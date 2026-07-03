# Hardness Plan

## Persona and Business Function

- **Persona**: Robert Calloway — Owner / Licensed Mortgage Broker (`robert.calloway@keystonemortgage.com`; Slack `keystone_e85bc913c756` mapped to `r.calloway@keystonemortgage.com`).
- **Business Function**: Executive.
- **Universe**: keystone (single entity, mortgage brokerage; universe today 2026-04-28 America/New_York).
- **Anchoring scenario for S1**: `scenario_14b3ffde` — ransomware pay-vs-restore decision. Robert is the deciding persona (2 BTC ransom vs 72-hour cloud-backup restore path; Monday closings at risk). Richest cross-service surface (email 5 hits + Slack 20 hits + CRM 2 engagement notes + 4 DM channels + at-risk-closing loans). Second-choice fallback if S1 needs a pivot: `scenario_7da8f37a` (Marcus Webb departure — 146 email mentions, 16 in 2026-03; single-service-heavy).

## Levers Available

| # | Lever | Status | Evidence (path :: row_id or subject) | Cost range |
|---|---|---|---|---|
| 1 | Latching | yes | `email.emails.json :: email_email_b2572b3105dc` (Robert to Megan: "The demand is 2 BTC... restore from that point would require environment rebuild plus validation, with likely file gaps and manual reconstruction"). Raj's IT-authority framing anchors Robert on "restore is hard" — first-framing trap live. Additional anchor in `crm.crm_engagements :: crm_engagement_f1cb06ea7b65` note "Leadership weighing pay vs restore" | 5-8 |
| 2 | Structured-DB skip | yes | `crm.crm_engagements.json :: crm_engagement_b95df55fbf01` (2026-04-14 "Escalated to Robert. 3 borrower files in post-term access review; borrower notice may be needed") + `crm_engagement_f1cb06ea7b65` (2026-03-20 "2 BTC demand... 72 hrs old"). CRM engagement NOTE type is a structured surface agents rarely query when Slack/email chatter is rich. Also available: `mortgage_los.conditions.json` (32 rows, 8 outstanding across 4 loans) and `mortgage_los.document_checklist_items.json` (8,841 rows) as alternative KeyStone-native surrogates for the Brookfield SAP-subledger skip in Learnings §L10 | 4-7 |
| 3 | Missing reply | partial | Robert's 2026-03-20 request to Megan Sloane (`email_email_b2572b3105dc`) has no Sloane reply in the split — the pending-counsel state IS the puzzle; but this is a natural-narrative gap rather than a buried reply that flips a conclusion. Denise's 4/14 CRM escalation acts as the flipping data point on a different surface | 3-5 |
| 4 | Search-result-cap eviction | yes | Ransomware incident is dated 2026-03-20 (~5 weeks before universe today 2026-04-28). Any Slack search anchored on `#general` returns 55 messages; a "ransomware" keyword pull returns 4 in C001 + 1 in C008 + 15 more matching on adjacent keywords. Older Marcus/CFPB threads may crowd `#general` search cap; the 3/20 ransomware messages may be evicted from top results for keyword queries not tightly scoped | 3-5 |
| 5 | Thread-reply blindness | partial | Slack threads exist (`reply_count`, `thread_parent_id`, `latest_reply`) but the ransomware C001 exchange is a linear message chain rather than deep replies. Slack thread structure is present but under-utilized as the load-bearing surface for THIS scenario | 2-4 |
| 6 | Near-miss entity confusion | yes | `contacts.contacts.json` lists FIVE Bennett-* legal contacts (`lauren.bennett@icloud.com`, `lbennett@bennettfairlendinglaw.com`, `laura.bennett@bennettethicslaw.com`, `lbennett@bennettcyberlaw.com`, `laura.bennett@bennettstokeslaw.com`) — but PersonaBrief pins Laura Bennett as EMPLOYMENT counsel; cyber counsel is Megan Sloane at `wardbarrettlaw.com`. `bennettcyberlaw.com` is a live near-miss trap for routing the ransomware to the wrong firm. Also: Robert's email is `robert.calloway@keystonemortgage.com` but his Slack profile carries `r.calloway@keystonemortgage.com` and Denise addresses him at `r.calloway` in `email_email_fc27f9914e8b` | 3-5 |
| 7 | Multi-write diversification | yes | Universe supports writes across 8 services: `email` (reply Megan / update Denise / notify Grace), `slack` (C001 status post + DM update to D_grace_robert_denise), `crm` (append engagement note), `filesystem` (upload privileged decision memo), `contacts` (no write per typical usage), `mortgage_los` (potentially update condition status on at-risk closings), `quickbooks` (no natural write here). Realistic 3-4 writes across 3-4 services for an executive-brief prompt | 9-12 |
| 8 | Multi-link chain | yes | A → B → C chain live: A = Raj IT escalation email + C008 initial "Anyone else unable to get into LOS?" (findable via broad search); B = Denise's 3/20 privileged email + Megan Sloane engagement (moderate-effort follow-up); C = CRM engagement `crm_engagement_b95df55fbf01` (4/14 escalation — borrower-notice consideration; low-discovery structured DB). Three services (email → Slack DMs → CRM) chained | 6-9 |
| 9 | Universe-grounded gotcha | yes | (a) KeyStone TRID landmine: LE within 3 business days of application; CD 3 business days before closing (`mortgage_los.disclosures` absent from split — `document_checklist_items` may carry disclosure rows; agent must not fabricate CD timing). (b) Marcus Webb departed-employee trap live but adjacent scenario. (c) No account-number cross-entity trap (single entity). (d) `records_dated_after_today = 8940` per today_horizon.json — legitimate future rows but a groundedness risk if the prompt claims "as of today" against forward-dated status | 3-5 |
| 10 | Reversal / supersession | yes | Denise's 2026-03-20 privileged emails (`email_email_985ac55f2911`, `email_email_fc27f9914e8b`) outline a PRELIMINARY reporting-obligation / borrower-notice plan ("we likely have reporting and notification obligations once scope is confirmed"). That preliminary plan is superseded (or at minimum evolved) by the 2026-04-14 CRM engagement `crm_engagement_b95df55fbf01` ("3 borrower files in post-term access review; borrower notice may be needed") — a fresher, more specific escalation the agent must reconcile. Existing-output anchor per Learnings §L25 | 4-6 |
| 11 | Net-vs-gross framing | partial | Applies conceptually: "72-hour backup restore" is the GROSS optimistic frame; agent must NET out (a) environment rebuild time (b) file gaps for activity since 2026-03-17 (~3 days of pipeline activity) (c) manual reconstruction cost. Not a clean numeric net-vs-gross in the accounting sense; a decision-quality framing lever. Lower yield than L8/L9/L10 on this scenario | 4-7 |

**Playbook-lever inventory: 8 yes, 3 partial, 0 no. Well past the 3-lever floor.**

## Selected Levers (5)

Chosen 5 anchors from the Learnings-empirical playbook, mapped to Playbook lever numbers above. All selected levers cite specific Learnings entries per HARDNESS runbook Step 4.

- **Learnings §L8 (three reductions across three services) → Playbook Lever 8 (Multi-link chain, cost 6-9, midpoint 7.5)**. Rationale: the ransomware disposition depends on triangulating (a) Raj's IT assessment in email + C001 Slack + C008 initial trigger, (b) Denise's compliance framing in privileged email + `D_denise_grace` DM, and (c) the CRM engagement escalation trail. Three structurally different systems, each holding a distinct piece. Learnings §L8: "Stack reductions across DIFFERENT structured systems, each requiring a different search strategy."

- **Learnings §L9 (authority-figure dismissal, soft verb per §L24) → Playbook Lever 1 (Latching, cost 5-8, midpoint 6.5)**. Rationale: Raj Anand's technical-authority framing ("restore path requires environment rebuild + validation, likely file gaps and manual reconstruction") plausibly nudges an agent toward paying. Prompt-side authority phrasing will follow §L24 soft-verb convention ("Raj's read was that restore looks costly" NOT "restore is impossible"). Learnings §L9 is the single most reliable stumping mechanism observed; §L24 preserves QC Truthfulness.

- **Learnings §L10 (structured-DB skip on non-conversational surface) → Playbook Lever 2 (Structured-DB skip, cost 4-7, midpoint 5.5)**. Rationale: `crm.crm_engagements` is the KeyStone-native surrogate for Brookfield's SAP subledger — a 472-row structured surface agents rarely query when email/Slack chatter is rich. `crm_engagement_b95df55fbf01` (2026-04-14 borrower-notice escalation) is the load-bearing atom the agent must find to reconcile Denise's 3/20 preliminary plan with the current state. Alternative surrogates (`mortgage_los.conditions`, `document_checklist_items`) available but CRM engagements are the higher-yield surface because they carry decision-relevant prose rather than tabular state. Adapts Learnings §L10 SAP invisibility pattern to KeyStone.

- **Learnings §L25 (existing-output anchor) → Playbook Lever 10 (Reversal/supersession, cost 4-6, midpoint 5)**. Rationale: Denise's 2026-03-20 privileged emails contain a preliminary borrower-notice / SAR-consideration plan. That plan is a "previously staged artifact" that superficially satisfies "the compliance path is set" but is missing the fresher signal in the 4/14 CRM engagement about specific borrower files under post-term access review. Agent may latch on Denise's 3/20 plan and never reconcile against the 4/14 CRM data. Learnings §L25: "the strongest single-mechanism stump observed" — plant a previously staged artifact that lacks one or two rubric-tested fields.

- **Learnings §L26 (decoy parent thread) → Playbook Lever 4 (Search-result-cap eviction, cost 3-5, midpoint 4)**. Rationale: three plausible Slack parent threads coexist for the 2026-03-20 window — C001 (executive discussion — Robert's canonical "I need the ugly version" at ts 1774032333), C002 (loan-processing — Grace's "Need quick read from processing on Monday closings" at ts 1774029240), and C008 (it-support — initial "Anyone else unable to get into LOS?"). A Slack write for an executive brief belongs in C001 (or a specific DM), not C002/C008 which are more topically relevant to the tactical fallout. Agents anchoring on "Monday closings" keyword will post to C002. Learnings §L26: decoy parent doesn't need eviction — it needs to look more topically plausible.

**Not selected (with reasoning):**
- Learnings §L4 (near-miss entity alone) — supporting-density-only lever per Learnings ("~0% fail alone"). The 5 Bennett variants + Sloane routing choice STILL enters the trajectory via contact-lookup calls (adds density) but is not a primary stump anchor.
- Playbook Lever 11 (net-vs-gross) — partial fit only; ransomware decision quality is qualitative-quantitative hybrid, not the clean accounting framing this lever expects.
- Playbook Lever 5 (Thread-reply blindness) — Slack thread structure present but under-populated for this scenario; §L26 decoy-parent covers the Slack-write miss more cleanly.

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (persona resolve, channel lookup, contact resolve, temporal scoping) | 5-8 | 6.5 |
| §L8 → Playbook L8 (Multi-link chain across email/Slack/CRM) | 6-9 | 7.5 |
| §L9 → Playbook L1 (Latching / authority dismissal) | 5-8 | 6.5 |
| §L10 → Playbook L2 (Structured-DB skip on CRM engagements) | 4-7 | 5.5 |
| §L25 → Playbook L10 (Existing-output anchor / supersession) | 4-6 | 5 |
| §L26 → Playbook L4 (Decoy parent thread search) | 3-5 | 4 |
| Write actions (3-4 writes × ~3 supporting reads each: email reply Sloane, Slack C001 or DM update, CRM engagement append, filesystem privileged memo upload) | 9-12 | 10.5 |
| Cross-service triangulation buffer (contact re-resolve, borrower-loan cross-reference, ambient at-risk-closing status pulls) | 5-8 | 6.5 |
| **TOTAL projected** | **41-63** | **52.0** |

**Gate result**: midpoint 52.0 ≥ 50 = **PASS** (design target met).

Cross-checks:
- Low-end (41) is above the 40-floor. Even in the pessimistic corner the projection stays inside the THIN_DENSITY band and does not fall to INSUFFICIENT.
- High-end (63) leaves headroom without cresting into contrivance.
- Lever independence: no two levers count the same tool call (L8's email/Slack/CRM reads are separate from L9's Raj-email re-reads and L26's Slack-thread search).
- Write actions assume the prompt asks for a decision brief + at least one downstream operational update; a lighter write mix would drop the projection ~2-3 calls but still land in PASS.

## Service Breadth (v11 G1)

Projected trajectory distribution across the 8 KeyStone services available in this universe. `oracle_gl`, `sap_subledger`, `blackline`, `records_vault`, `linear`, `airtable` are Brookfield/MoveOps services and do NOT appear in KeyStone tool-catalog `Mortgage_Base_Universe/6_Server_Tools_Details.json`.

| Service | Calls | % of total | Dominant flag |
|---|---:|---:|---|
| email | 12 | 23% | — |
| slack | 10 | 19% | — |
| mortgage_los | 8 | 15% | — |
| crm | 6 | 12% | — |
| filesystem | 5 | 10% | — |
| contacts | 4 | 8% | — |
| quickbooks | 4 | 8% | — |
| stripe | 3 | 6% | — |
| **Distinct services** | **8** | — | — |
| **Total** | **52** | 100% | — |

**Breadth gate**: 8 distinct services, each ≥ 5%; dominant `email` at 23% (well below 60%) = **PASS**. The projected trajectory spans the full KeyStone service catalog — no single-service context lock-in.

Notes:
- `filesystem` shown here is used as an agent WRITE surface (privileged memo upload for the decision-record) — it has no seeded data in the split, per Learnings §L28 tool-variant caution. If the S1 prompt requires a filesystem upload, the OE writer must specify path + content requirements atomically to avoid the L28 version-bump-vs-fresh-upload trap.
- `quickbooks` and `stripe` are exercised as ambient checks (any pending bill from Ward Barrett Law / Sloane, any outbound stripe transfer for retainer). No hits currently seeded — the reads register as null checks, still counting toward breadth.
- `mortgage_los` calls span both `loans` (at-risk closing status) and `conditions` (structured-DB skip alternate surface if the agent double-checks).

## Stump Hypothesis (4 predictions)

1. **[HIGH] Agent skips the CRM engagement surface entirely and treats Denise's 3/20 privileged emails as the authoritative compliance plan.** Mechanism: Learnings §L10 (structured-DB skip on non-conversational surface) + §L25 (existing-output anchor). Predicted rubric outcome: fails the evidence-anchored rubric on the 4/14 borrower-notice escalation (`crm_engagement_b95df55fbf01`) that reconciles the "3 borrower files in post-term access review" state against Denise's original prelim plan. Anchoring scenario: `scenario_14b3ffde`.

2. **[HIGH] Agent latches on the technical-authority framing that restore is costly and materially misweights the pay-vs-restore analysis toward payment for Monday-closings urgency.** Mechanism: Learnings §L9 (authority-figure dismissal, applied with §L24 soft verb) + Playbook Lever 1 (latching). Predicted rubric outcome: fails a decision-quality rubric that requires the brief to enumerate the specific restore-path considerations (72-hour data gap, environment rebuild, validation windows) as tradeoffs rather than treat restore as effectively foreclosed. Anchoring scenario: `scenario_14b3ffde`.

3. **[MED] Agent posts an executive Slack update to the topically-plausible C002 (loan-processing) or C008 (it-support) parent thread instead of the canonical C001 executive-general thread (or the D_grace_robert_denise 3-way DM).** Mechanism: Learnings §L26 (decoy parent thread). Predicted rubric outcome: channel-pinned Slack-write rubric fails on `channel_id` check. Dependent on OE writer pinning the canonical channel — if OE is channel-agnostic, drop to LOW. Anchoring scenario: `scenario_14b3ffde`.

4. **[MED] Agent routes cyber-counsel outreach to a Bennett-* firm (`bennettcyberlaw.com` in particular) rather than Megan Sloane at `wardbarrettlaw.com`.** Mechanism: Learnings §L4 (near-miss entity — supporting only; five Bennett-* email contacts of which `bennettcyberlaw.com` is a semantic near-miss for "cyber counsel") + Playbook Lever 6 (near-miss entity confusion). Predicted rubric outcome: contact-resolution rubric fails on `recipient` field for any counsel-outreach write. Note: §L4 says near-miss alone is ~0% fail; this hypothesis is MED only because the ransomware scenario elevates the "cyber counsel" semantic pull relative to the persona-brief pin on Megan Sloane. Anchoring scenario: `scenario_14b3ffde`.

## Hardness Score

**5/5 — PASS.**

- Levers selected: 5 (default target hit).
- Density midpoint: 52.0 ≥ 50 → PASS.
- Service breadth: 8 distinct, dominant 23% → PASS.
- All 5 selected levers cite a specific Learnings §L<n> entry.
- Anchoring scenario named: `scenario_14b3ffde` (ransomware pay-vs-restore).

## Hardness Brief for the Prompt Writer

Write the S1 prompt in Robert Calloway's voice (Owner / Licensed Mortgage Broker, KeyStone Mortgage Partners) anchored on **`scenario_14b3ffde`** — the 2 BTC ransomware / 72-hour-cloud-backup decision that has been live since 2026-03-20 and remains unresolved as of universe today 2026-04-28. Do NOT name any tools, IDs, thread timestamps, channel IDs, or specific email subjects. Do NOT hint that any circulating framing is wrong (Learnings §L15 implicit-prompts rule). Robert should believe the current state and ask the assistant to produce an executive decision brief with downstream operational updates — the assistant must self-discover that (a) Denise's 3/20 preliminary reporting-obligation plan has been superseded by a fresher 4/14 escalation about specific borrower files in post-term access review (Learnings §L25 existing-output anchor via Playbook Lever 10 supersession), (b) Raj's authority-framing on the restore path should be interpreted as a tradeoff enumeration not a foregone conclusion (Learnings §L9 authority dismissal, soft-verb per §L24), (c) the evidence trail runs across email → Slack (C001 canonical, C002/C008 decoy) → CRM engagement notes and the CRM surface is the structured skip (Learnings §L8 multi-service reductions + §L10 structured-DB skip via Playbook Levers 8 and 2), (d) the ambient at-risk-closing loans (LN-2026-00601 and others) are a separate ops-triage layer not the decision anchor. Require 3-4 writes across 3-4 services (default: reply to outside cyber counsel via email; status post to canonical Slack channel or DM; CRM engagement update; filesystem privileged decision memo upload — the last is optional based on prompt design). Target density: midpoint 52 (range 41-63) across 8 KeyStone services with dominant service ≤ 25%. Watch for L26 decoy-thread channel choice on the Slack write and L28 tool-variant trap on the filesystem write. NEVER state the pay-vs-restore disposition in the prompt or any injected artifact (Learnings §L6 correct-answer-in-artifact rule) — the brief must be DERIVED from the trajectory, not repeated from any seeded message.
