Oppgave: Vurder om kandidatene under viser repo-sammenhengsdrift.
Les kun radene under. Ikke finn pa fakta. Returner JSON med ok, flagged_rows, reason, recommended_action.

Repo-regler fra AGENTS/README/CONTEXT:
- Dette repoet er IPN-soknadsprosjektet VERIFIED, ikke VIBS-produktet.
- Produktkode, UI, snekkerpilot og nettside horer til vibs-boligpass, ikke her.
- Startrekkefolge: AGENTS.md -> CONTEXT.md -> INDEX.yml -> IPN-FLYTTES.md.
- INDEX.yml skal vaere filoversikt.

Kandidatsett:

1. Produkt/nettside-materiale finnes likevel i repoet
- README.md sier repoet ikke inneholder produktkode, plattform, UI, pilot, nettside; det ligger i vibs-boligpass.
- AGENTS.md sier produktkode, UI, snekkerpilot og nettside horer til vibs-boligpass, ikke her.
- rg --files viser site/index.html, site/styles.css, site/design-brief.md, site/mockup/index.html, site/mockup/screens og kandidatbilder.
- IPN-FLYTTES.md sier nettside/UI handoff 28 er bevisst igjen i vibs-boligpass, men handoffs 30-34 og site/mockup finnes i dette repoet.

2. INDEX.yml dekker bare deler av repoet
- Deterministisk sjekk: alle 28 stier som er nevnt eksplisitt i INDEX.yml finnes.
- Samtidig lister INDEX.yml ikke site/, .scratch/, skills/ eller de nyere handoffene 30-34.
- INDEX.yml header sier "full filoversikt", men fungerer mer som kurert oversikt.

3. Handoff-nummerdrift
- CONTEXT.md sier "Ingen nummerert handoff #30 dokumenterer at Codex-rettingen/sprakjobben er utfort".
- docs/handoffs inneholder 30_agy_mockup_og_bakgrunnsbilder_handoff.md, 31_agy_mockup_innholdstro_handoff.md, 32_codex_review_mockup_handoff.md, 33_codex_tekst_og_presentasjon_handoff.md, 34_agy_mockup_v2_loft_handoff.md.
- Dette kan bety at CONTEXT mener "ingen #30 for Codex-rettingen", ikke at nummer 30 mangler.

4. Orchestration-doc er utdatert pa neste ledige nummer
- docs/agents/orchestration.md sier handoff-plassering: neste ledige nummer; siste er 29 -> bruk 30+.
- docs/handoffs har allerede 34 som hoyeste nummer.
- Risiko: neste agent kan velge feil nummer hvis orchestration.md leses isolert.

5. Utskilt fra vibs-boligpass ikke ferdig
- CONTEXT.md sier nylig utskilt, originalfiler ligger fortsatt i vibs-boligpass, repoet er ikke git-initiert enna.
- IPN-FLYTTES.md sier kopiert, ikke flyttet/slettet; slett originalene forst etter bekreftelse + git-init.
- Dette er konsistent, men ma regnes som apent arbeid.

6. Kildearbeid og site-arbeid blandet i samme repo
- docs/reference er soknads- og kildegrunnlag.
- site/ og handoffs 30-34 er status-/mockup/nettsidearbeid rundt VERIFIED.
- Hvis repoet skal vaere strengt IPN-soknad, ma site enten merkes som formidlingsflate for soknaden eller flyttes/parkes.
