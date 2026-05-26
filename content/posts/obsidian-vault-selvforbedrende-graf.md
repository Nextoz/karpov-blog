---
title: "Mit Obsidian-vault fik en lille forskningsafdeling"
date: 2026-05-26
lastmod: 2026-05-26
draft: false
description: "Jeg har bygget et Obsidian-setup med graph memory, daglig research scout og blogkladder. Ikke som magi, men som et praktisk AI-arbejdsbord."
summary: "Et kig ind i mit Obsidian-vault: graph memory, daglig research scout, kandidatnoter og blogkladder. AI som arbejdsbord, ikke som tryllestav."
tags: ["AI", "Obsidian", "DevOps", "Platform Engineering", "Knowledge Management", "AI Agents"]
categories: ["AI", "DevOps", "Teknologi"]
author: "Evgeny Karpov"
ShowReadingTime: true
cover:
  image: "/karpov-blog/images/obsidian-vault-knowledge-graph.svg"
  alt: "Et Obsidian-lignende knowledge graph over noter, research, job search og blogarbejde."
  caption: "Mit vault som graf. Det ligner lidt en efterfest for noter, men der er faktisk en ide med det."
---

# Mit Obsidian-vault fik en lille forskningsafdeling

![Et Obsidian-lignende knowledge graph over noter, research, job search og blogarbejde.](/karpov-blog/images/obsidian-vault-knowledge-graph.svg)

Jeg har gjort noget, der på papiret lyder en smule farligt:

Jeg har givet mit Obsidian-vault en lille AI-agent.

Ikke en agent med adgang til at købe aktier, slette produktion eller sende mails til tidligere chefer klokken 02:13. Det ville være en anden type blogindlæg. Muligvis også en anden type liv.

Den her agent har et mere jordnært job:

Den skal hjælpe mig med at holde styr på viden.

Mere præcist har jeg bygget to ting oven på mit Obsidian-vault:

1. En **self-improving graph memory**, der scanner mine noter og finder huller i grafen.
2. En **daily research scout**, der hver dag leder efter ny forskning og relevante AI/tech-nyheder, laver en briefing, opretter kandidatnoter og foreslår blogkladder.

Det lyder måske som noget, man siger i en pitch deck med alt for mange gradienter.

Men ideen er egentlig ret ydmyg:

Jeg vil ikke have en AI, der tænker for mig.

Jeg vil have et arbejdsbord, der gør det lettere at tænke.

## Problemet med noter er ikke at skrive dem

Jeg har mange noter.

DevOps-noter. Job-search-noter. AI-research. Blogideer. Guides. Projekter. Halvfærdige tanker. Gode tanker. Noter der engang var gode tanker, men nu mest er digitalt kompost.

Obsidian er fantastisk til den slags, fordi alt er markdown, links og lokal kontrol.

Men et vault kan også langsomt blive en kælder.

Ikke en hyggelig vinkælder.

Mere sådan en kælder hvor der står en kasse med "vigtige kabler" fra 2011, og man er bange for at smide den ud, fordi der måske ligger et mini-USB-kabel der en dag redder civilisationen.

Problemet med en personlig knowledge base er sjældent, at man ikke kan skrive mere.

Problemet er:

- Hvad er stadig relevant?
- Hvad er forældet?
- Hvad hænger sammen?
- Hvad mangler links?
- Hvilke noter er bare støj?
- Hvilke nye ting på internettet er faktisk værd at gemme?

Det er her grafen bliver interessant.

## Graph memory: når noter ikke kun ligger, men peger

Obsidian har allerede et graph view. Det er visuelt tilfredsstillende på samme måde som et kontrolrum i en science fiction-film.

Man ser noder, forbindelser, klynger og små ensomme prikker ude i mørket, som tydeligvis har brug for enten kærlighed eller arkivering.

Men en graf er kun nyttig, hvis man bruger den som mere end pynt.

Derfor lavede jeg en lille scanner, der læser mine markdown-filer og bygger et lokalt graph memory:

- titel
- filsti
- frontmatter
- tags
- aliases
- wikilinks
- indgående og udgående forbindelser
- manglende metadata
- mulige relaterede noter

Den skriver resultatet til en JSON-fil og laver en menneskelig review-note i Obsidian.

Det vigtige er, hvad den **ikke** gør:

Den retter ikke automatisk hele mit vault.

Den sletter ikke noter.

Den flytter ikke rundt på ting som en begejstret praktikant med administratorrettigheder.

Den siger bare:

> "Her er 25 noter uden gode forbindelser. Her er nogle dubletter. Her er nogle store noter uden hub-link. Måske burde du kigge på dem, kammerat."

Det er ikke fuld autonomi.

Det er bedre end fuld autonomi.

Det er en assistent med situationsfornemmelse.

## Selvforbedrende betyder ikke selvforherligende

"Self-improving graph" kan hurtigt lyde som om systemet sidder om natten og bliver klogere, mens man selv sover.

Det gør det ikke.

Og det er nok meget godt.

Det jeg mener med selvforbedrende er mere nøgternt:

1. Systemet scanner grafen.
2. Det finder svage steder.
3. Det foreslår forbedringer.
4. Jeg eller en AI-session kan lave små ændringer.
5. Næste scanning viser, om grafen blev bedre.

Det er en feedback loop.

Ikke magi.

Bare en rimelig voksen måde at bruge AI på.

Den samme ide kender vi fra software engineering:

- kør tests
- læs fejlene
- ret småt
- kør igen

Jeg bruger bare samme princip på min viden.

Hvis en note er vigtig, skal den kunne findes. Hvis en research-konklusion betyder noget, skal den linkes fra et hub. Hvis en gammel note er erstattet, skal den markeres som superseded i stedet for at ligge og hviske forældede råd fra 2023.

Det sidste burde egentlig stå i Grundloven for knowledge workers.

## Den daglige research scout

Den anden del er min daily research scout.

Den scanner hver dag kilder som:

- arXiv
- OpenAI
- GitHub Blog
- Microsoft Research
- Google Research
- Google News RSS-søgninger på AI agents, computer science og quantum computing

Den leder efter emner, jeg faktisk går op i:

- AI agents
- coding agents
- MCP
- RAG og GraphRAG
- agent memory
- software engineering benchmarks
- DevOps og platform engineering
- security
- quantum computing
- AI governance

Den laver tre outputs:

1. En daglig research-briefing i Obsidian.
2. Kandidatnoter for ting, der virker vigtige nok.
3. Blogkladder, hvis noget har en offentlig vinkel.

Igen: den udgiver ikke noget.

Hvis en agent automatisk begynder at publicere ens blogindlæg, er man kun cirka to prompts fra at blive thought leader på LinkedIn mod sin vilje.

Og det ønsker vi ikke.

Eller jo, måske lidt.

Men ikke sådan.

## Hvordan den beslutter, hvad der er vigtigt

Det svære er ikke at finde nyheder.

Internettet er lavet af nyheder. De fleste af dem er enten gentagelser, produktannoncer med slips på eller "banebrydende" ting, der viser sig at være en dropdown med AI i navnet.

Det svære er at filtrere.

Min scout bruger derfor en simpel beslutningsmodel:

- Matcher emnet mine kerneområder?
- Kommer det fra en nogenlunde troværdig kilde?
- Er det forskning, tooling eller praksis, der kan ændre hvordan jeg arbejder?
- Er det relevant for DevOps, platform engineering, AI agents eller bloggens tekniske profil?
- Er det bare interessant, eller er det faktisk brugbart?

Hvis noget kun er let interessant, kommer det i briefingen.

Hvis noget virker vigtigt, opretter den en **research-intake note** med `status: candidate`.

Det er et vigtigt ord: candidate.

Det betyder:

> "Dette kan være vigtigt. Men en voksen skal stadig kigge på det."

Den første kørsel fandt for eksempel et paper om automated benchmark auditing for AI agents. Det er interessant, fordi benchmarks er blevet en del af den måde vi taler om AI-kapabilitet på, men benchmark-opgaver kan selv være fejlbehæftede.

Det er en god påmindelse:

Hvis vi måler AI dårligt, bygger vi også AI-systemer på dårlige antagelser.

Det er præcis den type ting, jeg gerne vil have min scout til at fange.

## Bloggen som biprodukt af læring

Jeg vil gerne skrive mere.

Men jeg vil ikke skrive bare for at fodre algoritmen med endnu en tekst om "5 måder AI ændrer alt".

Min blog skal helst komme fra faktisk arbejde:

- noget jeg har bygget
- noget jeg har lært
- noget jeg har observeret
- noget der ændrer min måde at tænke på software, drift eller AI

Derfor er blogdelen af scout'en ikke en tekstmaskine.

Den er en ide-maskine.

Når den finder noget relevant, opretter den en draft med:

- kilde
- kort vinkel
- mulig struktur
- relation til eksisterende posts
- reminder om at tilføje min egen vurdering

Det er en startblok, ikke et færdigt løb.

AI må gerne hjælpe med at hente bolden.

Den skal ikke spille kampen alene og bagefter forklare, at den altid har været passioneret omkring dansk teknologipolitik.

## Hvorfor det her faktisk er DevOps

Det kan lyde som et personligt produktivitetsprojekt.

Det er det også.

Men under overfladen er det meget DevOps-agtigt:

- klare inputkilder
- konfiguration
- automatiseret daglig kørsel
- output som filer
- review før promotion
- ingen automatisk publicering
- små feedback loops
- tydelige guardrails
- lokal kontrol

Det er ikke nok at sige "AI, hold mig opdateret."

Det er en følelse, ikke et system.

Et system kræver:

- hvor skal den lede?
- hvad tæller som relevant?
- hvad må den ændre?
- hvad må den ikke ændre?
- hvordan ser jeg resultatet?
- hvordan retter jeg kursen?

Det er de samme spørgsmål, man bør stille til enhver automation, der får lov at røre noget vigtigt.

Og ens noter er vigtige.

Ikke fordi hver enkelt note er genial.

Nogle af mine noter er bestemt ikke geniale. Nogle af dem burde måske stå med hjelm.

Men samlet set er de kontekst.

Og kontekst er blevet en af de vigtigste ressourcer i AI-arbejde.

## Det ydmyge ved AI

Der er en fristelse til at tale om AI som noget meget stort.

En ny intelligens. En revolution. En maskine der kan gøre alt, lige efter næste release og med lidt bedre prompting.

Men min erfaring er mere jordnær:

AI bliver mest nyttig, når man giver den et lille, klart job.

Ikke:

> "Forstå hele mit liv."

Men:

> "Find noter uden links."

Ikke:

> "Gør mig til ekspert i AI."

Men:

> "Scan de her kilder hver morgen og vis mig de tre ting, der faktisk kan betyde noget."

Ikke:

> "Skriv min blog."

Men:

> "Lav en kladde med kilder og vinkel, så jeg kan skrive bedre og hurtigere."

Det er måske mindre spektakulært.

Til gengæld virker det.

Og i software er "det virker" stadig en undervurderet feature.

## Min konklusion

Jeg tror mere og mere på personlige AI-systemer, der er bygget som små platforme.

Ikke én stor chatbot.

Men en samling af:

- noter
- scripts
- graph memory
- daglige scouts
- review-noter
- kandidater
- blogkladder
- klare regler for hvad der må ske automatisk

Det er ikke perfekt.

Det er ikke en erstatning for at læse, tænke og skrive selv.

Men det er et ret godt stillads.

Og måske er det netop sådan AI bliver mest nyttig for almindelige udviklere:

Ikke som en alvidende kollega med lidt for meget selvtillid.

Men som en tålmodig assistent, der hver morgen møder ind og siger:

> "Jeg har ryddet lidt op i grafen, fundet tre papers og lavet en blogkladde. Kaffen må du selv stå for."

Det kan jeg godt leve med.

Læs også:

- [AI er ikke længere en chatbot - det er det nye produktionsapparat](/karpov-blog/posts/ai-er-ikke-laengere-en-chatbot/)
- [DevOps er ikke en pipeline](/karpov-blog/posts/devops-er-ikke-en-pipeline/)
- [EU AI Act i praksis: transparens er ikke bare en pop-up](/karpov-blog/posts/eu-ai-act-transparens-er-ikke-bare-en-popup/)

