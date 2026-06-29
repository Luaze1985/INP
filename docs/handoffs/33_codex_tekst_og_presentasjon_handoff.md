---
title: Handoff (Codex) - Tekst og presentasjon av VERIFIED-prosjektet
date: 2026-06-28
status: ready
from: claude
to: codex
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
tags: [vibs, verified, ipn, site, tekst, copy, presentasjon, codex]
---

# Handoff (Codex): Tekst + presentasjon av prosjektet

## Kort beskjed

Lås den **endelige teksten** for VERIFIED-statussiden, og skjerp **hvordan prosjektet presenteres** —
kildeverifisert, i riktig stemme, troverdig for en Forskningsrådet-leser. Du leverer ett **tekstmanus**
(`site/tekstmanus.md`); du **endrer ikke** mockupen eller koden. Dekker tekst-delen; UI/a11y/kode er separat (#32).

## Rollefordeling (ærlighetsregel)

- **Codex (deg):** verifiser + skriv endelig tekst + skjerp presentasjonen. Lever tekstmanus.
- **Claude:** skrev handoffen, speccen og issuene. Styrer deg ikke direkte.
- **Lars Erik:** beslutter (bl.a. om søknadsbeløp skal vises, grensetilfeller).

## Inndata (les)

- **Issues:** `.scratch/verified-statusside/issues/01-innholdsverifisering.md`, `02-seksjonscopy.md`, `03-mikrocopy-metadata.md` — oppgavene du utfører.
- **Spec:** `site/design-brief.md` (stemme/tone/innholdsprinsipp), `site/innhold-kanban.md` (narrativ + 🟢/🟡/🔴-fakta).
- **Kildegrunnlag:** `docs/reference/vibs-verified-kildedom-2026-06-27.md`, `ipn-hovedokument.md`, `state-of-the-art-verified-ipn.md`, `ipn-samledokument.md`.
- **Nåværende tekst:** `site/mockup/index.html` (les for kontekst — **ikke endre**).
- `AGENTS.md` — kilde- og sannhetsregler.

## Oppgaven (issue 01 → 02 → 03)

1. **Verifiser & rett (01).** Sjekk hver påstand i mockup-teksten mot kildegrunnlaget. Avklar de tre flaggene:
   `index.html:217` (sanntidsdata/sensordokumentasjon — i scope eller fjern?), `:233` («SINTEF Community» — riktig institutt?), `:62-63` («Søkertall» — vises beløpet? riktig begrep?). Fjern/omskriv alt som ikke er dekket.
2. **Endelig seksjonscopy (02).** Skriv alle 7 seksjoner ferdig i **«vi»-stemme**, korte setninger, jordnært, ingen sjargong. Hero eksakt (uendret). Vet/vet-ikke-kontrasten skal stå skarpt. Reguleringer/bærekraft i Utfordringen.
3. **Mikrocopy + metadata (03).** Sidebar-labels (rett «Søkertall»), partnerstripe, scroll-prompt, CTA, `<title>`/description, alt-strategi.
4. **Presentasjon av prosjektet.** Vurder helheten: leser det troverdig og tydelig for Forskningsrådet, *uten* å nevne kriteriene? Foreslå forbedringer i rekkefølge/flyt/budskap der det styrker presentasjonen.

## Kilde- og presentasjonsregler (ufravikelige)

- Kun **🟢-fakta** vises som påstand (jf. `innhold-kanban.md`). **🔴** (Wiik 2025, konfliktkostnad) er ute.
  **🟡** (f.eks. byggefeil) fraseres som «forskning indikerer», aldri som VERIFIED sin påstand.
- Hver påstand med tall får en **stille kildehenvisning**.
- **Ingen oppdiktede tall/scope.** Egen kunnskap teller ikke som belegg.
- **NFR-kriteriene (Kvalitet/Effekter/Gjennomføring) nevnes aldri eksplisitt** — de skal merkes implisitt.

## Språk: hard strip til dagligspråk + av-KI (v2 — låst)

Forbilder/forbudsliste: `site/benchmark-forbilder.md`. Dette er en **hard** strip for «enkle folk»:

- **Fjern/forklar fagsjargong i klartekst:** EPD, NOBB, LCA, MCDA, DPP, «verifiseringsmodell» osv. Hvis et begrep må stå, gi én enkel forklarende bisetning.
- **Av-KI-fisering:** korte setninger; ingen svulstige ord/superlativer; ingen amerikansk tone; ikke repeterte formuleringer (særlig gjentatt «bro fra data til beslutning»).
- **Forbudte/uønskede formuleringer fra v1** (rett disse): «tas i blinde» (`mockup/index.html:112`), «ødeleggende for økonomien» (:138), «tydelig indikasjon på sårbarheten» (:145), tette regelsetninger (:117).
- Skriv som en **dyktig fagperson som forklarer rett ut** — jordnært, konkret, trygt.

## Det du skal levere

- **`site/tekstmanus.md`** — endelig tekst for hvert element på siden:
  - Per seksjon (1–7): badge/eyebrow, overskrift, brødtekst, evt. faktakort (tall + stille kilde).
  - Mikrocopy: sidebar-labels + verdier, partnerstripe, scroll-prompt, CTA.
  - Metadata: `<title>`, meta-description, alt-tekster (eller «dekorativt — ingen alt»).
  - En kort **endringslogg** av hva du rettet vs. mockupen, og **åpne spørsmål til Lars** (f.eks. søknadsbeløp).

## Ikke-mål

- Ikke endre `site/mockup/`, `site/index.html`, `styles.css`, `scrollspy.js` eller `docs/reference/`.
- Ikke design/CSS/kode — kun tekst og presentasjon.
- Ikke dikt opp fakta; ikke bruk 🔴/🟡 som påstand.

## Akseptansekriterier

1. Hvert tekstelement på siden er dekket i `site/tekstmanus.md`, i «vi»-stemmen.
2. Hver påstand er sporet til 🟢-kilde (eller fraset som «forskning indikerer»); 🔴 er ute; de 3 flaggene avklart.
3. NFR-kriteriene nevnes ikke eksplisitt noe sted.
4. Endringslogg + åpne spørsmål til Lars er med.

## Startprompt (lim inn til Codex i VS Code)

```text
Jobb i repoet C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified.
Les docs/handoffs/33_codex_tekst_og_presentasjon_handoff.md,
.scratch/verified-statusside/issues/01-,02-,03-, site/design-brief.md og
site/innhold-kanban.md.

Oppgave: lås endelig TEKST for VERIFIED-statussiden + skjerp presentasjonen av
prosjektet. Du leverer ETT tekstmanus til site/tekstmanus.md — du endrer IKKE
site/mockup/, index.html, styles.css eller docs/reference/.

Gjør: (1) verifiser hver påstand i site/mockup/index.html mot docs/reference/
(kildedom, ipn-hovedokument, state-of-the-art) og rett — avklar spesielt
index.html:217 (sanntidsdata/sensordokumentasjon), :233 (SINTEF Community), :62-63
(Søkertall). (2) skriv alle 7 seksjoner ferdig i «vi»-stemme, korte setninger,
jordnært, vet/vet-ikke-kontrast tydelig, reguleringer/bærekraft i Utfordringen.
STRIP hardt: forklar/fjern fagsjargong (EPD/NOBB/LCA/MCDA/DPP) i klartekst, av-KI
(ingen svulstige ord/superlativer, ingen repetert «bro»; rett «tas i blinde»,
«ødeleggende»). Se site/benchmark-forbilder.md for forbudsliste.
(3) mikrocopy + metadata (rett «Søkertall», title/description, alt-strategi).
(4) foreslå forbedringer i flyt/budskap for en Forskningsrådet-leser.

Regler: kun 🟢-fakta som påstand (innhold-kanban.md), 🔴 ute, 🟡 som «forskning
indikerer» med stille kilde; ingen oppdiktede tall; NFR-kriteriene nevnes ALDRI
eksplisitt. Lever site/tekstmanus.md med per-seksjon tekst, mikrocopy, metadata,
endringslogg og åpne spørsmål til Lars.
```
