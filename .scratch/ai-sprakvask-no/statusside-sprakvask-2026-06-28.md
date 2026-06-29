# Språkvaskrapport - VERIFIED-statusside

Dato: 2026-06-28  
Kilde: `site/tekstmanus.md`  
Skill: `ai-sprakvask-no`

## Input-antakelser

- Målgruppe: Forskningsrådet, partnere og fagmiljø.
- Sjanger: nettsidetekst / statusside.
- Skriftspråk: bokmål.
- Ønsket stemme: jordnær, kort, faglig trygg, ikke glatt.
- Må ikke endres: fakta, kildestatus, tall, partnernavn, forsiktighetsnivå og åpne spørsmål.

## Diagnose

```yaml
summary:
  verdict: noe_ki_preg
  main_risks:
    - Enkelte setninger var litt interne eller byråkratiske.
    - Partneravsnittet var for langt og kompakt for nettside.
    - Noen fagord var riktige, men unødvendig tunge for offentlig side.
```

## Funn og tiltak

| Funn | Problem | Tiltak |
|---|---|---|
| `beslutningsgrunnlag` | Byråkratisk og brukt flere steder | Endret ett synlig sted til `valggrunnlag`; meta ble gjort mer konkret |
| `forskningsfaglig tyngde og primærverifisering` | Internt/faglig tungt | Endret til `faglig kontroll og kildeverifisering` |
| `primærverifisere` | Domeneterm, men tungt på nettside | Endret til `åpne og kontrollere originalkildene` |
| `komplement, ikke en kopi` | Konsulent-/søknadsspråk | Endret til `utfyller eksisterende forskning, ikke kopierer den` |
| Partneravsnitt | For tett og oppramsende | Delt i to avsnitt og forenklet inngangen |
| CPR/DPP-setning | Litt teknisk og hard påstand | Endret til `legger grunnlaget for digitale produktpass` |

## Norm- og kildeport

```yaml
norm_status: ok
source_status: ok_with_existing_caveats
final_gate: pass
```

Merknad: Språkvasken endret ikke tall, kilder eller påstandsnivå. Gule/åpne kilder står fortsatt forsiktig formulert.

## Stemmebevaring

Teksten er fortsatt i `vi`-stemme. Endringene gjør den litt mer direkte uten å gjøre den muntlig eller løsere enn søknads-/partnersammenhengen tåler.

