# Prototype Data Dictionary

Dataset ID: `DATA-P0-REVIEWS-001`  
File: `data/project_task_reviews.csv`  
Classification: Fully synthetic educational data

Each row is a recorded review event for one submission attempt. A task can have more than one submission attempt and, because raw operational data can be imperfect, more than one recorded row for the same logical review position.

| Field | Type | Nullable | Meaning | Valid examples / controls |
|---|---|---:|---|---|
| `review_id` | text | No | Unique row identifier for the recorded review event. | Must be unique and nonblank. |
| `task_id` | text | No | Stable identifier for the underlying task across attempts. | Format `T###`. |
| `expert_id` | text | No | Synthetic contributor identifier. | Format `E###`; not a real person. |
| `task_type` | text | No | Synthetic work category. | `budget_variance`, `valuation`, `cash_flow`, `forecasting`. |
| `submission_attempt` | integer | No | Attempt number for the underlying task. | Positive integer; `1` is the original submission event. |
| `submitted_at` | ISO-8601 timestamp | No | When this submission attempt was recorded. | UTC timestamp ending in `Z`. |
| `reviewed_at` | ISO-8601 timestamp | Yes | When the review event was recorded. | UTC timestamp; blank only if no review time is known. |
| `review_status` | text | Yes | Recorded review outcome. | `accepted`, `revise`, `rejected`, or blank for a missing outcome. |
| `review_sequence` | integer | No | Intended ordinal review position within a submission attempt. | Positive integer; raw duplicates may share the same value. |
| `guideline_version` | text | No | Guideline version active for the event. | `G1` or `G2`. |

## Known data-quality conditions

The dataset deliberately contains:

- a duplicated logical review position;
- a blank review outcome;
- reworked tasks represented by later submission attempts; and
- records that force an explicit denominator policy.

These conditions are exercise inputs, not instructions about how to calculate the metric. The metric dictionary remains draft until checkpoint `P0-C1` is passed.
