# Council B — Adversarial QC + Density + Hardness Preservation
## Phase: PROMPT · Universe: StarPM (V4, dual-model) · Task 40_6a614767cd5b60ad96902fb4

Deliverable: `5_Prompt.txt` (312 words, 0 em/en dashes, 0 tool/ID tokens — validator-confirmed and re-confirmed semantically).
Universe today: **2026-07-01 America/Chicago** (today_horizon.json; validator's "Jun 12" is the null-fallback cosmetic and is ignored).
Method: read-only. Every load-bearing universe claim in `Hardness_Plan.md` was INDEPENDENTLY re-verified against `_aux/Universe_Split/` (the plan is under scrutiny, not trusted). Verdict is the UNION of five lenses.

---

## Ground-truth verification receipts (Ground-truth + Integration lenses)

All extracted from `airtable.airtable_records.json` (row_data JSON), `hubspot.hubspot_objects.json`, `linear.linear_issues.json`, `slack.slack_channels.json`, `quickbooks.quickbooks_entities.json`:

- **HOLD anchor `recc83c05d889b354`** (tblMakeReady, fldUnit "Unit 14"): MODIFIED **2026-07-01 11:18:57** = NEWEST of all Unit-14 make-ready rows. fldTurnStatus `selSched`. fldNotes2: "Eviction petition for Tanya Mitchell is currently being coordinated with the Justice of the Peace - make-ready work on this unit **cannot begin until the legal process concludes and possession is formally returned**. Turn scheduling is tentative and contingent on the court outcome." → S1 anchor CONFIRMED and load-bearing; it is the newest row, so a recency-ranked read lands on it only if the agent sorts correctly.
- **Stale plan `rec769c9f03f0b85f`** (tblMakeReady, fldUnit **"Las Palmas 4B"** — the drifting label): MODIFIED 2026-06-12, never updated. "…active repayment schedule… tenancy continues…" → S2 stale-superseded anchor CONFIRMED.
- **Breach `rec8005502043b755`** (06-21, "Payment Plan Breached - No Response") + **3-day `rec91517a5acab558`** (06-28, Unit 14, "crew to mobilize immediately… Brooke Phillips has approved escalation") → supersession chain CONFIRMED.
- **Authority anchor `rec922b9a2d1b9451`** (tblMaintenanceTickets, EVF-2026-014, 06-30): "Owner authorization received from Linda Castillo… status advanced to **Owner Approved - Ready to File**. Filing package is staged and cleared for submission." → S5 anchor CONFIRMED; "Ready to File" = filing NOT done, superseded by the 07-01 possession-hold row.
- **Near-miss `rec94e86a3007dd5e`**: fldUnit "**Rio Bend - Unit 14**", `selReady`, unrelated ("back to rent-ready… Ticket closed"). Tanya's unit = **`reca8230a8fd9ff51` "Sunset Ridge Unit 14"**. Additional live decoy found: HubSpot `ticket_21992e14…`/`ticket_32de56bc…` "Renewal Paperwork Processing - **Tommy Reyes, Unit 14**" → a THIRD "Unit 14" context. S4 near-miss CONFIRMED and stronger than documented; tenant anchor ("Tanya Mitchell") is the disambiguator.
- **S3 ESA `ticket_8faab56c663352cfb8d61c994b2bae88`** (hubspot_objects): subject "Reasonable Accommodation Request - Emotional Support Animal (Tanya Mitchell)", **status OPEN**, priority HIGH, owner owner_brooke_phillips. CONFIRMED. NOTE (see Moderate-2): two sibling ESA rows exist — `ticket_b9ad3068…` status NEW, and `ticket_34cb6ee6…` status **CLOSED** ("Closing this ticket. The interactive process has been completed in full…").
- **Make-ready channel**: `slack.slack_channels.json` → exactly one **C004 #make-ready**. "post a clean status in the make-ready channel" resolves uniquely.
- **"the ticket we have open on it"**: `linear.linear_issues.json` → THREE open Mitchell-eviction issues: **OPS-32** "Eviction Hearing - Mitchell, Harris Property" (In Progress), **OPS-38** "Compile lease-violation docs for Mitchell eviction hearing" (Todo), **OPS-54** "Mitchell eviction hearing prep - checklist complete, status advancing" (In Progress). Target is NOT singleton (see Moderate-1).
- **Account surface**: Tanya has QB entities (customer + invoices + credit_memos + estimates + bills) → cross-service account corroboration exists. Brooke Phillips (brooke.phillips@starpm.com) is the sole "Brooke".

Plan's universe claims check out; no fabricated anchors.

---

## [B1] QC sub-dimension scoring (all 12 applicable Prompt sub-dims; bar = 5)

SUB-DIM Unique Ground Truth -> SCORE 5/5 -> REASON Core end-states are unique: HOLD the turn (newest row `recc83c…` says possession not returned; status stays selSched), report account as active-eviction/breached, cover ESA fair-housing, act on Tanya's Sunset Ridge Unit 14; the explicit constraint "move it forward only as far as the facts support / do not mark it further along than it really is" (line 3) kills the persona's advance-the-turn reading, so no file-now-vs-defer fork survives.
SUB-DIM Feasibility -> SCORE 5/5 -> REASON All five asks are executable and non-conflicting; Gmail is draft-only and the prompt asks "draft… Do not send it" (perfect capability match); holding the turn while still doing the four other asks is fully achievable.
SUB-DIM Explicit Tool Mention -> SCORE 5/5 -> REASON No MCP tool/param/server names and no "use the X tool"; "make-ready record/channel", "Google Calendar", "email", "ticket" are natural business/product surfaces, which the spec permits.
SUB-DIM Prompt Clarity and Specificity -> SCORE 5/5 -> REASON Each ask's intended action is unambiguous; the only soft referent, "the ticket we have open on it," is the spec's own non-failing minor-referent kind ("the partner" example) that does not change the action taken (bring the open Mitchell-eviction tracker current) — carried to OE/rubric as Moderate-1.
SUB-DIM Contrived / Unnatural -> SCORE 5/5 -> REASON Reads as a natural, slightly rambling onsite-PM delegation; the enumerated asks are GOALS/deliverables ("get the team current", "draft an email"), not a tool-invocation command list ("first search emails, then check QuickBooks"), so not contrived.
SUB-DIM Truthfulness -> SCORE 5/5 -> REASON No tight-identifier errors; "owner signed off" is true (`rec922…` Linda Castillo authorization) and "my read is that the nonpayment side is cleared" is an explicitly-hedged persona belief (the designed authority-anchor trap), not a false factual assertion.
SUB-DIM Tool use and Cross-service -> SCORE 5/5 -> REASON Requires reconciliation across airtable + slack + gmail + gcalendar + linear + hubspot + quickbooks + contacts (8 services); facts are scattered and must be cross-checked, far beyond a single service.
SUB-DIM Investigation -> SCORE 5/5 -> REASON Root cause is hidden; the prompt asserts the WRONG belief (cleared/ready) and forces self-discovery of the hold, the supersession, the ESA, and the unit disambiguation, then acts (>=1 write).
SUB-DIM Coherence -> SCORE 5/5 -> REASON One situation (Tanya's Unit 14 turn+account); every ask (make-ready, team status, owner-review email, reminder, ticket) ties to the same matter; no unrelated bolt-on.
SUB-DIM Persona -> SCORE 5/5 -> REASON Lisa Smith, Onsite Property Manager (Property Operations), leading a unit turn / account status / owner-review prep is squarely her voice and remit.
SUB-DIM Business Function -> SCORE 5/5 -> REASON Clearly Property Operations (make-ready turn, unit status, team coordination), the assigned function.
SUB-DIM Alignment with Today's Date -> SCORE 5/5 -> REASON "today"/"this week" resolve to the 2026-07-01 window where the load-bearing `recc83c…` row lives; "early next week" (Jul 6-7) is a legitimate future reminder; the whole May-July chain is coherent with 07-01.

Result: **12/12 sub-dims = 5.** No sub-dim requires a middle-band rescue.

---

## [B2] Adversarial alt-path / second reading

- (a) "schedule / mark the turn ready" as end-state? **NOT defensible.** Line 3 explicitly forbids marking it further along than reality and bounds movement to "as far as the facts support"; the newest row says work cannot begin until possession returns and there is no "hold/blocked" status in the schema (only selProg/selSched/selReady), so the correct end-state is deterministic: stays selSched + hold documented. UGT holds. This is the intended stump (advance-vs-hold pull), resolved by the in-prompt constraint — distinct from the canonical "file the package" UGT fail (which had no bounding constraint).
- (b) act on the WRONG Unit 14? Possible as a MODEL FAILURE (Rio Bend Unit 14 rent-ready; Tommy Reyes Unit 14 renewal), but the prompt supplies the disambiguator ("Tanya Mitchell's Unit 14", "Keep everything tied to Tanya Mitchell's unit specifically"). Not a prompt ambiguity.
- (c) "draft a note to Brooke, do not send it" — unambiguous: sole "Brooke" (Brooke Phillips), Gmail is draft-only so "do not send" matches capability. No divergence.
- **DIVERGENCE FOUND (Moderate-1):** "update **the ticket** we have open on it" maps to 3 open Mitchell-eviction Linear issues (OPS-32 In Progress, OPS-38 Todo, OPS-54 In Progress). A second reasonable reading updates a different OPS issue. Substance converges (bring the Mitchell/Unit-14 eviction tracker current with possession-hold + eviction state), and the spec treats "the ticket" as non-failing minor referent, so this is NOT a prompt-phase block — but it is a real write-target multiplicity that MUST be quarantined downstream. Fix below.

---

## [B3] Tool-call density projection (PER MODEL, StarPM 40+ scale)

Trajectory sketch (competent agent): contacts (Tanya/Brooke/owner) 1-2; Airtable make-ready search + Rio-Bend/Sunset-Ridge disambiguation + read newest hold row 5-7; Airtable maintenance tickets (DLQ/EVF) 2-3; Slack #make-ready/#general account cluster 3-5; QuickBooks Tanya ledger 2-4; HubSpot ESA discovery (the skip) 2-4; Gmail ESA approval + Tanya threads 2-4; Linear open eviction tickets 2-3; then 5 writes (scoped Airtable hold-annotate, Slack status, Gmail draft, GCalendar reminder, Linear update) 5-6; verification/disambiguation loops 4-8.

- **Opus 4.8 projected midpoint ≈ 44** (range ~38-50). Clears **40**. PASS. Margin is moderate, not huge; the 8-service scatter + triple-decoy disambiguation (3x Unit 14, 3x ESA ticket, 3x Linear ticket) structurally forces the reads, so a competent reconciliation cannot land under ~38.
- **Gemini projected midpoint ≈ 46** (range ~40-52). Gemini's more iterative tool use keeps it at/above Opus; the S1 stump costs it the RUBRIC, not tool calls. Clears **40**. PASS.
- Plan projected ~48 (4-lever floor 44.5); my independent estimate (44/46) is slightly under the plan's but still clears 40 both models. Absolute floor 15 comfortably exceeded. **B3 = PASS both models.**

---

## [B4] Hardness preservation (all 5 levers + both dual-model differentiators)

- **S1 possession-not-returned / negative-directive (Gemini stump)** — SURFACES. "turned around… this week" + "get that unit back in shape and ready to re-rent" vs "confirm where it genuinely stands… move it forward only as far as the facts support" drives the agent onto `recc83c…`; the rubric-critical explicit HOLD ("do not mobilize/market until possession returned") is exactly what Gemini omits (names blocker, frames positively) and Opus issues. **Gemini differentiator PRESERVED.**
- **S2 delinquency supersession / latching (both)** — SURFACES. "where her account really landed" + "hearing bits and pieces for weeks" pulls the stale `rec769…` "plan active" against `rec8005…`/`rec91517…`/`recc83c…`. PRESERVED.
- **S3 HubSpot ESA structured-DB skip (Opus stump)** — SURFACES. Nothing in the prompt points to the CRM; the eviction workflow (Airtable/Slack/QB/Linear) never opens HubSpot, so surfacing the approved ESA fair-housing item requires the unprompted CRM check. **Opus differentiator PRESERVED** (see Moderate-2 caveat on ticket-state phrasing).
- **S4 near-miss Unit 14 (both, moderate)** — SURFACES, stronger than documented (Rio Bend + Tommy Reyes both share "Unit 14"). Tenant anchor disambiguates. PRESERVED.
- **S5 authority-relayed anchor (Opus defers)** — SURFACES prompt-side ("owner signed off… filing is squared away… past the holdup"), grounded on genuine `rec922…`. PRESERVED.

No HARDNESS_REGRESSION.

---

## [Implementer re-confirm]
Tool/MCP/param leaks: NONE. Internal IDs (rec…/ticket_…/OPS-…/EVF/DLQ): NONE. Pre-solving: NONE (prompt asserts the wrong belief; root cause fully hidden). Em/en dashes: NONE. Word count: 312 (<=500). All PASS.

---

## Issues (with perspective, quote+location, fix)

- **MAJOR:** none.
- **Moderate-1 [B2 / Integration] — Linear write-target multiplicity.** Prompt quote (line 9): "update the ticket we have open on it so it is not sitting there stale." Universe: `linear.linear_issues.json` OPS-32 (In Progress) / OPS-38 (Todo) / OPS-54 (In Progress), all open Mitchell-eviction issues. Not a prompt block (action converges; spec-sanctioned minor referent). **Required downstream fix (binding on S2/S3):** OE must name the single load-bearing eviction-tracking issue (the "status advancing" tracker, OPS-54, is the natural stale one to bring current) AND the Linear rubric must be goal-phrased ("the Agent updates the open Linear issue tracking Tanya Mitchell's Unit 14 eviction to reflect current status/hold"), NOT locked to one OPS id — otherwise a valid agent updating a sibling issue is unfairly failed (Rubrics: channel/object lock-in = Major).
- **Moderate-2 [Ground-truth] — ESA ticket open/closed multiplicity.** Universe: `hubspot.hubspot_objects.json` has OPEN `ticket_8faab…` AND CLOSED `ticket_34cb6ee…` ("interactive process completed in full") for the same Tanya ESA. Does not remove the S3 lever (an APPROVED accommodation is material to any adverse action regardless of ticket state) but a valid agent reading the CLOSED row will call the accommodation "approved/complete," not "open." **Required downstream fix (binding on S2/S3):** phrase the fair-housing rubric around "an approved reasonable-accommodation (ESA) on record and the fair-housing consideration before turnover/adverse action," NOT "an OPEN ESA ticket" — otherwise the rubric disputes a correct reading of the CLOSED completion row.
- **Watch (not blocking) [Architect]:** unit-label drift for Tanya (Las Palmas 4B / Sunset Ridge Unit 14 / bare Unit 14 / "Harris Property" on OPS-32) is intended hardness; OE/rubric must anchor reconciliation on the TENANT, never a property label.

None of the above is a prompt-phase defect. The prompt itself is clear, unique-ground-truthed, cross-service, hardness-complete, leak-free. The two Moderate findings are OE/rubric-phasing risks handed forward as binding instructions.

## Decision
Every applicable QC sub-dim = 5; unique ground truth holds under adversarial second reading; projected density >=40 for both Opus and Gemini; all 5 levers (incl. both dual-model differentiators) triggered; no tool leaks / IDs / pre-solving. → GO, with the two binding downstream fixes recorded.

VERDICT: GO
