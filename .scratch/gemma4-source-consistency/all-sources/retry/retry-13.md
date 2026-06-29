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

1. [Mecca2023]
[Mecca2023]
- Kildebibliotek linje 68: | `[Mecca2023]` | Mecca (2023). MCDA for urban/arkitektonisk bærekraft. DOI 10.1002/mcda.1818. AHP 46 / TOPSIS 20 / MIVES 11 / COPRAS 9. | Sekundær | [H\*] | 🟡 | nei (Wiley 402) | §5 / F4 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:26: | `[Mecca2023]` | Mecca (2023). «Assessing the sustainable development...» *Journal of Multi-Criteria Decision Analysis*, 10.1002/mcda.1818. | AHP (46 %) og TOPSIS (20 %) er de mest brukte MCDA-metodene. | 🟢 **Bekreftet** | **Bekreftet:** Tallene stemmer (AHP 
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:59: - MCDA-metodene finnes i litteratur, ikke som SMB-produkter. `[Mecca2023]` 🟡 `[Lohman2023]` 🟢

2. [ecoinvent]
[ecoinvent]
- Kildebibliotek linje 67: | `[ecoinvent]` | ecoinvent – pedigree → lognormal/Monte Carlo. | Sekundær | [M] | 🟡 | ja (mirror) | §6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
