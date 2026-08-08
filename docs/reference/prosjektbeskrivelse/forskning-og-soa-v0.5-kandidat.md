# VIBS VERIFIED — State of the Art og Forskningsevaluering (v0.5 Kandidat)

**Dokument-ID:** `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`  
**Status:** Utkast for SINTEF-evaluering og Norsk forskningsråd (NFR IPN 2026)  
**Kilde- og ontologikontroll:** Verifisert i tråd med `vibs-verified-ord-og-kildekart-v0.5.yml`, `ipn-kildebibliotek.md` og `vibs-verified-kildedom-2026-06-27.md`.

---

# Seksjon 1: Sammendrag og hovedkonklusjon for SINTEF-evaluering

## 1.1 Formål og kontekst for SINTEF-evalueringen
Denne State of the Art (SoA)-rapporten utgjør det autoritative, kildekritiske og vitenskapelige fundamentet for SINTEF sin evaluering av forskningshøyde (FoU-høyde), nyhetsverdi og metodisk gjennomførbarhet i prosjektet **VIBS VERIFIED** (Norges forskningsråd, IPN 2026, avgrenset til 1–16 MNOK med 50 % maksimal støttesats `[NFR_IPN2026]` 🟢).

Rapporten kartlegger det internasjonale og nasjonale forskningsfrontlandskapet innen fire sammenhengende domener:
1. **Livsløpsanalyse (LCA) og livssykluskostnader (LCC)**, med vekt på datakvalitetsindikatorer (DQI) og TEK17 § 9-2.
2. **Flerkriterie-beslutningsanalyse (MCDA)** og synlig usikkerhetsrepresentasjon uten ugjennomsiktige aggregatskårer.
3. **Finans- og reguleringskontekst**, herunder empiriske korrelasjoner mellom energieffektivitet, bygningskvalitet og kredittrisiko (Probability of Default, PD).
4. **Norsk SMB-kontekst og tilbudsbeslutninger**, herunder eksisterende programvareverktøy og Nordisk Ministerråds lempelighetsbegrunnelse for små og mellomstore bedrifter.

## 1.2 Kjerneutfordring og forskningshøyde (FoU-høyde)
Kartleggingen bekrefter at **70 % av de materialrelaterte klimagassutslippene** (modulene A1–A3 i EN 15804+A2 `[EN15804]` 🟡) i representative referansebygg låses i de tidlige valgene av materialer og utførelse (`[KD2024]` 🟡). For at små og mellomstore entreprenører (SMB) og deres kunder (*ikke-spesialister*) skal kunne foreta reelle lavutslippsvalg, må **løsningsvalg** evalueres direkte i **tilbudsfasen** — før prosjekteringen og kontraktene fastlåses `[Nordic2023]` 🟢 `[BKA2]` 🟢.

Dagens praksis preges imidlertid av to alvorlige barrierer:
- **Metodisk silo-oppsplitting:** Miljøpåvirkning (LCA), levetidskostnader (LCC per NS-EN 16627 `[NS-EN16627]` 🟢, der den eldre NS 3454 eksplisitt er trukket tilbake 07.09.2023), teknisk levetid (Byggforsk 700.320 `[Byggforsk700.320]` 🟡) og fuktrobusthet/skaderisiko (over 87 600 årlige vannskader og 5,1 mrd. kr i utbetalinger per Finans Norge 2023 `[FinansNorge2024VASK]` 🟢) behandles i adskilte systemer.
- **Ugjennomsiktig usikkerhet og spesialistkrav:** Eksisterende beslutningsmodeller baserer seg enten på spesialistkrevende ekspertsystemer eller aggregerer indikatorer til én enkelt skjult totalscore ("svart boks"). Dette bryter med formålsavhengig datakvalitetsmetodikk (Edelen & Ingwersen 2018 `[Edelen2018]` 🟢) og forhindrer transparente avveininger for ikke-spesialister.

## 1.3 Det finansielle risikolenket og det udekket forskningsgapet
Mens nyere finansiell litteratur (Kaza et al. 2014 `[Kaza2014]` 🟢; Billio et al. 2022 `[Billio2022]` 🟢; An & Pivo 2020 `[An2020]` 🟡) empirisk bekrefter at energieffektivitet reduserer misligholdsrisiko (PD) på bolig- og næringslån med opptil 32–34 %, avdekker SoA-rapporten et **krystallklart udekket forskningsgap**:
> *Det finnes i dag ingen empirisk litteratur eller metodiske rammeverk som kobler bygningsteknisk kvalitet, materialenes holdbarhet, levetid, fuktrobusthet eller vedlikeholdsbyrde direkte til bankenes finansielle risikomodeller (IRB PD/LGD).*

Regulatoriske initiativ fra European Banking Authority (EBA EU 2023 `[EBA_EU2023]` 🟢) og Bank of England (PS25/25 `[BoE_PS25-25]` 🟡; DP1/25 `[BoE_DP1-25]` 🟡) understreker at manglende harmoniserte bygningsdata utgjør den primære flaskehalsen for grønn utlånspraksis. VERIFIED adresserer dette gapet ved å undersøke om byggetekniske levetids- og risikodata kan oversettes til risikoparametere for finanssektoren.

## 1.4 Sammenstilling av eksisterende verktøy (6-aksers syntese)
En systematisk kartlegging av markedets eksisterende verktøy i Norge og internasjonalt viser følgende:
- **SmartKalk Miljø 🟡 & Reduzer 🟡:** Tilbyr kalkylerelevant EPD-oppslag i tilbudsfasen, men er avgrenset til **enkriterium for klimagasser (CO₂)** uten LCC, levetid, fuktrobusthet eller synlig usikkerhet.
- **Concular 🟡 & ORIS 🟡:** Tilbyr henholdsvis ombrukskataloger/garantiordninger og infrastruktur-LCA, men mangler tilbudsfase-MCDA for bygningsmessige løsningsvalg.
- **EC3 🟢 & One Click LCA 🟡:** EC3 viser forbilledlige usikkerhetsintervaller ("achievable vs. conservative"), men dekker kun karbon. One Click LCA tilbyr avansert LCA/LCC, men er utformet for prosjekterende ingeniører i detaljfasen uten synlige datakvalitetsindikatorer per valgmulighet.

Ingen av de undersøkte verktøyene integrerer samtlige 6 nødvendige akser i en tilpasset arbeidsflyt for norske SMB-entreprenører og boligkjøpere.

## 1.5 Hovedkonklusjon og formelt FoU-gap statement
Basert på den kildekritiske gjennomgangen av forskningslitteratur, standarder, finansiell regulering og eksisterende programvarerelaterte løsninger, formuleres VERIFIED-prosjektets formelle, avgrensede FoU-gap slik:

> **«Innenfor det undersøkte utvalget av verktøy finnes enkeltkomponenter, men ingen enkeltverktøy kombinerer alle 6 akser i en integrert, forklarbar testflate for beslutningsstøtte for norske SMB-er i tilbudsfasen.»** 🟢

VERIFIED-prosjektets nyhetsverdi og FoU-høyde ligger dermed i å utvikle, teste og evaluere en **testflate** for **beslutningsstøtte** som samler LCA, LCC, levetid, fuktrobusthet og finansiell risikokobling i én transparent flerkriteriemodell med synlig usikkerhet.

---

# Seksjon 2: Metodisk fundament (LCA/LCC og datakvalitet)

## 2.1 Oversikt og metodisk innramming

Det metodiske fundamentet for verifisert og bærekraftig beslutningsstøtte i byggenæringen hviler på to komplementære analysegrenser: **klimagass- og miljøvurdering gjennom livsløpsanalyse (LCA - Life Cycle Assessment)** og **økonomisk livssyklusanalyse (LCC - Life Cycle Costing)**. I dagens praksis behandles miljøpåvirkning og levetidskostnader som adskilte fagsiloer, hovedsakelig tilpasset spesialister i prosjekteringsfasen etter at de vesentligste arkitektoniske og materialmessige rammene er låst `[Nordic2023]` 🟢.

For at små og mellomstore entreprenører (SMB) og deres kunder skal kunne foreta kunnskapsbaserte og bærekraftige **løsningsvalg** allerede i **tilbudsfasen**, kreves et integrert datagrunnlag der miljødata, kostnader, levetidsintervaller og skaderisiko sammenstilles transparent `[BKA2]` 🟢. VERIFIED-prosjektet har som mål å utvikle og teste en **beslutningsstøtte** som sammenligner heterogene byggevaredata i en intuitiv **testflate**, der datakvalitet og usikkerhet eksplisitt synliggjøres i stedet for å skjules bak en skjult totalscore `[Edelen2018]` 🟢 `[Lohman2023]` 🟢.

Denne seksjonen gjennomgår det vitenskapelige, regulatoriske og standardiserte fundamentet for LCA, LCC, datakvalitetsindikatorer (DQI) og usikkerhetsmodellering som utgjør state of the art for prosjektets testflate.

---

## 2.2 Vugge-til-port-dominans: 70 % A1–A3-regelen `[KD2024]` 🟡

Emboided carbon (innbygd karbon) utgjør en stadig økende andel av et byggs samlede livsløpsutslipp etter hvert som driftsfasens energibruk (modul B6) effektiviseres gjennom skjerpede energikrav `[KD2024]` 🟡 `[EBA_NO2023]` 🟡. Kartlegginger utført av Multiconsult og Direktoratet for byggkvalitet (DiBK, 2023/2024) i 4 representative referansebyggtyper (boligblokk, yrkesbygg/kontor, enebolig og rekkehus/skole) dokumenterer at materialrelaterte utslipp i livsløpsmodulene A1–A3 utgjør **63 % til 70 % (avrundet til 70 %)** av de totale materialrelaterte klimagassutslippene over byggets levetid `[KD2024]` 🟡.

### Modulenes definisjon i EN 15804+A2 `[EN15804]` 🟡:
- **Modul A1:** Råvareuttak og utvinning (cradle/vugge).
- **Modul A2:** Transport av råvarer til foredling og fabrikk.
- **Modul A3:** Produksjon og fremstilling av byggevarer ved fabrikkport (gate).

Sluttresultatet for modulsammenstillingen A1–A3 betegnes som *cradle-to-gate* (vugge-til-port). De resterende 30 % av materialutslippene fordeler seg på byggeplass/transport til byggeplass (A4–A5), utskifting og vedlikehold i driftsfasen (B2–B4), samt sluttfase og avhending (C1–C4) `[EN15804]` 🟡.

### Betydning for tilbudsfasen og VERIFIEDs beslutningsstøtte
70 %-dominansen i A1–A3 innebærer at de mest avgjørende utslippsreduksjonene oppnås ved valg av materialer, leverandører og produksjonsteknologier før byggeprosessen starter `[KD2024]` 🟡. I tilbudsfasen har entreprenøren og kunden fortsatt fleksibilitet til å vurdere alternative **løsningsvalg** (f.eks. lavkarbonbetong vs. konvensjonell betong, eller hulldekker vs. massivtre) `[EBA_NO2023]` 🟡. Når tilbudet er akseptert og prosjekteringen låst, begrenses handlingsrommet dramatisk. 

VERIFIED skal undersøke om en testflate som vektlegger A1–A3-data i tilbudsfasen gjør det mulig for ikke-spesialister å identifisere og velge lavutslippsalternativer med høy effekt tidlig i prosjektløpet `[BKA2]` 🟢 `[KD2024]` 🟡.

---

## 2.3 TEK17 § 9-2 og sikkerhetsfaktoren på 1,25 (+25 % påslag for generiske data)

Norsk byggteknisk forskrift (TEK17) § 9-2 stiller krav om at klimagassregnskap skal utarbeides for boligblokker og yrkesbygg basert på NS 3720 / EN 15978 `[EN15978-2026]` 🟢¹. Ved beregning av klimagassutslipp fra materialer skiller forskriften og DiBKs retningslinjer strengt mellom spesifikke og generiske miljødeklarasjoner:

1. **Spesifikk EPD (Environmental Product Declaration):** Tredjepartsverifisert miljødeklarasjon i henhold til NS-EN 15804+A2 `[EN15804]` 🟡 for et konkret produkt fra en spesifikk produsent. Brukes med faktiske, dokumenterte utslippstall uten straffepåslag.
2. **Generiske LCA-data:** Standardiserte gjennomsnittsdata fra databaser (f.eks. ecoinvent `[ecoinvent]` 🟡 eller Norsk Treteknisk Institutt) som benyttes dersom spesifikk EPD mangler.

### Regulatorisk sikkerhetsfaktor (+25 % utslippsstraff)
For å ta høyde for usikkerhet, spredning i produksjonsteknologi og manglende sporbarhet ved bruk av generiske kilder, pålegger det norske regelverket og NS 3720 at generiske klimagassfaktorer skal multipliseres med en **sikkerhetsfaktor på 1,25** (+25 % utslippspåslag) `[EN15804]` 🟡 `[KD2024]` 🟡. 

$$\text{Klimagassutslipp}_{\text{generisk}} = \text{Utslippsfaktor}_{\text{databasetall}} \times 1{,}25$$

### Operasjonalisering i VERIFIEDs testflate
I VERIFIEDs testflate benyttes denne 1,25-faktoren som et aktivt pedagogisk og incitamentskapende verktøy for beslutningsstøtte:
- Når en entreprenør vurderer et løsningsvalg uten spesifikk EPD, flagges datagrunnlaget som *«Generelt (påført +25 % TEK17-sikkerhetsfaktor)»*.
- Testflaten viser umiddelbart den beregnede gevinsten dersom leverandøren fremskaffer en verifisert, spesifikk EPD som fjerner straffepåslaget.
- Dette gir gjennomsiktig informasjon til både entreprenør og kunde om hvor usikkerheten ligger, uten å stoppe kalkylen eller skjule datagrunnlaget `[Edelen2018]` 🟢.

---

## 2.4 Datakvalitet og usikkerhetsmodellering: Weidema Pedigree-matrise

For å gi strukturert beslutningsstøtte basert på heterogene datakilder må usikkerheten i livsløpsinventaret (LCI) kvantifiseres systematisk. Det vitenskapelige standardrammeverket for dette er **Weidema Pedigree-matrisen**, opprinnelig utviklet av Weidema & Wesnæs (1996) `[Weidema1996]` 🟡 og videreutviklet med empiriske usikkerhetsfaktorer av Ciroth et al. (2016) `[Ciroth2016]` 🟡.

### De 5 datakvalitetsindikatorene (DQIs)
Pedigree-matrisen vurderer hvert datapunkt i et LCI-sett langs fem uavhengige kvalitetsdimensjoner, der hver indikator tildeles en skår fra **1 (best/høyest kvalitet)** til **5 (dårligst/lavest kvalitet)**:

| DQI-nr. | Datakvalitetsindikator (DQI) | Beskrivelse og vurderingskriterium | Skår 1 (Best) | Skår 5 (Dårligst) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Pålitelighet** (*Reliability*) | Datainnsamlingsmetodikk, målekvalitet og grad av uavhengig verifikasjon. | Verifiserte primærdata basert på kontinuerlige målinger. | Uverifiserte skjønnsmessige estimater eller ukjente kilder. |
| **2** | **Kompletthet** (*Completeness*) | Statistisk representativitet og andel steder/bedrifter inkludert i utvalget. | Data fra 100 % av relevante steder over tilstrekkelig tidsrom. | Data fra under 50 % av steder eller fra et lite utvalg bedrifter. |
| **3** | **Tidsmessig korrelasjon** (*Temporal correlation*) | Tidsavvik mellom dataenes innsamlingsår og prosjektets vurderingsår. | Data fra under 3 år før vurderingsåret. | Data fra mer enn 15 år før vurderingsåret. |
| **4** | **Geografisk korrelasjon** (*Geographical correlation*) | Geografisk samsvar mellom datakildens opprinnelse og norsk/lokalt byggested. | Data fra det spesifikke lokasjonsområdet (Norge). | Data fra ukjent region eller regioner med helt ulik energimiks. |
| **5** | **Teknologisk korrelasjon** (*Technological correlation*) | Samsvar mellom den modellerte prosessen/teknologien og den faktiske byggevaren. | Data fra nøye tilpasset, spesifikk produksjonsteknologi. | Data fra vesentlig ulik teknologisk prosess eller generisk proxy. |

### Stokastisk usikkerhetspropagering i ecoinvent `[ecoinvent]` 🟡
I den globale databasen ecoinvent oversettes de fem kvalitetsindikatorene ($i \in \{1, 2, 3, 4, 5\}$) til kvadratiske lognormale variansfaktorer ($\sigma_i^2$). Sammen med en grunnleggende usikkerhetsfaktor ($\sigma_{\text{basic}}^2$) beregnes den samlede geometriske standardavviksfaktoren ($\text{SD}_{95}$) for datapunktet `[ecoinvent]` 🟡 `[Ciroth2016]` 🟡:

$$\ln(\text{SD}_{95}) = \sqrt{\sigma_{\text{basic}}^2 + \sum_{i=1}^{5} \sigma_i^2}$$

Denne lognormale fordelingen danner grunnlaget for Monte Carlo-simuleringer, der tusenvis av iterasjoner genererer konfidensintervaller for utslippstallene. VERIFIED bygger på dette matematiske fundamentet for å synliggjøre konfidensintervaller i løsningssammenligningen `[Lohman2023]` 🟢.

---

## 2.5 Formålsavhengig datakvalitetsrammeverk: Edelen & Ingwersen (2018) `[Edelen2018]` 🟢

Mens Pedigree-matrisen leverer den matematiske konverteringen til varians, etablerer **Edelen & Ingwersen (2018)** `[Edelen2018]` 🟢 (*International Journal of Life Cycle Assessment*) det metodiske prinsippet for hvordan datakvalitet skal forvaltes og fremstilles i beslutningsprosesser.

### Hovedprinsipp: Formålsavhengig vurdering uten skjult totalscore
Edelen & Ingwersen dokumenterer at datakvalitet må vurderes eksplisitt i forhold til **formål, kontekst og den spesifikke beslutningsrollen** `[Edelen2018]` 🟢. Et helt avgjørende metodisk krav er at **datakvalitetsindikatorer ALDRI må aggregeres eller summeres til én enkelt komposittscore (skjult totalscore)**.

#### Begrunnelse mot skjult totalscore:
1. **Ikke-kompensatorisk natur:** Høy skår i én kvalitetsdimensjon kan aldri oppveie et kritisk avvik i en annen. Eksempelvis kan ikke et datasetts ferske tidsmessige stempel (DQI 3 = 1) kompensere for at dataene stammer fra et helt annet kontinent med ulik energimiks og teknologi (DQI 4 = 5). Å midle disse tallene gir en tilsynelatende «middels» score (3,0) som maskerer en alvorlig geografisk feilkilde.
2. **Beslutningsforvrengning:** En sammenhektet single-point score skjuler hvor usikkerheten ligger, og forhindrer brukeren i å ta stilling til om avviket er akseptabelt for det konkrete løsningsvalget.

### Konsekvenser for VERIFIEDs ontologi og testflate
I samsvar med Edelen & Ingwersen (2018) `[Edelen2018]` 🟢 og prosjektets ontologiske guardrails (`vibs-verified-ord-og-kildekart-v0.5.yml`) avviser VERIFIED alle former for skjulte totalscorer eller «svart boks»-vektingsmodeller. Testflaten skal i stedet eksponere datakvalitetsstatusen langs fire krystallklare kategorier:
- 🟢 **Verifisert:** Produktspesifikk EPD/FDV-dokumentasjon (DQI skår 1–2).
- 🟡 **Generelt:** Standard databasetall påført TEK17 1,25-sikkerhetsfaktor (DQI skår 3).
- 🟠 **Estimert:** Proxydata basert på lignende materialkategorier (DQI skår 4).
- 🔴 **Manglende data:** Eksplisitt synliggjort datagap som påkaller oppmerksomhet (DQI skår 5).

Dette sikrer at entreprenør og kunde får beslutningsstøtte med full transparens om datagrunnlagets pålitelighet `[Edelen2018]` 🟢 `[Lohman2023]` 🟢.

---

## 2.6 Standardiseringsrammeverket for bygg-LCA: EN 15978:2026, ISO 14040/14044 og EN 15804+A2

For at klimagassberegninger i VERIFIED skal ha juridisk og faglig autoritet overfor banker, byggherrer og myndigheter, må alle kilder og beregninger forankres i gjeldende europeiske og internasjonale standarder.

### EN 15978:2026 (CEN-CENELEC 17.04.2026) `[EN15978-2026]` 🟢¹
**EN 15978:2026** (*Bærekraftige byggverk - Vurdering av bygningers miljøprestasjon - Beregningsmetode*) ble offisielt publisert av CEN-CENELEC den **17. april 2026** og erstatter den eldre 2011-versjonen `[EN15978-2026]` 🟢¹. Standardoppdateringen representerer et gjennombrudd for sirkulærøkonomi og rehabiliteringsprosjekter:
- **Utvidet virkeområde:** Standarden omfatter nå eksplisitt både nybygg, eksisterende bygningsmasse, større ombygginger og **rehabiliteringsprosjekter**.
- **Harmonisert modulstruktur:** Etablerer strenge regler for aggregering av produkt-EPD-er over moduler A1–A3, A4–A5, B1–B7, C1–C4 og modul D (Gjenbruk, gjenvinning og energigjenvinning utenfor systemgrensen).
- **Systemgrenser for ombruk:** Standarden gir entydige beregningsregler for bevaring av eksisterende bygningsdeler og ombruk av brukte byggevarer, noe som er direkte relevant for VERIFIEDs vurdering av rehabiliteringsalternativer vs. nybygg.

### ISO 14040/14044:2006 `[ISO14040]` 🟡
ISO 14040 og ISO 14044 utgjør det generelle metodiske fundamentet for livsløpsvurderinger (LCA). Standarden definerer de fire obligatoriske fasene i en LCA-studie: (1) Mål- og omfangsdefinisjon, (2) Inventaranalyse (LCI), (3) Konsekvensanalyse (LCIA), og (4) Tolkning.

### NS-EN 15804:2012+A2:2019 `[EN15804]` 🟡
EN 15804+A2 er kjernestandarden for utarbeidelse av miljødeklarasjoner (EPD) for byggevarer i Europa. Fra oktober 2022 krever A2-revisjonen at alle nye EPD-er obligatorisk må rapportere utslipp og miljøpåvirkninger for modulene A1–A3, C1–C4 og D, noe som sikrer at avhendings- og gjenbrukspotensialet alltid er dokumentert `[EN15804]` 🟡.

### Praktikervariabilitet og databasedifferanser: Benke et al. (2025) `[Benke2025]` 🟢
Nylig publisert empirisk forskning av Benke et al. (2025) `[Benke2025]` 🟢 i *Scientific Data* (PMC12218139) understreker hvorfor standardisering og transparent datakvalitet er tvingende nødvendig. Ved analyse av 292 bygg-LCA-prosjekter avdekket forfatterne at industri-genererte LCA-resultater sjelden samles i sammenlignbare åpne databaser, og at kommersielle verktøy (som One Click LCA og Tally) oppviser vesentlige avvik seg imellom på grunn av ulikheter i bakgrunnsdata (LCI-databaser), standardforutsetninger for scenerier og modellørenes personlige skjønn `[Benke2025]` 🟢. Dette empiriske funnet bekrefter VERIFIEDs hypoteser om at verktøyuavhengig, gjennomsiktig dataintegrasjon er påkrevd.

---

## 2.7 Livssykluskostnader (LCC): NS-EN 16627 og ISO 15686-5 (og tilbaketrekkingen av NS 3454)

Bærekraftige **løsningsvalg** i tilbudsfasen kan ikke vurderes ut fra klimagassutslipp alene. Et alternativ med lave A1–A3-utslipp kan vise seg å ha kort levetid, høye vedlikeholdskostnader eller høy skaderisiko, noe som vil medføre betydelige økonomiske og miljømessige belastninger i driftsfasen. LCC-analyser er derfor en integrert del av beslutningsstøtten.

### ISO 15686-5:2017 `[ISO15686-5]` 🟡
ISO 15686-5 (*Buildings and constructed assets - Service life planning - Part 5: Life cycle costing*) etablerer internasjonale prinsipper for beregning av livssykluskostnader i bygg. Standarden definerer nåverdisammenstillinger (Net Present Value - NPV), kapitalutgifter (CapEx), driftsutgifter (OpEx), samt vedlikeholds- og utskiftingskostnader over en definert kalkylperiode.

### NS-EN 16627 `[NS-EN16627]` 🟢
NS-EN 16627 (*Bærekraftige byggverk - Vurdering av bygningers økonomiske prestasjon - Beregningsmetoder*) er den gjeldende norsk-europeiske standarden for LCC-beregninger på byggnivå. Standarden samkjører kostnadsmodulene direkte med LCA-modulstrukturen i EN 15978 (A1–A5, B1–B7, C1–C4).

### Kritisk regulatorisk avklaring: Tilbaketrekkingen av NS 3454 `[NS-EN16627]` 🟢
En svært viktig faglige avklaring for VERIFIED-prosjektet gjelder den nasjonale standarden NS 3454 (*Livssykluskostnader for byggverk*):
- **NS 3454 ble offisielt TRUKKET TILBAKE den 7. september 2023** av Standard Norge `[NS-EN16627]` 🟢.
- Standarden ble erstattet av **NS-EN 16627**, i kombinasjon med NS-EN ISO 15686-5.
- **Formelt krav til VERIFIED:** Prosjektet og dets dokumentasjon skal **aldri** referere til utgåtte NS 3454 som gjeldende beregningsgrunnlag, men konsekvent forankre LCC-strukturen i **NS-EN 16627** og **ISO 15686-5** `[NS-EN16627]` 🟢 `[ISO15686-5]` 🟡.

### Integrasjon av levetider og vedlikeholdsintervaller `[Byggforsk700.320]` 🟡
For å beregne realistiske LCC-tall i tilbudsfasen benytter VERIFIED standardiserte levetidsdata fra **Byggforskserien 700.320** (*Intervaller for vedlikehold og utskifting av bygningsdeler*) `[Byggforsk700.320]` 🟡. Anvisningen gir veiledende intervaller for utskifting og service. I henhold til det eksplisitte forbeholdet i anvisningen skal disse tabellintervallene *ikke benyttes som eksakte levetidssvar for en konkret eksisterende bygningsdel*, men som statistiske utgangsverdier i kalkylen `[Byggforsk700.320]` 🟡. Usikkerheten i levetidsangivelsene behandles i henhold til DQI-prinsippene i § 2.5 `[Edelen2018]` 🟢.

---

## 2.8 Oppsummering og metodiske føringer for VERIFIEDs testflate

Tabellen nedenfor oppsummerer det metodiske fundamentet, kildenes portstatus og de operative føringene for utviklingen av VERIFIEDs testflate:

| Metodisk element | Primærkilde / Standard | Port-status | Operativt krav til VERIFIEDs testflate |
| :--- | :--- | :---: | :--- |
| **A1–A3 Dominans (70 %)** | Multiconsult / DiBK (2023/2024) `[KD2024]` | 🟡 | Prioritere A1–A3 EPD-data i tilbudsfasen der reduksjonspotensialet er størst før prosjekteringslås. |
| **TEK17 1,25-sikkerhetsfaktor** | TEK17 § 9-2 / DiBK / NS 3720 `[EN15804]` | 🟡 | Synliggjøre +25 % utslippsstraff på generiske data; vise gevinst ved innhenting av spesifikk EPD. |
| **Stokastisk usikkerhet (5 DQIs)** | Weidema & Wesnæs (1996) `[Weidema1996]` / ecoinvent `[ecoinvent]` | 🟡 | Konvertere DQI-skår (1–5) til lognormale variansfaktorer for Monte Carlo-baserte konfidensintervaller. |
| **Formålsavhengig datakvalitet** | Edelen & Ingwersen (2018) `[Edelen2018]` | 🟢 | **Forbud mot skjult totalscore/svart boks.** Vise flerdimensjonal datastatus (verifisert, generell, estimert, mangler). |
| **Bygg-LCA & Rehabilitering** | EN 15978:2026 (publisert 17.04.2026) `[EN15978-2026]` | 🟢¹ | Følge harmonisert modulstruktur (A1–D); anvende oppdaterte beregningsregler for rehabilitering vs. nybygg. |
| **LCC-beregningsstandard** | NS-EN 16627 `[NS-EN16627]` / ISO 15686-5 `[ISO15686-5]` | 🟢 / 🟡 | **Forankre LCC i NS-EN 16627.** Eksplisitt unngå referanse til tilbaketrukket NS 3454 (trukket 07.09.2023). |
| **Levetidsintervaller** | Byggforskserien 700.320 `[Byggforsk700.320]` | 🟡 | Benytte veiledende utskiftingsintervaller for LCC med synliggjort usikkerhetsforbehold. |
| **Praktikervariabilitet** | Benke et al. (2025) `[Benke2025]` | 🟢 | Dokumentere behovet for verktøyuavhengig, gjennomsiktig dataintegrasjon uten leverandørskjønn. |

---

# Seksjon 3: Flerkriterieanalyse og usikkerhet (MCDA)

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

VERIFIEDs beslutningsmodell bygger på prinsippet om at manglende eller usikre data aldri skal skjules bak et fikst gjennomsnittstall, men eksplisitt eksponeres som utvidet usikkerhet i beslutningsgrunnlaget 🟢 (`[Edelen2018]`, `[Lohman2023]`).

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

Høy datakvalitet på én dimensjon (f.eks. fersk tidsmessig data) kan ikke kompensere for alvorlige mangler på en annen dimensjon (f.eks. feil geografisk opprinnelse). En aggregert samlescore ville fungert som en ugjennomsiktig modell som tilslører risiko for brukeren. I stedet skal datakvalitet og usikkerhet vises åpent for brukeren 🟢.

### 3.2.3 Synlig usikkerhetsrepresentasjon i moderne rammeverk (Lohman & EC3)

VERIFIED henter inspirasjon fra to ledende internasjonale rammeverk for synlig usikkerhet:
- **DMsan-rammeverket (Lohman et al. 2023)** (`[Lohman2023]`, *ACS Environ. Au*, PMC10197171 🟢): Demonstrerer hvordan MCDA for miljøvalg kan gjennomføres ved å eksponere usikkerhetsintervaller og følsomhet for kriteriavekter, i stedet for å levere stive punktestimater.
- **EC3 / Building Transparency (`[EC3]` 🟢):** Viser et forbilledlig praksiseksempel ved å beregne og vise konfidensintervaller for innbygd karbon («conservative vs. achievable estimate»). Dersom en byggevare mangler spesifikk EPD og må bruke generiske data, straffes alternativet med et utvidet usikkerhetsspenn i brukergrensesnittet.

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

I stedet for å peke ut én stiv «vinner», benytter VERIFIEDs testflate **mulighetsrom-visualisering (*opportunity space visualization*)** 🟢 (`[Lohman2023]`, `[EC3]`). 

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
2. **Sensitivitetsvarsling i testflaten:** I stedet for å skjule rangfølsomhet, skal VERIFIEDs testflate teste grensesnitt som varsler brukeren dersom relaterte alternativer ligger nær hverandre i utfall, eller dersom rangeringen er såfremt følsom for vektendringer at ranginversjon kan inntreffe 🟢.
3. **Stabilitetsvurdering:** Prosjektet skal undersøke om kombinasjonen av AHP-basert kriteriavekting og MIVES-baserte verdefunksjoner (som benytter absolutt heller enn relativ normalisering) reduserer risikoen for uønsket ranginversjon i tilbudsfasen 🟡 (`[Mecca2023]`).

---

## 3.4 Syntese og VERIFIEDs testflate for tilbudsfasen

Syntesen av flerkriterieanalyse og usikkerhetsrepresentasjon definerer VERIFIEDs nyhetsverdi langs **fire sentrale akser** i prosjektets forskningsgapsmatrise 🟢:

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

---

# Seksjon 4: Finans- og reguleringskontekst

## 4.1 Innledning og overordnet finansielt rammeverk

Eiendoms- og byggesektoren utgjør en dominerende del av finanssektorens utlånsporteføljer. I Norge utgjør eiendom og boliglån over 60 % og opp mot to tredjedeler av bankenes samlede utlån (`[FinanceNorway2018]` 🟡; `[Multiconsult2023]` 🟡). Finansielle institusjoner er dermed eksponert for både fysisk klimarisiko (som akutte fuktskader og ekstreme værhendelser) og overgangsrisiko (som regulatoriske krav til energimerking, karbonavgifter og tekniske bygningsstandarder).

Offisiell skadestatistikk fra Finans Norge 2023 (`[FinansNorge2024VASK]` 🟢) dokumenterer et betydelig omfang av fysiske bygningsskader i Norge: det registreres i gjennomsnitt **10 vannskader i timen** (tilsvarende ca. 87 600 skader årlig), med et samlet erstatningsutbetalingsvolum på **5,1 milliarder kroner i 2023**. Dette understreker at bygningsteknisk kvalitet, fuktrobusthet og vedlikehold har direkte og umiddelbare økonomiske konsekvenser for forsikringsselskaper og eiendomseiere.

Samtidig stiller regulatoriske organer og investorer stadig strengere krav til ESG-rapportering og klimarisikostyring. Finansielle aktører etterspør i økende grad strukturerte, etterprøvbare bygningsdata for å klassifisere grønne utlånsporteføljer i henhold til EU-taksonomien (`[EUTax]` 🟡) og EUs direktiv om bærekraftsrapportering (CSRD / Omnibus I `[OmnibusI]` 🟡).

I denne konteksten skal prosjektet VERIFIED utvikle og teste en **testflate** for **beslutningsstøtte** som setter **entreprenør og kunde** (herunder **ikke-spesialister** i SMB-segmentet) i stand til å sammenligne alternative **løsningsvalg** allerede i **tilbudsfasen**. Beslutningsmodellen skal framstille forutsigbare avveininger mellom klimagassutslipp (LCA per EN 15978:2026 `[EN15978-2026]` 🟢), livsløpskostnader (LCC per NS-EN 16627 `[NS-EN16627]` 🟢 og ISO 15686-5 `[ISO15686-5]` 🟡), teknisk levetid og fuktrobusthet — med **synlig datagrunnlag og usikkerhet** fremfor skjulte totalskårer.

---

## 4.2 Empirisk litteratur om energi- og klimaeffektivitet vs. misligholdsrisiko (PD)

Det finnes et etablert og empirisk dokumentert forskningsgrunnlag som viser en sammenheng mellom bygningers energieffektivitet og finansiell kredittrisiko, målt ved misligholdssannsynlighet (Probability of Default, PD). Tre sentrale studier danner det empiriske fundamentet for denne sammenhengen:

### 1. Kaza et al. (2014) — Boliglånsrisiko i USA 🟢
- **Kilde:** Kaza, N., Quercia, R.G. & Tian, C.Y. (2014). *Home Energy Efficiency and Mortgage Risks.* Cityscape, 16(1), 279–298 (`[Kaza2014]` 🟢).
- **Datagrunnlag og funn:** Analyserte ca. 71 000 residensielle boliglån i USA. Studien dokumenterer at eiere av ENERGY STAR-sertifiserte boliger har i gjennomsnitt **~32 % lavere misligholdssannsynlighet (PD)** enn eiere av uverifiserte boliger, kontrollert for inntekt, belåningsgrad (LTV) og kredittskår.
- **Mekanisme:** Lavere og mer forutsigbare energikostnader frigjør likviditet i husholdningsbudsjettet, noe som direkte reduserer faren for betalingsmislighold under økonomiske sjokk.
- **Status og omfang:** 🟢 **Bærende primærkilde**. Gjelder eksplisitt residensielle boliglån.

### 2. Billio et al. (2022) — Boliglånsrisiko i Nederland 🟢
- **Kilde:** Billio, M., Costola, M., Pelizzon, L. & Riedel, M. (2022). *Buildings' Energy Efficiency and the Probability of Mortgage Default: The Dutch Case.* The Journal of Real Estate Finance and Economics, 65(3), 419–450. DOI: 10.1007/s11146-021-09838-0 (`[Billio2022]` 🟢).
- **Datagrunnlag og funn:** Empirisk undersøkelse av nederlandske residensielle boliglån. Studien dokumenterer en statistisk signifikant korrelasjon der bedre energimerkeklasse (EPC — Energy Performance Certificate, fra A til G) er forbundet med lavere misligholdssannsynlighet (PD).
- **Mekanisme:** Høyere energieffektivitet gir lavere løpende driftsutgifter og bedre verdibevaring i boligmarkedet, noe som styrker pantesikkerheten for banken og låntakers betalingsevne.
- **Status og omfang:** 🟢 **Bærende primærkilde**. Dokumenterer empirisk energi↔PD-sammenheng innenfor et europeisk residensielt boliglånsmarked.

### 3. An & Pivo (2020) — Kommersiell eiendom og CMBS 🟡
- **Kilde:** An, X. & Pivo, G. (2020). *Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms.* Real Estate Economics, 48(1), 7–42. DOI: 10.1111/1540-6229.12228 (`[An2020]` 🟡).
- **Datagrunnlag og funn:** Empirisk studie av kommersielle eiendomslån i det amerikanske CMBS-markedet (Commercial Mortgage-Backed Securities). Viser at LEED- og ENERGY STAR-sertifiserte næringsbygg har **34 % lavere misligholdsrisiko (PD)** sammenlignet med umerket kommersiell eiendom.
- **Viktig avgrensning og metodisk forbehold:** Studien gjelder **utelukkende kommersiell eiendom (CMBS)**, og må *aldri* overføres uforbeholdent til residensielle boliglån. Primærteksten har publiseringsforbehold / betalingsmur (Wiley 402) og har status 🟡 **Under avklaring** inntil SINTEF har fullført primærverifisering av fullteksten.

---

## 4.3 Regulatorisk påtrykk og bankenes risikostyring

Finanssektorens etterspørsel etter bygningsnær miljø- og risikodata drives sterkt av europeiske og internasjonale finanstilsyn.

### 1. European Banking Authority — EBA EU 2023 🟢
- **Kilde:** European Banking Authority (15. desember 2023). *Report on Green Loans and Mortgages* (EBA/Op/2023/13) (`[EBA_EU2023]` 🟢).
- **Innhold og betydning:** EBA foreslår et frivillig europeisk merke for grønne lån og boliglån (EU Green Loan Label), samt en harmonisering av rapporteringskrav under boligkredittdirektivet (Mortgage Credit Directive, MCD). Rapporten konkluderer med at **manglende harmoniserte data, uverifisert dokumentasjon og fragmentert bygningsinformasjon** utgjør de største bindende flaskehalsene for at banker skal kunne tilby grønn finansiering til SMB-segmentet og bygningsrenovering.
- **Status:** 🟢 **Bærende primærkilde** for finansregulatoriske krav i banksektoren.

### 2. Bank of England — PS25/25 🟡
- **Kilde:** Bank of England Prudential Regulation Authority (desember 2025). *Enhancing banks' and insurers' approaches to managing climate-related risks* (PS25/25) (`[BoE_PS25-25]` 🟡).
- **Innhold og frist:** Erstatter de tidligere klimaforventningene fra SS3/19 (2019). PS25/25 stiller bindende krav om at banker og forsikringsselskaper skal integrere både fysisk klimarisiko og overgangsrisiko i sine kjernerammeverk for risikostyring, kredittvurdering og styrebehandling. Frist for fullstendig gjennomføring er **juni 2026**.
- **Status:** 🟡 **Under avklaring** (substans bekreftet via uavhengige fagkilder, primærdokumentasjonen krever formell verifisering).

### 3. Bank of England — DP1/25 🟡
- **Kilde:** Bank of England Prudential Regulation Authority (juli 2025). *Residential mortgages: LGD and PD estimation* (DP1/25) (`[BoE_DP1-25]` 🟡).
- **Innhold og presisering:** Diskuterer utfordringer og kapasitetsbegrensninger mellomstore banker møter når de skal utvikle egne IRB-modeller (Internal Ratings-Based) for å beregne misligholdssannsynlighet (PD) og tap ved mislighold (Loss Given Default, LGD) for residensielle boliglån.
- **Viktig ontologisk og faglige presisering:** DP1/25 omhandler **ikke klimarisiko direkte**, men representerer den underliggende kredittrisikoinfrastrukturen (IRB PD/LGD-modellene) som framtidig bygnings- og klimarisikodata må mates inn i.

---

## 4.4 Ontologisk og enhetsmessig distinksjon: EBA EU vs. EBA Norge

En av de viktigste kildekritiske og ontologiske kontrollreglene i VERIFIED-prosjektet er å opprettholde et **strengt og ufravikelig skille** mellom to helt ulike enheter som deler akronymet «EBA».

```
                  ┌─────────────────────────────────────────┐
                  │          AKRONYM: «EBA»                 │
                  └────────────────────┬────────────────────┘
                                       │
           ┌───────────────────────────┴───────────────────────────┐
           ▼                                                       ▼
┌──────────────────────────────┐                       ┌──────────────────────────────┐
│       [EBA_EU2023] 🟢        │                       │       [EBA_NO2023] 🟡        │
├──────────────────────────────┤                       ├──────────────────────────────┤
│ European Banking Authority   │                       │ Entreprenørforeningen –      │
│ (EU-organ for banktilsyn)    │                       │ Bygg og Anlegg (Norge)       │
├──────────────────────────────┤                       ├──────────────────────────────┤
│ Domene: Finansregulering,    │                       │ Domene: Byggebransje,        │
│ grønne boliglån, ESG, MCD    │                       │ materialvalg, klimagass i    │
│ (Report EBA/Op/2023/13)      │                       │ boligblokker (veileder 2023) │
└──────────────────────────────┘                       └──────────────────────────────┘
```

### Obligatoriske skillereregler:
1. **Fullt navn ved første gangs nevnelse:**
   - EU-kontekst: *«European Banking Authority (EBA EU) …»* (`[EBA_EU2023]` 🟢)
   - Norsk byggkontekst: *«Entreprenørforeningen – Bygg og Anlegg (EBA Norge) …»* (`[EBA_NO2023]` 🟡, utgitt i samarbeid med Grønn Byggallianse og Norsk Eiendom).
2. **Aldri slå sammen nøklene:** Det er strengt forbudt å bruke et generisk `[EBA]`. Finansielle vurderinger siterer utelukkende `[EBA_EU2023]` 🟢. Byggetekniske materialvurderinger (som viser at tidlige materialvalg kan gi inntil 20 % reduksjon i klimagassutslipp i boligblokker uten merkostnad) siterer utelukkende `[EBA_NO2023]` 🟡.

---

## 4.5 Det avgrensede FoU-gapet: Holdbarhet og fuktrobusthet til kredittrisiko

Selv om eksisterende forskning og regulering er moden innenfor visse delområder, avslører State of the Art-kartleggingen et tydelig og udekket forskningsgap.

### Kjernen i forskningshullet:
1. **Energisentrert etablert kunnskap:** Den empiriske litteraturen (Kaza et al. 2014 `[Kaza2014]` 🟢; Billio et al. 2022 `[Billio2022]` 🟢; An & Pivo 2020 `[An2020]` 🟡) dokumenterer at energieffektivitet (kWh/m²/år og energimerkeklasser) korrelerer med lavere misligholdsrisiko (PD).
2. **Det udekkede gapet (FoU-høyden):** Det finnes **null publisert empirisk litteratur** som kobler bygningsteknisk kvalitet, materialenes holdbarhet, levetid, fuktrobusthet eller vedlikeholdsbyrde direkte til finansiell kredittrisiko (PD og LGD).
3. **Regulatorisk svakhet i dagens grønne finans:** Gjeldende finansielle rammeverk (EU-taksonomien `[EUTax]` 🟡, EEMI `[EEMI]` 🟡, EBA grønne lån `[EBA_EU2023]` 🟢) er i stor grad snevert energisentrerte. De fanger ikke opp om et lavenergibygg er oppført med fuktutsatte materialer, har kort teknisk levetid eller pådrar seg store vedlikeholdsetterslep som over tid svekker panteobjektets verdi.

### VERIFIEDs forskningshypotese (FoU-spørsmål F1 og F5):
> **Prosjektet skal undersøke om** strukturerte bygningsdata om levetid, fuktrobusthet og vedlikeholdsintervaller (NS-EN 16627 `[NS-EN16627]` 🟢, Byggforskserien 700.320 `[Byggforsk700.320]` 🟡) kan oversettes til relevante risikoparametere for finans- og forsikringssektoren.

Dette utgjør prosjektets avgrensede nyhetsverdi på det finansielle området: å etablere en bro fra byggeteknisk kvalitet og DNSH-kriterier (Do No Significant Harm) til bankenes risikomodeller (IRB PD/LGD), tilrettelagt for enkel bruk av ikke-spesialister i tilbudsfasen.

---

## 4.6 Parkert status og kildeavklaringer

For å opprettholde streng kildekritikk og unngå sirkelargumentasjon, er enkelte kilder satt i parkert status (⏸) i samsvar med prosjektleders beslutning (Lars Gunnar, 2026-06-28):

1. **`[Wiik2025]` — SINTEF Notat nr. 57** (*Kostnadseffekten av klimatiltak i byggenæringen*, 2025):  
   - **Status:** ⏸ **Parkert**.
   - **Begrunnelse:** Dokumentet er et internt, uindeksert notat utarbeidet for konsortiet. Å sitere et internt notat for å bevise kostnadsnøytralitet utgjør sirkelargumentasjon.
   - **Erstatningskilder:** Påstander om at tidlige materialvalg kan gi betydelige utslippsreduksjoner uten merkostnad skal i stedet støttes av uavhengige, publiserte kilder som `[EBA_NO2023]` 🟡 (20 % reduksjon i boligblokker) og `[KD2024]` 🟡 (handlingsrom i tidligfase).

2. **`[SA2018]` — Samfunnsøkonomisk analyse Rapport 4-2018** (*Konflikter i bygg- og anleggsnæringen*):  
   - **Status:** ⏸ **Parkert** / 🟡 **Under avklaring**.
   - **Begrunnelse:** Rapporten er ikke bekreftet fysisk åpnet i offentlige registre i denne runden.
   - **Operativ regel:** Påstanden om 2,2 milliarder kroner i årlige konfliktkostnader kan ikke brukes som uforbeholdent primærbelegg før kildefilen er fysisk lokalisert og åpnet.

3. **`[NFR_IPN2026]` — Norsk forskningsråd IPN Utlysning 2026 (§10.1)** 🟢:  
   - **Status:** 🟢 **Bærende offisiell kilde**.
   - **Rammer:** Støttebeløp er avgrenset til **1–16 MNOK**, med en maksimal støttesats på **50 %** av prosjektets godkjente kostnader for bedriftspartnere.

---

## 4.7 Oppsummerende kildematrise for finans og regulering

Tabellen nedenfor oppsummerer de sentrale kildene som inngår i Seksjon 4, deres domene, provenans og autoritative portstatus i henhold til `ipn-kildebibliotek.md`.

| Kildenøkkel | Tittel / Referanse | Domene | Provenans | Port-status | Primær rolle / Omfang i Seksjon 4 |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `[Kaza2014]` | Kaza et al. (2014) *Cityscape* 16(1) | Akademia | Primær | 🟢 | Emne: Residensielle boliglån i USA (~32 % lavere PD for ENERGY STAR). |
| `[Billio2022]` | Billio et al. (2022) *JREFE* 65(3) | Akademia | Primær | 🟢 | Emne: Residensielle boliglån i Nederland (EPC energimerke korrelerer med lavere PD). |
| `[An2020]` | An & Pivo (2020) *Real Estate Econ.* 48(1) | Akademia | Primær | 🟡 | Emne: Kommersiell eiendom (CMBS, 34 % lavere PD for LEED/ENERGY STAR). Betalingsmur. |
| `[EBA_EU2023]` | European Banking Authority (Dec 2023) | Finanstilsyn | Primær | 🟢 | Emne: EBA Green Loan Report (EBA/Op/2023/13); manglende data er bindende skranke. |
| `[BoE_PS25-25]`| Bank of England PS25/25 (Dec 2025) | Finanstilsyn | Sekundær | 🟡 | Emne: Klimarisikostyring i banker/forsikring; frist juni 2026. |
| `[BoE_DP1-25]` | Bank of England DP1/25 (July 2025) | Finanstilsyn | Sekundær | 🟡 | Emne: IRB PD/LGD-modellering for boliglån (ikke-klima infrastruktur). |
| `[FinansNorge2024VASK]`| Finans Norge Skadestatistikk (2023) | Forsikring | Offisiell | 🟢 | Emne: 10 vannskader/time (~87 600/år), 5,1 mrd. kr utbetalt i 2023. |
| `[EBA_NO2023]` | EBA Norge / Grønn Byggallianse (2023) | Byggebransje | Sekundær | 🟡 | Emne: Veileder for boligblokker (20 % CO₂-kutt uten merkostnad). Må skille fra EBA EU. |
| `[Wiik2025]` | SINTEF Notat nr. 57 (2025) | Konsortium | Internt | ⏸ | Emne: Materialkostnadsnøytralitet. Parkert (sirkelargumentasjon). |
| `[SA2018]` | Samfunnsøkonomisk analyse (4-2018) | Konsulenter | Primær | ⏸ | Emne: Konfliktkostnader 2,2 mrd. kr/år. Parkert (ubekreftet fil). |
| `[NFR_IPN2026]` | NFR IPN Utlysning 2026 (§10.1) | Offisiell | Offisiell | 🟢 | Emne: Ramme 1–16 MNOK, maks 50 % støtte. |

---

# Seksjon 5: Norsk SMB-kontekst og tilbudsbeslutninger

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

1. **Akse (a) Dataintegrasjon 🟢:** Integrasjon av heterogene datakilder i én modell: EPD/LCA (A1–A3, C, D) + LCC (NS-EN 16627 `[NS-EN16627]` 🟡) + teknisk levetid (Byggforskserien 700.320 `[Byggforsk700.320]` 🟡) + fuktrobusthet/skaderisiko + ombruksbarhet.
2. **Akse (b) Fase (Tilbudsfasen) 🟢:** Opererer eksplisitt i tilbudsfasen (*tilbudsfasen*) før kontrakt signeres og før løsningsvalg låses i detaljprosjektering. Tidligfasebeslutninger i A1–A3 står for opptil **70 % av bygningsmaterialenes klimagassutslipp** (`[KD2024]` 🟡), der handlingsrommet for utslipps- og kostnadsreduksjon er størst uten merkostnad (`[EBA_NO2023]` 🟡).
3. **Akse (c) Brukergruppe (Ikke-spesialister) 🟢:** Utformet for SMB-entreprenører og kunden (*ikke-spesialister*). Krevende LCA- og LCC-analyser forenkles til et forståelig visualisert sammenligningsgrunnlag uten at kunden må ansette egne miljørådgivere.
4. **Akse (d) Forklarbarhet og usikkerhet 🟢:** Ingen skjult totalscore eller «svart boks». Datakvalitet og usikkerhet eksponeres åpent gjennom DQI-kategorier (verifisert EPD, generisk data med TEK17 1,25-påslag `[Edelen2018]` 🟢, estimert proxy-data, manglende data). Usikkerhet formidles som konfidensintervaller og handlingsrom («opportunity spaces» `[Lohman2023]` 🟢).
5. **Akse (e) Beslutningseffekt og attribusjon 🟢:** Systemet inneholder innebygd loggingsarkitektur for å måle om presentasjonen av sammenlignbare data faktisk påvirket, endret eller bekreftet entreprenørens og kundens endelige løsningsvalg i tilbudet.
6. **Akse (f) Bredde i bærekraft (DNSH-prinsippet) 🟢:** Rommer Do No Significant Harm (DNSH)-kriterier som fuktrobusthet (forebygging av vannskade; Finans Norge 2023-statistikk viser 10 vannskader/time og 5,1 mrd. kr utbetalt `[FinansNorge2024VASK]` 🟢), teknisk levetid og lave livsløpskostnader, i stedet for utelukkende å prioritere lavest initial CO₂.

---

## 5.5 Ontologiske guardrails og kildekritisk forankring 🟢

For å sikre vitenskapelig konsistens og samsvar med autoritativ kildedom i prosjektet, gjelder følgende ontologiske føringer strengt for Seksjon 5:

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

---

# Seksjon 6: Syntese og VERIFIEDs avgrensede FoU-gap

## 6.1 Helhetlig forskningssyntese og teoretisk forankring
State of the Art-kartleggingen i denne rapporten har undersøkt det vitenskapelige og empiriske fundamentet for verifisert beslutningsstøtte i byggesektoren på tvers av fire sentrale søyler:

1. **Det metodiske fundamentet (Seksjon 2):** Dokumenterer at opptil **70 % av de materialrelaterte klimagassutslippene** over et byggs livsløp skjer i vugge-til-port-modulene A1–A3 (`[KD2024]` 🟡). Videre etablerer analysen at TEK17 § 9-2 sin **1,25-sikkerhetsfaktor (+25 % utslippsstraff på generiske data)** `[KD2024]` 🟡 `[EN15804]` 🟡 og **Weidema Pedigree-matrisen** (5 DQIs) `[Weidema1996]` 🟡 `[Ciroth2016]` 🟡 utgjør det matematiske og regulatoriske utgangspunktet for å modellere usikkerhet i byggevaredata. I henhold til **Edelen & Ingwersen (2018)** `[Edelen2018]` 🟢 må datakvalitet vurderes ut fra formål og aldri komprimeres til en skjult totalscore. LCC-beregninger må forankres i gjeldende **NS-EN 16627** `[NS-EN16627]` 🟢 og **ISO 15686-5** `[ISO15686-5]` 🟡, med eksplisitt forbehold mot den tilbaketrukne standarden NS 3454.

2. **Flerkriterieanalyse og usikkerhetsrepresentasjon (Seksjon 3):** Viser via **Mecca (2023)** `[Mecca2023]` 🟡 at MCDA-metodikk (AHP 46 %, TOPSIS 20 %, MIVES 11 %, COPRAS 9 %) er akademisk moden, men at eksisterende anvendelser lider av faseforskyvning (fokus på prosjektering eller offentlig tildeling snarere enn SMB-tilbudsfasen), spesialistavhengighet og ugjennomsiktig aggregering. VERIFIED etablerer et **metodisk forbehold mot ranginversjon (Rank Reversal)** i TOPSIS/COPRAS som en FoU-hypotese som skal undersøkes, ikke som en ferdig bevist påstand. Usikkerhet eksponeres åpent gjennom fire datatilstander (verifisert 🟢, generisk 🟢/🟡, estimert 🟡, manglende data 🔴/🟡) og mulighetsrom-visualisering (*opportunity spaces*) `[Lohman2023]` 🟢 `[EC3]` 🟢.

3. **Finans- og reguleringskontekst (Seksjon 4):** Kartlegger det etablerte empiriske fundamentet der energieffektivitet korrelerer med lavere misligholdsrisiko (PD) på boliglån (~32 % lavere PD per Kaza et al. 2014 `[Kaza2014]` 🟢; Billio et al. 2022 `[Billio2022]` 🟢) og næringseiendom (34 % lavere PD per An & Pivo 2020 `[An2020]` 🟡 for CMBS). Videre dokumenteres det regulatoriske drivet fra European Banking Authority (**`[EBA_EU2023]` 🟢**, grønne lån) og Bank of England (PS25/25 `[BoE_PS25-25]` 🟡; DP1/25 `[BoE_DP1-25]` 🟡). Analysen avdekker et krystallklart FoU-hull: koblingen mellom fuktrobusthet, teknisk levetid og levetidskostnader mot bankenes kredittrisikomodeller (IRB PD/LGD) er helt uutforsket i litteraturen.

4. **Norsk SMB-kontekst og eksisterende verktøy (Seksjon 5):** Belyser Nordisk Ministerråds (**`[Nordic2023]` 🟢**) lempelighetsbegrunnelse for mindre aktører, og viser hvordan forskningsprosjektet **BKA2** (11,7 MNOK, ledet av Trondheim kommune v/ SINTEF og Vegard Knotten `[BKA2]` 🟢) danner et komplementært grensesnitt på bestillersiden, mens VERIFIED leverer beslutningsmodellen på tilbydersiden. Kartleggingen av SmartKalk Miljø 🟡, Reduzer 🟡, Concular 🟡, ORIS 🟡, One Click LCA 🟡 og EC3 🟢 dokumenterer at eksisterende verktøy tilbyr verdifulle enkriterie- eller prosjekteringsløsninger, men at ingen kombinerer alle 6 nødvendige akser.

---

## 6.2 Sammenstilt 6-aksers matrise (Konkurrent- og verktøyanalyse)

Tabellen nedenfor oppsummerer den systematiske kartleggingen av eksisterende verktøy i det norske og internasjonale markedet mot de 6 definerte aksene i VERIFIEDs forskningsrammeverk:

| Verktøy / Kilde | (a) Dataintegrasjon (LCA+LCC+Levetid+Fukt) | (b) Tilbudsfase (Før kontrakt & låsing) | (c) SMB-bruker (Ikke-spesialist) | (d) Synlig usikkerhet (DQI / Ingen svart boks) | (e) Beslutningseffekt (Måling & Loggingsarkitektur) | (f) DNSH-bredde (Fuktrobusthet, skade, LCC) | Kildestatus & Belegg |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **SmartKalk Miljø** (Holte, NO) | Delvis (LCA+Pris) | **JA** | **JA** | NEI (Kun punkt) | NEI | NEI (Kun CO₂) | 🟡 `[NOBB]` |
| **Reduzer** (NTNU spin-off, NO) | NEI (Kun LCA) | **JA** | **JA** | NEI | NEI | NEI (Kun CO₂) | 🟡 |
| **Concular** (Tyskland) | Delvis (Ombruk+Garanti) | NEI | Delvis | NEI | NEI | Delvis (Ombruk) | 🟡 |
| **ORIS** (Frankrike / Intl) | Delvis (Transport-LCA) | Delvis | NEI (Krevende input) | NEI | NEI | NEI (Kun transport) | 🟡 |
| **One Click LCA** (Finland) | **JA** (LCA + LCC) | Delvis | NEI (Ingeniør-fokus) | NEI (Ingen synlig DQI) | NEI | Delvis (LCC etter 16627) | 🟡 |
| **EC3** (Building Transparency, US) | NEI (Kun LCA) | Delvis | Delvis | **JA** (Konfidensintervall) | NEI | NEI (Kun karbon) | 🟢 `[EC3]` |
| **VERIFIED (Mål for IPN-prosjektet)** | **JA** (LCA, LCC, Levetid, Fukt) | **JA** (Tilbudsfasen) | **JA** (Ikke-spesialist) | **JA** (Synlig DQI, 1,25-påslag, ingen svart boks) | **JA** (Attribusjon & loggingsflate) | **JA** (DNSH, fuktrisiko, Finans Norge-data) | 🟢 (IPN 2026 Mål) |

---

## 6.3 Det avgrensede FoU-gapet og forskningshøyden (Formelt gap-utsagn)

Basert på den 6-aksiale funksjonsmatrisen og den kildekritiske litteraturgjennomgangen formuleres prosjektets autoritative og avgrensede FoU-gap:

> **«Innenfor det undersøkte utvalget av verktøy finnes enkeltkomponenter, men ingen enkeltverktøy kombinerer alle 6 akser i en integrert, forklarbar testflate for beslutningsstøtte for norske SMB-er i tilbudsfasen.»** 🟢

### Utdyping av de 6 aksene og tilhørende FoU-hypoteser (F1–F5):

1. **Akse (a) Dataintegrasjon & Finansiell Kobling (FoU-hypotese F1):**
   *Beskrivelse:* Sømløs kobling av heterogene datakilder: EPD/LCA (modul A1–A3, C, D) + LCC (NS-EN 16627 `[NS-EN16627]` 🟢) + teknisk levetid (Byggforsk 700.320 `[Byggforsk700.320]` 🟡) + fuktrobusthet/skaderisiko (Finans Norge 2023 `[FinansNorge2024VASK]` 🟢).
   *FoU-hypotese F1:* Prosjektet skal undersøke om byggetekniske levetids- og risikodata kan oversettes til relevante parametere for bankenes kredittrisikomodeller (IRB PD/LGD), og dermed tette hullet mellom bygningskvalitet og grønn finansiering (`[EBA_EU2023]` 🟢; `[BoE_PS25-25]` 🟡).

2. **Akse (b) Fase — Tilbudsfasen (FoU-hypotese F4):**
   *Beskrivelse:* Beslutningsstøtten opererer eksplisitt i tilbudsfasen (*tender phase*), der 70 % av de materialrelaterte klimagassutslippene låses `[KD2024]` 🟡, og der handlingsrommet for utslippskutt uten merkostnad er størst `[EBA_NO2023]` 🟡.
   *FoU-hypotese F4:* Prosjektet skal evaluere hvordan TEK17 § 9-2 sin **1,25-sikkerhetsfaktor (+25 % utslippsstraff på generiske data)** påvirker entreprenørens motivasjon til å kreve produktspesifikke EPD-er fra underleverandører i tilbudsprosessen.

3. **Akse (c) Brukergruppe — Ikke-spesialister i SMB-segmentet:**
   *Beskrivelse:* Tilpasset for SMB-entreprenører og boligkjøpere som mangler egne miljørådgivere `[Nordic2023]` 🟢. Grensesnittet oversetter avansert LCA/LCC til et intuitivt sammenligningsgrunnlag uten å kreve spesialistkompetanse.

4. **Akse (d) Synlig usikkerhet & Metodisk forbehold (FoU-hypoteser F2 og F3):**
   *Beskrivelse:* Ufravikelig forbud mot "svart boks"-vektingsmodeller og skjulte totalskårer, i samsvar med Edelen & Ingwersen (2018) `[Edelen2018]` 🟢. Datakvalitet eksponeres åpent langs fire datatilstander (verifisert 🟢, generisk 🟢/🟡, estimert 🟡, manglende data 🔴/🟡) og konfidensintervaller (`[Lohman2023]` 🟢; `[EC3]` 🟢).
   *FoU-hypotese F2:* Testflaten skal undersøke om synliggjøring av datakvalitetsindikatorer (DQI) øker entreprenørens og kundens trygghet på løsningsvalget sammenlignet med tradisjonelle punktestimater.
   *FoU-hypotese F3:* Prosjektet stiller et metodisk forbehold mot at klassiske vektornormaliserende MCDA-metoder (TOPSIS/COPRAS) kan utsettes for ranginversjon (*Rank Reversal*), og skal teste om en kombinasjon av AHP-kriteriavekting og MIVES-baserte absoluttverdefunksjoner gir en mer stabil beslutningsstøtte `[Mecca2023]` 🟡.

5. **Akse (e) Beslutningseffekt og attribusjon (FoU-hypotese F5):**
   *Beskrivelse:* Innebygd loggingsarkitektur i testflaten for å empirisk måle og attribuere om sammenligningen faktisk bekreftet, endret eller påvirket entreprenørens og kundens endelige valgte tilbudsløsning.
   *FoU-hypotese F5:* Prosjektet skal overvåke og registrere reelle tilbudsvalg i valideringspiloter for å dokumentere om tilgang til flerkriterie-beslutningsstøtte fører til målbare adferdsendringer mot mer bærekraftige og fuktrobuste løsningsvalg.

6. **Akse (f) Bredde i bærekraft (DNSH-prinsippet):**
   *Beskrivelse:* Integrerer Do No Significant Harm (DNSH)-kriterier som fuktrobusthet, skadeforebygging (87 600 årlige vannskader `[FinansNorge2024VASK]` 🟢) og teknisk levetid sammen med LCA (A1–A3), for å forhindre suboptimering der lav CO₂ trumfer byggeteknisk kvalitet eller levetid.

---

## 6.4 Ontologiske guardrails, kildekritisk forankring og fremdrift for IPN-søknaden

Utarbeidelsen av denne State of the Art-kandidatrapporten (v0.5) har fulgt de strengeste ontologiske og kildekritiske retningslinjene i prosjektet (`vibs-verified-ord-og-kildekart-v0.5.yml`, `ipn-kildebibliotek.md`, og `vibs-verified-kildedom-2026-06-27.md`):

1. **Terminologi:**
   - **«Løsningsvalg»** er konsekvent benyttet for å omfatte både materialer, monteringsmåte, vedlikeholdsintervall, levetid og LCC-profil i tilbudsfasen (aldri snevert «produktvalg»).
   - **«Testflate»** benyttes om VIBS-plattformens eksperimentelle verktøyflate.
   - **«Beslutningsstøtte»** benyttes om modellens rolle som åpen sammenligner. Påstander om at «VERIFIED velger / anbefaler automatisk» eller referanser til en «svart boks» er utelatt.
   - Målgruppen betegnes presist som **«entreprenør og kunde»** eller **«ikke-spesialister»**.

2. **Kildekritisk separasjon og status:**
   - **`[EBA_EU2023]` 🟢** (European Banking Authority, Report EBA/Op/2023/13 om grønne lån og bankregulering) er strengt skilt fra **`[EBA_NO2023]` 🟡** (Entreprenørforeningen Bygg og Anlegg Norge, veileder for 20 % klimagassreduksjon i boligblokker).
   - **Parkerte kilder:** `[Wiik2025]` ⏸ (SINTEF Notat nr. 57) og `[SA2018]` ⏸ (Samfunnsøkonomisk analyse Rapport 4-2018) opprettholdes som parkerte med status ⏸ i tråd med prosjektleders beslutning (2026-06-28). Utslippsreduksjoner og handlingsrom forankres i stedet i uavhengige, aktive kilder (`[EBA_NO2023]` 🟡 og `[KD2024]` 🟡).
   - Standarder for LCC forankres utelukkende i **NS-EN 16627** `[NS-EN16627]` 🟢 og **ISO 15686-5** `[ISO15686-5]` 🟡. Den utgåtte standarden NS 3454 (trukket 07.09.2023) er eksplisitt unngått.
   - Publiseringen av **EN 15978:2026** den 17. april 2026 (`[EN15978-2026]` 🟢¹) bekrefter det oppdaterte standardiseringsgrunnlaget for LCA i rehabilitering og nybygg.

3. **Innsendingsklar fremdrift:**
   Denne kandidatrapporten (`docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`) sammenstiller Seksjon 1 til Seksjon 6 i et helhetlig, faglig autoritativt norsk Markdown-dokument. Rapportens funn, 6-aksers matrise og avgrensede FoU-gap utgjør det direkte beslutningsgrunnlaget for SINTEF og Norsk forskningsråd i IPN 2026-søknaden.

---
*State of the Art kandidatrapport v0.5 er ferdigstilt i tråd med oppdragsbeskrivelse og gjeldende kildedom.*
