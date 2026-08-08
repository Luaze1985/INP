import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import source_guard  # noqa: E402


def sample_registry() -> dict:
    return {
        "schema_version": 1,
        "decision_owner": "Lars",
        "excluded_path_prefixes": ["governance/", "docs/sintef/", "tests/"],
        "excluded_paths": [],
        "guarded_paths": ["site/example.md"],
        "active_paths": ["site/example.md"],
        "protected_policy_paths": ["governance/source-blocklist.json"],
        "entries": [
            {
                "id": "SP-01",
                "canonical_key": "Wiik2025",
                "aliases": ["SINTEF Notat 57"],
                "normalized_title": "Kostnadseffekten av klimatiltak i byggenæringen",
                "identifiers": {"doi": [], "url": ["https://example.com/wiik.pdf"]},
                "status": "blocked-original-required",
                "reason": "Original og uavhengighet må kontrolleres.",
                "decision_date": "2026-08-03",
                "decision_maker": "Lars",
                "replacement": [],
                "reopen_rule": "original-required",
                "match": {"type": "any-identifier"},
            },
            {
                "id": "SP-02",
                "canonical_key": "Mecca2023",
                "aliases": [],
                "normalized_title": "Assessing the sustainable development",
                "identifiers": {"doi": ["10.1002/mcda.1818"], "url": []},
                "status": "blocked-original-required",
                "reason": "Detaljpåstander krever original.",
                "decision_date": "2026-08-03",
                "decision_maker": "Lars",
                "replacement": [],
                "reopen_rule": "original-required",
                "match": {"type": "any-identifier"},
            },
            {
                "id": "SP-03",
                "canonical_key": "BjorheimWrongRelation",
                "aliases": [],
                "normalized_title": "",
                "identifiers": {"doi": [], "url": []},
                "status": "retired-relationship",
                "reason": "Bjørheim kan ikke bære BDO, UNION eller ombruk.",
                "decision_date": "2026-08-03",
                "decision_maker": "Lars",
                "replacement": [],
                "reopen_rule": "manual-only",
                "match": {
                    "type": "all-groups-in-paragraph",
                    "groups": [["Bjørheim2026"], ["BDO", "UNION", "ombruk"]],
                },
            },
        ],
    }


class RegistryTests(unittest.TestCase):
    def test_registry_requires_unique_ids(self) -> None:
        registry = sample_registry()
        registry["entries"].append(dict(registry["entries"][0]))
        with self.assertRaises(source_guard.RegistryError):
            source_guard.compile_registry(registry, enforce_required_policy=False)

    def test_registry_requires_lars_as_decision_owner(self) -> None:
        registry = sample_registry()
        registry["decision_owner"] = "Agent"
        with self.assertRaises(source_guard.RegistryError):
            source_guard.compile_registry(registry, enforce_required_policy=False)

    def test_registry_rejects_string_instead_of_path_list(self) -> None:
        registry = sample_registry()
        registry["guarded_paths"] = "site/example.md"
        with self.assertRaises(source_guard.RegistryError):
            source_guard.compile_registry(registry, enforce_required_policy=False)

    def test_registry_rejects_unknown_status(self) -> None:
        registry = sample_registry()
        registry["entries"][0]["status"] = "approved"
        with self.assertRaises(source_guard.RegistryError):
            source_guard.compile_registry(registry, enforce_required_policy=False)

    def test_real_policy_cannot_drop_entries_or_guarded_paths(self) -> None:
        registry_path = REPO_ROOT / "governance" / "source-blocklist.json"
        original = json.loads(registry_path.read_text(encoding="utf-8"))

        without_entry = json.loads(json.dumps(original))
        without_entry["entries"].pop()
        with self.assertRaises(source_guard.RegistryError):
            source_guard.compile_registry(without_entry)

        without_paths = json.loads(json.dumps(original))
        without_paths["guarded_paths"] = []
        without_paths["active_paths"] = []
        with self.assertRaises(source_guard.RegistryError):
            source_guard.compile_registry(without_paths)

        without_policy_lock = json.loads(json.dumps(original))
        without_policy_lock["protected_policy_paths"] = []
        with self.assertRaises(source_guard.RegistryError):
            source_guard.compile_registry(without_policy_lock)

    def test_every_real_block_entry_has_a_working_match(self) -> None:
        registry = source_guard.load_registry(REPO_ROOT / "governance" / "source-blocklist.json")
        examples = {
            "SP-01": "[Wiik2025]",
            "SP-02": "[SA2018]",
            "SP-03": "[An2021]",
            "SP-04": "[Billio_SAFE261]",
            "SP-05": "Harerusten2022 brukes som kilde for 2,2 mrd.",
            "SP-06": "[Multiconsult2023DiBK]",
            "SP-07": "KD2024-Asplan",
            "SP-08": "[Bjørheim2026]",
            "SP-09": "https://doi.org/10.1002/mcda.1818",
            "SP-10": "[Ciroth2016]",
            "SP-11": "Bjørheim2026 brukes som samlekilde for BDO og UNION.",
        }
        self.assertEqual({entry.entry_id for entry in registry.entries}, set(examples))
        for entry_id, text in examples.items():
            with self.subTest(entry_id=entry_id):
                hit_ids = {hit.entry_id for hit in source_guard.scan_text("candidate.md", text, registry)}
                self.assertIn(entry_id, hit_ids)

        alias_examples = {
            "SP-01": "Marianne Kjendseth Wiik",
            "SP-02": "Samfunnsøkonomisk analyse",
            "SP-08": "Bisnode / Byggeindustrien / SINTEF",
            "SP-10": "Ciroth et al. 2016",
        }
        for entry_id, text in alias_examples.items():
            with self.subTest(alias=entry_id):
                hit_ids = {hit.entry_id for hit in source_guard.scan_text("candidate.md", text, registry)}
                self.assertIn(entry_id, hit_ids)

        ciroth_doi_hits = source_guard.scan_text(
            "candidate.md", "https://doi.org/10.1007/s11367-013-0670-5", registry
        )
        self.assertIn("SP-10", {hit.entry_id for hit in ciroth_doi_hits})


class MatchingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.compiled = source_guard.compile_registry(sample_registry(), enforce_required_policy=False)

    def test_detects_key_case_insensitively(self) -> None:
        hits = source_guard.scan_text("candidate.md", "Vi bruker [WIIK2025] som kilde.", self.compiled)
        self.assertEqual([hit.entry_id for hit in hits], ["SP-01"])

    def test_detects_alias(self) -> None:
        hits = source_guard.scan_text("candidate.md", "Grunnlaget er SINTEF Notat 57.", self.compiled)
        self.assertEqual([hit.entry_id for hit in hits], ["SP-01"])

    def test_detects_doi_inside_url(self) -> None:
        text = "Kilde: https://doi.org/10.1002/mcda.1818"
        hits = source_guard.scan_text("candidate.md", text, self.compiled)
        self.assertEqual([hit.entry_id for hit in hits], ["SP-02"])

    def test_detects_registered_url(self) -> None:
        text = "Kilde: https://example.com/wiik.pdf"
        hits = source_guard.scan_text("candidate.md", text, self.compiled)
        self.assertEqual([hit.entry_id for hit in hits], ["SP-01"])

    def test_detects_retired_relationship_in_same_paragraph(self) -> None:
        text = "Bjørheim2026 brukes her som støtte for BDO-marginen og UNION-tallet."
        hits = source_guard.scan_text("candidate.md", text, self.compiled)
        self.assertEqual([hit.entry_id for hit in hits], ["SP-03"])

    def test_relationship_does_not_match_across_paragraphs(self) -> None:
        text = "Bjørheim2026 omtaler konkurser.\n\nBDO omtales i et annet kildespor."
        hits = source_guard.scan_text("candidate.md", text, self.compiled)
        self.assertEqual(hits, [])

    def test_safe_replacement_text_passes(self) -> None:
        text = "BDO og UNION behandles som separate kildespor."
        hits = source_guard.scan_text("candidate.md", text, self.compiled)
        self.assertEqual(hits, [])

    def test_new_relationship_is_detected_using_full_candidate_context(self) -> None:
        baseline = "Bjørheim2026 omtaler konkurser."
        candidate = "Bjørheim2026 omtaler konkurser og brukes også for BDO-marginen."
        baseline_hits = source_guard.scan_text("site/example.md", baseline, self.compiled)
        candidate_hits = source_guard.scan_text("site/example.md", candidate, self.compiled)
        new_hits = source_guard.new_hits_against_baseline(baseline_hits, candidate_hits)
        self.assertIn("SP-03", {hit.entry_id for hit in new_hits})

    def test_existing_unchanged_hit_is_not_reported_as_new(self) -> None:
        text = "Vi bruker [Wiik2025] som kilde."
        baseline_hits = source_guard.scan_text("site/example.md", text, self.compiled)
        candidate_hits = source_guard.scan_text("site/example.md", text, self.compiled)
        self.assertEqual(source_guard.new_hits_against_baseline(baseline_hits, candidate_hits), [])


class CliTests(unittest.TestCase):
    def test_cli_returns_one_for_blocked_input_and_writes_json_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            candidate_path = tmp_path / "candidate.md"
            report_path = tmp_path / "report.json"
            candidate_path.write_text("Bruk [Wiik2025].", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "tools" / "source_guard.py"),
                    "scan",
                    "--path",
                    str(candidate_path),
                    "--report",
                    str(report_path),
                    "--quarantine-dir",
                    str(tmp_path / "quarantine"),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 1)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["result"], "BLOCK")
            self.assertEqual(report["hits"][0]["entry_id"], "SP-01")
            manifest_path = Path(report["quarantine_manifest"])
            self.assertTrue(manifest_path.is_file())
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertTrue(manifest["originals_preserved"])

    def test_explicit_scratch_intake_is_not_excluded(self) -> None:
        scratch_root = REPO_ROOT / ".scratch"
        scratch_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch_root) as tmp:
            candidate = Path(tmp) / "intake.txt"
            candidate.write_text("[Wiik2025]", encoding="utf-8")
            registry = source_guard.compile_registry(sample_registry(), enforce_required_policy=False)
            hits, scanned = source_guard.scan_paths([candidate], registry, respect_exclusions=False)
            self.assertEqual([hit.entry_id for hit in hits], ["SP-01"])
            self.assertEqual(len(scanned), 1)


if __name__ == "__main__":
    unittest.main()
