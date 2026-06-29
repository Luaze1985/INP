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

1. [Multiconsult2023]
[Multiconsult2023]
- Kildebibliotek linje 87: | `[Multiconsult2023]` | Multiconsult/Eika Boligkreditt (2023). Nyere boliger 11,3 % av masse, 3,9 % av utslipp. | Sekundær | [M] | 🟡 | nei (via Kunnskapsfil) | §7 / F5 |
- Kildedom-treff: ingen (ikke flagg dette alene)
- Bruk i kanoniske soknadsdocs: ingen direkte key-treff

2. [Wiik2025]
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
