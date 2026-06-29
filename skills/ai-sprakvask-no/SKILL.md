---
name: "ai-sprakvask-no"
description: "Bruk når norsk tekst skal av-KI-fiseres, klarspråkvaskes, stemmebevares eller norm-/kildekontrolleres før publisering."
---

# AI-språkvask NO

## Når du skal bruke skillen

Bruk denne når brukeren ber om:
- å fjerne KI-preg fra norsk tekst
- språkvask, klarspråk eller mer naturlig norsk
- kontroll av bokmål/nynorsk, anglifisering eller generisk KI-stil
- å bevare avsenderstemme etter omskriving
- kilde-/påstandskontroll i norsk tekst før publisering

Normal inngang er `anti_ai_sprakredaktor_no`. Bruk teamflyten bare når teksten skal publiseres eksternt, brukes i offentlig sektor, inneholder fakta/tall, er på nynorsk/blandet norm, eller har en tydelig personlig/organisatorisk stemme.

## Obligatoriske inndata

Hvis ikke brukeren allerede har gitt dette, gjør en rimelig antakelse og noter den kort:
- tekst
- målgruppe
- sjanger
- skriftspråk: bokmål eller nynorsk
- ønsket stemme
- hva som ikke må endres: fakta, sitater, juridiske formuleringer, begreper, kildekrav

Ikke stopp for spørsmål ved enkel språkvask. Spør bare hvis tekstens risiko er høy eller formålet er uklart.

## Arbeidsflyt

1. **Lås originalen.** Ikke endre fakta, tall, sitater eller rettslig/økonomisk betydning uten å markere risiko.
2. **Diagnose.** Finn KI-preg, anglifisering, normbrudd, repetisjon, overstruktur og generisk tone.
3. **Omskriv.** Gjør teksten konkret, norsk og målgruppetilpasset. Sett aktør og handling tydeligere.
4. **Stemmebevar.** Trekk tilbake formuleringer som blir for glatte, konsulentaktige eller fremmede for avsender.
5. **Norm- og kildeport.** Skill fakta, vurderinger og anbefalinger. Marker påstander som trenger kilde. Ikke finn opp kilder.
6. **Lever.** Gi omskrevet tekst først, deretter kort diagnose, risiko for meningsendring og åpne spørsmål.

## Outputformat

For vanlig bruk:

```yaml
summary:
  verdict: naturlig|noe_ki_preg|tydelig_ki_preg
  main_risks:
    - string
rewritten_text: string
ai_language_findings:
  - original: string
    problem: string
    suggested_fix: string
meaning_preservation_notes:
  - string
source_or_norm_flags:
  - string
open_questions:
  - string
```

For korte tekster kan du svare enklere:
- `Forslag:`
- `Dette endret jeg:`
- `Må sjekkes:`

## Kvalitetsregler

- Ikke gjør teksten mer "perfekt" enn den bør være.
- Ikke fjern nødvendige forbehold.
- Ikke forveksle formell fagspråk med KI-preg.
- Ikke påstå at teksten faktisk er skrevet av KI.
- Ikke bruk KI-deteksjon som bevis i eksamen, personalsak eller juksesak.
- Ikke legg inn falske personlige erfaringer for å gjøre teksten mer menneskelig.
- Ikke bruk KI-svar som kilde.
- I norsk offentlig språk: bruk `KI`, og bruk bindestrek i sammensetninger som `KI-systemer`.

## Når du skal eskalere

Escaler eller marker tydelig risiko ved:
- juridisk bindende tekst, enkeltvedtak, avtalevilkår eller anskaffelser
- medisinsk, finansiell, sikkerhetskritisk eller personalrettslig innhold
- tekst som brukes til anklage om juks eller vurdering av enkeltperson
- udokumenterte tall eller sterke påstander før publisering

## Teamroller ved krevende tekst

Les `references/agent_cards.md` når du trenger detaljer. Kortversjon:
- `ki_sprakdetektor_no`: diagnose, ikke full omskriving.
- `norsk_klarsprak_redaktor`: klarere tekst, aktør og handling frem.
- `stemmebevarer_no`: bevar avsenderens rytme, temperatur og særpreg.
- `norm_og_kildekontroll_no`: sluttport for norm, begreper, påstander og kilder.

## Eval før global/promotert bruk

Evalene ligger i `references/eval_cases_ai_sprak.md`. Skillen regnes som brukbar når den:
- flagger generisk KI-tekst uten å overdrive korte tekster
- gjør kommunal tekst mer aktiv uten å fjerne krav
- oppdager bokmål/nynorsk-blanding
- stopper påstander som trenger kilde
- bevarer personlig stemme når originalen har tydelig energi

