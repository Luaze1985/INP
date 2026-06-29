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

2. [BoE_PS25-25]
[BoE_PS25-25]
- Kildebibliotek linje 83: | `[BoE_PS25-25]` | Bank of England PS25/25 (des. 2025). Klimarisiko inn i kjernerammeverk; frist juni 2026. | Sekundær | [H\*] | 🟡 | nei (BoE 403) | §7 / F5 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:56: - *Utkast:* `- **Bro til grønn finans:** energi↔PD er bekreftet [An2021] 🟢 [Billio_SAFE261] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:58: - *Tiltak:* Skriv om til: `- **Bro til grønn finans:** energi↔PD er bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:91: - **Bro til grønn finans:** energi↔PD er bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er FoU-hullet (F1). `[BoE_PS25-25]` 🟡 gir drahjelp fra kommende regelverk.

3. [BoE_DP1-25]
[BoE_DP1-25]
- Kildebibliotek linje 84: | `[BoE_DP1-25]` | Bank of England DP1/25 (juli 2025). Boliglån LGD/PD-estimering. NB: ikke klima. | Sekundær | [M] | 🟡 | nei | §7 / F5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

4. [EEMI]
[EEMI]
- Kildebibliotek linje 85: | `[EEMI]` | EEMI / Energy Efficient Mortgage Label; DeliverEEM. | Sekundær | [M] | 🟡 | via søk | §7 / F5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

5. [FinanceNorway2018]
[FinanceNorway2018]
- Kildebibliotek linje 86: | `[FinanceNorway2018]` | Finance Norway (2018). Roadmap for Green Competitiveness. Eiendom = 60 % av bankutlån; boliglån = 47 %. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §7 / F5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

6. [Multiconsult2023]
[Multiconsult2023]
- Kildebibliotek linje 87: | `[Multiconsult2023]` | Multiconsult/Eika Boligkreditt (2023). Nyere boliger 11,3 % av masse, 3,9 % av utslipp. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §7 / F5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

7. [EC3]
[EC3]
- Kildebibliotek linje 95: | `[EC3]` | EC3 (Building Transparency, USA). Synlig usikkerhet, enkriterium karbon. | Primær | [H] | 🟢 | ja | §10 / F4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-samledokument.md:128: Status nå: flere kilder er 🟢, flertallet er 🟡, og noen få er 🔴. Tyngdepunktet flytter seg mot grønt når SINTEF åpner primærene i fulltekst. De sterkeste grønne er standardene EN 15978:2026 og NS-EN 16627, EU-forordningene om digitalt produktpass (CPR/ESPR), fi
  - docs\reference\ipn-prosjektbeskrivelse-utkast.md:26: De ledende verktøyene stopper konsekvent på de samme to aksene. Synlig datakvalitet integrert i selve beslutningen finnes i praksis bare i ett verktøy, og der bare for karbon (EC3). Attribusjon av faktisk beslutningseffekt — om grunnlaget endret eller bekrefte
  - docs\reference\ipn-prosjektbeskrivelse-utkast.md:28: > **Kildestatus (avsnittet over):** Sterkest her. EN 15978:2026 og CPR (EU) 2024/3110 er 🟢 (offisielle kilder åpnet); EC3 og Benke mfl. (2025) er 🟢. Mecca (2023) er 🟡 — metodefordelingen er bekreftet via to sekundærkilder, men Wiley-fulltekst er ikke åpnet; SI

8. [OneClickLCA]
[OneClickLCA]
- Kildebibliotek linje 96: | `[OneClickLCA]` | One Click LCA (FIN). Sterkest dataintegrasjon LCA+EPD+LCC. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F2 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
