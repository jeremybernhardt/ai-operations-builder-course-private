from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


scanner = load_module("reliability_scan", ROOT / "scripts/reliability_scan.py")
packager = load_module("package_bundle", ROOT / "scripts/package_bundle.py")


class ReliabilityScanTests(unittest.TestCase):
    def copy_course(self, destination: Path) -> None:
        shutil.copytree(
            ROOT,
            destination,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(
                ".git", ".next", ".sites-runtime", ".wrangler", "__pycache__", "dist", "node_modules", "*.zip"
            ),
        )

    def test_canary_source_text_is_never_emitted(self) -> None:
        canary = "CANARY_PRIVATE_SOURCE_42f78b9d"
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            (temp_root / "ordinary.md").write_text(canary, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/reliability_scan.py"), "--root", str(temp_root)],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertNotIn(canary, result.stdout)
        self.assertNotIn(canary, result.stderr)

    def test_inventory_digest_changes_without_returning_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            target = temp_root / "ordinary.md"
            target.write_text("first private value", encoding="utf-8")
            first = scanner.scan_inventory(temp_root)
            target.write_text("second private value", encoding="utf-8")
            second = scanner.scan_inventory(temp_root)
        self.assertNotEqual(first["repository_digest_sha256"], second["repository_digest_sha256"])
        self.assertNotIn("first private value", scanner.serialize_report({"inventory": first}))
        self.assertNotIn("second private value", scanner.serialize_report({"inventory": second}))

    def test_full_report_is_bounded(self) -> None:
        output = scanner.serialize_report(scanner.build_report(ROOT), pretty=True)
        self.assertLessEqual(len(output.encode("utf-8")), scanner.MAX_OUTPUT_BYTES)

    def test_excel_lock_file_is_excluded_from_packages(self) -> None:
        self.assertTrue(packager.is_transient_lock_file(Path("student/~$example.xlsx")))
        self.assertFalse(packager.is_transient_lock_file(Path("student/example.xlsx")))
        self.assertTrue(packager.is_binary_workbook(Path("student/example.xlsx")))
        self.assertFalse(packager.should_include(ROOT / ".codex-m05l3-verify.mjs"))
        self.assertTrue(scanner.is_excluded(ROOT / ".codex-m05l3-verify.mjs", ROOT))

    def test_workbook_contents_are_not_read_by_reliability_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            workbook = temp_root / "fixture.xlsx"
            workbook.write_bytes(b"synthetic workbook placeholder")
            inventory = scanner.scan_inventory(temp_root)
        self.assertEqual(inventory["workbook_files_metadata_only"], 1)
        self.assertEqual(inventory["text_files_scanned"], 0)

    def test_critical_quality_boundaries_pass_without_source_output(self) -> None:
        report = scanner.build_report(ROOT)
        by_id = {check["id"]: check["status"] for check in report["checks"]}
        required = {
            "critical_course_facts",
            "prerequisite_evidence",
            "assistance_and_mastery_boundary",
            "scope_and_next_action_boundary",
            "approved_reliability_teaching_decisions",
            "limitations_boundary",
        }
        self.assertTrue(all(by_id.get(check_id) == "pass" for check_id in required))

    def test_unverified_recovery_artifact_does_not_advance_progress(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory) / "course"
            self.copy_course(temp_root)
            state_before = (temp_root / "COURSE_STATE.json").read_bytes()
            progress_before = (temp_root / "PROGRESS.json").read_bytes()
            recovered = temp_root / "student" / "M0.5-L4_RECOVERED_ANSWER.md"
            recovered.write_text("unverified learner recovery canary", encoding="utf-8")
            report = scanner.build_report(temp_root)
            self.assertEqual(state_before, (temp_root / "COURSE_STATE.json").read_bytes())
            self.assertEqual(progress_before, (temp_root / "PROGRESS.json").read_bytes())
            self.assertEqual(report["status"], "pass")

    def test_critical_state_conflict_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory) / "course"
            self.copy_course(temp_root)
            state_path = temp_root / "COURSE_STATE.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["current_checkpoint_id"] = "CONFLICT-CHECKPOINT"
            state_path.write_text(json.dumps(state), encoding="utf-8")
            report = scanner.build_report(temp_root)
        failures = {failure["code"] for failure in report["failures"]}
        self.assertIn("CRITICAL_COURSE_FACTS", failures)


if __name__ == "__main__":
    unittest.main()
