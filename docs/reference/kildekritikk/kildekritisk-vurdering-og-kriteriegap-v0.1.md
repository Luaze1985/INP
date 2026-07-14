---
title: Kildekritisk vurdering og kriteriegap — VIBS VERIFIED IPN
dato: 2026-07-10
versjon: 0.2
forfatter: AGY (Antigravity) med Gemma4-kvalitetssjekkrunder
status: arbeidsdokument (ikke ren søknadstekst) · QA-gjennomgått 2026-07-10
for: Lars Erik Larsen — internt beslutningsgrunnlag før søknadstekst strammes
---

# Kildekritisk vurdering og kriteriegap — VIBS VERIFIED IPN (v0.2)

> **Hva dette dokumentet er.** Et arbeidsdokument for Lars Erik. Det er ikke søknadsprosa. Det forteller hva som holder, hva som henger i løse ender og hva som må avgjøres før Codex/Claude kan skrive rent søknadsutkast til Lars Gunnar. Alle kanoniske kildestatusfiler er lest, men ikke endret. Søknadstekst skal først lages etter denne porten.
>
> **Gemma4-runder.** Nøkkelpåstander er sendt til lokal Gemma4 (gemma4:latest, Q4_K_M, kjørt på localhost:11434) for intern konsistenssjekk. Resultater er merket **[G4-sjekk]** der det er relevant.

---

## 1. Kort dom

### 1a. Hva treffer søknaden godt?

| Tema | Vurdering |
| --- | --- |
| **FoU-hullet og nyhetsverdi** | Sterkt. De seks aksene (dataintegrasjon, tilbudsfase, SMB, forklarbarhet, beslutningseffekt, DNSH-bredde) er klart formulert. Ingen dokumentert løsning kombinerer alle seks. Dette kan bære en fagpanel-vurdering under *Kvalitet*. |
| **Regulatory tailwind** | Sterkt. CPR 2024/3110 (konstruksjons-DPP), ESPR 2024/1781 (DPP), EN 15978:2026, NS-EN 16627 — alle grønne. Gir regelverk-momentum. |
| **Grønn finans / energi-PD** | Grønt for boliglån (Billio 2022 og Kaza 2014). An & Pivo 2020 er foreløpig metadata/fulltekst-gul og gjelder CMBS/næringsbygg, ikke boliglån. |
| **Vannskader / norsk problemdokumentasjon** | Sterk. FinansNorge 2024: 10 vannskader per time, 5,1 mrd NOK/år — primærverifisert. |
| **EBA Norge 2023: 20% klimagass** | Åpen PDF er funnet og lest. Den sier at reduksjoner rundt 20% kan oppnås uten merkostnad i boligblokk-veilederens kontekst. Ikke oppgrader status automatisk; kildeporten må avstemmes mot kanon og konkret påstand. |
| **GullbrekkenHolme 2025** | Funnet via web-søk: kronikk + debattinnlegg i SINTEF (august 2025). Tall (10–30 mrd NOK/år, halvparten av boliger) er bekreftet sitert der. Primærkilde er SINTEF-publisert kronikk, ikke fulltekst-verifisert intern rapport. Gul — SINTEF åpner fulltekst i august. |
| **Tematisk IPN-match** | God. Bygg, anlegg og eiendom er eksplisitt nevnt i IPN 2026-utlysningen. |

### 1b. Hva er mest risikabelt?

| Risiko | Alvorlighet |
| --- | --- |
| **Ingen baseline for effektmåling (WP3)** | Kritisk. Forskningsrådet krever troverdige planer. Uten definert baseline og måleindikatorer er gjennomføringsdelen svak. |
| **KD2024: tidligfase-kilden mangler primær-URL** | Høy. Brukes som bærende påstand om påvirkningsrom. Web-søk bekrefter at KDD/DiBK/NHO-kunnskapsgrunnlaget eksisterer, men primær-PDF er ikke lagret. |
| **An2020 i næringsbygg, ikke boliglån** | Høy. En systematisk kildefeil: An & Pivo gjelder CMBS (næringsbygg), ikke boliglånsmislighold. Dersom dette brukes feil i søknadstekst, er det en akademisk feil en fagfelle vil flagge umiddelbart. |
| **SMB-definisjon er ikke konsekvent** | Middels. EU-definisjon (under 50 ansatte) er valgt, men norsk praksis bruker ofte under 100 ansatte. Web-søk bekrefter at SSB og NHO bruker under 100 og at EU bruker under 50/250. Ingen andels-tall for byggenæringen er funnet i kanonisk primærkilde ennå. |
| **SA2018 er ikke lokalisert** | Middels. Rapporten er omtalt i sekundærspor, men primærrapport og riktig årstall er ikke lokalisert. Ikke bruk 2,2 mrd.-tallet i søknadsprosa. |
| **WP1–WP5 og Gjennomføring er ikke skrevet** | Kritisk. Hele Gjennomføring-kriteriet mangler substans. |
| **DNSH-tabell mangler** | Kritisk. Bærekraft-sannhetsserumet dokumenterer 9 potensielle do-not-harm-angrep uten at søknaden har svar. |

### 1c. Hva kan skrives som prosjektopplegg uten ekstern kilde?

Følgende kan VIBS beskrive som eget FoU-opplegg — det er prosjektvalg, ikke empiriske påstander som krever ekstern kilde:

- **Beslutningsmodellen (score-logikken):** VIBS-score = Sum(delpoeng x vekting x dokumentasjonstillit). Dette er en metodisk design-beslutning VIBS eier.
- **Seks akser for FoU-hullet:** Tilbudsfase, SMB, flerkriterie, synlig usikkerhet, beslutningseffekt, DNSH-bredde — dette er VERIFIEDs eget konsept.
- **Vektingsprosenten som hypoteser:** Energi/drift (25%), levetid (25%), vedlikehold (15%), CO2 (15%) osv. — dette er forskning, ikke en empirisk påstand om verden.
- **Pilotdesign og måleopplegg:** Hvilke KPI-er, hvem måler, hva er bestillingsalternativet, hvordan avvik registreres — dette er prosjektvalg VIBS/SINTEF definerer.
- **Dataintegrasjonsarkitekturen:** NOBB som hovednøkkel, EPD-XML, FDV-data, GTIN-kobling — dette er teknisk arkitektur VIBS beskriver.
- **DNSH-tabellen:** Hvilke negative sideeffekter som er identifisert og avbøtende tiltak — dette er VIBS' metodiske ansvar.

### 1d. Hva må kildeverifiseres eksternt?

Se del 2 og 4 for fullstendig liste. Korte stikkord:
- [KD2024]: tidligfase/påvirkningsrom — primær-PDF fra regjeringen.no
- [GullbrekkenHolme2025]: fulltekst SINTEF (august)
- [An2020]: akseptert manus (Wiley fulltekst/OA), korrekt bruksområde avklare
- [Mecca2023]: Wiley betalingsmur — SINTEF henter
- [SA2018/2019]: primærrapport fra Samfunnsøkonomisk analyse må lokaliseres
- [EBA_NO2023]: PDF bør lagres av Lars Erik
- SMB-andel i byggenæringen: SSB primærtall hentes

---

## 2. Hva gjenstår før rent arbeidsutkast kan strammes

### 2a. Må kildeverifiseres (eksternt, av Lars Erik eller SINTEF)

| Kildehull | Hva som mangler | Prioritet | Kilde å åpne |
| --- | --- | --- | --- |
| [KD2024] — tidligfasens påvirkningsrom | Primær-PDF fra regjeringen.no, eller PDF fra DiBK/NHO Byggenæringen. Web-søk bekrefter at KDD-kunnskapsgrunnlaget (2024) eksisterer og dokumenterer at rammene for utslipp låses tidlig. Men ingen primær-URL er hentet og lagret. | Høy | regjeringen.no eller DiBK (plangrunnlag/klimatiltak bygg) |
| [EBA_NO2023] — 20% klimagassreduksjon uten merkostnad | Web-søk bekrefter: Veileder for klimagassreduksjoner: Boligblokker, EBA + Grønn Byggallianse, publisert 25. april 2023 (v1.1 jan. 2025). Åpent tilgjengelig på eba.no og byggalliansen.no. Lars Erik lagrer PDF og bekrefter 20%-tallet. | Middels | eba.no / byggalliansen.no |
| [GullbrekkenHolme2025] — byggfeil 10–30 mrd, halvparten av boliger | Web-søk bekrefter: kronikk av Lars Gullbrekken og Jonas Holme (SINTEF), august 2025, publisert på sintef.no. Tallene er verifisert sitert i kronikken. Primærkilde bak kronikken (intern SINTEF-rapport) må åpnes av SINTEF midten av august. | Middels | sintef.no (kronikk: umiddelbart); bak kronikken: SINTEF august |
| [An2020] — 34% lavere misligholdsrisiko for næringsbygg | DOI 10.1111/1540-6229.12228 bekreftet via web-søk (RepEC, ResearchGate). Tall er 34%, ikke ca.32%. Gjelder CMBS (næringsbygg), IKKE boliglån. Fulltekst er bak Wiley-betalingsmur. Akseptert manus bør søkes på SSRN/GoogleScholar. | Middels | SSRN / GoogleScholar / Wiley (SINTEF) |
| [Mecca2023] — MCDA-metodefordeling | Web-søk bekrefter: J. of Multi-Criteria Decision Analysis, DOI 10.1002/mcda.1818, metadata korrekt. Wiley-betalingsmur. SINTEF henter fulltekst. | Middels | Wiley (SINTEF august) |
| [SA2018/2019] — konfliktkostnad 2,2 mrd | Web-søk bekrefter: Samfunnsøkonomisk analyse, oppdrag for EBA, 2018. Rapporten omtales som Effektive prosjekter med lavere konfliktnivå (publisert 2019). Nøkkelen [SA2018] kan ha feil årstall. Primærrapporten er ikke funnet i åpent register. | Høy | Samfunnsøkonomisk analyse AS / EBA direkte |
| SMB-andel av norsk byggenæring | Web-søk bekrefter: SSB statistikkbank (tabell 07091 og 12939) har bedriftsandeler per størrelsesklasse for SN2007 F (bygg/anlegg). Eksakt primærtall for andel SMB er ikke hentet. EU-definisjon (under 50 ansatte) valgt, men norsk praksis bruker under 100. | Middels | ssb.no statistikkbank, tab. 07091 |

### 2b. Må besluttes av VIBS / Lars Gunnar

| Beslutningspunkt | Hva som må avklares |
| --- | --- |
| **SMB-definisjon i søknaden** | EU-def (under 50 ansatte) er valgt, men må stå konsekvent. Enten bruk EU-definisjon og oppgi det eksplisitt, eller bruk norsk under 100 og dokumenter norsk andel fra SSB. Bland dem ikke. |
| **Baseline for effektmåling (WP3)** | Hva er bestillingsalternativet i piloten? Hvilke KPI-er måles (tidsbruk, avvik, omarbeid, beslutningsendring, CO2 per enhet)? Hvem måler — SINTEF, VIBS, Buildington/Ordercontrol? |
| **Pilotopplegg for beslutningseffekt** | Før/etter på samme prosjekttype? A/B-opplegg med og uten score? Intervju etter beslutning? Design av dette er FoU-valg som må avgjøres med SINTEF. |
| **Bankavgrensning** | Hva er den konkrete rollen til Flekkefjord Sparebank i piloten? Hvilken bankbeslutning testes — bedre rente, enklere dokumentasjonskontroll, raskere innvilgelse? Uten dette er V3 (økonomi) svak. |
| **DNSH-tabell** | Søknaden mangler en eksplisitt do-not-harm-tabell (se sannhetsserum del 4). Bærekraft-sannhetsserumet lister 9 angrep. VIBS/Lars Gunnar må beslutte hvilke som adresseres i søknaden og med hvilke tiltak. |
| **WP1–WP5 struktur** | Gjennomføring-kriteriet er tomt. Lars Gunnar / Lars Erik må beslutte WP-inndeling, tidsplan og rollefordeling VIBS vs. SINTEF per WP. |
| **Sirkulærøkonomi-posisjon** | Utlysningen øremerker 40 MNOK til sirkulær økonomi (ombruk, reparasjon, deling). Skal VIBS søke inn under dette sporet? I så fall må reparasjon/vedlikehold og ombrukbarhet eksplisitt inn som VERIFIED-dimensjoner med målepunkter. |
| **Støttebeløp og støttegrad** | IPN-beløp: 1–16 MNOK, maks 50% av bedriftenes kostnader. Hva er VERIFIEDs planlagte totalbudsjett og NFR-andel? |

### 2c. Kan beskrives som FoU-opplegg (ingen ekstern kilde nødvendig)

- Vektingsmodellen (med begrunnelse for vektene som forskningshypoteser, ikke fakta)
- Datakvalitetsmodellen og pedigree-logikken (dokumentasjonstillit x delpoeng)
- Integrasjonsarkitekturen (NOBB-nøkkel, EPD-XML, FDV-data, GTIN-kobling)
- Pilotdesign: hvilke prosjekter, hvem er deltakere, hva er kontrollbetingelsen
- DNSH-tabellen (selve tabellen; de empiriske tallene den bygger på trenger kilde)
- FoU-hypotesen om kvalitet-finansiell risiko (hypotesen er eget FoU-bidrag; selve empirien kommer i prosjektet)

---

## 3. Forskningsrådets kriterier

### 3a. Kvalitet

**Krav:** Utfordre state of the art, solide metodevalg, modeller og antakelser.

| Element | Status i søknaden nå | Dom |
| --- | --- | --- |
| SoA-gapmatrisen (6 akser) | God. Eksisterende verktøy (One Click LCA, EC3, Reduzer) dekker karbon men ikke kombinasjonen. | Kan bære |
| MCDA-metodevalg | Mecca 2023 (AHP 46%, TOPSIS 20%) brukes som bakgrunn. Metodevurdering er til stede, men gul (fulltekst bak paywall). | Kan nevnes med forbehold |
| Vektingsmodell og usikkerhet | Modellen er beskrevet, men metodisk begrunnelse for vekter mangler. | Må utbedres |
| FoU-hullet: holdbarhet-PD | Klart formulert som ny, etterprøvbar hypotese. | Sterkt FoU-bidrag |
| Dataintegrasjonsmetode (pedigree) | Edelen 2018, Benke 2025, Lohman 2023 — alle grønne. Gir metodisk ryggdekning. | Kan bære |

**Konklusjon Kvalitet:** Sterkt fundament, men Solide metodevalg er svakt fordi vektingsmodellen mangler metodisk forankring (hvilken vektingsmetode, sensitivity analysis, validering).

### 3b. Virkninger og effekter

**Krav:** Sannsynlig samfunnsnytte, bidrag til bærekraftsmål, do-not-harm.

| SDG-spor | Status |
| --- | --- |
| **SDG 12.2 (ressurseffektivitet)** | Beste match. Materialvalg, levetid, vedlikehold og ombruk er kjernen i VERIFIED. |
| **SDG 12.5 (ombruk/avfall)** | Relevant hvis pilotene måler utsatt utskifting / spart materialmengde. Trenger eksplisitt målepunkt. |
| **SDG 9.4 (SMB-omstilling)** | Relevant hvis VIBS fremstilles som ny beslutningsinfrastruktur for bransjen, ikke bare én app. |
| **Do-not-harm** | DNSH-tabell mangler. Sannhetsserumet lister 9 angrep (Lav CO2 kan gi kortere levetid, AI-data kan gi grønnvasking m.fl.). Kritisk manko. |
| **Samfunnsnytte i tall** | Byggfeil 10–30 mrd (GullbrekkenHolme, gul), vannskader 5,1 mrd (FinansNorge, grønn), konflikter 2,2 mrd ([SA2018/2019], gul). Koblingen til VIBS-effekt er ikke bevist — det er FoU-hypotesen. |

**Konklusjon Virkninger:** Godkjent retning, men DNSH-tabellen er en showstopper. En IPN-fagfelle vil si: Bærekraftsbidrag uten do-not-harm er ikke godkjent under Virkninger.

### 3c. Gjennomføring

**Krav:** Realistiske arbeidspakker, troverdige planer, relevante risikovurderinger.

| Element | Status |
| --- | --- |
| WP1–WP5 | Ikke skrevet. Nevnt i arbeidsplan, men innhold mangler. |
| Tidsplan | Ikke skrevet. |
| Rollefordeling VIBS / SINTEF | Delvis skissert, men ikke i søknadstekst. |
| Pilotopplegg (WP3) | Omtalt, men baseline og måleopplegg er ikke definert. |
| SINTEF som FoU-part | Nødvendig for FoU-tyngde. Nevnes, men ikke eksplisitt rolleavklart per WP. |

**Konklusjon Gjennomføring:** Tomt felt. Kritisk. Ingen plan kan godkjennes.

### 3d. Bærekraft / do-not-harm

Jf. sannhetsserum del 4 og par. 3b ovenfor. Må ha én eksplisitt DNSH-tabell i søknaden med:
- risikohendelse
- sannsynlighet
- avbøtende tiltak
- ansvarlig part
- målepunkt

### 3e. Støttebeløp, støttesats og formalkrav

Fra NFR_IPN2026 (grønn primærkilde):
- Støttebeløp: NOK 1 000 000 – 16 000 000 per prosjekt
- Maks støttesats: 50% av bedriftenes kostnader
- Prosjektbeskrivelse: PDF på maks 10 sider (eget mal)
- Søknaden skal ikke lenke til nettsider — kilder skrives som korte referanser i teksten

> Advarsel: Ingen av disse rammevilkårene er brutt i nåværende utkast, men støttebeløp og -sats er ikke eksplisitt nevnt i K/V-tekstene. Bør inn i en innledning eller i gjennomføringsdelen.

---

## 4. Kildekritisk gjennomgang av dagens hovedpåstander

| Nr | Påstand | Nåværende kilde | Status | Kan bære søknadstekst nå? | Anbefalt formuleringstype |
| --- | --- | --- | --- | --- | --- |
| P1 | Tidlige beslutninger låser rammene for utslipp, men påvirkningsrommet er størst i tidligfase | [KD2024] | Gul: primær ikke hentet | Nei | Ut av prosa inntil primær er åpnet; kan først senere brukes som kildebelagt bakgrunn |
| P2 | Tidlige materialvalg kan redusere klimagassutslipp med opptil 20% uten merkostnad | [EBA_NO2023] | Åpen PDF lest; boligblokk-kontekst | Nei som generell påstand | Må tones ned til veilederens kontekst og avstemmes mot kanonisk status |
| P3 | Utbedring av byggfeil koster 10–30 mrd NOK/år. Halvparten av boliger har minst én feil | [GullbrekkenHolme2025] | Gul: kronikk bekreftet på sintef.no; primærrapport åpnes august | Ja, med forbehold | Kan stå med formulering som reflekterer kilde (kronikk/analyse, ikke vitenskapelig artikkel) |
| P4 | 34% lavere misligholdsrisiko for næringsbygg med LEED/Energy Star | [An2020] | Gul: DOI bekreftet; fulltekst bak paywall; gjelder CMBS — IKKE boliglån | Nei — bruk kun for næringsbygg | Må tones ned og flyttes til næringsbygg-kontekst |
| P5 | 32% lavere misligholdsrisiko for boliglån med ENERGY STAR-sertifisering | [Kaza2014] | Grønn | Ja | Kan stå |
| P6 | Energieffektivitet henger sammen med lavere misligholdsrisiko for boliglån i Nederland | [Billio2022] | Grønn | Ja | Kan stå |
| P7 | Konflikter koster 2,2 mrd NOK/år | [SA2018] | Gul: primærrapport ikke lokalisert; nøkkelår kan være 2019 | Nei | Ut av prosa inntil primærrapport og årstall er kontrollert |
| P8 | 10 vannskader per time, 5,1 mrd NOK/år i erstatninger (2023) | [FinansNorge2024VASK] | Grønn | Ja | Kan stå |
| P9 | AHP er mest brukt MCDA-metode (46%), TOPSIS nest mest (20%) | [Mecca2023] | Gul: metadata bekreftet; fulltekst bak Wiley-paywall | Nei (ennå) | Kan stå som FoU-bakgrunn med forbehold inntil fulltekst åpnes |
| P10 | LCA-krav og verktøyadopsjon er vesentlig svakere for SMB | [Nordic2023] | Grønn | Ja | Kan stå |
| P11 | 1 583 konkurser i bygg og anlegg i 2025 | [Bjørheim2026] | Gul: bransjeblad/kredittratingdata | Ja, med forbehold | Kan stå med en tydelig indikasjon-formulering |
| P12 | Driftsmargin 3,3% i 2024 | [BDO2025] | Gul: BDO-rapport, ikke fagfellevurdert | Ja, med forbehold | Kan stå med ifølge BDO-formulering |
| P13 | 18 000 kr/m2 dyrere å bygge enn Sverige | [UNION2025] | Gul: UNION Gruppen, ikke primærkilde | Ja, med forbehold | Kan stå med bransjeanslaget-formulering |

**[G4-sjekk — kjørt]:** Påstand P4 ble sendt til Gemma4 med spørsmål: Er det konsistent å bruke An & Pivo 2020 (som gjelder CMBS/næringsbygg) som bevis for at energieffektivitet reduserer misligholdsrisiko i boliglån? Gemma4-svar: NEI, det er ikke konsistent. CMBS-studier gjelder kommersielle eiendommer. Overføringen til boliglån krever en separat kilde. Dom bekreftet av kildedom.

---

## 5. Målrettet åpne kildesøk — resultater

### 5a. SMB-definisjon og andel av norsk byggenæring

**Søk utført:** SSB, NHO, EU-definisjon for SMB i norsk byggenæring

**Funn:**
- EU-definisjon (under 50 ansatte, omsetning under 10 MEUR) er offisiell norsk-statlig i statsstøttesammenheng (Enova, SIVA) og tilsvarer IPN-rammen.
- Norsk praksis (NHO, SSB): under 100 ansatte brukes i NHO-statistikk.
- SSB statistikkbank: Tabell 07091 (Bedrifter etter størrelse og næring) gir fordeling per størrelsesklasse for SN2007 F (bygg/anlegg). Primærtall ikke hentet i denne kjøringen.
- Byggenæringen er bekreftet dominert av bedrifter under 50 ansatte (SSB-struktur bekreftet via søk).

**Anbefaling:**
- Bruk EU-definisjon (under 50 ansatte) og oppgi det eksplisitt. Dette harmonerer med statsstøtteregelverket IPN faller under.
- Lars Erik: hent eksakt andel fra SSB tabell 07091 for SN2007 F, siste tilgjengelige år.
- Forslag til ny kilde: SSB Strukturstatistikk for bygge- og anleggsvirksomhet (tab. 12939) — foreslått status: grønn etter at primærtall er hentet.

### 5b. [KD2024] — tidligfase/påvirkningsrom

**Funn:**
- Søket bekrefter at KDD, DiBK og NHO Byggenæringen har utarbeidet et kunnskapsgrunnlag (2024) som dokumenterer at beslutninger i tidligfase låser rammene for klimaeffekt.
- Nøkkelformulering bekreftet: påvirkningsrommet for utslippsreduksjon er størst i de tidligste fasene.
- Ingen direkte URL til PDF-primæren ble funnet i denne kjøringen.

**Anbefaling:**
- Lars Erik søker på regjeringen.no etter klimatiltak byggenæringen 2024 eller klimaplan bygg KDD DiBK. PDF-en bør lagres lokalt.
- Alternativt: DiBK.no har veiledere og kunnskapsgrunnlag; søk klimagassutslipp nybygg tidligfase 2024.
- Inntil primær-PDF er lagret: formuler som [...] viser at påvirkningsrommet er størst i tidligfase (Kommunal- og distriktsdepartementet mfl. 2024; primærkilde åpnes).

### 5c. [EBA_NO2023] — 20% klimagassreduksjon

**Funn:**
- Veilederen er bekreftet: Veileder for klimagassreduksjoner: Boligblokker, EBA + Grønn Byggallianse + Norsk Eiendom, publisert 25. april 2023 (v1.1 jan. 2025).
- URL: eba.no og byggalliansen.no (åpent tilgjengelig).
- Tall bekreftet: minst 20% reduksjon i klimagassutslipp fra materialvalg uten merkostnad.
- Grønn Byggallianse strakstiltak nr. 19 i Eiendomssektorens veikart mot 2050 bekrefter.

**Anbefaling:**
- Lars Erik: last ned og lagre PDF fra eba.no eller byggalliansen.no. Etter det: oppgrader [EBA_NO2023] til grønn.
- Foreslått ny formulering i søknaden: Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 prosent uten at prosjektkostnaden øker (Entreprenørforeningen – Bygg og Anlegg, Grønn Byggallianse og Norsk Eiendom 2023).

### 5d. [GullbrekkenHolme2025] — byggfeil 10–30 mrd, halvparten av boliger

**Funn:**
- Bekreftet: kronikk og debattinnlegg av Lars Gullbrekken (SINTEF forskningsleder) og Jonas Holme (SINTEF forskningsdirektør), publisert august 2025 på sintef.no.
- Tall bekreftet sitert: 10–30 mrd NOK/år, over halvparten av boliger oppført 2010–2020 har minst én byggfeil.
- Kronikken er SINTEF-publisert, men er ikke en fagfellevurdert artikkel — det er en kronikk/analyse.

**Anbefaling:**
- Kronikken er tilstrekkelig som kildenivå for problemdokumentasjon. Kan brukes nå med formulering: SINTEF-forskerne Gullbrekken og Holme (2025) anslår at...
- Primærkilde bak kronikken (internt SINTEF-materiale) hentes av SINTEF i august.
- Oppgrader til grønn etter at SINTEF bekrefter primærkilde.

### 5e. [Mecca2023] — MCDA-metodefordeling

**Funn:**
- Bekreftet: Mecca, B. (2023). Journal of Multi-Criteria Decision Analysis, 30(5–6), 203–218. DOI bekreftet (10.1002/mcda.1818).
- Artikkelen finnes i universitetsdatabaser (vu.lt, icm.edu.pl, tuni.fi), men ikke i åpent fulltekst.
- Wiley-betalingsmur bekreftet.

**Anbefaling:**
- Metadatastatusen er nå bekreftet. Status forblir gul inntil SINTEF henter fulltekst.
- Kan brukes i bakgrunnsformuleringer: systematiske gjennomganger viser at AHP er den mest brukte MCDA-metoden (Mecca 2023) — med forbehold om at fulltekst er bak betalingsmur.

### 5f. [An2020] — 34% lavere PD for næringsbygg

**Funn:**
- Bekreftet: An, X. & Pivo, G. (2020). Real Estate Economics, 48(1), 7–42. DOI: 10.1111/1540-6229.12228.
- Tall bekreftet: 34% lavere misligholdsrisiko (ikke ca.32%).
- Gjelder CMBS (Commercial Mortgage-Backed Securities) — næringsbygg, ikke boliglån.

**Kritisk merknad:** Dersom [An2020] er brukt i søknadstekst for å støtte påstander om boliglån, er det en feil. Bruk:
- [Kaza2014] grønn for boliglån (ENERGY STAR, residensielt)
- [Billio2022] grønn for boliglån (Nederland, EPC)
- [An2020] kun for næringsbygg/CMBS

### 5g. [SA2018/2019] — konfliktkostnad 2,2 mrd

**Funn:**
- Bekreftet: Samfunnsøkonomisk analyse AS utarbeidet rapporten på oppdrag av EBA og bransjeorganisasjoner (Nelfo, Rørentreprenørene mfl.).
- Rapporten omtales som Effektive prosjekter med lavere konfliktnivå, trolig publisert 2019 (ikke 2018).
- Kilden bekreftet sitert med 2,2 mrd NOK/år konfliktkostnad.
- Primærrapporten er ikke funnet i åpent register (Google Scholar, Cristin, Samfunnsøkonomisk analyse AS' nettside).

**Anbefaling:**
- Kontakt EBA direkte for PDF av rapporten.
- Sjekk om nøkkelåret er 2018 eller 2019 — nøkkelen bør mulig rettes til [SA2019].
- Status forblir gul inntil primærrapporten er lokalisert og lagret.

### 5h. SMB-atferd i tilbudsfasen

Ikke ferdig undersøkt. Nordic Council 2023 ([Nordic2023], grønn) dekker bare deler av spørsmålet. Det trengs en egen åpen primærkilde om hvordan små entreprenører faktisk bruker LCA/EPD- og beslutningsverktøy i tilbudsfasen. Ikke presenter dette som dokumentert markedseffekt.

### 5i. Effektmåling i pilot

Selve baseline-designen er et VIBS/SINTEF-valg, men beste praksis for før/etter, alternativ/A-B, tidsbruk, beslutningsendring og avvik må kildeundersøkes før metoden beskrives som etablert. Inntil da skal teksten kalle dette planlagt FoU-design.

---

## 6. Nye relevante kilder som bør vurderes

| Tittel | Utgiver | URL/tilgang | Hva den kan støtte | Foreslått status |
| --- | --- | --- | --- | --- |
| Veileder for klimagassreduksjoner: Boligblokker (v1.0, 25.04.2023) | EBA + Grønn Byggallianse | [Åpen PDF](https://www.eba.no/siteassets/dokumenter/rapporter-og-publikasjoner/klima--veiledere/veileder-klimagassreduksjoner-boligblokk.pdf) | Mulighetsrom rundt 20% i boligblokk-veilederens kontekst | Gul inntil kanonisk port er avstemt |
| SSB Strukturstatistikk bygge- og anleggsvirksomhet | Statistisk sentralbyrå | [Tabell 07091](https://www.ssb.no/en/statbank/table/07091) | SMB-andel av byggenæringen, primærtall | Ikke verifisert i denne runden |
| Byggskader – det glemte pengesluket | Lars Gullbrekken & Jonas Holme, SINTEF | [SINTEF-kronikk](https://www.sintef.no/siste-nytt/2025/byggskader-det-glemte-pengesluket/) | Problemdokumentasjon: 10–30 mrd NOK/år | Gul; kronikk er ikke underliggende primærstudie |
| Effektive prosjekter med lavere konfliktnivå | Samfunnsøkonomisk analyse AS, for EBA | Primær-URL ikke lokalisert | Konfliktkostnad 2,2 mrd NOK/år | ⏸ Ikke bruk |
| DiBK/KDD klimakunnskapsgrunnlag 2024 | Direktoratet for byggkvalitet / KDD / NHO Byggenæringen | Primær-URL ikke lokalisert | Tidligfasens påvirkningsrom for klimagassreduksjon | Gul; ikke bruk bærende |
| The Operating Environment of Building LCA and BIM in the Nordics and Estonia (2023) | Nordic Council of Ministers / Nordic Sustainable Construction | nordicsustainableconstruction.com | LCA-adopsjon i Norden, SMB-tilpasning, BIM4LCA | Grønn (allerede i kildebibliotek som [Nordic2023]) |

---

## 6b. Oppdatert kandidatliste etter siste kildepass

Dette er den korte listen for neste kildepass. Resten under er støtte, ikke første prioritet.

1. `[KD2024]`
   - Hva den skal bevise: at tidligfase faktisk låser utslipp, og at påvirkningsrommet er størst tidlig.
   - Hvorfor nå: den påvirker bakgrunnssetningen direkte.
   - Status: gul; primær-PDF må åpnes.

2. `[SSB 07091/12939]`
   - Hva den skal bevise: SMB-andel og næringsstruktur i bygg/anlegg.
   - Hvorfor nå: vi trenger et norsk tallgrunnlag, ikke bare EU-definisjon.
   - Status: gul; tall må hentes direkte.

3. `[EBA_NO2023]`
   - Hva den skal bevise: 20 %-påstanden og boligblokk-konteksten.
   - Hvorfor nå: den brukes allerede som mulig virkningsstøtte og må være presis.
   - Status: gul til kanonisk port er avstemt.

4. `[GullbrekkenHolme2025]`
   - Hva den skal bevise: skadeomfanget bak problembeskrivelsen.
   - Hvorfor nå: den kan gi en mer norsk og tydelig problemåpning.
   - Status: gul; kronikk/analyse, ikke primærstudie.

5. `[Mecca2023]`
   - Hva den skal bevise: metodefordeling i MCDA, hvis vi trenger det i hovedteksten.
   - Hvorfor nå: bare hvis vi vil underbygge metodevalg litt sterkere.
   - Status: gul; kun metodebakgrunn.

6. `[NOBB]` og `[EPD-Norge]`
   - Hva de skal bevise: norsk datainfrastruktur og koblingspunkt.
   - Hvorfor nå: disse er nyttige hvis vi vil stramme bakgrunn og metode, men de er ikke bærende før vi har direkte kilder.
   - Status: gul; bør få direkte offisiell kilde.

7. `[OneClickLCA]`
   - Hva den skal bevise: markedets integrasjon av LCA/EPD/LCC som sammenligningspunkt.
   - Hvorfor nå: bare hvis vi trenger et kort state-of-the-art-kontrastpunkt.
   - Status: gul; sammenligningspunkt, ikke bærende bevis.

8. `[Benke2025]`, `[Lohman2023]`, `[EC3]`, `[Weidema1996]` og `[Ciroth2016]`
   - Hva de skal bevise: metodisk ryggrad for usikkerhet, vekting og sammenlignbarhet.
   - Hvorfor nå: de er allerede kortlagt godt nok til å støtte hovedsporet; ytterligere lesing er bare nødvendig hvis vi skal stramme metodeavsnittet ytterligere.
   - Status: allerede i bruk i research-syntesen.

## 7. Anbefaling til neste skrivepass (Codex/Claude)

### 7a. Hva kan strammes nå — uten ny kildeåpning

1. **K1 (Bakgrunn):** Vannskader og GullbrekkenHolme kan brukes nå med riktige forbehold. Konkurstall og driftsmargin kan stå med ifølge BDO/ifølge Bjørheim. Fjern eller ton ned 18 000 kr/m2 til bransjeanslaget.
2. **K2 (Nyhetsverdi):** Seks-aksetabellen er sterk. [Nordic2023], [Billio2022], [Kaza2014], [Benke2025], [Lohman2023] og sentrale EU-standarder kan brukes direkte. [Mecca2023] kan nevnes med forbehold.
3. **V1 (Bærekraft):** SDG 12.2 og 12.5-satsningen kan skrives klart. Merk: DNSH-tabell MANGLER — det er et stopp-punkt som Codex ikke kan løse uten VIBS-beslutning (se 2b).
4. **V2 (Sikkerhet/do-not-harm):** Ikke skriv uten DNSH-tabell fra Lars Gunnar.
5. **V3 (Økonomi):** Grønn finans-argumentet holder for [Billio2022]/[Kaza2014] (boliglån) og [An2020] (næringsbygg, hvis brukt riktig). Bankavgrensningen mangler — ikke stram V3 uten Lars Gunnar-beslutning.
6. **K3 (Forskning) og K4 (Metode):** Vektingsmodell og pedigree-logikk kan skrives som FoU-opplegg uten ekstern kilde. Men metodisk begrunnelse for vektene mangler.

### 7b. Stopp-punkter — ikke stram disse uten videre avklaring

| Stopp-punkt | Årsak |
| --- | --- |
| WP1–WP5 og tidsplan | Tomt. Gjennomføring-kriteriet er ikke mulig å skrive. |
| DNSH-tabell | Mangler. Bærekraft-kriteriet er ikke søknadsklart. |
| Baseline for WP3 (effektmåling) | Mangler. Gjennomføring og Virkninger-kriteriet er svake. |
| Bankavgrensning | Mangler. V3 er ikke skrivebar uten dette. |
| [KD2024] primær-PDF | Ikke lagret. P1-påstanden bør ikke bæres alene i søknadstekst. |
| [SA2018/2019] primærrapport | Ikke lokalisert. P7-påstanden bæres ikke sikkert. |

### 7c. Instruksjon til Codex/Claude for neste pass

Når Lars Erik gir klarsignal: Bruk dette arbeidsdokumentets kildestatus-tabell (del 4) som styringsdokument. Skriv kun i de kapitlene der stopp-punktene er løst. Bruk formuleringstypene fra del 4 (kan stå / kan stå med forbehold / kan stå som FoU-hypotese) nøyaktig. Ikke overclaim effekt. Formuler VERIFIED som et prosjekt som skal teste og måle — ikke som om effekten allerede er bevist. Ingen lenker til nettsider i søknadsteksten.

---

## Vedlegg: Gemma4-kvalitetssjekkrunder utført i denne kjøringen

| Runde | Påstand sendt til Gemma4 | Gemma4-svar (kortversjon) | Brukt i dokumentet |
| --- | --- | --- | --- |
| G4-test (kalibrering) | Er utsagnet konsistent: EBA_NO2023 = EBA Norge, EBA_EU2023 = European Banking Authority? | NEI — to ulike EBA-er, ikke konsistent å kalle dem begge EBA uten distinksjon | Bekrefter kildekollisjon; skillet er korrekt dokumentert i kildebibliotek |
| G4-P4 | Er det konsistent å bruke An & Pivo 2020 (CMBS/næringsbygg) som bevis for boliglåns-misligholdsrisiko? | NEI — CMBS er næringsbygg, overføring til boliglån krever separat kilde | Bekreftet: P4-anbefaling Må tones ned / flyttes til næringsbygg-kontekst |

---

Dokument opprettet: 2026-07-10 av AGY (Antigravity / Claude Sonnet 4.6 Thinking) med Gemma4:latest kvalitetssjekkrunder. v0.2 QA-justert av Codex 2026-07-10. Gemma4 er kun intern konsistenssjekk, ikke kildebelegg.
Kanoniske kildestatusfiler (ipn-kildebibliotek.md, vibs-verified-kildedom-2026-06-27.md) er lest men ikke endret.
