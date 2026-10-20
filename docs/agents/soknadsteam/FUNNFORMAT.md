# Funnformat og beslutningsport

Hver fil .scratch/soknadsteam/<run-id>/findings/<role>.json skal inneholde:

    {
      "role": "research",
      "status": "COMPLETED",
      "limitations": "Kun søknadsutkast og oppgitte repo-filer undersøkt.",
      "findings": [
        {
          "id": "IPN-RESEARCH-001",
          "priority": "P1",
          "surface": "IPN",
          "location": "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v2.0.md",
          "problem": "Akseptgrense for holdout er ikke forhåndsfastsatt.",
          "proposal": "Legg inn et forhåndsregistrert måleark med ...",
          "acceptance_test": "Terskel og beregningsregel er godkjent før holdout åpnes.",
          "owner": "Prosjektansvarlig + FoU-leverandør",
          "confidence": "MEDIUM",
          "requires_human": true,
          "evidence": [
            {
              "source": "docs/reference/prosjektbeskrivelse/reviews/2026-09-27-finpuss-v2.0.md",
              "status": "INTERNAL",
              "note": "Åpent punkt dokumentert i review."
            }
          ]
        }
      ]
    }

Verdier: priority P0/P1/P2; surface IPN/KOBLINGSBOKS/BOTH; confidence HIGH/MEDIUM/LOW; evidence.status PRIMARY_VERIFIED/INTERNAL/UNVERIFIED. Et internt review er aldri automatisk en ekstern primærkilde. Bare faktisk åpnet original kan gis PRIMARY_VERIFIED, med kilde og dato dokumentert i notat. Skriptet validerer JSON-struktur og at lokale kildefiler eksisterer, IKKE sannheten i påstandene.

P0 = stopper godkjenning/innsending eller kan skape vesentlig feil. P1 = svekker vurderingskriterium eller etterprøvbarhet. P2 = forbedring uten beslutningskritisk effekt.

Beslutningsprotokoll per funn: ACCEPT / MODIFY / REJECT / DEFER, med eier, dato, begrunnelse og lenke til ny commit/PR. Et «ACCEPT» er ikke en kildeverifisering og endrer ikke automatisk aktiv tekst.

En gyldig strukturell QA er nødvendig, men ikke tilstrekkelig: mennesket må også godkjenne metode, kildestatus, budsjett og eventuelle eksterne tiltak.
