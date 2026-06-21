# Linter Decision — S1.5

Task: `24_6a36e84723508b4e3f391cfc`
Linter run date: 2026-06-21
Class: A (persona consistency, not similarity)
Resolution: REVISE + JUSTIFY (mixed)

## What the linter blocked

The platform persona-consistency check flagged Lena Park (Procurement Officer) as the wrong persona for the prompt. Specific findings:

1. Lena is "deliberately separated from AP per segregation-of-duties controls"; the prompt had her pulling and triaging the full pending-approval AP queue across all three entities — which is Priya Khatri's (AP Coordinator) territory.
2. AP-coordinator-level fluency in the prompt (compound aging methodology, AP exception ticket terminology, orphan-approver routing diagnosis, 210000/219000 ledger family awareness) did not match Lena's procurement-officer profile.
3. Payables-channel posting and AP-routing ticket commenting were called out as Priya's operational outputs, not Lena's.
4. The Daniel-Jones escalation email was flagged as an unusual escalation path for Lena (claim: Lena coordinates with Priya and Marina, not direct to Daniel/Steven).
5. Engagement-record vault checks were called out as "outside Lena's lane".

Conclusion in linter output: "Mark as invalid" or pivot to Priya Khatri.

## What we did (REVISE)

Rewrote `5_Prompt.txt` to reframe Lena as the procurement-seat triage-and-handoff:

- Opening establishes WHY procurement is engaging: "They reach me because procurement owns the relationship, but the queue itself is on the AP side and that is not my call."
- Queue snapshot is explicitly non-decisional: information gathering before handoff, not ownership.
- Per-vendor root-cause classification is reframed as TRIAGE for cross-functional ownership ("first three are procurement's problem to fix; last two are AP's"). The fluency now serves the procurement-side angle (SOW currency, change-order status, scope-out-of-bounds) rather than AP-internal queue mechanics.
- All four writes are explicit cross-team handoff outputs:
  - Slack post FOR Priya and the AP folks (cross-team awareness, not channel ownership)
  - Linear comment WITH procurement-side evidence (cross-team INPUT to the AP-routing ticket, not ticket ownership)
  - Email TO Daniel cc Steven (the persona brief's defined escalation when procurement crosses into AP-disposition territory)
  - Personal reminder (self-only, no ownership claim)
- Closing broadens the SoD acknowledgment: "I am not approving or routing; Priya, Daniel, and Steven own that call."
- AP-coordinator jargon softened ("queue status field flattens..." removed; "compound aging methodology" replaced with plain-English "age against outstanding dollars together rather than top-dollar alone").

Word count: 470 (was 478). Validator: PASS (0 fails, 0 warns, 1 note).

## What we pushed back on (JUSTIFY)

See `_aux/Linter_Justifications.md`. The two linter claims we did NOT accept:

1. **Lena has no escalation path to Daniel.** Her base-universe persona brief explicitly names "Daniel Jones when an escalation crosses procurement into AP-disposition territory" as a key relationship.
2. **Engagement-record vault checks are outside Lena's lane.** Her brief lists "Records Vault vendor SOWs and PO packets" as Recent Activity and names SOW-lifecycle ownership as her core function. The Acme engagement evolved through an addendum and at least one change order — both governed by procurement's SOW lifecycle.

These two are why the persona stays as Lena (rather than pivoting to Priya, which would have required overwriting the user's pasted `2_Persona.txt` input).

## Council re-runs after revision

- **Council A v2 (Grounding + Convention):** GO. Persona-fit anchors verified in base brief (Lena's escalation path to Daniel; vault SOWs as Recent Activity; Acme addendum + change order under procurement's SOW ownership). All 5 Hardness levers verified preserved. No new ungrounded atoms.
- **Council B v2 (Adversarial + Density + Hardness):** GO. Persona/Business-function fit 4 → 5. All 5 levers preserved. Density midpoint 44 (unchanged from v1, well above 40 floor). Zero adversarial divergence on 4 targeted second-readings. Zero new phrasing hits.

## Final state

- `5_Prompt.txt` revised in place. Validator + both councils GO.
- Justification on file for the linter reviewer covering the bits we pushed back on.
- Ready to resubmit to platform linter.

If platform clears → `PIPELINE S2 — Tasks/24_6a36e84723508b4e3f391cfc`.
If platform still blocks → `PIPELINE S1.5 — Tasks/24_6a36e84723508b4e3f391cfc` with new linter output.
