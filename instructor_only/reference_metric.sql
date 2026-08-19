-- Instructor-only controlled reference for release-gate verification.
-- This is not Jeremy's frozen metric definition and must not be linked in the
-- student interface. The learner definition may require an explicit decision
-- log entry if it justifiably differs from this controlled fixture policy.

WITH ranked_reviews AS (
    SELECT
        review_id,
        task_id,
        submission_attempt,
        review_status,
        review_sequence,
        reviewed_at,
        ROW_NUMBER() OVER (
            PARTITION BY task_id, submission_attempt, review_sequence
            ORDER BY reviewed_at, review_id
        ) AS logical_review_row
    FROM review_events
),
eligible_initial_reviews AS (
    SELECT review_status
    FROM ranked_reviews
    WHERE submission_attempt = 1
      AND review_sequence = 1
      AND logical_review_row = 1
      AND review_status IS NOT NULL
      AND TRIM(review_status) <> ''
)
SELECT
    SUM(CASE WHEN review_status = 'accepted' THEN 1 ELSE 0 END) AS accepted_first_pass_count,
    COUNT(*) AS eligible_first_pass_count,
    1.0 * SUM(CASE WHEN review_status = 'accepted' THEN 1 ELSE 0 END) / COUNT(*) AS first_pass_acceptance_rate
FROM eligible_initial_reviews;
