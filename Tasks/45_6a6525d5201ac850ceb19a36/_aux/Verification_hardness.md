## RESOLUTION (2026-07-27, atoms parsed from split) — updates discrepancy #1 below

Discrepancy #1's census claim ("$387 is only an AR line, not a standalone AP bill") is itself SUPERSEDED after parsing `row_data`:
- The $387 deep clean is BOTH a standalone AP bill (`2026-SC-4C`, Sunshine, $387 unpaid, CURRENT turn) AND an AR pass-through line (`2026-534`). A current-turn deep-clean AP bill EXISTS → **INJ-2 DROPPED**; injection scope = INJ-1 only.
- Current-turn OPEN-scope (deep clean + interior repaint) unpaid AP = `2026-SC-4C` $387 + `PD-2026-09` $1,340 = **$1,727 gross**; NET of INJ-1 $340 credit = **$1,387**. Prior-turn closet-trim `2026-519` ($85) excluded; owner AR invoice `2026-534` ($1,622) is the W-AR decoy.
- Bonus native L11 (no injection): AP repaint $1,340 vs AR pass-through repaint line $1,140 = $200 unreconciled gap.
- 7/15 QC re-inspection confirmed as the SOLE future 4C calendar event (deep-clean/repaint events are past, both 5/21).
- `recbd087.fldNotes2` confirmed verbatim ("deep clean and interior repaint still tracking ... update to Ready once all scopes signed off") — single-field-states-the-answer, justifying injection for the dollar discriminator.

All `[VERIFY-AT-INJECTION]` flags on the QB census are now RESOLVED (exact balances/types confirmed). The only remaining injection-phase work is authoring the INJ-1 `credit_memo` SQL and clearing `validate.py --phase injection`.

---

## REDO verification (2026-07-27) — supersedes the original block below

## Data sources consulted
- `_aux/Universe_Split/` :: airtable.airtable_records (verified recbd087a4abd605b / recc8534b3fd13954 / reca424761ae15355 / rec12969a3fdb0852 all present); quickbooks.quickbooks_entities (verified PD-2026-09, 2026-481-566, 2026-519, 2026-534 present; `credit_memo` entity-type ×117 → INJ-1 schema-consistent); gcalendar.gcalendar_events (Mesa Vista 4C ×20, incl. the 2026-07-15 QC inspection oracle field-read).
- `_aux/Fact_Ledger.json` :: amount atoms cross-checked (387 / 1340 / 85 / 1622).
- `_aux/Universe_Index/` :: today_horizon (2026-07-01 America/Chicago), key_facts, service_inventory.
- `_aux/REDO_reason.md` + `_aux/Candidate_Originals/` :: prior failed lever set + failing trajectories.
- Oracle consult `ses_05ba878c1ffeqGmkLJDrrW46Ku` (bg_96b57bdc) :: lever redesign + injection ruling.

## Reference docs consulted
- `Reference/Hardness_Playbook.md` :: 11-lever catalog + costs; all 11 + L31 scanned; selected = L2 × L11 (INJ-1) symmetric, L8 Opus-pressure, L31 Gemini-sel, L4/L9 support.
- `Tasks/_meta/Learnings.md` :: L36 (withheld-inference root cause), L2/item11 (symmetric structured-store skip), L11/L18/L34 (net-vs-gross + figure-is-the-rubric + accept-set widening), L31 (Gemini negative-directive omission), items 9/20 (displaced-lever / escape-valve pairing), L33 (design for margin).

## Eval spec sub-dims relevant to this phase
- Trajectory dim Tool Call Count (StarPM 15 floor; per-model 40 design target) :: projected per-model midpoint ~45, THIN band (sub-40 real-run risk documented).

## QC spec sub-dims relevant to this phase
- Trajectory T1 Tool Call Count :: ~45 projected, THIN; hard S4 sub-40 REDO gate carried forward.

## Verification statements
- [x] At least 3 levers selected; each cites a Learnings entry.
- [x] Density midpoint projection classified (THIN, 40-49 band; sub-40 real-run risk explicit).
- [x] Service breadth table populated (7 of 8 services).
- [x] REDO lever set materially differs (recency L1/L10 RETIRED; injected net-vs-gross ADDED); `## Lever changes from previous attempt` present in the plan.
- [x] Oracle injection-vs-prompt-only ruling captured; operator decision surfaced, not silently overridden.

## Discrepancies surfaced
1. **CENSUS CORRECTION** — original plan + Learnings L36 assert "$387 + $1,340 unpaid bills". Oracle's field-read + this session's token counts indicate the $387 is a *line inside* AR invoice 2026-534 (owner receivable), NOT a standalone AP bill. Current-turn AP payables = PD-2026-09 (~$1,340) + 2026-481-566 (~$85); prior-turn 2026-519 (~$85) excluded from any current-turn figure. Exact composition + whether a standalone current-turn deep-clean AP bill exists flagged `[VERIFY-AT-INJECTION]` (drives INJ-2).
2. **SCOPE CONFLICT** — `REDO_reason.md` scoped this rebuild as prompt-only / no-universe-edits; oracle ruled minimal V4 injection is REQUIRED to reach Opus ≤40% (the SoR note states the top-line answer in one field, so no prompt-only reframe survives careful reading). Surfaced to the operator as a decision before S1.

---

# Verification — HARDNESS (Task 45, StarPM V4)

## Sources consulted
- Per-task data :: _aux/Universe_Split/airtable.airtable_records.json — grepped tblMakeReady + tblMaintenanceTickets: Mesa Vista 4C = 3 records (recbd087 selProg current turn / recc8534 selReady prior turn / reca424 maint-ticket "complete"); ambiguity counts Las Palmas 8D=4, Las Vistas 9D=7, Las Palmas 212D=1, Las Vistas 3C=1.
- Per-task data :: _aux/Universe_Split/gcalendar.gcalendar_events.json — only future (>=2026-07-01) Mesa Vista 4C event is the QC inspection 2026-07-15 (confirmed).
- Per-task data :: _aux/Fact_Ledger.json — confirmed recbd087a4abd605b in airtable id list; amount/date/id atom counts checked for lever feasibility.
- Per-task data :: _aux/Universe_Index/graph_report.md — make-ready density (selProg 56 / selSched 43 / selReady 21), Jaime 48 mentions, C004 #make-ready busiest (144); density signals support cross-service breadth.
- Reference :: Reference/Hardness_Playbook.md — considered all 11 levers; selected L2 (structured-DB skip), L1+L10 (latching/supersession), L31 (negative directive), plus L7/L9 support.
- Reference :: Tasks/_meta/Learnings.md — cited L1/L13, L2/L10/L11, L4/L5 (avoided as sole levers), L6, L7, L9, L15/L16, L31, dual-model items 9-12, Task-39 items 13-16, base64 item 17.
- Eval spec :: Evals_starpm Trajectory dim Tool Call Count (StarPM floor 15; design 40+ per model) — projected midpoint Opus ~45 / Gemini ~43.
- QC spec :: Docs_starpm/7_QC_Spec_Doc1.json Trajectory Tool Call Count — projected per-model ~45/~43, band = PASS (StarPM >= 40 design target).

## Verification statements
- [x] At least 3 levers selected; each cites a Learnings entry (L2, L1/L10, L31 + support L7/L9).
- [x] Density midpoint projection classified on the StarPM per-model band {PASS >= 40, THIN 15-39, INSUFFICIENT < 15} — result PASS (both models >= 40). (V3-family 50/40 scheme deliberately NOT applied — universe is starpm.)
- [x] Service breadth table populated (v11 G1) — 7 of 8 distinct services, PASS.
- [x] Single-target uniqueness pre-check performed (rule 13) — anchor is multi-row; disambiguation contract issued to S1/S3; F9 future-event sweep clean.

## Discrepancies surfaced
- Sub-agent under-counted Mesa Vista 4C rows (claimed 2, actual 3 records across 2 tables: 2 make-ready + 1 maint ticket). Las Palmas 8D grepped as 4 records but the accurate breakdown is **3 make-ready rows + 1 maintenance ticket** (`recb403fe` MT-2026-1325) — do not conflate tables (same care taken for 4C). 8D stays excluded either way. Corrections strengthen the plan: the maintenance-ticket + prior-turn selReady form a richer latching/supersession decoy set, and the later-created selReady row is a verified "latest-row" disambiguation trap.

## Verdict
- PASS — all four verification statements confirmed; three-plus levers selected with density projection PASS on the StarPM per-model band, service breadth 7/8, single-target uniqueness pre-check done. Ready for S1.
