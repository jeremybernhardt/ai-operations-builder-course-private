"""Deterministic known-answer checks for the M0.5-L4 transfer helper."""

import unittest

from review_routing import review_route


class ReviewRoutingTests(unittest.TestCase):
    def test_changed_bank_details_override_high_amount_route(self) -> None:
        self.assertEqual(
            review_route(
                approved=True,
                bank_details_changed=True,
                amount=12_000,
            ),
            "MANUAL_REVIEW",
        )

    def test_changed_bank_details_on_small_invoice_require_manual_review(self) -> None:
        self.assertEqual(
            review_route(
                approved=True,
                bank_details_changed=True,
                amount=500,
            ),
            "MANUAL_REVIEW",
        )

    def test_high_amount_with_stable_bank_details_requires_manager(self) -> None:
        self.assertEqual(
            review_route(
                approved=True,
                bank_details_changed=False,
                amount=12_000,
            ),
            "MANAGER_REVIEW",
        )

    def test_routine_invoice_can_release_automatically(self) -> None:
        self.assertEqual(
            review_route(
                approved=True,
                bank_details_changed=False,
                amount=500,
            ),
            "AUTO_RELEASE",
        )

    def test_missing_approval_takes_precedence(self) -> None:
        self.assertEqual(
            review_route(
                approved=False,
                bank_details_changed=True,
                amount=12_000,
            ),
            "PENDING_APPROVAL",
        )


if __name__ == "__main__":
    unittest.main()
