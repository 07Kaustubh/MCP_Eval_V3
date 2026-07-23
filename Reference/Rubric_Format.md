# Rubric Format Card

## Schema

Each rubric is a JSON object in the FLAT shape — exactly four fields, nothing else:

```json
{
  "title": "The Agent ...",
  "category": "outcome",
  "justification": "...",
  "evidence": "..."
}
```

**No `id` field, no `annotations` wrapper, no extras.** Pure flat.

The validator still ACCEPTS the legacy nested shape (`{id, title, annotations: {evidence, justification, rubric_category}}`) for back-compat with V3 reference tasks and older shipped tasks, but emits a WARN — `nested schema is deprecated, convert to flat`. New tasks ship flat. `15_Updated_Rubrics.json` in the REVIEW flow must also be flat.

## Hard rules

| Rule | Detail |
|---|---|
| **Two categories only** | `outcome` or `process`. No TS, no QC. Those are V2. |
| **Outcome must outnumber Process** | Process is rare. All 4 V3 reference tasks have **zero** process rubrics. Process counts >50% of total = FAIL. |
| **Agent-centric phrasing** | Every title starts with `The Agent` or `Agent`. Never passive ("An email was sent..."). |
| **No tool names in `title`** | Tool names are allowed only in `evidence` and `justification`. The validator greps the title against `8_Server_Tools_Details.json` and blocks matches. |
| **No "at least N" in title** unless the prompt explicitly mandates a minimum | "At least N" is reward-hackable. For N independent write actions, write N atomic rubrics. |
| **Self-contained** | Every expected value (email, amount, ID, account number, classification, retention code) embedded in the `title` itself. The judge does not have the universe; the judge has only the trajectory + the rubric set. |
| **Atomic** | One independent claim per rubric. If the rubric can fail for two unrelated reasons, split it. **StarPM V4 tighter atomicity (ML-confirmed July 2026, universe = starpm only):** if the criterion fails, there must be EXACTLY ONE clear reason why. Independent content topics or actions — even on the same artifact — must be split. Same-tool-call bundling permitted only when the values are attributes of the SAME record (e.g., name + company + city on one relocation record; recipient + CC in one send call). Enumerated `(a) X (b) Y (c) Z` and numbered `(1) X (2) Y` bundles in a title are forbidden — validator FAILs both under `universe == starpm`. Multi-recipient send: email *sent* to A, B, C = three separate 1.1 rubrics; email *content* identical across A, B, C = one 1.2 rubric. Catch-all summary criterion is never atomic — split it. V3 reference tasks (Task 11/12/14, Brookfield) shipped under Brookfield spec authority and may show narrative bundles — do NOT cite as precedent for StarPM V4 work. **Brookfield / Keystone / MoveOps tasks:** the older "interconnected parts of the same request" bundling exception still applies — the StarPM V4 tightening is not part of their spec authority. |
| **Grounded** | Every concrete value in the title must appear verbatim in this task's `_aux/Universe_Split/`. The validator does a substring sweep. |

## Outcome sub-categories

The category field is just `outcome`. The sub-type is inferred from the title shape:

| Sub-type | Title shape | When to use |
|---|---|---|
| **1.1** | "The Agent sends an email to X." / "The Agent creates a Linear issue ...". Verifiable from the tool call itself. | One per write action. Always required. |
| **1.2** | "The Agent's email to X includes Y." / "The Agent's reconciliation memo states Z." Verifiable from the tool-call parameters. | When the write has specific content requirements beyond just being sent. |
| **2.1** | "The Agent reports / identifies / flags / states ...". Verifiable from the final response. | When the user asked to be told a specific fact directly. |

## Process — three-condition test

Add a Process rubric ONLY when ALL THREE hold:

1. **Required by every valid solution path**, phrased broadly enough that any valid path passes (`Agent notifies legal`, NOT `Agent emails legal`).
2. **A stricter Outcome rubric cannot capture the same requirement.** If a precise value the agent could only produce by doing the work would prove it, use that Outcome.
3. **It describes a behavioral property, not an execution trace.** ✅ "Agent verifies the wire instructions match the file before initiating the transfer." ❌ "Agent called `contacts_get_contact` then `email_get_thread`."

If any condition fails, drop the Process or tighten the Outcome.

## Phrasing verbs (cheat sheet)

| Sub-type | Verbs |
|---|---|
| 1.1 — write actions | sends, creates, updates, posts, schedules, assigns, uploads, certifies, submits, approves, voids, files |
| 1.2 — action content | includes, mentions, states, covers, references, names |
| 2.1 — key facts | identifies, reports, flags, lists, recommends, concludes |
| Process | verifies, confirms, checks, reviews, reconciles, notifies (before X) |

## Flexibility patterns

| Situation | Pattern | Example |
|---|---|---|
| One correct value | Strict / exact match | `chloe.vance@brookfieldcpas.com` |
| Free-text the agent generates | Fuzzy + `(or similar)` | `subject related to a relocation proposal (or similar)` |
| Calculated / rounded amount | `approximately` | `approximately $117,000` |
| Multiple valid answers (closed set) | `must be one of: A, B, or C` | |
| Multiple attributes of the same record | Natural comma phrasing on one record, no `(a)(b)(c)` enumeration | `Noah Fitzgerald (GreenStack Solutions) relocating to Seattle` (all three are attributes of one relocation record) |
| Method-agnostic goal | Name the goal, not the method | `Agent notifies legal` (not `Agent emails legal`) |

## When NOT to use these qualifiers

- Never use `approximately` in front of IDs, dates, account numbers, exact static values. These are exact-match.
- Never use `(or similar)` near emails, IDs, dates. These are exact-match.
- Never use `at least N` for write actions of the same type. Atomic rubric per item.

## The three fields

| Field | What it says |
|---|---|
| `title` (criterion) | The specific yes/no claim. Self-contained, atomic, agent-centric. The only field the judge evaluates. |
| `justification` | Why this rubric exists. 1 to 2 sentences. Connects to the prompt or a known failure mode. |
| `evidence` | What to look for in the trajectory or final response to prove pass/fail. Reference the tool call, parameter, OR response section. |

## Worked example shape (Outcome 1.1 + 1.2 + 2.1)

```json
[
  {
    "title": "The Agent sends an email to peter.sanchez@brookfieldcpas.com with steven.perry@brookfieldcpas.com in CC.",
    "category": "outcome",
    "justification": "The prompt says 'Email Peter the final analysis ... and copy Steven since he will need to sign off at the partner level.'",
    "evidence": "Look for a send-email call with recipient peter.sanchez@brookfieldcpas.com and CC containing steven.perry@brookfieldcpas.com. Confirm success response."
  },
  {
    "title": "The Agent's email to Peter includes the net third-party wire aggregate of approximately $117,000.",
    "category": "outcome",
    "justification": "The prompt asks Peter to receive 'the final analysis with the recommendation'. The correct net aggregate is approximately $117,000 (gross $186,350 less three documented adjustments).",
    "evidence": "Check the content parameter of the email for the figure approximately $117,000 (or the exact $117,000)."
  },
  {
    "title": "The Agent reports the GraniteRack vendor-master has not been confirmed corrected and still references the deprecated contract (or similar statement).",
    "category": "outcome",
    "justification": "The prompt explicitly asks 'confirm whether the vendor-master was updated, because it was still showing the old contract reference'.",
    "evidence": "Check the agent's final response for a statement that the vendor-master correction is unconfirmed and the entry still references the stale SOW."
  }
]
```

## Anti-patterns (rubric reviewers will fail these)

- Title in passive voice: "An email was sent to ..." → rewrite as "The Agent sends an email to ..."
- Tool name in title: "The Agent calls oracle_gl_post_journal_entry" → drop the tool name; rewrite as the user-visible outcome.
- Bundling: "The Agent sends an email to X AND creates a Linear issue" → split into two rubrics.
- **Enumerated bundle (StarPM V4 only, ML-confirmed July 2026):** "The Agent's update includes (a) escalation, (b) $1,850, (c) Thursday" → three independent content claims can each pass/fail separately, so this violates the one-clear-reason-to-fail test. Split into three atomic rubrics (or a natural-phrasing same-record bundle when the elements are attributes of one record). Validator FAILs `(a) ... (b) ...` and `(1) ... (2) ...` shapes on StarPM V4 tasks only. Brookfield / Keystone / MoveOps tasks continue to allow the shape per their respective rulebooks.
- **Multi-recipient send bundle (StarPM V4 only, ML-confirmed July 2026):** "The Agent emails Alice, Bob, and Carol" → three distinct tool calls on StarPM V4, split into one 1.1 per recipient. Identical body across recipients may share one 1.2. Not gated for other universes.
- "At least 5 follow-up issues" without prompt mandate → one rubric per issue grounded in ground truth.
- "(or similar)" near an exact email or ID → drop the qualifier; emails / IDs are strict.
- A Process rubric that names a specific tool path → delete it. If the work is provable from an Outcome value, tighten the Outcome.
- **Tool capability mismatch (ML-confirmed July 2026):** Rubric requires an action the service cannot perform (e.g., "The Agent sends a Gmail message to X" when Gmail only supports `gmail_draft_email` — there is no send action). Rewrite as "The Agent drafts a Gmail message to X" or route to a service that does support sending.
- **Single-channel lock-in (ML-confirmed July 2026):** Rubric mandates one specific communication channel (e.g., "The Agent sends a Slack message") when the prompt allows multiple valid channels and a reasonable agent might legitimately choose another. Use a Process rubric that names the goal ("Agent notifies the property manager") or name all valid paths in the criterion.
- **Over-embedded non-required specifics (ML-confirmed July 2026):** Rubric pins free-text details (subject lines, paragraph wording, exact phrasing) to values not mandated by the prompt. Agent-generated content must use `(or similar)`. Only structured fields with exactly one correct value (IDs, emails, dollar amounts, dates) get exact-match criteria.
- **Ambiguous universe data enforcement (ML-confirmed July 2026):** Rubric selects one interpretation of a genuinely ambiguous or conflicting universe field and penalizes the agent for choosing another reasonable reading. When universe data is ambiguous, either (a) tighten the prompt to resolve the ambiguity, or (b) accept all defensible interpretations in the criterion with `must be one of:`.
- **De-duplication penalty (ML-confirmed July 2026):** Rubric counts specific send/create actions and fails the agent for making fewer calls than expected because the agent correctly de-duplicated redundant or conflicting records. A rubric must test outcomes, not call counts; if the agent achieves the correct business outcome through fewer operations, it passes.
- **System-of-record vs. reality mismatch (ML-confirmed July 2026):** Rubric demands the agent echo a stale system-of-record field value when downstream evidence in the same universe (later emails, audit logs, subsequent records) clearly contradicts it. Rubrics must be grounded in the most authoritative available evidence; if the universe contains a confirmed correction, the rubric must reflect the corrected value.

## Severity taxonomy (ML-confirmed July 2026)

When a rubric defect is identified, assign severity using this taxonomy. The pipeline's absolute-count gates below use these tiers.

| Defect type | Severity | Notes |
|---|---|---|
| Self-Containment failure (missing grounding) | **Major** | Judge cannot verify without universe data |
| Incorrect value (wrong amount, wrong recipient, wrong ID) | **Major** | Rubric tests a value the agent cannot satisfy correctly |
| Channel / method lock-in when valid alternative exists | **Major** | Escalates from Minor per Phase 2.7 rule; Minor only when no realistic alternative path exists |
| **Overly Specific** (free-text field pinned to exact wording when agent-generated) | **Moderate** | Heavier penalty than before (July 2026 change). Use `(or similar)` for agent-generated text; keep exact only for structured fields with one correct value (IDs, emails, amounts, dates). |
| Tool name in rubric title | **Moderate** | Validator catches; council confirms |
| Wrong category (e.g., write action filed as Process) | **Moderate** | |
| Passive voice phrasing | **Moderate** | "An email was sent" instead of "The Agent sends" |
| **Under-Specific** (rubric so broad a wrong answer passes) | **Minor** | Lighter penalty than Overly Specific (July 2026 change). Flag but does not immediately block if the prompt direction is recoverable. |
| `(or similar)` adjacent to an exact-match field (email, ID, date) | **Minor** | Qualifier must be removed |
| Justification / evidence field thin or missing | **Minor** | |

**Severity swap summary (July 2026):** Overly Specific promoted to Moderate; Under Specific demoted to Minor. Rationale: an over-specified rubric actively causes valid agent paths to fail; an under-specified rubric merely weakens discrimination but does not wrongly penalize correct behavior.

## Threshold math + dilution prevention

The QC spec's Overall Rubric Quality scoring uses % of total criteria as the denominator. A 5-rubric set with 1 Major = 20% FAIL; a 100-rubric set with 1 Major = 1% PASS. To prevent the dilution incentive (adding filler rubrics to lower the %), the pipeline applies ADDITIONAL absolute-count gates alongside the % thresholds:

| Condition | Result |
|---|---|
| Major > 10% OR Major absolute count >= 3 | **FAIL** |
| (Major + Moderate) > 15% OR (Major + Moderate) absolute count >= 5 | **FAIL** |
| (Major + Moderate + Minor) > 20% OR (Major + Moderate + Minor) absolute count >= 8 | **FAIL** |
| No Major AND no Moderate AND < 5% Minor (and absolute Minor < 3) | **PASS (5)** |
| Otherwise | **NON-FAIL (3-4)** |

The absolute-count gates are a pipeline extension to prevent gaming. They activate ONLY when the rubric count is < 30; above 30, the % thresholds alone are reliable. AUDIT Lens 1 applies both the % and absolute gates strictly.
