# AUDIT (STRICT) — S2 OE Task 36

Universe: **moveops** (V2.1 framework). Universe today = 2026-04-26 (US/Pacific). Model under test = Opus 4.8.
Interpretation: strictest possible reading of `Evals_moveops/2_Oracle_Events_Eval.md` + `Docs_moveops/1_Prompt_QC_Guidelines.md` (OE dimension) + `Reference/OE_Format.md`. Density bar 50+ midpoint (STRICT). Every "should" reads as "must". Every OE step must trace end-to-end to a prompt sentence AND to a Fact_Ledger / Universe_Split atom.

## Verdict: **REVISE**

Two in-place defects surface under STRICTEST reading. Neither is REBUILD-class. Both are fixable inside the OE file without touching the prompt.

**Blocking (under STRICT):**
- **[BLOCKER-STRICT] OE 7 folder_name = "INBOX" is factually wrong** on BOTH email records. Universe verification: `email_email_ca010e9c9446` is `folder = SENT`; `email_email_87f575fcacf9` is also `folder = SENT`. If the Email MCP scopes `get_email_by_id` by `folder_name`, the tool call fails to return either record — the OE is not executable as written. If the tool ignores `folder_name` when `email_id` is provided, the OE still contains a documented factual defect (STRICT auto-fails Accuracy on any per-atom mislabel).
- **[BLOCKER-STRICT] Density midpoint under STRICT no-buffer count = 37, below the 40 THIN floor and 13 short of the 50 STRICT bar.** With a realistic cross-service verification buffer of ~10 calls, midpoint lifts to ~47 (THIN band per AGENTS.md rule 11). Under STRICT AUDIT lens 4 (bar 50+, no generosity), this fails.

Both are per-OE fixes (change one parameter value; add 3–5 forced probes distributed across OE 5 / OE 8 / OE 12). Task remains at REVISE, not REBUILD.

## QC scoring under STRICT interpretation

Scored against `Docs_moveops/2_Rubrics_V3_Guidelines.md` OE dimension and `Evals_moveops/2_Oracle_Events_Eval.md`. No NON-FAIL middle band invoked. Every "should" read as "must".

| Sub-dim | Score | Basis |
|---|---:|---|
| **OE Completeness** (forward-map from every prompt ask to at least one OE) | **5/5** | Council B B1 forward map covers all 14 explicit + implicit asks; independently reverified in Lens 7 below. |
| **OE Accuracy** (per-atom record ID / parameter / body fidelity) | **3/5** | OE 7 folder_name mismatch on two records + OE 12 wording of `thread_ts_legacy` as prose (Council A already surfaced) + density THIN under STRICT no-buffer. Under STRICTEST, one hard defect + one prose defect + density-shortfall combine to 3/5 on Accuracy. |

## Per-lens findings

### Lens 1 — Per-atom evidence table

Universe atoms independently re-verified via python queries into `_aux/Universe_Split/*.json`.

| OE | Atom | Source file | Verified? | PASS/FLAG |
|---|---|---|---|---|
| 1 | `julian.brooks@moveops.com` (moveops_julian_brooks) | contacts.contacts.json | ✓ | PASS |
| 1 | `mina.hashimoto@moveops.com` (moveops_mina_hashimoto) | contacts.contacts.json | ✓ | PASS |
| 2 | `email_email_6d0501ac647f` (Julian → Simone 4/23; parent_id = `email_email_b6ce20dc2587`; folder SENT; content confirmed "apology + promise, not delivery"; ts 2026-04-23T16:24:00+00:00) | email.emails.json | ✓ | PASS |
| 3 | `email_email_b6ce20dc2587` (Simone → Mina 4/8; folder INBOX; is_read=False; parent_id=null; ts 2026-04-08T17:14:00+00:00; content confirms "one-bedroom … placed in a studio") | email.emails.json | ✓ | PASS |
| 4 | `email_email_ab2391d62ab1` (folder SENT; sender=carmen.reyes@urbannestsolutions.com [ANOMALY]; recipients_json=["carmen.reyes@urbannestsolutions.com"] [SELF-LOOP]; cc mina + chloe; body "Hi Carmen…" signed Julian; 6 questions verified verbatim in body) | email.emails.json | ✓ | PASS (anomaly handled correctly) |
| 5 | Absence of Carmen INBOX reply on the six-question subject | email.emails.json | ✓ (grep for inbound from `@urbannestsolutions.com` on the Simone-unit-type subject returns 0 rows) | PASS |
| 6 | `email_email_bedc44dbea30` (Julian → Marcus 4/23; parent_id = `email_email_ca010e9c9446`; folder SENT; ts 2026-04-23T16:18:00+00:00; content confirms "apology + promise 2 PM PT") | email.emails.json | ✓ | PASS |
| 7 | `email_email_ca010e9c9446` — cited as `folder_name "INBOX"` but actual folder = **SENT** | email.emails.json | ✓ record exists; **folder param wrong** | **FLAG (Blocker-STRICT)** |
| 7 | `email_email_87f575fcacf9` — cited as `folder_name "INBOX"` but actual folder = **SENT** | email.emails.json | ✓ record exists; **folder param wrong** | **FLAG (Blocker-STRICT)** |
| 8 | `email_email_a3ca1b6dd238` (Road Runner delay; folder INBOX; is_read=False; sender=dispatch@roadrunnerautotransport.com; recipient=blessing.okafor@moveops.com [shared workspace]; content confirms "Indianapolis transfer hub", "April 18-20", "no driver replacement") | email.emails.json | ✓ | PASS |
| 9 | `appMoveOpsOps001` (base) + `recSimoneRichterBrightloop` (fields verified: Status=In Progress, Origin=Chicago→Boston, Coordinator=Suki Patel, Special Requirements says "URGENT — lease ends April 6. 5-day turnaround. Employee needs 2 weeks furnished temp housing on arrival in Boston. Rush surcharge applies. Expedited packing scheduled April 4-5." — **SILENT ON UNIT TYPE** as claimed) | airtable.bases.json + airtable.records.json | ✓ | PASS |
| 10 | `recMarcusWebbBrightloop` (Status=In Progress, Origin=Atlanta→Boston, VIN 2HGFC2F53KH123456, Road Runner ~$1,100; Special Requirements silent on Indianapolis-stall / April 18-20 window) | airtable.records.json | ✓ | PASS |
| 11 | QB invoice `1008` = DocNumber INV-2026-0308; TotalAmt 11350; TxnDate 2026-04-02; DueDate 2026-05-02; CustomerRef cust_brightloop; BillEmail tessa.moreno@brightloopanalytics.com; **5 line items sum to exactly $11,350**: $4500 + $750 + $4500 + $1100 + $500. Per-employee decomposition Simone $5,250 (4500+750) + Marcus $5,600 (4500+1100) + Platform $500 = $11,350 exact. | quickbooks.invoices.json | ✓ | PASS |
| 12 | Slack parent ts `1776997200.000000` on channel_id `C002` (=customer-engagement); user=moveops_mina_hashimoto; thread_ts=null (**parent, not reply**); content opens "I just did a BrightLoop audit after Tessa's expansion note and we have a real exposure here. The April batch is not actually clean." — verbatim match | slack.slack_messages.json + slack.slack_channels.json | ✓ | PASS (see Lens 9 for `thread_ts_legacy` wording nit) |
| 13 | Same parent as OE 12; `conversations_replies` param binding correct | slack.slack_messages.json | ✓ | PASS |
| 14 | `linear_issue_f85be674c9b8` (title matches; assignee=moveops_chloe_vance; team=team_operations; due_date=2026-04-22; **labels=null**, OE claims "labels brightloop plus service-recovery" — advisory only) | linear.linear_issues.json | ✓ record; labels claim mismatched (see advisories) | PASS on ID, FLAG on labels claim (non-blocking) |
| 15 | `linear_issue_c16357d188c6` (Mina audit issue; assignee=moveops_mina_hashimoto; team=team_operations; due=2026-04-22) | linear.linear_issues.json | ✓ | PASS |
| 16 | `engagement_brightloop_apr2026_relocations` (NOTE type; body silent on unit type as claimed) | crm.crm_engagements.json | ✓ | PASS |
| 17 | `contact_brightloop_simone_richter` (BrightLoop primary Simone) | crm.crm_contacts.json | ✓ | PASS |
| 17 | `contact_brightloop_marcus_webb` (BrightLoop primary Marcus) | crm.crm_contacts.json | ✓ | PASS |
| 17 | `contact_brightloop_hr` = Tessa Moreno | crm.crm_contacts.json | ✓ | PASS |
| 17 | Reject `simone.richter@stormcloud.io` (contacts_contact_4d531c818e2a) | contacts.contacts.json | ✓ decoy exists | PASS |
| 17 | Reject `m.webb@ironcladsec.com` (contact_ironclad_001 / ext_prospect_ironclad) | crm.crm_contacts.json + contacts.contacts.json | ✓ decoy exists | PASS |
| 17 | Reject `marcus.webb.lab@gmail.com` (contact_canopy_marcus_webb) | crm.crm_contacts.json | ✓ decoy exists | PASS (added post-revision) |
| 17 | Reject `marcus.thorne@moveops.com` (moveops_marcus_thorne, Head of Finance) | contacts.contacts.json | ✓ decoy exists | PASS |
| 17 | Reject `carmen.delgado-reyes@palmettofoundation.org` (contacts_contact_03800e48b5a4) | contacts.contacts.json | ✓ decoy exists | PASS (added post-revision) |
| 17 | Bind `contacts_contact_00589cf8404a` (Carmen @ UrbanNest) | contacts.contacts.json | ✓ | PASS (see Lens 6 duplicate note) |
| 20 | `airtable_update_records` target: base_id=appMoveOpsOps001, table_id=tblRelocations01, record_id=recSimoneRichterBrightloop | airtable.bases.json + airtable.tables.json + airtable.records.json | ✓ | PASS |
| 22 | same as OE 20 for Marcus record | same | ✓ | PASS |
| 23 | thread_ts `1776997200.000000` exact match | slack.slack_messages.json | ✓ | PASS |
| 24 | issueId `linear_issue_f85be674c9b8` | linear.linear_issues.json | ✓ | PASS |
| 24 | Batch total $11,350 with per-employee decomposition $5,250 / $5,600 / $500 | quickbooks.invoices.json | ✓ | PASS |
| 25 | company_ids [company_brightloop] + contact_ids [contact_brightloop_hr] | crm.crm_companies.json + crm.crm_contacts.json | ✓ | PASS |
| 26 | Attendee `julian.brooks@moveops.com`; datetimes 2026-04-28T16:30:00-07:00 → 17:00:00-07:00 (US/Pacific PDT for late April) | contacts.contacts.json + AGENTS.md registry | ✓ | PASS |
| 27 | Recipient `mina.hashimoto@moveops.com`; sender `julian.brooks@moveops.com`; no external cc | contacts.contacts.json | ✓ | PASS |

**Lens 1 summary:** 32 verified atoms PASS; 2 atoms FLAG (OE 7 folder_name on both records); 1 non-blocking mismatch (OE 14 labels).

### Lens 2 — Prompt-sentence mapping

Every OE traces to a specific prompt sentence. Reverse map re-verified from `5_Prompt.txt`.

| OE | Prompt sentence anchor | PASS/FLAG |
|---|---|---|
| 1 | Foundational (sender identity + cc target for every outbound) — implicit from "Email her back, cc Mina" + "cc Mina" (Marcus arm) + "send Mina a short internal email" | PASS |
| 2 | "Both went out the door as apologies with promises attached, not actual answers" | PASS |
| 3 | "The truth of what we actually promised her and what got booked" | PASS |
| 4 | "I asked Carmen six specific questions Thursday and I do not remember an answer coming back" | PASS |
| 5 | "If she still owes us one, escalate plainly by email, do not just send another gentle nudge" — the verification that "she still owes us one" is the OE 5 predicate | PASS |
| 6 | "I promised him a fresh carrier status Thursday afternoon and never sent it" | PASS |
| 7 | Marcus arm prior-silence chain (both records) — "I promised him … and never sent it" + implicit "you have not been given a real answer" context | PASS |
| 8 | "Get the current position from Road Runner" | PASS |
| 9 | "Update her Airtable placement record so anyone reading it can see this is live and not resolved" (read-then-write) | PASS |
| 10 | "Reflect the actual state on his Airtable placement record" (read-then-write) | PASS |
| 11 | "The finance side of these two moves is not something I can answer with feelings on Wednesday" + "what the money impact looks like on the batch" | PASS |
| 12 | "Put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post" | PASS |
| 13 | Verifies no Julian status has already landed — supports "not in a fresh post" and "so it stops reading like … done" | PASS |
| 14 | "Add a Linear comment on the BrightLoop operational issue" | PASS |
| 15 | Sister audit issue — framing context for the operational issue. **STRICT flag risk (borderline scope-creep)**: prompt says "the BrightLoop operational issue" (singular); OE 15 pulls a second Linear record. Purpose is to disambiguate correct target vs Mina's account-audit issue, so retention is defensible. | PASS (advisory only) |
| 16 | "Update the BrightLoop engagement on our CRM so it stops reading like the April cohort is basically done" (read-before-create-only tool) | PASS |
| 17 | Foundational (recipient disambiguation before every write) — implicit from Simone/Marcus/Carmen naming | PASS |
| 18 | "Email her back, cc Mina" + "Simone needs a real answer today, not another 'reviewing your file' note" | PASS |
| 19 | "Escalate plainly by email, do not just send another gentle nudge" | PASS |
| 20 | "Update her Airtable placement record so anyone reading it can see this is live and not resolved" | PASS |
| 21 | "Email him a concrete next checkpoint, cc Mina" + "If the carrier still cannot give a hard delivery date, say that. Do not soften it" | PASS |
| 22 | "Reflect the actual state on his Airtable placement record" | PASS |
| 23 | "Put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post" | PASS |
| 24 | "Add a Linear comment on the BrightLoop operational issue that captures where each employee stands and what the money impact looks like on the batch" | PASS |
| 25 | "Update the BrightLoop engagement on our CRM so it stops reading like the April cohort is basically done" | PASS |
| 26 | "Hold thirty minutes on my calendar late Tuesday to recheck Simone's housing outcome" | PASS |
| 27 | "Send Mina a short internal email pulling the whole position together in one place" | PASS |

**Lens 2 summary:** 27/27 OEs map to prompt sentences. Zero unanchored OEs. Zero scope creep beyond OE 15 defensible-context advisory.

### Lens 3 — Hardness lever preservation

Cross-referenced against `_aux/Hardness_Plan.md` selection (L25 / L9 / L26 / L2 primary + emergent L8).

| Lever | Design | Exercised by OE(s) | Preserved end-to-end? |
|---|---|---|---|
| **L25 existing-output anchor** (highest-yield stump) | Julian's own 4/23 outbounds were apology + promise, not delivery — agent must not paraphrase them as "the answer" | OE 2 (Julian → Simone re-read; explicit "cannot be re-used as the recovery answer") + OE 4 (Julian → Carmen re-read; six Qs still open) + OE 6 (Julian → Marcus re-read; explicit "promise, not delivery") + OE 18 body constraint ("Do not paraphrase Julian's 4/23 apology. This message is the factual delivery, not another promise") | **PASS** — lever lands hardest; three explicit "promise-not-delivery" conclusions across the read chain + one hard write-side constraint |
| **L9 authority self-anchor (soft verbs per L24)** | Julian's own 4/22 C007 voice "If Airtable is showing completed/confirmed, just send him a quick acknowledgment" tells the agent to trust `Status = In Progress` | Prompt-embodied (S1 responsibility, verified in Verification_s1). OE-side reinforcement: OE 9 explicitly reads Special Requirements silence ("does not confirm the one-bedroom promise") to break the L9-induced short-circuit. | **PASS** — L9 prompt-level + OE 9 direct-observation counter |
| **L26 decoy parent thread** | 4 competing Julian-adjacent parents; canonical must be Mina C002 `1776997200` | OE 12 identifies canonical parent (channel C002 + user Mina + verbatim content match) + OE 13 verifies no Julian reply landed + OE 23 posts with `thread_ts "1776997200.000000"` exact. Julian's own C007 `1777011000` orphan and C002 `1777012200` "Drafted and sent" remain in universe as unresolved decoys. | **PASS** — canonical target forced with exact ts across 3 OEs |
| **L2 Airtable-silence + QB-invoice skip** | Unit-type claim lives only in email/Slack chatter; Airtable Special Requirements + QB invoice are the credit-math SSOT | OE 9 direct observation of Special Requirements silence on unit type + OE 10 direct observation of Marcus's Special Requirements silence on carrier stall + OE 11 QB invoice pull for credit-math base + OE 24 forces the $11,350 decomposition into the Linear comment | **PASS** — three-service reduction forces L2 |
| **Emergent L8 three-service reduction** | Airtable (relocation record) + email (Carmen no-reply) + QB (credit-math) triangulate the truthful answer | OE 4+5 (email UrbanNest thread) + OE 9 (Airtable relocation) + OE 11 (QB invoice) form the natural triangulation. OE 24 (Linear comment) forces the L8 chain to a single defensible artifact. | **PASS** — natural byproduct of A + D stack |

**Lens 3 summary:** 5/5 levers preserved. Zero lever loss.

### Lens 4 — Density hard STRICT

Recount without generosity. **STRICT interpretation:** only OEs the agent MUST execute are counted; no exploration buffer; no candidate-probe generosity.

| OE | STRICT no-buffer calls | Realistic-buffer calls |
|---|---:|---:|
| 1 (contacts × 2) | 2 | 2 |
| 2 (search + get) | 2 | 2 |
| 3 (get) | 1 | 1 |
| 4 (search + get) | 2 | 2 |
| 5 (search only; candidate probes optional) | 1 | 3 |
| 6 (search + get) | 2 | 2 |
| 7 (2× get_email_by_id) | 2 | 2 |
| 8 (search + get; possible candidate probes) | 2 | 3 |
| 9 (list_bases + get_record) | 2 | 2 |
| 10 (get_record) | 1 | 1 |
| 11 (read_invoice) | 1 | 1 |
| 12 (Slack search; possible candidate exploration) | 1 | 3 |
| 13 (replies) | 1 | 1 |
| 14 (list + get) | 2 | 2 |
| 15 (get) | 1 | 1 |
| 16 (list_engagements) | 1 | 1 |
| 17 (crm_search × 2 + contacts_search × 1) | 3 | 3 |
| 18–22 writes (send_email × 3 + airtable_update_records × 2) | 5 | 5 |
| 23–27 writes (Slack + Linear + CRM + calendar + email) | 5 | 5 |
| Cross-service verification buffer (contact re-check, thread parent verify, invoice cross-ref, base-id verify) | 0 | 5 |
| **TOTAL midpoint** | **37** | **~47** |

**Verdict Lens 4: FLAG — density BLOCKER-STRICT.**

- Under STRICTEST no-buffer counting: **37 calls midpoint** — **below the 40 THIN floor per AGENTS.md rule 11** (which triggers INSUFFICIENT_DENSITY = BLOCKER at the pipeline level).
- With realistic cross-service verification buffer of ~10: midpoint ~47 (THIN band 40–49) — still 3 below the 50 STRICT design target.
- Council B B3 projected 49 midpoint using a slightly more generous 7-call buffer plus more forgiving OE-5/OE-8/OE-12 exploration counts (2–4, 2–3, 1–3 ranges); AUDIT lens 4 removes that generosity per its own charter.

The task's structural intent (Customer Support recovery close spanning 8 services) supports realistic-buffer counting reaching ~47, but under STRICT AUDIT reading with buffer removed, the 37-count exposes real underflow risk on the platform.

**Fix path (non-REBUILD):** thicken the OE list at 3 known-thin points to force ~5 additional calls without changing the prompt, e.g.

1. **OE 5** — upgrade "*Also call get_email_by_id on any candidate inbound record surfaced by the search*" from optional to forced: "*Retrieve each candidate inbound record surfaced by `search_emails` (target: minimum 2 candidate probes) to defensibly conclude Carmen has not replied. If the search returns no candidates, run a second search with alternate keywords ('one-bedroom' or 'studio' or 'transfer') before concluding.*" — adds +2 calls forced.
2. **OE 8** — force a second `search_emails` pass with alternate keywords (`"delay update"` or `"Indianapolis"` or `"eastbound carrier"`) to defensibly locate any Road Runner follow-ups after the 4/11 initial notice. Adds +1 call forced.
3. **OE 12** — force enumeration of all Mina-authored Slack messages in the past 5 days across C002/C004/C006 before selecting the canonical parent, to defensibly reject the 4 known decoys per L26. Adds +2 calls forced.

Post-fix projection: STRICT no-buffer 37 + 5 = **42** (clears 40 THIN floor); realistic-buffer 47 + 5 = **~52** (clears 50 STRICT bar).

### Lens 5 — Parameter trap audit

Every parameter name walked against MoveOps tool catalog (`MoveOps_Base_Universe/6_Server_Tools_Details.json`).

| Tool | OE(s) | Params used | MoveOps trap | PASS/FLAG |
|---|---|---|---|---|
| contacts_search_contacts | 1, 17 | `query` | none | PASS |
| search_emails | 2, 4, 5, 6, 8 | `query`, `folder_name` | none | PASS |
| get_email_by_id | 2, 3, 4, 6, 7, 8 | `email_id`, `folder_name` | none (folder_name is opt) | **PASS on param names**; OE 7 `folder_name = "INBOX"` VALUE is wrong (FLAG under Lens 1) |
| airtable_list_bases | 9 | (none) | none | PASS |
| airtable_get_record | 9, 10 | `base_id`, `table_name`, `record_id` | GET uses `table_name` (NOT `table_id`) | **PASS** — trap respected |
| airtable_update_records | 20, 22 | `base_id`, `table_id`, `records` (array of {id, fields}) | UPDATE uses `table_id` (NOT `table_name`) | **PASS** — trap respected. Two different keys for two different tools; both handled correctly |
| conversations_search_messages | 12 | `search_query`, `filter_in_channel`, `filter_users_from` | none | PASS |
| conversations_replies | 13 | `channel_id`, `thread_ts` | `thread_ts` (NOT `thread_ts_legacy`) | **PASS on param names**; OE 12 prose uses `thread_ts_legacy` as descriptor (see Lens 9) |
| conversations_add_message | 23 | `channel_id`, `thread_ts`, `payload` | payload (NOT text/body/content) | **PASS** — trap respected |
| linear_list_issues | 14 | `query`, `team` | `team` (NOT `teamId`) — MoveOps-specific, differs from Brookfield | **PASS** — trap respected |
| linear_get_issue | 14, 15 | `id` | none | PASS |
| linear_create_comment | 24 | `issueId`, `body` | both required | PASS |
| crm_search_contacts | 17 | `full_name` | none | PASS |
| crm_list_engagements | 16 | `company_ids` | none | PASS |
| crm_create_engagement | 25 | `engagement_type`, `body`, `company_ids`, `contact_ids`, `title` | `engagement_type` + `body` both REQUIRED | **PASS** — both present |
| quickbooks_read_invoice | 11 | `invoice_id` | none | PASS |
| calendar_add_calendar_event | 26 | `title`, `start_datetime`, `end_datetime`, `attendees`, `description` | none | PASS |
| send_email | 18, 19, 21, 27 | `sender`, `recipients`, `cc`, `subject`, `content` | `content` (NOT body/text) | **PASS** — trap respected |

**Lens 5 summary:** 100% parameter-name accuracy across all 17 tool signatures. All 5 MoveOps parameter traps (table_id vs table_name split, payload vs text, team vs teamId, content vs body, engagement_type+body required) respected. The only issue at parameter-level is the `folder_name` VALUE mismatch in OE 7 (documented under Lens 1 as the primary Blocker-STRICT).

### Lens 6 — Persona-attribution audit

Cross-referenced against auto-memory `persona_attribution_landmine.md` (grep the OTHER candidate name before accepting).

| Identity | Correct target | Rejection stated in OE 17? | Universe verified? |
|---|---|---|---|
| Marcus Webb BrightLoop (correct) | `contact_brightloop_marcus_webb` @ `marcus.webb@brightloopanalytics.com` | Bound as recipient (OE 21 write) | ✓ |
| Marcus Webb Ironclad (decoy) | `contact_ironclad_001` / `ext_prospect_ironclad` @ `m.webb@ironcladsec.com` | **YES — explicit reject** | ✓ decoy exists |
| Marcus Webb Canopy (decoy) | `contact_canopy_marcus_webb` @ `marcus.webb.lab@gmail.com` | **YES — explicit reject** (added post-revision) | ✓ decoy exists |
| Marcus Thorne (decoy — MoveOps CFO name-similarity) | `moveops_marcus_thorne` @ `marcus.thorne@moveops.com` | **YES — explicit reject** (added post-revision) | ✓ decoy exists |
| Simone Richter BrightLoop (correct) | `contact_brightloop_simone_richter` @ `simone.richter@brightloopanalytics.com` | Bound as recipient (OE 18 write) | ✓ |
| Simone Richter StormCloud (decoy) | `contacts_contact_4d531c818e2a` @ `simone.richter@stormcloud.io` | **YES — explicit reject** | ✓ decoy exists |
| Carmen Reyes UrbanNest (correct) | `contacts_contact_00589cf8404a` @ `carmen.reyes@urbannestsolutions.com` | Bound as recipient (OE 19 write) | ✓ |
| Carmen Delgado-Reyes Palmetto (decoy) | `contacts_contact_03800e48b5a4` @ `carmen.delgado-reyes@palmettofoundation.org` | **YES — explicit reject** (added post-revision) | ✓ decoy exists |

**Additional observations (Universe verification):**
- `contacts_contact_6921464373bd` = second BrightLoop Marcus record in `contacts.contacts.json` (same email `marcus.webb@brightloopanalytics.com` as `contact_brightloop_marcus_webb`). **Duplicate of the correct identity, same email, not a near-miss.** Agent may bind either; send_email lands on the same recipient either way. Not a rejection candidate; advisory only.
- `contact_vendor_apartments` in `contacts.contacts.json` shares email `carmen.reyes@urbannestsolutions.com` with `contacts_contact_00589cf8404a`. **Same duplicate pattern for Carmen.** Send lands correctly either way. Advisory only.

**Lens 6 summary:** 4-way Marcus (3 decoys) + 2-way Simone (1 decoy) + 2-way Carmen (1 decoy) — **ALL near-miss identities explicitly rejected in OE 17**. Post-revision rejection list is complete under STRICTEST reading. This closes the Council B B5 advisory (Canopy Marcus + Palmetto Carmen incompleteness) and closes the user-memory persona-attribution landmine.

### Lens 7 — Coverage completeness (STRICT)

Enumerated every explicit + implicit prompt ask.

| Prompt ask | Explicit or implicit? | Covering OE(s) | PASS/FLAG |
|---|---|---|---|
| Close BrightLoop recovery before Tessa's weekly | goal (implicit) | OE 27 internal summary aggregates the whole close | PASS |
| Pull booking-vs-delivered picture from email | explicit | OE 2 + OE 3 + OE 4 + OE 5 | PASS |
| Figure out same-unit-type transfer availability | explicit | OE 4 (Q5 posed) + OE 5 (Carmen still owes) — truthfully unknown, correctly preserved through writes | PASS |
| Figure out swing on account | explicit | OE 4 (Q5/Q6 to Carmen) + OE 11 (QB base) + OE 24 (batch decomposition surfaced) | PASS |
| Escalate Carmen plainly (not gentle nudge) | explicit | OE 19 body enforces "escalation on Simone Richter Boston placement, not another nudge" + same-day requirement | PASS |
| Simone real answer today, cc Mina | explicit | OE 18 body enforces "factual delivery, not another promise" + cc Mina | PASS |
| Update Simone Airtable so "live not resolved" is visible | explicit | OE 20 with Special Requirements text + Status stays In Progress | PASS |
| Get current Road Runner position | explicit | OE 8 unread Road Runner delay email | PASS |
| Email Marcus concrete next checkpoint, cc Mina | explicit | OE 21 with Indianapolis + April 18-20 + cc Mina | PASS |
| Say if no hard delivery date, don't soften | explicit | OE 21 body "state directly that Road Runner cannot commit to a hard delivery date … Do not soften the absence of a hard date" | PASS |
| Reflect actual state on Marcus Airtable | explicit | OE 22 | PASS |
| Slack post on audit thread NOT fresh | explicit | OE 12 + OE 13 + OE 23 with exact thread_ts | PASS |
| Linear comment: per-employee status + money impact | explicit | OE 24 with $11,350 decomposition | PASS |
| Update CRM engagement (stop reading "cohort done") | explicit | OE 16 read + OE 25 new engagement (create-only tool) | PASS |
| 30 mins late Tuesday to recheck Simone | explicit | OE 26 (2026-04-28T16:30–17:00 -07:00) | PASS |
| Short internal email to Mina pulling whole position | explicit | OE 27 | PASS |
| cc Mina (implicit universal) | implicit — 2 mentions plus universal cadence | OE 18 cc + OE 19 cc + OE 21 cc; OE 27 direct-to-Mina | PASS |
| "same day" for Carmen | implicit — from "escalate plainly" | OE 19 body enforces same-day response requirement | PASS |
| "supersedes without deleting" implicit for CRM | implicit — create-only tool constraint | OE 25 correctly creates new engagement (not update) | PASS |

**Lens 7 summary:** 19/19 explicit + implicit asks covered. Zero gap. Note that "figure out transfer availability" is correctly preserved as UNKNOWN (Carmen hasn't replied), which is the load-bearing L25 stump — the write chain must NOT fabricate an answer, and OEs 18/19/24 all encode this correctly.

### Lens 8 — Data-anomaly containment

`email_email_ab2391d62ab1` carries a **compound anomaly**:
- `sender = "carmen.reyes@urbannestsolutions.com"` — but body opens "Hi Carmen" and is signed "Julian Brooks · Lead Customer Support Specialist · MoveOps"
- `recipients_json = ["carmen.reyes@urbannestsolutions.com"]` — **recipient-to-self loop** (bonus glitch not explicitly called out but noted in Council A advisory 5)
- `cc_json = ["mina.hashimoto@moveops.com", "chloe.vance@moveops.com"]` — consistent with Julian's outbound intent
- `folder = "SENT"` — consistent with outbound from MoveOps side

**Containment check across downstream OEs:**

| Downstream OE | Uses sender field? | Uses body / content? | Contained? |
|---|---|---|---|
| OE 5 (verify no Carmen reply) | No — filters by INBOX + subject + `carmen.reyes@urbannestsolutions.com` in a fresh search | Yes | ✓ Contained |
| OE 17 (bind Carmen contact) | No — binds via `contacts_search_contacts` full-name search returning `contacts_contact_00589cf8404a` | (indirect) | ✓ Contained |
| OE 19 (Carmen escalation email) | No — recipient literal `carmen.reyes@urbannestsolutions.com`; sender literal `julian.brooks@moveops.com` | Yes (restates 6 Qs from body) | ✓ Contained |

**Lens 8 summary:** Anomaly correctly flagged at OE 4. **Zero downstream propagation of the sender-field glitch.** Body-content-truth pattern held end-to-end.

### Lens 9 — Convention drift

Checked against `Reference/OE_Format.md` and `Reference/OE_Convention_Inventory.json`.

| Convention | Compliance | Notes |
|---|---|---|
| Opening phrases (e.g. "Search…", "Retrieve…", "Call…", "Look up…", "List…", "Write action.") | ✓ PASS | Every OE opens with a canonical verb |
| `tool_name (param "value", param "value")` pattern | ✓ PASS | Every tool call follows this format |
| "Conclude:" usage for observation → inference | ✓ PASS | Used correctly in OEs 2, 5, 8, 9, 10, 11, 16 |
| Write-action prefix | ✓ PASS | OEs 18–27 all open with "Write action." |
| No tool names in prose outside tool-name-with-params blocks | ✓ PASS | Tool tokens confined to canonical brackets |
| **OE 12 prose descriptor `thread_ts_legacy`** | **FLAG (advisory)** | OE 12 says "The rubric-canonical parent is thread_ts_legacy `1776997200.000000`" — this reads as if the parameter name is `thread_ts_legacy`. The tool parameter is `thread_ts` (confirmed via MoveOps catalog). OE 13/23 actual invocations use `thread_ts` correctly. Rename the prose descriptor to plain `thread_ts` for clarity. Council A already surfaced this (advisory 1). Not a Blocker but under STRICTEST reading it's convention drift on prose. |

**Lens 9 summary:** Convention compliance high. One prose-level drift on OE 12 descriptor already advised.

## Block issues (BLOCKER-STRICT)

Under STRICT AUDIT interpretation, two defects block PASS:

1. **BLOCKER-STRICT [OE 7 folder_name = "INBOX" is factually wrong]**
   - `email_email_ca010e9c9446` actual folder = **SENT** (verified in `email.emails.json`)
   - `email_email_87f575fcacf9` actual folder = **SENT** (verified in `email.emails.json`)
   - Both are Marcus's outbound emails to `support@moveops.com`. From MoveOps's shared-workspace perspective these should logically be INBOX (they were received), but the universe data stores them as SENT. This is a universe-data quirk the OE writer inherited.
   - Risk: if the Email MCP scopes `get_email_by_id` retrieval by `folder_name`, the tool call fails on both records. Even if the tool ignores `folder_name` when `email_id` is provided, STRICT auto-fails Accuracy on any documented factual defect.

2. **BLOCKER-STRICT [Density midpoint = 37 under STRICT no-buffer]**
   - Below the AGENTS.md rule 11 THIN floor of 40 → structural INSUFFICIENT_DENSITY risk on real platform runs.
   - Realistic-buffer midpoint ~47 lifts to THIN band but does not clear the 50 STRICT design target.
   - Council B / Hardness_Plan midpoint projections of 49–50 relied on generous OE-5/OE-8/OE-12 exploration counts that STRICT AUDIT lens 4 removes.

## Per-issue fixes (REVISE — in-place, no REBUILD)

**Fix 1 — OE 7 folder_name correction (5-second edit)**

Change OE 7 from:

> Retrieve Marcus's original "Checking in on my car delivery status" using get_email_by_id (email_id "email_email_ca010e9c9446", folder_name "INBOX") and Marcus's later escalation "Second follow-up: I need an actual ETA for my car" using get_email_by_id (email_id "email_email_87f575fcacf9", folder_name "INBOX").

To either:

> Retrieve Marcus's original "Checking in on my car delivery status" using get_email_by_id (email_id "email_email_ca010e9c9446", folder_name "SENT") and Marcus's later escalation "Second follow-up: I need an actual ETA for my car" using get_email_by_id (email_id "email_email_87f575fcacf9", folder_name "SENT"). Note: both records are stored as SENT in the universe despite being inbound to MoveOps support — the folder metadata reflects Marcus's outbound perspective.

Or (safer against future tool-scoping changes):

> Retrieve Marcus's original "Checking in on my car delivery status" using get_email_by_id (email_id "email_email_ca010e9c9446") and Marcus's later escalation "Second follow-up: I need an actual ETA for my car" using get_email_by_id (email_id "email_email_87f575fcacf9"). [drop folder_name param entirely; email_id is unique]

**Fix 2 — Density thickening (~5 forced additional calls)**

Upgrade the three known-thin OEs to force additional realistic exploration:

- **OE 5:** Change "*Also call get_email_by_id on any candidate inbound record surfaced by the search*" to "*Retrieve at least 2 candidate inbound records surfaced by search_emails via get_email_by_id to defensibly conclude no Carmen reply. If the first search returns no candidates, run a second search_emails pass with alternate keywords ('one-bedroom' or 'studio' or 'unit type').*"

- **OE 8:** Add "*After retrieving `email_email_a3ca1b6dd238`, run a second search_emails pass with alternate keywords ('delay update' or 'Indianapolis' or 'eastbound carrier') scoped to INBOX to confirm no Road Runner follow-up landed after 4/11.*"

- **OE 12:** Change "*Search Slack using conversations_search_messages...to locate Mina's Thursday audit thread parent.*" to "*Search Slack using conversations_search_messages... to enumerate all Mina-authored parents in the past 5 days across C002, C004, C006 (expect 4 competing candidates including ts 1776999900 C004 expansion ping and Julian-adjacent decoys). Explicitly reject all non-C002 candidates and all non-audit-topic C002 candidates before locking on the canonical thread_ts 1776997200.000000.*"

Post-fix expected midpoint: STRICT no-buffer ~42 (clears 40 floor); realistic-buffer ~52 (clears 50 STRICT bar).

**Fix 3 — OE 12 prose descriptor (1-second edit)**

Change "The rubric-canonical parent is thread_ts_legacy `1776997200.000000`" to "The rubric-canonical parent is thread_ts `1776997200.000000`" (rename the descriptor to match the tool parameter name).

**Fix 4 — OE 14 labels claim (30-second edit, optional)**

OE 14 states `labels brightloop plus service-recovery`. Universe verification: `labels = null` on `linear_issue_f85be674c9b8`. Either seed the labels in universe (outside pipeline scope per hard rule 4) or drop the labels claim from OE 14. Since labels don't gate OE 24's `linear_create_comment` (issueId + body only), this is cosmetic; drop the claim for accuracy. Non-blocking.

## Non-blocking advisories forwarded to S3

1. **[Lens 6 duplicates]** Carmen has 2 contact records with the same email in Universe_Split (`contacts_contact_00589cf8404a` + `contact_vendor_apartments`); Marcus BrightLoop has 2 records with the same email (`contact_brightloop_marcus_webb` in CRM + `contacts_contact_6921464373bd` in Contacts). Send_email lands correctly either way. S3 rubric grounding should accept either contact_id as valid for the correct-recipient check.

2. **[Lens 2 borderline]** OE 15 (retrieve sister audit issue) is defensible-context but under STRICTEST reads as borderline scope creep (prompt says "the BrightLoop operational issue", singular). S3 should NOT rubric-grade OE 15 as required — the Linear comment writes only to Chloe's ops-gaps issue (OE 14 target). Retain OE 15 as context-only.

3. **[Lens 5 CRM create-only]** OE 25 correctly uses `crm_create_engagement` because MoveOps CRM has no update tool. S3 Outcome 1.1 rubric MUST NOT check for `crm_update_engagement` (does not exist in MoveOps V2.1 tool catalog). Rubric must grade "new engagement supersedes 4/2 note".

4. **[Lens 8 additional glitch]** `email_email_ab2391d62ab1` also has `recipients_json = ["carmen.reyes@urbannestsolutions.com"]` (recipient-to-self anomaly in addition to sender-field anomaly). Not called out in OE 4 (Council A advisory 5 flagged it). Downstream OE 5/17/19 do not use this record's recipient field for binding, so containment holds. S3 rubric must NOT grade the recipient list of this specific email.

5. **[Lens 4 buffer sensitivity]** Post-fix density projection (~52 midpoint realistic-buffer) relies on the OE-5/OE-8/OE-12 forced probes. If S3 rubric-grades any of these as "optional" or "not required", the effective forced count on real platform runs may drop back into the THIN band. Recommend S3 rubric ALL of OE 5 (min-2-probes), OE 8 (second-search), OE 12 (candidate enumeration) as Outcome 1.1 tool-call verification rubrics.

6. **[Lens 9 OE 12 prose]** Already listed as Fix 3. If not fixed inline, forward to S3 as rubric-grounding advisory only.

7. **[Lens 1 OE 14 labels]** Already listed as Fix 4. If not fixed inline, forward to S3 as advisory.

8. **[Downstream S3 timezone]** OE 26 uses `-07:00` (US/Pacific PDT) correctly per AGENTS.md moveops registry. S3 Outcome 1.2 timezone check must ground on AGENTS.md, not on the stale `Universe_Index/today_horizon.json` which shows `America/New_York` (Verification_s1 discrepancy #2). Do NOT accept `-04:00` EDT on OE 26 rubric grading.

---

**Bottom line:** Task 36 S2 OE has strong grounding (Lens 1: 32/34 atoms verified; Lens 3: 5/5 levers preserved; Lens 5: 100% parameter accuracy; Lens 6: all near-miss identities rejected; Lens 8: data anomaly contained), strong prompt coverage (Lens 7: 19/19 asks), and clean convention compliance (Lens 9). Two REVISE-class defects gate STRICT-PASS: OE 7 folder_name factual error on 2 records, and density midpoint 37 under STRICT no-buffer (47 with realistic buffer, still below 50 STRICT target). Both are fixable in-place without touching the prompt. Recommend Fix 1 + Fix 2 (mandatory) + Fix 3 + Fix 4 (cosmetic) inline; re-run AUDIT for PASS (STRICT) verdict.

**Verdict: REVISE.**
