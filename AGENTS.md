# AGENTS.md — ipn-verified

Styringsfil for IPN-søknaden **VERIFIED** til Norges forskningsråd (NFR).
Les denne + `CONTEXT.md` før du gjør noe i repoet.

## Hva dette er (og ikke er)

- Dette repoet er **søknadsprosjektet** — selve IPN-søknaden, kildene og verifiseringen.
- Det er **ikke** VIBS-produktet. VIBS (plattform) og VERIFIED (score-modell) er FoU-*objektet* søknaden handler om. Produktkode, UI og snekkerpilot hører til `vibs-boligpass/` — ikke her.
- **Unntak: `site/`.** Den offentlige statussiden for VERIFIED bygges og publiseres herfra (`site/web/`, deployet av Vercel). Den er søknadskommunikasjon, ikke produkt. Regelen for den er enkel: **siden skal aldri si mer enn gjeldende søknadstekst sier.** Se `site/arbeid/faktasjekk-2026-08-07.md`.
- Skilt ut fra `vibs-boligpass/` 2026-06-28 (se `IPN-FLYTTES.md`).

## Utlysning og kriterier (fasit: `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md` §10)

- Utlysning: *Innovasjonsprosjekt i næringslivet — Industri og tjenestenæringer 2026*.
- Vurderingskriterier (0–5 hver): **Kvalitet**, **Effekter**, **Gjennomføring**. Bærekraft vurderes under *Virkninger og effekter*.
- Beløp: 1–16 MNOK, maks 50 % støttesats. Søknadsfrist: løpende. Kun én innsending.

## Kilde- og sannhetsregler (ufravikelige)

1. **Bare åpen, uavhengig sitering teller.** Claudes/agentens egen kunnskap er aldri belegg.
2. **Statusporter:** 🟢 primær åpnet (kan stå alene) · 🟡 sterk men ikke primærverifisert (må åpnes / fraseres med forbehold) · 🔴 bare søketreff (ikke siterbar) · ⏸ tatt ut av søknadstekst, parkert med gjeninnsettingsvilkår.
3. **Ubekreftet skal helt vekk fra søknadsteksten** (Lars' regel) — men ikke slettes: parkeres i `ipn-hovedokument.md` / `ipn-kildebibliotek.md` og kan «stå opp som ja» (→ 🟢) når kilden er funnet/åpnet.
4. **Bestillingsverk er ikke uavhengig belegg.** Konsortie-interne notater er arbeidsgrunnlag, ikke bevis.
5. Endring av kildestatus skal alltid logges i dokumentets endringslogg (hvem, hva, hvorfor).

## Roller (ærlighetsregel)

- **Lars Erik / Lars Gunnar:** leser, beslutter, godkjenner. Avgjør grensetilfeller.
- **Claude:** skriver utkast, omformulerer, faktasjekker åpne kilder (Sonar), lager handoffs. Kan **ikke** styre Codex/AGY direkte — lager handoff-filer de leser i VS Code. Rollespill som «Codex/AGY-agent» er forbudt.
- **Codex / Antigravity (AGY):** utførende agenter i VS Code (kode, retting, verifisering).
- **SINTEF:** primærverifiserer vitenskapelige kilder mot original. Kommer inn **midten av august 2026**.
- **Sonar:** faktasjekk-verktøy (loopback-API), ikke en agent.

## Retning: dokumentdatabasert (mål)

Dagens kildebibliotek er en database skrevet for hånd i markdown. Måljustering mot prinsippene i
`Produksjonsbase/.../ki_database_kodingsprinsipper.md`: innfør `ipn.sqlite` som sannhetskilde
(`sources`, `claims`, `claim_sources`, `source_verifications`, `audit_log`) med statusverdiene
`imported/suggested/uncertain/approved/rejected/conflict/outdated/manually_edited` i stedet for emoji.
Markdown blir da visningslag, generert fra basen. Se `IPN-FLYTTES.md` → «Neste steg».

## Før du redigerer søknadstekst

- **Gjeldende samlet søknadstekst er `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.9.md`** (2026-08-07). Den navngir ingen partnere og ingen personer, og oppgir ingen prosentsatser som ikke er kontrollert mot originalanalysen. Ikke legg dette tilbake uten at Lars har bestemt det.
- Hvilket dokument er kanonisk for endringen? (skjelett = `ipn-hovedokument.md`, prosa = `ipn-samledokument.md` / `ipn-prosjektbeskrivelse-utkast.md`)
- Er kilden 🟢? Hvis ikke — ikke la den bære setningen.
- Logg endringen i endringsloggen.
- Spør Lars før irreversible endringer.

## Agent skills

Repoet bruker Matt Pocock engineering-skills. Per-repo konfig ligger i `docs/agents/`:

- **`docs/agents/skills.md`** — skill-katalog, arbeidsflyt (idé → PRD → oppgaver → triage → TDD → handoff) og «hvilken skill, når»-tabell. Inneholder også kodeprinsipper (Security-first + Red/Green TDD, proporsjonalt anvendt).
- **`docs/agents/issue-tracker.md`** — saker/PRD-er som lokal markdown i `.scratch/` (ingen git-remote ennå).
- **`docs/agents/triage-labels.md`** — triage-roller mappet mot status-portene (🟢🟡🔴⏸). Merk: triage-tilstand ≠ kildestatus.
- **`docs/agents/domain.md`** — hvilke dokumenter skillene leser før de jobber.
- **`docs/agents/orchestration.md`** — Claude-subagenter vs. handoffs til Codex/AGY (følger ærlighetsregelen over).

Skillene endrer ikke kilde- og sannhetsreglene over — de er rammeverket for *hvordan* arbeid drives, ikke for *hva som teller som belegg*.
