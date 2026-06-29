# Startprompt — Claude Code-appen (deploy til Vercel/Netlify)

Kopier alt under streken og lim inn som første melding i Claude Code-appen.

---

Du starter arbeidet på VERIFIED-statussiden, et IPN-forskningsprosjekt (Norges Forskningsråd).
Repoet er allerede klonet og kildedisiplin-klar. Les disse tre filene FØRST:

1. `AGENTS.md` — sikkerhetsregler, kildedisiplin og orkestreringsprinsipper
2. `site/design-brief.md` — eksakt palett, fonter, visuelle regler og v2-løft
3. `site/mockup/index.html` — siden vi jobber med (mockupen)

---

## Hva som skal bygges nå

### 1. Deploy-oppsett (Vercel eller Netlify)
Siden er statisk HTML/CSS/JS — ingen build-steg. Målet er at `site/mockup/index.html`
(og tilhørende filer) er tilgjengelig på en offentlig URL så snart som mulig.

Lag deploy-konfigurasjon for **Vercel** (foretrukket) eller **Netlify**:
- Vercel: `vercel.json` i roten med `outputDirectory: "site/mockup"`
- Netlify: `netlify.toml` med `publish = "site/mockup"`
- Ingen build-kommando trengs — ren statisk side
- Sett `site/mockup/` som rot for deploy (index.html + mockup-styles.css + kandidater/)

### 2. Jargong-strip i seksjon 3 («Hva vi vet i dag»)
Filen er `site/mockup/index.html`, seksjon `#sec-what-we-know` (rundt linje 155–177).
Disse tekniske termene trenger klartekst-forklaring eller fjerning:
- **EPD** → forklar i parentes: «miljødeklarasjoner (EPD)» eller bare «miljødokumentasjon»
- **NOBB** → forklar: «produktregisteret NOBB» eller bare «store produktbaser»
- **MCDA** → forklar: «flerkriterieanalyse (en metode for å veie ulike egenskaper mot hverandre)»

Målgruppen er snekkere og boligkjøpere — ikke fagspesialister.

### 3. Bildeoppsett (venter på nye bilder fra Lars)
Bakgrunnsbildene ligger i `site/mockup/kandidater/kandidat-1.jpg` → `kandidat-7.jpg`.
Lars genererer nye bilder (DALL-E). Når de er klare: overskriv filene direkte.
Ingen kodeendring trengs — filnavnene er allerede låst i HTML.

---

## Hva du IKKE skal røre

- `site/index.html` og `site/styles.css` — Lars sin lærings-/håndkodingsfil. Aldri endre.
- Kildedisiplin: Legg aldri til påstander uten kilde i `site/mockup/index.html`.
  Les `AGENTS.md` for status-porter (🟢/🟡/🔴). 🔴-funn = rett umiddelbart.
- `docs/reference/` — kildedokumenter, ikke endre disse.

---

## Teknisk kontekst

- **Palett:** `#11111f` (navy/sort) · `#ffc600` (gull) · `#ffffff`
- **Fonter:** Comfortaa (overskrift) + Quicksand (brødtekst) — lastes fra Google Fonts
- **Ingen rammeverk, ingen build** — ren HTML/CSS/JS
- **Duotone:** `background-blend-mode: luminosity` + `background-color: #232336` på `.story-section`
- **Scroll-reveal:** `animation-timeline: view()` — av ved `prefers-reduced-motion: reduce`
- **Navigasjon:** Sticky sidebar (desktop ≥1024px) / drawer (mobil) via `IntersectionObserver`
- **Bilder:** Alle 10 kandidatbilder i `site/mockup/kandidater/` (kun 7 brukes i HTML)

## Sist kjørte faktasjekk
- 2026-06-29: 0 🔴 — siden er kildedisiplin-klar
- Rapport: `site/mockup/faktasjekk-2026-06-29.md`
- Åpent: Thomas Thorsen (akseptert manuelt av Lars), 3 🟡-kilder venter SINTEF-verifisering fra aug 2026

---

Start med deploy-oppsettet. Spør Lars om han foretrekker Vercel eller Netlify.
