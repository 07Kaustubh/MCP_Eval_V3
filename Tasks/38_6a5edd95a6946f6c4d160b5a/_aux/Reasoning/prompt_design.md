# S1 Prompt Design Report — Task 38_6a5edd95a6946f6c4d160b5a

**Phase:** S1  
**Persona:** Denise Morales (p_013, Onsite Property Manager)  
**Universe:** StarPM (Star Property Management, San Antonio TX)  
**Today:** 2026-07-01 (Wednesday)  
**Final word count:** 200  
**Validator result:** 0 FAIL, 3 WARN (all confirmed bolt-on false positives by AUDIT)

---

## Hardness levers engineered

| Lever | Surface in prompt | Expected stump mode |
|---|---|---|
| L9 — Authority-figure dismissal | Tony's Slack message ("probably a clogged filter, he'd get someone in Thursday") frames the answer before the agent checks | Agent latches onto Tony's verbal diagnosis and skips inspection-record pull; reports "clogged filter" without ground truth |
| L11 — Net-vs-gross | "the $8,400 approved scope" framed as owner exposure, but real billing picture requires cross-referencing invoice vs scope vs any extras | Agent reports $8,400 as the answer without netting down credits or verifying actual billed amount |
| L2 — Structured-DB skip | AC status and Ridgeview billing both require tool-layer queries (Airtable, Linear); conversational framing invites prose summary | Agent skips the query, synthesizes from narrative context only |
| L8 — Multi-link chain | Ridgeview billing: invoice → scope approval back-and-forth (Robert) → Airtable billing record → Linear issue — 4-hop chain | Agent stops after one source; reports partial picture |
| L6 — Near-miss entity | Tanya Mitchell has two universe records: Las Palmas 4B (correct) vs Sunset Ridge Unit 14 (decoy Airtable row) | Agent reports "Sunset Ridge Unit 14" from the decoy without verifying via Airtable rec ID |

---

## Prompt revisions

- **v1 → v2:** Added explicit investigation cues ("check what the current status really is", "figure out what the real owner exposure is", "look up her current status") to satisfy binary QC sub-dim "Investigation + Action". Validator WARN count held at 3 (bolt-on heuristic false positives, all load-bearing per AUDIT).

---

## Council verdicts

| Council | Verdict | Notes |
|---|---|---|
| A — Grounding | GO | All universe atoms verified; persona voice consistent; no internal IDs or tool names in prompt |
| B — Adversarial QC + Density | GO | 12/12 sub-dims at 5/5; density midpoint ~50 PASS; THIN_DENSITY watch-out flag propagated to S2/S3 |

---

## Similarity gate

- **Score:** max composite 24.6 vs `QC_Tasks/V3_Tasks/Task13`  
- **Result:** CLEAR (threshold < 40)

---

## AUDIT verdict

**PASS (STRICT)** — all 5 lenses clean.

- 3 validator WARNs confirmed false positives (bolt-on heuristic; all 3 sentences structurally load-bearing)
- THIN_DENSITY watch-out propagated: prompt midpoint ~50 is at the floor of the design target; S2 must add OE density shoulder to clear 50+ midpoint cleanly

---

## Carry-forward flags for S2/S3

1. **THIN_DENSITY:** Design at ~50 midpoint. S2 must not lose density in OE coverage — Ridgeview 4-hop chain and AC inspection pull are primary density drivers.
2. **L6 near-miss (Tanya Mitchell):** UGT is Las Palmas 4B (rec769c9f03f0b85f). S3 rubric must anchor on that specific unit and property, not just "Tanya Mitchell status".
3. **L9 (Tony's Slack):** S3 rubric binary guard must distinguish "reports Tony's verbal claim" vs "retrieves actual inspection status from Airtable/Linear".
4. **Gmail draft-only:** S3 write rubric must not require "sent" state — draft creation is the correct terminal action in StarPM.
