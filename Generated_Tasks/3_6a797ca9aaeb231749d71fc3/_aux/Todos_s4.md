# S4 TODO — 3_6a797ca9aaeb231749d71fc3

Pass 2 (2026-08-12, after operator applied 10-of-12 pass-1 fixes + re-uploaded + pasted new export at 17:02).

## Pass 1 (superseded, describes stale bytes per rule 15)

Archived. See `_aux/7_Rubrics_pre_s4fix_20260812_154519.json` for the 30-criterion pre-fix rubric set and `_aux/Verifier_Exports/8_Verifier_Fails.4440f979d6f5.txt` for the pass-1 export.

## Pass 2 (current, describes export sha `07f7235...` against 28-criterion rubrics)

- [x] Read root AGENTS.md and verify HarmonyGames S4 routing (rules 1, 2, 15, 16, 17, 21).
- [x] Inventory task directory: confirm all S4 inputs present + prior-pass artifacts.
- [x] Run `phase_ready.py --phase s4` — fixed upstream Verification_final.md formatting; gate now PASS.
- [x] Run `parse_trajectories.py` — 6/6 ok, avg 72 total / 57.8 MCP tool calls. T1 PASS.
- [x] Run `check_export_freshness.py --pin` — new pin recorded against pass-2 bytes.
- [x] Run `check_criterion_dependencies.py` — 11 dependent pairs inferred, 0 violations.
- [x] Run `check_oe_rubric_sync.py` — 30 OEs / 28 criteria, every decompose element carries.
- [x] T3 error-rate gate: 0/6 errored. PASS.
- [x] T2 agent-failure-rate gate: 0/6 runs passed all criteria. pass@1 = 0.0%. PASS.
- [x] Build rubric x run matrix by hand from the pinned export. 8 AF criteria identified.
- [x] Audit passing cells for dependency inconsistency (rule 17). One advisory observation on R2 Run 4 / R6 Run 4; addressed via R1 accept-set broadening.
- [x] Trajectory walk per failing rubric. 5-point pre-write checklist applied per candidate.
- [x] Classify 8 AF criteria: 2 Bucket 1 (R1, R3), 0 Bucket 2, 6 Bucket 3 (R4, R5, R10, R17, R18, R26).
- [x] Compute All-Failing Rubrics sub-dim ratio: 2/8 = 25.0% → 3/5 NON-FAIL. Fix projection: 5/5 PASS post-edits.
- [x] Confirm classifications against `_aux/Universe_Split/` (PR #16/#36/#37 dates, PR #37 review, ART-770/ART-252/ART-760 statuses, three Marcus mailboxes, PERSON_0396 profile email = None).
- [x] Update hardness calibration in `_aux/Council_Reports/S4_verdict.md` and in `Tasks/_meta/Hardness_Patterns_Log.md` (pass-2 delta entry).
- [x] Write `_aux/Council_Reports/S4_AF_justifications.md` (6 justifications, plain reviewer voice).
- [x] Run `check_justification.py` on AF batch → 0 hits, exit 0.
- [x] Write `_aux/Council_Reports/S4_fixes.md` (R1 accept-set broaden, R3 title normalize).
- [x] Write `_aux/Council_Reports/S4_judge_errors.md` (empty, advisory observation only).
- [x] Write `_aux/Council_Reports/S4_verdict.md` with pass-2 matrix, classifications, sub-dim scoring, hardness calibration.
- [x] Write `_aux/Verification_s4.md` cross-source verification.
- [x] Write `_aux/Reads_s4.md` (E2 compliance).
- [x] Update `Tasks/_meta/Stump_Hypotheses.md` with pass-2 lever confirmations and shape catalog additions.
- [x] Re-run `check_export_freshness.py` (bare, drift check at exit) — PASS, no drift mid-pass.
- [x] Re-run `check_rubric_antipatterns.py` — PASS, 0 anti-patterns.
- [x] Re-run `phase_ready.py --phase s4` — PASS, all upstream artifacts, pin verified.

## STOP gate

Pass 2 exits here. Operator next steps:
1. Apply the two Bucket-1 fixes in `_aux/Council_Reports/S4_fixes.md` to `7_Rubrics.json` (R1 accept-set broaden to include ART-760; R3 title normalize).
2. Ship the six Bucket-3 AF justifications from `_aux/Council_Reports/S4_AF_justifications.md` to the platform.
3. Re-upload rubrics + rerun the platform verifier. Expect pass@1 to stay at 0/6 (the four PR #37 lever criteria alone stump 6/6); expect the All-Failing Rubrics sub-dim to move from 3/5 NON-FAIL to 5/5 PASS.
