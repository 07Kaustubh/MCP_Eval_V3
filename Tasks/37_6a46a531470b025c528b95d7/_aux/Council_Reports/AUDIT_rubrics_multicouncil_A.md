# AUDIT rubrics (STRICTEST — multicouncil A) — Task 37

**Auditor role:** Veteran QC council #3 (rubrics phase), STRICTEST interpretation.
**Artifact under audit:** `15_Updated_Rubrics.json` (corrected materialization — what will ship).
**Regression baseline:** `7_Rubrics.json` (candidate original) + `AUDIT_rubrics.md` + `AUDIT_rubrics_original.md`.
**Universe:** keystone (confirmed via `_aux/Universe.txt`).
**Scope:** 30 rubrics (30 outcome, 0 process). Every atom in the 2 Applied rows independently re-queried against `_aux/Universe_Split/`. Every hardness lever from REVIEW_hardness.md traced end-to-end.

## Programmatic floor (re-checked)

- Rubric count: 30. Category split: 30 outcome / 0 process (Counter confirmed).
- Em-dashes / en-dashes in any rubric field: **0** (checked all 30 across title/justification/evidence).
- Tool names in titles: **0** (checked against mortgage_los_/stripe_/crm_/conversations_/send_email/filesystem_/quickbooks_/contacts_/channels_/search_emails tokens).
- "At least N" in titles: **3** (rubric[22] activity note, rubric[23] CRM engagement, rubric[24] compliance concern). All three prompt-conditional; baseline AUDIT accepted.
- Validator `validate.py --phase rubrics` on `15_Updated_Rubrics.json`: FAIL (2 fails, 13 warns, 4 notes) — **byte-for-byte identical** to the candidate-original FAIL band. The 2 Applied rows changed the substance of rubric[3] title + rubric[24] justification, but neither touched the Jaccard-71% cluster.

## LENS 1 — Per-atom evidence table (STRICTEST truthfulness/accuracy)

Focused on the two Applied rows and the highest-stakes cross-referenced atoms.

### Row #1 (rubric[3] Derek Moss content) — re-verified

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Derek Moss is LO on active loans in Sofia's pipeline | `mortgage_los.staff WHERE name='Derek Moss'` | `id=los_staff_f9aa4c3c2fcb, role=loan_officer, spec='VA, Conventional', active=True, email=derek.moss@…` | ✅ grounded |
| Derek has exactly 3 active loans in Sofia's pipeline | `mortgage_los.loans WHERE assigned_lo=los_staff_f9aa4c3c2fcb AND assigned_processor=los_staff_afc9caafae9d AND status in active_set` | 3 rows: LN-2026-00008, LN-2026-00196, LN-2026-00632 | ✅ grounded (matches AFTER title exactly) |
| LN-2026-00008: conditional_approval, $276,400, lock_exp 2026-03-11, 2 conditions, 2 required docs (appraisal, homeowners_insurance) | loans + conditions + document_checklist_items | Exact match; conditions=2 outstanding (PTD bank statements, PTC appraisal); docs=[appraisal, homeowners_insurance] | ✅ grounded |
| LN-2026-00196: processing, $229,000, lock_exp 2026-03-13, 1 required doc (w2_current) | loans + document_checklist_items | Exact match; docs=[w2_current]; 0 outstanding conditions | ✅ grounded |
| LN-2026-00632: underwriting, $268,000, lock_exp 2026-04-04 | loans | Exact match; docs=[] (0 outstanding); 0 outstanding conditions | ✅ grounded |

Bundled-message pass/fail defensible: all 3 loans go in a single email to Derek per OE 14. Pattern matches Keisha [5] (4/4), Priya [13] (3/3), James [11] (3/3), Amy [7] (2/2), Marcus [15] (2/2), Natasha [9] (2/2) — coverage symmetry restored.

**Row #1 verdict:** PASS (STRICT). Every atom independently verified. Justification correctly frames the bundled pass/fail. Evidence correctly enumerates all 3 loan numbers.

### Row #2 (rubric[24] Elena+Denise compliance attribution) — re-verified

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Denise Holloway is compliance authority | `contacts.contacts WHERE name~'Denise Holloway'` | `job='Compliance Officer -- Keystone Mortgage Partners', description='TRID, RESPA, HMDA, fair lending', is_user=True` | ✅ grounded — **STRONGER than justification claim.** Denise's role is explicitly "Compliance Officer" in contacts data, not merely inferred from Slack activity |
| Denise Slack C004 breach-response initiation | `slack_messages WHERE channel_id='C004' AND user_id='keystone_a989261d4d33'` | ts=1775570820: "initiating formal breach response on the compromised wholesale lender portal login tied to Keisha's account. Do not contact borrowers yet…" | ✅ grounded verbatim |
| Denise C004 portal-access audit tied to Keisha | slack_messages same filter | ts=1775572140: "I pulled the portal-access list against LOS. I have 4 likely impacted borrower files tied to Keisha's lender access window: LN-2026-00522, LN-2026-00008, LN-2026-00010, and LN-2026-00009" | ✅ grounded verbatim; exact loan enumeration matches justification |
| Elena Marchetti = senior processor, spec includes lender coordination | `mortgage_los.staff WHERE name='Elena Marchetti'` | `role='processor', specialization='Doc collection, lender coordination', is_active=True` | ✅ grounded — justification correctly avoids labeling Elena as compliance authority |
| LN-2026-00613 TRID redisclosure (30yr→15yr, no revised LE) | `slack_messages WHERE text LIKE '%LN-2026-00613%'` | 6 matches in C002 including verbatim "borrower wants to switch from 30yr to 15yr", "the LE in file is still the old 30yr one. I don't see a revised LE anywhere", "term change like 30yr to 15yr is a new LE trigger", "assume new 3 biz day wait once corrected disclosure is issued" | ✅ grounded verbatim |
| 5 loans on terminated LOs (Veronica ×4, Brian ×1) | `mortgage_los.loans × staff.is_active=False for Sofia pipeline` | LN-2025-00305 (Brian), LN-2025-00314 / LN-2026-00261 / LN-2026-00625 / LN-2026-00627 (Veronica) — exact count 5 | ✅ grounded |

**Row #2 verdict:** PASS (STRICT). Every claim in the AFTER justification has verbatim universe evidence. Denise's compliance authority is confirmed via BOTH contacts data (job title) AND Slack C004 verbatim (breach-response leadership). Elena is correctly framed as processor (not compliance). Justification is the most atom-dense of any of the 30 rubrics.

## LENS 2 — Answer-leakage sweep on rubric bodies

- Prompt does NOT reveal: the 26 count, any LN-2026-* loan number, borrower names, terminated-LO names, lender names, lock expiration dates, condition/doc counts, phishing-portal scope, TRID redisclosure trap.
- Every rubric-hardcoded atom would need to be discovered by the agent via tool use. All 8 hardness levers require universe traversal.
- **Answer leakage: NONE.** No rubric criterion body is a giveaway.

## LENS 3 — Hardness end-to-end trace (rubric half)

| # | REVIEW_hardness.md lever | Rubric surface | Trace |
|---|---|---|---|
| 1 | 26 active loans | rubric[25] | ✅ count-atom hardcoded, discoverable only via `mortgage_los_get_pipeline` |
| 2 | All 26 rate locks expired | rubric[17], rubric[26] | ✅ universal-quantifier claim, verifiable only via full loan enumeration |
| 3 | 5 loans on terminated LOs | rubric[20], rubric[24] justification, rubric[27] | ✅ requires `staff.is_active` cross-check with `assigned_lo` |
| 4 | 26 outstanding docs across 8 loans | rubric[1], rubric[3], rubric[5], rubric[9], rubric[13], rubric[28], rubric[29] | ✅ per-loan `document_checklist_items` inspection |
| 5 | Phishing/UWM portal compromise scope | rubric[24] justification (LN-2026-00008 + LN-2026-00010 + Slack C004 sibling LNs) | ✅ requires Slack C004 search |
| 6 | TRID redisclosure trap on LN-2026-00613 | rubric[24] justification (30yr→15yr, no revised LE per Slack C002) | ✅ requires Slack C002 search |
| 7 | LN-2026-00623 CTC anomaly (5 docs at clear_to_close) | rubric[13], rubric[28] | ✅ requires per-loan doc query + status cross-reference |
| 8 | LN-2026-00010 max outstanding docs (7) | rubric[9], rubric[29] | ✅ requires pipeline-wide doc-count comparison |

**Every lever traces to at least one rubric surface. No HARDNESS_REGRESSION.**

## LENS 5 — Adversarial veteran review specific to rubrics

- **Three-condition test on the 0 Process rubrics:** No discoverable process behavior surfaces. Prompt is a fan-out of write actions ("reach out", "make sure Camille gets", "pull together", "post", "add", "log", "flag"). All are outcome-testable. No silent process rubric present.
- **Persona-scope errors:** None. Each rubric scoped correctly to Sofia's pipeline. No "$2,650 vs $850" style scope drift.
- **Method-lock hygiene:**
  - rubric[21] locks Slack channel C002 — prompt-mandated ("the processing channel"). Baseline AUDIT accepted; still valid.
  - rubric[24] title requires BOTH Elena AND Denise — prompt-mandated ("flag it separately for Elena and Denise with specifics"). AND is prompt-inherent, not a method-lock error.
  - All other write rubrics use method-agnostic verbs ("notifies", "provides", "adds", "creates", "flags"). Compliant with prompt's method-agnostic language.
- **Unique Ground Truth two-reading test:** Every hardcoded atom (loan number, count, status, amount, expiration date, name) has a single verifiable value in the universe. No Reading A vs Reading B ambiguity.
- **Tool names in titles:** 0 (re-verified programmatically).
- **Em-dashes in titles:** 0 (re-verified across all 30 rubrics, all 3 fields).
- **"At least N" in titles without prompt mandate:** All 3 uses are prompt-conditional or prompt-unenumerated ("add activity notes to any loan", "log everything in the CRM", "If anything you find looks like it could be a compliance concern"). Acceptable.

## LENS 5 (cont.) — Overall Rubric Quality aggregate band

- Validator computes 27% Moderate-or-Major, 27% any-severity. Both driven ENTIRELY by 12 Jaccard-71% pairs across 2 clusters:
  - Cluster A (LO-notify, low-count LOs): rubric[0] Carlos + rubric[2] Derek + rubric[10] James + rubric[14] Marcus.
  - Cluster B (LO-notify, higher-count LOs): rubric[4] Keisha + rubric[6] Amy + rubric[8] Natasha + rubric[12] Priya.
- The 12 pairs correspond to 4C2 + 4C2 = 12. Each rubric in a cluster shares the skeleton "notifies X with an update on his/her borrowers' loans in Sofia's pipeline" but targets a **different recipient email address** (semantically distinct — removing any drops LO coverage).
- Under AGENTS.md's documented pipeline-deviations table: "Rubrics Eval Phase 4.2 threshold math allows dilution. Pipeline adds absolute-count gates (Major ≥ 3 = FAIL)". Corrected materialization has **0 Major**, so the pipeline's own strictest absolute-count reading = PASS.
- Under the audit prompt's LENS 5 "aggregate quality band < 15%" criterion + LENS 7 anti-rationalization: the 27% band did NOT drop, and I must NOT explain it away without evidence of a distribution drop.

**This creates a genuine interpretive conflict between two operator-adopted strictness readings.** I resolve as follows (see LENS 7 section below).

## LENS 7 — Anti-Rationalization on the persistent 27% band

Honest self-report: **I did consider whether the 27% band is a "false positive" that can be explained away.** Per LENS 7 explicit instruction, I promote that consideration to a finding rather than absorb it silently.

- The 2 Applied changes.md rows fixed 2 substantive findings (Derek coverage symmetry Moderate + Elena attribution grounding Minor) documented in AUDIT_rubrics_original.md.
- Neither Applied row touched the Jaccard-71% cluster.
- The 27% aggregate persists byte-for-byte from candidate original.
- Prior councils (AUDIT_rubrics_original.md, AUDIT_rubrics.md) ruled the Jaccard band a structural false-positive on grounds of recipient-email distinctness.
- **Under the STRICTEST reading of THIS audit's LENS 7:** the fact that "distinct recipient emails" is a defensible substantive rationale does not by itself flip the aggregate FAIL to PASS. The audit prompt's PASS criterion is literal: "aggregate quality band < 15%". That criterion is NOT met.

## VERDICT

**REVISE**

The corrected materialization is SUBSTANTIVELY high-quality: 0 Major, 100% atom-grounded, every hardness lever traces, 2 Applied rows correctly landed. But the audit prompt's LENS 7 explicit rule ("do NOT explain it away… unless the per-rubric severity distribution actually dropped below 15%") forbids issuing PASS (STRICT) on the current artifact.

The Applied rows fixed the 2 substantive findings the ORIGINAL AUDIT surfaced. They did NOT close the aggregate-band gap because that gap was not on their scope. That gap needs its own changes.md row before the audit can flip to PASS (STRICT).

## Findings

- **[BLOCKER] Overall Rubric Quality aggregate band unchanged at 27% Moderate-or-Major / 27% any-severity.** — `15_Updated_Rubrics.json`:rubrics[0,2,4,6,8,10,12,14] (2 Jaccard-71% clusters of 4 rubrics each). — **Fix:** rewrite the 8 LO-notification titles to introduce ≥15% unique lexical variation per LO so pairwise Jaccard drops below the 71% band. Suggested pattern per LO: include the loan-count anchor ("2 processing loans" / "3 mixed-status loans" / "4 long-expired loans" / etc.) and a per-LO status keyword (application / processing / underwriting / conditional / clear_to_close). Preserves recipient distinctness AND breaks the shared skeleton. Alternative fix: propagate operator sign-off invoking the pipeline-deviations table's absolute-count-gate reading (Major ≥ 3 = FAIL; corrected has 0 Major → PASS), documented as a per-task deviation acceptance.

- **[MAJOR] LENS 7 anti-rationalization escalation vs prior councils.** — `_aux/Council_Reports/AUDIT_rubrics.md` (prior PASS STRICT verdict on same artifact). — **Fix:** Reconcile with the multicouncil verdict. If operator accepts absolute-count-gate reading, add explicit changes.md row (see BLOCKER alt fix) so the deviation is recorded, not hand-waved.

- **[MINOR] rubric[24] title contains "at least one" — prompt-conditional ("If anything you find") and defensible.** — `15_Updated_Rubrics.json`:rubric[24] title. — **Fix:** none required (baseline AUDIT accepted). Noted for transparency.

- **[NOTE] rubric[24] Elena-Denise attribution grounding is now the strongest of any rubric.** — `15_Updated_Rubrics.json`:rubric[24] justification. — Denise's compliance-officer role is confirmed via BOTH `contacts.contacts.json` (job title "Compliance Officer -- Keystone Mortgage Partners", description "TRID, RESPA, HMDA, fair lending") AND `slack_messages` C004 verbatim (breach-response initiation, portal-access audit) — even stronger than the AUDIT_rubrics.md characterization. Row #2 landed cleanly.

- **[NOTE] Row #1 Derek Moss coverage-symmetry fix confirmed at atom level.** — `15_Updated_Rubrics.json`:rubric[3] title. — All 3 loans present with exact status / amount / lock-expiration / doc atoms matching `mortgage_los.loans` + `document_checklist_items` verbatim.

## Recommended changes.md rows to add

| # | Phase | Dimension | Severity | Before | After (proposed) | Why | Status |
|---|---|---|---|---|---|---|---|
| 3 | Rubrics | Overall Rubric Quality — Jaccard cluster | Moderate (structural) | rubric[0,2,10,14] and rubric[4,6,8,12] share skeleton "notifies X with an update on his/her borrowers' loans in Sofia's pipeline" → 12 pairs at Jaccard 71%, drives aggregate to 27% Moderate-or-Major (validator cap 15%) | Rewrite each title to embed loan-count + primary-status anchor per LO. Example: rubric[0] Carlos → "notifies Carlos Rivera about the state of his 2 processing loans in Sofia's pipeline"; rubric[2] Derek → "notifies Derek Moss about his 3 mixed-status loans (conditional, processing, underwriting) in Sofia's pipeline"; rubric[4] Keisha → "notifies Keisha Williams about her 4 long-expired-lock loans in Sofia's pipeline"; rubric[6] Amy → "notifies Amy Chen about her 2 loans (conditional and underwriting) in Sofia's pipeline"; rubric[8] Natasha → "notifies Natasha Okafor about her 2 loans (clear-to-close and heaviest-doc-load) in Sofia's pipeline"; rubric[10] James → "notifies James Thornton about his 3 loans (VA, conventional, and FHA)"; rubric[12] Priya → "notifies Priya Desai about her 3 loans (processing, conditional, and CTC-anomaly)"; rubric[14] Marcus → "notifies Marcus Webb about his 2 loans (underwriting and USDA-conditional)". | Preserves semantic distinctness AND breaks lexical Jaccard band. Drops aggregate below 15% by structural mechanism. |Proposed |
| 3-ALT | Rubrics | Overall Rubric Quality — deviation acceptance | Moderate (deviation-accepted) | 27% aggregate FAIL persists per validator | Operator sign-off invoking AGENTS.md pipeline-deviations-table absolute-count-gate reading (Major ≥ 3 = FAIL; corrected has 0 Major → PASS). Record deviation acceptance in changes.md with reason. | Recognizes the fan-out structural artifact without rubric rewriting. Requires explicit operator authorization per LENS 7. | Proposed |

Either row 3 or row 3-ALT would close the audit gap. Row 3 is the substantive fix; row 3-ALT is the operator-adjudication path.

## Regression sweep summary

- Atomicity: no regression (bundled-message pattern preserved).
- Self-containment: no regression.
- Truthfulness: no regression (all atoms grounded, verbatim on Applied rows).
- Outcome/Process: no regression (30/0 unchanged).
- Method-lock: no regression.
- Coverage: **improved** (Derek symmetry restored).
- Attribution: **improved** (Elena/Denise grounded).
- All-Failing Rubrics (S4 bucket): no regression.
- Answer-leakage: none.
- Hardness levers: all 8 trace to rubric surfaces.

## LENS 8 — Regression anchor verification

48/48 anchors passed per prior council output. No new regression introduced by MATERIALIZE.
