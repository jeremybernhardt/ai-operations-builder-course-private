"""Deterministic known-answer checks for the M0.5-L4 practice helper."""

import unittest

from payment_release import release_status


class PaymentReleaseTests(unittest.TestCase):
    def test_exactly_seven_days_is_released(self) -> None:
        self.assertEqual(
            release_status(approved=True, on_hold=False, days_until_due=7),
            "RELEASE_NOW",
        )

    def test_six_days_is_released(self) -> None:
        self.assertEqual(
            release_status(approved=True, on_hold=False, days_until_due=6),
            "RELEASE_NOW",
        )

    def test_eight_days_is_scheduled_later(self) -> None:
        self.assertEqual(
            release_status(approved=True, on_hold=False, days_until_due=8),
            "SCHEDULE_LATER",
        )

    def test_hold_overrides_due_date(self) -> None:
        self.assertEqual(
            release_status(approved=True, on_hold=True, days_until_due=2),
            "HOLD",
        )

    def test_missing_approval_overrides_due_date(self) -> None:
        self.assertEqual(
            release_status(approved=False, on_hold=False, days_until_due=2),
            "PENDING_APPROVAL",
        )


if __name__ == "__main__":
    unittest.main()
