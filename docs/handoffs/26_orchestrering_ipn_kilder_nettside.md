---
title: Orkestrering - IPN juli-aug, kildesjekk + nettside
date: 2026-06-26
status: aktiv
from: claude
to: lars / codex / antigravity
branch: antigravity/snekker-pilot
tags: [vibs, verified, ipn, orchestrering, kilder, nettside, oversikt]
---

# Orkestrering: IPN-arbeidet juli-august

## Hva dette er

Oversiktsdokumentet for VERIFIED IPN-arbeidet. Det forklarer hvem som gjoer hva, hva status er, og peker til de to oppgavene som er viktigst naa: **kildesjekk** (handoff 27) og **nettside** (handoff 28). Selve arbeidsplanen ligger i `docs/reference/ipn-arbeidsplan-juli-aug-2026.md`.

## AERLIGHETSREGEL (gjelder all orkestrering)

Claude kan **kun** styre Claude-subagenter via Agent-verktoeyet. Claude kan **ikke** styre Codex eller Antigravity direkte. Maaten oppgaver flyttes til disse paa er **handoff-filer** (denne typen MD-fil) som Lars Erik selv aapner eller limer inn i VS Code. Ingen rollespill som "Codex-agent" eller "Antigravity-agent" - det er bare handoff-instrukser til manuell sending.

## Rollefordeling

| Verktoey / agent | Rolle | Kan Claude styre? |
| --- | --- | --- |
| **VS Code** | Arbeidsbenken. Alt repo-arbeid skjer her. | - |
| **Codex** | Utfoerende agent: kode, repo, dokumenter. | Nei - via handoff |
| **Antigravity** | Utfoerende agent: nettside og UI. | Nei - via handoff |
| **Claude** | Handoff-filer, omformulering, Sonar-faktasjekk. | Ja (seg selv + subagenter) |
| **Sonar** | Faktasjekk-verktoey (loopback REST :8765). Ikke en agent. | Ja (kaller API) |
| **SINTEF** | Primaerverifisering av betalingsmur-kilder. Inn midten av august. | Nei (ekstern) |
| **Lars Erik** | Beslutninger, definisjoner, aapner offentlige kilder. | Nei (mennesket) |

## Slik orkestrerer Claude (via VS Code)

Claude er orkestratoren og jobber inne i VS Code. Det betyr:

- Claude gjoer **selv** alt repo-, fil- og Sonar-arbeid (skriver dokumenter, redigerer, faktasjekker).
- For arbeid som hoerer til **Codex** (kode/repo) eller **Antigravity** (nettside/UI), lager Claude en **handoff-fil** med en ferdig "Startprompt".
- Lars Erik aapner eller limer startprompten inn til riktig agent i VS Code. Agenten gjoer jobben i repoet og rapporterer tilbake.
- Claude leser resultatet, faktasjekker ved behov, og forbereder neste steg.

Kort: **Claude styrer flyten via VS Code og handoff-filer - ikke ved aa fjernstyre de andre agentene.**

## Arbeidsdeling: Codex vs Claude

Prosjektregel (CLAUDE.md): **Claude = dyp implementering, multi-fil, kjoerer kommandoer. Codex = uavhengig review, sikkerhet, fange hallusinasjoner.** Codex skriver ikke produksjonsteksten - Codex er den uavhengige kontrollen som fanger det Claude er blind for. Det er avgjoerende her, der oppdiktede kilder er den stoerste risikoen.

### Claude (implementerer)

- Kildesjekk: kjoere Sonar-domkortene, hente siteringer (handoff 27)
- Oppdatere `ipn-kildebibliotek.md` + `ipn-samledokument.md` fortloepende
- Scaffolding: opprette kapittelfilene K1-K4, V1-V3
- Skrive kapittel-utkast (prosa) + omformuleringer
- Kjoere `npm run build` / tester ved behov

### Codex (uavhengig review)

- **Kildesjekk-review:** stikkproeve siteringene Claude/Sonar fant - finnes kilden, sier den virkelig det? (fange hallusinerte siteringer)
- **Provenans-revisjon:** er hver 🟢 faktisk en aapnet primaerkilde? Er noen 🟡 sneket inn som baerende?
- **Konsistens:** matcher hver (Forfatter Aar) i prosaen en post i kildebiblioteket med samme port? Er EBA-navnekollisjonen (EBA EU <> EBA NO) intakt?
- **Overclaim-jakt:** paastander sterkere enn kilden taaler (f.eks. Wiik-tallet som garanti i stedet for mulighetsrom)
- **Sikkerhetsreview:** Sonar-API-koden (API-noekler, loopback-binding), netlify-funksjoner

### Flyt mellom dem

Claude implementerer -> Codex reviewer (uavhengig) -> funn tilbake til Claude for retting -> Lars godkjenner. Antigravity staar utenfor denne splitten (bygger nettsiden, handoff 28).

## Status naa (2026-06-26)

- **Arbeidsplan v0.3** ferdig: `docs/reference/ipn-arbeidsplan-juli-aug-2026.md` (omskrevet til enkel norsk, orkestreringsmodell rettet).
- **Samledokument v0.2**: `docs/reference/ipn-samledokument.md` - alle gronne F-rettelser gjort (F2, F3, F7, F9, F11a, F11e, F11f, F12b, F16). Ett aapent spoersmaal staar inline i do-not-harm (F16: bekreft "S mangler" = sosiale minstekrav?).
- **F4 faktasjekk gjort** (Sonar): "stoerste fastlandsnaering" bekreftet (NHO Byggenaeringen, Sammen 2030); "blant de minst digitaliserte" er faglig konsensus, beholdes som "en av de minst" (ikke "den minst"); "mest fragmentert" bekreftet (SSB: >99 % SMB). Detaljer i 27.
- **Scope-regel staar**: kun Kvalitet + Virkninger bearbeides. Gjennomfoering (WP1-WP5) er PARKERT.

## De to prioriteringene naa

1. **Kildesjekk** -> [27_kildesjekk_handoff.md](27_kildesjekk_handoff.md). Flytt noekkelkilder fra gul (ikke verifisert) mot groenn der det er mulig uten SINTEF. Sonar + Lars aapner offentlige PDF-er.
2. **Nettside** -> [28_antigravity_verified_nettside_handoff.md](28_antigravity_verified_nettside_handoff.md). Enkel VERIFIED-forskningsside. Antigravity bygger. GUARDRAIL: forskningsprosjektet, ikke produktet.

## Sentrale filer

| Fil | Innhold |
| --- | --- |
| `docs/reference/ipn-arbeidsplan-juli-aug-2026.md` | Hovedplan (v0.3) |
| `docs/reference/ipn-samledokument.md` | Populaerversjon (v0.2), kilde for nettsidetekst |
| `docs/reference/ipn-kildebibliotek.md` | Kanonisk kildeliste (Vedlegg C), noekler + provenans |
| `docs/reference/ipn-kildestrategi-2026-06-22.md` | To-lags arkitektur + provenans-port |
| `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md` | AErlig status per paastand |
| `docs/reference/state-of-the-art-verified-ipn.md` | Kunnskapsstatus (SoA) |
| `docs/reference/ipn-tilbakemeldinger-aksjonsliste-2026-06-22.md` | F1-F16 tilbakemeldinger + eierskap |

## Neste steg

1. Lars Erik aapner handoff 27 og 28, gir startpromptene til riktig agent (eller ber Claude kjoere kildesjekken direkte).
2. Etter kildesjekk: oppdater `ipn-kildebibliotek.md` (port-farger) -> slaa gjennom i samledokument og kapitler.
3. Naar prosjektbeskrivelse-kapitlene skal bygges: egen handoff (scaffolding K1-K4, V1-V3) - se arbeidsplan trinn 1/5.

## Foreslaatte skills for neste oekt

- `sonar-search` - faktasjekk av aapne kilder
- `grill-with-docs` - naar en kapitteltekst skal stresstestes mot kildene
- `handoff` - naar arbeidet igjen skal overleveres
