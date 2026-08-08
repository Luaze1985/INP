# Section 5: Norsk SMB-kontekst og tilbudsbeslutninger

## 5.1 Reguleringskontekst og lempelighetsbegrunnelse for SMB-konkurransekraft 🟢

Bygg- og anleggssektoren i Norge preges av en høy andel små og mellomstore bedrifter (SMB), spesielt innen boligbygging, rehabilitering og lokalentrepreniser. Når myndighetene og EU innfører skjerpede miljø- og klimaforordninger, oppstår et regulatorisk dilemma: Hvordan sikre reduksjon i klimagassutslipp og miljøbelastning uten å påføre mindre aktører uforholdsmessig store administrative byrder?

Nordisk Ministerråd (2023) dokumenterer i rapporten *Building LCA and BIM practices in Norway* (`[Nordic2023]` 🟢) at norske klimagassberegningskrav for bygg er bevisst utformet med lempeligere krav og større fleksibilitet for SMB-er enn for storskalaprosjekter:

> *«The regulations for LCA of buildings are less stringent than what large actors are doing. This is driven mainly by a fear of reducing the competitiveness for smaller actors who might not have resources to follow stringent regulations.»* (`[Nordic2023]` 🟢)

Denne lempelighetsbegrunnelsen er metodisk og markedsmessig avgjørende:
1. **Konkurransekraft for SMB-er 🟢:** Strengere krav om fullskala livsløpsanalyser (LCA) og detaljerte EPD-beregninger i tidligfase ville favorisert store riksentreprenører med egne miljøavdelinger og spesialiserte rådgivere.
2. **Kapasitetsskranker hos ikke-spesialister 🟢:** Mindre entreprenører og håndverksbedrifter mangler både tid, verktøykompetanse og finansielle ressurser til å gjennomføre komplekse spesialistanalyser under tilbudsarbeid.
3. **Konsekvens for tilbudsbeslutninger 🟢:** Resultatet er at material- og løsningsvalg i tilbudsfasen hos norske SMB-er i stor grad har vært basert på innkjøpspris, etablerte leverandørrelasjoner og erfaringstall, snarere enn dokumentert miljøavtrykk, levetidskostnader (LCC) eller fuktrobusthet.

Forordninger som Byggevareforordningen (`[CPR2024]` 🟢) og ESPR (`[ESPR2024]` 🟢) innfører gradvis krav om digitale produktpass (DPP), men uten tilpasset beslutningsstøtte vil dette informasjonskravet forsterke skranken for SMB-er. Det eksisterer derfor et udekket behov for en forenklet, forklarbar testflate som setter SMB-entreprenører og boligkjøpere i stand til å vurdere heterogene byggevaredata direkte i tilbudsfasen.

---

## 5.2 BKA2-prosjektet: Bærekraftige anskaffelser i praksis 🟢

Det pågående forsknings- og utviklingsprosjektet **BKA2** (*Bærekraftige anskaffelser for de vanlige bygg- og anleggsprosjektene, fase 2*, 2024–2028) (`[BKA2]` 🟢) adresserer direkte utfordringen med å innføre bærekraftskriterier i hverdagsbyggeriet.

### Nøkkelfakta om BKA2 (`[BKA2]` 🟢):
- **Prosjekteier og ramme:** Prosjektet ledes av Trondheim kommune med et totalbudsjett på **11,7 MNOK** over perioden 2024–2028.
- **FoU-partner:** SINTEF v/ seniorforsker Vegard Knotten er sentral FoU-partner.
- **Formål:** Utvikle, teste og standardisere praktiske bærekraftskriterier for offentlige og private anskaffelser i de «vanlige» bygg- og anleggsprosjektene – det vil si prosjektene som utgjør hovedtyngden av SMB-entreprenørenes marked.

### Synergi og grensesnitt mot VERIFIED (`[BKA2]` 🟢):
BKA2 og VERIFIED er komplementære initiativer som sammen tetter broen mellom anskaffelseskrav og tilbudsbeslutninger:

1. **BKA2 fokuserer på bestillersiden (kriterier og krav) 🟢:** BKA2 utvikler tildelingskrav og evalueringsopplegg for byggherrer som ønsker å etterspørre bærekraft uten å ekskludere SMB-aktører.
2. **VERIFIED fokuserer på tilbydersiden og beslutningsmodellen (testflate) 🟢:** VERIFIED leverer den underliggende flerkriterie-beslutningsmodellen og programvarebaserte testflaten som gjør det mulig for SMB-entreprenøren å sammenligne alternativer og dokumentere samlet bærekraft (LCA, LCC, levetid, fuktrobusthet) i sitt tilbud til kunden.
3. **Faglig overføring via SINTEF 🟢:** Vegard Knottens sentrale rolle i både BKA2 og VERIFIED sikrer sømløs felles utnyttelse av forskningsinnsikt om SMB-atferd, uten duplisering av FoU-innsats.

---

## 5.3 Kartlegging og analyse av eksisterende verktøy (Konkurrentscan) 🟡

For å kartlegge nyhetsverdien til VERIFIED er det gjennomført en grundig analyse av eksisterende programvareverktøy i det norske og internasjonale markedet. Analysen avkrefter påstanden om at norske SMB-er overhodet ikke har tilgang til miljøverktøy, men viser samtidig at alle eksisterende løsninger er begrenset til enkeltkriterier eller prosjekteringsfasen.

```
+-----------------------------------------------------------------------------------+
|               KARTLEGGING AV EKSISTERENDE VERKTØY I NORSK OG INTL. MARKED         |
+---------------------+-----------------------------------+-------------------------+
| Verktøy             | Hovedfokus / Sterkeste akse       | Begrensning / Gap       |
+---------------------+-----------------------------------+-------------------------+
| SmartKalk Miljø 🟡   | Kalkyleintegrert EPD-oppslag      | Enkriterium (kun CO₂),  |
| (Holte, Norge)      | i tilbudsfasen (NOBB/EPD)         | ingen LCC/fukt/DQI      |
+---------------------+-----------------------------------+-------------------------+
| Reduzer 🟡          | Anbudsprosess og klimagass-       | Enkriterium (kun CO₂),  |
| (NTNU-spinoff, NO)  | optimalisering (15 000+ EPD-er)   | ingen LCC/usikkerhet    |
+---------------------+-----------------------------------+-------------------------+
| Concular 🟡         | Ombrukskatalog, materialpass      | Ombruksmatching, ikke   |
| (Tyskland)          | og ombruk+garanti-rammeverk       | tilbudsfase-MCDA        |
+---------------------+-----------------------------------+-------------------------+
| ORIS 🟡             | Infrastruktur/anlegg, masse-      | Manuell input, anlegg,  |
| (Frankrike/Intl)    | transport-LCA og rutevalg         | ikke byggevare-MCDA     |
+---------------------+-----------------------------------+-------------------------+
| EC3 🟢              | Synlige usikkerhetsintervaller    | Kun karbon; mangler LCC |
| (Building Transp.)  | for innbygd CO₂ ("achievable")    | og fuktrisiko           |
+---------------------+-----------------------------------+-------------------------+
| One Click LCA 🟡    | Spesialist-LCA/LCC for            | Prosjektering/ekspert,  |
| (Finland)           | prosjekterende ingeniører         | ingen synlig DQI/attrib.|
+---------------------+-----------------------------------+-------------------------+
```

### 1. SmartKalk Miljø (Holte, Norge) 🟡
- **Funksjonalitet og praksis 🟡:** SmartKalk Miljø er integrert direkte i Holtes kalkulasjonsprogramvare for entreprenører. Verktøyet henter maskinlesbare EPD-data koblet til NOBB-databasen (`[NOBB]` 🟡), slik at kalkylatøren kan se CO₂-utslipp parallelt med prisberegningen under tilbudsarbeidet.
- **Nyhet: Rejser påstanden om at SMB-er kun ser på pris 🟢:** Eksistensen og bruken av SmartKalk Miljø motbeviser påstanden om at norske SMB-entreprenører utelukkende vurderer innkjøpspris. Verktøyet viser at SMB-aktører er villige til å bruke miljødata dersom dataene er integrert direkte i deres etablerte kalkulasjonsarbeidsflyt.
- **Begrensninger mot VERIFIED 🟡:** SmartKalk Miljø er et **enkriterieverktøy** fokusert på klimagassutslipp (kg CO₂e). Det mangler flerkriterieanalyse (MCDA), livssykluskostnader (LCC etter NS-EN 16627 `[NS-EN16627]` 🟡), teknisk levetids- og fuktrisikovurdering, synlige datakvalitetsindikatorer (DQI etter Edelen & Ingwersen 2018 `[Edelen2018]` 🟢), samt mønstre for måling og attribusjon av faktisk beslutningseffekt.

### 2. Reduzer (Norge / NTNU spin-off) 🟡
- **Funksjonalitet og praksis 🟡:** Reduzer er en norsk programvareplattform utviklet for å forenkle klimagassberegninger i anbudsprosesser. Plattformen inneholder en database med over 15 000 EPD-er og tilbyr automatiserte karbonestimater for byggeprosjekter.
- **Sterke sider 🟡:** Svært godt tilpasset norsk anbudskontekst og har et moderne, brukervennlig grensesnitt rettet mot entreprenører.
- **Begrensninger mot VERIFIED 🟡:** Reduzer er i praksis et **enkriterieverktøy for klimagasser**. Det tilbyr ikke integrerte livssykluskostnader (LCC), vurdering av fuktrobusthet eller teknisk holdbarhet, eksplisitt usikkerhetseksponering per løsningsvalg, eller loggingsmoduler for å måle om beslutningsstøtten faktisk endret entreprenørens tilbud.

### 3. Concular (Tyskland) 🟡
- **Funksjonalitet og praksis 🟡:** Concular er en ledende europeisk plattform for sirkulær økonomi i byggesektoren. Plattformen tilbyr digitale materialpass, ombrukskartlegging ved rivning, CircularLCA, samt et integrert garanti- og kvalitetssikringsrammeverk (*ombruk+garanti*) for brukte byggevarer.
- **Sterke sider 🟡:** Pioner innen ombruksmatching, restverdivurdering og garantiordninger for brukte materialer.
- **Begrensninger mot VERIFIED 🟡:** Concular er spesialisert mot ombrukskartlegging, demontering og avfallsreduserende materialutveksling. Det utgjør ikke et flerkriterie beslutningsstøtteverktøy for ordinære tilbudsbeslutninger i nybygg- og rehabiliteringsprosjekter for norske SMB-er.

### 4. ORIS (Frankrike / Internasjonalt) 🟡
- **Funksjonalitet og praksis 🟡:** ORIS er en digital plattform for bærekraftig infrastruktur og anleggsbygging (vei, bane, masseforflytning). Plattformen analyserer transportveier, råmaterialkilder og CO₂-avtrykk basert på geografiske data.
- **Sterke sider 🟡:** Avansert optimalisering av transport-LCA og massehåndtering for anleggsprosjekter.
- **Begrensninger mot VERIFIED 🟡:** ORIS krever i stor grad **manuell parameterinntasting** og er skreddersydd for tung infrastruktur og vegbygging, ikke for bygningsmessige løsningsvalg, EPD/FDV-kobling eller LCC-beregninger for SMB-byggentreprenører.

### 5. Internasjonale benchmark-referanser (EC3, One Click LCA, Cobuilder)
- **EC3 (Building Transparency, USA) 🟢:** EC3 utmerker seg ved sin forbilledlige håndtering av usikkerhet i innbygd CO₂ («conservative vs. achievable emissions»). EC3 viser synlige konfidensintervaller, men er et enkriterieverktøy for karbon, uten kobling til LCC, fuktrisiko eller tilbudsarbeidsflyten for norske SMB-er.
- **One Click LCA (Finland) 🟡:** Markedsledende spesialistverktøy for LCA og LCC (NS-EN 16627). Utviklet for prosjekterende ingeniører og miljørådgivere i prosjekteringsfasen. Mangler synlig usikkerhet per alternativ i grensesnittet og har ingen funksjon for å attribusjonsteste beslutningspåvirkning hos SMB-brukere.
- **Cobuilder (Norge) 🟡 & Madaster (Nederland) 🟡:** Cobuilder leverer strukturert datainfrastruktur (DPP-klare produktdata), mens Madaster leverer materialpass og sirkularitetsindekser. Begge utgjør verdifulle datakilder, men fungerer som datalag snarere enn beslutningsstøtte i tilbudsfasen.

---

## 5.4 Syntese og VERIFIEDs avgrensede FoU-gap (6-aksematrise)

Kartleggingen viser et entydig mønster: Eksisterende verktøy dekker enkeltelementer med høy modenhet, men lever i adskilte siloer. VERIFIEDs nyhetsverdi ligger ikke i å oppfinne nye isolerte enkeltmetoder, men i den **integrerte syntesen av seks akser** i én forklarbar testflate for norsk SMB-kontekst.

```
+-----------------------------------------------------------------------------------------------------------------------+
|                                  SAMMENSTILT FUNKSJONSMATRISE OG FOU-GAP (6 AKSER)                                    |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| Verktøy / Kilde  | (a) Dataintegr.  | (b) Tilbudsfase  | (c) SMB-gruppe   | (d) Usikkerhet   | (e) Beslutn.eff. | (f) DNSH-bredde  |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| SmartKalk Miljø  | Delvis (LCA+Pris)|      YES         |      YES         |       NO         |       NO         |       NO         |
| Reduzer 🟡       | NO (Kun LCA)     |      YES         |      YES         |       NO         |       NO         |       NO         |
| Concular 🟡      | Delvis (Ombruk)  |       NO         |    Delvis        |       NO         |       NO         | Delvis (Ombruk)  |
| ORIS 🟡          | Delvis (Transp)  |    Delvis        |       NO         |       NO         |       NO         |       NO         |
| One Click LCA 🟡 | YES (LCA+LCC)    |    Delvis        |       NO         |       NO         |       NO         | Delvis (LCC)     |
| EC3 🟢           | NO (Kun LCA)     |    Delvis        |    Delvis        |      YES         |       NO         |       NO         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
| VERIFIED (Mål)   |      YES         |      YES         |      YES         |      YES         |      YES         |      YES         |
+------------------+------------------+------------------+------------------+------------------+------------------+------------------+
```

### De seks aksene i VERIFIEDs FoU-gap:

1. **Akse (a) Dataintegrasjon 🟢:** Integration av heterogene datakilder i én modell: EPD/LCA (A1–A3, C, D) + LCC (NS-EN 16627 `[NS-EN16627]` 🟡) + teknisk levetid (Byggforskserien 700.320 `[Byggforsk700.320]` 🟡) + fuktrobusthet/skaderisiko + ombruksbarhet.
2. **Akse (b) Fase (Tilbudsfasen) 🟢:** Opererer eksplisitt i tilbudsfasen (*tilbudsfasen*) før kontrakt signeres og før løsningsvalg låses i detaljprosjektering. Tidligfasebeslutninger i A1–A3 står for opptil **70 % av bygningsmaterialenes klimagassutslipp** (`[KD2024]` 🟡), der handlingsrommet for utslipps- og kostnadsreduksjon er størst uten merkostnad (`[EBA_NO2023]` 🟡).
3. **Akse (c) Brukergruppe (Ikke-spesialister) 🟢:** Utformet for SMB-entreprenører og kunden (*ikke-spesialister*). Krevende LCA- og LCC-analyser forenkles til et forståelig visualisert sammenligningsgrunnlag uten at kunden må ansette egne miljørådgivere.
4. **Akse (d) Forklarbarhet og usikkerhet 🟢:** Ingen skjult totalscore eller «svart boks». Datakvalitet og usikkerhet eksponeres åpent gjennom DQI-kategorier (verifisert EPD, generisk data med TEK17 1,25-påslag `[Edelen2018]` 🟢, estimert proxy-data, manglende data). Usikkerhet formidles som konfidensintervaller og handlingsrom («opportunity spaces» `[Lohman2023]` 🟢).
5. **Akse (e) Beslutningseffekt og attribusjon 🟢:** Systemet inneholder innebygd loggingsarkitektur for å måle om presentasjonen av sammenlignbare data faktiske påvirket, endret eller bekreftet entreprenørens og kundens endelige løsningsvalg i tilbudet.
6. **Akse (f) Bredde i bærekraft (DNSH-prinsippet) 🟢:** Rommer Do No Significant Harm (DNSH)-kriterier som fuktrobusthet (forebygging av vannskade; Finans Norge 2023-statistikk viser 10 vannskader/time og 5,1 mrd. kr utbetalt `[FinansNorge2024VASK]` 🟢), teknisk levetid og lave livsløpskostnader, i stedet for å utelukkende prioritere lavest initial CO₂.

---

## 5.5 Ontologiske guardrails og kildekritisk forankring 🟢

For å sikre vitenskapelig konsistens og samsvar med autoritativ kildedom i prosjektet, gjelder følgende ontologiske føringer strengt for Section 5:

1. **«Løsningsvalg» fremfor «produktvalg» 🟢:** Det benyttes konsekvent begrepet **«løsningsvalg»**, ettersom tilbudsbeslutningen omfatter både produktvalg, monteringsmetode, vedlikeholdsintervaller, levetid og LCC-profil.
2. **«Testflate» og «beslutningsstøtte» 🟢:** VIBS VERIFIED omtales som en **«testflate»** for **«beslutningsstøtte»**. Påstander som «VERIFIED velger automatisk», «VERIFIED anbefaler optimal løsning» eller referanser til en «svart boks» er eksplisitt forbudt. Entreprenøren beholder alltid det faglige ansvaret for tilbudet.
3. **Målgruppe 🟢:** Målgruppen omtales som **«entreprenør og kunde»** eller **«ikke-spesialister»**.
4. **Effektpåstander som FoU-hypoteser 🟢:** Årsakssammenhenger fremstilles som hypoteser som skal testes («prosjektet skal undersøke om...», «testflaten skal evaluere om...»), ikke som ferdig bevisste årsakseffekter.
5. **Korrekt kildeseparasjon (`[EBA_EU2023]` vs `[EBA_NO2023]`) 🟢:** 
   - `[EBA_EU2023]` 🟢 refererer utelukkende til European Banking Authority (des. 2023) angående grønne lån og bankregulering.
   - `[EBA_NO2023]` 🟡 refererer utelukkende til Entreprenørforeningen Bygg og Anlegg (Norge), Grønn Byggallianse og Norsk Eiendom angående veileder for 20 % CO₂-reduksjon i boligblokker.
6. **Behandling av parkerte kilder (⏸) 🟢:**
   - `[Wiik2025]` ⏸ (SINTEF Notat 57) og `[SA2018]` ⏸ (Samfunnsøkonomisk analyse 4-2018) opprettholdes som **⏸ Parkert** per prosjektleders beslutning (Lars Gunnar 2026-06-28). Påstander om tidligfaserom og 20 % klimagassreduksjon forankres i de bærende/aktive kildene `[EBA_NO2023]` 🟡 og `[KD2024]` 🟡.

---

### Formelt FoU-gap utsagn for VERIFIED (Konklusjon):

> **«Innenfor det undersøkte utvalget av verktøy finnes enkeltkomponenter, men ingen enkeltverktøy kombinerer alle 6 akser i en integrert, forklarbar testflate for beslutningsstøtte for norske SMB-er i tilbudsfasen.»** 🟢
