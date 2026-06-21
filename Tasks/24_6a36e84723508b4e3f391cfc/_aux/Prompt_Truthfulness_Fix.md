# Prompt Truthfulness Fix — applied 2026-06-21

**Trigger:** S4 Phase 3 universe cross-check found the prompt's "was patched last sprint" claim is not literally present in the Slack record (Daniel Jones's actual C010 reply attributes routing fix ownership to Mateo as in-progress). To pre-empt a strict-literalist QC reading of `7_QC_Spec_Doc1.json` Truthfulness 5 ("no misleading statements"), the prompt + downstream OE / rubric wording was softened from "completed action" to "scheduled target".

## Diff

### `5_Prompt.txt` (1 sentence)

**Before:**
> Daniel posted in the payables channel a couple of weeks back that the routing rule for departed approvers **was patched last sprint**. The procurement picture won't tell me **whether that held**, but if the invoices we are still sitting on were dated **after that patch**, the routing issue is alive on the AP side and Priya needs that signal.

**After:**
> Daniel posted in the payables channel a couple of weeks back that the routing rule for departed approvers **was supposed to land last sprint**. The procurement picture won't tell me **whether it actually landed**, but if the invoices we are still sitting on were dated **after that target**, the routing issue is alive on the AP side and Priya needs that signal.

### `6_Oracle_Events.txt` OE 15

- "Check whether the departed-approver routing fix **held**" -> "**landed**"
- "invoices dated after the **patch**" -> "**target**"
- "the routing fix **did not hold**" -> "**did not land**"

### `7_Rubrics.json`

- **R7 justification + evidence:** "patched routing rule held" -> "routing-rule fix actually landed"; "post-patch orphaned items" / "post-patch-dated invoices" -> "invoices dated after the target"; "did not hold" -> "did not land"
- **R22 title + justification + evidence:** "did not hold" -> "did not land"; "after the patch" -> "after the target"; "Daniel claimed... was patched last sprint" -> "Daniel claimed... was supposed to land last sprint"; "Post-patch items" -> "Items dated after that target"

## What is preserved (binding constraints)

| Property | Before | After |
|---|---|---|
| Persona second-hand-recall framing ("Daniel posted... a couple of weeks back") | YES | YES |
| Explicit uncertainty marker ("won't tell me whether...") | YES | YES |
| Conditional verification trigger ("if the invoices were dated after...") | YES | YES |
| R22 stump pattern: agent must triangulate Linear ticket status + post-target invoice dates to reach the conclusion | YES | YES |
| Word count | within 500 cap | within 500 cap |
| No em-dashes | OK | OK |
| No tool names in prompt or rubric titles | OK | OK |

## What changed semantically

The persona-voiced claim shifted from "asserted completed action" to "asserted scheduled target". This:

- Removes the surface that a strict QC literalist could flag as Truthfulness 5 violation (no completed-action assertion that the universe contradicts).
- Keeps the L9 (authority-figure dismissal) lever firing: the agent still has to discover (a) the Linear routing-fix issue is still `todo` past its 2026-05-22 due date, (b) the 6 post-target invoices still carry `approver = null`. Neither is named in the prompt.
- Does NOT name Mateo, Linear issue_378874..., or the post-target invoice IDs in the prompt itself — verification path is intact.

## Trajectory implication

The 6 trajectories in `trajectory-runs/*.json` ran on the OLD prompt wording. Their judge verdicts and Trajectory_Stats numbers (density 68.7, pass@1 0/6) remain the empirical record for that wording. If the task is re-uploaded with the NEW wording, the platform will produce new trajectories; the R22 fail rate is expected to land in the same 30-50% band because the operative reasoning (post-target invoices + open Linear ticket -> fix did not land) is unchanged. The L9 lever is preserved.

## Validation

Re-validated post-fix:

```
[PASS] prompt: 0 fails, 0 warns, 1 notes
[PASS] oe:     0 fails, 0 warns, 1 notes
[PASS] rubrics: 0 fails, 0 warns, 2 notes
```

Zero `was patched` / `after the patch` / `post-patch` / `did not hold` strings remain anywhere in the prompt / OE / rubrics.

## Truthfulness QC re-score (projected)

Under the strict-literalist reading: **PASS (5)** — no assertion of a completed action that the universe contradicts. The persona quotes Daniel's stated target ("was supposed to land last sprint") and explicitly admits she cannot confirm it. A reader looking for "misleading statements" finds none.

Under the project's design-intent reading: still **PASS (5)** — the L9 authority-dismissal lever is intact (the persona's belief about Daniel's intent remains the anchor the agent has to verify against SSOT).

Both readings now agree.
