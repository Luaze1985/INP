---
title: Handoff 60 – Work-gjennomgang av SINTEF-innspill og Lars siste
date: 2026-09-28
status: ready
branch: claude/finpuss-v2.0-2026-09-27
mode: candidate-review
source_of_truth: GitHub
---

# Handoff 60 – Work-gjennomgang av SINTEF-innspill og «Lars siste»

## Formål

Gjennomfør en kontrollert vurdering av nye tekst- og metodeinnspill uten å miste kontroll over den gjeldende søknadskandidaten.

**GitHub-repoet er sannhetskilden.**
Den gjeldende søknadsteksten skal ikke erstattes av et nytt heldokument.

Arbeidet skal produsere **kandidater til endring**, ikke automatisk skrive om søknaden.

## Kildehierarki

Les i denne rekkefølgen:

1. `CONTEXT.md` – låste begreper og beslutninger.
2. `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v2.0.md` – gjeldende tekstkandidat.
3. `docs/reference/prosjektbeskrivelse/reviews/2026-09-27-finpuss-v2.0.md` – beslutninger og siste finpuss.
4. `docs/reference/prosjektbeskrivelse/innspill/2026-09-28-sintef-innspill.md` – viktig eksternt innspill, men ikke vedtak.
5. «Verified-Lars-siste-versjon.docx» – bruk som forslag-/analysebank. Den må være tilgjengelig i Work-sesjonen som fil eller eksplisitt import. Den er **ikke** sannhetskilde.

## Absolutt arbeidsregel

Ikke merge hele «Lars siste» inn i repo-kandidaten.

For hvert nytt forslag:

**repo-original → kandidat → begrunnelse/kilde → konsekvens → Lars beslutning → eventuelt senere innarbeiding**

Tillatte statuser:
- ÅPEN
- GODKJENT
- AVVIST
- PARKERT

Ingen kandidat får endre grunnteksten før den er GODKJENT.

## Hva gjennomgangen 28.09 allerede har vist

Den gjeldende repo-kandidaten er ca. 40 000 tegn. «Lars siste» er ca. 127 000 tegn og inneholder 64 markører med «INPUT KREVES». Det er derfor ikke en ferdig erstatning, men en omfattende analyse-/utviklingsversjon.

Vesentlige forskjeller som **ikke kan merges automatisk**:

### A. Forskningsbegrep
- Repo bruker den konkrete tredelingen: sammenlignbar / sammenlignbar med forbehold / for svakt grunnlag.
- «Lars siste» introduserer «sammenlignbarhetsgrense» som et gjennomgående fagbegrep.
- Dette kan være en god kandidat, men endrer prosjektets språklige kjerne og må besluttes eksplisitt.

### B. Case- og testdesign
- Repo: 6–8 tilbudscaser, tre holdes utenfor til reglene er låst.
- «Lars siste», hovedtekst: 6–8 caser, ca. 4–5 utvikling og 2–3 hold-out.
- «Lars siste», WP1: anslagsvis 8–12 case-sammenligninger, ca. 6–8 utvikling og 3–4 hold-out.
- Det finnes altså også intern variasjon i «Lars siste». Ikke velg tall uten beslutning.

### C. Arbeidspakkearkitektur
- Repo bruker AP1–AP7 og er portaltilpasset.
- «Lars siste» bruker WP1–WP7, tasks, leveranser og DG1–DG4.
- Behold AP-strukturen i repoet inntil annet er eksplisitt besluttet.
- DG-logikken kan vurderes som kandidat for å styrke milepæler/stoppunkter uten å skifte hele strukturen.

### D. Budsjett og ressurser
- Repo: 16,0 MNOK totalt, 8,0 MNOK støtte, 8,0 MNOK egenfinansiering.
- «Lars siste»: ca. 25,9 MNOK, ca. 20 400 timer, FoU-leverandør ca. 11,0 MNOK, Partner A/B.
- Dette er en reell konflikt, ikke språkvask. Ikke berør budsjett eller kostnadsfelt i tekstverksted-runden.

### E. Partnere og ansvar
- Repo navngir VIBS, SINTEF, D Takst, Byggmester Espeland og Norsk Byggtjeneste som aktuelle roller/kandidater.
- «Lars siste» bruker flere steder generiske «Partner A» og «Partner B».
- SINTEFs innspill 28.09 gir en konkret egenforståelse av AP1–AP7 og skal veie tungt ved vurdering av FoU-rollen.
- Ikke erstatt navngitte aktører med modellroller.

### F. VIBS/VERIFIED
- Repoets låste begrepsbruk beskriver VERIFIED som metode og unngår at søknaden gjør den til en eksisterende funksjon/plattformmodul.
- «Lars siste» bruker «VERIFIED-modul i VIBS» flere ganger.
- Dette er konflikt med gjeldende låst retning og må ikke innarbeides uten eksplisitt beslutning.

### G. Sterke metodekandidater fra «Lars siste»
Følgende bør vurderes som kandidater, fordi de kan styrke repoet uten å overta hele arkitekturen:
- tydeligere definert forsknings-/sammenlignbarhetsgrense,
- sterkere baseline-design mot dagens praksis,
- tydeligere forhåndslåsing før test på hold-out-caser,
- konkret definisjon av «kritisk feil»,
- eksplisitt vern mot overtilpasning/bekreftelsesbias,
- tydeligere skille mellom referansegrunnlag og VERIFIED-regler,
- sterkere operasjonalisering av brukerforståelse,
- tydeligere sporbarhet mellom datakvalitet, usikkerhet og tillatt konklusjonsstatus,
- mer eksplisitt gyldighetsområde og RESTRICT/STOP-logikk,
- klarere kompetanse- og kapasitetshull som faktisk må lukkes før innsending.

Disse skal høstes selektivt og oversettes til eksisterende AP-/portalstruktur.

## SINTEF – særskilt prioritet

SINTEF-innspillet er lagret i:
`docs/reference/prosjektbeskrivelse/innspill/2026-09-28-sintef-innspill.md`

Behandle det som **høy prioritet**, men fortsatt som innspill.

To hovedkandidater:

### S1 – bransjeproblemet tidligere
Vurder om sammendrag/problemforståelse tidligere skal forklare dokumentasjonsasymmetrien mellom:
- nyanskaffelse
- reparasjon
- rehabilitering
- ombruk
- eventuelt fortsatt bruk/utsatt utskifting

Poenget er ikke å love klimaeffekt, men å forklare hvorfor et mer sporbart sammenligningsgrunnlag kan hindre at godt dokumenterte nyanskaffelser får et kunstig beslutningsmessig fortrinn.

Behold eksisterende forsiktighet:
- teknisk egnethet først,
- lav klimabelastning alene definerer ikke beste valg,
- beregnede material-/klimaforskjeller er ikke realiserte effekter før faktiske valg er dokumentert.

### S2 – SINTEFs AP-rolle
Sammenlign SINTEFs egen forståelse mot dagens AP-er:
- AP1: faglig ansvar, forskningsplan og state of the art
- AP2: faglig ansvar
- AP3: faglig ansvar, usikkerhet og sensitivitetsanalyse
- AP4: dokumentasjon av regler/metode og etterprøvbare casekjøringer
- AP5: faglig ansvar og mulig analyse av feilmønstre
- AP6: vitenskapelig publisering
- AP7: faglig bidrag til rapportering

Kontroller spesielt:
- at AP4 ikke gir SINTEF ansvar for ordinær teknisk implementering,
- at AP7 ikke gjør SINTEF ansvarlig for prosjektadministrasjon,
- at formuleringen «endelig oppgavefordeling avklares etter tildeling» ikke svekker troverdigheten i søknadens rolle-/gjennomføringsplan.

## Work-økt – anbefalt sekvens

### Fase 1 – Differanseanalyse, ingen omskriving
Lag en matrise med:
- felt/avsnitt i repo
- nåværende budskap
- relevant innspill fra SINTEF
- relevant innspill fra «Lars siste»
- konflikt med låst beslutning? ja/nei
- kandidatverdi: høy/middels/lav
- beslutning kreves? ja/nei

Ikke rediger søknaden i denne fasen.

### Fase 2 – Prioriter maks 8 kandidater
Velg bare kandidatene som kan gi størst forbedring uten å rive opp arkitekturen.

Foreløpig prioritet:
1. Problem-/bransjeinnramming i sammendraget (SINTEF).
2. SINTEFs FoU-rolle og ansvar.
3. Baseline mot dagens praksis.
4. Metodelåsing før hold-out.
5. Kritisk feil / falsk sikkerhet.
6. Gyldighetsområde.
7. Referansegrunnlag vs VERIFIED-regler.
8. Brukerforståelse.

Budsjett, timer, Partner A/B og full WP-arkitektur skal ikke inn i denne tekstkandidatrunden.

### Fase 3 – Tekstverksted, 2–3 avsnitt per runde
For hver prioritert kandidat:
- vis repo-original,
- vis kandidat A med minst mulig endring,
- bare ved reell faglig avveining: kandidat B,
- oppgi hva kandidaten endrer faglig,
- oppgi eventuell konflikt/avhengighet,
- be Lars velge: A / B / ORIGINAL / PARKER.

Bruk raske endringer på rent språk. Bruk Ask bare når mening, ansvar, metode eller styrke i påstanden endres.

### Fase 4 – Beslutningslogg
Etter hver godkjenning:
- registrer kandidat-ID,
- felt,
- beslutning,
- kort begrunnelse,
- kilde: SINTEF / Lars siste / repo-intern,
- berørte felt,
- om endringen krever senere samsvarsendring i AP/risko/kompetanse.

Ikke skriv inn i hovedkandidaten før en liten sammenhengende gruppe av endringer er godkjent.

### Fase 5 – Kontrollert innarbeiding
Når 5–10 kandidater er godkjent:
- lag én separat kandidatgren/commit,
- oppdater bare de berørte tekstfeltene,
- ikke endre budsjett/AP-kostnader uten eksplisitt bestilling,
- kjør repoets eksisterende tester/gater,
- vis diff før merge/PR.

## Felt som skal behandles som tekst først

Høy prioritet:
- Sammendrag
- Kunnskapsbehov og mål
- FoU-metoder og -aktiviteter
- Innovasjonen
- Samfunnseffekter
- Prosjektgruppens kompetanse
- Styring og roller
- Risiko, men bare der metodeendringer krever konsistens

Lavere prioritet / vent:
- Gjennomføringsplanens budsjettlinjer
- Kostnadsspesifikasjoner
- Ressursfordeling
- Partnerøkonomi
- Portal-/skjemadata
- endelig AP/WP-arkitektur

## Stoppskilt

Work skal stoppe og be om beslutning før den gjør noe som:
- endrer totalbudsjett eller støttebeløp,
- endrer caseantall,
- bytter AP-struktur til WP-struktur,
- introduserer «VERIFIED-modul i VIBS» som ny låst retning,
- endrer partnerstatus eller formelt ansvar,
- gjør SINTEF til arbeidspakkeleder/formell samarbeidspartner uten grunnlag,
- gjør klima/materialeffekt til dokumentert realisert effekt,
- gjenåpner tidligere låste beslutninger uten å vise konflikten.

## Ønsket leveranse fra første Work-pass

Ikke en ny søknad.

Lever:
1. én differansematrise,
2. maks 8 kandidatkort,
3. anbefalt behandlingsrekkefølge,
4. liste over reelle beslutninger Lars må ta,
5. liste over ting som kan forbedres direkte uten beslutning,
6. ingen endringer i hovedteksten før Lars har valgt kandidatene.

## Kort startprompt til Work

```
GitHub-repoet Luaze1985/INP er sannhetskilden. Les Handoff 60 og kildene i oppgitt rekkefølge. Bruk den vedlagte «Verified-Lars-siste-versjon.docx» som forslag-/analysebank, ikke som ny baseline.

Første pass skal ikke skrive om søknaden. Lag en differansematrise og maks åtte prioriterte tekst-/metodekandidater. SINTEF-innspillet 28.09 er høy prioritet. Bevar AP-strukturen, dagens budsjett og låste begreper inntil jeg eksplisitt godkjenner noe annet.

Arbeid som Tekstverksted: små kandidater, original synlig, Ask bare ved reelle beslutninger. Ingen full rewrite.
```
