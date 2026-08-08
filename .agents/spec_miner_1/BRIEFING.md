# BRIEFING — 2026-08-02T22:54:43Z

## Mission
Perform specification mining for VERIFIED IPN research status report (State of the Art), extracting authoritative specifications, methodologies, regulatory framework, financial links, tool feature matrix, and ontology rules.

## 🔒 My Identity
- Archetype: Specification Miner
- Roles: Spec Miner
- Working directory: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\spec_miner_1
- Original parent: 809995f2-86c3-44bf-831f-2d3b16c9ca10
- Milestone: Specification Mining for SoA v0.5

## 🔒 Key Constraints
- Read-only on codebase/project files (write only to .agents/spec_miner_1/).
- Follow term rules in vibs-verified-ord-og-kildekart-v0.5.yml (løsningsvalg, testflate, no black box, preserve parked sources with ⏸, distinguish EBA_EU2023 vs EBA_NO2023, etc.).
- Never make absolute gap claims ("no tools exist") without scope boundaries.
- Mine authoritative specifications for all 5 domains + 6-axis matrix.

## Current Parent
- Conversation ID: 809995f2-86c3-44bf-831f-2d3b16c9ca10
- Updated: 2026-08-02T22:54:43Z

## Task Summary
- **What to build**: Extract and document spec into `spec.md` and `handoff.md`.
- **Success criteria**: Comprehensive, evidence-based spec mining covering all 5 requested domain topics, ontology rules, source statuses, edge cases, and 6-axis feature matrix.
- **Interface contracts**: `docs/reference/vibs-verified-kildedom-2026-06-27.md`, `docs/reference/ipn-kildebibliotek.md`, `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`, `research/evidence_matrix.md`.
- **Code layout**: N/A (read-only spec mining agent).

## Key Decisions Made
- Mining directly from canonical reference documents and evidence matrix in project repo.

## Artifact Index
- `.agents/spec_miner_1/DISPATCH.md` — Task dispatch instructions.
- `.agents/spec_miner_1/BRIEFING.md` — Agent working memory.
- `.agents/spec_miner_1/spec.md` — Comprehensive specification mining output.
- `.agents/spec_miner_1/handoff.md` — Handoff report with verification method.
