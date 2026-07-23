# TODOs — PIPELINE FINAL (Task 40, StarPM V4)

- [x] Read FINAL runbook + AGENTS.md bootstrap
- [x] Confirm universe = starpm and required inputs present (5/6/7 + Hardness_Plan + Fact_Ledger)
- [x] Run `Validators/phase_ready.py --phase final` (initial run; Verification_s3.md header renamed)
- [x] Re-run phase_ready.py after Verification_s3.md fix -> expected [OK]
- [x] Run `Validators/validate.py --phase all` -> already PASS on all 3 (0/0/0 fails; WARNs on $1,850 known-false-positive per Verification_s3.md)
- [x] Spawn Final Council (oracle sub-agent, 6 lenses); saved to `_aux/Council_Reports/FINAL_council.md` (419 lines, VERDICT: PASS)
- [x] Read verdict: PASS on all 6 lenses; 0 BLOCKER / 0 MAJOR / 0 MINOR new; 1 HARD FLAG inherited (density THIN)
- [x] Wrote `_aux/Verification_final.md` per v16 cross-source template
- [x] Appended predicted-only entry to `Tasks/_meta/Hardness_Patterns_Log.md` (levers L1/L2/L5/L7/L8/L9; actuals pending S4)
- [x] STOP gate — StarPM V4 next trigger is `PIPELINE SUBMISSION_GATE — Tasks/40_6a61a86a31b9c973b2021ba5` (not S4 — S4 comes after platform runs return)

## RE-RUN v2 (2026-07-23, rubric count 16 → 28 after prior FINAL)

- [x] Detect stale prior FINAL via mtime check (rubrics 19:30:57 > prior FINAL 18:59:27)
- [x] Re-run `phase_ready.py --phase final` → OK (hash-drift WARN on Evals hashes, non-blocking)
- [x] Re-run `validate.py --phase all` → PASS/PASS/PASS (0/0/0 fails; $1,850 WARNs are known-false-positives per Verification_s3.md)
- [x] Spawn fresh Final Council (oracle sub-agent, 6 lenses on 28 rubrics); saved to `_aux/Council_Reports/FINAL_council.md` (501 lines, OVERWROTE stale v1)
- [x] Read v2 verdict: **PASS**. 0 BLOCKER · 0 MAJOR · 1 MINOR observation (rubric-7 bundling asymmetry — V3-permitted, non-defect). THIN density HARD FLAG inherited (write-count unchanged by rubric expansion).
- [x] Hardness_Patterns_Log.md — no update (same 6 levers L1/L2/L5/L7/L8/L9 preserved end-to-end; v2 rubric expansion strengthens enforcement of same lever set)
- [x] STOP gate — next trigger unchanged: `PIPELINE SUBMISSION_GATE — Tasks/40_6a61a86a31b9c973b2021ba5`
