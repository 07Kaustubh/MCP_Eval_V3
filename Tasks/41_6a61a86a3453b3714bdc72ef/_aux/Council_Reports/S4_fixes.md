# S4 Bucket 1 (Rubric-Invalid) fixes — Tasks/41_6a61a86a3453b3714bdc72ef

## Status this run (post-fix re-grade): NO OUTSTANDING FIXES

This S4 pass classifies the re-graded output (8a/8b 2026-07-24 22:41-42) produced after the prior fix batch was applied. **Bucket 1 this run = 0.** The one prior substantive fix (R6 vs OE 14) is CONFIRMED EFFECTIVE — see below. Nothing further to change in `7_Rubrics.json`.

## CONFIRMED EFFECTIVE — R6 reconciliation with OE 14 (prior fix, verified by this re-grade)

**Prior defect:** R6 (Agent updates Tanya's Sunset Ridge Unit 14 make-ready record) whitelisted an exact-ID accept-set (`recc83c05d889b354` / `reca8230a8fd9ff51`) and failed every other Tanya-Unit-14 record — contradicting OE 14's own grading guidance ("grade on the hold content plus correct tenant and property, **not the exact record id**"). It produced inconsistent grading: identical writes to `receee45491536859` + `rec3782834f35df50` were passed on one run and failed on others.

**Fix applied (2026-07-24, before the platform re-run):** R6 rewritten to grade on tenant + property (Tanya Mitchell's Sunset Ridge Unit 14 make-ready turn) and the hold content, "not the exact record id", excluding only Rio Bend `rec94e86a3007dd5e`. Aligned with OE 14. R1 and R16 fail-lists also gained **$2,287.50** (invoice 7214's three charge lines summed), the dominant wrong answer.

**Re-grade result (this run):** R6 passes **6/6 on Opus** (and was never a Gemini fail). The records that previously flip-flopped now grade consistently and pass. `grep` confirms `$2,287.50` is present twice in `7_Rubrics.json` (R1 + R16 fail-lists). The fix removed the flip-flop without lowering difficulty (pass@1 stays 0/6 both models — every run still fails on the balance and the model-asymmetric levers).

**Calibration note:** the R6 pre-fix "fails" were NOT a legitimate difficulty lever. They were an over-strict rubric false-failing correct writes (right tenant, right Unit 14, right hold content). Do not count them as an L10 reversal/supersession stump (the prior _meta calibration entry is corrected on this point — see `Tasks/_meta/Hardness_Patterns_Log.md` re-run delta).

## Re-checked this run, NOT changed (deliberate — confirmed valid, not Bucket 1)

- **R14** (no-marketing directive in the #make-ready CREW channel): valid. Deliberate negative-directive lever (L31, Gemini differentiator), grounded in OE 16 + the prompt ("us marketing something we can't deliver"), a distinct atomic check from R20 (same prohibition in the owner draft, which R14's failing Gemini runs still passed), and achievable (Opus 6/6, Gemini 3/6). Not over-decomposition; not channel lock-in. Bucket 3.
- **R4 / R11 / R18** (owner-authorization): valid and now grading consistently. FAIL fires when the run names Harris as owner or misdirects the owner email to Harris; PASS fires when the run lands on Castillo (flagging the Harris discrepancy as a note is allowed). Ground truth (EVF-2026-014 + Gmail 06-30) unambiguously attributes the on-file authorization to Linda Castillo. Achievable (Gemini 6/6; Opus 3/6). Bucket 3.
- **R1 / R2 / R16** (balance): valid, universe-grounded (bill QR-2026-0441 lines re-confirmed in raw QB entities), achievable (bill is queryable via `search_bills`). The flagship symmetric stump. Bucket 3, AF justifications shipped.

## Validity summary (Phase 2)

Every failing criterion was validated against the universe: tools exist, expected values exist and were re-confirmed in `_aux/Universe_Split/`, and each criterion traces to a specific ask in `5_Prompt.txt`. No phantom tools, no wrong expected values, no bundled/over-strict criteria that a valid agent approach would trip. No hard-invalid rubric remains.
