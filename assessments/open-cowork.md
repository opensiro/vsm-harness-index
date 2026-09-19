---
harness_id: open-cowork
project_name: Open Cowork
repository: https://github.com/OpenCoworkAI/open-cowork
review_ref: a1d0e4ab0f0f78bc42c622653174650cd2025968
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Open Cowork

## Review boundary

- System in focus: the first-party Open Cowork desktop/headless agent harness at pinned revision `a1d0e4ab0f0f78bc42c622653174650cd2025968`, including `CoworkAgentRunner`, session/workspace management, first-party tool/MCP/skills integration, sandbox synchronization, permission enforcement, runtime extensions, persistent memory, remote channels, and the shipped subagent extension.
- Purpose and identity: provide a local desktop/headless AI-agent workspace that turns user requests into tool-mediated work over local/project environments, optionally delegates focused work to child agents, persists sessions/memory, and exposes the same operating surface through local or remote interaction channels.
- Relevant environment: user requests and approvals; project files and processes; WSL/Lima/native workspaces; MCP and built-in tools; external model-provider responses; installed skills/plugins; remote Slack/Feishu messages; and changing session/tool results.
- Standard-distribution boundary: the packaged Open Cowork application plus its supported headless/remote modes at the pinned revision. External model providers, `@mariozechner/pi-ai`, `@mariozechner/pi-coding-agent` internals, MCP servers, Slack/Feishu services, OS/WSL/Lima substrates and user-controlled external skills are dependencies/environment rather than Open Cowork-owned organizational actors.
- Credited operating / distribution surfaces: `src/main/agent/agent-runner.ts`; `src/main/agent/subagent-extension.ts`; `src/main/agent/agent-runner-loop-guard.ts`; `src/main/session/session-manager.ts`; `src/main/extensions/`; `src/main/config/permission-rules-store.ts`; `src/main/config/config-extension.ts`; `src/main/memory/`; first-party MCP/skills/sandbox integration under `src/main/`; and the normal/headless wiring in `src/main/index.ts`.
- Adjacent first-party surfaces excluded from ownership: repository CI/review/contributor policy; roadmap documents as future intent; tests and memory evaluation/prompt-optimizer harnesses that are not wired into supported runtime operation; website/marketing material; and external SDK example implementations. They may corroborate architecture but do not close a VSM function for the assessed runtime.
- First-party operating / deployment modes considered: ordinary interactive desktop sessions; headless JSONL operation; remote Slack/Feishu-triggered sessions; sandboxed WSL/Lima/native tool execution; persistent-memory-enabled sessions; and runtime use of the shipped `spawn_subagent` tool.
- Recursion level: one Open Cowork installation as the system-in-focus. The parent agent session and spawned child agent sessions are operational actors inside it; SDK/model inference, schedulers/queues, sandbox adapters, traces, permission stores and remote transports are supporting mechanisms unless they own a function-specific organizational decision.
- Reviewed revision: `a1d0e4ab0f0f78bc42c622653174650cd2025968`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Open Cowork is an Electron/TypeScript harness that wraps a model-backed agent session with first-party session, workspace, tool, sandbox, skills, memory, permission and remote-control surfaces. `CoworkAgentRunner.run()` establishes the working directory/sandbox, resolves the configured model route, assembles coding/MCP/custom tools and skills, creates or reuses an agent session, installs permission hooks, streams tool and model events into Open Cowork trace/session state, calls `piSession.prompt(...)`, and synchronizes resulting sandbox changes back to the host workspace. The model and `pi-coding-agent` SDK supply inference/session substrate, while Open Cowork supplies the supported product boundary, action surfaces, persistence, permissions, environment coupling and result transport.

The runtime extension manager wires memory, config and subagent extensions into normal and headless operation. `SubagentExtension` exposes `spawn_subagent`: the active parent agent may create a focused child session with isolated context, inherited/restricted tools, timeout and a three-child concurrency cap. Child progress is emitted and the final child response returns to the parent as a tool result. This is real multi-agent delegation, but delegation and a static concurrency ceiling do not by themselves establish VSM S2 or S3.

SessionManager serializes prompts within each session and keeps active-session/queue state, while `LoopGuard` detects repetitive tool-call loops inside a single agent turn and can steer or abort the run. These are meaningful operational reliability controls, but they regulate one session/S1 trajectory or deterministically enforce configured limits rather than autonomously coordinating interference among distinct S1s or exercising whole-system current control.

Open Cowork also persists core/experience memory and can inject retrieved memory into later prompts. It permits user-installed skills and exposes a small allow-list of runtime configuration fields through `config_write`, always requiring interactive approval. Repository code also contains memory evaluation/prompt-optimization utilities, but the optimizer is reached in tests/evaluation rather than the supported operating path. The runtime memory path extracts/retrieves prior experience; it does not establish an external-and-prospective adaptation loop.

## Operational model

A supported task run begins with a user/local/remote prompt. Open Cowork establishes the session/workspace and relevant tools, applies memory/config extensions, and gives the active agent the prompt through the configured agent session. The active agent selects environment-facing tool actions; Open Cowork executes or bridges those actions through first-party tool/sandbox/MCP surfaces, applies permission rules where needed, and returns tool/environment results to the ongoing agent trajectory. The agent can also choose `spawn_subagent`, after which Open Cowork constructs an isolated child session and returns the child's result to the parent for subsequent reasoning/action.

Deterministic machinery constrains this operation: prompts are serialized per session, child concurrency is capped, tool permissions may allow/deny/ask, timeouts can abort inactive work, and LoopGuard may steer or terminate repetitive execution. Traces and remote progress expose what happened to users/operators. Persistent memory can alter later prompt context. None of those mechanisms is promoted to a metasystem function merely because it observes, schedules, constrains or stores agent activity.

## S1 — Operations

- State: A
- Function: autonomously transform user-request and workspace/environment state through iterative model-selected tool actions, including optional focused child-agent work, and use resulting observations to select subsequent actions.
- Disturbance / variety regulated: heterogeneous user tasks, changing files/processes/browser/tool state, MCP results/errors, provider responses, sandbox state, permission outcomes and child-agent results that require context-sensitive next actions.
- Decisive decision or feedback right: choose the next environment-facing tool/action or `spawn_subagent` call from current context/results and decide whether further work is required before returning an answer/outcome.
- Decision owner: the active model-backed agent actor instantiated through Open Cowork's supported parent or child session. External model inference is compute substrate; the agent's context-sensitive action selection is distinct from Open Cowork's deterministic transport/enforcement mechanisms.
- Supporting / enforcement mechanisms: `CoworkAgentRunner`, tool/MCP bridging, skills/resource loading, sandbox/workspace setup and synchronization, SessionManager persistence/queueing, permission hooks, timeouts, LoopGuard steering/abort, extension wiring and child-session lifecycle management.
- Closure path: user/task context plus workspace state → active agent chooses a tool/action → Open Cowork-owned tool/sandbox/MCP integration executes or gates it → result/changed environment returns into the agent session → agent chooses the next action, delegates a focused child task, or completes the run.
- Boundary reachability: `CoworkAgentRunner` is the core supported desktop/headless execution path, and `SubagentExtension` is registered in the first-party runtime extension manager for supported operation; the credited loop does not depend on repository CI/tests or an unwired SDK example.
- Why this is / is not agent-owned: removing the active agent actor while leaving Open Cowork's queues, sandbox, permissions, traces and tool adapters intact removes the context-sensitive choice of what operation to perform next. Those first-party mechanisms execute, constrain or transport the decision rather than replacing it with a fixed rule.
- Evidence: [`src/main/agent/agent-runner.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/agent/agent-runner.ts), [`src/main/agent/subagent-extension.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/agent/subagent-extension.ts), [`src/main/index.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/index.ts), [`src/main/session/session-manager.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/session/session-manager.ts).
- Basis: structural
- Confidence: high
- Caveats: `pi-coding-agent` and model providers implement material session/inference substrate. This assessment does not import undocumented SDK organizational semantics; it credits only the agent decision path as actually wired into Open Cowork's supported first-party action/result boundary.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination function is established at the reviewed recursion.
- Disturbance / variety regulated: Open Cowork can run a parent and child operational agents, but no reviewed supported path identifies a specific inter-S1 interference, collision, oscillation or mutually destabilizing condition and then regulates that disturbance.
- Decisive decision or feedback right: no S2-specific actor is shown choosing or revising a coordination response to cross-S1 disturbance.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: `spawn_subagent` task delegation, child progress/result return, a static maximum of three concurrent subagents, per-session prompt queues, cancellation propagation, tool permissions and isolated child context.
- Closure path: delegation and queueing close task/session transitions, but no inter-S1 disturbance → attenuation response → changed subsequent S1 behaviour loop is evidenced.
- Why this is / is not agent-owned: the parent agent may decide to delegate a focused task, while deterministic runtime code limits concurrency and transports results. Neither task decomposition nor a hard concurrency cap is function-specific evidence of S2.
- Evidence: [`src/main/agent/subagent-extension.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/agent/subagent-extension.ts), [`src/main/session/session-manager.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/session/session-manager.ts), [`src/main/agent/agent-runner-loop-guard.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/agent/agent-runner-loop-guard.ts).
- Basis: structural
- Confidence: high
- Caveats: users may issue tasks that happen to require agents to reconcile information, but generic framework expressiveness or possible disagreement is below the Profile's S2 threshold.

### Absence scope

- Surfaces inspected: parent/child agent extension; session prompt queues and active-session tracking; runtime extension manager; LoopGuard; permission handling; sandbox/workspace execution; remote progress channels.
- Plausible first-party paths checked: child concurrency limiting, parent cancellation propagation, per-session serialization, progress events, shared workspace access, delegation/result return and single-agent loop damping.
- Why no material first-party path remains: the reviewed mechanisms delegate, serialize, constrain or transport work; none is tied to a concrete actual/structural conflict among distinct S1 units together with an attenuation decision and feedback into later S1 behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established in the supported Open Cowork distribution.
- Disturbance / variety regulated: session activity, queued prompts, tool permission boundaries, repetitive tool loops, child timeouts/concurrency and sandbox lifecycle are regulated, but as local/deterministic execution controls rather than discretionary whole-system management of shared commitments/resources/priorities.
- Decisive decision or feedback right: no first-party actor is shown combining a current view across the Open Cowork organization with discretionary authority to revise shared priorities, budgets, resource allocations, commitments or constraints on behalf of the whole.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: SessionManager active-session/queue state, cancellation, timeouts, LoopGuard warn/halt/abort, child concurrency cap, permission rules, `config_read`/approved `config_write`, sandbox adapters and remote session-status reporting.
- Closure path: these controls close local execution, authorization and lifecycle transitions according to fixed/user-configured rules; they do not close an S3 whole-system current-control conversation.
- Why this is / is not agent-owned: the parent agent can choose task actions and delegation, and may propose selected configuration writes, but it is not shown owning organization-wide current resource/commitment regulation. Human-approved config changes and deterministic guards do not transfer that decision right to the agent.
- Evidence: [`src/main/session/session-manager.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/session/session-manager.ts), [`src/main/agent/agent-runner-loop-guard.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/agent/agent-runner-loop-guard.ts), [`src/main/config/config-extension.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/config/config-extension.ts), [`src/main/config/permission-rules-store.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/config/permission-rules-store.ts).
- Basis: structural
- Confidence: high
- Caveats: a user can manually supervise several sessions or alter runtime settings, but ordinary operator control and task delegation are not published as autonomous S3 at this harness boundary.

### Absence scope

- Surfaces inspected: SessionManager queues/status/cancel paths; parent/child runtime; LoopGuard; config extension; permission rules; sandbox lifecycle; remote session/control channels; memory/runtime extension wiring.
- Plausible first-party paths checked: session manager as supervisor, parent agent as manager, child concurrency allocation, loop-guard intervention, runtime config mutation, remote session control and current-status/trace surfaces.
- Why no material first-party path remains: no inspected actor has both whole-system current visibility and discretionary authority over shared organizational resources, commitments, priorities or constraints. The strongest candidates are deterministic local controls or parent-agent task decomposition.

## S3* — Complementary audit

- State: —
- Function: no material complementary operational-audit path is established for Open Cowork's current operations.
- Disturbance / variety regulated: trace events, persisted execution steps, errors, memory debug surfaces and remote progress expose operational information, but no supported runtime path independently challenges an S1/current-control claim through a materially different access channel and returns the finding into current control.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: `trace.step`/`trace.update`, persisted session/message state, logs, memory inspection/debug utilities, remote progress reporting, tests and memory evaluation harnesses.
- Closure path: routine traces/results are produced by the same operating path and displayed/persisted for users; repository evaluation utilities are adjacent rather than wired into the supported runtime control loop.
- Why this is / is not agent-owned: observability does not create an independent audit judgment. The reviewed tests/evaluators can assess development artifacts, but they are outside the declared operating boundary and do not feed findings into a first-party S3 owner during operation.
- Evidence: [`src/main/agent/agent-runner.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/agent/agent-runner.ts), [`src/main/session/session-manager.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/session/session-manager.ts), [`src/main/memory/memory-eval-harness.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/memory/memory-eval-harness.ts).
- Basis: structural
- Confidence: high
- Caveats: humans may inspect traces and artifacts manually; the negative state concerns a first-party complementary S3* path under the autonomous-harness publication boundary, not the usefulness of observability.

### Absence scope

- Surfaces inspected: agent traces/events, session persistence, remote progress, logs/debug paths, memory overview/read/debug surfaces, memory evaluation/prompt-optimizer code and repository tests.
- Plausible first-party paths checked: trace replay/inspection, independent verifier/evaluator search, remote operator visibility, memory evaluation judges, error/loop detection and persisted artifacts.
- Why no material first-party path remains: runtime traces and guards are routine same-path reporting/control, while the materially separate evaluation utilities are adjacent development/test surfaces. No supported complementary operational-reality channel returns an independent finding into current S3 control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established in the supported runtime boundary.
- Disturbance / variety regulated: Open Cowork remembers prior sessions/preferences, loads or installs skills, exposes configuration changes, and can retrieve experience into later prompts, but these paths do not by themselves model external/future change and generate/test an adaptation option that returns into current capability.
- Decisive decision or feedback right: no runtime actor is shown autonomously owning the full external distinction → future option development → capability-change closure required for S4.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: core/experience memory extraction and retrieval, user-installed skills/plugins, `config_read`/human-approved `config_write`, model selection, skill path invalidation/reload, and adjacent memory evaluation/prompt-optimizer utilities.
- Closure path: memory ingestion can change later prompt context and user-installed/configured capability can change later runs, but the decisive adaptation choices remain user/configuration-driven or lack the required external/prospective option-development loop.
- Why this is / is not agent-owned: LLM-based memory extraction summarizes experience and the operational agent can consume it, but memory consolidation is not S4 without prospective environmental modeling and adaptation-option closure. The prompt optimizer is not wired into supported runtime operation at the reviewed revision.
- Evidence: [`src/main/memory/memory-extension.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/memory/memory-extension.ts), [`src/main/memory/memory-service.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/memory/memory-service.ts), [`src/main/config/config-extension.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/config/config-extension.ts), [`src/main/skills/skills-manager.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/skills/skills-manager.ts), [`src/main/memory/memory-prompt-optimizer.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/memory/memory-prompt-optimizer.ts).
- Basis: structural
- Confidence: high
- Caveats: external users can install new skills or change models/settings, and future releases may wire prompt/capability optimization into operation. Those are not autonomous S4 evidence at the frozen revision.

### Absence scope

- Surfaces inspected: memory extension/service/extractors/retrieval; skills manager and runtime skill loading; config extension; model/runtime selection; plugin surfaces; memory eval/prompt optimizer; roadmap future-platform material.
- Plausible first-party paths checked: memory as learning, skill installation as adaptation, runtime model/config mutation, prompt optimization/evaluation, external plugin discovery and roadmap self-improvement plans.
- Why no material first-party path remains: supported runtime memory is retrospective context, skill/config changes are user/configuration-owned, and the prompt optimizer/eval harness is adjacent rather than runtime-wired. No autonomous external/prospective option-development loop returns a selected adaptation into current capability.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established at the reviewed recursion.
- Disturbance / variety regulated: tool permissions, sudo prompts, sandbox boundaries, remote DM allowlist/pairing policy and selected app settings constrain operations and access, but the reviewed runtime does not surface identity/ultimate-policy issues to legitimate authority and return such decisions to govern later operation as S5.
- Decisive decision or feedback right: no identity/ultimate-policy decision path is established; users choose ordinary configuration/access/permission settings rather than resolving an evidenced S5 issue.
- Decision owner: none established for S5 under the Methodology publication boundary.
- Supporting / enforcement mechanisms: allow/deny/ask permission rules, session-scoped always-allow memory, explicit `config_write` approval, sudo password prompts, sandbox isolation, remote pairing/allowlist policy, security configuration and static application policy/docs.
- Closure path: permission/access decisions can immediately allow or block a tool/session/message path, but those are operational authorization closures, not an identity/purpose/ultimate-policy escalation-and-return loop.
- Why this is / is not agent-owned: the agent does not own the relevant security/access policy; humans/configuration do. More importantly, the observed policy/approval mechanisms regulate ordinary actions/access rather than a demonstrated S5 identity-level issue, so they are not promoted to `P` merely because a human has final say.
- Evidence: [`src/main/config/permission-rules-store.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/config/permission-rules-store.ts), [`src/main/config/config-extension.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/config/config-extension.ts), [`src/main/remote/types.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/remote/types.ts), [`src/main/index.ts`](https://github.com/OpenCoworkAI/open-cowork/blob/a1d0e4ab0f0f78bc42c622653174650cd2025968/src/main/index.ts).
- Basis: structural
- Confidence: high
- Caveats: maintainers and users obviously hold real-world policy authority over their projects and installations; this negative classification is limited to the first-party runtime S5 closure required by the Profile.

### Absence scope

- Surfaces inspected: permission rules and interactive approval; config extension; sudo approval; sandbox policy; remote Slack/Feishu pairing/allowlist and gateway auth; security/project policy docs; runtime extension/session wiring.
- Plausible first-party paths checked: permission approval as Parent, DM policy as governance, config writes as policy changes, sandbox/security controls and maintainer policy as organization-level identity authority.
- Why no material first-party path remains: inspected runtime decisions concern tool/action/access configuration, while repository governance belongs to the adjacent development organization. No identity/ultimate-policy issue is shown escalating to legitimate parent authority and returning as a runtime S5 decision.

## Recursion, variety, escalation, and evidence gaps

- The shipped child-agent mechanism is task decomposition, not evidence that each child is a recursively viable VSM unit. Child sessions have bounded local tool autonomy but no separately established S2–S5 metasystem.
- Variety amplification comes from model/tool/MCP/skill choice and optional child agents. Variety attenuation comes from sandbox boundaries, permissions, context compaction, per-session prompt serialization, timeouts, child concurrency limits and LoopGuard.
- Operational exceptions can reach the human through permission/sudo prompts or visible errors/traces. These are useful escalation channels but are classified by their actual operational function rather than treated as S5 merely because a human responds.
- The strongest unresolved architectural dependency is `pi-coding-agent`: its internal agent loop is not first-party Open Cowork code. The assessment therefore credits only decisions/closure observable through Open Cowork's supported assembled runtime and does not import undocumented SDK-internal metasystem behavior.

## Summary

Open Cowork is an included autonomous harness because its supported runtime closes an environment-facing agent/tool/result loop and additionally exposes real child-agent execution. Its strongest distinctive controls at this revision—prompt serialization, subagent concurrency limits, LoopGuard, traces, memory, sandboxing, remote control and permissions—remain operational/delegation/enforcement mechanisms under the function-first Profile. No material first-party S2, S3, S3*, S4 or S5 closure is established at the frozen boundary, yielding **`A — — — — —`**.
