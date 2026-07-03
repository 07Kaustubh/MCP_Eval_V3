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
