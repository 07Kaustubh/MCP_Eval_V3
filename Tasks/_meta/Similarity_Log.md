# Similarity_Log

Append-only. One entry per 40%+ similarity hit caught by the platform linter.

## Schema

```
## Entry — Tasks/<TASK_DIR> — YYYY-MM-DD

**Linter excerpt:**
> <verbatim linter complaint, including similarity %>

**Matched-task reference:** <prior task id or descriptor>

**Pivot levers applied:** <which of the 6 levers from Reference/Similarity_Pivot.md>

**Outcome:** <Pending / Accepted / Re-blocked> — <one line if re-blocked, what the new linter response said>
```

## Entries

## Entry — Tasks/27_6a39fd19048f9213281ec7b — 2026-06-23

**Linter excerpt:**
> "Prompt Similarity. This prompt is too similar to an existing prompt:" followed by a Brookfield May close-period prompt (preparer disputing duplicate-entry exception, corrective reversal in flight against original reading, ask to block the action and escalate to deciders, surface recurring pattern). Internal `calc_similarity.py` scored only 3.4% lexical against Tasks/10; reviewer flag was therefore on archetype shape, not word overlap.

**Matched-task reference:** Tasks/10_6a2d9411aa26e656b0eff46b (vendor-payables variance / duplicate-entry exception / corrective reversal scenario)

**Pivot levers applied:**
- L2 (reactive → proactive trigger): dropped relay-from-colleague open; persona is now self-driving a pre-cert pass on the May close items.
- L3 (conflict type swap: variance-label dispute → precedent-validation audit): the agent no longer adjudicates "my read vs theirs"; instead it walks a four-pillar gating test (period / figure / cause / disposition route) on a prior-period precedent claim.
- L6 (workflow shape: linear → branching): replaces linear "investigate → escalate → flag pattern" with explicit branching — Path A (precedent carries → confirm + standby) vs Path B (precedent fails → route findings + notify approver + notify executor + reminder).

Hardness Plan levers P1 latching / P2 structured-DB skip / P7 multi-write / P8 multi-link chain / P9 universe-grounded gotcha / L9 authority dismissal overlay all preserved end to end (see `_aux/Linter_Decision.md` Round 2 for the per-lever mechanism check).

**Outcome:** Pending platform resubmit. Internal post-pivot `calc_similarity.py`: max 5.8% (Tasks/25, after Round 2 vault-anchor revise), 4.2% (Tasks/10) — all well under 40% ceiling. Per-phase exit gate cleared: Council A GO, Council B GO (density 46.5 midpoint, 3-write/3-service floor hit on both branches), AUDIT PASS (STRICT) after Round 2 REVISE iteration (single surgical fix: vault upload anchor added on both Path A and Path B per AUDIT's recommendation). Resolution within 3-round REVISE cap (Round 1 of 3 used). Five forward-looking S2/S3 hooks carried in `Tasks/27_6a39fd19048f9213281ec7b/_aux/Linter_Decision.md`. Ready for resubmit.

**Postscript — Round 3 (Class A persona role / authority, not a similarity hit):** After the Round 2 pivot + AUDIT vault-anchor exit but before platform resubmit, the platform's AI helper Brookfield Persona check flagged Ben's authority overstep on the Round 2 prompt ("pre-cert review", "clear this account", direct messaging to approver/executor, binary "precedent does not carry" determinations). The complaints landed — revised in place. Ben rebalanced to records-resource preparing findings; branching (L6) dropped; single linear path with upward escalation to George (his direct manager per persona master; also the senior who cited the wrong precedent, which sharpens L9). Post-Round 3 numbers: similarity max 5.6% (Tasks/25 WIP-recognition), 4.1% (Tasks/10) — well under 40% ceiling. Per-phase exit gate cleared again: Council A GO + Council B GO (density 45 midpoint, L24 soft-verb scoring R2 4/5 → R3 5/5) + AUDIT PASS (STRICT) with archetype overlap dropping from R2's ~30-40% to ~15-25%. Two REVISE iterations used within the 3-round cap. S2/S3 hook count grew from 5 → 8 (OBS A through H now in `Tasks/27_6a39fd19048f9213281ec7b/_aux/Linter_Decision.md`). Still pending platform resubmit.
