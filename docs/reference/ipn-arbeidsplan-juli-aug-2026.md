# Arbeidsplan — IPN-søknad, juli–august 2026

**Dato:** 2026-06-26 · **Ansvarlig:** Lars Erik · **Status:** Klar til å begynne

---

## Kort fortalt

Vi skriver søknaden til Forskningsrådet for VERIFIED — et forskningsprosjekt om bedre materialvalg i byggebransjen. Lars Erik gjør det meste av jobben. Claude hjelper med skriving, omformuleringer og nettsøk. SINTEF kommer inn seinere for å sjekke vitenskapelige kilder.

**Status nå:** første kildesjekk er gjennomført og flettet inn i kanonen. Neste hovedoppgave er å skrive videre på prosjektbeskrivelsen med grønne kilder først, mens gule kilder holdes som forbehold. Nettsiden kan gå parallelt. Handoff-filer ligger i den nummererte loggen `docs/context/windows-score/` (26 = oversikt, 27 = kildesjekk, 28 = nettside).

---

## Hva vi jobber med nå

To deler av søknaden:
- **Kvalitet:** Hva vi forsker på og hvorfor det er nytt
- **Virkninger:** Hva forskningen fører til

**Vi jobber ikke med arbeidspakkene (WP1–WP5) nå.** De finnes allerede og tas i neste runde.

## Status på state of the art og kilder

Kunnskapsgrunnlaget er sterkt nok til å bære IPN-retningen og FoU-høyden: komponentene finnes hver for seg, men ingen dokumentert løsning dekker kombinasjonen **tilbudsfase + SMB + flerkriterie-score + synlig usikkerhet + målt beslutningseffekt**.

Arbeidsregelen videre:
- Bruk **norske/offisielle kilder først** for norske forhold, regelverk, marked, skader, SMB og byggenæring.
- Bruk **internasjonal fagfellevurdert forskning** for generelle mekanismer der norsk kilde ikke finnes, særlig metode og energi↔finansiell risiko.
- Ikke bruk gule kilder som bærende bevis i innsendingstekst før primær/fulltekst er åpnet.

Grønt nok til å brukes direkte nå:
- `[Billio2022]` og `[Kaza2014]` for energi↔PD i boliglån.
- `[NFR_IPN2026]` for støttebeløp og støttegrad.
- `[FinansNorge2024VASK]` for vannskader 2023.
- `[Benke2025]`, `[Lohman2023]`, `[Nordic2023]`, `[BKA2]`, `[EC3]` og sentrale EU/standardkilder som allerede er åpnet i kanonen.

Gult / må åpnes før bærende bruk:
- `[An2020]`: metadata og DOI er bekreftet, men Wiley-fulltekst/akseptert manus må åpnes før 34 %-tallet brukes bærende.
- `[SA2018]`: primærrapporten fra Samfunnsøkonomisk analyse må lokaliseres og åpnes før 2,2 mrd.-tallet blir grønt.
- `[Mecca2023]`: metodefordeling er bekreftet via sekundære åpne spor, men Wiley-fulltekst bør hentes av SINTEF.
- `[EBA_NO2023]` og `[KD2024]`: brukes som norske primærspor for klima/tidligfase, men bør åpnes og lagres av Lars Erik/SINTEF før endelig innsending.

Konklusjon: SoA-argumentet holder, men søknadsteksten må ikke overclaime effekt. Formuler VERIFIED som et prosjekt som **skal teste og måle** CO₂, kvalitet, risiko og beslutningseffekt, ikke som om effekten allerede er bevist.

---

## Dokumentene

Søknaden skrives som sju separate kapitler — ett dokument per kapittel — i mappen `docs/reference/prosjektbeskrivelse/`. De slås sammen til én PDF når søknaden er ferdig.

| Fil | Innhold |
| --- | --- |
| `k1-bakgrunn.md` | Problemet i bransjen |
| `k2-nyhetsverdi.md` | Hva som er nytt med VERIFIED |
| `k3-forskning.md` | Hva vi forsker på |
| `k4-metode.md` | Hvordan vi gjør det |
| `v1-baerekraft.md` | Miljø og bærekraft |
| `v2-sikkerhet.md` | At vi ikke skader noen |
| `v3-okonomi.md` | Samfunnsøkonomi og banker |

---

## Hvem gjør hva

| Hvem | Rolle |
| --- | --- |
| **Lars Erik** | Leser, bestemmer og godkjenner. Henter noen åpne kilder selv (se kildeliste). |
| **Claude** | Skriver utkast, omformulerer, faktasjekker åpne nettkilder med Sonar. Lager handoff-instrukser (MD-filer) som Codex og Antigravity leser i VS Code. |
| **Codex / Antigravity** | De utførende agentene i VS Code. Skriver kode, bygger nettside, gjør repo-arbeid. Leser handoff-filene og rapporterer tilbake. |
| **Lars Gunnar** | Bestemmer hva vi skal måle for å vise at scoren faktisk påvirker valg. |
| **SINTEF** | Sjekker vitenskapelige kilder mot originaldokumentene. Kommer inn **midten av august** — ikke nå. |

---

## Rekkefølge

### Trinn 1 — Lag dokumentstrukturen (Claude gjør dette)
Claude oppretter mappen og de sju kapittelfilene. Hver fil starter med en innholdsoversikt og en liste over hva som trengs av kilder og beslutninger.

### Trinn 2 — Rettelser Claude gjør selv (allerede godkjent)
Disse gjøres uten at Lars Erik trenger å bestemme noe nytt:

| Hva som endres | Hvor i søknaden |
| --- | --- |
| "tynne marginer" → "lave/pressede marginer" | Bakgrunn (k1) |
| "spesialistverktøy" → presiseres til programvare | Bakgrunn (k1) |
| "alt finnes allerede" → mykes opp til "det meste, for de fleste" | Hva VERIFIED er (k2) |
| "digitalt produktpass (DPP)" — brukt likt i alle dokumenter | Hele søknaden |
| Listen over datatyper — utvides med full liste | Hva VERIFIED er (k2) |
| Beslutningspåvirkning — omformuleres mer forsiktig | Hva VERIFIED er (k2) |
| "lett vedlikehold" legges til i listen over bærekraftskriterier | Hva VERIFIED er (k2) |
| Do-not-harm-avsnittet — korrekturleses | Virkninger (v2) |

### Trinn 3 — Faktasjekk via nettsøk (Claude bruker Sonar)
Claude sjekker disse påstandene mot offentlige kilder:
- «Byggenæringen er Norges største fastlandsnæring»
- «En av de minst digitaliserte næringene»
- «En av de mest fragmenterte næringene»

### Trinn 4 — Lars Erik tar stilling til disse
Disse oppgavene krever Lars Eriks vurdering — Claude kan ikke avgjøre dem alene:

| Spørsmål | Notater |
| --- | --- |
| Definer SMB: antall ansatte + andel av bransjen | Trenger tall fra SSB eller NHO |
| Hva er inkludert i 2,2 mrd/år (konflikter og reklamasjoner)? | Harerusten 2022 — hva er egentlig medregnet? |
| Gjøre utfordringen tydeligere — andre parametere enn pris | Utkast til ny setning finnes i tilbakemeldingslista |
| Hvilke påstander er vi sikre på, og hvilke er hypoteser? | Gjelder hele søknaden |
| SMB-entreprenørene er fagfolk, ikke ikke-spesialister | Viktig nyanse — de er dyktige håndverkere, bare ikke LCA-eksperter |

### Trinn 5 — Kapittel for kapittel
For hvert av de sju kapitlene:
1. Claude skriver utkast basert på det vi allerede har
2. Markerer hva som trenger kildeverifisering (🟡 = ikke ferdig sjekket)
3. Lars Erik leser og gir tilbakemelding
4. Claude justerer og gjentar

### Trinn 6 — Nettside (parallelt, enkelt)
En enkel første versjon av VERIFIED-nettsiden — **kun om forskningsprosjektet, ikke VIBS-produktet**. Ingen produktinfo, pris eller salgsbudskap.

Innhold:
- Problemet i bransjen
- Hva vi forsker på
- Metoden, enkelt forklart
- Konsortiet (VIBS + SINTEF)

Lars Erik har ideer til bilder og design — det bestemmes seinere.

---

## Kildeliste å sjekke

Disse kildene brukes i søknaden, men er ikke fullt grønne ennå (🟡):

| Prioritet | Kilde | Brukes til | Hvem sjekker |
| --- | --- | --- | --- |
| 1 | `SA2018` — konfliktkostnad 2,2 mrd | Bakgrunn/WP2 | Lars Erik/SINTEF må finne og åpne primærrapport |
| 2 | `An2020` — CMBS/næringsbygg og 34 %-tall | Finansbro, kun støtte | SINTEF må åpne Wiley/fulltekst |
| 3 | `Mecca2023` — flerkriterie-metode | Kvalitet/nyhetsverdi | SINTEF (betalt tilgang) eller Lars Erik (ResearchGate) |
| 4 | `EBA_NO2023` — 20 % uten merkostnad | Virkninger | **Lars Erik** åpner/laster ned PDF |
| 5 | `KD2024` — tidligfase/påvirkningsrom | Bakgrunn og kvalitet | **Lars Erik** åpner fra regjeringen.no |
| 6 | Gullbrekken & Holme 2025 — byggfeil 10–30 mrd | Bakgrunn | SINTEF |
| 7 | Wiik 2025 — internt SINTEF-notat | Kun arbeidsgrunnlag | SINTEF; ikke bærende uavhengig bevis |

Disse er allerede bekreftet (🟢) og kan brukes som de er:
Billio 2022 · Kaza 2014 · NFR IPN 2026 · Finans Norge VASK 2023 · EN 15978:2026 · NS-EN 16627 · EU-forordningene om digitalt produktpass · Benke 2025 · Lohman 2023 · EC3 · Nordic Council 2023 · BKA2

**Pass på navnekollisjonen:** «EBA» er to ulike organisasjoner i søknaden vår — den europeiske bankorganisasjonen (EBA EU) og den norske byggforeningen (EBA NO). Disse holdes alltid fra hverandre.

---

## Tidslinje

| Periode | Hva skjer |
| --- | --- |
| Juli uke 1–2 | Lars Erik + Claude jobber gjennom kapitlene |
| August uke 1 | Ferdig første utkast |
| Midten av august | Overlevering til SINTEF for kildesjekk |
| Slutten av september | Søknad sendes til Forskningsrådet |

---

## Slik fungerer arbeidet — verktøy og agenter

Selve arbeidet skjer i **VS Code**. Der jobber to agenter: **Codex** og **Antigravity**. De er de viktigste — de skriver kode og bygger nettsiden. **Sonar** er et støtteverktøy som brukes til faktasjekk, ikke en agent.

| Verktøy / agent | Rolle |
| --- | --- |
| **VS Code** | Arbeidsbenken. Alt repo-arbeid skjer her. |
| **Codex** | Utførende agent. Kode, repo-struktur, dokumenter. |
| **Antigravity** | Utførende agent. Nettside og UI. |
| **Claude** | Skriver handoff-instrukser, omformulerer tekst, kjører Sonar-faktasjekk. |
| **Sonar** | Faktasjekk-verktøy (loopback-API). Brukes ved behov, ikke en agent. |

**Viktig ærlighetsregel:** Claude kan **ikke** styre Codex eller Antigravity direkte — de er separate verktøy. Claude lager i stedet **handoff-filer** (MD) som du selv limer inn eller åpner i VS Code. Slik flyttes en oppgave over til riktig agent.

Syklusen:

1. Lars Erik velger en oppgave
2. Claude skriver en handoff-fil (MD) med mål, steg og en ferdig «Startprompt»
3. Lars Erik gir startprompten til Codex eller Antigravity i VS Code
4. Agenten gjør jobben i repoet og rapporterer tilbake
5. Sonar brukes til faktasjekk underveis der det trengs
6. Lars Erik leser, godkjenner, og neste oppgave starter

**Claude kan gjøre selv (uten ekstern agent):**
- Rettelsene i trinn 2 (allerede gjort)
- Sonar-faktasjekk av åpne nettkilder
- Skrive handoff-filer og tekstutkast

**Krever alltid Lars Eriks beslutning:**
- Innholdsspørsmål (definisjoner, tall, påstander)
- Godkjenning av hvert kapittel- og kodeutkast

---

## Hva som venter til seinere

- Arbeidspakkene (WP1–WP5) — finnes, røres ikke nå
- Innsendingsklar finpuss — SINTEF tar det fra midten av august
- Nettside-teknologi og design — bestemmes seinere

---

### Endringslogg
- 0.4 (2026-06-27): Oppdatert etter Codex-kildesjekk. SoA-status, kildeprioritering og grønn/gul kildeliste synket mot kanon.
- 0.1 (2026-06-22): Første plan. Avgrensning til Kvalitet + Virkninger. Arbeidspakker lagt til side.
- 0.2 (2026-06-26): Omskrevet til enklere norsk. Engelsk sjargong fjernet. Lagt til seksjon om agent-koordinering og Sonar-faktasjekk.
- 0.3 (2026-06-26): Rettet orkestreringsmodellen — VS Code + Codex + Antigravity som utførende agenter (viktigere enn Sonar), Sonar demotert til faktasjekk-verktøy, ærlighetsregel tydeliggjort. Nå-fokus: kildesjekk + nettside, med egne handoff-filer (26–28).
