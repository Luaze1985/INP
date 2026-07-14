---
title: Handoff (AGY) - Kildekritikk og kriteriegap
date: 2026-07-10
status: ready
from: claude
to: antigravity (AGY)
branch: main
tags: [vibs, verified, ipn, kildekritikk, forskningsradet]
---

# Handoff (AGY): kildekritikk, kriteriegap og nye kilder for VERIFIED IPN

## Kort beskjed

Lag et arbeidsdokument som hjelper Lars Erik og Lars Gunnar å se hva som gjenstår før IPN-søknaden kan strammes til. Du skal ikke skrive ren søknadsprosa. Du skal lage kildekritisk vurdering, kriteriematch og målrettet kildejakt.

## Rollefordeling (ærlighetsregel)

- **AGY (deg):** gjør kildekritisk review, åpne kildesøk og kriteriegap-analyse.
- **Claude:** skrev denne handoffen. Styrer deg ikke direkte.
- **Lars Erik / Lars Gunnar:** avgjør grensetilfeller, metodevalg, baseline og hva som skal inn i ren søknadstekst.
- **Codex:** kan senere bruke funnene dine til å oppdatere arbeidsutkast eller lage PDF-grunnlag.
- **SINTEF:** primærverifiserer vitenskapelige fulltekstkilder fra midten av august 2026.

## Inndata (les for kontekst)

- `AGENTS.md` — ufravikelige kilde- og sannhetsregler.
- `CONTEXT.md` — gjeldende status og åpne risikoer.
- `docs/agents/domain.md` — domenedokumenter og vokabular.
- `docs/reference/prosjektbeskrivelse/` — første røffe K1-K4 / V1-V3-utkast.
- `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md` — Forskningsråd-kriterier, sannhetsserum, bærekraft/DNSH og §10 om utlysningen.
- `docs/reference/vibs-verified-kildedom-2026-06-27.md` — autoritativ kildedom for statusporter.
- `docs/reference/ipn-kildebibliotek.md` — kanonisk kildeliste.
- `docs/reference/state-of-the-art-verified-ipn.md` — SoA og gap-matrise.
- `docs/reference/ipn-arbeidsplan-juli-aug-2026.md` — arbeidsplan og kilder som må åpnes.
- `../vibs-boligpass/docs/business/gronn-plattform.md` — eldre, men nyttig grunnlag for KPI-er, WP-er og pilotlogikk. Ikke behandle som IPN-fasit.

## Det du skal levere

Skriv ett arbeidsdokument:

`docs/reference/kildekritikk/kildekritisk-vurdering-og-kriteriegap-v0.1.md`

Dokumentet skal ha disse delene:

1. **Kort dom**
   - Hva treffer søknaden godt?
   - Hva er mest risikabelt?
   - Hva kan skrives som prosjektopplegg uten ekstern kilde?
   - Hva må kildeverifiseres eksternt?

2. **Hva gjenstår før rent arbeidsutkast kan strammes**
   Bruk tre kategorier:
   - `Må kildeverifiseres`
   - `Må besluttes av VIBS / Lars Gunnar`
   - `Kan beskrives som FoU-opplegg`

3. **Forskningsrådets kriterier**
   Vurder søknaden mot:
   - Kvalitet
   - Virkninger og effekter
   - Gjennomføring
   - bærekraft / do-not-harm
   - støttebeløp, støttesats og formalkrav

   Bruk kun dokumenterte krav fra utlysningen eller `ipn-barekraft-sannhetsserum-2026-06-21.md`.

4. **Kildekritisk gjennomgang av dagens hovedpåstander**
   For hver hovedpåstand:
   - påstand
   - nåværende kilde(r)
   - status fra kildedom/kildebibliotek
   - kan den bære ren søknadstekst nå?
   - anbefalt formuleringstype: `kan stå`, `må tones ned`, `må ut`, `kan stå som FoU-hypotese`

5. **Målrettet åpne kildesøk**
   Prøv å finne eller verifisere kilder for disse hullene:
   - SMB-definisjon og andel av norsk byggenæring: SSB, NHO, BNL/NHO Byggenæringen, Eurostat/EU-definisjon.
   - Byggenæringens størrelse, fragmentering og digitaliseringsgrad: offentlige eller bransjenære primærkilder.
   - `[KD2024]`: tidligfase/påvirkningsrom, helst regjeringen.no eller offisiell PDF.
   - `[EBA_NO2023]`: 20 prosent material-/klimagassreduksjon uten merkostnad, helst EBA Norge / Grønn Byggallianse / Norsk Eiendom.
   - `[GullbrekkenHolme2025]`: byggfeil 10-30 mrd og feil i halvparten av boliger.
   - `[Mecca2023]`: fulltekst hvis åpent tilgjengelig, ellers bekreft metadata og at betalingsmur gjenstår.
   - `[An2020]`: fulltekst/akseptert manus hvis åpent tilgjengelig; ellers bekreft metadata og at fulltekst gjenstår.
   - SMB-atferd i tilbudsfasen: forskning eller rapporter om hvordan små entreprenører bruker LCA/EPD/digitale beslutningsverktøy.
   - Effektmåling i pilot: kilder eller beste praksis for før/etter, A/B, beslutningsendring, tidsbruk, avvik/omarbeid.

6. **Nye relevante kilder**
   Liste over nye kilder som bør vurderes inn i kildebiblioteket. For hver:
   - tittel
   - utgiver/forfatter
   - URL
   - hva den kan støtte
   - foreslått status: grønn/gul/rød, med begrunnelse

7. **Anbefaling til neste skrivepass**
   Hva bør Codex/Claude gjøre med rent søknadsutkast etter denne reviewen?

## Ikke-mål

- Ikke skriv eller omskriv ren søknadsprosa.
- Ikke endre `docs/reference/prosjektbeskrivelse/` direkte.
- Ikke endre `ipn-kildebibliotek.md` eller `vibs-verified-kildedom-2026-06-27.md`.
- Ikke oppgrader kildestatus i kanoniske dokumenter. Foreslå statusendring i arbeidsdokumentet.
- Ikke bruk egen kunnskap som belegg. Åpen kilde, URL og kort begrunnelse kreves.
- Ikke les `.env`, credentials, tokens eller private vaults.
- Ikke la konkurrentanalyse ta over oppgaven. EG HOLTE / ByggSjekk og andre verktøy er relevante bare hvis de hjelper å vurdere FoU-høyde eller Forskningsråd-kriterier.

## Akseptansekriterier

1. Arbeidsdokumentet finnes på `docs/reference/kildekritikk/kildekritisk-vurdering-og-kriteriegap-v0.1.md`.
2. Dokumentet skiller tydelig mellom eksterne kildehull og prosjektvalg VIBS kan beskrive selv.
3. Alle nye eksterne kilder har URL og kort vurdering av hva de faktisk dokumenterer.
4. Det står eksplisitt hvilke påstander som ikke bør bæres i ren søknadstekst ennå.
5. Forskningsrådets kriterier vurderes konkret, ikke generelt.
6. Ingen kanoniske kildestatusfiler er endret.

## Startprompt (lim inn til AGY i VS Code)

```text
Les docs/handoffs/36_agy_kildekritikk_og_kriteriegap_handoff.md.

Lag arbeidsdokumentet docs/reference/kildekritikk/kildekritisk-vurdering-og-kriteriegap-v0.1.md for VIBS VERIFIED IPN. Oppgaven er kildekritisk vurdering, Forskningsråd-kriteriegap og målrettet åpne kildesøk. Ikke skriv ren søknadsprosa og ikke endre kanoniske kildestatusfiler. Skill tydelig mellom det som må kildeverifiseres eksternt, det Lars/Lars Gunnar må beslutte, og det VIBS kan beskrive som eget FoU-opplegg.
```
