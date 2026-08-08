# Handoff Report: Challenger 1 (Source Claims & Empirical Data Challenger)

**Working Directory:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\challenger_k3_sources_1`  
**Target File Reviewed:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\docs\reference\prosjektbeskrivelse\k3-forskning-sannhetsserum-v0.5.md`  
**Verdict:** **APPROVE**  

---

## 1. Observation
- **Direct Inspection of `k3-forskning-sannhetsserum-v0.5.md`**:
  - `[GullbrekkenHolme2025]`: Cited in Seksjon 1.2, 2.1, 4.1, 4.5, 6 with status 🟡. Claims: 10–30 mrd. NOK/år defect costs, >50 % of homes built 2010–2020 have ≥1 defect, 2–6 % revenue share.
  - `[Ingvaldsen2008]`: Cited in Seksjon 1.2, 2.2, 4.1, 4.3, 6 with status 🟡. Claims: 75 % moisture-related defects (3 of 4), 2–6 % of turnover (average 5 %).
  - `[FinansNorge2024VASK]`: Cited in Seksjon 1.2, 2.8, 4.1, 4.5, 6 with status 🟢. Claims: 5,1 milliarder NOK water damage in 2023, 10 water damages per hour (≈ 87 600/year). Correctly updated from old 2021 data (78 500 / 4,0 mrd NOK).
  - `[KD2024]`: Cited in Seksjon 1.2, 2.4, 4.2, 4.3, 4.4, 4.6, 6 with status 🟡. Claims: 63–70 % A1–A3 carbon footprint, 17,3 Mt CO₂e sector total, early-phase decision space (Figur 1).
  - `[Multiconsult2023DiBK]`: Cited in Seksjon 1.2, 2.5, 4.2, 6 with status 🟢. Claims: 70 % A1–A3 carbon footprint verified across 4 reference building types.
  - `[EBA_NO2023]`: Cited in Seksjon 1.2, 2.6, 4.1, 4.4, 4.5, 6 with status 🟡. Claims: 20 % emission cuts at 0 % CapEx increase. Strictly separated from `[EBA_EU2023]` (European Banking Authority). Replaces `[Wiik2025]` ⏸.
  - `[Kaza2014]`: Cited in Seksjon 1.2, 3.3, 4.1, 4.5, 6 with status 🟢. Claims: ~32 % PD reduction for ENERGY STAR residential homes.
  - `[An2020]`: Cited in Seksjon 1.2, 3.3, 4.5, 6 with status 🟡. Claims: 34 % CMBS commercial default reduction. Explicit domain constraint enforced: strictly commercial properties, NEVER applied to residential mortgages.
- **Reference Libraries Checked**:
  - `docs/reference/ipn-kildebibliotek.md`
  - `docs/reference/vibs-verified-kildedom-2026-06-27.md`
  - `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`
  - `docs/reference/prosjektbeskrivelse/sannhetsserum-oppdatering-v0.5.md`

## 2. Logic Chain
1. **Source Fidelity**: Each of the 8 audited source citations in `k3-forskning-sannhetsserum-v0.5.md` was cross-referenced against `ipn-kildebibliotek.md` and `vibs-verified-kildedom-2026-06-27.md`. Every numerical value, percentage, and scope condition in the candidate note matches the canonical definitions without discrepancy.
2. **Kildedom Correction Compliance**: The 2023 Finans Norge statistics (5,1 bn NOK / 10 damages per hr = 87 600/yr) were used instead of the 2021 data (78 500 / 4,0 bn NOK). NFR support limits are accurately set to 1–16 MNOK with 50 % max support rate per `[NFR_IPN2026]`.
3. **Domain Constraint Integrity**: An & Pivo (2020) is explicitly restricted to commercial CMBS mortgages across all mentions, preventing false generalization to residential mortgages. Kaza et al. (2014) is correctly cited for residential ENERGY STAR mortgages (~32 % PD reduction).
4. **EBA Separation Rule**: `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg) and `[EBA_EU2023]` (European Banking Authority) are strictly separated. No unqualified "EBA" acronym usage exists.
5. **Parked Sources Handling**: `[Wiik2025]` ⏸ and `[SA2018]` ⏸ are correctly preserved as parked in Section 6 and carry zero standalone primary evidence load.
6. **Ontological Conformance**: Preserves required terms ("løsningsvalg", "beslutningsstøtte", "testflate") and avoids forbidden terms ("produktvalg", "svart boks", "automatisk valg").

## 3. Caveats
- `[GullbrekkenHolme2025]`, `[KD2024]`, `[EBA_NO2023]`, `[An2020]`, `[Mecca2023]`, and `[Bjørheim2026]` remain at port status 🟡 in accordance with `ipn-kildebibliotek.md`. This is intentional and correct until SINTEF completes full-text primary verification for these items.
- No source code or implementation files were modified (review-only mandate).

## 4. Conclusion
- **Verdict:** **APPROVE**
- **Assessment**: The candidate note `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md` passes all empirical source verification tests, respects all domain boundaries, and complies fully with Sannhetsserum and Kildedom rules.

## 5. Verification Method
1. Inspect `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md` Seksjon 1.2, 2.1–2.8, 3.3, 4.1–4.6, 6, and 7 using `view_file` or `grep_search`.
2. Cross-check against `docs/reference/ipn-kildebibliotek.md` and `docs/reference/vibs-verified-kildedom-2026-06-27.md`.
3. Run `.agents/challenger_k3_sources_1/verify_k3_sources.py` or inspect `.agents/challenger_k3_sources_1/challenge_sources.md`.
