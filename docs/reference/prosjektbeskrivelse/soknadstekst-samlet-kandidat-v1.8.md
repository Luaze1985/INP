# VERIFIED — søknadstekst v1.8 etter portalmalen

> Dato: 2026-09-16. Status: arbeidskandidat, ikke innsendingsklar. Grunnlag: v1.7 IF-only, forbedringer fra kvalitetsutkast v4.0 og beslutninger fra Lars 2026-09-15/16.

> Rød skrift = innhold som ikke fantes i v1.7 (nye avsnitt, påstander, tall og plassholdere). Tekst fra v1.7 står i svart også når den er flyttet eller forkortet. [FYLLES INN] markerer opplysninger som må bekreftes.

> Overskriftene følger portalmalen i innsendingspakker/v2.0. Feltlisten er et ikke manuelt verifisert video-uttrekk. Tegntelling per felt står bakerst.

## Tittel og tema

### PROSJEKTTITTEL PÅ NORSK

<span style="color:red">VERIFIED – etterprøvbar sammenligning av løsningsvalg i tilbudsfasen i bygg</span>

### PROSJEKTTITTEL PÅ ENGELSK

<span style="color:red">VERIFIED – verifiable comparison of building solutions at the tender stage</span>

### KORTNAVN

VERIFIED

## Mål

### Hovedmål

Hovedmålet er å utvikle og prøve et forskningsbasert metodegrunnlag for å sammenligne alternative løsninger i tilbudsfasen. Metoden skal vise både forskjeller mellom alternativene og kvaliteten og usikkerheten i datagrunnlaget. <span style="color:red">Den skal også avgjøre om en sammenligning er robust, betinget eller utilstrekkelig belyst, og vise hvilke data og forutsetninger som styrer resultatet.</span>

### Delmål

Delmålene er å avgrense nødvendige data, utvikle en sporbar sammenligningsmetode, prøve hvordan forklaring og usikkerhet forstås, og dokumentere begrensningene som må være synlige før en modell kan fryses.

<span style="color:red">Forventede resultater:</span>

- <span style="color:red">D1: Forskningsprotokoll, caseutvalg og referansestandard (AP1).</span>
- <span style="color:red">D2: Sporbar datamodell og harmoniseringsregler med kontrollerte datavarianter (AP2).</span>
- <span style="color:red">D3: Regelsett for når alternativer kan sammenlignes, med teknisk egnethet, usikkerhet og vekting (AP3).</span>
- <span style="color:red">D4: Reproduserbar forskningsimplementasjon (AP4).</span>
- <span style="color:red">D5: Empirisk prøvd forskningsversjon, testet på caser som ikke er brukt i utviklingen og mot dagens praksis, med dokumentert gyldighetsområde (AP5).</span>

## Sammendrag

### Skriv et sammendrag av prosjektet

VERIFIED skal utvikle en forskningsbasert metode for å sammenligne alternative løsninger i tilbudsfasen i små og mellomstore byggeprosjekter. Metoden skal gjøre det tydelig hva som er kjent, hva som er usikkert, og hvordan pris, klima, levetid, vedlikehold, teknisk kvalitet, dokumentasjon og risiko kan vurderes samlet. <span style="color:red">Metoden skal klassifisere en sammenligning som robust, betinget eller utilstrekkelig belyst, og vise hvilken tilleggsinformasjon som betyr mest.</span> Resultatet er ikke en automatisk anbefaling. Entreprenør og kunde beholder ansvaret for valget.

<span style="color:red">Prosjektet bruker 6–8 reelle norske tilbudscaser i to løsningskategorier. Opplysninger fjernes eller endres systematisk for å finne når konklusjonen endrer seg, og regelsettet prøves til slutt på caser som ikke er brukt i utviklingen. Vi Bygger Sammen AS leder prosjektet med D Takst AS, Byggmester Espeland AS og Norsk Byggtjeneste AS som samarbeidspartnere og SINTEF som planlagt FoU-leverandør.</span>

Prosjektet er avgrenset til industriell forskning. Det skal etablere metodegrunnlag, datamodell og usikkerhetsmodell før eventuell videre utvikling vurderes i et eget senere løp.

## Soliditet

### Kunnskapsbehov og mål for prosjektet

I tilbudsfasen priser entreprenøren arbeidet, foreslår alternative løsninger og forklarer dem for kunden. Pris er ofte lett å sammenligne. Forskjeller i levetid, vedlikehold, klima, teknisk egnethet, dokumentasjon og risiko kan være vanskeligere å se samlet. VERIFIED skal undersøke hvordan slike avveininger kan gjøres synlige uten at usikkerheten skjules.

Relevante opplysninger kan ligge i produktdata, FDV-dokumentasjon, miljødeklarasjoner, levetidsvurderinger og prisdata. Kildene kan ha ulike formater, detaljeringsnivå og bruksbegrensninger.

ISO 14040 gir et rammeverk for livsløpsvurdering, NS 3720 beskriver klimagassberegninger for bygninger, og ISO 15686-5 omhandler livsløpskostnader [2–4]. VERIFIED undersøker hvordan opplysninger med ulik dokumentasjonsstyrke kan brukes tidlig i tilbudsfasen, hvordan avveininger kan forklares, og hvordan usikkerhet kan påvirke sammenligningen. Det er en avgrenset forskningsoppgave, ikke en påstand om at standardene mangler dette.

<span style="color:red">Kommersielle verktøy dekker allerede deler av behovet. Ifølge leverandørenes egne beskrivelser sammenligner One Click LCA kostnad og miljøpåvirkning mellom scenarier, og Reduzer tilbyr tidligfaseberegning og sammenligning av design og EPD-er [5, 6]. Nyhetsverdien ligger derfor ikke i å kombinere kostnad og klima. Kunnskapshullet er hvor grensen går mellom tilstrekkelig og utilstrekkelig informasjon for en forsvarlig sammenligning, hvordan ulike data og faglig skjønn kan representeres uten falsk sikkerhet, og hvordan grensen kan forklares for ikke-spesialister.</span> <span style="color:red">**[FYLLES INN: nærmeste forskning]**</span>

<span style="color:red">Hovedhypotese: Det er mulig å definere en etterprøvbar grense for når alternative løsninger kan sammenlignes, slik at færre konklusjoner framstår som sikrere enn datagrunnlaget tillater, samtidig som en praktisk andel av tilbudssituasjonene fortsatt får et nyttig beslutningsgrunnlag.</span>

Forskningsspørsmål:

- F1: <span style="color:red">Hvilke funksjons-, tilstands- og kildedata må være på plass før en sammenligning kan regnes som robust?</span>
- F2: <span style="color:red">Hvordan kan data fra ulike kilder gjøres sammenlignbare uten å skjule forskjeller i enhet, systemgrense, tidspunkt eller dokumentasjonsstyrke?</span>
- F3: Hvordan kan reparasjon, rehabilitering, ombruk og nyanskaffelse sammenlignes uten at estimert levetid eller faglig skjønn framstår som målte fakta?
- F4: <span style="color:red">Hvordan kan grensen for sammenlignbarhet forklares slik at fagperson og tilbudsmottaker forstår hva som er sikkert, betinget og uavklart?</span>
- F5: Hvordan kan modellens sporbarhet, datamangel og følsomhet dokumenteres slik at <span style="color:red">reglene kan etterprøves på caser som ikke er brukt til å utvikle dem?</span>

### FoU-metoder og -aktiviteter

<span style="color:red">Forskningsløypen følger AP1–AP5, med AP6 for utnyttelse og AP7 for styring.</span> Først fastsettes protokoll, datakvalitet og avgrensninger. Deretter prøves harmoniserings- og måleregler på avgrensede tilbudssituasjoner. Til slutt undersøkes hvordan vekting og usikkerhet påvirker resultatet, før modellen enten fryses med synlige begrensninger eller sendes til omarbeiding.

For hver opplysning skal metoden kunne vise kilde, tidspunkt, enhet, produktnivå og dokumentasjonsstatus. Manglende, generelle, estimerte og verifiserte opplysninger skal ikke blandes sammen. Teknisk egnethet er en faglig port; modellen erstatter ikke entreprenørens eller fagpersonens ansvar.

<span style="color:red">Casedesign. Prosjektet bruker to løsningskategorier og 6–8 godt dokumenterte norske tilbudscaser med 2–3 faglig relevante alternativer hver. Kategoriene velges i AP1 etter tre kriterier: ulike usikkerhets- og dataproblemer, tilgang til reelle caser og data hos partnerne, og gjentakende økonomisk relevans. Vinduer og utvendig kledning er foreløpige kandidater. 4–5 caser brukes til å utvikle regelsettet, og 2–3 holdes utenfor til reglene er låst.</span>

<span style="color:red">Kontrollerte datamangler. Fra et best mulig dokumentert case fjernes eller endres én informasjonskomponent om gangen, for eksempel tilstand, restlevetid, vedlikehold, EPD, produktidentifikasjon, pris eller systemgrense. Det undersøkes om metoden endrer status riktig, hvilke feil som oppstår, og hvilken informasjon som har størst beslutningsverdi (F1–F3).</span>

<span style="color:red">Referansestandard. Riktig konklusjon defineres som en dokumentert faglig vurdering under best tilgjengelige informasjon, ikke som én objektiv fasit. Kritiske vurderinger gjøres av minst to uavhengige fagpersoner, og uenighet registreres. Restlevetid og andre usikre størrelser angis som intervall eller scenario. En konklusjonsfeil er en konklusjon som framstår sikrere eller annerledes enn referansen tillater.</span>

<span style="color:red">Sammenligning med dagens praksis. Casene som holdes utenfor, vurderes både slik en erfaren tilbudsansvarlig gjør i dag og med VERIFIED. Antall feilaktig sikre konklusjoner og oversette datamangler sammenlignes (F5).</span>

<span style="color:red">Brukertester. 8–12 fagpersoner fra flere SMB-er og 8–15 tilbudsmottakere deltar i strukturerte tester (F4). Primære utfall er kritiske datamangler som oppdages, feilaktig sikre konklusjoner og korrekt forståelse av forbehold; tidsbruk er sekundært. Med dette utvalget er analysen deskriptiv og kombineres med systematisk kvalitativ feilanalyse. Studien skal ikke brukes til å hevde representativ effekt for næringen.</span>

<span style="color:red">Suksesskriterier. Regelsettet skal klassifisere minst</span> <span style="color:red">**[FYLLES INN: andel]**</span> <span style="color:red">av kontrollvariantene riktig mot referansen, og gi færre feilaktig sikre konklusjoner enn dagens praksis i casene som holdes utenfor.</span> Hvis porten ikke nås, skal kunnskapshull og behov for omarbeiding dokumenteres; det skal ikke hevdes at modellen er validert.

Metoden utvikles trinnvis og dokumenteres slik at faglige valg, kildegrunnlag og begrensninger kan ettergås. Praktisk beslutnings- og kommersiell effekt er ikke et akseptkriterium for modellfrys. AP1 skal likevel fastsette hvordan slike effekter kan måles etterpå, slik at en senere pilot ikke blander sammen opplevd nytte, teknisk kvalitet og økonomisk gevinst.

Måleplan. AP1 gjør følgende måleplan til del av forskningsprotokollen. Den viser hva som skal observeres, ikke hvilke resultater prosjektet vil oppnå. VIBS er ansvarlig for samlet målelogg; hver partner bekrefter bare egne data.

- Tilbudsoppgave og datagrunnlag: avgrenset oppgave, alternativer, kilder, mangler, lisensstatus og tidspunkt før bruk av modellen (AP1). Port: uegnede eller ulovlige data tas ut før AP2.
- Arbeidsflyt og kvalitet: tidslogg for oppslag, sammenstilling, rettelser og spørsmål; synlige mangler og forklaringssteg i samme type oppgave (<span style="color:red">baseline i AP1, måling i AP5</span>). Port: bare endring uten skjult kvalitetstap går videre som prosesshypotese.
- Forståelse og beslutningsgrunnlag: strukturert test av korrekt gjenfortelling av alternativer, forbehold og usikkerhet; ikke bare tilfredshet (<span style="color:red">AP5</span>). Port: resultatet brukes bare dersom forbehold og begrensninger fortsatt forstås.
- Økonomisk verdi hos bruker: dokumentert timekostnad og eventuell reell kostnadsreduksjon eller inntektsgivende bruk av frigjort tid, først etter modellfrys i separat pilot. Port: ingen økonomisk gevinst uten identifisert budsjetteier og godkjent beregning.
- Betaling og dekningsbidrag: bestilling, faktura eller fornyelse; data-, oppstarts-, drifts- og brukerstøttekostnad per kunde, først etter modellfrys i separat kommersielt løp. Port: ingen lønnsomhetspåstand uten faktiske inntekts- og kostnadsdata.

### Etiske problemstillinger

Prosjektet skal samle inn minst mulig persondata. Kommersielt sensitive opplysninger, datarettigheter, lagring, tilgang og eventuell anonymisering avgrenses i AP1 før analyse. VERIFIED skal ikke bruke personprofilering eller automatisk beslutning. Usikkerhet, faglig dissens og datamangler skal være synlige i beslutningsgrunnlaget.

<span style="color:red">Deltakere i brukertester får informasjon om formål, frivillighet, lagring og sletting, og samtykker før deltakelse. Lisensierte produktdata og tilbudsdata brukes bare etter dokumentert bruksrett. En datahåndteringsplan utarbeides i AP1. Teknisk egnethet og faglig ansvar forblir hos kvalifisert fagperson; VERIFIED er beslutningsstøtte, ikke sertifisering.</span> <span style="color:red">**[FYLLES INN: etikkansvarlig]**</span>

### Kjønnsperspektiver

<span style="color:red">Kjønn er ikke en variabel i metodens beregninger. Kjønnsperspektivet er likevel relevant for brukertestene, fordi sammensetningen av utvalget kan påvirke hvordan forklaringer og forbehold forstås. Prosjektet rekrutterer fagpersoner og tilbudsmottakere med variert bakgrunn, rapporterer kjønnssammensetningen og undersøker om forståelsesmønstrene varierer systematisk. Er utvalget for lite til å si noe om dette, rapporteres det som en begrensning.</span>

## Originalitet

### Innovasjonen

<span style="color:red">Innovasjonen er en beslutningsmetode for tilbudsfasen som først avgjør om tilgjengelige data er tilstrekkelige til at alternativene kan sammenlignes forsvarlig, og deretter viser konsekvenser, forutsetninger og hva som kan endre konklusjonen.</span>

<span style="color:red">Fra dagens arbeidsflyt til VERIFIED:</span>

- <span style="color:red">Data hentes manuelt fra flere kilder → hver opplysning knyttes til kilde, versjon, enhet, systemgrense og dokumentasjonsstatus.</span>
- <span style="color:red">Fagpersonen må selv avgjøre om alternativene er sammenlignbare → teknisk egnethet og funksjon prøves før økonomi og klima sammenlignes.</span>
- <span style="color:red">Mangler kan skjules i antakelser eller standardverdier → mangler vises og kan stoppe eller betinge en rangering.</span>
- <span style="color:red">Resultatet framstår lett som én sikker anbefaling → resultatet klassifiseres som robust, betinget eller utilstrekkelig belyst.</span>
- <span style="color:red">Det er uklart hvilken informasjon som bør hentes først → metoden viser hvilken tilleggsinformasjon som betyr mest.</span>

VERIFIED skal undersøke en avgrenset, forklarbar metode for å angi nødvendige data, koble opplysninger uten å gjøre mangler til sikre verdier, synliggjøre vekting og usikkerhet, og prøve om framstillingen er forståelig i en avgrenset tilbudssituasjon. Nyhetsverdien ligger ikke i å hevde én universell score eller å automatisere fagansvar.

<span style="color:red">Eksisterende løsninger. LCA, LCC og flerkriterieanalyse er etablerte fagområder, og leverandørene av One Click LCA og Reduzer beskriver sammenligning av kostnad, klima og tidlige designalternativer [5, 6]. VERIFIED skal ikke konkurrere på beregning, men på å vise når en sammenligning kan forsvares. Blant prosjekter som er tildelt støtte i samme utlysning, retter ByggSjekk (EG HOLTE AS) seg etter tittelen mot KI-basert kvalitetskontroll i boligbygging [7]. VERIFIED gjelder valget mellom løsningsalternativer før kontrakt, i tilbudsfasen.</span>

<span style="color:red">Insentiveffekt. Uten støtte kan VIBS utvikle en enklere tilbudsfunksjon basert på kjent metode og manuelt arbeid, men ikke finansiere systematisk kunnskapsstatus, kontrollerte datamangler, uavhengig referansestandard, prøving på caser holdt utenfor og innkjøpt FoU. Støtten utløser aktiviteter med reell kunnskapsrisiko som kan avkrefte eller endre den kommersielle hypotesen. Ingen prosjektaktiviteter er startet før innsending.</span> <span style="color:red">**[FYLLES INN: styrebekreftelse]**</span>

> Insentiveffekt har ikke eget tekstfelt i portaluttrekket. Flyttes hvis portalen spør om det et annet sted.

### Behov og markedsmuligheter

SSB registrerte 68 359 virksomheter i bygge- og anleggsnæringen per 1. januar 2026; 91,2 prosent hadde færre enn ti ansatte når virksomheter uten ansatte regnes med [1]. Prosjektet legger derfor til grunn at beslutningsgrunnlaget må være mulig å bruke uten å forutsette spesialistkapasitet hos små entreprenører. Dette er en brukerforutsetning som skal prøves, ikke en slutning fra SSB-tallene alene.

<span style="color:red">Behovseiere er tilbudsansvarlige, prosjektledere og kalkulatører i små og mellomstore entreprenørbedrifter, og tilbudsmottakere som skal forstå alternativene. Budsjetteier antas å være daglig leder eller tilbudsansvarlig med resultatansvar. Behovet er drøftet med partnerne i partnerdialog i 2026; dette er innspill, ikke dokumentert effekt. En systematisk behovskartlegging gjennomføres i AP1. Markedsmodellen bygges nedenfra i AP1: relevante virksomheter, andel som sammenligner alternativer, tilbud per år og pris. Partnerne har kommersiell interesse gjennom egne tjenester, se Verdiskapingspotensial. Prosjektet er avgrenset til norske forhold; internasjonale muligheter vurderes først etter modellfrys.</span>

## Referanseliste

### Referanseliste

[1] Statistisk sentralbyrå (2026). Bedrifter, etter størrelse og næring, 1. januar 2026. Statistikkbanken, tabell 10309.

[2] ISO (2006, bekreftet 2022). ISO 14040:2006 Environmental management – Life cycle assessment – Principles and framework, med Amendment 1:2020.

[3] Standard Norge (2018). NS 3720:2018 Metode for klimagassberegninger for bygninger.

[4] ISO (2017, bekreftet 2024). ISO 15686-5:2017 Buildings and constructed assets – Service life planning – Part 5: Life-cycle costing.

<span style="color:red">[5] One Click LCA. Leverandørens beskrivelse av funksjon for livsløpskostnader og karbon. Lest 10. august 2026.</span>

<span style="color:red">[6] Reduzer. Leverandørens beskrivelse av tidligfaseberegning, EPD-bibliotek og sammenligning av design og EPD-er. Lest 10. august 2026.</span>

<span style="color:red">[7] Norges forskningsråd (2026). Innovasjonsprosjekt i næringslivet: Industri og tjenestenæringer 2026. Utlysning med oversikt over tildelte prosjekter. Lest 27. juni 2026.</span>

## Potensial

### Samfunnseffekter

VERIFIED skal undersøke om et tydeligere sammenligningsgrunnlag kan gjøre det mulig å vurdere nyanskaffelse, reparasjon, rehabilitering, ombruk og utsatt utskifting på en mer sporbar måte. Klima, materialmengde, levetid og livsløpskostnad kan bare beregnes eller estimeres innen en avtalt systemgrense og med synlige forutsetninger. Prosjektet oppgir ingen generell klimaeffekt eller prosentsats.

Klima og ressursbruk: beregnet klima- og materialkonsekvens innen valgt systemgrense, for avgrensede alternativer i samme tilbudsoppgave. Levetid og vedlikehold: dokumentert, estimert eller faglig vurdert informasjon holdes fra hverandre. Brukbarhet og dokumentasjon: tidsbruk, forståelse og synlige datamangler kan måles.

<span style="color:red">Effekten beregnes nedenfra for hvert case: forskjell i materialbruk, klima, kostnad og vedlikehold mellom alternativer innen samme funksjon og systemgrense. Metoden gjør reparasjon, rehabilitering og ombruk mulig å sammenligne med nyanskaffelse på samme grunnlag, i tråd med utlysningens vekt på ombruk og reparasjon. Realisert effekt kan først anslås når faktiske valg observeres etter prosjektet.</span>

Et lavt beregnet klimaavtrykk er ikke tilstrekkelig dersom løsningen har svak teknisk egnethet, kort eller usikker levetid, stort vedlikeholdsbehov eller mangelfull dokumentasjon. Relevante forhold knyttet til kjemikalier, sosiale forhold, transport, ansvar og faktisk materialbesparelse skal avgrenses i protokollen. Uavklarte forhold skal vises som uavklarte, ikke regnes som positive effekter.

Byggevareprodusenten kan få vite hvilke produktopplysninger entreprenøren og tilbudsmottakeren mangler eller misforstår. Dataaktørene kan se hvor produktidentifikatorer, dokumenter og datafelt ikke lar seg koble sammen. Denne kunnskapen kan brukes til å rette mangler og gjøre produktinformasjonen enklere å finne og bruke.

<span style="color:red">For FoU-miljøer gir prosjektet et empirisk prøvd eksempel på hvordan sammenlignbarhet kan behandles under ufullstendige data, publisert med åpen tilgang.</span>

### FNs bærekraftsmål

<span style="color:red">Hovedbidraget er til delmål 12.2 om bærekraftig forvaltning og effektiv bruk av naturressurser, og delmål 12.5 om å redusere avfall gjennom forebygging, reduksjon, materialgjenvinning og ombruk.</span>

<span style="color:red">Årsakskjeden er: et sporbart sammenligningsgrunnlag i tilbudsfasen gjør at reparasjon, rehabilitering, ombruk og utsatt utskifting kan vurderes på like vilkår med nyanskaffelse; løsninger med lavere materialbruk kan da velges der det er teknisk forsvarlig; det gir mindre materialforbruk og avfall. Prosjektet beregner forskjell i materialmengde og klimagassutslipp mellom alternativene i hvert case, men påstår ingen nasjonal effekt før faktiske valg er fulgt opp. Lav klimabelastning skal aldri alene definere beste valg; teknisk egnethet, levetid og dokumentasjon må inngå.</span> <span style="color:red">**[FYLLES INN: FN-indikator]**</span>

### Verdiskapingspotensial

Prosjektet skal gi et tydeligere grunnlag for å undersøke forskjeller mellom alternative løsninger. Det kan gjøre det lettere å se når en billig løsning på kort sikt har svak dokumentasjon eller andre avveininger som bør diskuteres.

For entreprenøren skal prosjektet måle tiden som brukes på oppslag, sammenstilling, rettelser og spørsmål før og etter bruk av VERIFIED. Frigjort tid skal verdsettes med bedriftens faktiske timekostnad og bare regnes som økonomisk verdi når den kan brukes til flere tilbud, annet inntektsgivende arbeid eller en reell kostnadsreduksjon. Målingen skal samtidig kontrollere at dokumentasjonskvaliteten og forståeligheten ikke svekkes.

Tilbudsmottakeren skal få se hva alternativene koster, hvilke egenskaper som skiller dem, hvilket vedlikehold de krever, hvilke forutsetninger som gjelder, og hvor opplysningene kommer fra. Dette kan gjøre det lettere å velge og redusere misforståelser og nye avklaringsrunder. Prosjektet skal måle om tilbudsmottakeren faktisk forstår innholdet bedre, ikke bare om presentasjonen oppleves som god.

<span style="color:red">Etter et vellykket prosjekt er det planlagte kommersielle produktet en VERIFIED-modul i VIBS som hjelper entreprenøren å dokumentere og forklare løsningsvalg. Mulige prismodeller er prosjektlisens eller abonnement, med betalt oppstart.</span> Dette forutsetter at VIBS har avtalte rettigheter til å bruke resultatene, at en identifisert kjøper vil betale for den målte forbedringen, og at betalingen overstiger kostnadene ved data, oppstart, drift og støtte. En lønnsom og gjentakbar tjeneste forutsetter også at samme metode kan brukes hos flere kunder uten tilsvarende vekst i manuelt arbeid.

<span style="color:red">Gevinst for samarbeidspartnerne, beskrevet uten beløp til rolle og budsjett er bekreftet:</span>

- <span style="color:red">D Takst AS kan få nye eller bedre oppdrag om tilstand og restlevetid ved å bruke dokumenterte vurderingsregler.</span>
- <span style="color:red">Byggmester Espeland AS kan bruke mindre tid på oppslag og avklaringer og gi tydeligere tilbud, uten at kvaliteten svekkes.</span>
- <span style="color:red">Norsk Byggtjeneste AS kan få oversikt over hvilke produktdata som mangler, og bruke læringen i datakvalitets- og datatjenester.</span>

Eventuelle besparelser eller nye inntekter hos partnerne må dokumenteres separat og skal ikke regnes som VIBS' inntekt.

<span style="color:red">Illustrativt regneeksempel for VIBS, år 3 etter kommersiell lansering. Tallene bygger på VIBS' egne forutsetninger og er ikke en prognose:</span>

- <span style="color:red">Lavt: 25 SMB-kunder og 2 større kunder; inntekt 1,05 MNOK; dekningsbidrag 0,49 MNOK; resultat etter faste kostnader −2,01 MNOK.</span>
- <span style="color:red">Basis: 100 SMB-kunder og 8 større kunder; inntekt 6,40 MNOK; dekningsbidrag 4,80 MNOK; resultat 0,80 MNOK.</span>
- <span style="color:red">Høyt: 300 SMB-kunder og 20 større kunder; inntekt 24,90 MNOK; dekningsbidrag 21,50 MNOK; resultat 13,50 MNOK.</span>

<span style="color:red">Basisscenariet forutsetter at flere produktkategorier bruker samme kjerne, at datatilgang er avtalt og at kundeoppstart er standardisert. Høyt scenario er ikke forventet utfall.</span>

<span style="color:red">Prosjektkostnaden er 16,0 MNOK. Etter prosjektet kreves investering i produktutvikling, datatilgang og salg før inntekter kan oppnås.</span> <span style="color:red">**[FYLLES INN: investering etter prosjektet]**</span>

Den økonomiske hypotesen skal vurderes som seks adskilte ledd. Et resultat i ett ledd er ikke bevis for neste ledd.

- Forskningsresultat: en versjonert og etterprøvbar modell med synlige kilder, datakvalitet og usikkerhet. Ikke tilstrekkelig alene: at modellen gir bruker- eller økonomisk nytte.
- Tilbudsprosess: endring i tidsbruk, manuelle oppslag, dokumentasjonsmangler, rettelser eller forklaringssteg i en avgrenset tilbudsoppgave. Ikke tilstrekkelig alene: at forbedringen er verdifull nok til å betale for.
- Kundeverdi: at en identifisert budsjetteier kan knytte den målte endringen til en kostnad, risiko eller bedre beslutning. Ikke tilstrekkelig alene: at aktøren vil kjøpe eller fornye en tjeneste.
- Betalingssignal: betalt pilot, bestilling eller fornyelse fra en bestemt juridisk kjøper. Ikke tilstrekkelig alene: at inntekten dekker kundespesifikke kostnader.
- Dekningsbidrag: fakturert inntekt overstiger dokumenterte kostnader til data, oppstart, drift og støtte per kunde. Ikke tilstrekkelig alene: at løsningen kan gjentas effektivt.
- Skalerbarhet: nye kunder eller produktkategorier kan tas inn uten tilsvarende vekst i onboarding-, integrasjons- og supportarbeid. Ikke tilstrekkelig alene: at markedet eller samlet lønnsomhet er dokumentert.

## Kunnskapsdeling og utnyttelse

### Realiseringsplan for verdiskaping

<span style="color:red">Resultater brukes underveis: datamangler som avdekkes i AP2, meldes til dataaktørene, og partnerne prøver regelsettet i egne tilbudssituasjoner i AP5.</span> Før kommersialisering kan vurderes, skal VIBS fastsette et sammenligningsgrunnlag for tilbudsoppgaven og føre tids-, kostnads- og kvalitetsdata.

<span style="color:red">Etter forskningsfrys tas en kommersiell beslutning i AP6. Videre pilot startes bare dersom kjøper, betalingssignal, dekningsbidrag, rettigheter, finansiering og plan for skalering er troverdige. Forretningsmodellen er lisens eller abonnement med betalt oppstart.</span>

<span style="color:red">Prinsipper for rettigheter: VIBS' plattform og eksisterende kode er VIBS' bakgrunn; partnernes eksisterende data og metoder er deres bakgrunn; VERIFIED-regelsettet eies etter faktisk bidrag, med rett for VIBS til kommersialisering etter avtale; publiseringsrett for FoU-leverandøren avtales. Datalisenser og personvern avklares i AP1.</span> <span style="color:red">**[FYLLES INN: rettighetsavtale]**</span>

### Kommunikasjons- og formidlingstiltak

<span style="color:red">Formidlingen skal støtte utnyttelse og kunnskapsspredning:</span>

- <span style="color:red">Vitenskapelig: minst ett metodenotat eller én artikkel om sammenlignbarhet under ufullstendige data, publisert med åpen tilgang.</span>
- <span style="color:red">Næringsrettet: bransjenotat med praktiske læringspunkter for entreprenører og tilbudsmottakere, og presentasjoner på relevante bygg- og rehabiliteringsarenaer.</span> <span style="color:red">**[FYLLES INN: arenaer]**</span>
- <span style="color:red">Populærvitenskapelig: kort, åpen omtale av hva prosjektet har funnet og ikke funnet.</span>
- <span style="color:red">Data- og standardiseringsaktører: målrettet dialog der prosjektet avdekker systematiske datamangler.</span> Det skal ikke loves en ny standard.

<span style="color:red">Ansvaret for formidling ligger i AP6. Forskningsdata deles i tråd med datahåndteringsplanen og bruksrettighetene.</span>

## Prosjektgruppens kompetanse

### Prosjektgruppens kompetanse

<span style="color:red">Vi Bygger Sammen AS er prosjektansvarlig og bidrar med kunnskap om tilbudsfasen og VIBS-plattformen.</span> <span style="color:red">**[FYLLES INN: prosjektleder]**</span>

<span style="color:red">SINTEF er planlagt FoU-leverandør. Forskningsdesign, referansestandard og usikkerhetsanalyse krever uavhengig forskningskompetanse som prosjektansvarlig ikke har selv.</span> <span style="color:red">**[FYLLES INN: enhet og fagpersoner]**</span>

<span style="color:red">D Takst AS er nødvendig for faglige vurderinger av restlevetid, vedlikehold og teknisk tilstand, og for referansevurderingene.</span> <span style="color:red">**[FYLLES INN: fagperson]**</span>

<span style="color:red">Byggmester Espeland AS er nødvendig for reelle tilbudscaser og for å prøve om metoden er forståelig og relevant i en SMB-tilbudsprosess.</span> <span style="color:red">**[FYLLES INN: kontaktperson]**</span>

<span style="color:red">Norsk Byggtjeneste AS er nødvendig for kunnskap om produktdata, identifikatorer, dokumentasjonskvalitet og datarettigheter.</span> <span style="color:red">**[FYLLES INN: kontaktperson]**</span>

Innkjøpt FoU, teknisk arbeid og øvrige spesialisttjenester inngår i prosjektansvarligs kostnad og står derfor ikke som egne finansierende aktører.

## Organisering

### Gjennomføringsplan

<span style="color:red">Prosjektet varer 36 måneder og har sju arbeidspakker:</span>

- <span style="color:red">AP1 Behov, kunnskapsstatus og forskningsdesign (M1–M6, 2,0 MNOK)</span>
- <span style="color:red">AP2 Data, proveniens og harmonisering (M4–M15, 2,8 MNOK)</span>
- <span style="color:red">AP3 Sammenlignbarhetsmetoden (M8–M22, 3,8 MNOK)</span>
- <span style="color:red">AP4 Forskningsimplementasjon (M10–M24, 2,2 MNOK)</span>
- <span style="color:red">AP5 Uavhengig prøving og anvendelighet (M20–M33, 2,5 MNOK)</span>
- <span style="color:red">AP6 Utnyttelse, rettigheter og formidling (M6–M36, 1,3 MNOK)</span>
- <span style="color:red">AP7 Prosjektledelse, kvalitet og risiko (M1–M36, 1,4 MNOK)</span>

AP2 starter først når AP1 har gitt et etterprøvbart datagrunnlag.

<span style="color:red">Hovedmilepælene er beslutningsporter: M6 forskningsprotokoll godkjent, M15 dataport, M22 regelsett låst, M24 reproduserbar forskningsversjon, M26 prøving på caser holdt utenfor, M31 brukertester fullført, M33 forskningsfrys og M36 kommersiell beslutning. En port passeres ikke før kriteriene er oppfylt.</span> Ordinær plattform-, grensesnitt- og produktutvikling inngår ikke.

<span style="color:red">Beløpene er foreløpig skalert og bekreftes med timer per AP og tilbud fra FoU-leverandøren.</span>

### Styring og roller

<span style="color:red">Vi Bygger Sammen AS er prosjektansvarlig og har ansvar for økonomi, kontrakter, framdrift og kommersiell utnyttelse. FoU-leverandøren har faglig ansvar for analyseplan og metodeendringer og kan avvise forskningspåstander som data ikke støtter. VIBS kan ta kommersielle beslutninger, men kan ikke overstyre forskningsresultater. Styringsgruppen består av VIBS og samarbeidspartnerne, og FoU-leverandøren deltar i faglige beslutninger. AP-ansvarlige rapporterer kvartalsvis på leveranser, timer, dataavvik, risiko og budsjett. Endringer etter godkjent forskningsprotokoll begrunnes og kan spores.</span>

<span style="color:red">Rollefordeling: VIBS leder AP1, AP4, AP6 og AP7 og er leveranseeier i alle arbeidspakker. FoU-leverandøren har faglig ansvar i AP1, AP2, AP3 og AP5. D Takst AS bidrar i AP1, AP3 og AP5 med fagvurderinger og referansestandard. Byggmester Espeland AS bidrar i AP2 og AP5 med tilbudscaser og brukertester. Norsk Byggtjeneste AS bidrar i AP1–AP3 med produktdata, koblingsregler og testdata.</span>

<span style="color:red">Hver partner bekrefter rolle, timer, egenfinansiering og resultatbruk i et intensjonsbrev.</span> <span style="color:red">**[FYLLES INN: intensjonsbrev]**</span>

<span style="color:red">Foreløpig kostnadsfordeling, forslag fra VIBS og ikke avtalt med partnerne:</span>

- Vi Bygger Sammen AS: prosjektkostnad 12,6 MNOK, søkt støtte 6,3 MNOK, egenfinansiering 6,3 MNOK
- <span style="color:red">D Takst AS</span>: 1,5 MNOK, 0,75 MNOK, 0,75 MNOK
- <span style="color:red">Byggmester Espeland AS</span>: 0,6 MNOK, 0,30 MNOK, 0,30 MNOK
- <span style="color:red">Norsk Byggtjeneste AS</span>: 1,3 MNOK, 0,65 MNOK, 0,65 MNOK
- Sum: 16,0 MNOK, 8,0 MNOK, 8,0 MNOK

En spesialist på brukerinnsikt kan vurderes for avgrenset arbeid med forståelighet og forklarbarhet dersom dette blir en konkret forskningsleveranse. Ordinær søknadsrådgivning og prosjektbistand holdes utenfor FoU-budsjettet. En standardiseringsfaglig rådgiver kan bidra med standardkart, begreper og lisens- og bruksgrenser, men er ikke foreslått som formell partner. Én test- eller spesialistleverandør kan vurderes dersom en nødvendig leveranse blir definert. Data- og materialaktører kan bidra med avgrensede datasett, provenans og bruksrett, men ikke som finansierende partnere. En offentlig referanseaktør tas bare inn dersom prosjektet trenger et konkret offentlig krav- eller anskaffelsescase. Banker og andre finansaktører inngår ikke i prosjektet, verken som partner, leverandør, referanseaktør eller brukergruppe.

Alle aktivitetene er budsjettert som industriell forskning med 50 prosent støtte. Kostnadene må kontrolleres mot utlysningen, statsstøtteregelverket, selskapsstørrelse og uavhengighet. Leverandørkjøp underfordeles i prosjektansvarligs budsjett og dobbelttelles ikke som egenfinansiering hos leverandøren.

### Risiko

- <span style="color:red">Behovet er mindre enn antatt (sannsynlighet middels, konsekvens høy). Tegn: behovskartleggingen i AP1 viser lav frekvens eller verdi. Tiltak: snevre inn bruksområdet før protokollen låses. Eier: VIBS.</span>
- <span style="color:red">Kunnskapshullet er mindre enn antatt (middels, høy). Tegn: kunnskapsstatus dekker kjernen. Tiltak: avgrense forskningsspørsmålene og ikke overdrive nyhetsverdien. Eier: FoU-leverandør.</span>
- <span style="color:red">Case- eller datatilgang svikter (middels, høy). Tegn: manglende skriftlig tilgang ved M4. Tiltak: reservecase eller redusert omfang, aldri konstruerte data. Eier: VIBS.</span>
- <span style="color:red">Stor faglig uenighet i referansen (middels, middels). Tegn: høy dissens. Tiltak: rapportere intervall og dissens og justere hva som kan prøves. Eier: FoU-leverandør.</span>
- <span style="color:red">Metoden gir falsk sikkerhet (middels, høy). Tegn: feilaktig robuste resultater i kontrollvarianter. Tiltak: stramme grensen; regelsettet låses ikke. Eier: FoU-leverandør.</span>
- <span style="color:red">Uklare resultater i brukertester (middels, middels). Tegn: stor individuell variasjon. Tiltak: rapportere deskriptivt og ikke generalisere. Eier: VIBS.</span>
- <span style="color:red">Partner eller finansiering svikter (middels, høy). Tegn: uavklart kapasitet eller egenfinansiering. Tiltak: omfordele eller avgrense oppgaven. Eier: VIBS.</span>
- <span style="color:red">Svak betalingsvilje (middels, middels). Tegn: kjøper vil ikke betale for dokumentert verdi. Tiltak: endre eller stoppe kommersialiseringsmodellen ved kommersiell beslutning. Eier: VIBS.</span>

## Arbeidspakker

### AP1

#### NAVN PÅ ARBEIDSPAKKE / DELMÅL

<span style="color:red">AP1 Behov, kunnskapsstatus og forskningsdesign</span>

#### BESKRIVELSE

AP1 skal fastsette hva som kan inngå i forskningen, hvordan hver opplysning spores til en kilde, og hvordan kvalitet, mangler og bruksbegrensninger registreres. <span style="color:red">Oppgaver: T1.1 systematisk behovskartlegging med tilbudsansvarlige; T1.2 kunnskapsstatus og konkurrentanalyse; T1.3 valg av to løsningskategorier og 6–8 caser med skriftlig case- og datatilgang; T1.4 forskningsprotokoll, referansestandard, datahåndteringsplan og måleplan. Ansvar: VIBS leder; FoU-leverandøren har faglig ansvar for protokollen; D Takst AS og Norsk Byggtjeneste AS bidrar med fag- og datakrav.</span> Uavklarte datakilder skal utelates eller merkes som ubrukbare for neste trinn.

#### TITTEL PÅ MILEPÆL

<span style="color:red">M6 Forskningsprotokoll godkjent</span>

#### BESKRIVELSE AV MILEPÆL

<span style="color:red">Kunnskapshullet er dokumentert, 6–8 caser er tilgjengelige med skriftlig tilgang, kritiske data- og lisensforhold er lukket, og forskningsprotokoll, referansestandard og datahåndteringsplan er godkjent av FoU-leverandøren.</span> AP1 godkjennes når protokollen angir inklusjons- og eksklusjonsregler, provenans, datakvalitetsklasser, behandling av manglende data og avgrensning av data-, lisens-, personvern- og sikkerhetsansvar. Leveranseeier dokumenterer beslutningen om hvilke datasett og tilbudssituasjoner som går videre til AP2.

#### KOSTNADSSPESIFIKASJONER

<span style="color:red">2,0 MNOK, foreløpig.</span> <span style="color:red">**[FYLLES INN: kostnadstype og aktør]**</span>

### AP2

#### NAVN PÅ ARBEIDSPAKKE / DELMÅL

<span style="color:red">AP2 Data, proveniens og harmonisering</span>

#### BESKRIVELSE

AP2 skal utvikle og prøve regler for å gjøre opplysninger fra ulike kilder sammenlignbare uten å skjule forskjeller i definisjon, systemgrense, tidspunkt eller dokumentasjonsstyrke. <span style="color:red">Oppgaver: T2.1 datamodell og proveniens; T2.2 datakvalitetsklasser; T2.3 harmoniseringsregler; T2.4 kontrollerte datavarianter der én faktor endres om gangen. Ansvar: FoU-leverandøren faglig; Norsk Byggtjeneste AS med koblingsregler og testdata; Byggmester Espeland AS med tilbudscaser.</span>

#### TITTEL PÅ MILEPÆL

<span style="color:red">M15 Dataport</span>

#### BESKRIVELSE AV MILEPÆL

AP2 godkjennes når samme dokumenterte regelsett kan anvendes på de valgte tilbudssituasjonene, alle transformasjoner kan spores tilbake til kildegrunnlaget, og manglende eller ikke-sammenlignbare opplysninger vises i stedet for å fylles inn som sikre verdier. <span style="color:red">Obligatoriske datafelt er klassifisert, og de kontrollerte datavariantene kan reproduseres.</span> Avvik og uløste harmoniseringsproblemer skal dokumenteres før de inngår i AP3.

#### KOSTNADSSPESIFIKASJONER

<span style="color:red">2,8 MNOK, foreløpig.</span> <span style="color:red">**[FYLLES INN: kostnadstype og aktør]**</span>

### AP3

#### NAVN PÅ ARBEIDSPAKKE / DELMÅL

<span style="color:red">AP3 Sammenlignbarhetsmetoden</span>

#### BESKRIVELSE

AP3 skal undersøke hvordan usikkerhet og vekting påvirker sammenligningen. Målet er en forklarbar modell som viser konsekvensene av faglige valg, ikke én universell rangering av løsninger. <span style="color:red">Oppgaver: T3.1 teknisk egnethetsport; T3.2 konsekvensmodell for kostnad, klima, levetid og vedlikehold; T3.3 usikkerhets- og sensitivitetsregler; T3.4 regler for når en sammenligning er robust, betinget eller utilstrekkelig belyst. Ansvar: FoU-leverandøren faglig; D Takst AS med vurderinger av restlevetid og tilstand; Norsk Byggtjeneste AS med kontroll av hvordan datamangler slår ut.</span>

#### TITTEL PÅ MILEPÆL

<span style="color:red">M22 Regelsett låst</span>

#### BESKRIVELSE AV MILEPÆL

Alternative vektinger og sentrale usikkerheter er testet, endringer i resultatet kan forklares, og modellen er versjonert med kilder, forutsetninger, begrensninger og kjente feilkilder. <span style="color:red">Casene som holdes utenfor, er ikke brukt til justering.</span>

#### KOSTNADSSPESIFIKASJONER

<span style="color:red">3,8 MNOK, foreløpig.</span> <span style="color:red">**[FYLLES INN: kostnadstype og aktør]**</span>

### AP4

#### NAVN PÅ ARBEIDSPAKKE / DELMÅL

<span style="color:red">AP4 Forskningsimplementasjon</span>

#### BESKRIVELSE

<span style="color:red">AP4 lager en minimal, reproduserbar implementasjon av regelsettet og et forklaringslag, slik at metoden kan prøves og resultatene gjenskapes. Oppgaver: T4.1 datainntak og sporbarhet; T4.2 implementasjon av regler; T4.3 forklaringslag og testgrensesnitt. Ansvar: VIBS, eventuelt med teknisk underleverandør.</span> Teknisk leveranse gir ikke i seg selv rollen som FoU-leverandør. Ordinær plattform-, grensesnitt- og produktutvikling inngår ikke.

#### TITTEL PÅ MILEPÆL

<span style="color:red">M24 Reproduserbar forskningsversjon</span>

#### BESKRIVELSE AV MILEPÆL

<span style="color:red">Kode og regler er versjonert, og testresultatene kan gjenskapes uten muntlig støtte.</span>

#### KOSTNADSSPESIFIKASJONER

<span style="color:red">2,2 MNOK, foreløpig.</span> <span style="color:red">**[FYLLES INN: kostnadstype og aktør]**</span>

### AP5

#### NAVN PÅ ARBEIDSPAKKE / DELMÅL

<span style="color:red">AP5 Uavhengig prøving og anvendelighet</span>

#### BESKRIVELSE

<span style="color:red">AP5 prøver regelsettet på caser som ikke er brukt i utviklingen, sammenligner med dagens praksis og undersøker om fagpersoner og tilbudsmottakere forstår resultatene. Oppgaver: T5.1 prøving på 2–3 caser holdt utenfor, uten regelendring; T5.2 sammenligning med vurderinger etter dagens praksis; T5.3 test med 8–12 fagpersoner; T5.4 test med 8–15 tilbudsmottakere; T5.5 forskningsfrys med gyldighetsområde. Ansvar: FoU-leverandøren faglig; D Takst AS med referansevurderinger; Byggmester Espeland AS med fagpersoner og tilbudssituasjoner.</span> Modellfrys vedtas bare dersom forskningsgrunnlaget kan etterprøves.

#### TITTEL PÅ MILEPÆL

<span style="color:red">M26 Prøving på caser holdt utenfor</span>

#### BESKRIVELSE AV MILEPÆL

<span style="color:red">Alle 2–3 caser er kjørt uten regelendring, og avvik og dissens er logget.</span>

#### TITTEL PÅ MILEPÆL

<span style="color:red">M31 Brukertester fullført</span>

#### BESKRIVELSE AV MILEPÆL

<span style="color:red">Fagperson- og mottakertestene er gjennomført, og primære utfall og feilmønstre er dokumentert.</span>

#### TITTEL PÅ MILEPÆL

<span style="color:red">M33 Forskningsfrys</span>

#### BESKRIVELSE AV MILEPÆL

<span style="color:red">Empirisk prøvd forskningsversjon med gyldighetsområde, usikkerhet og kjente feilkilder.</span> Hvis porten ikke nås, skal kunnskapshull og behov for omarbeiding dokumenteres; det skal ikke hevdes at modellen er validert.

#### KOSTNADSSPESIFIKASJONER

<span style="color:red">2,5 MNOK, foreløpig.</span> <span style="color:red">**[FYLLES INN: kostnadstype og aktør]**</span>

### AP6

#### NAVN PÅ ARBEIDSPAKKE / DELMÅL

<span style="color:red">AP6 Utnyttelse, rettigheter og formidling</span>

#### BESKRIVELSE

<span style="color:red">AP6 sørger for at resultatene kan tas i bruk og deles. Oppgaver: T6.1 rettighetsprinsipper for bakgrunn, nye resultater, kode, data og publisering; T6.2 partnernes resultatbruk og måling av gevinst; T6.3 formidling og åpen publisering; T6.4 grunnlag for kommersiell beslutning. Markedsundersøkelser inngår ikke. Ansvar: VIBS, med alle partnere.</span>

#### TITTEL PÅ MILEPÆL

<span style="color:red">M36 Kommersiell beslutning</span>

#### BESKRIVELSE AV MILEPÆL

<span style="color:red">Videre pilot besluttes bare dersom kjøper, betalingssignal, dekningsbidrag, rettigheter, finansiering og plan for skalering er troverdige.</span> Praktisk beslutnings- og kommersiell effekt er ikke et akseptkriterium for modellfrys.

#### KOSTNADSSPESIFIKASJONER

<span style="color:red">1,3 MNOK, foreløpig.</span> <span style="color:red">**[FYLLES INN: kostnadstype og aktør]**</span>

### AP7

#### NAVN PÅ ARBEIDSPAKKE / DELMÅL

<span style="color:red">AP7 Prosjektledelse, kvalitet og risiko</span>

#### BESKRIVELSE

<span style="color:red">AP7 omfatter framdrift, økonomi, kvalitetssikring, risikooppfølging og protokollerte portbeslutninger. Oppgaver: T7.1 styringsgruppe og kvartalsrapportering; T7.2 budsjett og timeføring; T7.3 risikoregister; T7.4 beslutningslogg for portene. Ansvar: VIBS.</span>

#### TITTEL PÅ MILEPÆL

<span style="color:red">M36 Sluttrapport</span>

#### BESKRIVELSE AV MILEPÆL

<span style="color:red">Sluttrapport med beslutningslogg, regnskap og samlet vurdering av porter og risiko.</span>

#### KOSTNADSSPESIFIKASJONER

<span style="color:red">1,4 MNOK, foreløpig.</span> <span style="color:red">**[FYLLES INN: kostnadstype og aktør]**</span>

## Vedlegg (ikke søknadstekst)

### Hvor v1.7 har havnet

- Sammendrag → Sammendrag (forkortet)
- K1 → Kunnskapsbehov; SSB-avsnittet og brukerforutsetningen → Behov og markedsmuligheter
- K2 → Kunnskapsbehov (standarder) og Innovasjonen (nyhetsverdi)
- K3 → Hovedmål, Delmål og forskningsspørsmål i Kunnskapsbehov
- K4 → FoU-metoder (metode) og Etiske problemstillinger (persondata)
- V1 → Samfunnseffekter (tabellen omskrevet til tekst)
- V2 → Samfunnseffekter
- V3 → Verdiskapingspotensial, Realiseringsplan og Samfunnseffekter (produsent og dataaktør)
- AP1–AP3 med porter → AP1, AP2, AP3 og AP5 med milepæler
- Foreløpig organisering og økonomi → Styring og roller og Prosjektgruppens kompetanse

### Tatt ut fra v1.7

- AP1–AP3 som eneste struktur (erstattet av AP1–AP7). Akseptkriteriene er lagt tilbake i milepælene M6, M15 og M22.
- Måleplan og gevinstkjede er lagt tilbake som punktlister (FoU-metoder og Verdiskapingspotensial), fordi portalfeltene ikke tar tabeller.
- Underfordeling av VIBS' 12,6 MNOK, likviditet, timefordelingsport og krav til rollekort: flyttet til sannhetsserumet §2b (arbeidsliste, ikke søknadstekst).
- Nærstående testarena (Sør Bygg AS er tatt ut av VERIFIED).
- Avsnittet om mulig andre SMB-test.
- Avsnittet om kartlegging av arbeidet i avgrensede tilbudsoppgaver som forskningshypotese (dekkes av måleplan og gevinstkjede).

### Tatt ut fra v4.0

- 12,6 MNOK som ramme, Ciroth og Theilig som kilder, overførbarhetsstudien (T5.4), markedsundersøkelser, interne sjekklister og 5/5-målbilde

### Tegntelling per portalfelt

> Tegn med mellomrom og linjeskift, uten markering. Over grensen = må kortes i v2.0.

| Felt | Grense | Faktisk | Status |
|---|---:|---:|---|
| PROSJEKTTITTEL PÅ NORSK | 100 | 75 | OK |
| PROSJEKTTITTEL PÅ ENGELSK | 100 | 74 | OK |
| KORTNAVN | 10 | 8 | OK |
| Hovedmål | 500 | 379 | OK |
| Delmål | 1000 | 680 | OK |
| Skriv et sammendrag av prosjektet | 1500 | 1138 | OK |
| Kunnskapsbehov og mål for prosjektet | 5000 | 2588 | OK |
| FoU-metoder og -aktiviteter | 5000 | 4610 | OK |
| Etiske problemstillinger | 2000 | 718 | OK |
| Kjønnsperspektiver | 2000 | 447 | OK |
| Innovasjonen | 5000 | 2241 | OK |
| Behov og markedsmuligheter | 2000 | 1108 | OK |
| Referanseliste | 5000 | 911 | OK |
| Samfunnseffekter | 5000 | 1993 | OK |
| FNs bærekraftsmål | 2000 | 798 | OK |
| Verdiskapingspotensial | 5000 | 4319 | OK |
| Realiseringsplan for verdiskaping | 2000 | 924 | OK |
| Kommunikasjons- og formidlingstiltak | 5000 | 705 | OK |
| Prosjektgruppens kompetanse | 3000 | 946 | OK |
| Gjennomføringsplan | 3000 | 979 | OK |
| Styring og roller | 5000 | 2590 | OK |
| Risiko | 3000 | 1384 | OK |
| AP1 – NAVN PÅ ARBEIDSPAKKE / DELMÅL | 100 | 46 | OK |
| AP1 – BESKRIVELSE | 1500 | 649 | OK |
| AP1 – TITTEL PÅ MILEPÆL | 100 | 31 | OK |
| AP1 – BESKRIVELSE AV MILEPÆL | 1000 | 527 | OK |
| AP1 – KOSTNADSSPESIFIKASJONER | 500 | 56 | OK |
| AP2 – NAVN PÅ ARBEIDSPAKKE / DELMÅL | 100 | 37 | OK |
| AP2 – BESKRIVELSE | 1500 | 468 | OK |
| AP2 – TITTEL PÅ MILEPÆL | 100 | 12 | OK |
| AP2 – BESKRIVELSE AV MILEPÆL | 1000 | 430 | OK |
| AP2 – KOSTNADSSPESIFIKASJONER | 500 | 56 | OK |
| AP3 – NAVN PÅ ARBEIDSPAKKE / DELMÅL | 100 | 28 | OK |
| AP3 – BESKRIVELSE | 1500 | 575 | OK |
| AP3 – TITTEL PÅ MILEPÆL | 100 | 18 | OK |
| AP3 – BESKRIVELSE AV MILEPÆL | 1000 | 241 | OK |
| AP3 – KOSTNADSSPESIFIKASJONER | 500 | 56 | OK |
| AP4 – NAVN PÅ ARBEIDSPAKKE / DELMÅL | 100 | 28 | OK |
| AP4 – BESKRIVELSE | 1500 | 437 | OK |
| AP4 – TITTEL PÅ MILEPÆL | 100 | 35 | OK |
| AP4 – BESKRIVELSE AV MILEPÆL | 1000 | 84 | OK |
| AP4 – KOSTNADSSPESIFIKASJONER | 500 | 56 | OK |
| AP5 – NAVN PÅ ARBEIDSPAKKE / DELMÅL | 100 | 38 | OK |
| AP5 – BESKRIVELSE | 1500 | 604 | OK |
| AP5 – TITTEL PÅ MILEPÆL | 100 | 34 | OK |
| AP5 – BESKRIVELSE AV MILEPÆL | 1000 | 73 | OK |
| AP5 – TITTEL PÅ MILEPÆL | 100 | 25 | OK |
| AP5 – BESKRIVELSE AV MILEPÆL | 1000 | 94 | OK |
| AP5 – TITTEL PÅ MILEPÆL | 100 | 18 | OK |
| AP5 – BESKRIVELSE AV MILEPÆL | 1000 | 213 | OK |
| AP5 – KOSTNADSSPESIFIKASJONER | 500 | 56 | OK |
| AP6 – NAVN PÅ ARBEIDSPAKKE / DELMÅL | 100 | 41 | OK |
| AP6 – BESKRIVELSE | 1500 | 344 | OK |
| AP6 – TITTEL PÅ MILEPÆL | 100 | 26 | OK |
| AP6 – BESKRIVELSE AV MILEPÆL | 1000 | 225 | OK |
| AP6 – KOSTNADSSPESIFIKASJONER | 500 | 56 | OK |
| AP7 – NAVN PÅ ARBEIDSPAKKE / DELMÅL | 100 | 39 | OK |
| AP7 – BESKRIVELSE | 1500 | 255 | OK |
| AP7 – TITTEL PÅ MILEPÆL | 100 | 16 | OK |
| AP7 – BESKRIVELSE AV MILEPÆL | 1000 | 83 | OK |
| AP7 – KOSTNADSSPESIFIKASJONER | 500 | 56 | OK |
