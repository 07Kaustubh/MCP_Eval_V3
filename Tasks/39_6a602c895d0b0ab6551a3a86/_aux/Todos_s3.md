# Todos — S3 (REDO — 2026-07-23)

Atomic todos for Phase S3 (Rubrics) per Reference/Sessions/S3.md.
Pre-REDO S3 artifacts (Council Reports + Verification + Coverage Matrix) archived to
_aux/Candidate_Originals/S3_pre_redo_2026-07-22/. This todo list is the fresh REDO run.

- [x] T1. Run phase_ready.py --phase s3 (v11 E1 gate).
- [x] T2. Overwrite _aux/Todos_s3.md (this file) for the REDO cycle.
- [x] T3. Overwrite _aux/Reads_s3.md and log every reference doc read this REDO cycle.
- [x] T4. Read Reference/Rubric_Format.md end to end (v4 severity taxonomy re-confirmed).
- [x] T5. Read Reference/Strict_Convention_Inventory.json for allowed phrasings.
- [x] T6. Read Reference/Sessions/S3.md runbook end to end.
- [x] T7. Read _aux/Hardness_Plan.md (S1.5 REVISION UPDATE section — L6 removed, soft-lever amplifiers active).
- [x] T8. Read _aux/Fact_Ledger.json for persona / email / date / channel atoms.
- [x] T9. Read _aux/Verification_s2.md — PROPAGATE TO S3 flags (guardrails, atomicity, thread-lock-in).
- [x] T10. Re-read 5_Prompt.txt (R5 REDO — Jul 23 01:41) + 6_Oracle_Events.txt (REDO — Jul 23 02:36).
- [x] T11. Universe grep confirms every rubric atom present in _aux/Universe_Split/ (rec291f423370e2a2db + OPS-224/225/226 + state_OPS_4 + 1781788320.000202 + UADB2B4E045 + b8e4d0a3f2c5b9e7 + d0e6f2c5b4a70b19 + C004 all found).
- [x] T12. Drafted 7_Rubrics.json — 26 outcome, 0 process, flat schema {title, category, justification, evidence}.
- [x] T13. Three-condition Process test applied; zero Process rubrics (Bennett-verify + Airtable-pre-read both covered by Outcome content rubrics R2/R5/R8/R13 already).
- [x] T14. S2 propagation flags applied — (a) `(or similar)` on 8 content-bearing 1.2 rubrics (R2/R5/R8/R14/R15/R16/R19/R23/R26); (b) Sandra Slack tag `<@UADB2B4E045>` exact match (structured field); (c) NO cc-recipient split (R17 covers to+cc in one 1.1 per V4 atomicity); (d) Friday-morning treated as 07:00-10:00 CT window (R25); (e) multi-atomic Airtable 1.2s (R11+R12+R13+R14+R15+R16) NOT bundled per V4 atomicity; multi-atomic Slack 1.2s (R21+R22+R23) NOT bundled.
- [x] T15. Validate.py --phase rubrics — PASS clean (post-differentiation fix to clear Jaccard 80% WARN on R3/R6/R9 + swap R17 to "email" verb).
- [x] T16. Council A spawned (ultrabrain, background) — VERDICT: GO. Report at _aux/Council_Reports/S3_A_grounding.md.
- [x] T17. Council B spawned (ultrabrain, background) — VERDICT: NO-GO (2 Moderate on R18/R21 + 2 Minor on R11/R25). Report at _aux/Council_Reports/S3_B_adversarial.md.
- [x] T18. Fixes deferred to AUDIT arbitration since Council B was ambivalent (both PROPAGATE-TO-S1 and loosening would kill L26).
- [x] T19. AUDIT spawned (ultrabrain, background) — Round 1 VERDICT: REVISE + Option A on R18/R21. Report at _aux/Council_Reports/AUDIT_rubrics.md.
- [x] T20. Round-1 AUDIT REVISE fixes applied in-place: R11 attribution widening + R25 window widening 07:00-10:00 → 07:00-11:00 CT. Post-fix validator FAIL (forbidden "such as J" in R11 title) resolved by reverting to canonical `(or similar)` V3 pattern; final validator PASS clean. Round-2 AUDIT spawned — VERDICT: **PASS (STRICT)** 5/5 Overall Rubric Quality. R18/R21 upgraded to non-failing structured-field exact-match. Council A + B round-2 re-runs skipped (guardrail-widening non-destructive fixes; AUDIT Lens R2 delta-impact scan independently verified zero new defects).
- [x] T21. Wrote _aux/Reasoning/Rubric_Coverage_Matrix.md with AUDIT PASS (STRICT) header + forward+reverse coverage maps + hardness lever operationalization table.
- [x] T22. Wrote _aux/Verification_s3.md with cross-source check per S3 runbook step 0.5.
- [x] T23. STOP gate — S3 exits clean. Ready for PIPELINE FINAL in a fresh chat.
