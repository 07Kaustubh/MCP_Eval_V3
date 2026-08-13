# S2 Council B — Adversarial QC on `6_Oracle_Events.txt`

Task: `Generated_Tasks/3_6a797ca9aaeb231749d71fc3` · Universe: `harmonygames` (framework `hg`) · Model under test: Claude Opus 4.7 · Today: 2026-02-28 (Saturday, America/Chicago) · Persona: Victor Barnes (`victor.barnes@harmonygames.co`, Engineering).

Adversarial posture: try to break the OE list. Every "5" requires zero Major AND zero Moderate.

---

## Section 1 — QC sub-dim scoring

Authority: `Docs_harmonygames/7_QC_Spec_Doc1.json` entry index 4 ("Oracle Event (OE)"). All OE sub-dims are individually non-failing (Fail = N/A). Landing bands are 3/4 (Non-Fail band) or 5 (Pass).

| Sub-dim (spec entry 4) | Score | Reason |
|---|---:|---|
| OE Authority | **5** | OEs remain subordinate to universe/tool catalog. No claim in the OE overrides `6_Server_Tools_Details.json`, live universe, or prompt. |
| OE Completeness | **4** | Affirmative critical path present; every OE names tool + params + observable expectation. **Downgrade to 4** because OE 29 carries a "Skip this OE only if the merged VFX genuinely does not touch either sibling's scope" conditional that leaves a coverage gap S3 must resolve, and OE 27's non-close of "Engineer to implement" needs a paired rubric to remain observable. |
| OE Accuracy | **4** | All tools/params/dates/counts verifiable against catalog and universe. **Downgrade to 4** because OE 24 hedges the ART tracking ticket ID ("id 'ART-768' (or the closest live-state ART Zombie Match 3D VFX tracking ticket ...)"), which weakens the anchor for OE 26 and downstream rubrics. Also flag `linear_get_issue`/`linear_create_comment` with `id/issueId = "ART-768"` (human identifier rather than internal UUID) — accepted in HG's Linear per catalog signature (`id: string`), but worth Council-A verification. |
| Negative Events | **5** | Pre-scan for *does not / must not / never / no / refrains from* returns 8 hits: OE 3 "zero submitted reviews" (lookup confirming factual state — valid), OE 4 "zero inline comments" (valid), OE 10 "no unresolved CHANGES_REQUESTED" (valid), OE 11 "email field empty" (valid), OE 20 "still incomplete" (factual state — valid), OE 22 "zero checklists (per the actual universe)" (lookup — valid), OE 27 "Do NOT close 'Engineer to implement'" (rides on OE 27's affirmative `trello_update_check_item` write, not a standalone non-action event), OE 29 conditional skip (has default affirmative write). All hits are affirmative discoveries or ride on affirmative actions. |

No propagated OE contradiction flag. No BLOCKing sub-dim.

---

## Section 2 — B2 Forward map (every prompt sentence → OE coverage)

Prompt sentences numbered S1..S23 (I collapsed intra-paragraph runs on the same predicate).

| Sentence (abridged) | OE steps that address it | Coverage |
|---|---|---|
| S1 "Leonard cornered me on my way out Friday evening" | — | context, no OE needed |
| S2 "Marcus told him the import PR ... is already covered ... treat that draft as parked" | OE 2 (PR #1 draft state), OE 5/6 (real merged VFX), OE 32 (reply) | ✓ |
| S3 "we shipped a build with two placeholder assets" | — | context |
| S4 "know what has actually merged ... what is still open, and who owns each piece" | OE 1, 5, 6, 7, 8, 9, 10, 11, 12, 13 | ✓ |
| S5 "Start on the Combo-Fighters repo" | OE 1 | ✓ |
| S6 "Walk PR history since December, both merged and unmerged" | OE 1, 2, 5, 6, 7, 10 | ✓ |
| S7 "the state of the code, not just the state of the PR title" | OE 2 (0 additions), OE 5/6/7 (additions + changed_files), OE 9 (inline comments) | ✓ |
| S8 "if a merged PR still has review pushback that never got resolved, that counts as still open" | OE 7, 8, 9 | ✓ |
| S9 "if a draft PR has no code in it at all, note that separately" | OE 2 | ✓ |
| S10 "cross-check that against the Zombie Match 3D roadmap board" | OE 16, 17, 18 | ✓ |
| S11 "cards ... for the VFX implementation work" | OE 18, 19, 22 | ✓ |
| S12 "Read the checklist items on those cards, not just the card names" | OE 20, 22 | ✓ |
| S13 "the real state, item by item" | OE 20, 21, 22 | ✓ |
| S14 "Get the owner attribution right" | OE 11, 12, 13 | ✓ |
| S15 "more than one person named Marcus ... GitHub author not always tied to a company email" | OE 11, 12, 13 | ✓ |
| S16 "be specific about which Marcus" | OE 11, 12, 13 (evidence for downstream rubric) | ✓ |
| S17 "reconciliation comment on the ART tracking ticket in Linear" | OE 23, 24, 26 | ✓ |
| S18 "update the affected roadmap card in Trello" | OE 27, 28 | ✓ (but see §8 Q4 — OE 29 is sibling-scope) |
| S19 "Leave a comment there on what still needs owner attention" | OE 28 | ✓ |
| S20 "close out any checklist items that the merged code actually finished" | OE 27 | ✓ |
| S21 "short status brief in a Drive doc ... send Leonard on Monday morning" | OE 25 (context read), OE 30 (write) | ✓ |
| S22 "vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet" | OE 15, 31 | ✓ |
| S23 "tell me in the reply whether ... supports Leonard's 'treat it as parked' read" | OE 32 | ✓ |

**No uncovered prompt sentence.** Coverage is complete.

---

## Section 3 — B2 Reverse map (every OE → prompt motivation)

| OE | Motivating sentence(s) | Scope-creep flag |
|---:|---|---|
| 1 | S5, S6 | — |
| 2 | S6, S7, S9 | — |
| 3 | S6 (real vs placeholder — no reviews = no engineering endorsement) | — |
| 4 | S6, S7 | — |
| 5 | S6, S7 | — |
| 6 | S6, S7 | — |
| 7 | S6, S8 | — |
| 8 | S8 | — |
| 9 | S7, S8 (inline pushback = the "state of the code") | — |
| 10 | S6, S8 (sweep for other unresolved CHANGES_REQUESTED) | — |
| 11 | S15 | — |
| 12 | S14, S15, S16 | — |
| 13 | S14, S15, S16 | — |
| **14** | **S22 (asserts Ozhan is "context for the vendor followups section")** | **MINOR — Ozhan is not named in prompt; prompt names Leapblock + Martin Walsh only. Persona-brief pull-through, not prompt-motivated.** |
| 15 | S22 | — |
| 16 | S10 | — |
| 17 | S10 | — |
| 18 | S10, S11 | — |
| 19 | S11, S12 | — |
| 20 | S12, S13 | — |
| 21 | S13 (drift/toggle-history) | — |
| 22 | S12 (sibling checklists) | — |
| 23 | S17 | — |
| 24 | S17 | — |
| 25 | S21 (scoping context for the Drive doc) | — |
| 26 | S17 | — |
| 27 | S20 | — |
| 28 | S18, S19 | — |
| **29** | **S18 ("the affected roadmap card" reads singular)** | **MODERATE — commenting on a *sibling* card is a scope expansion unless the merged VFX genuinely touches that sibling's scope. OE's skip clause hedges this but doesn't resolve it.** |
| 30 | S21 | — |
| 31 | S22 | — |
| 32 | S23 | — |

Two flags: OE 14 (Minor scope creep), OE 29 (Moderate scope creep).

---

## Section 4 — B3 Tool-call density projection

Conservative per-OE projection. `set_acting_user` excluded (environment config per instructions). Ranges reflect realistic loop expansions on OE 10 (10 PRs × 2 calls = 20 midpoint, 10 low to 30 high), OE 22 (2 sibling cards × 2 calls = 4 midpoint, 2 low to 6 high with checklist descent), OE 15 (2 explicit contact queries), OE 20 (2 calls per body text — `trello_get_checklists_on_board` + `trello_get_checklist`).

| OE | Low | Mid | High | Service |
|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | github |
| 2 | 1 | 1 | 1 | github |
| 3 | 1 | 1 | 1 | github |
| 4 | 1 | 1 | 1 | github |
| 5 | 1 | 1 | 1 | github |
| 6 | 1 | 1 | 1 | github |
| 7 | 1 | 1 | 1 | github |
| 8 | 1 | 1 | 1 | github |
| 9 | 1 | 1 | 1 | github |
| **10 (10 PRs × 2 calls)** | **10** | **20** | **30** | github |
| 11 | 1 | 1 | 1 | github |
| 12 | 1 | 1 | 1 | contacts |
| 13 | 1 | 1 | 1 | linear |
| 14 | 1 | 1 | 1 | contacts |
| 15 (2 queries) | 2 | 2 | 2 | contacts |
| 16 | 1 | 1 | 1 | trello |
| 17 | 1 | 1 | 1 | trello |
| 18 | 1 | 1 | 1 | trello |
| 19 | 1 | 1 | 1 | trello |
| 20 (2 calls) | 2 | 2 | 2 | trello |
| 21 | 1 | 1 | 1 | trello |
| **22 (2 siblings × 2 calls)** | **2** | **4** | **6** | trello |
| 23 | 1 | 1 | 1 | linear |
| 24 | 1 | 1 | 1 | linear |
| 25 | 1 | 1 | 1 | gdrive |
| 26 | 1 | 1 | 1 | linear (write) |
| 27 | 1 | 1 | 1 | trello (write) |
| 28 | 1 | 1 | 1 | trello (write) |
| 29 | 1 | 1 | 1 | trello (write) |
| 30 | 1 | 1 | 1 | gdocs (write) |
| 31 | 1 | 1 | 1 | gsheets (write) |
| 32 (reply) | 0 | 0 | 0 | — |

**Totals: `{low: 43, midpoint: 55, high: 67}`.**

**Distinct services (7):** github, contacts, linear, trello, gdrive, gdocs, gsheets — matches Hardness Plan's 7-service target exactly. Well above HG framework's 3+ services floor.

**Verdict: PASS.** Midpoint 55 ≥ 50 pipeline-convention target; also clears HG authoring 40+ target with 38% margin, prompt-eval hard-gate >15 with 3.7× margin, and QC trajectory floor 15 with 3.7× margin. Six of seven services carry ≥ ~4% share; no single-service deep trap (highest is github at 33 calls = 60% of midpoint, which is high but the multi-service breadth is preserved).

---

## Section 5 — B4 Lever preservation

| Lever | Anchor per Hardness Plan | OE step(s) exercising it | Status |
|---|---|---|---|
| **L1 Latching** | PR #1 draft (0 changes, "do not merge") vs merged PR #36 + PR #16 | OE 2 (PR #1 draft), OE 5 (PR #36), OE 6 (PR #16) | ✅ preserved |
| **L2 Structured-DB skip** | (a) `github.review_comments` on PR #37, (b) `trello.check_items` on ZM ROADMAP card | OE 9 (10 inline review_comments on PR #37 incl. enum pushback), OE 20 (both check_items on card `6851a9942b47001e59c8e777`), OE 21 (card actions timeline) | ✅ preserved, both variants |
| **L6 Marcus disambiguation** | 3-way triangulation via Contacts + Linear + GitHub | OE 11 (GitHub user has no linked email), OE 12 (3 Marcus contacts), OE 13 (3 Marcus in Linear) | ✅ preserved |
| **L9 Authority dismissal** | Prompt-anchored Leonard quote | Prompt paragraph 1; addressed by OE 32 (reply pushback) | ✅ preserved |
| **L10 Reversal / supersession** | PR #1 superseded by PR #36 + PR #16; stale Trello check_item | OE 2 + OE 5 + OE 6 (supersession pair); OE 20 (stale "Marcus to create VFX" incomplete); OE 21 (actions timeline confirming no re-toggle) | ✅ preserved |

**All 5 levers preserved. No lever lost its anchor.**

---

## Section 6 — B8 Write-action forward map

Six write-action OEs. Each needs an Outcome 1.1 rubric (write-action result) planned for S3.

| Write OE | Write action | Planned Outcome 1.1 rubric | Propagate to S3? |
|---:|---|---|---|
| **26** | `linear_create_comment` on ART tracking ticket | "Agent posts a Linear comment on the ART Zombie-Match-3D-VFX tracking ticket (`ART-768` or the Council-A-verified equivalent) covering PR #1 draft state + PR #36/PR #16 merged imports + PR #37 unresolved CHANGES_REQUESTED + four-Marcus attribution" | ⚠ **PROPAGATE TO S3**: OE 24's hedge on which ticket ID means S3 rubric must anchor on Council-A-verified ID, not on the hedged "ART-768 or ..." string. |
| **27** | `trello_update_check_item` closing "Marcus to create VFX" | "Agent updates Trello check_item `6855f20fb11687de8c0be3c8` on card `6851a9942b47001e59c8e777` to state `complete`" | ⚠ **PROPAGATE TO S3**: pair with a companion criterion that FAILS if the agent also closes `6855f2153528bf8d9fb8e116` ("Engineer to implement"). Otherwise the negative-constraint half of OE 27 is ungraded. |
| **28** | `trello_add_comment` on primary VFX card | "Agent posts a Trello comment on card `6851a9942b47001e59c8e777` naming that 'Engineer to implement' is still open, tied to PR #37's unresolved CHANGES_REQUESTED, with the two engineer owners (EMPLOYEE_0003_GITHUB_USERNAME and PERSON_5877_GITHUB_USERNAME) identified" | ✓ direct 1:1 |
| **29** | `trello_add_comment` on a sibling VFX card | "Agent posts a Trello comment on sibling card `6852f6014ef0266338b1728b` OR `6851aafe8c9e95ec0abbd262` describing merged PR #36 scope overlap" | ⚠⚠ **PROPAGATE TO S3 (Moderate)**: prompt says "the affected roadmap card" (singular). Either drop this write from the OE (revise) or S3 must bind the rubric to a Council-A-verified fact that PR #36 touches sibling scope, otherwise the rubric will grade a write the prompt didn't authorize. |
| **30** | `gdocs_create_document` status brief | "Agent creates a Google Doc titled 'Combo-Fighters art-import reconciliation 2026-02-28' (or equivalent date-stamped title) containing (a) PR #1 draft state, (b) PR #36 + PR #16 merged imports, (c) PR #37 open pushback, (d) four-Marcus breakdown, (e) Leapblock + Martin Walsh vendor followups, (f) pushback recommendation" — decompose per OE 30's (a)-(f) list into 6 Outcome 1.2 content-check criteria | ✓ decomposable |
| **31** | `gsheets_create_spreadsheet` vendor tracker | "Agent creates a Google Sheet titled 'Art vendor followups 2026-02-28' with initial sheet 'Followups' containing rows for Leapblock followup and Martin Walsh followup with owner + next action + tracking link" — decompose per OE body into Outcome 1.1 (create) + Outcome 1.2 (content rows) | ✓ decomposable |

**S3 propagation flags:**
1. Re-anchor OE 26 rubric on the Council-A-verified ART ticket (do not use the hedge string).
2. Add the negative-constraint companion for OE 27 (agent must NOT close "Engineer to implement").
3. Decide OE 29's scoring status — either drop from graded writes or bind to Council-A-verified sibling-scope overlap fact.
4. Decompose OE 30 into 6 content-check criteria matching (a)-(f).

---

## Section 7 — HG-specific hard checks

| Check | Result | Evidence |
|---|---|---|
| Any Slack read or write? (Victor ACL-blocked from all Slack) | ✅ **ZERO** | No `slack_*` tool call anywhere in the 32 OEs. |
| Any Gmail send/reply/compose/draft? (HG Gmail read-only) | ✅ **ZERO** | No `gmail_send`, `gmail_reply`, `gmail_compose`, `gmail_create_draft` (also, none exist in HG catalog). No gmail reads either. |
| Retired-server reference (Snowflake, Confluence, wiki, knowledge base, BigQuery, Firebase, analytics warehouse) | ✅ **ZERO** | grep-clean. No Airtable/QuickBooks/Stripe references either. |
| Bare `SCHEMA.TABLE` reference | ✅ **ZERO** | OE body uses tool names (`github_list_pull_requests`, `trello_get_checklists_on_board`), not SQL-shaped table refs. |
| Prohibition-only / no-op pseudo-OE ("The Agent does not X") | ✅ **ZERO** | OE 27's "Do NOT close 'Engineer to implement'" rides on OE 27's affirmative `trello_update_check_item` write. OE 29's "Skip only if..." is a conditional on an otherwise-affirmative write. No standalone prohibition-only OEs. |
| Persona-scoped reads plausibly persona-visible for Victor | ✅ | Only scoped-service read is OE 25 (`gdrive_list_recent_files` — Victor's own drive is always visible). All other reads are on unscoped services (github, trello, linear, contacts). |
| OE 27 `trello_update_check_item` uses `cardId + checkItemId + state` | ✅ | Verified against catalog: params `cardId` (required), `checkItemId` (required), `state` (optional). OE 27: `cardId "6851a9942b47001e59c8e777", checkItemId "6855f20fb11687de8c0be3c8", state "complete"` — exact match. |
| OE 30 `gdocs_create_document` uses `bodyText` (not `body`/`content`) | ✅ | Verified against catalog: params `title` (required), `bodyText` (optional). OE 30: "gdocs_create_document with title '...' and bodyText covering..." — exact match. |
| OE 28/29 `trello_add_comment` uses `text` (not `payload`/`body`/`message`) | ✅ | Verified against catalog: params `cardId` (required), `text` (required). Both OE 28 ("with cardId '...' and text that names...") and OE 29 ("using trello_add_comment. The text should note...") use `text` — exact match. |
| OE 26 `linear_create_comment` uses `issueId + body` | ✅ | Verified against catalog: params `issueId` (required), `body` (required). OE 26: "linear_create_comment with issueId 'ART-768' and body containing..." — exact match on shape. **Sub-concern**: `"ART-768"` is a human identifier, not a UUID. HG catalog signature is `issueId: string` and `linear_get_issue.id: string` also accepts human IDs per convention — should verify at S1.5 that the runtime accepts the human ID form. |

**All HG hard checks: PASS.** One sub-concern flagged on Linear human-ID acceptance (verifiable at S1.5).

---

## Section 8 — Adversarial questions

**Q1: What if the agent asks about a different Marcus?**
A: OE 12 + 13 return the three harmonygames.co Marcuses (Bennett `usr_c77c50cc15c5342d`, Lee `usr_b501f018a4c5319f`, `marcus@` `usr_d7ae9de750a5640a`), and OE 11 confirms the GitHub author has no linked company email. The four-way disambiguation is complete at the OE level; whether the agent's *reply* names the right Marcus per artifact is a rubric-side concern. **Not a defect at OE level.**

**Q2: What if PR #37 was actually resolved outside the CHANGES_REQUESTED review?**
A: OE 9 descends to inline `github_get_pull_request_comments` to confirm the three substantive pushbacks (enum `E` prefix, `ComboRarityDefinition` justification, `_specialPrefab` vs `_lockedPrefab`). If the pushbacks were resolved by follow-up commits or by a review-dismissal, that state would need to be verified via `github_get_pull_request_reviews` (OE 8) or by checking commits after the review date. **OE 8 catches formal review-dismissal state; a follow-up-commit resolution is a Council A ground-truth concern.** Defer to Council A.

**Q3: What if the ART tracking ticket is a different one?**
A: OE 24 hedges with "id 'ART-768' (or the closest live-state ART Zombie Match 3D VFX tracking ticket the ART team search returns)". **This is a genuine defect (Moderate).** OE 23 returns multiple candidates (ART-252, ART-102, ART-768, ART-790). Without a definitive OE anchor, the S3 rubric can't specify which ticket. **Fix: Council A verifies which ticket is actually "the" ART Zombie-Match-3D-VFX tracking ticket and OE 24 is revised to name it definitively; alternatively S3 rubric allows any Linear comment on any live ART team ZM VFX ticket, which weakens rubric precision.**

**Q4: Does anywhere in the OE prescribe a write the prompt forbids?**
A: The prompt authorizes: (1) Linear comment on ART tracking ticket, (2) update the affected roadmap card in Trello (comment + close finished checklist items), (3) Drive doc status brief, (4) Sheet vendor followups. OE 29 writes a comment on a *sibling* Trello card, which the prompt does not explicitly authorize — the prompt's "the affected roadmap card" reads singular. **This is a Moderate scope-creep flag.** OE 27's paired constraint ("Do NOT close 'Engineer to implement'") is *consistent* with the prompt's "close out any checklist items that the merged code actually finished" (Engineer to implement is not finished code). All other writes align with prompt authorization.

**Q5: Is any OE a prohibition-only no-op?**
A: **No.** OE 27 pairs an affirmative check_item close with an implicit "leave the other item alone" constraint — the affirmative write is the event. OE 29 has a conditional skip but a default affirmative write. No standalone "Agent does not X" OE.

**Q6: Does the OE conflict with the prompt's "push back or park" framing?**
A: OE 32 correctly nuances the reply — supports parking PR #1 (draft with no code, no reviews), pushes back on the broader "already covered" framing because PR #37 has unresolved CHANGES_REQUESTED and the ZM ROADMAP "Engineer to implement" check_item is genuinely still open. **Aligned with prompt.**

**Q7: What if OE 22's "sibling cards carry zero checklists" claim is wrong?**
A: OE 22's expectation is a ground-truth claim ("per the actual universe"). If a sibling card actually carries checklists, OE 29's comment becomes doubly speculative because the sibling then has line-item state the OE isn't reconciling. **Defer to Council A ground-truth verification.**

**Q8: What if OE 10's Marcus-authored merged PRs (3, 5, 6, 7, 11, 12, 13, 22, 27, 33) contain a hidden unresolved CHANGES_REQUESTED?**
A: OE 10 claims "each is state 'closed', merged true, ..., and the review sets contain no unresolved CHANGES_REQUESTED." This is a ground-truth claim — if any of the 10 PRs actually carries an unresolved CHANGES_REQUESTED, that PR would need to be reported as still open per S8's rule, and the reconciliation brief would be incomplete. **Defer to Council A.** Note the 20 tool calls this OE requires make this a high-density check that's earning its weight even if the ground truth turns out clean.

**Q9: Ozhan is named in OE 14 but not in the prompt.**
A: OE 14 pulls in `ozhan@harmonygames.co` as "context for the vendor followups section." The prompt names Leapblock and Martin Walsh only; Ozhan is a persona-brief context, not prompt-motivated. **Minor scope creep.** Fix: drop OE 14 or explicitly mark it as "supporting context — no rubric scoring."

**Q10: Does OE 25 `gdrive_list_recent_files` risk hitting a persona-ACL blocker?**
A: No. Victor's own Drive is always visible to Victor regardless of the persona-scoped read rule (own-mailbox / own-drive reads always ACL-visible). **Safe.**

---

## Section 9 — Final verdict

**Findings summary:**

| Sev | Finding | Fix instruction |
|---|---|---|
| **MODERATE** | OE 24 hedges the ART tracking ticket ID ("id 'ART-768' (or the closest live-state ART Zombie Match 3D VFX tracking ticket ...)"). Anchor for OE 26 write and downstream Outcome 1.1 rubric is not definitively pinned. | Council A verifies which ART team ZM-VFX tracking ticket is authoritative; S3 rubric anchors on the verified ID, not the hedge string. If Council A can't uniquely resolve, OE 24 must be REVISED to name the winning ticket. |
| **MODERATE** | OE 29 writes a comment on a sibling ZM ROADMAP VFX card, but the prompt's "the affected roadmap card in Trello" reads as singular scope. Risk: rubric will grade a write the prompt didn't authorize. | Either (a) DROP OE 29 (prompt doesn't require it), or (b) bind the S3 rubric to a Council-A-verified fact that PR #36 touches the sibling card's scope, so the "affected" plural reading is grounded in ground truth. |
| MINOR | OE 14 (Ozhan contact lookup) is persona-brief context, not prompt-motivated. | Drop OE 14 or explicitly mark as "supporting context — no rubric scoring at S3." |
| MINOR | OE 27's "Do NOT close 'Engineer to implement'" needs a paired Outcome rubric that FAILS if the agent closes both check_items. | S3 adds a companion criterion: `check_item "6855f2153528bf8d9fb8e116" remains state=incomplete after the trajectory`. |
| MINOR | OE 26 uses `issueId "ART-768"` (human identifier). Should verify at S1.5 that the runtime accepts the human ID form for `linear_create_comment`. | S1.5 check against a live Linear call in the harness. |

**No Major findings. Two Moderate findings, both S3-tractable (with Council A ground-truth input on the ART ticket and the sibling-scope check).**

**Density: 55 midpoint, 7 distinct services → PASS.** All 5 levers preserved. All HG hard checks pass.

---

**Council B verdict: GO** (with S3-propagation flags on OE 24 anchoring, OE 27 negative-constraint pairing, OE 29 scope-creep resolution, OE 30 (a)-(f) decomposition, and the S1.5 verification of Linear human-ID acceptance).
