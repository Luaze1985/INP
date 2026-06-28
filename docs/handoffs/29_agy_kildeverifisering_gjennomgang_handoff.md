---
title: Handoff (AGY) - Gjennomgang og samordning av kildeverifisering
date: 2026-06-27
status: ready
from: claude
to: antigravity (AGY)
branch: antigravity/snekker-pilot
tags: [vibs, verified, ipn, kilder, verifisering, agy, sjekk]
---

# Handoff (AGY): Gå gjennom og samordne kildeverifiseringen

## Kort beskjed

Flere agentkjoeringer (2026-06-26) har produsert **fire delvis overlappende verifiseringsrapporter** med noen motstridende konklusjoner. Din jobb er aa **gaa gjennom dem, samordne til EN autoritativ dom per kilde/paastand**, og levere en ren liste som Codex kan rette dokumentene etter. **Du sjekker - du retter ikke dokumentene** (det gjoer Codex i neste handoff).

## Rollefordeling (aerlighetsregel)

- **AGY (deg):** gaa gjennom rapportene, verifiser paa nytt der det er tvil, lever EN samordnet domsliste. Pri **norske og europeiske kilder**.
- **Codex (neste steg):** retter de tre kanoniske dokumentene etter din domsliste.
- **Claude:** skrev denne handoffen. Styrer ikke deg direkte.
- **Lars Erik:** avgjoer grensetilfellene du flagger (se F8-regelen nederst).

## Hovedregel for domsavsigelse

1. **Bekreftet** = aapen, uavhengig kilde (helst norsk/europeisk) bekrefter paastanden -> 🟢.
2. **Ikke bekreftet** = ingen aapen kilde funnet, eller bare bestillingsverk/konsortie-intern -> 🔴. **Disse skal flagges for fjerning** (Lars' regel: ubekreftet skal helt vekk fra soeknadsteksten - ikke beholdes som 🟡).
3. **Feil** = kilden finnes men er feilattribuert (feil DOI/journal/scope) -> maa rettes, ikke fjernes.
4. Claudes egen kunnskap teller aldri som belegg. Uten sitering = ikke bekreftet.

## Inndata du skal gaa gjennom

**Fire verifiseringsrapporter (2026-06-26):**
- `docs/reference/vibs-verified-agentsøk-2026-06-26.md`
- `docs/reference/vibs-verified-agentverifisering-2026-06-26.md`
- `docs/reference/vibs-verified-full-kildesjekk-2026-06-26.md`
- `docs/reference/vibs-verified-sonar-2026-06-26.md`

**Tre kanoniske maaldokumenter (som Codex senere retter - les for kontekst, ikke endre):**
- `docs/reference/ipn-kildebibliotek.md` (port-farger)
- `docs/reference/ipn-samledokument.md` (prosa)
- `docs/reference/ipn-hovedokument.md` (skjelett)

**Bindende referanse for IPN-fakta:**
- `docs/reference/ipn-barekraft-sannhetsserum-2026-06-21.md` **§10** - komprimert kildekopi av selve utlysningen (Industri og tjenestenaeringer 2026). Bruk denne som fasit for utlysningstall.

## Konkrete punkter som MAA avklares (kjente motsetninger)

Rapportene spriker paa disse - din dom avgjoer:

| # | Sak | Hva rapportene sier | Hva du skal fastslaa |
| --- | --- | --- | --- |
| 1 | **An & Pivo vs Billio vs Kaza** (groenn finans, PD) | Tidlig: DOI `10.1007/s11146-021-09838-0` + "32 % lavere PD" knyttet til An. Senere korrigert: den DOI-en er **Billio et al. (JREFE 65(3):419-450, 2022)**; **An & Pivo** = *Real Estate Economics*, DOI `10.1111/1540-6229.12228`, **34 %**, kommersiell/CMBS; **Kaza et al. (2014)** = *Cityscape*, **32 %**, residensielt (~71 000 ENERGY STAR-boliger). | Bekreft de tre som **separate** kilder med riktig DOI/journal/scope. Tre poster, ikke en. |
| 2 | **Vannskadetall** | "78 500 vannskader" er **2021-tall**. Finans Norge 2023: ~10 skader/time (~87 600/aar), 5,1 mrd kr. | Fastslaa hvilket aar/tall som skal gjelde, og hvor det evt. staar (ikke i SotA). |
| 3 | **Wiik 2025 (SINTEF Notat 57)** | Flere soek: **ikke funnet** i aapne kilder (rapport-serien finnes, Notat 57 ikke indeksert). | 🔴 ikke bekreftet -> flagg for fjerning ELLER SINTEF-avklaring (grensetilfelle, se F8). |
| 4 | **Harerusten 2022 (konflikt 2,2 mrd)** | **Null treff** paa alle varianter (norsk+engelsk). Mulig feilstavet/upublisert. | 🔴 ikke bekreftet. Sjekk om 2,2 mrd-tallet finnes i en **annen, aapen norsk kilde** foer det flagges for fjerning. |
| 5 | **IPN-beloep** | Rapportene sier "16-20 mill". Utlysningen (sannhetsserum §10) sier **stoettegrenser 1-16 mill**, maks 50 %. | Rett til utlysningens tall (1-16 mill). |
| 6 | **Mecca 2023** | Bekreftet reell publikasjon (AHP 46 %/TOPSIS 20 %), men kildebiblioteket har den 🟡 (Wiley betalingsmur). | Bekreft metadata; marker om den kan baere paastand uten fulltekst. |

## Det du skal levere

Skriv resultatet til `docs/reference/vibs-verified-kildedom-2026-06-27.md` med:

1. **Samordnet domstabell** - en rad per kilde/paastand:
   `Paastand | Noekkel | Dom (🟢 bekreftet / 🔴 ikke bekreftet / ⚠️ feil-maa-rettes) | Kilde som bekrefter (pri NO/EU) | Hvilket dokument + ca. linje den staar i`
2. **Fjern-liste** - alle 🔴 samlet, klar for Codex (hva som skal ut, og hvilken setning det rammer).
3. **Rett-liste** - alle ⚠️ med foer/etter (riktig DOI/journal/tall).
4. **Grensetilfeller til Lars** - kilder som er 🔴 men teamet kanskje vil holde til SINTEF (Wiik 2025, Harerusten 2022). Ikke avgjoer disse selv.

## F8-regelen (grensetilfeller - ikke avgjoer selv)

Lars' regel er "ubekreftet helt vekk". Men Wiik 2025 og Harerusten 2022 er **ikke motbevist** - de venter paa SINTEF-fulltekst. Aa fjerne dem rykker ut baerende tall (2,2 mrd konflikt; -20 % klima). **Ikke slett dem og ikke behold dem stille** - legg dem i "grensetilfeller til Lars" med konsekvensen tydelig, saa han avgjoer.

## Ikke-maal

- Ikke rett i de tre kanoniske dokumentene (det er Codex' jobb).
- Ikke primaerverifiser betalingsmur-kilder (SINTEF, august).
- Ikke bruk Claudes/agentens egen kunnskap som belegg - kun aapen sitering.

## Akseptansekriterier

1. De fire rapportene er gjennomgaatt og samordnet til EN domstabell uten interne motsetninger.
2. Punkt 1-6 over er eksplisitt avgjort (riktig DOI/journal/scope/tall).
3. Hver dom har kilde med sitering; 🟢 prioriterer norske/europeiske kilder.
4. Fjern-liste, rett-liste og grensetilfelle-liste er separate og klare for Codex/Lars.
5. EBA-navnekollisjonen (EBA EU = bank vs EBA NO = entreprenoerforening) er intakt.

## Startprompt (lim inn til AGY i VS Code)

```text
Les docs/context/windows-score/29_agy_kildeverifisering_gjennomgang_handoff.md.

Gaa gjennom de fire verifiseringsrapportene (vibs-verified-*-2026-06-26.md) og
samordne dem til EN autoritativ domstabell. Avgjoer eksplisitt de seks kjente
motsetningene (An/Billio/Kaza, vannskadetall, Wiik 2025, Harerusten 2022,
IPN-beloep, Mecca 2023). Prioriter norske og europeiske kilder. Bruk
ipn-barekraft-sannhetsserum §10 som fasit for utlysningstall.

Lever til docs/reference/vibs-verified-kildedom-2026-06-27.md:
(1) samordnet domstabell, (2) fjern-liste (alle 🔴), (3) rett-liste (alle ⚠️
med foer/etter), (4) grensetilfeller til Lars (Wiik/Harerusten - ikke avgjoer
selv). Ikke rett i kildebibliotek/samledokument/hovedokument - det gjoer Codex.
```
