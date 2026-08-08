# VERIFIED — samlet K/V-tekst, kandidat v0.6

**Status:** K/V-integrasjonskandidat med kildepass og språkport
**Dato:** 2026-08-04
**Baseline:** `soknadstekst-samlet-kandidat-v0.4.md`
**Tekstgrunnlag:** godkjente arbeidsversjoner for K1–K4 og V1–V3, datert 2026-07-24–25
**Avgrensning:** Formuleringer og prosjektlogikk for K1–K4 og V1–V3 er innarbeidet. `v0.4` er låst baseline for innholdsdekning. Kildestatus er ikke oppgradert. Kandidaten må gjennom samlet kilde- og innflettingskontroll før den kan regnes som innsendingsklar.

## Sammendrag

VERIFIED skal utvikle og teste en forskningsbasert beslutningsmodell for sammenligning av alternative løsninger i små og mellomstore byggeprosjekter. Modellen skal brukes i tilbudsfasen, der entreprenøren priser jobben, foreslår løsninger og forklarer dem for kunden.

Prosjektet skal undersøke hvordan pris, klima, levetid, vedlikehold, teknisk kvalitet, ombruk, dokumentasjon og risiko kan settes sammen til et forklarbart og etterprøvbart beslutningsgrunnlag. Grunnlaget skal vise forskjeller, avveininger og usikkerhet uten at verktøyet tar beslutningen for entreprenøren og kunden.

VERIFIED skal utvikles og testes gjennom konkrete løsningsvalg. Prosjektet skal måle om entreprenør og kunde forstår grunnlaget, hvordan de bruker det, om det endrer eller bekrefter valget, og om nytten forsvarer tidsbruken. VIBS-plattformen er prosjektets testflate. Forsknings- og utviklingsarbeidet (FoU) ligger i VERIFIED-lagets metode, datakvalitet, vekting, usikkerhet og måling av beslutningseffekt.

Arbeidet forutsetter samarbeid mellom forskningsmiljø, utførende entreprenør- og håndverksbedrifter, produktleverandører og aktører som forvalter produktdata.

## K1 — Bakgrunn og utfordring

### Tilbudsfasen

I små og mellomstore byggeprosjekter tas mange sentrale løsningsvalg i tilbudsfasen. Entreprenøren priser jobben, foreslår alternative løsninger og forklarer dem for kunden. Valgene kan få betydning for utslipp, levetid, vedlikehold og risiko senere i prosjektet.

### Spredt informasjon

Relevant informasjon finnes i flere kilder, blant annet produktdata, dokumentasjon for forvaltning, drift og vedlikehold (FDV), miljødeklarasjoner (EPD-er), levetidsdata og prisdata. Informasjonen bruker ulike formater og må ofte sammenstilles manuelt. Prosjektets utgangspunkt er at dette gjør den vanskelig å bruke samlet i tilbudsfasen.

### Ressurser i små bedrifter

Mindre entreprenørbedrifter har ofte høy fagkompetanse. Tilgangen til egne ressurser for livsløpsvurderinger (LCA), kostnadsanalyser over levetiden og andre spesialiserte vurderinger varierer. Mye av kapasiteten er bundet i produksjon og utførende arbeid, og et beslutningsgrunnlag må derfor kunne tas raskt i bruk i tilbudsarbeidet.

### Sammenligningsbehovet

I tilbudsfasen må entreprenøren veie pris, faglig erfaring og tilgjengelig dokumentasjon mot hverandre. Uten et samlet grunnlag er det krevende å sammenligne alternative løsninger på tvers av levetid, klima, vedlikehold, ombruk og dokumentasjonskvalitet.

Kunden har på sin side ofte begrenset faglig grunnlag for å vurdere tilbud utover pris. Løsningsvalgene påvirker utslipp, ressursbruk, levetid, vedlikehold og risiko for feil. Når slike forskjeller ikke er synlige i tilbudsfasen, kan et valg som ser rimelig ut på pris, gi høyere kostnader og større belastning senere.

## K2 — Nyhetsverdi

### Hva nyhetsverdien er

VERIFIEDs nyhetsverdi ligger i å utvikle og teste hvordan flere typer byggdata kan settes sammen til et forklarbart og etterprøvbart beslutningsgrunnlag i tilbudsfasen. FoU-arbeidet omfatter datakvalitet, vekting, usikkerhet og måling av beslutningseffekt.

### Eksisterende datakilder og metoder

Flere deler av grunnlaget finnes allerede. Det finnes standarder for livsløpsvurdering og livsløpskostnader, EPD-er, produktdata, FDV-data og metoder for å veie flere hensyn mot hverandre.

Tilgjengelighet, kvalitet og format varierer mellom datakildene. De undersøkte standardene, datakildene, metodene og verktøyene dekker ulike deler av behovet. SmartKalk kobler kalkyle, pris og klima i tilbudsarbeidet. Reduzer kobler anbudsarbeid, EPD-er og klimagassberegning. One Click LCA kombinerer LCA og LCC, mens EC3 viser datakvalitet og usikkerhet i karbonberegninger. I det undersøkte, ikke uttømmende utvalget er det ikke dokumentert ett verktøy som samler hele VERIFIED-kombinasjonen for norske små entreprenører i tilbudsfasen.

### Hva VERIFIED skal undersøke

VERIFIED skal undersøke hvordan disse datakildene og metodene kan settes sammen til et enkelt, forklarbart og etterprøvbart beslutningsgrunnlag i tilbudsfasen. Prosjektet skal teste om informasjonen kan gjøres anvendbar for mindre entreprenører og kunder før innkjøpet er låst.

### Forskningshullet

Forskningshullet kan beskrives med seks spørsmål:

| Spørsmål | Forsiktig formulering |
| --- | --- |
| Kan flere datatyper kobles? | Eksisterende løsninger dekker ulike deler av kombinasjonen. En samlet løsning for hele bredden er ikke dokumentert i det undersøkte utvalget. |
| Brukes det i tilbudsfasen? | SmartKalk og Reduzer dokumenterer tilbudsrelevans for deler av behovet. Bruk av hele kombinasjonen er ikke dokumentert i gjennomgangen. |
| Kan små entreprenører bruke det? | Ressursbehov og anvendbarhet for små entreprenører er ikke tilstrekkelig dokumentert. |
| Vises usikkerheten? | EC3 dokumenterer synlig usikkerhet i karbonarbeid. Gjennomgående visning på tvers av alle kriteriene er ikke dokumentert i gjennomgangen. |
| Måles beslutningseffekt? | Gjennomgangen identifiserte ingen dokumentert metode i det undersøkte materialet for å måle og tilskrive om et slikt samlet grunnlag endret eller bekreftet valget. |
| Håndteres do-not-harm? | En samlet behandling av klima, levetid, vedlikehold, ombruk og teknisk risiko er ikke dokumentert i gjennomgangen. |

Prosjektet skal teste disse spørsmålene. VERIFIED skal fungere som beslutningsstøtte: modellen viser forskjeller, avveininger og usikkerhet mellom alternative løsninger. Entreprenøren og kunden tar beslutningen og beholder ansvaret.

Et slikt grunnlag kan også bli relevant for en bank som etterspør etterprøvbar prosjekt- og byggdokumentasjon. Hvordan og i hvilken grad dette kan brukes, skal undersøkes mot ett avgrenset bankbehov i prosjektet.

## K3 — Mål og FoU-spørsmål

### Hovedmål

Hovedmålet er å utvikle og teste en forskningsbasert beslutningsmodell for sammenligning av alternative løsninger i små og mellomstore byggeprosjekter.

Modellen skal gjøre det mulig å sammenligne pris, klima, levetid, vedlikehold, teknisk kvalitet, ombruk, dokumentasjon og risiko før valget tas. Den skal også vise når grunnlaget er godt, når det er svakt, og når det mangler data.

### Delmål

Prosjektet skal:

1. kartlegge hvilke datakilder og informasjonsfelt som trengs for å sammenligne alternative løsninger i tilbudsfasen
2. utvikle en åpen og begrunnet beslutningsmodell for slike sammenligninger
3. teste hvordan forskjeller, avveininger og usikkerhet bør vises for entreprenør og kunde
4. prøve om modellen gir praktisk nytte i konkrete løsningsvalg

### FoU-bidraget

Prosjektets FoU-bidrag omfatter dokumentasjon og forklaring av vekting, datakvalitet og usikkerhet, samt empirisk testing av modellen i reelle løsningsvalg.

VERIFIED skal teste om entreprenører og kunder forstår grunnlaget, hvordan de bruker det, og om det endrer eller bekrefter valget.

### FoU-spørsmål

| ID | Tema | FoU-spørsmål |
| --- | --- | --- |
| F1 | Kvalitet og levetid mot økonomi | Hvordan kan dokumentasjon av levetid, vedlikehold og kvalitet omsettes til sammenlignbare livsløpskostnader og inngå i avveiingen mellom økonomi, klima og teknisk kvalitet? |
| F2 | Data tidlig nok i tilbud | Kan varedata fra NOBB, globale produktnumre (GTIN), miljødeklarasjoner (EPD), FDV-dokumentasjon og prisdata kobles slik at de kan brukes før tilbudet sendes? |
| F3 | Ombruk, reparasjon og rehabilitering | Hvordan kan modellen synliggjøre avveininger mellom ombruk, reparasjon, vedlikehold, rehabilitering og nyanskaffelse under ulike forutsetninger for kostnad, klima, levetid og dokumentasjonskvalitet? |
| F4 | Forståelse og beslutning | Hvordan forstår og bruker små og mellomstore entreprenørbedrifter og kunder beslutningsgrunnlaget, og i hvilken grad endrer eller bekrefter det valget de tar? |
| F5 | Byggdata mot bank | Hvordan kan dokumentasjon av byggteknisk kvalitet, levetid og vedlikeholdsbehov struktureres som relevant tilleggsinformasjon for bankens vurdering, uten personprofilering eller automatisk kredittbeslutning? |
| F6 | Sporbarhet og skalering | Hvordan kan dataflyt, dokumentasjon og nødvendige grensesnitt utformes og testes slik at modellen er etterprøvbar og kan overføres til en ny produktkategori? |

## K4 — Metode og forskningsetikk

### Forskningsløype

Prosjektet skal bruke en trinnvis utviklings- og utprøvingsprosess. Først utvikles en første versjon av beslutningsmodellen. Den prøves deretter i konkrete løsningsvalg, resultatene måles, og modellen justeres på grunnlag av funnene. Endelig forskningsdesign og validering utformes sammen med forskningspartneren.

### Datagrunnlag og dokumentasjonstillit

Først samles data fra produktkilder, dokumentasjon og praktiske utprøvinger (piloter). Datagrunnlaget kan omfatte pris, EPD, FDV, levetid, vedlikehold, ombruksmulighet, kvalitet og dokumentasjonsstatus.

For hver opplysning registreres kilde, alder, enhet, produktnivå og dokumentasjonsstatus. Statusen skal vise om opplysningen mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen. Reglene for status og dokumentasjonstillit fastsettes før piloteringen og brukes likt på alle alternativer. Slik skal svake eller manglende data ikke skjules i en totalscore.

### Minste informasjonsgrunnlag og teknisk egnethet

Prosjektet skal definere hvilket minste informasjonsgrunnlag som trengs for å sammenligne en løsning på en faglig forsvarlig måte. Dersom grunnlaget er for svakt, skal dette vises tydelig.

Teknisk egnethet fungerer som en faglig port. Pilotprotokollen skal angi hvem som vurderer egnetheten og hvilket informasjonsgrunnlag vurderingen krever. Uklar eller mangelfull dokumentasjon skal gi synlig uavklart status og krav om faglig vurdering før valg.

### Flerkriteriemodell og metodevalg

Deretter utvikles en flerkriteriemodell som viser avveininger mellom pris, klima, levetid, kvalitet, vedlikehold, ombruk, dokumentasjon og risiko.

Prosjektet skal sammenligne aktuelle flerkriteriemetoder ut fra faste krav: hvor lett vektingen kan forklares, hvor følsomt resultatet er for endrede vekter, hvilke data metoden krever, hvordan manglende data håndteres, og om entreprenør og kunde forstår resultatet. På dette grunnlaget velges én metode eller en avgrenset metodekombinasjon for piloteringen.

### Visning av resultatet

Sammenligningen skal ha to nivåer. Først skal entreprenør og kunde få et enkelt overblikk over hva som taler for, imot og er usikkert ved hvert alternativ. Deretter skal entreprenøren kunne kontrollere dokumentasjon, datagrunnlag og vekting.

### Aktuelle testområder

Prosjektet skal undersøke testbehovet på områder som:

1. valg mellom alternative takløsninger
2. valg mellom alternative innvendige vegg- eller overflateløsninger
3. valg mellom reparasjon, utsatt utskifting og ny løsning
4. vurdering av ombruk der det faktisk er relevant

Eksakte testtyper, protokoller og partnerpiloter utformes sammen med konsortiet og forskningspartneren i gjennomføringsplanen.

### Pilotering og måling

Modellen testes i reelle løsningsvalg. Før piloteringen kobles hvert FoU-spørsmål til datakilde, målepunkt, sammenligningsgrunnlag og kriterium for vurdering.

Testene skal sammenligne vanlig tilbudsarbeid med tilbudsarbeid der VERIFIED brukes. For hver test skal prosjektet dokumentere løsningene som ble sammenlignet, tilgjengelige opplysninger, mangler, faglige avklaringer og hvordan entreprenør og kunde brukte grunnlaget.

| Hva måles | Eksempel på målepunkt |
| --- | --- |
| Dataintegrasjon | Andel nødvendige felt som kan kobles, og behov for manuell behandling |
| Livsløpssammenligning | Om levetid og vedlikehold kan omsettes til sammenlignbare kostnader |
| Forklarbarhet | Om entreprenør og kunde forstår hvorfor alternativene får ulike resultater |
| Usikkerhet | Om entreprenør og kunde oppdager manglende, generelle eller estimerte data |
| Beslutningseffekt | Om grunnlaget endrer, bekrefter eller ikke påvirker valget |
| Tidsbruk | Tid brukt sammenlignet med vanlig tilbudsarbeid |
| Bankrelevans | Om den avtalte dokumentasjonen svarer på bankens definerte informasjonsbehov |
| Skalering | Hvilke deler av modellen som kan overføres til en ny produktkategori |
| Sirkulær sammenligning | Materialmengde, restlevetid, teknisk egnethet og beregnede utskiftninger for nyanskaffelse, reparasjon, rehabilitering og ombruk |

### Forskningsetikk og datahåndtering

Pilotene kan omfatte brukerdata, kommersielt sensitive opplysninger og beslutningsdata. Prosjektet skal samle inn minst mulig persondata, informere deltakerne om formål, databruk, lagringstid og retten til å trekke seg, og anonymisere eller pseudonymisere forskningsdata før analyse.

Datakilder, antakelser og usikkerhet skal være sporbare. Prosjektet konkretiserer datahåndteringsplanen ved eventuell tildeling. Søknaden beskriver prinsippene, risikoene og ansvarsdelingen.

## V1 — Miljø og bærekraft

### Hovedbidrag

Prosjektets viktigste bærekraftsbidrag er bedre bruk av ressurser i bygg. Det treffer særlig FNs bærekraftsmål 12.2 om effektiv bruk av naturressurser.

Prosjektet har også et sekundært bærekraftsmål: 12.5 om å redusere avfallsmengden gjennom forebygging og ombruk. Mekanismen er at materiale som beholdes lenger, ikke blir avfall i samme periode. VERIFIED-modellen sammenligner ombruk, reparasjon, rehabilitering og utsatt utskifting med nyanskaffelse, og pilotene måler restlevetid, materialmengde og antall beregnede utskiftninger for alternativene som sammenlignes.

### Mekanismen

Prosjektet konsentrerer bærekraftsarbeidet om målbare virkninger av løsningsvalg. VERIFIED-modellen sammenligner nyanskaffelse, vedlikehold, reparasjon, rehabilitering og ombruk der alternativene er teknisk relevante. Pilotene måler hvordan dette grunnlaget påvirker eller bekrefter løsningsvalgene.

### Klima og systemgrense

VERIFIED sammenligner utslipp og kostnad for konkrete alternativer innenfor en definert systemgrense. Pilotene måler om en forklarbar modell gjør avveiningene lettere i praksis. Prosjektet oppgir ingen generell prosentsats for klimaeffekt før den tilhørende originalanalysen er kontrollert.

### Målt og beregnet effekt

Prosjektet skal sammenligne resultatene mot et definert sammenligningsgrunnlag. Noen resultater kan måles direkte i pilotene, som tidsbruk, forståelse og endring av valg. Andre virkninger, som framtidige utskiftninger, klimagassutslipp og livsløpskostnader, må beregnes ut fra dokumenterte forutsetninger.

| Effektområde | Målepunkt i piloten | Sammenligningsgrunnlag |
| --- | --- | --- |
| Klimagassutslipp | Beregnede klimagassutslipp per funksjonell enhet eller bygningsdel | Valgt løsning mot ett eller flere reelle alternativer |
| Ressursbruk | Materialmengde, forventet levetid og antall beregnede utskiftninger | Nyanskaffelse mot reparasjon, rehabilitering eller ombruk |
| Livsløpskostnad | Anskaffelse, vedlikehold og beregnede utskiftninger | Kostnad over avtalt analyseperiode |
| Beslutningseffekt | Om grunnlaget endrer, bekrefter eller ikke påvirker valget | Valg før og etter at sammenligningen vises |
| Brukbarhet | Forståelse, tidsbruk og behov for hjelp | Vanlig tilbudsarbeid mot bruk av VERIFIED |
| Dokumentasjonskvalitet | Andel opplysninger som mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen | Alternativene som sammenlignes |

### Feil og omarbeid

Prosjektet skal undersøke om bedre dokumentasjon kan redusere risikoen for feil og omarbeid. I prosjektperioden måles dokumentasjonsmangler og eventuelle observerbare avvik. Faktisk effekt på reklamasjoner og langsiktige byggskader kan ikke fastslås uten lengre oppfølging.

### Sirkulærøkonomi

VERIFIED behandler ombruk, reparasjon, rehabilitering og vedlikehold som reelle alternativer i sammenligningen. Pilotene måler restlevetid, redusert materialbruk og teknisk egnethet for disse alternativene der de er relevante.

### Do-not-harm

Prosjektet skal også teste mulige negative sideeffekter. Lavt klimagassutslipp skal ikke alene gi et alternativ høy vurdering dersom levetid, fuktrobusthet, vedlikeholdsbehov eller dokumentasjonskvalitet er svak.

Ombruk og reparasjon skal bare vurderes som positive alternativer når teknisk egnethet, restlevetid, transport, ansvar og faktisk materialbesparelse kan dokumenteres.

## V2 — Do-not-harm

### Del av modellen og piloteringen

Do-not-harm skal inngå i beslutningsmodellen og piloteringen. Hvert alternativ skal vurderes for mulige negative virkninger på levetid, teknisk risiko, dokumentasjonskvalitet, ressursbruk, helse og sikkerhet.

Modellen viser avveininger, usikkerhet og mulige negative konsekvenser ved hvert alternativ uten å utpeke ett som best. Levetid, dokumentasjonskvalitet og teknisk risiko inngår i vurderingen på lik linje med klimagassutslipp og pris. Svakheter ved ett kriterium er synlige selv når et annet er gunstig.

### Operative regler

Hver identifisert risiko skal knyttes til en modellregel, en reaksjon og en test i piloten.

| Risiko | Modellregel og reaksjon | Hvordan det testes |
| --- | --- | --- |
| Lavt klimagassutslipp kombinert med svak levetid eller teknisk risiko | Levetid, vedlikehold og teknisk risiko vises separat, med tydelig advarsel og synlig avveining | Test om entreprenør og kunde oppdager konflikten mellom kriteriene |
| Lav pris kombinert med økt materialbruk eller utskifting | Nyanskaffelse sammenlignes med reparasjon, vedlikehold, rehabilitering og ombruk der det er relevant | Sammenlign livsløpskostnad og beregnet ressursbruk |
| Manglende nødvendig produktdokumentasjon | Alternativet kan ikke få status som verifisert; det får stopp eller tydelig uavklart status | Registrer manglende dokumentasjon og om den kan suppleres |
| Generelle eller estimerte data framstår som sikre | Datastatus og usikkerhet vises for hvert relevant datapunkt | Test om entreprenør og kunde oppdager usikkerheten |
| Store leverandører favoriseres av bedre dokumentasjon | Produktprestasjon og dokumentasjonskvalitet vurderes separat | Kontroller at samme mangel ikke straffes i begge dimensjoner |
| Økt rapporteringsbyrde for små bedrifter | Tidsbruk og behov for dobbelregistrering måles | Sammenlign tidsbruk med vanlig tilbudsarbeid |
| Person- eller kredittdata brukes i banksporet | Bare produkt-, prosjekt- og byggdokumentasjon tillates; personprofilering og automatisk kredittbeslutning stoppes | Kontroller datakilder, tilgang og lagring |
| Ombruk uten dokumentert teknisk egnethet | Egnethet, restlevetid, transport og ansvar må dokumenteres | Kontroller dokumentasjonskravene i piloten |
| Kjemikalie-, helse- eller sikkerhetsfare overses | Lavt klimagassutslipp skal ikke overstyre dokumenterte krav | Kartlegg hvilke opplysninger som finnes og hva som ligger utenfor modellen |
| Reparasjon eller vedlikehold brukes uten reell effekt | Utsatt utskifting, spart materiale og teknisk forsvarlighet må dokumenteres | Sammenlign mot nyanskaffelse og dokumenter forutsetningene |
| Effekt påstås uten sammenligningsgrunnlag | Hver effekt kobles til sammenligningsgrunnlag, indikator, datakilde og måleansvarlig | Kontroller måleplanen før pilotstart |

### Felles datastatus

Datastatus skal vise om en opplysning mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen. En usikker eller generell opplysning skal ikke framstilles med samme presisjon som en produktspesifikk, verifisert opplysning.

Leverandører skal kunne supplere eller korrigere dokumentasjonen før vurderingen låses.

### Falsk presisjon og følsomhet

En poengsum kan virke sikrere enn datagrunnlaget er. Prosjektet skal derfor vise datakilder, datakvalitet, antakelser og begrensninger.

Prosjektet skal undersøke hvor følsomt resultatet er for sentrale vekter, forutsetninger og datamangler. Metode og terskler for følsomhetsvurderingen utformes sammen med forskningspartneren.

### Kjemikalier og sosiale forhold

Prosjektet skal undersøke hvilke kjemikalie-, helse- og sikkerhetsopplysninger som er tilgjengelige i EPD, FDV og annen produktdokumentasjon, og synliggjøre når nødvendig informasjon mangler eller ligger utenfor modellen.

Prosjektet skal også avklare hvilke sosiale og leverandørrelaterte forhold som kan dokumenteres gjennom tilgjengelige produkt- og prosjektdata. Forhold modellen ikke kan kontrollere, skal beskrives som utenfor vurderingsgrunnlaget og skal ikke framstilles som verifisert.

### Beslutningsansvar

VERIFIED skal gi beslutningsstøtte. Modellen skal ikke profilere personer eller ta kredittbeslutninger. Aktørene som bruker grunnlaget, har det faglige og kommersielle beslutningsansvaret.

## V3 — Økonomiske virkninger og bankrelevans

### Virkninger for entreprenøren

For entreprenøren skal prosjektet undersøke om beslutningsgrunnlaget påvirker tidsbruk, tilbudskvalitet, dokumentasjonsmangler og observerbare avvik. Faktisk effekt på omarbeid og reklamasjoner kan bare vurderes dersom pilotperioden og datagrunnlaget gjør det mulig.

### Virkninger for kunden

For kunden skal modellen vise anskaffelseskostnad, beregnede livsløpskostnader, relevante tekniske forskjeller og usikkerhet ved alternativene. Prosjektet skal teste om kunden forstår denne informasjonen og hvordan den påvirker valget.

### Kunnskapsgrunnlag og FoU-hull

Kaza (2014) og Billio mfl. (2022) dokumenterer avgrensede sammenhenger mellom energieffektivitet og lavere misligholdsrisiko i boliglån i henholdsvis USA og Nederland. European Banking Authority beskriver behov for tydeligere og mer sammenlignbare data i markedet for grønne lån `[EBA_EU2023]`.

Den gjennomførte kunnskapskartleggingen fant avgrenset dokumentasjon om energieffektivitet og misligholdsrisiko. Sammenhengen mellom byggteknisk kvalitet, levetid, vedlikeholdsbehov og bankens risikovurdering står derfor som et FoU-spørsmål.

### Avgrenset bankpilot

Prosjektet skal undersøke om dokumentasjon av byggteknisk kvalitet, levetid og vedlikeholdsbehov kan struktureres som relevant tilleggsinformasjon for et avgrenset behov hos en bank.

Banken må før piloteringen definere hvilken informasjon den trenger, hvordan informasjonen skal vurderes, og hva som skal regnes som et nyttig resultat. Grunnlaget skal bare bygge på produkt-, prosjekt- og byggdokumentasjon. Det skal ikke brukes til personprofilering eller automatiske kredittbeslutninger.

| Virkning som testes | Målepunkt |
| --- | --- |
| Tidsbruk i tilbud | Tid med og uten beslutningsgrunnlaget |
| Tilbudskvalitet | Fullstendighet og synliggjorte alternativer |
| Livsløpsøkonomi | Anskaffelse, vedlikehold og beregnede utskiftninger |
| Dokumentasjonskvalitet | Manglende, generelle, estimerte og verifiserte opplysninger |
| Kundens forståelse | Forståelse av kostnad, risiko og usikkerhet |
| Bankrelevans | Om dokumentasjonen svarer på bankens forhåndsdefinerte informasjonsbehov |

## Referanser

Hver bærende påstand skal kobles til originalkilde, relevant passasje og avgrenset bevisrolle i kildepasset. Den samlede kildevurderingen for `v0.5` er kontrollgrunnlaget for denne kandidaten.
