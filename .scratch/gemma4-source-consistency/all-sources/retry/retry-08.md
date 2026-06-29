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

1. [Harerusten2022]
[Harerusten2022]
- Kildebibliotek linje 122: | `[Harerusten2022]` | Harerusten (2022, NTNU). Konflikter i bygg- og anleggsbransjen. Sekundær omtale av konfliktkostnad; ikke bærende kilde for 2,2 mrd.-tallet. | Sekundær | [M] | 🟡 | ja (sekundær) | bakgrunn / WP2 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:23: | `[Harerusten2022]` | Harerusten, S. (2022). «Konflikter i bygg- og anleggsbransjen...» *NTNU Masteroppgave*. | Konflikter i bygg- og anleggssektoren koster 2,2 milliarder kroner årlig. | 🔴 **Ubekreftet** | **Grensetilfelle:** Masteroppgaven inneholder ikke p
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:24: | `[SA2018]` *(ny nøkkel)* | Samfunnsøkonomisk analyse (2018). «Konflikter i bygg- og anleggsnæringen» (Rapport 4-2018). | (Sitert sekundært via Harerusten 2022). | 🟢 **Bekreftet** | **Ny kilde:** Erstatt `[Harerusten2022]` med denne primærkilden for påstanden
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:41: - *Utkast:* `- Konfliktkostnad 2,2 mrd NOK/år. [Harerusten2022] 🟡`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:42: - *Årsak:* `[Harerusten2022]` er en masteroppgave (sekundærkilde) som ikke dokumenterer tallet primært.
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [WLC-benchmark-NO]
[WLC-benchmark-NO]
- Kildebibliotek linje 71: | `[WLC-benchmark-NO]` | Norsk/nordisk WLC-benchmark for bygg (2024–25). | Sekundær | [L] | 🔴 | nei | §3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
