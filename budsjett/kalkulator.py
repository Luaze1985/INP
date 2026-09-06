"""Enkel, deterministisk IF-kalkyle for VERIFIED.

Denne modellen gjelder bare AP1-AP3. Leverandørkjøp er samlet under Vi Bygger
Sammen AS og skal ikke føres som ekstra kostnadsbærere eller egenfinansiering.
Alle beløp er hele NOK.
"""

PROJECT_TOTAL_NOK = 16_000_000
PROJECT_TYPE = "IF"
SUPPORT_RATE_PERCENT = 50
DURATION_MONTHS = 36
ALLOCATION_STATUS = "VIBS-kvalifisert forslag; ikke avtalt i møte eller bekreftet av aktørene"

WORK_PACKAGES = (
    {"id": "AP1", "title": "Forskningsprotokoll og datakvalitet", "budget_nok": 3_000_000, "type": "IF"},
    {"id": "AP2", "title": "Målemodell og harmonisering", "budget_nok": 5_500_000, "type": "IF"},
    {"id": "AP3", "title": "Usikkerhetsmodell og modellfrys", "budget_nok": 7_500_000, "type": "IF"},
)

# Dette er de eneste aktørene som bærer prosjektkostnad og egenfinansiering.
COST_CARRIERS = (
    {"id": "vibs", "name": "Vi Bygger Sammen AS", "role": "Prosjektansvarlig", "total_cost_nok": 12_600_000, "support_rate_percent": 50},
    {"id": "d_takst", "name": "D Takst AS", "role": "Kandidat samarbeidspartner", "total_cost_nok": 1_500_000, "support_rate_percent": 50},
    {"id": "espeland", "name": "Byggmester Espeland AS", "role": "Kandidat samarbeidspartner", "total_cost_nok": 300_000, "support_rate_percent": 50},
    {"id": "norgesbygg_sor", "name": "Norgesbygg Sør AS", "role": "Kandidat samarbeidspartner", "total_cost_nok": 300_000, "support_rate_percent": 50},
    {"id": "norsk_byggtjeneste", "name": "Norsk Byggtjeneste AS", "role": "Kandidat samarbeidspartner", "total_cost_nok": 1_300_000, "support_rate_percent": 50},
)

LOCKED_COST_CARRIER_IDS = (
    "vibs",
    "d_takst",
    "espeland",
    "norgesbygg_sor",
    "norsk_byggtjeneste",
)

# Samme kostnadsbærere som over, fordelt på AP1-AP3. Alle beløp er hele NOK.
ACTOR_AP_MATRIX = {
    "vibs": {"AP1": 2_600_000, "AP2": 4_300_000, "AP3": 5_700_000},
    "d_takst": {"AP1": 100_000, "AP2": 600_000, "AP3": 800_000},
    "espeland": {"AP1": 0, "AP2": 100_000, "AP3": 200_000},
    "norgesbygg_sor": {"AP1": 0, "AP2": 100_000, "AP3": 200_000},
    "norsk_byggtjeneste": {"AP1": 300_000, "AP2": 400_000, "AP3": 600_000},
}

# VIBS-raden er en fast budsjettramme, men underfordelingen er ikke priset.
# Beløp skal først settes når dokumentasjonsporten for posten er lukket. Dette
# hindrer at historiske anslag blir behandlet som tilbud eller bemanningsplan.
VIBS_COST_ITEMS = (
    {
        "id": "own_personnel_indirect",
        "name": "Egne personal- og indirekte kostnader",
        "cost_type": "personal_og_indirekte",
        "amount_nok": None,
        "decision_status": "open",
        "evidence_reference": None,
        "supplier": None,
        "required_evidence": "Navngitte personer, årslønn, beregnet timesats, timer per person/AP og kapasitet",
    },
    {
        "id": "sintef_rnd_purchase",
        "name": "Innkjøpt FoU fra SINTEF",
        "cost_type": "innkjop_av_fou",
        "amount_nok": None,
        "decision_status": "open",
        "evidence_reference": None,
        "supplier": "SINTEF (juridisk enhet uavklart)",
        "required_evidence": "Signert eller datert tilbud med juridisk enhet, markedspris, timer, leveranser per AP og rettigheter",
    },
    {
        "id": "axon_subcontract",
        "name": "Teknisk underleveranse fra Axon",
        "cost_type": "andre_prosjektkostnader",
        "amount_nok": None,
        "decision_status": "open",
        "evidence_reference": None,
        "supplier": "Axon (juridisk enhet uavklart)",
        "required_evidence": "Avgrenset tilbud med juridisk enhet, pris, timer, leveransested, IP/dataansvar og skille mot VIBS-produkt",
    },
    {
        "id": "advisory_services",
        "name": "Eventuelle rådgiver-/spesialisttjenester",
        "cost_type": "andre_prosjektkostnader",
        "amount_nok": None,
        "decision_status": "open",
        "evidence_reference": None,
        "supplier": None,
        "required_evidence": "Valgt juridisk leverandør, nødvendig IF-oppgave, tilbud og skille mot søknadsrådgivning/markedsføring",
    },
    {
        "id": "test_services",
        "name": "Eventuelle test-/spesialistleveranser",
        "cost_type": "andre_prosjektkostnader",
        "amount_nok": None,
        "decision_status": "open",
        "evidence_reference": None,
        "supplier": None,
        "required_evidence": "Valgt juridisk leverandør, testprotokoll, tilbud, data-/IP-vilkår og støtteberettigelse",
    },
)

VIBS_DECISION_GATES = (
    "Egne timer og satser er dokumentert per person og AP uten kapasitetskonflikt",
    "SINTEF-tilbudet dokumenterer markedspris og selvstendig FoU-leveranse",
    "Axon-tilbudet avgrenser VERIFIED-FoU fra eksisterende og ordinær produktutvikling",
    "Eventuelle rådgiver- og testkjøp er nødvendige IF-kostnader og har valgt juridisk motpart",
    "Alle leverandørbeløp er ført én gang under VIBS og summerer med egne kostnader til 12,6 MNOK",
    "Likviditetsplanen dekker dokumentert betalingsprofil og utbetalingstidspunkt uten udokumentert reserveanslag",
    "Hver partnerrad er vurdert mot nødvendig oppgave og dokumentert kompetanse; møtereferatet brukes bare som indikativt kontrollspor",
)


def fmt_nok(amount: int) -> str:
    return f"{amount:,}".replace(",", " ")


def fmt_mnok(amount: int) -> str:
    return f"{amount / 1_000_000:.1f}".replace(".", ",")


def support_nok(carrier: dict) -> int:
    return carrier["total_cost_nok"] * carrier["support_rate_percent"] // 100


def own_financing_nok(carrier: dict) -> int:
    return carrier["total_cost_nok"] - support_nok(carrier)


def carrier_by_id() -> dict[str, dict]:
    return {carrier["id"]: carrier for carrier in COST_CARRIERS}


def work_package_by_id() -> dict[str, dict]:
    return {work_package["id"]: work_package for work_package in WORK_PACKAGES}


def vibs_cost_status() -> dict[str, int | bool]:
    priced = [item for item in VIBS_COST_ITEMS if item["amount_nok"] is not None]
    priced_total = sum(item["amount_nok"] for item in priced)
    return {
        "priced_total_nok": priced_total,
        "unallocated_nok": carrier_by_id()["vibs"]["total_cost_nok"] - priced_total,
        "unpriced_items": len(VIBS_COST_ITEMS) - len(priced),
        "complete": len(priced) == len(VIBS_COST_ITEMS),
    }


def run_analysis() -> None:
    total_support = sum(support_nok(carrier) for carrier in COST_CARRIERS)

    print("VERIFIED — IF-only budsjett")
    print(f"Prosjektramme: {fmt_nok(PROJECT_TOTAL_NOK)} kr | {PROJECT_TYPE} | {DURATION_MONTHS} måneder")
    print(f"Søkt støtte: {fmt_nok(total_support)} kr | Egenfinansiering: {fmt_nok(PROJECT_TOTAL_NOK - total_support)} kr")
    print("\nArbeidspakker")
    for work_package in WORK_PACKAGES:
        print(f"{work_package['id']}: {work_package['title']} — {fmt_nok(work_package['budget_nok'])} kr")
    print("\nKostnadsbærere")
    for carrier in COST_CARRIERS:
        print(
            f"{carrier['name']}: {fmt_nok(carrier['total_cost_nok'])} kr "
            f"(støtte {fmt_nok(support_nok(carrier))} kr, "
            f"egenfinansiering {fmt_nok(own_financing_nok(carrier))} kr)"
        )
    status = vibs_cost_status()
    print("\nVIBS-underfordeling")
    print(
        f"Dokumentert/priset: {fmt_nok(status['priced_total_nok'])} kr | "
        f"Ikke underfordelt: {fmt_nok(status['unallocated_nok'])} kr | "
        f"Åpne poster: {status['unpriced_items']}"
    )
    for item in VIBS_COST_ITEMS:
        amount = "IKKE PRISET" if item["amount_nok"] is None else f"{fmt_nok(item['amount_nok'])} kr"
        print(f"- {item['name']}: {amount}")


if __name__ == "__main__":
    run_analysis()
