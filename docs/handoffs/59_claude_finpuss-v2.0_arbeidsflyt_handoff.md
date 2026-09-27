---
title: Handoff (CLAUDE) - Fortsett finpuss av v2.0 med feltkort, grilling og språkvask
date: 2026-09-27
status: ready
from: claude
to: claude
branch: main (ingenting committet)
tags: [vibs, verified, ipn, soknadstekst, finpuss, sprakvask, arbeidsflyt]
---

# Handoff (CLAUDE): Fortsett finpussen av søknadstekst v2.0

## Kort beskjed

Alle tekstfelt utenfor arbeidspakkene er finpusset og språkvasket 27.09
(F1–F24). Hovedideen er låst, og det samme er begrepene. Du skal gjøre ferdig det
som gjenstår med samme arbeidsflyt. Fristen er onsdag. AP-kostnader, budsjett og
partnerbekreftelser venter på andre, så de er ikke din jobb nå. Du skal ikke gjenåpne
beslutninger som står i loggen.

## Rollefordeling (ærlighetsregel)

- **Claude (deg):** Lager feltkort, griller Lars kort, skriver tekst, kjører
  språkvask og gater, og logger.
- **Claude (forrige økt):** Gjennomførte F1–F24 og skrev denne handoffen.
- **Lars Erik:** Tar alle beslutninger. Han er ofte på mobil, skriver med
  talegjenkjenning og vil ha korte, klare spørsmål.

## Inndata (les i denne rekkefølgen)

1. `docs/reference/prosjektbeskrivelse/reviews/2026-09-27-finpuss-v2.0.md`
   Hovedloggen. Her står kjernebudskapet, prioriteringen, F1–F24 med kilder og
   «Status for ny økt». **Dette er fasiten for hva som er bestemt.**
2. `docs/reference/prosjektbeskrivelse/reviews/2026-09-27-hva-er-verified-analyse.md`
   Logikken i fem ledd: prisen vinner og reparasjon taper, mer data kommer
   (produktpass), og datatillit er det som mangler. Hvor VERIFIED står i den
   større kjeden. Hva som var ulogisk.
3. `CONTEXT.md` seksjonen «Låst begrepsbruk». Den definerer VERIFIED,
   løsningsvalg og VIBS (i søknaden), og den sier hvilke ord som skal unngås.
4. `skills/ai-sprakvask-no/SKILL.md` og særlig «KI-trekk å se etter». Lars krever
   at dette kjøres før tekst vises eller skrives inn.
5. `docs/reference/prosjektbeskrivelse/reviews/2026-09-27-anti-slop-analyse.md`
   Tellingen per felt, slik den så ut før vask runde 2.
6. `docs/reference/prosjektbeskrivelse/reviews/2026-09-24-grillingsbeslutninger-v2.0.md`
   B1–B7. B4 er delvis opphevet av F23.
7. `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v2.0.md`
   Selve teksten. Den redigeres på stedet, fordi alle verktøy har stien
   hardkodet. Sikkerhetskopi fra morgenen 27.09 ligger i `C:/tmp/finpuss-2026-09-27/`.

## Arbeidsflyten (arbeidsøkt per felt)

Dette er arbeidsmåten Lars godkjente 27.09. Følg den for hvert felt.

1. **Feltkort.** Lag et kort som får plass på én mobilskjerm. Det skal si hva
   portalen ber om (feltveiledningen og tegngrensen står i
   `innsendingspakker/v2.1/portalstruktur.json`), hvilket vurderingskriterium
   feltet teller på (sannhetsserum §10.7), status fra slop-tellingen og kildene,
   og eventuelle konflikter med låste beslutninger.
2. **Grilling.** Still høyst to spørsmål om gangen, bare om det som er Lars'
   beslutning. Skriv anbefalingen først og forklar i én setning hvorfor. Slå opp
   fakta selv i stedet for å spørre. Si det rett ut hvis noe er ulogisk.
   Forklar med et konkret eksempel når han sier at han ikke forstår. Vindueseksempelet
   (reparere eller bytte) har fungert.
3. **Skriv og vask.** Bruk `ai-sprakvask-no` i teamflyt. Unngå oppramsinger med
   3–5 ledd, den logiske trappen («Da …/Derfor …»), gjentatte kontrastfigurer,
   tankestreker, kolon brukt retorisk og slagordsavslutninger. Ikke legg til
   faktapåstander uten kilde fra kildebiblioteket eller sannhetsserumet.
4. **Gater etter hver endring.** Alle fire må være grønne:
   - `py -m pytest -q` skal gi 54 passed.
   - `py tools/build_verified_v21_portal_draft.py` skal gi 0 over limit.
   - `py tools/source_guard.py scan --path <v2.0.md>` skal gi PASS.
   - `py scripts/verify_nfr_submission.py <v2.0.md>` skal gi SUKSESS.

   Tegn telles med `py tools/tegn_per_felt.py`, slop med
   `py tools/slop_telling.py`, og et helt felt byttes med
   `py tools/bytt_felt.py "<Felt>" "<Neste felt>" <tekstfil>`.
5. **Logg.** Legg til en ny F-rad i finpuss-loggen med hva som ble gjort, hvorfor
   og kilde, og oppdater «Status for ny økt». Svar Lars med én linje per felt.

Lars ønsker det mest effektive: samle flere feltkort i ett skjema
(grill-me-with-forms) som han fyller ut på mobil og limer tilbake. Spør ham om
det før en stor runde.

## Det som gjenstår

1. **AP1–AP7, beskrivelser og milepæler.** Samkjør med beslutningene:
   - T1.3 i AP1 skal nevne at minst ett alternativ i hvert case er reparasjon,
     rehabilitering eller ombruk (F1, F8).
   - AP5 har fått insentivtesten (F11) og sier 3 caser (B7).
   - «VIBS» står i mange AP-felt. I teksten betyr det selskapet, og det er
     tillatt. Vurder om det skal byttes med «prosjektansvarlig».
   - Språkvask.
2. **Kjønnsperspektiver.** Feltet er ikke vasket. Det har lite slop, så bare
   bekreft det.
3. **Hovedmål og Behov.** Begge har bare fått vask runde 1. Hovedmål ligger på
   496/500 og har lite rom.
4. **Leseversjonen** (`VERIFIED-soknadstekst-v2.0-lesbar.md`) har fortsatt
   merkene «[endret 24.09]». Word-filen `soknadstekst-samlet-kandidat-v2.0.docx`
   er bygget 27.09 og er den Lars leser.
5. **Venter på andre, ikke din jobb nå:**
   - Kostnadsspesifikasjoner, Gjennomføringsplan og budsjett. B6 er ikke fordelt
     på AP4–AP7.
   - Personer i Kompetanse. Lars legger inn navnene under Roller i portalen, og
     teksten er skrevet på organisasjonsnivå, så han slipper flere e-poster.
   - Skriftlige partnerbekreftelser.

## Ikke-mål

- Ikke gjenåpne kjernebudskapet, F1–F24 eller B1–B7 (bortsett fra der F23 har
  opphevet B4).
- Ikke skriv «stopp-regel» som navn på metoden, «avgjør», «VIBS-plattformen» eller
  at banker er med.
- Ikke lov en standard. Standarden er et langsiktig mål som prosjektet gir
  grunnlag for (F4).
- Ikke bruk ISO 25737-1 eller de 🟡-merkede bransjetallene (BDO 3,3 %, 1 583
  konkurser) som belegg.
- Ikke skriv status før innsending, som manglende bekreftelser eller manglende
  casetilgang, inn i søknaden som usikkerhet eller risiko. Søknaden beskriver bare
  risiko i prosjektperioden (F25).
- Ikke commit uten at Lars ber om det.
- Ikke bruk egen kunnskap som belegg. Bare åpen sitering gjelder (jf. `AGENTS.md`).

## Akseptansekriterier

1. Hver felt-endring har en F-rad i finpuss-loggen.
2. De fire gatene er grønne etter siste endring.
3. Ingen ny tekst bryter «KI-trekk å se etter» (sjekk med `tools/slop_telling.py`).
4. Word-filen er bygget på nytt med
   `node tools/build_verified_v20_application_docx.cjs` og sendt til Lars.

## Startprompt (lim inn til Claude)

```text
Les docs/handoffs/59_claude_finpuss-v2.0_arbeidsflyt_handoff.md og deretter
docs/reference/prosjektbeskrivelse/reviews/2026-09-27-finpuss-v2.0.md.

Vi fortsetter finpussen av VERIFIED-søknaden (v2.0) med samme arbeidsflyt:
feltkort, kort grilling med anbefaling først, språkvask med
skills/ai-sprakvask-no, fire gater og logging. Neste er AP1–AP7 beskrivelser
og milepæler. Samkjør dem med F1, F8, F11 og B7, og vask språket. Jeg er på mobil:
still korte, klare spørsmål og bruk konkrete eksempler.
```
