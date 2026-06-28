# Filesystem Server — DO NOT USE FOR PROMPTS

The Filesystem MCP server has known issues. Do NOT craft prompts that require the agent to read or write files via `filesystem_read_file`, `filesystem_write_file`, or any other `filesystem_*` tool.

This folder has been intentionally emptied. All universe data for task creation and evaluation should come from the database-backed services only (see `Get_Universe_Data.sql`).
