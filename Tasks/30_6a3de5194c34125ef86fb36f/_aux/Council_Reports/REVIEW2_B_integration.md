LENS: Integration

# REVIEW2 Council B — Integration Lens (B3 / B4 / B6)

**Task:** `Tasks/30_6a3de5194c34125ef86fb36f`
**Deliverables under review:** `_aux/Scratch_Corrected/{5_Prompt.txt, 6_Oracle_Events.txt, 7_Rubrics.json, 2_Persona.txt}`
**Lens:** Integration — read all three artifacts as a connected set.
**Read-only.** Every cross-artifact claim cited to `file:location`.

---

## VERDICT: REVISE

**Drivers (one BLOCKER, one MAJOR, one MINOR):**

| Severity | Perspective | Issue (one-line) | Fix locus |
|---|---|---|---|
| BLOCKER | B6 + B4 (Lever 2) | Rubric #5 (email-subject-JE-id) demands a step the prompt does not surface — hidden trap | PROPAGATE TO S1 |
| MAJOR | B3 | Integrated density midpoint projects 45-50 (THIN_DENSITY band) — Row 2 edits do NOT meaningfully lift the measured 43.2 baseline | per-task justification (HARDNESS report) — acceptable but flag fragility |
| MINOR | B4 (Lever 1) | Marina-coordinator memo-content lever is preserved end-to-end and Row 6 evidence tightening is correct, but the prompt's first-person framing ("I coordinated...") still nudges Opus 4.8 toward "Prepared by: Marina" failure mode | acceptable as-shipped; flagged for hardness fragility log |

---

## B3 — Integrated tool-call density projection

### Trajectory sketch (competent Opus 4.8 agent, post Row-2 edits)

Prompt now reads (after Row 2): *"a settlement receipt from Acme's largest enterprise SaaS customer tripped our standing FinCEN wire-monitoring threshold ... earlier this quarter"* — no `$57,077.69`, no "late April" anchor (`_aux/Scratch_Corrected/5_Prompt.txt:3`).

| # | Step | Tool calls | Cumulative |
|---|---|---:|---:|
| 1 | Search emails for AML clearance trail (query: "Acme Cloud AML", "FinCEN wire") | 2-3 | 2-3 |
| 2 | Search Slack C008 for case thread (query: "Acme Cloud wire", "AML") | 2-3 | 4-6 |
| 3 | List reminders → find AML monitoring tickler (names JE id in title) | 1 | 5-7 |
| 4 | List JEs in `acme_cloud_FP-2026-04` filtered by customer-settlement-receipt | 1-2 | 6-9 |
| 5 | Get specific JE (`je_b2c2b939a1244823`) to confirm DR/CR + amount | 1 | 7-10 |
| 6 | List records-vault docs (entity=acme_cloud, kind=memo) to confirm gap | 1 | 8-11 |
| 7 | (optional) Get existing AML memos for format reference | 0-2 | 8-13 |
| 8 | (optional) Look up account 101000 / 110000 chart details | 0-2 | 8-15 |
| 9 | (optional) Contacts lookup / list slack users for emails | 0-2 | 8-17 |
| 10 | Upload disposition memo | 1 | 9-18 |
| 11 | Search Slack for exact `thread_ts` (if not yet captured) | 0-2 | 9-20 |
| 12 | Post threaded Slack reply (C008, thread_ts=1776969000.000000) | 1 | 10-21 |
| 13 | Send close-out email | 1 | 11-22 |

**Tight-path minimum:** 11 tool calls (rushed). **Expected mid:** 22-30 atomic + 10-20 overhead = ~35-50.

### Projected midpoint: **45-50** — `THIN_DENSITY`

Per `_aux/Trajectory_Stats.json`:
- Pre-iteration measured avg = **43.2** (range 33-56).
- 3 of 6 runs (#2: 34, #3: 33, #5: 36) underflowed the 40 floor.

The Row 2 edit removes two answer anchors that a smart agent could otherwise have grepped:
- `$57,077.69` removal → forces email/Slack search instead of amount grep across emails. Net +1 to +3 calls.
- "late April" removal → modest effect; the reminder name already exposes the JE id, and the OE03 step assumes the agent finds the reminder.

**Net midpoint lift from Row 2: estimated +2 to +6 calls.** Projected new midpoint: **45-50**.

This sits in the **THIN_DENSITY band (40-49)** per AGENTS.md Hard Rule #11. The HARDNESS report explicitly accepted this fragility (`_aux/Council_Reports/REVIEW_hardness.md`: *"Density 43.2 sits in the THIN band; half the runs underflow 40. Flag for SALVAGEABLE path with explicit hardness-fragility note."*).

The per-task justification exists. THIN_DENSITY is therefore **acceptable but not safe** — a re-run sample with different seeds could easily produce 2+ runs under 40 and re-trip density failure.

**B3 verdict: THIN_DENSITY (acceptable with HARDNESS-documented per-task justification, MAJOR fragility flag).**

---

## B4 — Hardness preservation end-to-end

### Lever 1 — Marina-coordinator-role memo content (rubric #13)

**Trace prompt → OE → rubric:**

- **Prompt cue** (`5_Prompt.txt:5`): *"Farah ran the analyst pass and I coordinated the CDD package through to clearance with Anita and Steven."*
  - Surfaces Marina's coordinator role ✓ in literal language.
  - Risk: the first-person framing nudges Opus 4.8 to interpret "I" as memo authorship and write `Prepared by: Marina Soko` → triggers the Fail example in rubric #13.

- **OE06 cue** (`6_Oracle_Events.txt:24-27`): explicitly enumerates *"Farah Dlamini (AML analyst), Marina Soko (CDD package coordinator), Anita Knowles (supervisory officer), and Steven Perry (engagement partner)"* in the memo `content` description.
  - Provides the lever in concrete tool-call shape ✓.

- **Rubric #13 evidence** (`7_Rubrics.json` rubric 13): Row 6 tightened with Pass examples (`'Marina Soko (CDD coordinator)'`, `'CDD package routed by Marina'`, `'Coordinated by: Marina Soko (Compliance Officer)'`, `'Marina Soko assembled and routed the CDD package'`) AND Fail examples (`'Prepared by: Marina Soko'`, `'Author: Marina Soko'`, `'uploaded_by: marina.soko@brookfieldcpas.com'`).
  - Tightening is correct and disambiguates the grader pass condition ✓.

**Lever 1 verdict: TRIGGERED end-to-end.** The prompt → OE → rubric chain is intact and the rubric evidence is grader-defensible. The persona-as-author trap that drove 5/6 failures in the original measured runs is preserved. (Minor fragility note: if Opus 4.8 reads OE06's phrasing as a memo template and replicates the role labels verbatim, the lever collapses to ~100% pass. The Hardness report's single-rubric-monopoly observation still applies.)

### Lever 2 — Email-subject-JE-id (rubric #5, NEW per Row 5)

**Trace prompt → OE → rubric:**

- **Prompt cue** (`5_Prompt.txt:6`): *"drop Matthew and Steven a quick email confirming the file is fully closed on the compliance side, CC Farah since she did the analyst work."*
  - **No mention** of subject line, JE id, filterability, traceability, reference, or correlation with the original alert.
  - The phrase "quick email confirming" naturally produces subject lines like *"Acme Cloud AML compliance file - close-out confirmation"* — which would **FAIL** rubric #5.

- **OE08 cue** (`6_Oracle_Events.txt:31-34`): explicitly demands *"subject referencing the Acme Cloud AML compliance close-out AND the JE identifier JE-acme_cloud-FP-2026-04-0052"*, with rationale *"for filterability"* in the Target Data field.
  - The OE encodes the requirement ✓ — but the OE only exists to specify the grader's expectation, not to teach the agent.

- **Rubric #5 evidence** (`7_Rubrics.json` rubric 5): *"The subject parameter of the email_send_email call to Matthew Li and Steven Perry contains the JE identifier JE-acme_cloud-FP-2026-04-0052 or an unambiguous equivalent (e.g., je_b2c2b939a1244823 or 'JE 0052'). A subject line that references only 'Acme Cloud AML close-out' without the JE id does not pass."*
  - Demands the exact step the prompt does not surface.

**Lever 2 verdict: HIDDEN TRAP (PROMPT_RUBRIC_MISMATCH).** The rubric's own justification reveals the gap: *"Matthew and Steven are sweeping their inboxes ahead of the partner review cycle; the JE id in the subject line allows them to correlate the close-out against the original alert without opening the message."* That reasoning belongs in the **prompt**, not the rubric. As written, the agent has no signal from the user's request that the close-out email is a correlation artifact rather than a confirmation message. A competent agent that writes a perfectly natural close-out subject ("Acme Cloud AML file — close-out confirmation") will fail rubric #5 for reasons external to the prompt's surface ask.

This is exactly the failure mode `Reference/Council_Protocol.md` B6 example calls out:
> *"During S3 rubric review, you notice the prompt's framing is implicit ... but the rubric set demands an explicit investigation step ... → flag PROPAGATE TO S1: prompt framing mismatch — re-frame the prompt to make the investigation step explicit, OR drop the rubric (do not silently keep both)."*

---

## B6 — Upstream propagation

### **PROPAGATE TO S1** (BLOCKING)

`PROPAGATE TO S1: prompt does not naturally surface the JE-id-in-subject requirement that rubric #5 demands -- _aux/Scratch_Corrected/5_Prompt.txt:6 -- either re-frame the close-out email sentence to imply filterability / correlation with the original alert ("...so they can thread it against the original alert"), OR drop rubric #5 from 7_Rubrics.json.`

**Two acceptable remediations:**

1. **Prompt edit (preserves the lever).** Rewrite line 6 to: *"...drop Matthew and Steven a quick email tagging the JE in the subject so they can correlate it against the original alert, confirming the file is fully closed on the compliance side, CC Farah since she did the analyst work."* This makes the JE-id-in-subject ask explicit. Re-run S2 (OE08 stays as-is) and S3 (rubric #5 stays as-is) against the updated prompt.

2. **Rubric drop (cheaper).** Remove rubric #5 from `15_Updated_Rubrics.json` and re-number subsequent rubrics. Rubric count drops 24 → 23, which leaves the task's lever diversity even thinner. The Marina-coordinator rubric (#13) becomes the dominant lever again — i.e., the single-rubric monopoly the HARDNESS report flagged remains the primary fragility. Materialization Row 5's stated purpose ("the lever's diversification intent is still met by Row 5's email-subject-JE-id rubric" — `_aux/Council_Reports/REVIEW_materialization.md`, Row 3 column) is **lost** if this remediation is chosen.

**Recommended path: option 1 (prompt edit).** This preserves the rubric-diversification intent of Row 5 while removing the hidden-trap defect. Without it, the corrected materialization regresses against the very fragility Row 5 was added to mitigate.

### No other PROPAGATE flags

- All persona references in the prompt (`Marina`, `Farah`, `Anita`, `Steven`, `Matthew`) are real personas in `_aux/Universe_Index/entities_personas.md` (Marina Soko: Compliance Officer; Farah Dlamini: AML Analyst; Anita Knowles: AML Supervisory Officer; Steven Perry: Managing Partner; Matthew Li: Accounting Services Partner).
- Persona-file `_aux/Scratch_Corrected/2_Persona.txt` correctly identifies Marina + supervisor Anita Knowles + scope — internally consistent with the prompt's framing.
- Steven Perry's stated role in OE06 ("engagement partner") matches the rubric #12 evidence ("engagement partner"). Universe index lists Steven as "Managing Partner" — but the rubric #12 evidence accepts both ("engagement partner," "managing partner," "final partner sign-off"). No drift.

---

## Cross-artifact consistency checks

### Entity drift sweep

| Entity / atom | Prompt | OE | Rubric | Universe (`entities_personas.md`) | Status |
|---|---|---|---|---|---|
| Marina Soko / `marina.soko@brookfieldcpas.com` | "I" (Marina, persona) | OE02, OE06, OE08-sender | rubrics #13, #19 | ✓ Compliance Officer | consistent |
| Farah Dlamini / `farah.dlamini@brookfieldcpas.com` | "Farah ran the analyst pass" | OE02, OE06, OE08-cc | rubrics #10, #20 | ✓ AML Analyst | consistent |
| Anita Knowles | "Anita" | OE02, OE06 | rubric #11 | ✓ AML Supervisory Officer | consistent |
| Steven Perry / `steven.perry@brookfieldcpas.com` | "Steven" | OE02, OE06, OE08 | rubrics #12, #18 | ✓ Managing Partner | minor role-label variance (OE/rubric say "engagement partner"; universe says "Managing Partner") — rubric #12 evidence accepts both; not blocking |
| Matthew Li / `matthew.li@brookfieldcpas.com` | "Matthew" | OE08 | rubric #18 | ✓ Accounting Services Partner | consistent |
| Acme Cloud / `acme_cloud` | "Acme Cloud" | OE01, OE05, OE06 | rubric #4 (variants Acme Cloud Solutions, Acme Cloud Inc.) | ✓ entity id | consistent |
| Channel `C008` / `#compliance-and-registrations` | "#compliance-and-registrations" | OE02, OE07 | rubrics #14, #15, #16, #17 | ✓ AGENTS.md | consistent |
| `thread_ts=1776969000.000000` | (implicit — "case thread") | OE07 | rubric #14 | ✓ universe | consistent |
| JE-acme_cloud-FP-2026-04-0052 / `je_b2c2b939a1244823` | (implicit) | OE01, OE06, OE08 | rubric #5 (alt: "JE 0052") | ✓ universe | consistent |
| `reminder_scen_041_audit_compliance_0000` | (implicit) | OE03, OE04 | rubric #2 | ✓ universe | consistent |
| `AICPA_SQMS_7Y` / `restricted` | (implicit — "appropriate retention and classification") | OE06 | rubrics #6, #7 | ✓ AGENTS.md valid codes | consistent |
| `acme_cloud_FP-2026-04` | (implicit — "earlier this quarter") | OE01 | rubric #8 | ✓ closed period | consistent |

**No entity drift detected.** All cross-artifact references resolve to the same canonical universe atom.

### Forward map (prompt ask → OE → rubric)

| Prompt ask (`5_Prompt.txt`) | OE step(s) | Rubric(s) | Status |
|---|---|---|---|
| "pull up the ledger entry and check that the cash posting lines are consistent with the documented CDD rationale" | OE01 (get JE), OE02 (search CDD trail) | rubric #1 (consistency finding in memo), rubric #22 (consistency in final response) | ✓ |
| "review whether the compliance file is fully closed out on our end" | OE03 (list reminders) | rubric #2 (delete reminder) | ✓ |
| "If anything is still sitting open, reminders, documentation gaps, anything that hasn't been properly put to bed, please take care of it" | OE04 (delete reminder), OE05 (list vault), OE06 (upload memo) | rubrics #2, #3, #8-#13 (memo content + author chain) | ✓ |
| "with whatever retention and classification treatment is appropriate" | OE06 (retention + classification params) | rubrics #6 (AICPA_SQMS_7Y), #7 (restricted) | ✓ |
| "post a brief recap under the case thread in #compliance-and-registrations" | OE07 (threaded reply) | rubrics #14 (thread_ts), #15, #16, #17 | ✓ |
| "drop Matthew and Steven a quick email confirming the file is fully closed on the compliance side, CC Farah" | OE08 (email send) | rubrics #18 (Matthew), #19 (Steven), #20 (Farah CC), #21 (body) | ✓ |
| **(implicit / absent)** — no surface ask for JE-id-in-subject | OE08 (Target Data adds JE-id-in-subject requirement) | **rubric #5 (REQUIRES JE id in subject)** | ✗ MISMATCH |

### Reverse map (rubric → OE → prompt ask)

Every rubric except **#5** traces cleanly back to a prompt-surfaced ask.

**Rubric #5 reverse trace:**
- Rubric → demands JE id in subject of email_send_email call.
- OE08 → demands JE id in subject (encoded in Target Data field).
- Prompt → silent on subject content beyond "confirming the file is fully closed."
- **Reverse trace fails at the prompt boundary.** The rubric and OE encode an ask that has no upstream origin.

### Implicit-vs-explicit framing check

The prompt is implicit about email-subject formatting. The rubric is explicit about it. Per L15/L16 framing constraint: this is a major mismatch. (Same finding as Lever 2 / B6, listed once with the integration-lens cross-reference.)

No other implicit/explicit framing mismatches detected. The prompt's implicit framing on retention/classification ("with whatever retention and classification treatment is appropriate") matches rubrics #6 and #7's expectations because the prompt explicitly delegates the determination to the agent — the agent is signaled to make the call.

---

## Cross-reference to prior reports

- `_aux/Council_Reports/REVIEW_hardness.md` flagged single-rubric-monopoly fragility. Row 5's addition of rubric #5 was the intended diversification fix. **The integration lens finds rubric #5 is not viable as-shipped** — it must be matched by a prompt edit (option 1 above), or the diversification is lost.
- `_aux/Council_Reports/REVIEW_materialization.md` Row 3 explicitly cites *"The lever's diversification intent is still met by Row 5's email-subject-JE-id rubric"* as the justification for dismissing Row 3. **That justification is invalidated** if rubric #5 is dropped (option 2). The prompt edit (option 1) is therefore strongly preferred to preserve the materialization-report's own dismissal rationale.
- `_aux/Council_Reports/REVIEW_triage.md` R8/R9 scores (lever diversity = 3, memo-rubric concentration = 3) projected raising to 5/5 by *"adding 2-3 rubrics that probe other levers"*. Rubric #5 was that addition; if the upstream-rooted defect drops it, R8/R9 stay at 3 and the salvage objective is incomplete.

---

## Detailed issue list (BLOCKER / MAJOR / MINOR)

| # | Severity | Perspective | Cross-artifact citation | Fix |
|---|---|---|---|---|
| 1 | **BLOCKER** | B6 + B4 (Lever 2) | `_aux/Scratch_Corrected/5_Prompt.txt:6` (no subject-line / filterability cue) ↔ `_aux/Scratch_Corrected/6_Oracle_Events.txt:31-34` (OE08 encodes JE-id-in-subject) ↔ `_aux/Scratch_Corrected/7_Rubrics.json` rubric #5 (mandates JE id in subject) | **PROPAGATE TO S1.** Re-frame prompt line 6 to imply filterability / correlation with the original alert. Recommended phrasing: *"...drop Matthew and Steven a quick email tagging the JE in the subject so they can correlate it against the original alert, confirming the file is fully closed on the compliance side, CC Farah since she did the analyst work."* Then re-run S2 (OE08 unchanged) and S3 (rubric #5 unchanged). Acceptable alternative: drop rubric #5 entirely; sacrifices Row 5's diversification intent. |
| 2 | MAJOR | B3 | `_aux/Trajectory_Stats.json` (measured 43.2 avg, 3/6 underflow 40) ↔ projected post-Row-2 midpoint 45-50 | THIN_DENSITY band. Acceptable because `_aux/Council_Reports/REVIEW_hardness.md` documented the per-task justification (*"flag for SALVAGEABLE path with explicit hardness-fragility note"*). No further fix required, but a re-run with different seeds is at risk of re-tripping density. If the operator wants to lift midpoint into the 50+ design-target zone, the cheapest move is to add 1-2 more grounded asks to the prompt (e.g., look up the existing FY2026 BO refresh memo as a format reference) — adds 1-3 tool calls and preserves the scenario. |
| 3 | MINOR | B4 (Lever 1) | `_aux/Scratch_Corrected/5_Prompt.txt:5` ("I coordinated the CDD package") ↔ `_aux/Scratch_Corrected/6_Oracle_Events.txt:24-27` (OE06 lists Marina as "CDD package coordinator") ↔ `_aux/Scratch_Corrected/7_Rubrics.json` rubric #13 (Pass/Fail examples per Row 6) | No fix required. Lever is triggered end-to-end. Row 6 tightening is correct. Hardness fragility noted: the first-person "I coordinated" phrasing remains the lever's load-bearing element, and a model that defaults to "Prepared by: Marina" will continue to fail. This is the **intended** trap — flagged here only so the cross-task Hardness Patterns Log records single-rubric-monopoly risk for re-runs. |

---

## Summary

The corrected materialization is structurally sound across persona / entity / channel / ID consistency, and Lever 1 (Marina coordinator role) is preserved end-to-end with Row 6's evidence tightening. However, the integration lens surfaces one BLOCKING defect: Lever 2 (email-subject-JE-id, NEW per Row 5) is a **hidden trap** — rubric #5 demands a step the prompt does not surface, and the rubric's own justification reveals the gap (the filterability/correlation reasoning belongs in the prompt, not the rubric). This must be resolved by a prompt re-frame (preferred) or rubric drop (sacrifices diversification) before the deliverable can ship.

Secondary finding: B3 projects 45-50 midpoint, sitting in THIN_DENSITY band. Acceptable under the HARDNESS report's per-task justification, but the task remains marginal on density — half the pre-iteration runs underflowed 40.

**Verdict: REVISE (1 BLOCKER, 1 MAJOR, 1 MINOR).**
