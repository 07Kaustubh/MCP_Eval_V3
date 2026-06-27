# Council Protocol

Every deliverable (S1 prompt, S2 OEs, S3 rubrics, REVIEW intake) must pass two councils before shipping. Validators run first as a cheap gate. Councils run after. Both councils must return GO with zero Major issues.

Each council is one sub-agent call but enumerates **multiple perspectives** in its prompt template. As of v13: Council A covers 13 perspectives (A1 Grounding, A2 Convention, A3 Narrative-State, A4 Action-vs-Universe-Prescription, A5 Persona Authorship, A6 Persona Scope, A7 Clarity & Specificity, A8 Truthfulness Tally, A9 Persona Fit, A10 Business Function Match, A11 End-to-End Solvability, A12 Cross-Service Coherence, A13 Open-Ended Write Ask Atomicity). Council B covers 11 perspectives (B1 QC Scoring, B2 Adversarial Alt-Path, B3 Tool-Call Density, B4 Hardness Preservation, B5 Tool-Leak / Phrasing Scan, B6 Upstream Propagation, B7 Per-rubric Cross-artifact Consistency, B8 OE Completeness, B9 OE Service Mapping, B10 OE Write-Action → Outcome 1.1, B11 Prompt Tell-me → Outcome 2.1). This is the "multi-council" coverage from every perspective without paying for separate sub-agent calls per perspective.

---

## Council A — Grounding and Convention

**Role:** verifies (a) every concrete claim is backed by per-task universe atoms [A1 Grounding], (b) deliverable structure matches V3 conventions [A2 Convention], (c) prompt's narrative state matches universe's actual lifecycle state [A3 Narrative State Consistency], (d) every action prescribed by the prompt is consistent with the universe record's prescribed actions or includes explicit override language [A4 Action-vs-Universe-Prescription].

**Tool:** `explore` sub-agent.

**Inputs:**
- The deliverable file
- `_aux/Universe_Split/*` (the only universe source of truth)
- `_aux/Universe_Index/*` (cheap lookups)
- `Reference/<Prompt|OE|Rubric>_Format.md`
- `Reference/Strict_Convention_Inventory.json` (rubric phase)
- `Reference/OE_Convention_Inventory.json` (OE phase)
- 2 to 3 sample V3 reference files for the phase

**Perspectives covered (single prompt template, both must pass):**

### A1 — Grounding sweep
For every dollar amount, email, JE id, exception id, recon id, vendor id, AP invoice id, document id, Linear issue id, Airtable record id, account number, retention code, classification, persona / NPC name, period id, and date in the deliverable, confirm the value appears in `_aux/Universe_Split/`. For each: `VALUE → FILE:RECORD_INDEX (or NOT FOUND)`.

### A2 — Convention sweep
Compare the deliverable's structure (phrasing patterns, field shapes, qualifier usage, opening-phrase patterns, parameter-naming conventions) against:
- `Reference/<phase>_Format.md`
- The relevant inventory file (`Strict_Convention_Inventory.json` for rubrics, `OE_Convention_Inventory.json` for OEs)
- The sample V3 reference files.
Flag any structural drift.

### A3 — Narrative State Consistency (prompt + OE phase)
For every STATE-IMPLYING claim in the deliverable (verbs like "is wrapping up", "before X finalizes", "is pending review", "approaching the SLA", "the dispute is unresolved", "the period is open", "the certification is in progress", "still awaiting approval"), identify the underlying universe record AND verify the prompt's claimed state matches the universe's ACTUAL lifecycle state. Use `_aux/Fact_Ledger.json` lifecycle atoms first; fall back to `_aux/Universe_Split/` records.

Common contradictions to catch:
- Prompt says "X is wrapping up" but universe shows X's completion email/timestamp dated BEFORE today.
- Prompt says "the period is open" but universe shows the period locked.
- Prompt says "SLA approaches" but universe's today has already passed the SLA.
- Prompt says "dispute is unresolved" but resolution_status = resolved.
- Prompt says "certification in progress" but the sign-off email is in the record set.

Output per claim: `STATE CLAIM "<quote>" -> CONTRADICTING RECORD <file>:<row_id>` (or `CONSISTENT`). Any contradiction = BLOCK.

### A4 — Action-vs-Universe-Prescription (prompt + OE phase)
For every action verb the deliverable asks for (send, post, create, approve, dismiss, escalate, override, reclassify, void, certify), identify the relevant universe record AND check if the record has a field that prescribes a DIFFERENT action (`proposed_resolution`, `recommended_action`, `next_step`, `assigned_to`, `expected_action`, `proposed_action`).

Decision:
- Record prescribes action X, prompt asks for Y, prompt EXPLICITLY says "override the proposed resolution because Z" → ACCEPT (intentional override with justification).
- Record prescribes action X, prompt asks for Y, prompt SILENT on the divergence → FLAG as `ACTION_DIVERGENCE: <prompt action> vs <universe prescription> at <file>:<row_id>`. BLOCK.

Same rule for authority/permission collision: if the prompt asks persona A to do X but the universe shows A lacks the role/permission/authority (e.g., AR clerk overriding a completed partner sign-off without explicit grant), flag as `AUTHORITY_GAP: <persona> -> <action> at <file>:<row_id>`. BLOCK.

This perspective prevents the Unique Ground Truth failure where two valid end-states exist (the prompt-prescribed and the universe-prescribed) without disambiguation.

### A5 — Persona Authorship Whitelist (prompt phase)
Read `Brookfield_Base_Universe/2_Persona_Briefs.md` end to end. The file enumerates the 28 authoring personas — the only personas valid as the TASK AUTHOR (the voice issuing the prompt). Verify the persona assigned in `Tasks/<TASK_DIR>/2_Persona.txt` matches one of the 28 by name AND role.

Negative blocklist (caught by `Validators/validate.py`): Owen Mercer, Brenda Abbas, Sofia Halabi, Farah Dlamini, James Randall, Lucia Ferreira, Mateo Kovac. These are NPCs — counterparties / participants in scenarios, never task authors.

This perspective performs the POSITIVE-whitelist check the validator cannot: the validator only catches the 7 known NPCs by name; A5 catches assignments to ANY persona absent from the 28-authoring list (including personas hallucinated from the universe). Output: `PERSONA <name> -> POSITION_IN_AUTHORING_LIST <n>/28 (or NOT_IN_LIST)`. NOT_IN_LIST = BLOCK with reason "persona is not in the 28-authoring set per 2_Persona_Briefs.md".

### A6 — Persona Scope (prompt + rubrics phase)
When the prompt uses possessive scope ("my X", "our X", "my vendors", "my open POs", "my drafts", "the items in my queue"), the scope is bound to the PERSONA's universe assignments — not the firm's full inventory. For every rubric value that is universe-grounded (vendor_id, JE_id, exception_id, recon_id, amount, recipient), verify the value belongs to the persona's assignment scope per `_aux/Universe_Split/`.

How to verify the scope: read the persona's role from `Brookfield_Base_Universe/2_Persona_Briefs.md` + the persona's assigned entities/queues/owners from `_aux/Universe_Split/` (e.g., `journal_entries.json` rows where `created_by` or `owner_email` = persona email; `ap_invoices.json` rows where `approver_email` = persona email; etc.). Build the persona's assignment set.

For each rubric value: if the value is in the persona's assignment set → PASS. If absent → FLAG as `SCOPE_DRIFT: rubric[i] tests <value> NOT in persona scope. Either the prompt's "my X" framing is wrong, or the rubric tests a value the persona has no claim to.` BLOCK.

Exception: if the prompt explicitly broadens scope ("our entire vendor master", "across all entities", "firm-wide"), persona scope does not apply — record as `SCOPE_OVERRIDE` and move on.

### A7 — Clarity & Specificity holistic read (prompt phase)
Re-read the prompt as a first-time recipient with NO context from this council session. Ask: (a) can the request be reasonably interpreted in two materially different ways that lead to different write actions? (b) are major details missing that the agent cannot reasonably infer from the universe? (c) is the persona's intent recoverable from the prompt alone, or does it require reading their inbox / role / past tasks?

Output per ambiguity: `CLARITY_GAP: <one-line description> -> reading A produces <action set>, reading B produces <action set>. Fix: <how to disambiguate>`. Mark as MAJOR if both readings produce different write-actions; MINOR if both readings produce the same write-actions but different framing in the response.

This perspective catches the Prompt Clarity & Specificity 1/3/5 NON-FAIL middle band where the prompt has a leading interpretation but is reasonable in two ways.

### A8 — Truthfulness deep tally (prompt phase)
For every factual claim in the prompt, classify as MAJOR (claim is core to the request — wrong = the prompt is unanswerable / leads to wrong action) or MINOR (claim is incidental / context-only). Tally:
- 1+ MAJOR factual error = FAIL
- 2+ MINOR factual errors = FAIL
- exactly 1 MINOR error = NON-FAIL

Source of truth: `_aux/Fact_Ledger.json` + `_aux/Universe_Split/`. For each error: `TRUTHFULNESS_ERROR: severity=<MAJOR|MINOR> claim=<quote> actual=<value from universe>`. Closes the "no irrelevant-statement check" gap in the existing A1 grounding sweep.

### A9 — Persona Fit Comparison (prompt phase)
Read `Brookfield_Base_Universe/2_Persona_Briefs.md` end-to-end. For the assigned persona, grade prompt-fit 1-5. Then identify any OTHER persona from the 28 that would fit the prompt BETTER. If a better fit exists, output:
`PERSONA_FIT_MISMATCH: assigned=<name> (fit=<n>/5) better_candidate=<name> (fit=<n>/5) reason=<one-line>`.

Decision: better-fit candidate with delta ≥ 2 = NON-FAIL (Persona Mismatch). Delta = 1 = NOTE. No better fit = PASS. Acceptance rule: CBs may swap persona for a better-fitting one (without changing assigned business function), so flag for operator-decision, not auto-block.

### A10 — Business Function Match (prompt phase)
Read `Docs/5_Prompt_Diversity_Business_Function.md` (or `Brookfield_Base_Universe/3_Task_Categories_Business_Functions.md` as fallback) to enumerate the 10 Brookfield business functions: Accounting Operations, Bookkeeping, Tax, Compliance & Internal Controls, Audit, AP / Vendor Operations, BlackLine Close-Discipline & Variance, Engagement Mgmt & Client Operations, Executive / Partner Oversight, HR & People Operations.

For the assigned business function, verify the prompt's primary scenario is genuinely within that category. Output: `BUSINESS_FUNCTION: assigned=<n> prompt_primary=<n> match=<true|ambiguous|false>`. Ambiguous (could reasonably belong to either) = NON-FAIL. False = consider escalating to BLOCK (since CBs cannot change assigned business function).

### A11 — End-to-End Solvability (prompt + OE phase)
Walk the dependency chain from `_aux/Hardness_Plan.md` (the projected agent trajectory). For each step, verify the required source row is materialized in `_aux/Universe_Split/`. Specifically: every contact lookup resolvable, every JE / exception / recon / invoice / vendor id present, every fiscal period / account / Slack channel valid. The Fact_Ledger groundedness sweep proves named atoms EXIST; this perspective proves the FULL DEPENDENCY CHAIN connects.

Output per missing link: `SOLVABILITY_BREAK: step <n> requires <link> NOT MATERIALIZED in <expected source>. Without this link the task is not end-to-end solvable.` BLOCK.

### A13 — Open-Ended Write Ask Atomicity (rubrics phase)
When the prompt has an open-ended write ask ("create tickets for all follow-up items", "send emails to anyone affected", "update all the records that need it"), the rubric set must contain ONE atomic Outcome rubric per ground-truth item, NOT a single "at least N" rubric.

How to verify: identify open-ended write asks in the prompt (regex hints: "all the", "for each", "anyone who", "every", "all" + plural noun). For each ask: count the number of ground-truth items from `_aux/Universe_Split/` that match the criterion (e.g., for "create tickets for all open AP exceptions on Acme", count `blackline_exceptions` rows where entity_id = acme_cloud AND status = open). Verify the rubric set has ≥ that many distinct atomic rubrics, each tied to a specific ground-truth item.

Output per gap: `OPEN_ASK_BUNDLED: prompt asks "<open-ended quote>" with <N> ground-truth items, but rubric set has <M> atomic rubrics (M < N). Replace any "at least N" rubric with N atomic per-item rubrics.`

Exception: when the ground truth is genuinely indeterminate (the prompt asks the agent to apply judgment on which items qualify), "at least one" is acceptable. Record as `OPEN_ASK_INDETERMINATE` and move on.

This perspective enforces the QC spec rule: "When the prompt asks for multiple write actions of the same type, write one Outcome rubric per item grounded in ground truth — never bundle into 'at least N' thresholds. 'At least N' is reward-hackable."

### A12 — Cross-Service Coherence (universe phase)
For each key entity that appears in 2+ services (persona email in contacts + journal_entries.created_by; vendor in vendors + ap_invoices; recon in blackline_reconciliations + journal_entries; client in clients + email threads + Slack channels), verify name + ID + date consistency across services. Universe edits (per `_changelog` if present) must not have introduced cross-service contradictions.

Output per contradiction: `CROSS_SERVICE: entity <name> referenced as <value_A> in <service_A> but <value_B> in <service_B>. Either edit is inconsistent or service B is stale.` BLOCK if the contradiction would cause an agent failure (e.g., the rubric expects value_A but the agent sees value_B in their primary lookup path).

**Prompt template:**

```
You are Council A — Grounding and Convention.

DELIVERABLE: <path>
PHASE: <prompt | oe | rubrics>
PER-TASK UNIVERSE: Tasks/<TASK_DIR>/_aux/Universe_Split/
INDEX: Tasks/<TASK_DIR>/_aux/Universe_Index/
FORMAT CARD: Reference/<phase>_Format.md
INVENTORY: Reference/{Strict_Convention_Inventory.json | OE_Convention_Inventory.json}
SAMPLES: QC_Tasks/V3_Tasks/Task11..Task14/{Rubrics.json | Oracle_Events.txt | Prompt.txt}

TASK:

[A1 — Grounding] For every concrete claim in the deliverable, verify against
the per-task universe split. Output: VALUE -> FILE:RECORD_INDEX (or NOT FOUND).

[A2 — Convention] Compare structure against the format card, inventory, and
sample V3 references. Flag any drift.

[A3 — Narrative State Consistency] For every STATE-IMPLYING claim in the
deliverable (verbs like "is wrapping up", "before X finalizes", "is pending",
"the period is open", "the dispute is unresolved", "the SLA approaches"),
identify the underlying universe record AND verify the prompt's claimed state
matches the universe's ACTUAL lifecycle state per Fact_Ledger.json + Universe_Split.
Output: STATE CLAIM "<quote>" -> CONTRADICTING RECORD <file>:<row_id> (or
CONSISTENT). Any contradiction = BLOCK. Common contradictions: completion
email dated before today contradicting "in progress"; period locked
contradicting "open"; today past SLA contradicting "approaches"; resolution_status
= resolved contradicting "unresolved".

[A4 — Action-vs-Universe-Prescription] For every action verb the deliverable
asks for (send, post, create, approve, dismiss, escalate, override, reclassify,
void, certify), identify the relevant universe record AND check if the record
has a proposed_resolution / recommended_action / next_step / assigned_to /
proposed_action field that prescribes a DIFFERENT action. If prompt prescribes
Y while record prescribes X:
  - Prompt EXPLICITLY overrides with reason -> ACCEPT.
  - Prompt SILENT on divergence -> FLAG ACTION_DIVERGENCE: <prompt> vs <universe>
    at <file>:<row_id>. BLOCK.
Same rule for authority/permission: persona lacks the role to do the asked
action (e.g., AR clerk overriding partner sign-off without explicit grant) ->
FLAG AUTHORITY_GAP. BLOCK.

[A5 — Persona Authorship Whitelist] (prompt phase only) Read
Brookfield_Base_Universe/2_Persona_Briefs.md end to end (28 authoring personas).
Verify Tasks/<TASK_DIR>/2_Persona.txt assigns one of the 28 by name AND role.
Output: PERSONA <name> -> POSITION <n>/28 (or NOT_IN_LIST). NOT_IN_LIST = BLOCK.
This is the POSITIVE-whitelist check; the validator only catches the 7 NPCs by
name (Owen Mercer / Brenda Abbas / Sofia Halabi / Farah Dlamini / James Randall /
Lucia Ferreira / Mateo Kovac).

[A6 — Persona Scope] (prompt + rubrics phase) When the prompt uses possessive
scope ("my X", "our X", "my vendors", "the items in my queue"), build the
persona's assignment set from _aux/Universe_Split/ (rows where created_by /
owner_email / approver_email = persona email, plus role-based assignments).
For each rubric value (vendor_id, JE_id, exception_id, recon_id, amount,
recipient), verify it is in the persona's assignment set. Absent = FLAG
SCOPE_DRIFT: rubric[i] tests <value> NOT in persona scope. BLOCK unless the
prompt explicitly broadens scope ("firm-wide", "across all entities").

[A7 — Clarity & Specificity holistic] (prompt phase) Re-read the prompt as a
first-time recipient. Identify any reasonable second interpretation that
produces a different write-action set, missing major details, or
unrecoverable persona intent. Per ambiguity: CLARITY_GAP: <desc>. MAJOR if
readings produce different write-actions; MINOR otherwise.

[A8 — Truthfulness deep tally] (prompt phase) For every factual claim,
classify MAJOR (core to request) or MINOR (incidental). Source of truth =
Fact_Ledger + Universe_Split. 1+ MAJOR or 2+ MINOR = FAIL; 1 MINOR = NON-FAIL.

[A9 — Persona Fit Comparison] (prompt phase) Read 2_Persona_Briefs.md.
Grade assigned persona fit 1-5. Identify a better-fit candidate. Delta >= 2
= NON-FAIL (Persona Mismatch). Delta = 1 = NOTE. CBs may swap persona, so
flag for decision not auto-block.

[A10 — Business Function Match] (prompt phase) Read
Docs/5_Prompt_Diversity_Business_Function.md to enumerate the 10 Brookfield
categories. Verify assigned business function matches the prompt's primary
scenario. False = BLOCK (CB cannot change assigned business function).
Ambiguous = NON-FAIL.

[A11 — End-to-End Solvability] (prompt + OE phase) Walk the dependency
chain from Hardness_Plan.md. For each step, verify the required source row
is materialized in _aux/Universe_Split/. Missing link = SOLVABILITY_BREAK.
BLOCK.

[A12 — Cross-Service Coherence] (universe phase) For each entity appearing
in 2+ services, verify name + ID + date consistency. Per contradiction:
CROSS_SERVICE: entity <name> referenced as <value_A> in <service_A> but
<value_B> in <service_B>. BLOCK if it would cause agent failure.

[A13 — Open-Ended Write Ask Atomicity] (rubrics phase) For every open-ended
write ask in the prompt ("all the X", "for each Y", "anyone who Z"), count
the ground-truth items in _aux/Universe_Split/ that match the criterion.
Verify the rubric set has >= that many distinct atomic rubrics. Per gap:
OPEN_ASK_BUNDLED: prompt asks "<quote>" with <N> ground-truth items, rubric
set has <M> atomic rubrics. Replace "at least N" with N atomic per-item
rubrics. Exception: ground truth is genuinely indeterminate -> ACCEPT.

Verdict:
  GO: zero ungrounded claims (A1) AND zero convention drift on Major fields (A2)
      AND zero narrative-state contradictions (A3) AND zero action-divergences
      / authority-gaps without explicit override (A4) AND persona is in the
      28-authoring whitelist (A5) AND zero persona-scope drifts (A6) AND zero
      MAJOR clarity gaps (A7) AND zero MAJOR truthfulness errors and <= 1
      MINOR (A8) AND business function matches (A10) AND zero solvability
      breaks (A11) AND zero cross-service contradictions causing agent
      failure (A12) AND zero bundled open-ended asks (A13). Persona fit
      comparison (A9) is decision-only, not auto-block.
  BLOCK: list each issue with location + fix, cite the perspective (A1-A13).

Save to _aux/Council_Reports/<phase>_A_grounding.md.
```

**Pass criteria:**
- A1: zero ungrounded concrete claims.
- A2: zero convention drift on Major fields (rubric category, agent-centric phrasing, tool names in title, "at least N" without prompt mandate, OE numbered-prose format, OE parameter traps).
- A3: zero narrative-state contradictions between the deliverable's state-implying claims and the universe's actual lifecycle state (Fact_Ledger atoms + Universe_Split records).
- A4: zero action-vs-universe-prescription divergences without explicit override language; zero authority/permission gaps. Prompts that diverge from a record's `proposed_resolution` / `recommended_action` / `next_step` must include explicit override reasoning (e.g., "override the proposed resolution because X is misclassified").
- A5: persona assigned in `2_Persona.txt` matches one of the 28 authoring personas in `Brookfield_Base_Universe/2_Persona_Briefs.md` by name and role. NPCs (Owen Mercer, Brenda Abbas, Sofia Halabi, Farah Dlamini, James Randall, Lucia Ferreira, Mateo Kovac) and any persona absent from the authoring list = BLOCK.
- A6: every universe-grounded rubric value (vendor_id, JE_id, exception_id, recon_id, amount, recipient) belongs to the persona's assignment scope when the prompt uses possessive framing ("my X", "our X"). Out-of-scope values = BLOCK unless the prompt explicitly broadens scope.
- A7: zero MAJOR clarity gaps (a second valid reading that produces a different write-action set).
- A8: zero MAJOR factual errors and at most 1 MINOR factual error.
- A9: persona fit grading recorded; better-fit candidate with delta ≥ 2 surfaces as NON-FAIL for operator decision.
- A10: assigned business function matches prompt primary scenario (or marked AMBIGUOUS as NON-FAIL).
- A11: every step in the projected agent trajectory has materialized source data in Universe_Split.
- A12: zero cross-service entity contradictions that would cause agent failure.

---

## Council B — Adversarial QC + Density + Hardness Preservation

**Role:** scores against every applicable QC sub-dim, attempts adversarial moves, projects tool-call density vs the 40+ baseline, and confirms the deliverable still triggers the hardness levers HARDNESS phase selected.

**Tool:** `oracle` (or `ultrabrain` for S3 rubrics phase).

**Inputs:**
- The deliverable file
- The prompt and (for OE / rubrics phases) the upstream deliverables
- `_aux/Hardness_Plan.md` (the lever selection + density projection)
- `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md`
- The relevant phase eval (`Evals/<n>_<phase>_Eval.md`)
- `_aux/Universe_Index/*`

**Perspectives covered (single prompt template, all four must pass):**

### B1 — QC sub-dim scoring
Score every applicable sub-dimension from `Docs/7_QC_Spec_Doc1.json`. For each: `SUB-DIM → SCORE (1-5) → ONE-LINE REASON`. Bar is 5 on every dim. Any sub-dim < 5 must be explicitly justified against per-task universe state (never against base-universe assumptions).

### B2 — Adversarial alt-path
Sketch a valid agent path that satisfies the prompt intent but would fail an Outcome rubric. If such a path exists, the rubric is over-specific OR the prompt has a second valid reading that the rubric set doesn't cover.

For S1 prompt phase: also attempt a second-reading attack. Read the prompt with a different but reasonable interpretation. Does it produce a different set of write actions, a different recipient, or a different final universe state? If yes, the prompt fails Unique Ground Truth or Clarity & Specificity.

### B3 — Tool-call density projection
Sketch the trajectory a competent Opus 4.8 agent would take to satisfy the deliverable. Count expected tool calls. The design target is **50+ on average across 6 runs**; the absolute floor is **40+**. The HARDNESS phase produced a projected midpoint; this perspective re-validates that the deliverable as written still hits that target.

Tiered output:
- Sketch produces 50+ → PASS.
- Sketch produces 40-49 → `THIN_DENSITY` — the deliverable meets the absolute floor but misses the design target. Real platform runs are at risk of underflow. For S1 prompt phase, suggest expanding asks or service breadth; for S2 OE phase, suggest expanding the OE list; for S3 rubrics phase, surface that the rubric set under-covers the trajectory. THIN is acceptable if the HARDNESS plan already documented a `## THIN density acceptance` per-task justification, otherwise it BLOCKS.
- Sketch produces < 40 → `INSUFFICIENT_DENSITY` — BLOCKER. The deliverable does not meet the absolute floor. For S1 prompt phase, the prompt is too lean and must be expanded with more asks or more service breadth. For S2 OE phase, the OE list is too thin. For S3 rubrics phase, the rubric set fundamentally under-covers the trajectory.

### B4 — Hardness preservation
For each lever selected in `_aux/Hardness_Plan.md`, verify the deliverable still triggers it.
- S1 prompt phase: does the prompt's framing actually surface each lever to the agent? (e.g., if Lever 3 is "missing reply", does the prompt's situation naturally lead the agent to search for replies?)
- S2 OE phase: does at least one OE step exercise each lever?
- S3 rubrics phase: does at least one Outcome rubric depend on the agent traversing the lever to satisfy it?

If any lever is no longer triggered, flag `HARDNESS_REGRESSION` — the deliverable lost a lever the prompt was designed around.

### B5 — Tool-leak / phrasing scan (lightweight)
Search the deliverable for tool names in forbidden positions, internal IDs in the prompt, em-dashes / en-dashes, "at least N" phrases, "approximately" misuse, "(or similar)" near exact values. Report each hit.

### B6 — Upstream propagation
When you find an issue that originates in an UPSTREAM artifact (not the one under review), flag it with a `PROPAGATE TO <PHASE>: ...` tag instead of patching it downstream. The principle: fix the issue at the phase where the root cause lives, then re-run downstream phases. Patching a downstream artifact to paper over an upstream root cause silently embeds the bug forever.

Concrete trigger examples:

- During **S2 OE review**, you notice the prompt has a truthfulness gap (a claim that does not ground to `Fact_Ledger.json` or a second valid reading the prompt allows that flips a write action) → flag `PROPAGATE TO S1: prompt has <issue> — re-run S1 to fix, do not patch the OE around it`.
- During **S2 OE review**, you notice a Hardness lever the prompt was supposed to surface is no longer visible to the agent under the prompt's framing → flag `PROPAGATE TO S1: prompt framing kills Lever <n>, OE cannot trigger it post-hoc`.
- During **S3 rubric review**, you notice an OE step expects a tool parameter that does not match `8_Server_Tools_Details.json` or references a record that is not in `_aux/Universe_Split/` → flag `PROPAGATE TO S2: OE<n> has <issue> — re-run S2 to fix, do not encode the wrong value into the rubric`.
- During **S3 rubric review**, you notice the prompt's framing is implicit ("execute on the figure") but the rubric set demands an explicit investigation step ("flag the discrepancy first") → flag `PROPAGATE TO S1: prompt framing mismatch — re-frame the prompt to make the investigation step explicit, OR drop the rubric (do not silently keep both)`.
- During **FINAL holistic review**, any cross-artifact issue that traces to a root cause in S1 or S2 → flag `PROPAGATE TO <S1|S2>: ...` with the exact upstream sentence / step at fault.

Output format for each finding: `PROPAGATE TO <PHASE>: <one-line root cause> -- upstream file:location -- recommended upstream fix`.

A B6 finding is BLOCKING — the deliverable under review cannot ship until the upstream phase has been re-run with the fix and the downstream phase re-run on the fresh upstream artifact. Do NOT accept "fix it in place at the current phase" as an alternative when the root cause is upstream.

### B7 — Per-rubric Cross-artifact Consistency (S3 rubrics phase)
For every rubric criterion, identify the matching OE step that produces / asserts the value. Verify the value in the rubric matches the value in the OE step exactly (modulo "(or similar)" flexibility on freetext fields).

How to verify: build a map `value_in_rubric -> {amount | recipient | vendor_id | exception_id | je_id | recon_id | date | account | retention_code | classification}`. For each value, grep the OE for a step that produces the same value with the same type. Mismatches to flag:
- Rubric tests `$12,345.67` but the matching OE step writes `$12,345.06`.
- Rubric tests recipient `alice@brookfield.com` but the matching OE step sends to `alice.smith@brookfield.com`.
- Rubric tests retention code `AICPA_SQMS_7Y` but the matching OE step writes `FIRM_INTERNAL`.
- Rubric tests JE id `JE-northstar_legal-FP-2025-12-0042` but no OE step produces or references that JE id.
- Rubric tests a vendor / exception / recon id that no OE step covers.

Output per mismatch: `CONSISTENCY_GAP: rubric[i] tests <value> | OE<n> writes <other value> | type=<amount|recipient|id|...>`.

This perspective prevents the silent-divergence failure where the rubric set is internally consistent + the OE chain is internally consistent, but rubric-value-in-criterion does not match OE-value-in-step. Without B7, agents that correctly follow the OE chain still fail rubrics because the rubric was written against a different value than the OE produced.

A B7 finding is BLOCKING — if rubric and OE disagree, one of them is wrong. If the OE is wrong, propagate via B6 (`PROPAGATE TO S2`). If the rubric is wrong, fix at S3 in place.

### B8 — OE Completeness semantic (S2 OE phase)
Walk the dependency chain implied by the prompt + Hardness_Plan. For each step a competent agent MUST take to satisfy the prompt, verify the OE chain contains that step. Specifically check for: discovery steps that resolve key entities (contact lookup before send; vendor lookup before AP action; period lookup before GL post); validation steps that confirm the action's prerequisites (e.g., the JE references a valid account in the entity's chart); and the final write step.

Output per missing step: `OE_INCOMPLETE: prompt requires <step> (e.g., "resolve recipient before sending email to <persona>") but no OE entry covers it. Without this step the OE chain cannot prove solvability.`

This perspective catches the OE Completeness sub-dim "missing critical steps" non-fail. Each missing step = NON-FAIL (not BLOCK, per QC spec). Multiple missing steps = FAIL.

### B10 — OE Write-Action → Outcome 1.1 forward map (S3 rubrics phase)
For every OE step that performs a write action (send / post / create / approve / file / upload / update / void / reverse / submit / archive / notify / email / schedule / draft / add / certify / dismiss / escalate / forward / publish / stage / circulate), verify there exists at least one Outcome rubric (sub-category 1.1) whose title checks that the action happened.

How to verify: build a map `oe_write_steps -> {action verb, recipient/target}`. For each write step, search the rubric set for an Outcome rubric whose title contains the same action verb directed at the same target. Mismatches:
- OE creates a Linear issue, no Outcome 1.1 rubric checks issue creation = `MISSING_OUTCOME_1.1: OE<n> writes <action> but no rubric verifies the action.`
- OE sends an email, no Outcome 1.1 rubric checks email send to that recipient = MISSING.
- OE files a document, no Outcome 1.1 rubric checks the upload = MISSING.

This perspective closes the forward-map gap that validator X1 partially covers (X1 maps prompt verbs → Outcome rubrics; B10 maps OE write actions → Outcome rubrics, which is the binding contract since OEs are the dependency chain the rubrics validate).

A B10 finding is BLOCKING — every OE write action needs a covering Outcome 1.1 to prove the agent's trajectory executed it.

### B11 — Prompt "Tell-me" cue → Outcome 2.1 forward map (S3 rubrics phase)
For every cue in the prompt that asks the agent to report a key fact in the final response ("tell me where it lands", "report back", "let me know", "walk me through", "I want to know", "show me", "give me the figures"), verify there exists at least one Outcome rubric (sub-category 2.1) whose title checks that the agent reported the requested fact in the final response.

Output per missing 2.1: `MISSING_OUTCOME_2.1: prompt cue "<quote>" expects final-response report of <fact>, no Outcome 2.1 rubric covers it.`

This perspective enforces the QC spec rule that Outcome 2.1 covers "key facts/findings in the final response when the user asked to be told a specific fact" — a gap the existing Outcome 1.1/1.2 mappings cannot fill (1.1 = trajectory action; 1.2 = trajectory content; 2.1 = final-response key facts).

A B11 finding is BLOCKING — a prompt that asks the agent to TELL the user something must have a 2.1 rubric checking the user was actually told.

### B9 — OE Service Mapping (S2 OE phase)
For each OE step, verify the named tool/service matches the data type the step queries or writes. The Brookfield universe data lives in specific services:
- Reconciliations / exceptions / variance / SLA tracking → BlackLine (NOT Oracle GL).
- AP invoices / vendor master / accounts payable → SAP subledger (NOT Oracle GL primary).
- Journal entries / posted-period state → Oracle GL.
- Retention codes / archived docs → Records Vault.
- Issue tickets / backlog → Linear.
- HR / personnel data → Airtable.
- Slack channels / DMs → Slack messaging.

Output per misaligned step: `OE_SERVICE_MISMATCH: OE<n> queries <data type> in <wrong service>. Data type belongs in <correct service>. Following this OE literally would return wrong-or-no results.`

This perspective catches the OE Accuracy sub-dim "Inaccurate Oracle Events" non-fail where the OE chain is structurally correct but points to the wrong service.

### Role-Lens Anchoring (apply across B1-B9)

Each B perspective is reviewed through five role lenses — read the deliverable five times, once per lens, and combine findings. This is a single sub-agent call but the prompt forces multi-perspective coverage so single-model blind spots are caught.

| Lens | Question to ask | Maps strongest to |
|---|---|---|
| **Architect** | Does the deliverable's structure fit the V3 framework cleanly? Are the abstractions right? | B1, B4 |
| **Implementer** | Will this actually run? Every tool name real, every ID format valid, every recipient resolvable? | B5 |
| **Red-team** | How do I break this? What's the most adversarial valid agent path? What's the second valid reading? | B2 |
| **Ground-truth** | Is every claim in the deliverable grounded in this task's universe (per-task SSoT)? Any base-universe assumption? | B1, B5 |
| **Integration** | Does this deliverable hold together with the upstream ones? Prompt-OE-rubrics consistency? Per-rubric value matches matching OE step value? Hardness levers preserved end to end? Any issue whose root cause is in an upstream artifact rather than the one under review? | B3, B4, B6, B7 |

A `BLOCK` from any lens propagates to the perspective it maps to. The verdict is the union of all five lens reads, not the average.

**Prompt template:**

```
You are Council B — Adversarial QC + Density + Hardness Preservation.

DELIVERABLE: <path>
PHASE: <prompt | oe | rubrics>
PROMPT: <path>
OE: <path> (if reviewing rubrics)
HARDNESS PLAN: Tasks/<TASK_DIR>/_aux/Hardness_Plan.md
QC SPEC: Docs/7_QC_Spec_Doc1.json + Docs/8_QC_Spec_Doc2.md
PHASE EVAL: Evals/<n>_<phase>_Eval.md
UNIVERSE INDEX: Tasks/<TASK_DIR>/_aux/Universe_Index/

TASK:

Apply five role lenses across the perspectives below. Read the deliverable
five times, once per lens, and combine findings (the verdict is the union):

  Architect     - structural fit to V3 framework, abstractions, cohesion
  Implementer   - will it run? real tool names, valid ID formats, resolvable recipients
  Red-team      - how to break it? adversarial valid path? second valid prompt reading?
  Ground-truth  - every claim grounded in PER-TASK universe (Fact_Ledger.json, Universe_Split/)?
  Integration   - prompt-OE-rubrics consistency, hardness levers preserved end-to-end

A BLOCK from any lens propagates to its mapped perspective (B1-B9).

[B1] QC sub-dim scoring. For each sub-dim in the QC spec, output:
SUB-DIM -> SCORE (1-5) -> ONE-LINE REASON. Bar is 5 on every dim.

[B2] Adversarial alt-path. Sketch a valid agent path that fails an Outcome
rubric (or a second valid reading of the prompt that flips a write action).
If found, name the divergence.

[B3] Tool-call density projection. Sketch the trajectory and count expected
tool calls. Design target 50+; absolute floor 40. < 40 = INSUFFICIENT_DENSITY
(BLOCKER); 40-49 = THIN_DENSITY (acceptable only if HARDNESS plan documented
per-task justification, otherwise BLOCKS); 50+ = PASS.

[B4] Hardness preservation. For each lever in Hardness_Plan.md, verify the
deliverable still triggers it. If any lever is no longer triggered, flag
HARDNESS_REGRESSION with the missing lever.

[B5] Tool-leak / phrasing scan. Report any tool name in title (rubrics) or
prompt body, internal IDs in the prompt, em-dashes, 'at least N' without
mandate, 'approximately' before IDs/dates, '(or similar)' near exact values.

[B6] Upstream propagation. For every issue you find whose ROOT CAUSE lives
in an upstream artifact (not the one under review), output:
PROPAGATE TO <PHASE>: <one-line root cause> -- <upstream file:location> --
<recommended upstream fix>.
A B6 finding is BLOCKING. Do NOT accept "fix it in place" as a substitute
when the root cause is upstream — patching downstream silently embeds the
bug. The fix is to re-run the upstream phase and then re-run the current
phase against the fresh upstream output.

[B7] Per-rubric Cross-artifact Consistency (S3 rubrics phase ONLY). For
every rubric criterion, identify the matching OE step that produces / asserts
the value. Verify the value in the rubric matches the value in the OE step
exactly (modulo "(or similar)" flexibility on freetext fields). Output per
mismatch: CONSISTENCY_GAP: rubric[i] tests <value> | OE<n> writes <other> |
type=<amount|recipient|id|date|account|retention_code|classification>. A B7
finding is BLOCKING. If the OE is wrong, propagate via B6 (PROPAGATE TO S2);
if the rubric is wrong, fix at S3 in place.

[B8] OE Completeness semantic (S2 OE phase). Walk the dependency chain from
prompt + Hardness_Plan. For each step a competent agent MUST take to satisfy
the prompt, verify the OE chain contains that step. Discovery steps before
write actions, validation steps before posts, final write step. Output per
missing step: OE_INCOMPLETE: prompt requires <step> but no OE covers it.

[B9] OE Service Mapping (S2 OE phase). For each OE step, verify the named
tool/service matches the data type the step queries / writes:
reconciliations -> BlackLine; AP invoices -> SAP; JEs -> Oracle GL;
retention -> Records Vault; tickets -> Linear; HR -> Airtable;
chat -> Slack. Output per misaligned step: OE_SERVICE_MISMATCH: OE<n>
queries <data type> in <wrong service>. Belongs in <correct service>.

[B10] OE Write-Action -> Outcome 1.1 forward map (S3 rubrics phase). For
every OE step performing a write action (send / post / create / approve /
file / etc.), verify there is at least one Outcome 1.1 rubric checking that
action happened. Output: MISSING_OUTCOME_1.1: OE<n> writes <action> but no
rubric verifies the action. BLOCK.

[B11] Prompt "tell-me" cue -> Outcome 2.1 forward map (S3 rubrics phase).
For every cue in the prompt asking the agent to report a key fact in the
final response ("tell me where it lands", "report back", "let me know",
"walk me through"), verify at least one Outcome 2.1 rubric covers the
requested fact. Output: MISSING_OUTCOME_2.1: prompt cue "<quote>" expects
report of <fact>, no 2.1 rubric covers it. BLOCK.

Verdict:
  GO: every QC sub-dim >= 5 (or NON-FAIL bands explicitly justified by per-
      task universe), AND no adversarial divergence found, AND projected
      tool calls >= 40, AND every Hardness lever still triggered, AND no
      phrasing hits, AND no PROPAGATE TO <upstream> flags raised, AND
      every rubric value matches the matching OE step value (B7), AND
      the OE chain covers every must-take step (B8), AND every OE step
      targets the correct service (B9), AND every OE write action has
      a matching Outcome 1.1 (B10), AND every prompt tell-me cue has a
      matching Outcome 2.1 (B11).
  BLOCK: list each Major / Moderate issue with the perspective cited (B1-B11)
         and the fix. For B6 findings the fix MUST name the upstream phase
         to re-run.

Save to _aux/Council_Reports/<phase>_B_adversarial.md.
```

**Pass criteria:**
- B1: every applicable QC sub-dim scores 5 (or 3-4 is explicitly justified against per-task universe state).
- B2: returns "no divergence found".
- B3: projected tool calls ≥ 50 (design target) OR 40-49 with explicit `THIN_DENSITY` justification carried from HARDNESS. < 40 BLOCKS.
- B4: every lever from Hardness_Plan.md is still triggered.
- B5: returns "no hits".
- B6: returns "no upstream propagation flags". If any `PROPAGATE TO <upstream>` flag is raised, the deliverable is BLOCK — the operator must re-run the named upstream phase, then re-run the current phase against the fresh upstream output. Patching downstream is not an acceptable resolution.
- B7: zero `CONSISTENCY_GAP` findings (S3 rubrics phase only). Every universe-grounded rubric value matches the value in the matching OE step. Rubric-OE divergence on the same record = BLOCK.
- B8: zero `OE_INCOMPLETE` findings (S2 OE phase only). Every must-take step in the agent's dependency chain has a covering OE entry. Single missing step = NON-FAIL; multiple missing steps = FAIL.
- B9: zero `OE_SERVICE_MISMATCH` findings (S2 OE phase only). Every OE step targets the correct service for the data type it queries / writes.

## Severity tally rule (binding for all councils + AUDIT)

The QC spec rule "count only the HIGHEST severity issue per criterion" applies as follows when an issue triggers multiple severity classifications:

| Scenario | Resolution |
|---|---|
| Same rubric flagged Major (Self-Containment) + Major (Persona Scope) | Count once at Major. |
| Same rubric flagged Major (Incorrect — over_specified) + Moderate (Incorrectly Labeled Category) | Count once at Major. The Moderate is absorbed for the Overall Quality tally. |
| Same rubric is an invalid Process AND has a wrong write-action category | Count once at Moderate for Overall Quality tally. **Separately**: it counts as 1 toward the `Process Rubrics` scored sub-dim's "2+ invalid → FAIL" threshold. The double-track is INTENTIONAL (Overall Quality is severity-based; Process Rubrics is count-based on invalid Process rubrics specifically). |
| Same rubric has both a B6 PROPAGATE flag and an inline Major | Both are recorded but Overall Quality counts only the Major; the PROPAGATE flag is a STOP signal regardless. |

## Sub-dimension scoring scheme map

Per-sub-dim score-band scheme from `Docs/7_QC_Spec_Doc1.json`:

| Sub-dimension | Scheme | Notes |
|---|---|---|
| **Prompt** Unique Ground Truth | 1/3/5 | NON-FAIL middle band |
| **Prompt** Feasibility | 1/3/5 | NON-FAIL middle band |
| **Prompt** Explicit Tool Mention | 1/5 | Binary — single leak = FAIL |
| **Prompt** Clarity & Specificity | 1/3/5 | NON-FAIL middle band |
| **Prompt** Contrived / Unnatural | 1/3/5 | NON-FAIL middle band |
| **Prompt** Alignment with Today's Date | 1/3/5 | NON-FAIL middle band |
| **Prompt** Truthfulness | 1/3/5 | NON-FAIL middle band |
| **Prompt** Tool Use & Cross-service | 1/5 | Binary — single-service = FAIL |
| **Prompt** Investigation + Action | 1/5 | Binary — no write action = FAIL |
| **Prompt** Coherence (Bolt-on) | 1/5 | Binary — bolt-on present = FAIL |
| **Prompt** Persona | 1/3/5 | NON-FAIL middle band |
| **Prompt** Business Function | 3/5 | No FAIL band (only NON-FAIL or PASS) |
| **Universe** Data Exists | 1/5 | Binary |
| **Universe** Cross-service Coherence | 1/5 | Binary |
| **OE** Completeness | 3/4/5 | NON-FAIL only (no FAIL band) |
| **OE** Accuracy | 3/4/5 | NON-FAIL only (no FAIL band) |
| **Rubric** Overall Quality | 1/3/5 | NON-FAIL middle band, threshold-based |
| **Rubric** All-Failing | 1/3/5 | Verifier-stage; rubric-stage = 5 |
| **Rubric** Category Balance | 1/2 or 5 | Binary — `#Outcome ≤ #Process` or 0 Outcome = FAIL |
| **Rubric** Process Rubrics | 1/3/5 | FAIL at 2+ invalid |
| **Rubric** Agent-Centric Phrasing | 1/2 or 5 | Binary — single violation = FAIL |

Council B-B1 must emit one line per sub-dim in this format:

```
SUB-DIM <name> -> SCORE <n>/<scheme> -> REASON <one-line>
```

Examples:
```
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5 scheme) -> all factual claims verified vs Fact_Ledger
SUB-DIM Coherence -> SCORE 1/5 (1/5 binary) -> bolt-on sentence "...the May FX revaluation..." doesn't share entities with rest of prompt
SUB-DIM OE Accuracy -> SCORE 4/5 (3/4/5 NON-FAIL only) -> minor count mismatch in OE 7 (rubric says 6 exceptions; universe has 4)
SUB-DIM Agent-Centric Phrasing -> SCORE 1/5 (1/2 or 5 binary) -> rubric[3] title starts with "The email mentions..." (artifact subject)
SUB-DIM Category Balance -> SCORE 5/5 (1/2 or 5 binary) -> 8 Outcome, 0 Process
```

Outputting the scheme explicitly prevents scoring-drift where a sub-agent treats a binary dim as 1/3/5. AUDIT Lens 1 inherits the same scheme but applies the strictest interpretation: NON-FAIL middle bands collapse to REVISE (not PASS).

---

## Opt-in: True multi-model Council B (`COUNCIL_MODE=multi`)

The default Council B is one `oracle` sub-agent call applying 5 lenses in sequence. The lenses overlay catches most of what 5 separate model invocations would catch, at 1/5 the cost.

For maximum rigor on a critical task (final deliverable for a benchmark seat, a task that has already been bounced by the platform reviewer, or a 5/5-or-die deliverable), invoke the multi-model variant by prefixing the trigger: `PIPELINE S3 — Tasks/<TASK_DIR> COUNCIL_MODE=multi`. The runbook does this instead:

1. **Spawn 5 sub-agents in parallel**, one per lens, each `read-only`. Each gets the same brief (deliverable + upstream + Hardness_Plan + QC spec + relevant inventory). The model + role assignment:

   | Seat | Lens | Sub-agent | What it owns |
   |---|---|---|---|
   | 1 | Architect | `oracle` | Structural fit to V3 framework, abstractions, cohesion. Maps to B1 + B4. |
   | 2 | Implementer | `oracle` | Will it run? Real tool names, valid ID formats, resolvable recipients. Maps to B5. |
   | 3 | Red-team | `ultrabrain` | How to break it. Adversarial valid path. Second valid prompt reading. Maps to B2. |
   | 4 | Ground-truth | `oracle` | Every claim grounded in PER-TASK universe (`_aux/Fact_Ledger.json`). Maps to B1 + B5. |
   | 5 | Integration | `oracle` | Prompt-OE-rubrics consistency, hardness levers preserved end-to-end. Maps to B3 + B4. |

2. **Each seat returns the same output contract** as the single-call Council B (B1-B11 perspectives), plus a `LENS: <name>` header so the consensus knows the origin.

3. **Crash / empty / quorum.** If a seat errors or returns empty, re-spawn it (up to 2 retries). The round needs ≥ 4 successful seats. If fewer, the round is INVALID — do NOT synthesize a PASS; escalate to the user.

4. **Consensus synthesis.** Spawn a 6th `oracle` sub-agent with the role of CONSENSUS. It receives all 5 seat outputs labeled by lens. Its job:
   - Deduplicate findings across seats.
   - Rank by severity (BLOCKER > MAJOR > MINOR).
   - Resolve disagreements by citing repo evidence (the per-task universe, the QC spec). A seat's verdict without cited evidence is ignored.
   - **Veto propagation.** Any single seat BLOCKER forces REVISE unless the consensus disproves it with cited evidence. Any `UNKNOWN` on a hard constraint counts as REVISE.
   - Output: `VERDICT: PASS | REVISE`, `ROUND VALID: yes/no`, deduped issue list with per-issue fix, proceed recommendation.

5. **Cost note.** Multi-mode is 6 sub-agent calls per Council B invocation vs 1 in default. Use it when the stakes justify the spend.

## Both councils must GO before the deliverable ships

If either returns BLOCK:
1. Apply the fixes.
2. Re-run the validator.
3. Re-run BOTH councils (not just the one that blocked).
4. Loop until clean.

Do not negotiate with a BLOCK by editing the rubric to make it lenient. Tighten the deliverable. The councils exist precisely because the bar is 5/5 on every QC dim and 40+ tool calls minimum.

---

## When BOTH councils GO but density still feels marginal

If Council B's B3 returns "exactly 40" or "40-42 midpoint", consider:
- Adding one more write action to push the floor higher.
- Adding one more lever to widen the projected range.

A target midpoint of 50+ is the comfortable zone. 40 is the floor.

## Unified verdict format (v11 F2)

Every council / AUDIT / FINAL report MUST end with a fenced JSON block conforming to this schema. Cross-task aggregation scripts read these blocks; humans read the markdown above. Both stay in the same file.

```
{
  "phase": "<prompt | oe | rubrics | final | audit_prompt | audit_oe | audit_rubrics | s4>",
  "council": "<A | B | AUDIT | FINAL>",
  "task_dir": "<Tasks/<TASK_DIR>>",
  "verdict": "<GO | BLOCK | PASS | REVISE | REBUILD | PASS_STRICT>",
  "perspectives": {
    "<A1 | B1 | Lens1 | ...>": {
      "status": "<PASS | FAIL | NOTE>",
      "findings": [
        {
          "severity": "<BLOCKER | MAJOR | MODERATE | MINOR | NOTE>",
          "location": "<file:line | rubric[i] | OE<n> | prompt:para>",
          "issue": "<one-line>",
          "fix": "<one-line>",
          "propagate_to": "<S1 | S2 | S3 | null>"
        }
      ]
    }
  },
  "scores": {
    "<sub_dim_name>": {
      "score": <1 | 2 | 3 | 5>,
      "scheme": "<1/5 | 1/3/5 | 1/2/5>",
      "reason": "<one-line>"
    }
  },
  "density_projection": {
    "midpoint": <integer>,
    "band": "<PASS | THIN | INSUFFICIENT>",
    "breadth_services": <integer>,
    "breadth_band": "<PASS | THIN_BREADTH | null>"
  },
  "lever_preservation": {
    "expected": <integer>,
    "preserved": <integer>,
    "missing": ["<lever name>", ...]
  },
  "bucket_1_risk_pct": <float | null>,
  "iteration": <integer>,
  "timestamp": "<ISO 8601>"
}
```

**Rules:**
- The JSON block goes at the END of the report file, after the human-readable verdict prose.
- Fields not applicable to the phase use `null` (e.g., `density_projection` is `null` on AUDIT prompt-phase; `bucket_1_risk_pct` is `null` outside FINAL Lens 6).
- `propagate_to` is the v6 B6 propagation field — if non-null, the deliverable is BLOCKED until the upstream phase is re-run.
- `iteration` increments on every REVISE round (cap 3, then escalate).
- Cross-task aggregation: future `Validators/aggregate_verdicts.py` will glob `Tasks/*/_aux/Council_Reports/*.md`, extract the trailing JSON blocks, and emit portfolio-level QC trend tables.

This format closes the gap where every council emitted its own freeform verdict text. Now any verdict from any phase can be parsed for portfolio-level analysis without writing per-phase regex.
