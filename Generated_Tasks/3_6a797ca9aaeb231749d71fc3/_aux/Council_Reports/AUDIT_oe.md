# AUDIT — OE (Strictest Veteran Interpretation)

**Framework:** `hg` (HarmonyGames V5)
**Persona:** Victor Barnes (`victor.barnes@harmonygames.co`, Engineering)
**Universe today:** 2026-02-28 (Saturday, America/Chicago)
**Model under test:** Claude Opus **4.7** (universe-scoped exception per AGENTS.md rule 1)
**Deliverable:** `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/6_Oracle_Events.txt` — 32 OE steps
**Mode:** on-demand (fresh chat), --phase oe. Read-only.

Interpretation contract: every "should" is "must"; only 5/5 is acceptable on every applicable QC sub-dim; density bar is 50+ midpoint (V3-family strict) on top of the HG authoring target of 40+ calls AND 3+ services.

---

## Section 1 — Preamble (v18 required)

Universe = `harmonygames` per `_aux/Universe.txt`. Doc set: `Docs_harmonygames/`. Eval set: `Evals_harmonygames/`. Tool catalog: `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` + capability authority `HarmonyGames_Base_Universe/Tool_Access/*.json`. Persona ACL doc: `Docs_harmonygames/14_Persona_ACL.md` (four services unscoped: contacts, github, trello, linear; seven scoped). QC spec: `Docs_harmonygames/7_QC_Spec_Doc1.json`, Section OE.

Validator: PASS 0/0/3 (universe=hg, 32 OE steps, no closed fiscal periods so lifecycle-precondition check was skipped).

---

## Section 2 — Strict QC scoring, OE dimension

Citing `Docs_harmonygames/7_QC_Spec_Doc1.json` OE sub-dimensions.

| OE sub-dim | Score | Reason under STRICT interpretation |
|---|---:|---|
| `OE / Completeness` | **3/5** | The prompt asks for the "vendor followups I still owe Leapblock and Martin Walsh". The OE only issues `contacts_search_contacts` for Leapblock (Council A already confirmed Leapblock is NOT in `contacts.contacts`; the query returns empty) and a broad `gdrive_list_recent_files` with no Leapblock filter. No `trello.cards` search, no `github.pull_requests` search on Leapblock (Council A: 27 Drive hits, 2 Trello hits, 7 GameOfDominoes PR hits — all Victor-reachable, none traversed). The tracker OE (OE 31) creates the sheet but no read step gathers Leapblock followup content. Result: one prompt-mandated deliverable is under-covered. Strict 5/5 requires each prompt ask to have a materialised discovery step ending in a verifiable atom. |
| `OE / Accuracy` | **4/5** | 30 of 32 steps ground cleanly against the split. Two accuracy concerns: (i) OE 24 pins `id "ART-768"` **or** "the closest live-state ART Zombie Match 3D VFX tracking ticket" — a dual-target OE cannot be Accurate in a single reading; (ii) OE 22 issues `trello_get_checklists_on_board` scoped to a card, but `Tool_Access/trello-tools.json` treats checklists as board-level (scoping is a post-filter, not a call parameter). The step is still executable but the parameter framing is loose. |
| `OE / Negative Events` | **5/5** | No negative-event asks in the prompt (nothing of the "confirm X did NOT happen" shape). N/A but scored full per the spec convention that N/A → 5/5 on this sub-dim. |
| `OE / Cross-service` | **5/5** | 7 distinct services touched (github, contacts, linear, trello, gdrive, gdocs, gsheets). Clears HG 3+ floor by 4. |
| `OE / Investigation before Action` | **4/5** | OE 25 (`gdrive_list_recent_files`) sits AFTER the Marcus disambiguation reads but BEFORE the writes, which is correct in ordering. However OE 25's expected result is described as scoping context; no specific artifact is bound to a downstream write. Writes (OE 26 / 27 / 28 / 30 / 31) do not chain through OE 25 evidence. Under strict reading, investigation-before-action requires the discovery to inform the write choice, not merely precede it. |
| `OE / Coherence with Prompt` | **3/5** | See Rule 13 finding F1 below. OE 24 and OE 26 pin `ART-768` and `checkItemId 6855f20fb11687de8c0be3c8` etc., while the prompt only says "the ART tracking ticket" and "any checklist items that the merged code actually finished". OE hard-codes identifiers the prompt does not name — coherence is preserved when identifiers are content-bound in OE evidence and left unnamed in the prompt; hard-pinning without prompt authority pushes the coherence score below 5. |

**Two applicable sub-dims below 5 → REVISE.**

---

## Section 3 — End-to-end trace: every step to (a) prompt sentence AND (b) Fact_Ledger atom

Prompt sentences (P1–P11 numbered by line):
- P1 anchor (Leonard's Friday dismissal)
- P2 backstory (placeholder-asset burn)
- P3 "walk PR history since December, merged and unmerged"
- P4 "if merged PR still has review pushback that never got resolved, that counts as still open"
- P5 "if a draft PR has no code in it at all, note that separately"
- P6 "cross-check that against the Zombie Match 3D roadmap board"
- P7 "read the checklist items on those cards, not just the card names"
- P8 "Get the owner attribution right. More than one Marcus. GitHub author not always tied to a company email"
- P9 "put a reconciliation comment on the ART tracking ticket in Linear"
- P10 "update the affected roadmap card... close out any checklist items that the merged code actually finished"
- P11 "short status brief in a Drive doc"
- P12 "vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet"
- P13 "Tell me in the reply whether the reconciliation actually supports Leonard's 'treat it as parked' read"

Fact_Ledger atoms: 47 emails / 41 amounts / 1078 dates / 3859 linear issue ids / 987 slack channel ids (unused here) / 8783 trello card ids / 53702 gdrive file ids / 17 declared personas.

| OE | Prompt tie | Atom tie | Orphan? |
|---|---|---|---|
| 1 | P3 | `github.pull_requests` PRs #1, #37 (verified in Council A grounding table row 4) | no |
| 2 | P5 | PR #1 draft state atoms (Council A row 4) | no |
| 3 | P5 | PR #1 reviews (zero) | no |
| 4 | P5 | PR #1 pull_request_comments | no |
| 5 | P3, P4 | PR #36 merged 2026-02-11 (Council A row 5) | no |
| 6 | P3 | PR #16 merged 2025-12-21 (Council A row 5) | no |
| 7 | P4 | PR #37 merged 2026-02-13 | no |
| 8 | P4 | PR #37 reviews CHANGES_REQUESTED | no |
| 9 | P4 | PR #37 review_comments (10, per Council A row) | no |
| 10 | P3 | 10 Marcus-authored PRs enumerated | no |
| 11 | P8 | `github.users` PERSON_0396 empty email (Council A row 10) | no |
| 12 | P8 | 3 Marcus contacts in `contacts.contacts` (Council A row 2) | no |
| 13 | P8 | 3 Marcus `linear.users` rows | no |
| 14 | (context only) | `contacts.contacts` ozhan@harmonygames.co (Fact_Ledger emails line) | **weak** — orphan re: prompt: no prompt sentence names Ozhan. Justified by persona brief context, but strict reading: OE not tied to a prompt sentence. |
| 15 | P12 | Leapblock: search returns empty; Martin Walsh: `contacts.contacts` `contact_id=51f5f16d46e8cf55f5ee337b` | partial — Leapblock leg produces no atom |
| 16 | P6 | `trello.boards` ZM ROADMAP `6851a6569f3bf818760632ab` | no |
| 17 | P6, P7 | `trello.lists` on that board | no |
| 18 | P6 | `trello.cards` including `6851a9942b47001e59c8e777` | no |
| 19 | P7 | `trello.cards` card details | no |
| 20 | P7 | `trello.check_items` `Marcus to create VFX` incomplete + `Engineer to implement` incomplete (Council A row 9) | no |
| 21 | P7 | `trello.actions` toggle history | no |
| 22 | P6 | 2 sibling cards; **checklist scoping call is loose** (see Section 2 Accuracy note) | no |
| 23 | P9 | `linear.teams` `team_ART` (597 issues) | no |
| 24 | P9 | `linear.issues` ART-768 **OR** "closest live-state" — dual target | **defect** (see F1) |
| 25 | P11, P12 | `gdrive.drive_files` recent (persona-scoped read: OK, Victor-owned) | no |
| 26 | P9 | Write `linear.save_comment` — dual target inherited from OE 24 | **defect** (see F1) |
| 27 | P10 | Write `trello.update_check_item` on Marcus-VFX check_item | no |
| 28 | P10 | Write `trello.add_comment` on primary VFX card | no |
| 29 | P10 | Write `trello.add_comment` on sibling; **conditional "Skip this OE only if..."** | **defect** (see F2) |
| 30 | P11 | Write `gdocs.create_document` (create is write-unscoped) | no |
| 31 | P12 | Write `gsheets.create_spreadsheet` — sheet content is empty at creation | partial — sheet has no rows; Leapblock/Martin Walsh followup rows never populated by a preceding read step |
| 32 | P13 | Final reply text | no |

**Orphans / partial-orphans:**
- **OE 14** (Ozhan) — no prompt sentence names Ozhan. Persona-brief context only. Under strict interpretation this is a bolt-on OE; either the prompt needs to name him or OE 14 comes out.
- **OE 15 Leapblock leg** — no atom returned; the Council A grounding note ("Leapblock NOT in contacts.contacts; groundable via Drive/Trello/GitHub") was surfaced back to S2 and S2 encoded the failing contacts search anyway.
- **OE 25 → OE 30/31 chain** — the recent-Drive-files discovery is described as "scoping context" but nothing in OE 30 (status brief) or OE 31 (vendor tracker) binds a returned file to specific content. The write steps do not consume OE 25's output.

---

## Section 4 — Density re-derivation from OE text (STRICT bar 50+ midpoint)

Re-counted tool calls per OE, ignoring the Hardness_Plan projection:

```
OE 1..9:  9 calls (1 each)
OE 10:    20 calls (10 PRs x 2: get_pull_request + get_pull_request_reviews)
OE 11..14: 4 calls
OE 15:    2 calls (2 contacts searches)
OE 16..19: 4 calls
OE 20:    2 calls (get_checklists_on_board + get_checklist)
OE 21:    1 call
OE 22:    4 calls (2 get_card + 2 get_checklists_on_board)
OE 23..25: 3 calls
OE 26..31: 6 calls (writes)
OE 32:    0 (reply)
--------
TOTAL:    55 tool calls midpoint (range roughly 41-72 accounting for OE 10's per-PR sweep variability and OE 22's conditional descent)
```

**Density verdict, STRICT V3-family reading (50+ midpoint):** PASS at 55. Clears by 5.
**Density verdict, HG authoring target (40+ calls AND 3+ services):** PASS (55 calls, 7 services).
**Density verdict, HG prompt-eval hard gate (>15 NECESSARY calls AND 2+ services):** PASS.
**Density verdict, HG trajectory QC floor (>=15 avg):** PASS.

No density REVISE. However, OE 10 (`for each of 10 PRs, 2 calls`) is heavily front-loaded onto one OE step and drives the count. If the agent instead performs `github_list_pull_request_reviews` in bulk, the actual density drops. Not a blocker at this phase; flag for S4 trajectory review.

---

## Section 5 — Todos_s2.md cross-check (v11 E1 gate)

Read `_aux/Todos_s2.md`. **All 22 items are UNCHECKED (`- [ ]`).** Per AGENTS.md v11 E1, the discipline gate requires every step marked completed or in-progress at the point the phase claims exit. Under strict interpretation this is a hard defect — either the operator did not maintain the file or ran the steps without ticking. Either way the artifact of record fails the gate.

**Finding F3 (HIGH) — Todos_s2.md v11 E1 discipline gate FAIL. All 22 items unchecked.**

---

## Section 6 — Verification_s2.md exit requirement

`_aux/Verification_s2.md` **does not exist** (directory listing confirms only `Verification_hardness.md` + `Verification_s0.md` + `Verification_s1.md`). Per S2 runbook TODO #20 and AUDIT.md Step 0.5, `Verification_s2.md` must be written before the S2 phase declares complete. This is an **exit requirement**, not a per-OE finding — flagged and carried into the verdict conditions.

---

## Section 7 — Adversarial trigger list (S2 runbook Track F v21) — MANDATORY vs OPTIONAL determination

Re-checking whether AUDIT auto-fire was **mandatory** given the state at S2 exit:

| Trigger | State at S2 exit | Fires MANDATORY? |
|---|---|---|
| (a) Council B NON-FAIL band justifications | Council B report absent from `_aux/Council_Reports/` (only S1_A, S1_B, AUDIT_prompt present) — the S2 Council A + B reports were **never produced** | **unknown → treat as fire** |
| (b) validator WARN | 0 warns per `Validator_Reports/oe.md` | no |
| (c) atom-verifier flags | Not run at S2 gate (no atom-verifier report file present) | **unknown → treat as fire** |
| (d) OE revisions this pass | Unknown (no revision log); no draft-vs-final diff | **unknown → treat as fire** |
| (e) OE → rubric forward-map gap | S3 not yet run, so forward-map cannot be checked. Would be evaluated at S3 phase, not here | N/A at S2 phase |

**Determination:** AUDIT auto-fire is **MANDATORY** under the STRICT reading because three of the five triggers (a, c, d) cannot be evidenced as clean and the S2 Council A + B reports are **absent from disk**. The v21 conditional-OPTIONAL branch requires ALL of "uniform 5/5 + clean validator + clean atom-verifier + first-pass" to hold; ONLY the validator is provably clean.

**Corollary defect: Section 8 councils missing.** The AUDIT contract in `Reference/Sessions/AUDIT.md` line 11 states: "the `_aux/Council_Reports/AUDIT_<phase>.md` report with `PASS (STRICT)` is the exit criterion **when AUDIT fires**". AUDIT fires AFTER Council A + Council B. Running AUDIT without the two upstream councils is **out-of-order**. This audit report is written under the operator's explicit invocation, but the finding stands: F4 (HIGH) — S2 Council A + B reports missing from `_aux/Council_Reports/`.

---

## Section 8 — HG-specific strictness

### Persona-scoped reads
- **Drive read (OE 25)**: `gdrive_list_recent_files` with `limit 25`. Expected description: "files owned by or shared with victor.barnes@harmonygames.co". Persona-scope contract HELD. ✓
- No `gdocs_get_document` / `gsheets_get_spreadsheet` reads issued. All Docs / Sheets use is create-write (OE 30 / OE 31), which is not ACL-governed. ✓

### Slack — ZERO tolerance
Grepped OE for `slack`: **0 hits**. Zero Slack reads, zero Slack writes. Consistent with Hardness_Plan revision 2026-08-12: Victor is a member of zero channels of any type, so any Slack step would be a REBUILD-level defect. ✓

### Gmail — ZERO send/reply/compose/draft
Grepped OE for `gmail`: **0 hits**. HG gmail is read-only (no send / reply / compose / draft tool exists). No gmail read step either. ✓

### Retired servers — ZERO tolerance
Grepped OE for `snowflake`, `confluence`, `wiki`, `knowledge base`, `bigquery`, `firebase`, `airtable`, `quickbooks`, `stripe`: **0 hits** on any of them. ✓

### Rule 13 single-target uniqueness
- **OE 24 (target: `ART-768` OR closest live-state)**: The prompt says "the ART tracking ticket in Linear" — a definite article with no unique-identifier binding. `linear.list_issues` on team_ART with query "VFX" returns "many historic ART VFX tickets (ART-252, ART-102, ART-768, ART-790)" (OE 23 verbatim). Multiple candidate rows exist. The OE pins `ART-768` while offering "or the closest live-state ART Zombie Match 3D VFX tracking ticket" as an escape. Under Rule 13 this is **AMBIGUOUS_TARGET** — either the OE names the one row by CONTENT (title / body binding) and the prompt is left generic, or the prompt is amended to select uniquely. Currently the OE pins an identifier the prompt does not name AND admits alternates. Downstream at S3, a rubric that pins ART-768 by identifier has no prompt authority. **Finding F1 (MODERATE)**.
- **OE 26 (write target: same ART-768 OR "the ART-team ticket resolved in OE 24")**: Inherits F1. Write action locks on the same ambiguous target.

### Rule 13 Calendar sweep
HG has no `gcal` in this task's `_aux/Universe_Split/` (directory listing shows no `gcal.*` files). Per HG-U11 (`v4_gates.py` skips F9 for HarmonyGames), the every-service Calendar sweep is manual for HG. **Confirmed no-op here.** ✓

### Rule 14 mirroring (OE decompose directives ↔ rubric carriers)
Not applicable at OE phase (rubrics not yet drafted). Carried into S3 as a MUST-DO: any content element named in an OE `S3 must decompose this into one criterion per content element` directive must be mirrored into the rubrics in the same pass. This OE set contains no explicit `S3 must decompose` directive — that itself is a MINOR S3-handoff gap because OE 15 (Leapblock+Martin Walsh in the tracker) needs per-vendor atomic rubrics and OE 20 (check_items) needs per-item atomic rubrics.

---

## Section 9 — Findings summary (tagged per rule 91)

| ID | Severity | Sub-dim mapping | Location | Finding |
|---|---|---|---|---|
| **F1** | MODERATE (Overly Specific) | OE / Coherence with Prompt; Rule 13 AMBIGUOUS_TARGET | OE 24, OE 26 | `ART-768` pinned by identifier where prompt only says "the ART tracking ticket"; dual-target "or closest live-state" clause makes even the OE-internal target non-unique. |
| **F2** | MINOR (Overly Broad) | OE / Unique Ground Truth | OE 29 | Conditional "Skip this OE only if the merged VFX genuinely does not touch either sibling's scope" turns a graded write into an optional one. OEs must be non-conditional. |
| **F3** | HIGH (Discipline gate) | v11 E1 (`Todos_s2.md`) | `_aux/Todos_s2.md` | All 22 TODO items unchecked at S2 exit. |
| **F4** | HIGH (Phase order) | AUDIT.md contract | `_aux/Council_Reports/` | S2 Council A + B reports missing on disk; AUDIT auto-fired out of order per the Track F conditional table (three triggers cannot be evidenced as clean). |
| **F5** | MODERATE (Coverage) | OE / Completeness | OE 15, OE 25, OE 31 | Prompt asks for Leapblock followups. OE runs empty `contacts_search_contacts` and a broad `gdrive_list_recent_files`; no `trello.cards` search, no `github.pull_requests` search on Leapblock; the sheet in OE 31 is created empty with no preceding read step populating the two vendor rows. |
| **F6** | MINOR (Orphan) | OE / Coherence with Prompt | OE 14 | Ozhan lookup has no prompt-sentence tie. Persona-brief-only context. Either extend prompt or drop OE 14. |
| **F7** | MINOR (Loose parameter) | OE / Accuracy | OE 22 | `trello_get_checklists_on_board` scoped to a card conflates board-level and card-level tool semantics per `Tool_Access/trello-tools.json`. |
| **F8** | MINOR (Investigation→Action chain) | OE / Investigation before Action | OE 25 → OE 30 / 31 | Discovery step precedes writes but is not consumed by them; writes do not reference specific Drive artifacts surfaced by OE 25. |

**Exit requirement not yet met:** `_aux/Verification_s2.md` must be written before S2 declares complete (Section 6).

---

## Section 10 — Per-issue fixes (for REVISE)

| Finding | Fix in place |
|---|---|
| F1 | Rewrite OE 24 to describe the ART ticket by CONTENT ("the ART-team issue whose title or body ties Zombie Match 3D VFX import work; if multiple match, the most recently updated one") and drop the identifier `ART-768` from the OE body. Move the identifier into the OE's "Expected" evidence field only. Same treatment for OE 26 (`issueId` becomes "the ART issue resolved in OE 24" and no identifier is stated in the write step). |
| F2 | Rewrite OE 29 as non-conditional: either the sibling comment is a mandatory write and the OE binds the write to the sibling card whose scope IS affected (name the card by content), or OE 29 comes out. No "Skip this OE only if..." language. |
| F3 | Operator: mark each Todos_s2.md item completed with a one-line evidence pointer (validator report path, council report path, atom check). |
| F4 | Run S2 Council A (grounding + convention) and S2 Council B (adversarial + density + hardness preservation) and save as `_aux/Council_Reports/S2_A_grounding.md` and `_aux/Council_Reports/S2_B_adversarial.md`. Re-invoke AUDIT after both PASS. |
| F5 | Add OE steps between OE 15 and OE 25: (a) `trello_get_cards_on_board` with a Leapblock filter on the ZM ROADMAP and any other Victor-reachable boards; (b) `github_list_pull_requests` on GameOfDominoes (7 Leapblock hits per Council A); (c) `gdrive_search_files` scoped to Leapblock. Then bind OE 31 tracker rows to specific atoms returned by (a)-(c). |
| F6 | Either add one sentence to `5_Prompt.txt` naming Ozhan as part of the "vendor followups" (requires re-running S1.5) or drop OE 14. |
| F7 | Rewrite OE 22's second call as `trello_get_checklists_on_board` at board level (unfiltered) followed by an explicit filter step in the "Expected" field naming the two sibling cardIds. |
| F8 | Bind OE 30's "bodyText" and OE 31's sheet-row expectations to specific `gdrive.drive_files` returned by OE 25 (name the file titles the agent must reference). |

---

## Section 11 — Verdict

**REVISE.**

Three moderate-or-higher findings (F1, F3, F4, F5) and four minor findings (F2, F6, F7, F8). Two applicable QC sub-dims below 5 under STRICT reading (`Completeness` at 3/5; `Coherence with Prompt` at 3/5). Exit requirement (`Verification_s2.md`) not yet met.

Iteration cap: 3 per S2 runbook. Operator applies fixes in place, re-runs `validate.py --phase oe` + S2 Council A + S2 Council B, then re-invokes AUDIT.

If the S2 councils, once run, both return uniform 5/5 AND the fixes above collapse F1 / F2 / F5 / F7 / F8 to no-op, then AUDIT can be re-scored to PASS (STRICT). F3 (Todos discipline) and F4 (missing councils) must be closed regardless.

Density is not a blocker (55 midpoint clears both the strict V3-family 50+ and the HG 40+ authoring target with margin). Slack / Gmail / retired-server / persona-scope checks all clean.

---

## Verdict line

**VERDICT: REVISE**
