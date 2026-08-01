# S3 Reads Log — Task 45 (StarPM V4)

Every QC spec doc / Reference card / Eval spec / reference rubric read during S3, one line each.

## Runbook + gates
- Reference/Sessions/S3.md :: S3 procedure, exit criteria, 60-cap budgeting, ordering-coverage rule, signal-cut-before-trim.
- Validators/phase_ready.py + check_verification.py :: s3 gate delegates to check_verification (requires Sources consulted + Verdict + Per-task data/Eval spec/QC spec source categories).

## Deliverables under rubric
- 5_Prompt.txt :: HOLD scenario; 6 asks (record QC determination + give call; open ticket; post make-ready channel; email Carlos; notify Brooke before marketing). Standard: billed-but-unfinished OR finished-with-bill-unpaid != closed; 7/15 re-inspection factors in.
- 6_Oracle_Events.txt :: 15 OEs; correct call HOLD on recbd087a4abd605b; writes OE10-15; final-response fact list.

(appended below as read)


## Framework + format (rubric authoring SSOT)
- Reference/Rubric_Format.md :: FLAT 4-field schema; agent-centric; no tool names in title; no "at least N"; self-contained; atomic; single-target uniqueness; split 3+ item enumerations (F8); sub-cats 1.1/1.2/2.1; absolute-count dilution gates (<30 rubrics).
- Docs_starpm/2_Rubrics_V3_Guidelines.md :: Outcome default / Process rare (three-condition test); "approximately" only for calculated/rounded NOT fixed/counts/IDs/dates; method-agnostic where prompt names a goal; service metadata; one rubric per multi-item write.
- Docs_starpm/9_Common_Error.md :: Part 3 — no process for outcome-covered; NO single-channel forcing; no cross-call bundling; self-contained; values match universe; reverse-coverage; no "approximately" on fixed values; all-6-fail removed unless vehemently defensible (rule 21).

## Task-specific inputs
- _aux/Hardness_Plan.md :: 5 levers L2(sym)/L1+L10(opus)/L31(gemini)/L7/L9. QC-status rubric binds recbd087, checks NOT-advanced-to-Ready + hold recorded, never a hold enum, not satisfiable by the "done" ticket or prior selReady recc8534. Density THIN accepted per-model.
- _aux/Fact_Ledger.json :: 403 amounts (387.00, 1340.00, 1622.00 present), 206 emails.

## Reference rubric corpus (V4 voice SSOT — Brookfield-flavored, voice only)
- QC_Passed/Task1 (32) :: multi-write 1.1/1.2/2.1; method-agnostic notify; valid negative outcome; record ids in titles; evidence describes ACTION not tool fn; same fact in 2 artifacts w/ cross-ref in justification (R31).
- QC_Passed/Task2 (14) :: exact amounts as hard requirements; distinct vendors => distinct rubrics; email content lists items.

## QC spec (Docs_starpm/7_QC_Spec_Doc1.json — Rubric dimension) + severity
- Rubric Category Balance (BINARY): outcome 18 > process 0 => PASS. Severity ladder (Doc2 07/16): Overly Specific=MODERATE, Overly Broad=MINOR; Pass(5) needs 0 Major + 0 Moderate.

## Deterministic gate results (this phase)
- validate.py rubrics :: PASS 0 fails / 8 benign warns / 5 notes; outcome=18 process=0.
- check_ordering_coverage :: OK (no ordering => 0 process correct).
- check_rubric_signal :: SKIP (no verifier export; CB pre-upload). 18 << 60 cap.
- check_qc_binary :: Rubric Category Balance PASS; lone FAIL = Prompt/Coherence heuristic FP (action-directive sentence, 24% vs 0.25 threshold; passes spec's sentence-removal test; S1 AUDIT PASS STRICT; prompt S1-locked, not a rubric defect). Council B adjudicating.