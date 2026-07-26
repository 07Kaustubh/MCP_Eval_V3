# Bucket 1: Rubric Invalid

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Basis:** `8a_Verifier_Fails_Opus.txt` (13:24) + `8b_Verifier_Fails_Gemini.txt` (13:28), trajectories unchanged since 10:50.

> **Supersedes** `_superseded/pass2_2026-07-26_1245/S4_fixes.md`.

## Result: 0 open Bucket 1 entries

**Bucket 1 count: 0 of 48 failing criteria (0.0%).** No fix is required and `7_Rubrics.json` needs no further edit for S4 purposes. The set stays at 60 criteria, inside the 60-criterion hard cap.

Every failing criterion was run through the 5-point pre-write checklist before any justification was written. None returned NO on any question. The checklist results are recorded in `S4_AF_justifications.md`.

---

## Closed: the pass-2 Bucket 1 fix landed and is verified

**Criterion 48.** "The Agent's draft to Brooke Phillips names the person holding the East cluster QC confirmation, which must be one of: Elias Navarro, Jaime Salinas, or Brooke Phillips."

**Fix applied 2026-07-26 12:35, evidence field only, title unchanged.**

Before:
> Check the draft body for one of Elias Navarro, Jaime Salinas, or Brooke Phillips named as holding the outstanding East cluster QC confirmation.

After:
> Check the draft body for one of Elias Navarro, Jaime Salinas, or Brooke Phillips named as holding the outstanding East cluster QC confirmation. Because the draft is written and signed by Jaime Salinas, a first-person self-reference that assigns the outstanding East cluster QC to the sender, for example wording that says the item is owned by me or that I will run it, satisfies this criterion as naming Jaime Salinas.

**Verification against the new grading.** `Opus Run 2` was the cell the fix targeted: its draft assigns the East QC to the sender in the first person rather than by name. That cell **flipped from Fail to Pass** in the pass-3 export. `Gemini Run 5`, which pass 2 recorded as a contested cell on this criterion ("Who is Holding It: **Jaime Salinas** (QC Inspector)"), also flipped to Pass. The criterion moved from 3 Opus + 6 Gemini fails to 2 Opus + 5 Gemini fails, and every remaining fail is a draft that presents the East cluster as closed with no open QC item at all, for example `Gemini Run 4, tool call 88 (create_draft)`: "Work Owners / Open Items: None. Fully wrapped."

**Criterion 48 is therefore Bucket 3 in this pass.** The fix is closed and needs no further action.

---

## Also closed: the three `QC_Strict_Check.md` hardening edits

Applied 2026-07-26 12:58, all evidence-field only, no title or category changes.

| Criterion | Edit | Effect in the pass-3 grading |
|---|---|---|
| 11 | Clarified that the criterion grades only that tenant-access work was raised, and that one combined item or two per-cluster items satisfy it equally | No cell moved. The criterion still fails 3/6 Opus and 6/6 Gemini, in every case because no tenant-access work was raised at all. The clarification removed a latent ambiguity rather than a live false fail. |
| 22, 23, 24 | Stated that the comment target may be identified by issue identifier or internal id, both accepted | One cell moved (criterion 22, `Opus run 6`, Fail to Pass). Criterion 22 is now 0/6 on Opus. |
| 34 | Added that naming the record or its date is not required and that a paraphrase satisfies the criterion | Two cells moved to Pass on Opus (runs 1 and 3) and one on Gemini (run 4). One residual cell, `Gemini run 5`, was failed for exactly the omission the amendment waives and is filed in `S4_judge_errors.md`. |

---

## Watch item, not a fix: criterion 5

**Criterion 5.** "The Agent's West cluster tracking item states that OPS-186, dated June 17, 2026, records the West Cluster work as still underway."

Fails 12/12 across both models and is the tightest criterion in the set. It is retained as Bucket 3 because it clears all five checklist questions, but the near-miss is recorded here so a future reviewer sees it was examined rather than overlooked.

`Opus Run 6, tool call 49 (save_issue)` created OPS-1002 whose description reads: "electrical was reported \"still underway\" at the mid-initiative check-in (OPS-186), and no QC spot-check has been performed." That names the record and the still-underway status, and misses only the June 17 dating and the West-versus-electrical scoping of the claim.

**Why no fix is proposed.** The date is what makes the statement the *latest* dated status on the West cluster, which is the point of the lever: OPS-186 is the record that contradicts the crew's earlier all-clusters-wrapped message. Dropping the date would leave a criterion a run could satisfy by citing any older status. Relaxing the scoping to accept "electrical still underway" would accept a narrower claim than the record supports. Either relaxation costs the criterion its discriminating power, and no run on either model reached the full statement, so there is no achievability proof to justify the trade.

**If the platform disputes this criterion,** the fallback is to add an explicit accept-set to the evidence field, allowing the date to be given either as June 17, 2026 or as the mid-initiative check-in, with the title unchanged. That preserves the lever and removes the most literal reading. It is not applied here because Bucket 1 is empty on the evidence available.
