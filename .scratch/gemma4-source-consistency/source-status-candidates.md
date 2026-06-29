Oppgave: Vurder om kandidatene under viser kildestatus- eller kildekonsistensdrift i repoet.
Les kun radene under. Ikke finn pa fakta. Returner JSON med ok, flagged_rows, reason, recommended_action.

Regler fra repo:
- Bare apen, uavhengig sitering teller.
- Gronn kan baere en soknadssetning alene.
- Gul ma apnes/fraseres med forbehold.
- Pause betyr tatt ut av soknadstekst, parkert med gjeninnsettingsvilkar.

Kandidatsett:

1. SA2018 statusdrift
- CONTEXT.md: SA2018/2,2 mrd er fjernet fra prosa, parkert pause fordi rapport ikke er lokalisert.
- ipn-kildebibliotek.md: SA2018 er gul + pause; "nei (ma lokaliseres/apnes)".
- ipn-hovedokument.md: SA2018 er pause, tatt ut av soknadstekst, gjeninnsett naar rapporten er funnet/apnet.
- ipn-samledokument.md: Samfunnsokonomisk analyse 2018 og 2,2 mrd er tatt ut fordi rapporten ikke er lokalisert.
- vibs-verified-kildedom-2026-06-27.md: SA2018 er markert gronn/bekreftet og tiltak sier erstatt Harerusten med SA2018 gronn.

2. Wiik2025 statusdrift
- CONTEXT.md: Wiik2025 er fjernet fra prosa, parkert pause fordi SINTEF Notat 57 ikke er funnet.
- ipn-kildebibliotek.md: Wiik2025 er gul + pause; konsortie-internt/uindeksert, ikke baerende alene.
- ipn-hovedokument.md: Wiik2025 er pause og tatt ut av soknadstekst; 20 prosent hviler paa EBA_NO2023 + KD2024.
- ipn-prosjektbeskrivelse-utkast.md: Wiik 2025 er tatt ut; 20 prosent hviler paa EBA Norge 2023 og KDD 2024.
- vibs-verified-kildedom-2026-06-27.md: Wiik2025 er rod/ubekreftet og bor ikke brukes som uavhengig primaerbevis.

3. Mecca2023 statusdrift
- CONTEXT.md: Mecca2023 venter pa primaer/fulltekst; Wiley betalingsmur.
- ipn-kildebibliotek.md: Mecca2023 er gul; "nei (Wiley 402)".
- ipn-hovedokument.md: Mecca2023 er gul og brukes sammen med Lohman2023 gronn.
- ipn-prosjektbeskrivelse-utkast.md: Mecca 2023 er gul; metodefordeling bekreftet via sekundarspor, Wiley-fulltekst ikke apnet.
- vibs-verified-kildedom-2026-06-27.md: Mecca2023 er markert gronn/bekreftet, men sier samtidig Wiley betalingsmur.

4. EBA_NO2023 og KD2024 status
- CONTEXT.md: 20 prosent hviler paa EBA_NO2023 + KD2024.
- ipn-kildebibliotek.md: EBA_NO2023 er gul, sekundar via bestillingsverk; KD2024 er gul, sekundar via bestillingsverk.
- ipn-hovedokument.md: innsendingssetning om 20 prosent bruker EBA_NO2023 + KD2024, men bevislaget markeres gul og setningen fraseres som "kan redusere".
- ipn-prosjektbeskrivelse-utkast.md: kildestatus sier belegget enna er gul og ma primaerhentes.
- vibs-verified-kildedom-2026-06-27.md: EBA_NO2023 er markert gronn/bekreftet.

5. Finansbro An/Billio/Kaza
- ipn-kildebibliotek.md: Billio2022 og Kaza2014 er gronne; An2020 er gul og gjelder kommersiell CMBS/naringsbygg, ikke boliglansbelegg alene.
- ipn-hovedokument.md: finansbroen bruker Billio2022 gronn + Kaza2014 gronn, og "stottet for naringsbygg av An2020" gul.
- ipn-samledokument.md: samme skille: Billio/Kaza boliglansstudier, An & Pivo kommersiell eiendom/CMBS.
- vibs-verified-kildedom-2026-06-27.md: forklarer at An2020 ikke skal brukes for boliger og at Kaza2014 er residensiell.

6. Utdaterte gamle nokler
- rg i canonical docs viser ingen An2021 eller Billio_SAFE261 utenom historiske rettingsnotater i kildedommen.
- brukt-men-ikke-definert i de tre kanoniske docs gir bare vanlige markdown-lenketekster: "kildebiblioteket" og "nokkel".
