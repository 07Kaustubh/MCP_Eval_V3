# Council B — Adversarial QC + Density + Hardness Preservation — S2 Oracle Events

Task: Tasks/26_6a390e724c34487b95645dcc
Phase: oe (S2)
Deliverable: 6_Oracle_Events.txt (OE1–OE17)
Date: 2026-06-22

Five-lens read (Architect / Implementer / Red-team / Ground-truth / Integration). Findings combined as the union.

---

## [B1] QC sub-dim scoring (OE-applicable dims)

| Sub-Dim | Score | One-line reason |
|---|---|---|
| OE Completeness | 5 | All seven write actions (closed-period JE staging+submit+approve+post, restricted memo upload, audit-trail email, BlackLine reclass+resolve, orphan-reminder dismissal, Slack confirm, Linear find-or-create comment) are covered, each gated by the discovery OE(s) that make the value defensible (slack anchor → email authorization → fiscal-period lock check → GL triangulation → vault stub recon → orphan exception+approval chain reads → reminder lookup). No critical lookup is missing — recipient/channel/period/account/document/reminder/issue resolution all have explicit OE steps. |
| OE Accuracy | 5 | Every cited identifier ground-truths against `_aux/Universe_Split/`: `northstar_legal_FP-2025-12` (status=closed, locked_at=2026-01-05T12:36:07-05:00, locked_by=julia.vance, FY2025/Q4 — OE4); accounts 103000 Cash - Tax Reserve (debit, 2,320,660.31), 230000 Income Tax Payable (credit, 1,766,752.72), 530000 booked-account number per William's explicit authorization (OE5/OE7); `email_scen_068_*_0006`/`_0008` Hannah→William and William→Hannah with body verbatim "DR 530000 SALT expense and CR 230000 accrued SALT payable" and "$4,820.30" (OE2/OE3); `exc_652c0931bb2546` proposed_resolution = "Reclassify to the correct cost center via standard 4-eyes approval", state=awaiting_approval, $9.61, recon BL-1F548113B049, approver daniel.jones (OE10); `exc_151b0bee7e374e` state=closed, $647.97 on 110000, recon BL-2E691B2E18FA, resolution_executed_at 2025-08-06T04:59:16-04:00, approver james.randall (OE13); `email_scen_001_*_0006/0007` James + Matthew dismissal-and-polling-bug chain verbatim (OE14); reminders `reminder_scen_012_orphan_exception_0000` (due 2026-06-02T17:00:00+00:00, BL-1F548113B049, $9.61) and `reminder_scen_001_orphan_exception_0000` (due 2025-08-11T17:05:00+00:00) (OE12/OE15); slack ts=1781013600.100000 (persona_004 C006) and ts=1781119800.200000 (persona_027 C006) — both body verbatim incl. "$4,820.30" and "account 230000 versus year-end state estimated payments" (OE1); docs doc_8f821bbad10c4eb4 (107 bytes, restricted, IRS_TAX_7Y, 2026-06-12T09:30:00-04:00, persona_027) and doc_03f88abe3bb5482a (restricted, IRS_TAX_7Y, 2026-06-08T16:00:00-04:00) (OE6). Parameter conventions correct: slack `payload`, email `content`, vault `content_b64`, Linear `issueId`+`body`. |

Bar (5/5) met on every sub-dim.

---

## [B2] Adversarial alt-path

- Intended L9 stump (persona-says-dismiss vs BlackLine-says-reclassify on exc_652c0931bb2546): preserved cleanly. OE10 + OE12 force "Reclassify per `proposed_resolution`" with explicit override language. **Intended; not a defect.**
- Intended L25 stump (doc_8f821bbad10c4eb4 "Signed/E-Filed" stub vs unbooked SALT JE): preserved cleanly. OE6 explicitly concludes "the 'Signed/E-Filed' label is a forward-looking stub, the underlying SALT late-post JE has not yet been booked, and the prompt's intent is to actually stage and post the JE now." **Intended; not a defect.**
- No second-readable prompt framing that would flip an OE write action under the soft-instruction over-compliance failure mode: the OE list pins all six writes to specific values (JE id/entry_number propagated, vault `related_resource_id` bound to JE id, email cc list pinned, slack `payload` pinned to C006, BlackLine reclass route pinned to 4-eyes with named preparer/approver, reminder ids pinned, Linear find-or-create pinned).
- No adversarial divergence flagged.

---

## [B3] Tool-call density projection

Walking a competent Opus 4.8 trajectory through OE1–OE17 with realistic discovery hops:

| Block | Calls |
|---|---:|
| OE1 slack discovery (search_messages + conversations_replies on the C006 thread) | 2–3 |
| OE2 email search + get on William's authorization | 2 |
| OE3 email_get on Hannah's routing | 1 |
| OE4 oracle_gl_get_fiscal_period on `northstar_legal_FP-2025-12` | 1 |
| OE5 GL triangulation (list_accounts + 3× get_account + list_journal_entries on 230000 + get_account_balance on 230000 + list_journal_entries / sap_subledger_list_subledger_transactions on 103000) | 6–8 |
| OE6 vault discovery (list_documents tax_return + 2× get_document + optional download_document_content) | 3–4 |
| OE7 JE lifecycle (create_journal_entry + submit + approve + post, respecting 300s gates) | 4 |
| OE8 records_vault_upload_document for the SALT memo (content_b64, restricted, IRS_TAX_7Y, related_resource_id=JE id) | 1 |
| OE9 email confirmation (send_email or reply_to_email to Hannah + cc William) | 1 |
| OE10 blackline_get_exception + blackline_get_reconciliation | 2 |
| OE11 email_get_email_by_id on Tom→Daniel + email_get_thread (or email_search_emails) for no-reply confirm | 2 |
| OE12 blackline_update_exception + blackline_resolve_exception + reminder_get_all_reminders + reminder_delete_reminder | 4 |
| OE13 blackline_get_exception on the closed stale exception | 1 |
| OE14 email_search_emails + email_get_thread for scen_001 chain | 2 |
| OE15 reminder_get_all_reminders + reminder_delete_reminder for the stale tickler | 2 |
| OE16 linear_list_projects + linear_list_issues + (create_issue if find fails) + linear_create_comment | 3–4 |
| OE17 slack_channels_list (optional) + slack_conversations_add_message to C006 | 1–2 |
| Cross-service triangulation buffer (re-search of email threads, audit-trail confirms, BD3 horizon checks, contact lookup to confirm cc list, journal_entry_lines validation on the posted JE) | 4–6 |
| **Projected total** | **42–60** |
| **Midpoint** | **~51** |

Floor 40: **PASS**. Comfort 50: **PASS**. Aligns with Hardness Plan midpoint 52 and S1 Council B 54.

---

## [B4] Hardness preservation

| Lever | Triggered by | Verdict |
|---|---|---|
| Lever 1 Latching | OE1 surfaces Hannah's "data package is complete and Step 1 is signed off" + Tom's "tie cleanly to the closed FP-2025-12 TB" framing as anchors; OE2/OE3 reinforce William's "authorization of record" framing. Combined, these read as "close is done" before OE6 forces the vault-stub recognition. | PRESERVED |
| Lever 2 Structured-DB skip | OE5 explicitly forces "verify the SALT shortfall through Northstar's own GL rather than copying the figure off the slack chatter" — list_journal_entries on 230000 northstar FY2025 (in-period activity confirms zero — only the opening-balance JE exists) and walk 103000 outflows; OE7 binds the staged JE to William's email as `late_post_authorization_id`. | PRESERVED |
| Lever 8 Multi-link chain (A→B→C→D) | OE1 (slack anchor) → OE5 (GL absence + recomputation) → OE7 (closed-period JE staging with email-id binding) → OE8 (vault memo tied to JE id). All four hops are explicit, parameterized, and dependency-ordered. | PRESERVED |
| Lever 9 Universe-grounded gotcha | OE4 forces fiscal-period lock check (forces `late_post_authorization_id` requirement). OE10 forces independent read of exc_652c0931bb2546.proposed_resolution = "Reclassify" with explicit "the persona-relayed 'dismiss' framing must be overridden." OE11 reinforces the override with "absence of approver reply as further reason to fall back to the BlackLine record's documented proposed_resolution." | PRESERVED |
| Lever 10 Reversal / supersession (L25 anchor) | OE6 explicitly surfaces doc_8f821bbad10c4eb4 ("Signed/E-Filed" stub) with verified metadata and concludes "the 'Signed/E-Filed' label is a forward-looking stub, the underlying SALT late-post JE has not yet been booked, and the prompt's intent is to actually stage and post the JE now." Forces agent to override the existing-output anchor. | PRESERVED |

No HARDNESS_REGRESSION.

---

## [B5] Tool-leak / phrasing scan

| Check | Result |
|---|---|
| Em-dashes (—) | None found in OE1–OE17 |
| En-dashes (–) | None found |
| "at least N" without prompt mandate | None found |
| "approximately" near IDs/dates | None found |
| "(or similar)" near exact values | None — all "(or X)" patterns are tool alternatives in OE bodies (oracle_gl_get_account / email_reply_to_email / sap_subledger_list_subledger_transactions / reminder_get_due_reminders / email_search_emails) which are explicitly allowed in OE bodies per the format card |
| Tool names in OE titles | None — every OE summary leads with the action verb ("Search the…", "Pull William White's…", "Verify the…", "Inspect the…", "Create and post…", "Upload the…", "Notify…", "Read the disposition…", "Confirm Daniel did not reply…", "Resolve exc_…", "Confirm the older…", "Retrieve the March…", "Find and dismiss…", "Add the polling-bug…", "Confirm in the tax channel"). Tool names appear only in OE bodies, which is allowed |
| Parameter conventions | Slack `payload` ✓, email `content` ✓, vault `content_b64` ✓, Linear `issueId`+`body` ✓ |

No phrasing hits.

---

## [B6] Upstream propagation

No B6 PROPAGATE TO S1 flags raised.

**Polling-bug Linear find-or-create check:** I enumerated all 30 issues in `linear.linear_issues.json`. There is no dedicated "polling-bug" ticket; the closest active ops trackers are linear_d49cf721d655 (Retail PBC stale audit requests), linear_d8b80c5bad34 (Bank feed exception follow-up on exc_4d5d3582698946), and several "stale / orphan / blackline" AP-controls issues, none of which match the polling-bug operational tracker Matthew Li references. The S1 prompt design report explicitly allows find-or-create. OE16 encodes this cleanly:

> "If a dedicated polling-bug Linear issue exists, use linear_create_comment with parameters issueId set to that issue id and body recording …. If no exact polling-bug issue is found, use linear_create_issue under the closest active ops project to open the tracking ticket, then use linear_create_comment with issueId and body to record the same occurrence note, so Matthew Li's escalation ask is reflected in the running record."

The find-or-create branch is explicit, both arms are parameterized (issueId + body for comment, and create_issue scoped to "closest active ops project"), and the occurrence-note content is pinned to "this week's occurrence on exc_151b0bee7e374e, the March partner-level dismissal authorization chain (James Randall plus Matthew Li), and the disposal of reminder_scen_001_orphan_exception_0000." No contradiction with prompt framing, no implicit existence claim — the OE matches the universe state and the prompt design's explicit allowance.

**Observational note (not a defect; not a B6 flag):** Northstar's account 530000 chart-of-accounts name is "Court Filing & Expert Witness Costs" rather than "SALT expense." The OE faithfully encodes William White's authorization email which explicitly states "DR 530000 SALT expense and CR 230000 accrued SALT payable" — this is a within-universe contradiction (the email body labels 530000 as SALT expense while the chart name describes a litigation expense). The OE is correct to follow William's explicit account binding because (a) it is the authorization of record (b) northstar has no dedicated SALT expense account in its 5xxxxx chart (verified: 500000 Direct Engagement Costs, 510000 Salaries Direct, 519000 Partner Compensation, 520000–523000 software/research, 530000 Court Filing, 535000 CLE, 536000 Bar Dues, 540000 Travel, 550000 Lease, 551000 Facilities, 555000 Utilities, 560000 Liability Ins, 565000 Malpractice, 570000 Depreciation, 580000 Marketing, 590000 Bad Debt). No 5xxxxx tax-expense account exists; William's explicit binding is the only mapping available. This actually *strengthens* the L9 universe-grounded gotcha rather than weakening it. No fix needed.

---

## Verdict

- All applicable QC sub-dims at 5/5 ✓
- No adversarial divergence (intended L9 + L25 stumps preserved) ✓
- Projected tool calls 42–60, midpoint ~51 (≥40 floor, ≥50 comfort) ✓
- All 5 Hardness levers (1, 2, 8, 9, 10) still triggered ✓
- 0 phrasing hits ✓
- 0 PROPAGATE TO S1 flags ✓

VERDICT: GO
