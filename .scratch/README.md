# .scratch — lokal issue-tracker

Saker og PRD-er for `ipn-verified` ligger her som markdown. Se `docs/agents/issue-tracker.md`.

## Struktur

```
.scratch/
└── <feature-slug>/
    ├── PRD.md
    └── issues/
        ├── 01-<slug>.md
        └── 02-<slug>.md
```

- Triage-tilstand: `Status:`-linje øverst i hver oppgavefil (se `docs/agents/triage-labels.md`).
- Kommentarer/historikk: nederst under `## Kommentarer`.

Mapper opprettes når en feature faktisk starter — denne filen dokumenterer bare konvensjonen.
