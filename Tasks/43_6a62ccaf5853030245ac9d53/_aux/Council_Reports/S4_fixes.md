# Bucket 1 — Rubric Invalid · Task 43_6a62ccaf5853030245ac9d53 (StarPM V4, dual-model)

**Bucket 1 count: 0 of 15 failing rubrics. No rubric change is required and none is recommended.**

Bucket 1 ratio = 0/15 = 0.0% → All-Failing Rubrics sub-dim **5/5 (PASS)**.

This file records the two candidates that were examined seriously and rejected, so the reasoning is on the record if the platform reviewer raises either.

---

## Candidate 1 (rejected) — "The Agent keeps the $85 bedroom closet trim touch-up ... as outside vendor work"

**Why it looked like Bucket 1.** It failed 12 of 12 runs across two independent model families, and both families converged on the *same* alternative answer ($1,727) rather than scattering. The v15 checklist flags exactly this shape at point 5: if no run passes despite a valid-looking approach, suspect the rubric. The universe also carries two agent-reachable signals that support the agents' reading:

- Bill `546359391323` (`DocNumber 2026-519`) opens its `PrivateNote` with "Internal labor charge for Tony Reyes touch-up on Mesa Vista 4C closet trim." All 12 runs retrieved this record in full.
- Slack C004 carries "Jaime flagged a paint touch-up on the bedroom closet trim. Tony got it done today, Airtable updated." 8 of 12 runs retrieved it.
- `contacts.contacts.json` confirms `tony.reyes@starpm.com` is Star PM's own Lead Maintenance Technician, so "Tony did it" genuinely does read as in-house time under the prompt's exclusion.

**Why it is nonetheless Bucket 3.** Three independent discriminators point the other way and all three are reachable:

1. **Structured field beats prose on the same record.** `VendorRef.name` on that bill is "Permian Make-Ready Crew", vendor id 204, the identical outside vendor as the $1,340 repaint on `PD-2026-09` that every run accepted as owner-billable without hesitation.
2. **The same note answers the question directly two sentences later.** "Pass-through to owner - pair with corresponding AR invoice to Pete Donovan's owner account for 4C make-ready close-out." Every run had this text in its context window and none acted on it.
3. **The corroborating document is reachable and was retrieved.** OE 7 prescribes `search_threads` then `get_thread (threadId: "66132537181ecbe1")`. Nine of twelve runs made exactly that call. `get_thread` returns the full body in `payload.body.data`, base64 encoded, 842 bytes. Decoded it reads: *"Pete Donovan finished the interior repaint (including a touch-up on the bedroom closet trim that came out of our QC walkthrough), and Tony's team handled all internal repairs in-house."* That single sentence settles the split in the rubric's favour and explicitly separates the trim from Tony's in-house work. **Zero of twelve runs decoded it.** Gemini Run 2 ran base64 decoding on other content at calls 7 through 12 of the same run, then retrieved this thread at call 21 and left it encoded, so the capability was in hand and simply not applied.

The prompt's exclusion clause is also narrower than the agents treated it: "an internal walk or a condition check we handled in house". A repaint touch-up is neither. The charge that *does* match that clause is the Alamo HVAC condition walk on `2026-481-566`, which the rubric set separately requires the agent to exclude, and which three Gemini runs got wrong in the opposite direction.

**Verdict:** the ground truth is uniquely determined and reachable through the prescribed call path. The failure is a genuine evidence-weighting failure at a designed landmine, not an unreachable answer. Bucket 3.

**One honest caveat recorded for the reviewer:** the decisive corroboration sits behind a base64 decode step that no run performed. The rubric survives without it, on `VendorRef` plus the pass-through clause alone. But if the platform reviewer disputes the closet-trim ground truth, nine rubrics fall together. See the concentration-risk note in `S4_verdict.md`.

---

## Candidate 2 (rejected) — "The Agent states in the email draft to Linda Castillo that Mesa Vista 4C is now closed on her side"

**Why it looked like Bucket 1.** v15 checklist point 3 asks whether the criterion is actually required by the prompt. The prompt binds the closure statement to the Airtable record, not to the email: *"get our 4C make-ready record in Airtable updated so it shows the final owner cost and the unit fully closed."* The email ask is separate and softer: *"email Linda a short note letting her know where it landed."*

**Why it is nonetheless Bucket 3.** The task's opening sentence frames the whole request as *"Mesa Vista 4C is one I want fully closed on the owner side"*, and "where it landed" is a disposition ask, not only a figure ask. The evidence field accepts three distinct expressions (closed, finalized on the owner side, or no further owner charges outstanding), which is as flexible as this criterion can be made without grading nothing. Six of twelve drafts satisfied it spontaneously, so it discriminates rather than blocks.

**Verdict:** valid but the weakest criterion in the set. No change. Flagged in `S4_verdict.md` as the one criterion to expect a platform-QC challenge on.

---

## Actions

None on `7_Rubrics.json`. The file ships unchanged.
