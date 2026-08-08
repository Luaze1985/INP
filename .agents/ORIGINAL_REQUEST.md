# Original User Request

## Initial Request — 2026-06-28T18:01:58Z

The goal of this project is to review the current high-fidelity mockup of the VERIFIED research status page, search the web for design references of credible research and academic portals—specifically looking up design styles from Google Stitch and Google Search—and create a comprehensive design improvement report. The team must NOT modify any code files directly.

Working directory: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\site\mockup
Integrity mode: development

## Requirements

### R1. Design Review & Reference Search
The team must review the existing static HTML/CSS mockup in `site/mockup/` and search the web for design patterns of high-quality research, scientific, and academic portals. Specifically, they must:
- Search Google for visual layouts and design codes associated with "Google Stitch".
- Examine NFR/Norges forskningsråd portals, EU Horizon projects, or academic research showcases for design inspirations.

### R2. Design & Content Improvement Report
Draft a comprehensive improvement report (`site/mockup/improvements-proposal.md`). The report must propose specific changes to:
- Layout and structure (how to make the research focus stand out)
- Typographic hierarchy (improving readability of research targets)
- Accent colors and contrast ratios (ensuring WCAG compliance)
- The sidebar layout on mobile and desktop viewports

### R3. Alternative Image Proposals
Search for and propose 3-5 specific alternative background images from Unsplash/Pexels that represent local, authentic carpentry or wooden residential construction. For each image, provide the direct link, photographer credit, license, and why it matches the "enkle folk fra bygda" identity.

## Acceptance Criteria

### Improvement Report
- [ ] A markdown report is created at `site/mockup/improvements-proposal.md`.
- [ ] The report lists concrete, actionable design suggestions for layout, typography, and contrast.
- [ ] The report contains direct links to reference portals, Google Stitch design guides, or reference layouts for inspiration.
- [ ] The report proposes 3-5 new, specific background image candidates (IDs and links) that match the authentic local craftsman identity.

### Code Integrity
- [ ] The existing mockup HTML (`site/mockup/index.html`) and CSS (`site/mockup/mockup-styles.css`) remain unmodified.
- [ ] All other files in the project workspace remain unmodified.

## Follow-up — 2026-08-02T20:54:13Z

Sekvensiell gjennomgang av verifisert kilde- og evidensgrunnlag i VIBS VERIFIED IPN-prosjektet, og utarbeidelse av en omfattende forskningsrapport (State of the Art) klar for SINTEF-evaluering.

Working directory: `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified`
Integrity mode: `development`

Målfil: `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`

## Requirements

### R1. Kilde- og evidenssjekk
Gjennomgå og verifiser konsistensen mellom kanonisk kildedom (`docs/reference/vibs-verified-kildedom-2026-06-27.md`), kildebibliotek (`docs/reference/ipn-kildebibliotek.md`), ord- og kildekart (`docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`), evidensmatrise (`research/evidence_matrix.md`) og handoff 40-søkekøen.

### R2. Omfattende forskningsrapport (State of the Art)
Utarbeid en fullstendig og strukturert forskningsrapport på `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md` som dekker:
1. **Sammendrag og hovedkonklusjon** for SINTEF-evaluering.
2. **Metodisk fundament (LCA/LCC og datakvalitet):** Multiconsult/DiBK 70 % A1–A3 i 4 referansebygg, TEK17 1,25-faktor for generiske data, Weidema Pedigree-matrise, Edelen & Ingwersen formålsavhengig DQI uten skjult totalscore, EN 15978:2026 rehabilitering, ISO 14040/EN 15804+A2/ISO 15686-5.
3. **Flerkriterieanalyse og usikkerhet (MCDA):** Mecca 2023 review, håndtering av usikkerhet som synlig datagrunnlag, metodisk forbehold mot TOPSIS/COPRAS/VIKOR rank reversal uten at det påstås ferdig bevist.
4. **Finans- og reguleringskontekst:** Billio (nederlandske boliglån), Kaza (~32 % ENERGY STAR), An (34 % CMBS næringsbygg), EBA EU 2023 (frivillig EU-lånemerke), BoE PS25/25 (klimarisikostyring juni 2026), BoE DP1/25 (IRB PD/LGD uten klima), samt det eksplisitte FoU-hullet for holdbarhet/fuktrobusthet → kredittrisiko/PD.
5. **Norsk SMB-kontekst og tilbudsbeslutninger:** Nordic Council 2023 (lempeligere krav for SMB-konkurransekraft), BKA2 (SINTEF v/ Vegard Knotten 11,7 MNOK), SmartKalk Miljø (kalkyleintegrert EPD), Reduzer (anbud), Concular (ombruk+garanti), ORIS (infrastruktur/tilbud med manuell input).
6. **Syntese og VERIFIEDs avgrensede FoU-gap:** Sammenstilt funksjonsmatrise (6 akser) som viser at verktøyene dekker enkeltdeler, mens VERIFIEDs nyhetsverdi ligger i den integrerte, forklarbare testen av alle 6 akser for norsk SMB i tilbudsfasen.

### R3. Kildekritisk og ontologisk samsvar
Følg begrepsreglene i `vibs-verified-ord-og-kildekart-v0.5.yml` uten avvik:
- Bruk «løsningsvalg» (ikke smalt «produktvalg»).
- Unngå «VERIFIED velger / anbefaler automatisk» og «svart boks».
- Bruk «testflate» om VIBS-plattformen.
- Bevar parkerte kilder (`[Wiik2025]`, `[SA2018]`) med ⏸-status og bruk `[EBA_NO2023]` og `[KD2024]` som bærende kilder.
- Skill strengt mellom `[EBA_EU2023]` (bank) og `[EBA_NO2023]` (bygg).

## Acceptance Criteria

### Dokumentsamsvar og kildeverifikasjon
- [ ] Dokumentet `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md` er opprettet med komplett og lesbar markdown-struktur.
- [ ] Alle påstander er merket med kildestatus (🟢, 🟡, ⏸, 🔴) i samsvar med autoritativ kildedom.
- [ ] Ingen absolutte gap-påstander («ingen verktøy finnes») framsettes som fakta utenfor det undersøkte utvalget.
- [ ] Rapporten skiller eksplisitt mellom etablert kunnskap, leverandørfunksjoner, empirisk dokumenterte effekter og prosjektets FoU-hypoteser.

## Follow-up — 2026-08-02T21:22:13Z

Spisset utarbeidelse av kapittel K3 (Forskning og FoU-høyde) for VIBS VERIFIED IPN-søknaden, basert på uavhengige internasjonale og norske forsknings- og myndighetskilder i repoet, NFRs IPN-kriterier og prosjektets Sannhetsserum.

Working directory: `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified`
Integrity mode: `development`

Målfil: `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md`

## Requirements

### R1. Spisset K3 Forskning & FoU-høyde (NFR IPN-kriteriet)
Utarbeid et dedikert kandidatnotat for kapittel K3 på `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md`. Notatet skal spisses mot NFRs kriterier for Forskningsrådsstøttede IPN-prosjekter og integrere både internasjonale og **norske uavhengige forsknings- og myndighetskilder**:
1. **Norske forsknings- og myndighetskilder:**
   - **Gullbrekken & Holme (2025)** `[GullbrekkenHolme2025]`: SINTEF-forskning på byggskader (10–30 mrd NOK/år, 1 feil i halvparten av boliger).
   - **Ingvaldsen (2008)** `[Ingvaldsen2008]`: Byggforsk-studie av byggfeil, levetid og skaderisiko.
   - **Bjørheim mfl. (2026)** `[Bjørheim2026]`: SINTEF-forskning på sirkulære byggevarer og ombruksdokumentasjon.
   - **KD / DiBK (2024)** `[KD2024]`: *Byggenæringens klimafotavtrykk – et kunnskapsgrunnlag* (63 % A1–A3, tidligfase-påvirkningsrom).
   - **Multiconsult for DiBK (2023)** `[Multiconsult2023DiBK]`: 70 % A1–A3 i fire referansebygg.
   - **EBA Norge mfl. (2023)** `[EBA_NO2023]`: *Veileder for klimagassreduksjoner – boligblokker* (20 % utslippskutt fra materialvalg utan merkostnad).
   - **BKA2 / Vegard Knotten (SINTEF, 2024–2028)** `[BKA2]`: Bærekraftige anskaffelser for vanlige BA-prosjekter (11,7 MNOK).
   - **Finans Norge (2024)** `[FinansNorge2024VASK]`: Skadestatistikk (5,1 mrd. kr i vannskader i 2023).
2. **Internasjonal forskning:** Edelen & Ingwersen 2018 (formålsavhengig DQI), Weidema 1996 (Pedigree-matrise), Mecca 2023 (MCDA review), Benke 2025 (LCA-variasjon), Lohman 2023 (usikkerhetsvisning), Billio 2022 (nederlandske boliglån), Kaza 2014 (~32 % ENERGY STAR), An & Pivo 2020 (34 % CMBS næringsbygg 🟡), Ciroth 2016 (empirisk pedigree).
3. **De 6 sentrale FoU-spørsmålene (F1–F6):** Formuler og utdyp prosjektets seks forskningsspørsmål med tilhørende hypoteser, uavhengig norsk og internasjonal kildedokumentasjon og eksperimentelle målepunkter.
4. **Forskningsmetode og testsløyfe:** Beskriv den iterative forskningsprosessen fra datamodellering og usikkerhetsrepresentasjon (DQI/Pedigree) til utprøving i pilotprosjekter.

### R2. Sannhetsserum- og kildehierarkisamsvar
Innarbeid alle relevante prinsipper fra `docs/reference/prosjektbeskrivelse/sannhetsserum-oppdatering-v0.5.md` og AGENTS.md:
- Bruk kun **uavhengige forsknings- og myndighetskilder** som bærende bevis (🟢 eller 🟡 med forbehold).
- Konsortie-interne notater (`[Wiik2025]`) og uverifiserte rapporter (`[SA2018]`) bevares som parkert ⏸ og skal ikke bære søknadspåstander alene.
- Målte pilotresultater skal skille eksplisitt fra beregnede framtidige virkninger.
- Klimaeffekt fremstilles som et *mulighetsrom* som skal utforskes og måles, ikke som en garantert effekt.
- Skjul aldri svak levetid, fuktrisiko eller dokumentasjonsmangler bak lav pris eller lav CO₂-skår.

### R3. Ontologisk og terminologisk samsvar
Følg begrepsreglene i `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`:
- Bruk «løsningsvalg» (ikke smalt «produktvalg»).
- Unngå «VERIFIED velger / anbefaler automatisk» og «svart boks».
- Bruk «testflate» om VIBS-plattformen.
- Skill strengt mellom `[EBA_EU2023]` (bank) og `[EBA_NO2023]` (bygg).

## Acceptance Criteria

### K3-notatets fullstendighet og kildekvalitet
- [ ] Kandidatfilen `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md` er opprettet med komplett og velstrukturert markdown.
- [ ] Både norske forsknings- og myndighetskilder (Gullbrekken & Holme 2025, Ingvaldsen 2008, Bjørheim 2026, KD/DiBK 2024, Multiconsult 2023, EBA Norge 2023, BKA2/Knotten, Finans Norge 2024) og internasjonale kilder er integrert.
- [ ] Samtlige 6 FoU-spørsmål (F1–F6) er eksplisitt forankret i uavhengige forskningskilder og belagt med kildestatus (🟢, 🟡, ⏸).
- [ ] Notatet tilfredsstiller alle 31 kontrollpunkter i Sannhetsserumet som angår forskningsdesign, metodisk avgrensning og etikk.
- [ ] Ingen leverandørpåstander eller uverifiserte notater benyttes som uavhengig forskningsbelegg.

## Follow-up — 2026-08-02T21:22:35Z

Viktig oppdatering fra Lars (bruker): De norske forsknings- og myndighetskildene (Gullbrekken & Holme 2025, Ingvaldsen 2008, Bjørheim 2026, KD/DiBK 2024, Multiconsult 2023, EBA Norge 2023, BKA2/Knotten, Finans Norge 2024) er DE VIKTIGSTE og skal utgjøre det primære fundamentet i K3-notatet. De europeiske/internasjonale kildene (Edelen, Weidema, Mecca, Benke, Billio, Kaza, EBA EU, BoE) følger deretter som den internasjonale forsknings- og reguleringskonteksten. Enforce denne prioriteringsrekkefølgen i teksten.

