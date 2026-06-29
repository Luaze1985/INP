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

1. [Reduzer]
[Reduzer]
- Kildebibliotek linje 97: | `[Reduzer]` | Reduzer (NO, NTNU). Norsk, 15 000+ EPD, enkriterium i praksis. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [Madaster]
[Madaster]
- Kildebibliotek linje 98: | `[Madaster]` | Madaster (NL). Materialpass/restverdi, porteføljenivå. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

3. [Cobuilder]
[Cobuilder]
- Kildebibliotek linje 99: | `[Cobuilder]` | Cobuilder (NO). Produktdata-infrastruktur, DPP, FDV. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

4. [Concular]
[Concular]
- Kildebibliotek linje 100: | `[Concular]` | Concular (DE). Sirkularitet/ombruk + CircularLCA. | Sekundær | [M] | 🟡 | ja (leverandørside) | §10 / F3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

5. [2050Materials]
[2050Materials]
- Kildebibliotek linje 101: | `[2050Materials]` | 2050 Materials. Flere miljødimensjoner + API. | Sekundær | [L/M] | 🔴 | ja (leverandørside) | §10 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

6. [NOBB-OCL]
[NOBB-OCL]
- Kildebibliotek linje 102: | `[NOBB-OCL]` | Norsk Byggtjeneste × One Click LCA-partnerskap (EPD-adopsjon). | Sekundær | [M] | 🟡 | ja (OCL-PM, leverandørframstilling) | §4, §10 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

7. [NOBB]
[NOBB]
- Kildebibliotek linje 112: | `[NOBB]` | NOBB / Norsk Byggtjeneste; GS1/GTIN-regelverk. ~3 mill. varer. | Sekundær | [M] | 🟡 | nei | §4 / F2 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:42: | **F2** | NOBB/GTIN/EPD/FDV tidlig nok i tilbud | §4 | Data finnes `[NOBB]` 🟡, ikke koblet til tilbudsbeslutning |
  - docs\reference\ipn-hovedokument.md:72: | **WP1** | Datastandard og leverandørleveranse | Bedre data → lavere ressursbruk/bedre levetid | Andel varer m/ GTIN/NOBB/EPD/FDV/status | ‹TODO› |
  - docs\reference\ipn-samledokument.md:26: Samtidig finnes mye av dataene som skal til for å ta bedre valg allerede. Miljødeklarasjoner (EPD), produktdata i NOBB, livsløpskostnader og levetidsdata eksisterer.
  - docs\reference\ipn-samledokument.md:44: Datagrunnlaget modnes gjennom EPD-systemet, NOBB og det kommende digitale produktpasset (DPP, forordning (EU) 2024/3110).
  - docs\reference\ipn-samledokument.md:82: - **Manglende data skjules ikke.** Dokumentasjonstillit er en multiplikator: tredjepartsverifisert (1,0), standardisert kilde som NOBB (0,75), egenoppgitt fra produsent (0,5). Et produkt får ikke full score på påstander det ikke kan dokumentere.

8. [EPD-Norge]
[EPD-Norge]
- Kildebibliotek linje 113: | `[EPD-Norge]` | EPD-Norge / ECO Platform / ECO Portal. | Sekundær | [M] | 🟡 | nei | §4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
