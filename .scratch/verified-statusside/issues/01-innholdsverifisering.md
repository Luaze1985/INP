# 01 — Innholdsverifisering & retting

Status: ready-for-agent

**Feature:** verified-statusside · **Type:** tekst · **Prioritet:** tracer bullet (gjør først)

## Mål
All tekst på siden må være sann og dekket av kildegrunnlaget. Samle og rett alle påstander før copy låses.

## Omfang
- Avklar Claudes 3 flagg:
  - `mockup/index.html:217` — «sanntidsdata fra byggeplass, sensordokumentasjon»: i VERIFIED-scope eller pynt?
  - `mockup/index.html:233` — «SINTEF Community»: riktig institutt? (Docs: SINTEF / Vegard Knotten / Byggforsk.)
  - `mockup/index.html:62-63` — «Søkertall: 1–16 MNOK»: skal beløpet vises offentlig? Riktig begrep?
- Innarbeid funn fra Codex-review (#32) hvis den kjøres.
- Sjekk hver påstand mot `site/innhold-kanban.md` (🟢) og `docs/reference/` (kildedom, hovedokument, state-of-the-art).

## Definition of Done
- [ ] Hver påstand sporet til 🟢 i `innhold-kanban.md`, eller fraset som «forskning indikerer» (🟡).
- [ ] Ingen 🔴-påstander (Wiik 2025, konfliktkostnad).
- [ ] De 3 flaggene rettet eller eksplisitt bekreftet.
- [ ] Scope-påstander (sensordata o.l.) verifisert mot kildegrunnlaget eller fjernet.

## Avhengigheter
- Blokkert av: Codex-review #32 (for å batche funn) — kan også gjøres direkte i tekst-handoffen #33.
- Blokkerer: 02, 03.

## Kommentarer
