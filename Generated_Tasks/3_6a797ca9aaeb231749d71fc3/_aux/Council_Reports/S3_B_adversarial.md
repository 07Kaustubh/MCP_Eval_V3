# Council B — Adversarial QC — S3 Rubrics

**Task:** `Generated_Tasks/3_6a797ca9aaeb231749d71fc3`
**Universe:** `harmonygames` (framework `hg`, single-model verifier, Opus 4.7)
**Rubric set size:** 26 criteria (all categorized `outcome`, 0 `process`)
**Reviewer:** Council B — Adversarial QC
**Date:** 2026-08-12

Severity taxonomy applied is the HG pre-swap ordering: **Overly Broad = MODERATE, Overly Specific = MINOR** (`Rubric_Format.md` HG deltas + `7_QC_Spec_Doc1.json` Rubric dimension).

---

## Part 1 — QC Sub-Dimension Scoring (`Docs_harmonygames/7_QC_Spec_Doc1.json` Rubric dimension)

### 1a. Four-Field JSON Schema and Blank Fields — **FAIL (1/2)**

HG QC spec: *"Valid category values are `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, and `Process`."* Any object using an invalid category triggers `[Fail - Invalid Rubric Schema]`.

Observed: **all 26 rubrics use `"category": "outcome"` (flat lowercase form)**, which is the V3-family value, not the HG 4-value enum. `Reference/Rubric_Format.md` HG-deltas section is explicit that HG stores the sub-category in the `category` field itself.

Impact: schema hard-fail. This is one systematic defect but under the spec's per-criterion counting, all 26 criteria carry the issue.

**Severity: MAJOR (systemic — 26/26 criteria).**

### 1b. Overall Rubric Quality — **FAIL (1/2)**

Denominator = 26 (contributor criterion count). Highest severity per criterion.

| Bucket | Count | % | HG threshold |
|---|---:|---:|---|
| Major | 26 (schema) OR 1 (systemic) | 100% / 3.8% | Fail >10% |
| Moderate | 7 (see 1c below) | 26.9% | Fail >15% Moderate-or-Major |
| Minor | 0 |  | Fail >20% Minor-or-higher |

Even excluding the schema issue as one systemic finding (1 Major), the **Moderate-or-Major band still hits 30.8% (7 Moderates + 1 Major) — above the 15% Moderate-or-Major fail line**. FAIL under both readings.

**Severity: FAIL threshold breach.**

### 1c. Atomicity + Specificity Findings (per-criterion, feeding into 1b)

MODERATE findings (Atomicity / Overly Broad):

- **R2:** "identifies Combo-Fighters PR #1 as a draft with zero code changes and a \"do not merge\" label" — three independently-verifiable content items under one predicate. Rule 32 (Rubric_Format.md) and Guidelines Rule 2: 3+ items under a completeness predicate = not atomic. **MODERATE (Atomicity).**
- **R13:** "identifies Combo-Fighters PR #36 as merged on 2026-02-11 with substantial VFX content" — `substantial VFX content` is subjective / undefined. Guidelines Common Mistake 1 and QC spec Specificity, Accuracy, Acceptance: "Overly Broad or Undefined Acceptance." Ground truth is +22,309 additions / 2,568 changed_files; the rubric substitutes an ungrounded characterization. **MODERATE (Overly Broad).**
- **R16:** "distinguishes GitHub author \"Marcus\" from the three harmonygames.co Marcus mailboxes marcus.bennett@..., marcus.lee@..., marcus@..." — four identities under one completeness predicate. Split candidates: one criterion for the GitHub attribution, one per mailbox (or one for "the three harmonygames.co mailboxes are distinct from GitHub Marcus" if bundling that specific tuple is defensible). **MODERATE (Atomicity).**
- **R17:** "reports that ZM ROADMAP check_item \"Marcus to create VFX\" was toggled complete and \"Engineer to implement\" was left open, with reasons" — two independent state reports plus an undefined `with reasons` acceptance term. **MODERATE (Atomicity + Overly Broad, counted once at highest severity).**
- **R18:** "covers the Leapblock vendor followup and the Martin Walsh (martin.walsh@harmonygames.co) followup that Victor still owes" — two independent items in one completeness claim. Ground truth is two distinct vendor followups; each can pass or fail independently. **MODERATE (Atomicity).**
- **R19:** "states that parking draft PR #1 is safe on its own merits but the broader \"already covered\" framing overstates the position because PR #37 pushback and the \"Engineer to implement\" check_item are still open" — four bundled facts under one predicate: (a) parking safe, (b) framing overstates, (c) PR #37 pushback, (d) check_item open. **MODERATE (Atomicity).**
- **R26:** "attributes the merged Combo-Fighters VFX to GitHub \"Marcus\" (PERSON_0396_GITHUB_USERNAME) and states that this GitHub identity has no linked harmonygames.co email so mapping to a specific mailbox requires cross-service triangulation" — three items under one predicate. **MODERATE (Atomicity).**

Borderline / INFO (not counted):

- **R6:** "identifies the merged Combo-Fighters VFX author as GitHub \"Marcus\" (PERSON_0396_GITHUB_USERNAME) with no linked harmonygames.co email" — two facts, but the second is a factual property of the identified GitHub user record and reads as "same data point" per Guidelines Rule 2 bundling exception. Not flagged.
- **R20:** "creates a Google Sheets spreadsheet titled for the art vendor followups" — grammatically awkward ("titled for" is nonstandard) but delivers a flexible-title acceptance rule. INFO only.
- **R11:** "creates a Google Doc for the Monday-morning status brief for Leonard" — no title required. Acceptable given prompt says "a short status brief in a Drive doc I can send Leonard on Monday morning" (title not prompt-mandated).

### 1d. Rubric Category Balance — **PASS (5)**

HG rule: `Process <= 40%`, zero Process valid, no Outcome-majority requirement.
Observed: 26 Outcome + 0 Process = 0% Process. **PASS.**

### 1e. Process Rubrics — **N/A**

Zero Process rubrics present. QC spec: no failure path when zero Process.

However, **hard rule 23 check applies**: does the prompt contain an ordering/sequential dependency requiring a Process rubric? Scanning the prompt:

- "Start on the Combo-Fighters repo. Walk the pull-request history..." — describes an investigation sequence, but the OUTCOME rubrics (R1-R26) all check final state / content; no ordering-between-writes is prompt-mandated.
- "Once the picture is straight, put a reconciliation comment on the ART tracking ticket in Linear so the next person who picks this up sees the state, and update the affected roadmap card in Trello" — "Once the picture is straight" is investigation-precedes-writes, which is trivially enforced by the writes' content depending on evidence discovered. No inter-write ordering.
- "Then write me a short status brief... and put the vendor followups... in a fresh sheet" — no order between the brief and the sheet is prompt-mandated.
- "Tell me in the reply whether the reconciliation actually supports Leonard's 'treat it as parked' read" — reply is the last action but timing is not scored.

**No prompt-mandated ordering dependency exists.** Zero Process is correct. PASS.

### 1f. Agent-Centric Affirmative Phrasing — **PASS (5)**

All 26 titles use `The Agent` or `The Agent's` (possessive form) as subject. Possessive form is explicitly allowed by the Guidelines ("The Agent's message to Brian includes..."). QC spec Non-Fail band for possessive is "3/4 Rating," but the possessive is the recommended shape for content criteria on the agent's own artifact, so the spec's Pass(5) reading applies here.

No artifact-as-subject constructions, no tool names in titles.

**PASS.**

### 1g. Negative Criteria (HG-specific gate — rule 31) — **PASS (5)**

Two-stage pre-scan (`does not`, `must not`, `never`, `no`, `without`, `fails to`, `avoids`) applied to all 26 titles:

- **R6:** "with no linked harmonygames.co email" — `no` as noun-phrase head (`no [linked email]`). Only names reported content; actor and verb are affirmative (`identifies`). Per HG QC spec `:291`: "The Agent reports that PR #438 had no human-submitted review" is the canonical accepted shape. **PASS.**
- **R8:** "leaves Trello check_item ... in the incomplete state" — affirmative preserved-state construction (`leaves ... unchanged`). Guidelines Rule 5 explicitly names this as the correct pattern. Evidence field contains a negative check (`confirm no update sets check_item id X to state complete`), but that is inspection-side wording, not title-side. **PASS.**
- **R12:** "identifies PR #1 as a draft with zero code changes" — `zero` is a negative-factual quantity, actor/verb affirmative. Acceptable factual-state reporting.
- **R15:** "identifies PR #37 as merged with unresolved CHANGES_REQUESTED" — `unresolved` is a QC-spec-permitted negative factual state when affirmatively reported. **PASS.**
- **R26:** "no linked harmonygames.co email" — same as R6 shape.

**Zero negations on the Agent's own VERB. PASS.**

### 1h. Vague Exemplar Language (HG-specific gate) — **PASS (5)**

Grep for `such as`, `e.g.`, `for example` across all 26 rubrics' titles, justifications, and evidence fields returns **zero hits**. **PASS.**

### 1i. Duplicate Rubrics — **PASS (5)**

Pair-scan for same-requirement / same-artifact / same-signal:
- R2 (ART comment: PR #1 draft) vs R12 (status brief: PR #1 draft) — different artifacts (Linear comment vs GDoc). Distinct.
- R3 (ART comment: PR #36 merged) vs R13 (status brief: PR #36) — different artifacts.
- R4 (ART comment: PR #16) vs R14 (status brief: PR #16) — different artifacts.
- R5 (ART comment: PR #37 unresolved) vs R15 (status brief: PR #37) vs R24 (reply: PR #37) — three artifacts, three distinct destinations. All required by the prompt separately.
- R6 (ART comment: Marcus) vs R16 (status brief: 4 Marcuses) vs R26 (reply: Marcus) — three artifacts. Distinct.

**No duplicates.** PASS.

### 1j. Requirement Coverage and Destination — **PASS (5)**

Prompt sentence-by-sentence coverage:
- "put a reconciliation comment on the ART tracking ticket in Linear" — R1 write + R2-R6 content ✓
- "update the affected roadmap card in Trello" — R7 (check_item complete), R8 (check_item left incomplete) ✓
- "Leave a comment there on what still needs owner attention" — R9 write + R10 content ✓
- "close out any checklist items that the merged code actually finished" — R7 ✓
- "write me a short status brief in a Drive doc I can send Leonard on Monday morning" — R11 write + R12-R19 content ✓
- "put the vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet" — R20 write + R21, R22 rows ✓
- "Tell me in the reply whether the reconciliation actually supports Leonard's 'treat it as parked' read, or whether I need to push back on it" — R23 (parking), R24 (push back), R25 (Engineer to implement), R26 (Marcus attribution) ✓

All authorized deliverables covered on their correct artifacts. **PASS.**

### 1k. Self-Containment and Verifiability — **PASS (5)**

Every title carries the acceptance-bearing values in-line: PR numbers, dates, checklist IDs, emails, check_item IDs, card ID, ART ticket ID (per operator carryover). Judge does not need to open evidence to know what passes.

**PASS.**

### 1l. All-Failing Rubrics — **N/A**

No trajectories yet. Deferred to S4.

### 1m. Grounding — **DEFER to Council A** (per instruction).

---

## Part 2 — Adversarial Checks

### B1. Alt-Path — Valid Trajectory Failing Over-Specific Outcome

Attempted: construct a valid path that satisfies the prompt but fails a rubric due to over-specification.

- **Ground-truth check:** all pinned values (PR #1/#16/#36/#37 numbers and merge dates, Trello card / check_item IDs, ART-770, PERSON_0396, three Marcus mailboxes, martin.walsh@harmonygames.co) are the unique universe records satisfying the prompt's semantic ask.
- **Method-agnostic paths:** the prompt does not require a specific Slack channel, specific document format, or specific title. R11 asks for a GDoc (prompt-mandated: "a short status brief in a Drive doc"), R20 asks for a Sheet (prompt-mandated: "put ... in a fresh sheet") — both method-mandated by prompt language, so not over-specification.
- **Author identification:** R6, R16, R26 all name `PERSON_0396_GITHUB_USERNAME`. GitHub `harmonygames-Games/Combo-Fighters` PR #36 author is exactly this login. An agent that names only "Marcus" without the GitHub login token would fail R6 — but the prompt says "be specific about which Marcus" and the ONLY disambiguator for this Marcus is the GitHub login (no linked email exists). This is prompt-required specificity, not over-specification.

**No alt-path hit found.** R13's "substantial VFX content" is Overly BROAD (already flagged in 1c), not Overly Specific.

### B2. Reverse-Coverage — Rubric Beyond Prompt Scope

Every rubric traced to a prompt clause and/or an OE write action (see 1j above). No rubric grades a beyond-prompt requirement.

**No hit.**

### B3. Tool-Call Density Projection

Enumerate the reads and writes needed to satisfy the full rubric set:

| Bucket | Calls | Service |
|---|---:|---|
| List Combo-Fighters PRs (OE 1) | 1 | github |
| Get PR #1, #16, #36, #37 detail (OE 2, 5, 6, 7) | 4 | github |
| Reviews on PR #1, #37 (OE 3, 8) | 2 | github |
| PR comments on PR #1, #37 (OE 4, 9) | 2 | github |
| Other merged Marcus PRs (OE 10: #3, #5, #6, #7, #11, #12, #13, #22, #27, #33) — detail + reviews | 20 | github |
| GitHub user PERSON_0396 (OE 11) | 1 | github |
| Contacts Marcus + Leapblock + Martin Walsh (OE 12, OE 14a) | 3 | contacts |
| Linear users Marcus (OE 13) | 1 | linear |
| Drive list Victor recent (OE 14b) | 1 | gdrive |
| GameOfDominoes Leapblock scan (OE 14c) | 2 | github |
| Trello boards, lists, cards, card detail, checklists, checklist items, card actions (OE 15-21) | 8 | trello |
| Sibling card checklist descent (OE 22) | 1-3 | trello |
| Linear ART VFX search + get_issue (OE 23-24) | 2 | linear |
| Writes: Linear comment (OE 25), Trello update_check_item (OE 26), Trello comment (OE 27), GDoc create (OE 28), GSheet create (OE 29), reply | 6 | linear + trello + gdocs + gsheets |
| **Total midpoint (rounded up sibling fallback)** | **56** | 7 services |

Cross-check vs Hardness_Plan projection of **56 midpoint across 7 services** — matches exactly. Confirmed against 41-72 range in Hardness_Plan density table.

**Verdict: PASS on HG authoring target (40+ calls, 3+ services) AND on the V3-family 50+ design target.** No THIN_DENSITY / BLOCK risk.

### B4. Hardness Lever Preservation

For each of L1/L2/L6/L9/L10, name at least one rubric whose passing depends on the agent traversing that lever:

| Lever | Rubric coverage |
|---|---|
| **L1 Latching** (PR #1 as stale anchor, real work in PR #36/#16) | R2 (must identify PR #1 as draft/no-code), R3 (must identify PR #36 merged), R4 (must identify PR #16 merged), R12 (brief: PR #1 draft), R13 (brief: PR #36 merged), R14 (brief: PR #16 merged). **6 rubrics anchor this lever.** ✓ |
| **L2 Structured-DB skip** — GitHub review_comments carrier | R5 (comment: PR #37 CHANGES_REQUESTED), R10 (Trello card comment: PR #37 CHANGES_REQUESTED), R15 (brief: PR #37 pushback), R24 (reply: PR #37 CHANGES_REQUESTED). Agents that skip `github_list_review_comments` on PR #37 will fail all four. ✓ |
| **L2 Structured-DB skip** — Trello check_items carrier | R7 (update `Marcus to create VFX` to complete), R8 (leave `Engineer to implement` incomplete), R17 (brief covers both toggle decisions), R25 (reply: `Engineer to implement` still open). Agents that skip `trello_get_check_items` will fail these. ✓ |
| **L6 Marcus disambig** (4 Marcuses, GitHub Marcus has no linked email) | R6 (ART comment: attribute to GitHub Marcus PERSON_0396 with no linked email), R16 (brief distinguishes 4 Marcuses), R26 (reply attributes correctly with triangulation caveat). Agents that skip Contacts + Linear cross-reference will fail these. ✓ |
| **L9 Authority dismissal** (Leonard's "treat as parked") | R19 (brief pushes back on "already covered" framing), R23 (reply: parking supported), R24 (reply: push back). Agents that accept Leonard's dismissal wholesale will fail R19, R24. ✓ |
| **L10 Reversal / supersession** (PR #1 superseded by #36/#16; stale Trello check_items) | R3 (PR #36 merged), R4 (PR #16 merged), R7 (toggle Marcus to create VFX complete — the supersession act), R13 (brief), R14 (brief). Agents that miss the supersession fail these. ✓ |

**All 5 levers preserved with rubric coverage.** ✓

### B5. Atomicity — Per-Rubric Split Analysis

Already covered in Part 1c. Confirmed split candidates: R2, R13, R16, R17, R18, R19, R26. All flagged MODERATE.

### B6. Single-Target Uniqueness (Hard Rule 13)

- **ART-770** — operator ruling in `_aux/Reasoning/S3_S2_carryover.md` accepted. Under OE 24's fallback (satisfied unconditionally because zero fresh unresolved ART VFX tickets exist), the resolution is deterministic and unique. ✓
- **Trello card 6851a9942b47001e59c8e777** — single Equipped Card Item Infusion VFX card. ✓
- **check_item 6855f20fb11687de8c0be3c8** (`Marcus to create VFX`) — single. ✓
- **check_item 6855f2153528bf8d9fb8e116** (`Engineer to implement`) — single. ✓
- **PR #1, #16, #36, #37** — single each on `harmonygames-Games/Combo-Fighters`. ✓
- **PERSON_0396_GITHUB_USERNAME** — single GitHub user "Marcus" with no linked email. ✓
- **marcus.bennett@harmonygames.co, marcus.lee@harmonygames.co, marcus@harmonygames.co** — three distinct roster personas. ✓
- **martin.walsh@harmonygames.co** — single roster persona. ✓

**All pinned targets are unique.** ✓

### B7. Cross-Artifact Consistency (Prompt / OE / Rubric Triangle)

- Prompt "art tracking ticket in Linear" — OE 24 resolves to ART-770 via fallback — R1 pins ART-770. Consistent under operator ruling. ✓
- Prompt "if a merged PR still has review pushback that never got resolved, that counts as still open" — OE 8 identifies PR #37 CHANGES_REQUESTED unresolved — R5, R10, R15, R24 all use this framing. Consistent. ✓
- Prompt "close out any checklist items that the merged code actually finished" — OE 20 identifies Marcus to create VFX as finished-by-merge, Engineer to implement as still open — R7 (toggle complete) + R8 (leave incomplete) match. Consistent. ✓
- Prompt "be specific about which Marcus" — OE 11-13 disambiguate 4 Marcuses — R6, R16, R26 all specify PERSON_0396 + the three mailboxes. Consistent. ✓
- Prompt "put the vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet" — OE 14 + 29 identify both vendors + Martin Walsh's internal email — R20, R21, R22 match. Consistent. ✓
- Prompt "Tell me in the reply whether the reconciliation actually supports Leonard's 'treat it as parked' read, or whether I need to push back" — R23 (supports parking) + R24 (push back on broader framing) split the reply's two required assertions. Consistent. ✓

**No triangulation contradiction.** ✓

**One nuance flagged INFO only:** R22 calls `martin.walsh@harmonygames.co` "the internal owner." Martin Walsh IS a harmonygames.co employee per PersonaBrief and the roster, so "internal owner" is factually correct, but "the internal owner of the Martin Walsh row" reads slightly circularly. Not a defect.

---

## Part 3 — Overall Verdict

**BLOCK** — one MAJOR systematic schema defect and seven MODERATE atomicity/specificity defects. The MAJOR alone triggers `[Fail - Invalid Rubric Schema]` on the Four-Field JSON Schema sub-dimension; the Moderate cluster additionally breaches the Overall Rubric Quality Moderate-or-Major threshold (26.9% > 15%).

Note: the pipeline validator canonicalizes `outcome` to the internal bucket and may report green, but the HG QC spec's strict schema check requires the 4-value enum. STOP shipping.

### Per-Finding REVISE Plan

| # | Severity | Rubric(s) | Defect | Fix |
|---|---|---|---|---|
| F1 | **MAJOR** | R1–R26 (all) | Schema — `"category": "outcome"` is not a valid HG value. HG QC spec `Four-Field JSON Schema` requires one of `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, `Process`. | For each rubric assign the correct sub-category: 1.1 for write-action results (R1, R7, R8, R9, R11, R20), 1.2 for write-action content (R2–R6, R10, R12–R19, R21, R22), 2.1 for reply/final-response facts (R23–R26). Update `"category"` field accordingly across all 26. |
| F2 | MODERATE | R2 | Atomicity — bundles (a) draft status, (b) zero code changes, (c) "do not merge" label under one predicate. | Split into three: "The Agent's ART-770 comment identifies Combo-Fighters PR #1 as a draft (state = open, draft = true)." / "The Agent's ART-770 comment states that PR #1 has zero code changes (0 additions, 0 changed files)." / "The Agent's ART-770 comment names the \"do not merge\" label on PR #1." |
| F3 | MODERATE | R13 | Overly Broad — `substantial VFX content` is undefined/subjective. | Rewrite as: "The Agent's status brief identifies Combo-Fighters PR #36 as merged on 2026-02-11 as the substantive VFX import (+22,309 additions across 2,568 files)." — or split the merge fact from the content-scale fact. |
| F4 | MODERATE | R16 | Atomicity — four identities under one `distinguishes` predicate. | Split: one for GitHub author identification ("The Agent's status brief identifies GitHub author \"Marcus\" (PERSON_0396_GITHUB_USERNAME) as the author of the merged Combo-Fighters VFX and states this GitHub identity has no linked harmonygames.co email."), plus three per-mailbox distinctness rubrics OR one combined ("The Agent's status brief names the three harmonygames.co Marcus mailboxes marcus.bennett@harmonygames.co, marcus.lee@harmonygames.co, and marcus@harmonygames.co as distinct from the GitHub author."). Recommend the 2-rubric split. |
| F5 | MODERATE | R17 | Atomicity — two independent state reports; and Overly Broad on `with reasons`. | Split into two: "The Agent's status brief reports that the ZM ROADMAP check_item \"Marcus to create VFX\" was toggled to complete because PR #36 shipped the merged VFX." / "The Agent's status brief reports that the ZM ROADMAP check_item \"Engineer to implement\" remains incomplete because Combo-Fighters PR #37 carries unresolved CHANGES_REQUESTED." |
| F6 | MODERATE | R18 | Atomicity — two independent vendor followup items. | Split: "The Agent's status brief covers the Leapblock vendor followup Victor still owes." / "The Agent's status brief covers the Martin Walsh (martin.walsh@harmonygames.co) followup Victor still owes." |
| F7 | MODERATE | R19 | Atomicity — four bundled facts under one predicate. | Split into (at minimum) two: "The Agent's status brief states that parking draft PR #1 is safe on its own merits (no code, no reviews)." / "The Agent's status brief states that the broader \"already covered\" framing overstates the position because Combo-Fighters PR #37 pushback and the ZM ROADMAP \"Engineer to implement\" check_item are still open." — the second is still 2-fact but they are the same causal reason. Consider three-way split if strict atomicity is required. |
| F8 | MODERATE | R26 | Atomicity — three items (attribution + no-email + triangulation caveat). | Split into two: "The Agent's reply attributes the merged Combo-Fighters VFX to GitHub \"Marcus\" (PERSON_0396_GITHUB_USERNAME)." / "The Agent's reply states that GitHub \"Marcus\" has no linked harmonygames.co email so mapping to a specific mailbox requires cross-service triangulation." |

### Ancillary INFO (not counted as defects, worth polishing)

- **R6:** could optionally split into attribution + no-email but the bundling exception under "same data point" applies; leave as is.
- **R20:** phrase "titled for the art vendor followups" reads awkwardly. Consider "The Agent creates a Google Sheets spreadsheet with a title related to the art vendor followups (or similar)."
- **R11:** no title specified; prompt does not require one. OK as is.

### Downstream Effects

- After F1 is fixed (systemic schema): Overall Rubric Quality Major-count drops to 0, so the sub-dim then depends on how many of F2–F8 are collapsed by splitting. Splitting typically INCREASES the rubric count (26 → ~34) and pushes the count toward the pipeline 60-criterion ceiling, but well under.
- After F2–F8 splits: expected Moderate count drops to 0. Overall Rubric Quality would then PASS(5).
- Lever coverage preserved through all splits (splits only tighten discrimination, not loosen).
- No re-run of S2 needed unless the OE 24 ART resolution ruling is overturned.

### Iteration Cap

Per pipeline convention (S3 REVISE up to 3 rounds), one revise round should be sufficient because all findings are localized to rubric wording, not structural changes.

**Verdict: BLOCK. Apply F1–F8, resubmit for S3 Council B re-check.**
