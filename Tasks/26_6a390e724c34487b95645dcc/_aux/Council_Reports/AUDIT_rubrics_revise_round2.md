# AUDIT — Rubrics phase (Strict Veteran QC, REVISE round 2)

**Task:** 26_6a390e724c34487b95645dcc
**Deliverable:** `7_Rubrics.json` (23 outcome rubrics, 0 process — up from 21)
**Universe today:** 2026-06-12 (US/Eastern)
**Audit date:** 2026-06-22
**Auditor stance:** STRICTEST possible interpretation. 5/5 only. Every "should" read as "must". Density bar 50+ midpoint. Any derived-answer leak = BLOCKER.
**Scope:** RE-AUDIT of the 4 touched rubrics ONLY (the 19 unchanged rubrics already passed STRICT in `AUDIT_rubrics.md`).
**Prior verdict:** REVISE — 2 MAJOR atomicity bundles flagged on R7 (5 facts) and R8 (4 facts), fix-in-place via specified splits.

---

## Touched rubrics under re-audit

### R7a — id `d24e1078-a191-43e0-f3b2-8f70a1a2c3c6` (modified)
> "The Agent's email to Hannah and William confirms the $4,820.30 SALT late-post is posted to northstar_legal_FP-2025-12 against William's reply as the late-post authorization."

### R7b — id `7e8d9c2b-1a4f-4e5d-9c3f-2a1b3c4d5e60` (NEW)
> "The Agent's email to Hannah and William references the posted journal entry id and entry number returned by the SALT late-post booking."

### R8a — id `e35f2189-b2a2-44f1-04c3-9081b2b3d4d7` (modified)
> "The Agent's email to Hannah and William references the SALT support memo filed under restricted classification with IRS_TAX_7Y retention."

### R8b — id `8f9e0d3c-2b5f-4f6e-0d4f-3b2c4d5e6f71` (NEW)
> "The Agent's email to Hannah and William confirms the return package can move to client signature and the e-file path is unblocked."

---

## LENS 1 — Strict QC scoring on the 4 touched rubrics

### R7a — posting-confirmation atom

| Sub-dim | Score | Reason |
|---|---:|---|
| Atomicity | **5** | One semantic claim: "posting confirmation" = (figure + target period + auth source) as a single unit. Matches V3 Task11..14 posting-confirmation precedent where figure + booking target + auth source stay bundled as one atom because they describe one act (the booking). The 5-fact bundle defect (figure + period + auth + JE id + entry_number) is dissolved by lifting the JE identifiers into R7b. Cannot meaningfully split further without artificial fracture (an agent that writes "$4,820.30 posted to FP-2025-12 under William's reply" hits all three in one breath — V3 norm). |
| Self-Containment | **5** | All values embedded: `$4,820.30`, `northstar_legal_FP-2025-12`, "William's reply as the late-post authorization". Judge needs no universe access. |
| Completeness | **5** | Covers OE9's posting-confirmation requirement ("$4,820.30 SALT late-post JE is posted to northstar_legal_FP-2025-12 with William's reply as the late_post_authorization_id"). |
| Flexibility | **5** | Strict EM on figure + period id; auth reference is "William's reply" (descriptive; ties to William White's email_scen_068 via R6 + evidence). No `(or similar)`, no `approximately`, no soft language. |
| Accuracy | **5** | All three values grounded: `$4,820.30` (William's auth email body + OE9), `northstar_legal_FP-2025-12` (OE4), William's reply (email_scen_068_northstar_annual_corp_tax_0008, OE2). |
| Agent-Centric Phrasing | **5** | "The Agent's email to Hannah and William confirms…" — agent-centric, active voice. |
| Convention Compliance | **5** | Zero em-dashes / en-dashes. No "at least N". No leaked internal IDs in title. No subjective language. Hyphenated `late-post` is V3-standard compound. |
| Tool-Name Leak | **5** | Re-grepped against `8_Server_Tools_Details.json`. Zero hits. |

**R7a verdict:** **5/5 on every sub-dim.**

### R7b — JE identifier atom

| Sub-dim | Score | Reason |
|---|---:|---|
| Atomicity | **5** | One semantic claim: "the booked JE's identifiers" = paired identifier reference (JE id + entry_number always move together as the runtime output of `oracle_gl_post_journal_entry`). V3 reference treats paired identifier references as a single atom (e.g., Task11..14 patterns where `id + number` or `id + url` stay bundled). |
| Self-Containment | **5** | Identifier references are described (no forward-reference confusion); judge cross-checks against the posted JE id/entry_number from OE7. |
| Completeness | **5** | Covers the OE9 ask "reference the staged JE id and entry_number". |
| Flexibility | **5** | Identifiers are runtime outputs (cannot be pre-stated). No `(or similar)` needed — judge checks presence of the actual returned id and entry_number string. |
| Accuracy | **5** | OE7 produces the posted JE id and entry_number; OE9 binds the email back. No drift. |
| Agent-Centric Phrasing | **5** | "The Agent's email to Hannah and William references…" — agent-centric. |
| Convention Compliance | **5** | Zero violations. "SALT late-post booking" matches the prompt's voice ("the booking is live"). |
| Tool-Name Leak | **5** | No tool function names in title. |

**R7b verdict:** **5/5 on every sub-dim.**

### R8a — memo-reference atom

| Sub-dim | Score | Reason |
|---|---:|---|
| Atomicity | **5** | One semantic claim: "the memo with its filing metadata" = (memo reference + classification + retention) describes one artifact's filing attributes as a single bundle. V3 norm for artifact-reference rubrics (Task11..14 same pattern: artifact reference + classification + retention bundled when describing the same upload). |
| Self-Containment | **5** | Concrete values embedded: `restricted`, `IRS_TAX_7Y`. The "SALT support memo" descriptor is unambiguous (only one memo is created in OE8). Evidence specifies "support memo document id (from OE8)" so the judge knows the memo doc id is the binding value. |
| Completeness | **5** | Covers OE9's memo-reference ask ("reference the support memo document id filed under restricted classification with IRS_TAX_7Y retention"). |
| Flexibility | **5** | Strict EM on classification + retention codes. Title says "the SALT support memo"; evidence pins to the doc id — title-evidence pairing is V3-standard. |
| Accuracy | **5** | `restricted` + `IRS_TAX_7Y` match OE8 upload spec and universe retention-code whitelist. |
| Agent-Centric Phrasing | **5** | "The Agent's email…references the SALT support memo…" — agent-centric. |
| Convention Compliance | **5** | Zero em-dashes. No "at least N". No subjective language. |
| Tool-Name Leak | **5** | `records_vault` does not appear in title (it does in evidence, where allowed). No tool function names. |

**R8a verdict:** **5/5 on every sub-dim.**

### R8b — package/e-file clearance atom

| Sub-dim | Score | Reason |
|---|---:|---|
| Atomicity | **5** | One semantic claim: "the downstream workflow is unblocked" = (package to signature + e-file unblocked) describes one workflow state (the prompt frames both as the same clearance: "the e-file path shouldn't be sitting behind accrual housekeeping" + "package can move to the client for signature"). Both clearance statements share one semantic intent. Justification correctly states "Both clearance statements share one semantic intent and stay bundled, but split from the memo-reference fact for partial-credit granularity". |
| Self-Containment | **5** | Plain-language workflow facts. No external lookup needed. |
| Completeness | **5** | Covers the two clearance statements OE9 calls out ("the return package can move to the client for signature and the e-file path is unblocked"). |
| Flexibility | **5** | Freetext clearance phrasing; the two concrete concepts (client signature, e-file path unblocked) come directly from the prompt's own words, so the agent will naturally echo. No `(or similar)` needed — V3 precedent for tight prompt-echoed clearance phrasing does not require softening. Adjacent rubrics in this set that do use `(or similar)` are agent-identification 2.1 rubrics, not artifact-content rubrics. |
| Accuracy | **5** | Both phrases traced verbatim to prompt + OE9. |
| Agent-Centric Phrasing | **5** | "The Agent's email…confirms the return package can move…" — agent-centric. |
| Convention Compliance | **5** | Zero em-dashes. "e-file" is V3-standard hyphenation. No "at least N". No subjective language. |
| Tool-Name Leak | **5** | No tool function names. |

**R8b verdict:** **5/5 on every sub-dim.**

**LENS 1 cross-rubric verdict:** All 4 touched rubrics clear every sub-dim at 5/5 under STRICTEST reading. **Atomicity defect from prior REVISE is fully resolved** — the 5-fact R7 bundle and the 4-fact R8 bundle now decompose into 2+2 same-artifact atoms that match V3 Task11..14 granularity.

---

## LENS 2 — Answer-leakage sweep on the 4 new/modified titles

| Token | Appears in R7a / R7b / R8a / R8b? | Disposition |
|---|---|---|
| `$4,820.30` | R7a title | EXPECTED — figure is the check target; agent must DERIVE via R17 (GL trace) before writing. The prompt's "not one we copied off the messaging trail" + R17's explicit GL-derivation identification rubric remain the synthesis gate. R7a checks that the derived figure ends up in the email content. |
| `northstar_legal_FP-2025-12` | R7a title | EXPECTED — period id is the booking target the agent must surface in confirmation. R18 forces the closed-period identification upstream. |
| `William's reply` | R7a title | EXPECTED — auth source is the binding that R2 + R18 force; the email confirmation must echo. Not a leak — judge checks presence in agent's own write. |
| `posted journal entry id and entry number` | R7b title | EXPECTED — runtime outputs from OE7. Cannot be leaked (not knowable until the agent posts the JE). |
| `restricted` / `IRS_TAX_7Y` | R8a title | EXPECTED — filing metadata the agent uploaded in OE8 must be reflected in the email. R3 forces the upload-spec; R8a verifies the audit-trail email surfaces it. |
| `return package can move to client signature` / `e-file path is unblocked` | R8b title | EXPECTED — these phrases come directly from the prompt ("move to the client for signature" + "e-file path shouldn't be sitting behind accrual housekeeping"). Echoing the prompt's own workflow language is not a leak — it is a content check. |

**Cross-source synthesis check:** No new tool-call shortcut introduced. The new titles re-cite values already present in pre-split R7 + R8 — splits only repartition the partial-credit signal. The agent's path through the levers (L2 GL triangulation, L8 multi-link chain, L9 universe override, L10 stub recognition) is unchanged.

**LENS 2 verdict:** **ZERO new derived-answer leaks.** All literal hits are check targets the agent must include in the email, traceable to R17 / R18 / OE7 / OE8 derivations.

---

## LENS 3 — Hardness end-to-end trace (Lever 8 chain integrity)

**Lever 8 — A → B → C → D multi-link chain:**

| Hop | Pre-split rubric coverage | Post-split rubric coverage | Preserved? |
|---|---|---|---|
| A: slack anchor (manager-asserted figure) | R17 (GL-grounded derivation overrides slack chatter) | unchanged | ✓ |
| B: GL absence + recomputation | R17 + R1 (JE amount lock) + R4 (memo content GL trace) | unchanged | ✓ |
| C: JE staging with auth binding | R1 (JE staging) + R2 (late_post_authorization_id binding) | unchanged | ✓ |
| D: audit-trail email + memo with related_resource_id | R3 (memo upload tied to JE) + R5 (memo body cites William's email + JE id + entry_number) + R6 (email channel) + **R7 + R8** (email content) | R3 + R5 + R6 + **R7a + R7b + R8a + R8b** | **✓ — D-link is now 5 rubrics instead of 4, with finer partial-credit granularity on the email-content content fork** |

**Composition check:** The D-link audit-trail email previously needed pre-split R7 (5 facts in one rubric) + R8 (4 facts in one rubric) to fire together. Now an agent gets credit per atom — R7a (posting confirmation) and R7b (JE identifiers) and R8a (memo reference) and R8b (package + e-file clearance) score independently. Total D-link fact coverage is **unchanged**; partial-credit signal is **stronger**.

**LENS 3 verdict:** Lever 8 chain integrity preserved end-to-end. All 4 layers (prompt sentence → OE step → rubric criterion → Fact_Ledger atom) still cited at every hop. No hardness regression.

---

## LENS 4 — Density projection

**Touched rubrics:** all 4 are email-body content checks on a single email send (or reply). One tool call (`email_send_email` or `email_reply_to_email`) covers all 4.

**Tool-call delta from split:** **+0 tool calls.** The agent's runtime path is unchanged — they still send one email; the email's content is now scored across 4 rubrics instead of 2.

| Metric | Pre-split | Post-split | Delta |
|---|---:|---:|---:|
| Hyper-strict floor | 43 | 43 | 0 |
| Realistic-strict midpoint | 47 | 47 | 0 |
| Council B midpoint | 52 | 52 | 0 |
| Hardness Plan midpoint | 52 | 52 | 0 |

**LENS 4 verdict:** Density projection **unchanged**. Splits do not move the floor or midpoint. Runtime monitor disposition from prior audit carries forward.

---

## LENS 5 — Adversarial veteran review on the 4 touched rubrics

| Check | Finding | Verdict |
|---|---|---|
| V3 voice preservation | R7a/R7b/R8a/R8b all use "The Agent's email to Hannah and William confirms/references…" — direct match to V3 Task11..14 email-content rubric pattern. | PRESERVED |
| Single-channel lock-in introduced? | R6 (parent rubric on email channel) already allows email_send_email OR email_reply_to_email. R7a/R7b/R8a/R8b are content checks on either path — no method/channel lock-in introduced. | NO LOCK-IN |
| Off-framework phrasing | All 4 titles use framework-standard agent-centric phrasing. Hyphenated `late-post`, `e-file` match V3 norms. | CLEAN |
| Missing `(or similar)` where needed for freetext | R8b is the most freetext-shaped (workflow clearance phrasing). The two concrete concepts ("client signature", "e-file path unblocked") come directly from prompt language, so agent will echo. V3 precedent: artifact-content rubrics checking presence of prompt-anchored concepts do NOT require `(or similar)` — adjacent 2.1 identification rubrics in this set (R12/R13/R15/R16/R17/R19/R20/R21) use `(or similar)` because they describe agent-generated identifications. R7a/R7b/R8a/R8b are different shape (content presence, not identification framing). | CLEAN |
| New atomicity violations introduced? | R7a packs (figure + period + auth) = posting-confirmation atom, V3-norm. R7b packs (JE id + entry_number) = paired-identifier atom, V3-norm. R8a packs (memo + classification + retention) = artifact-filing-attribute atom, V3-norm. R8b packs (signature + e-file unblocked) = single-clearance atom, V3-norm. Each new rubric is at V3-reference granularity — no new bundle defect. | CLEAN |
| New entity drift introduced? | Email addresses (Hannah/William) referenced as display names in the rubric prose; binding addresses already in R6. Period id `northstar_legal_FP-2025-12` exact. No drift. | NO DRIFT |
| Em-dashes / "at least N" / `approximately` / forbidden softeners | Zero across all 4 new titles. | CLEAN |
| Tool-name regrep | Re-grepped all 4 titles against full tool registry. Zero hits. | CLEAN |
| Justification quality on new rubrics | R7b justification: "Splitting from the posting-confirmation fact preserves partial-credit granularity per V3 reference voice" — invokes V3 voice correctly. R8b justification: "Both clearance statements share one semantic intent and stay bundled, but split from the memo-reference fact for partial-credit granularity" — correctly identifies the bundle decision. | SOUND |
| Evidence quality on new rubrics | R7b evidence explicitly says "check the content parameter…for an explicit reference to the posted JE id and entry_number returned by OE7" — pins the runtime values. R8b evidence: "check the content parameter…for an explicit confirmation that the return package can move to client signature and the e-file path is unblocked" — pins the concrete concepts. | SOUND |

**LENS 5 verdict:** **Zero new defects introduced.** V3 voice preserved across all 4 touched rubrics. Atomicity decomposition matches V3 Task11..14 granularity. No regressions on entity drift, lock-in, phrasing, tool-name leak, or justification/evidence quality.

---

## Cross-lens roll-up

| Lens | Result | Blockers |
|---|---|---|
| L1 — Strict QC scoring on R7a/R7b/R8a/R8b | All 4 rubrics 5/5 on every sub-dim under STRICTEST reading | 0 |
| L2 — Answer-leakage sweep on 4 new titles | Zero new derived-answer leaks; all literal hits are check targets | 0 |
| L3 — Hardness end-to-end trace (Lever 8) | A→B→C→D chain integrity preserved; D-link granularity strengthened | 0 |
| L4 — Density projection | Unchanged (+0 tool calls from splits) | 0 |
| L5 — Adversarial veteran review | Zero new defects; V3 voice preserved | 0 |

---

## Resolution of prior REVISE items

| Prior REVISE item | Severity | Status |
|---|---|---|
| R7 — 5-fact atomicity bundle | MAJOR | **RESOLVED** — split into R7a (posting-confirmation atom) + R7b (JE-identifier atom). Each new rubric is at V3-reference granularity with 5/5 atomicity. |
| R8 — 4-fact atomicity bundle | MAJOR | **RESOLVED** — split into R8a (memo-reference atom) + R8b (clearance atom). Each new rubric is at V3-reference granularity with 5/5 atomicity. |
| R5 — memo body 3-fact bundle | MINOR (defensible) | **NOT TOUCHED** (not required by prior REVISE) — log for runtime monitor. |
| R13 — Linear body 3-fact bundle | MINOR (designed-lever bundle) | **NOT TOUCHED** (not required) — designed Lever 5 thread-reply-blindness compound. |
| R21 — 3-authority bundle | MINOR (designed-lever bundle) | **NOT TOUCHED** (not required) — designed Lever 4+5 compound. |
| Density realistic-strict midpoint 47 | NOTE | **CARRIED FORWARD** as runtime monitor — splits introduce zero tool-call delta; trigger conditions (avg < 40 OR pass@1 > 40%) unchanged. |

---

## Upstream-propagation findings

**None.** Splits are rubric-file-local; no S1 (prompt) or S2 (OE) revision required.

---

## VERDICT

**PASS (STRICT)** — All 4 touched rubrics (R7a, R7b, R8a, R8b) clear every lens at 5/5 under STRICTEST reading. The prior MAJOR atomicity defect on R7 (5-fact bundle) and R8 (4-fact bundle) is fully resolved by the specified splits. No new defects introduced. V3 Task11..14 granularity is now matched on the email-content rubric cluster.

**The rubric set (23 outcome / 0 process) is ready for the FINAL council.**

### Carry-forward items (not blocking)
- **Runtime monitor:** if avg tool calls < 40 across 6 runs OR pass@1 > 40%, density retroactively becomes a BLOCKER → PIPELINE REDO.
- **Defensible bundles (R5 / R13 / R21):** logged for post-trajectory review only; not actionable at this phase.

### Not required
- No further rubric revisions.
- No S1 redo.
- No S2 redo.
- Ready to proceed to FINAL council on the cross-artifact bundle.

---

VERDICT: **PASS (STRICT)**
