# Prompt Writing Anti-Patterns & Guidelines

## ❌ Mistakes to Avoid

### 1. Cloning QC Sample Tonality
The passed samples share a recognizable pattern:
- "Go through everything and surface every..."
- "I need the full picture: what happened, who was involved..."
- "Dig through our emails, Slack, project tickets..."
- "Email me the full [X] and loop in [Y]"
- "CC our CEO", "flag the biggest risks to [person]"

**These are reference structures, not templates.** Repeating them produces prompts that feel mass-produced.

### 2. Enumerated Action Lists Disguised as Prose
Many samples end with a stack of "do X, then Y, then Z, and also post in channel." While technically valid, overusing this creates a command-list feel.

**Instead:** Let actions emerge naturally from the situation. The persona should describe their *problem*, not their *to-do list*.

### 3. Over-Signaling the Investigation
Phrases like "check our messages, emails, and project records" are borderline tool-hinting. A real person wouldn't inventory their own company's systems — they'd describe what's wrong and expect you to figure out where to look.

### 4. Generic Urgency Framing
"Before it blows up", "keeping me up at night", "I can't tell you what the net position is anymore" — these are fine individually but become patterns when repeated across tasks.

**Instead:** Ground urgency in specific, concrete consequences unique to this scenario.

### 5. Formulaic Closing Actions
Almost every sample ends with: email [boss], CC [CEO], post in [channel]. Diversify the *shape* of the output — not everything has to culminate in a summary email to leadership.

---

## ✅ What Makes a Prompt Feel "Runny" (Natural & Flowing)

### Voice Principles
- **Situational, not procedural** — describe the mess, not the cleanup steps
- **Mid-thought entry** — the persona is already in the middle of dealing with something, not starting fresh
- **Emotional texture** — frustration, confusion, relief, skepticism — real people have reactions
- **Asymmetric knowledge** — the persona knows some things but not others, and that gap drives the ask
- **Conversational asides** — "I think", "if I remember right", "unless I'm wrong about..."

### Structural Variety
- Don't always open with "[Person] told me [thing]" 
- Don't always close with "email [person] the results"
- Let the prompt breathe — not every sentence needs to advance the plot
- Mix certainty with uncertainty within the same ask

### Data Injection Philosophy
- **Augment, don't contradict** — new data must be consistent with existing names, dates, amounts, relationships
- **Create friction** — inject data that makes the *investigation* harder (conflicting Slack messages, partial email threads, ambiguous records)
- **Support the ground truth** — every claim the prompt implies should be verifiable through at least one data source
- **Cross-service threads** — the best injections create breadcrumbs across 2-3 services that the agent must connect

---

## 🎯 Checklist Before Submitting a Prompt

- [ ] Prompt should be complex enough to fail opus 4.5 for making the prompt more hard we can make senarios and edit universe data  
        "Docs/10_How_To_Load_and_Edit_Universe.md' , Brookfield_Base_Universe/4_Scenario_Storylines.md Brookfield_Base_Universe/7_Brookfield_Universe_One_pager.md
- [ ] Read it aloud — does it sound like a real person talking?
- [ ] Remove any sentence that could apply to ANY MoveOps task
- [ ] Verify no tool names, parameter names, or system names are mentioned
- [ ] Confirm the voice is distinct from all 12 sample tasks
- [ ] Check that actions are implied by the situation, not listed as instructions
- [ ] Ensure at least one piece of information requires cross-service triangulation
- [ ] Validate all referenced data exists (or will be injected) in the universe
- [ ] Never use emdashes in the prompt
