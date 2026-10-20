---
name: soknadsteam
description: Kritisk, sporbar gjennomgang av VERIFIED IPN og et separat lite FoU-/Koblingsboks-utkast. Gir redlines, ikke bare spørsmål. Krever menneskelig godkjenning.
---

# Søknadsteam for VIBS / VERIFIED

Start med AGENTS.md, CONTEXT.md, INDEX.yml og docs/agents/soknadsteam/README.md. Be om eksplisitt valgt søknadsfil når INDEX og CONTEXT er uenige. Bruk docs/agents/soknadsteam/ROLLER.md som rollebrief og FUNNFORMAT.md som utkontrakt.

Gjenbruk skills/grill-me-verified for kritiske spørsmål og docs/agents/intake-outtake.md for research/proveniens. Denne skillen skal levere konkrete forslag: originalsted, problem, presis erstatningstekst, evidens, prioritet, eier og aksepttest.

Kjør ikke «fem agenter» ved å late som om én modell har gjort fem uavhengige kjøringer. Bruk reelle separate kjøringer og uavhengig red team, eller merk rollene NOT_RUN. Ikke endre aktiv søknad, INDEX, kildedom, Source Guard eller partnerstatus. Ikke send eksternt.

Praktisk start: python tools/soknadsteam.py init --repo . --application-file <valgt-fil> --run-id <id>. Fullfør rollenes JSON-output; kjør validate og report. Alle utkast og kjøringer er ikke-godkjente frem til beslutningseier har vurdert dem.
