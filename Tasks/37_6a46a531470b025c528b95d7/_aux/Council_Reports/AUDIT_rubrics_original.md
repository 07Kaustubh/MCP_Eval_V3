# AUDIT rubrics (STRICTEST interpretation) — Task 37 ORIGINAL

**Scope:** Candidate's `7_Rubrics.json` (30 rubrics, 30 Outcome, 0 Process) — every rubric title read atomically, every evidence field checked against universe, no charity given.

## Programmatic floor
- `validate.py --phase rubrics`: **FAIL** (2 fails, 13 warns, 4 notes)
  - Fails: 27% Moderate+ and 27% any-severity. Both driven ENTIRELY by Jaccard similarity between LO-notification rubric pairs (structural similarity, not semantic redundancy).
  - Warns: 12 Jaccard 71% pairs + 1 missing "email" write-verb rubric title.

Below: strictest re-evaluation of every WARN + hand-audit of every rubric.

## Strict lens checks

### 1. Jaccard similarity 71% (12 pairs) — false-positive audit
Pairs flagged: rubric[0]/[2]/[10]/[14] cluster (LO notification titles) and rubric[4]/[6]/[8]/[12] cluster (LO content titles).

Semantic distinctness check:
- Rubric [0]: "notifies Carlos Rivera (carlos.rivera@…)"
- Rubric [2]: "notifies Derek Moss (derek.moss@…)"
- Rubric [10]: "notifies James Thornton (james.thornton@…)"
- Rubric [14]: "notifies Marcus Webb (marcus.webb@…)"

Each rubric targets a DIFFERENT recipient email address. Removing any one drops coverage of that LO. **These are legitimately non-redundant** — the Jaccard is structural (shared shell "notifies X with an update on his/her borrowers' loans"), not semantic.

- **Verdict: false-positive. PASS strict.**

### 2. Missing "email" write-verb Outcome rubric
- Validator: prompt uses write-verb "email" but no rubric title contains "email".
- Ground truth: prompt does NOT say "email". It says "reach out to Carlos, Derek, Keisha…", "give each of them a clear summary", "make sure Camille gets a full lock status summary", "post a heads up in the processing channel". No "email" verb.
- The rubric authors correctly used method-agnostic "notifies" / "provides" language per Rubric_Format.md Section 4 (method-agnostic when prompt is method-agnostic).
- **Verdict: false-positive. PASS strict.**

### 3. Outcome-Process ratio
- 30 Outcome, 0 Process. Rule 8 (Outcome outnumbers Process) satisfied.
- Three-condition test for Process rubrics: no discoverable Process behavior surfaces during trajectory review. No propagation flag needed.
- **Verdict: PASS strict.**

### 4. "At least N" rule (rule 6)
Rubric titles containing "at least":
- Rubric [22]: "adds an activity note to at least one loan" — prompt mandate: "add activity notes to any loan in the system that needs updating" (plural implied but not enumerated). "At least one" is a defensible minimum. Marginal but acceptable.
- Rubric [23]: "creates at least one CRM engagement" — prompt: "log everything in the CRM" (not enumerated). "At least one" acceptable.
- Rubric [24]: "flags at least one compliance concern" — prompt: "If anything you find looks like it could be a compliance concern" (conditional). "At least one" is the natural minimum given conditional discovery. Acceptable.

- **Verdict: PASS strict — all 3 "at least" uses are minimum-bar rubrics where the prompt does not enumerate a specific count.**

### 5. Tool names in titles
- Zero rubric titles contain tool names. Compliant with rule 7.
- Evidence fields do mention tool patterns (e.g., "email_id was returned") — allowed per rule 7.
- **Verdict: PASS strict.**

### 6. Atomicity (rubric-by-rubric hand audit)

Walked all 30 rubrics for AND-bundling and multi-atom collapse.

- Rubrics [0]/[2]/[4]/[6]/[8]/[10]/[12]/[14] — "notifies LO X" — pure single-atom send events. ✅
- Rubrics [1]/[5]/[7]/[9]/[11]/[13]/[15] — "content includes A, B, C for LO X's loans" — bundled per-LO content check. Justifications state "the loan details come from the same communication and would pass or fail together." Legitimate bundle when atoms co-exit in one message.
- Rubric [3] Derek content — flags below (**coverage gap**).
- Rubric [16] Camille — "notifies Camille Foster with lock status summary" — atomic.
- Rubric [17] Camille content — "lock expiration dates for Sofia's active loans, noting all 26 locks expired" — bundled but single-message atom.
- Rubric [18] Grace — "provides Grace pipeline status report" — atomic.
- Rubric [19] Grace content structure — "broken down by loan status, assigned LO, blocker/next step" — bundled content shape.
- Rubric [20] Grace terminated LOs — hardcodes Veronica ×4 + Brian ×1 with dates. Bundled but content-of-one-report is atomic.
- Rubric [21] Slack C002 post — atomic.
- Rubrics [22]/[23] — activity note + CRM engagement — atomic minimum-bar.
- Rubric [24] compliance — "flags concern to BOTH Elena AND Denise". The AND is method-lock on recipients, not atomicity failure — see #7 below.
- Rubrics [25]/[26]/[27]/[28]/[29] — final response detail claims — atomic single-fact statements.

- **Verdict: PASS strict** for atomicity except for one coverage gap (below).

### 7. Coverage gap — Rubric [3] Derek Moss content (MODERATE)
- Rubric [3] title: "Agent's update to Derek Moss includes LN-2026-00008 (conditional approval, $276,400, rate lock expired 2026-03-11, 2 outstanding conditions and 2 required documents)."
- Derek's active pipeline has **3 loans**: LN-2026-00008, LN-2026-00196, LN-2026-00632.
- Rubric [3] checks ONLY LN-2026-00008. Asymmetric with:
  - Rubric [5] Keisha — all 4 loans
  - Rubric [7] Amy — both 2 loans
  - Rubric [9] Natasha — both 2 loans
  - Rubric [11] James — all 3 loans
  - Rubric [13] Priya — all 3 loans
  - Rubric [15] Marcus — both 2 loans
- Justification defends the narrower scope ("the most complex of Derek's loans, the only active loan in Sofia's pipeline with outstanding LOS conditions plus 2 required documents"). Defensible narrowing, but asymmetric strictness across LO cohorts.
- **Severity: Moderate.** Under STRICTEST interpretation, an agent could pass rubric [3] by mentioning only LN-2026-00008 while ignoring LN-2026-00196 (1 required doc: w2_current) and LN-2026-00632 (underwriting, $268,000, lock expired 2026-04-04). Fix path: extend rubric [3] to check all 3, OR split into rubrics [3a]/[3b] for the two omitted loans. Recommend extension.
- **Verdict: 1 Moderate finding — flag to changes.md.**

### 8. Method-lock check
- Rubric [21] Slack channel C002 — locked. Prompt says "the processing channel" — natural language for #loan-processing. Acceptable method-lock (matches prompt intent).
- Rubric [24] compliance email to BOTH Elena AND Denise — locked. Prompt says "flag it separately for Elena and Denise with specifics" — "AND" is inherent in the prompt. Acceptable method-lock.
- All other write rubrics use method-agnostic verbs ("notifies", "provides", "adds", "creates", "flags").
- **Verdict: PASS strict.**

### 9. Truthfulness (atom-level) — Council A-A1 sweep
Every hardcoded atom in rubric titles verified against universe:
- Rubric [0]/[1]: Carlos Rivera / carlos.rivera@… / LN-2026-00184 processing $340,000 lock 2026-03-23 / LN-2026-00611 processing $214,000 lock 2026-04-10, 1 required doc (drivers_license). All verified. ✅
- Rubric [3]: LN-2026-00008 conditional_approval $276,400 lock 2026-03-11, 2 conditions (bank statements PTD + appraisal PTC) + 2 required docs (appraisal, homeowners_insurance). Verified. ✅
- Rubric [4]/[5]: Keisha Williams 4 loans — LN-2024-00103 lock 2024-09-08 / LN-2025-00330 lock 2025-06-22 / LN-2025-00380 conditional_approval lock 2025-08-30 / LN-2026-00376 lock 2026-03-20, 3 required docs (tax_return_prior, drivers_license, hoi_binder). Verified. ✅
- Rubric [6]/[7] Amy Chen: LN-2024-00123 conditional_approval $267,000 lock 2024-10-07 / LN-2026-00532 underwriting $218,400 lock 2026-03-24. Verified. ✅
- Rubric [8]/[9] Natasha Okafor: LN-2025-00286 clear_to_close $382,800 lock 2025-05-12 / LN-2026-00010 processing $519,200 lock 2026-04-24, 7 required docs. Verified. ✅
- Rubric [10]/[11] James Thornton: LN-2025-00344 conditional_approval $800,000 VA lock 2025-07-05 / LN-2025-00363 processing $196,200 lock 2025-07-29 / LN-2026-00541 application $720,000 FHA lock 2026-04-06. Verified. ✅
- Rubric [12]/[13] Priya Desai: LN-2025-00244 processing $185,300 lock 2025-03-21 / LN-2026-00613 conditional_approval $433,000 lock 2026-04-14 / LN-2026-00623 clear_to_close $467,000 lock 2026-04-01, 5 required docs. Verified. ✅
- Rubric [14]/[15] Marcus Webb: LN-2024-00125 underwriting $246,600 lock 2024-10-17 / LN-2026-00539 conditional_approval $734,000 USDA lock 2026-04-03. Verified. ✅
- Rubric [17] "all 26 locks expired" as of universe today 2026-04-28. Verified (latest expiration is LN-2026-00010 at 2026-04-24). ✅
- Rubric [20] Veronica Hayes (terminated 2025-09-30) × 4 loans + Brian Mitchell (terminated 2025-04-15) × 1 loan (LN-2025-00305). Verified. ✅
- Rubric [24] compliance — phishing scope for LN-2026-00008 + LN-2026-00010 verified via Slack C004. TRID redisclosure on LN-2026-00613 verified via Slack C002 (30yr→15yr, no revised LE). Terminated-LO accountability gap verified. ✅
- Rubric [25] 26 active loans count. Verified. ✅
- Rubric [26] all rate locks expired. Verified. ✅
- Rubric [27] Veronica Hayes departure. Verified. ✅
- Rubric [28] LN-2026-00623 CTC with 5 outstanding required docs (paystub_1, w2_current, w2_prior, tax_return_current, drivers_license). Verified. ✅
- Rubric [29] LN-2026-00010 with 7 required docs (pay_stubs, W2s, tax_returns, credit_report, VOE, appraisal, homeowners_insurance) — "most outstanding docs in the pipeline". Verified as maximum in pipeline. ✅

- **Verdict: 100% atom grounding. PASS strict.**

### 10. Elena Marchetti persona attribution (MINOR)
- Rubric [24] expects the agent to email `elena.marchetti@keystonemortgage.com` (and `denise.holloway@keystonemortgage.com`) with compliance concerns.
- Universe check: Elena Marchetti's LOS role = `processor`, specialization = "Doc collection, lender coordination". She is NOT tagged as compliance officer in LOS staff.
- Denise Holloway: confirmed compliance authority via Slack C004 messages ("initiating formal breach response", "pulled portal-access list", etc.). Denise IS compliance.
- The prompt (candidate-written) directs Sofia to escalate to both Elena AND Denise. This is a persona-attribution question:
  - **Defense:** In a 17-person shop, senior processors can hold informal compliance-adjacent duties. Elena's specialization includes "lender coordination" which touches breach response. Sofia the processor might reasonably escalate to her senior processor peer AND to compliance.
  - **Concern:** No Slack/email evidence attributes compliance authority to Elena. The rubric accepts an agent's email to Elena as satisfying the compliance-escalation criterion, when Elena is not the correct recipient by universe evidence.
- **Severity: Minor.** The prompt permits Sofia's judgment call; the rubric accepts what the prompt directs. Not a REBUILD trigger. Flag to changes.md as a Minor note for candidate rating and MATERIALIZE-time consideration.

### 11. Discovery-fabrication check (Learnings memo L7)
- No rubric fabricates loan IDs or names not present in universe. All IDs discoverable.
- **Verdict: PASS strict.**

## AUDIT verdict — RUBRICS: **PASS (STRICT)** with 1 Moderate + 1 Minor finding for changes.md

- **1 Moderate**: Rubric [3] Derek content coverage gap (LN-00196, LN-00632 uncovered)
- **1 Minor**: Rubric [24] Elena Marchetti attribution question (defensible via processor-hat)

Both findings addressable via targeted rubric edits (extension / clarification) — no REBUILD required.
