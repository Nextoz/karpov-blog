---
title: "EU AI Act i praksis: transparens er ikke bare en pop-up"
date: 2026-05-19
lastmod: 2026-05-19
draft: true
description: "EU AI Act gør transparens til et praktisk produkt-, DevOps- og arkitekturproblem. Her er hvad teams bør begynde at forberede nu."
summary: "Fra 2. august 2026 begynder centrale transparensregler i EU AI Act at gælde. Det lyder som jura, men i praksis bliver det også et spørgsmål om UI, logs, metadata, audit trails og drift."
tags: ["AI", "EU AI Act", "DevOps", "Platform Engineering", "Regulering"]
categories: ["Teknologipolitik"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

EU AI Act lyder som noget man kan parkere hos Legal.

Det tror jeg er en fejl.

Fra **2. august 2026** begynder de centrale transparensregler i EU AI Act at gælde. Det betyder blandt andet, at mennesker i EU skal informeres, når de interagerer med AI-systemer eller bliver eksponeret for visse typer AI-genereret eller manipuleret indhold.

Det kan lyde som en pop-up.

Men hvis man bygger software, ved man godt at "bare lige vise en besked" sjældent er hele opgaven.

Transparens bliver et produktproblem. Et UX-problem. Et compliance-problem. Og meget hurtigt også et DevOps- og arkitekturproblem.

## Hvorfor det betyder noget nu

EU-Kommissionen åbnede den 8. maj 2026 en høring om udkast til retningslinjer for transparensforpligtelserne under AI Act. Formålet er at afklare, hvordan reglerne skal forstås, før de begynder at gælde.

Det vigtige er ikke kun datoen. Det vigtige er at virksomheder nu bør begynde at stille nogle meget konkrete spørgsmål:

- Hvor bruger vi AI i vores systemer?
- Hvornår møder brugeren AI direkte?
- Hvornår producerer vi AI-genereret indhold?
- Hvordan markerer vi det?
- Hvor ligger ansvaret i vores organisation?
- Kan vi dokumentere det bagefter?

Hvis svaret er "det må vi finde ud af senere", så er senere ved at være nu.

## Transparens er ikke kun tekst i UI

Den nemme version af transparens er:

> "Denne besked er genereret med AI."

Det kan være fint. Men det er kun overfladen.

Den svære version er:

- Hvilket system genererede indholdet?
- Hvilken model eller leverandør blev brugt?
- Hvilken version af prompt, policy eller workflow gjaldt?
- Blev der brugt menneskelig godkendelse?
- Kan man se det i logs?
- Kan man forklare det til en bruger, en kunde eller en myndighed?

Det er her, emnet holder op med kun at være jura og begynder at ligne almindeligt godt softwarearbejde.

## Machine-readable marking er engineering

EU-Kommissionen nævner, at udbydere skal tilføje maskinlæsbare markeringer, så AI-genereret eller manipuleret indhold kan opdages.

Det er en sætning der burde få platform teams til at spidse ører.

For maskinlæsbar markering er ikke bare "vi skriver noget i bunden af siden". Det kan betyde metadata, vandmærkning, API-felter, audit logs, content provenance eller andre tekniske mekanismer der gør det muligt at identificere AI-output på tværs af systemer.

Og så kommer de klassiske spørgsmål:

- Hvor gemmer vi markeringen?
- Overlever den eksport, copy/paste og integrationer?
- Hvad sker der når data sendes videre til et andet system?
- Hvordan tester vi at markeringen stadig findes efter næste release?
- Hvem ejer fejlen hvis den forsvinder i en pipeline?

Der er meget lidt "bare en pop-up" over det.

## DevOps-vinklen

For mig er det interessante, at AI governance ofte bliver talt om som noget abstrakt. Men i praksis lander meget af arbejdet hos de mennesker der bygger og driver systemerne.

Hvis et team bruger AI i produktion, bør man kunne svare på:

- Hvilke miljøer bruger AI-funktioner?
- Hvilke secrets og API-nøgler bruges?
- Hvilke logs indeholder AI-relaterede hændelser?
- Hvilke dashboards viser fejlrate, latency og model-afhængige flows?
- Hvilke deployment gates beskytter mod at transparens forsvinder?
- Hvilke rollback-planer findes hvis en AI-feature opfører sig forkert?

Det er ikke glamourøst. Det er ikke demo-venligt.

Men det er den slags arbejde der afgør, om AI bliver en robust del af systemet eller endnu en feature, som alle er begejstrede for indtil nogen spørger: "hvem har egentlig ansvar for den?"

## En praktisk tjekliste for danske teams

Hvis jeg sad i et produkt- eller platformteam, ville jeg starte her:

### 1. Lav et AI-inventar

Find alle steder hvor organisationen bruger AI:

- Chatbots
- Dokumentgenerering
- Kundesupport
- Søgefunktioner
- Anbefalingssystemer
- Interne agent-workflows
- Kode- og dokumentationsautomatisering
- Billed-, video- eller lydgenerering

Man kan ikke lave transparens for systemer man ikke ved findes.

### 2. Skeln mellem intern og brugerrettet AI

Ikke alle AI-features har samme risiko eller samme brugerforventning.

En intern udviklerassistent er noget andet end en borgerrettet chatbot. Et resumeværktøj er noget andet end et system der påvirker en afgørelse, en ansøgning eller en kundes mulighed for hjælp.

Lav en enkel kategorisering før det bliver for akademisk:

- Intern hjælp
- Brugerrettet interaktion
- AI-genereret indhold
- AI-assisterede beslutninger
- Højere risiko / kræver særlig vurdering

### 3. Design transparens ind i produktet

Transparens skal ikke være en sidste-øjebliks label.

Spørg i designfasen:

- Hvornår skal brugeren informeres?
- Hvor tydeligt skal det være?
- Hvordan undgår vi at skabe mere forvirring end klarhed?
- Hvad skal brugeren kunne gøre med informationen?

En dårlig transparensbesked er bare compliance-støj. En god transparensbesked hjælper brugeren med at forstå situationen.

### 4. Gør det testbart

Hvis transparens er et krav, skal det kunne testes.

Eksempler:

- UI-tests der sikrer at AI-labels vises i relevante flows
- API-tests der sikrer metadata på AI-genereret indhold
- Log-tests der sikrer at AI-hændelser kan spores
- Deployment checks der fanger manglende markeringer

Det lyder lidt kedeligt. Det er også pointen. De bedste compliance-løsninger er ofte kedelige på den rigtige måde.

### 5. Gør det auditérbart

Hvis nogen spørger om seks måneder, bør man kunne finde svaret.

Ikke nødvendigvis med en roman. Men med nok struktur til at forklare:

- Hvilken AI-funktion blev brugt
- Hvornår den blev brugt
- Hvilken bruger eller proces der udløste den
- Hvad systemet gjorde
- Om der var menneskelig godkendelse

Hvis det kun findes i Slack-tråde og folks hoveder, findes det ikke rigtigt.

## Hvad betyder det for seniorudviklere?

Jeg tror AI gør seniorrollen vigtigere, ikke mindre vigtig.

Ikke fordi seniorudviklere skal kunne alle paragraffer i EU AI Act udenad. Det ville være en lidt trist superkraft.

Men fordi seniorer ofte sidder tæt på de beslutninger, hvor jura bliver til arkitektur:

- Skal AI-output gemmes?
- Skal det kunne genskabes?
- Hvad logger vi?
- Hvordan adskiller vi model-fejl fra almindelige applikationsfejl?
- Hvordan undgår vi at sende følsomme data til forkerte steder?
- Hvordan bygger vi godkendelsesflows uden at kvæle produktiviteten?

Det er her erfaring betyder noget. Ikke som "nej-hat", men som evnen til at se konsekvenser før de bliver dyre.

## Min holdning

Jeg er grundlæggende positiv over for AI.

Men jeg er endnu mere positiv over for AI der kan drives, forklares, testes og vedligeholdes.

Hvis transparens bliver til en pop-up der ingen læser, har vi ikke vundet meget. Hvis transparens bliver designet ind i systemerne som metadata, logs, UI, processer og ansvar, kan det blive en del af tillidsinfrastrukturen.

Det er måske ikke den mest sexede sætning i verden.

Men i produktion slår tillidsinfrastruktur næsten altid demo-magi.

## Kilder

- [EU-Kommissionen: høring om udkast til retningslinjer for AI-transparensforpligtelser](https://digital-strategy.ec.europa.eu/en/news/commission-opens-consultation-draft-guidelines-ai-transparency-obligations)
- [AI Act Service Desk: tidslinje for implementering af EU AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act)

