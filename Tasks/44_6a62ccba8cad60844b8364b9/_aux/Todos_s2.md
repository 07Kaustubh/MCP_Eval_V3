# S2 Todos — Oracle Events

Task: `Tasks/44_6a62ccba8cad60844b8364b9` · Universe: `starpm` (V4) · Date anchor: 2026-07-01 America/Chicago

- [x] T0. Create this TODO file (v11 E1 gate). — completed
- [x] T0b. Create `_aux/Reads_s2.md` and log every spec / reference / eval doc read (v11 E2 gate). — completed, corrected after Council round 1
- [x] T1. Run `phase_ready.py --phase s2`. — OK, 1/1 upstream artifact present
- [x] T2. Read upstream artifacts: `5_Prompt.txt`, `_aux/Hardness_Plan.md`, `_aux/Verification_s1.md`, `_aux/Council_Reports/S1_A_grounding.md`, `S1_B_adversarial.md`, `AUDIT_prompt.md`, `_aux/Reasoning/prompt_design.md`. — completed; 10 downstream-binding constraints extracted
- [x] T3. Read format + spec surfaces: `Reference/OE_Format.md`, `Evals_starpm/2_OE_Eval.md`, `Docs_starpm/7_QC_Spec_Doc1.json` (OE dimension), `Docs_starpm/1_Project_Instructions_Overall.md` Step 3.5, `Docs_starpm/2_Rubrics_V3_Guidelines.md`. — completed
- [x] T4. Read `StarPM_Base_Universe/7_Server_Tools_Details.json`; recorded exact names + signatures for airtable, contacts, gcalendar, gmail, linear, slack. Confirmed `save_issue.assignee` has type `null` and cannot carry a value. — completed
- [x] T5. Read V4 reference OE corpus (QC_Passed Task1 22 OEs, Task2 28 OEs) for voice / structure. — completed
- [x] T6. Decompose `5_Prompt.txt` into explicit + implicit asks; map to discovery steps and write actions. — completed, 11 write actions identified
- [x] T7. Ground every step against `_aux/Universe_Split/` — every issue id, state, assignee, project, Slack ts, thread parentage, date, email, base/table/field id, calendar event verified first-hand. — completed
- [x] T8. Single-target uniqueness (rule 13 / F7), atomicity (F8), future-event sweep (F9). — completed. All 11 writes unique by construction; F9 clean across 565 calendar rows; Jaime has zero events on or after 2026-07-01
- [x] T9. Draft `6_Oracle_Events.txt`. — completed, 38 OEs
- [x] T10. `validate.py --phase oe` — **PASS, 0 fails, 0 warns, 3 notes**
- [x] T11. `verify_universe_atoms.py` — 33 atoms, 0 FAIL, 1 WARN (2026-07-15 outside active window; that is the real Mesa Vista 4C future event, intentional and adjudicated)
- [x] T12. Council A (grounding) round 1 — NO-GO (0 BLOCKER, 5 MAJOR, 5 MODERATE, 4 MINOR, 4 NOTE)
- [x] T13. Council B (adversarial QC) round 1 — NO-GO (2 BLOCKER, 4 MAJOR, 3 MODERATE, 4 MINOR, 3 NOTE); OE Completeness 4/5, OE Accuracy 4/5
- [x] T14a. Verify every council finding against source before acting. — completed; 2 findings adjudicated partly against the councils with reasons returned to them
- [x] T14b. Apply round-1 fixes. — 13 defects fixed; OE list 36 -> 38 steps
- [x] T14c. Council A round 2 — **GO** (0 BLOCKER, 0 MAJOR, 0 MODERATE, 5 MINOR, 6 NOTE); all 5 round-1 MAJORs and all 5 MODERATEs verified closed
- [x] T14d. Apply Council A round-2 minors and notes (9 edits). Validator re-run clean.
- [x] T14e. Council B round 2 — **GO**, both QC sub-dims 5/5
- [x] T15. Write `_aux/Verification_s2.md` (Step 0.5 cross-source verification, MANDATORY before exit).
- [x] T16. Fire AUDIT (`--phase oe`). **Auto-fire is MANDATORY here** — step-8 conditions (b) atom-verifier edge-case flag, (d) OE revised this pass, and (e) no rubrics exist yet, all hold. Resolve REVISE within the 3-round cap.
- [x] T17. Append final report to `_aux/Reasoning/OE_solvability.md` (coverage map + rubric preview + AUDIT verdict).
- [x] T18. Append one line to `Tasks/_meta/Audit_Log.md`.
- [x] T14f. Councils round 3 (post-AUDIT edits) — A NO-GO 3 MAJOR, B NO-GO 1 MAJOR; all applied.
- [x] T16b. AUDIT round 2 — REVISE, 1 MAJOR (OE 30 unbounded absence); applied.
- [x] T16c. AUDIT round 3 — **PASS (STRICT)**.
- [ ] T19. STOP. Report to operator; do not start S3.

## Gates already green

- `validate.py --phase oe` :: PASS 0/0/3
- `verify_universe_atoms.py` :: 34 atoms, 0 FAIL / 1 adjudicated WARN
- `test_regression_anchors.py` :: **62/62 PASS**
- Structural :: 38 sequential steps, zero em/en dashes, pure ASCII, all internal cross-references resolve, every step names a real tool

## Infra fix applied this phase

`_aux/Fact_Ledger.json` `lifecycle.today` backfilled from `null` to `"2026-07-01"` per AUDIT finding A-11, which required the fix to land before S2. The companion code change (`validate.py:464` should read the universe registry instead of a hardcoded Brookfield `2026-06-12`) is shared-code and remains open for the operator.
