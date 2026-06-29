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

2. [EBA_NO2023]
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

3. [KD2024]
[KD2024]
- Kildebibliotek linje 148: | `[KD2024]` | Kommunal- og distriktsdepartementet, DiBK, Fellesforbundet, NHO Byggenæringen (2024). Byggenæringens klimafotavtrykk – et kunnskapsgrunnlag. Figur 1: påvirkningsrom størst i tidligfase. A1–A3 ≈ 63 % av materialeutslipp; sektor 17,3 mill. tonn CO₂e (2020). | Sekundær (via bestillingsverk) | [M] | 🟡 | §2, §3 / F2. NB: A1–A3-tallet attribuert «Asplan Viak/DiBK 2024» i Kunnskapsfil – avklar om samme rapport. |
- Kildedom-treff:
  - docs\reference\vibs-verified-kildedom-2026-06-27.md:53: - *Tiltak:* Skriv om til: `Innsendingssetning: «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (EBA Norge 2023; KDD et al. 2024).» [EBA_NO2023] [KD2024]`
- Bruk i kanoniske soknadsdocs:
  - docs\reference\ipn-hovedokument.md:12: - **Ingen lenker** i den innsendte teksten (bekreftet 2026). Nøkler er interne; ved innsending erstattes `[EBA_NO2023]` og `[KD2024]` med korte tekstreferanser til EBA Norge (2023) og KDD et al. (2024).
  - docs\reference\ipn-hovedokument.md:25: - Påvirkningsrommet for utslipp er størst i de tidligste fasene. `[KD2024]` 🟡
  - docs\reference\ipn-hovedokument.md:27: - SMB har lav grad av digitale arbeidsprosesser; BIM brukes av spesialister/store. `[KD2024]` `[Bygg21_2019]` 🟡
  - docs\reference\ipn-hovedokument.md:88: - Bevislag: «−20 % fra leverandørvalg uten merkostnad» `[EBA_NO2023]` 🟡 og tidligfasepåvirkning `[KD2024]` 🟡. `[Wiik2025]` ⏸ **TATT UT av søknadstekst** — SINTEF Notat 57 ikke funnet i åpne registre. Gjeninnsett kun hvis SINTEF dokumenterer at notatet finnes.
  - docs\reference\ipn-hovedokument.md:89: - Innsendingssetning: «Tidlige materialvalg kan redusere klimagassutslipp med opptil 20 % uten merkostnad for prosjektet (EBA Norge 2023; KDD et al. 2024).» `[EBA_NO2023]` `[KD2024]`

4. [VIBS-FoUpanel]
[VIBS-FoUpanel]
- Kildebibliotek linje 149: | `[VIBS-FoUpanel]` | VIBS_VERIFIED_FoU-panel.docx / VIBS_ByggSpor_FoU-panel.docx. Internt FoU-panelnotat. | Konsortie-intern | – | 🔴 | Ikke siterbar i søknad. Intern struktur/argument. |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff
