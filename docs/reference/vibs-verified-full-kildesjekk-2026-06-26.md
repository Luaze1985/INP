# VIBS VERIFIED — Full kildesjekk
**Dato:** 2026-06-26 · **Utarbeidet av:** Claude (Anthropic) i Cowork-modus
**Grunnlag:** 5 interne referansedokumenter + 30 websøk
**Formål:** Systematisk verifisering av ALLE referanser og faktapåstander i IPN-dokumentene før Sonar-runden.
**NB:** Tre kritiske feil er avdekket — se §A, §B og §C under.

---

## KRITISKE FEIL — LES FØRST

### Kritisk feil A: An et al. — feil DOI, feil journal, feil studie
**Problem:** I SotA §7 og §13 er An et al. oppgitt med DOI `10.1007/s11146-021-09838-0`. **Denne DOI-en tilhører Billio et al. (2022)** — ikke An & Pivo (2020). Det betyr at lenken «åpnet og verifisert» i SotA §7 faktisk er Billio-artikkelen, ikke An-artikkelen. I tillegg er jou-rnaltilknytningen feil (SotA impliserer JREFE; An & Pivo er i *Real Estate Economics*), og studien gjelder **kommersiell eiendom / CMBS** — ikke boliglån.

**Korrekt referanse:**
> An, X. & Pivo, G. (2020). «Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms.» *Real Estate Economics*, 48(1), 7–42. DOI: 10.1111/1540-6229.12228

### Kritisk feil B: «32 % lavere PD (UNC-studie)» — feil attribusjon
**Problem:** SotA §7 attribuerer «boliger med energisertifisering har ~32 % lavere PD (UNC-studie)» til An et al. med Billio-lenken. 32 %-tallet stammer faktisk fra en **annen og separat studie:**

> Kaza, N., Quercia, R.G. & Tian, C.Y. (ca. 2012). *Home Energy Efficiency and Mortgage Risks.* IMT (Institute for Market Transformation) / UNC Center for Community Capital. Tilgjengelig: https://imt.org/wp-content/uploads/2018/02/IMT_UNC_HomeEEMortgageRisksfinal.pdf

IMT/UNC-studien analyserte ~71 000 ENERGY STAR-sertifiserte **boliger** (residential) og fant 32 % lavere misligholds­risiko. An & Pivo (2020) analyserte CMBS (kommersiell eiendom) og fant 34 % lavere default­risiko.

**I søknaden er det altså to ulike studier som er blandet til én:** IMT/UNC (32 %, bolig) og An & Pivo (34 %, kommersiell). Begge er relevante, men må holdes fra hverandre og siteres korrekt.

### Kritisk feil C: Finans Norge vannskader — 78 500 er 2021-tall
**Problem:** Dersom dokumentene bruker tallet 78 500 om vannskader i 2023, er dette feil. 78 500 er antall innmeldte vannskader i **2021**. I 2023 ble det meldt inn gjennomsnittlig **10 vannskader per time** (Finans Norge Skadestatistikk 2023), noe som tilsvarer ≈ 87 600 per år. Total erstatning i 2023 var 5,1 mrd kr.

---

## Kildeoversikt per kilde

### [An & Pivo 2020] Green Buildings in Commercial Mortgage-Backed Securities
- **Søkt:** An Pivo 2020 LEED Energy Star CMBS default risk Real Estate Economics
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms»
  - Tidsskrift: *Real Estate Economics*, Vol. 48, No. 1, s. 7–42, mars 2020
  - DOI: **10.1111/1540-6229.12228**
  - Funn: CMBS-lån på LEED/Energy Star-sertifiserte bygg har **34 % lavere default-risiko**, alt annet likt. Mekanisme: grønn prisbonus → lavere LTV.
  - Gjelder: **kommersiell eiendom (CMBS)** — ikke boliglån
- **Avvik fra dokumentet:**
  - SotA gir feil DOI: `10.1007/s11146-021-09838-0` (Billio-DOI)
  - SotA sier «J. Real Estate Finance and Economics» (JREFE) — feil. Riktig journal er *Real Estate Economics* (Wiley)
  - SotA attribuerer 32 %-funnet til An et al. — feil (32 % er IMT/UNC-studien, se kritisk feil B)
  - Tittel i SotA er «Green building certification and mortgage default risk» — upresist
- **Status:** ⚠️ FEIL DOI OG JOURNAL
- **Kan brukes i søknaden:** Ja — men med korrekt referanse, korrekt DOI, og med tydelig merking av at studien gjelder kommersiell eiendom

---

### [IMT/UNC ~2012] Home Energy Efficiency and Mortgage Risks
- **Søkt:** home energy efficiency mortgage risk UNC Center for Community Capital 32 percent default residential
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: *Home Energy Efficiency and Mortgage Risks*
  - Utgiver: IMT (Institute for Market Transformation) / UNC Center for Community Capital
  - Forfattere: Kaza, N., Quercia, R.G. & Tian, C.Y. (ca. 2012–2014)
  - Funn: Eiere av ENERGY STAR-boliger har **32 % lavere sannsynlighet for mislighold** på boliglånet. Analyserte ~71 000 ENERGY STAR-sertifiserte boliger (residential mortgages).
  - PDF: https://imt.org/wp-content/uploads/2018/02/IMT_UNC_HomeEEMortgageRisksfinal.pdf
- **Avvik fra dokumentet:** Denne studien er ikke sitert eksplisitt i dokumentene — funnet er i stedet feilattribuert til An et al. (kritisk feil B). Studien eksisterer og er relevant.
- **Status:** ❓ IKKE NAVNGITT (eksisterer, relevant, men feilattribuert)
- **Kan brukes i søknaden:** Ja — som separat referanse (residential 32 %; An & Pivo = commercial 34 %)

---

### [Billio et al. 2022] Buildings' Energy Efficiency and Mortgage Default — Dutch Case
- **Søkt:** Billio Costola Pelizzon Riedel 2022 energy efficiency mortgage default Dutch JREFE 65
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «Buildings' Energy Efficiency and the Probability of Mortgage Default: The Dutch Case»
  - Tidsskrift: *Journal of Real Estate Finance and Economics*, Vol. 65, No. 3, s. 419–450, oktober 2022
  - DOI: **10.1007/s11146-021-09838-0** ✅
  - Opprinnelig: SAFE Working Paper No. 261 (2020)
  - Forfattere: Monica Billio, Michele Costola, Loriana Pelizzon, Max Riedel ✅
  - Metode: logit-regresjon + Cox-modell, nederlandske lånenivå-data + EPC-klasser fra RVO
  - Tre mekanismer: (i) låntagerprofil, (ii) energisparing → disponibel inntekt, (iii) boligverdi → lavere LTV ✅
- **Avvik fra dokumentet:** Ingen — referansen er korrekt i kildelisten. DOI-en er imidlertid feilaktig gitt til An et al. i §7/§13 (se kritisk feil A).
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [Mecca 2023] MCDA review — AHP/TOPSIS/MIVES/COPRAS
- **Søkt:** Mecca 2023 multi-criteria decision analysis urban architectural sustainability AHP TOPSIS MIVES COPRAS Journal of Multi-Criteria Decision Analysis
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «Assessing the sustainable development: A review of multi-criteria decision analysis for urban and architectural sustainability»
  - Tidsskrift: *Journal of Multi-Criteria Decision Analysis* (Wiley Online Library)
  - DOI: **10.1002/mcda.1818** ✅
  - Funn bekreftet: AHP 46 %, TOPSIS 20 %, MIVES 11 %, COPRAS 9 % ✅
  - Artikkel er bak Wiley-betalingsmur (PDF), men eksistens og innhold bekreftet via søk
- **Avvik fra dokumentet:** Ingen relevante avvik. Forfatternavnet «Mecca, B.» og tallene er korrekte.
- **Status:** ✅ BEKREFTET (H* → SINTEF bør hente fulltekst for nøyaktig sitering)
- **Kan brukes i søknaden:** Ja — SINTEF henter fulltekst via institusjonstilgang

---

### [Harerusten 2022] Konflikter i byggebransjen — 2,2 mrd/år
- **Søkt:** Harerusten 2022 byggkonflikter norsk studie 2,2 milliarder
- **Funnet:** Delvis
- **Faktisk info:**
  - Funnet i NTNU Open: «Konflikter i bygg- og anleggsbransjen — Analyse av årsaker» https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/3108486
  - Syver Harerusten er identifisert som mulig forfatter (NTNU-masteroppgave 2022)
  - «2,2 milliarder hvert år» finnes i medieomtale (Dagens Perspektiv: «Krangler om 2,2 milliarder hvert år»), muligens opprinnelig fra en Samfunnsøkonomisk analyse-rapport (~2018)
  - Det er uklart om 2,2 mrd-tallet stammer direkte fra Harerusten (2022) eller fra en eldre rapport
- **Avvik fra dokumentet:** Full referanse (fullt navn, tittel, utgiver, type) er ikke verifisert. Tallverdien kan stamme fra en eldre kilde.
- **Status:** ❓ IKKE FULLSTENDIG VERIFISERT
- **Kan brukes i søknaden:** Med forbehold — SINTEF verifiserer via NTNU Open og primærtekst

---

### [Benke et al. 2025] Harmonized Dataset — Embodied LCA North America
- **Søkt:** Benke 2025 harmonized dataset embodied LCA buildings North America Scientific Data 292
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «A Harmonized Dataset of High-Resolution Embodied Life Cycle Assessment Results for Buildings in North America»
  - Tidsskrift: *Scientific Data* (Nature Publishing Group)
  - Publisert: 1. juli 2025
  - PMC: **PMC12218139** ✅
  - DOI: se Nature-link https://www.nature.com/articles/s41597-025-05216-0
  - Forfattere: Brad Benke, Manuel Chafart, Yang Shen, Milad Ashtiani, Stephanie Carlisle, Kathrina Simonen (University of Washington)
  - Innhold: 292 byggeprosjekter i USA og Canada. Bekrefter at industri-LCA sjelden er offentlig/sammenlignbar og at verktøy har ulike default-antakelser ✅
- **Avvik fra dokumentet:** Ingen relevante avvik. SotA sier «292 byggprosjekter Nord-Amerika» — korrekt.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [Weidema & Wesnæs 1996] Pedigree-matrisen
- **Søkt:** Weidema Wesnæs 1996 data quality management life cycle inventories Journal of Cleaner Production pedigree matrix
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «Data quality management for life cycle inventories — an example of using data quality indicators»
  - Tidsskrift: *Journal of Cleaner Production*, Vol. 4, Issues 3–4, s. 167–174, 1996
  - DOI: **10.1016/S0959-6526(96)00043-1**
  - Forfattere: Bo Pedersen Weidema & Marianne Suhr Wesnæs ✅
  - Inneholder fem datakvalitetsindikatorer (pågrenselighets-, pålitelighets-, fullstendig-, tidsmessig/geografisk/teknologisk korrelasjon) — opprinnelsen til pedigree-matrisen ✅
- **Avvik fra dokumentet:** SotA sier «Weidema, B.P. & Wesnæs, M.S.» — korrekt. Sideserie «4(3–4):167–174» ✅. DOI ikke oppgitt i SotA, men nå funnet.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [Edelen & Ingwersen 2018] LCA data quality
- **Søkt:** Edelen Ingwersen 2018 data quality information LCA International Journal of Life Cycle Assessment PMC5919259
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «The creation, management, and use of data quality information for life cycle assessment»
  - Tidsskrift: *International Journal of Life Cycle Assessment*, Vol. 23(4), s. 759–772, 2018
  - DOI: **10.1007/s11367-017-1348-1**
  - PMC: **PMC5919259** ✅
  - Forfattere: Andrew Edelen & Wesley Ingwersen (US EPA) ✅
- **Avvik fra dokumentet:** Ingen. Alt i SotA stemmer.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [Lohman et al. 2023] DMsan — Multi-Criteria Decision Analysis
- **Søkt:** Lohman 2023 DMsan multi-criteria decision analysis sanitation ACS Environmental Au PMC10197171
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «DMsan: A Multi-Criteria Decision Analysis Framework and Package to Characterize Contextualized Sustainability of Sanitation and Resource Recovery Technologies»
  - Tidsskrift: *ACS Environmental Au*, 2023
  - DOI: https://pubs.acs.org/doi/10.1021/acsenvironau.2c00067
  - PMC: **PMC10197171** ✅
  - Fem kriterier, 28 indikatorer, viser «opportunity spaces» under ulike vektscenarioer ✅
- **Avvik fra dokumentet:** Ingen relevante avvik.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [Finans Norge 2023] Vannskadestatistikk — VASK
- **Søkt:** Finans Norge VASK 2023 vannskader 5,1 milliard 78 500 87 600 skader per år
- **Funnet:** Ja (med viktig presisering)
- **Faktisk info (2023):**
  - Gjennomsnittlig **10 vannskader per time** meldt til forsikring i 2023 (mot 8 i 2022)
  - Total erstatning for vannskader i 2023: **5,1 mrd kr** (av totalt 12,6 mrd kr for private boliger/innbo) ✅
  - 10/time × 8 760 timer/år = **≈ 87 600 vannskader per år** (2023)
  - Kilde: Finans Norge Skadestatistikk for 2023 (februar 2024): https://www.finansnorge.no/artikler/2024/02/skadestatistikk-for-2023/
- **Avvik fra dokumentet:**
  - Tallet **78 500** refererer til **2021**, ikke 2023
  - «10 per time» (2023) = ca. 87 600/år — bruk dette for 2023-argumentet
  - Dersom dokumentene bruker «78 500» som 2023-tall, er dette feil
- **Status:** ⚠️ DELVIS — 5,1 mrd kr ✅, men talloppgitt antall skader avhenger av årstall
- **Kan brukes i søknaden:** Ja — bruk «10 vannskader per time i 2023» og «5,1 mrd kr» med korrekt kilde

---

### [Bank of England PS25/25] Klimarisiko — desember 2025
- **Søkt:** Bank of England PS25/25 climate-related risks SS3/19 December 2025 banks insurers
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «PS25/25 – Enhancing banks' and insurers' approaches to managing climate-related risks – Update to SS3/19»
  - Publisert: **3. desember 2025** av UK Prudential Regulation Authority (PRA) ✅
  - Nytt supervisory statement: **SS5/25** (samme dato)
  - Erstatter SS3/19 i sin helhet ✅
  - Overgangsperiode: seks måneder (til ~juni 2026) ✅
  - Inkluderer governance, risikostyring, scenarioanalyse, data og disclosure
  - URL: https://www.bankofengland.co.uk/prudential-regulation/publication/2025/december/enhancing-banks-and-insurers-approaches-to-managing-climate-related-risks-policy-statement ✅
- **Avvik fra dokumentet:** Ingen. Substans bekreftet. «Step change, not a refinement» — karakterisering bekreftet av bransjekildene.
- **Status:** ✅ BEKREFTET (H* → nå styrket til nær H via søkeresultater)
- **Kan brukes i søknaden:** Ja

---

### [Bank of England DP1/25] Residential mortgages — PD og LGD
- **Søkt:** Bank of England DP1/25 residential mortgages probability of default LGD estimation discussion paper 2025
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «DP1/25 – Residential mortgages: Loss given default (LGD) and probability of default (PD) estimation»
  - Publisert: **juli 2025** av UK PRA ✅
  - Formål: utforsker mulig «foundation IRB» for boliglån, der mellomstore banker modellerer PD men bruker faste supervisory LGD-verdier
  - Høringsfrist: **31. oktober 2025** ✅ (SotA sier «lukket okt. 2025» ✅)
  - URL: https://www.bankofengland.co.uk/prudential-regulation/publication/2025/july/residential-mortgages-loss-given-default-and-probability-of-default-estimation-discussion-paper ✅
  - Gjelder **IKKE klima** ✅ (bekrefter SotA-rettelsen)
- **Avvik fra dokumentet:** Ingen — DP1/25 er korrekt beskrevet som PD/LGD/IRB, ikke klima.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja — men ikke som klimareferanse

---

### [Omnibus I 2026] CSRD-innsnevring
- **Søkt:** Omnibus I CSRD stop-the-clock February 2026 adopted EU regulation 1000 employees 450 million
- **Funnet:** Ja
- **Faktisk info:**
  - Vedtatt av EUs råd: **24. februar 2026** ✅
  - Publisert i Official Journal: **26. februar 2026** som Directive (EU) **2026/470** ✅
  - Ikrafttredelse: **18. mars 2026**
  - Terskel for CSRD-rapporteringsplikt: **>1 000 ansatte OG >450 mEUR** nettoomsetning ✅
  - Andel selskapers fjernet fra scope: **~80–90 %** (SotA sier «~80 %» — bekreftet) ✅
  - Viktig presisering: «Stop-the-Clock» Directive (2025/794) er en SEPARAT, tidligere direktiv (publisert OJ 16. april 2025) — ikke det samme som Omnibus I
- **Avvik fra dokumentet:** Ingen substansielle. SotA's «vedtatt 24.02.2026» er korrekt for det substantielle Omnibus I. SotA-notatet om «ulike tidslinjer» for Stop-the-Clock vs. Omnibus er korrekt.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja — OJ-referanse er Directive (EU) 2026/470

---

### [EN 15978:2026] LCA på byggnivå
- **Søkt:** EN 15978:2026 CEN-CENELEC 17 April 2026 published building environmental assessment
- **Funnet:** Ja
- **Faktisk info:**
  - Publisert av CEN-CENELEC: **17. april 2026** ✅
  - Erstatter EN 15978:2011 ✅
  - Gjelder nye bygg, eksisterende bygg og rehabiliteringsprosjekter ✅
  - URL: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-04-17-en-15978-2026/ ✅
  - Utviklet av CEN/TC 350
- **Avvik fra dokumentet:** Ingen.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [NS 3454 → NS-EN 16627] Norsk LCC-standard
- **Søkt:** NS 3454 withdrawn 7 september 2023 NS-EN 16627 Norway life cycle costs standard replacement
- **Funnet:** Ja
- **Faktisk info:**
  - NS 3454 trukket: **7. september 2023** ✅
  - Erstattet av: **NS-EN 16627** ✅
  - Standard Norge har utgitt veiledning for overgangen (Standard Morgen, 27.9.2023)
  - URL: https://standard.no/fagomrader/barekraftige-bygg-og-anlegg/barekraftige-byggverk--rammeverk-for-vurdering-av-bygg-og-anlegg/livssykluskostnader-for-byggverk---ns-3454/ ✅
- **Avvik fra dokumentet:** Ingen.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [Ingvaldsen / SINTEF Byggforsk 2008] Byggskadeomfanget i Norge
- **Søkt:** Ingvaldsen SINTEF 2008 byggskadeomfanget i Norge 5 prosent fuktskader
- **Funnet:** Delvis
- **Faktisk info:**
  - Prosjektrapport 308 (2001) er primærkilden — funnet på SINTEF.no
  - SINTEF Open-oppføring bekrefter en 2008-publikasjon med tittel «Byggskadeomfanget i Norge. Utbedringskostnader i norsk bygge-/eiendomsbransje — og erfaringer fra andre land»
  - URL: https://sintef.brage.unit.no/sintef-xmlui/handle/11250/2415798
  - Gullbrekken & Holme (2025) refererer til at «SINTEF estimated in 2008 that damage costs represented 2 to 6 percent of turnover»
  - «Tre av fire byggskader er fuktskader» bekreftet via norskbyggebransje.no ✅
  - 5 % av bransjens omsetning bekreftet i PR308 (2001), oppdatert/referert i 2008-publikasjon
- **Avvik fra dokumentet:** Ingen alvorlige. SotA siterer «(PR308/2001, PR163/1994)» som underkilder — dette er korrekt. Årstallet 2008 refererer til oppdatert publikasjon.
- **Status:** ⚠️ DELVIS (primærkilde funnet men ikke fulltekst-åpnet; 5 % og ¾ fukt bekreftet via sekundærkilder)
- **Kan brukes i søknaden:** Ja — med forbehold (eldre data, 2008, med referanse til prosjektrapport)

---

### [Gullbrekken & Holme 2025] Byggskader — Det glemte pengesluket
- **Søkt:** Gullbrekken Holme 2025 SINTEF byggskader det glemte pengesluket rapport
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «Byggskader – det glemte pengesluket»
  - Forfattere: Lars Gullbrekken og Jonas Holme (SINTEF) ✅
  - Publisert: 2025 (SINTEF)
  - Innhold: Argumenterer for nasjonalt byggskaderegister. Estimerer byggfeilkostnad til **10–30 mrd kr/år** basert på 2–6 % av omsetning (oppdatert fra 2008-data) ✅
  - URL/profiler bekreftet: https://www.sintef.no/en/all-employees/employee/lars.gullbrekken/ og https://www.sintef.no/en/all-employees/employee/jonas.holme/
- **Avvik fra dokumentet:** Ingen alvorlige. 10–30 mrd kr er avledet, ikke et primært målt tall (= 2–6 % av dagens omsetning). Bør fraseres som «anslått» i søknaden.
- **Status:** ✅ BEKREFTET (forfattere og tall bekreftet via SINTEF)
- **Kan brukes i søknaden:** Ja — som konsortieinternt notat (SINTEF), ikke uavhengig studie

---

### [Nordic Council of Ministers 2023] Building LCA and BIM Practices in Norway
- **Søkt:** Nordic Council Ministers 2023 Building LCA BIM practices Norway TemaNord pub.norden.org
- **Funnet:** Ja
- **Faktisk info:**
  - URL bekreftet: https://pub.norden.org/us2023-463/appendix-building-lca-and-bim-practices-in-norway.html ✅
  - Er vedlegg til TemaNord 2023-463
  - Innhold: bekrefter at LCA-reguleringer holdes svakere for SMB av konkurransehensyn ✅
  - Sitatet om SMB-skranke er fra dette dokumentet ✅
- **Avvik fra dokumentet:** Ingen.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [BKA2] Bærekraftige anskaffelser for vanlige bygg- og anleggsprosjekter, fase 2
- **Søkt:** BKA2 bærekraftige anskaffelser vanlige bygg fase 2 Trondheim kommune Knotten SINTEF 11,7 millioner
- **Funnet:** Ja
- **Faktisk info:**
  - URL: https://nit.no/prosjekter-og-innsikt/prosjekter/bærekraftige-anskaffelser-for-de-vanlige-bygg-og-anleggsprosjektene ✅
  - Budsjett: **11,7 MNOK** ✅
  - Prosjekteier: **Trondheim kommune** ✅
  - SINTEF er teknisk rådgiver med ansvar for datainnsamling ✅
  - Partnere: NiT, Trøndelag fylkeskommune, NTNU, Prosjekt Norge, RIF, EBA Trøndelag, Håndverkernes Samarbeidsforening Trondheim
  - Vegard Knottens navn ikke eksplisitt bekreftet i søkeresultatene — SINTEF-rollen er bekreftet
- **Avvik fra dokumentet:** Ingen alvorlige. Knottens personlige rolle er ikke eksternt bekreftet via søk, men er sannsynlig gitt SINTEF-tilknytningen.
- **Status:** ✅ BEKREFTET (H — prosjektside åpnet og bekreftet)
- **Kan brukes i søknaden:** Ja

---

### [Byggforskserien 700.320] Intervaller for vedlikehold og utskifting av bygningsdeler
- **Søkt:** Byggforskserien 700.320 vedlikehold utskifting bygningsdeler intervaller levetid SINTEF
- **Funnet:** Ja
- **Faktisk info:**
  - Tilgjengelig på: https://www.byggforsk.no/dokument/3312/intervaller_for_vedlikehold_og_utskifting_av_bygningsdeler ✅
  - Inneholder tabeller for vedlikeholds- og utskiftningsintervaller ✅
  - Eksplisitt forbehold: «skal ikke brukes direkte til å vurdere levetiden på en konkret eksisterende bygningsdel» ✅
  - Bak betalingsmur (abonnement på Byggforsk) — ikke fritt tilgjengelig
- **Avvik fra dokumentet:** Ingen. SotA siterer forbeholdet korrekt.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja — med eksplisitt forbehold

---

### [EBA 2023] Report on Green Loans and Mortgages
- **Søkt:** EBA 2023 Report on Green Loans green mortgages European Banking Authority December 2023
- **Funnet:** Ja
- **Faktisk info:**
  - Fullstendig: EBA/Op/2023/13
  - Publisert: **15. desember 2023** ✅
  - PDF: https://www.eba.europa.eu/sites/default/files/2023-12/e7bcc22e-7fc2-4ca9-b50d-b6e922f99513/EBA%20report%20on%20green%20loans%20and%20mortgages_0.pdf ✅
  - Innhold: foreslår frivillig EU Green Loan Label, integrering i Mortgage Credit Directive; grønne lån for energirenovering og SMB er under EU-målet; manglende data og harmoniserte definisjoner er bindende skranke ✅
- **Avvik fra dokumentet:** Ingen.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja

---

### [Ciroth et al. 2016] Pedigree-matrix uncertainty factors — ecoinvent
- **Søkt:** Ciroth 2016 pedigree matrix uncertainty factors ecoinvent International Journal of Life Cycle Assessment 21 1338
- **Funnet:** Ja
- **Faktisk info:**
  - Tittel: «Empirically based uncertainty factors for the pedigree matrix in ecoinvent»
  - Tidsskrift: *International Journal of Life Cycle Assessment*, Vol. 21, Issue 9, s. 1338–1348, 2016
  - DOI: **10.1007/s11367-013-0670-5**
  - Forfattere: Ciroth, Muller, Weidema, Lesage ✅
  - Innhold: empirisk grunnlag for usikkerhetsfaktorer i pedigree-matrisen (ecoinvent) ✅
- **Avvik fra dokumentet:** SotA sier «Vol. 21:1338» — riktig. Full tittel og DOI nå identifisert.
- **Status:** ✅ BEKREFTET
- **Kan brukes i søknaden:** Ja — SINTEF henter fulltekst via institusjonstilgang (var L/M i SotA)

---

### [Wiik 2025] SINTEF Notat nr. 57 — «Kostnadseffekten av klimatiltak i byggenæringen»
- **Søkt:** SINTEF Wiik 2025 Notat nr. 57 kostnadseffekten klimatiltak byggenæringen 20 prosent
- **Funnet:** Delvis
- **Faktisk info:**
  - Publikasjon funnet: «Effektive klimatiltak i byggenæringen: Kostnad og utslippskutt» — SINTEF, publisert **november 2025**
  - Forfatter: Marianne Kjendseth Wiik ✅
  - URL: https://www.sintef.no/publikasjoner/publikasjon/019a960bca35-d7a1c1b1-e59a-4d84-85d3-4f414c919dc6/
  - En annen side om samme: https://www.sintef.no/publikasjoner/publikasjon/10287146/
  - Innhold: sammenstilling av 34 vitenskapelige rapporter og artikler om kostnadseffektivitet. Funn: mange klimatiltak har liten eller ingen merkostnad; smartere design, riktige materialvalg og økt ombruk kan kutte utslipp raskere enn antatt.
  - «Notat nr. 57» og «opptil 20 %»-påstanden er **ikke bekreftet i søkeresultatene**
- **Avvik fra dokumentet:** Notat-nummeret (nr. 57) er ikke bekreftet eksternt. «opptil 20 prosent uten merkostnad» er ikke bekreftet i åpne søkeresultater — primærlesing er nødvendig.
- **Status:** ❓ DELVIS (publikasjonen eksisterer, SINTEF-sida kan åpnes, men notat-nr og 20%-påstand er ikke eksternt bekreftet)
- **Kan brukes i søknaden:** Med forbehold — SINTEF primærleser obligatorisk. Frasér som «mulighetsrom», ikke garanti.

---

## Oppsummerende tabell

| Kilde | Status | Søknadstrygg |
|---|---|---|
| **An & Pivo (2020)** *Real Estate Economics* DOI 10.1111/1540-6229.12228 | ⚠️ FEIL DOI/JOURNAL i SotA | Ja — med korrekt referanse og presisering (kommersiell/CMBS) |
| **IMT/UNC (~2012)** *Home Energy Efficiency and Mortgage Risks* | ❓ IKKE NAVNGITT | Ja — legg til som separat referanse (bolig, 32 %) |
| **Billio et al. (2022)** JREFE 65(3):419–450, DOI 10.1007/s11146-021-09838-0 | ✅ BEKREFTET | Ja |
| **Mecca (2023)** JMCDA DOI 10.1002/mcda.1818 | ✅ BEKREFTET | Ja — fulltekst via SINTEF |
| **Harerusten (2022)** NTNU-masteroppgave | ❓ IKKE FULLSTENDIG | Med forbehold — SINTEF verifiserer |
| **Benke et al. (2025)** *Scientific Data* PMC12218139 | ✅ BEKREFTET | Ja |
| **Weidema & Wesnæs (1996)** *J. Cleaner Production* 4(3–4):167–174 | ✅ BEKREFTET | Ja |
| **Edelen & Ingwersen (2018)** *Int. J. LCA* 23(4):759–772 PMC5919259 | ✅ BEKREFTET | Ja |
| **Lohman et al. (2023)** *ACS Environmental Au* PMC10197171 | ✅ BEKREFTET | Ja |
| **Finans Norge VASK 2023** 5,1 mrd / 10 per time | ⚠️ DELVIS — 78 500 er 2021-tall | Ja — bruk 10/time og 5,1 mrd med korrekt årstall |
| **Bank of England PS25/25** des. 2025 | ✅ BEKREFTET | Ja |
| **Bank of England DP1/25** juli 2025 | ✅ BEKREFTET | Ja — ikke klimareferanse |
| **Omnibus I (EU) 2026/470** vedtatt 24.02.2026 | ✅ BEKREFTET | Ja — riktig direktiv-nr: 2026/470 |
| **EN 15978:2026** CEN-CENELEC 17.04.2026 | ✅ BEKREFTET | Ja |
| **NS 3454 → NS-EN 16627** trukket 07.09.2023 | ✅ BEKREFTET | Ja |
| **Ingvaldsen/SINTEF Byggforsk 2008** 5 % / ¾ fukt | ⚠️ DELVIS — eldre data, primær-PDF ikke åpnet | Med forbehold — oppdater med Gullbrekken/Holme |
| **Gullbrekken & Holme (2025)** 10–30 mrd/år | ✅ BEKREFTET | Ja — merk: konsortieintern kilde |
| **Nordic Council (2023)** pub.norden.org | ✅ BEKREFTET | Ja |
| **BKA2** Trondheim, SINTEF, 11,7 MNOK | ✅ BEKREFTET | Ja |
| **Byggforskserien 700.320** | ✅ BEKREFTET | Ja — med forbehold om direkte bruk |
| **EBA (2023)** Green Loans report | ✅ BEKREFTET | Ja |
| **Ciroth et al. (2016)** Int. J. LCA 21(9):1338 | ✅ BEKREFTET | Ja — fulltekst via SINTEF |
| **Wiik (2025) SINTEF Notat nr. 57** | ❓ DELVIS — notat-nr og 20%-tall ubekreftet | Med forbehold — SINTEF primærleser obligatorisk |

---

## Handlingsliste etter kildesjekken

**KRITISK — MÅ RETTES FØR INNSENDING:**

1. **Fiks An & Pivo-referansen** i SotA §7 og §13:
   - Bytt DOI til `10.1111/1540-6229.12228`
   - Bytt journal til *Real Estate Economics*
   - Tydeliggjør at studien gjelder CMBS (kommersiell eiendom), ikke boliglån
   - 34 % = An & Pivo (CMBS, kommersiell) — hold dette adskilt fra 32 % (IMT/UNC, residensiell)

2. **Legg til IMT/UNC-studien** som separat referanse for «32 % lavere PD for energisertifiserte boliger»:
   - Kaza, N., Quercia, R.G. & Tian, C.Y. «Home Energy Efficiency and Mortgage Risks.» IMT/UNC Center for Community Capital. https://imt.org/resources/home-energy-efficiency-and-mortgage-risks/

3. **Vannskadestatistikk** — Dersom dokumentene bruker «78 500»: bytt til «10 vannskader per time i gjennomsnitt (2023)» med kilde Finans Norge Skadestatistikk for 2023.

**BØR GJØRES FØR INNSENDING:**

4. **Omnibus I** — legg til direktiv-nr «(EU) 2026/470» for OJ-forankring. Ikrafttredelse 18. mars 2026.

5. **Wiik 2025 notat** — SINTEF primærleser og bekrefter notat-nummer og 20%-påstanden.

6. **Harerusten 2022** — SINTEF henter via NTNU Open (https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/3108486) og bekrefter at 2,2 mrd-tallet stammer derfra.

7. **Mecca 2023** — SINTEF henter fulltekst (Wiley, DOI 10.1002/mcda.1818) via institusjonstilgang. Status løftes fra H* til H.

8. **Ciroth et al. 2016** — SINTEF henter fulltekst. DOI: 10.1007/s11367-013-0670-5. Status løftes fra L/M til H.

---

*Generert av Claude (Anthropic) i Cowork-modus, 2026-06-26. Alle søkefunn er fra WebSearch (sekundærkilder). Faglig primærverifisering eies av SINTEF (Knotten/Gullbrekken).*
