---
title: "AI-agenter skal bruge hukommelse"
date: 2026-06-06
lastmod: 2026-06-06
slug: "ai-agenter-skal-bruge-hukommelse"
draft: false
description: "En praktisk note om hvorfor AI-agenter ikke kun skal bruge API'er, men også hukommelse, kilder, validering og menneskelig review."
summary: "API'er giver AI-agenter adgang til systemer. Hukommelse afgør, om de kan arbejde ansvarligt over tid uden at gentage fejl, miste kontekst eller opfinde en flot forklaring bagefter."
tags: ["AI", "AI Agents", "Agent Memory", "DevOps", "Platform Engineering", "Observability"]
categories: ["AI", "DevOps"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# AI-agenter skal bruge hukommelse

Jeg skrev for nylig, at AI-agenter skal bruge API'er.

Det mener jeg stadig.

Men API'er er kun halvdelen af problemet.

En agent, der kan kalde et API, kan gøre noget i verden. Den kan hente data, oprette en pull request, ændre en konfiguration, skrive en kommentar eller starte en proces.

Det er nyttigt.

Det er også dér, problemerne begynder.

For hvis agenten ikke kan huske, hvorfor den gjorde noget, hvilke kilder den brugte, hvilke checks der fejlede, hvilke beslutninger et menneske allerede har taget, og hvor grænsen for opgaven går, så har man ikke fået en kollega.

Man har fået en meget hurtig praktikant med hukommelsestab og adgang til produktion.

Det lyder måske som en joke.

Det er mest en driftshændelse, der venter på at ske.

## Hukommelse er ikke chat history

Mange tænker stadig på AI-hukommelse som en længere samtale.

Det er for snævert.

For rigtige AI-agenter handler hukommelse ikke kun om at huske, hvad brugeren skrev for fem minutter siden. Det handler om at kunne arbejde med tilstand over tid.

En brugbar agent skal kunne huske:

- opgavens mål
- hvilke filer, systemer og kilder den har brugt
- hvilke antagelser den har lavet
- hvilke checks der er kørt
- hvad der fejlede
- hvad den allerede har prøvet
- hvilke beslutninger et menneske har godkendt
- hvilke dele af arbejdet der stadig er usikre

Det er ikke romantisk AI.

Det er almindelig software engineering.

Men det er præcis derfor, det er vigtigt.

## Kontekst uden struktur bliver hurtigt støj

En stor context window kan føles som en løsning.

Bare giv modellen mere tekst. Flere filer. Flere noter. Flere logs. Hele repoet. Hele dokumentationen. Hele virksomhedens kollektive dårlige samvittighed i Markdown.

Problemet er, at mere kontekst ikke automatisk giver bedre forståelse.

Nogle gange giver det bare en agent flere muligheder for at finde den forkerte detalje og lyde sikker imens.

Derfor tror jeg, at agent memory bliver et systemproblem, ikke kun et modelproblem.

Hukommelsen skal have struktur:

- Hvad er fakta?
- Hvad er en beslutning?
- Hvad er en midlertidig antagelse?
- Hvad er et gammelt notat?
- Hvad er en kilde?
- Hvad er en valideret ændring?
- Hvad er en opgave, der stadig mangler review?

Hvis alt bare ligger som tekst i én stor bunke, bliver agenten ikke nødvendigvis klogere. Den bliver bare bedre fodret.

Og alle, der har arbejdet med gamle dokumentationsmapper, ved at godt fodret forvirring stadig er forvirring.

## Min lille version: Obsidian som agent-hukommelse

Jeg har brugt min egen Obsidian-vault som et lille laboratorium for det her.

Ikke som et stort fancy produkt. Mere som et praktisk forsøg:

Kan noter, research, opgaver, skills og links gøres brugbare for AI-agenter over tid?

Det korte svar er ja.

Men kun hvis noterne er skrevet til at blive brugt igen.

En note, der bare er et tekst-dump, hjælper ikke meget. En note med en kort konklusion, frontmatter, kilder, status, relaterede noter og et tydeligt link til en hub er meget mere værd.

Det lyder småt.

Det er det ikke.

For når en agent starter en opgave, skal den kunne finde den rigtige kontekst uden at læse hele mit digitale loftsrum først.

Derfor er jeg begyndt at behandle noter som små memory objects:

- `type`: er det research, guide, skill, dashboard eller reference?
- `status`: er det aktivt, udkast, arkiveret eller superseded?
- `memory`: er det semantisk viden, en procedure eller en episodisk log?
- `confidence`: hvor sikker er noten?
- `source`: hvor kommer informationen fra?
- `related notes`: hvor hører den hjemme i grafen?

Det er ikke fordi YAML er magisk.

Det er fordi agenten skal kunne sortere.

## Den vigtige forskel: at huske og at bevise

En agent skal ikke kun huske.

Den skal også kunne vise, hvorfor den mener noget.

Det er her, software engineering og AI governance mødes ret naturligt.

Hvis en agent ændrer kode, skal vi kunne se:

- hvad den ændrede
- hvorfor den ændrede det
- hvilke tests der blev kørt
- hvilke tests der ikke blev kørt
- hvilke filer den rørte
- hvilke krav den forsøgte at opfylde
- hvilke risici der stadig findes

Det er meget tæt på almindelig PR-disciplin.

Og måske er det pointen.

Den bedste agent-hukommelse er ikke en mystisk AI-evne. Det er en kombination af gode noter, gode logs, klare opgaver, tests, review og en smule ydmyghed.

Altså: alt det kedelige, der plejer at redde softwareprojekter, når demoen er slut.

## Når agenter arbejder længere, bliver drift vigtigere

OpenAI, Microsoft og GitHub bevæger sig alle i retning af agenter, der arbejder længere og tættere på rigtige workflows.

Det kan være coding agents i GitHub, agentic development i Warp, enterprise-kontekst i Microsoft 365 eller baggrundsopgaver, der ikke bare svarer i en chat, men faktisk forsøger at gennemføre et stykke arbejde.

Det ændrer risikobilledet.

En chatbot, der svarer forkert, er irriterende.

En agent, der arbejder forkert i flere timer med adgang til tools, repositories og interne data, er noget andet.

Derfor bliver de gamle DevOps-spørgsmål pludselig meget moderne igen:

- Hvad må køre automatisk?
- Hvad kræver review?
- Hvor er logs?
- Hvordan opdager vi fejl?
- Hvordan stopper vi processen?
- Hvem ejer ændringen?
- Hvad sker der, når agenten rammer en uklar instruktion?

Det er ikke nok, at agenten er intelligent.

Den skal også være driftbar.

## Agent-ready betyder memory-ready

Jeg tror, mange teams kommer til at tale om, om deres systemer er agent-ready.

Det er et godt spørgsmål.

Men det bør ikke kun handle om API'er.

Et agent-ready system skal også være memory-ready:

1. Dokumentationen skal være opdateret nok til at blive brugt.
2. Beslutninger skal være synlige.
3. Systemgrænser skal være tydelige.
4. Tests og checks skal kunne køres uden drama.
5. Logs skal kunne forklare både menneskelige og agentdrevne handlinger.
6. Opgaver skal have klare stopkriterier.
7. Vigtig viden skal kunne findes igen.

Hvis det lyder som godt platform engineering-arbejde, er det fordi det er det.

AI gør ikke de gamle disciplinproblemer mindre vigtige.

Den gør dem mere synlige.

## Min konklusion

AI-agenter skal bruge API'er.

Men de skal også bruge hukommelse.

Ikke bare som en lang chatlog, men som en struktureret arbejdshukommelse med kilder, beslutninger, status, validering og review.

Ellers får vi agenter, der kan handle uden at kunne forklare sig.

Og det er en dårlig kombination.

Den næste store AI-opgave i virksomheder bliver derfor ikke kun at købe flere agents.

Det bliver at bygge miljøer, hvor agents kan arbejde uden at gøre systemerne mere uklare.

Det handler om kontekst.

Det handler om drift.

Det handler om hukommelse.

Og ja, det betyder desværre, at dokumentation stadig betyder noget.

Beklager.

Læs også:

- [AI-agenter skal bruge API'er](/karpov-blog/posts/ai-agenter-skal-bruge-api-er/)
- [AI er ikke længere en chatbot - det er det nye produktionsapparat](/karpov-blog/posts/ai-er-ikke-laengere-en-chatbot/)
- [DevOps er ikke en pipeline](/karpov-blog/posts/devops-er-ikke-en-pipeline/)
- [Obsidian som selvforbedrende graf](/karpov-blog/posts/obsidian-vault-selvforbedrende-graf/)

## Kilder

- [OpenAI: Warp's big bet on building open source with GPT-5.5](https://openai.com/index/warp/)
- [OpenAI: Codex for almost everything](https://openai.com/index/codex-for-almost-everything/)
- [Microsoft: AI alone won't change your business. The system running it will.](https://blogs.microsoft.com/blog/2026/06/02/ai-alone-wont-change-your-business-the-system-running-it-will/)
- [GitHub Changelog: Copilot CLI improved UI, rubber duck, prompt scheduling and voice input](https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input/)
- [arXiv: Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448)
- [arXiv: Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents](https://arxiv.org/abs/2606.06036)
