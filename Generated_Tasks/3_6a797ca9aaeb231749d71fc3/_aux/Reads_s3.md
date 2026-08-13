# S3 Reads log

Framework: `hg` (HarmonyGames V5). Universe: `harmonygames`. Model under test: **Claude Opus 4.7** (universe-scoped exception).

## Runbook + reference cards

- `Reference/Sessions/S3.md` :: bootstrap runbook; step 9 requires AUDIT auto-fire; step 5 lists validator checks.
- `Reference/AGENTS.md` :: HG uses `Generated_Tasks/`; hybrid `hg` framework (single-model verification + V4 injection/submission gates).
- `Reference/Rubric_Format.md` :: HG `hg` deltas — `category` is stored 4-value enum (`Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, `Process`); Process cap = 40%, zero Process valid; NO Outcome-majority requirement; Severity PRE-swap ordering (Overly Broad = Moderate, Overly Specific = Minor); Negative Criteria + Vague Exemplar Language rules apply.

## Root AGENTS.md hard rules re-confirmed

- Rule 1: HarmonyGames model under test is Claude Opus 4.7 (NOT 4.8).
- Rule 8: HG binary cap Process <= 40%, zero Process valid; no Outcome-majority.
- Rule 13: single-target uniqueness; see S3_S2_carryover.md for ART-770 ruling.
- Rule 14: 60-rubric ceiling; cut existence-only weak-signal criteria before coverage carriers.
- Rule 23: ordering constraints require Process rubric.
- Rule 31: HG negative-criteria gate (framework key `rubric_negative_criteria_gate=true`).
- Rule 32: HG persona ACL is prompt-feasibility gate; writes are not ACL-scoped.

## HG-specific spec docs (to be read this phase)

- `Docs_harmonygames/9_Common_Error.md` :: Part 3 rubric errors + all-failing-criteria default-to-remove rule.
- `Docs_harmonygames/2_Rubrics_Guidelines.md` :: HG framework rules.
- `Docs_harmonygames/12_Always_Failing_Rubrics.md` :: AF pattern catalog.
- `Docs_harmonygames/7_QC_Spec_Doc1.json` :: QC dimension bands, negative-criteria + vague-exemplar spec.
- `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` :: tool + parameter authority.

## Reference corpus (HG-specific)

- `QC_Tasks/V5_HG_Buckets/QC_Passed/*/7_Rubrics.json` :: voice + structure.
- `Reference/Strict_Convention_Inventory.json` :: allowed phrasings (Brookfield-derived; HG cross-check via Passed corpus above).

## Prior-phase artifacts (already loaded)

- `_aux/Universe_Split/` (43 row-level lookups verified in S2).
- `_aux/Fact_Ledger.json` (47 personas, 4 Marcuses, Combo-Fighters + GameOfDominoes present).
- `_aux/Hardness_Plan.md` (5 levers L1/L2/L6/L9/L10; density 56/7 services; ACL-revised anchors).
- `_aux/Verification_s2.md` (PASS with documented S3<-S2 carryover per operator ruling).
- `5_Prompt.txt` (Victor's art-import reconciliation ask; 11 lines).
- `6_Oracle_Events.txt` (30 OEs; PR #1 latching, PR #37 pushback, Trello check_items, 4-Marcus disambiguation, ART-770 comment, Trello check_item close + card comment, GDoc brief, GSheet tracker, final response).
