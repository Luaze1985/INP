# plan.md — Vibs IPN Source Verdict Reconciliation

## Architecture / Overview
This plan coordinates the reconciliation of four conflicting source verification reports for the Vibs IPN project, resolving key contradictions, and producing a unified source verdict document `docs/reference/vibs-verified-kildedom-2026-06-27.md` without modifying canonical files.

## Requirements Checklist
- **R1**: Reconcile 4 source verification reports from 2026-06-26.
- **R2**: Resolve 6 known contradictions (An/Billio/Kaza, Vannskadetall, Wiik 2025, Harerusten 2022, IPN Amount, Mecca 2023).
- **R3**: Prioritize Norwegian/European sources.
- **R4**: Output unified source verdict at `docs/reference/vibs-verified-kildedom-2026-06-27.md` with judgment table, removal list, correction list, and boundary cases.
- **R5**: No modifications to the three canonical source documents.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Exploration & Analysis | Run Explorer agents to analyze the 4 reports and truth serum, and define the synthesis strategy. | None | DONE |
| 2 | Implementation | Spawn Worker agent to write the unified source verdict document `docs/reference/vibs-verified-kildedom-2026-06-27.md`. | M1 | DONE |
| 3 | Review & Verification | Run Reviewer, Challenger, and Auditor agents to check correctness, alignment with requirements, and integrity. | M2 | DONE |
| 4 | Final Handoff | Update progress, compile final handoff, and report to Sentinel. | M3 | DONE |

## Interface Contracts
- **Input files**:
  - `docs/reference/vibs-verified-agentsøk-2026-06-26.md`
  - `docs/reference/vibs-verified-agentverifisering-2026-06-26.md`
  - `docs/reference/vibs-verified-full-kildesjekk-2026-06-26.md`
  - `docs/reference/vibs-verified-sonar-2026-06-26.md`
  - `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md`
- **Output files**:
  - `docs/reference/vibs-verified-kildedom-2026-06-27.md`
