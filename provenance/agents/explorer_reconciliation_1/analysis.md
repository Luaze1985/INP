# SOURCE RECONCILIATION AND ANALYSIS REPORT

**Date:** 2026-06-27  
**Prepared by:** Read-only Exploration Agent  
**Target Project:** VIBS VERIFIED IPN Application  
**Context:** Analysis of source verification reports and truth serum to reconcile conflicts, identify boundary cases for Lars, and correct metadata errors before application submission.

---

## Executive Summary
This report reconciles critical conflicts and errors identified across four source verification reports and the project's truth serum. Major findings include the separation of three previously confused grønn finans sources (An, Kaza, and Billio), correction of the IPN funding range to 1–16 million NOK (50% max support), update of the national water damage figures to 2023 statistics (10 per hour / 5.1 billion NOK), and identification of boundary cases (Wiik 2025, Harerusten 2022) requiring manual validation by Lars Gunnar.

---

## Detailed Reconciliation of Conflict Points

### 1. Differentiation of An, Billio, and Kaza as Separate Sources
The previous draft documents conflated three distinct studies into a single credit risk narrative, leading to incorrect DOIs, mismatched journals, and false attributions. They must be treated as three independent sources:

| Detail | Source A: An & Pivo (2020) | Source B: Kaza et al. (2014) | Source C: Billio et al. (2022) |
| :--- | :--- | :--- | :--- |
| **Authors** | An, X. & Pivo, G. | Kaza, N., Riley, S. F., Quercia, R. G. & Towe, C. | Billio, M., Costola, M., Pelizzon, L. & Riedel, M. |
| **Year** | 2020 | 2014 (early draft ~2012) | 2022 (working paper 2020) |
| **Title** | *Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms* | *Home Energy Efficiency and Mortgage Risks* | *Buildings' energy efficiency and the probability of mortgage default: The Dutch case* |
| **Journal / Pub**| *Real Estate Economics*, 48(1), 7–42 | *Cityscape*, 16(1), 279–298 (also IMT/UNC report) | *Journal of Real Estate Finance and Economics*, 65(3), 419–450 |
| **DOI / URL** | `10.1111/1540-6229.12228` | [IMT/UNC PDF Link](https://imt.org/wp-content/uploads/2018/02/IMT_UNC_HomeEEMortgageRisksfinal.pdf) | `10.1007/s11146-021-09838-0` |
| **Core Finding** | **34% lower default risk** for certified buildings | **32% lower default risk** for certified homes | Higher energy efficiency (EPC rating) reduces default probability |
| **Domain** | **Commercial Real Estate (CMBS)** | **Residential Mortgages** | **Residential Mortgages (Dutch)** |
| **SotA Errors** | Linked to Billio's DOI; JREFE journal; and Kaza's 32% figure. | Omitted by name; finding misattributed to An & Pivo. | DOI was copied over to An et al. |

**Reconciliation Recommendation:** Update `ipn-kildebibliotek.md` and `state-of-the-art-verified-ipn.md` to list these as three separate entries. Explicitly specify that the **32% default reduction applies to residential housing** (Kaza) and the **34% default reduction applies to commercial real estate** (An & Pivo).

---

### 2. Water Damage Statistics (Vannskadetall): 2021 vs. 2023
The draft documents used the figure **78,500** for water damage claims. This is a chronological error.
- **78,500** is the number of reported water damage claims in **2021**.
- **2023 Statistics** from Finans Norge (Skadestatistikk for 2023, published Feb 2024):
  - In 2023, an average of **10 water damages per hour** were reported.
  - This translates to **≈ 87,600 claims per year** in 2023 (an increase from 2021).
  - Total payouts/compensation (erstatningsutbetalinger) for water damages in 2023 reached **5.1 billion NOK** (out of 12.6 billion NOK total for private buildings and contents).

**Reconciliation Recommendation:** Replace the outdated 78,500 figure with the 2023 stats in all application drafts:
> *"I 2023 ble det meldt inn gjennomsnittlig 10 vannskader per time i Norge, noe som tilsvarer ca. 87 600 skader per år, med samlede erstatningsutbetalinger på 5,1 milliarder kroner (Finans Norge 2023)."*
If "78,500" is retained, it must be explicitly labeled as a 2021 figure.

---

### 3. Boundary Case: Wiik 2025 (SINTEF Notat 57)
The draft references Marianne Kjendseth Wiik (2025), *SINTEF Notat nr. 57*, claiming a **20% CO2 reduction from supplier choice without extra cost**.
- **Observation:** This document cannot be found in open repositories (such as NTNU Open or SINTEF's Brage repository). It is a consortium-internal, unpublished project draft or "bestillingsverk."
- **Impact Assessment:**
  - **Positive Impact:** Directly supports VIBS' core value proposition (carbon reduction in material selection with 0% cost penalty) in a highly localized Norwegian context.
  - **Negative Impact:** Reviewers checking the citation will find a "blind citation." Citing an unpublished, internal report authored by a consortium partner (SINTEF) raises concerns of self-referential research bias and scientific inflation.
- **Recommendation for Lars:** 
  1. Lars Gunnar must request the actual PDF of SINTEF Notat 57 from Vegard Knotten or the author (Marianne Wiik) to verify that the 20% figure is supported.
  2. If the report is finalized, SINTEF must upload it to their open repository (Brage) to assign it a public handle before submission.
  3. If it remains unpublished, change the citation to Wiik's peer-reviewed public meta-analysis from November 2025 (*"Effektive klimatiltak i byggenæringen: Kostnad og utslippskutt"*) and adjust the claim to reflect what that publication actually states.

---

### 4. Boundary Case: Harerusten 2022 (2.2B NOK Construction Conflicts)
The draft cites *Harerusten (2022)* for the statistic that construction conflicts cost **2.2 billion NOK per year** in Norway.
- **Observation:** Syver Harerusten's NTNU Master's thesis (2022), *«Konflikter i bygg- og anleggsbransjen — Analyse av årsaker»*, is available on NTNU Open. However, the thesis does not contain original research calculating the 2.2B NOK figure. It is highly likely a secondary citation of an older industry report.
- **Analysis:** The 2.2B NOK figure appears widely in Norwegian media (e.g., Dagens Perspektiv: *«Krangler om 2,2 milliarder hvert år»*) and is believed to originate from a *Samfunnsøkonomisk analyse* report (~2018).
- **Recommendation for Lars:**
  1. Lars Gunnar should check page 15-20 of Harerusten's NTNU thesis to find the original source of the 2.2B figure.
  2. The application should cite the original primary report (e.g., *Samfunnsøkonomisk analyse*) directly, rather than a student Master's thesis.
  3. Alternatively, lead with Gullbrekken & Holme (2025), which provides a more recent and robust estimate of building defect costs (10–30 billion NOK/year), and frame conflict costs as a subordinate point.

---

### 5. IPN Amount Correction
Previous drafts referenced a support budget of "16-20 million NOK" for the IPN application.
- **Reconciled Fact:** According to the official Forskningsrådet call (*Innovasjonsprosjekt i næringslivet: Industri og tjenestenæringer 2026*, §10.1):
  - Støttegrenser (funding range): **1 000 000 – 16 000 000 NOK** per project.
  - Støttesatser (support rate): **Maximum 50%** of the companies' costs.
  - The maximum funding request is **16 million NOK**, not 20 million NOK.

**Reconciliation Recommendation:** Change all references to project funding limits from "16-20 million NOK" to **"1-16 million NOK, with a maximum 50% funding rate."** Adjust WP budgets and partner matching allocations accordingly.

---

### 6. Mecca 2023 Metadata and Wiley Paywall
The draft cites *Mecca (2023)* to establish that MCDA weighting methods are veletablerte in urban/architectural contexts.
- **Metadata Verification:**
  - Title: *Assessing the sustainable development: A review of multi-criteria decision analysis for urban and architectural sustainability*
  - Journal: *Journal of Multi-Criteria Decision Analysis* (Wiley, 2023). DOI: `10.1002/mcda.1818`.
  - Figures: AHP (Analytic Hierarchy Process) accounts for **46%** of papers, and TOPSIS accounts for **20%** of papers. MIVES represents 11% and COPRAS 9%.
  - Paywall: **Confirmed**. The PDF is paywalled (402 Payment Required).
- **Recommendation:** The metadata and percentages are correct. Since the PDF is behind a Wiley paywall, SINTEF must access the full text via their institutional subscription to verify the context of these percentages prior to final submission.

---

### 7. EBA Name Collision (EBA EU vs. EBA NO)
The acronym "EBA" is used for two completely different entities in the project documentation:
1. **EBA (EU)**: European Banking Authority.
   - Relevant for: *Report on Green Loans and Mortgages* (Dec 15, 2023). Focuses on grønn finans, green loan label, and the MCD (Mortgage Credit Directive) revision.
2. **EBA (NO)**: Entreprenørforeningen - Bygg og Anlegg (Norwegian Association of Heavy Equipment Contractors).
   - Relevant for: *Veileder for klimagassreduksjoner – boligblokker* (2023), which discusses the 20% CO2 reduction guidelines.

**Reconciliation Recommendation:** 
- In the bibliography, separate the keys into `[EBA_EU2023]` and `[EBA_NO2023]`.
- In the body text, write out the full names upon first mention: *"European Banking Authority (EBA)"* and *"Entreprenørforeningen Bygg og Anlegg (EBA)"* respectively to prevent reader confusion.

---

## Synthesis of Findings

### Consensus
- **The FoU Gap holds:** There is a well-documented connection between building energy efficiency and reduced mortgage default probability (proven by Kaza et al. 2014 for residential, and An & Pivo 2020 for commercial). However, **no study from 2024–2026 connects building durability, physical quality, or maintenance to credit default risk (PD/LGD)**. This is a genuine and citeable research gap.
- **MCDA usage:** AHP (46%) and TOPSIS (20%) are the dominant methodologies in architectural multi-criteria decision analysis, supporting the choice of weight-based models in VIBS.
- **Digital Product Passports (DPP):** Standard structures (GS1/GTIN, CPR 2024, ESPR 2024) are developing rapidly, but construction-specific DPPs are in early pilot phases (CIRPASS-2), creating a market window for a "DPP-ready" tool in the bidding phase.

### Resolved Conflicts
- **An & Pivo (2020) vs. Kaza et al. (2014):** Confirmed that these are separate studies on commercial and residential loans, respectively, correcting the mixed references and DOIs.
- **Finans Norge stats:** Shifted the baseline from 2021 (78,500 claims) to 2023 (10 water damages per hour / 5.1B NOK erstatning).
- **IPN Budget:** Corrected the erroneous "16-20 million NOK" limit to the official "1-16 million NOK" range with a 50% cap.

### Dissenting Views / Boundary Cases
- **Wiik (2025) / Notat 57:** A conflict exists between the desire to cite a highly relevant 20% reduction statistic and the lack of a public, verifable record of the document.
- **Harerusten (2022) / 2.2B NOK:** The NTNU master's thesis exists but is likely a secondary source for the 2.2B figure. The primary source must be checked and cited directly.

### Gaps
- **SMB behavior in bidding:** There is a lack of empirical, published literature regarding how Norwegian SMB contractors make material and sustainability decisions during the bidding phase. This should be framed as a core research question that the IPN project intends to investigate (especially via WP4 and the BKA2 project alignment).

---

## Action Items for Application Text Update

1. **Kildebibliotek:** Update references for `[An2020]`, `[Kaza2014]`, and `[Billio2022]` with correct DOIs, journals, and domains.
2. **Water Damage Text:** Replace *"78 500 vannskader"* with *"10 vannskader per time i 2023 (≈ 87 600 per år) med utbetalinger på 5,1 milliarder kroner"*.
3. **Budget Figures:** Audit and modify the budget sheets to ensure the NFR request does not exceed 16,000,000 NOK and that no partner receives more than 50% support.
4. **EBA Citations:** Explicitly clarify the identity of "EBA" in sections discussing banking regulations versus construction guidelines.
5. **Wiik 2025 & Harerusten 2022:** Perform the manual PDF audits suggested in the boundary case section before final submission.
