# Verification — AUDIT (prompt phase, strictest interpretation)

## Strictest interpretation re-applied
- Every "should" in the QC spec read as "must".
- Every NON-FAIL middle band collapsed to REVISE (none needed — all sub-dims genuinely 5/5).
- Density judged on the StarPM V4 PER-MODEL bar (design 40+, floor 15), NOT the V3-family 50/40 scheme (universe = starpm per _aux/Universe.txt).
- Every soft convention (Reference/Prompt_Format.md) treated as binding.

## Data sources consulted (re-verified from source — NOT trusting prior phase outputs)
- _aux/Universe_Split/airtable.airtable_records.json :: receb057b02f20052 (selReady 5/1 stale), recf7aecc318b2252 (John+James 5/14), rec651427ec0d84dd5a (selProg 6/25 target 6/26), recac236210094352 (MT-2026-1271 fldCompletionDate="" OPEN), recb403fe04c2f97683 (Rio Bend 214 twin) — all row_data parsed.
- _aux/Universe_Split/linear.linear_comments.json :: comment_16a0a0c53f... OPS-227 disposal-seized/parts-approval flip.
- _aux/Universe_Split/linear.linear_teams.json :: team_001 Airtable-is-SoR declaration.
- _aux/Universe_Split/slack.slack_messages.json :: 140558.../21f0475... latching chatter; C001 6/22 James "8D still open" corroboration cluster (Lens 2 finding).
- _aux/Universe_Split/slack.slack_channels.json :: C004 #make-ready.
- _aux/Universe_Split/contacts.contacts.json :: John Smith (starpm Lead) vs John Castillo (external gmail) recipient dedupe.
- StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md :: L76/L400/L528 BF4 + persona-anchor rule.

## Tool catalog (universe-aware)
- starpm -> StarPM_Base_Universe/7_Server_Tools_Details.json. Prompt names no tools; Gmail draft-only confirms "draft John an email" feasibility. Signature checks deferred to S2 (prompt names no params).

## Eval spec verified for this phase
- Evals_starpm/1_Prompt_Eval.md :: strictest reading applied — UGT no-middle-band (06/09), Feasibility no-middle-band, phantom tight-identifier grep, pre-solving/command-list/bolt-on gates, write-action-divergence + delegation-clarity gates, 2.8 fixed-date July 1 2026 litmus.

## QC spec re-verified
- Docs_starpm/7_QC_Spec_Doc1.json :: 14 applicable prompt/universe sub-dims rescored under strict interpretation, all 5/5. Stale "Jun-12" string in the JSON noted and superseded by 2026-07-01.
- Docs_starpm/13_QC_Companion.md :: NOT used as SSOT (Brookfield-contaminated per ROUTING_DECISIONS.md).

## All 9 lenses status
- Lens 1 strict QC scoring :: PASS (14/14 sub-dims = 5)
- Lens 2 answer-leakage sweep :: PASS (no prompt/artifact/figure leak; 1 universe-resident corroboration -> non-blocking S2/S3 advisory)
- Lens 3 hardness end-to-end :: PASS (5/5 levers, cited atoms)
- Lens 4 strict density :: PASS (~46/model, V4 per-model >= 40)
- Lens 5 adversarial review :: PASS (no write/recipient/state flip)
- Lens 6 lifecycle+narrative :: RETIRED (folded into Lens 1)
- Lens 7 anti-rationalization :: PASS (leak logged + routed, not dismissed)
- Lens 8 regression-anchor verification :: 62/62 PASS
- Lens 9 unique ground truth :: PASS (single end-state: 8D NOT ready)

## Verification statements
- [x] Validator (validate.py --phase prompt) re-run during audit; exit 0 (0 fails / 0 warns / 4 notes).
- [x] Regression-anchor suite executed; 62/62 PASS.
- [x] Anti-rationalization output check passed; no "considered flagging X but it's fine" dismissals (Lens 2 finding LOGGED + routed).
- [x] Verdict (PASS STRICT) recorded with explicit per-issue trail.

## Discrepancies surfaced
- Net-new (vs Council A/B): James's own 6/22 #maintenance corroboration of "8D still open" — non-blocking, routed to S2/S3 (require synthesis+writes for credit; optional authority-injection re-hardens).
- Validator "today = 2026-06-12" note is a null-Fact_Ledger fallback artifact; authoritative today 2026-07-01; end-state robust either way; zero prompt impact.
