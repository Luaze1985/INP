# Project: VIBS VERIFIED IPN State of the Art Research Report

## Architecture
Target Document: `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`
The report synthesizes scientific literature, regulatory frameworks, empirical financial data, LCA/LCC standards, decision methodology, and commercial software analyses into a comprehensive State of the Art document for SINTEF evaluation.

## Feature Inventory
| # | Feature / Topic | Description | Milestone | Source |
|---|----------------|-------------|-----------|--------|
| 1 | Source Gate Verification | Verify canonical source list, gate status tags (🟢, 🟡, ⏸, 🔴), EBA separation, parked sources | M1 | R1 |
| 2 | Terminology Guardrails | Enforce "løsningsvalg", "testflate", "beslutningsstøtte", forbid black box & auto-select | M1 | R3 |
| 3 | LCA/LCC Standards | EN 15978:2026, NS-EN 16627, ISO 14040/14044/15686-5 (NS 3454 withdrawn Sept 2023) | M2 | R2 §2 |
| 4 | 70% A1-A3 Dominance | Multiconsult/DiBK 2023 summary p. 3 across 4 reference buildings | M2 | R2 §2 |
| 5 | TEK17 1.25 Factor | 25% markup on generic EPD data per Norwegian TEK17 guidance | M2 | R2 §2 |
| 6 | Weidema Pedigree Matrix | 5 DQIs driving Monte Carlo lognormal variance in ecoinvent (1996/2016) | M2 | R2 §2 |
| 7 | Edelen & Ingwersen DQI | Fitness-for-purpose DQI framework without hiding uncertainty in total score (2018) | M2 | R2 §2 |
| 8 | Mecca 2023 Review | MCDA distribution in construction: AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9% | M3 | R2 §3 |
| 9 | Visible Uncertainty | Lohman DMsan 2023 & EC3 visible confidence intervals and opportunity space | M3 | R2 §3 |
| 10 | Rank Reversal Reservation | Methodological reservation for TOPSIS/COPRAS/VIKOR without claiming final proof | M3 | R2 §3 |
| 11 | Empirical Energy-PD Link | Kaza 2014 (~32% residential ENERGY STAR), Billio 2022 (Dutch EPC), An 2020 (34% CMBS) | M4 | R2 §4 |
| 12 | Banking & Prudential Regs | EBA EU 2023 (green loans), BoE PS25/25 (June 2026 climate deadline), BoE DP1/25 (IRB limits) | M4 | R2 §4 |
| 13 | EBA Entity Separation | Strictly separate EBA EU 2023 (banking) and EBA NO 2023 (building guide) | M4 | R3 |
| 14 | Durability-to-PD FoU Gap | Explicit research gap: zero empirical literature linking durability/moisture to credit risk | M4 | R2 §4 |
| 15 | Nordic Council 2023 | Norwegian LCA rules flexibility for SME competitiveness | M5 | R2 §5 |
| 16 | BKA2 SINTEF Project | BKA2 sustainable procurement phase 2 project (SINTEF / Vegard Knotten 11.7 MNOK) | M5 | R2 §5 |
| 17 | SmartKalk Miljø | Tender calculation + EPD/NOBB integration (rebutting price-only tool claim) | M5 | R2 §5 |
| 18 | Reduzer | Tender carbon optimization tool (15k EPDs, carbon-only) | M5 | R2 §5 |
| 19 | Concular | Material circularity, reuse catalog, guarantee framework | M5 | R2 §5 |
| 20 | ORIS | Infrastructure sustainability, transport LCA, manual input | M5 | R2 §5 |
| 21 | SINTEF Summary | Section 1 Executive summary & main conclusions for SINTEF evaluation | M6 | R2 §1 |
| 22 | 6-Axis Comparison Matrix | Section 6 synthesized 6-axis matrix (Integration, Phase, User, Uncertainty, Effect, DNSH) | M6 | R2 §6 |
| 23 | VERIFIED Bounded FoU Gap | Section 6 integrated explainable test surface in offer phase for Norwegian SMEs | M6 | R2 §6 |
| 24 | Final Assembly & Gate Verification | Complete candidate document at target path; Reviewer & Auditor gate approval | M6 | R1-R3 |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Source & Evidence Verification | Survey canonical sources, gate status tags, term rules, EBA disambiguation | none | DONE |
| 2 | Section 2: Methodological Foundation | Draft Section 2 (LCA/LCC, DQI, TEK17 1.25, 70% A1-A3, EN 15978:2026, ISO standards) | M1 | DONE |
| 3 | Section 3: MCDA & Uncertainty | Draft Section 3 (Mecca 2023, visible uncertainty, Rank Reversal reservation) | M1 | DONE |
| 4 | Section 4: Financial & Regulatory | Draft Section 4 (Billio, Kaza, An, EBA EU vs NO, BoE PS25/25 & DP1/25, FoU PD gap) | M1 | DONE |
| 5 | Section 5: SME Context & Tools | Draft Section 5 (Nordic Council 2023, BKA2 11.7 MNOK, SmartKalk, Reduzer, Concular, ORIS) | M1 | DONE |
| 6 | Assembly, Synthesis & Gate Check | Sections 1 & 6, 6-axis matrix, final document assembly & Reviewer/Auditor gate | M2, M3, M4, M5 | DONE |

## Code Layout & Deliverables
- Target Report: `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`
- Draft Sections Directory: `.agents/orchestrator/sections/`
- Gate Status: `.agents/orchestrator/GATE_STATUS.md`
