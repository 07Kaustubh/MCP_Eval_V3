# REVIEW dismissed findings

Findings the council surfaced that the per-task universe contradicted, so they did not make it into `changes.md`.

## 1. Hannah Grant role mismatch
- **Council claim**: Hannah Grant is "Corporate Tax Senior" but the prompt and OE 4 cast her as identifying an AP duplicate posting during a Q1 AP review.
- **What the universe actually shows**: The exception `exc_a0f77f2a19104e` has `identified_by: hannah.grant@brookfieldcpas.com` (verified in `blackline.blackline_exceptions.json`). Hannah's contact record is "Corporate Tax Senior" with description "Corporate tax senior; I pull Hannah in when client accounts have tax knock-ons or deadlines are getting tight." Hannah's slack post by persona_004 in C005 at ts=1779895920 explicitly states she caught the item during Q1-2026 AP review prep. The universe itself authored this attribution; the candidate is faithfully reflecting it.
- **Decision**: Not added to `changes.md`. This is universe-authored, not a candidate-introduced error.

## 2. VEN-441207 not in SAP AP invoices
- **Council claim**: Rubric 6 requires the agent to name vendor `VEN-441207` but no SAP AP invoice for that vendor exists in the universe.
- **What the universe actually shows**: Verified - `VEN-441207` count in `sap_subledger.ap_invoices.json` is 0, and the amount `6328.86` count in AP invoices is also 0. The vendor is mentioned exactly once in the universe: Hannah's slack post. The agent is expected to trust the slack breadcrumb (it cites consecutive invoice numbers and an 11-day-apart pattern). This is a deliberate hardness lever - the agent has to commit to a vendor identified only from a Slack message, with no posted invoice to corroborate. The Run #2 fail in `8_Verifier_Fails.txt` confirms this lever bites (Run #2 never named VEN-441207).
- **Decision**: Not a candidate error. Noted in `REVIEW_hardness.md` as the validated "vendor-only-in-slack" lever.

## 3. No replies under thread_ts 1779891480 yet
- **Council claim**: The persona_014 close-coordination breadcrumb post at ts=1779891480 has `reply_count=2` but a thread_ts query for `1779891480.000000` returns 0 replies in `slack.slack_messages.json`.
- **What the universe actually shows**: The reply_count field is metadata; the actual reply rows may be hydrated dynamically by the slack tools at call time, or may live elsewhere in the universe schema. The agent's `slack_conversations_add_message` call with `thread_ts="1779891480.000000"` is still well-targeted because the parent message exists and is on-topic.
- **Decision**: Not a candidate error. The thread parent atom is real; the reply set is irrelevant to the OE/rubric grading.
