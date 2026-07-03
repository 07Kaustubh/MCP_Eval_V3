# Verification — AUDIT prompt (Task 37, on-demand strictest)

## Strictest interpretation re-applied
- 5/5 only on every applicable Docs/7_QC_Spec_Doc1.json sub-dim.
- Every "should" in the eval spec read as "must".
- Every validator WARN treated as a hard candidate issue (each verified by re-derivation, not narrative dismissal).
- Density bar: 50+ midpoint (not 40 floor).
- Any answer-leakage on a derived figure = BLOCKER.

## Data sources consulted
- `5_Prompt.txt` (unchanged from candidate)
- `_aux/Universe.txt` → `keystone` confirmed
- `_aux/Universe_Split/mortgage_los.staff.json` (Marcus Webb landmine — DIRECT QUERY)
- `_aux/Universe_Split/mortgage_los.loans.json` (26-loans + status distribution + LO assignment atoms)
- `_aux/Universe_Split/mortgage_los.conditions.json` (LN-2026-00008 2-outstanding-conditions atom)
- `_aux/Universe_Split/mortgage_los.document_checklist_items.json` (26-outstanding-docs / 8-loans atom set)
- `_aux/Universe_Split/slack.slack_messages.json` (C002/C004 verbatim scope quotes)
- `_aux/Fact_Ledger.json` (41 atoms cross-reference)
- `_aux/Universe_Index/*.json` (service inventory, entities, today horizon)
- `_aux/Council_Reports/REVIEW_hardness.md` (8 lever inventory + measured 216.8 avg / 33.3% pass@1)
- `_aux/Council_Reports/verify_universe_atoms.md` (41/41 PASS)
- `_aux/Council_Reports/REVIEW_FINAL.md` (prior baseline)
- `_aux/Council_Reports/FINAL_materialize.md` (prior baseline on corrected artifact)
- `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` (QC spec — Prompt Phase sub-dims)
- `Evals/1_Prompt_Eval.md` (Prompt evaluator spec)
- `Reference/Prompt_Format.md` + `Reference/Sessions/AUDIT.md` (LENS 1-8, 6+9 retired v18)

## Eval spec verified
- Prompt Eval 2.8 (universe-level date alignment): pipeline non-FAIL because per-task universe seeds data windows for all relative-date phrases; trajectory-level solvability deferred to S4.
- Prompt Eval 1.3 anti-pattern binary mapping: Command-List = ❌, Bolt-on candidates = 3 (all confirmed load-bearing via remove-sentence), Pre-Solving = ❌, Tool Mention = 0.
- Prompt Eval 4.1 sub-dim scoring: all mapped to 5/5.

## QC spec re-verified
- Coherence: 5/5 (3 bolt-on WARN sentences confirmed load-bearing).
- Explicit tool mention: 5/5 (0 tokens).
- Universe alignment: 5/5 (13 atoms all trace).
- Persona voice: 5/5 (matches Sofia processor voice).
- Multi-step / density hint: 5/5 (216.8 measured).
- Unique ground truth: 5/5 (each claim maps to single deterministic atom).
- Discoverability: 5/5 (cross-service required).

## All 9 lenses status
| Lens | Status | Note |
|---|---|---|
| 1 Strict QC scoring + per-atom evidence | PASS | 13-atom table in AUDIT_prompt.md |
| 2 Answer-leakage sweep | PASS | 0 leakage of any derived figure/name/date |
| 3 Hardness end-to-end trace | PASS | All 8 levers anchored |
| 4 Density projection | PASS | 216.8 avg (4× strict bar) |
| 5 Adversarial veteran review | PASS | No method-lock / persona-drift / tool-leak / em-dash / "at least N" in prompt |
| 6 RETIRED v18 | — | Merged into LENS 1 per-atom table |
| 7 Anti-rationalization | PASS | 3 potential rationalizations re-examined; all confirmed valid |
| 8 Regression anchors | PASS | 48/48 |
| 9 RETIRED v18 | — | Merged into LENS 1 unique-ground-truth + LENS 5 adversarial |

## Verification statements
- **Statement 1:** All 13 prompt atoms directly re-verified against `_aux/Universe_Split/*.json` (not narrative-dismissed from prior audit).
- **Statement 2:** Marcus Webb landmine directly queried against `mortgage_los.staff.json` → `is_active=True, termination_date=None, email=marcus.webb@keystonemortgage.com` — per-task universe swap from base scenario_7da8f37a. Prompt reference to any LO in Sofia's pipeline (which includes Marcus via 2 loans) is not writing to a departed employee.
- **Statement 3:** 3 bolt-on WARN sentences confirmed load-bearing by mechanical remove-sentence test — each removal loses a lever anchor (terminated-LO / Camille summary / compliance escalation).
- **Statement 4:** Aggregate tool availability (compliance_alerts / get_pipeline) does NOT collapse hardness — measured 216.8 avg tool calls and 33.3% pass@1 across 6 runs.
- **Statement 5:** Zero em-dashes, zero "at least N", zero tool tokens, zero internal IDs in prompt.

## Discrepancies surfaced
None. Prior audit verdict PASS (STRICT) re-derived independently and holds.
