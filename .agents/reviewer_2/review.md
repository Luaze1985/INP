# Review-rapport: State of the Art og Forskningsevaluering (v0.5 Kandidat)

**Reviewer:** Reviewer 2 (Roller: `reviewer`, `critic`)  
**Dato:** 2026-08-02  
**Vurdert dokument:** `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md`  
**Referansekontroll:** `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`  
**Konklusjon / Vurdering:** **`APPROVE`**

---

## 1. Review Sammendrag (Review Summary)

Dokumentet `forskning-og-soa-v0.5-kandidat.md` har gjennomgått en fullstendig ontologisk, terminologisk og portstatus-messig samsvarskontroll mot `vibs-verified-ord-og-kildekart-v0.5.yml` og tilhørende kilde- og sannhetsregler.

Kandidatdokumentet er et særdeles grundig, faglig autoritativt og kildekritisk samledokument på 703 linjer som dekker samtlige seks seksjoner for State of the Art og forskningsevaluering til NFR IPN 2026-søknaden.

### Verdivurdering per kontrollpunkt:

1. **Godkjent begrep «løsningsvalg» (og fravær av smalt «produktvalg»):** **`BESTÅTT` 🟢**
   - «Løsningsvalg» benyttes gjennomgående (Seksjon 1, 2, 3, 4, 5, 6) for å beskrive helhetlige valg i tilbudsfasen (byggevare, montering, levetid, LCC).
   - Det smale begrepet «produktvalg» forekommer **kun** som eksplisitt avvisning/metadiskusjon (f.eks. «'Løsningsvalg' fremfor 'produktvalg'»), aldri som aktiv beskrivelse.

2. **Godkjent begrep «testflate» for VIBS-plattformen:** **`BESTÅTT` 🟢**
   - VIBS-plattformen omtales konsekvent som en **«testflate»** for utprøving av beslutningsmodeller i tilbudsfasen.

3. **Bruk av «beslutningsstøtte» og fravær av forbudte automatiserte/svart boks-påstander:** **`BESTÅTT` 🟢**
   - Modellens rolle defineres konsekvent som **«beslutningsstøtte»**.
   - Påstander som «VERIFIED velger automatisk» eller «anbefaler automatisk» er fullstendig fraværende.
   - Alle forekomster av uttrykket «svart boks» brukes enten kritisk mot eksisterende verktøy eller for å slå fast et ufravikelig forbud mot skjulte totalskårer for VERIFIED.

4. **Parkert status ⏸ opprettholdt for `[Wiik2025]` og `[SA2018]`:** **`BESTÅTT` 🟢**
   - `[Wiik2025]` (SINTEF Notat 57) og `[SA2018]` (Samfunnsøkonomisk analyse 4-2018) er eksplisitt markert som **⏸ Parkert** i samsvar med prosjektleders beslutning (2026-06-28).
   - Ingen av de parkerte kildene benyttes som aktivt primærbelegg. Aktive kilder (`[EBA_NO2023]` 🟡 og `[KD2024]` 🟡) benyttes for påstander om materialvalg og tidligfaserom.

5. **Strengt skille mellom `[EBA_EU2023]` 🟢 og `[EBA_NO2023]` 🟡:** **`BESTÅTT` 🟢**
   - `[EBA_EU2023]` 🟢 (European Banking Authority, finansregulering/grønne lån) og `[EBA_NO2023]` 🟡 (Entreprenørforeningen Bygg og Anlegg Norge, veileder for boligblokker) behandles som to helt adskilte kilder.
   - Seksjon 4.4 inneholder en egen ontologisk distinksjonsfigur og eksplisitte skillereregler. Generisk `[EBA]` forekommer ikke i sitatsammenheng.

6. **Portstatussymboler (🟢, 🟡, ⏸, 🔴) på alle vitenskapelige påstander og tabellrader:** **`BESTÅTT` 🟢**
   - Alle kildesitater i teksten er påført sine respektive portstatussymboler.
   - Samtlige tabeller i Seksjon 2.8, 3.2.4, 4.7, 5.4 og 6.2 har eksplisitte portstatuskolonner eller markører på alle rader.

---

## 2. Verifiserte påstander (Verified Claims)

| Påstand / Kontrollpunkt | Verifiseringsmetode | Resultat |
| :--- | :--- | :---: |
| Absence of active "produktvalg" | Linje-for-linje skanning for `produktvalg` | **PASS** 🟢 |
| Consistent "løsningsvalg" usage | Tekstgransking i Seksjon 1.2, 2.2, 3.2.4, 4.1, 5.5, 6.4 | **PASS** 🟢 |
| Platform termed "testflate" | Tekstgransking i Seksjon 1.4, 2.1, 3.4, 5.5, 6.3 | **PASS** 🟢 |
| Function termed "beslutningsstøtte" | Tekstgransking i Seksjon 1.1, 2.1, 3.2.5, 4.1, 5.5, 6.3 | **PASS** 🟢 |
| No automated choice/recommendation claims | Søk etter `velger automatisk` / `anbefaler automatisk` | **PASS** 🟢 |
| Black box claims rejected/forbidden | Søk etter `svart boks` og kontekstanalyse | **PASS** 🟢 |
| `[Wiik2025]` & `[SA2018]` status ⏸ Parkert | Tekstgransking i Seksjon 4.6, 4.7, 5.5, 6.4 | **PASS** 🟢 |
| Separation of `[EBA_EU2023]` 🟢 & `[EBA_NO2023]` 🟡 | Tekstgransking i Seksjon 1.3, 2.2, 4.3, 4.4, 4.7, 5.5, 6.4 | **PASS** 🟢 |
| Gate status symbols on text & table rows | Tekstgransking i alle seksjoner (Seksjon 1–6 og tabeller) | **PASS** 🟢 |

---

## 3. Adversariell vurdering og stresstesting (Critic Challenge)

Som kritiker har jeg stresstestet dokumentet mot potensielle sviktmodeller, skjulte forutsetninger og ontologiske smutthull:

### Challenge 1: Fare for sirkelargumentasjon via SINTEF-kilder
- **Stresstest:** Ble konsortie-interne notater (f.eks. `[Wiik2025]`) forsøkt sneket inn for å bevise at materialendringer i tilbudsfasen er kostnadsnøytrale?
- **Funn:** Kandidatdokumentet opprettholder et krystallklart forbud mod sirkelargumentasjon. `[Wiik2025]` er eksplisitt parkert (⏸), og påstanden om at tidlige materialvalg gir reduksjoner uten merkostnad forankres i den uavhengige kilden `[EBA_NO2023]` 🟡 (veileder for boligblokker utgitt med Grønn Byggallianse og Norsk Eiendom) samt `[KD2024]` 🟡.

### Challenge 2: Sammenblanding av bankregulering (EBA EU) og byggveileder (EBA Norge)
- **Stresstest:** Er det noen steder i teksten hvor leseren kan mistolke at European Banking Authority har utgitt en veileder for boligblokker, eller at EBA Norge regulerer grønne boliglån?
- **Funn:** Seksjon 4.4 adresserer denne risikoen direkte med et ontologisk kildeddiagram og to obligatoriske skillereregler. Ingen sammenblanding forekommer.

### Challenge 3: Skjult ranginversjon i MCDA-modellen
- **Stresstest:** Fremstilles flerkriteriemodellen (AHP/TOPSIS/MIVES) som en feilfri "fasit" som løser alle rangingsproblemer?
- **Funn:** Dokumentet tar et eksplisitt **metodisk forbehold mot ranginversjon (Rank Reversal)** i Seksjon 3.3 og 6.3 (FoU-hypotese F3). Det framsettes som en FoU-hypotese som skal undersøkes og varsles i testflaten, ikke som et ubegrunnet løfte.

### Challenge 4: Integritetskontroll (fusk, facades, hardkoding)
- **Stresstest:** Finnes det tegn på hardkodede jukseresultater, atarbeidede fasader uten reelt innhold, eller manglende uavhengig verifikasjon?
- **Funn:** Dokumentet er et genuint og konsistent syntesearbeid på 703 linjer med dyptgående vitenskapelige referanser (bl.a. Edelen & Ingwersen 2018, Weidema 1996, Benke 2025, Kaza 2014, Billio 2022, An & Pivo 2020, EN 15978:2026 publisert 17.04.2026, NS-EN 16627 der NS 3454 eksplisitt oppgis som trukket 07.09.2023). Ingen integritetsbrudd avdekket.

---

## 4. Konklusjon og vedtak (Verdict)

**Endelig vedtak:** **`APPROVE`**

Dokumentet `docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md` tilfredsstiller samtlige krav i `docs/reference/vibs-verified-ord-og-kildekart-v0.5.yml`. Det anbefales godkjent som SoA-kandidat for v0.5.
