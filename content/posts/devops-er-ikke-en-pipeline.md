---
title: "DevOps er ikke en pipeline"
date: 2026-05-22
lastmod: 2026-05-22
draft: false
description: "En kort praktisk note om DevOps, CI/CD, observability, rollback og dokumentation. DevOps er ikke bare YAML med selvtillid."
summary: "DevOps er ikke bare en pipeline. Det er evnen til at få software sikkert fra ide til drift, opdage problemer hurtigt og rette dem uden panik."
tags: ["DevOps", "Platform Engineering", "CI/CD", "Observability", "Azure DevOps", "Kubernetes"]
categories: ["DevOps", "Platform Engineering"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# DevOps er ikke en pipeline

Der er en særlig type optimisme, der opstår, når nogen siger:

> "Vi har DevOps. Vi har en pipeline."

Det er lidt som at sige, at man har et køkken, fordi man ejer en ske.

En pipeline er god. Jeg elsker en pipeline, der bygger, tester og deployer uden at kræve røgelse, tribal knowledge og en bestemt udvikler ved navn Brian.

Men DevOps er ikke bare YAML med selvtillid.

DevOps er det arbejde, der gør software **leverbar, driftbar og forståelig**.

## Den korte version

Et godt DevOps-flow svarer på fem spørgsmål:

- Kan vi bygge det samme artefakt igen?
- Kan vi teste ændringen hurtigt nok til at turde merge?
- Kan vi deploye uden håndholdt ceremonidans?
- Kan vi se, om systemet har det godt bagefter?
- Kan vi rulle tilbage, når virkeligheden får en kreativ ide?

Hvis svaret er nej, har man ikke et DevOps-problem.

Man har fem DevOps-problemer i trenchcoat.

## Start med feedback

Den vigtigste egenskab ved en pipeline er ikke, at den er flot.

Det er, at den giver feedback hurtigt nok til, at nogen stadig kan huske, hvad de lavede.

Build. Test. Security scan. Package. Deploy til et miljø, der ligner virkeligheden nok til ikke at være teater.

Hvis feedback først kommer to dage senere, er det ikke feedback. Det er arkæologi.

DORA peger på de samme grundting igen og igen: små ændringer, automatiserede tests, deployment automation, version control og observability. Ikke fordi det lyder moderne, men fordi det reducerer risikoen ved at ændre software.

## Gør deployment kedeligt

Det bedste deployment er ikke det heroiske deployment.

Det bedste deployment er det, hvor ingen behøver skrive "lige 5 min, jeg deployer" i Slack med den der særlige energi, som får alle til at holde vejret.

Kedelige deployments kræver:

- samme build-artefakt gennem miljøerne
- konfiguration uden hemmelige manuelle klik
- migrations der er tænkt igennem
- feature flags eller anden måde at styre risiko på
- rollback-plan før rollback bliver poesi

Release engineering handler i praksis om reproducerbarhed, automatisering og sporbarhed. Det lyder tørt. Det er også pointen. Produktion belønner sjældent drama.

## Observability er ikke pynt

Logs, metrics og traces er ikke noget, man drysser på systemet bagefter, som persille på en lidt trist suppe.

De er en del af designet.

Når noget fejler, skal teamet kunne svare:

- Hvad skete der?
- Hvilken version kører?
- Hvilke afhængigheder fejler?
- Hvor er latency steget?
- Hvilke brugere eller jobs er ramt?

Hvis svaret er "vi kigger lige i tre portaler og spørger Anders", er systemet ikke observerbart. Det er bare socialt distribueret logging.

OpenTelemetrys grundide er netop at samle signaler som traces, metrics og logs, så man kan forstå systemadfærd på tværs. Det er ikke magi. Det er bedre brødkrummer.

## Dokumentation er også drift

Den mest undervurderede DevOps-disciplin er dokumentation.

Ikke 80 sider i Confluence, som ingen har rørt siden Java 8 var ung og håbefuld.

Men korte noter:

- sådan deployer vi
- sådan fejlsøger vi
- sådan roterer vi secrets
- sådan læser vi dashboardet
- sådan ruller vi tilbage
- sådan ved vi, at alt er normalt

En god runbook er ikke litteratur. Den er en brandvejledning for træt software.

## Min praktiske tjekliste

Hvis jeg skulle forbedre et DevOps-flow i morgen, ville jeg starte her:

1. Find den mest smertefulde manuelle release-opgave.
2. Gør den synlig i pipeline eller dokumentation.
3. Tilføj en hurtig test, der fanger den mest pinlige fejl.
4. Sørg for at deployment efterlader spor: commit, version, miljø, tidspunkt.
5. Lav et dashboard, der viser brugeroplevet sundhed, ikke kun CPU-fitness.
6. Skriv en rollback-note, mens alt er roligt.
7. Gentag uden at kalde det en transformation.

Det sidste punkt er vigtigt.

Hvis hver forbedring kræver en transformation, bliver organisationen til sidst allergisk over for forbedringer.

## Konklusion

DevOps handler ikke om at have flest tools.

Det handler om at gøre ændringer mindre farlige.

En god pipeline hjælper. Kubernetes kan hjælpe. Azure DevOps kan hjælpe. Observability kan hjælpe. AI kan snart hjælpe endnu mere.

Men kun hvis systemet omkring dem er forståeligt.

For DevOps er ikke en pipeline.

DevOps er evnen til at ændre software uden at hele rummet instinktivt begynder at kigge på den samme stakkels person.

Læs også:

- [AI er ikke længere en chatbot - det er det nye produktionsapparat](/karpov-blog/posts/ai-er-ikke-laengere-en-chatbot/)
- [Project Glasswing - Når AI finder de fejl mennesker overser](/karpov-blog/posts/project-glasswing/)
- [Portfolio: DevOps, Platform Engineering og .NET](/karpov-blog/projekter/)

## Kilder

- [DORA: Continuous delivery](https://dora.dev/capabilities/continuous-delivery/)
- [Google SRE Book: Release Engineering](https://sre.google/sre-book/release-engineering/)
- [OpenTelemetry: Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
