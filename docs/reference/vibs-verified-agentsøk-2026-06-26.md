# VIBS VERIFIED — Agentsøk og statusrapport
**Dato:** 2026-06-26 · **Utarbeidet av:** Claude (Anthropic) · **Grunnlag:** tre interne referansedokumenter + 8 websøk
**Formål:** Lukke hull fra aksjonslisten (2026-06-22) og SotA-dokumentet (v0.2, 2026-06-21) før videre arbeid med IPN-søknaden.

---

## Del 1 — Statussammendrag

### Hva er VIBS VERIFIED?

VIBS VERIFIED er et IPN-søknadsprosjekt (Innovasjonsprosjekt i næringslivet, Forskningsrådet) med formål å utvikle en **forklarbar, etterprøvbar flerkriterie-beslutningsmodell** for SMB-entreprenører og boligkjøpere i tilbudsfasen. Modellen kombinerer LCA, LCC, EPD, FDV, levetid, kvalitet, skaderisiko, vedlikehold og ombruk til én transparent score der datakvalitet er synlig — ikke skjult i et enkelt tall.

Kjernehypotesen er todelt: **(1) atferdshypotesen** — at en forklarbar, kontekstuell score faktisk endrer materialvalg hos SMB og boligkjøpere (empirisk udokumentert i norsk kontekst); og **(2) finanshypotesen** — at byggteknisk kvalitet og holdbarhet korrelerer med lavere misligholdsrisiko (PD/LGD) på boliglån, et gap ingen studie har dekket. Metoden kombinerer litteraturstudie, dataintegrering, MCDA-utvikling, brukertesting og effektmåling i reelle pilotprosjekter.

FoU-høyden ligger **ikke** i enkeltkomponentene (som er modne), men i syntesen: at kombinasjonen av de seks aksene (dataintegrasjon, tilbudsfase, SMB-brukergruppe, synlig usikkerhet, beslutningseffekt, DNSH-bredde) ikke finnes i noe eksisterende verktøy eller metode.

### Hva mangler / gjenstår (per aksjonsliste 2026-06-22)?

**SINTEF eier primærverifisering:**
- **F4** — Faktasjekke «byggenæringen er Norges største fastlandsnæring / minst digitaliserte / mest fragmenterte». Websøk (se Del 2 S5) bekrefter kjernetallet («57 000 bedrifter, 235 000 ansatte, ~500 mrd omsetning, lav digitalisering»), men kilde er ikke finkornet nok for søknadssitering — SINTEF bør hente SSB-statistikk direkte.
- **F5** — Avklare hva Harerusten 2022 (2,2 mrd/år) faktisk teller (rettssaker, konflikter, reklamasjoner).
- **F10** — Verifisere «metodene for å veie kriterier er veletablerte (Mecca 2023)». Mecca er fortsatt bak betalingsmur (402); ResearchGate-PDF anbefalt.
- **F12a** — Primærverifisere Mecca 2023.
- **F13** — Kvalitetssikre WP1–WP5 og «rødt punkt» om WP3-baseline.
- **F14** — Primærverifisere Wiik 2025 (SINTEF Notat nr. 57): «opptil 20 prosent uten merkostnad».
- **F15** — Billio et al.-referansen er nå fullstendig (se Del 2 S4). Gjenstår: sikre at forfatterne er korrekt nevnt i teksten og at referansen er koblet til riktig publisert artikkel (JREFE 2022, ikke WP 261).

**VIBS-teamet eier innholdsbeslutninger:**
- **F1** — Definere SMB presist etter antall ansatte og andel av næringen (tall finnes i SSB/NHO).
- **F8** — Strategisk avklaring: hvilke påstander er åpne hypoteser vs. etablert kunnskap. Avgjørende for formuleringer i hele søknaden.
- **F11c** — Omformulering: SMB-entreprenører er fagfolk, ikke ikke-spesialister.

**Lars Gunnar eier:**
- **F12b** — Definere konkrete måleparametere for beslutningseffekt (atferdsforskningsdelen).

**Allerede løst i v0.2 (2026-06-26):**
F2 (marginer), F3 (programvare), F7 (myket opp «alt finnes»), F9 (DPP-term), F11a (dataintegrasjonslisten), F11e (beslutningseffekt omformulert), F11f (vedlikehold inn), F12b (mellomformulering lagt inn), F16 (sosiale minstekrav, avventer Lars Eriks bekreftelse).

### Faktapåstander i SotA-dokumentet som fortsatt er hull eller usikre

| Påstand | Status | Hva gjenstår |
| --- | --- | --- |
| Holdbarhet/kvalitet → lavere PD/LGD | **HULL [bekreftet]** | Ingen studie dekker dette. Er selve FoU-argumentet. |
| Mecca 2023: AHP 46 % / TOPSIS 20 % osv. | [H*] — primær ikke åpnet | SINTEF åpner via institusjonstilgang |
| Wiik 2025: «opptil 20 %» uten merkostnad | [🟡] — ikke primærverifisert | SINTEF åpner SINTEF Notat nr. 57 |
| Bank of England PS25/25 | [H*] — primær 403 | Substans bekreftet via Green Central Banking |
| Bank of England DP1/25 | [M] — via søkesammendrag | SINTEF/Lars åpner via BoE-nettsted |
| Omnibus I (vedtatt 24.02.2026) | [H*] — primær EUR-Lex ikke åpnet | Pinn mot OJ/EUR-Lex |
| Norsk/nordisk WLC-benchmark | [L] — kun søketreff | SINTEF søker aktivt |
| Byggskadeomfang SINTEF (5 %/¾ fukt) | [M] — data fra 2008, primær PDF død | Oppdaterte tall fra Gullbrekken/Holme 2025 |

---

## Del 2 — Søkeresultater med vurdering

### S1 — Norske banker og bygningskvalitet i kredittmodeller
**Søkt:** «Norwegian banks mortgage credit risk building quality durability PD LGD model 2024 2025»

**Funn:** Ingen norsk bank har publisert kredittmodell som inkluderer bygningskvalitet eller holdbarhet som variabel. Nordeas Capital and Risk Management Report 2025 og Norges Banks Financial Stability Report 2025-2 omhandler LTV, disponibel inntekt og CRE-eksponering — ikke bygningsfysisk tilstand. Finanstilsynets Risk Outlook (des. 2025) fokuserer på makroøkonomiske faktorer og kommersiell eiendom.

**Vurdering:** **Styrker FoU-argumentet sterkt.** Bekrefter at norske banker ikke har operasjonalisert holdbarhet/kvalitet i kredittmodeller. Kombinert med DP1/25 (PRA, 2025) som viser at mellomstore banker mangler IRB-modellkapasitet, peker dette mot et reelt markedsvindu.

**Relevante lenker:**
- [Norges Bank Financial Stability 2025-2](https://www.norges-bank.no/en/news-events/publications/Financial-Stability-report/2025-2/web-report-2025-2-financial-stability/)
- [Finanstilsynet Risk Outlook des. 2025](https://www.finanstilsynet.no/en/publications/risk-outlook-reports/risk-outlook--december-2025/html/2025/)

---

### S2 — NFR IPN-krav og rammer 2025/2026
**Søkt:** «NFR IPN Innovasjonsprosjekt næringslivet krav budsjett FoU-andel 2025 2026 søknad»

**Funn:** 2026-utlysningen (industri og tjenestenæringer) ble publisert 18. desember 2025. Sentrale krav:
- Maks støttegrad: **50 % av selskapenes kostnader**
- Maks støttebeløp: **16–20 mill. kr** (avhengig av temaområde)
- Prosjektvarighet: **min. 2 år, maks 4 år**
- Krav om **minst én samarbeidspartner** (bedrift) eller kjøp av FoU-tjenester fra minst én FoU-leverandør
- Tidligst prosjektstart: 15. april 2026; senest: 15. april 2027

**Vurdering:** VIBS VERIFIED er i korrekt løp. SINTEF som FoU-partner oppfyller partnervilkåret. Budsjettrammen på 16–20 mill. kr setter konkret tak for WP-budsjettering. Kravet om «vesentlig innslag av industriell forskning (IF) og/eller eksperimentell utvikling (EU)» stiller krav til at FoU-innholdet er tydelig skilt fra produktutvikling i søknaden.

**Relevante lenker:**
- [IPN 2026: Industri og tjenestenæringer](https://www.forskningsradet.no/utlysninger/2026/innovasjonsprosjekt-naringslivet-industri-og-tjenestenaringer/)
- [IPN generell side](https://www.forskningsradet.no/finansiering/naringsliv/innovasjonsprosjekt-i-naringslivet/)

---

### S3 — Nyere studier: bygningsfysisk tilstand → PD/LGD
**Søkt:** «building physical condition durability mortgage default probability study 2023 2024 2025»

**Funn:** Systematisk review av default-prediction-modeller (2015–2024) publisert i PMC (nov. 2024) viser at klimarisiko og eiendomsverdi er inkludert i noen modeller, men **bygningsfysisk kondisjon, holdbarhet og vedlikeholdssvikt er ikke representert som variabler**. PRA DP1/25 bekrefter at mellomstore banker mangler IRB-modellkapasitet for PD/LGD — noe som speiler SMB-skranken VERIFIED adresserer. Ingen av søkeresultatene inneholder studier som kobler bygningskvalitet direkte til misligholdsrisiko.

**Vurdering:** **Styrker FoU-hullet meget sterkt.** Litteraturen frem til 2025 mangler koblingen holdbarhet→PD. Dette bekrefter at påstanden i SotA §7 er korrekt og at forskningshullet er reelt og siterbart. Det anbefales å supplere med et eksplisitt søk i Web of Science/Scopus via SINTEF for å sikre at ingen nyere studie er oversett i fagfellevurderte journaler.

**Relevante lenker:**
- [BoE DP1/25 – PD og LGD for boliglån](https://www.bankofengland.co.uk/prudential-regulation/publication/2025/july/residential-mortgages-loss-given-default-and-probability-of-default-estimation-discussion-paper)
- [PMC: Systematic review of default prediction](https://pmc.ncbi.nlm.nih.gov/articles/PMC11564005/)

---

### S4 — Billio et al. — fullstendig referanse (F15)
**Søkt:** «Billio Costola Pelizzon Riedel buildings energy efficiency mortgage default Dutch SAFE working paper»

**Funn:** Fullstendig referanse er nå identifisert og bekreftet:

> Billio, M., Costola, M., Pelizzon, L., & Riedel, M. (2022). «Buildings' energy efficiency and the probability of mortgage default: The Dutch case». *Journal of Real Estate Finance and Economics*, **65**(3), 419–450. https://doi.org/10.1007/s11146-021-09838-0

Opprinnelig SAFE Working Paper No. 261 (2020), publisert i journal 2022. Studien kombinerer nederlandske lånenivå-data med energiklassifisering fra RVO (Netherlands Enterprise Agency). Metode: logit-regresjon og utvidet Cox-modell. Tre mekanismer identifisert: (i) låntagerprofil, (ii) energisparing → disponibel inntekt, (iii) boligverdi → lavere LTV.

**Vurdering:** **Lukker F15** — referansen er nå fullstendig og kan brukes i søknaden. Viktig presisering: studien gjelder **energieffektivitet** (EPC-klasse), IKKE holdbarhet eller bygningskvalitet. Dette understøtter snarere enn svekker FoU-hullet: selv den sterkeste finansstudien stopper ved energi og går ikke til holdbarhet.

**Relevante lenker:**
- [Billio et al. 2022 – Springer](https://link.springer.com/article/10.1007/s11146-021-09838-0)
- [SAFE WP 261 – IDEAS/RePeC](https://ideas.repec.org/p/zbw/safewp/261.html)

---

### S5 — Byggenæringen som Norges største fastlandsnæring (F4)
**Søkt:** «byggenæringen Norges største fastlandsnæring digitalisering SSB 2024 2025»

**Funn:** Påstanden bekreftes i åpne sekundærkilder:
- «Bygg-, anlegg-, og eiendomsbransjen er Norges største fastlandsnæring med 57 000 bedrifter og 235 000 ansatte. Den samlede årlige omsetningen nærmer seg 500 milliarder kroner.» (Digital Norway / Construction City-kilde)
- SSB: bransjen står for ~15 % av CO₂-utslipp, 40 % av materialforbruk, 25 % av alt avfall
- Digitalnorway.com bekrefter at bransjen «ligger langt bak andre bransjer når det kommer til digitalisering»
- DiBK er nå med i Digital Norway-klyngen, noe som bekrefter at lav digitalisering er politisk anerkjent

**Vurdering:** **Delvis lukker F4.** Kjernetallene for «størst fastlandsnæring» og «lav digitalisering» er tilgjengelige i åpne kanaler. Kilden er imidlertid sekundær (Digital Norway, Construction City). For søknadsbruk bør SINTEF hente SSB-data direkte (SSB Bygg og anlegg, statistikk tabell). Leddet «mest fragmentert» er ikke eksplisitt dokumentert i søkeresultatene og bør verifiseres separat (antall aktører per omsetning er en mulig proxy).

**Relevante lenker:**
- [Construction City / DiBK Digital Norway](https://digitalnorway.com/aktuelt/direktoratet-for-byggkvalitet-inn-i-digital-norway)
- [SSB Kredittindikator](https://www.ssb.no/en/bank-og-finansmarked/finansielle-indikatorer/statistikk/kredittindikator)

---

### S6 — EU Mortgage Credit Directive og ESG/grønne boliglån
**Søkt:** «EU Mortgage Credit Directive ESG green mortgage building sustainability 2024 2025 revision»

**Funn:**
- EPBD (Energy Performance of Buildings Directive) ble revidert i mai 2024 med Minimum Energy Performance Standards
- EBA anbefaler integrering av EPC-klasse i MCD, og at finansielle insentiver (rabatterte renter, høyere LTV) knyttes til grønne egenskaper
- EU Taxonomy: grønne boliglån krever EPC-klasse A eller topp 15 % energieffektivitet — rent energifokus
- FSUG (Financial Services User Group) la inn forslag til revisjon av MCD i mars 2025
- Finance Watch rapporterer om pågående MCD-revisjonsprosess i EU-mandatperioden 2024–2029
- Full EBA-rapport om grønne lån og boliglån (des. 2023) er tilgjengelig som PDF fra EBA.

**Vurdering:** Bekrefter at **hele det grønne finansapparatet i EU er energisentrert** (kWh, EPC-klasse). Ingen plass i MCD-revisjon eller EU Taxonomy berører holdbarhet, fuktrobusthet, vedlikehold eller levetidskvalitet som kredittvariabel. Dette er presist det FoU-hullet VERIFIED adresserer, og det styrker posisjonering som «det neste steget etter energi».

**Relevante lenker:**
- [EBA Report on Green Loans and Mortgages (PDF)](https://www.eba.europa.eu/sites/default/files/2023-12/e7bcc22e-7fc2-4ca9-b50d-b6e922f99513/EBA%20report%20on%20green%20loans%20and%20mortgages_0.pdf)
- [Finance Watch: Revised MCD](https://www.finance-watch.org/policy-portal/retail-inclusion/a-revised-mortgage-credit-directive/)
- [FSUG forslag til MCD-revisjon (PDF)](https://finance.ec.europa.eu/document/download/933fc73e-f4a3-472d-8f88-207f45e496de_en?filename=fsug-opinions-250327-review-mortgage-credit-directive_en.pdf)

---

### S7 — Finans Norge og fysisk klimarisiko i norske banker
**Søkt:** «Finans Norge boliglånsmodell bygningskvalitet klimarisiko fysisk risiko 2024 2025»

**Funn:**
- Finans Norges klimarapport 2025 bekrefter at norske banker er i gang med fysisk klimarisiko, men fokuset er skadehendelser (flom, temperatur) — ikke bygningskvalitet/holdbarhet
- SINTEF/Finans Norge-survey: 1 av 3 banker mener fysisk klimarisiko er stor del av bærekraftfokuset; 17 av 24 har inkorporert det i strategi
- HiØF (Høgskolen i Østfold, 2025): Studie av klimaskaderisiko og boligpriser i fem norske byer (2019–2024, ~200 000 transaksjoner). Kobler klimarisiko til prisutvikling, men ikke til kredittrisiko/PD.
- Norges Bank Staff Memo 12/2025: kartlegging av skader fra klimaendringer i bygg — fokus på hendelsesdokumentasjon, ikke kredittmodell.

**Vurdering:** Bekrefter at norske banker er oppmerksomme på fysisk klimarisiko, men **koblingen fra bygningskvalitet/holdbarhet til kredittkvalitet er ikke operasjonalisert i norsk kontekst**. HiØF-studien og Norges Bank-memoen er begge relevante sekundærkilder for å vise at norsk fagmiljø nærmer seg tematikken, og kan styrke søknadens relevansargument. Ingen av dem fyller FoU-hullet.

**Relevante lenker:**
- [Finans Norge: norske banker og klimarisiko](https://www.finansnorge.no/tema/statistikk-og-analyse/klimarapporten/norske-banker-og-forsikringsselskaper-tar-grep-mot-klimarisiko/)
- [HiØF: Klimarisiko og boligmarkeder 2025](https://www.hiof.no/iio/ois/forskning/grupper/anvendt-samfunnsokonomi/aktuelt/2025-HLWP2025-4.html)
- [Norges Bank Staff Memo 12/2025](https://www.norges-bank.no/contentassets/afc40bb030be4a58a316d58a5f52308c/25_08492-2-staff-memo-12-2025-v2-1987038_1_1.pdf)

---

### S8 — Eiendom, fysisk risiko og kredittrisiko i Europa
**Søkt:** «property physical risk climate adaptation mortgage valuation flood degradation credit risk Europe 2024 2025»

**Funn:**
- ECB Working Paper 3036 (2024) «From flood to fire: is physical climate risk taken into account in mortgage pricing?» — viser at klimarisiko er priset inn i boliglånsrenter med en positiv risikopremie som øker over tid
- OECD «Future-Proofing Real Estate Investment» — fysisk risiko kan redusere eiendomsverdi med **5–20 %**; klimatilpasning koblet til investerings- og finansieringsrammer
- ECB/ESRB (2024): Klimarelatert forverring av makroøkonomisk miljø gir ~2 prosentpoengs økning i defaultfrekvens under stressscenarier
- EGUsphere preprint (2026): Finansiell risiko fra ekstremnedbør for eiendomsporteføljer (Europa)
- Ingen av studiene inkluderer **bygningskvalitet, fuktrobusthet eller vedlikeholdssvikt** som variabel

**Vurdering:** Klimarisiko → eiendomsverdi → kredittrisiko-koblingen er under aktiv utvikling i EU/ECB, men stopper konsekvent ved **lokalisering og klimahendelser** (flom, brann) — ikke bygningsfysisk tilstand. **Styrker FoU-hullet** ytterligere. ECB WP 3036 kan nevnes i søknaden som eksempel på at markedsaktørene beveger seg mot mer granulær risikoprising — som VERIFIED er posisjonert for å levere byggteknisk grunnlag til.

**Relevante lenker:**
- [ECB WP 3036: From flood to fire](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp3036~43450e2b8f.en.pdf)
- [OECD Future-Proofing Real Estate](https://www.oecd.org/en/publications/future-proofing-real-estate-investment_2dd12063-en/full-report/from-climate-related-shocks-to-financial-risks_d85d5492.html)
- [ECB Macroprudential Bulletin – climate stress test](https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202511_04.en.html)

---

## Del 3 — Anbefalinger: hull lukket vs. gjenstående

### Hull som er lukket eller vesentlig styrket etter dette søket

| Punkt | Status før | Status nå | Kilde |
| --- | --- | --- | --- |
| **Billio et al. fullstendig referanse (F15)** | Ufullstendig | **Lukket** | JREFE 65(3):419–450, 2022 |
| **FoU-hullet holdbarhet→PD** | Dokumentert internt | **Eksternt bekreftet** | S1, S3, S6, S7, S8 |
| **Byggenæringen = Norges største fastlandsnæring (F4, del 1)** | Udokumentert | **Delvis lukket** (sekundær) | Digital Norway / Construction City |
| **Lav digitalisering i byggenæringen (F4, del 2)** | Udokumentert | **Delvis lukket** (sekundær) | Digital Norway / DiBK |
| **IPN-rammevilkår** | Ikke sjekket | **Bekreftet** | Forskningsrådet.no 2026-utlysning |
| **EU MCD/ESG som energisentrert apparat** | [M] | **Styrket** | EBA 2023, FSUG 2025, MCD-revisjon |
| **Fysisk klimarisiko ikke = holdbarhet i norsk bankpraksis** | Antatt | **Bekreftet** | Finans Norge 2025, HiØF 2025 |

### Hull som gjenstår — krever SINTEF eller teamet

| Punkt | Hva som mangler | Hvem |
| --- | --- | --- |
| **Wiik 2025 «20 % uten merkostnad»** | Primærlesing av SINTEF Notat nr. 57 | SINTEF |
| **Mecca 2023 primærtekst** | Fulltekst via institusjonstilgang (ResearchGate-PDF finnes) | SINTEF |
| **Harerusten 2022 innhold (F5)** | Definere hva 2,2 mrd dekker | VIBS/SINTEF |
| **«Mest fragmentert» (F4, del 3)** | Kilde for fragmenteringsgrad | SINTEF/SSB |
| **WP-struktur (F13)** | SINTEF faglig gjennomgang | SINTEF |
| **Omnibus I primærkilde** | EUR-Lex/OJ-verifisering | Lars/SINTEF |
| **DNSH-matrise inkl. sosiale krav (F16/bolk 5)** | Matrise ennå ikke skrevet | VIBS-team |
| **WP3 baseline** | Pilotdesign mangler målt utgangspunkt | VIBS/Lars Gunnar |
| **SMB-atferd empirisk (F12b)** | Konkrete måleparametere | Lars Gunnar |

### Strategisk anbefaling

Det sterkeste argumentet for IPN-søknaden er nå godt underbygget: **litteraturen bekrefter konsekvent energi↔PD, men ingen studie dekker holdbarhet↔PD**. Åtte søk i dette agentsøket fant ingen motbevis. Formuler hullet presist i søknaden som «et dokumenterbart, eksternt verifiserbart gap i internasjonal litteratur» — ikke bare som en intern antagelse.

De tre røde hullene i samledokumentet (SMB-brukertest, DNSH-matrise, WP3-baseline) bør stå åpent i søknaden slik Forskningsrådet forventer: dette er nettopp hva prosjektet skal forske frem.

For den neste agentøkten prioriteres: SINTEF-verifisering av Wiik 2025 og Mecca 2023, samt utarbeiding av DNSH-matrise.

---

*Generert av Claude (Anthropic) som beslutningsstøtte. Påstandene i Del 2 er basert på åpnede websøkeresultater, ikke primærkilder. SINTEF eier faglig verifisering.*
