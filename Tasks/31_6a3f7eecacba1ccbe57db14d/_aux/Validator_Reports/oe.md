# Validator report: oe

**Status:** PASS  
**Fails:** 0 · **Warns:** 1 · **Notes:** 1

## WARN
- OE step 15: sends email to william.white@brookfieldcpas.com but no earlier OE step performs a contact lookup. Dependency chain: typically needs contact-lookup step (contacts_search_contacts or similar) before the send.

## NOTE
- OE step count: 18
