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

1. [MCDM2025]
[MCDM2025]
- Kildebibliotek linje 70: | `[MCDM2025]` | Material selection in construction: systematic review on MCDM (2025). DOI 10.1007/s10669-025-10001-w. | Sekundær | [L/M] | 🔴 | nei (abstrakt) | §5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [BKA2]
[BKA2]
- Kildebibliotek linje 133: | `[BKA2]` | BKA2 – Bærekraftige anskaffelser fase 2. 11,7 MNOK, til 2028. Knotten (SINTEF). | Primær | [H] | 🟢 | ja | §9 / WP1, WP4 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:31: | `[BKA2]` | Knotten, V. / SINTEF (2024–2028). *Bærekraftige anskaffelser fase 2*. | Koordinering og faglig synergi, ikke duplisering. Budsjett 11,7 mill. | 🟢 **Bekreftet** | **Bekreftet:** Kobling bekreftet. Sikrer faglig overføringsverdi for WP4 uten overlap
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:101: - Konsortierollen: SINTEF (Knotten) kobler til pågående `[BKA2]` 🟢 — komplement, ikke duplikat.
  - docs\reference\ipn-samledokument.md:128: Status nå: flere kilder er 🟢, flertallet er 🟡, og noen få er 🔴. Tyngdepunktet flytter seg mot grønt når SINTEF åpner primærene i fulltekst. De sterkeste grønne er standardene EN 15978:2026 og NS-EN 16627, EU-forordningene om digitalt produktpass (CPR/ESPR), fi
