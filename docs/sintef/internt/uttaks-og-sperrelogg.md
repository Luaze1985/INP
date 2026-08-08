# Tørrkjøring: uttaks- og sperrelogg

Dato: 2026-08-03
Status: internt beslutningsgrunnlag — ingen statusendring er utført
Eier av gjenåpning: Lars

## Formål og regler

Dette er en foreslått sperrelogg for senere konsolidering. Den er ikke en ny
kildedom og endrer ikke `ipn-kildebibliotek.md`, portstatus eller aktiv tekst.
Identitet og alias beholdes for å hindre at utgåtte eller uavklarte kilder
importeres på nytt som nye kilder.

- **UTTATT-USIKKER / `original-required`:** ute av bærende bruk til en navngitt
  original er lokalisert, åpnet og presist kontrollert. Bare Lars kan gjenåpne.
- **ERSTATTET:** gammel nøkkel eller bærende rolle er sperret; beholdes som
  alias med peker til gjeldende nøkkel/kilde. Bare Lars kan oppheve sperren.
- **PENSJONERT:** permanent ute av aktive flater. Identitet, begrunnelse og
  erstatning beholdes. Bare Lars kan gjenåpne, også når regelen er
  `manual-only`.

## Foreslåtte sperreposter

| ID | Identitet og alias som beholdes | Foreslått behandling | Erstatning / tillatt restbruk | Aktiv forekomst og grunn | Gjenåpning |
|---|---|---|---|---|---|
| SP-01 | `[Wiik2025]`; Marianne Kjendseth Wiik; *Kostnadseffekten av klimatiltak i byggenæringen*; «SINTEF Notat 57» | **UTTATT-USIKKER / original-required** som uavhengig belegg | `[EBA_NO2023]` for et mulig, avgrenset 20 %-funn og `[KD2024]` for tidligfaserom, begge innen gjeldende kildeport. Wiik beholdes som konsortieinternt historisk arbeidsgrunnlag. | Kildebibliotek linje 145 og kildekart linje 463–468 parkerer notatet. Handoff 41 krever at identiteten bevares og at permanent pensjonering eller `original-required` vurderes; den avgjør ikke valget. | Original, vurdering av uavhengighet og Lars-beslutning. En funnet original gir ikke automatisk status som uavhengig belegg. |
| SP-02 | `[SA2018]`; Samfunnsøkonomisk analyse; *Konflikter i bygg- og anleggsnæringen*; «Rapport 4-2018» | **UTTATT-USIKKER / original-required** | Ingen bærende erstatning før originalen er åpnet. `[Harerusten2022]` kan stå som sekundært søkespor, ikke som belegg for 2,2 mrd. | Kildebibliotek linje 121 og kildekart linje 453–462 sier parkert; kildedom linje 24 sier grønn. Nyere Lars-beslutning gjelder operativt, men konflikten må beholdes. | Original + presis lokasjon + Lars-beslutning. |
| SP-03 | `[An2021]` | **ERSTATTET** alias | `[An2020]`; An & Pivo (2020), DOI `10.1111/1540-6229.12228`. Kun kommersiell eiendom/CMBS; 34 %-tallet krever fulltekst. | Kildedom linje 18 og 97–99. Gammel nøkkel gir feil år, DOI, populasjon og effektstørrelse. | Bare Lars; aliaset skal normalt aldri bli selvstendig kilde igjen. |
| SP-04 | `[Billio_SAFE261]`; SAFE Working Paper 261 | **ERSTATTET** alias | `[Billio2022]`, publisert tidsskriftversjon, DOI `10.1007/s11146-021-09838-0`. | Kildedom linje 20 og 102–103. Arbeidspapiret må ikke gjenimporteres som en separat bærende studie. | Bare Lars; kan kun gjenåpnes som historisk versjon, ikke ny kildeidentitet. |
| SP-05 | `[Harerusten2022]` i rollen «primærkilde for 2,2 mrd.» | **ERSTATTET** bærende rolle | `[SA2018]` er kandidat-original, men hele påstanden forblir blokkert av SP-02. Harerusten beholdes som sekundær henvisning. | Kildebibliotek linje 122 og kildedom linje 127–134/161–164 viser at masteroppgaven ikke inneholder primærberegningen. | Bare Lars etter at SP-02 er avklart. |
| SP-06 | `[Multiconsult2023DiBK]`; *Klimagassberegningsanalyse av fire referansebygg*; Multiconsult for DiBK 2023/2024 | **UTTATT-USIKKER / original-required** fra bærende bruk | Kan senere etableres som egen kilde eller dokumentert relasjon til `[KD2024]`; ikke slå sammen med `[Multiconsult2023]` om Eika Boligkreditt. | Brukes som 🟢 i K3 linje 24, 75–76, 120–125, 205, 263 og 449, men finnes ikke i kanonisk kildebibliotek. Perplexity-funn linje 33–49 viser identitetskonflikten. | Original, metadata, URL/DOI, presis lokasjon, biblioteknøkkel og Lars-beslutning. |
| SP-07 | `KD2024-Asplan`; Asplan Viak/DiBK-beregning av samlet klimafotavtrykk | **UTTATT-USIKKER / original-required** | Holdes separat fra `[KD2024]` til dokumentrelasjonen er dokumentert. | Perplexity-funn linje 35–49 og kildekart K-03 linje 569–574. Kilden finnes ikke som selvstendig oppføring. | Original + identitetsavstemming + Lars-beslutning. |
| SP-08 | `[Bjørheim2026]` som samlekilde; «Bisnode/Byggeindustrien/SINTEF» | **ERSTATTET** samlekildebruk og **UTTATT-USIKKER / original-required** for konkurstallet | Behold identiteten som kandidatspor for 1 583 konkurser, men ikke som aktivt belegg før konkursoriginal og presis lokasjon er registrert. Bruk separate spor `[BDO2025]`, `[UNION2025]` og en faktisk ombrukskilde. | K3 linje 30, 69–70, 104–109, 208, 286, 300/310 og 443 blander fire kilder. Perplexity-funnet peker mot et eget konkursstatistikk-/Byggeindustrien-spor, men registrerer ikke en entydig original her. | Bare Lars; hver del krever egen original og presis lokasjon. |
| SP-09 | `[Mecca2023]` prosentene 46/20/11/9 og «Rank Reversal» som samme belegg | **UTTATT-USIKKER / original-required** for bærende detaljbruk | Behold metadata som kandidat. Rank Reversal krever egen primærkilde eller merkes prosjektfaglig hypotese. | K3 linje 36, 169–176 og SoA linje 207–217/285–301 bruker bredere konklusjoner enn Perplexity-funn linje 196–205 støtter. Arbeidsloggene er internt uenige om fulltekståpning. | SINTEF-fulltekst, presis tabell/lokasjon og Lars-beslutning. |
| SP-10 | `[Ciroth2016]`; alle tittel-/utgavevarianter for pedigree-usikkerhetsfaktorer | **UTTATT-USIKKER / original-required** for eksakt formel/utgave | `[Weidema1996]`, `[ecoinvent]` og `[Ciroth2016]` skal forbli separate identiteter; ingen av dem arver den andres åpning. | Kildebibliotek linje 66–69 og Perplexity-funn linje 207–215 viser uåpnet/uklar identitet. | Original, korrekt bibliografi og presis formellokasjon + Lars. |
| SP-11 | «`Bjørheim2026` → BDO/UNION/ombruk»-aliaser som kan ligge i eldre tekst | **PENSJONERT** aliasrelasjon | Pek alltid til SP-08 og den faktiske separate kilden. | Relasjonen er dokumentert feil i Perplexity-funn linje 51–67 og handoff 41. Å beholde en sperre for selve feilrelasjonen hindrer ny sammenslåing. | `manual-only`; krever én original som faktisk dokumenterer hele pakken, samt Lars-beslutning. |

## Kilder som ikke foreslås sperret nå

- `[KD2024]`, `[EBA_NO2023]`, `[GullbrekkenHolme2025]`, `[BKA2]`,
  `[BDO2025]`, `[UNION2025]`, `[An2020]`, `[Benke2025]` og `[Lohman2023]`
  beholdes med dagens porter. Flere påstander må avgrenses eller
  originalverifiseres, men det er ikke grunnlag i denne tørrkjøringen for å
  pensjonere kildeidentitetene.
- `[Multiconsult2023]` i kildebibliotekets finansdel beholdes som en annen
  identitet enn SP-06.
- `[EBA_EU2023]` og `[EBA_NO2023]` beholdes som to separate kilder; generisk
  `[EBA]` skal fortsatt avvises.

## Dekning og konflikter

- **Dekning:** 11 foreslåtte sperreposter dekker alle eksplisitte identitets-
  og aliasproblemene i handoff 41, handoff 42, Perplexity-kildefunnene,
  kildebiblioteket, kildedommen og kildekartets K-01–K-03.
- **Åpen konflikt K-01:** `[SA2018]` er grønn i datert kildedom, men nyere
  parkert i kildebibliotek/kildekart. Ingen automatisk harmonisering er gjort.
- **Åpen konflikt K-02:** `[An2020]` gjelder CMBS/næringsbygg og 34 %-tallet
  mangler åpnet fulltekst; alias kan sperres uten å godkjenne tallet.
- **Åpen konflikt K-03:** `[KD2024]`, SP-06 og SP-07 kan være relaterte
  dokumenter, men relasjonen er ikke dokumentert godt nok til sammenslåing.
- **Provenienskonflikt:** Perplexity-leveransen er internt uenig om Mecca,
  Benke og Lohman ble åpnet. Eksisterende porter er ikke endret.

Ingen kilde er faktisk tatt ut, erstattet eller pensjonert av dette dokumentet.
