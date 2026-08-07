# Linter responses, 2026-08-07

## 1. Rubric Tests Unrequested Scope (FAIL): revised, no pushback

Flagged: "The Agent leaves the 24,275 R&D tax credit outside the funds available for the wind down."

Accepted. The prompt never mentions a tax credit, so the criterion was naming a subject the persona
never raised. Rewritten to grade the in-scope figure instead:

> The Agent's written account puts the funds available against the wind down at 13,300.

13,300 is the 10,800 of net data proceeds plus the 2,500 of cash on hand. The record still catches an
account that treats the credit as money in the bank, because that account puts funds available near
37,575 rather than 13,300, but nothing in the criterion asks about a subject the prompt did not raise.
Mirrored into the oracle events in the same pass.

## 2. Rubric Not More Specific Than Prompt (PASS): no action

## 3. Prompt Requirement Coverage (PASS): no action

## 4. Rubrics Atomicity: partly accepted

### 4a. Engagement figures criterion: accepted, revised

Flagged: "states one or more of these Combo Fighter engagement figures: a peak of 801 daily active
users, 845 lifetime new users, 55,101 lifetime sessions, or average D1 retention of 44.0 percent."

Accepted. Four alternatives in one criterion means a failure has no single cause. Rewritten to a
single figure:

> The Agent's written account states that Combo Fighter's daily active users peaked at 801 across
> both platforms.

801 is the combined ios and android peak on 2026-02-07; "across both platforms" is in the title
because the per-platform maximum is a different number on a different day, and the criterion should
not turn on which aggregation the reader assumes. The oracle event's content list was narrowed to
match.

### 4b. Lead-figure count criterion: dismissed

Flagged: "The Agent gives two or three figures in its final response as the ones it would lead with
on the angel calls."

Dismissing this one. The prompt's closing line is "Then tell me the two or three figures you would
lead with, if you were making those calls." The range is the user's own, and narrowing it to exactly
two or exactly three would fail an answer that does precisely what was asked. The criterion makes one
claim, that the count of lead figures falls in the range the user named, and it fails on one count,
one figure or four. Whether each figure is grounded is a separate criterion.

---

## Reviewer-facing text

Only the block below would go back to the platform if a written response is required. It carries no
internal terminology and cites the prompt sentence at issue.

> The prompt closes by asking for "the two or three figures you would lead with", so the range comes
> from the user rather than from us. Pinning an exact count would fail an answer that gives exactly
> what was asked for. The check is a single one, that the number of lead figures is two or three, and
> it fails cleanly on one, on four, or on none. Whether each of those figures is supported by the
> records is checked separately. Happy to revise if you read the closing line differently.

---

## 5. Rubric Tests Unrequested Scope, second pass: accepted, no pushback

Flagged: "The Agent leaves ANALYTICS.MONETIZATION.REVENUE_DAILY_V2 outside the Combo Fighter revenue
evidence set", with the companion criterion on ANALYTICS.MARKETING.UA_SPEND_UNIFIED_V2 named in the
reasoning.

Accepted, and the same reading was applied to the two remaining criteria of that shape rather than
waiting for them to be flagged separately.

Both mart criteria were removed outright. The only wrong answer those tables can produce is a report
that Combo Fighter has no revenue data or no spend data, and two criteria already contradict that
directly: the account has to state 0.00 revenue and 7,483.42 of acquisition spend. Naming the tables
added nothing except a subject the prompt never raises.

The Metabase and dbt check was reworded rather than dropped, because the underlying point is the
prompt's own: "that list got put together fast and nobody has been back over it properly". It now reads

> The Agent's written account identifies continuing paid user acquisition as the cost still running
> that the cancellation list does not cover.

which asks about the list the user raised instead of about two vendors the user never named.

The monthly net burn criterion was removed. It guarded against confusing two figures that happen to
share the value 22,500, but an account that meets the burn figure in the cash row still reports the
offer as 22,500 and the net as 10,800, so nothing graded moves either way. It was carrying an
out-of-scope subject for no discrimination.

The one criterion of this family kept is the data transaction being described in its licensing form
rather than as an outright sale, because the prompt raises that subject itself in "I know roughly what
we are getting for the data".

Rubric count 32 to 29. Oracle events mirrored in the same pass.

---

## 6. Overlapping items: accepted, opposite member cut

Flagged: the net proceeds check is subsumed by the gross-versus-net check, since an account that keeps
22,500 and 10,800 in separate roles has necessarily stated 10,800.

The implication is correct and the overlap is real. One of the two had to go. We cut the
gross-versus-net one and kept the plain net proceeds figure, which is the reverse of what the note
suggests, for two reasons.

First, the gross-versus-net wording can fail an account that is entirely right. "The data agreement
nets 10,800 after their 11,700 charge" gives the gross implicitly and is a complete, correct answer,
but a reader looking for both figures held apart could mark it down. The plain figure check has no
such failure mode: either the account says the net is 10,800 or it does not.

Second, nothing is lost. An account that stops at the 22,500 headline already fails on three other
checks: it does not state the net as 10,800, it cannot say the wind down service alone costs more than
the net, and it puts funds available at 25,000 rather than 13,300. The gross-versus-net wording was
the fourth guard on a point already guarded three times, and it was the softest of the four to read.

Count 29 to 28. The oracle events were updated to match.

---

## 7. Second linter set, 2026-08-07: 8 warnings across three checks

Set shape, checked before answering any of them: 28 criteria, 27 of which grade an end state and
exactly 1 of which grades order. 16 of the 28 titles carry no figure at all. Of the 10 criteria that
actually separated the six agent runs, 6 carry no figure.

Disposition: 6 invalid, 2 valid and already acted on.

### 7a. Process Supervision, three warnings: invalid

Flagged: "remove exact dates/amounts unless essential to detect procedural rigidity"; "these are
action/order checks, but they need broader wording to target workflow rigidity"; "avoid
solution-specific milestones; focus on whether the rubric forces a fixed method/sequence".

All three describe a set built to supervise method. This one is not that. There is exactly one order
check in it:

> The Agent's written account is created before its message is posted to the #winddown channel.

It names no tool, no service and no number of steps. Three runs wrote the account in Confluence and
three wrote it in Google Docs; all six passed it. Nothing anywhere in the set requires a particular
query, search term, tool or path. The other 27 checks are end-state checks, so widening them toward
"workflow rigidity" would be widening them away from what they grade.

### 7b. Overly Specified, collapse process steps and allow equivalents: invalid

Equivalent forms are already accepted, and the runs prove it. The written account is "a standalone
written page or document", which took two different forms across the six runs and passed every time.
The tracking item is "an issue tracker or task board", with no tracker named. The post "points to the
written account by link or by title", and runs did it both ways and passed.

The three deliverables stay separate because the request asks for three separate things: write it up,
then post it to Leonard and Arthur, and file a tracking item. Collapsing them gives one failure with
three possible causes, which is the thing an earlier round of this review asked us to fix elsewhere.

### 7c. Overly Specified, reduce exact-match brittleness: valid, already fixed

This one is right, and it had already been caught and corrected before the warning arrived. Two
acquisition totals were pinned to the cent, 7,483.42 and 8,452.64, but the warehouse serves whole
dollars on every numeric column. Every query returns 7,476 and 8,447 instead. No agent could have
produced the pinned figures, and two runs that had the scope and the window exactly right were marked
down over a five dollar gap. Both are now stated as the whole-dollar figures, with the exact ones
still accepted.

The figures that remain are not brittle. All six runs stated the 10,800 net and the 2,500 cash. Where
a figure check does separate runs, the split is a real difference in the work: the peak of 801 needs
the two platforms summed per day before the maximum is taken, and the runs that reported 784 or 426
had taken the maximum of the raw rows.

### 7d. Overly Specified, merge the finance checks: invalid

The runs show these are not interchangeable. One run stated the 10,800 net and the 2,500 cash and
never put the two together, so it passed both component checks and failed the funds-available total
of 13,300. A merged sufficiency check would score that run as fine. Separately, one run failed the
narrow point that the wind-down firm's price alone exceeds the net proceeds while passing the wide
point that funds fall short overall, which is the difference between noticing one line item and
adding up the whole picture.

### 7e. Contradictory, trim numbers unless all are verifiable in-source: valid, already fixed

Same underlying finding as 7c and the same fix. Every remaining number has been re-checked against
the records: the 2026-01-05 to 2026-02-09 window is where both the engagement and revenue tables
stop, revenue is 0.00 across it, the combined peak of 801 falls on 2026-02-07, cash on hand at month
end is 2,500, the 10,800 net is the 22,500 offer less their 11,700 charge, 13,300 is those two added,
and the wind-down firm's price is stated as about 15,000 in one place and as 13,000 to 15,000 in
another.

On the "possibly conflicting" half, there are two places where the same number means two things and
both are handled. 22,500 is the data offer and it is also February's net burn, so no check grades
22,500 at all. 13,000 is the low end of the wind-down quote and it is also February's legal line in
the burn table, so that check now says in as many words that the burn line does not satisfy it.

### 7f. Contradictory, separate workflow from content and clarify what is required: invalid

The request asks for all three, in its own words: "Write it up as one honest account ... Then post it
to him and Arthur in the wind down channel, and file a tracking item". Each has its own existence
check and all six runs produced all three.

Only one sequence is graded, the account existing before the post, because that is the only order the
request states. Where the tracking item falls is deliberately not graded. Order and content are
already held apart: the order check says it grades sequence only, and that whether either record is
correct or complete is graded elsewhere.

---

## Reviewer-facing text for set 7

> Two of these are fair and are already fixed. Two acquisition totals were written to the cent,
> 7,483.42 and 8,452.64, but the warehouse returns whole dollars, so a query gives 7,476 and 8,447 and
> no agent could ever have matched the cent figures. Both now ask for the whole-dollar figures. I also
> re-checked every other number against the records and separated the two places where one number
> means two things, since 22,500 is both the data offer and February's net burn and 13,000 is both the
> low end of the wind-down quote and February's legal line.
>
> On the process and merging points I would push back. Of the 28 checks, 27 grade an end state and one
> grades order, and that one names no tool or method: it only asks that the account exist before the
> post, which the request itself sequences. Alternatives are already open, the account can be a page or
> a document and the tracking item can be any tracker or board, and the runs used different ones and
> passed. Merging the finance checks would lose real signal, because one run stated the 10,800 net and
> the 2,500 cash and never added them, so it would pass a combined sufficiency check while missing the
> 13,300 the request asked for. Happy to revise if you read any of these differently.

---

## 8. Third linter set, 2026-08-07: 6 warnings

Disposition: 5 invalid, 1 fair and already fixed (the exact-cents totals, same finding as set 7).
W6 is answered by naming each source in the reply rather than by editing, since the reviewer
cannot see the records.

## W1. Process Supervision: "Replace exact facts/amounts with checks for method rigidity vs outcome quality"

Of the 28 checks here, 27 grade the end state and only one grades order, so there is almost no method supervision in the set to convert. The amounts sit inside the end-state checks, where they are the answer the request asks for rather than a step in a method, and half the titles carry no figure at all. Nothing anywhere names a query, a search term, a tool or a path. Replacing the amounts would leave checks that cannot separate a correct account from a plausible-sounding one, which is the only thing the request actually cares about.

## W2. Process Supervision: "If sequence matters, phrase as broad deliverables, not mandatory step order"

Sequence is graded once and only because the request states it: "Write it up as one honest account ... Then post it to him and Arthur in the wind down channel". The single order check asks that the account exist before the post and nothing else. It names no tool and no step count, and where the tracking item falls is deliberately left ungraded. The deliverables themselves are already phrased broadly, as a written page or document, a message in the channel, and an item on any issue tracker or task board.

## W3. Overly Specified: "Too many exact numbers/facts; allow reasonable variants and focus on substantive correctness"

Variants are already accepted wherever the records allow one. The account can be a page or a document, the tracking item can be any tracker or board, the post can point at the account by link or by title, and the wind down price is accepted either as a single figure or as a range. Two totals were genuinely over-tight and are now fixed: they were written to the cent as 7,483.42 and 8,452.64, while any query returns whole dollars, so they now ask for 7,476 and 8,447 with the exact figures still accepted. The numbers that remain are not brittle, since every run stated the 10,800 net and the 2,500 cash without trouble, and where a number does separate runs it reflects real work, as the peak of 801 needs the two platforms added together per day before the maximum is taken.

## W4. Overly Specified: "Channel-post criteria are over-specified; relax wording/link/title and keep core intent"

These are already at the loose end and the runs bear it out. The post check asks only that a message land in the wind down channel. Addressing the two founders is satisfied either way, and runs did it both ways: some tagged them by their user handles and one simply opened with "Leonard, Arthur". Pointing at the account is written as "by link or by title", and runs did each and were fine. Those three were satisfied by every run. The only two that separated runs are the ones carrying substance, the coverage conclusion and the continuing spend figure, which is the core intent you are asking to keep.

## W5. Contradictory: "Same spend figure repeated across artifacts; consolidate or scope each use"

Each use is already scoped to its own artifact, and each says which one it is checking: one for the written account, one for the message in the channel, one for the tracking item. The request treats them as three separate deliverables and asks for the figure in each, since the account is what Leonard hands to the angels, the post is what the other two founders read, and the tracking item is what keeps the cost from getting lost between the three of them. Consolidating would let an account that buries the figure in a long document and leaves it out of the post and the tracker still count as complete, which is the exact failure the request is trying to avoid. Each one also names what does not satisfy it, so a run that carries only the smaller single-title figure fails on its own terms in each place.

## W6. Contradictory: "Many exact figures assume hidden source data; clarify source/acceptance basis"

Fair, so here is the basis for each. The measurement window of 2026-01-05 to 2026-02-09 is where both the daily engagement table and the daily revenue table stop, and revenue sums to 0.00 across it. The peak of 801 is the two platforms added together on 2026-02-07, which matters because the largest single-platform row is 426 on a different day. Acquisition spend is 7,476 across the full record to 2026-02-28 and 8,447 across all three titles over the 19 days from 2026-02-10, both as the warehouse returns them, with the underlying 7,483.42 and 8,452.64 also accepted. Cash on hand at month end is 2,500 from the finance records, the 10,800 net is the 22,500 offer less the 11,700 they charge, both stated in the wind down channel, and 13,300 is those two added. The wind down firm's price is given as about 15,000 in one message and as 13,000 to 15,000 in the meeting notes, and either is accepted. Two numbers do double duty and both are separated in the wording: 22,500 is the offer and also February's net burn, so nothing grades 22,500 on its own, and 13,000 is the low end of the wind down quote and also February's legal line in the burn table, so that check says in as many words that the legal line does not satisfy it.

## Consolidated version, if only one box is available

One of these is fair and is already fixed. Two acquisition totals were written to the cent, 7,483.42 and 8,452.64, but a query returns whole dollars, so they now ask for 7,476 and 8,447 with the exact figures still accepted. On sources, the window is where both the engagement and revenue tables stop, revenue is 0.00 across it, the peak of 801 is the two platforms added together on 2026-02-07, cash at month end is 2,500, the 10,800 net is the 22,500 offer less their 11,700 charge, and 13,300 is those two added.

On the rest I would push back. Of the 28 checks, 27 grade an end state and one grades order, and that one only asks that the account exist before the post, which the request itself sequences. Variants are already open, since the account can be a page or a document, the tracker can be any board, and the post can point by link or by title, and runs took different routes on all three and were fine. The spend figure appears in three checks because the request asks for three separate deliverables, and each names its own artifact, so consolidating would let a run that leaves the figure out of the post and the tracker still count as complete. Happy to revise if you read any of these differently.
