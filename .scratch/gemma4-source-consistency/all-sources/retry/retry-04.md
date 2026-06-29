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

1. [GullbrekkenHolme2025]
[GullbrekkenHolme2025]
- Kildebibliotek linje 146: | `[GullbrekkenHolme2025]` | Gullbrekken & Holme (2025). Byggskader – Det glemte pengesluket. SINTEF. 1 feil i halvparten av boliger; 10–30 mrd NOK/år. | Primær (via bestillingsverk) | [M] | 🟡 | §8 / WP2. SINTEF åpner fulltekst → 🟢. |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:29: | `[GullbrekkenHolme2025]` | Gullbrekken & Holme (2025). «Byggskader – Det glemte pengesluket.» *SINTEF*. | 1 feil i halvparten av boliger; årlig kostnad 10–30 mrd. NOK. | 🟢 **Bekreftet** | **Bekreftet:** Sentral kilde for problembeskrivelsen i WP2, men må for
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:23: - Byggfeil koster 10–30 mrd NOK/år; minst én feil i halvparten av boliger. `[GullbrekkenHolme2025]` 🟡
  - docs\reference\ipn-hovedokument.md:29: > **Oversettelsesnote:** Dette avsnittet hviler i dag på 🟡-kilder via bestillingsverk/Kunnskapsfil. Før innsending: SINTEF åpner `[GullbrekkenHolme2025]` primær (→ 🟢); de norske problemtallene kan ellers hentes fra `forskning-kunnskapsbase.md` som etablert gru

2. [EBA_EU2023]
[EBA_EU2023]
- Kildebibliotek linje 79: | `[EBA_EU2023]` | European Banking Authority (2023). Report on Green Loans and Mortgages (15.12.2023). | Primær | [H] | 🟢 | ja | §7 / F5 |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:27: | `[EBA_EU2023]` | European Banking Authority (2023). *Report on Green Loans and Mortgages* (EBA/Op/2023/13). | ESG bankrapportering, grønne lån og MCD-revisjon. | 🟢 **Bekreftet** | **Kollisjonshåndtering:** Må skilles strengt fra den norske entreprenørforenin
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:104: | **EBA-akronym** | «EBA» (blandet bruk) | `[EBA_EU2023]` (European Banking Authority) vs. `[EBA_NO2023]` (Entreprenørforeningen Bygg og Anlegg) | Skilt i to distinkte kildeoppføringer for å unngå forveksling av bank- og byggeregler. |
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:184: * *Nøkkel i kildebibliotek:* `[EBA_EU2023]`.
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:194: - Citationsnøklene i interne utkast må holdes strengt adskilt som `[EBA_EU2023]` og `[EBA_NO2023]`. De må aldri slås sammen til en felles `[EBA]`-nøkkel.
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:45: | **F5** | Byggdata → ESG/grønn finans/forsikring | §7 | Apparatet energisentrert `[EBA_EU2023]` 🟢; bro mangler |
