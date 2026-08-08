# AGENTS.md — ipn-verified

Styringsfil for IPN-søknaden **VERIFIED** til Norges forskningsråd (NFR).
Les denne + `CONTEXT.md` før du gjør noe i repoet.

## Hva dette er (og ikke er)

- Dette repoet er **søknadsprosjektet** — selve IPN-søknaden, kildene og verifiseringen.
- Det er **ikke** VIBS-produktet. VIBS (plattform) og VERIFIED (score-modell) er FoU-*objektet* søknaden handler om. Produktkode hører til `vibs-boligpass/`.
- Skilt ut fra `vibs-boligpass/` 2026-06-28 (se `IPN-FLYTTES.md`).

## Utlysning og kriterier (fasit: `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md` §10)

- Utlysning: *Innovasjonsprosjekt i næringslivet — Industri og tjenestenæringer 2026*.
- Vurderingskriterier (0–5 hver): **Kvalitet**, **Effekter**, **Gjennomføring**. Bærekraft vurderes under *Virkninger og effekter*.
- Beløp: 1–16 MNOK, maks 50 % støttesats. Søknadsfrist: løpende. Kun én innsending.

## Kilde- og sannhetsregler (ufravikelige)

1. **Bare åpen, uavhengig sitering teller.** Claudes/agentens egen kunnskap er aldri belegg.
2. **Statusporter:** 🟢 primær åpnet (kan stå alene) · 🟡 sterk men ikke primærverifisert · 🔴 bare søketreff · ⏸ tatt ut av søknadstekst.
3. **Ubekreftet skal vekk fra kanonisk og innsendingsklar søknadstekst** (Lars' regel) — parkeres i kildebiblioteket under `docs/reference/` til kilden er funnet/åpnet.
4. **Bestillingsverk er ikke uavhengig belegg.** Konsortie-interne notater er arbeidsgrunnlag, ikke bevis.
5. Endring av kildestatus skal alltid logges i dokumentets endringslogg.

## Permanent kildeport mot gjenimport

- Maskinlesbar sperreliste: `governance/source-blocklist.json`.
- Validator: `python tools/source_guard.py scan --path <inntak>`.
- Aktiv kontroll: `python tools/source_guard.py scan --active`.
- Sperremekanismer og Lars-port: se `governance/README.md`.

## Roller (ærlighetsregel)

- **Lars Erik / Lars Gunnar:** leser, beslutter, godkjenner. Avgjør grensetilfeller.
- **Claude:** skriver utkast, omformulerer, faktasjekker åpne kilder (Sonar), lager handoffs. Kan **ikke** styre Codex/AGY direkte.
- **Codex / Antigravity (AGY):** utførende agenter i VS Code (kode, retting, verifisering).
- **SINTEF:** primærverifiserer vitenskapelige kilder (midten av august 2026).
- **Sonar:** faktasjekk-verktøy via loopback-API.

## Regler for Søknadstekst (K1–K4 & V1–V3)

- Planlagt fremtidig databasemodell: `ipn.sqlite` (se `IPN-FLYTTES.md` for neste steg).
- For detaljerte sjekkregler, handoffs og ordlydsfasit før du redigerer søknadstekst, se `docs/agents/SOKNADSTEKST_REGLER.md`.

## Agent skills

Repoet bruker Matt Pocock engineering-skills. Se konfigurasjon i `docs/agents/`:

- `docs/agents/skills.md` — skill-katalog og TDD-arbeidsflyt.
- `docs/agents/issue-tracker.md` — lokal saksoppfølging.
- `docs/agents/triage-labels.md` — triage-roller.
- `docs/agents/orchestration.md` — Claude vs. Codex/AGY handoffs.
