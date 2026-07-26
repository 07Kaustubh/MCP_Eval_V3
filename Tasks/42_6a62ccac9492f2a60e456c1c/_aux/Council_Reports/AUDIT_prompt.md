# AUDIT — S1 Prompt (STRICTEST QC Re-Verification)

**Task:** `Tasks/42_6a62ccac9492f2a60e456c1c` · **Phase:** prompt (S1) · **Deliverable:** `5_Prompt.txt`
**Universe:** starpm (V4, dual-model Opus 4.8 + Gemini) · **Density scheme:** StarPM PER-MODEL (design >=40 / floor 15). The V3 50/40 scheme is NOT applied.
**Date SSOT:** universe today = **2026-07-01** (Wed, Q3/H2 start; `_aux/Universe_Index/today_horizon.json` confirmed). The QC-spec "Jun 12 2026" string is stale base-universe text, superseded.
**Council history:** Council A (grounding) GO · Council B (adversarial) GO. This audit re-derives everything from `_aux/Universe_Split/` — prior phase outputs were NOT trusted.

## VERDICT: **PASS (STRICT)**

Zero BLOCKER hits. Zero Lens-1 sub-dims below 5. All 5 hardness levers trace from explicit prompt sentences with cited universe atoms. Density: Opus midpoint ~48 = PASS, Gemini midpoint ~40 = PASS (at floor — the single material caveat, flagged below). Answer-leakage sweep clean on every derived figure.

---

## LENS 8 — Regression anchors (recorded)
- `test_regression_anchors.py`: **62/62 PASS** (recorded as run).
- `validate.py --phase prompt`: PASS, 0 fails, 0 warns, 4 notes.
- `verify_universe_atoms.py`: PASS, 0 fails / 0 warns (re-confirmed independently below).
- `calc_similarity.py`: max composite **27.1** (< 35 threshold) — no near-pivot.

The 4 validator notes disposed: (1) word count ~319/320 — well under the 500-word cap, no issue; (2) "distinct services 2" — a narrow literal-mention count; the actual trajectory spans 7 services (Tool-Use dim), not a fail; (3) universe=starpm — informational; (4) tone note — benign. None escalates.

---

## LENS 2 — Answer-leakage sweep (derived figures) — **CLEAN, no BLOCKER**

The derived answer surface = (a) vendor of record = **Big Bend Restoration** (not Donovan Roofing); (b) single payable **$8,400 not $16,800** (duplicate caught); (c) explicit payment **HOLD**; (d) correct property = Ridgeview. `$8,400` is leaked verbatim across the universe, so the prompt must NOT state any derived fact. String search of `5_Prompt.txt`:

| Token searched | Hit? | Disposition |
|---|---|---|
| `8400`, `8,400` | none | clean |
| `16800`, `16,800` | none | clean |
| `Big Bend` | none | clean |
| `Donovan Roofing` | none | clean |
| `duplicate` / `twice` / `two bills` / `double` | none | clean |
| `hold` (as answer) | 1 hit — `"what we are holding for him"` | NOT a leak: this is "holding [reserve money] in trust for him," a natural funding reference. The derived "issue a payment HOLD" answer is NOT stated. |
| `2026-481`, `PD-2026-084`, `2026-494` | none | clean |
| `Teresa` | none | clean |
| `reserve` | 1 hit — `"coming out of Finley's reserve"` | NOT a leak: grounded funding-source reference (account 64 Owner Reserve Trust). The specific reserve-confirmation *control* is NOT stated. |
| `Ridge` | only `Ridgeview` | clean — no Ridge* decoy named, and Ridgeview is the correct target |

**"Pete Donovan" is the allowed persona-belief latch, not a leak.** The answer is that Donovan is NOT the payable vendor (he is a QB customer). Naming him surfaces L1; it does not reveal the answer. **No leakage BLOCKER.** Confirmed em-dash/en-dash: 0.

---

## LENS 1 — Strict QC scoring (every applicable Prompt sub-dim, 5/5-or-REVISE)

All scores re-derived under the strictest interpretation (NON-FAIL middle bands collapse to REVISE; every "should" read as "must").

| Sub-dim | Score / scheme | One-line reason | Prior-council miss? |
|---|---|---|---|
| Unique Ground Truth | **5** /1-3-5 (mid removed 06/09) | Single end-state: pay Big Bend once at $8,400, catch PD-2026-084 duplicate, HOLD release pending reserve confirm + duplicate resolution, pass-through $8,400 to Finley, property = Ridgeview. Hold is co-determined by prompt language AND universe controls; no reading releases. | None — but see anti-rationalization note on Para2/Para3 (escalate-vs-execute) and OPS-100/OPS-10, both resolved to single end-state. |
| Feasibility | **5** /1-3-5 | All asks actionable with StarPM tools; "prepare-but-hold" is coherent, not self-contradictory; "email Finley" resolves to a Gmail draft (StarPM gmail is draft-only). | None |
| Explicit Tool Mention | **5** /1-5 binary | No MCP tool/function names; "the books / owner relations channel / our tracker / my calendar" are natural. | None |
| Clarity & Specificity | **5** /1-3-5 | Queue-vs-hold tension explicitly resolved ("Before any money leaves"); no second reading flips the write-action SET. | None |
| Contrived / Unnatural | **5** /1-3-5 | Natural harried-supervisor voice, mid-thought entry, one situation, not a command list. | None |
| Alignment with Today's Date | **5** /1-3-5 | today 2026-07-01: "into July" ✓, "new quarter"=Q3 ✓, "late May" past ✓; forward reminder legit future. | None |
| Truthfulness | **5** /1-3-5 | Every claim grounded; Finley approval genuinely TRUE; "Pete Donovan's crew" is the persona's grounded belief (the trap is vendor-of-record, never a prompt assertion). | None |
| Tool Use & Cross-service | **5** /1-5 binary | Load-bearing cross-store reconciliation across QuickBooks + Gmail + Slack + Linear + gcalendar + Airtable (+contacts). | None |
| Investigation + Action | **5** /1-5 binary | Hidden root cause (true vendor, duplicate, hold) not pre-solved; 5 write actions. | None |
| Coherence (Bolt-on) | **5** /1-5 binary | One cohesive situation (Ridgeview roof CapEx closeout); every ask causally flows from it; sentence-removal test passes. | None |
| Persona | **5** /1-3-5 | Brooke Phillips (Apartment Property Supervisor) owns vendor-invoice approval, budget oversight, owner reporting, owner CapEx flow — in-voice. | None |
| Business Function | **5** /3-5 (no FAIL band) | Owner pass-through + owner reporting + vendor disbursement = BF#2 Portfolio Coordination & Owner Relations. | None |

**All 12 applicable Prompt sub-dims = 5/5 under strictest interpretation. No sub-dim below 5.**
Universe-dimension spot check (informational, prompt-phase): **Data Exists = 5** (all core rows materialized, verified below); **Cross-service Coherence = 5** (the Pete Donovan/Big Bend split is coherent-by-design — QB structured store is the authoritative vendor-of-record; the chatter is a deliberate, resolvable near-miss, not an unresolvable contradiction).

### PER-ATOM EVIDENCE TABLE — Truthfulness (5/5)
| Atom asserted in prompt | Universe file / query | Row excerpt | Verdict |
|---|---|---|---|
| "Robert Finley gave his approval on the Ridgeview scope" | `gmail.gmail_messages.json` id `4bcbe384bedfd26f`, from robert.finley@gmail.com → brooke.phillips@starpm.com, 2026-05-28 19:20:01 UTC | "You have my approval to proceed with the $8,400 roof section repair at Ridgeview" | TRUE — genuine approval, not false claim |
| "Pete Donovan's crew is confirmed for the work" | `slack.slack_messages.json` id `a33ed99937...` (C001, Brooke U9741B657FE, 2026-05-28); bill `528539050604` PrivateNote; AR invoice `109367557444` line | "Pete Donovan is confirmed for the job, visit is scheduled" / "Pete Donovan quote accepted at $8,400" | GROUNDED persona belief (the vendor-of-record trap is separate) |
| "I already posted that we were good to move" | `slack.slack_messages.json` ids `a33ed99937...` (19:15:37) + `7d94bdcbe1...` (19:16:09), both Brooke U9741B657FE in C001 | "Roof repair at Ridgeview is approved..." / "We're good to go." | TRUE (and predates owner approval by ~4 min = the planted L31 defect) |
| "coming out of Finley's reserve" | `quickbooks.quickbooks_entities.json` account `64` | "Owner Reserve (Trust)", Bank/TrustAccounts, CurrentBalance 70624.57 | GROUNDED |
| "sitting since late May" | approval 2026-05-28; bills TxnDate 2026-05-01, Due 2026-05-31 | all past vs today 2026-07-01 | COHERENT (defensible loose descriptor) |

### PER-ATOM EVIDENCE TABLE — Persona (5/5)
| Atom | File / query | Excerpt | Verdict |
|---|---|---|---|
| Brooke Phillips = author persona | `_aux/Universe_Index/entities_personas.md`; `slack.slack_users.json` U9741B657FE | "Brooke Phillips, brooke.phillips@starpm.com, Apartment Property Supervisor, persona" | VALID authoring persona |
| Owns owner/CapEx/vendor scope | Hardness_Plan BF#2; Slack posts + Gmail to Pete + owner-report OPS-100 authored by Brooke | Brooke posts approvals, coordinates vendor + owner pass-through | IN-SCOPE authority; no AUTHORITY_GAP |

### PER-ATOM EVIDENCE TABLE — Alignment with Today's Date (5/5)
| Atom | File / query | Excerpt | Verdict |
|---|---|---|---|
| today = 2026-07-01, Q3 start | `today_horizon.json` | "universe_today: 2026-07-01, America/Chicago" | Wed, first day of Q3 |
| "into July / new quarter" | today 2026-07-01 | first day of Q3/H2 | COHERENT |
| "late May" past | approval 2026-05-28, bills 2026-05-01 | before today | COHERENT |
| forward reminder ("come back and confirm the release") | future-facing calendar action | legit future event per date-dim note | COHERENT |

### PER-ATOM EVIDENCE TABLE — Unique Ground Truth (5/5)
| End-state component | File / query | Excerpt | Verdict |
|---|---|---|---|
| Vendor of record = Big Bend (203), single payable | `quickbooks.quickbooks_entities.json` vendors (8 total) | Big Bend `203`; NO "Donovan Roofing" vendor exists; Pete Donovan = customer `proj-f6f9edfeae5c` | Unique vendor |
| Payable = $8,400 once, NOT $16,800 (duplicate) | bills `528539050604` (Doc 2026-481, 1 line 8400) + `301715729067` (Doc PD-2026-084, 3 lines 4100+2900+1400=8400), both VendorRef 203, TxnDate 2026-05-01, Balance 8400, LinkedTxn None | two identical unpaid bills; AR note ties to 2026-481 only | Unique payable |
| HOLD until reserve confirm + duplicate resolved | bill 2026-481 note "Teresa Wood to confirm reserve balance covers disbursement before payment is released"; PD-2026-084 note "Confirm payment from Ridgeview reserve account before releasing funds" | pre-release controls unmet | Unique disposition = HOLD |
| Owner pass-through = $8,400 to Finley | invoice `109367557444` Doc 2026-494, CustomerRef Robert Finley `proj-e59d4a436ed7`, 8400 | single AR mirror | Unique recipient/amount |

Empty evidence column count = **0** → all four 5/5 dims retain their score.

---

## LENS 3 — Hardness end-to-end trace (prompt-phase) — 5/5 levers PRESERVED

| Lever | Exact prompt sentence that surfaces it | Universe atom(s) the agent must touch | Status |
|---|---|---|---|
| **L2 structured-DB skip (FLAGSHIP, symmetric)** | "Go into the books, figure out what the payable for that roof job actually is, get it set up correctly and queued" | QB AP bills `528539050604`/`301715729067` (VendorRef Big Bend 203) vs conversational "Pete Donovan"; vendor list has no Donovan Roofing; Pete Donovan = customer `proj-f6f9edfeae5c` | PRESERVED |
| **L10 duplicate / reversal (Opus-selective)** | "figure out what the payable for that roof job actually is... make sure the amount we pass back to the owner is the right one. If anything about it does not line up the way I am assuming, do not just push it through." | two identical $8,400 Big Bend bills (2026-481 + PD-2026-084), same TxnDate, both unpaid; AR 2026-494 ties to 2026-481 only | PRESERVED |
| **L31 negative-directive / HOLD (Gemini-selective)** | "Before any money leaves... do not just push it through. Bring it back to me first with what you found and what still has to happen before we can release" + "ready the moment we are truly clear" + "confirm the release once the last piece is done" | reserve-confirmation notes on both bills (Teresa Wood / Ridgeview reserve); premature Slack approval predating owner email | PRESERVED |
| **L1 latching (Opus-selective support)** | "As far as I know we are clear on it... Pete Donovan's crew is confirmed for the work" | Pete Donovan customer record; Slack/Gmail/Airtable/bill-note "Donovan" anchors; Finley owner-decoy QB records | PRESERVED |
| **L6 near-miss entity (distractor/density)** | "the Ridgeview roof section repair. The roof at Ridgeview..." (named consistently, no decoy) | Ridge* decoys confirmed in QB: Ridgecrest, Ridgeline, Ridgemont, Ridgeway, Ridgewood; doc-number near-misses | PRESERVED |

Every lever traces from a cited sentence to a materialized atom. **No HARDNESS_REGRESSION. lever_preservation = 5/5.**

---

## LENS 4 — Strict density projection (StarPM PER-MODEL, minimizing reading)

Trajectory minimizing inferred exploration (correct agent, single investigation pass, 5 mandated writes). Writes are load-bearing and cannot be dropped by a correct agent; the core investigation is load-bearing (wrong vendor / wrong amount / wrong disposition if skipped).

**Opus 4.8** — base discovery (Brooke, contacts Finley+Pete, channels, calendar) ~6 · QB bill/vendor/customer (L2) ~5 · duplicate compare + payment/link check (L10) ~5 · latching/near-miss (Donovan customer, vendor list, Ridge* , Finley decoys) (L1/L6) ~6 · thread/reply + reserve notes ~4 · Airtable roof + Linear OPS-100 ~4 · 5 writes x ~2 supporting reads ~10 · triangulation buffer ~6 → **midpoint ~48 = PASS** (>=40).

**Gemini** (reads scaled ~0.85, writes held constant) → **midpoint ~40 = PASS** (>=40), range ~32-52.

- **4/5-write mandate is genuinely present in the prompt** (verified verbatim): (1) "get the vendor payment in order... ready the moment we are truly clear" = QB bill flag/queue-with-hold; (2) "email Finley a note closing out the approval and the pass-through" = Gmail draft; (3) "post where this landed to the owner relations channel" = Slack #owner-relations (C006); (4) "Leave the disposition as a comment on the owner report issue in our tracker" = Linear OPS-100; (5) "set a reminder on my calendar" = gcalendar. Five writes across five services. This is the density backbone that holds Gemini above 40.
- **Caveat (the single material strict finding):** Gemini sits **exactly at the 40 floor**. Empirical StarPM anchors (Task 39 Gemini 33; Task 41 ~33-47) show real downside into THIN (15-39) territory under aggressive minimization. The projected midpoint meets the >=40 PASS bar and the write mandate is maxed (adding writes would bloat/gold-plate), so this does not cross into REVISE — but it is AT-FLOOR and should be confirmed on the first S4 Gemini run.
- Breadth: **7 distinct services**, dominant (QuickBooks ~33%) < 60%, top-6 each >=5% → breadth PASS.

Density band = **PASS** both models (Opus ~48, Gemini ~40 at-floor).

---

## LENS 5 — Adversarial veteran review (200+ tasks pattern recognition)

- **Implicit-prompt framing preserved.** Persona writes from the mistaken belief ("As far as I know we are clear on it"); she does not suspect the trap. Correct for L15/L16 implicit framing.
- **Entity-drift seams clean.** Finley → robert.finley@gmail.com (external owner, gmail correct). Prompt names only "Ridgeview" — no Ridge* decoy bleeds in. "Pete Donovan" is the intended latch, not drift.
- **No tool-name / MCP leaks, no em/en-dashes, no "at least N", no internal IDs, no "approximately"/"(or similar)" near exact values.** Grep-confirmed.
- **No single-channel lock-in.** The write set spans QB + Gmail + Slack + Linear + gcalendar; naming #owner-relations for the post is the persona naming a goal channel, not method lock-in.
- **Queue-payment vs HOLD is not a live contradiction.** "get the vendor payment... set up and moving" (Para 1) is explicitly governed by "Before any money leaves... do not just push it through" (Para 2) and "ready the moment we are truly clear... confirm the release once the last piece is done" (Para 3). Feasibility-safe: prepare-but-hold.
- **No authority overreach.** Brooke owns vendor-invoice approval / budget oversight / owner reporting. The one authority-adjacent item — the reserve confirmation (Teresa Wood's role) — is correctly DEFERRED by the prompt ("what still has to happen before we can release"), not usurped. No AUTHORITY_GAP.

---

## LENS 7 — Anti-Rationalization (promoted considerations)

Each "I considered flagging X but..." is promoted and given its hard exclusion:

1. **Para2 "bring it back to me first" vs Para3 "do the writes" — possible escalate-vs-execute UGT fork.** *Excluded:* Para 3 opens "Once you have a clear read" (a clear read = understanding the situation, achievable even when the situation is "not clean") and then ENUMERATES the writes, explicitly framing them around a held payment + disposition ("ready the moment we are truly clear", "set a reminder... to confirm the release once the last piece is done"). "Bring it back to me first" governs the RELEASE, and is itself satisfied by the disposition email/post/comment. No zero-write reading and no release reading is defensible → single end-state. UGT stays 5.
2. **"the owner report issue" — OPS-100 vs OPS-10 referent.** *Excluded:* OPS-100 is literally titled "May Monthly Owner Report - Finley Properties" (In Progress, Finley-specific); OPS-10 is "Mid-Year Owner Portfolio Reviews - June 2026" (Backlog, a portfolio review naming four owners). The definite article + "owner report" + roof being a May vendor cost make OPS-100 the unique referent; OPS-10 is a review, not a report. Leading-and-correct, same write action (a Linear comment). Logged as an **S3 anchoring NOTE** (anchor the comment rubric to OPS-100, do not accept OPS-10) — not a prompt-level UGT break.
3. **"Pete Donovan's crew is confirmed" — is this a false claim?** *Excluded:* it is the persona's genuine, chatter-grounded belief (Slack + Gmail + bill note + AR line all name Pete Donovan on the roof job). The universe deliberately conflates Donovan with the job on the conversational/free-text surface; the AUTHORITATIVE vendor-of-record (QB structured store) is Big Bend. The prompt asserts the belief, not the vendor identity — this is the designed L1/L2 trap, not a Truthfulness error.
4. **Gemini density at the 40 floor.** *Not fully excluded — promoted to a MINOR finding* (see Lens 4). Basis for not escalating to REVISE: projected midpoint meets the StarPM >=40 gate and the 5-write mandate (density backbone) is verified present and maxed. Action: confirm on first Gemini run.

No remaining rationalizations.

---

## Independent universe re-verification (queried live from `_aux/Universe_Split/`)
- QB vendors = 8; **Big Bend Restoration = id 203**; **no "Donovan Roofing" vendor exists**. Pete Donovan = **customer** `proj-f6f9edfeae5c` (pete.donovan@gmail.com). ✓
- Bills `528539050604` (Doc 2026-481) + `301715729067` (Doc PD-2026-084): both VendorRef 203, TotalAmt 8400, TxnDate 2026-05-01, Due 2026-05-31, Balance 8400, LinkedTxn None. **Exactly two Big Bend $8,400 bills** (the duplicate); 9 other smaller Big Bend bills provide search-cap cover (L4). ✓
- AR invoice `109367557444` Doc 2026-494, CustomerRef Robert Finley, 8400; note ties to "vendor bill 2026-481 (Pete Donovan)" only. ✓
- Reserve controls present on both bills; account 64 "Owner Reserve (Trust)" balance 70,624.57. ✓
- Finley approval email `4bcbe384bedfd26f` genuine (2026-05-28 19:20:01 UTC). Brooke Slack posts `a33e...`/`7d94b...` (19:15:37 / 19:16:09) predate it by ~4 min = L31 defect. ✓
- OPS-100 "May Monthly Owner Report - Finley Properties" (In Progress); OPS-10 decoy confirmed. #owner-relations = C006. ✓
- Ridge* decoys: Ridgecrest, Ridgeline, Ridgemont, Ridgeway, Ridgewood. ✓

---

## Summary
Zero BLOCKERs; zero sub-dims below 5; all 5 levers trace from cited prompt sentences to materialized atoms; density Opus ~48 / Gemini ~40 (StarPM per-model, both >=40 PASS). The one material caveat is Gemini sitting exactly on the 40 floor — carried as a MINOR watch-item (confirm first run), not a blocker. Two non-blocking S3 anchoring notes: (1) anchor the Linear-comment rubric to OPS-100 (reject OPS-10); (2) reward duplicate-catch / correct single $8,400 payable without hard-pinning which doc survives.

```json
{
  "phase": "audit_prompt",
  "council": "AUDIT",
  "task_dir": "Tasks/42_6a62ccac9492f2a60e456c1c",
  "verdict": "PASS_STRICT",
  "perspectives": {
    "Lens1_strict_qc": {"status": "PASS", "findings": []},
    "Lens2_answer_leakage": {"status": "PASS", "findings": []},
    "Lens3_hardness_trace": {"status": "PASS", "findings": []},
    "Lens4_density": {"status": "PASS", "findings": [
      {"severity": "MINOR", "location": "density Gemini", "issue": "Gemini midpoint ~40 sits exactly at the StarPM PASS floor; empirical anchors dip into THIN under aggressive minimization", "fix": "confirm on first S4 Gemini run; 5-write mandate already present and maxed to hold the line", "propagate_to": null}
    ]},
    "Lens5_adversarial": {"status": "PASS", "findings": []},
    "Lens7_anti_rationalization": {"status": "PASS", "findings": [
      {"severity": "NOTE", "location": "prompt:para3 / Linear OPS-100 vs OPS-10", "issue": "'the owner report issue' referent is leading-and-correct (OPS-100); OPS-10 is a portfolio review decoy", "fix": "S3: anchor comment rubric to OPS-100, reject OPS-10", "propagate_to": null},
      {"severity": "NOTE", "location": "QB bills 2026-481 vs PD-2026-084", "issue": "correct single payable is unique ($8,400 once) but which doc survives is not prompt-pinned", "fix": "S3: reward duplicate-catch / correct single payable without over-specifying surviving doc number", "propagate_to": null}
    ]},
    "Lens8_regression": {"status": "PASS", "findings": [
      {"severity": "NOTE", "location": "test_regression_anchors.py", "issue": "62/62 PASS recorded", "fix": "n/a", "propagate_to": null}
    ]}
  },
  "scores": {
    "Unique Ground Truth": {"score": 5, "scheme": "1/3/5", "reason": "single end-state: pay Big Bend once $8,400, catch duplicate, HOLD pending reserve confirm + duplicate resolution, pass-through to Finley; co-determined by prompt + universe controls"},
    "Feasibility": {"score": 5, "scheme": "1/3/5", "reason": "all asks actionable; prepare-but-hold coherent; email resolves to draft (StarPM draft-only)"},
    "Explicit Tool Mention": {"score": 5, "scheme": "1/5", "reason": "no MCP tool/function names"},
    "Clarity & Specificity": {"score": 5, "scheme": "1/3/5", "reason": "queue-vs-hold tension explicitly resolved; no second reading flips the write-action set"},
    "Contrived / Unnatural": {"score": 5, "scheme": "1/3/5", "reason": "natural harried-supervisor prose, one situation, not a command list"},
    "Alignment with Today's Date": {"score": 5, "scheme": "1/3/5", "reason": "today 2026-07-01: into July / Q3 start / late-May past all coherent; forward reminder legit future"},
    "Truthfulness": {"score": 5, "scheme": "1/3/5", "reason": "all claims grounded; Finley approval genuinely true; Pete-Donovan-crew is grounded persona belief; vendor discrepancy is designed trap not assertion"},
    "Tool Use & Cross-service": {"score": 5, "scheme": "1/5", "reason": "QuickBooks+Gmail+Slack+Linear+gcalendar+Airtable(+contacts); cross-store reconciliation load-bearing"},
    "Investigation + Action": {"score": 5, "scheme": "1/5", "reason": "hidden root cause not pre-solved; 5 write actions"},
    "Coherence (Bolt-on)": {"score": 5, "scheme": "1/5", "reason": "one cohesive situation; every ask flows from the roof CapEx closeout"},
    "Persona": {"score": 5, "scheme": "1/3/5", "reason": "Brooke Phillips owns owner relations + CapEx + vendor approval; in-voice"},
    "Business Function": {"score": 5, "scheme": "3/5", "reason": "owner pass-through + reporting + vendor disbursement = Portfolio Coordination & Owner Relations (BF#2)"}
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
  "timestamp": "2026-07-25"
}
```
