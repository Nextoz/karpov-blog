---
title: "Project Glasswing — Når AI finder de fejl mennesker overser"
date: 2026-04-16
lastmod: 2026-05-19
description: "Anthropics Project Glasswing bruger AI til at finde kritiske sikkerhedssårbarheder i open source software. Hvad betyder det for DevOps og cybersikkerhed?"
tags: ["AI", "Cybersecurity", "DevOps"]
categories: ["Teknologi"]
author: "Evgeny Karpov"
summary: "En AI-model fandt en 27 år gammel sikkerhedssårbarhed i OpenBSD. Det er Project Glasswing — og det ændrer alt for defensiv sikkerhed."
ShowReadingTime: true
---

Anthropic lancerede i april 2026 **Project Glasswing**: et initiativ hvor frontier AI bruges defensivt til at finde og rette sikkerhedssårbarheder i kritisk software.

Det mest opsigtsvækkende eksempel er en **27 år gammel sårbarhed i OpenBSD**. Ifølge Anthropics tekniske gennemgang har Claude Mythos Preview også vist markant stærkere evner til at finde, reproducere og i nogle tilfælde udnytte sårbarheder end tidligere modeller.

Det er ikke kun interessant for sikkerhedsforskere. Det er interessant for alle os der bygger og driver software.

## Hvad betyder det for DevOps?

Som DevOps- og infrastrukturperson tænker jeg ikke kun: "AI kan finde flere fejl."

Jeg tænker:

- Hvor hurtigt kan vi triagere fund?
- Hvor hurtigt kan vi patche?
- Hvor sikkert kan vi deploye?
- Kan vi se effekten i logs og dashboards?
- Har vi rollback klar hvis en sikkerhedsrettelse knækker noget?

Hvis AI øger hastigheden på sårbarhedsfinding, bliver flaskehalsen hurtigt alt det bagefter: prioritering, test, release, kommunikation og drift.

Det er her DevOps bliver relevant. Ikke som buzzword, men som den praktiske disciplin der forbinder udvikling, sikkerhed og produktion.

## En praktisk forsvarsliste

Hvis man vil forberede sig på en verden med AI-assisteret sårbarhedsfinding, ville jeg starte her:

- Kend dine vigtigste open source-afhængigheder.
- Sørg for at dependency scanning faktisk bliver fulgt op.
- Gør patch-deployments hurtigere og mindre dramatiske.
- Hav gode miljøer til at teste sikkerhedsrettelser.
- Brug observability til at se om rettelser ændrer systemadfærd.
- Dokumentér hvordan kritiske sårbarheder prioriteres.
- Lad AI hjælpe med analyse, men behold menneskelig validering.

Det positive er, at værktøjerne nu begynder at komme i hænderne på forsvarerne. Det er et kapløb, og vi skal sørge for at de vinder det.

Læs også:

- [DevOps er ikke en pipeline](/karpov-blog/posts/devops-er-ikke-en-pipeline/)
- [AI er ikke længere en chatbot - det er det nye produktionsapparat](/karpov-blog/posts/ai-er-ikke-laengere-en-chatbot/)

---

Kilder:

- [Anthropic: Project Glasswing](https://www.anthropic.com/project/glasswing)
- [Anthropic Frontier Red Team: Assessing Claude Mythos Preview's cybersecurity capabilities](https://red.anthropic.com/2026/mythos-preview/)
