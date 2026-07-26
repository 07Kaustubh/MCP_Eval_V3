# Verification: PIPELINE S4 · Task 44 (`44_6a62ccba8cad60844b8364b9`) · pass 4

**Universe:** starpm (V4, Star Property Management, LLC) · **Universe today:** 2026-07-01 (America/Chicago)
**Models:** Opus 4.8 (6 runs) + Gemini (6 runs), both complete · **Date:** 2026-07-26

## Sources consulted

- **`7_Rubrics.json`** :: the 60-criterion set being classified. Diffed field-by-field against `_aux/7_Rubrics.pre_audit_fixes.json`: **13 criteria changed at 14:42** (8 titles, 11 evidence fields, 3 justifications), every edit widening an accept-set rather than narrowing one. Set size unchanged at 60, inside the 60-criterion cap. This is a second input delta beyond the regrade, and it is why pass 3's walks could not simply be carried forward for those 13.
- **`8a_Verifier_Fails_Opus.txt` (16:18) + `8b_Verifier_Fails_Gemini.txt` (16:19)** :: verifier output. Parsed to a 60 x 12 decision grid; **all 60 titles matched exactly in all 12 run blocks, 720 of 720 decisions matched, 0 unmatched rows, 0 duplicate titles**. Both files therefore grade the current set, including the 8 retitled criteria.
- **`Agent_Responses/{Opus,Gemini}/Run1-6`** :: all 12 trajectories walked. Confirmed **unchanged since 10:50**: `parse_trajectories.py` reproduces identical per-run tool-call counts to the unit (Opus 74/56/79/52/57/57, Gemini 79/72/86/91/60/91). Write payloads (`save_issue`, `save_comment`, `create_records_for_table`, `create_draft`, `slack_send_message`, `create_event`) and final-response text extracted per run. Both trajectory layouts handled: the Opus stream-json shape and the Gemini `tool_use`/`tool_result` shape with the final response reconstructed from trailing delta messages.
- **Linear identifier resolution** :: a uuid-to-identifier map was built from the tool results across all 12 runs (**257 uuids resolved**) because several runs address comment targets by internal record id rather than by issue identifier. This settled the OPS-87 contested cell on Opus run 4, where `1d96db3b-56d6-4530-b2e6-afc6df6354c3` resolves to OPS-87 and the judge read it as OPS-99.
- **Per-task data** :: `_aux/Universe_Split/` ground truth re-confirmed for every classification. Linear states resolved by id, not by prose: OPS-87 Todo, OPS-96 Todo, OPS-98 In Progress, OPS-97 Todo, OPS-99 In Progress, OPS-108 Backlog, OPS-186 Todo, OPS-56 In Progress, OPS-43 In Progress, OPS-40 Done, OPS-91 Done, OPS-35 In Progress. Slack ts values resolved to exact text and author.
- **`_aux/Fact_Ledger.json`** :: atom cross-reference for every value cited in a justification.
- **`_aux/Hardness_Plan.md`** :: four pre-registered predictions re-scored against the new grading, including the pre-registered lever re-attribution rule.
- **`5_Prompt.txt`** :: re-read in full for checklist question 3 (is the criterion required by the prompt).
- **Eval spec** :: `Evals_starpm/4_Verifier_Fails_Eval.md` bucket taxonomy, applied once per model.
- **QC spec** :: `Docs_starpm/1` density bar (40+ average per model), fail floor 15, pass@1 <= 40%, error runs <= 2.

## Eval spec verified

- `Evals_starpm/4_Verifier_Fails_Eval.md` :: bucket taxonomy (Rubric Invalid / Judge Error / Legit Fail) re-applied from scratch against the new grading and the new rubric text, once per model per the "run this eval once per model" mandate.
- 5-point pre-write checklist applied before every one of the 34 justifications.

## QC spec sub-dims verified

- **All-Failing Rubrics sub-dim** :: Bucket 1 ratio computed on four bases. Post-fix: 3 of 50 failing criteria (**6.0%**), 0 of 34 either-model all-failing, 0 of 6 both-model all-failing, 3 of 404 fail cells (0.7%). All inside the 25% band, score **5/5**.
- **Trajectory T1 (density)** :: Opus 62.5 avg total / 44.7 MCP; Gemini 79.8 / 67.0. V4 target 40+ per model. **PASS both.**
- **Trajectory T2 (pass@1 <= 40%)** :: 0/6 on both models, **0.0%**. **PASS both.**
- **Trajectory T3 (<= 2 error runs)** :: 0/6 errored on both models. **PASS both.**

## Verification statements

- [x] Trajectory walk recorded for EVERY failing criterion, not just contested ones. 50 failing criteria across both models. The 13 criteria whose text changed at 14:42 were re-walked from scratch against the new text, and every cell whose decision moved between the two gradings (74 cells) was re-walked against the artifact.
- [x] T2 + T3 hard gates evaluated and recorded in `_aux/Council_Reports/S4_verdict.md`.
- [x] T1 density gate evaluated per model against the V4 40+ target.
- [x] Bucket 1 ratio computed; All-Failing Rubrics sub-dim scored 5/5. The 3 Bucket 1 defects were fixed in place and every fix re-graded against all 12 trajectories before shipping.
- [x] 5-point checklist confirmed YES on all 5 before each of the 34 justifications (detail in the AF file).
- [x] `check_justification.py` exit 0 on the AF batch.
- [x] 0 em-dashes across all four S4 reports, the verification doc, the TODO list, `7_Rubrics.json` and `6_Oracle_Events.txt` (verified by grep).
- [x] Every bucket entry carries a trajectory citation naming the run, the call and the parameter values, or records that the action was not attempted.
- [x] Comment targets given as internal record ids resolved to issue identifiers before any bucket call was made.

## Verdict

**S4 pass 4 COMPLETE, fixes applied.** All three trajectory hard gates PASS on both models. Three Bucket 1
defects were identified and fixed in place, holding `7_Rubrics.json` at 60 criteria, 60 outcome / 0 process.
All-Failing Rubrics sub-dim **5/5** (Bucket 1 ratio 6.0% of failing criteria, inside the 25% band). AF union
falls from 35 to 34 with the false all-fail removed. AF batch clean on the voice gate. No REDO.

## Fixes applied and re-verified

| Fix | Criterion | Defect | Re-verified against all 12 trajectories |
|---|---|---|---|
| B1-1 | South electrical finished | Overly Specific: attribution demand the evidence disclaimed, 5 cells | 8 fail cells to 3; the 3 remaining fails (Opus 2, 3, 5) confirmed substantively correct |
| B1-2 | East service recorded complete | Overly Specific: same via "by the crew", 3 cells | 8 fail cells to 5; leaves the all-failing set; the 5 remaining fails confirmed correct |
| B1-3 | West coverage item owner | Overly Broad: unbound from the coverage item, passed 6/6 Gemini vs 2/6 on its sibling | Opus unchanged at `FF.FF.`; Gemini corrects to 2/6, matching its sibling exactly |
| Hardening | West coverage in channel post | OPS-96 portfolio-scope exposure, unrealized | No decision change on any of the 12 cells |
| OE mirror | OE 29 | Still named "OPS-186 dated 2026-06-17" after criterion 5 was generalised at 14:42 | OE and rubric now agree; owner-binding rule added to the decompose directive |

**Regression check on the widenings.** Every fail cell on the four edited criteria was re-graded by hand under
the new text. Two widenings (B1-1, B1-2) flip only cells whose artifact text satisfies the criterion, and no
legitimate fail is flipped. One tightening (B1-3) makes four Gemini cells fail that were passing for the wrong
reason. An earlier draft of B1-2 used an exhaustive `FAIL only if` list that would have let a run carrying East
as merely unconfirmed pass without reporting completion; that was caught in re-grading and corrected before the
edit shipped.

**Validator after the edits:** PASS on prompt (0F/1W), oe (0F/0W), rubrics (0F/0W), all, submission_gate
(0F/2W) and injection (0F/0W). Snapshots at `_aux/7_Rubrics.pre_qc5_fixes.json` and
`_aux/6_Oracle_Events.pre_qc5_fixes.txt`.

## Discrepancies surfaced

1. **Grader non-determinism reproduces, with the net direction reversed (material).** 74 of 720 decision cells (10.3%) changed between the pass-3 and pass-4 gradings. Only 12 fall on the 13 criteria whose text was edited; **62 (8.6% of all cells) are decision changes on unchanged text**. Pass 3 measured 8.5% on the same basis but skewed 42 Fail-to-Pass against 25 Pass-to-Fail, whereas pass 4 skews 46 Pass-to-Fail against 28 Fail-to-Pass. Two independent regradings now agree that roughly one cell in twelve is not reproducible, and that the direction of the noise is itself not stable. Recorded in `S4_verdict.md` and in `Tasks/_meta/Learnings.md`.

2. **A judge decision rests on an unresolved internal record id.** `Opus run 4 / OPS-87 note`: the judge asserted no comment was written on OPS-87, listed six comment targets for the run's six comment calls, and mis-resolved the OPS-87 uuid as OPS-99. The run wrote no comment on OPS-99 at all. The criterion's evidence explicitly accepts the internal id form. This is the strongest single appeal in the set because it is a resolution error rather than a judgment call, and it also produced a false accusation that the run's final response misreports its own actions.

3. **Seven cells were failed for an attribution requirement that the criteria explicitly disclaim.** The recorded-South-electrical and recorded-East-service criteria both carry evidence text saying the record identifier is not required, and the East criterion states a single FAIL condition that none of the contested cells meets. The grader nonetheless required attribution to a named record on four and three cells respectively. Filed as judge errors, with a watch item in `S4_fixes.md` proposing that the disclaimer be lifted into the title if the misreading recurs.

4. **Two judge justifications are internally contradictory.** `Gemini run 4 / recorded South electrical` reads "This is borderline, but the agent does report electrica[l]" and returns Fail. `Gemini run 2 / West QC walk` quotes the passing text, writes "This does partially mention a QC walk", and returns Fail. Both are filed.

5. **Three judge justifications reason from the run's own summary rather than the sent artifact.** `Gemini run 6 / end-of-June target` and `Gemini run 4 / plumbing open` both say the response summary does not show the framing, when the posted channel payload carries it verbatim. This is a distinct failure mode from over-strict reading and is worth flagging to the platform separately.

6. **The 14:42 accept-set widening is measurable and favourable.** The note-on-OPS-98 criterion moved from 0/6 to 4/6 on Opus once any correct reason was accepted, and three filter run criteria each gained a first Opus pass once a comment on an existing open record was accepted. Two widened criteria moved slightly against the agent, both inside the documented variance and neither attributable to the edit, since the edits only added acceptable locations.

7. **No universe or artifact discrepancy.** Every fact asserted in a justification was re-confirmed against the per-task split. No entity, date or identifier drift found.
