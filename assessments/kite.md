---
harness_id: kite
project_name: Kite
repository: https://github.com/KhanUzeb/kite
review_ref: 1a8b7feafb3661e688e48e5b1923c6390b443d78
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Kite

## Review boundary

- System in focus: first-party Python terminal coding-agent harness shipped in `KhanUzeb/kite` at `1a8b7feafb3661e688e48e5b1923c6390b443d78`, evaluated as one operator-started coding session including its optional child-agent tools.
- Purpose and identity: autonomously inspect, change, and verify a local codebase according to a user's task within configurable tool and approval limits.
- Relevant environment: local repository/workspace, shell and tests, external model provider, optional plugins/skills/MCP integrations, and a human operator.
- Standard-distribution boundary: installed `kite` CLI and the `src/kite` package with first-party runtime, tools, policy, verification, session state, optional subagents and headless task modes. Provider inference and third-party tool servers remain external dependencies.
- Credited operating / distribution surfaces: `agent/loop.py`, `agent/harness.py`, `agent/runtime.py`, `agent/orchestrator.py`, `agent/parallel.py`, `agent/verification.py`, `application/verification.py`, `application/policy.py`, `tools/`, `memory/` and packaged CLI entrypoints.
- Adjacent first-party surfaces excluded from ownership: development tests, CI, benchmark suite, `eval.py`, release/install scripts, contributor/maintainer workflow, and demonstration assets. They do not supply the decisive ownership of installed sessions. External coding runtimes, model-serving backends, operator choices and plugin/skill authors do not donate functions.
- First-party operating / deployment modes considered: interactive plan/build/review usage, headless `kite run` or task execution, resumed sessions, gated coding tools, optional subagents and configurable providers. No external-provider live inference was performed as part of this source inspection.
- Recursion level: one local coding-agent session; optional subagents are nested workers inside that session rather than independent enterprise-level S1 domains by default.
- Reviewed revision: `1a8b7feafb3661e688e48e5b1923c6390b443d78` (frozen from Index discovery #379; subsequent upstream changes not credited).
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The README describes a locally installed CLI with plan/build modes, provider selection, coding tools, optional subagents, sessions/checkpoints and verification gates ([README.md](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/README.md)). The implementation is more probative: `DefaultAgent.run` loops over model-driven turns, invokes `step`, and continues or exits on terminal message, provider fault, budget or interruption ([src/kite/agent/loop.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/loop.py)). Its `query` obtains model responses and `execute_actions` dispatches returned tools and feeds observations back to the model for later decisions. `Harness` configures a first-party `AgentRuntime` rather than delegating the entire agent loop to a third-party coding CLI ([src/kite/agent/harness.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/harness.py), [src/kite/agent/runtime.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/runtime.py)).

Tool execution is gated by policy and session approval modes; the harness records tool outcomes and passes them through a `VerificationCollector` ([src/kite/agent/loop.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/loop.py), [src/kite/agent/verification.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/verification.py)). `application/verification.py` infers relevant checks, records check-command tool outcomes and blocks some submissions that lack required verification ([src/kite/application/verification.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/application/verification.py)). `agent/parallel.py` partitions potentially conflicting tool actions to avoid overlapping writes; `agent/orchestrator.py` runs bounded child-agent tasks with scopes and a result gate. They are safety, execution, and delegated-work mechanisms rather than automatic evidence of higher VSM functions.

Session and context modules store, summarize, compact, checkpoint and recover local interaction state ([src/kite/memory/session.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/memory/session.py), [src/kite/memory/context_checkpoint.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/memory/context_checkpoint.py), [src/kite/agent/compaction.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/compaction.py)). Persistence is not proof of environment-directed future adaptation; test result collection is not proof of an independently owned complementary audit.

## Operational model

The user selects a repository task and operating permissions. The installed Kite agent prepares model messages and local context, requests model inference, receives tool actions, applies first-party policy/permissions, executes permitted file/shell/search actions and returns observations into subsequent model turns. The agent may finish through a textual response or `submit`, with selected edit/verification paths constrained by required checks. A model-driven subagent may receive an explicitly scoped task and report back into the parent session.

S1 unit at this recursion: the main coding-work transformation, optionally subdivided into children without treating every child as an autonomous organizational division. The model-connected actor selects task steps; the Python runtime enforces bounds; the user selects goals and permissions; ordinary test commands provide observations rather than a separately governed audit verdict.

## S1 — Operations

- State: A
- Function: execute open-ended local software-engineering work using model-selected tool actions, inspection and observation-dependent continuation.
- Disturbance / variety regulated: unknown repository content, test failures, command output, edit consequences and changing task state.
- Decisive decision or feedback right: choose the next model action, tool arguments and whether to continue or finish the engineering task.
- Decision owner: model-driven Kite agent operating inside the first-party `DefaultAgent` turn loop; external inference is a provider dependency, not an external prebuilt coding-agent decision workflow.
- Supporting / enforcement mechanisms: `Harness` and `AgentRuntime` setup, policy gates, tool registry/execution, parallel-tool conflict partitioning, user approvals, budgets, session/checkpoint state and verification collector.
- Closure path: operator task → `DefaultAgent.run` → `query` → `execute_actions` → formatted tool observations added to messages → next model turn or final submission.
- Boundary reachability: the ordinary shipped CLI/runtime instantiates this first-party model/tool continuation loop; it is not limited to tests, examples or benchmarks.
- Why this is / is not agent-owned: next-step tool selection is model-directed rather than predetermined by a static script; first-party policy limits tools but does not replace the agent's task discretion.
- Evidence: [src/kite/agent/loop.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/loop.py), [src/kite/agent/harness.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/harness.py), [src/kite/agent/runtime.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/runtime.py), [src/kite/tools/coding.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/tools/coding.py).
- Basis: explicit first-party source.
- Confidence: high for code structure and reachable path; no live provider-backed execution observed.
- Caveats: actual results and permissible actions vary with provider, mode, operator grants and installed plugins.

## S2 — Coordination

- State: —
- Function: no separately evidenced regulation of a specific interference or oscillation among distinct operational S1 units at the selected session boundary.
- Disturbance / variety regulated: tool write collisions and subagent work-scope violations are possible, but the observed mechanisms prevent unsafe overlap or reject out-of-scope results without establishing an S2-specific inter-S1 coordination judgment.
- Decisive decision or feedback right: an actor would need to arbitrate a substantive interaction disturbance between distinct S1s and return that result to their future work; this right is not established in the inspected shipped paths.
- Decision owner: `plan_execution_batches` deterministically serializes overlapping tool calls; child-task orchestrator accepts task scopes and enforces them, while the main agent can request child work. Neither is evidenced as an independent S2 owner.
- Supporting / enforcement mechanisms: `actions_conflict`, `plan_execution_batches`, child scope gate and parent task result transport.
- Closure path: tool calls and child outputs return to the main work loop, but no S2-specific disturbance→coordination→changed distinct-S1 behavior cycle was established.
- Why this is / is not agent-owned: selecting generic child tasks and preventing same-file parallel writes do not, without a concrete inter-S1 disturbance relation, establish a distinct VSM S2 function.
- Evidence: [src/kite/agent/parallel.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/parallel.py), [src/kite/agent/orchestrator.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/orchestrator.py), [src/kite/agent/loop.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/loop.py).
- Basis: bounded source inspection and explicit counterfactual.
- Confidence: moderate; narrowly scoped to the shipped session architecture and inspected conflict-handling paths.
- Caveats: a custom deployment could compose children into organizational S1s, but that external composition is not credited here.

### Absence scope

- Surfaces inspected: main loop/tool scheduler, child-agent orchestrator and scope gating, session/task queues, operator modes and runtime setup.
- Plausible first-party paths checked: model-led delegation, same-workspace parallel tool scheduling, child-job registry, scope/timeout/result gates and child-to-parent returns.
- Why no material first-party path remains: these paths operate a shared session and enforce local action safety or generic delegation; no distinct S1 interaction disturbance with an S2-specific arbitrating owner and returned attenuation is demonstrated.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-session current-regulation function with its own discretionary system-wide decision and return is established beyond user task governance and local action management.
- Disturbance / variety regulated: budgets, mode/permission constraints, tool and child capacity, and task completion are current operational constraints, not automatically S3.
- Decisive decision or feedback right: substantive current allocation/priority/commitment intervention across the system would be needed; no such first-party S3-specific rights path was located.
- Decision owner: user selects task and approval/mode; the running model selects work actions; deterministic runtime enforces limits.
- Supporting / enforcement mechanisms: run budgets, interrupt, user steering, mode restrictions, policy engine, child spawn limits and session state.
- Closure path: budget/permission gates can stop or alter a tool action; no independent S3-level current-regulatory decision and subsequent S1 return distinct from ordinary execution is evidenced.
- Why this is / is not agent-owned: session-level planning, workflow stages, human tool approval and agent self-steering are not sufficient for whole-system current control.
- Evidence: [src/kite/agent/loop.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/loop.py), [src/kite/agent/runtime.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/runtime.py), [src/kite/agent/mode.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/mode.py), [src/kite/application/policy.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/application/policy.py).
- Basis: source-first negative determination.
- Confidence: moderate for selected recursion and standard distribution.
- Caveats: operator-guided plan/build progression exists, but no separate legitimate S3 parent-mode closure was established.

### Absence scope

- Surfaces inspected: agent loop/budgets, execution policy and permissions, plan/build modes, session steering, child orchestration, configuration and CLI controls.
- Plausible first-party paths checked: user approvals as a parent mode, model planning as current regulation, budget constraints, child scheduling and checkpoint recovery.
- Why no material first-party path remains: each observed right regulates an action or single task under user-defined limits; the missing function is a whole-system current-control choice with a separately reconstructable right and feedback into operational S1.

## S3* — Complementary audit

- State: ?
- Function: plausible but unestablished function-specific complementary checking of coding outcome claims, rather than ordinary in-loop test evidence.
- Disturbance / variety regulated: an agent could claim successful edits or tests when required checks did not pass; verification collector and submission gate attenuate some of that risk.
- Decisive decision or feedback right: verification collector may block submission and request check evidence; whether this is an independently owned complementary audit of S1 performance rather than ordinary task-execution validation is unresolved.
- Decision owner: deterministic first-party collector/check planning; the main agent executes check commands and receives their tool outcomes. No independent auditor/claim-adjudication owner is evidenced.
- Supporting / enforcement mechanisms: `EvidenceVerifier.consume` derives records from tool results, `submit_block_reason` and `VerificationCollector`, plus user-visible status and tool-result nudges.
- Closure path: command result → verification records/status → potentially blocked `submit` or requested additional checks → normal agent work continues; no demonstrated separate independently owned audit-judgment/organizational return.
- Why this is / is not agent-owned: the main coding actor can select and run checks; verification derives evidence independently of model-written claims but a separate complementary audit function/owner is not demonstrated solely by parsing the same check stream.
- Evidence: [src/kite/agent/verification.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/verification.py), [src/kite/application/verification.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/application/verification.py), [src/kite/agent/loop.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/loop.py), [src/kite/data/subagents/reviewer.md](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/data/subagents/reviewer.md).
- Basis: explicit positive checking implementation, insufficient evidence for S3* ownership/independence threshold.
- Confidence: high for source mechanics, unresolved classification of whether the path forms a genuinely complementary audit.
- Caveats: shipped reviewer persona is task text, not evidence of an independently executed reviewer, independent test process or recognized audit mandate. The narrow `?` is not a claim that checks are absent.

## S4 — Outside-and-then intelligence

- State: —
- Function: no established outside-environment intelligence and prospective capability-adaptation loop at this session boundary.
- Disturbance / variety regulated: context loss and changing task details; session compaction and memory handle continuity, not demonstrably future organizational adaptation.
- Decisive decision or feedback right: select a prospective change to the harness capability or future operating strategy based on external/future signals, then return that choice into current capability; not evidenced.
- Decision owner: model may revise a current task plan while external providers and users supply prompts; local memory and compaction are deterministic/summarizing support.
- Supporting / enforcement mechanisms: memory, checkpoint/handoff, preserved context, goal/session persistence and context compaction.
- Closure path: saved context can influence subsequent turns, but no established outside-and-then signal → adaptation option → implemented capability change loop.
- Why this is / is not agent-owned: memory and generic re-planning inside a coding task do not demonstrate an S4 function with a prospective/environmental remit.
- Evidence: [src/kite/memory/session.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/memory/session.py), [src/kite/agent/compaction.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/compaction.py), [src/kite/memory/goal.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/memory/goal.py), [src/kite/memory/context_checkpoint.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/memory/context_checkpoint.py).
- Basis: inspected shipped memory/continuity modes.
- Confidence: moderate; no uninspected custom plugins credited.
- Caveats: user-installed skills/plugins might supply adaptations, but external future constructors are outside this pinned first-party ownership claim.

### Absence scope

- Surfaces inspected: context compaction, goal memory, session/checkpoints, recovery, available extensions and runtime mode transitions.
- Plausible first-party paths checked: long-task memory, summaries, checkpoints, plan revisions and external skill/plugin loading.
- Why no material first-party path remains: observed changes preserve or steer current task context, while no first-party future/environment distinction and capability-changing feedback path is established.

## S5 — Identity and ultimate policy

- State: —
- Function: no first-party organizational identity/ultimate-policy decision function with legitimate enclosing authority and returned policy closure is established at the session recursion.
- Disturbance / variety regulated: policy violations and unsafe tool requests are constrained, but tool-approval and configuration limits alone are not evidence of S5.
- Decisive decision or feedback right: set or reinterpret the identity and ultimate policy of the whole system and cause a returned decision to govern current operation; absent as a distinct first-party function.
- Decision owner: the human operator configures settings, authorizes tools and supplies the task; installed runtime enforces policies. No evidence that the user performs a specified first-party S5 identity/ultimate-policy function rather than ordinary local operation control.
- Supporting / enforcement mechanisms: approval modes, project trust guardrails, system prompts, risk policy, config files and cancellation.
- Closure path: permissions can allow/deny local actions, but there is no evidenced S5-grade identity/policy deliberation and return loop.
- Why this is / is not agent-owned: policies constrain a coding agent; neither model prompt nor external operator approval by itself establishes ultimate organizational authority.
- Evidence: [src/kite/agent/mode.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/agent/mode.py), [src/kite/application/policy.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/application/policy.py), [src/kite/guardrails/project_trust.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/guardrails/project_trust.py), [src/kite/config/user.py](https://github.com/KhanUzeb/kite/blob/1a8b7feafb3661e688e48e5b1923c6390b443d78/src/kite/config/user.py).
- Basis: bounded first-party policy/authority inspection.
- Confidence: moderate.
- Caveats: a higher-level organization can govern its installed Kite workers, but that external parent's S5 is not this repository's credited function.

### Absence scope

- Surfaces inspected: operator modes and approvals, policy/guardrail/configuration code, prompts, role files, and maintainer-facing development/release surfaces.
- Plausible first-party paths checked: user parent mode, trust policy, system instructions, reusable roles/skills and developer configuration.
- Why no material first-party path remains: no installed first-party ultimate-identity/policy decision right and return, beyond input/task permissions and guardrail enforcement, is supported at the reviewed session boundary.

## Evidence gaps

- No provider-backed live session or exercised independent audit deployment was performed. Existence of first-party methods is source verified; production correctness and model behavior are not empirically claimed.
- S3* remains `?` because same-stream test evidence plus submit gating does not establish who owns a genuinely complementary audit judgment and how findings reach a separate accountable decision boundary.
- No custom skill/extension or external orchestrator is assumed installed; alternative compositions would require a fresh declared boundary and evidence.

## Conclusion

At the pinned standard installed-session boundary, Kite has a first-party model-driven S1 coding operation (`A`). The observed deterministic collision avoidance, user restrictions, verification collector, and context continuity are substantive supporting mechanisms but do not by themselves prove S2, S3, S4 or S5. The complementary-audit interpretation for S3* remains `?` pending specific independence and functional evidence. This is a standalone proposed assessment for the normal Index review/admission lifecycle, not a cohort score or a live system test.
