# Kontrollrapport for dokumentpakken

Dato: 2026-08-03
Kontrollør: Codex hovedagent, med separat skrivebeskyttet agentkontroll
Resultat: bestått med rettede dokumentavvik

## Kontrollert omfang

- fire kollegatekster;
- uttaks- og sperrelogg;
- endringskart for tre aktive søknads-/reviewflater;
- endringskart for IPN-nettsiden;
- lagret, ikke sendt SINTEF-pakke;
- sentral README, arbeidspakker og registrering i repoets innganger.

## Resultater

| Kontroll | Resultat | Merknad |
| --- | --- | --- |
| Alle avtalte leveranser finnes | **Bestått** | 14 opprinnelig avtalte filer finnes og er ikke tomme. Denne rapporten er kontrollleveransen i tillegg. |
| Aktiv søknad er urørt | **Bestått** | SHA-256 er uendret for de tre aktive reviewfilene. |
| IPN-nettsiden er urørt | **Bestått** | SHA-256 er uendret for `tekstmanus.md`, `innhold-kanban.md` og `index.html`. |
| Kildebibliotek og kildedom er urørt | **Bestått** | SHA-256 er uendret for begge filene. |
| Ingen Perplexity-status er oppgradert | **Bestått** | Funnene brukes som kontrollspor, ikke originalverifisering. |
| Usikre uttak er synlige | **Bestått** | `UTTATT-USIKKER` og `original-required` brukes for bærende bruk som krever original. |
| Identitet beholdes mot gjenimport | **Bestått** | Sperreloggen har 11 unike `SP-*`-poster med alias, restbruk og gjenåpningsregel. |
| Bare Lars beslutter og gjenåpner | **Bestått etter retting** | Kollegatekstene sier nå at kollegaer gir innspill, mens Lars beslutter. |
| SINTEF-pakken er lagret, ikke sendt | **Bestått** | Status og godkjenningsport sier uttrykkelig `IKKE SENDT` og `IKKE GODKJENT`. |
| Søknads- og nettsidekart er tørrkjøring | **Bestått** | Kartene foreslår handlinger, men gjennomfører ingen. |
| Uavhengig P0/P1-kontroll | **Bestått** | Ingen kritiske avvik ble funnet. Fem P1-avvik ble rettet og bestod retest 5/5. |

## Avvik som ble rettet i kontrollen

1. Kollegapakken kunne leses som at kollegaene godkjenner arbeidsdelingen.
   Dette er endret til at kollegaene gir innspill og Lars alene beslutter.
2. Sperreloggen inneholdt en ekstra Mecca-tittel som ikke kunne spores i det
   avtalte kontrollgrunnlaget eller de leverte arbeidsloggene. Oppføringen ble
   fjernet, og sperre-ID-ene ble gjort sammenhengende.
3. Wiik var formulert som permanent pensjonert selv om handoff 41 bare krevde
   vurdering. Den er nå `UTTATT-USIKKER / original-required`, med separat krav
   om vurdering av uavhengighet og Lars-beslutning.
4. Bjørheim ble fortsatt beholdt som belegg for konkurstallet uten registrert
   original. Nå er også denne rollen `original-required`; identiteten beholdes
   bare som kandidatspor.
5. En gammel `SP-12`-peker ble rettet til eksisterende `SP-11`.
6. Kollegateksten om Wiik ble utvidet med bestillingsverk-/uavhengighetsregelen.
7. EBA-tallet på 20 prosent ble flyttet fra **Behold** til **Avklar**, med krav
   om original, avgrensning og Lars-godkjenning.

## Åpne forhold som ikke er dokumentfeil

- `SA2018` har motstridende eldre og nyere status.
- `KD2024`, Multiconsult/DiBK og Asplan Viak må identitetsavstemmes.
- Perplexity-leveransen er uenig om fulltekst for Mecca, Benke og Lohman.
- BDO-, UNION- og BKA2-tall trenger entydige originaler.
- Partnerroller, offentlighetsnivå og eventuell SINTEF-omtale på nettsiden må
  besluttes før publisering.

Disse punktene er beholdt som synlige avklaringer. De er ikke fylt med
antakelser.

## Konklusjon

Dokumentpakken kan brukes som internt beslutningsgrunnlag og som lettlest
kollegemateriale. Den autoriserer ikke endringer i søknad, nettside eller
kildestatus. Neste irreversible eller eksterne handling krever Lars'
uttrykkelige godkjenning.
