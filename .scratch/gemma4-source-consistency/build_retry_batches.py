from pathlib import Path

from build_all_source_batches import HEADER, OUT_DIR, build_candidate, extract_library_rows


FAILED_KEYS = {
    "ecoinvent",
    "Mecca2023",
    "Ciroth2016",
    "MCDM2025",
    "WLC-benchmark-NO",
    "EBA_EU2023",
    "Billio2022",
    "An2020",
    "Kaza2014",
    "BoE_PS25-25",
    "BoE_DP1-25",
    "EEMI",
    "FinanceNorway2018",
    "Multiconsult2023",
    "EC3",
    "OneClickLCA",
    "Harerusten2022",
    "Bygg21_2019",
    "KS2025",
    "Nordic2023",
    "BKA2",
    "Lutdal2021",
    "Refleksjonsnotat2026",
    "Wiik2025",
    "GullbrekkenHolme2025",
    "EBA_NO2023",
    "KD2024",
    "VIBS-FoUpanel",
}


def chunks(items: list[dict[str, str]], size: int) -> list[list[dict[str, str]]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def main() -> int:
    retry_dir = OUT_DIR / "retry"
    retry_dir.mkdir(parents=True, exist_ok=True)
    for old in retry_dir.glob("retry-*.md"):
        old.unlink()

    rows = [row for row in extract_library_rows() if row["key"] in FAILED_KEYS]
    key_order = {key: index for index, key in enumerate(FAILED_KEYS)}
    rows.sort(key=lambda row: key_order[row["key"]])

    manifest = ["# Retry Gemma microbatches", "", f"Total sources: {len(rows)}", ""]
    for index, batch in enumerate(chunks(rows, 2), start=1):
        path = retry_dir / f"retry-{index:02d}.md"
        body = [HEADER.strip(), "", "Kandidater:"]
        for offset, row in enumerate(batch, start=1):
            body.append("")
            body.append(f"{offset}. [{row['key']}]")
            body.append(build_candidate(row))
        path.write_text("\n".join(body) + "\n", encoding="utf-8")
        manifest.append(f"- {path.relative_to(OUT_DIR.parents[2])}: " + ", ".join(f"[{row['key']}]" for row in batch))

    (retry_dir / "manifest.md").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(f"wrote {len(rows)} sources in {len(chunks(rows, 2))} retry batches to {retry_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
