---
harness_id: myharness
project_name: MyHarness
repository: https://github.com/woolcoxm/MyHarness
review_ref: 801082b90e182badb93ad3aca1946e4ff9ccfae6
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# MyHarness

## Review boundary

- System in focus: the first-party MyHarness terminal coding-agent runtime at frozen revision `801082b90e182badb93ad3aca1946e4ff9ccfae6`, including the main model/tool loop, autonomous mode, built-in coding tools, subagent `task` tool, session persistence, zero-mem retrieval, permissions/sandboxing, hooks, skills, MCP/LSP integrations and server/TUI/headless surfaces.
- Purpose and identity: perform repository coding work interactively or autonomously, with optional bounded subagent delegation and complementary review/testing workers.
- Relevant environment: user goals, repository/workspace state, command/build/test output, provider responses, persisted session/memory state, subagent reports and configured MCP/LSP services.
- Standard-distribution boundary: repository-owned Rust runtime and built-in tools are inside. External model providers, MCP/LSP servers and host/container facilities are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: TUI, headless and autonomous modes; main coding loop; `task` subagents; verify/self-check loops; event-sourced sessions; zero-mem; skills; permissions/sandboxing; server mode.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests, BENCHMARK.md evaluation, maintainer governance and build/release automation.
- First-party operating / deployment modes considered: ordinary interactive/headless coding, `--autonomous`, foreground/background subagents including documented code-review/testing use, session resume and configured verify hooks.
- Recursion level: the main coding run is the focal S1. A spawned subagent is a bounded subordinate S1 when it receives its own context/tool set and coding/review task.
- Reviewed revision: `801082b90e182badb93ad3aca1946e4ff9ccfae6`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

MyHarness is a single Rust coding-agent binary. `Agent::run_turn` streams model output, executes first-party or bridged tools, feeds concrete results back into the same conversation, supports steering and bounded continuation, and persists session events. Autonomous mode repeatedly asks the same main actor to verify completion and requires two consecutive `GOAL COMPLETE` confirmations, while optional deterministic verify/schema/stop-hook gates can force further work.

The `task` tool creates fresh-context subagents with role-specific restricted tool sets. Its shipped contract explicitly includes exploration, parallel coding, testing, research and code-review use. Reviewer-style subagents can directly inspect workspace evidence with read/search tools and return only their final report to the parent; the parent then uses that report as normal tool feedback.

Persistent zero-mem deterministically retrieves prior-session snippets and session replay restores operational state. Skills are discovered/loaded from static SKILL.md files. These mechanisms reuse prior knowledge but do not autonomously create future-oriented adaptations.

## Operational model

The main model receives a coding objective, selects tools, observes repository/command results and changes subsequent actions. It may spawn one or more fresh-context subagents, synchronously or in the background, and later consume their reports. In autonomous mode the same main actor performs repeated self-check turns; deterministic validators and hooks may reject premature stopping.

## S1 — Operations

- State: A
- Function: autonomously perform coding work through model-selected repository/tool actions and iterative feedback.
- Disturbance / variety regulated: unfamiliar codebases, file state, command/build/test failures, tool/provider errors, incomplete requirements, context pressure and long-running goal completion uncertainty.
- Decisive decision or feedback right: choose the next inspection/edit/command/subagent action, revise work from returned evidence, and decide when to claim task completion.
- Decision owner: the active model-backed MyHarness coding agent.
- Supporting / enforcement mechanisms: `Agent::run_turn`, coding tools, steering, verify hooks, autonomous continuation, permissions/sandboxing, sessions, MCP/LSP bridges, skills and subagent tool.
- Closure path: task/context → model chooses action/tool → concrete result or subagent report returns → model revises subsequent work → repeat until completion, interruption or bounded stop.
- Boundary reachability: TUI, headless and autonomous entry points instantiate the same first-party agent/tool loop directly.
- Why this is / is not agent-owned: without the model actor, the runtime retains tools, validators and persistence but loses the open-ended decisions that transform evidence into coding actions.
- Evidence: README; `src/agent/mod.rs`; `src/main.rs`; `src/tools/mod.rs`; `src/tools/task.rs`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external providers supply inference but not first-party organizational ownership.

## S2 — Coordination

- State: —
- Function: no distinct first-party inter-S1 coordination loop is established.
- Disturbance / variety regulated: multiple subagents can run in parallel and coder subagents may share the workspace, but no shipped mechanism specifically detects and attenuates peer interference among them.
- Decisive decision or feedback right: no S2-specific conflict/oscillation decision was found.
- Decision owner: not established at S2 level.
- Supporting / enforcement mechanisms: subagent tool restriction, independent contexts, background-task handles, shared cancellation and parent polling.
- Closure path: parent delegation/report collection sequences or parallelizes work but does not close a peer-interference attenuation loop.
- Why this is / is not agent-owned: generic delegation and concurrency are not S2 without a concrete disturbance-specific coordination relation.
- Evidence: `src/tools/task.rs`; `src/agent/mod.rs`; README.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: parallel coder subagents may themselves create workspace contention; the absence of a dedicated coordination path is why this is not credited positively.

### Absence scope

- Surfaces inspected: foreground/background subagents, tool concurrency, shared workspace, background tasks, cancellation, todo state and session/runtime controls.
- Plausible first-party paths checked: parallel subagents as S2; todo list as coordination; background-task polling as coordination; permission/sandbox guards as peer conflict control.
- Why no material first-party path remains: these paths delegate, serialize, constrain or observe work but do not establish a specific inter-S1 interference → attenuation decision → changed peer behaviour loop.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established.
- Disturbance / variety regulated: turn limits, budgets, background tasks, todo state, permissions and autonomous completion checks regulate one focal coding run and its delegated helpers.
- Decisive decision or feedback right: no separate authority holds a whole-system current view and substantively manages a portfolio of current S1 commitments/resources/priorities.
- Decision owner: not established at S3 level.
- Supporting / enforcement mechanisms: autonomous budgets, turn caps, todo state, background-task registry, steering, permissions and session state.
- Closure path: these mechanisms constrain or inform the same operational loop rather than forming a separate whole-current management loop.
- Why this is / is not agent-owned: the parent agent delegates and consumes reports as part of S1 task execution; no distinct metasystemic current-control owner is exposed.
- Evidence: `src/main.rs`; `src/agent/mod.rs`; `src/tools/task.rs`; `src/tools/todo.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: subagent dispatch alone is insufficient for S3 without a whole-system current view and substantive current-control scope.

### Absence scope

- Surfaces inspected: autonomous mode, subagent dispatch, todo state, background tasks, budget/turn limits, session controls, monitor tool and permission modes.
- Plausible first-party paths checked: parent subagent orchestration as S3; todo list as whole-system view; budget controls as current management; monitor/background-task state as supervisory control.
- Why no material first-party path remains: all inspected decisions remain scoped to executing one coding objective and do not establish a separate current-management layer over a standing operational portfolio.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation/correctness claims by direct fresh-context review or testing and return findings to the producing parent agent.
- Disturbance / variety regulated: defects, incorrect assumptions, security problems and unverified completion claims that may survive the producer's own reasoning or self-check.
- Decisive decision or feedback right: the reviewer/tester subagent decides which directly observed repository/test evidence constitutes a material finding or failure and reports that judgment to the parent.
- Decision owner: the separate model-backed subagent instantiated through the first-party `task` tool.
- Supporting / enforcement mechanisms: fresh `AgentState`, isolated model context, role-specific tool subsets, documented reviewer/tester task modes, direct workspace/search/read/bash access and final-report return.
- Closure path: parent/producer changes or proposes workspace state → parent dispatches reviewer/tester subagent → child directly inspects repository and/or executes verification → child report returns as tool output → parent changes later coding/repair action based on findings.
- Boundary reachability: `task` is a shipped first-party tool and explicitly documents code-review/testing uses; no external reviewer product is required.
- Why this is / is not agent-owned: removing the child model leaves role/tool plumbing but removes the independent semantic audit judgment over inspected evidence.
- Evidence: README; `src/tools/task.rs`; `src/agent/mod.rs`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: dispatch is chosen by the parent and review is not mandatory for every task; the positive state concerns the supported first-party complementary-audit mode.

- Claim being audited: that produced implementation/workspace state is correct, secure or test-valid enough to accept.
- Ordinary reporting path: the producing parent or coder subagent reports its own completion/result through the normal agent/tool return path.
- Complementary access path: a fresh reviewer/tester subagent directly reads/searches the workspace and, for tester mode, can run commands rather than relying solely on producer self-report.
- Independence boundary: the child has a separate context and role-restricted tool set; an `explore` reviewer is read/search-only and cannot silently repair the code it is judging.
- Who acts on findings: the parent coding agent receives the returned report as a tool result and can revise code or dispatch additional work.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop is established.
- Disturbance / variety regulated: zero-mem retrieves prior-session evidence, skills provide reusable instructions, web/MCP/LSP tools expose external information and session replay restores past state.
- Decisive decision or feedback right: no first-party actor generates and installs future-oriented harness capability adaptations from environmental change.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: zero-mem BM25/entity retrieval, static skills, session replay, web tools, MCP/LSP integrations and context compaction.
- Closure path: remembered/external evidence feeds current task execution; it does not close an outside-and-then adaptation cycle back into durable harness capability.
- Why this is / is not agent-owned: persistence, retrieval and external research are insufficient for S4 without prospective distinction, adaptation-option generation and capability return.
- Evidence: README; `src/zero_mem.rs`; `src/skills.rs`; `src/session.rs`; `src/mcp.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: users can manually create skills or reconfigure providers, but generic extensibility is not autonomous organizational adaptation.

### Absence scope

- Surfaces inspected: zero-mem, skills, session replay, web research, MCP/LSP integration, compaction, hooks and autonomous mode.
- Plausible first-party paths checked: memory as S4; skill loading as adaptation; web research as environmental intelligence; self-reflection/autonomous self-check as learning; configuration changes as future adaptation.
- Why no material first-party path remains: the paths reuse or retrieve evidence for current work and do not generate/persist a new capability in response to a prospective environmental distinction.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure is established.
- Disturbance / variety regulated: permission modes, deny/allow rules, approval prompts, sandbox boundaries, hooks, workspace scoping and authentication constrain ordinary operation.
- Decisive decision or feedback right: no identity/ultimate-policy issue is routed to a legitimate ultimate authority and returned as a durable system-level policy decision.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: permission engine, plan/ask/auto-edit/yolo modes, sandboxing, hooks, auth, workspace/write guards and configured tool rules.
- Closure path: operator configuration and approvals affect current actions but do not close identity-level policy questions for the harness.
- Why this is / is not agent-owned: static/configurable safety and access constraints are enforcement mechanisms, not S5.
- Evidence: README; `src/perms.rs`; `src/sandbox.rs`; `src/hooks.rs`; `src/auth.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: maintainers/operators retain authority outside a run, but development/deployment governance is adjacent to the assessed operating boundary.

### Absence scope

- Surfaces inspected: permission modes/rules, approval prompts, sandboxing, auth, hooks, autonomous budgets, system prompt and repository governance.
- Plausible first-party paths checked: permission mode as S5; hooks as policy authority; system prompt as constitution; user approval as ultimate authority; maintainer governance as deployed-harness identity.
- Why no material first-party path remains: these mechanisms constrain ordinary actions or development governance and do not establish an identity-policy issue → legitimate authority → authoritative decision → returned durable operation loop.

## Recursion

The main coding run is the focal S1. Subagents have fresh contexts and bounded tool sets and can act as subordinate S1 or complementary reviewer cells, but no claim is made that each contains a complete recursive viable-system stack.

## Variety and escalation

The main actor absorbs coding variety through iterative tool use, steering, verification feedback, memory and bounded delegation. Autonomous mode surfaces unfinished-work uncertainty back to the same actor through repeated self-check prompts. Complementary review/testing can be delegated to a fresh child and its report returned to the parent. Hard budgets, permissions and hooks bound execution.

## Evidence gaps

No `?` state is required. The frozen repository exposes the complete coding loop, subagent implementation, self-check/validation paths, persistence/memory and safety surfaces sufficiently to support the positive S1/S3* findings and negative S2/S3/S4/S5 conclusions.

## Assessment summary

MyHarness closes autonomous S1 through its model/tool coding loop and provides an autonomous complementary S3* mode through fresh-context reviewer/tester subagents whose findings return to the parent. Parallel subagents do not establish S2, the parent delegation path does not create whole-current S3, persistent memory/skills do not form S4, and permissions/sandboxing do not close S5.

**Vector:** A · — · — · A · — · —
