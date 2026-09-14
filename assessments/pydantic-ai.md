---
harness_id: pydantic-ai
project_name: Pydantic AI
repository: https://github.com/pydantic/pydantic-ai
review_ref: 5cbacfc8f86d653baa0ca2e31970cbf4f0fcec95
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Pydantic AI

## Review boundary
Pydantic AI at the pinned revision. The separately packaged Pydantic AI Harness is recognized where the repository explicitly integrates it, but its distinct implementation is not silently attributed to core.

## Repository architecture
Pydantic AI provides typed autonomous agent loops, tools, durable execution, web/realtime interfaces and capability composition. The repository documents optional Harness capabilities for memory, subagents, planning/context and an advisor model.

## Primary evidence
- `README.md`: typed extensible agent loop; autonomous tools; durable execution; explicit Harness/subagent/advisor integration and repository boundary.

## Operational model
An `Agent` is S1. Subagents/advisor capabilities can extend one agent's work, but delegation/second opinion alone does not establish S2 or S3*.

## S1 — Operations
`A`: agents autonomously choose tools/actions across iterative runs. Confidence: high.

## S2 — Coordination
`?`: first-party-supported multi-agent collaboration exists through Harness capabilities, but the coordination relation is not sufficiently evidenced at this repo boundary to classify anti-oscillation.

## S3 — Inside-and-now control
`?`: durable execution/contexts are runtime control rather than autonomous whole-system regulation.

## S3* — Complementary audit
`?`: an advisor provides a second opinion, but sufficient independence, alternative reality access and corrective authority are not established.

## S4 — Outside-and-then intelligence
`?`: planning/web search/memory do not by themselves establish S4.

## S5 — Policy and identity
`?`: instructions/approval remain parent-owned.

## Recursion, variety, escalation
Subagents/capabilities are compositional and do not by themselves establish recursion.