# Linter Decision — Round 1 (2026-07-23)

## What the linter blocked

Property Operations business alignment check returned FALSE with five flagged issues on the S1 prompt for `Tasks/40_6a61a86a31b9c973b2021ba5/5_Prompt.txt`:

1. Diane Flores misattributed to Hill Country Plumbing (linter claim: her canonical universe row is at Lone Star Maintenance Supply).
2. Tony Reyes NPC sign-off authority (linter claim: Tony is an NPC Lead Maintenance at a sister property, cannot hold internal sign-off authority).
3. QuickBooks bill read is outside the Property Operations 1.2 tool matrix (linter claim: it belongs to Portfolio Coordination 2.2, Brooke's lane).
4. Direct cost heads-up to Robert Finley bypasses Brooke (linter claim: owner communication is Portfolio Coordination 2.3, Brooke's lane).
5. Scope-change escalation gate missing (linter claim: if the revised scope crosses the vendor-spend threshold, Onsite PM must loop Brooke before confirming with Hill Country).

## What we did

**Class A INVALIDATE — all five complaints.** No prompt revision. Justification-only resolution.

## Skeptical-first reasoning

Each of the five complaints was scored against per-task universe evidence before deciding invalidate vs revise.

Complaint 1 (Diane): the linter automatically reads any "Diane" as Diane Flores. Universe grep on the injected Gmail (record 7b, `ap@hillcountryplumbing.com` sender) shows the vendor summary is literally signed "Diane at Hill Country Plumbing" — a signature-only entity distinct from Diane Flores at Lone Star Maintenance Supply (who does not appear in the Mesa Vista thread). The prompt anchors the correct Diane with "their AP contact at Hill Country" precisely to disambiguate. This was the AUDIT F2 fix on v4. The linter's collision claim does not survive the vendor-anchor + role-anchor defense. INVALIDATE.

Complaint 2 (Tony): factually wrong. `tony.reyes@starpm.com` is a Star PM internal Lead Maintenance Technician per `contacts.contacts`. No "sister property" concept exists in Star PM (single-firm, ~45 employees, ~10 apartment properties, one shared `#maintenance` channel C001). Tony's authority to endorse plumbing scope in his home channel is on-role. INVALIDATE.

Complaint 3 (QB bill read lane): subjective lane restriction. Cross-service scope verification is a deliberately-designed part of the workflow — pulling a vendor's diagnostic write-up before confirming scope is a routine onsite-manager cross-check on an older unit. Not a Portfolio-Coordination-only tool call. INVALIDATE.

Complaint 4 (direct owner comms): subjective lane restriction. The heads-up to Robert Finley is a courtesy on a scope call the onsite manager is already carrying, on a property he owns. Owner-communication routing rules the linter cites are not universe-anchored. INVALIDATE.

Complaint 5 (escalation gate): the linter itself notes that the initial $310 scope is below threshold. The Brooke-loop suggestion assumes the revised scope will cross threshold, which is speculation about how the agent will read the diagnostic. The prompt does not commit to any specific revised dollar figure — it points the agent to the diagnostic bill and asks them to land the scope. INVALIDATE.

**Cost asymmetry:** invalidation is cheap (justification-only, no re-councils, no AUDIT re-run). Revision is expensive (new validator + Council A + B + AUDIT rounds) and risks weakening the six selected hardness levers, which were extensively documented in AUDIT_prompt.md as preserved end-to-end. When five of five complaints have plausible counter-evidence or are subjective, the skeptical-first default is invalidation across the board.

## Final state

- `5_Prompt.txt`: UNCHANGED (386 words, validator PASS, Council A GO, Council B GO, AUDIT PASS STRICT).
- `_aux/Linter_Justifications.md`: written (single Class A pushback, three paragraphs, four sentences per paragraph, cites `ap@hillcountryplumbing.com` and `tony.reyes@starpm.com` as concrete records).
- No AUDIT re-run (justification-only per S1.5 step 8 skip condition).
- Next steps: run `python Validators/check_justification.py Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Linter_Justifications.md` — exit 0 required. Resubmit the original prompt with the justification to the platform.

## Escalation note (cross-task pattern)

This is the 4th recorded instance of a platform linter false positive in the cross-task log (Task 35 wrong-universe rulebook, Task 36 wrong-universe rulebook, Task 38 stale StarPM property allowlist, Task 40 now). Task 38 and Task 40 are both StarPM, both had multiple flagged issues that did not survive per-task universe grep. Consider surfacing the pattern to the platform on the next occurrence.
