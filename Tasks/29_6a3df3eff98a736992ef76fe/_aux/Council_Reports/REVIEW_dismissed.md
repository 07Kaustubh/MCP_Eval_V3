# REVIEW — Candidate concerns considered and dismissed

Read-only audit trail of issues the strict-veteran reviewer **considered** during scoring and **dismissed** after re-checking the per-task universe. Recorded here so a future re-reviewer can see what was already examined and not re-litigate it.

## D1. "Prompt pre-states the answer" (L6 concern) — DISMISSED

**Concern:** The prompt body says "Supervisory and partner clearance are both in now, so the file should be ready to close" and "The disposition is settled, so relay it faithfully into the close-out record rather than reopening it." This pre-states facts that rubrics R5, R6, R7, R15, R16, R17 ask the agent to report.

**Re-check:** The prompt explicitly continues with "I would rather close it on the strength of the actual record than because an alert says the work is finished, so confirm the real state before we shut it" and "I would rather not take that on faith." The verification step is mandated, not optional. Run #3 in the trajectory set actually misread the universe trail and reported the review as OPEN, cascade-failing 11 of 17 rubrics. The discriminator works — the rubrics are not trivially echoable. This is the structural pattern of "confirm-already-done-but-with-a-twist" rather than the L1/L6 anti-pattern (the twist is the moot reminder, the stale Slack chatter about 6/18, and the FFIEC_5Y decoy).

**Verdict:** Not a defect. Unique Ground Truth stays 5 / 5; Investigation stays 5 / 5.

## D2. "Retention code is not enforced by any rubric" — DISMISSED

**Concern:** OE9 directs the agent to use `retention_policy_code = AICPA_SQMS_7Y` and resist the FFIEC_5Y decoy in email 0008, but no rubric explicitly tests the retention parameter on the vault upload.

**Re-check:** Rubric R3 (kind must be memo OR audit_evidence) blocks the most likely wrong-path (an agent that fell for the decoy would pick kind=bank_statement). FFIEC_5Y is not a valid code in the records vault retention-policy table (valid: AICPA_SQMS_7Y, IRS_TAX_7Y, FIRM_INTERNAL, INDEFINITE) — any agent that attempts to use FFIEC_5Y would receive a tool error rather than a successful upload, so the bad path is self-blocking at the tool layer. The four valid codes are substitutable for this control record (all are firm-recognized retentions); the only behavioral consequence of picking IRS_TAX_7Y or FIRM_INTERNAL instead of AICPA_SQMS_7Y is a slightly different retention horizon, not a wrong record. Adding a strict-AICPA_SQMS_7Y rubric would penalize valid agent choices.

**Verdict:** Not a defect. Overall Rubric Quality stays 5 / 5.

## D3. "Vault and final-response rubrics duplicate" — DISMISSED

**Concern:** R4–R7 (close-out record states X) and R14–R17 (final response reports X) appear to test the same facts on two surfaces, looking like padded coverage.

**Re-check:** The vault record is a persistent, restricted-classification artifact filed for FY2026 AML evidence retention; the final response is the agent's transient user-facing answer. These are two distinct deliverable surfaces with distinct evidence trails (the rubric evidence sections explicitly point to the upload `content` param vs the final-message text). The candidate's pattern of split-surface rubrics is the same anti-bundling pattern used in V3 reference tasks (Task14 splits vault content vs Slack content vs final-response). Not bundling; not duplication.

**Verdict:** Not a defect. Atomicity stays 5 / 5.

## D4. "Calendar rubric is too loose" — DISMISSED

**Concern:** R13 (schedule a future AML control-effectiveness review) accepts "any future date." Runs ranged 2026-09-03 → 2027-06-16, which is a 9-month window.

**Re-check:** The prompt itself says "set the next control-effectiveness review on the calendar as a recurring item, because the threshold calibration Steven flagged on this rule will come round again" — no specific cadence is named (annual vs quarterly vs ad-hoc). Universe state shows the prior cycle was 2026-06-03, suggesting annual cadence, but Steven's email also says "make sure threshold calibration is formally reviewed in the FY26 AML control-effectiveness session" — implying the calibration might happen sooner than the annual cycle. Pinning a specific date would over-constrain valid interpretations. The looseness matches the prompt's looseness — Unique Ground Truth is preserved at the action level (a future event must exist), not at the precise-date level.

**Verdict:** Not a defect. Unique Ground Truth stays 5 / 5.

## D5. "Scope disambiguator names may be fabricated" — DISMISSED

**Concern:** The prompt's scope-fix paragraph mentions "the Northstar adverse-media name match I have running alongside it" and "the quarterly partner sign-off control test." If those concurrent threads do not exist in the universe, the disambiguator is decorative rather than functional.

**Re-check:** Both grounded. Northstar adverse-media is `AML-REG-northstar-2025-001` (referenced in email + messaging + reminder universe rows; "soft-watch with Medium risk" disposition). Partner-sign-off control test is `event_scen_042_audit_compliance_0000` ("FY26 Q1 partner-sign-off control test working session") on the calendar. Both surface under the same compliance keyword searches the agent would run for the Acme wire review, so the disambiguator does real work — it tells the agent NOT to widen scope to those threads if compliance searches surface them.

**Verdict:** Not a defect. Truthfulness stays 5 / 5.

## D6. "Slack-chatter-vs-calendar inconsistency is a universe defect" — DISMISSED

**Concern:** The closing Slack message in C008 (msg `ca6b3a86…`, 2026-05-04) asserts "FY26 calibration session is now on the calendar for 2026-06-18." The actual `event_scen_041_audit_compliance_0011` is dated 2026-06-03 and no event exists on 6/18. This could be flagged as a Cross-service Coherence FAIL.

**Re-check:** The inconsistency is INTENTIONAL and load-bearing: OE7 explicitly tells the agent to "treat that as a prose claim to verify against the actual calendar state in OE11, not as established fact" and OE11 instructs the agent to trust the structured calendar over the chatter. This is exactly the Cross-service Coherence sub-dim's intended exception ("contradictions that break solvability or realism AND cause an agent failure" is the FAIL band; designed traps where the universe has a contradiction the prompt forces the agent to resolve are PASS). The trajectory data confirms: 6 / 6 runs correctly placed a future event after detecting the prior-cycle event was past.

**Verdict:** Not a defect — designed lever. Cross-service Coherence stays 5 / 5.

## D7. "Word count 379 > 300 sweet spot" — DISMISSED

**Concern:** Validator note flags the prompt is over the 300-word sweet spot.

**Re-check:** Sweet spot is advisory; the hard cap is 500 (Hard Rule 5). 379 is comfortably under 500. The extra length is doing legitimate work — the scope-disambiguator paragraph (which is grounded in two real concurrent threads, see D5) is what pushes the count up. Trimming it would lose Truthfulness anchors and risk Investigation 5/5 (the disambiguator is what tells the agent to ignore Northstar adverse-media + partner-sign-off test results when its compliance searches surface them).

**Verdict:** Not a defect. Feasibility stays 5 / 5.
