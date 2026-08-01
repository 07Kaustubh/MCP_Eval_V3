# S3 Council B (Adversarial QC), Round 3

Task `46_6a62ccb6ce2323b4b9e0c8d8` · Universe StarPM (V4) · 34 criteria (34 outcome / 0 process)

Round 2 returned BLOCK (Major 0 / Moderate 5 / Minor 6). A strict AUDIT then returned REVISE. Both sets
of findings are applied. Round 2's report is preserved byte-identical at `S3_B_adversarial_r2.md`.

## Input pins

Hashed at entry. `check_export_freshness.py --pin` does not apply: this task has no platform-pasted
export yet (no `8a`/`8b`, no `Agent_Responses`). Substitute pins, re-verified at exit and unchanged:

| File | sha256 (first 16) | bytes |
|---|---|---|
| `7_Rubrics.json` | `49b8c088fbfbfe5f` | 32438 |
| `6_Oracle_Events.txt` | `b848980b5c620acf` | 44184 |
| `5_Prompt.txt` | `885750ecef51acc5` | 1383 |
| `_aux/Handoff_S2_S3.md` | `2590246144479dbb` | 28112 |

`Handoff_S2_S3.md` read in full (426 lines), not skimmed.

## Method note: three subagent fact-checks discarded as fabricated

I dispatched three explore agents to verify universe facts. The first returned a fully-formed report
citing Slack ids `msg_c006_0041_r3`, Airtable ids `recMR0041`, Linear `cmt_0042` / `iss_0117`, and users
`U007` / `usr_lsmith`. None of those id shapes exists in this universe, which uses 32-hex Slack ids,
`rec` plus 16 hex Airtable ids, `comment_` plus 32 hex, and `U` plus 10 hex users. It also reported
"Oakfield Commons: REFUTED, zero matches across all 35 files", and asserted the 94% and 97% figures sit
in two different messages nine minutes apart.

All three claims are false. A direct sweep returns 358 Oakfield/Commons hits across 7 files, and the two
percentages are in one message. **Every fact in this report was re-derived by direct query against
`_aux/Universe_Split/`.** No subagent output was used anywhere. Recording it because it is exactly the
failure mode rule 19 names, arriving through a new channel: a confident secondary report standing in for
the primary source.

## B1. Sub-dimension scoring

Names verbatim from `Docs_starpm/7_QC_Spec_Doc1.json`.

### Rubric

| Sub-Dimension | Score | Basis |
|---|---|---|
| Overall Rubric Quality | **4/5** | 2 Moderate issues (B8). Pass(5) requires zero major AND zero moderate. |
| All-Failing Rubrics | **5/5** (projected) | 1 predicted all-fail, below the 2+ gate. Re-derived in B9. |
| Rubric Category Balance | **5/5** | 34 outcome > 0 process. Binary sub-dim, no 3/4 band. |
| Process Rubrics | **5/5** | Zero process is correct here: `check_ordering_coverage.py` finds no ordering language, confirmed by re-run, and none of the prompt's four deliverables carries a sequencing clause. |
| Agent Centric Phrasing | **5/5** | All 34 titles open "The Agent ...". |

### Bearing on other dimensions

| Sub-Dimension | Score | Basis |
|---|---|---|
| Universe / Universe Feasibility (Data Exists) | **5/5** | Every record the rubrics pin resolved by direct query. Nothing ungrounded. |
| Oracle Event (OE) / OE Accuracy | **5/5** | All five decompose directives map exactly onto carriers (B5). |
| Trajectory / Tool Call Count | **PASS** (projected) | Midpoint 67 against the V4 40+ target (B3). |
| Trajectory / Agent Failure Rate, Error Rate | not measurable | No trajectories exist pre-run. |

Gates re-run by me rather than taken on report: `validate.py` rubrics / oe / submission_gate / injection
all 0 fails; `check_ordering_coverage`, `check_rubric_antipatterns`, `check_qc_binary`,
`check_oe_rubric_sync` all OK. `check_rubric_signal` SKIPs (no export). The 17 warns on the rubrics phase
are all benign and enumerated in B10.

## B2. Adversarial alternative paths

| # | Path | Verdict |
|---|---|---|
| 1 | Agent scopes Calendar to `lisa.smith@starpm.com` only. She holds rows on the June 2 Harris original, the May 19 Finley review, and the May Owner Report Review, so she sees exactly one review per owner. This positively confirms the prompt's "either of those" while the duplicate stays invisible. | Fails criterion 4 only. The designed stump and the AF candidate, not a rubric defect. |
| 2 | Agent batches all three make-ready corrections into one `update_records_for_table` call with a 3-element records array. | Passes 1, 2, 3. Correct: the criteria grade per-record end state, not call count. |
| 3 | Agent writes one Slack post carrying both owner names, the Finley figure, the open item, and a Harris clause. | Passes 22 to 26 from one message. The intended deliverable, not a hack. |
| 4 | Agent guesses "Harris: nothing past due" without querying QuickBooks. | Passes 26 (option B) and 33 without work. Inherent to grading a negative. Mitigated: criterion 24's FAIL-guard makes the opposite guess costly, and 8 and 9 require the `$0.00` and `$1,975.00` figures, which cannot be guessed. Accepted. |
| 5 | Agent opens one issue naming BOTH unresolved items. | Passes 21 ("either target is correct"; naming both includes naming either). Correct. |
| 6 | Agent opens two issues, one per unresolved item. | Fails 21 on the new `FAIL if more than one` clause. **Declined as a finding**, on artifact text rather than on precedent: the prompt reads "open **a separate item** for whatever is still genuinely unresolved", a singular determiner, and OE 35 states "Exactly one issue is expected, matching the prompt's 'a separate item'." Requiring one is not narrower than the prompt, so it is not Overly Specific. |
| 7 | Agent corrects Mesa Vista 207A or 4C alongside the graded three. | Not penalised by any criterion. Verified: no criterion names those rows. Correct per the OE 30 accept-set. |

## B3. Tool-call density

V4 design target 40+ average per model (`Docs_starpm/1`), QC-spec fail floor 15.

| Driver | Low | High |
|---|---:|---:|
| Scope setup (contacts, OPS-10 plus comments, owner split) | 4 | 7 |
| Cross-service discovery, OE 5 to 12 | 9 | 15 |
| Owner entity sweeps, OE 13 / 14 | 5 | 10 |
| Calendar enumeration (`list_calendars` plus `list_events` across 5 calendars; unavoidable for the duplicate) | 6 | 9 |
| QuickBooks AR (invoice and credit-memo searches, then per-entity reads on 7 invoices and 6 memos) | 6 | 18 |
| Airtable reads (`tblMakeReady` 120 rows, `tblMaintenanceTickets` 50 rows) | 3 | 7 |
| Slack (channel list, C006 history, thread expansion on `831d2b6760205432a20487e2664a607e`) | 3 | 6 |
| Gmail and HubSpot corroboration | 3 | 7 |
| Writes (Airtable 1 to 3, calendar 2, draft 1, comment 1, issue 1, Slack 1) | 7 | 9 |

**Low 46 · High 88 · Midpoint 67.** Clears the 40+ target with margin. Density is not at risk on this
task; the binding risk is difficulty, not volume.

## B4. Lever coverage

Levers as defined in `_aux/Hardness_Plan.md`, re-read rather than paraphrased from a council report.

| Lever | Definition | Carriers (1-based) | Status |
|---|---|---|---|
| **L1** | Latching on the persona's own undispositioned claim | 13, 14, 15, 16, 17, 27, 30 | 7 carriers. Strongest coverage in the set. |
| **L2** | Structured-DB skip (QuickBooks AR plus the unmirrored Calendar) | QB half 8, 9, 10, 11, 24, 31, 32, 33; Calendar half 4, 5 | 10 carriers, both halves live. |
| **L7** | Multi-write diversification | 1, 2, 3 (Airtable), 4, 5 (Calendar), 6 (Gmail), 18, 21 (Linear), 22 (Slack) | 9 write carriers across 5 services. |
| **L10** | Reversal / supersession | 1, 2, 3 (later row supersedes), 4 (Harris double-booking), 34 (OPS-10 state vs its own narrative) | **5 carriers. Survives the cut.** |
| **L11** | Net-vs-gross, 117 unapplied credit memos | 9, 11, 32, plus FAIL-guards in 10, 24, 31 | 3 positive carriers, no 1.1 carrier, as handoff obligation 6 requires. |

**L10 after the cut, which the brief asks about specifically.** The cut 2.1 restatement was one of five
L10 carriers, and the lever retains both a write carrier (4) and a read carrier (34). Criterion 34 is
genuinely reachable without the off-persona calendar fan-out: it needs only Linear reads on OPS-10 and
its comments, and criterion 18 already forces the agent to open that issue in order to comment on it.
Verified directly: OPS-10 carries `state_OPS_0` (Backlog) with `updated_at == created_at`
(`2026-05-03T22:11:57.112604-05:00`), against `comment_79dc83838bd65d678c48b5911f942412` ("Moving this
to In Progress") and `comment_179d6b0702be5ca1b0a1e967e1e136e0` ("Moving this up to In Review"). Zero
calendar dependency.

**L11 budget confirmed.** All six credit memos verified as `Balance == TotalAmt`, absent `LinkedTxn`,
`RemainingCredit: 0`. The lever is intact and none of its three carriers may be cut (rule 14).

## B5. Reverse coverage, both directions

**Forward, OE directive to criterion.** All five decompose directives map exactly, with no element
uncarried and no carrier invented:

| OE | Elements | Carriers | Match |
|---|---:|---|---|
| 30 | 3 | 1, 2, 3 | exact |
| 31 | 2 | 4, 5 | exact |
| 33 | 12 | 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 | exact |
| 34 | 2 | 19, 20 (plus write carrier 18) | exact |
| 36 | 5 | 22, 23, 26, 24, 25 | exact |
| 35 | single-criterion instruction | 21 | exact |

The M3 split is mirrored: OE 34's directive now names the two elements criteria 19 and 20 carry, closing
round 2's M3. The M4 addition is mirrored: OE 36's directive runs to 5 elements against 5 C006 criteria
(1 write plus 4 content). Both fixes are complete on both sides, so neither introduced artifact drift.

**Reverse, criterion to OE.** Criteria 1 to 26 trace to OE 30 through 36. Criteria 27 to 34 are Outcome
2.1 final-response restatements, and each traces to a fact established in the OE chain: 27 and 30 to OE
33's spring-read correction block; 28, 29, 31, 32, 33 to OE 33's per-owner position block; 34 to OE 34's
"two transitions that never took effect". No orphan criteria. `check_oe_rubric_sync` agrees, with 5
advisory identifier observations, all non-graded context bounds.

## B6. Atomicity

No F8 NON_ATOMIC_ENUM shape found. Re-checked with attention to the fixes, since the brief flags
fix-induced defects:

- **M3 split (18 / 19 / 20).** One 1.1 carrier plus two 1.2 content criteria on one comment. Naming both
  owners and stating the hand-off are independently discoverable and independently failable. Properly
  atomic; this closes round 2's M3 rather than trading it for a new defect.
- **M4 addition (26).** A *disjunctive* accept-set ("either the make-ready position or the receivable
  position"), not a conjunctive bundle. Disjunction is the anti-F8 shape, not the F8 shape. Atomic.
- **Criterion 21.** Disjunctive on target, pinned to cardinality one. Correct construction.
- **Criterion 32** is the one title carrying a conjunction ("on both owners' accounts"). It grades a
  uniform property over one set of six records rather than two independently-discoverable facts, so it
  is not F8, but its title and evidence disagree on scope. Filed as MINOR-1.

The three make-ready criteria (1, 2, 3) are one-per-row as OE 30 requires, never one criterion over the
set. All three rows verified present at `selSched`: `rec98bdfeec73545e` (Sunset Ridge 104B),
`rec987aae7d522057` (Sunset Ridge 309C), `rec8b679d92f30753` (the sole Ridgeview row).

## B7. Overlap

No two criteria grade the same content in the same artifact.

Three facts are each graded in three artifacts: the Finley `$10,980.00` (10 draft, 24 Slack, 31 final),
the Sunset Ridge Ready position (7 draft, 26 option A Slack, 29 final), and the Harris nil receivable (8
draft, 26 option B Slack, 33 final). The prompt mandates all three artifacts separately ("Put an email
together", "Bring the mid-year review item up to date", "Post a short version in the owner relations
channel"), so each is a distinct deliverable and grading the same fact in each is not duplication.
**The m5 cut is not re-raised**; it was declined and AUDIT upheld the decline.

**M4 did not open a new overlap.** Criterion 26 was the specific risk, checked against its three
neighbours: 23 requires *both* names, so no single act satisfies both 23 and 26; 24 grades Finley's
figure while 26 option B grades the absence of one for Harris, complementary rather than nested; 7 and
29 grade the same Harris position in *different* artifacts. No nesting found.

**Rule 17 pre-check.** Every dependent criterion binds its subject to the antecedent's artifact by
content rather than by criterion number: 7 through 17 all say "the draft addressed to
brooke.phillips@starpm.com", 19 and 20 say "the comment on OPS-10", 23 through 26 say "the message text
posted to the owner relations channel". A run where the antecedent write fails therefore cannot produce
a passing dependent. Correct by construction. `check_criterion_dependencies.py` is not runnable
pre-trajectory; re-run it at S4.

## B8. Severity census, denominator 34

| Severity | Count | % | Fail threshold | Result |
|---|---:|---:|---|---|
| Major | 0 | 0.0% | >10% | pass |
| Moderate or worse | 2 | 5.9% | >15% | pass |
| Minor or worse | 4 | 11.8% | >20% | pass |
| Absolute Major gate | 0 | | >=3 | pass |

Percentage bands all pass. **Overall Rubric Quality Pass(5) nonetheless fails**, because it requires zero
major AND zero moderate, and two Moderate issues stand.

### MODERATE-1. Criterion 34's title contradicts the OE it implements (new, opened by the M5 fix)

Title: "The Agent reports that the mid-year review issue OPS-10 **is still in** its Backlog state despite
comments announcing that it moved to In Progress and then to In Review."

OE 34 states: "The agent may also move OPS-10 out of `state_OPS_0` using `save_issue` ... That state
change is optional and must not be graded ... an agent that leaves the state alone is equally correct."

The OE therefore explicitly blesses an agent that corrects the state. That agent is the *strongest* path
available (it finds the contradiction, reports it, and repairs it), and it falsifies the title's
present-tense claim at the moment the final response is written. The evidence field is tense-neutral and
grades correctly ("a statement that OPS-10's recorded state contradicts its own comment thread, or
equivalently that the announced transitions never took effect"), and the explicit FAIL clause is narrowed
to "on the strength of the comments", so neither fires. The defect is confined to the title, which is
what graders anchor on (rule 16).

Overly Specific, MODERATE under the 07/16 taxonomy. The fix is one field: retitle to the discovery
framing, for example "The Agent reports that OPS-10's recorded state contradicted the two comments
announcing it had moved to In Progress and then to In Review." That passes on both permitted paths.

### MODERATE-2. Criterion 27 asserts a universe fact that is false (new; the AUDIT fix closed only half of it)

Title: "The Agent reports that **no record in either portfolio carries an occupancy figure**, so the 94%
read cannot be confirmed." The evidence repeats it: "because no record carries an occupancy figure for
either of these portfolios".

Re-read from the split, that is false. Slack message `a6779a055eaf5fb1893d0ed6d92e3b39` (channel C006,
Lisa Smith `U6480117503`, 2026-05-28T21:08:01+00:00, reply to `831d2b6760205432a20487e2664a607e`) reads
verbatim:

> "Robert's Mesa Vista portfolio is sitting at 94% occupancy, one unit still in make-ready targeting
> early June. Collections at 97%, one late payment cleared after first notice. Closed out three tickets
> this month including a water heater leak, and the turn is on track."

That is a record, it names one of the two portfolios, and it carries an occupancy figure. The true claim
is that nothing *corroborates* it, which is a different sentence.

The AUDIT reworded this criterion because a 94% occupancy figure exists on Oakfield Commons (confirmed:
`deal_9664cf85817555d0b1e0dfddfc054c96`, "Occupancy across the Oakfield Commons units held at 94%").
That half of the fix is sound. But the rewording left the criterion asserting the stronger falsehood
about the task's own source message.

This matters beyond tidiness because it attacks **L1, the highest-scoring lever at 6.5**. An agent that
reasons correctly about L1 writes "the only occupancy figure for these portfolios is your own May Slack
note, which no operational record supports". Against this title, that reads as a contradiction, so the
criterion is sharpest against the agent it should reward.

Criterion 13 already carries the correct phrasing for the same fact in the draft: "no record **supports**
the 94% occupancy figure". The fix is to mirror 13 into 27's title and drop the trailing evidence clause.

### MINOR-1. Criterion 32's title and evidence disagree on scope

The title requires the conclusion "on **both owners'** accounts". The evidence checks only "the credit
memos are not applied against any invoice", unscoped. An agent that states it for Finley alone, which is
where it is financially material since Harris owes nothing, passes the evidence and fails the title.
Blast radius is low because the natural phrasing covers all six memos, but it is a title/evidence
divergence of the kind that produces unstable grading (rule 29). Align the evidence to the title.

### MINOR-2. Criterion 13's justification is internally self-contradictory

It says the 94% "appears for either of these two portfolios **only in Lisa Smith's own Slack reply**"
and, in the same sentence, that "**no record anywhere carries an occupancy figure** for either
portfolio". Both cannot hold. Criterion 13's *title* is correct and justifications are not graded, so
impact is low, but it is the same false claim as MODERATE-2 and should be corrected in the same pass so
the artifacts do not drift apart.

## B9. Pre-submission all-fail prediction, re-derived on 34

**Predicted all-fail: 1. Below the 2+ hard gate.**

**Criterion 4, HIGH risk, the single AF candidate.** Root cause verified directly rather than inherited
from the handoff. The Rescheduled Harris event `qqbwq3s2h7wh5udoek2940mffk` fans out to exactly four
per-calendar rows, on `patricia.nguyen`, `aurora.winona`, `teresa.wood`, and `brooke.phillips`. There is
**no `lisa.smith` row**. The June 2 original `1pon50ds1aevem63td6f7emdn3` fans out to five rows
*including* hers. So an agent scoping Calendar to the persona sees one Harris review and two Finley
events, which positively confirms the prompt's "either of those" while the duplicate stays invisible.
Reaching it requires enumerating calendars Lisa is not on.

**Does the cut genuinely take the count below 2, or does another criterion inherit the root cause?**
It genuinely does. I swept all 34 for dependency on the Rescheduled instance and criterion 4 is the only
one. Criteria 27 to 34 were the place an inheritor would hide, and none of the eight mentions the Harris
calendar at all. Criterion 5 is *not* an inheritor: its target `8mwlxrq5w5oodwdpmvo83e00f2` carries a
`lisa.smith` row (`-b0504ab4`), verified, so it is reachable inside persona scope.

**The residual risk the cut did not address: criteria 9, 11, and 32 share one root cause.** All three
require overcoming the L11 inversion, and the inversion is uniform: all six credit memos carry
`Balance == TotalAmt`, absent `LinkedTxn`, and `RemainingCredit: 0`. An agent reading
`RemainingCredit: 0` as "already consumed" fails all three together. I do not predict them as all-fail,
because `Balance == TotalAmt` is a visible counter-signal on the same record and the prompt asks directly
for the money position. But **S4 must treat these as one root cause rather than three independent
findings**: if they all-fail together the count is 4 and the gate blows, and the correct response would
be to reword one carrier, not to write three AF justifications (rule 21 defaults to removal, and rule 16
reclassifies a repeated identical misreading as a rubric defect).

Lower-tier watch item: criterion 2 must discriminate `rec987aae7d522057` from `reca06d89f1a4ac5b`. Sunset
Ridge 309C verified as carrying exactly two `selSched` rows, so the F7 hazard is real; the criterion
states the discriminator (the open deep-clean question versus the unresolved utility transfer) in both
title and evidence, which is the correct construction. Medium-low risk.

## B10. Verdict

**VERDICT: BLOCK**

**Major 0 · Moderate 2 · Minor 2**

Round 2's eleven findings all close cleanly, and I could not find a case where a round-2 fix opened a new
defect in the way M2 and m2 did last round. The two Moderates have a different origin: MODERATE-1 was
opened by the **M5 addition**, and MODERATE-2 by an **incomplete AUDIT fix** that corrected the
Oakfield-facing half of a claim and left the half contradicting the task's own source message. Both are
single-field title rewrites with no structural consequence, no effect on lever coverage, and no change to
the criterion count. Neither is a rebuild trigger.

Both must clear before this can score Pass(5) on Overall Rubric Quality, which hard rule 10 requires. The
percentage bands in B8 all pass; it is the zero-moderate condition that binds.

Recommended fixes, in order:

1. Criterion 34: retitle to the discovery framing so both OE-permitted paths pass.
2. Criterion 27: mirror criterion 13's "no record supports" phrasing into title and evidence.
3. Criterion 32: scope the evidence to match the title's "both owners".
4. Criterion 13: correct the self-contradictory sentence in the justification.

No ADD is recommended. I looked for a coverage gap worth spending some of the 26 remaining slots on and
did not find one: all five OE decompose directives are exactly carried, every lever has carriers, and
reverse coverage is clean in both directions. Adding here would dilute rather than cover.

Two items for the phases that follow, neither a finding against this artifact:

- The `validate.py --phase rubrics` census reads "0/34 with Moderate+". That is the authoring agent's
  self-report and it disagrees with this review. Per rule 18 it is a claim, not evidence.
- The 17 warns are all benign. Six flag the derived sums `$0.00`, `$1,975.00`, `$10,980.00`, and
  `$3,655.00` as absent from the Fact_Ledger, and each was confirmed against QuickBooks
  (195 + 1250 + 530 = 1975; 8400 + 2190 + 390 = 10980; 2755 + 490 + 410 = 3655; all three Harris invoices
  at `Balance 0.00`). The rest flag evidence-side FAIL-guards (`$7,325.00`, `$1,622.00`, the three `rec`
  ids) as absent from titles, which is the correct construction, not a defect.
