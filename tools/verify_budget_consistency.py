"""Kontroller IF-only-tall og dokumentdrift i den kanoniske budsjettpakken."""

from __future__ import annotations

import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import budget_validator


class BudgetDocumentError(ValueError):
    """Raised when a canonical budget document has drifted from IF-only."""


TABLE_EXPECTATIONS = {
    "budsjett/fordelingsplan.md": {
        "offset": 1,
        "rows": {
            "Vi Bygger Sammen AS": ("2,6", "4,3", "5,7", "12,6", "6,3", "6,3"),
            "D Takst AS, partnerkandidat": ("0,1", "0,6", "0,8", "1,5", "0,75", "0,75"),
            "Byggmester Espeland AS, partnerkandidat": ("0,0", "0,2", "0,4", "0,6", "0,30", "0,30"),
            "Norsk Byggtjeneste AS, partnerkandidat": ("0,3", "0,4", "0,6", "1,3", "0,65", "0,65"),
            "Sum": ("3,0", "5,5", "7,5", "16,0", "8,0", "8,0"),
        },
    },
    "budsjett/partneroversikt.md": {
        "offset": 2,
        "rows": {
            "Vi Bygger Sammen AS": ("2,6", "4,3", "5,7", "12,6", "6,3", "6,3"),
            "D Takst AS": ("0,1", "0,6", "0,8", "1,5", "0,75", "0,75"),
            "Byggmester Espeland AS": ("0,0", "0,2", "0,4", "0,6", "0,30", "0,30"),
            "Norsk Byggtjeneste AS": ("0,3", "0,4", "0,6", "1,3", "0,65", "0,65"),
            "Sum": ("3,0", "5,5", "7,5", "16,0", "8,0", "8,0"),
        },
    },
    "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.7-if-only.md": {
        "offset": 1,
        "rows": {
            "Vi Bygger Sammen AS": ("12,6", "6,3", "6,3"),
            "Kandidat: metode- og valideringspartner": ("1,5", "0,75", "0,75"),
            "Kandidat: SMB-partner A": ("0,6", "0,30", "0,30"),
            "Kandidat: data- og standardpartner": ("1,3", "0,65", "0,65"),
            "Sum": ("16,0", "8,0", "8,0"),
        },
    },
}

REQUIRED_MARKERS = {
    "budsjett/beregningsformler.md": (
        "16 000 000 × 50 % = 8 000 000 kroner søkt støtte",
        "VIBS egne kostnader",
        "= 12,6 MNOK",
        "Ingen reserve i kroner angis før dette finnes.",
    ),
}

STALE_CLAIMS = (
    "Totalt prosjektbudsjett:** 32 000 000",
    "Søkt NFR-støtte:** **15 130 000",
    "SINTEF Community (FoU-innkjøp): 8,5 MNOK",
    "Axon Development LLC (2,8 MNOK",
)


def _clean_cell(value: str) -> str:
    return value.replace("**", "").replace("MNOK", "").strip()


def _decimal_cell(value: str) -> Decimal:
    try:
        return Decimal(_clean_cell(value).replace(" ", "").replace(",", "."))
    except InvalidOperation as error:
        raise BudgetDocumentError(f"Kan ikke lese budsjettbeløp: {value}") from error


def _markdown_rows(text: str) -> list[list[str]]:
    return [[_clean_cell(cell) for cell in line.strip().strip("|").split("|")] for line in text.splitlines() if line.lstrip().startswith("|")]


def validate_document_consistency() -> list[str]:
    checked: list[str] = []
    for relative_path, specification in TABLE_EXPECTATIONS.items():
        path = ROOT / relative_path
        if not path.is_file():
            raise BudgetDocumentError(f"Mangler kanonisk budsjettfil: {relative_path}")
        text = path.read_text(encoding="utf-8")
        rows = _markdown_rows(text)
        for label, expected_values in specification["rows"].items():
            matches = [row for row in rows if row and row[0] == label]
            if not matches:
                raise BudgetDocumentError(f"{relative_path} mangler budsjettrad: {label}")
            expected = tuple(_decimal_cell(value) for value in expected_values)
            offset = specification["offset"]
            if not any(tuple(_decimal_cell(cell) for cell in row[offset : offset + len(expected)]) == expected for row in matches):
                raise BudgetDocumentError(f"{relative_path} har feil beløp i raden: {label}")
        stale = [claim for claim in STALE_CLAIMS if claim in text]
        if stale:
            raise BudgetDocumentError(f"{relative_path} inneholder gammel 32 MNOK-modell: {stale[0]}")
        checked.append(relative_path)
    for relative_path, required in REQUIRED_MARKERS.items():
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        missing = [marker for marker in required if marker not in text]
        if missing:
            raise BudgetDocumentError(f"{relative_path} mangler beregningsregel: {missing[0]}")
        checked.append(relative_path)
    return checked


def main() -> int:
    try:
        totals = budget_validator.validate_all()
        checked = validate_document_consistency()
    except (budget_validator.BudgetValidationError, BudgetDocumentError) as error:
        print(f"BUDSJETTKONSISTENS FEILET: {error}")
        return 1
    print("BUDSJETTKONSISTENS PASS")
    print(f"Kontrollerte dokumenter: {len(checked)}")
    print(
        f"Ramme/støtte/egenfinansiering: {totals['total_cost_nok']} / "
        f"{totals['total_support_nok']} / {totals['own_financing_nok']} kr"
    )
    if totals["vibs_unpriced_items"]:
        print(f"STATUS: IKKE INNSENDINGSKLAR — {totals['vibs_unpriced_items']} VIBS-poster er ikke priset")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
