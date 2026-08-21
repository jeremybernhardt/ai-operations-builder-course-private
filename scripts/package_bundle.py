#!/usr/bin/env python3
"""Create and verify the durable source bundle."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_NAME = "AI_Operations_Builder_Course_Prototype_v2.0.5_M0.5-L1.zip"
OUTPUT = ROOT / BUNDLE_NAME
ARCHIVE_ROOT = "AI_Operations_Builder_Course_Prototype_v2.0.5_M0.5-L1"
EXCLUDED_PARTS = {
    ".git",
    ".sites-runtime",
    ".wrangler",
    ".next",
    "node_modules",
    "dist",
    "__pycache__",
}
EXCLUDED_ROOTS = {"examples"}


def should_include(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if path == OUTPUT or relative.parts[0] in EXCLUDED_ROOTS:
        return False
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return False
    if path.suffix in {".log", ".pyc", ".zip"}:
        return False
    return path.is_file()


def main() -> None:
    if OUTPUT.exists():
        OUTPUT.unlink()
    files = sorted(path for path in ROOT.rglob("*") if should_include(path))
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(ROOT)
            archive.write(path, f"{ARCHIVE_ROOT}/{relative.as_posix()}")

    with zipfile.ZipFile(OUTPUT) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise SystemExit(f"Bundle CRC check failed at {bad_member}")
        names = set(archive.namelist())
        required = {
            f"{ARCHIVE_ROOT}/COURSE_CONTRACT.md",
            f"{ARCHIVE_ROOT}/CURRICULUM_MAP.md",
            f"{ARCHIVE_ROOT}/COURSE_STATE.json",
            f"{ARCHIVE_ROOT}/PROGRESS.json",
            f"{ARCHIVE_ROOT}/CAPABILITY_EVIDENCE_LEDGER.md",
            f"{ARCHIVE_ROOT}/SESSION_HANDOFF.md",
            f"{ARCHIVE_ROOT}/NEXT_CHAT_PROMPT.md",
            f"{ARCHIVE_ROOT}/lesson/M0-L2_LOCAL_BRANCHES_MERGES_SAFE_RECOVERY.md",
            f"{ARCHIVE_ROOT}/evidence/LEARNER_CHECKPOINT_M0-C2.md",
            f"{ARCHIVE_ROOT}/lesson/M0-L3_GIT_IDENTITY_PRIVACY_GITHUB_READINESS.md",
            f"{ARCHIVE_ROOT}/evidence/LEARNER_CHECKPOINT_M0-C3.md",
            f"{ARCHIVE_ROOT}/lesson/M0-L4_PRIVATE_GITHUB_COURSE_REPOSITORY_FIRST_VERIFIED_PUSH.md",
            f"{ARCHIVE_ROOT}/evidence/LEARNER_CHECKPOINT_M0-C4.md",
            f"{ARCHIVE_ROOT}/lesson/M0.5-L1_DEFINING_OUTCOMES_CONSTRAINTS_DONE_CRITERIA.md",
            f"{ARCHIVE_ROOT}/student/M0.5-L1_EXPENSE_FILE_READINESS_BUILD_BRIEF.md",
            f"{ARCHIVE_ROOT}/evidence/LEARNER_CHECKPOINT_M0.5-C1.md",
            f"{ARCHIVE_ROOT}/evidence/RELEASE_CHECKS_v2.0.5.md",
            f"{ARCHIVE_ROOT}/evidence/RECONSTRUCTION_CHECK_v2.0.5.md",
            f"{ARCHIVE_ROOT}/AGENTS.md",
            f"{ARCHIVE_ROOT}/database/prototype.sqlite",
            f"{ARCHIVE_ROOT}/student/first_pass_acceptance.sql",
            f"{ARCHIVE_ROOT}/package-lock.json",
        }
        missing = required - names
        if missing:
            raise SystemExit(f"Bundle is missing required members: {sorted(missing)}")

    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(f"Created {OUTPUT.name} with {len(files)} files")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    print(f"SHA-256: {digest}")


if __name__ == "__main__":
    main()
