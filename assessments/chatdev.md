---
harness_id: chatdev
project_name: ChatDev
repository: https://github.com/OpenBMB/ChatDev
review_ref: 4fb2db0ea90375ce1059f44fe03ffbd191a7a169
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ChatDev

## Review boundary
ChatDev 2.0/DevAll at the pinned revision, including its configurable agents, workflows and execution strategies. Legacy ChatDev 1.0 and experimental branches are supporting historical evidence, not silently merged into the standard distribution.

## Repository architecture
ChatDev is a configurable multi-agent workflow platform. The pinned runtime supports DAG, cyclic and majority-vote execution strategies over configured agent nodes.

## Primary evidence
- `workflow/graph.py`: selects DAG, cycle or `MajorityVoteStrategy` execution according to the authored graph configuration.
- `workflow/runtime/execution_strategy.py`: DAG/cycle strategies execute the configured graph; `MajorityVoteStrategy` sends the same initial input to multiple nodes, executes them in parallel, collects outputs and selects the most common non-empty result.
- The pinned runtime tree contains executor/runtime machinery for those configured workflows; the orchestration itself is authored topology rather than an autonomous whole-system manager.

## Operational model
Configured agents perform S1 work. DAG/cycle execution is workflow routing. Majority voting is different: it explicitly reconciles competing peer outputs into one accepted outcome, which can instantiate a coordination function, but only when the user selects that topology.

## S1 — Operations
`A`: configured agents autonomously perform bounded task work. Confidence: high.

## S2 — Coordination
`C`: the first-party majority-vote strategy provides a concrete composable conflict-resolution mechanism across multiple S1 outputs. It is not the default closed coordination policy and must be selected/configured by the parent, so it does not reach `A`. Confidence: medium-high.

## S3 — Inside-and-now control
`—`: graph executors and node scheduling follow authored workflow structure; no autonomous superior regulator owns current whole-system priorities, resources or commitments.

## S3* — Complementary audit
`—`: majority voting is peer-output reconciliation (S2), not an independent audit function. No distinct standard reviewer compares operational claims with evidence and returns corrective findings.

## S4 — Outside-and-then intelligence
`—`: workflow execution and task-local agent reasoning do not establish a prospective environment/intelligence loop for future organizational adaptation.

## S5 — Policy and identity
`—`: roles, workflow topology, voting mode and ultimate task/policy boundary are parent-authored.

## Recursion, variety, escalation
Large or cyclic agent graphs do not imply VSM recursion without durable local viable-system closure.