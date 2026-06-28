# IPN FLYTTES — flyttemanifest

**Dato:** 2026-06-28 · **Status:** kopiert til `ipn-verified/`, originaler beholdt i `vibs-boligpass/`.

IPN-materialet er **kopiert** (ikke flyttet/slettet) ut av produkt-repoet `vibs-boligpass/` til dette
selvstendige `ipn-verified/`. Originalene står igjen til Lars har bekreftet at uttrekket er komplett
og repoet er git-initiert. Da slettes originalene fra `vibs-boligpass/` (steg 3 under).

## 1. Kopiert hit (119 filer)

| Fra `vibs-boligpass/` | Til `ipn-verified/` |
| --- | --- |
| `docs/reference/ipn-*.md` + `ipn-samledokument.pdf` | `docs/reference/` |
| `docs/reference/vibs-verified-*.md` (6) | `docs/reference/` |
| `docs/reference/state-of-the-art-verified-ipn.md`, `…-leseark-…html` | `docs/reference/` |
| `docs/reference/boligspor-innovasjon-notat.md` | `docs/reference/` |
| `docs/reference/forskning-kunnskapsbase.md`, `forskningsekstraksjon-…md` | `docs/reference/` |
| `docs/reference/claude-guardrails.md` | `docs/reference/` |
| `docs/context/windows-score/{26,27,29}_*.md` | `docs/handoffs/` |
| `VIBS_VERIFIED_FoU-panel.docx` | `panel/` |
| `.agents/*` (reconciliation + teamwork_preview) | `provenance/agents/` |

## 2. Bevisst IGJEN i vibs-boligpass (produkt, ikke IPN)

- `docs/reference/{datamodell,produkt-passport-dryguard,incitamentsystem,bank-forsikring}.md` — produktdomene.
- `docs/context/windows-score/28_antigravity_verified_nettside_handoff.md` — nettside/UI = produkt.
- `VIBS_ByggSpor_FoU-panel.docx` — annen produktlinje (ByggSpor), ikke VERIFIED-søknaden.
- All appkode (`api/`, `src/`, `netlify/`, `multi-agent-poc/`, …).

→ Vurder disse hvis noe av dem likevel skal bære søknaden.

## 3. Gjenstår (krever din bekreftelse — IKKE gjort)

1. **Bekreft** at uttrekket over er komplett og riktig avgrenset.
2. **Git-init** `ipn-verified/` som eget repo (`git init`, `.gitignore`, første commit).
3. **Slett originalene** fra `vibs-boligpass/` (de som er listet i del 1) — først etter steg 1–2.
   Marker i `vibs-boligpass/` ligger i `docs/reference/_IPN-FLYTTET-UT.md`.
4. **Oppdater kryssreferanser:** noen dokumenter peker på `forskning-kunnskapsbase.md` o.l. med
   relative stier — sjekk at de fortsatt stemmer etter sletting.

## 4. Neste steg (dokumentdatabasert, jf. AGENTS.md)

Innfør `ipn.sqlite` som sannhetskilde for kilder/påstander/status; generer de kanoniske
markdown-dokumentene fra basen. Tabeller: `sources`, `claims`, `claim_sources`,
`source_verifications`, `audit_log` med statusverdier i stedet for emoji.
