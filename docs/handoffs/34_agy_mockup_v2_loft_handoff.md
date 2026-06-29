---
title: Handoff (AGY) - Visuelt v2-løft av VERIFIED-mockup
date: 2026-06-28
status: ready
from: claude
to: antigravity (AGY)
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
builds-on: docs/handoffs/31_agy_mockup_innholdstro_handoff.md
tags: [vibs, verified, ipn, site, mockup, v2, motion, dataviz, agy]
---

# Handoff (AGY): Løft mockupen fra v1 til v2

## Kort beskjed

V1-mockupen (`site/mockup/`) er en sterk v1, men ligger ett nivå under forbildene. Løft den til v2 etter
de **fire låste valgene** og den strenge kritikken under. Behold kjernebriefen (gull/sort, myke flater,
VERIFIED-foregrunnet, vet/vet-ikke). **Rør ikke** `site/index.html`/`styles.css`/`scrollspy.js` (Lars sin lærings-fil).

## Bindende spec
- `site/benchmark-forbilder.md` — **forbildene** (scrollytelling-håndverk, troverdighet, klarspråk) + lenker.
- `site/design-brief.md` → «v2-løft»-seksjonen — de fire prinsippene.
- `site/innhold-kanban.md` — narrativ + 🟢-fakta.

## De fire løftene (gjør disse)

1. **Bevegelse (middels — ikke effektjag).**
   - Subtil reveal: faktabokser/innhold fader/stiger mykt inn ved scroll (IntersectionObserver).
   - **Én pinned «vet→vet-ikke»-overgang:** bruk scrollen til å sette kjernekontrasten — f.eks. «Hva vi vet» pinnes og glir/transformeres over i «Hva vi ikke vet ennå».
   - **`prefers-reduced-motion: reduce` → all bevegelse av.** Hold mobil lett.
2. **Fakta-viz (1–2 grep).**
   - Visualiser signaturen **vet / vet-ikke** (f.eks. en enkel akse/kontrast, ikke et travelt diagram).
   - Ett nøkkeltall som visuelt grep (~32 %). Elegant, rolig — ikke infografikk-støy.
3. **Av-«dashboard» faktakortene.**
   - Dagens `facts-grid` (`mockup/index.html:121`) leser som SaaS-dashboard. Gjør det **redaksjonelt og mykt**: mer luft, mykere flater, mindre «kort-i-rutenett».
4. **Bilder: kuratere + duotone.**
   - Velg **ikke-klisjé** byggebransje-bilder (unngå «arbeidere som går»). Gi **alle** seksjoner lik dempet **duotone** (navy/gull-toning) så de henger sammen og forblir myke.
   - Oppdater `bakgrunnsbilder-forslag.md` ved bytte (kilde + lisens).

Pluss: **varier rytmen** — ikke 7 identiske fullskjerm-seksjoner (full-bleed / split / pinned).

## Streng kritikk som skal være lukket i v2
- Statiske seksjoner → nå med subtil reveal + én pinned overgang.
- `facts-grid` dashboard-følelse → redaksjonelt/mykt.
- Monoton rytme → variert.
- Stock-klisjé/ujevn bildebehandling → kuratert + konsistent duotone.

## Ikke-mål
- Ikke rør `site/index.html`/`styles.css`/`scrollspy.js` eller `docs/reference/`.
- Ikke tung/«kreativ» animasjon som slår ut a11y/mobil-ytelse.
- Ikke endre teksten (Codex eier tekst via #33) — jobb med struktur/visuell form.

## Akseptansekriterier
1. Subtil reveal finnes; **minst én pinned vet→vet-ikke-overgang**; `prefers-reduced-motion` slår alt av.
2. 1–2 enkle fakta-viz til stede (vet/vet-ikke + ett nøkkeltall), elegant — ikke støy.
3. Faktakortene leser redaksjonelt/mykt, ikke dashboard.
4. Bilder er ikke-klisjé + konsistent duotone; `bakgrunnsbilder-forslag.md` oppdatert (kilde+lisens).
5. Mobil + desktop screenshots i `site/mockup/screens/`. Kjernebrief (gull/sort, VERIFIED-foregrunnet) intakt.

## Startprompt (lim inn til AGY i VS Code)

```text
Jobb i repoet C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified.
Les docs/handoffs/34_agy_mockup_v2_loft_handoff.md, site/benchmark-forbilder.md,
site/design-brief.md (v2-løft-seksjonen) og site/innhold-kanban.md.

Løft mockupen i site/mockup/ fra v1 til v2 — IKKE rør site/index.html, styles.css
eller scrollspy.js, og ikke endre teksten (Codex eier tekst).

Gjør fire løft: (1) middels bevegelse — subtil reveal (fade/stigning) + ÉN pinned
«vet→vet-ikke»-overgang via scroll; prefers-reduced-motion slår ALT av; hold mobil
lett. (2) 1–2 enkle, elegante fakta-viz — visualiser «vet/vet-ikke»-kontrasten + ett
nøkkeltall (~32 %), rolig, ikke infografikk-støy. (3) gjør facts-grid (index.html:121)
redaksjonelt og mykt, ikke SaaS-dashboard. (4) bytt til ikke-klisjé byggebransje-bilder
med konsistent dempet duotone (navy/gull); oppdater bakgrunnsbilder-forslag.md med
kilde+lisens. Varier rytmen (full-bleed/split/pinned), ikke 7 like fullskjerm.

Behold kjernebriefen: gull #ffc600 / navy #11111f / hvit, Comfortaa, VERIFIED
foregrunnet, VIBS/SINTEF som partnere. Lever oppdatert mockup + nye screenshots
(mobil+desktop) i site/mockup/screens/.
```
