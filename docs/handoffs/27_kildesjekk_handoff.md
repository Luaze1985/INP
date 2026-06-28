---
title: Handoff - Kildesjekk for IPN-soeknaden
date: 2026-06-26
status: ready
from: claude
to: claude (Sonar) + lars
branch: antigravity/snekker-pilot
tags: [vibs, verified, ipn, kilder, sonar, faktasjekk, provenans]
---

# Handoff: Kildesjekk for IPN-soeknaden

## Kort beskjed

Flytt de viktigste kildene fra **gul** (sterk, men ikke primaerverifisert) mot **groenn** (aapnet og bekreftet) saa langt det gaar **uten SINTEF**. To verktoey: Sonar (Claude, aapne nettkilder) og Lars Erik (laster ned offentlige PDF-er). Betalingsmur-kilder venter paa SINTEF i august.

## Maal

Etter denne oppgaven skal `docs/reference/ipn-kildebibliotek.md` ha oppdaterte port-farger paa de kildene som kan lukkes naa, og endringene skal slaa gjennom i `ipn-samledokument.md` og berorte kapitler.

## Provenans-porten (repetisjon)

- 🟢 **Primaerkilde aapnet og verifisert for den paastanden den stoetter** - kan baere en setning alene i soeknaden.
- 🟡 **Sterk men ikke primaerverifisert**, eller konsortie-internt (bestillingsverk) - maa aapnes foer baerende bruk.
- 🔴 **Bare metadata/soeketreff** - ikke siterbar.

## Allerede gjort: F4-faktasjekk (Sonar, 2026-06-26)

| Paastand | Resultat | Status |
| --- | --- | --- |
| "Norges stoerste fastlandsnaering" | Bekreftet - NHO Byggenaeringen, Sammen 2030. ~8-9 % av Fastlands-BNP (NTNU/Concept). | OK, legg kilde i margen |
| "En av de minst digitaliserte" | Faglig konsensus, men ingen rapport rangerer naeringene eksplisitt. | Behold "en av de minst", ikke "den minst" |
| "En av de mest fragmenterte" | Bekreftet - SSB: >99 % SMB, byggenaering hoey SMB-andel, faa store. | OK |

## Cowork-modus (mobil) - koe av domkort

Dette er hovedmodusen for kveldsoekten: du styrer fra mobil, jeg jobber, du sjekker.

**Pipeline per kort:** Claude (LLM) formulerer soeket -> Sonar (eller Claude Research) henter kilde med sitering -> du tapper.

**Jernregel:** Claudes egen kunnskap teller ALDRI som belegg. Et kort blir 🟢 bare hvis en aapen kilde med sitering bekrefter paastanden. Uten sitering = 🟡.

Hvert kort presenteres slik (kort nok for telefon):

> **Kort N - [paastand]**
> Kilde funnet: [sitering]
> Domforslag: 🟢 / 🟡
> Du svarer: ✅ godta · ↩ gul · ⏭ hopp

### Koen (Sonar-sjekkbare paastander)

| # | Paastand | Kilde i dag | Sjekk |
| --- | --- | --- | --- |
| 1 | Byggfeil 10-30 mrd/aar | Gullbrekken og Holme 2025 (bestillingsverk 🟡) | Finnes tallet i aapen uavhengig kilde? |
| 2 | Konflikt 2,2 mrd/aar + hva omfatter det (F5) | Harerusten 2022 🟡 | Bekreft tall + hva som er inkludert |
| 3 | Driftsmargin 3,3 % (2024) | BDO 2025 🟡 | Bekreft |
| 4 | 1 583 konkurser i naeringen 2025 | Bjorheim 2026 🟡 | Bekreft |
| 5 | 18 000 kr/m2 dyrere enn Sverige | UNION 2025 🟡 | Bekreft + kontekst |

F4-kortene (stoerste fastlandsnaering / minst digitalisert / mest fragmentert) er allerede kjoert - se tabellen over.

**Etter hvert godkjent kort:** Claude oppdaterer port-farge i `ipn-kildebibliotek.md` og slaar tallet gjennom i `ipn-samledokument.md`. Audit-trail (soekestreng, modell, kilde, tidspunkt) logges per kort.

---

## Steg 1: Lars aapner de offentlige kildene (ingen betalingsmur)

| Kilde | Hvor | Brukes til | Sjekk |
| --- | --- | --- | --- |
| **KD mfl. 2024** (tidligfase + A1-A3 = 63 %) | regjeringen.no kunnskapsgrunnlag | K1, K2, V1 | Bekreft tidligfase-poeng + A1-A3-andel |
| **EBA NO 2023** (20 % uten merkostnad) | EBA NO klimagass-veileder, offentlig PDF | V1 | Bekreft 20 %-tallet og konteksten |
| **Billio mfl.** (bankrisiko) | Fullfoer referansen (SAFE WP 261?) | V3 | Komplett referanse + kobling energi<->mislighold |

Naar en kilde er aapnet og tallet stemmer: sett 🟢 i kildebiblioteket, "aapnet: ja".

## Steg 2: Sonar-faktasjekk (Claude kjoerer)

Kjoer Sonar paa paastander som kan verifiseres mot aapne kilder. Start server foerst (idempotent), POST til `http://127.0.0.1:8765/search`, oppgi soekestreng + modell + tidspunkt + kilder i audit-trail.

Kandidater aa sjekke:
- Byggfeil-kostnad 10-30 mrd/aar (Gullbrekken og Holme 2025) - finnes tallet i en aapen sekundaerkilde uavhengig av bestillingsverket?
- Konflikt 2,2 mrd/aar (Harerusten 2022) - hva omfatter tallet (F5)?
- Driftsmargin 3,3 % 2024 (BDO 2025) - bekreft.
- 1 583 konkurser 2025 (Bjorheim 2026) - bekreft.
- 18 000 kr/m2 vs Sverige (UNION 2025) - bekreft.

For hver: marker 🟢 hvis aapen kilde bekrefter, 🟡 hvis bare bestillingsverket har den.

## Steg 3: Det SINTEF maa ta (IKKE naa)

Disse staar 🟡 til SINTEF aapner fulltekst i august - ikke bruk tid paa dem naa:
- **Mecca 2023** (MCDA "veletablert") - Wiley, betalingsmur
- **Wiik 2025** (Notat 57, klima -20 %) - SINTEF fulltekst
- **Gullbrekken og Holme 2025** - SINTEF fulltekst (hvis ikke lukket i steg 2)

## Ikke-maal

- Ingen primaerverifisering av betalingsmur-kilder (SINTEF, august).
- Ikke endre paastander til "etablert" som teamet ennaa vil ha som aapne hypoteser (F8 - Lars avgjoer).
- Ingen masseinnhenting via Sonar uten at det er nytte i det.

## Akseptansekriterier

1. KD 2024, EBA NO 2023 og Billio-referansen er aapnet/komplettert og oppdatert i kildebiblioteket med ny port-farge.
2. Sonar-faktasjekkene i steg 2 er kjoert, med audit-trail (soekestreng, modell, kilder, tidspunkt).
3. Endringene er slaatt gjennom i `ipn-samledokument.md` der tallene staar.
4. EBA-navnekollisjonen (EBA EU <> EBA NO) er fortsatt korrekt overalt.

## Startprompt - cowork mobil (lim inn i kveld)

```text
Les docs/context/windows-score/27_kildesjekk_handoff.md.

Kjoer cowork-koen som domkort, ett om gangen. For hvert kort: formuler soeket,
hent kilde med sitering via Sonar (sonar-search-skillen), og gi meg domforslag
🟢/🟡 i kortformatet. Jernregel: 🟢 bare med sitering. Vent paa mitt tapp
(godta/gul/hopp) foer neste kort. Oppdater ipn-kildebibliotek.md +
ipn-samledokument.md fortloepende, med audit-trail per kort. Ikke roer
betalingsmur-kildene (SINTEF).
```
