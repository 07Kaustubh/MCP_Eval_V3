# Verification — PIPELINE S4 · Task 43_6a62ccaf5853030245ac9d53

**Universe:** StarPM V4 (dual-model: 6 Opus 4.8 + 6 Gemini 3.6 Flash) · **Persona:** Carlos Mendez, Onsite Property Manager · **Today in-universe:** 2026-07-01 America/Chicago · **Date run:** 2026-07-25

## Sources consulted
Categories covered: **Per-task data**, **Eval spec**, **QC spec**. Full read log in `_aux/Reads_s4.md`.

- **Per-task data** — `_aux/Universe_Split/quickbooks.quickbooks_entities.json` (the 4 AP bills + AR invoice 2026-534 re-read by id, field by field), `contacts.contacts.json` (Tony Reyes / Pete Donovan / Linda Castillo role and domain), `gmail.gmail_messages.json` (message `5101c5a41dffa90a`, body base64-decoded), `airtable.airtable_records.json` (both 4C make-ready rows), `_aux/Fact_Ledger.json` (amount atoms; 1812 absent, confirming derive-only).
- **Eval spec** — `Evals_starpm/4_Verifier_Fails_Eval.md` bucket taxonomy re-applied once per model per the eval's own mandate; `Reference/Sessions/S4.md` procedure, T1/T2/T3 gates, v15 5-point checklist, All-Failing Rubrics threshold table.
- **QC spec** — `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md` trajectory sub-dims; `AGENTS.md` hard rule 11 (V4 density is per-model, 40 design target, 15 fail floor, NOT the Brookfield 50/40 scheme).
- **Task artifacts** — `7_Rubrics.json` (25 criteria), `8a_Verifier_Fails_Opus.txt` + `8b_Verifier_Fails_Gemini.txt` (12 run blocks, 300 graded cells), `Agent_Responses/{Opus,Gemini}/trajectory-run-{1..6}.json` (all 12 walked), `5_Prompt.txt`, `6_Oracle_Events.txt`, `_aux/Hardness_Plan.md`, `_aux/Verification_final.md`.
- **Tool catalog** — `StarPM_Base_Universe/7_Server_Tools_Details.json` to establish that the gmail surface exposes no plaintext message read.

## Eval spec verified
- `Evals_starpm/4` bucket taxonomy (Rubric Invalid / Judge Error / Legit Fail) re-applied to all 15 failing rubrics, independently per model set.
- The v15 5-point pre-write checklist was applied before every AF justification. Two criteria returned NO on first pass and were escalated to a full Bucket 1 examination; both were resolved back to Bucket 3 with the reasoning recorded in `S4_fixes.md` rather than waved through.
- Deviation table (`AGENTS.md`) honoured: the pipeline exceeds `Evals_starpm/4` Phase 3.3 by having full trajectory access, and the trajectory walk was made mandatory for every bucket call including Bucket 3.

## QC spec sub-dims verified
- **All-Failing Rubrics sub-dim** — Bucket 1 ratio computed and scored: 0/15 = 0.0% → 5/5 PASS.
- **Trajectory T1 (density)** — per model, against the StarPM 40 design target / 15 fail floor. Opus 41.7 PASS; Gemini 36.8 THIN, clear of the floor.
- **Trajectory T2 (pass@1 ≤ 40%)** — 0.0% on both models and combined. PASS.
- **Trajectory T3 (≤ 2 error runs)** — 0 of 12 errored. PASS.

## Verification statements
- [x] `phase_ready.py --phase s4` exit 0. Initially blocked on the upstream `Verification_final.md` heading contract (`## Data sources consulted` vs the required `## Sources consulted` plus the three source-category labels). Heading normalised and category labels added; no substantive content of the FINAL verification was altered. Re-run clean.
- [x] `parse_trajectories.py` run; `_aux/Trajectory_Stats.json` written with measured per-model pass@1 and density. Neither `REBUILD_CANDIDATE_DENSITY` nor `REBUILD_CANDIDATE_DIFFICULTY` returned.
- [x] Rubric × run matrix built for all 25 rubrics × 12 runs (300 cells), parsed from `8a`/`8b` rather than transcribed by hand. All 25 titles reconciled against `7_Rubrics.json`; the one mismatch was a platform-side markdown mailto link on the email-draft criterion, normalised, zero unmatched titles remaining.
- [x] **Trajectory walk recorded for EVERY failing rubric, not just Bucket 2.** Every bucket entry carries a `Run X, tool call Y` citation or an explicit not-attempted citation.
- [x] T2 and T3 hard gates evaluated and recorded in `S4_verdict.md`.
- [x] Bucket 1 ratio computed; All-Failing Rubrics sub-dim scored 5/5.
- [x] 5-point checklist confirmed YES on all five before each AF justification; the two NO results are documented as rejected Bucket 1 candidates.
- [x] `check_justification.py` exit 0 on the AF batch (0 hits). Em-dashes removed (1 found in the title, corrected).
- [x] Every Bucket 1 / Bucket 2 call re-confirmed against `_aux/Universe_Split/` by direct re-grep of the source rows, not by trusting upstream phase claims.
- [x] Hardness calibration written against the pre-registered predictions in `_aux/Hardness_Plan.md`, including the FINAL-council carry-forward re-attribution.
- [x] `Tasks/_meta/Stump_Hypotheses.md`, `Tasks/_meta/Hardness_Patterns_Log.md` and `Tasks/_meta/Learnings.md` updated.

## Ground truth re-derived from source (not taken from upstream phases)

| Component | Bill id | DocNumber | `VendorRef.name` | Amount | Invoice 2026-534 line | Owner-billable |
|---|---|---|---|---:|---|---|
| Post-move-out deep clean | `195089456477` | 2026-SC-4C | Sunshine Cleaning | 387.00 | line 1 = 387.00 | yes, ties |
| Interior repaint | `696089964235` | PD-2026-09 | Permian Make-Ready Crew | 1340.00 | line 2 = 1140.00 | yes, **200 understated** |
| Bedroom closet trim touch-up | `546359391323` | 2026-519 | **Permian Make-Ready Crew** | 85.00 | line 3 = 95.00 | **yes, 10 overstated** |
| Unit condition walk | `991582431419` | 2026-481-566 | Alamo HVAC Services | 85.00 | absent | **no, in-house time** |

Correct pass-through 387 + 1340 + 85 = **1812.00** against invoice `445653930748` (TotalAmt/Balance 1622.00). Net **190.00** understated. Decoys recompute exactly: 1897 (adds the condition walk), 1727 (drops the closet trim), 1810 (substitutes the 385.00 Rio Bend deep clean).

The two $85 bills were separated on evidence, not on keyword: both `PrivateNote` fields open with "Internal labor charge for <a StarPM person>". `546359391323` is billed by an outside vendor and its note instructs "Pass-through to owner"; `991582431419` is Carlos's own walk and carries no pass-through instruction. The prompt's exclusion is narrowed to "an internal walk or a condition check", which matches the second bill and not the first.

## Discrepancies surfaced

1. **[FIXED — gate blocker]** Upstream `Verification_final.md` used `## Data sources consulted`, which `check_verification.py` rejects (it requires the literal `## Sources consulted` plus the categories `Per-task data` / `Eval spec` / `QC spec`). This blocked `phase_ready.py --phase s4` at exit 1. Heading normalised and a category line added. **Root cause is a template-vs-checker mismatch, not an operator lapse**: the runbook templates in `Reference/Sessions/*.md` (S4's own Step 0.5 included) print `## Data sources consulted`, while the checker demands `## Sources consulted`. 27 verification files across the repo use the rejected wording and 46 use the accepted one. Worth reconciling at the source; flagged to the operator, not fixed repo-wide here.

2. **[NO ACTION — recorded]** 6 judge run-cells are wrong. 2 wrong-FAIL on the closet-trim-amount criterion (Opus runs 2 and 3, inconsistent enforcement of an evidence-field vendor attribution that runs 1, 4 and 6 were waived on) and 4 wrong-PASS on the two Airtable criteria (Opus runs 2 and 4 wrote only to the stale In Progress row, which the evidence field explicitly excludes; Gemini run 3 did the same and was correctly failed). Detail and the full write-target table in `S4_judge_errors.md`. No rubric-level Bucket 2.

3. **[NO ACTION — design finding]** The corroborating evidence that OE 7 designates as the resolver for the central classification is inert in practice. `get_thread` returns the message body base64-encoded and the StarPM gmail surface has no plaintext read tool. 9 of 12 runs made the prescribed call; 0 decoded the payload. The rubric survives on `VendorRef` plus the note's pass-through clause, so this is not a defect in this task, but it is a design rule going forward and is banked in `Learnings.md` item 17.

4. **[NO ACTION — concentration risk, disclosed]** 9 of the 15 failing rubrics rest on one classification call. Each is individually atomic and correctly decomposed per the write-action-per-rubric rule, so this is not a bundling defect, but a reviewer who disputes the closet-trim ground truth takes down 9 criteria at once. The counter-argument is written out in `S4_fixes.md` Candidate 1.

5. **[NO ACTION — expected challenge]** The email-closure criterion is the weakest in the set: the prompt binds "fully closed" to the Airtable record and asks the email only to say "where it landed". It passed 6 of 12 runs and its evidence field accepts three expressions, so it discriminates rather than blocks. Counter-argument in `S4_fixes.md` Candidate 2.

6. **[NO ACTION — prediction corrected, not a defect]** Three of four pre-registered stump predictions were wrong in direction or magnitude. The FINAL-council carry-forward predicted this and named the correct replacement mechanism in advance. Calibration recorded in `Hardness_Patterns_Log.md`; no artifact change.

## Verdict

**PASS.** All three trajectory gates clear on both models. Bucket 1 empty, so `7_Rubrics.json` ships unchanged. The AF batch is voice-gate clean and ready for the platform. No re-run and no REDO. Next trigger: `PIPELINE CLOSE — Tasks/43_6a62ccaf5853030245ac9d53`.
