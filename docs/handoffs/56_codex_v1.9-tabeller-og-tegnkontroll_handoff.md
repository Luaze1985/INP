---
title: Handoff (CODEX) - Gjenopprett tabeller i v1.9 og kontroller tegngrenser
date: 2026-09-16
status: completed
from: claude
to: codex
branch: codex/partneroppgaver-v1-7
tags: [vibs, verified, ipn, soknadstekst, v1.9, tabeller, tegngrenser]
---

# Handoff (CODEX): Gjenopprett tabeller i v1.9 og kontroller tegngrenser

## Kort beskjed

`docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.9.md` har sju steder der en tabell fra v1.7/v4.0 ble skrevet om til punktliste, fordi portalfeltene (jf. `innsendingspakker/v2.0/portalstruktur.json`) bare er registrert som type «tekstfelt». Lars vil ha tabellene tilbake i `.md`-filen for lesbarhet. Din jobb er å gjenopprette dem som ekte Markdown-tabeller **uten å endre tall eller innhold**, og kontrollere at ingen felt sprenger portalens tegngrense. Ikke din jobb: å vurdere om innholdet er riktig, eller å hente inn nye tall.

**Utført 2026-09-16:** De sju tabellene er gjenopprettet. Tegntellingen er oppdatert; alle berørte felt er innenfor portalenes grenser. Word-filen er generert på nytt, Source Guard passerte, og testgaten passerte. Lars ba deretter om at den validerte pakken committes.

## Rollefordeling (ærlighetsregel)

- **Codex (deg):** gjenoppretter tabellene, oppdaterer tegntellingen bakerst i filen, regenererer `.docx`, kjører Source Guard, rapporterer tilbake.
- **Claude:** skrev denne handoffen og v1.8/v1.9. Styrer deg ikke direkte.
- **Lars Erik:** avgjør om et felt som sprenger grensen skal kortes, eller om tabellen heller skal holdes som liste i akkurat det feltet.

## Inndata (les for kontekst)

- `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.9.md` — filen du redigerer. **Ikke rør `v1.8.md`** — den er en frosset mellomversjon (se `INDEX.yml`).
- `docs/reference/prosjektbeskrivelse/innsendingspakker/v2.0/feltkart.md` og `portalstruktur.json` — tegngrenser og feltyper (alle copy-paste-klare felt er type «tekstfelt», ikke rik tekst).
- `AGENTS.md` — kilde- og sannhetsregler (uendret av dette arbeidet).
- `docs/agents/domain.md` — domenedokumenter og vokabular.

## Det du skal levere

Gjenopprett disse sju punktlistene som Markdown-tabeller, med **samme innhold og tall**, bare i tabellform. Foreslåtte kolonner i parentes — du kan justere retning (rader/kolonner) hvis det gir en klarere tabell, men ikke fjern eller legg til opplysninger.

1. **Måleplan** (i «FoU-metoder og -aktiviteter», avsnittet som starter «Måleplan. AP1 gjør...»). Kolonner: Målepunkt | Sammenligningsgrunnlag og kilde | Når/ansvar | Beslutningsport.
2. **Fra dagens arbeidsflyt til VERIFIED** (i «Innovasjonen»). Kolonner: Dagens arbeidsflyt | VERIFIED etter prosjektet.
3. **Gevinst for samarbeidspartnerne** (i «Verdiskapingspotensial», avsnittet «Gevinst for samarbeidspartnerne...»). Kolonner: Aktør | Resultatbruk.
4. **Regneeksempel lavt/basis/høyt** (samme seksjon, rett under). Sett scenarioene (Lavt/Basis/Høyt) som kolonner og kunder/inntekt/dekningsbidrag/resultat som rader, eller omvendt — velg det som blir mest lesbart.
5. **Seks adskilte ledd** (samme seksjon, «Den økonomiske hypotesen skal vurderes som seks adskilte ledd»). Kolonner: Ledd | Hva som må vises | Ikke tilstrekkelig alene.
6. **Foreløpig kostnadsfordeling** (i «Styring og roller»). Kolonner: Aktør | Prosjektkostnad | Søkt støtte | Egenfinansiering. Husk summeraden (16,0 / 8,0 / 8,0 MNOK).
7. **Risiko** (seksjonen «Risiko»). Kolonner: Risiko | S/K | Tidlig indikator | Tiltak | Eier.

Etter gjenopprettingen:

8. **Regn tegn på nytt** for feltene som fikk en tabell, spesielt «FoU-metoder og -aktiviteter» og «Verdiskapingspotensial» (grense 5000 hver — de lå på hhv. ~4600 og ~4300 tegn med punktlister, så tabellsyntaks kan sprenge grensen). Tell tegn **uten** `<span style="color:red">`-markering og uten Markdown-tegnene selv hvis portalen bare tar ren tekst — se hvordan «Tegntelling per portalfelt» bakerst i filen er regnet ut, og oppdater den tabellen med de nye tallene.
9. Hvis et felt havner **over** grensen: ikke kort innholdet selv. Merk feltet `OVER` i tegntellingen og skriv en kort merknad i handoff-svaret om hvilket felt og hvor mye det må ned. Lars avgjør kuttet.
10. **Regenerer `.docx`** fra den oppdaterte `.md`-filen (samme metode som brukt for v1.8/v1.9 — rød tekst for det som er markert med `<span style="color:red">`, resten svart).
11. **Kjør Source Guard:**
    ```powershell
    python tools/source_guard.py scan --path docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.9.md --report .scratch/sg-v1.9-tabeller.json
    ```
    Skal gi `PASS hits=0`. Hvis ikke: stopp og rapporter, ikke fjern treffet selv.

## Ikke-mål

- Ikke rør `v1.7-if-only.md` eller `v1.8.md`.
- Ikke legg til, fjern eller omformuler faktapåstander — bare formatendring.
- Ikke flytt Source Guard sin `active_paths`/`guarded_paths` (`governance/source-blocklist.json`) — det krever egen beslutning fra Lars.
- Ikke commit. Legg fram diff for Lars.
- Ikke bruk egen kunnskap som belegg — kun åpen sitering (jf. `AGENTS.md`).

## Akseptansekriterier

1. Alle sju punktlistene er erstattet med Markdown-tabeller med identisk innhold (kontroller mot denne handoffen og mot git-diff at ingen tall er endret).
2. `.md`, `.docx` og tegntellingen bakerst i filen er konsistente med hverandre.
3. Source Guard gir `PASS hits=0` på v1.9 etter endringen.
4. Ethvert felt som havner over tegngrensen er merket `OVER` og rapportert, ikke stille korrigert.
5. `v1.7-if-only.md` og `v1.8.md` er urørt (`git status` viser bare `v1.9.md`, `v1.9.docx` og eventuelt `.scratch/sg-v1.9-tabeller.json`).

## Startprompt (lim inn til Codex i VS Code)

```text
Les docs/handoffs/56_codex_v1.9-tabeller-og-tegnkontroll_handoff.md.

Gjenopprett de sju punktlistene i docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.9.md
som Markdown-tabeller (måleplan, arbeidsflyt-før/etter, partnergevinst, regneeksempel,
seks adskilte ledd, kostnadsfordeling, risiko), uten å endre tall eller påstander. Regn tegn
på nytt for "FoU-metoder og -aktiviteter" og "Verdiskapingspotensial" mot 5000-tegnsgrensen,
oppdater tegntellingen bakerst i filen, regenerer .docx, og kjør
python tools/source_guard.py scan --path docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.9.md.
Ikke rør v1.7 eller v1.8. Ikke commit.
```
