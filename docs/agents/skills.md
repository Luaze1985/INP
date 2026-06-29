# Agent skills i ipn-verified

Hvordan Matt Pocock-skillene kobles til arbeidsflyten i dette repoet. Konfig ligger ved siden av:
`issue-tracker.md`, `triage-labels.md`, `domain.md`, `orchestration.md`.

## Arbeidsflyt (idé → ferdig)

```
grill-me / grill-with-docs   →  forankre idé/plan (1–2 spørsmål av gangen)
   ↓
to-prd / write-prd           →  PRD i .scratch/<feature>/PRD.md
   ↓
to-issues / prd-to-issues    →  oppgaver i .scratch/<feature>/issues/NN-*.md
   ↓
triage                       →  sett Status: (se triage-labels.md)
   ↓
tdd / tdd-loop               →  bygg testdrevet (proporsjonalt, se kodeprinsipper)
   ↓
handoff                      →  overlever til Codex/AGY når noe skal utføres i VS Code
```

`zoom-out` (forstå kodeområde) og `improve-codebase-architecture` (rydde teknisk gjeld) brukes ved behov.

## Hvilken skill, når

| Situasjon | Skill | Hvorfor |
|---|---|---|
| Sette opp arbeidsflyt på repoet | `setup-matt-pocock-skills` | Tracker, labels, domenedoks |
| Idé → forankret plan før kode | `grill-me` / `grill-with-docs` | Stress-tester design 1–2 spørsmål av gangen |
| Skrive kravspec | `to-prd` / `write-prd` | PRD med edge cases + out-of-scope |
| Bryte PRD til oppgaver | `to-issues` / `prd-to-issues` | Vertikale skiver, høyrisiko først |
| Vurdere/merke en sak | `triage` | State machine + labels |
| Bygge feature testdrevet | `tdd` / `tdd-loop` | Red → green → refactor |
| Forstå et kodeområde | `zoom-out` | Modulkart + dataflyt før detalj |
| Rydde teknisk gjeld | `improve-codebase-architecture` | 3 refaktorkandidater → RFC |
| Overlevere til Codex/AGY | `handoff` | Kompakt mål/status/neste steg |
| Web-research / faktasjekk | `sonar-search` | Kildeverifisering via Sonar |
| Norsk språkvask / av-KI-fisering | `ai-sprakvask-no` | KI-preg, klarspråk, stemmebevaring og norm-/kildeport |
| Lage ny egen skill | `write-a-skill` | Riktig struktur + progressive disclosure |

## Kodeprinsipper (proporsjonalt anvendt)

Fra global `CLAUDE.md` («Security-first + Red/Green TDD»). Skaler etter risiko:

- **Statisk side (f.eks. `site/`):** full TDD er overkill. Lett variant — valider HTML, sjekk
  a11y/kontrast, test scrollspy-atferd manuelt. Security-first betyr: ingen hemmeligheter i koden,
  varsomhet med eksterne bilde-/skript-kilder, vurder CSP ved publisering, saniter dynamisk tekst.
- **Datakode (f.eks. fremtidig `ipn.sqlite`-lag):** skriv feilende test først (Red), minimal kode
  (Green), refaktorer. Security-tester for input/injection der relevant.
- **Felles:** commit kun når sjekkene er grønne; uavhengig review (Claude `code-reviewer` eller
  Codex) før noe regnes som ferdig.
