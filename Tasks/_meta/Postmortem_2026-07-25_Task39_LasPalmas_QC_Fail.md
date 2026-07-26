# Post-mortem: Task 39 (Las Palmas 8D) shipped a QC-fail-capable fault

Date: 2026-07-25 · Task: `Tasks/39_6a602c8886ebb06f12354d77` (StarPM V4, persona James Bennett)
Platform verdict: Reviewer f3b9ed, Poor 2/5, "full redo", parts fixed: none (July 23 2026).
Attempt id: 6a614f63de351e29a7249257.

## What the reviewer found (all 7 claims verified against this task's own data)

1. Ambiguous target record. Three tblMakeReady rows are all "Las Palmas 8D"
   (receb057b02f20052, recf7aecc318b2252, rec651427ec0d84dd5a). The prompt says
   "square up what we've got logged" and never names a row. R2/R3/R4 hard-require
   receb057b02f20052; 7 of 12 runs updated the June row instead and were failed for
   a reasonable choice.
2. One turn or two. Two rows have moveOut 2026-05-01, the third moveOut 2026-06-18 /
   targetReady 2026-06-26. Reads as two turns; setting the May row back to In Progress
   is defensibly wrong. Confirmed verbatim from the split.
3. MT-2026-1271. Created 2026-05-01, scope carpet/faucet/walls, all done per Slack, so
   closing it is reasonable; 4 Gemini runs did. No rubric scores that, while R14 rewards
   "still open." Confirmed (recac236210094352, blank fldCompletionDate).
4. Missed calendar event. gcalendar "Vendor Walk-Through - A Plus Carpet, Las Palmas 8D",
   2026-07-07, status confirmed, John Smith invited, scope = carpet replacement. Base
   universe (4_Changelog.json is [] and the inject carries no scenario data). Breaks R15
   ("carpet complete") and the "disposal is the only open item" premise (R7/R10/R13,
   OE 7/11/12). Confirmed by F9 output.
5. R6 requires unstated content. The Slack post must say 8D "should not be marketed or
   shown"; the prompt never asks for that; 0/12 runs said it, so R6 fails every run.
6. Non-atomic rubrics. R15 bundles 5 items (repairs, carpet, deep clean, punch-list,
   fridge); R11 bundles 3. R3/R4 were split correctly; the rest were not.
7. Temporal impossibility. The 2026-05-01 row reports work Slack shows happening
   2026-05-15..05-29. A record cannot report work that has not happened yet.

## How the pipeline left it (the real answer)

The gates did NOT get skipped. `_aux/` shows S0, HARDNESS, S1, S2, S3, S4, all four
AUDITs, and FINAL all ran and returned GO. They ran and were WRONG. The faults were
seen and mis-scored:

- FINAL LENS 6 wrote of R6: "mild AND-bundle ... Ship-as-is (a judge penalizing a
  correct not-ready post for missing 'don't market' = Bucket 2 judge error)." Of R11:
  "three-part finish path ... Acceptable as-is." Of R15: "five-item enumeration ...
  Acceptable as-is." All three reviewer-fatal rubrics were seen and waved through as MINOR.
- FINAL Red-Team #3 "confirmed" receb057 unambiguous because it is "the only selReady
  row." But the prompt says square up what is LOGGED, not "find the ready row." The gate
  reasoned backward from the answer it already knew, so the ambiguity that only exists for
  a naive agent was invisible. 7/12 runs proved it wrong.
- FINAL Red-Team #4 "confirmed" the disposal was the sole blocker WITHOUT sweeping
  Calendar. No lens enumerated the 2026-07-07 carpet walk.
- AUDIT scored Atomicity 5/5 using a definition that only looks for cross-action bundling,
  missing the within-criterion 3- and 5-item enumerations.
- S4 had all 12 trajectories showing the false-fails and still scored Bucket-1
  (Rubric Invalid) = 0/11, classifying "5/6 Gemini updated the June row" and "R6 failed
  6/6" as legit model failures.

Root cause: answer-anchored review with no deterministic backstop. Every human-judgment
gate reasoned from the known intended answer and mis-scored real ambiguity/bundling as
Minor, and there was no mechanical gate to override the mis-score.

## The fix (shipped 2026-07-25)

Deterministic backstops added to `Validators/v4_gates.py` `validate_submission_gate`
(v4-only phase; v3-family SKIPs, so frozen hashes untouched):

- F7 AMBIGUOUS_TARGET: a rubric pins one record id while >=2 universe rows share its
  entity and the prompt names none.
- F8 NON_ATOMIC_ENUM: one criterion enumerates >=3 conjunctive items under a
  completeness/step predicate.
- F9 UNRECONCILED_FUTURE_EVT: a confirmed calendar event dated >= universe today
  references the task entity, its date is uncited in the OEs, and the deliverables assert
  completeness.

Evidence:
- RED: `validate.py --phase submission_gate` on Task 39 flips PASS -> FAIL (6 fails:
  F7 x3 on R2/R3/R4, F8 x2 on R11/R15, F9 x1 on the 7/7 carpet walk).
- Precision: Tasks 41/43 stay PASS; Task 40 fires F7 (5 rows share "Unit 14") - a real
  second instance, not a false positive.
- Safe: check_regression 62/62 anchors, 21/21 reports, 7/7 verdicts unchanged;
  test_regression_anchors 62/62.

Run it: `python Validators/validate.py --phase submission_gate --task Tasks/<DIR>`.

## Standing rules (now codified in AGENTS.md + Rubric_Format.md + FINAL/AUDIT/S3)

1. Single-target uniqueness. Before writing any write-action rubric that pins a record,
   confirm exactly one universe record matches the prompt's described target. If two or
   more match, clean the data (V4: inject a disambiguator) or name the record in the prompt.
2. Every-service sweep incl. Calendar. Before any "complete" or "only open item" claim,
   enumerate the entity across every service, Calendar included.
3. Naive-agent ambiguity simulation. Review the prompt WITHOUT the OE in view; list every
   record/entity a reasonable agent could pick for each write ask; the rubric must accept
   every reasonable target or the prompt must disambiguate.

## Immediate follow-up

- Task 40 (`40_6a614767cd5b60ad96902fb4`) fires F7 on a "Unit 14" cross-property ambiguity
  and likely fails QC for the same reason. Re-open before/after any submission.
