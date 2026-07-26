# Reads — S3 — Tasks/40_6a614767cd5b60ad96902fb4 (StarPM V4)

Reference docs consulted for rubric drafting. One line each per v11 E2 gate.

## Reference cards
- Reference/Rubric_Format.md :: FLAT 4-field schema {title, category, justification, evidence}; Outcome sub-types 1.1 (write-action result) / 1.2 (action content) / 2.1 (key fact in final response); three-condition Process test (default ZERO process); phrasing verbs; flexibility (approximately only for calc/rounded, never IDs/dates/exact amounts; "(or similar)" never near emails/IDs/dates); anti-patterns (passive voice, tool-name-in-title, bundling, at-least-N); threshold math + absolute-count gates (Major>=3 FAIL / Major+Moderate>=5 FAIL) active when rubric count < 30.

## QC / framework specs (StarPM)
- Docs_starpm/2_Rubrics_V3_Guidelines.md :: two categories only (Outcome default / Process rare); Outcome-first workflow; 1.1 for every write action, 1.2 if distinct content reqs, 2.1 only if user asked to be told a fact directly; atomic rubric per item for multi-write (never "at least N"); service metadata reqs (email: recipient+CC+content items; slack: channel+content items; linear: title+fields); Required Elements pattern allowed for single-action content; "approximately" only for calc/rounded; pass@1<=40% difficulty target.
- Docs_starpm/7_QC_Spec_Doc1.json (Rubric dimension) :: to be scored at Council B + AUDIT — Atomicity, Self-Containment, Completeness, Flexibility, Accuracy, Category Balance, Agent-Centric Phrasing.
- StarPM phrasing SSOT :: QC_Tasks/V4_Tasks/QC_Passed/Task1..4/7_Rubrics.json — delegated to explore agent bg_d33ab2e8 (distilling real-corpus voice, evidence-field shape, atomic split conventions).

## Task artifacts
- 5_Prompt.txt :: Lisa Smith wants Tanya Mitchell's Unit 14 turned around this week on the FALSE belief the holdup is cleared (owner signed off / nonpayment cleared / filing squared away); 5 asks — update make-ready record tight-and-true, post account status in make-ready channel, draft Brooke review email (do not send), set calendar reminder early next week, update the open ticket.
- 6_Oracle_Events.txt :: 19 OEs; 5 write actions (OE14 make-ready update held-at-Scheduled; OE15 slack #make-ready C004; OE16 Brooke draft; OE17 calendar 2026-07-06 on lisa.smith calendar; OE18 OPS-32 comment); OE19 = the 5 content facts binding the write actions.
- _aux/Fact_Ledger.json :: grounded atoms confirmed — records recc83c05d889b354 / reca8230a8fd9ff51 / rec94e86a3007dd5e (Rio Bend decoy); amounts 2132.00 / 185.00 / 75.00 / 8173.44 / 0.00; tickets EVF-2026-014 / DLQ-2026-0601; Linear OPS-32/38/54; emails brooke.phillips@starpm.com / tanya.mitchell@gmail.com / lisa.smith@starpm.com; slack C004; date 2026-07-06 Monday.
- _aux/Verification_s1.md + Verification_s2.md :: 4 S1 binding carries + 3 S2->S3 carries (dual write-target accept recc83c05d889b354 or reca8230a8fd9ff51, bar Rio Bend rec94e86a3007dd5e; QB bill QR-2026-0441 keyed on 2132.00 arrears + Tanya, not the Alamo HVAC decoy vendor; cross-service property-name variance).
