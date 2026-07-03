# Dismissed findings — Task 37

Findings raised by validators or first-pass council instinct that were investigated but NOT written into `changes.md` because universe re-check invalidated them.

## Prompt bolt-on WARNs (3) — DISMISSED

### Sentence A: "Check what's been going on with each of these loans, look at any recent email threads or Slack discussions about them, and figure out exactly what's blocking progress on each one."
- **Validator claim:** shares no named entities with the rest of the prompt.
- **Re-check:** the sentence introduces the investigation lever (recent emails + Slack discussions), which is a core discovery path used in every trajectory (avg 216.8 tool calls includes heavy email/Slack search). Removing the sentence would eliminate the primary hardness lever for per-loan blocker discovery.
- **Verdict:** false-positive. Coherent, load-bearing. DISMISS.

### Sentence B: "Reach out to Carlos, Derek, Keisha, and any other LO with active files in my queue..."
- **Validator claim:** shares no named entities with the rest of the prompt.
- **Re-check:** the sentence names 3 LOs by first name AND introduces the "every LO who has a borrower in my pipeline needs an update" mandate — directly drives 8+ rubrics (rubric [0]-[15] all trace here).
- **Verdict:** false-positive. Core deliverable-defining sentence. DISMISS.

### Sentence C: "If anything you find looks like it could be a compliance concern, flag it separately for Elena and Denise with specifics."
- **Validator claim:** shares no named entities with the rest of the prompt.
- **Re-check:** Elena and Denise appear only here — but the sentence introduces the conditional compliance-escalation lever tied to phishing/TRID/terminated-LO scenarios that surface during investigation. Removing it removes a discoverable hardness lever documented in Slack C004.
- **Verdict:** false-positive. DISMISS. (Elena attribution question retained as separate Minor — see changes.md row 2.)

## Rubric Jaccard similarity WARNs (12 pairs) — DISMISSED

Validator flagged 12 rubric pairs at 71% Jaccard: rubric[0]/[2]/[10]/[14] cluster (LO notification titles) and rubric[4]/[6]/[8]/[12] cluster (LO content titles).

- **Re-check:** each pair targets a different LO recipient email (Carlos / Derek / James / Marcus for the [0]/[2]/[10]/[14] cluster; Amy / Natasha / Priya-per-loan-set for the [4]/[6]/[8]/[12] cluster). Removing any one drops coverage of that LO.
- **Verdict:** false-positive from purely lexical Jaccard analysis. Semantically distinct. DISMISS all 12.

## Rubrics-level FAIL on 27% Moderate+ threshold — DISMISSED

The 2 validator FAILs (27% Moderate+ + 27% any-severity thresholds breached) are ENTIRELY driven by the 8 rubrics implicated in the 12 Jaccard WARNs. Since the Jaccard WARNs are false positives, the aggregate quality metric is also invalidated.

- **Verdict:** cascading false-positive. DISMISS the validator FAIL banner. Actual quality: 30 clean rubrics + 1 Moderate coverage gap (rubric [3]) + 1 Minor attribution note (rubric [24]). ~93% clean by hand-audit.

## Rubrics missing "email" write-verb WARN — DISMISSED

- **Validator claim:** prompt uses write-verb "email" but no rubric title contains "email".
- **Re-check:** prompt does NOT use the verb "email" — it uses "reach out", "give each of them", "make sure Camille gets", "post a heads up". Rubric titles correctly use method-agnostic verbs ("notifies", "provides", "posts") per Rubric_Format.md Section 4.
- **Verdict:** validator token-extraction bug (likely misreading "send email" in OE bodies). false-positive. DISMISS.

## OE 10 CRM/loans service-mismatch WARN — DISMISSED

- **Validator claim:** OE 10 references `loans` but tool call targets `crm` service (expected `mortgage_los`).
- **Re-check:** OE 10 explicitly uses `crm_search_deals` with `dealname` = loan numbers. `crm.crm_deals.json` DOES contain deal records keyed by loan number as dealname. This is a legitimate cross-system linkage query for retrieving CRM engagement history tied to a loan.
- **Verdict:** false-positive. DISMISS.

## Prompt word count 343 note

- Note-level observation: "word count 343 is over 300 — within sweet spot but could still be tightened."
- Not a defect. No change required.

---

Total dismissed: 17 low-quality signals (3 bolt-on WARN + 12 Jaccard WARN + 1 missing-verb WARN + 1 OE service WARN + 2 rubrics-level FAILs cascading). All confirmed false-positive via universe or rubric hand-audit.
