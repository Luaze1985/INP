# MASTER VERIFIKASJONSSPESIFIKASJON (VERIFIED IPN-SØKNAD OG NETTSIDE)

**Dato:** 2026-08-08  
**Status:** Konsolidert hovedspesifikasjon for kildekontroll, terminologi, formelle beslutninger og AI-agentverifisering.

---

## 1. Hva VERIFIED er (og hva det IKKE er)

- **HVAD DET ER:** VERIFIED er et selvstendig forsknings- og utviklingsprosjekt (IPN) for Norges forskningsråd (NFR). Prosjektet utvikler og tester en forskningsbasert beslutningsmodell som samler klimadata, levetid, utslipp og kvalitet til én forklarbar verdiscore i tilbudsfasen.
- **HVAD DET IKKE ER:** VERIFIED er **IKKE** VIBS-produktet. Produktkoden hører til `vibs-boligpass/`. Ordet `VIBS` skal **ALDRI** forekomme i VERIFIED sine søknadstekster eller på den offentlige statussiden.
- **IKKE BKA2 / VEGARD KNOTTEN:** BKA2 var et tilstøtende initiativ i et tidlig arbeidsnotat. Det skal **IKKE** være med i VERIFIED-teksten.

---

## 2. Konsoliderte Styringsbeslutninger (F-03, F-12, F-21, F-28, F-35, F-36)

| ID | Tema | Vedtatt regel / Praksis |
| :--- | :--- | :--- |
| **F-03** | Partnernavn | **Ingen firmanavn på partnere.** Kun uformell interesse foreligger. Omtal **kun partnertyper** (f.eks. *«forskningspartner», «utførende entreprenører», «finans og forsikring», «kommunale pilotarenaer»*). Ingen firmanavn skal ramses opp før skriftlig LOI/avtale er låst. |
| **F-12** | VIBS-rolle | **VIBS-plattformen er fjernet.** VERIFIED omtales kun som den uavhengige FoU-beslutningsmodellen som utvikles og testes. |
| **F-21** | Bærekraftsmål | Bærekraftsmål **12.5** (redusere avfallsmengde gjennom forebygging, gjenbruk og ombruk) er fastslått som sekundært bærekraftsmål under V1. |
| **F-28 / F-36** | Økonomisk mekanikk | V3-overskriften er *«Økonomiske virkninger og bankrelevans»*. V3 beskriver den kvalitative økonomiske mekanismen i tre ledd uten uverifiserte talløfter. |
| **F-35** | Kvalitet & Kjønn | K4 inneholder et eget avsnitt om deltakersammensetning og kjønnsperspektiv i pilotene (jf. NFR §10.7/§10.5). |

---

## 3. Kildedisiplin og Source Guard (Ufravikelige Kilderegler)

1. **Sannhetsport-statuser:**
   - 🟢 **Primær åpnet:** Fulltekst lest, verifisert og kontrollert mot original (kan stå alene).
   - 🟡 **Sterk, men ikke primærverifisert:** Åpnet av fagmiljø/fagkilde, men venter på SINTEFs primærkontroll (midten av august 2026).
   - 🔴 **Bare søketreff / ubekreftet:** Kan IKKE bruke som bærende søknadspåstand.
   - ⏸ **Parkert kilde:** Tatt helt ut av søknadsprosaen til kilden er funnet og lokalisert.
2. **Sperret liste (Source Blocklist):**
   - `Wiik2025` (SINTEF Notat 57) $\rightarrow$ PARKERT (⏸). Skal ALDRI brukes i prosa.
   - `SA2018` (2,2 mrd kr konfliktkostnad) $\rightarrow$ PARKERT (⏸). Skal ALDRI brukes i prosa.
   - `Mecca2023` / `Ciroth2016` $\rightarrow$ Krever originalkilde før metodepåstander kan brukes som bevis.
   - `Bjørheim2026` $\rightarrow$ Skal ALDRI brukes som samlekilde for BDO/UNION. Kun SSB/Brønnøysundregistrene gjelder for konkurstall.

---

## 4. Terminologiske og Ontologiske Guardrails

```text
+-----------------------+-----------------------+-------------------------------------------------------+
| BRUK RIKTIG BEGREP    | FORBUDT / VAGT BEGREP | BEGRUNNELSE                                           |
+-----------------------+-----------------------+-------------------------------------------------------+
| Løsningsvalg          | Produktvalg           | Løsningen omfatter produkter, montering, levetid      |
|                       |                       | og vedlikehold.                                       |
| Beslutningsstøtte     | Automatisk valg /     | VERIFIED anbefaler aldri automatisk. Entreprenøren    |
|                       | Svart boks            | beholder det faglige ansvaret.                        |
| Entreprenør & Kunde   | Bruker / Brukeren     | Spesifiser hvem som gjør hva (tømrer vs. boligkjøper).|
| Tilbudsfasen          | Byggeplass /          | Valgene tas og prissettes i tilbudsfasen før          |
|                       | Prosjektering         | prosjektet låses.                                     |
+-----------------------+-----------------------+-------------------------------------------------------+
```

---

## 5. Problemstillingen i Tilbudsfasen (Tre-leddsmodellen)

Tekst som beskriver utfordringen i tilbudsfasen MÅ eksplisitt dekke alle tre ledd:

1. **Entreprenørens utfordring:** Mindre bedrifter (91,2 % har færre enn 10 ansatte jf. SSB 2026) har høy fagkompetanse, men mangler tid og spesialistverktøy til tunge livsløpsanalyser (LCA/LCC) under tilbudspresset.
2. **Kundens utfordring:** Kunden ser kun pris på tilbudene. De kan ikke sammenligne hva et dyrere tilbud gir i lavere strømregning, lengre levetid, lavere vedlikehold eller mindre fuktrisiko.
3. **Møtepunktet i tilbudsfasen:** Når forskjellene er usynlige for kunden, vinner det billigste tilbudet på papiret — selv om det koster mer over tid.

---

## 6. Språkport og Rytmekontroll (5-stegs validering)

1. **Pass 1 — Fortellerstemme:** Én konsekvent fortellerstemme. «Prosjektet» eller «VERIFIED» er aktør; ingen «du» eller interne selvinstrukser.
2. **Pass 2 — Kontrast og KI-rytme:** 0 maskintreff på svulstige fyllord (*«revolusjonere», «banebrytende», «synergi»*).
3. **Pass 3 — Notat- og promptlekkasje:** Ingen interne instrukser, filstier eller utlysningskommentarer i offentlig tekst.
4. **Pass 4 — Modalkontroll («skal»-tetthet):** Ordet «skal» brukes kun om bindende etikk/do-no-harm-regler. Prosjektaktivitet skrives i presens (*«modellen samler», «prosjektet undersøker»*).
5. **Pass 5 — Høytlesing:** Sjekk at rytmen er naturlig og enkel å lese.

---

## 7. Verifiseringsprompter for testing i andre AI-agenter

### Prompt for kvalitetskontroll av tekst:
```text
Du er en streng auditor for IPN-prosjektet VERIFIED. Sjekk følgende tekst mot disse 5 reglene:

1. VIBS-FORBUD: Inneholder teksten ordet "VIBS"? (Hvis JA -> FEIL. Skal ut).
2. PARTNER-FORBUD: Inneholder teksten firmanavn på partnere? (Hvis JA -> FEIL. Kun partnertyper jf. Beslutning F-03).
3. BKA2-FORBUD: Er BKA2 eller Vegard Knotten nevnt? (Hvis JA -> FEIL. Skal ut).
4. AKTØRSJEKK: Er problemet i tilbudsfasen beskrevet for BÅDE entreprenøren og kunden?
5. SPERREKILDE-FORBUD: Er Wiik2025, SA2018 eller udokumenterte påstander brukt?

Rapporter: PASS eller FAIL med begrunnelse.
```

---

## 8. Sjekkliste for Sluttverifisering

- [x] **`VIBS`** er 100 % fjernet fra tekster og nettside.
- [x] **`BKA2`** og Vegard Knotten er 100 % fjernet.
- [x] Firmanavn på partnere er erstattet med **partnertyper**.
- [x] Tilbudsfasen er etablert som arenaen for valg.
- [x] Kundens og entreprenørens utfordringer er beskrevet parallelt.
- [x] `python tools/source_guard.py scan --path site/mockup/index.html` $\rightarrow$ **`PASS (0 treff)`**.
- [x] `python tools/source_guard.py scan --path docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.7.md` $\rightarrow$ **`PASS (0 treff)`**.
- [x] `pytest` $\rightarrow$ **17/17 passed**.
