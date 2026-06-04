---
title: "AI-agenter skal bruge API'er"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "En kort note om hvorfor AI-agenter hurtigt bliver et API-, governance- og platform engineering-problem."
summary: "Postman, Microsoft og OpenAI peger i samme retning: AI-agenter skal ikke kun blive klogere. De skal kunne arbejde mod rigtige systemer med kontekst, adgangsstyring, logs og klare grænser."
tags: ["AI", "AI Agents", "APIs", "DevOps", "Platform Engineering", "Governance"]
categories: ["AI", "DevOps"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# AI-agenter skal bruge API'er

AI-agenter har fået et meget almindeligt softwareproblem:

De skal bruge API'er.

Det lyder tørt. Det er også pointen.

Postman har lanceret en AI Engineer, der kan arbejde med API-design, root cause analysis og PR-checks. Microsoft gør Work IQ APIs klar til Microsoft 365, så agenter kan hente forretningskontekst og handle via færre, mere agentvenlige tools. OpenAI flytter Codex længere ind i enterprise-flows og AWS.

Det er tre forskellige produktnyheder.

Men de peger på den samme bevægelse:

AI er ved at få en integrationsflade.

## Den nye flaskehals er kontekst

Den første bølge af AI-snak handlede meget om svaret.

Kan modellen skrive kode? Kan den forklare fejlen? Kan den lave en plan?

Det er stadig relevant. Men i rigtige systemer er det sjældent nok.

En agent, der skal hjælpe med software, skal vide mere end hvordan en god funktion ser ud i isolation. Den skal forstå kontrakter, afhængigheder, navngivning, ejerskab, miljøer, data, permissions og de mærkelige lokale regler, som ikke står i dokumentationen, men alligevel styrer halvdelen af systemet.

Postman kalder blandt andet problemet for context debt. Det er et godt begreb.

For når agenter kan producere mere kode, flere tests, flere ændringer og flere forslag, vokser behovet for fælles systemforståelse også. Ellers får man ikke hurtigere softwareudvikling. Man får bare hurtigere forvirring med pænere commit-beskeder.

## Fra chatbot til platformoverflade

Det interessante ved de nye agent-nyheder er ikke kun, at værktøjerne bliver smartere.

Det interessante er, at de bliver koblet på de steder, hvor arbejdet allerede foregår:

- API-kataloger
- pull requests
- sandboxes
- dokumentation
- Microsoft 365-data
- enterprise cloud-miljøer
- eksisterende governance- og sikkerhedsmodeller

Det ændrer spørgsmålet.

Det handler ikke kun om:

> Hvor god er modellen?

Det handler også om:

- Hvilke endpoints må agenten kalde?
- Hvilke credentials får den?
- Hvad kører i en sandbox?
- Hvad kræver menneskelig godkendelse?
- Hvor bliver handlinger logget?
- Hvem ejer kontrakten?
- Hvordan opdager vi, at agenten har misforstået systemet?
- Hvordan ruller vi tilbage?

Det er ikke den slags spørgsmål, der giver de flotteste keynote-slides.

Til gengæld er det den slags spørgsmål, der afgør, om teknologien kan bruges uden at skabe en ny type driftsproblem.

## Agent-æraen bliver platformarbejde

Jeg tror, mange virksomheder kommer til at undervurdere det her.

De kommer til at spørge:

> Hvilken agent skal vi købe?

Det bedre spørgsmål er måske:

> Hvilken platform skal agenten lande i?

Hvis API'erne er utydelige, permissions er rodede, dokumentationen er gammel, og ingen ved, hvem der ejer hvad, bliver agenten ikke pludselig klog af at få adgang.

Den bliver bare endnu en bruger af et uklart system.

Omvendt bliver gode interne platforme mere værdifulde. Klare API-kontrakter, driftbar dokumentation, observability, security boundaries og gode review-processer er ikke kun rare for mennesker. De bliver også det grundlag, agenter skal arbejde på.

Det er en ret vigtig pointe:

Agent-ready software ligner meget af det, vi allerede burde bygge.

Bare med mindre tolerance for rod.

## Min korte tjekliste

Hvis et team vil gøre sig klar til AI-agenter, ville jeg starte med noget ret jordnært:

1. Find de vigtigste interne API'er.
2. Gør ejerskab og kontrakter tydelige.
3. Sørg for, at logs kan forklare både menneskelige og agentdrevne handlinger.
4. Brug sandboxes til alt, der kan ændre noget.
5. Kræv menneskelig godkendelse ved irreversible eller risikable ændringer.
6. Test agentens forslag som alle andre ændringer.
7. Skriv runbooks, før den første agent får lov at "hjælpe" i nærheden af produktion.

Det lyder måske lidt konservativt.

Det er fint.

Produktion er også et konservativt sted. Den belønner ikke begejstring alene.

## Konklusion

AI-agenter bliver ikke kun et AI-problem.

De bliver et API-problem, et governance-problem og et platform engineering-problem.

Det er faktisk en god nyhed.

For det betyder, at den næste fase af AI ikke kun handler om at vælge den rigtige model. Den handler om at bygge de rigtige rammer omkring den.

Hvem må agenten tale med?

Hvad må den gøre?

Hvordan ser vi, hvad der skete?

Og hvordan stopper vi den igen?

Hvis de spørgsmål er på plads, bliver agenter langt mere interessante.

Hvis ikke, får vi bare automatisering oven på uklarhed.

Og det har softwarebranchen, trods alt, allerede ret god erfaring med.

Læs også:

- [AI er ikke længere en chatbot - det er det nye produktionsapparat](/karpov-blog/posts/ai-er-ikke-laengere-en-chatbot/)
- [DevOps er ikke en pipeline](/karpov-blog/posts/devops-er-ikke-en-pipeline/)
- [EU AI Act i praksis: transparens er ikke bare en pop-up](/karpov-blog/posts/eu-ai-act-transparens-er-ikke-bare-en-popup/)

## Kilder

- [Postman: Introducing the AI Engineer](https://blog.postman.com/introducing-the-ai-engineer/)
- [Microsoft 365 Blog: Announcing the new Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/)
- [OpenAI: OpenAI frontier models and Codex are now available on AWS](https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/)
- [OpenAI: Codex for every role, tool, and workflow](https://openai.com/index/codex-for-every-role-tool-workflow/)
