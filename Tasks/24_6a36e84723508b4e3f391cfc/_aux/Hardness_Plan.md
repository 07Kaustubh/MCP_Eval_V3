# Hardness Plan

Task: `24_6a36e84723508b4e3f391cfc` (REDO rebuild — prior FAIL on DENSITY, avg 32.5 vs 40 floor; difficulty acceptable at pass@1 = 16.7%)
Universe today: 2026-06-12 (US/Eastern)
Hardness reading anchor: `Tasks/_meta/Learnings.md` L1-L22, `Reference/Hardness_Playbook.md` levers 1-11.

## Persona and Business Function

- Persona: Lena Park (`lena.park@brookfieldcpas.com`), Procurement Officer. Authority is to TRIAGE and ESCALATE, NOT to approve, route, or post. Always defers AP disposition to Daniel Jones (Accounts Manager) or Steven Perry (Managing Partner). Owen Mercer (AP Specialist), Priya Khatri (AP Coordinator), Tariq Soto (AP Clerk), Margaret Sullivan (Controller) are the supporting cast.
- Business function: AP / Vendor Operations — Procurement Officer view of the pending-approval queue across all three entities (Brookfield, Northstar Legal, Acme Cloud), with scope verification on high-value invoices touching managed-client entities.
- Authority-figure pattern (for L9 dismissal): Daniel Jones is the believed-authority figure Lena will quote on a Slack thread reply, claiming the routing rule was already fixed; Steven Perry is the partner-sign-off escalation channel. Margaret Sullivan is the controller-tier reviewer when Daniel and Steven are unavailable.

## Levers Available (table — all 11 levers)

| # | Lever | Status | Evidence (file:row_id or file:index) | How prompt writer weaves it | Learnings cite |
|---|---|---|---|---|---|
| 1 | Latching | PRESENT | `slack.slack_messages.json` C010 has 189 messages including persona_009 "Flagging a recurring issue: vendor approvals are stacking up late enough that we're missing payment windows" and persona_014 acme_cloud "stale approval chain" parent posts; persona narrative pre-anchors "two or three" complaint vendors | Persona believes the orphan-approver problem is already fixed because she recalls Daniel saying the routing rule was patched; prompt should plant the dollar-bias anchor ("the worst ones") and a separate age-bias counter-anchor so the agent must reconcile both | L13 first-framing trap, L1 single-hop discoverability |
| 2 | Structured-DB skip | PRESENT | `records_vault.rv_documents.json`: `doc_eb7cb30c59bd4f03` (acme_cloud `engagement_letter_addendum`), `doc_2d85ac5a698745c5` (acme_cloud `engagement_change_order`), `doc_0036f5b991574808` (northstar_legal `engagement_letter`), 0 of any of these for brookfield | Mandate scope verification on TWO managed-client entities. Acme scope = addendum + change_order (multi-state sales tax + AR-aging bucket); Northstar scope = engagement letter. The agent must search MULTIPLE doc kinds per entity, not just `engagement_letter` | L11 structured-source vs conversation skip, L18 the figure IS the rubric |
| 3 | Missing reply | PRESENT | `email.emails.json` thread "vendor approval chain delays are causing missed payment runs" from `jones.harrison@brookfieldcpas.com` has 5+ replies (blue.evans, edith.banda, ron.atkins); Owen Mercer escalation chains on VEN-010 / VEN-012 / VEN-033 with Daniel Jones replies | Persona asks the agent to check whether the issue has come up before. Reply chains carry the diagnosis (orphan vs dispute vs missing credit memo). Agent who reads the parent and stops misses the actual disposition | L12 thread-reply blindness |
| 4 | Search-result-cap eviction | PARTIAL | `sap_subledger.ap_invoices.json` 320 pending_approval rows across 3 entities (brookfield 127, acme 106, northstar 87); 275 over 80 days; the highest-aged record (VEN-010-B TimeLedger Nexus 341 days) sits in a different vendor cluster than the highest-dollar | If the agent searches only by `entity_id` or only by `status` without age-sort or pagination, the long tail is invisible. Not strong alone but pairs with latching | L11 subledger invisibility |
| 5 | Thread-reply blindness | PRESENT | `slack.slack_messages.json`: 2070 thread replies overall, 145 in C010 alone; multiple existing parent + reply chains on `VEN-019-583136` (Bridgefield), `VEN-012-753165` (GraniteRack), `VEN-030-817856` (CrownPeak) | Plant the Daniel Jones "routing was fixed last sprint" dismissal as a Slack thread REPLY to an existing C010 parent post, not as the top-level message. Same for the "missing credit memo on GraniteRack" disposition | L12 |
| 6 | Near-miss entity confusion | PARTIAL | `sap_subledger.ap_invoices.json` vendor IDs include suffix collisions: `VEN-002` vs `VEN-002-B` (CivisCode), `VEN-012` vs `VEN-012-B` (GraniteRack), `VEN-019` vs `VEN-019-A` (Summit Shield Casualty vs Bridgefield Backup), `VEN-030` vs `VEN-030-B` (CrownPeak); also account `210000` vs `219000` trap | Use one confusable-pair vendor (e.g. mention "Bridgefield" without the VEN suffix); force the agent to distinguish 219000 employee reimbursements from 210000 external vendor AP when ranking exposure | L4 (weak alone, adds friction) |
| 7 | Multi-write diversification | PRESENT | `slack.slack_channels.json:C010` (vendor-bills-and-ap); `linear.linear_issues.json:issue_378874ffeb8f4cb0b0417021f2d3d647` ("Fix AP routing rule for departed approvers and sweep orphaned pending approvals"); `linear.linear_issues.json:issue_0b05ec215a854a439472fb0c6bd3307b` ("Run expired W-9 sweep across managed-client vendor master"); `contacts.contacts.json` Daniel Jones + Steven Perry + Margaret Sullivan exist | Mandate FOUR distinct write actions: (a) C010 Slack post with vendor-level detail, (b) Linear comment on the existing orphan-approver tracking issue, (c) email draft to Daniel Jones (primary) plus Steven Perry (cc) for partner sign-off on 80+ day items, (d) reminder for a 7-day follow-up sweep. This is the dominant density lever | L5 writes alone don't stump but drive density floor |
| 8 | Multi-link chain | PRESENT | Three named 3-link chains exist in the universe: (i) `apinv_5e09decd035d4443` / `VEN-033-86573` BeaconPay (SAP pending) → no Linear issue → email "partner sign-off request: release of apinv_5e09decd035d4443 / ven-033-86573" from Daniel Jones; (ii) `apinv_6131b7c637aa4b6e` / `VEN-012-753165` GraniteRack (SAP pending) → `issue_e5abbb9af74642eeb10a93426b0bbaa2` Linear "void-and-rebill" → Owen Mercer escalation email; (iii) `apinv_d3019cdcc6ed44b2` / `VEN-010-514242` TimeLedger (SAP pending) → `issue_e6fbc488077344c28cc7cd13640c54bc` Linear "AP escalation" → Daniel Jones partner sign-off email "conditioned release for timeledger invoice" | Mandate per-vendor root-cause diagnosis for the top 3-5 aged invoices, requiring SAP detail + Linear issue check + email escalation cross-reference per vendor. Without all three the agent cannot distinguish orphan-approval from disputed-deliverable from missing-credit-memo | L8 three-link chain, L11 structured-source skip, L14 correct observation / wrong conclusion |
| 9 | Universe-grounded gotcha | PRESENT | All scope docs are `classification = restricted` (`doc_eb7cb30c59bd4f03`, `doc_2d85ac5a698745c5`, `doc_0036f5b991574808`); `records_vault.rv_access_grants.json` has 184 grants — Lena Park is a Procurement Officer (non-restricted default role) and may need an explicit grant to read; approver field is null on 320/320 pending records (systemic data signal); GL account split `210000` (external vendor AP) vs `219000` (employee reimbursements) creates a category trap | Force scope-verification on RESTRICTED docs; the agent must either find an access_grant for Lena or report the access constraint. Force the agent to filter on `210000` specifically rather than all AP; otherwise employee-reimbursement items pollute the "vendor backlog" count | L18 the figure IS the rubric, L11 structured-source skip |
| 10 | Reversal / supersession | ABSENT | No reversed JEs or superseded SOWs directly relevant to the pending-approval AP workflow exist in a way that drives this task. 92 voided invoices exist but are not in the pending queue | Do not weave in. Saves rubric atomicity for the load-bearing levers | not cited |
| 11 | Net-vs-gross framing | PARTIAL | `sap_subledger.subledger_transactions.json` (2752 records) includes credit memos and adjustments per vendor; computing "net exposure per vendor" is possible but not the primary lens for backlog triage | Could embed as a secondary check ("after credits, what's the net exposure on the worst offenders?") but adds contrivance risk if stacked with L8. Mark partial; do not select | L18 if used |

## Selected Levers (3-5)

Five levers, deliberately chosen so the prior attempt's narrow surface (1 Slack write, 1 RV entity scope, no Linear, no per-vendor drill) is structurally impossible:

1. **L1 Latching** (cost 5-8). Persona-anchored dollar-bias plus a planted Daniel-Jones dismissal that the routing rule "was already fixed last sprint." Agent must reconcile the dismissal with the fact that invoices DATED AFTER the supposed fix still appear with `approver = null`. Maps to Learnings L9 (authority-figure dismissal — the single most effective stumping mechanism) and L13 (first-framing trap).

2. **L2 Structured-DB skip** (cost 4-7). Scope verification on BOTH managed-client entities (Acme Cloud + Northstar Legal) with mixed doc kinds — Acme is `engagement_letter_addendum` + `engagement_change_order`, Northstar is `engagement_letter`. The prior R4 trap demanded an Acme `engagement_letter` that doesn't exist; the new lever rewards the agent for FINDING the addendum + change_order (which DO exist) and reporting Acme's scope from those. Maps to Learnings L11 + L18.

3. **L7 Multi-write diversification** (cost 9-12). Four distinct writes across four services: (a) Slack post to `C010` (vendor-bills-and-ap), (b) Linear comment on the existing `issue_378874ffeb8f4cb0b0417021f2d3d647` orphan-approver tracking issue, (c) email draft to Daniel Jones with Steven Perry on cc for partner sign-off on 80+ day items, (d) reminder for a 7-day follow-up sweep. Maps to Learnings L5 (writes are a density floor, not a stumping lever — used here PURELY for density).

4. **L8 Multi-link chain** (cost 6-9). Per-vendor 3-link diagnosis (SAP → Linear → email) for the 3-5 top aged invoices. The universe carries three named chains (BeaconPay VEN-033 / GraniteRack VEN-012 / TimeLedger VEN-010); the agent who only reads SAP cannot classify root cause (orphan-approval vs disputed vs missing-credit-memo). Maps to Learnings L8 + L11 + L14.

5. **L9 Universe-grounded gotcha** (cost 3-5). RESTRICTED classification on scope docs + 320/320 null-approver systemic signal + `210000` vs `219000` account split. The agent who pulls all AP including 219000 employee reimbursements over-counts the backlog; the agent who skips the access-grant check may misreport "scope doc retrieval failed" without distinguishing from "no doc exists." Maps to Learnings L18.

Not selected (and why):
- L3 Missing reply: covered indirectly by L1 and L8 (the reply chains BECOME the cross-service evidence chain). Adding it explicitly would over-stack.
- L4 Search-result-cap eviction: marked PARTIAL and weaker than L1 + L9 for the same effect.
- L5 Thread-reply blindness: folded INTO L1 (the Daniel-Jones dismissal is planted as a thread reply, not the parent). Counted once under L1.
- L6 Near-miss entity confusion: weak alone (L4 in Learnings); added as flavor inside the prompt but not selected as a load-bearing lever.
- L10 Reversal: not present in usable form.
- L11 Net-vs-gross: would add contrivance; skipped.

## Lever changes from previous attempt

Prior effective levers (from `_aux/Candidate_Originals/` review):
- Latching on top-dollar framing (L1 in playbook terms — but only one anchor)
- Structured-DB skip targeting Records Vault for ONE entity (acme_cloud) on ONE kind (engagement_letter) — IMPOSSIBLE atom, broke R4 in 3/6 runs
- Missing reply on prior-conversation check (loose, no specific chain mandated)
- Single multi-write (only Slack post + final summary = 1 write surface)

Material deltas in this rebuild:

| Dimension | Prior | New | Net effect |
|---|---|---|---|
| Scope verification | 1 entity, 1 doc kind (impossible) | 2 entities, 3 doc kinds (real atoms — addendum, change_order, engagement_letter) | Forces 6-9 extra RV reads; fixes the unwinnable R4 trap |
| Per-vendor drill | One big SAP batch (e.g. "list pending_approval") | 3-link chain per vendor (SAP detail + Linear lookup + email check) for top 3-5 | Forces 9-15 extra reads across 3 services |
| Write actions | 1 (Slack only) | 4 (Slack + Linear comment + email draft + reminder) across 4 services | +9-12 calls minimum |
| Authority-dismissal lever | Top-dollar framing implicit | Explicit Daniel-Jones "fixed already" Slack thread reply + dollar-bias anchor | Adds Learnings-L9 explicit pressure (the highest-yield stump pattern) |
| Prior-conversation check | "Loose" — agent may skip | Reading 3+ email/Slack threads (Jones Harrison parent + Owen Mercer escalations + C010 history) is required to differentiate root causes | Forces 4-6 extra reads |

The previous attempt's 32.5 average is structurally re-routed: the agent that satisfies the prompt without 40+ calls must skip an entity, skip a write, skip a service, or skip a root-cause classification — each of which the rubric and OE will explicitly catch.

## Tool-Call Density Projection (table)

| Component | Low | High | Mid | Notes |
|---:|---:|---:|---:|---|
| Base discovery (period lookup, channel resolution, contact lookup, vendor master sweep) | 5 | 8 | 6.5 | C010 channel lookup, Daniel/Steven/Margaret contact lookup, fiscal period boundary check |
| L1 Latching | 5 | 8 | 6.5 | Slack C010 history sweep + Daniel-Jones thread reply find + reconcile dismissal against post-fix-date invoices |
| L2 Structured-DB skip | 4 | 7 | 5.5 | 2 entities × 3 doc kinds = 6 RV calls min, plus access-grant check |
| L7 Multi-write diversification | 9 | 12 | 10.5 | 4 writes × ~2.5 supporting reads each |
| L8 Multi-link chain | 6 | 9 | 7.5 | 3 vendors × (SAP detail + Linear issue + email thread) |
| L9 Universe-grounded gotcha | 3 | 5 | 4.0 | Access-grant check + 210000-vs-219000 account filter + null-approver count |
| Cross-service triangulation buffer | 5 | 8 | 6.5 | Re-fetches when initial filter misses, BlackLine exception cross-check, Airtable AP Workflow Exceptions sweep |
| **PROJECTED TOTAL** | **37** | **57** | **47.0** | |

Midpoint **47 >= 40**. PASS density gate with margin (+7 above floor, +14.5 above the prior 32.5 failure). High-end 57 leaves room for thorough agents to over-spend; low-end 37 still risks density miss for fast-and-loose agents — explicit OE pressure on per-vendor drill + 4 writes is what closes the low-end gap.

## Stump Hypothesis (2-4 predictions)

### Prediction 1 — Root-cause miscategorization on 2 of 3 top vendors (HIGH confidence)

Agent reports the 3 top-aged invoices (BeaconPay VEN-033, GraniteRack VEN-012, TimeLedger VEN-010) as "stuck in approval" or "pending senior sign-off" without distinguishing orphan-approver from disputed-deliverable from missing-credit-memo. Mechanism: L8 three-link chain — agent reads SAP (pending status, approver=null) and stops, never cross-references Linear (`issue_e5abbb9af74642eeb10a93426b0bbaa2` says GraniteRack needs void-and-rebill for a missing credit memo; `issue_e6fbc488077344c28cc7cd13640c54bc` says TimeLedger is awaiting partner sign-off; BeaconPay VEN-033 has no Linear issue, indicating true orphan). Cite Learnings L11 + L14. Atoms verified: all three apinv IDs + both Linear issues + Owen Mercer / Daniel Jones email threads all confirmed present.

### Prediction 2 — Acme Cloud scope reported as "not found" instead of "addendum + change order" (HIGH confidence)

Agent searches for `kind = engagement_letter` on `entity_id = acme_cloud`, finds 0, reports "Acme scope not in vault" — and fails to pivot to `engagement_letter_addendum` (`doc_eb7cb30c59bd4f03`) or `engagement_change_order` (`doc_2d85ac5a698745c5`) which together document Acme's scope (multi-state sales tax + AR-aging bucket). Mechanism: L2 + L9 — keyword-narrow search misses the kind variants. Cite Learnings L18. Atoms verified: both Acme docs exist (`restricted` classification, both confirmed in `records_vault.rv_documents.json`). Northstar's `engagement_letter` (`doc_0036f5b991574808`) is also `restricted` — agent may need an access grant.

### Prediction 3 — Authority-figure dismissal: agent defers to Daniel-Jones "routing-fixed" claim and de-escalates (MED-HIGH confidence)

A Slack thread reply from Daniel Jones in C010 will assert the routing rule was patched last sprint. The agent who reads the dismissal and trusts it concludes "this is residual, not active" and downgrades the escalation severity. The catch: at least 8-12 of the top-aged invoices have `invoice_date` AFTER the supposed fix date, so the orphan signal is ACTIVE not residual. Mechanism: Learnings L9 (authority-figure dismissal is the highest-yield Opus 4.8 stumping mechanism on Brookfield tasks). Atoms verified: 275 pending_approval invoices over 80 days; the dismissal is planted as a thread REPLY (per L12 thread-reply blindness pattern) so agents who read only parents miss it AND agents who read it defer.

### Prediction 4 — Misses at least one age-vs-dollars trade-off vendor (MED confidence)

Despite explicit "compound rank (age × outstanding $)" framing in the prompt, the agent's prior-attempt dollar bias persists. BeaconPay VEN-033-26339 ($108,826, 320 days, account 210000, acme_cloud) is a known prior miss in 5/6 runs of the previous candidate. The new prompt's age-banding language reduces the gap but the latch is sticky. Mechanism: L1 latching + L13 first-framing trap. Atoms verified: VEN-033-26339 present in `sap_subledger.ap_invoices.json` with confirmed 320-day age at universe today 2026-06-12.

## Hardness Score

**5 / 5 — PASS.** Five load-bearing levers selected from the 11-lever catalog, each backed by verified per-task atoms. Density midpoint 47 clears the 40 floor by 7 calls. Three of four stump predictions are HIGH confidence with all referenced atoms (apinv IDs, Linear issues, RV docs) verified present in `Universe_Split/`. No Acme `engagement_letter` retrieval is required (prior R4 trap is gone — the new rubric rewards finding the addendum + change_order, which DO exist).

## Hardness Brief for the Prompt Writer

Lena Park, Procurement Officer, opens the week worried about a vendor-payment backlog she heard about secondhand — "two or three" complaints she did not log, and she now wants the picture. The prompt frames a sweep of the pending-approval queue across all three entities anchored on compound risk (age in days × outstanding dollar amount) rather than top-dollar alone, with an 80+ day critical band so high-age mid-dollar items like BeaconPay surface naturally. For the top 3 to 5 worst offenders, force per-vendor root-cause classification (orphan approval chain vs disputed deliverable vs missing credit memo) by mandating the agent cross-reference SAP (status + null-approver), Linear (existing AP-orphan or void-and-rebill issues), and email escalation history (Owen Mercer and Daniel Jones partner-sign-off threads). For any 80+ day vendor that touches Acme Cloud or Northstar Legal, force scope verification in Records Vault across THREE doc kinds — `engagement_letter`, `engagement_letter_addendum`, `engagement_change_order` — so the agent finds Northstar's executed engagement letter and Acme's addendum + change order (Acme has no plain `engagement_letter`, and reporting that as "missing" is the trap). Plant a Slack thread reply in C010 from Daniel Jones dismissing the orphan-approver issue as "already fixed last sprint" — the agent must notice that invoices dated after the supposed fix still carry `approver = null` and surface the inconsistency rather than defer. Mandate four write actions across four services: a vendor-detail Slack post to `#vendor-bills-and-ap` (C010), a Linear comment on the existing AP-routing orphan-approver issue (`issue_378874ffeb8f4cb0b0417021f2d3d647`), an email draft to Daniel Jones with Steven Perry cc'd for 80+ day partner sign-off, and a reminder for a 7-day follow-up sweep. End by deferring all approval / routing authority to Daniel Jones (primary) or Steven Perry (escalation) — Lena does not approve or route AP. Target tool-call density midpoint 47 (low 37 / high 57); the prior attempt's 32.5 failure is structurally precluded because no narrower path satisfies the 4-write × 3-vendor-chain × 2-entity-scope mandate.
