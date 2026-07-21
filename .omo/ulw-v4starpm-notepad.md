# Ultrawork Notepad — Extend the eval pipeline to V4 StarPM (no regression to V1/V2/V3), deterministic QC, version-scoped routing, fixed feedback flow
Started: 2026-07-21

## Mission (all steers folded in)
ONE pipeline at `/Users/kaustubhbhargava/MCP_Eval_V3` serves V1/V2/V3 (Brookfield). EXTEND in-place to also serve V4 (StarPM):
1. Zero regression to Brookfield. 100% parity.
2. Universe/docs/evals routing VERSION-SCOPED: StarPM task loads ONLY StarPM constants; no cross-universe pollution. (= agents isolated, verify vs SSOT only: per-task universe data + QC docs + evals.)
3. Binary QC DETERMINISTIC: structural parse + SSOT cross-ref. NO grep/substring-only.
4. Enforcement audit: pipeline must actually enforce Docs+Universe+Evals.
5. Rebuild reiteration/feedback flow (currently weak).
6. Ruthless veteran critique throughout.

## KEY PATHS
- V3 repo: /Users/kaustubhbhargava/MCP_Eval_V3 (git main).
- V4 SOURCE staged (read-only): /Users/kaustubhbhargava/MCP_Eval_V3/.omo/_v4_source/MCP_Eval_V4_StarPM/
- Raw truncated discovery outputs (re-read via Grep/Read offset, do NOT full-read):
  - routing map: /Users/kaustubhbhargava/.local/share/opencode/tool-output/tool_f84194fa6001eikKKlfhuk7g1V
  - StarPM constants+deltas: /Users/kaustubhbhargava/.local/share/opencode/tool-output/tool_f841955e1001v6YX0HjKJ2AH4V
- Base universe data: StarPM_Base_Universe/Data/Base_Universe_Complete_Data.json (5.2MB, 3892-record array). jq only.

## AGENTS
- Discovery DONE: bg_3ba05a04 (enforcement core), bg_f5365945 (routing), bg_2e44993e (StarPM+deltas).
- Oracle IN FLIGHT: bg_482dc4df (ses_07be33033ffeC8A4N7lBbvcrZX) — architecture review. BLOCKS implementation. Do NOT implement architecture until it returns.

## FINDINGS A — enforcement core (validate.py etc.)
- validate.py = 12 PROMPT + 9 OE + 21 RUBRICS checks. Classes: KEEP (D-STRUCT: dash ban, word cap<=500, JSON schema/array/object/field-presence, category enum, uuid, agent-centric title, outcome>=process, process<=50%), HARDEN (D-XREF but fragile: O7 tool-existence, R12 tool-in-title, R13 "at least N" vs prompt, R16-18 $/email/ID groundedness), REBUILD (FRAGILE grep: P5 tool-leak, P6 MCP-server, P7 internal-ID, O8/O9 param traps, R14 approximately, R15 or-similar), SOFT (HEUR: P8-12, O5 sparsity, O6 60%-verb).
- ALL Brookfield hardcoding concentrated in 2 files: validate.py (ID regexes :52-63, service/MCP names :54, tool literals :52/217/219, tool-defs path :49 = Brookfield_Base_Universe/8_Server_Tools_Details.json, fixed date :164, inline 60-verb tuple :193-203, param traps body->content/text->payload :217-220) and build_universe_index.py (12 <service>.<table>.json filenames + field-name assumptions + fixed date/tz :25/231).
- split_universe.py + data.py already universe-agnostic (source-driven). data.legacy.py = corruption hazard (shared Data/ dir + groups.get(source,[]) truncation). data.py refuses non-3_UniverseData files.
- Cross-ref checks fragile: Brookfield-shaped regex extraction + substring-in-concatenated-blob; SILENTLY skip if split dir / tool-defs missing.
- TWO convention SSOTs: Reference/{Strict,OE}_Convention_Inventory.json (documented, extracted from Task11-14) are NOT loaded by validate.py which re-inlines a divergent subset -> DRIFT.

## FINDINGS B — routing / context pollution
- Every runbook bootstrap = "read root AGENTS.md first" -> injects Brookfield "Universe constants" block (AGENTS.md:102-111) into EVERY fresh chat. #1 pollution surface, wholly Brookfield.
- Universe DATA routes per-task (_aux/Universe_Split from 3_UniverseData). Constants/cards/inventories/tool-defs/persona-source/reference-tasks do NOT route -> fixed Brookfield for any task.
- S2.md bootstrap itself hardcodes Brookfield param traps + retention codes (:64). Format cards = UA-rules + US-examples. OE_Convention_Inventory.json wholly US.
- 8 PIPELINE triggers: S0,HARDNESS,S1,S1.5,S2,S3,S4,REVIEW. <TASK_DIR>=repo-root folder name (find-replace). Ship => move folder to Submitted-Tasks/. _aux/=per-task work. _meta/=append-only cross-task logs.
- Stale: CHANGELOG.md + command workflow.txt use old Tasks/<TASK_DIR> convention. Prompt_Guidelines.md leaks "MoveOps" universe + "opus 4.5". Legacy transcripts (command workflow.txt, additional knowledge.txt, hardness.txt) carry MoveOps/Keystone literals.
- Reference tasks Task11-14 = Brookfield, baked into S1/S2/S3 bootstraps; both inventories extracted from them. New universe needs its own reference corpus.

## FINDINGS C — StarPM universe constants
- StarPM = Star Property Management (Texas residential property mgmt). 8 services w/ data + Files + Public = 10 Data folders.
- 268 tools / 8 servers: airtable 22, contacts 8, gcalendar 9, gmail 13, hubspot 14, linear 42, quickbooks 141, slack 19. (Brookfield=36). Naming e.g. `list_records_for_table` under `airtable` server (docs use `airtable_mock_*` infix -> MISMATCH between doc names and registry names).
- 7_Server_Tools_Details.json shape: {servers:[{name, tools:[{name, parameters:{p:{required,type}}, description}]}]}
- 8_Universe_Schema.json: 60 tables / 9 schemas (public,airtable,contacts,gcalendar,gmail,hubspot,linear,quickbooks,slack). ~27 ship empty.
- Data record shape identical to Brookfield: {source:"schema.table", row_data:{...}} -> split/index record-shape holds; table NAMES differ.
- PARAM TRAPS (differ + partially INVERT vs Brookfield): Slack content=`message` (BF=payload); Gmail=`body`/`htmlBody` (BF email=content) AND Gmail has ONLY create_draft (no send); Airtable comment=`text`; Linear comment=`issueId`+`body` (same as BF); QuickBooks writes=generic `properties` obj + `SyncToken` optimistic concurrency.
- Accounts NAME-based (7 accts, no AcctNum) -> BF 105000/120000 collision trap ABSENT; analog = name/entity collisions (Reyes, Okafor, Delgado, owner-as-person vs owner-as-LLC).
- Slack channels C001-C008 (#maintenance,#leasing,#general,#make-ready,#vendors,#owner-relations,#budget-review,#applications).
- NO retention codes, NO classification enum, NO JE state machine.
- Enums: Airtable make-ready selSched/selProg/selReady; Maintenance MT-2026-XXXX; Linear team OPS `OPS-N` states Backlog/Todo/In Progress/In Review/Done, projects proj_001-003; HubSpot leasing pipeline stages.
- Texas statutory ladder: 5-day grace -> late notice -> payment plan -> 3-day pay-or-quit -> eviction packet -> court (JP Patricia Lowe); 60-day renewal window; pass-through owner billing.
- DATA-vs-DOC discrepancy: docs narrate ~2-3x more records than shipped base seed (Airtable 170 vs doc 398; bills 113 vs doc 360; invoices 155 vs doc 318). Base under-seeded; FLAG.

## FINDINGS D — V4 framework deltas
- DUAL-MODEL: runs Opus 4.8 AND Gemini 3.5 Flash. => 8a_Verifier_Fails_Opus + 8b_Verifier_Fails_Gemini; Agent_Responses/{Opus,Gemini} subfolders; NEW human trajectory-rating step. (V3 was Opus-only single 8_Verifier_Fails.)
- NEW Evals/0_Injection_Quality_Eval.md: first-class universe INJECTION workflow via 9_Universe_inject.sql, gated by 7 structural checks (Schema, ID-format, Date/Time, Cross-Service Integrity, Naturalness/anti-AI-tell, Reachability, Pre-Solve) + 7-dim difficulty score (composite >=3.5). INVERTS Brookfield hard-rule "no universe edits".
- NEW Evals/5_Submission_Gate_Eval.md: zero-tolerance final gate, 6 defect families (F1 Impossible-w-Tools, F2 Persona/Date, F3 Process, F4 Broken/Over-Strict, F5 Illegal Tool-Output Deps, F6 QC-Pattern from 158-task audit). TOO_EASY = solvable <15 tool calls (vs BF 40+ floor). Model-agnostic on final deliverable.
- NEW Docs/13_QC_Companion.md: CONTAMINATED (StarPM title, Brookfield/Keystone examples: Acme, Northstar, retention codes, account numbers, Mia Hartwell). QC framework portable (UGT binary, Clarity, Truthfulness major-vs-minor), examples need re-port.
- Docs/8_QC_Spec_Doc2.md gutted 331->92L. 11_Taxonomy.md grew (new business functions + "2 models + Human Rating"). 4_Prompt_Hard_Tips.md ~identical (Opus version bump).
- Tasks_Template deltas: 8a/8b split, Agent_Responses/{Opus,Gemini}, 9_Universe_inject.sql changed, 3_UniverseData changed. 16 labeled QC_Tasks (Passed/True_Fails/Non_Fails/False_Fails_PT_Dispute_Accepted x4) = StarPM ground-truth test set + potential StarPM reference corpus.

## PROPOSED ARCHITECTURE (under Oracle review bg_482dc4df)
A. Universe descriptor Reference/Universes/<id>.json holding every hardcoded literal (base_dir, tool_defs_path, persona_source, reference_tasks, fixed_today+tz, id_grammars, param_traps per-tool, channels, enums(null for StarPM), index_tables map, density_floor(BF40/SP15), injection_enabled, models).
B. Auto-detect universe id from split source-set; persist _aux/universe.txt; --universe override; validators+runbooks read only routed descriptor.
C. validate.py: descriptor-driven; structural field-index membership (not substring-blob); unify convention SSOT; per-tool param traps; tool names from routed defs; FAIL-LOUD on missing SSOT.
D. build_index: descriptor index_tables map.
E. NEW phases PIPELINE INJECT (0_Injection_Quality) + PIPELINE GATE (5_Submission_Gate); dual-model S4.
F. Feedback_Protocol.md + structured feedback-artifact schema citing exact SSOT row/rule/criterion; isolated agents.
G. Move Brookfield constants out of root AGENTS.md into descriptor + per-universe card; bootstraps load routed card; split UA-rules from US-examples in format cards.

## SCENARIOS (THE CONTRACT — validator vs labeled fixtures)
- S1 PASS: validate over each QC_Passed/Task* -> PASS (no blocking mechanical violation). Surface: validator stdout. Test: pytest.
- S2 FAIL-DETECT: QC_True_Fails/Task* whose cited reason is MECHANICAL -> validator FAILS w/ matching category. Test: pytest per task.
- S3 NO-FALSE-POSITIVE: QC_False_Fails_PT_Dispute_Accepted/Task* -> validator must NOT emit the disputed check. Test: pytest per task.
- S4 REGRESSION+ROUTING: Brookfield V3 task (Submitted-Tasks/* or QC_Tasks/V3_Tasks/Task11-14) validates identically to baseline; StarPM task routes to StarPM descriptor. Test: pytest snapshot + routing unit test.
NOTE: validator covers MECHANICAL rules only; purely-semantic QC fails route to council/human (documented). Classify per QC_Feedback_Verdict during build.

## Plan (finalize after Oracle -> plan agent)
- [x] D1-D3 discovery
- [~] O1 Oracle architecture review (bg_482dc4df) — WAITING
- [ ] P1 plan agent: wave task graph + per-task verify
- [ ] E* execute per waves
- [ ] V1 verify vs 16 labeled QC tasks + Brookfield regression

## Now
Oracle running. Notepad pinned. NO implementation until Oracle returns. NO polling.

## Learnings
- User steers actively = refinement; fold in, don't restart.
- "no grep-only" is THE technical mandate -> structural + SSOT-crossref.
- Biggest regression traps: density floor 40->15, injection-inversion, param-trap inversion. Prove Brookfield unchanged via fixtures.


## FINDINGS E — QC ground-truth verdicts (CRITICAL corrections)
- CORRECTION: V4 QC_Tasks/* are BROOKFIELD-universe QC-CALIBRATION examples, NOT StarPM. (All cite brookfieldcpas.com, BlackLine, Oracle GL, acct 105000/101000, Acme/Northstar.) => they are (a) extra BROOKFIELD regression fixtures, (b) ground truth for the universe-AGNOSTIC QC scoring methodology. Oracle prompt mis-framed them as StarPM; correct via Oracle session ses_07be33033ffeC8A4N7lBbvcrZX after it returns (affects only Q3 regression-net + Q7 reference-corpus answers).
- StarPM has NO shipped end-to-end labeled tasks yet; StarPM validation = routing + split + index + deterministic validate over StarPM base universe/tools/schema (+ possibly author a StarPM reference task from the 16 QC methodology examples' shape).

### QC scoring model (universe-agnostic; the thing the pipeline must ENFORCE)
- Score bands: 5 = PASS; 3 = NON-FAIL (issues below fail threshold); 2 = FAIL.
- Buckets: QC_Passed(5) · QC_Non_Fails(3) · QC_True_Fails(2, dispute rejected/none) · QC_False_Fails_PT_Dispute_Accepted(QC said 2 -> PT disputed -> APPROVED -> Final raised 3/4/5). Last bucket = QC FALSE POSITIVES (S3 no-false-positive net).
- FAIL categories (threshold arithmetic = DETERMINISTIC given per-criterion severities): [Fail-10%+ Major Rubric Errors], [Fail-20%+ Minor], [Fail-15%+ Moderate], [Fail-Too Easy] (N runs pass when a criterion fixed / solvable < density floor), [Fail-Prompt Impossible Request], [Fail-Missing Universe Data].
- NON-FAIL categories: [Non-Fail-5-20% Minor], [Non-Fail-Up to 10% Major], [Non-Fail-Incomplete/Inaccurate/Minor OE], [Non-Fail-Persona Mismatch], [Non-Fail-Suspected LLM Cheating], [Non-Fail Minor Clarity/Specificity].
- Rubric-criterion tags (per-criterion, feed the thresholds): Incorrect Criteria, Missing Criteria-Outcome, Overly Specific, Overly Broad, Rubric Wording Errors, Non-atomic.
- DETERMINISTIC-vs-SEMANTIC split: threshold math + structural checks (atomic, agent-centric, category balance, uuid, at-least-N, groundedness, overly-specific channel-when-prompt-unspecified) = validator. Per-criterion severity classification + impossible-request + missing-data + persona-mismatch = council/human (validator SCAFFOLDS w/ SSOT, does not decide).
- DO NOT over-claim: validator cannot reproduce full 5/3/2 verdict; it enforces the mechanical floor + supplies SSOT-grounded scaffolding for the semantic layer.

### Feedback flow = PT-Dispute chain (the 'almost always bad' loop to fix)
- Chain: 9_QC_Feedback.txt (auditor) -> 10_PT_Dispute_To_QC_Feedback.txt (PT: 'Verdict: Disagree, Proposed Score: X' + point-by-point) -> 11_Final_QC_Validation_On_PT_Dispute.txt (QC: 'Decision: Approve/Reject') -> Final Score.
- GOOD-feedback pattern (model these): EVERY claim cites an exact SSOT artifact id (email_scen_059_wip_recognition_0000, BL-2BE9D12487D9, acct 101000 'Cash - Operating', rubric criterion #, OE#). Feedback_Protocol MUST mandate citation-per-claim + score-band arithmetic + isolated agents reading SSOT only.
- BAD-feedback (what to eliminate): ungrounded severity assertions, no SSOT id, no threshold math, cross-universe leakage.

## ARCHITECTURE OF RECORD (Oracle-blessed bg_482dc4df) — implement exactly
1. ROUTING: explicit declare = SSOT. S0 writes _aux/universe.txt from --universe arg / per-task manifest. Auto-detect = FAIL-LOUD GUARD only (hard-error on contradiction/ambiguity; StarPM+Brookfield share slack.*/linear.* -> never silent-infer). Do NOT overload 4_Changelog.json.
2. DESCRIPTOR SPLIT into 2 axes: (a) UNIVERSE FACTS (id shapes, param traps, channels, enums, tz, fixed_today) - keep THIN, DERIVE from 8_Server_Tools_Details.json + per-task data, not hand-mirrored 3rd SSOT; (b) FRAMEWORK PROFILE (density_floor, injection_enabled, models, phases/gates, TOO_EASY thresh) = V3-vs-V4 POLICY not universe. Bind task = (universe, framework). Today (brookfield,v3),(starpm,v4).
3. THIN-DERIVED: genuinely authored = fixed_today+tz, framework profile, wrong-alias trap hints (plausible confusions not derivable from tool-defs), leakage-shape list. Everything else derived. Drop universal-ID-grammar ambition; keep small leakage-shape list for prompt-leak check only.
4. TYPED CROSS-REF (replaces substring-on-blob): money->Decimal cents numeric compare (kills variants hack validate.py:301-313); email/id/date->exact case-normalized SET membership (fix substring bug :315); freetext(names/desc)->NOT grounded by validator (Council-A). Absent-legit vs hallucinated: keep money=WARN, email/id=FAIL; exemption signal = authored 'approximately'/'Conclude:' conventions.
5. FAIL-LOUD: validate.py silent-skips (:126-127 no split, :209-210 no tool-defs) -> hard FAIL. Golden harness MUST feed real split or fixtures flip PASS->FAIL (looks like regression).
6. PHASES: INJECT precedes S0 (writes 9_Universe_inject.sql, augments data, then S0 splits). Order: INJECT->S0->HARDNESS->S1/S1.5->S2->S3->S4->GATE. Dual-model S4 = one runbook, human-rating = new node (prepare 8a/8b + per-model AF + HALT). Density projection + TOO_EASY per-model (Opus vs Gemini differ).
7. PROSE = co-equal w/ code. Demote profile-specific root hard-rules (#4 no-edits, #11 40-floor) OUT of global block into routed profile/card; keep universals (500-word cap, no em-dash, no tool-names-in-prompt). Literal-lint greps runbooks/cards for 40 / retention codes / brookfieldcpas.com / trap words outside descriptor.
8. CONVENTION SSOT: descriptor canonical for hard_traps+enums; validate.py READS them, STOPS re-inlining divergent subset (:217-220,:193-203). *_Convention_Inventory.json -> per-universe REGENERATED style artifact for Council A (LLM) only. StarPM style seed = passing subset only; don't block launch on rich inventory.
9. FEEDBACK CONTRACT: structured finding {phase, deliverable, locus, check_id, severity, ssot_ref, observed, expected, suggested_action}. Resolved ONLY when re-run of that check flips RED->GREEN (no prose-only 'fixed'). Reiteration agent sees routed-SSOT + findings + deliverable ONLY (council reasoning advisory, never contract). Bounded iters, additive findings, escalate after N.
10. build_index needs per-universe summarization LOGIC (not filename map): schema-driven group-by/count over discovered categorical fields OR per-universe summarizer modules. accounts_per_entity:240-249 assumes account_number+entity_id -> breaks on StarPM name-based accts.
11. DATA-vs-DOC: declare SEED authoritative, docs non-authoritative narrative; add check flagging doc-only entities (else fat-doc-authored rubrics false-fail membership).
12. 13_QC_Companion contamination structural -> generate universe cards from agnostic TEMPLATE + descriptor; never hand-fork.

### WAVE PLAN (sequential; each gates the next; parallel WITHIN wave)
W0 Golden-master harness on Brookfield fixtures (no product change). Gate: harness green on current code.
W1 Descriptor + framework-profile scaffolding; populate Brookfield CURRENT literals; route Python to read them; ZERO semantic change. Gate: byte-identical Brookfield goldens.
W2 StarPM universe-facts (derived) + V4 profile; explicit-declare + auto-detect guard. Gate: Brookfield goldens identical; StarPM splits/indexes with ZERO Brookfield constants loaded.
W3 [HIGHEST RISK] substring->typed structural cross-ref; unify traps into descriptor; fail-loud. SHADOW MODE (log would-be verdicts, compare, then enforce). Gate: Brookfield verdict-equivalence + reviewed diff; StarPM/QC conformance.
W4 descriptor/schema-driven build_index (summarizer logic). Gate: Brookfield index golden identical; StarPM index non-empty.
W5 new runbooks INJECT(pre-S0)+GATE(post-S4)+dual-model S4. Gate: additive; Brookfield V3 path unchanged.
W6 prose de-literalization: split root hard-rules universal vs profile; runbooks read routed card; literal-lint. Gate: lint clean; spot-run each phase per universe.

### FIXTURE CORRECTION (carry, no Oracle re-consult)
16 QC_Tasks = BROOKFIELD QC-methodology calibration -> prove QC scoring logic + Brookfield behavior (NOT StarPM). StarPM acceptance = routing/isolation/deterministic-validate over StarPM_Base_Universe; NO end-to-end StarPM task exists yet (may author 1 StarPM reference task). StarPM style corpus cannot be seeded from Brookfield tasks.