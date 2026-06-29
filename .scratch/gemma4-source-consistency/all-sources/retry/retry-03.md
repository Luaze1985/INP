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

1. [Kaza2014]
[Kaza2014]
- Kildebibliotek linje 82: | `[Kaza2014]` | Kaza, Quercia & Tian (2014). Home Energy Efficiency and Mortgage Risks. Cityscape 16(1), 279–298. Residensielle boliglån; 32 % lavere misligholdsrisiko for ENERGY STAR-sertifiserte boliger. | Primær | [H] | 🟢 | ja (HUD/Cityscape) | §7 / F1, F5 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:19: | `[Kaza2014]` *(ny nøkkel)* | Kaza, N., Riley, S. F., Quercia, R. G. & Towe, C. (2014). «Home Energy Efficiency and Mortgage Risks.» *Cityscape*, 16(1), 279–298. | (Tidligere misattribuert til An et al.) | 🟢 **Bekreftet** | **Ny kilde:** Skal brukes for påsta
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:48: - *Tiltak:* Skriv om til: `| **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er hullet |`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:58: - *Tiltak:* Skriv om til: `- **Bro til grønn finans:** energi↔PD er bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:97: | **Kilde 2: Nøkkel** | (Mangler / utelatt) | `[Kaza2014]` | Kaza et al. må legges til som en egen, separat residensiell kilde. |
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:41: | **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er hullet |
  - docs\reference\ipn-hovedokument.md:91: - **Bro til grønn finans:** energi↔PD er bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er FoU-hullet (F1). `[BoE_PS25-25]` 🟡 gir drahjelp fra kommende regelverk.

2. [Bygg21_2019]
[Bygg21_2019]
- Kildebibliotek linje 123: | `[Bygg21_2019]` | Bygg21 (2019). Digitalt materialkjøp 3 mrd/år; sporbarhet = forutsetning for ombruk. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §4 / F3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:27: - SMB har lav grad av digitale arbeidsprosesser; BIM brukes av spesialister/store. `[KD2024]` `[Bygg21_2019]` 🟡
