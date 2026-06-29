# Gemma all-source audit summary

Reports counted: 18
Reports ok=true: 9
Reports ok=false: 9
Flagged source keys: 16

## Flagged rows

### [An2020]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-11.gemma.json`
- Reason: Kilden viser statusdrift og historisk inkonsistens (tidligere listet som [An2021]). Viktigere er at den inneholder et spesifikt kvantitativt tall ('34 %-tallet') som krever verifisering i fulltekst/akseptert manus før det kan brukes bærende. Dette utgjør en kritisk vurdering av dataenes nøyaktighet.
- Recommended action: needs_professional_review: Verifiser kildens fulle tekst og aksepterte manus for å bekrefte 34 %-tallet, samt løs opp i nøkkelinkonsistensen ([An2021] vs. [An2020]).

### [CPR2024]
- Report: `.scratch\gemma4-source-consistency\all-sources\batch-01.gemma.json`
- Reason: Selv om kilden er grønn (🟢), indikerer bruksnotatet i kanoniske dokumenter at anvendelsen ('DPP umoden for bygg') krever en vurdering av teknisk/juridisk egnethet som overgår standard statusdrift. Dette faller inn under juridisk/teknisk vurderingsbehov.
- Recommended action: needs_professional_review: Vurder om 'DPP umoden for bygg' kan brukes i en spesifikk kontekst, eller om det kreves oppdatering av anvendelsesområdet.

### [Ciroth2016]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-07.gemma.json`
- Reason: Kilden er markert gul (🟡), noe som indikerer forbehold/potensiell bruk. Imidlertid har den ingen treff i kildedommen eller direkte nøkkelbruk, noe som tyder på potensiell statusdrift eller at kilden er utdatert.
- Recommended action: Bekreft behovet for denne kilden og vurder om gul-statusen fortsatt er relevant uten dokumentasjon av bruk.

### [EEMI]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-07.gemma.json`
- Reason: Kilden er markert gul (🟡), noe som indikerer forbehold/potensiell bruk. Imidlertid har den ingen treff i kildedommen eller direkte nøkkelbruk, noe som tyder på potensiell statusdrift eller at kilden er utdatert.
- Recommended action: Bekreft behovet for denne kilden og vurder om gul-statusen fortsatt er relevant uten dokumentasjon av bruk.

### [EN15804]
- Report: `.scratch\gemma4-source-consistency\all-sources\batch-01.gemma.json`
- Reason: Kilden har status Gul (🟡), som ifølge repo-reglene kun kan brukes med forbehold. Dette må sikres i all dokumentasjon.
- Recommended action: Sjekk at alle sitater fra denne kilden eksplisitt inkluderer et forbehold om dens gyldighet/begrensninger.

### [GullbrekkenHolme2025]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-04.gemma.json`
- Reason: Kilden er kritisk for å etablere problembeskrivelsen (10–30 mrd NOK/år) og er markert som Gul (🟡). Dette representerer en statusdrift da den støtter sentrale økonomiske påstander, men krever forbehold. Statusen avhenger av ekstern tilgjengelighet (SINTEF fulltekst → 🟢).
- Recommended action: needs_professional_review: Vurder om de økonomiske tallene kan hentes fra en annen kilde med grønn status, eller om påstanden må formuleres med et tydelig forbehold inntil kilden er bekreftet (🟢).

### [Harerusten2022]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-08.gemma.json`
- Reason: Kilden er merket sekundær (🟡) og brukes til å bære et sentralt tall (2,2 mrd NOK/år). Kildedommen indikerer at en primærkilde med grønn status ([SA2018]) er tilgjengelig for dette påstået.
- Recommended action: Erstatt [Harerusten2022] med [SA2018] i teksten der det bærende tallet brukes.

### [ISO14040]
- Report: `.scratch\gemma4-source-consistency\all-sources\batch-01.gemma.json`
- Reason: Kilden har status Gul (🟡), som ifølge repo-reglene kun kan brukes med forbehold. Dette må sikres i all dokumentasjon.
- Recommended action: Sjekk at alle sitater fra denne kilden eksplisitt inkluderer et forbehold om dens gyldighet/begrensninger.

### [ISO15686-5]
- Report: `.scratch\gemma4-source-consistency\all-sources\batch-01.gemma.json`
- Reason: Kilden har status Gul (🟡), som ifølge repo-reglene kun kan brukes med forbehold. Dette må sikres i all dokumentasjon.
- Recommended action: Sjekk at alle sitater fra denne kilden eksplisitt inkluderer et forbehold om dens gyldighet/begrensninger.

### [MCDM2025]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-02.gemma.json`
- Reason: Kilden er markert 🔴 (Rød) og er eksplisitt merket som 'ikke siterbar' i kildebiblioteket. Dette indikerer en klar statusdrift, da den ikke kan brukes til å underbygge påstander.
- Recommended action: Fjern eller oppdater denne kilden fullstendig, da dens nåværende status gjør den uegnet for sitering.

### [Mecca2023]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-13.gemma.json`
- Reason: Kilden er markert som gul (🟡) i både kildebiblioteket og kanoniske dokumenter. Imidlertid viser siteringsdokumentet at de kvantitative funnene fra denne kilden er 'Bekreftet' (🟢), noe som indikerer en potensiell statusdrift mellom kildens generelle brukbarhet og det spesifikke innholdets styrke.
- Recommended action: Vurder å oppdatere kildebibliotekstatusen fra gul til grønn, eller legg inn et tydelig forbehold i teksten som anerkjenner at selv om kilden er merket gul, er det spesifikke funnet bekreftet.

### [NOBB]
- Report: `.scratch\gemma4-source-consistency\all-sources\batch-05.gemma.json`
- Reason: Kilden har status 🟡 (Gul) men brukes som et bærende datagrunnlag for flere kritiske påstander i hoveddokumentene (F2, WP1). Dette representerer en potensiell statusdrift der kildebegrensningen kan undergrave dokumentets troverdighet.
- Recommended action: Needs_professional_review: Vurder om det er nødvendig med et midlertidig unntak eller skjerpet formulering i alle seksjoner som benytter denne kilden, for å ivareta reservasjonen knyttet til gul status.

### [OneClickLCA]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-01.gemma.json`
- Reason: Kilden er markert som gul og sekundær, men den brukes ikke i de kanoniske dokumentene som ble vurdert. Dette indikerer potensiell statusdrift eller at kilden er overflødig for det nåværende omfanget.
- Recommended action: Vurder å nedgradere statusen til 'Pause' eller fjerne den fra aktive kilder, med mindre det foreligger planlagt fremtidig bruk.

### [RICS-WLC]
- Report: `.scratch\gemma4-source-consistency\all-sources\batch-01.gemma.json`
- Reason: Kilden har status Gul (🟡), som ifølge repo-reglene kun kan brukes med forbehold. Dette må sikres i all dokumentasjon.
- Recommended action: Sjekk at alle sitater fra denne kilden eksplisitt inkluderer et forbehold om dens gyldighet/begrensninger.

### [Refleksjonsnotat2026]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-05.gemma.json`
- Reason: Kilden er merket som 🔴 (Ikke siterbar i søknad), men den brukes til å støtte primærsitatene. Dette utgjør en klar statusdrift/misbruk av kilde.
- Recommended action: Fjern all bruk og referanser til denne kilden fra alle dokumenter umiddelbart.

### [Wiik2025]
- Report: `.scratch\gemma4-source-consistency\all-sources\retry\retry-06.gemma.json`
- Reason: Kilden er konsistent markert som parkert/utilgjengelig (🟡 ⏸) fordi det underliggende SINTEF Notat 57 ikke finnes i åpne registre. Dette representerer en vedvarende avhengighet av uverifisert, internt materiale.
- Recommended action: Bekreft at betingelsen for gjeninnsetting (SINTEF publiserer notatet) fortsatt er gyldig. Hvis ikke, må kilden forbli parkert og alle referanser fjernes fra aktiv tekst.
