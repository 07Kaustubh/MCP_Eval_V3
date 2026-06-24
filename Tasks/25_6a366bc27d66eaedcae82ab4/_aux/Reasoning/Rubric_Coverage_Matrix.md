# Rubric Coverage Matrix — S3
# Task: 25_6a366bc27d66eaedcae82ab4
# Date: 2026-06-22
# Validator: PASS (0 fails / 0 warns / 2 informational notes)
# Council A (Grounding): GO
# Council B (Adversarial QC): GO (8/8 sub-dims at 5/5, density midpoint ~50, all 5 levers covered)
# Strict Veteran AUDIT: PASS (STRICT) — strict midpoint ~52, zero leakage, all levers trace end-to-end, zero entity drift

Rubric set: **20 rubrics, all outcome, 0 process.** Nested schema. Sub-type distribution: 8 write-action (1.1), 8 action-content (1.2), 4 key-fact report (2.1).

## Rubric short-label index

| ID (short) | Sub-type | Short label |
|---|---|---|
| W1 (80d39aeb) | 1.1 | Stage and submit JE totaling $147,825 across 3 service-line credits with offsetting debit to 119000 |
| C1 (07a64324) | 1.2 | Staged JE business justification references Andrea's stage-completion review + exc_1ddfc978ce5a4d |
| W2 (4a022be0) | 1.1 | Add accept-timing variance_explanation on BL-75810CD0FEE4 without submit/approve/certify |
| C2 (1af03630) | 1.2 | Recon update cites Hannah 2026-06-02 + FP-2026-06 BD3 + exc_1ddfc978ce5a4d |
| W3 (8ca25c9d) | 1.1 | Update exception exc_1ddfc978ce5a4d to record disposition without resolving (state remains investigating) |
| C3 (3952b3e7) | 1.2 | Exception update cites Hannah 2026-06-02 + FP-2026-06 BD3 |
| W4 (c2d08157) | 1.1 | RV upload — classification restricted, retention AICPA_SQMS_7Y, linked to staged JE |
| C4 (ac93a531) | 1.2 | Memo body covers run_e33ed2561f2c46 success / 2083 / 2083 / 0 vs partial-feed narrative |
| W5 (a485a9e1) | 1.1 | Slack reply on C005 thread_ts 1780248600.000000 |
| C5 (2e0b7395) | 1.2 | Slack reply covers $147,825 staged + accept-timing on BL-75810CD0FEE4 / exc_1ddfc978ce5a4d per Hannah |
| W6 (07c488a4) | 1.1 | Email reply on email_scen_059_wip_recognition_0000 from George to Andrea with Margaret cc |
| C6a (b4eaf6a4) | 1.2 | Andrea reply confirms $147,825 staged across 3 service lines + queued for Daniel |
| C6b (5248e45d) | 1.2 | Andrea reply confirms $4,390.62 residual parked + accept-timing applied per Hannah |
| C6c (0e49d120) | 1.2 | Andrea reply surfaces run_e33ed2561f2c46 success / 2083 / 2083 / 0 vs partial-feed narrative |
| W7 (0e88aacd) | 1.1 | Delete reminder_scen_010_orphan_exception_0000 |
| W8 (702ef241) | 1.1 | Add new reminder due ~2026-07-03 for FP-2026-06 BD3 revisit on exc_1ddfc978ce5a4d / BL-75810CD0FEE4 |
| D1 (10033d88) | 2.1 | Final response: feed run success / 2083 / 2083 / 0 contradicts partial-feed narrative |
| D2 (2640ecb4) | 2.1 | Final response: open review note rn_564e65ce0d594f flagged as unresolved (SLA past) |
| D3 (576e29f5) | 2.1 | Final response: blackline_bdbbea5db590 identified as parallel scaffold of same incident |
| D4 (32b42ee4) | 2.1 | Final response: BL-75810CD0FEE4 current state (in_progress, $4,390.62, no attachments / reviewer / submitted / approved / certified) |

## Prompt sentence → OE step(s) → rubric(s)

| Prompt sentence (paraphrased) | OE step(s) | Rubric(s) |
|---|---|---|
| Context: "Andrea sent over the engagement-stage completion review ... $147,825 lined up for recognition" | OE 2 (read Andrea email scen_059) | (context — surfaced through C1 + C6a) |
| Context: "She also flagged a separate residual variance ... leave it out of this cycle as next-period cleanup" | OE 2 (Andrea email scen_059 anchor) | (context — surfaced through C6b) |
| Context: "Hannah came back on the exception side and signed off on accept-timing for May, with a note to revisit at FP-2026-06 BD3" | OE 10 (Hannah reply scen_010_orphan_exception_0009) | (context — drives C2, C3, C6b, W8) |
| Context: "Anaya was the preparer, and her read is that the May subledger feed retry produced a partial batch" | OE 4 / OE 5 (recon variance_explanation by anaya.wallace) | (latching context — falsified by D1, C4, C6c) |
| "Pull the May engagement-stage support, confirm the recognition figure ties out across our records, and walk the reconciliation end to end" | OE 2 (pull support); OE 3 → OE 6 (recon walk); OE 13 → OE 15 (subledger feed read) | D4 (current recon state), D2 (open review note), D1 (feed run finding), D3 (doppelganger), C1 (JE business justification ties to support) |
| "I want the actual state, the evidence attached, anything else opened or reviewed against it that I have not seen including any open reviewer notes" | OE 4 (canonical recon state — attachments=[]); OE 7 (review notes — rn_564e65ce0d594f); OE 6 (audit trail) | D4 (actual state + attachments empty + no reviewer + no timestamps), D2 (open review note rn_564e65ce0d594f) |
| "how the period subledger runs sit underneath the support trail" | OE 14 (list_subledger_feed_runs); OE 15 (get_subledger_feed_run) | D1 (feed run finding), C4 (memo body) |
| "The vault memo needs to be complete, not a paraphrase of what Anaya remembers" | OE 25 (records_vault_upload_document) | W4 (RV upload), C4 (memo body covers feed run finding) |
| "stage the recognition entry for the $147,825 across the three service lines so it is queued for Daniel's review through the normal close path" | OE 13 (fiscal period open); OE 16 (JE surface sanity); OE 17 (account 119000 role on brookfield); OE 22 (create + submit JE) | W1 (JE stage + submit), C1 (JE business justification) |
| "Update the reconciliation and exception dispositions to accept-timing per Hannah, leaving the underlying exception trail referenced as-is for now" | OE 23 (blackline_update_reconciliation_variances on BL-75810CD0FEE4); OE 24 (blackline_update_exception on exc_1ddfc978ce5a4d, no resolve) | W2 (recon update), C2 (recon content), W3 (exception update — state stays investigating), C3 (exception content) |
| "Drop a brief note in the close coordination channel on the thread we already have running" | OE 11 (slack_conversations_search + replies on f936a11a46b05e0e9e16fdfac02bf8e4); OE 26 (slack_conversations_add_message on C005 thread_ts 1780248600.000000) | W5 (Slack reply on existing thread), C5 (Slack content) |
| "reply to Andrea with the recognition status and confirmation that the residual is parked per her instruction" | OE 27 (email_reply_to_email on email_scen_059_wip_recognition_0000 with Margaret in cc) | W6 (email reply), C6a (147,825 staged for Daniel), C6b (residual parked + accept-timing per Hannah) |
| "File the supporting memo and stage schedule in the vault under the right firm classification and retention, with the engagement-stage backup attached" | OE 18 (rv_list_documents — find doc_42c851aed8fb40ab); OE 19 (rv access grant + get + download); OE 20 (rv_list_retention_policies — confirm AICPA_SQMS_7Y); OE 25 (rv_upload_document with restricted + AICPA_SQMS_7Y, related to staged JE) | W4 (RV upload classification + retention + JE link), C4 (memo body) |
| "Close the open reminder on the orphan exception once the disposition is updated" | OE 21 (reminder_get_all_reminders — find reminder_scen_010_orphan_exception_0000); OE 28 (reminder_delete_reminder) | W7 (reminder delete) |
| "set a fresh follow-up for the FP-2026-06 BD3 revisit Hannah called for so it does not slip next month" | OE 13 (fiscal period FP-2026-06 BD3 anchor 2026-07-03); OE 29 (reminder_add_reminder with due ~2026-07-03 referencing Hannah's accept-timing approval) | W8 (reminder add) |
| "If anything in what you pull together changes the read on this before I take it to Daniel, say so plainly. I would rather hear it from you before the package moves than from Andrea after" | OE 14 (subledger feed run record); OE 15 (subledger feed run row read); OE 30(e) (final disclosure: feed run finding flagged as the read change); OE 27 (email reply surfaces it) | D1 (final response feed run flag), C6c (Andrea email surfaces feed run flag), C4 (memo body covers feed run finding) |

## Hardness lever coverage

| Lever | Hardness_Plan reference | OE step(s) | Rubric(s) — value can only be produced by traversing the lever |
|---|---|---|---|
| L1 Latching | Hardness_Plan ll. 18–22 (partial-feed narrative repeated across recon + doppelganger + email + Slack + DM + prior recommendation) | OE 4, OE 5, OE 10, OE 11, OE 12 (latching atoms); OE 14, OE 15 (falsifier) | D1, C4, C6c — value (feed run success / 2083 / 2083 / 0 contradicts the latching story) is producible only by breaking the latch and querying the structured feed run record |
| L2 Structured-DB skip (primary `ogl_subledger_feed_runs`) | Hardness_Plan ll. 23–26 | OE 14, OE 15 | D1, C4, C6c — `run_e33ed2561f2c46` + 2083/2083/0 atom is reachable only through the structured feed-runs surface |
| L2 Structured-DB skip (secondary `blackline_review_notes`) | Hardness_Plan ll. 26–28 | OE 7 | D2 — `rn_564e65ce0d594f` + Edith Banda FX-revaluation question + past 2026-06-02 SLA is reachable only through `blackline_list_review_notes`; no conversational artifact mentions this review note by ID |
| L6 Near-miss entity confusion (doppelganger) | Hardness_Plan ll. 31–34 (BL-75810CD0FEE4 vs blackline_bdbbea5db590 share entity/period/account/preparer/variance) | OE 3, OE 4, OE 5 | D3, W1 (account 119000 on brookfield role check via OE 17) — D3 forces the duplicate-scaffold identification and blocks the failure mode of aggregating to $8,781.24 or substituting the doppelganger |
| L8 Multi-link chain (Andrea email → BL recon → subledger feed → exception + Hannah reply → JE staging) | Hardness_Plan ll. 35–38 | OE 2 → OE 3–7 → OE 14–15 → OE 8–10 → OE 22–29 | W1 + C1 (JE end of chain), C2 + C3 (disposition wording draws from Hannah's reply), D1 + C4 + C6c (chain output: feed-run finding) — chain spans 6+ write families |
| L9 Universe-grounded gotcha | Hardness_Plan ll. 41–46 (restricted doc + account-role asymmetry + open period + retention codes) | OE 13 (open period), OE 17 (account 119000 on brookfield only), OE 18–20 (RV grant + retention enumeration), OE 25 (upload) | W4 — classification=restricted (mirroring doc_42c851aed8fb40ab) and retention from the four-code closed set (AICPA_SQMS_7Y / IRS_TAX_7Y / FIRM_INTERNAL / INDEFINITE) block invented codes like SOX_7Y; W1 — debit to account 119000 on brookfield blocks the entity-role trap with northstar_legal / acme_cloud |

All 5 selected levers (plus L2 secondary surface) have at least one Outcome rubric whose value cannot be produced without traversing the lever.

## No-gaps check

Every prompt ask above maps to at least one rubric. No prompt sentence is dropped.

## No-surplus check

Every rubric ties back to at least one prompt ask. Spot check:

| Rubric | Anchor prompt ask |
|---|---|
| W1, C1 | "stage the recognition entry for the $147,825 across the three service lines" + "memo can stand on its own" (business justification anchors JE to the audit trail) |
| W2, C2 | "Update the reconciliation ... dispositions to accept-timing per Hannah" |
| W3, C3 | "Update the ... exception dispositions to accept-timing per Hannah, leaving the underlying exception trail referenced as-is" |
| W4 | "File the supporting memo ... in the vault under the right firm classification and retention" |
| C4 | "memo needs to be complete, not a paraphrase" + "If anything ... changes the read" |
| W5, C5 | "Drop a brief note in the close coordination channel on the thread we already have running" |
| W6, C6a, C6b | "reply to Andrea with the recognition status and confirmation that the residual is parked" |
| C6c | "If anything in what you pull together changes the read on this before I take it to Daniel, say so plainly. I would rather hear it from you before the package moves than from Andrea after" (the read change goes BOTH to George — D1 — AND to Andrea — C6c) |
| W7 | "Close the open reminder on the orphan exception once the disposition is updated" |
| W8 | "set a fresh follow-up for the FP-2026-06 BD3 revisit Hannah called for" |
| D1 | "how the period subledger runs sit underneath the support trail" + escape-valve clause |
| D2 | "anything else opened or reviewed against it that I have not seen including any open reviewer notes" |
| D3 | "walk the reconciliation end to end" (the doppelganger record is part of the recon surface for FP-2026-05 / 119000) |
| D4 | "I want the actual state, the evidence attached" |

Zero surplus.

## Density alignment

| Source | Strict midpoint |
|---|---|
| Hardness_Plan projection | 51.0 |
| Council B-B3 projection | ~50 |
| AUDIT LENS 4 strict midpoint | ~52 |
| 50+ STRICT bar | met (≥+2 margin) |
| 40 PASS floor | met (≥+10 margin) |

Rubric set aligns with a trajectory producing 50+ tool calls on average across 6 Opus 4.8 runs.

## Verdict roll-up

- Validator: **PASS** (0 fails / 0 warns / 2 informational notes)
- Council A (Grounding): **GO** — every concrete value in rubric titles grounded verbatim in `_aux/Universe_Split/`
- Council B (Adversarial QC): **GO** — 8/8 sub-dims at 5/5, density ~50, all 5 levers covered, zero Major/Moderate adversarial hits
- Strict Veteran AUDIT (rubrics): **PASS (STRICT)** — strict midpoint ~52, zero answer-leakage on derived figures, all 5 levers + L2 secondary trace end-to-end, zero entity drift, zero silent process rubrics, zero tool-name leaks, voice consistent with V3 Task14 reference

S3 exit criteria fully met.
