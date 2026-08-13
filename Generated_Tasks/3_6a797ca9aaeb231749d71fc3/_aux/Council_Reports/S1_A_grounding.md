# Council A - Grounding and Convention (S1)

**Universe:** HarmonyGames (framework `hg`)
**Model under test:** Claude Opus 4.7 (universe-scoped exception)
**Today:** 2026-02-28 (Saturday, America/Chicago)
**Deliverable:** `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/5_Prompt.txt` (430 words, 11 lines)
**Reviewer perspectives applied:** A1, A2, A3, A4, A6, A7, A10, A11 (A13 = N/A at prompt phase; note for S3 below).

---

## Headline verdict

**GO.**

- Zero ungrounded concrete claims (A1)
- Zero convention drift (A2)
- Zero narrative-state contradictions (A3)
- Zero action-vs-prescription divergences and zero authority gaps (A4)
- Persona scope holds; Slack correctly absent from the prompt (A6)
- Zero MAJOR clarity gaps; two MINOR target-selection notes flagged for S3 awareness (A7)
- Business function match confirmed - Engineering scope holds (A10)
- Full dependency chain materialised in `_aux/Universe_Split/` (A11)

**One upstream cleanup flagged (not blocking this phase):** Hardness_Plan claims a `contacts.contacts Leapblock vendor row` (Lever 8 anchor). Verified as FALSE. Leapblock is groundable via other services, so this is a Hardness_Plan hygiene fix, not a prompt-phase defect. Detail in the A11 section.

---

## A1 - Grounding sweep

For each concrete claim, VALUE -> FILE:RECORD.

| # | Claim in prompt | Verified against | Result |
|---|---|---|---|
| 1 | "Leonard" (Leonard Hayes) | `contacts.contacts` `contact_id=63fffeb4fab5233ed5bb73bf` `email=leonard.hayes@harmonygames.co` `is_user=True`; `linear.users` `id=usr_63fffeb4fab5233e`; roster `persona_key=leonard_hayes` Co-founder & Creative Director | GROUNDED |
| 2 | "Marcus" - deliberately ambiguous | Four distinct identities: `contacts.contacts` (a) `marcus@harmonygames.co` `contact_id=48415476...` `is_user=False`, (b) `marcus.bennett@harmonygames.co` `contact_id=c77c50cc...` `is_user=True`, (c) `marcus.lee@harmonygames.co` `contact_id=c7b13b5c...` `is_user=False`; `linear.users` mirrors the three; `github.users` login `PERSON_0396_GITHUB_USERNAME` `name="Marcus"` `email=""` | GROUNDED (4 identities, ambiguity is real per L6) |
| 3 | "Combo-Fighters" repo | `github.repositories` `full_name=harmonygames-Games/Combo-Fighters` `default_branch=main` | GROUNDED |
| 4 | "the import PR on Combo-Fighters" | `github.pull_requests` `repo_id=harmonygames-Games/Combo-Fighters` #1 `state=open` `draft=True` `additions=0` `deletions=0` `changed_files=0` `labels=["do not merge"]` `head_ref="Marcus/ImportingArtAssets"` `author_login=PERSON_0396_GITHUB_USERNAME` `created_at=2025-12-02T17:29:27Z` `updated_at=2026-01-21T13:30:50Z` | GROUNDED (matches Hardness_Plan Lever 1 exactly) |
| 5 | "the merged VFX branch" | `github.pull_requests` #16 merged 2025-12-21 "Marcus/win screen coin vfx" + #36 merged 2026-02-11 "vfx updates" (22,309 additions / 2,568 changed_files) | GROUNDED |
| 6 | "over the last quarter" (from today 2026-02-28) | 32 merged PRs on Combo-Fighters between 2025-12-01 and 2026-02-28 | GROUNDED |
| 7 | "Zombie Match 3D roadmap board" | `trello.boards` `id=6851a6569f3bf818760632ab` `name="ZM ROADMAP"` `closed=False`; 79 cards on that board | GROUNDED |
| 8 | "cards on there for the VFX implementation work" | `trello.cards` `id=6851a9942b47001e59c8e777` `name="[Improvement] Equipped Card Item Infusion VFX implementation - [PERSON_NAME_0120]"` | GROUNDED |
| 9 | "the underlying checklist items sit open" | `trello.check_items` `id=6855f20fb11687de8c0be3c8` `state=incomplete` `name="Marcus to create VFX"` on checklist `6855f203cc9b82840c24e782` "Workflow" (with a sibling `Engineer to implement` also incomplete) | GROUNDED |
| 10 | "GitHub author on the recent art work is not always tied to a company email I recognize" | `github.users` login `PERSON_0396_GITHUB_USERNAME` name=`Marcus` `email=""` (no linked email) | GROUNDED |
| 11 | "the ART tracking ticket in Linear" | `linear.teams` `key=ART` `name=Art` `id=team_ART` with 597 issues; 170 issues match "VFX/import" title filter | GROUNDED (see A7 for MINOR clarity note on definite article "the") |
| 12 | "Leapblock" | Persona brief "Key relationships"; `slack.channels` `#leapblock` (private, 3 members - Victor NOT a member per ACL); `gdrive.drive_files` 27 hits; `trello.cards` 2 hits; `github.pull_requests` 7 hits on GameOfDominoes repo. NOT in `contacts.contacts` | GROUNDED via persona brief + Drive/Trello/GitHub (see A11 note below) |
| 13 | "Martin Walsh" | `contacts.contacts` `contact_id=51f5f16d46e8cf55f5ee337b` `email=martin.walsh@harmonygames.co` `is_user=True`; `linear.users` `id=usr_51f5f16d46e8cf55`; `slack.users` `display_name="Martin Walsh"`; roster `persona_key=martin_walsh` (role Game Designer, Design dept); persona brief lists him under Victor's "Key relationships (art)" | GROUNDED |
| 14 | "Friday evening" (implicit 2026-02-27) | Today 2026-02-28 is Saturday; Friday = 2026-02-27 | GROUNDED (consistent with Hardness Plan L9 time anchor, clear of weekend-comms rule) |
| 15 | "three other things landing Monday" | Narrative texture; not a universe-groundable atom, permitted under prompt-format persona-voice conventions | NARRATIVE (no grounding required) |
| 16 | "the last time I took someone else's word on an art-import status we shipped a build with two placeholder assets" | Narrative texture; prior-history framing device; not universe-groundable but a standard prompt-format persona convention | NARRATIVE (no grounding required) |

Note on the Fact_Ledger `personas_declared=17` vs `personas=41` split: per the HG-specific gap called out in the task briefing (HG populates `personas_declared` from the roster; the higher `personas` count includes NPCs and other email-carrying rows). Not flagged as ungrounded per the briefing instruction.

**A1 verdict: GO.** Every concrete claim is universe-backed. No NOT FOUND.

---

## A2 - Convention sweep

Compared against `Reference/Prompt_Format.md` + `QC_Passed/Task2_.../5_Prompt.txt` + `QC_Passed/Task3_.../5_Prompt.txt`.

| Rule | Result | Evidence |
|---|---|---|
| 500-word hard cap | PASS | 430 words |
| 400-word soft target | ACCEPTABLE (26 over) | 430 words - not blocking; comparable to Task2 register (7 lines, dense) |
| Em-dash `U+2014` | CLEAN | 0 hits |
| En-dash `U+2013` | CLEAN | 0 hits |
| Tool function names (`_send`, `_create_`, `save_issue`, `list_pull_requests`, ...) | CLEAN | 0 hits |
| MCP-server names ("Linear MCP", "the Trello MCP") | CLEAN | 0 hits |
| Service names ("Linear", "Trello", "Drive doc", "sheet") permitted | PASS | Prompt uses service nouns naturally, as permitted by format card ("Refer to systems naturally") |
| Internal IDs (PR#, ART-###, hex card ids, `usr_`, `PERSON_`) | CLEAN | 0 hits |
| Pre-solving (root cause / final number / named culprit) | CLEAN | Prompt hints Leonard *might* be wrong (the placeholder-build backstory) but does not state which PR is stale, which check_items are incomplete, or how many; agent still investigates |
| First-person, natural voice | PASS | "Leonard cornered me on my way out Friday evening" - clearly Victor speaking |
| One coherent situation | PASS | Everything anchored on "did the art import actually land or not" |
| Structure (Trigger / Context / Asks) | PASS | Trigger = Leonard's Friday dismissal; Context = prior placeholder incident + persona's Monday pressure; Asks = walk PR history, cross-check roadmap, disambiguate Marcus, write reconciliation |
| Bolt-on / sentence-removal test | PASS | Every sentence load-bearing. Line 3 sentence 1 ("Start on the Combo-Fighters repo. Walk the pull-request history since December, both merged and unmerged...") is not a bolt-on despite being an opener - it anchors the specific investigation window that Line 3 sentence 3 ("If a merged PR still has review pushback that never got resolved, that counts as still open for the brief") depends on |
| Name-swap test | PASS - load-bearing | Swapping Leonard / Marcus / Combo-Fighters / ZM ROADMAP / Leapblock / Martin Walsh preserves shape but breaks the specific tensions (PR #1 draft with 0 changes vs merged VFX PRs #16/#36, Marcus 4-way ambiguity via GitHub-with-no-email, stale ZM ROADMAP check_items) - the details are load-bearing on this universe |

**Register comparison:**
- Task2 (7 lines, ~350 words): terse, single-scenario, single write-target register.
- Task3 (1 line, ~50 words): extremely terse "handoff" register.
- This prompt (11 lines, 430 words): slightly longer than either sample but within cap; register is a fuller "before-Monday-reconciliation" voice that fits a mid-thought Friday-evening handoff. Consistent with the sample register spectrum.

**A2 verdict: GO.** Zero convention drift.

---

## A3 - Narrative State Consistency

For every state-implying verb, verify against universe lifecycle:

| # | State claim | Universe check | Consistent? |
|---|---|---|---|
| 1 | "the import PR on Combo-Fighters is already covered by the merged VFX branch" | Leonard's REPORTED claim (Victor is asked to verify, not asserting). Actual state: PR #1 is `draft=True`, `changed_files=0`, unchanged since 2026-01-21; merged VFX shipped in PRs #16 and #36 | CONSISTENT (framed as claim to verify, not fact) |
| 2 | "treat that draft as parked" | PR #1 IS `draft=True` | CONSISTENT |
| 3 | "what has actually merged on Combo-Fighters over the last quarter" | 32 merged PRs since 2025-12-01 | CONSISTENT |
| 4 | "what is still open" | 1 open PR on Combo-Fighters (PR #1) | CONSISTENT |
| 5 | "If a merged PR still has review pushback that never got resolved" | PR #37 has structural markers of unresolved pushback per Hardness_Plan L2a; framed conditionally in the prompt, so no factual assertion made | CONSISTENT (conditional framing) |
| 6 | "If a draft PR has no code in it at all" | PR #1: `additions=0` `deletions=0` `changed_files=0` - exact match | CONSISTENT |
| 7 | "There are cards on there for the VFX implementation work that should be done by now if Marcus's import actually landed" | Card `6851a9942b47001e59c8e777` "Equipped Card Item Infusion VFX implementation" exists, `closed=False`; check_item `Marcus to create VFX` `state=incomplete` | CONSISTENT |
| 8 | "We have been marking cards 'in progress' for months while the underlying checklist items sit open" | ZM ROADMAP card checklists confirmed incomplete; Hardness_Plan notes the toggle history dates from mid-2025, giving ~8 months of "in progress" latency | CONSISTENT ("months" is accurate) |
| 9 | "There is more than one person named Marcus in our systems" | 4 identities confirmed | CONSISTENT |
| 10 | "the GitHub author on the recent art work is not always tied to a company email I recognize" | `github.users` PERSON_0396_GITHUB_USERNAME name=`Marcus` `email=""` (empty) | CONSISTENT |
| 11 | "the vendor followups I still owe Leapblock and Martin Walsh" | Persona brief names both as active art-vendor scope | CONSISTENT |

**A3 verdict: GO.** Zero narrative-state contradictions.

---

## A4 - Action-vs-Universe-Prescription

For every action verb the prompt asks for:

| Action verb | Target | Prescription conflict? | Authority? | Result |
|---|---|---|---|---|
| "Start on the Combo-Fighters repo. Walk the pull-request history" | GitHub read | No prescription field on PRs; read-only | GitHub UNSCOPED for reads | OK |
| "cross-check that against the Zombie Match 3D roadmap board" | Trello read | No prescription conflict | Trello UNSCOPED | OK |
| "Read the checklist items on those cards" | Trello read | No conflict | Trello UNSCOPED | OK |
| "Get the owner attribution right" | Cross-service identity resolution | No conflict | Contacts + Linear + GitHub all UNSCOPED (Contacts/GitHub/Linear are in the 4-unscoped set) | OK |
| "put a reconciliation comment on the ART tracking ticket in Linear" | Linear write (comment) | ART tickets carry `state=None` (no `proposed_resolution`/`recommended_action`); no prescription conflict | Linear UNSCOPED; ACL does not govern writes (HG rule) | OK |
| "update the affected roadmap card in Trello" | Trello card update / comment | No prescription field on Trello cards | Trello UNSCOPED | OK |
| "close out any checklist items that the merged code actually finished" | Trello check_item state update | No prescription conflict | Trello UNSCOPED | OK |
| "write me a short status brief in a Drive doc" | GDocs create_document | New doc, no prior state to contradict | GDocs is a persona-scoped READ service; **writes are NOT ACL-governed** (HG rule); Victor can create | OK |
| "put the vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet" | GSheets create_spreadsheet | New sheet | GSheets same read-scoped/write-unscoped pattern | OK |
| "Tell me in the reply whether the reconciliation actually supports Leonard's 'treat it as parked' read, or whether I need to push back" | Final response text | Not a tool write | N/A | OK |

**A4 verdict: GO.** Zero silent action divergences. Zero authority/permission gaps.

---

## A6 - Persona Scope

Prompt uses possessive scope implicitly:
- "I need to know" / "before Monday" / "the vendor followups I still owe" - Victor's scope
- "who owns each piece" - organisational fact, not "my" scoped

**Victor's assignment set (from PersonaBrief):**
- character-ability VFX quality
- character-profile UI
- outsourced art-vendor management **Leapblock, Martin Walsh** (explicit)
- Quests art
- zombie animation roster (Ozhan)
- hero video / UA creative
- ART Linear tickets; #god-gameart / #god-vfx Slack threads (Slack ACL-blocked - Victor NOT in those channels)

**Prompt scope reconciliation:**
- Combo-Fighters codebase - Victor's role is Game Engineer / Engineering dept; brief clarifies he leads the art/animation team including VFX quality. VFX imports in Combo-Fighters IS his scope.
- ZM ROADMAP VFX cards - character-ability VFX quality, in-scope.
- ART Linear tickets - explicit in brief.
- Leapblock + Martin Walsh follow-ups - explicit in brief under "outsourced art-vendor management".
- Marcus disambiguation - Marcus Bennett is named in brief under "Key relationships (art)"; owner attribution is in-scope.

**Slack ACL:** Victor has zero channel membership per re-verification. Prompt correctly:
- Does NOT name any Slack channel
- Does NOT ask Victor to post to Slack
- Does NOT frame any read on Slack messages/files

**A6 verdict: GO.** Persona scope holds. Slack correctly absent.

---

## A7 - Clarity & Specificity holistic read

Re-reading with no prior context:

| Potential ambiguity | Reading A -> writes | Reading B -> writes | Severity |
|---|---|---|---|
| "the ART tracking ticket in Linear" (definite article "the") | Agent identifies the one ART issue that specifically tracks the Combo-Fighters VFX import reconciliation (e.g., an ART-team issue tied to VFX import) and comments there | Agent picks a slightly different ART issue with VFX in the title | MINOR - both readings produce the same write shape (one comment on one ART issue); the specific target differs but the reconciliation content is identical |
| "the affected roadmap card" | Agent updates card `6851a9942b47001e59c8e777` "Equipped Card Item Infusion VFX implementation" | Agent updates a sibling VFX card | MINOR - same write shape; picking the wrong specific card is a substantive-work error the rubric can score, not a prompt clarity problem |
| "close out any checklist items that the merged code actually finished" | Reasoning about which merged-PR changes obsolete which check_items IS the substantive work of the task | - | NOT a clarity gap; it is the discrimination the task tests |
| "vendor followups I still owe Leapblock and Martin Walsh" | Agent compiles followups from Victor's context (recent Drive/PR/Trello activity involving each vendor) | - | NOT a clarity gap; open-ended write ask that S3 must decompose into per-vendor rubrics |

**Persona intent recoverability:** Victor is under Monday pressure, was told by Leonard that Marcus's import is covered, has been burned before by unverified art-import claims, and wants a first-hand reconciliation. Intent is fully recoverable from the prompt alone.

**A7 verdict: GO.** Zero MAJOR clarity gaps. Two MINOR target-selection notes recorded above are within the design of the task (open-ended write asks) and belong to S3's decomposition work, not to a prompt-phase revise.

---

## A10 - Business Function Match

**Assigned:** Engineering (per `1_Business_Function.txt`, maps to HG's Engineering & Live-Ops 25% slice).

**Prompt's primary scenario:** VFX-import reconciliation across the Combo-Fighters codebase, the ZM ROADMAP Trello board, ART Linear tickets, and outsourced art-vendor coordination (Leapblock, Martin Walsh).

**Fit analysis:** The scenario sits inside code-repository walk + ticket-system reconciliation + art-vendor management, all owned by Engineering & Live-Ops per HG's function distribution. The persona brief confirms Victor is in the Engineering department with an art/animation lead scope. Vendor management for outsourced art is part of Engineering's remit here (contrast with Finance/Legal/HR/Ops which handles procurement paperwork).

**A10 verdict: GO.** `assigned=Engineering prompt_primary=Engineering match=true`.

---

## A11 - End-to-End Solvability

Walking Hardness_Plan.md dependency chain:

| Step | Required source | Materialised? |
|---|---|---|
| Contacts lookup for Leonard | `contacts.contacts` (174 rows), Leonard confirmed | YES |
| Contacts lookup for the 3 email-carrying Marcuses | Confirmed | YES |
| GitHub user resolution for the 4th Marcus | `github.users` PERSON_0396_GITHUB_USERNAME | YES |
| Combo-Fighters PR history | `github.pull_requests` (2,629 total; 37 on Combo-Fighters) | YES |
| PR #1 draft state / #16 + #36 merged status | Verified in split | YES |
| Review-comment descent on merged PRs | `github.review_comments` (1,614 rows) | YES |
| ZM ROADMAP board -> lists -> cards -> checklists -> check_items | `trello.boards` (5), `trello.lists` (48), `trello.cards` (803), `trello.checklists` (54), `trello.check_items` (161) | YES |
| `Marcus to create VFX` incomplete check_item on card `6851a9942b47001e59c8e777` | Confirmed | YES |
| ART Linear team + tickets | `linear.teams` (`team_ART` present), `linear.issues` (3,852 total; 597 ART) | YES |
| Owner triangulation across Contacts + Linear + GitHub | All 3 in split | YES |
| GDocs / GSheets / GDrive write feasibility | Tools exist in HG catalog; Victor can create own-owned artifacts | YES |
| Leapblock context reachable to Victor | NOT in `contacts.contacts`; discoverable via `gdrive.drive_files` (27 hits), `trello.cards` (2 hits), `github.pull_requests` (7 hits on GameOfDominoes repo); slack.channels has `#leapblock` but Victor is ACL-blocked so he cannot enter that channel | YES (via Drive/Trello/GitHub; Slack path unavailable) |
| Martin Walsh context reachable to Victor | Contacts + Linear users + roster + Slack users (visible via `slack_get_user_info` on unscoped identity lookup) | YES |

**Upstream cleanup (not blocking):** Hardness_Plan.md Lever 8 chain claims a "contacts.contacts Leapblock vendor row + Ozhan freelance row" - the Ozhan row exists but there is NO Leapblock row in contacts.contacts. Leapblock is groundable through Drive/Trello/GitHub instead. S2 should be aware when drafting the Leapblock-touching OE step: name Drive files / Trello cards / GitHub PRs as the discovery surface, not a contacts lookup for Leapblock. Flag this back to HARDNESS or handle at S2. Not a prompt-phase BLOCK because the prompt does not name a specific discovery method.

**A11 verdict: GO.** Full dependency chain materialised. Zero SOLVABILITY_BREAK.

---

## A13 - N/A at prompt phase; note for S3

S3 will need atomic Outcome rubrics for the open-ended write asks:
- "close out any checklist items that the merged code actually finished" - one atomic rubric per check_item that was made obsolete by the merged PRs (identifiable at S3 by walking merged PRs #16 and #36 changed_files against ZM ROADMAP check_items). No "at least N" allowed unless the prompt explicitly mandates a minimum (it does not).
- "the vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet" - one atomic rubric per vendor row (2 vendors named; ground truth is a 2-row set).
- The two MINOR target-selection ambiguities in A7 - S3 must bind the reconciliation comment / roadmap update rubrics to the specific artifact identified by content ("the ART-team issue whose title or body ties the VFX import work" / "the ZM ROADMAP card whose incomplete check_items were finished by merged PRs #16 and #36"), not to a hard-coded ID that the prompt does not name.

---

## Format-card specific checks (summary)

- **Word count:** 430 (hard cap 500, soft target 400 - 26 over soft, acceptable)
- **Char count:** 2,375
- **Em-dash `U+2014`:** 0 hits
- **En-dash `U+2013`:** 0 hits
- **Tool-function-name scan:** 0 hits (`_send`, `_create_`, `save_issue`, `list_pull_requests`, MCP-server names all absent)
- **Internal-ID leak scan:** 0 hits (no `#N`, no `ART-N`, no 24-hex, no `usr_`, no `PERSON_`, no `EMPLOYEE_`)
- **Pre-solving scan:** NO - prompt hints at Leonard *possibly* being wrong via the prior-placeholder-build backstory but does not disclose the answer
- **Bolt-on / sentence-removal test:** every sentence load-bearing
- **Name-swap test:** load-bearing (universe-specific details drive the discrimination)
- **Weekend rule:** PASS - Friday 2026-02-27 anchor is BEFORE weekend; no outgoing routine business communication dated on Saturday 2026-02-28; no Slack send; no email send (HG gmail read-only anyway)
- **Q1 incoherence:** PASS - prompt does not reference Q1 close / Q1 results
- **Persona ACL:** PASS - no Slack channel named; no Slack post asked; Victor's zero-channel membership respected
- **Persona email construction:** PASS - no `@harmonygames.co` addresses embedded, no email derivation

---

## Per-sub-dim gate readout (for downstream council-tally)

| Perspective | QC sub-dim mapping | Outcome |
|---|---|---|
| A1 | Prompt / Truthfulness; Universe / Data Exists | PASS |
| A2 | Prompt / Explicit Tool Mention; Prompt / Coherence (Bolt-on); Prompt / Contrived-Unnatural | PASS |
| A3 | Prompt / Alignment with Today's Date; Prompt / Truthfulness | PASS |
| A4 | Prompt / Feasibility with Tools; Prompt / Unique Ground Truth | PASS |
| A6 | Prompt / Persona; Prompt / Persona ACL (HG-specific) | PASS |
| A7 | Prompt / Clarity & Specificity | PASS (2 MINOR notes for S3 decomposition; no MAJOR) |
| A10 | Prompt / Business Function | PASS |
| A11 | Prompt / Feasibility with Tools; Prompt / Tool Use & Cross-service | PASS (7-service breadth per Hardness_Plan) |
| A13 | Rubric / Category Balance (S3 phase) | N/A |

---

## Final verdict

**GO.**

Proceed to Council B (Adversarial + Density + Hardness Preservation). Carry forward two S2/S3-facing notes:

1. **Upstream Hardness_Plan hygiene:** Lever 8 chain reference to "contacts.contacts Leapblock vendor row" is incorrect. Leapblock is groundable via Drive/Trello/GitHub only. Update the plan or handle in S2 OE authorship (do not encode a contacts lookup for Leapblock in an OE step).
2. **S3 atomicity reminders:** two open-ended write asks ("close out any checklist items" and "vendor followups for Leapblock and Martin Walsh") require per-item atomic Outcome rubrics; two definite-article target references ("the ART tracking ticket" / "the affected roadmap card") require content-bound rubric evidence, not ID-bound.
