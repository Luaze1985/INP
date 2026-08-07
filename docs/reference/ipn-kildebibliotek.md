# Vedlegg C — Kildebibliotek (VERIFIED / IPN)

**Dato:** 2026-08-07 · **Versjon:** 0.6 · **Eier:** forskningspartner (primærverifisering) + prosjekteier (vedlikehold)
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
| `[ISO14040]` | ISO 14040/14044:2006 – LCA prinsipper og krav. Bekreftet 2022, med Amendment 1:2020. Sitert som [2] i v0.9 K2. | Sekundær | [M] | 🟡 | nei | §3 · v0.9 K2 |
| `[EN15804]` | EN 15804+A2 – EPD core rules (CEN/TC 350). | Sekundær | [M] | 🟡 | nei | §3, §4 |
| `[ISO15686-5]` | ISO 15686-5:2017 – livsløpskostnad (LCC). Bekreftet 2024. Sitert som [4] i v0.9 K2. | Sekundær | [M] | 🟡 | nei | §3 / F1 · v0.9 K2 |
| `[NS3720]` | Standard Norge (2018). NS 3720:2018 Metode for klimagassberegninger for bygninger. Sitert som [3] i v0.9 K2. | Sekundær | [M] | 🟡 | nei (bak betalingsmur) | v0.9 K2 |
| `[Levels2024]` | European Commission, DG Environment (2024). Level(s) Frequently Asked Questions. Bruker pålitelighetsvurdering av datainput, sensitivitetsanalyse og usikkerhetsanalyse som kriterier ved vurdering av LCA-verktøy. Sitert som [14] i v0.9 K2. | Offisiell | [M] | 🟡 | nei | v0.9 K2 / F4 |
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
| `[Mecca2023]` | Mecca (2023). MCDA for urban/arkitektonisk bærekraft. DOI 10.1002/mcda.1818. AHP 46 / TOPSIS 20 / MIVES 11 / COPRAS 9. **Ute av søknadsteksten fra v0.9** — erstattet av `[Munda2006]` som MCDA-grunnlag; AHP/TOPSIS-prosentene er ikke lenger i bruk. | Sekundær | [H\*] | 🟡 | nei (Wiley 402) | §5 / F4 (ikke i v0.9) |
| `[Munda2006]` | Munda, G. (2006). Multi-Criteria Decision Analysis and Sustainable Development. European Commission, Joint Research Centre, JRC32641. MCDA som egnet tilnærming til bærekraftsproblemer med økonomiske, miljømessige, tekniske og etiske dimensjoner. Sitert som [5] i v0.9 K2. | Primær | [M] | 🟡 | nei | v0.9 K2 / F4 |
| `[Raheim2023]` | Råheim, Å. F. (2023). Klimagassutslipp fra tekniske systemer i bygninger: En utforskende studie av beregningsmetoder og resultater. Masteroppgave, NTNU. NTNU Open. Manglende produktspesifikke miljødata tvang bruk av EPD-er for lignende produkter → økt usikkerhet. Sitert som [12] i v0.9 K4. | Primær | [M] | 🟡 | nei | v0.9 K4 |
| `[Liodden2024]` | Liodden, J. M. (2024). Ombruk av tegl i norske bygg. En analyse av livsløpsbaserte klimagassutslipp og variasjon i miljødeklarasjoner. Masteroppgave, NTNU. NTNU Open. Betydelig variasjon mellom EPD-er i samme produktgruppe. Sitert som [13] i v0.9 K2. | Primær | [M] | 🟡 | nei | v0.9 K2 / F3 |
| `[Reif2023]` | Reif, T. S. (2023). Evaluation of Early-Phase Building LCA Tools. Masteroppgave, NTNU. NTNU Open. Komparativ studie av to tidligfaseverktøy; begrensninger i treffsikkerhet og håndtering av usikkerhet. Sitert som [15] i v0.9 K2. | Primær | [M] | 🟡 | nei | v0.9 K2 / F4 |
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
| `[EC3]` | EC3 (Building Transparency, USA). Synlig usikkerhet, enkriterium karbon. «Uncertainty and statistics» + «Find and compare materials» lest 2026-08-06. Sitert som [9] i v0.9 K2. | Primær | [H] | 🟢 | ja | §10 / F4 · v0.9 K2 |
| `[OneClickLCA]` | One Click LCA (FIN). Sterkest dataintegrasjon LCA+EPD+LCC. «Life-cycle costing and carbon assessments» lest 2026-08-06. Sitert som [8] i v0.9 K2. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F2 · v0.9 K2 |
| `[Reduzer]` | Reduzer (NO, NTNU). Norsk, 15 000+ EPD, enkriterium i praksis. Tidligfase, EPD-bibliotek, BIM-integrasjon, sammenligning av material-/leverandør-/designalternativer; brukes til å dokumentere miljøkrav i konkurranser. Lest 2026-08-06. Sitert som [7] i v0.9 K2. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 · v0.9 K2 |
| `[SmartKalk]` | EG SmartKalk (NO). Kobler kalkyle, pris og materialmengder; tilgang til NOBB- og EPD-data; genererer FDV-dokumentasjon; beregner og sammenligner klimagassutslipp fra materialvalg. Lest 2026-08-06. Sitert som [6] i v0.9 K2. **Nærmeste norske avgrensning av VERIFIEDs nyhetsverdi.** | Sekundær | [M] | 🟡 | ja (leverandørside) | v0.9 K2 |
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
| `[SSB2026]` | Statistisk sentralbyrå (2026). Bedrifter, etter størrelse og næring, 1. januar 2026. Statistikkbanken, tabell 10309. 68 359 bedrifter i bygge- og anleggsnæringen; 91,2 % med færre enn ti ansatte (inkl. bedrifter uten ansatte); 76,2 % med 1–9 ansatte blant dem som har ansatte. Gjelder hele næringen, ikke VERIFIEDs avgrensede målgruppe. Sitert som [1] i v0.9 K1. | Offisiell | [H] | 🟢 | ja (Statistikkbanken) | v0.9 K1 |
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
| `[Refleksjonsnotat2026]` | «Et blikk på byggebransjen og muligheter fremover», refleksjonsnotat v0.1. SINTEF/Knotten-faglig syntese for VIBS. | Konsortie-intern | [M] | 🟡 | Intern faglig syntese og spor til primærkilder. Ikke uavhengig belegg; kan ikke bære søknadssetning alene. |
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

De etablerte norske problemtallene (byggfeilkostnad 10–30 mrd/år, konfliktkostnad 2,2 mrd/år, 18 000 kr/m² dyrere enn Sverige) ble regnet som etablert grunnlag fram til v0.9.

> ⚠️ **Gjelder ikke lenger for søknadsteksten.** Fra v0.9 (2026-08-07) er disse tallene ute; K1 hviler på `[SSB2026]` i stedet. Se endringslogg 0.6. Avsnittet står igjen som historikk over hva tidligere versjoner bygde på.

---

### Endringslogg
- **0.6 (2026-08-07): v0.9-synk.** Søknadskandidat v0.9 (`prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.9.md`) har en egen referanseliste på 15 poster. Biblioteket er avstemt mot den.
  - **Nye nøkler inn:** `[SSB2026]` (🟢, erstatter bransjetallene som SMB-belegg), `[NS3720]`, `[Levels2024]`, `[Munda2006]`, `[Raheim2023]`, `[Liodden2024]`, `[Reif2023]`, `[SmartKalk]`. Alle 🟡 unntatt `[SSB2026]` — de fire NTNU-oppgavene er åpent tilgjengelige i NTNU Open og bør kunne løftes til 🟢 ved åpning.
  - **Oppdatert:** `[ISO14040]`, `[ISO15686-5]`, `[EC3]`, `[OneClickLCA]`, `[Reduzer]` — lesedato 2026-08-06 og v0.9-referansenummer lagt inn. Ingen portendring.
  - **Ute av søknadsteksten fra v0.9** (kildene beholdes i biblioteket, porten er *uendret* — de er ikke nedgradert, bare ikke lenger i bruk): `[Kaza2014]`, `[Mecca2023]`, `[An2020]`, `[GullbrekkenHolme2025]`, `[FinansNorge2024VASK]`, `[PlanGridFMI2018]`, samt bransjetallene UNION 2025 (18 000 kr/m²), BDO 2025 (3,3 % driftsmargin) og Bjørheim 2026 (1 583 konkurser) som aldri fikk egen nøkkel her.
    **Hvorfor:** v0.9 bygger K1 på offisiell SSB-statistikk i stedet for bransjetall, og sier eksplisitt at prosjektet ikke oppgir generelle prosentsatser før den tilhørende originalanalysen er kontrollert (V1 → «Klima og systemgrense»). 32 %-tallet fra `[Kaza2014]` er derfor ute, og `[Billio2022]` brukes uten prosentsats — bare som dokumentert *sammenheng* i nederlandske boliglånsdata, med eksplisitt forbehold om at studien ikke dekker byggteknisk kvalitet.
    **Konsekvens:** «Underlag»-avsnittet nedenfor, som regner 10–30 mrd/år, 2,2 mrd/år og 18 000 kr/m² som etablert grunnlag, gjelder ikke lenger for søknadsteksten. Det står igjen som historikk.
  - **Gjeninnsetting:** kildene over kan tas inn igjen når originalanalysen er kontrollert og porten står 🟢 for den konkrete påstanden. Ingen av dem er parkert (⏸) — de er tilgjengelige, men ubrukte.
- 0.5 (2026-06-29): Løftet `[Refleksjonsnotat2026]` fra 🔴 til 🟡 som SINTEF/Knotten-faglig intern syntese etter Lars' avklaring. Fortsatt ikke uavhengig belegg og ikke bærende alene; primærkildene må åpnes for søknadstekst.
- 0.4 (2026-06-28): Markert `[SA2018]` og `[Wiik2025]` ⏸ tatt ut av søknadstekst (Lars' beslutning) — kildene ikke bekreftet å eksistere i åpne registre. Beholdt i biblioteket som parkert; gjeninnsettes ved funn.
- 0.3 (2026-06-27): Faktisk kildesjekk etter innfletting. Korrigert Kaza-forfattere; nedgradert An2020 og SA2018 til 🟡 fordi fulltekst/primærrapport ikke ble åpnet i denne kontrollen.
- 0.2 (2026-06-27): Kildedom flettet inn. Rettet An/Billio/Kaza, lagt til SA2018, NFR_IPN2026 og FinansNorge2024VASK, og demotert Wiik2025 til konsortie-internt grensetilfelle.
- 0.1 (2026-06-22): Første konsolidering. SoA §13 + bestillingsverk-kilder + Kunnskapsfil-kilder samlet til mnemoniske nøkler med provenans-port. EBA-navnekollisjon flagget. Status: ~10 🟢, flertall 🟡, noen 🔴.
