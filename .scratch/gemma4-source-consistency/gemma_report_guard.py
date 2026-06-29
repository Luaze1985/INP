import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = {"ok", "flagged_rows", "reason", "recommended_action"}
REQUIRED_ROW_FIELDS = {"item", "reason", "recommended_action"}


def audit_report(candidates_path: Path | str, report_path: Path | str) -> dict[str, Any]:
    candidate_titles = _candidate_titles(Path(candidates_path))
    report = _load_json(Path(report_path))

    issues: list[dict[str, str]] = []
    missing = REQUIRED_TOP_LEVEL - set(report)
    if missing:
        issues.append(
            {
                "code": "missing_top_level_fields",
                "detail": ", ".join(sorted(missing)),
            }
        )
        return {"ok": False, "issues": issues}

    flagged_rows = report.get("flagged_rows")
    if not isinstance(flagged_rows, list):
        issues.append({"code": "invalid_flagged_rows", "detail": "flagged_rows must be a list"})
        return {"ok": False, "issues": issues}

    if report.get("ok") is False and not flagged_rows:
        issues.append(
            {
                "code": "non_actionable_false_report",
                "detail": "ok=false must include at least one flagged row",
            }
        )

    for row in flagged_rows:
        if not isinstance(row, dict):
            issues.append({"code": "invalid_flagged_row", "detail": "row must be an object"})
            continue

        missing_row_fields = REQUIRED_ROW_FIELDS - set(row)
        if missing_row_fields:
            issues.append(
                {
                    "code": "missing_flagged_row_fields",
                    "detail": ", ".join(sorted(missing_row_fields)),
                }
            )
            continue

        item = str(row["item"]).strip()
        if item not in candidate_titles:
            issues.append({"code": "unknown_flagged_item", "detail": item})

    return {"ok": not issues, "issues": issues}


def _candidate_titles(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    titles: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^\s*\d+\.\s+(.+?)\s*$", line)
        if match:
            titles.add(match.group(1))
    return titles


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("report JSON must be an object")
    return value


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 2:
        print("usage: gemma_report_guard.py <candidates.md> <gemma-report.json>", file=sys.stderr)
        return 2

    result = audit_report(Path(args[0]), Path(args[1]))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
