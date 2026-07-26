# Linter Decision — Tasks/42_6a62ccac9492f2a60e456c1c

**Date:** 2026-07-25
**Mode:** Review (candidate prompt in `5_Prompt.txt`; kept pristine)
**Class:** A — Business alignment check, single finding (invented vendor)

## What the linter blocked
The "Benchmark/StarPM Business alignment check" returned FALSE on one finding: it claimed "Pete Donovan's crew" is an invented vendor absent from the Star PM universe, and suggested renaming the roofer to Big Bend Restoration. Every other dimension the check ran (systems, write actions, scope/authority, authoring seat, naturalness) passed.

## What we did: INVALIDATE with justification (no prompt edit)
Skeptical-first re-grep of the per-task universe contradicts the linter unambiguously:

- **Pete Donovan is a real universe entity.** Contact record (job "Exterior Painter", `pete.donovan@gmail.com`, contact_id `8628aa258df55e62a6d89f64897fce77`) and a QuickBooks **customer** entity (`proj-f6f9edfeae5c`, DisplayName "Pete Donovan"). The name appears 40+ times across the data.
- **The roof records name him directly.** Bill `528539050604` (Doc 2026-481) PrivateNote: "Pete Donovan quote accepted at $8,400." Owner AR pass-through invoice `109367557444` (Doc 2026-494) line description: "Pete Donovan Roofing, capital expenditure pass-through," and its note references "vendor bill 2026-481 (Pete Donovan)."
- **The vendor of record differs on purpose.** Both roof bills (`528539050604`, `301715729067`) book `VendorRef` = **Big Bend Restoration** (203). There is **no "Donovan Roofing" vendor**; Pete Donovan is a customer, not a vendor.

This vendor-of-record conflict (conversational surface says "Pete Donovan / Donovan Roofing," the AP record books Big Bend) is the flagship structural trap of this task — the symmetric skip that neither model is expected to sweep. The prompt names Pete Donovan precisely because that is what Brooke believes from the emails and Slack posts going in; the agent's job is to open the AP store and discover the payable is booked against Big Bend. The linter's premise ("not present in the universe") is factually false.

## Why NOT revise
The linter's suggested revision — "Big Bend Restoration is confirmed for the work" — would write the vendor-of-record answer directly into the prompt, collapsing the flagship trap and handing the agent the derived fact the rubrics are built on. Revising would actively degrade the task. This is a clearly-wrong linter, so the cheap and correct move is invalidation.

## Re-check for missed issues (linter under-inclusive)
Independent re-read of `5_Prompt.txt` found no additional defect. The prompt correctly avoids leaking the headline `$8,400`, the vendor of record, and the duplicate bill (all of which must stay hidden per the answer-leak constraint). The conditional "if anything does not line up, bring it back to me first" is the intended payment-HOLD gate. No revision warranted.

## Final state
- `5_Prompt.txt` — **unchanged** (Review-mode original preserved for rating).
- `_aux/Linter_Justifications.md` — pushback authored, voice gate clean (0 hits).
- `Tasks/_meta/Linter_Justifications.md` — appended.
- AUDIT — skipped (justification-only resolution, no new artifact to audit).
