# OE Solvability + Coverage — S2 — Tasks/40_6a614767cd5b60ad96902fb4

**Universe:** starpm (V4) · **Deliverable:** 6_Oracle_Events.txt (19 OEs) · **AUDIT:** PASS (STRICT) after 1 REVISE round.

## OE-to-prompt coverage map (forward: every prompt ask has >=1 OE)

| Prompt ask (5_Prompt.txt) | Discovery OEs | Write OE |
|---|---|---|
| 1. Pull the current Unit 14 make-ready record, confirm true state, move forward only as facts support, tied to Tanya's unit | OE 1 (base/tables), OE 2 (disambiguate Sunset Ridge vs Rio Bend), OE 3 (read hold note), OE 4 (delinquency supersession), OE 5 (DLQ/EVF tickets) | OE 14 (Airtable update: keep selSched, hold note) |
| 2. Figure where the account stands, post a clean status in the make-ready channel | OE 6 (Slack eviction/filing), OE 7 (superseded payment commit), OE 8 (QB customer), OE 9 (QB arrears + books-vs-notes) | OE 15 (slack_send_message C004 #make-ready) |
| 3. Draft (do not send) an email to Brooke walking Unit 14 end to end | OE 10 (HubSpot ESA), OE 11 (Gmail approval), OE 13 (contacts: Brooke) | OE 16 (create_draft to Brooke, draft-only) |
| 4. Set a Google Calendar reminder early next week | (uses today 2026-07-01) | OE 17 (create_event 2026-07-06) |
| 5. Update the open ticket so it is not stale | OE 12 (find OPS-32) | OE 18 (save_comment OPS-32) |

OE 19 = content-requirements synthesis (source for the Outcome 1.2 content rubrics on OE 15 + OE 16). Reverse coverage: every OE maps to a real prompt ask (no scope creep).

## OE-to-rubric mapping preview (for S3)

| OE | Type | Rubric preview |
|---|---|---|
| OE 14 | Write | Outcome 1.1 (make-ready record updated, status stays Scheduled, NOT advanced) + 1.2 (hold-note content: cannot begin/market until possession returned). **Accept recc83c05d889b354 OR reca8230a8fd9ff51; FAIL rec94e86a3007dd5e (Rio Bend). Grade on hold content + correct-tenant/property, not exact rec id.** |
| OE 15 | Write | Outcome 1.1 (status posted to #make-ready / C004) + 1.2 (account = active eviction, plan breached, not on a plan; turn held) |
| OE 16 | Write | Outcome 1.1 (draft to brooke.phillips@starpm.com created, NOT sent) + 1.2 (end-to-end content: account state, turn hold, open items incl. owner-approved-but-JP-coordination, approved ESA on record, Sunset Ridge vs Rio Bend disambiguation) |
| OE 17 | Write | Outcome 1.1 (calendar reminder set early next week, ~2026-07-06, Lisa's calendar) |
| OE 18 | Write | Outcome 1.1 (comment on the open eviction tracker OPS-32) + 1.2 (status content: turn held, active eviction, ESA on record) |
| OE 1,3,4,5,6,7,8,9,10,11,12,13 | Read/Discovery | Usually NO rubric — proven by the downstream Outcome 1.1/1.2. Load-bearing discovery facts (possession NOT returned; account in active eviction; approved ESA on record; Unit 14 = Sunset Ridge not Rio Bend) surface inside the OE 14/15/16/18 content rubrics. |
| OE 2 | Read/Discovery | The Unit 14 near-miss disambiguation is enforced via the OE 14 correct-record rubric (fail Rio Bend), not a standalone rubric. |

**Outcome 2.1 candidate:** the prompt delegates ("lay it all out in that email for me") — the key findings land in the OE 16 draft, so 2.1 (final-response report) is light; S3 to decide whether a 2.1 rubric on reporting the hold/eviction/ESA findings back to Lisa is warranted.
**Process candidates:** the negative-directive hold (do not advance / do not mobilize) is captured by the OE 14 Outcome 1.1 (status stays Scheduled) — no ordering Process rubric obviously required; S3 applies the three-condition test.

## Hardness levers exercised (Council B B4 + AUDIT Lens 3, all confirmed)
S1 possession-not-returned/negative-directive hold -> OE 3/14/15/16/19; S2 delinquency supersession/latching -> OE 4/6/7/9; S3 HubSpot ESA structured-DB skip -> OE 10/11; S4 Unit 14 near-miss -> OE 2/14 (Rio Bend barred at the write step); S5 authority-relayed anchor -> OE 5/6.

## Density (StarPM V4 bar 40+/model)
Opus ~46, Gemini ~43 (both >= 40). Hardness_Plan midpoint ~48. PASS per model.

## AUDIT verdict
PASS (STRICT). OE Completeness 5/5, OE Accuracy 5/5. Round 1 REVISE (OE 14 write-target co-target [Minor] + OE 9 invoice-gloss [Nit]) applied and re-cleared by Council A GO + Council B GO + AUDIT PASS (STRICT). No PROPAGATE TO S1.

## Carries to S3 (non-blocking, from council + AUDIT forward-notes)
1. Make-ready write rubric: accept either recc83c05d889b354 or reca8230a8fd9ff51, fail Rio Bend rec94e86a3007dd5e; grade on hold content + correct record, not exact id. (Also baked into OE 14 body.)
2. ESA rubric: phrase as a behavioral property ("an approved reasonable-accommodation on record ... before turnover/adverse action"), not locked to a specific HubSpot ticket.
3. Account-state rubrics (Slack post, Brooke draft): load-bearing fact = active eviction / plan breached; treat dollar figures ($2132.00 arrears, $8173.44/0.00) as supporting detail ("or similar"), not hard-locked.
4. QuickBooks decoy awareness: bill QR-2026-0441 VendorRef is "Alamo HVAC Services" (decoy) though content is Tanya's rent ledger (Balance 2132.00); any rubric citing it keys on the arrears + Tanya linkage, not the vendor. Bill 2026-EV-047 Balance 185.00 confirmed.
