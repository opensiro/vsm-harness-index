---
harness_id: mcp-zero
project_name: MCP-Zero
repository: https://github.com/xfey/MCP-Zero
review_ref: fd666c44c9290a671949b974444c30f4ab161622
reviewed_at: 2026-09-15
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
Deep re-review of MCP-Zero at the pinned paper-code revision, treating catalog position 61 explicitly rather than skipping the excluded record.

## Repository architecture
The released repository is an active tool-discovery/retrieval method and MCP-tools dataset. Its executable surface is composed of retrieval experiments, matching, reformatting, sampling and dataset-building utilities. It does not ship the autonomous environment/action loop that would make MCP-Zero itself an operational agent harness.

## Primary evidence
- `README.md`: released paper-code tree consists of APIBank/MCP-tools experiments, `matcher.py`, prompts, reformatter, sampler and retrieval utilities.
- `README.md`: explicitly states that the released code implements retrieval capabilities, while dynamic MCP-server deployment and GAIA environment deployment remain future work.

## Inclusion decision
`excluded-no-agentic-vsm`: MCP-Zero attenuates tool-selection variety for another autonomous agent, but the pinned repository is not itself a ready autonomous decision/action system satisfying the minimum S1 boundary.

## VSM states
The `?` vector remains structural placeholder metadata required by the assessment schema. Because the record is excluded, it is not rendered into `TLDR.md` or `RANKINGS.md`, and no VSM-function autonomy claim is made.

## Recursion, variety, escalation
The retrieval method can support an agent by discovering a relevant tool set. That supporting capability is not a viable operational unit on its own.