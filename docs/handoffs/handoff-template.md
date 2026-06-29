---
title: Handoff (<CODEX|AGY>) - <kort tittel>
date: <ÅÅÅÅ-MM-DD>
status: ready
from: claude
to: <codex | antigravity (AGY)>
branch: <branch eller "main">
tags: [vibs, verified, ipn, <tema>]
---

# Handoff (<CODEX|AGY>): <hva som skal gjøres>

## Kort beskjed

<1–3 setninger: hva, og hva som IKKE er din jobb (avgrens skarpt).>

## Rollefordeling (ærlighetsregel)

- **<CODEX|AGY> (deg):** <hva du gjør>.
- **Claude:** skrev denne handoffen. Styrer deg ikke direkte.
- **Lars Erik:** avgjør grensetilfellene du flagger.
- <evt. neste agent i kjeden og hva de gjør etterpå.>

## Inndata (les for kontekst)

- `<sti til relevant fil>` — <hva den er>
- `docs/agents/domain.md` — domenedokumenter og vokabular
- <bindende fasit hvis relevant, f.eks. utlysningstall>

## Det du skal levere

1. <konkret artefakt + hvor den skrives>
2. <…>

## Ikke-mål

- <hva du IKKE skal røre — f.eks. kanoniske dokumenter, betalingsmur-kilder>
- Ikke bruk egen kunnskap som belegg — kun åpen sitering (jf. `AGENTS.md`).

## Akseptansekriterier

1. <målbart kriterium>
2. <…>

## Startprompt (lim inn til <CODEX|AGY> i VS Code)

```text
Les <faktisk-sti-til-denne-handoffen>.

<2–4 setninger som gjentar oppgaven selvstendig, slik at den kan limes inn
uten ekstra kontekst. Referer faktiske filstier i repoet.>
```
