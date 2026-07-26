# Hardness Lever Scan — Task 41_6a61a86a3453b3714bdc72ef (StarPM V4, dual-model Opus 4.8 + Gemini)

Persona: **Lisa Smith, Onsite Property Manager** (lisa.smith@starpm.com, p_002). Leads the Tanya Mitchell ESA reasonable-accommodation scenario; participates in the Las Vistas 9D make-ready turn. Universe today = **2026-07-01** (America/Chicago).

Every "yes" below is grounded in a record ID I read directly. Airtable `created_time` is a **batch-load artifact** (many Tanya records stamped `2026-05-01 08:43` while their notes describe late-June events — e.g. `rec3782834f35df50` created `2026-05-01 08:43:02` but says "did not cure before the **June 29** three-day notice deadline"). The authoritative chronology is the **semantic date in each note**, not `created_time`. Freshest-by-real-timestamp Tanya make-ready record is `recc83c05d889b354` (created/mod 2026-07-01).

---

## 0. Lead verification (all four leads + extensions)

### Lead 1 — Accommodation-vs-eviction contradiction — **HOLDS (flagship)**
ESA accommodation (cat) fully approved AND consummated; June rent eviction runs in parallel. The two are legally independent (ESA ≠ rent forgiveness) — the landmine is the *narrative* collision.

**Accommodation chain (Gmail):**
- `faf333212824c009` (thread `cfabf41121992633`) 05-15 — Tanya → Sandra: formal ESA request (cat), no-pet lease.
- `2cfa230354808d4c` + `d0d7909b992c156b` (thread `37a90450b4c2de2c`) 05-19/05-20 — Sandra **forwards to Lisa** (two near-duplicate forwards).
- `18e65a4437759304` (thread `9f2b3cd66c907597`) 05-20 — **Lisa opens formal accommodation file**, requests form + provider letter.
- `60f57619a3bc34ab` 05-23 — Tanya submits form + **Dr. Carol Reyes** therapist letter.
- `33d1b63fbeb2a9c3` 05-23 — **Lisa APPROVES effective immediately**, lease addendum promised.

**Accommodation consummated (HubSpot + Calendar):**
- `ticket_34cb6ee660b659029fe68d82bc4e5dd5` (CLOSED, 05-28): "Brooke Phillips approved the accommodation, Tanya signed the **ESA lease addendum**."
- `engagement_03023bd76561542686cdc4445fb29e05` (note, 05-30): "ESA lease addendum was **signed by all parties**."
- gcalendar `2026-05-26 ESA Lease Addendum Signing`.
- (Earlier stages: `ticket_b9ad3068...` NEW 05-22, `ticket_8faab56c...` OPEN 05-22.)

**Internally contradictory Tanya Airtable records (all verified):**
| Record ID | Table | fldUnit | Status | Semantic state |
|---|---|---|---|---|
| `recc0ecc885e9645e` | tickets | — (DLQ-2026-0601) | — | June rent unpaid past 5-day grace, $75 late fee ("Past Due – Grace Expired") |
| `reca8230a8fd9ff51` | makeready | Sunset Ridge Unit 14 | selSched | Tanya acknowledged late notice, committed to payment timeline |
| `rec46234590708b5c` | tickets | — (MT-2026-0184) | — | Second-month delinquency; tenant requested payment arrangement, Patricia reviewing |
| `rec769c9f03f0b85f` | makeready | **Las Palmas 4B** | selSched | **Active payment plan**, holding turn Scheduled through end of July |
| `rec8005502043b755` | makeready | Delinquency Escalation | selProg | **Payment Plan Breached – No Response** (June 23 installment missed) |
| `rec91517a5acab558` | makeready | Unit 14 | selSched | **3-Day Notice** served June 26, cure deadline June 29 |
| `rec3782834f35df50` | makeready | Eviction Track | selSched | Did **not** cure by June 29, no contact; assembling filing package |
| `receee45491536859` | makeready | Unit 14 – Tanya Mitchell Eviction | selSched | Filing package compiled, **awaiting owner sign-off** |
| `recc83c05d889b354` | makeready | Unit 14 | selSched | **Eviction petition being coordinated with Justice of the Peace** — make-ready cannot begin (created/mod **2026-07-01**, the freshest) |
| `rec922b9a2d1b9451` | tickets | — (EVF-2026-014) | — | **Owner Linda Castillo authorization received → "Owner Approved – Ready to File"** (CompletionDate 06-30) |

**TRUE current state (2026-07-01):** payment plan **breached**; owner (Linda Castillo) **approved** eviction filing (EVF-2026-014, 06-30); petition **being coordinated with JP — NOT yet filed**; Unit 14 make-ready **on hold** pending possession. The "active payment plan" (`rec769c9f03f0b85f`) and "awaiting owner sign-off" (`receee45491536859`) are **superseded** earlier states.

### Lead 2 — Cross-property Unit 14 ambiguity — **HOLDS (strong)**
- **Different, rent-ready Unit 14:** `rec94e86a3007dd5e` = "**Rio Bend – Unit 14**", `selReady`, full carpet replacement by Victor Rios 05-20, "back to rent-ready condition, ticket closed." Genuinely a *different unit at a different property* that IS ready. (`rec390d3c3b1a3b55` "Rio Bend 214" is a third near-miss.)
- **Same-tenant dual designation:** Tanya's own unit is referenced as **"Las Palmas 4B" / "Unit 4B"** on the *payment-plan* track (`rec769c9f03f0b85f`; QB invoice 7214/payment; Gmail "Payment Plan Confirmation, Unit 4B" `cfbebf14ff71b16e`, "Payment Arrangement Proposal, Unit 4B" `6707492228d78dc1`) AND **"Sunset Ridge Unit 14" / "Unit 14" / "Sunridge Apartments" / "1402 Rimrock Drive, Unit 14"** on the *eviction* track (`reca8230a8fd9ff51`; QB bill `146128608253` "Sunridge Apartments"; Gmail `74cc50c7d2ffb7dc` "1402 Rimrock Drive, Unit 14").
- **Two eviction OWNERS:** **Harry Harris** (Linear/May framing) vs **Linda Castillo** (Gmail/Airtable/current). See Lever 1.

### Lead 3 — Three conflicting arrears representations — **HOLDS, with a correction**
- **AR Invoice `283231782926` (DocNumber 7214)** — the "paid" **decoy**: lines $1,125 May arrears + $975 June rent + $187.50 late fees + **$5,885.94 "partial payment plan credit applied"** (padding) = **TotalAmt $8,173.44**, **Balance $0.0**, zeroed by **payment `952690463873`** ($8,173.44, LinkedTxn→7214, UnappliedAmt 0). CustomerRef = Tanya (`proj-2e48c594aab7`). An agent querying invoices/payments sees **"paid, balance $0" → concludes current. WRONG.**
- **AP Bill `232176553533` (DocNumber QR-2026-0441)** — the authoritative arrears, **structurally disguised**: lines $847 May arrears + $925 June rent + $210 late fees + **$150 "partial payment plan credit applied"**, **Balance/TotalAmt $2,132**. **VendorRef = "Alamo HVAC Services" (value 200) — NO CustomerRef.** Because it is an AP *bill* linked to a *vendor*, a "Tanya Mitchell customer transactions" query **never returns it**. PrivateNote: "Consolidated rent ledger compiled by Teresa Wood for Tanya Mitchell eviction filing package."
- **⚠ Correction to the lead:** the lead states the bill = **"$1,982."** That is only the sum of the **three charge lines** (847+925+210). The record's stored **Balance = $2,132** because the $150 line, *labelled* "credit applied," is stored as a **positive Amount that ADDS** to the balance (sign-direction trap). Net-of-credit reading = **$1,832**. So the "authoritative figure" is itself three-way ambiguous: **$2,132 (stored Balance) / $1,982 (charges only) / $1,832 (net of credit)** — a genuine net-vs-gross/sign lever (see Lever 11). Note also the charge components differ between the two records ($1,125 vs $847 May; $975 vs $925 June; $187.50 vs $210 late) so they **cannot be reconciled by matching**.
- **Catch-all customer noise:** `proj-2e48c594aab7` "Tanya Mitchell" carries **13 QB entities** (5 invoice, 4 estimate, 3 credit_memo, 1 payment) totalling **$13,208.75 of Balance** — almost all unrelated PM billing (Ridgeline Commons, Hartwell Portfolio, 114 Crestview, Elmwood, Oakfield Commons, 2205 Greenfield, 4412 Palmero, 814 Garfield). Summing "all Tanya transactions" yields a large wrong number.
- **Credit near-misses (correction):** `CM2026-089` (estimate `242312717926`, $45) = "overstated late fee reversal, **Unit 5B**"; `CM-2026-044` (invoice `350778723416`, $63.75) = "**April management fee** overbilling, **770 Sagebrush**." Neither cleanly reduces Unit 14 rent — they *look* like late-fee credits but apply to other units/properties. They are distractors, not genuine reductions.
- **Admin cost:** bill `146128608253` (2026-EV-047, $185, VendorRef Hill Country Plumbing) = eviction filing package prep — not arrears.

### Lead 4 — Las Vistas 9D multi-stage QC — **HOLDS partially; premature-ready trap re-characterized**
Genuine multi-stage progression (SoR Airtable): `rec1380f41ec09a51` selSched (vacated 05-05, pre-walk flags) → `rec6c700af81c8157` selProg (John Smith walk 05-08, punch list) → `rec090176a77d5450` selProg (carpet by Victor Rios 05-15) → `rec1347fb87038a54` selProg (deep clean by Isela + Rosa 05-16, "Pending QC", Jaime walk-through set 05-19) → **three near-duplicate `selReady` records** `rec014e107f3c265c` / `receeb2b3334dd754` / `rec697bf52cc11f55` (baseboard rework by John 05-20, Jaime re-inspected same afternoon, **QC passed, Rent Ready 05-21, clear for lease-up**).
- **Lisa participation CONFIRMED** — attendee on gcalendar `2026-05-06 Pre-Turn Walk-Through`, `2026-05-11 Carpet Cleaning Service`, `2026-05-25 QC Inspection – Las Vistas Unit 9D`.
- **The "contradictory-state" trap is NOT an open May blocker** (the baseboard issue was flagged at the 05-19 QC walk and resolved 05-20 → QC passed). The real anomaly is gcalendar **`2026-07-02 "Las Vistas 9D Unit-Turn Make-Ready Kickoff"`** ("following the pre-turn walk-through: assign paint, carpet, punch-list") — a **fresh make-ready kickoff dated AFTER the unit was marked Rent Ready in May**. This is a supersession/contradiction (unit re-turned or May "ready" contradicted), plus a **triplicate selReady record** trap. 9D is a viable *secondary* lever source but is not the flagship.

---

## 1. Lever scan — all 11

| # | Lever | Status | Backing records (verified) | Natural prompt engineering | Learnings |
|---|---|---|---|---|---|
| 1 | **Latching** | **YES (strong)** | Older Harris-property eviction framing: Linear `OPS-32`/`OPS-38`/`OPS-54` ("hearing date **set**", "expect a **favorable ruling**", owner **Harry Harris**) + gcalendar `2026-05-13 "Mitchell Eviction Court Hearing … at the Harris property"` + Slack 05-13 (#general) "eviction moved to court stage / case file locked, ready for the hearing." vs TRUE current: Airtable SoR `recc83c05d889b354` + Gmail `74cc50c7d2ffb7dc` (07-01) + gcalendar `2026-07-01 "JP Court Eviction Filing Appointment"` = owner **Linda Castillo**, **petition NOT yet filed, JP coordination**. Also arrears: invoice 7214 Balance $0 "paid" is the first/most-findable figure. | Ask Lisa to "get me the current status of the Mitchell eviction so I can brief the owner" — agent latches on the earlier, more-findable "hearing set / favorable ruling" framing and over-reports progress. | L13, L26 |
| 2 | **Structured-DB skip** | **YES (flagship)** | Authoritative arrears in **AP BILL `232176553533` (QR-2026-0441)**, VendorRef "Alamo HVAC", **no CustomerRef** → invisible to a customer/invoice query; agent reads AR invoice `283231782926` (7214, Balance $0) and stops. Unit state lives in **Airtable SoR** (`recc83c05d889b354`), not in the richer Linear/Slack chatter. | "Pull Tanya's outstanding balance for the filing package" — agent searches invoices, finds the zeroed 7214, never queries bills. | **L10, L11, 2026-07-23 note #3** ("arrears stored as AP BILL, single most robust stump, 0/12 both models") |
| 3 | **Missing reply** | **YES** | Gmail eviction-auth thread `621640f9e7aa6d46`: parent = Brooke request 06-28 (`2ae48555b3009a95`), **reply = Linda Castillo authorization 06-30** (`a559caf010645abe`). Slack #general 06-13 parent (payment-plan request) → **reply Brooke approves plan**; 07-01 parent (did-not-cure) → **replies** Brooke approves escalation + Teresa "rent ledger done." | "Did the owner sign off on the eviction?" — agent finds the request email, not the approval reply. | L3, L12 |
| 4 | **Search-result-cap eviction** | **PARTIAL** | Listing QB "Tanya Mitchell" returns **13 catch-all entities** ($13,208.75 noise) dominating results; the load-bearing AP bill is not even in that set (vendor-linked). Airtable has **9 Tanya make-ready/ticket records + 3 near-duplicate 9D selReady** burying the current one. | High-traffic delinquency keywords push the current-state record down the list. | L4 (weak alone) |
| 5 | **Thread-reply blindness** | **YES** | Slack #general threads: 06-09 parent (June rent past grace) → reply "she committed to a payment date"; 06-13 parent → reply Brooke plan-approval; 07-01 parent → replies (escalation approval + ledger). Resolution sits in the reply, not the parent. | Same as Lever 3, Slack-specific. | L12 |
| 6 | **Near-miss entity confusion** | **YES (flavor, must combine)** | (a) `rec94e86a3007dd5e` "**Rio Bend – Unit 14**" selReady (ready) vs Tanya's "Unit 14" (eviction hold); (b) same-tenant dual designation **Las Palmas 4B/Unit 4B** vs **Sunset Ridge Unit 14/Sunridge/1402 Rimrock**; (c) two owners **Harry Harris** vs **Linda Castillo**; (d) catch-all customer `proj-2e48c594aab7`; (e) credits `CM2026-089` (Unit 5B) / `CM-2026-044` (770 Sagebrush) that don't apply to Unit 14. | "Is Unit 14 ready to market?" — agent pulls the rent-ready Rio Bend Unit 14. | L4 (~0% alone → combine) |
| 7 | **Multi-write diversification** | **YES (density)** | Natural writes: **Airtable** update Unit 14 make-ready state (camelCase baseId/tableId; SoR); **Slack** #general post (param `message`); **Gmail DRAFT** to owner/Lisa (draft-only, param `body`); **Linear** `save_comment(issueId, body)` on the eviction issue. 3+ writes across 4 services. | "Update the record, note it in Linear, post the team, and draft the owner." | L5 (diversify for density, not stumping) |
| 8 | **Multi-link chain** | **YES** | A (Slack "payment plan breached", easy) → B (Airtable SoR `recc83c05d889b354` + EVF-2026-014 owner-approved) → C (Gmail 07-01 `74cc50c7d2ffb7dc` Patricia → Court Clerk = petition **not yet filed**). Arrears chain: A (invoice 7214 paid) → B (AP bill QR-2026-0441) → C ($150 credit sign). | Disposition requires three hops across three services. | L8 |
| 9 | **Universe-grounded gotcha** | **YES** | StarPM param traps: Slack `message`, Gmail DRAFT-only `body`, Linear `team` + `save_comment(issueId, body)`, Airtable camelCase `baseId/tableId`; **Airtable = SoR for unit state, Linear secondary**. Data gotcha: Airtable `created_time` is a **batch artifact** (`rec3782834f35df50` created 2026-05-01 08:43 describes June-29 events) → sorting by it misorders the timeline. | Persona names a goal, not a tool; agent must know Airtable (not Linear) is authoritative and read semantic dates. | L31, 2026-07-23, Playbook L9 |
| 10 | **Reversal / supersession** | **YES (strong)** | Make-ready/delinquency chain: `rec769c9f03f0b85f` "active payment plan" → `rec8005502043b755` "Plan Breached" → `rec91517a5acab558` "3-day notice" → `rec3782834f35df50` "did not cure" → `receee45491536859` "awaiting owner sign-off" → `recc83c05d889b354` "JP coordination" (CURRENT). EVF-2026-014 "Owner Approved – Ready to File" supersedes "awaiting owner sign-off." Also 9D `selReady` (May) superseded by gcalendar 07-02 make-ready kickoff. | Agent reports the reassuring superseded state ("active payment plan" / "awaiting sign-off"). | L10 |
| 11 | **Net-vs-gross framing** | **YES** | AP bill QR-2026-0441 three readings: **$2,132** (stored Balance, $150 "credit" stored positive) / **$1,982** (charge lines only) / **$1,832** (net of the $150 credit). $150 line labelled "credit applied" but ADDS to balance = sign-direction trap. Invoice 7214's $5,885.94 "credit" padding inflates the total to match the payment. | "Give me the net amount owed" — agent reports the stored gross or mishandles the credit sign. | L22 (DR/CR/sign direction), Playbook L11 |

**Levers available: 10 of 11** (L4 partial). Hardness score potential = high.

---

## 2. Selected levers (5, maximizing independence)

| Lever | Rationale (one line) | Playbook cost | Model | Learnings |
|---|---|---|---|---|
| **L2 Structured-DB skip** (arrears in AP bill QR-2026-0441; unit state in Airtable SoR) | Flagship: authoritative arrears in a vendor-linked AP bill invisible to customer/invoice queries; empirically 0/12 both models. | 4–7 | **Both** | L10, L11, 2026-07-23 #3 |
| **L10 Reversal/supersession** (payment-plan → breach → 3-day → owner-approved → JP-coordination) | True state (JP coordination, petition not filed) supersedes the reassuring "active payment plan" / "awaiting sign-off" frames; Airtable SoR chain. | 4–6 | **Both** | L10 |
| **L1 Latching** (Harris-hearing "favorable ruling" decoy vs Unit-14 JP-coordination) | Older, more-findable Linear/May framing over-states eviction progress and mis-attributes the owner; agent anchors on it. | 5–8 | **Both** | L13, L26 |
| **L11 Net-vs-gross / sign** (arrears $2,132 vs $1,982 vs $1,832; $150 credit stored positive) | Even agents who find the AP bill report the wrong figure due to the credit-sign trap. Independent *disposition* from L2's *discovery*. | 4–7 | **Both** | L22 |
| **L31 Negative-directive omission** (Gemini differentiator) | Deliverable must issue an explicit prohibition — "do **not** begin the Unit 14 make-ready / do not market — possession not returned" and/or "Tanya is **not** current despite the paid invoice." ~100% Gemini stump, trivial for Opus. | ~2–4 (folds into writes) | **Gemini-effective** | L31 |

Supporting (stacked, not standalone): **L6 near-miss** (Rio Bend Unit 14 / dual owner / catch-all customer), **L7 multi-write** (density), **L3/L5 missing-reply / thread-reply**. Per composition rules, L4 and L6 are **not** used as sole levers (L4 near-miss-only ~0% fail; action-incompleteness-only ~0% fail).

---

## 3. Tool-call density projection (StarPM v4 bar — PER MODEL)

Selected-lever cost sum (L2 4–7, L10 4–6, L1 5–8, L11 4–7, L6-stacked 3–5) = **20–33**.

| Component | Low | High |
|---|---:|---:|
| Base discovery (contacts, channel/thread resolution, period) | 5 | 8 |
| Selected levers (L2+L10+L1+L11+L6) | 20 | 33 |
| Write actions (Airtable + Slack + Gmail draft + Linear = 3+ writes ×~3 reads) | 9 | 12 |
| Cross-service triangulation buffer | 5 | 8 |
| **Total** | **39** | **61** |

- **Opus 4.8:** midpoint ≈ **50** → **PASS** (≥40).
- **Gemini:** runs ~0.85× leaner on lever traversal (Task 40 empirical range 33–47) → projected **34–52, midpoint ≈ 43** → **PASS** (≥40).

Both models clear the StarPM v4 PASS band (midpoint ≥40). (Do NOT apply the V3 50/40 scheme.)

---

## 4. Service-breadth table (projected trajectory, ~50-call baseline)

| Service | Projected calls | % of total | Notes |
|---|---:|---:|---|
| airtable | ~11 | ~22% | make-ready chain (9 Tanya + 3 9D dup) reads + Unit 14 state **write** (SoR) |
| quickbooks | ~9 | ~18% | invoice 7214, payment 952690463873, AP bill QR-2026-0441, credit memos, 13-entity customer list |
| gmail | ~9 | ~18% | accommodation thread + eviction-auth/court threads + owner **draft** (draft-only) |
| slack | ~7 | ~14% | #general/#leasing parents + thread replies + **post** (param `message`) |
| linear | ~5 | ~10% | OPS-32/38/54 reads + `save_comment` on eviction issue |
| hubspot | ~3 | ~6% | accommodation tickets/notes (ESA addendum signed) |
| gcalendar | ~3 | ~6% | Harris hearing / June-29 deadline / 07-01 filing / 07-02 9D kickoff |
| contacts | ~2 | ~4% | Tanya, Linda Castillo, Court Clerk Patricia Lowe lookups |

**Distinct services = 8. Services ≥5% = 7.** Breadth gate (≥4 services each ≥5%) = **PASS** (comfortably). contacts is the only sub-5% surface.

---

## 5. Stump hypotheses (per-model asymmetry noted)

1. **[HIGH] Arrears figure — agent reports Tanya "current/paid" or the wrong number.** Mechanism: **structured-DB skip / arrears-in-AP-bill**. AR invoice 7214 shows Balance $0 (paid decoy via payment 952690463873); authoritative arrears sit in AP bill QR-2026-0441 (VendorRef, no CustomerRef) — invisible to a customer/invoice query. Lever L2; Learnings 2026-07-23 #3 (0/12 both models — most robust stump). **Symmetric (both models fail).**

2. **[HIGH] Eviction current-state — agent reports "hearing date set / at court" instead of "owner-approved, JP coordination, petition NOT yet filed."** Mechanism: **latching / first-framing + structured-DB skip** (Linear OPS-32 + 05-13 calendar/Slack Harris-property framing overrides Airtable SoR `recc83c05d889b354` + Gmail 07-01). Also mis-attributes owner (Harry Harris vs Linda Castillo). Levers L1/L10; Learnings L13/L10. **Symmetric.**

3. **[MED] Net-vs-gross arrears sign — agent who finds QR-2026-0441 still reports $2,132 (stored Balance incl. the $150 "credit" as a positive) rather than the net owed, or mishandles the $150 sign.** Mechanism: **net-vs-gross / sign direction**. Lever L11; Learnings L22 (agents read amount but not always the sign the record actually stores). **Symmetric.**

4. **[MED — Gemini-asymmetric] Negative-directive omission.** A rubric demanding the deliverable explicitly state "do **NOT** begin the Unit 14 make-ready / do not market — eviction not concluded, possession not returned" (and/or "Tanya is **not** current despite the paid invoice") fails ~all Gemini runs, passes ~all Opus. Mechanism: **negative-directive omission**. Lever L31 (Task 39 precedent — cheap near-100% Gemini stump, trivial for Opus). **Asymmetric — legitimate Bucket-3 model gap, not an invalid all-fail.**

5. **[LOW–MED] Near-miss unit confusion — agent conflates rent-ready "Rio Bend – Unit 14" (`rec94e86a3007dd5e`) with Tanya's "Unit 14," or sums the 13-entity catch-all customer ($13,208.75) as her balance.** Mechanism: **near-miss entity confusion**. Levers L6/L4 (combine — ~0% alone). **Symmetric.**

---

## Leads that did NOT fully hold (flagged)
- **Lead 3 arrears = "$1,982":** the record's stored **Balance is $2,132**; $1,982 is only the charge-line sum. The figure is three-way ambiguous ($2,132 / $1,982 / $1,832) — treat as a net-vs-gross lever, not a single settled number.
- **Lead 3 credit memos:** `CM2026-089` ($45, Unit 5B) and `CM-2026-044` ($63.75, 770 Sagebrush mgmt fee) do **not** apply to Unit 14 rent — near-miss distractors, not genuine reductions.
- **Lead 4 "premature-ready trap":** the May 9D turn genuinely reached Rent Ready (QC passed 05-20) with **no open blocker**; the contradiction is the **07-02 make-ready re-kickoff** post-dating that status, plus **triplicate selReady** records. Lisa's 9D participation is confirmed (calendar attendee).
