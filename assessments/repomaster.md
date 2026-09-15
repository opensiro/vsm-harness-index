---
harness_id: repomaster
project_name: RepoMaster
repository: https://github.com/QuantaAlpha/RepoMaster
review_ref: 9cf59930102970d61d6eb2f702fd936d3cda7f11
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# RepoMaster

## Review boundary
Deep review of the pinned scheduler/repository-agent implementation. AutoGen collaboration and mode switching are tested against VSM decision rights rather than treated as S2 solely because multiple agent objects participate.

## Repository architecture
RepoMaster uses an assistant scheduler plus execution proxy and specialized repository/search/code agents. The scheduler agent analyzes the current user task, selects a mode/tool/repository, invokes operational agents and can try another repository or mode when an attempt fails. This is hierarchical task routing and fallback within one problem-solving trajectory, not mutual regulation among autonomous operational units.

## Primary evidence
- `src/core/agent_scheduler.py`: `scheduler_agent` creates a current-task plan, chooses web/repository/general-code modes and invokes tools one at a time.
- Repository-mode fallback evaluates the latest operational result and sequentially tries another repository if needed.
- `user_proxy` acts as an execution proxy for scheduler tool calls rather than an independently governed operational S1 with shared commitments.

## Operational model
A scheduler agent chooses how to solve the current request and calls repository/search/code execution capabilities, evaluating returned results and switching approach when necessary.

## S1 — Operations
`A`: repository/code agents autonomously explore, execute and react to task results inside their configured mode. Confidence: high.

## S2 — Coordination
`—`: scheduler→tool/agent routing and sequential fallback are delegation/orchestration. No mechanism was established for regulating interference, oscillation or shared constraints among multiple autonomous S1 units. The shallow `S2=C` interpretation is removed.

## S3 — Inside-and-now control
`—`: the scheduler manages a current problem-solving plan but does not expose whole-system authority over persistent shared resources, capacities or multi-S1 commitments.

## S3* — Complementary audit
`—`: result evaluation is performed by the same scheduler trajectory; no separate complementary audit channel was established.

## S4 — Outside-and-then intelligence
`—`: web/repository search gathers external information for the current objective, not a prospective intelligence function responsible for adapting future system strategy/capability.

## S5 — Policy and identity
`—`: modes, prompts, tools and termination policy are developer-defined.

## Recursion, variety, escalation
RepoMaster has useful hierarchical operational variety and fallback behavior, but the reviewed metasystem boundary remains open.