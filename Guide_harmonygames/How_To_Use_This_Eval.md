# How to Run the HarmonyGames Evaluation

This runbook drives a manual, AI-assisted QC workflow for HarmonyGames MCP
tasks. It owns the **operating sequence** and the **copy-paste commands** — it
does not redefine the rules that live in `[Docs/](../Docs/)` or
`[Evals/](../Evals/)`.

New here? Read `[../README.md](../README.md)` and
`[../Docs/README.md](../Docs/README.md)` first, then come back to this guide.

---

## 1. Prerequisites

- Cursor IDE with Agent mode enabled.
- **Claude Opus 4.7** for the final six task runs.
- A local copy of this repository and the task artifacts to evaluate.

There is no automated eval runner — run every phase below manually in Cursor.

---



## 2. Repository layout

```text
<repository-root>/
├── Docs/                       # Normative rules and QC specifications
├── Evals/                      # Six eval playbooks, numbered 0–5
├── Guide/                      # This operational runbook
├── HarmonyGames_Base_Universe/ # Narrative, schema, tool catalog, Services_Data
│   └── 6_Server_Tools_Details.json   # Combined authoritative tool catalog
├── QC_Tasks/                   # Completed calibration examples
├── Tasks_Template/             # Canonical task scaffold
└── <task-name>/                # In-progress task workspace (copied from Tasks_Template/)
```

Keep each in-progress task in its own `<task-name>/` folder at the repository
root. Never add work-in-progress tasks to `QC_Tasks/` — those folders represent
completed QC outcomes.

---



## 3. Set up a task

Copy `Tasks_Template/` to a new `<task-name>/` folder at the repository root,
then populate:


| File                                      | Contents                                                                                                         |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `1_Business_Function.txt`                 | Assigned business function.                                                                                      |
| `2_Persona.txt`                           | Exact Persona Key, Persona Email, Name, Role, and Department, copied from one `4_Persona_ACL_Roster.json` entry. |
| `3_UniverseDataForThisTask.json`          | Optional task-specific universe export.                                                                          |
| `4_Changelog.json`                        | Task injection/change manifest.                                                                                  |
| `5_Prompt.txt`                            | Prompt under evaluation.                                                                                         |
| `6_Oracle_Events.txt`                     | Non-authoritative solution plan.                                                                                 |
| `7_Rubrics.json`                          | Rubric array using `title`, `category`, `justification`, `evidence`.                                             |
| `8_Verifier_Fails.txt`                    | Raw per-run verifier failure blocks, when available.                                                             |
| `9_Universe_inject.sql`                   | SQL record of injected or modified rows.                                                                         |
| `Agent_Responses/trajectory-run-{N}.json` | Exported trajectories for runs 1–6.                                                                              |


`trajectory-run-{N}.json` is canonical for new exports; evaluators also accept
legacy `Run{N}_Trajectory.json`. An empty trajectory means that run errored and
is excluded from rubric fail counts. Follow
`[../Tasks_Template/Agent_Responses/README.md](../Tasks_Template/Agent_Responses/README.md)`.

**Historical calibration compatibility.** Original QC calibration folders may
retain a free-text persona artifact or a non-roster identity. Those are
craft/history references only — not proof of current ACL compliance, and not a
persona format to copy. Every current task requires `2_Persona.txt` with exact
values from one roster entry. The long-horizon Task5 example is a craft
baseline, but its persona artifact is not the current template.

---



## 4. Persona ACL setup & feasibility

Persona ACL is active. Use this order for every task:

1. Select the required persona in Taxonomy — Taxonomy is the selection source.
2. Copy the full matching `4_Persona_ACL_Roster.json` entry into `2_Persona.txt`.
  Copy the Persona Email exactly; never infer it from the name.
3. **Do not touch the AMV persona dropdown.** It overrides the Taxonomy
  selection and persists into later runs.
4. Load the intended universe. After load, the platform automatically applies
  `set_acting_user` with the roster email; it is re-applied on every Agent
   Runner / Run Verifier run/turn. Do not call it manually.
5. Author against complete Universe Explorer truth, then check feasibility
  separately through the assigned persona's Agent scope.
6. Keep the same required persona in Agent Runner and Run Verifiers.

The Universe Explorer is author god-mode; its visibility does **not** prove the
task Agent or verifier can read a record. For every required injected fact in a
persona-scoped service, confirm the assigned persona has a natural discovery
path and the needed ownership, membership, share, invite, or visibility
relationship — or that the task is an affirmative-denial outcome or uses an
authorized unscoped alternate.

**Read boundaries (read the doc; do NOT hardcode).** Exactly **13 services** are
task-visible. Derive the persona-scoped vs unscoped read sets from the
`Docs/14_Persona_ACL.md` **Access matrix** at eval time; if that doc changes,
this guide follows it with no edit here — do not assert a specific service's
scope status from memory. (Mechanic note, not a scope claim: if the matrix marks
the Google Drive-family scoped, GDocs/GSheets/GSlides inherit GDrive's file ACL
and a known object ID does not bypass it.) Writes are outside Persona ACL scope.
Judge feasibility using these boundaries plus the exact capabilities in
`6_Server_Tools_Details.json`.

Automatic acting-user setup is environment configuration, not an Agent tool
call — do not count it toward complexity, Oracle Events, or Process rubrics.

---



## 5. Run order

There are **six eval files** but **seven workflow phases**:

- Phases 0–4 invoke Evals 0–4.
- Phase 5 is a separate full QC-spec scorecard (no dedicated file in `Evals/`).
- Phase 6 invokes Eval 5, the final submission gate.

Run every phase in order. Replace `TaskXX_XXXXX` with the actual folder name,
complete every checklist required by the referenced Eval, and resolve findings
before continuing.

Each phase has one **primary command** that runs the full Eval as the single
source of truth for that phase, followed by focused **deep-check commands** —
one dimension per command, each framed as a strict, critical HARD GATE. Run the
primary first, then run the deep checks individually and fix issues as they
surface.

**Long-horizon condition.** If at least one run uses 500–1,000 calls, read
[`../Docs/13_Long_Horizon_Task_Guidelines.md`](../Docs/13_Long_Horizon_Task_Guidelines.md)
before Phase 0 and calibrate against the long-horizon worked example it develops
end to end. Reuse its craft structure — never its scenario, data, wording, or
totals.

---



## Phase 0 — Injection quality

Run before prompt, OE, or rubric evaluation.

**Primary command**

```text
Evaluate @TaskXX_XXXXX/9_Universe_inject.sql and @TaskXX_XXXXX/4_Changelog.json strictly per @Evals/0_Injection_Quality_Eval.md — that eval is the ONLY source of truth for this phase. Follow it exactly: create every required TODO and execute every HARD GATE with zero deviation, skipping, or softening. Compare against @HarmonyGames_Base_Universe/7_Universe_Schema.json and @HarmonyGames_Base_Universe/Services_Data/, and read the @HarmonyGames_Base_Universe/6_Server_Tools_Details.json catalog. Do not conclude until every gate is executed and reported.
```

**Deep check 0a — Structural, cross-service & temporal integrity**

```text
CRITICAL HARD GATE — STRUCTURAL, CROSS-SERVICE & TEMPORAL INTEGRITY. Strict and non-negotiable. For EVERY injected/modified row in @TaskXX_XXXXX/9_Universe_inject.sql, diff against @HarmonyGames_Base_Universe/Services_Data/ across all 13 services and check: (1) COLLISIONS — ID collisions, name-spelling mismatches, amount conflicts, status contradictions, timeline collisions, broken cross-service references; (2) ORPHANS & CONSISTENCY — every entity the injection changes still resolves and still agrees everywhere else it appears (threads, mentions, shares, invites, links, quoted amounts, meeting times) with no dangling reference, stale mention, or contradicted downstream record; (3) TEMPORAL — every timestamp within 2026-01-01 to 2026-02-28, on weekdays, created <= updated, parents strictly before children, causally consistent with base; (4) AI-TELLS — read every injected message/body/comment in the attributed human's voice and flag emojis, over-formal or too-perfect chat, repeated syntactic patterns across authors, corporate filler, and uniform lengths, cross-checking voice against @HarmonyGames_Base_Universe/Services_Data/. Any collision, orphan, contradiction, out-of-window/weekend/out-of-order timestamp, or machine-generated/off-voice text = FAIL — cite the offending injected row and the colliding/contradicted base record. Do not waive or rationalize.
```

**Deep check 0b — Persona ACL reachability**

```text
CRITICAL HARD GATE — PERSONA ACL REACHABILITY. Strict and non-negotiable. Using @Docs/14_Persona_ACL.md, @HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json, and @TaskXX_XXXXX/2_Persona.txt, first derive the persona-scoped service set live from the @Docs/14_Persona_ACL.md Access matrix (do NOT hardcode it — defer to the doc if it changes). Then prove the assigned persona can actually read EVERY required fact in those scoped services via the appropriate visibility test (mailbox ownership; membership/public visibility; calendar ownership/share/invite; Drive file ownership/share). Services the doc marks unscoped are always readable. Any required scoped fact with no path and no affirmative-denial framing = FAIL.
```

---



## Phase 1 - Prompt

**Primary command**

```text
Evaluate @TaskXX_XXXXX/5_Prompt.txt strictly per @Evals/1_Prompt_Eval.md — that eval is the ONLY source of truth for this phase. Follow it exactly: create every required TODO and execute every phase and HARD GATE with zero deviation, skipping, or softening. Read the task universe artifacts, @HarmonyGames_Base_Universe/, and the @HarmonyGames_Base_Universe/6_Server_Tools_Details.json catalog. Do not conclude until every gate is executed and reported.
```

  
**Deep check 1a - Feasibility**

```text
CRITICAL HARD GATE — FEASIBILITY. Strict and non-negotiable. For EVERY explicit ask and buried sub-ask in @TaskXX_XXXXX/5_Prompt.txt, confirm the data exists, a concrete tool path reaches it with tools/params that exist in @HarmonyGames_Base_Universe/6_Server_Tools_Details.json, and the assigned persona can do it under ACL (derive the scoped set live from @Docs/14_Persona_ACL.md Access matrix — do not hardcode it; defer to the doc if it changes). If any single ask cannot be fulfilled end-to-end = FAIL. No "minor secondary ask" escape.
```

  
**Deep check 1b - Persona ACL feasibility**

```text
CRITICAL STRONG HARD GATE — PERSONA ACL FEASIBILITY. Strict, standalone, and non-negotiable. Using @Docs/14_Persona_ACL.md, @HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json, and @TaskXX_XXXXX/2_Persona.txt, first confirm 2_Persona.txt matches one roster entry EXACTLY on Persona Key, Persona Email, Name, Role, and Department, then derive the persona-scoped service set live from the @Docs/14_Persona_ACL.md Access matrix (do NOT hardcode it; defer to the doc if it changes). Run BOTH lenses: (1) REQUIRED-READ FEASIBILITY — for every fact @TaskXX_XXXXX/5_Prompt.txt requires from a scoped service, prove the assigned persona can read it via the appropriate visibility test (mailbox ownership; Slack membership/public visibility; calendar ownership/share/invite; Drive-family file ownership/share, which inherits GDrive's file ACL and is NOT bypassed by a known object ID); (2) ASK-LEVEL ACL VIOLATION — scan every explicit and buried ask for any directive that makes the persona read scoped data outside their visibility. Any required scoped fact with no assigned-persona path, or any ask that forces an out-of-scope scoped read, = FAIL — unless the intended outcome is an affirmative denial (identify/report/escalate) or an explicitly authorized unscoped alternate. Services the doc marks unscoped are always readable; writes are never ACL-blocked. Universe Explorer author god-mode never proves reachability, and raw-data existence never satisfies this gate. This gate fails the prompt on its own regardless of how strong every other dimension is; it cannot be waived, offset, or excused as a minor/secondary ask.
```

  
**Deep check 1c - Truthfulness**

```text
CRITICAL HARD GATE — TRUTHFULNESS. Strict and non-negotiable. Extract every tight identifier in @TaskXX_XXXXX/5_Prompt.txt (channels, names, IDs, amounts, dates, counts) and require an EXACT match in the universe data/injection. Any near-match or unmatched identifier = phantom = FAIL. List each identifier with its located source or mark it phantom.
```

**Deep check 1d - Unique ground truth (UGT)**

```text
CRITICAL HARD GATE — UNIQUE GROUND TRUTH. Strict and non-negotiable. Enumerate the end-states under every reasonable reading of @TaskXX_XXXXX/5_Prompt.txt. Same writes via different wording is fine; two genuinely different defensible write-sets = ambiguous = FAIL. Convergence across runs earns extra scrutiny but never excuses an under-specified prompt.
```

**Deep check 1e - Delegation / action-decision ambiguity**

```text
CRITICAL HARD GATE — DELEGATION / ACTION-DECISION AMBIGUITY. Strict and non-negotiable. In @TaskXX_XXXXX/5_Prompt.txt, flag any "I'll [verb]" mixed with agent imperatives, or any action whose actor (agent vs human) or execute-vs-prepare intent is unclear. Any such ambiguity = FAIL.
```

**Deep check 1f - Complexity**

```text
CRITICAL HARD GATE — COMPLEXITY. Strict and non-negotiable. Trace the minimum necessary calls for @TaskXX_XXXXX/5_Prompt.txt: it must need more than 15 necessary calls, 2+ genuine services (real work, not incidental reads), multiple meaningful writes, and real information friction. A single-service investigate-then-email task = Too Easy = FAIL. 40+ calls / 3+ services are targets, not the gate.
```

---



## Phase 2 - Oracle Events

**Primary command**

```text
Evaluate @TaskXX_XXXXX/6_Oracle_Events.txt strictly per @Evals/2_OE_Eval.md — that eval is the ONLY source of truth for this phase. Follow it exactly: create every required TODO and execute every phase with zero deviation, skipping, or softening. Read the prompt, task universe artifacts, and the @HarmonyGames_Base_Universe/6_Server_Tools_Details.json catalog. Treat OEs as internal plans, not ground truth.
```

**Deep check 2a — Completeness (bidirectional mapping)**

```text
CRITICAL HARD GATE — OE COMPLETENESS. Strict and non-negotiable. Decompose @TaskXX_XXXXX/5_Prompt.txt sentence by sentence and map both ways to @TaskXX_XXXXX/6_Oracle_Events.txt: every prompt ask must have an OE step (missing = FAIL) and every OE step must trace to an ask or a necessary intermediate (extra = scope-creep flag).
```

**Deep check 2b — Accuracy (tools, params, values)**

```text
CRITICAL HARD GATE — OE ACCURACY. Strict and non-negotiable. For every step in @TaskXX_XXXXX/6_Oracle_Events.txt, the tool must exist exactly in @HarmonyGames_Base_Universe/6_Server_Tools_Details.json, every parameter must be valid for that tool, and every entity/amount/ID/email/date/channel must match universe data exactly. Any nonexistent tool, invalid parameter, or value mismatch = FAIL.
```

---



## Phase 3 — Rubrics

**Primary command**

```text
Evaluate @TaskXX_XXXXX/7_Rubrics.json strictly per @Evals/3_Rubrics_Eval.md — that eval is the ONLY source of truth for this phase. Follow it exactly: create every required TODO and execute every phase and HARD GATE with zero deviation, skipping, or softening. Read the prompt, OEs, task universe artifacts, and the @HarmonyGames_Base_Universe/6_Server_Tools_Details.json catalog.
```



**Deep check 3a — Atomicity**

```text
CRITICAL HARD GATE — ATOMICITY. Strict and non-negotiable. Read each `title` in @TaskXX_XXXXX/7_Rubrics.json word by word; if it makes more than one independently pass/failable claim it MUST be split (e.g., "mentions damage AND new city AND flight details" = 3 items). Any bundled criterion = FAIL. This is the #1 QC failure pattern.
```



**Deep check 3b — Accuracy of values & tool-name placement**

```text
CRITICAL HARD GATE — RUBRIC ACCURACY. Strict and non-negotiable. Verify every value in @TaskXX_XXXXX/7_Rubrics.json (amounts, emails, names, IDs, dates, counts) against universe data — any mismatch = FAIL. Tool names may appear ONLY in `evidence` and must exist in @HarmonyGames_Base_Universe/6_Server_Tools_Details.json; a tool name in `title`, or a wrong/nonexistent tool in evidence = FAIL.
```



**Deep check 3c — Forward coverage (missing criteria)**

```text
CRITICAL HARD GATE — FORWARD COVERAGE. Strict and non-negotiable. Decompose @TaskXX_XXXXX/5_Prompt.txt into every write action and key finding; each must be covered by at least one Outcome rubric in @TaskXX_XXXXX/7_Rubrics.json. Any explicit deliverable with zero coverage = Missing Criteria = FAIL (Major); watch multi-part asks with partial coverage.
```



**Deep check 3d — Extra / beyond-prompt**

```text
CRITICAL HARD GATE — EXTRA / BEYOND-PROMPT. Strict and non-negotiable. Trace every rubric in @TaskXX_XXXXX/7_Rubrics.json back to a specific explicit ask in @TaskXX_XXXXX/5_Prompt.txt. Any rubric that grades something the prompt never asked for = beyond-prompt = flag for removal.
```

**Deep check 3e — Overly broad**

```text
CRITICAL HARD GATE — OVERLY BROAD. Strict and non-negotiable. Take each criterion in @TaskXX_XXXXX/7_Rubrics.json in ISOLATION and ask whether a factually wrong answer could still pass it; if yes and the wrong path is plausible = FAIL. Never excuse it with "a sibling criterion covers it."
```

**Deep check 3f — Self-containment**

```text
CRITICAL HARD GATE — SELF-CONTAINMENT. Strict and non-negotiable. For each criterion in @TaskXX_XXXXX/7_Rubrics.json, a judge must decide pass/fail from the `title` + trajectory ALONE. Every expected value (amounts, emails, names, IDs, counts, dates) must be embedded in the text; if the judge must grep the universe or compute a value = NOT self-contained = FAIL.
```

**Deep check 3g — Overlap, redundancy & contradiction**

```text
CRITICAL HARD GATE — OVERLAP / REDUNDANCY / CONTRADICTION. Strict and non-negotiable. Compare every pair in @TaskXX_XXXXX/7_Rubrics.json: if removing one changes no score for any possible behavior = redundant (flag for removal); if two conflict (one rewards X, another penalizes X) = FAIL. Report each offending pair.
```

**Deep check 3h — Flexibility & over-specificity**

```text
CRITICAL HARD GATE — FLEXIBILITY / OVER-SPECIFICITY. Strict and non-negotiable. In @TaskXX_XXXXX/7_Rubrics.json: goal-level asks must not lock to one method (email vs #channel should both pass); exact match only for data values, "approximately" only for calculated values, "(or similar)" only for free-text; no pinning a tool path/param/ID format when the catalog accepts alternatives (check @HarmonyGames_Base_Universe/6_Server_Tools_Details.json). Any over-specificity that fails a valid alternative = FAIL (Major).
```

**Deep check 3i — Categories & required fields**

```text
CRITICAL HARD GATE — CATEGORIES & FIELDS. Strict and non-negotiable. In @TaskXX_XXXXX/7_Rubrics.json every `category` must be exactly `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, or `Process`; Outcome is mandatory; Process is rare, must pass the three-condition test, and may not exceed 40% of the set; all four fields (`title`, `category`, `justification`, `evidence`) must be non-blank. Any violation = FAIL.
```

---



## Phase 4 — Verifier failures

Run after trajectories and verifier results exist.

**Primary command**

```text
Analyze @TaskXX_XXXXX/8_Verifier_Fails.txt and @TaskXX_XXXXX/Agent_Responses/ strictly per @Evals/4_Verifier_Fails_Eval.md — that eval is the ONLY source of truth for this phase. Follow it exactly and complete every required TODO with zero deviation. Read the @HarmonyGames_Base_Universe/6_Server_Tools_Details.json catalog. Classify every failing rubric/run as Rubric Invalid, Judge Error, Legitimate Fail, Tool Precision Mismatch, or Excluded — leave nothing unclassified.
```

**Deep check 4a — Classification integrity**

```text
CRITICAL HARD GATE — CLASSIFICATION INTEGRITY. Strict and non-negotiable. For every failing rubric/run in @TaskXX_XXXXX/, back the label with cited evidence from @TaskXX_XXXXX/Agent_Responses/ and the rubric text (quote the exact tool call, parameter, or response). Legitimate Fail needs a real missing/incorrect action; Rubric Invalid a concrete rubric defect; Judge Error proof the agent satisfied it; Tool Precision Mismatch a valid alternate path; Excluded an empty/errored run. Any uncited label = re-classify.
```

---



## Phase 5 — Full QC specification

This phase is not an additional file in `Evals/`.

**Primary command**

```text
Evaluate @TaskXX_XXXXX/ against every dimension of @Docs/7_QC_Spec_Doc1.json and @Docs/8_QC_Spec_Doc2.md as the source of truth for this phase. Score every sub-dimension explicitly, apply current Eval overrides, and treat any hard-failing dimension as a task failure. Do not skip, merge, or soften any dimension.
```

---



## Phase 6 — Submission gate

**Primary command**

```text
Run the final submission gate on @TaskXX_XXXXX/ strictly per @Evals/5_Submission_Gate_Eval.md — that eval is the ONLY source of truth for this phase. Follow it exactly: create every required TODO, check all six defect families and every listed pattern, and execute every HARD GATE with zero deviation, skipping, or softening. Read the @HarmonyGames_Base_Universe/6_Server_Tools_Details.json catalog.
```

**Submit only when Phase 6 passes with zero hard failures.**