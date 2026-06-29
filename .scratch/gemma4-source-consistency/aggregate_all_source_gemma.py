import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / ".scratch" / "gemma4-source-consistency" / "all-sources"
REPORTS = [
    OUT_DIR / "batch-01.gemma.json",
    OUT_DIR / "batch-02.gemma.json",
    OUT_DIR / "batch-05.gemma.json",
    OUT_DIR / "batch-06.gemma.json",
    *sorted((OUT_DIR / "retry").glob("retry-*.gemma.json")),
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    rows_by_item = defaultdict(list)
    ok_count = 0
    false_count = 0

    for report in REPORTS:
        data = load_json(report)
        if data.get("ok") is True:
            ok_count += 1
        else:
            false_count += 1
        for row in data.get("flagged_rows", []):
            rows_by_item[row["item"]].append(
                {
                    "report": str(report.relative_to(ROOT)),
                    "reason": row.get("reason", ""),
                    "recommended_action": row.get("recommended_action", ""),
                }
            )

    lines = [
        "# Gemma all-source audit summary",
        "",
        f"Reports counted: {len(REPORTS)}",
        f"Reports ok=true: {ok_count}",
        f"Reports ok=false: {false_count}",
        f"Flagged source keys: {len(rows_by_item)}",
        "",
        "## Flagged rows",
        "",
    ]

    for item in sorted(rows_by_item):
        lines.append(f"### {item}")
        for hit in rows_by_item[item]:
            lines.append(f"- Report: `{hit['report']}`")
            lines.append(f"- Reason: {hit['reason']}")
            lines.append(f"- Recommended action: {hit['recommended_action']}")
        lines.append("")

    out = OUT_DIR / "gemma-all-source-summary.md"
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(out.relative_to(ROOT))
    print(f"flagged={len(rows_by_item)} reports={len(REPORTS)} ok_true={ok_count} ok_false={false_count}")
    for item in sorted(rows_by_item):
        print(item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
