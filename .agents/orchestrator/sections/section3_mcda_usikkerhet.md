# 3. Flerkriterieanalyse og usikkerhet (MCDA)

## 3.1 Metodisk landskap for MCDA i bygg og arkitektur (Mecca 2023)

Flerkriterie-beslutningsanalyse (Multi-Criteria Decision Analysis, MCDA / MCDM) utgjør det teoretiske fundamentet for å veie sammen motstridende beslutningskriterier — som klimagassutslipp (LCA), livssykluskostnader (LCC), teknisk levetid og skaderisiko. I akademia og bærekraftlitteraturen innen bygge- og arkitektursektoren er MCDA-metodikk veletablert 🟡.

En kvantitativ gjennomgang av forskningslitteraturen innen urban og arkitektonisk bærekraft gjennomført av **Mecca (2023)** (`[Mecca2023]`, *Journal of Multi-Criteria Decision Analysis*, DOI 10.1002/mcda.1818 🟡) kartlegger den metodiske fordelingen av MCDA-anvendelser i sektoren:

- **Analytic Hierarchy Process (AHP): 46 %** 🟢/🟡. AHP er den mest utbredte metoden for kriteriavekting og hierarkisk strukturering av beslutningsproblemer gjennom parvise sammenligninger.
- **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS): 20 %** 🟢/🟡. TOPSIS benytter vektornormalisering for å rangere alternativer basert på kortest geometrisk avstand til en ideal positiv løsning og lengst avstand til en negativ ideal løsning.
- **Multi-Attribute Utility Theory / MIVES (Integrated Value Model for Sustainable Assessment): 11 %** 🟢/🟡. MIVES kombinerer verdefunksjoner og flerattributt utility-teori for å oversette heterogene fysiske enheter (kg CO₂e, NOK, år) til en standardisert verdiprosent.
- **Complex Proportional Assessment (COPRAS): 9 %** 🟢/🟡. COPRAS evaluerer alternativene basert på direkte proporsjonal sammenligning av nyttemaksimerende og kostnadsminimerende attributter.
- **Øvrige metoder (SAW, VIKOR, PROMETHEE, ELECTRE osv.): 14 %** 🟡.

### Modenhetsgap: Akademia vs. Norsk SMB-praksis

Selv om MCDA-metodene har høy teoretisk modenhet i faglitteraturen 🟡, er den praktiske modenheten og utrullingen i byggebransjen for lav — spesielt for norske små og mellomstore bedrifter (SMB-entreprenører) og boligkjøpere 🟢 (`[Nordic2023]`).

Forskningen peker på tre strukturelle skranker ved eksisterende MCDA-anvendelser i byggesektoren:
1. **Faseforskyvning:** Flertallet av studiene fokuserer på tildelingsfasen hos offentlige eller store byggherrer (*award phase*), eller på detaljprosjektering 🟡. Tidligfase beslutningsstøtte i **tilbudsfasen** (*tender phase*) for entreprenører er underutforsket.
2. **Spesialistavhengighet:** Metodene (som AHP og MIVES) krever omfattende ekspertinnsats for matrisekonstruksjon og vekting, noe SMB-aktører uten egne bærekraftavdelinger ikke har kapasitet til å gjennomføre 🟢 (`[Nordic2023]`).
3. **Ugjennomsiktig aggregering:** Mange akademiske MCDA-modeller summerer delskårer til én enkelt sammenrettet score uten å eksponere underliggende datakvalitet eller usikkerhet 🟢 (`[Edelen2018]`).

---

## 3.2 Synlig datakvalitet, usikkerhetsrepresentasjon og mulighetsrom

VERIFIEDs beslutningsmodell bygger på prinsippet om at manglende eller usikre data aldri skal skjules bak et fikst gennomsnittstall, men eksplisitt eksponeres som utvidet usikkerhet i beslutningsgrunnlaget 🟢 (`[Edelen2018]`, `[Lohman2023]`).

### 3.2.1 Datakvalitet og Pedigree-matrisen

For å håndtere usikkerhet i miljø- og livsløpsdata (LCI/LCA) benyttes **Weidema & Wesnæs (1996)** sin Pedigree-matrise (`[Weidema1996]` 🟡), videreutviklet av **Ciroth et al. (2016)** (`[Ciroth2016]` 🟡). Pedigree-matrisen vurderer datakvalitet langs fem uavhengige indikatorer (Data Quality Indicators – DQI):
1. **Pålitelighet (*Reliability*):** Verifiserte målinger vs. antakelser eller uverifiserte estimater.
2. **Kompletthet (*Completeness*):** Representativ utvalgsstørrelse og statistisk dekning.
3. **Tidsmessig korrelasjon (*Temporal correlation*):** Dataenes alder i forhold til prosjekteringstidspunktet.
4. **Geografisk korrelasjon (*Geographical correlation*):** Hvorvidt data representerer norske/nordiske forhold vs. globale prosesser.
5. **Teknologisk korrelasjon (*Technological correlation*):** Samsvar mellom den modellerte prosessen og den faktiske byggevaren.

Hver indikator skåres fra 1 (best) til 5 (dårligst). I databaser som ecoinvent omsettes Pedigree-skårene til lognormale variansfaktorer for å drive Monte Carlo-usikkerhetsanalyser 🟡 (`[ecoinvent]`).

### 3.2.2 Edelen & Ingwersen-prinsippet: Ingen skjult totalscore

Et avgjørende metodisk krav hentes fra **Edelen & Ingwersen (2018)** (`[Edelen2018]`, *Int. J. LCA*, PMC5919259 🟢): **Datakvalitet må vurderes ut fra formål, kontekst og beslutningsrolle, og må ALDRI komprimeres eller skjules i en enkelt totalscore.**

Høy datakvalitet på én dimensjon (f.eks. fersk tidsmessig data) kan ikke kompensere for alvorlige mangler på en annen dimensjon (f.eks. feil geografisk opprinnelse). En aggregert samlescore ville fungert som en ugjennomsiktig modell som tilslører risiko for brukeren. I steden skal datakvalitet og usikkerhet vises åpent for brukeren 🟢.

### 3.2.3 Synlig usikkerhetsrepresentasjon i moderne rammeverk (Lohman & EC3)

VERIFIED henter inspirasjon fra to ledende internasjonale rammeverk for synlig usikkerhet:
- **DMsan-rammeverket (Lohman et al. 2023)** (`[Lohman2023]`, *ACS Environ. Au*, PMC10197171 🟢): Demonstrerer hvordan MCDA for miljøvalg kan gjennomføres ved å eksponere usikkerhetsintervaller og følsomhet for kriteriavekter, i steden for å levere stive punktestimater.
- **EC3 / Building Transparency (`[EC3]` 🟢):** Viser et forbilledlig praksiseksampel ved å beregne og vise konfidensintervaller for innbygd karbon («conservative vs. achievable estimate»). Dersom en byggevare mangler spesifikk EPD og må bruke generiske data, straffes alternativet med et utvidet usikkerhetsspenn i brukergrensesnittet.

### 3.2.4 Klassifisering av datatilstander i VERIFIEDs testflate

I VERIFIEDs **testflate** kategoriseres datagrunnlaget for et **løsningsvalg** i fire eksplisitte datatilstander 🟢:

1. **Verifisert (*Verified*)** 🟢: Spesifikk, tredjepartsverifisert EPD (jf. EN 15804+A2 `[EN15804]` 🟡) eller godkjent FDV-dokumentasjon for det konkrete produktet. Lavest usikkerhetspåslag.
2. **Generisk (*Generic*)** 🟢/🟡: Standard sertifiserte databasedata (f.eks. EPD-Norge eller ecoinvent). I henhold til TEK17 § 9-2 og DiBK-veiledning illegges generiske miljødata et **sikkerhetspåslag på 1,25 (25 % utslippsstraff)** for å ta høyde for variasjon 🟢.
3. **Estimert (*Estimated*)** 🟡: Proxydata basert på tilstøtende materialgrupper eller sjablongverdier.
4. **Manglende (*Missing*)** 🔴/🟡: Dokumentasjon mangler fullstendig. Tilstanden synliggjøres eksplisitt som et rødt datagap med maksimal usikkerhetsmargin, heller enn å gi en tilfeldig skjønnsmessig verdi.

| Datatilstand | Kildegrunnlag | TEK17 1,25-påslag | Usikkerhetsmargin i testflaten | Gate-status |
| :--- | :--- | :---: | :--- | :---: |
| **Verifisert** | Spesifikk EPD / FDV | Nei | Smalt konfidensintervall | 🟢 |
| **Generisk** | Bransje-EPD / ecoinvent | **Ja (+25 %)** | Videre konfidensintervall (TEK17-straff) | 🟢/🟡 |
| **Estimert** | Proxydata / sjablong | Ja | Betydelig usikkerhetsspenn | 🟡 |
| **Manglende** | Ingen data tilgjengelig | Maks påslag | Eksplisitt synliggjort datagap | 🔴/🟡 |

### 3.2.5 Mulighetsrom-visualisering (*Opportunity Spaces*)

I steden for å peke ut én stiv «vinner», benytter VERIFIEDs testflate **mulighetsrom-visualisering (*opportunity space visualization*)** 🟢 (`[Lohman2023]`, `[EC3]`). 

Mulighetsrommet viser under hvilke vektingspreferanser et gitt løsningsvalg vil dominere:
- Dersom entreprenøren eller kunden prioriterer lavest initiale LCA-utslipp (A1–A3) 🟢 (`[KD2024]`), vil alternativer med verifiserte EPD-er dominere.
- Dersom fokus flyttes mot laveste levetidskostnader (LCC jf. NS-EN 16627 `[NS-EN16627]` 🟢) og høy fuktrobusthet/holdbarhet (DNSH-bredde) 🟢 (`[FinansNorge2024VASK]`), vil løsningsvalg med lengre utskiftingsintervaller og dokumentert skaderisiko tre fram i mulighetsrommet.

Dette gir en pedagogisk og forklarbar **beslutningsstøtte** der brukeren selv ser konsekvensene av sine prioriteringer 🟢.

---

## 3.3 Metodisk forbehold: Ranginversjon (Rank Reversal) i TOPSIS, COPRAS og VIKOR

### 3.3.1 Problemet med Ranginversjon

Et veletablert fenomen i litteraturen om flerattributt-analyse er **ranginversjon (*Rank Reversal*)** 🟡. Fenomenet oppstår i klassiske vektornormaliseringsmetoder som TOPSIS, COPRAS og VIKOR:

> Ranginversjon inntreffer når introduksjonen eller fjerningen av et uavhengig alternativ (eller marginale endringer i kriterievekter) fører til at den innbyrdes rangeringen mellom to uberørte alternativer uventet snur.

For eksempel: Dersom løsningsvalg A vurderes som bedre enn løsningsvalg B, og et nytt løsningsvalg C legges til i sammenligningen, kan vektornormaliseringen i TOPSIS/COPRAS medføre at B plutselig rangeres foran A — selv om egenskapene til A og B er uendrede.

### 3.3.2 Metodisk forbehold og forskningshypotese i VERIFIED

I VERIFIED-prosjektet framsettes håndtering av ranginversjon som et **metodisk forbehold (*methodological reservation*)** og en FoU-hypotese, **ikke som en ferdig empirisk bevist løsning** 🟢:

1. **Ingen absolutt påstand om eliminering:** VERIFIED påstår ikke å ha eliminert ranginversjon i alle MCDA-konfigurasjoner, men behandler ranginversjon som en kjent metodisk begrensning ved etablerte vektornormaliserende MCDA-algoritmer 🟢.
2. **Sensitivitetsvarsling i testflaten:** I steden for å skjule rangfølsomhet, skal VERIFIEDs testflate teste grensesnitt som varsler brukeren dersom relaterte alternativer ligger nær hverandre i utfall, eller dersom rangeringen er såfremt følsom for vektendringer at ranginversjon kan inntreffe 🟢.
3. **Stabilitetsvurdering:** Prosjektet skal undersøke om kombinasjonen av AHP-basert kriteriavekting og MIVES-baserte verdefunksjoner (som benytter absolutt heller enn relativ normalisering) reduserer risikoen for uønsket ranginversjon i tilbudsfasen 🟡 (`[Mecca2023]`).

---

## 3.4 Syntese og VERIFIEDs testflate for tilbudsfasen

Syntesen av flerkriterieanalyse og usikkerhetsrepresentasjon definerer VERIFIEDs nyhetsverdi langs **fire sentrale akser** i prosjektets forskningsgapsmatrise 🟢 (`[spec_miner_1]`):

- **Akse (c) Brukergruppe:** Tilpasset for SMB-entreprenører og boligkjøpere (ikke-spesialister). Komplekse matriseberegninger skjules bak et intuitivt grensesnitt som viser resultatene uten krav om dyp LCA-kompetanse 🟢 (`[Nordic2023]`).
- **Akse (d) Forklarbarhet og usikkerhet:** Full transparens i datakilde, TEK17 1,25-påslag, Pedigree-usikkerhet og datatilstander (verifisert, generisk, estimert, manglende).
- **Akse (e) Beslutningseffekt:** Måling og attribusjon av om beslutningsstøtten faktisk bekrefter, endrer eller påvirker entreprenørens tilbudsvalg før kontraktsinngåelse.
- **Akse (f) DNSH-bredde:** Integrerer LCC (NS-EN 16627 `[NS-EN16627]` 🟢), teknisk levetid (Byggforsk 700.320 🟡) og fuktrisiko (`[FinansNorge2024VASK]` 🟢) sammen med klimagassutslipp (A1–A3 🟢 `[KD2024]`).

### Ontologisk og terminologisk samsvar

Gjennomgående i hele analysen og prosjektutformingen overholdes de ontologiske kontrollreglene fra `vibs-verified-ord-og-kildekart-v0.5.yml` 🟢:
- Begrepet **«løsningsvalg»** benyttes konsekvent for å omfatte byggevare, installasjonsmetode, utskiftingsintervall og livssyklusegenskaper i tilbudsfasen (i motsetning til det smale begrepet «produktvalg»).
- Plattformen omtales presist som en **«testflate»** for utprøving av beslutningsmodeller.
- VERIFIED sin rolle defineres entydig som **«beslutningsstøtte»** som sammenligner, forklarer og belyser konsekvenser. 
- Uttrykk som indikerer automatiserte valg («VERIFIED velger / anbefaler automatisk») og lukkede modeller («svart boks») er strengt unngått.
- Effektelementer omtales konsekvent som FoU-hypoteser som skal testes («VERIFIED skal teste om...»), uten ubelagte påstander om etablert årsakssammenheng.
