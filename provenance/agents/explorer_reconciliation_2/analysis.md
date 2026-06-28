# Source Reconciliation and Verification Analysis

## Executive Summary
This report analyzes and reconciles the four source verification reports (`vibs-verified-*.md`) and the truth serum document (`ipn-barekraft-sannhetsserum-2026-06-21.md`) for the VIBS VERIFIED IPN application. Seven critical conflicts regarding research citations, water damage statistics, regulatory funding, and organizational name collisions are resolved, providing a clear path for document corrections.

---

## 1. Observation

A systematic review of the four source verification reports and the truth serum document shows the following exact observations:

1. **An & Pivo (2020) vs. Billio et al. (2022) vs. Kaza et al. (2014)**:
   - In `vibs-verified-full-kildesjekk-2026-06-26.md` (lines 11-24), it is observed that early drafts conflated these sources:
     > "In SotA §7 and §13 is An et al. oppgitt med DOI `10.1007/s11146-021-09838-0`. Denne DOI-en tilhører Billio et al. (2022) — ikke An & Pivo (2020)."
     > "SotA attribuerer 'boliger med energisertifisering har ~32 % lavere PD (UNC-studie)' til An et al. med Billio-lenken. 32 %-tallet stammer faktisk fra en annen og separat studie: Kaza, N., Quercia, R.G. & Tian, C.Y. (ca. 2012). *Home Energy Efficiency and Mortgage Risks.*"
     > "An & Pivo (2020) analyserte CMBS (kommersiell eiendom) og fant 34 % lavere default­risiko."
   - In `state-of-the-art-verified-ipn.md` (lines 253-254), the corrected details are:
     - **An & Pivo (2020)**: *Real Estate Economics* 48(1):7–42. DOI: `10.1111/1540-6229.12228`.
     - **Kaza et al. (2014)**: *Cityscape* 16(1):279–298. IMT/UNC Center for Community Capital.
     - **Billio et al. (2022)**: *Journal of Real Estate Finance and Economics* 65(3):419–450. DOI: `10.1007/s11146-021-09838-0`.

2. **Water Damage Statistics (Vannskadetall)**:
   - In `vibs-verified-full-kildesjekk-2026-06-26.md` (lines 26-27), it is observed:
     > "78 500 er antall innmeldte vannskader i 2021. I 2023 ble det meldt inn gjennomsnittlig 10 vannskader per time (Finans Norge Skadestatistikk 2023), noe som tilsvarer ≈ 87 600 per år. Total erstatning i 2023 var 5,1 mrd kr."
   - In `runde3-norske-fagkilder.md` (lines 277-278):
     > "78 500 vannskader på private boliger og hytter [marked as 2023 in some places, but is actually 2021]."

3. **Wiik 2025 (SINTEF Notat 57)**:
   - In `vibs-verified-sonar-2026-06-26.md` (lines 13):
     > "Ingen treff på «SINTEF Notat 57» (2025) spesifikt, hverken som tittel, DOI eller åpen-kildepublisering. SINTEF Open-repositoryet (sintef.brage.unit.no) er bekreftet som det stedet nyere SINTEF Notat er lagt ut, men Notat 57 (2025) dukker ikke opp..."

4. **Harerusten 2022 (2.2B NOK conflict)**:
   - In `vibs-verified-full-kildesjekk-2026-06-26.md` (lines 103-106):
     > "NTNU Open: 'Konflikter i bygg- og anleggsbransjen — Analyse av årsaker' ... Syver Harerusten ... '2,2 milliarder hvert år' finnes i medieomtale (Dagens Perspektiv: 'Krangler om 2,2 milliarder hvert år'), muligens opprinnelig fra en Samfunnsøkonomisk analyse-rapport (~2018)"

5. **IPN Amount limits**:
   - In `ipn-barekraft-sannhetsserum-2026-06-21.md` (line 259), it is observed:
     > "Støttegrenser | Kr 1 000 000 – 16 000 000 per prosjekt"
     > "maks 50 % per bedrift" (line 290)
   - Early drafts in `vibs-verified-agentsøk-2026-06-26.md` (line 74) incorrectly stated:
     > "Maks støttebeløp: 16–20 mill. kr (avhengig av temaområde)"

6. **Mecca 2023**:
   - In `vibs-verified-full-kildesjekk-2026-06-26.md` (lines 88-92):
     > "Assessing the sustainable development: A review of multi-criteria decision analysis for urban and architectural sustainability ... Journal of Multi-Criteria Decision Analysis (Wiley) ... DOI: 10.1002/mcda.1818 ... AHP 46 %, TOPSIS 20 %, MIVES 11 %, COPRAS 9 % ... Wiley-betalingsmur (PDF)"

7. **EBA Name Collision**:
   - In `ipn-samledokument.md` (line 24) and `runde3-norske-fagkilder.md` (line 33), "EBA" is used in two conflicting contexts:
     - European Banking Authority: ESG bank requirements, green loans and mortgages.
     - Entreprenørforeningen - Bygg og Anlegg (EBA NO): Norwegian construction association, co-publisher of "Veileder for klimagassreduksjoner boligblokker" (2023) estimating 20% materials GHG reduction potential.

---

## 2. Logic Chain

1. **An / Billio / Kaza Separation**:
   - *Premise*: Conflating distinct research studies on credit risk and sustainability leads to academic invalidation during review.
   - *Deduction*:
     - **An & Pivo (2020)** must be cited exclusively for **commercial real estate (CMBS)** default risk reduction (**34%**), using DOI `10.1111/1540-6229.12228`.
     - **Kaza et al. (2014)** must be cited for **residential mortgages** default risk reduction (**32%**), based on the ENERGY STAR housing study.
     - **Billio et al. (2022)** must be cited for the Dutch residential mortgage study using energy performance certificates (EPC), with DOI `10.1007/s11146-021-09838-0`.

2. **Water Damage Statistics (Vannskadetall)**:
   - *Premise*: Using 2021 data (78,500) and labeling it as current 2023 or 2026 data is factually incorrect.
   - *Deduction*: The IPN proposal should use the official **2023 statistics** (published in 2024 by Finans Norge): an average of **10 water damages per hour** (approx. **87,600 cases per year**) and **5.1 billion NOK** in total compensation.

3. **Wiik 2025 (SINTEF Notat 57) - Boundary Case**:
   - *Premise*: The report is not indexed in public databases but serves as a key local support.
   - *Deduction*: Because SINTEF is a project partner, this is likely an internal/reflection note. If removed, the application loses its direct Norwegian-specific empirical support for "20% emissions reduction without added cost." If kept without public availability, it risks being flagged by assessors. Thus, it belongs in "grensetilfeller til Lars" with clear instructions to either publish it on SINTEF Open or rephrase as a consortium-internal document.

4. **Harerusten 2022 (2.2B NOK) - Boundary Case**:
   - *Premise*: The thesis exists, but the 2.2B figure is a secondary citation, likely originating from a Samfunnsøkonomisk Analyse (SØA) report.
   - *Deduction*: Removing this figure weakens the problem-description for WP2 (reducing construction conflict costs). Keeping it under "Harerusten 2022" without checking the primary source is academically weak. It is placed in "grensetilfeller" with a recommendation to cite the primary SØA/EBA report.

5. **IPN Amount correction**:
   - *Premise*: The binding 2026 utlysning is the absolute authority for funding rules.
   - *Deduction*: The truth serum §10 confirms the funding limits are **1 to 16 million NOK** (max 50% support). The draft's 16-20 million NOK range must be corrected.

6. **Mecca 2023**:
   - *Premise*: Academic validity requires checking access constraints.
   - *Deduction*: The Wiley paywall is confirmed. Metadata (AHP 46%, TOPSIS 20%) is correct. Recommend SINTEF accesses the full text via institutional access.

7. **EBA Name Collision**:
   - *Premise*: Identical acronyms (EBA) for the European Banking Authority and the Norwegian Contractors Association (Entreprenørforeningen - Bygg og Anlegg) create confusion.
   - *Deduction*: The "20% material GHG reduction without added cost" is from **EBA NO** (2023 guide). The "ESG bank reporting/mortgages" is from **EBA EU** (European Banking Authority). They must be tagged separately as `[EBA EU 2023]` and `[EBA NO 2023]`.

---

## 3. Caveats

- Since the agent operates in CODE_ONLY mode, direct external confirmation of Wiley articles or internal SINTEF databases was not possible during this turn. All observations are verified via the provided internal reports (`docs/reference/vibs-verified-*.md`), which contain cached search results.
- The 2.2B NOK dispute figure is widely accepted in Norwegian media, but its primary econometric calculation details (e.g., from Samfunnsøkonomisk Analyse) remain to be fully audited by the implementation agent.

---

## 4. Conclusion & Actionable Recommendations

### Summary Table of Reconciled Sources

| Source/Topic | Current Draft Status | Reconciled Status / Dom | Actionable Correction / Citation |
|---|---|---|---|
| **An & Pivo (2020)** | Conflated DOI & 32% figure | ⚠️ Feil - må rettes | Set DOI to `10.1111/1540-6229.12228`. Scope: Commercial (CMBS) default risk reduction (34%). |
| **Kaza et al. (2014)** | Feilattribuert til An et al. | ⚠️ Feil - må rettes | Add as separate residential source. Scope: Residential default risk reduction (32%). |
| **Billio et al. (2022)** | Correct bibliography, wrong inline use | 🟢 Bekreftet | Maintain as separate Dutch residential mortgage study. DOI: `10.1007/s11146-021-09838-0`. |
| **Vannskadetall** | Outdated 2021 data (78,500) | ⚠️ Feil - må rettes | Use 2023 data: **10 damages per hour** (≈ 87,600/year) and **5.1 billion NOK** erstatning. |
| **Wiik 2025 (SINTEF 57)** | Unconfirmed in public databases | 🔴 Ikke bekreftet (Grensetilfelle) | Escalate to Lars: publish to SINTEF Open or rephrase as internal consortium reference. |
| **Harerusten 2022** | Unconfirmed 2.2B figure origin | 🔴 Ikke bekreftet (Grensetilfelle) | Escalate to Lars: verify primary SØA/EBA source for the 2.2B figure or replace citation. |
| **IPN Amount** | Incorrect 16-20 MNOK range | ⚠️ Feil - må rettes | Correct to **1-16 million NOK** (max 50% support) per truth serum §10.1. |
| **Mecca 2023** | Confirmed but paywalled | 🟢 Bekreftet (Paywalled) | Verify metadata (AHP 46%, TOPSIS 20%). Wiley paywall holds. SINTEF to retrieve full text. |
| **EBA Collision** | Conflated EBA EU and EBA NO | ⚠️ Feil - må rettes | Distinguish: `[EBA EU]` for European Banking Authority, `[EBA NO]` for Entreprenørforeningen - Bygg og Anlegg. |

---

### Grensetilfeller til Lars (Boundary Cases)

#### 1. Wiik 2025 (SINTEF Notat nr. 57)
- **Claim**: 20% greenhouse gas reduction potential from materials at zero extra cost in early phases.
- **Implication if removed**: The application loses its strongest local empirical claim for early-phase material optimization, making the CO2 reduction targets look speculative or purely international.
- **Implication if kept (unverified)**: Evaluators checking SINTEF Open will find a citation gap, which could impact the credibility of the research methodology section.
- **Recommendation**: Lars should instruct SINTEF to upload the report to SINTEF Open or rephrase the citation as "Wiik 2025 (SINTEF, konsortieinternt notat)."

#### 2. Harerusten 2022 (2.2B NOK Conflict)
- **Claim**: Annual disputes in the construction sector cost 2.2 billion NOK.
- **Implication if removed**: Weakens the problem-quantification for WP2 (Control and Quality Trail), reducing the perceived socio-economic impact of the project.
- **Implication if kept (unverified)**: Using a master's thesis as the primary source for a major macroeconomic figure is academically weak.
- **Recommendation**: Lars should replace the citation with the primary Samfunnsøkonomisk Analyse (SØA) or EBA report, or rephrase: "estimated at 2.2 billion NOK annually (Samfunnsøkonomisk Analyse; ref. Harerusten 2022)."

---

## 5. Verification Method

To verify these recommendations:
1. **SSB & Finans Norge**: Check the Finans Norge 2023 Skadestatistikk (published Feb 2024) to confirm the 10 damages/hour and 5.1 billion NOK figures.
2. **DOI Lookup**: Perform a cross-ref query for DOI `10.1111/1540-6229.12228` (An & Pivo) and `10.1007/s11146-021-09838-0` (Billio et al.).
3. **Wiley Online Library**: Search DOI `10.1002/mcda.1818` to confirm Mecca 2023 metadata (AHP 46% / TOPSIS 20%) and paywall status.
4. **EBA NO vs EBA EU**: Inspect `ipn-samledokument.md` and verify that the 20% materials reduction claim is attributed to the Norwegian Contractors Association guide, not the European Banking Authority.
