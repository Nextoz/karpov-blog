from pathlib import Path
import sys
import xml.etree.ElementTree as ET


BASE = "https://nextoz.github.io/karpov-blog"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


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
    path = public / relative / "index.html"
    if not path.exists():
        raise AssertionError(f"Missing generated page: {path}")
    return path.read_text(encoding="utf-8")


def require_text(haystack: str, needle: str, label: str) -> None:
    if needle not in haystack:
        raise AssertionError(f"{label} is missing {needle!r}")


def main() -> int:
    public = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("public")
    da = read_locs(public / "da" / "sitemap.xml")
    en = read_locs(public / "en" / "sitemap.xml")

    require(da, f"{BASE}/posts/ai-agenter-skal-bruge-api-er/", "da/sitemap.xml")
    require(da, f"{BASE}/posts/devops-er-ikke-en-pipeline/", "da/sitemap.xml")
    require(en, f"{BASE}/en/posts/ai-agents-need-apis/", "en/sitemap.xml")
    require(en, f"{BASE}/en/posts/devops-is-not-a-pipeline/", "en/sitemap.xml")
    require(en, f"{BASE}/en/posts/eu-ai-act-in-practice-transparency-is-not-just-a-popup/", "en/sitemap.xml")

    reject(da, f"{BASE}/search/", "da/sitemap.xml")
    reject(en, f"{BASE}/en/search/", "en/sitemap.xml")
    reject(en, f"{BASE}/en/om/", "en/sitemap.xml")
    reject(en, f"{BASE}/en/emner/", "en/sitemap.xml")

    da_post = read_html(public, "posts/ai-agenter-skal-bruge-api-er")
    en_post = read_html(public, "en/posts/ai-agents-need-apis")
    require_text(da_post, f"{BASE}/en/posts/ai-agents-need-apis/", "Danish post")
    require_text(en_post, f"{BASE}/posts/ai-agenter-skal-bruge-api-er/", "English post")
    require_text(en_post, "global-language-switch", "English post")
    require_text(en_post, ".appendChild(", "English language switch")
    require_text(da_post, "author-note", "Danish author note")
    require_text(en_post, "author-note", "English author note")

    print("Sitemap checks passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"Sitemap check failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
