---
title: Handoff (Codex) - agentisk intake, outtake og SINTEF-forberedelse
date: 2026-08-03
status: ready-for-human
from: codex
to: codex
tags: [vibs, verified, ipn, agents, intake, outtake, sintef]
neste_ledige_handoff: 43
---

# Handoff: viderefør agentisk intake/outtake og SINTEF-pakke

## Mål for neste sesjon

Bruk den nye agentpakken til å føre dagens Perplexity-, kilde- og
konkurrentfunn videre til avstemt intern kontekst, SINTEF-utkast og et senere
tørrkjøringskart. Ikke endre søknadstekst, kildeporter eller produktkode i
denne fasen.

## Les først

- `AGENTS.md`
- `CONTEXT.md`
- `.scratch/agent-intake-outtake-2026-08/README.md`
- `.scratch/agent-intake-outtake-2026-08/agentroster-utkast.md`
- `.scratch/agent-intake-outtake-2026-08/intake-pipeline-utkast.md`
- `.scratch/agent-intake-outtake-2026-08/sintef-outtake-utkast.md`
- `.scratch/agent-intake-outtake-2026-08/internal/00-intern-status-2026-08-03.md`
- `.scratch/kilde-og-konkurrentkonsolidering-2026-08/funn-perplexity-kilder-2026-08-03.md`
- `.scratch/kilde-og-konkurrentkonsolidering-2026-08/funn-perplexity-konkurrenter-2026-08-03.md`

## Det som er opprettet

- Ni varige roller, A0–A8, med avgrenset skriveeierskap og stoppregler.
- Batchbasert intake med integritet, proveniens, sannhetsskille, repoavstemming,
  QA og menneskelig godkjenning.
- Separat internt notatspor og SINTEF-outtake.
- SINTEF `draft-01` med mottakerintroduksjon, 15 hovedspørsmål, svarmal og
  godkjenningsport.
- Korte startprompter for alle rollene.

Tre subagenter utarbeidet henholdsvis agentroster, intake-pipeline og
SINTEF-outtake. Artefaktene er arbeidsgrunnlag og ikke faglig belegg.

## Viktig ny kontroll

Den gamle `.agents`-orkestreringen rapporterte full konsistens og ingen åpne
beslutninger. Perplexity-kontrollen viser senere kildeblandinger, overstrekk og
ufullstendig konkurrentdekning. Gamle `APPROVE`, `CLEAN` og `VICTORY` beholdes
som historikk, men skal ikke brukes som gjeldende faglig godkjenning.

## Anbefalt neste kjøring

1. Start A0 med et nytt `run-id`.
2. Kjør A1 på dagens komplette Perplexity-leveranse. Ikke be Lars om flere
   eksporter; manglende original registreres som `NEEDS-ORIGINAL`.
3. Kjør A2, A3 og A5 parallelt.
4. Kjør A4 når de tre avstemmingene er ferdige.
5. Bygg A6-utkast til SINTEF og A7-tørrkjøring parallelt.
6. Kjør uavhengig A8-audit.
7. Stopp ved Lars' godkjenningsport.

## Ikke-mål

- Ikke kjør nye nettsøk uten egen godkjent research-oppgave.
- Ikke endre `v0.4`, `v0.5`, kanoniske K/V-filer eller produktkode.
- Ikke endre, pensjoner eller slett kilder.
- Ikke sende noe til SINTEF.
- Ikke gjøre `.scratch` til en ny autoritativ kildedatabase.

## Foreslåtte skills

- `wayfinder` for én avgrenset beslutning eller ticket per sesjon.
- `handoff` når et ferdig kontrollert run skal overleveres.
- `code-review` for uavhengig audit av faktisk diff og styringsregler.
- `ai-sprakvask-no` før SINTEF-pakken klargjøres for ekstern leser.
- `sonar-search` bare dersom Lars senere godkjenner nye eksterne søk.

## Startprompt

```text
Les docs/handoffs/42_codex_agentisk_intake_outtake_og_sintef-forberedelse_handoff.md
og .scratch/agent-intake-outtake-2026-08/README.md.

Start et avgrenset A0/A1-run for dagens komplette Perplexity-leveranse. Bruk
rolle- og filkontraktene i agentpakken. Ikke be om flere Perplexity-filer, ikke
endre søknadstekst eller kildeporter, og ikke send noe til SINTEF. Stopp etter
A1 dersom inntaket ikke kan rutes uten gjetning; ellers rapporter klar frontier
for A2, A3 og A5.
```
