"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver) which karpov.dk pages changed.

Runs after a deploy. Reads the live sitemaps, keeps URLs whose <lastmod> is within the last
--days days, and submits them in one request to https://api.indexnow.org/indexnow.
The key is public by design: it is served at https://karpov.dk/<key>.txt so engines can verify
that the submitter controls the site.

Never fails the workflow: problems are printed as warnings and the script exits 0.

Usage: python scripts/indexnow.py [--days 3] [--dry-run]
"""
import argparse
import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

HOST = "karpov.dk"
KEY = "286e4f19be84c04a35801ef21c8836fb"
SITEMAPS = [f"https://{HOST}/sitemap.xml", f"https://{HOST}/en/sitemap.xml"]
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
UA = "karpov-blog-indexnow/1.0"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def entries(url, seen):
    if url in seen:
        return []
    seen.add(url)
    root = ET.fromstring(fetch(url))
    if root.tag.endswith("sitemapindex"):
        out = []
        for loc in root.findall("sm:sitemap/sm:loc", NS):
            out += entries(loc.text.strip(), seen)
        return out
    out = []
    for u in root.findall("sm:url", NS):
        loc = u.findtext("sm:loc", default="", namespaces=NS).strip()
        lastmod = u.findtext("sm:lastmod", default="", namespaces=NS).strip()
        if loc:
            out.append((loc, lastmod))
    return out


def parse_date(s):
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    try:
        key_live = fetch(f"https://{HOST}/{KEY}.txt").decode().strip()
    except Exception as e:  # noqa: BLE001 - report and stop quietly
        print(f"::warning::IndexNow key file not reachable yet: {e}")
        return 0
    if key_live != KEY:
        print("::warning::IndexNow key file content does not match the key; nothing submitted")
        return 0

    seen, urls = set(), {}
    for sm in SITEMAPS:
        try:
            for loc, lastmod in entries(sm, seen):
                urls[loc] = lastmod
        except Exception as e:  # noqa: BLE001
            print(f"::warning::could not read {sm}: {e}")

    since = datetime.now(timezone.utc) - timedelta(days=a.days)
    changed = sorted(u for u, lm in urls.items() if (d := parse_date(lm)) and d >= since and u.startswith(f"https://{HOST}/"))
    print(f"{len(urls)} URLs in sitemaps, {len(changed)} changed in the last {a.days} days")
    for u in changed:
        print("  " + u)
    if not changed or a.dry_run:
        return 0

    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": changed[:10000]}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA})
    for attempt in (1, 2):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f"IndexNow answered HTTP {r.status}")
                return 0
        except urllib.error.HTTPError as e:
            print(f"::warning::IndexNow answered HTTP {e.code}: {e.read()[:300]!r}")
            if e.code not in (429, 500, 502, 503) or attempt == 2:
                return 0
        except Exception as e:  # noqa: BLE001
            print(f"::warning::IndexNow request failed: {e}")
            if attempt == 2:
                return 0
        time.sleep(20)
    return 0


if __name__ == "__main__":
    sys.exit(main())
