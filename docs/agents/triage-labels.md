# Triage-labels

Skillene snakker i fem kanoniske triage-roller. Denne filen mapper rollene til strengene vi bruker
i `ipn-verified`, og kobler dem mot status-portene i `AGENTS.md`.

| Rolle (mattpocock/skills) | Streng her        | Betydning i dette repoet                                              |
| ------------------------- | ----------------- | -------------------------------------------------------------------- |
| `needs-triage`            | `needs-triage`    | Ny sak, ikke vurdert ennå                                            |
| `needs-info`              | `needs-info`      | Mangler info/kilde — typisk knyttet til 🟡/🔴 (trenger primæråpning) |
| `ready-for-agent`         | `ready-for-agent` | Fullt spesifisert, klar for AFK-agent (Codex/AGY). Innholdssaker: kilde bør være 🟢 |
| `ready-for-human`         | `ready-for-human` | Krever Lars' beslutning (grensetilfeller, irreversible endringer)    |
| `wontfix`                 | `parkert`         | Tatt ut / ⏸ parkert med gjeninnsettingsvilkår (slettes aldri)        |

## Viktig skille

**Triage-tilstand ≠ kildestatus.** Triage sier om *saken* er klar å jobbe med; status-portene sier
om *belegget* er åpnet. En sak kan være klar (`ready-for-agent`) mens en kilde fortsatt er 🟡 —
løsningen er da å frasere med forbehold eller ikke la kilden bære setningen, ikke å blokkere saken.

Når en skill nevner en rolle (f.eks. «sett AFK-klar label»), bruk strengen fra tabellen over.
