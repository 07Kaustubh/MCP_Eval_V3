# Council A — Grounding and Convention Report v2 (S1.5 / Prompt revision)

Task: `24_6a36e84723508b4e3f391cfc`
Deliverable: `5_Prompt.txt` (revised after linter pushback)
Universe today: 2026-06-12 (US/Eastern)
Verdict: **GO** (zero BLOCKers)

## Context for v2

The platform linter flagged the v1 prompt as a persona mismatch: Lena Park is a Procurement Officer, deliberately separated from AP per segregation-of-duties controls per her PersonaBrief, so she should not OWN AP-queue triage. The v2 revision reframes Lena as the procurement-seat triage hand-off — vendors reach her because procurement owns the vendor relationship, she filters inbound to what procurement can answer cleanly (SOW currency, change-order coverage, engagement-scope in the vault), then explicitly hands off the AP-side disposition to Priya / Daniel / Steven. All 5 Hardness levers are preserved. This v2 scope is restricted to the revision delta — items already passed in v1 are not re-walked.

## A1 — Grounding sweep (revision delta)

| # | Claim in revised prompt | Status | Evidence (file : record-id / location) |
|---|---|---|---|
| 1 | "Priya" handoff target = Priya Khatri (AP Coordinator) | GROUNDED | (a) `Fact_Ledger.json` emails[] contains `priya.khatri@brookfieldcpas.com` — confirms the contact record exists. (b) `Brookfield_Base_Universe/2_Persona_Briefs.md` ~L287: "**Priya Khatri — AP Coordinator** *(new in v47)*" full persona block including "She owns invoice intake routing, vendor master accuracy, and the weekly AP exceptions triage" and "Daniel Jones above her on AP escalation triage" and "Lena Park is her procurement-side counterpart on PO/SOW questions" and "Recent activity: SAP Subledger AP invoice updates; Slack in `#vendor-bills-and-ap`". Priya is explicitly the natural handoff target FROM Lena's procurement seat INTO the AP queue — exact pattern the v2 prompt invokes. |
| 2 | Lena's brief explicitly authorizes the email-to-Daniel escalation when procurement crosses into AP-disposition territory | GROUNDED | `Brookfield_Base_Universe/2_Persona_Briefs.md` ~L540 Lena Park section, "Key relationships:" line: verbatim **"Daniel Jones when an escalation crosses procurement into AP-disposition territory"**. Exact authorization for the v2 email-draft-to-Daniel write action. |
| 3 | Lena's "Recent activity" supports vault scope-doc checks and the C010 payables-channel post | GROUNDED | `Brookfield_Base_Universe/2_Persona_Briefs.md` ~L540 Lena Park "Recent activity:" line: verbatim **"Records Vault vendor SOWs and PO packets; Slack in `#vendor-bills-and-ap`; vendor-side coordination via messaging."** Both write-surface anchors (vault read + C010 post) are explicitly in-scope per her brief. |
| 4 | Acme engagement evolved through an addendum + change order (procurement-side SOW lifecycle, multi-doc check) | GROUNDED | Per v1 Council A report `prompt_A_grounding.md` row 12 (already verified): `records_vault.rv_documents.json` carries `doc_eb7cb30c59bd4f03` kind=`engagement_letter_addendum` entity=acme_cloud title="Acme Cloud FY2026 Engagement Letter Addendum #1 - Scope Expansion (Multi-State Sales Tax + AR-Aging Bucket)" classification=restricted; and `doc_2d85ac5a698745c5` kind=`engagement_change_order` entity=acme_cloud title="Acme Cloud FY2026 Change Order - Multi-State Sales Tax & AR-Aging Bucket Scope Expansion" classification=restricted. SOW-lifecycle ownership maps to Lena per brief ("PO issuance, vendor onboarding diligence, and the SOW lifecycle"). |
| 5 | Rest of prompt's atoms still grounded (entities, Linear orphan-approver ticket, restricted classification, 210000/219000 split, Owen Mercer / Daniel Jones email escalations, three-entity AP scope, Northstar engagement letter) | GROUNDED (carry-over from v1) | All 16 substantive claim rows from `prompt_A_grounding.md` v1 remain unchanged in v2: 15 grounded, 1 plantable in S2 (the Daniel-Jones "patched last sprint" Slack thread reply, which has strong precedent in `slack.slack_messages.json` Daniel Jones C010 post `ts=1779204300.000000` "orphan-approver routing after the July 2025 departure"). v2 wording on this point — "Daniel posted in the payables channel a couple of weeks back that the routing rule for departed approvers was patched last sprint" — is unchanged from v1 and remains plantable, no v2 regression. |

**Revision-delta grounding result: 5 / 5 GROUNDED. Zero NOT FOUND. Zero new ungrounded atoms introduced by the revision.**

## A2 — Convention sweep (persona consistency, revision focus)

| # | Check | Status | Evidence in revised prompt |
|---|---|---|---|
| 1 | Voice matches Procurement Officer register (formal, SOW-aware, procurement/AP separation-conscious) — NOT AP Coordinator (queue-fluent, exception-routing-fluent) | PASS | Opening: "Vendors have been calling me since Monday about outstanding payments... They reach me because procurement owns the relationship, but the queue itself is on the AP side and that is not my call." Procurement-side vocabulary throughout: "stale or superseded SOW", "missing change order", "out-of-scope line", "active vendor dispute" — all procurement-relationship and SOW-lifecycle framings. No AP-queue-internal phrasing like "approval workflow", "GR/IR", "three-way match", or "exception triage queue". Brief: "Highly formal, organized, and procurement-aware. She communicates with the structured precision of a procurement function — references specific PO numbers, SOW versions, and contract dates, and keeps procurement and AP responsibilities cleanly separated." Match is on-point. |
| 2 | All four write actions described as procurement-seat outputs (cross-team handoff, escalation upward, procurement-side input to an AP ticket) rather than as the persona OWNING the AP queue | PASS | Write 1 (Slack): "post a summary in the payables channel **for Priya and the AP folks** with the per-vendor read and **which side owns each one**" — explicitly framed as handoff input, not queue ownership. Write 2 (Linear): "Drop a comment on the open AP-routing orphan-approver ticket **with the procurement-side evidence so the AP team has it when they work the ticket**" — explicitly "procurement-side evidence" + AP team owns the work. Write 3 (Email): "Draft an email to Daniel with Steven on copy on the vendors that need **partner sign-off for release**" — upward escalation for partner disposition, not Lena's own approval. Write 4 (Reminder): "set **me** a reminder to re-check in seven days" — personal follow-up, not an AP-queue mutation. |
| 3 | Prompt explicitly acknowledges SoD ("not approving or routing", "AP side is not my call", "Priya / Daniel / Steven own that call") | PASS | Three explicit SoD beats: (a) "the queue itself is on the AP side and that is not my call" (opening), (b) "The first three are procurement's problem to fix. The last two are AP's" (mid-prompt role separation), (c) "I am not approving or routing; Priya, Daniel, and Steven own that call" (closing line). This is exactly the linter's stated requirement and directly mirrors the brief's "Deliberately separated from AP per segregation-of-duties controls" sentence. |
| 4 | Four writes still mandated (payables-channel summary FOR Priya, Linear comment WITH procurement evidence, email to Daniel cc Steven, reminder) | PASS | All four present in the closing paragraph, all four naturally surface-named (no tool-name leakage). Counted: Slack post (1) + Linear comment (1) + email draft to Daniel cc Steven (1) + reminder (1) = 4. Matches Hardness Plan L7 mandate. |
| 5 | All 5 Hardness levers still surfaced after revision | PASS | **L1 Daniel-Jones dismissal**: "Daniel posted in the payables channel a couple of weeks back that the routing rule for departed approvers was patched last sprint. The procurement picture won't tell me whether that held, but if the invoices we are still sitting on were dated after that patch, the routing issue is alive on the AP side and Priya needs that signal." Reconciliation pressure intact, and now framed as a signal Lena PASSES TO Priya (consistent with the procurement-seat reframe). **L2 RV multi-doc-kind scope**: "For Acme, the original engagement evolved through an addendum and at least one change order, so we have multiple documents to check, not a single letter. For Northstar the engagement letter itself should be cleaner." Multi-kind sweep intact. **L7 4-write**: see row 4. **L8 per-vendor 3-link**: "Cross-check the active engagement records in the vault, the open AP exception ticket on the issues board, and any partner sign-off or void-and-rebill threads in email from Owen or Daniel." Three-link chain (vault + Linear + email) intact per vendor. **L9 restricted + account split**: "If a record is marked restricted and you can't get to it without an access grant, say so plainly, don't call it missing." + "Stay on external-vendor activity; employee reimbursements run through a different account family and are not ours." Both halves of L9 intact. |

**Persona-consistency result: 5 / 5 PASS. Linter's SoD concern is directly and explicitly addressed without sacrificing any Hardness lever.**

## Carry-over convention checks (unchanged from v1)

These passed in v1 and the revision did not introduce regressions — quick re-check:

| Rule | Status | Note |
|---|---|---|
| 500-word cap | PASS | Revised body fits within cap; no inflation from the SoD reframing (linter would have flagged) |
| No em-dash / en-dash | PASS | Zero occurrences in revised text |
| No tool names | PASS | "the payables channel" / "the vault" / "the open AP-routing orphan-approver ticket" / "email" — all natural-surface references |
| No internal IDs (apinv_, VEN-, issue_, doc_) | PASS | Zero ID leaks |
| No pre-solving | PASS | Root-cause CLASSES named (stale SOW, missing change order, out-of-scope, vendor dispute, missing credit memo, orphan approval chain), but no vendor-to-class mapping and no answer numbers |
| First-person natural voice, mid-thought entry, asymmetric knowledge | PASS | "Vendors have been calling me since Monday... at least two or three now"; "Before I push this to Priya or Daniel, I want to know what procurement can answer cleanly so I'm not adding noise to their backlog" — mid-thought, asymmetric, register-correct |

## Verdict

**GO.**

- The persona-mismatch concern from the platform linter is addressed at three explicit beats ("queue itself is on the AP side and that is not my call" / "first three are procurement's problem to fix, last two are AP's" / "I am not approving or routing; Priya, Daniel, and Steven own that call") and the framing throughout is procurement-seat triage-and-handoff, not AP-queue ownership.
- All 5 Hardness levers (L1 Daniel-Jones dismissal, L2 RV multi-doc-kind scope, L7 4-write, L8 per-vendor 3-link, L9 restricted + account split) are preserved verbatim or with equivalent surface strength.
- Both new persona handoff anchors (Priya Khatri as AP-side handoff target, Daniel Jones as cross-into-AP-disposition escalation per Lena's brief) are explicitly grounded in `Brookfield_Base_Universe/2_Persona_Briefs.md`.
- Zero new ungrounded atoms; zero convention regressions; the prior v1 Council A grounding sweep carries over cleanly.

No revisions required before S2 OE drafting. S2 plant note from v1 (Daniel Jones "patched last sprint" as a C010 thread reply under the existing 2026-05-19 "orphan-approver routing after the July 2025 departure" parent) remains in force.
