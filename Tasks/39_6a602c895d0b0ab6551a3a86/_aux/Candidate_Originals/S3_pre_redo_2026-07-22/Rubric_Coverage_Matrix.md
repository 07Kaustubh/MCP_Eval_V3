# Rubric Coverage Matrix — 39_6a602c895d0b0ab6551a3a86

**AUDIT verdict:** PASS (STRICT). All 8 lenses clean. All 5 hardness levers preserved end-to-end. Zero PROPAGATE flags.

**Council A verdict:** GO. 22/22 rubrics fully atom-grounded against `_aux/Universe_Split/`. All persona attributions co-occur in universe atoms.

**Council B verdict:** GO. Zero Major, zero Moderate, zero Minor. Density midpoint 49.5 (rounds to 50, meets design target). All 5 hardness levers rubric-preserved.

**Validator verdict:** PASS. 0 fails, 5 WARNs (3 Jaccard similarity between structurally-parallel per-item content rubrics R2/R5/R8, 2 date-typed-value observations on decoy-thread dates 2026-06-16 in R16 + R19 — all non-blocking; A/B/AUDIT confirmed grounded).

**Rubric count:** 22 outcome / 0 process. Flat schema.

---

## Prompt sentence → OE step(s) → Rubric(s)

| # | Prompt sentence (paraphrased anchor) | OE step(s) | Rubric(s) |
|---|---|---|---|
| P1 | "Never got a proper closeout together on Las Vistas 3C after my second-pass re-check…Brooke asked me at the time to wrap the field team on 3C…Circling back today to finally close 3C out before the week is over." | OE1 (contact anchor) + OE3 (Airtable state read) + OE15 (Gmail canonical thread) + OE17 (Slack canonical parent) | Context / framing — no rubric required (self-directed anchor, not a deliverable). |
| P2 | "All three punch items from the first-pass fail cleared on the re-check. Baseboard in the living room came out even, no shadow lines under the touch-ups. Refrigerator and oven interiors were clean, no residue on the shelves or the door seals. Towel ring in the bathroom was on the right way and secure." | OE5 (get_issue OPS-224/225/226) | Content anchor — feeds R2, R5, R8 (per-item pass observations). |
| P3 | "Bennett dropped a completion note on each of the three 3C punch items around the time I re-inspected. Pull those up so my closeout comments track the right item, then get each ticket moved through my sign and out of my queue with the pass called out for each item, not a blanket close." | OE6 (list_comments × 3) + OE7 (Done state) + OE8 + OE9 + OE10 + OE11 + OE12 + OE13 | R1 (comment OPS-224) · R2 (baseboard per-item content) · R3 (OPS-224 → Done) · R4 (comment OPS-225) · R5 (appliance per-item content) · R6 (OPS-225 → Done) · R7 (comment OPS-226) · R8 (towel ring per-item content) · R9 (OPS-226 → Done). |
| P4 | "Pull the make-ready record on 3C and get my second-pass sign-off written into it. My name, the re-inspection date, and one line per punch item. Anyone pulling 3C up after this should read the second-pass sign-off and not just Brooke's supervisory note." | OE2 (list_bases/tables) + OE3 (Airtable state read) + OE14 (update_records_for_table) | R10 (Airtable update fires) · R11 (Jaime Salinas named) · R12 (2026-06-18 re-inspection date) · R13 (one line per punch item, three items) · R14 (appends, does not overwrite). |
| P5 | "Carlos needs an email from us that 3C is clear so leasing can start today. Copy Brooke so she knows the loop closed on 3C. Keep it short, this is a hand-off, not a report." | OE1 (contact anchor) + OE15 (canonical thread select) + OE16 (create_draft) | R15 (draft to Carlos, cc Brooke) · R16 (threads under Brooke's 6/18 canonical, NOT 6/16 QC-Fail decoy — L26) · R17 (states QC-passed + leasing can activate today). |
| P6 | "Same pass update on 3C in Slack so the crew sees it without having to chase me." | OE17 (canonical parent select) + OE18 (slack_send_message) | R18 (posts to C004 #make-ready) · R19 (threaded under Brooke's 6/18 canonical parent ts=1781788320.000202, NOT 6/16 QC-FAIL decoy ts=1781645520.000200 — L26) · R20 (three per-item confirmations + leasing activation). |
| P7 | "Check the calendar for any 3C showings booked between now and next Wednesday, and set me a reminder for Friday morning to spot-check 3C's fridge and oven interiors again before whichever tour hits earliest." | OE19 (list_events window check) + OE20 (create_event Friday morning) | R21 (calendar event on jaime.salinas@starpm.com Friday 2026-07-03 morning America/Chicago) · R22 (summary references Las Vistas 3C + fridge and oven interior spot-check). Note: OE19 calendar-check is a read; not rubric-tested since it feeds R21 timing only. |

**Coverage completeness:** 22/22 rubrics map to at least one prompt sentence. 6/7 prompt sentences have at least one rubric (P1 is framing anchor with no deliverable — legitimately unrubric-covered). 10/10 OE write actions covered.

---

## Hardness lever → Rubric preservation map

| Lever | Mechanism | Rubric(s) that fail when lever not traversed |
|---|---|---|
| **L1 Latching** (Airtable already `selReady` — agent short-circuits) | Existing state contradicts Linear tickets still needing sign-off. | R1-R9 (Linear closures fail if agent latches on Airtable state) + R10-R14 (Airtable append fails if agent no-ops). |
| **L8 Multi-link chain** (3 OPS closures across Airtable + Linear + Slack + Gmail) | Every ticket needs comment + state flip; every artifact needs its own write. | R1-R9 (3 tickets × 3 rubrics) + R10-R14 + R15-R17 + R18-R20 + R21-R22 = full chain. |
| **L9 StarPM parameter gotcha** (Slack `message` NOT `payload`; Gmail `body` NOT `content` + no send tool; Airtable camelCase; save_comment `issueId`) | Tool call fails if wrong param names. | R1/R4/R7 (Linear comment must land — indirect via tool success) · R10 (Airtable update must land) · R15 (Gmail draft must land — no send tool) · R18 (Slack post must land — draft tool != send). |
| **L25 Existing-output anchor** (Airtable `fldTurnStatus=selReady` short-circuits agent's write cascade) | Rubrics require FULL cross-service closeout; agent's "already Ready" instinct kills the writes. | R10 (Airtable write required) · R11-R13 (Jaime name + date + per-item lines required) · R14 (append, don't overwrite) · R1-R9 (Linear closures required despite Airtable Ready). |
| **L26 Decoy parent thread** (Slack 6/16 QC-FAIL vs 6/18 CLOSEOUT-REQUEST; Gmail 6/16 QC-FAIL vs 6/18 closeout package) | Older decoy has richer keyword overlap; agents mis-target. | R16 (Gmail — threads under Brooke's 6/18 canonical closeout, NOT 6/16 fail decoy) · R19 (Slack — thread_ts must be 1781788320.000202 canonical, NOT 1781645520.000200 decoy). |

**Lever preservation completeness:** 5/5 hardness levers rubric-preserved end-to-end.

---

## Rubric → OE step reverse map (orphan check)

| Rubric | OE step(s) | Prompt sentence anchor |
|---|---|---|
| R1 · Agent comments on OPS-224 | OE6 + OE8 | P3 |
| R2 · Comment on OPS-224 confirms baseboard pass | OE6 + OE8 | P2 + P3 |
| R3 · OPS-224 → Done | OE7 + OE9 | P3 |
| R4 · Agent comments on OPS-225 | OE6 + OE10 | P3 |
| R5 · Comment on OPS-225 confirms appliance pass | OE6 + OE10 | P2 + P3 |
| R6 · OPS-225 → Done | OE7 + OE11 | P3 |
| R7 · Agent comments on OPS-226 | OE6 + OE12 | P3 |
| R8 · Comment on OPS-226 confirms towel ring pass | OE6 + OE12 | P2 + P3 |
| R9 · OPS-226 → Done | OE7 + OE13 | P3 |
| R10 · Agent updates Airtable rec291f423370e2a2db | OE2 + OE3 + OE14 | P4 |
| R11 · Update names Jaime Salinas | OE14 | P4 |
| R12 · Update includes 2026-06-18 re-inspection date | OE14 | P4 |
| R13 · Update includes one confirmation line per punch item | OE14 | P4 |
| R14 · Update appends existing narrative | OE14 | P4 |
| R15 · Agent drafts email to Carlos cc Brooke | OE1 + OE16 | P5 |
| R16 · Draft threads under Brooke's 6/18 canonical thread (L26) | OE15 + OE16 | P5 |
| R17 · Draft states 3C QC-passed + leasing can activate | OE16 | P5 |
| R18 · Agent posts to C004 #make-ready | OE18 | P6 |
| R19 · Slack threaded under Brooke's 6/18 canonical parent (L26) | OE17 + OE18 | P6 |
| R20 · Slack post per-item confirmations + leasing activation | OE18 | P6 |
| R21 · Calendar event Friday morning 2026-07-03 America/Chicago | OE19 + OE20 | P7 |
| R22 · Event summary references Las Vistas 3C + fridge and oven | OE20 | P7 |

**Orphan check:** 0 orphan rubrics. Every rubric maps to at least one OE step + one prompt sentence.

---

## Category distribution

- Outcome: 22 (100%)
- Process: 0 (0%)

Matches V3 reference distribution across `QC_Tasks/V3_Tasks/Task11..Task14` (59 outcome / 0 process across 4 tasks) and V4 QC_Passed samples (Task1 = 33/0, Task2 = 15/0). Zero-process is the default expectation for StarPM Jaime-role hand-off tasks; every requirement folds into a stricter Outcome under the three-condition Process test.

---

## Density projection (Council B B3 + AUDIT LENS 7)

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (contacts, Airtable list_bases / list_tables_for_base / get_table_schema, Slack read, Gmail search, list_issue_statuses, list_events) | 8-12 | 10 |
| Linear ticket triple-close chain (3 × get_issue + 3 × list_comments + 3 × save_comment + 3 × save_issue) | 12-15 | 13.5 |
| Airtable update chain (search_records + update_records_for_table) | 2-3 | 2.5 |
| Gmail draft chain (search_threads + optional get_thread + create_draft) | 2-4 | 3 |
| Slack post chain (slack_read_channel + slack_send_message) | 2-3 | 2.5 |
| Calendar chain (list_events + create_event) | 2-3 | 2.5 |
| L1 / L25 verification re-reads + L9 parameter retry loops | 6-10 | 8 |
| L26 decoy disambiguation re-searches | 3-5 | 4 |
| Cross-service triangulation buffer | 3-5 | 4 |
| **TOTAL projected** | **40-60** | **50** |

**Gate:** midpoint 50 → **PASS** (≥ 50 design target, well above 40 floor). No THIN band invoked.
