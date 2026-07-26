# STATUS: APPLIED + VALIDATED (Opus + Gemini) 2026-07-23
R12 split applied to 7_Rubrics.json (16 -> 17 rubrics: R12a owner-approved + R12b JP-coordination/not-closed).
validate.py --phase all PASS (prompt 0F/0W, oe 0F/0W, rubrics 0F/4W - no new warns).
VALIDATED on BOTH models. Opus post-split re-run (8a, 17 criteria): R12a passes 6/6; R12b is atomic and fails only run 1 (genuine JP-coordination omission); the old combined rubric's EVF-id grading inconsistency is eliminated (old Opus run 5 failed combined, now passes both halves because the EVF-2026-014 token is optional grounding, not a graded string). Gemini post-split re-verify (8b, 17 criteria): R12a 6/6 pass, R12b 6/6 pass - the same six trajectories that graded inconsistently under the combined rubric now grade cleanly. No remaining gate.

# S4 Fixes (Bucket 1 - Rubric Invalid) - Task 40_6a614767cd5b60ad96902fb4

## R12 - "eviction filing owner-approved (EVF-2026-014) but still in JP coordination, so not closed"
Classification: Bucket 1 (Not Atomic + inconsistent grading). Applies to both models.

Evidence from the trajectories:
- Two independently-verifiable claims that fail independently: the EVF-2026-014 identifier and the Justice-of-the-Peace coordination status. Opus run 1 stated EVF-2026-014 but omitted the JP-coordination clause (fail); Opus run 5 and Gemini runs 1, 2, 6 gave the owner-authorization plus JP substance but omitted the EVF-2026-014 id (fail). The two halves land in opposite runs, which is the Not-Atomic signature.
- Inconsistent grading tied to the ambiguous "(EVF-2026-014)" parenthetical. Gemini runs 4 and 5 PASSED in the same state that failed runs 1, 2, 6: the judge wrote "the EVF-2026-014 ID is not mentioned by name but the substance is present" on a PASS (run 4) and "the specific filing reference required by this criterion is absent" on a FAIL (run 1). Same condition, opposite verdicts.

Before:
"The Agent's email to Brooke states that the eviction filing is owner-approved (EVF-2026-014) but still in coordination with the Justice of the Peace, so the matter is not closed."

After (split into two atomic rubrics; EVF id becomes optional grounding, not a graded token):
- R12a: "The Agent's email to Brooke states that the eviction filing is owner-approved and authorized to proceed."
- R12b: "The Agent's email to Brooke states that the eviction is still in Justice-of-the-Peace coordination and the matter is not closed, so possession has not been returned."

Both halves stay grounded: EVF-2026-014 owner approval is on the maintenance ticket (OE 5), the JP coordination is in the make-ready note and the Slack thread (OE 3 / OE 6). Splitting removes the independent-fail bundling and the identifier ambiguity that produced the inconsistent grading. Re-graded on both models, the halves grade cleanly: Opus R12a 6/6 pass + R12b 5/6 (one run-1 omission); Gemini R12a 6/6 pass + R12b 6/6 pass. The inconsistency is gone.

Scope note: R12 is a partial-fail rubric (Opus 4/6 pass combined, Gemini 3/6 pass combined), not an always-failing rubric, so it does not enter the All-Failing Rubrics Bucket-1 ratio. It was a Major (Not Atomic) rubric-quality defect; the split fix is applied to 7_Rubrics.json and validated on both models, so the shipped 17-rubric set is a clean 5/5.

## R10 - re-confirmed ATOMIC (not a fix)
R10 couples the amount 2,132.00 with bill QR-2026-0441, but both come from the same QuickBooks bill record and never failed independently (every failing run was at a wholly different figure). Two facts from the same record are acceptable bundling. R10 stays Bucket 3.
