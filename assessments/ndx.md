---
harness_id: ndx
project_name: ndx
repository: https://github.com/hikaMaeng/ndx
review_ref: b1cb16e9b3b3fcd514c9b71a199e10490b7900d7
reviewed_at: 2026-10-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ndx

## Review boundary

- System in focus: the shipped ndx TypeScript local coding-agent composition at the frozen revision, centered on `@neurondev/ndx-core`, its agent loop, runtime/session server, first-party tool registry, Docker-backed sandbox path, and the in-process TypeScript subagent controller wired into those surfaces.
- Purpose and identity: a local terminal coding agent that performs coding work through model-selected tools and can create/control subordinate in-process agent loops inside the same workspace.
- Relevant environment: the active local workspace, first-party session server and SQLite state, Docker tool sandbox when configured, model/provider configuration, project/user AGENTS.md and skill catalogs, MCP/external tools, and the interactive user.
- Standard-distribution boundary: current ndx TypeScript sources at the frozen ref. Historical/current OpenAI Codex behavior and Rust Codex control-plane semantics described for comparison in ndx documentation are reference lineage only and cannot donate organizational functions.
- Credited operating / distribution surfaces: `packages/ndx/src/agent`, `packages/ndx/src/runtime`, `packages/ndx/src/session`, `packages/ndx/src/tools`, `packages/ndx/src/config`, supported app wrappers, and `apps/toolcontainer` where those surfaces are directly wired into the ndx product.
- Adjacent first-party surfaces excluded from ownership: repository development `.codex/skills`, test/agenttest artifacts, CI/release tooling, documentation-only descriptions of Rust Codex behavior, and external model/MCP/tool implementations not instantiated as first-party organizational owners.
- First-party operating / deployment modes considered: standard local ndx session using `runAgent`; first-party collaboration tools with the TypeScript subagent controller; session-server mode; Docker-backed tool execution; configured skill/AGENTS.md loading.
- Recursion level: one ndx root coding session as system-in-focus; child `runAgent` executions created by the shared controller are subordinate operational units.
- Reviewed revision: `b1cb16e9b3b3fcd514c9b71a199e10490b7900d7`.
- Observation date: 2026-10-07.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The active product logic is implemented in `@neurondev/ndx-core`. `runAgent` builds a first-party tool registry, creates or receives a TypeScript `SubAgentController`, performs model sampling, executes returned tools, feeds tool outputs into the next sampling turn, and stops on a final response or the configured turn bound. Tool calls marked parallel-safe may execute concurrently; collaboration tools themselves are non-parallel task tools.

The TypeScript subagent controller is a real first-party runtime path at the frozen revision. `spawn_agent` creates a separate child `runAgent` execution with a stable id and optional inherited history. The child receives the same current working directory, product config/client and shared controller. `wait_agent` returns lifecycle snapshots/results after waiting, `list_agents` exposes the controller's known agent set, `close_agent` aborts a selected child and marks it closed, `resume_agent` reopens the record, and follow-up/input operations can start another child turn when the target is not already running. CSV jobs can create one child per row.

The controller is intentionally smaller than the Rust Codex topology discussed in `agent-loop-analysis.md`: ndx's own document states that it does not implement Rust's full session-wide mailbox/watch/task-graph topology. That distinction is treated as a boundary constraint, not as missing evidence to be imported from upstream.

The repository also carries development-time `.codex/skills/code-review*` files and a command registry entry named `review`, but no reviewed first-party ndx runtime path turns those repository-maintainer assets into a distinct constrained reviewer child or mandatory complementary audit loop. Likewise, model-pool configuration has a `reviewer` pool name, while the TypeScript `spawnAgent` path merely records `agent_type` metadata and invokes the same `runAgent` client/config rather than selecting a reviewer role/tool boundary.

Primary evidence:
- [README](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/README.md)
- [agent loop](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/agent/loop.ts)
- [TypeScript subagent controller](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/agent/subagents.ts)
- [collaboration tools](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/tools/collaboration/agents.ts)
- [agent-job tools](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/tools/collaboration/agent-jobs.ts)
- [tool execution](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/agent/loop/tool-execution.ts)
- [ndx agent-loop analysis](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/docs/agent-loop-analysis.md)
- [architecture](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/docs/architecture.md)

## Operational model

The root model owns the focal coding loop. It can inspect/edit/run through registered tools and receives each tool result before its next model decision. When collaboration tools are available, the root can create subordinate model-backed `runAgent` units in the same working directory and observe/control their lifecycle through first-party tools.

The TypeScript controller supplies current-control mechanics but does not itself assign a semantic review role, a disjoint filesystem lane or a conflict-detection/repair policy. An optional `agent_type` string is stored in the child snapshot; it does not alter the child model/config/toolset in the reviewed implementation. This matters for separating S3 lifecycle control from S2 interference attenuation and S3* independent audit.

## S1 — Operations

- State: A
- Function: perform coding work by interpreting a user request, selecting first-party tools, inspecting/modifying the workspace, running commands or sandboxed tools, and iterating from tool results.
- Disturbance / variety regulated: task ambiguity, codebase state, tool/process results, errors, provider responses and evolving user/session context.
- Decisive decision or feedback right: choose the next operational tool/action, interpret returned evidence, revise the approach, optionally delegate bounded work, and decide when the answer/work is complete.
- Decision owner: the ndx root model-backed coding agent; child `runAgent` loops can own bounded delegated work.
- Supporting / enforcement mechanisms: agent loop, tool registry/worker processes, Docker sandbox for eligible paths, session/runtime persistence, streaming events, max-turn guard, project/user context loading.
- Closure path: user input → model decision → first-party tool action → tool result/history → next model decision → further action or terminal response.
- Boundary reachability: `runAgent` is directly wired into the product runtime/session server and creates the first-party tool registry at the frozen revision.
- Why this is / is not agent-owned: the runtime executes, persists and constrains operations, but the task-specific choice of tool, interpretation of results and next action comes from the model loop.
- Evidence: [loop.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/agent/loop.ts), [tool-execution.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/agent/loop/tool-execution.ts), [architecture.md](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external; sandbox/configuration and human environment bound reachable actions.

## S2 — Coordination

- State: —
- Function: no sufficiently evidenced first-party inter-S1 interference-attenuation loop is established.
- Disturbance / variety regulated: multiple child agents can share one cwd and therefore can in principle interfere through overlapping files/dependencies, but the reviewed ndx path does not establish a concrete first-party attenuation policy for that disturbance.
- Decisive decision or feedback right: no S2-specific decision right is established beyond generic delegation, messaging/waiting and per-child lifecycle operations.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: `spawn_agent`, `send_input`/`send_message`, `wait_agent`, per-record state, CSV worker creation, generic tool-result feedback.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: the model can create well-scoped children and wait/message them, but Methodology 0.3.6 does not treat delegation, messaging, shared state or sequencing alone as S2. The TypeScript controller supplies no disjoint worktree/file-ownership assignment, collision detector, dependency frontier, mutual-exclusion policy or repair/feedback loop tied to inter-S1 interference.
- Evidence: [agents.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/tools/collaboration/agents.ts), [subagents.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/agent/subagents.ts), [agent-loop-analysis.md](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/docs/agent-loop-analysis.md).
- Basis: structural.
- Confidence: high.
- Caveats: `spawn_agents_on_csv` declares concurrency-related arguments at the tool-schema layer, but the reviewed TypeScript implementation iterates rows and calls `spawnAgent` without implementing an S2-specific interference controller.

### Absence scope

- Surfaces inspected: root/child agent loop, collaboration tool schemas, TypeScript subagent controller, agent-job path, tool execution/concurrency, product architecture/docs and generated test evidence.
- Plausible first-party paths checked: well-scoped task description, parallel children, shared cwd, send/wait/follow-up, CSV worker jobs, tool-call ordering, controller lifecycle state.
- Why no material first-party path remains: distinct S1 units exist, but no concrete first-party relation both identifies a material inter-S1 disturbance and attenuates it with feedback into subsequent S1 behaviour. Generic task scoping and lifecycle transport do not satisfy the active S2 gate.

## S3 — Inside-and-now control

- State: A
- Function: observe and regulate the live set of subordinate child-agent commitments during the current coding session.
- Disturbance / variety regulated: running/completed/failed/closed child work, children that should be waited on or terminated, the need to launch additional bounded work, and settled children that need a subsequent turn.
- Decisive decision or feedback right: inspect child lifecycle snapshots, decide to spawn additional children, wait on selected children, close/abort a selected active child, and start a subsequent turn for a settled child.
- Decision owner: the root ndx model-backed agent through model-callable collaboration tools.
- Supporting / enforcement mechanisms: shared `SubAgentController`, stable child ids, per-agent status/error/finalText timestamps, AbortController, child promises, `list_agents`, `wait_agent`, `close_agent`, resume/follow-up/input tools.
- Closure path: root requests current agent-set/status evidence → model decides a current intervention → controller applies spawn/wait/close/resume/follow-up action → updated lifecycle/result evidence returns as a tool result → root decides subsequent work.
- Boundary reachability: the collaboration tools are registered in the first-party tool registry and dispatch through `ToolContext.agentController`; both root runtime and nested child runs receive the shared controller.
- Why this is / is not agent-owned: the TypeScript controller stores status and executes lifecycle operations, while the model chooses which child to observe, wait on, stop, resume or task next. Removing the model leaves lifecycle machinery without the same task-specific current-control judgment.
- Whole-system current view: `list_agents` returns snapshots for the controller's known agent set, including status, task prompt, final text/error and timestamps; `wait_agent` returns selected current/final snapshots after a bounded wait.
- Current-control decision scope: child spawn, selective wait, targeted close/abort, resume/reuse of a closed child record, and follow-up/input into a non-running child. The reviewed controller does not provide Rust Codex's full mailbox/watch graph, so the S3 claim is bounded to this implemented child set.
- Evidence: [subagents.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/agent/subagents.ts), [agents.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/tools/collaboration/agents.ts), [agent-loop-analysis.md](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/docs/agent-loop-analysis.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `send_input` on an already-running child returns a `queued` status in the reviewed implementation without a Rust-style durable mailbox; S3 is therefore credited from the implemented view/wait/close/spawn/reuse control surface, not from unsupported live-message semantics.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent first-party audit/reviewer loop with corrective closure is established inside the shipped ndx runtime boundary.
- Disturbance / variety regulated: not established as S3*.
- Decisive decision or feedback right: none meeting S3* independence/closure.
- Decision owner: none established.
- Supporting / enforcement mechanisms: generic child-agent creation, model-pool field named `reviewer`, repository-development `.codex/skills/code-review*`, builtin command metadata named `review`, ordinary tests/tool results.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: naming/configuration surfaces do not instantiate a distinct reviewer owner. The reviewed TypeScript subagent path records `agent_type` metadata but launches the same `runAgent` config/client/tool environment; no first-party reviewer restriction, fresh evidence contract or returned veto/corrective gate is wired.
- Evidence: [subagents.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/agent/subagents.ts), [config/index.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/config/index.ts), [session command registry](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/session/commands/registry.ts).
- Basis: structural.
- Confidence: high.
- Caveats: repository-maintainer code-review skills may help contributors review ndx itself, but they are excluded from the installed coding-agent organizational boundary and cannot donate S3*.

### Absence scope

- Surfaces inspected: collaboration controller/tool path, model pools/configuration, session commands, repository skills, tool/test path, agent loop and product documentation.
- Plausible first-party paths checked: `agent_type`, reviewer model pool, `review` command label, code-review skills, generic child agents and test execution.
- Why no material first-party path remains: no runtime path creates a complementary agent with an independent evidence-access boundary and routes its audit judgment back as a corrective acceptance gate for the focal operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective capability-adaptation loop is established.
- Disturbance / variety regulated: not established as S4.
- Decisive decision or feedback right: none for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: AGENTS.md/skill discovery, provider/model settings, session history/logs, environment context and manual configuration.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: ndx can load instructions/skills and users can alter configuration, but no reviewed first-party model loop autonomously identifies future/environmental change, generates an adaptation option and writes/promotes it into continuing product capability.
- Evidence: [initial-context/skill architecture described in agent-loop-analysis.md](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/docs/agent-loop-analysis.md), [architecture.md](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/docs/architecture.md).
- Basis: structural.
- Confidence: high.
- Caveats: reloadable project/user resources are operator-authored extensibility, not autonomous S4.

### Absence scope

- Surfaces inspected: AGENTS.md/skills loading, session persistence/logs, collaboration children, planning, runtime/configuration and architecture docs.
- Plausible first-party paths checked: skill catalog loading, model pools, session restore, planning updates, subagent research, external/MCP resources.
- Why no material first-party path remains: none closes external/future distinction → adaptation-option generation → adaptation decision → return into current capability/S3. Persistence and resource loading remain support/configuration.

## S5 — Policy and identity

- State: —
- Function: no runtime first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: none for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: configured instructions, permission/sandbox settings, project/user AGENTS.md, tool/MCP configuration and local user authority.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: these mechanisms constrain or configure current operation; they do not grant a model-backed actor legitimate authority to decide ndx's ultimate identity/purpose/policy and return that decision as binding governance.
- Evidence: [config/index.ts](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/packages/ndx/src/config/index.ts), [architecture.md](https://github.com/hikaMaeng/ndx/blob/b1cb16e9b3b3fcd514c9b71a199e10490b7900d7/docs/architecture.md).
- Basis: structural.
- Confidence: high.
- Caveats: user/developer configuration is an external authority boundary, not by itself a parent-governed S5 loop under Methodology 0.3.6.

### Absence scope

- Surfaces inspected: provider/system instructions, AGENTS.md, session commands, sandbox/permission/configuration, subagent controller and runtime lifecycle.
- Plausible first-party paths checked: instruction mutation, permission/sandbox controls, reviewer pool labels, session administration, skill/resource configuration.
- Why no material first-party path remains: no identity/ultimate-policy issue is framed and routed to a legitimate S5 decision owner with an authoritative returned decision governing subsequent operation.

## Distributed OSS parent arrangement

Repository maintainer/contributor governance is outside the assessed installed ndx runtime. No operating ndx session routes S3/S4/S5 matters into GitHub project governance and receives a binding decision back, so no parent-mode notation is inferred.

## Self-hosted and non-human modes

ndx is local-first and self-hosted. User settings, sandbox availability and model/provider configuration constrain the runtime. Those controls do not create additional VSM owners beyond the published vector.

## Recursion

The root coding session plus its in-process child-agent set is the assessed recursion. Child `runAgent` executions are meaningful S1 units for current-control analysis, but the reviewed TypeScript implementation does not supply a distinct metasystem for each child or the full upstream Rust task/mailbox topology.

## Variety and escalation

The root agent absorbs operational variety through first-party tools and can delegate work to child loops. Child lifecycle failure/completion/status can be observed and a child can be aborted/closed, allowing current-control escalation. No separate S2 conflict attenuation, S3* reviewer gate, S4 adaptation loop or S5 ultimate-policy loop is established at the frozen boundary.
