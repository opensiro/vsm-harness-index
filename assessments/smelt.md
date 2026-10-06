---
harness_id: smelt
project_name: Smelt
repository: https://github.com/leonardcser/smelt
review_ref: bc44da1696a74fde792c26cdb1dca3e5a42e3e28
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Smelt

## Review boundary

- System in focus: the first-party Smelt coding-agent runtime at frozen revision bc44da1696a74fde792c26cdb1dca3e5a42e3e28, including the Rust engine/model-tool loop, built-in coding tools, Lua plugin host, permission modes, sessions/history/compaction, managed worktrees, provider layer, TUI/headless paths and bundled Plan/Apply/Yolo modes.
- Purpose and identity: run one highly customizable terminal coding agent that reads, edits and verifies a software project while Lua customizes tools, modes, prompts and UI behavior.
- Relevant environment: user requests/approvals, repository files, shell/test results, provider/model responses, session history, configured Lua plugins/MCP servers, worktree state and local settings.
- Standard-distribution boundary: shipped Smelt binary, Rust crates and bundled Lua runtime/plugins. External model endpoints, MCP servers, OS processes and user/project Lua customizations are dependencies/extensions and cannot donate uninstantiated organizational functions.
- Credited operating / distribution surfaces: crates/engine, crates/core, crates/tui, crates/protocol/provider/store, runtime/lua and bundled prompts/tools/modes.
- Adjacent first-party surfaces excluded from ownership: CI/fuzzing/release infrastructure and user-authored third-party plugins unless the standard distribution itself instantiates their organizational role.
- First-party operating / deployment modes considered: interactive TUI, headless one-shot, Normal/Plan/Apply/Yolo, managed worktrees, bundled Lua plugins and supported provider/MCP configurations.
- Recursion level: one Smelt coding session. The frozen standard runtime instantiates one model-backed coding S1; Lua coroutines/background asks are runtime components rather than separate operational coding agents.
- Reviewed revision: bc44da1696a74fde792c26cdb1dca3e5a42e3e28.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Smelt's engine runs one model/tool conversation and processes StartTurn, cancellation, steering/configuration, tool calls and provider responses. The shipped system prompt gives that agent repository read/edit/bash/search tools and asks it to verify its own result. Session/history storage, compaction and managed worktree transitions preserve execution context.

The Lua APIs do not establish hidden model subagents. smelt.agent appends system-prompt fragments; smelt.task alloc/resume is an external coroutine bridge; smelt.spawn runs Lua coroutines on the Lua task runtime; smelt.remember only controls recall of last-used model/mode/reasoning settings. EngineAsk creates auxiliary LLM requests used by features such as title/predict/compaction, not a standard separate coding or audit actor with organizational decision rights.

## Operational model

The active model owns open-ended coding decisions and consumes returned tool evidence. Normal/Plan/Apply/Yolo vary permissions and interaction style around that same S1. Deterministic queues, cancellation, permissions, worktrees, Lua tasks and persistence support one agent rather than constituting additional VSM owners.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify software through model-selected coding/tool actions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, shell/test failures, provider variability, context pressure and permission constraints.
- Decisive decision or feedback right: choose substantive repository/tool actions, interpret their results and decide how to repair or complete the requested work.
- Decision owner: the active model-backed Smelt coding agent.
- Supporting / enforcement mechanisms: Rust engine loop, tool dispatcher, permissions, modes, session/history storage, compaction, provider adapters, MCP and worktrees.
- Closure path: user goal → model chooses tool/coding actions → first-party runtime executes and returns evidence → model revises/verifies → final answer closes the turn.
- Boundary reachability: both interactive and headless runtime paths instantiate the same engine/model/tool organization.
- Why this is / is not agent-owned: deterministic runtime machinery executes and constrains actions, but the model owns the substantive engineering choices.
- Evidence: [README.md](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/README.md); [crates/engine/src/agent.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/engine/src/agent.rs); [crates/engine/src/prompts/system.txt](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/engine/src/prompts/system.txt).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Lua can extend behavior, but this assessment credits only organizational functions instantiated by the frozen standard distribution.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established.
- Disturbance / variety regulated: no distinct standard operational S1 peers are instantiated whose recurring interference is placed under a coordination feedback loop.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: concurrent tool calls, Lua task scheduling, queues and worktree mechanics coordinate components inside one coding session, not peer S1 organizations.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: no qualifying S2 function exists at the declared boundary.
- Evidence: [crates/core/src/lua/api/task.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/core/src/lua/api/task.rs); [crates/core/src/lua/api/spawn.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/core/src/lua/api/spawn.rs); [crates/engine/src/agent.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/engine/src/agent.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: generic extensibility could be used to build multi-agent behavior, but uninstantiated extension potential is not S2.

### Absence scope

- Surfaces inspected: engine loop, Lua agent/task/spawn APIs, worktree/session runtime, tools, modes, provider/MCP and bundled plugins.
- Plausible first-party paths checked: model subagents, peer worker pools, worktree-isolated agents, file/path conflict arbitration and peer message routing.
- Why no material first-party path remains: located task/spawn mechanisms are Lua/runtime tasks rather than independently goal-owning model agents, and no standard peer-interference loop is instantiated.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control function is established beyond the single coding S1.
- Disturbance / variety regulated: no portfolio of operational S1 commitments/resources exists under a distinct current-control owner.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: cancellation, steering, mode/model changes, queueing and worktree transitions alter one current coding session but do not supervise multiple S1 commitments.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the coding S1 controls its own work; runtime/user controls do not form a distinct whole-current organizational controller.
- Evidence: [crates/engine/src/agent.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/engine/src/agent.rs); [crates/core/src/runtime.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/core/src/runtime.rs); [docs/docs/guide/usage.md](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/docs/docs/guide/usage.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: generic turn cancellation and permission-mode switching are local control, not sufficient S3 under Methodology 0.3.6.

### Absence scope

- Surfaces inspected: active-turn commands, queue/cancel/steer behavior, modes, worktree transitions, Lua tasks and runtime state.
- Plausible first-party paths checked: multi-worker status view, current commitment allocation/reallocation, selective worker intervention and supervisory model role.
- Why no material first-party path remains: all located controls govern one S1/session or runtime component state rather than a whole-system portfolio of operational units.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established.
- Disturbance / variety regulated: no separately owned audit judgment independently challenges the coding agent's result and feeds corrective findings back.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: system-prompt self-verification, tests/tools run by the same agent, EngineAsk auxiliary requests and Plan mode may improve quality but are not an independent audit owner.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: verification remains in the author S1 unless a plugin/user constructs something additional; the standard distribution does not instantiate a separate reviewer.
- Evidence: [crates/engine/src/prompts/system.txt](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/engine/src/prompts/system.txt); [crates/engine/src/agent.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/engine/src/agent.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: an auxiliary LLM request is not sufficient without a distinct audited claim, complementary evidence path, independence boundary and corrective return loop.

### Absence scope

- Surfaces inspected: system prompt, EngineAsk, bundled plugins, modes, tools/tests and Lua extension APIs.
- Plausible first-party paths checked: dedicated reviewer/verifier actor, second-model critique, fresh-context repository audit and automatic review gate.
- Why no material first-party path remains: standard first-party paths leave verification with the author agent or use auxiliary LLM calls for non-audit UI/context features.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no outside/future distinction is converted into adaptation options and returned to present capability by a dedicated owner.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: sessions/history, compaction, recent-setting recall, skills, providers and MCP preserve or configure capability but do not close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: smelt.remember restores user choices; session persistence/compaction preserve context rather than generating prospective adaptations from external change.
- Evidence: [crates/core/src/lua/api/remember.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/core/src/lua/api/remember.rs); [crates/core/src/session_runtime.rs](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/core/src/session_runtime.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: plugin extensibility can introduce external data, but generic extension capability is not an instantiated S4 loop.

### Absence scope

- Surfaces inspected: remember/recent choices, sessions, compaction, provider/model configuration, MCP/skills and Lua lifecycle/hooks.
- Plausible first-party paths checked: durable learned strategy, environment scanning, autonomous capability reconfiguration and future-oriented option generation.
- Why no material first-party path remains: identified mechanisms persist/configure present behavior rather than close an external-and-prospective adaptation conversation.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level conflict is routed to an ultimate authoritative owner and returned as governing runtime policy.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes, trusted project-local Lua, system prompt and configuration constrain operation but do not create S5.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent follows user/developer-authored rules and cannot authoritatively redefine Smelt's identity or ultimate policy.
- Evidence: [docs/docs/reference/permissions.md](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/docs/docs/reference/permissions.md); [docs/docs/guide/customization.md](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/docs/docs/guide/customization.md); [crates/engine/src/prompts/system.txt](https://github.com/leonardcser/smelt/blob/bc44da1696a74fde792c26cdb1dca3e5a42e3e28/crates/engine/src/prompts/system.txt).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user configuration/trust is legitimate operating authority but no identity/ultimate-policy decision loop is evidenced.

### Absence scope

- Surfaces inspected: modes/permissions, project trust, system prompt, Lua config/plugins, provider/MCP settings and runtime state.
- Plausible first-party paths checked: constitutional revision, parent identity governance, agent-authored policy and authoritative return-to-operation path.
- Why no material first-party path remains: observed policy surfaces are configuration/enforcement for current operation, not S5 governance.

## Distributed OSS parent arrangement

The assessed organization is one running Smelt coding session, not the GitHub maintainer project. Contributor/release governance is not imported into runtime ownership.

## Self-hosted and non-human modes

Smelt supports local/self-hosted providers and headless operation. These change deployment but do not add S2-S5 owners in the standard runtime.

## Recursion

One model-backed coding agent is the viable-unit operational core. Lua coroutines, EngineAsk helpers, tools, providers and worktrees are components/support mechanisms rather than separate viable operational agents.

## Variety and escalation

Coding and ordinary verification variety remain in S1. Permission/mode/context/worktree machinery bounds execution without establishing higher VSM functions.

## Evidence gaps

No ? state is required. The frozen runtime exposes the relevant engine, Lua task/agent/spawn, session, mode, permission and auxiliary LLM paths sufficiently to support the positive S1 and bounded negative conclusions.
