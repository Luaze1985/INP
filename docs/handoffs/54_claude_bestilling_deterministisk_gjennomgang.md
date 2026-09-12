---
title: Bestilling (Claude → AGY) - Deterministisk gjennomgang av struktur-sannhetsserum
handoff_nr: 54
date: 2026-09-12
status: bestilt
from: claude
to: antigravity
branch: codex/partneroppgaver-v1-7
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
svar_paa: 53_claude_oppgave_til_agy_strukturkorrigering.md
tags: [vibs, verified, ipn, sannhetsserum, faktasjekk, determ]
---

# Handoff #54 (Claude → AGY): Bestilling om deterministisk gjennomgang

## Hva som er nytt siden #53

Søknadsteksten er ryddet: `soknadstekst-samlet-kandidat-v1.7-if-only.md`
inneholder nå kun søknadstekst. Status, NFR-kriterieforankring, åpne punkter
og endringslogg er samlet i et eget kontrolldokument (samme sjanger som
`ipn-barekraft-sannhetsserum-2026-06-21.md` og
`k3-forskning-sannhetsserum-v0.6.md`):

`docs/reference/prosjektbeskrivelse/verified-struktur-sannhetsserum-2026-09-12.md`

Dette erstatter `2026-09-12-forbedringsplan-struktur.md`, som er fjernet.

## Bestillingen

Gjør en **deterministisk** gjennomgang av sannhetsserum-dokumentet — samme
disiplin som Lars' `determ`-skill: lokaliser presist med søk/grep før du
leser eller konkluderer, ikke fri resonnering rundt hva som "virker riktig".

Konkret, for **hver rad** i seksjon 1 («NFR-kriterier») og **hvert punkt** i
seksjon 4 («Rød/gul/grønn»):

1. Søk opp den eksakte påstanden i kildefilen den stammer fra
   (`soknadstekst-samlet-kandidat-v1.7-if-only.md`, `budsjett/fordelingsplan.md`
   eller `budsjett/partneroversikt.md`).
2. Rapporter **treff / ikke treff** — ikke en vurdering av om påstanden
   "virker" riktig, men om den faktisk finnes ordrett eller nær-ordrett i
   kilden.
3. For punkter merket 🔴 eller 🟡: bekreft at de faktisk mangler i kilden
   (dvs. at "ikke priset", "kandidat", "uavklart" o.l. faktisk står der) —
   ikke bare at forslaget vårt om hva som mangler høres fornuftig ut.
4. Meld tilbake som en enkel liste: `[radnavn] → TREFF (sitat) / IKKE TREFF /
   AVVIK (forklar)`. Ingen fritekstvurdering utover dette per rad.

## Hvorfor nå, ikke bare tillit til forrige runde

Forrige runde (#51–#53) var LLM-basert faktasjekk med god treffrate, men
ingen har kjørt et rent deterministisk søk mot **dette spesifikke, nylig
omstrukturerte** dokumentet ennå. Feilen som oftest snek seg inn tidligere i
prosjektet var ikke regnefeil, men **påstander som hørtes riktige ut uten et
eksakt kildetreff**. Denne bestillingen lukker akkurat det hullet før
dokumentet brukes videre som beslutningsgrunnlag.

## Ikke gjort av meg

Ingen endring i selve budsjettallene eller partnerlisten. Ingen ny
konklusjon lagt til utover det som allerede sto i søknadsteksten, skissen
eller forbedringsplanen før den ble flyttet.
