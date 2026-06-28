# Source Verification and Conflict Reconciliation Report — VERIFIED (IPN)

**Date:** 2026-06-27T09:12:00+02:00  
**Prepared by:** Read-only Exploration Agent  
**Metadata Directory:** `C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/explorer_reconciliation_3`  
**Purpose:** Reconcile conflicts and resolve academic/regulatory discrepancies across the source verification reports and truth serum documents to prepare the IPN application for submission.

---

## Executive Summary
This report reconciles seven core bibliographic, economic, and regulatory conflicts in the draft IPN documents. By correcting critical misattributions of mortgage default risks (An vs. Billio vs. Kaza), updating water damage statistics to 2023, reframing commissioned and student work (Wiik 2025 and Harerusten 2022) as boundary cases to Lars, correcting the IPN funding limit to 1–16 million NOK, and distinguishing European and Norwegian EBA entities, we establish a robust, verified evidence chain that ensures the application's scientific and regulatory integrity.

---

## 1. Conflict Reconciliation Findings

### Conflict 1: Differentiating An, Billio, and Kaza
In previous drafts, energy-to-default-risk studies were mixed up: Kaza's 32% residential mortgage default risk reduction was attributed to An et al. (under a false JREFE journal citation), and Billio's DOI was mistakenly assigned to An. 

The three sources must be differentiated as separate entities:

| Attribute | **An & Pivo (2020)** | **Billio et al. (2022)** | **Kaza et al. (2012/2014)** |
|---|---|---|---|
| **Author(s)** | An, X. & Pivo, G. | Billio, M., Costola, M., Pelizzon, L. & Riedel, M. | Kaza, N., Quercia, R.G. & Tian, C.Y. (2012) / Kaza, Riley, Quercia & Towe (2014) |
| **Title** | "Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms" | "Buildings' energy efficiency and the probability of mortgage default: The Dutch case" | "Home Energy Efficiency and Mortgage Risks" |
| **Journal / Publisher** | *Real Estate Economics* (Wiley) | *Journal of Real Estate Finance and Economics* (Springer) | IMT/UNC Center for Community Capital (2012) / *Cityscape* (2014) |
| **DOI / URL** | [10.1111/1540-6229.12228](https://doi.org/10.1111/1540-6229.12228) | [10.1007/s11146-021-09838-0](https://doi.org/10.1007/s11146-021-09838-0) | [IMT/UNC Report PDF](https://imt.org/wp-content/uploads/2018/02/IMT_UNC_HomeEEMortgageRisksfinal.pdf) |
| **Scope** | **Commercial real estate** (CMBS loans) | **Residential mortgages** (Netherlands) | **Residential mortgages** (US, Energy Star) |
| **Key Finding** | **34% lower default risk** for LEED / Energy Star commercial buildings. | Energy efficiency rating (EPC class) correlates with lower default probability via borrower cash flow and LTV. | **32% lower default risk** for ENERGY STAR certified residential homes (~71k mortgages). |
| **Correction Needed** | Rename citation key from `[An2021]` to `[An2020]`, fix DOI and journal name, and clarify that it covers commercial property, not residential. | Update `[Billio_SAFE261]` to point to its published journal version `[Billio2022]`. | Add `[Kaza2014]` as a separate, distinct residential reference. |

---

### Conflict 2: Water Damage Statistics (Vannskadetall)
*   **The Conflict:** The drafts referenced **78,500** water damages in connection with the 2023 statistics.
*   **Reconciliation:** 78,500 is actually the figure for the year **2021**. In **2023**, Finans Norge Skadestatistikk (released in Feb 2024) reported an average of **10 water damages per hour**, which yields approximately **87,600 cases per year** (an 11.6% increase over 2021). The total compensation paid out in 2023 was **5.1 billion NOK** (not 4.0 billion).
*   **Recommendation:** Use the **2023 statistics** (10 damages per hour, ~87,600 cases/year, 5.1 billion NOK) in the application. This reflects the most recent verified dataset and highlights the increasing risk profile due to climate change and aging building stock, strengthening the societal need for the VERIFIED tool.

---

### Conflict 3: Wiik 2025 (SINTEF Notat 57) — Boundary Case
*   **The Conflict:** Citing Wiik 2025 (Notat 57) for the claim that *"Gode materialvalg som gjøres tidlig kan gi opptil 20 % reduksjon i utslipp uten at prisen stiger"* (up to 20% emission reduction without added cost).
*   **Evaluation:** This is a project-internal reflection note commissioned by VIBS from SINTEF. It is not an independent peer-reviewed publication. It is not indexed in open databases.
*   **Impact Statements (Grensetilfelle):**
    1.  **Circularity Risk:** An external evaluator may dismiss the citation as circular reasoning ("using a report commissioned by the applicant to validate the applicant's own claims").
    2.  **Verifiability Failure:** Because the document is not indexed in public repositories, it cannot be verified by reviewers. This damages the application's credibility.
    3.  **Dependency on Secondary Sources:** The 20% cost-neutral reduction claim actually originates from secondary sources cited within the note (e.g. EBA (Norge) 2023 and KDD 2024).
*   **Recommendation:** Place in "grensetilfeller til Lars". Do not cite Wiik 2025 as an independent academic authority. Instead, cite the primary Norwegian reports directly: *Entreprenørforeningen Bygg og Anlegg (EBA NO), Grønn Byggallianse & Norsk Eiendom (2023)* and *Kommunal- og distriktsdepartementet (KDD) et al. (2024)*.

---

### Conflict 4: Harerusten 2022 (2.2B NOK Conflict Cost) — Boundary Case
*   **The Conflict:** Citing Harerusten 2022 (NTNU master's thesis) for the figure that conflicts in the construction sector cost **2.2 billion NOK annually**.
*   **Evaluation:** The thesis exists ("Konflikter i bygg- og anleggsbransjen – Analyse av årsaker"), but the 2.2B NOK statistic does not originate from Harerusten's primary calculations. It is a secondary citation of a **2018 Samfunnsøkonomisk analyse (SA) report** (Rapport 4-2018).
*   **Support by other open Norwegian sources:** The 2.2B figure is widely supported in industry media (e.g., *Dagens Perspektiv*, *Byggeindustrien*) but they all trace back to the same 2018 SA report.
*   **Impact Statements (Grensetilfelle):**
    1.  **Academic Rigor:** Citing a student master's thesis as the primary authority for a multi-billion NOK national statistic is weak and academically sub-standard for an IPN review.
    2.  **Age of Data:** The underlying data is from 2018 (pre-inflation, pre-pandemic), meaning the actual current conflict costs are likely much higher.
*   **Recommendation:** Place in "grensetilfeller til Lars". Reframe the citation to reference the primary source directly: *Samfunnsøkonomisk analyse (2018), «Konflikter i bygg- og anleggsnæringen»*, rather than Harerusten 2022.

---

### Conflict 5: IPN Funding Amount Correction
*   **The Conflict:** Previous drafts claimed that the maximum IPN funding support was **16–20 million NOK**.
*   **Reconciliation:** Under §10 of the official 2026 IPN call text (*Innovasjonsprosjekt i næringslivet: Industri og tjenestenæringer 2026*), the funding limits are strictly set to **1,000,000 to 16,000,000 NOK** per project, with a maximum support rate of **50% of the companies' costs** (based on GBER Article 25).
*   **Recommendation:** Immediately correct the erroneous "16-20 million NOK" references to "1-16 million NOK" with a maximum 50% funding rate to prevent budget blocking or disqualification by the Research Council of Norway (RCN).

---

### Conflict 6: Mecca 2023 Metadata and Paywall
*   **Status:** Wiley Online Library, DOI: `10.1002/mcda.1818`.
*   **Paywall Status:** Confirmed. The full text is behind a Wiley subscription paywall (HTTP 402).
*   **Metadata Verification:** The metadata is fully verified. AHP (Analytic Hierarchy Process) is indeed the most used method (46%), followed by TOPSIS (20%), MIVES (11%), and COPRAS (9%).
*   **Recommendation:** Keep the citation. It is highly valid and establishes the academic baseline for MCDA weighting models. SINTEF should fetch the full text via institutional access if specific formula details are needed.

---

### Conflict 7: EBA Name Collision
*   **The Conflict:** The acronym **EBA** is used interchangeably for two completely distinct entities:
    1.  **European Banking Authority (EBA EU):** Published the *Report on Green Loans and Mortgages* in December 2023 (EBA/Op/2023/13).
    2.  **Entreprenørforeningen Bygg og Anlegg (EBA NO / EBA Norge):** Co-authored the *Veileder for klimagassreduksjoner – boligblokker* in 2023 containing the 20% emission cut data.
*   **Reconciliation:** Ambiguous use of "EBA" in the texts confuses financial policy with Norwegian contractor margins.
*   **Recommendation:** Split the citations clearly:
    *   Financial/regulatory statements → cite as **EBA (EU)** or `[EBA_EU2023]`.
    *   Contractor/emission reduction statements → cite as **EBA (Norge)**, **EBA NO**, or `[EBA_NO2023]`.

---

## 2. Proposed Document Updates (Diff & Snippets)

Since the agent is in **read-only investigation** mode, the following changes should be applied by the implementer agent.

### A. Changes to `docs/reference/ipn-kildebibliotek.md`

Replace the incorrect references for An, Billio, and Kaza:

```markdown
<<<<
| `[An2021]` | An et al. Green building cert & mortgage default risk. JREFE. DOI 10.1007/s11146-021-09838-0. ~32 % lavere PD. | Primær | [H] | 🟢 | ja | §7 / F1, F5 |
| `[Billio_SAFE261]` | Billio, Costola, Pelizzon, Riedel. Energy efficiency & mortgage default: Dutch case. SAFE WP 261. | Primær | [H] | 🟢 | ja | §7 / F1, F5 |
====
| `[An2020]` | An, X. & Pivo, G. (2020). «Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms.» Real Estate Economics, 48(1), 7–42. DOI: 10.1111/1540-6229.12228. 34 % lavere default-risiko (CMBS). | Primær | [H*] | 🟢 | ja (metadata) | §7 / F1, F5 |
| `[Billio2022]` | Billio, M., Costola, M., Pelizzon, L. & Riedel, M. (2022). «Buildings' energy efficiency and the probability of mortgage default: The Dutch case». Journal of Real Estate Finance and Economics, 65(3), 419–450. DOI: 10.1007/s11146-021-09838-0. (Tidligere SAFE WP 261). | Primær | [H] | 🟢 | ja | §7 / F1, F5 |
| `[Kaza2014]` | Kaza, N., Riley, S.F., Quercia, R.G. & Towe, C. (2014). «Home Energy Efficiency and Mortgage Risks.» Cityscape, 16(1), 279–298. (Utgitt av IMT/UNC Center for Community Capital). ~32 % lavere default-sannsynlighet for boliger (residensielt). | Primær | [M] | 🟢 | ja (sekundær) | §7 / F1, F5 |
>>>>
```

Correct the Harerusten reference to focus on the primary source:

```markdown
<<<<
| `[Harerusten2022]` | Harerusten (2022, NTNU). Konfliktkostnad 2,2 mrd NOK/år. | Sekundær | [M] | 🟡 | nei (via bestillingsverk) | §8 / WP2 |
====
| `[SA2018]` | Samfunnsøkonomisk analyse (2018). «Konflikter i bygg- og anleggsnæringen» (Rapport 4-2018). Konfliktkostnad 2,2 mrd kr/år. (Sitert via NTNU masteroppgave Harerusten 2022). | Primær | [H*] | 🟢 | ja (medieomtale) | §8 / WP2 |
>>>>
```

### B. Changes to `docs/reference/ipn-hovedokument.md`

Correct line 24 (Conflict costs):
```markdown
<<<<
- Konfliktkostnad 2,2 mrd NOK/år. `[Harerusten2022]` 🟡
====
- Konfliktkostnad 2,2 mrd NOK/år. `[SA2018]` 🟢
>>>>
```

Correct line 41 (F1 references):
```markdown
<<<<
| **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet `[An2021]` 🟢; holdbarhet→PD er hullet |
====
| **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet `[An2020]` 🟢 `[Billio2022]` 🟢 `[Kaza2014]` 🟢; holdbarhet→PD er hullet |
>>>>
```

Correct line 91 (Finansbro references):
```markdown
<<<<
- **Bro til grønn finans:** energi↔PD er bekreftet `[An2021]` 🟢 `[Billio_SAFE261]` 🟢; holdbarhet→PD er FoU-hullet (F1). `[BoE_PS25-25]` 🟡 gir regulatorisk medvind.
====
- **Bro til grønn finans:** energi↔PD er bekreftet `[An2020]` 🟢 `[Billio2022]` 🟢 `[Kaza2014]` 🟢; holdbarhet→PD er FoU-hullet (F1). `[BoE_PS25-25]` 🟡 gir regulatorisk medvind.
>>>>
```

### C. Changes to `docs/reference/ipn-samledokument.md`

Correct line 24 (Conflict costs and EBA):
```markdown
<<<<
2025 ga 1 583 konkurser i næringen (Bjørheim 2026). I tillegg koster konflikter rundt 2,2 milliarder kroner i året (Harerusten 2022), og norske krav gjør det anslagsvis 18 000 kr/m² dyrere å bygge enn i Sverige (UNION 2025).
====
2025 ga 1 583 konkurser i næringen (Bjørheim 2026). I tillegg koster konflikter rundt 2,2 milliarder kroner i året (Samfunnsøkonomisk analyse 2018), og norske krav gjør det anslagsvis 18 000 kr/m² dyrere å bygge enn i Sverige (UNION 2025).
>>>>
```

Correct line 55 (Finansbro paragraph):
```markdown
<<<<
- **Å koble byggteknisk kvalitet to finansiell risiko.** Litteraturen bekrefter at energieffektivitet henger sammen med lavere misligholdsrisiko, men ingen har vist at *holdbarhet og kvalitet* gjør det (An et al. 2021). Det er en ny, etterprøvbar hypotese — og et selvstendig forskningsbidrag.
====
- **Å koble byggteknisk kvalitet til finansiell risiko.** Litteraturen bekrefter at energieffektivitet henger sammen med lavere misligholdsrisiko, men ingen har vist at *holdbarhet og kvalitet* gjør det (An & Pivo 2020; Billio et al. 2022; Kaza et al. 2014). Det er en ny, etterprøvbar hypotese — og et selvstendig forskningsbidrag.
>>>>
```

Correct line 102 (Finansbro summary):
```markdown
<<<<
**Finansbro.** At energieffektivitet henger sammen med lavere risiko for boliglånsmislighold er empirisk bekreftet (An et al. 2021; Billio et al.). Men ingen studie kobler *holdbarhet og byggteknisk kvalitet* til misligholdsrisiko — det er et dokumentert forskningshull, og selve begrunnelsen for VERIFIEDs finansieringsvinkel.
====
**Finansbro.** At energieffektivitet henger sammen med lavere risiko for boliglånsmislighold er empirisk bekreftet (An & Pivo 2020; Billio et al. 2022; Kaza et al. 2014). Men ingen studie kobler *holdbarhet og byggteknisk kvalitet* to misligholdsrisiko — det er et dokumentert forskningshull, og selve begrunnelsen for VERIFIEDs finansieringsvinkel.
>>>>
```

Correct line 100 (Wiik reference):
```markdown
<<<<
Tidlige materialvalg kan redusere klimagassutslippene med opptil 20 prosent uten at prosjektkostnaden øker (Wiik 2025; EBA mfl. 2023).
====
Tidlige materialvalg kan redusere klimagassutslippene med opptil 20 prosent uten at prosjektkostnaden øker (EBA Norge 2023; KDD et al. 2024).
>>>>
```

---

## 3. Synthesis Analysis

### Consensus
*   **Energy-to-Default Correlation:** Multiple high-quality, independent studies confirm that energy efficiency (EPC rating / LEED / Energy Star) is statistically linked to lower mortgage default risk. This establishes the legitimacy of the "green financial premium" argument.
*   **The Research Gap (Embodied Quality-to-Default):** No published academic study has successfully operationalized physical building durability, moisture robustness, or maintenance cycles into a bank's probability of default (PD) or loss given default (LGD) models. This remains the core innovation and research gap for the IPN application.
*   **Early Phase Decisions:** Decision impact is highest in the initial concept and bidding phases, making the tilbudsfase (bidding phase) the most strategic target for decision intervention.

### Resolved Conflicts
*   **The An/Billio/Kaza Discrepancies:** Resolved the DOI collision, journal names, and default percentage errors by splitting them into three separate, correctly characterized citations (An & Pivo 2020 for commercial/CMBS, Billio et al. 2022 for European residential, and Kaza et al. 2014 for US residential).
*   **Water Damage Statistics (Vannskade):** Updated outdated 2021 figures (78,500) to 2023 figures (10 damages per hour / ~87,600 per year) and updated compensation to 5.1 billion NOK.
*   **IPN Budget Caps:** Confirmed 1–16 million NOK (50% max support rate) per RCN guidelines, resolving the incorrect 16–20 million NOK.
*   **Mecca 2023 Weighting Data:** Confirmed AHP (46%) and TOPSIS (20%) metadata, and identified the Wiley paywall constraint.
*   **EBA Abbreviations:** Differentiated European Banking Authority (EBA EU) from Entreprenørforeningen Bygg og Anlegg (EBA NO).

### Dissenting Views (Reframing to Lars)
*   **Wiik 2025 (SINTEF Notat 57):** Citing it as a primary academic authority is highly problematic due to circularity (commissioned work). By placing this in "grensetilfeller til Lars," we recommend Lars either cite the original reports (EBA Norge 2023 and KDD 2024) or frame Wiik 2025 strictly as an internal feasibility study.
*   **Harerusten 2022:** Because it is a master's thesis and relies on secondary statistics for the 2.2B NOK conflict cost, it lacks academic weight. Placing it in "grensetilfeller til Lars" highlights that Lars should redirect the citation to the primary 2018 Samfunnsøkonomisk analyse report.

### Gaps
*   **Empirical SMB Atferdsbevis:** How small contractors actually make decisions in Norway's construction bidding phase is still an open empirical question. The ongoing BKA2 project led by Vegard Knotten is the closest research attempt to fill this gap, but published results are not yet available. This must be presented in the application as a planned output of the research work, rather than an established baseline.
*   **DNSH Social Minimum Requirements:** The social safeguard criteria (e.g., labor rights in the supply chain) have not yet been integrated into the MCDA scoring framework. A DNSH matrix detailing risks and mitigation measures must be drafted before the final application submission.

---

## 4. Verification and Reference Quality Control
All observations and recommended changes in this report have been cross-verified with:
*   `docs/reference/vibs-verified-full-kildesjekk-2026-06-26.md` (identifying the DOI conflict, Kaza studies, and water damage years)
*   `docs/reference/vibs-verified-sonar-2026-06-26.md` (detailing the missing open-access indices for Wiik 2025 and Harerusten 2022)
*   `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md` (detailing the RCN call requirements and budget limits under §10)
*   `docs/reference/ipn-kildebibliotek.md` (cataloging the baseline citation metadata)

This report provides complete traceability and ensures that the implementer agent can execute the suggested updates directly.
