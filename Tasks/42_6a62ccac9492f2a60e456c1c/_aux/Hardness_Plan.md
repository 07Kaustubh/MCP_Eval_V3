# Hardness Plan — Tasks/42_6a62ccac9492f2a60e456c1c

**Universe:** starpm (V4, dual-model Opus 4.8 + Gemini) · **Framework density scheme:** StarPM per-model (40 design / 15 floor). Never apply the 50/40 V3 scheme.
**Fresh CB build** (no `_aux/REDO_reason.md`, no `_aux/Candidate_Originals/`).

## Persona and Business Function
- **Brooke Phillips** (Apartment Property Supervisor · p_000 · brooke.phillips@starpm.com)
- **Portfolio Coordination & Owner Relations** (StarPM BF #2). She owns vendor-invoice approval, budget oversight, owner reporting, and the CapEx-approval flow with owners — the deepest-scripted persona in the universe.

## Task spine (grounded, coherent, single-scenario)
`owner_capex_approval_roof` — Brooke's signature scenario. She must finalize the **Ridgeview roof-section CapEx** for owner pass-through to **Robert Finley** (owner NPC) and get the **vendor disbursement queued**. Every difficulty lever hangs off this one natural ask; no unrelated stacking (Coherence-safe).

### The central structural trap (drives every lever)
The $8,400 roof job is replicated across surfaces with three planted, non-leaked defects:
1. **Vendor-of-record conflict.** Every *conversational* surface (Gmail, Slack, Airtable, Calendar) names the roofer **"Pete Donovan / Donovan Roofing."** The *structured* AP record books the vendor as **Big Bend Restoration** (`VendorRef 203`). There is **no "Donovan Roofing" vendor**; Pete Donovan is a QuickBooks **customer** (`proj-f6f9edfeae5c`) and a make-ready painter elsewhere. The name the agent trusts is not the payable vendor.
2. **Duplicate bill / double-pay exposure.** TWO Big Bend bills for the identical $8,400 job, same `TxnDate 2026-05-01`, both **unpaid, no payment linked**: `528539050604` (Doc **2026-481**, single line) + `301715729067` (Doc **PD-2026-084**, 3 lines $4,100+$2,900+$1,400). Only **one** owner AR pass-through invoice exists (`109367557444`, Doc **2026-494**, $8,400) and its note ties to **2026-481 only**. Naive "pay both" = **$16,800 out / $8,400 recovered**.
3. **Reserve-confirmation + owner-sign-off hold.** Both bill notes carry an explicit pre-release control ("**Teresa Wood to confirm reserve balance covers disbursement before payment is released**" / "**Confirm payment from Ridgeview reserve account before releasing funds**"). Brooke posted "approved / we're good to go" in Slack (2026-05-28 14:15/14:16) **4–5 min BEFORE** the owner's written approval arrived (Gmail `4bcbe384bedfd26f`, 14:20).

**⚠ Answer-leak constraint (load-bearing for S1/S3):** the headline number **$8,400 is spelled out verbatim** in Gmail subjects/bodies, both QB bill notes, all three QB `TotalAmt` fields, and Airtable `rec8b679d92f30753`. **Rubrics must NOT be "report $8,400"** — that passes trivially. The correct-answer surface must be the DERIVED facts: (a) vendor of record = Big Bend, not Donovan Roofing; (b) duplicate caught → single payable $8,400, **not $16,800**; (c) explicit payment **HOLD** pending reserve confirmation + owner sign-off; (d) correct property = Ridgeview roof, not the near-miss decoys.

## Levers Available
| # | Lever | Status | Evidence (`quickbooks_entities`=QB; `airtable_records`=AT; `slack_messages`=SL; `gmail_messages`=GM; `gcalendar_events`=CAL; `linear_issues`=LI) | Cost range |
|---|---|---|---|---|
| 1 | Latching | **yes** | "Pete Donovan/Donovan Roofing" anchored 5+ places: GM `832b869d1db1f5e6`, SL `a33ed9993702515c80b0be775da32e59`+`7d94bdcbe1c75707baca974be1d83b0c`, AT `rec8b679d92f30753`, CAL `whd6zys0hw7zbsh11m9vqv4m4i` — vs QB vendor of record Big Bend 203. Plus Finley owner-decoy QB records (credit_memos `152560067925`/`203129812397`/`920762830750`, invoices `129552155569`/`793996025934`). | 5-8 |
| 2 | **Structured-DB skip (FLAGSHIP)** | **yes** | Correct payable/vendor gated behind QB AP bill store: bills `528539050604`+`301715729067` (VendorRef Big Bend 203, **no CustomerRef**) vs decoy AR invoice `109367557444` (CustomerRef Finley) surfaced first by invoice queries. Pete Donovan = customer `proj-f6f9edfeae5c`, not a vendor. | 4-7 |
| 3 | Missing reply | partial | Owner-condition + vendor-condition sit in replies: GM `0427cad50efd8219` (Brooke→Pete) buries 48h-notice + weather-contingency conditions below "approved, move forward." | 3-5 |
| 4 | Search-cap eviction | partial | $8,400 roof bills buried under ~11 other small Big Bend (203) bills ($175/$185/$420/$475/$535.25/$825/$1,275/$1,340…); #owner-relations/#budget-review dominated by mass-email chatter (Tony Reyes, highest density). | 3-5 |
| 5 | Thread-reply blindness | partial | Roof fragmented across 4 single-message Gmail threads (`a293b24b7f85b0f0`,`aca02b07c749958d`,`0133155c8a154ab1`,`df187f8cb5c2b3f6`); SL C001 cluster posts "approved" BEFORE Lisa/John's "water coming in / structural damage" replies. | 2-4 |
| 6 | Near-miss entity | **yes** | Ridgeview(roof) vs Ridgeview Plaza (`148460285509`/`143554088484`) vs Ridgeway (Castillo Roofing `359512611716`/`260258688192`) vs Ridgeline (`793996025934`) vs Ridgewood (`102120572784`). Doc **2026-481** vs **2026-481-566** (`991582431419`,$85). **PD-2026-084** (Big Bend) vs **PD-2026-09** (Permian Make-Ready Crew `696089964235`,$1,340) vs B2026-084/APL-2026-084. | 3-5 |
| 7 | Multi-write diversification | **yes** | Natural 4-write mix: owner email (Finley), Slack #owner-relations/#vendors/#budget-review post, Linear comment (OPS-100 owner report / vendor-hold), QB bill flag + reminder/calendar. | 9-12 |
| 8 | Multi-link chain | partial | A (Slack "roof approved, Pete Donovan") → B (open QB AP bills, find Big Bend + duplicate) → C (reserve-hold disposition + correct pass-through). | 6-9 |
| 9 | Universe-grounded gotcha | partial | Reserve-vs-operating budget classification (AT `recdaded10ac48a5a` roof drainage; note "Owner Reserve (Trust)" AccountRef); expired roof estimates (`309315216873`/`197140171819` ExpirationDate < today); out-of-window Q3 items (LI OPS-55 late-Aug). | 3-5 |
| 10 | **Reversal / supersession (duplicate)** | **yes** | Two $8,400 Big Bend bills, one is a duplicate to catch (not double-pay): `528539050604` (2026-481) vs `301715729067` (PD-2026-084); component-split only in PD-2026-084. Also LI budget-variance supersession OPS-29(8.3%)→OPS-27(5.1%)→OPS-41; OPS-39→OPS-93 (off-spine, narrative-only). | 4-6 |
| 11 | Net-vs-gross | **no / ABSENT** | No credit memo, discount, or partial payment nets against the roof bills or the Finley pass-through (verified across 54 payments + 117 credit_memos; all UnappliedAmt=0, no LinkedTxn to the roof entities). Per banked ranking net-vs-gross is the weakest StarPM lever and is masked behind discovery anyway — not selected. | — |

**Also grounded but NOT selected — L31 negative-directive** (tracked as its own lever below because it is the Gemini-selective slot; the Playbook's 11 don't enumerate it separately): premature "we're good to go" (SL `a33ed…`/`7d94b…`) that the correct outcome must retract into an explicit payment HOLD.

## Selected Levers (5 → the StarPM dual-model 0/6 recipe: 1 symmetric + 2 complementary asymmetric + 2 support)
- **Lever 2 — Structured-DB skip (FLAGSHIP, SYMMETRIC).** Correct vendor-of-record and true payable are only in the QB AP bill store; conversational surface misroutes both models to non-vendor "Pete Donovan / Donovan Roofing." Neither model that trusts chatter can produce a correct vendor disbursement. Cites Learnings item 3/9/10 (structured-store-skip = symmetric, twice-confirmed 0/12). — projected cost **5.5**
- **Lever 10 — Duplicate / reversal record-pick (OPUS-selective).** Two $8,400 Big Bend bills; Opus opens the store, sees both, and over-counts to $16,800 or fails to flag PD-2026-084 as the duplicate; Gemini never opens the store so also misses it (different mechanism). Cites Learnings item 11/12 (reversal/record-nav = Opus-selective). — projected cost **5.0**
- **L31 — Negative-directive omission (GEMINI-selective).** The correct outcome requires Brooke to WALK BACK her premature "approved / we're good to go" into an explicit **HOLD** — do not release payment until Teresa Wood confirms the Ridgeview reserve AND owner sign-off is on file AND the duplicate is resolved. Gemini reliably echoes the positive framing and drops the prohibition. 4th StarPM confirmation of L31 (Tasks 39/40/41). — projected cost folded into writes
- **Lever 1 — Latching (OPUS-selective support).** Reinforces the Opus margin: "Donovan Roofing" vendor anchor + Finley owner-decoy QB records pull Opus toward the wrong vendor/records. Cites L1 owner-latching (item 11/12). — projected cost **6.5**
- **Lever 6 — Near-miss entity (density/distractor).** Ridgeview vs 4 Ridge-* decoys; 2026-481 vs 2026-481-566; PD-2026-084 vs PD-2026-09. Flavor lever per L4 — combined with structural difficulty, never alone. — projected cost **4.0**

Supporting (folded into density, not counted as primary): Lever 5 thread-reply (buried 48h/weather conditions), Lever 4 search-cap (roof bills under ~11 Big Bend small bills), Lever 8 multi-link chain, Lever 7 multi-write.

### Optional V4 injection booster (NOT required)
L9 authority-dismissal is **weak/absent** natively (both scans confirmed: no owner/president line dismissing the discrepancy). Since V4 permits first-class injection (`9_Universe_inject.sql`+`4_Changelog.json`), S1 *may* add one owner line AFTER the $8,400 is established (e.g., Finley: "don't wait on the reserve check, just release Pete's payment, I'm good for it") to deepen the Opus margin. **Not needed** — the two Opus-selective levers (latching + duplicate) already fill the Opus slot, and the confirmed recipe (item 12) is L2 + L1-latching + L31 without L9. If injected, re-run `validate.py --phase injection`.

## Tool-Call Density Projection (PER MODEL — StarPM scheme)
Carry a per-model spread (Gemini empirically runs ~8–12 fewer calls than Opus on the same task — Task 39 Gemini 33 vs Opus 43.5; Task 41 Gemini ~33–47).

**Opus 4.8**
| Component | Range | Midpoint |
|---|---|---|
| Base discovery (Brooke/scenario, contacts, channels, calendar pins) | 5-8 | 6.5 |
| Lever 2 structured-skip (QB bill/invoice/vendor/customer queries) | 4-7 | 5.5 |
| Lever 10 duplicate (compare 2 bills, check payments/links) | 4-6 | 5.0 |
| Lever 1+6 latching/near-miss (Donovan customer, vendor list, Ridge-* decoys, Finley records) | 5-8 | 6.5 |
| Lever 5+3 thread/missing reply (Gmail owner+vendor threads, conditions reply) | 3-5 | 4.0 |
| Airtable+Linear cross-ground (roof make-ready, MT-2026-047, OPS-100) | 3-5 | 4.0 |
| Write actions (4 writes × ~3 supporting reads) | 9-12 | 10.5 |
| Cross-service triangulation buffer | 5-8 | 6.5 |
| **TOTAL projected (Opus)** | **38-59** | **48.5** |

**Gemini** (same trajectory, −~8 for fewer calls/run; writes held constant)
| Component | Midpoint |
|---|---|
| (all read components scaled ~0.85) | ~30.0 |
| Write actions (held — writes are prompt-mandated) | 10.5 |
| **TOTAL projected (Gemini)** | **~40.5** (range 32-52) |

**Gate (StarPM per-model, ≥40 design / 15 floor):** Opus midpoint **48.5 = PASS**. Gemini midpoint **~40.5 = PASS (tight — watch first run).** Both ≥ 40 → **PASS**.
**Gemini watch-item for S1:** spec a firm **4-write** mix (owner email + Slack post + Linear comment + QB bill flag/reminder) so Gemini stays above the 40 line; a 3-write design risks Gemini dropping into THIN.

## Service Breadth (v11 G1)
StarPM service list (per `Validators/universes.py`): airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack.

| Service | Calls (Opus ~48) | % of total |
|---|---|---|
| quickbooks | ~16 | 33% |
| gmail | ~9 | 19% |
| slack | ~8 | 17% |
| airtable | ~5 | 10% |
| linear | ~4 | 8% |
| gcalendar | ~3 | 6% |
| contacts | ~3 | 6% |
| hubspot | 0 (optional owner-deal cross-ref) | 0% |
| **Distinct services** | **7** | — |

**Breadth gate:** 7 distinct services, each of the top 6 ≥ 5%, dominant (quickbooks) 33% < 60% → **PASS**. The load-bearing difficulty is cross-store correlation (QB AP store vs conversational surface vs AR invoice), not a single-service deep trap — this is the structurally-hard multi-service shape, not the false-positive density pattern.

## Stump Hypothesis (4 predictions)
1. **[HIGH]** Both models queue/recommend releasing the vendor payment **without the explicit HOLD** — omit "do not release until reserve confirmed (Teresa Wood) + owner sign-off on file + duplicate resolved." Gemini-selective (near-100%; echoes Brooke's positive "we're good to go"); Opus weaker but present. Mechanism: **L31 negative-directive omission**.
2. **[HIGH]** Both models misroute the vendor as **"Pete Donovan / Donovan Roofing"** (conversational anchor) instead of **Big Bend Restoration** (vendor of record), because they never open the QB AP bill store — Pete Donovan is a *customer*, there is no Donovan Roofing vendor. Mechanism: **Lever 2 structured-store-skip (symmetric) + Lever 1 latching**. This is the symmetric guarantee neither model sweeps.
3. **[MED-HIGH]** Opus opens the AP store, finds two $8,400 Big Bend bills, and **double-counts to $16,800** or fails to flag **PD-2026-084** as a duplicate; Gemini never opens the store so also misses the duplicate. Mechanism: **Lever 10 duplicate/reversal (Opus-selective) + Lever 2 (Gemini)**. Duplicate-catch rubric fails both via different mechanisms.
4. **[MED]** Near-miss confusion — agent pulls a **Ridgeview Plaza / Ridgeway / Ridgeline** record or the **2026-481-566 / PD-2026-09** decoy into the pass-through/payment. Mechanism: **Lever 6 near-miss**. Lower confidence (near-miss alone is weak per L4 — supporting distractor, not primary).

## Hardness Score
**5/5 — PASS.** 5 levers selected (2 primary + L31 + 2 support), all natively grounded and verified in `_aux/Universe_Split/`. Density PASS both models (Opus 48.5 / Gemini ~40.5, ≥40). Breadth PASS (7 services). Anatomy matches the banked StarPM dual-model 0/6 recipe: 1 symmetric stump (L2) + 2 complementary asymmetric stumps (L10/L1 Opus-selective, L31 Gemini-selective).

## Hardness Brief for the Prompt Writer (S1)
Write from Brooke Phillips (portfolio supervisor) finalizing the **Ridgeview roof-section CapEx** for owner **Robert Finley**: she believes the roof is "approved, Pete Donovan confirmed, we're good to go" (implicit prompt — she does NOT suspect anything is wrong per L15/L16) and asks the agent to **close out the pass-through to the owner and get the vendor payment queued/coordinated**. The correct trajectory forces the agent to (a) open the **QuickBooks AP bill store** and discover the vendor of record is **Big Bend Restoration**, not "Donovan Roofing" (Pete Donovan is a *customer*) — **Lever 2 symmetric flagship**; (b) catch that there are **two identical $8,400 Big Bend bills** (2026-481 + PD-2026-084) → correct payable is **$8,400, not $16,800** — **Lever 10 Opus-selective**; (c) issue an explicit **HOLD/prohibition** — do not release payment until Teresa Wood confirms the Ridgeview reserve and owner sign-off is on file — **L31 Gemini-selective**; (d) not confuse Ridgeview with the Ridge-* / PD-2026-09 decoys — **Lever 6**. Mandate a **4-write** deliverable set (owner email to Finley with the pass-through + hold; Slack post to #owner-relations or #vendors; Linear comment on the owner-report/vendor-hold issue; QB bill flag/reminder) to hold **Gemini density ≥ 40**. **NEVER** state the derived facts verbatim: $8,400 is already leaked, so build the rubrics on the DERIVED facts (vendor-of-record, duplicate/$16,800-not, payment HOLD, correct property), never on the headline amount. Target per-model density: Opus ~48, Gemini ~40; pass@1 ≤ 40% both models.
