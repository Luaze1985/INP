# VIBS / VERIFIED – søknadsteam (arbeidspakke 2026-10-20)

Status: FORSLAG / IKKE GODKJENT. Dette er en installert, selvstendig arbeidsmetode – ingen agent er startet automatisk, og ingen søknadstekst er endret.

## Hva pakken gir

- Fire spesialistroller og en uavhengig red-team-kontroll, med menneskelig beslutningsport.
- Strukturert funnformat: eksakt fil/avsnitt, problem, kildegrunnlag, foreslått redline, test og eier.
- Python-verktøy for å inspisere repoet, opprette kjøringsmapper, validere agentresultater og samle rapport. Bare Python-standardbiblioteket.
- En separat, foreløpig Koblingsboks-søknad; den er IKKE verifisert mot gjeldende utlysning.
- Prioritert funnliste og egen IPN-forbedringsliste, metodeforslag, forskningsinntak og evals.

Dette bygger videre på AGENTS.md, CONTEXT.md, INDEX.yml, docs/agents/orchestration.md, docs/agents/intake-outtake.md og skills/grill-me-verified/SKILL.md. Det erstatter ikke disse.

## Viktig prosjektgrense

INP er søknadsrepoet. Produktimplementasjonen ligger i et separat VIBS-repo. VIBS er dokumentasjons-/plattformsporet; VERIFIED v2.0 er forskningsmetoden for datatillit og etterprøvbar sammenlignbarhet. VERIFIED v2.0 er IKKE en boligverdi-score og gir IKKE automatisk produktanbefaling. Historiske dokumenter med andre mål skal ikke blandes inn i dagens FoU-påstand.

## Oppstart (fra INP-reporoten)

    python tools/soknadsteam.py inspect --repo .
    python tools/soknadsteam.py init --repo . --application-file docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v2.0.md --run-id ipn-review-001
    python tools/soknadsteam.py validate --repo . --run-id ipn-review-001
    python tools/soknadsteam.py report --repo . --run-id ipn-review-001 --write

Init oppretter bare .scratch/soknadsteam/<run-id>/ med briefinger, tomme rolleutdata og manifest. Deretter må virkelige, separat utførte agenter/personer fylle funnfilene. En tom eller NOT_RUN rolle er aldri «fullført». Verktøyet sender ikke API-kall til en LLM og kjører ikke flere agenter av seg selv.

## Styring

1. Menneske velger eksplisitt søknadsfil og ordning. Automatisk «nyeste versjon» er forbudt ved motstrid.
2. Spesialistene leser samme frosne baseline, men arbeider uavhengig og skriver bare i egen .scratch-rollemappe.
3. Red team får de ferdige funnene og skal teste dem, ikke redigere dem.
4. Rapporten kan foreslå tekst, men ingen agent endrer aktiv søknad, INDEX.yml, Source Guard, kildedom eller budsjettfasit.
5. Beslutningseier godkjenner hver redline, kildestatus og eventuell innsending separat. Endringer gjøres deretter på egen branch/PR og med eksisterende verifikasjonsverktøy.

Les ROLLER.md, FUNNFORMAT.md, PRIORITERT_BACKLOG.md, KOBLINGSBOKS_UTKAST.md og EVALS.md.

## Reell versjonskonflikt observert ved inspeksjon

Per main-commit 9c0ad9b9cd541436f9ad48984e4e201b0b6752f7 peker INDEX.yml på v1.9 som NYESTE; README.md navngir v0.9; CONTEXT.md beskriver finpuss av v2.0; innsendingspakker/README.md bruker v2.0-struktur, men peker på v1.9-tekstgrunnlag. Dette er en beslutningssak, ikke en tillatelse til automatisk ompeking.

## Status for research

Innholdet er basert på verifisert inspeksjon av repoet og tidligere samtale-/researchbrief. En utvidet Deep Research-rapport var bestilt, men dens endelige funn er ikke importert i denne pakken. Ikke behandle denne pakken som bekreftelse på tilskuddsregler, partneravtaler eller forskningsresultater. Se RESEARCH_INNTAK.md.
