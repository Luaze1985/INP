---
title: Handoff (AGY) - Innholdstro mockup av VERIFIED-statusside + bakgrunnsbilder
date: 2026-06-28
status: ready
from: claude
to: antigravity (AGY)
branch: antigravity/site-mockup (foreslått)
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
supersedes: docs/handoffs/30_agy_mockup_og_bakgrunnsbilder_handoff.md
tags: [vibs, verified, ipn, site, mockup, innhold, design, agy]
---

# Handoff (AGY): Innholdstro mockup + bakgrunnsbilder

## Kort beskjed

Bygg en **høy-fidelity mockup** av VERIFIED-statussiden med det **ekte innholdet og narrativet** —
ikke plassholder-fluff. Følg `site/design-brief.md` (look + stemme) og `site/innhold-kanban.md`
(narrativ + hvilke fakta som kan vises). **Erstatter handoff #30.** Du rører IKKE `site/index.html`,
`styles.css` eller `scrollspy.js` — alt ligger i `site/mockup/`.

## Rollefordeling (ærlighetsregel)

- **AGY (deg):** bygg innholdstro mockup + bildeforslag i `site/mockup/`. Lever screenshots.
- **Claude:** skrev denne handoffen + de to spec-dokumentene. Styrer deg ikke direkte.
- **Lars Erik:** godkjenner, leverer VIBS-logo/farge-fil og ev. egne bilder.
- **Codex (senere):** kan bygge produksjonssiden etter godkjent mockup.

## Bindende spec (les disse — de er sannhetskilden)

- **`site/design-brief.md`** — look, palett, «myke flater», **stemme/tone**, posisjonering, innholdsprinsipp.
- **`site/innhold-kanban.md`** — narrativ-arc (7 seksjoner), hero (valgt B), og 🟢/🟡/🔴-fakta (🟢 = kan vises).
- `AGENTS.md` + `docs/agents/domain.md` — kilderegler + vokabular.

## Ikke-forhandlbare punkter (lett å bomme på — gjenta fra speccen)

1. **VERIFIED er et forskningsprosjekt — ikke et VIBS-produkt.** Toppmerke = **VERIFIED-ordmerke** (typografisk). VIBS + SINTEF (+ fagskole) vises som **partnere** i en diskré partnerstripe (f.eks. nederst), ikke som hovedavsender.
2. **Estetikk (eksakt, fra VIBS merkevareguide):** navy-sort `#11111f` + gull `#ffc600` + hvit tekst. Overskrift i **Comfortaa**, brødtekst **Hiruko** (rund fallback ved behov). Dempet/mørkt ekte byggebransje-foto som bakteppe — *ikke* vivid fargefoto. Gull reservert til aksent. Myke flater, myke overganger, avrundet, god luft.
3. **Stemme:** direkte **«vi»-stemme**, korte setninger, jordnært dagligspråk («enkle folk»). Ingen LCA-/akademisk sjargong.
4. **Struktur = kontrast «vet / vet-ikke».** Følg de 7 seksjonene i Kanban-en. Hero (eksakt tekst):
   - Overskrift: **«Her er hva vi vet. Her er hva vi skal finne ut.»**
   - Underlinje: *«VERIFIED er et forskningsprosjekt for tryggere og mer bærekraftige byggevalg — bygd på åpen kunnskap, kvalitetssikret av SINTEF.»*
5. **Ingen statusfarger på siden.** 🟡/🔴 er interne. Usikkerhet uttrykkes i klar tekst («åpent spørsmål / det vi skal finne ut»), aldri som gult merke.
6. **Tall som lett tekstur, ikke overskrift.** Bruk kun 🟢-fakta fra Kanban-en, med stille kilde. 🔴 (Wiik 2025, konfliktkostnad) er ute. 🟡 kun som «forskning indikerer», ikke som VERIFIED sin påstand.
7. **Treff NFR-kriteriene implisitt** (Kvalitet/Effekter/Gjennomføring) — **aldri nevn dem eksplisitt**. Reguleringer/bærekraft/samfunn hører hjemme i *Utfordringen* som «hvorfor det haster nå».

## Det du skal levere (alt i `site/mockup/`)

1. **Innholdstro mockup** (`site/mockup/`): statisk HTML/CSS, **mobil-først + desktop**, som dekker hero + hele vet/vet-ikke-kjernen (minst seksjon 1–4) i full kvalitet, med ekte tekst i «vi»-stemmen.
2. **Screenshots** (`site/mockup/screens/`): mobil + desktop.
3. **Bildeforslag** (`site/mockup/bakgrunnsbilder-forslag.md`): 8–12 byggebransje-kandidater med **kilde, lisens, hvorfor den passer, anbefalt dempet behandling**. Last ned kun lovlig lisensierte til `site/mockup/kandidater/`, vist dempet.

## Ikke-mål

- Ikke rør `site/index.html`, `styles.css`, `scrollspy.js` (Lars håndkoder dem).
- Ikke bygg hele produksjonssiden — dette er en mockup.
- Ikke rør kanoniske IPN-dokumenter i `docs/reference/`.
- Ikke dikt opp tall; ikke bruk 🟡/🔴-fakta som påstander; ikke bruk ulisensierte bilder.

## Akseptansekriterier

1. Hero matcher eksakt tekst over. De 7 seksjonene følger Kanban-arc-en; «vet»/«vet-ikke» står i tydelig kontrast.
2. VERIFIED er foregrunnet; VIBS/SINTEF kun som partnere. Ingen VIBS-logo som hovedmerke.
3. Stemmen er «vi»/jordnær; ingen statusfarger; tall kun som lett 🟢-støtte med kilde.
4. Look følger design-briefen (gull/sort, dempet foto, myke flater). Mobil + desktop vist (screenshots finnes).
5. `site/index.html`/`styles.css`/`scrollspy.js` urørt. Bildeforslag har kilde+lisens per kandidat.

## Startprompt (lim inn til AGY i VS Code)

```text
Jobb i repoet C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified.
Les docs/handoffs/31_agy_mockup_innholdstro_handoff.md, site/design-brief.md og
site/innhold-kanban.md. (Denne erstatter handoff #30.)

Bygg en høy-fidelity, INNHOLDSTRO mockup (statisk HTML/CSS, mobil-først + desktop)
av VERIFIED-statussiden i site/mockup/ — IKKE rør site/index.html, styles.css eller
scrollspy.js.

Ikke-forhandlbart: VERIFIED er et FORSKNINGSPROSJEKT (ikke et VIBS-produkt) — VERIFIED-
ordmerke øverst, VIBS+SINTEF som partnere i en diskré stripe. Estetikk (eksakt, fra VIBS
merkevareguide): navy-sort #11111f + gull #ffc600 + hvit tekst; fonter Comfortaa
(overskrift) + Hiruko (brødtekst, rund fallback); dempet/mørkt ekte byggebransje-foto,
gull kun som aksent, myke flater/overganger. Stemme: direkte «vi», korte setninger,
jordnært. Struktur: kontrast
«hva vi vet» / «hva vi ikke vet ennå» (følg de 7 seksjonene i innhold-kanban.md).
Hero-overskrift eksakt: «Her er hva vi vet. Her er hva vi skal finne ut.» Underlinje:
«VERIFIED er et forskningsprosjekt for tryggere og mer bærekraftige byggevalg — bygd på
åpen kunnskap, kvalitetssikret av SINTEF.»

INGEN statusfarger på siden; usikkerhet i klar tekst. Tall kun som lett støtte, og kun
de 🟢-markerte i innhold-kanban.md (🔴 er ute). Treff NFR-kriteriene implisitt, aldri
nevn dem. Reguleringer/bærekraft hører til i «Utfordringen».

Lever: (1) mockup i site/mockup/, (2) screenshots (mobil+desktop) i site/mockup/screens/,
(3) site/mockup/bakgrunnsbilder-forslag.md (kilde+lisens+dempet behandling per kandidat)
+ kun lovlig lisensierte bilder i site/mockup/kandidater/.
```
