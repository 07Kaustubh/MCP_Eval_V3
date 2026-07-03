# Council B — S2 Adversarial Report

**Task:** 35_6a4421ec8169e23828bb442d
**Universe:** keystone (today = 2026-04-28)
**Phase:** S2 Oracle Events (adversarial QC)
**Perspectives:** B3 (density), B4 (lever preservation), B8 (forward map), B9 (reverse map)

## Upstream inputs consulted

- `5_Prompt.txt` (399-word Owner voice, ransomware pay-vs-restore + borrower-notice reconciliation)
- `6_Oracle_Events.txt` (27 OE steps: OE 1–17 discovery, OE 18–21 writes, OE 22–27 verification)
- `_aux/Hardness_Plan.md` (5 selected levers L8/L9/L10/L25/L26; density midpoint 52; service breadth 8)
- `_aux/Verification_s1.md` (S1 verdict PASS; 3 propagate flags carried to S2)
- Universe atoms deep-queried via `python3` on `_aux/Universe_Split/*.json` — 22/22 CRM engagement IDs verified; 10/10 Slack timestamps verified; 6/6 email IDs verified; Sloane reply-absence verified (Sloane appears only as recipient, never as sender).

---

## B3 Density projection

Component-by-component projection across the 27 OE steps (OE 22–27 are verification guardrails, not new calls). Reads include realistic query-variant fan-out; writes count once each.

| Component | Low | Mid | High |
|---|---:|---:|---:|
| Base discovery (persona resolve, folder/label scan, service inventory) | 3 | 4 | 5 |
| OE 1 — contacts_search_contacts (Sloane) | 1 | 2 | 3 |
| OE 2 — search_emails (Raj escalation, 2-3 query variants) | 2 | 3 | 4 |
| OE 3 — get_email_by_id (Robert 3/20 counsel request) | 1 | 1 | 1 |
| OE 4 — get_email_by_id × 3 (Denise 3/20 privileged trio) | 3 | 3 | 3 |
| OE 5 — search_emails (Sloane reply check, 2 query variants) | 1 | 2 | 3 |
| OE 6 — channels_list (find leadership channel) | 1 | 1 | 2 |
| OE 7 — conversations_search_messages (ransomware, 3-4 query variants) | 2 | 4 | 5 |
| OE 8 — conversations_history / search (Raj later readout) | 1 | 2 | 3 |
| OE 9 — conversations_search_messages (leadership triad ambient) | 1 | 2 | 3 |
| OE 10 — conversations_history (C002 ambient at-risk closings) | 1 | 2 | 3 |
| OE 11 — crm_list_engagements (3/20 stream) | 1 | 1 | 2 |
| OE 12 — crm_get_engagement × ~5 (4/07 portal breach detail) | 2 | 5 | 6 |
| OE 13 — crm_get_engagement × ~5 (Raj-access-audit detail) | 2 | 5 | 6 |
| OE 14 — crm_get_engagement × ~5 (Marcus 4/14 post-term detail) | 2 | 5 | 6 |
| OE 17 — mortgage_los_get_pipeline / search_loans (at-risk closings) | 1 | 2 | 3 |
| Cross-service triangulation buffer (contact re-resolve for Grace/Denise MPIM, loan lookups) | 2 | 3 | 5 |
| OE 18 — send_email (Sloane reconciled outreach) | 1 | 1 | 1 |
| OE 19 — conversations_add_message (D_grace_robert_denise MPIM status) | 1 | 1 | 1 |
| OE 20 — crm_create_engagement (NOTE on incident record) | 1 | 1 | 1 |
| OE 21 — filesystem_write_file (+ optional filesystem_create_directory) | 1 | 2 | 2 |
| **TOTAL** | **30** | **52** | **68** |

- **Low projection:** 30 (skeleton compliance — batched CRM pull, minimal query variants, no detail get_engagement calls)
- **Midpoint projection:** 52 (typical competent agent)
- **High projection:** 68 (thorough agent verifying each detail engagement)

**Verdict: PASS (midpoint 52 ≥ 50).**

Cross-check against Hardness_Plan midpoint 52 → exact match. No underprojection gap. Low end 30 falls under the 40 THIN floor which is a mild pessimistic-corner risk (skeleton compliance could dip to THIN_DENSITY) but a competent agent walking L8/L10 correctly will hit ≥ 40 via CRM stream detailing alone (4 workstreams × 4-6 engagements each).

---

## B4 Lever preservation

Each of the 5 selected Hardness levers is checked for OE exercise.

- **L8 (Multi-link chain across email, Slack, CRM) :: PASS** — email chain in OE 2/3/4/5, Slack chain in OE 7/8/9/10, CRM chain in OE 11/12/13/14; OE 15 forces cross-service reconciliation. Three structurally distinct systems each carry a decision-relevant piece. Lever fully exercised.

- **L9 (Latching / authority dismissal — Raj's restore-cost read) :: PASS** — OE 8 pins Raj's later ts 1774447787 readout ("best case restore is from cloud snapshot from tues pm... prob significant data re-entry... can't promise LOS integrity till tested") as the load-bearing evidence that walks the Friday-evening picture back. OE 16 explicitly requires the agent to conclude "restore is a lift but is not foreclosed" and enumerate 72-hour gap / rebuild / validation / integrity caveat as tradeoffs. OE 23 verifies the read-differences from the March framing. Latching lever surfaced and countered.

- **L10 (Structured-DB skip on CRM engagements) :: PASS** — CRM surface exercised on FOUR separate streams: OE 11 (3/20 ransomware), OE 12 (4/07 portal breach — the true supersession per S1 propagate flag), OE 13 (Raj-access-audit), OE 14 (Marcus Webb 4/14). Agent must query the structured-DB non-conversational surface to reconcile borrower-notice scope. Lever hits the load-bearing atoms.

- **L25 (Existing-output anchor / supersession — Denise's 3/20 preliminary plan) :: PASS** — OE 4 anchors Denise's 3/20 preliminary trio; OE 15 forces reconciliation showing the plan has been superseded / evolved across the 4/07 portal breach (4 files), the Raj-access-audit stream, and the 4/14 Marcus Webb post-term access (3 files). OE 23 explicitly requires the agent to state "March borrower-notice framing is materially larger than Denise's 3/20 preliminary plan". Supersession lever cleanly exercised.

- **L26 (Decoy parent thread — C001 canonical vs C002/C008 decoys) :: PASS** — OE 7 explicitly labels C008 the "IT-support origin thread, a topically plausible decoy" and C002 "the tactical loan-processing decoy that the write must not target", pinning C001 as "Robert's canonical exec anchor". OE 19 write action pins `channel_id = D_grace_robert_denise` (MPIM), and OE 25 verifies the tight-distribution posture across all four writes (mpim / crm NOTE / filesystem incident folder / Sloane-only email). Decoy parent addressed and tight-distribution guard installed — resolves the S1 propagate flag #2.

**All 5 levers exercised. No lever weakened by OE construction.**

---

## B8 Forward map (prompt → OE)

| Prompt sentence / ask | OE(s) covering |
|---|---|
| "Denise pinged me... put a stake in the ground this week" | Context (no OE required) |
| "the pay versus restore call" | OE 2, 3, 8, 16, 21§a, 22§a |
| "where we actually land on borrower notice" | OE 4, 9, 11–15, 21§b, 22§b |
| "walk Raj's picture back to what emails and records actually say, not my memory of a Friday-evening call" | OE 2, 8, 16 |
| "restore is still a lift... specific gaps and rebuild items as tradeoffs, not a foregone conclusion" | OE 16, 22§a, 23(i) |
| "confirm nothing has shifted on the legal side since we asked outside cyber counsel for the sanctions and privilege read" | OE 3, 5, 16 |
| "plain read of Denise's preliminary borrower-notice plan" | OE 4 |
| "Has scope narrowed" | OE 15 |
| "Are there specific files anyone has identified since" | OE 12, 14, 15 |
| "Anything queued I have not been looped on" | OE 13, 15 |
| "Do not take the March framing at face value" | OE 15, 23 |
| "Anything feeding the same borrower notice counts, even from a separate workstream" | OE 12, 13, 14, 15 |
| "Find the freshest signals on the incident and reconcile them, wherever they live" | OE 8, 15 |
| "decision brief with the tradeoffs on the payment call, current borrower-notice posture with any specific files, anything counsel still needs before I decide" | OE 21, 22 |
| "Email outside cyber counsel with the reconciled picture and a request for their view on whatever is still open" | OE 1, 18, 26 |
| "Post a short status in the leadership channel so we are all reading the same room without pushing it wider than needed" | OE 6, 19, 25 |
| "Put a formal note on the incident record in our engagement log so the paper trail is clean" | OE 20 |
| "drop the memo itself in the incident folder alongside the counsel correspondence" | OE 21 |
| "If your read differs from the picture I have been operating on, say so plainly" | OE 23 |

**Uncovered prompt asks: none.** Every substantive Robert ask maps to ≥ 1 OE step. Verification OEs 22/24/25/26/27 install cross-artifact guardrails that lock the writes to the reconciled facts.

---

## B9 Reverse map (OE → prompt)

| OE# | Primary prompt sentence addressed |
|---|---|
| OE 1 | "Email outside cyber counsel" (contact resolution for Sloane; Bennett-* near-miss guard) |
| OE 2 | "walk Raj's picture back to what emails and records actually say" |
| OE 3 | "confirm nothing has shifted on the legal side since we asked outside cyber counsel" |
| OE 4 | "plain read of Denise's preliminary borrower-notice plan" |
| OE 5 | "confirm nothing has shifted on the legal side since we asked outside cyber counsel" |
| OE 6 | "Post a short status in the leadership channel... not wider than needed" (channel discovery) |
| OE 7 | "walk Raj's picture back" + establishes C001 canonical vs C002/C008 decoy structure for OE 19 write target |
| OE 8 | "walk Raj's picture back... not my memory of a Friday-evening call" + "Find the freshest signals" |
| OE 9 | "leadership channel... not wider than needed" (ambient signals in leadership triad) |
| OE 10 | "Do not take the March framing at face value" (ambient at-risk-closings context; explicitly flagged as color not driver) |
| OE 11 | "Denise queued a preliminary plan" + "March framing" |
| OE 12 | "Anything feeding the same borrower notice counts, even from a separate workstream" + "specific files identified since" |
| OE 13 | "Anything queued I have not been looped on" + "separate workstream" |
| OE 14 | "separate workstream" + "specific files identified since" |
| OE 15 | "reconcile them, wherever they live" + "Has scope narrowed" + "Anything feeding the same borrower notice counts" |
| OE 16 | "tradeoffs on the payment call" + "restore is still a lift... not a foregone conclusion" |
| OE 17 | Ambient — supports "Monday operations at risk" context but not a decision anchor; **see scope-creep note below** |
| OE 18 | "Email outside cyber counsel with the reconciled picture" |
| OE 19 | "Post a short status in the leadership channel... not wider than needed" |
| OE 20 | "Put a formal note on the incident record in our engagement log" |
| OE 21 | "drop the memo itself in the incident folder" + "decision brief with the tradeoffs on the payment call, current borrower-notice posture with any specific files, anything counsel still needs" |
| OE 22 | "decision brief with the tradeoffs... current borrower-notice posture with any specific files... anything counsel still needs" (three-section order verification) |
| OE 23 | "If your read differs from the picture I have been operating on, say so plainly" + "Do not take the March framing at face value" |
| OE 24 | Implicit guardrail — prompt does NOT ask for ledger writes |
| OE 25 | "not wider than needed" (tight-distribution posture verification across 4 writes) |
| OE 26 | Derived from "the reconciled picture" flowing consistently through the 4 write artifacts |
| OE 27 | Density / breadth surface verification (no direct prompt anchor; QC guardrail) |

**Scope-creep candidates:**

- **OE 17 — WEAK scope creep.** The prompt does not name Monday closings, LN-2026-00601, or the pipeline at-risk read as a decision anchor. OE 17 exists as ambient L26 decoy exercise + color for "Monday operations at risk" flavor. OE body correctly labels it "color for the timing pressure but should not treat ops triage as the decision anchor". This is defensible as decoy-lever exercise but if the S3 rubric author writes a rubric that FAILs an agent for not calling `mortgage_los_get_pipeline`, that would be scope creep. Recommend the rubric author treat OE 17 as SOFT-OUTCOME (agent may or may not query LOS pipeline; not scored as required behavior).
- **OE 10 — MINOR.** Similar concern: C002 conversation history is ambient decoy context, not a load-bearing atom. OE body correctly labels it "color rather than as the driver". Same rubric-author caution as OE 17.

No hard scope creep. No OE step duplicates another without added angle (each CRM stream OE 11/12/13/14 addresses a structurally distinct workstream; email OE 2/3/4/5 address distinct actors and pull types).

---

## QC sub-dim scoring

Per `Docs_keystone/7_QC_Spec_Doc1.json` Oracle Event dimension and `Reference/Council_Protocol.md` 1/3/5 mapping.

- **OE Completeness :: 5** — Every substantive prompt ask maps to ≥ 1 OE step. Verification OEs 22/24/25/26 install cross-artifact consistency guards. Robert's "If your read differs from the picture I have been operating on, say so plainly" is covered by OE 23. No prompt sub-clause lacks OE coverage. The 4 write actions (email, Slack, CRM NOTE, filesystem memo) each map cleanly and the tight-distribution posture ("not wider than needed") is enforced by OE 25. No NON-FAIL band justification invoked.

- **OE Accuracy :: 5** — Deep-queried every named atom against Universe_Split:
  - 22/22 CRM engagement IDs verified (4/07 portal-breach file list LN-2026-00522/00008/00010/00009 confirmed on `crm_engagement_d27cd1da0d5a`; Marcus 4/14 file list LN-2025-00002/00007/00229 confirmed on `crm_engagement_985a3efbbee8`, `_a33cc635ceed`, `_1b81acccf98e`)
  - 10/10 Slack timestamps verified with correct channel + user mapping (Robert's canonical anchor `ts 1774032333` on C001; Raj's later readout `ts 1774447787` on C001)
  - 6/6 email IDs verified with correct sender / recipient / subject
  - Sloane reply-absence verified (Sloane never appears as `sender` in the mailbox — OE 5 grounded)
  - Contact routing atom: OE 1 correctly enumerates ALL 5 Bennett-* near-miss variants and pins Megan Sloane at `megan.sloane@wardbarrettlaw.com` as the persona-brief cyber counsel of record. `lbennett@bennettcyberlaw.com` explicitly called out as the semantic near-miss trap. No NON-FAIL band justification invoked.

---

## Verdict

**GO** — S2 Oracle Events passes Council B adversarial QC.

- B3 density: PASS (midpoint 52 = Hardness Plan target)
- B4 lever preservation: 5/5 PASS
- B8 forward map: complete, no uncovered prompt asks
- B9 reverse map: complete, 2 WEAK scope-creep flags (OE 10, OE 17 as ambient color / L26 decoy exercise — non-blocking; propagate to S3 rubric author as SOFT-OUTCOME guidance)
- QC sub-dims: OE Completeness 5/5, OE Accuracy 5/5

**Propagate flags to S3 rubric author:**

1. **OE 17 + OE 10 SOFT-OUTCOME.** At-risk-closing LOS pipeline read and C002 ambient history are L26 decoy exercise; do not FAIL an agent that skips them provided the decision brief still lands the ransomware disposition correctly.
2. **Supersession anchor is the 4/07 portal-breach stream** (per S1 verification propagate flag #1). OE 12 correctly pins this; OE 14 (Marcus 4/14) is the *fourth* separate workstream, not the supersession. Rubric author should score reconciliation evidence on the 4/07 stream (4 files) as the primary supersession atom.
3. **Tight-distribution write posture is a hard requirement.** OE 19 pins `D_grace_robert_denise` MPIM; OE 25 enforces the four-write channel constraint. Rubric author must score the Slack write channel against MPIM (not C001 general, not C002, not C008) and the counsel email recipient against `megan.sloane@wardbarrettlaw.com` only.
4. **Sloane reply-absence is a truthful universe state** (verified in this session). Rubric author should NOT expect the agent to find a Sloane response; OE 5 correctly frames this as an open item to route back.

No BLOCK issues. S2 exit is clean.
