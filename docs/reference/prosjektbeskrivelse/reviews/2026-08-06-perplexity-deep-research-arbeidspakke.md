# Arbeidspakke: Perplexity Deep Research for Reduzer og manglende kilder

**Dato:** 2026-08-06  
**Status:** Klar for manuell bestilling – ikke kjørt  
**Eier av kildeport:** Lars  
**Berører:** Port A og D i grunnlagsarbeidet for v0.7

## 1. Formål

Arbeidspakken skal finne, identifisere og lenke til originalkilder som fortsatt
mangler i repoet. Den skal også gi en etterprøvbar, norsk konkurrentsammenligning
med særlig vekt på Reduzer.

Perplexity brukes som søke- og kartleggingsverktøy. Et Perplexity-svar er ikke
belegg i søknaden. Bare en identifisert original med direkte lenke og kontrollert
innhold kan bli kandidat til aktiv bruk.

Arbeidet skal svare på fire spørsmål:

1. Hva dokumenterer Reduzer selv, og hva er bekreftet av uavhengige eller
   akademiske kilder?
2. Hvilke originaler bak dagens kildeoppføringer kan faktisk finnes og åpnes?
3. Hvilke viktige kilder eller moteksempler mangler helt i dagens utvalg?
4. Hvilke setninger i v0.7 må få kilde, avgrenses eller stå som
   prosjekthypotese?

## 2. Styrende grunnlag

Les før søket:

- `docs/handoffs/41_codex_perplexity-inntak_og_kildepensjonering_handoff.md`
- `docs/handoffs/47_claude_v0.7-skrevet_og_kontrollrigg-funn_handoff.md`
- `.scratch/sintef-forskningsrapport-2026/research/perplexity-sjekkliste-k3-og-soa-v0.5.md`
- `research/source_inventory.md`
- `research/evidence_matrix.md`
- `docs/reference/ipn-kildebibliotek.md`
- `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.7.md`
- `docs/reference/prosjektbeskrivelse/reviews/2026-08-05-tilbakemeldingsregister-v0.6.md`
- `governance/source-blocklist.json`

Den eksisterende Perplexity-sjekklisten har 28 detaljerte kontrollpunkter.
Denne arbeidspakken erstatter ikke sjekklisten. Den prioriterer kjøringene,
utvider søket etter kilder som mangler i dagens utvalg og fastsetter
leveranseformatet.

## 3. Ufravikelige regler

- Ikke endre søknadstekst, kildebibliotek, kildefarge eller sperrepost i
  researchfasen.
- Skill alltid mellom leverandørpåstand, offentlig dokumentasjon,
  fagfellevurdert forskning og prosjektets egen slutning.
- Negativt funn skrives `IKKE DOKUMENTERT I DETTE SØKET`, aldri «finnes ikke».
- Bruk direkte lenke til originalen, ikke en Perplexity-lenke eller generell
  søkeresultatside.
- Registrer DOI, permanent publikasjonsside og PDF-lenke når de finnes.
- For betalingsmurer registreres både metadata-/DOI-lenke og eventuell lovlig
  åpen manusversjon. Ikke omgå tilgangskontroll.
- Et sammendrag eller en snippet teller ikke som lest fulltekst.
- Alle grønne kandidater skal kontrolleres manuelt før de kan brukes.
- `[Wiik2025]`, `[SA2018]`, `[Multiconsult2023DiBK]`, `[KD2024-Asplan]`,
  `[Bjørheim2026]`, `[Mecca2023]` og `[Ciroth2016]` beholder dagens sperre eller
  begrensning til Lars uttrykkelig beslutter noe annet.

## 4. Obligatorisk registrering per kilde

Hver rad skal inneholde:

| Felt | Krav |
| --- | --- |
| Kandidat-ID | Eksisterende kildenøkkel eller `NEW-###` |
| Full referanse | Forfatter/organisasjon, tittel, år og utgiver |
| Direkte lenker | Publikasjonsside, DOI og PDF/fulltekst hver for seg |
| Kildetype | Offentlig, standard, forskning, bransje, leverandør eller intern |
| Lesedybde | `METADATA`, `SAMMENDRAG`, `FULLTEKST` eller `IKKE ÅPNET` |
| Presis lokasjon | Side, tabell, figur, kapittel eller avsnitt |
| Støtter | Avgrenset påstand kilden faktisk støtter |
| Støtter ikke | Nærliggende eller sterkere påstand den ikke dekker |
| Geografi/utvalg | Land, bransjedel, byggtype, bedriftstype og periode |
| Konflikt/duplikat | Mulig alias, nyere utgave, erstatning eller motstrid |
| Resultatkode | Se kodene under |
| Søkespor | Søkestreng, dato og eventuelle databaser/domener |

Resultatkoder:

- `VERIFIED-FOR-CLAIM`
- `PARTIAL`
- `CONFLICT`
- `NEEDS-ORIGINAL`
- `NOT-FOUND-IN-SCOPE`
- `PROJECT-HYPOTHESIS`
- `NEW-CANDIDATE`

## 5. Kjøringsplan og godkjenningsporter

Deep Research kan bruke mer tid og kvote enn ordinære søk. Før hver batch skal
Lars bekrefte at den skal kjøres. Kontroller synlig kostnads-/kvoteinformasjon i
verktøyet før start. Kjør batchene i rekkefølge og stopp etter hver leveranse.

### Batch 1 – Reduzer og norske moteksempler

**Prioritet:** P0  
**Mål:** Dokumentere Reduzers faktiske omfang og teste om gapformuleringen i
v0.7 holder mot norske løsninger.

Undersøk:

1. Reduzers juridiske virksomhet, eierskap, NTNU-relasjon, historikk og status.
2. Dokumenterte funksjoner for anbud/tilbud, EPD, LCA/klimagassberegning,
   kostnader/LCC, vedlikehold, levetid, teknisk kvalitet, ombruk, datakvalitet,
   usikkerhet, vekting og sammenligning av alternativer.
3. Hvilke brukergrupper og prosjektfaser løsningen er laget for.
4. Hvilke datakilder og antall EPD-er som faktisk dokumenteres, med dato.
5. Akademiske publikasjoner, NTNU-prosjekter, offentlige piloter, kundecaser og
   uavhengige omtaler som beskriver eller evaluerer løsningen.
6. Om løsningen måler beslutningseffekt eller bare produserer beregninger.
7. Samme kriterier for SmartKalk Miljø, ORIS Contractors, One Click LCA, EC3,
   Madaster, Cobuilder/NOBB, Concular og andre norske løsninger søket avdekker.

**Viktig:** Fravær av dokumentasjon skal ikke registreres som fravær av
funksjonalitet.

**Leveranse:** ett konkurransekort for Reduzer, én sammenligningstabell og en
kort vurdering av hvilke formuleringer om nyhetsverdi som er dokumenterbare.

### Batch 2 – SMB, tilbudsfase og kundegrunnlag

**Prioritet:** P0  
**Mål:** Løse Port A uten å bruke løse anslag som «80–90 prosent».

Finn offentlige eller forskningsbaserte originaler for:

1. antall og andel norske bygg-/entreprenørbedrifter med under ti ansatte;
2. forskjellen mellom andel foretak, andel sysselsatte og andel omsetning;
3. bedriftenes tids-, kompetanse- og administrasjonsbelastning;
4. faktisk bruk av BIM, LCA, EPD, miljøsertifisering og produktdata i små
   entreprenørbedrifter;
5. hvordan tilbud sammenlignes og hvilke andre kriterier enn pris kundene
   forstår og bruker;
6. informasjonsasymmetri mellom entreprenør, profesjonell bestiller og
   privatkunde.

Prioriter SSB, Brønnøysundregistrene, NHO Byggenæringen, DiBK, DFØ,
Forskningsrådet, nordiske myndigheter og fagfellevurderte studier. Skill
byggenæringen samlet fra utførende entreprenører og håndverksbedrifter.

**Leveranse:** talltabell med definisjoner og år, evidenskort for atferds- og
kapasitetspåstander og anbefalt, nøktern problemformulering.

### Batch 3 – Standarder og datainfrastruktur i den aktive teksten

**Prioritet:** P0  
**Mål:** Dokumentere setningen i v0.7 om standarder, EPD, produktdata, FDV og
metoder.

Finn offisielle original- eller metadata-/omfangssider for:

- EN 15978:2026
- NS-EN 16627 / relevant gjeldende LCC-standard
- ISO 14040 og ISO 14044
- EN 15804+A2
- ISO 15686-5:2017
- NS-EN ISO 22057
- NS 3720 og TEK17 § 9-2, inkludert eventuell faktor 1,25
- CPR, forordning (EU) 2024/3110
- ESPR, forordning (EU) 2024/1781
- EU-taksonomi/DNSH der dette brukes
- NOBB, EPD-Norge/ECO Portal og FDV-relevante datakilder

For standarder bak betalingsmur skal rapporten ikke late som standardteksten er
lest. Registrer om bare tittel, omfang og status er kontrollert. Finn offentlige
veiledere som beskriver praktisk anvendelse, men hold dem atskilt fra selve
standarden.

**Leveranse:** en standard- og datakildematrise som viser hva hver kilde kan og
ikke kan brukes som belegg for.

### Batch 4 – Norske problem-, skade- og økonomikilder

**Prioritet:** P1  
**Mål:** Lokalisere originalene bak sentrale norske problempåstander og splitte
feilaktige samlekilder.

Kjør kontrollpunktene NO-01 til NO-08 fra den eksisterende sjekklisten, med
særlig vekt på:

- Multiconsult/DiBK og forholdet til KD2024/Asplan Viak;
- Bjørheim2026 splittet i separate kilder for konkurser, BDO-margin,
  UNION-kostnadstall og ombruk;
- Gullbrekken & Holme 2025 og underliggende datasett/rapport;
- Ingvaldsen 2008;
- EBA Norge-veilederen og «20 prosent uten merkostnad»;
- Finans Norge 2024;
- BKA2;
- NOBB, EPD-Norge, CIRPASS-2, Bygg21, KS2025, Herfjord2021,
  PlanGrid/FMI og SINTEF Fag 18/FutureBuilt/Resirqel som separate kilder.

Forsøk også å lokalisere `[SA2018]` og `[Wiik2025]`, men behold sperren selv om
en mulig omtale finnes. Gjenåpning krever original og Lars' beslutning.

**Leveranse:** originalregister, splittkart for samlekilder og liste over
påstander som fortsatt mangler belegg.

### Batch 5 – metode, usikkerhet og MCDA

**Prioritet:** P1  
**Mål:** Kontrollere metodekilder som i dag mangler fulltekst, DOI eller presis
lokasjon.

Kjør MET-01 til MET-06 fra den eksisterende sjekklisten. Dekk minst:

- Edelen & Ingwersen 2018;
- Weidema & Wesnæs 1996;
- Ciroth mfl.;
- Benke mfl. 2025;
- Lohman mfl. 2023;
- Mecca 2023;
- MCDM-oversikten fra 2025;
- primærlitteratur om rank reversal og om relevante absolutte
  verdifunksjoner faktisk reduserer problemet.

**Leveranse:** påstand–metode–kilde-tabell. Skill standard metodepraksis fra
metodevalg prosjektet ennå ikke har tatt.

### Batch 6 – finans, bank og mulige moteksempler

**Prioritet:** P2  
**Mål:** Avgrense hva forskning og regulering faktisk sier om bygningsdata og
kredittrisiko.

Kjør FIN-01 til FIN-07. Finn originaler for Kaza 2014, Billio 2022, An & Pivo
2020, EBA 2023, Bank of England-dokumentene, EEMI/DeliverEEM, Finance Norway
2018 og Multiconsult/Eika 2023. Søk aktivt etter moteksempler til prosjektets
forskningsgap.

**Leveranse:** evidenskjede som skiller energiytelse, teknisk tilstand,
byggskader, forsikringsskade, panteverdi, PD, LGD og lånepris.

### Batch 7 – åpent mangelsøk

**Prioritet:** P2  
**Mål:** Finne viktige kilder og verktøy som dagens register ikke kjenner.

Be Deep Research identifisere:

- nyere norsk/nordisk forskning fra 2023–2026;
- relevante pågående eller avsluttede FoU-prosjekter;
- norske verktøy for tilbud, kalkyle, produktvalg, LCA/LCC, FDV, ombruk og
  dokumentasjonskontroll;
- forskning på beslutningsstøtte til små entreprenører;
- kilder som motsier eller vesentlig begrenser VERIFIEDs problem- eller
  nyhetsverdipåstander.

Nye funn registreres som `NEW-CANDIDATE`. De flettes ikke inn i søknaden i
samme arbeidsøkt.

## 6. Masterprompt til Perplexity Deep Research

Bruk denne prompten som grunnmur. Sett inn bare én batch om gangen.

```text
Du gjennomfører kildekritisk deep research for en norsk IPN-søknad om
beslutningsstøtte i tilbudsfasen for små entreprenørbedrifter.

Oppdraget i denne kjøringen er:
[LIM INN ÉN BATCH FRA ARBEIDSPAKKEN]

Arbeidsregler:
1. Prioriter originalkilder: offentlige publikasjoner, standardorganisasjonenes
   offisielle sider, fagfellevurderte artikler, institusjonelle arkiver og
   leverandørens egen dokumentasjon for leverandørpåstander.
2. Perplexity-svar, søkeresultatsnutter og tredjepartsoppsummeringer er ikke
   tilstrekkelig belegg.
3. Oppgi direkte klikkbar URL til publikasjonsside, DOI og PDF/fulltekst hver
   for seg når de finnes.
4. Merk lesedybde for hver kilde som METADATA, SAMMENDRAG, FULLTEKST eller
   IKKE ÅPNET. Ikke skriv FULLTEKST dersom bare sammendrag, snippet eller
   metadata er lest.
5. Oppgi presis side, tabell, figur, kapittel eller avsnitt for hver påstand.
6. Skriv både hva kilden støtter og hva den ikke støtter.
7. Skill leverandørpåstander, uavhengig dokumentasjon og egen slutning.
8. Ikke konkluder at noe ikke finnes. Bruk formuleringen IKKE DOKUMENTERT I
   DETTE SØKET og oppgi søkestrenger, domener/databaser og dato.
9. Søk etter moteksempler og kilder som begrenser premisset, ikke bare
   bekreftende kilder.
10. Ikke foreslå kildefarge eller endre prosjektets kildestatus.

Returner:
A. Kort konklusjon med viktigste funn og usikkerheter.
B. En tabell med: kandidat-ID, full referanse, kildetype, direkte lenker,
   lesedybde, presis lokasjon, støtter, støtter ikke, geografi/utvalg,
   konflikt/duplikat og resultatkode.
C. En egen liste over nye kandidater som ikke var nevnt i oppdraget.
D. En egen liste over kilder som fortsatt ikke kunne identifiseres eller åpnes,
   med dokumentert søkespor.
E. En liste over setninger/påstander som bør avgrenses eller stå som hypotese.
```

## 7. Mottak og lagring av resultatene

Hver batch lagres urørt i en ny mappe:

```text
.scratch/research-intake/perplexity-deep-2026-08-06-bNN/raw/
```

Opprett samtidig:

- `manifest.yml` med filnavn, størrelse, SHA-256, mottakstid, batch og modell;
- `search-log.md` med formål, prompt, søkestrenger, dato og usikkerheter;
- `candidate-register.md` med tabellen fra seksjon 4;
- `not-found-log.md` for mislykkede identitets- og fulltekstsøk;
- `decision-queue.md` med saker Lars senere må godkjenne.

Direkte nedlastede originaler lagres separat fra Perplexity-rapporten. Det skal
være synlig om AI bare fant kilden, leste metadata/sammendrag eller faktisk
kontrollerte fulltekst.

## 8. Godkjenningsport etter hver batch

Batchen er ikke ferdig før følgende er kontrollert:

- alle viktige kilder har direkte klikkbar original- eller DOI-lenke;
- lesedybde er registrert ærlig;
- påstand og kilde har presis lokasjon;
- leverandørpåstand og uavhengig bekreftelse er skilt;
- mulige duplikater og aliaser er flagget;
- moteksempler og begrensninger er tatt med;
- manglende treff er dokumentert uten eksistenspåstand;
- ingen aktiv fil, kildefarge eller sperrepost er endret.

Etter kontroll kan Codex lage et forslag til oppdatering av kildebibliotek,
evidenskort, konkurrentfil og påstand–kilde-matrise. Lars godkjenner hvert
statusskifte før innfletting i søknad eller nettside.

## 9. Minimumsleveranse dersom tiden er knapp

Kjør bare batch 1–3. Det gir:

1. kontrollert Reduzer-sammenligning;
2. offentlig SMB-grunnlag;
3. klikkbare original-/omfangslenker til standardene og datakildene som allerede
   omtales i v0.7.

Batch 4–7 kan deretter kjøres etter verdi og gjenværende kvote.

## 10. Ikke-mål

- Ikke masseimporter alle treff til repoets aktive kunnskapsfiler.
- Ikke gjøre leverandørnettsteder til uavhengig belegg.
- Ikke bruke Deep Research til å fastsette forskningsmetode eller
  partneransvar.
- Ikke omskrive v0.7 i samme økt som kildesøket.
- Ikke sende forskningsresultater eller søknad eksternt.
- Ikke fjerne gamle kilder uten godkjent pensjoneringsbeslutning og sperrepost.
