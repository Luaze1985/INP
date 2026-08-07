# CONTEXT.md — ipn-verified

Tilstand og kjente risikoer. Oppdatert: **2026-08-07**.

## Siste endring: v0.9 inn, nettsiden rettet etter den (2026-08-07)

Søknadskandidat **v0.9** er rullet inn i repoet som markdown
(`docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.9.md`). Den er en klart mer
forsiktig tekst enn v0.1–v0.4: den navngir **ingen partnere og ingen personer**, bygger K1 på
SSB-statistikk i stedet for bransjetall, og sier eksplisitt at prosjektet ikke oppgir prosentsatser
før originalanalysen er kontrollert. Femten referanser, hvorav åtte er nye for repoet.

Den publiserte nettsiden sto med et faktagrunnlag v0.9 hadde forlatt — 32 %-tallet, fire bransjetall,
åtte navngitte partnere, fem personnavn og BKA2. Alt dette er nå ute. Se
`site/arbeid/faktasjekk-2026-08-07.md` for full sporing påstand for påstand.

- **v0.5–v0.8 finnes ikke i repoet.** De er skrevet utenfor. Hoppet er notert, ikke rekonstruert.
- **Fem åpne kommentarer** fra partnergjennomgangen er hentet ut av Word-fila til
  `prosjektbeskrivelse/v0.9-apne-kommentarer-2026-08-05.md`. Ingen er behandlet.
- **`site/mockup/` er døpt om til `site/web/`.** Det var aldri en mockup — det er den publiserte
  siden. `vercel.json` og `netlify.toml` peker dit nå.
- **Bilderettigheter er en åpen risiko.** Fem nye byggeplassbilder er tatt i bruk uten dokumentert
  bruksrett, etter Lars' beslutning. Se `site/arbeid/bilder-kilder.md`.

## Låst begrepsbruk for neste søknadspass

**Løsningsvalg:** Valget mellom flere mulige løsninger for samme byggeoppgave i tilbudsfasen. Det er bredere enn et produktvalg, fordi en løsning kan omfatte produkter, montering, vedlikehold og forventet levetid.  
_Unngå_: «produktvalg» når hele løsningen menes.

**VERIFIED:** Et FoU-prosjekt som skal utvikle og teste en felles måte å samle, vekte og forklare informasjon om alternative løsninger. Dette vises i et enkelt sammenligningsverktøy.  
_Unngå_: at VERIFIED «velger» eller «anbefaler automatisk».

**Sammenligning:** En åpen framstilling av fordeler, ulemper, usikkerhet og begrunnelse for hvert alternativ. Entreprenør og kunde bruker den sammen; entreprenøren har faglig ansvar for tilbudet.  
_Unngå_: «svart boks», «automatisk beslutning».

**Brukerforutsetning:** Informasjonen skal være mulig å bruke i tilbudsfasen uten å forutsette fagkunnskap og tid som mange små bedrifter ikke har.  
_Unngå_: «spesialister».

## Status nå

- **Søknadstekst:** tre kanoniske dokumenter er språkvasket (presens→futurum, sjargong fjernet) og kildedom er flettet inn.
- **Prosjektbeskrivelse K/V:** første røffe utkast er skrevet i `docs/reference/prosjektbeskrivelse/`
  for K1–K4 og V1–V3. Språkretning: enkelt snekker-språk, korte setninger, ingen effekt i
  presens, og tydelig skille mellom hva VERIFIED skal teste og hva som er dokumentert.
- **Kildeverifisering:** AGY samordnet fire spriktende rapporter til én kildedom (`vibs-verified-kildedom-2026-06-27.md`); Codex flettet den inn. An/Billio/Kaza splittet i tre, EBA-kollisjon skilt (EU-bank vs. NO-entreprenørforening), IPN-beløp rettet til 1–16 MNOK.
- **Grensetilfeller tatt ut (Lars 2026-06-28):** `[Wiik2025]` (SINTEF Notat 57 ikke funnet) og `[SA2018]`/2,2 mrd (rapport ikke lokalisert) er fjernet fra prosaen, parkert ⏸ i hovedokument/kildebibliotek. 20 %-påstanden hviler nå på `[EBA_NO2023]` + `[KD2024]`.

## Åpne punkter / risiko

- **Bilderettigheter (ny 2026-08-07):** de fem bildene på den offentlige siden har ukjent opphav.
  Rettighetshaver bør spores og skriftlig bruksrett innhentes, eller bildene erstattes med egne.
- **Kommentarene til v0.9 er ubehandlet.** Tre av fem gjelder avgrensning og struktur og bør avklares
  før teksten går inn i Forskningsrådets skjema.
- **v0.9s kilder er ikke primærverifisert.** Fire NTNU-masteroppgaver ligger åpent i NTNU Open og
  bør kunne løftes til 🟢 raskt. `[SSB2026]` er allerede 🟢.
- **🟡 venter på primær:** `[An2020]`, `[GullbrekkenHolme2025]`, `[KD2024]`, `[Mecca2023]` (Wiley-betalingsmur) m.fl. SINTEF åpner fulltekst **midten av august 2026** → 🟢. Ikke innsendingsklar før disse er 🟢 eller fraset med forbehold.
- **Parkerte kilder (⏸):** `[Wiik2025]`, `[SA2018]` venter på at kilden lokaliseres/dokumenteres.
- **Fortsatt ikke innsendingsklar:** K/V-utkastet mangler Lars-/Lars Gunnar-avklaringer om SMB-definisjon,
  baseline, målepunkter, metodevalg, bankavgrensning og konkrete DNSH-tiltak. WP1–WP5 og
  Gjennomføring er fortsatt parkert.
- **Ingen SQLite ennå.** Kildestatus, provenans og audit er markdown for hånd → drifter, krever manuell avstemming. Se AGENTS.md → «dokumentdatabasert».
- **Nylig utskilt fra `vibs-boligpass/`.** Originalfilene ligger fortsatt der, markert «IPN FLYTTES». Repoet er ikke git-initiert ennå (se `IPN-FLYTTES.md`).
- **Ingen nummerert handoff #30** dokumenterer at Codex-rettingen/språkjobben er utført, selv om begge er gjort.

## Pekere

- Kriterier og utlysningsfakta → `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md` §10
- Kanonisk kildeliste → `docs/reference/ipn-kildebibliotek.md`
- Kildedom (autoritativ) → `docs/reference/vibs-verified-kildedom-2026-06-27.md`
- Verifiserings-provenans (agent-kjøringer) → `provenance/agents/`
- Full filoversikt → `INDEX.yml`
