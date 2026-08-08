# VERIFIED — samlet K/V-tekst, kandidat v0.7

**Status:** K/V-integrasjonskandidat etter beslutningspasset 2026-08-05
**Dato:** 2026-08-05
**Baseline:** `soknadstekst-samlet-kandidat-v0.6.md` (bevart urørt som sendt arbeidsgrunnlag)
**Tekstgrunnlag:** godkjente arbeidsversjoner for K1–K4 og V1–V3, datert 2026-07-24–25
**Styringsregister:** `reviews/2026-08-05-tilbakemeldingsregister-v0.6.md`
**Avgrensning:** Kandidaten dekker K1–K4 og V1–V3. Gjennomføring, arbeidspakker, milepæler, budsjett, risiko og utnyttelse er ikke skrevet her — de krever bekreftet konsortium og faglig eier, og hentes fortsatt fra `v0.4` som baseline. Kildestatus er ikke oppgradert i denne versjonen. Kandidaten må gjennom samlet kilde- og innflettingskontroll før den kan regnes som innsendingsklar.

## Sammendrag

VERIFIED utvikler og tester en forskningsbasert beslutningsmodell for sammenligning av alternative løsninger i små og mellomstore byggeprosjekter. Modellen hører hjemme i tilbudsfasen, der entreprenøren priser jobben, foreslår løsninger og forklarer dem for kunden.

Prosjektet undersøker hvordan pris, klima, levetid, vedlikehold, teknisk kvalitet, ombruk, dokumentasjon og risiko kan settes sammen til et forklarbart og etterprøvbart beslutningsgrunnlag. Målet er et grunnlag som viser forskjeller, avveininger og usikkerhet, uten at verktøyet tar beslutningen for entreprenøren og kunden.

Modellen utvikles og prøves i konkrete løsningsvalg. Prosjektet måler om entreprenør og kunde forstår grunnlaget, hvordan de bruker det, om det endrer eller bekrefter valget, og om nytten forsvarer tidsbruken. VIBS-plattformen er prosjektets testflate. Forsknings- og utviklingsarbeidet (FoU) ligger i VERIFIED-lagets metode, datakvalitet, vekting, usikkerhet og måling av beslutningseffekt.

Arbeidet forutsetter samarbeid mellom forskningsmiljø, utførende entreprenør- og håndverksbedrifter, produktleverandører og aktører som forvalter produktdata.

## K1 — Bakgrunn og utfordring

### Tilbudsfasen

I små og mellomstore byggeprosjekter tas mange sentrale løsningsvalg i tilbudsfasen. Entreprenøren priser jobben, foreslår alternative løsninger og forklarer dem for kunden. Valgene kan få betydning for utslipp, levetid, vedlikehold og risiko senere i prosjektet.

### Spredt informasjon

Relevant informasjon finnes i flere kilder, blant annet produktdata, dokumentasjon for forvaltning, drift og vedlikehold (FDV), miljødeklarasjoner (EPD-er), levetidsdata og prisdata. Informasjonen bruker ulike formater og må ofte sammenstilles manuelt. Prosjektets utgangspunkt er at dette gjør den vanskelig å bruke samlet i tilbudsfasen.

### Ressurser i små bedrifter

Mindre entreprenørbedrifter har ofte høy fagkompetanse. Tilgangen til egne ressurser for livsløpsvurderinger (LCA), kostnadsanalyser over levetiden og andre spesialiserte vurderinger varierer. Mye av kapasiteten er bundet i produksjon og utførende arbeid. Et beslutningsgrunnlag må derfor kunne tas raskt i bruk i tilbudsarbeidet.

### Sammenligningsbehovet

I tilbudsfasen må entreprenøren veie pris, faglig erfaring og tilgjengelig dokumentasjon mot hverandre. Uten et samlet grunnlag er det krevende å sammenligne alternative løsninger på tvers av levetid, klima, vedlikehold, ombruk og dokumentasjonskvalitet.

Kunden har på sin side ofte begrenset faglig grunnlag for å vurdere tilbud utover pris. Løsningsvalgene påvirker utslipp, ressursbruk, levetid, vedlikehold og risiko for feil. Når slike forskjeller ikke er synlige i tilbudsfasen, kan et valg som ser rimelig ut på pris, gi høyere kostnader og større belastning senere.

## K2 — Nyhetsverdi

### Hva nyhetsverdien er

VERIFIEDs nyhetsverdi ligger i å utvikle og teste hvordan flere typer byggdata kan settes sammen til et forklarbart og etterprøvbart beslutningsgrunnlag i tilbudsfasen. FoU-arbeidet omfatter datakvalitet, vekting, usikkerhet og måling av beslutningseffekt.

### Eksisterende datakilder og metoder

Flere deler av grunnlaget finnes allerede. Det finnes standarder for livsløpsvurdering og livsløpskostnader, EPD-er, produktdata, FDV-data og metoder for å veie flere hensyn mot hverandre.

Tilgjengelighet, kvalitet og format varierer mellom datakildene. De undersøkte standardene, datakildene, metodene og verktøyene dekker ulike deler av behovet. SmartKalk kobler kalkyle, pris og klima i tilbudsarbeidet. Reduzer kobler anbudsarbeid, EPD-er og klimagassberegning. One Click LCA kombinerer LCA og LCC, mens EC3 viser datakvalitet og usikkerhet i karbonberegninger. I det undersøkte, ikke uttømmende utvalget er det ikke dokumentert ett verktøy som samler hele VERIFIED-kombinasjonen for norske små entreprenører i tilbudsfasen.

### Hva VERIFIED undersøker

Prosjektet undersøker hvordan disse datakildene og metodene kan settes sammen til et enkelt, forklarbart og etterprøvbart beslutningsgrunnlag i tilbudsfasen, og tester om informasjonen kan gjøres anvendbar for mindre entreprenører og kunder før innkjøpet er låst.

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

Prosjektet tester disse spørsmålene. VERIFIED fungerer som beslutningsstøtte: modellen viser forskjeller, avveininger og usikkerhet mellom alternative løsninger. Entreprenøren og kunden tar beslutningen og beholder ansvaret.

Et slikt grunnlag kan også bli relevant for en bank som etterspør etterprøvbar prosjekt- og byggdokumentasjon. Hvordan og i hvilken grad dette kan brukes, undersøkes mot ett avgrenset bankbehov i prosjektet.

## K3 — Mål og FoU-spørsmål

### Hovedmål

Hovedmålet er å utvikle og teste en forskningsbasert beslutningsmodell for sammenligning av alternative løsninger i små og mellomstore byggeprosjekter.

Modellen som utvikles, gjør det mulig å sammenligne pris, klima, levetid, vedlikehold, teknisk kvalitet, ombruk, dokumentasjon og risiko før valget tas. Den viser også når grunnlaget er godt, når det er svakt, og når det mangler data.

### Delmål

Prosjektet har fire delmål:

1. kartlegge hvilke datakilder og informasjonsfelt som trengs for å sammenligne alternative løsninger i tilbudsfasen
2. utvikle en åpen og begrunnet beslutningsmodell for slike sammenligninger
3. teste hvordan forskjeller, avveininger og usikkerhet bør vises for entreprenør og kunde
4. prøve om modellen gir praktisk nytte i konkrete løsningsvalg

### FoU-bidraget

Prosjektets FoU-bidrag omfatter dokumentasjon og forklaring av vekting, datakvalitet og usikkerhet, samt empirisk testing av modellen i reelle løsningsvalg.

Prosjektet tester om entreprenører og kunder forstår grunnlaget, hvordan de bruker det, og om det endrer eller bekrefter valget.

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

Prosjektet bruker en trinnvis utviklings- og utprøvingsprosess. Først utvikles en første versjon av beslutningsmodellen. Den prøves deretter i konkrete løsningsvalg, resultatene måles, og modellen justeres på grunnlag av funnene. Endelig forskningsdesign og validering utformes sammen med forskningspartneren.

### Datagrunnlag og dokumentasjonstillit

Først samles data fra produktkilder, dokumentasjon og praktiske utprøvinger (piloter). Datagrunnlaget kan omfatte pris, EPD, FDV, levetid, vedlikehold, ombruksmulighet, kvalitet og dokumentasjonsstatus.

For hver opplysning registreres kilde, alder, enhet, produktnivå og dokumentasjonsstatus. Statusen viser om opplysningen mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen. Reglene for status og dokumentasjonstillit fastsettes før piloteringen og brukes likt på alle alternativer. Slik holdes svake eller manglende data synlige i stedet for å forsvinne i en totalscore.

### Minste informasjonsgrunnlag og teknisk egnethet

Prosjektet definerer hvilket minste informasjonsgrunnlag som trengs for å sammenligne en løsning på en faglig forsvarlig måte. Et for svakt grunnlag vises tydelig.

Teknisk egnethet fungerer som en faglig port. Pilotprotokollen angir hvem som vurderer egnetheten og hvilket informasjonsgrunnlag vurderingen krever. Uklar eller mangelfull dokumentasjon gir synlig uavklart status og krav om faglig vurdering før valg.

### Flerkriteriemodell og metodevalg

Deretter utvikles en flerkriteriemodell som viser avveininger mellom pris, klima, levetid, kvalitet, vedlikehold, ombruk, dokumentasjon og risiko.

Prosjektet sammenligner aktuelle flerkriteriemetoder ut fra faste krav: hvor lett vektingen kan forklares, hvor følsomt resultatet er for endrede vekter, hvilke data metoden krever, hvordan manglende data håndteres, og om entreprenør og kunde forstår resultatet. På dette grunnlaget velges én metode eller en avgrenset metodekombinasjon for piloteringen.

### Visning av resultatet

Sammenligningen har to nivåer. Først får entreprenør og kunde et enkelt overblikk over hva som taler for, imot og er usikkert ved hvert alternativ. Deretter kan entreprenøren kontrollere dokumentasjon, datagrunnlag og vekting.

### Aktuelle testområder

Prosjektet undersøker testbehovet på områder som:

1. valg mellom alternative takløsninger
2. valg mellom alternative innvendige vegg- eller overflateløsninger
3. valg mellom reparasjon, utsatt utskifting og ny løsning
4. vurdering av ombruk der det faktisk er relevant

Eksakte testtyper, protokoller og partnerpiloter utformes sammen med konsortiet og forskningspartneren i gjennomføringsplanen.

### Pilotering og måling

Modellen testes i reelle løsningsvalg. Før piloteringen kobles hvert FoU-spørsmål til datakilde, målepunkt, sammenligningsgrunnlag og kriterium for vurdering.

Testene sammenligner vanlig tilbudsarbeid med tilbudsarbeid der VERIFIED brukes. For hver test dokumenterer prosjektet løsningene som ble sammenlignet, tilgjengelige opplysninger, mangler, faglige avklaringer og hvordan entreprenør og kunde brukte grunnlaget.

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

### Deltakersammensetning og kjønnsperspektiv

Forskningsspørsmål F4 gjelder hvordan entreprenør og kunde forstår og bruker beslutningsgrunnlaget. Slike funn avhenger av hvem som deltar, og deltakersammensetningen avgjør hvor bredt resultatene gjelder.

Prosjektet registrerer derfor kjønn som bakgrunnsvariabel for deltakerne i pilotene og vurderer ved analysen om forståelse og bruk av grunnlaget varierer. På kundesiden tas beslutninger om bolig ofte av flere personer i en husholdning, og rekrutteringen tar sikte på at kundesiden ikke representeres av bare én av dem. Kjønnsbalanse i prosjektgruppen og i pilotutvalget avklares med konsortiet ved oppstart.

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

Prosjektet sammenligner resultatene mot et definert sammenligningsgrunnlag. Noen resultater kan måles direkte i pilotene, som tidsbruk, forståelse og endring av valg. Andre virkninger, som framtidige utskiftninger, klimagassutslipp og livsløpskostnader, må beregnes ut fra dokumenterte forutsetninger.

| Effektområde | Målepunkt i piloten | Sammenligningsgrunnlag |
| --- | --- | --- |
| Klimagassutslipp | Beregnede klimagassutslipp per funksjonell enhet eller bygningsdel | Valgt løsning mot ett eller flere reelle alternativer |
| Ressursbruk | Materialmengde, forventet levetid og antall beregnede utskiftninger | Nyanskaffelse mot reparasjon, rehabilitering eller ombruk |
| Livsløpskostnad | Anskaffelse, vedlikehold og beregnede utskiftninger | Kostnad over avtalt analyseperiode |
| Beslutningseffekt | Om grunnlaget endrer, bekrefter eller ikke påvirker valget | Valg før og etter at sammenligningen vises |
| Brukbarhet | Forståelse, tidsbruk og behov for hjelp | Vanlig tilbudsarbeid mot bruk av VERIFIED |
| Dokumentasjonskvalitet | Andel opplysninger som mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen | Alternativene som sammenlignes |

### Feil og omarbeid

Prosjektet undersøker om bedre dokumentasjon kan redusere risikoen for feil og omarbeid. I prosjektperioden måles dokumentasjonsmangler og eventuelle observerbare avvik. Faktisk effekt på reklamasjoner og langsiktige byggskader kan ikke fastslås uten lengre oppfølging.

### Sirkulærøkonomi

VERIFIED behandler ombruk, reparasjon, rehabilitering og vedlikehold som reelle alternativer i sammenligningen. Pilotene måler restlevetid, redusert materialbruk og teknisk egnethet for disse alternativene der de er relevante.

### Do-not-harm

Prosjektet tester også mulige negative sideeffekter. Lavt klimagassutslipp skal ikke alene gi et alternativ høy vurdering dersom levetid, fuktrobusthet, vedlikeholdsbehov eller dokumentasjonskvalitet er svak.

Ombruk og reparasjon vurderes bare som positive alternativer når teknisk egnethet, restlevetid, transport, ansvar og faktisk materialbesparelse kan dokumenteres.

## V2 — Do-not-harm

### Del av modellen og piloteringen

Do-not-harm inngår i beslutningsmodellen og piloteringen. Hvert alternativ vurderes for mulige negative virkninger på levetid, teknisk risiko, dokumentasjonskvalitet, ressursbruk, helse og sikkerhet.

Modellen viser avveininger, usikkerhet og mulige negative konsekvenser ved hvert alternativ uten å utpeke ett som best. Levetid, dokumentasjonskvalitet og teknisk risiko inngår i vurderingen på lik linje med klimagassutslipp og pris. Svakheter ved ett kriterium er synlige selv når et annet er gunstig.

### Operative regler

Hver identifisert risiko knyttes til en modellregel, en reaksjon og en test i piloten.

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

Datastatus viser om en opplysning mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen. En usikker eller generell opplysning framstilles ikke med samme presisjon som en produktspesifikk, verifisert opplysning.

Leverandører kan supplere eller korrigere dokumentasjonen før vurderingen låses.

### Falsk presisjon og følsomhet

En poengsum kan virke sikrere enn datagrunnlaget er. Prosjektet viser derfor datakilder, datakvalitet, antakelser og begrensninger.

Prosjektet undersøker hvor følsomt resultatet er for sentrale vekter, forutsetninger og datamangler. Metode og terskler for følsomhetsvurderingen utformes sammen med forskningspartneren.

### Kjemikalier og sosiale forhold

Prosjektet undersøker hvilke kjemikalie-, helse- og sikkerhetsopplysninger som er tilgjengelige i EPD, FDV og annen produktdokumentasjon, og synliggjør når nødvendig informasjon mangler eller ligger utenfor modellen.

Prosjektet avklarer også hvilke sosiale og leverandørrelaterte forhold som kan dokumenteres gjennom tilgjengelige produkt- og prosjektdata. Forhold modellen ikke kan kontrollere, beskrives som utenfor vurderingsgrunnlaget og framstilles ikke som verifisert.

### Beslutningsansvar

VERIFIED gir beslutningsstøtte. Modellen skal ikke profilere personer eller ta kredittbeslutninger. Aktørene som bruker grunnlaget, har det faglige og kommersielle beslutningsansvaret.

## V3 — Økonomiske virkninger og bankrelevans

### Mekanismen

Den økonomiske virkningen går gjennom tre ledd. Et løsningsvalg som ser rimelig ut på anskaffelsespris, kan gi høyere kostnad over levetiden gjennom vedlikehold og utskiftninger. Når forskjellen er synlig før tilbudet låses, kan valget tas på et grunnlag som omfatter begge deler.

For entreprenøren ligger virkningen i tilbudsarbeidet: færre dokumentasjonsmangler og tydeligere alternativer, målt mot tiden grunnlaget koster å bruke. For kunden ligger den i at anskaffelseskostnad og beregnet livsløpskostnad kan sammenlignes i samme beslutning.

Pilotene måler disse leddene hver for seg. Størrelsen på virkningen er ikke fastsatt på forhånd — den er et av spørsmålene prosjektet undersøker.

### Virkninger for entreprenøren

For entreprenøren undersøker prosjektet om beslutningsgrunnlaget påvirker tidsbruk, tilbudskvalitet, dokumentasjonsmangler og observerbare avvik. Faktisk effekt på omarbeid og reklamasjoner kan bare vurderes dersom pilotperioden og datagrunnlaget gjør det mulig.

### Virkninger for kunden

For kunden viser modellen anskaffelseskostnad, beregnede livsløpskostnader, relevante tekniske forskjeller og usikkerhet ved alternativene. Prosjektet tester om kunden forstår denne informasjonen og hvordan den påvirker valget.

### Kunnskapsgrunnlag og FoU-hull

Kaza (2014) og Billio mfl. (2022) dokumenterer avgrensede sammenhenger mellom energieffektivitet og lavere misligholdsrisiko i boliglån i henholdsvis USA og Nederland. European Banking Authority beskriver behov for tydeligere og mer sammenlignbare data i markedet for grønne lån `[EBA_EU2023]`.

Den gjennomførte kunnskapskartleggingen fant avgrenset dokumentasjon om energieffektivitet og misligholdsrisiko. Sammenhengen mellom byggteknisk kvalitet, levetid, vedlikeholdsbehov og bankens risikovurdering står derfor som et FoU-spørsmål.

### Avgrenset bankpilot

Prosjektet undersøker om dokumentasjon av byggteknisk kvalitet, levetid og vedlikeholdsbehov kan struktureres som relevant tilleggsinformasjon for et avgrenset behov hos en bank.

Banken må før piloteringen definere hvilken informasjon den trenger, hvordan informasjonen skal vurderes, og hva som skal regnes som et nyttig resultat. Grunnlaget bygger bare på produkt-, prosjekt- og byggdokumentasjon. Det brukes ikke til personprofilering eller automatiske kredittbeslutninger.

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

## Endringslogg mot v0.6

| ID | Sted | Endring | Grunnlag |
| --- | --- | --- | --- |
| B-01 | V1, «Hovedbidrag» | 12.5 skrevet ut som sekundært bærekraftsmål med mekanisme og målepunkt, i stedet for betinget «kan også treffe … dersom» | F-21, besluttet av Lars 2026-08-05 |
| B-02 | V3, nytt avsnitt «Mekanismen» | Økonomisk mekanisme beskrevet kvalitativt i tre ledd, uten tall og uten lovet effektstørrelse | F-36, svarer på delpunktet «Økonomiske gevinster for bedriftene» i vurderingskriteriet Effekter |
| B-03 | K4, nytt avsnitt «Deltakersammensetning og kjønnsperspektiv» | Kjønn som bakgrunnsvariabel i pilotene, rekruttering på kundesiden, og kjønnsbalanse avklart med konsortiet | F-35, svarer på delpunktet «Kjønnsperspektiv ivaretatt» i vurderingskriteriet Kvalitet |
| B-04 | Hele teksten | Rytmepass på «skal»: modalverbet beholdt der det uttrykker en bindende regel eller framtidig modellatferd, og erstattet med presens der setningen beskriver prosjektets egen aktivitet | Planlagt v0.7-pass i handoff #46 |

### Uendret fra v0.6

Overskriften på V3 står uendret (F-28, besluttet 2026-08-05, forankret i godkjent arbeidsversjon fra 2026-07-25). Sammendraget beskriver fortsatt partnertyper uten navn (F-03, besluttet 2026-08-05: kun uformell interesse foreligger). Ingen prosentsats, kildestatus, metodebetegnelse eller testprotokoll er endret.

### Krever bekreftelse før innsending

- **B-03** binder en rekrutteringspraksis. Lars og konsortiet må bekrefte at den er gjennomførbar før den står i en innsendt søknad.
- Port A (SMB-definisjon og størrelse) er fortsatt uløst og krever offentlig originalkilde. Ingen andel eller prosentsats er brukt i teksten.
- Port C (forskningsdesign, testtyper, validering, følsomhetsterskler) krever faglig eier. Teksten beskriver derfor prosess og testområder, ikke metodebetegnelse eller protokoll.
- Port F (arbeidspakker, milepæler, budsjett, roller) er ikke skrevet i denne kandidaten og hentes fortsatt fra `v0.4`.
