# Faktasjekk — VERIFIED-nettsiden mot søknadskandidat v0.9

**Dato:** 2026-08-07
**Kontrollert av:** Claude Code (automatisk, ikke primærverifisert)
**Kontrollert mot:** `docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.9.md`
**Erstatter:** `faktasjekk-2026-06-29.md` som gjeldende faktasjekk.

## Regel som er brukt

Siden skal ikke si mer enn v0.9 sier. Hver synlig påstand er sporet til et kapittel i v0.9.
Der v0.9 tar forbehold, skal siden ta samme forbehold.

## Domstabell

| Nr | Påstand på siden | Dekning i v0.9 | Status |
|---|---|---|---|
| 1 | «VERIFIED er et forskningsprosjekt om løsningsvalg i byggeprosjekter. Vi utvikler og tester en måte å sammenligne alternative løsninger på — og å vise hvor sikkert grunnlaget faktisk er.» | Sammendrag, avsn. 1–2 | ✅ dekket |
| 2 | Badge «IPN-forskningsprosjekt» | Utlysningsformalia; `[NFR_IPN2026]` 🟢 | ✅ dekket |
| 3 | «mange av de viktigste løsningsvalgene tas i tilbudsfasen» | K1 → Tilbudsfasen | ✅ dekket |
| 4 | «Informasjonen ligger spredt, i ulike formater, og må ofte settes sammen for hånd» | K1 → Spredt informasjon | ✅ dekket |
| 5 | «den billigste løsningen kan framstå som best, selv om den koster mer over tid» | K1 → Sammenligningsbehovet, siste avsn. | ✅ dekket (nesten ordrett) |
| 6 | **68 359 bedrifter** per 1. januar 2026 | K1 → Ressurser i små bedrifter [1] | ✅ dekket · `[SSB2026]` 🟢 |
| 7 | **91,2 %** færre enn ti ansatte | K1 [1] | ✅ dekket · `[SSB2026]` 🟢 |
| 8 | **76,2 %** mellom én og ni ansatte | K1 [1] | ✅ dekket · `[SSB2026]` 🟢 |
| 9 | Forbehold: «Tallene gjelder hele bygge- og anleggsnæringen, ikke bare gruppen VERIFIED retter seg mot» | K1, siste setning i samme avsnitt | ✅ dekket — forbeholdet er v0.9s eget og er gjengitt synlig |
| 10 | «Mindre entreprenørbedrifter har ofte høy fagkompetanse … kapasiteten er bundet i produksjon» | K1, avsn. 2 under samme overskrift | ✅ dekket |
| 11 | «internasjonale standarder for livsløpsvurdering og livsløpskostnader, og en norsk standard for klimagassberegninger» | K2 → Standarder og metoder [2-4] | ✅ dekket |
| 12 | «Flerkriterieanalyse er en etablert måte å behandle beslutninger med flere hensyn» | K2 [5] (Munda) | ✅ dekket |
| 13 | «Norske løsninger kobler kalkyle, pris, materialmengder, produktdata og miljødeklarasjoner …» | K2 → Eksisterende løsninger [6-7] | ✅ dekket. Verktøyene er ikke navngitt på siden — v0.9 navngir dem, så siden sier mindre, ikke mer |
| 14 | «noen viser usikkerheten i materialenes klimatall» | K2 [9] (EC3) | ✅ dekket |
| 15 | **«har vi likevel ikke funnet én løsning som gir små norske entreprenører et samlet og etterprøvbart beslutningsgrunnlag i tilbudsfasen»** | K2, avsn. som starter «Flere av funksjonene…» | ✅ dekket — ordrett gjengitt |
| 16 | Forbehold: «Dette er en avgrenset gjennomgang. Den må oppdateres når underlaget utvides.» | K2, samme avsnitt | ✅ dekket — v0.9s eget forbehold, synlig på siden |
| 17 | De fem åpne spørsmålene i seksjon 4 | K2 → tabellen «Forskningshullet», rad 1, 3, 4, 5, 6 | ✅ dekket — omskrevet til dagligspråk, ingen påstand lagt til |
| 18 | Hovedmål og de fire delmålene (seksjon 5) | K3 → Hovedmål + Delmål | ✅ dekket |
| 19 | «Vi skal teste om den blir forstått, hvordan den brukes, og om den endrer eller bekrefter valget» | K3 → FoU-bidraget; F4 | ✅ dekket |
| 20 | «Forskning på nederlandske boliglånsdata finner en sammenheng mellom energieffektivitet og lavere sannsynlighet for mislighold» | V3 → Kunnskapsgrunnlag [10] | ✅ dekket · `[Billio2022]` 🟢. **Ingen prosentsats** — i tråd med v0.9 |
| 21 | «Den samme sammenhengen er ikke vist for byggteknisk kvalitet, levetid eller vedlikeholdsdata» | V3, samme avsnitt | ✅ dekket — v0.9s eksplisitte avgrensning |
| 22 | «En avgrenset pilot skal undersøke … Banken må selv definere behovet på forhånd» | V3 → Avgrenset bankpilot | ✅ dekket. **Ingen bank er navngitt** |
| 23 | «Prosjektet forutsetter ikke at informasjonen forbedrer risikovurderingen» | V3 → Kunnskapsgrunnlag, siste setning | ✅ dekket — ordrett |
| 24 | Dokumentasjonsstatus per opplysning (seksjon 6) | K4 → Datagrunnlag og dokumentasjonstillit | ✅ dekket |
| 25 | «Et minste informasjonsgrunnlag» | K4 → Minste informasjonsgrunnlag | ✅ dekket |
| 26 | «Teknisk egnethet er en faglig port» + eksempelet med fuktrobusthet | K4 → Minste informasjonsgrunnlag; V2, avsn. 1 | ✅ dekket |
| 27 | Skillet måler / beregner / estimerer / faglig vurderer / undersøker | K4 → Pilotering og begrepsbruk | ✅ dekket |
| 28 | «Selve beslutningen og ansvaret ligger fortsatt hos entreprenør og kunde. Modellen velger ikke.» | K2, siste avsnitt | ✅ dekket. Andre setning er sidens egen presisering — den *innskrenker*, den utvider ikke |
| 29 | «forskningspartneren» (seksjon 6) | K4 → Forskningsløype | ✅ dekket — v0.9s egen formulering, ingen navngitt partner |
| 30 | Hele statuslisten i seksjon 7 | v0.9 → «Åpent / mangler» + «Gjennomføring, arbeidspakker, budsjett og organisering» | ✅ dekket |
| 31 | «Søknadsteksten foreligger som en revidert arbeidskandidat. Den er ikke innsendingsklar.» | v0.9 statuslinje | ✅ dekket — ordrett |
| 32 | Sidemeny: «Revidert arbeidskandidat — ikke innsendingsklar» | Samme | ✅ dekket |
| 33 | Sidemeny: målgruppe «Små og mellomstore entreprenørbedrifter og deres kunder» | K3 → Hovedmål | ✅ dekket |

**Ingen påstand på siden går ut over v0.9.** To formuleringer (nr. 28 og 13) sier mindre enn v0.9.

## Fjernet siden forrige faktasjekk

Disse sto live fram til 2026-08-07 og er nå ute. Ingen av dem finnes i v0.9.

| Påstand | Hvorfor ute |
|---|---|
| «~32 % lavere risiko for mislighold» (Kaza 2014; Billio 2022) | v0.9 oppgir ingen prosentsats og sier eksplisitt at prosjektet ikke gjør det før originalanalysen er kontrollert |
| Vannskader 5,1 mrd / ~10 per time (Finans Norge 2023) | Ikke i v0.9 |
| 18 000 kr/m² dyrere enn Sverige (UNION 2025) | Ikke i v0.9. Var 🟡 i faktasjekken 2026-06-29 — publisert uten forbehold |
| Driftsmargin 3,3 % (BDO 2025) | Ikke i v0.9. Samme situasjon som over |
| 1 583 konkurser (Bjørheim 2026) | Ikke i v0.9. Kilden «Bjørheim» var aldri beskrevet i noe kildedokument |
| «minst halvparten av boliger har minst én byggefeil, 10–30 mrd/år» (Gullbrekken & Holme 2025) | Ikke i v0.9 |
| Konsortiumslisten: VIBS, SINTEF, Ordercontrol/Byggstand, Tirna Fagskole, NorDan, Flekkefjord Sparebank, Farsund kommune, Miljødirektoratet | v0.9 navngir ingen partnere. Konsortiet er ikke bekreftet |
| Nøkkelpersoner: Bjørn Skeime, Lars Gunnar Stokke, Lars Erik Brekne Johnsen, Christine Reinertsen, Thomas Thorsen | Ingen personnavn i v0.9. **«Thomas Thorsen» var flagget ⚪ (ikke verifiserbar) allerede 2026-06-29 og sto likevel live til nå** |
| «SINTEF AS leder det faglige arbeidet med verifiseringsmodellen» | Ikke i v0.9 |
| «kvalitetssikret av SINTEF» / «under kvalitetssikring av SINTEF fra august 2026» | Ikke i v0.9. Var også flagget som intern selvmotsigelse (H0) i faktasjekken 2026-06-29 |
| BKA2, 11,7 MNOK til 2028, Vegard Knotten | Ikke i v0.9 |
| «Sammen med Flekkefjord Sparebank skal vi undersøke…» | v0.9: «En avgrenset pilot kan undersøke…», ingen bank navngitt |
| Partnerstripe «Et forskningssamarbeid mellom VIBS • SINTEF» | Samme grunn |
| Bunnbilde fra Listers kapitaldag med fire navngitte personer | Navn ute av teksten; bildet navnga de samme fire i bildetekst, alt-tekst og OG-bilde |
| «Metodikk: Systematisk sammenligning av egenskaper og atferdsstudier» | Erstattet av v0.9s egen beskrivelse |

## Merknad om bildene

Bakgrunnsbildene er byttet fra Unsplash-stock (betong, tårnkraner, glassfasade-høyhus) til fem norske
trehus-/småhusbilder. **Rettighetsstatus for de nye bildene er ikke dokumentert** — se
`site/arbeid/bilder-kilder.md`. Dette er en kjent og akseptert risiko etter Lars' beslutning 2026-08-07, ikke en
forglemmelse.

## Hva denne faktasjekken ikke gjør

Den kontrollerer at siden er dekket av v0.9. Den kontrollerer **ikke** at v0.9 selv er
primærverifisert. Fire av v0.9s femten referanser er NTNU-masteroppgaver som ligger åpent i NTNU
Open og bør kunne løftes til 🟢 ved åpning — de står 🟡 i kildebiblioteket nå.
