# Skisse — beslutningsgrunnlag for VERIFIED-strukturen (v1.7 / AP1–AP3)

**For:** Lars Erik og Lars Gunnar, felles gjennomgang.
**Grunnlag:** `soknadstekst-samlet-kandidat-v1.7-if-only.md`, `CONTEXT.md`, `budsjett/fordelingsplan.md`, `budsjett/partneroversikt.md` (alle i dette repoet), samt `soknadsstruktur-og-krav.md` og `gjennomforing-struktur-utkast.md` fra den kuraterte pakken `VERIFIED_VS_CODE_GRUNNLAG.zip` (lest, ikke endret). Et eksternt AGY-notat vurderte samsvaret mellom pakken og v1.7; påstandene der er faktasjekket direkte mot kildene under, ikke tatt for gitt.
**Ingen filer er endret som del av dette dokumentet.** Ingen partnernavn, budsjett- eller effekttall er lagt til utover det som står i kildene.

---

## Del 1 — Hva er avklart nå

| Punkt | Avklaring | Kilde |
|---|---|---|
| Rammen | Industriell forskning i AP1–AP3 (36 måneder, 16,0 MNOK, 8,0 MNOK søkt støtte). AP4–AP6 og eksperimentell utvikling inngår ikke. | v1.7, linje 5, 120–125 |
| FoU-spørsmål | F1–F5 gjelder. Det er ikke noe F6 i v1.7. | v1.7, linje 67–71 |
| Bankspor | Fullstendig utelukket — verken som partner, leverandør, referanseaktør eller brukergruppe. | v1.7 linje 274; CONTEXT.md; partneroversikt.md linje 79 |
| Feltuttesting | **Skjer, men ikke i denne søknaden.** v1.7 sier selv at «økonomisk verdi hos bruker» først måles «etter modellfrys i separat pilot» (linje 248), og at AP1 bare skal *forberede* hvordan en senere pilot kan måle effekt (linje 167) — ikke gjennomføre den. AP3 avsluttes med modellfrys, ikke med testing hos snekkere/bygningsfolk. | v1.7 linje 167, 248 |
| Budsjett | 16,0 MNOK totalt, 8,0 MNOK støtte (50 %), 8,0 MNOK egenfinansiering. VIBS-raden er 12,6 MNOK. | fordelingsplan.md linje 17–24 |
| Partnere | SINTEF (FoU-leverandør, juridisk enhet uavklart), Norsk Byggtjeneste AS (data/standard), D Takst AS, Byggmester Espeland AS og Norgesbygg Sør AS (SMB-/pilotcase-kandidater). Axon og BEWI er tatt ut av alle planer. | partneroversikt.md linje 22–24, 64, 79, 108–109 |

**Rettelse av tidligere formulering:** I forrige runde sa jeg at prosjektet «ikke skal teste noe ute i felt». Det var upresist — Lars presiserte: *«Det skal jo testet i felt. På sikt hos snekkere og bygningsfolk.»* Riktig bilde: feltuttesting er planlagt, men som en **senere, separat, ikke-finansiert fase** etter modellfrys — ikke som del av AP1–AP3s leveranser eller akseptkriterier. Dette er allerede v1.7s egen posisjon, ikke noe nytt som må vedtas.

**Konsekvens for pakkedokumentene:** `gjennomforing-struktur-utkast.md` sitt WP4 (demonstrator), WP5 (pilot/beslutningseffekt), WP6 (overførbarhet) og WP7 (utnyttelse/IPR) beskriver nettopp den senere fasen — de er ikke feil, men de hører til **fase 2** (etter modellfrys), ikke til den søknaden som nå skal leveres. `soknadsstruktur-og-krav.md`s F1–F6 og bankspor-avsnitt har samme status: F6 og banksporet hører til fase 2 eller er utelukket helt.

### Slik sjekker dere Del 1 selv

Ikke stol på linjenumrene alene — de forskyver seg hvis noen redigerer filen. Bruk Ctrl+F i `soknadstekst-samlet-kandidat-v1.7-if-only.md` og søk på disse eksakte setningene:

| Punkt | Søk etter (eksakt sitat) |
|---|---|
| Rammen | `Industriell forskning i AP1–AP3. AP4–AP6 og eksperimentell utvikling inngår ikke` |
| FoU-spørsmål | `Hvordan kan modellens sporbarhet, datamangel og følsomhet` (F5 — søk så på `F6`: null treff bekrefter at det ikke finnes) |
| Bankspor | `Banker og andre finansaktører inngår ikke i denne IF-only-kandidaten` |
| Feltuttesting (1) | `Praktisk beslutnings- og kommersiell effekt er ikke et akseptkriterium for modellfrys` |
| Feltuttesting (2) | `Først etter modellfrys i separat pilot` (i måleplan-tabellen, raden «Økonomisk verdi hos bruker») |

Og i `budsjett/`-filene:

| Punkt | Fil | Søk etter |
|---|---|---|
| Budsjett | `fordelingsplan.md` | `Prosjektkostnad \| 16,0 MNOK` og `VIBS-ramme` |
| Partnere (SINTEF) | `partneroversikt.md` | `SINTEF, juridisk enhet uavklart` |
| Partnere (Axon ute) | `partneroversikt.md` | `Tok Axon helt ut av gjeldende partner-` |
| Partnere (BEWI/bank ute) | `partneroversikt.md` | `BEWI, banker og øvrige finansaktører er utenfor` |

Hvis noen av søkene ikke gir treff, er kilden endret siden dette dokumentet ble skrevet (2026-09-12) — da bør dette dokumentet oppdateres, ikke antas fortsatt riktig.

---

## Del 2 — Forbedringsforslag

Rekkefølge etter det dere markerte som viktigst: **fordeling → arbeidspakker → søknadstekst.** Dette er forslag til vurdering, ikke vedtak.

### 2.1 Fordeling — hvem gjør hva, og hvor mye penger (høyest prioritet)

Budsjettrammen (16,0/8,0/8,0 MNOK, AP1 3,0 / AP2 5,5 / AP3 7,5 MNOK) er avstemt og låst. Det som **ikke** er avklart, og som bør prioriteres nå:

1. **VIBS-radens fire underposter (12,6 MNOK) er alle «ikke priset».**
   - Egne personal-/indirekte kostnader: mangler navngitte personer, årslønn, timesats, timer per person/AP og signert bemanningsplan.
   - Innkjøpt FoU fra SINTEF: mangler tilbud fra korrekt juridisk enhet, markedspris, timer, AP-leveranser og rettigheter.
   - Eventuelle rådgiver-/spesialisttjenester og test-/spesialistleveranser: mangler valgt leverandør og tilbud, eller må settes til 0.
   - *Hvorfor dette haster:* uten disse fire postene kan ikke 12,6 MNOK forsvares som annet enn en ramme — det er ikke en reell underfordeling ennå. (Kilde: fordelingsplan.md, §3)
   - *Minste trygge steg:* hent tilbud fra SINTEF og en foreløpig bemanningsplan for VIBS — disse to alene lukker to av fire porter.

2. **Partnerkandidatenes status er «kandidat», ikke bekreftet.** D Takst, Norsk Byggtjeneste, Espeland og Norgesbygg Sør har alle rollekort, men avtale, timer og resultatbruk er ikke bekreftet (fordelingsplan.md linje 22–24). Uten dette kan ikke deres kostnadsbidrag (til sammen ca. 3,4 MNOK) tas med som noe mer enn et foreløpig forslag.
   - *Minste trygge steg:* få skriftlig bekreftelse (selv uforpliktende foreløpig) fra de to nærmeste kandidatene (SINTEF og én SMB-partner) før neste versjon.

3. **Likviditetsplan mangler helt.** 8,0 MNOK egenfinansiering er ikke det samme som kontantbehov — VIBS trenger en betalingsplan (personalkostnader, fakturaer, MVA, NFR-utbetalinger, sikkerhetsmargin) før styret kan godkjenne. (fordelingsplan.md §6)
   - *Minste trygge steg:* dette kan vente til nærmere innsending, men bør ikke glemmes — sett en frist.

### 2.2 Arbeidspakker — hvordan WP1–WP3 (pakken) og AP1–AP3 (v1.7) faktisk henger sammen

Dette er den konkrete sammenligningen dere ba om. **De tre pakkene matcher ikke 1-til-1** — de er delt opp langs forskjellige akser:

| Pakkens WP | Hva den dekker | Faktisk hjemme i v1.7 |
|---|---|---|
| WP1 — Styring, krav og forskningsbaseline | Prosjektkart, rollemodell, **forskningsprotokoll**, målepunktregister, risikobilde | Protokoll-delen hører til **AP1**. Rollemodell og risikobilde er ikke en del av AP1–AP3s forskningsinnhold i det hele tatt — de hører til v1.7s eget kapittel «Foreløpig organisering og økonomi». |
| WP2 — Data og dokumentasjonstillit | Datadictionary, provenansmodell, minimumsinformasjonsgrunnlag, regler for datastatus | Dette **er AP1**, ikke AP2. v1.7s AP1 dekker nøyaktig dette: kildesporing, datakvalitetsklasser, håndtering av manglende data (v1.7 linje 131, 139). |
| WP3 — Beslutningsmodell og usikkerhet | Metodevalg, vektingsregler, sensitivitetsanalyse, forklaringsformat | Dette **spenner over AP2 og AP3**: metodevalg/vekting hører til AP2 («målemodell og harmonisering»), mens sensitivitetsanalyse og forklaringsformat hører til AP3 («usikkerhetsmodell og modellfrys»). |

**Konkret forslag:** ikke bruk WP1–WP3 som en parallell til AP1–AP3 — de er ikke samme inndeling. I stedet:
- Behold AP1–AP3 som den eneste offisielle strukturen i søknaden (det er den som allerede har budsjett, akseptkriterier og porter).
- Bruk pakkens WP2-innhold (datadictionary, provenansmodell) som **utdyping av AP1s andre halvdel** — det er mer presist enn det AP1-teksten har i dag.
- Del WP3s innhold i to og legg metodevalg/vekting inn under **AP2**, og sensitivitetsanalyse/forklaringsformat inn under **AP3** — ikke som én samlet «beslutningsmodell-pakke».
- La WP1s rollemodell og risikobilde bli en utdyping av organiseringskapittelet, ikke av en arbeidspakke.

**Om rolletabellen (RACI) i pakken:** kolonnene «Pilotaktør» og «Kunde/sluttbruker» er ikke feil eller irrelevante — de beskriver fase 2 (feltuttesting etter modellfrys), som faktisk skal skje, bare ikke i denne søknaden. Anbefaling: hvis rolletabellen tas videre, merk de to kolonnene tydelig «Fase 2 — etter modellfrys, ikke finansiert i denne søknaden» i stedet for å fjerne dem. Det holder dem synlige for senere uten at noen leser dem som gjeldende AP1–AP3-ansvar.

### 2.3 Søknadstekst — presisjon

Kortere punkter, lavest prioritet nå:

- `soknadsstruktur-og-krav.md`s krav om å skille «målt, beregnet, estimert og faglig vurdert» er allerede fulgt konsekvent i v1.7 (se effekt-/gevinstkjeden, linje 219–229) — ingen endring nødvendig, bare verdt å vite at v1.7 allerede oppfyller dette kravet.
- Samme dokuments K3-krav om at hvert FoU-spørsmål må kunne spores til data/metode/AP/målepunkt/pilot er delvis oppfylt for F1–F5, men bør sjekkes eksplisitt mot AP-tabellen når WP-innholdet flyttes inn (se 2.2).
- Ingen ny prosa foreslås her — dette er en sjekkliste å bruke når v1.7 revideres videre, ikke en endring nå.

---

## Kilder brukt (alle lest i sin helhet eller i relevante utdrag)

- `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.7-if-only.md`
- `CONTEXT.md`, `AGENTS.md`
- `budsjett/fordelingsplan.md`, `budsjett/partneroversikt.md`
- `soknadsstruktur-og-krav.md`, `gjennomforing-struktur-utkast.md` (fra `VERIFIED_VS_CODE_GRUNNLAG.zip`, lest rent lesende via `unzip -p`, ikke endret)
- AGYs vurdering (limt inn av Lars i chat) — brukt som utgangspunkt, faktasjekket mot kildene over
