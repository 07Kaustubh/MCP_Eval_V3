# Todos — S1

- [x] Run phase-readiness gate (`phase_ready.py --phase s1`) — OK, 1/1 upstream artifact present
- [x] Read inputs (1_Business_Function, 2_Persona, PersonaBrief, Hardness_Plan, Universe_Index)
- [x] Read mandated spec docs (Docs_starpm/9_Common_Error.md Part 1, 6_Prompt_Relative_Time_Updates.md)
- [x] Read format card (Reference/Prompt_Format.md) + V4 QC_Passed reference corpus (Task1..Task4)
- [x] Ground the atoms the prompt names (owners, deadline, Brooke, channel) against Universe_Split
- [x] Draft 5_Prompt.txt (254 words, 0 em-dashes)
- [x] Run validator — PASS, 0 fails / 0 warns / 3 distinct services (2 iterations to clean)
- [x] Run similarity gate — max composite 27.5 vs ceiling 40; Task 40 collision 27.1 at multiplier 1.000
- [x] Run verify_universe_atoms — PASS (0 fails, 0 warns; 0 atoms, expected given the withholding design)
- [x] Write Reads_s1.md
- [x] Council A — Grounding — **GO** (iteration 3)
- [x] Council B — Adversarial QC — **GO** (iteration 3), all 12 Prompt sub-dims at 5
- [x] AUDIT (strict veteran) — **PASS (STRICT)** at its iteration 2, after REVISE at iteration 1
- [x] Write Verification_s1.md — passes `check_verification.py` (see pipeline defect below)
- [x] Write final report to _aux/Reasoning/prompt_design.md
- [x] Write _aux/Handoff_S2_S3.md (consolidated 19-item obligation list for downstream phases)

## Validator iteration history (for AUDIT)
1. Draft v1 (252 w): FAIL cross-service (0 services) + WARN bolt-on.
   Root cause of FAIL: SERVICE_KEYWORDS needs 2+ natural service references. Fixed by naming
   DELIVERABLE surfaces only (email / issue tracker / owner relations channel), leaving the
   INVESTIGATION surfaces (calendar, QuickBooks, Airtable) unnamed to preserve lever L2.
2. Draft v2 (262 w): PASS 0 fails, WARN bolt-on persisted.
   Root cause of WARN: regex artifact. NAMED_ENTITY_RE_PROMPT tokenizes consecutive capitals,
   so "The Harris" never string-matched "Harry Harris". Fixed structurally by merging the
   deadline clause into the opening sentence rather than suppressing the warn.
3. Draft v3 (254 w): PASS 0 fails / 0 warns. Current.

## Open defect surfaced (NOT patched — needs operator decision)
`Validators/validate.py:472` hardcodes a Brookfield fallback date `"2026-06-12"` when
`Fact_Ledger.lifecycle.today` is null. This starpm task's Fact_Ledger has `lifecycle.today = null`
(StarPM has no fiscal_periods table), so the validator reports the WRONG universe today for every
StarPM task. Correct value is 2026-07-01 per today_horizon.json + Docs_starpm/6 + the registry.
Not patched here: validate.py is covered by frozen regression report hashes in
Validators/regression_baseline/, so a fix belongs in its own change with check_regression.py re-run.

## Pre-computed answers for downstream phases

### Rule 23 (ordering -> Process rubric) — RESOLVED AT S1, zero Process rubrics needed
`check_ordering_coverage.py` cannot run at S1 (it crashes on the `7_Rubrics.json` template
placeholder rather than reporting N/A). Ran its `ORDERING` detector against the prompt manually:
**all 6 patterns return zero hits.** The prompt contains no `then <action>`, no `before/after
<action>` precondition, no `once X ... then Y` dependency, no `based on what you find`, and no
`first ... then`. S3 may therefore ship zero Process rubrics without leaving an ordering
requirement ungraded.

This was deliberate. An earlier draft opened the deliverables paragraph with "When you have the
full picture, ..."; that clause was cut precisely because rule 23 would have forced a Process
rubric against an already-tight 60-criterion cap. The near-miss to watch: the prompt says "where
our own records do not match what you find", and ORDERING pattern [4] is `based on what you find`.
Different string, no hit, but if S2/S3 reword that clause, re-run the check.

### Council A carry-forward constraints (binding on S2/S3)
1. A7 MODERATE: "put the records right" is unbounded. A second reading adds a QuickBooks write
   (6 unapplied credit memos: Harris $1,975, Finley $3,655, all RemainingCredit 0, no LinkedTxn).
   Council A declined to block, reasoning the fix belongs downstream. S2/S3 must pin write targets
   uniquely BY CONTENT and must create no criterion a QuickBooks write could satisfy.
2. OPS-11 and OPS-13 share an identical title ("Owner review packages: data compilation and
   presentation prep"); OPS-20 and OPS-23 are nearby. OPS-10 resolves uniquely but S3 must pin by
   content, not by title. Hard rule 13 / F7 AMBIGUOUS_TARGET.
3. A10 business function = ambiguous (scored 3/5, NON-FAIL not FAIL). `owner_portfolio_review_midyear`
   is a documented Cat 2 scenario and #owner-relations is a Cat 2 channel; the persona home-function
   rule is controlling and no owner-facing action occurs. Top residual risk to re-check at FINAL.
4. L10 is partially signposted ("anything on the scheduling side ... not properly settled" reveals
   WHERE but not WHAT). Council A recorded this rather than claiming clean 5/5 preservation.

## ITERATION 2 — Council B BLOCK and the fix

### The blocker (Council B, B2 / Unique Ground Truth)
Draft v3 paragraph 3 read: "Where our own records do not match **what you find**, put the records
right." Paragraph 2 defines what the agent must find as "occupancy ... maintenance ... turns ...
**plus anything on the money side**". By anaphora, "what you find" carried the correction mandate
into the money workstream.

That is load-bearing because inside the money workstream the records are self-contradictory in
exactly the instruction's own terms: all six Harris/Finley credit memos (INV-2026-0841-572,
BILL-2026-0336, 2026-CM-089, BILL-2026-0335, INV-2026-0718, 2026-B-317, $5,630 total) carry
`RemainingCredit = 0` while `Balance == TotalAmt` and `LinkedTxn` is absent. QuickBooks exposes
`update_credit_memo` and `create_payment` among 141 tools. So a second reading applies the credits,
moves Finley from $10,980 to $7,325, and writes to a service the Hardness Plan marks read-only.

**The gradient inverted.** The agent that performs the L11 net-vs-gross reasoning CORRECTLY is
precisely the agent the prompt then pushed into the unplanned write. That is worse than plain
ambiguity, and it is why this was a BLOCKER rather than a MODERATE.

### Why it was not declined
Council A found the same text (A7) and declined it as MODERATE, reasoning the fix belonged to
S2/S3. Council B validated it as real and blocked. AGENTS.md rule 19 is explicit: a council may not
decline a finding it has itself validated as real on internal-precedent grounds alone. Council B was
right and the draft was wrong. Fixed at S1, where the root cause lives.

### The fix (v3 -> v4, one clause, no other edit)
- "Where our own records do not match what you find, put the records right ..."
+ "Where the unit and turn records do not line up with what you actually find on the ground, put
  those records right ..."

Scopes the correction verb to the operational record class and re-anchors the comparator to physical
property reality. Money survives ONLY as a read/report item via paragraph 2 and the email
deliverable. No figure, property, discrepancy, record state or service is named, so the L36
withholding test still holds.

### Lever accounting for the fix
- L11 net-vs-gross: PRESERVED but now rides paragraph 2's read/report clause only. This is the main
  risk the iteration-2 councils were asked to test. If L11 no longer reaches the agent at all, that
  is a HARDNESS_REGRESSION and a worse outcome than the blocker it closed.
- L10 calendar: UNTOUCHED (second clause unchanged).
- L2 / L1 / L7: unaffected. Still 6 writes across 5 services.

### Post-fix deterministic state
validate.py PASS 0 fails / 0 warns / 262 words / 3 services · 0 em-dashes · ORDERING zero hits.
Backup of the pre-fix draft: `_aux/5_Prompt_v3_preblock.txt.bak`.

### Open cross-council disagreement (carry to FINAL)
Business Function: Council A 3/5 (ambiguous, Cat 2 scenario container), Council B 5/5 (persona
home-function rule controlling, no owner-facing action anywhere). Verdict-neutral either way, both
agree it is NOT a FAIL. FINAL adjudicates.

### New carry-forward from Council B (strengthens L1)
Lisa posted two near-duplicate C004 thread replies 19 minutes apart on 2026-05-12
(`49b2873d46d55e4291a78d91d91a5054`, `5f60afa12c4c53b6b7694d59373acae8`) claiming "Harris and
Finley: occupancy is solid, two make-readies on track, no escalations to flag" against Sunset
Ridge's 7 make-ready rows across 3 units with ZERO in a Ready state. The Hardness Plan treats
latching as Finley-only, so L1 is stronger than recorded. This is a countable claim against a
countable reality. S3 must pin by content, not by picking one of the near-duplicate pair.

## ITERATION 3 — AUDIT returned REVISE. Both councils had missed a MAJOR defect.

Prompt is now at revision 5. AUDIT found a defect in the exact clause BOTH councils examined and
explicitly accepted at iteration 2. This is the clearest justification for the strict-audit gate the
pipeline has produced.

### AUDIT F1 (MAJOR) — "the scheduling side" denoted Airtable, not Calendar
Both councils debated only whether that clause OVER-SIGNPOSTED lever L10. Neither asked what the
phrase DENOTES. Verified independently by me before acting, every figure reproduced:
- `tblMakeReady.fldTurnStatus` = `{selSched: 43, selReady: 21, selProg: 56}` of 120 rows. The status
  option is literally named "Scheduled".
- Field literally named `fldTargetReady`. **99 of 120** rows past target and NOT Ready.
- 45 rows mention `schedul*`.
- Both owners have a qualifying row: `rec987aae7d522057` (Sunset Ridge 309C, Harris, `selSched`,
  notes "Alicia to confirm whether deep-clean crew is available July 21 or if we need to push to
  July 23. Awaiting her input") and `rec8b679d92f30753` (Ridgeview roof, Finley, `selSched`).

"Do the same" inherits the correction verb from the immediately preceding Airtable clause, and
Calendar is never gestured at anywhere else in the prompt. So an agent could discharge the entire
clause inside Airtable and never open Calendar, making the calendar criterion **beyond-prompt** —
precisely the defect both councils kept the clause in order to prevent. AUDIT also computed a
conditional density consequence: the strict Opus floor drops to ~37-40, under the V4 target of 40,
on that reading.

**Why both councils missed it.** They evaluated a false binary (keep the clause vs delete it) and
never considered rewording. AUDIT's phrase for this: they did not agree themselves into a leak, they
agreed themselves into an artificially narrow option set.

**Fix (rev4 -> rev5), paragraph 3 second clause:**
- "..., and do the same for anything on the scheduling side for these two that is not properly settled."
+ "... . Do the same for their review meetings if either of those did not end up properly settled."

Disambiguation evidence: NO Airtable field name carries a meeting concept (`tblMakeReady` is
`fldUnit` / `fldTurnStatus` / `fldMoveOut` / `fldTargetReady` / `fldNotes2`); 268 calendar events
carry "Review" in properties; the 22 Airtable rows containing "meeting" have it only as free text in
notes. A make-ready row cannot BE a review meeting.

### AUDIT F2 (MODERATE) — the Hardness Plan's calendar pin list was FALSE
It certified the Harris pair as "safe to pin (distinct base ids)". Distinct from each other, yes, but
that is not what hard rule 13 asks. Calendar stores ONE ROW PER INVITEE CALENDAR. Verified:
- `1pon50ds1aevem63td6f7emdn3` -> **5 rows** (patricia.nguyen, aurora.winona, teresa.wood,
  brooke.phillips, lisa.smith)
- `qqbwq3s2h7wh5udoek2940mffk` -> **4 rows** (same minus lisa.smith)

Two binding consequences for S2/S3:
1. F7 AMBIGUOUS_TARGET: pinning a bare base id matches 5 rows (or 4). Pin the per-calendar row or
   describe by content plus calendar.
2. **Lisa has NO row on the Rescheduled event**, so `respond_to_event` is not an available path for
   her. Her options are `update_event` or `delete_event`. Any OE step or rubric assuming she can
   respond to the reschedule is unsatisfiable on EVERY run. S2 must record the accepted end-state set.

Both councils repeated the false claim without re-deriving it. Root cause: the uniqueness check was
run against Airtable (one record = one row) and carried across to Calendar without re-checking
Calendar's storage shape.

**Actioned:** `Hardness_Plan.md` line 143 corrected in place with an inline marker, plus two new
sections at end of file (`## CORRECTION: Calendar pin list`, `## CORRECTION: prompt clause that
carries the Calendar write`). Original backed up to `Hardness_Plan.md.pre_s1audit.bak`. The false
claim can no longer be read without the correction.

### AUDIT adjudications on the open items
- **tblMaintenanceTickets**: Council A RIGHT, Council B WRONG. Four fields, no unit field, no turn
  semantics. "unit and turn records" licenses `tblMakeReady` ONLY. Maintenance is read-and-report
  (feasible: 7 rows with null `fldCompletionDate`, attribution via description prose).
- **L11 no Outcome 1.1 carrier**: real, but NOT an S1 defect. L11 lives in QuickBooks, which is
  read-only and the exact surface Council B blocked; giving it a write carrier reintroduces the
  closed defect. It is correctly report-only. Mitigation belongs in S3's budget (rules 14 + 28).
- **Business Function 5/5**: reached independently, not via the home-function rule. Decisive fact:
  EVERY write is internal. The owners are subjects, not recipients.
- **L36**: concur, no leak. "unit and turn records" does not over-signal, because L1's actual
  discriminators (the 94%/97% figures, the water-heater attribution) live in Slack/Linear/QuickBooks,
  not in unit or turn records.

### Process signal worth keeping
`check_council_yield.py` flagged `S1_A_grounding.md` **DECLINE-HEAVY** (6 of 11 findings declined,
55%). That flag was predictive twice over: Council A's A7 decline was overturned by Council B's
block, and its acceptance of the scheduling clause was overturned by AUDIT. Corpus totals: 4 reports,
81 KB, 41 findings, 12 declines, 5.09 findings per 10 KB.


## PIPELINE DEFECT found at S1 close — runbook contradicts its own validator

`Reference/Sessions/S1.md` Step 0.5 gives a template with `## Data sources consulted` and NO
`## Verdict` section. `Validators/check_verification.py:17-27` requires `## Sources consulted`,
`## Verification statements`, `## Discrepancies surfaced`, `## Verdict`, plus the literal labels
`Per-task data` / `Eval spec` / `QC spec` inside the Sources block.

**An agent that follows the S1 runbook verbatim writes a Verification file that FAILS the gate and
blocks `phase_ready.py --phase s2`.** Hit on this task: the first `Verification_s1.md` failed with
"missing section `## Sources consulted`" and "missing section `## Verdict`", and S2 refused to open.
Fixed by rewriting to the validator's contract; pre-fix copy at `Verification_s1.md.pre_gate.bak`.

This is the exact defect class AGENTS.md rule 30 created `check_pipeline_wiring.py` for. The template
is a citation of the validator's contract, and it does not resolve. Worth checking whether the other
phase runbooks carry the same stale template.
