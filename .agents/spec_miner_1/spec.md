# Authoritative Specification Mining Report — VERIFIED IPN (SoA v0.5)

**Document Version:** 1.0  
**Date:** 2026-08-02  
**Author:** Spec Miner 1  
**Working Directory:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\spec_miner_1`  
**Target Context:** SINTEF State of the Art Evaluation & IPN Grant Application (NFR 2026)

---

## Executive Summary

This document presents the authoritative specification mining for the **VERIFIED IPN Research Project (State of the Art v0.5)**. It extracts and formalizes requirements, methodological standards, regulatory frameworks, financial risk literature, competitive tool capabilities, ontology rules, and boundary conditions from primary project sources:
- Canonical Kildedom (`docs/reference/vibs-verified-kildedom-2026-06-27.md`)
- Source Library (`docs/reference/ipn-kildebibliotek.md`)
- Ontological Control Map (`docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`)
- Evidence Matrix (`research/evidence_matrix.md`)
- State of the Art Working Draft (`docs/reference/state-of-the-art-verified-ipn.md`)

---

## 1. Methodological Foundation Specifications

### 1.1 70% A1–A3 Rule (Cradle-to-Gate Dominance)
- **Source:** Multiconsult / DiBK (2024), KD2024 (`[KD2024]`).
- **Specification:** Across 4 reference building types analyzed, material emissions in modules A1–A3 (cradle-to-gate raw material extraction, transport, and manufacturing) account for **63% to 70%** (rounded to 70%) of total material lifecycle greenhouse gas emissions.
- **System Impact:** Decision support in early tender phases must prioritize material choices and supplier selection in A1–A3, where emission reduction potential is highest before design freeze.

### 1.2 TEK17 1.25 Safety Factor for Generic Data
- **Source:** TEK17 § 9-2 / DiBK guidance / NS 3720.
- **Specification:** When specific verified Product EPDs are missing and generic LCA data is utilized, Norwegian regulations and standards enforce a **1.25 safety factor (25% emission penalty markup)**.
- **System Impact:** The test surface must explicitly flag when generic data is used, applying the 1.25 penalty markup transparently, thereby incentivizing contractors to select products with verified EPDs.

### 1.3 Weidema Pedigree Matrix (Uncertainty Quantification)
- **Source:** Weidema & Wesnæs (1996) `[Weidema1996]`, Ciroth et al. (2016) `[Ciroth2016]`.
- **Specification:** Evaluates LCI data quality across 5 distinct Data Quality Indicators (DQIs):
  1. *Reliability* (Pålitelighet): Data collection methodology and verification.
  2. *Completeness* (Kompletthet): Statistical representative sampling fraction.
  3. *Temporal correlation* (Tidsmessig korrelasjon): Age of data vs project date.
  4. *Geographical correlation* (Geografisk korrelasjon): Spatial origin matching Norway.
  5. *Technological correlation* (Teknologisk korrelasjon): Process technology match.
- Each indicator is scored from **1 (best)** to **5 (worst)**. Scores are transformed into lognormal variance factors to drive Monte Carlo uncertainty propagation (as implemented in ecoinvent).

### 1.4 Edelen & Ingwersen DQI Framework (2018)
- **Source:** Edelen & Ingwersen (2018) `[Edelen2018]`, Int. J. LCA (PMC5919259).
- **Specification:** Data quality MUST be evaluated based on specific purpose, context, and decision role — **never collapsed into a single hidden total score**.
- **System Impact:** High scores in one DQI dimension (e.g. recent temporal data) cannot compensate for severe gaps in another (e.g. wrong geographical region). The user interface must present multi-dimensional quality attributes openly.

### 1.5 EN 15978:2026 (Building-Level LCA including Rehabilitation)
- **Source:** CEN-CENELEC, published April 17, 2026 (`[EN15978-2026]`), replacing EN 15978:2011.
- **Specification:** Standardizes whole-building environmental performance assessments across lifecycle modules (A1–A3, A4–A5, B1–B7, C1–C4, D). Explicitly extends calculation rules to cover existing buildings, major renovations, and rehabilitation projects.

### 1.6 ISO 14040/14044 & EN 15804+A2 (Product EPD Standards)
- **Source:** ISO 14040/14044:2006 (`[ISO14040]`), EN 15804:2012+A2:2019 (`[EN15804]`).
- **Specification:** EN 15804+A2 defines core rules for construction product EPDs, mandating reporting for modules A1–A3, C1–C4 (end of life), and D (reuse/recycling benefits).

### 1.7 Life Cycle Costing (NS-EN 16627 & ISO 15686-5)
- **Source:** ISO 15686-5:2017 (`[ISO15686-5]`), NS-EN 16627 (`[NS-EN16627]`).
- **Critical Requirement:** **NS 3454 was officially withdrawn on September 7, 2023**, and replaced by NS-EN 16627. VERIFIED must anchor all LCC cost structures in NS-EN 16627 and ISO 15686-5, never referencing obsolete NS 3454.

---

## 2. MCDA & Uncertainty Specifications

### 2.1 Mecca (2023) Quantitative Review
- **Source:** Mecca, B. (2023), *Journal of Multi-Criteria Decision Analysis*, DOI 10.1002/mcda.1818 (`[Mecca2023]`).
- **Specification:** Method distribution across urban and architectural sustainability literature:
  - **AHP** (Analytic Hierarchy Process): **46%**
  - **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution): **20%**
  - **MIVES** (Multi-Attribute Utility Theory + Value Functions): **11%**
  - **COPRAS** (Complex Proportional Assessment): **9%**
- **Paywall Status:** Wiley full-text requires 402/institutional access 🟡, but metadata and distribution ratios are verified `[H*]`.

### 2.2 Visible Uncertainty & Opportunity Spaces
- **Source:** Lohman et al. (2023) DMsan framework `[Lohman2023]`, EC3 `[EC3]`.
- **Specification:** Rather than hiding data gaps behind an opaque composite score, uncertainty must be displayed as visible data confidence intervals and data status classifications:
  - *Verified* (specific EPD/FDV)
  - *Generic* (standard database with 1.25 TEK17 markup)
  - *Estimated* (proxy data)
  - *Missing* (explicitly highlighted gap)
- Employs "opportunity spaces" to show under which weighting preferences a specific solution choice dominates.

### 2.3 Rank Reversal Reservations (TOPSIS / COPRAS / VIKOR)
- **Source:** MCDA literature review.
- **Specification:** Classic vector-normalization MCDA methods (TOPSIS, COPRAS, VIKOR) suffer from Rank Reversal — where adding or removing an alternative, or slightly altering criteria weights, unexpectedly flips the relative ranking of unaffected alternatives.
- **System Guardrail:** VERIFIED treats Rank Reversal as an explicit methodological reservation/disclaimer. The system must NOT claim to have eliminated rank reversal, but rather expose weight sensitivity transparently to the user.

---

## 3. Financial & Regulatory Specifications

### 3.1 Empirical Energy-to-Default Literature (Billio, Kaza, An)
- **Billio et al. (2022)** (`[Billio2022]`): *JREFE* 65(3), 419–450, DOI 10.1007/s11146-021-09838-0. Proves that higher EPC energy classes in Dutch residential mortgages statistically correlate with significantly lower Probability of Default (PD).
- **Kaza et al. (2014)** (`[Kaza2014]`): *Cityscape* 16(1), 279–298. Analyzed ~71,000 US residential mortgages; proves **~32% lower default risk (PD)** for owners of ENERGY STAR-certified residential homes.
- **An & Pivo (2020)** (`[An2020]`): *Real Estate Economics* 48(1), 7–42, DOI 10.1111/1540-6229.12228. Analyzed US Commercial Mortgage-Backed Securities (CMBS); proves **34% lower default risk** for LEED/ENERGY STAR certified **commercial real estate** (NOT residential loans).

### 3.2 Bank Regulatory Guidance (EBA EU 2023 vs EBA NO 2023)
- **`[EBA_EU2023]` — European Banking Authority:** Report on Green Loans and Mortgages (EBA/Op/2023/13). Proposes voluntary EU green loan/mortgage labels, ESG reporting standards, and Mortgage Credit Directive (MCD) integration. Highlights that missing technical documentation and unharmonized data are key barriers for bank ESG risk assessment.
- **`[EBA_NO2023]` — Entreprenørforeningen Bygg og Anlegg (Norge):** Industry guide with Grønn Byggallianse & Norsk Eiendom. Documents that up to **20% greenhouse gas reduction from early material choices** is achievable without added project cost in apartment blocks.
- **Strict Distinction Rule:** These two entities share an acronym but must NEVER be conflated. `[EBA_EU2023]` applies exclusively to banking regulations; `[EBA_NO2023]` applies exclusively to Norwegian construction material guidance.

### 3.3 Prudential Climate Risk Directives (Bank of England)
- **`[BoE_PS25-25]` — Bank of England PS25/25 (Dec 2025):** Replaces SS3/19. Mandates integration of climate-related physical and transition risks into bank and insurer core risk frameworks and board governance. Implementation deadline: **June 2026**.
- **`[BoE_DP1-25]` — Bank of England DP1/25 (July 2025):** Discussion Paper on IRB (Internal Ratings-Based) PD and LGD estimation for residential mortgages. Identifies capacity constraints in medium-sized banks. **Note: DP1/25 does NOT deal with climate**, but represents the credit risk model infrastructure that building risk data will feed.

### 3.4 The FoU Gap: Durability & Moisture Robustness to Credit Risk (PD)
- **Empirical Baseline:** Existing literature proves Energy Efficiency ↔ Lower Default Risk (Billio, Kaza, An).
- **The Gap:** **Zero published studies** connect building technical quality, moisture robustness, durability, or maintenance burden to loan default probability (PD) or Loss Given Default (LGD).
- **VERIFIED Hypothesis:** "Holdbarhet/fuktrobusthet → Kredittrisiko (PD)" represents VERIFIED's core financial FoU research gap.

---

## 4. Norwegian SME Context & Existing Tool Breakdown

### 4.1 SME Competitiveness & Flexibility (Nordic Council 2023)
- **Source:** Nordic Council of Ministers (2023), *Building LCA and BIM practices in Norway* (`[Nordic2023]`).
- **Specification:** Norwegian building LCA regulations deliberately maintain flexibility and lower stringency for SMEs to prevent disproportionate administrative burdens that would undermine SME competitiveness against large corporations.

### 4.2 BKA2 Synergy (SINTEF / Vegard Knotten)
- **Source:** BKA2 — *Bærekraftige anskaffelser for de vanlige bygg- og anleggsprosjektene, fase 2* (`[BKA2]`).
- **Specification:** 11.7 MNOK budget (2024–2028), owned by Trondheim kommune with SINTEF (Vegard Knotten). Focuses on developing procurement sustainability criteria.
- **Synergy:** VERIFIED delivers the tender-phase decision model and software test interface, complementing BKA2's procurement criteria. Vegard Knotten's role across both projects guarantees academic transfer without duplication.

### 4.3 Detailed Tool Breakdown (Competitive Landscape)
1. **SmartKalk Miljø (Holte, Norway):**
   - *Strengths:* Integrated into contractor calculation/estimation software (kalkyle); seamless EPD lookups during cost bidding.
   - *Limitations vs VERIFIED:* Single-criterion (carbon/LCA focus); lacks MCDA, LCC, moisture risk, visible data quality indicators, and decision attribution.
2. **Reduzer (NTNU Spin-off, Norway):**
   - *Strengths:* Norwegian tender/anbud focus with 15,000+ EPDs; highly accessible interface for Norwegian contractors.
   - *Limitations vs VERIFIED:* Single-criterion greenhouse gas focus; lacks multi-criteria LCC/durability, visible uncertainty representation, and decision attribution.
3. **Concular (Germany):**
   - *Strengths:* Circular material matching, material passports, circular LCA, and material reuse guarantees (ombruk+garanti).
   - *Limitations vs VERIFIED:* Focuses on circular material exchange and deconstruction, not an offer-phase multi-criteria decision support tool for Norwegian building tenders.
4. **ORIS (France/International):**
   - *Strengths:* Infrastructure and earthworks (vei og anlegg); material route and transport optimization with manual parameter entry.
   - *Limitations vs VERIFIED:* Tailored for civil infrastructure, relying on manual data input; does not provide building EPD/LCC/FDV decision support for SMEs.
5. **Additional Reference Tools:**
   - *One Click LCA (Finland):* Dominant specialist LCA/LCC tool; lacks visible uncertainty per alternative and decision attribution; designed for design engineers.
   - *EC3 (Building Transparency, USA):* Exemplary visible carbon uncertainty intervals ("conservative vs achievable"); single-criterion carbon only; no LCC or moisture risk.

---

## 5. 6-Axis Feature Matrix & VERIFIED's Bounded FoU Gap

The 6-axis matrix defines the exact boundary of existing tools vs. VERIFIED's innovation test surface:

| Axis | Axis Name | Full Definition | Existing Tools Status | VERIFIED Target (Test Surface) |
|:---:|:---|:---|:---|:---|
| **(a)** | **Dataintegrasjon** | Combines heterogeneous data sources (LCA + LCC + EPD/FDV + lifetime + moisture risk + reuse) into one structure. | Tools cover single domains (e.g. Reduzer=LCA, Concular=Reuse, SmartKalk=Cost+LCA). | Integrated data model combining NS-EN 16627 LCC, EPD A1–A3/C/D, lifetime, and moisture risk. |
| **(b)** | **Fase** | Functions in the tender/offer phase (*tilbudsfasen*) prior to contract sign-off and material purchasing. | Tools target design/prosjektering (One Click LCA) or post-construction compliance (Cobuilder). | Tailored decision support during tender preparation when choices are still flexible. |
| **(c)** | **Brukergruppe** | Operable by non-specialists (SME contractors and house buyers) without dedicated LCA engineers. | Specialist tools (One Click LCA, ecoinvent, DMsan) require expert LCA knowledge. | Simplified, explainable visual interface for craftspeople and non-specialist clients. |
| **(d)** | **Forklarbarhet og usikkerhet** | Displays data source, completeness, TEK17 1.25 penalty markup, and confidence intervals — no single hidden score. | Tools produce single opaque composite scores; only EC3 shows carbon confidence intervals. | Visible data quality (verified, generic, estimated, missing), 1.25 TEK17 flag, and no black box. |
| **(e)** | **Beslutningseffekt** | Tracks and attributes whether the report changed, confirmed, or influenced the actual tender decision. | Zero existing market tools measure or attribute user decision impact. | Built-in decision attribution tracking (logging if/how tender choices change post-review). |
| **(f)** | **Bredde i bærekraft (DNSH)** | Incorporates lifetime, moisture robustness, and low LCC (Do No Significant Harm), not just low initial CO₂. | Existing tools are predominantly carbon- or energy-centric (kg CO₂e or kWh). | Multi-attribute DNSH scoring incorporating moisture risk, maintenance intervals, and LCC. |

**Bounded FoU Gap Claim:** "Within the investigated sample of tools, individual components exist, but no single tool combines all 6 axes into an integrated, explainable decision support test surface for Norwegian SMEs in the tender phase."

---

## 6. Ontology, Terminology & Source Status Rules

### 6.1 Required Terminology Rules
- **Use "løsningsvalg"** (solution choice), NOT narrow "produktvalg" (product choice). A solution choice includes product selection, installation method, maintenance needs, and expected service life.
- **Use "testflate"** (test surface / platform), NOT "integrasjonsflate".
- **Describe VERIFIED as "beslutningsstøtte"** (decision support) that shows, compares, and explains. **NEVER use** "VERIFIED velger / anbefaler automatisk" or "svart boks" (black box).
- **Target audience term:** Use "entreprenør og kunde" or "ikke-spesialister" (NOT "spesialister").
- **Effect claims rule:** NEVER claim established causal effect ("VERIFIED reduserer utslipp/feil/risiko"). ALWAYS phrase as hypotheses ("VERIFIED skal teste om...").

### 6.2 Source Status & Citation Rules
- **`[Wiik2025]` (SINTEF Notat 57):** Status ⏸ **Parked**. Unindexed internal customer report. Must NOT be cited as an independent primary proof. Use `[EBA_NO2023]` and `[KD2024]` for the 20% early material emission reduction claim.
- **`[SA2018]` (Samfunnsøkonomisk analyse 2018):** Status ⏸ **Parked** (Lars' decision 2026-06-28). Unconfirmed in open registries; retain as parked until located.
- **`[An2020]`:** Status 🟡. CMBS commercial real estate default reduction (34%), NOT residential.
- **`[Kaza2014]`:** Status 🟢. Verified residential ENERGY STAR default reduction (~32%).
- **`[Billio2022]`:** Status 🟢. Verified Dutch residential EPC rating default reduction.
- **Finans Norge Water Damage (2023):** 10 water damages per hour (≈87,600/year), total payout **5.1 billion NOK** in 2023 (correcting outdated 2021 figure of 78,500 damages).
- **NFR IPN 2026 Grant Limits:** Funding range **1,000,000 – 16,000,000 NOK**, maximum **50%** funding rate for enterprise costs.

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Methodological | 70% A1–A3 Cradle-to-Gate Dominance | Prioritizes raw material and manufacturing emission reduction in early tender decisions | Building material list (A1–A3) | Percentage share of total embodied CO₂e | Flags missing A1–A3 EPD data | `[KD2024]`, Multiconsult/DiBK (2024) |
| 2 | Methodological | TEK17 1.25 Safety Markup | Applies 25% emission markup penalty when generic EPD data is used | Generic LCA factor flag | Calculated CO₂e × 1.25 markup | Alerts user of penalty for unverified data | TEK17 § 9-2, DiBK |
| 3 | Methodological | 5-D DQI Pedigree Assessment | Evaluates data quality across Reliability, Completeness, Temporal, Geographic, Tech correlation (scored 1–5) | Data origin metadata | 5 DQI scores & Monte Carlo lognormal variance | Highlights high-uncertainty data (score 4–5) | `[Weidema1996]`, `[Ciroth2016]`, ecoinvent |
| 4 | Methodological | Edelen Purpose-Fit Quality Display | Presents DQI dimensions separately without collapsing into a single hidden total score | Multi-dimensional DQI metadata | Multi-attribute quality breakdown | Warns against using proxy data across regions | `[Edelen2018]` |
| 5 | Methodological | EN 15978:2026 Rehabilitation LCA | Extends building LCA standard rules to existing building renovation and rehabilitation | Renovation material & demolition scope | Lifecycle modules A1–D impact summary | Rejects non-compliant module aggregation | `[EN15978-2026]` |
| 6 | Methodological | NS-EN 16627 LCC Baseline | Standardized Life Cycle Costing structure replacing withdrawn NS 3454 | Maintenance & replacement intervals | LCC net present value (NPV) | Rejects references to legacy NS 3454 | `[NS-EN16627]`, `[ISO15686-5]` |
| 7 | MCDA & Uncertainty | Multi-Criteria Method Breakdown | Evaluates solution choices using AHP, MIVES, or SAW weighting models | Criteria weights & normalized scores | Alternative ranking & score breakdown | Flags sensitivity to weight variations | `[Mecca2023]` |
| 8 | MCDA & Uncertainty | Opportunity Space Visualization | Exposes preference ranges where specific solution choices dominate | Criteria weight bounds | Visual dominance intervals | Displays non-dominated trade-off sets | `[Lohman2023]`, `[EC3]` |
| 9 | MCDA & Uncertainty | Rank Reversal Disclaimer | Explicitly notes rank reversal sensitivity in TOPSIS/COPRAS ranking models | Alternative set changes | Ranking stability indicator | Warns user of potential rank flipping | MCDA Literature Review |
| 10 | Financial & Regulatory | Residential Energy-to-PD Link | Incorporates verified empirical data connecting EPC/ENERGY STAR to lower default risk | EPC rating / ENERGY STAR certification | Mortgage default risk reduction indicator | Limits residential claims to verified sources | `[Billio2022]`, `[Kaza2014]` |
| 11 | Financial & Regulatory | CMBS Commercial Default Link | Tracks commercial real estate default reduction for LEED/ENERGY STAR properties | Commercial building certification | Commercial mortgage risk metric | Restricts 34% claim strictly to commercial CMBS | `[An2020]` |
| 12 | Financial & Regulatory | EBA Green Mortgage Alignment | Aligns documentation requirements with voluntary EU green loan/mortgage labels | Building energy & material documentation | Green mortgage compliance checklist | Separates bank EBA from contractor EBA | `[EBA_EU2023]` |
| 13 | Financial & Regulatory | BoE Prudential Climate Risk Tracking | Prepares climate risk reporting metrics for bank governance per PS25/25 | Physical & transition climate risk data | Bank risk disclosure summary | Enforces June 2026 readiness horizon | `[BoE_PS25-25]` |
| 14 | Financial & Regulatory | IRB Credit Model Parameterization | Maps building quality parameters to bank internal rating models | Mortgage portfolio parameters | PD/LGD model input structure | Clarifies DP1/25 is IRB capacity, not climate | `[BoE_DP1-25]` |
| 15 | Financial & Regulatory | Durability-to-Credit Risk Gap Test | Tests hypothesis connecting moisture robustness & durability to loan default risk (F1/F5) | Moisture risk score & LCC profile | Credit risk hypothesis test report | Flags claim as unproven FoU hypothesis | `[GullbrekkenHolme2025]`, SoA §7 |
| 16 | SME Context & Tools | SME Regulatory Flexibility Flag | Applies flexible LCA reporting requirements suitable for SME contractors | Contractor company size / tier | Simplified report format | Prevents specialist over-complexity | `[Nordic2023]` |
| 17 | SME Context & Tools | BKA2 Procurement Synergy | Synchronizes tender evaluation test surface with BKA2 sustainability criteria | BKA2 criteria set | Tender comparison summary | Avoids duplicating BKA2 scope | `[BKA2]`, SINTEF |
| 18 | SME Context & Tools | SmartKalk Calculation EPD Lookup | Benchmarks calculation-integrated EPD lookups in Norwegian bidding software | Estimate bill of quantities (BOQ) | Itemized EPD carbon totals | Identifies single-criterion LCA limit | Holte SmartKalk Miljø scan |
| 19 | SME Context & Tools | Reduzer Tender EPD Search | Benchmarks 15,000+ EPD database matching for Norwegian tender bids | Tender specification items | EPD carbon match options | Highlights lack of LCC/moisture risk | Reduzer scan |
| 20 | SME Context & Tools | Concular Circular Warranty Lookup | Benchmarks circular material passport matching and reuse guarantees | Demolished/salvaged material profile | Reusability score & warranty status | Identifies focus on circularity vs tender MCDA | Concular scan |
| 21 | SME Context & Tools | ORIS Transport Route Optimization | Benchmarks infrastructure material and haulage transport modeling | Earthwork material & transport distance | Infrastructure transport footprint | Identifies reliance on manual input | ORIS scan |
| 22 | 6-Axis Matrix | Heterogeneous Data Integration (Axis a) | Synthesizes LCA, LCC, EPD, service life, moisture risk, and reuse data | Multi-source product & building data | Unified solution comparative profile | Flags missing data per domain | SoA §2, Matrix Axis (a) |
| 23 | 6-Axis Matrix | Tender Phase Decision Support (Axis b) | Enables solution comparison before contract sign-off during bid preparation | Bid specification & alternative choices | Offer comparison report | Prevents post-contract lock-in | SoA §2, Matrix Axis (b) |
| 24 | 6-Axis Matrix | Non-Specialist Interface (Axis c) | Delivers plain-language summaries for SME contractors and house buyers | Technical LCA/LCC outputs | Intuitive comparison dashboard | Suppresses expert jargon | SoA §2, Matrix Axis (c) |
| 25 | 6-Axis Matrix | Transparent Quality & TEK17 Markup (Axis d) | Displays data origin, completeness, and TEK17 1.25 penalty markup | Data provenance metadata | Transparent confidence breakdown | Rejects single black-box score | SoA §2, Matrix Axis (d) |
| 26 | 6-Axis Matrix | Decision Attribution Measurement (Axis e) | Logs and attributes whether decision support altered or confirmed offer choices | Pre- and post-review user selection | Decision impact metric | Flags unverified effect claims | SoA §2, Matrix Axis (e) |
| 27 | 6-Axis Matrix | DNSH Multi-Attribute Scoring (Axis f) | Scores long-term durability, moisture robustness, and low LCC | Service life & moisture hazard class | DNSH multi-attribute rating | Penalizes low-carbon items with high risk | SoA §2, Matrix Axis (f) |
| 28 | Ontology & Rules | Løsningsvalg Term Enforcement | Replaces narrow product choice with holistic solution choice (products + assembly + LCC) | Solution alternative description | Standardized solution terminology | Corrects "produktvalg" usage | `ord-og-kildekart-v0.5.yml` |
| 29 | Ontology & Rules | Testflate Non-Automated Guardrail | Ensures system acts as decision support test surface without automated selection | System output prose | Decision support presentation | Blocks "VERIFIED velger automatisk" | `ord-og-kildekart-v0.5.yml` |
| 30 | Ontology & Rules | Parked Source Citation Guardrail | Prevents unverified parked sources from carrying independent application claims | Reference citation key | Validated reference list | Rejects `[Wiik2025]` & `[SA2018]` | Kildedom §2, `ord-og-kildekart-v0.5.yml` |

---

## Edge Cases

| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | TEK17 1.25 Safety Markup | Generic EPD entry for timber framing | System applies 1.25 multiplier to carbon emissions, flags generic status, and displays potential emission savings if specific EPD is provided. |
| 2 | Weidema Pedigree DQI | Data with 2005 publication date (Temporal score = 5) | System calculates expanded lognormal variance, widening the confidence interval and alerting user of outdated temporal data. |
| 3 | Edelen Purpose-Fit DQI | Solution with verified French EPD (Geographic score = 4 for Norway) | System preserves high Reliability score (1) but flags Geographic mismatch (4), preventing score averaging from hiding spatial mismatch. |
| 4 | LCC Baseline | Input referencing legacy NS 3454 standard | System rejects input or raises validation error, requiring cost structure alignment with NS-EN 16627 / ISO 15686-5. |
| 5 | Rank Reversal Disclaimer | User adds a 4th material alternative to tender comparison | System recalculates TOPSIS/COPRAS rankings, displays a rank-reversal sensitivity note if relative order of top 2 options shifts. |
| 6 | Commercial vs Residential Default Claim | User attempts to apply 34% default reduction claim to residential mortgage | System restricts 34% default reduction claim strictly to commercial CMBS (`[An2020]`), enforcing ~32% for residential ENERGY STAR (`[Kaza2014]`). |
| 7 | EBA Acronym Resolution | Document text contains generic "EBA guidance" | System requires disambiguation between `[EBA_EU2023]` (banking regulation) and `[EBA_NO2023]` (Norwegian contractor guide). |
| 8 | Parked Source Citation | Text draft attempts to cite `[Wiik2025]` as sole proof for 20% emission reduction | System flags citation, suppresses `[Wiik2025]` per ⏸ status, and substitutes primary sources `[EBA_NO2023]` and `[KD2024]`. |
| 9 | Finans Norge Water Damage Payout | User inputs legacy 2021 figure of 78,500 water damages | System updates metric to 2023 statistics: 10 damages/hr (≈87,600/year) and 5.1 billion NOK compensation. |
| 10 | NFR IPN Grant Request | Project budget proposes 18 million NOK grant funding | System raises validation error against NFR 2026 §10.1, capping maximum funding request at 16 million NOK (50% max intensity). |
| 11 | DNSH vs Carbon Trade-off | Low-carbon insulation with high moisture degradation risk | System highlights DNSH penalty under Axis (f), preventing low initial CO₂ from masking high technical moisture risk. |
| 12 | Decision Attribution Tracking | User selects alternative solution after viewing comparison dashboard | System logs pre-view vs post-view choice, attributing the decision change without claiming automated selection. |

