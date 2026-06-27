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
| **Atomic** | One independent claim per rubric. If the rubric can fail for two unrelated reasons, split it. |
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
| Multiple required elements | `must include: (a) ..., (b) ..., (c) ...` | |
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
- "At least 5 follow-up issues" without prompt mandate → one rubric per issue grounded in ground truth.
- "(or similar)" near an exact email or ID → drop the qualifier; emails / IDs are strict.
- A Process rubric that names a specific tool path → delete it. If the work is provable from an Outcome value, tighten the Outcome.

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
