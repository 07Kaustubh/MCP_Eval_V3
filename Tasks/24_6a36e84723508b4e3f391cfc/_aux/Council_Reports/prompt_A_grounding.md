# Council A — Grounding and Convention Report (S1 / Prompt)

Task: `24_6a36e84723508b4e3f391cfc`
Deliverable: `5_Prompt.txt` (478 words)
Universe today: 2026-06-12 (US/Eastern)
Verdict: **GO** (with one S2-plant NOTE, no BLOCKers)

## A1 — Grounding sweep (per-claim trace)

| # | Claim in prompt | Status | Evidence (file : record-id / index) |
|---|---|---|---|
| 1 | Persona "Daniel" = Daniel Jones | GROUNDED | `contacts.contacts.json` → first_name="Daniel" last_name="Jones" email=daniel.jones@brookfieldcpas.com |
| 2 | Persona "Steven" = Steven Perry | GROUNDED | `contacts.contacts.json` → Steven Perry, steven.perry@brookfieldcpas.com |
| 3 | Persona "Owen" = Owen Mercer | GROUNDED | `contacts.contacts.json` → Owen Mercer, owen.mercer@brookfieldcpas.com |
| 4 | "Three entities ... Brookfield, Northstar Legal, Acme Cloud" | GROUNDED | `sap_subledger.ap_invoices.json` row counts by entity: brookfield 375 / acme_cloud 348 / northstar_legal 264 (all three present) |
| 5 | "The payables channel" = `#vendor-bills-and-ap` (C010) | GROUNDED | `slack.slack_channels.json` → name="vendor-bills-and-ap" exists; per hardness plan = C010 (channel_id field renders blank in row_data view but channel name confirmed) |
| 6 | "Daniel said in the payables channel a couple of weeks back that the routing rule for departed approvers was patched last sprint" | NOTE (plantable in S2) | `slack.slack_messages.json` Daniel Jones (persona_002) has 15 C010 posts. Strong precedent post `ts=1779204300.000000` (≈ 2026-05-19): "Closing the loop here: apinv_5e09decd035d4443 was approved for release in full ... Root cause was orphan-approver routing after the July 2025 departure, so this was workflow plumbing rather than a bill dispute. Mateo owns the routin..." This authorizes the L9 dismissal lever. Exact wording "patched last sprint" is **plantable in S2 OEs as a Slack thread reply** to an existing C010 parent without contradicting prior data. NOT a BLOCK — flagged as expected S2 plant. |
| 7 | "Vendors calling about outstanding payments ... past 60 days ... 80+ critical" | GROUNDED | `sap_subledger.ap_invoices.json`: 320 pending_approval rows total; 320/320 have `approver=None`. Past-80d invoices include the three named chains (BeaconPay apinv_5e09decd035d4443 invoice_date=2026-03-03 = 101d; GraniteRack apinv_6131b7c637aa4b6e invoice_date=2026-03-07 = 97d; TimeLedger apinv_d3019cdcc6ed44b2 invoice_date=2026-03-05 = 99d), plus VEN-002 / VEN-009 at 227d due-age. > 0 records exist in both the 60d and 80d bands. |
| 8 | "Orphaned approval chain" root-cause class | GROUNDED | 320/320 pending_approval rows have `approver=None`. Daniel Jones C010 post explicitly: "Root cause was orphan-approver routing after the July 2025 departure". `linear.linear_issues.json` `issue_378874ffeb8f4cb0b0417021f2d3d647` "Fix AP routing rule for departed approvers and sweep orphaned pending approvals" |
| 9 | "Disputed deliverable" root-cause class | GROUNDED | `linear.linear_issues.json` `issue_e5abbb9af74642eeb10a93426b0bbaa2` "Verify GraniteRack AP void-and-rebill for VEN-012-753165 / apinv_6131b7c637aa4b6e"; `issue_45d50dfc34c74996a477309304270f26` "Track Pinecrest VEN-006-193120 dispute for invoice apinv_dff20c11abdc495c"; multiple Owen Mercer escalation emails |
| 10 | "Missing credit memo" root-cause class | GROUNDED | Daniel Jones C010 thread reply ts=1779196440: "release $17,825 now and hold $6,650.25 pending the credit memo resolution on VEN-010-514242" — credit-memo class explicitly named in-channel |
| 11 | "The open AP-routing orphan-approver ticket" | GROUNDED | `linear.linear_issues.json` `issue_378874ffeb8f4cb0b0417021f2d3d647` confirmed: title "Fix AP routing rule for departed approvers and sweep orphaned pending approvals", state=todo, priority=2 |
| 12 | "For Acme, the original engagement evolved through an addendum and at least one change order" | GROUNDED | `records_vault.rv_documents.json`: 1× kind=`engagement_letter_addendum` entity=acme_cloud title="Acme Cloud FY2026 Engagement Letter Addendum #1 - Scope Expansion (Multi-State Sales Tax + AR-Aging Bucket)" classification=restricted; 1× kind=`engagement_change_order` entity=acme_cloud title="Acme Cloud FY2026 Change Order - Multi-State Sales Tax & AR-Aging Bucket Scope Expansion" classification=restricted. **Confirmed**: NO `engagement_letter` exists for acme_cloud (prior R4 trap reversed — finding the addendum + change order is the correct path) |
| 13 | "For Northstar the engagement letter itself should be cleaner" | GROUNDED | `records_vault.rv_documents.json`: 1× kind=`engagement_letter` entity=northstar_legal title="Northstar Legal FY2026 Audit Engagement Letter - Executed 2026-05-11" classification=restricted |
| 14 | "If a record is marked restricted and you can't get to it without an access grant" | GROUNDED | All three engagement-scope docs above have `classification=restricted`. `records_vault.rv_access_grants.json` exists with 184 grants; **0 grants for Lena Park** — agent must report access constraint, not "missing". `rv_classifications.json` confirms restricted = `requires_elevated_role: true` |
| 15 | "External-vendor side ... vs employee-reimbursement side ... different account family" | GROUNDED | `oracle_gl.ogl_accounts.json` exposes account_number=210000 (external AP) and 219000 (employee reimb). Verified live in pending data: VEN-002 brookfield rows post to acct=210000; VEN-009 brookfield rows post to acct=219000 (these are the actual two account families on the same entity). The "don't conflate" instruction is grounded in the data split. |
| 16 | "Void-and-rebill request sitting in email from Owen or Daniel" | GROUNDED | `email.emails.json` from owen.mercer@brookfieldcpas.com: "Escalation: void-and-rebill recommendation for apinv_6131b7c637aa4b6e / VEN-012-753165", "Recommendation to release apinv_5e09decd035d4443 / VEN-033-86573", "Escalation on VEN-010-514242 for acme_cloud". From daniel.jones@brookfieldcpas.com: "Partner sign-off request: GraniteRack void-and-rebill for VEN-012-753165 ($39,090.56)", "Partner sign-off request: release of apinv_5e09decd035d4443 / VEN-033-86573", "Sign-off request: TimeLedger Nexus VEN-010-514242 / apinv_d3019cdcc6ed44b2" |

**Grounding result: 15 of 16 claims GROUNDED, 1 claim NOTE (S2-plantable with strong precedent). Zero ungrounded.**

## A2 — Convention sweep (Prompt_Format.md)

| Rule | Status | Note |
|---|---|---|
| 500-word cap | PASS | 478 words (22-word headroom) |
| No em-dash (`—`) | PASS | zero occurrences (validator already cleared) |
| No en-dash (`–`) | PASS | zero occurrences |
| No tool names | PASS | uses "the payables channel", "the vault", "email", "the issues side", "the open AP-routing orphan-approver ticket" — all natural surface references; no `email_send_email`, `linear_*`, `sap_*`, `records_vault_*`, etc. |
| No MCP-server names | PASS | none |
| No internal IDs | PASS | zero `apinv_`, `VEN-`, `issue_`, `doc_`, `exc_`, `BL-`, `JE-` ID leaks |
| No pre-solving | PASS | the three root-cause **classes** are named (orphan / disputed / missing credit memo) but the prompt explicitly asks the agent to classify per vendor; this is task framing, not a vendor-to-class mapping. No final numbers, no named culprit vendor, no "the answer is X". |
| First-person natural voice | PASS | "I've had vendors calling since Monday", "I'm now hearing it from at least two or three", "Before I take anything to Daniel or Steven", "I am not approving or routing anything myself" — mid-thought entry, asymmetric knowledge, mild frustration, Procurement Officer register matches PersonaBrief |
| One coherent situation (sentence-removal test) | PASS | three movements (trigger / context / asks) all advance the same pending-approval backlog triage; sentence-removal test confirms no bolt-on |
| Voice match vs V3 sample prompts (Task11, Task12, Task14) | PASS | comparable mid-thought entry, comparable asymmetric-knowledge framing, comparable defer-to-authority structure ("Daniel and Steven own that call") |
| Validator anti-pattern warns (clichés, over-signaling, generic urgency) | PASS | no QC clichés ("loop in", "go through everything and surface every", "CC our CEO"); no investigation over-signaling ("check our emails, slack, linear"); urgency framing is concrete ("vendors calling since Monday", "two or three of them") not generic ("keeping me up at night") |

**Convention result: PASS on all Major fields. Zero drift.**

## Verdict

**GO.**

- All 16 substantive claims either resolve to verified atoms in the per-task universe (15) or are labeled as S2-plantable with strong existing precedent (1 — the Daniel-Jones "patched last sprint" dismissal, which the Hardness Plan already commits to plant as a C010 thread reply via OE).
- Zero convention drift on Major fields (500-word cap, dashes, tool names, IDs, pre-solving, voice, coherence).
- Voice / register / structure match the three V3 reference prompts.

Recommendation to S2: when planting the Daniel Jones "routing rule was patched last sprint" line, attach as a **thread reply** under an existing C010 parent (per hardness plan + Learnings L12) and choose wording consistent with the existing 2026-05-19 "Closing the loop ... orphan-approver routing after the July 2025 departure" post so the dismissal reads as continuous with prior in-channel history. No prompt revision required.
