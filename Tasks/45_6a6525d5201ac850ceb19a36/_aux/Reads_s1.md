# Reads — S1 (Task 45, StarPM V4)

Every QC spec doc / Reference card / Eval spec / universe artifact consulted while drafting `5_Prompt.txt`.

## Runbook + format cards
- Reference/Sessions/S1.md :: S1 procedure, required inputs, exit criteria, STOP gate.
- Reference/Prompt_Format.md :: hard rules (500-word cap, no em/en-dash, no tool names, no MCP-server names, no internal IDs, no pre-solving, first-person, one coherent situation); voice (mid-thought entry, asymmetric knowledge); Trigger->Context->Asks; push 3+ writes across 3+ services; anti-patterns (command list, pre-solve, ID leak, tool-name list, contrived format, bolt-on). Confirmed draft complies on all.
- Reference/Council_Protocol.md :: Council A (explore) + Council B (oracle) perspective sets for prompt phase; sub-dim scoring-scheme map (which Prompt sub-dims are binary 1/5 vs 1/3/5).
- Reference/Hardness_Playbook.md :: lever catalog (consulted via _aux/Hardness_Plan.md lever table).

## StarPM specs / evals
- Docs_starpm/9_Common_Error.md :: Part 1 prompt-writing errors (7 pitfalls: over-specific/ID leak, sequential command list, tool/param names, pre-solving, bolt-on, email-only writes, too-short). Verified draft avoids all 7.
- Docs_starpm/4_Prompt_Hard_Tips.md :: Opus failure modes that validate the chosen levers — "agents skip structured databases" (= L2 symmetric primary), "agents latch onto the first framing" (= L1), "agents don't search for responses", "diversify write actions", "ask for both investigation and action (agent wrote report but never sent it)".
- Docs_starpm/6_Prompt_Relative_Time_Updates.md :: universe today = 2026-07-01; relative-date resolution rules. Draft dates: "middle of June" ~6/15, "end of the month" ~6/30 (past), "middle of this month" ~7/15 (near future, 4C QC re-inspection). All coherent with the 7/1 baseline.
- Evals_starpm/1_Prompt_Eval.md :: per-sub-dim scoring deferred to Council B adversarial pass; verdicts recorded in Verification_s1.md.

## Per-task universe artifacts
- _aux/Hardness_Plan.md :: levers L2 (structured-DB skip, symmetric), L1+L10 (latching/supersession, Opus-sel), L31 (explicit negative directive, Gemini-sel), + L7 multi-write, L9 future-event; anchor = tblMakeReady recbd087a4abd605b (selProg); rule-13 disambiguation contract (pin the current turn by mid-June move-out / end-June target / 7-15 re-inspection); density projection per-model ~45/~43.
- PersonaBrief.txt :: Jaime Salinas (QC Inspector, p_007) voice — short, factual, observation-first, verbosity 0.30, zero emoji, impartial sign-off anchor.
- _aux/Universe_Index/entities_personas.md :: Carlos Mendez (Onsite Property Manager), Brooke Phillips (Apartment Property Supervisor), Jaime Salinas (QC Inspector) — grounded cast.
- _aux/Universe_Index/today_horizon.json :: today 2026-07-01 America/Chicago.
- _aux/Feasible_Surface.json :: service/field/state surface for feasibility.
- Validators/validate.py SERVICE_KEYWORDS :: cross-service detector logic (drove adding natural detectable system references: "issue tracker" / "channel" / "email").

## Reference corpus (voice/structure only — Brookfield-flavored content)
- QC_Tasks/V4_Tasks/QC_Passed/Task1..Task4/5_Prompt.txt :: first-person, situation-first, asks woven in prose, write targets named by business function (never tool functions), correct answer implicit, sign-off/hold archetype (Task3/Task4).
