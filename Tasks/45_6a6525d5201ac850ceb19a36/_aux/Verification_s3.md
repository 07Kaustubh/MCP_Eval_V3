# S3 Cross-Source Verification - Task 45 (StarPM V4) - Rubrics

Deliverable: `7_Rubrics.json` (19 Outcome, 0 Process). Universe: **starpm**. Universe today 2026-07-01 America/Chicago. Correct answer = HOLD / kick-back on Mesa Vista 4C current turn recbd087a4abd605b (selProg).

## Sources consulted
- Per-task data :: `_aux/Universe_Split/` :: Council A independently re-grounded every concrete value in all 19 rubric titles + evidence: recbd087a4abd605b (selProg, move-out 2026-06-15, target 2026-06-30) vs the recc8534b3fd13954 selReady decoy; the two unpaid carrying-scope bills (Sunshine Cleaning deep-clean balance 387.00 id 195089456477; Permian interior-repaint balance 1340.00 id 696089964235); the 2026-07-15 QC re-inspection event; C004 = #make-ready; Operations team key OPS; carlos.mendez / brooke.phillips @starpm.com; selProg = In Progress / selReady = Ready. No drift.
- Per-task data :: `_aux/Fact_Ledger.json` :: amounts 387.00 / 1340.00 present, emails present, record ids present. Cross-checked by Council A + AUDIT.
- Per-task data :: `6_Oracle_Events.txt` :: every write action (OE10-OE15) mapped to a 1.1 rubric; the final-response fact list mapped to 2.1 rubrics.
- Per-task data :: `_aux/Hardness_Plan.md` :: 5 engaged levers (L2 / L1+L10 / L31 / L7 / L9) each mapped to a carrier rubric; the QC-status rubric binds recbd087, checks not-advanced-to-Ready + hold recorded, never a nonexistent hold enum.
- Eval spec :: Evals_starpm Rubrics eval + `Docs_starpm/2_Rubrics_V3_Guidelines.md` :: sub-dims (Atomicity, Self-Containment, Completeness, Flexibility, Accuracy, Category Balance, Agent-Centric Phrasing) scored 5/5 by Council B and re-scored 5/5 by AUDIT under the strictest interpretation.
- QC spec :: `Docs_starpm/7_QC_Spec_Doc1.json` (Rubric dimension) :: Rubric Category Balance binary PASS (19 outcome > 0 process); Overall Rubric Quality 0 Major / 0 Moderate / 0 counting Minor.

## Reference docs consulted
- `Reference/Rubric_Format.md` :: flat 4-field schema, agent-centric, atomic, self-contained, single-target uniqueness, split 3+ item enumerations, sub-cats 1.1/1.2/2.1, absolute-count dilution gates re-checked.
- `Reference/Strict_Convention_Inventory.json` + `QC_Tasks/V4_Tasks/QC_Passed/Task1..Task4/7_Rubrics.json` :: V4 phrasing / structure voice (method-agnostic notify, valid negative outcome, same-fact-in-2-artifacts with cross-ref, exact amounts as strict requirements).
- `Docs_starpm/9_Common_Error.md` (Part 3) :: no single-channel forcing, reverse-coverage, no "approximately" on fixed values, all-6-fail removal default.

## Verification statements
- [x] validate.py --phase rubrics exit 0 - PASS (0 fails, 8 benign warns = amount verify-nudges + X2 observation-period on the exact-amount rubrics, all grounded per Council A; 5 notes).
- [x] Schema flat 4-field {title, category, justification, evidence}; every title agent-centric; no tool names in titles; no "at least N"; no em/en-dash (grep clean).
- [x] Outcome (19) > Process (0). check_ordering_coverage.py = OK (no ordering language -> 0 process correct).
- [x] check_qc_binary.py - Rubric Category Balance PASS. (Lone FAIL = Prompt/Coherence, a prompt-phase heuristic false-positive on the S1-locked action sentence; confirmed a FP by Council B + AUDIT via the spec's sentence-removal bolt-on test; not a rubric defect; no PROPAGATE.)
- [x] check_rubric_antipatterns.py = OK (mandatory AUDIT pre-verdict gate); regression anchors 62/62.
- [x] Council A (grounding) GO - every concrete value in all 19 rubrics grounded verbatim / documented numeric equivalent; no S2 -> S3 drift.
- [x] Council B (adversarial QC) GO - 0 Major / 0 Moderate; sub-dims 5/5 post-fix; alt-path / reverse-coverage / atomicity / process all clean; B3 density THIN per-model (pre-accepted); B4 all 5 levers carried.
- [x] AUDIT verdict = PASS (STRICT) - strictest interpretation; 0 Major / 0 Moderate / 0 counting Minor.
- [x] Every OE write action (OE10-15) has a 1.1 rubric; content beyond 1.1 -> 1.2; every prompt tell-me cue -> 2.1. Coverage matrix confirms no gaps, no surplus.
- [x] Each outstanding fact graded in exactly 2 artifacts (Linear ticket + final response); the HOLD decision graded on 5 prompt-named surfaces. No dilution (each fails independently).

## Discrepancies surfaced
- Council B flagged 2 Minors (R12 clause-stack; email "with the specifics" under-covered). BOTH FIXED before AUDIT: R12 made atomic (email held-only, the listing-until-closed condition carried by R14 in the final response); added R12b (email identifies the two unpaid carrying-scope bills, the exact claim Carlos made in Slack that the email must correct). AUDIT confirmed both resolved and the restructure an improvement over the 18-rubric version.
- R12b / R7 / R17 are 2-item couplings. Adjudicated bundling-exception-eligible (below the 3+ enumeration threshold; check_rubric_antipatterns clean; ground truth requires both facets, so no valid-path false-fail). Logged by AUDIT as non-counting MINOR observations; optional split is polish only, not required for GO.
- check_qc_binary Prompt/Coherence FAIL: heuristic false-positive on the S1-locked prompt action sentence (24% shared vocab, 1% under the 0.25 bolt-on threshold). Confirmed a FP by Council B + AUDIT via the spec's sentence-removal test; S1 AUDIT scored Coherence PASS (STRICT). Not a rubric defect; prompt not re-opened; no PROPAGATE.
- X2 rubric-OE consistency WARNs (amounts 387.00 / 1340.00 "no OE amount reference"): benign WARN-only observation-period heuristic false-negative; OE6 does reference both amounts (TotalAmt / Balance 387.00 and 1340.00).
- Density THIN per-model (competent Opus ~43-45, Gemini ~41-43; empirical StarPM 33-38): pre-accepted at S1 AUDIT with per-task justification + a standing hard S4 REDO gate (per-model avg < 40 on real runs -> PIPELINE REDO). Clears the StarPM 15 QC-spec floor with wide margin. Density is a trajectory-time property, not a rubric defect.
- Upstream hygiene: normalized Verification_s2.md section headers to the canonical check_verification.py shape at S3 entry (Sources consulted + Verdict). S2 substance unchanged; every S2 gate artifact present on disk. This was the stale-runbook-template quirk flagged in Verification_s1.md.

## Verdict
- PASS - `7_Rubrics.json` (19 Outcome, 0 Process) clears every S3 exit criterion: validator PASS, Council A GO, Council B GO (all sub-dims 5/5, 0 Major / 0 Moderate), AUDIT PASS (STRICT), Rubric Category Balance binary PASS, ordering-coverage clean, all 5 Hardness levers carried by an Outcome whose value depends on traversing the lever, coverage matrix complete (no gaps / no surplus). Density THIN pre-accepted with the standing S4 REDO gate. Ready for PIPELINE FINAL (cross-artifact holistic council) before platform upload.
