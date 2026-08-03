---
title: Handoff (AGY) - forslag til ord- og kildekart v0.5
date: 2026-08-02
status: ready-for-human
from: codex
to: antigravity (AGY)
branch: change/tekstpresisering-v0.5
tags: [vibs, verified, ipn, v0.5, terminology, sources, read-only]
---

# Handoff (AGY): foreslå ord- og kildekart for v0.5

## Bestilling

Gjennomfør en helt skrivebeskyttet kontroll av prosjektets dokumentroller, ordbruk og kildeporter. Foreslå innholdet til en framtidig fil med arbeidsnavnet:

`docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`

Returner YAML-forslaget direkte i AGY-svaret. Ikke opprett, endre, flytt eller slett filer.

## Les først

- `AGENTS.md`
- `CONTEXT.md`
- `INDEX.yml`
- `docs/agents/domain.md`
- `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.5.md`
- `docs/reference/prosjektbeskrivelse/sannhetsserum-oppdatering-v0.5.md`
- `docs/reference/prosjektbeskrivelse/arbeidsversjoner/HANDOFF-godkjent-review-k1-k4-v1-v3-2026-07-25.md`
- `docs/reference/ipn-kildebibliotek.md`
- `docs/reference/vibs-verified-kildedom-2026-06-27.md`
- `docs/reference/state-of-the-art-verified-ipn.md`
- `research/evidence_matrix.md`

## YAML-forslaget skal kartlegge

1. Aktiv status: `v0.4` som låst baseline og `v0.5` som aktiv K/V-kandidat, ikke innsendingsklar hovedtekst.
2. Dokumentroller: kanonisk, baseline, kandidat, review, kildekontroll, research-intake og historikk.
3. Godkjent ordbruk, blant annet `løsningsvalg`, `alternativer`, `beslutningsstøtte`, `usikkerhet` og `teknisk risiko`.
4. Ord og formuleringer som skal unngås, med anbefalt erstatning og begrunnelse.
5. Kildeporter og provenans: primær, sekundær og konsortie-intern samt grønn, gul, rød og parkert status.
6. Kilder og gamle nøkler som er tatt ut, parkert eller korrigert, uten å slette historikken.
7. Kontrollregler for framtidig kildebruk og vurdering av state of the art.
8. Åpne konflikter som må avgjøres av Lars eller primærverifiseres av SINTEF.

## Viktige avgrensninger

- Ikke endre noen filer, heller ikke `.scratch`.
- Ikke oppgradere eller nedgradere kildestatus.
- Ikke omskrive søknadsteksten.
- Ikke utføre ny nettbasert forskning i denne oppgaven.
- Ikke behandle agentkonsensus som belegg.
- Ikke gjøre historiske dokumenter gjeldende igjen.
- Ikke sende noe eksternt.

## Leveranse i AGY-svaret

Svaret skal inneholde:

1. En kort dom over om prosjektets ordbruk og dokumentroller er konsistente.
2. Ett komplett YAML-forslag i en kodeblokk.
3. En avviksliste med fil, uttrykk eller nøkkel, observert problem og anbefalt behandling.
4. En tydelig liste over forhold AGY ikke kunne avgjøre.

YAML-forslaget er kun et forslag. Codex kontrollerer det mot repoet, og Lars godkjenner før eventuell opprettelse.

## Startprompt til Antigravity

```text
Les docs/handoffs/38_agy_ord-og-kildekart-v0.5_read-only_handoff.md og følg den ordrett.

Arbeid helt read-only. Returner et komplett forslag til vibs-verified-ord-og-kildekart-v0.5.yml direkte i svaret, sammen med kort dom, avviksliste og åpne spørsmål. Ikke opprett eller endre noen filer, ikke gjør ny nettresearch og ikke endre kildestatus.
```
