# Section 4: Finans- og reguleringskontekst

**Dokumentstatus:** Arbeidsutkast for VERIFIED State of the Art-rapport (v0.5)  
**Målgruppe:** SINTEF-evaluering og Norsk forskningsråd (NFR IPN 2026)  
**Kilde- og ontologikontroll:** Verifisert i tråd med `vibs-verified-ord-og-kildekart-v0.5.yml`, `ipn-kildebibliotek.md` og `vibs-verified-kildedom-2026-06-27.md`.

---

## 4.1 Innledning og overordnet finansielt rammeverk

Eiendoms- og byggesektoren utgjør en dominerende del av finanssektorens utlånsporteføljer. I Norge utgjør eiendom og boliglån over 60 % og opp mot to tredjedeler av bankenes samlede utlån (`[FinanceNorway2018]` 🟡; `[Multiconsult2023]` 🟡). Finansielle institusjoner er dermed eksponert for både fysisk klimarisiko (som akutte fuktskader og ekstreme værhendelser) og overgangsrisiko (som regulatoriske krav til energimerking, karbonavgifter og tekniske bygningsstandarder).

Offisiell skadestatistikk fra Finans Norge 2023 (`[FinansNorge2024VASK]` 🟢) dokumenterer et betydelig omfang av fysiske bygningsskader i Norge: det registreres i gjennomsnitt **10 vannskader i timen** (tilsvarende ca. 87 600 skader årlig), med et samlet erstatningsutbetalingsvolum på **5,1 milliarder kroner i 2023**. Dette understreker at bygningsteknisk kvalitet, fuktrobusthet og vedlikehold har direkte og umiddelbare økonomiske konsekvenser for forsikringsselskaper og eiendomseiere.

Samtidig stiller regulatoriske organer og investorer stadig strengere krav til ESG-rapportering og klimarisikostyring. Finansielle aktører etterspør i økende grad strukturerte, etterprøvbare bygningsdata for å klassifisere grønne utlånsporteføljer i henhold til EU-taksonomien (`[EUTax]` 🟡) og EUs direktiv om bærekraftsrapportering (CSRD / Omnibus I `[OmnibusI]` 🟡).

I denne konteksten skal prosjektet VERIFIED utvikle og teste en **testflate** for **beslutningsstøtte** som setter **entreprenør og kunde** (herunder **ikke-spesialister** i SMB-segmentet) i stand til å sammenligne alternative **løsningsvalg** allerede i **tilbudsfasen**. Beslutningsmodellen skal framstille forutsigbare avveininger mellom klimagassutslipp (LCA per EN 15978:2026 `[EN15978-2026]` 🟢), livsløpskostnader (LCC per NS-EN 16627 `[NS-EN16627]` 🟢 og ISO 15686-5 `[ISO15686-5]` 🟡), teknisk levetid og fuktrobusthet — med **synlig datagrunnlag og usikkerhet** fremfor skjulte totalskårer.

---

## 4.2 Empirisk litteratur om energi- og klimaeffektivitet vs. misligholdsrisiko (PD)

Det finnes et etablert og empirisk dokumentert forskningsgrunnlag som viser en sammenheng mellom bygningers energieffektivitet og finansiell kredittrisiko, målt ved misligholdssannsynlighet (Probability of Default, PD). Tre sentrale studier danner det empiriske fundamentet for denne sammenhengen:

### 1. Kaza et al. (2014) — Boliglånsrisiko i USA 🟢
- **Kilde:** Kaza, N., Quercia, R.G. & Tian, C.Y. (2014). *Home Energy Efficiency and Mortgage Risks.* Cityscape, 16(1), 279–298 (`[Kaza2014]` 🟢).
- **Datagrunnlag og funn:** Analyserte ca. 71 000 residensielle boliglån i USA. Studien dokumenterer at eiere av ENERGY STAR-sertifiserte boliger har i gjennomsnitt **~32 % lavere misligholdssannsynlighet (PD)** enn eiere av uverifiserte boliger, kontrollert for inntekt, belåningsgrad (LTV) og kredittskår.
- **Mekanisme:** Lavere og mer forutsigbare energikostnader frigjør likviditet i husholdningsbudsjettet, noe som direkte reduserer faren for betalingsmislighold under økonomiske sjokk.
- **Status og omfang:** 🟢 **Bærende primærkilde**. Gjelder eksplisitt residensielle boliglån.

### 2. Billio et al. (2022) — Boliglånsrisiko i Nederland 🟢
- **Kilde:** Billio, M., Costola, M., Pelizzon, L. & Riedel, M. (2022). *Buildings' Energy Efficiency and the Probability of Mortgage Default: The Dutch Case.* The Journal of Real Estate Finance and Economics, 65(3), 419–450. DOI: 10.1007/s11146-021-09838-0 (`[Billio2022]` 🟢).
- **Datagrunnlag og funn:** Empirisk undersøkelse av nederlandske residensielle boliglån. Studien dokumenterer en statistisk signifikant korrelasjon der bedre energimerkeklasse (EPC — Energy Performance Certificate, fra A til G) er forbundet med lavere misligholdssannsynlighet (PD).
- **Mekanisme:** Høyere energieffektivitet gir lavere løpende driftsutgifter og bedre verdibevaring i boligmarkedet, noe som styrker pantesikkerheten for banken og låntakers betalingsevne.
- **Status og omfang:** 🟢 **Bærende primærkilde**. Dokumenterer empirisk energi↔PD-sammenheng innenfor et europeisk residensielt boliglånsmarked.

### 3. An & Pivo (2020) — Kommersiell eiendom og CMBS 🟡
- **Kilde:** An, X. & Pivo, G. (2020). *Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms.* Real Estate Economics, 48(1), 7–42. DOI: 10.1111/1540-6229.12228 (`[An2020]` 🟡).
- **Datagrunnlag og funn:** Empirisk studie av kommersielle eiendomslån i det amerikanske CMBS-markedet (Commercial Mortgage-Backed Securities). Viser at LEED- og ENERGY STAR-sertifiserte næringsbygg har **34 % lavere misligholdsrisiko (PD)** sammenlignet med umerket kommersiell eiendom.
- **Viktig avgrensning og metodisk forbehold:** Studien gjelder **utsluttsomt kommersiell eiendom (CMBS)**, og må *aldri* overføres uforbeholdent til residensielle boliglån. Primærteksten har publiseringsforbehold / betalingsmur (Wiley 402) og har status 🟡 **Under avklaring** inntil SINTEF har fullføre primærverifisering av fullteksten.

---

## 4.3 Regulatorisk påtrykk og bankenes risikostyring

Finanssektorens etterspørsel etter bygningsnær miljø- og risikodata drives sterkt av europeiske og internasjonale finanstilsyn.

### 1. European Banking Authority — EBA EU 2023 🟢
- **Kilde:** European Banking Authority (15. desember 2023). *Report on Green Loans and Mortgages* (EBA/Op/2023/13) (`[EBA_EU2023]` 🟢).
- **Innhold og betydning:** EBA foreslår et frivillig europeisk merke for grønne lån og boliglån (EU Green Loan Label), samt en harmonisering av rapporteringskrav under boligkredittdirektivet (Mortgage Credit Directive, MCD). Rapporten konkluderer med at **manglende harmoniserte data, uverifisert dokumentasjon og fragmentert bygningsinformasjon** utgjør de største bindende flaskehalsene for at banker skal kunne tilby grønn finansiering til SMB-segmentet og bygningsrenovering.
- **Status:** 🟢 **Bærende primærkilde** for finansregulatoriske krav i banksektoren.

### 2. Bank of England — PS25/25 🟡
- **Kilde:** Bank of England Prudential Regulation Authority (desember 2025). *Enhancing banks' and insurers' approaches to managing climate-related risks* (PS25/25) (`[BoE_PS25-25]` 🟡).
- **Innhold og frist:** Erstatter de tidligere klimaforventningene fra SS3/19 (2019). PS25/25 stiller bindende krav om at banker og forsikringsselskaper skal integrere både fysisk klimarisiko og overgangsrisiko i sine kjernerammeverk for risikostyring, kredittvurdering og styrebehandling. Frist for fullstendig gjennomføring er **juni 2026**.
- **Status:** 🟡 **Under avklaring** (substans bekreftet via uavhengige fagkilder, primærdokumentasjonen krever formell verifisering).

### 3. Bank of England — DP1/25 🟡
- **Kilde:** Bank of England Prudential Regulation Authority (juli 2025). *Residential mortgages: LGD and PD estimation* (DP1/25) (`[BoE_DP1-25]` 🟡).
- **Innhold og presisering:** Diskuterer utfordringer og kapasitetsbegrensninger mellomstore banker møter når de skal utvikle egne IRB-modeller (Internal Ratings-Based) for å beregne misligholdssannsynlighet (PD) og tap ved mislighold (Loss Given Default, LGD) for residensielle boliglån.
- **Viktig ontologisk og faglige presisering:** DP1/25 omhandler **ikke klimarisiko direkte**, men representerer den underliggende kredittrisikoinfrastrukturen (IRB PD/LGD-modellene) som framtidig bygnings- og klimarisikodata må mates inn i.

---

## 4.4 Ontologisk og enhetsmessig distinksjon: EBA EU vs. EBA Norge

En av de viktigste kildekritiske og ontologiske kontrollreglene i VERIFIED-prosjektet er å opprettholde et **strengt og ufravikelig skille** mellom to helt ulike enheter som deler akronymet «EBA».

```
                  ┌─────────────────────────────────────────┐
                  │          AKRONYM: «EBA»                 │
                  └────────────────────┬────────────────────┘
                                       │
           ┌───────────────────────────┴───────────────────────────┐
           ▼                                                       ▼
┌──────────────────────────────┐                       ┌──────────────────────────────┐
│       [EBA_EU2023] 🟢        │                       │       [EBA_NO2023] 🟡        │
├──────────────────────────────┤                       ├──────────────────────────────┤
│ European Banking Authority   │                       │ Entreprenørforeningen –      │
│ (EU-organ for banktilsyn)    │                       │ Bygg og Anlegg (Norge)       │
├──────────────────────────────┤                       ├──────────────────────────────┤
│ Domene: Finansregulering,    │                       │ Domene: Byggebransje,        │
│ grønne boliglån, ESG, MCD    │                       │ materialvalg, klimagass i    │
│ (Report EBA/Op/2023/13)      │                       │ boligblokker (veileder 2023) │
└──────────────────────────────┘                       └──────────────────────────────┘
```

### Obligatoriske skillereregler:
1. **Fullt navn ved første gangs nevnelse:**
   - EU-kontekst: *«European Banking Authority (EBA EU) …»* (`[EBA_EU2023]` 🟢)
   - Norsk byggkontekst: *«Entreprenørforeningen – Bygg og Anlegg (EBA Norge) …»* (`[EBA_NO2023]` 🟡, utgitt i samarbeid med Grønn Byggallianse og Norsk Eiendom).
2. **Aldri slå sammen nøklene:** Det er strengt forbudt å bruke et generisk `[EBA]`. Finansielle vurderinger siterer utsluttsomt `[EBA_EU2023]` 🟢. Byggetekniske materialvurderinger (som viser at tidlige materialvalg kan gi inntil 20 % reduksjon i klimagassutslipp i boligblokker uten merkostnad) siterer utsluttsomt `[EBA_NO2023]` 🟡.

---

## 4.5 Det avgrensede FoU-gapet: Holdbarhet og fuktrobusthet til kredittrisiko

Selv om eksisterende forskning og regulering er moden innenfor visse delområder, avslører State of the Art-kartleggingen et tydelig og udekket forskningsgap.

### Kjernen i forskningshullet:
1. **Energisentrert etablert kunnskap:** Den empiriske litteraturen (Kaza et al. 2014 `[Kaza2014]` 🟢; Billio et al. 2022 `[Billio2022]` 🟢; An & Pivo 2020 `[An2020]` 🟡) dokumenterer at energieffektivitet (kWh/m²/år og energimerkeklasser) korrelerer med lavere misligholdsrisiko (PD).
2. **Det udekkede gapet (FoU-høyden):** Det finnes **null publisert empirisk litteratur** som kobler bygningsteknisk kvalitet, materialenes holdbarhet, levetid, fuktrobusthet eller vedlikeholdsbyrde direkte til finansiell kredittrisiko (PD og LGD).
3. **Regulatorisk svakhet i dagens grønne finans:** Gjeldende finansielle rammeverk (EU-taksonomien `[EUTax]` 🟡, EEMI `[EEMI]` 🟡, EBA grønne lån `[EBA_EU2023]` 🟢) er i stor grad snevert energisentrerte. De fanger ikke opp om et lavenergibygg er oppført med fuktutsatte materialer, har kort teknisk levetid eller pådrar seg store vedlikeholdsetterslep som over tid svekker panteobjektets verdi.

### VERIFIEDs forskningshypotese (FoU-spørsmål F1 og F5):
> **Prosjektet skal undersøke om** strukturerte bygningsdata om levetid, fuktrobusthet og vedlikeholdsintervaller (NS-EN 16627 `[NS-EN16627]` 🟢, Byggforskserien 700.320 `[Byggforsk700.320]` 🟡) kan oversettes til relevante risikoparametere for finans- og forsikringssektoren.

Dette utgjør prosjektets avgrensede nyhetsverdi på det finansielle området: å etablere en bro fra byggeteknisk kvalitet og DNSH-kriterier (Do No Significant Harm) til bankenes risikomodeller (IRB PD/LGD), tilrettelagt for enkel bruk av ikke-spesialister i tilbudsfasen.

---

## 4.6 Parkert status og kildeavklaringer

For å opprettholde streng kildekritikk og unngå sirkelargumentasjon, er enkelte kilder satt i parkert status (⏸) i samsvar med prosjektleders beslutning (Lars Gunnar, 2026-06-28):

1. **`[Wiik2025]` — SINTEF Notat nr. 57** (*Kostnadseffekten av klimatiltak i byggenæringen*, 2025):  
   - **Status:** ⏸ **Parkert**.
   - **Begrunnelse:** Dokumentet er et internt, uindeksert notat utarbeidet for konsortiet. Å sitere et internt notat for å bevise kostnadsnøytralitet utgjør sirkelargumentasjon.
   - **Erstatningskilder:** Påstander om at tidlige materialvalg kan gi betydelige utslippsreduksjoner uten merkostnad skal i stedet støttes av uavhengige, publiserte kilder som `[EBA_NO2023]` 🟡 (20 % reduksjon i boligblokker) og `[KD2024]` 🟡 (handlingsrom i tidligfase).

2. **`[SA2018]` — Samfunnsøkonomisk analyse Rapport 4-2018** (*Konflikter i bygg- og anleggsnæringen*):  
   - **Status:** ⏸ **Parkert** / 🟡 **Under avklaring**.
   - **Begrunnelse:** Rapporten er ikke bekreftet fysisk åpnet i offentlige registre i denne runden.
   - **Operativ regel:** Påstanden om 2,2 milliarder kroner i årlige konfliktkostnader kan ikke brukes som uforbeholdent primærbelegg før kildefilen er fysisk lokalisert og åpnet.

3. **`[NFR_IPN2026]` — Norsk forskningsråd IPN Utlysning 2026 (§10.1)** 🟢:  
   - **Status:** 🟢 **Bærende offisiell kilde**.
   - **Rammer:** Støttebeløp er avgrenset til **1–16 MNOK**, med en maksimal støttesats på **50 %** av prosjektets godkjente kostnader for bedriftspartnere.

---

## 4.7 Oppsummerende kildematrise for finans og regulering

Tabellen nedenfor oppsummerer de sentrale kildene som inngår i Section 4, deres domene, provenans og autoritative portstatus i henhold til `ipn-kildebibliotek.md`.

| Kildenøkkel | Tittel / Referanse | Domene | Provenans | Port-status | Primær rolle / Omfang i Section 4 |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `[Kaza2014]` | Kaza et al. (2014) *Cityscape* 16(1) | Akademia | Primær | 🟢 | Emne: Residensielle boliglån i USA (~32 % lavere PD for ENERGY STAR). |
| `[Billio2022]` | Billio et al. (2022) *JREFE* 65(3) | Akademia | Primær | 🟢 | Emne: Residensielle boliglån i Nederland (EPC energimerke korrelerer med lavere PD). |
| `[An2020]` | An & Pivo (2020) *Real Estate Econ.* 48(1) | Akademia | Primær | 🟡 | Emne: Kommersiell eiendom (CMBS, 34 % lavere PD for LEED/ENERGY STAR). betalingsmur. |
| `[EBA_EU2023]` | European Banking Authority (Dec 2023) | Finanstilsyn | Primær | 🟢 | Emne: EBA Green Loan Report (EBA/Op/2023/13); manglende data er bindende skranke. |
| `[BoE_PS25-25]`| Bank of England PS25/25 (Dec 2025) | Finanstilsyn | Sekundær | 🟡 | Emne: Klimarisikostyring i banker/forsikring; frist juni 2026. |
| `[BoE_DP1-25]` | Bank of England DP1/25 (July 2025) | Finanstilsyn | Sekundær | 🟡 | Emne: IRB PD/LGD-modellering for boliglån (ikke-klima infrastruktur). |
| `[FinansNorge2024VASK]`| Finans Norge Skadestatistikk (2023) | Forsikring | Offisiell | 🟢 | Emne: 10 vannskader/time (~87 600/år), 5,1 mrd. kr utbetalt i 2023. |
| `[EBA_NO2023]` | EBA Norge / Grønn Byggallianse (2023) | Byggebransje | Sekundær | 🟡 | Emne: Veileder for boligblokker (20 % CO₂-kutt uten merkostnad). Må skille fra EBA EU. |
| `[Wiik2025]` | SINTEF Notat nr. 57 (2025) | Konsortium | Internt | ⏸ | Emne: Materialkostnadsnøytralitet. Parkert (sirkelargumentasjon). |
| `[SA2018]` | Samfunnsøkonomisk analyse (4-2018) | Konsulenter | Primær | ⏸ | Emne: Konfliktkostnader 2,2 mrd. kr/år. Parkert (ubekreftet fil). |
| `[NFR_IPN2026]` | NFR IPN Utlysning 2026 (§10.1) | Offisiell | Offisiell | 🟢 | Emne: Ramme 1–16 MNOK, maks 50 % støtte. |

---

*Utkastet til Section 4 er utarbeidet for å inngå direkte i VERIFIED IPN State of the Art-rapporten (`docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`).*
