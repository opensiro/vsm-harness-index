---
harness_id: r2r
project_name: R2R
repository: https://github.com/SciPhi-AI/R2R
review_ref: 9c5a94d151f90876bd7eb860f300a8fd662dc481
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# R2R

## Review boundary
R2R at the pinned revision, focusing on its first-party agentic RAG/research-agent runtime.

## Repository architecture
R2R implements base agents plus RAG/research agents that use document retrieval, content and web-search tools for deep research through iterative tool interaction.

## Primary evidence
- `py/core/base/agent/agent.py`: base agent abstraction.
- `py/core/agent/rag.py`: RAG agent with file/content/web-search tools.
- `docs/documentation/retrieval/agentic-rag.md`: first-party agentic RAG/tool behavior.

## Operational model
A RAG/research agent is the S1 unit; retrieval/graph/web tools amplify its informational variety.

## S1 — Operations
`A`: the agent chooses search/retrieval tools and iterates toward research answers. Confidence: high.

## S2 — Coordination
`—`: no material multi-S1 coordination path is established at this boundary.

## S3 — Inside-and-now control
`?`: service/runtime management does not establish autonomous whole-system regulation.

## S3* — Complementary audit
`?`: source attribution/retrieval checks are part of normal production, not independent audit.

## S4 — Outside-and-then intelligence
`?`: web search is current-task environment sensing, not demonstrated prospective adaptation.

## S5 — Policy and identity
`?`: prompts/settings are parent-owned.

## Recursion, variety, escalation
Multiple retrieval modalities expand one S1's requisite variety without creating recursive viable units.