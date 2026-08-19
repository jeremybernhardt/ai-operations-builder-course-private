#!/usr/bin/env python3
"""Build the local SQLite database and read-only portal snapshots."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "project_task_reviews.csv"
DEFAULT_DATABASE = ROOT / "database" / "prototype.sqlite"
DEFAULT_GENERATED = ROOT / "app" / "generated"
DEFAULT_PUBLIC_ARTIFACTS = ROOT / "public" / "artifacts"

REQUIRED_FIELDS = [
    "review_id",
    "task_id",
    "expert_id",
    "task_type",
    "submission_attempt",
    "submitted_at",
    "reviewed_at",
    "review_status",
    "review_sequence",
    "guideline_version",
]
VALID_STATUSES = {"accepted", "revise", "rejected", ""}
PORTAL_ARTIFACTS = [
    "COURSE_CONTRACT.md",
    "CURRICULUM_MAP.md",
    "COURSE_STATE.json",
    "PROGRESS.json",
    "CAPABILITY_EVIDENCE_LEDGER.md",
    "LESSON_TEMPLATE.md",
    "PROJECT_SPEC.md",
    "METRIC_DICTIONARY.md",
    "DATA_DICTIONARY.md",
    "DECISION_LOG.md",
    "SESSION_HANDOFF.md",
    "NEXT_CHAT_PROMPT.md",
    "README.md",
    "MANIFEST.md",
]


def read_rows(csv_path: Path = CSV_PATH) -> list[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_FIELDS:
            raise ValueError(
                f"Unexpected CSV fields: {reader.fieldnames}; expected {REQUIRED_FIELDS}"
            )
        rows = list(reader)

    review_ids = [row["review_id"] for row in rows]
    if len(review_ids) != len(set(review_ids)):
        raise ValueError("review_id must be unique for every raw row")

    for index, row in enumerate(rows, start=2):
        if row["review_status"] not in VALID_STATUSES:
            raise ValueError(f"Invalid review_status on CSV row {index}")
        for field in ("submission_attempt", "review_sequence"):
            try:
                value = int(row[field])
            except ValueError as exc:
                raise ValueError(f"{field} must be an integer on CSV row {index}") from exc
            if value < 1:
                raise ValueError(f"{field} must be positive on CSV row {index}")
        if not row["task_id"] or not row["expert_id"]:
            raise ValueError(f"Required identifier missing on CSV row {index}")
    return rows


def build_database(rows: list[dict[str, str]], database_path: Path) -> None:
    database_path.parent.mkdir(parents=True, exist_ok=True)
    if database_path.exists():
        database_path.unlink()

    with sqlite3.connect(database_path) as connection:
        connection.executescript(
            """
            PRAGMA foreign_keys = ON;
            CREATE TABLE review_events (
                review_id TEXT PRIMARY KEY,
                task_id TEXT NOT NULL,
                expert_id TEXT NOT NULL,
                task_type TEXT NOT NULL,
                submission_attempt INTEGER NOT NULL CHECK (submission_attempt >= 1),
                submitted_at TEXT NOT NULL,
                reviewed_at TEXT,
                review_status TEXT CHECK (
                    review_status IN ('accepted', 'revise', 'rejected')
                    OR review_status IS NULL
                ),
                review_sequence INTEGER NOT NULL CHECK (review_sequence >= 1),
                guideline_version TEXT NOT NULL
            );
            CREATE INDEX idx_review_events_task_attempt
                ON review_events(task_id, submission_attempt, review_sequence);
            """
        )
        connection.executemany(
            """
            INSERT INTO review_events (
                review_id, task_id, expert_id, task_type, submission_attempt,
                submitted_at, reviewed_at, review_status, review_sequence,
                guideline_version
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    row["review_id"],
                    row["task_id"],
                    row["expert_id"],
                    row["task_type"],
                    int(row["submission_attempt"]),
                    row["submitted_at"],
                    row["reviewed_at"] or None,
                    row["review_status"] or None,
                    int(row["review_sequence"]),
                    row["guideline_version"],
                )
                for row in rows
            ],
        )
        connection.commit()


def build_quality_summary(rows: list[dict[str, str]]) -> dict[str, object]:
    logical_groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        key = (row["task_id"], row["submission_attempt"], row["review_sequence"])
        logical_groups[key].append(row)

    duplicate_groups = [
        {"task_id": key[0], "submission_attempt": int(key[1]), "review_sequence": int(key[2]), "row_count": len(group)}
        for key, group in logical_groups.items()
        if len(group) > 1
    ]
    missing_rows = [row for row in rows if not row["review_status"].strip()]
    reworked_rows = [row for row in rows if int(row["submission_attempt"]) > 1]
    affected_tasks = {
        *(item["task_id"] for item in duplicate_groups),
        *(row["task_id"] for row in missing_rows),
        *(row["task_id"] for row in reworked_rows),
    }
    status_counts = Counter(row["review_status"] or "missing" for row in rows)

    return {
        "schema_version": "2.0.0",
        "source": "data/project_task_reviews.csv",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "synthetic_data": True,
        "total_review_rows": len(rows),
        "distinct_tasks": len({row["task_id"] for row in rows}),
        "duplicate_logical_review_groups": len(duplicate_groups),
        "missing_outcome_rows": len(missing_rows),
        "reworked_submission_rows": len(reworked_rows),
        "tasks_requiring_policy_choice": len(affected_tasks),
        "status_counts_raw_rows": dict(sorted(status_counts.items())),
        "operator_note": "Resolve metric policy and data-quality treatment before treating the rate as decision-ready.",
    }


def build_progress_snapshot() -> dict[str, object]:
    with (ROOT / "PROGRESS.json").open(encoding="utf-8") as handle:
        progress = json.load(handle)
    with (ROOT / "COURSE_STATE.json").open(encoding="utf-8") as handle:
        state = json.load(handle)
    lesson = next(item for item in progress["lessons"] if item["lesson_id"] == state["current_lesson_id"])
    return {
        "schema_version": "2.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "PROGRESS.json",
        "source_progress_version": progress["progress_version"],
        "non_authoritative": True,
        "label": "Read-only mirror — canonical progress lives in PROGRESS.json",
        "lesson": lesson,
    }


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def copy_portal_artifacts(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for filename in PORTAL_ARTIFACTS:
        source = ROOT / filename
        if source.exists():
            shutil.copy2(source, destination / filename)
    shutil.copy2(CSV_PATH, destination / CSV_PATH.name)
    shutil.copy2(ROOT / "lesson" / "stages" / "01_define_metric.md", destination / "ACTIVE_CHECKPOINT.md")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--generated-dir", type=Path, default=DEFAULT_GENERATED)
    parser.add_argument("--public-artifacts", type=Path, default=DEFAULT_PUBLIC_ARTIFACTS)
    args = parser.parse_args()

    rows = read_rows()
    build_database(rows, args.database)
    quality = build_quality_summary(rows)
    progress = build_progress_snapshot()
    write_json(args.generated_dir / "data-quality-summary.json", quality)
    write_json(args.generated_dir / "progress-snapshot.json", progress)
    write_json(
        args.generated_dir / "data-preview.json",
        [
            {
                **row,
                "submission_attempt": int(row["submission_attempt"]),
                "review_sequence": int(row["review_sequence"]),
                "reviewed_at": row["reviewed_at"] or None,
                "review_status": row["review_status"] or None,
            }
            for row in rows
        ],
    )
    copy_portal_artifacts(args.public_artifacts)
    print(f"Prepared {len(rows)} synthetic rows in {args.database}")
    print("Generated read-only portal snapshots")


if __name__ == "__main__":
    main()
