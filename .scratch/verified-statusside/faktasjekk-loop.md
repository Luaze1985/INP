# Faktasjekk-loop — VERIFIED statusside

Gjenbrukbar sannhetssjekk for sideteksten. Kjøres på loop (se «Kadens») eller på forespørsel.
Formål: fange nye hallusinasjoner/scope-creep når agenter eller mennesker redigerer siden, og
fange status-endringer når SINTEF primærverifiserer kilder (fra midten av august 2026).

## Hva loopen gjør (prompt som kjøres)

```text
Streng, uavhengig faktasjekk av VERIFIED-statussiden.

Sjekk all synlig tekst i site/mockup/index.html (overskrifter, avsnitt, faktakort,
sidemeny, partnerstripe, nøkkelpersoner) mot kildegrunnlaget:
- docs/reference/vibs-verified-kildedom-2026-06-27.md
- docs/reference/ipn-hovedokument.md
- docs/reference/state-of-the-art-verified-ipn.md
- docs/reference/ipn-samledokument.md
- AGENTS.md (status-porter 🟢🟡🔴⏸)
- site/innhold-kanban.md (hvilke fakta er 🟢)
- ../vibs-boligpass/docs/business/gronn-plattform.md (konsortium/partnere)

For HVER påstand: sett 🟢 (åpen kilde bekrefter) / 🟡 (sterk, ikke primærverifisert) /
🔴 (motsies eller ikke dekket = hallusinasjon) / ⚪ (kan ikke verifiseres fra docs).
Oppgi kilde for 🟢/🟡. Flagg ny hallusinasjon/scope-creep eksplisitt.

Sjekk spesielt: at 🔴-kilder (Wiik 2025, konfliktkostnad 2,2 mrd) IKKE brukes som påstand;
at byggefeiltallet er fraset «forskning indikerer» (🟡); at NFR-kriteriene ikke nevnes
eksplisitt; at ingen statusfarger lekker til siden; og at tall + konsortium + navn stemmer.

Skriv rapport til site/mockup/faktasjekk-<DATO>.md (domstabell + handlingsliste +
konklusjon). VARSLE tydelig hvis noe er 🔴 eller en ny hallusinasjon er introdusert.
Ikke rett teksten — bare rapporter.
```

## Kadens (anbefaling)

- **Mens siden aktivt redigeres:** kjør på forespørsel etter hver større endringsrunde.
- **Løpende drift-vakt:** ukentlig er nok inntil innhold er låst.
- **Rundt SINTEF-verifisering (fra ~15. aug 2026):** tettere (f.eks. daglig) for å fange 🟡→🟢/🔴.

## Hva som skjer ved funn

- **🔴 / ny hallusinasjon:** rett umiddelbart (eller flagg til Lars hvis det krever domenebeslutning).
- **🟡→🟢:** oppdater `innhold-kanban.md` og ev. ordlyd (kan nå stå som påstand).
- **🟡→🔴:** ta påstanden ut av siden (kildedisiplin).

## Kjøringslogg
- 2026-06-28: 19 🟢 / 2 🟡 / 0 🔴 / 3 ⚪ — kildedisiplin-klar. Rettet: byggefeil-ordlyd, 3,3 %-årstall. Åpent: «Thomas Thorsen» (ikke i docs — Lars bekreftet manuelt).
- 2026-06-29: 0 🔴. Rettet H0 (hero nåtid→«under kvalitetssikring av SINTEF fra august 2026»), H2 («broen»→«veien»). Bjørheim2026/BDO2025/UNION2025 lagt til i kildedomet som 🟡. Åpent: Thomas Thorsen (akseptert manuelt), SINTEF-primærverifisering av 3 nye 🟡 venter til aug 2026.
