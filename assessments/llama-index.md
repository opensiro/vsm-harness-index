---
harness_id: llama-index
project_name: LlamaIndex
repository: https://github.com/run-llama/llama_index
review_ref: 7169bcd0dca2e16aecc8e0247f34e50079d9c0d5
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# LlamaIndex

## Review boundary
LlamaIndex OSS at the pinned revision. LlamaParse/LlamaCloud hosted platform behavior is not imported unless represented by first-party OSS code in this repository.

## Repository architecture
The framework supplies data connectors, indexes/graphs, retrieval/query engines, agentic application tooling, workflows, and integrations. The README describes a broad orchestration toolkit and points to agents built with Workflows/Agent Builder while keeping document/data access central.

## Primary evidence
- `README.md`: OSS agentic-application framework, orchestration toolkit, retrieval/query interfaces, integrations, Workflows and agents.

## Operational model
A tool/retrieval-using agent can be an S1 unit. Query engines, retrievers and workflow steps are not automatically separate S1 units; orchestration claims alone do not establish S2.

## S1 — Operations
`A`: first-party agentic applications can autonomously choose retrieval/action paths to produce task outcomes. Confidence: high.

## S2 — Coordination
`?`: Workflows and agent orchestration exist, but reviewed evidence does not establish whether the standard path regulates interference among autonomous S1 units rather than routing/sequencing them.

## S3 — Inside-and-now control
`?`: no verified agent-owned whole-system regulator with resource/commitment authority.

## S3* — Complementary audit
`?`: benchmark/verification material is not evidence of an independent audit function in deployed agent operation.

## S4 — Outside-and-then intelligence
`?`: data access and document agents do not by themselves establish prospective environmental adaptation.

## S5 — Policy and identity
`?`: no verified runtime ultimate-policy closure.

## Recursion, variety, escalation
The data/integration layer strongly amplifies S1 informational variety. Workflow nesting is not counted as VSM recursion without durable local viability and metasystemic closure.