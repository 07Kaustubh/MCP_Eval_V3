# Verification — PIPELINE S4 (2_6a6beba55996ad2ada369b15)

Pass 1, 2026-08-07. Universe **harmonygames**, single-model (Claude Opus 4.7).

## Data sources consulted
- `7_Rubrics.json` :: the 28-criterion set being classified, pinned at `69713012b52f17d6…` 11,941 B.
- `8_Verifier_Fails.txt` :: verifier output, pinned at `d28c7c4ac71a9abd…` 53,558 B, per-run [16, 20, 22, 18, 16, 17]. Arrived as `8_Verifier_fails.txt` and was renamed before it was read.
- `trajectory-runs/trajectory-run-{1..6}.json` :: all six walked. Arrived as `trajectory-run-N (2).json` and were renamed before they were read.
- `HarmonyGames_Base_Universe/Services_Data/` :: ground truth, per hard rule 2. `4_Changelog.json` is `[]` and `9_Universe_inject.sql` touches no marketing, engagement or finance table, so the base export is the graded universe for every figure re-derived here.
- `_aux/Hardness_Plan.md` :: stump hypotheses and risk register, compared against what actually failed.
- `_aux/Trajectory_Stats.json` :: measured density and pass@1, written by the parser rather than read off by hand.

`_aux/Fact_Ledger.json` was deliberately **not** used as the atom source for this pass. HarmonyGames ledgers do not index the warehouse row values these criteria turn on, so every figure was re-derived directly from `snowflake.tables.json`.

## Eval spec verified
- `Evals_harmonygames/4_Verifier_Fails_Eval.md` :: five-verdict taxonomy for this universe re-applied. The **Tool Precision Mismatch** hard gate (lines 250-266) was run for every failed criterion containing an amount, as that section requires, and it is what classifies criteria 4, 6, 17 and 20. Its mixed-finding clause (line 265) is what preserves the scope miss on runs 1-4 as a genuine task miss.
- Phase 3.3 cross-run comparison applied to criterion 10.
- `AGENTS.md` rule 21 and `Docs_harmonygames/9_Common_Error.md:29` :: removal argued first for every all-failing criterion. Five-point pre-write checklist reached question 5 ("could a capable agent realistically pass this") and answered NO for criteria 4, 6, 17 and 20, so no AF justification was written for any of them.

## QC spec sub-dims verified
- All-Failing Rubrics sub-dim: Bucket 1 ratio 6/14 = 42.9% -> **3/5 NON-FAIL**. All-failing-only view 4/4 = 100% recorded alongside it.
- Trajectory T1 (tool-call floor): avg 61.5 total / 49.3 MCP -> **PASS** against 40+ and against the 15 floor.
- Trajectory T2 (pass@1 <= 40%): raw 0.0%, corrected 16.7% excluding Rubric-Invalid criteria -> **PASS** on both.
- Trajectory T3 (<= 2 error runs): 0/6 -> **PASS**.

## Verification statements
- [x] Trajectory walk recorded for EVERY failing rubric across all six runs, not just the judge-error candidates. All 14 failing criteria carry a `Run X, tool call Y` citation or an explicit absence-of-action finding.
- [x] T2 and T3 hard gates evaluated and recorded in `S4_verdict.md`.
- [x] Bucket 1 ratio computed; All-Failing Rubrics sub-dim scored, with the sharper all-failing-only reading stated rather than buried.
- [x] Five-point checklist applied before every candidate AF justification. Four criteria answered NO on question 5 and were reclassified to Rubric Invalid.
- [x] `check_justification.py` exit 0 on the AF batch file.
- [x] Passing cells audited (step 1b), by checker and by hand. One structurally wrong PASS found that the checker cannot see.
- [x] Every Bucket 1 and Bucket 3 classification re-confirmed against the universe source of truth, not against the judge's justification text.

## Cross-source re-derivations (procedure step 3)

| Claim | Universe value | What the tool served | Where confirmed |
|---|---|---|---|
| combo_fighter spend, 2026-01-05 to 2026-02-28 | 7,483.42 (330 rows) | `"7476"` | Run 1 call 52, Run 5 call 45, Run 6 call 41 |
| combo_fighter spend through 2026-02-09 | 5,039.34 | `"5035"` | Run 6 call 129 |
| all titles, 2026-02-10 to 2026-02-28 | 8,452.64 (280 rows, 19 days) | `"8447"` | Run 5 call 134, Run 6 call 53 |
| combo_fighter share of that window | 2,444.08 | `"2441"` | Run 5 call 134, Run 6 call 45 |
| peak combined DAU | 801 on 2026-02-07 | `"801"` | Run 3 call 125, Run 6 call 81 |
| `avg_session_minutes` column average | 12.674 exact / 12.736 integer-rounded | `12.74` | Run 6 call 39 (the control that proves the storage path) |
| February `legal` burn line | 13,000 | `"13000"` | queried by every run |
| Sunset managed wind-down quote | ~15,000, `C07C2866011` ts `1770850852.708789` | never returned | absent from all six trajectories |
| wind-down meeting notes range | 13,000 to 15,000, Gmail `Notes: "Harmony Games Wind Down" Feb 11, 2026` | never returned | absent from all six trajectories |
| ad-account ownership grounding | `C07C2866011` 2026-01 messages | never returned | absent from all six trajectories |

The last three rows were each checked for existence in the base universe before any zero-of-six claim was made. All three exist and all three are inside the persona's read scope, so the non-retrieval is agent behaviour rather than a missing record.

## Second pass — falsification checks run against my own findings

Each finding was attacked before it was written up.

1. **Could the rounding be at serialization instead of storage?** Falsified. Serialization-rounding predicts `SUM(spend_usd)` returns 7483; the tool returns 7476, the sum of rounded rows. Twelve aggregates predicted from the storage model before comparison, twelve matched. Zero decimals returned from any stored column across all six runs.
2. **Is there another reachable path to the exact figures?** No. `SINGULAR_INSTALLS_RAW` and `UA_SPEND_UNIFIED_V2` carry zero combo_fighter rows. No business record on any service states either figure. A text search does hit `7483.42` and `8452.64` in Slack and Gmail, but every hit is a substring of an unrelated 2023-2025 message timestamp (`"ts": "1715188452.640269"`). Recorded so the grep is not misread later.
3. **Is #executives ACL-blocked, which would make criterion 10 unfailable rather than hard?** No. Run 5 call 5 returned the channel in `slack_channels_list`, and searches returned message bodies from it (Run 3 call 114, Run 5 call 19). Only February 2026 messages were never surfaced, on any run, and no run called `slack_conversations_history` on it. The Gmail grounding is in `robert@harmonygames.co/1856871678357556733`, the persona's own mailbox. The Persona ACL hard gate does not fire.
4. **Is criterion 10's collision really the PASS being wrong rather than three judge errors?** Confirmed. All six runs queried `MONTHLY_BURN` and all six received `legal = 13000`; run 2's own sources list cites that table. The value was in front of every agent.
5. **Are criteria 12, 16 and 24 a grader coin-flip?** No. Runs 2, 3 and 4 each assert an unconditional negative ("marginal, not comfortable", "no buffer", "roughly negative $6-7K", "does not fund the reserves"); runs 1, 5 and 6 lead with a positive coverage headline plus conditions ("closes roughly cash-neutral if and only if"). The directions differ and the grader applied one judgement per run consistently across all three surfaces. Legitimate fail stands.
6. **Does the matrix reconcile?** Yes. Reconstructed per-run pass counts are 16, 20, 22, 18, 16, 17, matching the export exactly. Corrected pass@1 confirmed at 1/6: run 3's failures are exactly the six Rubric-Invalid criteria and nothing else.

**One error found and fixed in my own output.** The paired Oracle Event list in `S4_fixes.md` section C was incomplete on first writing. OE 22 (line 43) carries the literal `8,452.64`, which I had recorded as needing no change, and OE 28 (line 55) carries `7,483.42` and was missing from the table altogether. Both are now listed, and the table carries a completeness check against every occurrence of the four figures in the file.

## Third pass — fixes applied (2026-08-07, on operator instruction)

The phase STOP gate leaves fix application to the operator. The operator instructed otherwise, so all six rubric edits and every paired Oracle Event edit were applied here.

**Gate results after the edits**

| Gate | Result |
|---|---|
| `check_oe_rubric_sync.py` | exit 0, 28 OEs / 28 criteria |
| `check_rubric_antipatterns.py` | exit 0 after two rewrites, see below |
| `check_criterion_dependencies.py` | exit 0, still no dependent passing under a failed antecedent |
| `validate.py --phase rubrics` | PASS, **0 fails, 0 warns**, 6 notes |
| `validate.py --phase oe` | PASS, **0 fails, 0 warns**, 3 notes |
| `check_export_freshness.py` | FAILed on the expected rubric drift, then re-pinned; OK |
| `check_justification.py` | exit 0, unchanged |

**Three gate-forced corrections to my own drafts.** All three were caught by the gates rather than by me, which is the point of running them after every edit.

1. `check_rubric_antipatterns.py` raised MODERATE on criteria 4 and 10 for `FAIL only if`: *"makes every unenumerated shape a PASS, including plain omission."* The checker is right and outranks the phrasing the S4 runbook suggests for Bucket 1b fixes. Rewritten additively as `FAIL if X, and FAIL if Y`.
2. `validate.py --phase rubrics` warned that criterion 6's evidence introduced `2026-02-09`, a date its title does not carry. Reworded to "the stop-decision day itself", which the title already bounds.
3. `validate.py --phase oe` warned that OE 24 now referenced `warehouse` while its tool calls target Confluence, Docs and Drive. My own wording caused it; reworded to "the whole-dollar figure a query returns".

**Pin handling.** Applying the fixes moved `7_Rubrics.json` from `69713012b52f17d6…` (11,941 B) to `bf26e5373d7fbab6…` (13,703 B) and the freshness gate FAILed, correctly. The classification-time pin is preserved at `_aux/S4_input_pin.classification.json` and the pre-fix artefacts at `_aux/7_Rubrics.pre_s4fix.bak.json` and `_aux/6_Oracle_Events.pre_s4fix.bak.txt`. `8_Verifier_Fails.txt` is byte-identical throughout, so no per-run count, bucket call or all-failing set in these reports was invalidated by the edit. The matrix in `S4_verdict.md` describes the pre-fix rubric by construction and is superseded only by the next platform export.

## Gate results

| Gate | Entry | Exit |
|---|---|---|
| `phase_ready.py --phase s4` | OK, 4/4 artifacts | — |
| `parse_trajectories.py` | 6/6 runs, verdict OK | — |
| `check_export_freshness.py` | pinned, 2 inputs | re-verified, no drift |
| `check_criterion_dependencies.py` | exit 0, 13 edges, no hits | exit 0 |
| `check_oe_rubric_sync.py` | exit 0, 28 OEs / 28 criteria | exit 0 |
| `check_rubric_antipatterns.py` | exit 0 | exit 0 |
| `check_justification.py` | — | exit 0 |

No rubric or Oracle Event file was edited during this pass, so the exit runs of the sync and anti-pattern gates describe the same bytes as the entry runs. The fixes are drafted in `S4_fixes.md` for the operator to apply, per the phase STOP gate.

## Discrepancies surfaced

1. **The graded environment cannot serve the precision four criteria require.** The warehouse stores every `NUMBER` column as a half-up-rounded integer. This is a universe-wide property, not a Combo Fighter one, and it will invalidate any future HarmonyGames criterion that pins a warehouse-derived figure to the cent. It is worth carrying forward as a universe fact rather than as a task finding.
2. **A criterion passed on a value collision, and the checker could not see it.** `check_criterion_dependencies.py` catches dependent-antecedent inversions but not "the right magnitude from the wrong table". Criterion 10's single PASS is of the second kind. The `Hardness_Plan.md` risk register had already recorded the colliding row, as a coherence risk, and nothing downstream re-checked it against the acceptance band that was later written.
3. **Both [HIGH] stump hypotheses were solved 6/6.** The task's real difficulty came from four levers the plan does not name. Recorded to the meta logs.
4. **Raw pass@1 of 0.0 overstates the difficulty.** Corrected for the defective criteria it is 16.7%. Still a clear pass, but the raw figure should not be quoted as the task's difficulty.
