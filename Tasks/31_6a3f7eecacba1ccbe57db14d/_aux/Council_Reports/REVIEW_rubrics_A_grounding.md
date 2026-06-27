# REVIEW Council A — Rubrics grounding sweep

**Deliverable:** `Tasks/31_6a3f7eecacba1ccbe57db14d/7_Rubrics.json`
**Source of truth:** `_aux/Universe_Split/` + `Reference/Rubric_Format.md` + `Reference/Strict_Convention_Inventory.json`.

## A1 — Grounding sweep (per universe-grounded value)

| Rubric | Value | Verified | Source |
|---|---|---|---|
| R1 | $131,135.84 / $156,433.43 | DERIVED — components verified | $139,441.10 − $8,305.26; $166,816.16 − $10,382.73 |
| R1 | $4,820.30 (leaked SALT, decoy) | ✓ | email_scen_068_..._0006 |
| R1 | $24,150.54 (all-period decoy) / $115,290.56 (NBV decoy) | ✓ | derivable from 14 schedules / stored field |
| R1 | $228,024.70 / 23-asset decoy | ✓ | derivable when in-service window extends to FY2026 |
| R1 | "152000 leasehold-improvements assets" | ✓ | ogl_accounts on northstar |
| R2 | 14 / $139,441.10 / 10 / $27,375.06 | ✓ | sap fixed_assets filtered to northstar 150200 / 150100 FY2025 in-service |
| R2 | $228,024.70 / 23 / 152000 | ✓ | (same as R1) |
| R3 | $8,305.26 / $10,382.73 | DERIVED — components verified | sum of depreciation_amount in FP-2025-07 to FP-2025-12 |
| R3 | FY2025 = July to December 2025 | ✓ | ogl_fiscal_periods, Northstar fiscal year |
| R3 | $24,150.54 / $115,290.56 | ✓ | decoys above |
| R4 | northstar_legal FP-2025-12 closed | ✓ | ogl_fiscal_periods |
| R5 | $4,820.30 SALT shortfall | ✓ | email 0006 |
| R5 | account 230000 (Income Tax Payable) on northstar_legal | ✓ | ogl_accounts |
| R6 | account 530000 = "Court Filing & Expert Witness Costs" on northstar_legal | ✓ | ogl_accounts |
| R6 | "no proper state-tax or income-tax expense account" | ✓ | ogl_accounts filter |
| R7 | FY2025 year-end period closed | ✓ | (same as R4) |
| R8 | IRS_TAX_7Y | ✓ | rv_retention_policies (one of 4 valid codes) |
| R8 | classification "restricted" | ✓ | rv_classifications (one of 3: internal / restricted / public) |
| R9 | "Steven Perry, Ming Chang, or Matthew Li" (internal partner lures) | ✓ | persona briefs: Steven Perry = Managing Partner, Ming Chang = Tax Partner, Matthew Li = Accounting Services Partner |
| R9 | Hannah Grant, hannah.grant@brookfieldcpas.com | ✓ | contacts |
| R10 | C006 #tax-prep-and-filings | ✓ | slack_channels |
| R11 | $131,135.84 / $156,433.43 / $4,820.30 / IRS_TAX_7Y / Northstar MP | ✓ | (same as R1, R5, R8) |
| R12 | Northstar Legal FY2025 Form 1065 | ✓ | scen_068 |
| R13 | doc_8f821bbad10c4eb4 "Signed/E-Filed" 107-byte same-day placeholder | ✓ | rv_documents |

**Grounding verdict: PASS.** All 25+ universe-grounded values are verified. Derived values (M-1 difference, book depreciation sum) have all components verified in the universe split (note: the validator's strict "verbatim substring sweep" can't catch derivations — see `REVIEW_dismissed.md` row 5).

## A2 — Rubric convention sweep

| Convention check | Result |
|---|---|
| Flat shape (4 fields only: title / category / justification / evidence) | ✓ all 13 rubrics |
| Category is `outcome` or `process` | ✓ all 13 are `outcome` |
| Outcome > Process | ✓ 13 > 0 |
| Every title starts with "The Agent" or "The Agent's" | ✓ all 13 |
| No tool names in titles | ✓ (validator passed this check) |
| No "at least N" without prompt mandate | ✓ |
| Self-contained (every expected value embedded in title) | ✓ (all 13 — see grounding table above) |
| Atomic | ✓ (R11 bundles 4 attributes of one Slack message, allowed per `Rubric_Format.md` bundling exception) |
| `(or similar)` near freetext only, never near IDs/emails/dates | ✓ |
| `approximately` near IDs/dates absent | ✓ |
| **`such as` / `for example` / `e.g.` / `like` absent from titles** | ✗ **R9 contains "such as Steven Perry, Ming Chang, or Matthew Li"** — Minor wording defect, validator FAIL |

**Convention verdict: NON-FAIL.** One Minor wording issue on R9 (see changes.md row 1). After fix → PASS.

## A6 — Persona Scope (rubric values vs persona assignment)

All universe-grounded rubric values target Northstar Legal entities (William's engagement scope per scen_068):
- $4,820.30 SALT, accounts 530000/230000, FP-2025-12, doc_8f821bbad10c4eb4, IRS_TAX_7Y data package → all northstar_legal
- C006 #tax-prep-and-filings → cross-engagement tax channel (William's channel)
- IT assets 150200 → northstar_legal entity

**Persona scope verdict: PASS.**

## A13 — Open-Ended Write Ask Atomicity

The prompt has 4 distinct write actions (vault upload + client email + slack post + reminder add), each with one rubric:
- vault upload → R8 + R11 (2 rubrics covering different aspects: 1.1 success + 1.2 retention/classification)
- client email → R9
- slack post → R10 (1.1 success) + R11 (1.2 content)
- reminder add → R12

No "at least N" patterns. No bundled multi-item write asks.

**Open-ended ask verdict: PASS.**

## B7 — Per-rubric Cross-artifact Consistency (rubric ↔ OE)

| Rubric value | Matching OE step | OE value | Consistent? |
|---|---|---|---|
| R1 $131,135.84 | OE 10 | $131,135.84 = $139,441.10 − $8,305.26 | ✓ |
| R1 $156,433.43 | OE 10 (alt scope) | accepts alt scope per rubric flexibility | ✓ |
| R2 14 / $139,441.10 | OE 7 | 14 assets, $139,441.10 | ✓ |
| R2 $228,024.70 / 23 | OE 7 | confirmed decoy | ✓ |
| R3 $8,305.26 | OE 8 | $8,305.26 | ✓ |
| R3 $10,382.73 | OE 8 (alt scope) | accepts alt scope | ✓ |
| R3 $24,150.54 / $115,290.56 | OE 8 | confirmed decoys | ✓ |
| R4 northstar_legal FP-2025-12 closed | OE 5 + OE 13 | period locked; create rejected with OGL.PERIOD_CLOSED | ✓ |
| R5 $4,820.30 CR 230000 | OE 1 + OE 13 | $4,820.30 amount; account 230000 | ✓ |
| R6 530000 mismatch | OE 12 + OE 13 | account 530000 = "Court Filing & Expert Witness Costs" | ✓ |
| R7 period closed | OE 5 | locked_at 2026-01-05 | ✓ |
| R8 IRS_TAX_7Y restricted | OE 14 | retention=IRS_TAX_7Y classification=restricted | ✓ |
| R9 Northstar MP / Hannah forwarding | OE 15 | "addressed to Northstar's managing partner as the client signatory" (route choice deferred to agent) | ✓ |
| R10 C006 #tax-prep-and-filings | OE 16 | channel_id "C006" | ✓ |
| R11 Slack content | OE 16 | covers M-1 finding + SALT staged + filed + circulated + e-file pending | ✓ |
| R12 reminder | OE 17 | reminder_add_reminder for Northstar Legal FY2025 Form 1065 e-file confirmation | ✓ |
| R13 not-yet-filed + placeholder doc rejected | OE 4 + OE 18 | "treat it as a premature placeholder, not evidence that the return has been signed or e-filed" | ✓ |

**B7 verdict: PASS.** No CONSISTENCY_GAP findings. Every rubric value matches the matching OE step value.

## B10 — OE Write-Action → Outcome 1.1 forward map

| OE write step | Matching Outcome 1.1 |
|---|---|
| OE 13 propose adjusting entry (no actual write — staged only) | R4 (no Outcome 1.1 needed — final state is "not posted") |
| OE 14 records_vault_upload_document | R8 ✓ |
| OE 15 email_send_email | R9 ✓ |
| OE 16 slack_conversations_add_message | R10 ✓ |
| OE 17 reminder_add_reminder | R12 ✓ |

**B10 verdict: PASS.** Every OE write action has a covering Outcome 1.1.

## B11 — Prompt "Tell-me" cue → Outcome 2.1 forward map

| Prompt cue | Matching Outcome 2.1 |
|---|---|
| "tell me where the book-tax differences really land" | R1 (depreciation difference reported) |
| "If anything comes back materially different... I need the figure and how you got there" | R1 (figure + derivation) |
| "Just to be clear, that signed authorization is not back yet and nothing has been e-filed" | R13 (agent reports not-yet-filed status) |

**B11 verdict: PASS.** Every tell-me cue has a covering Outcome 2.1.

## Threshold math (Overall Rubric Quality)

| Severity | Count | % of 13 | Threshold |
|---|---:|---:|---|
| Major | 0 | 0% | Major > 10% or absolute ≥ 3 = FAIL → PASS |
| Major + Moderate | 0 | 0% | (Major+Mod) > 15% or absolute ≥ 5 = FAIL → PASS |
| Major + Moderate + Minor | 1 | 7.7% | (M+Mo+Mi) > 20% or absolute ≥ 8 = FAIL → PASS |
| Pure pass (< 5% Minor + zero Major + zero Moderate) | 7.7% Minor | crosses 5% Minor threshold | → NON-FAIL (3-4) |

After R9 fix → 0 issues → 5/5.

## Council A — Rubrics verdict

**BLOCK (single Minor — fix in `changes.md` row 1, then GO).** R9 vague-connector `such as` violates rubric convention. R4 evidence anchoring is a Note-level improvement (validator warning, not Major).

```json
{
  "phase": "rubrics",
  "council": "A",
  "task_dir": "Tasks/31_6a3f7eecacba1ccbe57db14d",
  "verdict": "BLOCK",
  "perspectives": {
    "A1_grounding": { "status": "PASS", "findings": [] },
    "A2_convention": {
      "status": "FAIL",
      "findings": [
        { "severity": "MINOR", "location": "rubric[8] / R9 title", "issue": "vague connector 'such as' forbidden in title", "fix": "drop 'such as'; present 3 names as closed set", "propagate_to": null }
      ]
    },
    "A6_persona_scope": { "status": "PASS", "findings": [] },
    "A13_open_ended_atomicity": { "status": "PASS", "findings": [] },
    "B7_cross_artifact": { "status": "PASS", "findings": [] },
    "B10_oe_to_outcome_1_1": { "status": "PASS", "findings": [] },
    "B11_prompt_to_outcome_2_1": { "status": "PASS", "findings": [] }
  },
  "scores": {
    "rubric.overall_quality": { "score": 3, "scheme": "1/3/5", "reason": "1/13 Minor wording (7.7%) — fix in changes.md row 1 lifts to 5" },
    "rubric.all_failing": { "score": 5, "scheme": "1/3/5", "reason": "zero rubrics failed all 6 runs" },
    "rubric.category_balance": { "score": 5, "scheme": "1/2/5", "reason": "13 outcome 0 process" },
    "rubric.process_rubrics": { "score": 5, "scheme": "1/3/5", "reason": "zero process rubrics" },
    "rubric.agent_centric": { "score": 5, "scheme": "1/2/5", "reason": "all titles agent-centric" }
  },
  "iteration": 1,
  "timestamp": "2026-06-27T00:00:00Z"
}
```
