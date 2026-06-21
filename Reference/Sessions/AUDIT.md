# PIPELINE AUDIT — Veteran QC Second-Opinion (Strictest Interpretation)

**Trigger:** `PIPELINE AUDIT — Tasks/<TASK_DIR> --phase {prompt|oe|rubrics|all}`

## What this phase does

Veteran audit of a completed deliverable (or a full task) using the **STRICTEST possible QC interpretation**. Two invocation modes:

### Mode 1 — Auto-fire (mandatory, runs after every per-phase deliverable)

S1, S2, S3, S1.5 (revise path), and REVIEW (corrected materialization) runbooks now spawn an AUDIT sub-agent INLINE after the per-phase Council A + Council B pass, BEFORE the STOP gate. The `_aux/Council_Reports/AUDIT_<phase>.md` report with `PASS (STRICT)` is a required exit criterion for those phases.

Rationale (v7 design): operator found flaws on Tasks 23-24 that escaped per-phase Council A + B + FINAL. Catching them early — at the phase that produced them — is cheaper than catching them downstream at FINAL or at platform-reviewer time. Per-phase councils enforce the 5/5 bar with NON-FAIL bands explicitly justified; AUDIT enforces the same bar without ANY NON-FAIL band tolerance, plus tightens density (50+ midpoint vs 40 floor) and reads every "should" as "must". The cost is ~3 additional sub-agent calls per task (S1 + S2 + S3, with S3 using ultrabrain) — accepted for early risk mitigation.

### Mode 2 — On-demand (manual, fresh chat)

Operator-triggered re-verification in a fresh chat using the trigger phrase above. Use when:

- Pre-FINAL high-stakes sanity check on a task you already shipped through the auto-fire loop, before platform upload.
- A FINAL council passed but something still feels off.
- A task came back from the platform reviewer with a fail and we want to retro the full task under strictest lens before deciding rebuild vs. fix.
- A new pipeline change (validator, council perspective, lever) just landed and we want to re-audit recently shipped tasks against the new bar.
- A reviewer is calibrating the project bar and needs a worked audit example.

Both modes use the SAME prompt template (below) and produce the SAME report format. Auto-fire mode is invoked inline as a sub-agent inside the phase chat; on-demand mode is invoked in a fresh chat via the trigger phrase. Read-only either way — does NOT modify deliverables.

## When NOT to use AUDIT

- As a substitute for FINAL. AUDIT audits per-phase artifacts in isolation; FINAL is the mandatory cross-artifact council before platform upload (checks cross-artifact consistency, entity drift, integrated density). They are complementary, not replacements.
- For trivial sanity checks. AUDIT is heavyweight (oracle / ultrabrain sub-agent with strictest interpretation). For quick checks, run `Validators/validate.py` or `Validators/check_justification.py`.

## Required inputs

| File | Source | Required when |
|---|---|---|
| `Tasks/<TASK_DIR>/5_Prompt.txt` | S1 | `--phase prompt` or `--phase all` |
| `Tasks/<TASK_DIR>/6_Oracle_Events.txt` | S2 | `--phase oe` or `--phase all` |
| `Tasks/<TASK_DIR>/7_Rubrics.json` | S3 | `--phase rubrics` or `--phase all` |
| `Tasks/<TASK_DIR>/_aux/Hardness_Plan.md` | HARDNESS | always |
| `Tasks/<TASK_DIR>/_aux/Fact_Ledger.json` | S0 | always |
| `Tasks/<TASK_DIR>/_aux/Universe_Split/*` | S0 | always |
| `Tasks/<TASK_DIR>/_aux/Universe_Index/*` | S0 | always |
| `Tasks/<TASK_DIR>/_aux/Council_Reports/*.md` | per-phase + FINAL councils | always (the audit re-reads them to spot pattern misses) |
| `Tasks/_meta/Learnings.md` | empirical Opus 4.8 failure modes | always |
| `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` | strictest QC scoring source | always |
| `Evals/1_Prompt_Eval.md` | strictest prompt eval | `--phase prompt` or `--phase all` |
| `Evals/2_OE_Eval.md` | strictest OE eval | `--phase oe` or `--phase all` |
| `Evals/3_Rubrics_Eval.md` | strictest rubric eval | `--phase rubrics` or `--phase all` |

## Strictest QC interpretation — what that means

The per-phase Council B scores QC sub-dims and allows 3-4 bands when explicitly justified against per-task universe state. AUDIT does NOT. It applies the **strictest reading** of every sub-dim in `Docs/7_QC_Spec_Doc1.json`:

- 5/5 is the only acceptable score on every applicable sub-dim. 4 is treated as a soft fail and must be raised to 5 or the deliverable is REVISE.
- Every "should" in the eval spec is read as "must".
- Every soft convention in `Reference/<phase>_Format.md` is read as binding.
- Every per-phase warning in the validator output is treated as a hard issue worth listing.
- Every Hardness lever from `Hardness_Plan.md` must trace end-to-end through the artifact set with cited evidence; "probably triggered" is REVISE.
- Density bar is 50+ midpoint (not 40 floor). 40-49 is flagged as `THIN`, not `PASS`.
- Any answer-leakage hit on a derived figure is BLOCKER (per L6 from Learnings.md — agents read full thread depth and an answer stated verbatim is 100% pass).

The point is to catch what the lighter per-phase pass let through. If AUDIT returns PASS under the strictest interpretation, the deliverable is genuinely 5-of-5.

## Phase-readiness gate (run FIRST)

```
python Validators/phase_ready.py --phase final --task Tasks/<TASK_DIR>
```

Re-uses the FINAL gate (same upstream artifact requirements). If it STOPs, run the upstream phase first. AUDIT cannot run on incomplete tasks.

## Procedure

1. **Parse the phase argument.** `--phase prompt`, `--phase oe`, `--phase rubrics`, or `--phase all`. For each phase scope, prepare the inputs table above.

2. **Run validators first** to catch the cheap stuff before spending on the audit sub-agent.
   ```
   python Validators/validate.py --phase {prompt|oe|rubrics|all} --task Tasks/<TASK_DIR>
   python Validators/check_justification.py Tasks/<TASK_DIR>/_aux/Linter_Justifications.md   # if present
   python Validators/check_justification.py Tasks/<TASK_DIR>/13_Feedback.txt                # if REVIEW flow
   python Validators/calc_similarity.py Tasks/<TASK_DIR>                                    # similarity vs ref corpus
   ```
   Read the reports. Note every WARN and every NOTE — the audit treats these as worth listing under strictest interpretation.

3. **Spawn the Audit Council** as a single `oracle` (or `ultrabrain` for `--phase rubrics` or `--phase all`) sub-agent. Use the prompt template below.

4. **Read the verdict.** Three outcomes:

| Verdict | Action |
|---|---|
| `PASS (STRICT)` | The deliverable holds up under the strictest interpretation. Append a one-line entry to `Tasks/_meta/Audit_Log.md` noting which phase was audited + verdict. The deliverable is genuinely 5-of-5; you can ship with high confidence. |
| `REVISE` | The deliverable has issues the per-phase councils missed. Apply the fixes IN PLACE (per the audit's per-issue fix). Re-run the per-phase validators + councils. Re-run PIPELINE AUDIT only when you want a second strict-pass confirmation; do not re-run on every iteration. |
| `REBUILD` | The deliverable has structural issues that a fix-in-place cannot repair (e.g., the prompt's framing actively blocks 3+ levers; the OE list contradicts the prompt's implicit framing across multiple steps; the rubric set has a category split that cannot be patched). Invoke `PIPELINE REDO — Tasks/<TASK_DIR>` to rebuild the affected artifact(s) from scratch. |

5. **Exit criteria.** `Tasks/<TASK_DIR>/_aux/Council_Reports/AUDIT_{phase}.md` exists with a clear verdict (`PASS (STRICT)`, `REVISE`, or `REBUILD`) and per-issue findings with cited evidence.

## Audit prompt template

Use this prompt for the `oracle` (or `ultrabrain`) sub-agent. Fill in `<TASK_DIR>` and `<PHASE>`. For `--phase all`, include all three deliverables in INPUTS and run all phase-specific lenses.

```
You are a VETERAN QC AUDITOR on a Brookfield MCP Eval V3 task. Your job is
re-verification under the STRICTEST possible QC interpretation. Per-phase
councils already passed this deliverable — your job is to catch what they
missed.

Strictest interpretation means:
  - 5/5 is the ONLY acceptable score on every applicable sub-dim.
  - Every "should" in the eval spec is read as "must".
  - Every soft convention in the format card is binding.
  - Every validator WARN / NOTE is a hard issue worth listing.
  - Every Hardness lever must trace end-to-end with cited evidence.
  - Density bar is 50+ midpoint (not 40 floor); 40-49 = THIN, not PASS.
  - Any answer-leakage hit on a derived figure is BLOCKER.

INPUTS:
  Deliverable(s) for phase <PHASE>:
    <list the relevant 5_/6_/7_ files>
  Tasks/<TASK_DIR>/_aux/Hardness_Plan.md
  Tasks/<TASK_DIR>/_aux/Fact_Ledger.json
  Tasks/<TASK_DIR>/_aux/Universe_Split/*
  Tasks/<TASK_DIR>/_aux/Universe_Index/*
  Tasks/<TASK_DIR>/_aux/Council_Reports/*.md  (re-read prior council verdicts)
  Tasks/_meta/Learnings.md
  Docs/7_QC_Spec_Doc1.json + Docs/8_QC_Spec_Doc2.md
  Evals/<n>_<PHASE>_Eval.md

TASK:

Apply five lenses in sequence. The verdict is the union.

LENS 1 — Strict QC scoring
For EVERY applicable QC sub-dim in Docs/7_QC_Spec_Doc1.json, score it
1-5 under STRICTEST interpretation. Output: SUB-DIM -> SCORE -> ONE-LINE
REASON -> WHAT THE PRIOR COUNCIL MISSED (if anything). Any sub-dim < 5
= REVISE. List the exact change needed to reach 5.

LENS 2 — Answer-leakage sweep (deeper than FINAL's)
Identify the correct/derived answer the task is built around (read
Hardness_Plan.md + infer from the deliverables). Then:
  - String-search every artifact body for the exact figure.
  - String-search every artifact body the prompt asks the agent to read
    (emails, slack messages, docs, vault entries) for the figure.
  - String-search for ARITHMETIC NEIGHBORS of the figure (off-by-one, off-by-
    decimal-place, off-by-percent variants the agent might stumble across).
  - For numeric answers: confirm no single tool call (one email read, one
    doc fetch) reveals the figure without requiring synthesis across 2+
    sources.
Any hit = BLOCKER.

LENS 3 — Hardness end-to-end trace
For EACH lever in Hardness_Plan.md, name:
  - The prompt sentence that surfaces it.
  - The OE step that exercises it.
  - The rubric criterion that depends on the agent traversing it.
  - The Fact_Ledger atom(s) the agent must touch to satisfy it.
Any lever missing any of those four = HARDNESS_REGRESSION.
"Probably triggered" or "implied" without cited evidence = REVISE.

LENS 4 — Strict density projection
Sketch the trajectory under the STRICTEST reading of the prompt (the
reading that minimizes inferred exploration). Count tool calls. The
strict bar is 50+ midpoint. 40-49 = THIN (revise the deliverable to
add asks or breadth). < 40 = BLOCKER.

LENS 5 — Adversarial veteran review
You have audited 200+ Brookfield tasks. Apply pattern recognition:
  - Is the implicit-prompt framing actually preserved across all 3
    artifacts? (L15+L16 framing constraint — a rubric that demands a
    "flag the discrepancy" step when the prompt says "execute on the
    figure" is a structural fail.)
  - Are there entity-drift seams (Andrea Phil vs the partner vs
    andrea.phil@brookfieldcpas.com)?
  - Are there silent process rubrics disguised as outcomes? (Apply the
    three-condition test: required by every valid path, outcome can't
    cover it, evaluates verification not execution.)
  - Tool name leaks in rubric titles? Tool name leaks in prompt?
    Em-dashes? "at least N" without prompt mandate? Internal IDs in
    the prompt? OE meta-tags (write action / read action arrows)?
  - Single-channel lock-in where the prompt named only a goal?
  - "Approximately" near IDs / dates / account numbers / dollar amounts?
  - "(or similar)" near values that must be exact?
  - For REVIEW flow only — does 13_Feedback.txt contain forbidden
    internal terms? (run check_justification.py mentally; flag hits.)

VERDICT:
  PASS (STRICT)  if zero BLOCKER hits AND zero LENS-1 sub-dims < 5 AND
                 every lever traces end-to-end AND density >= 50.
  REVISE         if issues are fix-in-place. List each as
                 [SEVERITY] <one-line issue> -- <file>:<location> -- <exact fix>.
  REBUILD        if structural issues a fix cannot repair (3+ levers
                 untriggered by prompt framing, OE list contradicts prompt
                 framing across multiple steps, rubric set has a category
                 split that cannot be patched). Name the structural fail
                 and the recommended REDO scope.

Save the report to Tasks/<TASK_DIR>/_aux/Council_Reports/AUDIT_<PHASE>.md.
```

## Cost note

AUDIT spends 1 oracle (or 1 ultrabrain for rubrics / all) sub-agent call per invocation.

- **Auto-fire mode** (mandatory): ~3 additional calls per task (S1 + S2 + S3, with S3 using ultrabrain), plus any S1.5 / REVIEW re-runs. Accepted cost for early risk mitigation per the v7 design decision — catching defects at the producing phase is cheaper than catching them downstream at FINAL or at platform-reviewer time.
- **On-demand mode** (manual): 1 call per invocation. Use for the discrete scenarios listed under Mode 2 above.

## STOP gate (on-demand mode only)

Auto-fire mode does NOT have its own STOP gate — it runs inline as a sub-agent inside the parent phase chat (S1/S2/S3/S1.5/REVIEW), and the parent phase's STOP gate handles the chat termination.

On-demand mode ends here after the audit report is saved. End your response.

If the user pastes follow-up content (a new task, a different deliverable to audit, fix attempts, etc.), do NOT process it in this chat. Tell the user: "PIPELINE AUDIT is single-shot per phase in on-demand mode. Open a fresh chat and invoke the appropriate next trigger." This keeps the audit chat decision-clean.

Three next-trigger paths:
- `PASS (STRICT)` → user ships the task (or proceeds to platform upload after FINAL if not yet run). Append a one-line entry to `Tasks/_meta/Audit_Log.md`.
- `REVISE` → user applies fixes IN PLACE in a fresh chat (or invokes the relevant phase trigger if the fix needs the per-phase machinery).
- `REBUILD` → user invokes `PIPELINE REDO — Tasks/<TASK_DIR>` in a fresh chat.

Do NOT proceed to fix application, platform upload, or any other phase inside this chat.

## Bootstrap

Read root `AGENTS.md` first. AUDIT is the highest-rigor read-only check in the pipeline; it exists to catch what the per-phase + FINAL councils missed under the strictest interpretation. It is NOT a substitute for FINAL (which is mandatory before platform upload) but a complementary tool for high-stakes re-verification.
