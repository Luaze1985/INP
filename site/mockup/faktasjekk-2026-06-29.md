# Faktasjekk — VERIFIED statusside (index.html)

**Dato:** 2026-06-29
**Kontrollert av:** Claude Code (automatisk, ikke primærverifisert)
**Kildegrunnlag:** vibs-verified-kildedom-2026-06-27.md, ipn-hovedokument.md, state-of-the-art-verified-ipn.md, ipn-samledokument.md, AGENTS.md, site/innhold-kanban.md, vibs-boligpass/docs/business/gronn-plattform.md, site/benchmark-forbilder.md
**Formål:** Streng kryssjekk av alle synlige påstander i index.html mot kildedomet.

> Statuskolonne bruker prosjektets egne porter: 🟢 (åpen kilde bekrefter) / 🟡 (sterk, ikke primærverifisert) / 🔴 (motsies eller ikke dekket) / ⚪ (kan ikke verifiseres fra docs).
>
> **ADVARSEL:** Tre funn krever handling: 🟡 H0 (hero selvmotsigelse SINTEF-QA), ⚪ H1 (Thomas Thorsen ubekreftet), 🟡 H2 (nær-variant av forbudt «bro»-metafor). Se handlingsliste.

---

## 1. Domstabell — påstand for påstand

| Nr | Påstand (slik den vises i index.html) | Status | Kilde(r) som bekrefter / avviker | Merknad |
|---|---|---|---|---|
| 1 | "VERIFIED er et forskningsprosjekt for tryggere og mer bærekraftige byggevalg — bygd på åpen kunnskap, **kvalitetssikret av SINTEF**." | 🟡 | AGENTS.md; gronn-plattform.md bekrefter SINTEF som FoU-partner. MEN: seksjon 7 på samme side sier SINTEF «starter det formelle arbeidet med primærverifisering… i midten av august 2026» (fremtid). Hero-teksten bruker «kvalitetssikret» i presens som avsluttet faktum. Intern selvmotsigelse. | Intern selvmotsigelse med seksjon 7: QA er ikke utført ennå. Forsvares som «SINTEF er utpekt QA-ansvarlig», men streng leser vil lese det som gjennomført. Se H0 i handlingslisten. |
| 2 | "IPN-Forskningsprosjekt" (topptag) | 🟢 | AGENTS.md (utlysning: Innovasjonsprosjekt i næringslivet 2026) | Korrekt. |
| 3 | Prosjekttype: "Innovasjonsprosjekt i næringslivet (IPN)" | 🟢 | AGENTS.md | Korrekt. |
| 4 | Målgruppe: "SMB-entreprenører og boligkjøpere" | 🟢 | ipn-samledokument §0; kanban narrativ-arc | Korrekt. |
| 5 | Metodikk: "Flerkriterieanalyser (MCDA) og atferdsstudier" | 🟢 | ipn-samledokument §2; state-of-the-art §5 og §9 | Korrekt. |
| 6 | Sidebar-partner: "Et forskningssamarbeid mellom VIBS og SINTEF" | 🟡 | gronn-plattform.md (8 partnere) | Korrekt, men en forenkling. Konsortiet har 8 formelle partnere. Akseptabel sideforenkling. |
| 7 | "Vi mangler i dag et samlet og uavhengig beslutningsgrunnlag for å velge bærekraftige materialer." | 🟢 | state-of-the-art §4, §10; ipn-samledokument §1 | Kjerneargument godt dokumentert. |
| 8 | "digitale produktpass er på vei inn" | 🟢 | state-of-the-art §4: ESPR (EU) 2024/1781 og CPR 2024/3110 — EUR-Lex åpnet [H] | Korrekt. |
| 9 | "kravene bevisst mildere for de minste bedriftene — av hensyn til konkurranseevnen" | 🟢 | Nordic Council 2023 — fulltekst åpnet [H], state-of-the-art §9: «driven mainly by a fear of reducing the competitiveness for smaller actors» | Korrekt, direkte sitert. |
| 10 | "dagens verktøy er laget for spesialister, ikke for en travel tilbudsfase" | 🟢 | state-of-the-art §10 (verktøyscan); Nordic Council 2023 [H] | Korrekt. |
| 11 | **Vannskader 2023: "5,1 milliarder kroner" / "10 skader hver eneste time"** (Kilde: Finans Norge 2023) | 🟢 | kildedom rad [Vannskadetall]: 2023-tall bekreftet etter korrigering (2021-tall var 78 500/4,0 mrd). 5,1 mrd og 10/time er de riktige 2023-verdiene. | Korrekt og bekreftet. |
| 12 | **"Norske boliger er i snitt 18 000 kr/m² dyrere å bygge enn i Sverige"** (Kilde: UNION 2025) | 🟡 | Kanban 🟢-liste (bransjerapport); state-of-the-art §1 behandler det som «etablert grunnlag». Kildedom-tabellen verifiserer ikke UNION 2025 eksplisitt. | I kanban merket 🟢, men uten dokumentert primæråpning i kildedomtabellen. Publisert som faktapåstand uten forbehold — akseptabelt etter kanbans redaksjonelle dom, men bør noteres. |
| 13 | **"Gjennomsnittlig driftsmargin i byggebransjen lå på kun 3,3 % i 2024"** (Kilde: BDO 2025) | 🟡 | Kanban 🟢-liste; ipn-samledokument §1. Kildedom-tabellen verifiserer ikke BDO 2025 eksplisitt. | Samme situasjon som UNION 2025. Kanbans redaksjonelle dom er 🟢, men ingen dokumentert primæråpning i kildedom. |
| 14 | **"I 2025 ble det registrert 1 583 konkurser i bygg og anlegg"** (Kilde: Bjørheim 2026) | 🟡 | Kanban 🟢-liste; ipn-samledokument §1 (linje 24). Kildedom-tabellen verifiserer ikke Bjørheim 2026 eksplisitt. Hvem er Bjørheim? Ikke beskrevet i noen kildedokument. | Kanban sier 🟢, men kildedomet mangler eksplisitt verifikasjon. «Bjørheim 2026» er ikke nærmere beskrevet (forfatter, utgiver) i noen tilgjengelig kildedokument. Bør avklares. |
| 15 | **"Forskning indikerer at minst halvparten av alle boliger har minst én byggefeil, med en årlig samfunnskostnad på mellom 10 og 30 milliarder kroner."** (Kilde: Gullbrekken & Holme 2025) | 🟡 | Kildedom [GullbrekkenHolme2025] 🟢 i kildedommen, men behandles som 🟡 i kanban (konsortie-notat, primær ikke åpnet). HTML-teksten er korrekt frasert med «Forskning indikerer» i tråd med kanban-regelen. | RIKTIG FRASERT. Forbehold er inkludert. |
| 16 | "Vi vet at rådataene finnes. Miljødeklarasjoner (EPD) og teknisk dokumentasjon ligger lagret i store baser som NOBB." | 🟢 | state-of-the-art §4 (EPD-Norge, NOBB) [M]; ipn-samledokument §2 | Korrekt. |
| 17 | "Flerkriterieanalyser (MCDA) er en etablert vitenskapelig metodikk" | 🟢 | state-of-the-art §5 (Mecca 2023 [H*], AHP 46 %/TOPSIS 20 %) | Korrekt. |
| 18 | "energikvalitet henger sammen med finansiell risiko for de som låner ut penger" | 🟢 | kildedom [Billio2022] 🟢 og [Kaza2014] 🟢; state-of-the-art §7 [H] | Korrekt. |
| 19 | **"~32 % lavere risiko for mislighold av boliglån... på energieffektive boliger"** (Kilde: Kaza 2014; Billio 2022) | 🟢 | kildedom: Kaza 2014 = 32 % for residensielle boliger (Cityscape 16(1):279–298) 🟢; Billio 2022 = nederlandske boliglån (JREFE 65(3):419–450) 🟢. Begge fulltekst åpnet. Korrekt attribuert til boliglån (ikke næringsbygg/An & Pivo). | Korrekt og korrekt attribuert. An & Pivo 2020 (næringsbygg/CMBS, 34 %) brukes ikke her — riktig. |
| 20 | Åpent FoU-spørsmål 1: "Vi mangler empirisk bevis på om høyere teknisk kvalitet og holdbarhet på byggevarer kan kobles direkte til redusert finansiell risiko for bankene." | 🟢 | state-of-the-art §7 «HULL / FoU-ARGUMENT»: «Ingen studie kobler bygningskvalitet, fuktrobusthet eller vedlikeholdssvikt direkte til misligholdsrisiko.» [H for hullet]; ipn-samledokument §2 og §5 | Korrekt dokumentert gap. |
| 21 | Åpent FoU-spørsmål 2: "Vi vet ikke om tømrere og byggmestere faktisk vil endre sine materialvalg..." | 🟢 | state-of-the-art §9 «HULL – bekreftet»; Nordic Council 2023 [H]; BKA2-kobling | Korrekt. |
| 22 | Åpent FoU-spørsmål 3: "Vi mangler en vitenskapelig metodikk for å måle om et forenklet beslutningsgrunnlag faktisk fører til mer bærekraftige valg i praksis." | 🟢 | F4 i ipn-hovedokument; state-of-the-art §9; ipn-samledokument §2 (punkt 5) | Korrekt. |
| 23 | **H2-tittel seksjon 5: "Vi skal teste broen fra data til valg"** | 🟡 | benchmark-forbilder.md forbudsliste: «gjentatt «bro fra data til beslutning»». Nøkkelkvalifisereren er **gjentatt** og nøkkelordet er **beslutning** — ikke **valg**. HTML bruker en enkelt nær-variant («valg», ikke «beslutning») én gang som overskrift. Strengt lest er dette ikke en bokstavelig brudd på «gjentatt»-regelen. | Nær-variant av den frarådte «bro»-metaforen, brukt én gang. Ikke et teknisk forbudsbrudd («gjentatt» er vilkåret), men bør omformuleres for å unngå klisjetonen. Se H2. |
| 24 | "Vi skal utvikle og teste en etterprøvbar scoremodell for byggevalg." | 🟢 | ipn-samledokument §3; state-of-the-art §2 | Korrekt. |
| 25 | "Den skal gjøre komplekse data enklere å bruke, uten å late som om alle data er like sikre." | 🟢 | ipn-samledokument §3 (dokumentasjonstillit-prinsipp); state-of-the-art §6 (synlig usikkerhet) | Korrekt. |
| 26 | "Modellen skal koble produktdokumentasjon, miljødata, levetid, kostnad, risiko og ombruk i ett forklarbart grunnlag." | 🟢 | ipn-samledokument §2 (seks egenskaper); state-of-the-art §2 (seks akser) | Korrekt — matcher de seks dokumenterte dimensjonene. |
| 27 | "Den skal brukes i tilbudsfasen, der mange valg tas før prosjektet er låst." | 🟢 | ipn-samledokument §1 og §2 (akse b: tilbudsfasen) | Korrekt. |
| 28 | "Vi vet at energieffektive boliger har lavere risiko for mislighold av lån — men ingen har vist det samme for byggteknisk kvalitet og holdbarhet." | 🟢 | kildedom og state-of-the-art §7: korrekt beskrivelse av det dokumenterte gapet. Billio/Kaza bekreftet, holdbarhet→PD er hullet. | Korrekt. |
| 29 | "Sammen med Flekkefjord Sparebank skal vi undersøke om bedre dokumentert kvalitet kan gi tryggere lånevilkår." | 🟢 | gronn-plattform.md (Flekkefjord Sparebank: «Bankpilot og kravstiller») | Korrekt. |
| 30 | "VIBS stiller med den digitale plattformen og direkte tilgang til pilotprosjekter og tømrerbedrifter." | 🟢 | gronn-plattform.md (VIBS: prosjekteier/koordinator, plattform) | Korrekt. |
| 31 | "SINTEF AS leder det faglige arbeidet med verifiseringsmodellen." | 🟢 | gronn-plattform.md (SINTEF: FoU-partner, metodikk, effektmåling) | Korrekt. |
| 32 | Konsortiumsliste: VIBS, SINTEF, Ordercontrol/Byggstand, Tirna Fagskole, NorDan, Flekkefjord Sparebank, Farsund kommune, Miljødirektoratet | 🟢 | gronn-plattform.md konsortiumstabell — alle 8 matcher rolle-for-rolle. | Korrekt. |
| 33 | **Nøkkelpersoner: "Bjørn Skeime, Lars Gunnar Stokke, Lars Erik Brekne Johnsen, Christine Reinertsen, Thomas Thorsen"** | ⚪ | gronn-plattform.md (prosjektledelse) lister kun fire: Bjørn Skeime, Lars Gunnar Stokke, Lars Erik Brekne Johnsen, Christine Reinertsen. «Thomas Thorsen» finnes ikke i noen av de ni kildedokumentene som er gjennomgått. Ikke aktivt motsagt, men ikke bekreftet. | Kan ikke verifiseres fra tilgjengelige docs. Enten hallusinert av skriveagent, eller en reell prosjektperson som ikke er registrert i kildedokumentene ennå. Se H1. |
| 34 | **BKA2: "11,7 MNOK fram til 2028, der Vegard Knotten er SINTEFs representant"** | 🟢 | state-of-the-art §9 (linje 160): «Budsjett: 11,7 MNOK, prosjektperiode til 2028. Prosjekteier: Trondheim kommune. SINTEF-representant: Vegard Knotten.» Åpnet: ja [H] | Korrekt. |
| 35 | "planlegger pilotene for 2026 — blant annet med Flekkefjord Sparebank og Farsund kommune" | 🟢 | gronn-plattform.md; kanban §7 narrativ | Korrekt. |
| 36 | "SINTEF starter det formelle arbeidet med primærverifisering... i midten av august 2026" | 🟢 | AGENTS.md (linje 31): «SINTEF: primærverifiserer vitenskapelige kilder mot original. Kommer inn midten av august 2026.» | Korrekt. |
| 37 | NFR-kriteriene (Kvalitet/Effekter/Gjennomføring) nevnes ikke eksplisitt | 🟢 | Kanban (linje 71): «NFR-kriteriene... skal merkes implisitt i innholdet — aldri nevnes eksplisitt.» Sjekket HTML: de nevnes ikke. | Riktig — krav oppfylt. |
| 38 | Statusfarger (🟢🟡🔴) vises ikke på siden | 🟢 | Kanban intro og innholdsprinsipp: «Fargekodene her er INTERNE — vises ikke på siden.» Sjekket HTML: ingen emoji-statuser i synlig tekst. | Riktig — krav oppfylt. |
| 39 | Wiik 2025 (SINTEF Notat 57) brukes ikke | 🟢 | Kildedom: 🔴 «Ubekreftet». Kanban: 🔴 «Ikke funnet i åpne registre; tatt ut.» HTML: Wiik 2025 nevnes ikke. | Riktig utelatt. |
| 40 | Konfliktkostnad 2,2 mrd kr/år brukes ikke | 🟢 | Kildedom: [Harerusten2022] 🔴; [SA2018] ikke lokalisert ⏸. Kanban: 🔴. HTML: tallet nevnes ikke. | Riktig utelatt. |

---

## 2. Handlingsliste

### 🟡 BØR RETTES FØR LANSERING

**H0: Hero «kvalitetssikret av SINTEF» — intern selvmotsigelse**
- Hero-teksten bruker «kvalitetssikret av SINTEF» i presens, som om det er gjennomført.
- Seksjon 7 på nøyaktig samme side sier: «SINTEF starter det formelle arbeidet med primærverifisering... i midten av august 2026» (fremtid).
- En streng leser ser en selvmotsigelse: siden sier at SINTEF-QA er gjort i hero, men at den begynner i august i footer.
- Handling: Formuler hero-linjen fremtidsrettet eller rollebasert, f.eks. «faglig kvalitetssikret av SINTEF» → «med SINTEF som faglig kvalitetssikrer» eller «faglig forankret i SINTEF-samarbeidet». Alternativt: fjern «kvalitetssikret» og behold «bygd på åpen kunnskap».

**H1: Thomas Thorsen — ikke verifisert personnavn**
- Seksjon «Konsortiet» lister fem nøkkelpersoner. «Thomas Thorsen» er ikke nevnt i noen kildedokument (gronn-plattform.md, kildedom, AGENTS.md, state-of-the-art, samledokument, kanban). Kan ikke bekreftes, men heller ikke aktivt avkreftes.
- Handling: Bekreft med Lars Gunnar/Lars Erik om Thomas Thorsen er en reell prosjektperson. Hvis nei — fjern umiddelbart. Hvis ja — legg til i gronn-plattform.md og oppdater kildedom.
- Alternativ: Endre nøkkelpersonlisten til kun de fire dokumenterte navnene.

**H2: "Vi skal teste broen fra data til valg" — nær-variant av frarådet klisjé**
- H2-tittelen i seksjon 5 bruker «broen fra data til valg». Forbudslisten i benchmark-forbilder.md forbyr «gjentatt «bro fra data til beslutning»». Teknisk sett er dette ikke et bokstavelig brudd (vilkåret er «gjentatt», ordet er «valg» ikke «beslutning»), men tonen er nær nok den frarådte klisjeen til å bør omformuleres.
- Handling: Endre seksjonstittelen til noe uten «bro»-metaforen. Forslag: «Vi skal finne det ingen har målt», «Hva VERIFIED skal finne ut», eller kanbanens eget forslag «Hva VERIFIED skal finne ut» (narrativ-arc linje 67).

### 🟡 BØR AVKLARES FØR LANSERING

**H3: Bjørheim 2026 (1 583 konkurser)**
- Kilde er i kanban 🟢-listen, men identiteten til «Bjørheim 2026» er ikke beskrevet noe sted (hvilken organisasjon, rapport, publikasjon?). Det kan ikke etterprøves om dette er primær, bransje, pressenotis eller intern rapport.
- Handling: Legg til kildeidentitet (utgiver, type, URL) i kildedom-tabellen. Alternativt: bytt til en mer etablert konkurskilde (SSB, Brønnøysundregistrene).

**H4: BDO 2025 (3,3 % driftsmargin) og UNION 2025 (18 000 kr/m²)**
- Begge er i kanban 🟢-listen og ipn-samledokument, men ingen av dem er eksplisitt verifisert i kildedom-tabellen (vibs-verified-kildedom-2026-06-27.md). De er behandlet som «etablert grunnlag» uten dokumentert primæråpning.
- Handling: Legg til en linje for begge i kildedom-tabellen med verifiseringsstatus og kildebeskrivelse. Alternativt: aksepter kanbans redaksjonelle dom og dokumenter grunnlaget der.

### ✅ INGEN HANDLING NØDVENDIG

- Wiik 2025 er korrekt ekskludert.
- 2,2 mrd konfliktkostnad er korrekt ekskludert.
- «Forskning indikerer» er korrekt brukt for Gullbrekken & Holme 2025-påstanden.
- 32 %-kilden er korrekt attribuert til boliglån (Kaza/Billio), ikke til An & Pivo 2020 (næringsbygg).
- NFR-kriteriene er korrekt utelatt fra synlig tekst.
- Statusfarger lekker ikke til offentlig side.
- BKA2 / 11,7 MNOK / Vegard Knotten: fullt dokumentert.
- Konsortiumslisten (8 partnere): stemmer mot gronn-plattform.md.
- Timing for SINTEF (midten av august 2026): stemmer mot AGENTS.md.

---

## 3. Konklusjon

Siden er gjennomgående solid og følger kilde- og sannhetsreglene i AGENTS.md. De store risikokildene (Wiik 2025, 2,2 mrd) er korrekt ekskludert, statusfarger lekker ikke, og det mest sensitive faktakortet (32 % mislighold) er korrekt attribuert til de riktige boliglånsstudiene.

**Ingen aktive 🔴-funn.** Alle tre handlingspunktene er 🟡 eller ⚪ — ingen påstander er aktivt motbevist av kildedokumentene.

**Fire 🟡/⚪-funn som bør rettes før lansering:**

1. **H0 (🟡):** Hero-linjen «kvalitetssikret av SINTEF» er internt selvmotsigende: seksjon 7 på samme side sier SINTEF-primærverifisering begynner midten av august 2026. Formuler som fremtids- eller rollemarkering, ikke som avsluttet QA-prosess.

2. **H1 (⚪):** «Thomas Thorsen» er ikke bekreftet i noe kildedokument. Enten hallusinert av skriveagent, eller en reell prosjektperson som mangler i kildesystemet. Bekreft med konsortiet.

3. **H2 (🟡):** «Vi skal teste broen fra data til valg» er en nær-variant av den frarådte «bro»-metaforen. Ikke et teknisk forbudsbrudd («gjentatt» er vilkåret), men bør omformuleres for å unngå klisjétonen. Kanbans «Hva VERIFIED skal finne ut» er et ferdig alternativ.

4. **H3/H4 (🟡):** Bjørheim 2026, BDO 2025 og UNION 2025 er i kanbans 🟢-liste men mangler eksplisitt primærverifikasjon i kildedom-tabellen. Redaksjonelt godkjent, men bør dokumenteres før SINTEF-gjennomgang i august 2026.
