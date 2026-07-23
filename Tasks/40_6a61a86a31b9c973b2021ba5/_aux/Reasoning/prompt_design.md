# S1 Prompt Design — Task 40 (StarPM V4)

## Scenario
Water heater scope-correction at Mesa Vista Unit 7B on 2026-07-01 (Wed). Vendor Hill Country Plumbing quoted a narrow scope (exchanger + thermocouple swap ~$310) that materially understates the required work per the diagnostic bill's line description (full unit replacement recommended, ~$1850). Tenant Tanya Mitchell escalated Tuesday evening. Carlos Mendez (Onsite PM) needs the scope call closed today before Thursday's install slot.

## Levers engineered into the prompt (6 selected)
| # | Lever | Prompt surface | Universe atom |
|---|---|---|---|
| L1 | Latching | Mesa Vista Unit 7B specificity | Base universe Unit 14 water-heater incident (Tommy Reyes / Linda Castillo, 5/15-5/27, closed) as decoy |
| L2 | Structured-DB skip on QB | "actually go through Diane's diagnostic write-up on the bill itself and check whether the detail she has captured lines up with the summary" | QB bill B2026-211 Line[0].Description — "Full unit replacement recommended, approx 1850 dollars for equal model swap" |
| L5 | Thread-reply blindness | "I dropped an update into the tenant thread I had going but I have not touched the actual maintenance ticket yet" | Slack C001 tenant-update parent (Tue morning) + thread reply (Tue evening) — reply carries escalation content not in the parent |
| L7 | Multi-write diversification | 8 writes across 5 services in closing paragraph | Airtable ticket update / Linear issue update + comment / Slack thread reply / Gmail drafts (Diane / Tanya / Robert) / GCalendar event |
| L8 | Multi-link chain | Slack thread reply → Airtable ticket → Linear issue → QB bill line description | Records 3-4, 1, 5, 6 respectively — 4-hop chain |
| L9 | Authority dismissal | Tony Reyes's Slack post narrated authoritatively: "endorsing that scope, said the tank held pressure on the hold test and it keeps us on Robert's June budget" | Slack C001 record 2 (Tony's authority post) — Lead Maintenance Technician plausibly wrong on scope |

## Expected stump targets (per Hardness_Plan.md)
1. **[HIGH]** Agent conflates the resolved Unit 14 water-heater incident with the active Mesa Vista 7B; reports "already handled" and skips all 8 writes.
2. **[HIGH]** Agent accepts Tony's narrow-scope recommendation without reading the QB bill line description; drafts vendor / tenant / owner updates with the wrong scope.
3. **[HIGH]** Agent reads the Slack morning parent (medium priority framing) and skips the evening thread reply; priority stays at medium in Airtable and downstream drafts are toned down.
4. **[MED]** Agent lists Hill Country bills via `list_entities` but skims `TotalAmt`; skips `Line[0].Description` where the scope truth lives; recommendation cascades to wrong scope in all 8 downstream writes.

## Council verdicts across revisions
- **v1**: Council A BLOCK (A3 timeline "yesterday" mismatched injected Tony post at Mon 2026-06-29). Council B BLOCK (L9 regression from persona skepticism; L5 regression from escalation-content leak; Clarity/UGT ambiguity on Slack thread target; THIN density; minor timeline slip).
- **v2**: v1 issues addressed. Council B GO with THIN density carry. Council A still BLOCK on 2 A3 (Diane email "that night" vs injected Mon 15:12 CDT; "Yesterday morning I logged" vs injected Airtable Mon 21:14 CDT).
- **v3**: Prompt aligned to actual injected timestamps ("that afternoon" for Diane email, "The ticket went in Monday night" for Airtable creation). Both councils GO. AUDIT REVISE — 4 minor findings (Truthfulness/Clarity 4/5, THIN carry not documented, word count preference).
- **v4**: All 4 AUDIT findings fixed. Both councils GO. AUDIT round-2 PASS (STRICT).

## Final metrics
- Word count: 386 (under 400 sweet spot; under 500 hard cap).
- Em-dashes: 0.
- Tool names / MCP-server names / internal IDs: 0.
- Similarity max composite vs prior corpus: 29.1 (well under 40).
- Regression anchor suite: 48/48 PASS.
- Density projection: ~49-50 midpoint (THIN carry documented in Hardness_Plan.md per AUDIT F3).
- Service breadth: 8 distinct services.
- All 6 hardness levers preserved end-to-end.

## AUDIT verdict
**PASS (STRICT)** at round 2. All 12 Prompt sub-dims scored 5/5.

## Notes for downstream phases
- S2 OE authoring: the QB bill B2026-211 (record 6) Line[0].Description is the load-bearing source of scope truth. OE step for QB read must use `get_entity` (or equivalent line-expansion) rather than `list_entities` because line-description is not returned by list.
- S3 rubric authoring: 8 write actions decompose to 8+ atomic Outcome 1.1 rubrics (per StarPM V4 multi-recipient sub-rule + per Rubric Format card). No process rubrics needed for this trajectory (all 8 writes have verifiable end-state signatures).
- FINAL: verify Diane vendor anchor (`Hill Country` explicit) survives OE + rubric drafting; entity-drift risk against base-universe Diane Flores (Lonestar Account Rep) has been mitigated at prompt but not at OE / rubric layers yet.
