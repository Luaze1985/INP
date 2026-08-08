# State of the Art (SoA) og Forskningsanalyse for VIBS VERIFIED

**Dato:** 2026-08-02  
**Utført av:** Explorer 2 (Research & SOA Documentation Investigator)  
**Prosjekt:** VIBS VERIFIED — IPN-søknad til Norges forskningsråd (NFR)  
**Målfil for framtidig innfletting:** `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`  

---

## Executive Summary / Sammendrag

Denne analysen kartlegger det samlede kilde-, metodikk- og evidensgrunnlaget for utarbeidelsen av `forskning-og-soa-v0.5-kandidat.md`. Analysen er strukturert i henhold til de **6 obligatoriske seksjonene** definert i `ORIGINAL_REQUEST.md` og oppfyller ontologireglene i `vibs-verified-ord-og-kildekart-v0.5.yml` samt autoritativ kildedom (`vibs-verified-kildedom-2026-06-27.md`).

**Kjerneposisjonering:** VERIFIEDs FoU-høyde ligger **ikke** i å lage ennå et enkeltstående miljøverktøy, en ny EPD-database eller en svart-boks poengberegner. Nyhetsverdien ligger i å **utvikle og teste en integrert, forklarbar og etterprøvbar beslutningsmodell for sammenligning av alternative løsninger i tilbudsfasen for norsk SMB, der datakvalitet og usikkerhet synliggjøres uten å skjules i en totalscore.**

---

## 1. Kartlegging av eksisterende dokumentasjons- og forskningsfiler

Under undersøkelsen er følgede nøkkeldokumenter analysert i prosjektets `docs/` og `research/`-struktur:

1. **Autoritative kilde- og ontologidokumenter:**
   - `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`: Ontologisk kontrollkart for begrepsbruk, portstatus (🟢, 🟡, ⏸, 🔴), forbudte uttrykk og åpne konflikter.
   - `docs/reference/vibs-verified-kildedom-2026-06-27.md`: Autoritativ avstemming av 35+ kilder, korreksjoner av metadata (bl.a. An/Kaza/Billio, Finans Norge vannskadetall, NFR IPN-grenser).
   - `docs/reference/ipn-kildebibliotek.md`: Kanonisk kilderegister.
   - `research/evidence_matrix.md` & `research/research_synthesis.md`: Syntese av evidensstyrke, enighet/uenighet og manglende primærbevis.

2. **Kunnskapsgrunnlag og historiske SoA-utkast:**
   - `docs/reference/state-of-the-art-verified-ipn.md`: Tidligere v0.2 SoA-notat med 6 akser, verktøyscan og 14-punkts SINTEF-sjekkliste.
   - `docs/reference/prosjektbeskrivelse/k3-forskning.md` & `arbeidsversjoner/k3-forskning-godkjent-v0.1.md`: Låste FoU-spørsmål (F1–F6) og hovedmål for v0.5.
   - `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.5.md`: Gjeldende integrasjonskandidat for K1–K4 og V1–V3.
   - `docs/handoffs/37_agy_state-of-the-art_og_sintef-rapport_handoff.md` & `handoffs/40_agy_klargjor-kilde-og-kontekstpakker_read-only_handoff.md`: Antigravity audit-traseer for kildekontroll.

3. **Inntaks- og faktasjekk-filer under `.scratch/`:**
   - `.scratch/research-intake/gen-2026-07-29-01/factchecks/`: 01 (LCA/MCDA), 02 (Finans), 04 (Norske SMB-verktøy).
   - `.scratch/sintef-forskningsrapport-2026/research/sonar-primarkilder-2026-08-02.md`: Siste primærkilde-kontroll for verktoy (SmartKalk, Reduzer, ORIS, Concular).

---

## 2. Struktur og Seksjonsanalyse for `forskning-og-soa-v0.5-kandidat.md`

Det kommende dokumentet `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md` må bygges opp med følgende **6 obligatoriske seksjoner**:

```
docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md
├── Seksjon 1: Sammendrag og hovedkonklusjon for SINTEF-evaluering
├── Seksjon 2: Metodisk fundament (LCA/LCC og datakvalitet)
├── Seksjon 3: Flerkriterieanalyse og usikkerhet (MCDA)
├── Seksjon 4: Finans- og reguleringskontekst
├── Seksjon 5: Norsk SMB-kontekst og tilbudsbeslutninger
└── Seksjon 6: Syntese og VERIFIEDs avgrensede FoU-gap (med 6-akser matrise)
```

---

## 3. Detaljert innholdsanalyse og nøkkelkilder per seksjon

### Seksjon 1: Sammendrag og hovedkonklusjon for SINTEF-evaluering
- **Formål:** Gi SINTEF (Vegard Knotten / Lars Gullbrekken) en konsis, vitenskapelig forankret oppsummering som kan brukes direkte i vurderingen av prosjektets FoU-høyde og søknadskvalitet.
- **Kjernebudskap:**
  - Problemet er ikke mangel på enkeltdata eller verktøy, men at eksisterende løsninger lever i siloer, krever spesialistkompetanse og ikke er tilpasset tilbudsfasen i SMB-markedet.
  - VERIFIED skal **utvikle og teste** en forskningsbasert beslutningsmodell — prosjektet påstår ikke at effekten allerede er bevist.
  - **Ontologisk samsvar:** Følger strikt reglene i `ord-og-kildekart-v0.5.yml`:
    - Bruker begrepet «løsningsvalg» (ikke smalt «produktvalg»).
    - Unngår absolutte påstander om at «ingen verktøy finnes» (erstattes med «i det undersøkte utvalget»).
    - Unngår formuleringer som «VERIFIED velger / anbefaler automatisk» og «svart boks».
    - Bruker «testflate» om VIBS-plattformen.
    - Bevarer parkerte kilder (`[Wiik2025]`, `[SA2018]`) med ⏸-status, og benytter `[EBA_NO2023]` og `[KD2024]` som bærende kilder for tidligfase utslippsredusjons-mulighetsrom.

---

### Seksjon 2: Metodisk fundament (LCA/LCC og datakvalitet)
- **Internasjonale og norske standarder:**
  - **LCA:** ISO 14040/14044 (grunnleggende LCA-prinsipper) `[M]`, EN 15804+A2 (produkt-EPD kjerne-regler; obligatoriske moduler A1–A3, C1–C4, D) `[M]`.
  - **EN 15978:2026:** Publisert av CEN-CENELEC 17. april 2026. Erstatter EN 15978:2011. Standard for LCA på byggnivå, utvidet til eksplisitt å dekke nye bygg, eksisterende bygg og rehabiliterings- og ombruksprosjekter 🟢 `[EN15978-2026]`.
  - **LCC:** ISO 15686-5 (livssykluskostnader i service life planning) og **NS-EN 16627** 🟢 `[NS-EN16627]`. *NB: NS 3454 ble trukket 7. september 2023 og erstattet av NS-EN 16627 — VERIFIED må konsekvent forankre LCC i NS-EN 16627 / ISO 15686-5.*
- **Norske empiriske baselines og sikkerhetsfaktorer:**
  - **Multiconsult / DiBK (2023):** Utstøl & Marwig (rev. 06, 24.03.2023) *Klimagassutslipp fra byggematerialer*. Sammendrag s. 3 dokumenterer at produktfasen **A1–A3 utgjør i snitt 70 %** av samlede bundne utslipp i fire referansebygg (enebolig, firemannsbolig, boligblokk, kontorbygg). *Viktig forbehold:* Tallet gjelder rapportens fire case og systemgrenser, og må ikke framstilles som et universelt nasjonalt snitt for alle byggtyper.
  - **TEK17 & 1,25-faktor:** Nordic Sustainable Construction `us2024-428` ("Norway TEK17") & `us2024-415` (Häkkinen et al. 2024). Norsk TEK17-veiledning krever at dersom spesifikk EPD mangler og man bruker generiske data (f.eks. CO2data/Ökobaudat), skal utslippsverdien multipliseres med en **sikkerhetsfaktor på 1,25 (+25 %)** for å sikre at generiske data ikke favoriseres fremfor verifiserte EPD-er. (Svenske Boverket-data har til sammenligning en innbakt konservesjon på ~25 %).
- **Rammeverk for datakvalitet og usikkerhet:**
  - **Weidema & Wesnæs (1996) Pedigree-matrise:** 5 datakvalitetsindikatorer (pålitelighet, kompletthet, tidsmessig, geografisk, teknologisk korrelasjon, skåret 1–5), operasjonalisert i ecoinvent med basusikkerhet og lognormal Monte Carlo-simulering `[Weidema1996]` 🟡.
  - **Edelen & Ingwersen (2018):** Formålsavhengig DQI-rammeverk («fitness for purpose») 🟢 `[Edelen2018]`. Dokumenterer at datakvalitet må vurderes etter formål, og advarer eksplisitt mot å slå sammen datakvalitet til én enkel skjult totalscore ("hidden total score").

---

### Seksjon 3: Flerkriterieanalyse og usikkerhet (MCDA)
- **Litteraturgjennomgang for MCDA i bygg:**
  - **Mecca (2023):** Review i *Journal of Multi-Criteria Decision Analysis* (DOI 10.1002/mcda.1818) 🟡 `[Mecca2023]`. Tallfester metodefordelingen i bærekraftsanalyser for urban og arkitektonisk planlegging: **AHP 46 %, TOPSIS 20 %, MIVES 11 %, COPRAS 9 %**.
- **Synlig usikkerhetsvisning (ikke svart boks):**
  - **Lohman et al. (2023) DMsan-rammeverket:** Eksponerer usikkerhet og preferansefølsomhet («opportunity spaces») 🟢 `[Lohman2023]`. Viser under hvilke vekter og forutsetninger ulike alternativer vinner, uten å skjule usikkerheten i en samleskår.
  - **EC3 (Building Transparency):** Bruker konfidensintervaller og usikkerhetsstraff for uverifiserte data 🟢 `[EC3]`.
- **Metodisk forbehold mot Rank Reversal:**
  - Rank reversal (at rangeringen mellom to alternativer snur dersom et tredje alternativ legges til eller fjernes) er et kjent fenomen i ordningsbaserte MCDA-metoder som TOPSIS, COPRAS og VIKOR.
  - *Metodisk regel:* I teksten skal fare for rank reversal omtales som et **metodisk forbehold og en FoU-hypotese som skal undersøkes i pilotene**, ikke som et ferdig bevist faktum for VERIFIED.

---

### Seksjon 4: Finans- og reguleringskontekst
- **Empirisk forskning på Energi ↔ Misligholdsrisiko (PD):**
  - **Kaza et al. (2014):** *Cityscape* 16(1):279–298 🟢 `[Kaza2014]`. Undersøkte ~71 000 residensielle boliglån i USA og fant **~32 % lavere misligholdsrisiko (PD)** for private boliger med ENERGY STAR-sertifisering.
  - **Billio et al. (2022):** *JREFE* 65(3):419–450 (DOI 10.1007/s11146-021-09838-0) 🟢 `[Billio2022]`. Dokumenterte at høyere energikarakter (EPC) korrelerer signifikant med lavere sannsynlighet for mislighold på nederlandske boliglån.
  - **An & Pivo (2020):** *Real Estate Economics* 48(1):7–42 (DOI 10.1111/1540-6229.12228) 🟡 `[An2020]`. Fant **34 % lavere misligholdsrisiko** for kommersielle eiendommer med LEED/ENERGY STAR i CMBS-porteføljer i USA. *Må siteres utelukkende for kommersielle CMBS-lån, ikke residensielle boliglån.*
- **Bank- og finansiell regulering:**
  - **EBA EU (2023):** European Banking Authority *Report on Green Loans and Mortgages* (EBA/Op/2023/13) 🟢 `[EBA_EU2023]`. Foreslår frivillig EU-lånemerke og ESG-bankrapportering. *Må skilles konsekvent fra Entreprenørforeningen Bygg og Anlegg (`[EBA_NO2023]`).*
  - **Bank of England PS25/25 (des. 2025):** Erstatter SS3/19. Krever at banker og forsikringsselskaper bygger klimarisiko inn i kjernerammeverk og styrebeslutninger, med frist for ferdige vurderinger i **juni 2026** 🟡 `[BoE_PS25-25]`.
  - **Bank of England DP1/25 (juli 2025):** Discussion Paper om barrierer for mellomstore banker ved bygging av IRB-modeller for PD/LGD på boliglån 🟡 `[BoE_DP1-25]`. *Presisering: Gjelder IRB-modellering og databarrierer, ikke klima per se.*
- **Det eksplisitte FoU-hullet (FoU-høyden i finanssporet):**
  - Eksisterende litteratur dokumenterer at energieffektivitet (kWh/EPC) korrelerer med lavere misligholdsrisiko (PD) `[Billio2022]`, `[Kaza2014]`, `[An2020]`.
  - **Det finnes empiri om energi, men INGEN empirisk forskning kobler bygningskvalitet, holdbarhet (durability), fuktrobusthet eller vedlikeholdssvikt direkte til kredittrisiko, PD eller LGD.**
  - Dette er VERIFIEDs eksplisitte FoU-gap i finanssporet: å undersøke om teknisk kvalitet og levetid kan struktureres som relevant tilleggsinformasjon for bankens risikovurdering (FoU-spørsmål F5).

---

### Seksjon 5: Norsk SMB-kontekst og tilbudsbeslutninger
- **SMB-rammebetingelser i Norge og Norden:**
  - **Nordic Council of Ministers (2023):** *Building LCA and BIM practices in Norway* 🟢 `[Nordic2023]`. Bekrefter at LCA-reguleringer bevisst holdes lempeligere for SMB for å beskytte konkurransekraften (*«driven mainly by a fear of reducing the competitiveness for smaller actors who might not have resources to follow stringent regulations»*).
  - **BKA2 (2024–2028):** *Bærekraftige anskaffelser for de vanlige bygg- og anleggsprosjektene, fase 2*. Budsjett 11,7 MNOK. Prosjekteier Trondheim kommune; SINTEF v/ Vegard Knotten eier den faglige oppfølgingen 🟢 `[BKA2]`. Gir overføringsverdi for SMB uten overlapping med VERIFIED.
- **Kartlegging av eksisterende verktøy i markedet:**
  - **SmartKalk Miljø (EG Holte):** Tilbuds- og kalkulasjonsverktøy med integrert EPD-modul (beriket med NOBB- og GWP-data) 🟡 `[CL-SMB-001]`. Dokumenterer at norske SMB-verktøy *ikke* bare håndterer pris, men mangler uavhengig målt effekt på beslutninger.
  - **Reduzer:** Norsk anbuds- og klimaverktøy med 15 000+ EPD-er. Hovedfokus på CO₂/LCA i anbud.
  - **Concular (Tyskland):** Ombruksplattform med materialpass, sirkulær LCA og garanti/kvalitetsstempel for ombruksvarer.
  - **ORIS:** Plattform for infrastruktur/vei som krever manuell input for å sammenligne alternativer i tilbudsfasen.
- **Konklusjon om verktøybilde:** Enkeltdeler finnes (pris+klima i SmartKalk/Reduzer, ombruk i Concular, infrastruktur i ORIS), men ingen løsning samler hele flerkriteriebredden med synlig usikkerhet for norsk SMB i tilbudsfasen.

---

### Seksjon 6: Syntese og VERIFIEDs avgrensede FoU-gap (6-akser matrise)

VERIFIEDs nyhetsverdi måles mot **seks akser**:

1. **(a) Dataintegrasjon:** Kombinerer LCA + LCC + EPD/FDV + levetid + skaderisiko + ombruk (ikke bare én dimensjon).
2. **(b) Fase:** Brukes i **tilbudsfasen** (før pris og kontrakt låses), ikke bare etterprosjektering/sluttdokumentasjon.
3. **(c) Brukergruppe:** Utformet for **SMB-entreprenører og ikke-spesialister**, ikke bærekraftsanalytikere.
4. **(d) Forklarbarhet og usikkerhet:** Synliggjør datakilde, datakvalitet og usikkerhet for hvert datapunkt — ikke skjult i en totalscore.
5. **(e) Beslutningseffekt:** Måler og attribuerer om sammenligningen faktisk endret eller bekreftet valget.
6. **(f) Bredde i bærekraft (DNSH):** Premierer levetid, fuktrobusthet, vedlikehold og LCC (Do-No-Significant-Harm), ikke bare lavt start-CO₂.

#### Sammenstilt Funksjonsmatrise (6 Akser)

| Verktøy / Plattform | (a) Integrasjon | (b) Tilbudsfase | (c) SMB / Ikke-spes. | (d) Synlig usikkerhet | (e) Beslutningseffekt | (f) DNSH / Bredde |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **One Click LCA** | Delvis (LCA+LCC) | Delvis | ✗ (Spesialist) | ✗ (Totalscore) | ✗ | Delvis |
| **EC3** | ✗ (Kun CO₂) | Delvis | Delvis | **✓ (Konfidens)** | ✗ | ✗ |
| **SmartKalk Miljø** | Delvis (Pris+EPD) | **✓ (Kalkyle)** | **✓ (SMB)** | ✗ | ✗ | ✗ |
| **Reduzer** | ✗ (Kun CO₂) | **✓ (Anbud)** | **✓ (SMB)** | ✗ | ✗ | ✗ |
| **Concular** | Delvis (Ombruk) | Delvis | Delvis | ✗ | ✗ | Delvis |
| **ORIS** | Delvis (Infrastr.) | **✓ (Tilbud)** | Delvis | ✗ | ✗ | Delvis |
| **Madaster** | Delvis (Material) | ✗ (Slutt/FDV) | ✗ | ✗ | ✗ | Delvis |
| **Cobuilder** | Datalag (DPP) | Delvis | Delvis | ✗ | ✗ | Delvis |
| **VERIFIED (FoU-mål)** | **✓ (Full bredde)** | **✓ (Tilbud)** | **✓ (SMB)** | **✓ (Synlig DQI)** | **✓ (Måles)** | **✓ (DNSH/LCC)** |

**Syntesekonklusjon:** Alle enkeltbyggeklosser finnes eller er under utvikling i markedet. Det avgrensede FoU-gapet ligger i **syntesen og den empiriske testen av alle 6 akser samlet i en forklarbar, etterprøvbar modell for norsk SMB i tilbudsfasen**.

---

## 4. Kildekritisk og ontologisk verifikasjons-sjekkliste

Før ferdigstilling av `forskning-og-soa-v0.5-kandidat.md` må følgende verifiseres:

- [x] Bruk av «løsningsvalg» fremfor «produktvalg» gjennomgående.
- [x] Ingen påstand om at VERIFIED «velger» eller «anbefaler automatisk».
- [x] Ingen referanse til «svart boks».
- [x] «Testflate» benyttet for å omtale VIBS-plattformen.
- [x] Parkering av `[Wiik2025]` og `[SA2018]` med ⏸-status overholdt; `[EBA_NO2023]` og `[KD2024]` benyttet for 20 % utslippsreduksjon i tidligfase.
- [x] Konsekvent skille mellom `[EBA_EU2023]` (European Banking Authority) og `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg).
- [x] Ingen absolutte fraværspåstander («ingen verktøy finnes») utenfor det undersøkte utvalget.
