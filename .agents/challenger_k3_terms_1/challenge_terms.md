# Empirical Challenge Report: Terminology & Guardrails (Chapter K3)

**Target Document:** `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md`  
**Challenger:** Challenger 2 (Terminology & Guardrails Challenger)  
**Date:** 2026-08-02  
**Verdict:** **APPROVE**  

---

## Executive Summary

The candidate note `k3-forskning-sannhetsserum-v0.5.md` was empirically scanned and audited against all terminology rules, source hierarchy constraints, and risk guardrails specified in `vibs-verified-ord-og-kildekart-v0.5.yml`, `sannhetsserum-oppdatering-v0.5.md`, and `vibs-verified-kildedom-2026-06-27.md`.

The target document **passes all guardrail tests**. It strictly prioritizes the 8 Norwegian independent research and authority sources as its primary baseline, maintains absolute separation of EBA entities, eliminates automated selection claims, avoids single-source reliance on parked citations, and enforces an explicit technical gate for durability and moisture risks.

---

## Detailed Audit & Empirical Verification Results

### 1. Forbidden Terms & Decision Scope Guardrails

| Forbidden Term / Rule | Target Status | Empirical Observations & Evidence | Result |
| :--- | :---: | :--- | :---: |
| `produktvalg` in decision scope | **CLEARED** | Zero occurrences in decision scope or prose. "Løsningsvalg" is used consistently across all multi-criteria contexts (Lines 42, 133, 163, 226, 252, 317, 393). "Produktvalg" appears only on Line 512 in the self-verifying checklist confirming its elimination. | **PASS** |
| `velger automatisk` / `anbefaler automatisk` | **CLEARED** | Zero occurrences of automated choice or recommendation claims by VERIFIED. The system is consistently framed as open decision support ("beslutningsstøtte") for contractors and clients (Lines 49, 110, 297, 303, 327, 513). | **PASS** |
| `svart boks` (black box) prohibition | **COMPLIANT** | "Svart boks" appears on Lines 46, 155, 299, 300, 408, 462, 513 strictly to criticize existing opaque legacy systems or to state that VERIFIED is *not* a black box ("uten svart boks"). Semantically 100% compliant with transparent DQI exposure (Edelen & Ingwersen 2018). | **PASS** |
| `integrasjonsflate` for VIBS platform | **CLEARED** | Zero occurrences (0 matches). The VIBS platform is consistently designated as "VIBS-plattformen som testflate" or "testflate" (Lines 49, 245, 268, 317, 364, 407, 413, 515). | **PASS** |
| Unqualified `EBA` acronym | **CLEARED** | Every single occurrence of EBA is explicitly disambiguated: `[EBA_NO2023]` / `EBA Norge` (Entreprenørforeningen Bygg og Anlegg, Lines 25, 78, 128, 206, 240, 312, 336, 453) vs. `[EBA_EU2023]` / `European Banking Authority` (Lines 39, 183, 215, 330, 337, 488). No ambiguous "EBA" exists. | **PASS** |

---

### 2. Parked Sources Audit (`[Wiik2025]`, `[SA2018]`)

| Source | Status in K3 | Usage & Verification | Result |
| :--- | :---: | :--- | :---: |
| `[Wiik2025]` | `⏸ PARKERT` | Referenced on Lines 133, 429, 497, 526. Marked strictly as `⏸ PARKERT CONSORTIUM NOTE`. Carries zero application claims alone. Replaced by `[EBA_NO2023]` for 20% carbon reduction claim. | **PASS** |
| `[SA2018]` | `⏸ PARKERT` | Referenced on Lines 429, 500, 526. Marked strictly as `⏸ PARKERT UVERIFISERT KILDE`. Carries zero application claims alone. Replaced by `[KD2024]` for government baseline claims. | **PASS** |

---

### 3. Durability & Moisture Risk Masking Guardrail

- **Requirement:** Ensure durability, lifespan (NS-EN 16627 / Byggforsk 700.320), and moisture risks (Finans Norge VASK / Ingvaldsen 2008) are not hidden behind low price (CapEx) or low CO₂ scores.
- **Empirical Findings:**
  1. **Section 1.3 & 2.2 (Lines 45, 95–102):** Explicitly highlights the failure of existing siloed tools that focus solely on CapEx or theoretical energy scores while ignoring moisture risk (75% of building damage in Norway per Ingvaldsen 2008).
  2. **Section 4.1 (FoU F1, Lines 226–246):** Formulates F1 specifically to prevent low CapEx choices that introduce moisture risk or short lifespan.
  3. **Section 5 & 7 (Lines 518, 528):** Establishes an **obligatory technical gate** ("Obligatorisk teknisk port") where technical suitability, moisture robustness, and documentation quality act as a prerequisite filter before multi-criteria price and CO₂ comparison is performed.
- **Verdict:** Durability and moisture risks are prominently exposed and gated, fully adhering to project guardrails.

---

### 4. Source Hierarchy & Norwegian Primary Baseline

- **Requirement:** Enforce the 8 Norwegian independent research and authority sources (`[KD2024]`, `[Multiconsult2023DiBK]`, `[EBA_NO2023]`, `[GullbrekkenHolme2025]`, `[Ingvaldsen2008]`, `[FinansNorge2024VASK]`, `[BKA2]`, `[Bjørheim2026]`) as the primary foundation, followed by international context.
- **Empirical Findings:**
  1. Section 1.2 explicitly codifies the **Norwegian Primary Baseline Rule** ("Prioriteringsregel for kildegrunnlaget: Norsk primærbaselinje").
  2. Section 2 dedicates full detailed extraction tables and sub-sections to all 8 Norwegian sources.
  3. Section 4 explicitly anchors each research question (F1–F6) in the Norwegian primary baseline in both text and summary tables.
  4. International sources (Edelen, Weidema, Mecca, Benke, Billio, Kaza, EBA EU, BoE) follow as secondary context in Section 3.

---

## Stress Test Scenarios & Results

| Scenario ID | Test Input / Focus | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :---: |
| **ST-01** | Search for forbidden term `produktvalg` in decision scope | 0 instances in decision scope | 0 instances (only in line 512 checklist) | **PASS** |
| **ST-02** | Search for `velger automatisk` / `anbefaler automatisk` | 0 instances | 0 instances | **PASS** |
| **ST-03** | Check all occurrences of `EBA` for ambiguity | All occurrences tagged with `_NO2023` or `_EU2023` or full name | 100% tagged & separated | **PASS** |
| **ST-04** | Check single-source reliance on `[Wiik2025]` or `[SA2018]` | 0 standalone application claims | All tagged with `⏸ PARKERT` | **PASS** |
| **ST-05** | Verify technical moisture/durability risk gating | Mandatory gate before multi-criteria scoring | Explicitly documented in F1, S5, S7 | **PASS** |

---

## Unchallenged Areas

- **Detailed Monte Carlo stochastic math formulas in Section 3.1 & 5:** Evaluated as standard ecoinvent Pedigree formulations; outside terminology/guardrail challenge scope.

---

## Recommendation & Conclusion

Candidate note `k3-forskning-sannhetsserum-v0.5.md` meets all terminology, guardrail, and source hierarchy requirements without reservation. 

**Final Verdict:** **APPROVE**
