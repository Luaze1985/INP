# Kildekontroll, kollegatekster og lagret SINTEF-pakke

Denne mappen er den sentrale inngangen til konsolideringen etter
Perplexity-kontrollen. Innholdet beskriver funn, anbefalte uttak og spørsmål
som eventuelt kan kontrolleres av SINTEF senere.

Ingen filer i denne mappen er i seg selv faglig belegg. De endrer heller ikke
kildestatus eller aktiv søknadstekst.

De godkjente sperrene håndheves maskinelt gjennom
`governance/source-blocklist.json`. Bruk og kontrollkommandoer står i
`governance/README.md`.

## Finn riktig del

```text
docs/sintef/
├── README.md                         ← start her
├── ARBEIDSPAKKER.md                  ← ansvar, leveranser og kontrollporter
├── KONTROLLRAPPORT.md                ← kontrollresultat og rettede avvik
├── kollegapakke/                     ← lettleste tekster for kollegaer
├── internt/                          ← uttaks-, sperre- og endringskart
├── pakke-lagret-ikke-sendt/          ← mulig senere kontroll hos SINTEF
└── svar-fra-sintef/                  ← tom mottaksplass for faktiske svar
```

## Fast arbeidsregel

1. **Behold** betyr at innholdet kan arbeides videre med innenfor gjeldende
   kildeport.
2. **Ta ut** betyr at innholdet fjernes fra aktive flater etter Lars'
   godkjenning. Kildeidentitet og begrunnelse beholdes internt.
3. **Avklar** betyr at innholdet holdes ute av aktive flater til originalen er
   kontrollert. Bare Lars kan gjenåpne.

`Ikke funnet` betyr ikke at en kilde er bevist ikke-eksisterende. Praktisk kan
den tas ut og sperres mot automatisk gjenimport, men beslutningen skal beskrives
som `retired-not-found` eller `original-required`.

## Avgrensning

- Ingen materiale sendes automatisk eller uten Lars' uttrykkelige beslutning.
- Ingen aktive søknadsfiler eller nettsidefiler endres i denne dokumentfasen.
- Ingen kilde pensjoneres eller slettes bare fordi den står i et tørrkjøringskart.
- Historiske dokumenter beholdes som historikk, ikke som gjeldende sannhet.
