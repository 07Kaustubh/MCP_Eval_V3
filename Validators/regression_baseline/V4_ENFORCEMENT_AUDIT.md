# V4 Enforcement Audit - Evals_starpm/0 + 5 mandate coverage

Maps every hard gate in Evals_starpm/0_Injection_Quality_Eval.md and
5_Submission_Gate_Eval.md to its enforcement mechanism. DETERMINISTIC checks
live in Validators/v4_gates.py (invoked via validate.py --phase injection /
--phase submission_gate, v4-gated). COUNCIL items are emitted as explicit
COUNCIL note lines in the phase report so no mandate is silently dropped.

## Eval 0 - Injection Quality

| Mandate | Mechanism | Where |
|---|---|---|
| P1 Schema and structural validity (SQL parses, col/val counts, changelog JSON) | DETERMINISTIC | v4_gates.validate_injection [Eval0 P1 SCHEMA_VIOLATION] |
| P2 ID format and convention | DETERMINISTIC (StarPM ID shape classes) | [Eval0 P2 ID_VIOLATION] |
| P3 Date/time window 2026-05-01..2026-07-01, valid calendar dates, epoch ts | DETERMINISTIC | [Eval0 P3 TEMPORAL_VIOLATION] |
| P4A record collision (own primary id vs base) | DETERMINISTIC | [Eval0 P4 COLLISION] |
| P4A fact/status/amount/timeline/relationship contradiction | COUNCIL (semantic) | COUNCIL note in report |
| P4B broken cross-reference (ID not in base+injected) | DETERMINISTIC | [Eval0 P4 CROSS_SERVICE_VIOLATION] |
| P4B slack channel validity | DETERMINISTIC (registry slack_channels) | [Eval0 P4 CROSS_SERVICE_VIOLATION] |
| P4B email/mailbox validity for persona-domain addresses | DETERMINISTIC (registry personas) | [Eval0 P4 CROSS_SERVICE_VIOLATION] |
| P4B name spelling mismatch across services | COUNCIL (fuzzy identity) | COUNCIL note |
| P5 AI-tell counting rule (3+ fields = FAIL) | DETERMINISTIC (phrase/emoji census) | [Eval0 P5 AI_TELL] |
| P5 formality/length/register vs channel norms | COUNCIL | COUNCIL note |
| P6 orphaned record (no atom anchor to base/prompt/injection) | DETERMINISTIC | [Eval0 P6 ORPHANED] |
| P6 chain depth >5 tool calls | COUNCIL (needs tool-surface simulation) | COUNCIL note |
| P7 pre-solve: single injected field holds 3+ rubric-expected values | DETERMINISTIC | [Eval0 P7 PRE_SOLVED] |
| P7 NO_FRICTION (non-blocking) | COUNCIL (feeds difficulty) | COUNCIL note |
| P8 difficulty composite >= 3.5 | COUNCIL (semantic scoring) | COUNCIL note |
| P9 verdict: any gate failure = FAIL | DETERMINISTIC | Report status + exit code |
| STEP 0 TODO hard gate | N/A for validator (operator process step; runbook enforces) | Reference/Sessions runbooks |

## Eval 5 - Submission Gate

| Mandate | Mechanism | Where |
|---|---|---|
| F1 phantom tool names vs catalog | DETERMINISTIC (registry tool_catalog cross-ref) | [Eval5 P1 IMPOSSIBLE] |
| F1 foreign-universe service references | DETERMINISTIC (registry services) | [Eval5 P1 IMPOSSIBLE] |
| F2 persona-domain address not a persona/mailbox | DETERMINISTIC | [Eval5 P2 PHANTOM] |
| F2 future-dated expectations vs universe today | DETERMINISTIC | [Eval5 P2 MISMATCH] |
| F2 phantom entity IDs (absent from universe+injection+OE) | DETERMINISTIC | [Eval5 P2 PHANTOM] |
| F3 TOOL_GATE / QUERY_GATE process rubrics | DETERMINISTIC (pattern) | [Eval5 P3 TOOL_GATE] |
| F3 ALWAYS_PASS / ALWAYS_FAIL classification | COUNCIL (needs universe query result reasoning) | COUNCIL note (P6 list) |
| F3 outcome-first (process must not outnumber outcome; zero outcome = fail) | DETERMINISTIC | [Eval5 P3] / [Eval5 P6 6.2] |
| F4 BROKEN: expected amount absent from SSOT | DETERMINISTIC | [Eval5 P4 BROKEN] |
| F4 OVER_STRICT: valid alternative paths penalized | COUNCIL | COUNCIL note (P6 list) |
| F5 NEEDS_TOOL_OUTPUT dependency phrases | DETERMINISTIC (pattern census) | [Eval5 P5 NEEDS_TOOL_OUTPUT] |
| F6.1 atomicity (bundled verifiable values) | DETERMINISTIC flag + COUNCIL confirm | [Eval5 P6 6.1 NOT_ATOMIC] warn |
| F6.2 forward coverage (zero outcome rubrics) | DETERMINISTIC | [Eval5 P6 6.2 MISSING_CRITERIA] |
| F6.3 under-strict | COUNCIL | COUNCIL note |
| F6.4 destination consistency (prompt vs rubric channels) | DETERMINISTIC | [Eval5 P6 6.4 WRONG_DESTINATION] |
| F6.5 blank fields | DETERMINISTIC | [Eval5 P6 6.5 BLANK_FIELD] |
| F6.6 exclusion coverage | COUNCIL | COUNCIL note |
| F6.7 delegation clarity (I'll + imperative mix) | DETERMINISTIC flag + COUNCIL confirm | [Eval5 P6 6.7] warn |
| F6.8 UGT convergence signal | COUNCIL (trajectory-time, S4) | COUNCIL note |
| F6.9 OE authority contradiction | COUNCIL | COUNCIL note |
| F6.10 strict feasibility | COUNCIL | COUNCIL note |
| F6.11 strict date alignment | COUNCIL | COUNCIL note (deterministic window check covers explicit dates) |
| P7 verdict: PASS only if zero failures across families | DETERMINISTIC | Report status + exit code |
| STEP 0 TODO hard gate | N/A for validator (operator process step; runbook enforces) | Reference/Sessions runbooks |

Counts: Eval0 = 11 deterministic, 6 council, 1 n/a. Eval5 = 13 deterministic, 9 council, 1 n/a.
