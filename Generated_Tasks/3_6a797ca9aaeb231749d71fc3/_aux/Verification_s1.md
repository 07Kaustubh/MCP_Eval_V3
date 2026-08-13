# Verification - S1 phase (v16 cross-source verification)

## Verdict

**PASS (STRICT).** S1 prompt drafted, validated, cleared by Council A (GO), Council B (GO), similarity gate (max composite 23.3 vs 40 ceiling), sample-clone gate (CLEAR 0/7 mechanically confirmed), and strict veteran AUDIT (PASS (STRICT), zero MAJOR / zero MODERATE at S1). Three findings are downstream handoffs (M1 -> S2 for ART-ticket target binding, m1 -> S3 for owner-attribution triangulation, m2 -> S2 for investigation-load-bearing OE sequence), not S1 REVISE. Prompt is 430 words / 0 em-dashes / 0 en-dashes / 0 tool-function-name tokens / 0 internal IDs / 0 pre-solving cues. Five Hardness levers all unambiguously surfaced. Density projected 52-56 midpoint across 7 services (github, trello, linear, contacts, gdocs, gsheets, gdrive), pessimistic floor ~37 calls / 6 services. Ready for platform linter or direct S2.

## Sources consulted

- **Per-task data** :: `_aux/Universe_Split/` (39 service files) grounded every named entity via A1: Combo-Fighters repo `harmonygames-Games/Combo-Fighters`, Zombie Match 3D ZM ROADMAP board `6851a6569f3bf818760632ab`, ART Linear team (597 tickets in scope), Leonard Hayes contacts + linear.users + roster (Co-founder & Creative Director), Marcus 4-way ambiguity (Marcus Bennett `usr_c77c50cc15c5342d`, Marcus Lee `usr_b501f018a4c5319f`, `marcus@harmonygames.co` `usr_d7ae9de750a5640a`, GitHub `PERSON_0396_GITHUB_USERNAME` no linked email), Martin Walsh in contacts + roster + slack.users, Leapblock groundable via drive/trello/github/slack surfaces (contacts.contacts has no `Leapblock` row - not encoded in the prompt as a contacts anchor). `_aux/Universe_Index/today_horizon.json` confirmed 2026-02-28 Saturday America/Chicago. `_aux/Fact_Ledger.json` (47 emails, 41 amounts, 1078 dates, 174 contacts) consulted for atom surface. `_aux/Hardness_Plan.md` all 5 levers preserved in prompt framing.
- **Eval spec** :: `Evals_harmonygames/1_Prompt_Eval.md` for the density hard-gate arithmetic (>15 necessary calls AND 2+ services AND multiple meaningful writes AND information friction), the persona-ACL derive-live rule at :14/:42/:99/:432, and the Prompt sub-dim scoring bands.
- **QC spec** :: `Docs_harmonygames/7_QC_Spec_Doc1.json` (Trajectory Tool Call Count floor 15 avg, Universe Feasibility + Cross-service Coherence binary, Rubric Category Balance 40% Process cap binary with zero Process valid) + `Docs_harmonygames/8_QC_Spec_Doc2.md` (severity taxonomy pre-swap: Overly Broad = Moderate, Overly Specific = Minor here - REVERSED from StarPM).

## Eval spec sub-dims (Evals_harmonygames/1_Prompt_Eval.md) verified

- 1.1 Unique Ground Truth :: **5/5 (binary)** — HG middle band removed; single canonical read forced by "what has ACTUALLY merged", "state of the code not just PR title", "last time I took someone else's word", closing "push back on it Monday morning?" question.
- 1.2 Feasibility :: **5/5** — all named surfaces reachable via unscoped services (GitHub, Trello, Linear, Contacts) + Victor-owned Drive assets; zero Slack ACL exposure.
- 1.3 Explicit Tool Mention :: **5/5 (binary)** — no tool-function names, no MCP-server names, no forbidden phrasings.
- 1.4 Prompt Clarity and Specificity :: **5/5** — no material second-reading that flips writes (tested by both Council B and AUDIT).
- 1.5 Contrived / Unnatural Prompts :: **5/5** — mid-thought entry, real persona register, no artificial precision, no spec-sheet language.
- 1.6 Truthfulness :: **5/5** — every factual claim grounded in `_aux/Universe_Split/`; PR #1 draft state, merged VFX PRs, incomplete check_items, four Marcuses all verified.
- 1.7 Tool use and Cross-service requirement :: **5/5 (binary)** — 7 services in projected trajectory, well above HG 3+ requirement.
- 1.8 Investigation :: **5/5 (binary)** — investigation is the load-bearing work (agent must derive whether Leonard's dismissal is correct against PR + Trello + attribution evidence).
- 1.9 Coherence :: **5/5 (binary)** — every sentence supports the same "before Monday status brief" outcome; validator bolt-on flags are false-positive transitional-openers with verifiable back-references (Council A + AUDIT both cleared).
- 1.10 Persona :: **5/5** — Victor Barnes's voice (engineer with vendor-management scope) consistent; no register creep.
- 1.11 Business Function :: **5/5** — Engineering (matches HG Engineering & Live-Ops 25% slice; art-lead scope is within Engineering per PersonaBrief).
- 1.12 Alignment with Today's Date :: **5/5** — Friday 2026-02-27 dismissal is pre-weekend; "Monday morning" is future; no Q1-close or Q1-completed framing.

## QC spec sub-dims (Docs_harmonygames/7_QC_Spec_Doc1.json - Prompt dimension) verified

All 12 Prompt sub-dims scored 5/5 per the scoring scheme table in Reference/Council_Protocol.md and Docs_harmonygames/7_QC_Spec_Doc1.json. HG-specific bands: 10 binary sub-dims across the spec (including Alignment with Today's Date which HG spec did NOT remove from the binary set per AGENTS.md HG-U rules); 4 authored 1/3/5 with NON-FAIL middle band. Council B + AUDIT both scored every applicable dim at 5 with no NON-FAIL invocation.

## Reference docs consulted

- `Reference/Prompt_Format.md` :: voice / structure / hard rules / HG deltas re-checked at draft time and at AUDIT.
- `Reference/Sessions/S1.md` :: runbook followed end-to-end (steps 0-9, Track F v21 AUDIT auto-fire condition (b) applied).
- `Reference/Council_Protocol.md` :: Council A + Council B templates followed; 5-role-lens overlay applied by both.
- `Reference/Hardness_Playbook.md` :: 5 levers preserved from HARDNESS phase; framework-scoped density scheme applied (HG 40+/3+ not V3-family 50/40).

## Verification statements

- [x] Validator (validate.py --phase prompt) exit 0. 0 fails / 3 warns (all non-blocking; 1 soft word-count preference, 2 known false-positive transitional-opener bolt-on flags cleared by Council A + AUDIT).
- [x] Council A grounding + convention clean (GO): zero ungrounded claims across every atom + zero convention drift + zero narrative-state contradictions + zero action-vs-universe-prescription divergences + zero persona-scope drifts + zero MAJOR clarity gaps + business function matches + zero solvability breaks.
- [x] Council B QC scoring shows every applicable sub-dim = 5/5 (or binary PASS): 15/15 at 5 with no NON-FAIL band invoked; zero adversarial divergence; density projection 52 midpoint across 7 services; all 5 Hardness levers still triggered; zero PROPAGATE TO HARDNESS flags; 7/7 HG-specific hard gates cleared.
- [x] Similarity gate (calc_similarity.py) composite 23.3 < 40 ceiling. Top match `QC_Non_Fails/Task1_6a71380e73befe867c047584_HG` at 23.3 composite. Recorded to `_aux/Similarity_Report.json`.
- [x] Sample-clone gate (check_sample_clone.py) verdict = CLEAR across all 7 vendored HG samples (2 QC_Passed, 3 QC_Non_Fails, 2 QC_True_Fails_DEPRECATED). 0/7 mechanically confirmed clones. Recorded to `_aux/Sample_Clone_Report.json`.
- [x] AUDIT verdict = PASS (STRICT). Zero MAJOR / zero MODERATE at S1. Three findings all downstream handoffs (M1 -> S2 ART-ticket target binding; m1 -> S3 owner-attribution triangulation; m2 -> S2 investigation-load-bearing sequence). Recorded to `_aux/Council_Reports/AUDIT_prompt.md`.

## Discrepancies surfaced (for downstream phases, not S1 REVISE)

1. **M1 (S2 handoff):** "the ART tracking ticket in Linear" is not uniquely resolvable at prompt-read time - 597 ART-team issues exist. Bind the OE step by content ("the ART issue whose body ties the Combo-Fighters VFX import vendor work") + accept-set the rubric, or propagate back if S2 verification finds no singleton. Also carried forward from Hardness_Plan §L10 warning.
2. **m1 (S3 handoff):** the owner-attribution rubric must bind to the specific correct identity (GitHub `PERSON_0396_GITHUB_USERNAME`, no linked email - NOT Marcus Bennett the Artist persona) via 3-way Contacts + Linear + GitHub triangulation. The prompt correctly demands "be specific about which Marcus" but does not compel triangulation method.
3. **m2 (S2 handoff):** OE sequence must make the final-response "push back on Leonard?" answer load-bearing on the investigation-derived writes (Linear comment + Trello updates + GDocs brief), not answerable as a shortcut opinion.
4. **Council A hygiene note (Hardness_Plan §L8 chain):** the L8 multi-link chain in Hardness_Plan references `contacts.contacts Leapblock vendor row` - Leapblock has 0 contacts rows. The prompt does not encode a contacts lookup for Leapblock, and the Leapblock followup can be grounded via Drive + Trello + GitHub surfaces. S2 should not encode a contacts lookup for Leapblock in an OE step.
