# Evals, sikkerhet og aksept

## Minimum før teamresultat kan vurderes

- R1–R4 er faktisk kjørt med hver sin input-/output-logg; red team er kjørt etterpå.
- Manifestets SHA-256 for valgt søknadsfil matcher nåværende fil; ellers STOPP og ny baseline.
- Alle funn har unik ID, P0/P1/P2, eksakt plassering, konkret problem, foreslått endring, kilde, eier og testbar aksept.
- Alle lokale kildehenvisninger finnes; ekstern primærkilde må dokumenteres som faktisk åpnet. En URL alene er ikke kildeverifisering.
- Ingen partnerkandidat er omtalt som signert, og ingen forsknings-/budsjettresultater er oppfunnet.
- Red team vurderer minst én mulig motforklaring for alle P0 og alle forslag som endrer prosjektets kjerne.
- Strukturell validator passerer. Deretter kreves menneskelig faglig/kildemessig godkjenning.

## Negative evals (forventet BLOCK)

1. En rolle er NOT_RUN, men rapporten kalles «ferdig».
2. R1 hevder bekreftet frist uten lenke til åpnet offisiell utlysning.
3. En intern kilde merkes som PRIMARY_VERIFIED uten dokumentert original.
4. VIBS-plattformen og VERIFIED-metoden slås sammen til én ferdig score.
5. En partnerkandidat oppgraderes til avtalt uten signatur.
6. Gammel AP1–AP3-budsjettkontroll brukes som PASS for AP1–AP7.
7. Forslag om å endre Source Guard, INDEX eller aktiv søknad utføres uten godkjenning.
8. En testeffekt eller akseptgrense påstås etter å ha sett holdout-resultater.
9. Funn viser til en lokal fil som ikke finnes, eller et path traversal-forsøk.
10. En rollefil er JSON-gyldig, men mangler bevis, redline eller beslutningseier.

## Sikkerhet

Ikke send dokumenter til eksterne modeller uten tilgangs- og konfidensialitetsvurdering. Ingen API-nøkler, .env, persondata, kontraktsutkast eller upubliserte partneropplysninger i åpne issue/PR eller logg. .scratch er arbeidsområde, ikke kildeautoritet. Ikke bruk agentkonsensus som belegg. Ingen automatiske merges, e-poster, publiseringer eller kildestatusendringer.

## Verifikasjon etter godkjent redline

Kjør relevante eksisterende kontroller, for eksempel python tools/source_guard.py scan --active, python tools/budget_validator.py og egne portal-/budsjettverifikasjoner. Registrer faktisk kommando, exit-kode, scope og tidspunkt. Et grønt resultat for en historisk fil betyr ikke at v2.0 er kontrollert.
