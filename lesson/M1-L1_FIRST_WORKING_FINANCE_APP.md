# M1-L1 — First Working Finance App

Lesson ID: `M1-L1`

Checkpoint: `M1-C1`

Skill ID: `SK-APP-BUILD-VERIFY-001`

Status: Prepared for the next fresh task; learner checkpoint not attempted

Estimated required learner time: 60–90 minutes, provisional; split safely if the actual build takes longer

Primary capability: directing an AI-assisted local app build, understanding its data flow, checking important results, and verifying a bounded change

Applicable resume-level gate: none at this first scaffold; later SQL, Python, and dashboard gates remain required

Prerequisite evidence: `evidence/LEARNER_CHECKPOINT_M0.5-C4.md`

Progression exception: `DEC-C2-014` permits this lesson using verified C1-C4 while M0.5-L5 is deferred without a passed checkpoint.

## Useful result

Build the first small piece of the synthetic finance flagship: a local expense actual-versus-budget review app. A finance user can see account-level differences for one period, narrow the view by department, and identify expenses that need investigation. This is a working learner project separate from the Course Portal.

## Bounded implementation

Use a small synthetic source with one row per period, department, and expense account, containing actual and budget amounts. Start with a deliberately simple data shape; later modules teach normalized tables, joins, persistence, and imports as the app needs them. Include a readable comparison table, one useful filter, and a clear data/validation indicator. Keep the first period, dataset, and calculation scope small. A full dashboard, forecasts, live integrations, authentication, deployment, and runtime model calls are later work.

Verify the available local environment and choose the smallest appropriate Mac-compatible stack at implementation time. Reuse installed components where practical. Do not reinstall verified tools or require external accounts/spending for the first app.

## Teaching through the actual build

1. Explain the user, useful output, and source-to-calculation-to-screen path in plain language. Teach unfamiliar terms before the related action; connect them to Jeremy's spreadsheet experience.
2. Establish only the material rules needed for this small build: row meaning, calculation and sign conventions, percentage/zero-budget treatment, filter behavior, and readiness evidence. Reuse relevant prior reasoning without repeating worksheets. Ask at most one or two substantive questions before useful implementation work.
3. AI generates an initial assisted implementation. Explain the relevant calculation and how the interface obtains its data. Let Jeremy use the app early; a scaffold is software, not mastery evidence.
4. Compare actual app results to a small independently determined known answer. Inspect the relevant calculation/filter logic when a plausible display could hide an error.
5. Jeremy directs a meaningful change to a rule, validation behavior, or interaction, states the intended result, and evaluates the changed and unaffected behavior. AI may execute the code and commands.
6. Use a different input or failure to test understanding with less help, then record a limitation. Teach missing knowledge directly; do not turn immediate repetition of supplied reasoning into evidence.

## Deliverables and acceptance

- A local runnable app and synthetic source, with concise start/stop instructions and enough visual QA to establish usability.
- A short frozen behavior/data-flow record assembled by AI from Jeremy's decisions.
- Actual-output checks, a learner-directed change, regression evidence, and a failure case such as invalid values, duplicate row keys, or ambiguous zero-budget percentages.
- Jeremy's explanation of the relevant flow and logic, readiness decision, and limitation; maximum substantive help and AI execution are disclosed.

Passing M1-C1 requires these results and evidence, not merely a working screen. Do not reveal the final answer for the learner's change or unfamiliar failure before an attempt. Contribution disclosure is a brief factual closeout record, not a separate writing assessment.

Current authorization covers only this lesson. Do not implement the Expense File Readiness Checker, later flagship features, other modules, live integrations, or external actions. End with canonical continuity in a fresh-task packet; authorize only the next bounded lesson after verification.
