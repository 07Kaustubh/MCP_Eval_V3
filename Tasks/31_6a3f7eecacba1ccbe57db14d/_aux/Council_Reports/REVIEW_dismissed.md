# REVIEW dismissed findings — Task 31_6a3f7eecacba1ccbe57db14d

These are findings the validator or a first-pass review surfaced but that, on per-task universe verification, do NOT warrant a row in `changes.md`. Documented here for traceability.

## Validator heuristic false positives

### Dismissed #1 — Prompt bolt-on warning on Hannah/Tom-routing sentence
**Validator:** `bolt-on candidate: sentence "Hannah has routed the federal return and the state filings to me for the partner sign-off..." shares no named entities with the rest of the prompt.`

**Verification:** The sentence introduces Hannah, Tom, the data package, the year-end trial balance, the recurring-treatment framing, and the not-released state. ALL referenced later in the prompt:
- "the draft summary" → Tom's draft (mentioned in subsequent sentence)
- "the data package" → referenced in "file the finalized return package in the vault"
- "year-end" → "still needs to be staged against the year-end"
- "nothing has actually been released" → "that signed authorization is not back yet and nothing has been e-filed"
- "the recurring lease and depreciation differences" → L9 authority dismissal anchor that the M-1 work must override

This is a setup-paragraph sentence, not a bolt-on. The validator's entity-overlap heuristic doesn't detect anaphoric/possessive references ("her note", "Tom's draft work"). Dismissed.

### Dismissed #2 — Prompt bolt-on warning on closing actions sentence
**Validator:** `bolt-on candidate: sentence "Once the reconciliation is settled and that entry is staged, file the finalized return package in the vault..." shares no named entities with the rest of the prompt.`

**Verification:** Same heuristic miss as #1.
- "the reconciliation" → "Schedule M-1" / "the reconciliation be built from what the underlying records actually show" (paragraph 2)
- "that entry" → "state tax provision true-up that still needs to be staged" (paragraph 3)
- "the retention we use for tax work" → `IRS_TAX_7Y` retention code (engagement convention from scen_068)
- "Northstar's managing partner" → the external client signatory the prompt explicitly named

The closing-actions sentence by definition references prior commitments. NOT a bolt-on. Dismissed.

### Dismissed #3 — OE 15 contact-lookup warning
**Validator:** `OE step 15: sends email to william.white@brookfieldcpas.com but no earlier OE step performs a contact lookup. Dependency chain: typically needs contact-lookup step before the send.`

**Verification:** OE 15 sender is William (the persona himself, no lookup needed), recipient is "Northstar's managing partner" (external, no stored contact — the rubric R9 explicitly accepts this with a role-addressed or Hannah-forwarded path). The "william.white@..." token the validator latched onto is the SENDER, not the RECIPIENT. The heuristic doesn't distinguish sender vs recipient. Dismissed.

### Dismissed #4 — Rubric evidence stricter than criterion (R1, R2, R3, R11)
**Validator:** `rubric[0,1,2,10]: evidence contains dates/IDs/amounts NOT in criterion: [list of derivation components].`

**Verification:** The criterion grades the DERIVED FIGURE; the evidence specifies the COMPUTATION COMPONENTS for the judge to recognize the agent's derivation path. Specifically:
- R1 criterion grades the M-1 difference ($131,135.84 or $156,433.43); evidence lists the cost base ($139,441.10 / $166,816.16) and book offset ($8,305.26 / $10,382.73) so the judge can verify the agent's math.
- R2 criterion grades the asset scope (14 / 23 / 10); evidence lists the cost totals and date bookends so the judge can verify the in-service window.
- R3 criterion grades the book depreciation offset ($8,305.26 / $10,382.73); evidence lists the FP period range (FP-2025-07 to FP-2025-12) so the judge can verify the summation window.
- R11 criterion grades the Slack note CONTENT (must mention the depreciation difference quantified from records); evidence lists the figures the agent might quote so the judge has the expected values.

These are intentional: the rubric accepts EITHER scope (150200-only or combined) AND any internally-consistent rate, so the title can't pin to one figure. The evidence pattern is `criterion = pass/fail check; evidence = derivation context for the judge`. This is the V3 reference pattern (see Task 11 / 12 rubrics in `QC_Tasks/V3_Tasks/`). Dismissed as a real issue; the heuristic correctly flags stricter-evidence cases but mis-flags this acceptable derivation-context pattern.

### Dismissed #5 — Dollar amounts not in Universe_Split (R1, R2, R3 derived figures)
**Validator:** `dollar amount $131,135.84 not found verbatim in Universe_Split` (and similar for $156,433.43, $24,150.54, $228,024.70).

**Verification:** These are COMPUTED values that the agent must DERIVE from the universe:
- $131,135.84 = $139,441.10 (cost) − $8,305.26 (FY2025 book dep)
- $156,433.43 = $166,816.16 (combined cost) − $10,382.73 (combined book dep)
- $24,150.54 = sum of all-period depreciation (decoy)
- $228,024.70 = sum of all FY2025+FY2026 IT additions (decoy)

The validator's verbatim-substring sweep only catches stored values. The Fact_Ledger.json was not present at validator time (note: `Fact_Ledger.json not present — falling back to raw blob substring match`), but even with the ledger built, computed derivations are NOT stored. The components ($139,441.10, $8,305.26, $166,816.16, $10,382.73) DO appear in the asset records and depreciation schedules. The derivations are valid. Dismissed.

## Trajectory-pattern observations (not findings, just context)

### Held-everything pattern (R8 + R9 + R10 cascade)
Runs 3, 4, 6 deferred multiple release actions despite the prompt's explicit "file...then get...over to" sequencing. This is the candidate's hardness mechanism working — the L9-reverse pattern (authority frame says "everything is ready", agent's discovery contradicts → over-corrects on caution). NOT a rubric issue. The agent has the literal instructions; choosing to hold despite them is the failure mode being measured. Designing around the held-everything pattern would lower difficulty below the 40% ceiling.

### M-1 cascade (R1 + R2 + R3)
4 / 6 runs failed all three together because they used the wrong cost base or wrong period filter. R1, R2, R3 are intentionally a tied triad — if you get the scope wrong, all three fall together. This is acceptable per QC spec: "Content-of-deliverable rubrics that reference the correct figure will cascade-fail when the figure is wrong. This is desired — do not consider it bundling." (Learnings.md L19). Per-rubric atomicity is preserved (each rubric tests one independent property: figure, scope, offset). Cascade-fail is a hardness signal, not a bundling defect.
