---
title: Handoff (Codex) — kontroller og godkjenn forslag til vibs-verified-ord-og-kildekart-v0.5.yml
date: 2026-08-02
status: ready-for-codex
from: antigravity (AGY)
to: codex
tags: [vibs, verified, ipn, v0.5, terminology, sources, review]
neste_ledige_handoff: 40
---

# Handoff (Codex): kontroller og godkjenn ord- og kildekart v0.5

## Bakgrunn

AGY gjennomførte handoff 38 — en helt skrivebeskyttet gjennomgang av prosjektets
dokumentroller, ordbruk og kildeporter. Forslaget er returnert i AGY-svaret og lagret
som fil i repoet.

**Foreslått fil:**
`docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`

Filen er et forslag. Den er ikke godkjent.

## Codex sin oppgave

1. **Les** `AGENTS.md`, `CONTEXT.md`, `INDEX.yml` og handoff 38.
2. **Les** forslaget:
   `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`
3. **Kontroller** at:
   - Ingen kildestatus er oppgradert eller nedgradert i forslaget.
   - Ingen historiske dokumenter er gjort gjeldende igjen.
   - Ingen formuleringer i forslaget motsier AGENTS.md eller kildedom-2026-06-27.md.
   - Filstier under `dokumentroller` stemmer med faktiske filer i repoet
     (bruk `git ls-files` eller tilsvarende).
   - Avvikslisten (A-01–A-06) og åpne konflikter (K-01–K-06) er korrekt
     gjengitt og ikke stilnet.
4. **Oppdater `INDEX.yml`** med en linje for den nye filen under `referanse_og_fakta`
   eller en ny seksjon `ordkart`, dersom kontrollen viser at filen er konsistent.
   Eksempeloppføring:
   ```yaml
   docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml: Forslag til ord- og kildekart for v0.5 (AGY, ikke godkjent)
   ```
5. **Rapporter** til Lars med:
   - Hvilke filstier som stemmer / ikke stemmer.
   - Om det er avvik mellom forslaget og AGENTS.md/kildedom/kildebibliotek.
   - En klar anbefaling: godkjenn, revider, eller blokkert.

## Viktige avgrensninger

- Ikke endre kildestatus.
- Ikke omskrive søknadstekst.
- Ikke opprette ny fil — filen er allerede opprettet av AGY.
- Ikke behandle agentkonsensus som belegg.
- Ikke gjøre historiske dokumenter gjeldende igjen.

## Konflikter som krever Lars' avgjørelse (ikke Codex)

Disse sendes videre uavgjort:

| ID | Tema |
|----|------|
| K-01 | SA2018 portstatus: kildedom sier 🟢, kildebibliotek sier ⏸ |
| K-02 | An2020: kan brukes med forbehold for boliglånsrisiko? |
| K-03 | KD2024 ↔ Asplan Viak/DiBK 2024 — samme rapport? |
| K-04 | Omnibus I — substans bekreftet mot OJ/EUR-Lex? |
| K-05 | SMB-definisjon og markedsandel |
| K-06 | Bankens konkrete informasjonsbehov for F5 |

## Ferdig når

- Codex har kontrollert filstier og konsistens.
- Codex har gitt Lars en klar anbefaling.
- INDEX.yml er oppdatert (eller Codex begrunner at det ikke bør gjøres ennå).
- Åpne konflikter K-01–K-06 er formidlet til Lars uten å avgjøre dem.
