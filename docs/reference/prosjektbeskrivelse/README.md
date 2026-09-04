# Prosjektbeskrivelse — VERIFIED / IPN

Sju kapitler, ett dokument hver. Slås sammen til én PDF når utkastet er ferdig.
Opprettet 2026-07-08 (fase 0 i `../ipn-multiagent-workflow-2026-07-08.md`).

## Gjeldende arbeidsretning 2026-09-04

- **Nyeste arbeidskandidat:** `soknadstekst-samlet-kandidat-v1.7-if-only.md`
- **Avgrensning:** industriell forskning i AP1–AP3, 16,0 MNOK kostnad,
  8,0 MNOK søkt støtte og 8,0 MNOK egenfinansiering
- **Partnergrunnlag:**
  `arbeidsversjoner/06-partnerroller-og-bekreftelsesporter-v1.7.md`
- **Budsjett-/aktørgrunnlag:** `../../../budsjett/partneroversikt.md` og
  `../../../budsjett/kalkulator.py`
- **Status:** ikke innsendingsklar. Partnerkandidatene, leverandørtilbudene,
  rettighetene og støtteforutsetningene må bekreftes. Source Guard peker fortsatt
  på v1.5 til en egen flyttebeslutning er tatt.

V1.7 gjør partneroppgavene vurderbare uten å framstille interesse som avtale.
VIBS er prosjektansvarlig; de øvrige navngitte rollene er foreløpige og følger
bekreftelsesportene i partnergrunnlaget.

## Historisk arbeidsgrunnlag

- **Beslutninger og avgrensninger:** `arbeidsversjoner/HANDOFF-godkjent-review-k1-k4-v1-v3-2026-07-25.md`
- **Gjeldende tekstgrunnlag:** de sju `*-godkjent-v0.1.md`-filene i `arbeidsversjoner/`
- **Låst baseline for innholdsdekning:** `soknadstekst-samlet-kandidat-v0.4.md`
- **Tidligere K/V-integrasjonskandidat:** `soknadstekst-samlet-kandidat-v0.5.md`
- **Aktiv kontrollkandidat med kildepass:** `soknadstekst-samlet-kandidat-v0.6.md`
- **K3-kontroll og sannhetsserum:** `k3-forskning-sannhetsserum-v0.6.md`
- **Styrende tilbakemeldingsregister:** `reviews/2026-08-05-tilbakemeldingsregister-v0.6.md`
- **Dagens avgrensede partnerpass:** `reviews/2026-08-05-v0.6-overflatepass-2-3-timer.md`
- **Senere grunnlagsløp mot v0.7:** `reviews/2026-08-05-v0.7-grunnlagsarbeid-og-partnerprosess.md`
- **Kollegareview mot Sannhetsserum:** `sannhetsserum-oppdatering-v0.5.md`
- **Kanoniske innflettingsmål:** de sju K/V-filene i tabellen under
- **Historisk status:** `v0.6` skulle gjennom et avgrenset partnerpass; dette er
  senere avløst av v1.7 IF-only-retningen over.
- **Åpen kvalitetsport C7:** kildeverifisering, kildehenvisninger og endelig innflettingskontroll

Arbeidsversjonene er ordlydskilden. `v0.4` skal ikke endres og bevarer innholdsdekningen. `v0.5` bevares som tidligere integrasjonskandidat. `v0.6` er den nye kontrollkandidaten for kildeavgrensning, språk og samsvar med K3-sannhetsserumet. De kanoniske kapittelfilene er målfilene og inneholder foreløpig eldre tekst.

## Status for kanoniske innflettingsmål

| Fil | Kriterium | Side | Status |
| --- | --- | --- | --- |
| `k1-bakgrunn.md` | Kvalitet | ~1,5 | Eldre måltekst — godkjent arbeidsversjon finnes |
| `k2-nyhetsverdi.md` | Kvalitet | ~2 | Eldre måltekst — godkjent arbeidsversjon finnes |
| `k3-forskning.md` | Kvalitet | ~1,5 | Eldre måltekst — godkjent arbeidsversjon finnes |
| `k4-metode.md` | Kvalitet | ~1,5 | Eldre måltekst — godkjent arbeidsversjon finnes |
| `v1-baerekraft.md` | Virkninger | ~1,5 | Eldre måltekst — godkjent arbeidsversjon finnes |
| `v2-sikkerhet.md` | Virkninger | ~1 | Eldre måltekst — godkjent arbeidsversjon finnes |
| `v3-okonomi.md` | Virkninger | ~1 | Eldre måltekst — godkjent arbeidsversjon finnes |
| `g1-gjennomforing.md` | Gjennomføring | ~1 (+~2 AP) | Nytt utkast — forankret i låst budsjett v2.1 (handoff #50) |

**Historisk AP1–AP6-materiale:** `g1-gjennomforing.md` dokumenterer den tidligere
32-MNOK-modellen etter handoff #50. Den er avløst av IF-only-beslutningen og
skal ikke brukes som gjeldende gjennomførings- eller budsjettgrunnlag. Gjeldende
arbeidsretning omfatter bare AP1–AP3 som angitt øverst.

## Regler som gjelder alle sju

1. **Bare 🟢 kan bære en setning alene.** 🟡 frases med forbehold. 🔴/⏸ brukes ikke.
   Farger leses fra `../vibs-verified-kildedom-2026-06-27.md` — aldri sett av en agent.
   **Emoji-fargene betyr kildestatus og ingenting annet.** Bruk dem aldri om kapittelstatus,
   framdrift eller triage — det forurenser signalet agenter og SINTEF leser etter.
2. **Ingen effektpåstand i presens.** VERIFIED *skal teste og måle*. Effekten er ikke bevist.
3. **Ingen lenker i teksten** (§10.6). Nøkler erstattes med korte tekstreferanser ved innsending.
4. **Skill *eksisterer* / *under bygging* / *veikart*** (`../claude-guardrails.md`).
   VIBS-plattformen er under bygging. Skriv ikke «den eksisterende plattformen».
5. **EBA er to organisasjoner.** `[EBA_EU2023]` = bank (V3). `[EBA_NO2023]` = entreprenør (V1).

## Sidebudsjett — kjent spenning

Tabellen summerer til ~10 sider. Men hovedokumentets budsjett er ~10 sider **inkludert** WP
(~2 s) og Gjennomføring (~1 s). K/V får altså ~7 sider i den endelige søknaden.

Ikke løs dette nå. Men ikke skriv 10 sider K/V i den tro at det er endelig format.

## Språkretning

Første utkast er skrevet i enkelt "snekker-språk": kortere setninger, konkret handling,
ingen KI-/konsulentsjargong, og tydelig skille mellom hva prosjektet skal teste og hva som
allerede er dokumentert. Videre språkvask skal bevare dette.

## Måltall

Innvilges fortløpende ved **snitt ≥ 4,0 og ingen delkarakter ≤ 3** (§10.8).
Forrige runde: 54 søknader, 6 innvilget — ~11 %.
