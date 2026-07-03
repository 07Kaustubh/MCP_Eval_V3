# Hardness Plan

## Anchor Decision

**Anchor A** (NorthWind / Emilia Cruz piano-damage operational docket). Blessing Okafor (Relocation Coordinator and operational owner of the Emilia Cruz move since the Apr 11 damage incident) must close out the operational damage docket on Apr 24 — the same day the $1,200 KeyMove insurance rider (`BILL-KEYMOVE-2026-0417`, DueDate 2026-04-24) sits unprocessed in QuickBooks AND Pam Kowalski's formal escalation (`email_email_7168baed8438`) lands demanding a Friday EOD proposal that includes "resolution path and reimbursement handling for Emilia Cruz's damage claim." Marcus Thorne's same-morning email (`email_email_99e10a978b48`) verbatim: *"Operationally, we need to process it unless someone has a basis to dispute the charge... I do not love paying this, but I also do not see a clean finance argument for rejecting it as submitted"* — the textbook L9 authority dismissal that frames the $1,200 vendor rider as the whole disposition and lets the customer-side docket fall through. The Mosaic Robotics precedent (`mosaic_incident_report_final_001` + `bill_mosaic_damage_accrual_001`) establishes the correct structured model (vendor cap $50K + MoveOps direct exposure + customer credit memo CM-2026-0415 against client invoice + Section 6 process improvements) that Blessing must recognize, flag, and feed to David/Catalina for the Friday retention package — without overstepping into Marcus's finance authority on the rider itself.

**Leak check:** verbatim grep for "Emilia Cruz" × "reimbursement / credit memo / compensation / customer comp / goodwill credit" returns ZERO Emilia-specific dollar figures across email + Slack + Linear + Airtable + QB. The customer-side disposition is genuinely open (Pam asks for "any commercial consideration you believe is appropriate"). L6 hard rule PASSES.

## Persona and Business Function

- Blessing Okafor (Relocation Coordinator)
- Operations

## Levers Available

| # | Lever | Status | Evidence | Cost range |
|---|---|---|---|---|
| 1 | Latching | **PRESENT (strong)** | `$1,200` anchored 6+ surfaces: `BILL-KEYMOVE-2026-0417`, Marcus's Apr 17 email subject + body, Catalina's Apr 13 draft to David, Alejandro's Apr 16 retention model, plus 6 Slack messages in KeyMove/Emilia context. Marcus's L9 dismissal is on-brand domain-correct finance language. | 5-8 |
| 2 | Structured-DB skip | **PRESENT (strong)** | Airtable `tblRelocations01` Emilia row `recEmiliaCruzChicagoDenver` (damage disposition field via `Special Requirements` multilineText per Sarah Chen + Jamie Reeves precedents) AND `bill_mosaic_damage_accrual_001` ($90K accrual w/ $50K vendor cap + $40K direct exposure model) AND `mosaic_incident_report_final_001` (Section 6 process improvements). All require structured queries the agent typically skips. | 4-7 |
| 3 | Missing reply | PRESENT (moderate) | Craig Nguyen's Apr 11 email closes verbatim: *"Please let me know whether you want us to open a formal insurance claim on our side now or hold pending your client's review."* Blessing has not replied. | 3-5 |
| 4 | Search-cap eviction | LOW (not selected) | Emilia content is high-density (13 emails + 15 Slack + 4 Linear comments + Linear issue). Not buried. | 3-5 |
| 5 | Thread-reply blindness | LOW (not selected) | Key facts are in top-level emails, not thread replies. | 2-4 |
| 6 | Near-miss entity confusion | LOW (not selected) | One Emilia, one KeyMove, one Steinway. No near-misses. | 3-5 |
| 7 | Multi-write diversification | **PRESENT (strong)** | 6 distinct writes naturally required across 5 services: email × 2 (Craig + Catalina/David), airtable update (Emilia row), Slack post (#operations C006), Linear comment (retention issue), reminder (Mon follow-up). | 9-12 |
| 8 | Multi-link chain | **PRESENT (strong)** | 5-link: Craig Apr 11 ask → Marcus Apr 17 L9 → Pam Apr 24 escalation → `linear_issue_c8cdba4408f1` retention issue → Catalina's Apr 14 EOD-Friday commitment. Spans email + Linear + QB + Airtable. | 6-9 |
| 9 | Universe-grounded gotcha | PRESENT (light) | MoveOps universe constants: Slack #operations is C006 (Blessing's home channel, NOT #customer-engagement C002 or #finance C005); Linear comment uses `issueId + body`; email uses `content` (not `body`). Bundled into base discovery. | 3-5 |
| 10 | Reversal / supersession | NOT APPLICABLE | No reversal pattern in play. | 4-6 |
| 11 | Net-vs-gross framing | **PRESENT (moderate-strong)** | Gross vendor cost ($1,200 KeyMove rider, payable to vendor) ≠ net MoveOps cost (rider + customer-side credit memo/comp per Mosaic precedent + commercial concession per Pam item 4). Agent must distinguish vendor disposition from customer disposition. | 4-7 |

## Selected Levers (5)

- **Lever 1 (Latching)** — `$1,200` anchored in 6+ surfaces; Marcus's L9 dismissal frames the rider as a finance-clean disposition. Cites Learnings L9 (authority-dismissal, ~100% fail rate as single mechanism) + L13 (first-framing) + L25 (existing-output anchor). Cost midpoint **7**.
- **Lever 2 (Structured-DB skip)** — Agent must query `tblRelocations01` for Emilia row + `bill_mosaic_damage_accrual_001` for the precedent model. Cites Learnings L10 (0/6 query rate on analogous structured DB) + L11 + L25. Cost midpoint **6**.
- **Lever 7 (Multi-write diversification)** — 6 writes / 5 services / 1 reminder. Cost midpoint **11**.
- **Lever 8 (Multi-link chain)** — 5-link chain (Craig→Marcus→Pam→Linear→Catalina commitment). Cites Learnings L8. Cost midpoint **8**.
- **Lever 11 (Net-vs-gross framing)** — Vendor rider ≠ customer-side reimbursement scope. Cites Learnings L11 + L14 (correct-observation/wrong-conclusion: agent finds the $1,200 but reasons "this IS the disposition" instead of "this is one ledger line, customer-side is open"). Cost midpoint **6**.

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (contacts, channels, vendor lookup, account schema, NorthWind CRM, Mosaic precedent baseline) | 6-9 | 7 |
| Lever 1 reads (KeyMove bill, 4 surfaces of $1,200 anchor) | 4-6 | 5 |
| Lever 2 reads (airtable schema + Emilia row + Mosaic bill + retention engagement) | 4-6 | 5 |
| Lever 8 reads (Craig Apr 11, Marcus Apr 17, Pam Apr 24, Catalina Apr 14 commitment, Linear issue + comments, Julian customer-side note) | 6-9 | 7 |
| Lever 11 reads (QB chart of accounts ACC-6185 / Claims & Remediation; NorthWind QB customer + invoices for credit-memo precedent; Alejandro retention model context) | 4-6 | 5 |
| Lever 7 write actions (6 writes + 6 write-support reads not double-counted) | 11-14 | 12 |
| Cross-service triangulation buffer | 5-8 | 6 |
| **TOTAL projected** | **40-58** | **47** |

**Gate:** THIN_DENSITY (midpoint 47, range 40-58)

### THIN density acceptance

Per-task justification for operator continuation despite midpoint < 50:

1. **6 distinct writes across 5 services + reminder** is the realistic ceiling for a single Relocation-Coordinator-scoped task — pushing to 7+ writes would force scope creep into Marcus's (finance) or David's (customer-comm) authority, which corrupts the persona-fit and the L25 mechanism (Blessing must distinguish vendor disposition from customer disposition, not assume both).
2. The multi-link chain (Lever 8) is genuinely 5 links across 3 services (email + Linear + QB) — its 6-9 range upper bound (9) is justified given the chain length, which would raise midpoint to 51. Operators willing to weight Lever 8 at the upper end can treat this as PASS.
3. Agents who actually traverse the L2 + L8 chain will hit 50+; agents who short-circuit at L1+L9 will land at the lower 40s — which is the *intended* discrimination. The THIN band IS the expected projection when the design relies on stump levers that 50%+ of agents will fail to fully execute (THIN_DENSITY is the natural projection for L9-anchored stumps).
4. If midpoint comes in below 45 in real platform runs, operator should rescope to add a `tblClientAccts01` NorthWind ARR-context read + a calendar event create (Friday EOD anchor) to push densities up; do NOT add levers that pull the persona into finance/customer-comm scope.

**Operator decision:** continue to S1 with explicit STUMP_HYPOTHESIS attention to Lever 8 traversal; flag for re-evaluation after first trajectory cycle.

## Service Breadth (v11 G1)

| Service | Calls | % of total |
|---|---|---|
| email (search, get, send) | 12-14 | ~27% |
| airtable (tables, records, update) | 5-6 | ~12% |
| quickbooks (bills, vendor, accounts, customer, invoices) | 6-8 | ~15% |
| linear (issues, comments, create_comment) | 5-6 | ~12% |
| slack (channels, search, post) | 4-5 | ~10% |
| contacts (search, get) | 3-4 | ~8% |
| crm (companies, deals, engagements) | 3-4 | ~8% |
| reminders | 1 | ~2% |
| **Distinct services** | **8 (7 with ≥5%, reminders at 2%)** | — |

**Breadth gate:** PASS — 7 services with ≥5% share, dominant service (email) at 27% well under the 60% cap. The 4-service-with-≥5% floor cleared by 3.

## Stump Hypothesis (4)

1. **[HIGH]** Agent stops at "approve / process the $1,200 KeyMove rider" and never files the customer-side damage-claim docket distinct from the vendor disposition. Mechanism: Lever 1 (Latching on Marcus's L9 frame + 6-place $1,200 anchor) + Lever 11 (treating gross vendor rider as net disposition). Reasoning: Marcus Thorne speaks in domain-correct finance language ("their paperwork lines up... I do not see a clean finance argument for rejecting it as submitted") — Learnings L9 source notes this is the single most effective stump mechanism observed on Brookfield. The $1,200 is anchored in 12+ surfaces (QB + 6 emails + 6 Slack messages in KeyMove/Emilia context), making it the strongest L13 first-framing target seen in V3 to date.

2. **[HIGH]** Agent never queries Airtable `tblRelocations01` for the Emilia Cruz row AND never queries `bill_mosaic_damage_accrual_001` for the precedent model (vendor cap $50K + $40K direct exposure + customer credit memo CM-2026-0415 + Section 6 process improvements). Mechanism: Lever 2 (Structured-DB skip). Reasoning: Learnings L10 source — 0/6 agents in the analogous Brookfield SAP-subledger task ever queried the structured DB even when in-conversation hints pointed at it. The Mosaic precedent is in a QB BILL (an "AP" pile most agents won't enumerate when the prompt anchors on a single vendor rider) and the Emilia damage state lives in an Airtable Special Requirements free-text field that agents don't naturally search.

3. **[MED]** Agent posts the operational lesson-learned to #customer-engagement (C002, Catalina's home) or #finance (C005, Marcus's home) instead of #operations (C006, Blessing's home). Mechanism: Lever 9 (universe-grounded persona-channel gotcha) + Learnings L26 (decoy-parent / channel-misalignment). Reasoning: the NorthWind retention discussion thread reads as customer-engagement topical; the $1,200 vendor rider reads as finance topical; #operations is correct because the lesson-learned is operational (walkup-assessment process gap, per Blessing's persona-brief admission and the Mosaic precedent Section 6 model).

4. **[MED]** Agent emails Craig Nguyen but does NOT answer his Apr 11 open question (*"open a formal insurance claim on our side now or hold pending your client's review"*). Mechanism: Lever 3 (Missing-reply / question-blindness — adjacent). Reasoning: Craig's question is at the END of a long damage-photos email — Learnings L12 source shows agents reliably find parent messages but miss trailing asks and thread replies. Agent's natural reply is "acknowledged, will process" without addressing Craig's specific procedural question, which leaves the formal insurance filing in limbo and reproduces the same documentation-gap pattern the Mosaic precedent's Section 6 was designed to prevent.

## Hardness Score

**5/5 — PASS** (with THIN_DENSITY operator note on Lever 8 traversal weighting)

## Answer-Leak Audit

- **The "correct" decision the agent must derive:** File the operational damage docket distinguishing vendor disposition ($1,200 KeyMove rider, process-as-submitted per Marcus, vendor-side closed) from the customer-side disposition (per Mosaic precedent: credit-memo-equivalent against NorthWind invoice + commercial-consideration scope = flag for David/Catalina's Friday retention package — Blessing has no finance authority to issue the credit memo herself). No specific reimbursement dollar figure is the "right" answer — the customer-side scope is a commercial decision genuinely open for David/Catalina/Elena.
- **Verbatim search across email + Slack + Linear + Airtable + QB:** Zero hits for "Emilia Cruz" within 100 chars of "reimburs|credit memo|customer comp|goodwill credit|compensation|comp X|settle X|make whole". All "reimbursement / goodwill" hits in universe are on Simone Richter $340 (StormCloud freeze), Jamie Reeves $500 (StormCloud Jae-won), Sarah Chen $100 (Greenleaf), Liam Park unnamed "promised goodwill credit." Alejandro's retention model mentions "piano-related goodwill credit" abstractly with NO number. **L6 PASSES.**
- **Persona's anchored wrong number:** $1,200 (KeyMove vendor rider). Surface count: 12+ places (QB bill + 6 emails + 6 Slack messages in KeyMove/Emilia context).
- **L9 authority dismissal quote (Marcus Thorne, Apr 17, `email_email_99e10a978b48`):** *"I reviewed the KeyMove bill that came in this morning and they added a $1,200 insurance claim rider tied to Emilia Cruz's Steinway damage claim. Operationally, we need to process it unless someone has a basis to dispute the charge. Their paperwork lines up with Craig Nguyen's April 11 damage email and Blessing's note that the walkup assessment was insufficient. I do not love paying this, but I also do not see a clean finance argument for rejecting it as submitted."*
- **L6 hard rule passes:** YES — confirmed by verbatim grep.
- **L15 implicit-prompt rule:** Prompt-design intent — anchor on Blessing's view that the KeyMove rider hit QB and Catalina is asking ops for the operational damage-claim status by EOD; DO NOT hint that the $1,200 is wrong, DO NOT hint that the customer-side disposition is open, DO NOT mention Pam's Apr 24 formal escalation or Friday's retention package. Blessing should believe the rider is routine vendor disposition; agent must self-discover (via the Mosaic precedent query) that vendor disposition ≠ customer disposition.
- **L29 escape-valve check:** **Moderate risk surfaced.** Marcus's email contains the line *"If we are paying the vendor rider before the customer even has a callback, that is not going to look great internally"* — this directly invites the agent to check the customer side. **Mitigation:** (a) the prompt itself must not include any escape-valve clauses ("if anything looks off, say so plainly", "let me know if I'm missing something"); (b) Lever 2 (Structured-DB skip on Airtable + Mosaic precedent) provides a second layer — even agents who notice Marcus's customer-side flag must still query the precedent to recognize the correct customer-side credit-memo model. Without the Mosaic precedent query, an L29-rescued agent will write "callback Emilia" but not "file the customer-side credit-memo scope for David/Catalina's Friday package per Mosaic precedent." The prompt writer should NOT echo Marcus's customer-side question; the prompt anchors only on the operational vendor-side disposition Blessing has been sitting on.

## Hardness Brief for the Prompt Writer

Anchor the prompt on Blessing seeing the KeyMove rider (`BILL-KEYMOVE-2026-0417`, $1,200, due Apr 24, line description "Insurance claim rider for Emilia Cruz Steinway piano scratch during stairwell extraction") sitting in QB this morning, with Chloe asking ops to close out the operational side of the Emilia Cruz damage claim before COB because "Catalina is pulling a NorthWind status package together" — NEVER name Pam's formal escalation, the Friday EOD package, the retention question, or the $60K account risk. Blessing should believe the rider is routine vendor disposition. Selected levers: L1 (latching on the $1,200 + Marcus L9 frame), L2 (Airtable + Mosaic precedent skip), L7 (6 writes / 5 services), L8 (5-link chain Craig→Marcus→Pam→Linear→Catalina commitment), L11 (vendor gross ≠ customer net). Required derivations: (a) the $1,200 KeyMove rider is the VENDOR-side line, not the customer-side disposition; (b) the Mosaic precedent (`bill_mosaic_damage_accrual_001` + the analogous incident report email pattern) establishes the correct customer-side model — vendor cap, MoveOps direct exposure, credit memo against client invoice, Section 6 process improvements — but Blessing has NO finance authority to issue a customer credit memo herself; (c) the operational docket must distinguish vendor-side ("acknowledge KeyMove rider, ask Craig the open Apr 11 question about formal insurance claim filing") from customer-side ("flag for Catalina/David: credit-memo scope + commercial consideration to be decided by them") AND must reference the walkup-assessment process gap as a Mosaic-precedent-aligned operational lesson. Load-bearing writes: email Craig Nguyen (acknowledge rider + answer Apr 11 formal-claim-or-hold question), email Catalina cc David (operational damage docket summary + flag customer-side credit-memo scope for their retention package), `airtable_update_records` on Emilia Cruz's `tblRelocations01` row (damage detail + vendor disposition + customer disposition pending flag — write to `Special Requirements` per Sarah Chen/Jamie Reeves precedent format), Slack post to `#operations` C006 (walkup-assessment lesson-learned, NOT C002 #customer-engagement or C005 #finance), `linear_create_comment` on `linear_issue_c8cdba4408f1` (operational facts for the retention plan), reminder for Mon Apr 27 (follow up on Craig's formal-claim response + Catalina's package landing). Density target: 47-55 midpoint via Lever 8 traversal. Hard rules: NO escape-valve clauses, NO Pam-escalation mention, NO Friday-EOD-package mention, NO $60K-account-risk mention, NO em-dashes, ≤500 words, no tool names, no service names, no Linear issue IDs, no Airtable record IDs, no QB bill numbers, no specific $-figure for any customer-side reimbursement (none exists in universe). Channel-lockin minor risk on the Slack post — phrase persona ask as "drop the ops lesson where it belongs" rather than naming #operations.
