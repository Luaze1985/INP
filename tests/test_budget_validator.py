from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "budsjett"))
sys.path.insert(0, str(ROOT / "tools"))

import budget_validator
import kalkulator
import verify_budget_consistency


class BudgetValidatorTests(unittest.TestCase):
    def test_current_if_only_model_passes(self) -> None:
        self.assertEqual(
            budget_validator.validate_all(),
            {
                "total_cost_nok": 16_000_000,
                "total_support_nok": 8_000_000,
                "own_financing_nok": 8_000_000,
                "vibs_unallocated_nok": 12_600_000,
                "vibs_unpriced_items": 5,
            },
        )

    def test_detects_cost_carrier_and_matrix_mismatch(self) -> None:
        original = kalkulator.COST_CARRIERS[0]["total_cost_nok"]
        kalkulator.COST_CARRIERS[0]["total_cost_nok"] += 1
        try:
            with self.assertRaises(budget_validator.BudgetValidationError):
                budget_validator.validate_all()
        finally:
            kalkulator.COST_CARRIERS[0]["total_cost_nok"] = original

    def test_detects_double_counted_vibs_purchases(self) -> None:
        original_carriers = kalkulator.COST_CARRIERS
        original_matrix = kalkulator.ACTOR_AP_MATRIX
        try:
            sintef = {
                "id": "sintef",
                "name": "SINTEF",
                "role": "FoU-leverandør",
                "total_cost_nok": 100_000,
                "support_rate_percent": 50,
            }
            kalkulator.COST_CARRIERS = (*original_carriers, sintef)
            kalkulator.COST_CARRIERS[0]["total_cost_nok"] -= 100_000
            kalkulator.ACTOR_AP_MATRIX = {**original_matrix, "sintef": {"AP1": 100_000, "AP2": 0, "AP3": 0}}
            kalkulator.ACTOR_AP_MATRIX["vibs"]["AP1"] -= 100_000
            with self.assertRaises(budget_validator.BudgetValidationError):
                budget_validator.validate_all()
        finally:
            kalkulator.COST_CARRIERS[0]["total_cost_nok"] += 100_000
            kalkulator.ACTOR_AP_MATRIX["vibs"]["AP1"] += 100_000
            kalkulator.COST_CARRIERS = original_carriers
            kalkulator.ACTOR_AP_MATRIX = original_matrix

    def test_requires_complete_vibs_breakdown_to_equal_vibs_row(self) -> None:
        originals = [(item["amount_nok"], item["decision_status"], item["evidence_reference"]) for item in kalkulator.VIBS_COST_ITEMS]
        try:
            for item in kalkulator.VIBS_COST_ITEMS:
                item["amount_nok"] = 1_000_000
                item["decision_status"] = "closed"
                item["evidence_reference"] = "testgrunnlag"
            with self.assertRaises(budget_validator.BudgetValidationError):
                budget_validator.validate_all()
        finally:
            for item, original in zip(kalkulator.VIBS_COST_ITEMS, originals):
                item["amount_nok"], item["decision_status"], item["evidence_reference"] = original

    def test_rejects_priced_vibs_breakdown_with_open_gates(self) -> None:
        originals = [item["amount_nok"] for item in kalkulator.VIBS_COST_ITEMS]
        amounts = (4_000_000, 4_000_000, 2_000_000, 1_300_000, 1_300_000)
        try:
            for item, amount in zip(kalkulator.VIBS_COST_ITEMS, amounts):
                item["amount_nok"] = amount
            with self.assertRaises(budget_validator.BudgetValidationError):
                budget_validator.validate_all()
        finally:
            for item, original in zip(kalkulator.VIBS_COST_ITEMS, originals):
                item["amount_nok"] = original

    def test_if_only_documents_are_consistent(self) -> None:
        self.assertEqual(
            set(verify_budget_consistency.validate_document_consistency()),
            {
                "budsjett/fordelingsplan.md",
                "budsjett/partneroversikt.md",
                "budsjett/beregningsformler.md",
                "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.7-if-only.md",
            },
        )

    def test_document_parser_detects_wrong_table_value(self) -> None:
        rows = verify_budget_consistency._markdown_rows("| Sum | 3,0 | 5,5 | 99,0 |")
        actual = tuple(verify_budget_consistency._decimal_cell(cell) for cell in rows[0][1:])
        self.assertNotEqual(actual, (3, 5.5, 7.5))


if __name__ == "__main__":
    unittest.main()
