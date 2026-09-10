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
