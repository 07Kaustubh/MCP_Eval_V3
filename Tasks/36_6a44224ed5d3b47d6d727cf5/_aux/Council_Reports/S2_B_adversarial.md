# Council B — Adversarial (S2 OE Task 36)

## Verdict: GO

Rationale: forward-map covers all 14 prompt asks; reverse-map ties every OE to a prompt sentence; 4 primary Hardness levers + emergent L8 all exercised end-to-end by at least one OE step; density midpoint ~49 (PASS, tight margin); persona-attribution and sender-field anomaly correctly handled where they land. Two Minor advisories forwarded to S3 (near-miss rejection completeness, OE 7 subject/folder misalignment). No Majors; no lever lost; no density collapse; no forward-map gap.

## QC scoring

### OE Completeness — 1/3/5 per role lens

- Skeptical Reviewer: **5/5** — every one of the prompt's 14 explicit/implicit asks maps to at least one OE. Booking-vs-delivered pull (OEs 2, 3, 4, 5), Carmen escalation (OE 19), Simone reply (OE 18), Simone Airtable update (OE 20), Road Runner position (OE 8), Marcus reply (OE 21), Marcus Airtable update (OE 22), Slack post on Mina's audit thread (OE 23), Linear comment (OE 24), CRM engagement correction (OE 25), calendar hold (OE 26), internal Mina summary (OE 27).
- Adversarial Client (Tessa expecting Monday weekly): **5/5** — the internal wrap-up email at OE 27 gives Julian a single defensible source for the Monday weekly; per-employee status + $11,350 batch decomposition on the Linear comment (OE 24) sizes the exposure Tessa will ask about.
- Senior QC Engineer (strictest interpretation): **5/5** — no unlabeled implicit ask remains uncovered. Prompt says "figure out whether a same-unit-type transfer is available and what the swing on our account is" — OE 5 concludes Carmen has not replied yet with these facts, so the truthful answer (transfer availability unknown, credit unquantified) is preserved through the write chain rather than fabricated. Prompt says "if the carrier still cannot give a hard delivery date, say that. Do not soften it." — OE 21 explicitly states no hard delivery date without softening.
- Pipeline Auditor: **5/5** — Hardness_Plan requires L25 anchor re-read (OEs 2/4/6), L26 canonical parent (OEs 12/13/23 on `1776997200.000000`), L2 Airtable/QB skip (OEs 9/10/11), L9 self-anchor absorbed by prompt framing (no OE required). Emergent L8 three-service chain surfaces naturally via OE 4/5 (email) + OE 9 (Airtable) + OE 11 (QB).
- Rubric Author S3: **5/5** — 10 write OEs = 10 Outcome 1.1 rubrics; content-specific writes (OEs 18/19/21/23/24/25/27) give 7 Outcome 1.2 targets; the "no hard delivery date" fact from OE 21 gives one Outcome 2.1 candidate.

### OE Accuracy — 1/3/5 per role lens

- Skeptical Reviewer: **5/5** — every OE traces back to a prompt sentence with no scope creep. OE 1 (contact lookup) and OE 15 (audit issue for context) are foundational; every other OE maps to a specific prompt sentence enumerated in B2.
- Adversarial Client: **5/5** — no OE step demands facts Tessa would not expect Julian to gather. Money-impact anchor on INV-2026-0308 is exactly the tabletop question the CFO/People-Ops side will ask.
- Senior QC Engineer: **5/5** — every OE parameter (base_id / table_id / record_id / issue_id / thread_ts / channel_id / email_id) is verified against the per-task universe split. Zero fabricated identifiers.
- Pipeline Auditor: **5/5** — no OE re-introduces the sender-field anomaly on `email_email_ab2391d62ab1`. OE 4 explicitly rules "sender field is a data anomaly; treat body content as truth." Downstream OE 19 sends to `carmen.reyes@urbannestsolutions.com` and cc's Mina — content-truth path preserved.
- Rubric Author S3: **5/5** — no OE forces a rubric that would demand behavior beyond the prompt's ask (no over-specified formatting demand, no unrealistic content template).

## Per-perspective findings (B1 through B9)

### B1. OE Completeness — Forward map

| Prompt ask | OE(s) covering | Coverage OK? |
|---|---|---|
| Pull booking-vs-delivered picture from email | OE 2 (Julian's 4/23 outbound) + OE 3 (Simone parent 4/8) + OE 4 (Julian's UrbanNest outbound with 6 Qs) + OE 5 (verify no Carmen reply) | Yes |
| Figure out same-unit-type transfer availability + account swing | OE 4 + OE 5 (Q5/Q6 posed to Carmen, still open) + OE 11 (QB $11,350 credit-math base) | Yes — truthfully unknown pending Carmen |
| Escalate Carmen plainly by email (not gentle nudge) | OE 19 | Yes |
| Email Simone back today, cc Mina, real answer | OE 18 (cc Mina, factual delivery not another promise) | Yes |
| Update Simone Airtable placement record | OE 20 (Special Requirements updated, Status stays In Progress) | Yes |
| Get current Road Runner position | OE 8 (retrieve unread `email_email_a3ca1b6dd238`) | Yes |
| Email Marcus concrete next checkpoint, cc Mina | OE 21 (Indianapolis hub, April 18-20 window) | Yes |
| Say if no hard delivery date, don't soften | OE 21 body requirement + no-softening clause | Yes |
| Update Marcus Airtable placement record | OE 22 | Yes |
| Slack status on Mina's audit thread NOT fresh post | OE 12 (identify parent `1776997200`) + OE 13 (verify no Julian reply landed) + OE 23 (post with `thread_ts "1776997200.000000"`) | Yes |
| Linear comment on BrightLoop operational issue: per-employee status + money impact | OE 14 (retrieve `linear_issue_f85be674c9b8`) + OE 24 (comment with $ decomposition) | Yes |
| Update BrightLoop CRM engagement so it stops reading "cohort done" | OE 16 (retrieve current NOTE) + OE 25 (create new engagement, create-only tool) | Yes |
| Hold 30 mins late Tuesday for Simone housing recheck | OE 26 (2026-04-28T16:30:00-07:00) | Yes |
| Send Mina short internal email pulling whole position together | OE 27 | Yes |

**Forward map: PASS.** All 14 asks covered.

### B2. OE Accuracy — Reverse map

| OE | Prompt sentence | In scope? |
|---|---|---|
| 1 | Foundational — sender identity + cc target for every outbound | Yes |
| 2 | "Both went out the door as apologies with promises attached, not actual answers" | Yes |
| 3 | "The truth of what we actually promised her and what got booked" | Yes |
| 4 | "I asked Carmen six specific questions Thursday" | Yes |
| 5 | "I do not remember an answer coming back. If she still owes us one, escalate" | Yes |
| 6 | Marcus recovery arm — "I promised him a fresh carrier status Thursday afternoon and never sent it" | Yes |
| 7 | Marcus arm — prior-silence proof | Yes |
| 8 | "Get the current position from Road Runner" | Yes |
| 9 | "Update her Airtable placement record" (read-then-write) | Yes |
| 10 | "Reflect the actual state on his Airtable placement record" (read-then-write) | Yes |
| 11 | "What the money impact looks like on the batch" | Yes |
| 12 | "The audit thread Mina raised Thursday" | Yes |
| 13 | Verify no Julian status already there, supports "not in a fresh post" | Yes |
| 14 | "Add a Linear comment on the BrightLoop operational issue" | Yes |
| 15 | Sister audit issue for context, supports the operational issue framing | Yes |
| 16 | "Update the BrightLoop engagement on our CRM" (read-then-write via create) | Yes |
| 17 | Foundational — recipient disambiguation before every write | Yes |
| 18 | "Email her back, cc Mina" | Yes |
| 19 | "Escalate plainly by email, do not just send another gentle nudge" | Yes |
| 20 | "Update her Airtable placement record so anyone reading it can see this is live" | Yes |
| 21 | "Email him a concrete next checkpoint, cc Mina" + "do not soften it" | Yes |
| 22 | "Reflect the actual state on his Airtable placement record" | Yes |
| 23 | "Put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post" | Yes |
| 24 | "Add a Linear comment on the BrightLoop operational issue that captures where each employee stands and what the money impact looks like" | Yes |
| 25 | "Update the BrightLoop engagement on our CRM so it stops reading like the April cohort is basically done" | Yes |
| 26 | "Hold thirty minutes on my calendar late Tuesday to recheck Simone's housing outcome" | Yes |
| 27 | "Send Mina a short internal email pulling the whole position together in one place" | Yes |

**Reverse map: PASS.** No scope creep.

### B3. Tool-call density projection

| Component | Range | Midpoint |
|---|---|---:|
| OE 1 contacts_search_contacts x 2 (Julian, Mina) | 2 | 2 |
| OE 2 search_emails + get_email_by_id | 2 | 2 |
| OE 3 get_email_by_id | 1 | 1 |
| OE 4 search_emails + get_email_by_id | 2 | 2 |
| OE 5 search_emails + candidate get_email_by_id probes | 2-4 | 3 |
| OE 6 search_emails + get_email_by_id | 2 | 2 |
| OE 7 get_email_by_id | 1 | 1 |
| OE 8 search_emails + get_email_by_id | 2-3 | 2 |
| OE 9 airtable_list_bases + airtable_get_record | 2 | 2 |
| OE 10 airtable_get_record | 1 | 1 |
| OE 11 quickbooks_read_invoice | 1 | 1 |
| OE 12 conversations_search_messages (with candidate exploration) | 1-3 | 2 |
| OE 13 conversations_replies | 1 | 1 |
| OE 14 linear_list_issues + linear_get_issue | 2-3 | 2 |
| OE 15 linear_get_issue | 1 | 1 |
| OE 16 crm_list_engagements | 1-2 | 1 |
| OE 17 crm_search_contacts x 2 + contacts_search_contacts x 1 (Carmen) | 3 | 3 |
| OE 18-22 writes (send_email x 3, airtable_update_records x 2) | 5 | 5 |
| OE 23-27 writes (conversations_add_message, linear_create_comment, crm_create_engagement, calendar_add_calendar_event, send_email) | 5 | 5 |
| Cross-service verification buffer (recipient re-check, thread parent re-verify, invoice cross-ref) | 5-9 | 7 |
| **TOTAL projected** | **41-56** | **~49** |

**Verdict: PASS (tight).** Midpoint 49 sits AT the 50 design threshold; conservative floor 41 clears the 40 hard floor. Buffer of 7 assumes normal exploratory behavior; if the agent skips OE 26 (calendar hold) or short-circuits Simone-thread candidate exploration, midpoint drops to ~44 (THIN). Range remains defensible; forwarded to S3 as a watch-item, not a block.

### B4. Hardness lever preservation

| Lever | Exercised by OE(s) | Preserved? |
|---|---|---|
| **L25 existing-output anchor** | OE 2 re-reads Julian's 4/23 Simone outbound `email_email_6d0501ac647f` (concludes promise-not-delivery); OE 4 re-reads Julian's 4/23 Carmen outbound `email_email_ab2391d62ab1` (six Qs, no reply yet); OE 6 re-reads Julian's 4/23 Marcus outbound `email_email_bedc44dbea30` (concludes promise-not-delivery) | Yes — each OE explicitly rules "cannot be re-used as the recovery answer" |
| **L9 authority self-anchor (soft verbs per L24)** | Prompt-level framing (Julian's soft-verb voice, "I need a defensible position", implicit "closure just needs sending"). No OE step required — lever fires at prompt-reading time, not at OE-execution time. Prompt-level L9 preserved per S1 AUDIT (all 12 Prompt sub-dims 5/5). | Yes (lever is prompt-embodied, not OE-embodied) |
| **L26 decoy parent thread** | OE 12 identifies canonical Mina audit parent `thread_ts_legacy 1776997200.000000` on C002; OE 13 verifies no Julian status has landed on that thread (universe confirms 0 replies); OE 23 posts with `thread_ts "1776997200.000000"` exact. Julian's own C007 orphan `1777011000` and C002 "Drafted and sent" `1777012200` remain visible as decoys. | Yes (yield ~40-60% per S1 note, thinned from 80% by prompt's "the audit thread Mina raised Thursday" phrasing) |
| **L2 Airtable-silence + QB-invoice skip** | OE 9 explicitly notes Simone's Special Requirements is silent on unit type (universe verified — mentions only "2 weeks furnished temp housing", no "1BR" or "studio"); OE 10 notes Marcus's record does not currently reflect the transfer-hub stall or April 18-20 window; OE 11 pulls INV-2026-0308 $11,350 with per-line decomposition | Yes |
| **Emergent L8 3-service reduction** | OE 4/5 (email UrbanNest thread) + OE 9 (Airtable relocation record) + OE 11 (QB invoice) form the natural 3-service triangulation. OE 24 (Linear comment) forces the L8 chain to a single artifact. | Yes |

**All 5 levers preserved.** L25 lands hardest (three explicit "promise-not-delivery" conclusions across OEs 2/4/6). L26 canonical parent forced with exact ts across three OEs.

### B5. Persona-attribution safety

OE 17 handles the multi-Marcus / multi-Simone / multi-Carmen landmine with mixed completeness:

| Identity | Correct target | Explicitly rejected in OE 17? | Verified in universe? |
|---|---|---|---|
| Marcus Webb BrightLoop | `contact_brightloop_marcus_webb`, `marcus.webb@brightloopanalytics.com` | Bound as recipient | Yes (`contact_brightloop_marcus_webb`) |
| Marcus Webb Ironclad | (reject) | Yes — "reject m.webb@ironcladsec.com" | Yes (`contact_ironclad_001`) |
| Marcus Webb Canopy (gmail.lab) | (reject) | **No** — not called out | Yes (`contact_canopy_marcus_webb`, `marcus.webb.lab@gmail.com`) |
| Simone Richter BrightLoop | `contact_brightloop_simone_richter`, `simone.richter@brightloopanalytics.com` | Bound as recipient | Yes |
| Simone Richter StormCloud | (reject) | Yes — "reject simone.richter@stormcloud.io" | Yes (`contacts_contact_4d531c818e2a`) |
| Carmen Reyes UrbanNest (primary) | `contacts_contact_00589cf8404a`, `carmen.reyes@urbannestsolutions.com` | Bound as recipient | Yes |
| Carmen Reyes UrbanNest (duplicate) | (implicit — same email) | Not called out (`contact_vendor_apartments` also carries same UrbanNest email) | Yes — duplicate ID exists |
| Carmen Delgado-Reyes Palmetto | (reject) | **No** — not called out | Yes (`contacts_contact_03800e48b5a4`, `carmen.delgado-reyes@palmettofoundation.org`) |

Per auto-memory `persona_attribution_landmine.md`, this is the recurring landmine. Two near-misses (Canopy Marcus + Palmetto Carmen) are not explicitly rejected. Since the outbound email addresses in OEs 18/19/21 are specified literally, the actual send will land on the correct recipient; the risk is the AGENT may bind the wrong contact_id at lookup time and cite it in the response body. **Minor advisory forwarded to S3** — S3 rubric grounding must include explicit "does NOT send to `marcus.webb.lab@gmail.com`" and "does NOT send to `carmen.delgado-reyes@palmettofoundation.org`" evidence checks on the Outcome 1.2 rubric for OE 19 (Carmen write) and OE 21 (Marcus write).

### B6. Missing-Process propagation

Reviewed every prompt sentence for ordering constraints Outcome rubrics cannot capture:

| Constraint | Captured how? |
|---|---|
| "put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post" | Outcome 1.2 (content check on `thread_ts` parameter of the `conversations_add_message` write). Three-condition test FAILS the second condition ("not verified by any Outcome rubric") because thread_ts is a write parameter |
| "cc Mina" on both employee replies | Outcome 1.2 (content check on `cc` param) |
| "supersedes the 4/2 note without deleting it" (implicit — create-only CRM) | Outcome 1.1 (create-engagement, not update) — enforced by tool availability |
| "email a concrete next checkpoint" for Marcus + "do not soften it" | Outcome 1.2 (content check for "April 18-20" + "no hard delivery date" language) |

**No missing Process behavior surfaces.** All ordering constraints reduce to write-parameter content checks under Outcome 1.2. Zero Process rubrics recommended. Consistent with V3 reference tasks (all 4 have zero process rubrics per AGENTS.md hard rule 8).

### B7. Data anomaly propagation

- OE 4 correctly handles the sender-field anomaly on `email_email_ab2391d62ab1`. Universe verified: `sender: carmen.reyes@urbannestsolutions.com` but `content` opens "Hi Carmen" and is signed "Julian Brooks, Lead Customer Support Specialist, MoveOps". OE 4 explicitly rules: "Note the sender field on this record shows carmen.reyes@urbannestsolutions.com as a data anomaly. The body opens 'Hi Carmen' and is signed by Julian, so treat body content as truth. Do not accept the sender field for identity."
- Downstream OE 19 sends to `carmen.reyes@urbannestsolutions.com` with sender `julian.brooks@moveops.com` — the anomaly does NOT propagate into the write chain.
- Downstream OE 5 verifies no Carmen INBOUND reply exists — the anomaly does NOT contaminate the "no reply" conclusion because OE 5 filters by folder INBOX + subject.

**Data anomaly correctly contained.** No re-introduction downstream.

### B8. OE-to-Rubric forward map preview

Write OEs (10 total):

| OE | Type | Rubric class | S3 note |
|---|---|---|---|
| OE 18 | send_email to Simone | Outcome 1.1 (email sent) + Outcome 1.2 (recipient=simone.richter@brightloopanalytics.com; cc=mina.hashimoto@moveops.com; sender=julian.brooks@moveops.com; content states escalation-to-Carmen + same-day-response-requested + not-another-promise) | Content check must reject re-use of Julian's 4/23 apology-then-promise template |
| OE 19 | send_email escalation to Carmen | Outcome 1.1 + Outcome 1.2 (recipient=carmen.reyes@urbannestsolutions.com; cc=mina.hashimoto@moveops.com; content restates six Qs + declares this is escalation + same-day requirement) | Content check must explicitly reject sending to `carmen.delgado-reyes@palmettofoundation.org` (Palmetto Carmen) |
| OE 20 | airtable_update_records for Simone record | Outcome 1.1 + Outcome 1.2 (base_id=appMoveOpsOps001; table_id=tblRelocations01; record_id=recSimoneRichterBrightloop; Special Requirements text reflects mismatch + escalation state; Status remains In Progress) | Field-name check: table has only "Special Requirements", no "Notes" field — S3 should not require both |
| OE 21 | send_email to Marcus | Outcome 1.1 + Outcome 1.2 (recipient=marcus.webb@brightloopanalytics.com; cc=mina.hashimoto@moveops.com; content states Indianapolis transfer hub + April 18-20 revised window + no hard delivery date NOT softened) | Content check must explicitly reject sending to `m.webb@ironcladsec.com` OR `marcus.webb.lab@gmail.com` |
| OE 22 | airtable_update_records for Marcus record | Outcome 1.1 + Outcome 1.2 (base_id / table_id / record_id + Special Requirements text reflects transfer-hub stall + April 18-20 window + no hard date) | Same field-name caveat as OE 20 |
| OE 23 | conversations_add_message on Mina's audit thread | Outcome 1.1 (post happened) + Outcome 1.2 (channel_id=C002; **thread_ts="1776997200.000000" EXACT**; payload summarizes Simone + Marcus + Airtable + Linear + CRM state) | thread_ts EXACT match is the L26 canonical target — do NOT accept alternate values |
| OE 24 | linear_create_comment on ops-gaps issue | Outcome 1.1 + Outcome 1.2 (issueId=linear_issue_f85be674c9b8; body captures Simone status + Marcus status + $11,350 batch with $5,250/$5,600/$500 decomposition) | Money-impact numbers are the L2/L8 payoff — S3 must check each dollar figure |
| OE 25 | crm_create_engagement (create-only, supersedes NOTE) | Outcome 1.1 (create happened, engagement_type=NOTE) + Outcome 1.2 (company_ids=[company_brightloop]; body states cohort-not-closed + Simone-unit-mismatch + Marcus-hub-stall) | Rubric should NOT check for an update tool (`crm_update_engagement` does not exist in MoveOps V2.1 catalog) |
| OE 26 | calendar_add_calendar_event | Outcome 1.1 (event created) + Outcome 1.2 (start=2026-04-28T16:30 local; end=17:00 local; attendees include julian.brooks@moveops.com; description mentions pending UrbanNest response) | TZ offset -07:00 correct per AGENTS.md moveops registry (US/Pacific = PDT on 2026-04-28). Do NOT allow -04:00 EDT |
| OE 27 | send_email internal summary to Mina | Outcome 1.1 + Outcome 1.2 (recipient=mina.hashimoto@moveops.com; sender=julian.brooks@moveops.com; content covers Simone + Marcus + Slack + Linear + CRM + calendar in one place) | Monday-weekly defensible-source anchor — content check must include all 5 workstream anchors |

Outcome 2.1 candidate: "no hard delivery date" fact from OE 21 — the prompt explicitly requires this be surfaced without softening. Candidate for Outcome 2.1 tied to the Marcus reply write.

**S3 forward map: 10 Outcome 1.1 + ~7 Outcome 1.2 + 1 Outcome 2.1 candidate = ~18 rubrics minimum.** No write action forces a rubric beyond the prompt's asks.

### B9. Coherence / Sequencing

- Discovery block (OEs 1-17) fully precedes write block (OEs 18-27).
- OE 3 (Simone parent thread) precedes OE 20 (Simone Airtable update) — read-then-write.
- OE 5 (verify no Carmen reply) precedes OE 19 (Carmen escalation) — verify-then-escalate.
- OE 8 (Road Runner delay email) precedes OE 21 (Marcus reply) — read-then-write.
- OE 11 (QB invoice) precedes OE 24 (Linear comment with $ figures) — read-before-money-claim.
- OE 12/13 (Mina audit parent identify + reply state) precedes OE 23 (post to thread) — verify-parent-before-post.
- OE 16 (CRM engagement current state) precedes OE 25 (new engagement) — read-before-create.
- OE 17 (contact bindings) precedes every write.

No OE depends on a future OE's output. Related discoveries are batched (Simone arm OEs 2-5, Marcus arm OEs 6-8). **Coherence PASS.**

## Block issues (Major)

- **None.**

## Non-blocking advisories (forwarded to S3)

1. **OE 7 subject + folder misalignment (Minor).** OE 7 says "Retrieve the parent Marcus email using get_email_by_id (email_id 'email_email_ca010e9c9446', folder_name 'INBOX') to pull Marcus's original 'second follow-up: I need an actual ETA for my car' note." Universe verification: `email_email_ca010e9c9446` has **subject: "Checking in on my car delivery status"** (NOT "second follow-up") and **folder: SENT** (NOT INBOX). The "Second follow-up..." subject actually belongs to `email_email_87f575fcacf9` (Marcus's 4/20 follow-up, parent_id=`ca010e9c9446`, timestamp 2026-04-20T23:37). Julian's 4/23 reply `email_email_bedc44dbea30` has parent_id=`email_email_ca010e9c9446` — the parent link is correct, but the OE misquotes the subject and passes the wrong folder param. Prior-silence evidence is still established either way; the mislabel does not block the evidence purpose. S3 rubric grounding for OE 7 should either (a) target `email_email_87f575fcacf9` if the "second follow-up" subject is load-bearing, or (b) target `email_email_ca010e9c9446` and quote the correct subject ("Checking in on my car delivery status"). Recommend (a) — the more recent Marcus message better proves prior silence.

2. **OE 17 incomplete near-miss rejection (Minor).** OE 17 explicitly rejects `simone.richter@stormcloud.io` and `m.webb@ironcladsec.com` but does **not** explicitly reject `marcus.webb.lab@gmail.com` (Canopy Marcus, verified in universe as `contact_canopy_marcus_webb`) or `carmen.delgado-reyes@palmettofoundation.org` (Palmetto Carmen, verified in universe as `contacts_contact_03800e48b5a4`). Per auto-memory `persona_attribution_landmine.md`, S3 rubric grounding on the Outcome 1.2 rubrics for OE 19 (Carmen write) and OE 21 (Marcus write) must include explicit "does NOT send to the wrong recipient" evidence checks against both of these near-miss addresses.

3. **OE 20 / OE 22 field-name drift (Minor).** Both OEs say "Notes or Special Requirements must be updated." Universe verification: `tblRelocations01` schema has only "Special Requirements" field (multilineText); there is no "Notes" field. S3 Outcome 1.2 rubrics should check the `Special Requirements` field only. No block — the OE's intent is preserved by updating Special Requirements.

4. **Density projection at 50 midpoint is tight (Watch-item).** Recomputed midpoint from the actual OE list = ~49 (conservative floor 41, ceiling 56). This clears the 40 hard floor comfortably but sits at the 50 design target. If the agent short-circuits candidate exploration on OE 5 (Carmen no-reply verify), OE 8 (Road Runner candidate emails), or OE 12 (Mina audit thread candidates), midpoint drops toward 44 (THIN band). Recommend S3 keep all 10 write actions rubric-mandatory — dropping any (especially OE 26 calendar hold) collapses density.

5. **CRM create-only tool constraint (Advisory).** OE 25 correctly notes CRM engagements in this tool set are create-only. S3 Outcome 1.1 rubric for OE 25 must NOT check for a `crm_update_engagement` call (does not exist in MoveOps V2.1 tool catalog per `MoveOps_Base_Universe/6_Server_Tools_Details.json`).

6. **L26 canonical thread_ts value precision (Advisory).** The prompt-level L26 yield thinning noted in Verification_s1 (from 80%+ to ~40-60% failure) means S3 Outcome 1.2 rubric on OE 23 must require EXACT value match `thread_ts="1776997200.000000"` — not approximate. Slack `1776999900` (Mina C004 expansion ping, verified on C004 not C002) is filtered by "the audit thread" phrasing but is still a decoy S3 must actively reject.

7. **TZ offset -07:00 vs Universe_Index -04:00 drift (Advisory).** OE 26 correctly uses `-07:00` (US/Pacific PDT) per AGENTS.md moveops registry. Verification_s1 flagged Universe_Index today_horizon.json currently shows America/New_York (should be US/Pacific). Non-blocking — S3 should ground the Outcome 1.2 TZ check on AGENTS.md registry (US/Pacific), not Universe_Index.
