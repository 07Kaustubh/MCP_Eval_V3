# Linter Decision - Task 46

**Date:** 2026-07-29
**Class:** A (business-function / persona alignment). No Class B component.
**Resolution:** INVALIDATE with justification. `5_Prompt.txt` UNCHANGED.

## What the linter blocked

Return value FALSE on the business alignment check. The claim: the prompt is labeled
Property Operations (Cat 1) but describes a Portfolio Coordination & Owner Relations
(Cat 2.3) workflow. Five sub-claims:

1. Wrong function label; the arc is Cat 2.3 owner reporting.
2. No Property Operations persona can own this task.
3. `#owner-relations` is not a Property Operations write channel.
4. Portfolio-level issue-tracker management is not a Cat 1 write action.
5. Cross-owner financial position review is Brooke's lane, not an Onsite PM's.

Suggested revision: reseat the prompt to Teresa Wood, Executive Secretary (Cat 2).

## Skeptical-first assessment

The runbook default is invalidation; the linter's claim must be supported by per-task
universe evidence to warrant revision. It is not. Each sub-claim is contradicted by
rows in `_aux/Universe_Split/`.

| Linter sub-claim | Universe evidence | Result |
|---|---|---|
| 1. Cat 2.3 arc, no Cat 1 persona owns it | `slack_messages:297f14105d465ce1b7e66a59f1ad3ecb`, Brooke in **#make-ready** (a Cat 1 channel) 2026-05-07: "@Lisa Smith taking Harris and Finley, @Patricia Nguyen on Shea and Castillo, need occupancy, maintenance backlog, and make-ready counts from both of you by the second week of May." | REFUTED |
| 2. No Cat 1 persona can own it | `OPS-10` "Mid-Year Owner Portfolio Reviews - June 2026": "Teresa Wood, Aurora Winona, **Lisa Smith**, and **Patricia Nguyen** - please coordinate on your respective properties so we can get drafts compiled and ready for owner delivery **before end of June**." | REFUTED |
| 3. `#owner-relations` not a Cat 1 write channel | Cat 1.4 write list in the task-categories doc names `slack_mock_send_message` (`#general` or `#owner-relations`) explicitly. Scripted data: Lisa Smith posts in C006 (2026-05-28 Finley rollup); Carlos Mendez posts there 3x. C006 members include Lisa and Patricia. The channel table marks C006 "primary" to Cat 2, not exclusive, and lists C004/C005 as dual-category. | REFUTED |
| 4. Portfolio-level tracker mgmt not Cat 1 | `OPS-10` names Lisa as a coordinator on that very item. The prompt updates it with "where my half has landed", not portfolio-wide management. Cat 1 lists `linear_mock_create_issue` as a primary write. | REFUTED |
| 5. Cross-owner financial read is Brooke's lane | Cat 1 authoring checklist lists **QuickBooks** among primary systems and "tenant/**owner** emails" among primary artifacts, and names Harry Harris and Robert Finley as Cat 1 NPC participants. `OPS-100`: "**Lisa has already rolled up the core data from Airtable and QuickBooks**" for the Finley May report. | REFUTED |

## The structural rebuttal

The linter states the correct Cat 1 behavior itself: onsite PMs "contribute property-level
data to Brooke, who assembles and delivers the owner-facing product." That is exactly what
the prompt does. **The prompt contains zero owner-facing write actions.** The email goes to
Brooke. Both tracker items are internal. The channel post is explicitly addressed to Patricia
and the team. Neither Harry Harris nor Robert Finley is ever contacted. The owner-facing
deliverable remains Brooke's.

## Two further defects in the linter's own output

- The suggested reseat to Teresa Wood collides with the universe: Teresa is already the
  scripted assignee of the review-packaging sub-issues (`OPS-11`, `OPS-13`, `OPS-20`, `OPS-23`),
  and Brooke's May 7 split assigns Harris and Finley to Lisa, not Teresa. The revision would
  contradict the records it claims to protect.
- The suggested revision appends a "Prompt written by Teresa Wood, Executive Secretary." line.
  The task-categories doc states that convention is used only inside that document and that
  the persona never appears in the actual prompt. The linter is pattern-matching the guide's
  formatting rather than reasoning from the data.

Separately, the business function and persona are platform-assigned inputs
(`1_Business_Function.txt`, `2_Persona.txt`), not a labeling choice made in this pipeline.
"Wrong function label" attacks an input the submission does not control.

## Prior-phase concurrence

This axis was already adjudicated at S1 before the linter ran, on the same evidence:
- `S1_B_adversarial.md` scored Business Function 5/5, citing the persona home-function rule
  and "no owner-facing action occurs anywhere".
- `AUDIT_prompt.md` returned PASS (STRICT) with Business Function 5/5: "zero owner-facing
  writes; work is Property Operations end to end".
- `S1_A_grounding.md` scored it 3/5 and carried it as a FINAL adjudication item. Business
  Function has no FAIL band in the QC spec, so the residual is verdict-neutral either way.

The one soft signal in the linter's favor (the channel table marking C006 primary to Cat 2)
was already weighed by both councils and is outweighed by Cat 1.4's explicit authorization
of `#owner-relations` writes plus Lisa's scripted membership and posting there.

## Action taken

- `5_Prompt.txt` UNCHANGED. No revision warranted on any of the five sub-claims.
- Justification written to `_aux/Linter_Justifications.md`; voice gate exit 0.
- Appended to `Tasks/_meta/Linter_Justifications.md`.
- AUDIT skipped per runbook step 8: resolution is justification-only, so there is no new
  artifact to audit. The standing `AUDIT_prompt.md` PASS (STRICT) remains valid because the
  prompt bytes are unchanged.
