# changes.md — Task 31_6a3f7eecacba1ccbe57db14d

Review verdict: **SALVAGEABLE**. Two findings (1 Minor wording defect + 1 Note-level evidence-anchoring polish). After both rows are marked Applied, re-invoke `PIPELINE REVIEW — Tasks/31_6a3f7eecacba1ccbe57db14d` to materialize `15_Updated_Rubrics.json` with the fixes.

The hardness anatomy is empirically validated (pass@1 = 16.7%, avg tool calls = 59.8) and does not need a rebuild. Originals `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` stay untouched.

| # | Phase | Dimension | Severity | Before | After (proposed) | Why | Verified | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Rubrics | Overall Rubric Quality (wording — vague connector) | Minor | rubric[8] / R9 title: "The Agent circulates the finalized return package toward Northstar Legal's external client signatory (its managing partner) for the client signature, and does not treat a Brookfield-internal partner **such as Steven Perry, Ming Chang, or Matthew Li** as the signatory." | rubric[8] / R9 title: "The Agent circulates the finalized return package toward Northstar Legal's external client signatory (its managing partner) for the client signature, and does not treat any of the Brookfield-internal partners Steven Perry, Ming Chang, or Matthew Li as the signatory." | The vague connector `such as` is forbidden in rubric titles per `Reference/Rubric_Format.md` and the QC spec's canonical-pattern rule (`must be one of` / `including but not limited to` / `at least one of`). The three names are not examples of a larger class — they are the closed set of Brookfield internal partners that could be plausibly confused for the external Northstar signatory (Steven Perry = Managing Partner; Ming Chang = Tax Partner; Matthew Li = Accounting Services Partner per `Brookfield_Base_Universe/2_Persona_Briefs.md`). Replacing `such as` with `any of` presents them as a closed disjunctive set and satisfies the validator. | yes — confirmed by `Validators/validate.py --phase rubrics` (FAIL on `forbidden vague connector 'such as'`) and by persona briefs (the three named partners are the only internal partners that map to a "managing partner"-adjacent signatory role) | **Applied** |
| 2 | Rubrics | Convention (evidence anchoring) | Note | rubric[3] / R4 evidence starts: "PASS via either path. (i) The Agent attempts a create-journal-entry call for northstar_legal targeting period northstar_legal_FP-2025-12, the system returns a closed-period error..." | rubric[3] / R4 evidence starts: "Look for either path. (i) The Agent attempts a create-journal-entry call for northstar_legal targeting period northstar_legal_FP-2025-12, the system returns a closed-period error..." | Validator note: evidence neither references an OE step nor uses trajectory-anchoring phrasing (`Look for` / `Check the` / `Verify that` / `Inspect` / `Confirm` / `payload` / `final response`). Adding `Look for` as the prefix anchors the judge to the trajectory pass-check. Trivial wording polish, no semantic change. | yes — flagged by `Validators/validate.py --phase rubrics` warn list | **Applied** |

## Findings dismissed without a row

Five validator findings were verified against the per-task universe and dismissed as heuristic false-positives (see `_aux/Council_Reports/REVIEW_dismissed.md` for the per-finding verification):

1. Prompt `bolt-on candidate` warning on Hannah/Tom-routing sentence — false positive (sentence is anaphorically connected to the rest of the prompt via "her note", "Tom's draft work", references to the data package / year-end / not-released state).
2. Prompt `bolt-on candidate` warning on closing actions sentence — false positive (sentence is the closing-actions paragraph, references "the reconciliation" and "that entry" both established earlier).
3. OE 15 contact-lookup warning — false positive (the email validator latched onto William's address as the sender, not the recipient; the recipient is external Northstar MP with no stored contact — the rubric R9 explicitly accepts this).
4. R1 / R2 / R3 / R11 evidence-stricter-than-criterion — false positive (criterion grades the derived figure; evidence provides derivation components for the judge to recognize the agent's computation path — V3 reference pattern).
5. R1 / R2 / R3 derived dollar amounts not in Universe_Split — false positive (computed values like $131,135.84 = $139,441.10 − $8,305.26 are NOT stored in the universe; the components ARE stored and verified).

## Triage detail

Per AGENTS.md triage table:

| Trigger row | Fired? | Reason |
|---|---|---|
| Any QC sub-dim 1-2 FAIL | NO | Worst sub-dim is Rubrics Overall Quality at 3 (NON-FAIL band); after R9 fix → 5. |
| Hardness fails (pass@1 > 0.40 OR avg tool calls < 40 OR B3 projected density < 40 OR B4 levers don't trigger OR FINAL answer leakage) | NO | All thresholds met: pass@1 = 0.167, avg 59.8, all 3 hardness levers (L1 confirm-already-done placeholder, L9 authority dismissal on recurring framing, L8 multi-link SAP depreciation derivation) empirically triggered |
| Otherwise SALVAGEABLE | **YES** | Apply rows above. |

## What lands when rows are Applied

- Row 1 Applied → `15_Updated_Rubrics.json` regenerated with R9 title `such as` → `any of`.
- Row 2 Applied → `15_Updated_Rubrics.json` regenerated with R4 evidence prefixed `Look for either path. (i) ...`.

Both rows are rubric-phase fixes. **No prompt edit needed** → no `_aux/REVIEW_prompt_draft.txt`. **No OE edit needed** → no `14_Updated_Oracle_Events.txt`.

On materialization, the corrected `15_Updated_Rubrics.json` will be re-run through `validate.py --phase rubrics` + Council A + Council B + AUDIT + FINAL per step 11 of the REVIEW runbook. Originals 5/6/7 stay pristine.

## Materialization complete (second REVIEW pass — 2026-06-27)

Both rows above marked **Applied** by the user. This second REVIEW invocation materialized the corrected deliverables and re-ran all gates per runbook step 11.

- `15_Updated_Rubrics.json` written with both fixes (R9 closed-set wording + R4 trajectory anchor).
- Originals `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` **UNTOUCHED**.
- No `14_Updated_Oracle_Events.txt` (no OE rows Applied).
- No `_aux/REVIEW_prompt_draft.txt` (no prompt rows Applied).

### Gate results on corrected `15_Updated_Rubrics.json`
- `validate.py --phase rubrics`: **PASS** — 0 fails, 17 warns, 3 notes (down from 1 fail, 18 warns on the original; remaining 17 warns are all in the dismissed-as-FP bucket per `_aux/Council_Reports/REVIEW_dismissed.md`).
- `test_regression_anchors.py`: **33/33 PASS**.
- `calc_similarity.py`: all composites < 40 (clear of ceiling).
- **AUDIT --phase rubrics**: **PASS (STRICT)** — see `_aux/Council_Reports/AUDIT_rubrics.md`. All 12 rubric QC sub-dims 5/5 strictest; zero answer-leakage; all 3 hardness levers trace end-to-end; density 59.8 avg clears 50+ design target; all 5 dismissed validator FPs re-confirmed under strict reading; 33/33 regression anchors PASS; LENS 9 middle-band ambiguities are rubric-acceptable.

### Next trigger
`PIPELINE FEEDBACK — Tasks/31_6a3f7eecacba1ccbe57db14d` in a fresh chat to write `13_Feedback.txt` (rating the candidate's ORIGINAL submission against the QC spec baseline; strict input allowlist).
