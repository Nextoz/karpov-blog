---
title: "Ugens research: Når retrieval og coding agents møder den virkelige kontekst"
date: 2026-10-25T00:00:00+02:00
lastmod: 2026-10-25T00:00:00+02:00
slug: "ugens-ai-research-2026-10-25"
translationKey: "ugens-ai-research-2026-10-25"
draft: false
authorship: "ai-assembled-digest"
description: "Denne uge peger fem preprints på samme driftserfaring: simple baselines og end-to-end validering er vigtigere end lokale forbedringer. For platform- og backendteams betyder det at teste retrieval i den rigtige stack og teste agentændringer mod systemets fortsatte adfærd."
summary: "Denne uge peger fem preprints på samme driftserfaring: simple baselines og end-to-end validering er vigtigere end lokale forbedringer. For platform- og backendteams betyder det at teste retrieval i den rigtige stack og teste agentændringer mod systemets fortsatte adfærd."
tags: ["AI", "Research", "AI Agents", "Platform Engineering"]
categories: ["AI", "Research"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

*Dette researchoverblik er samlet og skrevet af AI ud fra ugens udvalgte kilder. Det er ikke en personlig afprøvning eller en fagfællebedømmelse fra Evgeny Karpov.*

Ugens kilder: 19.10.2026–25.10.2026.

Ugens fælles mønster er, at agenters kvalitet ikke først og fremmest afgøres af, hvor avanceret et enkelt komponentnavn lyder. Den afgøres af, om retrieval, memory og ændringer holder, når de møder den fulde kontekst: rå historik, voksende korpusser, skiftende krav og et eksisterende system, der fortsat skal fungere.

## Simple retrieval er ikke det samme som simpel drift

Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought udfordrer antagelsen om, at conversation memory skal omskrive, strukturere og løbende mutere historik for at være effektiv. For de benchmarks, forfatterne har undersøgt, klarer Raw-RAG sig stærkt ved at hente og reranke direkte fra rå historik. Deres forklaring er især dækningsgrad: svaret afhænger ofte ikke kun af en enkelt værdi, men af relationer og afhængighedsveje, som en kondenseret memory-store kan have mistet.

Det er relevant for backend- og platformteams, fordi et memory-lag også er et datatabslager. Når historik transformeres til noter, profiler eller regler, bliver det lettere at slå noget op, men sværere at efterprøve, hvad der oprindeligt blev sagt eller gjort. Den rigtige baseline er derfor ikke fravær af intelligence, men en enkel retrieval-løsning over bevaret rå evidens med tydelige grænser for latency, adgang og retention.

Det betyder dog ikke, at Raw-RAG løser personalisering. Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences finder i sin simulerede evaluering, at retrieval-baserede systemer ikke slår No Memory på præferencevalg. Selv når en præference er tilgængelig, kan agentens standardadfærd vinde. Designet bør derfor skelne mellem faktuel evidens, som kan hentes ved behov, og eksplicitte policy-beslutninger som hvornår agenten må handle, afbryde eller bede om bekræftelse.

Kilder: [Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought](https://arxiv.org/abs/2610.30755v1); [Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences](https://arxiv.org/abs/2610.30485v1).

## Optimer hele kæden, og test ændringen som en del af systemet

Retrieval Augmented Generation Compositionality sætter tal på et velkendt integrationsproblem: komponenter, der ser gode ud hver for sig, giver ikke nødvendigvis den forventede samlede effekt. I forfatternes kontrollerede RAG-evaluering varierer den bedste kombination også med korpusstørrelsen, og retrieval-kvalitet kan pege i en anden retning end answer faithfulness. En højere retrieval-score er derfor ikke alene en tilstrækkelig release-gate for et RAG-workflow.

Det taler for at versionere og evaluere retrieval som en samlet pipeline: chunking, embedding, reranking, promptkontekst og svargenerering. En ændring af eksempelvis chunk-størrelse bør afprøves med den samme corpus-størrelse, adgangsmodel og observability som den tiltænkte deployment. Preprintets resultater er benchmark-bundne, men den operationelle pointe er robust: lokale komponentmålinger kan ikke erstatte en test af den fulde kæde.

Samme princip går igen for coding agents. ProductWebBench viser på levende frontend-repositorier, at en patch kan opfylde den bestilte ændring og samtidig skabe regressioner i allerede verificerede browsertilstande eller interaktion. Tallene kan ikke flyttes direkte til backend, men fejlmønstret er genkendeligt: en endpoint-ændring kan bestå sin nye test og stadig bryde auth, retries, kontrakter eller deployment. SWE-DIVE understreger desuden, at agentarbejde ofte sker gennem flere runder, hvor krav ændres undervejs. Evaluering bør derfor bevare tidligere checks gennem hele workflowet frem for kun at kontrollere den sidste opgave.

Kilder: [Retrieval Augmented Generation Compositionality](https://arxiv.org/abs/2610.29722v1); [ProductWebBench: Evaluating Website Continuity Beyond Task Completion](https://arxiv.org/abs/2610.31118v1); [SWE-DIVE: Multi-Turn Coding Agent Evaluation with Dynamic User Simulation](https://arxiv.org/abs/2610.30047v1).

## Hvad er værd at tage med?

Et afgrænset næste skridt er at vælge én retrieval- eller agentunderstøttet ændring i næste sprint og køre den mod en simpel baseline i den fulde workflow-kontekst. Mål både den ønskede opgave og mindst én bevaringsregel, for eksempel korrekt svar med kildegrundlag, uændret API-kontrakt, genkørbar deployment eller en tidligere passerende integrationstest. Det er en lille investering, men den gør det synligt, om ny kompleksitet faktisk hjælper, eller blot flytter fejlen til et andet led.

Overblikket bygger på de linkede kilders abstracts eller artikeluddrag. Resultaterne er forfatternes egne rapporter; forslag til praksis er overblikkets fortolkning. Kildeudvalget dækker ikke al ugens forskning.
