from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse


BASE = "https://nextoz.github.io/karpov-blog"
BASE_PATH = "/karpov-blog"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for attr in ("href", "src"):
            value = values.get(attr)
            if value:
                self.links.append((attr, value))


def read_locs(path: Path) -> set[str]:
    if not path.exists():
        raise AssertionError(f"Missing sitemap: {path}")
    root = ET.parse(path).getroot()
    return {loc.text or "" for loc in root.findall("sm:url/sm:loc", NS)}


def require(locs: set[str], url: str, sitemap: str) -> None:
    if url not in locs:
        raise AssertionError(f"{sitemap} is missing {url}")


def reject(locs: set[str], url: str, sitemap: str) -> None:
    if url in locs:
        raise AssertionError(f"{sitemap} should not include {url}")


def read_html(public: Path, relative: str) -> str:
    path = public / relative / "index.html" if relative else public / "index.html"
    if not path.exists():
        raise AssertionError(f"Missing generated page: {path}")
    return path.read_text(encoding="utf-8")


def require_text(haystack: str, needle: str, label: str) -> None:
    if needle not in haystack:
        raise AssertionError(f"{label} is missing {needle!r}")


def require_one_h1(html: str, label: str) -> None:
    count = len(re.findall(r"<h1(?:\s|>)", html, flags=re.IGNORECASE))
    if count != 1:
        raise AssertionError(f"{label} should contain exactly one h1, found {count}")


def generated_target(public: Path, path: str) -> Path | None:
    if path == BASE_PATH:
        path = BASE_PATH + "/"
    if not path.startswith(BASE_PATH + "/"):
        return None

    relative = path.removeprefix(BASE_PATH + "/").lstrip("/")
    candidate = public / relative
    if path.endswith("/"):
        candidate = candidate / "index.html"
    return candidate


def check_internal_links(public: Path) -> None:
    failures: list[str] = []
    checked: set[str] = set()

    for html_path in public.rglob("index.html"):
        relative = html_path.relative_to(public).as_posix()
        page_path = "/" if relative == "index.html" else "/" + relative.removesuffix("index.html")
        page_url = BASE + page_path
        parser = LinkCollector()
        parser.feed(html_path.read_text(encoding="utf-8"))

        for attr, raw in parser.links:
            if raw.startswith(("mailto:", "tel:", "data:", "javascript:", "#")):
                continue
            absolute = urljoin(page_url, raw)
            parsed = urlparse(absolute)
            if parsed.netloc != "nextoz.github.io":
                continue
            key = f"{parsed.path}|{attr}"
            if key in checked:
                continue
            checked.add(key)
            target = generated_target(public, parsed.path)
            if target is not None and not target.exists():
                failures.append(f"{relative}: {raw} -> missing {target.relative_to(public)}")

    if failures:
        sample = "\n".join(failures[:20])
        raise AssertionError(f"Broken internal links/assets ({len(failures)}):\n{sample}")


def check_json_ld(html: str, label: str) -> None:
    blocks = re.findall(
        r'<script\s+type=["\']?application/ld\+json["\']?[^>]*>(.*?)</script>',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not blocks:
        raise AssertionError(f"{label} has no JSON-LD")
    for block in blocks:
        json.loads(block)


def main() -> int:
    public = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("public")
    da = read_locs(public / "da" / "sitemap.xml")
    en = read_locs(public / "en" / "sitemap.xml")

    require(da, f"{BASE}/posts/ai-agenter-skal-bruge-api-er/", "da/sitemap.xml")
    require(da, f"{BASE}/posts/devops-er-ikke-en-pipeline/", "da/sitemap.xml")
    require(en, f"{BASE}/en/posts/ai-agents-need-apis/", "en/sitemap.xml")
    require(en, f"{BASE}/en/posts/devops-is-not-a-pipeline/", "en/sitemap.xml")
    require(en, f"{BASE}/en/posts/eu-ai-act-in-practice-transparency-is-not-just-a-popup/", "en/sitemap.xml")
    require(da, f"{BASE}/posts/claude-fable-5-er-en-platformtest/", "da/sitemap.xml")
    require(en, f"{BASE}/en/posts/claude-fable-5-is-a-platform-test/", "en/sitemap.xml")

    reject(da, f"{BASE}/search/", "da/sitemap.xml")
    reject(en, f"{BASE}/en/search/", "en/sitemap.xml")
    reject(en, f"{BASE}/en/om/", "en/sitemap.xml")
    reject(en, f"{BASE}/en/emner/", "en/sitemap.xml")

    home = read_html(public, "")
    en_home = read_html(public, "en")
    da_post = read_html(public, "posts/ai-agenter-skal-bruge-api-er")
    en_post = read_html(public, "en/posts/ai-agents-need-apis")
    unpaired_post = read_html(public, "posts/ai-tokens-er-billige-regningen-er-det-ikke")
    da_claude_post = read_html(public, "posts/claude-fable-5-er-en-platformtest")
    en_claude_post = read_html(public, "en/posts/claude-fable-5-is-a-platform-test")

    require_text(home, "Software, der skal virke i virkeligheden.", "Danish home")
    require_text(en_home, "Software that has to work in the real world.", "English home")
    require_text(home, "images/profile.png", "Danish home portrait")
    require_text(home, "class=language-links", "Danish home language switch")
    require_text(home, "/karpov-blog/en/", "Danish home English target")
    require_text(home, "Redaktørens valg", "Danish featured section")
    require_text(en_home, "Editor's picks", "English featured section")
    require_one_h1(home, "Danish home")
    require_one_h1(en_home, "English home")
    require_one_h1(unpaired_post, "Unpaired Danish post")

    require_text(da_post, f"{BASE}/en/posts/ai-agents-need-apis/", "Danish post")
    require_text(en_post, f"{BASE}/posts/ai-agenter-skal-bruge-api-er/", "English post")
    require_text(da_claude_post, f"{BASE}/en/posts/claude-fable-5-is-a-platform-test/", "Danish Claude post")
    require_text(en_claude_post, f"{BASE}/posts/claude-fable-5-er-en-platformtest/", "English Claude post")
    require_text(en_claude_post, "claude-fable-5-platform-signal-en.svg", "English Claude post")
    require_text(en_claude_post, "ai-agent-adoption-gap-2026-en.svg", "English Claude post")
    require_text(da_post, "class=language-links", "Danish paired-post language switch")
    require_text(en_post, "class=language-links", "English paired-post language switch")
    require_text(da_post, "author-note", "Danish author note")
    require_text(en_post, "author-note", "English author note")
    if "class=language-links" in unpaired_post or "/en/posts/ai-tokens-er-billige-regningen-er-det-ikke/" in unpaired_post:
        raise AssertionError("Unpaired Danish post must not advertise a missing English translation")

    for asset in (
        "images/profile.png",
        "images/karpov-mark.svg",
    ):
        if not (public / asset).exists():
            raise AssertionError(f"Missing generated asset: {asset}")

    check_json_ld(home, "Danish home")
    check_json_ld(unpaired_post, "Unpaired Danish post")
    check_internal_links(public)

    print("Generated-site checks passed: sitemaps, headings, translations, JSON-LD, assets and internal links.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"Generated-site check failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
