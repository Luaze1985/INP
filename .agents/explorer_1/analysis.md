# Comprehensive Review of Verified Source Data for Requirement R1

**Date:** 2026-08-02  
**Author:** Explorer 1 (Read-Only Investigation Agent)  
**Project:** VIBS VERIFIED — IPN-søknad (`C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified`)  
**Working Directory:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\explorer_1`

---

## 1. Executive Summary

This report performs a comprehensive, cross-document verification of all source data, provenances, gate statuses, entity distinctions, and terminology rules for **Requirement R1** in the VIBS VERIFIED IPN project.

Five core reference documents were examined line by line:
1. `docs/reference/vibs-verified-kildedom-2026-06-27.md` (Kildedom datert 2026-06-27)
2. `docs/reference/ipn-kildebibliotek.md` (Kanonisk kildebibliotek v0.5)
3. `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml` (Ontologisk kontrollkart v0.5)
4. `research/evidence_matrix.md` (Evidensmatrise for fase 2)
5. `docs/handoffs/40_agy_klargjor-kilde-og-kontekstpakker_read-only_handoff.md` (Handoff 40 search queue & context packages)

### Key Synthesis Points:
- **Canonical Source Hierarchy:** `ipn-kildebibliotek.md` is the live, canonical register for source gate statuses. `vibs-verified-kildedom-2026-06-27.md` is an authoritative dated reconciliation baseline (2026-06-27). Where newer explicit project leader (Lars Gunnar) decisions exist in `ipn-kildebibliotek.md` or `ord-og-kildekart-v0.5.yml`, the newer decision applies operationally.
- **Entity Disambiguation:** `[EBA_EU2023]` (European Banking Authority, Dec 2023 - green loans/mortgages) and `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg, 2023 - residential building GHG guide) represent two entirely distinct legal and domain entities. They must never be merged into a generic `[EBA]`.
- **Parked Sources:** Both `[Wiik2025]` (SINTEF Notat 57) and `[SA2018]` (Samfunnsøkonomisk analyse 4-2018) are **⏸ Parkert** as of Lars' decision on 2026-06-28. Neither can be used as unconditioned primary proof in grant proposals.
- **Strict Terminology Guardrails:** "løsningsvalg" replaces "produktvalg"; "testflate" replaces "integrasjonsflate"; expressions claiming automatic decisions ("VERIFIED velger/anbefaler automatisk"), black-box operation ("svart boks"), or unproven causal effects ("VERIFIED reduserer utslipp") are strictly prohibited.

---

## 2. Master Source Registry & Canonical Status Tags

Sources in the VIBS VERIFIED project are governed by four canonical status tags:
- 🟢 **Active / Bærende (Confirmed [H]):** Primary or official-authoritative source opened, read, and verified for the specific claim it supports. Can carry a grant proposal sentence alone.
- 🟡 **Under Avklaring (Unconfirmed Primary [H*] / Secondary [M]):** Methodologically strong or contextually relevant, but primary text not opened or secondary/consortium-internal. Supports internally; requires primary verification before standalone use.
- ⏸ **Parkert (Parked):** Withdrawn from active proposal prose by project leader decision. Retained in reference library; can be re-instated upon formal verification/location.
- 🔴 **Avvist / Ikke Siterbar (Unconfirmed [L] / Internal):** Search hit only, abstract only, or non-citeable internal note. Cannot be cited as evidence.

### Complete Categorized Inventory of Sources

| Nøkkel | Tittel / Referanse | Domain | Provenans | Port-status | Primary Assertion / Role |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Standarder & Regulering** | | | | | |
| `[EN15978-2026]` | EN 15978:2026 (CEN 17.04.2026) | Standard | Offisiell | 🟢¹ | 🟢 for publication fact/rehab scope; standard text unread |
| `[NS-EN16627]` | NS-EN 16627 (replaced NS 3454 07.09.2023) | Standard | Primær | 🟢 | LCC building standard benchmark |
| `[CPR2024]` | EU Regulation 2024/3110 (Revised CPR) | EU Reg. | Primær | 🟢 | Construction DPP & machine-readable product data |
| `[ESPR2024]` | EU Regulation 2024/1781 (ESPR) | EU Reg. | Primær | 🟢 | Digital Product Passport framework 2025–2030 |
| `[NFR_IPN2026]` | NFR IPN Call 2026 (§10.1) | Offisiell | Offisiell | 🟢 | Grant limits 1–16 MNOK, max 50 % support rate |
| `[ISO14040]` | ISO 14040/14044:2006 | Standard | Sekundær | 🟡 | LCA principles & framework |
| `[EN15804]` | EN 15804+A2 (CEN/TC 350) | Standard | Sekundær | 🟡 | EPD core rules |
| `[ISO15686-5]` | ISO 15686-5:2017 | Standard | Sekundær | 🟡 | LCC principles for buildings |
| `[RICS-WLC]` | RICS Whole Life Carbon Assessment (2024) | Standard | Sekundær | 🟡 | Whole life carbon methodology |
| `[EUTax]` | EU Taxonomy Climate Delegated Act | EU Reg. | Sekundær | 🟡 | DNSH and green taxonomy criteria |
| `[OmnibusI]` | Omnibus I / CSRD Adjustment (24.02.2026) | EU Reg. | Sekundær | 🟡 | CSRD reporting thresholds |
| `[EN17472]` | EN 17472:2022 (Infrastructure) | Standard | Sekundær | 🔴 | Infrastructure sustainability assessment |
| **Forskning & Metode** | | | | | |
| `[Edelen2018]` | Edelen & Ingwersen (2018) *Int. J. LCA* | Academic | Primær | 🟢 | DQI framework; purpose-fit quality without single score |
| `[Lohman2023]` | Lohman et al. (2023) *ACS Environ. Au* | Academic | Primær | 🟢 | DMsan MCDA framework for environmental choices |
| `[Benke2025]` | Benke et al. (2025) *Scientific Data* | Academic | Primær | 🟢 | Harmonized embodied LCA dataset methodology |
| `[Weidema1996]` | Weidema & Wesnæs (1996) *J. Clean. Prod.* | Academic | Primær | 🟡 | Pedigree matrix foundation |
| `[ecoinvent]` | ecoinvent Pedigree Database | Database | Sekundær | 🟡 | Uncertainty lognormal distribution |
| `[Mecca2023]` | Mecca (2023) *J. MCDA* (DOI 10.1002/mcda.1818) | Academic | Sekundær | 🟡 | MCDA review (AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9%); Wiley 402 |
| `[Ciroth2016]` | Ciroth et al. (2016) *Int. J. LCA* | Academic | Sekundær | 🟡 | Pedigree uncertainty factors |
| `[MCDM2025]` | Construction Material Selection Review (2025) | Academic | Sekundær | 🔴 | Abstract only |
| `[WLC-benchmark-NO]` | Nordic WLC Benchmark (2024-25) | Academic | Sekundær | 🔴 | Unverified benchmark |
| **Grønn Finans & Bank** | | | | | |
| `[EBA_EU2023]` | European Banking Authority (Dec 2023) | Banking | Primær | 🟢 | EBA/Op/2023/13 Green loans & mortgage guidelines |
| `[Billio2022]` | Billio et al. (2022) *JREFE* 65(3), 419–450 | Academic | Primær | 🟢 | Dutch residential mortgage default & EPC link (DOI 10.1007/s11146-021-09838-0) |
| `[Kaza2014]` | Kaza et al. (2014) *Cityscape* 16(1), 279–298 | Academic | Primær | 🟢 | US residential ENERGY STAR default risk (-32 % PD) |
| `[An2020]` | An & Pivo (2020) *Real Estate Econ.* 48(1) | Academic | Primær | 🟡 | US Commercial CMBS default risk (-34 % PD); Wiley 403 paywall |
| `[BoE_PS25-25]` | Bank of England PS25/25 (Dec 2025) | Banking | Sekundær | 🟡 | Climate risk framework (deadline June 2026) |
| `[BoE_DP1-25]` | Bank of England DP1/25 (July 2025) | Banking | Sekundær | 🟡 | IRB PD/LGD model estimation (non-climate) |
| `[EEMI]` | Energy Efficient Mortgage Label | Finance | Sekundær | 🟡 | European green mortgage labeling |
| `[FinanceNorway2018]` | Finans Norge Roadmap Green Competitiveness | Finance | Sekundær | 🟡 | Real estate 60% of bank lending |
| `[Multiconsult2023]` | Multiconsult / Eika Boligkreditt (2023) | Building | Sekundær | 🟡 | Residential building stock emissions share |
| **Verktøy (Konkurrentscan)** | | | | | |
| `[EC3]` | EC3 (Building Transparency, USA) | Tool | Primær | 🟢 | Embodied carbon & visible data uncertainty |
| `[OneClickLCA]` | One Click LCA (Finland) | Tool | Sekundær | 🟡 | LCA/EPD/LCC integration (vendor claims) |
| `[Reduzer]` | Reduzer (Norway / NTNU) | Tool | Sekundær | 🟡 | Norwegian EPD database & tender estimates |
| `[Madaster]` | Madaster (Netherlands) | Tool | Sekundær | 🟡 | Material passport & residual value |
| `[Cobuilder]` | Cobuilder (Norway) | Tool | Sekundær | 🟡 | Product data infrastructure & DPP |
| `[Concular]` | Concular (Germany) | Tool | Sekundær | 🟡 | Circularity, reuse & CircularLCA |
| `[NOBB-OCL]` | NOBB x One Click LCA Integration | Partnership | Sekundær | 🟡 | EPD adoption partnership |
| `[2050Materials]` | 2050 Materials API | Tool | Sekundær | 🔴 | Vendor presentation only |
| **Bransje & Norsk Kontekst** | | | | | |
| `[FinansNorge2024VASK]`| Finans Norge 2023 Skadestatistikk (Feb 2024) | Insurance | Offisiell | 🟢 | 10 water damages/hour (~87,600/yr), 5.1 BNOK payout |
| `[NOBB]` | NOBB / Norsk Byggtjeneste | Database | Sekundær | 🟡 | Norwegian building product database |
| `[EPD-Norge]` | EPD-Norge Database | Database | Sekundær | 🟡 | EPD registry & verification |
| `[CIRPASS2]` | CIRPASS-2 DPP Pilot | EU Project | Sekundær | 🟡 | Construction DPP pilot implementation |
| `[Byggforsk700.320]` | Byggforskserien 700.320 | Technical | Primær | 🟡 | Maintenance & replacement intervals |
| `[Ingvaldsen2008]` | Ingvaldsen (2008) SINTEF Byggforsk | Research | Sekundær | 🟡 | Building defect cost (~5% turnover, 3/4 moisture) |
| `[SINTEFFag18]` | FutureBuilt v3.1 / Resirqel (2019) | Technical | Sekundær | 🟡 | Reuse criteria for construction elements |
| `[PlanGridFMI2018]` | PlanGrid / FMI (2018) | Industry | Sekundær | 🟡 | Rework costs due to bad data (US context) |
| `[Herfjord2021]` | Herfjord & Adolfsen (2021, NTNU) | Academic | Sekundær | 🟡 | Rework time share (~20%) |
| `[Harerusten2022]` | Harerusten (2022, NTNU Master) | Academic | Sekundær | 🟡 | Dispute costs; replaced by SA2018 |
| `[Bygg21_2019]` | Bygg21 (2019) | Industry | Sekundær | 🟡 | Digital purchasing potential |
| `[KS2025]` | KS / NHO / DiBK / KDD (2025) | Public | Sekundær | 🟡 | Faulty building applications (60%) |
| `[Bjørheim2026]` | Bjørheim (2026) / Bisnode | Industry | Industry | 🟡 | Construction bankruptcies (1,583 in 2025) |
| `[BDO2025]` | BDO Byggebransjens Lønnsomhet (2025) | Industry | Industry | 🟡 | Construction operating margin (3.3% in 2024) |
| `[UNION2025]` | UNION Gruppen Boligmarkedsrapport (2025) | Industry | Industry | 🟡 | Norwegian construction cost vs Sweden (+18,000 kr/m²) |
| `[SA2018]` | Samfunnsøkonomisk analyse (Rapport 4-2018) | Consultancy | Primær | ⏸ 🟡 | Conflict cost 2.2 BNOK/yr; Parked 2026-06-28 (Lars) |
| **SMB & Anskaffelser** | | | | | |
| `[Nordic2023]` | Nordic Council of Ministers (2023) | Public | Primær | 🟢 | Building LCA and BIM practices; weaker for SMEs |
| `[BKA2]` | Knotten / SINTEF (2024–2028) BKA2 | FoU | Primær | 🟢 | Bærekraftige anskaffelser phase 2 (11.7 MNOK) |
| `[Lutdal2021]` | Lutdal & Brenden (2021, NTNU) | Academic | Sekundær | 🟡 | Homeowner priority for environmental certification |
| **Konsortie-Interne** | | | | | |
| `[Refleksjonsnotat2026]`| Knotten / SINTEF Refleksjonsnotat v0.1 | Internal | Consortium | 🟡 | Internal synthesis; cannot carry claim alone |
| `[EBA_NO2023]` | EBA Norge, Grønn Byggallianse, Norsk Eiendom| Industry | Sekundær | 🟡 | Multi-family housing guide; 20% CO2 reduction |
| `[KD2024]` | KDD, DiBK, NHO, Fellesforbundet (2024) | Public | Sekundær | 🟡 | Building sector carbon footprint; early phase room |
| `[GullbrekkenHolme2025]`| Gullbrekken & Holme (2025) SINTEF | Research | Primær | 🟡 | Building defect cost (10–30 BNOK/yr); awaiting fulltext |
| `[Wiik2025]` | Wiik, M.K. (2025) SINTEF Notat 57 | Internal | Consortium | ⏸ 🟡 | Material cost neutrality; Parked 2026-06-28 (Lars) |
| `[VIBS-FoUpanel]` | VIBS FoU-panel document | Internal | Consortium | 🔴 | Non-citeable internal text |

---

## 3. Cross-Document Consistency Matrix & Resolution of Discrepancies

### Cross-Verification Across the 5 Documents

| Topic / Key | Kildedom (2026-06-27) | Kildebibliotek (v0.5) | Ord- og Kildekart (v0.5) | Evidence Matrix | Handoff 40 Search Queue | Reconciled Status & Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[An2020]` vs `[An2021]` | Corrected from `An2021` to `An2020` (2020). CMBS Commercial 34% default risk. | Ported as `[An2020]`, 🟡 (Wiley 403). Commercial CMBS only. | Listed as 🟡. Caution: do not cite for residential. | Cited for financial association. | Included in FIN-* package for SINTEF/paywall check. | **Resolved:** Key is `[An2020]`. Port 🟡. CMBS commercial real estate ONLY. |
| `[Kaza2014]` | Added to fix misattribution. Residential ENERGY STAR -32% PD. | Listed as `[Kaza2014]`, 🟢. Primary residential mortgage risk proof. | Listed as 🟢 under grønne kilder. | Cited in Matrix (line 12) for residential mortgage risk. | Included in FIN-* package. | **Resolved:** Key is `[Kaza2014]`. Port 🟢. Residential proof. |
| `[Billio2022]` | Corrected from `Billio_SAFE261` to published JREFE 2022. | Listed as `[Billio2022]`, 🟢. Dutch residential EPC default risk. | Listed as 🟢 under grønne kilder. | Cited in Matrix (line 12, 30). | Included in FIN-* package. | **Resolved:** Key is `[Billio2022]`. Port 🟢. Dutch residential proof. |
| `[SA2018]` | Replaced `Harerusten2022` with `SA2018` as primary (🟢). | Marked ⏸ 🟡 (Parked by Lars 2026-06-28 as report not opened). | Documented as open conflict K-01 (🟢 in Kildedom vs ⏸ 🟡 in Library). | Not cited directly in Matrix. | Included in NO-* package for location. | **Operational Resolution:** ⏸ Parked. Kildebibliotek is newer. Re-insert when report is located. |
| `[Wiik2025]` | Marked unconfirmed consortium report (Notat 57). | Marked ⏸ 🟡 (Parked by Lars 2026-06-28). | Marked ⏸ Parked. Replace with `[EBA_NO2023]` & `[KD2024]`. | Not cited as independent proof. | Included in NO-* package. | **Operational Resolution:** ⏸ Parked. Do not cite as standalone proof. |
| `[EBA_EU2023]` | Disambiguated as European Banking Authority (Dec 2023). | Listed as `[EBA_EU2023]`, 🟢. Banking guidelines. | Listed as 🟢 under grønne kilder. Explicit disambiguation rule. | Cited in Matrix (lines 9, 12, 13, 18, 20). | Included in EU-* and FIN-* packages. | **Resolved:** Key `[EBA_EU2023]`. Port 🟢. Banking/Finance ONLY. |
| `[EBA_NO2023]` | Disambiguated as Entreprenørforeningen Bygg og Anlegg (2023). | Listed as `[EBA_NO2023]`, 🟡 (via bestillingsverk). | Listed as 🟡 under gule kilder. Explicit disambiguation rule. | Cited in Matrix (lines 11, 13, 27). Tension noted vs general sources. | Included in NO-* package. | **Resolved:** Key `[EBA_NO2023]`. Port 🟡. Construction/building ONLY. |
| `[FinansNorge2024VASK]`| Corrected from 78,500 (2021) to 10/hr (~87,600/yr), 5.1 BNOK (2023). | Listed as `[FinansNorge2024VASK]`, 🟢. Official stats. | Listed as 🟢 under grønne kilder. | Cited in Matrix (lines 12, 13). | Included in NO-* package. | **Resolved:** Key `[FinansNorge2024VASK]`. Port 🟢. Official 2023 stats. |
| `[NFR_IPN2026]` | Corrected max funding limit from 16-20 MNOK to 1–16 MNOK (50%). | Listed as `[NFR_IPN2026]`, 🟢. Official NFR call parameters. | Listed as 🟢 under grønne kilder. Max 16 MNOK rule. | Cited in Matrix (lines 11, 14, 22, 62). | Formal limit strictly enforced. | **Resolved:** Key `[NFR_IPN2026]`. Port 🟢. Range 1–16 MNOK, max 50%. |

---

## 4. Deep Dive: [EBA_EU2023] vs. [EBA_NO2023] (Banking vs. Building)

One of the most critical source management requirements in the project is maintaining strict separation between the two entities sharing the "EBA" acronym.

### Comprehensive Comparison Table

| Attribute | `[EBA_EU2023]` | `[EBA_NO2023]` |
| :--- | :--- | :--- |
| **Full Legal Name** | European Banking Authority | Entreprenørforeningen – Bygg og Anlegg (Norge) |
| **Co-Authors / Publisher** | European Union Agency (EBA) | EBA Norge, Grønn Byggallianse & Norsk Eiendom |
| **Publication Title** | *Report on Green Loans and Mortgages* (EBA/Op/2023/13) | *Veileder for klimagassreduksjoner – boligblokker* |
| **Publication Date** | December 15, 2023 | 2023 |
| **Domain Scope** | Financial regulation, banking ESG reporting, mortgage risk | Construction industry, building materials, emissions in housing |
| **Canonical Gate Status** | 🟢 **Active / Bærende** | 🟡 **Under Avklaring** (secondary via bestillingsverk) |
| **Primary Assertion Supported** | Bank ESG reporting requirements, green loan definitions, Mortgage Credit Directive (MCD) review | Early material selection can yield up to 20 % GHG reduction in multi-family housing without extra cost |
| **Application in Grant Proposal** | Section §7 (Financial relevance & bank framework / F5) | Section §3 (Material emissions & early-phase impact / F1) |

### Binding Writing Rules for Proposal Text:
1. **Full Name at First Mention:**
   - EU context: *"European Banking Authority (EBA)..."*
   - Norwegian context: *"Entreprenørforeningen – Bygg og Anlegg (EBA Norge)..."*
2. **Strict Key Separation:** Never collapse or abbreviate both as `[EBA]`. Interdisciplinary text must explicitly use `[EBA_EU2023]` or `[EBA_NO2023]`.
3. **Domain Isolation:**
   - Financial policy, climate risk in banking, green mortgages -> `[EBA_EU2023]` ONLY.
   - Building construction, contractor practices, material carbon cuts -> `[EBA_NO2023]` ONLY.

---

## 5. Deep Dive: Parked Sources Status ([Wiik2025] & [SA2018])

### 1. `[Wiik2025]` (SINTEF Notat nr. 57)
- **Title:** *Kostnadseffekten av klimatiltak i byggenæringen – en litteraturgjennomgang* (SINTEF Notat nr. 57, 2025).
- **Status:** ⏸ **Parkert** (Decision by Lars Gunnar on 2026-06-28).
- **Reason for Parking:** The document is an unindexed, internal consortium work ordered by VIBS/SINTEF. It does not exist in SINTEF Brage or open academic registers. Citing an unreleased internal report to prove the societal benefit of the consortium's own project constitutes circular reasoning.
- **Operational Rule:**
  - Do NOT cite `[Wiik2025]` as an independent primary proof in proposal prose.
  - Substitute with verified primary/secondary sources: `[EBA_NO2023]` (for the 20 % cost-neutral GHG reduction claim) and `[KD2024]` (for the early-phase decision space claim).
  - Re-instatement condition: Only if SINTEF formally opens, registers, and publishes Notat 57 as a public document.

### 2. `[SA2018]` (Samfunnsøkonomisk analyse Rapport 4-2018)
- **Title:** *Konflikter i bygg- og anleggsnæringen* (Rapport 4-2018).
- **Status:** ⏸ **Parkert** / 🟡 **Under Avklaring** (Decision by Lars Gunnar on 2026-06-28).
- **Document Discrepancy (Open Conflict K-01):**
  - `vibs-verified-kildedom-2026-06-27.md` (row 24) marked `[SA2018]` as 🟢, instructing to replace `[Harerusten2022]` with `[SA2018]`.
  - `ipn-kildebibliotek.md` and `vibs-verified-ord-og-kildekart-v0.5.yml` updated on 2026-06-28 marked `[SA2018]` as ⏸ 🟡, stating that the report file itself was not physically located/opened in public registries.
- **Operational Resolution:** Following the time hierarchy rule (newer explicit decisions override dated reconciliation documents), `[SA2018]` is **operationally parked (⏸)**.
- **Operational Rule:**
  - Neither `[Harerusten2022]` (secondary master thesis) nor `[SA2018]` (unopened report) can carry the 2.2 BNOK conflict cost assertion alone in grant prose without explicit qualification.
  - Re-instatement condition: Re-insert `[SA2018]` as active 🟢 as soon as the physical report file is located and verified.

---

## 6. Terminology Constraints & Ontological Guardrails

The project ontology defined in `vibs-verified-ord-og-kildekart-v0.5.yml` establishes mandatory terminology rules to maintain scientific integrity and prevent scope inflation.

### Approved vs. Forbidden Terminology

| Concept / Domain | Approved Terminology | Forbidden / Deprecated Terminology | Rationale & Context |
| :--- | :--- | :--- | :--- |
| **Decision Scope** | **«løsningsvalg»** | «produktvalg» | "løsningsvalg" encompasses products, installation, maintenance intervals, and lifespan in the tender phase. "produktvalg" is too narrow. |
| **Choice Alternatives** | **«alternativer»** (nyanskaffelse, vedlikehold, reparasjon, ombruk) | Single product swap | Broadens scope to circular solutions (HANDOFF 4.1). |
| **System Identity** | **«VERIFIED»** (shows, compares, and explains) | «VERIFIED velger / anbefaler automatisk» | VERIFIED provides decision support; it does NOT make decisions or provide automated recommendations. |
| **UI Framework** | **«sammenligning med synlig datagrunnlag»** | «svart boks» | Data quality, gaps, and uncertainty must be visible, not hidden in a single black-box score. |
| **Role of System** | **«beslutningsstøtte»** | «automatisk beslutningstaker» | The contractor retains professional responsibility for the offer. |
| **Uncertainty & Quality**| **«synlig datakvalitet og usikkerhet»** | «skjult totalscore» | Edelen 2018 DQI principles forbid collapsing multiple dimensions into one score. |
| **Platform Target** | **«testflate»** | «integrasjonsflate» | Data flows and architecture are currently in test phase (HANDOFF 4.4). |
| **Target User Group** | **«entreprenør og kunde» / «ikke-spesialister»** | «spesialister» | Solution must be usable by Norwegian SMEs without specialized internal LCA departments. |
| **Effect Claims** | **«VERIFIED skal teste om…» / «prosjektet skal undersøke om…»** | «VERIFIED reduserer utslipp / feil / omarbeid / risiko» | No current source proves causal impact of VERIFIED. Causal reduction claims are FoU hypotheses, not facts. |
| **IPN Grant Range** | **«1–16 MNOK, maks 50 % støttesats»** | «16–20 MNOK» | Strictly governed by NFR Call 2026 §10.1 (`[NFR_IPN2026]`). |
| **Evidence Basis** | **Independent verified source citations** | «agentkonsensus som belegg» | Explicitly forbidden under AGENTS.md Truth Rule 4. |

---

## 7. Methodological Findings & Verification Instructions

### 1. Evidence Matrix Insights (from `research/evidence_matrix.md`)
- **Data Quality:** Supported by `[Edelen2018]`, `[CPR2024]`, `[ESPR2024]`, `[EPD-Norge]`, `[EBA_EU2023]`. High strength. Data quality must be judged by purpose, context, and role—never collapsed into a single hidden total score.
- **SMB Operating Environment:** Supported by `[Nordic2023]`, `[BKA2]`, `[NFR_IPN2026]`, `[EBA_NO2023]`. Medium-high strength. Norwegian SMEs face fragmented tools and weaker regulatory LCA requirements.
- **Financial Relevance:** Supported by `[Kaza2014]` (residential -32% PD), `[Billio2022]` (Dutch residential EPC), `[An2020]` (commercial CMBS -34% default risk). Evidence proves associative/policy link between energy efficiency and default risk, but does NOT prove a causal effect for VERIFIED in the tender phase.

### 2. Search Queue Context (from `docs/handoffs/40_agy_klargjor-kilde-og-kontekstpakker_read-only_handoff.md`)
- Handoff 40 organizes read-only search packages into:
  - `NO-*` (Norwegian sources: `[SA2018]`, `[KD2024]`, `[EBA_NO2023]`, `[Wiik2025]`, 70% A1-A3, factor 1.25).
  - `FIN-*` (Financial sources: `[An2020]`, `[Billio2022]`, `[Kaza2014]`, `[EBA_EU2023]`).
  - `EU-*` (EU regulations: Omnibus I, CPR, ESPR, EN 15978).
  - `SMB-*` (SME tender practices, LCA adoption).
  - `TOOL-*` (Tool landscape: EC3, One Click LCA, Reduzer, Madaster, Cobuilder, Concular, NOBB).

---

## 8. Summary of Actionable Recommendations for Project Work

1. **Maintain Live Status Hierarchy:** Use `ipn-kildebibliotek.md` as the authoritative port status register.
2. **Enforce EBA Key Separation:** Check all document drafts to ensure `[EBA_EU2023]` and `[EBA_NO2023]` are never confused.
3. **Respect Parked Status (⏸):** Do not re-introduce `[Wiik2025]` or `[SA2018]` into submission prose without explicit unparking criteria being met.
4. **Audit Terminology:** Apply the forbidden words list ("produktvalg", "svart boks", "VERIFIED velger/anbefaler automatisk") as an automated or manual check on all proposal drafts.
5. **Differentiate Association vs. Causality:** Frame VERIFIED's impact on tender decisions as an FoU hypothesis to be tested, supported by associative financial/environmental data.

