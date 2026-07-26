# Cross-Source Verification — HARDNESS — Tasks/42_6a62ccac9492f2a60e456c1c

## Sources consulted
- Per-task data :: _aux/Universe_Split/quickbooks.quickbooks_entities.json — verified bills `528539050604` (Doc 2026-481, $8,400, VendorRef Big Bend 203, no CustomerRef) + `301715729067` (Doc PD-2026-084, $8,400, 3-line split) + AR invoice `109367557444` (Doc 2026-494, CustomerRef Robert Finley); Pete Donovan is a **customer** (`proj-f6f9edfeae5c`), NOT a vendor — no "Donovan Roofing" vendor exists (8 vendors, Big Bend = 203); no payment links either roof bill (double-pay exposure live).
- Per-task data :: _aux/Universe_Split/airtable.airtable_records.json — roof make-ready `rec8b679d92f30753` ($8,400, Pete Donovan, Ridgeview) + origin ticket `recb4aeaed326f156` (MT-2026-047, Finley portfolio) + Q2 budget-review make-ready rows.
- Per-task data :: _aux/Universe_Split/{slack.slack_messages,gmail.gmail_messages,gcalendar.gcalendar_events,linear.linear_issues,linear.linear_comments}.json — latching anchor (Donovan Roofing 5+ places), premature "we're good to go" (SL `a33ed…`/`7d94b…` 14:15/14:16) vs owner approval (GM `4bcbe384bedfd26f` 14:20), reserve-hold control in bill notes, buried conditions reply (GM `0427cad50efd8219`), OPS-100 owner report, budget-variance supersession OPS-29/27/41.
- Per-task data :: _aux/Fact_Ledger.json + _aux/Universe_Index/{graph_report,service_inventory,key_facts}.md — atom counts (amounts 403, invoice ids 504) and density signals; channels C005/C006/C007/C004 = Brooke's home.
- Eval spec :: Reference/Hardness_Playbook.md + Reference/Sessions/HARDNESS.md — 11-lever catalog + per-lever tool-call costs; StarPM per-model density scheme (40 design / 15 floor, applied to Opus and Gemini separately). Selected Lever 2 (flagship structured-skip) + Lever 10 (duplicate/reversal) + Lever 1 (latching) + Lever 6 (near-miss) + L31 (Gemini negative-directive); Lever 11 net-vs-gross ABSENT/not selected.
- Eval spec :: AGENTS.md hard rules — V4 injection is first-class (base rows never modified); density framework-scoped V4 = 40+ avg per model. Trajectory Tool Call Count dim (≥15 floor / 40+ design, PER MODEL) → projected Opus 48.5 / Gemini ~40.5, both PASS.
- QC spec :: Tasks/_meta/Learnings.md + Stump_Hypotheses.md + Hardness_Patterns_Log.md — QC-relevant calibration: banked dual-model 0/6 recipe (1 symmetric + 2 complementary asymmetric); item 3/9/10 (structured-store-skip symmetric, 0/12 twice); item 11/12 (L2 + L1-latching Opus-selective + L31 Gemini-selective); L31 (3x confirmed); robustness ranking (structured-skip > negative-directive ~ latching/reversal > net-vs-gross masked > near-miss weak); QC Trajectory T1 Tool Call Count band → Opus 48.5 PASS, Gemini ~40.5 PASS (tight, watch first run).

## Verification statements
- [x] At least 3 levers selected (5: Lever 2 + Lever 10 + L31 + Lever 1 + Lever 6); each cites a Learnings entry.
- [x] Density midpoint projection assigned per model to a StarPM band: Opus PASS (48.5 ≥ 40), Gemini PASS (~40.5 ≥ 40, tight).
- [x] Service breadth table populated (v11 G1): 7 distinct services, dominant (quickbooks) 33% < 60% → PASS.
- [x] Answer-leak flagged: $8,400 leaked verbatim; rubrics must target DERIVED facts (vendor-of-record, duplicate/$16,800-not, payment HOLD, correct property), not the headline amount — recorded in Hardness_Plan for S1/S3.
- [x] Load-bearing anchors verified directly against records (not only via sub-agent report): two roof bills, AR invoice, Pete-Donovan-is-customer, no-payment-link all confirmed by direct read of quickbooks_entities.

## Discrepancies surfaced
- Net-vs-gross (Lever 11) ABSENT on the roof spine (no credit memo/partial nets against the bills). Non-blocking — weakest StarPM lever per banked ranking; duplicate double-count ($16,800 vs $8,400) supplies the gross-vs-correct pressure instead.
- L9 authority-dismissal weak/absent natively — noted as OPTIONAL V4 injection (not required; the two Opus-selective levers already fill the Opus slot).
- Headline $8,400 leaked verbatim — handled by moving the correct-answer surface to derived facts. A design constraint carried forward to S1, not a defect.
- Gemini density tight (~40.5) — mitigated by mandating a 4-write deliverable mix in the S1 brief.

## Verdict
- PASS — 5 levers selected (anatomy matches banked StarPM dual-model 0/6 recipe: 1 symmetric + 2 complementary asymmetric + 2 support), per-model density PASS (Opus 48.5 / Gemini ~40.5), breadth PASS (7 services), all load-bearing anchors verified, answer-leak constraint documented. No blocking discrepancy. Proceed to S1.
