# Verification — AUDIT (oe) — `2_6a6beba55996ad2ada369b15`

Universe **harmonygames** (`hg`, single-model) · persona **Robert** (Executive) · today **2026-02-28** America/Chicago · model under test **Claude Opus 4.7**
Phase: `--phase oe`. READ-ONLY. Deliverable audited: `6_Oracle_Events.txt` (23 OE steps).

## Strictest interpretation re-applied
- Every "should" in the OE eval read as "must".
- Every NON-FAIL middle band collapsed to REVISE (Council B's OE Accuracy 4 is a soft fail).
- Density band: HarmonyGames scheme (>=40 midpoint PASS / 15-39 THIN / <15 INSUFFICIENT). The V3-family 50/40 bands were NOT applied.
- Every soft convention treated as binding.
- Any false-absence claim on the spine deliverable treated as a hard OE Accuracy defect, not advisory.

## Data sources consulted (re-verified from source — NOT trusting prior phase outputs)
- `_aux/Universe_Split/snowflake.snowflake.tables.json` (159 MB) :: streamed via `stream_rows`, memory-bounded (peaks 230-246 MiB, never json.load'd). Re-derived DAU (72 rows/36 dates/peak 801/new 845/sessions 55,101/D1 44.00 D7 22.10 D30 10.99/D1 37.34-50.73), REVENUE_DAILY (72 rows all 0.00), IAP combo 0 rows, AD_SPEND_DAILY combo lifetime 7,483.42 (6-channel split EXACT), post-02-09 strict 8,452.64 (280 rows/domino 5,569.66/combo 2,444.08/zombie 438.90), inclusive 8,922.12, 02-28 = 346.00 (combo 160.88, max date 02-28), CASH_BALANCE 02-28 (cash 2,500/net_burn 22,500/runway 0.1/headcount 6/"Company wind-down initiated"), MONTHLY_BURN Feb cats sum 20,000. REVENUE_DAILY_V2 title_id = {domino_delights, zombie_match_3d}, UA_SPEND_UNIFIED_V2 same — combo=0 both. All EXACT.
- `_aux/Universe_Split/slack.2026-02.json` (3.6 MB, 3,081 Feb msgs) :: re-parsed through `stream_rows` (row_data is a nested JSON string). All 13 cited timestamps FOUND and verbatim-matched. Cross-channel obligation sweep across ALL Robert-reachable Feb channels.
- `_aux/Universe_Split/slack.slack.channels.json` :: C0ADGSZKR3R = winddown (private, created 1770663237); C07C2866011 = executives; C04UEQVDVB7 = admin_foundersonly.
- Persona reachability by AUTHORSHIP (members[] unusable per Hardness Plan): Robert #winddown 21, #executives 132. C04UEQVDVB7 (admin_foundersonly) — Robert authored 0 → NOT reachable → correctly cannot poison the derivation.

## Eval spec verified for this phase
- `Evals_harmonygames/2_OE_Eval.md` :: OE Completeness 5, OE Negative Events 5. OE Accuracy **< 5** under strict reading — a persona-reachable message quantifies obligations the OE asserts are unquantified (F1).

## QC spec re-verified
- `Docs_harmonygames/7_QC_Spec_Doc1.json` :: "Inaccurate Oracle Events 12/12" is the top HG defect (per `9_Common_Error.md`). F1 is exactly that class — not a wrong number, a false statement that numbers do not exist.
- Universe / Cross-service Coherence (binary) :: PASS — the 20,000-vs-22,500 burn gap is NOT load-bearing in any OE, so it causes no agent failure. S3 must keep it latent.

## Deterministic floor (cited, not re-derived)
- `validate.py --phase oe` :: PASS, 0 fails, 0 warns, 3 notes, 23 steps.
- `check_qc_binary.py` :: 5/5 measurable binary sub-dims PASS.
- `verify_universe_atoms.py` :: PASS, 3 atoms.
- `check_persona_acl.py` :: 0 findings.
- `check_oe_rubric_sync.py` :: SKIP (no 7_Rubrics.json yet — expected at S2).
- Regression anchors (`test_regression_anchors.py`) :: 89/89 PASS (incl. v22 RA-5/RA-6/RA-7 HG-specific).

## Findings (full detail in `_aux/Council_Reports/AUDIT_oe.md`)
- **F1 [MAJOR — OE Accuracy / UGT / Truthfulness]** OE 16 + OE 18 assert Unity/Singular obligation amounts are "never stated" and "the universe does not contain [a total liabilities figure]". FALSE: ts `1770765511.243329` #executives (Robert-reachable) states Singular $18,750, Unity ~2.348×9 months, Helpshift $150×8. Corrupts the coverage verdict — the spine deliverable. Fix-in-place: rewrite OE 16/18 and the OE 20 "coverage verdict" element to carry the #executives figures; keep SVB alone as the unquantified gap; reconcile the Helpshift $1,500 (02-09, ×10) vs $1,200 (02-10, ×8) variance.
- **F2 [MINOR]** OE 7 attributes "Excludes Combo Fighter prototype monetization" to `calc_metadata`; it is the REVENUE_DAILY_V2 **table comment**. `calc_metadata` is `{"excludes_prototype": true, "reconciles_to": "shipped_games_revenue", "version": "v2"}`. Both facts true, locations conflated.
- **F3 [MINOR]** OE 2 says the 1770664094 message "opens 'After reviewing…'"; it is a pasted email draft opening "Hi [PERSON_NAME_1999],". Say "states" not "opens".

## All lenses status
- Numbers :: all snowflake/derived EXACT; zero wrong values. Defect is a false absence-claim (F1).
- Slack ts :: 13/13 FOUND, verbatim. Clean.
- Numeric visibility :: every figure SUM/AVG/MIN/MAX/GROUP BY exposable; no over-precision. Clean.
- Authority rank 6 :: all four decompose directives trace element-by-element to prompt sentences; only defect is OE 20's "coverage verdict" inheriting F1's content.
- UGT still-running spend :: 8,452.64 dominant (agree Council B, advisory). Secondary to F1.
- Tool/param exactness :: 0 fails; all HG traps correct. No finding.
- Density :: my own sketch necessary ~26-30, total ~37-48, midpoint ~42-43, >=4 services. HG >=40 = PASS. F1 fix only raises it.
- Hardness :: L11/L2/L8/L10/L7 all exercised; L8's obligations endpoint corrupted by F1 (chain runs, lands wrong). Fixing F1 restores it.
- Coverage both directions :: forward + reverse hold; P4 "who we still owe" mis-grounded (F1, accuracy not coverage).
- Rule-20 self-check :: F1 catches a defect class NO deterministic gate reaches (cross-channel reachability + semantic false-absence). No lens padded.

## Verification statements
- [x] Validator (`validate.py --phase oe`) re-run during audit; exit 0.
- [x] Regression-anchor suite executed; 89/89 PASS.
- [x] Every load-bearing figure and all 13 Slack timestamps re-derived from source; per-atom evidence table in AUDIT_oe.md.
- [x] Anti-rationalization output check: no "I considered flagging X but decided it's fine because…" line survives. F1 was NOT rationalized away despite Council B declining the UGT concern on the still-running spend — F1 is a distinct, stronger break.
- [x] Verdict recorded with explicit per-issue trail.

## Discrepancies surfaced
1. Both councils swept #winddown for obligation quantification; neither swept #executives, where Unity/Singular amounts are stated and Robert-reachable. This is the F1 blind spot (AGENTS.md rules 18/19: a council's own census cannot catch its own blind spot).
2. Council B issue 5 (OE 7 V2 game names unverified) is RESOLVED in AUDIT's favor: title_id values ARE domino_delights + zombie_match_3d. The remaining OE 7 defect is the calc_metadata/table-comment location conflation (F2), not the names.
3. Council A A3 "SVB quantified nowhere" is correct and unchanged; the F1 finding does NOT touch SVB — it touches Unity/Singular, which A3 never checked.

## Verdict
REVISE — F1 is fix-in-place. Rewrite OE 16/18 (+ OE 20 coverage element) to incorporate the #executives obligation figures and reconcile Helpshift, then re-run Council A/B on the revised OE.
