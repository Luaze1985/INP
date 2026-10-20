"""Regression tests for the safe review harness. Run: python -m unittest discover -s tests -p 'test_soknadsteam.py'"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "soknadsteam.py"
SPEC = importlib.util.spec_from_file_location("soknadsteam", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        (self.repo / "AGENTS.md").write_text("Rules\n", encoding="utf-8")
        (self.repo / "application.md").write_text("Draft v1\n", encoding="utf-8")

    def test_init_is_only_scratch_and_roles_not_run(self):
        MODULE.init(self.repo, "application.md", "test-001")
        path = self.repo / ".scratch/soknadsteam/test-001"
        self.assertTrue((path / "manifest.json").exists())
        data = json.loads((path / "findings/redteam.json").read_text(encoding="utf-8"))
        self.assertEqual(data["status"], "NOT_RUN")
        self.assertEqual(data["reviewed_roles"], [])
        self.assertEqual((self.repo / "application.md").read_text(encoding="utf-8"), "Draft v1\n")

    def test_unrun_roles_block(self):
        MODULE.init(self.repo, "application.md", "test-002")
        errors, _ = MODULE.validate(self.repo, "test-002")
        self.assertTrue(any("ikke fullført" in e for e in errors))

    def test_baseline_change_blocks(self):
        MODULE.init(self.repo, "application.md", "test-003")
        (self.repo / "application.md").write_text("Changed\n", encoding="utf-8")
        errors, _ = MODULE.validate(self.repo, "test-003")
        self.assertTrue(any("Baseline endret" in e for e in errors))

    def test_traversal_blocked(self):
        with self.assertRaises(MODULE.ReviewError):
            MODULE.safe_relative(self.repo, "../secret.md")

    def test_invalid_finding_is_rejected(self):
        MODULE.init(self.repo, "application.md", "test-004")
        path = self.repo / ".scratch/soknadsteam/test-004/findings/research.json"
        data = {"role": "research", "status": "COMPLETED", "limitations": "Only one file",
                "findings": [{"id": "x", "priority": "P1"}]}
        path.write_text(json.dumps(data), encoding="utf-8")
        errors, _ = MODULE.validate(self.repo, "test-004")
        self.assertTrue(any("mangler" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
