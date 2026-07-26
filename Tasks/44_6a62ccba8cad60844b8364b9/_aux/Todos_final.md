# Todos — PIPELINE FINAL · Task 44 (`44_6a62ccba8cad60844b8364b9`)

**Universe:** starpm (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Density scheme:** StarPM V4 — midpoint >= 40 PASS, applied PER MODEL. V3-family 50/40 does NOT apply.

| # | Step | Status |
|---|---|---|
| 1 | Read root `AGENTS.md` + `Reference/Sessions/FINAL.md` (bootstrap) | completed |
| 2 | Run `phase_ready.py --phase final` (upstream artifact gate) | completed |
| 3 | Create this `_aux/Todos_final.md` (v11 E1 gate) | completed |
| 4 | Create `_aux/Reads_final.md` (v11 E2 gate) | completed |
| 5 | Verify upstream artifacts exist: 5/6/7 + Hardness_Plan + Fact_Ledger + 4_Changelog + 9_Universe_inject | completed |
| 6 | Run `validate.py --phase all` — must exit 0 | completed |
| 7 | V4 gate: `validate.py --phase injection` (Evals_starpm/0, 7 hard gates) | completed |
| 8 | V4 gate: `validate.py --phase submission_gate` (Evals_starpm/5, F1-F9) | completed |
| 9 | Harvest carried-forward AUDIT notes (AUDIT_prompt / AUDIT_oe / AUDIT_rubrics) that FINAL must action | completed |
| 10 | Apply AUDIT_rubrics N6 (`PROPAGATE TO S2`): OE 36 `after 2026-07-01` -> `on or after 2026-07-01` | completed |
| 11 | Re-run validators after the OE 36 wording fix | completed |
| 12 | Spawn Final Council (6 lenses, single high-rigor sub-agent, StarPM-routed spec docs) | completed |
| 13 | Independent coordinator verification pass (answer-leakage grep, Fact_Ledger atom trace, lever trace, density, F7/F8/F9) | completed |
| 14 | Adjudicate council findings; apply fixes in place if REVISE (cap 3 rounds) | completed |
| 15 | Write `_aux/Council_Reports/FINAL_council.md` with VERDICT | completed |
| 16 | Write `_aux/Verification_final.md` (v16 cross-source verification, MANDATORY before exit) | completed |
| 17 | On PASS: append one line to `Tasks/_meta/Hardness_Patterns_Log.md` (levers confirmed end-to-end) | completed |
| 18 | STOP gate — end response, do not chain to S4 | completed |
