# Council B — Adversarial QC + Density + Hardness Preservation
## S1 PROMPT · Task 39_6a602c8886ebb06f12354d77 · StarPM (V4)

**Deliverable:** `Tasks/39_6a602c8886ebb06f12354d77/5_Prompt.txt`
**Phase:** prompt · **Universe:** starpm · **Today:** 2026-07-01 (America/Chicago)
**Reviewer:** Council B (oracle), five role lenses (Architect / Implementer / Red-team / Ground-truth / Integration), verdict = union.
**Read before scoring:** prompt (235 words, verified raw bytes), Hardness_Plan.md, Council_Protocol.md scoring-scheme map, today_horizon.json, and direct greps against `_aux/Universe_Split/` for every load-bearing atom. Brief NOT taken on trust.

---

## Ground-truth verification (done first, before any score)

| Atom | Universe_Split evidence | Status |
|---|---|---|
| Las Palmas 8D unit | `airtable.airtable_records` tblMakeReady + tblMaintenanceTickets | REAL |
| Stale "ready/closed out" 5/1 | `receb057b02f20052` fldTurnStatus=**selReady**, fldNotes2 "Turn closed out as of today… QC punch-list items resolved… passed final walk", created 2026-05-01 | CONFIRMED (L10 stale anchor) |
| In-house work 5/14 (John+James) | `recf7aecc318b2252` selProg "John Smith and James Bennett are three days into the in-house make-ready work" | CONFIRMED (James anchor) |
| Fridge swap 6/25 in progress | `rec651427ec0d84dd5a` selProg, target 6/26 | CONFIRMED (live state) |
| MT-2026-1271 OPEN | `recac236210094352` tblMaintenanceTickets, fldCompletionDate="" (blank=OPEN), "Move-out walk… full turn" | CONFIRMED (SoR open) |
| Rio Bend 214 twin | `recb403fe04c2f97683` MT-2026-1325, dishwasher, fldCompletionDate=2026-06-25 (twin is COMPLETE), same-day 6/25 | CONFIRMED (near-miss) |
| L1 latching chatter | slack C004 `140558bdd3…` "Both punch-list items on 8D are taken care of"; `21f0475e…` "Carpet is done on 8D… Unit is ready for the cleaning crew" | CONFIRMED |
| L3 the flip (missing reply) | linear `comment_16a0a0c53f…` OPS-227 "8D disposal is seized… full unit replacement… Routing back to you for parts approval before I swap it. — James" | CONFIRMED (OPEN) |
| L2 Airtable-is-SoR | linear `team_001` "…Airtable Maintenance Tickets table, which is the system of record. Linear is secondary…" | CONFIRMED |
| L4 decoy eviction | 61 "204B" vs 6 "Las Palmas 8D" occurrences in airtable_records | CONFIRMED (~10:1) |
| Recipient "John" | contacts `john.smith@starpm.com` = Lead Maintenance Technician (vs decoy `john.castillo@gmail.com` = external Water Delivery Rep) | RESOLVABLE / UNIQUE-IN-CONTEXT |
| make-ready channel | slack C004 #make-ready | REAL |
| Fact_Ledger.today | **null** (Brookfield-default bug; brief said 2026-06-12, actual is null) — IGNORED; used 2026-07-01 | S0 HYGIENE ADVISORY |

---

## [B1] QC sub-dimension scoring (scheme per Council_Protocol map)

- SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5) -> Investigation deterministically yields one end-state: 8D NOT ready (disposal replacement + parts approval outstanding, MT-2026-1271 OPEN, fridge swap unconfirmed). "Report ready" is a failure path, not a second valid reading (see B2).
- SUB-DIM Feasibility -> SCORE 5/5 (1/3/5) -> All required rows materialized and reachable by James's toolset; "John" resolves to john.smith@starpm.com; writes feasible across Airtable/Linear/Slack/Gmail; "draft John an email" correctly matches Gmail draft-only (no send).
- SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 binary) -> Zero tool/MCP names (verified raw-byte scan: 0 hits).
- SUB-DIM Clarity & Specificity -> SCORE 5/5 (1/3/5) -> One leading interpretation; prompt explicitly instructs verification over hearsay ("instead of going off what someone said in passing"), removing the ready/not-ready ambiguity. "get it moving" latitude is OE/rubric-pinnable and does not create a second end-state.
- SUB-DIM Contrived / Unnatural -> SCORE 5/5 (1/3/5) -> A junior tech verifying a turn before telling his lead it's done is highly natural; multi-service investigation arises organically, not bolted on.
- SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5) -> All relative phrases ("today", "since May", "a week later") resolve cleanly at 2026-07-01; live data exists in the resolved window (fridge target 6/26, disposal open through 6/22). Fact_Ledger.today=null does NOT affect this judgment.
- SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5) -> Every factual claim grounds. "punch-list got knocked out and the carpet's in" is hedged persona belief ("from what I've picked up… on paper") that faithfully mirrors the Slack chatter — the intended latch, not an authorial falsehood. The truly-done items really are done; the miss is the disposal.
- SUB-DIM Tool Use & Cross-service -> SCORE 5/5 (1/5 binary) -> Investigation spans Slack+Airtable+Linear+Gmail+Contacts+Calendar; writes span >=3 services. Not single-service.
- SUB-DIM Investigation + Action -> SCORE 5/5 (1/5 binary) -> Investigate ("figure out where 8D really stands") + Act ("get it moving so it can genuinely close" + reconcile the log + Slack post + Gmail draft). Write actions present.
- SUB-DIM Coherence (Bolt-on) -> SCORE 5/5 (1/5 binary) -> Single coherent scenario; every ask shares the same entities (8D, John, the crew, the make-ready channel). No bolt-on.
- SUB-DIM Persona -> SCORE 5/5 (1/3/5) -> James Bennett junior voice (formality 0.35): casual, deferential to his lead, practical ("square up", "come back on me", "the straight story"). No finance/exec register.
- SUB-DIM Business Function -> SCORE 5/5 (3/5, no FAIL band) -> Make-ready turn reconciliation + reporting is squarely Maintenance & Repairs (BF4). Match.

**B1 result: every applicable sub-dim = 5. PASS.**

---

## [B2] Adversarial second-reading attack

**Intended stump:** an agent that trusts the Slack "done" chatter + the most-emphatic 5/1 "closed out" row reports 8D **ready** — WRONG.

**Unique correct end-state:** 8D is **NOT** ready. The garbage-disposal replacement is outstanding (OPS-227: seized, needs full unit replacement, parts approval pending); MT-2026-1271 is OPEN in the Airtable SoR (blank completion date); the 6/25 fridge swap has no completion confirmation as of today (target was 6/26; today 7/1). At minimum the disposal is unambiguously open, so not-ready is determinate.

**Second-reading test — does any reasonable re-read flip a write action, recipient, or final state?**
- Recipient: "John" → john.smith@starpm.com uniquely in context (the external John Castillo is an implausible Water-Delivery-Rep decoy; prompt context — "waiting on word… make-ready channel… the crew" — binds John to the maintenance lead). No recipient flip.
- Final state: The prompt textually forbids taking chatter at face value ("confirm where each piece actually landed instead of going off what someone said in passing"). Reading it as "trust the chatter → ready" is a **violation of an explicit instruction**, i.e. the engineered FAILURE path, not a defensible alternative reading. No end-state flip.
- Write set: reconcile the log (Airtable), advance the open item (Linear/route parts approval), Slack #make-ready post, Gmail draft to John — content of each is fixed once the investigation surfaces the disposal. No write flip.

**Verdict: UNIQUE correct end-state confirmed. "Report ready" is a genuine failure path, not a second valid reading. No Unique-Ground-Truth / Clarity flag.**

Minor (non-blocking) note for S2/S3: "get it moving so it can genuinely close" leaves the exact unblock write (comment on OPS-227 vs escalate parts approval to the approver) to be pinned by the OE/rubric. This is bounded latitude, not a prompt ambiguity — it does not create a second end-state.

---

## [B3] Tool-call density projection — StarPM V4 per-model bands (>=40 PASS / 15-39 THIN / <15 INSUFFICIENT)

Opus 4.8 trajectory sketch (per model):
1. contacts: resolve "John" → john.smith@starpm.com (+ dedupe vs John Castillo) — 1-2
2. slack: read #make-ready (C004) history → the "8D done" chatter — 1-2
3. slack: search/read "8D" across channels + threads — 1-2
4. airtable: broad Las Palmas/make-ready query (returns 204B swarm) then refine to 8D — 2-4
5. airtable: tblMaintenanceTickets → MT-2026-1271 (blank completion = OPEN) — 1-2
6. airtable: the three 8D make-ready rows (selReady 5/1, selProg 5/14, selProg 6/25) — 2-3
7. linear: OPS-227 issue + comments → disposal-seized / parts-approval flip — 2-3
8. linear: team/SoR context — 1
9. gcalendar: 6/25 swap dispatch / completion check — 1-2
10. cross-check Rio Bend 214 twin (avoid conflation) — 1
11. gmail: related-thread scan — 1-2
   Discovery subtotal ≈ 16-24.
Writes + verification re-reads:
12. airtable update make-ready record to true (not-ready + outstanding) — 1-2
13. linear comment on OPS-227 to advance parts approval — 1-2
14. slack #make-ready post — 1
15. gmail create_draft to John — 1
   Write subtotal ≈ 4-6, plus re-query buffer under decoy pressure.

**Independent midpoint ≈ 46-48 per model** (Hardness_Plan projects 48.5). **Band: PASS** (>= 40 StarPM V4 design target; well above the 15 floor). Applies to Opus 4.8 and Gemini separately.

---

## [B4] Hardness preservation (each lever must still be surfaced by the prompt's framing)

- **L10 reversal/supersession** — PRESERVED. "this turn has been dragging since May", "I'd bet some of it is stale by now", "confirm where each piece actually landed" forces the agent past the 5/1 "ready" row to the later live rows.
- **L2 structured-DB skip** — PRESERVED. Prompt names no service; "confirm where each piece actually landed" + "square up what we've got logged" drives the agent to the Airtable SoR rather than the Linear mirror / Slack chatter.
- **L1 latching** — PRESERVED. Prompt echoes the "done" chatter ("punch-list got knocked out and the carpet's in… on paper it looks about there") AND demands it be broken ("instead of going off what someone said in passing"). Latch planted + challenge issued.
- **L4 search-result-cap eviction** — PRESERVED. Centering on "Las Palmas 8D" plus "everything that was supposed to happen on that unit" forces the 8D-specific dig under the 204B decoy swarm.
- **L3 missing reply** — PRESERVED. "if something's still open, run down whatever it's waiting on" pushes the agent into the OPS-227 reply where the disposal disposition ("parts approval before I swap it") lives.

**No HARDNESS_REGRESSION. All 5 levers preserved. The prompt correctly does NOT name Airtable/Linear (keeps L2/L4) and does NOT name the disposal (keeps L1/L3).**

---

## [B5] Tool-leak / phrasing scan

- Tool/MCP names: **0** (raw-byte scan).
- Internal IDs (MT-/OPS-/rec ids): **0** in prompt body.
- Em-dash / en-dash / figure-dash / minus / horizontal-bar: **0**. Smart quotes: **0**. Non-ASCII: none.
- "at least N": none. Generic-urgency cliché / QC-sample cliché: none.
- Word count: 235 (<= 500 cap).
- Pre-solving check: "I'd bet some of it is stale" is a hedged persona SUSPICION (does not name the disposal, the ticket, or which record); "if something's still open" / "what's still outstanding if anything" are conditional. The prompt reveals neither that the disposal is open, nor that a specific record is wrong, nor that the ticket is unclosed. It preserves the persona's belief that the unit is "about there". **No pre-solving, no over-signaling. No hits.**

---

## [B6] Upstream propagation

No B6 flag is triggered BY the prompt: the prompt masks no upstream defect and is itself fully date-aligned and grounded.

Two upstream S0 **hygiene advisories** are surfaced for the operator (neither affects any prompt sub-dim; neither blocks this GO, but both must be fixed before the phases that consume them):

- **ADVISORY (S0):** `_aux/Fact_Ledger.json` `lifecycle.today` is **null** (brief expected the Brookfield-default 2026-06-12; the real value is null). Authoritative today = 2026-07-01 per today_horizon.json, used throughout. **Impact: none on the prompt** (all prompt dates are relative and resolve correctly). **Must fix before S2/S3** — Council A A3 narrative-state checks consume Fact_Ledger lifecycle atoms; a null/wrong today will mis-judge state there. Fix: rebuild Fact_Ledger with `build_fact_ledger.py` seeding today from the registry (2026-07-01), or patch `lifecycle.today` to 2026-07-01.
- **ADVISORY (S0):** `_aux/S0_Setup_Report.md` claims `9_Universe_inject.sql` is "present with executable statements (73 lines)" and injection returned PASS, but the file is a comment-only stub and `4_Changelog.json` is `[]` (already caught by Hardness_Plan §"Injection status"). **Impact: none on the prompt** (scenario is baked into `3_UniverseDataForThisTask.json`). Fix: correct the S0 report to "no separately-documented injection".

**No blocking PROPAGATE flag for the S1 prompt.**

---

## Role-lens union
- **Architect:** structure fits V3/V4 prompt-format (situation → verification ask → reconcile+report ask → closing motive). Clean. No issue.
- **Implementer:** every referenced surface real and reachable (John Smith email, C004 channel, 8D rows, OPS-227). No issue.
- **Red-team:** best adversarial path is the engineered stump (trust chatter → "ready"), which the prompt text forbids — not a defensible alt-reading. No write/recipient/state flip. No issue.
- **Ground-truth:** every claim grounds to per-task Universe_Split (table above). No base-universe assumption. No issue.
- **Integration:** all 5 hardness levers preserved end-to-end; density holds; upstream advisories recorded, non-blocking. No issue.

---

## VERDICT: **GO**

Every applicable prompt sub-dim = 5; no second valid reading flips a write action, recipient, or final state; per-model density midpoint ≈ 47 (>= 40 StarPM V4); all 5 levers (L10/L2/L1/L4/L3) preserved; no phrasing hits; no prompt-blocking upstream PROPAGATE. Two S0 hygiene advisories recorded for pre-S2 fix (non-blocking for this phase).

```json
{
  "council": "B",
  "perspective_set": ["B1","B2","B3","B4","B5","B6"],
  "phase": "prompt",
  "task": "39_6a602c8886ebb06f12354d77",
  "universe": "starpm",
  "deliverable": "Tasks/39_6a602c8886ebb06f12354d77/5_Prompt.txt",
  "verdict": "GO",
  "blockers": [],
  "sub_dim_scores": {
    "Unique Ground Truth": "5/5 (1/3/5)",
    "Feasibility": "5/5 (1/3/5)",
    "Explicit Tool Mention": "5/5 (1/5 binary)",
    "Clarity & Specificity": "5/5 (1/3/5)",
    "Contrived / Unnatural": "5/5 (1/3/5)",
    "Alignment with Today's Date": "5/5 (1/3/5)",
    "Truthfulness": "5/5 (1/3/5)",
    "Tool Use & Cross-service": "5/5 (1/5 binary)",
    "Investigation + Action": "5/5 (1/5 binary)",
    "Coherence (Bolt-on)": "5/5 (1/5 binary)",
    "Persona": "5/5 (1/3/5)",
    "Business Function": "5/5 (3/5 no-FAIL)"
  },
  "adversarial_second_reading": {
    "unique_end_state": true,
    "end_state": "8D NOT ready: disposal replacement + parts approval outstanding, MT-2026-1271 OPEN, fridge swap unconfirmed",
    "report_ready_is_failure_path": true,
    "flips_write_or_recipient_or_state": false
  },
  "density": {
    "per_model_midpoint": 47,
    "range": "40-55",
    "band": "PASS",
    "bands_applied_separately_to": ["opus_4.8","gemini"],
    "floor": 15,
    "design_target": 40
  },
  "hardness_preservation": {
    "L10_reversal_supersession": "preserved",
    "L2_structured_db_skip": "preserved",
    "L1_latching": "preserved",
    "L4_search_cap_eviction": "preserved",
    "L3_missing_reply": "preserved",
    "regression": false
  },
  "phrasing_scan": {
    "tool_names": 0,
    "internal_ids": 0,
    "em_or_en_dash": 0,
    "at_least_n": 0,
    "pre_solving": false,
    "word_count": 235,
    "hits": false
  },
  "propagate_flags": [
    {"to": "S0", "blocking": false, "root_cause": "_aux/Fact_Ledger.json lifecycle.today is null (expected 2026-07-01)", "file": "_aux/Fact_Ledger.json", "fix": "rebuild via build_fact_ledger.py seeding today from registry (2026-07-01) or patch lifecycle.today", "impact_on_prompt": "none; must fix before S2/S3 A3 narrative-state checks"},
    {"to": "S0", "blocking": false, "root_cause": "S0_Setup_Report claims injection PASS but 9_Universe_inject.sql is comment-only stub and 4_Changelog.json is []", "file": "_aux/S0_Setup_Report.md", "fix": "correct report to 'no separately-documented injection'", "impact_on_prompt": "none"}
  ],
  "notes": [
    "Fact_Ledger.today is null (not 2026-06-12 as brief stated); used authoritative 2026-07-01 from today_horizon.json; no date-alignment judgment changed.",
    "'get it moving' unblock write is bounded latitude for S2/S3 to pin (comment on OPS-227 vs escalate parts approval); not a second end-state.",
    "'John' resolves uniquely-in-context to john.smith@starpm.com; John Castillo (external Water Delivery Rep, gmail.com) is an implausible decoy."
  ]
}
```
