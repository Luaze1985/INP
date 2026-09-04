"""Enkel, deterministisk IF-kalkyle for VERIFIED.

Denne modellen gjelder bare AP1-AP3. Leverandørkjøp er samlet under Vi Bygger
Sammen AS og skal ikke føres som ekstra kostnadsbærere eller egenfinansiering.
Alle beløp er hele NOK.
"""

PROJECT_TOTAL_NOK = 16_000_000
PROJECT_TYPE = "IF"
SUPPORT_RATE_PERCENT = 50
DURATION_MONTHS = 36

WORK_PACKAGES = (
    {"id": "AP1", "title": "Forskningsprotokoll og datakvalitet", "budget_nok": 3_000_000, "type": "IF"},
    {"id": "AP2", "title": "Målemodell og harmonisering", "budget_nok": 5_500_000, "type": "IF"},
    {"id": "AP3", "title": "Usikkerhetsmodell og modellfrys", "budget_nok": 7_500_000, "type": "IF"},
)

# Dette er de eneste aktørene som bærer prosjektkostnad og egenfinansiering.
COST_CARRIERS = (
    {"id": "vibs", "name": "Vi Bygger Sammen AS", "role": "Prosjektansvarlig", "total_cost_nok": 12_600_000, "support_rate_percent": 50},
    {"id": "d_takst", "name": "D Takst AS", "role": "Samarbeidspartner", "total_cost_nok": 1_500_000, "support_rate_percent": 50},
    {"id": "espeland", "name": "Byggmester Espeland AS", "role": "Samarbeidspartner", "total_cost_nok": 300_000, "support_rate_percent": 50},
    {"id": "norgesbygg_sor", "name": "Norgesbygg Sør AS", "role": "Samarbeidspartner", "total_cost_nok": 300_000, "support_rate_percent": 50},
    {"id": "norsk_byggtjeneste", "name": "Norsk Byggtjeneste AS", "role": "Samarbeidspartner", "total_cost_nok": 1_300_000, "support_rate_percent": 50},
)

# Samme kostnadsbærere som over, fordelt på AP1-AP3. Alle beløp er hele NOK.
ACTOR_AP_MATRIX = {
    "vibs": {"AP1": 2_600_000, "AP2": 4_300_000, "AP3": 5_700_000},
    "d_takst": {"AP1": 100_000, "AP2": 600_000, "AP3": 800_000},
    "espeland": {"AP1": 0, "AP2": 100_000, "AP3": 200_000},
    "norgesbygg_sor": {"AP1": 0, "AP2": 100_000, "AP3": 200_000},
    "norsk_byggtjeneste": {"AP1": 300_000, "AP2": 400_000, "AP3": 600_000},
}


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


if __name__ == "__main__":
    run_analysis()
