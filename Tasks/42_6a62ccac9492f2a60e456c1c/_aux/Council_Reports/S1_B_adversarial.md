# Council B — Adversarial QC + Density + Hardness Preservation

**Phase:** prompt (S1) · **Task:** `42_6a62ccac9492f2a60e456c1c` · **Deliverable:** `5_Prompt.txt`
**Framework:** StarPM (V4, dual-model Opus 4.8 + Gemini) · **Density scheme:** StarPM PER-MODEL (design ≥40 / floor 15). V3 50/40 scheme NOT applied.
**Date SSOT:** universe today = **2026-07-01** (confirmed `_aux/Universe_Index/today_horizon.json`; the QC-spec "Jun 12 2026" string is stale base-universe text and is overridden by this task's horizon file).
**Review mode:** read-only, 5 role lenses (Architect / Implementer / Red-team / Ground-truth / Integration).

---

## Verification base (queried live from `_aux/Universe_Split/`)

| Prompt claim / design atom | Universe evidence | Verdict |
|---|---|---|
| Ridgeview roof section repair | QB bill `528539050604` Line desc "Roof section repair - Ridgeview property, damaged flashing…" | GROUNDED |
| Vendor of record = **Big Bend Restoration** (not Donovan Roofing) | QB bills `528539050604` (Doc 2026-481) + `301715729067` (Doc PD-2026-084) both `VendorRef {Big Bend Restoration, 203}`. Vendor list = 8 vendors, **no "Donovan Roofing"** | GROUNDED (L2) |
| Pete Donovan is NOT a vendor | `proj-f6f9edfeae5c` = QB **customer** "Pete Donovan"; index role = "Exterior Painter" NPC | GROUNDED (L1) |
| Duplicate: two identical $8,400 bills | `528539050604` (1 line, $8,400) + `301715729067` (3 lines $4,100+$2,900+$1,400), both TxnDate 2026-05-01, Due 2026-05-31, Balance 8400, no LinkedTxn | GROUNDED (L10) |
| Single owner AR pass-through | invoice `109367557444` Doc 2026-494, `CustomerRef {Robert Finley, proj-e59d4a436ed7}`, $8,400; note ties to **bill 2026-481 only** | GROUNDED |
| Reserve-confirmation HOLD control | Bill 2026-481 note: "Teresa Wood to confirm reserve balance covers disbursement before payment is released." Bill PD-2026-084 note: "Confirm payment from Ridgeview reserve account before releasing funds." | GROUNDED (L31) |
| "coming out of Finley's reserve" | QB account `64` = "Owner Reserve (Trust)" Bank/TrustAccounts | GROUNDED |
| Finley "gave his approval" (verify NOT a false claim) | Gmail `4bcbe384bedfd26f` Finley→Brooke: "You have my approval to proceed with the $8,400 roof section repair" | **TRUE — not a false claim** |
| "Pete Donovan's crew is confirmed" (persona belief) | Brooke→Pete Gmail `0427cad50efd8219`: "ready to move forward with your crew"; Slack `a33e…` (C001, 2026-05-28 14:15 CT): "Pete Donovan is confirmed for the job" | GROUNDED as persona belief |
| "I already posted that we were good to move" | Slack `a33e…` (2026-05-28); water-intrusion reply `ad54…` posted 25 s later (L5) | GROUNDED |
| "owner relations channel" | Slack channel `C006` `#owner-relations` | GROUNDED |
| "owner report issue in our tracker" | Linear `OPS-100` "May Monthly Owner Report - Finley Properties" | GROUNDED |
| "set a reminder on my calendar" | gcalendar `brooke.phillips@starpm.com` exists | GROUNDED |
| Near-miss decoys (L6) | QB Ridge* tokens: Ridgecrest, Ridgeline, Ridgemont, Ridgeview, Ridgeway, Ridgewood | GROUNDED |
| "into July / new quarter" | today 2026-07-01 = first day of Q3 | COHERENT |
| "sitting since late May" | approval 2026-05-28, due 2026-05-31 | COHERENT (defensible loose descriptor) |

---

## [B1] QC sub-dimension scoring

SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5, mid band removed 06/09) -> Single end-state: pay Big Bend once at $8,400 (catch duplicate PD-2026-084), HOLD release pending reserve confirm + owner sign-off + duplicate resolution, pass-through to Finley, correct property Ridgeview; hold is co-determined by prompt language AND universe controls — no reading releases.
SUB-DIM Feasibility -> SCORE 5/5 (1/3/5) -> All asks actionable with StarPM tools; "queue but hold" is coherent not contradictory; "email Finley" resolves to a draft (StarPM gmail is draft-only) — feasible.
SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 binary) -> No MCP tool/function names; "the books / owner relations channel / our tracker / my calendar" are natural references.
SUB-DIM Clarity & Specificity -> SCORE 5/5 (1/3/5) -> Request is specific (reconcile payable, set up + hold, owner pass-through, four named writes + reminder); the queue-vs-hold apparent tension is resolved by "Before any money leaves…" and "confirm the release once the last piece is done"; no second reading flips a write action.
SUB-DIM Contrived / Unnatural -> SCORE 5/5 (1/3/5) -> Reads as a harried supervisor's natural message ("I'd rather spend the extra day now than have owner money go out wrong"); goal-oriented prose, not a step-by-step command list.
SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5) -> today 2026-07-01: "into July" ✓, "new quarter"=Q3 start ✓, "late May" past ✓; forward-facing reminder is legitimately future.
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5) -> Every claim grounded; Finley's approval is genuinely TRUE (Gmail 4bcbe384…); "Pete Donovan's crew" is the persona's hedged belief grounded in Gmail/Slack chatter; the Big Bend/duplicate discrepancy is the DESIGNED trap the agent must discover, never a prompt assertion.
SUB-DIM Tool Use & Cross-service -> SCORE 5/5 (1/5 binary) -> Requires QuickBooks + Gmail + Slack + Linear + gcalendar + Airtable (+contacts); load-bearing difficulty is cross-store reconciliation (AP store vs conversational surface vs AR invoice).
SUB-DIM Investigation + Action -> SCORE 5/5 (1/5 binary) -> Heavy hidden-root-cause investigation (open books → true vendor, catch duplicate, reconcile pass-through, resolve decoys) plus 4–5 write actions; root cause is concealed, not told.
SUB-DIM Coherence (Bolt-on) -> SCORE 5/5 (1/5 binary) -> One cohesive situation (close out the Ridgeview roof CapEx); every ask causally flows from that single purpose; no unrelated staple-on.
SUB-DIM Persona -> SCORE 5/5 (1/3/5) -> Brooke Phillips (Apartment Property Supervisor) owns vendor-invoice approval, budget oversight, owner reporting and the owner CapEx flow — the prompt is squarely in-voice.
SUB-DIM Business Function -> SCORE 5/5 (3/5, no FAIL band) -> Owner pass-through + owner reporting + vendor disbursement coordination is unambiguously "Portfolio Coordination & Owner Relations."

**All 12 applicable Prompt sub-dims = 5. Bar met on every dimension.**

## [B2] Adversarial alt-path / second reading

- **Queue-vs-hold collision — RESOLVED, not divergent.** Para 1's "set up and moving so the crew can be paid" is immediately governed by Para 2's "Before any money leaves, though…do not just push it through. Bring it back to me first" and Para 3's "ready the moment we are truly clear…confirm the release once the last piece is done." The instruction is unambiguously *prepare-but-hold*. No reasonable reading releases funds now.
- **Hold is universe-determined, not just prompt-asserted.** Both bill notes prescribe a reserve-confirmation pre-release control (Teresa Wood / Ridgeview reserve), the duplicate is unresolved, and the AR mirror ties only to 2026-481. The "truly clear" condition is objectively unmet → the correct end-state is HOLD regardless of how the prompt is parsed. Unique Ground Truth is reinforced by the universe, not merely by wording.
- **No recipient/write-set divergence.** Owner = Finley (only owner in scope); channel = #owner-relations (C006); tracker issue = the Finley owner report; calendar = Brooke's. All singular and grounded.
- **Two minor S3-scoping watch-items (NOT prompt-level UGT breaks):**
  1. Linear referent: "the owner report issue" points to `OPS-100` (Finley-specific "May Monthly Owner Report"); `OPS-10` (Mid-Year Portfolio Reviews) also names Finley among four owners. The definite article + Finley-specificity + the roof being a May vendor cost make OPS-100 the clear referent; the alternative is a portfolio-wide review, not "the owner report." Leading-and-correct — **NOTE for S3** (anchor rubric to OPS-100, don't over-specify).
  2. Which exact bill doc "survives": end-state (pay $8,400 once, flag the duplicate) is unique; AR ties to 2026-481. **NOTE for S3** to reward catching the duplicate / correct single payable without hard-pinning a doc number.

**No adversarial divergence that breaks Unique Ground Truth.**

## [B3] Tool-call density projection — StarPM PER-MODEL

Trajectory a competent agent runs: base discovery (Brooke/scenario, contacts, channels, calendar) → open QB AP books → identify Big Bend as vendor of record (vs Donovan customer) → catch the duplicate (compare both $8,400 bills, check payments/links) → find AR pass-through 2026-494 → find reserve-hold notes → cross-check Airtable roof record + Linear OPS-100 → resolve Ridge* / doc-number near-misses → **4–5 writes** (QB bill flag/hold-note, owner email draft to Finley, Slack #owner-relations post, Linear comment on OPS-100, calendar reminder) each with supporting reads.

| Component | Opus midpoint | Gemini (~0.85 reads) |
|---|---:|---:|
| Base discovery | 6.5 | 5.5 |
| L2 structured-skip (bill/invoice/vendor/customer) | 5.5 | 4.5 |
| L10 duplicate compare | 5.0 | 4.0 |
| L1+L6 latching / near-miss | 6.5 | 5.5 |
| L5+L3 threads / conditions reply | 4.0 | 3.5 |
| Airtable + Linear cross-ground | 4.0 | 3.5 |
| Writes (4–5 × ~3 reads, held constant) | 10.5 | 10.5 |
| Triangulation buffer | 6.5 | 3.5 |
| **TOTAL midpoint** | **≈48** | **≈40** |

- **Opus ≈ 48 → PASS** (≥40).
- **Gemini ≈ 40 → PASS** (≥40, tight — watch first run; already flagged in Hardness_Plan).
- **4-write mandate confirmed present in the prompt** ("get the vendor payment in order" = QB flag/hold; "email Finley a note"; "post…to the owner relations channel"; "leave the disposition as a comment on the owner report issue"; plus "set a reminder on my calendar"). This holds Gemini writes constant at ~10.5 and keeps Gemini above the 40 floor.

**Both models ≥ 40 → density band = PASS.**

## [B4] Hardness preservation

| Lever | Prompt trigger | Status |
|---|---|---|
| **L2 structured-DB skip (flagship, symmetric)** | "Go into the books, figure out what the payable for that roof job actually is" forces opening the QB AP store → surfaces Big Bend as vendor of record; anyone trusting the chatter ("Pete Donovan's crew") misroutes. | PRESERVED |
| **L10 duplicate / reversal (Opus-selective)** | "figure out what the payable…actually is…make sure the amount we pass back to the owner is the right one" → opening the store exposes two $8,400 Big Bend bills to reconcile. | PRESERVED |
| **L31 negative-directive / hold (Gemini-selective)** | "Before any money leaves…do not just push it through. Bring it back to me first…confirm the release once the last piece is done. I would rather spend the extra day now than have owner money go out wrong." | PRESERVED |
| **L1 latching (Opus-selective support)** | "As far as I know we are clear…Pete Donovan's crew is confirmed for the work" anchors the agent to Donovan (a customer/painter), the wrong-vendor decoy. | PRESERVED |
| **L6 near-miss (distractor/density)** | "Ridgeview" named consistently against 5+ Ridge* decoys + doc-number near-misses; agent must disambiguate. | PRESERVED |

**5/5 levers preserved. No HARDNESS_REGRESSION.**

## [B5] Tool-leak / phrasing scan

- No MCP tool/function names. ✓
- No internal IDs (no bill/doc/record numbers, no VendorRef). ✓
- No em-dashes / en-dashes (grep clean). ✓
- No "at least N", no "approximately", no "(or similar)". ✓
- **No leaked derived answer:** the prompt contains no dollar amount, no "Big Bend", no "duplicate", no "$16,800", no "$8,400", no "Teresa", no "Donovan Roofing". Only "reserve" (natural, grounded persona reference to the funding source — the specific reserve-confirmation *control* is NOT stated) and "Pete Donovan" (the intended latching decoy, not a derived answer). ✓

**No phrasing/leak hits.**

## [B6] Upstream propagation

The prompt faithfully implements the Hardness_Plan: every selected lever is grounded in `_aux/Universe_Split/`, the answer-leak constraint is honored (no derived fact stated), and the density/write mandate is met. No issue traces to a root cause in the Hardness_Plan.

**No propagation flags.**

---

## VERDICT: **GO**

Every applicable QC sub-dim scores 5. No adversarial divergence breaks Unique Ground Truth (the hold-vs-release end-state is co-determined by the prompt language and the universe's reserve-confirmation controls / unresolved duplicate). Projected density ≥ 40 for both models (Opus ≈48, Gemini ≈40 tight). All five hardness levers remain triggered by the prompt as written. No phrasing/leak hits. No upstream propagation flags.

**Non-blocking NOTES carried to S3:** (1) anchor the Linear-comment rubric to OPS-100 (not OPS-10); (2) reward catching the duplicate / correct single $8,400 payable without hard-pinning which doc number survives; (3) Gemini density is at the 40 floor — confirm on first run.

```json
{
  "phase": "prompt",
  "council": "B",
  "task_dir": "Tasks/42_6a62ccac9492f2a60e456c1c",
  "verdict": "GO",
  "perspectives": {
    "B1": {
      "status": "PASS",
      "findings": []
    },
    "B2": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "prompt:para3 / Linear OPS-100 vs OPS-10",
          "issue": "'the owner report issue' has a clear referent (OPS-100 Finley) but OPS-10 also names Finley among four owners",
          "fix": "S3: anchor the comment rubric to OPS-100; do not accept OPS-10",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "QB bills 2026-481 vs PD-2026-084",
          "issue": "correct single payable is unique ($8,400 once) but which doc survives is not prompt-pinned",
          "fix": "S3: reward duplicate-catch / correct single payable without over-specifying the surviving doc number",
          "propagate_to": null
        }
      ]
    },
    "B3": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MINOR",
          "location": "density Gemini",
          "issue": "Gemini midpoint ~40 sits exactly at the floor",
          "fix": "confirm on first S4 run; 4-write mandate already present to hold the line",
          "propagate_to": null
        }
      ]
    },
    "B4": {
      "status": "PASS",
      "findings": []
    },
    "B5": {
      "status": "PASS",
      "findings": []
    },
    "B6": {
      "status": "PASS",
      "findings": []
    }
  },
  "scores": {
    "Unique Ground Truth": {"score": 5, "scheme": "1/3/5", "reason": "single hold end-state co-determined by prompt + universe reserve controls; no reading releases funds"},
    "Feasibility": {"score": 5, "scheme": "1/3/5", "reason": "all asks actionable; queue-but-hold coherent; email resolves to draft (StarPM draft-only)"},
    "Explicit Tool Mention": {"score": 5, "scheme": "1/5", "reason": "no MCP tool/function names"},
    "Clarity & Specificity": {"score": 5, "scheme": "1/3/5", "reason": "specific asks; queue-vs-hold tension explicitly resolved; no second reading flips a write action"},
    "Contrived / Unnatural": {"score": 5, "scheme": "1/3/5", "reason": "natural harried-supervisor prose, single cohesive situation, not a command list"},
    "Alignment with Today's Date": {"score": 5, "scheme": "1/3/5", "reason": "today 2026-07-01: into July / Q3 start / late-May past all coherent"},
    "Truthfulness": {"score": 5, "scheme": "1/3/5", "reason": "all claims grounded; Finley approval genuinely true; Pete-Donovan crew is hedged persona belief, discrepancy is designed trap not assertion"},
    "Tool Use & Cross-service": {"score": 5, "scheme": "1/5", "reason": "QuickBooks+Gmail+Slack+Linear+gcalendar+Airtable; cross-store reconciliation load-bearing"},
    "Investigation + Action": {"score": 5, "scheme": "1/5", "reason": "hidden-root-cause investigation plus 4-5 writes; not pre-solved"},
    "Coherence (Bolt-on)": {"score": 5, "scheme": "1/5", "reason": "one situation; every ask flows from the roof CapEx closeout"},
    "Persona": {"score": 5, "scheme": "1/3/5", "reason": "Brooke Phillips owns owner relations + CapEx + vendor approval; in-voice"},
    "Business Function": {"score": 5, "scheme": "3/5", "reason": "owner pass-through + reporting + vendor disbursement = Portfolio Coordination & Owner Relations"}
  },
  "density_projection": {
    "midpoint": 40,
    "opus_midpoint": 48,
    "gemini_midpoint": 40,
    "band": "PASS",
    "scheme": "starpm_per_model",
    "breadth_services": 7,
    "breadth_band": "PASS"
  },
  "lever_preservation": {
    "expected": 5,
    "preserved": 5,
    "missing": []
  },
  "bucket_1_risk_pct": null,
  "iteration": 1,
  "timestamp": "2026-07-25T00:00:00Z"
}
```
