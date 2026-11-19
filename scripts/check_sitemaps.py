from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse


BASE = "https://karpov.dk"
BASE_PATH = ""
BASE_HOST = urlparse(BASE).netloc
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
            if parsed.netloc != BASE_HOST:
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

    require_text(home, "AI-rådgivning, .NET og DevOps i København", "Danish home")
    require_text(en_home, "AI consulting, .NET and DevOps in Copenhagen", "English home")
    # Review rounds 19 Nov 2026: business line, offer prices from the AI page, skip link, no digests on /posts/.
    require_text(home, "Karpov Consulting · CVR 44583445", "Danish home business line")
    require_text(home.replace(chr(34), ""), "class=offer-list", "Danish home offer block")
    require_text(home, "4.500 kr.", "Danish home assessment price")
    require_text(en_home, "DKK 4,500", "English home assessment price")
    for label, html in (("Danish home", home), ("English home", en_home)):
        require_text(html.replace(chr(34), ""), "class=skip-link href=#main-content", f"{label} skip link")
        require_text(html.replace(chr(34), ""), "id=main-content", f"{label} skip-link target")
    blog_list = read_html(public, "posts")
    if "Ugens AI-forskning:" in blog_list:
        raise AssertionError("The /posts/ list should leave out the AI-assembled digest")
    require_text(home, "images/profile.png", "Danish home portrait")
    require_text(home, "class=language-links", "Danish home language switch")
    require_text(home, f"{BASE_PATH}/en/", "Danish home English target")
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
    require_text(da_post, "AI skrev størstedelen af dette indlæg", "Danish legacy disclosure")
    require_text(en_post, "AI wrote most of this post", "English legacy disclosure")
    require_text(unpaired_post, "AI skrev størstedelen af dette indlæg", "Unpaired legacy disclosure")
    if "class=language-links" in unpaired_post or "/en/posts/ai-tokens-er-billige-regningen-er-det-ikke/" in unpaired_post:
        raise AssertionError("Unpaired Danish post must not advertise a missing English translation")

    for asset in (
        "images/profile.png",
        "images/karpov-mark.svg",
        "images/og/default.png",
        "images/og/default.en.png",
        "images/og/digest.png",
    ):
        if not (public / asset).exists():
            raise AssertionError(f"Missing generated asset: {asset}")

    portfolio = read_html(public, "projekter")
    en_portfolio = read_html(public, "en/projects")
    about = read_html(public, "om")
    llms = (public / "llms.txt").read_text(encoding="utf-8")

    # Share images: a real 1200x630 card per page, never the bare profile photo.
    require_text(home, f"{BASE}/images/og/default.png", "Danish home share image")
    require_text(en_home, f"{BASE}/images/og/default.en.png", "English home share image")
    require_text(unpaired_post, f"{BASE}/images/og/ai-tokens-er-billige-regningen-er-det-ikke.png", "Post share image")
    for label, html in (("Danish home", home), ("Unpaired Danish post", unpaired_post), ("Portfolio", portfolio)):
        if "og:image content=https://karpov.dk/images/profile.png" in html.replace(chr(34), ""):
            raise AssertionError(f"{label} still uses the profile photo as its share image")

    # Structured data: one job title everywhere, the right type per page.
    for label, html in (("Danish home", home), ("English home", en_home), ("About", about), ("Portfolio", portfolio)):
        require_text(html, "Senior Software Engineer", f"{label} job title")
    require_text(portfolio, "CollectionPage", "Portfolio structured data")
    require_text(en_portfolio, "CollectionPage", "English portfolio structured data")
    require_text(about, "ProfilePage", "About structured data")
    if "BlogPosting" in portfolio or "BlogPosting" in about:
        raise AssertionError("Portfolio and about pages must not be marked up as blog posts")
    require_text(en_home, "Freelance AI and DevOps consultant in Copenhagen", "English home structured data description")

    # The weekly digest has its own section and does not lead the home page.
    require_text(home, "id=research", "Danish home research section")
    if home.index("id=posts") > home.index("id=research"):
        raise AssertionError("The owner's posts must come before the research digest on the home page")

    # Portfolio content and llms.txt.
    for anchor in ("id=scouts", "id=ring-app", "id=sikkerhed", "id=vintonden"):
        require_text(portfolio, anchor, "Portfolio section")
    require_text(llms, "## Posts (Danish)", "llms.txt")
    require_text(llms, "## Weekly AI research digest", "llms.txt")
    require_text(llms, f"{BASE}/projekter/", "llms.txt")

    # AI consulting offer: both languages, in the sitemaps, with Service and FAQ structured data.
    require(da, f"{BASE}/ai-raadgivning/", "Danish sitemap")
    require(en, f"{BASE}/en/ai-consulting/", "English sitemap")
    service = read_html(public, "ai-raadgivning")
    en_service = read_html(public, "en/ai-consulting")
    for label, html in (("AI-raadgivning", service), ("AI consulting", en_service)):
        require_text(html, '"@type":"Service"', f"{label} structured data")
        require_text(html, '"@type":"FAQPage"', f"{label} FAQ structured data")
        require_text(html, '"priceCurrency":"DKK"', f"{label} offer currency")
        require_one_h1(html, label)
        check_json_ld(html, label)
    require_text(service, f"{BASE}/images/og/ai-raadgivning.png", "AI-raadgivning share image")
    require_text(en_service, f"{BASE}/images/og/ai-raadgivning.en.png", "AI consulting share image")
    require_text(llms, f"{BASE}/ai-raadgivning/", "llms.txt")
    require_text(llms, f"{BASE}/en/ai-consulting/", "llms.txt")
    require_text(home, "/ai-raadgivning/", "Danish home link to AI-raadgivning")
    require_text(service, "<title>AI-konsulent i København", "AI-raadgivning search title")
    require_text(en_service, "<title>AI consultant in Copenhagen", "AI consulting search title")

    # Project cards link to their write-ups.
    require_text(portfolio, "/posts/vault-companion/", "Portfolio Vault Companion card link")
    require_text(portfolio, "/posts/reverse-engineering-med-ai/", "Portfolio link to the ring post")
    require_text(portfolio, "https://github.com/Nextoz/repo-radar", "Portfolio Repo Radar card")
    require_text(en_portfolio, "https://github.com/Nextoz/repo-radar", "English portfolio Repo Radar card")

    # Tag and category lists stay out of the index and the sitemaps.
    for sitemap, locs, prefix in (("da/sitemap.xml", da, BASE), ("en/sitemap.xml", en, f"{BASE}/en")):
        for path in ("tags/", "tags/ai/", "categories/"):
            reject(locs, f"{prefix}/{path}", sitemap)
    for relative in ("tags", "tags/ai", "en/tags"):
        require_text(read_html(public, relative).replace(chr(34), ""), "name=robots content=noindex", f"{relative} robots")
    require_text(home.replace(chr(34), ""), "name=robots content=index", "Danish home robots")

    # Client conversion: a contact page, contact buttons where people decide, no job-seeking or
    # "new consultant" signals, a footer with contact details instead of the theme credit.
    require(da, f"{BASE}/kontakt/", "Danish sitemap")
    require(en, f"{BASE}/en/contact/", "English sitemap")
    contact = read_html(public, "kontakt")
    en_contact = read_html(public, "en/contact")
    en_about = read_html(public, "en/about")
    for label, html in (("Contact", contact), ("English contact", en_contact)):
        require_text(html, '"@type":"ContactPage"', f"{label} structured data")
        require_one_h1(html, label)
        check_json_ld(html, label)
    for label, html in (
        ("Danish home", home), ("English home", en_home), ("AI-raadgivning", service),
        ("AI consulting", en_service), ("Portfolio", portfolio), ("English portfolio", en_portfolio),
        ("Contact", contact), ("English contact", en_contact),
    ):
        flat = html.replace(chr(34), "")
        require_text(flat, "href=mailto:evgeny@karpov.dk?subject=", f"{label} contact button")
    for label, html, vintonden, contract in (("Danish home", home, "/projekter/#vintonden", "/projekter/#mypaperflow"), ("English home", en_home, "/en/projects/#vintonden", "/en/projects/#mypaperflow")):
        require_text(html.replace(chr(34), ""), "id=contact", f"{label} contact section")
        require_text(html, '"@type":"ProfessionalService"', f"{label} business structured data")
        require_text(html, vintonden, f"{label} Vintønden card")
        require_text(html, contract, f"{label} MyPaperFlow card")
        # Vintønden is the first project card: its link comes before the MyPaperFlow card's.
        if html.index(vintonden) > html.index(contract):
            raise AssertionError(f"{label}: the Vintønden card must come first")
    # Person.description is the bio, per language, not the blog tagline.
    require_text(home, '"description":"Senior software engineer og freelance-konsulent', "Danish Person bio")
    require_text(en_home, '"description":"Senior software engineer and freelance consultant', "English Person bio")
    for label, html in (("AI-raadgivning", service), ("AI consulting", en_service)):
        require_text(html, '"provider":{"@id":"https://karpov.dk/#business"}', f"{label} service provider")
        require_text(html, '"@type":"ProfessionalService"', f"{label} business node in the graph")
    for phrase in ("fastansættelse", "permanent roles", "ny som AI-rådgiver", "new as an AI consultant", "Det recruiters skal forstå", "What recruiters should understand"):
        for label, html in (("About", about), ("English about", en_about), ("Portfolio", portfolio),
                            ("English portfolio", en_portfolio), ("AI-raadgivning", service), ("AI consulting", en_service),
                            ("Danish home", home), ("English home", en_home), ("Contact", contact), ("English contact", en_contact)):
            if phrase in html:
                raise AssertionError(f"{label} still contains {phrase!r}")
    for label, html in (("Danish home", home), ("About", about)):
        footer = re.search(r"<footer class=\"?footer\"?>(.*?)</footer>", html, flags=re.DOTALL)
        if not footer:
            raise AssertionError(f"{label} has no footer")
        if "Powered by" in footer.group(1):
            raise AssertionError(f"{label} footer still shows the theme credit instead of contact details")
        require_text(footer.group(1).replace(chr(34), ""), "href=mailto:evgeny@karpov.dk", f"{label} footer email")
        # The footer override keeps the theme's scripts (menu scroll memory, theme toggle); scroll-to-top is switched off.
        flat = html.replace(chr(34), "")
        if "id=top-link" in flat:
            raise AssertionError(f"{label} should not show the scroll-to-top button")
        require_text(html, "menu-scroll-position", f"{label} footer menu script")
        if not re.search(r"setItem\([\"'`]pref-theme", html):
            raise AssertionError(f"{label} is missing the theme toggle script")
    require_text(about, "<title>Om Evgeny Karpov: freelance .NET-, DevOps- og AI-konsulent i København</title>", "About title without the doubled name")
    require_text(en_about, "<title>About Evgeny Karpov: freelance .NET, DevOps and AI consultant in Copenhagen</title>", "English about title without the doubled name")
    for label, html in (("About", about), ("English about", en_about)):
        if "class=toc" in html.replace(chr(34), ""):
            raise AssertionError(f"{label} should not show a table of contents")
    require_text(portfolio.replace(chr(34), ""), "id=kontraktopgaver", "Portfolio contract section")
    require_text(en_portfolio.replace(chr(34), ""), "id=contract-work", "English portfolio contract section")
    for label, html in (("Portfolio", portfolio), ("English portfolio", en_portfolio)):
        vintonden_heading = re.search(r"<h[23][^>]*id=\"?vintonden", html)
        twoday_heading = re.search(r"<h[23][^>]*>[^<]*twoday", html)
        if not vintonden_heading or not twoday_heading or vintonden_heading.start() > twoday_heading.start():
            raise AssertionError(f"{label}: Vintønden must come before the employer write-ups")
    require_text(llms, f"{BASE}/kontakt/", "llms.txt contact page")

    # Quick fixes after the 17 Nov re-review.
    require_text(home, "<title>Evgeny Karpov — freelance AI- og DevOps-konsulent i København</title>", "Danish home title says freelance")
    require_text(en_home, "<title>Evgeny Karpov — freelance AI and DevOps consultant, Copenhagen</title>", "English home title says freelance")
    for label, html in (("Unpaired Danish post", unpaired_post), ("Danish post", da_post), ("English post", en_post)):
        require_text(html.replace(chr(34), ""), "post-cta", f"{label} contact block")
        require_text(html.replace(chr(34), ""), "href=mailto:evgeny@karpov.dk?subject=", f"{label} contact button")
    require_text(da_post, "Har du en opgave?", "Danish post contact copy")
    require_text(en_post, "Got a project?", "English post contact copy")
    require_text(da_post, "/projekter/#kontraktopgaver", "Danish post contract-work button")
    require_text(en_post, "/en/projects/#contract-work", "English post contract-work button")
    digest = read_html(public, "posts/ugens-ai-research-2026-11-15")
    if "post-cta" in digest:
        raise AssertionError("AI-assembled digests should not get the contact block")
    if not re.search(r">\s*English\s*</a>", da_post):
        raise AssertionError("Danish post translation link should read 'English'")
    if not re.search(r">\s*Dansk\s*</a>", en_post):
        raise AssertionError("English post translation link should read 'Dansk'")
    for label, html in (("Danish home", home), ("English home", en_home), ("Portfolio", portfolio), ("English portfolio", en_portfolio)):
        for phrase in ("jobopslag", "job postings"):
            if phrase in html:
                raise AssertionError(f"{label} still mentions {phrase!r}")
    require_text(about, "Det kan du hyre mig til", "About hire heading")
    if "Site Reliability Engineering" in about:
        raise AssertionError("About should list tasks under the hire heading, not job titles")
    # Breadcrumbs: structured data starts at the home page; no lone "Start ›" crumb on top-level pages.
    def breadcrumb_names(html: str) -> list[str]:
        for block in re.findall(r'<script\s+type=["\']?application/ld\+json["\']?[^>]*>(.*?)</script>', html, flags=re.DOTALL):
            data = json.loads(block)
            if data.get("@type") == "BreadcrumbList":
                items = sorted(data["itemListElement"], key=lambda item: item["position"])
                if [item["position"] for item in items] != list(range(1, len(items) + 1)):
                    raise AssertionError("Breadcrumb positions must run 1..n")
                return [item["name"] for item in items]
        raise AssertionError("No BreadcrumbList found")
    if breadcrumb_names(service) != ["Forside", "AI-rådgivning til mindre virksomheder"]:
        raise AssertionError(f"AI-raadgivning breadcrumb is {breadcrumb_names(service)}")
    post_crumbs = breadcrumb_names(unpaired_post)
    if post_crumbs[:2] != ["Forside", "Blog"] or len(post_crumbs) != 3:
        raise AssertionError(f"Post breadcrumb should be Start, Blog, title; got {post_crumbs}")
    if breadcrumb_names(en_post)[0] != "Home":
        raise AssertionError("English breadcrumbs should start with Home")
    if "class=breadcrumbs" in service.replace(chr(34), ""):
        raise AssertionError("Top-level pages should not show a breadcrumb")
    require_text(unpaired_post.replace(chr(34), ""), "class=breadcrumbs", "Post breadcrumb")

    check_json_ld(home, "Danish home")
    check_json_ld(en_home, "English home")
    check_json_ld(portfolio, "Portfolio")
    check_json_ld(en_portfolio, "English portfolio")
    check_json_ld(about, "About")
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
