---
title: Handoff — godkjent review av K1–K4 og V1–V3
dato: 2026-07-25
status: komplett arbeids-handoff, ikke innsendingsklar
repository: Luaze1985/INP
branch: work/k1-godkjent-arbeidsversjon
scope: prosjektbeskrivelse K1–K4 og V1–V3
---

# Handoff — godkjent review av K1–K4 og V1–V3

## 1. Formål

Denne filen dokumenterer arbeidet som er gjennomført i reviewrunden for prosjektbeskrivelsen til VERIFIED.

Den skal brukes som direkte inngang til videre arbeid i repoet. Den viser:

- nøyaktige filstier;
- hvilke tekster som er godkjent;
- hvilke steder som er endret;
- hvilke formuleringer og avgrensninger som nå gjelder;
- hva som fortsatt må avklares før tekstene flettes inn i de kanoniske kapitlene;
- anbefalt neste arbeidssteg.

Denne handoffen erstatter ikke arbeidsversjonene. Ved videre redigering er arbeidsversjonene under kilden til selve teksten.

## 2. Repo- og grenstatus

- **Repository:** `Luaze1985/INP`
- **Arbeidsgren:** `work/k1-godkjent-arbeidsversjon`
- **Base:** `main`
- **Kanoniske kapitler:** ikke endret
- **Status:** godkjente arbeidsversjoner finnes på arbeidsgrenen
- **Viktig:** Tekstene er godkjent som arbeidsversjoner, men er ikke kildeverifisert, komprimert eller innsendingsklare.

## 3. Filer som er opprettet

| Kapittel | Godkjent arbeidsversjon | Kanonisk målfil |
| --- | --- | --- |
| K1 | `docs/reference/prosjektbeskrivelse/arbeidsversjoner/k1-bakgrunn-godkjent-v0.1.md` | `docs/reference/prosjektbeskrivelse/k1-bakgrunn.md` |
| K2 | `docs/reference/prosjektbeskrivelse/arbeidsversjoner/k2-nyhetsverdi-godkjent-v0.1.md` | `docs/reference/prosjektbeskrivelse/k2-nyhetsverdi.md` |
| K3 | `docs/reference/prosjektbeskrivelse/arbeidsversjoner/k3-forskning-godkjent-v0.1.md` | `docs/reference/prosjektbeskrivelse/k3-forskning.md` |
| K4 | `docs/reference/prosjektbeskrivelse/arbeidsversjoner/k4-metode-godkjent-v0.1.md` | `docs/reference/prosjektbeskrivelse/k4-metode.md` |
| V1 | `docs/reference/prosjektbeskrivelse/arbeidsversjoner/v1-baerekraft-godkjent-v0.1.md` | `docs/reference/prosjektbeskrivelse/v1-baerekraft.md` |
| V2 | `docs/reference/prosjektbeskrivelse/arbeidsversjoner/v2-dnsh-godkjent-v0.1.md` | `docs/reference/prosjektbeskrivelse/v2-sikkerhet.md` |
| V3 | `docs/reference/prosjektbeskrivelse/arbeidsversjoner/v3-okonomiske-virkninger-bankrelevans-godkjent-v0.1.md` | `docs/reference/prosjektbeskrivelse/v3-samfunnsokonomi.md` |
| Kontroll | `docs/reference/prosjektbeskrivelse/arbeidsversjoner/00-konsistenskontroll-godkjente-arbeidsversjoner-v0.1.md` | Ingen kanonisk målfil |

## 4. Felles beslutninger som gjelder alle kapitler

### 4.1 Løsningsvalg

VERIFIED skal omtale **alternative løsninger**, ikke bare material- eller produktvalg.

Begrepet omfatter blant annet:

- nyanskaffelse;
- vedlikehold;
- reparasjon;
- rehabilitering;
- ombruk;
- forskjellige produkter eller utførelsesmåter for samme behov.

### 4.2 Beslutningsstøtte, ikke automatisk valg

Modellen skal:

- sammenligne alternativer;
- vise forskjeller og avveininger;
- vise datakvalitet og usikkerhet;
- forklare grunnlaget.

Modellen skal ikke:

- kåre ett alternativ som «beste valg»;
- ta den faglige eller kommersielle beslutningen;
- profilere personer;
- ta automatiske kredittbeslutninger.

### 4.3 Datastatus

Felles ordlyd for datastatus er:

> En opplysning mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen.

Denne ordlyden skal brukes konsekvent i K4, V1 og V2.

### 4.4 Plattformens rolle

Godkjent formulering er:

> VIBS-plattformen kan brukes som testflate for prosjektet.

Vent med å omtale den som «integrasjonsflate» til dataflyt og arkitektur er nærmere definert.

### 4.5 Banksporet

Kjerneprosjektet er avgrenset til ett konkret bankbehov.

Banksporet skal:

- bygge på produkt-, prosjekt- og byggdokumentasjon;
- defineres av banken før pilotering;
- undersøke om dokumentasjonen er relevant tilleggsinformasjon;
- ikke bruke personprofilering;
- ikke utvikle automatisk kredittbeslutning.

Forsikring og takst er tatt ut som konkrete hovedspor og kan bare omtales som mulige senere skaleringsspor.

## 5. K1 — Bakgrunn og utfordring

### Fil

`docs/reference/prosjektbeskrivelse/arbeidsversjoner/k1-bakgrunn-godkjent-v0.1.md`

### Godkjent hovedretning

K1 beskriver at sentrale løsningsvalg tas i tilbudsfasen, at relevant informasjon er spredt, og at mindre entreprenører kan mangle egne ressurser til spesialiserte vurderinger selv om de har sterk fagkompetanse.

VERIFIED skal utvikle og teste en modell som samler, vekter og forklarer informasjon om alternative løsninger. Entreprenør og kunde beholder beslutningsansvaret.

### Viktige referansesteder

- `K1-P1-S1`–`K1-P1-S3`: tilbudsfasen og betydningen av tidlige løsningsvalg.
- `K1-P2-S1`–`K1-P2-S3`: spredte datakilder og prosjektets utgangspunkt.
- `K1-P3-S1`: forskjellen mellom fagkompetanse og tilgang til spesialiserte analyse­ressurser.
- `K1-P4-S1`–`K1-P4-S2`: behovet for å veie pris, erfaring og dokumentasjon.
- `K1-P5-S1`–`K1-P5-S2`: hva VERIFIED skal utvikle og teste.
- `K1-P6-S1`–`K1-P6-S2`: FoU-avgrensningen.

### Åpne porter

- SMB-definisjon og andel av næringen må avklares.
- Tidligfasepåstanden må primærverifiseres i `[KD2024]`.
- Ressurs- og kompetansebarrieren må kobles til korrekt kilde.

## 6. K2 — Nyhetsverdi

### Fil

`docs/reference/prosjektbeskrivelse/arbeidsversjoner/k2-nyhetsverdi-godkjent-v0.1.md`

### Godkjent hovedretning

Nyhetsverdien er ikke en ny app, miljømerking eller kalkulator. Den ligger i å utvikle og teste et forklarbart og etterprøvbart beslutningsgrunnlag som samler flere typer byggdata i tilbudsfasen.

Eksisterende standarder, datakilder, metoder og verktøy dekker ulike deler av behovet, men kartleggingen dokumenterer ikke én samlet løsning som kombinerer hele bredden.

### Viktige referansesteder

- `K2-P1-S1`–`K2-P1-S2`: presis definisjon av nyhetsverdien.
- `K2-P2-S1`–`K2-P2-S5`: eksisterende byggeklosser og begrensningene i kartlagte løsninger.
- `K2-P3-S1`–`K2-P3-S2`: hva VERIFIED skal undersøke.
- `K2-P4-S1`–`K2-P4-S3`: skillet mellom VIBS-plattformen og VERIFIEDs FoU-lag.
- `K2-T1-R1`–`K2-T1-R6`: seks kunnskapshull.
- `K2-P6-S1`–`K2-P6-S6`: FoU-avgrensning og mulig senere verdi.

### Konsistensretting som er gjennomført

- Bankomfanget er avgrenset til bank.
- Forsikring er tatt ut som konkret mottaker.
- Plattformen omtales konsekvent som testflate.

### Åpne porter

- Norske og europeiske verktøy trenger bedre uavhengig dekning.
- Påstander om tilbudsfase, SMB-anvendbarhet og beslutningseffekt må fortsatt behandles som kunnskapshull eller FoU-spørsmål.

## 7. K3 — Mål og FoU-spørsmål

### Fil

`docs/reference/prosjektbeskrivelse/arbeidsversjoner/k3-forskning-godkjent-v0.1.md`

### Hovedmål

Se `K3-P1-S1`–`K3-P1-S3`.

Hovedmålet er å utvikle og teste en forskningsbasert beslutningsmodell for sammenligning av alternative løsninger i små og mellomstore byggeprosjekter.

Kriterielisten er samordnet med senere kapitler og omfatter:

- pris;
- klima;
- levetid;
- vedlikehold;
- teknisk kvalitet;
- ombruk;
- dokumentasjon;
- risiko.

### FoU-spørsmål

- `K3-F1`: dokumentasjon av levetid, vedlikehold og kvalitet som grunnlag for sammenlignbare livsløpskostnader.
- `K3-F2`: kobling av NOBB, GTIN, EPD, FDV og prisdata før tilbudet sendes.
- `K3-F3`: avveining mellom ombruk, reparasjon, vedlikehold, rehabilitering og nyanskaffelse.
- `K3-F4`: forståelse, bruk og beslutningseffekt hos entreprenører og kunder.
- `K3-F5`: byggteknisk dokumentasjon som relevant tilleggsinformasjon for bankens vurdering, uten personprofilering eller automatisk kredittbeslutning.
- `K3-F6`: hvordan dataflyt, dokumentasjon og nødvendige grensesnitt kan utformes og testes slik at modellen er etterprøvbar og kan overføres til en ny produktkategori.

### Konsistensrettinger som er gjennomført

- Teknisk kvalitet og ombruk er lagt inn i hovedmålets kriterieliste.
- F6 er endret fra «bygge API-er» til utforming og testing av dataflyt, dokumentasjon og grensesnitt.
- Plattformen omtales som testflate.

### Åpne porter

- Lars Gunnar må definere konkrete målepunkter for F4.
- Banken må definere konkret behov og beslutningssituasjon for F5.
- Betydningen av «overføres til en ny produktkategori» må spesifiseres.

## 8. K4 — Metode og forskningsetikk

### Fil

`docs/reference/prosjektbeskrivelse/arbeidsversjoner/k4-metode-godkjent-v0.1.md`

### Godkjent forskningsløype

Se `K4-P1-S1`–`K4-P1-S3`:

1. utvikle første versjon av beslutningsmodellen;
2. teste den i konkrete løsningsvalg;
3. måle resultatene;
4. justere modellen på grunnlag av funnene.

### Datagrunnlag og dokumentasjonstillit

Se `K4-P2-S1`–`K4-P2-S6`.

For hver opplysning registreres:

- kilde;
- alder;
- enhet;
- produktnivå;
- dokumentasjonsstatus.

Reglene skal fastsettes før piloteringen og brukes likt på alle alternativer.

### Metodevalg

Se `K4-P3-S1`–`K4-P3-S3`.

Aktuelle flerkriteriemetoder skal sammenlignes etter:

- forklarbarhet;
- følsomhet for endrede vekter;
- datakrav;
- håndtering av manglende data;
- brukerforståelse.

### Målepunkter

Se `K4-T1-R1`–`K4-T1-R9`.

Tabellen dekker:

- dataintegrasjon;
- livsløpssammenligning;
- forklarbarhet;
- usikkerhet;
- beslutningseffekt;
- tidsbruk;
- bankrelevans;
- skalering;
- sirkulær sammenligning.

`K4-T1-R9` ble lagt til for å dekke F3 eksplisitt: materialmengde, restlevetid, teknisk egnethet og beregnede utskiftninger for nyanskaffelse, reparasjon, rehabilitering og ombruk.

### Etikk og ansvar

Se `K4-P5-S1`–`K4-P7-S1`.

- minst mulig persondata;
- informert deltakelse;
- anonymisering eller pseudonymisering;
- ingen personprofilering;
- ingen automatiske kredittbeslutninger;
- åpenhet om datakilder, antakelser og usikkerhet.

### Åpne porter

- produktkategorier;
- baseline og sammenligningsgrunnlag;
- bankens informasjonsbehov;
- målepunkter for beslutningseffekt;
- første MCDA-metode eller sammenligningsopplegg;
- kobling mot endelig arbeidspakkestruktur.

## 9. V1 — Miljø og bærekraft

### Fil

`docs/reference/prosjektbeskrivelse/arbeidsversjoner/v1-baerekraft-godkjent-v0.1.md`

### Godkjent hovedretning

- Primært bærekraftsmål: 12.2 om effektiv bruk av naturressurser.
- Sekundært: 12.5 dersom pilotene faktisk måler reparasjon, ombruk, utsatt utskifting og redusert materialbruk eller avfall.
- Prosjektet skal ikke telle flest mulig bærekraftsmål.

### Viktige referansesteder

- `V1-P1-S1`–`V1-P1-S3`: valg av bærekraftsmål.
- `V1-P2-S1`–`V1-P2-S3`: beslutningsmekanismen.
- `V1-P3-S1`–`V1-P3-S3`: klima som mulighetsrom, ikke lovet effekt.
- `V1-P4-S1`–`V1-P4-S3`: skille mellom direkte målt og beregnet effekt.
- `V1-T1-R1`–`V1-T1-R6`: effektmåling.
- `V1-P5-S1`–`V1-P5-S3`: feil og omarbeid.
- `V1-P6-S1`–`V1-P6-S2`: sirkulærøkonomi.
- `V1-P7-S1`–`V1-P7-S3`: do-not-harm.

### Effektområder

- beregnet klimagassutslipp;
- ressursbruk;
- livsløpskostnad;
- beslutningseffekt;
- brukbarhet;
- dokumentasjonskvalitet.

### Åpne porter

- `[EBA_NO2023]` og `[KD2024]` må primærverifiseres.
- produktkategorier og funksjonell enhet må avklares;
- analyseperiode for LCC må fastsettes;
- baseline, datakilde og måleansvarlig må defineres;
- reelle sirkulære alternativer må inngå dersom 12.5 skal brukes.

## 10. V2 — Do-not-harm

### Fil

`docs/reference/prosjektbeskrivelse/arbeidsversjoner/v2-dnsh-godkjent-v0.1.md`

### Godkjent hovedretning

Do-not-harm skal være en del av beslutningsmodellen og piloteringen, ikke et separat vedlegg.

Modellen skal ikke automatisk velge ett alternativ. Den skal vise avveininger, usikkerhet og negative konsekvenser.

### Operative regler

Se `V2-T1-R1`–`V2-T1-R11`.

Hver risiko kobles til:

- modellregel;
- reaksjon;
- pilotmåling.

Risikoene omfatter blant annet:

- lavt CO₂ og svak levetid;
- lav pris og høy livsløpsbelastning;
- manglende produktdokumentasjon;
- falsk presisjon;
- leverandørskjevhet;
- rapporteringsbyrde for SMB;
- persondata i banksporet;
- ombruk uten teknisk egnethet;
- kjemikalie-, helse- eller sikkerhetsfare;
- reparasjon uten dokumentert effekt;
- effektpåstander uten baseline.

### Viktige referansesteder

- `V2-P2-S1`–`V2-P2-S4`: sammenligning, ikke automatisk valg.
- `V2-P3-S1`: krav om modellregel, reaksjon og test.
- `V2-P4-S1`–`V2-P4-S3`: felles datastatus og retting av dokumentasjon.
- `V2-P5-S1`–`V2-P5-S4`: falsk presisjon og følsomhet.
- `V2-P6-S1`–`V2-P6-S3`: avgrensning av kjemikalier og sosiale forhold.
- `V2-P7-S1`–`V2-P7-S3`: beslutningsansvar.

### Åpne porter

- obligatoriske dokumentasjonskrav og stoppregler per produktkategori;
- hvem som godkjenner DNSH-regler og unntak;
- kobling av hver regel til arbeidspakke og målepunkt;
- avgrensning av sosiale minstekrav.

## 11. V3 — Økonomiske virkninger og bankrelevans

### Fil

`docs/reference/prosjektbeskrivelse/arbeidsversjoner/v3-okonomiske-virkninger-bankrelevans-godkjent-v0.1.md`

### Godkjent hovedretning

VERIFIED skal først og fremst løse et byggproblem. Bank er et avgrenset mulig anvendelsesområde for bedre byggdokumentasjon.

Kapitlet skal undersøke:

- tidsbruk i tilbud;
- tilbudskvalitet;
- dokumentasjonsmangler;
- observerbare avvik;
- kundens forståelse av kostnad, risiko og usikkerhet;
- om byggdokumentasjonen svarer på bankens forhåndsdefinerte informasjonsbehov.

### Viktige avgrensninger

- Energiforskning kan brukes som støtte for energi og boliglånsrisiko.
- Sammenhengen mellom teknisk kvalitet, levetid, vedlikehold og bankrisiko er et FoU-spørsmål, ikke en etablert konklusjon.
- Forsikring og takst er tatt ut som konkrete hovedspor.
- Bankgrunnlaget skal ikke bruke private kundedata eller personprofilering.

### Åpne porter

- Banken må definere konkret informasjonsbehov, vurderingssituasjon og kriterium for nytte.
- `[An2020]` kan ikke brukes bærende før fulltekstkontroll.
- Økonomiske effekter må kobles til baseline og måleansvarlig.

## 12. Konsistenskontroll som er gjennomført

### Fil

`docs/reference/prosjektbeskrivelse/arbeidsversjoner/00-konsistenskontroll-godkjente-arbeidsversjoner-v0.1.md`

### Løste avvik

- `C1`: bankomfang samordnet;
- `C2`: plattformrolle samordnet;
- `C3`: teknisk kvalitet og ombruk inn i hovedmålet;
- `C4`: eget målepunkt for F3 lagt inn i K4;
- `C5`: F6 omskrevet til utforming og testing;
- `C6`: datastatus standardisert.

### Gjenstående kvalitetsport

`C7` er fortsatt åpen:

> Arbeidsversjonene må gjennom et samlet kilde- og komprimeringspass før innfletting.

## 13. Det som ikke er gjort

Følgende er bevisst ikke gjort:

- ingen arbeidsversjon er flettet inn i kanoniske kapitler;
- `main` er ikke endret;
- ingen pull request er opprettet;
- kildestatus er ikke oppgradert uten verifisering;
- påstander med åpne kilder er ikke gjort sterkere;
- teksten er ikke tilpasset endelig sidebudsjett;
- arbeidspakker og gjennomføring er ikke omskrevet i denne runden.

## 14. Neste trygge steg

### Anbefalt rekkefølge

1. Gjennomfør kildepass for alle bærende påstander.
2. Merk hver påstand som dokumentert, forbeholden hypotese eller FoU-spørsmål.
3. Komprimer gjentakelser mellom K2, K3, K4, V1 og V2.
4. Behold sporbar kobling fra hvert FoU-spørsmål til metode og målepunkt.
5. Kontroller teksten mot samlet sidebudsjett og endelig arbeidspakkestruktur.
6. Lag én innflettingsdiff mot de kanoniske kapitlene.
7. Gjør kritisk review før pull request.

### Ikke gjør ennå

- Ikke flett arbeidsversjonene ordrett inn.
- Ikke opprett endelig PR før kilde- og komprimeringspasset er fullført.
- Ikke gjeninnfør forsikring, takst eller sterk bankeffekt uten eksplisitt beslutning og dokumentasjon.
- Ikke skriv at VERIFIED allerede reduserer utslipp, feil, omarbeid eller risiko.

## 15. Instruks til neste agent

Les i denne rekkefølgen:

1. `AGENTS.md`
2. `CONTEXT.md`
3. `docs/reference/prosjektbeskrivelse/README.md`
4. denne handoffen
5. `00-konsistenskontroll-godkjente-arbeidsversjoner-v0.1.md`
6. arbeidsversjonene K1–K4 og V1–V3
7. kanoniske kapitler
8. relevant kilde- og statusdokumentasjon

Oppgaven er først å kontrollere og komprimere, ikke å skrive prosjektet på nytt.

Ved endring skal agenten:

- bevare de godkjente beslutningene i denne handoffen;
- vise nøyaktig hvilke ID-er som endres;
- ikke styrke en påstand uten kildegrunnlag;
- holde hypoteser og planlagte tester tydelig atskilt fra dokumenterte funn;
- ikke endre kanoniske kapitler uten eksplisitt godkjenning;
- rapportere endrede filer, avvik, åpne spørsmål og anbefalt neste steg.
