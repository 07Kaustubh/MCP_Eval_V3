# Hardness Plan — Tasks/41_6a61a86a3453b3714bdc72ef

**Universe:** StarPM (Star Property Management, LLC) · **Framework:** V4 (dual-model: Opus 4.8 + Gemini) · **Universe today:** 2026-07-01 (America/Chicago).
**Density bar (framework-scoped):** StarPM v4 per-model — midpoint >=40 PASS / 15-39 THIN / <15 INSUFFICIENT. The V3 50/40 scheme does NOT apply.

## Persona and Business Function
- **Patricia Nguyen** (`patricia.nguyen@starpm.com`, p_010) — Onsite Property Manager. *(Reassigned from Lisa Smith p_002 at S1.5 — see `_aux/Linter_Decision.md`. The rent/eviction/QuickBooks-ledger/filing-package workstream this task exercises is Patricia's anchored territory, not Lisa's; Lisa's only Tanya Mitchell scenario is the ESA accommodation, which is legally independent of the delinquency.)*
- **Property Operations** (BF1, 32% weight) — unchanged (Patricia is also an Onsite PM in BF1).
- Anchors the **entire Tanya Mitchell rent-collection and eviction lifecycle**: leads `rent_late_first_notice`, `rent_delinquency_payment_plan`, `rent_3day_notice_pay_or_quit`, `eviction_filing_prep` (Teresa pulls the consolidated rent ledger from QuickBooks; Patricia assembles the filing packet and obtains Linda Castillo owner authorization), and `eviction_court_coordination` (creates the "Eviction Hearing — Mitchell, Harris Property" Linear issue, coordinates with Court Clerk Patricia Lowe).

## Levers Available
Every "yes" is grounded in a record ID read directly from `_aux/Universe_Split/` and independently re-verified.

| # | Lever | Status | Evidence (verified record ids) | Cost range |
|---|---|---|---|---|
| 1 | **Latching** | yes (strong) | Older/more-findable Harris framing overstates progress + mis-attributes owner: Linear `OPS-32` ("Eviction Hearing - Mitchell, **Harris Property**", hearing date **set**), `OPS-38`, `OPS-54` ("checklist complete") vs Airtable SoR `recc83c05d889b354` (freshest, 2026-07-01: petition being coordinated with JP, **not yet filed**) + `rec922b9a2d1b9451` EVF-2026-014 (owner = **Linda Castillo**). Arrears: AR invoice `283231782926` (DocNumber 7214) Balance $0 "paid" is the first figure the agent hits. | 5-8 |
| 2 | **Structured-DB skip** | yes (**flagship**) | Authoritative arrears in **AP bill `232176553533` (DocNumber QR-2026-0441)**: VendorRef "Alamo HVAC Services", **no CustomerRef** -> invisible to any customer/invoice query. Agent finds AR invoice `283231782926` (7214, Balance $0) and stops. Unit state lives in **Airtable SoR** (`recc83c05d889b354`), not the richer Linear/Slack chatter. | 4-7 |
| 3 | **Missing reply** | yes | Gmail eviction-auth thread: parent Brooke request (06-28) -> **reply Linda Castillo authorization (06-30)**. Slack #general parents (payment-plan request; did-not-cure) -> replies (Brooke plan approval; escalation approval + Teresa "ledger done"). | 3-5 |
| 4 | **Search-result-cap eviction** | partial | Listing QB "Tanya Mitchell" returns **13 catch-all customer entities** ($13,208.75 of unrelated PM billing on `proj-2e48c594aab7`); the load-bearing AP bill is vendor-linked and not even in that set. 9 Tanya make-ready/ticket records + 3 near-duplicate 9D `selReady` bury the current one. | 3-5 |
| 5 | **Thread-reply blindness** | yes | Slack #general threads (06-09 / 06-13 / 07-01): resolution sits in the reply (payment date committed; plan approved; escalation approved), not the parent. | 2-4 |
| 6 | **Near-miss entity confusion** | yes (stacked) | (a) `rec94e86a3007dd5e` "**Rio Bend - Unit 14**" selReady (rent-ready) vs Tanya's "Unit 14" (eviction hold); (b) same-tenant dual designation **Las Palmas 4B / Unit 4B** (payment-plan track) vs **Sunset Ridge Unit 14 / Sunridge / 1402 Rimrock** (eviction track); (c) two owners **Harry Harris** vs **Linda Castillo**; (d) catch-all customer `proj-2e48c594aab7`; (e) credits `CM2026-089` (Unit 5B) / `CM-2026-044` (770 Sagebrush) that do NOT apply to Unit 14. | 3-5 |
| 7 | **Multi-write diversification** | yes (density) | Natural writes: **Airtable** update Unit 14 make-ready state (SoR, camelCase baseId/tableId); **Slack** #general/#make-ready post (param `message`); **Gmail DRAFT** to owner/Lisa (draft-only, param `body`); **Linear** `save_comment(issueId, body)` on the eviction issue. 3+ writes across 4 services. | 9-12 |
| 8 | **Multi-link chain** | yes | A (Slack "payment plan breached", easy) -> B (Airtable SoR `recc83c05d889b354` + EVF-2026-014 owner-approved) -> C (Gmail 07-01 petition-not-filed). Arrears chain: A (invoice 7214 paid) -> B (AP bill QR-2026-0441) -> C ($150 credit sign). | 6-9 |
| 9 | **Universe-grounded gotcha** | yes | StarPM param traps (Slack `message`, Gmail draft-only `body`, Linear `team` + `save_comment(issueId, body)`, Airtable camelCase); **Airtable = SoR, Linear secondary**. Data gotcha: Airtable `created_time` is a **batch-load artifact** (`rec3782834f35df50` stamped 2026-05-01 08:43 describes June-29 events) -> sorting by it misorders the timeline; semantic note-dates are authoritative. | 3-5 |
| 10 | **Reversal / supersession** | yes (strong) | Delinquency chain: `rec769c9f03f0b85f` "active payment plan" -> `rec8005502043b755` "Plan Breached" -> `rec91517a5acab558` "3-day notice" -> `rec3782834f35df50` "did not cure" -> `receee45491536859` "awaiting owner sign-off" -> `recc83c05d889b354` "JP coordination" (CURRENT). EVF-2026-014 "Owner Approved" supersedes "awaiting sign-off". 9D `selReady` (May) superseded by gcalendar 07-02 make-ready re-kickoff. | 4-6 |
| 11 | **Net-vs-gross framing** | yes | AP bill QR-2026-0441 three readings: **$2,132** (stored Balance; $150 "credit applied" line stored as a **positive** that ADDS) / **$1,982** (three charge lines only) / **$1,832** (net of the $150 credit). Invoice 7214's $5,885.94 "credit" padding inflates the total to $8,173.44 to match the payment. Charge components differ between bill and invoice ($847 vs $1,125 May; $925 vs $975 June; $210 vs $187.50 late) so they cannot be reconciled by matching. | 4-7 |

**Levers available: 10 of 11** (L4 partial). Well above the 3-lever floor.

## Selected Levers (5)
- **Lever 2 — Structured-DB skip (flagship).** Authoritative arrears in vendor-linked AP bill QR-2026-0441, invisible to customer/invoice queries; empirically the single most robust StarPM stump (Learnings 2026-07-23 #3, 0/12 both models). Cites L10 + 2026-07-23 #3. Projected cost midpoint 5.5.
- **Lever 10 — Reversal / supersession.** True eviction state (JP coordination, petition not filed) supersedes the reassuring "active payment plan" / "awaiting owner sign-off" frames; Airtable SoR chain. Cites L10. Midpoint 5.
- **Lever 1 — Latching.** Older, more-findable Linear/calendar "hearing set / favorable ruling, Harris property" framing overstates progress and mis-attributes the owner (Harris vs Linda Castillo). Cites L13, L26. Midpoint 6.5.
- **Lever 11 — Net-vs-gross / sign.** Even agents who reach the AP bill report the wrong figure ($2,132 stored vs $1,832 net) because the $150 "credit" is stored as a positive. Independent disposition step from L2's discovery. Cites L22. Midpoint 5.5.
- **Lever 31 (StarPM dual-model) — Negative-directive omission (Gemini differentiator).** A deliverable line demanding an explicit prohibition ("do NOT begin the Unit 14 make-ready / do not market - possession not returned" and/or "Tanya is NOT current despite the paid invoice") is a near-100% Gemini stump, trivial for Opus. Cites L31. Cost folds into the write actions (~2-4).

Stacked/supporting (not standalone): **L6 near-miss** (Rio Bend Unit 14, dual owner, catch-all customer), **L7 multi-write** (density), **L3/L5 missing-reply / thread-reply**. Per composition rules, L4 and L6 are not used as sole levers (each ~0% fail alone). Independence: L2 (discovery) / L11 (disposition) / L1 (anchor override) / L10 (temporal supersession) attack four different reasoning failures; not three latching variants.

## Tool-Call Density Projection
Selected-lever cost sum (L2 4-7, L10 4-6, L1 5-8, L11 4-7, L6-stacked 3-5) = 20-33.

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (contacts, channel/thread resolution, period) | 5-8 | 6.5 |
| Selected levers (L2 + L10 + L1 + L11 + L6-stacked) | 20-33 | 26.5 |
| Write actions (Airtable + Slack + Gmail draft + Linear = 3+ writes x ~3 reads) | 9-12 | 10.5 |
| Cross-service triangulation buffer | 5-8 | 6.5 |
| **TOTAL projected** | **39-61** | **~50** |

**Per-model bands (StarPM v4):**
- **Opus 4.8:** midpoint ~50 -> **PASS** (>=40).
- **Gemini:** runs ~0.85x leaner on lever traversal (Task 40 empirical 33-47) -> projected ~34-52, midpoint ~43 -> **PASS** (>=40).

**Gate:** both models clear the StarPM v4 PASS band (midpoint >=40). No THIN/INSUFFICIENT justification required. (V3 50/40 scheme deliberately NOT applied.)

## Service Breadth (v11 G1)
StarPM services (per `Validators/universes.py`): airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack.

| Service | Calls | % of total |
|---|---|---|
| airtable | ~11 | ~22% |
| quickbooks | ~9 | ~18% |
| gmail | ~9 | ~18% |
| slack | ~7 | ~14% |
| linear | ~5 | ~10% |
| hubspot | ~3 | ~6% |
| gcalendar | ~3 | ~6% |
| contacts | ~2 | ~4% |
| **Distinct services** | **8** | — |

**Breadth gate:** 8 distinct services, **7 at >=5%** of a ~50-call trajectory -> **PASS** (>=4 services each >=5%). No single service dominates (max airtable ~22%, well under 60%). This is cross-correlation-heavy, not a single-service deep trap — the pattern Opus 4.8 actually fails on. contacts is the only sub-5% surface.

## Stump Hypothesis (5 predictions; per-model asymmetry noted)
1. **[HIGH] Arrears figure — agent reports Tanya "current / paid" or the wrong number.** Mechanism: structured-DB skip / arrears-in-AP-bill. AR invoice 7214 shows Balance $0 (paid decoy via payment 952690463873); authoritative arrears sit in AP bill QR-2026-0441 (VendorRef, no CustomerRef), invisible to a customer/invoice query. Levers L2; Learnings 2026-07-23 #3 (0/12 both models). **Symmetric.**
2. **[HIGH] Eviction current-state — agent reports "hearing date set / at court" instead of "owner-approved, JP coordination, petition NOT yet filed", and/or mis-attributes the owner as Harry Harris.** Mechanism: latching / first-framing + structured-DB skip (Linear OPS-32 + Harris-property calendar/Slack framing overrides Airtable SoR `recc83c05d889b354` + EVF-2026-014 Linda Castillo). Levers L1/L10; Learnings L13/L10/L26. **Symmetric.**
3. **[MED] Net-vs-gross sign — agent who finds QR-2026-0441 still reports $2,132 (stored Balance incl. the $150 "credit" as a positive) rather than the net owed, or otherwise mishandles the $150 sign.** Mechanism: net-vs-gross / sign direction. Lever L11; Learnings L22. **Symmetric.**
4. **[MED - Gemini-asymmetric] Negative-directive omission.** A rubric demanding the deliverable explicitly state "do NOT begin the Unit 14 make-ready / do not market - eviction not concluded, possession not returned" (and/or "Tanya is NOT current despite the paid invoice") fails ~all Gemini runs, passes ~all Opus. Mechanism: negative-directive omission. Lever L31 (Task 39 precedent). **Asymmetric — legitimate Bucket-3 model gap, not an invalid all-fail.**
5. **[LOW-MED] Near-miss unit confusion — agent conflates rent-ready "Rio Bend - Unit 14" (`rec94e86a3007dd5e`) with Tanya's "Unit 14", or sums the 13-entity catch-all customer ($13,208.75) as her balance.** Mechanism: near-miss entity confusion. Levers L6/L4 (combine — ~0% alone). **Symmetric.**

## Hardness Score
**5/5 — PASS.** 10 of 11 levers available; 5 selected with maximal independence, each cited to a Learnings entry. Density midpoint ~50 Opus / ~43 Gemini (both PASS the StarPM v4 >=40 bar). Breadth 8 services / 7 >=5% (PASS). No STOP gate fired.

## Hardness Brief for the Prompt Writer
Write an **implicit** ask in Lisa Smith's warm-professional voice that has her **believe the reassuring frame** and ask the agent to execute — do NOT hint anything is wrong (L15/L16). The natural task: Lisa needs the **current, filing-ready status of the Tanya Mitchell (Unit 14) eviction** and the **outstanding balance for the filing package / owner brief**, plus updates to the record and a note to the owner. The four load-bearing traps the deliverable must force the agent to get right, without naming any of them: (1) the authoritative arrears live in the **vendor-linked AP bill QR-2026-0441 ($2,132 stored / $1,832 net of the $150 credit)** — the findable AR invoice 7214 is a **$0-balance paid decoy**, so an invoice/payment-only agent reports "current" (L2, flagship); (2) the true eviction state per the **Airtable system of record** is **owner-approved (Linda Castillo, EVF-2026-014), petition being coordinated with the JP but NOT yet filed** — the more-findable **Linear "hearing set, Harris property" framing over-states progress and names the wrong owner** (L1 + L10); (3) the **net-vs-gross / sign** on the $150 "credit applied" line (L11); (4) a **Gemini-differentiating explicit prohibition** — the deliverable must state the Unit 14 make-ready must NOT begin / the unit must NOT be marketed because possession has not been returned, and/or that Tanya is NOT current despite the paid invoice (L31). Target density ~50 tool calls across 8 services (airtable + quickbooks + gmail + slack + linear dominant). Keep the accommodation approval (ESA, legally independent of the rent eviction) available as a near-miss that must NOT be conflated with the delinquency. Remember StarPM param traps: Slack `message`, Gmail draft-only `body`, Linear `save_comment(issueId, body)`, Airtable camelCase `baseId`/`tableId`. The correct arrears figure must NEVER appear verbatim in any prompt/email/Slack/note — it must be DERIVED from the AP bill lines.
