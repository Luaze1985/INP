# VERIFISERINGSPAKKE FOR AI-AGENTER (IPN VERIFIED)

**Dato:** 2026-08-08  
**Formål:** Instrukser, sjekkregler og sperrekriterier til bruk ved testing eller tekstgenerering i andre AI-agenter (Claude Code, Antigravity, OpenAI Codex m.fl.).

---

## 1. Ufravikelige Prosjektregler (Sperre- og Navneregler)

### 🔴 ABSOLUTTE FORBUD
1. **INGEN OMTALE AV VIBS:**  
   VERIFIED er et selvstendig FoU-prosjekt for Norges forskningsråd (IPN). VIBS er produktplattformen i et annet repo (`vibs-boligpass/`). Ordet `VIBS` skal **ALDRI** forekomme i VERIFIED sin søknadstekst eller på den offentlige statussiden.
2. **INGEN BKA2 ELLER VEGARD KNOTTEN:**  
   BKA2 og Vegard Knotten var tilstøtende kildereferanser fra et eldre notat og skal **IKKE** være med i VERIFIED sin tekst.
3. **INGEN BEKREFTEDE FIRMANAVN PÅ PARTNERE (Beslutning F-03):**  
   Deltakelse er foreløpig og uformell. Skriv **aldri** at firmaer som *NorDan, Flekkefjord Sparebank, Farsund kommune, BEWI eller Byggtjeneste* er bekreftede partnere. Omtal dem **kun som partnertyper** (f.eks. *«forskningspartner», «utførende entreprenører», «finans og forsikring», «kommunale pilotarenaer»*).
4. **INGEN BRUK AV SPERREDE KILDER SOM BEVIS:**  
   - `Wiik2025` (SINTEF Notat 57) $\rightarrow$ PARKERT (⏸). Skal ikke brukes.
   - `SA2018` (2,2 mrd i konfliktkostnad) $\rightarrow$ PARKERT (⏸). Skal ikke brukes.
   - `Mecca2023` / `Ciroth2016` $\rightarrow$ Krever originalkilde før metodepåstander kan brukes bærende.
   - `Bjørheim2026` (SP-08, sperret 2026-08-03) $\rightarrow$ Brukes kun for samlet konkurstall (1 583), aldri som samlekilde for BDO/UNION. ⚠️ Selv konkurstallet krever egen original og presis lokasjon før det kan brukes bærende.

---

## 2. Terminologi og Aktørroller

| Riktig begrep | Forbudt / Vagt begrep | Begrunnelse |
| :--- | :--- | :--- |
| **Løsningsvalg** | *Produktvalg* | Løsningen omfatter produkter, montering, levetid og vedlikehold. |
| **Beslutningsstøtte** | *Automatisk valg / Svart boks* | VERIFIED anbefaler aldri automatisk. Entreprenøren har faglige ansvaret. |
| **Entreprenør & Kunde** | *Bruker / Brukeren* | Spesifiser hvem som gjør hva (byggmester/tømrer vs. boligkjøper/byggherre). |
| **Tilbudsfasen** | *Byggeplass / Prosjektering* | Valgene tas og prissettes i tilbudsfasen før prosjektet låses. |

---

## 3. Krav til Problemstilling (Seksjon 2 / K1)

Tekst som beskriver utfordringen i tilbudsfasen **MÅ** eksplisitt dekke tre ledd:

1. **Entreprenørens utfordring:** Mindre bedrifter (91,2 % har <10 ansatte jf. SSB 2026) har høy fagkompetanse, men mangler tid og spesialistverktøy til tunge livsløpsanalyser (LCA/LCC) når tilbudet prissettes.
2. **Kundens utfordring:** Kunden ser kun pris på tilbudene. De kan ikke sammenligne hva et dyrere tilbud gir i lavere strømregning, lengre levetid, lavere vedlikehold eller mindre fuktrisiko.
3. **Møtepunktet i tilbudsfasen:** Når forskjellene er usynlige for kunden, vinner det billigste tilbudet på papiret — selv om det koster mer over tid.

---

## 4. Prompter til Liming inn i Annen AI-Agent

Kopier og lim inn teksten i boksene under når du ber en annen AI-agent om å validere eller skrive tekst for VERIFIED.

### Prompt 1: Verifiseringssjekk av tekstutkast
```text
Du er en streng kvalitets- og kilde-auditor for IPN-søknadsprosjektet VERIFIED.
Sjekk det følgende tekstutkastet mot disse ufravikelige reglene:

1. VIBS-SJEKK: Inneholder teksten ordet "VIBS"? (Hvis JA -> STOPP og rapporter regelbrudd).
2. PARTNERSJEKK: Ramses det opp spesifikke firmanavn (f.eks. NorDan, Flekkefjord Sparebank) som bekreftede partnere? (Hvis JA -> STOPP. Kun partnertyper er tillatt jf. Beslutning F-03).
3. BKA2-SJEKK: Er BKA2 eller Vegard Knotten nevnt? (Hvis JA -> STOPP. Skal ut).
4. AKTØRSJEKK: Er problemet i tilbudsfasen beskrevet for BÅDE entreprenøren (mangel på tid/verktøy) og kunden (kan kun sammenligne pris)?
5. SPERREKILDESJEKK: Er Wiik2025, SA2018 eller udokumenterte påstander brukt som bevis? Brukes Bjørheim2026 (1 583 konkurser) som bærende belegg uten egen original/lokasjon?

Gi en kort rapport: PASS eller FAIL på hvert punkt.
```

### Prompt 2: Generering av ny nettsidetekst
```text
Skriv et tekstutkast for IPN-prosjektet VERIFIED. 

Husk følgende ufravikelige instruksjoner:
- VERIFIED er et forskningsprosjekt for beslutningsstøtte i tilbudsfasen.
- Bruk ALDRI ordet "VIBS".
- Ikke nevne spesifikke firmanavn på partnere (skriv kun partnertyper: forskningspartner, utførende entreprenører, finans/forsikring, dataeiere).
- Ikke nevne BKA2 eller Vegard Knotten.
- Beskriv utfordringen i tilbudsfasen for både entreprenøren (små bedrifter med dårlig tid) og kunden (kan ikke se forskjell på levetid og kvalitet, ser kun pris).
- Bruk korrekte tall: SSB 2026 (91,2 % <10 ansatte), BDO 2025 (3,3 % margin), Bjørheim 2026 (1 583 konkurser), Finans Norge 2023 (5,1 mrd kr vannskader), Gullbrekken 2025 (10-30 mrd kr byggefeil).
- ⚠️ ADVARSELL (Bjørheim 2026): Tallet 1 583 konkurser er sperret mot bærende bruk (SP-08, vedtak 2026-08-03) inntil egen original og presis lokasjon foreligger. Det kan brukes til orientering, men ikke som bærende belegg jf. Beslutning F-03 / sperrelisten.
```

---

## 5. Sjekkliste for Manuell / Automatisk Godkjenning

- [ ] Er ordet `VIBS` helt fraværende?
- [ ] Er firmanavn erstattet med partnertyper?
- [ ] Er BKA2 / Vegard Knotten fjernet?
- [ ] Er tilbudsfasen etablert som arenaen hvor valget tas?
- [ ] Er kundens ulempe (kun synlig pris, usynlig levetid/kvalitet) beskrevet?
- [ ] Er entreprenørens ulempe (mangler tid og spesialistverktøy under tilbudspress) beskrevet?
- [ ] Er `source_guard.py` kjørt og rapportert PASS uten treff på sperrede kilder?
