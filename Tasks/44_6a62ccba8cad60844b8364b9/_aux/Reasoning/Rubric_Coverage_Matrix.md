# Rubric Coverage Matrix — Tasks/44_6a62ccba8cad60844b8364b9

**Universe:** starpm (V4) · **Persona:** Jaime Salinas, Quality Control Inspector · **Universe today:** 2026-07-01 (America/Chicago)
**Rubric set:** 64 criteria — 64 outcome, 0 process
**Validator:** `validate.py --phase rubrics` exit 0 · 0 fails · 0 warns · 0% Major / 0% Moderate / 0% any-issue
**Council A (grounding):** GO (round 3) · **Council B (adversarial QC):** GO (round 3)
**AUDIT verdict:** `PASS (STRICT)` — all 5 Rubric sub-dimensions at 5/5; density midpoint 50, Opus PASS / Gemini PASS; 5/5 levers traced; answer-leakage clean; 62/62 regression anchors.

Rubric ids below are **1-based** (R01..R64), matching the AUDIT report. Array indices are id minus 1.

---

## Part 1 — Forward coverage: every prompt ask has a rubric

| # | Prompt sentence / ask | Type | OE step(s) | Rubric(s) | Covered |
|---|---|---|---|---|---|
| P1 | "End of June was the target to have the Preventive Maintenance Push closed out. That came and went yesterday and it is still sitting open." | Framing + status ask | OE 3, OE 20 | R31, R64 | Yes |
| P2 | "I logged both cluster spot-checks as passing in late May and my read is that my part of it is finished." | Persona belief (Lever 9 anchor) — must be overturned, not confirmed | OE 12, OE 13, OE 14, OE 15 | R55, R53 | Yes |
| P3 | "The crew called the HVAC run wrapped around the same time." | Persona belief (Lever 1 anchor) — must be tested | OE 3, OE 5, OE 21 | R32, R57, R63 | Yes |
| P4 | "I need to know where every piece of it stands as of today, cluster by cluster" | Report to user (2.1) | OE 15-21 | R55, R56, R57, R58, R59, R60, R61, R62, R63, R64 | Yes |
| P5 | "and I need our records saying the same thing. Work out what is actually finished and what is not, and get our tracking to match." | Determination + reconcile | OE 9, OE 15, OE 17, OE 20 | not-finished: R55, R56, R57, R58, R59, R60, R61 · **finished: R62, R63** | Yes |
| P6 | "Anything still open gets its own tracking item raised" | Write (Linear issues) | OE 29, 30, 31, 32, 33 | R03, R07, R11, R15, R21-R23 | Yes |
| P7 | "with the person who owns that work named on it" | Write content (owner per item) | OE 29, 30, 31, 32, 33 | R06, R10, R14, R20, R24 | Yes |
| P8 | "My own spot-check records are part of that, with a short note left on each one saying where it landed and why." | Write (3 comments, atomic per record) | OE 34, OE 35 | R25, R26, R27 | Yes |
| P9 | "Anything flagged in the field that still needs a tech back onsite belongs in our maintenance ticket log rather than sitting as a tracking item" | Write (Airtable) + routing rule | OE 24, OE 25, OE 28 | R01, R02 (routing-flexible: R12, R17) | Yes |
| P10 | "and put a slot on my calendar to go back out and re-inspect whatever ends up in that follow-up" | Write (Calendar) | OE 22, OE 23, OE 36 | R28, R29 | Yes |
| P11 | "Then post where this stands in the channel the push has been running in so the crew is working off the same picture" | Write (Slack) + per-item content | OE 1, OE 7, OE 37 | R30, R31-R40 | Yes |
| P12 | "and draft an email to Brooke, cluster by cluster, with what is open, who is holding it, and what has to happen before this can close" | Write (Gmail draft) + per-cluster content | OE 26, OE 27, OE 38 | R41; open: R42, R44, R45, R46, R48; holder: R50, R51, R52; must-happen: R43, R47, R49 | Yes |
| P13 | "I do not want Brooke's email written so it can be read either way... say straight out that my earlier sign-off does not hold and this should not be treated as closeable yet, with the reasons." | Write content — two separable directives | OE 38 | R53, R54 | Yes |

**Forward-coverage gate: PASS.** Every explicit ask maps to at least one Outcome rubric. P5's "what is actually finished" half is covered by R62 and R63 — this was the AUDIT/Council B Major that the original draft missed.

### Cluster-by-cluster completeness check (P4 / P11 / P12)

| Cluster | Final response (2.1) | Channel post | Draft to Brooke | Holder in draft |
|---|---|---|---|---|
| South | R57 (open unit), R62 (electrical finished) | R32 | R42 open + R43 must-happen | R50 |
| North | R58 (flagged units) | R33 flagged + R34 access | R44 flagged + R45 access | R50 (access work) |
| East | R59 (unconfirmed), R63 (service recorded complete) | R35 | R46 open + R47 must-happen | R52 |
| West | R56 (coverage gap) | R36 gap + R37 latest status | R48 open + R49 must-happen | R51 |
| Portfolio (filters) | R61 | R38 | — (not a cluster) | — |
| Portfolio (plumbing) | R60 | R39 | — (not a cluster) | — |

---

## Part 2 — Reverse coverage: every rubric traces to a prompt ask

| Rubric | Prompt ask | OE anchor | Surplus? |
|---|---|---|---|
| R01, R02 | P9 | OE 28 | No |
| R03-R06 | P6, P7 | OE 29 | No |
| R07-R10 | P6, P7 | OE 30 | No |
| R11-R14 | P6, P7 | OE 31 | No |
| R15-R20 | P6, P7 | OE 32 | No |
| R21-R24 | P6, P7 | OE 33 | No |
| R25 | P8 | OE 34 | No |
| R26, R27 | P8 | OE 35 | No |
| R28, R29 | P10 | OE 36 | No |
| R30-R40 | P11 | OE 37 | No |
| R41-R52 | P12 | OE 38 | No |
| R53, R54 | P13 | OE 38 | No |
| R55-R64 | P4, P5 | OE 15-21 | No |

**Reverse-coverage gate: PASS.** No rubric goes beyond the prompt. No rubric grades an action the prompt assigns to the user rather than the agent (Gap 6 alignment check clean — every write in the set is one the prompt commissions).

---

## Part 3 — OE-to-rubric cross-reference (write OEs and user-asked discovery OEs)

| OE | Type | Covering rubric(s) | Aligned |
|---|---|---|---|
| OE 1-11, 24-27 | Read / discovery, not user-asked (channel resolution, board setup, contact lookup, mail sweep) | none required | N/A |
| OE 12, 13, 14, 15 | Read — load-bearing determination, user-asked | R55 | Yes |
| OE 16 | Read — user-asked (North flag disposition) | R33, R44, R58 (positive framing; absence is corroboration only) | Yes |
| OE 17 | Read — user-asked (South no-access) | R12, R32, R42, R57 | Yes |
| OE 18 | Read — user-asked (North access pending) | R13, R34, R45 | Yes |
| OE 19 | Read — user-asked (plumbing open) | R16, R39, R60 | Yes |
| OE 20 | Read — user-asked (West coverage gap + latest status) | R04, R05, R36, R37, R48, R56 | Yes |
| OE 21 | Read — user-asked (East unconfirmed) | R21, R22, R23, R35, R46, R59 | Yes |
| OE 22, 23 | Read — calendar precondition | R28 (new event, not an update) | Yes |
| **OE 28** | Write — Airtable ticket | R01 (1.1) + R02 (1.2) | Yes |
| **OE 29** | Write — West tracking item | R03 + R04, R05 + R06 | Yes |
| **OE 30** | Write — filter tracking item | R07 + R08, R09 + R10 | Yes |
| **OE 31** | Write — access tracking item(s) | R11 + R12, R13 + R14 | Yes |
| **OE 32** | Write — plumbing tracking item | R15 + R16, R17, R18, R19 + R20 | Yes |
| **OE 33** | Write — East position | R21, R22, R23 + R24 | Yes |
| **OE 34** | Write — note on OPS-87 | R25 | Yes |
| **OE 35** | Write — notes on OPS-96, OPS-98 | R26, R27 | Yes |
| **OE 36** | Write — calendar event | R28 (1.1) + R29 (1.2) | Yes |
| **OE 37** | Write — channel post | R30 (1.1) + R31-R40 (1.2, per item) | Yes |
| **OE 38** | Write — Gmail draft | R41 (1.1) + R42-R54 (1.2, per cluster + directives) | Yes |

**Every write OE has a 1.1 and, where the prompt specifies content, one or more 1.2 rubrics. Every user-asked discovery OE has a 2.1. No orphan OEs, no orphan rubrics.**

### OE-mandated decomposition directives — compliance

| OE directive | Complied |
|---|---|
| OE 29: one criterion per content element + separate owner criterion | Yes — R04, R05 content; R06 owner |
| OE 30: same, plus "no record shows completion" must NOT be a graded criterion | Yes — R08, R09 content; R10 owner; corroboration ungraded |
| OE 31: one criterion for South, one for North, plus owner; must pass whether one item or two | Yes — R12, R13, R14; both phrased location-agnostically |
| OE 32: one criterion per content element + owner; water heaters must accept either location | Yes — R16, R17 (dual-destination), R18, R19 + R20 |
| OE 33: one criterion per content element + owner; must accept tracking item OR the OPS-98 note | Yes — R21, R22, R23 + R24 (accept-set = tracking item or note) |
| OE 35: three atomic note criteria so a two-of-three agent fails exactly one | Yes — R25, R26, R27 |
| OE 37: per-item decomposition, never one enumerating criterion; grade destination descriptively | Yes — R31-R40; R30 accepts channel name or id |
| OE 38: split the cluster-by-cluster body one criterion per cluster (floor, not ceiling); two atomic directive criteria | Yes — R42-R49 exceed the floor; R53, R54 atomic |
| OE 28: no criterion may require or penalise a routing for the boundary residuals | Yes — R12 and R17 dual-destination; drain/compressor residuals ungraded |

---

## Part 4 — Hardness lever traceability (all 5 selected levers)

| Lever | Prompt sentence | OE step | Rubric carrier | Fact_Ledger / universe atom |
|---|---|---|---|---|
| **L2 — Structured-DB skip** (Linear `state_id`) | P2 "my read is that my part of it is finished" | OE 9, OE 12-15 | **R55** | OPS-87 `state_OPS_1`, OPS-96 `state_OPS_1`, OPS-98 `state_OPS_2` vs prose "moved to Done" |
| **L9 — Authority dismissal, persona-self** | P2 + P13 | OE 14, OE 38 | **R53** | OPS-98 comments 2026-05-25 09:00 / 14:00 |
| **L1 — Latching on the loudest wrap** | P3 "The crew called the HVAC run wrapped" | OE 3, OE 5 | **R57** (and R32) | Slack ts 1779308446.000005 "Every unit serviced" vs OPS-43 no-access unit |
| **L8 — Multi-link chain off Jaime's field note** | P8 "My own spot-check records are part of that" | OE 4, OE 16 | **R02** (and R33, R44, R58) | Slack ts 1779562423.000092 -> carrying issue -> disposition |
| **L5 — Thread-reply blindness** | P4 "where every piece of it stands" | OE 6 | **R09** (sole carrier) | Slack ts 1779569323.000012, `thread_parent_id` set; exists nowhere else |

**Lever gate: PASS — 5/5 traced on all four anchors.** Note carried to S4: L5 rests on R09 alone; the South no-access reschedule is *not* thread-exclusive (OPS-43's description and both comments carry it), so the plan's second L5 fact does not add independent lever coverage.

---

## Part 5 — Constraint compliance (Hardness Plan constraints 1-10)

| Constraint | Status |
|---|---|
| 1. F7 AMBIGUOUS_TARGET — no rubric pins one of Jaime's three interchangeable QC records the prompt names only by entity | PASS — every write graded is unique by construction (new issue, new ticket, new event, draft to a named recipient, post to the push channel). R25/R26/R27 pin OPS-87/96/98 individually, which is exact-by-enumeration, not ambiguous. |
| 2. F8 NON_ATOMIC_ENUM — no criterion enumerates 3+ items under a completeness predicate | PASS — deterministic F8 check clean; every multi-item ask decomposed. |
| 3. F9 UNRECONCILED_FUTURE_EVT | PASS — no rubric asserts Jaime's QC queue is otherwise clear or that the maintenance budget question is settled; the 2026-07-15 Mesa Vista 4C QC inspection and the 2026-07-23 budget review are uncontradicted. |
| 4. Gmail bodies base64 — no rubric depends on a fact reachable only inside an email body | PASS — Gmail is a write destination only (R41-R54). |
| 5. Channel-lock-in is Major by default | PASS — prompt names the method explicitly ("post ... in the channel", "draft an email"); R30 accepts channel name or id; validator open-goal-verb check does not fire (zero open-goal verbs in prompt). |
| 6. Do not build a rubric on OPS-91 | PASS — `OPS-91` returns 0 hits across all 64 x 3 fields. |
| 7. Do not build a graded criterion on an absence | PASS — R33/R44/R58 reframed to the positive fact with the absence demoted to optional corroboration; R04/R36/R48/R56 are bounded-enumeration claims (3 of 230 issues are Jaime's, none covers West), not open-world absences. |
| 7a. Scope the state claim to Jaime's three QC records, never the whole push | PASS — R55 is id-scoped with an explicit anti-generalisation FAIL guard; `OPS-40` returns 0 hits; R62 and R63 affirmatively put completed work on the record. |
| 8. Soft verbs on the prompt-side authority anchor | N/A to rubrics (S1 constraint, verified held). |
| 9. No escape-valve clause | N/A to rubrics (S1 constraint, verified held). |
| 10. Similarity pivot | N/A to rubrics (S1 constraint). |

---

## Part 6 — Gaps and surplus

- **Gaps:** none. Forward coverage 13/13 prompt asks; final-response coverage gate satisfied (10 x 2.1 criteria); every write OE mapped.
- **Surplus:** none. All 64 trace to a prompt ask and an OE anchor.
- **Non-failing note carried to FINAL (AUDIT N6, tagged `PROPAGATE TO S2`, wording-only, gates nothing):** OE 36's closing clause reads "is dated after 2026-07-01" while the same OE also permits "any future slot resolved from the current date of 2026-07-01". R28 takes the permissive branch ("on or after"). Recommended one-word OE fix: `is dated after 2026-07-01` -> `is dated on or after 2026-07-01`. Not applied here — editing `6_Oracle_Events.txt` is outside S3's scope.
- **Non-failing note (AUDIT N1):** no draft criterion names a holder for the two flagged North HVAC units. Deliberately not added: R50's accept-set already shares two of three names with the only grounded North accept-set on the same artifact and field, so adding it would reopen the overlap defect class closed at R24/R52.
