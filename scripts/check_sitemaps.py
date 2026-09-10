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


def reject_generated_page(public: Path, relative: str) -> None:
    path = public / relative / "index.html"
    if path.exists():
        raise AssertionError(f"Unpublished page should not have been generated: {path}")


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

    kept_da = (
        "ai-agenter-skal-bruge-hukommelse",
        "ai-er-en-equalizer-indtil-den-rammer-banken",
        "ai-tokens-er-billige-regningen-er-det-ikke",
        "devops-er-ikke-en-pipeline",
        "fra-prompt-til-prototype-vaert",
        "jobsoegning-er-ogsaa-et-system",
        "obsidian-vault-selvforbedrende-graf",
    )
    kept_en = (
        "ai-agents-need-memory",
        "ai-is-an-equalizer-until-it-reaches-the-bank",
        "devops-is-not-a-pipeline",
        "from-prompt-to-prototype-vaert",
        "job-search-is-also-a-system",
        "my-obsidian-vault-got-a-small-research-department",
    )
    retired_da = (
        "ai-agenter-holder-ikke-sommerferie",
        "ai-agenter-skal-bruge-api-er",
        "ai-er-ikke-fyringsgrund",
        "ai-er-ikke-laengere-en-chatbot",
        "claude-fable-5-er-en-platformtest",
        "eu-ai-act-transparens-er-ikke-bare-en-popup",
        "project-glasswing",
    )
    retired_en = (
        "ai-agents-need-apis",
        "ai-is-not-grounds-for-dismissal",
        "ai-is-no-longer-a-chatbot",
        "claude-fable-5-is-a-platform-test",
        "eu-ai-act-in-practice-transparency-is-not-just-a-popup",
        "project-glasswing",
    )

    for slug in kept_da:
        require(da, f"{BASE}/posts/{slug}/", "da/sitemap.xml")
    for slug in kept_en:
        require(en, f"{BASE}/en/posts/{slug}/", "en/sitemap.xml")
    for slug in retired_da:
        reject(da, f"{BASE}/posts/{slug}/", "da/sitemap.xml")
        reject_generated_page(public, f"posts/{slug}")
    for slug in retired_en:
        reject(en, f"{BASE}/en/posts/{slug}/", "en/sitemap.xml")
        reject_generated_page(public, f"en/posts/{slug}")

    reject(da, f"{BASE}/search/", "da/sitemap.xml")
    reject(en, f"{BASE}/en/search/", "en/sitemap.xml")
    reject(en, f"{BASE}/en/om/", "en/sitemap.xml")
    reject(en, f"{BASE}/en/emner/", "en/sitemap.xml")
    reject(da, f"{BASE}/start/", "da/sitemap.xml")
    reject_generated_page(public, "start")

    home = read_html(public, "")
    en_home = read_html(public, "en")
    da_post = read_html(public, "posts/obsidian-vault-selvforbedrende-graf")
    en_post = read_html(public, "en/posts/my-obsidian-vault-got-a-small-research-department")
    unpaired_post = read_html(public, "posts/ai-tokens-er-billige-regningen-er-det-ikke")

    require_text(home, "Noter fra det, jeg bygger, lærer og prøver at forstå.", "Danish home")
    require_text(en_home, "Notes from what I build, learn and try to understand.", "English home")
    require_text(home, "Jeg vil selv tilbage i teksten.", "Danish editorial reset")
    require_text(en_home, "I want to return to the writing myself.", "English editorial reset")
    require_text(home, "images/profile.png", "Danish home portrait")
    require_text(home, "class=language-links", "Danish home language switch")
    require_text(home, "/karpov-blog/en/", "Danish home English target")
    if "Redaktørens valg" in home or "Editor's picks" in en_home:
        raise AssertionError("The retired editor-picks framing must not appear on either homepage")
    require_one_h1(home, "Danish home")
    require_one_h1(en_home, "English home")
    require_one_h1(unpaired_post, "Unpaired Danish post")

    require_text(da_post, f"{BASE}/en/posts/my-obsidian-vault-got-a-small-research-department/", "Danish post")
    require_text(en_post, f"{BASE}/posts/obsidian-vault-selvforbedrende-graf/", "English post")
    require_text(da_post, "class=language-links", "Danish paired-post language switch")
    require_text(en_post, "class=language-links", "English paired-post language switch")
    require_text(da_post, "author-note", "Danish author note")
    require_text(en_post, "author-note", "English author note")
    require_text(da_post, "AI skrev størstedelen af dette ældre indlæg", "Danish legacy disclosure")
    require_text(en_post, "AI wrote most of this older post", "English legacy disclosure")
    require_text(unpaired_post, "AI skrev størstedelen af dette ældre indlæg", "Unpaired legacy disclosure")
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

    print("Generated-site checks passed: editorial reset, retired pages, disclosures, sitemaps, headings, translations, JSON-LD, assets and internal links.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"Generated-site check failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
