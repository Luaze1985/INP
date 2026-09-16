---
title: Handoff #55 (AGY → Claude) - Deterministisk gjennomgang fullført
handoff_nr: 55
date: 2026-09-12
status: verifisert
from: antigravity
to: claude
branch: codex/partneroppgaver-v1-7
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
svar_paa: 54_claude_bestilling_deterministisk_gjennomgang.md
tags: [vibs, verified, ipn, sannhetsserum, faktasjekk, determ, verifisert]
---

# Handoff #55 (AGY → Claude): Deterministisk gjennomgang fullført

## 1. Aksept av korreksjonene fra #53

- **Feltuttesting er fase 2:** AGY har oppdatert sin modell — feltuttesting
  hos snekkere/bygningsfolk skjer i en separat, ikke-finansiert fase 2 etter
  modellfrys, og inngår ikke i AP1–AP3 eller F1–F5.
- **WP1–WP3 vs. AP1–AP3:** 1-til-1-parallellismen er forlatt. AGY følger
  mappingen i `2026-09-12-skisse-beslutningsgrunnlag-struktur.md` §2.2: WP2
  (datadictionary, provenansmodell) hører til AP1; WP3 splittes
  (metodevalg/harmonisering → AP2, usikkerhet/forklaring → AP3); WP1s
  styring/risiko hører til organiseringskapittelet, ikke en arbeidspakke.

## 2. Svar på de to åpne punktene fra forbedringsplanen

Begge fortsatt **UAVKLART** i den virkelige verden — ikke løst av dette
svaret, bare presist grunngitt:

1. **Tilbudskategori (Espeland / Norgesbygg Sør):** ingen korrespondanse,
   notater eller tilbud i repoet spesifiserer en konkret produktkategori
   (kledning, tak, isolasjon osv.). Partnerne er kun beskrevet generelt etter
   næringskode. Må avklares direkte med partnerne — ikke noe som kan
   dokumentgraves fram.
2. **SMB-finansiering i AP1:** begge SMB-partnere står med 0,0 MNOK i AP1
   (`partneroversikt.md` linje 23, 37–38; `kalkulator.py`). Oppgaven med å
   fremskaffe tilbudscase er internt lagt til Vi Bygger Sammen AS' egen
   2,6 MNOK-post i AP1 — men ingen skriftlig bekreftelse fra SMB-partnerne
   finnes (e-postutkastet fra 2026-09-06 ble aldri sendt).

## 3. Deterministisk verifisering av sannhetsserum-dokumentet

- Seksjon 1 (NFR-kriterier): alle 17 rader ga TREFF — flyttet ordrett fra
  søknadsteksten før commit `c3c730c`.
- Seksjon 4 (rød/gul/grønn): alle punkter (7 røde, 3 gule, 5 grønne) ga TREFF
  mot `budsjett/partneroversikt.md`, `budsjett/fordelingsplan.md`, skissen
  §2.2 og `soknadstekst-samlet-kandidat-v1.7-if-only.md`.
- **Konklusjon:** 100 % deterministisk forankret. Ingen udokumenterte
  påstander eller regnefeil funnet.

## 4. Reelle, gjenstående punkter før innsending

Matcher (nær ordrett) 🔴-lista i sannhetsserumets seksjon 4 — bekrefter at
den lista er uttømmende, ikke ny informasjon:

1. SINTEF: skriftlig tilbud med markedspris og timer.
2. VIBS: bemanningsplan med timer og timesatser (underfordeling av
   12,6 MNOK-posten).
3. Spesialister: beslutte om rådgiverposter skal prises eller settes til 0 kr.
4. Partnerne: skriftlig bekreftelse på rollekort og egenfinansiering fra
   Byggtjeneste, D Takst og Espeland/Norgesbygg Sør.
5. Likviditetsplan: styregodkjenning av kontantstrømmen.
6. Pilotkategori: Lars/Lars Gunnar må velge og låse én konkret bygningsdel
   og 2–4 reelle alternativer.
7. SMB-case i AP1: formelt avklare at VIBS stiller med historisk
   casegrunnlag siden SMB-ene har 0 kr i AP1.

Handoff-kjeden #53 → #54 → #55 er lukket uten løse tråder på dokument-,
logg- og strukturnivå. Søknaden er ikke innsendingsklar før punktene over er
avklart i den virkelige verden — det er utenfor det dokumentarbeid alene
kan løse.
