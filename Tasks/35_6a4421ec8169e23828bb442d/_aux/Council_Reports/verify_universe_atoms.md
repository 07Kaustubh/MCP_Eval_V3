# Universe Atom Verification Report

**Atoms checked:** 20
**FAIL:** 0
**WARN:** 4

## WARN
- LOS-vs-CRM source-of-truth: `/14 Marcus Webb post-termination-access CRM stream identifie...` | POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state.
- LOS-vs-CRM source-of-truth: ` no payment was authorized.
The Agent's CRM engagement NOTE ...` | POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state.
- LOS-vs-CRM source-of-truth: `ord for any later reviewer.
The Agent's CRM engagement NOTE ...` | POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state.
- LOS-vs-CRM source-of-truth: `nd LN-2025-00229.
Check the body of the CRM engagement NOTE ...` | POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state.

## Per-atom evidence table

| Atom | Query | Row | Verdict | Severity |
|---|---|---|---|---|
| LOS-vs-CRM source-of-truth: `/14 Marcus Webb post-termination-access CRM stream identifie...` | `manual: loan-level data must be sourced from mortgage_los, not CRM` | CRM cited as source for loan-level data | POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state. | WARN |
| LOS-vs-CRM source-of-truth: ` no payment was authorized.
The Agent's CRM engagement NOTE ...` | `manual: loan-level data must be sourced from mortgage_los, not CRM` | CRM cited as source for loan-level data | POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state. | WARN |
| LOS-vs-CRM source-of-truth: `ord for any later reviewer.
The Agent's CRM engagement NOTE ...` | `manual: loan-level data must be sourced from mortgage_los, not CRM` | CRM cited as source for loan-level data | POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state. | WARN |
| LOS-vs-CRM source-of-truth: `nd LN-2025-00229.
Check the body of the CRM engagement NOTE ...` | `manual: loan-level data must be sourced from mortgage_los, not CRM` | CRM cited as source for loan-level data | POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state. | WARN |
| loan LN-2026-00008 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| loan LN-2025-00007 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| loan LN-2026-00601 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| loan LN-2026-00522 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| loan LN-2025-00229 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| loan LN-2026-00010 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| loan LN-2025-00002 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| loan LN-2026-00009 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email megan.sloane@wardbarrettlaw.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email raj.anand@keystonemortgage.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email lauren.bennett@icloud.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email robert.calloway@keystonemortgage.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email lbennett@bennettfairlendinglaw.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email lbennett@bennettcyberlaw.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email laura.bennett@bennettethicslaw.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email laura.bennett@bennettstokeslaw.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |