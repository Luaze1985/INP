# VERIFIED – K3 forskning og sannhetsserum v0.6

**Status:** Intern kontrollkandidat for K3 og kildebruk

**Dato:** 2026-08-04

**Søknadskandidat:** `soknadstekst-samlet-kandidat-v0.6.md`

**Kildepass:** `../../sintef/kollegapakke/02-detaljert-arbeidsnotat.md`

**Språkport:** `../../sintef/internt/sprakport-v0.6.md`

## 1. Kontrollgrunnlag

K3 skal beskrive hva prosjektet skal utvikle, hvilken kunnskap arbeidet bygger
på, og hvilke spørsmål som krever forskning. Hver bærende påstand skal ha en
avgrenset bevisrolle. Prosjektmål og testterskler skal framstå som prosjektvalg.

Kildebruken følger denne rekkefølgen:

1. åpnet norsk primærkilde eller offisiell kilde for norske forhold;
2. åpnet internasjonal fagfellevurdert original for metode og generelle
   mekanismer;
3. åpnet EU- eller standardkilde for regelverksrammer;
4. leverandørdokumentasjon for positivt dokumenterte produktfunksjoner;
5. sekundæromtale som spor til original, uten bærende rolle.

KI-baserte søk og oppsummeringer inngår som kontrollspor. Originalen og den
relevante passasjen avgjør bruksstatus.

## 2. Prosjektets forskningsidé

VERIFIED skal utvikle og teste en forklarbar sammenligning av alternative
løsningsvalg i tilbudsfasen. Sammenligningen skal behandle pris, klima,
levetid, vedlikehold, teknisk kvalitet, ombruk, dokumentasjon og risiko.

Entreprenøren skal kunne kontrollere datagrunnlag, antakelser og vekting.
Kunden skal kunne forstå sentrale forskjeller og usikkerheter. Entreprenøren
og kunden beholder beslutningsansvaret.

FoU-arbeidet omfatter:

- kobling av data med ulike formater, enheter og dokumentasjonsnivåer;
- formålsavhengig behandling av datakvalitet;
- forklarbar vekting og synlige avveininger;
- håndtering av manglende og usikre data;
- sammenligning av metodevalg og følsomhet;
- empirisk måling av forståelse, tidsbruk og beslutningseffekt.

## 3. Kunnskap som kan brukes med avgrensning

### 3.1 Tilbudsfase og små entreprenører

Den nordiske rapporten om LCA- og BIM-praksis beskriver kapasitetsforskjeller
mellom større og mindre aktører. Kilden støtter behovet for en anvendbar
arbeidsform for mindre bedrifter `[Nordic2023]`.

Kilden dokumenterer ikke at alle små entreprenører mangler kompetanse eller
utelukkende vurderer pris. Prosjektet skal undersøke brukerforutsetningene i
pilotene.

### 3.2 Standarder og regelverk

NS-EN 16627 gir prosjektets hovedretning for vurdering av økonomisk ytelse på
byggnivå `[NS-EN16627]`. Standardstatusen er åpnet. Detaljerte metodekrav skal
kontrolleres mot standardteksten ved operasjonalisering.

EN 15978:2026 omfatter miljøprestasjon på byggnivå og har relevans for nybygg,
eksisterende bygg og rehabilitering `[EN15978-2026]`. Den åpnete kilden
dokumenterer versjonen og virkeområdet. Standardteksten er ikke registrert som
lest, og kilden brukes derfor ikke til detaljerte metodekrav eller generelle
effekttall.

Forordning (EU) 2024/3110 og forordning (EU) 2024/1781 etablerer rammer for
produktinformasjon og digitale produktpass `[CPR2024]` `[ESPR2024]`. Videre
produktkrav og tidsplaner skal knyttes til åpnete gjennomføringsdokumenter.

### 3.3 Datakvalitet

Edelen og Ingwersen beskriver datakvalitet som formålsavhengig og
flerdimensjonal `[Edelen2018]`. Kilden støtter synlig dokumentasjon av
datakvalitet og begrunnede vurderinger.

Kilden gir ikke grunnlag for et generelt forbud mot aggregering. VERIFIED skal
teste en prosjektregel der svake data og kritiske mangler forblir synlige ved
siden av et eventuelt samlet resultat.

### 3.4 Skader og teknisk risiko

Finans Norges offisielle statistikk for 2023 oppgir om lag ti vannskader per
time og erstatninger på rundt 5,1 milliarder kroner
`[FinansNorge2024VASK]`. Et årstall på 87 600 er en beregning fra
timefrekvensen. Kilden dokumenterer skadeomfang og erstatninger. Den
dokumenterer ingen virkning på bankenes risikomodeller.

### 3.5 Energi og finansiell risiko

Kaza mfl. analyserer amerikanske boliglån og rapporterer lavere
misligholdsodds for ENERGY STAR-sertifiserte boliger `[Kaza2014]`. Billio mfl.
analyserer nederlandske boliglån og finner en sammenheng mellom energikarakter
og misligholdssannsynlighet `[Billio2022]`.

Studiene gjelder ulike markeder, utvalg og modeller. De støtter en avgrenset
sammenheng mellom energi- eller miljøegenskaper og lånerisiko i de undersøkte
materialene. De dokumenterer ingen tilsvarende effekt av fuktrobusthet,
levetid, vedlikehold eller VERIFIEDs datamodell.

European Banking Authority beskriver fragmenterte markeder og foreslår en
frivillig EU-definisjon og merking for grønne lån `[EBA_EU2023]`. Dokumentet
gir finanspolitisk kontekst. Det etablerer ingen bindende VERIFIED-spesifikasjon
eller dokumentert bankeffekt.

### 3.6 Eksisterende verktøy

Gjennomgangen dokumenterer flere relevante funksjoner:

- SmartKalk kobler kalkyle, pris og klima i tilbudsarbeidet;
- Reduzer kobler anbudsarbeid, EPD-er og klimagassberegning;
- Concular dekker ombruk, materialpass og deler av garanti og kvalitetssikring;
- EC3 viser datakvalitet og usikkerhet i karbonberegninger `[EC3]`;
- One Click LCA kombinerer LCA og LCC;
- ORIS dekker material-, transport-, kostnads- og karbonvalg i infrastruktur.

Produktdokumentasjon kan støtte positive funksjonspåstander. Fravær av en
funksjon krever full og datert produktkontroll.

## 4. Avgrenset FoU-gap

Det undersøkte, ikke uttømmende materialet dokumenterer ingen løsning som
samler hele VERIFIED-kombinasjonen for norske små entreprenører i
tilbudsfasen. Kombinasjonen omfatter:

- klima og livsløpskostnad;
- levetid og vedlikehold;
- teknisk risiko og dokumentasjonskvalitet;
- synlig behandling av usikre og manglende data;
- forklarbar sammenligning før tilbudet låses;
- måling av faktisk beslutningspåvirkning.

Gapet gjelder kombinasjonen, brukerforutsetningen og den empiriske testingen.
LCA, LCC, karbonberegning, usikkerhetsvisning, ombruk og tilbudsstøtte finnes
allerede som separate eller delvis kombinerte funksjoner.

Kunnskapskartleggingen har ikke identifisert dokumentasjon for en direkte
sammenheng mellom byggteknisk holdbarhet, fukt, levetid og bankenes PD- eller
LGD-modeller. Formuleringen gjelder det undersøkte materialet per
3. august 2026. F5 behandler sammenhengen som et forskningsspørsmål.

## 5. FoU-spørsmål

| ID | Tema | Forskningsspørsmål | Primær test |
| --- | --- | --- | --- |
| F1 | Kvalitet, levetid og økonomi | Hvordan kan levetid, vedlikehold og teknisk kvalitet omsettes til sammenlignbare livsløpskostnader og avveies mot klima? | Sammenlign løsning, vedlikehold og utskifting over avtalt analyseperiode. |
| F2 | Data i tilbudsfasen | Kan produkt-, EPD-, FDV-, levetids- og prisdata kobles tidlig nok til praktisk tilbudsarbeid? | Mål datadekning, manuell behandling og tidsbruk. |
| F3 | Reparasjon, rehabilitering og ombruk | Hvordan kan alternative tiltak sammenlignes under dokumenterte forutsetninger for kostnad, klima, restlevetid og egnethet? | Sammenlign reelle alternativer med samme funksjonelle grunnlag. |
| F4 | Forståelse og beslutning | Hvordan forstår og bruker entreprenør og kunde grunnlaget, og hvordan påvirker det valget? | Registrer forståelse, bruk, tidsbruk og valg før og etter sammenligning. |
| F5 | Byggdata og bank | Kan byggtekniske data struktureres som relevant tilleggsinformasjon for ett definert bankbehov? | Banken definerer behovet før pilot; prosjektet måler om dokumentasjonen svarer på det. |
| F6 | Sporbarhet og overføring | Hvordan kan dataflyt og grensesnitt utformes slik at vurderingen kan kontrolleres og overføres til en ny produktkategori? | Kontroller proveniens, enheter, regler og gjenbruk i en ny kategori. |

## 6. Metodekrav

### 6.1 Datatilstander

Hvert relevant datapunkt skal ha én av fire tilstander:

- mangler;
- generell eller sekundær verdi;
- estimert verdi;
- produktspesifikk og kontrollert verdi.

Kilde, dato, enhet, systemgrense og dokumentasjonsnivå skal følge datapunktet.
Kritiske mangler skal være synlige i resultatet.

### 6.2 Teknisk egnethet

Pilotprotokollen skal definere minste informasjonsgrunnlag og ansvarlig faglig
rolle. En løsning med uavklart egnethet skal få synlig uavklart status.

### 6.3 Valg av flerkriteriemetode

Aktuelle metoder skal sammenlignes etter:

- forklarbarhet;
- datakrav;
- håndtering av manglende data;
- følsomhet for vekter og antakelser;
- stabilitet når alternativer legges til eller tas ut;
- brukerforståelse.

Metodefordelinger fra litteraturgjennomganger og direkte dokumentasjon av
ranginversjon mangler ferdig originalkontroll. Kandidaten bruker derfor ingen
prosentsatser eller kildebåret konklusjon om ranginversjon. Stabilitet inngår
som en prosjekttest.

### 6.4 Følsomhet og usikkerhet

Prosjektet skal teste endrede vekter, alternative forutsetninger og manglende
data. Resultatet skal vise når små endringer påvirker rangering eller
konklusjon.

### 6.5 Pilot og måling

Hvert FoU-spørsmål skal kobles til datakilde, målepunkt,
sammenligningsgrunnlag og vurderingskriterium før pilotstart. Pilotene skal
sammenligne vanlig tilbudsarbeid med bruk av VERIFIED.

## 7. Prosjektmål og hypoteser

Tallfestede mål krever prosjektbeslutning og metodebegrunnelse. Følgende tall
er ikke dokumentert ekstern empiri i kildepasset:

- 30 prosent påvirkede beslutningstilfeller;
- 70 prosent tidsreduksjon;
- 85 prosent datadekning;
- null tilfeller av ranginversjon;
- 80 prosent brukerforståelse;
- 20 prosent utviklingsinnsats;
- 10 000 simuleringer.

Tall kan brukes som foreløpige testterskler når ansvar, målemetode og
begrunnelse er godkjent. Søknadskandidat `v0.6` bruker kvalitative målekrav der
en slik beslutning mangler.

## 8. Kilder og påstander som holdes ute

Source Guard forvalter 11 sperreposter for usikre identiteter, gamle aliaser og
feil kobling mellom kilde og påstand. Identitetene står i kildepasset og i
`governance/source-blocklist.json`.

K3 v0.6 bruker ingen sperret identitet som belegg. Følgende påstander holdes
ute til original og presis passasje er kontrollert:

- et universelt 70-prosenttall for utslipp i A1-A3;
- et generelt 20-prosentkutt uten merkostnad;
- presise tall for driftsmargin og byggekostnadsforskjell;
- et milliardbeløp for konfliktkostnader;
- metodeprosenter fra en uåpnet eller omstridt fulltekst;
- en direkte kobling mellom bygningsteknisk kvalitet og bankenes PD/LGD;
- absolutte negative påstander om konkurrentfunksjoner.

## 9. Åpne originalkontroller

Kildepasset beskriver den fulle listen. K3 påvirkes særlig av:

1. identitetsavstemming mellom klimafotavtrykk, fire referansebygg og samlet
   sektorberegning;
2. original og systemgrense for eventuelle A1-A3-andeler;
3. original og kostnadsdefinisjon for utslippskutt uten merkostnad;
4. relevante passasjer for MCDA-fordeling, pedigree-usikkerhet og
   mulighetsromvisualisering;
5. full produktkontroll for sentrale konkurrenter som mangler i dagens utvalg;
6. original dokumentasjon for presise bransje- og prosjekttall.

Disse kontrollene kan styrke senere versjoner. Søknadskandidat `v0.6` bruker
avgrenset ordlyd som ikke er avhengig av de åpne originalene.

## 10. Samsvar med søknadskandidat v0.6

| Tema | Sannhetsserum | Søknadskandidat v0.6 |
| --- | --- | --- |
| Prosjektets rolle | Forklarbar sammenligning; aktørene har beslutningsansvar | Samme rolle i sammendrag, K1 og K3 |
| Nyhetsverdi | Avgrenset kombinasjon og empirisk testing | Samme gapformulering i K2 |
| Datakvalitet | Formålsavhengig og synlig | Datatilstander og dokumentasjonstillit i K4 |
| Metode | Sammenligning, følsomhet og stabilitet | Metodevalg og pilotmåling i K4 |
| Klima | Konkrete alternativer og definert systemgrense | Ingen generell prosentsats i V1 |
| Finans | Avgrenset forskning og ett definert bankbehov | Hypotese og avgrenset pilot i V3 |
| Konkurrenter | Positivt dokumenterte funksjoner og datert utvalg | Forsiktig, ikke uttømmende gap i K2 |
| Sperrede kilder | Ingen bærende bruk | Null Source Guard-treff som mål |

## 11. Kontrollstatus

- Kildepass for alle 60 registrerte kilder: opprettet.
- Nye kandidater og sperreposter: registrert i kildepasset.
- Språkport: opprettet før `v0.6`.
- Absolutte forsknings- og markedsgap: avgrenset.
- Prosjektmål og ekstern empiri: skilt.
- K3 og samlet søknadskandidat: samstemt på FoU-spørsmål og metode.
- Innsendingsklar status: krever full innflettingskontroll og Lars' godkjenning.

## Endringslogg

- 2026-08-04: Opprettet som ny kontrollkandidat fra kildepasset og
  søknadskandidat `v0.6`. Ingen tekst er kopiert mekanisk fra K3-sannhetsserum
  `v0.5`.
