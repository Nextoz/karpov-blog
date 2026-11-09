---
title: "DevOps, Platform Engineering and .NET Portfolio"
description: "Portfolio for Evgeny Karpov: Azure DevOps, .NET, Kubernetes, CI/CD, observability, platform engineering, public-sector IT and AI-assisted software development."
summary: "Selected experience across DevOps, platform engineering, .NET backend, cloud, CI/CD, observability and AI-assisted software development."
translationKey: "portfolio"
schemaType: "portfolio"
lastmod: 2026-11-10
url: "/en/projects/"
hidemeta: true
ShowReadingTime: false
ShowShareButtons: false
ShowWordCount: false
---

I am a software engineer with a strong .NET/backend background and a growing focus on DevOps, platform engineering, CI/CD, infrastructure, observability and production troubleshooting.

My professional profile sits between software development and operations: I understand application code, pipelines, cloud infrastructure, deployments, environments and the practical problems that appear when systems need to work reliably in production.

## Projects

{{< project-cards >}}

## Short overview

- **6+ years of professional software development experience**
- **Core stack:** .NET, C#, Azure DevOps, SQL, REST APIs, Blazor
- **DevOps/platform:** CI/CD, Docker, Kubernetes, Helm, KEDA, Bicep, Terraform
- **Operations:** deployments, troubleshooting, monitoring, logs, tracing, OpenTelemetry, OpenSearch
- **Domains:** public-sector IT, payroll systems, document automation, SAP integration

## Selected experience and projects

### twoday / Arbejdstilsynet — DevOps and Infrastructure

**Area:** DevOps, infrastructure, CI/CD, observability, public-sector IT

**Technologies:** Azure DevOps, Azure, Bicep, PowerShell DSC, IIS, OpenTelemetry, OpenSearch, C#/.NET

At twoday, I worked as a DevOps and infrastructure consultant for Arbejdstilsynet on a large .NET and Sitecore-based platform.

#### My contribution

- Built and improved CI/CD pipelines and deployment flows
- Helped establish and configure a new test environment
- Supported monitoring, troubleshooting and documentation
- Worked with infrastructure automation and environment setup
- Helped bridge development, operations and platform concerns

#### Why it matters

This experience shows my ability to work in an enterprise/public-sector environment where stability, documentation, controlled deployments and operational understanding matter.

### MyPaperFlow — Cloud DevOps, Kubernetes and SAP integration

**Area:** DevOps, cloud infrastructure, document automation, SAP integration

**Technologies:** Azure DevOps, Docker, Kubernetes, Helm, KEDA, Azure Service Bus, Azure, Bicep, Terraform, PostgreSQL, .NET

MyPaperFlow was a cloud-based document and invoice platform with integration to SAP Business One.

#### My contribution

- Built and maintained Azure DevOps CI/CD pipelines
- Worked with Docker images, Kubernetes deployments and Helm configuration
- Improved autoscaling with KEDA based on Azure Service Bus queues
- Worked with infrastructure as code using Bicep and Terraform
- Troubleshot deployments, identities, environments and cloud components

#### Why it matters

This project demonstrates practical DevOps work beyond writing YAML: building, deploying, scaling and operating real cloud services.

### DCAB — Public-sector .NET system

**Area:** Backend development, public-sector systems, data, registers

**Technologies:** .NET, C#, ASP.NET, Blazor, MSSQL, Azure DevOps, OpenShift, Elasticsearch

DCAB was a central register system within the Danish public housing sector. The project involved complex domain logic, data quality, integrations and structured delivery processes.

#### My contribution

- Developed backend and Blazor features
- Worked with REST APIs, domain logic and data models
- Supported release processes and Azure DevOps workflows
- Worked with testing, quality and .NET upgrades
- Contributed to data migration and system maintenance work

#### Why it matters

This project shows experience with serious business-critical software, domain complexity and collaboration in a larger development team.

### Visma Enterprise — Payroll systems and legacy modernization

**Area:** Payroll systems, business-critical software, legacy modernization

**Technologies:** C#, ASP.NET, DB2, MSSQL, GitHub, TeamCity, Octopus Deploy, COBOL

At Visma Enterprise, I developed and maintained functionality for payroll systems.

#### My contribution

- Developed and maintained payroll functionality in C#
- Worked on implementation of the new Danish holiday act
- Worked with tax-card integration and salary-related business logic
- Analyzed production issues and rewrote legacy COBOL logic
- Supported systems where correctness directly affected salary payments

#### Why it matters

Payroll systems require precision, responsibility and understanding of business-critical software. This experience shows that I can work with legacy systems, complex rules and high-stakes production logic.

### Scouts — scheduled agents that find what is relevant {#scouts}

**Area:** AI agents, automation, operating scheduled jobs

**Technologies:** Python, PowerShell, Windows Task Scheduler, LLM APIs, Markdown, Git

Scouts are a set of scheduled jobs that gather Copenhagen events, grocery offers, new AI research and job postings every morning and write the result as Markdown in my vault. The event scouts end up as ten cards a day in my app Vault Companion, where I swipe yes or no.

#### How it works

- A cheap model reads every dated event. A stronger model only judges the shortlist.
- Sources are measured: new sources get a 14-day trial, quiet sources are flagged, and dead ones are retired.
- My swipes change how strong an interest is, which sources stay, and what gets searched for next.
- A weekly report compares what the scouts found with an independent web search, so I can see what they missed.
- Every job writes a status file. A job only counts as run when its exit code and a fresh output say so. Being registered in Task Scheduler is not enough.

#### Why it matters

It is a small system in operation with the same problems as a large one: jobs that fail silently, sources that change, and costs that have to stay low. The expensive model is only used where it makes a difference.

### Ring app — my own health data without the vendor cloud {#ring-app}

**Area:** iOS, Bluetooth, data ownership

**Technologies:** Swift, iOS, Bluetooth LE, Shortcuts, GitHub Actions

**Code:** [github.com/Nextoz/PulseLoopiOS](https://github.com/Nextoz/PulseLoopiOS)

I use an inexpensive smart ring and wanted to own my data, so I forked the open-source app PulseLoop. The app talks to the ring directly over Bluetooth, with no account and no network calls to the vendor, and the data stays on the phone until I export it myself.

#### What my fork adds

- Seven days of history and steps per 15 minutes
- A 30-day raw log of the ring's Bluetooth frames, so I can debug the protocol
- Sleep windows that can be corrected by hand
- A Shortcuts action that passes the ring's data on to my vault

The changes are built with AI agents that I direct and review. Every release goes through CI on GitHub and is installed on my own phone.

#### Why it matters

The project shows that I can get into an unfamiliar codebase on a platform I do not work with daily and ship changes that are in use every day. It also shows how I think about data: it should live somewhere I control.

### Karpov Blog — Technical writing and personal platform {#karpov-blog}

**Area:** Technical communication, portfolio, SEO, static site

**Technologies:** Hugo, PaperMod, GitHub Pages, Markdown, GitHub Actions

This website is my personal technical blog and portfolio. I use it to write about software engineering, DevOps, AI, digitalization and technology policy.

#### My contribution

- Built and maintain the site with Hugo and GitHub Pages
- Set up content structure, SEO metadata and deployment workflow
- Use the site as a public writing platform and professional portfolio
- Write about technical topics in Danish and English with a practical engineering angle

#### Why it matters

Clear technical communication is part of senior engineering work. This site shows that I can explain technology, document ideas and think beyond code.

### Vintønden — technical SEO, GEO and WordPress for a local bar {#vintonden}

**Area:** Technical SEO, GEO (visibility in AI assistants), WordPress

**Technologies:** WordPress, PHP, WP-CLI, SSH, schema.org/JSON-LD, hreflang, Playwright

**Link:** [vintonden.dk](https://vintonden.dk/)

Vintønden is a bar in Frederiksberg that I do ongoing work for. I work directly in their WordPress site and take a backup before every change.

#### My contribution

- Structured data for the bar, its events and frequently asked questions
- Pages in Danish, English and Spanish with correct hreflang
- Metadata and sitemap clean-up, verified against the public site
- My own small WordPress plugins in PHP
- A GEO plan: which sources AI assistants use about the bar, where facts contradict each other across platforms, and a fixed visibility test

#### Why it matters

The project shows that I can turn technical analysis into concrete changes in production for a real local business, and that I can work directly with a client without a team around me.

## Security in practice {#security}

I am not a security specialist, but I treat security as part of the delivery:

- **Vulnerable dependencies:** On MyPaperFlow I followed up on CVEs in packages and dependencies through Microsoft Defender for Cloud.
- **No long-lived secrets:** I have used OIDC workload identity federation and Key Vault instead of keys stored in pipelines.
- **Reviewing with security in mind:** In a review of an infrastructure pull request, I found a personal access token that had leaked through the deployment history.
- **AI agents:** In my own agent systems, web pages and tool output are data, never instructions. External writes, secrets, destructive Git commands and production deployments need my explicit approval.
- **Community:** I attended OWASP Copenhagen in 2025 and 2026.
## What recruiters should understand

I am strongest in roles where backend development, DevOps and platform work meet.

I can contribute as:

- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer
- Backend Developer with DevOps/platform responsibility
- .NET Engineer close to infrastructure and delivery

My value is that I understand both application code and the systems that build, deploy, monitor and operate it.

<div class="contact-cta">

**Want to talk?** I am open to permanent roles and to freelance and contract work in Greater Copenhagen.

Write to [evgeny@karpov.dk](mailto:evgeny@karpov.dk) or on [LinkedIn](https://www.linkedin.com/in/evgenykarpov91/).

</div>
