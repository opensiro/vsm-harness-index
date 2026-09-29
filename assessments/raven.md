---
harness_id: raven
project_name: Raven
repository: https://github.com/EverMind-AI/Raven
review_ref: e6c0344cb7ce00db25d554e4bb671ec1909a8f9f
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# Raven

## Review boundary

- System in focus: one first-party Raven Host Agent organization at pinned revision `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`, including the shared Agent Loop/Spine runtime, built-in Raven agents, host delegation and DAG machinery, Raven-Code's standard code-flow harness, permissions, session state, context/memory/skill integration, and supported user/control surfaces.
- Purpose and identity: provide a persistent host agent that can execute tasks directly or orchestrate specialized first-party and third-party agents, preserve state across turns, and expose reusable orchestration and control surfaces.
- Relevant environment: user objectives and interventions; project/workspace and Git state; configured model providers; tool/MCP/plugin results; built-in and external sub-agent outputs; remote A2A peers; memory/Skill Hub services; process and network failures.
- Standard-distribution boundary: the `raven/` runtime plus the shipped agent definitions and their first-party plugins under `agents/` are inside when reached through their supported launch/delegation paths. External model endpoints, MCP servers, third-party ACP/CLI/OpenAI-compatible agents, remote A2A peers, EverOS service internals, and user repositories remain environment/dependencies.
- Credited operating / distribution surfaces: `raven/core/runtime.py` assembly root; Spine and Agent Loop; host tool/delegation surfaces; `spawn` and `run_subagent_dag`; shipped Raven-Code/Design/Oncall/PPT/Research definitions; Raven-Code code-flow tools, read ledger, concurrency notices and Harness Manifest; session/task history; permissions; Agent-home bootstrap identity files and context assembly.
- Adjacent first-party surfaces excluded from ownership: the standalone `evolver/` benchmark-driven harness-development tool; benchmark suites and experimental simulations; repository-development CI/plans; documentation examples. These may provide evidence about architecture or development practice but do not become runtime owners merely because they are in the same repository.
- First-party operating / deployment modes considered: ordinary Host Agent turns; direct tool use; focused `spawn`; foreground/background DAGs; stateful sub-agent instances and steering; Raven-Code coding sessions; stored Playbooks executed through DAG machinery; ACP-hosted shipped agents; WebUI/TUI/RPC control; configured messaging/proactive entrances where they feed the same Host Agent Loop.
- Recursion level: one Raven host organization around a host session/workspace objective. Delegated built-in agent sessions and active DAG workers are lower-recursion S1 units. Independently operated A2A peers and third-party agents are environmental organizations even when Raven communicates with them.
- Reviewed revision: `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Raven's standard runtime converges its supported entrances on one assembly root and Agent Loop. The Spine schedules interactive turns; the Agent Loop owns turn state, tool execution, persistence and event ordering; context, memory, planning/capability selection and model response behavior are assembled around that loop. The host can execute work itself or delegate to a roster containing built-in Raven agents and configured external agents.

Multi-agent work is first-party rather than merely documented. `spawn` creates a focused delegated task, while `run_subagent_dag` validates dependencies and capabilities, schedules independent ready nodes concurrently, records node state/artifacts, and supports exception handling, continuation, abandonment, replanning and cancellation. Stateful child instances have separate histories and can receive later direct turns or supported in-turn steering.

Raven-Code adds two organizational mechanisms relevant here. First, its shipped code-flow tool face keeps a per-session read ledger: with read-before-edit enabled, an edit against unread or externally changed content is refused. The same product explicitly warns when other Raven-Code sessions are active in the directory. This does not make a shared checkout isolated, but it attenuates one concrete cross-worker disturbance: stale edits overwriting work another S1 changed after the first S1 read it. Second, at turn archive the code-flow hook independently reads Git state and emits a Harness Manifest. Its fields are machine-read from the workspace rather than copied from model prose; unknown or shared attribution becomes an explicit blocker instead of a fabricated integration-ready result.

The repository also contains a substantial self-evolution subsystem, but its own architecture documentation places it outside the production runtime. `evolver/` is a standalone benchmark-driven developer tool that diagnoses failures, designs candidate patches, evaluates candidate commits and records promotion evidence. The runtime does not import it, promoted candidates do not automatically replace the subject working tree, and deployment remains a separate operator action. It is therefore not borrowed as S4 ownership for the Host Agent organization.

Primary evidence:

- [`docs-site/docs/architecture.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/architecture.md) — shared assembly root, Spine/Agent Loop ownership, delegation boundaries, and explicit separation of runtime from Evolver.
- [`docs-site/docs/orchestration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/orchestration.md) — DAG validation, scheduling, node state, verdicts, exception resolution, replanning, cancellation and persisted graph artifacts.
- [`docs-site/docs/agent-collaboration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-collaboration.md) — delegated tasks, stateful instances, user-visible task/instance inspection and supported steering.
- [`docs-site/docs/agent-integrations.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-integrations.md) — shipped agent boundary, Raven-Code workspace semantics and warning that read-ledger notices are not file locks/worktree isolation.
- [`agents/raven-code/plugins/code-flow/code_flow/config.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/config.py) — shipped read-before-edit configuration and tool-face boundary.
- [`agents/raven-code/plugins/code-flow/code_flow/flow.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/flow.py) — live concurrency notice, session ledger and archive-time publication of the Harness Manifest to ACP metadata.
- [`agents/raven-code/plugins/code-flow/code_flow/manifest.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/manifest.py) — independent Git fact collection, shared-workspace attribution and fail-closed integration-readiness reporting.
- [`docs-site/docs/permissions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/permissions.md) — operator-owned allow/ask/deny policy and permission modes applied before first-party tool dispatch.
- [`raven/context_engine/segments/render.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/context_engine/segments/render.py) — `soul.md` / `agent.md` bootstrap identity and behavior files are part of live context assembly.
- [`agents/README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/README.md) — shipped agent definitions, agent-specific harness plugins, seeded identity/conduct and preservation of operator edits.
- [`docs-site/docs/evolver.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/evolver.md) and [`docs-site/docs/skills-and-extensions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/skills-and-extensions.md) — explicit boundary between runtime memory/skills and separate benchmark-driven harness evolution.

## Operational model

The Host Agent is the top-level operational actor for a session. A model-driven turn can select ordinary tools, choose a specialist, submit a DAG, inspect delegated results and continue the task. When delegated workers are active, each child process/session executes its own model/tool feedback loop against its assigned task and workspace. The host retains task/node records and can consume child outputs or intervene in current work.

Constructor/runtime mechanisms constrain that autonomy. Permission gates, concurrency/semaphore limits, path confinement, node-schema validation, backend capability checks, read-before-edit checks and Git-state collection are treated as enforcement/support unless a function-specific decision right is separately established. External model inference and third-party agent processes are dependencies rather than first-party owners.

## S1 — Operations

- State: A
- Function: transform user/task objectives into answers, files, repository changes, research/design/oncall outputs or other tool-mediated outcomes through repeated model decisions and returned observations.
- Disturbance / variety regulated: open-ended task ambiguity; changing workspace/files; model/tool/MCP/plugin results; failed operations; child-agent outputs; conversation state and environmental feedback.
- Decisive decision or feedback right: choose the next substantive tool, response, delegation or task action after observing current context and prior results.
- Decision owner: the model-driven Raven Host Agent for host work, or the model-driven built-in Raven child agent for its delegated operational task.
- Supporting / enforcement mechanisms: Spine scheduling; Agent Loop; context engine; session persistence; tool registry; permissions; model-provider binding; child backends; DAG runner; cancellation and runtime limits.
- Closure path: objective enters a supported entrance → Spine/Agent Loop assembles current context and tools → model selects a substantive response/tool/delegation → first-party runtime executes or dispatches it → observations/results return to the active agent context → model selects a next action or completion → resulting state/output is persisted or delivered.
- Boundary reachability: the same Agent Loop is the documented execution path for WebUI/TUI and other standard host entrances, and shipped agents are launched as supported Raven runtimes rather than documentation-only examples.
- Why this is / is not agent-owned: removing the model decision maker leaves scheduling, persistence and policy enforcement but removes open-ended action selection in response to changing task evidence.
- Evidence: [`docs-site/docs/architecture.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/architecture.md); [`docs-site/docs/agent-integrations.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-integrations.md); [`README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: inference may run on an external provider and environmental actions may be supplied by MCP/third-party tools; those dependencies do not own Raven's first-party operational feedback organization.

## S2 — Coordination

- State: C
- Function: attenuate stale-write interference among concurrently operating Raven-Code S1 sessions sharing one repository checkout by refusing an edit whose observed file version is no longer current and by surfacing live shared-directory concurrency.
- Disturbance / variety regulated: two Raven-Code sessions can read the same file, one can modify it, and the other can later attempt an edit based on stale content, risking overwrite or invalid work.
- Decisive decision or feedback right: decide whether a requested edit may proceed against the version this session previously observed or must be refused because the content is unread/stale/external-changed.
- Decision owner: constructor-defined Raven-Code code-flow policy and read-ledger implementation; the model does not decide whether the stale-version guard fires.
- Supporting / enforcement mechanisms: per-session read records; `require_read_before_edit`; live session ledger; workspace-concurrency system notice; tool-result error path back to the coding agent.
- Closure path: Raven-Code S1-A reads a target file → Raven-Code S1-B changes the shared file → S1-A submits an edit against its earlier observation → first-party tool guard detects the version mismatch and refuses the write → refusal is returned as tool feedback → S1-A must re-read/replan rather than silently overwrite B's change.
- Boundary reachability: Raven-Code is a shipped built-in agent; its launcher enables its product code-flow/tool configuration, and the integration guide documents read-before-edit refusal for externally changed versions in the supported coding mode.
- Distinct S1 units: separate active Raven-Code sessions/instances can execute independent coding tasks through their own model/tool loops while pointing at one shared checkout.
- Inter-S1 disturbance: a write by one session invalidates another session's previously read content and can otherwise create a lost/stale edit in the common file.
- Attenuating coordination relation: the read-version precondition blocks the stale edit at the first-party file-tool boundary; live concurrency notices additionally tell workers that the directory is shared.
- Feedback into subsequent S1 behaviour: the refused edit is observable to the affected Raven-Code loop, which can re-read current state, narrow work or stop/report the conflict.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited witness is not DAG dependency order, messaging or worker count; it detects a concrete cross-S1 write conflict and prevents one stale action from entering the shared environment.
- Why this is / is not agent-owned: the coordination choice is fixed by the configured tool policy rather than selected by a model after reasoning over inter-worker state, so the state is `C`, not `A`.
- Evidence: [`docs-site/docs/agent-integrations.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-integrations.md); [`agents/raven-code/plugins/code-flow/code_flow/config.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/config.py); [`agents/raven-code/plugins/code-flow/code_flow/flow.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/flow.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is a bounded S2 witness, not a claim of workspace isolation. Raven explicitly documents that shared checkouts have no general file lock/worktree isolation and full-file writes are not universally protected.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain current control over an active delegated organization by inspecting the live DAG/worker/task state and changing ongoing commitments through continuation, replanning, abandonment, cancellation or targeted steering.
- Disturbance / variety regulated: delegated nodes can be pending, running, completed, exceptional, failed, skipped, cancelled or interrupted; outputs can be incomplete; dependencies can block; current work can need correction or retirement.
- Decisive decision or feedback right: decide which current delegated work continues unchanged, receives corrective instructions, is replanned/replaced, is abandoned/cancelled, or is directly steered while running.
- Decision owner: base `A` mode — the Host Agent using first-party DAG/status/control tools after observing run state and outputs; parent `P` mode — the authorized user/control client using first-party task/instance inspection plus direct instance turns or supported `subagents.instance.steer` intervention.
- Supporting / enforcement mechanisms: DAG run/node records; `dag_status`; `resolve_dag_node`; `cancel_dag`; instance history; direct instance chat; steering RPC; foreground/background lifecycle and persisted node artifacts.
- Closure path: workers execute → Raven records statuses/results/exceptions → current-control owner inspects the run/instances → owner chooses continue/replan/abandon/cancel/steer → runtime applies the intervention → later worker execution and host synthesis proceed under the updated commitment.
- Boundary reachability: DAG control tools are part of the shipped host orchestration surface; task/instance inspection is exposed by the first-party WebUI/RPC surfaces, and the collaboration guide specifies the steering RPC contract.
- Whole-system current view: `dag_status` and persisted graph state expose the current node set and run status to the host; the sub-agent/task UI exposes active delegated tasks/instances and their recorded activity to the parent controller.
- Current-control decision scope: intervention changes current worker instructions or commitments rather than only enforcing a fixed semaphore, timeout or permission rule.
- Why this is / is not agent-owned: in base mode the Host Agent interprets current delegated-state evidence and selects the intervention. The separate parent path lets an authorized controller inspect and steer the same current organization without borrowing its decision from the host model.
- Evidence: [`docs-site/docs/orchestration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/orchestration.md); [`docs-site/docs/agent-collaboration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-collaboration.md).
- Basis: explicit + structural.
- Confidence: high for base mode; medium-high for parent mode.
- Caveats: steering support is backend-dependent; the positive parent witness is the supported Raven instance/control path, not a claim that every external backend accepts steering.

### Mode matrix

| Mode | Current view | Decisive owner | Return path | State contribution |
| --- | --- | --- | --- | --- |
| Base autonomous host | DAG/node statuses, outputs, exceptions and task history available to Host Agent tools | Host Agent | continue/replan/abandon/cancel changes later DAG execution | `A` |
| Parent-governed | First-party task/instance views and RPC-addressable active instance state | Authorized user/control client | direct turn or supported steering is injected into the active child path | `(P)` |

## S3* — Audit

- State: C
- Function: independently audit a Raven-Code session's repository-side completion/integration claims against machine-read Git reality and expose blockers/attribution to the host.
- Disturbance / variety regulated: a coding agent can claim completion while the workspace has uncommitted changes, no commits past the pinned base, unreadable Git state, or changes that cannot be attributed to that session because another session shared the directory.
- Decisive decision or feedback right: determine the manifest status (`unknown`, `shared_workspace`, `needs_commit`, `no_changes`, or `ready_for_integration`) from independently read repository facts rather than from the worker's prose.
- Decision owner: constructor-defined Raven-Code manifest logic; the status calculation is deterministic and not chosen by the coding model.
- Supporting / enforcement mechanisms: per-session pinned base commit; `git rev-parse`, branch, status, log and diff-stat reads; shared-session ledger; fail-closed blockers; ACP response `_meta` publication.
- Closure path: Raven-Code performs work and produces its ordinary model response → archive-time code-flow hook separately reads the workspace/Git state → deterministic manifest logic computes attribution/status/blockers → report is attached to ACP metadata and returned to the host → host/user can use the independent facts when deciding integration, continuation or escalation.
- Boundary reachability: Raven-Code's launcher enables code-flow; `CodeParticipant.archive()` calls `build_manifest()` on the normal turn-completion path and files it under `raven.harnessManifest` in the ACP metadata observer.
- Claim audited: whether the coding session produced attributable repository changes that are in a complete, integration-ready Git state.
- Ordinary reporting path: the Raven-Code model's natural-language completion response and checklist/task claims.
- Complementary access path: direct Git/worktree measurement from the first-party code-flow hook; the manifest explicitly states that every field is machine-read and nothing comes from model prose.
- Independence boundary: the coding model does not choose manifest values, and unknown/shared Git evidence degrades to blockers rather than accepting the worker's claim. The audit is still in the same product/process trust domain, so this is complementary runtime evidence rather than an external independent auditor.
- Who acts on findings: the Host Agent or authorized user/controller receiving the ACP response metadata decides whether to integrate, continue, reassign or investigate.
- Why this is / is not agent-owned: the audit verdict is produced by deterministic runtime rules, hence `C`; downstream management may be agent- or parent-owned, but that does not transfer ownership of the audit decision itself.
- Evidence: [`agents/raven-code/plugins/code-flow/code_flow/manifest.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/manifest.py); [`agents/raven-code/plugins/code-flow/code_flow/flow.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/raven-code/plugins/code-flow/code_flow/flow.py); [`docs-site/docs/agent-integrations.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/agent-integrations.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the manifest audits repository state/attribution, not arbitrary semantic correctness of the code; model-based DAG verdicts and the optional Eval Engine are not separately credited as S3* because they primarily inspect ordinary returned content/transcript rather than an independent operational reality channel.

## S4 — Intelligence / adaptation

- State: —
- Function: no first-party runtime owner is established for a prospective environment-model/adaptation loop that changes the Host Agent organization's future operating capabilities and returns those changes into production operation.
- Disturbance / variety regulated: Raven can retrieve memories/skills, construct task-specific worker tables, load Playbooks and react to current task evidence, but these paths do not by themselves establish prospective organizational adaptation under Methodology 0.3.6.
- Decisive decision or feedback right: choose and adopt an organizational capability change from evidence about future/external conditions, with that change becoming part of later production operation.
- Decision owner: not established inside the declared Host Agent runtime boundary.
- Supporting / enforcement mechanisms: Memory/EverOS recall; SkillForge retrieval; user-authored local skills and Playbooks; dynamic worker generation; optional proactivity; separate `evolver/` benchmark tooling.
- Closure path: no qualifying runtime closure is established. Retrieval can change current context and an operator can install/edit reusable artifacts, but the documented feedback-driven skill versioning/retirement path is not automatically implemented; the stronger harness-change loop lives in the separately operated Evolver and stops at candidate commits/evidence pending later deployment.
- Why this is / is not agent-owned: current-task planning, memory recall and skill selection are operational assistance, while the actual benchmark-driven harness adaptation tool is explicitly outside the production runtime and does not automatically deploy its selected candidate.
- Evidence: [`docs-site/docs/skills-and-extensions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/skills-and-extensions.md); [`docs-site/docs/evolver.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/evolver.md); [`docs-site/docs/architecture.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/architecture.md).
- Basis: explicit boundary analysis.
- Confidence: high.
- Caveats: this does not say Raven lacks R&D/self-improvement tooling. It says the adjacent Evolver organization is not silently imported as S4 ownership of the assessed production Host Agent runtime.

### Absence scope

- Surfaces inspected: Host Agent planning/delegation; context engine; memory and SkillForge; Playbooks; dynamic Worker Table generation; proactivity references; Eval Engine; Evolver usage/architecture and its runtime-import boundary.
- Plausible first-party paths checked: memory recall as adaptation; SkillForge retrieval/install as learning; generated worker charters as organizational redesign; Playbook creation/reuse as adaptation; Eval Engine verdict history as learning; Evolver candidate promotion as production self-modification.
- Why no material first-party path remains: the runtime paths either select current context/procedures or require an operator-authored/install step, while the explicit harness evolution loop is a separate developer tool whose candidate commits are not automatically adopted into the running Raven distribution.

## S5 — Identity / ultimate policy

- State: P
- Function: establish the durable identity/behavior and non-overridable operating policy within which the Raven organization may act.
- Disturbance / variety regulated: model/tool behavior can drift across tasks; tools can request unsafe or disallowed actions; specialized agents require stable identity/conduct across sessions and launches.
- Decisive decision or feedback right: define/edit the Agent-home identity/conduct files and configure persistent allow/ask/deny rules and permission mode that constrain subsequent tool dispatch.
- Decision owner: legitimate operator/user maintaining the Raven Agent home and configuration; no first-party autonomous agent is established as the ultimate authority over these controls.
- Supporting / enforcement mechanisms: `agent_memory/profile/soul.md`; `agent_memory/profile/agent.md`; context bootstrap assembly; agent launcher seeding/preservation of operator edits; Permission Gate; persistent tool rules; built-in denials; session-scoped mode override bounded by deny policy.
- Closure path: operator defines or edits identity/conduct/policy → runtime/launcher preserves the operator-owned files/config → context assembler injects identity/behavior into later model calls and Permission Gate evaluates later tool calls against configured rules → subsequent S1/S3 behavior occurs inside that returned policy boundary.
- Boundary reachability: bootstrap files are live inputs to standard context assembly; shipped agent launchers seed identity/conduct into their Agent homes while preserving operator edits; permission rules are evaluated before first-party tool dispatch on the standard runtime path.
- Identity / ultimate-policy issue: what the agent is instructed to be/how it must behave, and which classes of tool actions are permitted, require approval or are forbidden even when a model wants to execute them.
- Ultimate authority in this mode: the operator/user controlling the Agent home and Raven configuration. Built-in catastrophe denials are constructor policy above ordinary model discretion; the model is not credited with authority to override either layer.
- Return-to-operation path: changed identity files are read into future system context; changed permission rules/mode are applied to future tool decisions, directly governing subsequent operational turns.
- Why this is / is not agent-owned: Raven agents operate under these identity/policy inputs but no supported autonomous path grants them legitimate final authority to rewrite or bypass the operator's identity and deny rules.
- Evidence: [`raven/context_engine/segments/render.py`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/raven/context_engine/segments/render.py); [`agents/README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/agents/README.md); [`docs-site/docs/permissions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/permissions.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: session mode changes and smart permission review can alter ordinary operation but do not supersede user deny rules or constructor built-in denials; generic per-action approval is not itself the S5 witness.

## Distributed / OSS / self-hosted notes

- Raven is an Apache-2.0 public repository and can be run with local process, ACP and self-hosted service surfaces; model providers and optional services remain separately configured dependencies.
- External agents connected through ACP/CLI/OpenAI-compatible backends do not automatically inherit every Raven permission/isolation guarantee. Their native process and policy boundary remains environmental unless first-party Raven enforcement explicitly reaches it.
- A2A peers are independently operated remote hosts, not local DAG workers; their autonomy is not imported into Raven's ownership vector.
- EverOS memory is distributed separately; the assessment credits Raven's first-party integration/feedback surfaces but does not treat the external memory service implementation as an internal owner.
- Raven is explicitly described as pre-alpha at the reviewed revision. Classification records evidenced ownership/closure, not production maturity or reliability.

## Recursion

At the assessed recursion level, the Host Agent is the organization-level operational/controller actor around one objective/session/workspace. Shipped Raven child agents and DAG nodes can form lower-recursion S1 units with their own task loops and state. Parent/user control remains outside that base recursion but is admitted where a supported first-party parent mode closes the same function, as in S3 and S5.

A remote A2A peer is a separate organization across a protocol boundary. Likewise, Evolver is an adjacent first-party harness-development/evaluation organization over a subject checkout rather than an internal production S4 organ of the Host Agent runtime.

## Variety and escalation

Raven absorbs open-ended task variety first through the Host Agent's model/tool loop, then delegates specialized variety through the roster and DAG. Node dependencies, concurrency limits, task charters, permission checks and backend capability checks reduce execution variety before it reaches workers. Runtime exceptions and verdict failures return to the host as current-control evidence; the host can continue, replan, abandon or cancel affected work while independent branches can continue.

When a decision exceeds autonomous authority, Raven exposes multiple escalation paths: ask-tier permissions can reach an interactive user, instance/task state can be inspected by the parent controller, active supported instances can be steered, and denied/unsupported operations remain visible rather than being treated as successful work. Raven-Code additionally returns independently measured Git blockers through the Harness Manifest so integration decisions do not need to rely only on worker prose.

## Evidence gaps

- This assessment is source/documentation based at the pinned public revision; it does not claim a live end-to-end execution of every backend, shipped specialist or optional service.
- Third-party agent semantics vary by backend and release. Positive ownership claims rely on first-party Host/Raven-agent paths rather than assuming external agents honor Raven-specific steering, permission or charter semantics.
- S2 is intentionally bounded to the shipped Raven-Code stale-edit guard; Raven itself documents that shared checkouts are not generally isolated and that full writes are not universally guarded.
- S3* is intentionally bounded to Git/workspace completion evidence for Raven-Code. DAG model verdicts and the optional Eval Engine are not promoted to independent audit merely because they are called evaluators.
- Optional memory/Skill Hub/proactivity behavior depends on external configuration and service availability; no unavailable optional path is required for the recorded S1/S2/S3/S3*/S5 states.
- The separate Evolver implementation is present but marked for planned retirement pending sign-off. That lifecycle uncertainty reinforces, rather than creates, the boundary decision not to treat it as production-runtime S4 ownership.
