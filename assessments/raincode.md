---
harness_id: raincode
project_name: RainCode
repository: https://github.com/Rainmemery/RainCode
review_ref: 1fc73183d396e4935dd96dbeaf288be87a0d6f66
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# RainCode

## Review boundary

- System in focus: the first-party RainCode CLI/Desktop coding organization at frozen revision `1fc73183d396e4935dd96dbeaf288be87a0d6f66`, including its shared agent-service assembly, model/tool turn loop, built-in coding tools, permission path, subagent manager/tool, session/checkpoint recovery, memory and MCP surfaces where they affect organizational function.
- Purpose and identity: complete local software-development work through a conversational coding agent with file/shell tools, resumable sessions, optional delegated child agents, approvals and local memory.
- Relevant environment: user requests and approvals, local workspace files, shell/background processes, model/provider output, MCP servers, durable session/checkpoint state and local project memory.
- Standard-distribution boundary: `@raincode/server`, `@raincode/agent-core`, built-in tool executor/registry, permission runtime, subagent runtime, storage/session runtime, memory runtime and shipped CLI/Desktop hosts are inside. Provider inference, external MCP servers, host OS, target-project governance and development-only repository processes are outside.
- Credited operating / distribution surfaces: `README.md`; `packages/agent-core/src/turn/turn-loop.ts`; `packages/agent-core/src/subagent/agent-tool.ts`; `packages/agent-core/src/subagent/manager.ts`; `packages/tools/src/executor.ts`; `packages/server/src/subagent-runtime.ts`; `packages/permission/src/approval-broker.ts`; first-party session/memory assembly.
- Adjacent first-party surfaces excluded from ownership: repository plans/architecture documents as actors; CI, smoke tests and benchmarks; contributor/development governance; UI mockups; future M3 features not implemented at the frozen revision.
- First-party operating / deployment modes considered: CLI `run` and `chat`; headless `serve`; Windows desktop; normal/plan/auto-accept collaboration modes; resumable/forked sessions; model-created subagents; control-plane subagent list/stop; MCP augmentation and local memory.
- Recursion level: one RainCode coding organization around one user/workspace mission. The main model-backed loop is the primary S1. A concurrently executing child subagent can be another bounded S1 because it owns a separate model/tool turn over the same project environment.
- Reviewed revision: `1fc73183d396e4935dd96dbeaf288be87a0d6f66`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

RainCode uses one server assembly for CLI and Desktop. A first-party turn loop invokes an OpenAI-compatible model, evaluates tool permissions, executes built-in/MCP actions and returns results into later turns. Sessions are persisted locally with checkpoints and can be resumed or forked.

The model-visible `agent` tool creates a child session with a profile-specific tool projection. `SubagentManager` can run several child loops at once, queues excess work FIFO and returns the child's terminal result into the parent's tool result. Control-plane RPC also exposes subagent spawn/list/stop for frontends and diagnostics.

Tool execution deliberately parallelizes read-only calls and serializes side-effecting calls in model order **inside one `runBatch` invocation**. The `writeChain` is local to that batch. Child sessions reuse the first-party tool dependencies, but no cross-turn or cross-child shared write-arbitration closure was found at the reviewed revision. Thus parallel child S1s sharing one checkout do not, merely by using the same ToolExecutor object, receive a demonstrated inter-S1 collision regulator.

Memory extracts bounded facts from completed/compacted sessions and can persist/retrieve them later. Permission machinery closes ask/allow/deny tool execution with human responses or timeout. These mechanisms support operation but do not by themselves establish higher VSM functions.

## Operational model

A normal RainCode turn receives user/session context, lets the model choose coding tools, executes approved actions and feeds results back to subsequent model rounds. A main actor can delegate a self-contained task through `agent`; that call waits for the child terminal result, which is then returned as ordinary tool feedback to the parent.

Children may execute concurrently under `SubagentManager`, but model-side delegation does not expose a shipped semantic isolation/merge/conflict protocol. The runtime's read/write scheduling is scoped to a single tool batch, not the multi-S1 organization. RPC list/stop methods are frontend/control-plane operations rather than a model-owned whole-current control path.

## S1 — Operations

- State: A
- Function: perform environment-facing software-development work by interpreting a task, inspecting code/state, selecting tools, editing files, executing commands and reacting to returned evidence.
- Disturbance / variety regulated: repository structure, source defects, command/test results, changing local files, model/tool failures and implementation choices.
- Decisive decision or feedback right: choose what evidence to inspect, what coding action to take next, whether to delegate a bounded subtask, and when to return a result.
- Decision owner: the model-backed RainCode main actor and, inside a delegated child, that child model actor.
- Supporting / enforcement mechanisms: turn state machine; built-in/MCP tool registry; ToolExecutor; permissions; workspace path guards; session/checkpoint storage; model adapter.
- Closure path: user task/current workspace → model decision → first-party tool execution or rejection → result enters later model context → actor changes subsequent action or returns an outcome.
- Boundary reachability: CLI/Desktop both instantiate the same first-party Agent Service and turn loop, so the coding decision/tool/feedback path is available in the standard distribution without application-side composition.
- Why this is / is not agent-owned: removing model discretion while retaining storage, tools and permission machinery removes the open-ended choice and sequencing of software-development actions.
- Evidence: [`README.md`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/README.md); [`packages/agent-core/src/turn/turn-loop.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/agent-core/src/turn/turn-loop.ts); [`packages/agent-core/src/subagent/agent-tool.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/agent-core/src/subagent/agent-tool.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference and external MCP behavior remain dependencies rather than credited first-party owners.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination closure was established for concurrently executing coding agents.
- Disturbance / variety regulated: not established at S2 level.
- Decisive decision or feedback right: not established. The manager limits/queues child concurrency, and a ToolExecutor serializes side-effecting calls inside one tool batch, but neither path decides or feeds back on cross-child shared-workspace interference.
- Decision owner: not established.
- Supporting / enforcement mechanisms: child concurrency semaphore/FIFO queue; per-batch read-parallel/write-serial execution; permission/path controls; child final-result return.
- Closure path: not applicable; no concrete inter-child collision detection, semantic isolation, ownership partition, arbitration or returned conflict signal was located.
- Why this is / is not agent-owned: model delegation chooses child tasks, but generic task decomposition is not S2, and the deterministic mechanisms found do not close the required cross-S1 disturbance path.
- Evidence: [`packages/agent-core/src/subagent/manager.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/agent-core/src/subagent/manager.ts); [`packages/tools/src/executor.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/tools/src/executor.ts); [`packages/server/src/subagent-runtime.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/server/src/subagent-runtime.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: write ordering within one model tool batch is useful local sequencing; it is not evidence of an inter-S1 coordination relation across independently executing child loops.

### Absence scope

- Surfaces inspected: subagent creation/manager/queue; child server assembly; shared tool dependencies; ToolExecutor scheduling; workspace/path guards; permission chain; final child-result return.
- Plausible first-party paths checked: cross-child write locking; file ownership/leases; worktree or sandbox isolation; stale-write rejection; conflict detection; parent semantic partitioning with returned coordination feedback.
- Why no material first-party path remains: the located scheduler controls capacity, and `runBatch` serializes writes only within that invocation. No first-party mechanism was found that detects or attenuates a concrete interference relation between concurrent child S1s and feeds the result back into their later behavior.

## S3 — Inside-and-now control

- State: —
- Function: no material agent-owned or qualifying parent whole-current management loop was established at the selected mission recursion.
- Disturbance / variety regulated: not established at S3 level.
- Decisive decision or feedback right: not established. Model-side `agent` waits for a child terminal result; the separate RPC control plane can list/stop children, but no shipped model path provides a whole-current fleet view plus discretionary revision of ongoing commitments.
- Decision owner: not established.
- Supporting / enforcement mechanisms: SubagentManager status/queue; RPC `subagent.list` and `subagent.stop`; cascade cancellation; session archive/shutdown controls.
- Closure path: not applicable; these paths are lifecycle/operational controls rather than an evidenced whole-organization current-control loop.
- Why this is / is not agent-owned: capacity, stop and archive mechanisms are deterministic/operator controls. They do not give the model a current organization-wide decision right over resources, priorities or commitments.
- Evidence: [`packages/agent-core/src/subagent/agent-tool.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/agent-core/src/subagent/agent-tool.ts); [`packages/agent-core/src/subagent/manager.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/agent-core/src/subagent/manager.ts); [`packages/server/src/subagent-runtime.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/server/src/subagent-runtime.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a frontend can supervise children, but generic list/stop UI/control APIs alone do not satisfy Methodology 0.3.6 parent-mode S3 requirements.

### Absence scope

- Surfaces inspected: model-visible agent tool; manager list/status/stop; subagent RPC methods/events; CLI/Desktop session controls; cancellation/archive/shutdown paths.
- Plausible first-party paths checked: live organization view to the main model; model-driven reprioritization/steering of children; parent whole-current supervisory loop; resource/commitment revision.
- Why no material first-party path remains: the parent model receives delegated work at terminal return, while list/stop are control-plane operations. No standard whole-current management decision-and-return loop was established.

## S3* — Complementary audit

- State: —
- Function: no material sufficiently independent complementary audit path was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. Users can define a profile named reviewer and delegate verification, but the standard runtime does not supply an audit-specific independent challenge path with mandatory corrective return.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ordinary tests/commands; generic subagent profiles; user approvals; tool-result evidence.
- Closure path: not applicable; no standard independent claim → complementary examination → audit judgment → corrective current-control path was found.
- Why this is / is not agent-owned: generic configurable delegation can be used for review, but Methodology 0.3.6 does not infer S3* from an optional role name or generic child primitive.
- Evidence: [`README.md`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/README.md); [`packages/agent-core/src/subagent/agent-tool.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/agent-core/src/subagent/agent-tool.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user-authored reviewer profile may provide useful review behavior without becoming a constructor-supplied S3* organization.

### Absence scope

- Surfaces inspected: subagent profile discovery; example reviewer profile documentation; main/child result path; tests/commands; permission audit logging; development CI/benchmark boundary.
- Plausible first-party paths checked: built-in reviewer role; separate verifier model; read-only independent evidence channel; mandatory review after coding; findings returned to a control actor.
- Why no material first-party path remains: no first-party standard audit role or closed corrective-return path was found; review remains an optional use of generic delegation or external human/development process.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective organizational adaptation loop was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Memory extraction and project/session recall persist facts, but they do not generate and select future adaptation options that change RainCode's organizational capability or strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: MEMORY.md injection; session-memory extraction; FTS recall; contradiction/supersede logic; manual memory promotion; web/MCP access; compact hooks.
- Closure path: not applicable; no prospective environmental sensing → adaptation option → persistent capability change → later operation loop was found.
- Why this is / is not agent-owned: LLM-based fact extraction is a learning mechanism, but its output is retained information for later S1 work rather than an evidenced adaptation decision over organizational capability.
- Evidence: [`README.md`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/README.md); [`packages/memory/src/session-memory/extract.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/memory/src/session-memory/extract.ts); [`packages/memory/src/service.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/memory/src/service.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: persistence across sessions is not equivalent to the Profile's stronger outside-and-then adaptation function.

### Absence scope

- Surfaces inspected: project and session memory; extraction/promote/recall; compact; web/MCP; provider configuration; project agent profiles; documented future roadmap.
- Plausible first-party paths checked: environment trend sensing; option generation; self-modification; automatic profile/tool/workflow evolution; durable strategy revision returned to current management.
- Why no material first-party path remains: located features retain facts or expose operator-selected capabilities. No autonomous or constructor-owned prospective adaptation loop was established.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy closure was established.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. User requests, collaboration mode, permission rules, workspace trust/path boundaries and project instructions constrain operations but remain authored operational inputs.
- Decision owner: not established inside the assessed organization.
- Supporting / enforcement mechanisms: five-level permission decision chain; session/project/global rules; ApprovalBroker; workspace path guards; collaboration modes; user responses; project configuration.
- Closure path: not applicable; no identity/ultimate-policy issue is routed to a qualifying authority and returned as authoritative organizational policy.
- Why this is / is not agent-owned: RainCode strongly enforces permission policy, but deterministic enforcement and generic approval do not own the organization's purpose or ultimate policy.
- Evidence: [`README.md`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/README.md); [`packages/permission/src/approval-broker.ts`](https://github.com/Rainmemery/RainCode/blob/1fc73183d396e4935dd96dbeaf288be87a0d6f66/packages/permission/src/approval-broker.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: session/project/global rule scopes are enforcement scopes, not evidence of a legitimate S5 identity authority at this recursion.

### Absence scope

- Surfaces inspected: permission rules/approval broker; collaboration modes; workspace/path policy; project config/instructions; session steering/fork/archive; memory and subagent policy.
- Plausible first-party paths checked: agent-owned purpose revision; parent identity/policy adjudication with return; safety-policy exceptions; persistent mission/governance change.
- Why no material first-party path remains: all located controls constrain current tool/session operation or receive ordinary user input. No complete identity/ultimate-policy decision-and-return path was established.

## Recursion

The assessment treats one user/workspace coding mission as the organization. Main and child model/tool loops are potential S1s; UI/RPC lifecycle controls and repository development processes are not promoted into metasystem ownership without function-specific closure.

## Variety and escalation

RainCode handles coding variety through open-ended model/tool feedback, permission escalation, checkpoints and optional child sessions. Human approval, cancellation and session controls are operational escalation paths. They do not by themselves establish S3-S5.

## Evidence gaps

The frozen revision is sufficient to establish S1 and to reject a material S2 claim after inspecting the scope of write serialization. No unresolved evidence gap remains large enough to require `?` for S3-S5 after review of subagent control, memory, permission and supported runtime surfaces.
