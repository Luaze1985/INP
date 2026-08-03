---
title: Handoff (Codex) - Perplexity-inntak, kunnskapsfiler og kildepensjonering
date: 2026-08-03
status: ready-for-human
from: codex
to: codex
tags: [vibs, verified, ipn, perplexity, sources, competitors, retirement]
neste_ledige_handoff: 42
---

# Handoff (Codex): ta inn Perplexity-funn og forbered varig opprydding

## Mål for neste sesjon

Ta imot Lars' Perplexity-resultater som urørt råinntak og bruke dem til å
forberede:

1. en kunnskapsfil for kilder;
2. en kunnskapsfil for konkurrenter;
3. et livsløps- og sperresystem som hindrer pensjonerte kilder og gamle aliaser
   i å dukke opp igjen;
4. et tørrkjøringskart over hva som senere kan fjernes, arkiveres eller slettes.

Ikke gjennomfør permanent sletting eller statusendring i denne sesjonen.

## Les først

- `AGENTS.md`
- `CONTEXT.md`
- `INDEX.yml`
- `.scratch/kilde-og-konkurrentkonsolidering-2026-08/MAP.md`
- `.scratch/kilde-og-konkurrentkonsolidering-2026-08/issues/01-registrer-perplexity-funn.md`
- `.scratch/kilde-og-konkurrentkonsolidering-2026-08/issues/02-fastsett-livslop-og-sperrepost.md`
- `.scratch/sintef-forskningsrapport-2026/research/perplexity-sjekkliste-k3-og-soa-v0.5.md`
- `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`
- `docs/reference/ipn-kildebibliotek.md`
- `docs/reference/vibs-verified-kildedom-2026-06-27.md`
- `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md`
- `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`

## Status ved overlevering

- Wayfinder-kartet og åtte beslutnings-/undersøkelsestickets er opprettet.
- Perplexity-sjekklisten har 28 kontrollpakker og skiller eksterne fakta,
  fraværspåstander og prosjektets egne hypoteser.
- Selve Perplexity-resultatene er ikke mottatt i repoet eller funnet i
  `Downloads` ved siste kontroll.
- Ingen ny Perplexity- eller Sonar-kjøring skal startes automatisk.
- Ingen låste eller kanoniske søknads-/kildedokumenter er endret av Codex i
  denne fasen.
- Arbeidskopien inneholder omfattende AGY-artefakter under `.agents/`; behold
  dem urørt og skill dem fra dette arbeidet.

## Første handling når Lars leverer funnene

1. Identifiser alle leverte filer eller innlimte tekstblokker.
2. Kopier dem urørt til en ny, datert inntaksmappe under `.scratch/`.
3. Registrer opprinnelig filnavn, størrelse, SHA-256 og mottakstid i et manifest.
4. Skill Perplexity-svar, direkte originalkilder og Lars' egne konklusjoner.
5. Ikke oppgrader status fordi Perplexity sier at noe er verifisert.
6. Oppdater og lukk bare ticketen **Registrer Perplexity-funn som råinntak**.
7. Legg én kort beslutningspeker i Wayfinder-kartet. Ikke løs flere tickets i
   samme wayfinding-sesjon.

## Styringsregel for permanent pensjonering

«Ikke funnet» kan gi permanent utestengelse fra aktive flater, men skal ikke
skrives som «bevist ikke-eksisterende».

En permanent pensjonert kilde må beholde en minimal sperrepost med:

- kanonisk nøkkel og gamle aliaser;
- normalisert tittel og identifikatorer som DOI/URL hvis de finnes;
- beslutningsstatus og begrunnelse;
- beslutningsdato og godkjenner;
- erstatningskilde eller erstatningsformulering;
- gjenåpningsregel: `never`, `manual-only` eller `original-required`.

Aktiv tekst og aktive kunnskapsfiler kan deretter renses. Sperreposten beholdes
for å hindre gjenimport og bevare audit trail.

## Kjente kontrollpunkter

- `[Wiik2025]` og `[SA2018]` er parkert, men må vurderes for permanent
  pensjonering eller `original-required`.
- `[Multiconsult2023DiBK]` finnes i K3-notatet, men ikke i kildebiblioteket;
  identitet og mulig alias/duplikat må avstemmes.
- `[Bjørheim2026]` er feilaktig brukt som samlekilde for konkurser, BDO-margin,
  UNION-kostnadssammenligning og ombruksrammer. Disse må splittes.
- Gamle nøkler som `[An2021]` og `[Billio_SAFE261]` må sperres som erstattede
  aliaser dersom de fortsatt finnes i aktive flater.
- Konkurrentfunn må skille positivt dokumenterte funksjoner,
  leverandørpåstander og `ikke dokumentert i gjennomgangen`.

## Ikke-mål

- Ikke slett kilder eller råfiler før tørrkjøringskart og Lars-godkjenning.
- Ikke endre `v0.4`, `v0.5` eller kanoniske K/V-mål.
- Ikke omskriv historiske dokumenter som om tidligere beslutninger ikke fantes.
- Ikke lage en full SQLite-løsning før mellomsteg og migrering er besluttet.
- Ikke sende materiale eksternt.

## Foreslåtte skills

- `wayfinder` — arbeid én åpen ticket om gangen og behold beslutningene i kartet.
- `research` — kontroller originalkilder når råinntaket viser konkrete
  kunnskapshull; bruk primærkilder.
- `to-tickets` — først etter at livsløpsmodellen og tørrkjøringskartet er
  besluttet og skal gjøres om til implementeringsoppgaver.
- `code-review` — kontroller senere endringer mot styringsreglene og godkjent
  pensjoneringskart.

## Startprompt for neste Codex-sesjon

```text
Les docs/handoffs/41_codex_perplexity-inntak_og_kildepensjonering_handoff.md.

Lars har levert Perplexity-resultatene. Start med Wayfinder-ticketen
«Registrer Perplexity-funn som råinntak». Bevar råmaterialet urørt, lag manifest
og kontrollsummer, og skill Perplexity-svar fra åpnet original og Lars'
konklusjon. Ikke endre kildestatus, søknadstekst eller aktive kildefiler, og
ikke slett noe. Lukk bare denne ene ticketen når inntaket er etterprøvbart.
```
