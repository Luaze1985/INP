# VIBS VERIFIED IPN Kildedom Review Report

This report presents the Quality Review and Adversarial Review of the generated kildedom document at `docs/reference/vibs-verified-kildedom-2026-06-27.md` against the requirements in the project.

---

# PART 1: QUALITY REVIEW

## Review Summary

**Verdict**: **APPROVE**

The consolidated kildedom document (`vibs-verified-kildedom-2026-06-27.md`) is correct, complete, robust, and fully conforms to the requirements specified in `C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/ORIGINAL_REQUEST.md`. All 6 contradictions have been successfully resolved, the EBA name collision is preserved, the boundary cases are properly structured with impact statements, and no modifications have been made to the three canonical source documents.

---

## Findings

### Minor Finding 1: Age of Primary Source [SA2018]
- **What**: The primary source replacing `[Harerusten2022]` is Samfunnsøkonomisk analyse (2018) Rapport 4-2018.
- **Where**: `docs/reference/vibs-verified-kildedom-2026-06-27.md` (Sections 1, 2, 4, 5)
- **Why**: Siting a 2018 figure (2.2 billion NOK/year in conflict costs) in a 2026 proposal without mentioning the year or adjusting for inflation may make the figure look outdated to an assessor.
- **Suggestion**: The application text should note that this is a 2018 figure and estimate the inflation-adjusted value (e.g., "approx. 2.9 billion NOK in 2026 value").

### Minor Finding 2: Wiley Paywall for Mecca 2023
- **What**: Reliance on metadata/abstract for `[Mecca2023]` due to the Wiley paywall.
- **Where**: `docs/reference/vibs-verified-kildedom-2026-06-27.md` (Sections 1, 5)
- **Why**: Although the metadata (AHP 46%, TOPSIS 20%) is verified, citing specific ratios without full-text verification introduces a small risk of misrepresenting the context of these percentages (e.g., if they only apply to a specific sub-discipline).
- **Suggestion**: Ensure SINTEF uses their institutional access to download and review the full PDF of Mecca 2023 to confirm the exact scope of the survey.

---

## Verified Claims

- **Claim 1: Resolution of An/Billio/Kaza** → verified via `vibs-verified-full-kildesjekk-2026-06-26.md` and direct schema analysis → **PASS**
  - *An & Pivo (2020)*: Real Estate Economics, CMBS-lån, 34% PD, DOI `10.1111/1540-6229.12228`.
  - *Kaza et al. (2014)*: Cityscape, residensielt, 32% PD.
  - *Billio et al. (2022)*: JREFE, residensielt (Dutch), DOI `10.1007/s11146-021-09838-0`.
- **Claim 2: Vannskadetall Resolution** → verified via Finans Norge Skadestatistikk (2023 vs 2021) → **PASS**
  - 2021: 78,500 damages.
  - 2023: 10 damages/hour (~87,600/year) and 5.1 billion NOK total cost.
- **Claim 3: Wiik 2025 Status & Boundary Case** → verified via SINTEF Brage search results (not found) and Section 4 verification → **PASS**
  - Document is unindexed/internal and correctly routed to "grensetilfeller til Lars" with impact statements.
- **Claim 4: Harerusten 2022 Status & Boundary Case** → verified via NTNU Open search and Section 4 verification → **PASS**
  - Correctly identified as a secondary citation of Samfunnsøkonomisk analyse (2018), routed to "grensetilfeller til Lars" with impact statements, and replaced by the correct primary source.
- **Claim 5: IPN Amount Resolution** → verified via `ipn-barekraft-sannhetsserum-2026-06-21.md` §10.1 → **PASS**
  - Reconciled to 1–16 million NOK with a max 50% support rate. Corrected from 16-20 million NOK.
- **Claim 6: Mecca 2023 Metadata Verification** → verified via Wiley online library matching → **PASS**
  - AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9% verified.
- **Claim 7: EBA Name Collision Preservation** → verified via Section 6 of the kildedom document → **PASS**
  - European Banking Authority (`[EBA_EU2023]`) and Entreprenørforeningen Bygg og Anlegg (`[EBA_NO2023]`) are separated.
- **Claim 8: Canonical Source Integrity** → verified via `git status` check in the workspace → **PASS**
  - No changes made to `ipn-kildebibliotek.md`, `ipn-samledokument.md`, or `ipn-hovedokument.md`.

---

## Coverage Gaps

- **EBA Norge 2023 Data Validation** — risk level: **Low** — recommendation: **Accept risk**
  - The EBA Norge (2023) guideline is itself an industry-published report. While replacing Wiik (2025) with EBA (2023) is a major step forward, the 20% cost-neutral climate reduction claim is still an industry estimate rather than peer-reviewed academic literature. This risk is acceptable for an IPN application, but should be framed as a target for verification in the pilot projects.

---

## Unverified Items

- *None.* All elements in the kildedom document have been successfully cross-referenced with the corresponding verification reports and git states.

---

# PART 2: ADVERSARIAL REVIEW / CRITIQUE

## Challenge Summary

**Overall risk assessment**: **LOW**

The document is highly robust. The main vulnerabilities relate to standard industry assumptions and citation chains which, if left unaddressed, could attract minor criticism from strict academic reviewers on the NFR evaluation panel.

---

## Challenges

### Medium Challenge 1: The Inflation Gap in Conflict Cost (2.2B NOK)
- **Assumption challenged**: That replacing `[Harerusten2022]` with `[SA2018]` completely resolves the 2.2B NOK conflict cost issue.
- **Attack scenario**: An NFR evaluator flags that a 2.2B NOK conflict cost figure based on 2018 data is significantly outdated in 2026, especially given the rapid inflation in the Norwegian construction market over the last 8 years (which has seen a ~30-40% increase in building costs). Citing it raw might make the proposal look dusty.
- **Blast radius**: Low-Medium (assessor notes minor lack of timeliness in the problem description).
- **Mitigation**: Update the application text to adjust for inflation: "2.2 billion NOK in 2018, equivalent to approximately 3.0 billion NOK in 2026 terms."

### Low Challenge 2: Wiley Paywall institutional dependency
- **Assumption challenged**: That Mecca (2023) can be safely cited without the team having read the full-text copy due to the Wiley paywall.
- **Attack scenario**: The NFR panel might contain researchers who are experts in MCDA or authors of similar reviews. If the context of the 46% AHP / 20% TOPSIS figures is restricted in a way that isn't clear from the abstract (e.g., only in specific types of green building certifications, or only in high-rise buildings), citing them generally could be flagged as inaccurate.
- **Blast radius**: Low.
- **Mitigation**: Request that SINTEF's academic team downloads the full text of Mecca (2023) through their institutional access and double-checks the context before final submission.

### Low Challenge 3: Secondary industry-source validation for EBA NO 2023
- **Assumption challenged**: That citing EBA Norge (2023) in place of Wiik (2025) provides fully independent academic grounding for the 20% emission cut.
- **Attack scenario**: EBA Norge (2023) is an industry guideline and not a peer-reviewed academic study. An academic assessor might point out that the 20% number is an industry target/claim and not a scientifically proven fact.
- **Blast radius**: Low.
- **Mitigation**: Frame the 20% figure in the text as a practical target and state that WP3 will perform empirical verification of these levels in the pilot projects.

---

## Stress Test Results

- **Inflation stress test** → Assessor checks if 2.2B NOK represents current market reality → **FAIL** (figure is 8 years old; requires inflation adjustment in the application text).
- **Academic rigour test** → Assessor reviews whether the proposal relies on unindexed internal memos (`[Wiik2025]`) → **PASS** (the memo is correctly redirected to the boundary list and replaced by public sources).
- **Acronym confusion test** → Assessor checks if "EBA" refers to bank rules or contractor guidelines → **PASS** (strictly separated into `[EBA_EU2023]` and `[EBA_NO2023]`).

---

## Unchallenged Areas

- **MCDA methodology choice** — Mecca (2023) statistics are accepted as representative of the current state-of-the-art literature distribution.
