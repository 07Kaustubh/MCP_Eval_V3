# Verifier Fails - S4 verdict (Task 40_6a614767cd5b60ad96902fb4, StarPM V4, dual-model)

Universe: starpm (V4). Models verified: Opus 4.8 + Gemini. Classification run once per model per Evals_starpm/4.

INPUT NOTE (v4 Gemini re-verify closure, 2026-07-23): both verifier files are now on the SAME 17-rubric split set.
- `8a_Verifier_Fails_Opus.txt` (mtime 21:56) = post-split re-run, 17 criteria per run: R12 = R12a + R12b.
- `8b_Verifier_Fails_Gemini.txt` (mtime 22:31) = post-split RE-VERIFY, 17 criteria per run ("15/17 passed" on 5 of 6 runs): R12 = R12a + R12b, re-graded on the SAME six Gemini trajectories (tool-call counts 47/45/37/38/33/40 unchanged - a re-grade, not a fresh agent run).
- `7_Rubrics.json` = the 17-rubric split set; its R12a/R12b criterion text is byte-identical to what BOTH platforms graded (no rubric drift).
This pass closes the one open action from the v3 verdict: the Gemini re-verify on the split set has arrived and REPLICATES the Opus validation - R12a passes 6/6 and R12b passes 6/6 on Gemini, retiring the stale combined-R12 evidence. The R12 split is now VALIDATED ON BOTH MODELS. Zero open actions remain except shipping the AF justifications.

## Trajectory gates (per model)
- T3 Error Rate: Opus 0/6, Gemini 0/6 erroneous runs. PASS (< 3 each).
- T2 Agent Failure Rate: Opus 0/6, Gemini 0/6 runs passed every criterion. Overall pass@1 0.0%. PASS (<= 40%).
- Density (StarPM 40+): Opus 41.5 (31/40/47/39/47/45), Gemini 40.0 (47/45/37/38/33/40), overall 40.8. PASS.

## Run matrix (F = fail; . = pass)
OPUS (8a, 17-rubric split) pass/run: 13,14,15,13,12,12 of 17 -> AF: R10 ; partial: R1,R5,R8,R12b,R13,R15,R16
GEMINI (8b, 17-rubric split re-verify) pass/run: 15,15,15,15,14,15 of 17 -> AF: R10,R13 ; partial: R8
```
                 OPUS R1..R6        GEMINI R1..R6
R1   updRec      F F F F . F  (5)   . . . . . .  (0)
R5   slackBreach . . . F . .  (1)   . . . . . .  (0)
R8   identUnit   F . . . F .  (2)   . . . . F .  (1)
R10  arrears     F F F F F F  (6)   F F F F F F  (6)
R12a ownerAppr   . . . . . .  (0)   . . . . . .  (0)
R12b jpNotClosed F . . . . .  (1)   . . . . . .  (0)
R13  ESA         . F . F F F  (4)   F F F F F F  (6)
R15  OPS-32      . . . . F F  (2)   . . . . . .  (0)
R16  OPS-32 body . . . . F F  (2)   . . . . . .  (0)
(R2,R3,R4,R6,R7,R9,R11,R14 pass 6/6 both models)
```

## Classifications (every failing rubric walked against its trajectory)
Bucket 1 (rubric invalid): R12 combined -> RESOLVED by the split (applied to 7_Rubrics.json) and now VALIDATED ON BOTH MODELS (Opus post-split 8a + Gemini post-split 8b re-verify). See S4_fixes.md.
Bucket 2 (judge error): 0 -> see S4_judge_errors.md.
Bucket 3 (legitimate model failure): all other failing rubrics -> AF justifications for the always-failing ones (R10 Opus, R10 Gemini, R13 Gemini) in S4_AF_justifications.md.

### R12 split - VALIDATED ON BOTH MODELS (the core result, now closed)
- R12a "The Agent's email to Brooke states that the eviction filing is owner-approved.": Opus 6/6 Pass, Gemini 6/6 Pass. Owner authorization (Linda Castillo, 6/30) was stated in every run on both models; graded cleanly and independently.
- R12b "...the eviction is still in Justice of the Peace coordination and the matter is not yet closed.": Opus Fail run 1 only (5/6 Pass); Gemini 6/6 Pass. Opus run 1's email omitted the JP-coordination substance (judge: "does not mention 'Justice of the Peace' or JP coordination") - a Bucket 3 partial fail, atomic, graded consistently across runs. Gemini stated the JP substance in all six.
- Fix confirmation (both models): under the OLD combined rubric the id-absent state graded inconsistently (Opus failed runs 1 AND 5; Gemini failed 1,2,6 but passed 4,5 in the same state). Under the split, the "(EVF-2026-014)" token is optional grounding, not a graded string: Opus run 5 now passes both halves, and Gemini grades R12a/R12b consistently 6/6. The judge inconsistency is GONE on both models.

### OPUS Bucket 3 detail
- R1 (5/6) Bucket 3. Every failing run updated receee45491536859 ("Unit 14 - Tanya Mitchell Eviction", the eviction-package decoy) instead of the make-ready-hold accept-set recc83c05d889b354 / reca8230a8fd9ff51. OE 14 blesses exactly those two ids and excludes Rio Bend. Achievable: run 5 hit recc83c05d889b354; Gemini hit the accept-set 6/6. Near-miss cross-record lever fired on Opus.
- R5 (1/6, run 4) Bucket 3. Run 4 make-ready Slack message omitted the payment-plan breach. Achievable (5/6 pass).
- R8 (2/6, runs 1,5) Bucket 3. Used vague "Harris property"/"Harry Harris" with no Sunset Ridge naming or Rio Bend distinction; passing runs used "1402 Rimrock". Judge correct.
- R10 (6/6) Bucket 3 AF. Opus never queried the bills ledger in any run (no search_bills/get-bill); it worked customers, invoices, payments. QR-2026-0441 surfaced in a search result each run and the 2,132.00 value was visible in runs 1,3, yet every email quoted a reconstructed ~2,287.50 or invoice 7214's 8,173.44. The authoritative figure was in context and unused.
- R12b (1/6, run 1) Bucket 3 partial. See R12 split section above.
- R13 (4/6, runs 2,4,5,6) Bucket 3. ESA omission. Achievable (runs 1,3 passed). Run 4 surfaced the ESA in results but omitted it from the email; runs 5,6 used only a broad crm search that did not surface it. HubSpot/thread carry-through failure.
- R15 (2/6, runs 5,6) Bucket 3. Trajectory: runs 5,6 never wrote save_comment on OPS-32 (run 5 "No comment was added to OPS-32"; run 6 updated an Airtable record instead). Action not attempted; no comment for a judge to misread.
- R16 (2/6, runs 5,6) Bucket 3. Same root cause as R15 (no OPS-32 comment written).

### GEMINI Bucket 3 detail (8b post-split re-verify)
- R8 (1/6, run 5) Bucket 3. Same identity miss in one run. Achievable (5/6 pass).
- R10 (6/6) Bucket 3 AF. Never queried the bills ledger (no bills call, QR-2026-0441 never in trajectory); searched invoices/payments, rebuilt ~2,287.50, once fell back to 8,173.44. Authoritative 2,132.00 never surfaced.
- R13 (6/6) Bucket 3 AF. Gemini searched CRM objects and mail threads; the approved ESA surfaced in the results every run (approval thread in 5/6), yet every email omitted the fair-housing consideration. Carry-through failure, not a discovery failure.
- R12a/R12b: both 6/6 Pass on the re-verify (previously a combined-R12 Bucket-1 artifact on the pre-split 8b; now retired).

## All-Failing Rubrics sub-dim (Bucket-1 ratio over AF rubrics only)
- OPUS: AF = {R10}. Bucket-1 among AF = 0. 0/1 = 0% (< 25%) -> 5/5 PASS.
- GEMINI: AF = {R10, R13}. Bucket-1 among AF = 0. 0/2 = 0% (< 25%) -> 5/5 PASS.
The always-failing rubrics are all legitimate model failures. R12 was a partial-fail rubric, so it never entered this ratio. With the split APPLIED to 7_Rubrics.json AND VALIDATED on BOTH models, the Not-Atomic defect is fully resolved for the shipped rubric set, so the overall Rubric-quality dimension is 5/5. No caveat remains: the Gemini platform verifier has re-run on the split and R12a/R12b both pass 6/6.

## Hardness calibration
- S2 delinquency-supersession -> arrears source (R10): PREDICTED + FAILED, 0/12, model-symmetric. Sharper than first thought: the authoritative bill is an AP bill that agents never search; even when it surfaced in an invoice result (Opus runs 1,3) the figure was not used.
- S3 HubSpot ESA structured skip (R13): PREDICTED + FAILED. Gemini 6/6, Opus 4/6. Refined: not a pure "skip" - Gemini and Opus run 4 RETRIEVED the ESA and still omitted it. The stump is carry-through, not discovery.
- S4 near-miss cross-record Unit 14 (R1): PREDICTED + FAILED for Opus (5/6), OVER-PREDICTED for Gemini (0/6).
- S1 possession-hold + S5 false owner sign-off: guardrails held (R2/R3/R6/R11/R9 pass); not stumps.
- Rubric-atomicity calibration (confirmed dual-model this pass): the R12 split re-verify on BOTH models confirmed the "(EVF-2026-014)" token was the inconsistency source, not a real difficulty lever. Demoting it to optional grounding flipped the stale false-fails to passes (Opus run 5) and graded R12a/R12b consistently 6/6 on Gemini, isolating the one genuine JP-coordination omission (Opus run 1) into R12b. Splitting a bundled Outcome rubric can raise measured difficulty accuracy without changing task difficulty (pass@1 stayed 0% on both models).

## Corrections applied across passes
v4 (Gemini re-verify closure, this pass):
1. Gemini matrix rebuilt from the NEW 17-criterion 8b re-verify: R12 -> R12a (6/6 pass) + R12b (6/6 pass); R8 partial (run 5); R10 + R13 AF unchanged.
2. R12 split now VALIDATED ON BOTH MODELS; the stale combined-R12 8b caveat retired.
3. All-Failing / Rubric-quality caveat cleared (no pending platform re-verify).
4. Corrected the Opus pass/run counts: runs 5 and 6 are 12/17 each (the v3 verdict recorded 10/17 and 11/17 in error; the 8a run headers read 12/17).
v3 (post-split Opus re-verify):
1. Opus matrix rebuilt from the 17-criterion 8a: R12 -> R12a (6/6 pass) + R12b (1/6, run 1).
2. R12b Opus run-1 logged as a Bucket 3 partial fail.
v2 (skeptical re-verification):
1. R10 Opus AF justification re-grounded (surfaced QR-2026-0441 in-result but never queried the bills tool and used the wrong figure).
2. R13 Gemini AF justification re-grounded (Gemini queried CRM/threads, the ESA surfaced, the email omitted it).
3. R12 re-classified Bucket 3 -> Bucket 1 (non-atomic + judge inconsistency), with a split fix.

## Action items
- [DONE 2026-07-23] R12 split applied to 7_Rubrics.json (16 -> 17: R12a owner-approved + R12b JP-coordination/not-closed); validate --phase all PASS.
- [DONE 2026-07-23] R12 split VALIDATED on the Opus post-split re-run: R12a 6/6 pass, R12b atomic (only run-1 legit fail), EVF-id inconsistency eliminated.
- [DONE 2026-07-23] R12 split VALIDATED on the Gemini post-split re-verify: R12a 6/6 pass, R12b 6/6 pass; stale combined-R12 8b evidence retired.
- Ship the three Bucket 3 AF justifications (R10 Opus, R10 Gemini, R13 Gemini) - voice gate clean.
- No Bucket 2 appeals.
- No REDO: difficulty (pass@1 0%), density (40.8), and error-rate (0) gates all pass on both models.
- Keep the parse_trajectories.py Gemini-format fix (regression 62/62 / 21/21 / 7/7).

## Verdict
PASS on difficulty + density + error-rate for both models. The single Bucket-1 defect (R12 non-atomic + inconsistent grading) is FIXED (split applied to 7_Rubrics.json) and now VALIDATED ON BOTH MODELS: R12a passes 6/6 on Opus and Gemini, R12b passes 5/6 on Opus (one run-1 legitimate omission) and 6/6 on Gemini, and the EVF-id grading inconsistency is eliminated on both. Rubric-quality is 5/5 for the shipped 17-rubric set with zero remaining caveat. All AF justifications are re-grounded and voice-gate clean. No open platform follow-up remains. Task is a keeper; not a REDO.
