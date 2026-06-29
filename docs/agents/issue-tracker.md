# Issue tracker: lokal markdown

Saker og PRD-er for `ipn-verified` ligger som markdown-filer i `.scratch/`.
(Repoet har ingen git-remote ennå → ingen GitHub Issues. Bytt til `gh` hvis remote opprettes.)

## Konvensjoner

- Én feature per mappe: `.scratch/<feature-slug>/`
- PRD-en er `.scratch/<feature-slug>/PRD.md`
- Oppgaver er `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, nummerert fra `01`
- Triage-tilstand skrives som en `Status:`-linje øverst i hver oppgavefil
  (se `triage-labels.md` for rolle-strengene)
- Kommentarer/historikk legges nederst under en `## Kommentarer`-overskrift

## Når en skill sier «publiser til issue-trackeren»

Opprett en ny fil under `.scratch/<feature-slug>/` (lag mappen om den mangler).

## Når en skill sier «hent relevant sak»

Les filen på den oppgitte stien. Lars sender normalt sti eller saksnummer direkte.

## Forhold til kildedisiplinen

Issue-triage (er saken klar?) og kildestatus (🟢🟡🔴⏸, er belegget åpnet?) er **to ulike akser**.
En sak kan være `ready-for-agent` selv om en kilde fortsatt er 🟡 — men da må selve søknadsteksten
ikke la den uverifiserte kilden bære setningen (se `AGENTS.md` → kilderegler).
