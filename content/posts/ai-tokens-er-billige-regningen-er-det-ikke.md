---
title: "AI-tokens er billige. Regningen er det ikke."
date: 2026-07-03
lastmod: 2026-07-03
slug: "ai-tokens-er-billige-regningen-er-det-ikke"
translationKey: "ai-tokens-er-billige-regningen-er-det-ikke"
draft: false
authorship: "legacy-ai-drafted"
description: "En praktisk forklaring på tokenpriser, caching og hvorfor coding agents typisk bruger flere tokens end andre AI-agenter."
summary: "Coding agents læser filer, kører tests og sender en voksende arbejdshistorik gennem modellen. Derfor kan en billig tokenpris stadig blive til en dyr opgave."
tags: ["AI", "AI Agents", "Tokens", "Prompt Caching", "LLM Inference", "DevOps", "Platform Engineering"]
categories: ["AI", "DevOps", "Platform Engineering"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

En token er ikke særlig imponerende.

Det er et ord, et stykke af et ord, et tegn eller noget andet, som en tokenizer har skåret teksten op i.

Alligevel er tokens blevet AI-branchens nye møntfod. Vi køber dem i millioner, får dem i abonnementer og rammer limits på dem.

Og når en coding agent har haft en produktiv eftermiddag, kan usage-siden ligne en mindre kommunes varmebudget.

Det mærkelige er, at én million tokens ofte ser billig ud på prislisten.

Problemet er bare, at agenten sjældent nøjes med én million.

## Den lille prompt, der blev til to millioner tokens

Computerphile viste for nylig et godt eksempel. Mike Pound brugte GitHub Copilot til at lave en lille Windows 3.11-inspireret starfield-screensaver.

Efter omkring seks prompts og arbejde i få filer viste sessionen cirka **to millioner input-tokens og 47.000 output-tokens**.

Det er ikke et benchmark. Det er en konkret demonstration af mekanismen.

Agenten læser ikke kun brugerens spørgsmål. Den får også systeminstruktioner, historik, tidligere svar, tool calls, filindhold, testresultater og fejlbeskeder med som kontekst. Ved næste handling er prompten blevet større.

Den samme fil kan derfor ende på regningen flere gange.

Det er lidt som at hyre en håndværker, der før hvert nyt søm genlæser tilbuddet, byggereglementet og hele WhatsApp-tråden med kunden.

Håndværkeren kan være fremragende.

Men man begynder at forstå timeprisen.

## Hvorfor coding agents bruger flere tokens

En coding agent og en general agent kan være bygget på den samme model. Forskellen ligger ofte i arbejdet omkring den.

En general agent kan finde tre mødetider, opsummere en mailtråd eller hente en ordrestatus. Den kalder nogle få API'er, får kompakte svar tilbage og afslutter opgaven.

En coding agent får typisk denne besked:

> Der er en fejl et sted i systemet. Find den, ret den, og bevis, at du ikke ødelagde noget andet.

Det er ikke bare et spørgsmål.

Det er en lille ekspedition.

Agenten skal måske:

- finde de relevante mapper og filer
- læse kode, konfiguration og tests
- følge afhængigheder på tværs af repoet
- skrive et patch
- køre build, lint og tests
- læse compilerfejl, stack traces og logs
- prøve igen, hvis første løsning fejler
- forklare resultatet til et menneske

Hvert punkt skaber ny kontekst, som kan blive sendt med i næste modelkald.

Kode tåler heller ikke altid et kreativt resume.

```text
Der var noget med authentication. Jeg ordnede det vist.
```

Agenten skal kende de præcise funktionsnavne, typer, imports og fejl. En enkelt parentes kan være forskellen på deployment og eftermiddagsmøde.

Repository-arbejde er desuden en søgeopgave, før det er en kodeopgave. Agenten skal bruge tokens på at finde de fire relevante linjer, før den kan bruge tokens på at ændre dem.

Og bagefter kommer valideringen:

```text
patch -> build -> fejl -> analyse -> nyt patch -> test
```

Det er den rigtige arbejdsgang. Alternativet er kode uden kontrol.

Men hvert loop koster.

Coding agents bruger altså ikke nødvendigvis flere tokens, fordi de er dårligere. De bruger flere, fordi opgaven kræver mere søgning, mere præcision, flere tool calls og flere feedback loops.

Forskellen er ikke absolut. En research-agent med 40 rapporter eller en juridisk agent med tusindvis af sider kan være mindst lige så glubsk.

Coding agents rammer bare meget naturligt alle de dyre mønstre.

De har fået adgang til repoet, terminalen og firmakortet på samme dag.

## Cache hjælper, men cache er ikke hukommelse

Modellen producerer ét token ad gangen. Hvert nyt token bygger på konteksten og det output, der allerede er genereret.

For at undgå at beregne alt helt fra bunden gemmer modellen mellemresultater i en **KV-cache** under genereringen. Det gør arbejdet langt hurtigere, men cachen optager acceleratorhukommelse og vokser med konteksten.

**Prompt caching** er noget andet. Her genbruges en allerede behandlet begyndelse af prompten på tværs af API-kald: for eksempel en systemprompt, tool-definitioner eller et stort dokument.

OpenAI anvender automatisk prompt caching på prompts fra 1.024 tokens. Cache-hits kræver et identisk prefix, så fast indhold bør ligge først og den variable brugerbesked sidst.

Anthropic og Google tilbyder tilsvarende caching. Hos Anthropic koster et cache-hit en tiendedel af normal inputpris, men den første cache-write koster ekstra.

Det er en god handel, hvis cachen faktisk bliver ramt.

Ændrer man instruktionerne, flytter rundt på tools eller sender konteksten i en ny rækkefølge, kan rabatten forsvinde.

Der findes også ineffektivitet som service.

Den vigtigste besparelse ligger derfor ofte i applikationen selv:

- hent kun relevante filer og afsnit
- gem beslutninger som struktureret tilstand
- kompaktér historikken ved naturlige milepæle
- fjern gamle tool outputs
- start en ny session, når den gamle er blevet digitalt pulterkammer

Det er ikke modelmagi.

Det er kontekststyring.

## Hvorfor bliver regningen større?

Det er fristende at sige, at tokens bare bliver dyrere. Men prisen pr. token er faldet for mange modelklasser, mens den samlede regning er vokset.

Vi bruger modellerne til større opgaver, længere kontekster og flere autonome trin.

Vi har gjort benzin billigere og derefter opfundet en bil, der selv kører rundt for at lede efter flere veje.

Prisstrukturen viser også, hvor omkostningen ligger. Den 3. juli 2026 kostede GPT-5.5 på OpenAI's standardniveau 5 dollar pr. million input-tokens, 0,50 dollar for cached input og 30 dollar for output. Ved long context stiger priserne.

Claude Fable 5 stod til 10 dollar for input og 50 dollar for output. Google viste samme grundmønster for Gemini 3.5 Flash: output var markant dyrere end input, mens cached context var billigere.

Tallene kan ikke bruges som en ren rangliste. Modeller, tokenizers, kvalitet og thinking er forskellige.

Men de peger på tre enkle ting:

1. Stærkere modeller og hurtigere service tiers koster mere.
2. Lang kontekst presser beregning og hukommelse.
3. Reasoning, output og agentloops kan få et lille spørgsmål til at vokse voldsomt.

En context window på en million tokens er teknisk imponerende.

Den er ikke en opfordring til at fylde den.

## Effektivitet er pris pr. accepteret resultat

Computerphile gør med rette grin med virksomheder, der måler AI-adoption på, hvor mange tokens medarbejderne bruger.

Det er lidt som at måle en chaufførs kvalitet på dækslid.

Men den agent, der bruger færrest tokens, er heller ikke automatisk bedst. Den kan være billig, fordi den gav op eller producerede kode, som et menneske bagefter bruger fire timer på at reparere.

Den relevante enhed er derfor ikke kun:

> pris pr. million tokens

Den er:

> pris pr. accepteret resultat

For et softwareteam kan det være pris pr. godkendt pull request, løst incident eller feature, der faktisk kom sikkert i drift.

Derfor bør man måle:

- input, cached input og output
- antal agenttrin og tool calls
- cache-hit-rate
- retries og loops
- menneskelig reviewtid
- fejl og genarbejde
- om resultatet blev accepteret

Ellers kan den dyre model se billig ud, fordi den løser opgaven i ét forsøg. Den billige kan blive dyr, fordi den har besluttet sig for at lære gennem gentagelse.

## Min korte tjekliste

1. Log almindeligt input, cached input og output hver for sig.
2. Mål cache-hit-raten. En caching-feature er ikke en besparelse, før den rammer.
3. Hent relevante filer og linjer, ikke hele virksomhedens digitale loftsrum.
4. Kompaktér historikken ved milepæle.
5. Sæt grænser for pris, trin, tid og gentagne fejl.
6. Brug ikke frontier-modellen til arbejde, som en mindre model løser lige så sikkert.
7. Sammenlign modeller på kvalitet, pris og menneskelig indsats på de samme opgaver.

Det lyder mindre futuristisk end en million tokens.

Til gengæld er det sådan, man undgår at betale for den samme fil seks gange.

## Min konklusion

AI-modeller er effektive og ineffektive på samme tid.

De kan løse specialistopgaver på minutter. Men de gør det ved at behandle store mængder kontekst, generere ét token ad gangen og holde en voksende arbejdshukommelse tæt på dyr hardware.

Caching hjælper. Bedre retrieval, compaction, model-routing og stopkriterier hjælper mere.

AI bliver ikke billig, bare fordi prislisten bruger enheden *pr. million*.

Den bliver billig, når systemet bruger den rigtige model, den rigtige kontekst og det rigtige antal trin til at skabe et resultat, nogen faktisk vil beholde.

Så næste gang usage-grafen går lodret, er spørgsmålet ikke kun:

> Hvor mange tokens brugte vi?

Men:

> Hvad fik vi for dem?

Hvis svaret er en testet ændring, der kom sikkert i drift, kan regningen være fin.

Hvis svaret er 14 tool calls, tre genlæste filer og en undskyldning fra agenten, har man ikke købt intelligens.

Man har købt aktivitet.

Softwarebranchen har altid haft rigeligt af det.

## Læs også

- [AI-agenter skal bruge hukommelse](/posts/ai-agenter-skal-bruge-hukommelse/)
- [DevOps er ikke en pipeline](/posts/devops-er-ikke-en-pipeline/)
- [Mit Obsidian-vault fik en lille forskningsafdeling](/posts/obsidian-vault-selvforbedrende-graf/)

## Kilder

- [Computerphile: Why AI Tokens are so Expensive](https://www.youtube.com/watch?v=-0HRzXk8vlk)
- [OpenAI API: Pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API: Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)
- [Anthropic: Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Google AI for Developers: Context caching](https://ai.google.dev/gemini-api/docs/caching)
- [Google AI for Developers: Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs](https://arxiv.org/abs/2512.03324)
- [Accelerating LLM Inference via Dynamic KV Cache Placement in Heterogeneous Memory System](https://arxiv.org/abs/2508.13231)
