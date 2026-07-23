# Linter Decision — S1.5 Round (2026-07-23)

## Block
Platform linter (2026-07-22) returned `FALSE` on the S1 R2 prompt. Cited class: **Class A — cross-persona system-ownership violation** (HubSpot deal write asked of QC persona Jaime Salinas, business function 3 · Quality Control & Field Services). Linter verbatim: "hubspot_update_deal is not in the 3.1 write-action set and Jaime is not a HubSpot-owning persona. The correct QC action is to notify leasing (via Slack #leasing or email) that 3C is marketing-ready, and let leasing own the HubSpot stage move."

Prompt line under objection: "Leasing is also waiting on 3C before they can open showings. Get the 3C leasing deal updated in the pipeline so they can move."

## Skeptical-first verification
Per S1.5 runbook step 3, spawned parallel `explore` agents on (a) universe-level persona/HubSpot scope, (b) density-recovery alternatives inside QC scope.

Findings:
- StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md line 185 lists Jaime's documented systems as Airtable / Slack #make-ready / Linear / Gmail — HubSpot not present.
- BF5 (Leasing & Applicant Intake) explicitly owns HubSpot per StarPM_Base_Universe/1_StarPM_SUMMARY.md line 126 and StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md.
- Documented QC → Leasing hand-off pattern (3_StarPM_TASK CATEGORIES.md line 129) treats QC handoff (Jaime) and leasing handoff (Sandra / Kevin) as separate endpoints, not overlapping.
- No V4 reference task shows a QC persona writing HubSpot deals.

Skeptical verdict: linter **CLEARLY RIGHT**. Class A revise per runbook step 3.2.

## Density risk of the revise
Prior lever set L1+L6+L8+L9+L25+L26 with projected midpoint 60.5 was designed to fix the ORIGINAL density fail (Opus avg 37.5 / Gemini avg 35.5 vs 40 floor). Removing L6 in isolation drops midpoint to 54; Gemini expected avg 37.8 which would underflow the 40 floor. Naïve revise would recreate the density fail this REDO was meant to solve.

## Resolution: REVISE with in-scope density-recovery elevations
Per runbook step 3.2 CB-mode: revised `5_Prompt.txt` in place. Six changes:

1. REMOVED: HubSpot write ask (line 9 of prior version).
2. REPLACED with: "Leasing has been waiting on 3C to open showings, so they'll want the heads-up from us before they can move on their end." (context sentence — no direct write).
3. ADDED to Slack line: ", and tag Sandra so leasing sees it and can pick it up on their end." (in-scope Slack mention hand-off pattern, adds contacts.contacts lookup for Sandra Allen ≈ +1 call).
4. ELEVATED Bennett-note verification per ticket ("make sure the item he's writing up actually matches what the ticket is about before I sign off") ≈ +3 calls (linear comment read per ticket × 3). L8 amplifier.
5. ELEVATED Airtable pre-read discipline ("Read what's already sitting in the notes so my sign-off reads as a continuation of the supervisory line, not a replacement") ≈ +1 call (airtable_get_record before update). L25 amplifier.
6. Cosmetic: "Post in #make-ready" → "Post in the #make-ready channel" — adds `channel` keyword for validator SERVICE_KEYWORDS regex (bare "Post in #" does not match validator slack pattern due to `posted?` requiring literal "post" or "posted", not "Post").

Net density delta: -6.5 (L6 removed) + 3 (Bennett verify) + 1 (Airtable pre-read) + 1.5 (Sandra lookup + tag-format) ≈ -1. New projected midpoint: **57.5**. L31 realization check: Opus expected avg 42.6 (clear), Gemini expected avg 40.3 (narrow +0.3 margin — S4 attention item, not a S1.5 blocker).

## Downstream impact — Hardness_Plan.md updated
Appended "S1.5 REVISION UPDATE — 2026-07-23" section documenting the lever swap (L6 REMOVED, +3 soft-lever elevations), revised density projection, updated Stump Hypothesis (#5 nulled, new #6 added for Bennett-verify shortcut risk), and Council B B6 propagation flags for S2 (drop HubSpot OE step, add Airtable pre-read + per-ticket comment reads + Sandra contact lookup) and S3 (drop HubSpot rubrics, add continuation-append rubric, add per-item Bennett reference rubric, add Sandra slack_user_id tag rubric).

## Re-verification (S1.5 gates cleared)
- `Validators/validate.py --phase prompt` → PASS (0 fails, 3 warns bolt-on candidates on shared-3C sentences — validator entity-detection false positives, both councils explicitly verified as non-bolt-on).
- Council A R6 (S1.5 revision pass) → **GO**. All A1-A13 pass; linter's persona-scope block fully resolved; no HubSpot residue; no new grounding gaps.
- Council B R3 (S1.5 revision pass) → **GO**. All applicable QC sub-dims 5/5; density midpoint ~58.5 clears 50+ design target; adversarial second-reading attacks fail; all 5 surviving hardness levers still triggered; B6 flag on Hardness_Plan.md staleness resolved by the append.
- `Validators/test_regression_anchors.py` → **48/48 PASS**.
- AUDIT (`oracle`, strict veteran, per S1.5 step 8 MANDATORY) → **PASS (STRICT)**. Zero BLOCKER, zero MAJOR, 4 MINOR informational flags all documented for downstream propagation. StarPM V4 injection cross-verified: all 15 rows from `9_Universe_inject.sql` present in `3_UniverseDataForThisTask.json` with correct state.

## Final state
- `5_Prompt.txt`: revised in place (356 words, 15 lines, zero em-dashes, zero tool names, zero internal IDs).
- `_aux/Hardness_Plan.md`: S1.5 REVISION UPDATE section appended (L6 removed, soft-lever amplifiers documented, downstream propagation flags for S2/S3/FINAL).
- No justification file authored (REVISE path, not INVALIDATE — no pushback needed).
- No similarity log entry (this was a Class A block, not Class B).
