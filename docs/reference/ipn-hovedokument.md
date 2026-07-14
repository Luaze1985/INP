# Prosjektbeskrivelse — VERIFIED (IPN-søknad)

Dette dokumentet utgjør utkastet til prosjektbeskrivelse for forskningsprosjektet VERIFIED. Teksten er renset for interne agentnotater, fargekoder og forbeholdsmarkører, og er formulert for å fremstå beslutningsklar for konsortiet.

---

## 1. Bakgrunn og utfordring

I små og mellomstore byggeprosjekter tas mange av de mest kritiske valgene tidlig i prosessen. Det er i tilbudsfasen at entreprenøren priser arbeidet, foreslår produktløsninger og presenterer alternativer for kunden. Disse tidlige valgene legger rammene for byggets samlede miljøbelastning, tekniske levetid, fremtidige vedlikeholdsbehov og risiko for feil. Kunnskapsgrunnlag fra myndighetene indikerer at påvirkningsrommet for klimagassreduksjoner er størst nettopp i disse tidlige planleggingsfasene (Kommunal- og distriktsdepartementet mfl. 2024).

Utfordringen i næringen er ikke mangel på data. Det eksisterer store mengder produktdata i nasjonale databaser, miljødeklarasjoner (EPD), FDV-dokumentasjon, standardiserte levetidsdata og skadestatistikk. Problemet er at dataene ligger spredt, i ulike formater, og i hovedsak er utviklet for spesialister. For små og mellomstore bedrifter (SMB), som utgjør en dominerende del av utførende ledd i byggenæringen, er det krevende å ta i bruk tunge spesialistverktøy for livsløpsanalyser (LCA) og livsløpskostnader (LCC) i en travel tilbudsfasen. Kartlegginger viser at adopsjon og bruk av slike verktøy står vesentlig svakere blant mindre aktører enn i større selskaper (Nordic Council of Ministers 2023).

Driftstall for næringen understreker sårbarheten og behovet for marginforbedringer. Gjennomsnittlig driftsmargin for utførende bedrifter lå på 3,3 % i 2024 (BDO 2025), og sektoren opplevde 1 583 registrerte konkurser i 2025 (Bjørheim 2026). I tillegg peker bransjeanalyser på at kostnadsnivået for oppføring av boliger i Norge ligger vesentlig høyere enn i våre naboland, med anslag på opptil 18 000 kroner mer per kvadratmeter enn i Sverige (UNION Gruppen 2025).

Samtidig påfører kvalitetsavvik og feil samfunnet store kostnader. Beregninger fra SINTEF-forskere indikerer at utbedring av byggskader representerer en årlig kostnad på mellom 10 og 30 milliarder kroner, og at over halvparten av boliger oppført det siste tiåret har hatt minst én byggfeil (Gullbrekken og Holme 2025). Skadestatistikk fra forsikringsbransjen viser for eksempel at det i snitt registreres 10 vannskader per time i norske boliger og hytter, med en samlet erstatningskostnad på 5,1 milliarder kroner for 2023 (Finans Norge 2024). Videre indikerer bransjeanalyser at tvister og konflikter i bygg- og anleggsnæringen utgjør en betydelig samfunnsmessig ressursbruk, med anslag på opptil 2,2 milliarder kroner årlig (Samfunnsøkonomisk analyse 2019).

Fordi det mangler et enkelt og etterprøvbart beslutningsgrunnlag som integrerer pris, levetid, klima, vedlikehold og risiko, blir tilbudene i praksis ofte styrt primært av laveste innkjøpspris. VERIFIED skal møte dette gapet ved å utvikle og teste en beslutningsmodell som oversetter og sammenstiller heterogene byggevaredata to et forståelig og etterprøvbart grunnlag direkte i tilbudsfasen, tilpasset utførende fagfolk og deres kunder.

---

## 2. Mål og FoU-spørsmål

Prosjektets hovedmål er å utvikle og validere en vitenskapelig fundert beslutningsmodell for material- og produktvalg i små og mellomstore byggeprosjekter. Modellen skal gjøre det mulig for ikke-spesialister å sammenligne dimensjonene pris, klima, levetid, vedlikehold, ombruk og teknisk risiko før prosjektene låses.

For å realisere hovedmålet skal prosjektet besvare følgende seks sentrale forskningsspørsmål (FoU-spørsmål):

*   **F1: Kvalitet og levetid mot økonomi.** Hvordan kan dokumentert levetid, vedlikeholdsfrekvens og byggteknisk kvalitet oversettes til en livsløpskostnadsmodell (LCC) som dokumenterer økonomisk lønnsomhet ved holdbare materialvalg?
*   **F2: Dataintegrasjon i tilbudsfasen.** Hvordan kan produktdata fra byggevarebaser (NOBB/GTIN), miljødeklarasjoner (EPD), FDV-dokumentasjon og prisdata kobles sømløst sammen til et operasjonelt datagrunnlag i tilbudsfasen?
*   **F3: Sirkulær beslutningslogikk.** Hvordan kan modellen strukturere og synliggjøre avveininger mellom ombruk, reparasjon, vedlikehold og nyinnkjøp for spesifikke bygningsdeler?
*   **F4: Forståelse og atferdsendring.** Hvordan påvirker et integrert beslutningsgrunnlag atferden og valgene til mindre entreprenører og boligkjøpere, og hvilken form må informasjonen ha for å sikre korrekt risikoforståelse?
*   **F5: Grensesnitt mot grønn finans.** Hvordan kan dokumentert byggteknisk kvalitet og levetid oversettes til risikodata som er anvendbare for banker og forsikringsselskaper, uten at det utfordrer personvern eller krever personprofilering?
*   **F6: Sporbarhet og modellskalering.** Hvordan kan dataflyt og API-infrastruktur designes for å sikre sporbarhet av datakvalitet, og hvordan kan modellen skaleres til nye produktkategorier på en etterprøvbar måte?

Prosjektet skal ikke bevise at en ferdig løsning allerede eksisterer, men gjennomføre den nødvendige forskningen for å utvikle, teste og måle metodene i et reelt pilotmiljø.

---

## 3. Kunnskapsstatus og nyhetsverdi

### 3a. Forskningsfronten (State of the Art)
Metodegrunnlaget for miljøvurderinger og kostnadsberegninger i bygg er i dag standardisert og modent i to uavhengige spor:
1.  **Miljø/LCA:** Prinsipper og krav for livsløpsanalyser er regulert gjennom ISO 14040/14044, omfatter EN 15804+A2 som definerer reglene for produkt-EPD. På byggnivå reguleres aggregeringen av standarden EN 15978, som ble oppdatert til en ny utgave i 2026 for bedre å dekke eksisterende bygg og rehabilitering.
2.  **Kostnad/LCC:** Standarder som ISO 15686-5 definerer prinsipper for livsløpskostnader. I Norge ble den eldre standarden NS 3454 trukket i september 2023 og erstattet av den harmoniserte standarden NS-EN 16627 for økonomisk evaluering av bygninger.

Samtidig modnes datainfrastrukturen raskt. EPD-Norge leverer maskinlesbare miljødeklarasjoner, og Norsk Byggevarebase (NOBB) fungerer som bransjens felles produktdataportal. På europeisk nivå innfører revidert byggevareforordning (CPR, forordning 2024/3110) og forordningen for miljøvennlig utforming (ESPR, forordning 2024/1781) digitale produktpass (DPP) som et fremtidig transparensverktøy, der Cobuilder og partnere piloterer praktiske løsninger for byggsektoren gjennom initiativer som CIRPASS-2.

### 3b. Forskningshullet og nyhetsverdien
Selv om de enkelte byggeklossene eksisterer og er standardiserte, er de i dag fragmenterte og isolerte. Nyhetsverdien i VERIFIED ligger i selve sammenstillingen og beslutningslogikken. Eksisterende verktøy (for eksempel One Click LCA eller EC3) er utviklet for miljøspesialister og prosjekterende ledd i sene faser. Ingen etablert metode kombinerer følgende seks egenskaper:

1.  **Flerkriterie-integrasjon:** Kobling av levetid, FDV, LCC, CO2-avtrykk, ombruk og teknisk risiko i én felles modell.
2.  **Tidligfase-anvendelse:** Bruk i tilbudsfasen før kontrakter og innkjøp låses.
3.  **SMB-tilpasning:** Tilrettelagt for utførende fagfolk uten spesialistkompetanse innen LCA.
4.  **Synlig usikkerhet:** Tydelig visualisering av datakilde og dokumentasjonstillit, fremfor å skjule svake data i en aggregert totalscore.
5.  **Måling av beslutningseffekt:** Atferdsorientert forskning som måler om og hvordan informasjonen faktisk endrer valg.
6.  **DNSH-bredde (Do No Significant Harm):** Sikring av at lavt CO2-tall ikke premieres på bekostning av holdbarhet og fuktrobusthet.

Å løse disse utfordringene parallelt reiser grunnleggende forskningsspørsmål knyttet til vektingsmodeller, håndtering av ufullstendige data, og måling av atferdseffekter i beslutningsprosesser.

---

## 4. Metode og forskningsetikk

### 4a. Metode og flerkriteriemodell
Prosjektet vil anvende en iterativ forskningsmetodikk som kombinerer kvantitativ modellering med empirisk testing i pilotprosjekter.

Modelleringen skal baseres på flerkriterie-beslutningsanalyser (MCDA). I vitenskapelig litteratur om bærekraftsvurderinger i byggsektoren er Analytic Hierarchy Process (AHP) og TOPSIS de mest utbredte metodene (Mecca 2023). Prosjektet vil vurdere disse opp mot metoder som MIVES (forankret i verdiassosierte funksjoner) og COPRAS for å etablere en vektingsmodell som er både matematisk robust og forståelig for brukerne.

For å håndtere varierende datakvalitet vil det utvikles en modell for dokumentasjonstillit, inspirert av metoder for datakvalitetsindikatorer i LCA-databaser (Edelen og Ingwersen 2018; Benke mfl. 2025). Data fra offisielle, tredjepartsverifiserte kilder (som EPD) vil vektes høyere enn generiske estimater eller egenrapporterte tall fra produsenter.

### 4b. Pilotering og effektmåling
Beslutningsmodellen skal integreres som en testmodul i VIBS-plattformen og evalueres i en serie reelle pilotprosjekter. For å dokumentere faktisk effekt skal det etableres en testmetodikk som måler:
*   **Forståelse:** Hvorvidt brukerne (entreprenører og boligkjøpere) oppfatter usikkerhet og forskjeller i score.
*   **Beslutningsendring:** I hvilken grad tilgangen til modellen fører til at opprinnelig planlagte materialer byttes ut med mer holdbare eller klimavennlige alternativer, sammenlignet med en definert kontrollgruppe (baseline).
*   **Tidsbruk og kompleksitet:** At verktøyet kan betjenes innenfor rammene av ordinært tilbudsarbeid uten unødig tidsbruk.

### 4c. Forskningsetikk og personvern
Prosjektet involverer innsamling av atferdsdata, prosjektinformasjon og byggteknisk dokumentasjon. Alle empiriske undersøkelser skal følge etablerte forskningsetiske retningslinjer og personvernforordningen (GDPR). Det skal utvikles en datahåndteringsplan som sikrer at:
*   Deltakelse i pilotprosjekter baseres på informert samtykke.
*   Personidentifiserbare data og sensitive kommersielle opplysninger anonymiseres eller pseudonymiseres før analyse.
*   Modellen utelukkende vurderer byggteknisk dokumentasjon og produktkvalitet, og ikke kobles til personprofilering eller kredittvurdering av enkeltpersoner.

---

## 5. Miljø, bærekraft og samfunnseffekt

### 5a. Bidrag til FNs bærekraftsmål
VERIFIED posisjoneres spesifikt mot **bærekraftsmål 12.2** (bærekraftig forvaltning og effektiv bruk av naturressurser). Ved å integrere levetid, vedlikehold og LCC i samme modell, stimuleres det til valg som reduserer det samlede materialforbruket over byggets levetid.

Prosjektet understøtter også **mål 12.5** (redusere avfallsmengden gjennom forebygging, reduksjon, gjenvinning og ombruk). Dette kobles direkte til prioriteringen i IPN 2026-utlysningen om økt ombruk og reparasjon av knappe ressurser. Modellen skal gi konkret uttelling for produkter og løsninger som legger til rette for fremtidig ombruk eller har dokumentert restlevetid.

### 5b. Bærekraftig klimaeffekt og do-not-harm (DNSH)
For å sikre at prosjektet ikke fører til negative sideeffekter, etableres en DNSH-matrise (Do No Significant Harm) som styrer modellutviklingen:

| Risiko for negativ sideeffekt | Avbøtende tiltak i beslutningsmodellen | Målepunkt / Kontroll i prosjektet |
| --- | --- | --- |
| **1. Kortere levetid ved lavt CO2-avtrykk** | Lavt utslippstall kan ikke trumfe holdbarhet. Teknisk levetid og fuktrobusthet inngår som obligatoriske kriterier. | Vektingsregler og sensitivitetsanalyse av modellen. |
| **2. Økt ressursforbruk ved lav innkjøpspris** | Innkjøpspris avveies mot livsløpskostnad (LCC) og vedlikeholdsfrekvens over 60 år. | Modellbaserte LCC-beregninger i pilotene. |
| **3. Grønnvasking basert på uverifiserte data** | Dokumentasjonstillit (multiplikator) reduserer scoren for uverifiserte eller egenrapporterte påstander. | Audit-logg for produktdatagrunnlaget. |
| **4. Skjevfordeling til fordel for store aktører** | Modellen skal skille mellom faktisk produktprestasjon og dokumentasjonsgrad, slik at mangler synliggjøres uten å diskriminere gode produkter. | Evaluering av scorefordeling på tvers av leverandørstørrelser. |
| **5. Økt administrativ byrde for SMB** | Løsningen skal baseres på eksisterende dataoverføringer (NOBB/GTIN) for å minimere manuell registrering. | Måling av tidsbruk per tilbud i pilotene. |
| **6. Miljøskadelige stoffer overses for lav CO2** | Innhold av helse- og miljøfarlige kjemikalier (substanser på kandidatlisten/prioritetslisten) integreres i dokumentasjonsscoren. | Kobling mot sjekkliste for kjemikalieinnhold i FDV/EPD. |
| **7. Risiko ved bruk av ombruksmaterialer** | Ombrukte komponenter må dokumentere teknisk egnethet, restlevetid og transportavstand for å oppnå positiv score. | Egne kriteriesett for ombruksvarer i modellen. |

---

## 6. Samfunnsøkonomi og bro til grønn finans

VERIFIED skal først og fremst løse en byggteknisk utfordring for utførende ledd og byggherrer. Samtidig kan det strukturerte datagrunnlaget gi verdifulle ringvirkninger for finans- og forsikringssektoren.

Empirisk forskning bekrefter en signifikant sammenheng mellom energieffektive boliger og redusert misligholdsrisiko for private boliglån (Kaza mfl. 2014; Billio mfl. 2022). For næringsbygg viser tilsvarende studier en reduksjon i misligholdsrisikoen på 34 % for sertifiserte bygg (An og Pivo 2020). Dagens finansielle rammeverk og ESG-rapporteringskrav (for eksempel fra European Banking Authority 2023) etterspør i økende grad slik dokumentasjon.

Det eksisterende datagrunnlaget er imidlertid nesten utelukkende fokusert på energikarakter (EPC) og CO2-utslipp under drift. Det gjenstår et vesentlig forskningshull når det gjelder om og hvordan byggteknisk kvalitet, levetid, vedlikeholdsstatus og redusert skaderisiko påvirker det samlede risikobildet for en eiendom. VERIFIED skal utforske denne koblingen. Ved å oversette teknisk og sirkulær dokumentasjon to strukturerte data, skal prosjektet undersøke hvordan dette kan tjene som beslutningsstøtte for grønne utlånsprodukter og forsikringsvurderinger, uten bruk av personprofilering eller sensitive kundedata.

---

## 7. Planlagt gjennomføring (WP-oversikt og rammer)

Prosjektet skal gjennomføres i et nært samarbeid mellom industripartnerne og SINTEF som forskningspartner. For å sikre en strukturert fremdrift er forskningsarbeidet organisert i fem gjensidig avhengige arbeidspakker:

1.  **WP1: Datastandard og leverandørinfrastruktur.** Etablere datamodeller for integrasjon av NOBB, EPD og FDV-data, og definere krav til dokumentasjonstillit.
2.  **WP2: Kvalitetssikring og avviksdeteksjon.** Utvikle metoder for å identifisere mangelfulle eller inkonsistente data, og kartlegge risiko for tekniske avvik tidlig.
3.  **WP3: Pilotportefølje og effektmåling.** Etablere testmiljø og måle faktisk endring i beslutningsatferd mot en definert baseline i reelle byggeprosjekter.
4.  **WP4: Brukeradopsjon og kompetanseheving.** Utvikle metoder for formidling og visualisering som sikrer at ikke-spesialister forstår risikobildet.
5.  **WP5: Skalering og kommersiell utrulling.** Evaluere overføringsverdi to nye produktkategorier og forberede integrasjon mot finansielle risikomodeller.

Søknaden rammes inn av de offisielle IPN-retningslinjene (støttebeløp innenfor rammen 1–16 MNOK, med maksimalt 50 % støttesats for bedriftenes kostnader), og skal presenteres som et PDF-vedlegg begrenset til maksimalt 10 sider.
