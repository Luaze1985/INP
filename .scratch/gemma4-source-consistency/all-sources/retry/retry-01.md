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

1. [OneClickLCA]
[OneClickLCA]
- Kildebibliotek linje 96: | `[OneClickLCA]` | One Click LCA (FIN). Sterkest dataintegrasjon LCA+EPD+LCC. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F2 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [Nordic2023]
[Nordic2023]
- Kildebibliotek linje 132: | `[Nordic2023]` | Nordic Council (2023). Building LCA and BIM practices in Norway. LCA-krav bevisst svakere for SMB. | Primær | [H] | 🟢 | ja | §9 / F4 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:30: | `[Nordic2023]` | Nordic Council of Ministers (2023). *Building LCA and BIM practices in Norway*. | LCA-krav og verktøyadopsjon er vesentlig svakere for SMB. | 🟢 **Bekreftet** | **Bekreftet:** Støtter F4 og behovet for forenklet beslutningsverktøy i WP4. |
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:44: | **F4** | Forstår SMB rapporten; påvirker den valg | §5, §6, §9 | Forklarbarhet/attribusjon udekket; SMB-atferd udokumentert `[Nordic2023]` 🟢 |
  - docs\reference\ipn-hovedokument.md:60: - Forklarbar usikkerhet er empirisk bekreftet som udekket for SMB. `[Benke2025]` 🟢 `[Nordic2023]` 🟢
