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

1. [VIBS-FoUpanel]
[VIBS-FoUpanel]
- Kildebibliotek linje 149: | `[VIBS-FoUpanel]` | VIBS_VERIFIED_FoU-panel.docx / VIBS_ByggSpor_FoU-panel.docx. Internt FoU-panelnotat. | Konsortie-intern | – | 🔴 | Ikke siterbar i søknad. Intern struktur/argument. |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [FinanceNorway2018]
[FinanceNorway2018]
- Kildebibliotek linje 86: | `[FinanceNorway2018]` | Finance Norway (2018). Roadmap for Green Competitiveness. Eiendom = 60 % av bankutlån; boliglån = 47 %. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §7 / F5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
