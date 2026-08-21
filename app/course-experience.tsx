"use client";

import { useEffect, useMemo, useState } from "react";

type Area = "portal" | "lab";
type LabStep = "intro" | "explore" | "decide" | "review" | "closeout";
type Focus = "all" | "duplicate" | "missing" | "rework";

type DataRow = {
  review_id: string;
  task_id: string;
  expert_id: string;
  task_type: string;
  submission_attempt: number;
  submitted_at: string;
  reviewed_at: string | null;
  review_status: string | null;
  review_sequence: number;
  guideline_version: string;
};

type ProgressSnapshot = {
  non_authoritative: boolean;
  label: string;
  lesson: {
    lesson_id: string;
    title: string;
    mastery_status: string;
    assistance_level: string;
    current_checkpoint_id: string;
    learner_attempt_received: boolean;
    note: string;
  };
};

type QualitySummary = {
  total_review_rows: number;
  distinct_tasks: number;
  duplicate_logical_review_groups: number;
  missing_outcome_rows: number;
  reworked_submission_rows: number;
  tasks_requiring_policy_choice: number;
};

type CourseExperienceProps = {
  dataPreview: DataRow[];
  progressSnapshot: ProgressSnapshot;
  qualitySummary: QualitySummary;
};

type DecisionState = {
  unit: "unique_tasks" | "review_rows";
  duplicate: "keep_one" | "exclude_task";
  missing: "exclude_until_corrected" | "count_not_accepted";
  rework: "not_first_pass" | "eventual_acceptance";
};

const VERIFIED_DECISIONS: DecisionState = {
  unit: "unique_tasks",
  duplicate: "keep_one",
  missing: "exclude_until_corrected",
  rework: "not_first_pass",
};

const STORAGE_KEY = "ai-operations-course:p0-c1-review:v1.2.0";

const objectives = [
  "Distinguish a user outcome from an implementation choice.",
  "Separate blocking validation failures from nonblocking anomaly warnings.",
  "Define observable acceptance tests, independent verification, and a done threshold.",
];

const artifacts = [
  ["Course contract", "Purpose, constraints, teaching rules, and authority hierarchy.", "/artifacts/COURSE_CONTRACT.md"],
  ["Curriculum map", "The approved technical path from foundations through dashboards, automation, AI, agents, and portfolio.", "/artifacts/CURRICULUM_MAP.md"],
  ["Current course state", "The authoritative checkpoint, blocker, and next-action record.", "/artifacts/COURSE_STATE.json"],
  ["Progress record", "Verified learner evidence and assistance history.", "/artifacts/PROGRESS.json"],
  ["Capability evidence", "The gates required before a work skill or resume label is defensible.", "/artifacts/CAPABILITY_EVIDENCE_LEDGER.md"],
  ["Current project specification", "The prototype scenario, requirements, and boundaries.", "/artifacts/PROJECT_SPEC.md"],
  ["Decision log", "Material course decisions and the changes they supersede.", "/artifacts/DECISION_LOG.md"],
] as const;

const labSteps: Array<[LabStep, string, string]> = [
  ["intro", "01", "Learn the situation"],
  ["explore", "02", "Explore the data"],
  ["decide", "03", "Review the policies"],
  ["review", "04", "Review the definition"],
  ["closeout", "05", "Close the lesson"],
];

function AreaButton({ active, label, onClick }: { active: boolean; label: string; onClick: () => void }) {
  return (
    <button className={`area-button ${active ? "is-active" : ""}`} onClick={onClick} aria-pressed={active} type="button">
      <span className="area-dot" aria-hidden="true" />
      {label}
    </button>
  );
}

function Portal({ progressSnapshot, openCloseout }: { progressSnapshot: ProgressSnapshot; openCloseout: () => void }) {
  return (
    <div className="view-stack" data-area="course-portal">
      <section className="dashboard-hero">
        <div className="hero-copy">
          <p className="eyebrow">Course Portal · Repository v2.0.5</p>
          <h1>Your course, one <em>verified</em> step at a time.</h1>
          <p className="hero-deck">
            The first work-practical AI-builder specification lesson is complete. Continue by reviewing a proposed builder plan in a fresh task.
          </p>
          <div className="hero-actions">
            <button className="primary-action" type="button" onClick={openCloseout}>
              Open preserved KPI Lab <span aria-hidden="true">→</span>
            </button>
            <span className="time-note">One lesson per task · Next: M0.5-L2</span>
          </div>
        </div>

        <aside className="brief-card" aria-label="Current course action">
          <div className="brief-card-head">
            <span>Current action</span>
            <span className="status-chip is-approved">Approved</span>
          </div>
          <p className="brief-number">M0.5</p>
          <h2>Builder brief checkpoint verified</h2>
          <p>M0.5-C1 passed with limited assistance. The guided brief used substantial structure; independent mastery and resume-level capability are not claimed.</p>
          <div className="brief-footer"><span>Next action</span><strong>M0.5-L2 in a fresh task</strong></div>
        </aside>
      </section>

      <section className="dashboard-grid">
        <article className="panel progress-panel">
          <div className="section-heading">
            <div><p className="section-kicker">Course progress</p><h2>Current position and full path</h2></div>
            <span className="read-only-badge">Read only</span>
          </div>
          <p className="source-label">{progressSnapshot.label}</p>
          <div className="progress-summary">
            <div className="progress-orbit"><span>M0.5</span></div>
            <div><p className="progress-title">Builder specification checkpoint verified</p><p>{progressSnapshot.lesson.note}</p></div>
          </div>
          <div className="timeline" aria-label="Course progress">
            <div className="timeline-item is-complete"><span>✓</span><div><strong>Minimum Mac setup</strong><small>Node.js and Python verified</small></div></div>
            <div className="timeline-item is-complete"><span>✓</span><div><strong>Prototype teaching-format review</strong><small>v1.2.0 preserved with honest assistance evidence</small></div></div>
            <div className="timeline-item is-complete"><span>✓</span><div><strong>Course architecture</strong><small>v2.0.0 technical retarget approved</small></div></div>
            <div className="timeline-item is-complete"><span>✓</span><div><strong>M0-L1 local Git foundations</strong><small>Completed with limited assistance</small></div></div>
            <div className="timeline-item is-complete"><span>✓</span><div><strong>M0-L2 branches and recovery</strong><small>Completed with substantial assistance</small></div></div>
            <div className="timeline-item is-complete"><span>✓</span><div><strong>M0-L3 identity and GitHub readiness</strong><small>Completed with substantial assistance</small></div></div>
            <div className="timeline-item is-complete"><span>✓</span><div><strong>M0-L4 private course repository</strong><small>Completed with substantial assistance</small></div></div>
            <div className="timeline-item is-complete"><span>✓</span><div><strong>M0.5-L1 define the build</strong><small>Completed with limited assistance</small></div></div>
            <div className="timeline-item is-current"><span>●</span><div><strong>M0.5-L2 review the builder plan</strong><small>Next lesson in a fresh task</small></div></div>
          </div>
          <details className="roadmap-details">
            <summary>View the complete course roadmap</summary>
            <div className="roadmap-groups">
              <div><span>Required core · approximately 50–60 hours</span><strong>M0–M7</strong><p>Git, supervising AI, SQL, Python, connected data, an early work-dashboard slice, analysis tools, and the full learner-built work dashboard.</p></div>
              <div><span>Required extension · approximately 25–35 hours</span><strong>M8–M12</strong><p>Workflow automation, document AI, a permissioned action-taking agent, strategic decision support, and portfolio defense.</p></div>
              <div><span>Optional specialization · approximately 6–10 hours</span><strong>OH1</strong><p>Transfer the completed skills to Human-Data and AI Operations after the required foundations.</p></div>
            </div>
          </details>
        </article>

        <article className="panel objectives-panel">
          <div className="section-heading"><div><p className="section-kicker">Learning objectives</p><h2>What M0.5-L1 developed</h2></div></div>
          <ol className="objective-list">
            {objectives.map((objective, index) => <li key={objective}><span>{String(index + 1).padStart(2, "0")}</span><p>{objective}</p></li>)}
          </ol>
          <div className="time-breakdown">
            <div><span>Lesson status</span><strong>Completed</strong></div>
            <div><span>Help boundary</span><strong>Limited on transfer</strong></div>
            <p>AI command execution is allowed; assistance status reflects conceptual and verification help rather than syntax generation alone.</p>
          </div>
        </article>
      </section>

      <section className="dashboard-grid lower-grid">
        <article className="panel">
          <div className="section-heading"><div><p className="section-kicker">Verification status</p><h2>What the evidence currently supports</h2></div></div>
          <div className="verification-list">
            <div><span className="check-mark">✓</span><p><strong>Environment ready</strong><br />Git, Node.js, npm, and Python were verified on Jeremy&apos;s Mac.</p></div>
            <div><span className="check-mark">✓</span><p><strong>Repository and privacy verified</strong><br />Private GitHub main is authoritative; the disposable practice history remains unchanged and local-only.</p></div>
            <div><span className="check-mark">✓</span><p><strong>Work-practical build brief verified</strong><br />M0.5-C1 completed with limited assistance; independent mastery and every resume-level gate remain unearned.</p></div>
          </div>
        </article>

        <article className="panel artifacts-panel">
          <div className="section-heading"><div><p className="section-kicker">Course artifacts</p><h2>Inspect the source of truth</h2></div></div>
          <p className="panel-intro">These stable records preserve the course even when a chat or browser session ends.</p>
          <div className="artifact-list">
            {artifacts.map(([label, description, href]) => (
              <a href={href} key={label} target="_blank" rel="noreferrer"><span><strong>{label}</strong><small>{description}</small></span><span aria-hidden="true">↗</span></a>
            ))}
          </div>
        </article>
      </section>
    </div>
  );
}

function DecisionChoice({
  title,
  question,
  value,
  options,
  onChange,
}: {
  title: string;
  question: string;
  value: string;
  options: Array<[string, string, string]>;
  onChange: (value: string) => void;
}) {
  return (
    <fieldset className="decision-field">
      <legend><span>{title}</span>{question}</legend>
      <div className="choice-list">
        {options.map(([optionValue, label, explanation]) => (
          <button type="button" className={value === optionValue ? "is-selected" : ""} aria-pressed={value === optionValue} onClick={() => onChange(optionValue)} key={optionValue}>
            <span className="choice-indicator" aria-hidden="true">{value === optionValue ? "✓" : ""}</span>
            <span><strong>{label}</strong><small>{explanation}</small></span>
          </button>
        ))}
      </div>
    </fieldset>
  );
}

function Lab({ dataPreview, qualitySummary, initialStep }: { dataPreview: DataRow[]; qualitySummary: QualitySummary; initialStep: LabStep }) {
  const [step, setStep] = useState<LabStep>(initialStep);
  const [focus, setFocus] = useState<Focus>("all");
  const [decisions, setDecisions] = useState<DecisionState>(VERIFIED_DECISIONS);
  const [notes, setNotes] = useState("");
  const [copyState, setCopyState] = useState("Copy result");
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    const restore = window.setTimeout(() => {
      try {
        const saved = window.localStorage.getItem(STORAGE_KEY);
        if (saved) {
          const parsed = JSON.parse(saved) as { step?: LabStep; focus?: Focus; decisions?: DecisionState; notes?: string };
          if (parsed.step && initialStep === "intro") setStep(parsed.step);
          if (parsed.focus) setFocus(parsed.focus);
          if (parsed.decisions) setDecisions(parsed.decisions);
          if (typeof parsed.notes === "string") setNotes(parsed.notes);
        }
      } catch {
        // A blocked or malformed local draft should never prevent the lesson from opening.
      }
      setHydrated(true);
    }, 0);
    return () => window.clearTimeout(restore);
  }, [initialStep]);

  useEffect(() => {
    if (!hydrated) return;
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify({ step, focus, decisions, notes }));
    } catch {
      // The lesson remains usable when browser storage is unavailable.
    }
  }, [decisions, focus, hydrated, notes, step]);

  const definition = useMemo(() => {
    const unit = decisions.unit === "unique_tasks" ? "unique eligible work items" : "individual review rows";
    const duplicate = decisions.duplicate === "keep_one"
      ? "Duplicate logical reviews are counted only once."
      : "A task containing a duplicate logical review is excluded for investigation.";
    const missing = decisions.missing === "exclude_until_corrected"
      ? "Work items with a missing first-review outcome are excluded until corrected and reported separately as a data-quality issue."
      : "A missing first-review outcome remains in the denominator and is treated as not accepted.";
    const rework = decisions.rework === "not_first_pass"
      ? "Acceptance after revision or a later submission does not count as first-pass acceptance."
      : "A later acceptance is treated as an accepted first pass.";
    return `First-pass acceptance rate is the percentage of ${unit} accepted on their initial review without revisions or rework. The numerator is eligible work accepted on its first review without rework. The denominator is ${unit} with a known first-review outcome. ${duplicate} ${missing} ${rework} The metric helps an operations manager first examine the clarity of instructions and training, then review whether standards are being applied consistently.`;
  }, [decisions]);

  const focusedRows = useMemo(() => {
    if (focus === "duplicate") return dataPreview.filter((row) => row.task_id === "T011");
    if (focus === "missing") return dataPreview.filter((row) => row.task_id === "T008");
    if (focus === "rework") return dataPreview.filter((row) => row.submission_attempt > 1 || row.task_id === "T002" || row.task_id === "T012");
    return dataPreview;
  }, [dataPreview, focus]);

  function updateDecision<Key extends keyof DecisionState>(key: Key, value: DecisionState[Key]) {
    setDecisions((current) => ({ ...current, [key]: value }));
    setCopyState("Copy result");
  }

  function resetWorkspace() {
    setStep("intro");
    setFocus("all");
    setDecisions(VERIFIED_DECISIONS);
    setNotes("");
    setCopyState("Copy result");
    try { window.localStorage.removeItem(STORAGE_KEY); } catch { /* no-op */ }
  }

  async function copyResult() {
    const result = `${definition}${notes.trim() ? `\n\nReview notes:\n${notes.trim()}` : ""}`;
    try {
      await navigator.clipboard.writeText(result);
      setCopyState("Copied");
    } catch {
      setCopyState("Select and copy the text");
    }
  }

  return (
    <div className="lab-layout" data-area="kpi-lab">
      <aside className="lesson-rail" aria-label="Lesson path">
        <p className="section-kicker">Lesson path</p>
        <div className="stage-list">
          {labSteps.map(([stepId, number, label]) => (
            <button type="button" className={`stage-item ${step === stepId ? "is-active" : ""}`} onClick={() => setStep(stepId)} aria-current={step === stepId ? "step" : undefined} key={stepId}>
              <span className="stage-number">{number}</span><span><strong>{label}</strong><small>{step === stepId ? "Open now" : "Available in review mode"}</small></span>
            </button>
          ))}
          <div className="stage-item is-locked"><span className="stage-number">→</span><span><strong>Future: Implement in SQL</strong><small>Not part of this prototype</small></span></div>
        </div>
        <div className="local-note"><strong>Local draft storage</strong><p>Your review choices stay only in this browser on this Mac. They do not update official progress.</p><button type="button" onClick={resetWorkspace}>Reset review workspace</button></div>
      </aside>

      <div className="lab-main">
        <div className="review-banner"><span>Approved format</span><p>You already completed this checkpoint with guided instruction. The fifth stage now closes the lesson and prepares the next chat.</p></div>

        {step === "intro" && (
          <section className="lesson-screen intro-screen">
            <div className="lesson-title"><p className="eyebrow">KPI Lab · P0-C1</p><h1>What counts as a first pass?</h1><p>Before calculating a quality metric, define exactly what the business question means.</p></div>
            <div className="scenario-card">
              <p className="section-kicker">The situation</p>
              <h2>A project team wants to know how often work is ready the first time.</h2>
              <p>Finance experts submit synthetic reasoning tasks. Reviewers accept the work, request revisions, or reject it. An operations manager wants to know whether instructions and training are producing work that can be approved without revision.</p>
            </div>
            <div className="intro-grid">
              <article><span>Why it matters</span><h3>A simple percentage can answer the wrong question.</h3><p>Duplicate reviews, blank outcomes, and later revisions can all distort the result unless the counting rules are settled first.</p></article>
              <article><span>Your goal</span><h3>Create one unambiguous definition.</h3><p>Decide what belongs in the numerator and denominator and how messy records are treated. No calculation or SQL is required here.</p></article>
            </div>
            <div className="concept-strip">
              <div><strong>Numerator</strong><p>The work items that meet the success rule.</p></div>
              <div><strong>Denominator</strong><p>All eligible work items being evaluated.</p></div>
              <div><strong>First pass</strong><p>The initial review before any revision or rework.</p></div>
            </div>
            <div className="screen-actions"><span>Required time: 20–30 minutes</span><button className="primary-action" type="button" onClick={() => setStep("explore")}>Explore the data <span aria-hidden="true">→</span></button></div>
          </section>
        )}

        {step === "explore" && (
          <section className="lesson-screen explore-screen">
            <div className="lesson-title compact"><p className="eyebrow">Step 2 · Explore</p><h1>See why the raw rows need policy decisions.</h1><p>Select an issue to isolate its records and explanation.</p></div>
            <div className="focus-tabs" role="group" aria-label="Data issue focus">
              <button type="button" className={focus === "all" ? "is-active" : ""} onClick={() => setFocus("all")}>All {qualitySummary.total_review_rows} rows</button>
              <button type="button" className={focus === "duplicate" ? "is-active" : ""} onClick={() => setFocus("duplicate")}>Duplicate example</button>
              <button type="button" className={focus === "missing" ? "is-active" : ""} onClick={() => setFocus("missing")}>Missing outcome</button>
              <button type="button" className={focus === "rework" ? "is-active" : ""} onClick={() => setFocus("rework")}>Rework examples</button>
            </div>
            <div className="focus-explanation" aria-live="polite">
              {focus === "all" && <><strong>Start with the shape of the data.</strong><p>There are {qualitySummary.total_review_rows} review-event rows but only {qualitySummary.distinct_tasks} distinct tasks. A review row and a work item are not the same unit.</p></>}
              {focus === "duplicate" && <><strong>Two rows describe one logical review position.</strong><p>Counting both would give one real review twice the influence. The rule must preserve the review without double-counting it.</p></>}
              {focus === "missing" && <><strong>The first-review outcome is blank.</strong><p>The task cannot be classified as accepted or not accepted until the source is corrected. The missing record should remain visible as a data-quality issue.</p></>}
              {focus === "rework" && <><strong>These tasks required another submission.</strong><p>A later acceptance is useful operational information, but it does not make the original submission a first-pass success.</p></>}
            </div>
            <div className="table-wrap" tabIndex={0} aria-label="Scrollable synthetic review data">
              <table><thead><tr><th>review</th><th>task</th><th>type</th><th>attempt</th><th>outcome</th><th>sequence</th><th>guideline</th></tr></thead>
                <tbody>{focusedRows.map((row) => <tr key={row.review_id}><td>{row.review_id}</td><td>{row.task_id}</td><td>{row.task_type.replace("_", " ")}</td><td>{row.submission_attempt}</td><td><span className={`outcome outcome-${row.review_status ?? "missing"}`}>{row.review_status ?? "missing"}</span></td><td>{row.review_sequence}</td><td>{row.guideline_version}</td></tr>)}</tbody>
              </table>
            </div>
            <p className="table-note">All records are synthetic. Open the <a href="/artifacts/DATA_DICTIONARY.md" target="_blank" rel="noreferrer">data dictionary</a> only if you need exact field definitions.</p>
            <div className="screen-actions"><button className="secondary-action" type="button" onClick={() => setStep("intro")}>Back</button><button className="primary-action" type="button" onClick={() => setStep("decide")}>Review the policies <span aria-hidden="true">→</span></button></div>
          </section>
        )}

        {step === "decide" && (
          <section className="lesson-screen decide-screen">
            <div className="lesson-title compact"><p className="eyebrow">Step 3 · Decide</p><h1>Review the counting rules you chose.</h1><p>Your verified selections are prefilled. Changes here are for prototype review and remain local to this browser.</p></div>
            <div className="decision-stack">
              <DecisionChoice title="Unit of analysis" question="What should be counted once?" value={decisions.unit} onChange={(value) => updateDecision("unit", value as DecisionState["unit"])} options={[["unique_tasks", "Unique work items", "The question concerns whether each item was ready on its first submission."], ["review_rows", "Every review row", "Later reviews would give reworked tasks more weight."]]} />
              <DecisionChoice title="Duplicate policy" question="How should one logical review appearing twice be handled?" value={decisions.duplicate} onChange={(value) => updateDecision("duplicate", value as DecisionState["duplicate"])} options={[["keep_one", "Keep one valid copy", "Preserves the real review without counting it twice."], ["exclude_task", "Exclude the entire task", "Removes even the valid evidence from the metric."]]} />
              <DecisionChoice title="Missing outcome" question="What happens when the first-review result is blank?" value={decisions.missing} onChange={(value) => updateDecision("missing", value as DecisionState["missing"])} options={[["exclude_until_corrected", "Exclude until corrected", "Report it separately, then include it in a refreshed calculation once known."], ["count_not_accepted", "Count it as not accepted", "Lowers the rate even though the actual result is unknown."]]} />
              <DecisionChoice title="Rework policy" question="Does later acceptance become a first-pass success?" value={decisions.rework} onChange={(value) => updateDecision("rework", value as DecisionState["rework"])} options={[["not_first_pass", "No—rework is not first pass", "The task remains eligible, but it does not enter the numerator."], ["eventual_acceptance", "Yes—eventual acceptance counts", "This would answer a different question about eventual completion."]]} />
            </div>
            <div className="screen-actions"><button className="secondary-action" type="button" onClick={() => setStep("explore")}>Back</button><button className="primary-action" type="button" onClick={() => setStep("review")}>Review the definition <span aria-hidden="true">→</span></button></div>
          </section>
        )}

        {step === "review" && (
          <section className="lesson-screen review-screen">
            <div className="lesson-title compact"><p className="eyebrow">Step 4 · Review</p><h1>One definition assembled from the decisions.</h1><p>This is the result of your checkpoint reasoning. No SQL or final calculation is revealed.</p></div>
            <div className="definition-card"><span>First-pass acceptance definition</span><p>{definition}</p><div className="formula-box"><strong>Formula in words</strong><p>Unique eligible work items accepted on their first review without rework, divided by unique eligible work items with a known first-review outcome.</p></div></div>
            <div className="notes-box"><label htmlFor="review-notes">Optional prototype-review notes</label><textarea id="review-notes" value={notes} onChange={(event) => { setNotes(event.target.value); setCopyState("Copy result"); }} placeholder="Record only feedback that would improve the teaching experience…" /><p>Autosaved only in this browser. It does not change official course progress.</p></div>
            <div className="review-actions"><button className="secondary-action" type="button" onClick={() => setStep("decide")}>Back</button><button className="copy-action" type="button" onClick={copyResult}>{copyState}</button></div>
            <div className="screen-actions"><span>Your result is preserved in the canonical course files.</span><button className="primary-action" type="button" onClick={() => setStep("closeout")}>Close the lesson <span aria-hidden="true">→</span></button></div>
          </section>
        )}

        {step === "closeout" && (
          <section className="lesson-screen closeout-screen">
            <div className="lesson-title compact"><p className="eyebrow">Step 5 · Lesson closeout</p><h1>This lesson is complete. Start the next one in a fresh chat.</h1><p>The files below inform the new conversation. They are not extra lesson reading and you do not need them while staying in the same chat.</p></div>

            <div className="completion-grid">
              <article className="completion-card is-complete"><span>Completed</span><h2>What you finished</h2><p>You defined first-pass acceptance, handled duplicates, missing outcomes, and rework, and connected the metric to an operational investigation.</p></article>
              <article className="completion-card"><span>Mastery boundary</span><h2>What the evidence supports</h2><p>Completed with substantial assistance. Independent mastery, SQL, a comparable challenge, teach-back, and limitation work are not claimed.</p></article>
              <article className="completion-card"><span>Next current lesson</span><h2>M0.5-L2: Reviewing an AI builder plan, assumptions, and scope</h2><p>The fresh task will review a practical proposed plan against the approved build brief without implementing it.</p></article>
            </div>

            <div className="continuity-panel">
              <div className="continuity-heading"><p className="section-kicker">Continue in a new conversation</p><h2>Start from the private repository.</h2><p>Open the authoritative private repository in a fresh Codex task, then paste the text beneath “Then send this prompt” in the next-task file.</p></div>
              <ol className="continuity-files">
                <li><span>1</span><div><strong>Private GitHub repository</strong><p>The authoritative course architecture, evidence, and current state on private main.</p></div></li>
                <li><span>2</span><div><a href="/artifacts/SESSION_HANDOFF.md" target="_blank" rel="noreferrer">SESSION_HANDOFF.md</a><p>The factual briefing: what happened, what was verified, and what comes next.</p></div></li>
                <li><span>3</span><div><a href="/artifacts/NEXT_CHAT_PROMPT.md" target="_blank" rel="noreferrer">NEXT_CHAT_PROMPT.md</a><p>The exact instructions telling the new task how to resume.</p></div></li>
              </ol>
              <div className="continuity-steps"><strong>What you do</strong><p>Open the private repository in a new task → paste the designated prompt → send. Keep the versioned ZIP only as a backup.</p></div>
            </div>

            <div className="github-future"><span>GitHub continuity is active</span><p>New tasks read canonical files from the private repository, so repeated full-folder attachments are no longer necessary. Private browser clicks and local notes remain outside the repository, and no backend was added.</p></div>
            <div className="screen-actions"><button className="secondary-action" type="button" onClick={() => setStep("review")}>Back to result</button><span>Preserved prototype view · Course repository v2.0.5.</span></div>
          </section>
        )}
      </div>
    </div>
  );
}

export default function CourseExperience({ dataPreview, progressSnapshot, qualitySummary }: CourseExperienceProps) {
  const [area, setArea] = useState<Area>("portal");
  const [labStartStep, setLabStartStep] = useState<LabStep>("intro");
  function openLab(step: LabStep) {
    setLabStartStep(step);
    setArea("lab");
  }
  return (
    <main className="course-shell">
      <header className="app-header">
        <button className="brand" type="button" onClick={() => setArea("portal")} aria-label="Open Course Portal"><span className="brand-mark">AO</span><span><strong>AI Operations Builder</strong><small>Private course workspace</small></span></button>
        <nav aria-label="Application areas"><AreaButton active={area === "portal"} label="Course Portal" onClick={() => setArea("portal")} /><AreaButton active={area === "lab"} label="KPI Lab" onClick={() => openLab("intro")} /></nav>
        <div className="learner-chip" aria-label="Learner Jeremy Bernhardt"><span>JB</span><div><strong>Jeremy Bernhardt</strong><small>Course v2.0.5 · M0.5-L2 next</small></div></div>
      </header>
      {area === "portal" ? <Portal progressSnapshot={progressSnapshot} openCloseout={() => openLab("intro")} /> : <Lab key={labStartStep} dataPreview={dataPreview} qualitySummary={qualitySummary} initialStep={labStartStep} />}
      <footer className="app-footer"><span>Local/private prototype · Synthetic data only</span><span>Canonical state lives in the course files, not this interface.</span></footer>
    </main>
  );
}
