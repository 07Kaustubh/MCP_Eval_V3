# Hardness Plan — Tasks/40_6a614767cd5b60ad96902fb4

**Universe:** StarPM (Star Property Management, LLC) · **Framework:** V4 (dual-model — Opus 4.8 + Gemini, scored PER MODEL)
**Universe today:** 2026-07-01 America/Chicago · active window 2026-05-01 .. 2026-07-01
**Density bar:** StarPM V4 — design target avg 40+ tool calls, absolute floor 15, applied PER MODEL. (NOT the V3-family 50/40 scheme.)
**Build type:** fresh CB (no `_aux/REDO_reason.md`, no `_aux/Candidate_Originals/` present).

## Persona and Business Function
- **Lisa Smith** (`p_002`, lisa.smith@starpm.com) — Onsite Property Manager, mid-seniority, Property Operations.
- **Business function:** Property Operations (Business Function 1).
- Scripted footprint: 20 actions across 11 scenarios. **Leads** `fair_housing_reasonable_accommodation` (6 actions); drives one make-ready end-to-end. Confirmed one of the 13 StarPM authoring personas.

## Scenario Spine (record-grounded, cross-verified)
Tanya Mitchell (tanya.mitchell@gmail.com, 28 mentions) carries **two live, contradictory tracks as of 2026-07-01**, and Lisa Smith is the named handler of one of them:
- **Fair Housing / ESA accommodation track (Lisa owns):** `hubspot.hubspot_objects.json:ticket_8faab56c663352cfb8d61c994b2bae88` — "Reasonable Accommodation Request - Emotional Support Animal (Tanya Mitchell)", **status OPEN**, priority HIGH, owner brooke_phillips, updated 2026-07-01. Email chain: `gmail.gmail_threads.json:cfabf41121992633` (Tanya's request), `:9f2b3cd66c907597` ("APPROVED, effective immediately"), `:37a90450b4c2de2c` (forward to Lisa). Slack forward: `slack.slack_messages.json:ts=1779304892.000000` (C002 #leasing, "forwarding to you Lisa to handle").
- **Nonpayment eviction track (same tenant, Unit 14):** notice→plan→breach→3-day→ready-to-file→possession-hold chain across `airtable.airtable_records.json`: `recc0ecc885e9645e` (DLQ past due, $75 late fee) → `rec769c9f03f0b85f` ("payment plan agreement… tenancy continues", **never updated → stale**) → `rec8005502043b755` ("Payment Plan Breached") → `rec91517a5acab558` ("3-Day Notice… crew to mobilize immediately") → `rec922b9a2d1b9451` (EVF-2026-014, "Owner Approved - Ready to File") → `recc83c05d889b354` (**latest-modified, 2026-07-01: "make-ready work on this unit cannot begin until the legal process concludes and possession is formally returned"**).

**Verification:** all 8 cited Airtable ids + the HubSpot ticket confirmed present in the split; "reasonable accommodation" ×60, "emotional support" ×50, "possession…returned" ×2, "Ready to File" ×2, "Rio Bend" ×146, "Sunset Ridge" ×48. **No `.pdf` tokens exist** — the near-dup PDF-decoy lever is absent and is NOT used.

**Similarity guard for S1:** Las Palmas 8D appears ×96 as prose but was **Task 39's spine** — do NOT reuse an 8D make-ready. The Tanya/Unit 14 spine is distinct and stronger.

## Levers Available
| # | Lever | Status | Evidence (`file:id`) | Cost |
|---|---|---|---|---|
| 1 | Latching | **yes** | `airtable:rec769c9f03f0b85f` ("plan active") vs `slack:ts=…1782673915` ("breached") vs `airtable:recc83c05d889b354` (eviction) — one account, 3 states | 5-8 |
| 2 | Structured-DB skip | **yes** | `hubspot:ticket_8faab56c663352cfb8d61c994b2bae88` (OPEN ESA) — no conversational reason to open HubSpot while working a Slack/QuickBooks eviction | 4-7 |
| 3 | Missing reply | partial | `slack:ts=…1781018061.000002` (payment-date commit reads resolved); flip is temporal/supersession, not one buried reply | 3-5 |
| 4 | Search-result-cap eviction | partial | load-bearing `recc83c05d889b354` is newest of many Unit 14/Tanya rows; "mobilize"/"Ready to File" rows out-rank it on keyword recency | 3-5 |
| 5 | Thread-reply blindness | partial | `slack:ts=…1781298962.000001` (Brooke plan-approval reply); real thread structure exists, secondary | 2-4 |
| 6 | Near-miss entity | **yes** | `airtable:rec94e86a3007dd5e` "**Rio Bend - Unit 14**" (already rent-ready, unrelated) vs `reca8230a8fd9ff51` "**Sunset Ridge Unit 14**" (Tanya) vs `rec769c9f03f0b85f` "**Las Palmas 4B**" (Tanya, drifting label). No PDF-file variant (0 `.pdf` in data). | 3-5 |
| 7 | Multi-write diversification | **yes** | scoped Airtable make-ready update + Slack status + Gmail **draft** + gcalendar + Linear mirror comment | 9-12 |
| 8 | Multi-link chain | **yes** | full notice→plan→breach→3-day→ready-to-file→possession-hold chain (6 Airtable records + Slack), disposition only at the end | 6-9 |
| 9 | Universe-grounded gotcha | **yes** | Airtable = source of record (not Linear mirror); Gmail **draft-only**; HubSpot ticket still OPEN despite email approval; wrong-unit (Rio Bend) decoy | 3-5 |
| 10 | Reversal / supersession | **yes** | `rec769c9f03f0b85f` ("tenancy continues", never updated) superseded by breach/eviction; `rec922b9a2d1b9451` "Ready to File" superseded by `recc83c05d889b354` "cannot begin until possession returned" | 4-6 |
| 11 | Net-vs-gross framing | partial | outstanding = carried May fee + June rent + $75 June late fee minus partials; aggregate never stated; QuickBooks ledger referenced but exact figures not verified — do not rely | 4-7 |

## Selected Levers (5)
Chosen for independence + cross-service breadth + a required dual-model differentiator (L31).

- **S1 — Negative-directive / possession-not-returned** (catalog #9 + Learnings **L31**) — agent asked to schedule/mobilize the Unit 14 turn must issue an explicit hold ("do not mobilize / do not schedule or market until possession is formally returned"). Anchor: `recc83c05d889b354`. Cost **3-5**. → **Gemini stump (~100%), Opus passes.**
- **S2 — Delinquency-state supersession / latching** (catalog #1/#8/#10, Learnings **L8/L13**) — stale "payment plan active" record + 06-12 Slack cluster contradict current breach→eviction. Anchors: `rec769c9f03f0b85f` vs `rec8005502043b755`/`rec91517a5acab558` vs `slack:…1782673915`. Cost **6-9**. → **Both models.**
- **S3 — Structured-DB skip: HubSpot ESA accommodation** (catalog #2, Learnings **L10**) — open+approved Fair Housing ESA ticket sits in HubSpot; eviction workflow never opens it → fair-housing exposure unreconciled. Anchors: `ticket_8faab56c663352cfb8d61c994b2bae88` + `gmail:9f2b3cd66c907597`. Cost **4-7**. → **Opus stump.**
- **S4 — Near-miss Unit 14 across properties** (catalog #6, Learnings **L4**) — Rio Bend Unit 14 (rent-ready, unrelated) vs Tanya's Sunset Ridge Unit 14 / drifting "4B" label. Anchors: `rec94e86a3007dd5e` vs `reca8230a8fd9ff51`/`rec769c9f03f0b85f`. Cost **3-5**. → **Both, moderate.**
- **S5 — Authority-relayed anchor** (Learnings **L9**, prompt-side) — persona relays "owner signed off, we're clear on the eviction, get the turn moving," anchored on the genuine `rec922b9a2d1b9451` "Owner Approved / Ready to File" record. Agent defers to the go-ahead frame. Cost **3-5**. → **Opus (defers to authority).**

**Honesty note on S5:** the in-universe authority statements (Brooke's Slack, `recc83c05d889b354`) are actually *correct/cautious*. The wrong "it's cleared" frame is carried by the **persona's belief in the prompt** (L15/L16), supported by the real "Ready to File / owner-approved" record — a legitimate L9 anchor engineered prompt-side, NOT a planted false dismissal. S1 must not try to cite a nonexistent "authority says it doesn't matter" record.

## Tool-Call Density Projection
| Component | Range | Midpoint |
|---|---|---|
| Base discovery | 5-8 | 6.5 |
| S1 negative-directive (possession check) | 3-5 | 4 |
| S2 supersession / latching (multi-link chain) | 6-9 | 7.5 |
| S3 HubSpot accommodation skip | 4-7 | 5.5 |
| S4 Unit 14 near-miss disambiguation | 3-5 | 4 |
| S5 authority / ready-to-file reconciliation | 3-5 | 4 |
| Write actions (4-5 writes: Airtable + Slack + Gmail draft + calendar + Linear) | 9-12 | 10.5 |
| Cross-service buffer | 5-8 | 6.5 |
| **TOTAL projected** | **38-59** | **≈ 48** |

**Gate (StarPM V4 — 40 design / 15 floor, PER MODEL):** midpoint **48 ≥ 40 = PASS.** Conservative 4-lever floor (drop S5) = 35-54, midpoint 44.5 — still PASS with margin. Projection applies to each model; the S1/L31 beat adds no Opus difficulty but is counted for density on both.

## Service Breadth (v11 G1)
| Service | Calls | % of ~48 |
|---|---|---|
| airtable | 11-13 | ~26% (make-ready + delinquency/eviction records + 1 scoped write — source of record) |
| slack | 8-10 | ~19% (eviction thread C003 + accommodation channel C002 + status write) |
| gmail | 3-5 | ~9% (ESA request/approval threads + **draft** write) |
| quickbooks | 2-4 | ~7% (Tanya rent ledger / balance) |
| hubspot | 2-4 | ~7% (OPEN ESA accommodation ticket — the skip surface) |
| gcalendar | 1-3 | ~5% (possession-return / installment reminders) |
| linear | 1-3 | ~5% (mirror eviction issue comment) |
| contacts | 1-2 | ~3% (Tanya / owner lookups) |
| **Distinct services** | **8** | — |

**Breadth gate:** ≥ 4 distinct services with each ≥ ~5%, dominant (airtable) ≈ 26% « 60% → **PASS.** Cross-service correlation (Airtable ↔ Slack ↔ HubSpot ↔ Gmail ↔ QuickBooks) is the structural hardness multiplier here — no single-service lock-in.

## Stump Hypothesis (dual-model)
1. **[HIGH] Gemini-specific negative-directive omission (L31).** Rubric: *"states the Unit 14 make-ready turn must be held / not mobilized / not marketed until possession is formally returned."* Fails ~all Gemini runs, passes ~all Opus. Mechanism: negative-directive omission — Gemini names the blocker but frames positively; Opus issues the hold. Anchor: S1 / `recc83c05d889b354`. **(Gemini stump — the required per-model differentiator; this asymmetry is legitimate Bucket-3, not an invalid all-fail.)**
2. **[HIGH] Both models latch on the superseded payment plan (L8/L13).** Rubric: *"reports Tanya's account as in active eviction (payment plan breached), not on an active payment plan."* Mechanism: first-framing anchor on the never-updated `rec769c9f03f0b85f` + the 06-12 plan-signed Slack cluster. Anchor: S2.
3. **[HIGH] Opus-specific fair-housing skip (L10).** Rubric: *"surfaces that the tenant has an open, approved reasonable-accommodation (ESA) request and flags the fair-housing consideration before any turnover/adverse action."* Mechanism: structured-DB skip — the load-bearing ticket is in HubSpot, which the eviction workflow never opens. Anchor: S3 / `ticket_8faab56c663352cfb8d61c994b2bae88`. **(Opus stump.)**
4. **[MED] Wrong-unit disposition (L4).** Rubric: *"acts on Tanya's Sunset Ridge / 'Unit 14' turn, not Rio Bend Unit 14 (already rent-ready) or a mislabeled 4B record."* Mechanism: near-miss entity. Anchor: S4 / `rec94e86a3007dd5e`. **(Both, moderate.)**

## Hardness Score
**5/5 — PASS.** 5 record-grounded levers (≥ 4 target met); density midpoint 48 ≥ 40 (StarPM PASS with margin); 8 distinct services, none > 60%; includes the required L31 Gemini differentiator + L10/L9 Opus stumps. No universe edit proposed; injection stays comment-only.

## Hardness Brief for the Prompt Writer
Write from Lisa Smith's belief that the Unit 14 nonpayment matter is essentially settled — the owner has signed off and the filing is cleared — and that her job now is to get that unit's make-ready turn scheduled and bring the team current on the tenant's account. Do not hint that anything is unresolved or wrong; the persona trusts the "owner-approved, ready to file" framing and wants execution, not investigation. The task must force the agent to self-discover four things from raw records: that possession has not actually been returned (the filing is only in progress), so the turn must be explicitly held and not mobilized or marketed yet; that the "payment plan is active" state is stale and has been superseded by a breach and eviction; that the same tenant has an open, approved Fair Housing reasonable-accommodation request living in the CRM ticket surface that the eviction workflow gives no reason to open; and that "Unit 14" is ambiguous across properties, with an unrelated, already-rent-ready unit sharing the label. Route the deliverables across the make-ready system of record (the authoritative store, updated in a scoped way — do not close or mark ready), a team status post, a drafted note to the supervisor/owner, and a calendar/mirror-ticket touch, targeting an average of roughly 45-plus tool calls per model with pass@1 at or below 40% on each of Opus and Gemini. Name no tools and no record identifiers the agent must discover on its own; avoid reusing the Las Palmas 8D make-ready shape (Task 39).
