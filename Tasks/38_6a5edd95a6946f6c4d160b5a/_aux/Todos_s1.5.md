# S1.5 Todos — Tasks/38_6a5edd95a6946f6c4d160b5a

## Trigger
`PIPELINE S1.5 — Tasks/38_6a5edd95a6946f6c4d160b5a` + persona-scope linter complaint (Denise Morales → cross-portfolio brief to Aurora / Ridgeview CapEx / Tony-side coordination is Brooke's lane).

## Todos

- [x] Read S1.5 runbook + Linter_Playbook
- [x] Detect mode (CB) + classify block (Class A — persona-scope)
- [x] Skeptical-first check: score universe evidence on Denise's authoring guidance vs prompt scope
- [x] Verify Brooke's canonical brief maps 1:1 onto prompt's four asks (cross-portfolio ops sync, vendor billing recon, CapEx approval, owner reporting to Aurora)
- [x] Verify L9 mechanism (Tony's Sunset Ridge 208B AC Slack message) survives persona swap — Tony's post is public #maintenance C001, Brooke reads that channel
- [x] Classify verdict: Clearly Right → REVISE (persona swap Denise → Brooke)
- [x] Revise 5_Prompt.txt (linter's suggested text — drop "on my portfolio" possessive; rest unchanged)
- [x] Update 2_Persona.txt (Brooke Phillips / Apartment Property Supervisor)
- [x] Update PersonaBrief.txt (lift Brooke canonical section from StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md)
- [x] Run phase_ready.py --phase s1.5 → OK
- [x] Run validate.py --phase prompt → PASS (0 fails, 3 warns = coherence false positive on 3-item brief structure)
- [x] Fire Council A grounding sub-agent (bg_a7079949) — iter 1 REVISE (F1 BLOCKER: Ridgeview Linear issue nonexistent)
- [x] Fire Council B adversarial sub-agent (bg_018e83ea) — iter 1 PASS
- [x] Fire AUDIT sub-agent per S1.5 step 8 unconditional MANDATORY (bg_3c088edd) — iter 1 PASS (STRICT) but missed F1
- [x] Independently verify Council A's F1 via direct grep (231 Linear issues, zero roof matches → validated)
- [x] Apply iter-2 fix: retarget line 5 write from Linear to Airtable maintenance record
- [x] Re-run validator on iter-2 → PASS (0 fails, 2 warns down from 3)
- [x] Fire iter-2 Council A (bg_175c671e) — PASS
- [x] Fire iter-2 Council B (bg_0b9f7c2b) — PASS
- [x] Fire iter-2 AUDIT (bg_0de53999) — PASS (STRICT), all 4 write targets verified in per-write-target existence table
- [x] Write _aux/Linter_Decision.md documenting the two-iteration revise + reasoning
- [x] Append to Tasks/_meta/Audit_Log.md
- [x] Flag downstream cascade: OEs / rubrics / Hardness Plan reference "Denise" + "Linear write" — operator needs to re-run S2 / S3 / FINAL with Brooke + Airtable propagation OR trigger REDO if scenario architecture breaks too deeply
