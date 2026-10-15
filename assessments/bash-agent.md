---
harness_id: bash-agent
project_name: bash-agent
repository: https://github.com/lloydzhou/bash-agent
review_ref: e0062d42f7016f40639a8e69070131d521194cc1
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# bash-agent

## Review boundary

- System in focus: the published first-party Bash implementation `src/agent.sh` at frozen source SHA e0062d42f7016f40639a8e69070131d521194cc1, with supported async SubAgent sessions, not a composite grade importing the C, Go and Rust ports.
- Purpose and identity: minimal local terminal coding assistant with model-tool feedback, session persistence, context compaction and asynchronous child delegation.
- Standard-distribution boundary: Bash 5+ and utilities awk/curl/rg in README.md, with agent_loop/agent_loop_stream and in-process tool dispatch. Other language ports counted only as claims of parallel implementations, not sources of graded Bash organizational authority.
- Relevant environment: user command, model responses, filesystem/tools, persisted conversations and FIFO notifications.
- First-party modes considered: main coding loop, SubAgent fork/non-fork one-level asynchronous child sessions, streaming JSON events and tool policy.
- Recursion: one main operating model-guided Bash agent, optionally multiple independently looping child processes under shared workspace; no demonstrated higher organizational control authority.
- Profile 0.2.4 / Methodology 0.3.7.
- Credited operating / distribution surfaces: src/agent.sh agent_loop_stream, agent_loop, Bash tool dispatch, SubAgent process and FIFO return; docs/bash-tool-policy.md and sessions architecture for first-party permissions/history.
- Adjacent first-party surfaces excluded from ownership: other C/Go/Rust port implementations, external model inference server, maintainer CI and tests, docs-only architecture proposals, user project policy and any separate deployed orchestrator.


## Repository architecture

At frozen ref, `src/agent.sh` defines `agent_loop_stream`, a bounded while-turn iteration reading model replies, selecting each TOOL_CALL, executing `tool_dispatch`, and persisting tool results before subsequent model turns. `tool_sub_agent` launches a subshell after optional conversation fork and calls the same `agent_loop` for the new child session; a notification FIFO carries terminal AGENT_RESULT back into the main model context. Depth caps forbid recursive grandchildren. The architecture and sessions documentation explain local persisted conversations and compacting context. Bash tool policy and host permissions enforce operator constraints; they do not decide semantic coding actions. Other language ports cannot donate autonomy or audited metasystems to the Bash implementation.

## Operational model

A main model chooses terminal/repository actions, receives tool results, persists them and can continue. When asked to split independent subtasks, the model can launch true asynchronous child loops with their own session and optional forked context. They report results through FIFO as child messages; the parent can choose subsequent actions after seeing them. These mechanisms demonstrate first-party S1 loops but not specialized conflict resolution, whole-current S3 resource regulation, independent audit or future strategy.

## S1 — Operations

- State: A
- Function: Repeatedly choose and execute developer-task tools based on model outputs and changing code/tool feedback.
- Disturbance / variety regulated: Coding task, repository mutations, host shell result, model response and operator constraints.
- Decisive decision or feedback right: Choose a function-specific decision from observed changes to currently operating conditions.
- Decision owner: First-party Bash agent_loop model actor with llm_call and direct tool dispatch; the OpenAI-compatible provider supplies inference.
- Supporting / enforcement mechanisms: agent_loop_stream, tool_dispatch, store_conv_add_tool_results, agent_loop parent process, bounded MAX_TURNS and tool permissions.
- Closure path: User objective → model completion/action → tool execution → persisted tool result/history → another model call and task-specific next action or finish.
- Why this is / is not agent-owned: The shipped Bash agent_loop_stream repeatedly sends persisted conversation state to the model, executes tool calls via tool_dispatch, records results, and continues to a new model turn; child subprocesses run that same loop.
- Boundary reachability: The declared first-party packaged CLI or runtime directly exposes and runs the described mode without borrowing any external agent task loop.
- Evidence: [src/agent.sh](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/src/agent.sh); [docs/BASH_ARCHITECTURE.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/docs/BASH_ARCHITECTURE.md); [README.en.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/README.en.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: high.
- Caveats: Pinned first-party Bash distribution only, not external agents or separately implemented ports' unverified behavior.

## S2 — Coordination

- State: —
- Function: Attenuate actual interference between independently adapting child coding S1 workers and return revised work scopes.
- Disturbance / variety regulated: Multiple child edits may overlap within the same host workspace, while asynchronous reports arrive at different times.
- Decisive decision or feedback right: Choose a function-specific decision from observed changes to currently operating conditions.
- Decision owner: The parent model chooses initial child tasks and receives FIFO results; deterministic session-depth guard and background process signaling are not inter-S1 conflict-resolution owners.
- Supporting / enforcement mechanisms: SubAgent fork/subsession, NOTIFY_FIFO and AGENT_RESULT delivery, subagent depth cap, parent async result injection.
- Closure path: Parent launches independent child goals → children run their own model/tool loops → notifications return summaries to parent; no specific inter-child collision sensor/adaptive corrective-return path is evidenced.
- Why this is / is not agent-owned: SubAgent creates multiple independent Bash child model loops in background sessions; they share host filesystem and results arrive asynchronously, but no write-conflict sensing and model-owned inter-child rescope/repair is established.
- Evidence: [src/agent.sh](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/src/agent.sh); [docs/sessions.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/docs/sessions.md); [README.en.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/README.en.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Pinned first-party Bash distribution only, not external agents or separately implemented ports' unverified behavior.

### Absence scope

- Surfaces inspected: SubAgent tool implementation, Bash processes, FIFO notifications, child session files, tool dispatcher.
- Plausible first-party paths checked: parallel SubAgents as an S2 owner, context fork as workspace separation, shared-filesystem conflict management, automatic worker rescope.
- Why no material first-party path remains: context/session isolation does not isolate repository writes or supply a concrete conflict report; the parent receives completion results, not a closed specialized inter-S1 attenuation decision.

## S3 — Inside-and-now control

- State: —
- Function: Control whole-current active child S1 commitments and resources with discretionary team-wide intervention.
- Disturbance / variety regulated: Coding task, repository mutations, host shell result, model response and operator constraints.
- Decisive decision or feedback right: Choose a function-specific decision from observed changes to currently operating conditions.
- Decision owner: No distinct first-party owner with the full function-specific decision authority is established.
- Supporting / enforcement mechanisms: Built-in bounded agent loop, tool dispatcher, session history and deterministic operational gates.
- Closure path: A bounded tool/execution path exists without the required separate organizational judgment and corrective return.
- Why this is / is not agent-owned: Although a parent can launch children, the shipped Bash loop lacks a whole-child-roster management interface that selects and returns real current priority/reallocation decisions across still-active agents.
- Evidence: [src/agent.sh](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/src/agent.sh); [docs/sessions.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/docs/sessions.md); [docs/BASH_ARCHITECTURE.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/docs/BASH_ARCHITECTURE.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Pinned first-party Bash distribution only, not external agents or separately implemented ports' unverified behavior.

### Absence scope

- Surfaces inspected: parent/subagent process status, active-task file, notifications, session/fork state, turn limits.
- Plausible first-party paths checked: active task count as whole-current control, parent reassigning active children on completion, structured child cancellation and per-agent budget decisions.
- Why no material first-party path remains: the active task count and completion notifications monitor bounded execution, while live whole-organization resource decisions are not made by a distinct first-party controller.

## S3* — Complementary audit

- State: —
- Function: Independently inspect operational evidence from a complementary vantage and return an audit-based correction to the present S3 controller.
- Disturbance / variety regulated: Coding task, repository mutations, host shell result, model response and operator constraints.
- Decisive decision or feedback right: Choose a function-specific decision from observed changes to currently operating conditions.
- Decision owner: No distinct first-party owner with the full function-specific decision authority is established.
- Supporting / enforcement mechanisms: Built-in bounded agent loop, tool dispatcher, session history and deterministic operational gates.
- Closure path: A bounded tool/execution path exists without the required separate organizational judgment and corrective return.
- Why this is / is not agent-owned: The runtime stores model/tool history and shows tool output, but no separately owned audit observer with direct evidence inspection and a returned S3 corrective decision is shipped.
- Evidence: [src/agent.sh](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/src/agent.sh); [docs/BASH_ARCHITECTURE.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/docs/BASH_ARCHITECTURE.md); [README.en.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/README.en.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Pinned first-party Bash distribution only, not external agents or separately implemented ports' unverified behavior.

### Absence scope

- Surfaces inspected: session history, tool outcomes, traces/stream JSON, child reports and user approval.
- Plausible first-party paths checked: tool result replay as independent audit, separate reviewer model, external CI checks, telemetry-based corrective advice.
- Why no material first-party path remains: logs and child explanations are in-band operational records without an independent complementary audit decision owner or an actual S3 target of corrective control.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense future external environment and autonomously revise Bash agent's future capabilities or organizational strategy.
- Disturbance / variety regulated: Coding task, repository mutations, host shell result, model response and operator constraints.
- Decisive decision or feedback right: Choose a function-specific decision from observed changes to currently operating conditions.
- Decision owner: No distinct first-party owner with the full function-specific decision authority is established.
- Supporting / enforcement mechanisms: Built-in bounded agent loop, tool dispatcher, session history and deterministic operational gates.
- Closure path: A bounded tool/execution path exists without the required separate organizational judgment and corrective return.
- Why this is / is not agent-owned: Context compaction, forked sessions and on-demand skills preserve knowledge and current task continuity, but do not select or promote future-facing strategic change.
- Evidence: [src/agent.sh](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/src/agent.sh); [docs/compact-analysis.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/docs/compact-analysis.md); [docs/sessions.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/docs/sessions.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Pinned first-party Bash distribution only, not external agents or separately implemented ports' unverified behavior.

### Absence scope

- Surfaces inspected: skill loading, session/compaction management, model routing and project configuration.
- Plausible first-party paths checked: memory compaction as future adaptation, autonomous tool/skill promotion, monitoring external future conditions.
- Why no material first-party path remains: the supported mechanisms concern current model context and user-specified extension, not a closed future sensing → option choice → capability change feedback cycle.

## S5 — Policy and identity

- State: —
- Function: Resolve ultimate legitimate purpose and policy disputes on behalf of the whole agent organization.
- Disturbance / variety regulated: Coding task, repository mutations, host shell result, model response and operator constraints.
- Decisive decision or feedback right: Choose a function-specific decision from observed changes to currently operating conditions.
- Decision owner: No distinct first-party owner with the full function-specific decision authority is established.
- Supporting / enforcement mechanisms: Built-in bounded agent loop, tool dispatcher, session history and deterministic operational gates.
- Closure path: A bounded tool/execution path exists without the required separate organizational judgment and corrective return.
- Why this is / is not agent-owned: Allowed tools and operator-supplied credentials/approval gates bound execution rather than deciding or revising overarching identity/mission authority.
- Evidence: [src/agent.sh](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/src/agent.sh); [docs/bash-tool-policy.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/docs/bash-tool-policy.md); [README.en.md](https://github.com/lloydzhou/bash-agent/blob/e0062d42f7016f40639a8e69070131d521194cc1/README.en.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: Pinned first-party Bash distribution only, not external agents or separately implemented ports' unverified behavior.

### Absence scope

- Surfaces inspected: tool policy, command permissions, session and fork authority, user/operator configuration.
- Plausible first-party paths checked: step approvals as ultimate policy decisions, child inheritance as S5 delegated authority, external maintainer decisions.
- Why no material first-party path remains: all first-party actions remain within externally configured goals/permissions; no institutional ultimate-policy dispute and binding returned decision loop exists.

## Distributed OSS parent arrangement

Public maintainers, independent local users and external model providers are not one operationally shared governing institution. Package features provide no legitimate cross-installation S5 policy authority.

## Self-hosted and non-human modes

The Bash runtime can run locally with configured model API; tool/loop decisions remain first-party. Optional child sessions use Bash subprocesses and isolated histories, while their filesystem and ultimate human authority are not separate viable organizations by default.

## Recursion

Main Bash model/tool loop is one S1. The one-level child SubAgent starts actual additional model/tool loops with independent context; completion notifications return asynchronously, without an evidenced S2 conflict-control/whole-current S3 owner.

## Variety and escalation

Changing source state and tool errors return into model decisions. Shell and tool policies constrain operations, context compacting conserves capacity, child failures are reported. These are not automatically audit-to-governance or policy-identity control.

## Evidence gaps

Source shows model/tool loops and subprocess child execution but no mandatory worktree separation or cross-child conflict sensor/authority; do not infer S2 from fanout. No live model benchmark was run. This assessment is for the Bash version at pinned ref, not the named C/Go/Rust ports.

## Assessment summary

**Proposed included** with `S1=A / S2=— / S3=— / S3*=— / S4=— / S5=—`. Genuine first-party Bash model/tool loops and async children support S1, but session isolation, tool gates and reports do not themselves close higher VSM functions.

