# PRD — VERIFIED statusside

**Feature:** verified-statusside · **Dato:** 2026-06-28 · **Status:** utkast
**Eier:** Lars (godkjenner) · **Spec-kilder:** `site/design-brief.md`, `site/innhold-kanban.md`, `site/benchmark-forbilder.md`, `site/tekstmanus.md`

> Denne PRD-en konsoliderer det vi har bygd. Detaljene for *utseende* bor i `design-brief.md`,
> *innhold/fakta* i `innhold-kanban.md`, og *forbilder/v2-retning* i `benchmark-forbilder.md`.

## 1. Problembeskrivelse — hva løser vi?

VERIFIED er et **IPN-forskningsprosjekt** (Innovasjonsprosjekt i næringslivet, Forskningsrådet) som
trenger en **offentlig statusside**. I dag finnes ingen. Utfordringen er å presentere et FoU-prosjekt
der mye fortsatt er **uavklart**, på en måte som samtidig er:

- **troverdig og proff** for en Forskningsrådet-/partner-leser (ikke en «enkel kode-greie»),
- **ærlig** — viser *hva vi vet* og *hva vi ikke vet ennå* (forskningsfronten), uten å overdrive,
- **lojal mot prosjektets egen tese** om *synlig datakvalitet*: ingen uverifiserte tall som påstand,
- **forståelig for «enkle folk»** (SMB-entreprenører/boligkjøpere), uten fagsjargong.

## 2. Foreslått løsning — overordnet arkitektur

Statisk, **mobil-først scrollytelling-side**. Ren HTML/CSS/JS, **ingen build**. Bor i `site/`
(prototype i `site/mockup/`; produksjonssiden bygges derfra).

- **7 seksjoner** (arc i `innhold-kanban.md`): Hero → Utfordringen → Hva vi vet → Hva vi ikke vet → Hva vi skal finne ut → Hvorfor oss → Status nå.
- **Sticky sidemeny (desktop) / uttrekkbar drawer (mobil)** med seksjonsnavigasjon + forskningsinfo + partnerstripe.
- **Scrollspy** via `IntersectionObserver` (markerer aktiv seksjon).
- **Merke:** VIBS gull/sort. VERIFIED foregrunnet (ordmerke); VIBS/SINTEF + konsortium som partnere.
- **Visuelt v2:** dempet **navy-duotone** bakgrunnsfoto, **subtil CSS scroll-reveal**, **fakta-viz** (vet/vet-ikke-kontrast + 32 %-bar), myke (av-«dashboard») faktablokker.

## 3. Brukerhistorier

- Som **NFR-evaluator** vil jeg på sekunder forstå hva prosjektet er, og tydelig se *hva som er kjent* vs *hva som er kunnskapshullet* — så jeg kan vurdere FoU-høyden.
- Som **partner/investor** vil jeg se at prosjektet er seriøst, og hvem som står bak (konsortium + nøkkelpersoner).
- Som **SMB-leser** (snekker/byggmester) vil jeg forstå innholdet uten LCA-/akademisk sjargong.
- Som **mobilbruker** vil jeg ha en lett, lesbar opplevelse med en meny som åpnes/lukkes greit.
- Som **tastatur-/skjermleserbruker** vil jeg navigere via skip-link, landmarks og fungerende fokus.

## 4. Edge cases & feilhåndtering

- **Uten JavaScript:** ankerlenkene virker fortsatt; innholdet er lesbart. (Drawer-toggle krever JS — fallback bør sikre at navigasjon ikke låses.)
- **`prefers-reduced-motion: reduce`:** all bevegelse (reveal, scroll-puls) slås av.
- **Bilde mangler/treg lasting:** navy basefarge (`#11111f`) vises; lesbarhetsoverlegget sikrer at tekst alltid har nok kontrast.
- **Liten/mellomstor skjerm:** drawer i stedet for sidebar; ingen horisontal overflow.
- **Uverifisert innhold (kildedisiplin):** kun **🟢-fakta** vises som påstand; **🟡** fraseres «forskning indikerer» med stille kilde; **🔴** holdes ute. **Ingen statusfarger vises** på siden (interne).
- **WCAG:** gull kun som aksent (ikke brødtekst); krem/hvit-på-navy ≥ AA; dempet bildetone mørk nok til lesbarhet.

## 5. Out of scope (bygges IKKE nå)

- Backend, CMS, database, innlogging, skjema.
- Den **større Grønn plattform-siden** (eget, større løp — 2027–2030).
- **Lærings-`site/index.html`** — egen pedagogisk håndkodingsfil, ikke produksjonssiden.
- Full TDD-suite (statisk side — lett validering/a11y-sjekk i stedet).
- **Ekte scroll-pinnet** vet→vet-ikke-animasjon (vurderes/verifiseres live senere).
- Søknadsbeløp/økonomi offentlig.
- Eksplisitt omtale av NFR-vurderingskriteriene (skal treffes *implisitt*).

## 6. Tekniske begrensninger / implementasjonsbeslutninger

- **Plain HTML/CSS/JS, ingen rammeverk/build** — for læring og enkel deploy.
- **Palett (eksakt, merkevareguide):** `#11111f` (navy) / `#ffc600` (gull) / `#ffffff`. **Fonter:** Comfortaa (overskrift) + Quicksand (brødtekst, fallback for Hiruko).
- **Mobil-først**; desktop sticky sidebar via `@media (min-width:1024px)`.
- **Scrollspy + drawer:** `IntersectionObserver` + minimal JS.
- **Reveal:** CSS `animation-timeline: view()` (degraderer trygt der det ikke støttes; av ved reduced-motion).
- **Duotone:** `background-blend-mode: luminosity` + navy, så vanlige fargefoto blir konsistent navy-tonet uten forhåndsbehandling.
- **Bilder:** `site/mockup/kandidater/` (≥1920 px, liggende, lisensiert).
- **Kildedisiplin (`AGENTS.md`):** bare åpne, siterbare kilder; SINTEF primærverifiserer fra midten av august 2026.
- **Orkestrering:** Claude eier teksten nå (direkte fiks + verifisering mot kildene); AGY/Codex via handoffs ved behov.

## Status nå (hva er bygget)
- Mockup v2 i `site/mockup/` bygget og **visuelt verifisert** (`screens/v2/`). Tekst kildeforankret (5 hallusinasjoner rettet, konsortium + pilots + nøkkelpersoner inn).
- **Gjenstår:** kuratere/bytte klisjébilder, fullføre hard jargong-strip i «Hva vi vet», ev. pinnet overgang, og bygge produksjonssiden fra mockupen.

## Verifisering (Definition of Done for siden)
1. Alle 7 seksjoner rendrer mobil + desktop uten overflow; drawer + scrollspy virker.
2. Kun 🟢-fakta som påstand; ingen statusfarger; NFR-kriterier ikke nevnt eksplisitt.
3. WCAG AA-kontrast; `prefers-reduced-motion` slår av bevegelse; ankerlenker virker uten JS.
4. Merke korrekt (VERIFIED foregrunnet, VIBS/SINTEF + konsortium som partnere; eksakt palett/fonter).
5. Validér HTML (W3C) før deploy.
