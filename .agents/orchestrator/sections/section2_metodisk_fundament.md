# Seksjon 2: Metodisk fundament (LCA/LCC og datakvalitet)

## 2.1 Oversikt og metodisk innramming

Det metodiske fundamentet for verifisert og bærekraftig beslutningsstøtte i byggenæringen hviler på to komplementære analysegrenser: **klimagass- og miljøvurdering gjennom livsløpsanalyse (LCA - Life Cycle Assessment)** og **økonomisk livssyklusanalyse (LCC - Life Cycle Costing)**. I dagens praksis behandles miljøpåvirkning og levetidskostnader som adskilte fagsiloer, hovedsakelig tilpasset spesialister i prosjekteringsfasen etter at de vesentligste arkitektoniske og materialmessige rammene er låst `[Nordic2023]` 🟢.

For at små og mellomstore entreprenører (SMB) og deres kunder skal kunne foreta kunnskapsbaserte og bærekraftige **løsningsvalg** allerede i **tilbudsfasen**, kreves et integrert datagrunnlag der miljødata, kostnader, levetidsintervaller og skaderisiko sammenstilles transparent `[BKA2]` 🟢. VERIFIED-prosjektet har som mål å utvikle og teste en **beslutningsstøtte** som sammenligner heterogene byggevaredata i en intuitiv **testflate**, der datakvalitet og usikkerhet eksplisitt synliggjøres i stedet for å skjules bak en skjult totalscore `[Edelen2018]` 🟢 `[Lohman2023]` 🟢.

Denne seksjonen gjennomgår det vitenskapelige, regulatoriske og standardiserte fundamentet for LCA, LCC, datakvalitetsindikatorer (DQI) og usikkerhetsmodellering som utgjør state of the art for prosjektets testflate.

---

## 2.2 Vugge-til-port-dominans: 70 % A1–A3-regelen `[KD2024]` 🟡

Embodied carbon (innbygd karbon) utgjør en stadig økende andel av et byggs samlede livsløpsutslipp etter hvert som driftsfasens energibruk (modul B6) effektiviseres gjennom skjerpede energikrav `[KD2024]` 🟡 `[EBA_NO2023]` 🟡. Kartlegginger utført av Multiconsult og Direktoratet for byggkvalitet (DiBK, 2023/2024) i 4 representative referansebyggtyper (boligblokk, yrkesbygg/kontor, enebolig og rekkehus/skole) dokumenterer at materialrelaterte utslipp i livsløpsmodulene A1–A3 utgjør **63 % til 70 % (avrundet til 70 %)** av de totale materialrelaterte klimagassutslippene over byggets levetid `[KD2024]` 🟡.

### Modulenes definisjon i EN 15804+A2 `[EN15804]` 🟡:
- **Modul A1:** Råvareuttak og utvinning (cradle/vugge).
- **Modul A2:** Transport av råvarer til foredling og fabrikk.
- **Modul A3:** Produksjon og fremstilling av byggevarer ved fabrikkport (gate).

Sluttresultatet for modulsammenstillingen A1–A3 betegnes som *cradle-to-gate* (vugge-til-port). De resterende 30 % av materialutslippene fordeler seg på byggeplass/transport til byggeplass (A4–A5), utskifting og vedlikehold i driftsfasen (B2–B4), samt sluttfase og avhending (C1–C4) `[EN15804]` 🟡.

### Betydning for tilbudsfasen og VERIFIEDs beslutningsstøtte
70 %-dominansen i A1–A3 innebærer at de mest avgjørende utslippsreduksjonene oppnås ved valg av materialer, leverandører og produksjonsteknologier før byggeprosessen starter `[KD2024]` 🟡. I tilbudsfasen har entreprenøren og kunden fortsatt fleksibilitet til å vurdere alternative **løsningsvalg** (f.eks. lavkarbonbetong vs. konvensjonell betong, eller hulldekker vs. massivtre) `[EBA_NO2023]` 🟡. Når tilbudet er akseptert og prosjekteringen låst, begrenses handlingsrommet dramatisk. 

VERIFIED skal undersøke om en testflate som vektlegger A1–A3-data i tilbudsfasen gjør det mulig for ikke-spesialister å identifisere og velge lavutslippsalternativer med høy effekt tidlig i prosjektløpet `[BKA2]` 🟢 `[KD2024]` 🟡.

---

## 2.3 TEK17 § 9-2 og sikkerhetsfaktoren på 1,25 (+25 % påslag for generiske data)

Norsk byggteknisk forskrift (TEK17) § 9-2 stiller krav om at klimagassregnskap skal utarbeides for boligblokker og yrkesbygg basert på NS 3720 / EN 15978 `[EN15978-2026]` 🟢¹. Ved beregning av klimagassutslipp fra materialer skiller forskriften og DiBKs retningslinjer strengt mellom spesifikke og generiske miljødeklarasjoner:

1. **Spesifikk EPD (Environmental Product Declaration):** Tredjepartsverifisert miljadeklarasjon i henhold til NS-EN 15804+A2 `[EN15804]` 🟡 for et konkret produkt fra en spesifikk produsent. Brukes med faktiske, dokumenterte utslippstall uten straffepåslag.
2. **Generiske LCA-data:** Standardiserte gjennomsnittsdata fra databaser (f.eks. ecoinvent `[ecoinvent]` 🟡 eller Norsk Treteknisk Institutt) som benyttes dersom spesifikk EPD mangler.

### Regulatorisk sikkerhetsfaktor (+25 % utslippsstraff)
For å ta høyde for usikkerhet, spredning i produksjonsteknologi og manglende sporbarhet ved bruk av generiske kilder, pålegger det norske regelverket og NS 3720 at generiske klimagassfaktorer skal multipliseres med en **sikkerhetsfaktor på 1,25** (+25 % utslippspåslag) `[EN15804]` 🟡 `[KD2024]` 🟡. 

$$\text{Klimagassutslipp}_{\text{generisk}} = \text{Utslippsfaktor}_{\text{databasetall}} \times 1{,}25$$

### Operasjonalisering i VERIFIEDs testflate
I VERIFIEDs testflate benyttes denne 1,25-faktoren som et aktivt pedagogisk og incitamentskapende verktøy for beslutningsstøtte:
- Når en entreprenør vurderer et løsningsvalg uten spesifikk EPD, flagges datagrunnlaget som *«Generelt (påført +25 % TEK17-sikkerhetsfaktor)»*.
- Testflaten viser umiddelbart den beregnede gevinsten dersom leverandøren fremskaffer en verifisert, spesifikk EPD som fjerner straffepåslaget.
- Dette gir gjennomsiktig informasjon til både entreprenør og kunde om hvor usikkerheten ligger, uten å stoppe kalkylen eller skjule datagrunnlaget `[Edelen2018]` 🟢.

---

## 2.4 Datakvalitet og usikkerhetsmodellering: Weidema Pedigree-matrise

For å gi strukturert beslutningsstøtte basert på heterogene datakilder må usikkerheten i livsløpsinventaret (LCI) kvantifiseres systematisk. Det vitenskapelige standardrammeverket for dette er **Weidema Pedigree-matrisen**, opprinnelig utviklet av Weidema & Wesnæs (1996) `[Weidema1996]` 🟡 og videreutviklet med empiriske usikkerhetsfaktorer av Ciroth et al. (2016) `[Ciroth2016]` 🟡.

### De 5 datakvalitetsindikatorene (DQIs)
Pedigree-matrisen vurderer hvert datapunkt i et LCI-sett langs fem uavhengige kvalitetsdimensjoner, der hver indikator tildeles en skår fra **1 (best/høyest kvalitet)** til **5 (dårligst/lavest kvalitet)**:

| DQI-nr. | Datakvalitetsindikator (DQI) | Beskrivelse og vurderingskriterium | Skår 1 (Best) | Skår 5 (Dårligst) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Pålitelighet** (*Reliability*) | Datainnsamlingsmetodikk, målekvalitet og grad av uavhengig verifikasjon. | Verifiserte primærdata basert på kontinuerlige målinger. | Uverifiserte skjønnsmessige estimater eller ukjente kilder. |
| **2** | **Kompletthet** (*Completeness*) | Statistisk representativitet og andel steder/bedrifter inkludert i utvalget. | Data fra 100 % av relevante steder over tilstrekkelig tidsrom. | Data fra under 50 % av steder eller fra et lite utvalg bedrifter. |
| **3** | **Tidsmessig korrelasjon** (*Temporal correlation*) | Tidsavvik mellom dataenes innsamlingsår og prosjektets vurderingsår. | Data fra under 3 år før vurderingsåret. | Data fra mer enn 15 år før vurderingsåret. |
| **4** | **Geografisk korrelasjon** (*Geographical correlation*) | Geografisk samsvar mellom datakildens opprinnelse og norsk/lokalt byggested. | Data fra det spesifikke lokasjonsområdet (Norge). | Data fra ukjent region eller regioner med helt ulik energimiks. |
| **5** | **Teknologisk korrelasjon** (*Technological correlation*) | Samsvar mellom den modellerte prosessen/teknologien og den faktiske byggevaren. | Data fra nøye tilpasset, spesifikk produksjonsteknologi. | Data fra vesentlig ulik teknologisk prosess eller generisk proxy. |

### Stokastisk usikkerhets propagering i ecoinvent `[ecoinvent]` 🟡
I den globale databasen ecoinvent oversettes de fem kvalitetsindikatorene ($i \in \{1, 2, 3, 4, 5\}$) til kvadratiske lognormale variansfaktorer ($\sigma_i^2$). Sammen med en grunnleggende usikkerhetsfaktor ($\sigma_{\text{basic}}^2$) beregnes den samlede geometriske standardavviksfaktoren ($\text{SD}_{95}$) for datapunktet `[ecoinvent]` 🟡 `[Ciroth2016]` 🟡:

$$\ln(\text{SD}_{95}) = \sqrt{\sigma_{\text{basic}}^2 + \sum_{i=1}^{5} \sigma_i^2}$$

Denne lognormale fordelingen danner grunnlaget for Monte Carlo-simuleringer, der tusenvis av iterasjoner genererer konfidensintervaller for utslippstallene. VERIFIED bygger på dette matematiske fundamentet for å synliggjøre konfidensintervaller i løsningssammenligningen `[Lohman2023]` 🟢.

---

## 2.5 Formålsavhengig datakvalitetsrammeverk: Edelen & Ingwersen (2018) `[Edelen2018]` 🟢

Mens Pedigree-matrisen leverer den matematiske konverteringen til varians, etablerer **Edelen & Ingwersen (2018)** `[Edelen2018]` 🟢 (*International Journal of Life Cycle Assessment*) det metodiske prinsippet for hvordan datakvalitet skal forvaltes og fremstilles i beslutningsprosesser.

### Hovedprinsipp: Formålsavhengig vurdering uten skjult totalscore
Edelen & Ingwersen dokumenterer at datakvalitet må vurderes eksplisitt i forhold til **formål, kontekst og den spesifikke beslutningsrollen** `[Edelen2018]` 🟢. Et helt avgjørende metodisk krav er at **datakvalitetsindikatorer ALDRI må aggregeres eller summeres til én enkelt komposittscore (skjult totalscore)**.

#### Begrunnelse mot skjult totalscore:
1. **Ikke-kompensatorisk natur:** Høy skår i én kvalitetsdimensjon kan aldri oppveie et kritisk avvik i en annen. Eksempelvis kan ikke et datasetts ferske tidsmessige stempel (DQI 3 = 1) kompensere for at dataene stammer fra et helt annet kontinent med ulik energimiks og teknologi (DQI 4 = 5). Å midle disse tallene gir en tilsynelatende «middels» score (3,0) som maskerer en alvorlig geografisk feilkilde.
2. **Beslutningsforvrengning:** En sammenhektet single-point score skjuler hvor usikkerheten ligger, og forhindrer brukeren i å ta stilling til om avviket er akseptabelt for det konkrete løsningsvalget.

### Konsekvenser for VERIFIEDs ontologi og testflate
I samsvar med Edelen & Ingwersen (2018) `[Edelen2018]` 🟢 og prosjektets ontologiske guardrails (`vibs-verified-ord-og-kildekart-v0.5.yml`) avviser VERIFIED alle former for skjulte totalscorer eller «svart boks»-vektingsmodeller. Testflaten skal i stedet eksponere datakvalitetsstatusen langs fire krystallklare kategorier:
- 🟢 **Verifisert:** Produktspesifikk EPD/FDV-dokumentasjon (DQI skår 1–2).
- 🟡 **Generelt:** Standard databasetall påført TEK17 1,25-sikkerhetsfaktor (DQI skår 3).
- 🟠 **Estimert:** Proxydata basert på lignende materialkategorier (DQI skår 4).
- 🔴 **Manglende data:** Eksplisitt synliggjort datagap som påkaller oppmerksomhet (DQI skår 5).

Dette sikrer at entreprenør og kunde får beslutningsstøtte med full transparens om datagrunnlagets pålitelighet `[Edelen2018]` 🟢 `[Lohman2023]` 🟢.

---

## 2.6 Standardiseringsrammeverket for bygg-LCA: EN 15978:2026, ISO 14040/14044 og EN 15804+A2

For at klimagassberegninger i VERIFIED skal ha juridisk og faglig autoritet overfor banker, byggherrer og myndigheter, må alle kilder og beregninger forankres i gjeldende europeiske og internasjonale standarder.

### EN 15978:2026 (CEN-CENELEC 17.04.2026) `[EN15978-2026]` 🟢¹
**EN 15978:2026** (*Bærekraftige byggverk - Vurdering av bygningers miljøprestasjon - Beregningsmetode*) ble offisielt publisert av CEN-CENELEC den **17. april 2026** og erstatter den eldre 2011-versjonen `[EN15978-2026]` 🟢¹. Standardoppdateringen representerer et gjennombrudd for sirkulærøkonomi og rehabiliteringsprosjekter:
- **Utvidet virkeområde:** Standarden omfatter nå eksplisitt både nybygg, eksisterende bygningsmasse, større ombygginger og **rehabiliteringsprosjekter**.
- **Harmonisert modulstruktur:** Etablerer strenge regler for aggregering av produkt-EPD-er over moduler A1–A3, A4–A5, B1–B7, C1–C4 og modul D (Gjenbruk, gjenvinning og energigjenvinning utenfor systemgrensen).
- **Systemgrenser for ombruk:** Standarden gir entydige beregningsregler for bevaring av eksisterende bygningsdeler og ombruk av brukte byggevarer, noe som er direkte relevant for VERIFIEDs vurdering av rehabiliteringsalternativer vs. nybygg.

### ISO 14040/14044:2006 `[ISO14040]` 🟡
ISO 14040 og ISO 14044 utgjør det generelle metodiske fundamentet for livsløpsvurderinger (LCA). Standarden definerer de fire obligatoriske fasene i en LCA-studie: (1) Mål- og omfangsdefinisjon, (2) Inventaranalyse (LCI), (3) Konsekvensanalyse (LCIA), og (4) Tolkning.

### NS-EN 15804:2012+A2:2019 `[EN15804]` 🟡
EN 15804+A2 er kjernestandarden for utarbeidelse av miljødeklarasjoner (EPD) for byggevarer i Europa. Fra oktober 2022 krever A2-revisjonen at alle nye EPD-er obligatorisk må rapportere utslipp og miljøpåvirkninger for modulene A1–A3, C1–C4 og D, noe som sikrer at avhendings- og gjenbrukspotensialet alltid er dokumentert `[EN15804]` 🟡.

### Praktikervariabilitet og databasedifferanser: Benke et al. (2025) `[Benke2025]` 🟢
Nylig publisert empirisk forskning av Benke et al. (2025) `[Benke2025]` 🟢 i *Scientific Data* (PMC12218139) understreker hvorfor standardisering og transparent datakvalitet er tvingende nødvendig. Ved analyse av 292 bygg-LCA-prosjekter avdekket forfatterne at industri-genererte LCA-resultater sjelden samles i sammenlignbare åpne databaser, og at kommersielle verktøy (som One Click LCA og Tally) oppviser vesentlige avvik seg imellom på grunn av ulikheter i bakgrunnsdata (LCI-databaser), standardforutsetninger for scenerier og modellørenes personlige skjønn `[Benke2025]` 🟢. Dette empiriske funnet bekrefter VERIFIEDs hypoteser om at verktøyuavhengig, gjennomsiktig dataintegrasjon er påkrevd.

---

## 2.7 Livssykluskostnader (LCC): NS-EN 16627 og ISO 15686-5 (og tilbaketrekkingen av NS 3454)

Bærekraftige **løsningsvalg** i tilbudsfasen kan ikke vurderes ut fra klimagassutslipp alene. Et alternativ med lave A1–A3-utslipp kan vise seg å ha kort levetid, høye vedlikeholdskostnader eller høy skaderisiko, noe som vil medføre betydelige økonomiske og miljømessige belastninger i driftsfasen. LCC-analyser er derfor en integrert del av beslutningsstøtten.

### ISO 15686-5:2017 `[ISO15686-5]` 🟡
ISO 15686-5 (*Buildings and constructed assets - Service life planning - Part 5: Life cycle costing*) etablerer internasjonale prinsipper for beregning av livssykluskostnader i bygg. Standarden definerer nåverdisammenstillinger (Net Present Value - NPV), kapitalutgifter (CapEx), driftsutgifter (OpEx), samt vedlikeholds- og utskiftingskostnader over en definert kalkylperiode.

### NS-EN 16627 `[NS-EN16627]` 🟢
NS-EN 16627 (*Bærekraftige byggverk - Vurdering av bygningers økonomiske prestasjon - Beregningsmetoder*) er den gjeldende norsk-europeiske standarden for LCC-beregninger på byggnivå. Standarden samkjører kostnadsmodulene direkte med LCA-modulstrukturen i EN 15978 (A1–A5, B1–B7, C1–C4).

### Kritisk regulatorisk avklaring: Tilbaketrekkingen av NS 3454 `[NS-EN16627]` 🟢
En svært viktig faglige avklaring for VERIFIED-prosjektet gjelder den nasjonale standarden NS 3454 (*Livssykluskostnader for byggverk*):
- **NS 3454 ble offisielt TRUKKET TILBAKE den 7. september 2023** av Standard Norge `[NS-EN16627]` 🟢.
- Standarden ble erstattet av **NS-EN 16627**, i kombinasjon med NS-EN ISO 15686-5.
- **Formelt krav til VERIFIED:** Prosjektet og dets dokumentasjon skal **aldri** referere til utgåtte NS 3454 som gjeldende beregningsgrunnlag, men konsekvent forankre LCC-strukturen i **NS-EN 16627** og **ISO 15686-5** `[NS-EN16627]` 🟢 `[ISO15686-5]` 🟡.

### Integrasjon av levetider og vedlikeholdsintervaller `[Byggforsk700.320]` 🟡
For å beregne realistiske LCC-tall i tilbudsfasen benytter VERIFIED standardiserte levetidsdata fra **Byggforskserien 700.320** (*Intervaller for vedlikehold og utskifting av bygningsdeler*) `[Byggforsk700.320]` 🟡. Anvisningen gir veiledende intervaller for utskifting og service. I henhold til det eksplisitte forbeholdet i anvisningen skal disse tabellintervallene *ikke benyttes som eksakte levetidssvar for en konkret eksisterende bygningsdel*, men som statistiske utgangsverdier i kalkylen `[Byggforsk700.320]` 🟡. Usikkerheten i levetidsangivelsene behandles i henhold til DQI-prinsippene i § 2.5 `[Edelen2018]` 🟢.

---

## 2.8 Oppsummering og metodiske føringer for VERIFIEDs testflate

Tabellen nedenfor oppsummerer det metodiske fundamentet, kildenes portstatus og de operative føringene for utviklingen av VERIFIEDs testflate:

| Metodisk element | Primærkilde / Standard | Port-status | Operativt krav til VERIFIEDs testflate |
| :--- | :--- | :---: | :--- |
| **A1–A3 Dominans (70 %)** | Multiconsult / DiBK (2023/2024) `[KD2024]` | 🟡 | Prioritere A1–A3 EPD-data i tilbudsfasen der reduksjonspotensialet er størst før prosjekteringslås. |
| **TEK17 1,25-sikkerhetsfaktor** | TEK17 § 9-2 / DiBK / NS 3720 `[EN15804]` | 🟡 | Synliggjøre +25 % utslippsstraff på generiske data; vise gevinst ved innhenting av spesifikk EPD. |
| **Stokastisk usikkerhet (5 DQIs)** | Weidema & Wesnæs (1996) `[Weidema1996]` / ecoinvent `[ecoinvent]` | 🟡 | Konvertere DQI-skår (1–5) til lognormale variansfaktorer for Monte Carlo-baserte konfidensintervaller. |
| **Formålsavhengig datakvalitet** | Edelen & Ingwersen (2018) `[Edelen2018]` | 🟢 | **Forbud mot skjult totalscore/svart boks.** Vise flerdimensjonal datastatus (verifisert, generell, estimert, mangler). |
| **Bygg-LCA & Rehabilitering** | EN 15978:2026 (publisert 17.04.2026) `[EN15978-2026]` | 🟢¹ | Følge harmonisert modulstruktur (A1–D); anvende oppdaterte beregningsregler for rehabilitering vs. nybygg. |
| **LCC-beregningsstandard** | NS-EN 16627 `[NS-EN16627]` / ISO 15686-5 `[ISO15686-5]` | 🟢 / 🟡 | **Forankre LCC i NS-EN 16627.** Eksplisitt unngå referanse til tilbaketrukket NS 3454 (trukket 07.09.2023). |
| **Levetidsintervaller** | Byggforskserien 700.320 `[Byggforsk700.320]` | 🟡 | Benytte veiledende utskiftingsintervaller for LCC med synliggjort usikkerhetsforbehold. |
| **Praktikervariabilitet** | Benke et al. (2025) `[Benke2025]` | 🟢 | Dokumentere behovet for verktøyuavhengig, gjennomsiktig dataintegrasjon uten leverandørskjønn. |

---
*Rapportseksjon 2 er utarbeidet i henhold til ontologiske begrepsregler i `vibs-verified-ord-og-kildekart-v0.5.yml` og autoritativ kildedom.*
