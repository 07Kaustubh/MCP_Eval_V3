# OE solvability (interim - cap-hit escalation)

## OE-to-prompt coverage map
- P1..P5 (draft PR / import framing / PR history) -> OE 1-10
- P6 (Marcus disambiguation) -> OE 11-13
- P7 (vendor followups Leapblock + Martin Walsh) -> OE 14, OE 28(e), OE 29
- P8..P9 (ZM ROADMAP board, checklist items) -> OE 15-22
- P10 (ART tracking ticket reconciliation comment) -> OE 23-25
- P11 (close finished checklist items) -> OE 26
- P12 (comment on the affected roadmap card) -> OE 27
- P13 (Monday-morning status brief) -> OE 28
- P14 (vendor tracker sheet) -> OE 29
- P15 (reply: parked or push back?) -> OE 30

**Every prompt sentence maps to at least one OE step. No coverage gaps.**

## OE-to-rubric preview (for S3)
- Outcome 1.1 (write result): OE 25 (Linear comment), OE 26 (check_item close), OE 27 (Trello comment), OE 28 (GDoc), OE 29 (GSheet) - 5 write-action rubrics
- Outcome 1.2 (content check): OE 28 decomposes into 6 content criteria (a)-(f); OE 29 decomposes into 3-4 vendor-row content criteria; OE 25 decomposes into 4-5 content criteria on the comment body; OE 27 decomposes into 2 content criteria on the sibling engineer identification
- Outcome 2.1 (final response fact): OE 30 seeds 3 reply criteria (park-vs-pushback verdict; which Marcus owns which piece; which line-items remain open)
- Process (ordering): none needed; the write actions are order-agnostic
- Negative constraint: OE 26 companion rubric (agent must NOT close "Engineer to implement" check_item)
- Ambiguous target flag: **F1-r3 unresolved** - OE 24/25 target row not deterministic across two grammatically-valid readings of the OE 24 predicate. S3 rubric must anchor on Council-A-verified target after operator decides the OE 24 rewrite path.

## AUDIT verdicts (3 rounds)
- R1 AUDIT: REVISE (F1 ART-768 pinning, F2 OE 29 conditional, F3 Todos, F4 phase-order false positive, F5 Leapblock coverage, F6 Ozhan orphan, F7 OE 22 loose param, F8 OE 25 chain not bound)
- R2 AUDIT: REVISE (F1-r2 empty-set predicate on OE 24, F2-r2 loose atom claim on OE 22)
- R3 AUDIT: REVISE cap hit (F1-r3 predicate ambiguity on OE 24: two grammatically-valid readings converge on different rows; AUDIT-proposed inline rewrite unifies them deterministically to ART-770)

## Escalation summary
Both Council A and Council B verdicts are GO through R3. The single residual is a nuance in OE 24's predicate wording where the R3 fix intended a fallback-to-most-recent resolution but the primary predicate's "most recent live-state ART VFX work" disjunct pre-empts the fallback under a naive reading, resolving to ART-760 rather than ART-770. AUDIT proposes a concrete rewrite that removes the ambiguity by making the freshness qualifier explicit on the primary and dropping the two-branch structure. Under that rewrite, both readings converge to the same target (ART-770) because the freshness filter yields zero rows in this universe.

**Not REBUILD:** the OE set is structurally sound (7 services, 30 well-formed steps, correct HG-strictness posture, correct persona-scope, correct density at midpoint 54-56, all other findings closed across 3 rounds). Escalation is procedural (cap hit), not structural.

Density projection (R3): 41-72 range with midpoint 54, 7 services (github, contacts, linear, trello, gdrive, gdocs, gsheets). Clears the STRICT V3-family 50+ bar and the HG 40+ authoring target with margin.

All 5 Hardness_Plan levers preserved through R3 (L1 latching, L2 structured-DB skip both variants, L6 Marcus disambiguation, L9 authority dismissal, L10 reversal/supersession).
