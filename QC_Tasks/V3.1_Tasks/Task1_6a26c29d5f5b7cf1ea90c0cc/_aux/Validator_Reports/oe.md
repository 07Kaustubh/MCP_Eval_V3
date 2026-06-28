# Validator report: oe

**Status:** FAIL  
**Fails:** 4 · **Warns:** 1 · **Notes:** 1

## FAIL
- em-dash / en-dash at offset 6226: `pt ("The unpaid one — pull its current p`
- em-dash / en-dash at offset 6311: `ith what you find") — the paid record ai`
- linear_create_issue uses `team` — should be `teamId`
- OE step 10: parameter `table_id` bound to tool(s) ['airtable_list_records', 'airtable_list_tables'], but `table_id` exists only on ['airtable_create_field', 'airtable_delete_records', 'airtable_describe_table'].... Wrong tool binding — bind to the correct tool, or use a different parameter that exists on the named tool.

## WARN
- OE step 17: bolt-on candidate — `Set a reminder for early next week to recheck the blocked filing workstream usin...` shares no named entities with any other OE step. Apply remove-step test: if the rest of the OE chain still makes sense, this is a Coherence violation.

## NOTE
- OE step count: 22
