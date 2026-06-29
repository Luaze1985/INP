Oppgave: Vurder kildestatusdrift for disse kildene.
Les kun kandidatene under. Ikke finn pa fakta. Ikke gjor ny web/faktasjekk.

Returner gyldig JSON med:
{
  "ok": true/false,
  "flagged_rows": [
    {"item": "[EKSAKT_KILDEKEY]", "reason": "...", "recommended_action": "..."}
  ],
  "reason": "...",
  "recommended_action": "..."
}

Tvangsregel:
- Hvis ok=false, MAA flagged_rows ha minst en konkret rad.
- item MAA vaere en av kandidatoverskriftene, noyaktig som [KEY].
- Ikke flagg en kilde bare fordi den mangler i kildedommen; kildedommen er et subset.
- Flagg bare tydelig statusdrift: gronn vs gul/pause/rod, parkert kilde som brukes baerende, eller gammel/feil nokkel som fortsatt ser aktiv ut.

Repo-regler:
- Gronn kan baere en soknadssetning alene.
- Gul ma apnes/fraseres med forbehold.
- Rod er ikke siterbar.
- Pause betyr tatt ut av soknadstekst og parkert med gjeninnsettingsvilkar.

Kandidater:

1. [CIRPASS2]
[CIRPASS2]
- Kildebibliotek linje 114: | `[CIRPASS2]` | CIRPASS-2 (bygg-DPP-pilot, Cobuilder). | Sekundær | [M] | 🟡 | nei | §4 / F6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [Byggforsk700.320]
[Byggforsk700.320]
- Kildebibliotek linje 115: | `[Byggforsk700.320]` | Byggforskserien 700.320 – intervaller vedlikehold/utskifting. Forbehold: ikke for konkret bygningsdel. | Primær | [H] | 🟡 | ja (bak betalingsmur) | §8 / F1, F3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

3. [Ingvaldsen2008]
[Ingvaldsen2008]
- Kildebibliotek linje 116: | `[Ingvaldsen2008]` | Ingvaldsen, SINTEF Byggforsk (2008). Byggskadeomfanget i Norge. ~5 % av omsetning; 3/4 fuktrelatert. | Sekundær | [M] | 🟡 | delvis (døde lenker) | §8 / WP2 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

4. [FinansNorge2024VASK]
[FinansNorge2024VASK]
- Kildebibliotek linje 117: | `[FinansNorge2024VASK]` | Finans Norge (2024). Skadestatistikk for 2023. Vannskader: gjennomsnittlig 10 skader per time i 2023 (≈87 600/år); erstatninger nesten 5,1 mrd. kr. | Offisiell | [H] | 🟢 | ja | §8 / WP2 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

5. [SINTEFFag18]
[SINTEFFag18]
- Kildebibliotek linje 118: | `[SINTEFFag18]` | SINTEF Fag 18; FutureBuilt v3.1 (14.11.2025); DiBK/Resirqel (2019). Ombrukskriterier. | Sekundær | [M] | 🟡 | forsøkt | §8 / F3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:43: | **F3** | Når er ombruk/rehab best | §8 | Ombrukskriterier beskrevet `[SINTEFFag18]` 🟡, ikke tatt i bruk i praktiske verktøy |

6. [PlanGridFMI2018]
[PlanGridFMI2018]
- Kildebibliotek linje 119: | `[PlanGridFMI2018]` | PlanGrid/FMI (2018). Construction Disconnected. 52 % av omarbeid = dårlig data; $31,3 mrd/år US. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil, US/global) | §8 / WP2 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:26: - Dårlig data driver omarbeid (52 % internasjonalt). `[PlanGridFMI2018]` 🟡

7. [Herfjord2021]
[Herfjord2021]
- Kildebibliotek linje 120: | `[Herfjord2021]` | Herfjord & Adolfsen (2021, NTNU). BIM −15–20 % kost; rework ~20 % av produksjonstid. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | WP2 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

8. [SA2018]
[SA2018]
- Kildebibliotek linje 121: | `[SA2018]` | Samfunnsøkonomisk analyse (2018). Rapport om konflikter i bygg- og anleggsnæringen. Oppgitt primærkilde for konfliktkostnad 2,2 mrd. kr/år, men selve rapporten er ikke åpnet i denne kontrollen; tallet er kun gjenfunnet via sekundæromtale. **⏸ Tatt ut av søknadstekst 2026-06-28 (Lars' beslutning) — kilden ikke bekreftet å eksistere i åpne registre; gjeninnsett ved funn.** | Primær | [H\*] | 🟡 ⏸ | nei (må lokaliseres/åpnes) | §8 / WP2 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:24: | `[SA2018]` *(ny nøkkel)* | Samfunnsøkonomisk analyse (2018). «Konflikter i bygg- og anleggsnæringen» (Rapport 4-2018). | (Sitert sekundært via Harerusten 2022). | 🟢 **Bekreftet** | **Ny kilde:** Erstatt `[Harerusten2022]` med denne primærkilden for påstanden
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:43: - *Tiltak:* Erstatt med `- Konfliktkostnad 2,2 mrd NOK/år. [SA2018] 🟢` (Samfunnsøkonomisk analyse 2018).
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:24: - Konfliktkostnad 2,2 mrd NOK/år. `[SA2018]` ⏸ **TATT UT av søknadstekst** — Samfunnsøkonomisk analyse (2018), Rapport 4-2018 ikke lokalisert i åpne registre. Gjeninnsett som 🟢 når rapporten er funnet/åpnet.
  - docs\reference\ipn-hovedokument.md:121: - 0.5 (2026-06-28): Grensetilfeller markert ⏸ TATT UT av søknadstekst (Lars' beslutning): `[SA2018]`/2,2 mrd (rapport ikke lokalisert) og `[Wiik2025]` (Notat 57 ikke funnet). Ikke slettet — parkert her med gjeninnsettingsvilkår.
  - docs\reference\ipn-hovedokument.md:123: - 0.3 (2026-06-27): Faktisk kildesjekk etter innfletting. Justert `[SA2018]` og `[An2020]` til 🟡 inntil primærrapport/fulltekst er åpnet.
  - docs\reference\ipn-hovedokument.md:124: - 0.2 (2026-06-27): Kildedom flettet inn. Rettet konfliktkostnad til `[SA2018]`, An/Billio/Kaza-nøkler og CO₂-mekanisme uten `[Wiik2025]` som bærende kilde.
  - docs\reference\ipn-samledokument.md:177: - 0.6 (2026-06-28): Grensetilfeller tatt ut av søknadsteksten (Lars' beslutning): konflikttallet 2,2 mrd / `[SA2018]` (rapport ikke lokalisert) og `[Wiik2025]` (SINTEF Notat 57 ikke funnet i åpne registre). Kildene er ikke slettet — de står parkert i hovedokum
