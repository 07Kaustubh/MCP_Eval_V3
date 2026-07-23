# Pipeline Improvement Notes

Cross-task retros on where the pipeline missed defects that later surfaced. Each entry names a specific miss and the proposed optimization.

---

## 2026-07-01 — Task 35 (`Tasks/35_6a4421ec8169e23828bb442d`) — Persona-attribution mis-labeling propagated through 4 pipeline phases

**What was missed and when caught:** rubrics R10/R13/R18 attributed the 04-14 post-termination LOS access workstream to **Marcus Webb**. Universe explicitly names **Evan Mercer** (Slack C008 04-14 12:22/12:28/12:50/13:22 + email "Evan Mercer LOS access disabled" + `contacts_contact_387de5925670` job="Former Loan Officer" status=inactive). Marcus Webb is a distinct still-active-with-resignation identity (`mortgage_los.staff` `termination_date: None, is_active: True`) with a separate solicitation narrative.

The defect was **caught only in S4** during the user-triggered universe deep-query. Every prior pipeline phase certified the wrong attribution as universe-grounded:

| Phase | What it did | Why the miss propagated |
|---|---|---|
| S3 grounding | Verified atom text existence: "loan_number exists in mortgage_los.loans", "atom body verbatim in `crm_engagement_XXX`", "workstream label matches". Did NOT grep universe for the ENTITY NAME against workstream keywords. | The CRM engagements at 11:01/11:07/11:12 use generic "Former employee post-term access under review" language — the person name is NOT in the CRM chain. S3 grounding matched the atom text without cross-checking Slack. |
| S3 adversarial council | Ran alt-path analysis on R10 ("agent posts aggregate 'four wholesale-portal-breach files identified via CRM engagement d27cd1da0d5a' WITHOUT listing IDs. Would fail R8."). Did NOT question the workstream persona-label. | The council's threat model focused on alt-answer paths, not on whether the rubric's entity attribution was universe-truthful. |
| AUDIT_rubrics | Explicit KeyStone anchor KS-4 "Marcus Webb NPC / departed-employee trap" said: "Marcus Webb appears in the rubrics ONLY in his correct role (former LO whose post-term LOS access is the 4/14 CRM workstream). ✓ PASS." | AUDIT confirmed "correct role" by cognitive salience, not by universe grep. Marcus was the salient recent-departure name in operator memory. AUDIT did not check the Slack thread that names Evan Mercer explicitly. |
| FINAL_council | Ran answer-leakage scan for "Marcus Webb" as a prompt-leakage keyword. Verdict: zero hits (prompt clean). | Answer-leakage scan is prompt-vs-rubric leakage, NOT rubric-vs-universe factual grounding. The check was oriented to prevent the AGENT from being pre-fed answers, not to catch a factually-wrong rubric. |
| 6 platform agent runs | 6/6 agents also wrote "Marcus Webb" for the 4/14 post-term workstream. Judge accepted "Marcus Webb" attribution because rubric said the same. | Systemic: agents grounded on the same salient-name heuristic as the rubric author. Run 3 alone caught the correct attribution ("Evan Mercer post-termination access") + the LN drift, but the pre-Round-2 rubric graded it as Fail because the rubric expected Marcus. |
| S4 universe deep-query (this phase) | Grep `Slack.slack_messages` for "evan" + "post-term" / "LOS access" and for "marcus" + "post-term". Found 4 Slack messages on 04-14 explicitly naming Evan Mercer; found 0 Slack messages on 04-14 naming Marcus for post-term. Also read `mortgage_los.staff` and confirmed Marcus is `is_active: True, termination_date: None`. | The deep-query surfaced the defect because it queried the ENTITY NAME AGAINST WORKSTREAM KEYWORDS, not the atom text. |

## Root cause of the systemic miss

**Cognitive-salience anchoring.** Marcus Webb has a highly salient story in this scenario (03-25 resignation + 03-27 solicitation + spouse-agent conflict + 3/27 borrower-directed transfer requests). Evan Mercer has a small, quiet story (single Slack thread on 04-14 12:22/12:28 + email "Evan Mercer LOS access disabled" + contacts row). When the CRM chain uses generic pronoun-labels ("Former employee"), rubric authors, AUDIT reviewers, FINAL reviewers, AND agents all default-attach the salient name. The less-salient departed employee gets overwritten by the more-memorable one.

**Grounding-pass depth mismatch.** S3 grounding verifies atom EXISTENCE (does LN-XXX exist? does the CRM engagement body match?). It does not verify atom ATTRIBUTION (does the person named in the rubric appear in the universe alongside the workstream keywords?). Attribution grounding is a strictly harder check because it requires cross-referencing multiple universe sources, not just confirming atom presence in one source.

## Optimizations proposed

### O1 — Add persona-attribution cross-check to S3 grounding (Reference/Sessions/S3.md)

For every rubric that names a specific PERSON alongside a workstream label ("[Person] post-termination access workstream", "[Person]'s account activity", "the 4/14 [Person] audit"), the grounding pass MUST perform this additional query:

```python
# Pseudocode — persona attribution grep
person_name = extract_person_from_rubric(rubric.title + rubric.evidence)
workstream_kw = extract_workstream_keywords(rubric.title)  # e.g., "post-term", "LOS access", "4/14"

hits_person_with_workstream = grep_universe_communications(
    where=(person_name in text) AND any(kw in text for kw in workstream_kw)
)
if hits_person_with_workstream == 0:
    flag("Entity attribution unverified — no universe atom co-occurs [person] with [workstream_kw]. Deep-query required.")
```

Rejection criterion: if the named person's name does NOT co-occur with the workstream keywords in ANY universe communication, the attribution is likely wrong. Deep-query alternative candidates.

### O2 — Extend AUDIT_rubrics regression anchors with a "reverse-groundedness on named entities" check

Current AUDIT_rubrics regression anchors verify tool-name factuality (KS-1..KS-5), retention codes (KS-2), channel routing (KS-3), etc. Add a new anchor:

- **KS-9 (proposed): Persona-attribution reverse-groundedness.** For every named person in every rubric, confirm at least one universe communication where that person's name co-occurs with the rubric's workstream keywords. If zero co-occurrence exists, flag as Major.

This catches the exact defect Task 35 R10/R13/R18 had.

### O3 — Extend FINAL_council to include a "named-entity reverse-groundedness" section

Current FINAL_council does answer-leakage scan (prompt-vs-rubric leakage). Add a section:

- **Named-entity reverse-groundedness (proposed).** Enumerate every unique person name across all rubric titles/evidences. For each, confirm at least one universe atom that grounds the attribution to their assigned workstream. Zero-atom person names are Major defects.

### O4 — S3 adversarial council should include an "entity-swap alt-path" check

Current S3 adversarial council considers alt-answer paths (aggregate vs specific IDs, memo vs email surfaces). Add an entity-swap check:

- **Entity-swap alt-path (proposed).** For every rubric that names a specific person alongside a workstream label, ask: is there a DIFFERENT person in the universe who could ALSO plausibly be attributed to this workstream? If YES and both persons appear in adjacent universe atoms, the attribution is ambiguous and needs stronger anchoring or explicit person-verification in the rubric.

For Task 35 R10, this would have surfaced: "There are TWO departed-employee narratives on this task (Marcus resignation/solicitation + Evan post-term access). Which does the 4/14 workstream refer to? Grep universe for the explicit name." The adversarial council would have caught the ambiguity at S3.

### O5 — Add a "persona-attribution landmine" section to the Reference/Hardness_Playbook.md

Document the pattern as a first-class hardness lever so future rubric authors are aware of the trap. Cite Task 35 as the canonical example.

## Estimated pipeline effect

Adding O1 + O2 + O3 to the standard runbook would have caught the Task 35 defect at S3 grounding (earliest point). The additional grep cost is small: 5-15 seconds per rubric that names a person. The false-positive rate should be low because most person-named rubrics have clear universe grounding (e.g., "notifies Megan Sloane at megan.sloane@wardbarrettlaw.com" grounds trivially).

O4 catches ambiguity at the S3 council-of-2 phase — before the platform even sees the rubric.

O5 puts the pattern in the operator's mental model.

## Log

Referenced this improvement note from the S4 memory file [[persona_attribution_landmine]]. Future audits on multi-departure scenarios should surface this pattern from Phase 0.

---

## 2026-07-24 — Task 40 (`Tasks/40_6a61a86a31b9c973b2021ba5`, StarPM V4) — Enumerated `(a)(b)(c)` narrative bundle survived every defense layer

**Scope:** This defect + fix applies to **StarPM V4 tasks only**. The ML July 2026 atomicity rule is defined in `Docs_starpm/8_QC_Spec_Doc2.md` + `Evals_starpm/3_Rubrics_Eval.md` and is not part of Brookfield / Keystone / MoveOps spec authority. Task 40 is the only observed StarPM-native instance of this defect. Non-StarPM tasks with similar bundling shapes are not evidence for this rule because those tasks were authored under different spec authorities where enumerated bundles were permitted.

**What was missed and when caught:** Task 40 (StarPM V4) shipped 16 rubrics of which 8 used the `(a)(b)(c)` narrative-bundle shape (rubrics 3, 5, 7, 9, 11, 13, 15, 16 per `_aux/Council_Reports/AUDIT_rubrics.md` Lens 3 table). Every pipeline defense layer PASSED them. The platform verifier then forced atomic decomposition: 16 → 49 rubrics (3× expansion) via multiple linter iterations.

| Phase | Verdict | Why the miss |
|---|---|---|
| `validate.py` rubrics | PASS (0 fails, 15 warns unrelated to bundling) | `AND_BUNDLING` regex requires two write verbs joined by AND. Task 40 titles use one verb + `(a)(b)(c)` enumeration — different pattern. `v4_gates.py` F6.1 (v4-only WARN) only fires on 2+ money/ID/email atoms joined by "and"; also missed. |
| Council A A13 | GO | A13 targets open-ended asks + multi-recipient sends. Did not cover enumerated content element bundling in a single 1.2 rubric on one artifact. |
| Council B B6 | GO — `_aux/Council_Reports/S3_B_adversarial.md:151` verbatim: *"Bundled (a)(b)(c) narrative rubrics per Rubric_Format.md. Bundling is permitted 'when a single write action contains multiple interconnected parts of the exact same request'. Matches V3 reference-task Task 11 rubric 6 and Task 14 rubric 3."* | Cited V3 pre-July-2026 refs as precedent + used the "interconnected" clause in Rubric_Format.md:30 as escape hatch. |
| AUDIT_rubrics STRICT | PASS — `_aux/Council_Reports/AUDIT_rubrics.md:289` verbatim: *"I considered flagging bundled rubrics 3, 7, 9 as potential AND-bundling violations under strictest atomicity reading, but decided fine because they follow the V3 single-artifact narrative-bundle pattern (matches Task 11 rubric 6, Task 12 rubric 12, Task 14 rubric 3). HELD."* | Same V3-precedent-rationalization pattern. AUDIT self-documents the rationalization but does not have a Lens item that prohibits it. |
| Platform verifier | FORCED SPLIT | 16 → 49 rubrics via multiple linter passes. |

## Root cause of the systemic miss

**Pre-July-2026 "interconnected parts" escape hatch + cross-universe V3 precedent citation.** `Reference/Rubric_Format.md:30` allowed bundling when a single write action contained "multiple interconnected parts of the exact same request". This clause is inherited from Brookfield V3 spec authority and remains correct for Brookfield / Keystone / MoveOps tasks. The July 2026 ML update tightened atomicity for StarPM V4 to "if the criterion fails, there is EXACTLY ONE clear reason why", which directly conflicts with the "interconnected parts" language on the `(a)(b)(c)` shape when applied to StarPM V4: escalation + $1,850 + Thursday retention are three independent investigation outcomes that CAN fail independently, even though all three land in one Airtable `fldDescription` write. V3 reference tasks (Task 11/12/14, Brookfield) shipped under Brookfield spec authority and became precedent that Council B + AUDIT wrongly cited to defend the shape on a StarPM V4 task. The bug was the cross-universe precedent citation, not the V3 tasks themselves — those remain correct within Brookfield.

## Optimizations applied (2026-07-24)

### O1 — Add ENUMERATED_BUNDLE + NUMBERED_BUNDLE + MULTI_RECIPIENT_SEND regexes to `validate.py`, gated on `universe == "starpm"`

Three new FAIL-level regexes in `Validators/validate.py` (rubrics phase), guarded by `if universe == "starpm":` so they fire only for StarPM V4 tasks:
- `ENUMERATED_BUNDLE` catches `(a) X (b) Y ...` in a title.
- `NUMBERED_BUNDLE` catches `(1) X (2) Y ...` and `1) X 2) Y` and `1. X 2. Y`.
- `MULTI_RECIPIENT_SEND` catches "The Agent [sends/drafts/emails] to A, B, and C" style single-verb multi-recipient sends.

All three FAIL with a message citing the StarPM V4 atomicity rule (ML July 2026) + the same-record-attributes exception. Recourse for legitimate same-record bundles is S1.5 justification. Brookfield / Keystone / MoveOps tasks are unaffected — the older "interconnected parts" bundling exception still holds for them.

Empirical verification: all 5 Task 40 bundled titles (R3/R7/R9/R13/R15) CAUGHT by ENUMERATED_BUNDLE under `universe == starpm`. Zero false positives on 4 legitimate same-record natural-phrasing rubrics from the V3 reference set. Under `universe == moveops` the same enumerated-bundle title PASSES (verified via `StarPM V4 gate — (a)(b)(c) does NOT flag on non-StarPM universe` regression anchor).

### O2 — Tighten `Reference/Rubric_Format.md` atomic rule + flexibility row + anti-patterns

- Line 30 atomic-rule row: replaced "interconnected parts of the exact same request" language with the ML July 2026 "one clear reason to fail" test verbatim, plus the same-record-attributes exception carve-out.
- Line 70 flexibility table: removed the "Multiple required elements → `must include: (a) ..., (b) ..., (c) ...`" row that literally authorized the pattern we want to ban. Replaced with "Multiple attributes of the same record → natural comma phrasing on one record, no `(a)(b)(c)` enumeration".
- Anti-patterns section: added enumerated-bundle + multi-recipient-send anti-patterns as ML-confirmed July 2026 items.
- Grandfather note added: V3 reference tasks shipped pre-rule are NOT precedent for new work in any universe.

### O3 — Add multi-content-element sub-rule to Council A A13

`Reference/Council_Protocol.md` A13 gains a `**Multi-content-element sub-rule (ML-confirmed July 2026):**` block parallel to the existing multi-recipient sub-rule. Explicit BLOCK verdict format `MULTI_CONTENT_BUNDLED: ...`. Notes that V3-precedent-rationalization is not a valid defense.

### O4 — Add KS-10 anchor to AUDIT.md Lens 5

`Reference/Sessions/AUDIT.md` Lens 5 gains a KS-10 anchor citing the enumerated-content-bundling pattern by name. AUDIT_rubrics must now explicitly test for the shape and cannot rationalize past it using V3 precedent.

### O5 — Add 3 regression anchors to `Validators/test_regression_anchors.py`

- "Enumerated (a)(b)(c) bundle in rubric title (ML July 2026)" — expects `enumerated element bundling` in output.
- "Numbered (1)(2)(3) bundle in rubric title (ML July 2026)" — expects `numbered element bundling`.
- "Multi-recipient send bundle in rubric title (ML July 2026)" — expects `multiple recipients under a single write verb`.

All 51 regression anchors pass (48 pre-existing + 3 new).

### O6 — Update `AGENTS.md` V4 Spec Changes table

Added a new row for "Atomicity — enumerated content bundles (Jul 2026 extension, post-Task-40)" describing the escape pattern and the fix.

### O7 — Do NOT promote `v4_gates.py` F6.1 WARN → FAIL

Oracle plan-review verdict: F6.1 fires on a different pattern space (2+ value atoms + literal "and"). Would not have caught Task 40 titles anyway (they lack "and" between atoms). Promoting removes the escape valve for legitimate structured-field bundles like "The Agent creates a bill with vendor $X and terms Net-30". Keep F6.1 as WARN.

## Estimated pipeline effect

Applied at S3 validator step. Task 40's 5 bundled titles would have FAILed at validator time — before Council A / Council B / AUDIT ran on the bundled shape. Operator would have either split them immediately or hit S1.5 for justification. Either path is cheaper than the multi-round post-platform-linter atomization actually experienced (`_aux/Linter_Decision.md` documents rounds).

## Log

Referenced from `Tasks/_meta/Learnings.md` L34. Regression anchors ensure this catch cannot silently regress. If a future rubric legitimately needs the `(a)(b)(c)` shape for a same-record bundle, the S1.5 justification path handles it — no need to loosen the regex.
