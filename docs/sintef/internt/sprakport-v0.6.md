# Språkport for søknadskandidat og sannhetsserum v0.6

Dato: 2026-08-04

Status: obligatorisk kontroll før opprettelse og godkjenning av `v0.6`
Gjelder: samlet søknadskandidat, K3-sannhetsserum og senere nettsidekandidat

## Formål

Språkporten skal hindre at teksten får KI-preg, arbeidsnotatpreg eller en
fortellerstemme som diskuterer med seg selv. Søknaden skal leses som én samlet
faglig framstilling skrevet for en ekstern evaluator.

Porten vurderer språk og framstillingsform. Den erstatter ikke kildeporten.

## 1. Blokkerende språkformer

Et uavklart treff i disse kategoriene stopper kandidaten.

### Konstruert kontrast

Unngå standardformen «ikke A, men B» og varianter som gir teksten en mekanisk
argumentasjonsrytme:

- «ikke bare A, men også B»;
- «det betyr ikke A. Det betyr B»;
- «poenget er ikke A. Poenget er B»;
- gjentatte «selv om A, er B»-konstruksjoner brukt som retorisk oppskrift.

Skriv hovedpåstanden direkte.

**Unngå:** «VERIFIED skal ikke velge automatisk, men vise alternativene.»
**Skriv:** «VERIFIED skal vise alternativene med begrunnelse og synlig
usikkerhet. Entreprenøren beholder det faglige ansvaret.»

### Metatekst og selvinstruksjon

Følgende hører ikke hjemme i søknadsprosa eller sannhetsserumets fagtekst:

- «dette notatet», «denne teksten» eller «i denne versjonen»;
- «vi skal nå», «neste steg», «må rettes» eller «må avklares»;
- instruksjoner til Lars, SINTEF, en agent eller en senere skribent;
- omtale av prompt, Perplexity, Codex, Worker, review eller agentkjøring;
- sjekklister, avkryssingsbokser og produksjonsinstruksjoner inne i fagteksten.

Åpne forhold samles i en egen, tydelig merket kontrollseksjon. De blandes ikke
inn i argumentasjonen.

### Dialog mellom fortellerstemmer

Teksten skal ikke ligne en samtale mellom to KI-er eller mellom en KI og egne
notater. Følgende er varselsignaler:

- et spørsmål som umiddelbart besvares av teksten uten faglig behov;
- skifte mellom «vi», «prosjektet», «du» og en instruerende tredjeperson;
- påstander som kommenteres av en ny stemme i neste setning;
- gjentatte korreksjoner som «egentlig», «derimot», «samtidig» og «likevel»;
- forklaringer av hvorfor teksten selv har valgt en formulering.

Søknaden bruker «prosjektet» eller «VERIFIED» som aktør. «Vi» brukes bare når
det er nødvendig og konsekvent i en hel seksjon. «Du» brukes aldri.

### Generisk KI-språk og overdrivelse

Disse ordene og formene krever konkret begrunnelse eller omskriving:

- «helhetlig», «robust», «banebrytende», «transformativ» og «unik»;
- «krystallklart», «enorm», «avgjørende» og «revolusjonerende»;
- «i en tid der», «det er viktig å merke seg» og «på den ene siden»;
- absolutte fraværspåstander som «ingen forskning finnes» eller «ingen andre
  gjør dette»;
- lange rekker av abstrakte substantiver uten tydelig aktør og handling.

Fagbegreper som «fuktrobusthet» omfattes ikke av forbudet mot det generiske
adjektivet «robust».

## 2. Påkrevd skrivemåte

Hvert avsnitt skal:

1. starte med en faglig påstand eller et konkret prosjektvalg;
2. ha én tydelig hovedidé;
3. plassere kilde og avgrensning nær påstanden;
4. skille dokumentert kunnskap fra hypotese og testmål;
5. bruke aktivt subjekt der ansvar eller handling er relevant;
6. avsluttes uten å forklare tekstens egen skriveprosess.

Usikkerhet skrives direkte:

- «Originalen er ikke kontrollert.»
- «Resultatet gjelder fire referansebygg.»
- «Sammenhengen skal undersøkes i pilot.»
- «Funksjonen er ikke dokumentert i det undersøkte materialet.»

## 3. Fem obligatoriske kontrollpass

### Pass 1 – fortellerstemme

- Én stemme gjennom hele dokumentet.
- Ingen selvinstruksjon eller samtale med egne notater.
- Ingen rolleblanding mellom søker, kontrollør og senere godkjenner.

### Pass 2 – kontrast og KI-rytme

- Søk etter «ikke … men», «ikke bare», «det betyr ikke» og «poenget er ikke».
- Skriv hovedbudskapet direkte.
- Kontroller gjentatte treledd, parallelle setninger og mekaniske overganger.

### Pass 3 – notat- og promptlekkasje

- Fjern agentnavn, verktøynavn, arbeidsstatus og produksjonsinstruksjoner fra
  fagteksten.
- Flytt nødvendige åpne punkter til en egen kontrollseksjon.
- Fjern avkryssingsbokser, TODO-er og «senere agent»-formuleringer.

### Pass 4 – kilde og styrkegrad

- Kontroller at sikkerheten i språket følger lesetilgangen.
- Fjern absolutte gap- og markedspåstander.
- Kontroller at prosjektmål ikke framstår som dokumenterte effekter.

### Pass 5 – høytlesing og sluttkontroll

- Les avsnittene som sammenhengende prosa, ikke som separate KI-svar.
- Kontroller variasjon i setningslengde uten kunstig rytme.
- Fjern gjentakelser som bare oppsummerer forrige setning.
- Godkjenn først når teksten høres ut som én fagperson med ett formål.

## 4. Maskinell forhåndskontroll

Følgende søk kjøres på hver kandidat før menneskelig lesing:

```powershell
rg -n -i --pcre2 "ikke .{0,100},? men|ikke bare .{0,100} men|det betyr ikke|poenget er ikke" <fil>
rg -n -i --pcre2 "denne teksten|dette notatet|kandidatnotat|review|kontrollspor|Perplexity|Codex|agent|Worker" <fil>
rg -n -i --pcre2 "TODO|\[AVKLAR|\[SETT INN|må rettes|skal rettes|neste steg" <fil>
rg -n -i --pcre2 "\bhelhetlig\b|\brobust\b|banebrytende|transformativ|krystallklart|revolusjonerende|det er viktig å merke" <fil>
rg -n -i --pcre2 "ingen (empirisk |publisert )?(forskning|litteratur|konkurrent|verktøy)|ingen andre" <fil>
```

Treff er en kontrollkø, ikke automatisk bevis på dårlig språk. Hvert treff skal
enten omskrives eller få en kort, faglig begrunnelse i kontrollrapporten.

## 5. Baseline før v0.6

### Samlet søknadskandidat v0.5

- Ingen treff på de eksplisitte «ikke A, men B»-mønstrene i forhåndssøket.
- Ingen agent- eller promptrest ble funnet.
- Ett avklaringsavsnitt krever manuell vurdering, men beskriver en reell faglig
  port og kan omskrives uten metatekst.

### K3-sannhetsserum v0.5

- Dokumentet omtaler seg selv som kandidatnotat og inneholder intern
  produksjonsstatus.
- En Worker-signatur og review-begreper ligger i fagteksten.
- Flere formuleringer hevder at ingen litteratur eller metode finnes.
- Teksten bruker generiske styrkeord og forklarer flere steder sin egen rolle.
- Fortellerstemmen veksler mellom faglig framstilling, kontrollør og
  produksjonsnotat.

K3-sannhetsserumet krever derfor en full språk- og strukturkontroll. Det skal
ikke kopieres mekanisk til `v0.6`.

## 6. Godkjenningsregel

En `v0.6`-kandidat kan opprettes når denne språkporten finnes. Kandidaten kan
godkjennes når:

- alle fem kontrollpass er gjennomført;
- maskinelle treff er løst eller begrunnet;
- kildeporten er kontrollert separat;
- teksten ikke inneholder agentdialog, selvinstruksjon eller arbeidsnotater;
- Lars har godkjent den samlede vurderingen.
