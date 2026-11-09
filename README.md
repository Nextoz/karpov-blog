# Karpov Blog

Personal portfolio and technical blog for **Evgeny Karpov**.

The site publishes engineering notes about DevOps, platform engineering, .NET, observability, AI systems and the work required to make software reliable in production.

Live site:

https://karpov.dk/

## Stack

- Hugo
- PaperMod theme
- GitHub Pages
- GitHub Actions
- Markdown

## Content structure

content/
  start/       Homepage
  om/          About page
  projekter/   Portfolio and project cases
  posts/       Blog posts
  search/      Search page

## Local development

Install Hugo, then run:

hugo server

Open the local URL shown in the terminal.

## Deployment

The site is deployed through GitHub Actions to GitHub Pages.

Changes merged into `master` trigger a new deployment automatically.

Every pull request builds the production site and validates:

- sitemap coverage
- internal links and generated assets
- bilingual translation targets
- one primary heading on representative pages
- JSON-LD parsing
- required identity and favicon assets
- share images, structured data types, the home page order and llms.txt

Run the same checks locally with:

```powershell
hugo --gc --minify --cleanDestinationDir --baseURL "https://karpov.dk/"
python scripts/check_sitemaps.py public
```

## SEO focus

The site is structured around long-tail professional keywords such as:

- DevOps Engineer Copenhagen
- Platform Engineer Copenhagen
- Azure DevOps consultant
- .NET DevOps engineer
- Kubernetes and CI/CD
- Observability and platform engineering
- AI-assisted software engineering

## Share images

Every page gets a 1200x630 share image from `static/images/og/`. `layouts/partials/og-image.html` picks the post's own image, the shared digest image or the site default.

After adding or retitling a post, regenerate and commit the images (Windows):

```powershell
pwsh -NoProfile -File scripts/make_og_images.ps1
```

A post without its own image still gets the site default, so the weekly digest pipeline needs no extra step.

## Search engines and AI assistants

- `layouts/home.llms.txt` builds `/llms.txt`: who the author is, the main pages, the author's posts and, separately, the AI-assembled weekly digest.
- Structured data comes from `layouts/partials/templates/schema_json.html`; the Person (name, job title, profiles) is defined once in `layouts/partials/schema-person.html` and `hugo.toml` (`params.schema`).
- Search Console and Bing Webmaster Tools verification values go in `hugo.toml` under `params.analytics.google` and `params.analytics.bing`.
