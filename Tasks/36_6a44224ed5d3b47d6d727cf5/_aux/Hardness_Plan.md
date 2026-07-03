# Hardness Plan — Task 36

## Persona and Business Function
- **Persona:** Julian Brooks — Lead Customer Support Specialist
- **Business function:** Customer Engagement (MoveOps 30% weight)
- **Universe:** MoveOps (V2.1 framework · universe today 2026-04-26 · no Oracle GL / no SAP subledger / no BlackLine / no Records Vault)

## Levers Available

Per-lever presence in `_aux/Universe_Split/`. Cost ranges from `Reference/Hardness_Playbook.md`.

| # | Lever | Status | Evidence (file:record_id or excerpt) | Cost range |
|---|---|---|---|---|
| L1 | Confirm-already-done | avoid | Julian's April threads all show `In Progress` / open. No clean L1 anchor and per Learnings L1 = 100% pass. | n/a |
| L2 | Structured-DB skip (MoveOps analog = Airtable / QB / CRM engagement) | **yes** | `airtable.records.recSimoneRichterBrightloop.Special Requirements` — silent on unit type (says "2 weeks furnished temp housing," no "1BR" or "studio"); `crm.crm_engagements.engagement_brightloop_apr2026_relocations` — silent on unit type; `quickbooks.invoices.1008 = INV-2026-0308, $11,350` — batches Simone + Marcus and is the credit-math surface Julian would never open (off-domain for Customer Support Lead). | 4–6 |
| L3 | Two keyword-searchable reductions | partial | Achievable but per L3 = ~60% pass (weak alone). | n/a |
| L4 | Near-miss entity confusion alone | avoid | Present for free (3× Marcus Webb — `brightloopanalytics.com` + `m.webb@ironcladsec.com` + `marcus.webb.lab@gmail.com`; 2× Simone Richter — BrightLoop apartment recovery vs StormCloud PMM per `entities_personas.md`), but per L4 alone = ~0% fail — cannot be standalone. Included as secondary attribution risk. | n/a |
| L5 | Action-incompleteness alone | avoid | Per L5 = ~0% fail. | n/a |
| L6 | Correction email stating answer | must-not | Per L6 = 100% pass — the correct answer must NEVER appear verbatim in any artifact. | design guardrail |
| L7 | Binary "is it posted?" | avoid | Per L7 = 100% pass. | n/a |
| L8 | Three reductions across three services | **yes** (emergent) | Simone recovery answer requires: (a) `airtable.records.recSimoneRichterBrightloop` unit silent → (b) `email.emails.email_email_ab2391d62ab1` Julian's outbound to Carmen — Carmen's reply DOES NOT EXIST YET → (c) `quickbooks.invoices.1008 = INV-2026-0308 = $11,350` for credit math. Genuine 3-service triangulation across Airtable + email + QuickBooks. | 5–7 |
| L9 | Authority-figure dismissal (soft verbs per L24) | **yes** | `slack.slack_messages ts 1776298200` C007 — Julian himself: *"Sounds right. If Airtable is showing completed/confirmed, just send him a quick acknowledgment and leave it in the queue."* Persona self-anchor telling the agent to trust Airtable Status. Reinforced by Mina Hashimoto's `C002 ts 1776997200` audit: *"our system picture is misleading. CRM still reads like the BrightLoop April relocations were basically completed"* — the agent will side with Julian's own soft-verb voice. | 3–5 |
| L10 | SAP subledger invisibility (MoveOps analog = QB bills) | partial | `quickbooks.bills.bill_heartland_q1_2026 = $12,800` (dup-hold pattern) — completely off-domain for Customer Support; secondary buffer only. | 3–5 (bundled) |
| L11 | Structured-source vs conversation skip | **yes** (bundled with L2) | Rich Slack/email chatter (`C002` 4/23 Mina audit + Julian "Drafted and sent") tempts the agent to write from chatter without touching `airtable.recSimoneRichterBrightloop` or `crm_engagements`. Same mechanism as L2 in MoveOps context. | (bundled) |
| L12 | Thread-reply invisibility | partial | Julian's `C007 ts 1777011000` "I'm taking the two BrightLoop misses" has zero replies (dead thread — orphan). Better used as an L26 decoy candidate than as an L12 anchor. | (bundled with L26) |
| L13 | First-framing trap | **yes** (bundled with L25) | Julian's 4/23 email to Simone (`email.emails.email_email_6d0501ac647f`) sets first-framing "send an update" — hiding that Carmen has not replied yet with the UrbanNest facts. | (bundled) |
| L14 | Correct-observation / wrong-conclusion | **yes** (bundled with L9) | Airtable `recSimoneRichterBrightloop.Status = "In Progress"` (correct observation) → agent concludes "still active, just needs a check-in" (wrong conclusion; the actual state is Airtable-silent on unit type + no vendor reply + credit unquantified). | (bundled) |
| L23 | Dollar-threshold filter blindness | partial | `quickbooks.invoices.1008` $11,350 BrightLoop + `1005` $10,000 BrightLoop — usable but not the strongest fit for a Customer Support ask. | (bundled with L2) |
| L24 | Verb-tense sensitivity | apply | Soft verbs ("looks like," "sounds right," "I think we're good") in the Julian voice so L9 lands cleanly and does not spike Truthfulness risk. | (applies to L9) |
| L25 | Existing-output anchor trap | **yes — HIGHEST yield** | `email.emails.email_email_6d0501ac647f` = Julian → Simone 4/23 (apology + promise, NOT factual delivery); `email.emails.email_email_bedc44dbea30` = Julian → Marcus Webb 4/23 (same pattern); `email.emails.email_email_ab2391d62ab1` = Julian → Carmen Reyes 4/23 with six factual questions — Carmen's reply does not exist yet. Agent will latch on the 4/23 template as "already answered." Per L25 = highest-yield novel stump on this pipeline. | 4–6 |
| L26 | Decoy parent thread | **yes** | 4 competing Julian-adjacent parents late April: (a) `C007 ts 1777011000` Julian "I'm taking the two BrightLoop misses" (orphan, zero replies); (b) `C002 ts 1777012200` Julian "Drafted and sent both employee replies" (Mina CC'd); (c) `C002 ts 1776997200` Mina Hashimoto "BrightLoop audit" (the audit thread the response actually needs to close); (d) `C007 ts 1777116900` Julian "Context on the StormCloud credit issue" (different topic, same channel + voice). | 4–6 |
| L27 | Soft-instruction over-compliance | avoid | Not needed — density is load-bearing without this. | n/a |
| L28 | Tool-variant trap | partial | MoveOps analog = `airtable_update_records` vs `airtable_create_records` on `tblRelocations01`. Real risk, folds naturally under L2. | (bundled) |
| L29 | Escape-valve neutralizes L2 | must-not | Do NOT include escape-valve clauses ("if not visible, proceed anyway") — L2 is load-bearing. | design guardrail |

## Selected Levers (4 primary + emergent L8 anatomy)

### Lever A — L25 Existing-Output Anchor Trap (HIGHEST yield)
- **Rationale (per L25):** Julian ALREADY sent Simone + Marcus recovery replies on 4/23 — but both are apology + promise, not the factual delivery. Planting a superficially-matching artifact that lacks rubric-tested fields (UrbanNest booked-vs-delivered unit type, credit posture, hard-transfer availability, next factual checkpoint) is the highest-yield stump.
- **Attach records:** `email.emails.email_email_6d0501ac647f` (Julian → Simone 4/23); `email.emails.email_email_bedc44dbea30` (Julian → Marcus Webb 4/23); `email.emails.email_email_ab2391d62ab1` (Julian → Carmen Reyes 4/23 UrbanNest ask — CARMEN'S REPLY DOES NOT EXIST YET).
- **Projected cost midpoint:** 5 calls.
- **Failure mechanism:** agent paraphrases Julian's 4/23 apology-then-promise back to Simone/Marcus as the "status update," missing all rubric-required fields.

### Lever B — L9 Authority Dismissal (persona self-anchor, verb-soft per L24)
- **Rationale (per L9 = ~100% fail):** Julian's OWN 4/22 C007 reply to Omar Ibrahim is a persona-self-authority anchor telling the agent to trust Airtable Status and not dig into Special Requirements. Mina's 4/23 audit that the system picture is "misleading" is present but will be discounted because Julian's own voice is the persuasive framing.
- **Attach records:** `slack.slack_messages ts 1776298200` (Julian's persona-belief anchor); `slack.slack_messages ts 1776997200` (Mina audit, secondary).
- **Projected cost midpoint:** 4 calls.
- **Failure mechanism:** agent reads `airtable.recSimoneRichterBrightloop.Status = "In Progress"` (correct observation, L14 shell), concludes "still active, needs a check-in" (wrong conclusion) — never reads Special Requirements, never checks Carmen's reply status.

### Lever C — L26 Decoy Parent Thread
- **Rationale (per L26 = 80%+ failure on canonical thread_ts):** 4 competing candidate parents for the "BrightLoop recovery status" post. Julian's own dead C007 parent is the tempting orphan; the canonical target should be Mina's C002 audit thread (the audit the response must close) or Chloe's ops chain.
- **Attach records:** `slack.slack_messages ts 1777011000` (Julian C007 "I'm taking the two BrightLoop misses" — orphan); `ts 1777012200` (Julian C002 "Drafted and sent"); `ts 1776997200` (Mina C002 audit — canonical target candidate); `ts 1777116900` (Julian C007 StormCloud context — distractor).
- **Projected cost midpoint:** 5 calls.
- **Failure mechanism:** agent posts to Julian's own dead parent (self-answering) OR to a fresh unstubbed parent, when the rubric-canonical target is Mina's audit `1776997200`.

### Lever D — L2 MoveOps Airtable-silence + QuickBooks-invoice skip
- **Rationale (per L2 + MoveOps translation per HARDNESS runbook):** The "1BR promise" and "studio delivered" claim lives ONLY in email/Slack chatter. The Airtable Special Requirements field is silent on unit type. The CRM engagement note mentions area but not unit type. The credit-math surface is a QuickBooks invoice completely off-domain for a Customer Support Lead.
- **Attach records:** `airtable.records.recSimoneRichterBrightloop` (Special Requirements silent on unit type); `crm.crm_engagements.engagement_brightloop_apr2026_relocations` (silent on unit type); `quickbooks.invoices.1008 = INV-2026-0308` ($11,350 batched Simone + Marcus).
- **Projected cost midpoint:** 5 calls.
- **Failure mechanism:** agent trusts email/Slack chatter as SSOT for the unit-type claim, never queries Airtable Special Requirements or QB invoice for the factual scaffolding of a credit / transfer-cost answer.

### Emergent — L8 Three-Service Reduction (natural byproduct of A + D stacked)
- The truthful recovery answer requires (i) Airtable relocation record + Special Requirements read → (ii) email UrbanNest thread + verification Carmen has NOT replied → (iii) QuickBooks invoice INV-2026-0308 for credit-math base. Per L8 = ~40% pass — the target failure mode.
- **Projected cost midpoint:** 5 calls (cross-service triangulation buffer beyond individual Lever D reads).

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---:|
| Base discovery (contacts, initial Airtable list, email inbox scan, persona context) | 6–8 | 7 |
| Lever A — L25 (re-read Julian's 3 existing 4/23 outbounds + Carmen no-reply verify) | 4–6 | 5 |
| Lever B — L9 (Julian 4/22 self-anchor + Mina 4/23 audit + Airtable Status read) | 3–5 | 4 |
| Lever C — L26 (channel list + message enumeration + parent selection attempts) | 4–6 | 5 |
| Lever D — L2 (Airtable Special Requirements + CRM engagement + QB invoice) | 4–6 | 5 |
| Emergent L8 cross-service triangulation buffer | 4–6 | 5 |
| Write actions (email × 2 + Slack post + Airtable update × 2 + CRM engagement update + Linear comment + optional calendar hold + internal status email) | 9–13 | 11 |
| Cross-service verification buffer (contact re-check for 3-way Marcus Webb disambiguation, thread parent verify, invoice cross-ref) | 7–9 | 8 |
| **TOTAL projected** | **41–59** | **50** |

**Gate:** midpoint **50 = PASS** (design target ≥ 50). Range 41-59 clears the THIN floor of 40 even in the conservative case; the 50 midpoint sits AT the PASS threshold — S1 must be sized to include ALL the write actions the plan sketches to hit this reliably. If the S1 prompt is written such that the agent could reasonably skip the internal status email or the calendar hold, the projection drops to ~45 midpoint (THIN). Document any write-action trimming under the S1 phase.

## Service Breadth (v11 G1)

| Service | Calls | % of 50 midpoint | Basis |
|---|---:|---:|---|
| email | 12 | 24% | Simone thread + Marcus Webb Road Runner thread + Carmen/UrbanNest thread + Chloe ops-gaps + Mina audit thread + write × 2 |
| slack | 10 | 20% | C002 Mina audit + C002 Julian status + C007 Julian misses parent + C007 Omar/Julian Jae-won anchor + C006 Chloe ops + write |
| airtable | 7 | 14% | `recSimoneRichterBrightloop` + `recMarcusWebbBrightloop` + tblClientAccts BrightLoop + tblStipends BrightLoop + updates × 2 |
| crm | 5 | 10% | `engagement_brightloop_apr2026_relocations` + BrightLoop company + contact Simone + contact Marcus + write engagement |
| linear | 4 | 8% | `linear_issue_f85be674c9b8` Chloe BrightLoop ops gaps + `linear_issue_c16357d188c6` Mina audit + comment |
| contacts | 4 | 8% | Simone Richter + Marcus Webb (3-way identity disambiguation) + Carmen Reyes + Julian |
| quickbooks | 4 | 8% | invoice INV-2026-0308 + customer BrightLoop + optional bill lookup + vendor UrbanNest |
| calendar | 2 | 4% | Follow-up hold |
| calendar/other | 2 | 4% | (buffer) |
| **Distinct services with ≥ 5%** | **7** | | |

**Breadth gate:** 7 distinct services ≥ 5% (email 24%, slack 20%, airtable 14%, crm 10%, linear 8%, contacts 8%, quickbooks 8%); dominant service (email) is 24%, well under 60%. **PASS.** No structural lever-thinness — cross-service triangulation is intrinsic to the persona role (Customer Support Lead closing a recovery must touch Airtable relocation state, email/Slack chatter, CRM engagement, and QB credit math).

## Stump Hypothesis (4 predictions)

1. **[HIGH]** Opus 4.8 will re-use Julian's 4/23 apology-then-promise template (`email_email_6d0501ac647f`) as the "status update," producing a message that acknowledges silence and promises follow-up but never delivers the rubric-tested factual scaffolding (UrbanNest booked-vs-delivered unit type; credit posture against INV-2026-0308; hard-transfer availability; next concrete checkpoint). **Mechanism: L25 existing-output anchor.** Julian's own outbound to Carmen (`email_email_ab2391d62ab1`) enumerates the six required facts — but Carmen has not replied — the agent will paraphrase Julian's questions back to Simone as if they were answers.

2. **[HIGH]** Opus 4.8 will trust Julian's own 4/22 C007 self-anchor (*"If Airtable is showing completed/confirmed, just send him a quick acknowledgment"*, ts `1776298200`) and read only `airtable.recSimoneRichterBrightloop.Status = "In Progress"` — never opening Special Requirements, never noting the unit-type field is silent, never quantifying credit against `quickbooks.invoices.INV-2026-0308 = $11,350`. **Mechanism: L9 authority dismissal (persona self-anchor) + L14 correct-observation-wrong-conclusion.** Per L9 ≈ 100% fail; Julian's own voice is the most persuasive framing the agent will encounter.

3. **[MED]** The Slack recovery-status post will attach to the WRONG parent — Julian's own dead `C007 ts 1777011000` "I'm taking the two BrightLoop misses" (orphan, self-answering) OR to a fresh no-parent post, when the rubric-canonical target is Mina's `C002 ts 1776997200` BrightLoop audit parent (the audit that must be closed). **Mechanism: L26 decoy parent thread.** Per L26 = 80%+ failure on canonical thread_ts.

4. **[MED]** Opus 4.8 will conflate the three Marcus Webbs (`marcus.webb@brightloopanalytics.com` for BrightLoop recovery, `m.webb@ironcladsec.com` for Ironclad, `marcus.webb.lab@gmail.com` for standalone) and address the Marcus recovery follow-up to the wrong email — or fold the two Simones (BrightLoop apartment recovery vs StormCloud PMM) together. **Mechanism: L4-adjacent name-collision (secondary to L9, not standalone).** Per persona-attribution auto-memory, this is the recurring landmine on multi-Marcus threads; S3 grounding + AUDIT must grep both candidate addresses before latching.

## Hardness Score

**4/5 — PASS**

Four primary levers grounded in per-task records; emergent L8 three-service chain naturally stacks from Lever A + Lever D; density midpoint 50 clears the ≥ 50 design target (range 41–59, conservative baseline 41 also clears the 40 THIN floor); service breadth 7 distinct services with ≥ 5% (4-service gate cleared with wide margin, dominant email 24% << 60%). L1 / L6 / L7 must-not anti-patterns respected. L29 escape-valve guardrail respected (do NOT include invitations to surface contradictions — L2 is load-bearing). MoveOps landmines (Marcus Webb 3-way identity, Simone 2-way identity, Airtable-vs-CRM SSOT) surfaced but treated as secondary attribution risks rather than standalone levers, per Learnings "L4 alone = 0% fail" guidance.

## Hardness Brief for the Prompt Writer

Author a Julian Brooks recovery-close prompt anchored on the BrightLoop April cohort (Simone Richter apartment mismatch + Marcus Webb vehicle-shipping ETA). The prompt must land four stacked levers: **L25 existing-output anchor** — Julian's own 4/23 emails to Simone/Marcus were apology + promise, not factual delivery; the agent must not re-use the template as the answer. **L9 authority self-anchor with soft verbs (per L24)** — Julian believes his 4/23 replies "closed the loop" and that Airtable `Status = In Progress` plus the AM's audit are enough; implicit-only, no investigation prompt (per L15). **L26 decoy parent thread** — 4 competing Slack parents (Julian's own C007 "I'm taking the two BrightLoop misses," Julian's C002 "Drafted and sent," Mina's C002 audit, Chloe's ops chain); the canonical attach target must be inferable but non-obvious. **L2 Airtable-silence + QuickBooks-invoice skip** — unit-type claim lives only in email/Slack chatter; Airtable Special Requirements and QB invoice INV-2026-0308 for $11,350 are the SSOT for the factual answer + credit posture. Voice: Julian is Lead Customer Support Specialist asking for execution of what he thinks is already-in-flight closure — soft verbs ("looks like," "sounds like," "I think we're good on Simone once I send the update"), no reference to Learnings or Playbook artifacts, no escape-valve clauses (per L29). Density target: 50+ midpoint. Predicted failure: send-to-client message paraphrases Julian's own 4/23 apology; Slack post attaches to the wrong parent; Airtable Special Requirements and QB invoice stay untouched. Guardrail: DO NOT plant the derived answer (unit type / credit dollars / transfer availability) verbatim in any email/Slack/Airtable body (per L6).
