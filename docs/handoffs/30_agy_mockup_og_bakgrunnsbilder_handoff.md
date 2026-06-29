---
title: Handoff (AGY) - Mockup av VERIFIED-statusside + forslag til bakgrunnsbilder
date: 2026-06-28
status: ready
from: claude
to: antigravity (AGY)
branch: antigravity/site-mockup (foreslått; repo har ingen remote ennå)
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
tags: [vibs, verified, ipn, site, mockup, design, bilder, agy]
---

# Handoff (AGY): Lag mockup av statussiden + foreslå bakgrunnsbilder

## Kort beskjed

Lag en **høy-fidelity mockup** av scrollytelling-statussiden for VERIFIED, og **foreslå
bakgrunnsbilder** fra byggebransjen. Følg `site/design-brief.md` slavisk. **Du rører IKKE
`site/index.html`** — den er Lars sin lærings-/håndkodingsfil. All din output ligger i `site/mockup/`.

## Rollefordeling (ærlighetsregel)

- **AGY (deg):** bygg mockup + bildeforslag i `site/mockup/`. Lever visuell prøve + screenshots.
- **Claude:** skrev denne handoffen og design-briefen. Styrer deg ikke direkte.
- **Lars Erik:** godkjenner retning, leverer evt. logo-fil og egne bilder, avgjør grensetilfeller.
- **Codex (senere):** kan bygge produksjonssiden etter godkjent mockup — ikke din jobb nå.

## Inndata (les for kontekst — i dette repoet)

- `site/design-brief.md` — **sannhetskilden for utseendet.** Palett, «myke flater, fokus på fakta».
- `site/index.html` — den semantiske HTML-strukturen (les for layout/seksjoner — **ikke endre**).
- `AGENTS.md` — roller + kilde-/sannhetsregler (gjelder også fakta i mockupen).
- `docs/agents/domain.md` — vokabular (VERIFIED, VIBS, status-porter).

## Design-retning (oppsummert fra briefen — bindende)

- **Identitet:** VIBS gull/sennep (~`#E8B23E`) + nær-sort (`#1A1A1A`) + krem (`#F6F0E2`). Gull er den ekte merkevaren (ikke produktappens grønne).
- **Bakgrunnsflater = ekte byggebransje-foto, men DEMPET** — mørkt + avmettet lag over bildet, ikke vivid fargefoto. Bildet er bakteppe.
- **Gull reservert til faktaene** — tall, overskrift-detalj, tynn linje, logo. Ikke gull-toning av selve bildene. (Tillatt: en *anelse* varme i bildetonen.)
- **Faktabokser:** små, myke, dukker opp ved scroll (subtil fade/stigning). Myk mørk/translucent flate, krem tekst, ett gull-nøkkeltall.
- **Mykhet:** dempede bilder · myke gradient-overganger mellom seksjoner · avrundede kanter · god luft · subtil bevegelse (aldri sprettende).
- **Tone:** troverdig/kompetent for Forskningsrådet/partnere. Rolig, ikke selgende.
- **Typografi:** ren sterk sans (vurder **Geist** for konsistens med VIBS-appen).
- **Mobil-først**, deretter desktop.

## Det du skal levere (alt i `site/mockup/`)

1. **Visuell mockup** (`site/mockup/`): statisk HTML/CSS som viser **2–3 representative seksjoner**
   (hero + minst én faktaseksjon) i full kvalitet etter retningen over. Mobil-først + desktop.
   Demonstrer: dempet mørkt bakgrunnsfoto, myk faktaboks med ett gull-nøkkeltall, myk overgang,
   logo-plassering. Bruk **plassholder-fakta tydelig merket `[placeholder]`** — *ingen oppdiktede
   statistikk-tall* (kilderegel).
2. **Screenshots** (`site/mockup/screens/`): mobil + desktop av mockupen, så Lars ser den uten å kjøre noe.
3. **Bildeforslag** (`site/mockup/bakgrunnsbilder-forslag.md`): 8–12 kandidater fra byggebransjen.
   Per kandidat: **kilde-URL, lisens (må være fri/lovlig brukbar), hvorfor den passer (myk/troverdig),
   og anbefalt behandling** (mørkt/avmettet-verdier). Last ned KUN bilder med lisens som tillater det,
   til `site/mockup/kandidater/`, og vis dem **dempet** som forhåndsvisning. Prioriter Unsplash/Pexels
   (gratis) og noter attribusjon der det kreves.

## Ikke-mål

- **Ikke rør `site/index.html`** (Lars håndkoder den selv) eller `site/styles.css`/`scrollspy.js`.
- Ikke bygg hele produksjonssiden — dette er en mockup/retningsbevis.
- Ikke rør kanoniske IPN-dokumenter i `docs/reference/`.
- Ikke dikt opp fakta/tall som ser verifiserte ut — bruk merkede plassholdere.
- Ikke bruk opphavsrettsbeskyttede/ulisensierte bilder.

## Akseptansekriterier

1. Mockupen følger `site/design-brief.md`: gull reservert til fakta, dempet mørkt foto, myke
   faktabokser, myke overganger, troverdig tone. Mobil **og** desktop er vist (screenshots finnes).
2. `site/index.html`, `styles.css` og `scrollspy.js` er **urørt**.
3. Ingen oppdiktede tall — alle fakta merket `[placeholder]`.
4. `bakgrunnsbilder-forslag.md` har 8–12 kandidater, hver med kilde + lisens + behandling. Nedlastede
   bilder er kun lovlig lisensierte og vist dempet.
5. Eksakt gull-hex: bruk ~`#E8B23E`, men flagg at den bør bekreftes mot logo-fila hvis Lars leverer den.

## Startprompt (lim inn til AGY i VS Code)

```text
Jobb i repoet C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified.
Les docs/handoffs/30_agy_mockup_og_bakgrunnsbilder_handoff.md og site/design-brief.md.

Oppgave: lag en høy-fidelity mockup (statisk HTML/CSS, 2–3 seksjoner, mobil-først +
desktop) av VERIFIED-scrollytelling-statussiden, og foreslå 8–12 bakgrunnsbilder fra
byggebransjen. ALT du lager ligger i site/mockup/ — IKKE rør site/index.html,
styles.css eller scrollspy.js (Lars håndkoder dem selv).

Følg design-briefen: VIBS gull (~#E8B23E) + nær-sort (#1A1A1A) + krem (#F6F0E2);
bakgrunn = dempet/mørkt ekte byggebransje-foto (ikke vivid fargefoto); gull KUN som
aksent på fakta (tall/overskrift/linje/logo); små myke faktabokser som dukker opp ved
scroll; myke overganger; troverdig/kompetent tone for Forskningsrådet. Bruk
plassholder-fakta merket [placeholder] — ingen oppdiktede tall.

Lever: (1) mockup i site/mockup/, (2) screenshots (mobil+desktop) i site/mockup/screens/,
(3) site/mockup/bakgrunnsbilder-forslag.md med kilde+lisens+behandling per kandidat, og
kun lovlig lisensierte nedlastede bilder (dempet) i site/mockup/kandidater/.
```
