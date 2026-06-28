# Challenge Report — 2026-06-27T09:06:01+02:00

## Challenge Summary

**Overall risk assessment**: **LOW**

The document `docs/reference/vibs-verified-kildedom-2026-06-27.md` is highly accurate, logically consistent, and complies fully with the project guidelines. It successfully resolves all 6 contradictions identified in the source materials and establishes a robust system to handle the EBA EU vs. EBA NO name collision. No modifications have been made to the canonical source files, meaning that their draft states are preserved while the corrections are documented in this central kildedom.

However, several minor methodological assumptions and potential integration vulnerabilities have been identified and should be addressed by the team before final proposal submission.

---

## Challenges

### [Medium] Challenge 1: The "20% emission reduction without cost" claim validity
- **Assumption challenged**: The assumption that replacing the unindexed `[Wiik2025]` reference with `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg Norge) and `[KD2024]` maintains the exact same empirical support for the "20% carbon reduction from material choices without cost" claim.
- **Attack scenario**: A peer reviewer looking up the `[EBA_NO2023]` guide might find that the 20% cost-neutral reduction is highly dependent on specific conditions (such as specific concrete mixes, building scales, or locations) which do not apply generally to the broad SMB residential projects targeted by VIBS.
- **Blast radius**: Loss of credibility in the project's core sustainability and financial feasibility claims in WP3 and WP5.
- **Mitigation**: Ensure that the proposal qualifies the claim by adding the scope of the EBA Norge (2023) guide, e.g., "Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for representative boligblokker (EBA Norge 2023)."

### [Low] Challenge 2: Kaza et al. (2014) vs. IMT/UNC (2012) working paper metadata mismatch
- **Assumption challenged**: The assumption that the published *Cityscape* 2014 article has the exact same findings, figures, and author attribution as the 2012/2013 IMT/UNC working paper.
- **Attack scenario**: The 2012 working paper is authored by "Kaza, N., Quercia, R.G. & Tian, C.Y." while the 2014 Cityscape article is cited in the kildedom as "Kaza, N., Riley, S. F., Quercia, R. G. & Towe, C." If there are minor changes in the peer-reviewed statistics (e.g., default risk reduction being 31% instead of 32%), citing the 2014 version with 2012 numbers could be flagged as a citation error.
- **Blast radius**: Minor academic inaccuracy in the reference bibliography.
- **Mitigation**: SINTEF should verify the exact percentage in the published 2014 Cityscape PDF (`Cityscape, 16(1), 279–298`) rather than relying on the 2012 IMT/UNC working paper text.

### [Medium] Challenge 3: Use of outdated 2023 water damage statistics
- **Assumption challenged**: The assumption that 2023 is the most relevant baseline year for water damage statistics in a proposal being prepared in mid-2026.
- **Attack scenario**: Evaluators might question why a 2026 proposal relies on 2023 statistics (published Feb 2024). If 2024 or 2025 statistics show different trends (e.g., spikes due to extreme weather or shifts in claims), relying on 2023 data makes the problem definition look outdated.
- **Blast radius**: The proposal's risk definition for WP2 could be flagged as outdated.
- **Mitigation**: Check if Finans Norge has published the 2024 or 2025 Skadestatistikk (typically released early 2025 and 2026 respectively) and update the hourly water damage numbers and total cost claims accordingly.

### [Low] Challenge 4: Mecca (2023) paywall and methodological limitations
- **Assumption challenged**: The assumption that the literature review percentages (AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9%) are safe to cite without a full review of the paper's contents.
- **Attack scenario**: The review paper may highlight significant limitations of AHP (such as rank reversal or inconsistency) in SMB environments, which would contradict VIBS's proposed usage of simple and robust weighting models.
- **Blast radius**: The project might unknowingly adopt or reference a framework with documented weaknesses.
- **Mitigation**: SINTEF must download the full-text PDF of Mecca (2023) via Wiley and confirm that the cited methodologies are appropriate for the proposed VIBS decision framework.

### [Medium] Challenge 5: EBA citation key collision in collaborative writing tools
- **Assumption challenged**: The assumption that maintaining separate citation keys (`[EBA_EU2023]` and `[EBA_NO2023]`) in internal documents will naturally prevent citation mix-ups in the final Word/PDF draft.
- **Attack scenario**: During the final compile or when using citation managers (like Zotero, Mendeley, or EndNote), the system might automatically merge both keys into "EBA, 2023" or "EBA (2023)", resulting in mixed-up citations in the final text.
- **Blast radius**: The final PDF submitted to NFR could contain merged references, linking European Banking Authority guidelines to Norwegian building sites.
- **Mitigation**: Rename the institutional authors in the bibliography file to force distinct citation labels, e.g., "EBA Norge" and "European Banking Authority" rather than having both shorten to "EBA".

---

## Stress Test Results

- **Canonical Documents Check** → Verify that no changes are made to the three source files → Checked file sizes, contents, and metadata dates in `docs/reference/` → **PASS** (files are completely untouched and match draft state).
- **Contradiction 1 Resolution** → Verify correct metadata/separation for An, Billio, and Kaza → Check DOIs, journals, and scopes → **PASS** (perfectly separated commercial vs. residential, and corrected the DOI mix-up).
- **Contradiction 2 Resolution** → Verify water damage numbers → 2021 (78,500) vs. 2023 (10/hr, ~87,600/yr, 5.1 mrd NOK) → **PASS** (numerically and historically correct).
- **Contradiction 3 Resolution** → Verify Wiik 2025 handling → Flagged as internal/consortium, recommended primary sources → **PASS** (avoids circular references).
- **Contradiction 4 Resolution** → Verify Harerusten 2022 handling → Replaced with primary source Samfunnsøkonomisk analyse 2018 → **PASS** (academically rigorous).
- **Contradiction 5 Resolution** → Verify IPN funding limits → Corrected to 1–16 MNOK, max 50% funding → **PASS** (crucial for compliance).
- **Contradiction 6 Resolution** → Verify Mecca 2023 percentages → AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9% → **PASS** (metadata verified).
- **EBA Collision Handling** → Verify writing rules and separate keys → `[EBA_EU2023]` vs. `[EBA_NO2023]` with specific guidelines → **PASS** (extremely robust).

---

## Unchallenged Areas

- **Full-Text PDFs contents (e.g., Mecca 2023, Kaza 2014, Samfunnsøkonomisk analyse 2018)** — Reason not challenged: The reviewer did not have access to subscription-based primary PDFs (e.g., behind Wiley or paid firewalls) during this run due to CODE_ONLY network restrictions. Verification relied on secondary verification records and public abstracts.
- **2026 NFR Detailed Application System (in-system fields)** — Reason not challenged: The actual portal schema changes for the 2026 call were out of scope, and the analysis was restricted to the NFR guidelines and text.
