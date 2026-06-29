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

1. [EN15978-2026]
[EN15978-2026]
- Kildebibliotek linje 42: | `[EN15978-2026]` | EN 15978:2026 – LCA på byggnivå. Publ. CEN-CENELEC 17.04.2026, erstatter 2011. | Offisiell | [H] | 🟢¹ | ja (CEN nyhetsside; standardtekst ikke lest) | §3 / F2 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [NS-EN16627]
[NS-EN16627]
- Kildebibliotek linje 43: | `[NS-EN16627]` | NS 3454 trukket 07.09.2023, erstattet av NS-EN 16627 (LCC). | Primær | [H] | 🟢 | ja | §3 / F1 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

3. [CPR2024]
[CPR2024]
- Kildebibliotek linje 44: | `[CPR2024]` | Forordning (EU) 2024/3110 (revidert CPR) – konstruksjons-DPP. | Primær | [H] | 🟢 | ja (EUR-Lex) | §4 / F6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:46: | **F6** | Dataflyt/API/sporbarhet kan skaleres | §4, §10 | DPP umoden for bygg `[CPR2024]` 🟢; verktøy er ulike systemer uten kobling |

4. [ESPR2024]
[ESPR2024]
- Kildebibliotek linje 45: | `[ESPR2024]` | Forordning (EU) 2024/1781 (ESPR) – DPP; arbeidsplan 2025–2030. | Primær | [H/M] | 🟢 | ja (forordn.); arbeidsplandato sekundær | §4 / F6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

5. [ISO14040]
[ISO14040]
- Kildebibliotek linje 46: | `[ISO14040]` | ISO 14040/14044:2006 – LCA prinsipper og krav. | Sekundær | [M] | 🟡 | nei | §3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

6. [EN15804]
[EN15804]
- Kildebibliotek linje 47: | `[EN15804]` | EN 15804+A2 – EPD core rules (CEN/TC 350). | Sekundær | [M] | 🟡 | nei | §3, §4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

7. [ISO15686-5]
[ISO15686-5]
- Kildebibliotek linje 48: | `[ISO15686-5]` | ISO 15686-5:2017 – livsløpskostnad (LCC). | Sekundær | [M] | 🟡 | nei | §3 / F1 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

8. [RICS-WLC]
[RICS-WLC]
- Kildebibliotek linje 49: | `[RICS-WLC]` | RICS Whole Life Carbon Assessment, 2. utg. (01.07.2024). | Sekundær | [M] | 🟡 | nei | §3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
