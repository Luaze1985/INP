---
title: Handoff (Claude) - v0.7-grunnlagsarbeid og partnerprosess
date: 2026-08-05
status: blocked-until-v0.6-pass-and-lars-go
from: codex
to: claude
branch: change/tekstpresisering-v0.5
tags: [vibs, verified, ipn, v0.7, method, sources, consortium]
neste_ledige_handoff: 46
---

# Handoff: orkestrer grunnlagsarbeidet fram mot v0.7

## Kort beskjed

Denne handoffen starter først når v0.6-overflatepasset er godkjent og Lars
åpner neste fase. Orkestrer beslutninger om målgruppe, datamodell,
forskningsmetode, kilder, virkninger, partnerroller, arbeidspakker og budsjett.
Opprett v0.7 først når styrende valg og eiere er tydelige.

## Rollefordeling

- **Claude:** orkestrerer spørsmål, alternativer, handoffs og seksjonsvise
  tekstutkast etter beslutning.
- **Lars:** beslutter scope, partnerkontakt, kildestatus og ekstern sending.
- **Codex:** forvalter repo, versjoner, påstand–kilde-matrise, diff og
  kontrollporter.
- **Forskningspartner:** eier forskningsdesign, testopplegg og metodefaglig
  terminologi.
- **Erfaren evaluator/rådgiver:** leser prosjektet som søknad og peker på
  mangler, uklarhet og overstrekk.

## Les først

1. `docs/handoffs/44_claude_v0.6-overflatepass_og_partnerkandidat_handoff.md`
2. `docs/reference/prosjektbeskrivelse/reviews/2026-08-05-tilbakemeldingsregister-v0.6.md`
3. `docs/reference/prosjektbeskrivelse/reviews/2026-08-05-v0.7-grunnlagsarbeid-og-partnerprosess.md`
4. resultatrapporten fra v0.6-overflatepasset når den finnes;
5. godkjent v0.6 og K3-sannhetsserum v0.6;
6. `AGENTS.md`, `CONTEXT.md`, `INDEX.yml` og prosjektbeskrivelsens `README.md`;
7. kildepass, Source Guard-regler og relevante partner-/gjennomføringsfiler.

## Første fase

1. Lag et kort partnernotat med prosjektkjerne, status, åpne spørsmål og ønsket
   bidrag.
2. Forbered forhåndssparring med én erfaren evaluator/rådgiver.
3. Forbered en separat metodegjennomgang med forskningsfaglig kontakt.
4. Forbered et 30–40 minutters oppstartsmøte for status og arbeidsdeling.
5. Be Lars godkjenne mottakere, dokumenter og spørsmål før noe sendes.

## Arbeidsporter

Følg port A–F i grunnlagsdokumentet. Løs én beslutning om gangen og registrer:

- beslutningseier;
- alternativer og anbefaling;
- kilde- eller fagbehov;
- konsekvens for K1–K4, V1–V3, arbeidspakker og budsjett;
- hva som forblir åpent.

## Viktige åpne beslutninger

1. Offisiell definisjon og størrelse på SMB-målgruppen.
2. Om leverandørsoliditet og konkursrisiko er kjerne, eget spor eller ute.
3. Forskningsdesign, testtyper, validering og følsomhetsanalyse.
4. Om prosjektet skal ha et tydelig sekundært bærekraftsmål.
5. V3-overskrift og målbare økonomiske mekanismer.
6. Partnernavn, roller og faktisk deltakelse.
7. Arbeidspakker, ansvar, milepæler og budsjett.
8. Hvilke kilder som kan gjenåpnes etter originalkontroll og Lars-beslutning.

## Ikke-mål

- Ikke opprett v0.7 før v0.6-passet og Lars-porten er lukket.
- Ikke bruk partnerinteresse som bekreftet forpliktelse.
- Ikke la Claude eller andre agenter avgjøre kildestatus.
- Ikke fastsett metode uten forskningsfaglig eier.
- Ikke sende materiale, møteinnkalling eller e-post uten Lars' godkjenning.
- Ikke overskriv v0.6 når v0.7 senere opprettes.

## Akseptansekriterier

1. Alle F-rader med `KREVER BESLUTNING`, `KREVER KILDE`, `KREVER FAGPARTNER`
   eller `PARKERT TIL v0.7` er routet til eier og leveranse.
2. Partnerprosessen har kort formål, mottaker, ønsket bidrag og oppfølging.
3. Forskningsmetode og testdesign har faglig eier før søknadsprosa skrives.
4. Påstand–kilde-matrisen skiller kandidat, åpnet original, tillatt bevisrolle
   og Lars-godkjenning.
5. V0.7 opprettes som ny fil og har tydelig endringslogg mot v0.6.
6. Kilde-, språk-, kriterie- og innflettingskontroll er planlagt før ekstern
   bruk.

## Foreslåtte skills

- `grill-with-docs` for én styrende beslutning om gangen.
- `wayfinder` for port A–F og arbeid over flere sesjoner.
- `research` for avgrensede originalkilder etter godkjent bestilling.
- `to-tickets` når portene er besluttet og skal fordeles.
- `ai-sprakvask-no` etter faglig godkjent seksjonsutkast.
- `handoff` mellom Claude, Codex og eventuell annen utførende agent.

## Startprompt til Claude

```text
Les docs/handoffs/45_claude_v0.7-grunnlagsarbeid_og_partnerprosess_handoff.md,
tilbakemeldingsregisteret og grunnlagsdokumentet. Start bare dersom Lars har
godkjent v0.6-overflatepasset og eksplisitt åpnet v0.7-fasen. Forbered først et
kort partnernotat, spørsmål til evaluator/rådgiver og forskningspartner, og en
30–40 minutters oppstartsagenda. Løs deretter port A–F én beslutning om gangen.
Ikke opprett v0.7, endre kildestatus eller sende noe før riktig Lars-port er
lukket.
```
