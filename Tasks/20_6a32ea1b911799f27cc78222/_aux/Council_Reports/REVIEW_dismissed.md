# REVIEW — Dismissed Findings

This file logs any council-flagged finding that turned out, on per-task universe re-verification, to be incorrect — so the candidate is not penalized for it.

## Dismissed in this pass

### D1: "Brenda Abbas should not be named as a Brookfield reviewer because the persona briefs describe her as an external NPC"

- **Source:** initial reading of `2_Persona_Briefs.md` (notes section: "Brenda Abbas... appears in scenarios as named participants but never as the acting voice"; "Externally, Owen Mercer + Brenda Abbas — the AP-side NPCs"; under Sean Williams: "Externally: Brenda Abbas (Oracle GL vendor)").
- **Verification against per-task universe:**
  - `contacts.contacts.json`: `Brenda Abbas | brookfieldcpas.com | job: Account Manager | description: Vendor account manager`.
  - `oracle_gl.ogl_journal_entries.json` (`je_1ce7247752034cbc`): `approved_by = brenda.abbas@brookfieldcpas.com`.
  - `linear.linear_users.json`: Brenda Abbas as `npc_016`.
  - `slack.slack_users.json`: Brenda Abbas as `npc_016`.
- **Resolution:** Brenda's email domain is `brookfieldcpas.com` (per the persona-briefs note "Email domain for all personas and NPCs: brookfieldcpas.com"). She is listed as approver of record on the contested JE. The fact that her contact-card role is "Vendor account manager" while she is approving JEs is a deliberate hardness lever — agents in the trajectory caught this and flagged the approver-identity question as a documentation gap (Runs 1, 2, 3, 5, 6 all surface it). The rubric R8 and OE 2/8 correctly name her among stakeholders because she is on the JE as approver.
- **Dismissed.** No edit needed.

## No other findings dismissed in this pass

All other council-flagged signals resolved into either confirmed PASS or no-action-needed observations carried forward as non-failing notes.
