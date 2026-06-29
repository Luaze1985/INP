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

1. [Refleksjonsnotat2026]
[Refleksjonsnotat2026]
- Kildebibliotek linje 144: | `[Refleksjonsnotat2026]` | «Et blikk på byggebransjen og muligheter fremover», refleksjonsnotat v0.1. SINTEF-bestillingsverk for VIBS. | Konsortie-intern | – | 🔴 | Ikke siterbar i søknad. Kilde til primærsitatene under. |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [BoE_PS25-25]
[BoE_PS25-25]
- Kildebibliotek linje 83: | `[BoE_PS25-25]` | Bank of England PS25/25 (des. 2025). Klimarisiko inn i kjernerammeverk; frist juni 2026. | Sekundær | [H\*] | 🟡 | nei (BoE 403) | §7 / F5 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:56: - *Utkast:* `- **Bro til grønn finans:** energi↔PD er bekreftet [An2021] 🟢 [Billio_SAFE261] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:58: - *Tiltak:* Skriv om til: `- **Bro til grønn finans:** energi↔PD er bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:91: - **Bro til grønn finans:** energi↔PD er bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er FoU-hullet (F1). `[BoE_PS25-25]` 🟡 gir drahjelp fra kommende regelverk.
