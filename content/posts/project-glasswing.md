---
title: "Project Glasswing — Når AI finder de fejl mennesker overser"
date: 2026-04-16
lastmod: 2026-05-27
description: "Anthropics Project Glasswing viser, at AI kan hjælpe med defensiv sikkerhed. Den svære del for teams bliver triage, patching, rollout, observability og drift."
tags: ["AI", "Cybersecurity", "DevOps", "Platform Engineering", "Open Source"]
categories: ["Teknologi", "DevOps"]
author: "Evgeny Karpov"
summary: "Project Glasswing er interessant, fordi AI kan finde flere sikkerhedsfejl. Men den praktiske flaskehals bliver alt det bagefter: triage, patching, rollout, observability og incident response."
ShowReadingTime: true
---

Anthropic lancerede i april 2026 **Project Glasswing**: et initiativ hvor frontier AI bruges defensivt til at finde og rette sikkerhedssårbarheder i kritisk software.

Det mest opsigtsvækkende eksempel er en **27 år gammel sårbarhed i OpenBSD**. Ifølge Anthropics tekniske gennemgang har Claude Mythos Preview også vist markant stærkere evner til at finde, reproducere og i nogle tilfælde udnytte sårbarheder end tidligere modeller.

Det er ikke kun interessant for sikkerhedsforskere. Det er interessant for alle os, der bygger og driver software.

## Hvad vi ved, og hvad jeg læser ud af det

Det bekræftede er, at Anthropic præsenterer Project Glasswing som et defensivt sikkerhedsinitiativ, og at deres egen evaluering af Claude Mythos Preview viser stærkere cybersecurity-evner end tidligere modeller.

Min analyse er den her:

Hvis den slags værktøjer bliver almindelige, bliver sikkerhedsarbejde mindre afhængigt af, om nogen overhovedet finder fejlen. Flere fejl bliver fundet. Hurtigere.

Det flytter presset.

Fra discovery til delivery.

Fra "kan vi finde sårbarheden?" til "kan vi reagere uden at ødelægge produktion?"

## Hvad betyder det for DevOps?

Som DevOps- og infrastrukturperson tænker jeg ikke kun: "AI kan finde flere fejl."

Jeg tænker:

- Hvor hurtigt kan vi triagere fund?
- Hvor hurtigt kan vi patche?
- Hvor sikkert kan vi deploye?
- Kan vi se effekten i logs og dashboards?
- Har vi rollback klar hvis en sikkerhedsrettelse knækker noget?

Hvis AI øger hastigheden på sårbarhedsfinding, bliver flaskehalsen hurtigt alt det, der kommer bagefter: prioritering, test, release, kommunikation og drift.

Det er her DevOps bliver relevant. Ikke som buzzword, men som den praktiske disciplin der forbinder udvikling, sikkerhed og produktion.

## En praktisk forsvarsliste

Hvis man vil forberede sig på en verden med AI-assisteret sårbarhedsfinding, ville jeg starte her:

- Kend dine vigtigste open source-afhængigheder og deres ejere.
- Lav SBOM eller anden afhængighedsoversigt for kritiske systemer.
- Sørg for, at dependency scanning faktisk bliver fulgt op.
- Gør patch-deployments hurtigere og mindre dramatiske.
- Hav gode miljøer til at teste sikkerhedsrettelser.
- Brug observability til at se, om rettelser ændrer systemadfærd.
- Dokumentér, hvordan kritiske sårbarheder prioriteres.
- Øv rollback, før du står med en hastesag fredag eftermiddag.
- Lad AI hjælpe med analyse, men behold menneskelig validering.

## Spørgsmål danske teams bør stille

Jeg ville starte med fem ret jordnære spørgsmål:

1. Hvem ejer vores mest kritiske dependencies?
2. Hvor hurtigt kan vi patche en kritisk sårbarhed i produktion?
3. Kan vi se i logs, metrics og traces, om patchen ændrer systemadfærd?
4. Hvem må godkende en hastedeployment?
5. Har vi en runbook, der faktisk kan bruges, når der er pres på?

Hvis svaret er uklart, er AI ikke problemet endnu. Så er problemet, at organisationen ikke har bygget musklen til at reagere.

Det positive er, at værktøjerne nu begynder at komme i hænderne på forsvarerne. Det er et kapløb, og vi skal sørge for, at de vinder det.

Læs også:

- [DevOps er ikke en pipeline](/karpov-blog/posts/devops-er-ikke-en-pipeline/)
- [AI er ikke længere en chatbot - det er det nye produktionsapparat](/karpov-blog/posts/ai-er-ikke-laengere-en-chatbot/)

---

Kilder:

- [Anthropic: Project Glasswing](https://www.anthropic.com/project/glasswing)
- [Anthropic Frontier Red Team: Assessing Claude Mythos Preview's cybersecurity capabilities](https://red.anthropic.com/2026/mythos-preview/)
