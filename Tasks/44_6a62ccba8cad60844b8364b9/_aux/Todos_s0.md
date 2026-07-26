# TODOs — PIPELINE S0 — Tasks/44_6a62ccba8cad60844b8364b9

Phase: S0 (Setup). v11 E1 operator-discipline gate.

| # | Step | Status |
|---|---|---|
| 1 | Read root `AGENTS.md` bootstrap (PIPELINE DISPATCH + HARD RULES) | completed |
| 2 | Read `Reference/Sessions/S0.md` runbook | completed |
| 3 | Detect universe — `python Validators/universes.py Tasks/44_6a62ccba8cad60844b8364b9` → `_aux/Universe.txt` | completed |
| 4 | Extract Persona Brief verbatim → `PersonaBrief.txt` (universe-correct briefs file) | completed |
| 5 | Split per-task universe — `python Validators/split_universe.py` → `_aux/Universe_Split/` + `_aux/data_hash.txt` | completed |
| 6 | Build Universe Index — `python Validators/build_universe_index.py` → 5 summary files | completed |
| 7 | Build Fact Ledger — `python Validators/build_fact_ledger.py` → `_aux/Fact_Ledger.json` | completed |
| 8 | Build Graph Report — `python Validators/build_graph_report.py` → `_aux/Universe_Index/graph_report.md` | completed |
| 9 | Build Feasible Surface — `python Validators/build_feasible_surface.py` → `_aux/Feasible_Surface.json` | completed |
| 10 | V4 injection gate — `python3 Validators/validate.py --phase injection` (SKIP expected: `9_Universe_inject.sql` is comment-only template header) | completed |
| 11 | Write `_aux/S0_Setup_Report.md` (persona, business function, data hash, record counts, today/horizon, post-today note) | completed |
| 12 | Write `_aux/Verification_s0.md` (v16 cross-source verification, 4 exact headers, verdict) | completed |
| 13 | Confirm exit criteria + STOP (no HARDNESS in this chat) | completed |
