# Sannhetsserum & Terminology Review Report: Kapittel K3 (v0.5)

**Reviewer:** Reviewer 2 (Sannhetsserum & Terminology Reviewer)  
**Target File:** `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md`  
**Date:** 2026-08-02  
**Working Directory:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\reviewer_k3_sannhet_1`  

---

## Review Summary

**Verdict**: **APPROVE**

Chapter K3 candidate note (`k3-forskning-sannhetsserum-v0.5.md`) has been evaluated against all 31 Sannhetsserum checkpoints, the canonical source rules in `vibs-verified-ord-og-kildekart-v0.5.yml`, `sannhetsserum-oppdatering-v0.5.md`, `vibs-verified-kildedom-2026-06-27.md`, and `ipn-kildebibliotek.md`.

The candidate document demonstrates complete compliance with source integrity, methodological boundaries, ontological definitions, and NFR IPN research criteria.

---

## 31-Checkpoint Evaluation Matrix

### Group 1: Source Provenance & Hierarchy (CP1 – CP8)

| CP # | Checkpoint Description | Status | Verification Findings / Evidence |
|---|---|---|---|
| **CP1** | Independent Research Baseline (🟢/🟡) | **PASS** 🟢 | All primary claims are backed strictly by independent research and authority sources (`KD2024`, `Multiconsult2023DiBK`, `EBA_NO2023`, `GullbrekkenHolme2025`, `Ingvaldsen2008`, `FinansNorge2024VASK`, `BKA2`, `Bjørheim2026`, `Edelen2018`, `Billio2022`, `Kaza2014`, `EBA_EU2023`). |
| **CP2** | Parked Sources Status (⏸) | **PASS** 🟢 | `[Wiik2025]` ⏸ and `[SA2018]` ⏸ are explicitly marked with ⏸ status in text and matrices. `[Wiik2025]` is replaced by `[EBA_NO2023]` for cost-neutral climate claims. Neither parked source carries any application claim alone. |
| **CP3** | Norwegian Primary Source Priority | **PASS** 🟢 | §1.2 establishes the strict priority rule: 8 Norwegian independent research/authority sources constitute the primary baseline before international contextual sources. |
| **CP4** | Strict EBA Disambiguation | **PASS** 🟢 | `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg Norge) and `[EBA_EU2023]` (European Banking Authority) are strictly separated throughout. No naked "EBA" acronym is used without qualification. |
| **CP5** | An2020 Context Restriction | **PASS** 🟢 | `[An2020]` 🟡 (34% lower default) is explicitly restricted to commercial real estate CMBS loans and explicitly forbidden from being transferred to residential mortgages. |
| **CP6** | Verification of Norwegian Empirical Data | **PASS** 🟢 | Empirical values (10–30 mrd. NOK/yr defect costs in `GullbrekkenHolme2025`, 75% moisture damage in `Ingvaldsen2008`, 5.1 mrd. NOK water damage in `FinansNorge2024VASK`, 70% A1–A3 share in `KD2024`/`Multiconsult2023DiBK`, 20% CO2 cut at 0% CapEx in `EBA_NO2023`, 1583 bankruptcies & 3.3% margin in `Bjørheim2026`, 11.7 MNOK for `BKA2`) match repository source records exactly. |
| **CP7** | No Agent Consensus as Belegg | **PASS** 🟢 | All claims rely on cited literature and statutory baselines, not on internal agent agreement. |
| **CP8** | Explicit Verification Flags (🟢/🟡/⏸) | **PASS** 🟢 | Every source reference in text, ASCII tables, and Seksjon 6 matrix is annotated with explicit status codes. |

---

### Group 2: FoU Scope & Research Questions (CP9 – CP16)

| CP # | Checkpoint Description | Status | Verification Findings / Evidence |
|---|---|---|---|
| **CP9** | 6 Research Questions (F1–F6) | **PASS** 🟢 | Seksjon 4 explicitly formulates all 6 FoU questions with associated hypotheses, independent sources, and pilot measurement points (M1.1–M6.2). |
| **CP10** | F1: Quality, Durability & LCC | **PASS** 🟢 | Anchored in `GullbrekkenHolme2025`, `Ingvaldsen2008`, `FinansNorge2024VASK`, and `NS-EN 16627`. |
| **CP11** | F2: Early-Stage Data Integration | **PASS** 🟢 | Grounded in `KD2024` (63–70% A1–A3) and `Multiconsult2023DiBK` (70% A1–A3). |
| **CP12** | F3: Reuse & Rank Reversal Reservation | **PASS** 🟢 | Integrates `EN 15978:2026` and `Bjørheim2026`. Formulates Rank Reversal mitigation via AHP-MIVES as a testable hypothesis rather than an established proof. |
| **CP13** | F4: SMB Usability & Decision Support | **PASS** 🟢 | Grounded in `Bjørheim2026` (3.3% margin) and `BKA2` (11.7 MNOK). Targets non-specialist usability without administrative bloat. |
| **CP14** | F5: Building Data for Banking/Insurance | **PASS** 🟢 | Grounded in `FinansNorge2024VASK`, `Billio2022`, `Kaza2014`, `EBA_EU2023`, `BoE_PS25-25`, `BoE_DP1-25`. Strictly excludes personal profiling or automated credit decisions. |
| **CP15** | F6: Traceability, DPP & Scaling | **PASS** 🟢 | Anchored in NS-EN ISO 22057, CPR2024, and ESPR2024 Digital Product Passport. |
| **CP16** | BKA2 Synergy (Vegard Knotten / SINTEF) | **PASS** 🟢 | Articulates complementary roles: `BKA2` works on client-side procurement requirements, while `VERIFIED` works on bidder-side decision support for SMB contractors. |

---

### Group 3: Technical Integrity & Decision Support Ethics (CP17 – CP23)

| CP # | Checkpoint Description | Status | Verification Findings / Evidence |
|---|---|---|---|
| **CP17** | Mandatory Technical Suitability Gate | **PASS** 🟢 | Technical durability, moisture robustness, and documentation quality form an obligatory pre-filter (§1.3, §2.1, §5, §7.1). Durability/moisture risks are NEVER hidden behind price or CO2. |
| **CP18** | Explainable Decision Support | **PASS** 🟢 | VERIFIED is defined strictly as decision support («beslutningsstøtte») that presents options, trade-offs, and uncertainty. Automated selection («velger/anbefaler automatisk») is strictly forbidden and absent. |
| **CP19** | No "Svart Boks" / Hidden Total Score | **PASS** 🟢 | Conforms to `Edelen2018` 🟢 by exposing 4 distinct DQI data quality categories instead of aggregating into a single opaque total score. |
| **CP20** | DQI Datastatus Taxonomy | **PASS** 🟢 | Datastatus explicitly categorized into Verifisert 🟢, Generisk 🟢/🟡 (+25% TEK17 factor), Estimert 🟡, and Manglende 🔴/🟡. |
| **CP21** | Stochastic Uncertainty & Monte Carlo | **PASS** 🟢 | Employs `Weidema1996` 🟡 and `Ciroth2016` 🟡 ecoinvent lognormal variance formulas for 10 000-iteration Monte Carlo simulations. |
| **CP22** | Uncertainty Visualization (Mulighetsrom) | **PASS** 🟢 | Conforms to `Lohman2023` 🟢 and EC3 by presenting achievable vs. conservative ranges ("mulighetsrom") rather than false precision point values. |
| **CP23** | Separation of Measured vs Calculated | **PASS** 🟢 | Projections and hypotheses are strictly separated from empirical pilot measurement points (M1.1–M6.2). |

---

### Group 4: Terminology & Ontological Conformance (CP24 – CP28)

| CP # | Checkpoint Description | Status | Verification Findings / Evidence |
|---|---|---|---|
| **CP24** | Terminology «løsningsvalg» | **PASS** 🟢 | «Løsningsvalg» is used consistently across all holistic comparisons (product + installation + durability + maintenance + LCC). Narrow «produktvalg» is eliminated. |
| **CP25** | Terminology «testflate» | **PASS** 🟢 | Existing VIBS platform is consistently designated as an experimental «testflate» for the VERIFIED FoU layer. |
| **CP26** | Prohibition of Causal Software Claims | **PASS** 🟢 | The document refrains from asserting that VERIFIED *already* reduces emissions or defects, framing all effects as hypotheses to be tested. |
| **CP27** | Climate Effect as Exploratory Range | **PASS** 🟢 | Climate reduction is presented as an exploratory range (e.g. up to 20% potential per `EBA_NO2023`), not a guaranteed software outcome. |
| **CP28** | Formal FoU-gap Statement | **PASS** 🟢 | Formulates an explicit statement in §3.3 highlighting the absence of empirical frameworks linking technical durability/moisture to IRB PD/LGD credit risk models. |

---

### Group 5: NFR IPN Rules & Experimental Design (CP29 – CP31)

| CP # | Checkpoint Description | Status | Verification Findings / Evidence |
|---|---|---|---|
| **CP29** | NFR IPN 2026 Financial Frame | **PASS** 🟢 | Correctly specifies 1–16 MNOK with max 50% support rate `[NFR_IPN2026]` 🟢 (§1.1). |
| **CP30** | Closed 7-Step Iterative Test Loop | **PASS** 🟢 | §5 details the complete 7-step iterative methodology from data ingestion to pilot attribution logging and model recalibration. |
| **CP31** | Ethics, Data Privacy & No Profiling | **PASS** 🟢 | Confirms data minimisation, anonymised logging, and explicit prohibition of automated credit decisions or personal profiling (§4.5, §5, §7.2). |

---

## Verified Claims

1. **8 Norwegian Primary Baseline Sources**: `[KD2024]`, `[Multiconsult2023DiBK]`, `[EBA_NO2023]`, `[GullbrekkenHolme2025]`, `[Ingvaldsen2008]`, `[FinansNorge2024VASK]`, `[BKA2]`, `[Bjørheim2026]` verified in text and table matrices.
2. **Parked Sources Handled Correctly**: `[Wiik2025]` ⏸ and `[SA2018]` ⏸ marked as parked in Seksjon 6 table and excluded from carrying claims alone.
3. **No Terminology Infractions**: 0 occurrences of forbidden «produktvalg» in overall context; 0 occurrences of «svart boks» as a design pattern (only as prohibited anti-pattern); 0 occurrences of «automatisk decision-maker».
4. **EBA Disambiguation**: `[EBA_NO2023]` and `[EBA_EU2023]` fully disambiguated.

---

## Coverage Gaps

- **No material coverage gaps found in K3 note.** All required sources, research questions, measurement points, and Sannhetsserum rules are thoroughly addressed.

---

## Unverified Items

- None. All 31 Sannhetsserum checkpoints verified directly against repository documentation and candidate text.
