"""Synthetic invoice-review routing helper for the M0.5-L4 transfer."""


def review_route(
    *, approved: bool, bank_details_changed: bool, amount: int
) -> str:
    """Return the review route for one synthetic invoice.

    Missing approval takes precedence. Approved invoices with changed bank
    details require manual review, regardless of amount. Otherwise, invoices
    of 10,000 or more require manager review and smaller invoices may be
    released automatically.
    """

    if not approved:
        return "PENDING_APPROVAL"

    if bank_details_changed:
        return "MANUAL_REVIEW"

    if amount >= 10_000:
        return "MANAGER_REVIEW"

    return "AUTO_RELEASE"
