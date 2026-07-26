# S0 Setup — TODO list (v11 E1 operator-discipline gate)

Task: `Tasks/42_6a62ccac9492f2a60e456c1c`
Universe (expected): starpm (V4) — persona Brooke Phillips, BF "Portfolio Coordination & Owner Relations"

- [x] Step 1: Detect universe — `python Validators/universes.py Tasks/42_6a62ccac9492f2a60e456c1c` → writes `_aux/Universe.txt`
- [x] Step 2: Extract Persona Brief — copy Brooke Phillips section verbatim from `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` to `PersonaBrief.txt`
- [x] Step 3: Split universe — `python Validators/split_universe.py Tasks/42_6a62ccac9492f2a60e456c1c` → `_aux/Universe_Split/`, `_aux/data_hash.txt`
- [x] Step 3b: Build Universe Index — `python Validators/build_universe_index.py Tasks/42_6a62ccac9492f2a60e456c1c` → 5 summary files incl. `today_horizon.json`
- [x] Step 4: Build Fact Ledger — `python Validators/build_fact_ledger.py Tasks/42_6a62ccac9492f2a60e456c1c` → `_aux/Fact_Ledger.json`
- [x] Step 5: Build Graph Report — `python Validators/build_graph_report.py Tasks/42_6a62ccac9492f2a60e456c1c` → `_aux/Universe_Index/graph_report.md`
- [x] Step 6: Build Feasible Surface — `python Validators/build_feasible_surface.py Tasks/42_6a62ccac9492f2a60e456c1c` → `_aux/Feasible_Surface.json`
- [x] V4 injection gate: `9_Universe_inject.sql` is comment-only template header → injection validation SKIPS (no executable statements). Confirm.
- [x] Step 7: Write setup report — `_aux/S0_Setup_Report.md`
- [x] Step 0.5: Write cross-source verification — `_aux/Verification_s0.md` (4 headers, 3 source labels, >=1 checked box, Verdict PASS/REVISE/BLOCK)
- [x] Exit criteria check + STOP gate
