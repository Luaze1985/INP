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

1. [An2020]
[An2020]
- Kildebibliotek linje 81: | `[An2020]` | An & Pivo (2020). Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms. Real Estate Economics 48(1), 7–42. DOI 10.1111/1540-6229.12228. Kommersielle CMBS-lån; 34 %-tallet må sjekkes i fulltekst/akseptert manus før bærende bruk. | Primær | [H\*] | 🟡 | metadata ja (Crossref); Wiley 403 | §7 / F1, F5 (næringsbygg, ikke boliglån) |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:18: | `[An2020]` *(tidligere `[An2021]`)* | An, X. & Pivo, G. (2020). «Green Buildings in Commercial Mortgage-Backed Securities...» *Real Estate Economics*, 48(1), 7–42. | ~32 % lavere misligholdsrisiko (PD) for boliger med energisertifisering. | ⚠️ **Feil** | **R
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:48: - *Tiltak:* Skriv om til: `| **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er hullet |`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:58: - *Tiltak:* Skriv om til: `- **Bro til grønn finans:** energi↔PD er bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:94: | **Kilde 1: Nøkkel** | `[An2021]` | `[An2020]` | Endring av årstall til det offisielle publiseringsåret. |
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:41: | **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er hullet |
  - docs\reference\ipn-hovedokument.md:91: - **Bro til grønn finans:** energi↔PD er bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er FoU-hullet (F1). `[BoE_PS25-25]` 🟡 gir drahjelp fra kommende regelverk.
  - docs\reference\ipn-hovedokument.md:123: - 0.3 (2026-06-27): Faktisk kildesjekk etter innfletting. Justert `[SA2018]` og `[An2020]` til 🟡 inntil primærrapport/fulltekst er åpnet.

2. [BoE_DP1-25]
[BoE_DP1-25]
- Kildebibliotek linje 84: | `[BoE_DP1-25]` | Bank of England DP1/25 (juli 2025). Boliglån LGD/PD-estimering. NB: ikke klima. | Sekundær | [M] | 🟡 | nei | §7 / F5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
