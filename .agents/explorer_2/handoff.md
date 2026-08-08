# Handoff Report — Explorer 2 (Research & State-of-the-Art Analysis)

**Dato:** 2026-08-02  
**Fra:** Explorer 2  
**Til:** Parent / Orchestrator (`809995f2-86c3-44bf-831f-2d3b16c9ca10`)  
**Arbeidsmappe:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\explorer_2`  
**Prosjektrot:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified`  
**Leveranser:** `analysis.md`, `handoff.md`, `progress.md`, `BRIEFING.md`, `DISPATCH.md`

---

## 1. Observation

Direct observations from examining the project workspace, reference documentation, research matrices, and intake factchecks:

1. **Original Task Specification (`.agents/ORIGINAL_REQUEST.md`, lines 46–76):**
   - Goal: Prepare `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md` covering 6 required sections: (1) Sammendrag & hovedkonklusjon, (2) Metodisk fundament (LCA/LCC/DQI), (3) MCDA & usikkerhet, (4) Finans- & reguleringskontekst, (5) Norsk SMB-kontekst & tilbudsbeslutninger, (6) Syntese & VERIFIEDs avgrensede FoU-gap (med 6-akser matrise).
   - Strict terminology compliance required with `vibs-verified-ord-og-kildekart-v0.5.yml`: use «løsningsvalg» (not «produktvalg»), avoid «VERIFIED velger/anbefaler automatisk» and «svart boks», use «testflate» for VIBS platform, park `[Wiik2025]` and `[SA2018]` (status ⏸), use `[EBA_NO2023]` and `[KD2024]` for early-phase material emission savings, strictly separate `[EBA_EU2023]` (banking/finance) and `[EBA_NO2023]` (construction guide).

2. **Authoritative Source Reconciliations (`docs/reference/vibs-verified-kildedom-2026-06-27.md` & `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`):**
   - **Multiconsult / DiBK 2023:** Utstøl & Marwig (rev. 06, 24.03.2023) *Klimagassutslipp fra byggematerialer*, DiBK. Summary p. 3 documents that product phase A1–A3 accounts for **70 %** on average of embodied greenhouse gas emissions across 4 reference buildings (enebolig, firemannsbolig, boligblokk, kontorbygg).
   - **TEK17 & 1,25-faktor:** Nordic Sustainable Construction `us2024-428` ("Norway TEK17") & `us2024-415` (Häkkinen et al. 2024). Norwegian TEK17 guidance applies a **1.25 safety factor** (+25%) to non-conservative generic product data (CO2data/Ökobaudat) when product-specific EPDs are absent.
   - **EN 15978:2026:** Publisert av CEN-CENELEC 17. april 2026. Standard for LCA på byggnivå for nye og eksisterende bygg samt rehabilitering/ombruk 🟢 `[EN15978-2026]`.
   - **LCC & Standarder:** ISO 15686-5 & NS-EN 16627 🟢 `[NS-EN16627]`. NS 3454 ble trukket 7. september 2023 og erstattet av NS-EN 16627.
   - **Weidema Pedigree & Edelen DQI:** Weidema & Wesnæs (1996) 5-indikators pedigree-matrise 🟡 `[Weidema1996]`; Edelen & Ingwersen (2018) formålsavhengige DQI («fitness for purpose») uten å skjule usikkerhet i en samleskår 🟢 `[Edelen2018]`.
   - **Mecca 2023 & MCDA:** Mecca (2023) *J. Multi-Criteria Decision Analysis* 🟡 `[Mecca2023]` documents method distribution: AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9%. Rank reversal in TOPSIS/COPRAS/VIKOR is treated as a methodological reservation/hypothesis, not a proven fact.
   - **Finance & Default Risk (PD):** Kaza et al. (2014) *Cityscape* (32 % lavere PD for ENERGY STAR boliger) 🟢 `[Kaza2014]`; Billio et al. (2022) *JREFE* (EPC korrelerer med PD i Nederland) 🟢 `[Billio2022]`; An & Pivo (2020) *Real Estate Economics* (34 % lavere default for kommersielle CMBS-lån) 🟡 `[An2020]`. Bank of England PS25/25 (des 2025, frist juni 2026 for klimarisiko) 🟡 `[BoE_PS25-25]`; BoE DP1/25 (juli 2025, IRB PD/LGD modellbarriere) 🟡 `[BoE_DP1-25]`. EBA EU 2023 (grønne lån) 🟢 `[EBA_EU2023]`.
   - **FoU-gap i Finanssporet:** Ingen empiriske studier kobler bygningskvalitet, holdbarhet eller fuktrobusthet direkte til kredittrisiko/PD/LGD. Dette er et bekreftet kunnskapsgap (F5).
   - **SMB & Verktøy:** Nordic Council (2023) 🟢 `[Nordic2023]` (lempeligere krav for SMB-konkurransekraft); BKA2 SINTEF/Knotten (11,7 MNOK, 2024–2028) 🟢 `[BKA2]`. Verktøyscan: SmartKalk Miljø (kalkyle+EPD/NOBB) 🟡, Reduzer (anbud+EPD), Concular (ombruk+garanti), ORIS (infrastruktur/manuell input).

---

## 2. Logic Chain

1. **Step 1 (Problem & Scope Definition):** `ORIGINAL_REQUEST.md` specifies a 6-section structure for `forskning-og-soa-v0.5-kandidat.md`. Each section requires concrete evidence, verified citations, and ontological compliance with `ord-og-kildekart-v0.5.yml`.
2. **Step 2 (Methodological Foundation Verification):**
   - Observation 2 verifies that LCA/LCC standards must cite EN 15978:2026, NS-EN 16627 (replacing withdrawn NS 3454), Multiconsult/DiBK (70% A1–A3 in 4 reference buildings), TEK17 (1.25 generic multiplier), and Edelen & Ingwersen / Weidema DQI (purpose-dependent data quality without hidden total scores).
3. **Step 3 (MCDA & Uncertainty Alignment):**
   - Mecca (2023) provides empirical literature distribution (AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9%). Lohman DMsan (2023) and EC3 provide models for visible uncertainty. Rank reversal must be framed as a methodological reservation/hypothesis.
4. **Step 4 (Finance & Regulatory Synthesis):**
   - Kaza (2014) and Billio (2022) prove energy↔PD for residential mortgages; An (2020) covers commercial CMBS. The regulatory pull comes from EBA EU (2023), BoE PS25/25, and BoE DP1/25. The explicit FoU gap is the complete absence of empirical literature linking durability/moisture-robustness to credit risk (PD).
5. **Step 5 (SME Context & Tool Scan):**
   - Nordic Council (2023) confirms SME regulatory flexibility. BKA2 (11.7 MNOK) provides SINTEF collaboration context. SmartKalk Miljø rebuts the claim that SME tools only cover price, but no tool covers the full 6 axes.
6. **Step 6 (Synthesis & 6-Axis Matrix):**
   - Combining observations 1–5 yields a 6-axis matrix (Dataintegrasjon, Tilbudsfase, SMB-bruker, Synlig usikkerhet, Beslutningseffekt, DNSH-bredde). VERIFIED's research value lies in synthesizing and testing all 6 axes for Norwegian SMEs in the offer phase.

---

## 3. Caveats

- **Full-text Access:** Sources such as `[An2020]`, `[Mecca2023]`, `[BoE_PS25-25]` and `[GullbrekkenHolme2025]` were accessed via abstracts, Crossref metadata, or secondary synthesis files during this read-only pass. Primary full-text verification must be performed by SINTEF prior to final grant submission.
- **Scope Limit:** Explorer 2 is restricted to read-only investigation and analysis. Source code files and canonical files in `docs/reference/prosjektbeskrivelse/` remain untouched during this phase.

---

## 4. Conclusion

The comprehensive research and State-of-the-Art analysis for `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md` is complete and fully documented in `analysis.md`. The document structure across all 6 mandatory sections is established with exact citations, evidence matrices, tool breakdowns, and the 6-axis comparison matrix. Ontological rules and source status gates are strictly satisfied.

---

## 5. Verification Method

1. **Inspect Analysis File:** View `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\explorer_2\analysis.md` to review the full 6-section breakdown, evidence citations, and 6-axis tool matrix.
2. **Ontological Compliance Audit:** Verify that all terms match `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`:
   - Check that «løsningsvalg» is used (not «produktvalg»).
   - Check that «testflate» is used for VIBS.
   - Confirm that `[Wiik2025]` and `[SA2018]` are flagged as ⏸.
   - Confirm that `[EBA_EU2023]` and `[EBA_NO2023]` are kept separate.
3. **Citation Cross-Check:** Verify Multiconsult/DiBK (70% A1-A3, 4 reference buildings), TEK17 (1.25 generic factor), EN 15978:2026, NS-EN 16627, Mecca 2023 (AHP 46%, TOPSIS 20%), Kaza 2014, Billio 2022, An 2020 (CMBS), BoE PS25/25, BoE DP1/25, Nordic Council 2023, BKA2 11.7 MNOK, SmartKalk Miljø, Reduzer, Concular, ORIS.
