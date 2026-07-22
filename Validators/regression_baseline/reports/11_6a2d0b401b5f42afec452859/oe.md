# Validator report: oe

**Status:** FAIL  
**Fails:** 1 · **Warns:** 2 · **Notes:** 2

## FAIL
- OE step 5: parameter `late_post_authorization_id` bound to tool(s) ['oracle_gl_get_journal_entry'], but `late_post_authorization_id` exists only on ['oracle_gl_post_journal_entry']. Wrong tool binding — bind to the correct tool, or use a different parameter that exists on the named tool.

## WARN
- OE step 8 (X3 service-mapping): step text references `accounts` (expected service `oracle_gl` per brookfield oe_service_map) but tool call(s) target service(s) ['records_vault']. Verify the right service is being used for this data type. WARN-only observation period.
- OE step 11 (X3 service-mapping): step text references `accounts` (expected service `oracle_gl` per brookfield oe_service_map) but tool call(s) target service(s) ['blackline']. Verify the right service is being used for this data type. WARN-only observation period.

## NOTE
- universe: brookfield
- OE step count: 17
