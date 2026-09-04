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

    return {"total_cost_nok": total_cost, "total_support_nok": total_support, "own_financing_nok": total_cost - total_support}


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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
