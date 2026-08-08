---
title: Handoff (AGY) - klargjør kilde- og kontekstpakker før Perplexity
date: 2026-08-02
status: ready-for-human
from: codex
to: antigravity (AGY)
tags: [vibs, verified, ipn, sources, context, subagents, read-only]
neste_ledige_handoff: 41
---

# Handoff (AGY): klargjør kilde- og kontekstpakker før Perplexity

## Mål

Bruk AGY-subagenter til å forberede en presis og prioritert søkekø for senere
manuell kontroll i Perplexity. Denne fasen er kun lokal kontekstinnhenting og
planlegging. Ikke gjennomfør nettsøk nå.

## Bindende regler

- Arbeid helt read-only.
- Ikke bruk Perplexity, Sonar eller andre nettsøk i denne fasen.
- Ikke opprett eller endre filer, heller ikke under `.scratch`.
- Ikke endre kildestatus eller søknadstekst.
- Ikke avgjør K-01–K-06.
- Returner alle resultater direkte i AGY-svaret.
- En eksisterende agentoppsummering er kontekst, ikke belegg.

## Les først

- `AGENTS.md`
- `CONTEXT.md`
- `INDEX.yml`
- `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`
- `docs/reference/ipn-kildebibliotek.md`
- `docs/reference/vibs-verified-kildedom-2026-06-27.md`
- `docs/reference/state-of-the-art-verified-ipn.md`
- `research/evidence_matrix.md`
- `.scratch/research-intake/gen-2026-07-29-01/README.md`
- `.scratch/research-intake/gen-2026-07-29-01/work/pastandsregister.md`

## Subagenter

Kjør seks tydelig adskilte lokale analysepass. Passene kan kjøres parallelt.

### 1. Norske nøkkelkilder og tall

Forbered kontrollpakke for `[SA2018]`, `[KD2024]`, DiBK/Multiconsult,
`[EBA_NO2023]`, `[Wiik2025]`, 70 prosent A1–A3 og faktor 1,25.

### 2. Bank- og finansbelegg

Forbered kontrollpakke for `[An2020]`, `[Billio2022]`, `[Kaza2014]`,
`[EBA_EU2023]` og avgrensningen av F5. Skill næringsbygg, boliglån,
energieffektivitet, holdbarhet og teknisk kvalitet.

### 3. EU-regelverk og standarder

Forbered kontrollpakke for Omnibus I, CPR, ESPR/DPP, EN 15978 og andre
standardpåstander der publiseringsfaktum og detaljinnhold må skilles.

### 4. SMB og tilbudsfasen

Forbered kontrollpakke for SMB-definisjon, andel av næringen og dokumentasjon
av små entreprenørers bruk av LCA, EPD og digitale beslutningsverktøy i
tilbudsfasen.

### 5. Verktøybildet og FoU-gapet

Forbered en felles funksjonsmatrise og kontrollspørsmål for EC3, One Click LCA,
ORIS, SmartKalk, Reduzer, Madaster, Concular, NOBB/Cobuilder og relevante
moteksempler. Ikke konkluder med at et gap er bekreftet.

### 6. Utfordrer og ontologikontroll

Kontroller at pakkene bruker begrepene i ord- og kildekartet, at historiske
formuleringer ikke gjøres gjeldende igjen, og at hver mulig fraværspåstand har
et planlagt moteksempelsøk.

## Leveranseformat i AGY-svaret

Returner én samlet tabell med én rad per kontrollpunkt:

| Felt | Innhold |
| --- | --- |
| Pakke-ID | `NO-*`, `FIN-*`, `EU-*`, `SMB-*` eller `TOOL-*` |
| Påstands-ID | Påstands-ID fra registeret, hvis tilgjengelig |
| Nåværende formulering | Den konkrete påstanden som skal kontrolleres |
| Kildenøkkel | Eksisterende nøkkel eller `MANGLER` |
| Hvor påstanden brukes | Dokument og seksjon, ikke lange tekstutdrag |
| Hva som mangler | Identitet, original, side, omfang, metode eller kontekst |
| Ønsket originalkilde | Forfatter/organisasjon, tittel, år og mulig utgiver |
| Foreslått Perplexity-spørsmål | Presist søk som senere kan kjøres manuelt |
| Foretrukket kildedomene | Offisiell utgiver, DOI, tidsskrift eller myndighet |
| Motkontroll | Spørsmål som kan avkrefte eller avgrense påstanden |
| Godkjenningskriterium | Hva som må finnes i originalen for å støtte påstanden |
| Prioritet | Kritisk, høy, middels eller lav |

Avslutt med:

1. duplikater som kan slås sammen før søk;
2. kontrollpunkter som krever Lars-kontekst, ikke nettsøk;
3. kontrollpunkter som krever SINTEF/fulltekst;
4. sterkeste mulige motargument mot VERIFIEDs avgrensede FoU-gap.

## Startprompt til Antigravity

```text
Les docs/handoffs/40_agy_klargjor-kilde-og-kontekstpakker_read-only_handoff.md og følg den ordrett.

Bruk separate subagenter/pass for norske kilder, finans, EU/standarder, SMB,
verktøybildet og utfordrerkontroll. Arbeid bare mot lokale prosjektfiler.
Ikke bruk Perplexity, Sonar eller andre nettsøk ennå. Ikke endre filer eller
kildestatus. Returner én deduplisert og prioritert søkekø direkte i svaret.
```
