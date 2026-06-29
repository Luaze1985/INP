# Codex triage of Gemma all-source audit

Run date: 2026-06-28

## Inputs

- Source library: `docs/reference/ipn-kildebibliotek.md`
- Historical kildedom: `docs/reference/vibs-verified-kildedom-2026-06-27.md`
- Canonical docs checked:
  - `docs/reference/ipn-hovedokument.md`
  - `docs/reference/ipn-samledokument.md`
  - `docs/reference/ipn-prosjektbeskrivelse-utkast.md`

## Execution

- Parsed 60 source rows from `ipn-kildebibliotek.md`.
- Built 8 compact Gemma batches.
- 4 large batches returned valid JSON directly.
- 4 large batches failed JSON validation and were split into 14 microbatches.
- Final accepted report count: 18 JSON reports.
- Guard result: all accepted reports passed `gemma_report_guard.py`.
- Gemma flagged 16 source keys.

## Strong findings

These should be treated as real follow-up items.

### `SA2018` - Codex override, not caught in final all-source Gemma pass

- Current docs: `CONTEXT.md`, `ipn-kildebibliotek.md`, `ipn-hovedokument.md`, and `ipn-samledokument.md` treat `SA2018` / 2.2 mrd as not open-located and parked.
- Historical kildedom still says `SA2018` is green/bekreftet and recommends replacing `Harerusten2022` with it.
- Action: mark `vibs-verified-kildedom-2026-06-27.md` as historical/superseded on this point, or amend it with a 2026-06-28 override note.

### `Mecca2023`

- Current library and canonical docs treat it as yellow because Wiley full text is not opened.
- Historical kildedom marks it green/bekreftet while also saying it is behind Wiley payment wall.
- Action: keep yellow in current canon until full text is opened, and add an override note to kildedom or a later decision log.

### `GullbrekkenHolme2025`

- Current `CONTEXT.md` and `ipn-kildebibliotek.md` treat it as yellow pending SINTEF full text.
- Historical kildedom marks it green/bekreftet.
- It carries the 10-30 mrd NOK/year building-defect problem statement in the application prose.
- Action: either source the number from a current green/open source, or keep explicit yellow-margin note until SINTEF opens full text.

### `An2020`

- Current docs handle it mostly correctly: commercial CMBS/naringsbygg only, not residential mortgage proof.
- Risk remains because the historical kildedom contains old correction text around `[An2021]`, 32/34 percent, and green examples.
- Action: keep current yellow status and avoid using the 34 percent figure as bearing until full text/accepted manuscript is opened.

### `NOBB`

- It is yellow in the source library but is used as practical data infrastructure in F2/WP1.
- This is not necessarily wrong, but it is a bearing infrastructure assumption.
- Action: add a clearer note that NOBB is known industry infrastructure but not yet independently opened/verified in this source pass.

## Watchlist, lower urgency

These are not immediate misuse in the canonical docs, but should stay visible.

- `Wiik2025`: currently parked correctly. Keep parked unless SINTEF documents the note.
- `Harerusten2022`: current library says secondary/not bearing. Do not reintroduce the 2.2 mrd claim through Harerusten.
- `Refleksjonsnotat2026`: not siterbar; okay as internal trace only. Gemma's "remove all references" is too strong, but active application prose must not cite it.
- `MCDM2025`: red. Do not cite until upgraded.
- `CPR2024`: Gemma flagged legal/technical interpretation risk, but current use looks acceptable as long as it stays high-level.

## Likely Gemma noise

Gemma flagged these mainly because they are yellow or unused. That is not itself a defect.

- `ISO14040`
- `EN15804`
- `ISO15686-5`
- `RICS-WLC`
- `Ciroth2016`
- `EEMI`
- `OneClickLCA`

Action: no document change solely from these flags. Only revisit if they become bearing claims in the application prose.

## Verdict on forcing Gemma

Works, but only with guardrails.

- Good: JSON validation + non-empty `flagged_rows` forced actionable output.
- Good: microbatch retry fixed invalid/truncated Gemma output.
- Weak: Gemma still overflags yellow/unused sources and missed `SA2018` in the final all-source pass.
- Practical score for this run: 7/10.
