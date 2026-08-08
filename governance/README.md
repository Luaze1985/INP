# Source Guard — permanent sperre mot gjenimport

`source-blocklist.json` er den maskinlesbare håndhevingen av den interne
uttaks- og sperreloggen. Den gjør at en sperret kilde ikke blir «ny» bare fordi
en agent bruker en gammel nøkkel, en tittelvariant, DOI eller URL.

## Hva som håndheves

- 11 godkjente sperreposter med stabil `SP-*`-ID;
- kanonisk nøkkel, gamle aliaser, normalisert tittel, DOI og URL;
- feilrelasjoner, blant annet Bjørheim som samlekilde for BDO, UNION og ombruk;
- gjenåpningsregel og Lars som eneste beslutningseier.

Registeret er ikke en referanseliste og gjør ingen kilde faglig gyldig. Det er
en negativ kontroll: et treff skal i karantene og kan ikke føres inn i aktiv
tekst uten ny Lars-beslutning.

## Kommandoer

Kjør fra repoets rot:

```powershell
# Kontroller at registeret er gyldig
python tools/source_guard.py validate-registry

# Kontroller en ny Perplexity-, agent- eller kildefil før innfletting
python tools/source_guard.py scan --path "C:\sti\til\inntak.txt"

# Lag maskinlesbar rapport for et inntak
python tools/source_guard.py scan `
  --path "C:\sti\til\inntak.txt" `
  --report ".scratch\source-guard\rapport.json"

# Kontroller alle seks aktive søknads- og nettsideflater
python tools/source_guard.py scan --active

# Sammenlign staged versjon med HEAD for de seks aktive filene
python tools/source_guard.py scan --staged

# Kjør testene
python -m unittest tests.test_source_guard -v
```

Returkoder:

- `0`: `PASS` — ingen sperret identitet eller relasjon funnet;
- `1`: `BLOCK` — treff skal i karantene;
- `2`: konfigurasjons- eller leseproblem; prosessen skal stoppe.

## Git-port

Repoet har en sporet hook-mal i `.githooks/pre-commit`. Ved lokal aktivering
kopieres den til `.git/source-guard-hooks/`, utenfor den vanlige arbeidsflaten.
Hooken kjører den committede (`HEAD`) validatoren og sperrelisten, ikke en
eventuelt svekket arbeidskopi. Den kjører `scan --staged` for de seks aktive
filene. Hele staged filversjonen
sammenlignes med `HEAD`, slik at en ny BDO-påstand også stoppes når
`Bjørheim2026` allerede står i samme avsnitt. Historiske filer og mockuper er
ikke omfattet av commit-porten. Lokal aktivering:

```powershell
New-Item -ItemType Directory -Force .git/source-guard-hooks
Copy-Item .githooks/pre-commit .git/source-guard-hooks/pre-commit -Force
git config core.hooksPath .git/source-guard-hooks
```

Etter første commit blir endringer i blokkregister, validator og hook stoppet
uten en innebygd programmatisk overstyring. En eventuell policyendring må være
en egen, uttrykkelig Lars-beslutning og gjennomføres som en separat
vedlikeholdsoperasjon med manuell diffkontroll.

Denne porten er en lokal prosesskontroll, ikke identitetsautentisering på
operativsystemnivå. En aktør med full shell-tilgang kan teknisk omgå en lokal
Git-hook. Derfor er `AGENTS.md`, diffkontroll og Lars' eksklusive beslutningsrett
fortsatt nødvendige.

## Dagens overgangstilstand

Full kontroll av de seks aktive flatene gir foreløpig `BLOCK`, fordi eldre
reviewfiler og nettsidens interne kanban fortsatt inneholder kjente treff.
Dette er synlig teknisk gjeld fra før håndhevingen.

Pre-commit-porten tillater uendrede, kjente treff fra `HEAD`, men stopper nye
eller endrede treff. Når Lars senere godkjenner og gjennomfører
endringskartene, skal full `scan --active` ende i `PASS`. Først da er både
gammel gjeld og ny gjenimport lukket.

## Endring av sperrelisten

En agent kan foreslå en endring, men kan ikke:

- fjerne en `SP-*`-post;
- endre `decision_maker`;
- gjøre `original-required` eller `manual-only` svakere;
- legge en sperret identitet i et unntak for å få grønn test.

Bare Lars kan godkjenne dette. Historiske dokumenter og kontrollnotater kan
omtale sperrede kilder fordi identiteten må bevares; de er ikke aktive
siteringsflater.

## Karantene

Eksplisitt `scan --path` skanner også filer under `.scratch`. Ved `BLOCK`
beholdes originalen urørt, mens en kontrollkopi og `manifest.json` opprettes i
`.scratch/source-guard/quarantine/`. Manifestet inneholder originalsti,
størrelse, SHA-256 og alle treff. Råmaterialet kan arkiveres, men det skal ikke
føres videre til aktive flater.
