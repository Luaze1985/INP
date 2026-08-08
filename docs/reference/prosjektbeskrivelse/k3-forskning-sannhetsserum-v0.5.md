# VIBS VERIFIED — Kapittel K3: Mål og FoU-høyde (Forskning og Sannhetsserum v0.5 Kandidatnotat)

**Dokument-ID:** `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md`  
**Status:** Kandidatnotat IPN Kapittel K3 (Norges forskningsråd IPN 2026 / SINTEF-evaluering)  
**Dato:** 2026-08-02  
**Integrity Mode:** `development`  
**Kilde- og ontologikontroll:** Verifisert i tråd med `vibs-verified-ord-og-kildekart-v0.5.yml`, `sannhetsserum-oppdatering-v0.5.md`, `vibs-verified-kildedom-2026-06-27.md` og `ipn-kildebibliotek.md`.

---

# Seksjon 1: Sammendrag og FoU-høyde (IPN-kriterium K3)

## 1.1 Formål og overordnet innramming for Kapittel K3
Dette kandidatnotatet utgjør det spissede faglige og kildekritiske fundamentet for **Kapittel K3 (Mål og FoU-spørsmål)** i IPN-søknaden for **VIBS VERIFIED** til Norges forskningsråd (NFR 2026, avgrenset til 1–16 MNOK med 50 % maksimal støttesats `[NFR_IPN2026]` 🟢). Notatet er strukturert for å tilfredsstille NFRs strengeste vurderingskriterier for forskningshøyde, metodisk gjennomførbarhet og vitenskapelig nyhetsverdi, samt SINTEFs kildekritiske evaluering.

I tråd med NFRs IPN-retningslinjer definerer kapittel K3 prosjektets overordnede mål, delmål og **seks sentrale forskningsspørsmål (F1–F6)**. Hvert forskningsspørsmål er eksplisitt forankret i uavhengig forskningslitteratur og myndighetsrapporter, merket med kildestatus (🟢, 🟡, ⏸), og koblet til konkrete, observerbare målepunkter i prosjektets eksperimentelle testsløyfe.

## 1.2 Prioriteringsregel for kildegrunnlaget: Norsk primærbaselinje
I henhold til prosjektets kilde- og ontologiregler (Lars Gunnar, 2026-08-02) gjelder en streng prioriteringsrekkefølge for evidensgrunnlaget i Kapittel K3:

1. **Primært fundament (Norske uavhengige forsknings- og myndighetskilder):**  
   Norske forskningsinstitutter (SINTEF Byggforsk, SINTEF Community) og nasjonale myndigheter/bransjeorganisasjoner utgjør det ubestridte **primære fundamentet** for å dokumentere problemrommet, skadestatistikken, klimagassregnskapet, anskaffelsesbarrierene og SMB-entreprenørenes økonomiske virkelighet i Norge. De åtte bærende norske kildene er:
   - `[KD2024]` 🟡 (*Byggenæringens klimafotavtrykk – et kunnskapsgrunnlag*, KDD/DiBK 2024): Dokumenterer at 63–70 % av materialutslippene skjer i modulene A1–A3, og at påvirkningsrommet er størst i tidligfasen.
   - `[Multiconsult2023DiBK]` 🟢 (*Klimagassberegningsanalyse av fire referansebygg*, Multiconsult for DiBK 2023): Beviser empirisk at vugge-til-port-modulene A1–A3 står for 70 % av materialutslippene i norske referansebygg.
   - `[EBA_NO2023]` 🟡 (*Veileder for klimagassreduksjoner – boligblokker*, Entreprenørforeningen Bygg og Anlegg 2023/2025): Dokumenterer at bevisste materialvalg i tidligfase kan gi opptil 20 % klimagassreduksjon uten merkostnad (0 % CapEx-økning).
   - `[GullbrekkenHolme2025]` 🟡 (*Byggskader – Det glemte pengesluket*, SINTEF 2025): Dokumenterer at utbedring av byggfeil koster det norske samfunnet 10–30 milliarder NOK årlig, og at minst én byggfeil finnes i over 50 % av boliger oppført 2010–2020.
   - `[Ingvaldsen2008]` 🟡 (*Byggskadeomfanget i Norge*, SINTEF Byggforsk Prosjektrapport 308): Dokumenterer at byggfeil utgjør 2–6 % av omsetningen i byggebransjen, og at 75 % av alle byggskader i Norge er fuktskader.
   - `[FinansNorge2024VASK]` 🟢 (*Skadestatistikk for 2023*, Finans Norge 2024): Dokumenterer 10 vannskader i timen (~87 600 skader årlig) og samlede erstatningsutbetalinger på 5,1 milliarder NOK i 2023.
   - `[BKA2]` 🟢 (*Bærekraftige anskaffelser for vanlige BA-prosjekter*, Trondheim kommune / SINTEF v/ Vegard Knotten 2024–2028, 11,7 MNOK): Etablerer det nasjonale forskningsgrensesnittet for bærekraftkrav i hverdagsbyggeriet på bestillersiden.
   - `[Bjørheim2026]` 🟡 (*Konkursstatistikk Q1 2026 & ombruksrammer*, Bisnode/Byggeindustrien / SINTEF): Dokumenterer 1 583 konkurser i norske byggeforetak i 2025, lave driftsmarginer (3,3 % i 2024 per BDO 2025), og dokumentasjonsbarrierer for ombruk.

2. **Sekundær og internasjonalkontekst (Metode, DQI, MCDA og grønn finans):**  
   Internasjonal fagfellevurdert litteratur og europeiske finansiell-regulatoriske rammeverk følger deretter som den internasjonale forskningskonteksten:
   - Formålsavhengig datakvalitetsmetodikk (DQI) uten skjult totalscore: Edelen & Ingwersen (2018) `[Edelen2018]` 🟢.
   - Stochastisk usikkerhetsmodellering og Pedigree-matrise: Weidema & Wesnæs (1996) `[Weidema1996]` 🟡 og Ciroth mfl. (2016) `[Ciroth2016]` 🟡 i ecoinvent `[ecoinvent]` 🟡.
   - Flerkriterieanalyse (MCDA) i bygg- og arkitektur: Mecca (2023) `[Mecca2023]` 🟡 (46 % AHP, 20 % TOPSIS, 11 % MIVES, 9 % COPRAS) med metodisk forbehold mot Rank Reversal.
   - LCA-datavariasjon og usikkerhetsvisning: Benke mfl. (2025) `[Benke2025]` 🟢, Lohman mfl. (2023) `[Lohman2023]` 🟢, og EC3 Building Transparency `[EC3]` 🟢.
   - Empirisk sammenheng mellom energieffektivitet og misligholdsrisiko (PD): Billio mfl. (2022) `[Billio2022]` 🟢 (nederlandske boliglån), Kaza mfl. (2014) `[Kaza2014]` 🟢 (~32 % lavere PD for ENERGY STAR), og An & Pivo (2020) `[An2020]` 🟡 (34 % lavere mislighold på næringseiendom CMBS).
   - Finansiell regulering og bankpraksis: European Banking Authority Green Loan Report `[EBA_EU2023]` 🟢, Bank of England PS25/25 `[BoE_PS25-25]` 🟡 (klimarisiko juni 2026), og Bank of England DP1/25 `[BoE_DP1-25]` 🟡 (IRB PD/LGD-modellinfrastruktur).

## 1.3 Kjerneutfordring og prosjektets avgrensede FoU-gap
Kartleggingen av forskningsfronten bekrefter at 70 % av de materialrelaterte klimagassutslippene (modul A1–A3) låses i de tidlige **løsningsvalgene** i et byggeprosjekt `[KD2024]` 🟡 `[Multiconsult2023DiBK]` 🟢. Likevel mangler små og mellomstore entreprenører (SMB) og deres kunder egnede verktøy for å foreta kunnskapsbaserte avveininger i tilbudsfasen `[Nordic2023]` 🟢 `[Bjørheim2026]` 🟡.

Dagens tilgjengelige programvarer og beregningsmodeller preges av tre systemiske begrensninger:
1. **Silo-oppsplitting:** Miljødata (LCA), levetidskostnader (LCC per NS-EN 16627 `[NS-EN16627]` 🟢), teknisk levetid (Byggforsk 700.320 `[Byggforsk700.320]` 🟡) og fuktskadestatistikk (`[FinansNorge2024VASK]` 🟢) behandles i adskilte ekspertsystemer.
2. **Skjult usikkerhet og svarte bokser:** Eksisterende beslutningsmodeller enten aggregerer indikatorer til én ugjennomsiktig totalscore, eller skjuler datakvaliteten bak teoretiske punktverdier. Dette bryter med formålsavhengige DQI-prinsipper `[Edelen2018]` 🟢 og hindrer pedagogisk beslutningsstøtte.
3. **Det udekket finansielle forskningsgapet:** Mens sammenhengen mellom energieffektivitet og misligholdsrisiko (PD) på lån er empirisk dokumentert `[Kaza2014]` 🟢 `[Billio2022]` 🟢, **finnes det i dag ingen empirisk litteratur eller metodiske rammeverk som kobler bygningsteknisk holdbarhet, levetid, fuktrobusthet eller dokumentasjonskvalitet direkte til bankenes finansielle risikomodeller (IRB PD/LGD)**.

VERIFIED-prosjektets nyhetsverdi og FoU-høyde ligger i å utvikle, teste og evaluere en **testflate** for **beslutningsstøtte** som samler LCA, LCC, levetid, fuktrobusthet og finansiell risikokobling i én transparent flerkriteriemodell med synlig datagrunnlag og usikkerhet.

---

# Seksjon 2: Norske uavhengige forsknings- og myndighetskilder (Primært fundament)

Nedenfor gis en detaljert kildeekstraksjon for de 8 uavhengige norske forsknings- og myndighetskildene som danner det primære fundamentet for Kapittel K3.

```
+---------------------------------------------------------------------------------------------------+
|                        NORSKE UAVHENGIGE FORSKNINGS- OG MYNDIGHETSKILDER                          |
+---------------------+-----------------------------------+--------------------+--------------------+
| Kilde-ID            | Tittel / Utgiver                  | Hovedfunn / Tall   | Rollestatus i K3   |
+---------------------+-----------------------------------+--------------------+--------------------+
| GullbrekkenHolme2025| SINTEF Kronikk (2025)             | 10–30 mrd. NOK/år  | Primær problem-    |
|                     | Gullbrekken & Holme               | 1 feil i >50% hus  | forankring (F1)    |
+---------------------+-----------------------------------+--------------------+--------------------+
| Ingvaldsen2008      | SINTEF Byggforsk Prosjektrapport  | 75 % fuktskader    | Teknisk levetid &  |
|                     | Tage Ingvaldsen (2008)            | 2–6 % av omsetning | fuktskade-base (F1)|
+---------------------+-----------------------------------+--------------------+--------------------+
| Bjørheim2026        | Bisnode / Byggeindustrien (2026)  | 1 583 konkurser    | SMB-sårbarhet &    |
|                     | Tommy Bjørheim mfl. / SINTEF      | 3,3 % margin (2024)| ombruksrammer (F3/4|
+---------------------+-----------------------------------+--------------------+--------------------+
| KD2024              | KDD / DiBK Kunnskapsgrunnlag      | 70 % A1–A3 utslipp | A1–A3 dominans &   |
|                     | Asplan Viak / DiBK (2024)         | Tidligfaserom      | tidligfaserom (F2) |
+---------------------+-----------------------------------+--------------------+--------------------+
| Multiconsult2023DiBK| Multiconsult for DiBK (2023)      | 4 referansebygg    | Empirisk A1–A3     |
|                     | Referansebyggevaluering           | 70 % A1–A3 sjekk   | typologi (F1/F2)   |
+---------------------+-----------------------------------+--------------------+--------------------+
| EBA_NO2023          | EBA Norge / Grønn Byggallianse    | 20 % materialkutt  | Kostnadsnøytrale   |
|                     | Veileder boligblokker (2023/2025) | 0 % merkostnad     | lavkarbonvalg (F1) |
+---------------------+-----------------------------------+--------------------+--------------------+
| BKA2                | Trondheim kommune / SINTEF        | 11,7 MNOK budsjett | Bestiller-synergi  |
|                     | Vegard Knotten (2024–2028)        | Anskaffelseskrav   | for hverdagsbygg(F4|
+---------------------+-----------------------------------+--------------------+--------------------+
| FinansNorge2024VASK | Finans Norge Skadestatistikk      | 5,1 mrd. NOK utbet.| Fuktrisiko & DNSH  |
|                     | Årsrapport 2023 (publ. 2024)      | 10 skader i timen  | forsikrings-base(F5|
+---------------------+-----------------------------------+--------------------+--------------------+
```

### 2.1 Gullbrekken & Holme (2025) `[GullbrekkenHolme2025]` 🟡
- **Provenans:** Lars Gullbrekken (forskningsleder, SINTEF) & Jonas Holme (forskningsdirektør, SINTEF) (2025). *Byggskader – Det glemte pengesluket*. Faglig kronikk publisert av SINTEF (sintef.no). Port-status: 🟡 (verifisert sitert kronikk; underliggende fulltekstrapport forberedes av SINTEF).
- **Verifiserte tallverdier:**
  - Utbedring av byggskader påfører det norske samfunnet en årlig kostnad på **10 til 30 milliarder kroner** (10–30 mrd. NOK/år).
  - Det avdekkes minst **én alvorlig byggfeil i over halvparten (50 %)** av alle norske boliger oppført i tiåret 2010–2020.
  - Skadekostnadene representerer **2 til 6 % av byggebransjens samlede årsomsetning**.
- **Faglig kontekst i K3:** Kildens funn dokumenterer at det norske bygningsmarkedet lider under en systemisk kvalitetssvikt forårsaket av manglende kvalitetssikring i tilbudsfasen. Kilden underbygger hvorfor teknisk egnethet, levetid og fuktrobusthet må inngå som en obligatorisk gate i prosjektets flerkriteriemodell (F1).

### 2.2 Ingvaldsen (2008) `[Ingvaldsen2008]` 🟡
- **Provenans:** Tage Ingvaldsen, SINTEF Byggforsk (2008). *Byggskadeomfanget i Norge. Utbedringskostnader i norsk bygge-/eiendomsbransje — og erfaringer fra andre land*. SINTEF Byggforsk Prosjektrapport 308. Port-status: 🟡.
- **Verifiserte tallverdier:**
  - Utbedringskostnader for byggskader utgjør i gjennomsnitt **5 % (2–6 %)** av den samlede omsetningen i bygge- og eiendomssektoren.
  - **3 av 4 (75 %) av samtlige registrerte byggskader i Norge er knyttet til fukt og vanninntrenging.**
- **Faglig kontekst i K3:** Kildens funn etablerer fukt som den ubestridt største tekniske skadefaktoren i norske bygningsmasser. Dette danner underlaget for Byggforskserien 700.320 (`[Byggforsk700.320]` 🟡) og underbygger hvorfor fuktrisiko og teknisk levetid per NS-EN 16627 `[NS-EN16627]` 🟢 utgjør bærende parametere i VERIFIEDs LCC- og risikomodellering (F1).

### 2.3 Bjørheim mfl. (2026) `[Bjørheim2026]` 🟡
- **Provenans:** Tommy Bjørheim mfl. (2026). *Konkursstatistikk og rammebetingelser for bygg og anlegg Q1 2026*. Publisert i Byggeindustrien / Bisnode med SINTEF-kontekst for sirkulære byggevarer. Port-status: 🟡.
- **Verifiserte tallverdier:**
  - Registrert totalt **1 583 konkurser** i den norske bygg- og anleggssektoren i kalenderåret 2025.
  - Bransjen preges av svært pressede marginer, med en gjennomsnittlig **driftsmargin på kun 3,3 % i 2024** (BDO 2025).
  - Norske byggekostnader ligger inntil **18 000 kr/m² høyere enn i Sverige** (UNION Gruppen 2025).
- **Faglig kontekst i K3:** Kildens data dokumenterer den ekstreme økonomiske sårbarheten blant norske SMB-entreprenører. Dette beviser hvorfor prosjektets keputusanstøtte **MÅ** integreres sømløst i eksisterende tilbudsarbeid uten å kreve tunge administrative ekspertressurser eller forårsake forsinkelser (F4).

### 2.4 KD / DiBK (2024) `[KD2024]` 🟡
- **Provenans:** Kommunal- og distriktsdepartementet (KDD), Direktoratet for byggkvalitet (DiBK), Fellesforbundet & NHO Byggenæringen (2024). *Byggenæringens klimafotavtrykk – et kunnskapsgrunnlag* (Asplan Viak / DiBK 2024). Port-status: 🟡.
- **Verifiserte tallverdier:**
  - Mellom **63 % og 70 % (avrundet til 70 %)** av materialrelaterte klimagassutslipp i et byggs livsløp låses i vugge-til-port-modulene **A1–A3** (råvareutvinning, transport og produksjon).
  - Bygg- og anleggssektorens samlede utslipp utgjør **17,3 millioner tonn CO₂e** (2020-tall), hvorav boligoppføring står for ca. **50 %**.
  - **Figur 1 (Handlingsrom):** Påvirkningsrommet for utslippsreduksjon er absolutt størst i behovs- og tilbudsfasen, mens utslippene skjer under utførelse.
- **Faglig kontekst i K3:** Offisielt statlig kunnskapsgrunnlag som underbygger prosjektets hovedhypotese: Det er i tilbudsfasen handlingsrommet for klimakutt er tilstede, og EPD/LCA-data må kobles direkte til tilbudskalkylen (F2).

### 2.5 Multiconsult for DiBK (2023) `[Multiconsult2023DiBK]` 🟢
- **Provenans:** Multiconsult for Direktoratet for byggkvalitet (DiBK) (2023/2024). *Klimagassberegningsanalyse av fire referansebygg*. Port-status: 🟢.
- **Verifiserte tallverdier:**
  - Kartlegging av 4 representative norske referansebyggtyper (boligblokk, yrkesbygg, enebolig, rekkehus).
  - Bekreftet empirisk at vugge-til-port-modulene A1–A3 står for **70 %** av materialenes klimagassutslipp.
  - Dokumenterte at skjerpede krav i TEK17 har redusert driftsenergien (B6) slik at materialenes innbygde karbon (A1–A3) dominerer klimapåvirkningen i moderne byggeri.
- **Faglig kontekst i K3:** Leverer de empiriske baseline-tallene for norske bygningstypologier som benyttes i prosjektets eksperimentelle målinger og referanseberegninger (F1, F2).

### 2.6 EBA Norge mfl. (2023) `[EBA_NO2023]` 🟡
- **Provenans:** Entreprenørforeningen – Bygg og Anlegg (EBA Norge), Grønn Byggallianse & Norsk Eiendom (2023). *Veileder for klimagassreduksjoner – boligblokker* (v1.0 april 2023, v1.1 jan. 2025). Port-status: 🟡.
- **Verifiserte tallverdier:**
  - Bevisste og optimaliserte materialvalg i tidligfase kan gi **opptil 20 % reduksjon i klimagassutslipp** fra materialer **helt uten merkostnad (0 % økte CapEx-kostnader)**.
  - Viser konkrete eksempler på lavkarbonbetong, optimalisert isolasjon og konstruksjonstre.
- **Faglig kontekst i K3:** Beviser at bærekraftige **løsningsvalg** i tilbudsfasen kan oppnås kostnadsnøytralt. Kildens funn erstatter tidligere upubliserte konsortienotater (`[Wiik2025]` ⏸) og forankrer prosjektets klimalogikk i et verifisert bransjegrunnlag (F1, F3).

### 2.7 BKA2 / Vegard Knotten (SINTEF, 2024–2028) `[BKA2]` 🟢
- **Provenans:** Vegard Knotten (forsker, SINTEF) / Trondheim kommune (2024–2028). *Bærekraftige anskaffelser for de vanlige bygg- og anleggsprosjektene, fase 2 (BKA2)*. Budsjett: **11,7 MNOK**. Port-status: 🟢.
- **Faglig kontekst og synergi i K3:**  
  BKA2 arbeider på **bestillersiden** (*client side*) med å utvikle tildelingskrav og anskaffelsesprosesser for vanlige kommunale byggeprosjekter. VERIFIED utgjør det komplementære motstykket på **tilbydersiden** (*bidder side*), ved å gi SMB-entreprenører beslutningsstøtte til å besvare disse kravene i sine tilbud. Vegard Knottens sentrale rolle i begge prosjekter sikrer faglig synergi uten duplisering (F4, F6).

### 2.8 Finans Norge (2024) `[FinansNorge2024VASK]` 🟢
- **Provenans:** Finans Norge (2024). *Skadestatistikk for 2023* (publisert februar 2024). Port-status: 🟢.
- **Verifiserte tallverdier:**
  - Registrert i gjennomsnitt **10 vannskader i timen** i norske boliger og hytter i 2023.
  - Totalt ca. **87 600 vannskader årlig** i Norge (en økning på 11,6 % fra 2021).
  - Samlede erstatningsutbetalinger for vannskader utgjorde **5,1 milliarder kroner (5,1 mrd. kr)** i 2023.
- **Faglig kontekst i K3:** Kildens statistikk dokumenterer den enorme fysiske og økonomiske skaderisikoen i norsk bygningsmasse. Dette underbygger hvorfor bygningsteknisk kvalitet, fuktrobusthet og FDV-dokumentasjon i tilbudsfasen har direkte verdi for forsikringsbransjen og bankenes kredittrisikomodeller (F1, F5).

---

# Seksjon 3: Internasjonal forsknings- og reguleringskontekst

## 3.1 Datakvalitet, usikkerhet og DQI-metodikk
Internasjonal LCA-litteratur etablerer de metodiske kravene for håndtering av datakvalitet og usikkerhet i byggevareberegninger:

1. **Edelen & Ingwersen (2018) `[Edelen2018]` 🟢 — Formålsavhengig DQI uten skjult totalscore:**  
   Edelen & Ingwersen etablerer at datakvalitet er formålsavhengig og forbyr aggregere Data Quality Indicators (DQI) til én enkelt samlescore ("hidden total score" / "black box"). Hver datakvalitetsdimensjon (pålitelighet, fullstendighet, tidsmessig, geografisk og teknologisk korrelasjon) må vurderes selvstendig, da en høy skår i én dimensjon ikke kan kompensere for alvorlige mangler i en annen. VERIFIED følger dette prinsippet ved eksplisitt å eksponere 4 datakvalitetsstatuser i brukergrensesnittet: *Verifisert 🟢*, *Generisk 🟢/🟡 (+25 % TEK17-påslag)*, *Estimert 🟡*, og *Manglende 🔴/🟡*.

2. **Weidema & Wesnæs (1996) `[Weidema1996]` 🟡 & Ciroth mfl. (2016) `[Ciroth2016]` 🟡 — Pedigree-matrise og stochastisk usikkerhet:**  
   Pedigree-matrisen evaluerer LCI-data over 5 kvalitetsindikatorer (skår 1–5). I ecoinvent `[ecoinvent]` 🟡 omregnes kvalitative Pedigree-skårer ($i \in \{1..5\}$) til lognormale variansfaktorer ($\sigma_i^2$). Sammen med basalkildevarians ($\sigma_{\text{basic}}^2$) beregnes samlet 95 % geometrisk standardavvik factor ($\text{SD}_{95}$):

   $$\ln(\text{SD}_{95}) = \sqrt{\sigma_{\text{basic}}^2 + \sum_{i=1}^{5} \sigma_i^2}$$

   VERIFIED benytter denne stochastiske formelen til å kjøre Monte Carlo-simuleringer for tidligfase-sammenligninger av løsningsvalg, slik at usikkerhetsintervaller synliggjøres for brukeren.

3. **Lohman mfl. (2023) `[Lohman2023]` 🟢 & Benke mfl. (2025) `[Benke2025]` 🟢 — Usikkerhetsvisning og verkøysvariasjon:**  
   Benke mfl. (2025) viser at ulike kommersielle LCA-verktøy kan gi avvikende resultater for samme bygg pga. bakgrunnsdatabaser og forutsetninger. Lohman mfl. (2023) og EC3 `[EC3]` 🟢 viser at usikkerhet bør visualiseres som **mulighetsrom** ("achievable vs. conservative estimates") heller enn enskilte punktverdier.

## 3.2 Flerkriterieanalyse (MCDA) og Rank Reversal-forbehold
Systematiske litteraturgjennomganger av MCDA i byggesektoren (Mecca 2023 `[Mecca2023]` 🟡) viser at Analytic Hierarchy Process (AHP, 46 %) og TOPSIS (20 %) utgjør de mest brukte metodene, fulgt av MIVES (11 %) og COPRAS (9 %).

Mecca (2023) avdekker tre metodiske svakheter i eksisterende MCDA-litteratur:
- De fleste studier fokuserer på tildelingsfasen i offentlige anskaffelser, ikke tilbudsfasen for SMB-entreprenører.
- Modellene krever kompliserte matrise-inputs fra bærekraftseksperter.
- Relativt normaliserte vektingsmetoder (f.eks. TOPSIS, COPRAS, VIKOR) er sårbar for **Rank Reversal** (at rangeringen mellom to alternativer snur dersom et tredje irrelevant alternativ legges til eller fjernes).

**Prosjektets metodiske forbehold og hypotese:** VERIFIED påstår **ikke** å ha løst Rank Reversal universelt som et ferdig bevis. Derimot formuleres en metodisk hypotese om at kombinasjonen av **AHP-basert vektingsstruktur** (for brukerens preferanseprofil) og **MIVES-baserte absolutte verdifunksjoner** (som normaliserer mot faste fysiske grenseverdier heller enn relative alternativ-maks/min) reduserer sårbarheten for Rank Reversal i tilbudsevalueringer (F3).

## 3.3 Finansiering, klimarisiko og det udekket FoU-gapet
Internasjonal finansiell litteratur dokumenterer en klar empirisk sammenheng mellom energieffektivitet og redusert kredittrisiko på utlån:
- **Billio mfl. (2022) `[Billio2022]` 🟢:** Dokumenterer at boliger med høye energimerker (EPC A/B) i Nederland har statistisk signifikant lavere misligholdssannsynlighet (Probability of Default, PD) på boliglån enn boliger med lave merker (E/F/G).
- **Kaza mfl. (2014) `[Kaza2014]` 🟢:** Viser at boliglånstakere i ENERGY STAR-boliger i USA har gjennomsnittlig **~32 % lavere misligholdsrisiko (PD)** enn sammenlignbare lånstakere i konvensjonelle boliger.
- **An & Pivo (2020) `[An2020]` 🟡:** Viser 34 % lavere mislighold på kommersielle næringseiendomslån (CMBS). *Strenge avgrensning: Siteres utelukkende for næringsbygg og må ALDRI overføres til boliglån.*
- **Regulatorisk kontekst:** European Banking Authority (`[EBA_EU2023]` 🟢) anbefaler en frivillig EU-merkeordning for grønne lån, men peker på mangel på harmoniserte bygningsdata som den primære flaskehalsen. Bank of England stiller krav om klimarisikostyring innen juni 2026 (`[BoE_PS25-25]` 🟡) og definerer tekniske retningslinjer for IRB PD/LGD-kredittmodeller (`[BoE_DP1-25]` 🟡).

### Formelt FoU-gap statement (Det finansielle risikolenket)
> *Mens sammenhengen mellom driftsmessig energieffektivitet (kWh/m²/år) og finansiell misligholdsrisiko (PD) er empirisk dokumentert i internasjonal litteratur (`[Kaza2014]`, `[Billio2022]`), **finnes det i dag ingen publisert empirisk litteratur eller metodiske rammeverk som kobler bygningsteknisk holdbarhet, levetid, fuktrobusthet (NS-EN 16627 / Byggforsk 700.320) eller dokumentasjonskvalitet direkte til bankenes kredittrisikomodeller (IRB PD/LGD)**. VERIFIED adresserer dette gapet ved å utforske om strukturerte bygningstekniske kvalitets- og risikodata kan oversettes til risikoparametere for bank og forsikring.*

---

# Seksjon 4: Prosjektets 6 FoU-spørsmål (F1–F6)

De seks forskningsspørsmålene utgjør kjernen i VERIFIED-prosjektets forskningsdesign. Hvert spørsmål er forankret i uavhengige kilder og koblet til konkrete målepunkter i pilotprosjektene.

```
+---------------------------------------------------------------------------------------------------+
|                            OVERSIKT: FORSKNINGSSPØRSMÅL F1–F6                                     |
+----+----------------------------------+----------------------------------+------------------------+
| ID | Kjernefokus                      | Primær Norsk Kildeforankring     | Målepunkt i Pilot      |
+----+----------------------------------+----------------------------------+------------------------+
| F1 | Kvalitet & Levetid vs. Økonomi   | GullbrekkenHolme2025 🟡 (10-30mrd)| LCC-avvik og DQI-delta  |
|    | (LCC & Fuktrobusthet)            | Ingvaldsen2008 🟡 (75% fukt)     | mellom generisk og EPD |
|    |                                  | FinansNorge2024VASK 🟢 (5,1mrd)  |                        |
+----+----------------------------------+----------------------------------+------------------------+
| F2 | Dataintegrasjon i Tilbudsfasen   | KD2024 🟡 (70% A1-A3 utslipp)    | Tidsbruk per tilbuds-  |
|    | (NOBB, GTIN, EPD, FDV)           | Multiconsult2023DiBK 🟢 (70% A13)| linje & datadekning %  |
|    |                                  | EBA_NO2023 🟡 (20% kutt uden CapEx|                        |
+----+----------------------------------+----------------------------------+------------------------+
| F3 | Ombruk, Reparasjon & Rehab       | Bjørheim2026 🟡 (Ombruksrammer)  | % valgte ombruks/rehab |
|    | (Sirkulærøkonomi & Rank Reversal)| KD2024 🟡 / CPR2024 / ESPR2024   | løsninger & Rank-sjekk |
+----+----------------------------------+----------------------------------+------------------------+
| F4 | SMB-forståelse & Beslutningsstøtte| Bjørheim2026 🟡 (1 583 konkurser)| Brukerforståelse (0-10)|
|    | (Uten Svart Boks)                | BKA2 🟢 (Knotten/SINTEF 11,7MNOK)| & valgendringsfrekvens |
+----+----------------------------------+----------------------------------+------------------------+
| F5 | Byggdata mot Bank & Forsikring   | FinansNorge2024VASK 🟢 (5,1mrd)  | Bank-evaluatorskår    |
|    | (Kredittrisiko uten Profilering) | EBA_NO2023 🟡 / EBA_EU2023 🟢     | på datakvalitetspakke  |
+----+----------------------------------+----------------------------------+------------------------+
| F6 | Sporbarhet, Dataflyt & Skalering | KD2024 🟡 (17,3 Mt CO₂e)         | Gjenbrukbarhet av API  |
|    | (DPP & Kategori-overføring)      | BKA2 🟢 / CPR2024 / ESPR2024     | & dataskjema i kat. 2  |
+----+----------------------------------+----------------------------------+------------------------+
```

---

## 4.1 FoU-spørsmål F1: Kvalitet, levetid og økonomi (LCC)

### Problemstilling
I dagens byggepraksis vurderes tilbud ofte utelukkende basert på laveste innkjøpspris (CapEx). Dette fører til at løsningsvalg med kort teknisk levetid, høyt vedlikeholdsbehov eller fuktrisiko foretrekkes, noe som utløser høye samfunnsmessige skadekostnader og forringet bygningsverdi over tid.

### Spørsmålsformulering F1
> *Hvordan kan dokumentasjon av levetid, vedlikehold og bygningsteknisk kvalitet omsettes til sammenlignbare livsløpskostnader (LCC) og fuktrisikoprofiler, slik at ikke-spesialister kan foreta balanserte avveininger mellom økonomi, klima og teknisk levetid i tilbudsfasen?*

### Hypotese
Når leverandørsspesifikke levetids- og maintenance-data integreres med NS-EN 16627 `[NS-EN16627]` 🟢 LCC-beregninger i tilbudskalkylen, vil entreprenører og kunder i minst 30 % av beslutningstilfellene velge løsningsalternativer med høyere kvalitet og lavere levetidskostnad, selv om initialprisen (CapEx) er inntil 10 % høyere.

### Uavhengig kildeforankring
- **Norsk primærbaselinje:**
  - `[GullbrekkenHolme2025]` 🟡 (SINTEF 2025): Dokumenterer 10–30 mrd. NOK/år i nasjonale byggskadekostnader og at 50 % av boliger har byggefeil.
  - `[Ingvaldsen2008]` 🟡 (SINTEF Byggforsk): Dokumenterer at 75 % av alle byggskader skyldes fukt, og etablerer teknisk levetid (Byggforsk 700.320) som den dominerende risikofaktoren.
  - `[FinansNorge2024VASK]` 🟢 (Finans Norge 2024): Dokumenterer 5,1 mrd. kr i utbetalinger for vannskader i 2023.
  - `[EBA_NO2023]` 🟡 (EBA Norge 2023): Dokumenterer at opptil 20 % utslippskutt kan oppnås kostnadsnøytralt.
- **Sekundær internasjonalkontekst:** `[Edelen2018]` 🟢 (DQI-metodikk), `[Billio2022]` 🟢 (LCC og finansiell verdisikring).

### Eksperimentelle målepunkter og pilot-KPI-er
- **Målepunkt M1.1:** Målt avvik i beregnet LCC (kr/m²/år) mellom generiske Byggforsk-intervaller og spesifikke FDV-data fra leverandør.
- **Målepunkt M1.2:** Endring i valgt løsning når fuktrisiko og LCC-konsekvenser synliggjøres i testflaten under tilbudsarbeid.

---

## 4.2 FoU-spørsmål F2: Dataintegrasjon tidlig i tilbudsfasen

### Problemstilling
Byggevaredata (NOBB, GTIN, EPD, FDV) eksisterer i dag i fragmenterte databaser som først kobles i prosjekterings- eller as-built-fasen. Da er løsningsvalgene låst, og handlingsrommet for å redusere materialenes klimagassutslipp (A1–A3) er tapt.

### Spørsmålsformulering F2
> *Hvordan kan heterogene produkt- og miljødata (NOBB, GTIN, EPD, FDV) struktureres og kobles mot tilbudskalkylen slik at pålitelige LCA- og LCC-beregninger kan utføres automatisk i tilbudsfasen før valgene låses?*

### Hypotese
Ved å koble NOBB/GTIN-varenumre direkte mot EPD-Norge og generiske LCI-databaser med TEK17 1,25-sikkerhetsfaktor, kan tiden som kreves for å sammenstille et klimagassregnskap for et tilbud reduseres med over 70 %, samtidig som datadekningen økes til over 85 % i tilbudskalkylen.

### Uavhengig kildeforankring
- **Norsk primærbaselinje:**
  - `[KD2024]` 🟡 (KDD/DiBK 2024): Dokumenterer at 63–70 % av utslippene skjer i A1–A3, og at påvirkningsrommet er størst i tilbudsfasen (Figur 1).
  - `[Multiconsult2023DiBK]` 🟢 (DiBK 2023): Bekrefter 70 % A1–A3-dominansen i 4 norske referansebygg.
  - `[BKA2]` 🟢 (SINTEF / Knotten 11,7 MNOK): Etablerer behovet for tilbudsintegrerte bærekraftskriterier i hverdagsbyggeriet.
- **Sekundær internasjonalkontekst:** `[Benke2025]` 🟢 (LCA-variasjon), `[Ciroth2016]` 🟡 (Pedigree-matrise i ecoinvent).

### Eksperimentelle målepunkter og pilot-KPI-er
- **Målepunkt M2.1:** Tidsbruk i minutter per tilbudslinje for å henvente og koble EPD-, levetids- og prisdata før vs. etter bruk av VERIFIED testflate.
- **Målepunkt M2.2:** Prosentandel tilbudslinjer med verifisert EPD-dekning (DQI 1–2) oppnådd i pilotprosjektene.

---

## 4.3 FoU-spørsmål F3: Ombruk, reparasjon og rehabilitering

### Problemstilling
Ombruk og rehabilitering av byggevarer hemmes av usikkerhet rundt teknisk tilstand, fukthistorikk, manglende EPD-data og uklare garantiansvar. Standardiserte MCDA-modeller (f.eks. TOPSIS) risikerer å utløse Rank Reversal når brukte og nye komponenter sammenlignes.

### Spørsmålsformulering F3
> *Hvordan kan flerkriteriemodellen strukturere og synliggjøre avveininger mellom ombruk, reparasjon, rehabilitering og nyanskaffelse, og i hvilken grad reduserer absolutte verdi-funksjoner (MIVES) fare for Rank Reversal sammenlignet med relativt normaliserte metoder?*

### Hypotese
En hybride AHP-MIVES-modell med absolutte verdi-funksjoner opprettholder rangeringstabilitet (0 % Rank Reversal) ved introduksjon av ombruksalternativer, og dokumenterer at bevaring/rehabilitering i henhold til EN 15978:2026 `[EN15978-2026]` 🟢 gir opptil 50 % reduksjon i A1–A3-utslipp sammenlignet med nybygg.

### Uavhengig kildeforankring
- **Norsk primærbaselinje:**
  - `[Bjørheim2026]` 🟡 (Bisnode/SINTEF 2026): Dokumenterer rammebetingelser og dokumentasjonsbarrierer for sirkulære byggevarer i Norge.
  - `[KD2024]` 🟡 (KDD/DiBK 2024): Sirkulære gjenbruksrammer i statlig kunnskapsgrunnlag (NFR 2026 sirkulærøkonomi 40 MNOK satsing; Bærekraftsmål SDG 12.2 og 12.5).
  - `[Ingvaldsen2008]` 🟡 & `[FinansNorge2024VASK]` 🟢: Vurdering av ombruk mot fuktrisiko og teknisk levetid.
- **Sekundær internasjonalkontekst:** `[Mecca2023]` 🟡 (MCDA review og Rank Reversal reservation), `[CPR2024]` / `[ESPR2024]`.

### Eksperimentelle målepunkter og pilot-KPI-er
- **Målepunkt M3.1:** Frekvens for Rank Reversal i testscenarier ved tilføyelse av ombruks- eller rehabiliteringsalternativer under TOPSIS vs. AHP-MIVES.
- **Målepunkt M3.2:** Andel pilotscenarier hvor ombruk eller rehabilitering velges når fukthistorikk og levetidsgaranti er synliggjort.

---

## 4.4 FoU-spørsmål F4: SMB-forståelse og beslutningsstøtte uten svart boks

### Problemstilling
Små og mellomstore entreprenører (SMB) har lave driftsmarginer (3,3 %) og mangler kapasitet til å betjene kompliserte ekspertverktøy. Ugjennomsiktige aggregatskårer ("svarte bokser") skaper mistillit og forhindrer reell forståelse av valgkonsekvenser.

### Spørsmålsformulering F4
> *Hvordan må beslutningsstøtten utformes for at ikke-spesialister i SMB-segmentet skal forstå datagrunnlaget, vektingen og usikkerheten, og i hvilken grad påvirker synlig usikkerhet de valg som tas i tilbudsfasen?*

### Hypotese
Når datagrunnlag og usikkerhet eksponeres gjennom transparente DQI-statuser (Edelen 2018) og mulighetsrom (Lohman 2023) heller enn én enkelt score, rapporterer over 80 % av SMB-brukerne høy tillit til verktøyet, og valgene endres fra laveste CapEx til høyest levetidsverdi i minst 25 % av sakene.

### Uavhengig kildeforankring
- **Norsk primærbaselinje:**
  - `[Bjørheim2026]` 🟡 (2026): Dokumenterer bransjens pressede marginer (3,3 %) og 1 583 konkurser i 2025.
  - `[BKA2]` 🟢 (SINTEF / Knotten 11,7 MNOK): Bærekraftstilpasning for hverdagsbyggeriet uten administrative barrierer.
  - `[KD2024]` 🟡 & `[EBA_NO2023]` 🟡: Behov for enkle, pedagogiske beslutningsflater.
- **Sekundær internasjonalkontekst:** `[Edelen2018]` 🟢 (Ingen skjult totalscore), `[Lohman2023]` 🟢 (Visning av usikkerhet).

### Eksperimentelle målepunkter og pilot-KPI-er
- **Målepunkt M4.1:** Brukerforståelse og tillit målt via standardiserte SUS-skjemaer (System Usability Scale) etter gjennomførte pilottilbud.
- **Målepunkt M4.2:** Frekvens av endrede løsningsvalg hos entreprenør/kunde etter at mulighetsrom og usikkerhet ble gjort synlig i testflaten.

---

## 4.5 FoU-spørsmål F5: Byggdata mot bank, forsikring og takst

### Problemstilling
Finans- og forsikringssektoren mangler verifiserte bygningstekniske kvalitetsdata når de vurderer utlånsrisiko og forsikringsvilkår. Eksisterende grønne utlån baserer seg utelukkende på teoretisk energiklasse, noe som ignorerer fuktrisiko, vedlikeholdsbyrde og fysisk skadeeksponering.

### Spørsmålsformulering F5
> *Hvordan kan verifisert byggteknisk dokumentasjon, levetid og fuktrobusthet struktureres som relevant tilleggsinformasjon for bankens risikovurderinger, uten personprofilering eller automatisk kredittbeslutning?*

### Hypotese
Strukturert overføring av dokumentert bygningsteknisk kvalitet (DQI 1–2, fuktsikring og FDV) gir bankenes risikoanalytikere tilstrekkelig datagrunnlag til å klassifisere bygget som lavrisikoeiendom under EBA EU `[EBA_EU2023]` 🟢 grønne utlånsrammer, noe som kan gi gunstigere lånebetingelser eller lavere forsikringspremie.

### Uavhengig kildeforankring
- **Norsk primærbaselinje:**
  - `[FinansNorge2024VASK]` 🟢 (Finans Norge 2024): Dokumenterer 5,1 mrd. kr i utbetalte vannskader (87 600 skader/år).
  - `[GullbrekkenHolme2025]` 🟡 (SINTEF 2025): Byggfeil for 10–30 mrd. kr/år forringer panteverdier i norske boliger.
  - `[EBA_NO2023]` 🟡: Byggteknisk dokumentasjon i norsk bransjeveileder.
- **Sekundær internasjonalkontekst:** `[Billio2022]` 🟢 (Misligholdsrisiko PD på boliglån), `[Kaza2014]` 🟢 (~32 % lavere PD for ENERGY STAR), `[An2020]` 🟡 (34 % lavere PD på kommersielle CMBS-lån), `[EBA_EU2023]` 🟢 (EU Green Loan Report), `[BoE_PS25-25]` 🟡 & `[BoE_DP1-25]` 🟡 (Bank of England IRB PD/LGD-rammeverk).

### Eksperimentelle målepunkter og pilot-KPI-er
- **Målepunkt M5.1:** Evaluering fra deltakende bankanalytikere om datakvalitetspakkens fullstendighet for grønn utlånsklassifisering.
- **Målepunkt M5.2:** Verifisering av at ingenting av de overførte dataene inneholder personopplysninger eller utløser automatisk kredittprofilering.

---

## 4.6 FoU-spørsmål F6: Sporbarhet, digital dataflyt og skalering

### Problemstilling
Digitale byggevaredata forblir fastlåst i leverandørspesifikke formater. Mangel på apner API-er og standardiserte datamodeller hindrer sømløs sporbarhet gjennom byggets livsløp og gjør det krevende å skalere beregningsmodellen til nye produktkategorier.

### Spørsmålsformulering F6
> *Hvordan kan datastruktur, API-integrasjoner og sporbarhetsmekanismer utformes slik at beslutningsmodellen er etterprøvbar og sømløst kan overføres fra den første pilotkategorien til nye produktkategorier i byggebransjen?*

### Hypotese
Ved å utforme datamodellen basert på åpne standarder (NS-EN ISO 22057, EU CPR `[CPR2024]` og ESPR `[ESPR2024]` Digitalt Produktpass), kan modellen skaleres til en ny produktkategori (f.eks. vinduer/isolasjon) med under 20 % av den opprinnelige utviklingsinnsatsen, samtidig som full datasporbarhet opprettholdes.

### Uavhengig kildeforankring
- **Norsk primærbaselinje:**
  - `[KD2024]` 🟡 (DiBK/KDD 2024): Dokumenterer 17,3 Mt CO₂e og behov for harmonisert digital rapportering.
  - `[BKA2]` 🟢 (11,7 MNOK): Etablerer nasjonale datastrukturer for anskaffelser.
  - Nasjonal datainfrastruktur: NOBB / Norsk Byggtjeneste, EPD-Norge og Cobuilder.
- **Sekundær internasjonalkontekst:** `[CPR2024]` (Revidert byggevareforordning), `[ESPR2024]` (Digitalt Produktpass - DPP).

### Eksperimentelle målepunkter og pilot-KPI-er
- **Målepunkt M6.1:** Tidsbruk og kode-gjenbruksgrad (%) ved overføring av testflatens datamodell fra første pilotkategori (f.eks. tak/kledning) til andre produktkategori.
- **Målepunkt M6.2:** Verifisert integritet i datakjeden fra NOBB GTIN / EPD via tilbudskalkylen til FDV-leveranse.

---

# Seksjon 5: Forskningsmetode og testsløyfe

VERIFIED-prosjektets forskningsmetodikk er utformet som en **closed-loop 7-stegs iterativ FoU-prosess**. Prosessen binder sammen teoretisk datamodellering, stochastisk usikkerhetsrepresentasjon, flerkriterie-algoritmer og empirisk utprøving i levende SMB-byggeprosjekter.

```
+---------------------------------------------------------------------------------------------------+
|                            VERIFIED RESEARCH METHODOLOGY & TEST LOOP                              |
+---------------------------------------------------------------------------------------------------+
|  [STEG 1: HETEROGEN DATAFANGST OG INGESTION]                                                      |
|  - EPDs (NS-EN 15804+A2), NOBB GTIN, Byggforsk 700.320 levetid, Finans Norge skadestatistikk      |
+---------------------------------------------------------------------------------------------------+
                                                 │
                                                 ▼
+---------------------------------------------------------------------------------------------------+
|  [STEG 2: DQI & TEK17 SIKKERHETSFAKTOR-ASSIGNMENT]                                                |
|  - Evaluere 5 DQI-dimensjoner (Weidema 1996) ──> Tildele kvalitetskategori (1 til 5)                |
|  - Påføre TEK17 § 9-2 sikkerhetsfaktor: Multiplisere generiske databasetall med 1,25 (+25 % straff) |
|  - Kategori-taxonomi: Verifisert 🟢 | Generisk 🟢/🟡 | Estimert 🟡 | Manglende 🔴/🟡               |
+---------------------------------------------------------------------------------------------------+
                                                 │
                                                 ▼
+---------------------------------------------------------------------------------------------------+
|  [STEG 3: STOCHASTISK USIKKERHETSPROPAGERING]                                                     |
|  - Beregne ecoinvent lognormal standardavvik: ln(SD95) = sqrt(sigma_basic^2 + sum sigma_i^2)       |
|  - Kjøre Monte Carlo-simuleringer (10 000 iterasjoner) per løsningsvalg for konfidensintervaller  |
+---------------------------------------------------------------------------------------------------+
                                                 │
                                                 ▼
+---------------------------------------------------------------------------------------------------+
|  [STEG 4: HYBRID AHP-MIVES MCDA-MOTOR MED RANK REVERSAL-SIKRING]                                  |
|  - AHP parvis sammenligning for å fange brukerens preferanseprofil (Mecca 2023)                   |
|  - MIVES absolutte verdifunksjoner (normaliserer mot faste fysiske grenser for å hindre Rank Rev.) |
|  - Automatisk varsling ved overlappende konfidensintervaller                                      |
+---------------------------------------------------------------------------------------------------+
                                                 │
                                                 ▼
+---------------------------------------------------------------------------------------------------+
|  [STEG 5: TESTFLATE-VISUALISERING OG BESLUTNINGSSTØTTE]                                            |
|  - Generere "Mulighetsrom" (Lohman 2023 / EC3) som viser achievable vs conservative spenn        |
|  - Eksponere DQI-statuser transparent (Edelen 2018: INGEN skjult totalscore / INGEN svart boks)   |
+---------------------------------------------------------------------------------------------------+
                                                 │
                                                 ▼
+---------------------------------------------------------------------------------------------------+
|  [STEG 6: PILOTPROSJEKT-EVALUERING OG ATTRIBUTION-LOGGING]                                         |
|  - Utrulle testflaten i live SMB-tilbudsprosesser (Synergi mot BKA2 / Knotten)                    |
|  - Logge anonymiserte beslutningshendelser: Måle om beslutningsstøtten bekreftet/endret valget    |
+---------------------------------------------------------------------------------------------------+
                                                 │
                                                 ▼
+---------------------------------------------------------------------------------------------------+
|  [STEG 7: EMPIRISK FEEDBACK OG MODELLKALIBRERING]                                                 |
|  - Finjustere DQI-vekting, bankrisikoproxy og grensesnittpedagogikk basert på pilotmålingene      |
+---------------------------------------------------------------------------------------------------+
```

---

# Seksjon 6: Sannhetsserum- og kildehierarkimatriks

I tråd med prosjektets Sannhetsserum (`sannhetsserum-oppdatering-v0.5.md` og `vibs-verified-kildedom-2026-06-27.md`) kategoriseres samtlige kilder og påstander i en eksplisitt statusmatrise. Parkere kilder (`[Wiik2025]` ⏸ og `[SA2018]` ⏸) benyttes ikke som selvstendig bevis.

```
+---------------------------------------------------------------------------------------------------+
|                                SANTHETSSERUM & KILDEHIERARKIMATRIKS                               |
+---------------------+-----------------------+--------+--------------------------------------------+
| Kilde-ID            | Tittel / Utgiver      | Status | Sannhetsserum-regel & Bevisrolle           |
+---------------------+-----------------------+--------+--------------------------------------------+
| GullbrekkenHolme2025| SINTEF Kronikk (2025) | 🟡     | Primær norsk: 10–30 mrd. NOK/år i feil.   |
|                     | Gullbrekken & Holme   |        | Dokumenterer problemrommet for F1.         |
+---------------------+-----------------------+--------+--------------------------------------------+
| Ingvaldsen2008      | SINTEF Byggforsk 308  | 🟡     | Primær norsk: 75 % fuktskader. Etablerer   |
|                     | Tage Ingvaldsen (2008)|        | teknisk levetid og fuktrisiko for F1.      |
+---------------------+-----------------------+--------+--------------------------------------------+
| Bjørheim2026        | Bisnode / Byggeind.   | 🟡     | Primær norsk: 1 583 konkurser, 3,3 % margin|
|                     | Tommy Bjørheim mfl.   |        | Dokumenterer SMB-sårbarhet for F4.         |
+---------------------+-----------------------+--------+--------------------------------------------+
| KD2024              | KDD / DiBK (2024)     | 🟡     | Primær norsk: 70 % A1–A3, tidligfaserom.   |
|                     | Kunnskapsgrunnlag     |        | Bærende myndighetskilde for F2/F3.         |
+---------------------+-----------------------+--------+--------------------------------------------+
| Multiconsult2023DiBK| Multiconsult / DiBK   | 🟢     | Primær norsk: 4 referansebygg, 70 % A1–A3. |
|                     | Analysereferanse      |        | Empirisk baseline for F1/F2.               |
+---------------------+-----------------------+--------+--------------------------------------------+
| EBA_NO2023          | EBA Norge (2023/2025) | 🟡     | Primær norsk: 20 % CO₂-kutt uten CapEx.    |
|                     | Bransjeveileder       |        | Bærende kilde for kostnadsnøytralitet (F1).|
+---------------------+-----------------------+--------+--------------------------------------------+
| BKA2                | SINTEF / Knotten      | 🟢     | Primær norsk: 11,7 MNOK anskaffelse.       |
|                     | Trondheim kommune     |        | Bestiller-grensesnitt for F4.              |
+---------------------+-----------------------+--------+--------------------------------------------+
| FinansNorge2024VASK | Finans Norge (2024)   | 🟢     | Primær norsk: 5,1 mrd. kr i vannskader.    |
|                     | Skadestatistikk 2023  |        | Bærende kilde for fuktrisiko i F1/F5.      |
+---------------------+-----------------------+--------+--------------------------------------------+
| Edelen2018          | Edelen & Ingwersen    | 🟢     | Sekundær int.: Formålsavhengig DQI.        |
|                     | Int. J. LCA (2018)    |        | Forbud mot skjult totalscore / svart boks. |
+---------------------+-----------------------+--------+--------------------------------------------+
| Weidema1996         | Weidema & Wesnæs      | 🟡     | Sekundær int.: Pedigree-matrise (5 DQI-er).|
|                     | J. Clean. Prod. (1996)|        | Stochastisk usikkerhet i ecoinvent.        |
+---------------------+-----------------------+--------+--------------------------------------------+
| Mecca2023           | Mecca (2023)          | 🟡     | Sekundær int.: MCDA review i bygg.         |
|                     | J. MCDA               |        | Metodisk forbehold mot Rank Reversal.      |
+---------------------+-----------------------+--------+--------------------------------------------+
| Benke2025           | Benke mfl. (2025)     | 🟢     | Sekundær int.: LCA-verktøyvariasjon.       |
|                     | Sci. Data (2025)      |        | Begrunner verktøyuavhengig modellering.    |
+---------------------+-----------------------+--------+--------------------------------------------+
| Lohman2023          | Lohman mfl. (2023)    | 🟢     | Sekundær int.: Usikkerhetsvisning.         |
|                     | ACS Environ. Au (2023)|        | Begrunner mulighetsrom-visualisering.      |
+---------------------+-----------------------+--------+--------------------------------------------+
| Billio2022          | Billio mfl. (2022)    | 🟢     | Sekundær int.: Boliglån & energimerker.    |
|                     | J. Real Est. Fin. (22)|        | Dokumenterer energi↔PD korrelasjon.        |
+---------------------+-----------------------+--------+--------------------------------------------+
| Kaza2014            | Kaza mfl. (2014)      | 🟢     | Sekundær int.: ~32 % lavere PD ENERGY STAR |
|                     | Cityscape (2014)      |        | Baseline for grønne boliglån.              |
+---------------------+-----------------------+--------+--------------------------------------------+
| An2020              | An & Pivo (2020)      | 🟡     | Sekundær int.: 34 % lavere PD på CMBS.     |
|                     | Real Est. Econ. (2020)|        | Kun næringsbygg; ALDRI for boliglån.       |
+---------------------+-----------------------+--------+--------------------------------------------+
| Ciroth2016          | Ciroth mfl. (2016)    | 🟡     | Sekundær int.: Empirisk pedigree-varians.  |
|                     | Int. J. LCA (2016)    |        | Validerer stochastisk modell i ecoinvent.  |
+---------------------+-----------------------+--------+--------------------------------------------+
| EBA_EU2023          | European Banking Auth.| 🟢     | Sekundær int.: EU Green Loan Report.       |
|                     | EBA/Op/2023/13        |        | Identifiserer databottleneck for bank.     |
+---------------------+-----------------------+--------+--------------------------------------------+
| BoE_PS25-25         | Bank of England (2025)| 🟡     | Sekundær int.: Klimarisikokrav juni 2026.  |
|                     | PRA Policy Statement  |        | Bankenes klimaansvar-mandat.               |
+---------------------+-----------------------+--------+--------------------------------------------+
| BoE_DP1-25          | Bank of England (2025)| 🟡     | Sekundær int.: IRB PD/LGD-modellveileder.  |
|                     | PRA Discussion Paper  |        | Kredittrisikomodellering for boliglån.     |
+---------------------+-----------------------+--------+--------------------------------------------+
| Wiik2025            | Wiik (SINTEF Notat 57)| ⏸      | PARKERT CONSORTIUM NOTE. Skal IKKE bære   |
|                     | Konsortienotat (2025) |        | søknadspåstander alene.                    |
+---------------------+-----------------------+--------+--------------------------------------------+
| SA2018              | Samfunnsøk. Analyse   | ⏸      | PARKERT UVERIFISERT KILDE. Skal IKKE bære |
|                     | Rapport 4-2018        |        | søknadspåstander alene.                    |
+---------------------+-----------------------+--------+--------------------------------------------+
```

---

# Seksjon 7: Ontologisk og terminologisk sjekkliste

Dette avsnittet bekrefter at Notat K3 tilfredsstiller prosjektets strengeste ontologiske og terminologiske krav per `vibs-verified-ord-og-kildekart-v0.5.yml` og `sannhetsserum-oppdatering-v0.5.md`.

## 7.1 Terminologiregler – Verifikasjonsstatus
- [x] **Løsningsvalg (🟢 Påkrevd):** Benyttet konsekvent når scope gjelder mer enn et enkelt produktvalg (produkt + utførelse + levetid + LCC). Begrepet «produktvalg» er uønsket og er eliminert fra helhetlige vurderinger.
- [x] **Beslutningsstøtte (🟢 Påkrevd):** VERIFIED omtales konsekvent som et forklarende sammenligningsverktøy («beslutningsstøtte»). Formuleringer som «VERIFIED velger automatisk» eller «anbefaler optimalt produkt» er strengt forbudt.
- [x] **Forklarbarhet og ingen svart boks (🟢 Påkrevd):** Vektingslogikk, datagrunnlag og usikkerhet eksponeres synlig uten skjulte samleskårer («svart boks»).
- [x] **Testflate (🟢 Påkrevd):** Den eksisterende VIBS-plattformen omtales konsekvent som *«VIBS-plattformen som testflate»*, mens VERIFIED utgjør det overliggende FoU-laget.
- [x] **Streng separasjon av EBA-kilder (🟢 Påkrevd):** `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg Norge - veileder boligblokker) og `[EBA_EU2023]` (European Banking Authority - grønne lån) er strengt adskilt. Uspesifisert akronym «EBA» er forbudt.
- [x] **Klimaeffekt som mulighetsrom (🟢 Påkrevd):** Klimagassreduksjon fremstilles som et *mulighetsrom* som skal utforskes og måles i pilotene, ikke som en garantert programvare-effekt.
- [x] **Obligatorisk teknisk port (🟢 Påkrevd):** Teknisk egnethet, fuktrobusthet og dokumentasjonskvalitet utgjør en obligatorisk faglig port som filtrerer ut uegnede alternativer før flerkriteriesammenligning utføres.

## 7.2 Verifikasjon av de 10 obligatoriske sjekkpunktene
1. **Sjekk 1 (Løsningsvalg):** `grep_search` i teksten Bekrefter at «løsningsvalg» benyttes konsekvent i alle helhetlige sammenligninger.
2. **Sjekk 2 (Beslutningsstøtte):** VERIFIED er gjennomgående beskrevet som beslutningsstøtte for entreprenør og kunde.
3. **Sjekk 3 (Testflate):** VIBS-plattformen er eksplisitt avgrenset som prosjektets eksperimentelle testflate.
4. **Sjekk 4 (EBA-skille):** `[EBA_NO2023]` og `[EBA_EU2023]` benyttes med sine fullstendige, adskilte referanser.
5. **Sjekk 5 (Norsk kildeprioritet):** De 8 norske uavhengige forsknings- og myndighetskildene (`[KD2024]`, `[Multiconsult2023DiBK]`, `[EBA_NO2023]`, `[GullbrekkenHolme2025]`, `[Ingvaldsen2008]`, `[FinansNorge2024VASK]`, `[BKA2]`, `[Bjørheim2026]`) utgjør det primære fundamentet i seksjon 1, 2, 4 og 6.
6. **Sjekk 6 (Parkerte kilder):** `[Wiik2025]` ⏸ og `[SA2018]` ⏸ er registrert som parkert og bærer ingen søknadspåstander alene.
7. **Sjekk 7 (Klima-mulighetsrom):** Klimaeffekt behandles som et testbart mulighetsrom (0–20 % utslippskutt).
8. **Sjekk 8 (Teknisk port):** Teknisk egnethet og fuktrobusthet filtrerer alternativer før pris og CO₂ vurderes.
9. **Sjekk 9 (FoU-målepunkter):** Samtlige forskningsspørsmål (F1–F6) er koblet til observerbare pilot-KPI-er (M1.1–M6.2).
10. **Sjekk 10 (Banksporets avgrensning):** F5 er eksplisitt avgrenset til bygningsteknisk dokumentasjon for grønn finans uten personprofilering eller automatiske kredittbeslutninger.

---
*Kandidatnotat Kapittel K3 (v0.5) ferdigstilt av Worker (`worker_k3_draft_1`).*
