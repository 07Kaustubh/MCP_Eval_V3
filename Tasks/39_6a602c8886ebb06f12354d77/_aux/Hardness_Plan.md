# Hardness Plan — Tasks/39_6a602c8886ebb06f12354d77

## Phase context (read first)

Fresh forward HARDNESS (post-S0, pre-S1). Every deliverable in the task folder is an empty PIPELINE-NEW scaffold: `5_Prompt.txt` / `6_Oracle_Events.txt` / `7_Rubrics.json` are "Paste ... below" placeholders; `8a` / `8b` / `9` / `10` / `11` are 0 bytes; `Agent_Responses/` holds no valid runs (`parse_trajectories.py` → 0/12 evaluable, all `empty_or_invalid`). This plan is therefore a genuine forward lever projection for the S1 prompt writer, not a retrospective.

Universe: **StarPM V4** (`_aux/Universe.txt` = `starpm`). Today 2026-07-01 (America/Chicago); active window 2026-05-01 to 2026-07-01. Single entity `starpm`.

**Density gate is the StarPM V4 per-model scheme** (Docs_starpm/1 hard gate; FRAMEWORKS `density_floor`): design target average 40+ tool calls, absolute floor 15, applied to **Opus 4.8 and Gemini separately**. Bands: midpoint >= 40 = PASS, 15-39 = THIN, < 15 = INSUFFICIENT. The V3-family 50/40 bands do NOT apply to this task.

## Injection status (finding — surface downstream)

`9_Universe_inject.sql` is a **comment-only template stub**: lines 1-73 are all `--` comment lines ending at "PASTE YOUR SQL STATEMENTS BELOW" with zero executable statements after it. `4_Changelog.json` is `[]`. Per AGENTS.md, a comment-only inject header SKIPS the injection gate.

The S0 report (`_aux/S0_Setup_Report.md`) claims `9_Universe_inject.sql` is "present with executable statements (73 lines)" and that `validate.py --phase injection` returned **PASS** on injected scenario data. That claim is **inaccurate against the current file** (the 73 lines are all comments). Downstream phases must treat this task as having **no separately-documented injection**. The Las Palmas 8D scenario the levers ride on nonetheless exists in the per-task export (`_aux/Universe_Split/`, spot-verified below), i.e. the scenario is baked into `3_UniverseDataForThisTask.json` rather than carried by the inject file. No injection is required to proceed to S1; an optional sharpening injection is described in the last section.

## Persona and Business Function

- **James Bennett** (`p_006`, james.bennett@starpm.com) — Assistant Maintenance Technician. Junior; Department: Maintenance.
- Business Function 4 · **Maintenance & Repairs**.
- **Design-surface persona:** 0 scripted actions, participant-only cast in `makeready_laspalmas8d_turn`. Author-from-spec — model the ask on Assistant Maintenance Tech work (executes assigned tickets under Lead John Smith / Elias Navarro routing, tenant appointments, reports completion). Natural systems: Linear (ticket execution), Slack `#maintenance` (C001) / `#make-ready` (C004), Google Calendar (dispatch), Gmail (draft-only).

The load-bearing scenario is the **Las Palmas 8D make-ready turn**, in which James is a named participant.

## Levers Available

Every yes/partial lever cites a row spot-verified in `_aux/Universe_Split/` (see Verification section).

| # | Lever | Status | Evidence (file:row_id) | Cost |
|---|---|---|---|---:|
| 1 | Latching | yes | `slack.slack_messages.json:140558bdd3bc57c09660a0aeecc6d9ee` ("Both punch-list items on 8D are taken care of") + `slack:21f0475ef12952d0ac3e13f3019eb880` ("Carpet is done on 8D") anchor a "done" first framing that an early Airtable row echoes but `linear:comment_16a0a0c53f...` contradicts | 5-8 |
| 2 | Structured-DB skip | yes | `linear.linear_teams.json:team_001` ("...the system of record. Linear is secondary for maintenance items...") + true state in `airtable:recac236210094352` (MT-2026-1271, `fldCompletionDate` blank = OPEN) | 4-7 |
| 3 | Missing reply | yes | `airtable:rec4a0a0e7c845756` (Tony: "Which vendors are confirmed for the 204B turn?") answered only in `airtable:rec8e650892e2da5f` (Isela: "Carpet is confirmed... $610 Valley Floor Co."); `linear:comment_16a0a0c53f...` ("Routing back to you for parts approval before I swap it") needs the approval reply to resolve | 3-5 |
| 4 | Search-result-cap eviction | yes | 61 "Las Palmas 204B" occurrences across `tblMakeReady` rows (`rec06e5ecfb550a58`, `rec32c630c943c155`, ...) bury the ~6 "8D" occurrences (`receb057b02f20052`, `recf7aecc318b2252`, `rec651427ec0d84dd5a`, `recac236210094352`) | 3-5 |
| 5 | Thread-reply blindness | partial | `slack:0ebe25f10c325a1aa847244b1f50107c` (`reply_count` 1) and `slack:297f14105d465ce1b7e66a59f1ad3ecb` (`reply_count` 2) carry thread structure, but no confirmed 8D-critical resolution sits inside a reply in base data | 2-4 |
| 6 | Near-miss entity | yes | `airtable:rec651427ec0d84dd5a` (Las Palmas 8D refrigerator swap, Thu 6/25) vs `airtable:recb403fe04c2f97683` (Rio Bend 214 dishwasher swap, same 6/25); also `tony.reyes@starpm.com` vs a second Reyes contact | 3-5 |
| 7 | Multi-write diversification | yes | Write surfaces reachable by James: Slack C004/C001, Gmail draft, Linear `save_comment` on OPS-227, Airtable `tblMakeReady` update; anchor `airtable:recf7aecc318b2252` (James in-house on 8D) | 9-12 |
| 8 | Multi-link chain | yes | `slack:140558bdd3...` ("8D done") to `airtable:recac236210094352` (ticket still OPEN) + `airtable:rec651427ec0d84dd5a` (6/25 swap in progress) to `linear:comment_16a0a0c53f...` (6/22 disposal seized, replacement pending) | 6-9 |
| 9 | Universe-grounded gotcha | yes | Gmail draft-only (no send tool), Slack `message` not `payload`, Linear `team` not `teamId`; plus early "cleared/ready" note is not actual readiness (`airtable:receb057b02f20052` stale) and Airtable-is-SoR (`linear:team_001`) | 3-5 |
| 10 | Reversal / supersession | yes | `airtable:receb057b02f20052` (8D early "ready/closed out", 2026-05-01) superseded by `airtable:recf7aecc318b2252` (in-progress, 2026-05-14) and `airtable:rec651427ec0d84dd5a` (in-progress, 2026-06-25) and `linear:comment_16a0a0c53f...` (2026-06-22 disposal seized) | 4-6 |
| 11 | Net-vs-gross framing | partial (NOT selected) | `airtable:rec70812e7cb9c058` ("$340 bathroom fixture... turn budget or maintenance budget") + `rec4ca8d7181be15c` ($640 carpet); turn-cost aggregation exists but is finance-flavored and unnatural for a junior tech. `entities`/`fiscal_periods` = 0 confirms no GL/account-number trap | 4-7 |

Levers with sufficient base backing: **9 of 11** (5 partial/excluded: L5 partial, L11 partial-not-selected). Well above the 3-lever floor.

## Selected Levers (5)

1. **L10 Reversal / supersession** — the most-findable 8D record reads "ready / closed out" (2026-05-01) but three later rows show the turn still live through 6/25. Justified by Learnings **L25** (existing-output / stale-artifact anchor). Midpoint contribution: **5.0**.
2. **L2 Structured-DB (Airtable) skip** — `team_001` hardcodes Airtable as system of record with Linear as a secondary mirror; the OPEN ticket MT-2026-1271 lives only in Airtable. Justified by Learnings **L10** (structured-DB skip — Airtable is the StarPM analog of the SAP-subledger skip). Midpoint: **5.5**.
3. **L1 Latching** — the Slack "8D punch-list done / carpet done" chatter is the first framing an agent meets and reads as authoritative. Justified by Learnings **L13** (first-framing anchor); primed for **L9** (authority-figure dismissal) if a Lead reinforcement is planted (see optional injection). Midpoint: **6.5**.
4. **L4 Search-result-cap eviction** — the real 8D rows are buried under 61 "Las Palmas 204B" decoy make-ready occurrences (~10:1); a broad "Las Palmas / make-ready" query returns the 204B swarm and evicts 8D. Justified by Learnings **L26** (decoy overlap). Midpoint: **4.0**.
5. **L3 Missing reply** — the disposition (whether James swaps the disposal, whether the vendor is confirmed) sits in a reply the agent must chase, not the message it first finds. Justified by Learnings **L12** (reply invisibility). Midpoint: **4.0**.

Write breadth (catalog **L7**) is carried by the standalone Write-actions row below, not double-counted as a discovery lever. **Mechanism independence:** temporal-supersession (L10), source-of-record (L2), first-framing (L1), result-eviction (L4), and search-for-response (L3) fire through five distinct failure paths — not five variants of latching.

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---:|
| Base discovery (contacts, channel resolve, 8D record + OPS-227 lookup) | 5-8 | 6.5 |
| L1 Latching | 5-8 | 6.5 |
| L2 Structured-DB skip | 4-7 | 5.5 |
| L3 Missing-reply | 3-5 | 4.0 |
| L4 Search-cap eviction | 3-5 | 4.0 |
| L10 Reversal / supersession | 4-6 | 5.0 |
| Write actions (3+ writes: Airtable update, Linear comment, Slack post, Gmail draft) | 9-12 | 10.5 |
| Cross-service buffer | 5-8 | 6.5 |
| **TOTAL projected** | **38-59** | **48.5** |

**Per-model midpoint ≈ 48.5**, applied separately to Opus 4.8 and Gemini.
**Gate (StarPM V4: 40 design / 15 floor):** 48.5 >= 40 → **PASS**.

## Service Breadth (v11 G1)

| Service | Calls (est.) | % of total |
|---|---:|---:|
| airtable | 14 | 30% |
| linear | 10 | 21% |
| slack | 9 | 19% |
| gmail | 5 | 11% |
| contacts | 4 | 9% |
| gcalendar | 3 | 6% |
| quickbooks | 1 | 2% |
| hubspot | 1 | 2% |
| **Distinct services (meaningful)** | **6** | — |

Six services at >= 5% (airtable, linear, slack, gmail, contacts, gcalendar); quickbooks + hubspot are decoy-only touches (turn-cost classification, Tanya ESA ticket). Write surfaces span **4** services (airtable, linear, slack, gmail-draft).
**Breadth gate:** >= 4 distinct services each >= 5% → **PASS**. This is genuine cross-correlation breadth, not a single-service deep trap.

## Stump Hypothesis

1. **[HIGH]** Both models report Las Palmas 8D as ready/complete and omit the outstanding disposal replacement. Mechanism: **L10 + L1**. Reasoning: the early "ready/closed out" Airtable row plus Slack "punch-list done" anchor the first framing; the superseding 2026-06-22 `linear:comment_16a0a0c53f...` (disposal seized) and 6/25 swap row get missed (Learnings L13 / L25).
2. **[HIGH]** Both models trust the Linear OPS-227 mirror and never query the Airtable ticket table as SoR, so they miss MT-2026-1271 still OPEN. Mechanism: **L2**. Reasoning: `team_001` hardcodes Airtable-as-SoR; models default to Linear/Slack chatter (Learnings L10).
3. **[MED]** Both models conflate Las Palmas 8D with Rio Bend 214 (same-day 6/25 swap) or lose 8D under the 204B decoy swarm and report the wrong unit's status. Mechanism: **L4 + L6**. Reasoning: 61 "204B" occurrences evict the 6 "8D" ones; the 214/8D twin invites a cross-property mixup (Learnings L26).
4. **[MED]** Both models collapse the write into a single Slack/email update, or UPDATE the stale row instead of writing the correct current state across services. Mechanism: **L7 + tool-variant**. Reasoning: default single-write behavior and record-reuse over fresh-write (Learnings L27 / L28).

## Hardness Score

**5/5 selected — PASS.** Five independent-mechanism levers grounded in verified base rows; per-model density midpoint 48.5 (>= 40 StarPM V4 PASS); breadth across 6 services with 4 write surfaces. No STOP gate fired (levers >= 3; density >= 15 floor and >= 40 design target).

## Hardness Brief for the Prompt Writer

Write James a junior maintenance-tech ask centred on reconciling and advancing the **Las Palmas 8D make-ready turn**, then reporting the current true state and next actions. The hardness rides five levers: a stale "ready / closed out" record from May 1 superseded by live in-progress work through late June (supersession); Airtable as the system of record while Linear only mirrors it (structured-DB skip); early Slack "8D is done" chatter that reads as authoritative (latching); the real 8D rows buried under a swarm of Las Palmas 204B decoys (result eviction); and the disposition sitting in a reply the agent must chase, not the first message it finds (missing reply). Force 3+ writes across at least three services (Airtable status/notes correction, Linear comment on the open disposal thread, a Slack post, and a Gmail draft to the Lead). Keep it implicit (Learnings L15) — the persona believes the turn is essentially done and asks James to close it out and report; do NOT hint the record is wrong. Do not name tools or IDs in the prompt, do not place the answer verbatim in any body (L6), keep James's voice short and junior, and stay under the 500-word cap with no em-dashes. Density target: 40+ tool calls per model (projected ~48).

## Injection status & recommendation

**Base data SUFFICES — no injection required for a PASS.** The base per-task universe supports 9 of 11 levers, 5 independently selected, projecting ~48 tool calls per model (above both the 15 floor and the 40 design target). Recommend proceeding to S1 on base data. The inject file stays a comment-only stub and `4_Changelog.json` stays `[]`; this plan does not assume any injection.

**Load-bearing base rows (S1 MUST preserve):**
- `airtable.airtable_records.json:receb057b02f20052` — 8D early "ready / closed out" (2026-05-01), the stale anchor.
- `airtable.airtable_records.json:recf7aecc318b2252` — 8D in-house work, John Smith + James Bennett (2026-05-14), James's participation anchor.
- `airtable.airtable_records.json:rec651427ec0d84dd5a` — 8D refrigerator swap in progress (6/25, target 6/26), live-state proof.
- `airtable.airtable_records.json:recac236210094352` — MT-2026-1271, 8D, `fldCompletionDate` blank (OPEN ticket in the SoR).
- `airtable.airtable_records.json:recb403fe04c2f97683` — Rio Bend 214 twin (near-miss).
- `linear.linear_comments.json:comment_16a0a0c53f543a1221f08de6a786cb66` — OPS-227, James: flywheel frozen, needs full replacement + parts approval (the flip).
- `linear.linear_teams.json:team_001` — Airtable-is-SoR / Linear-secondary declaration.
- `slack.slack_messages.json:140558bdd3bc57c09660a0aeecc6d9ee` and `:21f0475ef12952d0ac3e13f3019eb880` — the "8D done" latching chatter.
- `airtable.airtable_records.json:rec4a0a0e7c845756` + `:rec8e650892e2da5f` — the question/reply pair for the missing-reply pattern.

**Optional sharpening (NOT required for PASS).** To lift difficulty toward the top of the band and add the ~100%-fail authority path (Learnings **L9**), a compliant `9_Universe_inject.sql` could ADD (never modify base): (a) one Lead message from John Smith or Elias Navarro in `#make-ready` around 6/28 asserting "8D is done, go ahead and mark it ready," planted AFTER the reductions so the agent must reject a plausible-but-wrong authority frame; and (b) a paired Airtable QC-inspection note for 8D (authoritative vs a superseded near-duplicate) to stand in for the StarPM near-duplicate-file landmine — this universe has NO filesystem service, so the base data contains no `report-laspalmas-8d-qc-inspection.pdf`-style file rows (that AGENTS.md landmine does not apply here). Any such injection must add rows only and clear `validate.py --phase injection` (7 gates + difficulty >= 3.5) before use.

## Verification (row-grounding spot check)

Independently confirmed via grep on `_aux/Universe_Split/` (not taken on the sub-agent's word):
- `receb057b02f20052` present (1 hit, airtable_records); `recf7aecc318b2252` present (James anchor).
- `recac236210094352` present → `"fldTicketNumber": "MT-2026-1271", "fldCompletionDate": ""` in `tblMaintenanceTickets`, created 2026-05-01 (OPEN confirmed).
- `comment_16a0a0c53f543a1221f08de6a786cb66` present → "...motor won't reset and the flywheel is frozen. This needs a full unit replacement... Routing back to you for parts approval before I swap it. — James", `issue_id` OPS-227 (the flip confirmed).
- `linear_teams.json` → "...table, which is the system of record. Linear is secondary for maintenance items..." (Airtable-is-SoR confirmed).
- Decoy swarm: **61** "204B" occurrences vs **6** "8D" occurrences in airtable_records (L4 eviction confirmed, ~10:1).
- `recb403fe04c2f97683` present → `"fldUnit": "Rio Bend 214"` appliance swap (near-miss twin confirmed).

Not fully verified (flagged for S1): the sub-agent could not finish reading `StarPM_Base_Universe/7_Server_Tools_Details.json`; S1 must re-confirm the exact StarPM write-tool signatures against that file before drafting write steps (Slack `message`, Gmail draft-only `body`, Linear `team`/`save_comment`, Airtable camelCase).
