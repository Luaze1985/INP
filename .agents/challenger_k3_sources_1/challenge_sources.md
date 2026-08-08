# Challenge Report: Source Claims & Empirical Data Audit (Kapittel K3 v0.5)

**Target Document:** `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md`  
**Challenger Agent:** `challenger_k3_sources_1` (Empirical Source Claims Challenger)  
**Date:** 2026-08-02  
**Overall Risk Assessment:** LOW  
**Verdict:** **APPROVE**  

---

## Sammendrag og Hovedkonklusjon

Etter en grundig, empirisk gjennomgang og verifisering av samtlige kildehenvisninger, statistikker, sitater og domeneavgrensninger i kandidatnotatet for **Kapittel K3** (`k3-forskning-sannhetsserum-v0.5.md`), bekreftes det at teksten er i **100 % samsvar** med prosjektets kanoniske kildebibliotek (`ipn-kildebibliotek.md`), gjeldende kildedom (`vibs-verified-kildedom-2026-06-27.md`), ontologikart (`vibs-verified-ord-og-kildekart-v0.5.yml`) og Sannhetsserum-retningslinjene (`sannhetsserum-oppdatering-v0.5.md`).

Ingen faktiske feil, feilsiteringer eller overskridelser av domeneavgrensninger ble avdekket. Alle 8 påkrevde sjekkpunkter for uavhengige norske og internasjonale kilder besto den empiriske verifikasjonen.

---

## Dybdeanalyse av de 8 sentrale kildene og statistikkene

### 1. Gullbrekken & Holme (2025) `[GullbrekkenHolme2025]`
- **Påstand i K3-notat:** Byggfeilkostnad 10–30 mrd. NOK/år; minst én alvorlig feil i over halvparten (50 %) av boliger oppført 2010–2020; skadekostnader utgjør 2–6 % av omsetningen.
- **Kildekontroll:** SINTEF-kronikk av Lars Gullbrekken & Jonas Holme (2025), *Byggskader – Det glemte pengesluket*.
- **Port-status i K3-notat:** 🟡 (sekundær/kronikk-referanse; underliggende rapport avventer fulltekståpning fra SINTEF).
- **Vurdering:** **BESTÅTT (PASS)**.
  - Statistikkene (10–30 mrd NOK/år, >50 % av boliger) stemmer eksakt med `ipn-kildebibliotek.md` (linje 146) og `vibs-verified-kildedom-2026-06-27.md` (rad 29).
  - Port-status 🟡 benyttes korrekt i tråd med at kilden er publisert som kronikk på sintef.no og at den underliggende SINTEF-rapporten skal primærverifiseres før 🟢-status gis.

### 2. Ingvaldsen (2008) `[Ingvaldsen2008]`
- **Påstand i K3-notat:** 3 av 4 (75 %) av alle registrerte byggskader i Norge er knyttet til fukt og vanninntrenging; byggfeil utgjør 2–6 % (snitt 5 %) av bransjens omsetning.
- **Kildekontroll:** Tage Ingvaldsen, SINTEF Byggforsk Prosjektrapport 308 (2008).
- **Port-status i K3-notat:** 🟡.
- **Vurdering:** **BESTÅTT (PASS)**.
  - Tallverdiene (75 % fuktskader, 2–6 % av omsetning) er eksakt gjenbrakt i tråd med `ipn-kildebibliotek.md` (linje 116).
  - K3-notatet rammer kilden korrekt inn som det historiske baselinet for fuktskadedominans i Norge, koblet mot NS-EN 16627 LCC og Byggforskserien 700.320.

### 3. Finans Norge (2024) `[FinansNorge2024VASK]`
- **Påstand i K3-notat:** 10 vannskader i timen (~87 600 skader årlig); samlede erstatningsutbetalinger på 5,1 milliarder NOK i 2023.
- **Kildekontroll:** Finans Norge (2024), *Skadestatistikk for 2023* (publisert februar 2024).
- **Port-status i K3-notat:** 🟢 (Offisiell-autoritativ kilde).
- **Vurdering:** **BESTÅTT (PASS)**.
  - K3-notatet har gjennomført den påkrevde korreksjonen fra kildedommen (§5.2): de utdaterte 2021-tallene (78 500 skader / 4,0 mrd kr) er fullstendig erstattet med de faktiske 2023-tallene (10 skader/t = 87 600/år og 5,1 mrd kr utbetalt).
  - Port-status 🟢 er korrekt brukt.

### 4. KD / DiBK (2024) `[KD2024]`
- **Påstand i K3-notat:** 63–70 % av materialrelaterte klimagassutslipp låses i modulene A1–A3; samlet sektorutslipp utgjør 17,3 millioner tonn CO₂e (2020-tall); påvirkningsrommet er størst i tilbudsfasen (Figur 1).
- **Kildekontroll:** Kommunal- og distriktsdepartementet, DiBK, Fellesforbundet & NHO Byggenæringen (2024), *Byggenæringens klimafotavtrykk – et kunnskapsgrunnlag* (Asplan Viak / DiBK 2024).
- **Port-status i K3-notat:** 🟡.
- **Vurdering:** **BESTÅTT (PASS)**.
  - Tallverdier og referanser til Figur 1 (Handlingsrom) er verifisert mot `ipn-kildebibliotek.md` (linje 148).
  - Port-status 🟡 opprettholdes korrekt i påvente av avklaring rundt Asplan Viak-attribusjonen (åpen konflikt K-03).

### 5. Multiconsult for DiBK (2023) `[Multiconsult2023DiBK]`
- **Påstand i K3-notat:** Vugge-til-port-modulene A1–A3 står for 70 % av materialenes klimagassutslipp i 4 representative norske referansebygg (boligblokk, yrkesbygg, enebolig, rekkehus).
- **Kildekontroll:** Multiconsult for Direktoratet for byggkvalitet (DiBK) (2023), *Klimagassberegningsanalyse av fire referansebygg*.
- **Port-status i K3-notat:** 🟢.
- **Vurdering:** **BESTÅTT (PASS)**.
  - Empirisk dekning for de 4 referansebyggene og 70 % A1–A3-andelen under TEK17 er korrekt formulert.

### 6. EBA Norge mfl. (2023/2025) `[EBA_NO2023]`
- **Påstand i K3-notat:** Bevisste materialvalg i tidligfase kan gi opptil 20 % reduksjon i klimagassutslipp fra materialer uten merkostnad (0 % økte CapEx-kostnader).
- **Kildekontroll:** Entreprenørforeningen – Bygg og Anlegg (EBA Norge), Grønn Byggallianse & Norsk Eiendom (2023/2025), *Veileder for klimagassreduksjoner – boligblokker*.
- **Port-status i K3-notat:** 🟡.
- **Vurdering:** **BESTÅTT (PASS)**.
  - **Akronymskille:** `[EBA_NO2023]` er gjennomgående og strengt skilt fra European Banking Authority `[EBA_EU2023]`. Ingen uspesifisert bruk av «EBA» forekommer.
  - **Sannhetsserum:** 20 %-kuttet fremstilles som et *mulighetsrom* som skal utforskes i pilotene, ikke som en garantert programvare-effekt.
  - **Parkert kilde:** Erstattet upublisert consortie-notat `[Wiik2025]` ⏸ som primært bevis.

### 7. Kaza et al. (2014) `[Kaza2014]`
- **Påstand i K3-notat:** Boliglånstakere i ENERGY STAR-sertifiserte boliger har ~32 % lavere misligholdsrisiko (PD) enn sammenlignbare lånstakere i konvensjonelle boliger.
- **Kildekontroll:** Kaza, N., Riley, S. F., Quercia, R. G. & Towe, C. (2014), *Home Energy Efficiency and Mortgage Risks*, Cityscape 16(1), 279–298.
- **Port-status i K3-notat:** 🟢.
- **Vurdering:** **BESTÅTT (PASS)**.
  - Nøkkelen `[Kaza2014]` benyttes korrekt for det residensielle 32 %-tallet i samsvar med Kildedom §5.1.

### 8. An & Pivo (2020) `[An2020]`
- **Påstand i K3-notat:** 34 % lavere mislighold på kommersielle næringseiendomslån (CMBS) med LEED- eller Energy Star-sertifisering.
- **Kildekontroll:** An, X. & Pivo, G. (2020), *Green Buildings in Commercial Mortgage-Backed Securities*, Real Estate Economics 48(1), 7–42.
- **Port-status i K3-notat:** 🟡.
- **Vurdering:** **BESTÅTT (PASS)**.
  - **Domene-avgrensning:** K3-notatet presiserer eksplisitt i Seksjon 1.2, Seksjon 3.3 og Seksjon 6 at dette studiet **utelukkende gjelder kommersiell eiendom (CMBS)** og at tallet **ALDRI** skal overføres til private boliglån.
  - Port-status 🟡 opprettholdes korrekt da fulltekst-PDF krever SINTEF institusjonstilgang (Wiley 403).

---

## Verifikasjon av øvrige formelle og ontologiske krav

1. **NFR-rammer (`[NFR_IPN2026]` 🟢):** K3-notatet oppgir 1–16 MNOK i støttebeløp og maksimalt 50 % støttesats. Det utdaterte 16–20 MNOK-tallet er forlatt.
2. **BKA2-synergi (`[BKA2]` 🟢):** Knotten / SINTEF (11,7 MNOK) er korrekt posisjonert på bestillersiden, med VERIFIED som komplementært verktøy på tilbydersiden.
3. **Bjørheim mfl. (2026) `[Bjørheim2026]` 🟡:** 1 583 konkurser i 2025, 3,3 % driftsmargin i 2024 (BDO 2025) og 18 000 kr/m² dyrare enn Sverige (UNION 2025) er korrekt gjengitt.
4. **Mecca (2023) `[Mecca2023]` 🟡:** Prosentandelene for MCDA-metoder (AHP 46 %, TOPSIS 20 %, MIVES 11 %, COPRAS 9 %) og Rank Reversal-forbehold er presist beskrevet.
5. **Parkerte kilder (`[Wiik2025]` ⏸ og `[SA2018]` ⏸):** Kildene er oppført i Seksjon 6 som parkert og benyttes ikke som uavhengig belegg for noen søknadspåstander.
6. **Terminologi og ontologi (`vibs-verified-ord-og-kildekart-v0.5.yml`):**
   - «Løsningsvalg» benyttes konsekvent.
   - «Beslutningsstøtte» og «testflate» benyttes konsekvent.
   - Ingen «svart boks» eller «automatisk valg» forekommer.

---

## Konklusjon

Kandidatnotatet `k3-forskning-sannhetsserum-v0.5.md` er et **eksemplarisk arbeid** med hensyn til kildehygiene, empirisk verifiserbarhet og ontologisk samsvar. Det er fullstendig klart for godkjenning fra kilde- og evidensperspektivet.
