# Multiagent-workflow — IPN-søknad VERIFIED

**Dato:** 2026-07-08 · **Ansvarlig:** Lars Erik · **Status:** Fase 0 utført; første røffe K/V-utkast skrevet 2026-07-09
**Formål:** Hvordan de sju kapitlene i prosjektbeskrivelsen skrives, verifiseres og monteres til én PDF.

---

## Kort fortalt

Vi skriver K1–K4 (Kvalitet) og V1–V3 (Virkninger) til ett PDF-utkast som SINTEF overtar
midt i august. Arbeidspakkene er fortsatt parkert.

Flere agenter brukes til **verifisering, review og konsistenssjekk** — ikke til å skrive
kapitlene. Selve prosaen skrives av én drafter med Lars Erik i loopen, kapittel for kapittel.
Det er et bevisst valg, begrunnet i §4.

---

## Beslutninger (Lars Erik, 2026-07-08)

| Spørsmål | Valg |
| --- | --- |
| Hvor arbeidet skjer | `ipn-verified/` — det kanoniske søknadsrepoet |
| Hva PDF-en inneholder | **Kun K1–K4 + V1–V3.** WP1–WP5 og Gjennomføring forblir parkert |
| Kildestatus i PDF-en | **Ren prosa + eget statusvedlegg bakerst** |

---

## Grunnbetingelser som styrer alt annet

**1. Tre av fire kilder kan ikke bære en setning alene.**
Kildebiblioteket står i dag på 22 🟢 · 47 🟡 · 9 🔴 · 5 ⏸. Bare 🟢 kan være bærende
(`AGENTS.md` → kilderegel 2). Dette er ikke en formalitet: det avgjør hvilke kapitler som
i det hele tatt kan skrives nå, og det er derfor kildekartlegging kommer *før* drafting.

**2. Dette blir et røft utkast, ikke en innsendingsklar søknad.**
`ipn-arbeidsplan-juli-aug-2026.md` definerer målet som «komplett, men røft utkast». SINTEF
åpner primærkilder midt i august. En PDF som *ser* ferdig ut ville feilrepresentere
kildestatus. Statusvedlegget er det som holder utkastet ærlig — det er ikke en formalitet
som kan droppes hvis PDF-en skal «se pen ut».

**3. Ingen effektpåstand i presens.**
Arbeidsplanen er eksplisitt: VERIFIED **skal teste og måle** CO₂, kvalitet, risiko og
beslutningseffekt. Det er ikke bevist at effekten finnes. Enhver setning som antyder noe
annet er en feil, uansett hvor god kilden er.

**4. Claude styrer bare Claude.**
Codex og Antigravity får handoff-filer. De styres ikke av noen agent i denne workflowen.
(`AGENTS.md` → ærlighetsregel.)

---

## Kapitlene og sidebudsjettet

Mappen `docs/reference/prosjektbeskrivelse/` er opprettet. Per 2026-07-09 finnes første røffe
utkast for K1–K4 og V1–V3.

| Fil | Innhold | Kilde i hovedokumentet | Side |
| --- | --- | --- | --- |
| `k1-bakgrunn.md` | Problemet i bransjen | §1 | ~1,5 |
| `k2-nyhetsverdi.md` | Hva som er nytt | §3 + SoA §11 gap-matrise | ~2 |
| `k3-forskning.md` | FoU-spørsmål F1–F6 | §2 | ~1,5 |
| `k4-metode.md` | Hvordan vi forsker | *ny — finnes ikke i skjelettet* | ~1,5 |
| `v1-baerekraft.md` | Miljø og bærekraft | §5 | ~1,5 |
| `v2-sikkerhet.md` | Do-not-harm (DNSH) | §5 — første røffe DNSH-utkast skrevet 2026-07-09 | ~1 |
| `v3-okonomi.md` | Samfunnsøkonomi, bank | §5 (bro til grønn finans) | ~1 |

**Merk to hull.** `k4-metode.md` hadde ingen forelder i skjelettet og måtte skrives fra bunn.
`v2-sikkerhet.md` (DNSH-tabellen) var markert **Rød** i `ipn-hovedokument.md:90`. Begge har nå
første røffe utkast, men trenger fortsatt faglig avklaring og konkrete målepunkter.

**Sidespenning:** hovedokumentets budsjett er ~10 sider *inkludert* WP (§4, ~2 s) og
Gjennomføring (§6, ~1 s). K/V-delene får altså ~7 sider i den endelige søknaden. Tabellen
over summerer til ~10. Én av to ting må skje senere: K/V strammes til ~7, eller
sidebudsjettet revideres når WP tas opp igjen. **Ikke løs dette nå** — men ikke skriv 10
sider K/V i den tro at det er endelig format.

---

## Fasene

### Fase 0 — Grunnmur *(Claude alene, ingen fan-out)*

Opprett `docs/reference/prosjektbeskrivelse/` med de sju filene. Hver fil får et hode:
kildenøkler seksjonen skal hvile på, sideanslag, og hvilke av Lars Eriks beslutninger som
blokkerer den.

Dette er trinn 1 i arbeidsplanen, som aldri ble utført.

---

### Fase 1 — Kildekvittering per kapittel *(7 parallelle agenter, read-only)*

Én agent per kapittel. Hver leser kanon — `ipn-hovedokument.md`, `ipn-kildebibliotek.md`,
`vibs-verified-kildedom-2026-06-27.md`, `state-of-the-art-verified-ipn.md` — og leverer for
sitt kapittel:

- hver bærende påstand, én for én
- nøkkel + farge per påstand, **avlest fra kildedommen**
- konsekvens av fargen: 🟢 kan bæres · 🟡 må frases med forbehold · 🔴/⏸ kan ikke brukes
- hva som mangler før kapittelet kan skrives

> **Agenten setter aldri en farge.** Fargen leses fra
> `vibs-verified-kildedom-2026-06-27.md`, som er autoritativ. Oppgaven er å **kartlegge
> eksisterende kildestatus over på den nye sju-kapittelstrukturen** og navngi hullene — ikke
> å vurdere kilder på nytt. Bare SINTEF åpner primærkilder, og agent-konsensus er aldri
> belegg (`AGENTS.md` → kilderegel 1). En agent som «oppgraderer» en 🟡 til 🟢 har begått
> prosjektets alvorligste feil.

Agentene skriver ikke prosa. De produserer strukturert output.

**Dette er en ekte barriere.** Alle sju må ligge på bordet samtidig før drafting, fordi:
- samme påstand kan gå igjen i flere kapitler med *ulik* farge — det må avstemmes
- et kapittel kan vise seg for tynt til å skrives nå, og det må Lars vite før noen skriver

> **Gate G1:** Lars leser de sju kvitteringene og bestemmer hvilke kapitler som skrives nå.

---

### Fase 2 — Drafting *(én drafter + Lars, kapittel for kapittel — ingen fan-out)*

For hvert godkjente kapittel: Claude skriver utkast → Lars leser → Claude justerer.

**Hvorfor ikke parallelle skriveagenter?** Tre grunner, i rekkefølge:

1. **Stemme.** Sju agenter gir sju stemmer. Prosjektbeskrivelsen leses av én person i
   Forskningsrådet som ett dokument.
2. **Lars eier innholdet.** Trinn 4 i arbeidsplanen lister spørsmål bare Lars kan avgjøre
   (SMB-definisjon, hvilke påstander som er hypoteser). Fan-out omgår ham.
3. **Fart er ikke flaskehalsen.** Kildestatus er. Sju kapitler skrevet på ti minutter hjelper
   ikke når 🟡-kildene ikke åpnes før midten av august.

Parallellitet her ville sett produktivt ut og vært verdiløst.

**Blokker som må ryddes først** (arbeidsplanen trinn 4 — krever Lars):
- Definer SMB: antall ansatte + andel av bransjen (tall fra SSB/NHO)
- Hvilke påstander er vi sikre på, hvilke er hypoteser? *(gjelder hele søknaden)*
- SMB-entreprenørene er fagfolk, ikke ikke-spesialister — nyansen må treffe i K1

> **Gate G2:** Hvert kapittelutkast godkjennes av Lars før det går videre.

---

### Fase 3 — Adversarial review *(3 linser per kapittel, parallelt)*

Her ligger den faktiske multiagent-verdien. Tre **ulike** linser, ikke tre like stemmer:

| Linse | Spør | Grunnlag |
| --- | --- | --- |
| **Kildevokter** | Bærer en 🟡-kilde en setning den ikke tåler? Er effekt påstått i presens? | `AGENTS.md` kilderegler |
| **Rådsvurderer** | Score 0–5 mot Kvalitet og Effekter. Hva trekker ned? | `ipn-barekraft-sannhetsserum` §10 |
| **Språkvask** | KI-preg, anglifisering, glatt konsulenttone? | `skills/ai-sprakvask-no` |

Linsene er komplementære, så et funn fra én overstyres ikke ved avstemning. I stedet får
hvert funn én skeptiker som prøver å **motbevise** det. Overlever funnet, går det til Lars.

Kapittel A kan gå til review mens kapittel B fortsatt skrives — ingen barriere her.

---

### Fase 4 — Kryssdokument-konsistens *(én agent, trenger alle sju samtidig)*

Sjekker som per definisjon ikke kan gjøres kapittelvis:

- **EBA-kollisjonen.** «EBA» er to organisasjoner — European Banking Authority og EBA Norge
  (entreprenørforeningen). Arbeidsplanen advarer eksplisitt. Denne feilen ville vært pinlig.
- Samme påstand med ulik kildefarge i to kapitler
- «Digitalt produktpass (DPP)» brukt likt overalt
- **Ingen lenker i den innsendte teksten** (`ipn-hovedokument.md:12`) — nøkler erstattes med
  korte tekstreferanser
- Sidebudsjett mot faktisk lengde

---

### Fase 5 — Statusvedlegg + PDF

**Statusvedlegget** bygges av kildekvitteringene fra fase 1, avstemt mot endelig tekst. Det
er dette som gjør at ren prosa ikke blir uærlig prosa: hver 🟡 står oppført med hva SINTEF må
åpne.

**PDF-en har ingen eksisterende toolchain.** Verken pandoc, weasyprint eller noe script
finnes i repoet. `ipn-samledokument.pdf` (28. juni) etterlot seg ingen oppskrift. To spor:

| Spor | Når |
| --- | --- |
| Claude bygger PDF via `pdf`-skillen (Python finnes) | Engangs røft utkast → **anbefalt nå** |
| Handoff `36_pdf_montering_handoff.md` til Codex | Hvis pipelinen skal kunne kjøres om igjen |

Handoff-nummereringen starter på **36** — `docs/handoffs/` går til 35, ikke 29 som
`orchestration.md` påstår. Den fila bør rettes.

> **PDF-strukturen er foreløpig.** `ipn-hovedokument.md:4` sier «2026-mal gjenstår å bekrefte».
> Sju-kapittelstrukturen er utledet av Forskningsrådets *vurderingskriterier*
> (Kvalitet/Virkninger), ikke av en bekreftet malfil. Det er forsvarlig, men PDF-en skal
> merkes som strukturelt foreløpig til 2026-malen er verifisert. Legg dette til G4.

> **Gate G4:** Lars godkjenner PDF-en før den sendes SINTEF.

---

## Hva som er styrbart, og hva som ikke er det

```
                        Lars (orkestrator, godkjenner)
                                    │
              ┌─────────────────────┴─────────────────────┐
      Claude-subagenter                          Codex / Antigravity
      (fase 1, 3, 4)                             (fase 5, hvis handoff-spor)
      kildekvittering, review,                   PDF-montering, repo-arbeid
      konsistens                                 ─ via handoff-fil, ikke styring
```

Fase 0 og 2 er Claude alene med Lars. Ingen fan-out.

---

## Hvordan agentene faktisk kjøres

Tre mulige mekanismer. Planen anbefaler den midterste.

| Mekanisme | Hva det er | Vurdering |
| --- | --- | --- |
| **Agent-verktøyet, manuelt** | Claude spawner subagenter én runde av gangen | Enkelt, men ingen audit trail |
| **`provenance/agents/`-mønsteret** | `BRIEFING.md` + `progress.md` + domeneoutput per agent — strukturen finnes allerede fra kildedom-kjøringen | **Anbefalt.** `orchestration.md` sier eksplisitt: gjenbruk denne ved større kjøringer. Gir sporbarhet, som er hele poenget i dette repoet |
| **Workflow-verktøyet** | Ett skript orkestrerer alle ~38 kallene | Krever at **Lars eksplisitt ber om det** — det er en opt-in-mekanisme som kan bruke mye tokens. Vurder for fase 3, som er den store fan-outen |

Anbefalingen: kjør fase 1 og 4 som `provenance/agents/`-kjøringer. Fase 3 er stor nok til at
Workflow-verktøyet er forsvarlig — men det krever at du sier ifra. Jeg starter det ikke selv.

---

## Kostnad

| Fase | Agentkall |
| --- | --- |
| 1 — kildekvittering | 7 |
| 3 — review (7 kap × 3 linser + skeptikere) | ~30 |
| 4 — konsistens | 1 |
| **Sum** | **~38** |

Fase 3 er tre firedeler av kostnaden. Kjøres den bare på kapitlene som faktisk klarerer G1,
faller tallet tilsvarende. Det er sannsynlig: med 47 🟡-kilder er det lite trolig at alle sju
kapitler er skrivbare i første runde.

---

## Gates

| Gate | Når | Lars avgjør |
| --- | --- | --- |
| **G0** | Nå | Godkjenner denne planen |
| **G1** | Etter fase 1 | Hvilke kapitler kan skrives nå? |
| **G2** | Per kapittel | Godkjenner utkast |
| **G3** | Etter fase 3 | Hvilke funn rettes, hvilke står |
| **G4** | Etter fase 5 | PDF sendes SINTEF |

---

## Avklaringsseksjonen (Lars, 2026-07-08) — avgjort

Lars foreslo en samlet avklaringsseksjon som lukker fire hull: rollefordeling, ikke-startet
FoU, underleverandører, forskningsetikk/-sikkerhet. **Hullet er reelt og sentralt** — det
beskytter FoU-høyde-argumentet mot innvendingen «dette er bare produktutvikling som alt er i
gang». `claude-guardrails.md` lister VIBS-score-formelen som *eksisterende* og MVP-plattformen
som *under bygging*, mens §10.2 sier at aktivitetene ikke kan ha startet. Den spenningen må
besvares eksplisitt.

Men innholdet spenner over tre vurderingskriterier og kan ikke ligge i ett kapittel.
Splittet følger `ipn-barekraft-sannhetsserum-2026-06-21.md` §10.7:

| Del | Vurderes under | Hjem | Beslutning |
| --- | --- | --- | --- |
| Forskningsetikk | **Kvalitet** («Etikk ivaretatt») | `k4-metode.md` | ✅ **full tekst i K4** |
| FoU-lag vs. eksisterende produkt | **Kvalitet** (nyhetsverdi/FoU-høyde) | `k2` + `k3` | ✅ skrives nå |
| Ingen falsk presisjon; skjevhet i vekting | **Virkninger** (DNSH) | `v2-sikkerhet.md` | ✅ matcher §4-angrepslista |
| Roller, underleverandører, formell org. | **Gjennomføring** («budsjett/roller») | Gjennomføring | ⛔ parkert med WP |
| Forskningssikkerhet, datahåndteringsplan | Ved innvilgelse (§10.6) | Etter tildeling | ⛔ kun framoverpeker |

### Språkrettinger før teksten brukes

**«vectorisering» → `dataintegrasjon` (ubekreftet — Lars må bekrefte).** Ordet har null treff i
repoet. Lars anga «glipp for vekting», men hans egen setning inneholder *begge* ord: «metode
for vectorisering, datakvalitet, usikkerhet, **vekting av kriterier** …». Mekanisk erstatning
gir redundans. Listen speiler i stedet SoA §3s seks akser, der akse (a) heter
**dataintegrasjon**. Det er den sannsynlige betydningen. Ikke skriv det inn som bærende før
Lars har bekreftet.

**«eier den eksisterende plattformen» → presiseres.** `claude-guardrails.md` forbyr å blande
*eksisterer* / *under bygging* / *veikart*. MVP-plattformen er under bygging. Formuler i
stedet: *VIBS-plattformen, som utvikles uavhengig av dette prosjektet, brukes som test- og
integrasjonsflate.* Dette er også det sterkeste argumentet — det viser at plattformarbeidet er
egenfinansiert produktutvikling, ikke FoU-en det søkes om.

**Åpen faktasjekk:** har søknadssystemet et eget etikkfelt? §10.6 ber om «kort beskrivelse», og
skjemaet bygges in-system. Hvis feltet finnes, hører langversjonen der — ikke i PDF-en. Lars
sjekker ved neste innlogging.

**Merk:** fakta Lars researchet fra utlysningen står allerede i §10 som kontrollert kildekopi
(§10.2 ikke-startet · §10.4 partnerkrav · §10.6 etikk/DMP · §10.7 kriterier). Kilden er
`[NFR_IPN2026]` 🟢. Bruksfeltet i kildebiblioteket sier i dag «formalia / budsjett» og bør
utvides til roller/støtteberettigelse/etikk. Én fakta derfra treffer Lars' underleverandørlinje
direkte: **enkeltpersonforetak kan ikke være prosjektansvarlig, kun samarbeidspartner** (§10.4).

---

## Utenfor scope

- **WP1–WP5 og Gjennomføring.** Parkert. Røres ikke. *(WP3 mangler fortsatt baseline —
  markert Rød i hovedokumentet. Det problemet venter.)*
- **Innsendingsklar finpuss.** SINTEF, fra midten av august.
- **Primærverifisering av 🟡-kilder.** SINTEF. Ingen agent kan åpne en Wiley-betalingsmur, og
  agent-konsensus er ikke belegg.
- **Nettsiden.** Eget spor.

---

### Endringslogg
- 0.2 (2026-07-09): Status oppdatert etter at første røffe K/V-utkast ble skrevet i
  `docs/reference/prosjektbeskrivelse/`. Utkastet følger enkelt snekker-språk og holder WP/Gjennomføring
  parkert. Ikke innsendingsklart; åpne avklaringer står i kapittelfilene.
- 0.1 (2026-07-08): Første plan. Skrevet etter at Lars valgte ipn-verified som arbeidssted,
  K/V-only scope, og ren prosa + statusvedlegg. Fant at `prosjektbeskrivelse/`-mappa aldri ble
  opprettet, at `k4-metode` mangler forelder i skjelettet, og at handoff-nummereringen i
  `orchestration.md` er utdatert (sier 29, faktisk 35).
