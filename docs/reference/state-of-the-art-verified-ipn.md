> Oppdatert 2026-06-27: kildestatus synket mot kanon. Billio 2022 og Kaza 2014 er grønne energi↔PD-kilder; An & Pivo 2020 er metadata-bekreftet, men fulltekst/34 %-tall må åpnes før bærende bruk.

# Kunnskapsstatus / State of the Art – VERIFIED (IPN)

**Status:** Utkast til intern bearbeiding. Skrevet som grunnlag for Vegard Knottens (SINTEF) leveranse «kartlegging av bransjeproblematikk og løsningsgrunnlag» og for FoU-/nyhetsverdidelen i en IPN-søknad (Innovasjonsprosjekt i næringslivet, Forskningsrådet).
**Versjon:** 0.2 – 2026-06-21
**Virkemiddel:** IPN (Forskningsrådet). Tilpasset fra konsortieversjonen GP26-220 VERIFIED (Grønn plattform) og FoU-panelnotatet `VIBS_VERIFIED_FoU-panel.docx`.
**Forfatteransvar:** Utkast generert som beslutningsstøtte. SINTEF (Knotten/Gullbrekken) eier den faglige vurderingen og må verifisere kilder før innsending.

> ⚠️ **Slik leses dokumentet:** Hver påstand er forsøkt knyttet til en faktisk åpnet kilde. Konfidens er flagget **[H]** (primærkilde åpnet og verifisert), **[H\*]** (høy konfidens via flere uavhengige sekundærkilder, men primærkilde ikke åpnet), **[M]** (bekreftet via sekundærkilde / kun sammendrag åpnet) eller **[L]** (kun søketreff/metadata – må verifiseres før sitering). Kilder merket «åpnet: nei» i [kildelisten](#13-kildeliste-og-verifiseringsstatus) er **ikke** lest i fulltekst og må kontrolleres av SINTEF før de brukes i søknaden. Dette er et bevisst trekk: en Forskningsrådet-leser skal kunne etterprøve hver referanse.

---

## 1. Hensikt og avgrensning

Denne kunnskapsstatusen skal gjøre tre ting for IPN-søknaden:

1. **Dokumentere at problemet er reelt** – at relevant data (LCA, LCC, EPD, FDV, levetid, risiko) finnes, men ikke er koblet til beslutning i tilbudsfasen.
2. **Vise hvor forskningsfronten står** – hvilke metoder, standarder og verktøy som finnes, og hvor modne de er.
3. **Begrunne forskningshullet (FoU-høyden)** – at ingen eksisterende metode eller verktøy kombinerer alle elementene VERIFIED bygger på, og at det gjenstår reelle, ikke-trivielle forskningsspørsmål.

Dokumentet bygger videre på, og dupliserer ikke, den eksisterende interne kunnskapsbasen i [`docs/reference/forskning-kunnskapsbase.md`](forskning-kunnskapsbase.md) (7 søyleområder, norsk problemdokumentasjon) og SINTEF-markedsanalysen i [`docs/business/marked-sintef.md`](../business/marked-sintef.md). De etablerte norske problemtallene (byggfeilkostnad 10–30 mrd/år, konfliktkostnad 2,2 mrd/år, 18 000 kr/m² dyrere enn Sverige osv.) behandles som etablert grunnlag og gjentas ikke her. Denne statusen legger til **standard-, forsknings- og reguleringslaget** med eksternt verifiserte kilder.

**Avgrensning:** Dette er en kunnskapsstatus, ikke en systematisk litteraturgjennomgang (SLR). Den er bred nok til å forankre nyhetsverdien, men SINTEF bør gjøre en målrettet fulltekst-verifisering av de fagfellevurderte kildene (se §11) før innsending.

---

## 2. Forskningshullet i korthet

VERIFIEDs nyhetsverdi er **ikke** et nytt enkeltverktøy, en ny miljøetikett eller en ny LCA-kalkyle. Forskningshullet ligger i **beslutningslogikken**:

> Hvordan kan heterogene og delvis mangelfulle byggevaredata (LCA, LCC, EPD/FDV, levetid, kvalitet, skaderisiko, ombruk) kombineres til et **forklarbart og etterprøvbart** flerkriteriegrunnlag som er anvendbart **allerede i tilbudsfasen**, av **ikke-spesialister** (SMB-entreprenører og boligkjøpere), og der **faktisk beslutningseffekt** kan måles og attribueres?

Kunnskapsstatusen under viser at hver byggekloss finnes, men at de lever i atskilte siloer, er bygget for spesialister i prosjekteringsfasen, og ikke er syntetisert til det VERIFIED beskriver. **Seks akser** definerer hullet, og brukes som målestokk gjennom hele dokumentet:

| Akse | Forklaring |
| --- | --- |
| **(a) Dataintegrasjon** | Kombinerer flere datatyper (LCA + LCC + EPD/FDV + levetid + risiko + ombruk), ikke bare én |
| **(b) Fase** | Brukt i **tilbudsfasen** (før kontrakt/innkjøp), ikke bare prosjektering/sluttdokumentasjon |
| **(c) Brukergruppe** | For **SMB / ikke-spesialister**, ikke bare LCA-/bærekraftfagfolk |
| **(d) Forklarbarhet og usikkerhet** | Synlig datakilde, datakvalitet og usikkerhet – ikke skjult i én totalscore |
| **(e) Beslutningseffekt** | Måler/attribuerer om rapporten faktisk endret eller bekreftet valget |
| **(f) Bredde i bærekraft (DNSH)** | Premierer levetid/robusthet/LCC, ikke bare lavt CO₂-tall |

---

## 3. LCA og LCC – metoder og standarder

**State of the art.** Metodegrunnlaget er modent og standardisert i to spor:

- **Miljø/LCA:** ISO 14040/14044 (prinsipper og rammeverk) **[M]**, EN 15804+A2 (produkt-EPD; obligatoriske moduler A1–A3, C1–C4 og D for nye EPD-er fra okt. 2022) **[M]**, og EN 15978 (aggregering av produkt-EPD til byggnivå) **[M]**.
- **Kostnad/LCC:** ISO 15686-5 (livsløpskostnad innen service life planning) **[M]** og ISO 15686-serien for levetidsplanlegging. I Norge ble **NS 3454 (livssykluskostnader) trukket 7. september 2023 og erstattet av NS-EN 16627** **[H]** – et viktig poeng: VERIFIED må forankre kostnadssiden i NS-EN 16627 / ISO 15686-5, ikke i utdaterte NS 3454.
- **Kombinert kost+karbon:** RICS «Whole Life Carbon Assessment» 2. utg. (i kraft fra 1. juli 2024) og EN 17472 (anlegg) viser at integrert LCA+LCC i ett rammeverk *finnes* – men foreløpig for anlegg / UK-profesjon. **[M/L]**

**Modenhet.** Høy. Dette er etablerte, internasjonalt brukte standarder. Norsk/nordisk forskning (SINTEF/NTNU) bygger nå whole-life-carbon-benchmarkverdier for norske bygg oppå EN 15978-strukturen **[L – kun søketreff, må verifiseres]**.

**Begrensning vs VERIFIED.** Konsistent på tvers av kildene:
- Rammeverkene er i hovedsak **enkeltsiloer** – miljø *eller* kostnad – og dekker ikke integrert flerkriterie inkl. levetid/skaderisiko/ombruk **(a, f)**.
- De er bygget for **kvalifiserte analytikere i prosjekteringsfasen**, ikke for SMB i tilbudsfasen **(b, c)**.
- De er **kalkyle-/rapporteringsstandarder** uten innebygd forklarbarhet eller attribusjon av beslutningseffekt **(d, e)**.

> **[BEKREFTET – 2026-06-21]** EN 15978:2026 ble publisert av CEN-CENELEC 17. april 2026. Erstatter EN 15978:2011. Gjelder nye bygninger, eksisterende bygninger og rehabiliteringsprosjekter. Kilde: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-04-17-en-15978-2026/ **[H – åpnet og verifisert]**

---

## 4. Produktdata, EPD og digitalt produktpass (DPP)

**State of the art.** Datainfrastrukturen modnes raskt:

- **EPD:** EPD-Norge (Norsk EPD-stiftelse) er programoperatør tilpasset ISO 14025 og EN 15804+A2, og publiserer maskinlesbare ILCD+EPD XML-datasett **[M]**. ECO Platform / ECO Portal harmoniserer europeisk EPD-tilgang **[M]**.
- **Produktidentitet:** **NOBB** (Norsk Byggevarebase, Norsk Byggtjeneste) er bransjens felles produktdataportal i Norge med ~3 mill. varer fra 900+ leverandører; NOBB-nummer + obligatorisk **GS1/GTIN** på pakninger gir en realistisk hovednøkkel for å koble heterogene data per byggevare **[M]**.
- **Regulatorisk retning (ferskvare – avgjørende for en Forskningsrådet-leser):**
  - **ESPR – forordning (EU) 2024/1781** er i kraft (vedtatt 13.06.2024) og etablerer digitalt produktpass (DPP) som transparensverktøy **[H – EUR-Lex åpnet]**. Første arbeidsplan (vedtatt 16.04.2025, dekker 2025–2030) prioriterer tekstil, møbler, jern/stål m.m. – **byggevarer er bevisst holdt utenfor første pulje** **[H/M]**.
  - **Revidert byggevareforordning – CPR (EU) 2024/3110** (vedtatt 27.11.2024, publisert 18.12.2024) innfører en egen **konstruksjons-DPP**; Kommisjonen får delegert myndighet til å etablere systemet, på linje med ESPR **[H – EUR-Lex åpnet]**. Faktiske produktkrav avhenger av delegerte rettsakter og harmoniserte standarder – anslagsvis andre halvdel av tiåret.
  - **CIRPASS-2** (Digital Europe, mai 2024–april 2027) piloterer bygg-DPP i praksis; byggepiloten ledes av **Cobuilder** (norsk kobling), med partnere som GS1 France, Velux, DFØ **[M]**.

**Modenhet.** Data og identifikatorer: middels–høy. Regulatorisk DPP for *bygg*: tidlig – lovfestet retning, men obligatoriske krav ennå ikke i kraft.

**Begrensning vs VERIFIED.** Hullet er **ikke mangel på data**, men at dataene er:
- **fragmentert** over flere portaler, med ulike PCR-regler, enheter og varierende generisk-vs-spesifikk kvalitet **(a, d)**;
- har **usikkerhet som sjelden synliggjøres** **(d)**;
- **ikke koblet til beslutning** i tilbudsfasen for SMB **(b, c)**.

VERIFIED kan posisjoneres som et tidlig, frivillig **«DPP-ready» beslutningslag** før de regulatoriske kravene biter – et tydelig markedsvindu.

---

## 5. Flerkriterie-beslutningsanalyse (MCDA)

**State of the art.** MCDA/MCDM for valg av byggematerialer er veletablert i akademia. **[BEKREFTET – 2026-06-21]** Mecca (2023), review i *Journal of Multi-Criteria Decision Analysis* (DOI 10.1002/mcda.1818), tallfester metodefordelingen i urban/arkitektonisk bærekraft: **AHP 46 %, TOPSIS 20 %, MIVES 11 %, COPRAS 9 %** **[H\* – metodefordeling bekreftet via to uavhengige søkekilder (Wiley-oppføring + ResearchGate); Wiley-fulltekst bak betalingsmur (402)]**. En systematisk gjennomgang av materialvalg i bygg bekrefter at AHP brukes mest til vekting, SAW til indeksbygging og TOPSIS til byggapplikasjoner **[L/M – abstrakt åpnet, ikke fulltekst]**.

**Modenhet.** Metodisk høy, men praktisk lav: dette er **metoder i litteratur, ikke utrullede produkter** for SMB.

**Begrensning vs VERIFIED.** Litteraturen peker selv konsistent på kjernesvakheten VERIFIED adresserer:
- **subjektiv vekting og ekspertavhengighet** – og at metode-/vektevalg kan endre rangeringer (resultatet er følsomt, ikke entydig) **[L/M]**;
- MCDA i bygg-anskaffelser konsentreres i **tildelingsfasen (award phase)**, mens prekvalifisering/verifisering er underutforsket **[M]**;
- **forklarbarhet** trekkes eksplisitt frem som problem (noen metoder er lite transparente).

Metodene for å kombinere data *forsvarlig* finnes altså, men er ikke pakket som et **forklarbart tilbudsfaseverktøy for ikke-spesialister** **(b, c, d)**.

---

## 6. Datakvalitet og usikkerhet i LCA

**State of the art.** Dette er det metodiske fundamentet for VERIFIEDs krav om at «manglende data ikke skjules, men gir høyere usikkerhet»:

- **Pedigree-matrisen (Weidema & Wesnæs 1996)** med fem datakvalitetsindikatorer (pålitelighet, kompletthet, tidsmessig/geografisk/teknologisk korrelasjon, hver skåret 1–5) er den etablerte rammen for å oversette kvalitativ datakvalitet til strukturerte usikkerhetsestimater **[H\* – primærartikkel ikke åpnet, men verifisert i to uavhengige åpnede kilder]**.
- Operasjonalisert i **ecoinvent**: pedigree-skår + basic uncertainty → lognormal fordeling → **Monte Carlo**-simulering **[M – mirror-kilde åpnet; bør suppleres med offisiell ecoinvent Data Quality Guideline]**.
- Edelen & Ingwersen (2018) dokumenterer forvaltning og bruk av datakvalitetsinformasjon i LCA **[H – fulltekst åpnet]**.
- Forskningsfronten (f.eks. **DMsan**, Lohman et al. 2023) viser at man kan unngå **én skjult totalscore** ved å eksponere usikkerhet og preferansefølsomhet («opportunity spaces» – under hvilke vekter vinner et alternativ) **[H – fulltekst åpnet]**.
- **[BEKREFTET – 2026-06-21]** Benke et al. (2025), *Scientific Data* (harmonisert datasett, 292 byggprosjekter Nord-Amerika), dokumenterer kjerneproblemet direkte: «industry-generated LCA results are rarely compiled into comparable datasets and rarely made public», og at verktøy som Tally og One Click LCA har «significant differences in their background LCI databases, default assumptions for certain life cycle stages and scenarios» – resultatene varierer med «modeling assumptions, and skill of the LCA modeler». Dette er empirisk belegg for at default-antakelser og modellørskjønn, ikke bare datakvalitet, driver usikkerhet. Kilde: https://pmc.ncbi.nlm.nih.gov/articles/PMC12218139/ **[H – fulltekst åpnet]**

**Modenhet.** Høy, men teknisk og spesialist-rettet.

**Begrensning vs VERIFIED.** Apparatet er **modent, men spesialist-orientert**: pedigree-matrisen er ekspertskjønn-basert, og verktøy som DMsan krever programmering og mangler GUI for ikke-tekniske brukere. Gapet – **«forklarbar usikkerhet for kunde/SMB i tilbudsfasen»** – er dermed empirisk bekreftet som reelt **(c, d)**.

---

## 7. Grønn finans, EU-taksonomi og ESG

**State of the art.** Rammeverket er modent på papiret, men energisentrert:

- **EU-taksonomien** krever for bygg (1) substansielt bidrag (TSC), (2) **DNSH** til øvrige miljømål og (3) minimumsgarantier. Aktiviteter med levetid >10 år krever **klimarisiko-/levetidsvurdering** – noe som treffer nær all eiendom **[H\* – rammeverk via sekundærkilder; M – eksakte TSC-tallverdier ikke verifisert mot EUR-Lex]**.
- **EBA-rapport om grønne lån og boliglån (15.12.2023)** foreslår et frivillig EU green loan-merke og å integrere grønt boliglån i Mortgage Credit Directive; peker på at lån til energirenovering og SMB ligger under EUs mål, og at **manglende harmoniserte definisjoner, data og teknisk dokumentasjon** er bindende skranke **[H – EBA åpnet]**.
- **EEMI / Energy Efficient Mortgage Label** (~37 banker; krav om ≥30 % energieffektivisering, taksonomi-tilpasset) er rammeverket VERIFIED kan koble seg på **[M]**.
- **Empiri energi↔risiko:** Høyere energieffektivitet er statistisk forbundet med **lavere sannsynlighet for boliglånsmislighold** i åpnet boliglånslitteratur (Billio et al. 2022; Kaza et al. 2014). An & Pivo (2020) støtter samme retning for kommersiell eiendom/CMBS, men Wiley-fulltekst må åpnes før 34 %-tallet brukes bærende. **[H for Billio/Kaza; H\* for An/Pivo]**.
- **Omnibus I** (vedtatt 24.02.2026) snevrer pliktig CSRD-/taksonomi-rapportering til store foretak (>1000 ansatte, >450 mEUR) og fjerner ~80 % av tidligere omfattede selskaper **[H\* – sekundærkilder; primær OJ/EUR-Lex ikke åpnet, se §13]**.

**Modenhet.** Regulatorisk høy; operasjonell dekning for SMB lav.

**Begrensning vs VERIFIED.**
- Hele apparatet er **energisentrert (kWh/EPC)** og fanger ikke levetid, fuktrobusthet eller vedlikehold – nettopp VERIFIEDs DNSH-utvidelse **(f)**.
- **[BEKREFTET]** Energieffektivitet korrelerer med lavere misligholdsrisiko (PD). Tre separate studier må holdes fra hverandre: (1) **Billio et al. (2022)** dokumenterer energi↔PD i nederlandske boliglån (*JREFE* 65(3):419–450; DOI 10.1007/s11146-021-09838-0). (2) **Kaza, Quercia & Tian (2014)** fant ~32 % lavere misligholdssannsynlighet for eiere av ENERGY STAR-sertifiserte **boliger** i USA (*Cityscape* 16(1):279–298). (3) **An & Pivo (2020)** gjelder **CMBS/kommersiell eiendom, ikke boliglån** (*Real Estate Economics* 48(1):7–42; DOI 10.1111/1540-6229.12228); 34 %-tallet må sjekkes i fulltekst/akseptert manus før bærende bruk. **[H for Billio/Kaza; H\* for An/Pivo]**
- **[HULL / FoU-ARGUMENT]** Ingen studie kobler bygningskvalitet, fuktrobusthet eller vedlikeholdssvikt direkte til misligholdsrisiko. Litteraturen dekker energi↔PD, men **ikke holdbarhet→PD**. Dette er et dokumenterbart og verifiserbart gap – og er selve FoU-argumentet for VIBS VERIFIEDs finansieringsvinkel.
- **[BEKREFTET – 2026-06-21] Regulatorisk medvind to spor:** (1) **Bank of England PS25/25** (des. 2025) erstatter klimaforventningene fra 2019 (SS3/19) og krever at banker og forsikringsselskap bygger klimarisiko inn i kjernerammeverk og styrebeslutninger, med frist for ferdige vurderinger **juni 2026** – betegnet som «a step change, not a refinement» **[H\* – substans bekreftet via uavhengig sekundærkilde (Green Central Banking); BoE-primær 403]**. (2) **Bank of England DP1/25** (juli 2025) gjelder **estimering av PD og LGD for boliglån** og barrierene mellomstore banker møter når de bygger IRB-modeller **[M – via søkesammendrag; BoE-primær 403]**. Merk: DP1/25 handler **ikke** om klima (tidligere antatt feil) – men det er nettopp PD/LGD/IRB-maskineriet VERIFIEDs holdbarhet→risiko-data skal mate, og «mellomstore aktører mangler modellkapasitet» speiler SMB-skranken. Begge sporene øker etterspørselen etter strukturert, bygningsnær risikodata uten å levere den selv.
- Etter Omnibus treffer tvungen rapportering færre SMB direkte – VERIFIED bør posisjoneres som **frivillig dokumentasjonsverktøy** for verdikjeden (trickle-down-press fra store kunder/banker består), ikke som compliance-tvang.

---

## 8. Byggskader, levetid, holdbarhet og ombruk

**State of the art.** Dataene finnes, men er generiske og lite anvendbare i beslutning:

- **Byggskadeomfang (SINTEF):** prosessfremkalte byggskader anslås til ca. **5 % av bransjens omsetning** i utbedringskostnader; ca. **3 av 4 byggskader er fuktrelaterte** **[M – eldre data (2006/2008), verifisert via flere søk; primær-PDF døde lenker]**.
- **Levetidsdata:** **Byggforskserien 700.320** («Intervaller for vedlikehold og utskifting av bygningsdeler») gir tabeller brukbare for LCC. **Eksplisitt forbehold i anvisningen:** intervallene skal *ikke* brukes direkte til å vurdere levetiden på en konkret eksisterende bygningsdel **[H – innhold/forbehold bekreftet]**. (Bak betalingsmur.)
- **Ombruk:** SINTEF Fag 18, FutureBuilt «Kriterier for sirkulære bygg» (v3.1, 14.11.2025) og DiBK/Resirqel «Forsvarlig ombruk av byggevarer» (2019) beskriver kriteriene (restlevetid, teknisk egnethet, dokumentasjon, ansvar, transport) – men **usikkerhet om kvalitet/egnethet er største barriere** **[M]**.

**Modenhet.** Datagrunnlag middels; operasjonalisering lav.

**Begrensning vs VERIFIED.** Treffer hullet presist: levetids-, fukt- og ombruksdata finnes, men er **(a) generiske, (b) delvis bak betalingsmur, og (c) eksplisitt ikke ment for direkte anvendelse på et konkret bygg eller en tilbudsbeslutning**. Det finnes **ingen bro** fra eksisterende kunnskap til den supplerende, anvendbare dokumentasjonen som grønn finans, forsikring, takst og ombruksbeslutninger etterspør **(b, e, f)**.

---

## 9. SMB-atferd og beslutningspraksis i tilbudsfasen

**State of the art.** Dette feltet er i stor grad udokumentert i fagfellevurdert litteratur for norsk kontekst:

- **[HULL – bekreftet]** Ingen empirisk studie dokumenterer hvordan norske SMB-entreprenører gjør materialvalg i tilbudsfasen. Beslutningspraksis for SMB i tilbud-/innkjøpsfasen er et verifisert blindfelt.
- **[BEKREFTET via Norden-rapport 2023]** Nordic Council (2023) bekrefter at LCA-reguleringer bevisst holdes svakere for SMB av konkurransehensyn: *«The regulations for LCA of buildings are less stringent than what large actors are doing. This is driven mainly by a fear of reducing the competitiveness for smaller actors who might not have resources to follow stringent regulations.»* *Åpnet: ja. [H]* Kilde: https://pub.norden.org/us2023-463/appendix-building-lca-and-bim-practices-in-norway.html
- **[BEKREFTET – pågående forskning]** BKA2 – *Bærekraftige anskaffelser for de vanlige bygg- og anleggsprosjektene, fase 2*. Budsjett: 11,7 MNOK, prosjektperiode til 2028. Prosjekteier: Trondheim kommune. SINTEF-representant: Vegard Knotten. Mål: teste og utvikle bærekraftskriterier for SMB i bygg- og anleggssektoren. *Åpnet: ja. [H]* Kilde: https://nit.no/prosjekter-og-innsikt/prosjekter/bærekraftige-anskaffelser-for-de-vanlige-bygg-og-anleggsprosjektene

**Modenhet.** Lav. Feltet er aktivt, men mangler publiserte empiriske data for norsk SMB-kontekst. BKA2 er pågående, ikke avsluttet.

**Begrensning vs VERIFIED.** Antagelsene om SMB-atferd i VERIFIED (at SMB velger pris fremfor kvalitet, ikke forstår LCA, trenger forenklede beslutningsverktøy) er plausible og faglig motiverte – men mangler empirisk belegg i norsk kontekst. BKA2 bekrefter at fagmiljøet anerkjenner hullet. Knottens dobbeltrolle i BKA2 og VERIFIED styrker konsortiekoblingen og troverdigheten av at prosjektet adresserer et aktivt forskningsspørsmål **(b, c)**.

---

## 10. Eksisterende verktøy og plattformer (konkurrentscan)

**Konklusjon:** Ingen åpnet verktøy dekker hele VERIFIED-kombinasjonen. Komponentene finnes spredt.

| Verktøy | Sterkest på | Stopper ved (gap vs VERIFIED) | Konf. |
| --- | --- | --- | --- |
| **One Click LCA** (FIN) | **(a)** sterkest dataintegrasjon: LCA+EPD+**LCC** med levetidsbasert utskifting (NS 3454/ISO 15686-5/EN 16627) | Spesialist-/dokumentasjonsverktøy; ingen synlig usikkerhet per valg **(d)**, ingen attribusjon **(e)**, tyngdepunkt prosjektering/sertifisering ikke tilbud **(b,c)** | M |
| **EC3** (Building Transparency, USA) | **(d)** forbilledlig synlig usikkerhet: konfidensintervall, «conservative/achievable estimate», usikkerhetsstraff ved manglende EPD | Enkriterium (kun innbygd karbon); ingen LCC/levetid/risiko **(a,f)**; «realized vs potential carbon» er estimat-vs-faktisk, ikke beslutningsattribusjon **(e)** | H |
| **Reduzer** (NO, NTNU) | Norsk, tilgjengelig, 15 000+ EPD; nærmest geografisk/brukermessig | Karbon-/LCA-fokusert, enkriterium i praksis; mangler flerkriterie, synlig usikkerhet, beslutningseffekt | M |
| **Madaster** (NL) | Materialpass + restverdi/sirkularitet, porteføljenivå | Passport/dokumentasjon, ikke MCDA i tilbudsfasen; ingen usikkerhet/attribusjon | M |
| **Cobuilder** (NO) | Produktdata-infrastruktur, DPP, FDV-struktur («verified data, not PDFs») | Datalag, ikke beslutningsmodell; gjør ingen forklarbar avveining | M |
| **Concular** (DE) | Sirkularitet/ombruk + CircularLCA + variantsammenligning | Ombruks-/LCA-fokus, ikke tilbudsfase-MCDA for SMB | M |
| **2050 Materials** | Flere miljødimensjoner + API | Miljødata-sammenligning, ikke integrert MCDA med kost/risiko/datatillit | L/M |

**Hvor de beste stopper:** konsekvent på to akser – **(d) synlig datakvalitet/usikkerhet integrert i selve beslutningen** (kun EC3, og kun for karbon) og **(e) attribusjon av faktisk beslutningseffekt** (ingen). Ingen kombinerer heterogen datasammenslåing + forklarbar flerkriterie-score + tilbudsfase + ikke-spesialist-brukergruppe + synlig usikkerhet + beslutningsattribusjon.

> **Forbehold:** Syv av åtte verktøyblokker hviler primært på én leverandørside åpnet én gang («ifølge leverandøren»); kun EC3 har uavhengig bekreftelse. WebSearch var US-rettet. Norske/EU-aktører bør få dypere uavhengig dekning før påstandene siteres. NOBB/Norsk Byggtjeneste produktside lot seg ikke åpne (404).

---

## 11. Syntese: gap-matrise (mater nyhetsverdi-delen direkte)

Hver rad er et felt der state of the art er moden, men stopper før VERIFIEDs kombinasjon. Denne tabellen kan limes nær uendret inn i søknadens nyhetsverdi-avsnitt.

| Felt / state of the art | (a) Integr. | (b) Tilbud­sfase | (c) SMB | (d) Synlig usikk. | (e) Besluln.­effekt | (f) DNSH-bredde |
| --- | :--: | :--: | :--: | :--: | :--: | :--: |
| LCA/LCC-standarder (EN 15804/15978:2026, ISO 15686-5) | Delvis | ✗ | ✗ | ✗ | ✗ | ✗ |
| EPD/produktdata/DPP (EPD-Norge, NOBB, ESPR/CPR) | Data­kilde | ✗ | ✗ | ✗ | ✗ | ✗ |
| MCDA-metoder (AHP/TOPSIS) | ✓ | ✗ | ✗ | Delvis | ✗ | ✓ |
| Datakvalitet/usikkerhet (pedigree, ecoinvent, DMsan) | – | ✗ | ✗ | ✓ | ✗ | – |
| Grønn finans/taksonomi/EEMI | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ (energi) |
| Levetid/skade/ombruk (Byggforsk, SINTEF Fag 18) | Data­kilde | ✗ | ✗ | ✗ | ✗ | ✓ |
| SMB-atferd/beslutningspraksis (Norden 2023, BKA2) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Verktøy: One Click LCA | ✓ | Delvis | Delvis | ✗ | ✗ | Delvis |
| Verktøy: EC3 | ✗ | Delvis | Delvis | ✓ | ✗ | ✗ |
| **VERIFIED (mål)** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** |

**Kjernepåstand for søknaden:** Komponentene finnes hver for seg og er modne. Ingen utrullet metode eller verktøy syr dem sammen til en **forklarbar, etterprøvbar flerkriterie-beslutningsmodell i tilbudsfasen for SMB-entreprenører og boligkjøpere, med synlig datatillit og målt beslutningseffekt**. Det er denne syntesen – ikke enkeltkomponentene – som er FoU-høyden.

---

## 12. Kobling til søknadens FoU-spørsmål

Kunnskapsstatusen forankrer FoU-spørsmålene F1–F6 fra prosjektbeskrivelsen:

| FoU-spm | Forankret i (§) | Dokumentert hull |
| --- | --- | --- |
| **F1** Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet for boliglån [H] via Billio/Kaza; An/Pivo støtter næringsbygg [H\*]; holdbarhet→PD er ubekreftet og er FoU-hullet |
| **F2** NOBB/GTIN/EPD/FDV tidlig nok i tilbud | §4 | Data finnes, men fragmentert og ikke koblet til tilbudsbeslutning |
| **F3** Når er ombruk/rehab best | §8 | Ombrukskriterier beskrevet, ikke operasjonalisert til beslutning |
| **F4** Forstår kunder/SMB rapporten; påvirker den valg | §5, §6, §9 | Forklarbarhet og attribusjon udekket; SMB-atferd empirisk udokumentert |
| **F5** Byggdata → ESG/grønn finans/forsikring/takst | §7 | Apparatet er energisentrert; bro fra byggteknisk dok. mangler |
| **F6** Dataflyt/API/sporbarhet kan verifiseres/skaleres | §4, §10 | DPP-infrastruktur umoden for bygg; verktøy er siloer |

---

## 13. Kildeliste og verifiseringsstatus

Status «åpnet: ja» = lest i denne runden; «nei» = kun søketreff/metadata, **må verifiseres av SINTEF før sitering**. Konfidens som i teksten.

### Standarder og regulering
- ISO 14040/14044:2006 – LCA prinsipper og krav. *Åpnet: nei (kun sekundærbeskrivelse). [M]*
- EN 15804:2012+A2:2019 – EPD core rules (CEN/TC 350). *Åpnet: nei (to sekundærkilder). [M]*
- **EN 15978:2026** – LCA på byggnivå. Publisert CEN-CENELEC 17. april 2026. Erstatter EN 15978:2011. Gjelder nye bygninger, eksisterende bygninger og rehabiliteringsprosjekter. *Åpnet: ja (CEN-CENELEC nyhetsside). [H]* Kilde: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-04-17-en-15978-2026/
- EN 17472:2022 – bærekraftvurdering anlegg (LCA+LCC). *Åpnet: nei. [L]*
- ISO 15686-5:2017 – livsløpskostnad (LCC). *Åpnet: nei. [M]*
- **NS 3454 → NS-EN 16627** – norsk LCC trukket 2023-09-07, erstattet. *Åpnet: ja (Standard Norge + Anskaffelser.no). [H]*
- RICS Whole Life Carbon Assessment, 2. utg. (i kraft 01.07.2024). *Åpnet: nei. [M]*
- **Forordning (EU) 2024/3110 (revidert CPR), konstruksjons-DPP.** EUR-Lex `eli/reg/2024/3110/oj`. *Åpnet: ja. [H]*
- **Forordning (EU) 2024/1781 (ESPR), DPP; arbeidsplan 2025–2030 (16.04.2025).** EUR-Lex `eli/reg/2024/1781/oj`. *Åpnet: ja (forordning); arbeidsplandato via flere sekundærkilder. [H/M]*
- EU-taksonomi, Climate Delegated Act + DNSH (under revisjon 2024–25). *Åpnet: via søk/bransje (ikke primær). [H\* rammeverk, M tallverdier]*
- Omnibus I «Stop-the-Clock» / CSRD-innsnevring (vedtatt 24.02.2026). *Åpnet: sekundær (PwC/White & Case); primær OJ/EUR-Lex ikke åpnet. [H\*]*
- **Bank of England PS25/25** (des. 2025). *Enhancing banks' and insurers' approaches to managing climate-related risks – Update to SS3/19.* Klimarisiko inn i kjernerammeverk; frist juni 2026. *Åpnet: nei (BoE 403); substans bekreftet via Green Central Banking. [H\*]* Kilde: https://www.bankofengland.co.uk/prudential-regulation/publication/2025/december/enhancing-banks-and-insurers-approaches-to-managing-climate-related-risks-policy-statement
- **Bank of England DP1/25** (juli 2025). *Residential mortgages: LGD and PD estimation* – barrierer mellomstore banker møter med IRB-modeller; lukket okt. 2025, PRA konsulterer 2026/27. **NB: gjelder ikke klima.** *Åpnet: nei (BoE 403); via søkesammendrag. [M]*

### Forskning og metode
- Weidema, B.P. & Wesnæs, M.S. (1996). *Data quality management for life cycle inventories – data quality indicators.* J. Cleaner Production 4(3–4):167–174. *Primærartikkel ikke åpnet; verifisert via to uavhengige åpnede sekundærkilder. [H\*]*
- Edelen, A. & Ingwersen, W. (2018). *The creation, management, and use of data quality information for LCA.* Int. J. LCA. PMC5919259. *Åpnet: ja (fulltekst). [H]*
- Lohman, H.A.C. et al. (2023). *DMsan: A Multi-Criteria Decision Analysis Framework…* ACS Environmental Au. PMC10197171. *Åpnet: ja (fulltekst). [H]*
- ecoinvent – usikkerhet/pedigree → lognormal/Monte Carlo. *Åpnet: ja (mirror; bør suppleres med offisiell DQG). [M]*
- Ciroth et al. (2016). *Empirically based uncertainty factors for the pedigree matrix in ecoinvent.* Int. J. LCA 21:1338. *Åpnet: nei. [L/M]*
- Mecca, B. (2023). *Assessing the sustainable development: A review of MCDA for urban and architectural sustainability.* J. Multi-Criteria Decision Analysis. DOI 10.1002/mcda.1818. Metodefordeling AHP 46 % / TOPSIS 20 % / MIVES 11 % / COPRAS 9 %. *Åpnet: nei på Wiley-fulltekst (402 betalingsmur); metodefordeling bekreftet via to uavhengige søkekilder; ResearchGate-PDF finnes for SINTEF-fulltekst. [H\*]* Kilde: https://onlinelibrary.wiley.com/doi/10.1002/mcda.1818
- *Material selection in the construction industry: a systematic review on MCDM* (2025). Environment Systems and Decisions. DOI 10.1007/s10669-025-10001-w. *Åpnet: nei (abstrakt). [L/M]*
- **Benke, B. et al. (2025).** *A Harmonized Dataset of High-Resolution Embodied LCA Results for Buildings in North America.* Scientific Data. Bekrefter at industri-LCA sjelden er offentlig/sammenlignbar og at verktøy (Tally, One Click LCA) har ulike default-antakelser og LCI-databaser. *Åpnet: ja (fulltekst PMC). [H]* Kilde: https://pmc.ncbi.nlm.nih.gov/articles/PMC12218139/
- Billio, M., Costola, M., Pelizzon, L. & Riedel, M. (2022). *Buildings' Energy Efficiency and the Probability of Mortgage Default: The Dutch Case.* The Journal of Real Estate Finance and Economics 65(3):419–450. DOI 10.1007/s11146-021-09838-0. *DOI/Springer + Crossref åpnet. [H]*
- An, X. & Pivo, G. (2020). *Green Buildings in Commercial Mortgage-Backed Securities: The Effects of LEED and Energy Star Certification on Default Risk and Loan Terms.* Real Estate Economics 48(1):7–42. DOI 10.1111/1540-6229.12228. Gjelder **kommersiell eiendom (CMBS)** — ikke boliglån. *Metadata bekreftet via Crossref; Wiley-fulltekst ga 403. 34 %-tallet må sjekkes i fulltekst/akseptert manus før bærende bruk. [H\*]*
- Kaza, N., Quercia, R.G. & Tian, C.Y. (2014). *Home Energy Efficiency and Mortgage Risks.* Cityscape 16(1):279–298. Analyserte ENERGY STAR-sertifiserte boliger (residensielle lån) og fant lavere misligholdssannsynlighet. *Åpnet via HUD/Cityscape; forfatterliste korrigert 2026-06-27. [H]*
- Norsk/nordisk WLC-benchmark for bygg (Building Research & Information / Building and Environment, 2024–25). *Åpnet: nei (søketreff). [L]*

### Bransje, offentlig og verktøy
- EBA (2023). *Report on Green Loans and Mortgages.* *Åpnet: ja. [H]*
- EEMI / Energy Efficient Mortgage Label; DeliverEEM (2024–). *Åpnet: via søk (ikke primær). [M]*
- EPD-Norge / ECO Platform / ECO Portal. *Åpnet: nei (sammendrag). [M]*
- NOBB / Norsk Byggtjeneste; GS1/GTIN-regelverk. *Åpnet: nei (sammendrag). [M]*
- CIRPASS-2 (bygg-DPP-pilot, Cobuilder). *Åpnet: nei (sammendrag). [M]*
- Ingvaldsen, T., SINTEF Byggforsk (2008). *Byggskadeomfanget i Norge* (PR308/2001, PR163/1994). *Åpnet: delvis (døde lenker, verifisert via søk). [M]*
- Byggforskserien 700.320 – *Intervaller for vedlikehold og utskifting av bygningsdeler.* *Åpnet: ja (via søk; anvisning bak betalingsmur). [H]*
- SINTEF Fag 18 – *Anbefalinger ved ombruk av byggematerialer*; FutureBuilt v3.1 (14.11.2025); DiBK/Resirqel (2019). *Åpnet: forsøkt (binær PDF), verifisert via søk. [M]*
- Verktøy: One Click LCA, EC3 (Building Transparency), Reduzer, Madaster, Cobuilder, Concular, 2050 Materials. *Åpnet: ja (produktsider); kun EC3 uavhengig bekreftet. [H for EC3, M/L øvrige]*
- **Norsk Byggtjeneste (NOBB) × One Click LCA-partnerskap** for å øke EPD-adopsjon i Norge til lav kostnad; as-built-LCA er nå regulatorisk krav i DK/FI/NO/SE. *Åpnet: ja (OCL pressemelding) – leverandørframstilling, bør suppleres med uavhengig kilde. [M]* Kilde: https://oneclicklca.com/en/resources/press-release/norsk-byggtjeneste-partners-up-with-one-click-lca-to-boost-epd-adoption-in-norway

### SMB-atferd og norsk kontekst
- Nordic Council of Ministers (2023). *Building LCA and BIM practices in Norway* (vedlegg til TemaNord-rapport). Bekrefter at LCA-krav bevisst holdes svakere for SMB av konkurransehensyn. *Åpnet: ja. [H]* Kilde: https://pub.norden.org/us2023-463/appendix-building-lca-and-bim-practices-in-norway.html
- BKA2 – *Bærekraftige anskaffelser for de vanlige bygg- og anleggsprosjektene, fase 2*. Budsjett 11,7 MNOK, til 2028. Prosjekteier: Trondheim kommune. SINTEF-representant: Vegard Knotten. *Åpnet: ja. [H]* Kilde: https://nit.no/prosjekter-og-innsikt/prosjekter/bærekraftige-anskaffelser-for-de-vanlige-bygg-og-anleggsprosjektene

### Interne konsortiekilder (ikke uavhengig hentet her – SINTEF leverer)
- **SINTEF Notat nr. 57** = Wiik, M.K. (2025). *Kostnadseffekten av klimatiltak i byggenæringen.* (Referert i [`marked-sintef.md`](../business/marked-sintef.md); innhold ikke selvstendig verifisert i denne runden.)
- Gullbrekken, L. og Holme, J. (2025). *Byggskader – Det glemte pengesluket.* SINTEF.
- Øvrige etablerte norske kilder: se [`forskning-kunnskapsbase.md`](forskning-kunnskapsbase.md) og [`marked-sintef.md`](../business/marked-sintef.md).

---

## Vedlegg A. Leseark og dispatch-vurdering

- [`state-of-the-art-leseark-2026-06-21.html`](state-of-the-art-leseark-2026-06-21.html) – samlet leseark for gjennomgang av dokumentet, med vurdering av dispatch-innsatsen, hva som er nytt etter dagens søk, hva dokumentet er/ikke er, Sonar-status og prioriterte kunnskapshull.

---

## 14. Hva Knotten/SINTEF må gjøre før innsending

1. **Fulltekst-verifiser fagfellevurderte kilder** merket «åpnet: nei» via institusjonstilgang. **[DELVIS – 2026-06-21]** Mecca (2023) metodefordeling nå bekreftet (AHP 46 / TOPSIS 20 / MIVES 11 / COPRAS 9); gjenstår: MCDM-review 2025 (DOI 10.1007/s10669-025-10001-w) og WLC-benchmark-artiklene.
2. ~~**Avklar EN 15978 revisjonsstatus**~~ **[LØST – 2026-06-21]** EN 15978:2026 publisert 17.04.2026 (CEN-CENELEC). Ingen videre handling nødvendig.
3. **Verifiser EU-taksonomiens eksakte TSC-tallverdier** mot EUR-Lex før de siteres.
3b. **Pinn Omnibus I mot primær OJ/EUR-Lex** – datoene (vedtatt 24.02.2026 / OJ 26.02.2026) er ferskt 2027-regelverk, kun sekundærsitert. Merk at «Stop-the-Clock»-trinnet og det substansielle Omnibus-innholdet fulgte ulike tidslinjer; bekreft hva som faktisk ble vedtatt før det går til Forskningsrådet.
4. **Lever SINTEF Notat 57 (Wiik 2025)** og koble dens kostnadseffekt-tall til F1.
5. **Styrk konkurrentscanet** med uavhengige kilder for de norske/EU-verktøyene (One Click LCA, Reduzer, Cobuilder, NOBB) – flere hviler nå på leverandørframstilling.
6. **FoU-hullet «holdbarhet → finansiell risiko» er dokumentert** (se §7): litteraturen bekrefter energi↔PD [H], men ikke holdbarhet→PD. Formuler dette eksplisitt som et eget empirisk bidrag i søknaden.
7. **Fagfellesjekk gap-matrisen (§11)** – det er den som mater nyhetsverdi-avsnittet direkte, så hver ✗/✓ må tåle SINTEF-kontroll.
8. **Koble BKA2 til søknadsnarrativet** – Knottens dobbeltrolle gir legitimitet; beskriv VERIFIED som et komplement til BKA2 (verktøy og beslutningslogikk, ikke bare kriterieliste).

---

### Verifiseringslogg 2026-06-21 (dispatch-runde, fem søk S1–S5)

| Søk | Tema | Status | Utfall |
| --- | --- | --- | --- |
| S1 | LCA-defaulter / praktikervariabilitet | ✅ Bekreftet | Benke et al. 2025 (Scientific Data) [H] → §6 |
| S2 | BKA2 full kontekst | ✅ Bekreftet (tidligere) | NiT-prosjektside [H] → §13 |
| S3 | Bank of England + EU-taksonomi fysisk risiko | ✅ Bekreftet m/korreksjon | PS25/25 klima [H\*]; DP1/25 = PD/LGD, **ikke klima** [M] → §7 |
| S4 | Mecca 2023 (MIVES) + MCDM-review | 🟡 Delvis | Mecca metodefordeling [H\*]; review 2025 gjenstår → §5 |
| S5 | SMB-marked / nordisk kapasitet / støtte | 🟡 Delvis | SMB-skranke + NOBB×OCL EPD-partnerskap [M]; Enova/IN-ordninger gjenstår → §8/§13 |

Primærkilder som returnerte 403/402 (BoE, Wiley) er flagget i §13 og må hentes via institusjonstilgang før direkte sitering.
