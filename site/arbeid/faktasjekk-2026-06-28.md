# Faktasjekk — VERIFIED statusside (index.html)

**Dato:** 2026-06-28
**Faktasjekker:** Claude (uavhengig kildekontroll, AGENTS.md kilde- og sannhetsregler)
**Sjekket fil:** `site/mockup/index.html`
**Sannhetskilder kryssjekket mot:**
- `docs/reference/vibs-verified-kildedom-2026-06-27.md` (kildedommen)
- `docs/reference/ipn-hovedokument.md`
- `docs/reference/state-of-the-art-verified-ipn.md`
- `docs/reference/ipn-samledokument.md`
- `docs/reference/forskning-kunnskapsbase.md`
- `site/innhold-kanban.md`
- `vibs-boligpass/docs/business/gronn-plattform.md` (konsortium/partnere)
- `AGENTS.md` (statusporter 🟢🟡🔴⏸)

**Statusvokabular:** 🟢 åpen siterbar kilde bekrefter · 🟡 sterk men ikke primærverifisert / venter SINTEF · 🔴 motsies eller ikke dekket (hallusinasjon / scope-creep) · ⚪ kan ikke verifiseres fra dokumentene (navn, intern info).

---

## 1. Domstabell

| # | Påstand i index.html | Ca. linje | Status | Kilde | Merknad |
|---|---|---|---|---|---|
| 1 | «kvalitetssikret av SINTEF» (hero-underlinje) | 95 | 🟡 | innhold-kanban §Hero (l.63); AGENTS.md (SINTEF inn aug. 2026) | Presens, men SINTEF starter primærverifisering først midten av aug. 2026. Sanksjonert ordlyd i kanban. Lav prioritet — noter spenningen. |
| 2 | «VERIFIED er et forskningsprosjekt for tryggere og mer bærekraftige byggevalg — bygd på åpen kunnskap» | 95 | 🟢 | innhold-kanban §Hero (l.63, ordrett valgt hero) | Eksakt godkjent hero-tekst. |
| 3 | Tilbudsfase-utfordring: valg tas under marginpress uten samlet, uavhengig beslutningsgrunnlag | 111–112 | 🟢 | ipn-samledokument §1 (l.22–32); state-of-the-art §2 | Kjernepremiss, godt dokumentert. |
| 4 | Digitale produktpass på vei + strengere klimadokumentasjonskrav; mildere krav for de minste | 115 | 🟢 | state-of-the-art §4 (CPR 2024/3110, DPP); §9 / Nordic Council 2023 (svakere krav for SMB) | DPP og SMB-lempning begge dekket. |
| 5 | Vannskader **5,1 mrd kr** i erstatninger 2023; «rundt 10 skader hver eneste time» | 122–124 | 🟢 | kildedom §2 / §5.2 (l.21,101,146–151); Finans Norge 2023 (publ. feb. 2024) | Korrigert + bekreftet i kildedommen. 100 % 🟢. Tall og «10/time» stemmer. |
| 6 | Norske boliger i snitt **18 000 kr/m²** dyrere å bygge enn Sverige | 129 | 🟢¹ | forskning-kunnskapsbase l.28,135 (UNION AS 2025); kanban 🟢-tabell | Bransjerapport (sekundær). Kilden på siden står «UNION 2025», dok. har «UNION AS 2025». Ikke kildedom-primærverifisert. |
| 7 | Driftsmargin norske byggmestere **3,3 %** | 136 | 🟢¹ | forskning-kunnskapsbase l.31,130 (BDO 2025); samledok l.24 | Kilden sier «3,3 % i **2024**» og «bygg» generelt; siden dropper årstall og skriver «byggmestere». Mindre presisjonsavvik. |
| 8 | **1 583** konkurser i bygg og anlegg 2025 | 143 | 🟢¹ | forskning-kunnskapsbase l.31,131 (Bjørheim 2026); samledok l.24 | Tall stemmer. Sekundærkilde, ikke kildedom-verifisert. |
| 9 | Byggefeil i **opptil halvparten** av alle **nye** boliger; årlig samfunnskostnad **10–30 mrd kr**, «Forskning indikerer» (Gullbrekken & Holme 2025) | 149–151 | 🟡 | kildedom §1 (l.29); hovedokument §1 (l.23); samledok §1 (l.12,35); kanban 🟡-tabell (l.41) | **10–30 mrd korrekt fraset som «Forskning indikerer» (🟡) ✓.** MEN ordlyd-avvik: kildene sier «**minst halvparten** har **minst én** byggefeil»; siden skriver «**opptil** halvparten» (svekker/vrir påstanden) og legger til «**nye**» som kildene ikke avgrenser til. Se §2 funn. |
| 10 | Rådata finnes: EPD og teknisk dok. i baser som NOBB | 162–163 | 🟢 | state-of-the-art §4 (NOBB, EPD-Norge); samledok §1 (l.26) | Dekket. |
| 11 | MCDA er etablert vitenskapelig metodikk | 163 | 🟢 | state-of-the-art §5 (Mecca 2023); samledok §2 (l.46) | Dekket. |
| 12 | Energikvalitet henger sammen med finansiell risiko for utlånere | 165–166 | 🟢 | state-of-the-art §7 (l.126,133); samledok §5 | Dekket. |
| 13 | **~32 %** lavere risiko for boliglånsmislighold på energieffektive boliger (Kaza 2014; Billio 2022) | 169–174 | 🟢 | kildedom (l.19,141); state-of-the-art §7 (l.133); kanban 🟢 (l.26) | **Korrekt:** bruker Kaza+Billio (residensielt, 🟢). Unngår 🟡-fellen An & Pivo 34 % (næringsbygg) ✓. |
| 14 | Åpne forskningsspørsmål: holdbarhet/kvalitet → redusert finansiell risiko mangler empirisk bevis | 191–192 | 🟢 | state-of-the-art §7 (l.134 HULL); samledok §2 (l.65); kanban 🔴 (l.55 — gap = FoU-spm) | **Korrekt:** presentert som åpent spørsmål/hypotese, ALDRI som påstand. Dette er riktig behandling av 🔴-gapet. |
| 15 | SMB-atferd i tilbudsfasen udokumentert | 194–195 | 🟢 | state-of-the-art §9 (l.158 HULL); samledok §2 (l.63) | Dekket som åpent spørsmål. |
| 16 | Mangler metodikk for å måle beslutningseffekt | 197–198 | 🟢 | state-of-the-art §2 akse (e); §11 | Dekket som åpent spørsmål. |
| 17 | Scoremodell skal koble produktdok., miljødata, levetid, kostnad, risiko og ombruk i ett forklarbart grunnlag for tilbudsfasen | 211–215 | 🟢 | samledok §0,§2,§3 (seks egenskaper); state-of-the-art §2 | Prosjektbeskrivelse, godt dekket. |
| 18 | Sammen med **Flekkefjord Sparebank** undersøke om bedre dok. kvalitet kan gi tryggere lånevilkår | 218 | 🟢 / ⚪² | gronn-plattform l.33,43,75 (Flekkefjord Sparebank = bankpilot/kravstiller) | Bankvinkel formulert som hypotese («undersøke om») ✓. Partner bekreftet. Selve lånevilkår-koblingen er FoU-hypotese, ikke påstand. |
| 19 | Holdbarhet→lån: «ingen har vist det samme for byggteknisk kvalitet» | 218 | 🟢 | state-of-the-art §7 (l.134); samledok §5 (l.112) | Korrekt fraset som gap. |
| 20 | VIBS = digital plattform + tilgang til pilotprosjekter/tømrerbedrifter | 233–234 | ⚪ | gronn-plattform (VIBS = eier/koordinator, plattform) | Rollebeskrivelse konsistent med GP-dok; pilotadgang er intern/forventet info. |
| 21 | **SINTEF AS** leder faglig arbeid med verifiseringsmodellen | 236–237 | 🟢 | gronn-plattform l.71 (SINTEF FoU-partner); AGENTS.md (SINTEF primærverifiserer) | Rolle dekket. |
| 22 | Konsortieliste: VIBS, SINTEF, Ordercontrol/Byggstand, Tirna Fagskole, NorDan, Flekkefjord Sparebank, Farsund kommune, Miljødirektoratet + roller | 242–251 | 🟢 / 🟡³ | gronn-plattform §Konsortium (l.64–77) | **Alle åtte partnere + roller matcher GP-dok ordrett.** MEN kilden er **Grønn Plattform**-søknaden (annet, større virkemiddel: 120/65 MNOK, 2027–2030), ikke et IPN-dok. GP-dok (l.33,150) sier Tirna/Byggstand/Miljødirektoratet er løftet til formelle roller *kun i GP-rammen*. Se §2 funn (scope/formalitetsnyanse). |
| 23 | **Nøkkelpersoner:** Bjørn Skeime, Lars Gunnar Stokke, Lars Erik Brekne Johnsen, Christine Reinertsen, **Thomas Thorsen** | 253 | ⚪ (4 navn bekreftet, 1 ikke funnet) | gronn-plattform §Prosjektledelse (l.79–84) | De fire første matcher GP-dok ordrett. **«Thomas Thorsen» finnes IKKE i noe lest kildedokument** — verken i prosjektledelse eller konsortium. Se §2 funn (krever handling). |
| 24 | Kobling til **BKA2** (Bærekraftige anskaffelser), **11,7 MNOK** fram til **2028**, Vegard Knotten = SINTEFs representant | 256–260 | 🟢 | kildedom (l.31 BKA2); state-of-the-art §9 (l.160) + §13 (l.271); kanban 🟢 (l.33) | Tall, årstall og navn bekreftet. BKA2 prosjekteier er Trondheim kommune (ikke nevnt på siden — ok). |
| 25 | Piloter for 2026 planlegges — bl.a. Flekkefjord Sparebank og Farsund kommune | 273 | 🟢 | gronn-plattform l.150 (piloter 2026: Flekkefjord Sparebank, Farsund kommune) | Begge pilotnavn bekreftet. |
| 26 | SINTEF starter formell primærverifisering **midten av august 2026** | 275–276 | 🟢 | AGENTS.md (l.31 «midten av august 2026»); kanban; samledok §6 | Dato bekreftet mot AGENTS.md. |
| 27 | Sidemeny: Prosjekttype IPN; metodikk «Flerkriterieanalyser (MCDA) og atferdsstudier» | 59,63 | 🟢 | state-of-the-art (IPN-virkemiddel); samledok §2 akse 5 (atferdsforskning); §5 MCDA | Dekket. |
| 28 | Partnerstripe: «forskningssamarbeid mellom VIBS • SINTEF» | 73–76 | 🟢 | gronn-plattform; AGENTS.md (VIBS + SINTEF kjerne) | Dekket. |

¹ 🟢 i innhold-kanban og forskning-kunnskapsbase, men **ikke** uavhengig verifisert i kildedommen; bransjerapporter (sekundærkilder). Akseptabelt for publisering per kanban, men ikke primærverifisert.
² Partner 🟢; den finansielle koblingen er FoU-hypotese (ikke påstand) og dermed riktig fraset.
³ Roller 🟢 mot GP-dok, men 🟡 på *formalitetsgrad for IPN-søknaden* — se funn.

---

## 2. Funn som krever handling (🔴 + tvil)

Ingen **🔴-kilder bærer noen påstand** på siden. De to nedenstående er **innholdsrettelser**, ikke kildedisiplin-brudd — men begge bør rettes før publisering.

### A. KREVER HANDLING NÅ — «Thomas Thorsen» (linje 253) ⚪
- De fire andre nøkkelpersonene (Skeime, Stokke, Brekne Johnsen, Reinertsen) er **ordrett bekreftet** i `gronn-plattform.md` (l.81–84). Nettopp derfor skiller dette navnet seg ut: **Thomas Thorsen finnes ikke i noe lest kildedokument** — verken som prosjektledelse, konsortium eller kontaktperson.
- Dette er ikke generisk «navn kan ikke verifiseres» — det er ett uverifisert navn blant fire som sjekker ut. Mulig korrekt intern person, mulig feil/utdatert.
- **Tiltak:** Lars må bekrefte at Thomas Thorsen faktisk er nøkkelperson før dette publiseres. Ikke rett selv.

### B. KREVER HANDLING NÅ — «opptil halvparten av alle nye boliger» (linje 150) 🟡
- Kildene sier konsekvent **«minst halvparten … har minst én byggefeil»** (kildedom l.29: «1 feil i halvparten»; hovedokument l.23: «minst én feil i halvparten»; samledok l.35: «Minst halvparten … har minst én byggefeil»).
- Siden skriver **«opptil halvparten»** — dette vrir «minst» til «opptil» (en svakere/annen påstand) — og legger til **«nye»**, en avgrensning kildene ikke har.
- 10–30 mrd-tallet og «Forskning indikerer»-framingen er **korrekt 🟡-fraset** ✓. Det er kun *halvparten*-ordlyden som avviker.
- **Tiltak:** Endre til kildenes formulering, f.eks. «minst halvparten av alle boliger har minst én byggefeil». Verifiser om «nye» skal stå.

### C. NOTER (scope/nuance, ikke blokker) — konsortium hentet fra Grønn Plattform-dok 🟡
- Alle åtte partnere + roller matcher `gronn-plattform.md` ordrett. Men dette er **Grønn Plattform**-konsortiet (annet/større virkemiddel: 120 MNOK total, 65 MNOK søkt, 2027–2030).
- GP-dok (l.33,150) sier eksplisitt at Tirna, Byggstand og Miljødirektoratet er løftet «fra «kontakter» til formelle konsortiumsroller» **kun i GP-rammen**. Å presentere alle åtte som et avklart «bredt konsortium» for IPN-en kan overdrive formaliteten for enkelte partnere.
- **Tiltak:** Bekreft at konsortierollene gjelder/er forpliktet også for IPN-søknaden, ev. nyansér ordlyd. Ikke en 🔴.

### D. MINDRE PRESISJON (lav prioritet)
- Linje 136: «3,3 %» — kilden presiserer **«i 2024»** og «bygg» generelt; siden dropper årstall + skriver «byggmestere».
- Linje 95: «kvalitetssikret av SINTEF» i presens, men SINTEF starter først aug. 2026 (sanksjonert av kanban — kun noter).
- Linje 131: «UNION 2025» vs. dok. «UNION AS 2025» (kosmetisk).

---

## 3. Bekreftede PASSES (kildedisiplin-kontroller)

Eksplisitt verifisert at følgende **ikke** forekommer / er korrekt behandlet:

- ✅ **Wiik 2025 (SINTEF Notat 57)** — nevnes IKKE noe sted på siden. (⏸ TATT UT, korrekt.)
- ✅ **Konfliktkostnad 2,2 mrd kr/år** — nevnes IKKE noe sted. (⏸ TATT UT, korrekt.)
- ✅ **NFR-vurderingskriterier (Kvalitet/Effekter/Gjennomføring)** — IKKE nevnt eksplisitt (kanban-krav l.71 overholdt).
- ✅ **Holdbarhet→misligholdsrisiko** — opptrer KUN som hypotese/åpent spørsmål (l.192, l.218 «undersøke om…»), aldri som påstand. Korrekt behandling av det dokumenterte gapet.
- ✅ **32 %-tallet** bruker Kaza+Billio (residensielt, 🟢) — unngår den 🟡-flaggede An & Pivo 34 %-fellen (næringsbygg/CMBS).
- ✅ **Byggefeil 10–30 mrd** fraset som «Forskning indikerer» (🟡), ikke som hard påstand.
- ✅ **Vannskade 5,1 mrd / ~10 per time** — korrekt 🟢-tall (Finans Norge 2023, korrigert i kildedom).
- ✅ **BKA2 11,7 MNOK / 2028 / Knotten** — korrekte tall og navn.
- ✅ **Ingen statusfarger (🟡/🔴) vises på siden** — usikkerhet uttrykkes som «åpne forskningsspørsmål» i klartekst (kanban-prinsipp l.11–13 overholdt).

---

## 4. Statustelling

| Status | Antall | Kommentar |
|---|---|---|
| 🟢 | 19 | (inkl. 3 med ¹-forbehold: UNION/BDO/Bjørheim sekundær, ikke kildedom-primærverifisert) |
| 🟡 | 2 | byggefeil/halvparten-ordlyd (#9); konsortie-formalitet for IPN (#22, delvis) |
| 🔴 | 0 | **Ingen 🔴-kilde bærer noen påstand.** |
| ⚪ | 3 | VIBS pilotadgang (#20); konsortium intern (#22 navn); nøkkelpersoner (#23) — hvorav «Thomas Thorsen» ikke funnet i kilder |

(Tellingen er per domstabell-rad; enkelte rader har dobbeltstatus markert med skråstrek og telles på primærstatus.)

---

## 5. Konklusjon — er siden innsendingsklar mht. kildedisiplin?

**Ja, i all hovedsak.** På ren **kildedisiplin** er siden essensielt innsendingsklar:

- Ingen 🔴-kilde bærer en påstand.
- Begge bannlyste elementer (Wiik 2025, konfliktkostnad 2,2 mrd) er fjernet.
- Forbeholdene er riktige: byggefeil-tallet (10–30 mrd) er 🟡-fraset som «Forskning indikerer», holdbarhet→risiko står som hypotese, og 32 %-tallet bruker de korrekte residensielle kildene (ikke An & Pivo-fellen).
- NFR-kriteriene er ikke nevnt eksplisitt; ingen statusfarger lekker til siden.

**To rettelser bør gjøres før publisering — men ingen av dem er kildedisiplin-brudd:**
1. **Thomas Thorsen** (l.253): bekreft navnet — ikke funnet i kildene mens de fire andre er ordrett bekreftet.
2. **«opptil halvparten av alle nye boliger»** (l.150): rett til kildenes «minst halvparten … minst én byggefeil», og avklar «nye».

I tillegg bør konsortie-formaliteten for IPN-rammen (vs. Grønn Plattform) bekreftes, og tre bransjetall (UNION/BDO/Bjørheim) noteres som sekundære/ikke primærverifiserte. Disse er nyanser, ikke blokkere.

**Bunnlinje:** «essensielt klar» betyr ikke «ingen handling». De to navngitte punktene over (navn-sjekk + ordlyd-mykning) bør rettes nå; resten er forbehold å være bevisst på.
