from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "budsjett"))
sys.path.insert(0, str(ROOT / "tools"))

import budget_validator
import kalkulator


class BudgetValidatorTests(unittest.TestCase):
    def test_current_if_only_model_passes(self) -> None:
        self.assertEqual(
            budget_validator.validate_all(),
            {"total_cost_nok": 16_000_000, "total_support_nok": 8_000_000, "own_financing_nok": 8_000_000},
        )

    def test_detects_cost_carrier_and_matrix_mismatch(self) -> None:
        original = kalkulator.COST_CARRIERS[0]["total_cost_nok"]
        kalkulator.COST_CARRIERS[0]["total_cost_nok"] += 1
        try:
            with self.assertRaises(budget_validator.BudgetValidationError):
                budget_validator.validate_all()
        finally:
            kalkulator.COST_CARRIERS[0]["total_cost_nok"] = original


if __name__ == "__main__":
    unittest.main()
