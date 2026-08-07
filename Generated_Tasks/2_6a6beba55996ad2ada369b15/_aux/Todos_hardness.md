# Todos — PIPELINE HARDNESS — `2_6a6beba55996ad2ada369b15`

Universe: **harmonygames** (framework `hg`) · Persona: **Robert**, Co-Founder & Creative Director · Business function: **Executive** · Universe today: **2026-02-28** (America/Chicago, a Saturday, month-end, mid-Q1) · Model under test: **Claude Opus 4.7**

v11 E1 operator-discipline gate. One line per atomic step the runbook prescribes.

| # | Step | Status |
|---|---|---|
| 1 | Run `phase_ready.py --phase hardness` and confirm S0 artifacts present | completed |
| 2 | Create this file as the first action of the phase | completed |
| 3 | Read `Tasks/_meta/Learnings.md` end to end (338 lines, L1-L36) | completed |
| 4 | Read `Reference/Hardness_Playbook.md` (11-lever catalog + cost ranges) | completed |
| 5 | Read the HarmonyGames universe constants + landmines in root `AGENTS.md` | completed |
| 6 | Read `_aux/Universe_Index/*` (graph_report, key_facts, entities_personas, accounts_per_entity, today_horizon) | completed |
| 7 | Confirm the injection posture: `4_Changelog.json` empty, `9_Universe_inject.sql` comment-only template | completed |
| 8 | Survey `_aux/Universe_Split/` for the active-window scenario surface (Slack 2026-01 / 2026-02, Linear, Trello, Confluence, GDocs, GSheets, Snowflake, GitHub) | completed |
| 9 | Create `_aux/Reads_hardness.md` (v11 E2 compliance gate) | completed |
| 10 | Spawn the deep-reasoning sub-agent with the lever catalog, Learnings, index files and split access | completed |
| 11 | Sub-agent: lever scan across all 11 levers with per-lever evidence and `L<n>` citation | pending |
| 12 | Sub-agent: select 3-5 levers, maximizing independence | pending |
| 13 | Sub-agent: tool-call density projection against the HarmonyGames scheme (40+ PASS / 15-39 THIN / <15 INSUFFICIENT), necessary-call subtotal reported separately | pending |
| 14 | Sub-agent: stump hypothesis, 2-4 predictions with confidence and mechanism | pending |
| 15 | Sub-agent: feasibility register (persona ACL readability, no Gmail send, no gcal/gslides, date coherence, single-target uniqueness) | pending |
| 16 | Verify the sub-agent's evidence pointers against the split myself before adopting them | pending |
| 17 | Write `_aux/Hardness_Plan.md` with all 6 required sections plus the service-breadth table | pending |
| 18 | Write `_aux/Verification_hardness.md` (v16 cross-source verification) | pending |
| 19 | Append the predicted lever set to `Tasks/_meta/Hardness_Patterns_Log.md` and the predictions to `Tasks/_meta/Stump_Hypotheses.md` | pending |
| 20 | Print the gate verdict (PASS / THIN_DENSITY / INSUFFICIENT_LEVERS / INSUFFICIENT_DENSITY) and STOP | pending |

## Phase-specific notes

- **Density scheme is framework-scoped.** The 50/40 bands in the runbook and playbook are the V3-family scheme and MUST NOT be applied here. HarmonyGames is single-model: authoring target 40+ calls AND 3+ services; prompt-eval hard gate >15 NECESSARY calls AND 2+ services; trajectory QC floor >=15 average.
- **No `gcal.*` and no `gslides.*` data exists in this split.** No lever may depend on Calendar or Slides. Hard rule 13's every-service Calendar sweep is inapplicable, and `v4_gates.py` F9 is skipped for `hg` regardless (deviation HG-U11).
- **Gmail is read-only in this universe.** No send, reply, compose or draft tool exists. Write actions must land on Slack, Linear, Trello, Confluence, GDocs, GSheets, GDrive, GitHub or Contacts.
- **Persona ACL gates reads in seven services** (gmail, slack, gcal, gdrive, gdocs, gsheets, gslides). Every record a lever requires must be readable by Robert specifically, not merely present in the universe.
- **L36 is the governing lesson for this phase.** A trapped universe contributes zero difficulty if the prompt names the traps. Each selected lever must be recorded together with what the prompt has to withhold.
