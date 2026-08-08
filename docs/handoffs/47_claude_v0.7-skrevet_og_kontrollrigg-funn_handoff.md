---
title: Handoff (Claude) – v0.7 skrevet, beslutningsporten lukket, funn i kontrollriggen
handoff_nr: 47
date: 2026-08-05
status: v0.7-utkast-klar-for-finredigering
from: claude-code (Opus 5)
to: claude
branch: change/tekstpresisering-v0.5
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
neste_ledige_handoff: 48
---

# Handoff #47 – v0.7 er skrevet, Lars finredigerer

## Hva som skjedde

Lars åpnet med `/grill-with-docs` på de fire åpne v0.6-beslutningene, og endret
underveis mandatet til: «Du skal bare skrive ny søknad. Og som jeg skal
finredigere fra dispatch.» Partnerprosessen (F-32/33/34) ble dermed lagt bort i
denne sesjonen.

## Beslutninger Lars tok

| ID | Beslutning | Konsekvens |
| --- | --- | --- |
| F-03 | Kun uformell interesse foreligger | Sammendraget beholder partnertyper uten navn. Ingen diff |
| F-21 | 12.5 slås fast som sekundært bærekraftsmål | Diff B-01 i V1 |
| F-28 | V3-overskriften beholdes | Ingen diff. Premisset i tilbakemeldingen var utdatert |
| F-32/33/34 | Utsatt | Ikke behandlet. Lars prioriterte søknadsteksten |

### Grunnlaget for F-28, så den ikke gjenåpnes

Overskriften «Økonomiske virkninger og bankrelevans» er forankret tre steder: den
godkjente arbeidsversjonen `arbeidsversjoner/v3-okonomiske-virkninger-bankrelevans-godkjent-v0.1.md`
(2026-07-25), ord- og kildekartets tekstgrunnlag for v0.5, og sannhetsserumets
§10-tabell. `v3-okonomi.md` sier «bank er en virkning, ikke et eget sidespor», noe
som isolert taler mot – men den filen er merket «første røffe utkast» og er eldre
enn den godkjente arbeidsversjonen.

## Nye rader i styringsregisteret

- **F-35 – kjønnsperspektiv.** Eget delpunkt under vurderingskriteriet Kvalitet
  (`ipn-barekraft-sannhetsserum-2026-06-21.md` §10.7) og rangeringshensyn i §10.5.
  Fantes ikke i søknadsteksten i det hele tatt. Besvart i v0.7 som B-03.
- **F-36 – økonomisk mekanisme i V3.** Delpunktet «Økonomiske gevinster for
  bedriftene» under Effekter. V3 beskrev hva som skulle måles, aldri hvilken
  mekanisme gevinsten går gjennom. Besvart i v0.7 som B-02.

## Partisjonskonflikt som ble avgjort

Registerets §4 holdt «ekstra bærekraftsmål» utenfor v0.6-passet, mens handoff #46
listet F-21 som en v0.6-blokkering. Radstatusen avgjorde: F-21 hadde
`KREVER BESLUTNING`, ikke `PARKERT TIL v0.7`. §4-linjen er strøket med begrunnelse
i registeret, og avgjørelsen er skrevet ned i resultatrapportens seksjon 4.

## Nøkkelartefakter

- **Ny målfil:** `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.7.md`
- **Kontrollstatus v0.7:** `docs/reference/prosjektbeskrivelse/reviews/2026-08-05-v0.7-kontrollstatus.md`
- **Styringsregister (oppdatert, F-35/F-36 lagt til):** `.../reviews/2026-08-05-tilbakemeldingsregister-v0.6.md`
- **Resultatrapport (oppdatert, seksjon 2c og 4):** `.../reviews/2026-08-05-v0.6-overflatepass-resultat.md`
- **v0.6 bevart urørt** som sendt arbeidsgrunnlag

## Kontrollstatus

Source Guard på målfil `PASS` (0 treff). Alle fem språkportpass rene – ett treff
er en filsti i statusheaderen, ikke søknadsprosa. Testsuite 17 passed, 15
subtests. «skal» redusert fra 61 til 9; K4 fra 16 til 2, V2 fra 15 til 2.

## To funn i kontrollriggen, ikke i teksten

Begge ligger i `governance/source-blocklist.json`, som er `protected_policy_path`
med Lars som `decision_owner`. **Ikke endret.**

1. **Kildeportens stier peker fortsatt på v0.5.** `guarded_paths` og
   `active_paths` nevner ingen v0.6- eller v0.7-fil. Den konfigurerte porten
   dekker ikke den aktive kandidaten – rapporterte `PASS` kom fra eksplisitt
   `--path`-skann.
2. **`scan --active` er BLOCK med 62 treff**, alle i filer som ikke er rørt.
   Pre-commit-hooken kjører `scan --staged`. To blokkerte filer er utrackede og
   ligger i `guarded_paths`; blir de stagede sammen med v0.6/v0.7-pakken, stopper
   hooken commiten.

## Neste steg

1. **Lars finredigerer v0.7 fra dispatch.**
2. Bekreft eller stryk **B-03** – avsnittet binder en rekrutteringspraksis for
   pilotene som konsortiet må kunne gjennomføre.
3. PDF-regenerering av v0.7 etter finredigering. Ikke kjørt.
4. Avklar kildeportens stier før commit, jf. funn 1 og 2.
5. Partnerprosessen F-32/33/34 gjenstår ubehandlet.

## Viktige ikke-mål

- Ikke overskriv v0.6 – den er sendt arbeidsgrunnlag
- Ikke legg til prosentsatser, partnernavn, metodebetegnelse eller arbeidspakker
- Ikke endre kildestatus eller `governance/source-blocklist.json` – kun Lars
- Ikke send materiale til partnere uten Lars' godkjenning

## Startprompt til neste agent

```text
Les docs/handoffs/47_claude_v0.7-skrevet_og_kontrollrigg-funn_handoff.md og
docs/reference/prosjektbeskrivelse/reviews/2026-08-05-v0.7-kontrollstatus.md.
Målfilen er soknadstekst-samlet-kandidat-v0.7.md. Lars finredigerer selv.
Ikke skriv ny prosa uten at han ber om det. Port A, C og F er fortsatt åpne og
krever kilde, faglig eier og bekreftet konsortium.
```
