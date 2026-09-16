# VERIFIED — IF-only-budsjett

**Arbeidsramme:** 16,0 MNOK i AP1–AP3, 8,0 MNOK søkt støtte og
8,0 MNOK egenfinansiering over 36 måneder.

Dette er et internt beslutningsgrunnlag, ikke et innsendingsklart budsjett.
Beløpene for fem kostnadsbærere og tre arbeidspakker er matematisk avstemt.
Underfordelingen av Vi Bygger Sammen AS sin rad på 12,6 MNOK er åpen til egne
timer og leverandørtilbud er dokumentert.

## Filer

- `kalkulator.py` er den deterministiske sannhetskilden for totaler,
  AP-matrisen og åpne VIBS-kostnadsposter.
- `partneroversikt.md` beskriver kostnadsbærere, leverandører og rolleporter.
- `fordelingsplan.md` viser den avstemte IF-only-modellen og alle åpne
  økonomiporter.
- `beregningsformler.md` beskriver beregningene og dokumentasjonskravene uten
  udokumenterte timesatser eller leverandørpriser.
- `grunnprompt.md` er et kort styringsgrunnlag for videre budsjettarbeid.

## Kontroller

Kjør fra repoets rot:

```powershell
python budsjett/kalkulator.py
python tools/budget_validator.py
python -m unittest tests.test_budget_validator
```

`BUDSJETTVALIDERING PASS` betyr at den matematiske rammen er konsistent. Så
lenge validatoren også skriver `STATUS: IKKE INNSENDINGSKLAR`, mangler det
dokumentasjon for VIBS-underfordelingen.

## Ufravikelige føringer

- Leverandørkjøp føres én gang hos kjøpende kostnadsbærer, ikke som
  egenfinansiering hos leverandøren.
- Ingen leverandørpris settes uten tilbud eller annet dokumentert grunnlag.
- Partnerkostnader må være reelle, bokførte kostnader hos den juridiske
  samarbeidspartneren.
- 50 prosent IF-støtte er en arbeidsberegning innenfor utlysningens tak;
  endelig støtte fastsettes av Forskningsrådet. Se primærkildene i
  `beregningsformler.md`.
- Den gamle 32 MNOK/AP1–AP6-modellen er historisk og skal ikke brukes i dette
  arbeidsgrunnlaget.

## Endringslogg

| Dato | Hvem | Hva | Hvorfor |
|---|---|---|---|
| 2026-09-06 | Codex | Erstattet gammel 32 MNOK-oversikt med IF-only-status og kontrollrutine. | Fjerne konflikt med v1.7 og hindre at historiske leverandøranslag brukes som priser. |
