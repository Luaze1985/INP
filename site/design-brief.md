# Design-brief — VERIFIED scrollytelling-statusside

Sannhetskilde for *utseendet* på `site/`. Bygges etter denne (av oss eller en kode-agent).
Status: **utkast til godkjenning** (Lars godkjenner). Forankret i grilling 2026-06-28.

## Formål og publikum
- **Seer:** Forskningsrådet / partnere (investor/partner, fagmiljø).
- **Følelse vi sikter mot:** *troverdig og kompetent* — «dette er et seriøst prosjekt med folk som kan dette». Rolig og institusjonelt, ikke selgende/blinkende.

## Merkevare og posisjonering
- **Siden er VERIFIED — et forskningsprosjekt**, ikke et VIBS-produkt. VIBS er selskapet/partneren bak (sammen med SINTEF og fagskole). VERIFIED foregrunnes; VIBS vises som *partner*.
- **Visuell estetikk beholdes:** sort på varm gull/sennep (VIBS' husuttrykk). Men toppmerket er en **VERIFIED-ordmerke** (typografisk — egen logo finnes ikke ennå), ikke VIBS-logoen.
- **Partnere** (VIBS, SINTEF, ev. fagskole) vises diskré i en partnerstripe (f.eks. nederst), ikke som hovedavsender.
- **Merkeverdier (fra VIBS merkevareguide):** logo = hvit «VIBS» + gul bue + «Vi Bygger Sammen» på navy-sort `#11111f`. Eksakt palett + fonter er nå kjent (se Palett/Typografi). VERIFIED-ordmerke settes i Comfortaa.

## Palett (eksakt — fra VIBS merkevareguide)
| Rolle | HEX | Bruk |
|---|---|---|
| Gull | `#ffc600` | **Aksent** — tall, ordmerke-detalj, tynn linje, CTA. Brukes sparsomt; det er det som holder helheten myk/premium. |
| Sort (navy) | `#11111f` | Base, mørke flater, overlegg over foto. NB: navy-tonet, ikke ren svart. |
| Hvit | `#ffffff` | Tekst/innhold på mørkt (ev. en hårfin varm off-white for mykhet) |

## Visuell retning: «myke flater, fokus på fakta»
- **Bakgrunnsflater = ekte byggebransje-foto, men dempet.** Mørkt + avmettet lag over bildet (ikke vivid fargefoto). Bildet er bakteppe, ikke hovedsak.
- **Gull reservert til faktaene.** Ikke gull-tonede bilder. Gullet dukker bare opp på tall/overskrift/linje/logo → øyet trekkes til fakta.
- **Faktabokser:** små, myke, dukker opp ved scroll (subtil fade/stigning). Myk mørk/translucent flate, krem tekst, ett gull-element (f.eks. ett nøkkeltall).
- **Mykhet skapes av:** dempede mørke bilder · myke gradient-overganger mellom seksjoner · avrundede kanter · god luft · subtil bevegelse (aldri sprettende/leken).
- **Typografi (fra merkevareguiden):** overskrift = **Comfortaa** (geometrisk, rund, gratis via Google Fonts); brødtekst = **Hiruko** (rund sans — bruk fallback som Quicksand/Nunito/Varela Round hvis Hiruko ikke er lisensiert). Runde/vennlige fonter matcher «enkle folk» og myke flater.

## Tilgjengelighet (ufravikelig)
- Gull = **aksent**, aldri stor brødtekst på sort (sliter på øyet / WCAG).
- Krem-på-mørk må ha nok kontrast. Dempet bilde-lag må være mørkt nok til at tekst alltid er lesbar (samme rolle som «lesbarhetslaget» i HTML-strukturen).

## Innholdsprinsipp — state of the art, ærlig
- Siden forteller **state of the art slik den er i dag: hva vet vi, og hva vet vi ikke.** Det vi *ikke* vet er ikke en svakhet — det er **selve forskningspremisset** (det SINTEF og andre forskningsmiljøer skal kvalitetssikre og forske frem).
- **Ingen status-farger på siden.** 🟢/🟡/🔴 er *interne* arbeidsverktøy (se `innhold-kanban.md`). Usikkerhet uttrykkes i klar tekst — «åpent spørsmål / det vi skal finne ut» — aldri som et gult varsel.
- **Ikke tallfokusert.** Tall brukes som lett tekstur der de er bunnsolide og siterbare, ikke som overskrifts-«hook». Hovedvekten er den kvalitative SoA-historien.
- **🔴-påstander holdes ute** (Wiik 2025, konfliktkostnad) — å vise uverifiserbart ville motsagt prosjektets egen tese om synlig datakvalitet.
- Hvert tall vi faktisk viser skal være forsvarlig og ha direkte kilde; omstridte funn fraseres som «forskning indikerer», ikke som VERIFIED sin påstand.

## Stemme og tone
- **Enkle, jordnære folk** — det er en del av VIBS-identiteten. Klart, direkte språk, ingen LCA-/akademisk sjargong, ingen oppblåste fraser. Som en dyktig fagperson som forklarer rett ut.
- **Kontrast som virkemiddel** — «vet / vet ikke» settes skarpt opp mot hverandre. Enkelhet + kontrast er signaturen.
- **Reguleringer, bærekraft og samfunnsnytte** hører hjemme i *Utfordringen* (EN 15978:2026, DPP/CPR 2024/3110, grønn finans, sirkulærøkonomi) — vist som *hvorfor dette haster nå*, ikke som en egen «compliance»-seksjon.
- **Treff NFR-kriteriene implisitt.** Kvalitet (FoU-høyde/SoA), Effekter (samfunns-/bærekraftsnytte) og Gjennomføring (team/SINTEF) skal *merkes* i innholdet — men **aldri nevnes eksplisitt** («dette møter kriterium X»).

## v2-løft — bevegelse, fakta-viz, språk, bilder (2026-06-28)
Forankret i ekte forbilder (se `benchmark-forbilder.md`). Hever v1 mot toppklasse uten å bryte kjernebriefen.
- **Bevegelse (middels):** subtil reveal (myk fade/stigning på faktabokser) + **én pinned «vet→vet-ikke»-overgang** der scrollen brukes til å sette kjernekontrasten. Respekter `prefers-reduced-motion`; hold mobil lett. Ikke effektjag.
- **Fakta-viz:** 1–2 enkle, elegante visuelle grep — visualiser signaturen «vet / vet-ikke» + ett nøkkeltall (~32 %). Faktakort skal lese **redaksjonelt og mykt**, ikke som SaaS-dashboard.
- **Språk (hard strip):** dagligspråk for «enkle folk». Fjern/forklar EPD, NOBB, LCA, MCDA, DPP i klartekst. Av-KI-fisering: korte setninger, ingen svulstige ord/superlativer, ingen repetert «bro». Se forbudsliste i `benchmark-forbilder.md`.
- **Bilder:** kuratere distinkte byggebransje-bilder + konsistent dempet **duotone**. Ingen «arbeidere som går»-klisjé.
- **Rytme:** varier seksjonsmønsteret (full-bleed, split, pinned) — ikke 7 identiske fullskjerm.

## Innhold (gjenstår — separat fra stil)
- Eksakt seksjonsliste + tekst per boks (jf. narrativ-arc i `innhold-kanban.md`).
- Kilde til byggebransje-foto (egne bilder? lisensiert?).

## Åpne punkter til Lars
1. Logo-fil (for eksakt hex + plassering).
2. Nøytralt mørke bilder, eller en anelse varme i tonen?
3. Har du byggebransje-bilder, eller må vi skaffe dem?
