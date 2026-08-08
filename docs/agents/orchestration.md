# Orkestreringsmodell

Hvordan arbeid drives over tid i `ipn-verified`. Bygger på rollene og ærlighetsregelen i `AGENTS.md`.

## To kontrollplan (viktig skille)

```
                    Lars (orkestrator / godkjenner)
                              │
                ┌─────────────┴──────────────┐
        STYRBART av Claude            IKKE styrbart av Claude
                │                              │
        Claude-subagenter              Codex / Antigravity (AGY)
        (Agent-verktøyet)              via handoff-filer i VS Code
        breddearbeid, research, QA     utførelse: kode, retting, verifisering
```

- **Claude kan kun styre Claude-subagenter.** Codex/AGY får **handoff-filer** (copy-paste) — Claude
  later aldri som om den styrer dem, og spiller aldri rollen «Codex/AGY-agent». (Ærlighetsregel.)
- **Sonar** er et faktasjekk-*verktøy* (loopback-API), ikke en agent.

## Claude-subagenter — når og hvilke

Bruk subagenter til **bredde, research og QA** — ikke til arbeid Lars skal lære/gjøre selv.

| Behov | Subagent / skill | Merk |
|---|---|---|
| Kartlegge repo / finne ting | `Explore` | Read-only, rask fan-out |
| Forstå hvordan noe henger sammen | `codebase-explorer` / `zoom-out` | Modulkart, dataflyt |
| Uavhengig kvalitets-/sikkerhetsreview | `code-reviewer` / `/code-review` | Før noe regnes som ferdig |
| Web-research / kildeverifisering | `sonar-search` | Åpen sitering, audit trail |
| Systematisk feilsøking | `debugger` / `/diagnose` | Reproduser før endring |
| Planlegge implementasjon | `Plan` | Returnerer stegplan |

Mønsteret finnes allerede i `provenance/agents/` (auditor, challengers, explorers, reviewers,
orchestrator, sentinel) — gjenbruk strukturen `BRIEFING.md` + `progress.md` + domeneoutput ved
større kjøringer.

For research-intake, kilde-/konkurrentavstemming, SINTEF-pakker og kontrollert
outtake gjelder den varige rollemodellen i `docs/agents/intake-outtake.md`.
Aktive run-artefakter og mottakerutkast skal ligge under `.scratch`, ikke i
kanoniske kilde- eller søknadsfiler.

> Flere agenter gir **bredde**, ikke automatisk **sannhet**. Verifiser funn; ikke behandl
> agent-konsensus som belegg (jf. kildereglene).

## Handoffs til Codex / AGY

Når noe skal **utføres** i VS Code (kode, retting, verifisering), lag en handoff-fil:

- Plassering: `docs/handoffs/NN_<kort_slug>_handoff.md` (neste ledige nummer; siste er 35 → bruk 36+).
- Format: bruk `docs/handoffs/handoff-template.md`.
- Startprompt skal referere **faktisk sti** til handoff-filen (eldre filer kan ha utdaterte stier
  fra migreringen — ikke kopier de stiene).
- Bruk `handoff`-skillen til å generere den; pek til artefakter i repoet i stedet for å kopiere
  store blokker.

## Rolledeling

| Rolle | Ansvar |
|---|---|
| **Lars** | Orkestrator, beslutter, godkjenner. Avgjør grensetilfeller. |
| **Claude** | Drafting, review, research, handoff-generering. Styrer Claude-subagenter. |
| **Codex / AGY** | Utførende i VS Code. Leser handoff-filer. |
| **Sonar** | Faktasjekk-verktøy (ikke agent). |
| **SINTEF** | Primærverifiserer vitenskapelige kilder (fra midten av august 2026). |

## Beslutning: subagent, handoff, eller selv?

| Situasjon | Velg |
|---|---|
| Trenger bredde/research/QA *nå*, innenfor Claude | **Claude-subagent** |
| Noe skal utføres/redigeres i VS Code av Codex/AGY | **Handoff-fil** |
| Lars skal lære / gjøre selv (f.eks. håndkode `site/`) | **Verken** — Claude forklarer + reviewer |
| Irreversibel endring, grensetilfelle, kildedom | **Til Lars** for beslutning |
