# Innsendingspakker for VERIFIED

Denne mappen er fast hjem for portaltilpassede søknadsversjoner fra og med
v2.0. En innsendingspakke samler portalstruktur, feltkart, ren innlimingstekst,
manuelle registreringer og endringslogg for samme versjon.

## Gjeldende pakke

- **Arbeidsversjon:** [`v2.0/`](v2.0/)
- **Tekstgrunnlag:**
  [`../soknadstekst-samlet-kandidat-v1.7-if-only.md`](../soknadstekst-samlet-kandidat-v1.7-if-only.md)
- **Status:** Struktur- og kartleggingsfase. Ikke innsendingsklar og ikke
  godkjent for registrering i Forskningsrådets portal.
- **Beslutningseier:** Lars.

V1.7 ligger urørt på sin opprinnelige plass og er historisk utgangspunkt for
v2.0. Opprettelsen av v2.0 flytter ikke aktiv Source Guard-kandidat.

## Innhold i hver versjon

| Fil | Formål |
| --- | --- |
| `portalstruktur.json` | Maskinlesbart kart over portalens felt, grenser, valg og registreringsflyter. |
| `feltkart.md` | Kobling mellom portalens felt og tekstgrunnlaget, med gap og avklaringer. |
| `innlimingsmal.md` | Portalens eksakte tekstfelt i riktig rekkefølge. Bare godkjent innlimingstekst skal stå under overskriftene. |
| `manuelle-registreringer.md` | Opplysninger som må registreres gjennom valg, menyer, datoer og repeterende skjema. |
| `endringslogg.md` | Sporbar logg over endringer, grunnlag, kontroll og godkjenning. |

## Versjonsregler

1. En ny hovedpakke opprettes som en ny søskenmappe, for eksempel `v2.1/`
   eller `v3.0/`. En godkjent pakke overskrives ikke.
2. Feltkart og innlimingsmal skal alltid ha samme versjonsnummer og vurderes
   samlet.
3. `portalstruktur.json` er foreløpig et video-uttrekk og er ikke manuelt
   verifisert. Uklare felt, valg og tegnbegrensninger skal merkes; de skal ikke
   gjettes.
4. Kontrollstatus og arbeidsnotater hører hjemme i feltkartet,
   registreringsfilen og endringsloggen. De skal ikke inn i innlimingsmalen.
5. Ubekreftede påstander skal ikke inn i innlimingsmalen. Kilde- og
   sannhetsreglene i prosjektets `AGENTS.md` gjelder uendret.
6. Lars godkjenner når en pakke blir gjeldende. Source Guard flyttes bare ved
   en egen, uttrykkelig beslutning.

