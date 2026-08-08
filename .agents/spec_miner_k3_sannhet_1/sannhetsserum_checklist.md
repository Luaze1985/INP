# Sannhetsserum & Terminology Specification Checklist for Chapter K3

**Target Chapter:** K3 (Mål og FoU-spørsmål / Research & R&D Height)  
**Project:** VIBS VERIFIED IPN Grant Application (NFR 2026)  
**Agent:** `spec_miner_k3_sannhet_1`  
**Date:** 2026-08-02  
**Status:** Authoritative Specification & Checkpoint Analysis  

---

## Executive Summary

This document establishes the authoritative Sannhetsserum (Truth Serum) checklist, terminology guidelines, and source hierarchy rules for **Chapter K3 (Mål og FoU-spørsmål)** of the VIBS VERIFIED IPN grant application.

Chapter K3 defines the primary objective, secondary objectives, and six central research questions (F1–F6) of the VERIFIED project. Under NFR IPN criteria, Chapter K3 is evaluated under the **Kvalitet (Quality)** criterion (~1.5–2 pages, score target ≥ 4.5/5.0).

To ensure zero risk of rejection during SINTEF review or NFR evaluation, every claim, question, and framing in Chapter K3 must rigorously comply with the **31 Sannhetsserum Checkpoints** extracted from `sannhetsserum-oppdatering-v0.5.md`, `vibs-verified-ord-og-kildekart-v0.5.yml`, `sannhetsserum-soknadstekst-v0.4.md`, and `AGENTS.md`.

---

## 1. Core Terminology & Ontological Rules for Chapter K3

| Term / Phrase | Status | Rule & Context in Chapter K3 | Approved Replacement / Format |
|---|---|---|---|
| **løsningsvalg** | 🟢 Mandatory | Use whenever referring to the total solution choice in the tender phase (product, assembly, maintenance, service life, LCC). | "løsningsvalg" |
| **produktvalg** | 🔴 Forbidden | Too narrow. Must NEVER be used when referring to the holistic tender evaluation. | Replace with "løsningsvalg" |
| **beslutningsstøtte** | 🟢 Mandatory | Describes VERIFIED as an explainable decision support system showing options, trade-offs, and data quality. | "beslutningsstøtte", "sammenligningsverktøy" |
| **VERIFIED velger / anbefaler automatisk** | 🔴 Forbidden | Implies automated selection or recommendation without human oversight. | "VERIFIED viser, sammenligner og forklarer" |
| **svart boks** | 🔴 Forbidden | Implies hidden algorithms or opaque scores. | "sammenligning med synlig datagrunnlag og usikkerhet" |
| **testflate** | 🟢 Mandatory | Defines the existing VIBS platform's role. VIBS is the commercial/operational testbed; VERIFIED is the R&D research layer. | "VIBS-plattformen som testflate" |
| **integrasjonsflate** | 🔴 Forbidden | Premature; implies pre-existing architecture interfaces before R&D phase. | Replace with "testflate" |
| **[EBA_NO2023]** | 🟢 Mandatory | Entreprenørforeningen Bygg og Anlegg Norge (*Veileder for klimagassreduksjoner – boligblokker*). Construction/climate source. | `[EBA_NO2023]` (EBA Norge) |
| **[EBA_EU2023]** | 🟢 Mandatory | European Banking Authority (Voluntary EU Green Loan / Mortgage label). Financial source. | `[EBA_EU2023]` (European Banking Authority) |
| **EBA (unqualified)** | 🔴 Forbidden | Ambiguous abbreviation. Must ALWAYS be written out on first mention to distinguish EBA Norge from EBA EU. | Write out fully on first mention |
| **mulighetsrom** | 🟢 Mandatory | Climate impact framing. Climate reduction must be described as an exploratory potential to be tested, NOT a guaranteed result. | "mulighetsrom for utslippskutt som skal undersøkes" |
| **VERIFIED reduserer CO₂ / feil** | 🔴 Forbidden | Claims verified causal effect prior to R&D execution. | "prosjektet skal undersøke/teste om VERIFIED gir..." |
| **[Wiik2025] som bærende kilde** | ⏸ Parked / 🔴 | Consortium internal note. Parked since 2026-06-28. MUST NOT bear application claims alone. | Use `[EBA_NO2023]`, `[KD2024]`, `[Multiconsult2023DiBK]` |
| **[SA2018] som bærende kilde** | ⏸ Parked / 🔴 | Unverified primary source. Parked since 2026-06-28. MUST NOT bear application claims alone. | Parked until primary source is opened/located |

---

## 2. Source Hierarchy & Citation Rules for Chapter K3

Per user instructions (2026-08-02T21:22:35Z), Norwegian independent research and authority sources constitute the **PRIMARY FOUNDATION** for Chapter K3. European and international sources follow as **SECONDARY CONTEXT**.

```
+-----------------------------------------------------------------------------------+
| TIER 1: PRIMARY NORWEGIAN RESEARCH & AUTHORITY SOURCES (Bærende Belegg)           |
| GullbrekkenHolme2025 | Ingvaldsen2008 | Bjørheim2026 | KD2024 | Multiconsult2023DiBK |
| EBA_NO2023 | BKA2 (SINTEF/Knotten) | FinansNorge2024VASK                           |
+-----------------------------------------------------------------------------------+
                                        |
                                        v
+-----------------------------------------------------------------------------------+
| TIER 2: SECONDARY INTERNATIONAL RESEARCH & REGULATORY CONTEXT                      |
| Edelen2018 | Weidema1996 | Mecca2023 | Benke2025 | Lohman2023 | Billio2022          |
| Kaza2014 | An2020 (🟡) | Ciroth2016 | EBA_EU2023 | BoE_PS25-25                      |
+-----------------------------------------------------------------------------------+
                                        |
                                        v
+-----------------------------------------------------------------------------------+
| TIER 3: PARKED CONSORTIUM NOTES & UNVERIFIED SOURCES (⏸ Må ikke stå alene)       |
| Wiik2025 (⏸) | SA2018 (⏸)                                                         |
+-----------------------------------------------------------------------------------+
```

### Detailed Source Status Matrix for K3

| Key | Author / Institution | Year | Domain | Status | Citation Role in Chapter K3 |
|---|---|---|---|---|---|
| `[GullbrekkenHolme2025]` | Gullbrekken & Holme (SINTEF) | 2025 | Building defects | 🟡 (SINTEF fulltext) | **Primary Norwegian:** 10–30 mrd NOK/yr building damage, 1 defect in 50% of homes. Anchors F1. |
| `[Ingvaldsen2008]` | Ingvaldsen (Byggforsk) | 2008 | Building defects & lifetime | 🟡 | **Primary Norwegian:** Building defect causes, service life, damage risk over time. Anchors F1. |
| `[Bjørheim2026]` | Bjørheim et al. (SINTEF) | 2026 | Circularity & reuse | 🟡 | **Primary Norwegian:** Documentation of circular building materials & reuse documentation. Anchors F3. |
| `[KD2024]` | KD / DiBK | 2024 | Climate footprint | 🟡 | **Primary Norwegian:** *Byggenæringens klimafotavtrykk* (63% A1–A3, early-phase impact space). Anchors F2/F3. |
| `[Multiconsult2023DiBK]`| Multiconsult for DiBK | 2023 | LCA / Materials | 🟢 | **Primary Norwegian:** 70% A1–A3 emissions in 4 reference buildings. Anchors F1/F2. |
| `[EBA_NO2023]` | EBA Norge et al. | 2023 | Climate guide (bygg) | 🟡 | **Primary Norwegian:** 20% emission kutt from material choice without cost increase. Anchors F1/F3. |
| `[BKA2]` | Vegard Knotten (SINTEF) | 2024–28| Sustainable procurement| 🟢 | **Primary Norwegian:** 11.7 MNOK project on sustainable procurement in ordinary BA projects. Anchors F4. |
| `[FinansNorge2024VASK]` | Finans Norge | 2024 | Water damage statistics | 🟢 | **Primary Norwegian:** 5.1 mrd NOK water damage in 2023. Anchors F1 risk cost. |
| `[Edelen2018]` | Edelen & Ingwersen | 2018 | LCA / DQI | 🟢 | International context: Purpose-dependent Data Quality Indicators (DQI). Anchors F1/F2. |
| `[Weidema1996]` | Weidema & Wesnæs | 1996 | LCA / Pedigree | 🟡 | International context: Pedigree matrix for data quality representation. Anchors F1/F2. |
| `[Mecca2023]` | Mecca et al. | 2023 | MCDA review | 🟡 (SINTEF fulltext) | International context: Multi-criteria decision analysis review in construction. Anchors F1/F4. |
| `[Benke2025]` | Benke et al. | 2025 | LCA variation | 🟢 | International context: LCA variation & data uncertainty. Anchors F2. |
| `[Lohman2023]` | Lohman et al. | 2023 | Uncertainty display | 🟢 | International context: User visual representation of uncertainty. Anchors F4. |
| `[Billio2022]` | Billio et al. | 2022 | Green mortgages | 🟢 | International context: Dutch residential mortgage & energy efficiency empirical study. Anchors F5. |
| `[Kaza2014]` | Kaza et al. | 2014 | Green building default | 🟢 | International context: ~32% lower default rate in ENERGY STAR homes. Anchors F5. |
| `[An2020]` | An & Pivo | 2020 | Commercial CMBS | 🟡 | International context: 34% CMBS commercial buildings (note: NOT residential). Anchors F5. |
| `[Ciroth2016]` | Ciroth et al. | 2016 | Empirical pedigree | 🟡 | International context: Empirical pedigree matrix validation. Anchors F1/F2. |
| `[EBA_EU2023]` | European Banking Authority | 2023 | EU Green Finance | 🟢 | International context: Voluntary EU Green Mortgage / Loan framework. Anchors F5. |
| `[BoE_PS25-25]` | Bank of England | 2026 | Climate risk supervision | 🟡 | International context: Climate physical/transition risk supervision (PS25/25). Anchors F5. |
| `[Wiik2025]` | Wiik (SINTEF) | 2025 | Consortium internal | ⏸ | **Parked:** Internal note (Notat 57). Cannot be used as independent source. |
| `[SA2018]` | Unknown | 2018 | Unverified | ⏸ | **Parked:** Unverified primary source. Cannot be used in candidate/canonical text. |

---

## 3. The 31 Sannhetsserum Checkpoints for Chapter K3

```
## Features Discovered
| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Terminology | CP-01 Løsningsvalg | Require 'løsningsvalg' over 'produktvalg' | Draft text | Validated K3 text | Reject 'produktvalg' when scope exceeds single product | v0.5 update §1, ordkart v0.5 |
| 2 | Terminology | CP-02 Beslutningsstøtte | Frame VERIFIED as decision support, avoid auto-choice | Draft text | Validated K3 text | Reject 'velger automatisk', 'anbefaler' | v0.5 update §2, ordkart v0.5 |
| 3 | Terminology | CP-03 Forklarbarhet | Require visible weighting, data basis & uncertainty | Draft text | Validated K3 text | Reject 'svart boks' or hidden scores | v0.5 update §2, §20 |
| 4 | Terminology | CP-04 Testflate | Use 'testflate' for VIBS platform layer | Draft text | Validated K3 text | Reject 'integrasjonsflate' or blurring plattform/R&D | v0.5 update §6, ordkart v0.5 |
| 5 | Terminology | CP-05 EBA Separation | Strictly separate EBA_EU2023 and EBA_NO2023 | Citation keys | Validated K3 keys | Reject merged 'EBA' key | v0.5 update §30, ordkart v0.5 |
| 6 | Source Hierarchy | CP-06 Independent Sources | Only independent research/authority carries claims | Claims & citations | Verified source status | Flag claims backed only by internal notes | AGENTS.md rule 1-4 |
| 7 | Source Hierarchy | CP-07 Norwegian Primary | Prioritize Norwegian research over international | K3 reference list | Hierarchy-compliant K3 | Reject international-first structure | User instruction 2026-08-02 |
| 8 | Source Hierarchy | CP-08 Parked Sources | Keep Wiik2025 and SA2018 parked (⏸) | Citation keys | Status ⏸ enforcement | Reject Wiik2025/SA2018 as standalone proof | Kildedom 2026-06-27, ordkart v0.5 |
| 9 | Evidence Separation| CP-09 Evidence Separation | Separate measured pilot results from future effects | Claims & goals | Separated evidence | Reject treating future hypotheses as proven facts | v0.5 update §25 |
| 10 | Climate Framing | CP-10 Climate Mulighetsrom | Frame climate reduction as opportunity/range to test | Climate impact text | Exploratory framing | Reject guaranteed CO2 savings claims | v0.5 update §26 |
| 11 | Risk Non-Masking | CP-11 Technical Gate | Technical suitability must gate before comparison | Risk & score logic | Technical-first gate | Reject masking moisture/durability behind low CO2 | v0.5 update §20, §28 |
| 12 | Datastatus | CP-12 Datastatus Taxonomy | Classify data as missing, generic, estimated, verif. | Data points | Explicit datastatus | Reject unclassified data precision | v0.5 update §19 |
| 13 | Multi-Criteria | CP-13 MCDA Weighting | Require explicit MCDA method testing & sensitivity | F1/F4 methodology | Transparent MCDA | Reject pre-determined unvalidated weighting | v0.5 update §21 |
| 14 | Pre-Funding Boundary| CP-14 Pre-Grant Boundary | Limit pre-funding work to analysis, concept, proposal| K3 timeline/scope | Scope-restricted K3 | Reject claiming R&D activities started pre-grant | v0.5 update §17 |
| 15 | Methodology | CP-15 Iterative Research | Structure FoU as iterative loop: develop->pilot->measure| R&D methodology | Iterative loop text | Reject static linear software release framing | v0.5 update §18 |
| 16 | User Roles | CP-16 Contractor Responsibility| Contractor holds professional responsibility for tender | User roles text | Role-aligned K3 | Reject placing decision authority on software | v0.5 update §3, §12 |
| 17 | FoU Question F1 | CP-17 F1 Quality vs LCC | F1 must link service life/quality to LCC & risk | F1 formulation | Source-anchored F1 | Reject F1 lacking Norwegian damage research base | v0.5 update §7, K3 godkjent v0.1 |
| 18 | FoU Question F2 | CP-18 F2 Early Tender Data | F2 must test NOBB/GTIN/EPD/FDV integration pre-tender| F2 formulation | Standard-anchored F2| Reject F2 claiming full pre-tender automation | v0.5 update §7, K3 godkjent v0.1 |
| 19 | FoU Question F3 | CP-19 F3 Circularity & Repair| F3 must evaluate reuse/repair vs new procurement | F3 formulation | SDG 12.2/12.5 F3 | Reject F3 focusing solely on new product choice | v0.5 update §7, §24 |
| 20 | FoU Question F4 | CP-20 F4 SME Understanding | F4 must test SME usability & measured decision effect| F4 formulation | Gap-anchored F4 | Reject F4 assuming proven SME adoption | v0.5 update §7, §13 |
| 21 | FoU Question F5 | CP-21 F5 Building Data to Bank| F5 must frame bank relevance as optional extra data | F5 formulation | Bounded F5 | Reject F5 as primary track or credit automation | v0.5 update §7, §30 |
| 22 | FoU Question F6 | CP-22 F6 Traceability/Scale| F6 must test data flow traceability & cross-cat. scale| F6 formulation | Standards-anchored F6| Reject F6 without explicit transferability test | v0.5 update §7, §13 |
| 23 | Ethics & Privacy | CP-23 Ethics & Minimization| Incorporate data minimization & anonymization | Ethics section | Ethically compliant K3| Reject missing data governance rules | v0.5 update §23 |
| 24 | Sustainability | CP-24 SDG 12.2 / 12.5 Focus| Concentrate sustainability on SDG 12.2 and 12.5 | Sustainability text | Focused SDG narrative| Reject laundry-list SDG broad claims | v0.5 update §24, bærekraftserum |
| 25 | Do-No-Harm | CP-25 DNSH Rules | Operationalize DNSH into concrete model rules | DNSH checks | DNSH-rule embedded K3| Reject relying on generic caution | v0.5 update §27 |
| 26 | Scope Boundary | CP-26 Bank Track Scope | Bound bank track to secondary effect of building data| Bank track text | Bounded bank narrative| Reject bank track taking over main R&D focus | v0.5 update §30 |
| 27 | Privacy Boundary | CP-27 No Credit Profiling | Explicitly exclude personal profiling & auto-credit | Financial scope | Excluded profiling text| Reject credit scoring or personal profiling | v0.5 update §31 |
| 28 | MCDA Robustness | CP-28 MCDA Rank Reversal | Require testing against rank reversal in MCDA | MCDA formulation | Methodically cautious | Reject claiming MCDA is proven without testing | SoA v0.5 kandidat §3 |
| 29 | Data Uncertainty | CP-29 DQI/Pedigree Visib. | Use Edelen DQI & Weidema Pedigree for data quality | Datastatus logic | DQI/Pedigree framework| Reject hiding data uncertainty in totals | SoA v0.5 kandidat §2 |
| 30 | Claim Scope | CP-30 Avoid Absolute Gaps | Do not claim absolute market absence without sample | SoA gap text | Sample-bounded gaps | Reject "no tools exist anywhere" claims | SoA v0.5 kandidat R3 |
| 31 | KPI Measurement | CP-31 Observable Points | Define observable experimental measurement points | F1-F6 measurement | KPI-mapped F1-F6 | Reject subjective or unobservable metrics | v0.5 update §22 |
```

---

## 4. Deep-Dive: Verification of the 31 Checkpoints for Chapter K3

### CP-01: Terminology — Løsningsvalg vs Produktvalg
- **Principle:** Chapter K3 must consistently use «løsningsvalg» when discussing choices in the tender phase. A solution choice encompasses products, assembly methods, maintenance requirements, and expected service life.
- **K3 Requirement:** In `K3-P1-S1`, `K3-P1-S2`, and `K3-P2-S2`, replace any instance of "produktvalg" or "materialvalg" with "løsningsvalg" when the scope includes execution and lifespan.
- **Verification Rule:** `grep_search` for "produktvalg" in `k3-forskning.md` must return 0 occurrences in context of holistic decision-making.

### CP-02: Terminology — Decision Support vs Automated Selection
- **Principle:** VERIFIED is an explainable decision support framework («beslutningsstøtte»). It MUST NOT be described as an automated decision-maker, recommendation engine, or automatic selector.
- **K3 Requirement:** Formulate `K3-P1-S1` and `K3-P2-S2` explicitly: "Modellen sammenligner, viser forskjeller og usikkerhet, men tar ikke beslutningen. Entreprenøren beholder det faglige ansvaret for tilbudet."
- **Forbidden Terms:** "VERIFIED velger automatisk", "anbefaler optimalt produkt", "automatisert beslutningsmotor".

### CP-03: Terminology — Explainability vs Black Box
- **Principle:** The core scientific novelty of VERIFIED lies in transparent weighting, visible data origin, and explicit representation of data uncertainty, avoiding "black box" scoring.
- **K3 Requirement:** `K3-P2-S1` & `K3-P2-S2` must emphasize: "FoU-bidraget ligger i å undersøke hvordan vekting, datakvalitet og usikkerhet kan dokumenteres og forklares uten falsk presisjon."

### CP-04: Terminology — VIBS Platform vs VERIFIED R&D Layer (Testflate)
- **Principle:** Explicitly distinguish the commercial VIBS platform from the VERIFIED research layer. VIBS is the *testbed* («testflate»); VERIFIED is the *R&D model layer*.
- **K3 Requirement:** `K3-P4-S3` must state: "VIBS-plattformen benyttes som testflate for prosjektet, men selve forskningsarbeidet utgjøres av VERIFIED-laget: datamodellering, usikkerhetsrepresentasjon, vektingslogikk og måling av beslutningseffekt."

### CP-05: Terminology — Strict Separation of EBA Sources
- **Principle:** `[EBA_EU2023]` (European Banking Authority - financial) and `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg Norge - construction) must never be merged under an ambiguous "EBA" tag.
- **K3 Requirement:** When citing construction climate guidelines in F1/F3, use `[EBA_NO2023]`. When citing green mortgage frameworks in F5, use `[EBA_EU2023]`. Always write out the full name on first mention.

### CP-06: Source Hierarchy — Primary Independent Research as Sole Proof
- **Principle:** Only independent peer-reviewed research or official government reports (🟢 or 🟡 with reservations) can bear claims alone.
- **K3 Requirement:** Every factual assertion in K3 (e.g. building defect costs, A1–A3 emission shares, water damage figures) must be anchored in independent sources.

### CP-07: Source Hierarchy — Primacy of Norwegian Research & Authority Sources
- **Principle:** Per user directive (2026-08-02T21:22:35Z), Norwegian sources form the **primary foundation** in Chapter K3. International research provides supplementary context.
- **K3 Requirement:** Section structure and source citations for F1–F6 in K3 must present Norwegian evidence first (`[GullbrekkenHolme2025]`, `[Ingvaldsen2008]`, `[Bjørheim2026]`, `[KD2024]`, `[Multiconsult2023DiBK]`, `[EBA_NO2023]`, `[BKA2]`, `[FinansNorge2024VASK]`), followed by international literature (`[Edelen2018]`, `[Weidema1996]`, `[Mecca2023]`, `[Billio2022]`, `[Kaza2014]`).

### CP-08: Source Hierarchy — Parked Consortium Notes (Wiik2025, SA2018)
- **Principle:** `[Wiik2025]` (SINTEF internal note 57) and `[SA2018]` (unverified source) are parked (⏸) as of 2026-06-28.
- **K3 Requirement:** Neither `[Wiik2025]` nor `[SA2018]` may be used as independent evidence in Chapter K3. Claims previously supported by Wiik2025 (e.g., 20% emission kutt) MUST be re-anchored in `[EBA_NO2023]` or `[KD2024]`.

### CP-09: Separation of Evidence — Measured Pilot Results vs Future Hypotheses
- **Principle:** Chapter K3 must explicitly separate established baseline facts, experimental pilot measurements, and calculated future effects.
- **K3 Requirement:** Frame F1–F6 outcomes using hypothesis language: "Prosjektet skal undersøke om..." and "Effekten måles i pilotering mot baseline...". Never present expected long-term benefits as pre-existing achievements.

### CP-10: Climate Effect Framing — Exploratory Opportunity (Mulighetsrom)
- **Principle:** Climate impact is framed as an exploratory potential to be tested during the R&D project, NOT a guaranteed delivery of the software.
- **K3 Requirement:** Anchor climate discussions in `[KD2024]` and `[EBA_NO2023]` as a "mulighetsrom i tidligfase", and state that VERIFIED will test whether access to structured data enables SMEs to realize this potential.

### CP-11: Risk Non-Masking — Mandatory Technical Gate
- **Principle:** Technical suitability («teknisk egnethet»), durability, moisture robustness, and documentation quality must NEVER be hidden or compensated for by a low CO₂ or low price score.
- **K3 Requirement:** `K3-P1-S2` and `K3-F1` must state: "Teknisk egnethet og fuktrobusthet utgjør en obligatorisk faglig port. Løsningsalternativer som ikke tilfredsstiller tekniske minstekrav eller dokumentasjonskrav filtreres ut før flerkriteriesammenligning utføres."

### CP-12: Datastatus Classification Taxonomy
- **Principle:** Data input to the model must be classified into explicit quality levels to eliminate false precision.
- **K3 Requirement:** Explicitly list the four datastatus levels in K3: (1) Manglende data, (2) Generiske data, (3) Estimerte data, and (4) Verifiserte data.

### CP-13: Multi-Criteria Weighting & Sensitivity Analysis
- **Principle:** The multi-criteria decision analysis (MCDA) method must be tested for weight sensitivity and rank reversal without assuming a pre-determined fixed formula.
- **K3 Requirement:** `K3-P2-S2` must specify that weight sensitivity testing and robustness against rank reversal (ref `[Mecca2023]`) form a core R&D task in VERIFIED.

### CP-14: Pre-Funding Scope Boundary
- **Principle:** Activities conducted prior to grant award are strictly limited to problem analysis, literature review, concept formulation, and proposal writing.
- **K3 Requirement:** `K3-P4-S1` & `K3-P4-S2` must state: "Arbeid før tildeling er avgrenset til problemanalyse, kildesjekk og søknadsforberedelse. De faktiske FoU-aktivitetene starter først etter eventuell innvilgelse."

### CP-15: Iterative Research & Development Loop
- **Principle:** VERIFIED's research methodology is an iterative R&D cycle, not a standard linear software deployment.
- **K3 Requirement:** Describe K3's operational model as an iterative loop: (1) Data modeling & DQI formulation -> (2) Multi-criteria algorithm design -> (3) Pilot testing in SME projects -> (4) Decision effect measurement -> (5) Model refinement.

### CP-16: Professional Responsibilities & User Roles
- **Principle:** The contractor («entreprenøren») retains full professional responsibility for tenders and technical execution; the customer («byggherre/forbruker») participates in informed trade-off choices.
- **K3 Requirement:** State in K3 that VERIFIED empowers non-specialist contractors and customers to evaluate trade-offs together, without transferring professional liability to the tool.

### CP-17: FoU Question F1 — Quality & Service Life vs Economy (LCC)
- **Question Text:** *Hvordan kan dokumentasjon av levetid, vedlikehold og kvalitet omsettes til sammenlignbare livsløpskostnader (LCC) og inngå i avveiingen mellom økonomi, klima og teknisk kvalitet?*
- **Primary Norwegian Foundation:** Anchor damage and defect costs in `[GullbrekkenHolme2025]` (10–30 mrd NOK/yr SINTEF), `[Ingvaldsen2008]` (Byggforsk damage statistics), and `[FinansNorge2024VASK]` (5.1 mrd NOK water damage).
- **Secondary Context:** `[Billio2022]` (LCC & financial risk), `[Edelen2018]` (DQI).
- **Observable Measurement Point:** Measured delta in LCC calculations between generic service life estimates vs verified supplier maintenance/durability data in pilot tenders.

### CP-18: FoU Question F2 — Early-Phase Tender Data Integration
- **Question Text:** *Kan NOBB, GTIN, EPD, FDV og prisdata kobles slik at de kan brukes før tilbudet sendes?*
- **Primary Norwegian Foundation:** Anchor early-phase decision impact in `[KD2024]` (DiBK/KD kunnskapsgrunnlag: 63% A1–A3 emissions, early-phase impact room), `[Multiconsult2023DiBK]` (70% A1–A3), and `[BKA2]`.
- **Secondary Context:** `[Benke2025]` (LCA variation), `[Edelen2018]`, `[Ciroth2016]`.
- **Observable Measurement Point:** Time required to assemble structured product data (NOBB/EPD/FDV) per tender line item before vs after VERIFIED integration.

### CP-19: FoU Question F3 — Circularity, Reuse, Repair & Rehabilitation
- **Question Text:** *Hvordan kan modellen synliggjøre avveininger mellom ombruk, reparasjon, vedlikehold, rehabilitering og nyanskaffelse under ulike forutsetninger for kostnad, klima, levetid og dokumentasjonskvalitet?*
- **Primary Norwegian Foundation:** Anchor circular material documentation in `[Bjørheim2026]` (SINTEF circular materials) and `[KD2024]`. Align with NFR 2026 40 MNOK sirkulærøkonomi priority & SDG 12.2 / 12.5.
- **Secondary Context:** `[CPR2024]`, `[ESPR2024]`.
- **Observable Measurement Point:** Proportion of pilot decision scenarios where maintenance, repair, or reused components are chosen over new procurement when documentation is made visible.

### CP-20: FoU Question F4 — SME Understanding & Decision Effect
- **Question Text:** *Hvordan forstår og bruker SMB-entreprenører og kunder beslutningsgrunnlaget, og i hvilken grad endrer eller bekrefter det valget de tar?*
- **Primary Norwegian Foundation:** Anchor SME competitive challenges in `[Nordic2023]` (Nordic Council report on SME regulatory burdens) and `[BKA2]` (SINTEF/Knotten sustainable procurement). Treat SME decision behavior as an explicit R&D gap.
- **Secondary Context:** `[Lohman2023]` (uncertainty visual representation), `[Mecca2023]`.
- **Observable Measurement Point:** User comprehension score (0–10 scale), decision confidence, and frequency of solution change in pilot tender tests.

### CP-21: FoU Question F5 — Building Data for Bank / Green Finance
- **Question Text:** *Hvordan kan dokumentasjon av byggteknisk kvalitet, levetid og vedlikeholdsbehov struktureres som relevant tilleggsinformasjon for bankens vurdering, uten personprofilering eller automatisk kredittbeslutning?*
- **Primary Norwegian Foundation:** Anchor bank track as a secondary potential effect using `[EBA_NO2023]` for building documentation.
- **Secondary Context:** `[EBA_EU2023]` (EBA EU Green Mortgage framework), `[Billio2022]`, `[Kaza2014]` (~32% ENERGY STAR lower default), `[An2020]` (34% CMBS commercial), `[BoE_PS25-25]`.
- **Observable Measurement Point:** Bank evaluator feedback on structured building quality data completeness in sample mortgage/loan risk reviews.

### CP-22: FoU Question F6 — Traceability & Scalability across Categories
- **Question Text:** *Hvordan kan dataflyt, dokumentasjon og nødvendige grensesnitt utformes og testes slik at modellen er etterprøvbar og kan overføres til en ny produktkategori?*
- **Primary Norwegian Foundation:** Standardized Norwegian product catalog data (NOBB/Byggtjeneste) and DiBK requirements.
- **Secondary Context:** `[CPR2024]` (EU Construction Products Regulation), `[ESPR2024]` (Digital Product Passport).
- **Observable Measurement Point:** Reusability score of data schema and API interfaces when expanding from initial pilot category (e.g. roofing/cladding) to a second category (e.g. windows/insulation).

### CP-23: Research Ethics, Data Minimization & Privacy
- **Principle:** Research involving SME contractors and house owners must follow strict data minimization, informed consent, and anonymization protocols.
- **K3 Requirement:** Explicitly state in K3 that pilot testing collects only anonymized project and tender metrics, excluding personal contractor or customer identifiers.

### CP-24: Sustainability Focus on SDG 12.2 and 12.5
- **Principle:** Avoid listing numerous SDGs. Focus tightly on **SDG 12.2** (sustainable management and efficient use of natural resources) and **SDG 12.5** (waste reduction through prevention, reduction, recycling, and reuse).
- **K3 Requirement:** Frame VERIFIED's sustainability contribution around resource efficiency, extended service life, and circular decision choices in early tender phases.

### CP-25: Do-No-Harm (DNSH) Operational Rules
- **Principle:** Do-no-harm must be operationalized into active model rules rather than passive statements.
- **K3 Requirement:** Specify in K3 that VERIFIED enforces DNSH rules in code: low carbon scores cannot override poor durability, moisture vulnerability, or missing safety documentation.

### CP-26: Bank Track Scope Bounding
- **Principle:** The bank/finance track is a secondary potential application of structured building data, NOT the main R&D focus of VERIFIED.
- **K3 Requirement:** Ensure F5 is framed as an exploratory secondary effect. The primary R&D focus remains decision support for SME contractors and clients in the tender phase.

### CP-27: Exclusion of Personal Profiling & Automated Credit Decisions
- **Principle:** VERIFIED strictly excludes personal credit scoring, borrower profiling, or automated loan underwriting.
- **K3 Requirement:** `K3-F5` must explicitly state: "...uten personprofilering eller automatisk kredittbeslutning."

### CP-28: Multi-Criteria Method Justification & Rank Reversal
- **Principle:** Multi-criteria analysis methods (e.g. TOPSIS, COPRAS, VIKOR) can suffer from rank reversal when alternatives are added or removed.
- **K3 Requirement:** State in K3 that VERIFIED will test and evaluate MCDA methods for mathematical stability against rank reversal (citing `[Mecca2023]`), rather than assuming a pre-validated algorithm.

### CP-29: Data Quality Indicators (DQI) & Pedigree Matrix Representation
- **Principle:** Incorporate purpose-dependent DQI (`[Edelen2018]`) and Pedigree matrices (`[Weidema1996]`, `[Ciroth2016]`) to represent data uncertainty visibly.
- **K3 Requirement:** Reference DQI and Pedigree matrix principles as the methodological foundation for displaying data uncertainty in VERIFIED.

### CP-30: Absence Claims Limitation (No Unsubstantiated Absolute Gaps)
- **Principle:** Never assert absolute negative claims (e.g. "no existing tool can do X") as proven fact beyond the investigated sample.
- **K3 Requirement:** Phrase State-of-the-Art gaps cautiously: "I det undersøkte utvalget av verktøy finnes det ikke en ferdig integrert løsning som dekker kombinasjonen av..."

### CP-31: Observable Experimental Measurement Points (KPIs)
- **Principle:** Each of the six research questions F1–F6 must be linked to observable, empirical measurement points during pilot testing.
- **K3 Requirement:** Map every FoU question (F1–F6) to concrete pilot KPIs (time, data completeness, decision change frequency, LCC accuracy, schema reusability).

---

## 5. Edge Cases & Observed Behaviors in Chapter K3 Mining

```
## Edge Cases
| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | EBA Citation | Text citing 'EBA 2023' without modifier | Ambiguity between EBA EU (banking) and EBA Norge (construction). MUST split into [EBA_EU2023] or [EBA_NO2023]. |
| 2 | Wiik2025 Citation | Claiming 20% CO2 reduction citing [Wiik2025] | Wiik2025 is parked (⏸). Must re-anchor claim in [EBA_NO2023] or [KD2024]. |
| 3 | Product vs Solution | Writing 'produktvalg' in K3-P1-S1 | Violates ontological rule. Scope includes assembly and service life; must use 'løsningsvalg'. |
| 4 | Bank Track Scope | Framing F5 as primary R&D objective | Violates scope boundary. Bank track is secondary effect; primary focus is SME tender decision support. |
| 5 | Climate Guarantee | Writing 'VERIFIED gir 20% utslippskutt' | Violates evidence separation. Must write 'mulighetsrom som skal undersøkes og måles i pilot'. |
| 6 | Technical Risk Masking | Option with low CO2 but high moisture risk scoring high | Violates CP-11. Technical suitability must act as initial mandatory gate before MCDA scoring. |
| 7 | Source Priority Order | Listing international sources (Edelen, Billio) before Norwegian sources | Violates user priority instruction. Norwegian research (Gullbrekken, KD, Multiconsult) MUST come first. |
```

---

## 6. Actionable Wording Checklist for Chapter K3 Drafters

Before finalizing the text for Chapter K3 (`docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md` or canonical `k3-forskning.md`), verify the following 10 mandatory checks:

- [ ] **Check 1:** Is «løsningsvalg» used consistently throughout? (No forbidden «produktvalg»).
- [ ] **Check 2:** Is VERIFIED described as explainable «beslutningsstøtte»? (No «velger automatisk» or «svart boks»).
- [ ] **Check 3:** Is VIBS defined as the «testflate» and VERIFIED as the R&D model layer?
- [ ] **Check 4:** Are `[EBA_NO2023]` and `[EBA_EU2023]` strictly separated and fully written out on first mention?
- [ ] **Check 5:** Are Norwegian research & authority sources (`[GullbrekkenHolme2025]`, `[Ingvaldsen2008]`, `[Bjørheim2026]`, `[KD2024]`, `[Multiconsult2023DiBK]`, `[EBA_NO2023]`, `[BKA2]`, `[FinansNorge2024VASK]`) placed FIRST as the primary foundation for F1–F6?
- [ ] **Check 6:** Are parked sources (`[Wiik2025]`, `[SA2018]`) kept in ⏸ status and NOT used as standalone claims?
- [ ] **Check 7:** Is climate impact framed as an exploratory «mulighetsrom» to be tested, rather than a guaranteed software feature?
- [ ] **Check 8:** Is technical suitability («teknisk egnethet») established as a mandatory gate prior to multi-criteria evaluation?
- [ ] **Check 9:** Are all 6 FoU questions (F1–F6) linked to concrete, observable pilot measurement points?
- [ ] **Check 10:** Is `K3-F5` (bank track) explicitly bounded to secondary building documentation without personal profiling or automated credit scoring?

---
*End of Sannhetsserum & Terminology Specification Checklist for Chapter K3.*
