---
title: V2 — Do-not-harm (DNSH) — godkjent arbeidsversjon
dato: 2026-07-25
versjon: 0.1
status: godkjent arbeidsversjon, ikke innsendingsklar
kilde: ChatGPT Work-gjennomgang, godkjent av Lars Erik
kanonisk_kapittel: ../v2-sikkerhet.md
formaal: Stabil referanse med faste avsnitts-, setnings- og tabell-ID-er
---

# V2 — Do-not-harm (DNSH)

> Denne filen er en godkjent arbeidsversjon. Den erstatter ikke det kanoniske kapitlet før endringen er flettet inn og loggført. Bruk ID-ene under ved kommentarer og videre revisjon.

## Referansenøkkel

- `V2` = virkningskapittel 2
- `P1` = avsnitt 1
- `S1` = setning 1 i avsnittet
- `T1-R1` = rad 1 i tabell 1

## Godkjent tekst

### V2-P1 — DNSH som del av modellen

<a id="v2-p1-s1"></a>**[V2-P1-S1]** Prosjektet skal bidra til bedre ressursbruk, men det må ikke løse ett problem ved å skape et annet.

<a id="v2-p1-s2"></a>**[V2-P1-S2]** Derfor skal do-not-harm være en del av beslutningsmodellen og piloteringen, ikke bare et kontrollpunkt i et vedlegg.

### V2-P2 — Sammenligning, ikke automatisk valg

<a id="v2-p2-s1"></a>**[V2-P2-S1]** Modellen skal ikke automatisk utpeke ett alternativ som best.

<a id="v2-p2-s2"></a>**[V2-P2-S2]** Den skal vise avveininger, usikkerhet og mulige negative konsekvenser ved hvert alternativ.

<a id="v2-p2-s3"></a>**[V2-P2-S3]** Lavt klimagassutslipp skal ikke skjule kort levetid, svak dokumentasjon eller høy teknisk risiko.

<a id="v2-p2-s4"></a>**[V2-P2-S4]** Lav pris skal heller ikke skjule høyt vedlikeholdsbehov, hyppige utskiftninger eller større risiko for avvik.

### V2-P3 — Operative DNSH-regler

<a id="v2-p3-s1"></a>**[V2-P3-S1]** Hver identifisert risiko skal knyttes til en modellregel, en reaksjon og en test i piloten.

| ID | Risiko | Modellregel | Reaksjon | Hvordan det testes |
| --- | --- | --- | --- | --- |
| **V2-T1-R1** | Lavt CO₂, men svak levetid eller teknisk risiko | Levetid, vedlikehold og teknisk risiko vises separat | Tydelig advarsel og synlig avveining | Test om brukeren oppdager konflikten mellom kriteriene |
| **V2-T1-R2** | Lav pris, men økt materialbruk eller utskifting | Nyanskaffelse sammenlignes med reparasjon, vedlikehold, rehabilitering og ombruk der det er relevant | Advarsel dersom kortsiktig pris skjuler høyere livsløpsbelastning | Sammenlign livsløpskostnad og beregnet ressursbruk |
| **V2-T1-R3** | Manglende nødvendig produktdokumentasjon | Alternativet kan ikke få status som verifisert | Stopp eller tydelig uavklart status | Registrer manglende dokumentasjon og om den kan suppleres |
| **V2-T1-R4** | Generelle eller estimerte data framstår som sikre | Datastatus og usikkerhet vises for hvert relevant datapunkt | Lavere dokumentasjonstillit og synlig forbehold | Test om brukeren oppdager usikkerheten |
| **V2-T1-R5** | Store leverandører favoriseres av bedre dokumentasjon | Produktprestasjon og dokumentasjonskvalitet vurderes separat | Manglende dokumentasjon gir usikkerhet, ikke automatisk svak produktprestasjon | Kontroller at samme mangel ikke straffes i begge dimensjoner |
| **V2-T1-R6** | Systemet gir økt rapporteringsbyrde for små bedrifter | Tidsbruk og behov for dobbelregistrering måles | Krav om forenkling dersom arbeidsbelastningen blir for høy | Sammenlign tidsbruk med vanlig tilbudsarbeid |
| **V2-T1-R7** | Person- eller kredittdata brukes i banksporet | Bare prosjekt- og produktdokumentasjon tillates | Stopp for personprofilering og automatisk kredittbeslutning | Kontroller datakilder, tilgang og lagring |
| **V2-T1-R8** | Ombruk uten dokumentert teknisk egnethet | Egnethet, restlevetid, transport og ansvar må dokumenteres | Alternativet presenteres ikke som forsvarlig ombruk uten nødvendig grunnlag | Kontroller dokumentasjonskravene i piloten |
| **V2-T1-R9** | Kjemikalie-, helse- eller sikkerhetsfare overses | Lavt CO₂ skal ikke overstyre dokumenterte krav | Advarsel eller stopp ved manglende obligatorisk dokumentasjon | Kartlegg hvilke opplysninger som finnes og hvilke som ligger utenfor modellen |
| **V2-T1-R10** | Reparasjon eller vedlikehold brukes uten reell effekt | Utsatt utskifting, spart materiale og teknisk forsvarlighet må dokumenteres | Alternativet merkes som udokumentert dersom virkningen ikke kan beregnes | Sammenlign mot nyanskaffelse og dokumenter forutsetningene |
| **V2-T1-R11** | Effekter påstås uten baseline | Hver effekt kobles til baseline, indikator, datakilde og måleansvarlig | Effekten kan ikke rapporteres som dokumentert uten dette | Kontroller måleplanen før pilotstart |

### V2-P4 — Felles datastatus

<a id="v2-p4-s1"></a>**[V2-P4-S1]** Datastatus skal vise om en opplysning mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen.

<a id="v2-p4-s2"></a>**[V2-P4-S2]** En usikker eller generell opplysning skal ikke framstilles med samme presisjon som en produktspesifikk, verifisert opplysning.

<a id="v2-p4-s3"></a>**[V2-P4-S3]** Leverandører skal kunne supplere eller korrigere dokumentasjonen før vurderingen låses.

### V2-P5 — Falsk presisjon og følsomhet

<a id="v2-p5-s1"></a>**[V2-P5-S1]** En poengsum kan virke sikrere enn datagrunnlaget er.

<a id="v2-p5-s2"></a>**[V2-P5-S2]** Prosjektet skal derfor vise datakilder, datakvalitet, antakelser og begrensninger.

<a id="v2-p5-s3"></a>**[V2-P5-S3]** Det skal også testes hvor følsomt resultatet er for endrede vekter, manglende data og alternative forutsetninger.

<a id="v2-p5-s4"></a>**[V2-P5-S4]** Dersom små endringer gir en annen rangering, skal dette vises for brukeren.

### V2-P6 — Avgrensning av kjemikalier og sosiale forhold

<a id="v2-p6-s1"></a>**[V2-P6-S1]** Prosjektet skal kartlegge hvilke kjemikalie-, helse- og sikkerhetsopplysninger som finnes i EPD, FDV og annen produktdokumentasjon, og tydelig vise når nødvendig informasjon mangler eller ligger utenfor modellen.

<a id="v2-p6-s2"></a>**[V2-P6-S2]** Prosjektet skal også avklare hvilke sosiale og leverandørrelaterte forhold som kan dokumenteres gjennom tilgjengelige produkt- og prosjektdata.

<a id="v2-p6-s3"></a>**[V2-P6-S3]** Forhold modellen ikke kan kontrollere, skal beskrives som utenfor vurderingsgrunnlaget og skal ikke framstilles som verifisert.

### V2-P7 — Beslutningsansvar

<a id="v2-p7-s1"></a>**[V2-P7-S1]** VERIFIED skal være beslutningsstøtte, ikke en automatisk beslutningstaker.

<a id="v2-p7-s2"></a>**[V2-P7-S2]** Modellen skal ikke profilere personer eller ta kredittbeslutninger.

<a id="v2-p7-s3"></a>**[V2-P7-S3]** Endelig faglig og kommersiell vurdering ligger hos aktørene som bruker grunnlaget.

## Åpne porter før innfletting

- Obligatoriske dokumentasjonskrav og faktiske stoppregler må defineres per produktkategori.
- Det må avklares hvem som godkjenner DNSH-reglene og eventuelle unntak.
- Hver tabellrad må kobles til arbeidspakke, datakilde og målepunkt.
- Sosiale minstekrav må avgrenses mot det datagrunnlaget prosjektet faktisk har tilgang til.
- Endringen må føres i endringsloggen når teksten flettes inn i det kanoniske kapitlet.
