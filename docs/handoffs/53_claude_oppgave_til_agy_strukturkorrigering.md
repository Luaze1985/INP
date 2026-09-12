---
title: Oppgave (Claude → AGY) - Korriger fase-2-forveksling og WP/AP-mapping i strukturvurderingen
handoff_nr: 53
date: 2026-09-12
status: apen
from: claude
to: antigravity
branch: codex/partneroppgaver-v1-7
repo: C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified
svar_paa: AGYs vurdering av VERIFIED_VS_CODE_GRUNNLAG.zip mot v1.7 (limt inn av Lars i chat 2026-09-12, ikke en egen fil i repoet)
tags: [vibs, verified, ipn, struktur, arbeidspakker, ap1-ap3, faktasjekk]
---

# Handoff #53 (Claude → AGY): Korriger fase-2-forveksling og WP/AP-mapping

## Kort dom

Jeg har faktasjekket vurderingen din direkte mot repoet: **alle
faktapåstander stemte** (AP1–AP3-beløp, F1–F5, bankavgrensning, budsjett
16,0/8,0/8,0 MNOK, VIBS-ramme 12,6 MNOK, partnerlisten) — ingen hallusinasjon.
To ting bør likevel korrigeres i din modell før neste runde. Full begrunnelse
og kildesitater står i de to filene under — ikke gjenta dem her, referer til
dem:

- `docs/reference/prosjektbeskrivelse/reviews/2026-09-12-skisse-beslutningsgrunnlag-struktur.md`
- `docs/reference/prosjektbeskrivelse/reviews/2026-09-12-forbedringsplan-struktur.md`

## 1. Feltuttesting er ikke fraværende — den er i fase 2

Du skrev at prosjektet holder R6/pilot-måling "utenfor IF-only-kjernebudsjettet",
som er riktig retning, men ikke presist nok: v1.7 sier eksplisitt at praktisk
beslutnings-/kommersiell effekt **ikke er et akseptkriterium for modellfrys**,
og at slik effekt først måles "etter modellfrys i separat pilot"
(måleplan-tabellen, raden "Økonomisk verdi hos bruker"). Dette er en egen,
ikke-finansiert **fase 2** — ikke en del av AP1–AP3 i det hele tatt, og ikke
noe som skal inn i outtake-lista for denne søknaden. Din F6/R6 hører til fase
2, ikke til F1–F5.

## 2. WP1–WP3 (referansepakken) matcher ikke AP1–AP3 (v1.7) 1-til-1

Du behandlet WP1–WP3 som strukturelt parallelle til AP1–AP3 og foreslo å
"tilpasse" dem inn. Ved nærlesing er de delt opp langs forskjellige akser:

- WP2 ("Data og dokumentasjonstillit") er reelt sett **AP1-innhold**
  (kildesporing, datakvalitetsklasser) — ikke AP2.
- WP3 ("Beslutningsmodell og usikkerhet") **spenner over AP2 og AP3**
  samtidig (metodevalg/vekting → AP2; sensitivitetsanalyse/forklaringsformat
  → AP3).

Se den fulle sammenligningstabellen i skissen §2.2 før du foreslår videre
tilpasning — en 1-til-1-mapping vil gi feil resultat.

## 3. Konkret oppgave til deg

To punkter i forbedringsplanen (§2b, punkt 2.5–2.6) krever trolig ekstern
bekreftelse fremfor tekstarbeid:

1. **Tilbudskategori for AP1–AP2:** har du (via korrespondanse, tilbud eller
   annet grunnlag du har tilgang til) informasjon om hvilken konkret
   produktkategori (kledning, tak, e.l.) Espeland eller Norgesbygg Sør faktisk
   kan levere reelle tilbudsalternativer på? Vi trenger 2–4 alternativer
   låst i AP1.
2. **SMB-finansiering i AP1:** kan du bekrefte (samme type oppslag som
   Brønnøysund-sjekken i handoff #52, men her trolig mot korrespondanse/tilbud
   fremfor register) om Espeland eller Norgesbygg Sør har signalisert vilje
   til å levere tilbudscase uten egen AP1-finansiering, eller om dette
   fortsatt er uavklart?

Ikke gjett på disse to — meld tilbake "uavklart" hvis du ikke har grunnlag,
ikke fyll inn plausible svar.

## Ikke gjort av meg i denne runden

Ingen av de to strukturdokumentene fra zip-pakken
(`soknadsstruktur-og-krav.md`, `gjennomforing-struktur-utkast.md`) er lagt inn
eller redigert i git-repoet — de forblir kun i
`VERIFIED_VS_CODE_GRUNNLAG.zip`. Ingen endring i selve søknadsteksten
(`soknadstekst-samlet-kandidat-v1.7-if-only.md`) eller budsjettfilene.
