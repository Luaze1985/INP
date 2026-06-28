# Google Stitch Readiness Review: VERIFIED Mockup

Dette er en grundig gjennomgang av mockupen for VERIFIED-statussiden som en Google Stitch-klar prototype, basert på retningslinjer for mobiltilpasning og Google Stitch sine prinsipper for UI-generering.

---

## Rapportdetaljer
- **Status**: Vurderingsrapport (Venter på godkjenning)
- **Verdict**: `partly_ready`

---

## 1. Top 5 Blockers (Kritiske mangler)
1. **For mørke bakgrunnsbilder (For sorte)**: Overleggene på bildene (`.story-section__readability-overlay`) har for høy opasitet (opptil 93% på mobil og 94% på desktop), noe som gjør at bildene oppleves som "for sorte". Vi må lyse dem opp ved å redusere opasiteten på overlegget, men samtidig beholde tilstrekkelig WCAG-tekstkontrast.
2. **Scroll Snapping på mobil**: Global scroll snapping på `html`-elementet gjør navigasjonen ustabil og og vanskelig på mobil. Hvis en seksjon (f.eks. `#sec-challenge` med 4 kort) har mer innhold enn skjermhøyden på en mobil, vil brukeren oppleve scroll-lås (scroll-fighting).
3. **Mangel på interaktive tilstander (States)**: Det mangler definerte stiler for `:focus-visible` (tastaturnavigasjon), `:active`, `disabled`, `loading`, og `error`-tilstander på knapper, lenker og kort.
4. **Verdiforslag og målgruppe (Første 10 sekunder)**: Overskriften i heroen (*"Her er hva vi vet. Her er hva vi skal finne ut."*) er for abstrakt for en travel byggmester. Den bør umiddelbart kommunisere den praktiske verdien: et enkelt, uavhengig beslutningsverktøy for trygge materialvalg.
5. **Mangel på spesifikke mobile regler for 320/375/414 px**: Siden er responsiv generelt, men har ikke finjusteringer for svært smale skjermer (f.eks. 320px) der tekstomlasting og polstring (*padding*) kan sprekke eller skape unødvendig mye luft.

---

## 2. Spesifikke CSS/HTML-risikoer
- **Mørkt overlegg**: I [mockup-styles.css](file:///c:/Users/larse/Documents/Interne prosjekter/Vibs/ipn-verified/site/mockup/mockup-styles.css#L303-L311) og `[mockup-styles.css:L636-639](file:///c:/Users/larse/Documents/Interne%20prosjekter/Vibs/ipn-verified/site/mockup/mockup-styles.css#L636-L639)` er opasiteten på gradienten for høy.
- **Scroll Snap**: `scroll-snap-type: y mandatory;` på `html` og `scroll-snap-align: start;` på `.story-section` må deaktiveres for mobilvisning via media-queries.
- **Berøringsflater (Touch targets)**: `[.menu-toggle](file:///c:/Users/larse/Documents/Interne%20prosjekter/Vibs/ipn-verified/site/mockup/mockup-styles.css#L102)` har for små berøringsflater (`padding: 0.4rem 0.8rem`), noe som er under anbefalt standard (min. 44x44px).

---

## 3. Manglende DESIGN.md-regler
Det finnes foreløpig ingen [DESIGN.md](file:///c:/Users/larse/Documents/Interne prosjekter/Vibs/ipn-verified/site/mockup/DESIGN.md) i mappen. For at en AI-agent (Stitch/Codex) skal kunne iterere på dette uten å gjette, må følgende regler formaliseres:
- **Farge-tokens**: Definisjon av `--color-bg-navy` (`#11111f`) og `--color-gold` (`#ffc600`) samt grenser for opasitet for å unngå kontrastbrudd (WCAG AA).
- **Forbudte mønstre**:
  - *Ikke* bruk scroll-snapping på mobil når innholdet kan flyte over.
  - *Ikke* bruk dekorative elementer eller fake data i statistikk-kort.
- **Tilstander (States)**: Eksplisitte regler for hvordan hover, focus, active, loading og disabled skal se ut.

---

## 4. Anbefalt Google Stitch Prompt (for iterasjon)
Bruk denne prompten for å redigere skjermen via Stitch:
```text
Edit this screen:
1. Adjust the dark background overlays to let more image detail show through, making the backgrounds lighter and less dark. Ensure text contrast remains high (min. 4.5:1 ratio).
2. Refactor the hero title to instantly highlight the project's value for Norwegian building contractors (e.g. "Enkelt og uavhengig beslutningsverktøy for trygge materialvalg").
3. Disable vertical scroll snapping for viewports smaller than 1024px.
4. Improve the mobile menu toggle touch target to a minimum of 44x44px.
```

---

## 5. Anbefalt neste patch (Tredje iterasjon)
Når du godkjenner, foreslår vi å patche følgende i [mockup-styles.css](file:///c:/Users/larse/Documents/Interne%20prosjekter/Vibs/ipn-verified/site/mockup/mockup-styles.css):
*   **Lysere bakgrunner**: Justere gradientene i `.story-section__readability-overlay` til lavere opasiteter, f.eks. `rgba(17, 17, 31, 0.55)` til `rgba(17, 17, 31, 0.80)`.
*   **Mobil scroll-snapping**: Flytte `scroll-snap-type` til et desktop-spesifikt media-query (`@media (min-width: 1024px)`).
*   **Tastaturfokus**: Legge til universelle `:focus-visible`-stiler for bedre tilgjengelighet.

---

## 6. Skjermbilder som må regenereres
Etter at endringene er patchet, må [capture_screens.py](file:///c:/Users/larse/Documents/Interne%20prosjekter/Vibs/ipn-verified/site/mockup/capture_screens.py) kjøres på nytt for å oppdatere:
- [mobile.png](file:///c:/Users/larse/Documents/Interne%20prosjekter/Vibs/ipn-verified/site/mockup/screens/mobile.png)
- [desktop.png](file:///c:/Users/larse/Documents/Interne%20prosjekter/Vibs/ipn-verified/site/mockup/screens/desktop.png)
