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

1. [KD2024]
[KD2024]
- Kildebibliotek linje 148: | `[KD2024]` | Kommunal- og distriktsdepartementet, DiBK, Fellesforbundet, NHO Byggenæringen (2024). Byggenæringens klimafotavtrykk – et kunnskapsgrunnlag. Figur 1: påvirkningsrom størst i tidligfase. A1–A3 ≈ 63 % av materialeutslipp; sektor 17,3 mill. tonn CO₂e (2020). | Sekundær (via bestillingsverk) | [M] | 🟡 | §2, §3 / F2. NB: A1–A3-tallet attribuert «Asplan Viak/DiBK 2024» i Kunnskapsfil – avklar om samme rapport. |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:53: - *Tiltak:* Skriv om til: `Innsendingssetning: «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (EBA Norge 2023; KDD et al. 2024).» [EBA_NO2023] [KD2024]`
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:12: - **Ingen lenker** i den innsendte teksten (bekreftet 2026). Nøkler er interne; ved innsending erstattes `[EBA_NO2023]` og `[KD2024]` med korte tekstreferanser til EBA Norge (2023) og KDD et al. (2024).
  - docs\reference\ipn-hovedokument.md:25: - Påvirkningsrommet for utslipp er størst i de tidligste fasene. `[KD2024]` 🟡
  - docs\reference\ipn-hovedokument.md:27: - SMB har lav grad av digitale arbeidsprosesser; BIM brukes av spesialister/store. `[KD2024]` `[Bygg21_2019]` 🟡
  - docs\reference\ipn-hovedokument.md:88: - Bevislag: «−20 % fra leverandørvalg uten merkostnad» `[EBA_NO2023]` 🟡 og tidligfasepåvirkning `[KD2024]` 🟡. `[Wiik2025]` ⏸ **TATT UT av søknadstekst** — SINTEF Notat 57 ikke funnet i åpne registre. Gjeninnsett kun hvis SINTEF dokumenterer at notatet finnes.
  - docs\reference\ipn-hovedokument.md:89: - Innsendingssetning: «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (EBA Norge 2023; KDD et al. 2024).» `[EBA_NO2023]` `[KD2024]`

2. [Billio2022]
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
