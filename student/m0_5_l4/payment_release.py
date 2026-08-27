"""Small synthetic payment-release helper for M0.5-L4 practice.

This is isolated lesson code. It is not part of the Expense File Readiness
Checker or the course flagship.
"""


def release_status(*, approved: bool, on_hold: bool, days_until_due: int) -> str:
    """Return the payment-operations queue for one synthetic invoice.

    Approved invoices that are not on hold should be released when they are
    due within seven calendar days. Other approved invoices are scheduled for
    later. Holds and missing approval take precedence over timing.
    """

    if on_hold:
        return "HOLD"

    if not approved:
        return "PENDING_APPROVAL"

    if days_until_due <= 7:
        return "RELEASE_NOW"

    return "SCHEDULE_LATER"
