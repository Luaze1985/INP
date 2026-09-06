"""Valider den IF-only budsjettmodellen uten skjulte standardantakelser."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "budsjett"))
import kalkulator


class BudgetValidationError(ValueError):
    """Raised when the budget source of truth is internally inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BudgetValidationError(message)


def validate_all() -> dict[str, int]:
    work_packages = kalkulator.work_package_by_id()
    carriers = kalkulator.carrier_by_id()
    package_ids = tuple(work_packages)
    carrier_ids = set(carriers)

    require(package_ids == ("AP1", "AP2", "AP3"), "Arbeidspakkene skal være AP1, AP2 og AP3")
    require(all(wp["type"] == kalkulator.PROJECT_TYPE == "IF" for wp in work_packages.values()), "Alle arbeidspakker skal være IF")
    require(sum(wp["budget_nok"] for wp in work_packages.values()) == kalkulator.PROJECT_TOTAL_NOK, "Arbeidspakkene summerer ikke til prosjektrammen")
    require(set(kalkulator.ACTOR_AP_MATRIX) == carrier_ids, "Matrisen og kostnadsbærerne har ulike aktørsett")
    require(tuple(carriers) == kalkulator.LOCKED_COST_CARRIER_IDS, "Budsjettet skal ha nøyaktig de fem besluttede kostnadsbærerne")

    for carrier_id, carrier in carriers.items():
        require(carrier["total_cost_nok"] >= 0, f"Negativ kostnad for {carrier['name']}")
        require(carrier["support_rate_percent"] == kalkulator.SUPPORT_RATE_PERCENT == 50, f"Feil IF-støttesats for {carrier['name']}")
        row = kalkulator.ACTOR_AP_MATRIX[carrier_id]
        require(tuple(row) == package_ids, f"Feil AP-kolonner for {carrier['name']}")
        require(all(isinstance(amount, int) and amount >= 0 for amount in row.values()), f"Ugyldig AP-beløp for {carrier['name']}")
        require(sum(row.values()) == carrier["total_cost_nok"], f"Aktørmatrisen stemmer ikke med kostnadsbærer for {carrier['name']}")

    for package_id, work_package in work_packages.items():
        matrix_total = sum(row[package_id] for row in kalkulator.ACTOR_AP_MATRIX.values())
        require(matrix_total == work_package["budget_nok"], f"Aktørmatrisen stemmer ikke med {package_id}")

    total_cost = sum(carrier["total_cost_nok"] for carrier in carriers.values())
    total_support = sum(kalkulator.support_nok(carrier) for carrier in carriers.values())
    require(total_cost == kalkulator.PROJECT_TOTAL_NOK, "Kostnadsbærerne summerer ikke til prosjektrammen")
    require(total_support == kalkulator.PROJECT_TOTAL_NOK // 2, "IF-støtten skal være 50 % av prosjektrammen")

    vibs = carriers["vibs"]
    vibs_item_ids = [item["id"] for item in kalkulator.VIBS_COST_ITEMS]
    require(len(vibs_item_ids) == 5, "VIBS-underfordelingen skal ha fem poster")
    require(len(set(vibs_item_ids)) == len(vibs_item_ids), "VIBS-underfordelingen har duplikate poster")
    for item in kalkulator.VIBS_COST_ITEMS:
        amount = item["amount_nok"]
        require(amount is None or (isinstance(amount, int) and not isinstance(amount, bool) and amount >= 0), f"Ugyldig beløp i VIBS-posten {item['name']}")
        require(bool(item["required_evidence"]), f"VIBS-posten {item['name']} mangler dokumentasjonsport")
        require(item["decision_status"] in {"open", "closed", "excluded"}, f"Ugyldig beslutningsstatus for {item['name']}")
        if amount is None:
            require(item["decision_status"] == "open", f"Upriset VIBS-post må stå åpen: {item['name']}")
        elif amount == 0:
            require(item["decision_status"] == "excluded" and bool(item["evidence_reference"]), f"Nullstilt VIBS-post mangler dokumentert uttaksbeslutning: {item['name']}")
        else:
            require(item["decision_status"] == "closed" and bool(item["evidence_reference"]), f"Priset VIBS-post mangler lukket dokumentasjonsport: {item['name']}")

    vibs_status = kalkulator.vibs_cost_status()
    require(vibs_status["priced_total_nok"] <= vibs["total_cost_nok"], "Prisede VIBS-poster overstiger VIBS-raden")
    if vibs_status["complete"]:
        require(vibs_status["priced_total_nok"] == vibs["total_cost_nok"], "Komplett VIBS-underfordeling summerer ikke til 12,6 MNOK")
    require(len(kalkulator.VIBS_DECISION_GATES) >= 6, "VIBS-underfordelingen mangler beslutningsporter")

    return {
        "total_cost_nok": total_cost,
        "total_support_nok": total_support,
        "own_financing_nok": total_cost - total_support,
        "vibs_unallocated_nok": vibs_status["unallocated_nok"],
        "vibs_unpriced_items": vibs_status["unpriced_items"],
    }


def main() -> int:
    try:
        result = validate_all()
    except BudgetValidationError as error:
        print(f"BUDSJETTVALIDERING FEILET: {error}")
        return 1
    print("BUDSJETTVALIDERING PASS")
    print(f"Totalbudsjett: {kalkulator.fmt_nok(result['total_cost_nok'])} kr")
    print(f"Søkt NFR-støtte: {kalkulator.fmt_nok(result['total_support_nok'])} kr (50,00 %)")
    print(f"Egenfinansiering: {kalkulator.fmt_nok(result['own_financing_nok'])} kr (50,00 %)")
    if result["vibs_unpriced_items"]:
        print(
            "STATUS: IKKE INNSENDINGSKLAR — "
            f"{result['vibs_unpriced_items']} VIBS-poster mangler dokumenterte beløp; "
            f"{kalkulator.fmt_nok(result['vibs_unallocated_nok'])} kr er ikke underfordelt."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
