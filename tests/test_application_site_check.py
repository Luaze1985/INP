from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "application_site_check", REPO_ROOT / "tools/application_site_check.py"
)
assert SPEC and SPEC.loader
application_site_check = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = application_site_check
SPEC.loader.exec_module(application_site_check)


class ApplicationSiteCheckTests(unittest.TestCase):
    def test_active_manuscript_excludes_change_history(self) -> None:
        source = """# Manus\n## Seksjon 1 - Intro\nAktiv tekst.\n## Endringslogg\n32 % er tatt ut.\n"""
        active = application_site_check.active_manuscript(source)
        self.assertIn("Aktiv tekst", active)
        self.assertNotIn("32 %", active)

    def test_html_parser_includes_metadata_and_alt_text(self) -> None:
        source = """<meta name="description" content="Offentlig beskrivelse">
        <style>hemmelig</style><img alt="Synlig alternativ"><p>Brødtekst</p>"""
        text = application_site_check.html_to_text(source)
        self.assertIn("Offentlig beskrivelse", text)
        self.assertIn("Synlig alternativ", text)
        self.assertIn("Brødtekst", text)
        self.assertNotIn("hemmelig", text)

    def test_compare_flags_unsupported_number(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            app = root / "app.md"
            manuscript = root / "manus.md"
            website = root / "index.html"
            app.write_text("Prosjektet tester en modell.", encoding="utf-8")
            manuscript.write_text(
                "## Seksjon 1 - Intro\nProsjektet tester en modell.", encoding="utf-8"
            )
            website.write_text(
                "<p>Prosjektet tester en modell. Effekten er 32 %.</p>", encoding="utf-8"
            )
            report = application_site_check.compare(
                app, manuscript, website, minimum_overlap=0
            )
            unsupported = [
                finding
                for finding in report.findings
                if finding.check == "unsupported-number-website"
            ]
            self.assertEqual([finding.value for finding in unsupported], ["32 %"])

    def test_compare_flags_number_in_manuscript_but_not_application(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            app = root / "app.md"
            manuscript = root / "manus.md"
            website = root / "index.html"
            app.write_text("Prosjektet tester en modell.", encoding="utf-8")
            manuscript.write_text(
                "## Seksjon 1 - Intro\nForventet effekt er 11,7 %.", encoding="utf-8"
            )
            website.write_text("<p>Prosjektet tester en modell.</p>", encoding="utf-8")
            report = application_site_check.compare(
                app, manuscript, website, minimum_overlap=0
            )
            unsupported = [
                finding
                for finding in report.findings
                if finding.check == "unsupported-number-manuscript"
            ]
            self.assertEqual([finding.value for finding in unsupported], ["11,7 %"])

    def test_compare_accepts_supported_number_and_matching_copy(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            app = root / "app.md"
            manuscript = root / "manus.md"
            website = root / "index.html"
            copy = "Prosjektet omfatter 68 359 bedrifter og tester en modell."
            app.write_text(copy, encoding="utf-8")
            manuscript.write_text("## Seksjon 1 - Intro\n" + copy, encoding="utf-8")
            website.write_text(f"<p>{copy}</p>", encoding="utf-8")
            report = application_site_check.compare(
                app, manuscript, website, minimum_overlap=0.5
            )
            self.assertEqual(report.blocking_count, 0)

    def test_low_overlap_is_blocking(self) -> None:
        overlap = application_site_check.shingle_overlap(
            "Dette er teksten som faktisk skal publiseres på nettsiden.",
            "Dette er en helt annen og gammel tekst uten samme innhold.",
        )
        self.assertLess(overlap, 0.55)


if __name__ == "__main__":
    unittest.main()
