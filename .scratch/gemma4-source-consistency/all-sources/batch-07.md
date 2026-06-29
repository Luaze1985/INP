Oppgave: Vurder kildestatusdrift for disse kildene.
Les kun kandidatene under. Ikke finn pa fakta. Ikke gjor ny web/faktasjekk.

Returner gyldig JSON med:
{
  "ok": true/false,
  "flagged_rows": [
    {"item": "[EKSAKT_KILDEKEY]", "reason": "...", "recommended_action": "..."}
  ],
  "reason": "...",
  "recommended_action": "..."
}

Tvangsregel:
- Hvis ok=false, MAA flagged_rows ha minst en konkret rad.
- item MAA vaere en av kandidatoverskriftene, noyaktig som [KEY].
- Ikke flagg en kilde bare fordi den mangler i kildedommen; kildedommen er et subset.
- Flagg bare tydelig statusdrift: gronn vs gul/pause/rod, parkert kilde som brukes baerende, eller gammel/feil nokkel som fortsatt ser aktiv ut.

Repo-regler:
- Gronn kan baere en soknadssetning alene.
- Gul ma apnes/fraseres med forbehold.
- Rod er ikke siterbar.
- Pause betyr tatt ut av soknadstekst og parkert med gjeninnsettingsvilkar.

Kandidater:

1. [Harerusten2022]
[Harerusten2022]
- Kildebibliotek linje 122: | `[Harerusten2022]` | Harerusten (2022, NTNU). Konflikter i bygg- og anleggsbransjen. Sekundær omtale av konfliktkostnad; ikke bærende kilde for 2,2 mrd.-tallet. | Sekundær | [M] | 🟡 | ja (sekundær) | bakgrunn / WP2 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:23: | `[Harerusten2022]` | Harerusten, S. (2022). «Konflikter i bygg- og anleggsbransjen...» *NTNU Masteroppgave*. | Konflikter i bygg- og anleggssektoren koster 2,2 milliarder kroner årlig. | 🔴 **Ubekreftet** | **Grensetilfelle:** Masteroppgaven inneholder ikke p
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:24: | `[SA2018]` *(ny nøkkel)* | Samfunnsøkonomisk analyse (2018). «Konflikter i bygg- og anleggsnæringen» (Rapport 4-2018). | (Sitert sekundært via Harerusten 2022). | 🟢 **Bekreftet** | **Ny kilde:** Erstatt `[Harerusten2022]` med denne primærkilden for påstanden
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:41: - *Utkast:* `- Konfliktkostnad 2,2 mrd NOK/år. [Harerusten2022] 🟡`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:42: - *Årsak:* `[Harerusten2022]` er en masteroppgave (sekundærkilde) som ikke dokumenterer tallet primært.
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [Bygg21_2019]
[Bygg21_2019]
- Kildebibliotek linje 123: | `[Bygg21_2019]` | Bygg21 (2019). Digitalt materialkjøp 3 mrd/år; sporbarhet = forutsetning for ombruk. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §4 / F3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:27: - SMB har lav grad av digitale arbeidsprosesser; BIM brukes av spesialister/store. `[KD2024]` `[Bygg21_2019]` 🟡

3. [KS2025]
[KS2025]
- Kildebibliotek linje 124: | `[KS2025]` | KS/NHO/DiBK/KDD (2025). 60 % av byggesøknader mangelfulle; digitalt enevalg 810 mill./år. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | F6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

4. [Nordic2023]
[Nordic2023]
- Kildebibliotek linje 132: | `[Nordic2023]` | Nordic Council (2023). Building LCA and BIM practices in Norway. LCA-krav bevisst svakere for SMB. | Primær | [H] | 🟢 | ja | §9 / F4 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:30: | `[Nordic2023]` | Nordic Council of Ministers (2023). *Building LCA and BIM practices in Norway*. | LCA-krav og verktøyadopsjon er vesentlig svakere for SMB. | 🟢 **Bekreftet** | **Bekreftet:** Støtter F4 og behovet for forenklet beslutningsverktøy i WP4. |
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:44: | **F4** | Forstår SMB rapporten; påvirker den valg | §5, §6, §9 | Forklarbarhet/attribusjon udekket; SMB-atferd udokumentert `[Nordic2023]` 🟢 |
  - docs\reference\ipn-hovedokument.md:60: - Forklarbar usikkerhet er empirisk bekreftet som udekket for SMB. `[Benke2025]` 🟢 `[Nordic2023]` 🟢

5. [BKA2]
[BKA2]
- Kildebibliotek linje 133: | `[BKA2]` | BKA2 – Bærekraftige anskaffelser fase 2. 11,7 MNOK, til 2028. Knotten (SINTEF). | Primær | [H] | 🟢 | ja | §9 / WP1, WP4 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:31: | `[BKA2]` | Knotten, V. / SINTEF (2024–2028). *Bærekraftige anskaffelser fase 2*. | Koordinering og faglig synergi, ikke duplisering. Budsjett 11,7 mill. | 🟢 **Bekreftet** | **Bekreftet:** Kobling bekreftet. Sikrer faglig overføringsverdi for WP4 uten overlap
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:101: - Konsortierollen: SINTEF (Knotten) kobler til pågående `[BKA2]` 🟢 — komplement, ikke duplikat.
  - docs\reference\ipn-samledokument.md:128: Status nå: flere kilder er 🟢, flertallet er 🟡, og noen få er 🔴. Tyngdepunktet flytter seg mot grønt når SINTEF åpner primærene i fulltekst. De sterkeste grønne er standardene EN 15978:2026 og NS-EN 16627, EU-forordningene om digitalt produktpass (CPR/ESPR), fi

6. [Lutdal2021]
[Lutdal2021]
- Kildebibliotek linje 134: | `[Lutdal2021]` | Lutdal & Brenden (2021, NTNU). ~200 boligeiere; miljøsertifisering 13. plass. | Sekundær | [M] | 🟡 | nei (via bestillingsverk) | §9 / F4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

7. [Refleksjonsnotat2026]
[Refleksjonsnotat2026]
- Kildebibliotek linje 144: | `[Refleksjonsnotat2026]` | «Et blikk på byggebransjen og muligheter fremover», refleksjonsnotat v0.1. SINTEF-bestillingsverk for VIBS. | Konsortie-intern | – | 🔴 | Ikke siterbar i søknad. Kilde til primærsitatene under. |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

8. [Wiik2025]
[Wiik2025]
- Kildebibliotek linje 145: | `[Wiik2025]` | Wiik, M.K. (2025). Kostnadseffekten av klimatiltak i byggenæringen – en litteraturgjennomgang. SINTEF Notat 57. Konsortie-internt/uindeksert grensetilfelle. Må ikke brukes som uavhengig bærende belegg; bruk primærkildene `[EBA_NO2023]` og `[KD2024]` for 20 %-påstanden. **⏸ Tatt ut av søknadstekst 2026-06-28 (Lars' beslutning) — notatet ikke funnet i åpne registre; gjeninnsett kun hvis SINTEF dokumenterer at det finnes.** | Konsortie-intern | [M] | 🟡 ⏸ | Ikke bærende alene. Kan omtales eksplisitt som internt notat hvis nødvendig. |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:22: | `[Wiik2025]` | Wiik, M. K. (2025). «Kostnadseffekten av klimatiltak i byggenæringen...» *SINTEF Notat nr. 57*. | Gode materialvalg tidlig gir opptil 20 % reduksjon i utslipp uten økt kostnad. | 🔴 **Ubekreftet** | **Grensetilfelle:** Rapporten er et konsortie
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:51: - *Utkast:* `Bevislag: «−20 % fra leverandørvalg uten merkostnad» [Wiik2025] 🟡 — kan ikke stå alene før SINTEF åpner Notat 57 (→ 🟢). Innsendingssetning (etter 🟢): «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjekte
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:52: - *Årsak:* Siterer `[Wiik2025]` (Notat 57) som er et uverifisert internt bestillingsverk. Setningen må baseres på primærkilder for å unngå fagfellekritikk om sirkelargumentasjon.
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:88: - Bevislag: «−20 % fra leverandørvalg uten merkostnad» `[EBA_NO2023]` 🟡 og tidligfasepåvirkning `[KD2024]` 🟡. `[Wiik2025]` ⏸ **TATT UT av søknadstekst** — SINTEF Notat 57 ikke funnet i åpne registre. Gjeninnsett kun hvis SINTEF dokumenterer at notatet finnes.
  - docs\reference\ipn-hovedokument.md:121: - 0.5 (2026-06-28): Grensetilfeller markert ⏸ TATT UT av søknadstekst (Lars' beslutning): `[SA2018]`/2,2 mrd (rapport ikke lokalisert) og `[Wiik2025]` (Notat 57 ikke funnet). Ikke slettet — parkert her med gjeninnsettingsvilkår.
  - docs\reference\ipn-hovedokument.md:124: - 0.2 (2026-06-27): Kildedom flettet inn. Rettet konfliktkostnad til `[SA2018]`, An/Billio/Kaza-nøkler og CO₂-mekanisme uten `[Wiik2025]` som bærende kilde.
  - docs\reference\ipn-samledokument.md:177: - 0.6 (2026-06-28): Grensetilfeller tatt ut av søknadsteksten (Lars' beslutning): konflikttallet 2,2 mrd / `[SA2018]` (rapport ikke lokalisert) og `[Wiik2025]` (SINTEF Notat 57 ikke funnet i åpne registre). Kildene er ikke slettet — de står parkert i hovedokum
