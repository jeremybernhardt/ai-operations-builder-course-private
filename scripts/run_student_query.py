#!/usr/bin/env python3
"""Run the learner SQL only after the definition checkpoint is frozen."""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUERY_PATH = ROOT / "student" / "first_pass_acceptance.sql"
DATABASE_PATH = ROOT / "database" / "prototype.sqlite"


def main() -> int:
    state = json.loads((ROOT / "COURSE_STATE.json").read_text(encoding="utf-8"))
    if state["current_checkpoint_id"] == "P0-C1":
        print("SQL is locked until checkpoint P0-C1 freezes the metric definition.")
        return 2

    query = QUERY_PATH.read_text(encoding="utf-8")
    if "TODO" in query or "SELECT" not in query.upper():
        print("The student SQL file is still incomplete.")
        return 2

    if not DATABASE_PATH.exists():
        print("Database missing. Run: python3 scripts/setup.py")
        return 2

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.row_factory = sqlite3.Row
        try:
            rows = connection.execute(query).fetchall()
        except sqlite3.Error as exc:
            print(f"SQL error: {exc}")
            return 1

    print(json.dumps([dict(row) for row in rows], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
