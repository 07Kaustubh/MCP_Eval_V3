# AUDIT — Veteran QC Second-Opinion (Strictest Interpretation) — S1 PROMPT

**Task:** Tasks/39_6a602c8886ebb06f12354d77
**Deliverable:** `5_Prompt.txt` (233 words, 1216 bytes)
**Universe:** starpm (V4) · today = 2026-07-01 America/Chicago
**Persona:** James Bennett (p_006, james.bennett@starpm.com) · Assistant Maintenance Technician · junior · formality 0.35 · Business Function 4 (Maintenance & Repairs)
**Mode:** Auto-fire (post Council A GO + Council B GO). Read-only.
**Density bar applied:** StarPM V4 PER-MODEL (design 40+ / floor 15), NOT the V3-family 50/40 scheme.
**Verdict:** **PASS (STRICT)**

Methodology: every load-bearing atom re-queried directly from `_aux/Universe_Split/` (row_data parsed, not taken on the brief's or the councils' word). Prior council verdicts re-read for pattern-misses. Byte-level phrasing scan run on raw prompt bytes. Regression-anchor suite executed. One net-new finding the lighter passes did not isolate (Lens 2 corroboration leak) is surfaced below as a NON-BLOCKING S2/S3 advisory.

---

## LENS 1 — Strict QC scoring (every applicable sub-dim, 5/5 the only pass)

| # | Sub-dim (band) | Score | Basis (strictest reading) | Prior council miss? |
|---|---|---|---|---|
| 1 | Unique Ground Truth (1/5) | **5** | Single end-state: 8D NOT ready (MT-2026-1271 OPEN + disposal replacement/parts-approval outstanding). "Report ready" violates the prompt's explicit "instead of going off what someone said in passing" = engineered FAILURE path, not a 2nd valid reading. No end-state divergence. | none |
| 2 | Feasibility (1/3/5) | **5** | All rows materialized + reachable by James. "draft John an email" matches Gmail draft-only `create_draft` EXACTLY (a strength, not a gap). 4 writes (Airtable update / Linear comment / Slack post / Gmail draft) all feasible + within junior authority; parts-approval spend correctly routed to John, not self-approved. No dimensional-breakdown ask. | none |
| 3 | Explicit Tool Mention (1/5) | **5** | Byte scan: 0 tool/MCP/param tokens. "make-ready channel"/"email"/"logged" are natural service references. | none |
| 4 | Clarity & Specificity (1/3/5) | **5** | One leading interpretation; prompt mandates verification over hearsay. Write-action-divergence gate: recipient resolves uniquely (below); channel literal; write set fixed. Delegation-clarity gate: no "I'll [verb]" self-action ambiguity — James delegates the work, then personally reports to John afterward (consistent with draft-only Gmail). | none |
| 5 | Contrived / Unnatural (1/3/5) | **5** | A junior tech double-checking a turn before telling his Lead it is done is highly natural. Difficulty is organic (scattered signals, stale record, buried disposal), not contrived precision. No timestamp/format demands. | none |
| 6 | Alignment with Today's Date (1/3/5) | **5** | Relative phrases ("today","since May","a week later","now") resolve cleanly vs fixed 2026-07-01; live data in-window; universe broadly consistent with 7/1. End-state robust to the local 6/12 validator artifact (see date deep-dive). | none |
| 7 | Truthfulness (1/3/5) | **5** | Per-atom evidence table below grounds every tight identifier; zero phantoms. The one belief-vs-truth gap ("looks about there") is a hedged persona belief mirroring real Slack chatter (the intended latch), not an authorial falsehood. | none |
| 8 | Tool Use & Cross-service (1/5) | **5** | Investigation spans Slack+Airtable+Linear+Gmail+Contacts+Calendar; writes span >=4 services. Not single-service. | none |
| 9 | Investigation + Action (1/5) | **5** | Investigate ("figure out where 8D really stands") + Act (advance open item + reconcile record + Slack post + Gmail draft). Multiple writes. | none |
| 10 | Coherence / Bolt-on (1/5) | **5** | Single coherent situation; sentence-removal test passes on all 4 paragraphs. No bolt-on. | none |
| 11 | Persona (1/3/5) | **5** | Junior voice, formality 0.35: "square up", "come back on me", "the straight story", "on paper it looks about there". No finance/exec register. Matches PersonaBrief. | none |
| 12 | Business Function (3/5) | **5** | Independently source-verified (see below). James home BF = 4; 8D disposal-replacement is the literal Cat 4.1 worked example; persona-anchor rule governs the turnover setting. Match. | none |
| 13 | Universe Data Exists (1/5) | **5** | Every load-bearing row materialized + MCP-retrievable. | none |
| 14 | Universe Cross-service Coherence (1/5) | **5** | No injection (comment-only stub); base scenario internally consistent across Airtable/Linear/Slack/Contacts. | none |

**Every applicable sub-dim = 5/5 under strictest interpretation. No sub-dim < 5.**

### Per-atom evidence table (required for Truthfulness / Data-Exists 5/5)

| Atom asserted (prompt) | Universe query | Row excerpt (verbatim) | Verdict |
|---|---|---|---|
| "Las Palmas 8D" unit | airtable_records tblMakeReady / tblMaintenanceTickets | `receb057b02f20052` fldUnit="Las Palmas 8D"; `recac236210094352` fldTicketNumber="MT-2026-1271" | GROUNDED |
| "John" (Lead / recipient) | contacts.contacts | John Smith `john.smith@starpm.com` job="Lead Maintenance Technician" (only other John = external John Castillo `john.castillo@gmail.com` Water Delivery Rep) | GROUNDED, unique-in-context |
| "punch-list got knocked out" | slack C004 | `140558bdd3...` "Both punch-list items on 8D are taken care of, touch-up paint and the baseboard are good to go." (John Smith, 5/27) | GROUNDED (belief-source) |
| "the carpet's in" | slack | `21f0475e...` "Carpet is done on 8D, Victor finished up the cleaning and seam fix." (5/23) | GROUNDED (belief-source) |
| "the make-ready channel" | slack_channels | `C004` name="#make-ready" | GROUNDED |
| "dragging since May" | airtable 8D date span | `receb057` 2026-05-01 -> `recf7aec` 2026-05-14 -> `rec651427` 2026-06-25 | GROUNDED |
| implicit open item (the flip) | linear_comments | `comment_16a0a0c53f...` OPS-227 "The 8D disposal is seized... needs a full unit replacement... Routing back to you for parts approval before I swap it." (6/22) | GROUNDED (OPEN) |
| Airtable = system of record | linear_teams | `team_001` "...Airtable Maintenance Tickets table, which is the system of record. Linear is secondary for maintenance items..." | GROUNDED |
| MT-2026-1271 OPEN (SoR) | airtable tblMaintenanceTickets | `recac236210094352` fldCompletionDate="" (blank = open) | GROUNDED (OPEN) |
| stale "ready" anchor | airtable tblMakeReady | `receb057b02f20052` fldTurnStatus="selReady", "Turn closed out as of today... cleared for leasing" created 2026-05-01 | GROUNDED (stale) |
| live-state supersession | airtable tblMakeReady | `rec651427ec0d84dd5a` fldTurnStatus="selProg", fldTargetReady="2026-06-26" (still selProg at today 7/1) | GROUNDED (live) |

Empty-evidence cells: none. Truthfulness scored 5/5 with proof, per the v18 per-atom contract.

---

## LENS 2 — Answer-leakage sweep (NET-NEW FINDING — non-blocking)

The "answer" is a QUALITATIVE end-state (8D NOT ready: disposal replacement + parts approval outstanding, MT-2026-1271 OPEN), not a derived figure. Sweeps run:

- Prompt body: does NOT reveal the disposal, the fridge, the ticket, parts-approval, "not ready", "wrong", or "incorrect" (byte scan: all such tokens = 0). Only hedged suspicion ("I'd bet some of it is stale") + conditionals ("if something's still open", "what's still outstanding if anything"). No prompt-side leak.
- Universe bodies the prompt asks the agent to read: **1 corroboration cluster found.** James Bennett's own two 6/22 messages in **#maintenance (C001)** state: *"8D disposal needs a replacement (waiting on parts approval from John), so that unit's still open"* and *"8D disposal is seized... routed it to @john.smith for parts approval before I swap it."* This verbalizes the core correct end-state in plain language.

**Severity: NON-BLOCKING ADVISORY (routed to S2/S3), NOT a prompt blocker. Reasoning (each an explicit hard-exclusion, not a rationalization):**
1. **Channel placement defuses the "single obvious read" concern.** The statement is in #maintenance (C001). The channel the prompt directs James to ("the make-ready channel" = C004) carries the MISLEADING narrative — its 8D thread ends at Brooke Phillips 5/29 "8D is officially cleared and ready for leasing" + the 6/25 fridge-swap logistics. The obvious channel points at the WRONG answer; the truth requires broadening to C001 / the Airtable SoR ticket / OPS-227.
2. **Over-determined + persona-organic.** It is the persona's OWN prior message (James flagged the disposal 9 days before "today"), part of the latching/missing-reply design, and the correct end-state is independently established by the SoR ticket (blank completion) + OPS-227 + supersession. Removing it would not change solvability; its presence does not remove the reconcile/advance/post/draft write workflow.
3. **Does not defeat the stump.** The failure mode (latch on the loud "done / cleared / ready" chatter -> report ready) is not neutralized by a contradicting line in a different channel: a shallow agent will not necessarily read C001-6/22, and an agent that does must still choose to trust the later "still open" over the earlier louder "cleared and ready" — which IS the intended synthesis.
4. **Out of scope for a PROMPT revise.** The leak is universe-data-resident (baked into `3_UniverseDataForThisTask.json`), not prompt-resident. No prompt edit adds or removes it; the prompt neither cites nor amplifies it. It therefore cannot force a prompt REVISE.

**S2/S3 action (advisory):** design the OE/rubric so full credit requires demonstrated synthesis + the write workflow (correct the SoR record to true state, advance OPS-227 / route parts approval, post #make-ready, draft John with the outstanding items). "Agent read one Slack line" must not alone earn the outcome. Optional re-hardening: the Hardness plan's authority-injection (a Lead "8D is done, mark it ready" message planted after the reductions) would neutralize the corroboration and lift difficulty — optional, not required for PASS.

No figure leak, no arithmetic-neighbor leak, no prompt/artifact-body leak. **No BLOCKER.**

---

## LENS 3 — Hardness end-to-end trace (all 5 levers preserved)

| Lever | Prompt sentence that surfaces it | Universe atom(s) the agent must touch | Status |
|---|---|---|---|
| L10 reversal/supersession | "dragging since May", "I'd bet some of it is stale by now", "confirm where each piece actually landed" | `receb057` selReady 5/1 vs `recf7aec` selProg 5/14 vs `rec651427` selProg 6/25 | PRESERVED |
| L2 structured-DB (Airtable-SoR) skip | "square up what we've got logged so it matches where the unit really is" | `team_001` (SoR decl) + `recac236210094352` MT-2026-1271 blank completion | PRESERVED |
| L1 latching | echoes chatter ("punch-list got knocked out and the carpet's in... on paper it looks about there") AND challenges it ("instead of going off what someone said in passing") | slack `140558...` + `21f0475...` + Brooke 5/29 "cleared and ready" | PRESERVED |
| L4 search-result-cap eviction | centers on "Las Palmas 8D" / "everything that was supposed to happen on that unit" | 61 "204B" vs 6 "Las Palmas 8D" occurrences (~10:1) | PRESERVED |
| L3 missing reply | "if something's still open, run down whatever it's waiting on and get it moving" | OPS-227 `comment_16a0a0c53f...` "parts approval before I swap it" | PRESERVED |

Mechanism independence intact (temporal / source-of-record / first-framing / result-eviction / search-for-response). No HARDNESS_REGRESSION. The prompt correctly does NOT name Airtable/Linear (keeps L2/L4) and does NOT name the disposal (keeps L1/L3).

---

## LENS 4 — Strict density projection (V4 per-model)

Strictest reading (minimizes inferred exploration), per model:
- Discovery: resolve "John" (dedupe Castillo) 1-2; read #make-ready 1-2; search "8D" across channels/threads incl. #maintenance 2-3; broad Las Palmas/make-ready Airtable query (204B swarm) -> refine to 8D 2-4; tblMaintenanceTickets -> MT-2026-1271 1-2; three 8D make-ready rows 2-3; Linear OPS-227 + comments 2-3; team/SoR 1; calendar 6/25 swap 1-2; Rio Bend 214 twin de-conflict 1; gmail scan 1-2. Subtotal ~16-22.
- Writes + re-verify: Airtable update 1-2; Linear comment on OPS-227 1-2; Slack #make-ready post 1; Gmail draft to John 1; re-query buffer under decoy pressure. Subtotal ~5-7.

**Independent midpoint ~= 46/model (range 40-52).** Shaded marginally below Council B (47) / Hardness (48.5) for the C001 corroboration trimming a few discovery calls — still comfortably >= 40. The irreducible 4-write workflow (4 services) floors density even on the leak-shortcut path. **Band: PASS** (V4 design target 40+, floor 15), applied to Opus 4.8 and Gemini separately. NOT THIN, NOT INSUFFICIENT.

---

## LENS 5 — Adversarial veteran review

- **Framing preserved across the intended artifact set:** the prompt sets up "verify true state -> advance open item -> reconcile records -> report" — no "execute on a stated figure" vs "flag a discrepancy" contradiction to seed downstream. Clean.
- **Recipient / entity drift:** "John" -> john.smith@starpm.com uniquely-in-context; external John Castillo (gmail, Water Delivery Rep) is an implausible make-ready-status recipient; James himself routes the disposal to "@john.smith". No drift seam.
- **Single-channel lock-in:** prompt names goals ("post an update in the make-ready channel" is a legitimate crew-broadcast target, not a lock-in that a valid alternative would fail; "draft John an email" is the persona's chosen medium and matches draft-only Gmail). No R9 lock-in defect.
- **Phrasing:** em/en/figure-dash/minus/horizontal-bar = 0; smart quotes = 0; non-ASCII = 0; double-hyphen = 0; "at least N" = 0; internal IDs (MT-/OPS-/rec/fld/tbl/sel/C0xx/p_006/team_001/204b) = 0; tool/param tokens = 0. Word count 233 <= 500.
- **"approximately"/"(or similar)" near exact values:** none.

No adversarial re-read flips a write action, a recipient, or the final state.

---

## LENS 6 — RETIRED (folded into Lens 1 per-atom + narrative-state).

## LENS 7 — Anti-rationalization check

Re-scanned reasoning for "I considered flagging X but decided it is fine" lines. One candidate: the Lens-2 corroboration leak. It is NOT talked away — it is LOGGED as a finding and routed to S2/S3 with four explicit hard-exclusions (figure-specific blocker mechanism does not apply to a qualitative status; universe-resident hence out-of-scope for a prompt fix; not in the prompt-directed channel; does not defeat the stump). Disposition = non-blocking advisory, not silent dismissal. No other findings suppressed. Belief-preservation "about there" + hedged "stale" examined and cleared as persona belief, not pre-solving (no record/ticket/disposal named).

## LENS 8 — Regression-anchor verification

`python3 Validators/test_regression_anchors.py` -> **62 passed, 0 failed out of 62** (incl. StarPM SP-9, SP-INJ-1/2/3, SP-SUB-1/2). Validator integrity confirmed; no silent regression.

## LENS 9 — RETIRED (UGT middle-band folded into Lens 1 + Lens 5 two-reading test; single end-state confirmed).

---

## Business Function — source verification (Lens 1 #12 backing)

`StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md`:
- L76: "James Bennett | Assistant Maintenance Technician | 4 Maintenance & Repairs" (home BF).
- L84: James Bennett = design-surface (0 scripted actions) -> author from role shape.
- L400 (Cat 4.1 worked example): "Carlos just moved a garbage-disposal ticket into my queue from a tenant at Unit 8D at Las Palmas... if it turns out the disposal needs replacement instead of repair, I'll handle the parts order..." -> the 8D disposal-replacement flip IS the canonical Cat 4 example.
- L528 (persona-anchor rule): "An Onsite PM authoring a maintenance task is a Category 1 prompt; a Lead Maintenance persona authoring the same shape is a Category 4 prompt." The make-ready SETTING (Cat 1 turnover, Carlos primary) does NOT demote a maintenance persona's task; James -> Category 4. Match confirmed from source, not from Council A.

---

## Date-alignment deep-dive (validator 6/12 note reconciled)

The validator NOTE resolves "today" against 2026-06-12 — the stale QC-spec fallback triggered because `_aux/Fact_Ledger.json` lifecycle.today is null (S0 artifact). The AUTHORITATIVE today is 2026-07-01 (today_horizon.json + the V4 fixed date). The 6/12 value never reaches the agent (the platform fixes 7/1). Robustness check: even under 6/12, the core end-state holds — MT-2026-1271 was created 2026-05-01 with blank completion, so 8D is OPEN under either date. All relative phrases resolve cleanly with in-window data at 7/1. **Prompt date-alignment = 5/5; the null Fact_Ledger is an S0 fix (before S2/S3), zero prompt impact.**

## Known advisories reconciled (pre-authorized, not re-raised as prompt blockers)
1. Fact_Ledger.json lifecycle.today null -> S0 artifact; confirmed zero prompt impact; must fix before S2/S3 (A3 narrative-state consumes it). Not a prompt blocker.
2. S0_Setup_Report injection claim inaccurate (comment-only stub; changelog []) -> already caught by HARDNESS; zero prompt impact. Not a prompt blocker.

---

## VERDICT: PASS (STRICT)

All 14 applicable sub-dims genuinely earn 5/5 under the strictest reading; density ~46/model (>= 40 V4 bar, per model); all 5 levers (L10/L2/L1/L4/L3) trace end-to-end with cited evidence; zero phrasing/leak/pre-solving hits in the prompt; unique ground truth intact (8D NOT ready); regression anchors 62/62; validator exit 0 during audit. The single net-new finding (James's 6/22 #maintenance corroboration of "8D still open") is universe-resident, out-of-scope for a prompt fix, absent from the prompt-directed channel, and does not defeat the stump -> logged as a NON-BLOCKING S2/S3 design advisory, not a prompt defect. The prompt does not telegraph the trap and preserves James's belief that 8D is "about there".

```json
{
  "phase": "prompt",
  "council": "AUDIT",
  "mode": "auto_fire",
  "task_dir": "Tasks/39_6a602c8886ebb06f12354d77",
  "universe": "starpm",
  "deliverable": "Tasks/39_6a602c8886ebb06f12354d77/5_Prompt.txt",
  "verdict": "PASS_STRICT",
  "blockers": [],
  "sub_dim_scores": {
    "Unique Ground Truth": "5/5",
    "Feasibility": "5/5",
    "Explicit Tool Mention": "5/5",
    "Clarity & Specificity": "5/5",
    "Contrived / Unnatural": "5/5",
    "Alignment with Today's Date": "5/5",
    "Truthfulness": "5/5",
    "Tool Use & Cross-service": "5/5",
    "Investigation + Action": "5/5",
    "Coherence (Bolt-on)": "5/5",
    "Persona": "5/5",
    "Business Function": "5/5",
    "Universe Data Exists": "5/5",
    "Universe Cross-service Coherence": "5/5"
  },
  "lenses": {
    "L1_strict_qc": "PASS (all 14 sub-dims = 5)",
    "L2_answer_leakage": "PASS (no figure/artifact/prompt-directed-channel leak; 1 universe-resident corroboration routed to S2/S3 as non-blocking advisory)",
    "L3_hardness_end_to_end": "PASS (5/5 levers preserved with cited atoms)",
    "L4_strict_density": "PASS (~46/model, >=40 V4 per-model bar)",
    "L5_adversarial": "PASS (no write/recipient/state flip)",
    "L7_anti_rationalization": "PASS (leak logged + routed, not dismissed)",
    "L8_regression_anchors": "62/62 PASS",
    "L9_unique_ground_truth": "PASS (single end-state: 8D NOT ready)"
  },
  "density": {
    "per_model_midpoint": 46,
    "range": "40-52",
    "band": "PASS",
    "bar": "starpm_v4_per_model",
    "design_target": 40,
    "floor": 15,
    "applied_separately_to": ["opus_4.8", "gemini"]
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
    "non_ascii": 0,
    "at_least_n": 0,
    "pre_solving": false,
    "telegraphs_trap": false,
    "word_count": 233
  },
  "unique_ground_truth": {
    "single_end_state": true,
    "end_state": "8D NOT ready: disposal replacement + parts approval outstanding, MT-2026-1271 OPEN, fridge-swap turn still selProg at 2026-07-01",
    "report_ready_is_failure_path": true,
    "flips_write_or_recipient_or_state": false
  },
  "non_blocking_advisories": [
    {"scope": "S2/S3", "type": "answer_corroboration_leak", "detail": "James's own 6/22 #maintenance (C001) messages state '8D ... still open (parts approval)'. Universe-resident, not in the prompt-directed #make-ready channel, does not defeat the stump. Require synthesis+write workflow for full credit; optional authority-injection re-hardens.", "blocks_prompt": false},
    {"scope": "S0", "type": "fact_ledger_today_null", "detail": "_aux/Fact_Ledger.json lifecycle.today null -> validator falls back to 6/12; authoritative today 2026-07-01. Zero prompt impact; fix before S2/S3.", "blocks_prompt": false},
    {"scope": "S0", "type": "s0_report_injection_claim_inaccurate", "detail": "S0_Setup_Report claims injection PASS but inject file is comment-only stub / changelog []. Already caught by HARDNESS; zero prompt impact.", "blocks_prompt": false}
  ],
  "validator_exit_0": true,
  "regression_anchors": "62/62",
  "iteration": 1,
  "timestamp": "2026-07-22T16:50:00-05:00"
}
```
