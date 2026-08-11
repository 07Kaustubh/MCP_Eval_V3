# FINAL Council — Cross-Artifact Holistic Review (Round 2)

**Task:** `Generated_Tasks/2_6a6beba55996ad2ada369b15`
**Universe:** harmonygames (framework `hg`, single-model) · **Model under test:** Claude Opus 4.7 · **Today:** 2026-02-28 America/Chicago (Saturday, month-end, mid-Q1)
**Date:** 2026-08-07 · **Round:** 2 · one REVISE applied in place and re-gated

**VERDICT: PASS**

---

## Why this round ran

Round 1 closed `PASS` at 02:44 against a 25-criterion / 26-OE artifact set. Both deliverables were
then edited outside the phase (`6_Oracle_Events.txt` 06:31, `7_Rubrics.json` 06:45) into a 27-OE /
35-criterion set, and nothing re-gated them. This round treats the on-disk artifacts as the subject
and re-derives every claim from `Services_Data/`. Round 1's findings are not carried forward as
evidence. Three defects introduced by those edits, and one the edits inherited, are recorded below.

Final shape: **28 OEs / 32 criteria**.

---

## Deterministic gates (all re-run on the corrected set)

| Gate | Result |
|---|---|
| `check_hydration.py` | `[OK] harmonygames: payload hydrated and matches its manifest` |
| `phase_ready.py --phase final` | `[OK] all 5 upstream artifacts present`; eval hashes 24/24 against the pinned baseline |
| `validate.py --phase prompt` | PASS · 0 fails, 0 warns |
| `validate.py --phase oe` | PASS · 0 fails, 0 warns |
| `validate.py --phase rubrics` | PASS · 0 fails, 0 warns · `Outcome 1.1=3, Outcome 1.2=25, Outcome 2.1=3, Process=1` · 0/32 Major, 0/32 Moderate+, 0/32 with any issue |
| `validate.py --phase injection` | PASS · task injects nothing (`4_Changelog.json` = `[]`) |
| `validate.py --phase submission_gate` | PASS · census 31 outcome / 1 process / 32 |
| `check_rubric_antipatterns.py` | `[OK] no construction anti-patterns found` (32 criteria x 3 fields) |
| `check_oe_rubric_sync.py` | `[OK] OEs and rubrics agree on required content` (28 OEs / 32 criteria) |
| `check_ordering_coverage.py` | `[OK] 1 Process rubric grades ordering` |
| `check_qc_binary.py` | `[OK] all 6 measurable binary sub-dimensions pass` |
| `check_persona_acl.py` | 0 findings |
| Rubric census | 32, under the 60 ceiling. Process 1/32 = 3.1%, under the flat 40% HG cap |

`check_rubric_signal.py` SKIPs — no verifier export exists until S4.

---

## LENS 1 — Truthfulness

Every load-bearing figure was recomputed from `Services_Data/` directly, not read from
`Fact_Ledger.json` and not accepted from S2 or from round 1.

| Claim | Recomputed | Match |
|---|---|---|
| DAU window 2026-01-05..2026-02-09, 72 rows / 36 dates | identical | yes |
| 45 first day; peak 801 on 02-07; 784 on 02-08; 783 on 02-09 | identical | yes |
| 845 lifetime new users; 55,101 lifetime sessions | identical (`total_sessions`) | yes |
| D1 44.0 / D7 22.1 / D30 11.0; D1 range 37.34..50.73 | 44.0 / 22.0996 / 10.9922; 37.34..50.73 | yes |
| REVENUE_DAILY combo_fighter: 72 rows, all three revenue columns and paying_users sum to 0 | identical | yes |
| IAP_TRANSACTIONS combo_fighter: zero rows | identical | yes |
| AD_SPEND_DAILY combo_fighter: 330 rows, 2026-01-05..2026-02-28, 7,483.42, 1,341 installs, 110,531 impressions, 3,904 clicks | identical | yes |
| Six-channel split (2,265.43 / 1,355.97 / 1,318.85 / 1,070.33 / 742.91 / 729.93) | identical | yes |
| Spend inside the engagement window: 5,039.34 | identical | yes |
| All titles after 2026-02-09: 280 rows, 8,452.64, split 5,569.66 / 2,444.08 / 438.90 | identical | yes |
| Including 2026-02-09: 298 rows, 8,922.12 | identical | yes |
| 2026-02-28: 17 rows, 346.00, combo_fighter 160.88 | identical | yes |
| CASH_BALANCE 2026-02-28: cash 2,500, burn 22,500, runway 0.1, headcount 6 | identical | yes |
| REVENUE_DAILY_V2 1,636 rows / 0 combo_fighter; UA_SPEND_UNIFIED_V2 4,313 rows / 0 combo_fighter | identical | yes |

All 21 cited Slack timestamps were opened and the quoted text matched byte for byte, including the
22,500 / 11,700 offer line, the sale-to-licence pair, the R&D supersession chain, the 15,000 Sunset
cost, the consolidated action list and the free-tier Slack decision. `#winddown` spans
2026-02-09 18:53 to 2026-02-13 19:40 across 212 messages with the authorship split the OE states.
Leonard Hayes and Arthur Blake resolve to the roster emails rather than to constructed ones.
Confluence `COMPANY`, Linear `team_ENG` and Trello list `670015c2ecd45b634d5eec81` are real rows.

**Answer leakage: clean.** `10,800` and `8,452` return zero word-boundary hits across every
Robert-reachable Slack channel and across all 16,249 threads in his mailbox. `11,700` appears once,
in an unrelated news digest reading "11700 Votes". The gross 22,500 is present, which is the point of
the lever.

**One truthfulness defect found and fixed — see BLOCKER-1.**

---

## LENS 2 — Rubric binding

Atomicity, self-containment, tight/loose and category correctness walked per criterion. Two defects
found (BLOCKER-2, MAJOR-1); everything else clears.

- **Self-containment**: every pinned value sits in the `title`. Hiding `justification` and `evidence`
  leaves each acceptance target intact.
- **Too-loose scan**: `approximately` appears only on the wind-down service cost, whose sources are
  `~$15K` and `$13,000 to $15,000` — genuinely rounded at source, which is the one case
  `Docs_harmonygames/12_Always_Failing_Rubrics.md` permits. No `(or similar)`, no `at least N`,
  no `such as` / `e.g.` / `for example` in any field.
- **Too-tight scan**: criterion 1 accepts a page or a document; criterion 19 accepts an issue tracker
  or a task board; criterion 14 pins `#winddown` only because the prompt names it.
- **Negative-criteria gate**: the six exclusion criteria are affirmative on the Agent's verb
  ("The Agent leaves X outside…", "The Agent keeps A distinct from B"). No `does not` / `never` /
  `fails to` on an Agent verb anywhere.
- **Evidence convention**: grading instructions, not `Per OE#` back-references. Confirmed against the
  shipped QC_Passed HG reference task; FINAL.md's `Per OE#` line is a Brookfield convention.
- **No tool name in any title.** Snowflake table identifiers in criteria 27 and 28 are data objects,
  not tools.

---

## LENS 3 — Cross-artifact holism

**Forward map.** Every prompt ask reaches at least one OE and at least one criterion.

| Prompt ask | OEs | Criteria |
|---|---|---|
| whole life of the game, how it performed, what we paid | 4-9 | 2, 3, 4, 5 |
| don't smooth it out | 4, 5 | 3 (the zero), 5 (the strong side) |
| what is still quietly running, with a figure and an owner | 10-13 | 6, 7, 29 |
| does the money cover an orderly shutdown, be precise | 14-22 | 8, 9, 10, 11, 12, 13, 25, 26, 30, 31 |
| write it up somewhere durable | 24 | 1 |
| post it to Leonard and Arthur in the wind down channel | 25 | 14, 15, 16, 17, 18 |
| file a tracking item for what is still costing us | 26 | 19, 20, 21, 22 |
| tell me the two or three figures to lead with | 27 | 23, 24 |
| ordering ("Write it up … Then post it") | 24 before 25 | 32 |

**Reverse map.** Every criterion traces back to a prompt sentence. The two that needed the closest
look are 27/28 (versioned marts), which answer "go back to the real numbers … work out how it
genuinely performed" — citing a mart that excludes the title as evidence of no revenue is a wrong
answer to that ask — and 31 (licensing), which answers "I know roughly what we are getting for the
data" and is required decoy coverage under the Rubrics-Eval Exclusion / Decoy hard gate.

**Lever map** (`_aux/Hardness_Plan.md`):

| Lever | Prompt sentence | OE | Criterion |
|---|---|---|---|
| L11 net-vs-gross | "I have been carrying a number around in my head that I am no longer confident in" | 14 | 8, 9 |
| L2 Snowflake FINANCE skip | "whether that genuinely covers shutting down in an orderly way" | 21 | 10 |
| L8 multi-link chain | "Tell me where that actually leaves us and be precise about it" | 22 | 12, 13, 25 |
| L10 supersession, hop 1 | "I know roughly what we are getting for the data" | 15 | 31 |
| L10 supersession, hop 2 | (vendor keep/cancel) | 13 | 29, partially |
| L7 multi-write | "Write it up … Then post it … and file a tracking item" | 24, 25, 26 | 1, 14, 19 |

**L10 is better carried than in round 1.** Round 1 recorded hop 1 as graded only indirectly and hop 2
as carrying no criterion at all. Criterion 31 now grades hop 1 directly and criterion 29 grades the
decoy side of hop 2. Hop 2's full keep/cancel disposition still carries no criterion, and that
remains correct: the prompt never asks for it, so a criterion would be beyond-prompt.

**Entity map.** Robert (`robert@harmonygames.co`, `U04TWDMDT0V`, `EMPLOYEE_0016_SLACK_ID`), Leonard
Hayes and Arthur Blake are the same entities in all three artifacts. Combo Fighter is the single
target title; `#winddown` / `C0ADGSZKR3R` is the single target channel. No drift.

**Density.** Projection unchanged at 41-55 calls, midpoint ~48, across slack, snowflake, gmail,
confluence or gdocs or gdrive, linear or trello, and contacts — **6 distinct services**. Against the
HG authoring target of 40+ calls and 3+ services this is **PASS**, and the necessary-call subtotal of
~28-33 clears the prompt-eval gate of >15. The QC floor of >=15 average clears with wide margin. The
round-2 edits removed four criteria but no discovery step, so no call was removed from the path.
Per the banked HG calibration, HG realises **above** projection (task 1 projected 75 and measured
150.2), so the midpoint is quoted raw and not adjusted downward.

---

## LENS 4 — Red-team adversarial

- **Shortcut path?** No. Reading only `#winddown` yields the 22,500 gross and never the cash position,
  so criteria 10, 12 and 13 fail together. Deriving 10,800 without querying `FINANCE.EXPENSES` fails
  criterion 10 and leaves the coverage arithmetic without its second term. At least two levers have
  to fire for the set to pass.
- **Second valid reading that flips a write?** No. The three writes are all creations, the destination
  is explicitly open for two of them and named by the prompt for the third.
- **Correct figure recoverable from one obvious search?** No. 10,800 exists nowhere in the universe;
  it survives only as a subtraction across two figures in one sentence, set against a cash balance in
  a different service.
- **Can the coverage conclusion be flipped by a defensible reading?** Checked explicitly, because
  removing the Singular and Unity criteria widened the space of grounded readings. The narrowest
  reachable cost total — wind-down at 13,000 plus Singular at the vendor's 6,250 plus Unity at
  ~21,000 — is 40,250 against funds of 13,300. Even zeroing both vendors leaves 13,000 of wind-down
  cost plus 9,722.90 of Deel arrears against 13,300, and the record's last word on both vendors
  (ts 1770911000.728559 and the 2026-02-13 action list) is that they still have to be settled, so
  zeroing them is not a grounded reading in the first place. **Criterion 13's direction holds on
  every combination.** OE 22's ratio claim was corrected from "more than three times" to a range,
  because the narrowest reading lands at 3.03x and the original phrasing had no margin.
- **Drift sweep.** Zero em-dashes in all three files. Zero tool names in rubric titles. Zero
  Keystone / MoveOps / Brookfield tokens (`mortgage_los`, `stripe`, `@keystonemortgage.com`,
  `oracle_gl`, `records_vault`). No `at least N`.
- **Weekend rule.** Today is a Saturday. No criterion dates a communications write to 2026-02-28;
  `submission_gate` P2 enforces this and returns 0 fails.
- **Calendar sweep (hard rule 13).** `gcal.events.json` and `gcal.calendars.json` are 3 bytes each,
  so no confirmed future event can contradict a completeness claim. Cleared manually, since deviation
  HG-U11 leaves `v4_gates.py` F9 unavailable for HarmonyGames.

---

## LENS 5 — Narrative-state + action-prescription + tool binding

- **Narrative state.** The prompt's "We decided to stop on the ninth and I have watched us cancel
  things since" matches the 2026-02-09 shutdown decision and the 02-11 to 02-13 cancellation traffic.
  The 15-day gap between the last Slack message (02-13) and today (02-28) is handled as "where did we
  land", never as fresh news. Nothing in the prompt claims an in-progress state the records show as
  closed, or the reverse.
- **Action prescription.** The prompt's three writes do not contradict any record-prescribed action.
  The 2026-02-13 action list assigns cancellations to Leonard and Arthur; the prompt asks Robert for
  an account, a post and a tracking item, none of which is assigned elsewhere.
- **Tool-parameter binding.** All 22 tools named in the OE resolve in
  `6_Server_Tools_Details.json`, and every parameter the OE binds is on that specific tool:
  `slack_search_channels(query, include_private)`, `slack_conversations_history(channel_id, cursor)`,
  `slack_read_channel(channel)`, `slack_conversations_search_messages(search_query, filter_in_channel)`,
  `snowflake_execute_query(sql)`, `snowflake_list_schemas(database)`, `snowflake_list_tables(database)`,
  `confluence_create_page(space, title, body, bodyFormat)`, `gdocs_create_document(title, bodyText)`,
  `gdrive_create_file(name, content, mimeType)`, `slack_send_message(channel, text)`,
  `slack_conversations_add_message(channel_id, payload)`,
  `linear_create_issue(team, title, description, assignee)`, `trello_create_card(idList, name, desc)`,
  `slack_search_users(query)`, `contacts_search_contacts(query)`, and the three `gmail_*` readers.
  Zero misbindings. The two Slack send tools are correctly kept apart on `text` versus `payload`.
- **Lifecycle preconditions.** All three writes are creations into unlocked destinations. No closed
  period, no locked record, no expired SLA.

---

## LENS 6 — Verifier-fails-spec pre-upload simulation

Every criterion was classified for what its failure would mean. After the fixes, **0 of 32 (0%)
surface as Bucket_1_Risk**, against a 20% ceiling. Before the fixes the count was 5 of 35 (14%) —
under the ceiling but carrying two criteria that could not fail at all, which the percentage test
cannot see.

Residual notes, neither blocking:

- **Criterion 5 is a four-way accept set** (801 peak DAU, 845 new users, 55,101 sessions, 44.0% D1).
  This is Overly Broad, which is Moderate under the HG ladder. It is kept because the prompt asks for
  the engagement side without naming a figure, and OE 24 authorises the disjunction. Expect it to pass
  on most runs; a 6/6 there is not evidence of judge lenience.
- **Criterion 8 is subsumed by criterion 9.** An account that distinguishes 22,500 from 10,800 must
  state 10,800, so 9 passing implies 8 passing. The reverse is not true, so the pair is a genuine
  partial-credit split rather than a duplicate. Flagged for the S4 passing-cell audit
  (`check_criterion_dependencies.py`), not for removal.

---

## Findings

### [BLOCKER-1] OE 20 asserted a Singular reconciliation the mailbox does not contain

The step claimed "three Singular past-due invoices at 6,250 each, which reconciles to the 18,750
stated in Slack". Robert's mailbox contains **one** Singular past-due thread of six messages. Its two
dunning messages, 2026-01-05 and 2026-01-15, each state "the total outstanding amount on your account
is $6,250.00" with an overdue amount of the same. There are two Singular invoices in the mailbox at
all, `INVSINC22671` of 2025-09-01 and `INVSINC23580` of 2025-11-30, and **`18,750` returns zero
word-boundary hits across all 16,249 threads**. There are no three invoices and no reconciliation.

**Applied.** OE 20 now states what the thread actually contains: the 6,250 outstanding figure, the
vendor's extension of the due date to 2026-03-15, Leonard's 2026-02-12 insolvency reply asking for a
clean mutual early termination that Singular never answers, and the two real invoice numbers. It also
states the relationship to Slack honestly — 18,750 is Leonard's forward statement of what the
contract still costs, the mailbox states only what was overdue in January, and the divergence is a
scope difference rather than a contradiction.

### [BLOCKER-2] Criterion 11 pinned 18,750 against a reachable source stating 6,250

Consequence of BLOCKER-1. OE 20 sends the agent into the mailbox as a corroborating surface; the
mailbox states 6,250 outstanding and an unanswered request to write the balance off. An agent that
sweeps Gmail as the OE intends and reports Singular at 6,250, or as unconfirmed, was failing a
criterion pinning 18,750 while being correctly grounded in the persona's own records. That is
Bucket 1, and it is also the shape the binary sub-dim *Universe / Cross-service Coherence* penalises.

Criterion 12 (Unity at approximately 21,000) carries the same class of weakness from a different
direction: the sole source is the unit-less product `~2.348*9 months`, and Gmail contains no Unity
obligation record at all.

Three independent grounds converge on removal rather than widening:
1. The prompt says "**I know who we still owe**". Restating a vendor balance the persona says he
   already knows is not a distinct prompt ask; the ask is the coverage verdict, which criteria 13, 17
   and 25 carry.
2. **OE 24's content-element list — the authoritative decompose directive for the written account —
   never listed Singular or Unity.** Under AGENTS.md rule 14 the criteria were the drift, not the OE.
3. AGENTS.md rule 21 sets removal as the default for a criterion that cannot be defended unprompted,
   and rule 14 puts Bucket-1-flagged and beyond-prompt criteria first in the cut order. Neither is a
   lever carrier.

Widening criterion 11 to accept either figure was considered and rejected: it would manufacture an
Overly Broad criterion (Moderate under the HG ladder) that grades nothing, and
`Docs_harmonygames/12_Always_Failing_Rubrics.md` forbids loosening an exact source value as the way
out of a split.

**Applied.** Criteria 11 and 12 removed. OE 16 now states explicitly that Singular and Unity are
named, reachable, and deliberately carry no criterion, with the reason for each, so a later phase
does not re-add them.

### [BLOCKER-3] Rubric `category` had been downgraded off the spec enum

All 35 criteria on disk carried `outcome` / `process`. `Evals_harmonygames/3_Rubrics_Eval.md` line 7
and its Phase 1.2 HARD GATE both state that the only valid values are `Outcome 1.1`, `Outcome 1.2`,
`Outcome 2.1` and `Process`, and Phase 5.0 names "one category mislabel" as a single-blemish
score-4 pattern. The round-1 artifact carried the correct enum; the post-FINAL edit replaced it with
the legacy two-value form.

The shipped `QC_Passed` HG reference tasks do use the lowercase form, which is why
`universes.py` accepts both — but the graded spec asks for the enum, and `check_qc_binary.py` and
`validate.py` now canonicalise correctly, so shipping it costs nothing.

**Applied.** Enum restored across all 32 criteria: `Outcome 1.1` on the three write-action results
(page created, message posted, tracking item filed), `Outcome 1.2` on the twenty-five action-content
criteria, `Outcome 2.1` on the three final-response criteria, `Process` on the ordering criterion.
`validate.py --phase rubrics` and `check_qc_binary.py` both re-run clean.

### [MAJOR-1] OE 8 contradicted criterion 4 and OE 24 on the acquisition window

OE 8 read: "Both are grounded readings, so an account that scopes spend to the engagement window is
defensible". Criterion 4 and OE 24 both pin 7,483.42 across 2026-01-05 to 2026-02-28. An agent that
followed OE 8's "defensible" scoping to 5,039.34 would fail criterion 4 — a per-rubric cross-artifact
mismatch, and the sharpest Bucket-1 shape in the set.

The prompt settles it: it asks for the record "to the last day there is anything to look at", and
OE 9 exists precisely to establish that this day differs by table — 2026-02-28 for acquisition
spend, 2026-02-09 for engagement and revenue. Criterion 4 is right and OE 8's sentence was the defect.

**Applied.** OE 8 now resolves the window against the prompt's own phrasing, names 7,483.42 with its
window as the figure to carry, and describes 5,039.34 as a correct arithmetic reading of a narrower
question the prompt does not ask.

### [MAJOR-2] Criterion 29 bundled two independent marts

"leaves `REVENUE_DAILY_V2` **and** `UA_SPEND_UNIFIED_V2` outside…" is two independently pass/fail
claims in one criterion, which the Atomicity Decomposition HARD GATE scores Major.

**Applied.** Split into two atomic criteria, one per mart, each naming the specific evidence claim it
guards (no revenue data / no spend data).

### [MAJOR-3] Criterion 30 graded a record the persona cannot read

"leaves the 12K third-party fiduciary line in direct message D04UC0UEN2V outside the account."
D04UC0UEN2V's member array is `U04SNNV580G` / `U04UP2L1RUY`; Robert is `U04TWDMDT0V` and is not in it.
Under persona-scoped Slack reads the message is invisible, so the criterion could not fail on any run
— it embedded an unobservable value, which `Evals_harmonygames/3_Rubrics_Eval.md` scores as wrong
scoring outright, and `Docs_harmonygames/14_Persona_ACL.md:129` states that inaccessible content
cannot be required ground truth, with `:134` forbidding an ACL denial being made necessary to a
rubric.

**Applied.** Criterion removed. OE 17 keeps the 12K as a reachability note, now with the member arrays
quoted, and states explicitly that it carries no criterion and why.

### [MAJOR-4] Criterion 34 graded an action the tool catalog does not expose

"The Agent confines Gmail activity to reading for this task." All 27 `gmail_*` tools read, label or
trash; there is no send, reply, compose or draft tool. The criterion could not fail. It also had no
prompt provenance — the prompt never mentions email — which the Requirement Provenance HARD GATE
scores as Incorrect (Major) for an OE-only requirement.

**Applied.** Criterion removed. OE 20 now states that Gmail's read-only nature is a property of the
catalog rather than of the agent's judgement and therefore carries no criterion.

### [MAJOR-5] Two criteria were not mirrored into their OE decompose directives

Criterion 9 (holding the 22,500 gross and the 10,800 net in their own roles) and criterion 25 (the
final-response coverage verdict) are both squarely prompt-authorised — the first by "I have been
carrying a number around in my head that I am no longer confident in", the second by "Tell me where
that actually leaves us and be precise about it". Neither appeared in OE 24's or OE 27's
"must carry, as separate elements" list, which is the drift AGENTS.md rule 14 forbids.

**Applied.** The gross/net distinction added to OE 24's element list; OE 27 rewritten to carry an
explicit three-element list including the coverage verdict with its authorising prompt sentence
quoted. A new **OE 28** enumerates the five reachable decoys that carry exclusion criteria and names
the two items that deliberately do not (the 12K and Gmail send discipline), so the reasoning behind
MAJOR-3 and MAJOR-4 survives in the artifact rather than only in this report.

### [MINOR-1] OE 19 misquoted the meeting-notes subject line

The OE gave the subject as `"Notes: Harmony Games Wind Down Feb 11, 2026"`. The real subject nests
curly quotes inside itself. **Applied** — OE 19 now describes the subject rather than misquoting it.

---

## Hard-rule table — evidence

| Rule | Verdict | Evidence |
|---|---|---|
| Derived answer never stated verbatim in any read surface | PASS | 10,800 and 8,452: zero word-boundary hits across every reachable Slack channel and all 16,249 Robert Gmail threads |
| Every tight identifier exists in the universe | PASS | Lens 1 table; all 21 Slack timestamps, both Confluence/Linear/Trello anchors, both roster emails; zero phantoms after BLOCKER-1 |
| Every Hardness lever still triggered end-to-end | PASS | Lens 3 lever map; L10 hop 1 now directly graded, which round 1 recorded as PARTIAL |
| Integrated density | PASS | 41-55, midpoint ~48, 6 services, against the HG 40+ target and the >=15 QC floor |
| Category balance; no tool name in a title; no em-dashes | PASS | 31 Outcome / 1 Process (3.1%, cap 40%); zero tool names; zero em-dashes |
| Entity references consistent across all three artifacts | PASS | Lens 3 entity map |
| Implicit-prompt framing preserved | PASS | no criterion demands an investigation step the prompt forbids |
| Narrative-state consistency | PASS | Lens 5 |
| Action-vs-universe-prescription | PASS | Lens 5 |
| OE tool-parameter binding exact per tool | PASS | 22/22 tools, every parameter on the named tool |
| Lifecycle preconditions | PASS | all three writes are creations |
| Bucket_1_Risk <= 20% | PASS | 0% after fixes (14% before, plus two criteria that could not fail at all) |
| No criterion dates a communications write to 2026-02-28 | PASS | `submission_gate` P2, 0 fails |
| 60-criterion cap | PASS | 32 |
| Calendar sweep (hard rule 13, manual for HG) | PASS | gcal is empty universe-wide |

---

## Files changed by this council

- `7_Rubrics.json` — 35 to **32**. Category enum restored on all criteria. Removed: Singular 18,750,
  Unity ~21,000, the 12K fiduciary exclusion, the Gmail read-only exclusion. Split: the versioned-mart
  exclusion into two atomic criteria. Evidence wording normalised on the exclusion set. No criterion
  merged, so no F8 NON_ATOMIC_ENUM was manufactured. No criterion carries a numeric cross-reference,
  so renumbering is safe.
- `6_Oracle_Events.txt` — 27 to **28** steps. OE 8 (window resolution), OE 16 (Singular/Unity carry no
  criterion), OE 17 (12K member arrays + no criterion), OE 19 (subject line), OE 20 (Singular thread
  corrected), OE 22 (cost-ratio claim made robust), OE 24 (gross/net element added), OE 27 (rewritten
  with a three-element list), **new OE 28** (decoy criterion map).
- `5_Prompt.txt` — **unchanged**.
- Pre-edit originals for this round preserved at `_aux/7_Rubrics.prefinal_r2.bak.json` and
  `_aux/6_Oracle_Events.prefinal_r2.bak.txt`.

## Carry into S4

1. **Criterion 5 is a four-way accept set.** A 6/6 there is expected and is not evidence of lenience.
2. **Criterion 9 implies criterion 8.** Run `check_criterion_dependencies.py` once the verifier export
   exists and audit that pair's passing cells, not only its failing ones.
3. **No Singular or Unity figure is pinned by design.** If a trajectory reports either and a grader
   marks it, that is a grader artefact, not a criterion.
4. **Density projection assumes the Gmail sweep.** HG has historically realised 1.5-2x above
   projection; if runs land at the low end of 41-55, check whether Gmail was skipped before
   attributing it to the task.
5. **L10 hop 2 (the full vendor keep/cancel disposition) still carries no criterion**, by prompt
   design. If the trajectories show agents tripping on it, that is unmeasured difficulty, not a gap.
6. **Universe / Cross-service Coherence** is the one binary sub-dim that cannot be settled before
   trajectories exist. The Slack-versus-Gmail Singular divergence is the specific thing to watch: it
   is documented in OE 20 and deliberately ungraded, but if it causes a run to fail outright, that
   sub-dim is in play.

---

## Addendum: platform rubric linters, 2026-08-07 (post-PASS)

Four rubric linters were run after this council closed. Two returned PASS (Not More Specific Than
Prompt; Prompt Requirement Coverage). Two returned findings, both against criteria this report had
already flagged as its residual risks. Responses are recorded in `_aux/Linter_Justifications.md`;
every gate was re-run afterwards and all return 0 fails / 0 warns. Criterion count unchanged at 32.

### Unrequested Scope (FAIL) — accepted, criterion 26 rewritten

The linter flagged *"The Agent leaves the 24,275 R&D tax credit outside the funds available for the
wind down"* as testing a subject the prompt never raises. **The linter is right, and this council had
the framing wrong.** The Rubrics-Eval Exclusion / Decoy Coverage hard gate says decoys must be
penalised, and this report cited it to justify the exclusion set; but the eval's own instruction is to
*"express them affirmatively"*, and an affirmative expression of this decoy does not need to name it.

Rewritten to grade the correct end-state instead of the decoy's absence:

> The Agent's written account puts the funds available against the wind down at 13,300.

13,300 is 10,800 net proceeds plus 2,500 cash. Discrimination is preserved and arguably improved: an
agent that swallows Leonard's *"This $25K is great if we can get it"* framing puts funds available near
37,575 and fails on the figure, without any criterion naming a subject the persona never raised.
Leakage re-checked: `13,300` returns zero hits across every reachable Slack channel and Robert's
mailbox, apart from one marketing URL tracking code. Mirrored into OE 18, OE 24 and OE 28.

**Carry-forward rule:** an exclusion criterion should be written as the positive figure or
classification the decoy would corrupt, not as the decoy's absence. Naming the decoy imports its
subject into the graded scope.

### Atomicity (FALSE) — one accepted, one dismissed

**Accepted, criterion 5 rewritten.** The four-way engagement disjunction is the item this report
recorded under Lens 6 as Overly Broad (Moderate on the HG ladder) and kept. The linter reaches the
same conclusion by the atomicity route, and the HG eval's own atomicity gate names quantifier-based
bundling explicitly. Now:

> The Agent's written account states that Combo Fighter's daily active users peaked at 801 across
> both platforms.

`across both platforms` is load-bearing and was added after checking the source: 801 is the combined
ios and android peak on 2026-02-07, while the per-platform maximum is **426**, on android, on
2026-02-08. Without the qualifier the criterion would turn on an aggregation the reader has to guess.
Under the HG ladder this trades a Moderate for at most a Minor. OE 24's content list narrowed to match.

**Dismissed, criterion 23 unchanged.** The linter reads *"two or three figures"* as a non-atomic count
range and asks for "at least two" or "exactly three". The prompt's closing line is *"Then tell me the
two or three figures you would lead with"* — the range is the user's, and pinning it would breach the
Prompt Specificity Ceiling hard gate, which forbids any field imposing a narrower requirement than the
prompt. The criterion makes one claim (the count falls in the range the user named) and fails cleanly
on one, four or none. Groundedness of each figure is criterion 24's job. Reviewer-facing text is in
`_aux/Linter_Justifications.md` and clears `check_justification.py`.

### Net effect on this report's residual notes

Lens 6's first residual note (criterion 5 as a kept Overly Broad) is **closed**. The second (criterion
8 subsumed by criterion 9) stands. A new note replaces the first: criterion 26 now pins a summed
figure, so an account that states 10,800 and 2,500 without printing the total is the one shape that
could fail it unfairly. Watch that cell at S4 before treating a failure there as legitimate.

---

## Addendum 2: Unrequested Scope, second pass (2026-08-07)

The scope linter re-fired on the versioned-mart criteria. **Accepted.** The carry-forward rule stated
in Addendum 1 was written and then not applied to the rest of the exclusion set in the same pass; that
was the error, and this addendum applies it. **32 to 29 criteria.**

| Was | Disposition | Why |
|---|---|---|
| leaves `ANALYTICS.MONETIZATION.REVENUE_DAILY_V2` outside the revenue evidence set | **REMOVED** | The only wrong end-state the mart produces is "Combo Fighter has no revenue data". Criterion 3 already requires the account to state 0.00 revenue, which contradicts it. Redundant, and it named a warehouse object the prompt never raises. |
| leaves `ANALYTICS.MARKETING.UA_SPEND_UNIFIED_V2` outside the spend evidence set | **REMOVED** | Same, against criterion 4's 7,483.42. |
| keeps the 22,500 monthly net burn distinct from the 22,500 gross data offer | **REMOVED** | Zero signal. An agent that meets the burn value in the cash row still reports the offer as 22,500 and the net as 10,800, so no graded value moves either way. It carried an out-of-scope subject for no discrimination (AGENTS.md rule 28). |
| leaves Metabase and dbt outside the set of costs still running unaddressed | **REWRITTEN** | The point is prompt-raised: *"that list got put together fast and nobody has been back over it properly."* The two vendor names were not. Now: *"The Agent's written account identifies continuing paid user acquisition as the cost still running that the cancellation list does not cover."* Asks about the list the user raised, keeps the discrimination, drops the unnamed subjects. |
| describes the data transaction in its licensing form rather than as an outright sale | **KEPT** | The only member of this family whose subject the prompt raises directly, in *"I know roughly what we are getting for the data"*. Describing a prompt-named record in its superseded form is a wrong statement about that record, not a new subject. |

### Decoy coverage after the cuts

The HG Exclusion / Decoy Coverage hard gate is still satisfied, affirmatively, which is what it asks
for. Every decoy is now graded through the value it would corrupt: the marts through 0.00 and
7,483.42; the R&D credit through the 13,300 funds figure; Metabase and dbt through the
still-running-cost identification. Only the sale-versus-licence decoy carries a criterion naming it,
and its subject is prompt-raised.

**Generalised rule, now applied consistently across the set:** a decoy earns a criterion of its own
only when the prompt raises its subject. Otherwise grade the figure or the identification the decoy
would corrupt, and record the mapping in the oracle events so the criterion is not re-added later.
OE 28 now carries that mapping explicitly.

### Gates after the change

All five validator phases and all five supporting checkers re-run: 0 fails, 0 warns. Census 28
Outcome / 1 Process (3.4%, cap 40%), 29 of 60. Zero em-dashes. Density unaffected: no discovery step
was removed, OE 7 still sends the agent at the marts, and the trajectory projection stands at 41 to 55
with a midpoint near 48 across 6 services.

### Effect on coverage

No prompt ask lost a carrier. The three removed criteria were each fully subsumed by a sibling that
grades the same wrong answer from the affirmative side. The forward map in Lens 3 is unchanged except
that the "what is still quietly running" row now reads criteria 6, 7 and 27 rather than 6, 7 and 29.

---

## Addendum 3: overlap linter (2026-08-07)

The overlap linter flagged the pair this report had already recorded under Lens 6 as residual note 2:
*"Criterion 8 is subsumed by criterion 9… the pair is a genuine partial-credit split rather than a
duplicate."* **That call is reversed.** One-directional implication with no independent requirement is
redundancy, and calling it partial credit was a rationalisation. **29 to 28 criteria.**

**Which member was cut, and why the linter's suggestion was inverted.** The linter proposed removing
the weaker criterion (net proceeds = 10,800) and keeping the stronger (gross distinguished from net).
The opposite was done.

1. **The stronger criterion has a false-fail mode the weaker one does not.** An account reading
   *"the data agreement nets 10,800 after their 11,700 charge"* has given the gross implicitly, is
   complete and correct, and can still be marked down by a grader looking for both figures held in
   separate roles. `distinguishes A from B` is an interpretive verb; `states the net as 10,800` is
   binary. Under AGENTS.md rule 29, a criterion that flips on identical trajectories is a wording
   defect, and the softer verb is the one that flips.
2. **Nothing is lost, because the L11 lever is guarded three more times.** An agent latched on the
   22,500 headline fails criterion 8 (no 10,800 net), criterion 12 (15,000 is not greater than 22,500,
   so the comparison inverts) and criterion 26 (funds at 25,000, not 13,300). The gross-versus-net
   criterion was the fourth guard on an already triple-guarded point, and the least reliable of the
   four.

OE 24's element list dropped the gross-and-net-held-apart element in the same pass.

### Standing note on the remaining one-directional pairs

Three pairs of the same logical shape remain and are **deliberate**: criteria 1, 14 and 19 (the write
actions) are each implied by their content criteria, since an account cannot state a figure that was
never created. These are the guidelines' `Outcome 1.1` / `Outcome 1.2` split, and cutting the 1.1
member deletes the service anchor for that write. If the overlap linter fires on one of them, that is
the dismissal to write, not a cut.

### Lens 6 residual notes, current state

Both original residuals are now closed: note 1 (criterion 5's four-way accept set) by addendum 1, note
2 (this pair) by this addendum. The one live residual is the one addendum 1 opened: criterion 26 pins
a summed figure, so an account stating 10,800 and 2,500 without printing 13,300 is the shape that
could fail it unfairly. Watch that cell at S4.

### Gates

All five validator phases and all five checkers re-run: 0 fails, 0 warns. Census 27 Outcome /
1 Process (3.6%, cap 40%), 28 of 60. Zero em-dashes. Density unaffected.
