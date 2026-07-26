# OE Solvability — S2

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm (V4) · **Universe today:** 2026-07-01 America/Chicago
**Deliverable:** `6_Oracle_Events.txt`, 38 numbered steps, 27 discovery and 12 write calls (OE 35 carries two `save_comment` calls).

## Prompt-to-OE forward coverage map

| # | Prompt sentence / ask | Type | Covered by |
|---|---|---|---|
| 1 | "End of June was the target to have the Preventive Maintenance Push closed out. That came and went yesterday and it is still sitting open." | context, sets the 2026-06-30 lapse | OE 2, OE 3 |
| 2 | "Brooke started this in early May, HVAC, plumbing and electrical across the whole portfolio" | context, scope + owner | OE 2 (kickoff ts `1778171944.000091`), OE 10 |
| 3 | "and I have been the QC eye on it" | persona scope | OE 11 (exactly three assignee-Jaime records) |
| 4 | "I logged both cluster spot-checks as passing in late May and my read is that my part of it is finished." | the belief to be tested | OE 12, OE 13, OE 14 |
| 5 | "The crew called the HVAC run wrapped around the same time." | Lever 1 latch | OE 3 (Elias wrap ts `...446.000005` / `...447.000006`), OE 16 (OPS-81, OPS-66) |
| 6 | "I need to know where every piece of it stands as of today, cluster by cluster" | explicit ask A | OE 15, 16, 17, 18, 19, 20, 21 |
| 7 | "and I need our records saying the same thing. Work out what is actually finished and what is not, and get our tracking to match." | explicit ask B | OE 15 (determination), OE 34, OE 35 (the correction is recorded in the notes; no state flip required) |
| 8 | "Anything still open gets its own tracking item raised, with the person who owns that work named on it." | explicit ask C | OE 29, 30, 31, 32, 33 (five `save_issue`, owner in `description` text) |
| 9 | "My own spot-check records are part of that, with a short note left on each one saying where it landed and why." | explicit ask D | OE 34 (OPS-87), OE 35 (OPS-96, OPS-98) |
| 10 | "Anything flagged in the field that still needs a tech back onsite belongs in our maintenance ticket log rather than sitting as a tracking item" | explicit ask E | OE 24, 25, 28 |
| 11 | "and put a slot on my calendar to go back out and re-inspect whatever ends up in that follow-up." | explicit ask F | OE 22, 23, 36 |
| 12 | "Then post where this stands in the channel the push has been running in so the crew is working off the same picture" | explicit ask G | OE 1 (resolve C001), OE 37 |
| 13 | "and draft an email to Brooke, cluster by cluster, with what is open, who is holding it, and what has to happen before this can close." | explicit ask H | OE 26 (recipient), OE 38 |
| 14 | "I do not want Brooke's email written so it can be read either way. If my QC side is a pass, say pass. If it is not, say straight out that my earlier sign-off does not hold and this should not be treated as closeable yet, with the reasons." | explicit ask I, the L31 beat | OE 38, split into two atomic graded facts per AUDIT A-3 |

Implicit asks covered without a prompt sentence naming them: decode the Linear workflow states (OE 9, the Lever 2 prerequisite); establish that Airtable is the maintenance system of record and Linear secondary (OE 8, OE 24); confirm no existing ticket already covers the field items (OE 25); confirm no push content lives in Gmail (OE 27); confirm nothing already scheduled covers the re-inspection (OE 23).

**Reverse map: clean.** Every OE step traces to a prompt ask or to a discovery required to satisfy one. No scope creep.

## The six open items and where each is grounded

| # | Open item | Primary evidence | OE |
|---|---|---|---|
| 1 | None of Jaime's three QC records is in a completed state (OPS-87 Todo, OPS-96 Todo, OPS-98 In Progress) despite prose claiming Done | Linear `state_id` column, decoded via `list_issue_statuses` | OE 9, 12, 13, 14, 15 |
| 2 | Two North units Jaime flagged 2026-05-23 as needing HVAC right away were never dispositioned | Slack ts `1779562423.000092`, plus no covering record among the ten a "North cluster" query returns | OE 4, 16 |
| 3 | One South unit never serviced, reschedule with Carlos still open | OPS-43 comments + C001 thread replies `...444.000003` / `...445.000004` | OE 5, 17 |
| 4 | Two North units still pending a second round of access notices | OPS-56 description and both comments, no reply in the 48-comment corpus | OE 18 |
| 5 | Portfolio filter run blocked on a 20x25 restock | C001 parent `1779567943.000011` + thread reply `1779569323.000012` | OE 6, 13, 20 |
| 6 | Plumbing findings open: two water heaters past serviceable life, hose bibs | OPS-97 (Todo vs "Moving this to In Progress"), Slack `1780256425.000094`, `1780494075.000095`, 2026-06-02 calendar agenda | OE 19, 22 |

Plus the West cluster QC coverage gap (OE 20) and the unconfirmed East QC state (OE 21), which are coverage findings rather than field items.

## OE-to-rubric forward map (preview for S3)

| OE | Write action | Rubric type | S3 notes carried in the OE |
|---|---|---|---|
| 28 | Airtable ticket, `appPropertyOps` / `tblMaintenanceTickets` | Outcome 1.1 + 1.2 | Grade on content, never a record id. No owner or status field exists. Priority value must not be graded. Boundary residuals (South unit, second condensate drain, compressor) free-routing, neither required nor penalised |
| 29 | Linear item, West QC coverage gap | Outcome 1.1 + 1.2 | Owner accept-set Lisa Smith / John Smith / Brooke Phillips. Decompose into two content criteria plus one owner criterion. Must not assert that no West work finished |
| 30 | Linear item, unfinished filter run | Outcome 1.1 + 1.2 | Owner accept-set John Smith / Elias Navarro / Brooke Phillips. Two positive content criteria (restock block; Brooke's unanswered ask). **The absence must not be a graded criterion** |
| 31 | Linear item, access reschedules | Outcome 1.1 + 1.2 | Owner accept-set Carlos Mendez / Elias Navarro / Tony Reyes. One criterion per cluster; each must pass whether filed as one item or two |
| 32 | Linear item, plumbing findings | Outcome 1.1 + 1.2 | Owner accept-set Carlos Mendez / Brooke Phillips. Four content criteria plus owner; the water-heater criterion must accept either Linear or Airtable |
| 33 | Linear item, East QC unconfirmed | Outcome 1.1 + 1.2 | Owner accept-set Elias Navarro / Jaime Salinas / Brooke Phillips. Three content criteria plus owner. **Must accept either a new item or the OPS-98 note** or a correct agent false-fails |
| 34 | `save_comment` OPS-87 | Outcome 1.1 + 1.2 | One of three atomic per-record criteria |
| 35 | `save_comment` OPS-96, `save_comment` OPS-98 | Outcome 1.1 + 1.2 x2 | Three atomic criteria across OE 34 and OE 35 so a two-of-three agent fails exactly one. Extra comments on OPS-99 / OPS-108 / OPS-51 not penalised |
| 36 | `create_event` on Jaime's calendar | Outcome 1.1 + 1.2 | No date, duration, attendee list or count pinned. Only: future-dated after 2026-07-01, on her calendar, describes the re-inspection |
| 37 | `slack_send_message` C001 | Outcome 1.1 + 1.2 | Nine per-item criteria, never one enumeration. Grade destination on the descriptive path, not the channel id |
| 38 | `create_draft` to brooke.phillips@starpm.com | Outcome 1.1 + 1.2 | One criterion per cluster, not one covering all four. Retraction split into two atomic criteria graded on substance, not lexical echo |

**Outcome 2.1 candidates** (facts the user asked to be told): the cluster-by-cluster standing as of 2026-07-01, and the determination that the QC side does not hold. Both are delivered through the writes above rather than a separate reply, so S3 should confirm whether the platform expects a 2.1 or whether the 1.2 content criteria already carry them.

**Process rubrics: expected zero.** No ordering constraint exists that an Outcome cannot prove. The three-condition test fails on every read step: the downstream Outcome criteria prove the reads happened, and the load-bearing determination is provable from the content of the notes, the Slack post and the draft.

## Hardness lever trace

| Lever | OE steps | Status |
|---|---|---|
| 2 — structured-DB skip on the Linear `state_id` column | OE 9, 12, 13, 14, 15 | preserved, the symmetric backbone |
| 9 — authority dismissal, persona-self variant | OE 12, 13, 14 (her own competently worded sign-off) | preserved |
| 1 — latching on the loudest wrap | OE 3, 16 (OPS-81 comment lands 7 min 14 s after her flag), 21 | preserved and **strengthened** |
| 8 — multi-link chain off her field note | OE 4, 16, 25 | preserved, L7 posture corrected so the graded fact is positive |
| 5 — thread-reply blindness | OE 5, 6, and graded through OE 30 and OE 31 | preserved |
| L31 retraction beat (Gemini-selective, not one of the 5) | OE 38 | preserved, now split per AUDIT A-3 |

## Density and breadth

Governing minimising reading: 47 calls, Opus midpoint **50**, Gemini **42**, combined **46**. Band **PASS** on both models against the StarPM V4 bar of 40. Gemini's floor of 38 is the soft spot; per Task 41 calibration individual sub-40 Gemini runs are expected and are not a defect.

Breadth: 4 services at >= 5% (threshold 4), but `linear` at **63.8%** trips the `>60% = THIN_BREADTH` disqualifier. Documented acceptance with the full reasoning is in `_aux/Verification_s2.md`; it is a prompt-and-universe property that no OE edit can fix, and manufacturing breadth was explicitly declined.

## Phase history

Three council rounds and two AUDIT passes were required. Round-1 councils returned 2 BLOCKER and 9 MAJOR between them; the first AUDIT returned REVISE with 3 MAJOR. Notably, two successive attempts at the F8 decomposition guards each introduced a fresh defect (a dropped Lever 5 element, then a reintroduced L7 absence-grading fault), both caught by councils rather than by the author. Two council claims were adjudicated partly against the councils and one council later conceded an arithmetic error of its own on the breadth figure.

## AUDIT verdict

**`PASS (STRICT)`** — 0 BLOCKER, 0 MAJOR, 0 outstanding MINOR, 4 NOTE. All five LENS 1 sub-dims at 5/5 (OE Completeness, OE Accuracy, Universe Feasibility, Cross-service Coherence, Trajectory Tool Call Count) on a 60-row per-atom evidence table. Lens 2 answer-leakage zero hits. Lens 3 five levers trace end-to-end. Lens 4 density PASS on both models with THIN_BREADTH carried as documented acceptance. Lens 8 regression anchors 62/62. Anti-rationalization 5 found / 1 promoted / 4 hard-excluded.

Two REVISE rounds were needed. Four MAJORs were raised and cleared across the three audit passes: the missing F8 decomposition guards on OE 29-33; the understated Linear breadth share; both council GOs predating the final text; and OE 30 instructing the agent to write an unbounded absence claim on the one surface where OPS-91's title contains the words being claimed.

**One note carried to FINAL:** all three rounds ended with the OE postdating both council reports, so the AUDIT passes carried all verification of final state. FINAL should re-verify rather than inherit council reasoning. Also carried: the Hardness Brief's own "keep Linear under 35%" instruction is missed by roughly 28 points, which FINAL should see alongside the THIN breadth acceptance.
