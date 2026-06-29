---
title: "AI-agenter holder ikke sommerferie. Men de kræver stadig en god overlevering."
date: 2026-06-29
lastmod: 2026-06-29
slug: "ai-agenter-holder-ikke-sommerferie"
translationKey: "ai-agenter-holder-ikke-sommerferie"
draft: false
description: "AI-agenter kan arbejde parallelt og længe. Sommerens egentlige platformtest er, om de kan stoppes, kontrolleres og reviewes, mens halvdelen af teamet er på ferie."
summary: "60 agenttimer på en dag er ikke det samme som 60 timers værdi. Når agenter arbejder videre, flytter flaskehalsen til overlevering, isolation, review og stopkriterier."
tags: ["AI", "AI Agents", "DevOps", "Platform Engineering", "GitHub Copilot", "AGENTS.md"]
categories: ["AI", "DevOps", "Platform Engineering"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# AI-agenter holder ikke sommerferie. Men de kræver stadig en god overlevering.

Det er sommer.

Halvdelen af Danmark har sat autosvar på mailen. Den anden halvdel holder Teams-status grøn fra et sommerhus med tvivlsomt Wi-Fi.

AI-agenterne arbejder imens videre.

OpenAI offentliggjorde den 25. juni en analyse af, hvordan Codex bliver brugt internt. Blandt de mest intensive daglige brugere – den øverste ene procent – blev der jævnligt kørt mere end 60 timers Codex-agentkørsel på én dag, fordelt på flere parallelle agenter.

Det er et imponerende tal.

Det er også et tal, der fortjener en lille parasol.

For 60 timers agentkørsel er ikke det samme som 60 timers værdi. En løvblæser kan også arbejde hele dagen. Det gør ikke haven strategisk.

## Den nye flaskehals er ikke arbejdstid

Når en agent kan arbejde i flere timer og flere agenter kan arbejde samtidig, bliver produktion af ændringer billigere.

Til gengæld bliver noget andet dyrere:

- at formulere opgaven præcist
- at give den rigtige kontekst
- at holde arbejdet isoleret
- at kontrollere resultatet
- at afgøre, hvad der må merges
- at stoppe arbejdet, når forudsætningerne ændrer sig

GitHub har gjort Copilot-appen generelt tilgængelig med parallelle sessions på hver sin branch og worktree. Der er integreret terminal, browser, diff og de eksisterende PR-checks. GitHub Desktop 3.6 understøtter nu også worktrees direkte, netop fordi mennesker og coding agents i stigende grad arbejder på flere grene samtidig.

Det er en vigtig produktbevægelse.

AI-værktøjerne handler mindre om at få ét hurtigt svar og mere om at drive en kø af arbejde.

Og en kø af arbejde er et driftssystem.

Hvis fem agenter åbner fem pull requests, har man ikke automatisk fået fem forbedringer.

Man har fået fem ting, nogen skal forstå.

## Overleveringen er flyttet ind i repoet

En anden lille, men ret afslørende nyhed kom fra GitHub den 18. juni: Copilot code review kan nu læse en `AGENTS.md` i roden af et repository og bruge den som kontekst for reviewet.

GitHub Desktop bruger også instruktioner fra `AGENTS.md`, når Copilot hjælper med commit-beskeder.

Det lyder som en filformatdetalje.

Det er i virkeligheden en personalehåndbog i Markdown.

Her kan et team beskrive:

- hvad agenten skal læse først
- hvilke filer den ikke må ændre
- hvilke tests der skal køres
- hvilke kommandoer projektet bruger
- hvilke sikkerhedsgrænser der gælder
- hvornår et menneske skal godkende arbejdet
- hvordan et færdigt resultat dokumenteres

Det er ikke en garanti for, at agenten gør alt rigtigt.

Men det er bedre end den klassiske sommeroverlevering:

> Spørg Mads. Han er tilbage i uge 32.

## Sommerferie er en fremragende platformtest

Et system er ikke robust, fordi det virker, mens alle sidder i samme rum og den person, der byggede det, har telefonen tændt.

Det er robust, når arbejdet kan fortsætte kontrolleret, selv om halvdelen af teamet spiser is et sted uden for Slack-rækkevidde.

Det gælder også agentarbejde.

Før man sender agenterne på digital sommerlejr, ville jeg kontrollere fem ting.

### 1. Efterlad en rigtig overlevering

Skriv mål, grænser, relevante kommandoer og validering tæt på koden. Brug `AGENTS.md`, README-filer, runbooks og issue-skabeloner til forskellige ting, men sørg for, at de ikke modsiger hinanden.

En agent kan ikke læse den fælles forståelse, som kun findes i et Teams-møde fra april.

Det kan nye kolleger i øvrigt heller ikke.

### 2. Isolér arbejdet

Én opgave, én branch, ét worktree og en tydelig ejer er et godt udgangspunkt.

Parallelisme uden isolation er bare en hurtigere måde at opdage merge conflicts på.

### 3. Begræns work in progress efter reviewkapacitet

Hvis ingen kan reviewe noget før august, behøver agenten måske ikke åbne 47 pull requests i juli.

En voksende kø er ikke produktivitet. Den er lagerbinding med flotte commit-beskeder.

### 4. Definér stopkriterier

Agenten skal vide, hvornår den skal stoppe og bede om hjælp:

- når tests fejler på en ukendt måde
- når opgaven kræver nye credentials eller permissions
- når ændringen påvirker produktion eller data
- når kilder eller krav modsiger hinanden
- når den er ved at udvide opgaven for at løse opgaven

Den sidste er særlig vigtig. AI-agenter kan være meget hjælpsomme på den måde, hvor man beder om en hylde og kommer hjem til en tilbygning.

### 5. Automatisér checks, ikke dømmekraft

Lad agenten bygge, teste, lint'e, scanne og dokumentere.

Lad de eksisterende branch policies, required checks og reviewkrav gælde som normalt.

Og lad være med at gøre sommerferien til pilotprojekt for automatisk deployment til produktion, medmindre I allerede har testet rollback, alarmer og ansvar grundigt.

En strand er et dårligt incident room. Sand er elendigt til tastaturer.

## Flere agenttimer kræver mere platform engineering

OpenAI's tal kommer fra OpenAI's egen brug og kan ikke uden videre oversættes til alle virksomheder. Men retningen er tydelig i produkterne: længere opgaver, flere parallelle sessions, cloud automation, worktrees og repository-specifikke instruktioner.

Det gør ikke platform engineering mindre vigtigt.

Det flytter platformens ansvar.

Den skal ikke kun hjælpe mennesker med at levere kode. Den skal også gøre agentarbejde:

- afgrænset
- observerbart
- reproducerbart
- reviewbart
- billigt nok
- muligt at stoppe

Den relevante måling er derfor ikke kun agenttimer.

Det er godkendte ændringer, fejl fanget før merge, tid brugt på review, genarbejde, omkostninger og hændelser, der aldrig nåede produktion.

Ellers risikerer vi at optimere for maksimal aktivitet og opdage værdien efter ferien.

Det har softwarebranchen prøvet før. Dengang kaldte vi det bare mange projekter.

## Min konklusion

AI-agenter holder ikke sommerferie.

Det betyder ikke, at de skal have lov til at arbejde uden opsyn hele juli.

Det betyder, at teams har brug for bedre overlevering, tydeligere grænser, isolerede arbejdsområder, automatiske checks og en reviewkø, der passer til den menneskelige kapacitet.

En god agentplatform skal gøre det lettere for mennesker at holde fri.

Ikke skabe en mere udholdende kilde til notifikationer.

Så før autosvaret bliver slået til, er sommerens bedste AI-spørgsmål måske ikke:

> Hvor mange timer kan agenten arbejde for os?

Men:

> Kan den arbejde sikkert, forklare resultatet og stoppe igen, uden at ringe til nogen på stranden?

Hvis svaret er ja, har I måske bygget en platform.

Hvis svaret er nej, har I bygget en meget energisk sommervikar.

God ferie.

## Læs også

- [AI-agenter skal bruge hukommelse](/karpov-blog/posts/ai-agenter-skal-bruge-hukommelse/)
- [AI-agenter skal bruge API'er](/karpov-blog/posts/ai-agenter-skal-bruge-api-er/)
- [DevOps er ikke en pipeline](/karpov-blog/posts/devops-er-ikke-en-pipeline/)
- [Claude Fable 5 er ikke bare en ny model. Det er en platformtest.](/karpov-blog/posts/claude-fable-5-er-en-platformtest/)

## Kilder

- [OpenAI: How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)
- [GitHub Changelog: GitHub Copilot app generally available](https://github.blog/changelog/2026-06-17-github-copilot-app-generally-available/)
- [GitHub Changelog: Copilot code review – AGENTS.md support and UI improvements](https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements/)
- [GitHub Changelog: GitHub Desktop 3.6 – Worktrees and deeper Copilot integration](https://github.blog/changelog/2026-06-26-github-desktop-3-6-worktrees-and-deeper-copilot-integration/)
