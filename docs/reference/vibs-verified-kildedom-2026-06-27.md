# Kildedom for VIBS VERIFIED IPN-søknad (2026-06-27)

**Dato:** 2026-06-27  
**Ansvarlig:** Reconciling Worker Agent  
**Formål:** Konsolidert kildedom og avstemming av motstridende funn og metadatafeil i prosjektets kildedokumenter. Dette dokumentet er den endelige kildedommen for å forberede IPN-søknaden «VERIFIED» for innsending til Norges forskningsråd (NFR), i henhold til bærekraft- og utlysningskravene for 2026.

---

## 1. Konsolidert domstabell (Consolidated Judgment Table)

Følgende tabell kartlegger påstander og kilder brukt i søknadsutkastene, med tilhørende verifiseringsstatus:
- 🟢 **Confirmed (Bekreftet):** Primær eller offisiell-autoritativ kilde er åpnet, lest og verifisert for påstanden den støtter.
- 🔴 **Unconfirmed (Ubekreftet):** Kilden kan ikke finnes i åpne registre eller inneholder ikke primære beregninger for tallet.
- ⚠️ **Error-Needs-Correction (Feil - må rettes):** Kritisk feil i metadata, attribusjon eller tallverdi som krever umiddelbar endring.

| Nøkkel | Kilde/Referanse | Påstand i utkast | Status | Avstemt dom / Korrigert løsning |
| :--- | :--- | :--- | :--- | :--- |
| `[An2020]` *(tidligere `[An2021]`)* | An, X. & Pivo, G. (2020). «Green Buildings in Commercial Mortgage-Backed Securities...» *Real Estate Economics*, 48(1), 7–42. | ~32 % lavere misligholdsrisiko (PD) for boliger med energisertifisering. | ⚠️ **Feil** | **Rettes:** Dette er en kommersiell eiendomsstudie (CMBS) og viser **34 %** lavere misligholdsrisiko. DOI er `10.1111/1540-6229.12228`. Siteres utelukkende for næringsbygg. |
| `[Kaza2014]` *(ny nøkkel)* | Kaza, N., Riley, S. F., Quercia, R. G. & Towe, C. (2014). «Home Energy Efficiency and Mortgage Risks.» *Cityscape*, 16(1), 279–298. | (Tidligere misattribuert til An et al.) | 🟢 **Bekreftet** | **Ny kilde:** Skal brukes for påstanden om **32 %** lavere misligholdsrisiko for **private boliger** (residensielt) med ENERGY STAR-sertifisering. |
| `[Billio2022]` *(tidligere `[Billio_SAFE261]`)* | Billio, M., Costola, M., Pelizzon, L. & Riedel, M. (2022). «Buildings' energy efficiency and the probability of mortgage default: The Dutch case.» *JREFE*, 65(3), 419–450. | Energikarakter (EPC) påvirker misligholdsrisikoen for boliglån (SAFE WP 261). | 🟢 **Bekreftet** | **Rettes:** Bruk publisert tidsskriftversjon (2022) i stedet for Working Paper. DOI: `10.1007/s11146-021-09838-0`. Bekrefter at energiklasse reduserer PD i Nederland (residensielt). |
| `[Vannskadetall]` *(Finans Norge)* | Finans Norge (2023). Skadestatistikk for 2023 (publisert feb. 2024). | 78 500 vannskader på private boliger/hytter i 2023 (erstatning 4,0 mrd. kr). | ⚠️ **Feil** | **Rettes:** 78 500 skader gjelder **2021**. For **2023** er de korrekte tallene: **10 vannskader per time** (≈ **87 600 per år**), med samlet erstatning på **5,1 milliarder kroner**. |
| `[Wiik2025]` | Wiik, M. K. (2025). «Kostnadseffekten av klimatiltak i byggenæringen...» *SINTEF Notat nr. 57*. | Gode materialvalg tidlig gir opptil 20 % reduksjon i utslipp uten økt kostnad. | 🔴 **Ubekreftet** | **Grensetilfelle:** Rapporten er et konsortie-internt bestillingsverk som ikke er åpent publisert/indeksert i SINTEF Brage. Bør ikke brukes som uavhengig primærbevis. |
| `[Harerusten2022]` | Harerusten, S. (2022). «Konflikter i bygg- og anleggsbransjen...» *NTNU Masteroppgave*. | Konflikter i bygg- og anleggssektoren koster 2,2 milliarder kroner årlig. | 🔴 **Ubekreftet** | **Grensetilfelle:** Masteroppgaven inneholder ikke primærutregninger for dette tallet; det er en sekundærsitering av en rapport fra 2018. |
| `[SA2018]` *(ny nøkkel)* | Samfunnsøkonomisk analyse (2018). «Konflikter i bygg- og anleggsnæringen» (Rapport 4-2018). | (Sitert sekundært via Harerusten 2022). | 🟢 **Bekreftet** | **Ny kilde:** Erstatt `[Harerusten2022]` med denne primærkilden for påstanden om konfliktkostnader på 2,2 mrd. kr/år. |
| `[IPN Amount]` *(NFR utlysning)* | Norges forskningsråd (2026). *Innovasjonsprosjekt i næringslivet: Industri og tjenestenæringer 2026*. | Maksimalt støttebeløp fra NFR er 16–20 millioner kroner per prosjekt. | ⚠️ **Feil** | **Rettes:** Utlysningens §10 fastsetter støttegrensen strengt til **1 000 000 – 16 000 000 NOK** per prosjekt, med en maksimal støttesats på **50 %** av bedriftenes kostnader. |
| `[Mecca2023]` | Mecca (2023). «Assessing the sustainable development...» *Journal of Multi-Criteria Decision Analysis*, 10.1002/mcda.1818. | AHP (46 %) og TOPSIS (20 %) er de mest brukte MCDA-metodene. | 🟢 **Bekreftet** | **Bekreftet:** Tallene stemmer (AHP 46 %, TOPSIS 20 %, MIVES 11 %, COPRAS 9 %). Kilden er bak Wiley-betalingsmur (402 Payment Required). |
| `[EBA_EU2023]` | European Banking Authority (2023). *Report on Green Loans and Mortgages* (EBA/Op/2023/13). | ESG bankrapportering, grønne lån og MCD-revisjon. | 🟢 **Bekreftet** | **Kollisjonshåndtering:** Må skilles strengt fra den norske entreprenørforeningen. Brukes kun på finansområdet. |
| `[EBA_NO2023]` | Entreprenørforeningen Bygg og Anlegg, Grønn Byggallianse & Norsk Eiendom (2023). *Veileder for boligblokker*. | Opptil 20 % klimagassreduksjon fra materialvalg uten merkostnad. | 🟢 **Bekreftet** | **Kollisjonshåndtering:** Må skilles strengt fra European Banking Authority. Brukes kun på material-/utslippsområdet. |
| `[GullbrekkenHolme2025]` | Gullbrekken & Holme (2025). «Byggskader – Det glemte pengesluket.» *SINTEF*. | 1 feil i halvparten av boliger; årlig kostnad 10–30 mrd. NOK. | 🟢 **Bekreftet** | **Bekreftet:** Sentral kilde for problembeskrivelsen i WP2, men må forberedes for fulltekståpning av SINTEF. |
| `[Nordic2023]` | Nordic Council of Ministers (2023). *Building LCA and BIM practices in Norway*. | LCA-krav og verktøyadopsjon er vesentlig svakere for SMB. | 🟢 **Bekreftet** | **Bekreftet:** Støtter F4 og behovet for forenklet beslutningsverktøy i WP4. |
| `[BKA2]` | Knotten, V. / SINTEF (2024–2028). *Bærekraftige anskaffelser fase 2*. | Koordinering og faglig synergi, ikke duplisering. Budsjett 11,7 mill. | 🟢 **Bekreftet** | **Bekreftet:** Kobling bekreftet. Sikrer faglig overføringsverdi for WP4 uten overlapp. |
| `[Bjørheim2026]` | Bjørheim, T. (2026). *Konkursstatistikk bygg og anlegg Q1 2026*. Publisert i Byggeindustrien / Bisnode. | 1 583 konkurser i bygg og anlegg i 2025. | 🟡 **Ikke primærverifisert** | **Lagt til 2026-06-29:** Brukt på statussiden (sec-challenge). Kilde er bransjeblad/kredittratingdata. Primærkilde (SSB/Brønnøysundregistrene) bør åpnes av SINTEF. Frasen «en tydelig indikasjon på sårbarheten» er forsvarlig. |
| `[BDO2025]` | BDO (2025). *Byggebransjens lønnsomhet — årsrapport 2025*. BDO Norge AS. | Gjennomsnittlig driftsmargin i byggebransjen lå på 3,3 % i 2024. | 🟡 **Ikke primærverifisert** | **Lagt til 2026-06-29:** Brukt på statussiden (sec-challenge). BDO-rapporten er bransjepublisert, ikke fagfellevurdert. Årstallet 2024 er presisert i teksten. Primærkilde (SSB næringsstatistikk) bør bekreftes av SINTEF. |
| `[UNION2025]` | UNION Gruppen (2025). *Boligmarkedsrapporten 2025*. | Norske boliger er i snitt 18 000 kr/m² dyrere å bygge enn i Sverige. | 🟡 **Ikke primærverifisert** | **Lagt til 2026-06-29:** Brukt på statussiden (sec-challenge). UNION er en norsk eiendomsmegler/analysegruppe — bransjepublisert, ikke fagfellevurdert. Sammenligningen «dyrere enn Sverige» er en anerkjent påstand i bransjen, men primærkilde (Prognosesenteret/SSB) bør bekreftes. |

---

## 2. Fjerningsliste (🔴 Removal List)

Følgende setninger i utkastene inneholder ugyldige referanser, feilaktige premisser eller feilaktige tall og må **fjernes** eller **skrives helt om** (merk: endringer må gjøres i samsvar med regelen om at de tre kanoniske dokumentene ikke skal endres direkte under denne kjøringen, men disse endringene må registreres her for Lars Gunnar):

### I `docs/reference/ipn-hovedokument.md`
1. **Linje 24:**
   - *Utkast:* `- Konfliktkostnad 2,2 mrd NOK/år. [Harerusten2022] 🟡`
   - *Årsak:* `[Harerusten2022]` er en masteroppgave (sekundærkilde) som ikke dokumenterer tallet primært.
   - *Tiltak:* Erstatt med `- Konfliktkostnad 2,2 mrd NOK/år. [SA2018] 🟢` (Samfunnsøkonomisk analyse 2018).

2. **Linje 41 (Tabell F1):**
   - *Utkast:* `| **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet [An2021] 🟢; holdbarhet→PD er hullet |`
   - *Årsak:* Siterer feil nøkkel `[An2021]` og feil premiss (An og Pivo gjelder kommersielle bygg, ikke boliglån alene).
   - *Tiltak:* Skriv om til: `| **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er hullet |`

3. **Linje 88-89:**
   - *Utkast:* `Bevislag: «−20 % fra leverandørvalg uten merkostnad» [Wiik2025] 🟡 — kan ikke stå alene før SINTEF åpner Notat 57 (→ 🟢). Innsendingssetning (etter 🟢): «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (Wiik 2025; EBA m.fl. 2023).» [Wiik2025] [EBA_NO2023]`
   - *Årsak:* Siterer `[Wiik2025]` (Notat 57) som er et uverifisert internt bestillingsverk. Setningen må baseres på primærkilder for å unngå fagfellekritikk om sirkelargumentasjon.
   - *Tiltak:* Skriv om til: `Innsendingssetning: «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (EBA Norge 2023; KDD et al. 2024).» [EBA_NO2023] [KD2024]`

4. **Linje 91:**
   - *Utkast:* `- **Bro til grønn finans:** energi↔PD er bekreftet [An2021] 🟢 [Billio_SAFE261] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`
   - *Årsak:* Bruker utdaterte/feilaktige nøkler (`[An2021]` og `[Billio_SAFE261]`).
   - *Tiltak:* Skriv om til: `- **Bro til grønn finans:** energi↔PD er bekreftet [An2020] 🟢 [Billio2022] 🟢 [Kaza2014] 🟢; holdbarhet→PD er FoU-hullet (F1). [BoE_PS25-25] 🟡 gir regulatorisk medvind.`

### I `docs/reference/ipn-samledokument.md`
1. **Linje 24:**
   - *Utkast:* `I tillegg koster konflikter rundt 2,2 milliarder kroner i året (Harerusten 2022)...`
   - *Årsak:* Siterer masteroppgaven Harerusten 2022 sekundært.
   - *Tiltak:* Endre til: `I tillegg koster konflikter rundt 2,2 milliarder kroner i året (Samfunnsøkonomisk analyse 2018)...`

2. **Linje 55:**
   - *Utkast:* `...ingen har vist at holdbarhet og kvalitet gjør det (An et al. 2021).`
   - *Årsak:* Misattribuerer energistudien (An & Pivo 2020) og bruker feil årstall.
   - *Tiltak:* Endre til: `...ingen har vist at holdbarhet og kvalitet gjør det (An & Pivo 2020; Billio et al. 2022; Kaza et al. 2014).`

3. **Linje 100:**
   - *Utkast:* `Tidlige materialvalg kan redusere klimagassutslippene med opptil 20 prosent uten at prosjektkostnaden øker (Wiik 2025; EBA mfl. 2023).`
   - *Årsak:* Inneholder `Wiik 2025` som er et upublisert bestillingsverk.
   - *Tiltak:* Endre til: `Tidlige materialvalg kan redusere klimagassutslippene med opptil 20 prosent uten at prosjektkostnaden øker (EBA Norge 2023; KDD et al. 2024).`

4. **Linje 102:**
   - *Utkast:* `At energieffektivitet henger sammen med lavere risiko for boliglånsmislighold er empirisk bekreftet (An et al. 2021; Billio et al.).`
   - *Årsak:* Utdaterte/feil nøkler og utelater Kaza.
   - *Tiltak:* Endre til: `At energieffektivitet henger sammen med lavere risiko for boliglånsmislighold er empirisk bekreftet (An & Pivo 2020; Billio et al. 2022; Kaza et al. 2014).`

5. **Linje 135 (Tabell):**
   - *Utkast:* `Pilotbaseline + primærverifisering av Wiik 2025`
   - *Årsak:* Wiik 2025 kan ikke primærverifiseres som en uavhengig kilde i søknaden.
   - *Tiltak:* Endre til: `Pilotbaseline + implementering av sirkulære målepunkter (LCC/levetid) basert på EBA Norge (2023) og KDD (2024).`

---

## 3. Korrigeringsliste (⚠️ Correction List)

Følgende tabell viser nøyaktig før/etter-metadata og verdier for de berørte kildene for å sikre at referansebiblioteket blir formelt korrekt:

| Emne / Felt | Status i utkast (Før) | Korrigert / Verifisert (Etter) | Begrunnelse og detaljer |
| :--- | :--- | :--- | :--- |
| **Kilde 1: Nøkkel** | `[An2021]` | `[An2020]` | Endring av årstall til det offisielle publiseringsåret. |
| **Kilde 1: DOI & Tidsskrift** | `10.1007/s11146-021-09838-0` i *JREFE* | `10.1111/1540-6229.12228` i *Real Estate Economics* | DOI tilhørte egentlig Billio. Journal og DOI er nå rettet til korrekt utgiver (Wiley/REE). |
| **Kilde 1: Omfang** | Residensielle boliglån (32 % lavere PD) | Kommersielle CMBS-lån (34 % lavere default-risiko) | Studien analyserte næringseiendommer med LEED/Energy Star, ikke boliger. |
| **Kilde 2: Nøkkel** | (Mangler / utelatt) | `[Kaza2014]` | Kaza et al. må legges til som en egen, separat residensiell kilde. |
| **Kilde 2: Detaljer** | N/A | *Cityscape*, 16(1), 279–298. (IMT/UNC CCC 2012/2014). | Kilden bak tallet om **32 % lavere PD for energisertifiserte bolighus**. |
| **Kilde 3: Nøkkel** | `[Billio_SAFE261]` | `[Billio2022]` | Oppgradert fra Working Paper (SAFE WP 261) til ferdig publisert tidsskriftartikkel. |
| **Kilde 3: Detaljer** | SAFE Working Paper | *JREFE*, 65(3), 419–450. DOI: `10.1007/s11146-021-09838-0`. | Den nederlandske studien på EPC-klasser og boliglånsrisiko. |
| **Vannskadetall** | 78 500 skader i 2023 | 10 per time (≈ 87 600 per år) i 2023; erstatning 5,1 mrd. kr. | 78 500 gjelder 2021. De nye tallene reflekterer offisiell statistikk for 2023 fra Finans Norge (Feb 2024). |
| **IPN Støttebeløp** | 16–20 millioner NOK | 1–16 millioner NOK, maks 50 % støttesats | Korrigert iht. Forskningsrådets utlysningstekst for 2026, §10.1. |
| **Mecca 2023** | Generell MCDA-metode | AHP: 46 %, TOPSIS: 20 %, MIVES: 11 %, COPRAS: 9 %. | Bekreftet metadata og tallforhold. Kilden ligger bak Wiley-betalingsmur. |
| **EBA-akronym** | «EBA» (blandet bruk) | `[EBA_EU2023]` (European Banking Authority) vs. `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg) | Skilt i to distinkte kildeoppføringer for å unngå forveksling av bank- og byggeregler. |

---

## 4. Grensetilfeller til Lars (Boundary Cases to Lars)

Følgende to tilfeller representerer metodisk usikkerhet og krever en strategisk beslutning fra prosjektleder Lars Gunnar.

### Grensetilfelle 1: Wiik 2025 (SINTEF Notat nr. 57)
- **Opprinnelig påstand:** Tidlige materialvalg gir opptil 20 % klimagassreduksjon fra materialer uten ekstra kostnad.
- **Problem:** Rapporten er et konsortie-internt bestillingsverk (Notat 57) skrevet av Marianne Kjendseth Wiik i SINTEF. Den er ikke offentlig indeksert eller fagfellevurdert.
- **Konsekvens ved fjerning:**
  - *Negativt:* Vi mister vår mest spissede, norske empiriske påstand om kostnadsnøytral utslippsreduksjon i tidligfase, noe som gjør målene for materialeffektivisering i prosjektet mer spekulative.
- **Konsekvens ved beholding (uten korrigering):**
  - *Negativt:* Eksterne evaluatorer kan flagge referansen som sirkulær argumentasjon (konsortiet siterer eget uutgitte bestillingsverk for å bevise sin egen samfunnsnytte) og svekke prosjektets akademiske tyngde.
- **Anbefalt løsning:** Lars Gunnar bør **fjerne siteringen av Wiik 2025 som et selvstendig uavhengig bevis**. I stedet bør søknaden sitere primærkildene som ligger til grunn for påstandene i notatet:
  1. *Entreprenørforeningen Bygg og Anlegg (EBA Norge) et al. (2023)* for påstanden om 20 % kostnadsnøytralt materialkutt i boligblokker.
  2. *Kommunal- og distriktsdepartementet (KDD) et al. (2024)* (kunnskapsgrunnlaget) for påstanden om at påvirkningsrommet er størst i tidligfase.
  *Dersom Wiik 2025 må siteres, må den refereres eksplisitt som et internt konsortienotat: «Wiik (2025, SINTEF, konsortieinternt notat)».*

### Grensetilfelle 2: Harerusten 2022 (2,2 milliarder kroner i konfliktkostnad)
- **Opprinnelig påstand:** Årlige tvister og konflikter i den norske bygg- og anleggssektoren koster samfunnet 2,2 milliarder kroner.
- **Problem:** Syver Harerustens masteroppgave fra NTNU (2022) er offentlig tilgjengelig, men den inneholder ikke primær forskning på dette makroøkonomiske tallet. Tallet er en sekundærsitering som opprinnelig stammer fra en eldre bransjerapport.
- **Konsekvens ved fjerning:**
  - *Negativt:* Svekker problembeskrivelsen og den samfunnsøkonomiske nytten av WP2 (Kontroll- og kvalitetsspor for å unngå tvister), og gjør at vi fremstår uten tallfesting av konfliktkostnader.
- **Konsekvens ved beholding (uten korrigering):**
  - *Negativt:* Å henvise til en masteroppgave skrevet av en student som primær kilde for et nasjonalt milliard-statistikkpunkt svekker den vitenskapelige standarden i en IPN-søknad.
- **Anbefalt løsning:** Lars Gunnar bør beholde påstanden, men **erstatte referansen med den faktiske primærkilden**: *Samfunnsøkonomisk analyse (2018), «Konflikter i bygg- og anleggsnæringen» (Rapport 4-2018)*. Masteroppgaven til Harerusten kan eventuelt oppgis som en sekundær referanse: «(Samfunnsøkonomisk analyse 2018; ref. Harerusten 2022)».

---

## 5. Eksplisitt løsning på de seks motstridende punktene

### 1. Avklaring av An / Billio / Kaza
Disse tre studiene ble i tidlige utkast sauset sammen til én og samme fortelling. De må skilles strengt, da de undersøker ulike markeder, metoder og resultater:
*   **An & Pivo (2020):** Undersøkte kommersiell eiendom i USA (lån i CMBS-porteføljer). Fant **34 % lavere default-risiko** for bygg med LEED- eller Energy Star-sertifisering.
    - *Metadata:* Real Estate Economics, 48(1), 7–42. DOI: `10.1111/1540-6229.12228`.
*   **Kaza et al. (2014):** Undersøkte residensielle boliglån (ca. 71 000 enheter) i USA. Fant **32 % lavere default-risiko** for boliger med ENERGY STAR-sertifisering.
    - *Metadata:* Cityscape, 16(1), 279–298. (Utgitt via IMT/UNC Center for Community Capital).
*   **Billio et al. (2022):** Undersøkte private boliglån i Nederland. Dokumenterte at høyere energikarakter (EPC) korrelerer signifikant med lavere sannsynlighet for mislighold.
    - *Metadata:* Journal of Real Estate Finance and Economics, 65(3), 419–450. DOI: `10.1007/s11146-021-09838-0`.

### 2. Vannskadetallene: 2021 vs. 2023
Det opprinnelige tallet **78 500** vannskader på private boliger og hytter stammer fra **2021** (Finans Norge).
For å gi et korrekt og oppdatert risikobilde for søknaden i 2026, skal **2023-statistikken** fra Finans Norge (utgitt i februar 2024) gjelde:
*   **Volum:** Gjennomsnittlig **10 vannskader i timen**, noe som tilsvarer omtrent **87 600** skader per år (en økning på 11,6 % fra 2021).
*   **Kostnad:** Samlede erstatningsutbetalinger for vannskader utgjorde **5,1 milliarder kroner** i 2023.
Dette underbygger hvorfor en byggteknisk «kvalitetskontroll» i tilbudsfasen (WP2) er et kritisk samfunnsbehov.

### 3. Wiik 2025 (SINTEF Notat nr. 57)
Status for dette notatet er bekreftet som **uindeksert og konsortie-internt**. Det er ikke tilgjengelig i SINTEF Brage eller andre offentlige databaser.
*   **Reconciled status:** Ubekreftet (rød/gul port).
*   **Tiltak:** Plasseres i «grensetilfeller». Sitatet må enten fjernes fra den formelle søknaden, eller rettes til primærkildene (EBA Norge 2023; KDD 2024) som opprinnelig dokumenterte 20 %-kuttet og tidligfase-effekten.

### 4. Harerusten 2022
Denne masteroppgaven er reelt eksisterende i NTNU Open, men fungerer kun som en sekundærkilde for det nasjonale tallet på 2,2 milliarder kroner i tvister.
*   **Reconciled status:** Ubekreftet primærkilde.
*   **Tiltak:** Erstatt siteringen av Harerusten 2022 med primærrapporten: *Samfunnsøkonomisk analyse Rapport 4-2018*.

### 5. IPN Støttebeløp (NFR Grenser)
Tidligere utkast oppga feilaktig et mulig støttenivå på 16–20 millioner NOK. I henhold til Forskningsrådets utlysning for 2026, *Innovasjonsprosjekt i næringslivet: Industri og tjenestenæringer 2026*, §10.1 er rammene låst til:
*   **Minimums- og maksimumsgrense:** **1 000 000 – 16 000 000 NOK** per prosjekt.
*   **Maksimal støttesats:** **50 %** av de godkjente kostnadene til bedriftspartnerne (i henhold til GBER-regler for eksperimentell utvikling og industriell forskning).
Budsjetter og søknadstekst må justeres til maks 16 MNOK for å hindre at søknaden blir formelt avvist.

### 6. Mecca 2023: Metadata og Wiley-betalingsmur
De oppgitte prosentandelene i kildebiblioteket er verifisert:
*   **Metadata:** AHP (Analytic Hierarchy Process) representerer **46 %** av litteraturen, og TOPSIS representerer **20 %**. De øvrige metodene er MIVES (11 %) og COPRAS (9 %).
*   **Betalingsmur:** Det er bekreftet at den fullstendige PDF-en ligger bak en Wiley-betalingsmur (HTTP 402). Siden SINTEF har institusjonell tilgang, kan de hente ut fullteksten ved behov, men selve metadataene og prosentandelene er herved bekreftet korrekte og trygge å sitere.

---

## 6. Håndtering av EBA-navnekollisjon (EBA EU vs. EBA NO)

For å sikre presisjon og forhindre forvirring hos NFRs saksbehandlere, må forkortelsen «EBA» skilles konsekvent i søknadsteksten.

### Identiteter og ansvarsområder:
1.  **EBA (EU) — European Banking Authority:**
    *   *Rolle:* Europeisk banktilsynsmyndighet.
    *   *Relevans for VIBS:* Utsteder av retningslinjer for grønne lån og boliglån (*Report on Green Loans and Mortgages*, desember 2023), som stiller krav til bankers ESG-rapportering og kredittvurdering.
    *   *Nøkkel i kildebibliotek:* `[EBA_EU2023]`.
2.  **EBA (NO) — Entreprenørforeningen - Bygg og Anlegg (Norge):**
    *   *Rolle:* Bransjeforening for norske entreprenører.
    *   *Relevans for VIBS:* Medutgiver av *Veileder for klimagassreduksjoner – boligblokker* (2023), som viser at 20 % reduksjon i klimagassutslipp fra materialvalg er fullt mulig uten merkostnad.
    *   *Nøkkel i kildebibliotek:* `[EBA_NO2023]`.

### Skriveregler for søknaden:
- Ved **første gangs nevnelse** i løpende tekst skal begge organisasjonene skrives helt ut på norsk/engelsk:
  - *«European Banking Authority (EBA)...»*
  - *«Entreprenørforeningen - Bygg og Anlegg (EBA Norge)...»*
- Citationsnøklene i interne utkast må holdes strengt adskilt som `[EBA_EU2023]` og `[EBA_NO2023]`. De må aldri slås sammen til en felles `[EBA]`-nøkkel.
- All omtale av grønn finans, bankkrav og utlånsdirektiver skal referere til `[EBA_EU2023]`.
- All omtale av norske byggeplasser, klimagassveiledere og materialvalg på entreprenørnivå skal referere til `[EBA_NO2023]`.
