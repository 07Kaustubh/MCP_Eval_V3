# REDO reason — Tasks/27_6a39fd19048f9213281ec7b

Decision date: 2026-06-23.

## Verdict

REBUILD. Per the REDO runbook's third trigger: FINAL-class BLOCKER that cannot be patched in 3 REVISE rounds. The underlying scenario is broken at the OE / rubric construction level, not at the surface QC level.

## Trajectory signals (both OK — NOT the failure mode)

Source: `_aux/Trajectory_Stats.json` (6 runs of the candidate's submission)

- pass@1 = 0.00 (0 of 6 cleared all 13 rubrics) — well below the 0.40 difficulty ceiling.
- avg tool calls (total) = 53; (MCP-only) = 43.7 — both above the 40 density floor.
- min/max tool calls (total) = 30 / 69.
- `density_ok_at_40` = true; `difficulty_ok_at_40pct` = true; overall `verdict` = "OK".

Difficulty and density both came in healthy. The candidate's task was hard enough and dense enough. The reason it is being rebuilt is not the trajectory metrics.

## Actual failure mode (structural — surfaced at REVIEW)

Source: `_aux/Candidate_Originals/changes.md` findings #1 through #6 (Major tier, all six re-verified by direct grep against the per-task universe split under `_aux/Universe_Split/`).

1. **Fabricated discriminator (Major).** OE5b names a SAP subledger transaction `brookfield_6000001115` carrying a $28.59 payroll-funding adjustment on account 102000, with no GL counterpart. Direct grep across `sap_subledger.subledger_transactions.json`, `sap_subledger.ap_invoices.json`, and `oracle_gl.ogl_journal_entries.json` returns ZERO hits for the transaction ID and ZERO hits for the dollar amount 28.59. The discriminator record is fabricated.
2. **Inherited fabrication in OE5c and OE10 (Major).** Both inherit the fabricated discriminator. The remediation path the OE chain prescribes ("book the missing $28.59 to GL on 102000") and the final-response shape ("the REAL cause is brookfield_6000001115...") can only be reported by an agent that hallucinates a record that does not exist.
3. **Unearnable rubrics 6 and 7 (Major).** Both are built on the same fabricated record. Trajectory data confirms: 0 of 6 runs cleared all 13 criteria, each missing 2 or 3 rubrics, with the two fabricated rubrics in every failed set.
4. **Invalid JSON escape in rubric 3 (Major).** The rubric 3 title contains the literal substring `\~$42`. JSON does not recognise `\~` as a valid escape; the file fails to parse — paste-back to the platform would reject it before any rubric grading runs.

The combination is unpatchable in REVISE. The discriminator the scenario hinges on is absent from the per-task universe, and pointing rubrics 6 and 7 at a different (real) record would mean redesigning the OE blueprint from OE4 forward. That is a CB-class rebuild, not a fix-in-place edit. REVIEW called REBUILD; the runbook calls REDO.

## What stays

- `3_UniverseDataForThisTask.json` — unchanged (same per-task universe)
- `1_Business_Function.txt` (Bookkeeping) and `2_Persona.txt` (Ben Arinzo, Bookkeeper) — unchanged
- `_aux/Universe_Split/`, `_aux/Universe_Index/`, `_aux/Fact_Ledger.json` — S0 outputs from the REVIEW pass, still valid against the unchanged universe
- `_aux/Trajectory_Stats.json`, `_aux/Linter_Decision.md`, `_aux/Linter_Justifications.md`, `_aux/Validator_Reports/`, `_aux/Council_Reports/` — candidate-rating evidence
- `_aux/Candidate_Originals/` — archived 5 / 6 / 7 / changes.md / 13_Feedback.txt

## What gets rebuilt

- `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` — fresh CB outputs from the HARDNESS → S1 → S2 → S3 → FINAL chain (each in a fresh chat).

The HARDNESS rebuild must pick a discriminator that the per-task universe actually contains. The candidate's gap was working blueprint-first ("the real cause is X, now find where X lives in the data") instead of data-first ("here is a real reconciling item in the data, build the OE around it"). The new HARDNESS pass should sweep the SAP subledger, the GL feed runs, the AP invoices, and the GL journal for real misposted / unrecorded / mistimed items, then build the scenario around one of those.

## Cross-task learning candidate

This is a high-value pattern for `Tasks/_meta/Learnings.md`: a CB built a hard, dense scenario but worked blueprint-first instead of data-first, and the discriminator they invoked at the rubric-discriminator slot did not exist in the data. The lesson: HARDNESS must verify every record cited in the discriminator slot with a direct grep against `_aux/Universe_Split/` before S1 starts.
