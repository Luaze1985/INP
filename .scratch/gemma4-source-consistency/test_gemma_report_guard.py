import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from gemma_report_guard import audit_report


class GemmaReportGuardTests(unittest.TestCase):
    def write(self, root: Path, name: str, text: str) -> Path:
        path = root / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_flags_non_actionable_false_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidates = self.write(
                root,
                "candidates.md",
                "1. Produkt/nettside-materiale finnes likevel i repoet\n"
                "- README sier A\n\n"
                "2. INDEX.yml dekker bare deler av repoet\n"
                "- INDEX sier B\n",
            )
            report = self.write(
                root,
                "report.json",
                json.dumps(
                    {
                        "ok": False,
                        "flagged_rows": [],
                        "reason": "Scope creep",
                        "recommended_action": "Cleanup",
                    }
                ),
            )

            result = audit_report(candidates, report)

            self.assertFalse(result["ok"])
            self.assertEqual(result["issues"][0]["code"], "non_actionable_false_report")

    def test_accepts_flagged_rows_that_match_candidate_titles(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidates = self.write(
                root,
                "candidates.md",
                "1. SA2018 statusdrift\n"
                "- context\n\n"
                "2. Mecca2023 statusdrift\n"
                "- context\n",
            )
            report = self.write(
                root,
                "report.json",
                json.dumps(
                    {
                        "ok": False,
                        "flagged_rows": [
                            {
                                "item": "SA2018 statusdrift",
                                "reason": "conflict",
                                "recommended_action": "fix",
                            }
                        ],
                        "reason": "one conflict",
                        "recommended_action": "fix",
                    }
                ),
            )

            result = audit_report(candidates, report)

            self.assertTrue(result["ok"])
            self.assertEqual(result["issues"], [])

    def test_flags_rows_that_do_not_match_candidate_titles(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidates = self.write(root, "candidates.md", "1. SA2018 statusdrift\n- context\n")
            report = self.write(
                root,
                "report.json",
                json.dumps(
                    {
                        "ok": False,
                        "flagged_rows": [
                            {
                                "item": "Unknown drift",
                                "reason": "conflict",
                                "recommended_action": "fix",
                            }
                        ],
                        "reason": "one conflict",
                        "recommended_action": "fix",
                    }
                ),
            )

            result = audit_report(candidates, report)

            self.assertFalse(result["ok"])
            self.assertEqual(result["issues"][0]["code"], "unknown_flagged_item")

    def test_cli_returns_nonzero_for_non_actionable_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidates = self.write(root, "candidates.md", "1. Repo drift\n- context\n")
            report = self.write(
                root,
                "report.json",
                json.dumps(
                    {
                        "ok": False,
                        "flagged_rows": [],
                        "reason": "drift",
                        "recommended_action": "fix",
                    }
                ),
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(Path(__file__).with_name("gemma_report_guard.py")),
                    str(candidates),
                    str(report),
                ],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("non_actionable_false_report", result.stdout)


if __name__ == "__main__":
    unittest.main()
