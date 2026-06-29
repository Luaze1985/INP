import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / ".scratch" / "gemma4-source-consistency" / "all-sources"
LIBRARY = ROOT / "docs" / "reference" / "ipn-kildebibliotek.md"
KILDEDOM = ROOT / "docs" / "reference" / "vibs-verified-kildedom-2026-06-27.md"
CANONICAL_DOCS = [
    ROOT / "docs" / "reference" / "ipn-hovedokument.md",
    ROOT / "docs" / "reference" / "ipn-samledokument.md",
    ROOT / "docs" / "reference" / "ipn-prosjektbeskrivelse-utkast.md",
]
BATCH_SIZE = 8


HEADER = """Oppgave: Vurder kildestatusdrift for disse kildene.
Les kun kandidatene under. Ikke finn pa fakta. Ikke gjor ny web/faktasjekk.

Returner gyldig JSON med:
{
  "ok": true/false,
  "flagged_rows": [
    {"item": "[EKSAKT_KILDEKEY]", "reason": "...", "recommended_action": "..."}
  ],
  "reason": "...",
  "recommended_action": "..."
}

Tvangsregel:
- Hvis ok=false, MAA flagged_rows ha minst en konkret rad.
- item MAA vaere en av kandidatoverskriftene, noyaktig som [KEY].
- Ikke flagg en kilde bare fordi den mangler i kildedommen; kildedommen er et subset.
- Flagg bare tydelig statusdrift: gronn vs gul/pause/rod, parkert kilde som brukes baerende, eller gammel/feil nokkel som fortsatt ser aktiv ut.

Repo-regler:
- Gronn kan baere en soknadssetning alene.
- Gul ma apnes/fraseres med forbehold.
- Rod er ikke siterbar.
- Pause betyr tatt ut av soknadstekst og parkert med gjeninnsettingsvilkar.
"""


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_library_rows() -> list[dict[str, str]]:
    rows = []
    for line_no, line in enumerate(read(LIBRARY).splitlines(), start=1):
        match = re.match(r"^\| `\[(?P<key>[^\]]+)\]` \| (?P<body>.+)$", line)
        if not match:
            continue
        rows.append({"key": match.group("key"), "line": str(line_no), "row": line})
    return rows


def key_hits(path: Path, key: str) -> list[str]:
    hits = []
    pattern = re.compile(re.escape(key), re.IGNORECASE)
    for line_no, line in enumerate(read(path).splitlines(), start=1):
        if pattern.search(line):
            clean = re.sub(r"\s+", " ", line).strip()
            hits.append(f"{path.relative_to(ROOT)}:{line_no}: {clean[:260]}")
    return hits


def build_candidate(row: dict[str, str]) -> str:
    key = row["key"]
    parts = [f"[{key}]", f"- Kildebibliotek linje {row['line']}: {row['row']}"]

    kildedom_hits = key_hits(KILDEDOM, key)
    if kildedom_hits:
        parts.append("- Kildedom-treff:")
        parts.extend(f"  - {hit}" for hit in kildedom_hits[:4])
    else:
        parts.append("- Kildedom-treff: ingen (ikke flagg dette alene)")

    canonical_hits = []
    for doc in CANONICAL_DOCS:
        canonical_hits.extend(key_hits(doc, key))
    if canonical_hits:
        parts.append("- Bruk i kanoniske soknadsdocs:")
        parts.extend(f"  - {hit}" for hit in canonical_hits[:5])
    else:
        parts.append("- Bruk i kanoniske soknadsdocs: ingen direkte key-treff")

    return "\n".join(parts)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUT_DIR.glob("batch-*.md"):
        old.unlink()

    rows = extract_library_rows()
    manifest_lines = ["# All-source Gemma batches", "", f"Total sources: {len(rows)}", ""]
    for batch_index, start in enumerate(range(0, len(rows), BATCH_SIZE), start=1):
        batch = rows[start : start + BATCH_SIZE]
        path = OUT_DIR / f"batch-{batch_index:02d}.md"
        body = [HEADER.strip(), "", "Kandidater:"]
        for offset, row in enumerate(batch, start=1):
            body.append("")
            body.append(f"{offset}. [{row['key']}]")
            body.append(build_candidate(row))
        path.write_text("\n".join(body) + "\n", encoding="utf-8")
        manifest_lines.append(f"- {path.relative_to(ROOT)}: " + ", ".join(f"[{row['key']}]" for row in batch))

    (OUT_DIR / "manifest.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    print(f"wrote {len(rows)} sources in {batch_index} batches to {OUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
