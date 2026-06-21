# Prompt Format Card

## Hard rules (any violation = revise before shipping)

| Rule | Detail |
|---|---|
| **500-word cap** | Tight, focused prompts beat sprawling ones. Strip every sentence that doesn't advance the same situation. |
| **No em-dash / en-dash** | Use periods, commas, or parentheses. The validator blocks both `—` and `–`. |
| **No tool names** | Never write `email_send_email`, `linear_create_issue`, `oracle_gl_post_journal_entry`, etc. Refer to systems naturally (`email`, `Slack`, `our ledger`, `the vault`). |
| **No MCP-server names** | Never write "the Oracle GL MCP server" or "use the Linear MCP". |
| **No internal IDs** | No `JE-...-FP-...`, `exc_...`, `BL-...`, `VEN-...`, `apinv_...`, `doc_...`, `issue_...`. A real person speaking to their assistant would name the vendor, the period, the situation. |
| **No pre-solving** | Do not tell the agent the root cause, the final number, or the named culprit. The agent investigates. |
| **First person, natural voice** | The persona is talking to their own assistant. Real life, not a spec. |
| **One coherent situation** | Every ask flows from the same problem. Sentence-removal test: cut any sentence. If the rest still makes perfect sense, that sentence is a bolt-on. Delete or merge it. |

## Voice principles

- **Mid-thought entry.** The persona is already in the middle of dealing with something. They don't start with "Hi, I need..." — they open with the situation.
- **Asymmetric knowledge.** The persona knows part of the picture, names the part they know, asks the agent to fill in the rest.
- **Emotional texture.** Frustration, time pressure, mild confusion. Real reactions, never theatrical.
- **Persona register.** A partner's voice differs from a trainee's. A compliance officer differs from an AP coordinator. Match the brief in `PersonaBrief.txt`.

## Structure that works

Three loose movements, in order:

1. **Trigger** — what just happened or what landed on the desk (a partner asked, a deadline is here, an exception is sitting open).
2. **Context** — the part the persona already knows (Farah pulled the data, the FP-2026-05 lock target passed, the SOW was superseded). Vague enough to require investigation, concrete enough to ground the task.
3. **Asks** — what needs to happen, phrased as work, not commands. Investigation + write actions, woven together.

## What makes a prompt hard without being contrived

Fold in 3 to 5 levers from `Reference/Hardness_Playbook.md`. The lever lives in the data. The prompt just opens the door.

- A vendor that requires checking SAP for the reissue.
- A reconciliation whose latest review note overrides the earlier one.
- A wire aggregate whose net depends on three adjustments (reversal, credit memo, intercompany reclass).
- An open exception waiting on a specific named approver.
- A document filing whose retention code depends on the entity and the document kind.

## Diversity beyond "investigate + send email"

Push for 3+ write actions across 3+ services per prompt. Mix of:

- send email / reply email
- post Slack channel message (NOT thread reply unless it is the natural fit)
- update Linear issue / add comment
- upload Records Vault document with retention + classification
- update Airtable record
- create reminder
- create calendar event
- post a journal entry through its lifecycle
- approve / void an AP invoice
- submit / approve / certify a reconciliation

## Anti-patterns (do not write)

- "First, search emails. Then check Oracle GL. Then send an email." (command list)
- "Julian's vibe-coded demo is rate-limiting us." (pre-solving)
- "Check what's happening with the Pinnacle proposal in `issue_pinnacle_proposal`." (internal ID leak)
- "Get into emails, Slack, Linear, CRM and tell me what's happening." (tool-name list, also bolt-on)
- "Write me a 3-sentence summary in passive voice." (contrived format)
- "Find the email from January 15 at 3:47 PM." (artificial precision)
- Four unrelated asks stapled together. (bolt-on)

## Output

Plain prose, in the persona's voice. No headings, no bullet lists in the prompt itself unless the persona would naturally write one. Write to the AI assistant, not to the QC reviewer.

## Validator catches automatically

`Validators/validate.py --phase prompt` warns when any of these `Prompt_Guidelines.md` anti-patterns appear in the draft:

- QC-sample clichés ("go through everything and surface every", "loop in", "CC our CEO", etc.)
- Over-signaling the investigation ("check our emails, slack, linear", etc.)
- Generic urgency framing ("before it blows up", "keeping me up at night", "something changed in the last few days", etc.)

These warns are not blocking — a human writer can override when the phrase is in fact natural for the persona — but they flag mass-produced tonality before the deliverable reaches the councils.
