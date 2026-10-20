# Prioriterte, konkrete funn (foreløpig inspeksjon)

Grunnlag: GitHub main 9c0ad9b (inspisert 2026-10-20). Funnene er forslag til beslutning, IKKE utførte redlines. P0/P1/P2 følger FUNNFORMAT.md. Stier viser hvor problemet er dokumentert; kontroller på nytt før endring.

| ID | Prioritet | Hvor | Observasjon og konsekvens | Presis foreslått endring / aksept | Eier |
|---|---|---|---|---|---|
| KB-01 | P0 | Utlysning, ekstern | Koblingsboks-regler og 100 000 kr er ikke uavhengig kontrollert i denne pakken | Åpne datert offisiell utlysning; fyll kravmatrise; stopp søknad før kontroll | Søker |
| IPN-01 | P0 | INDEX.yml, CONTEXT.md | INDEX sier v1.9 NYESTE, CONTEXT beskriver finpuss v2.0 | Beslutt eksplisitt aktiv kandidat og registrer beslutning; oppdater INDEX først etter godkjenning | Beslutningseier |
| IPN-02 | P1 | README.md | Peker på v0.9 som gjeldende | Erstatt hardkodet versjon med lenke til INDEX etter versjonsvedtak | Repoansvarlig |
| IPN-03 | P0 | tools/source_guard.py | REQUIRED_ACTIVE_PATHS omfatter eldre v0.5, ikke v2.0 | Kartlegg gjeldende scan-scope; lag forslag til ny aktivfil uten å endre policy før særskilt godkjenning | Kildeansvarlig |
| IPN-04 | P0 | tools/budget_validator.py, budsjett/kalkulator.py | Validator krever AP1–AP3 mens nyere søknad bruker AP1–AP7 | Opprett separat v2.0 budsjettgrunnlag fra bekreftede timer, test summer og unngå gjenbruk av gammel PASS | Økonomiansvarlig |
| IPN-05 | P0 | budsjett/partneroversikt.md | Dokumentet beskriver AP1–AP3 og er datert 04.09; v2.0 har AP1–AP7 | Ny status-/AP-matrise med eksplisitt merking kandidat/avtalt, uten å overskrive historikken | Partneransvarlig |
| IPN-06 | P0 | v2.0 sammendrag | D Takst, Espeland, Norsk Byggtjeneste er partnerkandidater, ikke avtalte | Innhent og journalfør skriftlig rolle, kostnader, egenfinansiering og signatur; ikke oppgrader status før dokumentasjon | Prosjektansvarlig |
| IPN-07 | P0 | v2.0 sammendrag, CONTEXT.md | SINTEF er planlagt FoU-leverandør; tilbud/leveranseomfang er ikke bekreftet | Få skriftlig tilbud med metode, leveranser, rettigheter, time-/kostnadsramme; alternativ vurderes separat | Prosjektansvarlig |
| IPN-08 | P0 | CONTEXT.md, v2.0 AP1–AP7 | 16/8/8 MNOK er ramme, men dokumentert AP-/aktørtimegrunnlag mangler | Kalkyle per aktør og AP med timepris, timer, kostnadstype, støtteregel og signert finansieringsplan | Økonomiansvarlig |
| IPN-09 | P1 | reviews/2026-09-27-finpuss-v2.0.md | Akseptgrenser og metodevalg omtalt som åpne punkter | Lås måleplan, falsk-sikkerhet-metrikk, baseline og terskler før holdout; dokumenter beslutning | FoU-ansvarlig |
| IPN-10 | P1 | v2.0, 6–8 case / 3 holdout | Lite holdout kan gi skjør konklusjon; fare for lekkasje fra utviklingscaser | Angi enhet for case, uttrekksregler, blinding, perturbasjoner og gyldighetsområde; unngå generaliseringspåstand | FoU-leverandør |
| IPN-11 | P1 | reviews/2026-09-27-anti-slop-analyse.md | Risiko har ni like «middels» sannsynligheter og tett nøkkel-verdi-prosa | Prioriter 3–5 kritiske risikoer i lesbar tekst med ulike begrunnede nivåer, tidlig indikator og eier | Søknadsredaktør |
| IPN-12 | P1 | AGENTS.md, reviews/hva-er-verified | AGENTS omtaler «score-modell», men v2.0 beskriver datatillit og tre sammenlignbarhetsutfall | Foreslå styringspresisering etter beslutning; fjern ikke historiske spor; ingen score-/automatikkpåstand i ny tekst | Beslutningseier |
| KB-02 | P0 | Koblingsboks-utkast | Fare for at 16 MNOK IPN-aktivitet eller produktutvikling gjenbrukes som 100k forskningskjøp | Avgrens ett metodeforsøk, én FoU-leverandør, egen kostnads-/aktivitetslogg; ingen dobbeltfinansiering | Søker/økonomi |
| IPN-13 | P1 | skills/grill-me-verified/SKILL.md | Skill er spørsmålssamling, ikke evidensbaserte redlines; beskriver AP1–AP3 | Legg dette teamet ved siden av eksisterende grill-me; ikke overskriv skillen; redline + QA + beslutningslogg | Agentansvarlig |
| IPN-14 | P1 | innsendingspakker/README.md | v2.0 pakke, men tekstgrunnlag v1.9; portaluttrekk ikke fullt manuelt verifisert | Kontroll av feltkart, tegnrammer og manuelle valg mot live portal etter versjonsvedtak | Innsendingsansvarlig |
| IPN-15 | P2 | v2.0 og kildegrunnlag | Standardreferanser og kildeklassifisering må vurderes per konkret utsagn | Påstand–kilde-matrise, åpne primærkilder, noter uverifiserte standarder; ingen automatiske grønne statuser | Kildeansvarlig |

## Første beslutningsrunde

1. Bekreft hvilken IPN-kandidat som skal være aktiv (v1.9 eller v2.0).
2. Bekreft offisiell Koblingsboks-utlysning og om et separat, lite metodeoppdrag er støtteberettiget.
3. Be økonomi og partneransvarlige skille historiske AP1–AP3 fra nytt AP1–AP7-budsjett.
4. Godkjenn bare foreslåtte redlines én etter én, på egen PR.
