# Analyse: Overholdelse av Claude-guardrails for IPN-dokumenter

Dette dokumentet inneholder analysen av `docs/reference/ipn-samledokument.md` og `docs/reference/ipn-hovedokument.md` opp mot retningslinjene definert i `docs/reference/claude-guardrails.md`.

---

## 1. Hovedfunn og oppsummering

- **AI-buzzwords**: Det er **null (0)** forekomster av AI-buzzwords (som *AI, kunstig intelligens, agent, maskinlæring, algoritme, llm, gpt, neural, deep learning*) i begge dokumentene. Dette er i tråd med prosjektets fokus på tradisjonelle flerkriterieanalyser (MCDA) og datakoordinering, og representerer god overholdelse av guardrails.
- **Sjargong (Jargon)**: Det er identifisert en del bransje- og akademisk sjargong som kan forenkles for å øke lesbarheten. Eksempler inkluderer *digitaliserte, fragmenterte, siloer, syntesen, robusthet, operasjonalisert* og *regulatorisk medvind*.
- **Komplekse setninger og lange ord**: Begge dokumentene, særlig `ipn-samledokument.md`, lider av lange setninger (opptil 60 ord) med mange innskutte ledd, tankestreker og parenteser. Det er også en høy forekomst av lange norske sammensatte ord (f.eks. *beslutningsgrunnlaget, prosjekteringsfasen, dokumentasjonstillit*).
- **Brudd på guardrails (Produktstatus/MVP)**: Det mest kritiske funnet er at **produktstatusen presenteres i presens** (f.eks. *"VIBS samler"*, *"VERIFIED flytter"*, *"VERIFIED gjør"*), noe som gir inntrykk av at løsningen er ferdig og i drift. Dette bryter direkte med regelen: *"Aldri beskrive MVP som ferdig. Aldri si at VIBS «leverer» noe som er under bygging."*
- **Samsvar på andre områder**:
  - **Finans/grønn rente**: Fullt samsvar. Dokumentene unngår å presentere konkrete rentebesparelser som fakta, og fremstiller koblingen til bank og risiko som en hypotese/forskningsspørsmål.
  - **Markedsandeler og tall**: Fullt samsvar. Alle bransjetall (som byggefeil på 10–30 mrd. og konflikter på 2,2 mrd.) har korrekte og eksplisitte kildehenvisninger.
  - **Partnere**: Ingen brudd. Verken NorDan eller Tirna Fagskole er nevnt i disse dokumentene, så det er ingen feilaktig fremstilling av deres status.
  - **VIBS-score**: Fullt samsvar. Scoren fremstilles ikke som en uavhengig tredjepartssertifisering, men som en relativ modell innenfor produktkategorier.
  - **Bærekraft**: Fullt samsvar. Bærekraft presenteres gjennomgående som økonomi og ressursbesparelse, helt uten moralske pekefingre.

---

## 2. Detaljert søkeresultat for AI-buzzwords og sjargong

### AI-buzzwords (AI, kunstig intelligens, agent, maskinlæring, algoritme, llm, gpt, neural, deep learning)
Det ble søkt systematisk gjennom begge dokumentene. Ingen av ordene ble funnet.

### Sjargong (Jargon)
Følgende forekomster av sjargong ble funnet og bør modereres:

| Dokument | Linje | Sjargong-uttrykk | Kontekst | Forslag til endring |
| :--- | :--- | :--- | :--- | :--- |
| `ipn-samledokument.md` | 24 | *digitaliserte*, *fragmenterte* | "...en av de minst digitaliserte og mest fragmenterte." | "...lavest grad av IT-bruk og består av mange små aktører." |
| `ipn-samledokument.md` | 26 | *siloer* | "...de lever i atskilte siloer..." | "...de er lagret i ulike systemer uten kobling..." |
| `ipn-samledokument.md` | 47, 49 | *syntesen* | "Det er denne syntesen...", "Hvorfor syntesen hever..." | "sammenstillingen", "koblingen av dataene" |
| `ipn-samledokument.md` | 40, 45, 52 | *robust*, *robusthet* | "...kvalitet og robusthet...", "...både forklarbar, etterprøvbar og robust..." | "holdbarhet", "pålitelig" |
| `ipn-hovedokument.md` | 43 | *operasjonalisert* | "...ikke operasjonalisert." | "...ikke tatt i bruk i praktiske verktøy." |
| `ipn-hovedokument.md` | 91 | *regulatorisk medvind* | "...gir regulatorisk medvind." | "...gir drahjelp fra kommende regelverk." |

---

## 3. Komplekse setninger og lange ord

### Analyse av komplekse setninger
Dokumentene inneholder flere setninger som er for lange og tunge for optimal lesbarhet.

#### Eksempel 1 (`ipn-samledokument.md` - Linje 26)
- **Før:** `Miljødeklarasjoner (EPD), produktdata i NOBB, livsløpskostnader og levetidsdata eksisterer — men de lever i atskilte siloer, er bygget for spesialister i prosjekteringsfasen, og er ikke koblet til den beslutningen som faktisk avgjør utslipp og kvalitet: valget av produkt og løsning i tilbudsfasen.` (41 ord)
- **Problem:** Mange innskutte ledd, tankestrek, kolon og passiv form.
- **Etter:** `Selv om miljødeklarasjoner (EPD), produktdata i NOBB og levetidsdata eksisterer, er dataene i dag spredt i ulike systemer. De er i hovedsak utviklet for spesialister i prosjekteringsfasen. Dermed kobles de ikke til tilbudsfasen, der de faktiske valgene av produkt og løsning tas.` (42 ord fordelt på 3 setninger. Gjennomsnittlig setningslengde redusert fra 41 til 14 ord).

#### Eksempel 2 (`ipn-samledokument.md` - Linje 36)
- **Før:** `Hver enkelt byggekloss finnes allerede og er faglig moden: standardene for livsløpsvurdering og livsløpskostnad er etablerte (EN 15978:2026; ISO 15686-5; NS-EN 16627), datainfrastrukturen modnes gjennom EPD-systemet, NOBB og det kommende digitale produktpasset (DPP, forordning (EU) 2024/3110), og metodene for å veie kriterier mot hverandre er veletablerte i forskningslitteraturen (Mecca 2023).` (60 ord)
- **Problem:** Ekstremt lang setning med kolon, parenteser, semikolon og flere sideordnede hovedsetninger.
- **Etter:** `De nødvendige byggeklossene finnes allerede og er faglige modne. Standardene for livsløpsvurdering og livsløpskostnad er etablerte (EN 15978:2026; ISO 15686-5; NS-EN 16627). Samtidig modnes datainfrastrukturen gjennom EPD-systemet, NOBB og det kommende digitale produktpasset (DPP, forordning (EU) 2024/3110). Metodene for å veie ulike kriterier mot hverandre er også veletablerte (Mecca 2023).` (56 ord fordelt på 4 setninger. Gjennomsnittlig setningslengde redusert til 14 ord).

#### Eksempel 3 (`ipn-samledokument.md` - Linje 51)
- **Før:** `Å slå dem sammen til ett tall som viser hvor sikkert grunnlaget er — i stedet for å gjemme svakheten i én totalscore — er fortsatt et uløst forskningsspørsmål (Benke et al. 2025; Lohman et al. 2023).`
- **Problem:** Tunge innskutte setninger markert med tankestrek mellom subjekt og verbal.
- **Etter:** `Å slå disse sammen til en samlet poengsum som synliggjør usikkerheten, i stedet for å skjule den, er fortsatt et uløst forskningsspørsmål (Benke et al. 2025; Lohman et al. 2023).`

---

## 4. Brudd på guardrails: Produktstatus (MVP vs. ferdig)

I `ipn-samledokument.md` beskrives VIBS og VERIFIED i presens som om funksjonene allerede eksisterer og leverer verdi. Her er de konkrete bruddene og anbefalte omskrivinger:

### Forekomst 1 (`ipn-samledokument.md` - Linje 10)
- **Før:** `VIBS er en plattform for små og mellomstore byggebedrifter som samler prosjektstyring, dokumentasjon, kommunikasjon og kvalitet på ett sted — uten tunge systemer og dyre abonnement. VERIFIED er forskningsdelen: en modell som gir hvert produkt- og løsningsvalg en etterprøvbar score basert på pris, levetid...`
- **Problem:** Fremstiller plattformen og score-modellen som ferdig operative.
- **Etter:** `VIBS er under utvikling som en plattform for små og mellomstore byggebedrifter. Den er designet for å samle prosjektstyring, dokumentasjon, kommunikasjon og kvalitet på ett sted, uten tunge systemer og dyre abonnement. Forskningsprosjektet VERIFIED skal utvikle en modell som gir hvert produkt- og løsningsvalg en etterprøvbar score basert på pris, levetid...`

### Forekomst 2 (`ipn-samledokument.md` - Linje 14)
- **Før:** `VERIFIED flytter beslutningsgrunnlaget dit, og gjør bærekraft til en konsekvens av bedre økonomi og lavere risiko...`
- **Problem:** Påstand om aktiv leveranse av verdi i presens.
- **Etter:** `VERIFIED skal flytte beslutningsgrunnlaget dit, og vil bidra til å gjøre bærekraft til en konsekvens av bedre økonomi og lavere risiko...`

### Forekomst 3 (`ipn-samledokument.md` - Linje 28)
- **Før:** `VERIFIED adresserer ikke mangel på data, men mangelen på en bro fra data til beslutning — et grunnlag en SMB-entreprenør eller boligkjøper kan bruke i tilbudsfasen...`
- **Problem:** Presenteres som aktiv løsning.
- **Etter:** `Forskningsprosjektet VERIFIED skal ikke adressere mangel på data, men mangelen på en bro fra data til beslutning. Målet er å utvikle et grunnlag som en SMB-entreprenør eller boligkjøper kan bruke i tilbudsfasen...`

### Forekomst 4 (`ipn-samledokument.md` - Linje 65)
- **Før:** `VERIFIED gjør et produktvalg om til en sammenliknbar score. Forenklet: hver dimensjon gis 0–100 poeng...`
- **Problem:** Beskriver poengberegning som aktiv funksjonalitet.
- **Etter:** `VERIFIED er designet for å gjøre et produktvalg om til en sammenliknbar score. Modellen legger opp til at hver dimensjon skal gis 0–100 poeng...`

### Forekomst 5 (`ipn-samledokument.md` - Linje 133-139 - Tabellpåstander)
I tabellen over "Sannhetsserum" er påstandene formulert som absolutte sannheter i presens:
- **Før:** 
  - `VIBS reduserer CO₂ fra materialvalg`
  - `VIBS reduserer byggfeil og omarbeid`
  - `VIBS hjelper SMB med bærekraft`
  - `VIBS gir bedre grønn bankdokumentasjon`
  - `VIBS bidrar til do-not-harm`
- **Problem:** Selv om tabellen viser svak bevisstyrke, bryter påstandene med regelen om å ikke hevde at uferdige produkter "leverer" resultater.
- **Etter:**
  - `Mål om å redusere CO₂ fra materialvalg`
  - `Potensial for redusert byggefeil og omarbeid`
  - `Støtte til SMB for bærekraftsvalg`
  - `Mål om bedre grønn bankdokumentasjon`
  - `Planlagt dokumentasjon av do-not-harm (DNSH)`

---

## 5. Konklusjon og handlingsliste

Dokumentene holder generelt høy faglig kvalitet, men språket må strammes opp før formell søknadsinnføring for å møte VIBS' egne kvalitetsstandarder:

1. **Endre tempus til futurum eller hensikt**: Alle steder der VIBS-plattformen eller VERIFIED-scoren omtales i presens som en aktiv leveranse, må det skrives om til fremtidsform (*"skal"*, *"vil"*, *"er designet for"*).
2. **Splitt komplekse setninger**: Gå gjennom og splitt alle setninger med over 25 ord eller mer enn to innskutte bisetninger.
3. **Erstatt/forklar sjargong**: Fjerne unødvendig akademisk/strategisk fyllord og erstatte dem med mer dagligdagse og konkrete ord.
4. **Behold god praksis**: Fortsette å referere grundig til alle eksterne tall og unngå moralske bærekraftsargumenter.
