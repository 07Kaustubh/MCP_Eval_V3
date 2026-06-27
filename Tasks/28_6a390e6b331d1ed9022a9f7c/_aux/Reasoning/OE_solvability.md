# OE Solvability — Task 28_6a390e6b331d1ed9022a9f7c

## Deliverable
- `6_Oracle_Events.txt` — 19 OEs (18 tool-call OEs + 1 posture summary).
- Validator: PASS (0 fails, 0 warns, 1 note).
- Council A (grounding): GO at v4 (after v3 OE10 param fix + v4 AUDIT-driven OE8/OE12/OE13/OE14 fixes).
- Council B (adversarial QC): GO at v4. Completeness 5/5, Accuracy 5/5, B3 density PASS (mid 52), B4 hardness preservation 5/5.
- Strict veteran AUDIT: PASS (STRICT) at v2 after one REVISE iteration that corrected parameter overstatements on the write-tool OEs.

## OE-to-prompt coverage map

| Prompt clause (paraphrase) | OE(s) |
|---|---|
| May FX recon still open, blocking period lock | OE2 + OE4 |
| Ran currency refresh on 25th, $6,328.86 variance against GL | OE1 + OE2 |
| April / May USD/GBP rates 0.7191 / 0.7838; one Acme Research Ltd UK GBP subscription line missed April reval | OE1 + OE12 (JE biz_just) + OE17 (memo) |
| Workings already in Vault under cited title | OE6 (verify absent — phantom doc) |
| Past bd3 / bd5 / Andrea's partner sign-off missed last Friday | OE4 + OE5 |
| Land corrective entry today and close the recon | OE12 (stage only, draft) |
| Stage entry in right place against right period referencing the exception | OE12 (period brookfield_FP-2026-05; business_justification references exc_a0f77f2a19104e) |
| Update recon variance notes so next person doesn't retrace | OE13 |
| Add same reference into exception so Ryan can see corrective | OE14 (proposed_resolution / supporting_evidence) |
| Don't resolve exception (disposition is Ryan's) | OE14 (no state param passed; no resolve call) + OE19 |
| Formal note to Ryan with the picture + ask him to confirm | OE15 |
| Cc Daniel, Andrea, Hannah | OE15 |
| Short summary in close channel | OE16 (C005) |
| Fresh memo filed in Vault: reasoning + rate sources + reviewers + pull underlying invoice line | OE9 + OE17 (memo surfaces SAP/GL absence honestly) |
| Tag the way journal-entry support memos normally go | OE17 (kind journal_entry_support, retention AICPA_SQMS_7Y) |
| Push slipped May exception reminder to tomorrow | OE18 (reminder_scen_011_orphan_exception_0000 → 2026-06-13) |

Every prompt clause maps to ≥1 OE. No unmapped asks.

## OE-to-rubric mapping preview (S3 input)

| Rubric type | Source OE(s) | Notes |
|---|---|---|
| **Outcome 1.1 — write actions** (one per write) | OE12 (JE staged), OE13 (recon variances update), OE14 (exception cross-ref), OE15 (email send), OE16 (Slack post), OE17 (Vault upload), OE18 (reminder push) | Seven distinct write rubrics across seven services. |
| **Outcome 1.2 — write content** | OE12 (JE business_justification names exception, rate sources, classification question, SAP/GL absence), OE15 (email body covers recon + entry + classification + ask), OE17 (memo body covers reasoning + rates + reviewers + absence trail) | Content verification for the three highest-value writes. |
| **Outcome 2.1 — facts surfaced to user** | None directly. The prompt asks for execution, not for the user to be "told" a fact. Skip. |
| **Discovery / process** | OE1, OE2, OE3, OE4, OE5, OE6, OE7, OE8, OE9, OE10, OE11 are reads that downstream Outcome rubrics prove. No process rubrics indicated. Apply the three-condition test in S3 before adding any. | |
| **Posture (OE19)** | Aggregates the L1 + L9 + scope-write disciplines. Maps to existing Outcome rubrics on content (do not assert FX framing as resolved, do not invent Vault doc title, do not post into FP-2026-06, do not resolve exception). | |

## Hardness lever preservation

| Lever | Exercising OEs |
|---|---|
| L1 Latching (msg FX vs BL duplicate) | OE1 + OE3 + OE12 (biz_just) + OE15 (email) + OE17 (memo) + OE19 |
| L5 Thread-reply blindness (Hannah's VEN-441207 reply) | OE7 + OE8 + OE15 |
| L7 Multi-write diversification (7 writes / 7 services) | OE12-OE18 |
| L8 Multi-link chain (msg → BL → Slack → SAP → GL, 5-hop after OE10 add) | OE1 → OE3 → OE7+OE8 → OE9 → OE10 |
| L9 Universe-grounded gotcha (wrong-period + phantom Vault doc) | OE4 + OE5 (period) + OE6 + OE17 (retention) + OE19 |

All 5 levers traced end-to-end.

## Tool-call density projection
- Lower bound: ~36
- Midpoint: ~52
- Upper bound: ~65
- Verdict: PASS (≥ 50 design target). THIN_DENSITY watch-flag cleared at v3 by adding OE10 (GL history sweep).

## Verdict summary
- AUDIT v2: **PASS (STRICT)**
- All S2 exit criteria met.
- Ready for S3 (Rubrics) in a fresh chat.

## Iteration log
- v1 OE list (18 OEs): councils GO with THIN_DENSITY watch-flag (mid 48).
- v2 OE list (19 OEs, added OE10 GL history sweep): councils GO; Council A v2 BLOCKED on `oracle_gl_list_journal_entries` param overstatement.
- v3 OE list (OE10 param fix): councils GO; AUDIT v1 REVISE on OE12 + OE14 parameter overstatements (`entity_id`/`entry_date`/missing `description` on JE create; non-writable `related_journal_entry_id`/`corrective_journal_entry_id` on exception update).
- v4 OE list (OE8/OE12/OE13/OE14 fixes): councils GO; AUDIT v2 PASS (STRICT).
