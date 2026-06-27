# REVIEW Council A — Prompt grounding sweep

**Deliverable:** `Tasks/31_6a3f7eecacba1ccbe57db14d/5_Prompt.txt`
**Source of truth:** `_aux/Universe_Split/` + persona briefs in `Brookfield_Base_Universe/2_Persona_Briefs.md`.

## A1 — Grounding sweep (per concrete claim)

| Value / claim in prompt | Verified in universe? | Source |
|---|---|---|
| Northstar Legal partnership return FY2025 | ✓ | scen_068; Northstar fiscal year is Jul-Dec; FY2025 = FP-2025-07 to FP-2025-12 |
| Hannah routed the federal return and state filings to William | ✓ | messaging conversation_scen_068_..., email_scen_068_..._0006 from Hannah |
| Partner sign-off framing | ✓ | William is "Tax Partner of record" for Northstar engagements (persona briefs) |
| Tom's draft work ties to closed year-end trial balance | ✓ | scen_068 thread; Tom prepared the package |
| Data package already in vault | ✓ | doc_03f88abe3bb5482a (Northstar Legal FY2025 Federal + State Tax-Preparation Data Package, kind tax_return, restricted) |
| Recurring lease/depreciation differences "expected book-tax items that do not require any adjustment" | ✓ | Hannah's email 0006 — this is the L9 authority dismissal anchor the agent must override on depreciation |
| State tax provision true-up needed (SALT) | ✓ | scen_068 thread; $4,820.30 amount in email 0006 |
| Late-post to closed period | ✓ | FP-2025-12 closed (locked_at 2026-01-05T12:36:07-05:00 by julia.vance@brookfieldcpas.com) |
| Authorization for posting into locked period | ✓ | William's reply 0008 contains explicit late-post authorization; precedent je_eadb3c10b2f047ee carries `late_post_authorization_id` "email_scen_063_..._0007" |
| File under tax retention | ✓ | IRS_TAX_7Y per scen_068 engagement convention (data package already filed under that code) |
| Northstar's managing partner as client signatory | ✓ | Persona briefs confirm Steven Perry (Brookfield) and Matthew Li (Brookfield) are internal partners; no external Northstar contact stored in directory (consistent with R9 evidence path-ii) |
| Tax channel | ✓ | C006 #tax-prep-and-filings (universe constant) |
| Signed authorization not back, nothing e-filed | ✓ | doc_8f821bbad10c4eb4 "Signed/E-Filed" 107-byte placeholder uploaded 2026-06-12 09:30 by Tom is contradicted by the still-open Step 3 sign-off request memo doc_f5e76056c31540bf (L1 confirm-already-done lure) |

**Grounding verdict: PASS.** Every concrete claim in the prompt grounds to a per-task universe record. No NOT_FOUND.

## A2 — Convention sweep

| Convention check | Result |
|---|---|
| Word count ≤ 500 | ✓ 382 words |
| Em-dash / en-dash absent | ✓ (validator passed) |
| No tool names | ✓ (validator passed) |
| No MCP-server names | ✓ |
| No internal IDs in prompt body | ✓ (no JE / doc / exception / vendor IDs leaked into prompt body — only natural references like "the data package", "the vault", "the tax channel") |
| First-person, natural voice | ✓ ("I want it genuinely finished", "I would rather not have it sitting past the window") |
| One coherent situation | ✓ (Northstar FY2025 partnership return sign-off) |
| Three-movement structure (trigger, context, asks) | ✓ |
| 4-5 hardness levers from playbook | ✓ (L1 confirm-already-done placeholder doc; L9 authority dismissal "recurring items net to nothing"; L7 multi-write across vault+email+slack+reminder; L2 SAP subledger derivation; L6 near-miss account-class trap on 530000) |
| 3+ writes across 3+ services | ✓ (vault upload, email send, slack post, reminder add — 4 writes across 4 services) |

**Convention verdict: PASS.** Two validator `bolt-on candidate` warns dismissed as heuristic false-positives — see `REVIEW_dismissed.md` rows 1 and 2.

## A3 — Narrative State Consistency

State-implying claims in the prompt vs universe state:

| Claim | Underlying record | Universe state | Verdict |
|---|---|---|---|
| "finally closing out Northstar Legal's FY2025 partnership return" | scen_068 thread | engagement open; Step 3 sign-off request memo doc_f5e76056c31540bf still pending | CONSISTENT |
| "Hannah has routed... to me for the partner sign-off" | email_scen_068_..._0006 | email exists in messaging, recipient = william.white | CONSISTENT |
| "the data package is already in the vault" | doc_03f88abe3bb5482a | filed under IRS_TAX_7Y, kind tax_return, classification restricted | CONSISTENT |
| "Tom's draft work ties to the closed year-end trial balance" | FP-2025-12 | status=closed, locked_at 2026-01-05 | CONSISTENT |
| "nothing has actually been released yet" | doc_8f821bbad10c4eb4 + Step 3 sign-off pending | "Signed/E-Filed" placeholder is 107-byte stub; the actual Step 3 request is still open; no posted final-return JE | CONSISTENT (the placeholder is the L1 lure, not evidence of completion) |
| "That period is already closed" | FP-2025-12 | locked 2026-01-05 by julia.vance | CONSISTENT |
| "that signed authorization is not back yet and nothing has been e-filed" | scen_068 + vault | no client-side signed authorization in vault; no e-file confirmation email | CONSISTENT |

**Narrative state verdict: PASS.** No contradictions between prompt's claimed state and universe lifecycle state.

## A4 — Action-vs-Universe-Prescription

| Prompt action | Universe record prescription | Decision |
|---|---|---|
| "work the M-1 through end to end" | scen_068 thread Tom names depreciation/SALT topics without quantifying the depreciation; the prompt overrides "no adjustment needed" framing | ACCEPT — the prompt explicitly invites overriding the recurring-no-adjustment framing ("I would rather the reconciliation be built from what the underlying records actually show than assume the recurring pieces net out to nothing"). |
| "staged against the year-end... as a proper late adjustment, with the authorization for posting into a locked period handled the way it is supposed to be" | William's email 0008 prescribes literal "DR 530000 SALT expense / CR 230000 accrued SALT payable" | ACCEPT — the prompt's "handled the way it is supposed to be rather than rushed" is an EXPLICIT instruction to apply correct judgment (which uncovers the 530000 account-class mismatch, since on Northstar 530000 = Court Filing & Expert Witness Costs, not SALT). The rubric R6 grades this realization. |
| "file the finalized return package in the vault" | data package doc_03f88abe3bb5482a already filed; placeholder doc_8f821bbad10c4eb4 is empty stub | ACCEPT — the prompt asks to file the FINALIZED package (with completed M-1), not the draft package. |
| "get the full package over to Northstar's managing partner for the client signature" | no stored external client contact for Northstar | ACCEPT — the rubric R9 accepts the role-addressed external recipient OR the Hannah-forwarded path with explicit no-contact statement. |

**Action-prescription verdict: PASS.** All deviations from universe-prescribed actions carry explicit override language in the prompt.

## A5 — Persona Authorship Whitelist

| Field | Value |
|---|---|
| Assigned persona | William White, Corporate Tax Associate |
| Persona Briefs position | William White is listed under "Tax" in `Brookfield_Base_Universe/2_Persona_Briefs.md`, valid authoring persona |
| Author tasks in | 3 (Tax) |
| Negative blocklist (NPC) | Not on the NPC list (Owen Mercer, Brenda Abbas, Sofia Halabi, Farah Dlamini, James Randall, Lucia Ferreira, Mateo Kovac) |
| Validator persona check | PASS |

**Persona authorship verdict: PASS.** William White is a valid authoring persona for Tax-category tasks; the scen_068 "Tax Partner of record" engagement role aligns with the prompt's partner sign-off framing.

## A6 — Persona Scope

The prompt uses possessive scope: "I am fairly comfortable the recurring items are just the usual treatment" / "Once the reconciliation is settled and that entry is staged". Scope is bound to William's assignment scope:
- Northstar Legal FY2025 partnership return → William is partner of record per scen_068
- M-1 / depreciation difference / SALT true-up → all attributes of the Northstar partnership return William signs off

**Persona scope verdict: PASS.** All rubric values (R1-R13) target Northstar/William scope.

## A7 — Clarity & Specificity (holistic re-read)

Reading the prompt as a first-time recipient with no context:

| Potential ambiguity | Resolution |
|---|---|
| "the figure and how you got there" — what figure? | Resolved by surrounding context: the book-tax depreciation difference (R1). |
| "the retention we use for tax work" — IRS_TAX_7Y vs FIRM_INTERNAL? | Resolved by engagement convention (existing data package doc_03f88abe3bb5482a is filed under IRS_TAX_7Y; only IRS_TAX_7Y matches "tax work"). |
| "Northstar's managing partner" — name? | Intentionally unspecified; the rubric R9 accepts role-addressed routing OR forwarding via Hannah. The lack of a name is the L9 multi-link chain forcing the agent to consult the contact directory and discover no external Northstar contact is stored. |
| "tax channel" | C006 #tax-prep-and-filings (only tax channel in the universe). |

**Clarity verdict: PASS.** No reading produces a different set of write actions. Minor ambiguities all resolve via universe lookup.

## A8 — Truthfulness deep tally

| Factual claim | Classification | Verified |
|---|---|---|
| "Hannah has routed the federal return and the state filings to me" | MAJOR | ✓ (email 0006) |
| "the data package is already in the vault" | MAJOR | ✓ (doc_03f88abe3bb5482a) |
| "Tom's draft work ties to the closed year-end trial balance" | MAJOR | ✓ (FP-2025-12 closed; Tom prepared package per persona brief) |
| "the recurring lease and depreciation differences are expected book-tax items" | MAJOR (this is the persona-relayed framing, not a fact to verify; it's the L9 anchor) | N/A — relayed claim, agent must override |
| "There is also a state tax provision true-up" | MAJOR | ✓ (scen_068 SALT shortfall $4,820.30) |
| "That period is already closed" | MAJOR | ✓ (FP-2025-12 closed) |
| "that signed authorization is not back yet and nothing has been e-filed" | MAJOR | ✓ (no signed-authorization email in vault; no posted final-return JE) |

**Truthfulness verdict: PASS.** Zero MAJOR factual errors. Zero MINOR factual errors. The "recurring items" framing is the persona's own belief (the L9 anchor the prompt is built around), not a Brookfield-claim of fact.

## A9 — Persona Fit Comparison

| Candidate | Fit | Rationale |
|---|---:|---|
| **William White (assigned)** | **5/5** | Persona briefs: William is "Tax Partner of record" for Northstar engagements (scen_068). The prompt's partner sign-off framing fits exactly. |
| Hannah Grant (Corporate Tax Senior) | 4/5 | Could plausibly route the package to herself, but the prompt is explicitly the partner-sign-off step which Hannah does NOT own. |
| Tom Chang (Tax Associate) | 3/5 | Tom is the preparer per scen_068, not the signer. Wrong role for sign-off framing. |
| Alex Cahoon (Corporate Tax Manager) | 3/5 | Wrong scenario — Alex is the IRS-liaison manager; Northstar partnership return is William's engagement role. |

**Persona fit verdict: PASS.** William is the best fit (delta = 1 vs nearest alternative). No better candidate exists for this engagement role.

## A10 — Business Function Match

| Field | Value |
|---|---|
| Assigned business function | Tax |
| Prompt primary scenario | FY2025 partnership return (Form 1065) + Schedule M-1 + state filings + SALT provision true-up + e-file authorization |
| Match | TRUE (Tax category covers annual returns, partnership tax, IRS liaison, etc.) |

**Business function verdict: PASS.**

## A11 — End-to-End Solvability

Walked the dependency chain:
1. Read emails (email_scen_068_..._0006, _0008) → ✓ in messaging
2. Read Slack thread (cb20bc3f303b5aeb93b72be8a18c6137, 14c2397fa6d858669e5b3312c02b0ce1) → ✓ in slack_messages
3. Read messaging kickoff (conversation_scen_068_...) → ✓
4. Read vault documents (doc_03f88abe3bb5482a data package; doc_212b1dffc93d4968 Step 1 sign-off; doc_f5e76056c31540bf Step 3 request; doc_8f821bbad10c4eb4 premature placeholder) → ✓ in rv_documents
5. Get fiscal period (northstar_legal_FP-2025-12) → ✓ in ogl_fiscal_periods (closed)
6. Find late-post precedent (je_eadb3c10b2f047ee with late_post_authorization_id) → ✓ in ogl_journal_entries
7. List fixed assets (14 IT assets, account 150200, FY2025 in-service) → ✓ in fixed_assets
8. Get depreciation schedules (FY2025 periods FP-2025-07 to FP-2025-12) → ✓ in depreciation_schedule
9. Compute M-1 difference → derivable
10. Validate SALT account class (530000, 230000 on northstar_legal) → ✓ in ogl_accounts
11. Attempt closed-period JE create → blocked by oracle_gl with OGL.PERIOD_CLOSED
12. Upload finalized vault doc → ✓ records_vault_upload_document available
13. Send email to external client → ✓ email_send_email available; rubric accepts forwarding via Hannah
14. Post slack to C006 → ✓ slack_conversations_add_message
15. Set reminder → ✓ reminder_add_reminder

**End-to-end solvability verdict: PASS.** Every step has materialized source data. Run #2 empirically achieved 13/13.

## Council A — Prompt verdict

**GO.** All A1-A11 perspectives pass. Two validator `bolt-on candidate` warns dismissed as heuristic false-positives. No grounding gaps, no convention drift, no narrative-state contradictions, no action divergences, persona valid, scope clean, no clarity gaps, zero truthfulness errors, persona fit appropriate, business function matches, end-to-end solvable.

```json
{
  "phase": "prompt",
  "council": "A",
  "task_dir": "Tasks/31_6a3f7eecacba1ccbe57db14d",
  "verdict": "GO",
  "perspectives": {
    "A1_grounding": { "status": "PASS", "findings": [] },
    "A2_convention": { "status": "PASS", "findings": [] },
    "A3_narrative_state": { "status": "PASS", "findings": [] },
    "A4_action_universe": { "status": "PASS", "findings": [] },
    "A5_persona_whitelist": { "status": "PASS", "findings": [] },
    "A6_persona_scope": { "status": "PASS", "findings": [] },
    "A7_clarity": { "status": "PASS", "findings": [] },
    "A8_truthfulness": { "status": "PASS", "findings": [] },
    "A9_persona_fit": { "status": "PASS", "findings": [] },
    "A10_business_function": { "status": "PASS", "findings": [] },
    "A11_solvability": { "status": "PASS", "findings": [] }
  },
  "iteration": 1,
  "timestamp": "2026-06-27T00:00:00Z"
}
```
