---
harness_id: cassady
project_name: Cassady
repository: https://github.com/owenqwenstarsky/cassady
review_ref: 1d3c354b8b92a7c3020a414ab510679459431556
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Cassady

## Review boundary

- System in focus: first-party Cassady Rust coding-agent CLI, provider-driven file/read/edit/search/shell tool loop, access rules, session storage and conversation branching, including the embeddable headless agent route.
- Purpose and identity: user-directed source inspection, project modifications, and shell/test operations.
- Relevant environment: code repository, shell output, model provider, user approval, persisted conversation and files.
- Standard-distribution boundary: native cass/cassady coding runtime with its own tool loop, not imported Codex coding agent, external model provider, npm/release transport, GUI shell or GitHub maintainer processes.
- Credited operating / distribution surfaces: src/agent.rs, src/tools, src/security.rs, src/access.rs, src/conversation.rs, src/embedding.rs, shipped CLI and app entrypoints.
- Adjacent first-party surfaces excluded from ownership: optional desktop UI, developer CI, roadmap/future features, provider internal organization and npm packaging.
- First-party operating / deployment modes considered: read-only, workspace-edit, full-access, terminal UI, headless embedding, branch/restore, user approval of commands, model switching and saved conversation resume.
- Recursion level: active local coding session with one agent-controlled operating S1; saved alternate conversations and tool processes are not distinct independent ongoing S1 units.
- Reviewed revision: 1d3c354b8b92a7c3020a414ab510679459431556.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Cassady has a first-party Rust model/tool loop. In src/agent.rs, run_turn_with_commands builds a provider request with native tool schemas, executes model-selected file/shell calls under tool authorization, appends results to its own conversation and repeats until the model finishes. ChatGPT Codex can be used as a provider preset but does not execute a separate imported coding harness in this route.

Its three access modes change permissible file/shell actions. Workspace-edit shell commands can require human approval, while read-only hides mutating tools. Conversation branches create alternative recorded trajectories; optional file restoration affects only tracked changes with safety checks, not concurrent independently operating coding S1s. Model-facing tool-result compaction preserves provenance, but it is support for the same coding task and does not establish an independent auditor.

No distinct first-party coordinating peer, multi-cell current manager, complementary source auditor, prospective external strategy actor or ultimate policy-governing agent has been established in the pinned deployed coding organization.

Primary source anchors: [src/agent.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/agent.rs); [src/tools/mod.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/tools/mod.rs); [src/security.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/security.rs); [src/access.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/access.rs); [src/conversation.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/conversation.rs); [src/embedding.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/embedding.rs).

## Operational model

One agent selects coding actions based on real project feedback and optional permission decisions. It can continue or fork saved sessions; those are histories of the same operating work, rather than a separately governed organization.

## S1 — Operations

- State: A
- Function: Execute agent-chosen source reading/editing and shell/test tool actions.
- Disturbance / variety regulated: Changing user requirements, files, tool errors and command outputs.
- Decisive decision or feedback right: Select next source/shell operation based on real returned evidence.
- Decision owner: Native Rust Cassady model-driven coding loop.
- Supporting / enforcement mechanisms: Provider tool-call schema and adapters, file/search/shell tools, conversation state, user permission gates.
- Closure path: User task → model tool call → local file/shell handler → result appended to conversation → next model decision or final response.
- Boundary reachability: The shipped interactive and embedded headless calls execute Cassady's own agent/tool loop with first-party source/shell tools.
- Why this is / is not agent-owned: The model owns operational discretion and the first-party runtime executes it.
- Evidence: [src/agent.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/agent.rs); [src/tools/mod.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/tools/mod.rs); [src/tools/write.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/tools/write.rs); [src/tools/edit.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/tools/edit.rs); [src/tools/shell.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/tools/shell.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Scoped to the frozen installed first-party coding runtime.

## S2 — Coordination

- State: —
- Function: No active two-S1 interdependence stabilization.
- Disturbance / variety regulated: Tools are executed in one coding-agent loop; forked histories do not compete as live independently responsible coding operations.
- Decisive decision or feedback right: No inter-S1 conflict detection/arbitration or responsive cross-unit decision.
- Decision owner: None evidenced.
- Supporting / enforcement mechanisms: Serial tool dispatch, recorded history and file restoration.
- Closure path: Tool outcomes return to one model, without a peer-agent control return.
- Why this is / is not agent-owned: A tool, model-provider call or alternate conversation branch is not a second operational S1.
- Evidence: [src/agent.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/agent.rs); [src/conversation.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/conversation.rs); [src/branch.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/branch.rs); [src/file_edits.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/file_edits.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Scoped to the frozen installed first-party coding runtime.

### Absence scope

- Surfaces inspected: Provider-to-agent tool loop, native tools, access/security guards, conversation branching, file edits and embedded session routing.
- Plausible first-party paths checked: A distinct S2 organizational decision-maker with its own evidence, authority and corrective/allocative feedback into operations.
- Why no material first-party path remains: All evidenced actions are task-level support for a single model-directed coder or human access choice, without an independently completed S2 operating relation.

## S3 — Inside-and-now control

- State: —
- Function: No distinct whole-current controller allocating live duties among several S1 cells.
- Disturbance / variety regulated: Active command permission, status and tool failure are individual coding task disturbances.
- Decisive decision or feedback right: Human grants/denies a shell/tool request; runtime processes task outcome.
- Decision owner: User and deterministic access policy, not first-party managerial agent.
- Supporting / enforcement mechanisms: Access mode rules, approval messages, current turn state.
- Closure path: The one coding loop continues or is blocked; no independent global priority or supervisory action into multiple S1s.
- Why this is / is not agent-owned: Current task status/control cannot stand in for whole-current multi-operation management.
- Evidence: [src/agent.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/agent.rs); [src/app.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/app.rs); [src/access.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/access.rs); [src/security.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/security.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Scoped to the frozen installed first-party coding runtime.

### Absence scope

- Surfaces inspected: Provider-to-agent tool loop, native tools, access/security guards, conversation branching, file edits and embedded session routing.
- Plausible first-party paths checked: A distinct S3 organizational decision-maker with its own evidence, authority and corrective/allocative feedback into operations.
- Why no material first-party path remains: All evidenced actions are task-level support for a single model-directed coder or human access choice, without an independently completed S3 operating relation.

## S3* — Complementary audit

- State: —
- Function: No separately owned independent operational audit plus corrective return.
- Disturbance / variety regulated: Faulty source changes and dangerous shell operations are possible.
- Decisive decision or feedback right: Static policy allow/ask/deny and human approval; no independent audit findings on code.
- Decision owner: Human approval and tool guard, not separate supplementary auditor.
- Supporting / enforcement mechanisms: PolicyDecision, runtime tool results, tracked file edits and display compaction.
- Closure path: Guard blocks/permits one tool; ordinary output returns to the same coding model with no separate audit decision.
- Why this is / is not agent-owned: Safety approvals and evidence preservation do not amount to an independent S3* control channel.
- Evidence: [src/agent.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/agent.rs); [src/security.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/security.rs); [src/tools/mod.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/tools/mod.rs); [src/file_edits.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/file_edits.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Scoped to the frozen installed first-party coding runtime.

### Absence scope

- Surfaces inspected: Provider-to-agent tool loop, native tools, access/security guards, conversation branching, file edits and embedded session routing.
- Plausible first-party paths checked: A distinct S3* organizational decision-maker with its own evidence, authority and corrective/allocative feedback into operations.
- Why no material first-party path remains: All evidenced actions are task-level support for a single model-directed coder or human access choice, without an independently completed S3* operating relation.

## S4 — Outside-and-then intelligence

- State: —
- Function: No future environment intelligence with binding capability renewal.
- Disturbance / variety regulated: Future provider/version changes and ecosystem shifts require prospective appraisal.
- Decisive decision or feedback right: User chooses provider/model and product updates; coder plans the immediate task.
- Decision owner: No agent-owned strategic decision owner.
- Supporting / enforcement mechanisms: Config, model metadata, session histories, update commands and context truncation.
- Closure path: Settings/history affect later work, but no strategic sensing/options/adaptation decision returns to the coding organization.
- Why this is / is not agent-owned: Model switching and saved context are not autonomous S4.
- Evidence: [src/config.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/config.rs); [src/agent.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/agent.rs); [src/update.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/update.rs); [src/conversation.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/conversation.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Scoped to the frozen installed first-party coding runtime.

### Absence scope

- Surfaces inspected: Provider-to-agent tool loop, native tools, access/security guards, conversation branching, file edits and embedded session routing.
- Plausible first-party paths checked: A distinct S4 organizational decision-maker with its own evidence, authority and corrective/allocative feedback into operations.
- Why no material first-party path remains: All evidenced actions are task-level support for a single model-directed coder or human access choice, without an independently completed S4 operating relation.

## S5 — Policy and identity

- State: —
- Function: No ultimate purpose/identity decision affecting the whole organization.
- Disturbance / variety regulated: Read-only, workspace-edit and full-access preferences are operational tool-risk choices.
- Decisive decision or feedback right: Human sets access posture and approves commands; deterministic enforcement executes it.
- Decision owner: Operator and static tool security policy.
- Supporting / enforcement mechanisms: AccessMode, PolicyDecision, approval channel and config.
- Closure path: Tool allowed or denied; no highest-policy governance deliberation or binding identity return.
- Why this is / is not agent-owned: Per-command human approval is not an autonomous constitutional S5 actor.
- Evidence: [src/access.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/access.rs); [src/security.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/security.rs); [src/agent.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/agent.rs); [src/config.rs](https://github.com/owenqwenstarsky/cassady/blob/1d3c354b8b92a7c3020a414ab510679459431556/src/config.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Scoped to the frozen installed first-party coding runtime.

### Absence scope

- Surfaces inspected: Provider-to-agent tool loop, native tools, access/security guards, conversation branching, file edits and embedded session routing.
- Plausible first-party paths checked: A distinct S5 organizational decision-maker with its own evidence, authority and corrective/allocative feedback into operations.
- Why no material first-party path remains: All evidenced actions are task-level support for a single model-directed coder or human access choice, without an independently completed S5 operating relation.

## Distributed OSS parent arrangement

The product's GitHub maintainers, provider platform and package release CI are adjacent systems rather than organizational authorities within this coding session.

## Self-hosted and non-human modes

Cassady's interactive and headless modes own native model/tool execution. A Codex model provider is inference, not a borrowed coding-loop owner.

## Recursion

One active coding session contains one S1; file/shell tools, saved branches, permissions and model configuration provide support within that recursion.

## Variety and escalation

Tool errors, unsafe command denial and user approvals affect this one coder. No independently audited verdict or highest-order policy return follows from a captured result.

## Evidence gaps

No benchmark success or system quality claims are inferred from source code or README. Externally designed multi-agent organizations may need separate evidence.
