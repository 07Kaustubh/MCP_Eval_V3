# PIPELINE AUDIT — `--phase all` (on-demand, veteran QC second-opinion)

**Task:** Tasks/39_6a602c8886ebb06f12354d77 · **Universe:** starpm (V4, confirmed `_aux/Universe.txt` = `starpm`)
**Scenario:** Las Palmas 8D make-ready turn closeout · **Persona:** James Bennett (p_006, Assistant Maintenance Technician)
**Artifacts audited:** `5_Prompt.txt` (233w) · `6_Oracle_Events.txt` (12 OEs) · `7_Rubrics.json` (15 rubrics, all Outcome)
**Mode:** On-demand fresh-chat re-verification under the STRICTEST interpretation (5/5-only; every "should"="must"; every soft convention binding; every WARN/NOTE listed). Read-only — no deliverable modified.
**Date:** 2026-07-23

## VERDICT: PASS (STRICT) on the deliverables. + one PIPELINE-TOOLING REVISE (non-blocking for this task; does NOT change the ship decision).

- All 24 QC sub-dims score **5/5** under strictest interpretation (0 sub-dim < 5).
- 0 BLOCKER. Answer-leakage clean. All 5 hardness levers trace end-to-end. Decoys quarantined. Gmail draft-only honored. No em-dash / "at least N" / tool-name-in-title / entity-drift.
- Difficulty PASS (pass@1 = 0/6 both models). Density on TRUE numbers clears the floor on both models (Opus 43.5 PASS-target; Gemini 33.0 THIN-of-40-target but >> 15 floor and >= 15 QC-spec pass line).
- The corrupt `Trajectory_Stats.json` (Gemini recorded as 0 tool calls) and the validator's stale-6/12 date fallback are **pipeline evidence/tooling artifacts, already documented in S4_verdict.md**, NOT deliverable defects. The task is **SHIPPABLE on true numbers.**

---

## Data sources consulted (re-verified FIRST-HAND from source — not trusting prior-phase outputs)

- `_aux/Universe_Split/airtable.airtable_records.json` (170 rows) — parsed the stringified `row_data` and dumped full `fields` for all 5 target records.
- `_aux/Universe_Split/slack.slack_messages.json` (580 msgs) — full C001 + C004 chronological read; 8D/disposal grep.
- `_aux/Universe_Split/linear.linear_comments.json` (48) + `linear.linear_issues.json` (230) + `linear.linear_teams.json` (1) — OPS-227 comment/issue/team.
- `_aux/Universe_Split/contacts.contacts.json` — john.smith.
- `_aux/Fact_Ledger.json` — atom counts (entities:0, fiscal_periods:0 confirm no GL trap) + id presence.
- `_aux/Universe_Index/today_horizon.json` — universe_today 2026-07-01 America/Chicago.
- Tool catalog `StarPM_Base_Universe/7_Server_Tools_Details.json` — extracted param schemas for all 16 tools the OE uses.
- Empirical: `_aux/Trajectory_Stats.json` (recorded) + hand-recompute of Gemini flat-schema density; `_aux/Council_Reports/S4_verdict.md`, `S4_bucket3.md`; `8a_/8b_` digested via S4.
- Prior councils re-read: `FINAL_council.md`, `AUDIT_prompt.md`, `AUDIT_oe.md`, `AUDIT_rubrics.md`, `S3_reconfirm.md`, `Linter_Decision.md`, `Validator_Reports/*`.
- QC spec `Docs_starpm/7_QC_Spec_Doc1.json` (5 dims / 24 sub-dims) — full read.
- Tooling: `Validators/parse_trajectories.py:130-149` read to confirm the parser defect first-hand.

---

## PER-ATOM EVIDENCE TABLE (Lens 1 — mandatory for every Truthfulness / Accuracy 5/5)

Every atom re-queried directly from `_aux/Universe_Split/`. Airtable rows: record id lives inside the stringified `row_data.fields`.

| Atom asserted (deliverable) | Universe query | Row excerpt (verbatim) | Verdict |
|---|---|---|---|
| receb057b02f20052 = 8D, STALE "ready/closed out", 2026-05-01 | airtable_records `id=receb057b02f20052` (tblMakeReady) | `fldUnit:"Las Palmas 8D"`, `fldTurnStatus:"selReady"`, `fldTargetReady:"2026-05-01"`, `fldNotes2:"Turn closed out as of today... cleared for leasing - available to show immediately."`, created 2026-05-01 | **PASS** |
| recf7aecc318b2252 = 8D, in-progress, John Smith + James in-house | airtable `id=recf7aecc318b2252` (tblMakeReady) | `fldUnit:"Las Palmas 8D"`, `fldTurnStatus:"selProg"`, `fldNotes2:"John Smith and James Bennett are three days into the in-house make-ready work..."`, created 2026-05-14 | **PASS** |
| rec651427ec0d84dd5a = 8D, live, fridge swap 6/25, target 6/26, "critical path" | airtable `id=rec651427ec0d84dd5a` (tblMakeReady) | `fldUnit:"Las Palmas 8D"`, `fldTurnStatus:"selProg"`, `fldMoveOut:"2026-06-18"`, `fldTargetReady:"2026-06-26"`, `fldNotes2:"Refrigerator swap scheduled Thu 6/25... 8D confirmed as the critical path... replacement delivered and installed in the morning window."` | **PASS** |
| recac236210094352 = MT-2026-1271, OPEN (blank completion), high | airtable `id=recac236210094352` (tblMaintenanceTickets) | `fldTicketNumber:"MT-2026-1271"`, `fldPriority:"selHigh"`, `fldCompletionDate:""` (BLANK), `fldDescription:"...carpet has visible staining... kitchen faucet is dripping... walls show scuff marks..."` | **PASS (open confirmed)** |
| recb403fe04c2f97683 = MT-2026-1325, Rio Bend 214 (DIFFERENT unit), dishwasher, done 6/25 | airtable `id=recb403fe04c2f97683` (tblMaintenanceTickets) | `fldTicketNumber:"MT-2026-1325"`, `fldPriority:"selMedium"`, `fldCompletionDate:"2026-06-25"`, `fldDescription:"Dishwasher pull-and-replace at Rio Bend 214..."` | **PASS (genuine decoy, different unit)** |
| OPS-227 comment: seized / full replacement / routed for parts approval / no reply | linear_comments `id=comment_16a0a0c53f543a1221f08de6a786cb66` | `body:"The 8D disposal is seized, not just jammed... needs a full unit replacement, not a repair. Routing back to you for parts approval before I swap it. — James"`, `issue_id:"OPS-227"`, author=James, `created_at:"2026-06-22T11:00:00-05:00"`; **only 1 comment on OPS-227** (no reply) | **PASS (no-reply confirmed)** |
| OPS-227 issue: 8D disposal, team_001, assignee James, still open | linear_issues `id=OPS-227` | `title:"Clear garbage disposal jam — Las Palmas 8D"`, `team_id:"team_001"`, `assignee_id=user_8cd13ca9...(James)`, `completed_at:null` | **PASS** |
| Airtable is System of Record; Linear secondary | linear_teams `id=team_001` | `"...Airtable Maintenance Tickets table, which is the system of record. Linear is secondary for maintenance items..."` | **PASS (SoR trap confirmed)** |
| john.smith@starpm.com = Lead Maintenance Technician (email recipient) | contacts `email=john.smith@starpm.com` | `job:"Lead Maintenance Technician"`, `first_name:"John"`, `last_name:"Smith"` | **PASS** |
| C001 6/22 load-bearing signal (James) | slack_messages C001 | `1782144900 (James): "...8D disposal is seized — needs a full replacement unit, so I routed it to @john.smith for parts approval before I swap it."` + `1782145200 (James): "...8D disposal needs a replacement (waiting on parts approval from John), so that unit's still open."` | **PASS** |
| C004 May latching chatter ("officially cleared and ready") | slack_messages C004 | `1780067965 (John): "8D is officially cleared and ready for leasing, go ahead and start scheduling showings!"` + carpet-done (5/23) + deep-clean + punch-list-done (5/27) | **PASS (stale anchor confirmed)** |
| Decoy swarm 204B vs 8D | airtable tblMakeReady unit counts | Las Palmas 204B = **53** make-ready rows vs Las Palmas 8D = **3** (~18:1) | **PASS (L4 eviction confirmed)** |

**No empty evidence cell → no forced ≤3.** Truthfulness (prompt) and OE Accuracy both cleared with cited proof.

---

## LENS 1 — Strict QC scoring (all 24 sub-dims of Docs_starpm/7_QC_Spec_Doc1.json)

Format: SUB-DIM → SCORE → REASON → WHAT PRIOR COUNCIL MISSED.

### Dimension: Prompt
1. **Unique Ground Truth → 5** — Exactly one correct end-state: 8D not-ready; keep MT-2026-1271 open; correct receb057 selReady→selProg + notes; advance OPS-227 for parts approval; post C004 not-ready; draft John. No two-valid-end-state fork (the 06/09 "file-now vs defer" pattern does not apply — marking the ticket complete is the designed TRAP, not a second valid answer). pass@1 0/6 with every rubric individually achievable = distributed difficulty, single GT. *Prior miss: none.*
2. **Feasibility → 5** — Fully actionable in one session; 4 writes all tool-supported; no conflicting/impossible request. *None.*
3. **Explicit Tool Mention → 5** — Zero tool/MCP names; "make-ready channel" is a business term. Validator prompt PASS. *None.*
4. **Prompt Clarity & Specificity → 5** — Four unambiguous asks; all reasonable readings converge on the same write set (no Action-Decision-Ambiguity). Which-record referent resolves via universe state (stale selReady row); R13/R14 OR-paths absorb alt reconciliations. *None.*
5. **Contrived / Unnatural → 5** — Cohesive natural situation (junior tech reconciles a dragging turn before reporting to his Lead); not a command-list; difficulty from scattered/conflicting data + decoys (spec-defined NATURAL). *None.*
6. **Truthfulness → 5** — Every prompt claim TRUE-but-stale and persona-believed ("punch-list got knocked out", "carpet's in", "on paper it looks about there"); grounded in C004 chatter + carpet/punch-list rows (see evidence table). No factual error, no false assertion. *None.*
7. **Tool use & Cross-service → 5** — Requires reconciliation across airtable + slack (C001/C004) + linear + gmail + contacts (5 services); facts scattered. *None.*
8. **Investigation → 5** — "figure out where 8D really stands... instead of going off what someone said in passing" — genuine self-initiated investigation; not pre-solved (no root cause named). L15/L16 implicit. *None.*
9. **Coherence → 5** — One situation; every ask ties to "get 8D genuinely closed / give John the straight story." Remove-a-sentence test: no bolt-ons. *None.*
10. **Persona → 5** — James (junior Assistant Maint Tech, Cat 4, formality 0.35). The disposal (OPS-227) is HIS OWN ticket (assignee); reconciling + reporting his own turn to his Lead is canonical junior work; voice matches. Linter Class-A challenge INVALIDATED with grounded counters (persona is a fixed input; nobody emails themselves). *Prior councils correctly held 5/5; linter false-positive.*
11. **Business Function → 5** — Cat 4 Maintenance & Repairs; investigate/advance a maintenance ticket + correct the log + report to Lead is squarely Maintenance. Linter "belongs to Property Ops" is factually wrong (James authors, John receives). *None.*
12. **Alignment with Today's Date → 5** — Under authoritative today 2026-07-01 (today_horizon.json), all events correctly past (6/22 disposal, 6/25 fridge, May chatter); "closed out today" = 7/01. No contradiction. *Prior miss (minor, pipeline-hygiene, does not drop score): the QC-JSON stale "Jun 12" string + validator 6/12 fallback are artifacts; evals + Docs_starpm/6 fix today at 7/01 — see Pipeline-Hygiene section.*

### Dimension: Universe
13. **Universe Feasibility (Data Exists) → 5** — All core facts exist + retrievable (verified first-hand). Base data suffices; no injection. *None.*
14. **Cross-service Coherence → 5** — No incoherent edits (inject = comment-only stub; changelog []; base unedited). The stale-vs-live contradiction is DESIGNED and RESOLVABLE (selReady superseded by later selProg + 6/22 disposal + SoR) — sufficient supporting evidence for the single "not ready" truth, so per the spec's own note it is NOT a failing "misaligned data" incoherence; the rubric is written to the well-supported truth. *None.*

### Dimension: Oracle Event
15. **OE Completeness → 5** — 12 OEs cover discovery (OE1-7) + pre-write dependency (OE10) + all 4 writes (OE8/9/11/12). No missing critical step; no reasoning-only OE (OE7 synthesis rides a real `list_comments` call). *None.*
16. **OE Accuracy → 5** — Every tool/service/param/expected-datum matches the universe (per-atom table) AND every param trap correct: `search_records`→`table`; `list/update_records_for_table`→`tableId`+`records`; `slack_send_message`→`message` (not payload); `create_draft`→`body` + draft-only (no send tool exists); `save_comment`→`issueId`+`body`; `list_issues`→`team` (not teamId). Following the OEs literally yields a correct trajectory. *None.*

### Dimension: Rubric
17. **Overall Rubric Quality → 5** — Validator rubrics PASS 0/0; 0/15 criteria with any issue. 15 atomic Outcome rubrics, all grounded first-hand. R6 AND-phrasing and R14 "make-ready ticket" descriptor scrutinized and EXCLUDED as non-issues (see Lens 5 + Lens 7). *Prior miss: none — the two half-applied evidence tweaks (R4/R11) that AUDIT_rubrics caught are confirmed fixed byte-exact in the live file.*
18. **All-Failing Rubrics → 5** — Exactly one AF rubric (Gemini R6, 6/6). It is Bucket 3 (valid): grounded in "crew isn't working off old info" (old info = "start scheduling showings"), achievable (Opus issues the walk-back 6/6), within scope, real tools; AF justification (S4_AF, voice-gate clean) confirms a genuine Gemini gap (Learnings L31). Bucket-1 ratio 0/11 = 0% → 5/5. *None.*
19. **Rubric Category Balance → 5** — 15 Outcome > 0 Process; not process-heavy; not zero-outcome. *None.*
20. **Process Rubrics → 5** — Zero process rubrics → nothing fails the 3-condition test → automatic 5/5. R12-R15 ("identifies/reports…") are final-response-content OUTCOMES, not disguised process. *None.*
21. **Agent-Centric Phrasing → 5** — All 15 titles = "The Agent" + action + context; zero tool names in titles. Validator PASS. *None.*

### Dimension: Trajectory (Agent Run)
22. **Tool Call Count → 5** — QC-spec fail-line is avg **< 15**. Opus 43.5, Gemini 33.0 (true), combined 21.8 — all ≥ 15 → PASS. (The recorded Gemini 0 is a parser artifact; the 40-target THIN band is a project construct, handled in Lens 4, not a QC-spec sub-dim downgrade.) *Prior miss: the stored artifact is wrong for Gemini — see parser finding; does not change this sub-dim's PASS.*
23. **Agent Failure Rate → 5** — pass@1 = 0/6 both models (0.0% << 40%). 0-2 of 6 pass → PASS; every rubric individually achievable → genuine difficulty. *None.*
24. **Error Rate → 5** — 0/6 errored runs both models (all 12 completed to verifier-evaluable state). < 3 → PASS. *None.*

**Lens 1 result: 24/24 sub-dims = 5/5. Zero sub-dim < 5. PASS.**

---

## LENS 2 — Answer-leakage sweep — PASS

- **Derived conclusion:** 8D not ready; sole blocker = seized kitchen garbage disposal awaiting parts approval; everything else (in-house repairs, carpet, deep clean, punch-list, 6/25 fridge) done.
- **Prompt does NOT pre-solve:** `5_Prompt.txt` carries only the stale frame ("punch-list got knocked out and the carpet's in... on paper it looks about there"); no mention of disposal / seized / replacement / approval / not-ready. Implicit (L15/L16). ✔
- **Regex sweep across slack + linear comments + linear issue descriptions + airtable notes + gmail** for "not ready to close / sole blocker / only blocker / everything else is done / cannot close" → **0 hits.** No single artifact states the full conclusion verbatim. ✔
- **Partial-signal (logged, hard-excluded, NOT a BLOCKER):** the 6/22 C001 message "8D disposal needs a replacement (waiting on parts approval from John), so that unit's still open" gives 3 of 4 conclusion elements (blocker + awaiting-approval + unit-open) in one message. HARD EXCLUSIONS: (1) it does NOT establish the SOLE-blocker / everything-else-done element (requires synthesizing C004 completion chatter + fridge row); (2) it must be TRUSTED over 3+ louder contradicting "ready" signals (selReady row + "officially cleared and ready" C004 + carpet/punch-list-done) — the L10 supersession decision the task is built on; (3) it is buried under 61 "204B" decoy occurrences (L4); (4) EMPIRICAL: 0/6 both models — a fatal leak would produce passes; instead every run failed. It is the intended, buried, contradicted discovery target, not a correction-email answer-statement (L6). Already flagged + routed by AUDIT_prompt (non-blocking advisory) + AUDIT_oe (F5) — I converge.
- No figure/arithmetic-neighbor leak (task is not numeric-derived).

**No single agent-readable source states the FULL conclusion without cross-source synthesis. No BLOCKER.**

---

## LENS 3 — Hardness end-to-end trace (5 selected levers) — PASS

| Lever (Hardness_Plan) | Prompt sentence | OE step | Rubric criterion | Fact_Ledger / Universe atom |
|---|---|---|---|---|
| **L10 Reversal / supersession** | "this turn has been dragging since May and a bunch of people have had a hand in it" | OE2 (receb057 5/1 selReady vs recf7 5/14 + rec651 6/25 selProg) | R2/R3 (flip receb057 selReady→selProg), R12 | receb057b02f20052 (5/1 selReady) superseded by recf7aecc318b2252 + rec651427ec0d84dd5a |
| **L2 Structured-DB (Airtable) SoR skip** | "confirm where each piece actually landed instead of going off what someone said in passing" | OE3 (MT-2026-1271 blank completion) + OE6 (team_001 SoR charter) | R14 (turn incomplete in Airtable SoR, MT-2026-1271 open) | recac236210094352 (blank fldCompletionDate) + linear_teams team_001 |
| **L1 Latching (first-framing)** | "the punch-list got knocked out and the carpet's in, so on paper it looks about there" | OE4 (C004 May "cleared and ready" chatter) | R12 (not ready despite logged status + earlier channel messages) | slack C004 1780067965 "officially cleared and ready" + carpet/punch-list-done |
| **L4 Search-result-cap eviction** | (implicit — "Las Palmas 8D" buried among 204B) | OE2/OE3 (isolate the 3 8D rows) | R2/R3/R4 + R14 (must hit the exact 8D records) | 53 "Las Palmas 204B" make-ready rows vs 3 "8D" (~18:1) |
| **L3 Missing reply** | "run down whatever it's waiting on and get it moving" | OE5/OE7 (disposal reply + OPS-227 comment, no answer) | R1 (advance for parts approval), R13 | comment_16a0a0c53f... (routed for approval) — 0 reply comments on OPS-227 |

All 5 levers have a prompt sentence + OE step + rubric criterion + grounded atom. **No HARDNESS_REGRESSION.** (Empirically all 4 stump mechanisms fired per S4 calibration, 3/4 on a different surface than predicted; distributed 0% pass@1.)

---

## LENS 4 — Strict density (V4 per-model; NOT the V3 50/40 scheme) — Opus PASS / Gemini THIN-of-target; net SHIPPABLE

Using the REAL trajectories (not re-projected). StarPM bar: design target avg 40+, absolute floor 15, applied PER MODEL.

| Model | Per-run totals | Avg | vs 40 target | vs 15 floor | Verdict |
|---|---|---:|---|---|---|
| Opus 4.8 | 46, 52, 46, 46, 45, 26 | **43.5** | ≥ 40 | ≫ 15 | **PASS** |
| Gemini | 33, 37, 28, 31, 36, 33 | **33.0** | THIN (< 40) | ≫ 15 | **PASS (floor); THIN vs target** |

- Gemini's true 33.0 was hand-recomputed by counting flat `type=="tool_use"` events (the recorded 0 is the parser artifact). Both models clear the 15 floor and the QC-spec pass line by a wide margin; neither triggers a REDO (REDO trigger is avg < 40 per REDO.md, and even the lower Gemini figure with 0% pass@1 is above floor + at max difficulty).
- **Does Gemini-THIN + corrupt-stats warrant a DELIVERABLE REVISE? NO.** (1) The deliverables are model-agnostic; the density delta is emergent Gemini behavior (fewer calls/run on the same asks), not fixable by editing the prompt without risking Opus over-inflation or answer-leakage. (2) The task already forces 4 writes across 4 services + heavy decoy-defeating discovery. (3) pass@1 = 0/6 on Gemini means THIN density is NOT producing an easy task. (4) The corrupt stat is an evidence artifact already documented in S4 with a fix recommendation; true numbers clear everything. → Record Gemini-THIN as a NOTED observation with the per-model-spread lesson (already logged to S4); NOT a deliverable REVISE.

---

## LENS 5 — Adversarial veteran review — PASS

- **Implicit-prompt framing preserved across all 3 artifacts.** Prompt names GOALS ("get it moving so it can genuinely close", "square up what we've got logged", "post an update", "draft John an email"); no artifact demands a "flag the discrepancy" step the prompt didn't authorize. ✔
- **Method-lock audit (Lens 7-grade):**
  - R1 is GOAL-phrased (OPS-227 comment OR Slack OR email to John) — correctly NOT channel-locked. ✔
  - R2-R4 pin record **receb057b02f20052** — VALID, not over-fit: it is the ONLY selReady / 2026-05-01 / "cleared for leasing" row; the other two 8D rows are already selProg. There is no alternative-record reconciliation an agent could pick that both corrects the stale "ready" signal AND would be wrongly failed — correcting readiness REQUIRES touching the one row that still asserts it. (Gemini's 5/6 failures updated the already-selProg June row and left the selReady row asserting "available to show immediately" — a genuine miss, not a rubric over-lock.) R14 additionally carries an OR-path (MT-2026-1271 open OR record still selProg). ✔
  - R5-R7 (C004) + R8-R11 (john.smith@starpm.com) are PROMPT-SOURCED ("Post an update in the make-ready channel"; "draft John an email"), not rubric-invented lock-in. ✔
- **Entity-drift seams:** none — John (Lead, john.smith@starpm.com) un-drifted vs decoy john.castillo@gmail.com; James assignee; OPS-227 / MT-2026-1271 / receb057 coherent; Rio Bend 214 / MT-2026-1325 quarantined (0 rubric targets). ✔
- **Silent process rubrics disguised as outcomes:** none — 0 process rubrics; R12-R15 are conclusion-correctness outcomes (three-condition test N/A, no process present). ✔
- **Format drift:** em-dash 0 / en-dash 0 / "at least N" 0 / no tool names in titles or prompt / no "approximately"/"(or similar)" near ids-dates / no OE meta-tags in prompt (verified: em-dashes appear ONLY in universe data rows — OPS-227 title/comment, recb403 description — NOT in any deliverable; validator prompt/oe/rubrics all PASS confirm). ✔
- **StarPM landmines:** near-duplicate-file decoy (report-laspalmas-8d-qc-inspection.pdf vs -2) is **N/A** — StarPM here has no filesystem service and no such file rows (confirmed: airtable is the make-ready SoR). Cross-property Unit-14 ambiguity not in play. The active near-miss (Rio Bend 214 / same-Thursday 6/25 swap; also a 9D "disposal swap done" May message) is correctly quarantined. ✔
- **Gmail draft-only honored:** OE12 + R8 use `create_draft` (body, draft-only); no send tool exists in the catalog; rubric checks a draft, not a sent email. ✔
- **Scrutinized-but-excluded (promoted honestly):** R6 "not ready AND should not be marketed or shown" — the FINAL council's own MINOR AND-bundle flag, and the exact seam that became Gemini's sole 6/6 all-fail. Assessed VALID: the two clauses are semantically fused (the stale C004 message it corrects literally said "go ahead and start scheduling showings", so retracting readiness in that channel entails "don't show"), and Opus satisfies BOTH in one natural sentence 6/6 → not over-specified, does not fail a valid path. A judge over-penalizing a correct not-ready-but-no-explicit-"market" post = Bucket-2 judge error, not a rubric defect. OPTIONAL (non-blocking) refinement only: splitting into R6a "not ready" / R6b "should not be shown/marketed" would give cleaner per-clause attribution — a nice-to-have, NOT a correctness fix.

---

## LENS 6 — RETIRED (v18). Not executed (folded into Lens 1 per-atom evidence table).

---

## LENS 7 — Anti-Rationalization ledger

Every considered-and-excluded item, each with a HARD exclusion (empirical/structural, not "the agent probably meant"):

1. **C001 6/22 "still open" partial-signal** — Considered as a Lens-2 leak. HARD EXCLUSION: does not state the FULL conclusion (no sole-blocker/everything-done; must be trusted over 3+ louder contradicting ready signals; buried under 204B; 0/6 empirical). Logged, not dismissed.
2. **R6 AND-bundle** — Considered as an atomicity/over-specification REVISE. HARD EXCLUSION: clauses semantically fused + Opus 6/6 joint achievability proves it fails no valid path; the Gemini all-fail is a documented Bucket-3 model gap (L31). Logged as scrutinized + optional-only refinement.
3. **R14 "make-ready ticket MT-2026-1271" descriptor** — Considered as a Truthfulness/Accuracy loosening (MT-2026-1271 lives in tblMaintenanceTickets). HARD EXCLUSION: the ID is EXACT and unambiguously grounds to recac236; MT-2026-1271 is literally the ticket that opened the 8D make-ready turn ("Make-Ready Turn record created" in its own description), so "the make-ready ticket" is a defensible functional descriptor; caused ZERO fails (R14 fails were backfilled-completion-date / derived-from-Linear, not label confusion). Non-issue.
4. **R14 OR-branch (selProg equivalent)** — Considered as weakening L2. HARD EXCLUSION: both tblMakeReady and tblMaintenanceTickets ARE the structured Airtable DB, so either branch still forces Airtable-over-Slack/Linear-chatter (the exact L2 mechanism); primary branch (MT-1271 blank) present + clean. Not a REVISE.
5. **#make-ready crew-post by a junior** — Considered as a Persona over-scope (John usually posts daily updates). HARD EXCLUSION: James is named in-house crew on THIS turn (recf7aecc318b2252); a crew member posting a factual stale-info correction is realistic and prompt-mandated; linter false-positive already INVALIDATED with grounding. Not a defect.
6. **Density lean-floor ~14** — Considered as an INSUFFICIENT-density risk. HARD EXCLUSION: the V4 gate is the realistic average of ACTUAL runs (Opus 43.5 / Gemini 33.0), not a perfect-agent floor; a sub-15 run only happens by skipping mandated verification (not a correct solve). THIN watch-item, not a blocker.

**Anti-rationalization output check:** re-scanned my reasoning for "I considered flagging X but decided it's fine because…" — every such line above carries a hard empirical/structural exclusion, not a likelihood hand-wave. No item improperly rationalized away. Clean.

---

## LENS 8 — Regression anchors + tooling-integrity — PASS (62/62) + one LOW tooling finding

- **`Validators/test_regression_anchors.py` = 62/62 PASS** (per orchestrator run; consistent with all 5 validators exit 0 this pass).
- **Tooling-integrity finding (the class Lens 8 exists to catch): `parse_trajectories.py` Gemini-schema blindspot.** A density counter that silently returns 0 for an entire model is the same silent-regression class. Severity **LOW** for THIS task because: (a) it is NOT silent here — S4_verdict.md explicitly surfaced it, hand-recomputed Gemini (33.0), and recommended the patch; (b) the corrupt figure did not flip any verdict (Opus 43.5 drives the density PASS; combined 21.8 clears `density_ok_at_15`). Severity would be HIGH on a future V4 task where Gemini is the ONLY model clearing the floor (would emit a FALSE `REBUILD_CANDIDATE_DENSITY`). Fix location below.

---

## LENS 9 — RETIRED (v18). Not executed (folded into Lens 1 + Lens 5).

---

## PARSER-BUG FINDING (pipeline tooling — exact fix location)

**File:** `Validators/parse_trajectories.py` · **Function:** `count_tool_calls(events)` · **Lines 130-149.**

Root cause (read first-hand):
- L138-140: `msg = ev.get("message"); if not isinstance(msg, dict): continue` — any event lacking a `message` wrapper is SKIPPED. Gemini trajectories use FLAT top-level events `{"type":"tool_use","tool_name":...,"parameters":...}` with no `message` wrapper → every Gemini tool call is skipped → returns (0, 0).
- L145: only counts `block["type"]=="tool_use"` nested in `message.content[]` (the Opus/Claude schema; docstring L26 hardcodes this assumption).
- L147: MCP detection uses `block.get("name","").startswith("mcp__")` — blind to Gemini's `tool_name` field and `mcp_mcp<hash>_` prefix.

**Exact fix:** in `count_tool_calls`, add a branch that also counts top-level events where `ev.get("type")=="tool_use"` (reading the tool name from `tool_name`), and broaden MCP detection to match both `name`/`tool_name` and both `mcp__`/`mcp_mcp` prefixes. Then regenerate `_aux/Trajectory_Stats.json` so `by_model.gemini.avg_tool_calls_total` records 33.0 rather than 0.

**Classification:** REVISE-the-PIPELINE-TOOLING (shared, regression-pinned validator — out of this task's deliverable scope). It is **REVISE-the-evidence**, NOT ship-gating: the true numbers (Opus 43.5, Gemini 33.0) clear the floor and difficulty, so **the task itself remains shippable**. Already logged in S4_verdict.md as a follow-up.

---

## Pipeline-hygiene findings (non-deliverable, non-ship-gating)

- **[LOW] Corrupt `_aux/Trajectory_Stats.json`** — records Gemini `tool_calls_total: 0` for all 6 runs + `by_model.gemini.avg_tool_calls_total: 0`. Consequence of the parser bug above. Regenerate after the fix. Does not change the shipped `verdict: OK` (correct on true numbers).
- **[LOW] Stale-date validator fallback** — `Validator_Reports/prompt.md` resolves `today` against `2026-06-12` because `_aux/Fact_Ledger.json` `lifecycle.today` is null → validator defaults to a stale constant. Authoritative today is **2026-07-01** (today_horizon.json + evals + Docs_starpm/6). Zero deliverable impact — under 7/01 the task is fully date-coherent (all events past). Already flagged by AUDIT_prompt + Linter carry-forward #1. Fix: seed `Fact_Ledger.lifecycle.today` = 2026-07-01 (rebuild `build_fact_ledger.py`).
- **[NOTE] `S0_Setup_Report.md` injection claim** — claims `9_Universe_inject.sql` "present with executable statements (73 lines)" + injection PASS, but the file is a comment-only stub / `4_Changelog.json` = `[]`. Already caught by HARDNESS; scenario is baked into base data; zero downstream impact.

---

## All 9 lenses status
- Lens 1 strict QC scoring :: **PASS** (24/24 sub-dims 5/5)
- Lens 2 answer-leakage sweep :: **PASS** (no full-conclusion single-source; partial-signal hard-excluded + 0/6)
- Lens 3 hardness end-to-end :: **PASS** (5/5 levers trace)
- Lens 4 strict density :: **Opus PASS / Gemini THIN-of-40-target** (both ≫ 15 floor; net shippable, not a deliverable REVISE)
- Lens 5 adversarial review :: **PASS**
- Lens 6 :: RETIRED (v18)
- Lens 7 anti-rationalization :: **PASS** (ledger clean, hard exclusions cited)
- Lens 8 regression anchors :: **62/62 PASS** + LOW tooling finding (parser bug, documented/non-silent)
- Lens 9 :: RETIRED (v18)

## Verification statements
- [x] All 5 validators re-confirmed exit 0 (prompt/oe/rubrics/injection/submission_gate PASS 0/0).
- [x] Regression-anchor suite 62/62 PASS.
- [x] Anti-rationalization output check passed; no un-excluded "decided it's fine because…" line.
- [x] Per-atom evidence table produced; no empty cell → no forced ≤3.
- [x] Verdict recorded with explicit per-issue trail (below).

---

## Final verdict — per-issue trail

**PASS (STRICT)** on the deliverables (`5_Prompt.txt` / `6_Oracle_Events.txt` / `7_Rubrics.json`). Zero BLOCKER; zero Lens-1 sub-dim < 5; every lever traces end-to-end; density clears the floor + difficulty on both models on true numbers.

Non-deliverable items (do NOT gate this task's ship; carry forward as pipeline work):

| Severity | Issue | Location | Fix |
|---|---|---|---|
| REVISE (tooling) | `count_tool_calls` blind to Gemini flat schema → Gemini density recorded as 0 | `Validators/parse_trajectories.py:130-149` | Add top-level `type=="tool_use"` branch + broaden MCP prefix (`mcp__`/`mcp_mcp`) + read `tool_name`; regenerate `Trajectory_Stats.json` |
| LOW (hygiene) | Corrupt `Trajectory_Stats.json` Gemini avg = 0 | `_aux/Trajectory_Stats.json` | Regenerate after parser fix (true Gemini avg = 33.0) |
| LOW (hygiene) | Validator resolves `today` against stale 2026-06-12 | `_aux/Fact_Ledger.json` `lifecycle.today` null | Seed 2026-07-01 via `build_fact_ledger.py`; re-run validate |
| NOTE | S0 report overstates injection | `_aux/S0_Setup_Report.md` | Correct to "no separately-documented injection" |
| OPTIONAL | R6 fuses "not ready" + "don't market/show" | `7_Rubrics.json` R6 | Nice-to-have split for per-clause attribution; NOT a correctness fix (rubric is valid + achievable) |

**Shippable on true numbers: YES.** The parser defect changes the recorded evidence, not the ship decision — Opus 43.5 + Gemini 33.0 both clear the 15 floor, pass@1 is 0/6 on both models, and all 24 QC sub-dims are 5/5.
