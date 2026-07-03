# REVIEW hardness — Task 37

**Source:** measured (6/6 trajectories completed, parsed via `parse_trajectories.py`)

## Density (tool-call budget)

| Run | Total | MCP-only | Verdict |
|---|---|---|---|
| 1 | 89  | 71  | ok |
| 2 | 85  | 69  | ok |
| 3 | 338 | 307 | ok |
| 4 | 256 | 233 | ok |
| 5 | 226 | 206 | ok |
| 6 | 307 | 282 | ok |

- **Avg total tool calls: 216.8** (design target ≥ 50, absolute floor 40 — WELL ABOVE)
- **Avg MCP tool calls: 194.7**
- Density verdict: **PASS** (comfortably above 50+ design target)

## Difficulty (pass@1)

| Run | Passed / Total | Status |
|---|---|---|
| 1 | 28/30 | FAIL |
| 2 | 30/30 | PASS |
| 3 | 28/30 | FAIL |
| 4 | 30/30 | PASS |
| 5 | 28/30 | FAIL |
| 6 | 28/30 | FAIL |

- **pass@1 = 2/6 = 33.3%** (threshold ≤ 40% — PASS but tight, 6.7 percentage points below cap)
- 4 of 6 runs failed exactly 2 rubrics — the same 2 in Run #1 (verified via 8_Verifier_Fails.txt) and by inspection the same pattern in Runs 3/5/6
- Failure locus is narrow: both fails are the "final-response must explicitly name loan number X AND state N outstanding docs" rubrics (LN-2026-00623 with 5 docs; LN-2026-00010 with 7 docs) — legitimate Bucket 3 model failures (summary drift: agents put details in emails, then over-abstract the final response)

## Answer leakage (FINAL Truthfulness lens)

- Prompt does NOT reveal:
  - The count "26 active loans"
  - Specific loan numbers (LN-2026-00XXX)
  - Borrower names
  - Terminated LO names (Veronica Hayes, Brian Mitchell)
  - Lender names
  - Rate lock expiration dates
  - Outstanding condition/doc counts
- All hardness levers must be discovered via tool use. **PASS — no leakage.**

## Lever coverage (Council B-B4 lens)

Confirmed hardness levers, all present and load-bearing:
1. **26 active loans** — must be discovered from pipeline query, then enumerated
2. **All 26 rate locks expired** — must be identified per-loan; universe-wide expiration is a single-atom finding
3. **5 loans on 2 terminated LOs** (Veronica Hayes ×4, Brian Mitchell ×1) — LOS `is_active=false` + `termination_date` fields must be checked against `assigned_lo`
4. **26 outstanding documents across 8 loans** — per-loan document checklist inspection needed
5. **Phishing/portal-compromise scope** — Slack channel C004 messages tie LN-2026-00522/00008/00010/00009 to Keisha's UWM portal compromise
6. **TRID redisclosure trap on LN-2026-00613** — Slack C002 messages show 30yr→15yr borrower term switch without revised LE issuance
7. **LN-2026-00623 anomaly** — status=clear_to_close with 5 outstanding required documents (a processing-gap smell)
8. **LN-2026-00010 mechanic's lien** — old lien on Ferguson property blocking title (adjacent to compromise scope)

Every lever surfaced in the failing trajectories, confirming the levers ARE probeable and load-bearing.

## Final verdict

- Density: **PASS** (216.8 avg vs 40 floor / 50 design)
- Difficulty: **PASS** (pass@1 33.3% vs 40% cap)
- Answer leakage: **PASS**
- Lever coverage: **PASS**

**Hardness is genuine — no REBUILD trigger from hardness axis.**
