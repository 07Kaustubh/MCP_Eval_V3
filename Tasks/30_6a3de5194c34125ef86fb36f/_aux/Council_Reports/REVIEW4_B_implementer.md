# REVIEW4 Implementer seat report (B3)

**Pass:** REVIEW4 COUNCIL_MODE=multi (post-REVIEW3 SHIP-READY pre-ship sanity check).
**Lens:** Implementer — simulate an Opus 4.8 agent receiving the corrected bundle, surface trajectory-execution defects (density, hardness calibration, known-failure modes) that the prior 3 passes' lenses could not see.
**Inputs read:** `AGENTS.md`, `Tasks/_meta/Learnings.md`, `Reference/Hardness_Playbook.md`, `_aux/REVIEW_prompt_draft.txt`, `_aux/REVIEW_persona_draft.txt`, `14_Updated_Oracle_Events.txt`, `15_Updated_Rubrics.json`, `_aux/Trajectory_Stats.json`, `8_Verifier_Fails.txt`, `changes.md`, `_aux/Council_Reports/REVIEW3_summary.md`.

---

## Seat verdict

**PASS — with one MAJOR caveat the operator must consume before ship.**

The corrected bundle (5 + 6 + 7) is structurally sound, every gate REVIEW3 ran returned PASS / PASS (STRICT), and the rubric set holds together against an Opus 4.8 simulation. The single material concern this seat surfaces — **measured-floor density underflow on 3 of 6 runs (33, 34, 36 tool calls)** — is technically within AGENTS.md Rule #11's THIN_DENSITY band on midpoint (midpoint analysis is what the rule actually gates on), and Row 12 was specifically designed and applied as the density fix. Further REVISE would not be cost-effective; the residual risk is a known shipping risk, not a producing-phase defect.

---

## Trajectory simulation

Walking the corrected prompt + 9 OEs as if I were an Opus 4.8 agent given Marina's brief and the prompt as the first user turn.

| OE | Predicted tool call(s) | Predicted parameters | Likely divergence | Salvageable? |
|---|---|---|---|---|
| OE01 | `reminder_get_all_reminders` then `oracle_gl_get_journal_entry` | none / `journal_entry_id=je_b2c2b939a1244823` | Some agents skip the reminder and go straight to `oracle_gl_list_journal_entries` with `period_id="acme_cloud_FP-2026-04"` — universe today (2026-06-12) + "earlier this quarter" + "settlement receipt from largest enterprise SaaS customer" gives them enough to filter the GL by April period + customer-name search. **Either path lands the JE** — reminder title or GL filter both unambiguously surface `JE-acme_cloud-FP-2026-04-0052`. | yes — both paths converge |
| OE02 | `email_search_emails` + `slack_conversations_search_messages` | broad queries: "Acme Cloud AML", "wire monitoring", "CDD clearance" | Agents reliably surface the full clearance chain (Farah → Marina → Anita → Steven) — verified in all 6 measured runs. No divergence risk. | n/a |
| OE03 | `reminder_get_all_reminders` | none | Already done in OE01 if reminder-first path taken. ~50% of runs duplicate this call. | n/a |
| OE04 | `reminder_delete_reminder` | `reminder_id="reminder_scen_041_audit_compliance_0000"` | **100% pass in measured.** No divergence. | n/a |
| OE05 | `records_vault_list_documents` | `entity_id="acme_cloud"`, `kind="memo"` (some agents omit `kind` and get the full list) | No divergence — 6/6 measured runs called this. | n/a |
| **OE06 (NEW)** | `records_vault_download_document_content` × 1-2 | `document_id="doc_fb028c9124e146c5"` (BO Refresh) and/or `document_id="doc_38a8236a0c4546e2"` (AML Risk Assessment) | **This is the load-bearing divergence.** The prompt nudge "anchored to the firm's existing AML precedent for this client" is a *soft instruction* per `Learnings.md` L27 pattern. Two readings: (a) **strict** — "download and quote the precedent in the memo content"; (b) **lax** — "match the existing AML treatment (retention code, classification) of similar memos." Reading (b) does NOT require a download. Measured 6-run sample had 0/6 agents call `records_vault_download_document_content` on either of these memos despite both being visible in the OE05 listing. The corrected prompt nudge is the only signal pushing toward reading (a). **Projected agents who actually do OE06: 2-4 of 6.** | partial — agents who skip OE06 still produce a complete memo but fail R25 + R26 |
| OE07 (was OE06) | `records_vault_upload_document` | `title`, `kind="memo"`, `retention_policy_code="AICPA_SQMS_7Y"`, `classification="restricted"`, `content_b64=<memo>` | **R13 (Marina-coordinator) divergence is unchanged from measured** — 5/6 measured runs wrote "Prepared by: Marina Soko" rather than labeling her active coordination role. The persona scope tightening (Row 7) added "CDD case management" to her scope but does NOT instruct her to label herself as coordinator. Prompt language "I coordinated the CDD package through to clearance with Anita and Steven" is unchanged from measured. **Projected R13 pass rate: 1-2 of 6 (unchanged from measured 1/6).** | n/a — lever is working as designed |
| OE08 (was OE07) | `slack_conversations_search_messages` then `slack_conversations_add_message` | `channel_id="C008"`, `thread_ts="1776969000.000000"` | 6/6 measured runs hit the correct thread_ts. No L26 decoy-parent risk in this universe (no measured competing thread on AML/Acme topic). | n/a |
| OE09 (was OE08) | `email_send_email` | `recipients=[matthew, steven]`, `cc=[farah]`, `subject=<includes JE id>` | The new Row 8 prompt clause "tagging the JE in the subject so they can correlate it against the original alert" is **explicit** — projected R5 pass rate: 5-6 of 6 (a near-guarantee, not a discriminating lever). | n/a |

**Net trajectory verdict:** the agent reliably executes the spine. The two divergence points are (a) OE06 will be skipped in ~50% of runs (drives R25 + R26 cascade fail), and (b) R13 Marina-coordinator labeling will be missed in ~80% of runs (the load-bearing measured lever, unchanged by the corrected bundle). Neither divergence is fatal to bundle integrity — they ARE the hardness levers.

---

## Hardness calibration

### Projected pass@1

| Rubric | Measured fail rate | Projected fail rate on corrected bundle | Reasoning |
|---|---:|---:|---|
| R13 (Marina coordinator) | 5/6 | 4-5 / 6 | Persona scope tightening adds "CDD case management" but does not instruct labeling; prompt language unchanged. |
| R5 (JE id in subject) | not measured | 0-1 / 6 | Row 8 prompt clause is explicit. Near-guaranteed pass. Not a discriminating lever. |
| R25 (precedent download) | not measured | 2-4 / 6 | Soft prompt nudge (L27 pattern); some agents will read "anchored to existing precedent" as "download and reference," some as "match the metadata." 50/50. |
| R26 (precedent linkage in memo content) | not measured | 2-4 / 6 | Cascading dependency on R25 — if agent didn't download, they can't reference. |
| All other 22 rubrics | ≤ 1/6 each | ≤ 1/6 each | Unchanged — measured runs were 23/24 at floor. |

**Projected pass@1 (all 26 rubrics pass):** 0/6 (0%). Lower than measured 1/6 (16.7%) because R25 + R26 introduce two new fail surfaces that did not exist at measurement time. The cascading dependency (R25 → R26) means an agent that skips OE06 typically loses both rubrics in one shot.

**Compliance with AGENTS.md pass@1 ≤ 40% target:** PASS. 0/6 is comfortably below 40%.

### Projected avg tool calls

Re-derived from the measured 6-run sample (NOT echoing REVIEW3's projection):

| Run | Measured | Will agent do OE06? | Predicted OE06 delta | Projected post-fix |
|---|---:|---|---:|---:|
| 1 | 50 | likely (high-density, thorough investigative profile) | +2 | 52 |
| 2 | 34 | unlikely (compact execution path) | 0 | 34 |
| 3 | 33 | unlikely (compact execution path) | 0 | 33 |
| 4 | 56 | likely (highest-density, exhaustive profile) | +2 | 58 |
| 5 | 36 | unlikely (the ONE passing run was compact, not exhaustive) | 0 | 36 |
| 6 | 50 | likely (high-density) | +2 | 52 |

**Projected avg:** (52 + 34 + 33 + 58 + 36 + 52) / 6 = 265 / 6 = **~44.2** (essentially identical to REVIEW3's ~44.7 estimate, with slightly different distribution).

### Density floor risk (per-run < 40 BLOCKER threshold per AGENTS.md Rule #11 absolute floor reference)

**3 of 6 runs are projected to remain under 40 tool calls** (runs 2, 3, 5 at 34, 33, 36).

Critical distinction: AGENTS.md Rule #11's BLOCKER threshold is on **midpoint < 40**, not per-run floor. The literal text: "midpoint < 40 = INSUFFICIENT_DENSITY (BLOCKER, STOPs the pipeline)". The 44.2 projected midpoint is in THIN_DENSITY band (40-49), explicitly allowed "with per-task justification."

REVIEW3's per-task justification is documented in `_aux/Council_Reports/REVIEW3_summary.md` and re-asserted here — the lever-quality tradeoff is real and the Row 12 design choice was correct.

**However**, the empirical risk that Rule #11's THIN_DENSITY warning anticipates ("the task is at risk of underflow on real platform runs") is not just a hypothetical risk for this task — it is **already measured**. Half the 6-run measured sample underflowed 40. The Row 12 OE06 fix lifts the midpoint but does NOT structurally repair the 3 underflowing runs because those runs were compact-execution profiles that won't necessarily inflate from a soft prompt nudge.

**This is a known shipping risk, not a producing-phase defect** — but the operator must understand it before ship.

---

## Lever-by-lever projections

### Lever 1 — Marina coordinator role (R13)

| Stage | Projection | Reasoning |
|---|---|---|
| Rubric grader applies it strictly | yes — Row 6 tightened evidence with explicit pass/fail examples ("Marina Soko (CDD coordinator)" PASS / "Prepared by: Marina Soko" FAIL) | Grader-resistant to drift. |
| Agent attempts the active-coordinator labeling | 1-2 of 6 | Measured 1/6 succeeded; persona scope tightening (Row 7) is a marginal positive; prompt language ("I coordinated the CDD package through to clearance with Anita and Steven") unchanged. |
| Pass rate on fresh 6-run sample | **1-2 of 6 (16-33%)** | The dominant Opus 4.8 pattern is "Prepared by" header attribution — the corrected bundle does not address this directly. |

**Lever status:** HIGH-yield, structurally sound. This is the task's strongest hardness mechanism per measured evidence.

### Lever 2 — JE id in email subject (R5)

| Stage | Projection | Reasoning |
|---|---|---|
| Rubric grader applies it strictly | yes — Row 9 title rewrite + explicit JE id in evidence | Clear. |
| Agent attempts JE-id-in-subject | 5-6 of 6 | Row 8 prompt clause is **explicit instruction**: "tagging the JE in the subject so they can correlate it against the original alert." Opus 4.8 reliably follows explicit instruction. |
| Pass rate on fresh 6-run sample | **5-6 of 6 (83-100%)** | This is a near-guarantee, not a discriminating hardness lever — it is a *good craft* rubric that closes the prompt-rubric framing gap (Row 8 BLOCKER). |

**Lever status:** LOW-yield as a hardness mechanism. Its real value is closing the Council_Protocol B2/B6 prompt-rubric framing defect, not driving fail rate. The "3 levers" claim in REVIEW3's hardness justification overcounts here — R5 is more accurately a *guard rubric*.

### Lever 3 — Precedent linkage (R25 + R26 as a pair)

| Stage | Projection | Reasoning |
|---|---|---|
| Rubric grader applies it strictly | yes — closed-set disjunctive titles (Row 13), evidence specifies both memo doc ids as acceptable targets | Grader-resistant. |
| Agent attempts the precedent download (R25) | 2-4 of 6 | Soft prompt nudge ("anchored to the firm's existing AML precedent for this client") is the L27 pattern from Learnings.md. Reading (a) "download and reference" vs reading (b) "match the metadata" splits the 6-run sample. Measured 0/6 agents called `records_vault_download_document_content` against either memo. |
| Agent attempts precedent reference in memo content (R26) | 2-4 of 6 | Cascading dependency on R25. If agent did download, they typically reference. If they didn't, they don't. |
| Pass rate on fresh 6-run sample | **R25: 2-4 of 6 (33-67%); R26: 2-4 of 6 (33-67%), correlated** | Discriminating but at the lighter end of mid-yield. |

**Lever status:** MID-yield, the only post-Row-12 fresh density+difficulty lever. Operator should understand that ~50% of runs will likely skip OE06 — this is desired behavior for the lever (it produces real failures), but it also means OE06's projected +1.5 tool-call lift is mostly on the runs that DON'T need the lift (the already-over-40 runs).

### Effective lever count (re-derived, not echoing REVIEW3)

- **R13 (Marina coordinator)** — high-yield discriminating lever ≈ 1 effective lever.
- **R5 (JE id in subject)** — guard rubric, ≈ 0 effective levers as hardness mechanism.
- **R25 + R26 (precedent linkage)** — paired mid-yield lever ≈ 1 effective lever (the two rubrics are mechanically dependent so they count as one mechanism).

**Effective lever count = 2 mechanisms** (Marina coordinator + precedent linkage), not 3.

This does NOT block ship — Hardness_Playbook's "3-of-target" is a default, not a hard rule, and the 2 effective mechanisms reach pass@1 ≤ 40% comfortably. But the REVIEW3 framing of "3 levers" is generous on R5. INFORMATIONAL finding only.

---

## Known-failure-mode scan (cited from `Tasks/_meta/Learnings.md`)

| Failure mode | Citation | Risk on this bundle | Mitigation |
|---|---|---|---|
| **L1 confirm-already-done (100% pass)** | `Learnings.md` L1 | LOW. Prompt says "confirm... is properly closed out" — could be read as L1. But also says "If anything is still sitting open... please take care of it." The action mandate is explicit; agents won't sit on a positive-confirm. | none needed |
| **L6 correct-answer-in-artifact-body (100% pass)** | `Learnings.md` L6 | NONE. JE id is discoverable from reminder title only; no email/Slack/document body states the correct retention code or the Marina-coordinator labeling. | n/a |
| **L7 binary "is it posted?" (100% pass)** | `Learnings.md` L7 | NONE. The JE IS posted and the agent finds it; the discriminating question is the memo *content*, not GL existence. | n/a |
| **L15 implicit prompt (HARD rule)** | `Learnings.md` L15 | OK. Prompt does not hint that anything is wrong with the JE / clearance / existing reminders — agent self-discovers the open reminder via OE03. | n/a |
| **L16 persona believes the (right) framing** | `Learnings.md` L16 | OK. Marina believes the case is cleared and asks for housekeeping wrap-up. | n/a |
| **L27 soft-instruction over/under-compliance** | `Learnings.md` L27 | **MEDIUM-HIGH on R25/R26 lever realization.** "Anchored to the firm's existing AML precedent" is exactly the L27 pattern: agents may read it as either a directive to download or as a metadata-matching style instruction. Expected R25 skip rate: 33-67%. This is desirable for the lever, but it means the projected pass@1 is driven partly by L27 ambiguity, not by genuine investigative depth. | This is a deliberate design choice — explicit instruction would over-prescribe and trip Investigation pre-solved (P6). Living with L27 is the right tradeoff. |
| **L29 escape-valve neutralizes L2** | `Learnings.md` L29 | NONE. No escape-valve clause in the corrected prompt. | n/a |

**Net:** the corrected bundle does NOT fall into any of the documented "100% pass" failure modes (L1/L6/L7). The L27 pattern is intentional and aligned with the lever design.

---

## Rubric grader perspective — ambiguity scan

Walking all 26 rubrics under a strictest-interpretation grader to find any title or evidence that two graders could reasonably interpret two different ways.

| Rubric | Ambiguity | Severity |
|---|---|---|
| #1 GL/CDD consistency in memo | clear — both elements + consistency conclusion required | clean |
| #2 delete reminder | exact id match | clean |
| #3 upload disposition memo | clean | clean |
| #4 title identifies client + AML/compliance | clear OR-disjunction on subject term | clean |
| #5 JE id in subject | explicit JE id in evidence; clear | clean |
| #6 retention AICPA_SQMS_7Y | exact match | clean |
| #7 classification restricted | exact match | clean |
| #8 ledger reference in memo | requires 2 of 4 identifiers — clear | clean |
| #9 CDD rationale in memo | OR-disjunction on rationale terms — clear | clean |
| #10-12 Farah / Anita / Steven stages | name OR role description — clear with pass/fail bar | clean |
| #13 Marina coordinator | tightened with explicit pass/fail examples | clean |
| #14 Slack thread reply C008 + thread_ts | exact match | clean |
| #15 Slack GL positive outcome | OR-list of acceptable phrasings — clear | clean |
| #16 Slack reminder dismissal | OR-list — clear | clean |
| #17 Slack memo filing | OR-list — clear | clean |
| #18 email to Matthew | exact email match | clean |
| #19 email to Steven | exact email match | clean |
| #20 cc Farah | exact email match | clean |
| #21 email body close-out | Row 10 corrected body→content | clean |
| #22 final response GL/CDD | both elements + positive outcome — clear | clean |
| #23 final response reminder dismissed | OR-list — clear | clean |
| #24 final response memo filed | OR-list — clear | clean |
| **#25 precedent download** | clear — two doc ids named as acceptable targets, "listing alone does not pass" explicit | clean |
| **#26 precedent linkage in memo** | "naming a prior memo OR quoting its substantive conclusion" — **MINOR ambiguity** on "substantive conclusion." A grader could read "cleared BO outcome" as sufficient, or could insist on a verbatim quote. Evidence does enumerate "the cleared beneficial-ownership outcome from the BO Refresh, or the prior risk-tier or counterparty risk-score determination from the AML Risk Assessment" as acceptable — this constrains drift but leaves room for strict graders to reject a paraphrase. | MINOR |

**Net:** 25 of 26 rubrics are grader-resistant. Rubric #26 has minor "substantive conclusion" semantic latitude. INFORMATIONAL — not blocker, not even MAJOR. The evidence enumeration constrains worst-case drift.

---

## Findings

### BLOCKER
none

### MAJOR
- **M1 — Density floor underflow on 3 of 6 measured runs persists after Row 12 fix.** Runs 2, 3, 5 measured at 34 / 33 / 36 tool calls. Row 12's OE06 projected +1.5 calls/run is an *average* that does not structurally repair the floor — the 3 underflowing runs are compact-execution profiles least likely to adopt the OE06 download under a soft prompt nudge (L27 pattern, `Learnings.md` L27). Projected post-fix: runs 2, 3, 5 stay at ~34 / 33 / 36. The 44.2 midpoint passes AGENTS.md Rule #11 (THIN_DENSITY band, midpoint-based) but the empirical risk Rule #11's THIN_DENSITY warning anticipates ("the task is at risk of underflow on real platform runs") is already MEASURED on this task, not hypothetical. **Recommended action:** ship, with explicit operator-level disclosure that ~50% of platform runs will likely return under 40 tool calls — and accept that if the platform applies a per-run-floor density check (rather than midpoint-only), this task may come back failing density. Not a producing-phase defect; not REVISE-grade; but the operator must consume this finding before pressing ship.

### MINOR
- **m1 — Effective lever count is 2 mechanisms, not 3.** R5 (JE id in email subject) is a *guard rubric* / near-guaranteed pass once the Row 8 prompt clause was added — it is not a discriminating hardness mechanism. The real mechanisms are R13 (Marina-coordinator labeling, high-yield) and R25 + R26 paired (precedent linkage, mid-yield). Hardness_Playbook composition rule allows "3 levers is acceptable only if the chosen 3 include high-cost levers" — this task qualifies because R13 + R25/R26 together project pass@1 = 0/6, comfortably below 40%. INFORMATIONAL, no fix needed, but the REVIEW3 framing of "3 independent levers" overcounts.
- **m2 — Rubric #26 "substantive conclusion" semantic latitude.** A strict-literalist grader could reject a paraphrase of the BO Refresh's cleared outcome and insist on a verbatim quote; a permissive grader accepts a label like "cleared per BO Refresh." The evidence enumeration constrains worst-case drift but leaves a ~10% interpretation gap. Not BLOCKER; ship as-is.

### INFORMATIONAL
- **i1 — R5 (JE id in subject) is structurally a guard rubric, not a discriminating lever.** Once the Row 8 prompt clause "tagging the JE in the subject" was added, this rubric became a near-100% pass. This is correct — Row 8's purpose was to close the Council_Protocol B2/B6 prompt-rubric framing gap (a BLOCKER class defect), not to add a hardness mechanism. The effect is that R5 now serves the QC bar without contributing to the difficulty signal.
- **i2 — R13 (Marina-coordinator) lever survives all bundle changes.** The persona scope tightening (Row 7) added "CDD case management" but does not instruct labeling. The prompt language ("I coordinated the CDD package through to clearance with Anita and Steven") is unchanged from measured. Projected R13 pass rate stays at 1-2 of 6 — the lever is intact.
- **i3 — Trajectory simulation finds the corrected bundle does not introduce any L1 / L6 / L7 / L15 / L16 / L29 known-failure-mode regressions.**

---

## Reasoning

The Implementer lens is asked specifically for what prior 3 passes missed: trajectory-execution defects (density, hardness calibration, Opus-4.8 failure modes). On this bundle:

1. **Trajectory simulation walks cleanly.** The 9 OEs map to predictable Opus 4.8 tool-call sequences. The two divergence points (OE06 skipped ~50% of runs; R13 Marina-coordinator labeling missed ~80% of runs) are exactly the hardness levers, not bundle defects. Bundle is internally coherent.

2. **Hardness calibration is sound but the projected pass@1 (~0/6) is driven by a mix of high-yield R13 and mid-yield R25/R26-paired** — not by three independent levers as REVIEW3 framed. This is acceptable per Hardness_Playbook composition rule (3 levers OK with high-cost mix) but the framing should be honest about R5's role as a guard rubric.

3. **Known Opus 4.8 failure modes do not trap the bundle.** L1, L6, L7, L15, L16, L29 all scanned clean. L27 (soft-instruction) is present and intentional on R25/R26 — that is the lever, not a defect.

4. **Rubric grader pass: 25 of 26 grader-resistant; #26 has minor "substantive conclusion" latitude** — MINOR, not MAJOR, and the evidence enumeration constrains worst-case drift to acceptable.

5. **Density floor analysis is the one finding REVIEW3 documented but did not strictly assess.** REVIEW3's justification correctly applied Rule #11 on the midpoint metric — that part is right. What REVIEW3 did not explicitly assess is that the 3 measured runs under 40 will likely *stay* under 40 after the Row 12 fix, because OE06 fires preferentially on the *already-over-40* runs (high-density, exhaustive profiles read soft nudges as directives). The Rule #11 letter is satisfied. The Rule #11 spirit ("at risk of underflow on real platform runs") is empirically validated rather than hypothetical. This is the MAJOR caveat the operator must consume — but it does not warrant REVISE because the corrected bundle is structurally the best the lever budget allows without inflating with synthetic OEs.

**Net verdict: PASS. One MAJOR finding for operator disclosure. No producing-phase defect found.**

---

## Cited rules engaged

- **AGENTS.md Rule #11** — "midpoint < 40 = INSUFFICIENT_DENSITY (BLOCKER); midpoint 40-49 = THIN_DENSITY (operator can continue with explicit per-task justification, but the task is at risk of underflow on real platform runs)." Engaged on M1 — confirms PASS letter, surfaces measured-floor risk as exactly the THIN_DENSITY-band caveat the rule warns about.
- **AGENTS.md Rule #1** — "Opus 4.8 is the model under test." Engaged on the trajectory simulation lens; all reasoning frames Opus 4.8 specifically, not generic LLM behavior.
- **AGENTS.md Rule #6** — "No 'at least N' in rubric titles unless prompt explicitly mandates a minimum." Verified clean on the corrected rubric set (Row 13 cleared the prior violation on R25/R26 titles).
- **AGENTS.md Rule #12** — "Strict veteran AUDIT runs after every per-phase deliverable." Confirmed by REVIEW3 round-2 PASS (STRICT) on AUDIT_rubrics.
- **`Reference/Hardness_Playbook.md`** composition rule — "4-to-5 levers per task is the design default. 3 is acceptable only if the chosen 3 include high-cost levers." Engaged on m1 — task has 2 effective mechanisms (R13 + R25/R26 paired), R5 is a guard rubric. Mechanism mix qualifies under the "high-cost" exception (R13 alone projects 4-5/6 fail, R25/R26 paired adds another 2-4/6 fail).
- **`Tasks/_meta/Learnings.md` L1, L6, L7, L15, L16, L27, L29** — engaged on Known-failure-mode scan. L27 is the only lens actively engaged by this bundle's design (soft prompt nudge on R25/R26); intentional and aligned with lever realization.
- **`Reference/Council_Protocol.md` B2 + B6** — engaged on validation that Row 8's prompt re-frame closed the prompt-rubric framing gap that REVIEW2 identified as BLOCKER. Confirmed via R5 being a near-100% pass on the corrected bundle (the prompt now matches the rubric expectation).
