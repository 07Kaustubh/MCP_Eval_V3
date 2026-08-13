# S2 Council B — Adversarial QC on `6_Oracle_Events.txt` (REVISE r2)

Task: `Generated_Tasks/3_6a797ca9aaeb231749d71fc3` · Universe: `harmonygames` (framework `hg`) · Model under test: **Claude Opus 4.7** (universe-scoped) · Today: **2026-02-28** (Saturday, America/Chicago) · Persona: Victor Barnes (`victor.barnes@harmonygames.co`, Engineering).

Round: **REVISE r2**. Round-1 verdict was GO with 2 Moderate + 3 Minor findings. This round re-scores the revised 30-OE file (was 32) adversarially. Every "5" requires zero Major AND zero Moderate. New concerns introduced by the revise are surfaced.

Mechanical pre-scan (bash inline, results captured in `_aux/Reasoning/S2_B_r2_prescan.txt`-equivalent output):

- OE headers 1..30 (30 total, was 32) ✓
- Tool prefixes: `github` 12, `trello` 9, `linear` 4, `contacts` 3, `gdrive` 1, `gdocs` 1, `gsheets` 1 → **7 distinct services**
- Slack tokens: **0** · Gmail tokens: **0** · Retired-server tokens (snowflake / confluence / firebase / bigquery / airtable / quickbooks / stripe / wiki / knowledge base / analytics warehouse): **0**
- Bare `SCHEMA.TABLE` refs: **0** · Em-dashes: **0** · En-dashes: **0**
- Write actions detected: `linear_create_comment` 1, `trello_update_check_item` 1, `trello_add_comment` 1, `gdocs_create_document` 1, `gsheets_create_spreadsheet` 1 → **5 writes**
- OE 14: Ozhan mentions **0**, Leapblock mentions **7**, Martin Walsh mentions **2**
- OE 24: `ART-768` mentions **0**, "or the closest" hedge tokens **0**
- OE 22: spot-check reads only (`trello_get_card` × 2); no sibling write remains
- Negative-events indicators inline: `does not` 2, `never` 4, `no` 13, `Do NOT` 3, `zero` 3, `empty` 2 — every hit adjudicated in §1.

---

## Section 1 — QC sub-dim scoring

Authority: `Docs_harmonygames/7_QC_Spec_Doc1.json` entry index 4 ("Oracle Event (OE)"). All OE sub-dims are non-fail-dimensioned; landing bands are 3/4 (Non-Fail) or 5 (Pass). Only 5/5 counts as clean.

| Sub-dim (QC spec entry 4) | Score | Reason |
|---|---:|---|
| **OE Authority** | **5** | OE remains subordinate to universe / tool catalog / prompt. No OE overrides `6_Server_Tools_Details.json`, live universe, or persona-brief scope. |
| **OE Completeness** | **5** | Every OE names tool + params + observable expectation. Round-1 downgrade drivers are both resolved: (a) OE 29 conditional-skip clause is **gone** (OE 29 dropped, list is 30), and (b) OE 26's negative constraint on "Engineer to implement" now embeds rationale directly inside an affirmative `trello_update_check_item` write. No coverage gap remains — critical path from PR audit through cross-service reconciliation through five writes to reply is unbroken. |
| **OE Accuracy** | **5** | Tools / params / dates / counts verifiable against catalog and universe. Round-1 downgrade driver is resolved: OE 24 **no longer names `ART-768`** and carries **zero** "or the closest" hedge tokens; the ticket is resolved by content match on ART-team issues whose title/body binds Zombie Match 3D vendor-art or VFX-import scope, with most-recent `updated_at` as the tiebreak. The identifier surfaces only as evidence for the OE 25 write. The remaining Linear human-ID vs UUID question (r1 Minor) is deferred to S1.5 harness verification, not an Accuracy defect at OE authoring. |
| **Negative Events** | **5** | Pre-scan adjudication (all indicators): `zero submitted reviews` (OE 3), `zero inline comments` (OE 4), `no unresolved CHANGES_REQUESTED` (OE 10 sweep result), `email field empty` (OE 11), `never re-toggled` (OE 20/21), `still incomplete` (OE 20), `no write is authorized` (OE 22 conclusion, prescriptive framing on an affirmative-read OE), `Do NOT close 'Engineer to implement'` (OE 26, rides on affirmative `trello_update_check_item` write; the constraint is a rationale clause on the SAME write, not a standalone prohibition-only OE), `empty result set` (OE 14 Leapblock contacts lookup, factual expectation on an affirmative read), `no linked company email` (OE 11 result), `no underlying line-item state` (OE 22 conclusion), `does not pin a specific ART number in prompt language` (OE 24 authoring guidance, not an OE-scored event). Every indicator is either an affirmative-discovery expectation or rides on an affirmative write in the same OE. Zero standalone `The Agent does not X` shape. Zero prohibition-only pseudo-OE. |
| **Cross-service Coherence** (Universe sub-dim, checked here for OE-level coherence) | **5** | Multi-service traversal preserved: GitHub → Contacts → Linear → Trello → GDrive → GDocs → GSheets. Reads on one surface feed downstream writes on another (OE 20 checklist state → OE 26 close; OE 8/9 review pushbacks → OE 25 Linear comment; OE 14 Drive artifact titles → OE 28 GDoc + OE 29 Sheet). No orphaned service. |

**No BLOCKing sub-dim. All four OE sub-dims 5/5.**

---

## Section 2 — Moderate #1 adjudication (OE 24 hedge → confirmed resolved)

R1 finding: OE 24 hedged the ART tracking ticket as `id 'ART-768' (or the closest live-state ART Zombie Match 3D VFX tracking ticket...)`, weakening the anchor for the OE 25 write and downstream Outcome 1.1 rubric.

Revised OE 24 (verbatim excerpt): *"Resolve the ART tracking ticket by content, not by identifier. From the OE 23 result set, select the ART-team issue whose title or body binds Zombie Match 3D vendor-art or VFX-import scope and whose updated_at is the most recent within that content match. Retrieve the resolved issue in detail using linear_get_issue with id set to the identifier of the winning row so the identifier, team_id, and title all bind together in evidence. The evidence identifier is used only for the downstream write; the OE does not pin a specific ART number in prompt language."*

Mechanical verification: `ART-768` mentions **0**, `or the closest` hedge tokens **0**.

**Verdict on Moderate #1: RESOLVED.** The AMBIGUOUS_TARGET flag is removed. Content-selection rule is deterministic (title/body binding on ZM3D VFX vendor-art scope + most-recent `updated_at` tiebreak), and the identifier is derived from OE 23's result set at read time, not asserted. Rubric anchor for OE 25 can now use the artifact-content shape ("Linear comment on the ART-team issue binding ZM3D VFX vendor-art scope"), which is the shape hard rule 17 (dependent binds to antecedent's artifact, not to a criterion number) requires. **No residual Moderate here.**

Minor residual: if OE 23's search returns two tickets that tie on both content-match and `updated_at`, OE 24's tiebreak is silent. Practically low risk (Linear timestamps are second-precision) but adjudicated in §9 Q4.

---

## Section 3 — Moderate #2 adjudication (OE 29 dropped → confirmed resolved)

R1 finding: r1's OE 29 wrote a Trello comment on a *sibling* ZM ROADMAP VFX card, expanding scope beyond the prompt's singular "the affected roadmap card in Trello".

Mechanical verification: r2 has 30 OEs (was 32); r2's OE 22 is now a **spot-check read only** (`trello_get_card` × 2 siblings) with an explicit conclusion *"no write is authorized against them because the prompt's 'the affected roadmap card' reads singular"*; and the five write actions are OE 25 (Linear comment on ART ticket), OE 26 (Trello check_item close on the PRIMARY card only), OE 27 (Trello comment on the PRIMARY card only), OE 28 (GDoc), OE 29 (GSheet). No `trello_add_comment` call remains on any sibling card.

**Verdict on Moderate #2: RESOLVED.** The scope-creep flag is removed. All Trello writes now target primary card `6851a9942b47001e59c8e777` exclusively, matching the prompt's singular reading. **No residual Moderate here.**

Bonus: OE 22 is now doing useful adversarial work — it establishes on-the-record that the siblings have zero attached checklists (post-filtering OE 19's board-level result), which pre-empts a future rubric argument that the siblings had reconcilable line-item state the OE ignored. Good defensive posture.

---

## Section 4 — Fresh scope-creep / orphan scan on the new OE 14

Round-1 Minor was Ozhan-only OE 14 (persona-brief pull-through, not prompt-motivated). R2's OE 14 is a complete rewrite: Leapblock + Martin Walsh coverage across three unscoped surfaces (contacts + Drive + GameOfDominoes repo).

Prompt sentence S22: *"put the vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet so I have one place to work from."* Prompt explicitly names both entities. OE 14 hits **both**: 7 Leapblock mentions, 2 Martin Walsh mentions, 0 Ozhan mentions.

Fresh scope-creep audit:

- **Contacts leg** (`contacts_search_contacts` × 2 for Leapblock and Martin Walsh): direct S22 support. ✓
- **Drive leg** (`gdrive_list_recent_files` for Leapblock artifact titles): supports OE 28 body clause (e) and OE 29 vendor-tracker row content. Bound to downstream rubric-scored writes. ✓
- **GameOfDominoes PR scan** (`github_list_pull_requests` + `github_get_pull_request` on any Leapblock-tied PR): this is the fresh concern to audit. GameOfDominoes is **not named in the prompt**. Prompt names only Combo-Fighters as the repo of interest.

Adversarial reading: is the GameOfDominoes scan a scope-creep flag? Ruling: **No, MINOR at worst.** The prompt sentence S9 ("put the vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet") requires the agent to populate row content beyond persona-brief-derived placeholders. If Leapblock work touches GameOfDominoes (a plausible reading given the vendor-art scope), the tracker row's `next action` field can only be substantive if the agent surfaces that scope. The OE's *"any PR whose title or body ties Leapblock"* is content-gated, not a blanket sweep. **This is prompt-motivated inference, not scope creep.**

Orphan check: OE 14's outputs feed OE 28 (GDoc body clause (e)) and OE 29 (GSheet row content). Not orphaned.

**No new scope-creep or orphan flag on OE 14.** Round-1 Minor is fully resolved. Fresh audit clean.

Residual very-minor: OE 14's Drive artifact result binds into OE 28's clause (e) with the phrase *"referencing the specific Drive artifact titles returned by OE 14, when present"* and into OE 29's rows with *"owner set from OE 14 Drive artifact context"*. The `when present` and `context` phrasing tolerates empty Drive results without failing the OE — this is defensive but pushes some rubric-side responsibility to S3 to write Outcome 1.2 criteria that grade **either** the Drive-artifact-populated shape **or** the fallback shape. Flagged for S3 (not a Council B defect).

---

## Section 5 — B3 density re-projection on the 30-OE list

R1 midpoint was **55** (32 OEs). Delta = drop old OE 14 (Ozhan lookup, 1 call) + drop old OE 29 (sibling comment write, 1 call) + expand new OE 14 (Leapblock 3-surface scan, ~6 calls). Net delta: +4. Also OE 22 in r2 uses post-filtering on OE 19's already-retrieved result set (2 calls) rather than r1's descent-per-sibling (4 calls); delta: −2. Net movement +2, but expressed against the 30-OE re-numbering below.

Per-OE projection (`set_acting_user` excluded per instructions):

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
| **14 (contacts×2 + gdrive×1 + github_list_pulls×1 + github_get_pr×1-3)** | **4** | **6** | **8** | contacts / gdrive / github |
| 15 | 1 | 1 | 1 | trello |
| 16 | 1 | 1 | 1 | trello |
| 17 | 1 | 1 | 1 | trello |
| 18 | 1 | 1 | 1 | trello |
| 19 | 1 | 1 | 1 | trello |
| 20 | 1 | 1 | 1 | trello |
| 21 | 1 | 1 | 1 | trello |
| **22 (2 sibling get_card, post-filter OE 19)** | **2** | **2** | **2** | trello |
| **23 (2 queries: Zombie Match + VFX follow-up)** | **1** | **2** | **2** | linear |
| 24 | 1 | 1 | 1 | linear |
| **25** (WRITE) | 1 | 1 | 1 | linear |
| **26** (WRITE) | 1 | 1 | 1 | trello |
| **27** (WRITE) | 1 | 1 | 1 | trello |
| **28** (WRITE) | 1 | 1 | 1 | gdocs |
| **29** (WRITE) | 1 | 1 | 1 | gsheets |
| 30 (reply) | 0 | 0 | 0 | — |

**Totals: `{low: 42, midpoint: 55, high: 71}`.**

**Distinct services: 7** (github, contacts, linear, trello, gdrive, gdocs, gsheets). Matches Hardness Plan's revised 7-service breadth exactly. Note: GameOfDominoes reads (OE 14) share the `github` service, so the service count is unchanged even though a second GitHub repo enters the mix.

**Gate verdicts:**

- Pipeline convention midpoint ≥ 50: **PASS** (55 = +10% margin).
- HG framework authoring target (40+ calls AND 3+ services, `Docs_harmonygames/1`): **PASS** (55/7 = +38% margin on calls, +133% on services).
- HG prompt-eval hard gate (>15 necessary calls AND 2+ services AND multiple meaningful writes AND information friction, `Docs_harmonygames/7`): **PASS** on all four sub-gates (5 writes ≥ multiple, information friction from L1+L2+L10 landmines).
- HG trajectory QC floor (>=15 average, `Docs_harmonygames/7`): **PASS** (3.7× margin).

**Verdict: 55 midpoint. Within the expected 55-60 band the revise brief cited. Passes.**

Small note against the r1 delta arithmetic: the +2 net (55 → 55) is honest because two offsetting movements (dropped OE 29 sibling write −1; OE 22 post-filter approach −2; new OE 14 expansion +6; dropped old OE 14 −1; net = +2) land at the same headline number after re-numbering.

---

## Section 6 — B4 lever preservation on the revised list

Hardness Plan selects L1, L2, L6, L9, L10 (post-ACL revision). Each lever must still be exercised by at least one OE step.

| Lever | Anchor per Hardness Plan | OE step(s) on the 30-OE r2 list | Status |
|---|---|---|---|
| **L1 Latching** | PR #1 draft (0 changes, "do not merge") vs merged PR #36 + PR #16 | OE 2 (PR #1 draft state), OE 5 (PR #36 merged), OE 6 (PR #16 merged) | ✅ preserved |
| **L2 Structured-DB skip** | (a) `github.review_comments` on PR #37; (b) `trello.check_items` on ZM ROADMAP primary card | OE 9 (10 inline review_comments on PR #37 incl. enum pushback), OE 20 (both check_items on card `6851a9942b47001e59c8e777`), OE 21 (card actions timeline showing no re-toggle) | ✅ preserved, both variants |
| **L6 Marcus disambiguation** | 3-way triangulation via Contacts + Linear + GitHub (post-ACL, Slack leg dropped) | OE 11 (GitHub author has empty email), OE 12 (3 Marcus contacts), OE 13 (3 Marcus Linear identities) | ✅ preserved |
| **L9 Authority dismissal** | Prompt-anchored Leonard quote ("Marcus told him... treat that draft as parked") | Prompt paragraph 1; addressed by OE 30 (reply pushback) | ✅ preserved |
| **L10 Reversal / supersession** | PR #1 superseded by PR #36 + PR #16; stale Trello check_item never re-toggled | OE 2 + OE 5 + OE 6 (supersession triangle); OE 20 (stale incomplete state); OE 21 (actions timeline confirming no re-toggle) | ✅ preserved |

**All 5 levers preserved. Zero lever lost anchor coverage.** No lever leaked into the prompt (L9 remains the only prompt-lever, which is by design).

---

## Section 7 — B8 write-action forward map (5 writes now)

Five write actions; each needs an Outcome 1.1 rubric planned for S3, plus content decomposition where the OE body enumerates content elements.

| Write OE | Write action | Planned Outcome 1.1 rubric | Propagate to S3? |
|---:|---|---|---|
| **25** | `linear_create_comment` on ART tracking ticket resolved in OE 24 | *"Agent posts a Linear comment on the ART-team issue whose title/body binds Zombie Match 3D vendor-art or VFX-import scope (identifier derived from OE 24 evidence) covering: PR #1 draft state + PR #36/PR #16 merged imports + PR #37 unresolved CHANGES_REQUESTED (enum-E, ComboRarityDefinition, prefab-naming) + four-Marcus attribution incl. GitHub `PERSON_0396_GITHUB_USERNAME` with no linked company email"* — decompose into one Outcome 1.1 (post exists on correct ticket) + Outcome 1.2 content-check criteria per named content element | ✓ decompose to 1.1 + 5-6 content-check 1.2 criteria (hard rule 14 mirroring — every content element the OE 25 body enumerates must round-trip to a 1.2 carrier, and the OE itself already carries the decompose directive) |
| **26** | `trello_update_check_item` closing "Marcus to create VFX" (checkItemId `6855f20fb11687de8c0be3c8`) on card `6851a9942b47001e59c8e777`, state `complete` | *"Agent updates Trello check_item `6855f20fb11687de8c0be3c8` on card `6851a9942b47001e59c8e777` to state `complete`"* + **companion negative**: *"check_item `6855f2153528bf8d9fb8e116` ('Engineer to implement') remains state `incomplete` after the trajectory"* | ⚠ **PROPAGATE TO S3**: OE 26 embeds the paired negative constraint cleanly in a single affirmative-write OE. S3 must materialize the companion criterion or the negative half is ungraded — Council B r1 flagged this as MINOR and it remains MINOR now (embedded correctly at OE level, deferred to S3 for rubric materialization). |
| **27** | `trello_add_comment` on primary card `6851a9942b47001e59c8e777` | *"Agent posts a Trello comment on card `6851a9942b47001e59c8e777` naming that 'Engineer to implement' is still open, tied to PR #37's unresolved CHANGES_REQUESTED, with the two engineer owners (EMPLOYEE_0003_GITHUB_USERNAME and PERSON_5877_GITHUB_USERNAME) identified"* + content-check 1.2 per named element | ✓ 1:1, decomposable |
| **28** | `gdocs_create_document` status brief | *"Agent creates a Google Doc titled 'Combo-Fighters art-import reconciliation 2026-02-28' (or equivalent date-stamped title) containing (a)–(f)"* — decompose OE 28's (a)–(f) body enumeration into 6 Outcome 1.2 content-check criteria (1 per lettered clause) | ✓ decompose to 1.1 + 6 content 1.2 criteria |
| **29** | `gsheets_create_spreadsheet` vendor tracker | *"Agent creates a Google Sheet titled 'Art vendor followups 2026-02-28' with initial sheet 'Followups' containing rows for Leapblock followup and Martin Walsh followup with owner + next action + tracking link"* — decompose per OE into 1.1 (create) + 1.2 (Leapblock row content) + 1.2 (Martin Walsh row content), plus a link-tracking-to-ART-ticket 1.2 | ✓ decompose to 1.1 + 3-4 content 1.2 criteria; the tracking-link should reference the ART ticket by artifact identity, not by pinned identifier (hard rule 17 shape) |

**All 5 write actions have a clean Outcome 1.1 anchor. S3 propagation notes:**

1. Decompose OE 25 into 1.1 + 5-6 content 1.2 criteria (per OE body's enumerated content elements — this is a directive OE 25 itself carries).
2. Materialize the OE 26 negative companion criterion (Engineer-to-implement remains incomplete).
3. Decompose OE 28 (a)–(f) into 6 content 1.2 criteria.
4. Decompose OE 29 into 1.1 + 3-4 content 1.2 criteria; bind the tracking-link criterion to the artifact from OE 24 by content (title/body binding), not by pinned identifier.

**No new S3 propagation flag from the revise.** The r1 flag for OE 24 anchor-rebinding is now naturally consumed by OE 24's content-anchor shape.

---

## Section 8 — HG-specific hard checks (fresh scan)

| Check | Result | Evidence |
|---|---|---|
| **Zero Slack anywhere** (Victor ACL-blocked from all channels) | ✅ **ZERO** | Bash pre-scan: no `slack_` token in file. |
| **Zero Gmail send/reply/compose/draft** (HG Gmail read-only, no send/draft tool exists) | ✅ **ZERO** | Bash pre-scan: no `gmail_` token in file. |
| **Zero retired-server refs** (snowflake, confluence, wiki, knowledge base, BigQuery, Firebase, analytics warehouse, Airtable, QuickBooks, Stripe) | ✅ **ZERO** | Bash pre-scan clean on all 10 patterns (hard rule per V5 A1, `Validators/check_retired_servers.py`). |
| **Zero bare `SCHEMA.TABLE` refs** | ✅ **ZERO** | Bash pre-scan: no `[A-Z_]{2,}\.[A-Z_]{2,}` matches. OE bodies use tool names (`github_list_pull_requests`, `trello_get_checklists_on_board`), never SQL-shape table refs. |
| **Zero prohibition-only pseudo-OEs** | ✅ **ZERO** | OE 26's "Do NOT close 'Engineer to implement'" is embedded rationale on an affirmative `trello_update_check_item` write (the write CLOSES `6855f20fb11687de8c0be3c8`; the "do NOT" is a scoping clause on the same OE). OE 22's "no write is authorized" is a prose conclusion on an affirmative-read OE. No standalone "The Agent does not X" event. |
| **Zero em-dashes anywhere** | ✅ **ZERO** | Bash count: 0 em-dashes, 0 en-dashes. |
| **Persona-scoped reads plausibly persona-visible for Victor** | ✅ | Only scoped-service read is OE 14's `gdrive_list_recent_files` (Victor's own Drive is always visible to Victor regardless of persona-scoped read rules). All other reads on unscoped services (github, trello, linear, contacts). Persona ACL matrix per `Evals_harmonygames/1_Prompt_Eval.md` Access matrix (parsed at read time by `check_persona_acl.py`). |
| **Tool parameter shape** — `trello_update_check_item(cardId, checkItemId, state)` | ✅ | OE 26 uses exact param names. |
| **Tool parameter shape** — `gdocs_create_document(title, bodyText)` | ✅ | OE 28 uses `bodyText` (not `body`/`content`), matching V5 HG catalog and hard rule per HarmonyGames universe constants. |
| **Tool parameter shape** — `trello_add_comment(cardId, text)` | ✅ | OE 27 uses `text`, matching catalog. |
| **Tool parameter shape** — `linear_create_comment(issueId, body)` | ✅ | OE 25 uses `issueId + body`. Sub-concern: `issueId` value derives from OE 24's content-match evidence, which may be a human ID (`ART-XXX`) or UUID depending on Linear runtime. **Deferred to S1.5 harness verification** (per user brief), not a Council B defect. |
| **Tool parameter shape** — `linear_get_issue(id)` (OE 24) | ✅ | Uses `id` param. Same human-ID vs UUID sub-concern as OE 25; same S1.5 deferral. |
| **Weekend-comms rule (today = 2026-02-28 Sat)** | ✅ | Zero email/Slack communications any day. GDoc + GSheet + Trello comment + Linear comment + check_item close are all non-comms writes; weekend rule does not fire. |
| **Density service-breadth** | ✅ | 7 services, all ≥ ~1 call each; multi-service, not single-service deep trap. |

**All HG hard checks: PASS.** One S1.5-deferred sub-concern (Linear ID form), no Council-B defect.

---

## Section 9 — Fresh adversarial questions (10 asked, 6+ required)

**Q1: Can I break the ART-by-content anchor if OE 23's `linear_list_issues` returns two ART-team tickets that tie on both content-match and `updated_at`?**
A: OE 24's tiebreak rule is silent on this. Practically, Linear `updated_at` is second-precision, so a true tie is extremely unlikely. But if it happens: OE 24 does not deterministically pick one. **MINOR sub-concern**, adjudicated as a Council-A ground-truth issue (does the ART team in fact have two content-matched tickets tied to the second?) rather than a Council-B OE defect. S3 can materialize the rubric to accept *any* ART-team ticket that binds ZM3D VFX vendor-art scope, which fully defuses the tie case. **Not a blocking Moderate.**

**Q2: Can I break the ART-by-content anchor by pointing at a title-match that isn't actually the "right" ticket per business intent?**
A: If ART-102, ART-252, ART-768, and ART-790 all title-bind Zombie Match 3D VFX-import scope (Council A r1 said "multiple candidates" existed), the content-match rule alone is under-specified — which of them is the *authoritative* tracking ticket for THIS piece of work? OE 24's "most-recent `updated_at`" tiebreak resolves it deterministically. **This is defensible** because the prompt itself asks the agent to "put a reconciliation comment on the ART tracking ticket in Linear so the next person who picks this up sees the state" — the next-person-consuming reading favours the freshest ticket. **Not a defect.**

**Q3: Can I break the Leapblock-artifact binding if OE 14's Drive lookup returns zero Leapblock-titled artifacts?**
A: OE 28 clause (e) uses `referencing the specific Drive artifact titles returned by OE 14, when present`. The `when present` guard tolerates empty Drive. OE 29's rows use `owner set from OE 14 Drive artifact context` and `next action tied to the specific Leapblock artifact title returned` — if the Drive returns nothing, OE 29 falls back to Contacts-derived owner (martin.walsh@harmonygames.co) and the OE 14 Contacts leg still populates `next action`. **Falls back cleanly.** MINOR: S3 must materialize the OE 29 rubric to accept the fallback shape. Not a blocking Moderate.

**Q4: Can I break the "no sibling write" boundary by having the agent read OE 22's spot-check result and infer a comment is needed?**
A: OE 22 explicitly concludes *"no write is authorized against them because the prompt's 'the affected roadmap card' reads singular"*. This is an OE-level scoping instruction. If the agent independently writes a sibling comment despite this, that's a rubric-fail via S3's Outcome 1.1 scoping ("comment on card `6851a9942b47001e59c8e777` only"), not an OE defect. **Boundary is clean at OE level.** No leak.

**Q5: Can the agent misread OE 26 and close BOTH check_items?**
A: Yes, this is exactly the L2-adjacent risk. OE 26 explicitly names the affirmative close (checkItemId `6855f20fb11687de8c0be3c8`) AND the negative constraint (checkItemId `6855f2153528bf8d9fb8e116` — Do NOT close). S3 must materialize a companion Outcome 1.1 criterion "Engineer-to-implement check_item remains `incomplete`". Council B r1 already flagged this MINOR; it remains MINOR here (embedded well in the OE; propagation is an S3 responsibility).

**Q6: Can I break the OE 25 write anchor if OE 24 fails to return a valid ticket (e.g. content-match yields zero hits)?**
A: Yes, this would be a hard failure of the whole reconciliation chain. But OE 23 is defensively scoped: query "Zombie Match" then fallback query "VFX", limit 25 each. If both return zero content-matches on the ART team, the underlying universe has no ZM3D VFX ART tracking ticket — which contradicts the Hardness Plan's L2 anchor and would need Council A ground-truth intervention. **This is a Council A concern, not a Council B OE defect.** Deferred.

**Q7: Does the GameOfDominoes PR read leg in OE 14 create a rabbit-hole?**
A: OE 14's third clause is content-gated (`github_get_pull_request on any PR whose title or body ties Leapblock`). If GameOfDominoes has 100+ PRs, `github_list_pull_requests` returns them but `get_pull_request` fires only on Leapblock-tied hits. Realistic hit count: 0-3. Density projection (§5) accounts for this range (4-8 total OE 14 calls). **Not a rabbit-hole; bounded by content-gate.**

**Q8: Can I break the OE 26 close by having the agent close the wrong check_item ID?**
A: OE 26 hard-codes `checkItemId "6855f20fb11687de8c0be3c8"` as the affirmative target. This is a landmine per Council B r1 §7 (verified against catalog). If the underlying universe has a different check_item ID for "Marcus to create VFX" than the OE claims, that's a Council A ground-truth defect — deferred. Assuming the universe check_item ID matches, the OE is deterministic.

**Q9: Is the OE 10 loop (10 Marcus-authored merged PRs × 2 calls = 20 midpoint) fair, or does it inflate density?**
A: OE 10 is defensible on two grounds: (a) the prompt sentence S8 ("if a merged PR still has review pushback that never got resolved, that counts as still open") requires the agent to verify no OTHER merged PR carries unresolved CHANGES_REQUESTED — this is the sweep. (b) L2 lever anchor lives on `github.review_comments`; the sweep exercises L2 across the peer set, not just PR #37. **Fair. Not density inflation.**

**Q10: Does OE 14's `martin.walsh@harmonygames.co present, the internal owner of the Leapblock thread` claim risk being wrong if Martin Walsh actually isn't the Leapblock internal owner in the universe?**
A: This is a Council A ground-truth claim (per Hardness Plan L8 chain: Leapblock vendor row with Martin Walsh's email as primary contact). If the universe disagrees, that's Council A territory. **Deferred to Council A, not a Council B defect.**

---

## Section 10 — Final verdict

**Findings summary vs r1 baseline:**

| r1 Finding | r2 Status | Note |
|---|---|---|
| MODERATE — OE 24 hedge weakens ART ticket anchor | ✅ **RESOLVED** | OE 24 now content-anchored; `ART-768` mentions **0**, hedge tokens **0**. |
| MODERATE — OE 29 sibling-card write scope creep | ✅ **RESOLVED** | OE 29 dropped; no sibling write in the 30-OE list. |
| MINOR — OE 14 Ozhan orphan (not prompt-motivated) | ✅ **RESOLVED** | OE 14 rewritten to Leapblock + Martin Walsh, both prompt-named. Ozhan mentions **0**. |
| MINOR — OE 26 needs paired negative-constraint rubric | ⚠ **UNCHANGED** (embedded cleanly at OE level; propagation to S3) | OE 26 embeds the "Do NOT close Engineer-to-implement" rationale on the same affirmative write. S3 materializes the companion criterion. |
| MINOR — OE 25 uses human ID (`ART-XXX`) for Linear | ⚠ **DEFERRED** to S1.5 per user brief | Same shape now applies to OE 24's `linear_get_issue(id=...)` call. S1.5 harness verifies acceptance. |

**Fresh r2 findings:**

| Sev | Finding | Fix instruction |
|---|---|---|
| MINOR | OE 24 tiebreak on `updated_at` is silent if two content-matched ART tickets tie to the second (Q1). Extremely low practical probability. | S3 rubric materialization accepts ANY content-matched ART-team ZM3D VFX ticket by artifact binding, defusing the tie. Not a blocking Moderate. |
| MINOR | OE 14 Drive-empty fallback (Q3): OE 28 (e) tolerates via `when present`; OE 29 needs S3 rubric to accept the Contacts-only fallback shape. | S3 materializes Outcome 1.2 for OE 29 to grade either Drive-populated or Contacts-only shape. |
| MINOR | OE 14 GameOfDominoes read leg is not prompt-named. Adjudicated as prompt-motivated inference (needed to populate OE 29 substantively), not scope creep. | No fix required; noted for the S3 write-content rubric. |

**Net severity ledger: 0 Major · 0 Moderate · 3 Minor (all with clear fix instructions, none blocking).**

Overall QC sub-dim scoring: **all four OE sub-dims 5/5** (Authority, Completeness, Accuracy, Negative Events). Cross-service coherence bonus check: **5/5**.

Density: **55 midpoint**, 42-71 range, 7 distinct services, all HG gates cleared with margin.

Lever preservation: **all 5 preserved** (L1, L2, L6, L9, L10).

HG hard checks: **all clean** (zero Slack, zero Gmail, zero retired-server, zero SCHEMA.TABLE, zero em-dashes, zero prohibition-only pseudo-OEs).

Write-action forward map: **5 writes, all with Outcome 1.1 anchors** planned; 4 with content-decomposition directives for S3.

---

**Council B verdict: GO** (clean pass; the two r1 Moderates are demonstrably resolved by mechanical inspection; three residual Minors are all S3-tractable and do not block).

**S3 propagation flags carried forward:**
1. Materialize the OE 26 companion negative criterion (Engineer-to-implement check_item remains `incomplete`).
2. Decompose OE 25 into Outcome 1.1 + 5-6 content 1.2 criteria matching the OE 25 body's enumerated content elements.
3. Decompose OE 28 (a)–(f) into 6 content 1.2 criteria (1 per lettered clause).
4. Decompose OE 29 into Outcome 1.1 + 3-4 content 1.2 criteria; bind tracking-link criterion to the ART artifact by content, not by pinned identifier.
5. Rubric anchor for OE 25 uses artifact-content shape ("Linear comment on the ART-team issue binding ZM3D VFX vendor-art scope"), not identifier pin.
6. Rubric materialization tolerates OE 14's Drive-empty fallback (grade either Drive-populated or Contacts-only shape for OE 29 rows).

**S1.5 verification still owed:** Linear runtime accepts human-ID form (`ART-XXX`) for both `linear_get_issue.id` and `linear_create_comment.issueId`.
