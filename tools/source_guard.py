#!/usr/bin/env python3
"""Block retired or uncertain sources from re-entering active text.

Exit codes:
  0: clean
  1: blocked source or relationship found
  2: invalid registry, arguments, or unreadable input
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence


REPO_ROOT = Path(os.environ.get("SOURCE_GUARD_REPO_ROOT", Path(__file__).resolve().parents[1])).resolve()
DEFAULT_REGISTRY = REPO_ROOT / "governance" / "source-blocklist.json"
TEXT_EXTENSIONS = {
    ".html",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}
REQUIRED_ENTRY_FIELDS = {
    "id",
    "canonical_key",
    "aliases",
    "normalized_title",
    "identifiers",
    "status",
    "reason",
    "decision_date",
    "decision_maker",
    "replacement",
    "reopen_rule",
    "match",
}
ALLOWED_MATCH_TYPES = {"any-identifier", "all-groups-in-paragraph"}
ALLOWED_REOPEN_RULES = {"original-required", "manual-only", "never"}
ALLOWED_STATUSES = {
    "blocked-original-required",
    "replaced-alias",
    "retired-relationship",
}
REQUIRED_ENTRY_IDS = frozenset(f"SP-{index:02d}" for index in range(1, 12))
REQUIRED_ACTIVE_PATHS = frozenset(
    {
        "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v0.5.md",
        "docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md",
        "docs/reference/prosjektbeskrivelse/forskning-og-soa-v0.5-kandidat.md",
        "site/tekstmanus.md",
        "site/innhold-kanban.md",
        "site/index.html",
    }
)
REQUIRED_PROTECTED_POLICY_PATHS = frozenset(
    {
        "governance/source-blocklist.json",
        "tools/source_guard.py",
        ".githooks/pre-commit",
    }
)


class RegistryError(ValueError):
    """The source blocklist is structurally invalid."""


@dataclass(frozen=True)
class CompiledEntry:
    entry_id: str
    status: str
    reason: str
    reopen_rule: str
    match_type: str
    terms: tuple[str, ...]
    groups: tuple[tuple[str, ...], ...]


@dataclass(frozen=True)
class CompiledRegistry:
    entries: tuple[CompiledEntry, ...]
    decision_owner: str
    excluded_path_prefixes: tuple[str, ...]
    excluded_paths: tuple[str, ...]
    guarded_paths: tuple[str, ...]
    active_paths: tuple[str, ...]
    protected_policy_paths: tuple[str, ...]


@dataclass(frozen=True)
class Hit:
    path: str
    line: int
    entry_id: str
    status: str
    matched: str
    reason: str
    reopen_rule: str
    context_hash: str


def normalize(value: str) -> str:
    """Normalize Unicode and whitespace for stable, case-insensitive matching."""

    value = unicodedata.normalize("NFKC", value).casefold()
    value = value.replace("–", "-").replace("—", "-").replace("−", "-")
    value = re.sub(r"\s*/\s*", "/", value)
    return " ".join(value.split())


def _require_string(entry: dict, field: str, entry_id: str) -> str:
    value = entry.get(field)
    if not isinstance(value, str) or not value.strip():
        raise RegistryError(f"{entry_id}: {field} must be a non-empty string")
    return value.strip()


def _require_string_list(value: object, field: str, entry_id: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise RegistryError(f"{entry_id}: {field} must be a list of strings")
    return [item.strip() for item in value if item.strip()]


def _require_top_level_string_list(data: dict, field: str) -> list[str]:
    value = data.get(field)
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
        raise RegistryError(f"{field} must be a list of non-empty strings")
    return [_normalize_path_label(item) for item in value]


def compile_registry(data: dict, *, enforce_required_policy: bool = True) -> CompiledRegistry:
    if not isinstance(data, dict):
        raise RegistryError("Registry root must be an object")
    if data.get("schema_version") != 1:
        raise RegistryError("schema_version must be 1")
    if data.get("decision_owner") != "Lars":
        raise RegistryError("decision_owner must be Lars")

    excluded_path_prefixes = _require_top_level_string_list(data, "excluded_path_prefixes")
    excluded_paths = _require_top_level_string_list(data, "excluded_paths")
    guarded_paths = _require_top_level_string_list(data, "guarded_paths")
    active_paths = _require_top_level_string_list(data, "active_paths")
    protected_policy_paths = _require_top_level_string_list(data, "protected_policy_paths")
    if enforce_required_policy:
        if set(guarded_paths) != REQUIRED_ACTIVE_PATHS or set(active_paths) != REQUIRED_ACTIVE_PATHS:
            raise RegistryError("guarded_paths and active_paths must contain the six required active files")
        if set(protected_policy_paths) != REQUIRED_PROTECTED_POLICY_PATHS:
            raise RegistryError("protected_policy_paths must contain the three required policy files")
    elif set(guarded_paths) != set(active_paths):
        raise RegistryError("guarded_paths and active_paths must contain the same files")

    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        raise RegistryError("entries must be a non-empty list")

    seen_ids: set[str] = set()
    compiled_entries: list[CompiledEntry] = []

    for raw_entry in entries:
        if not isinstance(raw_entry, dict):
            raise RegistryError("Every entry must be an object")
        missing = REQUIRED_ENTRY_FIELDS - raw_entry.keys()
        entry_id = str(raw_entry.get("id", "<missing-id>"))
        if missing:
            raise RegistryError(f"{entry_id}: missing fields: {', '.join(sorted(missing))}")
        if not re.fullmatch(r"SP-\d{2}", entry_id):
            raise RegistryError(f"{entry_id}: id must match SP-NN")
        if entry_id in seen_ids:
            raise RegistryError(f"Duplicate entry id: {entry_id}")
        seen_ids.add(entry_id)

        canonical_key = _require_string(raw_entry, "canonical_key", entry_id)
        normalized_title = raw_entry.get("normalized_title")
        if not isinstance(normalized_title, str):
            raise RegistryError(f"{entry_id}: normalized_title must be a string")
        status = _require_string(raw_entry, "status", entry_id)
        if status not in ALLOWED_STATUSES:
            raise RegistryError(f"{entry_id}: unsupported status {status}")
        reason = _require_string(raw_entry, "reason", entry_id)
        _require_string(raw_entry, "decision_date", entry_id)
        if _require_string(raw_entry, "decision_maker", entry_id) != "Lars":
            raise RegistryError(f"{entry_id}: decision_maker must be Lars")
        reopen_rule = _require_string(raw_entry, "reopen_rule", entry_id)
        if reopen_rule not in ALLOWED_REOPEN_RULES:
            raise RegistryError(f"{entry_id}: unsupported reopen_rule {reopen_rule}")
        _require_string_list(raw_entry.get("aliases"), "aliases", entry_id)
        _require_string_list(raw_entry.get("replacement"), "replacement", entry_id)

        identifiers = raw_entry.get("identifiers")
        if not isinstance(identifiers, dict):
            raise RegistryError(f"{entry_id}: identifiers must be an object")
        dois = _require_string_list(identifiers.get("doi", []), "identifiers.doi", entry_id)
        urls = _require_string_list(identifiers.get("url", []), "identifiers.url", entry_id)

        match = raw_entry.get("match")
        if not isinstance(match, dict) or match.get("type") not in ALLOWED_MATCH_TYPES:
            raise RegistryError(f"{entry_id}: unsupported match type")
        match_type = str(match["type"])

        terms: list[str] = []
        groups: list[tuple[str, ...]] = []
        if match_type == "any-identifier":
            candidates = [canonical_key]
            candidates.extend(raw_entry.get("aliases", []))
            candidates.append(normalized_title)
            candidates.extend(dois)
            candidates.extend(urls)
            terms = sorted({normalize(item) for item in candidates if normalize(str(item))})
            if not terms:
                raise RegistryError(f"{entry_id}: any-identifier needs at least one match term")
        else:
            raw_groups = match.get("groups")
            if not isinstance(raw_groups, list) or len(raw_groups) < 2:
                raise RegistryError(f"{entry_id}: relationship match needs at least two groups")
            for index, raw_group in enumerate(raw_groups):
                values = _require_string_list(raw_group, f"match.groups[{index}]", entry_id)
                normalized = tuple(sorted({normalize(item) for item in values if normalize(item)}))
                if not normalized:
                    raise RegistryError(f"{entry_id}: match group {index} is empty")
                groups.append(normalized)

        compiled_entries.append(
            CompiledEntry(
                entry_id=entry_id,
                status=status,
                reason=reason,
                reopen_rule=reopen_rule,
                match_type=match_type,
                terms=tuple(terms),
                groups=tuple(groups),
            )
        )

    if enforce_required_policy and seen_ids != REQUIRED_ENTRY_IDS:
        missing_ids = sorted(REQUIRED_ENTRY_IDS - seen_ids)
        extra_ids = sorted(seen_ids - REQUIRED_ENTRY_IDS)
        raise RegistryError(f"Registry must contain exactly SP-01..SP-11; missing={missing_ids}, extra={extra_ids}")

    return CompiledRegistry(
        entries=tuple(compiled_entries),
        decision_owner="Lars",
        excluded_path_prefixes=tuple(excluded_path_prefixes),
        excluded_paths=tuple(excluded_paths),
        guarded_paths=tuple(guarded_paths),
        active_paths=tuple(active_paths),
        protected_policy_paths=tuple(protected_policy_paths),
    )


def load_registry(path: Path) -> CompiledRegistry:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RegistryError(f"Could not read registry {path}: {exc}") from exc
    return compile_registry(data)


def _paragraphs(text: str) -> Iterable[tuple[int, str]]:
    lines = text.splitlines()
    start = 0
    buffer: list[str] = []
    for index, line in enumerate(lines, start=1):
        if line.strip():
            if not buffer:
                start = index
            buffer.append(line)
        elif buffer:
            yield start, "\n".join(buffer)
            buffer = []
    if buffer:
        yield start, "\n".join(buffer)


def _make_hit(label: str, line: int, entry: CompiledEntry, matched: str, context: str) -> Hit:
    context_hash = hashlib.sha256(normalize(context).encode("utf-8")).hexdigest()
    return Hit(
        path=label,
        line=line,
        entry_id=entry.entry_id,
        status=entry.status,
        matched=matched,
        reason=entry.reason,
        reopen_rule=entry.reopen_rule,
        context_hash=context_hash,
    )


def scan_text(
    label: str,
    text: str,
    registry: CompiledRegistry,
    *,
    line_offset: int = 0,
) -> list[Hit]:
    hits: list[Hit] = []

    for entry in registry.entries:
        if entry.match_type == "any-identifier":
            for line_number, line in enumerate(text.splitlines(), start=1):
                normalized_line = normalize(line)
                matched = next((term for term in entry.terms if term in normalized_line), None)
                if matched:
                    hits.append(_make_hit(label, line_offset + line_number, entry, matched, line))
        else:
            for paragraph_line, paragraph in _paragraphs(text):
                normalized_paragraph = normalize(paragraph)
                group_matches = [
                    next((term for term in group if term in normalized_paragraph), None)
                    for group in entry.groups
                ]
                if all(group_matches):
                    hits.append(
                        _make_hit(
                            label,
                            line_offset + paragraph_line,
                            entry,
                            " + ".join(str(item) for item in group_matches),
                            paragraph,
                        )
                    )

    return hits


def _repo_relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _normalize_path_label(value: str) -> str:
    normalized = value.replace("\\", "/")
    return normalized[2:] if normalized.startswith("./") else normalized


def is_excluded(relative_path: str, registry: CompiledRegistry) -> bool:
    normalized_path = _normalize_path_label(relative_path)
    if normalized_path in registry.excluded_paths:
        return True
    return any(
        normalized_path.startswith(_normalize_path_label(prefix))
        for prefix in registry.excluded_path_prefixes
    )


def is_guarded(relative_path: str, registry: CompiledRegistry) -> bool:
    return _normalize_path_label(relative_path) in registry.guarded_paths


def _iter_files(paths: Sequence[Path]) -> Iterable[Path]:
    seen: set[Path] = set()
    for path in paths:
        if path.is_file():
            resolved = path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                yield path
        elif path.is_dir():
            for candidate in sorted(path.rglob("*")):
                if candidate.is_file() and candidate.suffix.casefold() in TEXT_EXTENSIONS:
                    resolved = candidate.resolve()
                    if resolved not in seen:
                        seen.add(resolved)
                        yield candidate
        else:
            raise OSError(f"Path does not exist: {path}")


def scan_paths(
    paths: Sequence[Path],
    registry: CompiledRegistry,
    *,
    respect_exclusions: bool = False,
) -> tuple[list[Hit], list[str]]:
    hits: list[Hit] = []
    scanned: list[str] = []
    for path in _iter_files(paths):
        relative_path = _repo_relative(path)
        if respect_exclusions and is_excluded(relative_path, registry):
            continue
        text = path.read_text(encoding="utf-8-sig")
        scanned.append(relative_path)
        hits.extend(scan_text(relative_path, text, registry))
    return hits, scanned


def _git_output(args: Sequence[str], *, allow_failure: bool = False) -> str | None:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        if allow_failure:
            return None
        raise OSError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def _hit_fingerprint(hit: Hit) -> tuple[str, str, str]:
    return hit.entry_id, hit.matched, hit.context_hash


def new_hits_against_baseline(baseline_hits: Sequence[Hit], candidate_hits: Sequence[Hit]) -> list[Hit]:
    remaining = Counter(_hit_fingerprint(hit) for hit in baseline_hits)
    new_hits: list[Hit] = []
    for hit in candidate_hits:
        fingerprint = _hit_fingerprint(hit)
        if remaining[fingerprint]:
            remaining[fingerprint] -= 1
        else:
            new_hits.append(hit)
    return new_hits


def _policy_lock_hit(path: str) -> Hit:
    return Hit(
        path=path,
        line=1,
        entry_id="POLICY-LOCK",
        status="lars-approval-required",
        matched=path,
        reason="Source Guard policy files cannot be changed without Lars' explicit approval.",
        reopen_rule="manual-only",
        context_hash=hashlib.sha256(path.encode("utf-8")).hexdigest(),
    )


def scan_staged(registry: CompiledRegistry) -> tuple[list[Hit], list[str]]:
    names_output = _git_output(["diff", "--cached", "--name-only", "--diff-filter=ACMR", "--"])
    staged_paths = [_normalize_path_label(line) for line in (names_output or "").splitlines() if line]

    hits: list[Hit] = []
    scanned: list[str] = []
    for path in staged_paths:
        if path in registry.protected_policy_paths:
            existed_in_head = _git_output(["cat-file", "-e", f"HEAD:{path}"], allow_failure=True) is not None
            if existed_in_head:
                hits.append(_policy_lock_hit(path))

        if not is_guarded(path, registry):
            continue

        candidate_text = _git_output(["show", f":{path}"])
        if candidate_text is None:
            continue
        baseline_text = _git_output(["show", f"HEAD:{path}"], allow_failure=True) or ""
        baseline_hits = scan_text(path, baseline_text, registry)
        candidate_hits = scan_text(path, candidate_text, registry)
        hits.extend(new_hits_against_baseline(baseline_hits, candidate_hits))
        scanned.append(path)

    return hits, sorted(set(scanned))


def _path_from_hit(hit: Hit) -> Path:
    path = Path(hit.path)
    return path if path.is_absolute() else REPO_ROOT / path


def quarantine_hits(hits: Sequence[Hit], quarantine_root: Path) -> Path | None:
    source_paths = sorted({_path_from_hit(hit).resolve() for hit in hits if _path_from_hit(hit).is_file()})
    if not source_paths:
        return None

    digest_input = "\n".join(str(path) for path in source_paths).encode("utf-8")
    batch_hash = hashlib.sha256(digest_input).hexdigest()[:10]
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    batch_dir = quarantine_root / f"{timestamp}-{batch_hash}"
    batch_dir.mkdir(parents=True, exist_ok=False)

    files: list[dict] = []
    for source_path in source_paths:
        content_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
        destination = batch_dir / f"{content_hash[:12]}--{source_path.name}"
        shutil.copy2(source_path, destination)
        files.append(
            {
                "original_path": str(source_path),
                "quarantine_copy": str(destination),
                "bytes": source_path.stat().st_size,
                "sha256": content_hash,
            }
        )

    manifest = {
        "status": "QUARANTINED-COPY",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "decision_owner": "Lars",
        "originals_preserved": True,
        "files": files,
        "hits": [asdict(hit) for hit in hits],
    }
    manifest_path = batch_dir / "manifest.json"
    _write_report(manifest_path, manifest)
    return manifest_path


def _report_payload(
    hits: Sequence[Hit],
    scanned: Sequence[str],
    *,
    quarantine_manifest: Path | None = None,
) -> dict:
    return {
        "result": "BLOCK" if hits else "PASS",
        "decision_owner": "Lars",
        "scanned_files": list(scanned),
        "hit_count": len(hits),
        "quarantine_manifest": str(quarantine_manifest) if quarantine_manifest else None,
        "hits": [asdict(hit) for hit in hits],
    }


def _write_report(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _print_report(payload: dict, *, as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    print(f"SOURCE_GUARD={payload['result']} hits={payload['hit_count']}")
    for hit in payload["hits"]:
        print(
            f"{hit['path']}:{hit['line']}: {hit['entry_id']} "
            f"[{hit['status']}] matched={hit['matched']!r} "
            f"reopen={hit['reopen_rule']}"
        )
        print(f"  {hit['reason']}")
    if payload["hits"]:
        if payload.get("quarantine_manifest"):
            print(f"Quarantine manifest: {payload['quarantine_manifest']}")
        print("Blocked material is not authorized for active use. Only Lars can authorize reopening.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-registry", help="Validate the blocklist schema")
    validate.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)

    scan = subparsers.add_parser("scan", help="Scan files or staged additions")
    scan.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    scan.add_argument("--path", action="append", type=Path, default=[])
    scan.add_argument("--active", action="store_true", help="Scan configured active paths")
    scan.add_argument("--staged", action="store_true", help="Compare staged guarded files with HEAD")
    scan.add_argument("--report", type=Path, help="Write a JSON audit report")
    scan.add_argument(
        "--quarantine-dir",
        type=Path,
        default=REPO_ROOT / ".scratch" / "source-guard" / "quarantine",
        help="Copy blocked explicit inputs and a manifest here",
    )
    scan.add_argument("--json", action="store_true", help="Print JSON to stdout")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        registry = load_registry(args.registry)
        if args.command == "validate-registry":
            print(f"SOURCE_GUARD_REGISTRY=PASS entries={len(registry.entries)} owner=Lars")
            return 0

        if not args.path and not args.active and not args.staged:
            parser.error("scan requires --path, --active, or --staged")

        hits: list[Hit] = []
        scanned: list[str] = []
        quarantine_manifest: Path | None = None
        if args.path:
            path_hits, path_scanned = scan_paths(args.path, registry, respect_exclusions=False)
            hits.extend(path_hits)
            scanned.extend(path_scanned)
            if path_hits:
                quarantine_manifest = quarantine_hits(path_hits, args.quarantine_dir)
        if args.active:
            active_paths = [REPO_ROOT / path for path in registry.active_paths]
            active_hits, active_scanned = scan_paths(active_paths, registry, respect_exclusions=False)
            hits.extend(active_hits)
            scanned.extend(active_scanned)
        if args.staged:
            staged_hits, staged_scanned = scan_staged(registry)
            hits.extend(staged_hits)
            scanned.extend(staged_scanned)

        payload = _report_payload(
            hits,
            sorted(set(scanned)),
            quarantine_manifest=quarantine_manifest,
        )
        if args.report:
            _write_report(args.report, payload)
        _print_report(payload, as_json=args.json)
        return 1 if hits else 0
    except (RegistryError, OSError, UnicodeError, ValueError) as exc:
        print(f"SOURCE_GUARD=ERROR {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
