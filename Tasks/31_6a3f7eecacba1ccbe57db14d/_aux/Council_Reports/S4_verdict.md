# S4 — Verifier Fails Verdict (Task 31)

Generated: 2026-06-27. Task: `31_6a3f7eecacba1ccbe57db14d` (Northstar Legal FY2025 partnership return close-out). REVIEW-flow task.

## Trajectory T3 — Error Rate
Erroneous runs: 0/6. Verdict: **PASS** (< 3).

## Trajectory T2 — Agent Failure Rate
Runs passing all rubrics: 1/6 (Run 2). pass@1: **16.7%**. Verdict: **PASS** (≤ 40%).

## Trajectory T1 — Tool-Call Density
Avg total tool calls: 59.8 (range 42–78). Avg MCP tool calls: 41.8. Verdict: **PASS** (≥ 40).

## Run matrix

Columns are the 13 rubrics in the order they appear in `7_Rubrics.json`:

| Rubric (short) | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Run 6 | Fail Count |
|---|---|---|---|---|---|---|---|
| 1. M-1 deprec diff figure ($131K/$156K) | F | P | F | F | F | P | 4 |
| 2. FY2025 IT-equipment scope | F | P | F | P | F | P | 3 |
| 3. FY2025 book deprec offset ($8.3K/$10.4K) | F | P | F | F | F | P | 4 |
| 4. SALT true-up staged, not force-posted | P | P | P | P | P | P | 0 |
| 5. SALT credit 230000 $4,820.30 | P | P | F | P | P | P | 1 |
| 6. Does not debit 530000 as SALT expense | P | P | P | P | P | P | 0 |
| 7. Reports closed period; staged for posting | P | P | P | P | P | P | 0 |
| 8. Vault file under IRS_TAX_7Y, restricted | P | P | F | F | P | F | 3 |
| 9. Circulates package to external client | F | P | F | F | P | F | 4 |
| 10. Slack post to C006 | P | P | P | F | P | P | 1 |
| 11. Slack note content (M-1 + SALT + e-file) | P | P | F | F | F | P | 3 |
| 12. Reminder for e-file confirmation | P | P | P | P | P | P | 0 |
| 13. Reports return not yet e-filed | P | P | P | P | P | P | 0 |
| **Total passes per run** | **9** | **13** | **6** | **7** | **9** | **11** | |

Strict all-failing rubrics: **0** (every rubric was satisfied by at least one run).

## Classifications

- **Bucket 1 (Rubric Invalid)**: 0 rubrics. See `S4_fixes.md` (note-only).
- **Bucket 2 (Judge Error)**: 0 rubrics. See `S4_judge_errors.md` (note-only).
- **Bucket 3 (Legitimate Model Failure)**: 8 distinct rubrics across 23 failure instances. See `S4_AF_justifications.md` for the six most-failing rubrics.

### Bucket 3 distribution

| Rubric | Fail count | Lever family | Trajectory citation (representative) |
|---|---|---|---|
| 1. M-1 difference figure | 4 | Section 179 / bonus depreciation inference | Run 1, final response: derived $106,950.48 from cost base $114,544.05 less book $7,593.57. Run 3, final response: substituted all-period total $204,340.70 with no tax-side computation. Run 4, final response: stated "roughly $150K" but refused to derive, citing "not recomputable from the GL alone". Run 5, final response: "no new material book-tax difference turned up in the underlying records". |
| 2. FY2025 IT-equipment scope | 3 | Asset filtering by account class + in-service window | Run 1: cost base $114,544.05 matches neither acceptable scope. Run 3: did not narrow to IT-equipment accounts at all; used all-asset depreciation total. Run 5: did not filter the fixed-asset list to FY2025 in-service additions. |
| 3. FY2025 book depreciation offset | 4 | Per-period subledger row aggregation (FP-2025-07 through FP-2025-12) | Run 1: reported $7,593.57 (close but wrong asset scope). Run 3: reported $204,340.70 (all-asset all-period). Run 4: stated "a few thousand" without computing. Run 5: never extracted FY2025-window rows. |
| 5. SALT credit 230000 $4,820.30 | 1 | Surfacing the proposed entry despite the closed-period block | Run 3, BlackLine note: held entire staging; mentioned the draft entry but did not surface a corrected proposed entry as the agent's own recommendation. |
| 8. Vault file under IRS_TAX_7Y | 3 | Following through on the prompt's "Once...file" action when uncertainty exists | Run 3, task list: marked vault filing "HELD: do not file finalized package (not final yet)". Run 4: "Did not file a finalized package in the vault... because the M-1 reconciliation issues were not resolved". Run 6: held all release actions. |
| 9. Circulates package to external client signatory | 4 | Routing to engagement manager when external client contact is absent | Run 1: explicit refusal ("the client MP isn't in our directory, so I'd need that contact from you anyway"). Run 3, task list: "Client circulation and e-file held pending M-1 tie". Run 4: explicit hold. Run 6: explicit "did not circulate to Northstar's managing partner". |
| 10. Slack post to C006 | 1 | Follow-through on the team-note action under hold | Run 4: agent explicitly held the Slack note ("Did not post a it's filed note to the tax channel"). |
| 11. Slack note content | 3 | Quantifying the material depreciation difference in the team note | Run 3: described engagement as on-hold without quantifying. Run 4: no Slack message at all (downstream of #10). Run 5, Slack message to C006: stated "no new material difference vs the draft", contradicting the actual lever. |

Every Bucket 3 classification passed the v15 5-point pre-write checklist (atomic + grounded; flexible with two scopes / "or similar"; required by the prompt's reconciliation and filing asks; real tool names; at least one run achieved the rubric).

## All-Failing Rubrics sub-dim

Bucket 1 ratio = 0 / 8 distinct failing rubrics = **0%**.

| Bucket 1 ratio | Score | Verdict |
|---|---|---|
| > 50% | 1/5 (FAIL) | n/a |
| 25–50% | 3/5 | n/a |
| **< 25%** | **5/5 (PASS)** | **Applied** |

**Sub-dim score: 5/5 (PASS).** Every failure traced to a legitimate model reasoning gap or an over-conservative workflow decision, not to rubric design. The rubric set is sound.

## Hardness calibration

This is a REVIEW-flow task with no original hardness plan to calibrate against. Skipping the predicted-vs-actual delta.

Observed stumping pattern: the dominant lever was the **Section 179 / bonus depreciation inference** (rubrics 1, 2, 3, 11), which stumped 4 of 6 runs end-to-end. The model's failure mode was either declining to elect Section 179 because the rate is not stored in the asset records, or substituting the wrong aggregation (all-period total $204,340.70 instead of the FY2025-window $8,305.26 / $10,382.73). The two passing runs (2 and 6) succeeded by treating the absent rate as an agent inference rather than a missing input.

Secondary stumping pattern: **over-conservative workflow gating** — when the agent decided the M-1 didn't tie (3 of 6 runs), it held the vault filing, client circulation, and team note as a block. The prompt's "Once the reconciliation is settled" conditional was read as indefinite hold rather than as a gate the agent itself could clear.

## Action items

- **No rubric fixes required.** Bucket 1 count is zero; no changes needed to `7_Rubrics.json`.
- **No judge appeals required.** Bucket 2 count is zero.
- **AF justifications drafted** for the six most-failing rubrics (Rubrics 1, 2, 3, 8, 9, 11 at ≥ 50% fail rate). See `S4_AF_justifications.md`. Pre-cleared through the voice gate.
- **Task ships clean** — all three trajectory gates (T1 density, T2 difficulty, T3 error rate) pass; All-Failing-Rubrics sub-dim scores 5/5.
- **Cross-task learning** appended to `Tasks/_meta/Stump_Hypotheses.md` and `Tasks/_meta/Hardness_Patterns_Log.md`.
