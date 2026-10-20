#!/usr/bin/env python3
"""Safe, stdlib-only review harness: prepares briefs and validates real agent outputs.

No LLM calls, no application rewrites, no automatic approvals.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROLES = ("eligibility", "research", "evidence", "delivery", "redteam")
ROLE_TITLES = {
    "eligibility": "Utlysning og søknadskrav",
    "research": "FoU og metode",
    "evidence": "Kilder, påstander og produktgrense",
    "delivery": "Partnere, økonomi og gjennomføring",
    "redteam": "Uavhengig red team (sist)",
}
REQUIRED = {
    "id", "priority", "surface", "location", "problem", "proposal",
    "acceptance_test", "owner", "confidence", "requires_human", "evidence",
}
PRIORITIES = {"P0", "P1", "P2"}
SURFACES = {"IPN", "KOBLINGSBOKS", "BOTH"}
CONFIDENCES = {"HIGH", "MEDIUM", "LOW"}
EVIDENCE_STATUSES = {"PRIMARY_VERIFIED", "INTERNAL", "UNVERIFIED"}
STATUSES = {"NOT_RUN", "COMPLETED", "BLOCKED"}


class ReviewError(ValueError):
    pass


def safe_relative(root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts or not relative.strip():
        raise ReviewError("Ugyldig relativ sti: " + relative)
    result = (root / rel).resolve()
    try:
        result.relative_to(root.resolve())
    except ValueError as exc:
        raise ReviewError("Sti peker utenfor repo: " + relative) from exc
    return result


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ReviewError("JSON-roten må være objekt: " + str(path))
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_dir(repo: Path, run_id: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{2,63}", run_id):
        raise ReviewError("Run-ID må være 3–64 tegn: bokstaver, tall, _ eller -")
    return safe_relative(repo, ".scratch/soknadsteam/" + run_id)


def inspect(repo: Path) -> int:
    print("Repo:", repo)
    paths = [
        "AGENTS.md", "CONTEXT.md", "INDEX.yml",
        "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v1.9.md",
        "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v2.0.md",
        "tools/source_guard.py", "tools/budget_validator.py",
    ]
    for path in paths:
        print(("FUNNET " if (repo / path).is_file() else "MANGLER"), path)
    index = (repo / "INDEX.yml")
    context = (repo / "CONTEXT.md")
    if index.is_file() and context.is_file():
        a = index.read_text(encoding="utf-8")
        b = context.read_text(encoding="utf-8-sig")
        if "v1.9.md: NYESTE" in a and "finpuss av v2.0" in b:
            print("BESLUTNINGSPORT: INDEX peker v1.9, CONTEXT omtaler v2.0.")
    print("Ingen filer endret. Velg søknadsfil eksplisitt ved init.")
    return 0


def init(repo: Path, application_file: str, run_id: str) -> int:
    app = safe_relative(repo, application_file)
    if not app.is_file():
        raise ReviewError("Søknadsfil finnes ikke: " + application_file)
    output = run_dir(repo, run_id)
    if output.exists():
        raise ReviewError("Run finnes allerede; overskrives ikke: " + str(output))
    (output / "briefings").mkdir(parents=True)
    (output / "findings").mkdir()
    manifest = {
        "schema": 1,
        "run_id": run_id,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "application_file": application_file,
        "application_sha256": sha256(app),
        "roles": list(ROLES),
        "state": "FROZEN_BASELINE",
        "note": "Roller NOT_RUN. Ingen modeller/agenter kjørt av dette verktøyet.",
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    for role in ROLES:
        (output / "briefings" / (role + ".md")).write_text(
            "# " + ROLE_TITLES[role] + "\n\n"
            "Les AGENTS.md, CONTEXT.md, INDEX.yml, valgt søknadsfil: "
            + application_file + "\n\n"
            "Les docs/agents/soknadsteam/ROLLER.md og FUNNFORMAT.md.\n"
            "Skriv bare din egen findings/" + role + ".json.\n"
            "Ikke påstå at andre roller er kjørt. Ingen endring av aktiv søknad.\n",
            encoding="utf-8",
        )
        placeholder = {
            "role": role,
            "status": "NOT_RUN",
            "limitations": "Ikke kjørt.",
            "findings": [],
        }
        if role == "redteam":
            placeholder["reviewed_roles"] = []
        (output / "findings" / (role + ".json")).write_text(
            json.dumps(placeholder, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    (output / "DECISIONS.md").write_text(
        "# Menneskelige beslutninger\n\n"
        "Ingen funn er godkjent. Fyll inn ID, ACCEPT/MODIFY/REJECT/DEFER, "
        "eier, dato, begrunnelse og eventuell PR etter faktisk review.\n",
        encoding="utf-8",
    )
    print("Opprettet", output)
    print("Alle fem roller er NOT_RUN; dette er bare briefinger og struktur.")
    return 0


def validate(repo: Path, run_id: str) -> tuple[list[str], list[dict]]:
    directory = run_dir(repo, run_id)
    errors: list[str] = []
    collected: list[dict] = []
    manifest_path = directory / "manifest.json"
    if not manifest_path.is_file():
        return ["Manifest mangler: " + str(manifest_path)], collected
    try:
        manifest = read_json(manifest_path)
        app = safe_relative(repo, manifest["application_file"])
        if not app.is_file() or sha256(app) != manifest["application_sha256"]:
            errors.append("Baseline endret eller mangler; frys nytt grunnlag.")
    except (KeyError, OSError, ValueError, TypeError) as exc:
        errors.append("Ugyldig manifest: " + str(exc))
    ids: set[str] = set()
    completed: set[str] = set()
    for role in ROLES:
        path = directory / "findings" / (role + ".json")
        if not path.is_file():
            errors.append(role + ": fil mangler")
            continue
        try:
            data = read_json(path)
        except (OSError, ValueError) as exc:
            errors.append(role + ": ugyldig JSON: " + str(exc))
            continue
        if data.get("role") != role:
            errors.append(role + ": feil role-felt")
        status = data.get("status")
        if status not in STATUSES:
            errors.append(role + ": ugyldig status")
        elif status != "COMPLETED":
            errors.append(role + ": ikke fullført (" + status + ")")
        else:
            completed.add(role)
        if not isinstance(data.get("limitations"), str) or not data["limitations"].strip():
            errors.append(role + ": limitations mangler")
        findings = data.get("findings")
        if not isinstance(findings, list):
            errors.append(role + ": findings må være liste")
            continue
        for number, finding in enumerate(findings, 1):
            tag = role + "/" + str(number)
            if not isinstance(finding, dict):
                errors.append(tag + ": funn må være objekt")
                continue
            missing = REQUIRED - set(finding)
            if missing:
                errors.append(tag + ": mangler " + ", ".join(sorted(missing)))
                continue
            if finding["priority"] not in PRIORITIES or finding["surface"] not in SURFACES:
                errors.append(tag + ": ugyldig priority/surface")
            if finding["confidence"] not in CONFIDENCES:
                errors.append(tag + ": ugyldig confidence")
            if finding["requires_human"] is not True:
                errors.append(tag + ": requires_human må være true")
            for field in ("id", "location", "problem", "proposal", "acceptance_test", "owner"):
                if not isinstance(finding[field], str) or not finding[field].strip():
                    errors.append(tag + ": tomt felt " + field)
            fid = finding["id"]
            if isinstance(fid, str):
                if fid in ids:
                    errors.append(tag + ": duplikat ID " + fid)
                ids.add(fid)
            evidence = finding["evidence"]
            if not isinstance(evidence, list) or not evidence:
                errors.append(tag + ": evidence må ha minst én kilde")
            else:
                for item in evidence:
                    if not isinstance(item, dict) or not isinstance(item.get("source"), str):
                        errors.append(tag + ": ugyldig kilde")
                        continue
                    source = item["source"]
                    if item.get("status") not in EVIDENCE_STATUSES:
                        errors.append(tag + ": ugyldig kildestatus")
                    if not isinstance(item.get("note"), str) or not item["note"].strip():
                        errors.append(tag + ": kilde mangler forklaring")
                    if source.startswith("https://"):
                        pass  # URL alene verifiseres aldri av dette verktøyet.
                    elif source.startswith("http://"):
                        errors.append(tag + ": krever https for ekstern kilde")
                    else:
                        try:
                            if not safe_relative(repo, source).is_file():
                                errors.append(tag + ": lokal kilde mangler: " + source)
                        except ReviewError as exc:
                            errors.append(tag + ": " + str(exc))
            collected.append({"role": role, **finding})
        if role == "redteam" and status == "COMPLETED":
            reviewed = data.get("reviewed_roles")
            if not isinstance(reviewed, list) or set(reviewed) != set(ROLES[:-1]):
                errors.append("redteam: reviewed_roles må dekke alle fire spesialister")
    if "redteam" in completed and not set(ROLES[:-1]).issubset(completed):
        errors.append("Red team kan ikke fullføres før alle spesialister er fullført")
    return errors, collected


def make_report(repo: Path, run_id: str, write: bool) -> int:
    errors, findings = validate(repo, run_id)
    lines = [
        "# Samlerapport – " + run_id, "",
        "Strukturell status: " + ("INCOMPLETE/BLOCK" if errors else "STRUCTURAL_PASS"),
        "Dette er IKKE faglig godkjenning eller bekreftelse på at kilder er sanne.",
        "", "## Feil og åpne porter", "",
    ]
    lines += ["- " + x for x in errors] if errors else ["- Ingen strukturelle feil."]
    lines += ["", "## Funn", ""]
    for item in sorted(findings, key=lambda x: (x.get("priority", "P9"), x.get("id", ""))):
        lines += [
            "### " + str(item.get("id", "?")) + " (" + str(item.get("priority", "?")) + ")",
            "Rolle: " + str(item["role"]),
            "Sted: " + str(item.get("location", "")),
            "Problem: " + str(item.get("problem", "")),
            "Forslag: " + str(item.get("proposal", "")),
            "Aksept: " + str(item.get("acceptance_test", "")),
            "Eier: " + str(item.get("owner", "")), "",
        ]
    lines += ["## Menneskelig port", "",
              "Krever eksplisitt godkjenning av kilde, budsjett, redline og eventuell PR.",
              "Ingen aktiv søknad er endret av dette verktøyet.", ""]
    output = "\n".join(lines)
    if write:
        destination = run_dir(repo, run_id) / "REPORT.md"
        destination.write_text(output, encoding="utf-8")
        print("Skrev", destination)
    else:
        print(output)
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("inspect", "init", "validate", "report"):
        p = sub.add_parser(name)
        p.add_argument("--repo", type=Path, default=Path("."))
        if name != "inspect":
            p.add_argument("--run-id", required=True)
        if name == "init":
            p.add_argument("--application-file", required=True)
        if name == "report":
            p.add_argument("--write", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()
    if not repo.is_dir():
        raise ReviewError("Repo-mappe finnes ikke: " + str(repo))
    if args.command == "inspect":
        return inspect(repo)
    if args.command == "init":
        return init(repo, args.application_file, args.run_id)
    if args.command == "validate":
        errors, findings = validate(repo, args.run_id)
        print("Funn:", len(findings), "Feil:", len(errors))
        for error in errors:
            print("BLOCK:", error)
        print("Kun strukturell QA; menneskelig kontroll kreves.")
        return 1 if errors else 0
    return make_report(repo, args.run_id, args.write)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ReviewError, OSError, ValueError, KeyError) as exc:
        print("BLOCK:", exc, file=sys.stderr)
        sys.exit(2)
