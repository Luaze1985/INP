# Kildeinventar – VERIFIED

**Fase:** 1 av 4 – inspeksjon og behandlingsplan  
**Dato:** 2026-07-11  
**Avgrensning:** Bare kilder som er markert grønn eller gul i det kanoniske kildebiblioteket. Røde kilder er ikke tatt inn. Dette dokumentet analyserer ikke innhold eller argumenter.

## Grunnlag og status for filtilgang

Kildestatus er hentet fra `docs/reference/ipn-kildebibliotek.md`, med kontroll mot `docs/reference/vibs-verified-kildedom-2026-06-27.md`. Det finnes **ingen originale forskningsartikler, rapport-PDF-er, standardtekster eller nedlastede nettsidekopier lokalt** i `ipn-verified`. Det som faktisk finnes lokalt er:

| Lokal fil | Rolle | Dekning |
| --- | --- | --- |
| `docs/reference/ipn-kildebibliotek.md` | Kanonisk register med tittel-/statusmetadata | 60 registrerte kilder |
| `docs/reference/vibs-verified-kildedom-2026-06-27.md` | Avstemming av enkelte nøkkelreferanser | Delmengde; særlig korreksjoner og grensekilder |
| `.scratch/gemma4-source-consistency/all-sources/batch-01.md`–`batch-08.md` | Arbeidskopier av registerradene | Metadata, ikke originalkilder |
| `provenance/agents/explorer_reconciliation_3/analysis.md` | Tre direkte identifikatorer for finansstudier | DOI/URL for An, Billio og Kaza |

**Konsekvens:** «Åpnet: ja» i kilderegisteret er tidligere verifikasjonsstatus, ikke bevis på at fulltekst ligger lokalt nå. Evidenskort kan ikke lage presise sidehenvisninger før originalfil eller stabil kilde-URL er gjort tilgjengelig.

## Kilder i utvalget

Kolonnen *tilgang nå* skiller mellom originalkilde som kan identifiseres med direkte URL/DOI i repoet og rene metadata. «Lokal metadata» betyr at bare registeroppføringen er tilgjengelig.

### A. Standarder, regelverk og utlysningsramme

| Nøkkel | Tittel – forfatter/organisasjon – år | Type/kategori | Status | Tilgang nå |
| --- | --- | --- | --- | --- |
| EN15978-2026 | EN 15978:2026 – LCA på byggnivå – CEN-CENELEC – 2026 | Standard/regulering | 🟢¹ | Lokal metadata; standardtekst mangler |
| NS-EN16627 | NS-EN 16627 / erstatter NS 3454 – Standard Norge – år ikke oppgitt | Standard/LCC | 🟢 | Lokal metadata; original mangler |
| CPR2024 | Forordning (EU) 2024/3110 – EU – 2024 | Regelverk/DPP | 🟢 | Lokal metadata; EUR-Lex-URL mangler i repo |
| ESPR2024 | Forordning (EU) 2024/1781 – EU – 2024 | Regelverk/DPP | 🟢 | Lokal metadata; original URL mangler |
| ISO14040 | ISO 14040/14044:2006 – ISO – 2006 | Standard/LCA | 🟡 | Lokal metadata; standardtekst mangler |
| EN15804 | EN 15804+A2 – CEN/TC 350 – år ikke oppgitt | Standard/EPD | 🟡 | Lokal metadata; standardtekst mangler |
| ISO15686-5 | ISO 15686-5:2017 – ISO – 2017 | Standard/LCC | 🟡 | Lokal metadata; standardtekst mangler |
| RICS-WLC | Whole Life Carbon Assessment, 2. utg. – RICS – 2024 | Faglig veileder | 🟡 | Lokal metadata; original mangler |
| EUTax | EU-taksonomi, Climate Delegated Act + DNSH – EU – 2024–25 | Regelverk | 🟡 | Lokal metadata; primærlenke mangler |
| OmnibusI | Omnibus I / CSRD-innsnevring – EU – 2026 | Regelverk | 🟡 | Lokal metadata; primærtekst mangler |
| NFR_IPN2026 | Innovasjonsprosjekt i næringslivet: Industri og tjenestenæringer – Norges forskningsråd – 2026 | Offisiell utlysning | 🟢 | Lokal metadata; original URL mangler |

### B. Forskning og metode

| Nøkkel | Tittel – forfatter/organisasjon – år | Type/kategori | Status | Tilgang nå |
| --- | --- | --- | --- | --- |
| Edelen2018 | Creation, management, use of data quality information for LCA – Edelen & Ingwersen – 2018 | Fagfellevurdert artikkel | 🟢 | Lokal metadata; fulltekst/DOI mangler |
| Lohman2023 | DMsan: MCDA framework – Lohman mfl. – 2023 | Fagfellevurdert artikkel | 🟢 | Lokal metadata; fulltekst/DOI mangler |
| Benke2025 | Harmonized embodied-LCA dataset – Benke mfl. – 2025 | Fagfellevurdert artikkel/datasett | 🟢 | Lokal metadata; fulltekst/DOI mangler |
| Weidema1996 | Data quality indicators (pedigree) – Weidema & Wesnæs – 1996 | Fagfellevurdert artikkel | 🟡 | Lokal metadata; original mangler |
| ecoinvent | Pedigree → lognormal/Monte Carlo – ecoinvent – år ikke oppgitt | Metode/datasett | 🟡 | Lokal metadata; kun «mirror» registrert |
| Mecca2023 | Assessing the sustainable development: review of MCDA for urban and architectural sustainability – Mecca – 2023 | Fagfellevurdert oversikt | 🟡 | DOI `10.1002/mcda.1818`; fulltekst utilgjengelig i registeret (Wiley 402) |
| Ciroth2016 | Uncertainty factors for pedigree in ecoinvent – Ciroth mfl. – 2016 | Fagfellevurdert artikkel | 🟡 | Lokal metadata; original mangler |

### C. Grønn finans og finansielt sammenligningsspor

| Nøkkel | Tittel – forfatter/organisasjon – år | Type/kategori | Status | Tilgang nå |
| --- | --- | --- | --- | --- |
| EBA_EU2023 | Report on Green Loans and Mortgages – European Banking Authority – 2023 | Offisiell rapport | 🟢 | Lokal metadata; original URL mangler |
| Billio2022 | Buildings' energy efficiency and the probability of mortgage default: The Dutch case – Billio, Costola, Pelizzon & Riedel – 2022 | Fagfellevurdert artikkel | 🟢 | DOI `https://doi.org/10.1007/s11146-021-09838-0`; ingen lokal fulltekst |
| An2020 | Green Buildings in Commercial Mortgage-Backed Securities – An & Pivo – 2020 | Fagfellevurdert artikkel | 🟡 | DOI `https://doi.org/10.1111/1540-6229.12228`; Wiley 403/notert som ikke fulltekstverifisert |
| Kaza2014 | Home Energy Efficiency and Mortgage Risks – Kaza, Quercia & Tian – 2014 | Artikkel/rapport | 🟢 | IMT/UNC-PDF `https://imt.org/wp-content/uploads/2018/02/IMT_UNC_HomeEEMortgageRisksfinal.pdf`; ingen lokal kopi |
| BoE_PS25-25 | Policy Statement PS25/25 – Bank of England – 2025 | Regulatorisk policy | 🟡 | Lokal metadata; BoE 403 notert |
| BoE_DP1-25 | Discussion Paper DP1/25 – Bank of England – 2025 | Regulatorisk diskusjonsnotat | 🟡 | Lokal metadata; original mangler |
| EEMI | Energy Efficient Mortgage Label / DeliverEEM – EEMI – år ikke oppgitt | Bransjeinitiativ | 🟡 | Lokal metadata; URL mangler |
| FinanceNorway2018 | Roadmap for Green Competitiveness – Finance Norway – 2018 | Bransjerapport | 🟡 | Lokal metadata; original mangler |
| Multiconsult2023 | Bolig-/utslippstall – Multiconsult/Eika Boligkreditt – 2023 | Bransjeanalyse | 🟡 | Lokal metadata; original mangler |

### D. Verktøy og datainfrastruktur

| Nøkkel | Tittel – forfatter/organisasjon – år | Type/kategori | Status | Tilgang nå |
| --- | --- | --- | --- | --- |
| EC3 | EC3 – Building Transparency – år ikke oppgitt | Verktøy/konkurrentscan | 🟢 | Lokal metadata; original URL mangler |
| OneClickLCA | One Click LCA – One Click LCA – år ikke oppgitt | Leverandørverktøy | 🟡 | Lokal metadata; leverandørside, URL mangler |
| Reduzer | Reduzer – Reduzer/NTNU – år ikke oppgitt | Leverandørverktøy | 🟡 | Lokal metadata; leverandørside, URL mangler |
| Madaster | Madaster – Madaster – år ikke oppgitt | Leverandørverktøy | 🟡 | Lokal metadata; leverandørside, URL mangler |
| Cobuilder | Cobuilder – Cobuilder – år ikke oppgitt | Leverandørverktøy/datainfrastruktur | 🟡 | Lokal metadata; leverandørside, URL mangler |
| Concular | Concular / CircularLCA – Concular – år ikke oppgitt | Leverandørverktøy | 🟡 | Lokal metadata; leverandørside, URL mangler |
| NOBB-OCL | Norsk Byggtjeneste × One Click LCA-partnerskap – organisasjonene – år ikke oppgitt | Partnerskapsmelding | 🟡 | Lokal metadata; leverandørframstilling, URL mangler |

### E. Norsk bransje- og byggkontekst

| Nøkkel | Tittel – forfatter/organisasjon – år | Type/kategori | Status | Tilgang nå |
| --- | --- | --- | --- | --- |
| NOBB | NOBB / GS1/GTIN-regelverk – Norsk Byggtjeneste – år ikke oppgitt | Produktdata/infrastruktur | 🟡 | Lokal metadata; original mangler |
| EPD-Norge | EPD Norge / ECO Platform / ECO Portal – organisasjonene – år ikke oppgitt | Produktdata/EPD | 🟡 | Lokal metadata; original mangler |
| CIRPASS2 | CIRPASS-2, bygg-DPP-pilot – CIRPASS-2/Cobuilder – år ikke oppgitt | Pilot/program | 🟡 | Lokal metadata; original mangler |
| Byggforsk700.320 | Byggforskserien 700.320 – SINTEF Byggforsk – år ikke oppgitt | Faglig anvisning | 🟡 | Lokal metadata; standard/anvisning bak betalingsmur |
| Ingvaldsen2008 | Byggskadeomfanget i Norge – Ingvaldsen, SINTEF Byggforsk – 2008 | Rapport | 🟡 | Lokal metadata; delvis, døde lenker notert |
| FinansNorge2024VASK | Skadestatistikk for 2023 – Finans Norge – 2024 | Offisiell bransjestatistikk | 🟢 | Lokal metadata; original URL mangler |
| SINTEFFag18 | SINTEF Fag 18; FutureBuilt v3.1; DiBK/Resirqel – flere – 2019–2025 | Faglige veiledere | 🟡 | Sammenslått registerrad; originaler mangler |
| PlanGridFMI2018 | Construction Disconnected – PlanGrid/FMI – 2018 | Bransjerapport | 🟡 | Lokal metadata; original mangler |
| Herfjord2021 | BIM-/omarbeidstall – Herfjord & Adolfsen, NTNU – 2021 | Akademisk oppgave | 🟡 | Lokal metadata; original mangler |
| SA2018 | Konflikter i bygg- og anleggsnæringen – Samfunnsøkonomisk analyse – 2018 | Rapport | 🟡 ⏸ | Ikke lokalisert/åpnet; parkert i søknadstekst |
| Harerusten2022 | Konflikter i bygg- og anleggsbransjen – Harerusten, NTNU – 2022 | Masteroppgave/sekundærkilde | 🟡 | Lokal metadata; original er registrert som åpnet sekundærkilde, men ikke lokalt |
| Bygg21_2019 | Digitalt materialkjøp / sporbarhet – Bygg21 – 2019 | Bransjerapport | 🟡 | Lokal metadata; original mangler |
| KS2025 | Byggesøknader og digitalt enevalg – KS/NHO/DiBK/KDD – 2025 | Offentlig/bransjestatistikk | 🟡 | Lokal metadata; original mangler |

### F. SMB-praksis og konsortieinterne synteser

| Nøkkel | Tittel – forfatter/organisasjon – år | Type/kategori | Status | Tilgang nå |
| --- | --- | --- | --- | --- |
| Nordic2023 | Building LCA and BIM practices in Norway – Nordic Council of Ministers – 2023 | Offisiell/nordisk rapport | 🟢 | Lokal metadata; original URL mangler |
| BKA2 | Bærekraftige anskaffelser fase 2 – SINTEF/Knotten – 2024–2028 | Prosjekt/program | 🟢 | Lokal metadata; original mangler |
| Lutdal2021 | Boligeierundersøkelse – Lutdal & Brenden, NTNU – 2021 | Akademisk oppgave | 🟡 | Lokal metadata; kun via bestillingsverk |
| Refleksjonsnotat2026 | Et blikk på byggebransjen og muligheter fremover – SINTEF/Knotten – 2026 | Konsortie-intern syntese | 🟡 | Original fil er ikke funnet; metadata/arbeidsspor finnes |
| Wiik2025 | Kostnadseffekten av klimatiltak i byggenæringen – M. K. Wiik, SINTEF – 2025 | Konsortie-internt notat | 🟡 ⏸ | Ikke funnet i åpne registre eller lokalt; parkert |
| GullbrekkenHolme2025 | Byggskader – Det glemte pengesluket – Gullbrekken & Holme, SINTEF – 2025 | SINTEF-artikkel/rapport | 🟡 | Lokal metadata; fulltekst må åpnes |
| EBA_NO2023 | Veileder for klimagassreduksjoner – boligblokker – Entreprenørforeningen Bygg og Anlegg, Grønn Byggallianse & Norsk Eiendom – 2023 | Bransjeveileder | 🟡 | Lokal metadata; original mangler |
| KD2024 | Byggenæringens klimafotavtrykk – et kunnskapsgrunnlag – KDD, DiBK, Fellesforbundet & NHO Byggenæringen – 2024 | Offentlig/bransjerapport | 🟡 | Lokal metadata; original mangler |

## Ufullstendige, overlappende eller utilgjengelige kilder

- **Manglende originaler:** Alle kildene over mangler lokal fulltekst. Dette er den viktigste inngangsrisikoen for fase 2, fordi kortene krever presise sider, avsnitt, tabeller eller figurer.
- **Direkte identifikatorer finnes bare for fire:** Billio 2022, An 2020, Kaza 2014 og Mecca 2023 (DOI for sistnevnte). Kaza har i tillegg en konkret PDF-lenke. De øvrige trenger først offisiell URL eller originalfil.
- **Ufullstendige registerrader:** Flere verktøy- og infrastrukturoppføringer mangler årstall og stabil URL. `SINTEFFag18` er en sammenslått rad med tre eller flere kilder og må splittes før evidenskort kan lages.
- **Parkerte gule kilder:** `SA2018` og `Wiik2025` er markert ⏸ og skal ikke behandles som aktivt belegg uten at originalen lokaliseres og status endres.
- **Kjente overlapp:** `CPR2024` og `ESPR2024` berører DPP fra ulike regelverk; `EBA_EU2023` og `EBA_NO2023` har lik forkortelse, men ulike organisasjoner og tema; `SA2018` og `Harerusten2022` gjelder samme konfliktkostnadskjede, der Harerusten er sekundær; `Wiik2025` er en intern syntese som peker mot `EBA_NO2023` og `KD2024`.

## Behandlingsrekkefølge

1. **Grønne kilder som ligger nærmest søknadens metode og behov:** `Edelen2018`, `Lohman2023`, `Benke2025`, `Nordic2023`, `FinansNorge2024VASK`, `CPR2024`, `ESPR2024`, `NOBB` og `EPD-Norge`. Start med originalfil/URL og lag evidenskort når presise steder kan leses.
2. **Grønne ramme- og sammenligningskilder:** `EN15978-2026`, `NS-EN16627`, `NFR_IPN2026`, `EC3`, `BKA2`, `EBA_EU2023`, `Billio2022` og `Kaza2014`. Brukes for rammer, sammenligning og avgrensning, ikke som erstatning for pilotbevis.
3. **Gule, relevante tilleggs- og metodekilder:** standardene, usikkerhetsmetodene, verktøyene, produktdata-/DPP-kildene og norske kontekstkilder. Åpne originalen før kort lages; prioriter dem som dekker dokumentasjonskvalitet, kilder og brukerbelastning.
4. **Kontrasterende og kritiske kilder:** finanssporet, byggskade-/konfliktsporet, konsortieinterne notater og markeds-/bransjetall. Behandles sist og bare der de forklarer avgrensning, usikkerhet eller et reelt motargument.
5. **Holdes utenfor til videre varsel:** `SA2018`, `Wiik2025`, udelte `SINTEFFag18` og alle kilder der bare en sekundær omtale er tilgjengelig.

## Fase-1 konklusjon

Utvalget består av **55 grønne eller gule registeroppføringer**. Det er nok til å planlegge ekstraksjon, men ikke nok til å skrive sporbare evidenskort: originalfiler eller stabile offisielle URL-er må inn før fase 2. Kildebibliotekets statusmarkeringer beholdes uendret; denne inventarfilen erstatter dem ikke.
