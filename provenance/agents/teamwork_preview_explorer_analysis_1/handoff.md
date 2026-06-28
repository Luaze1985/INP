# Handoff Report — Guardrails Compliance Analysis for IPN Documents

This report documents the findings from the review of `docs/reference/ipn-samledokument.md` and `docs/reference/ipn-hovedokument.md` against `docs/reference/claude-guardrails.md`.

---

## 1. Observation

1. **Product Status Guardrail Rule**:
   - `docs/reference/claude-guardrails.md` lines 92-95:
     ```markdown
     92: **Produktstatus**
     93: 
     94: Aldri beskrive MVP som ferdig. Aldri si at VIBS «leverer» noe som er under bygging. Bruk «er designet for», «vil levere», «er under utvikling».
     ```
   - `docs/reference/claude-guardrails.md` lines 51-54:
     ```markdown
     51: ### 🔨 Under aktiv bygging
     52: 
     53: - MVP-plattformen (Axon er leverandør)
     ```

2. **Observed Product Status Violations**:
   - `docs/reference/ipn-samledokument.md` line 10:
     ```markdown
     10: **Hva VIBS er.** VIBS er en plattform for små og mellomstore byggebedrifter som samler prosjektstyring, dokumentasjon, kommunikasjon og kvalitet på ett sted — uten tunge systemer og dyre abonnement. VERIFIED er forskningsdelen: en modell som gir hvert produkt- og løsningsvalg en etterprøvbar score...
     ```
   - `docs/reference/ipn-samledokument.md` line 14:
     ```markdown
     14: ...VERIFIED flytter beslutningsgrunnlaget dit, og gjør bærekraft til en konsekvens...
     ```
   - `docs/reference/ipn-samledokument.md` line 28:
     ```markdown
     28: VERIFIED adresserer ikke mangel på data, men mangelen på en bro fra data til beslutning — et grunnlag en SMB-entreprenør eller boligkjøper kan bruke...
     ```
   - `docs/reference/ipn-samledokument.md` line 65:
     ```markdown
     65: VERIFIED gjør et produktvalg om til en sammenliknbar score. Forenklet: hver dimensjon gis 0–100 poeng...
     ```
   - `docs/reference/ipn-samledokument.md` lines 135-139 (Table Claims):
     ```markdown
     135: | VIBS reduserer CO₂ fra materialvalg | ... |
     136: | VIBS reduserer byggfeil og omarbeid | ... |
     137: | VIBS hjelper SMB med bærekraft | ... |
     138: | VIBS gir bedre grønn bankdokumentasjon | ... |
     139: | VIBS bidrar til do-not-harm | ... |
     ```

3. **Bank and Finance Guardrail Rule**:
   - `docs/reference/claude-guardrails.md` lines 72-74:
     ```markdown
     72: **Banker og finansiering**
     73: 
     74: Aldri hevde at banker allerede bruker VIBS eller at grønn rente er bekreftet og implementert. Aldri oppgi konkrete rentebesparelser som fakta – 0,15–0,40 % er estimat basert på EBA-rammeverk, ikke signert avtale.
     ```
   - *Observed compliance*: Target documents do not state bank integration is implemented or specify exact savings as facts. They refer to it as a research gap or a possibility:
     - `ipn-samledokument.md` line 96: *"På sikt kan god dokumentasjon også gi billigere lån og forsikring."*
     - `ipn-samledokument.md` line 102: *"At energieffektivitet henger sammen med lavere risiko for boliglånsmislighold er empirisk bekreftet... Men ingen studie kobler holdbarhet og byggteknisk kvalitet til misligholdsrisiko — det er et dokumentert forskningshull..."*

4. **Industry Figures Guardrail Rule**:
   - `docs/reference/claude-guardrails.md` lines 76-78:
     ```markdown
     76: **Markedsandeler og tall**
     77: 
     78: Aldri presentere «5 % av SMB-markedet innen 2030» som et tall – det er et mål. Aldri oppgi konfliktmerkostnad (2,2 mrd), byggefeilkostnad (10–30 mrd) eller andre bransjetall uten kildehenvisning.
     ```
   - *Observed compliance*:
     - `ipn-samledokument.md` line 12: *"Utbedring av byggfeil koster anslagsvis 10–30 milliarder kroner i året (Gullbrekken og Holme 2025)."*
     - `ipn-samledokument.md` line 24: *"driftsmargin var 3,3 % i 2024 (BDO 2025; Kommunal- og distriktsdepartementet mfl. 2024). 2025 ga 1 583 konkurser i næringen (Bjørheim 2026). I tillegg koster konflikter rundt 2,2 milliarder kroner i året (Samfunnsøkonomisk analyse 2018), og norske krav gjør det anslagsvis 18 000 kr/m² dyrere å bygge enn i Sverige (UNION 2025)."*
     - `ipn-hovedokument.md` line 23: *"Byggfeil koster 10–30 mrd NOK/år... [GullbrekkenHolme2025] 🟡"*
     - `ipn-hovedokument.md` line 24: *"Konfliktkostnad 2,2 mrd NOK/år. [SA2018] 🟢"*

5. **AI Buzzwords Rule**:
   - Search for: `ai, kunstig, agent, maskin, algoritme, llm, gpt, neural, deep`.
   - *Observed compliance*: 0 matches in either target document.

6. **Complex Sentences and Jargon**:
   - `ipn-samledokument.md` line 36 contains a single sentence of 60 words: *"Hver enkelt byggekloss finnes allerede og er faglig moden: standardene for livsløpsvurdering..."*
   - Heavy compound words like `prosjekteringsfasen`, `beslutningsgrunnlaget`, and `dokumentasjonstillit` are used.
   - Jargon words such as `digitaliserte`, `fragmenterte`, `siloer`, `syntesen`, `robusthet`, `operasjonalisert` are present.

---

## 2. Logic Chain

1. **Premise**: `claude-guardrails.md` sets clear requirements for styling, clarity, and factual accuracy.
2. **Step 1 (Product Status)**: Guardrails state that unbuilt features (like the platform and score model) must not be presented as finished or currently delivering results. However, `ipn-samledokument.md` uses present tense verbs like *"samler"*, *"flytter"*, *"gjør"*, and *"reduserer"* to describe these functionalities. Therefore, these occurrences constitute a direct violation of the product status guardrail.
3. **Step 2 (Factual Citations)**: Guardrails require that industry figures (such as 10-30 billion NOK construction defects or 2.2 billion NOK conflicts) have citations. The target documents cite Gullbrekken and Holme (2025) and Samfunnsøkonomisk analyse (2018) for these figures. Therefore, they are in compliance.
4. **Step 3 (Partners)**: Guardrails require partner status to be presented accurately (e.g. NorDan lacks signed LoI; Tirna Fagskole is a fagskole). The target documents do not mention these partners. Thus, no partner violations occur.
5. **Step 4 (AI Buzzwords)**: The guardrails discourage AI buzzwords. None were found, showing compliance.
6. **Step 5 (Readability)**: The guardrails promote clarity. The presence of 60-word sentences and complex Norwegian compound words represents a deviation from the clarity standard, requiring sentence-splitting and jargon reduction.

---

## 3. Caveats

- This review was strictly limited to `ipn-samledokument.md` and `ipn-hovedokument.md`. Other reference files in the workspace (such as drafts or sustainability sheets) were not checked.
- Partner and banking statuses were checked against the guidelines in `claude-guardrails.md` dated March 13, 2026. If agreements have been finalized or updated since that date, the check will need revision.

---

## 4. Conclusion

The target documents are highly compliant with financial, partner, and citation guardrails, but violate the product status guardrail by describing the platform and score model in present tense as if they are already completed. In addition, there are several instances of heavy jargon and overly complex sentence structures. Rewriting these specific sections using the provided drafts in `analysis.md` will bring the documents into full compliance.

---

## 5. Verification Method

- Open `analysis.md` in the working directory:
  `C:\Users\larse\Documents\Interne prosjekter\Vibs\vibs-boligpass\.agents\teamwork_preview_explorer_analysis_1\analysis.md`
- Inspect the "Before" vs "After" examples for product status violations and complex sentences.
- Check them against the corresponding lines in the target files (`ipn-samledokument.md` and `ipn-hovedokument.md`) to verify that the proposed changes address the issues accurately.
- No software test suite is applicable as this is a qualitative document review.
