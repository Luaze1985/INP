# Original User Request

## Initial Request — 2026-06-27T07:02:50Z

Review, coordinate, and reconcile four conflicting source verification reports for the Vibs IPN project, resolving key contradictions, and produce a unified source verdict document without editing the canonical files.

Working directory: C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass
Integrity mode: development

## Requirements

### R1. Reconcile Source Verification Reports
Review the four source verification reports from 2026-06-26:
- `docs/reference/vibs-verified-agentsøk-2026-06-26.md`
- `docs/reference/vibs-verified-agentverifisering-2026-06-26.md`
- `docs/reference/vibs-verified-full-kildesjekk-2026-06-26.md`
- `docs/reference/vibs-verified-sonar-2026-06-26.md`

Synthesize them into a single authoritative judgment table.

### R2. Resolve Six Known Contradictions
Explicitly resolve the following conflicts:
1. **An/Billio/Kaza**: Differentiate as three separate sources with correct DOI, journal, and scope:
   - Billio et al. (JREFE 65(3):419-450, 2022) with DOI `10.1007/s11146-021-09838-0`
   - An & Pivo (Real Estate Economics, DOI `10.1111/1540-6229.12228`) - 34%, commercial/CMBS
   - Kaza et al. (2014) (Cityscape) - 32%, residential (~71,000 ENERGY STAR homes)
2. **Vannskadetall**: Determine which year's figures (2021 vs. 2023) should apply based on Finans Norge 2023 (~10 damages/hour, ~87,600/year, 5.1B NOK) or 2021 (~78,500 damages).
3. **Wiik 2025 (SINTEF Notat 57)**: Reconcile status (not indexed/unconfirmed). Do not delete or keep silently; place in "grensetilfeller til Lars" (boundary cases to Lars).
4. **Harerusten 2022 (2.2B NOK conflict)**: Reconcile status (not found/unconfirmed). Check if this 2.2B figure is supported by any other open Norwegian source. If not, place in "grensetilfeller til Lars".
5. **IPN Amount**: Reconcile supporting limits. Use `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md` §10 (truth serum) which says 1-16 million NOK, max 50% support. Correct the erroneous 16-20 million NOK figure reported in some verification reports.
6. **Mecca 2023**: Reconcile metadata (AHP 46% / TOPSIS 20%) and confirm whether it can support its claim without full-text access (behind Wiley paywall).

### R3. Prioritize Norwegian/European Sources
Prioritize open Norwegian and European sources for confirming claims.

### R4. Output Unified Source Verdict
Generate a markdown file at `docs/reference/vibs-verified-kildedom-2026-06-27.md` containing:
1. A consolidated judgment table mapping claims to sources and verification status (🟢 confirmed, 🔴 unconfirmed, ⚠️ error-needs-correction).
2. A removal list (🔴) detailing affected sentences.
3. A correction list (⚠️) detailing before/after metadata and values.
4. A "boundary cases to Lars" list (e.g., Wiik 2025, Harerusten 2022) detailing implications if removed vs. kept.

### R5. Integrity Constraints
Do not modify the three canonical documents (`docs/reference/ipn-kildebibliotek.md`, `docs/reference/ipn-samledokument.md`, `docs/reference/ipn-hovedokument.md`).

## Acceptance Criteria

### Execution & Deliverables
- [ ] The output file `docs/reference/vibs-verified-kildedom-2026-06-27.md` is successfully created.
- [ ] No changes are made to the three canonical source documents (`ipn-kildebibliotek.md`, `ipn-samledokument.md`, `ipn-hovedokument.md`).

### Verdict Content & Conflict Resolution
- [ ] Every claim in the final judgment table has a clear source attribution and status (🟢, 🔴, ⚠️).
- [ ] The six known contradictions are explicitly resolved in accordance with the provided guidelines.
- [ ] The EBA name collision (EBA EU = bank vs. EBA NO = entrepreneur association) is preserved and correctly distinguished.
- [ ] Wiik 2025 and Harerusten 2022 are placed in "grensetilfeller til Lars" with impact statements rather than being silently deleted or kept.

## Verification
- An independent auditor agent will review the generated `docs/reference/vibs-verified-kildedom-2026-06-27.md` file against the input reports and truth serum document to verify the correctness of the synthesized table and that all 6 conflicts are resolved.
- A git status check will verify that no modifications have been made to the canonical documents.

## Follow-up — 2026-06-27T07:24:04Z

Conduct a word and semantic analysis of the Vibs IPN application documents using Python and Pandas to identify complex terminology and AI buzzwords, and compare the findings against project standards for simpler language and consistency.

Working directory: C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass
Integrity mode: development

## Requirements

### R1. Python/Pandas Text Analysis Script
Write a Python script using pandas that reads the target documents, tokenizes the text, and calculates the frequencies of:
1. AI/Tech buzzwords (e.g., AI, kunstig intelligens, agent, maskinlæring, algoritme, llm, gpt, neural, deep learning).
2. Complex consulting/academic jargon (e.g., synergi, transformasjon, optimalisering, robust, holistisk, digitalisering).
3. Complex sentences or long words that hinder simple language.

Save the script to the scratch directory at:
`C:/Users/larse/.gemini/antigravity-cli/brain/808bc8bb-a252-43c8-843a-e502f888be0a/scratch/word_analysis.py`

### R2. Analyze Target Documents
Run the script to analyze the following files:
- `docs/reference/ipn-samledokument.md`
- `docs/reference/ipn-hovedokument.md`

### R3. Compare against Project Standards
Compare the analysis results against the style, clarity, and consistency standards defined in `docs/reference/claude-guardrails.md` (e.g., simple language, clear definitions, avoid over-promising, correct partner naming, correct product status).

### R4. Generate Analysis Report
Produce a unified report at `docs/reference/vibs-verified-språkanalyse-2026-06-27.md` that contains:
1. A summary table of extracted terms, their category (AI buzzword, jargon, complexity), and frequency.
2. A comparison check against `claude-guardrails.md` rules.
3. Recommendations for rewriting specific sentences to use simpler language and maintain consistency.

## Acceptance Criteria

### Execution & Deliverables
- [ ] The Python analysis script is created and saved at the designated scratch path.
- [ ] The script executes successfully and outputs the frequency data.
- [ ] The markdown report at `docs/reference/vibs-verified-språkanalyse-2026-06-27.md` is successfully created.
- [ ] No changes are made to the analyzed source documents.

### Report Quality & Recommendations
- [ ] The report contains a clear table showing word frequencies for tech and jargon keywords.
- [ ] The report explicitly flags occurrences of AI buzzwords or complex jargon that violate the project's simple language guidelines.
- [ ] Concrete "Before/After" rewrite recommendations are provided for complex passages.

## Verification
- An independent auditor agent will run the python script to verify that it functions correctly and outputs the frequency list.
- The auditor will review the generated report to confirm it addresses all requirements and contains actionable recommendations.
