# SOKNADSTEKST_REGLER.md — ipn-verified

Spesifikke sjekkregler, versjonsfasit og arbeidsrekkefølge før redigering av K1–K4 og V1–V3 for IPN-søknaden VERIFIED.

## Arbeidsrekkefølge og Ordlydsfasit

For K1–K4 og V1–V3 på arbeidsgrenen gjelder denne spesifikke rekkefølgen:

1. **Beslutningsstyring**:
   `docs/reference/prosjektbeskrivelse/arbeidsversjoner/HANDOFF-godkjent-review-k1-k4-v1-v3-2026-07-25.md` styrer beslutninger og avgrensninger.
2. **Ordlydsfasit**:
   De sju `*-godkjent-v0.1.md`-filene under `docs/reference/prosjektbeskrivelse/arbeidsversjoner/` er ordlydsfasit for godkjente enkeltformuleringer.
3. **Låst Baseline (Innholdsdekning)**:
   `docs/reference/prosjektbeskrivelse/arbeidsversjoner/soknadstekst-samlet-kandidat-v0.4.md` er låst baseline for innholdsdekning. Innhold derfra skal ikke regnes som slettet bare fordi det mangler i en K/V-arbeidsversjon. Endre aldri `v0.4` under videre arbeid.
4. **Integrasjonskandidat**:
   `docs/reference/prosjektbeskrivelse/arbeidsversjoner/soknadstekst-samlet-kandidat-v0.5.md` er aktiv K/V-integrasjonskandidat. Den samler godkjent ordlyd, men erstatter ikke hele `v0.4` og er ikke innsendingsklar.
5. **Kanoniske Innflettingsmål**:
   `docs/reference/prosjektbeskrivelse/k1-bakgrunn.md` til `v3-okonomi.md` er kanoniske innflettingsmål, men ikke tekstfasit før kvalitetsport C7 er lukket.

## Håndtering av Konflikter og Historiske Støttedokumenter

* **Ved konflikt**: Handoff-filen gjelder for omfang, arbeidsversjonene for godkjent ordlyd og `v0.4` for innholdsdekning. Konflikten skal markeres i et notat; ingen agent skal velge stille.
* **Historisk referanselag**: Dokumenter som `ipn-hoveddokument.md`, `ipn-samledokument.md` og `ipn-prosjektbeskrivelse-utkast.md` var historiske utkast og er erstattet av strukturen under `docs/reference/prosjektbeskrivelse/`. De gjelder ikke som aktiv ordlydsfasit.
* **Kildeverifisering**: Er kilden 🟢? Hvis ikke — la den ikke bære setningen.
* **Endringslogg**: Logg alltid endringer i relevante dokumenters endringslogg.
* **Skrivebeskyttelse**: Spør Lars før du gjør irreversible endringer.
