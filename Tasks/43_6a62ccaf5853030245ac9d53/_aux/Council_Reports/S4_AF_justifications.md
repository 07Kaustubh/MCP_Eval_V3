# Always-Failing Rubric Justifications: Mesa Vista 4C owner pass-through

Reviewer-facing batch. One entry per always-failing criterion. Each cites the concrete data fact and the specific reasoning gap observed in the runs.

---

## The Agent reports $1,812 as the corrected owner pass-through on Linda Castillo's Mesa Vista 4C make-ready.

All twelve runs reported $1,727 instead of $1,812. Every run reached the vendor bills and correctly re-derived the $1,340 repaint against the $1,140 the owner was charged, then dropped the $85 closet trim touch-up on bill 2026-519 as internal labor. That bill is billed by Permian Make-Ready Crew, the same outside vendor as the repaint, and its own note says the charge passes through to the owner. The agents read the opening words of that note, "Internal labor charge for Tony Reyes," and stopped there. This is the intended failure mode: the note's prose contradicts the vendor field on the same record, and the agents took the prose.

## The Agent reports the net understatement on Linda Castillo's Mesa Vista 4C bill as $190.

No run reached $190. Ten runs stated $105 and two never netted the two corrections at all. The $105 comes from raising the repaint by $200 and then deleting the whole $95 closet trim line rather than lowering it to the $85 the vendor charged. Getting $190 requires holding both corrections at once, a $200 increase and a $10 decrease, and the agents that removed the trim line never had the second correction to net.

## The Agent keeps the $85 bedroom closet trim touch-up billed by Permian Make-Ready Crew on Linda Castillo's Mesa Vista 4C owner pass-through as outside vendor work.

This is the root failure of the task and it swept both models, twelve runs out of twelve. The universe carries two signals that point the wrong way, the bill note naming Tony Reyes and a channel message saying Tony did the touch-up, and Tony Reyes is a real Star PM maintenance technician, so the wrong reading is available and tempting. Three things resolve it and the agents used none of them together: the bill's vendor is Permian Make-Ready Crew, the same note ends by instructing that the charge pass through to the owner, and Carlos's own summary to Linda places the closet trim inside Pete Donovan's repaint scope while saying separately that Tony's team handled the internal repairs in house. Nine runs pulled that summary message and none read its body, which arrives base64 encoded. Opus Run 3 went further and invented a line-item breakdown of the $85 bill into four internal labor components that appears nowhere in the data.

## The Agent corrects Mesa Vista 4C owner invoice 2026-534 so that it totals $1,812.

Every run wrote $1,727 to invoice 445653930748. The write itself was clean, targeting the right invoice, on the right customer, without creating a duplicate. Only the figure was wrong, carried straight from the closet trim misclassification.

## The Agent lowers the bedroom closet trim line on Mesa Vista 4C owner invoice 2026-534 from $95 to $85.

No run made this correction. All twelve deleted the line from the amended array rather than repricing it, so the amended invoice carries two lines where the correct one carries three. Several runs stated in their own summaries that the $95 charge should not be on the bill at all, which is the misclassification expressed as a write.

## The Agent states in the Mesa Vista 4C make-ready record carrying the Ready turn status that the final owner pass-through is $1,812.

Every run wrote the wrong figure into the notes field. Eleven wrote $1,727 and one wrote it into the stale In Progress row instead of the Ready row. The mechanics were right, the notes field was used correctly because the turn status field has no Closed option, and the number was the only defect.

## The Agent states in the email draft to Linda Castillo that her Mesa Vista 4C owner invoice has been corrected to $1,812.

All twelve drafts told the owner her invoice now reads $1,727. The draft was addressed correctly and several runs threaded it onto her original summary message, so the failure is confined to the figure being communicated to the owner.

## The Agent states in the email draft to Linda Castillo that the corrected figure is $190 more than she was originally billed.

No draft stated $190. Six drafts stated the net movement as $105 and six stated no net movement at all, listing the corrected lines without ever comparing the new total to the $1,622 she is holding. The second group is a separate gap from the arithmetic one: even on their own wrong total, those runs never told the owner how far her bill had moved.

## The Agent states in the channel message that the Mesa Vista 4C owner pass-through has been corrected to $1,812.

Every channel post carried $1,727. The posts went to the make-ready channel and read as intended for the crew and front office, so the wrong number is the whole of the failure. Because the point of the post is that colleagues work off the corrected figure, the wrong figure propagates to everyone downstream.

---

## Partial failures, same root

The following criteria failed on some runs rather than all, and the cause is the same closet trim misclassification or a near neighbour of it.

**The Agent identifies the Mesa Vista 4C bedroom closet trim touch-up on the vendor bill as $85.** Six Gemini runs never stated the $85 at all. Having decided the work was in house, they described the line only as a $95 removal and never surfaced what the vendor actually charged, so the figure needed to correct the bill was never put on the record.

**The Agent identifies the $85 unit condition inspection and punch list charge on bill 2026-481-566 from Alamo HVAC Services as StarPM in-house time that stays off Linda Castillo's owner pass-through.** Three Gemini runs excluded the wrong $85 charge. They named bill 2026-519 as the internal item and never mentioned the Alamo HVAC condition walk, which is the charge that genuinely is Carlos's own time. The two $85 bills were swapped.

**The Agent updates the Mesa Vista 4C make-ready record that carries the Ready turn status** and **The Agent states in the Mesa Vista 4C make-ready record carrying the Ready turn status that the 4C turn is closed on the owner side.** Gemini Run 3 wrote only to record recbd087a4abd605b, the stale In Progress snapshot, and left the live Ready record recc8534b3fd13954 untouched. The two rows disagree and the date fields run opposite to the modification order, so sorting on the dates picks the stale one.

**The Agent states in the email draft to Linda Castillo that Mesa Vista 4C is now closed on her side.** Six drafts explained the corrections and the new total but never told the owner the turn was finished on her side or that nothing further was outstanding. Six other drafts did say it, so the omission is a disposition the agents dropped rather than one the task made unreachable.

**The Agent states in the channel message that the corrected Mesa Vista 4C figure supersedes the figure Linda Castillo was originally billed.** Gemini Run 6 announced the new number without flagging that it replaces the one already sent, which leaves a reader who saw the original summary with two live figures and no indication which governs.
