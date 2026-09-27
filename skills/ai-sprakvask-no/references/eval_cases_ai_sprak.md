# Eval cases - AI-språk-agenter NO

## Eval 1: Generisk KI-tekst

**Input:**  
I dagens komplekse og stadig skiftende samfunn er det viktig å merke seg at helhetlige tilnærminger kan bidra til å optimalisere arbeidsprosesser og skape robuste løsninger for fremtiden.

**Expected:**
- Flagges som høyt KI-preg.
- Omskrives til konkret norsk.
- Skal spørre: Hvilke arbeidsprosesser? Hvem gjør hva? Hva er problemet?

## Eval 2: Kommunal tekst til ansatte

**Input:**  
Det legges til rette for at enhetene kan gjennomføre nødvendige prosesser knyttet til oppfølging av avvik i tråd med gjeldende rutiner.

**Expected:**
- Aktør skal fram: leder/enhet/HMS-rådgiver.
- Verb skal fram: følge opp, registrere, lukke, melde.
- Ikke fjern krav om gjeldende rutiner.

## Eval 3: Nynorsk med bokmålsinnslag

**Input:**  
Kommunen ønskjer å begynne med ein meir helhetlig praksis der einhetene får bedre støtte.

**Expected:**
- Flagge bokmålsord/normblanding.
- Foreslå nynorsk versjon.
- Ikke påstå at meningen er feil.

## Eval 4: Påstand uten kilde

**Input:**  
Forskning viser at KI alltid gir bedre tekster og øker tilliten hos leseren.

**Expected:**
- Påstand må kildekontrolleres.
- "Alltid" skal flagges som for sterkt.
- Ingen kilde skal diktes opp.

## Eval 5: Personlig tekst som er blitt for glatt

**Input:**  
Original: Jeg tror dette kan funke, men bare hvis folk faktisk tør å vise fram det de lager, også når det er litt halvferdig.

KI-versjon: Dette initiativet kan bidra til økt delingskultur gjennom trygg eksponering av uferdige prosesser i et lærende fellesskap.

**Expected:**
- KI-versjonen skal flagges som overpolert.
- Ny versjon bør ligge nær originalens energi.
- Ordene "funke", "tør", "halvferdig" kan beholdes hvis sjangeren tillater det.


## Eval 6: Søknadstekst med oppramsing og logisk trapp

**Input:**  
I et tilbud i bygg er prisen lett å sammenligne. Levetid, vedlikehold, klima og dokumentasjon er vanskeligere, fordi opplysningene er ulikt sikre. Da er det lett at bare prisen blir sammenlignet, og at reparasjon, rehabilitering og ombruk taper fordi de er dårligst dokumentert. Relevante forhold knyttet til kjemikalier, sosiale forhold, transport, ansvar og faktisk materialbesparelse skal avgrenses.

**Expected:**
- Flagg oppramsinger med 3–5 ledd, og kutt til de ett til to leddene som bærer poenget.
- Flagg trappen situasjon → «Da …» → konsekvens, og start med poenget.
- Behold fakta og forbehold. Ikke legg til nye påstander.
- Resultatet skal høres ut som en fagperson som forklarer noe til en kollega.
