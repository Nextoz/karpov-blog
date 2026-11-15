---
title: "Ugens AI-forskning: Agenters svaghed er ofte manglende bevis, ikke manglende svar"
date: 2026-11-15T00:00:00+01:00
lastmod: 2026-11-15T00:00:00+01:00
slug: "ugens-ai-research-2026-11-15"
translationKey: "ugens-ai-research-2026-11-15"
draft: false
authorship: "ai-assembled-digest"
description: "Ugens forskning peger på en fælles driftsregel: Agenters kvalitet afhænger mindre af, hvor overbevisende de forklarer sig, end af om de kan se, verificere og afgrænse den konkrete situation, de handler i."
summary: "Ugens forskning peger på en fælles driftsregel: Agenters kvalitet afhænger mindre af, hvor overbevisende de forklarer sig, end af om de kan se, verificere og afgrænse den konkrete situation, de handler i."
tags: ["AI", "Research", "AI Agents", "Platform Engineering"]
categories: ["AI", "Research"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

*Dette researchoverblik er samlet og skrevet af AI ud fra ugens udvalgte kilder. Det er ikke en personlig afprøvning eller en fagfællebedømmelse fra Evgeny Karpov.*

Ugens kilder: 09.11.2026–15.11.2026.

For backend- og platformteams er den interessante udvikling ikke blot bedre modeller, men bedre rammer omkring modellerne. Tre nye preprints undersøger debugging, database-migrering og enterprise-sikkerhed. På tværs af dem opstår samme mønster: retrieval, runtime-data og tilladelsesbeviser er produktionsafhængigheder, ikke baggrundskontekst.

## Runtime-adgang og tilladelsesbevis er en del af agentens kontrolplan

Where LLM Agents Get Stuck Debugging Databases beskriver observationer af én coding agent i otte databasehændelser i en produktionsmotor. Når årsagen afhang af samtidighed, fremsatte agenten en diagnose og en rettelse, som senere måtte trækkes tilbage. Forfatterne knytter mønsteret til manglende adgang til blandt andet lock-visninger, komplette deadlock-rapporter, read-only forespørgsler og tydelig miljøkontekst. Det er et vigtigt skel: En plausibel forklaring på den synlige kode er ikke det samme som en verificeret forklaring på et levende system.

paragraphs are invalid

Kilder: [Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning](https://arxiv.org/abs/2611.17304v1); [DEPUTYBENCH: Evaluating Contextual Safety in Enterprise Agents](https://arxiv.org/abs/2611.13355v1).

## Memory er ikke det samme som læring

Does a Self-Learning Migration Agent Learn? undersøger en agent til Oracle-til-PostgreSQL-migrering og skelner mellem forbedring fra vedvarende memory, policy-tilpasning og genbrug af lignende referencer. I forfatternes audit blev meget af den oprindelige målte memory-effekt svagere, når datasæt med delte PostgreSQL-referencer blev isoleret, og en enkel nearest-target-copy baseline slog LLM-systemerne på deres referencekonformitetsmål.

Det betyder ikke, at retrieval er værdiløst. Det betyder, at et godt resultat kan være korrekt genfinding eller kopiering snarere end ny, overførbar problemløsning. For en migration-workflow bør benchmark derfor gruppere nært beslægtede mål, holde referencer adskilt mellem træning og evaluering og kontrollere den migrerede adfærd, ikke kun om output ligner en accepteret reference.

Forfatterne rapporterer også tilfælde, hvor PostgreSQL-accepteret kode var adfærdsmæssigt forkert, mens en menneskelig, gated fix-cyklus løftede antallet af påviseligt korrekte enheder. Det passer med debugging-resultatet: Systemets eksterne kontrolsignaler skal have forrang over agentens selvsikre mellemresultat. Studiet er et preprint baseret på de beskrevne datasæt og mål; det dokumenterer ikke generelt, at alle memory-systemer fejler.

Kilder: [Does a Self-Learning Migration Agent Learn? An Audited Evaluation of Evidence-Graded Experience Memory for Oracle-to-PostgreSQL Migration](https://arxiv.org/abs/2611.16143v1).

## Byg workflowet omkring reversible påstande

De tre studier peger samlet mod et mere jordnært designprincip. Giv ikke en agent bredere skriveadgang for at kompensere for dårlig kontekst. Giv den i stedet afgrænset read-only indsigt, et tydeligt miljøkort og et eksplicit svarformat, hvor hvert kritisk skridt angiver hvilket bevis der mangler. I database-debugging kan det være en anonymiseret lock-snapshot og en reproducerbar replay; i migrering kan det være tests mod kilde- og målsemantik; i enterprise-arbejde kan det være en verificerbar tilladelsesrecord.

Praktisk takeaway: Vælg én eksisterende agent-workflow med ændringsadgang, og indsæt en stop-gate før deploy eller skrivning. Gaten skal kræve både et autorisationsbevis og et domænespecifikt observationsbevis, eksempelvis en relevant runtime-måling eller en adfærdstest. Hvis et af dem mangler, skal workflowet returnere en konkret read-only undersøgelsesopgave frem for en rettelse. Det er en lille, målbar ændring, som kan testes på historiske sager uden at påstå, at agenten allerede har lært problemet.

Kilder: [Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning](https://arxiv.org/abs/2611.17304v1); [Does a Self-Learning Migration Agent Learn? An Audited Evaluation of Evidence-Graded Experience Memory for Oracle-to-PostgreSQL Migration](https://arxiv.org/abs/2611.16143v1); [DEPUTYBENCH: Evaluating Contextual Safety in Enterprise Agents](https://arxiv.org/abs/2611.13355v1).

## Hvad er værd at tage med?

Den fælles engineering-opgave er at gøre agentens grænser operationelle: adskil observation fra hypotese, retrieval fra læring og tilladt fra verificeret tilladt. Det giver teams en bedre mulighed for at gøre agentarbejde reversibelt, auditerbart og sikkert nok til virkelige platform-workflows.

Overblikket bygger på de linkede kilders abstracts eller artikeluddrag. Resultaterne er forfatternes egne rapporter; forslag til praksis er overblikkets fortolkning. Kildeudvalget dækker ikke al ugens forskning.
