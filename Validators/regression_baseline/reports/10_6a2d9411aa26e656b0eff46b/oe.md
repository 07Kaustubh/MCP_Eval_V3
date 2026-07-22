# Validator report: oe

**Status:** PASS  
**Fails:** 0 · **Warns:** 4 · **Notes:** 2

## WARN
- only 7/12 OE lines start with a recognized action verb (Search / Send / Call / etc.). V3 references use action-first openings consistently.
- OE step 2 (X3 service-mapping): step text references `reconciliations` (expected service `blackline` per brookfield oe_service_map) but tool call(s) target service(s) ['email']. Verify the right service is being used for this data type. WARN-only observation period.
- OE step 2 (X3 service-mapping): step text references `documents` (expected service `records_vault` per brookfield oe_service_map) but tool call(s) target service(s) ['email']. Verify the right service is being used for this data type. WARN-only observation period.
- OE step 4 (X3 service-mapping): step text references `accounts` (expected service `oracle_gl` per brookfield oe_service_map) but tool call(s) target service(s) ['blackline']. Verify the right service is being used for this data type. WARN-only observation period.

## NOTE
- universe: brookfield
- OE step count: 12
