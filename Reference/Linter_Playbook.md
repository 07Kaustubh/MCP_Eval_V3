# Linter Playbook

The platform linter blocks prompts on two classes of issue. Treat each class differently.

## Class A — Misalignment

The linter cites a specific QC dimension: persona mismatch, business-function mismatch, feasibility, tool mention, truthfulness, today-date alignment, contrived difficulty, coherence, cross-service requirement.

### Decision flow

1. **Re-check the cited dimension against the per-task universe.** Council A runs the targeted grep. Council B re-scores the cited sub-dimension against the QC spec.
2. **Linter is right →** revise `5_Prompt.txt` to fix the underlying issue. Log the change in `_aux/Linter_Decision.md`.
3. **Linter is wrong →** write a justification (template below), send it back, log to `_aux/Linter_Justifications.md`.
4. **Both →** revise the part that's clearly wrong, justify the rest.

## Class B — Similarity ≥ 40%

A previously submitted task overlaps too closely. Use `Reference/Similarity_Pivot.md` to pivot. No justification path — pivots are the only valid response.

## Justification style (Class A only)

Justifications go to a human reviewer. Concise, plain-spoken, no jargon, no references to guides or specs. The reviewer wants to see the agent grounded the call in actual data, not in process language.

### Hard rules

- **Two to five sentences.** Anything longer reads as defensive.
- **No em-dashes.** Use periods or commas.
- **No mention of "the guide", "the spec", "the QC doc", "the playbook", "the eval", "the rubric framework", "the V3 framework", or rule numbers.**
- **No bullet points unless the linter complaint listed multiple items.**
- **First person, human voice.** "I checked the AP invoice and it shows pending_approval as of June 12." Not "The agent has verified that..."
- **Cite the concrete record.** Vendor name, invoice number, period, dollar amount, date — whatever the linter doubted. One specific fact lands the point.

### Forbidden terms (enforced by `Validators/check_justification.py`)

The script scans every justification file before ship and fails on any of these eight categories. The justification goes to a human platform reviewer; their loop is "is this a sane operator looking at real data?" Internal terminology shatters that read.

| Category | What it catches | Why it's forbidden |
|---|---|---|
| Rubric numbers | `rubric 7`, `R3`, `rubric[12]`, `criteria #5` | Reviewer rates the prompt / artifact, not your numbered rubric set. Numbers expose the pipeline. |
| Council references | `Council A`, `Council B`, `council protocol`, `council report` | Council names are internal-process artifacts the reviewer should never see. |
| Pipeline phase names | `PIPELINE S1`, `phase S2`, `HARDNESS`, `FINAL`, `REDO`, etc. | Phase names are internal-process artifacts. The reviewer judges the deliverable, not the workflow. |
| Internal artifact names | `Fact_Ledger`, `Hardness_Plan`, `Stump_Hypothesis`, `Universe_Index`, `Universe_Split`, `Trajectory_Stats`, `Candidate_Originals`, etc. | These files exist only in our `_aux/` directory. A reviewer mention proves you copied process language into a human voice. |
| Script names | `validate.py`, `build_fact_ledger.py`, `parse_trajectories.py`, `check_justification.py`, `calc_similarity.py`, etc. | Tooling names belong in `_aux/` reports, not in reviewer-facing text. |
| Guide / spec references | "the eval guide", "the QC spec doc", "the framework", "the playbook", "the runbook", "guidelines doc" | Reviewers do not care what document you read. They care whether you grounded the call in actual data. |
| V3 framework refs | "V3 framework", "V3 rubric", "Outcome 1.1", "Process rubric three-condition test" | V3 is our internal taxonomy. Use plain words: "the email send", "the verification step". |
| Brookfield meta refs | `Brookfield_Base_Universe`, "per-task universe", "stale universe" | Internal directory + pipeline jargon. Use the persona / entity / service name directly. |

The script is invoked with one or more file paths:

```
python Validators/check_justification.py path/to/file1.md path/to/file2.txt
```

Exit code 0 = clean. Non-zero = per-hit report with line + matched term + 60-char context window. Revise and re-run.

`changes.md` (REVIEW flow operator-internal change log) is NOT subject to this check — it lives inside the project loop and uses internal terms legitimately. Files that MUST pass: `_aux/Linter_Justifications.md`, `_aux/Council_Reports/S4_AF_justifications.md`, `13_Feedback.txt` (review-mode candidate feedback).

### Template (for a Class A pushback)

> The prompt names <THING>. I checked <where in the data> and it shows <concrete fact>. <Optional second concrete fact>. The prompt reads naturally from <persona's> seat because <one short reason>. Happy to revise if you see something I missed.

### Example — feasibility pushback

> The prompt asks about the May FX revaluation drift on account 132000. I checked the BlackLine exception and reconciliation records and exc_cb0a9a94a3084c sits at awaiting_approval against BL-3978BDB68290 with a $435.41 variance and the June 4 SLA already passed. The lookup is solvable from the records the agent has access to. Happy to revise if you see something I missed.

### Example — persona pushback

> Harry Marks owns the account 132000 reconciliation on the open Brookfield May close. He has a personal stake in chasing the named approver, and the messaging thread between him and the second-eye reviewer about the corrective JE is already in his sent items. The prompt reads naturally from his seat. Happy to revise if you see something I missed.

### Example — truthfulness pushback

> The prompt mentions Brenda's soft commitment to deliver a refreshed W-9 by end of May. That commitment is in the vendor reply email dated May 19 and the invoice apinv_9aa666fc03424902 is still pending_approval today. The reference to a soft commitment is accurate to the data. Happy to revise if you see something I missed.

### Worked example — BEFORE (forbidden) vs AFTER (clean)

These two examples show the most common authoring mistake: writing the justification in process-aware voice. The BEFORE column trips `check_justification.py`; the AFTER column passes.

**Example 1 — feasibility pushback**

| | Text |
|---|---|
| BEFORE (`check_justification.py` FAILs) | The QC spec doc says feasibility requires every entity to be solvable from per-task universe data. I checked Fact_Ledger.json and confirmed exc_cb0a9a94a3084c sits at awaiting_approval. Rubric 3 in our set already grounds this. Council A flagged no issues. Happy to revise if you see something I missed. |
| Why it fails | `the QC spec doc` (guide ref), `Fact_Ledger.json` (internal artifact), `per-task universe` (Brookfield meta ref), `Rubric 3` (rubric number), `Council A` (council ref). Five hits. |
| AFTER (clean) | The prompt asks about the May FX revaluation drift on account 132000. I checked the BlackLine exception records and exc_cb0a9a94a3084c sits at awaiting_approval against BL-3978BDB68290 with a $435.41 variance and the June 4 SLA already passed. The lookup is solvable from the records the agent has access to. Happy to revise if you see something I missed. |

**Example 2 — AF (always-failing) justification on a numeric reasoning gap**

| | Text |
|---|---|
| BEFORE (`check_justification.py` FAILs) | Per the V3 framework Outcome 1.1 expects the agent to compute the net figure. The agent reported the gross amount instead. parse_trajectories.py shows all 6 runs failed Rubric 4. The Hardness_Plan predicted exactly this lever as the stump. This is a genuine model failure, not a rubric issue. |
| Why it fails | `V3 framework` + `Outcome 1.1` (V3 refs), `parse_trajectories.py` (script name), `Rubric 4` (rubric number), `Hardness_Plan` (internal artifact). Five hits. |
| AFTER (clean) | The agent reported the gross $186,350 aggregate without applying the three documented adjustments. The correct net is approximately $117,000 once the Meridian reversal, the CloudNova credit memo, and the intercompany reclass are excluded. All three adjustments are visible in the AP and GL records the agent had access to. This is a genuine reasoning gap, not a rubric issue. |

The pattern in both: strip every process-aware reference, lead with the concrete data fact, name the persona / record / amount the reviewer can grep, and end with the standing offer to revise (linter pushback) or the standing characterization "genuine model gap, not a rubric issue" (AF).

### Pre-ship check (Class A pushbacks)

Before submitting any linter pushback, run:

```
python Validators/check_justification.py Tasks/<TASK_DIR>/_aux/Linter_Justifications.md
```

Non-zero exit = revise + re-run. Do NOT ship a justification that fails the check; it reads as process leakage to the reviewer and immediately undermines the pushback.

### When to accept rather than push back

If the linter cites:

- A real factual error in the prompt that you can confirm by grepping the per-task universe.
- A real tool / parameter / internal-ID leak the validator missed.
- A real pre-solving phrase ("the root cause is X" with X actually being the answer).
- A real over-stack of unrelated asks (sentence-removal test passes for one or more sentences).

Then revise the prompt. Do not push back.

## All-Failing (AF) Rubric Justifications

After agent runs, the verifier may surface rubrics that failed across every completed run. Same style rules as above:

- Two to four sentences.
- No em-dashes.
- No references to guides, the framework, sub-types, or three-condition tests.
- First-person human voice, naming the specific gap.

### AF template

> The agent <what it did wrong, in plain words>. The correct answer is <concrete fact from the data>, which requires <specific reasoning the agent skipped>. The rubric is grounded in <where in the data>. This is a genuine model gap, not a rubric issue.

### AF example

> The agent reported the gross $186,350 aggregate without applying the three documented adjustments. The correct net is approximately $117,000 once the Meridian reversal, the CloudNova credit memo, and the intercompany reclass are excluded. All three adjustments are in the universe records. This is a genuine reasoning gap, not a rubric issue.

### AF example — entity confusion

> Every run sent the IOLTA reconciliation summary to the Brookfield trust contact instead of the Northstar trust contact. Account 105000 is Cash Client Trust on Brookfield and IOLTA on Northstar, and only the Northstar account holds segregated client funds. The rubric is grounded in the per-entity chart of accounts. This is the intended failure mode for the task.

### Pre-ship check (AF justifications)

Before submitting any AF justification batch, run:

```
python Validators/check_justification.py Tasks/<TASK_DIR>/_aux/Council_Reports/S4_AF_justifications.md
```

Non-zero exit = revise + re-run. Same rule as Class A pushbacks: zero process leakage allowed in reviewer-facing text.
