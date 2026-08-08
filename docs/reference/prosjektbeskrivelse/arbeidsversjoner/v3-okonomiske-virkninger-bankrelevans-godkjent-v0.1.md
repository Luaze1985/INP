---
title: V3 — Økonomiske virkninger og bankrelevans — godkjent arbeidsversjon
dato: 2026-07-25
versjon: 0.1
status: godkjent arbeidsversjon, ikke innsendingsklar
kilde: ChatGPT Work-gjennomgang, godkjent av Lars Erik
kanonisk_kapittel: ../v3-okonomi.md
formaal: Stabil referanse med faste avsnitts-, setnings- og tabell-ID-er
---

# V3 — Økonomiske virkninger og bankrelevans

> Denne filen er en godkjent arbeidsversjon. Den erstatter ikke det kanoniske kapitlet før endringen er flettet inn og loggført. Bruk ID-ene under ved kommentarer og revisjoner.

## Godkjent tekst

### V3-P1 — Hovedavgrensning

<a id="v3-p1-s1"></a>**[V3-P1-S1]** VERIFIED skal først og fremst løse et byggproblem.

<a id="v3-p1-s2"></a>**[V3-P1-S2]** Banksporet er en mulig anvendelse av bedre byggdata, ikke et eget hovedspor.

### V3-P2 — Virkninger for entreprenøren

<a id="v3-p2-s1"></a>**[V3-P2-S1]** For entreprenøren skal prosjektet undersøke om beslutningsgrunnlaget påvirker tidsbruk, tilbudskvalitet, dokumentasjonsmangler og observerbare avvik.

<a id="v3-p2-s2"></a>**[V3-P2-S2]** Faktisk effekt på omarbeid og reklamasjoner kan bare vurderes dersom pilotperioden og datagrunnlaget gjør det mulig.

### V3-P3 — Virkninger for kunden

<a id="v3-p3-s1"></a>**[V3-P3-S1]** For kunden skal modellen vise anskaffelseskostnad, beregnede livsløpskostnader, relevante tekniske forskjeller og usikkerhet ved alternativene.

<a id="v3-p3-s2"></a>**[V3-P3-S2]** Prosjektet skal teste om kunden forstår denne informasjonen og hvordan den påvirker valget.

### V3-P4 — Kunnskapsgrunnlag og FoU-hull

<a id="v3-p4-s1"></a>**[V3-P4-S1]** Det finnes forskning som kobler energieffektivitet til lavere misligholdsrisiko i boliglån.

<a id="v3-p4-s2"></a>**[V3-P4-S2]** Det finnes også europeiske bank- og ESG-rammer som etterspør bedre dokumentasjon, men disse er i stor grad energisentrerte.

<a id="v3-p4-s3"></a>**[V3-P4-S3]** Den gjennomførte kunnskapskartleggingen har ikke identifisert tilsvarende dokumentasjon for sammenhengen mellom byggteknisk kvalitet, levetid, vedlikeholdsbehov og bankens risikovurdering.

<a id="v3-p4-s4"></a>**[V3-P4-S4]** Dette behandles derfor som et FoU-spørsmål, ikke som en etablert sammenheng.

### V3-P5 — Avgrenset bankpilot

<a id="v3-p5-s1"></a>**[V3-P5-S1]** Prosjektet skal undersøke om dokumentasjon av byggteknisk kvalitet, levetid og vedlikeholdsbehov kan struktureres som relevant tilleggsinformasjon for et avgrenset behov hos en bank.

<a id="v3-p5-s2"></a>**[V3-P5-S2]** Banken må før piloteringen definere hvilken informasjon den trenger, hvordan informasjonen skal vurderes, og hva som skal regnes som et nyttig resultat.

<a id="v3-p5-s3"></a>**[V3-P5-S3]** Grunnlaget skal bare bygge på produkt-, prosjekt- og byggdokumentasjon.

<a id="v3-p5-s4"></a>**[V3-P5-S4]** Det skal ikke brukes til personprofilering eller automatiske kredittbeslutninger.

## V3-T1 — Foreslåtte målepunkter

| ID | Virkning som testes | Målepunkt |
| --- | --- | --- |
| **V3-T1-R1** | Tidsbruk i tilbud | Tid med og uten beslutningsgrunnlaget |
| **V3-T1-R2** | Tilbudskvalitet | Fullstendighet og synliggjorte alternativer |
| **V3-T1-R3** | Livsløpsøkonomi | Anskaffelse, vedlikehold og beregnede utskiftninger |
| **V3-T1-R4** | Dokumentasjonskvalitet | Manglende, generelle, estimerte og verifiserte opplysninger |
| **V3-T1-R5** | Kundens forståelse | Forståelse av kostnad, risiko og usikkerhet |
| **V3-T1-R6** | Bankrelevans | Om dokumentasjonen svarer på bankens forhåndsdefinerte informasjonsbehov |

## Kilde- og avgrensningsnotat

- `[Billio2022]` og `[Kaza2014]` brukes for energi og boliglånsrisiko.
- `[An2020]` gjelder kommersiell eiendom/CMBS og må ikke brukes som boligpåstand.
- Sammenhengen mellom holdbarhet og bankrisiko er en hypotese som skal undersøkes.
- Forsikring og takst er tatt ut av denne arbeidsversjonen og kan eventuelt behandles som senere skaleringsspor.
- Generell samfunnsøkonomisk effekt er ikke dokumentert i dette kapitlet.

## Åpne porter før innfletting

- Banken må definere ett konkret informasjonsbehov og ett vurderingspunkt.
- Måleopplegget må kobles til K3-F5 og K4s pilotmetode.
- `[An2020]` må fulltekstkontrolleres dersom konkrete tall skal brukes.
- Endringen må føres i endringsloggen når teksten flettes inn i det kanoniske kapitlet.
