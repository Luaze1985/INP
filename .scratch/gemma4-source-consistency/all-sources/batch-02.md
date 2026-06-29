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

1. [EUTax]
[EUTax]
- Kildebibliotek linje 50: | `[EUTax]` | EU-taksonomi, Climate Delegated Act + DNSH (revisjon 2024–25). | Sekundær | [H\* ramme, M tall] | 🟡 | via søk | §7 / F5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [OmnibusI]
[OmnibusI]
- Kildebibliotek linje 51: | `[OmnibusI]` | Omnibus I / CSRD-innsnevring (vedtatt 24.02.2026). | Sekundær | [H\*] | 🟡 | nei (primær OJ) | §7 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

3. [NFR_IPN2026]
[NFR_IPN2026]
- Kildebibliotek linje 52: | `[NFR_IPN2026]` | Norges forskningsråd (2026). Innovasjonsprosjekt i næringslivet: Industri og tjenestenæringer 2026. Støttegrense kr 1 000 000–16 000 000 per prosjekt; maks 50 % støtte til bedriftenes kostnader. | Offisiell | [H] | 🟢 | ja | formalia / budsjett |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

4. [EN17472]
[EN17472]
- Kildebibliotek linje 53: | `[EN17472]` | EN 17472:2022 – bærekraftvurdering anlegg (LCA+LCC). | Sekundær | [L] | 🔴 | nei | §3 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

5. [Edelen2018]
[Edelen2018]
- Kildebibliotek linje 63: | `[Edelen2018]` | Edelen & Ingwersen (2018). Creation, management, use of data quality info for LCA. Int. J. LCA. | Primær | [H] | 🟢 | ja | §6 / F4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

6. [Lohman2023]
[Lohman2023]
- Kildebibliotek linje 64: | `[Lohman2023]` | Lohman et al. (2023). DMsan: MCDA framework. ACS Environmental Au. | Primær | [H] | 🟢 | ja | §5, §6 / F4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:59: - MCDA-metodene finnes i litteratur, ikke som SMB-produkter. `[Mecca2023]` 🟡 `[Lohman2023]` 🟢

7. [Benke2025]
[Benke2025]
- Kildebibliotek linje 65: | `[Benke2025]` | Benke et al. (2025). Harmonized embodied-LCA dataset, N-Amerika. Scientific Data. | Primær | [H] | 🟢 | ja | §6 / F4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:60: - Forklarbar usikkerhet er empirisk bekreftet som udekket for SMB. `[Benke2025]` 🟢 `[Nordic2023]` 🟢

8. [Weidema1996]
[Weidema1996]
- Kildebibliotek linje 66: | `[Weidema1996]` | Weidema & Wesnæs (1996). Data quality indicators (pedigree). J. Cleaner Prod. | Primær | [H\*] | 🟡 | nei | §6 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
