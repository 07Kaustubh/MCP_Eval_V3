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

## 2026-08-08 — Task 2 (`Generated_Tasks/2_6a6beba55996ad2ada369b15`) — Four OE-prose defects reached the reviewer with every gate green

**Reviewer feedback:** "Great prompt great rubrics, just a few issues in oracle events." Four items, all in `6_Oracle_Events.txt`, none touching a criterion. `_aux/Validator_Reports/oe.md` reports **PASS, 0 fails, 0 warns**; `AUDIT_oe.md` scored the OE set on density and prompt-alignment and never inspected these claims.

**Grading impact: zero.** The rubrics say "the warehouse serves whole dollars" (correct) and every pinned figure is the tool-visible one, so no criterion moves and no run re-scores. This is an OE-hygiene retro, not a re-grade.

| # | Reviewer item | Verified verdict |
|---|---|---|
| 1 | OE 8/10/11 claim the warehouse "stores whole dollars"; storage is decimal, rounding is a per-row derivation | **Valid — a real false claim.** `snowflake.tables.json` holds `spend_usd` 53.57 / 29.44 / 27.76. The column is declared `NUMBER` with no scale, so the hydrated DuckDB casts each row half-up on retrieval. OE 8 states it as a storage property; OE 10 and 11 inherit the mechanism from that one sentence. |
| 2 | OE 16 count off: "130 text-bearing" vs 132 Feb messages | **Criticism valid, characterization not.** Robert authored 132 February messages in `C07C2866011`; exactly 130 have non-empty `text`; 2 are file-only image posts. The number was right as qualified. The defect is the *choice* of a qualified count. |
| 3 | OE 24/26 Trello list mislabeled "UA/BD board" instead of "BD Follow Up" | **Fix right, "mislabeled" overstated.** `670015c2ecd45b634d5eec81` resolves to list `BD Follow Up` on board `UA/BD`. The OE named the board correctly and never named the list — under-specified, not false. |
| 4 | OE 28 is meta/grading commentary, not a tool-use event | **Valid, and it violates our own written rule.** `Evals_harmonygames/2_OE_Eval.md`: "An OE must describe an affirmative tool-use step." |

## Root causes

**R1 — Mechanism sentences are not verified like values are.** The OE Eval has a Numeric Observability hard gate, and it worked: every figure in task 2 is the tool-visible one. Nothing checks the *sentence that explains why* the figure differs from the source. That sentence is load-bearing because **sum-of-rounded != round-of-sum**: OE 11 reads "345 as the warehouse serves it and 346.00 exactly," which is a visible arithmetic error unless the per-row cast is stated alongside it. Same shape in OE 8 (7,476 vs 7,483.42, round = 7,483) and OE 10 (8,447 vs 8,452.64, round = 8,453).

**R2 — Author-side reference notes are an unverified input.** The "warehouse stores whole dollars" phrasing came verbatim from an operator reference note carried between HarmonyGames tasks. The note was written from observed tool output and asserted a storage mechanism that was never checked against the schema. A wrong mechanism in a carried note propagates to every later task in that universe silently, because no phase re-derives it.

**R3 — Reviewer-reproducibility is not a grading criterion anywhere.** Items 2 and 3 contain no false statement. Both fail the same test: a reviewer who resolves the ID or re-runs the count gets a different string than the one sitting next to it in the prose. Supporting evidence in an OE exists to be re-checked cheaply; a qualified count and a parent-object label both defeat that.

**R4 — No per-OE structural check exists.** `validate.py` `validate_oe()` checks OE count, opening-verb ratio (aggregate, 60% threshold — 27/28 passed), unknown tool names, param traps, channel IDs, formatting. It never asks whether an *individual* OE names a tool. OE 28 passes every one of those.

## Optimizations proposed

### O6 — `validate.py`: rounding-pair consistency check (catches item 1)

In `validate_oe()`, for every OE matching `<N> ... (serves|returns) ... <M> exactly`, parse both numerals. If `round(M) != N`, require per-row rounding language (`per row`, `each row`, `sum of the rounded`) inside the same OE block; warn otherwise. This makes the mechanism sentence mandatory exactly where its absence produces an apparent arithmetic error, and stays silent on the ordinary case where the two renderings agree.

Ban the storage framing outright: fail on `warehouse|table|column ... stores ... whole (dollar|number)`. The correct framing is tool-return — "`snowflake_execute_query` returns each row rounded half-up."

### O7 — `validate.py`: ID-label resolution check (catches item 3)

Extract quoted IDs from `6_Oracle_Events.txt`, resolve them in `_aux/Universe_Split` (list/channel/board/space/team/file), and warn when the resolved object's own `name` does not appear within ~60 chars of the ID. Deterministic, cheap, and generalizes past Trello to `channel_id`, Linear `team`, Confluence `space`, gdrive `fileId`.

Authoring rule: the name nearest an ID is the name that ID resolves to; the container comes second and is labelled as such — `idList "670015c2ecd45b634d5eec81", the "BD Follow Up" list on the UA/BD board`.

### O8 — S2 authoring rule: scope counts are the naive count (catches item 2)

Counts that exist only to establish read scope or corroboration state what the obvious query returns. If a distinction genuinely matters, carry both: "132 February messages, 130 of them text-bearing." Discriminating figures — windows, totals, entity sets — stay strict; this narrows nothing that separates runs.

### O9 — `validate.py`: per-OE tool-presence check (catches item 4)

Split on `^OE \d+`, flag any block containing no catalog tool name, with the final-response OE the single exemption. Criterion-design rationale (decoy-to-criterion maps, "carries no criterion because the persona cannot reach it") moves to `_aux/Reasoning`. Note that trailing rationale *clauses* inside a real OE survived review — task 2's OE 17 and OE 20 both carry them. Only a whole event made of commentary is the defect.

**Blocked on O10 — do not ship O9 first.** Run against task 2 as-is, the check false-flags 17 of 28 OEs.

### O10 — `validate.py`: fix `TOOL_NAME_HINT` (prerequisite for O9, and a live gap on its own)

`Validators/validate.py:85` requires a *middle* token from a fixed verb list (`list|search|get|create|update|send|add|...`), i.e. it only matches `service_<verb>_noun`. Measured against HarmonyGames `6_Server_Tools_Details.json`: **276 tools, 215 matchable, 61 blind (22%)**. The blind set includes the names tasks lean on hardest — `snowflake_execute_query`, `slack_conversations_history`, `gdrive_read_file`, `gdrive_search`, `confluence_search`, `github_push_files`, `gdocs_batch_update`, `gcal_patch_event`, `gmail_archive_thread`.

Both the prompt check (line 528) and the OE unknown-tool check (line 718) use this regex, so **a hallucinated tool name of that shape passes `validate.py` silently today.** Replace the verb-shaped regex with a direct match against the loaded catalog set from `load_tool_names()`.

### O11 — Re-derive carried mechanism claims at S2 (root cause R2)

Any operator reference note asserting *why* a universe behaves as it does — not just what value it returns — is re-derived against the schema before it enters OE prose. The task-2 note was corrected in place: storage is decimal, `NUMBER` carries no scale, the cast is per-row at retrieval.

## Estimated pipeline effect

O6, O7, O9 and O10 are deterministic and run in seconds inside the existing `validate_oe()` pass; together they catch three of the four reviewer items at S2, before AUDIT. O8 and O11 are authoring rules with no tooling cost. O10 is worth shipping regardless of the rest — it is the only item here that can hide a *false* claim rather than an imprecise one.

## Log

Task 2's four items were all Non-Fail OE issues and cost nothing on this task. They are logged because the class is cheap to eliminate and because R2 shows this universe's carried notes can seed the same defect into every later HarmonyGames task. Correcting the note is what stops the recurrence; O6 is what catches it if another one slips.
