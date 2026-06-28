## 2026-06-27T07:04:53Z

You are a Worker Agent.
Working directory: C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass
Your metadata directory is C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/worker_reconciliation

MANDATORY INTEGRITY WARNING:
> DO NOT CHEAT. All implementations must be genuine. DO NOT
> hardcode test results, create dummy/facade implementations, or
> circumvent the intended task. A Forensic Auditor will independently
> verify your work. Integrity violations WILL be detected and your
> work WILL be rejected.

Task:
Reconcile the findings from the Explorer reports and write the final document `docs/reference/vibs-verified-kildedom-2026-06-27.md`.

Refer to the Explorer reports at:
- `C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/explorer_reconciliation_3/analysis.md`
- `C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/explorer_reconciliation_2/analysis.md`
- `C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/explorer_reconciliation_1/analysis.md`
And the truth serum document:
- `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md`

Output File Requirements for `docs/reference/vibs-verified-kildedom-2026-06-27.md`:
1. A consolidated judgment table mapping claims to sources and verification status (🟢 confirmed, 🔴 unconfirmed, ⚠️ error-needs-correction).
2. A removal list (🔴) detailing affected sentences.
3. A correction list (⚠️) detailing before/after metadata and values.
4. A "boundary cases to Lars" list (e.g., Wiik 2025, Harerusten 2022) detailing implications if removed vs. kept.
5. Explicitly resolve the six known contradictions:
   - An/Billio/Kaza: Differentiate as three separate sources with correct DOI, journal, and scope.
   - Vannskadetall: Determine which year's figures (2021 vs. 2023) should apply based on Finans Norge 2023 (~10 damages/hour, ~87,600/year, 5.1B NOK) or 2021 (~78,500 damages).
   - Wiik 2025 (SINTEF Notat 57): Reconcile status (not indexed/unconfirmed) and place in "grensetilfeller til Lars".
   - Harerusten 2022: Reconcile status (not found/unconfirmed) and place in "grensetilfeller til Lars".
   - IPN Amount: Reconcile supporting limits. Use §10 (1-16 million NOK, max 50% support) and correct the erroneous 16-20 million NOK.
   - Mecca 2023: Reconcile metadata (AHP 46% / TOPSIS 20%) and confirm Wiley paywall.
6. Distinguish and preserve the EBA name collision (EBA EU = European Banking Authority vs. EBA NO = Entreprenørforeningen Bygg og Anlegg).

Integrity constraints:
- Do not modify the three canonical documents (`docs/reference/ipn-kildebibliotek.md`, `docs/reference/ipn-samledokument.md`, `docs/reference/ipn-hovedokument.md`).

When done, write a progress report (progress.md) and a handoff report (handoff.md) in your metadata directory, and send a message back to me.
