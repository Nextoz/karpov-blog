---
title: "EU AI Act i praksis: transparens er ikke bare en pop-up"
date: 2026-05-25
lastmod: 2026-05-25
draft: false
description: "EU AI Act gør transparens til et praktisk produkt-, DevOps- og arkitekturproblem. Her er hvad teams bør begynde at forberede nu."
summary: "Fra 2. august 2026 begynder Article 50-transparensreglerne i EU AI Act at gælde. Det lyder som jura, men i praksis bliver det også et spørgsmål om UI, metadata, logs, audit trails, test og drift."
tags: ["AI", "EU AI Act", "DevOps", "Platform Engineering", "Regulering", "Compliance"]
categories: ["Teknologipolitik", "AI"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# EU AI Act i praksis: transparens er ikke bare en pop-up

EU AI Act lyder som noget, man kan parkere hos Legal.

Det tror jeg er en fejl.

Ikke fordi juristerne ikke skal være med. Det skal de. Meget gerne tidligt, før nogen har bygget en AI-feature, der sender persondata på sightseeing gennem tre SaaS-produkter og en optimistisk proof-of-concept.

Men fordi transparens ikke kun er en juridisk tekst. Det bliver også et produktproblem, et UX-problem, et arkitekturproblem og til sidst et driftproblem.

Og driftproblemer har det med at lande hos de mennesker, der bygger, deployer og vedligeholder systemerne.

## Hvorfor det betyder noget nu

EU-Kommissionen offentliggjorde den 8. maj 2026 udkast til retningslinjer for transparensforpligtelserne i Article 50 i EU AI Act. Høringen er åben indtil 3. juni 2026.

Selve transparensreglerne begynder at gælde fra **2. august 2026**.

Det er ikke en fjern "en dag burde vi nok"-dato. Det er snart.

Reglerne handler blandt andet om, at brugere skal informeres, når de interagerer med bestemte AI-systemer, og at AI-genereret eller manipuleret indhold i nogle tilfælde skal kunne opdages gennem maskinlæsbare markeringer.

Den korte version:

- bruger du AI direkte i produktet, skal brugeren måske vide det
- genererer du syntetisk tekst, lyd, billede eller video, skal det måske markeres
- bruger du emotion recognition eller biometrisk kategorisering, skal mennesker informeres
- publicerer du AI-genereret tekst om emner af offentlig interesse, skal du tænke dig særligt godt om

Det lyder måske som compliance.

Men hvis man har bygget software i mere end ti minutter, ved man godt, at "bare lige informer brugeren" sjældent er en lille ændring.

## Pop-up-fælden

Den nemme version af transparens er en pop-up:

> "Denne funktion bruger AI."

Så er alle glade, ikke?

Jura har fået sin tekst. Produkt har fået sin modal. Udvikleren har fået en ticket med acceptkriteriet "show label". Compliance kan sætte et flueben. Champagne, eller i det mindste billig kaffe.

Problemet er, at pop-up'en ofte kun er overfladen.

De rigtige spørgsmål kommer bagefter:

- Hvornår skal beskeden vises?
- Hvem skal se den?
- Hvad betyder "bruger interagerer med AI" i vores system?
- Hvad hvis AI kun assisterer en medarbejder bag kulissen?
- Hvad hvis output bliver redigeret af et menneske?
- Hvad hvis indholdet eksporteres til PDF, e-mail eller et andet system?
- Kan vi dokumentere bagefter, at transparensen faktisk var der?

Det er her, transparens holder op med at være tekst og begynder at være systemdesign.

## Machine-readable marking er ikke tryllestøv

Et af de mere tekniske elementer er maskinlæsbar markering af AI-genereret eller manipuleret indhold.

Det lyder lidt som noget, man kan købe i en pakke:

> "Vi installerer bare watermarking, så er den klaret."

Måske. Måske ikke.

Maskinlæsbar markering kan i praksis betyde metadata, provenance, vandmærkning, API-felter, content labels, audit logs eller andre mekanismer, der gør det muligt at opdage, at noget er AI-genereret eller manipuleret.

Og så begynder de kedelige, vigtige spørgsmål:

- Hvor gemmer vi markeringen?
- Overlever den copy/paste?
- Overlever den eksport til PDF?
- Overlever den upload til et CMS?
- Overlever den, når en integration laver data om til et andet format?
- Hvordan tester vi, at markeringen stadig findes efter næste release?
- Hvem ejer fejlen, hvis markeringen forsvinder i en pipeline?

Der er meget lidt "bare en pop-up" over det.

## Transparens skal kunne testes

Hvis transparens er et krav, bør det kunne testes.

Ellers har man ikke et krav. Så har man en intention med pæn skrifttype.

Eksempler:

- UI-tests, der sikrer at AI-labels vises i relevante flows
- API-tests, der sikrer metadata på AI-genereret indhold
- integrationstests, der sikrer at labels overlever eksport eller videresendelse
- log-tests, der sikrer at AI-relaterede hændelser kan spores
- deployment checks, der fanger manglende konfiguration
- runbooks, der forklarer hvad support skal svare, når en bruger spørger

Det lyder tørt. Det er også pointen.

De bedste compliance-løsninger er ofte kedelige på den rigtige måde. De ligger i pipeline, test, logging, dokumentation og release-processer. Ikke i en panisk Confluence-side skrevet aftenen før audit.

## DevOps-vinklen

AI governance bliver ofte talt om, som om det foregår i et mødelokale med en PowerPoint og meget alvorlige ansigter.

Men i praksis lander meget af arbejdet i systemerne.

Hvis et produktteam bruger AI i produktion, bør nogen kunne svare på:

- Hvilke miljøer har AI-features slået til?
- Hvilke modeller, services eller leverandører bruges?
- Hvilke secrets og API-nøgler findes?
- Hvilke data sendes til modellen?
- Hvilke logs viser AI-relaterede hændelser?
- Hvilke dashboards viser fejlrate, latency og afhængighedsfejl?
- Hvilke deployment gates beskytter mod at labels, logs eller metadata forsvinder?
- Hvad er rollback-planen, hvis en AI-feature opfører sig forkert?

Det her er ikke kun Legal. Det er platform engineering.

Det er CI/CD. Det er observability. Det er adgangsstyring. Det er dokumentation. Det er incident response. Det er produktansvar med arbejdstøj på.

## Fire typer AI, fire forskellige spørgsmål

Teams bør ikke behandle alle AI-features ens.

Jeg ville starte med en simpel opdeling:

### 1. Intern AI-hjælp

Eksempel: en udviklerassistent, en intern dokumentationsbot eller et supportværktøj til medarbejdere.

Spørgsmål:

- Hvilke interne data må den bruge?
- Logges prompts og svar?
- Kan medarbejdere komme til at indsætte persondata eller secrets?
- Skal output markeres, hvis det senere sendes til kunder eller borgere?

### 2. Brugerrettet AI-interaktion

Eksempel: chatbot, søgeassistent, rådgivningsflow eller kundesupport.

Spørgsmål:

- Ved brugeren, at de interagerer med AI?
- Kan brugeren få fat i et menneske?
- Er der en tydelig grænse mellem information, anbefaling og beslutning?
- Hvordan håndteres fejl og hallucinationer?

### 3. AI-genereret indhold

Eksempel: tekst, billeder, video, lyd, resuméer, rapporter eller produktbeskrivelser.

Spørgsmål:

- Skal indholdet markeres?
- Er der menneskelig redaktionel kontrol?
- Hvem tager ansvar for publiceringen?
- Overlever markeringen, når indholdet flyttes mellem systemer?

### 4. AI-assisterede beslutninger

Eksempel: screening, prioritering, risikovurdering eller sagsbehandling.

Spørgsmål:

- Er systemet højrisiko?
- Er brugeren eller borgeren påvirket af output?
- Kan beslutningen forklares?
- Hvor ligger menneskelig kontrol?
- Hvilke audit trails findes?

Det her er ikke en komplet juridisk klassifikation. Det er en praktisk start.

Og den er bedre end "vi bruger bare AI lidt hist og her".

## En praktisk tjekliste for danske teams

Hvis jeg sad i et dansk produkt-, DevOps- eller platformteam, ville jeg starte her:

### 1. Lav et AI-inventar

Find alle steder, hvor organisationen bruger AI:

- chatbots
- dokumentgenerering
- kundesupport
- søgning
- anbefalinger
- interne agent-workflows
- kode- og dokumentationsautomatisering
- billed-, video- eller lydgenerering
- rapporter og resuméer

Man kan ikke lave transparens for systemer, man ikke ved findes.

### 2. Sæt ejer på hver AI-feature

Ikke bare "IT".

Skriv konkret:

- produktejer
- teknisk ejer
- dataansvarlig kontakt
- supportkontakt
- compliance/juridisk kontakt

Hvis ingen ejer den, ejer alle problemet. Og det betyder som regel, at ingen gør.

### 3. Beslut hvor transparens bor

Transparens kan bo flere steder:

- UI
- API-response
- metadata
- database
- logs
- eksportformat
- dokumentation
- supportmateriale

Det vigtige er at beslutte det bevidst.

Hvis transparens kun bor i UI, men output også eksporteres, har man sandsynligvis bygget et hul med flot frontend.

### 4. Gør det testbart

Lav konkrete kontroller:

- AI-label vises i relevante brugerflows
- metadata følger med i API-output
- audit logs registrerer AI-hændelser
- eksport bevarer markering
- konfiguration er forskellig for dev, test og prod, men kravene er ikke glemt

Det skal kunne fanges før produktion.

### 5. Skriv en runbook

Support og drift skal kunne svare, når nogen spørger:

- Hvorfor står der, at dette er AI-genereret?
- Hvilken AI bruges?
- Kan jeg få en menneskelig vurdering?
- Hvad gør jeg, hvis output er forkert?
- Hvordan rapporterer jeg et problem?

Hvis svaret kun findes i hovedet på en produktmanager, findes det ikke rigtigt.

### 6. Byg audit trail uden at logge alt ukritisk

Auditability betyder ikke "gem alt for evigt".

Det betyder: gem nok til at kunne forstå, forklare og fejlfinde systemet, uden at skabe et nyt privatlivsproblem.

Det kræver balance:

- hvad skal logges?
- hvad skal maskeres?
- hvor længe gemmes det?
- hvem må læse det?
- hvordan slettes det?

Det er her, DevOps, sikkerhed, produkt og jura skal tale sammen, helst før produktion gør det for dem.

## Hvad betyder det for seniorudviklere?

Jeg tror AI gør seniorrollen vigtigere, ikke mindre vigtig.

Ikke fordi seniorudviklere skal kunne alle paragraffer i EU AI Act udenad. Det ville være en trist superkraft.

Men fordi seniorer ofte sidder tæt på de beslutninger, hvor jura bliver til arkitektur:

- Skal AI-output gemmes?
- Skal det kunne genskabes?
- Hvad logger vi?
- Hvordan adskiller vi model-fejl fra almindelige applikationsfejl?
- Hvordan undgår vi at sende følsomme data det forkerte sted hen?
- Hvordan bygger vi godkendelsesflows uden at kvæle produktiviteten?
- Hvordan sikrer vi, at transparens ikke forsvinder i næste refaktorering?

Det er her erfaring betyder noget.

Ikke som nej-hat. Mere som den person i rummet, der har set nok systemer knække til at spørge:

> "Okay, men hvordan virker det her mandag morgen, når support får den første sag?"

## Min holdning

Jeg er grundlæggende positiv over for AI.

Men jeg er endnu mere positiv over for AI, der kan drives, forklares, testes og vedligeholdes.

Hvis transparens bliver til en pop-up, ingen læser, har vi ikke vundet meget.

Hvis transparens bliver designet ind i systemerne som metadata, UI, logs, tests, runbooks, ansvar og audit trails, kan det blive en del af tillidsinfrastrukturen.

Det er måske ikke den mest sexede sætning i verden.

Men i produktion slår tillidsinfrastruktur næsten altid demo-magi.

## Læs også

- [DevOps er ikke en pipeline](/karpov-blog/posts/devops-er-ikke-en-pipeline/)
- [AI er ikke længere en chatbot - det er det nye produktionsapparat](/karpov-blog/posts/ai-er-ikke-laengere-en-chatbot/)
- [Project Glasswing - Når AI finder de fejl mennesker overser](/karpov-blog/posts/project-glasswing/)
- [Portfolio: DevOps, Platform Engineering og .NET](/karpov-blog/projekter/)

## Kilder

- [EU-Kommissionen: udkast til retningslinjer for transparensforpligtelser under Article 50](https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act)
- [EU-Kommissionen: høring om transparensforpligtelser under AI Act](https://digital-strategy.ec.europa.eu/en/consultations/consultation-draft-guidelines-transparency-obligations-under-ai-act)
- [AI Act Service Desk: implementeringstidslinje for EU AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act)
