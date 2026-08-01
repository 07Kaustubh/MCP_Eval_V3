# S1 -> S2/S3 Handoff

Single consolidated obligation list from `S1_A_grounding.md` (GO, iter 3), `S1_B_adversarial.md`
(GO, iter 3) and `AUDIT_prompt.md` (PASS STRICT, iter 2). S2 and S3 run in fresh chats; this is the
one file they need beyond the runbook. Every id below was re-verified against
`_aux/Universe_Split/` at S1 close, not copied from a report.

## BLOCKING obligations

### 1. Never pin a bare calendar base id (F7 AMBIGUOUS_TARGET)
Calendar stores **one row per invitee calendar**. Complete verified set:

| # | Event | base id | rows | when | Lisa has a row? |
|---|---|---|---:|---|---|
| 1 | Harry Harris Mid-Year Portfolio Review | `1pon50ds1aevem63td6f7emdn3` | **5** | 06-02 12:15-12:45 | yes, accepted |
| 2 | Harry Harris Mid-Year Portfolio Review **(Rescheduled)** | `qqbwq3s2h7wh5udoek2940mffk` | **4** | 06-03 15:00-16:30 | **NO** |
| 3 | Robert Finley Mid-Year Portfolio Review | `8mwlxrq5w5oodwdpmvo83e00f2` | **4** | 05-19 11:45-13:15 | yes, **declined** |
| 4 | May Owner Report Review - Finley Properties | `ti5zt1xubdggbehtp79um9mim6` | **3** | 05-28 11:45-12:15 | yes, **declined** |

Pin the per-calendar row, or describe by content plus the calendar it sits on.

### 2. Calendar accept-set must span `update_event` and `delete_event`
**Never require `respond_to_event` on event 2.** Lisa has no row there, so that path is
unsatisfiable on every run. She DOES have a row on 1, 3 and 4, so it is available there.
`update_event` / `delete_event` are `eventId`-addressed with `calendarId` OPTIONAL, so she is not
gated by calendar ownership on any of the four.

### 3. Pin OPS-10 by content, never by title
Verified near-duplicates. **OPS-11 and OPS-13 are BYTE-IDENTICAL in different states:**

| id | state | title |
|---|---|---|
| **OPS-10** | `state_OPS_0` | Mid-Year Owner Portfolio Reviews - June 2026 |
| OPS-11 | `state_OPS_1` | Owner review packages: data compilation and presentation prep |
| OPS-13 | `state_OPS_4` | Owner review packages: data compilation and presentation prep |
| OPS-20 | `state_OPS_2` | Owner review format confirmed - sub-issues assigned per owner |
| OPS-23 | `state_OPS_2` | Owner Review Packages - Data Compilation and Presentation Prep |

OPS-10 is the only one carrying "Mid-Year" in its title. That is the discriminator.

### 4. No write criterion against QuickBooks
QuickBooks is read-only in this design. Residual near-miss: credit memo `920762830750`
(`2026-B-317`, Finley, $2,755, the largest of the six) genuinely carries a `Unit Turn / Make-Ready`
line item, so a naive unit+turn match reaches it. It fails structurally (its fields have no ground
counterpart, so the prompt's conditional cannot fire), but **do not author a criterion a QuickBooks
write could satisfy.** Grade L11 on written content only.

### 5. No write criterion against `tblMaintenanceTickets`
Four fields (`fldTicketNumber` / `fldDescription` / `fldPriority` / `fldCompletionDate`), no unit
field, no turn semantics. "Unit and turn records" licenses `tblMakeReady` ONLY. Maintenance stays
read-and-report: feasible via 7 of 50 rows with null `fldCompletionDate` and 26 of 50 descriptions
carrying a unit/property token. AUDIT adjudicated this for Council A over Council B.

### 6. L11 must be explicitly budgeted at S3
It has **no Outcome 1.1 carrier** and is gradable only via 1.2 / 2.1. AUDIT ruled that correct,
because giving it a write carrier reintroduces the defect Council B blocked at iteration 1. But a
lever with no write carrier is exactly what silently vanishes when trimming to the 60-criterion
ceiling. **Never cut a lever carrier (rule 14).** Cut zero-signal criteria first (rule 28).

## PINNING cautions

7. **Pin L1 by content**, not by picking one of the 2026-05-12 near-duplicate pair
   (`49b2873d46d55e4291a78d91d91a5054`, `5f60afa12c4c53b6b7694d59373acae8`, same author, 19 minutes
   apart, both thread replies). L1 covers **both** owners, not Finley only as the Hardness Plan says.
8. **Pin event 4 by FULL title.** "May Owner Report Review - Finley Properties" is also a Finley
   review meeting and also looks unsettled. Additive, not competing, but a criterion aimed at the
   mid-year review must not be satisfiable by it.
9. **Cross-owner bleed:** "Linda Castillo Mid-Year Portfolio Review" exists (4 rows). Castillo is
   Patricia's owner. The prompt's possessive "their" excludes her. Do not let a criterion sweep her in.
10. **Make-ready carriers.** Safe: Mesa Vista 107A, Mesa Vista 310C (`rec88734a4fdfde57`), all of
    Sunset Ridge. Excluded as ambiguous: Mesa Vista 207A (3 rows), Mesa Vista 4C (2 rows), Las Palmas
    204B (53 rows), Las Vistas 311A (15 rows), any bare "Unit 14". The corrected-row set is
    data-determined, so write one atomic criterion per genuinely-mismatching row (F8 NON_ATOMIC_ENUM).

### 6b. Pin the cardinality of the Linear create (F8 NON_ATOMIC_ENUM)
Found by Oracle verification; **no council flagged it.** Every cardinality finding in the three
council reports targets `tblMakeReady` rows (obligation 10); none targets the Linear create. The
prompt says *"open **a separate item** for **whatever** is still genuinely unresolved"* - singular
determiner, plural-indeterminate complement. "A separate item" reads as ONE issue, so this is not a
prompt defect, but S3 must pin the expected count explicitly rather than leaving it open, or it
manufactures exactly the F8 NON_ATOMIC_ENUM shape hard rule 13 forbids. Do not write a criterion
that passes on "one or more items".

## Design facts S2/S3 must not contradict

11. **Zero Process rubrics is valid** (rule 23). All 6 `ORDERING` patterns in
    `check_ordering_coverage.py` return zero hits. If S2/S3 reword the "what you actually find on the
    ground" clause, re-run that check: ORDERING pattern [4] is `based on what you find`, a near-miss.
12. **The calendar defect is NOT Harris-only.** Finley's review is 05-19 11:45-13:15 against a comment
    saying "first week of June, 60 minutes in the afternoon", and **zero Finley events exist in
    06-01..09**. Lisa and Aurora both declined it. The Harris original also contradicts its Slack
    announcement (30 min midday June 2 vs "45-minute morning call late June"). Three carriers, not one.
13. **David Shea has 0 of 565 calendar rows**, confirming H4. The OPS-10 comment claiming "all four
    owner meetings are confirmed" is false. But the prompt scopes to Lisa's two owners, so Shea is
    Patricia's half. Do not author a Shea criterion.
14. **Pre-registered failure mode for S4 (rule 21) - the single highest all-fail risk in this task.**
    Lisa has rows on 3 of the 4 events but NOT on the Rescheduled duplicate. An agent scoping Calendar
    to the persona sees exactly two events, one per owner, which **positively CONFIRMS the prompt's
    "either of those"** while the Harris double-booking stays invisible. Sharpened by Oracle
    verification: this means **the L10 calendar write is reachable only by enumerating calendars Lisa
    is not on**. It is feasible (`list_calendars` + `list_events` exist) and fair, but it is the most
    likely place this task produces an all-failing criterion. **Rule 21's default for an all-failing
    criterion is REMOVAL, not justification** - S4 must argue for removal first and keep it only on a
    defence it would state to a reviewer unprompted.

## Escalated to FINAL, not closed

15. **L2's calendar half is attenuated** by naming "review meetings". MODERATE, knowingly accepted as
    the cost of licensing the calendar write. The QuickBooks half is untouched. Council A escalated
    rather than delegating it.
16. **Business Function** is an agreed 5/5, but Council A revised 3 -> 5 toward agreement, which is
    where groupthink hides. AUDIT reached 5/5 independently (every write is internal; the owners are
    subjects, not recipients). FINAL should re-read it cold.

## Pipeline defects surfaced, not patched

17. **The universe-today defect is 3 of 4 universes wide, and the regression baseline has enshrined
    it.** Measured at S1 close, after Oracle verification flagged that I had asserted the
    "blocked by frozen hashes" claim without ever testing it.

    **Root cause is a one-line key mismatch, not the fallback.** `build_fact_ledger.py:314` reads
    `th.get("today")`; `build_universe_index.py:310` writes that key as `"universe_today"`. So
    `Fact_Ledger.lifecycle.today` is `null` for EVERY task in EVERY universe, which means
    `validate.py:472`'s `or "2026-06-12"` fallback fires universally. That fallback is Brookfield's
    date and is universe-blind, even though the same function branches on `universe == "starpm"`
    two lines earlier.

    **Correct values per `Validators/universes.py`:** brookfield 2026-06-12 - keystone 2026-04-28 -
    moveops 2026-04-26 - starpm 2026-07-01. So the fallback is right ONLY for Brookfield, by
    coincidence, and silently wrong for the other three.

    **The frozen baseline pins the wrong answer.** Of the 7 baseline tasks with a date NOTE, all 18
    occurrences assert `2026-06-12`:

    | task | universe | frozen report says | correct |
    |---|---|---|---|
    | 10, 11, 12 | brookfield | 2026-06-12 | 2026-06-12 (OK) |
    | 33, 35 | keystone | 2026-06-12 | **2026-04-28** |
    | 34, 36 | moveops | 2026-06-12 | **2026-04-26** |

    **Decision-ready re-baseline scope (operator call, NOT done here):** fix the one-line key
    mismatch in `build_fact_ledger.py:314`; that changes **4 of 21** pinned reports (the `prompt.md`
    for tasks 33, 34, 35, 36) and requires re-pinning `build_fact_ledger.py` in
    `regression_baseline/code_hashes.txt`, which pins it today. Brookfield's 3 reports are
    unaffected. No `validate.py` change is needed, so its code hash is untouched.

    **Consequence while unfixed:** "Alignment with Today's Date" is a BINARY QC sub-dim (rule 26).
    On this task the validator NOTE claims 2026-07-01 is `2026-06-12`, which would make the correct
    phrase "It is now July" read as a future reference. AUDIT accepted the disposition only because
    the sub-dim was independently established by direct query of `today_horizon.json`, not because
    the validator signal was sound. **Do not cite the validator's date NOTE as evidence on any
    non-Brookfield task.**

18. **Every phase runbook's verification template contradicts `check_verification.py`.** Measured at
    S1 close, not estimated. `check_verification.py:17-27` requires `## Sources consulted`,
    `## Verification statements`, `## Discrepancies surfaced`, `## Verdict`, plus the literal labels
    `Per-task data` / `Eval spec` / `QC spec` inside the Sources block. Against that:
    - **16 of 16** runbooks in `Reference/Sessions/` write `## Data sources consulted` (wrong header).
    - **0 of 16** template blocks include a `## Verdict` section.
    - S1.md / S2.md / S3.md all lack the literal label `Per-task data`.

    So an agent following ANY phase runbook verbatim produces a verification file that fails the gate.
    Hit on this task: the first `Verification_s1.md` failed on the two missing sections and
    `phase_ready.py --phase s2` refused to open. Fixed here by writing to the validator's contract;
    pre-fix copy at `Verification_s1.md.pre_gate.bak`.

    **`check_pipeline_wiring.py` does not catch this** (it returns "[OK] no wiring errors"). It
    verifies that cited paths, scripts, flags and phases RESOLVE, not that a runbook's template
    contract MATCHES its validator's required contract. That is the gap, and it is the defect class
    AGENTS.md rule 30 exists for.

    **Live blast radius:** sweeping every task's `Verification_s1.md` against the gate,
    **`Tasks/42_6a62ccac9492f2a60e456c1c` currently FAILS** with "missing section
    `## Sources consulted`". Tasks 40, 41, 43, 44, 45 and 46 pass. So task 42 has a broken
    verification artifact on disk and would be blocked at its own S2 gate. Operator decision, not
    fixed from here.

19. **`check_qc_binary.py` and `check_ordering_coverage.py` traceback** on the `7_Rubrics.json`
    scaffold placeholder instead of reporting N/A. Cosmetic but they look broken at S1/S2.

---

# S2 -> S3 additions

Written at S2 close. Everything below was re-derived from `_aux/Universe_Split/` during S2, not carried
from a council report. Where a council claim turned out to be wrong it is marked.

## Corrections to the Hardness Plan, which S3 must not re-import

The plan carried six premises that the universe does not support. The OE file is written against the
corrected versions.

1. **QuickBooks customer rows carry no `Balance` field.** Only `Active`, `CompanyName`, `DisplayName`,
   `PrimaryEmailAddr`. An owner position must be aggregated from `invoice` rows. Never write a criterion
   that expects a customer-balance read.
2. **Harry Harris carries $0.00 open receivable.** All three of his invoices are `Balance 0.0`, each
   matched by a payment of identical amount. Only Finley carries a balance: **$10,980.00** across
   `2026-494` ($8,400.00), `2026-303` ($2,190.00), `4421` ($390.00), past due by 31 / 26 / 19 days.
3. **The net-vs-gross lever inverts.** All 117 credit memos carry `RemainingCredit: 0`, which reads as
   "already consumed" and argues AGAINST the correct answer. What establishes the credits are unapplied
   is `Balance == TotalAmt` plus absent `LinkedTxn`. Netting Finley's $3,655.00 against $10,980.00 to
   report $7,325.00 is the error, not the insight.
4. **Airtable has no owner field, no owner table and no property table**, and the string "Harris"
   appears zero times across all 170 Airtable records.
5. **The water-heater list was wrong on two of four.** Dunmore Unit 3 and 2214 Oleander do not exist in
   Airtable. The load-bearing claim survives: zero water-heater records touch Mesa Vista.
6. **A fifth owner-review calendar event exists**: Linda Castillo Mid-Year Portfolio Review
   (`epax0kiwoq0ygmqxezm2pax18l`, 2026-05-26), and Lisa holds a row on it and accepted. No prior phase
   modelled it. She is Patricia's owner. No criterion may sweep her in and no enumeration claim may be
   written that she would falsify.

## The three bridges the whole task rests on

Airtable cannot answer "which property belongs to which owner". All three bridges are external.

- **Finley to Mesa Vista**: OPS-100's description, plus Slack `831d2b6760205432a20487e2664a607e`,
  `a6779a055eaf5fb1893d0ed6d92e3b39`, `2687eb8d7cae501ea99b8c8305f12217`, three OPS-100 comments, and
  HubSpot `ticket_87552e6b23bc5a92bd2641b9054b8c13` (one of three near-identical move-out tickets and
  the only one naming him).
- **Finley to Ridgeview**: `rec8b679d92f30753` names Robert Finley directly; invoice `2026-494`
  corroborates.
- **Harris to Sunset Ridge**: this bridge is WEAK and S3 must treat it as such. It rests on the
  convergence of four records, all running through the same contested unit: Linear OPS-32 ("the Tanya
  Mitchell eviction case at one of Harry Harris's units"), calendar event `nuh928ma4rwhwf1bnap30rmfli`
  ("JP court hearing for the Mitchell eviction at the Harris property"), Airtable `reca8230a8fd9ff51`
  placing Mitchell on `fldUnit` "Sunset Ridge Unit 14", and QuickBooks invoice `113714702211`
  (DocNumber 4422) billing Harris for that unit.

  **Two earlier claims about this bridge were WRONG and were removed at AUDIT. Do not reinstate either.**
  (a) It is NOT "the only row in the universe naming Harris alongside a property": Harris carries ten
  property-naming line items across eight QuickBooks records, including Palomar Gardens, Fernwood
  Gardens, Maple Ridge Building 2, 4402 Larkspur Ave, 233 Elmsworth Blvd, 4722 Elmwood Ave, Elmwood
  Units 204 and 211, and Pinebrook Apartments. No single row establishes a portfolio.
  (b) `ItemRef` "Monthly Management Fee" does NOT discriminate ownership. It appears on 24 distinct
  customers, 9 times on Harris, 3 on the delinquent tenant Tanya Mitchell, 2 on Simone Okafor, and
  **zero times on Robert Finley**, the universe's other confirmed owner. Applying that rule
  symmetrically would make Harris the owner of Maple Ridge and Finley the owner of nothing.

  The counter-evidence is real and must stay visible: invoice `110274597983` (DocNumber 4418, $325.00)
  bills Simone Okafor for the same unit on the same `TxnDate` 2026-05-13 and `DueDate` 2026-06-12, and
  Gmail `2ae48555b3009a95` has Brooke Phillips asking `linda.castillo@gmail.com`, not Harris, for
  written owner authorization to evict the tenant in that unit.

**S3 obligation:** never require an agent to name the owner of Sunset Ridge Unit 14, and do not write
any criterion that depends on Harris's ownership of Sunset Ridge being cleanly established, because it
is not. Grade the Sunset Ridge make-ready work itself, which is unambiguous, rather than the ownership
inference that reaches it.

## Sunset Ridge Unit 14 ownership is contested and must stay unresolved

- Linear OPS-32 "Eviction Hearing - Mitchell, Harris Property" says the case is at "one of Harry
  Harris's units".
- Gmail `2ae48555b3009a95` is Brooke Phillips requesting written eviction authorization from
  **linda.castillo@gmail.com** for that same unit.
- Patricia Nguyen runs the delinquency correspondence, and under the verified OPS-10 split Patricia owns
  Shea and Castillo, not Lisa's owners.

The OE file declines to resolve this and **excludes both open delinquency records (`rec46234590708b5c`
MT-2026-0184 and `recc0ecc885e9645e` DLQ-2026-0601) from graded Harris content**. S3 must not
reintroduce them. An agent that reads the Gmail and excludes Unit 14 has reasoned better than a
criterion that demands it.

## The graded write set, with cardinality already pinned

| OE | Write | Expected cardinality |
|---|---|---|
| 30 | `update_records_for_table` on `tblMakeReady` | exactly 3 rows: `rec98bdfeec73545e`, `rec987aae7d522057`, `rec8b679d92f30753` |
| 31 | calendar resolution | exactly 2 outcomes, one per owner |
| 33 | `create_draft` to brooke.phillips@starpm.com | 1 draft, 10 content elements |
| 34 | `save_comment` on OPS-10 | 1 comment. The OPS-10 state change is NOT expected and NOT graded |
| 35 | `save_issue` | exactly 1 new issue, graded on title and description because `next_issue_number` is 1000 |
| 36 | `slack_send_message` to C006 | 1 post, 4 content elements |

Four `S3 must decompose this into one criterion per content element (...)` directives are embedded in
OE 30, 31, 33 and 36. Rule 14 requires that any cut removing a named element be mirrored back into the
OE in the same pass. Total: 6 write carriers plus 19 content elements = 25 before any Outcome 2.1, well
under the 60 ceiling.

**Mesa Vista 207A and 4C:** their `selProg`/`selReady` rows are genuinely out of step with the ground,
but each unit string matches several rows so no criterion can pin one. They sit outside the graded set.
An agent that corrects them has not erred and must not be marked down.

## Hazards for S4

1. **Highest all-fail risk:** the Harris calendar duplicate `qqbwq3s2h7wh5udoek2940mffk` is reachable
   only by enumerating calendars Lisa is not on. She holds no row. An agent scoping Calendar to the
   persona sees one review per owner and never finds it. Rule 21's default for an all-failing criterion
   is REMOVAL, not justification.
2. **Six of 251 Slack `latest_reply` pointers are dangling**, including the one on the C006 thread parent
   this task depends on. Following it instead of `thread_parent_id` returns nothing. Council B round 1
   fell into exactly this and inferred a wrong reply date from it before withdrawing the finding.
3. **Empty `fldCompletionDate` is stored two ways** in `tblMaintenanceTickets`: 3 rows carry `''` and 4
   carry `null`. Any open-ticket criterion must tolerate both.
4. **`next_issue_number` is 1000**, so the created issue's identifier cannot be predicted. Grade on
   content.

---

# S2 close: constraints discovered in the final review rounds

Thirteen gate rounds ran (Council A x4, Council B x4, AUDIT x5). These four items surfaced late and
are binding on S3.

## 1. Mesa Vista 4C belongs to Linda Castillo, not Robert Finley

Measured: **zero records anywhere in the universe name both "4C" and "Finley".** Against that, five
independent records place 4C with Castillo: `rec12969a3fdb0852` flags her on the turn, Gmail
`5101c5a41dffa90a` and `66132537181ecbe1` are Carlos Mendez writing to `linda.castillo@gmail.com` as
the owner, and QuickBooks invoice `445653930748` bills the 4C pass-throughs to her.

OE 14 enumerates all eight Mesa Vista rows as Finley's cluster, which is right as a search result and
wrong as an ownership claim for 4C specifically. **No criterion may treat Mesa Vista 4C as Finley's**,
and 4C sits outside the graded correction set on the same ground as the Unit 14 delinquency records.

## 2. Mesa Vista 4C is finished, and the earlier reading was backwards

An intermediate revision asserted that 4C's `selReady` row `recc8534b3fd13954` fails against the
ground because a confirmed QC inspection sits on 2026-07-15. That is wrong and is corrected. Closed
Airtable ticket `reca424761ae15355` records "All make-ready work at Mesa Vista 4C is complete", four
QuickBooks vendor bills are entered, and the owner has been told it is market-ready. The `selReady`
row matches the ground; the future QC event is the outlier.

## 3. Accept-set breadth is deliberate in four places and must survive into rubrics

Each of these was argued through at least two gate rounds. Narrowing any of them will fail an agent
that reasoned correctly.

| Step | Accept-set |
|---|---|
| OE 15 / OE 35 | Either unresolved-and-untracked item is a defensible new-issue target: the Mesa Vista 310C subfloor assessment, or the Sunset Ridge 309C utility transfer on `reca06d89f1a4ac5b` |
| OE 26 | An agent that surfaces invoice `445653930748` as a Mesa Vista billing question has found something real and must not be marked down, provided it is not added to Finley's balance |
| OE 30 | On Mesa Vista 4C, leaving the pair alone, moving `recbd087a4abd605b` forward, and moving `recc8534b3fd13954` back are all acceptable |
| OE 33 | Any Mesa Vista make-ready unit count from two to four is correct, provided the agent states that more than one unit is involved |

## 4. `search_invoices` with query "Mesa Vista" returns exactly one record

That record is `445653930748`, DocNumber `2026-534`, Balance $1,622.00, DueDate 2026-05-31, so 31 days
past due, billed to Linda Castillo. It is the single most natural money query for the Finley portfolio
and it returns a record that does NOT belong in his receivable. `$10,980.00` stands. The Hardness Plan
names this record as a designed trap.

## Mechanical state at S2 close

- `validate.py --phase oe`: 0 fails, 0 warns, 36 steps, zero em/en dashes.
- `verify_universe_atoms.py`: 0 fails, 57 atoms, 2 warns, both on future calendar dates cited
  deliberately for the rule-13 every-service sweep.
- Operator sweep: **144 of 144 identifiers** in the OE file resolve verbatim in the universe
  (32 Airtable record ids, 24 QuickBooks entity ids, 10 Slack message ids, 9 Linear issues, 9 calendar
  base ids, 6 Linear comments, 5 per-calendar rows, 5 HubSpot objects, 11 emails, and the field, table,
  option, state, project, team and channel ids). **32 of 32 tool names** resolve in the catalog.

---

# S2 close, addendum: notes for S3 raised by the post-council Oracle review

## 1. Occupancy is answered only as a refutation, and that is deliberate

The prompt asks for "the real position on occupancy". No record anywhere in this universe carries an
occupancy figure for either portfolio. The 94 percent traces to Lisa's own Slack message and to Brooke
repeating it back in `comment_5a6d779a715f587392dd00b9c8dbbd4a`, and nothing supports it independently.
So the OE chain produces a refutation rather than a number.

**S3 consequence:** any occupancy criterion has to be written out of a negative. Phrase it as the agent
correcting or qualifying the 94 percent claim, never as the agent reporting an occupancy figure, because
there is no figure in the universe to report.

## 2. Four steps carry no tool call

OE 4, OE 15, OE 16 and OE 17 state conclusions drawn over rows already retrieved at OE 3, OE 13 and
OE 14. `Evals_starpm/2_OE_Eval.md` Phase 1.2 flags pure-reasoning steps, and Council B round 4 accepted
these as synthesis over already-pulled rows rather than as skipped discovery. Recorded so S3 and any
later reviewer do not rediscover it as a defect. No criterion should rest on those steps having made a
call of their own.

## 3. Both Mesa Vista pairs now carry an explicit accept-set

4C and 207A both say plainly that an agent which corrects them and an agent which leaves them alone are
each acceptable. Neither pair is in the graded set. Do not narrow either.

## 4. The graded Sunset Ridge corrections rest on supersession, not on elapsed time

`rec98bdfeec73545e` and `rec987aae7d522057` are corrected because a later row on the same unit records a
further-advanced state, not because the July dates in their notes have passed. Those dates sit AFTER
universe today 2026-07-01. A criterion phrased as "the repaint has started" or "the July 15 date has
passed" would be wrong and would be defensibly refused by a date-checking agent. Phrase any criterion on
these two rows around the later row superseding the earlier one.

## 5. Every record the file cites is now reachable by a call the file names

Thirteen identifiers across OE 13 and OE 30 were cited without a retrieval path until the final pass.
The retrieval surface now includes `search_estimates` query "Harris" (returns exactly the 3 Harris
estimates), `search_bills` query "Mesa Vista" or "4C" (returns the 4 vendor bills), `search_records` on
`tblMaintenanceTickets` query "Mesa Vista" (returns both 4C turn tickets), `search_threads` query
"make-ready" (returns thread `66132537181ecbe1`), and `list_events` across carlos.mendez@starpm.com and
wesley.tran@starpm.com (returns `0hjw400xgjb3j7ay7ynuaqbnpi`). Each was confirmed by simulating the query
against the split.

**S3 consequence:** an evidence field may cite any of these records, because a trajectory following the
OE chain can now actually contain them. Before adding any NEW record to an evidence field, check that
some step in the OE chain retrieves it.

## 6. Two further S3 cautions from the closing council round

**Gmail identifier convention is mixed.** `2ae48555b3009a95` is a MESSAGE id (its thread is
`621640f9e7aa6d46`); `66132537181ecbe1` is a THREAD id (its message is `5101c5a41dffa90a`). `get_thread`
takes a threadId. Both are reachable, so nothing is broken, but S3 should quote content rather than
either id in an evidence field.

**F7 caution on Sunset Ridge 309C.** That unit carries TWO `selSched` rows. Only `rec987aae7d522057` is
graded; `reca06d89f1a4ac5b` must be left alone. Pin the graded row by content, the deep-clean crew
question answered on two later rows, never as "the 309C scheduled row", which matches both.

## 7. Two notes carried from the closing Oracle review

**OE 13's "returns three events" depends on the search model.** `list_events` with `fullText "Harris"`
across brooke, patricia and teresa returns **3** base events if the harness matches on summary,
description and location. It returns **4** under Google's `q` semantics, because
`vwdtvhm1y7ukp2v2vm5ytr9dpi` "Mitchell Eviction Case-Prep Review" matches only via the attendee address
`harry.harris@gmail.com`. AUDIT disclosed this and declined it on universe-grounded reasoning, which is
legitimate, and the step's conclusion does not depend on the count. **S3 must not write a criterion
that grades the number of events returned by that call.** Grade the records the step reaches, not the
size of the result set.

**Gmail identifier types differ between two steps.** `2ae48555b3009a95` is a MESSAGE id whose thread is
`621640f9e7aa6d46`; `66132537181ecbe1` is a THREAD id whose message is `5101c5a41dffa90a`. `get_thread`
takes a threadId. Both are reachable. Quote content rather than either id in an evidence field.
