# HARDNESS Cross-Source Verification - Tasks/38_6a5edd954557325b498168d1

## Sources consulted
- Per-task data :: `_aux/Universe_Split/` (airtable.airtable_records, quickbooks.quickbooks_entities, linear.linear_issues, slack.slack_messages, contacts.contacts) + `_aux/Fact_Ledger.json`. Orchestrator grounding battery confirmed every cited atom present: brooke.phillips@starpm.com; QB ids 101742946163 / 258920406326 / 103013736254 / 310712648304 / 340207319849; amounts 385.00 / 285.00 / 1340.00; MT-2026-1271 / MT-2026-1211 / MT-2026-1256 / EVF-2026-014; Unit-14 triple (Rio Bend / Sunset Ridge / Tanya eviction); Slack ts 1780067965 "cleared and ready"; Airtable "las palmas 8d" x6 / "mesa vista 4c" x3 / "rio bend" x10; pdf tokens 0. Also `_aux/Universe_Index/graph_report.md` + `_aux/Feasible_Surface.json` for the density map.
- Eval spec :: `Evals_starpm/` trajectory Tool Call Count dimension (floor >= 15; pipeline design target 50+ midpoint). Projected midpoint 55.0 (Playbook-fixed component ranges; corrected from an earlier 51.5 draft after Oracle skeptical review).
- QC spec :: `Docs_starpm/` StarPM density design target (avg 40+ tool calls per Docs_starpm/1; pass@1 <= 40%). Lever calibration from `Reference/Hardness_Playbook.md` (11-lever catalog + costs) and `Tasks/_meta/Learnings.md` (L8 three-service ~40% pass, L9 authority dismissal ~100% fail, L10 structured-DB skip, L23-L29 novel stumps).

## Eval spec sub-dims relevant to this phase
- Trajectory Tool Call Count (>= 15 floor; pipeline 50+ midpoint) :: projected midpoint 55.0, band PASS.

## QC spec sub-dims relevant to this phase
- Trajectory T1 Tool Call Count :: midpoint 55.0, PASS band (>= 50).

## Verification statements
- [x] At least 3 levers selected: 6 chosen (L8 3-system readiness contradiction, L9 Brooke Phillips authority dismissal, L10 Airtable-SoR + QB structured-DB skip, near-dup vendor-cost trap [L4/L23 near-miss + net-vs-gross Playbook #11; NOT Learnings L28, the Records-Vault tool-variant stump which is N/A in StarPM], L25 existing-output anchor, L14 water-heater flooring-escalation multi-link chain); each cites a Learnings entry or Playbook lever.
- [x] Density midpoint projection = 55.0, band PASS (one of {PASS >= 50, THIN 40-49, INSUFFICIENT < 40}). Post-Oracle-review correction: an earlier 51.5 draft inflated base/multi-write/L10 ranges beyond the Playbook-fixed costs and double-counted L25's 8D reads against L8; corrected to Playbook-fixed ranges (base 5-8, multi-write 9-12, structured-DB skip 4-7), de-overlapped L25 (net 1-3), and added the grounded water-heater multi-link chain as a 6th lever, honestly reaching 55.0.
- [x] Service breadth table populated (v11 G1): 7 distinct services each >= 5%, dominant (airtable) 27% < 60% - PASS.
- [x] Every cited record atom verified present in Universe_Split / Fact_Ledger via the orchestrator grounding battery (zero fabrication).
- [x] L6 check performed: the tested outcomes ($385 not $285, which 8D record is current, escalate to the flooring-vendor bill) are DERIVED, not stated; registry decoy-PDF landmine confirmed NOT instantiated (0 pdf tokens).

## Discrepancies surfaced
- The registry near-duplicate decoy-PDF landmine (`invoice-...-287.pdf`, `-920.pdf`, `agreement-...-tanya-mitchell-2.pdf`, `report-laspalmas-8d-qc-inspection-2.pdf`) is ABSENT from this per-task split (0 pdf tokens; Gmail carries only a `has_attachments` boolean). NOT a data error - equivalent hardness is instantiated at the record level (duplicate tblMakeReady rows, duplicate $1,340 QB bills). Documented as a hard constraint for S1 in Hardness_Plan.md.
- Slack carries near-verbatim disposition phrases ("8D officially cleared and ready" C004 ts 1780067965; "recommending a flooring vendor" C001). L6 risk flagged: S1 must frame the prompt as execute-the-write, never yes/no readiness.
- Tanya Mitchell Unit-14 contradiction is grounded but sits outside Carlos's four scripted scenarios; carried as an optional entity-confusion decoy only, not the spine.

## Verdict
PASS - 6 levers grounded and independently verified against the universe split, density midpoint 55.0 (PASS; every component sits within its Playbook-fixed band - the near-dup row is a near-miss / net-vs-gross blend, 54.0 even held to the strict 3-5 - after Oracle skeptical review), breadth 7 services (PASS), no INSUFFICIENT_LEVERS or INSUFFICIENT_DENSITY condition. Cleared to proceed to S1.
