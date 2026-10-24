---
harness_id: tura
project_name: Tura
repository: https://github.com/Tura-AI/tura
review_ref: 81fc96729115c85bd5be3e6f6b6a13893d4065c5
reviewed_at: 2026-10-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Tura

## Review boundary

- System in focus: the installable first-party Tura coding-agent runtime (Rust router/session worker, bundled agent configurations, provider turn and macro command execution) in its standard direct/balanced variants, not the project's performance benchmark or the human's organization.
- Purpose and identity: complete user coding tasks with model-selected code/shell command workflows, executing dependency-ordered multi-step tool graphs within fewer model turns and feeding real outcomes back to the coding agent.
- Relevant environment: local user workspace and shell, provider/model endpoint and credentials, configured agent modes, terminal/desktop session clients, per-session runtime/router and session DB service.
- Standard-distribution boundary: packaged Tura launcher/router and per-session runtime worker; built-in direct/balanced/thoughtful coding agents and enabled macro `command_run` workflows with first-party permission/context handling. Do not equate an operator spawning multiple Tura sessions with a packaged agent organization.
- Credited operating / distribution surfaces: [README.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/README.md); [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/ARCHITECTURE.md); [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/ARCHITECTURE.md); [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/ARCHITECTURE.md); [process.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/process.rs); [runtime_turn.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/runtime_turn.rs); [call.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/provider_flow/call.rs); [tool_step.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/turn_loop/tool_step.rs); [execute.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/tool_flow/execute.rs); [handler.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/tools/src/command_run/handler.rs); [schema.json](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/tools/src/command_run/schema.json); [child_dispatch.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/child_dispatch.rs); [mod.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/agent_router/mod.rs); [agent_management.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/state_machine/agent_management.rs); [store.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/src/store.rs); [agent_config.json](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/src/direct/agent_config.json); [activate_session.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/session/activate_session.rs); [permission.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/tool_flow/permission.rs); [compaction.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/context/compaction.rs).
- Adjacent first-party surfaces excluded from ownership: external benchmark dataset/reports and testing tools, development CI, screenshot UI previews, prepackaged examples/docs not invoked in standard operation, custom agent assemblies, third-party remote providers, user-run orchestrators and any special child-router mode explicitly restricted to tests.
- First-party operating / deployment modes considered: standard direct/balanced/thoughtful bundled coding agents, terminal/desktop session entrypoints, `command_run` macro execution and shared API/router handling; configurable agent definitions considered only to the extent the runtime actually wires them into such a supported mode.
- Recursion level: one active coding agent/session and its deterministic macro-command substeps; neither shell commands nor router-managed unrelated user sessions are independently autonomous subordinate S1 organizations.
- Reviewed revision: `81fc96729115c85bd5be3e6f6b6a13893d4065c5`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/README.md) explicitly describes Tura's design: a coding model constructs a macro `command_run` graph encompassing inspection, patching and verification steps. [process.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/process.rs) and [runtime_turn.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/runtime_turn.rs) execute a model-turn state machine and return tool outcomes to subsequent turns when needed; [call.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/provider_flow/call.rs) supplies model requests and [handler.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/tools/src/command_run/handler.rs)/[schema.json](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/tools/src/command_run/schema.json) implement deterministic grouped command execution. These scheduled commands are *tools of one model-led S1*, not a population of independent agentic coding workers merely because multiple shell steps can run within one model response.

[ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/ARCHITECTURE.md) describes the worker/router split. A per-session `tura_runtime` process handles a prompt and exits, communicating with a router gateway and single DB service. This is fault isolation and session ownership, not a first-party model deciding conflicts/priorities among distinct coding S1s. [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/ARCHITECTURE.md)/[store.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/src/store.rs) describe the supported bundled agent choices, including direct and balanced prompt/provider/tool capability settings. The default coding-agent constructor in [mod.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/agent_router/mod.rs) sets `need_validator: false`, and bundled direct/balanced configs [agent_config.json](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/src/direct/agent_config.json) likewise disable validator dispatch. A `general` agent constructor contains a validator config, but a declaration alone does not prove an executed independent audit-to-current-control loop in the assessed standard coding modes.

[child_dispatch.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/child_dispatch.rs) contains a helper to create subprocess child sessions, but `dispatch_child_agent` fails closed unless `TURA_ALLOW_CHILD_ROUTER_CLI_FOR_TEST=1`; neither that test-only route nor arbitrary end-user custom orchestration should donate decisive S2/S3/S3* ownership to the bundled coding agent. [activate_session.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/session/activate_session.rs) and [compaction.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/context/compaction.rs) preserve per-session context; [permission.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/tool_flow/permission.rs) enforces action constraints. The first-party kernel/router's many components can coordinate requests at transport level without becoming model-owned organizational management.

## Operational model

The coding model decides what repository work to perform, prepares a macro command graph with tooling, and consumes resulting outputs/verification for further coding choices. C/Rust scheduling, provider transport and session execution machinery enforce those choices. Tool graph parallelism is not inter-S1 coordination. User configuration governs provider identity, accepted permissions and agent variant, while model-authorized ultimate organizational policy is not part of this coding-session product.

## S1 — Operations

- State: A
- Function: decide and execute uncertain repository engineering edits, inspections and tests using one model-led coding session and its macro command graph.
- Disturbance / variety regulated: unknown repository state, failed shell tests, partial patches, unexpected command outputs, new context requirements.
- Decisive decision or feedback right: coding model selects command graph/tool arguments and what further investigation or repair to do once actual macro outputs return.
- Decision owner: model-powered coding agent (bundled direct/balanced/thoughtful session mode).
- Supporting / enforcement mechanisms: provider turn requests, macro-command schema/handler, dependency-ordered tool scheduling, runtime session and context compaction.
- Closure path: model selects `command_run` operations → Rust macro executor reads/patches/tests → tool result and status returned to current agent history → model chooses repair/final answer.
- Boundary reachability: bundled Tura coding sessions directly invoke the model and first-party `command_run` execution in the packaged runtime; no external agent script is necessary.
- Why this is / is not agent-owned: without the model's coding objective and command-plan choices the scheduler executes syntax but does not select context-sensitive repository engineering actions.
- Evidence: [README.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/README.md); [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/ARCHITECTURE.md); [process.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/process.rs); [handler.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/tools/src/command_run/handler.rs); [schema.json](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/tools/src/command_run/schema.json); [call.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/provider_flow/call.rs)
- Basis: explicit and structural
- Confidence: high for source-wired process, no credentialed live provider session run
- Caveats: deterministic execution reduces model round trips without making the tool graph itself an autonomous agent.

## S2 — Coordination

- State: —
- Function: no in-boundary cross-S1 interference-specific coordination and corrective return among multiple independent operating coding agents is established.
- Disturbance / variety regulated: parallel macro tool jobs or router sessions may contend for resources, but these are not automatically independently autonomous S1 workers at this recursion.
- Decisive decision or feedback right: no dedicated decision over conflict between separately model-led sibling coding S1 units reaches the bundled coding session.
- Decision owner: none demonstrated; macro executor and router are deterministic job/session controllers.
- Supporting / enforcement mechanisms: macro command-step dependencies, router/session isolation, process lifetime, direct child subprocess helper restricted to tests.
- Closure path: tool dependencies return to the originating agent; no concrete S1-to-S1 interference detection, attenuation, and feedback into affected autonomous siblings is supported.
- Why this is / is not agent-owned: step scheduling of one actor's command graph is within S1, not an S2 relationship; independent user sessions are outside this assessed single-session organizational boundary.
- Evidence: [handler.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/tools/src/command_run/handler.rs); [child_dispatch.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/child_dispatch.rs); [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/ARCHITECTURE.md); [mod.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/agent_router/mod.rs); [process.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/process.rs)
- Basis: structural and explicit test-only route restriction
- Confidence: medium-high in standard bundled modes
- Caveats: a separately composed Tura multi-agent application could need its own assessment with expanded boundary.

### Absence scope

- Surfaces inspected: macro handler/dependency graph, process/session router, agent registry, child router helper and bundled agent configs
- Plausible first-party paths checked: distinct running model-led child S1s and a concrete shared-resource interference detector, corrective feedback to both, active regulated ownership
- Why no material first-party path remains: command graph steps are tools, router sessions are client requests, and direct subprocess agent dispatch is test-only by explicit source flag; no packaged inter-S1 regulatory relation is established.

## S3 — Inside-and-now control

- State: —
- Function: no model-owned whole-current operational management of a distinct workforce of coding S1s is shipped in the assessed bundled session.
- Disturbance / variety regulated: multiple session requests or command steps, not competing autonomous worker commitments under one model supervisor.
- Decisive decision or feedback right: model governs its own task graph; router scheduling does not exercise autonomous portfolio priority/assignment rights.
- Decision owner: none in the assessed recursion for S3; human/host may externally run multiple sessions.
- Supporting / enforcement mechanisms: runtime worker lifecycle, DB routing, sessions and command graphs.
- Closure path: session step/status may affect the same coding actor, but no separate current portfolio decision returns to multiple S1s as binding work assignments.
- Why this is / is not agent-owned: having a management/router crate and many user sessions is not a whole-current agent manager; it does not choose competing subagent commitments.
- Evidence: [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/ARCHITECTURE.md); [process.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/process.rs); [mod.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/agent_router/mod.rs); [child_dispatch.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/child_dispatch.rs); [activate_session.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/session/activate_session.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: service process control and router health/version handshake remain operational infrastructure, not S3.

### Absence scope

- Surfaces inspected: router-per-session runtime, agent variant registry, macro execution, child dispatch test restriction and session DB contract
- Plausible first-party paths checked: whole currently owned worker roster/commitments, live resource tradeoffs with discretionary manager, returned changed S1 work
- Why no material first-party path remains: verified supported coding modes run individual sessions and command tools; first-party multi-S1 managerial authority and current-control feedback are not established.

## S3* — Complementary audit

- State: —
- Function: no reachable independent complementary auditor adjudicates developer claims with direct evidence and returns corrective S3 management in the shipped coding modes.
- Disturbance / variety regulated: potential false or incomplete code completion claims that would need a distinct reviewer.
- Decisive decision or feedback right: no executed independent reviewer verdict and corrective return established by the inspected default coding runtime.
- Decision owner: coding model performs ordinary verification; human/CI can evaluate results outside the session.
- Supporting / enforcement mechanisms: verification shell commands inside macro graph, `ValidatorConfig` field, agent-mode metadata and external benchmark verifiers.
- Closure path: command/test output returns to current coding actor; no separate first-party S3* reviewer-to-management correction is wired in bundled direct/balanced session.
- Why this is / is not agent-owned: declaring a validator configuration is not executing a distinct reviewer with direct source access; bundled coding agent variants set validator off and evaluation benchmark sits outside distribution.
- Evidence: [mod.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/agent_router/mod.rs); [agent_management.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/state_machine/agent_management.rs); [agent_config.json](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/src/direct/agent_config.json); [process.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/process.rs); [handler.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/tools/src/command_run/handler.rs); [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/ARCHITECTURE.md)
- Basis: explicit configured modes and structural call-site review
- Confidence: medium; other user-defined modes not credited without executed reachable audit wiring
- Caveats: a `general` constructor describes `need_validator:true`, but its flag alone, without a demonstrated validator dispatch/decision/return path, does not establish S3*. 

### Absence scope

- Surfaces inspected: bundled agent configs and registry, validator flag declarations, runtime execution and benchmark verification surfaces
- Plausible first-party paths checked: direct-access separately owned auditor dispatch, independent verdict, feedback to distinct manager and a corrective consequence
- Why no material first-party path remains: reviewed standard coding configs disable validator, and no material executable audit adjudication/return to first-party current-control was evidenced; test/benchmark verification cannot donate ownership.

## S4 — Outside-and-then intelligence

- State: —
- Function: no agent-owned future capability adaptation cycle reads external environment, decides long-horizon change and returns modified system capacity.
- Disturbance / variety regulated: changes in provider access or future development constraints.
- Decisive decision or feedback right: no model-led prospective capability investment/adoption decision and changed operational organization.
- Decision owner: human selects agent/provider variant and tool capabilities; coding model selects present task commands.
- Supporting / enforcement mechanisms: provider route config, command macro strategies, conversation compaction and stored agent profiles.
- Closure path: selected provider/tool capabilities are used now; no applied future organizational adaptation stage is returned to present control.
- Why this is / is not agent-owned: tool efficiency optimizations and alternative fast/balanced prompt profiles are prebuilt choices, not S4 intelligence and adaptation of the system organization.
- Evidence: [README.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/README.md); [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/ARCHITECTURE.md); [store.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/src/store.rs); [compaction.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/context/compaction.rs); [mod.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/agent_router/mod.rs)
- Basis: explicit/structural
- Confidence: medium-high
- Caveats: future roadmap and benchmark research are maintainer activity outside runtime.

### Absence scope

- Surfaces inspected: bundled agent variants, provider routing, state/context management, current task command graphs and docs
- Plausible first-party paths checked: prospective external sensing, adoption alternatives, legitimate adaptation decision and return to ongoing organizational capability
- Why no material first-party path remains: configured modes and context handling serve execution efficiency for current tasks, without an integrated prospective adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no ultimate organizational identity/purpose policy authority and binding return path at the coding-session recursion.
- Disturbance / variety regulated: constitutional or organization-purpose conflicts distinct from accepting shell/file command effects.
- Decisive decision or feedback right: no first-party identity arbiter or parent constitutional decision returned to operation.
- Decision owner: user/operator external to the runtime owns task identity/provider/permissions and organizational purpose.
- Supporting / enforcement mechanisms: runtime permission enforcement, static capabilities and agent config, session/router service policy.
- Closure path: tool approval or configured capability authorizes one coding effect; no ultimate-policy matter escalates to an identity owner and changes operational governing purpose.
- Why this is / is not agent-owned: runtime capabilities and request permissions protect operations, not decide mission-level purpose/identity.
- Evidence: [permission.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/tool_flow/permission.rs); [ARCHITECTURE.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/agents/ARCHITECTURE.md); [mod.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/agent_router/mod.rs); [process.rs](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/crates/runtime/src/manas/process.rs); [README.md](https://github.com/Tura-AI/tura/blob/81fc96729115c85bd5be3e6f6b6a13893d4065c5/README.md)
- Basis: structural
- Confidence: medium-high
- Caveats: project governance and hosted service decisions are external/adjacent to the assessed standard coding session.

### Absence scope

- Surfaces inspected: agent configs and capability whitelists, runtime permission, session owner policy and project governance docs
- Plausible first-party paths checked: identity conflict route, authorized parent policy decision and binding change in system purpose
- Why no material first-party path remains: observed enforcement constrains tools/sessions only; no decisive S5 policy/identity owner or return found.

## Recursion

One model-led coding session is the system-in-focus. The command macro contains many executable steps, but these are not separate S1 agents. Router worker processes host individual client sessions; unrelated user sessions are not a recursively managed workforce here. Alternate first-party agents in the registry represent selectable roles/configurations, not an automatically active organization.

## Variety and escalation

The model chooses engineering actions; deterministic macro control reduces feedback latency and can stop on failing tools; later tool output returns to the model. Runtime isolation, permissions and session DB ownership handle technical execution variety. None of those mechanisms alone owns multi-S1 interference control, organizational current control, independent audit, external-and-then adaptation or identity governance.

## Evidence gaps

Pinned-source static review, no live model-key run. The source contains a separate test-only child-router CLI helper and validator flags; neither was upgraded to positive S2/S3/S3* without a standard-mode executable decision/return chain. A distinct supported live multi-agent configuration, if later established on the same frozen SHA, would warrant targeted correction rather than silently credited adjacent behavior. Negative states are bounded to the shipped first-party modes examined.
