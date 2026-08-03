---
title: Handoff (AGY) - State of the art og SINTEF-rapport
date: 2026-08-02
status: ready
from: codex
to: antigravity (AGY)
branch: change/tekstpresisering-v0.5
tags: [vibs, verified, ipn, state-of-the-art, sintef, research]
---

# Handoff (AGY): utfordre state of the art før SINTEF-rapporten ferdigstilles

## Kort beskjed

Bruk Antigravity-agentene til en read-only forsknings- og utfordrerunde. Målet er å finne åpne primærkilder, moteksempler og presise forskningsgap som gjør den kommende SINTEF-rapporten sterkere. Ikke skriv søknadstekst og ikke endre kanoniske filer.

## Rollefordeling

- **AGY-agentene:** utforsker, kildejakter, utfordrer og kvalitetskontrollerer.
- **Codex:** samler AGY-resultatet med avgrenset Sonar-kontroll og bygger rapportutkastet.
- **Lars:** starter AGY manuelt, vurderer grensetilfeller og godkjenner rapport/mottakere.
- **SINTEF:** primærverifiserer vitenskapelige kilder og gir faglige korreksjoner.

## Inndata

- `AGENTS.md`
- `CONTEXT.md`
- `docs/agents/domain.md`
- `docs/agents/orchestration.md`
- `.scratch/research-intake/gen-2026-07-29-01/README.md`
- `.scratch/research-intake/gen-2026-07-29-01/work/pastandsregister.md`
- `.scratch/research-intake/gen-2026-07-29-01/work/forelopig-kildedom.md`
- `.scratch/research-intake/gen-2026-07-29-01/factchecks/`
- `.scratch/research-intake/gen-2026-07-29-01/sintef/`
- `docs/reference/state-of-the-art-verified-ipn.md`
- `docs/reference/vibs-verified-kildedom-2026-06-27.md`
- `docs/reference/ipn-kildebibliotek.md`
- `research/evidence_matrix.md`
- `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.4.md`
- `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.5.md`

## Agentoppsett

Bruk minst disse fire rollene, enten som separate agenter eller tydelig separate pass:

1. **Metode- og forskningsagent:** LCA/LCC, MCDA, datakvalitet og synlig usikkerhet.
2. **Marked- og verktøyagent:** EC3, One Click LCA, ORIS, Reduzer, SmartKalk, Madaster, Concular, NOBB/Cobuilder og relevante nye moteksempler.
3. **SMB- og forskningsdesignagent:** tilbudsfase, praktiske brukerforutsetninger, pilotdesign og målbare effekter.
4. **Utfordrer/auditor:** leter etter overclaiming, kildekollisjoner, falske fraværspåstander og sterkeste motargument mot VERIFIEDs FoU-høyde.

Flere agenter gir bredde, ikke automatisk sannhet. Hvert funn må ha åpen URL og tydelig kildeidentitet.

## Forskningsspørsmål

1. Hva er dokumentert state of the art for å sammenligne flere løsningsalternativer i byggeprosjekters tilbuds-/tidligfase på tvers av klima, kostnad, levetid, vedlikehold, teknisk risiko og usikkerhet?
2. Hvilke eksisterende verktøy dekker flere av disse dimensjonene, og hvor er gapet bare et mulig kombinasjons- eller brukerforutsetningsgap?
3. Hvilke metoder finnes for å vise datakvalitet og usikkerhet uten å skjule dem i én totalskår?
4. Hva vet åpne kilder om små entreprenørers faktiske bruk av LCA, EPD og digitale beslutningsverktøy i tilbudsfasen?
5. Hvilke mål og studiedesign kan vise om VERIFIED påvirker tidsbruk, sporbarhet, valg, feil/omarbeid eller klima-/kostnadsutfall?
6. Hvilke påstander i dagens K1–K4/V1–V3 kan styrkes, må tones ned eller bør stå som FoU-hypoteser?

## Leveranse

Skriv hovedresultatet til:

`.scratch/sintef-forskningsrapport-2026/agy/agy-state-of-art-review.md`

Dokumentet skal inneholde:

- kort dom
- verifiserte funn med kilde og presis støtte
- kilder som motsier eller avgrenser dagens framstilling
- oppdatert funksjonsmatrise for verktøy
- tydelige forskningsgap
- anbefalinger til SINTEF-rapporten
- separat liste over mulige forbedringer i K1–K4/V1–V3
- åpen restliste: `NEEDS-ORIGINAL`, `CONFLICT`, `NOT-FOUND-IN-SCOPE`

Legg agentenes korte audit trail i samme mappe. Ikke kopier store dokumentblokker.

## Ikke-mål

- Ikke endre `v0.4`, `v0.5`, K/V-filer, evidenskort, kildebibliotek eller kildedom.
- Ikke oppgradere kildestatus.
- Ikke bruke egen kunnskap, agentkonsensus eller Sonar-sammendrag som belegg.
- Ikke framstille «ikke funnet i dette utvalget» som «finnes ikke».
- Ikke sende noe til SINTEF.
- Ikke lese `.env`, credentials eller private vaults.

## Akseptansekriterier

1. Hver faglig påstand har en åpen primærkilde eller er tydelig merket som hypotese/restpunkt.
2. Funksjonsmatrisen bruker samme kriterier for alle verktøy.
3. Sterkeste motargument mot VERIFIEDs nyhetsverdi er eksplisitt.
4. Rapportanbefalinger og søknadstekstforslag er separate.
5. Ingen kanoniske eller låste dokumenter er endret.

## Startprompt (lim inn i Antigravity i VS Code)

```text
Les docs/handoffs/37_agy_state-of-the-art_og_sintef-rapport_handoff.md.

Kjør en read-only fleragentgjennomgang av state of the art, verktøybildet, SMB-bruk og forskningsdesign for VIBS VERIFIED. Lever .scratch/sintef-forskningsrapport-2026/agy/agy-state-of-art-review.md med åpne kilder, moteksempler, forskningsgap og anbefalinger. Ikke endre søknadstekst, kildedom, kildebibliotek eller evidenskort, og ikke send noe eksternt.
```
