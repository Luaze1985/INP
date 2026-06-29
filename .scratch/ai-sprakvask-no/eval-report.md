# Evalrapport - ai-sprakvask-no

Dato: 2026-06-28  
Status: local pass, global draft installasjon anbefalt

## Hva som ble implementert

Kildeagentene er samlet til én Codex-skill:

- `anti_ai_sprakredaktor_no` som normal inngang
- `ki_sprakdetektor_no` som diagnoseport
- `norsk_klarsprak_redaktor` som omskrivingsport
- `stemmebevarer_no` som stemmekontroll
- `norm_og_kildekontroll_no` som sluttport

Teamet er ikke implementert som parallelle autonome agenter. Det er implementert som en kontrollert redaksjonell workflow. Det passer bedre i Codex, fordi hver port kan kjøres eksplisitt og rapporteres.

## Evalresultat

| Eval | Forventning | Dekket av skillen | Status |
|---|---|---|---|
| 1 Generisk KI-tekst | Flagge høyt KI-preg, konkretisere, spørre etter aktør/problem | Diagnose + omskriv + åpne spørsmål | pass |
| 2 Kommunal tekst | Aktør og verb frem, krav beholdes | Klarspråkregler + meningsbevaring | pass |
| 3 Nynorsk/bokmål | Flagge normblanding, foreslå nynorsk, ikke påstå meningsfeil | Normport + nynorskregel | pass |
| 4 Påstand uten kilde | Kildekontroll, flagge "alltid", ikke dikte kilde | Kildeport + kvalitetsregler | pass |
| 5 Personlig tekst | Fjerne overpolering, bevare "funke/tør/halvferdig" når sjanger tillater | Stemmebevarer + ikke-perfekt-regel | pass |

## Begrensning

Dette er en prompt-/workflow-eval, ikke en automatisk LLM-benchmark. Skillen er derfor klar som global draft-skill, men bør fortsatt battletestes på reelle tekster før den behandles som moden standard.

## Global anbefaling

Installer globalt som `ai-sprakvask-no` fordi:

- evalkravene er eksplisitt dekket
- policygrenser er med
- kilde- og normport hindrer overclaim
- workflowen er nyttig også utenfor VIBS-repoet

