# VIBS VERIFIED — Språkanalyse og Guardrail-verifikasjon

**Dato:** 2026-06-27  
**Status:** Verifisert rapport  
**Ansvarlig agent:** teamwork_preview_worker  
**Analyserte filer:**
- `docs/reference/ipn-samledokument.md`
- `docs/reference/ipn-hovedokument.md`
**Styringsdokument:** `docs/reference/claude-guardrails.md`
**Grunnlag for sammenligning:** `C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/teamwork_preview_explorer_analysis_1/analysis.md`

---

## 1. Sammendrag og Hovedfunn

Denne rapporten presenterer den formelle språklige analysen og guardrail-sjekken av prosjektbeskrivelsene for VERIFIED-prosjektet. Analysen har blitt utført ved hjelp av et dedikert Python-analyseprogram (`word_analysis.py`) som har skannet dokumentene etter AI-buzzwords, bransjesjargong og kompleksitet.

### Viktigste konklusjoner:
1. **AI-buzzwords:** Begge dokumentene har **null (0)** forekomster av AI-buzzwords, noe som er i tråd med prosjektets fokus på tradisjonell flerkriterieanalyse (MCDA) fremfor AI.
2. **Bransje- og akademisk sjargong:** Det er identifisert enkelte forekomster av akademisk og strategisk sjargong (f.eks. *siloer*, *syntesen*, *robusthet*, *operasjonalisert*). Disse bør forenkles for å øke lesbarheten for ikke-spesialister.
3. **Guardrail-avvik:** Det er avdekket alvorlige brudd på **Produktstatus/MVP-regelen** i `ipn-samledokument.md`. Plattformen (VIBS) og score-modellen (VERIFIED) beskrives i presens som operative løsninger (f.eks. *"VIBS samler"*, *"VERIFIED flytter"*). Dette må omskrives til futurum eller målbeskrivelser.
4. **Samsvar på øvrige områder:** Det er fullt samsvar med guardrail-reglene for finans/grønn rente, bruk av markedsandeler/tall (alle bransjetall er kildebelagt), partnerstatus, og bærekraftspresentasjon (økonomifokus uten moralske pekefingre).

---

## 2. Frekvenstabell for AI-buzzwords og Sjargong

Nedenfor vises frekvensen av søkeordene i de to dokumentene, verifisert av vår Python-analyse.

| Kategori | Begrep | Forekomster i `ipn-samledokument.md` | Forekomster i `ipn-hovedokument.md` | Totalt |
| :--- | :--- | :---: | :---: | :---: |
| **AI/Tech buzzword** | AI | 0 | 0 | **0** |
| **AI/Tech buzzword** | kunstig intelligens | 0 | 0 | **0** |
| **AI/Tech buzzword** | agent | 0 | 0 | **0** |
| **AI/Tech buzzword** | maskinlæring | 0 | 0 | **0** |
| **AI/Tech buzzword** | algoritme | 0 | 0 | **0** |
| **AI/Tech buzzword** | llm | 0 | 0 | **0** |
| **AI/Tech buzzword** | gpt | 0 | 0 | **0** |
| **AI/Tech buzzword** | neural | 0 | 0 | **0** |
| **AI/Tech buzzword** | deep learning | 0 | 0 | **0** |
| **Jargon** | synergi | 0 | 0 | **0** |
| **Jargon** | transformasjon | 0 | 0 | **0** |
| **Jargon** | optimalisering | 0 | 0 | **0** |
| **Jargon** | robust | 1 | 0 | **1** |
| **Jargon** | holistisk | 0 | 0 | **0** |
| **Jargon** | digitalisering | 1 *(digitaliserte)* | 1 *(digitalisert)* | **2** |
| **Jargon** | siloer | 1 | 1 | **2** |
| **Jargon** | syntesen | 2 | 0 | **2** |
| **Jargon** | robusthet | 2 | 0 | **2** |
| **Jargon** | operasjonalisert | 0 | 1 | **1** |

---

## 3. Kompleksitetsmålinger og Lange Ord

Dokumentene har blitt analysert for setningslengde og lange, sammensatte ord som hemmer lesehastigheten.

### Setningsstatistikk
* **Komplekse setninger (> 25 ord):**
  * `ipn-samledokument.md`: **15 setninger** (inkludert setninger på opptil 50-60 ord med parenteser og innskutte ledd).
  * `ipn-hovedokument.md`: **1 setning** (dokumentet er primært et magert skjelett med punktlister).
* **Lange enkeltord (> 15 tegn):**
  * Unike ord i `ipn-samledokument.md`: **26 ord**
  * Unike ord i `ipn-hovedokument.md`: **8 ord**

### Liste over unike lange ord (> 15 tegn)
* **Begge dokumenter:** `prosjektbeskrivelsen` (20), `beslutningseffekt` (17), `bærekraftsbidrag` (16), `klimagassutslipp` (16), `leverandørleveranse` (19), `kommersialisering` (17).
* **Kun `ipn-samledokument.md`:** `beslutningsgrunnlaget` (22), `programvaresystemer` (19), `distriktsdepartementet` (22), `samfunnsøkonomisk` (17), `miljødeklarasjoner` (18), `livsløpskostnader` (17), `prosjekteringsfasen` (19), `påvirkningsrommet` (17), `beslutningslogikken` (19), `dokumentasjonstillit` (20), `forskningslitteraturen` (22), `datainfrastrukturen` (19), `livsløpsvurdering` (17), `konkurrentverktøyet` (19), `finansforskningen` (17), `klimagassutslippene` (19), `arbeidsrettigheter` (18), `finansieringsvinkel` (19), `misligholdsrisiko` (17), `atferdsforskning` (16), `tilbakemeldinger` (16).
* **Kun `ipn-hovedokument.md`:** `innsendingssetning` (18), `bærekraftseffekt` (16).

---

## 4. Evaluering mot Claude-Guardrails

| Tema / Regel | Status | Observasjon og Belegg |
| :--- | :---: | :--- |
| **Produktstatus / MVP** | 🔴 **BRUDD** | I `ipn-samledokument.md` omtales uferdig MVP-plattform og forskningsscore i presens (f.eks. linje 10, 14, 28, 65, samt i effekttabellen under avsnitt 7). Dette bryter direkte med regelen om aldri å beskrive MVP som ferdig. |
| **Finans & Grønn Rente** | 🟢 SAMSVAR | Ingen konkrete rentebesparelser (0,15–0,40 %) presenteres som faste avtaler. Risiko og bankkobling omtales korrekt som en hypotese/forskingsspørsmål (F1). |
| **Markedsandeler & Tall** | 🟢 SAMSVAR | Konfliktmerkostnad (2,2 mrd) og byggefeilkostnad (10–30 mrd) er kildebelagt med hhv. `[SA2018]` og `[GullbrekkenHolme2025]`/`[KD2024]`. Ingen udokumenterte påstander. |
| **Partnere** | 🟢 SAMSVAR | Ingen partnere omtales feilaktig som "signert" uten LoI. NorDan og Tirna Fagskole omtales korrekt. Tirna Fagskole omtales ikke som universitet. |
| **VIBS-score** | 🟢 SAMSVAR | Scoren fremstilles ikke som en uavhengig tredjepartssertifisering. Den er tydelig definert som et relativt beslutningsverktøy innenfor produktkategorier. |
| **Bærekraft** | 🟢 SAMSVAR | Bærekraft presenteres som økonomiske besparelser og ressurseffektivitet (mål 12.2 og 12.5), helt fri for moralske pekefingre. |

---

## 5. Anbefalte Omskrivinger (Før / Etter)

For å sikre full overholdelse av guardrails og forbedre tekstens lesbarhet, anbefales følgende konkrete endringer.

### 5.1. Rettelser av Guardrail-brudd (Produktstatus)

#### Forekomst 1 (`ipn-samledokument.md` - Linje 10)
* **Før:** `VIBS er en plattform for små og mellomstore byggebedrifter som samler prosjektstyring, dokumentasjon, kommunikasjon og kvalitet på ett sted — uten tunge systemer og dyre abonnement. VERIFIED er forskningsdelen: en modell som gir hvert produkt- og løsningsvalg en etterprøvbar score basert på pris, levetid...`
* **Etter:** `VIBS er under utvikling som en plattform for små og mellomstore byggebedrifter. Den er designet for å samle prosjektstyring, dokumentasjon, kommunikasjon og kvalitet på ett sted, uten tunge systemer og dyre abonnement. Forskningsprosjektet VERIFIED skal utvikle en modell som skal gi hvert produkt- og løsningsvalg en etterprøvbar score basert på pris, levetid...`

#### Forekomst 2 (`ipn-samledokument.md` - Linje 14)
* **Før:** `VERIFIED flytter beslutningsgrunnlaget dit, og gjør bærekraft til en konsekvens av bedre økonomi og lavere risiko...`
* **Etter:** `VERIFIED skal flytte beslutningsgrunnlaget dit, og vil bidra til å gjøre bærekraft til en konsekvens av bedre økonomi og lavere risiko...`

#### Forekomst 3 (`ipn-samledokument.md` - Linje 28)
* **Før:** `VERIFIED adresserer ikke mangel på data, men mangelen på en bro fra data til beslutning — et grunnlag en SMB-entreprenør eller boligkjøper kan bruke i tilbudsfasen...`
* **Etter:** `Forskningsprosjektet VERIFIED skal ikke adressere mangel på data, men mangelen på en bro fra data til beslutning. Målet er å utvikle et grunnlag som en SMB-entreprenør eller boligkjøper kan bruke i tilbudsfasen...`

#### Forekomst 4 (`ipn-samledokument.md` - Linje 65)
* **Før:** `VERIFIED gjør et produktvalg om til en sammenliknbar score. Forenklet: hver dimensjon gis 0–100 poeng...`
* **Etter:** `VERIFIED er designet for å gjøre et produktvalg om til en sammenliknbar score. Modellen legger opp til at hver dimensjon skal gis 0–100 poeng...`

#### Forekomst 5 (`ipn-samledokument.md` - Tabell under Avsnitt 7, Linje 133-139)
* **Før (Påstander i presens):**
  * `VIBS reduserer CO₂ fra materialvalg`
  * `VIBS reduserer byggfeil og omarbeid`
  * `VIBS hjelper SMB med bærekraft`
  * `VIBS gir bedre grønn bankdokumentasjon`
  * `VIBS bidrar til do-not-harm`
* **Etter (Målformuleringer):**
  * `Mål om å redusere CO₂ fra materialvalg`
  * `Potensial for redusert byggefeil og omarbeid`
  * `Støtte til SMB for bærekraftsvalg`
  * `Mål om bedre grønn bankdokumentasjon`
  * `Planlagt dokumentasjon av do-not-harm (DNSH)`

---

### 5.2. Forenkling av Akademisk/Strategisk Sjargong

| Dokument | Linje | Sjargong-uttrykk | Forslag til endring |
| :--- | :---: | :--- | :--- |
| `ipn-samledokument.md` | 24 | *digitaliserte*, *fragmenterte* | "...lavest grad av IT-bruk og består av mange små aktører." |
| `ipn-samledokument.md` | 26 | *siloer* | "...de er lagret i ulike systemer uten kobling..." |
| `ipn-samledokument.md` | 47, 49 | *syntesen* | "...sammenstillingen og koblingen av dataene..." |
| `ipn-samledokument.md` | 40, 45, 52 | *robust*, *robusthet* | "pålitelig", "holdbarhet", "pålitelighet" |
| `ipn-hovedokument.md` | 43 | *operasjonalisert* | "...ikke tatt i bruk i praktiske verktøy." |
| `ipn-hovedokument.md` | 91 | *regulatorisk medvind* | "...gir drahjelp fra kommende regelverk." |

---

### 5.3. Oppsplitting av Komplekse Setninger

#### Eksempel 1 (`ipn-samledokument.md` - Linje 26)
* **Før:** `Miljødeklarasjoner (EPD), produktdata i NOBB, livsløpskostnader og levetidsdata eksisterer — men de lever i atskilte siloer, er bygget for spesialister i prosjekteringsfasen, og er ikke koblet til den beslutningen som faktisk avgjør utslipp og kvalitet: valget av produkt og løsning i tilbudsfasen.` (41 ord)
* **Etter:** `Selv om miljødeklarasjoner (EPD), produktdata i NOBB og levetidsdata eksisterer, er dataene i dag spredt i ulike systemer. De er i hovedsak utviklet for spesialister i prosjekteringsfasen. Dermed kobles de ikke til tilbudsfasen, der de faktiske valgene av produkt og løsning tas.` (3 setninger, gjennomsnittlig lengde 14 ord).

#### Eksempel 2 (`ipn-samledokument.md` - Linje 36)
* **Før:** `Hver enkelt byggekloss finnes allerede og er faglig moden: standardene for livsløpsvurdering og livsløpskostnad er etablerte (EN 15978:2026; ISO 15686-5; NS-EN 16627), datainfrastrukturen modnes gjennom EPD-systemet, NOBB og det kommende digitale produktpasset (DPP, forordning (EU) 2024/3110), og metodene for å veie kriterier mot hverandre er veletablerte i forskningslitteraturen (Mecca 2023).` (60 ord)
* **Etter:** `De nødvendige byggeklossene finnes allerede og er faglige modne. Standardene for livsløpsvurdering og livsløpskostnad er etablerte (EN 15978:2026; ISO 15686-5; NS-EN 16627). Samtidig modnes datainfrastrukturen gjennom EPD-systemet, NOBB og det kommende digitale produktpasset (DPP, forordning (EU) 2024/3110). Metodene for å veie ulike kriterier mot hverandre er også veletablerte (Mecca 2023).` (4 setninger, gjennomsnittlig lengde 14 ord).

#### Eksempel 3 (`ipn-samledokument.md` - Linje 51)
* **Før:** `Å slå dem sammen til ett tall som viser hvor sikkert grunnlaget er — i stedet for å gjemme svakheten i én totalscore — er fortsatt et uløst forskningsspørsmål (Benke et al. 2025; Lohman et al. 2023).`
* **Etter:** `Å slå disse sammen til en samlet poengsum som synliggjør usikkerheten, i stedet for å skjule den, er fortsatt et uløst forskningsspørsmål (Benke et al. 2025; Lohman et al. 2023).`
