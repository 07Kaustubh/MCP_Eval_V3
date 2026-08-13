# S1 Prompt Design Log - 3_6a797ca9aaeb231749d71fc3

**Universe:** HarmonyGames (framework `hg`).
**Model under test:** Claude Opus 4.7 (universe-scoped exception; NOT 4.8).
**Universe today:** 2026-02-28 (Saturday, America/Chicago).
**Persona:** Victor Barnes, Game Engineer (actual scope: art/animation lead), `victor.barnes@harmonygames.co`, Engineering department.
**Business function:** Engineering (HG Engineering & Live-Ops slice).
**Working directory:** `Generated_Tasks/` (HarmonyGames uses this, not `Tasks/`).

## Levers engineered into the prompt

| Lever | How the prompt surfaces it | Environment placement |
|---|---|---|
| L1 - Latching | "the import PR on Combo-Fighters" (Leonard's dismissal) + "figure out which ones are real VFX imports versus which are placeholder branches sitting around" + "if a draft PR has no code in it at all, note that separately" | github.pull_requests: PR #1 draft `changed_files=0` since 2025-12-02, label `["do not merge"]`, `head_ref="Marcus/ImportingArtAssets"`. Anchors the reporting frame; the merged VFX in PRs #16 and #36 is the real work. |
| L2a - Structured-DB skip (github.review_comments) | "If a merged PR still has review pushback that never got resolved, that counts as still open for the brief" | github.review_comments: PR #37 has 10 unresolved Oliver Brooks CHANGES_REQUESTED line comments hidden under CodeRabbit auto-summary in pull_request_comments. |
| L2b - Structured-DB skip (trello.check_items) | "Read the checklist items on those cards, not just the card names" + "we have been marking cards 'in progress' for months while the underlying checklist items sit open" | trello.check_items on ZM ROADMAP: `Marcus to create VFX` incomplete on card `6851a9942b47001e59c8e777` since 2025-06-20 last toggle. |
| L6 - Four-Marcus disambiguation | "There is more than one person named Marcus in our systems and the GitHub author on the recent art work is not always tied to a company email I recognize. If you list a Marcus as the owner of something, be specific about which Marcus." | contacts.contacts + linear.users + github.users (3-way triangulation post-ACL revision; Slack leg dropped). 4 Marcus identities: Marcus Bennett `usr_c77c50cc15c5342d`, Marcus Lee `usr_b501f018a4c5319f`, `marcus@harmonygames.co` `usr_d7ae9de750a5640a`, GitHub `PERSON_0396_GITHUB_USERNAME` with no linked email. |
| L9 - Authority dismissal (Leonard, Friday evening) | Opening sentence: "Leonard cornered me on my way out Friday evening. He said Marcus told him the import PR on Combo-Fighters is already covered by the merged VFX branch and that I should treat that draft as parked. I want to believe him because I have three other things landing Monday..." | Prompt sentence, soft-verb L24 convention ("said Marcus told him", not "is covered"). Time-anchored Friday 2026-02-27 evening, pre-weekend, clear of the today-Saturday weekend-comms rule. |
| L10 - Reversal / supersession | "what has actually merged on Combo-Fighters over the last quarter, what is still open" + "close out any checklist items that the merged code actually finished" | github.pull_requests: PR #1 draft (`changed_files=0`) has been de facto superseded by merged PRs #36 (2026-02-11 vfx updates, 2568 changed_files) and #16 (2025-12-21 win screen coin vfx). Trello check_items last toggled 2025-06-20 never re-toggled after merged VFX shipped. |

## Expected stump targets (carried from Hardness_Plan)

1. **[HIGH]** Agent reports draft PR #1 as active in-progress art-import work (L1 + L10; L13 first-framing anchor + L25 existing-artifact latching).
2. **[HIGH]** Agent misses substantive engineering pushback in PR #37 `review_comments` (L2a; Oliver Brooks CHANGES_REQUESTED never surfaced under CodeRabbit summary).
3. **[MED-HIGH]** Agent lists card names but never descends to checklist state (L2b; `Marcus to create VFX` incomplete on Equipped Card card).
4. **[MED]** Agent conflates the four Marcuses when attributing merged VFX ownership (L6; likely picks Marcus Bennett the Artist persona without 3-way triangulation).

## Framework hygiene at draft time

- **Slack fully excised** (post-ACL revision): Victor is member of zero channels of any kind. Prompt references no Slack channel and asks for no Slack post.
- **Gmail read-only respected**: no send / reply / compose / draft ask. HG gmail has no `create_draft` unlike StarPM.
- **Weekend rule cleared**: today is Saturday 2026-02-28; Friday evening dismissal + Monday-morning delivery frame. No routine Slack/Gmail comms dated on the weekend.
- **Q1 incoherence check cleared**: no "Q1 close" or "Q1 results are final" framing (Feb 28 is mid-Q1).
- **V5-retired services**: zero references to Snowflake / Confluence / Firebase / BigQuery / App Store Connect / Airtable / QuickBooks / Stripe. No verb-scoped stand-ins (wiki, knowledge base, analytics warehouse).
- **Persona-email fabrication**: prompt embeds no `@harmonygames.co` addresses. V5 regularised addresses to `firstname.lastname@` but two single-token personas break the rule (`douglas@`, `robert@`), so no email is constructed anywhere.
- **Density (HG triple threshold)**: authoring target 40+ AND 3+ services CLEARED at midpoint 52 (Council B) / 56 (Hardness_Plan) across 7 services (github, trello, linear, contacts, gdocs, gsheets, gdrive). Prompt-eval hard gate >15 necessary calls AND 2+ services CLEARED. Trajectory floor 15 average CLEARED by 3.5x. Pessimistic-cautious floor (AUDIT) ~37 calls / 6 services still clears trajectory floor by 2.5x.

## Council verdicts

- **Validator** (`validate.py --phase prompt`): PASS. 0 fails, 3 warns (word count 430>400 soft; two false-positive transitional-opener bolt-on flags), 4 notes.
- **Council A** (Grounding + Convention): GO. Zero ungrounded claims, zero convention drift, zero narrative-state contradictions, zero persona-scope drifts, zero solvability breaks. Two carry-forwards for S2/S3 (Leapblock groundable off-contacts; open-ended write ask atomicity for S3).
- **Council B** (Adversarial QC + Density + Hardness): GO. 15/15 applicable Prompt sub-dims at 5/5 with no NON-FAIL band invoked. Zero adversarial divergence. Density 52 midpoint / 7 services. All 5 levers preserved. Zero PROPAGATE. All 7 HG-specific hard gates cleared.
- **Similarity** (`calc_similarity.py`): max composite 23.3 vs 40 ceiling. Top match `QC_Non_Fails/Task1_6a71380e73befe867c047584_HG`. Well under 35 near-pivot threshold.
- **Sample-clone** (`check_sample_clone.py`): CLEAR. 0/7 mechanically confirmed clones across all HG vendored samples.
- **AUDIT (STRICT VETERAN)**: PASS (STRICT). Zero MAJOR / zero MODERATE at S1. Three findings all downstream handoffs (M1 -> S2 ART-ticket target binding; m1 -> S3 owner-attribution triangulation; m2 -> S2 investigation-load-bearing OE sequence).

## Handoff to S2 (must address at S2 draft time)

1. **[M1]** Bind the OE step for the ART Linear ticket target by content ("the ART issue whose body ties the Combo-Fighters VFX import vendor work"), not by ID. If S2 universe verification finds no singleton candidate, propagate back for scope-narrowing S1 edit.
2. **[m2]** Sequence the OE so the final-response "push back on Leonard?" answer is load-bearing on the investigation-derived writes (Linear comment + Trello updates + GDocs brief), not answerable as a shortcut opinion.
3. **[Hardness_Plan hygiene]** Do NOT encode a `contacts.contacts` lookup for Leapblock - Leapblock has 0 contacts rows in this universe. Leapblock is groundable via Drive (27 hits) + Trello cards + GitHub PRs. The prompt does not anchor Leapblock in contacts.
4. **[M1 verification]** Before writing S2 OEs, verify the exact target set for the ART Linear ticket and the affected roadmap card. Multiple candidates = accept-set the rubric OR narrow the prompt.

## Handoff to S3 (must address at S3 draft time)

1. **[m1]** Bind the owner-attribution rubric to the specific correct identity (GitHub `PERSON_0396_GITHUB_USERNAME`, unlinked email - NOT Marcus Bennett the Artist persona) via 3-way Contacts + Linear + GitHub resolution.
2. **[A13]** Two open-ended write asks in the prompt ("close out any checklist items that the merged code actually finished" and "vendor followups I owe Leapblock and Martin Walsh") need per-item atomic Outcome rubrics. Two definite-article targets ("the ART tracking ticket" / "the affected roadmap card") need content-bound rubric evidence, not ID-bound. Do NOT use "at least N" phrasing.

## Exit criteria satisfied

- [x] `5_Prompt.txt` exists, 430 words <= 500 cap, 0 em-dashes.
- [x] Validator PASS.
- [x] Council A GO with zero ungrounded claims.
- [x] Council B GO with every applicable QC sub-dim at 5/5.
- [x] Council B-B3 projected tool-call count 52 midpoint (Hardness_Plan projected 56); clears HG authoring target 40+ / 3+ services with margin.
- [x] Council B-B4 all Hardness levers from `_aux/Hardness_Plan.md` still triggered.
- [x] Similarity gate composite 23.3 < 40 ceiling.
- [x] Sample-clone gate CLEAR.
- [x] Strict veteran AUDIT PASS (STRICT).

## Next step

Operator: hand to platform linter for prompt clearance, or invoke `PIPELINE S2 - Generated_Tasks/3_6a797ca9aaeb231749d71fc3` in a fresh chat if the linter is bypassed. If linter flags similarity to `QC_Non_Fails/Task1_6a71380e73befe867c047584_HG` (composite 23.3 recommendation INVALIDATE), the Class B invalidation template should cite: (a) different persona (Victor Barnes engineer vs Task1's Leonard-family scope), (b) different core scenario (art-import reconciliation across code + roadmap vs Task1's shape), (c) different write set (Linear + Trello + GDocs + GSheets vs Task1's), (d) different lever mechanism (L1+L2+L6+L9+L10 vs Task1's set).
