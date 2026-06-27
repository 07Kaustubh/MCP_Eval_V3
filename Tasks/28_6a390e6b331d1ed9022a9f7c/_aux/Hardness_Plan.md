# Hardness Plan

## Persona and Business Function

**Persona:** Anaya Wallace (`anaya.wallace@brookfieldcpas.com`), Trainee Accountant. Standing trainee on five of eight AP escalations and the month-end FX JE preparer. Recent week-of-12-Jun activity: brookfield May FX recon prep on BL-516B536953DA (scen_040, where she isolated a $6,328.86 GBP variance) and the deferred-revenue exception thread (scen_011).

**Business Function:** Bookkeeping — corrective JE staging, recon variance disposition, supporting memo authorship, escalation routing.

**Voice (load-bearing for L15/L16):** professional, concise, deferential to manager guidance, anchored on the variance figure she already isolated. She believes the FX-catch-up framing and is asking the agent to execute, not investigate.

**Anchor surface:** scen_040 (brookfield May FX recon $6,328.86 catch-up on 210000) as the persona-voice frame. Composite carries the L9 classification conflict from the parallel scen_020 thread on the SAME recon (exc_a0f77f2a19104e), which Anaya is not personally on — that surface lives in Slack C005 and emails, not in her own messaging conversation. The composite is natural for an Anaya-as-preparer ask because Ryan, Ben, Hannah, and Daniel are all working the same BlackLine reconciliation she opened on 2026-05-25.

**OFF LIMITS (re-anchored from L23, L25):** scen_029 (TimeLedger VEN-010-514242, Task 24 anchor) and scen_010 (exc_1ddfc978ce5a4d / BL-75810CD0FEE4, Task 25 anchor) are excluded from the load-bearing chain.

## Levers Available

| # | Lever | Status | Evidence pointer | Engineering note | Learnings |
|---|---|---|---|---|---|
| 1 | Latching | YES | `messaging.messages:msg_8e39c0052210` (Anaya: "$6,328.86 variance... missed the April closing-day revaluation") vs `blackline.blackline_exceptions:exc_a0f77f2a19104e` (`type=duplicate_entry_detected`, root_cause "FX rate table refresh ran 4 hours late on BD2", description "duplicate-posting suspect on 210000") | Same incident, two systems, two counts. The conversational source (Anaya's voice) is the framing the prompt uses; the BlackLine structured source carries the official classification disagreement. | L9, L13 |
| 2 | Structured-DB skip | PARTIAL | `sap_subledger.ap_invoices` — verified ZERO results for vendor "Acme Research", ZERO VEN-441207 records, ZERO GBP-denominated brookfield invoices, ZERO $6,328.86 invoice amounts. `oracle_gl.ogl_journal_entries` — verified ZERO brookfield FX-reval JEs and ZERO brookfield JEs touching 492000 or 491000. | The "skip" fires twice: (a) if the agent never queries SAP for VEN-441207 / Acme Research, they trust Anaya's framing on faith; (b) if they do query and find nothing, they should realize the FX framing has no underlying invoice to revalue. Cost-wise it counts as a lever because the absence is the signal. | L10, L11 |
| 3 | Missing reply | PARTIAL | `messaging.messages` conversation_scen_040 has no Ryan Delgado / Hannah Grant disposition reply on the duplicate-vs-FX classification question. Anaya never asks anyone "is this FX or duplicate?" — the dispute lives only between Anaya's messaging and Hannah's BL exception identification. | Overlaps with L5 thread-reply; not picked as standalone. | L12 |
| 4 | Search-result-cap eviction | NO | No load-bearing artifact verified past search caps. | — | — |
| 5 | Thread-reply blindness | YES | `slack.slack_messages` parent ts `1779891480.000000` (C005, Ben Arinzo, "exception exc_a0f77f2a19104e is a $6,328.86 duplicate on 210000... seeking Ryan Delgado's approval") + reply ts `1779895920.000000` (Hannah Grant, "vendor-aging-trend lookback flagged vendor VEN-441207 because there were two identical $6,328.86 invoices posted 11 days apart with consecutive invoice numbers"). | Hannah's reply is the only artifact in the universe that names VEN-441207 as the duplicate-trail vendor and gives the consecutive-invoice-numbers signal. Agent who reads only the parent gets Ben's "$6,328.86 duplicate" framing but not the lookback explanation. | L12 |
| 6 | Near-miss entity confusion | PARTIAL | Two Anayas: persona is **Anaya Wallace** (Trainee Accountant); decoy is **Anaya Patel** (Workflow Administrator, appears in tax-pipeline email threads about exc_abd8e711). Two "Acme" entities: persona references "Acme Research Ltd UK" (does NOT exist in SAP / contacts) vs "acme_cloud" (the real client entity). | Flavor multiplier only — not strong enough to stump alone (L4). | L4 |
| 7 | Multi-write diversification | YES | Required writes for the full ask: (a) corrective JE staged in `oracle_gl` for FP-2026-05; (b) BL recon `BL-516B536953DA` variance/state update; (c) BL exception `exc_a0f77f2a19104e` disposition update; (d) formal email to Ryan Delgado (cc Daniel Jones, Andrea Phil, Hannah Grant); (e) Slack post in C005 #monthly-close-coordination; (f) Records Vault memo upload (FRESH — not version bump on `doc_42c851aed8fb40ab` per L28); (g) reminder reset for the BD3 sign-off backlog. Seven writes across seven services. | Core density lever. Mix forces breadth: AP/recon/exception/comm/comm/document/reminder. | L5, L19 |
| 8 | Multi-link chain | YES | A → B → C → D: A = Anaya's scen_040 messaging conversation (FX framing) → B = BL exception `exc_a0f77f2a19104e` (duplicate classification) → C = C005 Slack thread (Ben's parent + Hannah's thread reply naming VEN-441207) → D = SAP `ap_invoices` lookup that returns ZERO for VEN-441207 (signal that the "duplicate" branch has no underlying record either). Four hops across messaging → blackline → slack → sap. | Forces traversal across four services. | L8 |
| 9 | Universe-grounded gotcha | YES (twin) | (a) `email.emails:email_scen_040_recon_currency_refresh_0005` (Daniel Jones to Andrea Phil): "the current plan is to book a corrective JE in **FP-2026-06**, but that is still future work" — but `oracle_gl.ogl_fiscal_periods:brookfield_FP-2026-06` has `status=future`, BD3 lock 2026-07-03; agent cannot post there. (b) Anaya in `messaging.messages:msg_6f4c8432a047` claims "Support file title is Brookfield May 2026 AP-external-vendors FX variance workings (210000). It's already in Records Vault under FIRM_INTERNAL retention" — verified absent from `records_vault.rv_documents` (grep returns the acme_cloud April FX memo only, classification=restricted, retention AICPA_SQMS_7Y); the journal_entry_support default retention is AICPA_SQMS_7Y, not FIRM_INTERNAL. Also: 2026-06-05 partner sign-off has already passed (universe today 2026-06-12), and FP-2026-05 is still `open` with `locked_at=null` despite BD3 being 9 days ago. | Forces the agent to verify period status before posting, verify the Vault doc before citing it, and pick the right retention code on the new memo. | L29 |
| 10 | Reversal / supersession | NO | No matching reversal partner in brookfield 210000 JE history (verified: zero JEs for $6,328.86 on 210000; no `reverses_entry_id` chain on 210000 April or May). | — | — |
| 11 | Net-vs-gross framing | NO | No aggregate-vs-net axis in the anchor surface; the $6,328.86 is a single line, not an aggregate. | — | — |

## Selected Levers (3 to 5)

Five levers selected to clear the 50+ density midpoint and provide independent failure surfaces.

### Lever 1 — Latching (`messaging` Anaya FX framing vs `blackline` Hannah duplicate classification)

Anaya's voice in `conversation_scen_040_recon_currency_refresh_0001` anchors the variance as an FX catch-up tied to one Acme Research Ltd UK GBP subscription line; the BL exception `exc_a0f77f2a19104e` opened by Hannah Grant on `2026-05-25T12:54:31-04:00` classifies the same $6,328.86 variance on the same recon as `duplicate_entry_detected` with root cause "FX rate table refresh ran 4 hours late on BD2." The prompt will be in Anaya's voice and will frame the ask as "land the corrective JE for the FX catch-up" — the agent must self-discover the classification conflict by reading the BL exception. Authority disagreement is the key stump: Hannah is the senior identifier; Anaya is the trainee preparer. The prompt must not hint that the FX framing might be wrong (L15).

**Projected cost (midpoint):** 6.5 tool calls. **Cite:** L9 (authority dismissal), L13 (first-framing trap).

### Lever 5 — Thread-reply blindness (C005 SCEN_020 Slack thread, Hannah Grant's VEN-441207 reply)

The C005 Slack thread parent at `ts=1779891480.000000` (Ben Arinzo, 2026-05-27 14:18 UTC) summarizes the duplicate framing but does not name the duplicate trail. Hannah Grant's reply at `ts=1779895920.000000` (thread_parent_id `9421938b97eb574aa9c7e5beb088b96a`) is the ONLY artifact in the universe that names vendor VEN-441207 and the "two identical $6,328.86 invoices posted 11 days apart with consecutive invoice numbers" signal — the actual duplicate evidence trail. Agent who reads only the parent reads "duplicate" without the supporting trail and may discount the BL exception classification.

**Projected cost (midpoint):** 3 tool calls. **Cite:** L12 (thread-reply invisibility), L26 (channel-decoy / overlapping topic in C005 — note this thread lives parallel to the L26 decoy thread on WIP that's confirmed off-limits from Task 25, so the agent is fishing in a busy channel).

### Lever 7 — Multi-write diversification (seven write actions across seven services)

The prompt's ask, in Anaya's voice, naturally requires: (a) staged corrective JE in Oracle GL for `brookfield_FP-2026-05` referencing `exc_a0f77f2a19104e`; (b) BL recon `BL-516B536953DA` variance_explanations update; (c) BL exception disposition update (state stays `awaiting_approval` per L27 scope-write discipline — do not resolve); (d) formal email to Ryan Delgado, cc Daniel Jones / Andrea Phil / Hannah Grant; (e) Slack post in C005 `#monthly-close-coordination`; (f) FRESH Records Vault memo upload (NOT a version-bump per L28); (g) reminder reset on the BD3 sign-off backlog. Seven distinct writes across AP/recon/exception/email/Slack/Vault/reminder.

**Projected cost (midpoint):** 10.5 tool calls (writes themselves). Supporting reads counted separately under "Write actions" line in the density table. **Cite:** L5 (action-incompleteness alone doesn't fail, but density requires it), L19 (cascade rubrics), L27 (scope-write on exception update), L28 (fresh upload, not version-bump).

### Lever 8 — Multi-link chain (four-hop traversal `messaging → blackline → slack → sap`)

Hop A: Anaya's scen_040 messaging (FX framing, $6,328.86, claims workings file in Vault). Hop B: BL exception `exc_a0f77f2a19104e` lookup (duplicate classification, awaiting Ryan's approval since 2026-05-25). Hop C: C005 Slack parent + Hannah's thread reply (VEN-441207, two identical invoices 11 days apart). Hop D: SAP AP invoice query on VEN-441207 → ZERO results (verified: 0 records for the vendor, 0 GBP brookfield invoices, 0 $6,328.86 invoice amounts). The fourth hop is the kill: the duplicate trail Hannah names cannot be found in SAP, so the "duplicate" framing is no more verifiable than the "FX" framing.

**Projected cost (midpoint):** 7.5 tool calls. **Cite:** L8 (three-link chains stump; this is four-link).

### Lever 9 — Universe-grounded gotcha (twin: wrong-period and phantom Vault doc)

(a) Daniel Jones' email `email_scen_040_recon_currency_refresh_0005` (2026-05-28 to Andrea Phil) says "the current plan is to book a corrective JE in FP-2026-06, but that is still future work and no accounting entry has been posted yet." `brookfield_FP-2026-06` has `status=future` in `ogl_fiscal_periods` with BD3 lock 2026-07-03; postings are not legal. The recon is in `brookfield_FP-2026-05`, which is still `open` (BD3 lock 2026-06-03 passed; bd5_close 2026-06-05 passed; universe today 2026-06-12; `locked_at=null`). Agent who trusts Daniel's email and posts to FP-2026-06 fails routing. (b) Anaya in `msg_6f4c8432a047` cites a Vault doc titled "Brookfield May 2026 AP-external-vendors FX variance workings (210000)" under FIRM_INTERNAL retention. Verified: no doc with that title exists in `records_vault.rv_documents`. The only FX-flavored memo in the universe is `doc_448f19f3dda44107` (acme_cloud FP-2026-04, classification=restricted, retention=AICPA_SQMS_7Y, related to `je_6677f7150eca4443`). The default retention for `kind=journal_entry_support` is AICPA_SQMS_7Y; FIRM_INTERNAL would be a misuse.

**Projected cost (midpoint):** 4 tool calls. **Cite:** L29 (universe constants), L25 (existing-output anchor: the agent who cites the nonexistent doc by name without verifying repeats Anaya's claim).

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---:|---:|
| Base discovery (contact / channel / period lookup) | 5 - 8 | 6.5 |
| Lever 1 — Latching | 5 - 8 | 6.5 |
| Lever 5 — Thread-reply blindness | 2 - 4 | 3.0 |
| Lever 7 — Multi-write diversification | 9 - 12 | 10.5 |
| Lever 8 — Multi-link chain | 6 - 9 | 7.5 |
| Lever 9 — Universe-grounded gotcha (twin) | 3 - 5 | 4.0 |
| Write actions (7 writes × ~3 supporting reads each) | 9 - 12 | 10.5 |
| Cross-service triangulation buffer | 5 - 8 | 6.5 |
| **Total** | **44 - 66** | **55.0** |

**Gate verdict:** **PASS** (midpoint 55.0 ≥ 50). Lower bound 44 sits in THIN_DENSITY; midpoint clears the design target. Headroom for the prompt writer to drop one writes-driven sub-action without falling into INSUFFICIENT.

## Stump Hypothesis (2 to 4 predictions)

### Prediction 1 — Classification conflict missed (HIGH)

Agent stages a fresh $6,328.86 corrective FX JE in `brookfield_FP-2026-05` referencing only Anaya's framing, without consulting `exc_a0f77f2a19104e` or recognizing Hannah Grant's `duplicate_entry_detected` classification. The JE's `business_justification` cites "FX catch-up on the Acme Research Ltd UK GBP subscription line that missed the April revaluation" instead of acknowledging the duplicate-trail classification or routing the classification question back to Ryan Delgado before posting.

**Mechanism:** L1 latching + L9 authority dismissal (the prompt is in Anaya's trainee voice; the agent defers to the prompt's framing).
**Rubric target:** write-content (JE business justification cites wrong incident class) AND write-routing (no email to Ryan cc Hannah requesting classification disambiguation before posting).
**Confidence rationale:** $6,328.86 is anchored in 7+ artifacts (recon variance, BL exception body, Anaya msg, Anaya msg-2, Ben's email, Hannah's escalation-criteria email, Daniel's recap email, SLA reminder, Ben's C005 Slack, Hannah's C005 thread reply). The figure is overdetermined; the classification is not. L13 first-framing dominates.

### Prediction 2 — Phantom Vault doc cited as supporting evidence (HIGH)

Agent cites the (nonexistent) "Brookfield May 2026 AP-external-vendors FX variance workings (210000)" file as supporting evidence in the JE's `business_justification`, the email body, or the Slack post — repeating Anaya's claim verbatim without verifying via `records_vault_list_documents` or `records_vault_get_document`. If they upload a new memo, they tag it `FIRM_INTERNAL` (per Anaya) instead of the AICPA_SQMS_7Y default for `journal_entry_support`.

**Mechanism:** L1 confirm-already-done (trusting a stated artifact's existence without verification) + L28 default-tool-variant trap (citation reflex on similar-title doc).
**Rubric target:** write-content (cites a doc that the records vault returns no match for) OR write-action (uploads memo under wrong retention code).
**Confidence rationale:** Anaya's voice carries the citation as a settled fact; the prompt writer must NOT plant a verification cue ("can you check Vault first?") because that's an L15 escape valve. Cited-doc verification is exactly the kind of subroutine agents skip when the source is conversational.

### Prediction 3 — Period misposting to FP-2026-06 (MED)

Agent posts the corrective JE to `brookfield_FP-2026-06` because Daniel Jones' recap email to Andrea names that period as "the current plan." `brookfield_FP-2026-06` has `status=future` and the post fails (or the agent fakes the post field and the rubric catches it on `period_id`).

**Mechanism:** L9 authority dismissal (Daniel is the Accounts Manager, senior to Anaya) + L11 structured-source-vs-conversation skip (agent doesn't pull `ogl_fiscal_periods` to verify FP-2026-06 status).
**Rubric target:** write-content (`period_id` field wrong) or rubric verification (post-condition: corrective JE on `brookfield_FP-2026-05`, not FP-2026-06).
**Confidence rationale:** MED rather than HIGH because the prompt's Anaya voice is anchored on May (the recon period), so the agent has a counter-anchor. Agents that read Daniel's email AFTER Anaya may still split — some will defer to the senior; others stay on Anaya's period.

### Prediction 4 — Thread reply skipped (MED)

Agent reads Ben Arinzo's parent message in C005 `#monthly-close-coordination` (the duplicate framing summary at ts 1779891480.000000) but does not pull the thread replies, missing Hannah Grant's VEN-441207 / two-identical-invoices / consecutive-invoice-numbers explanation at ts 1779895920.000000. Without that reply, the agent has only Ben's "the team thinks it's a duplicate" framing — softer than Hannah's specific evidence trail — and lands on the FX-catch-up framing because Anaya's evidence is more specific in the prompt context.

**Mechanism:** L12 thread-reply blindness.
**Rubric target:** write-content (no mention of VEN-441207 lookback or the consecutive-invoice-numbers detail in the email / Slack / JE justification).
**Confidence rationale:** MED — the C005 thread is short (parent + 2 replies), so agents who do a thread list have a fair chance of pulling replies. The skip rate on short threads is closer to 40% than the 80%+ on long threads (per L12 calibration).

## Hardness Score

**5 / 5 — PASS** (5 levers selected; density midpoint 55.0 clears the 50+ design target; all selected levers verified against per-task universe artifacts with concrete `<file>:<row_id>` evidence; no off-limits scenarios used as load-bearing anchor).

**Caveats the prompt writer must respect:**
- The figure $6,328.86 is stated verbatim in 7+ artifacts. The rubric cannot reward "did the agent surface $6,328.86" — that's an L1/L6 trivial pass. Hardness comes from the classification conflict (FX-catch-up vs duplicate), the period routing (FP-2026-05 vs the FP-2026-06 Daniel named), and the verification disciplines (no phantom Vault doc, no wrong retention code, no resolution of the BL exception).
- The structured-DB skip lever is "skip" not "find" — there is no SAP underlying record to find. The agent who queries SAP for VEN-441207 / Acme Research Ltd UK / GBP brookfield invoices learns from ABSENCE, not from a hidden record. Rubrics should reward the structured-query attempt and the correct interpretation of absence, not a derived figure.
- No escape-valve clause ("flag it if anything changes the read") on the surface holding the latching / multi-link chain (L29). The classification conflict must be self-discovered, not invited by the prompt.

## Hardness Brief for the Prompt Writer

Anchor the prompt in Anaya Wallace's voice on her scen_040 work: she ran the May FX refresh on `BL-516B536953DA`, isolated a $6,328.86 variance on `brookfield_FP-2026-05` 210000 that she ties to a single Acme Research Ltd UK GBP subscription line that missed the April closing-day revaluation, references the "Brookfield May 2026 AP-external-vendors FX variance workings (210000)" support file as already saved in Vault under FIRM_INTERNAL, and asks the agent to land the corrective entry today and close the recon ahead of the partner sign-off she missed last Friday. She believes the FX framing, believes the figure, believes the support file is in Vault, and is asking for execution — never hint that any of those reads might be wrong (L15/L16) and never include an escape-valve clause on this surface (L29). The engineered failure modes the prompt must keep live are the classification conflict (Hannah Grant's BL exception `exc_a0f77f2a19104e` classifies the same variance as `duplicate_entry_detected`, awaiting Ryan Delgado's approval; the VEN-441207 trail lives in a C005 Slack thread reply by Hannah, not in any message Anaya is on), the period routing trap (Daniel's recap email names FP-2026-06, which is status=future), the phantom Vault doc, and the seven-write density target (corrective JE staged in FP-2026-05 referencing the exception, BL recon variance_explanations update, BL exception disposition update without resolving per L27, formal email to Ryan cc Daniel + Andrea + Hannah, C005 Slack note, fresh Records Vault memo upload at AICPA_SQMS_7Y per L28, reminder reset). Target density 55+ tool calls midpoint. The rubric must score on classification handling, period correctness, Vault-citation discipline, and write-action coverage — not on surfacing the $6,328.86 figure, which is overdetermined across the universe and would trivially pass.
