#!/usr/bin/env python3
"""Compare the canonical application, website manuscript, and rendered HTML.

The check is deliberately deterministic. It does not decide whether a paraphrase
is scientifically supported; it finds drift that a person must review:

* numeric values in the public HTML that do not occur in the application text;
* named entities in the public HTML that do not occur in the application text;
* low word-shingle overlap between the active website manuscript and the HTML;
* missing canonical input files.

Exit codes: 0 = no blocking drift, 1 = drift found, 2 = invalid invocation.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APPLICATION = (
    REPO_ROOT
    / "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.9.md"
)
DEFAULT_MANUSCRIPT = REPO_ROOT / "site/tekstmanus.md"
DEFAULT_HTML = REPO_ROOT / "site/web/index.html"

WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)
NUMBER_RE = re.compile(
    r"(?<![\w])(?:~|ca\.\s*)?\d{1,3}(?:[ .\u00a0]\d{3})+(?:[,.]\d+)?"
    r"|(?<![\w])(?:~|ca\.\s*)?\d+[,.]\d+\s*(?:%|prosent)?"
    r"|(?<![\w])\d+\s*%"
    r"|(?<![\w])\d+\s*(?:skader?|mrd\.?|milliarder?|millioner?|mnok|kroner?|kr\b)",
    re.IGNORECASE,
)
ENTITY_RE = re.compile(
    r"\b(?:[A-ZÆØÅ][\wÆØÅæøå-]+(?:[ \t]+|/|&)){1,3}[A-ZÆØÅ][\wÆØÅæøå-]+\b"
)

# Common labels and sentence starts are not useful named-entity candidates.
ENTITY_STOPWORDS = {
    "IPN Forskningsprosjekt",
    "Hva VERIFIED",
    "Her Her",
    "Kilde Finans Norge",
    "Kilde SSB",
    "Kilde BDO",
}


@dataclass(frozen=True)
class Finding:
    severity: str
    check: str
    value: str
    location: str
    message: str


@dataclass(frozen=True)
class Report:
    application: str
    manuscript: str
    website: str
    application_manuscript_overlap: float
    manuscript_html_overlap: float
    html_manuscript_overlap: float
    findings: list[Finding]

    @property
    def blocking_count(self) -> int:
        return sum(f.severity == "error" for f in self.findings)


class VisibleHTMLParser(HTMLParser):
    """Collect public and assistive text, excluding code and CSS."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag in {"script", "style", "template"}:
            self._ignored_depth += 1
            return
        if tag == "meta" and attrs_dict.get("content") and (
            attrs_dict.get("name") in {"description", "twitter:title", "twitter:description"}
            or attrs_dict.get("property") in {"og:title", "og:description"}
        ):
            self.parts.append(attrs_dict["content"] or "")
        for attribute in ("alt", "aria-label", "title"):
            if attrs_dict.get(attribute):
                self.parts.append(attrs_dict[attribute] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "template"} and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._ignored_depth:
            self.parts.append(data)

    def text(self) -> str:
        return "\n".join(part.strip() for part in self.parts if part.strip())


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def active_manuscript(markdown: str) -> str:
    """Keep current public copy; discard workflow notes and change history."""
    start = markdown.find("## Seksjon 1")
    if start == -1:
        start = 0
    endpoints = [
        pos
        for marker in ("## Flyt og budskap", "## Endringslogg")
        if (pos := markdown.find(marker, start)) != -1
    ]
    end = min(endpoints) if endpoints else len(markdown)
    active = markdown[start:end]
    # These are editorial instructions about deliberately hidden elements, not
    # public copy. Keeping them would make removed claims look active.
    active = re.sub(
        r"(?m)^\*\*(?:Partnerstripe|Søknadsramme|Alt-strategi):\*\*.*(?:\n(?!\n).*)*",
        "",
        active,
    )
    return active


def markdown_to_text(markdown: str) -> str:
    text = re.sub(r"```.*?```", " ", markdown, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_>#|]", " ", text)
    return html.unescape(text)


def html_to_text(source: str) -> str:
    parser = VisibleHTMLParser()
    parser.feed(source)
    return parser.text()


def normalized_words(text: str) -> list[str]:
    return [word.casefold() for word in WORD_RE.findall(text)]


def shingle_overlap(expected: str, actual: str, size: int = 4) -> float:
    expected_words = normalized_words(expected)
    actual_words = normalized_words(actual)
    if len(expected_words) < size:
        return 1.0 if expected_words == actual_words else 0.0
    expected_shingles = {
        tuple(expected_words[index : index + size])
        for index in range(len(expected_words) - size + 1)
    }
    actual_shingles = {
        tuple(actual_words[index : index + size])
        for index in range(max(0, len(actual_words) - size + 1))
    }
    return len(expected_shingles & actual_shingles) / len(expected_shingles)


def unsupported_sentences(text: str, reference: str, *, size: int = 4) -> list[str]:
    """Return substantial sentences with no exact phrase anchor in reference."""
    reference_words = normalized_words(reference)
    reference_shingles = {
        tuple(reference_words[index : index + size])
        for index in range(max(0, len(reference_words) - size + 1))
    }
    candidates = re.split(r"(?<=[.!?])\s+|\n+", text)
    unsupported: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        candidate = re.sub(r"\s+", " ", candidate).strip(" -–—:;")
        words = normalized_words(candidate)
        if len(words) < 8:
            continue
        shingles = {
            tuple(words[index : index + size])
            for index in range(len(words) - size + 1)
        }
        if shingles & reference_shingles:
            continue
        folded = candidate.casefold()
        if folded not in seen:
            seen.add(folded)
            unsupported.append(candidate)
    return unsupported


def normalize_number(value: str) -> str:
    value = value.casefold().replace("\u00a0", " ")
    value = re.sub(r"^(?:~|ca\.\s*)", "", value)
    value = value.replace("prosent", "%")
    value = value.replace(" ", "").replace(".", "").replace(",", ".")
    return value


def numbers(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for match in NUMBER_RE.finditer(text):
        raw = match.group(0).strip()
        found.setdefault(normalize_number(raw), raw)
    return found


def entities(text: str) -> set[str]:
    return {
        match.group(0).strip()
        for match in ENTITY_RE.finditer(text)
        if match.group(0).strip() not in ENTITY_STOPWORDS
    }


def first_line_containing(text: str, needle: str) -> int:
    folded_needle = needle.casefold()
    for number, line in enumerate(text.splitlines(), start=1):
        if folded_needle in line.casefold():
            return number
    return 1


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def compare(
    application_path: Path,
    manuscript_path: Path,
    website_path: Path,
    *,
    minimum_overlap: float = 0.55,
    minimum_application_overlap: float = 0.10,
) -> Report:
    paths = [application_path, manuscript_path, website_path]
    missing = [path for path in paths if not path.is_file()]
    if missing:
        findings = [
            Finding("error", "input", rel(path), rel(path), "Canonical input is missing")
            for path in missing
        ]
        return Report(
            rel(application_path), rel(manuscript_path), rel(website_path), 0.0, 0.0, 0.0, findings
        )

    application_source = read_text(application_path)
    manuscript_source = read_text(manuscript_path)
    website_source = read_text(website_path)
    application_text = markdown_to_text(application_source)
    manuscript_text = markdown_to_text(active_manuscript(manuscript_source))
    website_text = html_to_text(website_source)

    findings: list[Finding] = []
    application_overlap = shingle_overlap(manuscript_text, application_text)
    manuscript_overlap = shingle_overlap(manuscript_text, website_text)
    html_overlap = shingle_overlap(website_text, manuscript_text)
    if application_overlap < minimum_application_overlap:
        findings.append(
            Finding(
                "error",
                "application-manuscript-overlap",
                f"{application_overlap:.1%}",
                rel(manuscript_path),
                "Active manuscript has too little deterministic phrase support in the application",
            )
        )
    if manuscript_overlap < minimum_overlap:
        findings.append(
            Finding(
                "error",
                "manuscript-html-overlap",
                f"{manuscript_overlap:.1%}",
                rel(website_path),
                f"Website matches less than {minimum_overlap:.0%} of the active manuscript",
            )
        )
    if html_overlap < minimum_overlap:
        findings.append(
            Finding(
                "error",
                "html-manuscript-overlap",
                f"{html_overlap:.1%}",
                rel(website_path),
                f"Less than {minimum_overlap:.0%} of public HTML is anchored in the manuscript",
            )
        )

    for sentence in unsupported_sentences(website_text, manuscript_text):
        line = first_line_containing(website_source, sentence[:40])
        findings.append(
            Finding(
                "error",
                "unsupported-prose-website",
                sentence,
                f"{rel(website_path)}:{line}",
                "Public sentence has no four-word phrase anchor in the active manuscript",
            )
        )

    application_numbers = numbers(application_text)
    numeric_inputs = (
        ("manuscript", manuscript_source, manuscript_text, manuscript_path),
        ("website", website_source, website_text, website_path),
    )
    for label, source, text, path in numeric_inputs:
        for normalized, raw in sorted(numbers(text).items()):
            if normalized not in application_numbers:
                line = first_line_containing(source, raw)
                findings.append(
                    Finding(
                        "error",
                        f"unsupported-number-{label}",
                        raw,
                        f"{rel(path)}:{line}",
                        "Numeric value does not occur in the application text",
                    )
                )

    application_folded = application_text.casefold()
    entity_inputs = (
        ("manuscript", manuscript_source, manuscript_text, manuscript_path),
        ("website", website_source, website_text, website_path),
    )
    for label, source, text, path in entity_inputs:
        for entity in sorted(entities(text)):
            if entity.casefold() not in application_folded:
                line = first_line_containing(source, entity)
                findings.append(
                    Finding(
                        "error",
                        f"unmatched-name-{label}",
                        entity,
                        f"{rel(path)}:{line}",
                        "Name or organization does not occur in the application text",
                    )
                )

    return Report(
        rel(application_path),
        rel(manuscript_path),
        rel(website_path),
        application_overlap,
        manuscript_overlap,
        html_overlap,
        findings,
    )


def report_payload(report: Report) -> dict[str, object]:
    return {
        "application": report.application,
        "manuscript": report.manuscript,
        "website": report.website,
        "application_manuscript_overlap": round(report.application_manuscript_overlap, 4),
        "manuscript_html_overlap": round(report.manuscript_html_overlap, 4),
        "html_manuscript_overlap": round(report.html_manuscript_overlap, 4),
        "blocking_count": report.blocking_count,
        "finding_count": len(report.findings),
        "findings": [asdict(finding) for finding in report.findings],
    }


def print_human(report: Report) -> None:
    print("APPLICATION ↔ WEBSITE CHECK")
    print(f"Application: {report.application}")
    print(f"Manuscript:  {report.manuscript}")
    print(f"Website:     {report.website}")
    print(f"Application/manuscript overlap: {report.application_manuscript_overlap:.1%}")
    print(f"Manuscript/HTML overlap: {report.manuscript_html_overlap:.1%}")
    print(f"HTML/manuscript overlap: {report.html_manuscript_overlap:.1%}")
    if not report.findings:
        print("OK: no deterministic drift found")
        return
    print(f"Findings: {len(report.findings)} ({report.blocking_count} blocking)")
    for finding in report.findings:
        marker = "ERROR" if finding.severity == "error" else "WARN"
        print(
            f"{marker} [{finding.check}] {finding.location}: "
            f"{finding.value!r} — {finding.message}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--application", type=Path, default=DEFAULT_APPLICATION)
    parser.add_argument("--manuscript", type=Path, default=DEFAULT_MANUSCRIPT)
    parser.add_argument("--website", type=Path, default=DEFAULT_HTML)
    parser.add_argument("--minimum-overlap", type=float, default=0.55)
    parser.add_argument("--minimum-application-overlap", type=float, default=0.10)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--report", type=Path, help="Write the same JSON payload to a file")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = build_parser().parse_args(argv)
    if not 0 <= args.minimum_overlap <= 1 or not 0 <= args.minimum_application_overlap <= 1:
        print("overlap thresholds must be between 0 and 1", file=sys.stderr)
        return 2
    report = compare(
        args.application,
        args.manuscript,
        args.website,
        minimum_overlap=args.minimum_overlap,
        minimum_application_overlap=args.minimum_application_overlap,
    )
    payload = report_payload(report)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_human(report)
    return 1 if report.blocking_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
