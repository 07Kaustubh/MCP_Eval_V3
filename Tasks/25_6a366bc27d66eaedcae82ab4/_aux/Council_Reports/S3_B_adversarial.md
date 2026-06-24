# Council B — Adversarial QC — Rubrics
# Task: 25_6a366bc27d66eaedcae82ab4
# Date: 2026-06-22
# Status: GO

Rubric set scope: 20 rubrics, nested shape, all `outcome`. Sub-type distribution: 8 write actions (1.1), 8 content checks (1.2), 4 key-fact reports (2.1). Zero process.

## Sub-dim scoring table
| # | Sub-dim | Score (1–5) | Notes |
|---|---|---|---|
| 1 | Atomicity | 5 | Write/content cleanly split for JE (R1/R2), recon (R3/R4), exception (R5/R6), vault (R7/R8), Slack (R9/R10), email (R11/R12/R13/R14). R16 bundles reminder write + due date + content per V3 reminder convention (inventory: "due date / window when material"). Acceptable. |
| 2 | Self-Containment | 5 | Every email, ID, amount, period, account, classification, retention, thread ts, channel, date embedded in title. Judge needs no external lookup. |
| 3 | Completeness (vs prompt coverage) | 5 | Every prompt ask covered: investigation (R17/R18/R19/R20), JE stage (R1/R2), recon disposition (R3/R4), exception disposition (R5/R6), vault filing (R7/R8), Slack note (R9/R10), Andrea reply (R11–R14), reminder close + follow-up (R15/R16), escape-valve disclosure (R14/R17). |
| 4 | Flexibility | 5 | "(or similar)" applied to free-text content only. Strict on IDs/emails/dates/amounts. R1 evidence explicitly accepts 1 consolidated JE OR 3 split JEs. R16 accepts "on or around 2026-07-03". |
| 5 | Accuracy | 5 | Every concrete value cross-checked against OE 1–30: $147,825, $4,390.62, BL-75810CD0FEE4, exc_1ddfc978ce5a4d, blackline_bdbbea5db590, rn_564e65ce0d594f, reminder_scen_010_orphan_exception_0000, email_scen_059_wip_recognition_0000, run_e33ed2561f2c46, doc_42c851aed8fb40ab, C005 + 1780248600.000000, 2026-06-02 (Hannah), 2026-07-03 (BD3), brookfield_FP-2026-05, account 119000, AICPA_SQMS_7Y, restricted. All grounded. |
| 6 | Category Balance (outcome > process) | 5 | 20 outcome, 0 process. Matches V3 reference distribution. |
| 7 | Agent-Centric Phrasing | 5 | All 20 titles open with "The Agent" or "The Agent's". Verbs (stages, adds, updates, uploads, posts, sends, deletes, creates, reports, flags, identifies, covers, references, confirms, surfaces, notes, carries) all in the Strict inventory. No tool function names in titles; field names (`retention_policy_code`, `resolution_summary`, `resolution_executed_at`) appear without code-fencing, consistent with the inventory's "parameter names in code-fence style" prohibition. |
| 8 | Grounding-in-Universe | 5 | All values traceable to `_aux/Universe_Split/`. Hannah's 2026-06-02 reply, Edith's review note SLA 2026-06-02, FP-2026-06 bd3_lock_at 2026-07-03, doc_42c851aed8fb40ab classification restricted, run_e33ed2561f2c46 success/2083/2083/0 — all verified through OE references. |

## B-B1 alt-path findings
None. Each Outcome rubric admits the V3-reference flex pattern: R1 accepts 1 or 3 JE entries summing to $147,825; R7 accepts kind `journal_entry_support` or `memo`; R16 accepts ~2026-07-03 ± window; R20 reports BL state "(or similar)" rather than verbatim. No valid agent trajectory satisfies the prompt intent while failing a rubric for over-specificity.

## B-B2 reverse-coverage findings
None. Every rubric maps to an explicit prompt clause:
- R1/R2 ← "stage the recognition entry for the $147,825 across the three service lines"
- R3/R4/R5/R6 ← "Update the reconciliation and exception dispositions to accept-timing per Hannah, leaving the underlying exception trail referenced as-is for now"
- R7/R8 ← "File the supporting memo and stage schedule in the vault under the right firm classification and retention" + "memo needs to be complete, not a paraphrase of what Anaya remembers"
- R9/R10 ← "Drop a brief note in the close coordination channel on the thread we already have running"
- R11–R14 ← "reply to Andrea with the recognition status and confirmation that the residual is parked"
- R14/R17 ← "If anything in what you pull together changes the read on this before I take it to Daniel, say so plainly"
- R15/R16 ← "Close the open reminder on the orphan exception... set a fresh follow-up for the FP-2026-06 BD3 revisit"
- R18 ← "anything else opened or reviewed against it that I have not seen including any open reviewer notes"
- R19/R20 ← "walk the reconciliation end to end. I want the actual state, the evidence attached"

## B-B3 tool-call density projection
**Projected midpoint: ≈ 50 calls / run. PASS (floor 40).**

Breakdown (reads + writes that the rubric set effectively forces):
- Base discovery (contacts ×4, channels_list, fiscal_period): 6
- Email walk (search + scen_059 + scen_010_orphan_exception_0008 + scen_010_orphan_exception_0009): 4–5
- Recon walk (list + get canonical + get doppelganger + audit_trail + review_notes): 5–6
- Exception walk (list + get): 2
- Subledger feed (list_runs + get_run): 2
- Slack triage thread (search + replies): 2
- Messaging DM (search + get): 2
- JE surface sanity (list_journal_entries + get_account): 2
- Vault (list_documents + list_grants + get_document + download + list_retention): 4–5
- Reminders (get_all): 1
- Writes (create_je, submit_je, update_recon_variances, update_exception, upload_document, slack_add_message, reply_email, delete_reminder, add_reminder): 9
- Cross-service triangulation / latching reinforcement buffer: 5–8

Total midpoint ≈ 50; cross-checks the Hardness_Plan midpoint 51.0 / strict 52.5 within rounding. Every Outcome rubric anchors a specific read or write — no rubric is satisfiable by pure recall.

## B-B4 hardness lever coverage table
| Lever | Covering rubric ID | Why the value can only be produced by traversing the lever |
|---|---|---|
| L1 Latching | 10033d88 (R17 — Agent reports feed-run success/2083/2083 contradicts partial-feed narrative) | The "success / 2083 of 2083 / 0 rejected" claim and the explicit contradiction-flag against the partial-feed story can only be produced by querying `ogl_subledger_feed_runs` for the period — i.e., breaking the latch that the recon + Andrea email + Slack + DM + prior recommendation email all reinforce. |
| L2 Structured-DB skip (primary `ogl_subledger_feed_runs`) | 10033d88 (R17), ac93a531 (R8 — vault memo body covers run_e33ed2561f2c46), 0e49d120 (R14 — Andrea reply surfaces the same finding) | Only the structured feed-run record yields `run_e33ed2561f2c46` + 2083/2083 + 0 rejected. The triple-anchoring across final response + memo body + Andrea reply forces the agent to retrieve the structured record. |
| L2 Structured-DB skip (secondary `blackline_review_notes`) | 2640ecb4 (R18 — Agent flags rn_564e65ce0d594f as open past-SLA reviewer item) | The review note ID, Edith Banda as author, FX-revaluation question, and past 2026-06-02 SLA are surfaceable only via `blackline_list_review_notes` against the canonical recon — no conversational artifact mentions this note. |
| L6 Near-miss entity confusion | 576e29f5 (R19 — blackline_bdbbea5db590 is parallel scaffold of BL-75810CD0FEE4 on same incident, not a second variance) | Identifying the doppelganger as a duplicate scaffold (same period brookfield_FP-2026-05, account 119000, anaya.wallace preparer, $4,390.62 variance) requires listing recons for the period+account and comparing both records. R19 also blocks the failure mode of aggregating to $8,781.24 or substituting the doppelganger for the canonical anchor. |
| L8 Multi-link chain | 80d39aeb (R1 — JE staged), 1af03630 (R4 — recon update cites Hannah 2026-06-02 + BD3 + exc), 10033d88 (R17 — feed-run finding) | Producing the recon disposition wording requires walking A (Andrea email) → B (BL recon) → C (`ogl_subledger_feed_runs` verification) → D (`exc_1ddfc978ce5a4d` + Hannah reply email) → E (JE stage + recon/exception updates). Each rubric anchors a distinct hop. |
| L9 Universe-grounded gotcha | c2d08157 (R7 — restricted + AICPA_SQMS_7Y + JE link), 80d39aeb (R1 — debit to account 119000 on brookfield), 32b42ee4 (R20 — state of BL-75810CD0FEE4) | R7 forces classification=restricted (mirroring doc_42c851aed8fb40ab) and a valid retention code from the four-code closed set (AICPA_SQMS_7Y / IRS_TAX_7Y / FIRM_INTERNAL / INDEFINITE), blocking invented codes like SOX_7Y. R1 fixes the debit to 119000 on brookfield (avoiding the entity-role trap with northstar_legal/acme_cloud). R20 anchors the period as open (no late_post_authorization_id needed). |

All 5 selected levers covered with non-trivial rubric anchors.

## Atomicity findings
- R16 (reminder write) bundles reminder creation + due ~2026-07-03 + description content (Hannah Grant + FP-2026-06 BD3 + exc/recon refs). On-pattern with the Strict inventory's reminder-rubric note ("due date / window when material") and with V3 references; not a defect. **No action.**
- R1 (JE) bundles entry creation + total + 3 service-line credits + offsetting 119000 debit + submitted state. Coherent single write action; failure modes co-vary. **No action.**
- R3/R5 (recon/exception updates) bundle update action + "without further state progression" / "without resolving" guards. Both guards co-vary with the update call structure — the negative claim is what makes the rubric non-trivial. **No action.**

## Voice / convention findings
- All 20 titles match Strict_Convention_Inventory openings ("The Agent <verb> ..." or "The Agent's <artifact> <verb> ...").
- All verbs (stages, carries, adds, references, updates, uploads, covers, posts, notes, sends, confirms, surfaces, deletes, creates, reports, flags, identifies) are in the on-framework verb list per sub-type.
- "(or similar)" usage on R2, R4, R6, R8, R10, R12, R13, R14, R16, R17, R18, R19, R20 sits at end-of-title and modifies free-text phrasing only; strict IDs/emails/dates/amounts inside those titles remain exact-match. Consistent with V3 reference convention.
- No em-dashes, no en-dashes, no "at least N", no tool function names, no passive voice, no subjective terms ("enough", "professional", "thorough").
- Schema field references (`retention_policy_code`, `resolution_summary`, `resolution_executed_at`) appear as plain snake_case (not code-fenced); the inventory prohibits code-fenced parameter names only — acceptable as-is.

No convention drift.

## Final verdict
**GO.** All 8 applicable QC sub-dims at 5/5. Density midpoint ≈ 50 (≥ 40 floor; in-line with Hardness_Plan 51.0). All 5 hardness levers anchored with at least one Outcome rubric whose value cannot be produced without traversing the lever. Zero Major/Moderate adversarial hits. Process count 0. Voice consistent with Strict_Convention_Inventory and V3 reference set.
