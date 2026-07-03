# Council B — Adversarial QC (S2 OE)

## Verdict
**REVISE** — two narrow surgical edits to lock B3 density cleanly above 40 and one cosmetic precision fix. No blocking defects; not a clean GO.

## B1 QC scoring

- **OE Completeness: 5/5** — The 22 numbered steps cover every prompt ask. Discovery anchors (OE1-OE15) load all entities, services, surfaces, and precedent context. Writes (OE16-OE21) discharge all six explicit asks: Craig reply, David+Catalina email, airtable update, Slack post, Linear comment, Monday reminder. Implicit asks also covered: "what David+Catalina would need" (OE17 customer-side handoff), "mirror Mosaic structure" (OE12 + OE17), "operational lesson on Emilia" (3-surface capture at OE18/OE19/OE20), "Pam not on recipients" (OE17 explicit + OE22 consistency). OE22 is a final no-call consistency pass, which is the correct pattern.

- **OE Accuracy: 5/5** — Tool bindings are unambiguous and per-call parameters are correct:
  - email `content` (not `body`) — correct per MoveOps trap (OE16, OE17)
  - Slack `payload` (not `text`) — correct (OE19)
  - Linear `issueId + body` — correct (OE20)
  - airtable `base_id "appMoveOpsOps001" + table_id "tblRelocations01" + record_id "recEmiliaCruzChicagoDenver"` — all verified against `airtable.bases/tables/records.json`
  - calendar `start_datetime`/`end_datetime`/`attendees` — correct (OE21)
  - Slack `channel_id "C006"` — verified as `operations` in `slack.slack_channels.json`
  - email `email_id` atoms — all six verified PRESENT in `email.emails.json`
  - QB bill `id "BILL-KEYMOVE-2026-0417"` — verified: TotalAmt 1200, TxnDate 2026-04-17, DueDate 2026-04-24, AccountRef ACC-6185 "Claims & Remediation Expense", vendor VEND-KEYMOVE-001
  
  Minor cosmetic precision: OE4 narrates the account as "Claims **and** Remediation Expense"; actual is "Claims **&** Remediation Expense" (ampersand). This is narrative-only — agent will land on the correct atom regardless. Flag as informational, not a parameter error.

## B2 Second-reading

| OE | Advances prompt? | Tool+param binding | Universe support | Verdict |
|---|---|---|---|---|
| 1 | Yes (recipient resolution + David disambiguation vs d.kowalski@harbourpharma) | unambiguous, 6 distinct contact lookups | all 6 contacts present | PASS |
| 2 | Yes (anchors Slack lesson destination) | unambiguous | C006=operations verified | PASS |
| 3 | Yes (vendor-side anchor) | search OR get_bill — both valid | KM-44192-ICR verified | PASS |
| 4 | Yes (account framing supports L11 vendor-vs-customer) | unambiguous | ACC-6185 present (cosmetic name typo only) | PASS |
| 5 | Yes (L9 framing anchor + L1 $1,200 latch) | unambiguous | email_email_99e10a978b48 verified | PASS |
| 6 | Yes (L3 trailing question + Craig's Apr 11 chain origin) | unambiguous | email_email_1f1459bff84c verified | PASS |
| 7 | Yes (L8 chain Pam + Catalina commitments) | unambiguous, 3 named email_ids | all 3 verified | PASS |
| 8 | Yes (Alejandro precedent abstract goodwill credit — supports L11) | unambiguous | email_email_348c5411b36f verified | PASS |
| 9 | Yes (Linear retention destination + existing comment hygiene) | unambiguous | linear_issue_c8cdba4408f1 verified ("NorthWind retention response plan after April escalations", team_operations) | PASS |
| 10 | Yes (Airtable schema for L2 traversal) | unambiguous | 2 bases + 3 tables verified | PASS |
| 11 | Yes (L2 Emilia row pre-read for OE18 update) | search OR get_record — both valid | recEmiliaCruzChicagoDenver present, Special Requirements 768 chars w/ piano+Steinway content | PASS |
| 12 | Yes (Mosaic precedent — core L2 + L11 mechanism) | unambiguous | bill_mosaic_damage_accrual_001 present, DocNumber ACCRUAL-2026-0415-MOSAIC verified, $90K amount confirmed | PASS |
| 13 | Yes (NorthWind customer identity supports L11 credit-memo framing) | unambiguous (cust_northwind) | NorthWind Technologies verified | PASS |
| 14 | Yes (Catalina ownership + David cc anchor) | unambiguous | company_northwind in CRM | PASS |
| 15 | Confirmatory only — channel home was already established at OE2; this step is low-utility but not redundant (gathers any peer commentary worth referencing) | unambiguous | C006 + recent ops messages | MINOR — keep but acknowledge low marginal density value |
| 16 | Yes (Craig reply discharges L3 trailing-question hardness) | reply_to_email + email_id + content | email exists | PASS |
| 17 | Yes (two-sided handoff — the core L11 + L8 chain landing) | send_email + 2 recipients + content | recipients present | PASS |
| 18 | Yes (L2 structured-DB write — extend not overwrite) | airtable_update_records + base_id + table_id + records[] | record + field present | PASS |
| 19 | Yes (operational lesson on correct channel — L9 channel-lock-in gate) | conversations_add_message + channel_id "C006" + payload | C006 verified | PASS |
| 20 | Yes (existing Linear issue, operational scope only) | linear_create_comment + issueId + body | issue verified | PASS |
| 21 | Yes (Monday next-business-day reminder) | calendar_add_calendar_event + start/end + attendees | 2026-04-27 is Monday per fact-ledger | PASS |
| 22 | Yes (consistency pass, no new calls) | no-call self-check | n/a | PASS |

No decorative/redundant/hand-wavy steps. OE15 is the only soft mark — keep but recognise low marginal density contribution.

## B3 Density projection

| OE | Action | Min | Max | Mid |
|---|---|---|---|---|
| 1 | 6 × contacts_search_contacts | 6 | 6 | 6 |
| 2 | channels_list | 1 | 1 | 1 |
| 3 | search_bills + get_bill (or get alone) | 1 | 2 | 1.5 |
| 4 | search_accounts (single) | 1 | 1 | 1 |
| 5 | search_emails + get_email_by_id | 2 | 2 | 2 |
| 6 | search_emails + get_email_by_id | 2 | 2 | 2 |
| 7 | search_emails + 3 × get_email_by_id (Pam + Catalina×2) | 3 | 4 | 3.5 |
| 8 | search_emails + get_email_by_id | 2 | 2 | 2 |
| 9 | linear_get_issue + linear_list_comments | 2 | 2 | 2 |
| 10 | airtable_list_bases + list_tables | 2 | 2 | 2 |
| 11 | airtable_search_records or get_record | 1 | 2 | 1.5 |
| 12 | search_bills + get_bill | 2 | 2 | 2 |
| 13 | search_customers + get_customer (+ optional search_invoices) | 2 | 3 | 2.5 |
| 14 | search_companies + get_company (+ optional search_deals + list_engagements) | 2 | 4 | 3 |
| 15 | conversations_search_messages | 1 | 1 | 1 |
| 16 | reply_to_email | 1 | 1 | 1 |
| 17 | send_email | 1 | 1 | 1 |
| 18 | airtable_update_records | 1 | 1 | 1 |
| 19 | conversations_add_message (C006) | 1 | 1 | 1 |
| 20 | linear_create_comment | 1 | 1 | 1 |
| 21 | calendar_add_calendar_event | 1 | 1 | 1 |
| 22 | consistency pass (no calls) | 0 | 0 | 0 |
| **Total** |  | **35** | **42** | **38.5** |

**Verdict: THIN_DENSITY (borderline) — REVISE for cleaner margin.**

Pure-OE-as-written midpoint (38.5) sits below the v11/v12 40-call floor when "or call X directly" branches are weighted at 50/50 and OE13/OE14 invoice/deal/engagement reads are read as truly optional. Realistic agent behaviour (search-then-get on the OR branches, OE13/OE14 follow-throughs treated as required) lifts the midpoint to ~42, which is THIN-band acceptable per Hardness_Plan's carry-forward justification. But the floor is too close to BLOCKER for comfort.

**Surgical revision to lock B3 cleanly in THIN band (midpoint ~44):**

1. **OE13** — change "Optionally call `quickbooks_search_invoices`" to required. The customer-side credit-memo authority framing depends on understanding the open invoice surface; this should not be optional. (+0.5 mid)
2. **OE14** — change "Optionally call `crm_search_deals`" AND "`crm_list_engagements`" to required (both). The Catalina-ownership and active-retention-stream framing depends on both. (+1 mid)
3. **Consider adding** at OE17 prep: "re-fetch `email_email_99e10a978b48` and `bill_mosaic_damage_accrual_001`" as required-reads before composing the customer-side handoff — realistic agent behaviour, lifts density and reinforces L1+L2. (+2 mid if added)

With edits 1+2: midpoint locks at ~43-44. With edit 3 added: ~46. Either floors the OE deterministically above 40 and the carry-forward THIN-justification from Hardness_Plan remains intact.

## B4 Lever preservation

| Lever | OE exercise | Verdict |
|---|---|---|
| L1 Latching ($1,200 + Marcus L9 frame) | OE3 (bill TotalAmt 1200), OE5 (Marcus's L9 quote on `email_email_99e10a978b48`), OE6 (Craig's photo evidence aligns with rider), OE12 (Mosaic precedent shows the rider is one ledger line) | EXERCISED |
| L2 Structured-DB skip (Airtable + Mosaic bill) | OE10 (airtable schema), OE11 (Emilia row), OE12 (Mosaic bill precedent), OE18 (write to structured DB) | EXERCISED |
| L7 Multi-write diversification (6 writes / 5 services) | OE16 email-reply, OE17 email-send, OE18 airtable-update, OE19 slack-post, OE20 linear-comment, OE21 calendar-event = 6 writes across email + airtable + slack + linear + calendar (5 services) | EXERCISED |
| L8 Multi-link chain (Craig → Marcus → Pam → Linear → Catalina) | OE6 (Craig Apr 11) → OE5 (Marcus Apr 17 L9) → OE7 (Pam Apr 24 escalation + Catalina Apr 14 EOD commitment + Apr 13 backup) → OE9 (Linear retention issue) → OE17 (David+Catalina handoff = chain landing) | EXERCISED |
| L11 Net-vs-gross (vendor rider ≠ customer disposition) | OE3 (vendor line $1,200) + OE4 (Claims & Remediation account framing) + OE12 (Mosaic two-sided precedent) + OE13 (NorthWind customer credit-memo surface) + OE17 (explicit two-sided handoff in outbound email) | EXERCISED |

All 5 selected levers exercised. PASS.

## B5 Entity weave

| Entity | Universe role | Used in OE as | Verdict |
|---|---|---|---|
| Emilia Cruz | NorthWind client, `recEmiliaCruzChicagoDenver` damage subject | OE11/OE18 subject | CORRECT |
| NorthWind Technologies | client (CRM `company_northwind`, QB `cust_northwind`) | OE13/OE14/OE17 customer context | CORRECT |
| KeyMove Specialty Transport | vendor `VEND-KEYMOVE-001`, ICR rider | OE3/OE5/OE6/OE16 vendor-side anchor | CORRECT |
| Heartland Movers | vendor on Mosaic precedent bill | OE12 precedent vendor | CORRECT |
| Mosaic Robotics | precedent client (90K accrual) | OE12 precedent context | CORRECT |
| Marcus Thorne | Head of Finance, L9 dismissal author | OE5 source + OE17 reference | CORRECT |
| Catalina Dubois | Account Manager (NorthWind owner) | OE7/OE14/OE17 retention-package owner | CORRECT |
| David Chen | Customer Engagement Lead | OE1 explicit disambiguation vs d.kowalski@harbourpharma + OE17 recipient | CORRECT (disambiguation explicit) |
| Craig Nguyen | KeyMove Dispatch Manager | OE6/OE16 Apr 11 question + reply | CORRECT |
| Pam Kowalski | NorthWind escalation author | OE7 context only, OE17/OE22 explicit "not on recipients, no echo" | CORRECT (defensive handling) |
| Alejandro Fuentes | Financial Analyst (retention model draft) | OE8 precedent context | CORRECT |
| Chloe Vance | Operations Manager (Blessing's ask-source) | OE1 resolution | CORRECT |
| Blessing Okafor | Relocation Coordinator (PERSONA) | OE1/OE16/OE17/OE19/OE21 sender + actor | CORRECT |

No swaps, no near-miss confusions, no dropouts. The David / d.kowalski disambiguation at OE1 is a strong defensive move against the most plausible persona confusion. PASS.

## B6 Process-rubric propagation

No ordering constraint requires a Process rubric. Every write is verifiable by its final-state Outcome:
- OE16-OE21 are independent writes — none has a hard sequencing precondition the others can't satisfy by Outcome inspection.
- OE18 "extend not overwrite" is a final-state Outcome (Special Requirements contains both old content AND damage-disposition addendum).
- OE17 "Pam not cc'd, no escalation echo" is a final-state Outcome on the sent email.

**Zero Process rubrics needed.** PASS — consistent with all 4 V3 reference tasks (zero process rubrics). No PROPAGATE TO S3 flags.

## B7 Fabricated-ID detection

| Atom cited in OE | Source check | Verdict |
|---|---|---|
| `email_email_99e10a978b48` (Marcus Apr 17) | `email.emails.json` | PRESENT — subject+date verified |
| `email_email_1f1459bff84c` (Craig Apr 11) | `email.emails.json` | PRESENT — subject+date verified |
| `email_email_7168baed8438` (Pam Apr 24) | `email.emails.json` | PRESENT |
| `email_email_ab22f67eeeb0` (Catalina Apr 14) | `email.emails.json` | PRESENT |
| `email_email_ab99acca3399` (Catalina Apr 13) | `email.emails.json` | PRESENT |
| `email_email_348c5411b36f` (Alejandro Apr 16) | `email.emails.json` | PRESENT |
| `BILL-KEYMOVE-2026-0417` | `quickbooks.bills.json` | PRESENT — TotalAmt 1200, vendor VEND-KEYMOVE-001 verified |
| DocNumber `KM-44192-ICR` | `quickbooks.bills.json` | PRESENT |
| `bill_mosaic_damage_accrual_001` | `quickbooks.bills.json` | PRESENT — $90K Mosaic accrual verified |
| DocNumber `ACCRUAL-2026-0415-MOSAIC` | `quickbooks.bills.json` | PRESENT |
| `ACC-6185` (account) | `quickbooks.accounts.json` | PRESENT — name "Claims & Remediation Expense" (OE narrative uses "and", cosmetic typo) |
| `cust_northwind` | `quickbooks.customers.json` | PRESENT |
| `VEND-KEYMOVE-001` | derived from bill VendorRef | PRESENT |
| `appMoveOpsOps001` (airtable base) | `airtable.bases.json` | PRESENT |
| `tblRelocations01` / `tblStipends00001` / `tblClientAccts01` | `airtable.tables.json` | ALL PRESENT |
| `recEmiliaCruzChicagoDenver` | `airtable.records.json` | PRESENT — Special Requirements 768 chars w/ piano+Steinway content |
| `linear_issue_c8cdba4408f1` | `linear.linear_issues.json` | PRESENT — title "NorthWind retention response plan after April escalations", team_id `team_operations` |
| `team_operations` | `linear.linear_teams.json` | PRESENT |
| `mosaic_incident_report_final_001` | `email.emails.json` | PRESENT (cited in Hardness_Plan, referenced indirectly via OE12 Mosaic precedent context) |
| Slack `C006` (#operations) | `slack.slack_channels.json` | PRESENT — name verified "operations" |
| Slack `C002` (#customer-engagement), `C005` (#finance) | `slack.slack_channels.json` | PRESENT (cited as wrong-channel decoys) |
| Contact `moveops_blessing_okafor` | `contacts.contacts.json` | PRESENT |
| Contact `contacts_contact_d6172aa9e622` (Craig) | `contacts.contacts.json` | PRESENT |
| Contact `moveops_catalina_dubois` | `contacts.contacts.json` | PRESENT |
| Contact `moveops_chloe_vance` | `contacts.contacts.json` | PRESENT |
| Contact `contacts_contact_a0f5307e237d` (David Chen) | `contacts.contacts.json` | PRESENT |

**Zero fabricated atoms.** PASS.

Single cosmetic note (B7-cos): OE4 narrates the account name as "Claims **and** Remediation Expense" — actual is "Claims **&** Remediation Expense". Narrative-only; agent will hit the correct atom by `id` or by substring match. Recommend fix for precision.

## B8 Forward-map to rubrics (Outcome 1.1 per write action)

| Write OE | Proposed Outcome 1.1 rubric title |
|---|---|
| OE16 (reply Craig) | "Reply sent on Craig Nguyen's Apr 11 KeyMove damage-photos email answering whether to file the formal insurance claim now or hold pending the customer-side disposition" |
| OE17 (email David + Catalina) | "Email sent to David Chen and Catalina Dubois with two-sided Emilia Cruz damage docket position: vendor-side closure + customer-side credit-memo/commercial-consideration handoff" |
| OE18 (airtable update Emilia row) | "Emilia Cruz relocation record Special Requirements field extended (not overwritten) with damage-disposition addendum naming vendor closure, customer-side pending flag, and walkup-assessment operational lesson" |
| OE19 (Slack post C006) | "Walkup-assessment operational lesson posted to the operations Slack channel" (rubric title MUST NOT name "C006" or "#operations" per rule 7) |
| OE20 (Linear comment on retention issue) | "Operational facts on the Emilia damage docket close-out added as a comment on the existing NorthWind retention Linear issue" |
| OE21 (Monday calendar reminder) | "Calendar event created for Monday Apr 27 to follow up on Craig's response regarding the KeyMove formal-claim filing" |

All 6 writes have natural Outcome 1.1 coverage. PASS.

Note for S3: rule 7 forbids tool names in rubric titles. OE19's title above is rule-compliant (no "Slack", no "C006") — surface name "operations" is allowed as a descriptive channel reference, but S3 should confirm pivot phrasing if a council flags it as channel-lock-in (Lever 9 risk, flagged in Hardness_Plan).

## B9 Reverse-map prompt-to-OE

| Prompt ask (explicit + implicit) | Covered by | Verdict |
|---|---|---|
| (a) Craig's Apr 11 trailing question — direct reply with formal-claim-or-hold direction | OE6 (read) + OE16 (reply) | COVERED |
| (b) Email David and Catalina with operational position + what's still moving on customer side | OE7 (context reads) + OE17 (send with two-sided structure including customer-side handoff) | COVERED |
| (c) Update Emilia's relocation record to reflect both sides — preserve existing field shape, extend not overwrite | OE10 (schema) + OE11 (pre-read) + OE18 (update with explicit "extend not overwrite") | COVERED |
| (d) Drop Emilia lesson in Slack where Chloe + ops team will see it (= operations channel C006) | OE2 (channel enumeration) + OE19 (post to C006) | COVERED |
| (e) Operational facts on the existing Linear retention item | OE9 (read existing issue + existing comments) + OE20 (create comment on linear_issue_c8cdba4408f1) | COVERED |
| (f) Monday reminder to confirm Craig got his answer | OE21 (2026-04-27 calendar event with Craig follow-up context) | COVERED |
| (implicit) Mirror Mosaic two-sided structure | OE12 (Mosaic precedent read) + OE17 (vendor-closed + customer-pending structure) | COVERED |
| (implicit) Walkup-assessment captured as operational lesson, not papered over | OE18 + OE19 + OE20 (3-surface capture) | COVERED |
| (implicit) Stay in operational lane — don't propose customer-side dollar | OE17 explicit ("hand the customer-side off rather than assume or recommend a dollar figure") + OE22 consistency check | COVERED |
| (implicit) Pam not on recipient list, no escalation echo | OE17 explicit + OE22 explicit | COVERED |
| (implicit) Surface what David+Catalina would need (credit-memo scope + commercial consideration) | OE17 (customer-side handoff text covers both) | COVERED |

Zero unmapped asks. PASS.

## Summary

**Issue counts:**
- Major: 0
- Moderate: 1 (B3 density THIN borderline — midpoint sits at ~38.5-42 depending on how "or" branches and "optional" steps are weighted; too close to the 40-floor BLOCKER for comfort)
- Minor: 2 (B2 OE15 is confirmatory low-marginal-utility; B7-cos OE4 narrative "and" vs "&" cosmetic typo)

**Final verdict: REVISE (light, surgical).**

Reasoning: B1 5/5 + 5/5, B2/B4/B5/B6/B7/B8/B9 all PASS. The only structural concern is B3 — pure-OE-as-written midpoint (38.5) is uncomfortably close to the v11/v12 INSUFFICIENT-DENSITY blocker. Two narrow surgical edits to OE13 and OE14 (promote the "optional" QB invoice search and the "optional" CRM deals + engagements reads to required) deterministically lock the OE-encoded midpoint at ~43-44, fully within THIN-DENSITY band and aligned with Hardness_Plan's carry-forward justification. Optional third edit (re-fetch Marcus's email + Mosaic bill before composing OE17) would push to ~46.

After those edits, the OE is GO-grade. No rebuild needed.

**AUDIT-trigger flags (for the strict-veteran AUDIT sub-agent):**
- B3 density math borderline — verify any chosen midpoint > 42 after edits, with explicit per-task justification anchored to Hardness_Plan rationale items 2 and 3 (Lever 8 upper-bound weighting + L9-anchored stump-design THIN expectation).
- B7-cos OE4 narrative precision ("Claims & Remediation Expense", with ampersand) — non-blocking but flag for tightening.
- Lever 9 channel-lock-in risk on OE19 — rubric title at S3 must NOT name "operations" / "C006" / "Slack". This OE is fine for the OE phase (rule 7 allows tool/channel names in OE bodies), but downstream S3 must pivot phrasing.

**Council A coordination:** running in parallel; if A surfaces grounding gaps in any cited atom, defer to A. This council confirms zero fabricated IDs against the universe split.
