---
name: "grill-me-verified"
description: "Bruk når Lars (ofte sammen med Lars Gunnar) vil stress-teste siste versjon av VERIFIED-søknaden, partnerrollene, arbeidspakkene (AP1–AP3) eller partner-/oppfølgingsmailene før noe går videre — til NFR, til en partner, eller til en intern beslutning. Trigges av «grill meg på», «stress-test», «se over søknaden/partnerne/AP-ene/mailene før vi sender», eller når Lars nevner at noe skal ut av huset snart. Finner selv nyeste kandidat via INDEX.yml og CONTEXT.md, still de skarpeste spørsmålene à la grill-me-metodikken i docs/agents/skills.md, og leverer et felles arbeidsdokument som Lars og Lars Gunnar kan fylle ut sammen."
---

# Grill-me VERIFIED

## Når du skal bruke denne

Bruk denne skillen når noen av de fire flatene i IPN-søknaden VERIFIED skal
stress-testes før de går videre:

- **Søknad** — sammendrag, K1–K4, V1–V3, forankring mot NFR-kriteriene
- **Partnere** — rollekort, bekreftelsesporter, partneroversikt
- **Arbeidspakker** — AP1–AP3, akseptkriterier, beslutningsporter, budsjett
- **Mailer** — partneroppfølging og intern oppfølging

Trigger på alle fire samtidig hvis brukeren ikke spesifiserer, eller på én/to av
gangen hvis de sier «grill meg bare på partnerne» e.l.

## Hvorfor grille før man sender

Hele repoet lever av at «foreslått», «kandidat», «interesse uttrykt» og
«bekreftet/avtalt» aldri blandes (se `skills/kilde-agent/SKILL.md`). En runde
med skarpe spørsmål før noe sendes ut — til Forskningsrådet, til en
partnerkandidat, eller til Lars Gunnar og Bjørn internt — fanger opp glidninger
mens de fortsatt er billige å rette. Grill-me er ikke en kildekontroll og ikke
en omskriving; det er en spørsmålsrunde som tvinger fram en beslutning.

## Steg 1 — finn nyeste versjon selv

Ikke anta filnavn eller stol på hukommelse fra forrige gjennomgang. Les
`INDEX.yml` og «Siste endring»-avsnittet øverst i `CONTEXT.md` for å bekrefte
hvilke filer som faktisk er nyeste kandidat akkurat nå:

- **Søknad:** nyeste `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-*.md`, pluss nyeste verdiskapings-/lønnsomhetsnotat i `arbeidsversjoner/` hvis et slikt finnes.
- **Partnere:** nyeste `arbeidsversjoner/*partnerroller*` + `budsjett/partneroversikt.md`.
- **Arbeidspakker:** AP-tabellene, ansvar og akseptkriterier i søknaden — samme kildegrunnlag som partnere, men lest med AP-blikk (periode, leveranseeier, port, budsjett).
- **Mailer:** nyeste `reviews/*e-post*` eller `*oppfolging*`-dokument.

Sjekk endringsloggen i hver fil (dato + hvem) — den forteller om filen faktisk
er nyest, ikke bare sist åpnet. Hvis to filer ser ut som konkurrerende
«nyeste», si fra til Lars i stedet for å gjette.

## Steg 2 — grill med sju linser

Gå gjennom linsene under for hver flate brukeren ber om. Målet er konkrete,
skarpe funn — ikke et avsnitt med generisk usikkerhet. Grill-me-prinsippet i
`docs/agents/skills.md` er 1–2 spørsmål av gangen: hvis du jobber interaktivt
med Lars, ikke lever tjue spørsmål på én gang — still de viktigste, vent på
respons, bygg videre. Hvis du leverer et skriftlig dokument til senere
gjennomgang med Lars Gunnar (den vanlige bruken av denne skillen), samle
spørsmålene i dokumentet i stedet, men hold hvert spørsmål like presist som om
du skulle stilt det muntlig.

1. **Svakeste påstander** — hvilke setninger bærer mer enn kildegrunnlaget, budsjettstatusen eller dagens partnerstatus faktisk holder?
2. **Skjulte antakelser** — hva må være sant for at avsnittet skal holde, men står ikke skrevet noe sted?
3. **Manglende perspektiv** — hvilken part (Forskningsrådet, en navngitt partnerkandidat, sluttbruker/entreprenør, LG selv) mangler stemme i dette utkastet?
4. **Falsk konsensus** — hvor later teksten som noe er avklart eller enighet, når det egentlig bare er ett møteinnspill, én kandidatvurdering eller ett Codex-utkast?
5. **Overavhengighet** — hvilken enkeltkilde, ett partnerutsagn, én beregning eller ett scenario bærer mer vekt enn det tåler alene?
6. **Årsaksoverdrivelse** — hvor blir en sammenheng, et scenario eller uttrykt interesse lest som et bevist resultat eller en bindende deltakelse?
7. **Portstatus** — stemmer «foreløpig / kandidat / interesse uttrykt / bekreftet»-merkingen faktisk overalt i teksten, eller har noe glidd mot å høres mer avtalt ut enn det er?

`references/grill-sporsmal.md` har et større, flate-spesifikt spørsmålsbibliotek
(søknad, partnere, AP, mailer) hvis du vil gå dypere enn de sju linsene, eller
trenger konkrete startspørsmål for en ny runde.

## Steg 3 — lever som felles arbeidsdokument for Lars og Lars Gunnar

Skriv resultatet til en egen fil:
`docs/reference/prosjektbeskrivelse/reviews/<dato>-grill-me-<flate(r)>.md`,
i samme stil som de andre review-filene i mappen (frontmatter: title, date,
status, base, input).

Strukturer selve gjennomgangen spørsmål for spørsmål, ikke som én lang liste,
og la svar-feltene stå tomme — dette er et dokument de to fyller ut sammen, du
skal ikke gjette deg til svaret:

```markdown
## Spørsmål N — <kort tittel>
**Hvorfor dette spørsmålet:** ...
**Hva teksten/planen sier i dag:** ...
**Svar / beslutning:**
- Lars Erik:
- Lars Gunnar:
```

Avslutt dokumentet med en kort, prioritert liste over hvilke punkter som haster
mest før neste steg (innsending, partnerutsending, styremøte) — maks fem
punkter, ikke en ny huskeliste over alt som er åpent i CONTEXT.md.

## Kvalitetsregler

- Ikke overta kilde-/sannhetskontrollen — det er `kilde-agent`-skillens jobb. Grill-me flagger *retorikk og resonnement*, ikke referansestatus (🟢🟡🔴⏸).
- Ikke fyll ut svar-feltene selv, og ikke lag et nytt søknadsutkast — dette er en spørsmålsrunde, ikke en omskriving av søknaden.
- Ikke bruk møtereferater eller partnerinnspill som fasit for hva som er bekreftet. De aktuelle dokumentene og CONTEXT.md er alltid strengere sannhetskilde enn et referat.
- Hold nøktern norsk tone, samme som resten av repoet — ingen konsulentspråk, ingen overdrevet alarm. Et grill-spørsmål skal skjerpe en beslutning, ikke skremme.

## Etter gjennomgangen

Legg en linje under `prosjektbeskrivelse` → `reviews` i `INDEX.yml`, og skriv
én kort linje i `CONTEXT.md` om at grill-me-runden er gjort og hvor filen
ligger. Et gjennomgangsdokument ingen finner igjen, er bortkastet arbeid.
