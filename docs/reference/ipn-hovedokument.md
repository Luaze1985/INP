# Hovedokument — VERIFIED / IPN (skjelett)

**Dato:** 2026-06-22 · **Versjon:** 0.1 (skjelett, ikke fylt) · **Eier:** VIBS (tekst) + SINTEF (faglig)
**Rolle:** Den **magre fortellingen**. Utdata herfra, komprimert til **~10 sider, blir prosjektbeskrivelsen** (eget PDF-vedlegg; 2025-baseline bekreftet, 2026-mal gjenstår å bekrefte – se kildestrategi §1). Siterer nøkler fra [Vedlegg C](ipn-kildebibliotek.md), gjentar ikke referanser.

---

## Slik brukes skjelettet

- Hver bærende påstand skrives som: **påstand + `[nøkkel]` + 🟢/🟡**. Fargen er fra kildebiblioteket.
- **Bare 🟢 kan stå alene** i prosjektbeskrivelsen. 🟡 må enten få primær åpnet av SINTEF først, eller fraseres med forbehold og uten å være bærende. Jf. kildestrategi §3 og §6.
- **Ingen lenker** i den innsendte teksten (bekreftet 2026). Nøkler er interne; ved innsending erstattes `[EBA_NO2023]` og `[KD2024]` med korte tekstreferanser til EBA Norge (2023) og KDD et al. (2024).
- **Sidebudsjett:** ~10 sider totalt (PDF). Noter grovt sideanslag per seksjon. Disiplinen er progressiv disclosure – det lange bor i vedleggene, ikke her.
- `‹TODO›` = må skrives/fylles. Dette er et skjelett, ikke tekst.

---

## 1. Bakgrunn og utfordring

*Formål: vis at problemet er reelt og kostbart, og at data finnes men ikke er koblet til beslutning i tilbudsfasen.*

Kjernepunkter (alle har etablert belegg):
- Byggfeil koster 10–30 mrd NOK/år; minst én feil i halvparten av boliger. `[GullbrekkenHolme2025]` 🟡
- Konfliktkostnad 2,2 mrd NOK/år. `[SA2018]` ⏸ **TATT UT av søknadstekst** — Samfunnsøkonomisk analyse (2018), Rapport 4-2018 ikke lokalisert i åpne registre. Gjeninnsett som 🟢 når rapporten er funnet/åpnet.
- Påvirkningsrommet for utslipp er størst i de tidligste fasene. `[KD2024]` 🟡
- Dårlig data driver omarbeid (52 % internasjonalt). `[PlanGridFMI2018]` 🟡
- SMB har lav grad av digitale arbeidsprosesser; BIM brukes av spesialister/store. `[KD2024]` `[Bygg21_2019]` 🟡

> **Oversettelsesnote:** Dette avsnittet hviler i dag på 🟡-kilder via bestillingsverk/Kunnskapsfil. Før innsending: SINTEF åpner `[GullbrekkenHolme2025]` primær (→ 🟢); de norske problemtallene kan ellers hentes fra `forskning-kunnskapsbase.md` som etablert grunnlag.

‹TODO› Skriv 1–2 avsnitt som lander på VIBS-utfordringen: heterogene byggevaredata kobles ikke til beslutning i tilbudsfasen for ikke-spesialister.

---

## 2. Mål og FoU-spørsmål

*Formål: definer FoU-høyden som ikke-triviell. F1–F6 er forankret i SoA (se [Vedlegg B](state-of-the-art-verified-ipn.md) §12).*

| FoU-spm | Spørsmål (kort) | Forankret i | Dokumentert hull |
| --- | --- | --- | --- |
| **F1** | Kvalitet/levetid → lønnsom bærekraft | §3, §7, §8 | Energi↔PD bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er hullet |
| **F2** | NOBB/GTIN/EPD/FDV tidlig nok i tilbud | §4 | Data finnes `[NOBB]` 🟡, ikke koblet til tilbudsbeslutning |
| **F3** | Når er ombruk/rehab best | §8 | Ombrukskriterier beskrevet `[SINTEFFag18]` 🟡, ikke tatt i bruk i praktiske verktøy |
| **F4** | Forstår SMB rapporten; påvirker den valg | §5, §6, §9 | Forklarbarhet/attribusjon udekket; SMB-atferd udokumentert `[Nordic2023]` 🟢 |
| **F5** | Byggdata → ESG/grønn finans/forsikring | §7 | Apparatet energisentrert `[EBA_EU2023]` 🟢; bro mangler |
| **F6** | Dataflyt/API/sporbarhet kan skaleres | §4, §10 | DPP umoden for bygg `[CPR2024]` 🟢; verktøy er ulike systemer uten kobling |

‹TODO› Skriv prosjektets hovedmål + delmål som binder F1–F6 sammen.

---

## 3. Kunnskapsstatus og nyhetsverdi

*Formål: «utfordre state of the art» (rådets ord). Vis at hver byggekloss finnes og er moden, men at ingen syr dem sammen.*

Bærende setning (nyhetsverdi): Komponentene finnes hver for seg og er modne, men ingen utrullet metode kombinerer **(a) dataintegrasjon, (b) tilbudsfase, (c) SMB, (d) synlig usikkerhet, (e) beslutningseffekt, (f) DNSH-bredde** til ett forklarbart verktøy.

- Lim inn gap-matrisen fra [Vedlegg B](state-of-the-art-verified-ipn.md) §11 (de seks aksene mot hver state-of-the-art-rad). Den er bygget for å mate dette avsnittet direkte.
- MCDA-metodene finnes i litteratur, ikke som SMB-produkter. `[Mecca2023]` 🟡 `[Lohman2023]` 🟢
- Forklarbar usikkerhet er empirisk bekreftet som udekket for SMB. `[Benke2025]` 🟢 `[Nordic2023]` 🟢

‹TODO› 1 avsnitt + gap-matrisen. Hold den til seks akser, ikke list alle verktøy.

---

## 4. Arbeidspakker

*Formål: vis sammenheng mellom AP og bærekraftsbidrag (rådets krav). Full test i [Vedlegg A](ipn-barekraft-sannhetsserum-2026-06-21.md) §5.*

| WP | Innhold | Bærekraftsbidrag | Målepunkt | Status nå |
| --- | --- | --- | --- | --- |
| **WP1** | Datastandard og leverandørleveranse | Bedre data → lavere ressursbruk/bedre levetid | Andel varer m/ GTIN/NOBB/EPD/FDV/status | ‹TODO› |
| **WP2** | Kontroll og kvalitetsspor | Færre feil/omarbeid | Avvik, omarbeid, manglende FDV, reklamasjon | ‹TODO› |
| **WP3** | Pilotportefølje og effektmåling | Sannsynliggjør faktisk effekt | CO₂, LCC, avvik, tidsbruk, beslutningsendring | **baseline mangler (Rød)** |
| **WP4** | Kompetanse og adopsjon | Setter SMB i stand til å bruke grunnlaget | Forståelse, aktiv bruk, endret praksis | ‹TODO› |
| **WP5** | Skalering og kommersialisering | Bransjeeffekt utover pilotene | Eksterne aktører, produktkategorier, datamal | ‹TODO› |

> **Kritisk:** WP3 må ha før/etter eller A/B mot baseline. Uten baseline blir effekten spekulativ (jf. Vedlegg A §5).

---

## 5. Virkninger, effekter og bærekraft

*Formål: Forskningsrådet vurderer bærekraft under «Virkninger og effekter» – do-not-harm, relativ front, ikke antall mål. Dette er der oversettelseslaget (kildestrategi §6) er hardest.*

- **SDG-spor:** Primær 12.2 (ressurseffektivitet), støtte 12.5 (avfall/ombruk). Sekundær 9.4 / 11.6. Begrunnelse i [Vedlegg A](ipn-barekraft-sannhetsserum-2026-06-21.md) §2.
- **CO₂-mekanisme (arbeidet eksempel på oversettelse):**
  - Bevislag: «−20 % fra leverandørvalg uten merkostnad» `[EBA_NO2023]` 🟡 og tidligfasepåvirkning `[KD2024]` 🟡. `[Wiik2025]` ⏸ **TATT UT av søknadstekst** — SINTEF Notat 57 ikke funnet i åpne registre. Gjeninnsett kun hvis SINTEF dokumenterer at notatet finnes.
  - Innsendingssetning: «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (EBA Norge 2023; KDD et al. 2024).» `[EBA_NO2023]` `[KD2024]`
- **Do-not-harm:** Egen DNSH-tabell kreves. Bruk angrepslisten i [Vedlegg A](ipn-barekraft-sannhetsserum-2026-06-21.md) §4 som grunnlag. **Status: Rød — må skrives.**
- **Bro til grønn finans:** energi↔PD er bekreftet `[Billio2022]` 🟢 `[Kaza2014]` 🟢 og støttet for næringsbygg av `[An2020]` 🟡; holdbarhet→PD er FoU-hullet (F1). `[BoE_PS25-25]` 🟡 gir drahjelp fra kommende regelverk.

‹TODO› Hver bærekraftseffekt skal ha baseline, indikator, datakilde og hvem som måler. Ingen effektpåstand uten det.

---

## 6. Gjennomføring, risiko og formidling

*Formål: realistiske arbeidspakker/leveranser og relevante risikovurderinger (rådets ord).*

- Konsortierollen: SINTEF (Knotten) kobler til pågående `[BKA2]` 🟢 — komplement, ikke duplikat.
- ‹TODO› Risikotabell (FoU-risiko i vektingsmodell, datakvalitet, pilottilgang, adopsjon).
- ‹TODO› Formidling/skalering.

---

## Sidebudsjett (~10 sider totalt)

| Seksjon | Sideanslag | Faktisk |
| --- | --- | --- |
| 1 Bakgrunn | ~1,5 | |
| 2 Mål/FoU | ~1,5 | |
| 3 Kunnskapsstatus | ~2 | |
| 4 Arbeidspakker | ~2 | |
| 5 Virkninger | ~2 | |
| 6 Gjennomføring | ~1 | |

---

### Endringslogg
- 0.5 (2026-06-28): Grensetilfeller markert ⏸ TATT UT av søknadstekst (Lars' beslutning): `[SA2018]`/2,2 mrd (rapport ikke lokalisert) og `[Wiik2025]` (Notat 57 ikke funnet). Ikke slettet — parkert her med gjeninnsettingsvilkår.
- 0.4 (2026-06-27): Språkvask. Byttet sjargong til konkret norsk og beholdt kildestatus uendret.
- 0.3 (2026-06-27): Faktisk kildesjekk etter innfletting. Justert `[SA2018]` og `[An2020]` til 🟡 inntil primærrapport/fulltekst er åpnet.
- 0.2 (2026-06-27): Kildedom flettet inn. Rettet konfliktkostnad til `[SA2018]`, An/Billio/Kaza-nøkler og CO₂-mekanisme uten `[Wiik2025]` som bærende kilde.
- 0.1 (2026-06-22): Skjelett. Seks seksjoner mot IPN-kriteriene, sitatnøkler + portfarge inn, oversettelses-eksempel i §5. Ikke fylt med tekst.
