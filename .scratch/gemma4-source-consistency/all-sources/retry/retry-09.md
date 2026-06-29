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

1. [EBA_NO2023]
[EBA_NO2023]
- Kildebibliotek linje 147: | `[EBA_NO2023]` | EBA (Entreprenørforeningen Bygg og Anlegg), Grønn Byggallianse, Norsk Eiendom (2023). Veileder for klimagassreduksjoner – boligblokker. Opptil 20 % CO₂-kutt fra materialbruk uten merkostnad. | Sekundær (via bestillingsverk) | [M] | 🟡 | §3 / F1. **Ikke** European Banking Authority – se `[EBA_EU2023]`. |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:28: | `[EBA_NO2023]` | Entreprenørforeningen Bygg og Anlegg, Grønn Byggallianse & Norsk Eiendom (2023). *Veileder for boligblokker*. | Opptil 20 % klimagassreduksjon fra materialvalg uten merkostnad. | 🟢 **Bekreftet** | **Kollisjonshåndtering:** Må skilles strengt
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:51: - *Utkast:* `Bevislag: «−20 % fra leverandørvalg uten merkostnad» [Wiik2025] 🟡 — kan ikke stå alene før SINTEF åpner Notat 57 (→ 🟢). Innsendingssetning (etter 🟢): «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjekte
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:53: - *Tiltak:* Skriv om til: `Innsendingssetning: «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (EBA Norge 2023; KDD et al. 2024).» [EBA_NO2023] [KD2024]`
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:104: | **EBA-akronym** | «EBA» (blandet bruk) | `[EBA_EU2023]` (European Banking Authority) vs. `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg) | Skilt i to distinkte kildeoppføringer for å unngå forveksling av bank- og byggeregler. |
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:12: - **Ingen lenker** i den innsendte teksten (bekreftet 2026). Nøkler er interne; ved innsending erstattes `[EBA_NO2023]` og `[KD2024]` med korte tekstreferanser til EBA Norge (2023) og KDD et al. (2024).
  - docs\reference\ipn-hovedokument.md:88: - Bevislag: «−20 % fra leverandørvalg uten merkostnad» `[EBA_NO2023]` 🟡 og tidligfasepåvirkning `[KD2024]` 🟡. `[Wiik2025]` ⏸ **TATT UT av søknadstekst** — SINTEF Notat 57 ikke funnet i åpne registre. Gjeninnsett kun hvis SINTEF dokumenterer at notatet finnes.
  - docs\reference\ipn-hovedokument.md:89: - Innsendingssetning: «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (EBA Norge 2023; KDD et al. 2024).» `[EBA_NO2023]` `[KD2024]`

2. [Lutdal2021]
[Lutdal2021]
- Kildebibliotek linje 134: | `[Lutdal2021]` | Lutdal & Brenden (2021, NTNU). ~200 boligeiere; miljøsertifisering 13. plass. | Sekundær | [M] | 🟡 | nei (via bestillingsverk) | §9 / F4 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
