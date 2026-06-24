# Council A — Grounding and Convention
## Phase: S1 (Prompt) | Task: 26_6a390e724c34487b95645dcc

## A1 — Grounding sweep (claim → evidence)

| # | Claim in prompt | Verification | Status |
|---|---|---|---|
| 1 | "Hannah just messaged that William cleared the Step 3 partner package for the Northstar Legal FY2025 return last night, including the state-and-local accrual piece" | `email.emails.json`:`email_scen_068_northstar_annual_corp_tax_0006` (Hannah → William, 2026-06-11T13:30Z, "Northstar Legal FY2025 Step 3 partner sign-off request", names the SALT accrual shortfall as the open item) and `email_scen_068_northstar_annual_corp_tax_0008` (William → Hannah, 2026-06-11T20:45Z, reply approving SALT late-post and e-file path). Both timestamps land on "last night" relative to universe today 2026-06-12. | GROUNDED |
| 2 | "the trial balance we locked in our December period for Northstar" | `oracle_gl.ogl_fiscal_periods.json`:`northstar_legal_FP-2025-12` `status`=closed, `locked_at`=2026-01-05T12:36:07-05:00, `locked_by`=julia.vance@brookfieldcpas.com | GROUNDED |
| 3 | "the SALT shortfall that surfaced in review when Hannah re-tested the provision against year-end estimated payments" | `email.emails.json`:`email_scen_068_..._0006` Hannah's body: "the SALT accrual shortfall identified in review. Based on account 230000 versus year-end state estimated payments..." | GROUNDED |
| 4 | "William's reply is the authorization of record we needed for a closed-period booking" | `email.emails.json`:`email_scen_068_..._0008` William's body: "Please treat this reply as my authorization of record for the closed-period late-post to northstar_legal FP-2025-12" | GROUNDED |
| 5 | "The May timing recon I sent Daniel for sign-off on June 1 went past its deadline" | `email.emails.json`:`email_scen_012_orphan_exception_0006` (Tom → Daniel, 2026-06-01T13:31Z, "Approval request to dismiss exc_652c0931bb2546 under materiality"). `blackline.blackline_exceptions.json`:`exc_652c0931bb2546` `sla_due_at`=2026-06-02T16:14:41-04:00 (already past universe today 2026-06-12), `approver`=daniel.jones, `assigned_to`=tom.chang, `related_period_id`=`brookfield_FP-2026-05` (May), `state`=awaiting_approval. | GROUNDED |
| 6 | "Jones and I had landed on dismissing under materiality" | `email_scen_012_..._0006` Tom's body: "Jones Harrison confirmed... either accept-timing or dismiss-under-materiality would be reasonable, but leaned toward dismissing it instead of sweeping it next period." `exc_652c0931bb2546` `identified_by`=jones.harrison. | GROUNDED |
| 7 | "the stale tickler that keeps firing on the Brookfield intercompany variance from last summer. That item closed in August" | `blackline.blackline_exceptions.json`:`exc_151b0bee7e374e` `entity_id`=brookfield, `related_account_id`=110000, `related_period_id`=`brookfield_FP-2025-07`, `root_cause`="Intercompany clearing journal didn't sweep on schedule.", `state`=closed, `resolution_executed_at`=2025-08-06T04:59:16-04:00, `sla_due_at`=2025-08-06T15:59:16-04:00 | GROUNDED |
| 8 | "partner-level confirmation back in March that the reminder was fine to dismiss" | `email.emails.json`:`email_scen_001_orphan_exception_0006` (James Randall → Tom, 2026-03-16T12:42Z): "You can dismiss the stale SLA reminder and keep this as the audit trail that the item remains closed." James Randall is the `approver` on the exception record. `email_scen_001_orphan_exception_0007` (Matthew Li → Tom, 2026-03-16T18:30Z): "You're fine to dismiss the reminder on exc_151b0bee7e374e. The August closure is on solid ground, and James Randall's sign-off gives us the audit trail..." | GROUNDED |
| 9 | "the underlying polling bug behind these stale ticklers" | `email_scen_001_..._0007` Matthew Li: "What is not fine is seeing three stale ticklers in one quarter. Please push the polling-bug ops ticket up the priority list, attach Hannah's running occurrence log, and copy me on the follow-up..." | GROUNDED |
| 10 | "the tax channel" | `slack.slack_channels.json`:`C006` `name`=tax-prep-and-filings, `purpose`="Return preparation, extension tracking, filing deadlines, and client tax document follow-up", 41 members. Tom is a member. Only tax-named channel in the universe. | GROUNDED |
| 11 | Persona = Tom Chang, Tax Associate | `PersonaBrief.txt` header: "Tom Chang — Tax Associate ... Approachable, fairly concise, and moderately formal" | GROUNDED |
| 12 | Recipients (Hannah, William, Jones, Daniel, Matthew, James, Brookfield, Northstar) all resolve | `contacts.contacts.json` confirms: Hannah Grant, William White, Jones Harrison, Daniel Jones, Matthew Li, James Randall, Tom Chang — all `@brookfieldcpas.com` and present. Entities `brookfield` and `northstar_legal` confirmed across `ogl_fiscal_periods`, `blackline_exceptions`, `ogl_accounts`. | GROUNDED |

**A1 result: 12 / 12 grounded, 0 ungrounded.**

## A2 — Convention sweep

| Check | Observation | Status |
|---|---|---|
| 500-word cap | 398 words (per `wc -w`). Under cap. V3 references: Task11=180, Task12=267, Task13=270, Task14=371. We are slightly above the high-end of the V3 cohort but the additional length carries one more lever-bearing strand (the polling-bug ops follow-up); cuts here would weaken Lever 9 / Lever 10 traps. | PASS |
| Em-dash / en-dash | `—`=0, `–`=0 (re-counted). Triple-hyphen=False; double-hyphen=False. | PASS |
| Tool names in body | No `email_send_email`, `linear_create_issue`, `oracle_gl_*`, `records_vault_*`, `slack_post_*`, `blackline_*` strings. Surfaces named naturally: "messaged", "reply", "vault", "tax channel", "open ops ticket". | PASS |
| MCP-server names | No "Oracle GL MCP", "Records Vault MCP", "Linear MCP", "BlackLine MCP". | PASS |
| Internal IDs | No `exc_*`, `BL-*`, `doc_*`, `email_scen_*`, `JE-*`, `persona_*`, `FP-2025-12`, `C006`, no raw account numbers (`230000`, `530000`, `110000`, `260000`, `103000`). All references go through natural-language anchors ("the December period for Northstar", "the May timing recon", "the Brookfield intercompany variance from last summer"). | PASS |
| Pre-solving — SALT figure | `$4,820.30` does not appear in the prompt. The prompt explicitly directs the agent to derive the figure ("I want the shortfall traced back through our own records on the Northstar side so the number we book is one we can ourselves stand behind, not one we copied off the messaging trail"). | PASS |
| Pre-solving — Records Vault "Signed/E-Filed" upload | No mention. The prompt says "File a short support memo to the vault under the restricted classification with our long tax-return retention" — does NOT acknowledge the existing-output anchor (doc_8f821bbad10c4eb4) per Hardness_Plan L25. | PASS |
| Pre-solving — exception disposition | Prompt frames Tom's belief as "dismissing under materiality" and asks agent to "push it through". Does NOT reveal that `proposed_resolution`="Reclassify to the correct cost center via standard 4-eyes approval" — preserves Lever 9 / L27 stump. | PASS |
| First-person persona voice (Tom Chang) | "Hannah just messaged...", "I want to get this actually put to bed...", "I want the shortfall traced back...", "I had partner-level confirmation back in March..." — first-person throughout. | PASS |
| Three loose movements | Movement 1 (Trigger): "Hannah just messaged that William cleared the Step 3 partner package... I want to get this actually put to bed..." Movement 2 (Context): "The federal return and the state returns both tie cleanly to the trial balance we locked... The thing still hanging was the SALT shortfall... William's reply is the authorization of record..." Movement 3 (Asks): "Once you have a figure the records support, stage..." through the closing Slack ping. Two further sub-asks (May timing recon, stale tickler) are woven into Movement 3 as same-morning queue cleanup, not bolted on — they share the "clear my queue before the day ends" frame and tie back to the same persona-credibility motif (the SALT figure he wants to "stand behind" mirrors the materiality call he wants "pushed through"). | PASS |
| Voice match to PersonaBrief | Tom is "approachable, fairly concise, and moderately formal... task-completion focused". Prompt voice: "put to bed", "shouldn't be sitting behind accrual housekeeping", "one we can ourselves stand behind", "stops sitting on me", "drop a confirmation". Working-style, moderately formal, action-oriented. Consistent with PersonaBrief. | PASS |
| Structural drift vs V3 samples (Task11..Task14) | All four V3 samples open mid-thought, name the trigger first, weave investigation+writes, end with a real downstream action. Our prompt does the same. Length is the only delta (398 vs 180-371) and remains under cap. No format drift detected. | PASS |

**A2 result: 0 convention drift on Major fields.**

## Verdict basis
- Grounding sweep: 12/12 grounded, 0 NOT FOUND.
- Convention sweep: 0 Major drifts.
- Anti-pre-solving: all three Hardness_Plan must-avoid anchors (SALT figure, Signed/E-Filed upload, reclass disposition) are absent from the prompt body.

VERDICT: GO
