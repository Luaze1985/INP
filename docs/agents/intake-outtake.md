# Agenter for intake, outtake og SINTEF-forberedelse

Denne arbeidsmodellen brukes når research, agentsvar eller SINTEF-svar skal
tas inn, avstemmes og føres videre uten at arbeidsnotater blir en ny
sannhetskilde.

Detaljerte maler, startprompter og aktive utkast ligger i
`.scratch/agent-intake-outtake-2026-08/`. Run-artefakter ligger alltid i
`.scratch`; denne filen er den varige rolle- og styringsbeskrivelsen.

## Styrende prinsipper

- `AGENTS.md`, `CONTEXT.md`, kildedommen og dokumenthierarkiet gjelder foran
  agentresultater.
- Perplexity-, Sonar- og agentsvar er kontrollgrunnlag, ikke selvstendig
  belegg.
- Bare Lars kan godkjenne kildestatus, pensjonering, tekstendring, mottakere
  og sending.
- `ipn-verified` eier søknad og faggrunnlag. `vibs-boligpass/src` og `api`
  eier sannheten om produktets faktiske funksjoner.
- «Ikke funnet» betyr `NOT-FOUND-IN-SCOPE`, ikke at noe ikke finnes.
- Gamle `.agents`-godkjenninger er historisk proveniens og må kontrolleres mot
  senere funn før de gjenbrukes.

## Roller

| ID | Rolle | Hovedleveranse |
| --- | --- | --- |
| A0 | Intake/outtake-orkestrator | Plan, eierskap, gate-status og samlet handoff |
| A1 | Inntaksforvalter og proveniensvakt | Inntaksinventar og routing av faktisk mottatt materiale |
| A2 | Kilde-, alias- og påstandsavstemmer | Kildeavstemming uten statusendring |
| A3 | Konkurrent- og markedsavstemmer | Ensartet, datert funksjons- og markedsavstemming |
| A4 | Søknads-, sannhetsserum- og påstandskartlegger | Tørrkjørt konsekvenskart mot tekstene |
| A5 | VIBS/VERIFIED-grensekontrollør | Kontroll av finnes, under bygging og veikart/hypotese |
| A6 | SINTEF-pakkebygger | Interne utkast til avgrensede mottakerpakker |
| A7 | Pensjonerings- og outtake-kartlegger | Reversibelt outtake-/sperrepostkart, ingen utførelse |
| A8 | Uavhengig sannhets- og integritetsauditor | Audit med `PASS`, `PASS-WITH-OPEN-ITEMS` eller `BLOCK` |

## Kjørerekkefølge

```text
A0
  -> A1
  -> A2 + A3 + A5
  -> A4
  -> A6 + A7
  -> A8
  -> Lars
```

A2, A3 og A5 kan kjøres parallelt etter A1. A6 og A7 kan kjøres parallelt
etter A4. A8 skal være et uavhengig pass og skal ikke rette leveransen selv.

## Filkontrakt

Hver kjøring bruker:

`.scratch/agent-intake-outtake-2026-08/runs/<run-id>/<rolle>/`

Hver rolle eier bare sin mappe og leverer:

- `BRIEFING.md` med mandat, input, write-set og stoppregler;
- `progress.md` med faktisk leste filer og åpne punkter;
- ett navngitt domeneprodukt;
- `handoff.md` med funn, usikkerhet, ikke undersøkt og neste mottaker.

`ORIGINAL_REQUEST.md` opprettes én gang på run-nivå. Ingen agenter
overskriver andres produkter. Orkestratoren peker til dem i stedet for å lage
en ny kildedom.

## Felles stoppregler

Agenten stopper og eskalerer når arbeidet vil:

- endre kildeport, kildedom eller aktiv søknadstekst;
- velge mellom motstridende autoritative dokumenter;
- slå sammen uklar kildeidentitet eller alias;
- formulere negativt søke- eller markedsfunn som absolutt fravær;
- slette, flytte eller pensjonere materiale;
- sende noe eksternt;
- endre eller deploye produktet;
- kreve `.env`, credentials eller betalingsmurbeskyttet original.

## Godkjenningsporter

1. **Scope:** input, write-set og ikke-mål er eksplisitte.
2. **Intake:** alt mottatt er klassifisert; hull er synlige og ikke gjettet.
3. **Avstemming:** kilder, konkurrenter og produktstatus bruker separate
   bevisklasser.
4. **Konsekvens:** hver berørt påstand har filpeker og foreslått behandling;
   målfilene er urørt.
5. **Outtake:** SINTEF-filer er interne utkast og opprydding er tørrkjøring.
6. **Audit:** faktisk diff og styringsregler er kontrollert uavhengig.
7. **Lars:** først menneskelig godkjenning kan autorisere neste endrings- eller
   sendefase.

## Obligatorisk Source Guard

Før A1 ruter et nytt inntak, kjøres:

```powershell
python tools/source_guard.py scan --path <mottatt-fil> --report <run-mappe>/source-guard.json
```

- `PASS`: vanlig intake kan fortsette.
- `BLOCK`: råmaterialet kan bevares urørt, men treffet legges i karantene og
  skal ikke føres til aktiv kilde, påstand, søknad eller nettside.
- `ERROR`: kjøringen stopper; ingen agent skal anta at fravær av rapport betyr
  at materialet er rent.

A4 og A8 kjører i tillegg `python tools/source_guard.py scan --active`.
Eksisterende treff rapporteres som åpen gjeld til endringskartet er gjennomført.
Bare Lars kan gjenåpne via `governance/source-blocklist.json`.
