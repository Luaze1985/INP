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

1. [ecoinvent]
[ecoinvent]
- Kildebibliotek linje 67: | `[ecoinvent]` | ecoinvent – pedigree → lognormal/Monte Carlo. | Sekundær | [M] | 🟡 | ja (mirror) | §6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [Mecca2023]
[Mecca2023]
- Kildebibliotek linje 68: | `[Mecca2023]` | Mecca (2023). MCDA for urban/arkitektonisk bærekraft. DOI 10.1002/mcda.1818. AHP 46 / TOPSIS 20 / MIVES 11 / COPRAS 9. | Sekundær | [H\*] | 🟡 | nei (Wiley 402) | §5 / F4 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:26: | `[Mecca2023]` | Mecca (2023). «Assessing the sustainable development...» *Journal of Multi-Criteria Decision Analysis*, 10.1002/mcda.1818. | AHP (46 %) og TOPSIS (20 %) er de mest brukte MCDA-metodene. | 🟢 **Bekreftet** | **Bekreftet:** Tallene stemmer (AHP 
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:59: - MCDA-metodene finnes i litteratur, ikke som SMB-produkter. `[Mecca2023]` 🟡 `[Lohman2023]` 🟢

3. [Ciroth2016]
[Ciroth2016]
- Kildebibliotek linje 69: | `[Ciroth2016]` | Ciroth et al. (2016). Uncertainty factors for pedigree i ecoinvent. Int. J. LCA. | Sekundær | [L/M] | 🟡 | nei | §6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

4. [MCDM2025]
[MCDM2025]
- Kildebibliotek linje 70: | `[MCDM2025]` | Material selection in construction: systematic review on MCDM (2025). DOI 10.1007/s10669-025-10001-w. | Sekundær | [L/M] | 🔴 | nei (abstrakt) | §5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

5. [WLC-benchmark-NO]
[WLC-benchmark-NO]
- Kildebibliotek linje 71: | `[WLC-benchmark-NO]` | Norsk/nordisk WLC-benchmark for bygg (2024–25). | Sekundær | [L] | 🔴 | nei | §3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

6. [EBA_EU2023]
[EBA_EU2023]
- Kildebibliotek linje 79: | `[EBA_EU2023]` | European Banking Authority (2023). Report on Green Loans and Mortgages (15.12.2023). | Primær | [H] | 🟢 | ja | §7 / F5 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:27: | `[EBA_EU2023]` | European Banking Authority (2023). *Report on Green Loans and Mortgages* (EBA/Op/2023/13). | ESG bankrapportering, grønne lån og MCD-revisjon. | 🟢 **Bekreftet** | **Kollisjonshåndtering:** Må skilles strengt fra den norske entreprenørforenin
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:104: | **EBA-akronym** | «EBA» (blandet bruk) | `[EBA_EU2023]` (European Banking Authority) vs. `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg) | Skilt i to distinkte kildeoppføringer for å unngå forveksling av bank- og byggeregler. |
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:184: * *Nøkkel i kildebibliotek:* `[EBA_EU2023]`.
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:194: - Citationsnøklene i interne utkast må holdes strengt adskilt som `[EBA_EU2023]` og `[EBA_NO2023]`. De må aldri slås sammen til en felles `[EBA]`-nøkkel.
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:45: | **F5** | Byggdata → ESG/grønn finans/forsikring | §7 | Apparatet energisentrert `[EBA_EU2023]` 🟢; bro mangler |

7. [Billio2022]
[Billio2022]
- Kildebibliotek linje 80: | `[Billio2022]` | Billio, Costola, Pelizzon & Riedel (2022). Buildings' energy efficiency and the probability of mortgage default: The Dutch case. JREFE 65(3), 419–450. DOI 10.1007/s11146-021-09838-0. | Primær | [H] | 🟢 | ja (DOI/Springer + Crossref) | §7 / F1, F5 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:20: | `[Billio2022]` *(tidligere `[Billio_SAFE261]`)* | Billio, M., Costola, M., Pelizzon, L. & Riedel, M. (2022). «Buildings' energy efficiency and the probability of mortgage default: The Dutch case.» *JREFE*, 65(3), 419–450. | Energikarakter (EPC) påvirker misl
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:48: - *Tiltak:* Skriv om til: `| **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er hullet |`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:58: - *Tiltak:* Skriv om til: `- **Bro til grønn finans:** energi↔PD er bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:99: | **Kilde 3: Nøkkel** | `[Billio_SAFE261]` | `[Billio2022]` | Oppgradert fra Working Paper (SAFE WP 261) til ferdig publisert tidsskriftartikkel. |
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:41: | **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er hullet |
  - docs\reference\ipn-hovedokument.md:91: - **Bro til grønn finans:** energi↔PD er bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er FoU-hullet (F1). `[BoE_PS25-25]` 🟡 gir drahjelp fra kommende regelverk.

8. [An2020]
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
