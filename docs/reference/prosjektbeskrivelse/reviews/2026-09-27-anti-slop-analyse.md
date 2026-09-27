---
title: Anti-slop-analyse av søknadsteksten
date: 2026-09-27
grunnlag: v2.0 slik den står etter F1–F16. Innovasjonen er målt i innskrevet versjon, ikke utkastet som venter på godkjenning.
metode: deterministisk telling (scratchpad/slop.py) + lesing mot skills/ai-sprakvask-no «KI-trekk å se etter»
---

# Anti-slop-analyse av søknadsteksten

## Tellingen

Tabellen gjelder bare felt utenfor arbeidspakkene. Kolonnene betyr:

- **ramse:** setninger med oppramsing av tre eller flere ledd
- **trapp:** setninger som begynner med «Da / Derfor / Deretter / Først / Så …»
- **strek:** tankestreker
- **kolon:** antall kolon
- **nom%:** andel lange ord på -ing, -het, -else og -asjon

| Felt | ord | ramse | trapp | strek | kolon | nom% | snitt ord/setn |
|---|---:|---:|---:|---:|---:|---:|---:|
| Kunnskapsbehov | 590 | **11** | 2 | 0 | 8 | 4,7 | 19 |
| FoU-metoder | 773 | 7 | **5** | 4 | **10** | 3,1 | 16 |
| Innovasjonen (innskrevet) | 623 | 7 | 3 | 5 | 1 | 3,9 | 17 |
| Verdiskapingspotensial | 505 | 6 | 0 | **6** | **12** | 4,4 | **24** |
| Styring og roller | 310 | **7** | 0 | 0 | 0 | 5,8 | 15 |
| Risiko | 272 | 0 | 0 | **9** | **36** | 3,7 | – |
| Etiske problemstillinger | 82 | 2 | 0 | 0 | 0 | **14,6** | 10 |
| FNs bærekraftsmål | 127 | 2 | 0 | 0 | 0 | 7,9 | **25** |
| Delmål | 105 | 2 | 0 | 0 | 6 | 6,7 | 18 |
| Realiseringsplan | 112 | 3 | 0 | 0 | 1 | 6,2 | 12 |
| Gjennomføringsplan | 234 | 3 | 0 | 0 | 2 | 6,4 | 21 |
| Sammendrag | 214 | 2 | 2 | 0 | 1 | 3,7 | 14 |
| Behov og markedsmuligheter | 238 | 0 | 0 | 0 | 1 | 1,7 | 12 |
| Samfunnseffekter | 203 | 0 | 0 | 0 | 0 | 3,9 | 15 |
| Kjønnsperspektiver | 56 | 0 | 0 | 0 | 0 | 5,4 | 14 |
| Kompetanse | 111 | 2 | 0 | 0 | 0 | 3,6 | 16 |
| Formidling | 81 | 0 | 0 | 0 | 5 | 6,2 | 12 |

## Det verste funnet: flate tabeller

Atten linjer er tabeller som er presset inn i tekst, med mønsteret
«tema — nøkkel: verdi; nøkkel: verdi; nøkkel: verdi». Ingen mennesker skriver
slik. Linjene står tre steder:

- **Måleplan i FoU-metoder** (`:85`–`:87`), tre linjer.
- **Seks ledd i Verdiskaping** (`:191`–`:196`), med «hva som må vises: …; ikke
  tilstrekkelig alene: …».
- **Risiko** (`:263`–`:271`), ni linjer med «s/k: Middels / høy; tidlig
  indikator: …; tiltak: …; eier: …». Alle ni risikoene har **middels**
  sannsynlighet. En evaluator ser da at risikoene ikke er prioritert.

## Prioritert rekkefølge

Rekkefølgen tar hensyn til hvor mye feltet teller for evaluator, hvor mye slop
det har, og om det er lov å røre feltet nå.

1. **Innovasjonen.** Utkastet på 3168 tegn er klart og venter bare på ja
   (spørsmål 19). Det fjerner fem tankestreker og punktlisten med «dagens –
   metoden».
2. **Kunnskapsbehov** (Kvalitet, «utfordrer state of the art»). Feltet har 11
   oppramsinger, flest i søknaden. Avsnittet om standarder og avsnittet om norske
   studier er tunge. F1–F5 kan stå som liste.
3. **FoU-metoder** (Kvalitet, «solide metodevalg»). Feltet har fem trapp-setninger,
   og måleplanen er en flat tabell. Teksten ligger på 4958/5000, så vasken må
   gjøre den kortere. Det er mulig, fordi den flate tabellen er ordrik.
4. **Verdiskapingspotensial** (Effekter, «økonomiske gevinster»). Seks ledd som
   flat tabell, 24 ord per setning og det mest konsulentaktige språket i
   søknaden. Setningen om 16,0 MNOK skal stå urørt.
5. **Risiko** (Gjennomføring, «relevante risikovurderinger»). Registerformatet
   bør bli korte, vanlige setninger, og sannsynligheten bør skille mellom
   risikoene. Å endre sannsynlighet er en faglig beslutning som Lars må ta, ikke
   bare språk.
6. **Etikk.** Nesten 15 % tunge substantiver. Feltet er kort og raskt å rette.
7. **FNs bærekraftsmål.** Første setning har 25 ord og lister tre delmål med
   fullt navn. Årsakskjeden er god.
8. **Delmål.** «Delmålene er å avgrense …, utvikle …, prøve … og dokumentere …»
   er en firledds oppramsing. D1–D5 kan stå.
9. **Styring og roller** (unntatt `:245`) og **Realiseringsplan.** Oppramsinger,
   men lav vekt.

Gjennomføringsplan, Kompetanse og AP-feltene venter. De er enten utenfor
denne runden eller blokkert.

## Allerede vasket

Hovedmål (runde 1), Sammendrag (runde 2), Samfunnseffekter (runde 2) og Behov
(runde 1, lite slop). Hovedmål har to oppramsinger, men begge er definerte
begrepssett (de tre nivåene og de tre svarene). Det er tillatt én gang per felt.
