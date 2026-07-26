# Verification — AUDIT prompt phase

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** `starpm` (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Report:** `_aux/Council_Reports/AUDIT_prompt.md` · **Verdict: PASS (STRICT)**

## Strictest interpretation re-applied
- Every "should" in the QC spec and in `Evals_starpm/1_Prompt_Eval.md` read as "must".
- Every NON-FAIL middle band collapsed to REVISE (none was needed — 14/14 sub-dims at 5).
- Density floor: **StarPM V4 per-model bands** (>= 40 PASS, 15-39 THIN, < 15 INSUFFICIENT), NOT the V3-family 50/40 scheme, per AGENTS.md hard rule 11 and the AUDIT.md framework-scoping note.
- Every soft convention in `Reference/Prompt_Format.md` treated as binding.
- Every validator WARN (1) and NOTE (6) listed and individually adjudicated.

## Data sources consulted (re-verified from source — NOT trusting prior phase outputs)
- `_aux/Universe_Split/` — parsed with `json.loads` on `row_data`, not grepped:
  - `linear.linear_issues` (230) — state_id + completed_at + assignee_id + creator_id + project_id on OPS-16/17/18/28/34/35/40/43/44/51/56/66/71/81/87/91/96/97/98/99/108/186; full proj_003 enumeration (60 rows)
  - `linear.linear_comments` (48) — full sweep; authorship resolved via author_id
  - `linear.linear_workflow_states` (5), `linear.linear_projects` (3), `linear.linear_users`
  - `slack.slack_messages` (580; C001 = 104, 56 replies under 37 parents), `slack.slack_channels` (8), `slack.slack_users`
  - `gcalendar.gcalendar_events` (565; 27 rows / 9 unique confirmed events on or after 2026-07-01), `gcalendar.gcalendar_calendars`
  - `airtable.airtable_tables`, `airtable.airtable_fields`, `airtable.airtable_records` (50 in tblMaintenanceTickets)
  - `contacts.contacts` (61), `gmail.gmail_messages` (484)
  - `Universe_complete_data.json` (4.4 MB) — 103-pattern answer-leakage sweep
- `_aux/Fact_Ledger.json` — atoms re-grounded: `ids.linear_issue` confirmed to contain OPS-87/96/98/40/91/186; `ids.slack_channel` = C001-C008; `lifecycle.today` = null (see discrepancies)
- `_aux/Universe_Index/today_horizon.json` — authoritative date anchor 2026-07-01 America/Chicago
- `_aux/Similarity_Report.json` — max composite 27.2, corpus 44, band below_40
- Tool catalog (universe-aware per `_aux/Universe.txt` = starpm): `StarPM_Base_Universe/7_Server_Tools_Details.json` — linear 42 tools, slack 19, airtable 22, gcalendar 9, gmail 13, contacts 8, quickbooks 141, hubspot 14. Verified `list_issue_statuses.team` is REQUIRED, `save_issue.assignee` typed "null", gmail exposes `create_draft` with no send tool.

## Eval spec verified for this phase
- Universe-correct eval set: `Evals_starpm/` (starpm). `Evals_starpm/1_Prompt_Eval.md` read in full; every hard gate executed literally — end-state divergence, T11 precision guardrail, convergence investigation (N/A at S1, recorded not skipped), T10 dimensional feasibility, phantom tight-identifier grep, write-action divergence, delegation clarity, minimum complexity, 2.8 date alignment against 2026-07-01.
- `Evals_starpm/5_Submission_Gate_Eval.md` defect families applied: F7 AMBIGUOUS_TARGET, F8 NON_ATOMIC_ENUM, F9 UNRECONCILED_FUTURE_EVT — all CLEAN, each re-derived independently (F9 by reading all 565 calendar rows).

## QC spec re-verified (universe-correct doc set: starpm → `Docs_starpm/`)
- `Docs_starpm/7_QC_Spec_Doc1.json` — 14 applicable sub-dims (12 Prompt + 2 Universe) rescored under strict interpretation; all 5. The stale "Jun 12, 2026" date string inside the JSON was NOT used; the evals plus `_aux/Universe_Index/today_horizon.json` fix today at 2026-07-01 America/Chicago.
- `Docs_starpm/8_QC_Spec_Doc2.md` — appendix issue taxonomy re-applied (atomicity, self-containment, incorrect vs overly-broad) to the downstream bindings recorded as A-1 through A-6.
- StarPM caveat honoured: `Docs_starpm/13_QC_Companion.md` was NOT consulted (Brookfield-contaminated per `Validators/regression_baseline/ROUTING_DECISIONS.md`).

## All 9 lenses status
- Lens 1 strict QC scoring :: PASS (14/14 sub-dims at 5; 17-row per-atom evidence table produced)
- Lens 2 answer-leakage sweep :: PASS (103 patterns, zero hits)
- Lens 3 hardness end-to-end :: PASS (5/5 levers trace with cited evidence; OE/rubric columns N/A at S1)
- Lens 4 strict density :: PASS (Opus 47, Gemini 41, combined 44; StarPM V4 per-model bands)
- Lens 5 adversarial review :: PASS (finding A-3 recorded on the L31 wording gift)
- Lens 6 lifecycle + narrative state :: RETIRED in v18, not executed
- Lens 7 anti-rationalization :: PASS (6 candidates found, 6 promoted, 0 silently cleared, 2 rejected as deference)
- Lens 8 regression-anchor verification :: 62/62 PASS
- Lens 9 unique ground truth middle-band :: RETIRED in v18, not executed

## Verification statements
- [x] Validator (`validate.py --phase prompt`) result consumed: PASS, exit 0, 0 fails, 1 WARN, 6 NOTES — every WARN and NOTE individually adjudicated (result pre-supplied, not re-run this pass).
- [x] Regression-anchor suite executed this pass; **62 of 62 anchors PASS**, 0 failed.
- [x] Anti-rationalization output check performed and reported in full; 6 "I considered flagging X" lines found, all 6 promoted to logged findings, none silently cleared.
- [x] Verdict (PASS STRICT) recorded with an explicit per-issue trail of 15 findings, each with severity, location and exact fix.

## Discrepancies surfaced
1. `_aux/Fact_Ledger.json` `lifecycle.today = null` → `Validators/validate.py:464` emits the hardcoded Brookfield fallback 2026-06-12. Wrong for starpm; 2026-07-01 is authoritative. Pre-declared known defect; three-part fix recorded at A-11, and fix (1) must land before S2 starts because `6_Oracle_Events.txt` is still an unfilled template.
2. `Validators/validate.py:464` bypasses `Validators/universes.py`, which already carries the correct `starpm.today = "2026-07-01"`.
3. Council A mis-cited proj_003 membership on its load-bearing "still sitting open" row (OPS-35/56/97/98/99/108/186 are proj_002 or proj_001). Conclusion survives on re-derivation; citation does not.
4. Council B's defence of the L31 retraction beat rests on an invalid premise (rubric visibility conflated with prompt visibility). The beat is displaced behind Lever 2's discovery gate rather than independently Gemini-selective.
5. `_aux/Hardness_Plan.md` carries three factual errors: C001 thread parents stated as 15, actual 37; "five days after Elias" is 7 days; service breadth stated as linear 34% with 6 services at >= 5%, strict re-derivation gives 53% with 4.
6. `StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md` names Linear as system of record for maintenance tickets, contradicting `linear_teams.team_001.description` and `airtable_tables.tblMaintenanceTickets.description`, which both name Airtable. Live universe data wins.
7. `StarPM_Base_Universe/7_Server_Tools_Details.json` `save_issue.assignee` is typed "null", the only such parameter in the catalog. Harmless here — the prompt says "named on it", not "assigned to it".
8. Base-universe noise, none CB-authored (`4_Changelog.json` = `[]`): OPS-34 carries 18 topically unrelated comments under an exterior-signage title and a dangling "#make-ready" cross-reference; GCalendar events repeat 3-6x per logical event; OPS-99/OPS-108 and OPS-51/OPS-71 are identical-title pairs in opposing states; OPS-91 is an inverted state/prose pair.
9. `verify_universe_atoms.py` returned 0 atoms checked with an empty evidence table — structurally correct for a prompt that carries no IDs, amounts or ISO dates by design, but evidentially vacuous, so Truthfulness 5/5 rests entirely on the manual 17-row table in the audit report.
