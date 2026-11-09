---
title: "DevOps, Platform Engineering og .NET Portfolio"
description: "Portfolio for Evgeny Karpov: Azure DevOps, .NET, Kubernetes, CI/CD, observability, platform engineering, offentlig IT og AI-assisteret softwareudvikling."
summary: "Udvalgte projekter og erfaringer inden for DevOps, platform engineering, .NET backend, cloud, CI/CD, observability og AI-assisteret softwareudvikling."
translationKey: "portfolio"
schemaType: "portfolio"
lastmod: 2026-11-09
hidemeta: true
ShowReadingTime: false
ShowShareButtons: false
ShowWordCount: false
---

Jeg er software engineer med en stærk .NET/backend-baggrund og et nyere fokus på DevOps, platform engineering, CI/CD, infrastruktur, observability og produktionstroubleshooting.

Min professionelle profil ligger i krydsfeltet mellem softwareudvikling og drift: jeg forstår både applikationskode, pipelines, cloud-infrastruktur, deployments, miljøer og de praktiske problemer, der opstår, når systemer skal fungere i produktion.

## Projekter

{{< project-cards >}}

## Kort overblik

- **6+ års professionel erfaring med softwareudvikling**
- **Kernestack:** .NET, C#, Azure DevOps, SQL, REST APIs, Blazor
- **DevOps/platform:** CI/CD, Docker, Kubernetes, Helm, KEDA, Bicep, Terraform
- **Drift:** deployments, fejlsøgning, monitoring, logs, tracing, OpenTelemetry, OpenSearch
- **Domæner:** offentlig IT, lønsystemer, dokumentautomatisering, SAP-integration

---

## twoday / Arbejdstilsynet — DevOps og Infrastruktur

**Område:** DevOps, infrastruktur, CI/CD, observability, offentlig IT  
**Teknologier:** Azure DevOps, Azure, Bicep, PowerShell DSC, IIS, OpenTelemetry, OpenSearch, C#/.NET

Hos twoday arbejdede jeg som DevOps- og infrastrukturkonsulent for Arbejdstilsynet på en større .NET- og Sitecore-baseret platform.

### Mit bidrag

- Byggede og forbedrede CI/CD pipelines og deployment flows
- Var med til at etablere og konfigurere et nyt testmiljø
- Understøttede monitoring, fejlsøgning og dokumentation
- Arbejdede med infrastrukturautomatisering og miljøopsætning
- Var med til at bygge bro mellem udvikling, drift og platform

### Hvorfor det er relevant

Erfaringen viser, at jeg kan arbejde i enterprise- og offentlig IT, hvor stabilitet, dokumentation, kontrollerede deployments og driftsforståelse er afgørende.

---

## MyPaperFlow — Cloud DevOps, Kubernetes og SAP-integration

**Område:** DevOps, cloud-infrastruktur, dokumentautomatisering, SAP-integration  
**Teknologier:** Azure DevOps, Docker, Kubernetes, Helm, KEDA, Azure Service Bus, Azure, Bicep, Terraform, PostgreSQL, .NET

MyPaperFlow var en cloud-baseret dokument- og fakturaplatform med integration til SAP Business One.

### Mit bidrag

- Byggede og vedligeholdt Azure DevOps CI/CD-pipelines
- Arbejdede med Docker images, Kubernetes deployments og Helm-konfiguration
- Forbedrede autoskalering med KEDA baseret på Azure Service Bus queues
- Arbejdede med infrastructure as code i Bicep og Terraform
- Fejlsøgte deployments, identities, miljøer og cloud-komponenter

### Hvorfor det er relevant

Projektet viser praktisk DevOps-erfaring med rigtige cloud-systemer. Ikke kun YAML, men arbejdet med at bygge, deploye, skalere og drifte services i rigtige miljøer.

---

## DCAB — Offentligt .NET-system

**Område:** Backendudvikling, offentlig IT, data, registre  
**Teknologier:** .NET, C#, ASP.NET, Blazor, MSSQL, Azure DevOps, OpenShift, Elasticsearch

DCAB var et centralt registersystem inden for den almene boligsektor. Projektet involverede kompleks domænelogik, datakvalitet, integrationer og strukturerede leveranceprocesser.

### Mit bidrag

- Udviklede backend- og Blazor-features
- Arbejdede med REST APIs, domænelogik og datamodeller
- Understøttede releaseprocesser og Azure DevOps workflows
- Arbejdede med test, kvalitet og .NET-opgraderinger
- Bidrog til datamigrering og systemvedligeholdelse

### Hvorfor det er relevant

Projektet viser erfaring med forretningskritisk software, komplekse domæner og samarbejde i et større udviklingsteam.

---

## Visma Enterprise — Lønsystemer og legacy-modernisering

**Område:** Lønsystemer, forretningskritisk software, legacy-modernisering  
**Teknologier:** C#, ASP.NET, DB2, MSSQL, GitHub, TeamCity, Octopus Deploy, COBOL

Hos Visma Enterprise udviklede og vedligeholdt jeg funktionalitet til lønsystemer.

### Mit bidrag

- Udviklede og vedligeholdt lønfunktionalitet i C#
- Arbejdede med implementering af den nye ferielov
- Arbejdede med eSkattekort-integration og lønrelateret forretningslogik
- Analyserede produktionsfejl og omskrev legacy COBOL-logik
- Understøttede systemer hvor korrekthed direkte påvirkede lønudbetalinger

### Hvorfor det er relevant

Lønsystemer kræver præcision, ansvarlighed og forståelse for forretningskritisk software. Erfaringen viser, at jeg kan arbejde med legacy, komplekse regler og produktionsnær fejlsøgning.

---

## Scouts — planlagte agenter, der finder det relevante {#scouts}

**Område:** AI-agenter, automatisering, drift af planlagte jobs  
**Teknologier:** Python, PowerShell, Windows Task Scheduler, LLM API'er, Markdown, Git

Scouts er et sæt planlagte jobs, der hver morgen samler københavnske events, dagligvaretilbud, ny AI-research og jobopslag og skriver resultatet som Markdown i mit vault. Event-scouterne ender som ti kort om dagen i min app Vault Companion, hvor jeg swiper ja eller nej.

### Sådan virker det

- En billig model læser alle daterede events. En stærkere model vurderer kun shortlisten.
- Kilderne bliver målt: nye kilder prøves i 14 dage, stille kilder markeres, og døde kilder tages ud.
- Mine swipes ændrer, hvor stærk en interesse er, hvilke kilder der bliver, og hvad der søges efter næste gang.
- En ugentlig rapport sammenligner scouternes fund med en uafhængig websøgning, så jeg kan se, hvad de overså.
- Hvert job skriver en statusfil. Et job tæller først som kørt, når exit code og et friskt output siger det. At det står i Task Scheduler, er ikke nok.

### Hvorfor det er relevant

Det er et lille system i drift med de samme problemer som et stort: jobs, der fejler stille, kilder, der ændrer sig, og omkostninger, der skal holdes nede. Den dyre model bruges kun dér, hvor den gør en forskel.

---

## Ring-app — egne sundhedsdata uden leverandørens cloud {#ring-app}

**Område:** iOS, Bluetooth, dataejerskab  
**Teknologier:** Swift, iOS, Bluetooth LE, Shortcuts, GitHub Actions

**Kode:** [github.com/Nextoz/PulseLoopiOS](https://github.com/Nextoz/PulseLoopiOS)

Jeg bruger en billig smart ring og ville eje mine egne data. Derfor har jeg forket open source-appen PulseLoop. Appen taler direkte med ringen over Bluetooth, uden konto og uden netværkskald til leverandøren, og data bliver på telefonen, indtil jeg selv eksporterer dem.

### Det har jeg tilføjet i min fork

- Syv dages historik og skridt pr. 15 minutter
- En rå log over ringens Bluetooth-frames i 30 dage, så jeg kan fejlsøge protokollen
- Søvnvinduer, der kan rettes i hånden
- En Shortcuts-handling, der sender ringens data videre til mit vault

Ændringerne er bygget med AI-agenter, som jeg styrer og reviewer. Hver release går gennem CI på GitHub og installeres på min egen telefon.

### Hvorfor det er relevant

Projektet viser, at jeg kan sætte mig ind i en fremmed kodebase på en platform, jeg ikke arbejder med til daglig, og levere ændringer, der er i brug hver dag. Det viser også, hvordan jeg tænker om data: de skal ligge et sted, jeg selv kontrollerer.

---

## Karpov Blog — Teknisk formidling og personlig platform {#karpov-blog}

**Område:** Teknisk formidling, portfolio, SEO, statisk website  
**Teknologier:** Hugo, PaperMod, GitHub Pages, Markdown, GitHub Actions

Denne hjemmeside er min personlige tekniske blog og portfolio. Jeg bruger den til at skrive om software engineering, DevOps, AI, digitalisering og teknologipolitik.

### Mit bidrag

- Bygger og vedligeholder siden med Hugo og GitHub Pages
- Arbejder med indholdsstruktur, SEO metadata og deployment workflow
- Bruger siden som offentlig skriveplatform og professionel portfolio
- Skriver om tekniske emner på dansk med en praktisk engineering-vinkel

### Hvorfor det er relevant

Klar teknisk formidling er en del af senior engineering-arbejde. Siden viser, at jeg kan forklare teknologi, dokumentere idéer og tænke ud over selve koden.

---

## Vintønden — teknisk SEO, GEO og WordPress for en lokal bar {#vintonden}

**Område:** Teknisk SEO, GEO (synlighed i AI-assistenter), WordPress  
**Teknologier:** WordPress, PHP, WP-CLI, SSH, schema.org/JSON-LD, hreflang, Playwright

**Link:** [vintonden.dk](https://vintonden.dk/)

Vintønden er en bar på Frederiksberg, som jeg løbende løser opgaver for. Jeg arbejder direkte i deres WordPress-site og tager backup før hver ændring.

### Mit bidrag

- Structured data til baren, events og ofte stillede spørgsmål
- Sider på dansk, engelsk og spansk med korrekt hreflang
- Oprydning i metadata og sitemap, verificeret mod det offentlige site
- Egne små WordPress-plugins i PHP
- En GEO-plan: hvilke kilder AI-assistenter bruger om baren, hvor fakta modsiger hinanden på tværs af platforme, og en fast test af synligheden

### Hvorfor det er relevant

Projektet viser, at jeg kan omsætte teknisk analyse til konkrete ændringer i produktion for en rigtig lokal virksomhed, og at jeg kan arbejde direkte med en kunde uden et team omkring mig.

---

## Sikkerhed i praksis {#sikkerhed}

Jeg er ikke sikkerhedsspecialist, men jeg arbejder med sikkerhed som en del af leverancen:

- **Sårbarheder i afhængigheder:** På MyPaperFlow fulgte jeg løbende op på CVE'er i pakker og afhængigheder via Microsoft Defender for Cloud.
- **Ingen langlivede secrets:** Jeg har brugt OIDC workload identity federation og Key Vault i stedet for nøgler, der ligger i pipelines.
- **Review med sikkerhedsbriller:** I et review af en infrastruktur-PR fandt jeg et personal access token, der var lækket gennem deployment-historikken.
- **AI-agenter:** I mine egne agentsystemer er websider og tool-output data, aldrig instruktioner. Eksterne skrivninger, secrets, destruktive Git-kommandoer og deployments til produktion kræver min udtrykkelige godkendelse.
- **Fællesskab:** Jeg har deltaget i OWASP Copenhagen i 2025 og 2026.

---

## Det recruiters skal forstå

Jeg er stærkest i roller, hvor backendudvikling, DevOps og platformarbejde mødes.

Jeg kan bidrage som:

- DevOps Engineer
- Platform Engineer
- Site Reliability Engineer
- Backend Developer med DevOps/platform-ansvar
- .NET Engineer tæt på infrastruktur og delivery

Min værdi er, at jeg både forstår applikationskode og de systemer, der skal bygge, deploye, monitorere og drifte den.

<div class="contact-cta">

**Skal vi tale sammen?** Jeg er åben for fastansættelse og for freelance- og kontraktopgaver i Storkøbenhavn.

Skriv til [evgeny@karpov.dk](mailto:evgeny@karpov.dk) eller på [LinkedIn](https://www.linkedin.com/in/evgenykarpov91/).

</div>
