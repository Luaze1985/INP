---
title: Handoff (Codex) - finskriving og nytt kildeinntak
date: 2026-08-03
status: ready-for-human
from: codex
to: codex
tags: [vibs, verified, ipn, finskriving, kilder, konkurrenter, sintef]
neste_ledige_handoff: 44
---

# Handoff: finskriv dokumentpakken og bevar kontrollert inntak

## Mål for neste sesjon

Lars skal finskrive de lettleste dokumentene til kollegaer. Neste agent skal
hjelpe med språk, struktur og konsistens uten å endre faglig status, gjøre
usikre funn sikrere eller sende materiale eksternt.

Dersom Lars senere leverer 10–15 nye kilder og flere konkurrentfunn, skal de
tas inn som en ny, separat batch. De skal ikke flettes direkte inn i
søknaden, nettsiden eller dagens kollegapakke.

## Les først

- `AGENTS.md`
- `CONTEXT.md`
- `docs/sintef/README.md`
- `docs/sintef/KONTROLLRAPPORT.md`
- `docs/sintef/kollegapakke/`
- `docs/agents/intake-outtake.md`
- `governance/README.md`
- `governance/source-blocklist.json`
- `docs/handoffs/41_codex_perplexity-inntak_og_kildepensjonering_handoff.md`
- `docs/handoffs/42_codex_agentisk_intake_outtake_og_sintef-forberedelse_handoff.md`

## Status nå

- Kollegapakken har fire lettleste tekster og er innholdsmessig klar for intern
  gjennomgang.
- `docs/sintef/` er sentral inngang til kollegatekster, interne endringskart og
  den lagrede SINTEF-pakken.
- SINTEF-pakken er et kontrollert utkast merket `IKKE SENDT` og `IKKE
  GODKJENT`. Den mangler mottaker, vedlegg/originaler, ansvar, svarfrist og
  sendemanifest.
- Søknad og IPN-nettside er ikke endret gjennom dokumentarbeidet.
- Source Guard ble innført i commit `89d6536` og håndhever 11 sperreposter.
  Validator, register og pre-commit-port er testet med 17 beståtte tester.
- Full aktiv kontroll gir fortsatt `BLOCK` på 62 historiske treff. Nye eller
  endrede treff stoppes; gammel gjeld skal bare ryddes gjennom et senere
  godkjent endringskart.
- Arbeidsgrenen er `change/tekstpresisering-v0.5`, syv commits foran registrert
  upstream ved denne handoffen.
- Arbeidstreet er ikke rent. `docs/sintef/`, handoff 37–42,
  `docs/agents/intake-outtake.md` og enkelte review-/kildekart er fortsatt
  usporet. Flere `.agents`-filer er endret eller usporet. Ikke bland dette inn
  i en finskrivingsoppgave uten uttrykkelig scope.

## Dokumenter som kan finskrives

- `docs/sintef/kollegapakke/01-kort-oversikt.md`
- `docs/sintef/kollegapakke/02-detaljert-arbeidsnotat.md`
- `docs/sintef/kollegapakke/03-behold-ta-ut-avklar.md`
- `docs/sintef/kollegapakke/04-anbefalt-arbeidsrekkefolge.md`

Bevar lettlest norsk, Unicode, anbefalinger og prosjektets etablerte
begrepsbruk. Dokumentene er forklaringstekster, ikke referanselister eller ny
kildedom.

## Ufravikelige skrivegrenser

- Bevar skillet mellom `Behold`, `Ta ut` og `Avklar`.
- Merk usikre kilder som tas ut med usikkerheten synlig; ikke skriv at de er
  bevist ikke-eksisterende.
- Bevar kildeidentitet og aliaser når noe tas ut, slik at det ikke importeres
  på nytt som en «ny» kilde.
- Perplexity- og agentfunn er kontrollgrunnlag, ikke selvstendig belegg.
- Manglende dokumentasjon på en konkurrentfunksjon er ikke bevis på at
  funksjonen mangler.
- Prosjektmål og testterskler er ikke ekstern empiri.
- Bare Lars kan godkjenne kildestatus, gjenåpning, tekstendring og ekstern
  sending.
- Ikke antyd at SINTEF allerede har kontrollert eller godkjent prosjektet.

## Hvis nye kilder og konkurrenter kommer

1. Opprett en ny datert intake-batch og bevar råleveransen urørt.
2. Registrer filnavn, opphav, tidspunkt, søkestreng/lenker og SHA-256.
3. Kjør `python tools/source_guard.py scan --path <mottatt-fil>` før routing.
4. Avstem nøkler, aliaser, titler, DOI-er og URL-er mot eksisterende kilder og
   sperreposter.
5. Koble hver kilde til den konkrete påstanden den kan eller ikke kan støtte.
6. Registrer konkurrentfunksjoner med dokumentasjonsgrunnlag, produktversjon
   og kontrolldato. Bruk `dokumentert`, `delvis` eller `ikke dokumentert i
   gjennomgangen`.
7. Lag et nytt konsekvenskart for kollegapakke, søknad og nettside. Ikke
   overskriv versjonen datert 2026-08-03.
8. Legg nye problemkilder i et forslag til sperrepost. Bare Lars kan godkjenne
   at registeret endres.
9. Stopp ved Lars' godkjenningsport før aktiv tekst eller kildestatus endres.

## Før repoet deles via Git

1. Oppdater `CONTEXT.md` til dagens Perplexity-, Source Guard- og
   konsolideringsstatus.
2. Avgrens hvilke `.agents`-artefakter som skal beholdes som proveniens,
   arkiveres eller holdes utenfor leveransen.
3. Kontroller og commit kollega-/SINTEF-dokumentene sammen med nødvendige
   innganger i `README.md` og `INDEX.yml`.
4. Kjør `git diff --check`, dokumentkontroll og Source Guard.
5. Skill en intern kollegaleveranse fra en eventuell senere ekstern
   SINTEF-leveranse.

## Ikke-mål

- Ikke endre låst `v0.4`, aktiv `v0.5` eller kanoniske K/V-filer under
  finskrivingen.
- Ikke endre nettsiden.
- Ikke oppgradere, pensjonere eller gjenåpne kilder uten Lars' beslutning.
- Ikke kjør nye nettsøk uten en uttrykkelig research-bestilling.
- Ikke send noe til SINTEF eller andre samarbeidspartnere.
- Ikke masseopprydd `.agents` som del av dokumentfinskrivingen.

## Foreslåtte skills

- `ai-sprakvask-no` for en avgrenset norsk finskriving uten faglig
  statusendring.
- `kunnskapsfil-pipeline` når nye kilder og konkurrenter skal konsolideres.
- `wayfinder` dersom et større nytt inntak skal deles i kontrollerte batcher.
- `code-review` for uavhengig kontroll av faktisk diff før commit.
- `handoff` etter avsluttet finskrivings- eller intake-runde.
- `sonar-search` bare dersom Lars uttrykkelig bestiller nye eksterne søk.

## Startprompt for neste Codex-sesjon

> Les AGENTS.md, CONTEXT.md og handoff 43. Lars skal finskrive de fire tekstene
> i docs/sintef/kollegapakke/. Hjelp med lettlest norsk, struktur og
> konsistens, men behold alle usikkerheter, beslutningsgrenser og statusporter.
> Ikke endre søknad, nettside, kildestatus eller SINTEF-pakken uten eksplisitt
> beskjed. Hvis nye kilder eller konkurrenter er vedlagt, registrer dem først
> som en separat rå intake-batch og kjør Source Guard før avstemming.
