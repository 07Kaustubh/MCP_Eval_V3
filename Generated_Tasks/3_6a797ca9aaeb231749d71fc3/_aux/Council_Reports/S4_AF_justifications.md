# All-Failing Rubric Justifications

Six criteria failed all six runs. Each carries a legitimate failure mode the task was built to test.

---

## ART-team VFX tracker comment identifies Combo-Fighters PR #16 as merged on 2025-12-21

The universe has PR #16 merged on 2025-12-21 with author PERSON_0396. The date is one field on the PR page the agents already opened in every run. In the two runs where an ART tracker comment was produced, the comment named PR #16 by title but omitted the merge date. The remaining four runs skipped the ART tracker altogether. The task tests whether the agent surfaces a concrete calendar anchor on each substantive VFX merge, which is what makes a reconciliation comment usable to the next person picking the work up. Every agent had the data; none included it.

## ART-team VFX tracker comment states that Combo-Fighters PR #37 carries unresolved CHANGES_REQUESTED review pushback despite being merged

PR #37 is merged and has one CHANGES_REQUESTED review recorded on it. The prompt names this exact pattern in the operator's own words: a merged PR whose review pushback never got resolved counts as still open. Across all six runs the string CHANGES_REQUESTED appears in zero trajectories, and no agent called the reviews descent on PR #37 specifically. Some runs called reviews on other PRs and stopped short of #37. This is a structured-database skip: agents inspected the PR list, saw #37 as merged, and did not read its review record. The task is designed to reward the agent that reads all the way down into the review payload before writing the reconciliation.

## Trello card comment identifies "Engineer to implement" as still open due to unresolved CHANGES_REQUESTED on Combo-Fighters PR #37

The Trello card comment is where the roadmap owner Oleg will actually see the reason the check_item is still open. Every run wrote a comment on the Equipped Card Item Infusion VFX card (five on the correct card, one on the wrong card), and every comment cited a different reason: a cancelled Linear ticket, no merged PR delivering the equipped-item infusion VFX, or a bare absence claim. None named PR #37 or its unresolved review. Without the PR #37 pointer the comment is not actionable. This is the intended discrimination between an agent that finds the actual blocker and one that describes the outcome without a cause.

## Status brief reports that the ZM ROADMAP check_item "Marcus to create VFX" was toggled to complete because a Marcus-authored merged Combo-Fighters VFX PR shipped

Two runs did toggle the check_item complete and stated the reason in the brief. Both cited Linear ticket ZOM-247 being marked done on 2025-06-26 as the justification, not a merged Combo-Fighters VFX PR. The prompt is explicit: close out only checklist items that the merged code actually finished. ZOM-247 being closed as a Linear ticket is a project-management artifact, not evidence that code shipped. PR #16 merged 2025-12-21 and PR #36 merged 2026-02-11 are the actual code-delivery events. Both agents that toggled the item took the Linear-status shortcut. The task rewards agents that verify against merged code rather than accepting an upstream project-management signal.

## Status brief reports that the ZM ROADMAP check_item "Engineer to implement" remains incomplete because Combo-Fighters PR #37 carries unresolved CHANGES_REQUESTED

Every brief noted the Engineer to implement item was still open, but every brief cited a different reason: a cancelled Linear ticket, no matching implementation in the repo, VFX only reaching develop and not main. None named PR #37. The brief is Victor's Monday-morning ammunition to push back on Leonard, and without the PR #37 pointer the pushback lacks substance. This criterion rewards the agent that connects the still-open check_item to the specific unresolved review on the specific merged PR.

## Reply states that Combo-Fighters PR #37 carries unresolved CHANGES_REQUESTED review pushback despite being merged

This is the artifact Victor actually reads. Across all six replies PR #37 appears zero times and CHANGES_REQUESTED appears zero times. Every reply reached the correct high-level conclusion of parking the draft and pushing back on the broader framing, but none had the specific universe fact that would let Victor cite a concrete blocker on Monday. This is the top-of-funnel test of whether the reconciliation actually surfaces the state the operator asked for.
