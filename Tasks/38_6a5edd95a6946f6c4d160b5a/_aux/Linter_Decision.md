# Linter Decision — Tasks/38_6a5edd95a6946f6c4d160b5a

## Iteration history

This file records two consecutive S1.5 rounds on the same task.

- **Round 1 (earlier on 2026-07-22):** persona-scope block on the Denise-authored prompt. Resolved by REVISE — persona reseated to Brooke Phillips + prompt lightly re-voiced + Airtable retarget on the Ridgeview roof clause (Linear → MT-2026-047). Validator PASS, Council A PASS, Council B PASS, AUDIT STRICT PASS. See "Historical: Round 1" section below for the full record preserved for downstream traceability.
- **Round 2 (this round, 2026-07-22):** two fresh linter checks came back FALSE against the Brooke-reseated prompt. Resolved by INVALIDATE with justification.

---

## Round 2 (this round)

## Platform linter block
Class A — two separate checks pushed back on the current Brooke-authored `5_Prompt.txt`:

1. **Persona/scope check:** claimed the prompt is assigned to Denise Morales and the scope (Aurora briefing + Ridgeview roof + cross-portfolio brief) exceeds an Onsite PM's lane. Explicit closing line: "Return: FALSE. The prompt as written is assigned to Denise Morales."

2. **Business-alignment check:** six flags — (a) Sunset Ridge is not a Star PM property ("The five populated properties are Mesa Vista, Las Palmas, Las Vistas, Rio Bend, and Ridgeview"); (b) Tony Reyes is an NPC Lead Maintenance at a sister property; (c) cross-portfolio scope belongs to Brooke, not an Onsite PM; (d) Ridgeview roof billing reconciliation is Brooke's lane, not Denise's; (e) "her make-ready record" for Tanya Mitchell conflates tenant status with unit-turn status; (f) "current status" is not a named field in tblMaintenanceTickets.

## Skeptical-first decision

Ran targeted universe grep against `_aux/Universe_Split/*` before choosing between REVISE and INVALIDATE. Findings:

| Linter claim | Universe evidence | Verdict |
|---|---|---|
| Sunset Ridge is not a Star PM property | 30+ references across Airtable, Slack, Gmail, gcal, QB. MT-2026-063 (`recb...`) is the actual Airtable record for Sunset Ridge Unit 208B in `tblMaintenanceTickets`. Units 208B / 309C / 104B / Unit 14 all populated. Tanya Mitchell's payment plan records key to Sunset Ridge Unit 14. | **CLEARLY WRONG** |
| Tony Reyes = NPC sister-property Lead Maintenance | `tony.reyes@starpm.com` in `slack.slack_users.json` and `contacts.contacts.json`. Multiple internal `#maintenance` posts closing tickets; on-site tech for MT-2026-063. Internal staff, not NPC. | **CLEARLY WRONG** |
| Prompt is assigned to Denise Morales | `2_Persona.txt` + `PersonaBrief.txt` + `5_Prompt.txt` are all Brooke-authored per Round 1 fix. Linter appears to have scored against the earlier Denise submission. | **STALE** (linter running against prior submission) |
| Cross-portfolio scope exceeds Onsite PM lane | Brooke Phillips (Apartment Property Supervisor) authors now. Her canonical scope: cross-portfolio ops sync, vendor invoice approval, budget oversight, owner reporting, CapEx approval flow with owners. 22 gcal events pair Brooke + Aurora. | **STALE + WRONG on current persona** |
| Ridgeview roof billing outside Onsite PM lane | Brooke owns CapEx approval flow. $8,400 approved scope with Robert Finley + Pete Donovan is the Ridgeview Roof Section Repair authorization — supervisor-level ask, on brand. | **STALE + WRONG on current persona** |
| "Her make-ready record" for Tanya conflates tenant/unit | Airtable fldunit values: `"tanya mitchell - eviction track"`, `"tanya mitchell - delinquency escalation"`, `"unit 14 - tanya mitchell eviction"`, `"sunset ridge unit 14"` (Tanya-referenced). Records are subject-keyed on Tanya; "her make-ready record" reads unambiguously. Prompt also asks agent to confirm the unit reference on that record, which forces the disambiguation explicitly. | **WRONG** (reasonable natural-language framing against the records) |
| "Current status" not a field on tblMaintenanceTickets | Technically correct — schema is `fldPriority` / `fldDescription` / `fldTicketNumber` / `fldCompletionDate`. But natural-language "update the maintenance record with the current status" reads as an ask to update `fldDescription` to reflect what the inspection actually found (currently the description still carries Tony's outdated dirty-filter guess against a compressor-failure reality). The record target is unambiguous; field choice is routine agent judgment. | **AMBIGUOUS / SOFT** — not blocking |

Six of seven claims fail against the actual per-task universe data. The seventh is a soft technicality. No claim is Clearly Right in the sense the Playbook's REVISE branch requires.

Verdict: **linter is Clearly Wrong on the hard universe claims and Stale on the persona/scope claims.** Playbook decision path: **INVALIDATE with justification** (default for Clearly Wrong + Stale).

## Fix applied

No prompt edits. `5_Prompt.txt` remains the Round-1 Brooke-authored version (Airtable-anchored on the Ridgeview roof clause, 4 writes across 3 services, density midpoint ~50.5). Pushback authored to `_aux/Linter_Justifications.md`:

- Voice-gate check: `python3 Validators/check_justification.py ... _aux/Linter_Justifications.md` → **exit 0** (0 forbidden-term hits).
- Em-dash / en-dash scan → **clean**.
- Sentence count per section: 3-5 per section, one intro paragraph, no bullet abuse.

## Cross-task learning

Appended to `Tasks/_meta/Linter_Justifications.md`. This is the **3rd recorded instance of platform-linter-wrong-model** across three universes:

- Task 35 (2026-07-01): KeyStone linted with Brookfield rulebook.
- Task 36 (2026-07-02): MoveOps linted with KeyStone rulebook.
- Task 38 (this round): StarPM linted with a stale property allowlist that omits Sunset Ridge despite 20+ universe references.

Same class of platform bug, different flavor. Threshold from Task 35 was "≥ 2 more instances triggers platform-issue filing" — we are at 3 total. Recommendation logged: surface to platform on next occurrence.

## AUDIT step

**Skipped per Playbook.** Justification-only resolution — no prompt revision means no new artifact to audit. If the platform accepts the pushback, downstream 6_/7_ artifacts (still Denise-era per Round-1 note) still need OE + rubrics regeneration in fresh chats before upload.

## Voice gate

- `_aux/Linter_Justifications.md`: PASS (0 forbidden-term hits, 0 em/en dashes).

---

## Historical: Round 1 (earlier 2026-07-22, preserved for downstream traceability)

### Platform linter block (Round 1)
Class A — persona-scope mismatch on the prompt originally authored for Denise Morales (Onsite PM). Linter cited four points: (1) role stretch — cross-portfolio 3-property brief exceeds an Onsite PM's property-level scope; (2) reporting-line skip — direct Gmail to Aurora Winona (President) bypasses Brooke Phillips who owns owner reporting; (3) Tony Reyes cross-property reference elevated for a design-surface persona; (4) Ridgeview roof billing reconciliation + Linear update on a CapEx-adjacent job sits with Brooke.

### Skeptical-first decision (Round 1)
Ran targeted universe grep before defaulting to invalidation. The canonical persona reference produced unambiguous evidence:

- Denise's authoring guidance: property-level, single-property scope, modeled after Lisa's / Carlos's rooted patterns.
- Brooke's canonical scope: cross-portfolio operations sync, vendor invoice approval, budget oversight, owner reporting, CapEx approval flow with owners — 1:1 map onto the four prompt asks.
- Brooke's signature scenarios: `owner_capex_approval_roof` (leads, 8 actions), `owner_monthly_report_review` (leads, 7 actions), `owner_portfolio_review_midyear` (leads, coordinates with Aurora Winona directly).
- L9 hardness mechanism survives persona swap: Tony's Sunset Ridge 208B AC Slack message at ts 1782914700 is a public C001 (#maintenance) channel post, not a Tony→Denise DM. Discoverable by Brooke.

Verdict: linter was **Clearly Right** — unambiguous canonical-scope mismatch. Decision: **REVISE** (persona swap Denise → Brooke).

### Fix applied — iteration 1
1. `5_Prompt.txt` — dropped "on my portfolio" possessive, otherwise preserved.
2. `2_Persona.txt` — rewritten to Brooke Phillips / Apartment Property Supervisor.
3. `PersonaBrief.txt` — rewritten to Brooke's canonical brief.

Validator PASS (0 fails, 3 WARNs — coherence heuristic false positives on the 3-item structure).

### Iteration 1 councils
- **Council A grounding — REVISE.** F1 BLOCKER: prompt line 5 asked "update the Linear issue with the current status" for the Ridgeview roof job, but grep of `linear.linear_issues.json` (231 issues) returned zero roof-specific matches. Ridgeview roof reconciliation lives in Airtable + QB.
- **Council B adversarial — PASS.** 14/14 sub-dims at 5/5.
- **AUDIT strict — PASS (STRICT).** 12/12 sub-dims at 5/5, regression 61/61 PASS, density ~49, L9 preserved. AUDIT missed the F1 defect Council A caught.

### Fix applied — iteration 2
Minimum-touch retarget per Council A: line 5 `update the Linear issue with the current status once you have it` → `update the maintenance record on it with the current status once you have it`. Retargets the write from a nonexistent Linear issue to Airtable MT-2026-047 (Ridgeview roof ticket, `recb4aeaed326f156`). Rest unchanged.

Validator PASS (0 fails, 2 WARNs).

### Iteration 2 councils
- **Council A grounding — PASS.** F1 cleared.
- **Council B adversarial — PASS.** All 14 sub-dims 5/5.
- **AUDIT strict — PASS (STRICT).** 12/12 sub-dims 5/5. All 4 write actions verified. Density midpoint ~50.5. Regression 61/61 PASS.

### Downstream cascade required (still open after Round 2)

`6_Oracle_Events.txt` and `7_Rubrics.json` still reference **Denise Morales** as the persona and the **Linear write action** for the Ridgeview clause. Both must be propagated to Brooke + Airtable MT-2026-047. `_aux/Hardness_Plan.md` header + lever cost lines still say Denise; L7 write-diversification line still lists Linear. All Denise-era Council / AUDIT / FINAL / S4 reports are stale.

Operator options after the platform clears the prompt (Round-2 pushback pending):
1. Re-run `PIPELINE S2` + `PIPELINE S3` + `PIPELINE FINAL` in fresh chats — full downstream regeneration with Brooke + Airtable propagation.
2. If the Denise-era architecture cannot be cleanly re-propagated, invoke `PIPELINE REDO` on the task.

Do not upload the current 6_/7_ artifacts to platform — they are stale relative to the fixed prompt.
