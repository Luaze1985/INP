---
title: Handoff (Codex) - Uavhengig review av VERIFIED-mockup
date: 2026-06-28
status: ready
from: claude
to: codex
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
tags: [vibs, verified, ipn, site, mockup, review, codex]
---

# Handoff (Codex): Review mockupen mot spec + fang hallusinasjoner

## Kort beskjed

Gjør en **uavhengig review** av AGY sin mockup i `site/mockup/` mot spec-dokumentene og
kildegrunnlaget. Hovedfokus: **fang scope-creep/hallusinasjoner** (påstander mockupen gjør som
*ikke* er dekket av prosjektdokumentene), **kildedisiplin**, **WCAG/a11y** og **kodekvalitet**.
Du **retter ikke** — du leverer en review-rapport; Lars/Claude beslutter.

Server kjører: http://localhost:8000/site/mockup/index.html

## Rollefordeling (ærlighetsregel)

- **Codex (deg):** uavhengig review + rapport. Endrer ikke filene.
- **Claude:** skrev handoffen + spec, og har gjort en første gjennomgang (flaggene under). Styrer deg ikke.
- **Lars Erik:** beslutter hva som rettes.

## Inndata

- `site/mockup/index.html`, `site/mockup/mockup-styles.css` — det som skal reviewes.
- `site/design-brief.md`, `site/innhold-kanban.md` — spec (look, stemme, narrativ, hvilke fakta som kan vises).
- `docs/reference/vibs-verified-kildedom-2026-06-27.md`, `ipn-hovedokument.md`, `state-of-the-art-verified-ipn.md` — **kildegrunnlaget** (sjekk påstandene mot dette).
- `AGENTS.md` — kilde- og sannhetsregler.

## Review-dimensjoner

1. **Hallusinasjon / scope-creep (viktigst).** Sjekk hver påstand i mockupen mot prosjektdokumentene. Flagg alt som ikke er dekket. Claude har allerede mistanke om:
   - `index.html:217` — «sanntidsdata fra byggeplass, sensordokumentasjon» — del av VERIFIED-scope, eller pynt?
   - `index.html:233` — «SINTEF Community» — riktig institutt? Docs sier SINTEF (Vegard Knotten)/Byggforsk.
2. **Kildedisiplin.** Vises bare 🟢-fakta (jf. `innhold-kanban.md`)? Er 🔴 (Wiik 2025, konfliktkostnad) ute? Er 🟡 (byggefeil) fraset som «forskning indikerer», ikke som påstand? (`index.html:151-153` ser riktig ut — bekreft.)
3. **Strategisk innhold.** `index.html:62-63` viser «Søkertall: 1–16 MNOK (50 % støtte)» offentlig. Bør beløpet stå på en offentlig side? Er «Søkertall» riktig begrep (vs. «Søknadsbeløp/Ramme»)?
4. **WCAG / a11y.** Kontrast på dempet subtitle/badges over foto; drawer (`#menu-panel`) — skjult fra tab-rekkefølge når lukket på mobil? Fokushåndtering. Skip-link + `aria-expanded` ser OK ut — bekreft.
5. **NFR-kriterier implisitt.** Nevnes Kvalitet/Effekter/Gjennomføring eksplisitt noe sted? (Skal *ikke*.)
6. **Kodekvalitet.** Semantisk HTML, hederlig CSS, ingen åpenbare feil. Småting: `index.html:239` «ledelse av» (grammatikk).
7. **Merkevare.** Eksakt `#11111f`/`#ffc600`/`#ffffff`, Comfortaa, VERIFIED foregrunnet, VIBS/SINTEF kun som partnere.

## Det du skal levere

- `site/mockup/review-codex.md`: funn per dimensjon, hver med **fil:linje, alvorlighet** (blokkerende / bør / nice-to-have) og forslag. Skill **bekreftet feil/hallusinasjon** fra **stil/smak**.

## Ikke-mål

- Ikke rett filene (review only). Ikke rør `site/index.html` (Lars sin lærings-fil), `site/styles.css`, `scrollspy.js` eller `docs/reference/`.

## Akseptansekriterier

1. Hver påstand i mockupen er sjekket mot kildegrunnlaget; hallusinasjoner/scope-creep er eksplisitt flagget med fil:linje.
2. WCAG-kontrast er vurdert; a11y-gap notert.
3. Rapporten skiller bekreftede feil fra smak/preferanse.

## Startprompt (lim inn til Codex i VS Code)

```text
Jobb i repoet C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified.
Les docs/handoffs/32_codex_review_mockup_handoff.md, site/design-brief.md og
site/innhold-kanban.md.

Gjør en UAVHENGIG review av mockupen i site/mockup/ (index.html + mockup-styles.css).
Server: http://localhost:8000/site/mockup/index.html. Du RETTER IKKE — lever rapport.

Hovedfokus: fang hallusinasjoner/scope-creep — sjekk HVER påstand i mockupen mot
docs/reference/ (kildedom, ipn-hovedokument, state-of-the-art). Sjekk spesielt:
- index.html:217 «sanntidsdata fra byggeplass, sensordokumentasjon» — i scope eller pynt?
- index.html:233 «SINTEF Community» — riktig institutt?
- index.html:62-63 «Søkertall: 1–16 MNOK» — bør beløpet vises offentlig? riktig begrep?
Sjekk også: kildedisiplin (kun 🟢-fakta, 🔴 ute, 🟡 fraset som «forskning indikerer»),
WCAG-kontrast + drawer-fokus/tab-orden, at NFR-kriteriene ikke nevnes eksplisitt,
kodekvalitet, og eksakt merkevare (#11111f/#ffc600, Comfortaa, VERIFIED foregrunnet).

Skriv funnene til site/mockup/review-codex.md: per funn fil:linje + alvorlighet
(blokkerende/bør/nice) + forslag. Skill bekreftet feil fra smak. Ikke rør andre filer.
```
