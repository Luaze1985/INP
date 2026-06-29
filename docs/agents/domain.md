# Domenedokumenter

Hvilke dokumenter skillene skal lese for å forstå domenet før de jobber i dette repoet.

## Les disse før utforsking

- **`AGENTS.md`** (rot) — styringsregler, roller, kilde- og sannhetsregler, status-porter.
- **`CONTEXT.md`** (rot) — gjeldende tilstand, åpne risikoer, blokkere.
- **`INDEX.yml`** (rot) — strukturert filinventar (hva ligger hvor).
- **`docs/reference/vibs-verified-kildedom-2026-06-27.md`** — konsolidert kildeverifiseringstilstand
  («kildedommen»), sannhetskilden for hvilke kilder som er 🟢/🟡/🔴/⏸.

Finnes ikke en fil → gå videre stille. Ikke flagg fravær eller foreslå å opprette dem uoppfordret.

## Bruk domenets vokabular

Når output navngir et domenebegrep (sakstittel, hypotese, testnavn, refaktorforslag), bruk begrepet
slik det er definert i `AGENTS.md`/`CONTEXT.md`. Ikke drift til synonymer. Sentrale begreper:
VERIFIED (score-modell), VIBS (plattform/produkt), kildedom, status-porter (🟢🟡🔴⏸),
kanonisk dokument, handoff.

## Flagg konflikter

Hvis output motsier en kilderegel i `AGENTS.md` eller en beslutning i kildedommen, **si det
eksplisitt** i stedet for å overstyre stille:

> _Motsier AGENTS.md §kilderegel 3 (ubekreftet skal helt vekk) — men verdt å ta opp fordi …_
