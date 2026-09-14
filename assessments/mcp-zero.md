---
harness_id: mcp-zero
project_name: MCP-Zero
repository: https://github.com/xfey/MCP-Zero
review_ref: fd666c44c9290a671949b974444c30f4ab161622
reviewed_at: 2026-09-14
status: excluded-no-agentic-vsm
autonomy_s1: ?
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# MCP-Zero

## Review boundary
MCP-Zero at the pinned revision as the code released for the active-tool-discovery paper.

## Repository architecture
The repository contains retrieval/matching/sampling experiments and an MCP-tools dataset. Its README explicitly says the released paper code implements retrieval capabilities and that deployment/environment modules remain future work.

## Primary evidence
- `README.md`: paper-code file map; retrieval experiments; explicit statement that dynamic MCP deployment and GAIA environment deployment are future work.

## Inclusion decision
`excluded-no-agentic-vsm`: the repository does not supply a ready autonomous decision/action loop as the system-in-focus. It is a tool-discovery/retrieval method intended for autonomous agents, not itself an agent harness satisfying S1.

## VSM states
The `?` vector is structural placeholder metadata for the excluded record and is not published in TLDR/rankings. No VSM-function autonomy claim is made.

## Recursion, variety, escalation
MCP-Zero can attenuate tool-selection variety for another agent, but that supporting mechanism is not a viable operational unit by itself.