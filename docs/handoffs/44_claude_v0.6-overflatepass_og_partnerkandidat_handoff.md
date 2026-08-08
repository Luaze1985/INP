---
title: Handoff (Claude) - avgrenset v0.6-overflatepass og partnerkandidat
date: 2026-08-05
status: ready-for-human
from: codex
to: claude
branch: change/tekstpresisering-v0.5
tags: [vibs, verified, ipn, v0.6, writing, partner-review]
neste_ledige_handoff: 45
---

# Handoff: gjør v0.6 partnerlesbar innen 2–3 timer

## Kort beskjed

Orkestrer et avgrenset pass på dagens v0.6. Målet er mer konkret innhold,
bedre struktur, mindre KI-preg og mer forsiktige løfter før teksten deles som
arbeidsgrunnlag med samarbeidspartnere. Ikke løs forskningsmetode,
leverandørsoliditet, nye bærekraftsmål, arbeidspakker, budsjett eller
kildestatus i denne runden.

## Rollefordeling

- **Claude:** orkestrerer passet og skriver seksjonsvise forslag innenfor
  tillatt scope.
- **Lars:** godkjenner ordlyd, åpne valg, kildestatus og ekstern sending.
- **Codex:** kan senere kontrollere diff, Source Guard, språkport og PDF.
- **Forskningspartner:** eier senere metode- og testavklaringer.

## Les først

1. `AGENTS.md`
2. `CONTEXT.md`
3. `INDEX.yml`
4. `docs/reference/prosjektbeskrivelse/README.md`
5. `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.6.md`
6. `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.6.md`
7. `docs/reference/prosjektbeskrivelse/reviews/2026-08-05-tilbakemeldingsregister-v0.6.md`
8. `docs/reference/prosjektbeskrivelse/reviews/2026-08-05-v0.6-overflatepass-2-3-timer.md`
9. `docs/sintef/internt/sprakport-v0.6.md`
10. `governance/README.md` og `governance/source-blocklist.json`

`CONTEXT.md` er utdatert på versjonsstatus: den omtaler v0.5 som aktiv, mens
README og INDEX registrerer v0.6 som aktiv kontrollkandidat. Følg README og
INDEX for denne oppgaven og flagg senere oppdatering av CONTEXT.

## Det du skal levere

1. Et forslag til avgrenset redigering av
   `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.6.md`.
2. En kort resultatrapport i
   `docs/reference/prosjektbeskrivelse/reviews/2026-08-05-v0.6-overflatepass-resultat.md`.
3. En beslutningsliste til Lars for de punktene som må stå åpne.
4. Etter godkjenning og teknisk kontroll: oppdatert partnerlesbar PDF i
   `output/pdf/soknadstekst-samlet-kandidat-v0.6.pdf`.

## Pålagt arbeidsmåte

1. Følg tids- og endringsgrensene i overflatepass-sjekklisten.
2. Arbeid én seksjon om gangen.
3. Vis kort før/etter eller konkret endringsforslag før større flytting.
4. Bruk registrerte kilder bare til godkjent bevisrolle.
5. La usikre tall og åpne metodevalg stå ute av prosaen.
6. Kjør språkport og Source Guard før kandidaten regnes som klar.
7. Stopp ved Lars' godkjenning før ekstern sending.

## Ikke-mål

- Ikke endre v0.4, v0.5, kanoniske K/V-filer, nettsiden eller
  kilderegisterets status.
- Ikke bruk 80–90 prosent for små bedrifter uten kontrollert original.
- Ikke legg leverandørsoliditet eller konkursrisiko inn som nytt kriterium.
- Ikke fastsett forskningsmetode, testprotokoll, arbeidspakker eller budsjett.
- Ikke oppgi partnernavn eller roller som bekreftet uten dokumentasjon.
- Ikke send e-post eller dokumenter til samarbeidspartnere.

## Akseptansekriterier

1. Alle rader merket `GJØR I v0.6` er adressert eller eksplisitt begrunnet.
2. Alle rader merket `GJØR FORSIKTIG I v0.6` har forsiktig ordlyd uten nye
   faglige løfter.
3. K1 beskriver problemet og K2 samler hva VERIFIED skal gjøre.
4. Reduzer er behandlet med positivt dokumentert funksjon og riktig
   avgrensning, eller parkert med konkret kildegrunn.
5. «Bruker», intern selvinstruksjon og mekanisk KI-rytme er fjernet.
6. Source Guard gir null treff på målfilen.
7. Resultatrapporten skiller endret, parkert og beslutningsåpent.

## Foreslåtte skills

- `ai-sprakvask-no` for det avgrensede språkpasset.
- `grill-with-docs` bare når en faktisk beslutning må tas av Lars.
- `research` kun ved en separat, godkjent kildeoppgave.
- `handoff` når v0.6-passet er ferdig og skal til kontroll.

## Startprompt til Claude

```text
Les docs/handoffs/44_claude_v0.6-overflatepass_og_partnerkandidat_handoff.md
og alle filene under «Les først». Orkestrer et avgrenset 2–3 timers pass på
soknadstekst-samlet-kandidat-v0.6.md. Gjør teksten mer konkret, konsistent og
partnerlesbar, og løs KI-språk, gjentakelser og for sterke løfter innenfor
overflatepass-sjekklisten. Ikke avgjør metode, nye datadimensjoner,
partnerforpliktelser, arbeidspakker, budsjett eller kildestatus. Arbeid
seksjonsvis og stopp ved Lars' godkjenning før ekstern sending.
```

