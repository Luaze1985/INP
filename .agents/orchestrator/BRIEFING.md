# BRIEFING — 2026-08-02T22:54:30Z

## Mission
Lead the team to conduct a sequential review of verified source and evidence data, and prepare a comprehensive State of the Art research report ready for SINTEF evaluation at `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`.

## 🔒 My Identity
- Archetype: teamwork_orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\orchestrator
- Original parent: parent
- Original parent conversation ID: 0d7d2775-cd99-479a-9b25-440fd36aa743

## 🔒 My Workflow
- **Pattern**: Project
- **Scope document**: PROJECT.md
1. **Decompose**:
   - M1: Source & Evidence Consistency Verification (R1)
   - M2: Methodological Foundation & Data Quality (LCA/LCC, DQI, TEK17, EN 15978)
   - M3: MCDA, Uncertainty & Decision Support (Mecca 2023, visible uncertainty, rank reversal)
   - M4: Financial & Regulatory Context (Billio, Kaza, An, EBA EU 2023, BoE PS25/25, BoE DP1/25, credit risk PD)
   - M5: Norwegian SME Context & Tender Decisions (Nordic Council 2023, BKA2, SmartKalk, Reduzer, Concular, ORIS)
   - M6: State of the Art Report Drafting & Verification (6-axis matrix, final synthesis in candidate doc, audit check)
2. **Dispatch & Execute**: Direct / Iterate per milestone
3. **On failure**: Retry -> Replace -> Skip -> Redistribute -> Redesign -> Escalate
4. **Succession**: Spawn count limit 20
- **Work items**:
  1. Source Verification [pending]
  2. Research Report Drafting [pending]
- **Current phase**: 1 (Survey & Assessment)
- **Current focus**: Survey codebase & source documents, decompose project in PROJECT.md

## 🔒 Key Constraints
- NEVER write, modify, or create source code files directly.
- NEVER run build/test commands yourself — require workers to do so.
- NEVER investigate or explore the problem at the code level — dispatch Explorers.
- Use term "løsningsvalg" (not "produktvalg").
- Avoid "VERIFIED velger / anbefaler automatisk" and "svart boks".
- Use "testflate" for VIBS platform.
- Preserve parked sources ([Wiik2025], [SA2018]) with ⏸ status; use [EBA_NO2023] and [KD2024] as primary.
- Strictly distinguish between [EBA_EU2023] (banking) and [EBA_NO2023] (building/DiBK).
- Tag all claims with status (🟢, 🟡, ⏸, 🔴) matching canonical kildedom.

## Current Parent
- Conversation ID: 0d7d2775-cd99-479a-9b25-440fd36aa743
- Updated: not yet

## Key Decisions Made
- Project Orchestrator initialized. Will perform survey by spawning 3 Explorers / Spec Miners to map source files and requirements.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| explorer_1 | teamwork_preview_explorer | Source & Evidence Verification (R1) | completed | 4145d478-bfcb-477a-b8a0-66f8ad8b66e0 |
| explorer_2 | teamwork_preview_explorer | Research Structure & Citations (R2) | completed | 44a5ccd2-ff19-49b4-a957-172d01f532dc |
| spec_miner_1 | teamwork_preview_spec_miner | Domain & Method Spec Mining (R2/R3) | completed | 31caaa7c-4111-4c39-aece-b80f0631fad0 |
| worker_m2 | teamwork_preview_worker | Section 2 Author (LCA/LCC & DQI) | completed | 0fed664d-5f9f-4d30-98a1-e755ef85e061 |
| worker_m3 | teamwork_preview_worker | Section 3 Author (MCDA & Uncertainty) | completed | 16e5feb0-9e2d-48bd-bc6c-cb17a0fdb7fe |
| worker_m4 | teamwork_preview_worker | Section 4 Author (Finance & Regulation) | completed | 294ed0b2-b9f8-44fd-bb2d-806496edb3db |
| worker_m5 | teamwork_preview_worker | Section 5 Author (SME Context & Tools) | completed | 26c95177-f323-4f00-bb84-2f82696ece2f |
| worker_m6 | teamwork_preview_worker | Report Assembly & Synthesis Author | completed | 6257586d-f197-4d6b-b148-7467f57c5f7a |
| reviewer_1 | teamwork_preview_reviewer | Methodological & Scientific Reviewer | running | 09aead2a-32ad-47f0-ab7a-c56d1100f5f0 |
| reviewer_2 | teamwork_preview_reviewer | Ontological & Terminology Reviewer | running | 79e7c5d2-f1ec-4bbb-9a45-d51202df55a5 |
| auditor_1 | teamwork_preview_auditor | Forensic Integrity Auditor | running | 67829e88-b74a-4322-a84c-a442e1fbfcc9 |

## Succession Status
- Succession required: no
- Spawn count: 0 / 20
- Pending subagents: none
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: not started
- Safety timer: none

## Artifact Index
- PROJECT.md — Project scope and milestone decomposition
- plan.md — High-level plan
- progress.md — Liveness & status tracking
- DISPATCH.md — Verbatim task assignment
