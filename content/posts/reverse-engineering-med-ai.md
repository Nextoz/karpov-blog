---
title: "Reverse engineering med AI: ringen til 191 kroner"
date: 2026-11-11
lastmod: 2026-11-11
slug: "reverse-engineering-med-ai"
translationKey: "reverse-engineering-med-ai"
draft: false
authorship: "legacy-ai-drafted"
description: "Jeg købte en billig smart ring, fik en anden model end forventet og brugte AI til at kortlægge dens Bluetooth-protokol. Her er metoden, fejlene og reglerne."
summary: "AI gør det meget billigere at læse en ukendt protokol. Den gør det ikke billigere at bevise, at man har læst rigtigt. Et forløb med en smart ring, en Windows-pc og en coding agent."
tags: ["AI", "AI Agents", "Reverse Engineering", "Bluetooth", "Security", "Data Ownership"]
categories: ["AI", "Security"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

Jeg bestilte en smart ring til 191 kroner inklusive fragt.

Annoncen sagde "R09", og jeg regnede med en COLMI R09, fordi der findes god open source til den. Jeg havde forberedt mig: en protokoltabel, to referenceprojekter og en plan for, hvordan målingerne skulle ende i mit eget vault og ikke i en producents cloud.

Så kom ringen.

På æsken stod der "SMART RING" og fem modelnumre med afkrydsningsfelter. Ingen af dem var krydset af, og R09 var ikke på listen. Manualen bad mig installere en helt anden app end den, jeg havde læst om.

Hele min forberedelse passede til en anden ring.

Dette indlæg handler om, hvad jeg gjorde bagefter, og hvad jeg lærte om at bruge AI til reverse engineering. Den korte version er, at AI gør læsearbejdet meget billigere. Beviset koster det samme som før.

## Hvorfor ikke bare bruge producentens app?

Der var tre grunde.

Appen kræver en konto, og dens privatlivsmærkat nævner kontaktoplysninger og lokation. Jeg vil gerne have mine søvn- og pulsdata, men jeg har ikke brug for, at andre også får dem.

Udviklerne bag Gadgetbridge har desuden rapporteret, at en app i samme familie sender data til sin cloud uden TLS.

Og så viser ringen blodsukker. Den har ingen sensor til det. Ifølge kildekoden i open source-appen PulseLoop bliver tallet beregnet ud fra brugerprofilen: køn, alder, højde og vægt. Ændrer man profilen, ændrer blodsukkeret sig.

Det er ikke en måling. Det er et regneark med Bluetooth.

## Trin 1: Find ud af, hvad du faktisk har

Det første, jeg bad min coding agent om, var ikke at hente data. Det var at finde ud af, hvilken enhed der lå på bordet.

Et Bluetooth-scan gav navnet `SMART_RING` og en service med id'et `0x56FF`. Ringen modtager kommandoer på én characteristic og svarer på en anden. Hver besked er 20 bytes, kommandoen står i den første byte, og der er hverken checksum eller kryptering.

COLMI-ringene bruger en anden service og 16 bytes med checksum. Der var altså ikke noget i mine forberedte parsere, der kunne genbruges.

Det lyder som en detalje, men det er her, de fleste forløb af denne type går galt. Hvis agenten havde fået lov til at fortsætte med den protokol, vi troede på, havde den sendt kommandoer til en enhed, der forstår noget andet ved de samme bytes.

## Trin 2: Læs, hvad andre allerede har fundet

Jeg var ikke den første med sådan en ring. Der findes en write-up om familien, en open source-app til iPhone (PulseLoop), en pull request til Gadgetbridge og en analyse af producentens SDK.

Her er AI virkelig stærk. At læse flere tusinde linjer Swift, som en anden har skrevet, og trække en protokoltabel ud af dem, er arbejde, der før tog dage. Nu tager det minutter.

Den fandt også en modsigelse. PulseLoops dokumentation siger, at ringfamilien ikke har nogen temperatursensor. Men koden læser en bitmaske over ringens funktioner, hvor bit 10 betyder temperatur. På min ring er bit 10 sat.

Dokumentation og kode var uenige, og ingen af dem kunne afgøre det. Det kunne kun ringen.

Der var også en blindgyde. Vi fandt et protokoldokument fra producenten i et offentligt repo. Det beskrev en anden enhedsfamilie med en anden service og andre beskeder. Det så autoritativt ud og var ubrugeligt.

## Trin 3: Spørg ringen, men kun med læsekommandoer

Selve laboratoriet er beskedent: en Windows-pc, Python og biblioteket `bleak`. Agenten skrev en håndfuld små scripts til at scanne, sende forespørgsler, hente historik og afkode svarene.

Reglerne var vigtigere end koden:

- Forespørgsler først. Indstillinger må kun ændres med kommandoer, vi allerede kender virkningen af, som at stille uret.
- Alle rå svar gemmes, præcis som de kom.
- En skriftlig liste over det, der aldrig må sendes: alt på ringens to firmware-services, nulstilling, afbinding og testtilstand.

Den sidste liste er ikke pedanteri. Ringen kan opdatere sin firmware trådløst. En agent, der "lige prøver" en ukendt kommando på den forkerte service, kan forvandle ringen til et meget lille stykke smykke.

## Trin 4: Bevis det mod noget, du kan se

Det bedste fund kom fra en kommando, der var dokumenteret som søvnhistorik.

På min ring svarede den med noget andet: én besked pr. kvarter, hver med 15 små tal. Hypotesen var skridt pr. minut. Men en hypotese om bytes er billig, og AI producerer dem gerne i store mængder.

Testen var enkel. Vi lagde alle minutværdierne for dagen sammen. Summen blev 1459. Ringens egen totaltæller for dagen, som hentes med en helt anden kommando, sagde også 1459.

<figure>
  <img src="/images/ring-frame-decoded.svg" alt="En Bluetooth-besked på 20 bytes skilt ad: første byte er kommandoen 0x10, de næste fire er et tidsstempel, og de sidste femten er skridt pr. minut. Summen for dagen er 1459, det samme som ringens egen total." width="1200" height="660" loading="lazy">
  <figcaption>Én besked fra ringen. Bytes og minutværdier er et eksempel; opdelingen og summen er fra min egen ring.</figcaption>
</figure>

Først dér var det viden og ikke et gæt. Og det var data, som open source-appen ikke afkodede.

Modeksemplet er lige så lærerigt. En anden kommando returnerer fem tal hver halve time. De to første ligner blodtryk. De tre sidste kan være træthed, stress og HRV, i en eller anden rækkefølge.

En sprogmodel sætter gerne etiketter på dem med stor selvtillid. I mine noter står de stadig som uverificerede, indtil de er sammenlignet med producentens app for det samme tidsrum.

Temperaturen fik samme behandling. Afkoderen accepterer kun værdier, der lander mellem 30 og 43 grader efter skalering. Alt andet vises som ingenting, men bliver liggende i den rå log, så det kan afkodes rigtigt senere.

## Det, der ikke virkede

**Måling på kommando.** Fra pc'en kunne vi ikke starte en pulsmåling. Ringen gentog kommandoen som kvittering, men dioden forblev slukket, og der kom ingen data. Vi prøvede flere varianter af opstartssekvensen.

Mit bidrag var at sidde med ringen på fingeren og sige "nej, den lyser stadig ikke". Agenten kan ikke se en diode. I dette forløb var jeg dens sensor.

**Ringen holdt op med at måle.** Samme aften var der intet lys, ingen nye målinger, og skridttælleren stod stille, mens jeg gik rundt. Min første tanke var, at vi havde ødelagt den.

Loggen sagde noget andet. Den første kommando fra pc'en blev sendt 18.57. Målingen kl. 18.45 manglede allerede. Fejlen var begyndt, før vi rørte ved ringen.

En fabriksnulstilling i producentens app løste det og slettede samtidig ringens historik.

To ting tog jeg med derfra. Sæt tidsstempel på alt, for det er det eneste alibi, man har. Og hent data ofte, for enheden er ikke et arkiv.

## Fra protokol til app, uden en Mac

Protokollen blev kortlagt på en aften. Dagen efter lå der en appudgave klar.

Jeg lavede en fork af PulseLoop, som er udgivet under CC BY 4.0, og fik agenten til at tilføje det, vi havde fundet: syv dages historik, skridt pr. kvarter, en rå log over alle beskeder i 30 dage, redigerbare søvnvinduer og en genvej, der afleverer data videre til mit eget system. Ingen konto og ingen cloud.

Der var ét praktisk problem: Jeg har en Windows-pc, og en iPhone-app skal bygges på en Mac.

Løsningen blev en macOS-runner i GitHub Actions, der tester koden og bygger appen. Jeg installerer resultatet fra Windows med en gratis signatur, som udløber hver syvende dag.

iOS-simulatoren har ikke Bluetooth. Hver eneste rigtige test foregår derfor på min egen telefon med ringen på fingeren. Agenten skriver koden, CI bygger den, og jeg er testmiljøet.

## Hvad AI er god og dårlig til i reverse engineering

Efter dette forløb vil jeg dele det sådan her.

**AI er god til:**

- at læse fremmed kode og dokumentation hurtigt og på tværs af kilder
- at skrive engangsværktøjer: en scanner, en afkoder, et script til at hente historik
- at foreslå, hvordan bytes kan være opdelt
- at føre laboratoriejournal, så man dagen efter ved, hvad der er testet

**AI er dårlig til:**

- at kende forskel på det, den ved, og det, den gætter. Begge dele bliver formuleret lige sikkert.
- at se den fysiske verden. Lyser dioden? Sidder ringen på en finger? Det ved kun mennesket.
- at opdage, at en kilde er forkert. Den arver fejl fra dokumentation, der ser officiel ud.
- at stoppe. En agent vil gerne videre, også når næste skridt er en kommando, ingen kender virkningen af.

Det ændrer arbejdsdelingen. Før var flaskehalsen at læse og forstå. Nu er flaskehalsen at kontrollere.

## Mine regler

1. **Identificér, før du genbruger.** Navnet i annoncen er ikke enhedens identitet.
2. **Læs andres arbejde først.** Det meste er fundet af nogen. Giv dem kredit, og respektér licensen.
3. **Start med læsekommandoer.** Skriv ned, hvad der aldrig må sendes, før agenten får adgang.
4. **Gem de rå svar.** Byg testdata af det, enheden faktisk sendte. Opfind dem aldrig.
5. **En parser er først rigtig, når den stemmer med noget uafhængigt.** En total, en skærm i den originale app eller en anden måling.
6. **Markér alt som verificeret eller uverificeret.** Også når det er fristende at lade være.
7. **Eksperimentér ikke på den enhed, du er afhængig af.** Vil man prøve egen firmware, køber man en ring mere.
8. **Hold rådata privat.** Mine optagelser indeholder enhedens adresse og helbredsdata. De kommer aldrig i et repo.

## Det gælder ikke kun ringe

Jeg har brugt en ring som eksempel, men metoden er den samme, når man står med et legacy-system uden dokumentation, et filformat fra en leverandør, der er lukket, eller en integration mod et API, som ingen længere kan forklare.

For en platform engineer er det ret almindelige arbejdsdage. Forskellen er, at det nu kan betale sig at forstå systemer, man før lod ligge, fordi læsearbejdet var for dyrt.

Der er også en bagside. Meget billig elektronik har været beskyttet af, at ingen gad kigge. Forbindelsen til min ring er ukrypteret. Ifølge analysen af producentens SDK hentes firmwareopdateringer over almindelig HTTP med en MD5-sum som eneste kontrol.

Når det tager mig en aften at læse protokollen, tager det også andre en aften. Det er ikke en grund til panik. Det er en grund til at holde op med at regne uklarhed for sikkerhed.

En sidste bemærkning: Jeg har arbejdet på min egen ring og mine egne data, holdt mig fra firmwaren og bygget videre på open source med navngiven licens. Jeg er ikke jurist, så undersøg selv reglerne, før du piller ved andres software.

## Min konklusion

Ringen kostede 191 kroner. Det, jeg fik for pengene, var mindre et sundhedsprodukt og mere en øvelse i at finde ud af, hvad en enhed faktisk gør.

AI gjorde øvelsen mulig på en aften. Den læste kilderne, skrev værktøjerne og holdt styr på noterne.

Men hver gang noget blev til viden, skyldtes det en kontrol, den ikke selv kunne udføre: en sum, der stemte, en diode, der ikke lyste, og et tidsstempel, der viste, at fejlen kom før os.

AI læste protokollen. Ringen måtte selv bekræfte den.

## Læs også

- [AI-agenter skal bruge hukommelse](/posts/ai-agenter-skal-bruge-hukommelse/)
- [AI-tokens er billige. Regningen er det ikke.](/posts/ai-tokens-er-billige-regningen-er-det-ikke/)
- [DevOps er ikke en pipeline](/posts/devops-er-ikke-en-pipeline/)

## Kilder

- [PulseLoop iOS](https://github.com/saksham2001/PulseLoopiOS) (CC BY 4.0), som min fork bygger på
- [Min fork: Nextoz/PulseLoopiOS](https://github.com/Nextoz/PulseLoopiOS)
- [Write-up om 56ff-ringene](https://sakshambhutani.xyz/hacking/2_hacking/)
- [Gadgetbridge pull request #5326](https://codeberg.org/Freeyourgadget/Gadgetbridge/pulls/5326)
- [Pipeliner/jring-client](https://github.com/Pipeliner/jring-client), analyse af producentens SDK
- [bleak](https://github.com/hbldh/bleak), Bluetooth LE til Python
