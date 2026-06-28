# Vedlegg C — Kildebibliotek (VERIFIED / IPN)

**Dato:** 2026-06-22 · **Versjon:** 0.1 · **Eier:** SINTEF (primærverifisering) + VIBS (vedlikehold)
**Rolle:** Eneste kanoniske kildeliste for IPN-søknaden. Alle andre dokumenter siterer en **nøkkel** herfra og gjentar ikke full referanse. Jf. [`ipn-kildestrategi-2026-06-22.md`](ipn-kildestrategi-2026-06-22.md).

---

## Slik leses biblioteket

**Nøkkel** = mnemonisk `[Forfatter+År]`, og er ankernavn (hovedteksten lenker hit internt).

**Provenans** — porten som avgjør siterbarhet:
- **Primær** = originalkilden selv.
- **Sekundær** = referert via annen kilde / kun sammendrag.
- **Konsortie-intern** = VIBS'/SINTEFs eget arbeid (bestillingsverk, FoU-panel). *Aldri uavhengig belegg.*

**Port-status:**
- 🟢 = primær eller offisiell-autoritativ kilde åpnet og verifisert **for den påstanden den støtter** ([H]) → kan bære en søknadssetning alene. (Merk: en kilde kan være 🟢 for én påstand og svakere for en annen — f.eks. `[EN15978-2026]` er 🟢 for *at* standarden er publisert/dekker rehab, men standardens detaljerte bestemmelser er ikke lest.)
- 🟡 = sterk men primær ikke åpnet ([H\*]), eller sekundær/konsortie-intern ([M]) → støtte internt; åpne primær før bærende bruk.
- 🔴 = kun søketreff/metadata ([L]) eller udokumentert → ikke siterbar.

**Status nå (grovtelling):** flere 🟢 · flertall 🟡 · noen 🔴. Tyngdepunktet er fortsatt 🟡 — SINTEFs fulltekst-verifisering er det som flytter biblioteket mot grønt.

> ⚠️ **Navnekollisjon å passe på:** «EBA» betyr **to helt ulike ting** i dette materialet — `[EBA_EU2023]` = *European Banking Authority* (grønne lån, finans) og `[EBA_NO2023]` = *Entreprenørforeningen Bygg og Anlegg* (klimagass-veileder, 20 %-tallet). Ikke bland dem i søknadsteksten.

## Prioritering i søknadstekst

Når flere kilder kan støtte samme påstand, brukes denne rekkefølgen:

1. **Norske/offisielle kilder først** for norske forhold, regelverk, marked, kostnader, skader, SMB og byggenæring. Eksempler: `[NFR_IPN2026]`, `[FinansNorge2024VASK]`, `[KD2024]`, `[EBA_NO2023]`, `[Nordic2023]`, `[BKA2]`.
2. **Internasjonal fagfellevurdert forskning** brukes for generelle metode- og finansmekanismer som ikke har like sterk norsk dokumentasjon. Eksempler: `[Billio2022]`, `[Kaza2014]`, `[An2020]`, `[Lohman2023]`, `[Benke2025]`, `[Mecca2023]`.
3. **EU/standarder/regulering** brukes når påstanden gjelder rammeverk, krav eller kommende infrastruktur. Eksempler: `[CPR2024]`, `[ESPR2024]`, `[EN15978-2026]`, `[NS-EN16627]`, `[EBA_EU2023]`.
4. **Sekundære eller uåpnede kilder** kan støtte internt, men skal ikke bære en søknadssetning alene før primær er åpnet. Eksempler: `[SA2018]` og `[An2020]` står foreløpig 🟡 av denne grunnen.
5. **Konsortie-interne kilder** brukes bare som arbeidsgrunnlag og spor til primærkilder, ikke som uavhengig bevis. Eksempel: `[Wiik2025]`.

---

## A. Standarder og regulering

| Nøkkel | Referanse | Prov. | Konf. | Port | Åpnet | Støtter |
| --- | --- | --- | --- | --- | --- | --- |
| `[EN15978-2026]` | EN 15978:2026 – LCA på byggnivå. Publ. CEN-CENELEC 17.04.2026, erstatter 2011. | Offisiell | [H] | 🟢¹ | ja (CEN nyhetsside; standardtekst ikke lest) | §3 / F2 |
| `[NS-EN16627]` | NS 3454 trukket 07.09.2023, erstattet av NS-EN 16627 (LCC). | Primær | [H] | 🟢 | ja | §3 / F1 |
| `[CPR2024]` | Forordning (EU) 2024/3110 (revidert CPR) – konstruksjons-DPP. | Primær | [H] | 🟢 | ja (EUR-Lex) | §4 / F6 |
| `[ESPR2024]` | Forordning (EU) 2024/1781 (ESPR) – DPP; arbeidsplan 2025–2030. | Primær | [H/M] | 🟢 | ja (forordn.); arbeidsplandato sekundær | §4 / F6 |
| `[ISO14040]` | ISO 14040/14044:2006 – LCA prinsipper og krav. | Sekundær | [M] | 🟡 | nei | §3 |
| `[EN15804]` | EN 15804+A2 – EPD core rules (CEN/TC 350). | Sekundær | [M] | 🟡 | nei | §3, §4 |
| `[ISO15686-5]` | ISO 15686-5:2017 – livsløpskostnad (LCC). | Sekundær | [M] | 🟡 | nei | §3 / F1 |
| `[RICS-WLC]` | RICS Whole Life Carbon Assessment, 2. utg. (01.07.2024). | Sekundær | [M] | 🟡 | nei | §3 |
| `[EUTax]` | EU-taksonomi, Climate Delegated Act + DNSH (revisjon 2024–25). | Sekundær | [H\* ramme, M tall] | 🟡 | via søk | §7 / F5 |
| `[OmnibusI]` | Omnibus I / CSRD-innsnevring (vedtatt 24.02.2026). | Sekundær | [H\*] | 🟡 | nei (primær OJ) | §7 |
| `[NFR_IPN2026]` | Norges forskningsråd (2026). Innovasjonsprosjekt i næringslivet: Industri og tjenestenæringer 2026. Støttegrense kr 1 000 000–16 000 000 per prosjekt; maks 50 % støtte til bedriftenes kostnader. | Offisiell | [H] | 🟢 | ja | formalia / budsjett |
| `[EN17472]` | EN 17472:2022 – bærekraftvurdering anlegg (LCA+LCC). | Sekundær | [L] | 🔴 | nei | §3 |

¹ 🟢 for publiseringsfaktumet (at standarden finnes/dekker rehab), ikke for standardens detaljerte bestemmelser – de krever standardteksten selv.

---

## B. Forskning og metode (fagfellevurdert)

| Nøkkel | Referanse | Prov. | Konf. | Port | Åpnet | Støtter |
| --- | --- | --- | --- | --- | --- | --- |
| `[Edelen2018]` | Edelen & Ingwersen (2018). Creation, management, use of data quality info for LCA. Int. J. LCA. | Primær | [H] | 🟢 | ja | §6 / F4 |
| `[Lohman2023]` | Lohman et al. (2023). DMsan: MCDA framework. ACS Environmental Au. | Primær | [H] | 🟢 | ja | §5, §6 / F4 |
| `[Benke2025]` | Benke et al. (2025). Harmonized embodied-LCA dataset, N-Amerika. Scientific Data. | Primær | [H] | 🟢 | ja | §6 / F4 |
| `[Weidema1996]` | Weidema & Wesnæs (1996). Data quality indicators (pedigree). J. Cleaner Prod. | Primær | [H\*] | 🟡 | nei | §6 |
| `[ecoinvent]` | ecoinvent – pedigree → lognormal/Monte Carlo. | Sekundær | [M] | 🟡 | ja (mirror) | §6 |
| `[Mecca2023]` | Mecca (2023). MCDA for urban/arkitektonisk bærekraft. DOI 10.1002/mcda.1818. AHP 46 / TOPSIS 20 / MIVES 11 / COPRAS 9. | Sekundær | [H\*] | 🟡 | nei (Wiley 402) | §5 / F4 |
| `[Ciroth2016]` | Ciroth et al. (2016). Uncertainty factors for pedigree i ecoinvent. Int. J. LCA. | Sekundær | [L/M] | 🟡 | nei | §6 |
| `[MCDM2025]` | Material selection in construction: systematic review on MCDM (2025). DOI 10.1007/s10669-025-10001-w. | Sekundær | [L/M] | 🔴 | nei (abstrakt) | §5 |
| `[WLC-benchmark-NO]` | Norsk/nordisk WLC-benchmark for bygg (2024–25). | Sekundær | [L] | 🔴 | nei | §3 |

---

## C. Grønn finans (energi↔risiko, bank)

| Nøkkel | Referanse | Prov. | Konf. | Port | Åpnet | Støtter |
| --- | --- | --- | --- | --- | --- | --- |
| `[EBA_EU2023]` | European Banking Authority (2023). Report on Green Loans and Mortgages (15.12.2023). | Primær | [H] | 🟢 | ja | §7 / F5 |
| `[Billio2022]` | Billio, Costola, Pelizzon & Riedel (2022). Buildings' energy efficiency and the probability of mortgage default: The Dutch case. JREFE 65(3), 419–450. DOI 10.1007/s11146-021-09838-0. | Primær | [H] | 🟢 | ja (DOI/Springer + Crossref) | §7 / F1, F5 |
| `[An2020]` | An & Pivo (2020). Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms. Real Estate Economics 48(1), 7–42. DOI 10.1111/1540-6229.12228. Kommersielle CMBS-lån; 34 %-tallet må sjekkes i fulltekst/akseptert manus før bærende bruk. | Primær | [H\*] | 🟡 | metadata ja (Crossref); Wiley 403 | §7 / F1, F5 (næringsbygg, ikke boliglån) |
| `[Kaza2014]` | Kaza, Quercia & Tian (2014). Home Energy Efficiency and Mortgage Risks. Cityscape 16(1), 279–298. Residensielle boliglån; 32 % lavere misligholdsrisiko for ENERGY STAR-sertifiserte boliger. | Primær | [H] | 🟢 | ja (HUD/Cityscape) | §7 / F1, F5 |
| `[BoE_PS25-25]` | Bank of England PS25/25 (des. 2025). Klimarisiko inn i kjernerammeverk; frist juni 2026. | Sekundær | [H\*] | 🟡 | nei (BoE 403) | §7 / F5 |
| `[BoE_DP1-25]` | Bank of England DP1/25 (juli 2025). Boliglån LGD/PD-estimering. NB: ikke klima. | Sekundær | [M] | 🟡 | nei | §7 / F5 |
| `[EEMI]` | EEMI / Energy Efficient Mortgage Label; DeliverEEM. | Sekundær | [M] | 🟡 | via søk | §7 / F5 |
| `[FinanceNorway2018]` | Finance Norway (2018). Roadmap for Green Competitiveness. Eiendom = 60 % av bankutlån; boliglån = 47 %. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §7 / F5 |
| `[Multiconsult2023]` | Multiconsult/Eika Boligkreditt (2023). Nyere boliger 11,3 % av masse, 3,9 % av utslipp. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §7 / F5 |

---

## D. Verktøy (konkurrentscan)

| Nøkkel | Referanse | Prov. | Konf. | Port | Åpnet | Støtter |
| --- | --- | --- | --- | --- | --- | --- |
| `[EC3]` | EC3 (Building Transparency, USA). Synlig usikkerhet, enkriterium karbon. | Primær | [H] | 🟢 | ja | §10 / F4 |
| `[OneClickLCA]` | One Click LCA (FIN). Sterkest dataintegrasjon LCA+EPD+LCC. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F2 |
| `[Reduzer]` | Reduzer (NO, NTNU). Norsk, 15 000+ EPD, enkriterium i praksis. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 |
| `[Madaster]` | Madaster (NL). Materialpass/restverdi, porteføljenivå. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F3 |
| `[Cobuilder]` | Cobuilder (NO). Produktdata-infrastruktur, DPP, FDV. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F6 |
| `[Concular]` | Concular (DE). Sirkularitet/ombruk + CircularLCA. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F3 |
| `[2050Materials]` | 2050 Materials. Flere miljødimensjoner + API. | Sekundær | [L/M] | 🔴 | ja (leverandørside) | §10 |
| `[NOBB-OCL]` | Norsk Byggtjeneste × One Click LCA-partnerskap (EPD-adopsjon). | Sekundær | [M] | 🟡 | ja (OCL-PM, leverandørframstilling) | §4, §10 |

> **Forbehold (fra SoA §10):** Syv av åtte verktøy hviler på leverandørframstilling åpnet én gang; kun `[EC3]` har uavhengig bekreftelse. Norske/EU-aktører trenger dypere uavhengig dekning før påstander siteres.

---

## E. Bransje, offentlig og norsk kontekst

| Nøkkel | Referanse | Prov. | Konf. | Port | Åpnet | Støtter |
| --- | --- | --- | --- | --- | --- | --- |
| `[NOBB]` | NOBB / Norsk Byggtjeneste; GS1/GTIN-regelverk. ~3 mill. varer. | Sekundær | [M] | 🟡 | nei | §4 / F2 |
| `[EPD-Norge]` | EPD-Norge / ECO Platform / ECO Portal. | Sekundær | [M] | 🟡 | nei | §4 |
| `[CIRPASS2]` | CIRPASS-2 (bygg-DPP-pilot, Cobuilder). | Sekundær | [M] | 🟡 | nei | §4 / F6 |
| `[Byggforsk700.320]` | Byggforskserien 700.320 – intervaller vedlikehold/utskifting. Forbehold: ikke for konkret bygningsdel. | Primær | [H] | 🟡 | ja (bak betalingsmur) | §8 / F1, F3 |
| `[Ingvaldsen2008]` | Ingvaldsen, SINTEF Byggforsk (2008). Byggskadeomfanget i Norge. ~5 % av omsetning; 3/4 fuktrelatert. | Sekundær | [M] | 🟡 | delvis (døde lenker) | §8 / WP2 |
| `[FinansNorge2024VASK]` | Finans Norge (2024). Skadestatistikk for 2023. Vannskader: gjennomsnittlig 10 skader per time i 2023 (≈87 600/år); erstatninger nesten 5,1 mrd. kr. | Offisiell | [H] | 🟢 | ja | §8 / WP2 |
| `[SINTEFFag18]` | SINTEF Fag 18; FutureBuilt v3.1 (14.11.2025); DiBK/Resirqel (2019). Ombrukskriterier. | Sekundær | [M] | 🟡 | forsøkt | §8 / F3 |
| `[PlanGridFMI2018]` | PlanGrid/FMI (2018). Construction Disconnected. 52 % av omarbeid = dårlig data; $31,3 mrd/år US. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil, US/global) | §8 / WP2 |
| `[Herfjord2021]` | Herfjord & Adolfsen (2021, NTNU). BIM −15–20 % kost; rework ~20 % av produksjonstid. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | WP2 |
| `[SA2018]` | Samfunnsøkonomisk analyse (2018). Rapport om konflikter i bygg- og anleggsnæringen. Oppgitt primærkilde for konfliktkostnad 2,2 mrd. kr/år, men selve rapporten er ikke åpnet i denne kontrollen; tallet er kun gjenfunnet via sekundæromtale. **⏸ Tatt ut av søknadstekst 2026-06-28 (Lars' beslutning) — kilden ikke bekreftet å eksistere i åpne registre; gjeninnsett ved funn.** | Primær | [H\*] | 🟡 ⏸ | nei (må lokaliseres/åpnes) | §8 / WP2 |
| `[Harerusten2022]` | Harerusten (2022, NTNU). Konflikter i bygg- og anleggsbransjen. Sekundær omtale av konfliktkostnad; ikke bærende kilde for 2,2 mrd.-tallet. | Sekundær | [M] | 🟡 | ja (sekundær) | bakgrunn / WP2 |
| `[Bygg21_2019]` | Bygg21 (2019). Digitalt materialkjøp 3 mrd/år; sporbarhet = forutsetning for ombruk. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §4 / F3 |
| `[KS2025]` | KS/NHO/DiBK/KDD (2025). 60 % av byggesøknader mangelfulle; digitalt enevalg 810 mill./år. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | F6 |

---

## F. SMB-atferd og beslutningspraksis

| Nøkkel | Referanse | Prov. | Konf. | Port | Åpnet | Støtter |
| --- | --- | --- | --- | --- | --- | --- |
| `[Nordic2023]` | Nordic Council (2023). Building LCA and BIM practices in Norway. LCA-krav bevisst svakere for SMB. | Primær | [H] | 🟢 | ja | §9 / F4 |
| `[BKA2]` | BKA2 – Bærekraftige anskaffelser fase 2. 11,7 MNOK, til 2028. Knotten (SINTEF). | Primær | [H] | 🟢 | ja | §9 / WP1, WP4 |
| `[Lutdal2021]` | Lutdal & Brenden (2021, NTNU). ~200 boligeiere; miljøsertifisering 13. plass. | Sekundær | [M] | 🟡 | nei (via bestillingsverk) | §9 / F4 |

---

## G. Konsortie-interne kilder (bestillingsverk / eget arbeid)

> **Provenans = konsortie-intern. Kan IKKE bære en søknadssetning alene.** Brukes for å hente primærsitater og for intern syntese. Tallene må spores til primærene under før de går i søknad.

| Nøkkel | Referanse | Prov. | Konf. | Port | Merknad |
| --- | --- | --- | --- | --- | --- |
| `[Refleksjonsnotat2026]` | «Et blikk på byggebransjen og muligheter fremover», refleksjonsnotat v0.1. SINTEF-bestillingsverk for VIBS. | Konsortie-intern | – | 🔴 | Ikke siterbar i søknad. Kilde til primærsitatene under. |
| `[Wiik2025]` | Wiik, M.K. (2025). Kostnadseffekten av klimatiltak i byggenæringen – en litteraturgjennomgang. SINTEF Notat 57. Konsortie-internt/uindeksert grensetilfelle. Må ikke brukes som uavhengig bærende belegg; bruk primærkildene `[EBA_NO2023]` og `[KD2024]` for 20 %-påstanden. **⏸ Tatt ut av søknadstekst 2026-06-28 (Lars' beslutning) — notatet ikke funnet i åpne registre; gjeninnsett kun hvis SINTEF dokumenterer at det finnes.** | Konsortie-intern | [M] | 🟡 ⏸ | Ikke bærende alene. Kan omtales eksplisitt som internt notat hvis nødvendig. |
| `[GullbrekkenHolme2025]` | Gullbrekken & Holme (2025). Byggskader – Det glemte pengesluket. SINTEF. 1 feil i halvparten av boliger; 10–30 mrd NOK/år. | Primær (via bestillingsverk) | [M] | 🟡 | §8 / WP2. SINTEF åpner fulltekst → 🟢. |
| `[EBA_NO2023]` | EBA (Entreprenørforeningen Bygg og Anlegg), Grønn Byggallianse, Norsk Eiendom (2023). Veileder for klimagassreduksjoner – boligblokker. Opptil 20 % CO₂-kutt fra materialbruk uten merkostnad. | Sekundær (via bestillingsverk) | [M] | 🟡 | §3 / F1. **Ikke** European Banking Authority – se `[EBA_EU2023]`. |
| `[KD2024]` | Kommunal- og distriktsdepartementet, DiBK, Fellesforbundet, NHO Byggenæringen (2024). Byggenæringens klimafotavtrykk – et kunnskapsgrunnlag. Figur 1: påvirkningsrom størst i tidligfase. A1–A3 ≈ 63 % av materialeutslipp; sektor 17,3 mill. tonn CO₂e (2020). | Sekundær (via bestillingsverk) | [M] | 🟡 | §2, §3 / F2. NB: A1–A3-tallet attribuert «Asplan Viak/DiBK 2024» i Kunnskapsfil – avklar om samme rapport. |
| `[VIBS-FoUpanel]` | VIBS_VERIFIED_FoU-panel.docx / VIBS_ByggSpor_FoU-panel.docx. Internt FoU-panelnotat. | Konsortie-intern | – | 🔴 | Ikke siterbar i søknad. Intern struktur/argument. |

---

## Underlag (etablert grunnlag – gjentas ikke som nye kilder)

- `forskning-kunnskapsbase.md` (7 søyleområder, norsk problemdokumentasjon)
- `business/marked-sintef.md` (SINTEF-markedsanalyse)
- `forskningsekstraksjon-2026-06-22.md` (innsamlingslogg, Vedlegg D)

De etablerte norske problemtallene (byggfeilkostnad 10–30 mrd/år, konfliktkostnad 2,2 mrd/år, 18 000 kr/m² dyrere enn Sverige) regnes som etablert grunnlag.

---

### Endringslogg
- 0.4 (2026-06-28): Markert `[SA2018]` og `[Wiik2025]` ⏸ tatt ut av søknadstekst (Lars' beslutning) — kildene ikke bekreftet å eksistere i åpne registre. Beholdt i biblioteket som parkert; gjeninnsettes ved funn.
- 0.3 (2026-06-27): Faktisk kildesjekk etter innfletting. Korrigert Kaza-forfattere; nedgradert An2020 og SA2018 til 🟡 fordi fulltekst/primærrapport ikke ble åpnet i denne kontrollen.
- 0.2 (2026-06-27): Kildedom flettet inn. Rettet An/Billio/Kaza, lagt til SA2018, NFR_IPN2026 og FinansNorge2024VASK, og demotert Wiik2025 til konsortie-internt grensetilfelle.
- 0.1 (2026-06-22): Første konsolidering. SoA §13 + bestillingsverk-kilder + Kunnskapsfil-kilder samlet til mnemoniske nøkler med provenans-port. EBA-navnekollisjon flagget. Status: ~10 🟢, flertall 🟡, noen 🔴.
