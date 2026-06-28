# IPN kildestrategi og dokumentarkitektur

**Dato:** 2026-06-22 · **Versjon:** 0.1 (til godkjenning) · **Eier:** VIBS (struktur) + SINTEF (faglig verifisering)
**Formål:** Hvordan samle, verifisere og presentere kildene til IPN-søknaden uten info overload — alt med, men i lag.

---

## 0. TL;DR

To lag, én port, mnemoniske nøkler.

1. **Innsendingslag** = det Forskningsrådet leser. Magert, selvbærende, kilder som korte innskrevne referanser. **Ingen lenker** (utlysningens regel). Skrives i skjemaet.
2. **Bevislag** = internt VIBS+SINTEF, «levende». Hovedokument + klikkbare vedlegg (sannhetsserum = Vedlegg A). Det er her de lange begrunnelsene bor.
3. **Provenans-porten** styrer broen mellom lagene: en påstand kan bare bære en søknadssetning *alene* hvis den er backet av en **åpnet primærkilde**. Konsortiets eget bestillingsverk teller ikke som uavhengig belegg.

Resten av dokumentet er detaljene. Les §1, §3 og §6 hvis du har dårlig tid — de bærer designet.

---

## 1. De to lagene

| | Innsendingslag | Bevislag |
| --- | --- | --- |
| **Hvem ser det** | Forskningsrådets panel | VIBS + SINTEF internt |
| **Format** | Prosa i søknadsskjema, tegnbegrensning | Markdown med lenker/ankere |
| **Kilder** | Korte innskrevne referanser, ingen URL | Full referanse + konfidens + provenans |
| **Endrer seg** | Låses ved innsending | Levende fram til innsending |
| **Lenker** | **Nei** — tas ikke med i vurderingen | Ja, klikkbare vedlegg |

**Hvorfor skillet er hardt (verifisert 2026-06-22):** Utlysningssiden «Industri og tjenestenæringer 2026» sier ordrett: *«Dere skal ikke lenke til nettsider i søknaden. Eventuelle lenker vil ikke tas med i vurderingen av søknaden.»* 🟢 Den klikkbare vedleggsarkitekturen din er derfor **arbeidslaget som gjør innsendingsteksten mulig** — ikke selve innsendingen.

**Avklart lag-grense:** IPN har **ingen vedleggsslot for kilder eller faglig dokumentasjon** utover prosjektbeskrivelsen selv. De obligatoriske vedleggene er prosjektbeskrivelse + CV (maks 5, 4 sider hver) + partneropplysninger — ingen av dem er et sted å legge sannhetsserum, SoA eller kildebibliotek. Bevislaget forblir derfor internt, ikke fordi «alt skrives i skjemaet», men fordi **det ikke finnes noe sted å sende det inn.** Den ene narrative teksten som sendes inn er prosjektbeskrivelsen, og den er lengdebegrenset og lenkefri.

> 🟢 **Avklart (2026-06-22):** 2025-utlysningen bekrefter at prosjektbeskrivelsen er et **eget PDF-vedlegg på maks 10 sider** (mal «Mal for prosjektbeskrivelse – IPN 2025.docx»), pluss CV (maks 5, 4 sider hver) og partneropplysninger (1 side). 2026-siden viser at det «nye søknadssystemet» gjelder **arbeidspakker og budsjett** (bygges in-system) — den bekrefter *ikke* at prosjektbeskrivelsen er flyttet in-form. Sannhetsserumets «skrives i skjemaet» gjelder derfor trolig arbeidspakke-/budsjettdelen, ikke prosjektbeskrivelsen. **Arbeidsantakelse: ~10-siders PDF med innskrevne referanser, ingen lenker.** Smalt gjenstående: last ned 2026-malen og bekreft sideformatet.

---

## 2. Dokumentkart

**Innsendingslag (Forskningsrådet ser):**
- **Prosjektbeskrivelse** — den ene narrative teksten. = **utdata fra hovedokumentet**, komprimert til ~10 sider (2025-baseline; bekreft 2026-mal). PDF-vedlegg, innskrevne referanser, ingen lenker.
- **CV** (maks 5, 4 sider hver) + **partneropplysninger** — administrative vedlegg, ikke en del av kilde-/bevislaget.
- *Ingen vedleggsslot for kilder/faglig dokumentasjon.* Derfor bor hele bevislaget under.

**Bevislag (internt, levende):**

| Rolle | Fil | Status |
| --- | --- | --- |
| **Hovedokument** — den magre fortellingen med sitatnøkler | `ipn-hovedokument.md` | Bygges (etter godkjenning) |
| **Vedlegg A — Sannhetsserum** (kontrollark, stress-test) | `ipn-barekraft-sannhetsserum-2026-06-21.md` | Finnes |
| **Vedlegg B — Kunnskapsstatus / State of the Art** | `state-of-the-art-verified-ipn.md` | Finnes |
| **Vedlegg C — Kildebibliotek** (én kanonisk kildeliste) | `ipn-kildebibliotek.md` | Bygges (konsolider SoA §13 + ekstraksjon) |
| **Vedlegg D — Innsamlingslogg** (ekstraksjoner per runde) | `forskningsekstraksjon-2026-06-22.md` | Finnes |
| **Underlag** — etablert grunnlag, gjentas ikke | `forskning-kunnskapsbase.md`, `business/marked-sintef.md` | Finnes |

**Eierskap:** SINTEF (Knotten/Gullbrekken) eier faglig vurdering og **primærverifisering**. VIBS eier struktur, pilotdata og sammenstilling. Markeres i hver fil.

> **Presisering om «Vedlegg A»:** Det er et vedlegg til *det interne hovedokumentet*, ikke et vedlegg til Forskningsrådet-skjemaet. Sannhetsserumet sier selv «dette er ikke søknadstekst … et kontrollark» — det er internt per egen definisjon. Si dette eksplisitt så ingen senere antar at Vedlegg A sendes inn.

---

## 3. Provenans-porten (ryggraden)

Dette er den viktigste disiplinen — lærdommen fra at refleksjonsnotatet er et bestillingsverk, ikke uavhengig belegg. Provenans er **ikke** én kolonne blant ni. Det er **porten** som avgjør om en påstand i det hele tatt kan stå i søknadsprosa.

Hver kilde får ett provenansmerke:

- **Primær** — originalkilden selv, åpnet i fulltekst.
- **Sekundær** — referert via en annen kilde / kun sammendrag åpnet.
- **Konsortie-intern** — VIBS'/SINTEFs eget arbeid (bestillingsverk, FoU-panelnotat, intern kunnskapsbase). *Aldri uavhengig bekreftelse.*

Porten (samme rød/gul/grønn som ellers):

| Status | Hva kreves | Hva den kan brukes til |
| --- | --- | --- |
| 🟢 **GRØNN** | Primær / offisiell-autoritativ kilde åpnet og verifisert **for den påstanden den støtter** ([H]) | Kan bære en søknadssetning **alene** |
| 🟡 **GUL** | Sterk men primær ikke åpnet ([H*]), **eller** sekundær/konsortie-intern ([M]) | Kan støtte **internt**; åpne primæren før bærende bruk i søknad |
| 🔴 **RØD** | Kun søketreff/metadata ([L]), eller udokumentert | Ikke siterbar |

*Merk: [H\*] = høy konfidens via flere uavhengige sekundærkilder, men primæren er ikke åpnet. Det er sterkt nok internt, men en bærende søknadssetning krever at SINTEF åpner primæren først. Derfor 🟡, ikke 🟢.*

**Regel:** En reviewer-vendt setning som kun hviler på konsortiets eget bestillingsverk er en sårbarhet. En som hviler på en åpnet primær er det ikke. Porten gjør den forskjellen mekanisk synlig.

---

## 4. Kildebibliotek (Vedlegg C)

Én kanonisk kildeliste erstatter de spredte (i dag ligger de inni SoA §13). Alle andre dokumenter siterer en **nøkkel** og gjentar ikke full referanse.

**Nøkkelkonvensjon — mnemonisk, ikke nummerisk.** Bruk `[Forfatter+År]`, ikke `[K12]`. I et levende dokument drifter numeriske nøkler (append-only) eller knekker alle referanser (renummerering). Mnemoniske nøkler overlever omrokering og er selvforklarende:

`[Wiik2025]` · `[GullbrekkenHolme2025]` · `[EBA2023]` · `[KD2024]` · `[Mecca2023]` · `[Benke2025]` · `[BoE_PS25-25]`

**Rad-skjema (per kilde):**

| Felt | Eksempel |
| --- | --- |
| Nøkkel (= ankernavn) | `[Wiik2025]` |
| Full referanse | Wiik, M.K. (2025). *Kostnadseffekten av klimatiltak i byggenæringen.* SINTEF Notat 57. |
| Type | Rapport / fagfelle / standard / offentlig / verktøy |
| **Provenans** | Primær / sekundær / **konsortie-intern** |
| Konfidens | [H] / [H*] / [M] / [L] |
| Port-status | 🟢 / 🟡 / 🔴 |
| Åpnet | ja/nei + dato + hvem |
| Støtter | Påstand / FoU-spm (F1–F6) / WP |
| Verifiserer | SINTEF / VIBS |

Hver nøkkel er et markdown-anker, så `[Wiik2025]` i hovedteksten lenker til `#wiik2025` i biblioteket (internt klikkbart — bevislaget).

---

## 5. Progressiv disclosure — mekanikken mot info overload

Tre nivåer, leseren velger dybde:

```
Påstand (hovedtekst)
  └─ én linje bevis + [Nøkkel] + 🟢/🟡  ← synlig styrke uten å lese mer
       └─ (klikk nøkkel) → full referanse i Kildebibliotek
            └─ (klikk vedlegg) → lang begrunnelse i SoA / Sannhetsserum
```

- Hovedteksten forblir ren: påstand + nøkkel + portfarge.
- Konfidens og provenans er **synlig inline** — leseren ser om noe er 🟢 primær eller 🟡 konsortie-intern uten å åpne begrunnelsen.
- Den som vil grave klikker seg nedover. Den som ikke vil, leser bare hovedlinjen.

---

## 6. Oversettelseslaget — den vanskelige 20 %-en

Det interne lenkede systemet er den lette delen. Det vanskelige er å gjøre en **bevislag-påstand** om til en **forsvarlig søknadssetning** med kilde og ærlig provenans — uten lenke, innenfor tegnbegrensning. Her møtes nei-til-lenker-regelen og provenans-porten.

**Disiplinen, i tre trinn:**

1. **Port-sjekk.** Er kilden 🟢? Hvis 🟡 (konsortie-intern/sekundær): enten hold påstanden ute av søknaden, eller få SINTEF til å åpne primæren først.
2. **Komprimér til selvbærende setning.** Kilden skrives inn som kort referanse i parentes — `(Forfatter År)` — ingen URL.
3. **Ikke overselg styrken.** En 🟡-påstand fraseres med forbehold og aldri som bærende bevis.

**Arbeidet eksempel (dagens Wiik-sak):**

| | |
| --- | --- |
| **Bevislag (rå)** | «Wiik 2025 viser −20 % CO2 fra leverandørvalg uten merkostnad» `[Wiik2025]` 🟡 *konsortie-intern sekundærgjengivelse* |
| **Port** | 🟡 → **kan ikke** stå alene i søknad. Krever at SINTEF åpner Notat 57 i fulltekst → blir 🟢 [H]. |
| **Innsendingssetning (etter 🟢)** | «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (Wiik 2025; EBA m.fl. 2023).» |
| **Hvorfor den holder** | Kort ref inline, ingen lenke, ingen overload, og to navngitte kilder som panelet kan etterprøve. |

Dette eksempelet er malen. Hver bærende søknadssetning skal kunne spores gjennom porten på samme måte.

---

## 7. Innsamlingsworkflow — hvordan samle kildene

1. **Inntak.** Hver ny kilde får straks en rad i Kildebiblioteket med mnemonisk nøkkel + provenansmerke. Default port-status = 🔴 (uverifisert) til noe annet er bevist.
2. **Tre kanaler:**
   - **SINTEF fulltekst** (institusjonstilgang) → primærverifisering. Dette er den eneste kanalen som flytter noe til 🟢.
   - **Sonar-søk** (`/sonar-search`) → orientering + sekundærbekreftelse. Aldri eneste belegg for jus/medisin/finans. Logg søkestreng, modell, tidspunkt.
   - **Eksisterende kunnskapsbase** (`forskning-kunnskapsbase.md`, `marked-sintef.md`) → etablert grunnlag, gjentas ikke.
3. **Verifisering = port.** En kilde flyttes 🔴→🟡→🟢 kun når primær er åpnet. Logg «åpnet: ja/nei» + dato + hvem.
4. **Kobling.** Merk hver kilde med hvilken påstand/FoU-spm (F1–F6) og hvilken WP den støtter — så hovedokumentet vet hvor den hører hjemme.
5. **Sannhetsserum-loop.** Når en kilde flytter en sannhetsserum-rad (rød/gul/grønn), oppdater både biblioteket og Vedlegg A. De to skal aldri si forskjellige ting.

---

## 8. «Levende dokument»-regler

- **Versjon + dato** i header på hvert bevislag-dokument.
- **Kort endringslogg** nederst i hvert dokument.
- **Status-farger betyr det samme overalt:** 🟢/🟡/🔴 = bevisstyrke/siterbarhet, ikke noe annet.
- **Én sannhet per fakta:** Kildebiblioteket er eneste kanoniske kildeliste. Andre docs siterer nøkkel.
- **SINTEF-eierskap markeres** der en faglig vurdering eller primærverifisering kreves.
- **Frys ved innsending:** Når søknaden sendes, tas et datert øyeblikksbilde av bevislaget som «as-submitted».

---

## 9. Åpne verifiseringspunkter (RØD)

1. ~~**Vedleggsregler i 2026-utlysningen**~~ **[AVKLART – 2026-06-22]** No-links ordrett bekreftet; ingen vedleggsslot for kilder → bevislaget er internt. 2025-baseline bekreftet: prosjektbeskrivelse = 10-siders PDF + CV + partneropplysninger. **Smalt gjenstående:** last ned 2026-malen og bekreft at 10-siders PDF-formatet står (det «nye søknadssystemet» bekreftet å gjelde arbeidspakker/budsjett, ikke prosjektbeskrivelsen).
2. **SINTEF fulltekst-verifisering** av primærene som i dag er 🟡: `[Wiik2025]`, MCDM-review 2025, WLC-benchmark, Omnibus I, BoE PS25/25 + DP1/25 (jf. SoA §14).

---

## 10. Neste steg

Få **arkitekturen godkjent** først. Deretter, i rekkefølge:

1. Bygg **Kildebibliotek (Vedlegg C)** — konsolider SoA §13 + forskningsekstraksjon til mnemoniske nøkler med provenans-port.
2. Bygg **hovedokument-skjelett** med sitatnøkler og progressiv disclosure.
3. Kjør **oversettelseslaget** (§6) på hver bærende påstand når WP-strukturen er satt.

*Ikke bygg skjelettet før arkitekturen er godkjent.*

---

### Endringslogg
- 0.3 (2026-06-22): 2025-baseline bekreftet — prosjektbeskrivelse = 10-siders PDF-vedlegg. «Nytt søknadssystem» gjelder arbeidspakker/budsjett, ikke prosjektbeskrivelsen. Port-definisjon (🟢) strammet til «for den påstanden den støtter». Smalt gjenstående: bekreft 2026-mal.
- 0.2 (2026-06-22): Vedleggsregler verifisert mot forskningsradet.no. No-links bekreftet ordrett; ingen vedleggsslot for kilder → lag-grense avklart (bevislag internt). Residual 🟡: PDF vs in-form for prosjektbeskrivelsen.
- 0.1 (2026-06-22): Første utkast. To-lags arkitektur, provenans-port, mnemoniske nøkler, oversettelseslag. Til godkjenning.
