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

1. [EC3]
[EC3]
- Kildebibliotek linje 95: | `[EC3]` | EC3 (Building Transparency, USA). Synlig usikkerhet, enkriterium karbon. | Primær | [H] | 🟢 | ja | §10 / F4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-samledokument.md:128: Status nå: flere kilder er 🟢, flertallet er 🟡, og noen få er 🔴. Tyngdepunktet flytter seg mot grønt når SINTEF åpner primærene i fulltekst. De sterkeste grønne er standardene EN 15978:2026 og NS-EN 16627, EU-forordningene om digitalt produktpass (CPR/ESPR), fi
  - docs\reference\ipn-prosjektbeskrivelse-utkast.md:26: De ledende verktøyene stopper konsekvent på de samme to aksene. Synlig datakvalitet integrert i selve beslutningen finnes i praksis bare i ett verktøy, og der bare for karbon (EC3). Attribusjon av faktisk beslutningseffekt — om grunnlaget endret eller bekrefte
  - docs\reference\ipn-prosjektbeskrivelse-utkast.md:28: > **Kildestatus (avsnittet over):** Sterkest her. EN 15978:2026 og CPR (EU) 2024/3110 er 🟢 (offisielle kilder åpnet); EC3 og Benke mfl. (2025) er 🟢. Mecca (2023) er 🟡 — metodefordelingen er bekreftet via to sekundærkilder, men Wiley-fulltekst er ikke åpnet; SI

2. [KS2025]
[KS2025]
- Kildebibliotek linje 124: | `[KS2025]` | KS/NHO/DiBK/KDD (2025). 60 % av byggesøknader mangelfulle; digitalt enevalg 810 mill./år. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | F6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
