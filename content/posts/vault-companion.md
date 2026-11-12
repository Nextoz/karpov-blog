---
title: "Vault Companion: AI, der hjælper mig fra viden til handling"
date: 2026-11-12T09:00:00+01:00
slug: vault-companion
translationKey: vault-companion-showcase
draft: false
authorship: legacy-ai-drafted
description: "En visuel tur gennem min personlige app: AI-scouts, egne noter og gamification — og arkitekturen, der binder det sammen."
summary: "Jeg har bygget en app til én bruger: mig selv. Se, hvordan AI-scouts finder muligheder, jeg træffer beslutninger, og almindelig kode gør fremskridt synlige."
tags: [AI, AI agents, Obsidian, software architecture, gamification]
categories: [Projekter]
author: Evgeny Karpov
ShowReadingTime: true
---

Jeg har ikke svært ved at samle information. Jeg har noter, idéer, artikler, opgaver og ting, jeg gerne vil lære. Det svære er at få den viden tilbage på det rigtige tidspunkt — og gøre noget med den.

Derfor bygger jeg **Vault Companion**: en personlig app, der forbinder mine noter med min hverdag. Den samler opgaver og aktiviteter, viser fund fra mine AI-scouts og gør min indsats synlig gennem levels, professioner og achievements.

<div class="vc-intro">
<p class="vc-eyebrow">Et personligt projekt · Et konkret AI-system</p>
<p><strong>AI finder muligheder. Jeg vælger. Appen holder styr på handlingerne.</strong></p>
<p>Her kan du se både brugeroplevelsen og maskinrummet. Du behøver hverken adgang til appen eller kendskab til AI for at følge med.</p>
</div>

*Skærmbillederne viser den rigtige app i et isoleret demomiljø med opdigtede opgaver, fund og aktivitetsdata. Datoer, scores og levels er eksempler, ikke mine personlige resultater. Appen og mine private noter er ikke offentligt tilgængelige gennem denne artikel.*

## 1. Scouts: fra søgning til et lille udvalg

En scout er mit navn for et tilbagevendende job med en afgrænset opgave: eksempelvis at finde relevante arrangementer, læringsmuligheder eller ny research. Den arbejder i baggrunden og afleverer resultater, som jeg kan læse senere.

I stedet for at starte den samme søgning igen kan jeg åbne appen og se, hvad der er fundet. Oversigten viser også, om jobbet faktisk lykkedes.

<figure class="vc-shot">
<div class="vc-screen"><img src="/images/vault-companion/scouts.jpg" alt="Scouts i Vault Companion: to sunde jobs, ét med problemer og konkrete fund fra arrangementer og læring." width="738" height="1600" loading="lazy"></div>
<figcaption><strong>01 / Overblik.</strong> Fund og driftsstatus står ved siden af hinanden. Den gule scout illustrerer en kørsel, hvor en kilde fejlede.</figcaption>
</figure>

Det er en vigtig detalje. Hvis der ikke dukker nye fund op, skal jeg kunne skelne mellem »der var ikke noget relevant« og »systemet kunne ikke hente en kilde«. Et flot AI-resumé er ikke nok til at besvare det spørgsmål.

AI er nyttig til at vurdere relevans og formulere et kort resumé. Koden omkring modellen står for kørsel, struktur og status. Modellen skal ikke selv afgøre, om dens egen kørsel var teknisk vellykket.

## 2. Fra et AI-fund til min beslutning

Et fund får først værdi, når jeg kan tage stilling til det. På et eventkort kan jeg se tidspunkt, sted, begrundelse og kalenderkontekst — og vælge **Skip**, **Maybe** eller **Go**.

<figure class="vc-shot">
<div class="vc-screen"><img src="/images/vault-companion/events.jpg" alt="Et eksempel på et eventkort med en AI-begrundelse og knapperne Skip, Maybe og Go." width="738" height="1600" loading="lazy"></div>
<figcaption><strong>02 / Beslutning.</strong> Et forslag bliver til et konkret valg. AI-scoren er en vurdering af relevans, ikke en sandsynlighed eller garanti for kvalitet.</figcaption>
</figure>

Forestil dig, at en scout finder en aften om praktisk AI. Den forklarer, hvorfor arrangementet kunne være relevant. Jeg vurderer selv, om jeg vil bruge min torsdag på det.

Når jeg vælger Go, registrerer appen beslutningen. I det tilknyttede workflow kan et job på min computer behandle den og opdatere kalenderen. Det er flere trin, og de behøver ikke ske øjeblikkeligt. **At trykke på en knap og at have gennemført ændringen i et andet system er to forskellige tilstande.**

Det er også en brugbar måde at forstå AI-agenter på: De får en opgave, adgang til bestemte værktøjer og et sted at aflevere resultatet. Hvor de må handle selv, er et designvalg.

## 3. Gamification: at gøre indsatsen synlig

Jeg ville også kunne se den indsats, der let forsvinder i en liste over afsluttede opgaver. Derfor har appen et karakterark med XP, levels, professioner og achievements.

<figure class="vc-shot">
<div class="vc-screen vc-screen--character"><img src="/images/vault-companion/character.jpg" alt="Karakterarket: level 21, fire professioner, tre mål undervejs og nyligt opnåede achievements." width="764" height="1600" loading="lazy"></div>
<figcaption><strong>03 / Fremskridt.</strong> Karakteren er beregnet af den rigtige regelmotor ud fra syntetiske aktivitetsdata. Ringene og målene gør forskellige typer indsats synlige.</figcaption>
</figure>

De fire professioner hedder Athletics, Scholar, Lorekeeper og Quartermaster. De giver træning, læring, refleksion og opgaver deres eget udtryk i samme system.

XP følger faste regler med daglige grænser. Der er ingen AI, som improviserer en belønning, og optjent XP forsvinder ikke, fordi jeg holder pause. Træning belønnes som deltagelse; pointene er ikke et mål for fysisk fremgang. På samme måde er Scholar-XP ikke dokumentation for, at jeg mestrer et emne.

**Spillet er en måde at vise aktivitet på.** Om det faktisk hjælper mig med at fastholde gode vaner, er noget, jeg må vurdere gennem brug — det er ikke bevist af et flot dashboard.

## 4. Maskinrummet: mine noter er fundamentet

Ordet *vault* kommer fra min Obsidian-vault: en mappe med noter i Markdown, et enkelt tekstformat. Appen giver mig en anden indgang til de samme typer information, især fra telefonen.

Den overordnede arkitektur ser sådan ud:

<figure class="vc-diagram">
<img src="/images/vault-companion/architecture-da.svg" alt="Mobilappen kommunikerer gennem en beskyttet API med en versionsstyret vault på GitHub. Desktop-synkronisering forbinder den med lokale noter, Obsidian og scouts. Scouts kan kalde AI-modeller." width="900" height="740" loading="lazy">
<figcaption>Forenklet arkitektur. Pilene viser dataforbindelser, ikke en garanti for øjeblikkelig synkronisering. Appens kildekode og den private vault er forskellige ting.</figcaption>
</figure>

Frontend er en React-app bygget med Vite og kan bruges som en PWA — en webapp, der også kan installeres på telefonen. API'et er bygget med Hono på en Cloudflare Worker og beskyttet med Cloudflare Access. Noterne versionsstyres med Git, mens synkronisering forbinder GitHub med min lokale vault.

Det valg har en pris. Tekstfiler er læsbare og passer til mit eksisterende arbejde, men de er ikke en database med gratis transaktioner. Når både telefonen og computeren kan ændre indhold, skal systemet håndtere samtidige ændringer og gamle versioner.

Derfor arbejder appen med afgrænsede kommandoer og revisionskontrol. Den forsøger at ændre det relevante stykke tekst og kan afvise en ændring, hvis indholdet ikke længere passer til det, den læste. Jeg foretrækker en forklarlig afvisning frem for en tavs overskrivning.

## 5. Hurtig feedback skal stadig være sand

En app føles langsom, hvis hvert flueben skal vente på netværket. Men hurtig feedback må ikke betyde, at appen lader som om noget er gemt, når det ikke er det.

Vault Companion har en lokal kø i IndexedDB, browserens lokale lager. Handlinger har egne ID'er, så gentagelser kan genkendes. Spilreglerne deles mellem klient og server: klienten kan forudsige en belønning, mens serverens svar senere bekræfter eller korrigerer den.

| Situation | Hvad systemet skal holde adskilt |
| --- | --- |
| Jeg registrerer en aktivitet | Handlingen er oprettet lokalt; den er endnu ikke nødvendigvis gemt i vaulten. |
| Telefonen mangler forbindelse | Handlingen venter i køen på denne enhed. |
| Serveren accepterer ændringen | Den gemte tilstand kan bekræftes, og forventet XP afstemmes. |
| En ændring bliver afvist | Appen skal vise problemet og korrigere den foreløbige belønning. |

Det er almindelig software engineering, men det er en stor del af det, der gør et AI-system anvendeligt. Et godt modelforslag hjælper ikke meget, hvis handlingen bagefter forsvinder eller bliver registreret to gange.

## Hvad projektet har lært mig om AI

Jeg bruger AI både som hjælp under udviklingen og i workflows omkring appen. De roller skal holdes adskilt: At kode er skrevet med AI, betyder ikke, at koden kalder en sprogmodel, hver gang den kører.

| AI | Almindelig kode | Mig |
| --- | --- | --- |
| Vurdere relevans og sammenfatte fund | Validere data, håndtere synkronisering og beregne XP | Vælge mål, vurdere forslag og tage beslutninger |

Projektet er udviklet til én bruger. Jeg præsenterer det ikke som et færdigt produkt til alle eller som bevis på målbare produktivitetsgevinster. Der er stadig fejl at finde og friktion at fjerne. Scout-kvalitet, synkronisering og om belønningerne hjælper i praksis er alle ting, der kræver løbende arbejde.

<div class="vc-takeaway">Det, jeg er mest stolt af, er at få delene til at hænge sammen: egne data, AI-forslag, menneskelige valg og en app, jeg kan bruge i hverdagen.</div>

Hvis du selv vil bygge noget med AI, så begynd med én tilbagevendende opgave. Beslut, hvilket resultat der skal komme ud, hvor det skal gemmes, hvordan en fejl bliver synlig, og hvornår et menneske skal tage over. Den afgrænsning er mindst lige så vigtig som valget af model.

### Teknisk grundlag

Beskrivelsen bygger på [Vault Companions kildekode og dokumentation](https://github.com/Nextoz/vault-companion), herunder domænelogik, kontrakter, testfixtures og arkitekturbeslutninger. Skærmbillederne er taget med appens eksisterende UI og isolerede testdata. Diagrammet er en forenklet forklaring af systemet; scout-producenterne er en del af det omgivende desktop-workflow.
