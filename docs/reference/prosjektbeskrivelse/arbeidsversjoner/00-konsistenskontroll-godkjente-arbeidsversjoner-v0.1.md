---
title: Konsistenskontroll — godkjente arbeidsversjoner K1–K4 og V1–V3
dato: 2026-07-25
versjon: 0.2
status: C1–C6 rettet i arbeidsversjonene, ingen kanoniske filer endret
omfang: k1, k2, k3, k4, v1, v2, v3
---

# Konsistenskontroll — godkjente arbeidsversjoner

## Kort dom

De sju arbeidsversjonene har nå en sammenhengende hovedretning:

- VERIFIED sammenligner og forklarer alternative løsninger, men tar ikke beslutningen.
- FoU-høyden ligger i dataintegrasjon, vekting, datakvalitet, usikkerhet, forklarbarhet og målt beslutningseffekt.
- Bærekraft måles mot baseline, og langsiktige virkninger skilles fra direkte pilotmålinger.
- Banksporet er avgrenset til ett konkret informasjonsbehov basert på prosjekt-, produkt- og byggdokumentasjon uten personprofilering.
- Do-not-harm er en operativ del av modell og pilotering.
- VIBS-plattformen omtales konsekvent som mulig testflate for prosjektet.

## Resultat av C1–C6

| ID | Tema | Status | Retting |
| --- | --- | --- | --- |
| C1 | Bankomfang | Rettet | K2, K3 og V3 er avgrenset til ett konkret bankbehov. Forsikring og takst er bare mulige senere skaleringsspor. |
| C2 | Plattformrolle | Rettet | K2 og K3 bruker formuleringen «VIBS-plattformen kan brukes som testflate for prosjektet». |
| C3 | Kriterier i hovedmålet | Rettet | K3 inkluderer nå teknisk kvalitet og ombruk. |
| C4 | Målepunkt for F3 | Rettet | K4 har fått `K4-T1-R9` for sirkulær sammenligning. |
| C5 | F6 forskning/systembygging | Rettet | F6 handler nå om hvordan dataflyt, dokumentasjon og grensesnitt kan utformes og testes. |
| C6 | Datastatus | Rettet | K4, V1 og V2 bruker samme fire nivåer. |

## Felles datastatus

Den godkjente ordlyden er:

> Opplysningen mangler, bygger på generelle data, er estimert eller er verifisert for den konkrete løsningen.

Denne ordlyden skal brukes konsekvent i modellbeskrivelse, metode, pilotmåling og senere UI-tekst.

## Gjenstående kvalitetsport C7 — komprimering og kildepass

Arbeidsversjonene er laget for vurdering og adresserbar revisjon. De skal ikke flettes ordrett inn som endelig prosjektbeskrivelse.

Før innfletting må en egen runde:

1. fjerne gjentakelser mellom K2, K3, K4, V1 og V2;
2. bevare koblingen mellom F1–F6 og målepunktene;
3. kontrollere at hver ekstern påstand har grønn kilde eller korrekt forbehold;
4. skille prosjektets hypoteser fra dokumenterte funn;
5. tilpasse teksten til samlet sidebudsjett sammen med arbeidspakker og gjennomføring;
6. føre endringene i endringsloggen.

## Åpne beslutninger som ikke kan løses med språkvask

- Første produktkategorier og funksjonell enhet.
- Baseline og sammenligningsopplegg.
- Analyseperiode for livsløpskostnader.
- Lars Gunnars konkrete målepunkter for beslutningseffekt.
- Bankens informasjonsbehov og beslutningssituasjon.
- Første MCDA-metode eller sammenligningsopplegg.
- Produktkategori som skal brukes for å teste overførbarhet i F6.

## Anbefalt neste rekkefølge

1. Gjør et kildepass på de bærende påstandene.
2. Lag én komprimert, sammenhengende søknadstekst fra arbeidsversjonene.
3. Kontroller teksten mot sidebudsjett og senere arbeidspakker.
4. Først deretter vurderes innfletting i kanoniske kapitler og eventuell pull request.
