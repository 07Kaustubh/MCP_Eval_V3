# Council B — Adversarial QC + Density + Hardness Preservation (iteration 3)

**Deliverable:** `Tasks/46_6a62ccb6ce2323b4b9e0c8d8/5_Prompt.txt` (261 words, 4 paragraphs)
**Phase:** prompt · **Universe:** `starpm` · **Framework:** V4 (dual-model Opus 4.8 + Gemini)
**Universe today:** 2026-07-01 America/Chicago · **Density scheme:** V4 per-model, >= 40 PASS / 15-39 THIN / < 15 INSUFFICIENT
**Mode:** read-only. No deliverable modified.
**Round:** 3 of max 3. Iteration 1 BLOCK (UGT / QuickBooks reading). Iteration 2 GO — **wrong**, AUDIT F1 MAJOR.

## VERDICT: GO

AUDIT F1 is **closed**, and I verified the closure against the universe rather than against AUDIT's report. The reworded clause is measurably *less* assertive than the one it replaces, so it withholds more, not less. Two new MODERATE carry-forwards for S3, both pinning-shaped. One substantial new lever carrier surfaced on the Finley side that no prior phase recorded.

## First: what I got wrong at iteration 2

Two errors, both mine, both of the same family — I reasoned about an artifact instead of reading the universe.

**1. I accepted AUDIT F1's clause on a false binary.** I framed the L2-calendar attenuation as keep-versus-delete, concluded that deleting would make the calendar write beyond-prompt, and accepted. The trade analysis was fine. The question I never asked was what the phrase *denotes*. I have now measured it: `tblMakeReady.fldTurnStatus` distribution is **`selProg` 56 / `selSched` 43 / `selReady` 21** across 120 rows — an option literally named Scheduled covering 36% of rows — beside a date field literally named `Target Ready` (`fldTargetReady`). "Anything on the scheduling side… not properly settled" resolves there. Because "do the same" inherited the correction verb from the immediately preceding Airtable clause, an agent could discharge the entire clause inside Airtable and never open Calendar. AUDIT's numbers reproduce exactly. **The finding is correct and I should have caught it at iteration 1.**

**2. I repeated the Hardness Plan's calendar pin list without re-deriving it.** I asserted `1pon50ds1aevem63td6f7emdn3` and `qqbwq3s2h7wh5udoek2940mffk` as pinnable targets in both prior reports. Calendar stores one row per invitee calendar, so those base ids match **5** and **4** rows. This is precisely the failure hard rule 19 names: I cited an upstream phase's conclusion as though it were evidence about the artifact. Every calendar claim in this report was re-derived from `gcalendar.gcalendar_events.json` this session.

---

## The clause under review

Paragraph 3, before (iteration 2):
> "…put those records right rather than working around them, **and do the same for anything on the scheduling side for these two that is not properly settled.**"

Paragraph 3, after (iteration 3):
> "…put those records right rather than working around them. **Do the same for their review meetings if either of those did not end up properly settled.**"

Paragraphs 1, 2 and 4 are byte-identical to iterations 1 and 2. Re-read to confirm.

**Post-fix deterministic state (inherited):** 261 words · 0 em-dashes / 0 en-dashes (re-verified) · `validate.py --phase prompt` PASS 0 fails 0 warns 3 distinct services · similarity max composite 27.8 vs ceiling 40 · rule-23 ORDERING zero hits, so zero Process rubrics remains valid.

---

## [Q1] B2 second-reading attack on the new clause — **survives**

### What "their review meetings" denotes, measured

**Airtable has no referent.** Verified against `airtable.airtable_fields.json`:

| Table | Fields |
|---|---|
| `tblMakeReady` | `fldUnit` Unit · `fldTurnStatus` Status · `fldMoveOut` Move-Out Date · `fldTargetReady` Target Ready · `fldNotes2` Notes |
| `tblMaintenanceTickets` | `fldTicketNumber` · `fldDescription` · `fldPriority` · `fldCompletionDate` |

Fields matching `meet|appoint|calendar|event`: **NONE**. AUDIT's disambiguation reproduces.

**Calendar has an exact referent.** 219 event rows carry "Review" in the title across 44 distinct base ids. Filtering to owner surnames yields exactly five titles:

```
Harry Harris Mid-Year Portfolio Review
Harry Harris Mid-Year Portfolio Review (Rescheduled)
Robert Finley Mid-Year Portfolio Review
May Owner Report Review - Finley Properties
Linda Castillo Mid-Year Portfolio Review
```

### Attacks run

| # | Attack | Result |
|---|---|---|
| A | **Airtable discharge** — the F1 failure mode. Can an agent put a "review meeting" right inside `tblMakeReady`? | **FAILS.** No field carries a meeting concept. The 22 rows containing "meeting" hold it as free text in `fldNotes2`; editing prose *about* a meeting is not correcting a meeting. Airtable rows are keyed by unit, and the clause's possessive "their" binds to owners. |
| B | **Linear discharge** — are "review meetings" the Linear review items? | **FAILS.** A meeting is not an issue, and paragraph 4 separately and explicitly handles the Linear review item. The reading manufactures redundancy. |
| C | **The May near-miss** — Finley has two events with "Review" in the title. Can `ti5zt1xubdggbehtp79um9mim6` "May Owner Report Review - Finley Properties" (3 rows; Lisa **declined**, Teresa **declined**, Robert Finley accepted) be the target? | **Strongest attack, and it does not flip the write.** Paragraph 1 frames the whole task as "the mid-year owner reviews" and paragraph 4 says "the mid-year review item", so the discourse topic is the mid-year review, and both mid-year events carry the owner's full name plus "Mid-Year Portfolio Review" in the title. This is an *additional candidate touch* in the same service with the same intent, not a competing answer. Filed as MODERATE S3 pinning risk, not a UGT failure. |
| D | **"either of those" scope** — does the quantifier admit a wider set? | **It narrows.** "Either of those" presupposes exactly **two** review meetings, one per owner, which is true at the mid-year level and false for any reading that sweeps in the May report review or Linda Castillo's. The quantifier actively works against attack C. |
| E | **Cross-owner bleed** — "Linda Castillo Mid-Year Portfolio Review" exists. | **FAILS on the possessive.** "**their** review meetings" binds to "both of my owners" from paragraph 2. Castillo is Patricia's. Filed as a NOTE for S3. |

**Unique Ground Truth holds at 5/5.** The clause licenses one write intent on one service against a data-determined target set. Attacks C and E are S3 pinning burdens, the same class as "the mid-year review item" resolving against five Linear candidates.

### One structural note on why the fix works
The old sentence coordinated "do the same" with the Airtable clause inside a single sentence, so both verb *and* object were pulled toward Airtable. The new text ends the Airtable sentence with a full stop and opens a new one. "Do the same" still inherits the corrective verb — which is what authorises the write and must be preserved — but the object is a noun phrase with no Airtable referent. **The verb inherits; the object does not.** That is the correct surgical result.

---

## [Q2] Does the fix over-signal L10? — **No. It signals less than the clause it replaced.**

| L36 kill sentence for L10 | Present? |
|---|---|
| "the Harris meeting was rescheduled" | **No.** No owner named in the clause, no "rescheduled". |
| "check for duplicate meetings" | **No.** No duplication, count or comparison language. |
| "OPS-10 was never updated" | **No.** |

**The new clause is grammatically weaker than the old one.** Old: "anything on the scheduling side… **that is not properly settled**" — a restrictive relative clause, which *presupposes* that unsettled things exist. New: "their review meetings **if either of those did not end up properly settled**" — a conditional, which presupposes nothing. The agent must establish whether either is unsettled, and which.

It names no owner, no date, no defect, no state, no figure, no service. Prompt-wide: zero numerals (`\d+` returns empty), zero service names, zero tool names.

### The compensating discovery — L10 got harder, not easier

Measured this session, one row per invitee calendar:

| Event | base id | rows | on `lisa.smith` calendar? |
|---|---|---:|---|
| Robert Finley Mid-Year Portfolio Review (05-19 11:45) | `8mwlxrq5w5oodwdpmvo83e00f2` | 4 | **yes** |
| May Owner Report Review - Finley Properties (05-28) | `ti5zt1xubdggbehtp79um9mim6` | 3 | **yes** |
| Harry Harris Mid-Year Portfolio Review (06-02 12:15) | `1pon50ds1aevem63td6f7emdn3` | 5 | **yes** |
| Harry Harris Mid-Year Portfolio Review **(Rescheduled)** (06-03 15:00) | `qqbwq3s2h7wh5udoek2940mffk` | 4 | **NO** |

Lisa has a row on three of the four, and **not** on the duplicate. An agent that scopes Calendar to the persona — the most natural scoping for a persona-voiced prompt — finds Harris's mid-year review sitting on her own calendar, accepted by all four attendees, and concludes it is settled. The duplicate exists only on other people's calendars.

The retrieval difficulty therefore moved from "will the agent open Calendar at all" — which the old clause defeated anyway by routing to Airtable — to "will the agent search beyond its own calendar". That is a **better** discriminator, because it is a scoping error rather than a store-selection error, and scoping errors survive an agent that has already decided to use the service.

### A second L10 carrier, on Finley, that no prior phase recorded

`comment_79dc83838bd65d678c48b5911f942412` on OPS-10 (2026-05-17, Brooke) states:

> "Teresa has **Robert Finley's portfolio review locked in for the first week of June**, 60 minutes **in the afternoon**…"

The calendar holds exactly two Finley events, verified by exhaustive sweep: **2026-05-19 at 11:45** and 2026-05-28. There is **no first-week-of-June Finley event**, and 11:45 is not the afternoon. The record narrative describes a meeting that does not exist as described.

And the Finley mid-year review is itself unsettled on its face: **`lisa.smith` declined** her own owner's review, `aurora.winona` declined, and **Robert Finley is not an attendee at all** (attendees are Aurora, Brooke, Lisa, Teresa).

So "if **either** of those did not end up properly settled" fires on **both** owners — Harris by duplication, Finley by a declined-by-the-owner's-own-manager review that the parent issue misdescribes. The Hardness Plan modelled this lever as Harris-only. It is not.

---

## [Q3] B3 — density per model, and the conditional THIN risk

**The AUDIT-computed Opus floor of ~37-40 was conditional on the Airtable discharge and is now unreachable.** Under the old clause an agent could satisfy paragraph 3 entirely inside Airtable, losing the calendar sweep (5-8 Opus / 5-9 Gemini) plus one write and its supporting reads. "Their review meetings" has no Airtable referent, so that path no longer exists.

| Component | Driven by | Opus | Gemini |
|---|---|---:|---:|
| Base discovery: review item, C006, Brooke | para 4 | 6-9 | 6-10 |
| Owner enumeration x2 across 4 workstreams | para 2 | 10-14 | 12-18 |
| QuickBooks sweep (reads only) | para 2 money clause | 7-11 | 6-10 |
| **Calendar sweep** — list calendars, list events across multiple calendars, per-event detail | **para 3 sentence 2** | 5-8 | 5-9 |
| Slack thread reads | para 2 "rough read… in the spring" | 3-6 | 2-5 |
| Linear comment traversal | para 4 | 4-7 | 4-7 |
| Six writes plus supporting reads | paras 3 and 4 | 10-14 | 10-15 |
| Cross-service triangulation buffer | — | 5-8 | 5-8 |
| **TOTAL** | | **50-77** | **50-82** |
| **MIDPOINT** | | **63.5** | **66.0** |

**Band: PASS on both models.** Opus **+23.5**, Gemini **+26.0** against the 40 target; both >4x the 15 floor.

The calendar component is now conservative rather than optimistic. Finding the targets requires searching past Lisa's own calendar (the duplicate sits on four others), and 219 "Review" rows across 44 distinct base ids means disambiguation costs `get_event` reads the table does not count.

**Every-reading check, as requested:**

| Reading | Opus | Gemini | Band |
|---|---:|---:|---|
| Full intended trajectory | 63.5 | 66.0 | PASS |
| Agent scopes Calendar to own calendar, finds 3 of 4, misses the duplicate, 1 calendar write | ~59 | ~61 | PASS |
| Agent finds no unit/turn mismatch and no unsettled meeting, 4 writes | ~59 | ~61 | PASS |
| Old-clause Airtable-discharge path | **unreachable** | **unreachable** | n/a |

**Both models clear 40 under every reading.** THIN risk removed.

**Service breadth:** 5 services carry writes (gmail, linear, slack, gcalendar, airtable); 7 of 8 carry reads. PASS.

---

## [Q4a] B1 — QC sub-dimension scoring

```
SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5, middle band removed 06/09) -> five attacks run; clause licenses one write intent on one service against a data-determined target set
SUB-DIM Feasibility -> SCORE 5/5 (1/3/5) -> satisfiable for BOTH owners; see Q5
SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 BINARY) -> zero tool names, zero MCP server names, zero use of "tool"; "review meetings" names a business object
SUB-DIM Prompt Clarity and Specificity -> SCORE 5/5 (1/3/5) -> the two residual near-misses are S3 pinning burdens, not reader ambiguity; a human reader knows exactly what is asked
SUB-DIM Contrived / Unnatural -> SCORE 5/5 (1/3/5) -> "if either of those did not end up properly settled" is naturally hedged colleague speech
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5) -> the edit asserts nothing; it is a conditional. All four original claims verified at row level in iteration 1
SUB-DIM Tool use and Cross-service requirement -> SCORE 5/5 (1/5 BINARY) -> 3 named surfaces plus airtable, quickbooks and gcalendar required for content
SUB-DIM Investigation -> SCORE 5/5 (1/5 BINARY) -> both sentences of para 3 are conditionals; nothing pre-solved
SUB-DIM Coherence -> SCORE 5/5 (1/5 BINARY) -> para 3's two sentences are the same corrective move on two surfaces of one package
SUB-DIM Persona -> SCORE 5/5 (1/3/5) -> "on the ground" and "did not end up properly settled" are onsite-PM register
SUB-DIM Business Function -> SCORE 5/5 (3/5, no FAIL band) -> HOLDING against Council A's 3; FINAL adjudication item
SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5) -> "It is now July, so I am already late" exact against 2026-07-01; the clause's past tense "did not end up" correctly matches meetings dated 05-19, 06-02 and 06-03, all before today
```

**All 12 applicable Prompt sub-dims score 5.**

---

## [Q4b] B4 — lever preservation, all five

| Lever | Trigger | Record the agent must reach | Status |
|---|---|---|---|
| **L2** QuickBooks AR | para 2 money clause (untouched) | Finley `2026-494` $8,400 / `2026-303` $2,190 / `4421` $390, all overdue; Harris zero open rows | **PRESERVED**, clean |
| **L2** Calendar | para 3 sentence 2 | the four owner-review event groups above | **REPAIRED.** Under iterations 1-2 this lever was not attenuated, it was **broken** — the clause routed to Airtable. It now fires. Retrieval half remains signposted by design |
| **L10** Harris double-booking | same clause | `1pon50ds1aevem63td6f7emdn3` (5 rows, all accepted, includes Lisa) vs `qqbwq3s2h7wh5udoek2940mffk` (4 rows, **no Lisa row**, Aurora + Patricia declined); both `confirmed`, neither cancelled | **PRESERVED and STRENGTHENED** — persona-scoping trap |
| **L10** Finley review vs OPS-10 narrative | same clause | `comment_79dc83838bd65d678c48b5911f942412` "first week of June… in the afternoon" against the only two Finley events, 05-19 11:45 and 05-28; Lisa and Aurora both declined; owner not an attendee | **NEWLY SURFACED** this round |
| **L10** OPS-10 state vs narrative | para 4 (untouched) | `OPS-10` `state_OPS_0` Backlog against two comments announcing transitions | **PRESERVED** |
| **L11** net-vs-gross | para 2 money clause (untouched); outlet via para 4 email + new item | six credit memos, $5,630, every one `RemainingCredit = 0` with `Balance == TotalAmt` and no `LinkedTxn` | **PRESERVED**, no 1.1 carrier — AUDIT ruling noted below |
| **L1** latching | para 2 (untouched) | C004 pair `49b2873d46d55e4291a78d91d91a5054` + `5f60afa12c4c53b6b7694d59373acae8` (2026-05-12, thread replies) and C006 `a6779a055eaf5fb1893d0ed6d92e3b39` | **PRESERVED and UPGRADED** (both owners) |
| **L7** multi-write | paras 3 and 4 | 6 writes across 5 services | **PRESERVED** |

**5 of 5 preserved. No HARDNESS_REGRESSION.** One lever repaired, one strengthened, one new carrier surfaced.

---

## [Q5] Feasibility of the new clause for BOTH owners

Verified per-owner against attendee rows.

**Harris.** Lisa holds a row on the original (`1pon50ds1aevem63td6f7emdn3`, 5 rows, she **accepted**) and **no row** on the Rescheduled instance (`qqbwq3s2h7wh5udoek2940mffk`, 4 rows: patricia.nguyen, aurora.winona, teresa.wood, brooke.phillips). Settling the double-booking requires acting on the Rescheduled instance, so `respond_to_event` is **not available to her there**. `update_event` and `delete_event` are, and neither requires attendee membership. **Satisfiable.**

**Finley.** Lisa holds a row on the mid-year review (`8mwlxrq5w5oodwdpmvo83e00f2`, 4 rows) and her response is **declined**. Both `respond_to_event` and `update_event` are available. **Satisfiable, via more paths than Harris.**

**Clause-level:** "either of those" needs at least one unsettled meeting; both qualify. **Feasibility 5/5.**

This produces carry-forward #2 below: the "settled" end state has several valid write forms, and S3 must not require `respond_to_event` on the Harris Rescheduled event, because Lisa cannot call it there.

---

## Rulings noted, not relitigated

- **`tblMaintenanceTickets` is out of scope for correction.** AUDIT sided with Council A: four fields, no unit field, no turn semantics, so "the unit and turn records" licenses `tblMakeReady` only and maintenance stays read-and-report. **Accepted.** This supersedes my iteration-2 carry-forward #1, which had flagged the table as plausibly in scope. My reading was wrong; the field list settles it.
- **L11's missing Outcome 1.1 carrier is an S3 budget item, not an S1 defect.** AUDIT concurred the finding is real and dissented on placement: L11 lives in QuickBooks, which is read-only precisely because I blocked that surface at iteration 1, so giving it a write carrier would reintroduce the closed defect. **Ruling accepted.** Mitigation belongs in S3 under rules 14 and 28.
- **Hardness Plan calendar pin list corrected in place.** `## CORRECTION: Calendar pin list`. All calendar claims in this report re-derived independently.

## Open disagreement with Council A

**Business Function — HOLDING 5/5 against 3/5.** `StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md` states the rule in terms: *"tasks are always authored from a persona's home Business Function, not from participant appearances"*, mapping Lisa Smith to **1 Property Operations**. Three of paragraph 2's four workstreams are Cat 1 objects, and no owner-facing action occurs anywhere — the email goes to Brooke, both items to the tracker, the post to an internal channel. The Cat 2 signal is C006, which the doc lists as *primary* to Cat 2, not exclusive. Verdict-neutral (no FAIL band). **FINAL adjudication item.**

---

## Carry-forwards for S2 / S3

| # | Sev | Issue | Required action |
|---|---|---|---|
| **1** | **MODERATE** *(new)* | **Calendar near-miss.** "their review meetings" sits beside `ti5zt1xubdggbehtp79um9mim6` "May Owner Report Review - Finley Properties" (3 rows; Lisa declined, Teresa declined, owner accepted), which is also a Finley review meeting and also looks unsettled. | S3 pins by **full title** ("Harry Harris Mid-Year Portfolio Review (Rescheduled)", "Robert Finley Mid-Year Portfolio Review"), never by partial match on "Review" plus surname. A criterion must not fail an agent that additionally touches the May report review. |
| **2** | **MODERATE** *(new)* | **The "settled" end state has multiple valid write forms.** Harris: `update_event` (status change on the duplicate) or `delete_event`. Finley: `respond_to_event` or `update_event`. Lisa has **no row** on the Harris Rescheduled event. | S3 writes an accept-set spanning `update_event` and `delete_event`, and **must not require `respond_to_event` on `qqbwq3s2h7wh5udoek2940mffk`** — the persona cannot call it there. |
| **3** | **MODERATE** *(carried)* | **Calendar pinning fan-out.** Events store one row per invitee calendar: `1pon50ds1aevem63td6f7emdn3` = 5 rows, `qqbwq3s2h7wh5udoek2940mffk` = 4, `8mwlxrq5w5oodwdpmvo83e00f2` = 4, `ti5zt1xubdggbehtp79um9mim6` = 3. | Never pin a bare base id (F7 AMBIGUOUS_TARGET). Pin the per-calendar row or describe the target by content plus the calendar it sits on. |
| **4** | **MODERATE** *(carried)* | "the mid-year review item" returns 5 Linear candidates; OPS-11 and OPS-13 carry byte-identical titles in different states. OPS-10 is the only one with "Mid-Year" in the title. | S3 pins OPS-10 by title content, never by issue number alone. |
| **5** | **MODERATE** *(carried)* | Corrected-row set in `tblMakeReady` is data-determined, not singular. | One atomic criterion per genuinely-mismatching row (rules 13/14, F7/F8). Pin only Mesa Vista 107A, Mesa Vista 310C, the Sunset Ridge cluster. Never 207A, 4C, Las Palmas 204B, Las Vistas 311A, or bare "Unit 14". |
| **6** | **MODERATE** *(carried, AUDIT-ruled)* | **L11 has no Outcome 1.1 carrier.** Gradable only via 1.2 email / new-item content and 2.1 final-response facts. | S3 budgets it explicitly. Lever carrier, must never be cut at the 60-criterion ceiling. |
| 7 | NOTE *(new)* | **Finley L10 carrier**, previously unrecorded: OPS-10 comment describes a first-week-of-June afternoon review; the only Finley events are 05-19 11:45 and 05-28; Lisa and Aurora both declined; the owner is not an attendee. | Carry into S2. This is what makes "either of those" fire on both owners rather than one. |
| 8 | NOTE *(new)* | "Linda Castillo Mid-Year Portfolio Review" exists and is excluded only by the possessive "their". | S3 must not let a criterion match it. |
| 9 | NOTE *(carried)* | L1 fires on both owners; the C004 pair are near-duplicates 19 minutes apart. | Pin by content. |
| 10 | MINOR *(carried)* | Stump H4 (David Shea negative-existence) largely unreachable; Shea is Patricia's owner. Confirmed this round: Shea has **no** review event in 565 rows. | S4 expects H1/H2/H3. Do not widen scope. |
| 11 | NOTE *(carried)* | `slack_send_message_draft` / `slack_schedule_message` are alternates to `slack_send_message`. | S2 names the post explicitly. |

---

## Role-lens union

| Lens | Iteration 3 finding |
|---|---|
| **Architect** | Clean. Splitting the sentence gives paragraph 3 two parallel corrective moves on two surfaces of one package. |
| **Implementer** | Clean, with one real constraint: Lisa has no row on the Harris Rescheduled event, so `respond_to_event` is unavailable there. Both owners remain satisfiable. |
| **Red-team** | Five attacks run on the new clause; all fail to move the write off Calendar. The strongest (May report review) is additive, not competing. |
| **Ground-truth** | Every calendar and Airtable claim re-derived this session after the iteration-2 pin-list failure. Surfaced one new L10 carrier the Hardness Plan lacks. |
| **Integration** | Six MODERATE carry-forwards, five of them pinning-shaped. S3 is where this task's remaining risk lives. |

Union verdict: **GO.**

---

## Exit criteria

| Criterion | Status |
|---|---|
| Every applicable Prompt sub-dim = 5 | **YES** (12 of 12; Business Function 5 mine / 3 Council A, no FAIL band) |
| No adversarial divergence | **YES** — five attacks on the new clause, none flips the write |
| AUDIT F1 closed | **YES** — verified independently, not accepted on report |
| Density >= 40 both models, every reading | **YES** — 63.5 / 66.0; worst reading 59 / 61; THIN path unreachable |
| Every Hardness lever triggered | **YES** — 5 of 5; one repaired, one strengthened, one new carrier |
| No phrasing hits | **YES** — 0 tool names, 0 service names, 0 numerals, 0 dashes |
| No upstream propagation flags | **YES** |

**GO. Proceed to S2.** The remaining risk is concentrated in S3 pinning: carry-forwards 1 through 5 are all F7/F8-shaped, and carry-forward 6 is a lever that can vanish during budgeting without any gate noticing.

```json
{
  "phase": "prompt",
  "council": "B",
  "task_dir": "Tasks/46_6a62ccb6ce2323b4b9e0c8d8",
  "verdict": "GO",
  "perspectives": {
    "B1": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "prompt:para1-4",
          "issue": "Business Function 5/5 here vs 3/5 Council A; persona home-function rule explicit and controlling, no owner-facing action occurs",
          "fix": "FINAL adjudicates with both reads in view; verdict-neutral",
          "propagate_to": null
        }
      ]
    },
    "B2": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "prompt:para3s2",
          "issue": "AUDIT F1 closed: 'their review meetings' has no Airtable referent (verified: no field in tblMakeReady or tblMaintenanceTickets matches meet/appoint/calendar/event); 219 calendar rows carry Review in title",
          "fix": "none required",
          "propagate_to": null
        },
        {
          "severity": "MODERATE",
          "location": "gcalendar:ti5zt1xubdggbehtp79um9mim6",
          "issue": "NEW: 'May Owner Report Review - Finley Properties' is a near-miss for 'their review meetings'; 3 rows, Lisa declined, Teresa declined, owner accepted",
          "fix": "S3 pins by full title, never by partial match on Review plus surname; must not fail an agent that additionally touches it",
          "propagate_to": null
        },
        {
          "severity": "MODERATE",
          "location": "linear:OPS-10",
          "issue": "'the mid-year review item' returns 5 Linear candidates; OPS-11 and OPS-13 have identical titles in different states",
          "fix": "S3 pins OPS-10 by title content, never by number alone",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "gcalendar:Linda Castillo Mid-Year Portfolio Review",
          "issue": "Castillo review exists; excluded only by the possessive 'their'",
          "fix": "S3 must not let a criterion match it",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "prompt:para4",
          "issue": "slack_send_message_draft and slack_schedule_message are alternates to slack_send_message",
          "fix": "S2 names the post explicitly",
          "propagate_to": null
        }
      ]
    },
    "B3": { "status": "PASS", "findings": [] },
    "B4": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "gcalendar:qqbwq3s2h7wh5udoek2940mffk",
          "issue": "NEW: 'settled' end state has several valid write forms and lisa.smith has NO row on the Harris Rescheduled event, so respond_to_event is unavailable to her there",
          "fix": "S3 accept-set spans update_event and delete_event; never require respond_to_event on that event",
          "propagate_to": null
        },
        {
          "severity": "MODERATE",
          "location": "gcalendar.gcalendar_events.json",
          "issue": "Calendar pinning fan-out: one row per invitee calendar; base ids match 5/4/4/3 rows respectively",
          "fix": "Never pin a bare base id; pin the per-calendar row or describe by content plus calendar",
          "propagate_to": null
        },
        {
          "severity": "MODERATE",
          "location": "airtable:tblMakeReady",
          "issue": "Corrected-row set is data-determined, not singular",
          "fix": "One atomic criterion per mismatching row; pin only Mesa Vista 107A, 310C, Sunset Ridge cluster",
          "propagate_to": null
        },
        {
          "severity": "MODERATE",
          "location": "_aux/Hardness_Plan.md:L11",
          "issue": "L11 has no Outcome 1.1 carrier; AUDIT ruled placement is S3 budget, not S1 defect, since QuickBooks is read-only by design",
          "fix": "S3 budgets explicitly under rules 14 and 28; lever carrier, never cut",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "linear:comment_79dc83838bd65d678c48b5911f942412",
          "issue": "NEW L10 carrier on Finley: comment describes a first-week-of-June afternoon review; only Finley events are 05-19 11:45 and 05-28; Lisa and Aurora declined; owner not an attendee",
          "fix": "Carry into S2; this is what makes 'either of those' fire on both owners",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "slack.slack_messages:49b2873d46d55e4291a78d91d91a5054,5f60afa12c4c53b6b7694d59373acae8",
          "issue": "L1 fires on both owners; C004 pair are near-duplicates 19 minutes apart",
          "fix": "Pin by content",
          "propagate_to": null
        },
        {
          "severity": "MINOR",
          "location": "_aux/Hardness_Plan.md:H4",
          "issue": "Stump H4 largely unreachable; confirmed David Shea has no review event in 565 rows",
          "fix": "S4 expects H1/H2/H3; do not widen scope",
          "propagate_to": null
        }
      ]
    },
    "B5": { "status": "PASS", "findings": [] },
    "B6": { "status": "PASS", "findings": [] },
    "B7": { "status": "NOTE", "findings": [] },
    "B8": { "status": "NOTE", "findings": [] },
    "B9": { "status": "NOTE", "findings": [] },
    "B10": { "status": "NOTE", "findings": [] },
    "B11": { "status": "NOTE", "findings": [] }
  },
  "scores": {
    "unique_ground_truth": { "score": 5, "scheme": "1/3/5", "reason": "five attacks run; clause licenses one write intent on one service against a data-determined target set" },
    "feasibility": { "score": 5, "scheme": "1/3/5", "reason": "satisfiable for both owners; Harris via update_event/delete_event, Finley via respond_to_event/update_event" },
    "explicit_tool_mention": { "score": 5, "scheme": "1/5", "reason": "zero tool names, zero MCP server names; 'review meetings' names a business object" },
    "clarity_and_specificity": { "score": 5, "scheme": "1/3/5", "reason": "residual near-misses are S3 pinning burdens, not reader ambiguity" },
    "contrived_unnatural": { "score": 5, "scheme": "1/3/5", "reason": "'if either of those did not end up properly settled' is naturally hedged colleague speech" },
    "truthfulness": { "score": 5, "scheme": "1/3/5", "reason": "the edit asserts nothing; it is a conditional. Original claims verified at row level" },
    "tool_use_cross_service": { "score": 5, "scheme": "1/5", "reason": "3 named surfaces plus airtable, quickbooks, gcalendar required for content" },
    "investigation": { "score": 5, "scheme": "1/5", "reason": "both sentences of para 3 are conditionals; nothing pre-solved" },
    "coherence": { "score": 5, "scheme": "1/5", "reason": "para 3's two sentences are the same corrective move on two surfaces of one package" },
    "persona": { "score": 5, "scheme": "1/3/5", "reason": "'on the ground' and 'did not end up properly settled' are onsite-PM register" },
    "business_function": { "score": 5, "scheme": "3/5", "reason": "persona home-function rule explicit and controlling; HOLDING against Council A's 3" },
    "alignment_with_today": { "score": 5, "scheme": "1/3/5", "reason": "past tense 'did not end up' correctly matches meetings dated 05-19, 06-02, 06-03, all before 2026-07-01" }
  },
  "density_projection": {
    "midpoint": 63,
    "band": "PASS",
    "per_model": {
      "opus": { "range": [50, 77], "midpoint": 63.5, "band": "PASS" },
      "gemini": { "range": [50, 82], "midpoint": 66.0, "band": "PASS" }
    },
    "scheme": "V4 per-model: >=40 PASS, 15-39 THIN, <15 INSUFFICIENT",
    "worst_reading": { "opus": 59, "gemini": 61, "band": "PASS" },
    "audit_thin_risk": "removed; the Opus 37-40 floor was conditional on the Airtable discharge path, which no longer exists",
    "breadth_services": 7,
    "breadth_band": "PASS"
  },
  "lever_preservation": {
    "expected": 5,
    "preserved": 5,
    "missing": [],
    "repaired": ["L2-calendar (previously routed to Airtable by the old clause; now fires)"],
    "strengthened": ["L10-Harris (persona-scoping trap: lisa.smith has no row on the duplicate)"],
    "newly_surfaced": ["L10-Finley (OPS-10 comment describes a first-week-of-June afternoon review that does not exist)"],
    "upgraded": ["L1 (fires on both owners)"],
    "at_risk_downstream": ["L11 (no Outcome 1.1 carrier; AUDIT-ruled S3 budget item)"]
  },
  "bucket_1_risk_pct": null,
  "iteration": 3,
  "timestamp": "2026-07-28T23:48:00-05:00"
}
```

---

## Post-hoc provenance note (added at S1 close, not by Council B)

**Why this exists.** Oracle verification flagged that `_aux/Hardness_Plan.md` was modified at
23:38:21, AFTER this report (23:35:43) and the other two council reports were written. So B4's
"levers 5 of 5 preserved" verdict was rendered against the PRE-correction plan, and nothing on disk
recorded which bytes it had seen. That is the AGENTS.md rule 15 shape: a verdict describing bytes
that subsequently changed.

**Pinned hashes (sha256, first 16):**

| State | Hash | Provenance |
|---|---|---|
| Hardness_Plan.md as B4 evaluated it | `dee6b5a10f34aaa9` | preserved at `_aux/Hardness_Plan.md.pre_s1audit.bak` |
| Hardness_Plan.md current | `b77f6cada1fa9c08` | after the S1 AUDIT corrections |

**Why no re-run is required.** The diff is **+108 lines, -1 substantive line**. The removed line was
the false certification that calendar base ids `1pon50ds1aevem63td6f7emdn3` and
`qqbwq3s2h7wh5udoek2940mffk` were "safe to pin (distinct base ids)"; they match 5 and 4 rows.
Everything else is additive and explicitly labelled `## CORRECTION:` or `## CARRY-FORWARD:`.

Critically, the **lever set is identical** (L1 / L2 / L7 / L10 / L11) and the **`### L36 test`
section is byte-identical**, so the standard against which the prompt was judged did not move. B4's
verdict is therefore unaffected by the edit. Recorded rather than re-run, because re-running three
councils to re-derive an unchanged verdict is the cost rule 20 warns against.
