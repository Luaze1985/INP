---
title: Konsistenskontroll — godkjente arbeidsversjoner K1–K4 og V1–V3
dato: 2026-07-25
versjon: 0.1
status: reviewnotat, ingen kanoniske filer endret
omfang: k1, k2, k3, k4, v1, v2, v3
---

# Konsistenskontroll — godkjente arbeidsversjoner

## Kort dom

De sju arbeidsversjonene har nå en sammenhengende hovedretning:

- VERIFIED sammenligner og forklarer alternative løsninger, men tar ikke beslutningen.
- FoU-høyden ligger i dataintegrasjon, vekting, datakvalitet, usikkerhet, forklarbarhet og målt beslutningseffekt.
- Bærekraft måles mot baseline, og langsiktige virkninger skilles fra direkte pilotmålinger.
- Banksporet skal bygge på prosjekt-, produkt- og byggdokumentasjon uten personprofilering.
- Do-not-harm skal være en operativ del av modell og pilotering.

Tekstene bør ikke flettes inn i de kanoniske kapitlene før avvikene under er håndtert.

## C1 — Bankomfang er ikke helt samordnet

**Steder:** `K2-P6-S5`, `K2-P6-S6`, `K3-F5`, `V3-P5-S1`–`V3-P5-S4`.

**Avvik:** K2 nevner banker og forsikringsselskaper. K3 og V3 er godkjent med bank som eneste konkret mottaker.

**Anbefalt retting:** Kjerneprosjektet avgrenses til ett konkret bankbehov. Forsikring og takst omtales bare som mulige senere skaleringsspor.

**Prioritet:** Høy.

## C2 — Plattformens rolle bruker to formuleringer

**Steder:** `K2-P4-S2`, `K3-P4-S3`.

**Avvik:** K2 sier «mulig test- og integrasjonsflate». K3 sier «kan brukes som testflate».

**Anbefalt retting:** Bruk konsekvent: «VIBS-plattformen kan brukes som testflate for prosjektet.» Vent med «integrasjonsflate» til dataflyt og arkitektur er definert.

**Prioritet:** Middels.

## C3 — Ombruk og teknisk kvalitet mangler i hovedmålets kriterieliste

**Steder:** `K3-P1-S2`, `K3-F3`, `K4-P3-S1`, `V1-P2-S2`.

**Avvik:** Hovedmålet i K3 nevner pris, klima, levetid, vedlikehold, dokumentasjon og risiko. Senere kapitler inkluderer også ombruk og teknisk kvalitet.

**Anbefalt retting:** Utvid `K3-P1-S2` med «teknisk kvalitet og ombruk», eller bruk en kortere formulering som viser til prosjektets definerte kriterier.

**Prioritet:** Middels.

## C4 — K4 mangler et tydelig målepunkt for FoU-spørsmål F3

**Steder:** `K3-F3`, `K4-T1`, `V1-T1-R2`, `V2-T1-R8`, `V2-T1-R10`.

**Avvik:** K3 spør om avveining mellom ombruk, reparasjon, vedlikehold, rehabilitering og nyanskaffelse. V1 og V2 har relevante indikatorer og regler, men K4s hovedtabell har ingen egen rad som tydelig dekker dette forskningsspørsmålet.

**Anbefalt retting:** Legg til et målepunkt i K4: «Sirkulær sammenligning — materialmengde, restlevetid, teknisk egnethet og beregnede utskiftninger for nyanskaffelse, reparasjon, rehabilitering og ombruk.»

**Prioritet:** Høy.

## C5 — F6 blander forskningsspørsmål og systembygging

**Steder:** `K3-F6`, `K4-T1-R8`.

**Avvik:** K3 spør om dataflyt og API-er kan «bygges», mens K4 måler hvilke deler som kan overføres til en ny produktkategori.

**Anbefalt retting:** Formuler F6 som utforming og testing: «Hvordan kan dataflyt, dokumentasjon og nødvendige grensesnitt utformes og testes slik at modellen er etterprøvbar og kan overføres til en ny produktkategori?»

**Prioritet:** Middels.

## C6 — Datastatus er innholdsmessig lik, men bør få én fast ordlyd

**Steder:** `K4-P2-S4`, `V1-T1-R6`, `V2-P4-S1`.

**Anbefalt standard:** «mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen».

**Prioritet:** Lav.

## C7 — Arbeidsversjonene er ikke ferdig sidekomprimert

De sju tekstene er laget for vurdering og adresserbar revisjon. De skal ikke flettes ordrett inn som endelig prosjektbeskrivelse. En senere komprimeringsrunde må:

- fjerne gjentakelser mellom K2, K3, K4, V1 og V2;
- beholde full metodekobling mellom FoU-spørsmål og målepunkter;
- legge inn bare verifiserte eller korrekt forbeholdne kildehenvisninger;
- tilpasses samlet sidebudsjett sammen med arbeidspakker og gjennomføring.

**Prioritet:** Høy før innfletting.

## Anbefalt rekkefølge

1. Rett C1 og C4.
2. Samordne C2, C3 og C5.
3. Standardiser C6.
4. Gjør en egen komprimerings- og kildepass.
5. Først deretter vurderes innfletting i kanoniske kapitler og eventuell pull request.
