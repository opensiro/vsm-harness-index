---
harness_id: lobehub
project_name: LobeHub
repository: https://github.com/lobehub/lobehub
review_ref: 3af256caae11796da471bec5f57d882853f30f19
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.4
profile_version: 0.2.2
assessment_procedure_version: 0.3.4
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# LobeHub

## Review boundary

- System in focus: LobeHub's first-party Agent/Agent Group runtime, group supervisor/orchestration tools, agent-management tools, scheduling and memory surfaces at the pinned revision.
- Purpose and identity: provide a workspace where users create and operate specialized agents individually or in groups, including supervisor-led multi-agent collaboration and task execution.
- Relevant environment: user requests, model/provider services, plugins/tools, marketplace agents, external data accessed through tools and user-managed workspace context.
- Standard-distribution boundary: first-party LobeHub application, Agent Group runtime and bundled management/orchestration tools; configured foundation models are execution hosts.
- First-party operating / deployment modes considered: individual agents, Agent Groups with orchestrator, sequential/parallel/iterative/debate collaboration, async agent tasks, self-hosted deployment and editable personal memory.
- Recursion level: one Agent Group when evaluating S2/S3*; individual agent operation remains the S1 substrate.
- Reviewed revision: `3af256caae11796da471bec5f57d882853f30f19`.
- Observation date: 2026-09-18.
- Generated Profile version: `0.2.2`.
- Generated Methodology version: `0.3.4`.
- Current Profile version: `0.2.2`.
- Current Methodology version: `0.3.4`.

## Repository architecture

LobeHub exposes individual agents plus Agent Groups. A built-in Group Supervisor receives tool contracts for speaking to one agent, broadcasting, executing one long task, executing parallel tasks and voting. The supervisor prompt instructs the model to analyze whether work is dependent, independent, opinion-seeking or extended and to choose the corresponding coordination pattern. Agent-management tooling can create, inspect, update and invoke agents. Personal Memory and continual-learning features adapt agents to user history.

## Operational model

S1 units are specialized model-driven agents performing the group's delegated work. The Group Supervisor is a model-driven coordination actor that selects agents, sequencing and parallelism, then resumes after member results to synthesize or continue. First-party iterative examples also expose a Writer→Editor→revision review loop, but reviewer independence/authority is composition-dependent rather than a mandatory autonomous audit role, so that path is constructor-level S3*.

## Primary evidence

- [`README.md`](https://github.com/lobehub/lobehub/blob/3af256caae11796da471bec5f57d882853f30f19/README.md) — product boundary, Agent Groups, scheduling and memory/learning.
- [`docs/usage/agent/agent-team.mdx`](https://github.com/lobehub/lobehub/blob/3af256caae11796da471bec5f57d882853f30f19/docs/usage/agent/agent-team.mdx) — sequential/parallel/iterative/debate modes and orchestrator responsibilities.
- [`packages/builtin-tool-group-management/src/systemRole.ts`](https://github.com/lobehub/lobehub/blob/3af256caae11796da471bec5f57d882853f30f19/packages/builtin-tool-group-management/src/systemRole.ts) — model-owned mode selection, task decomposition, parallel execution and synthesis contract.
- [`packages/builtin-tool-agent-management/src/manifest.ts`](https://github.com/lobehub/lobehub/blob/3af256caae11796da471bec5f57d882853f30f19/packages/builtin-tool-agent-management/src/manifest.ts) — create/update/search/call agent tools and supervisor-resume semantics.
- [`packages/agent-runtime/src/groupOrchestration/GroupOrchestrationSupervisor.ts`](https://github.com/lobehub/lobehub/blob/3af256caae11796da471bec5f57d882853f30f19/packages/agent-runtime/src/groupOrchestration/GroupOrchestrationSupervisor.ts) — first-party group supervisor runtime.

## S1 — Operations

- State: A
- Function: specialized agents autonomously perform assigned conversational, research, creation or tool-using work.
- Disturbance / variety regulated: open-ended user tasks, domain-specific information, tool/model observations and task-specific uncertainty.
- Decisive decision or feedback right: choose the substantive actions and output needed for the agent's assigned task or conversational role.
- Decision owner: the invoked model-driven agent.
- Supporting / enforcement mechanisms: agent configuration, system role, model/provider selection, plugins, isolated async task context and session state.
- Closure path: agent receives an instruction, performs work, returns a result to the group/user, and that result becomes input to subsequent orchestration or conversation.
- Why this is / is not agent-owned: the model-driven agent owns substantive task execution while LobeHub transports context/tools/results.
- Evidence: `README.md`, `docs/usage/agent/agent-team.mdx`, agent-management manifest/system role.
- Basis: explicit + structural
- Confidence: high
- Caveats: marketplace/configured models are hosts; organizational ownership is credited only through the LobeHub first-party runtime.

## S2 — Coordination

- State: A
- Function: coordinate multiple specialized S1 agents by choosing dependent versus parallel work, agent selection, handoff order and group interaction mode.
- Disturbance / variety regulated: dependency-sensitive work that would be wrong in parallel, redundant/overlapping contributions, poor handoffs and unstructured multi-agent interaction.
- Decisive decision or feedback right: choose whether to use one agent, broadcast, sequential speaking, one async task or multiple parallel tasks, and choose the participating agents/instructions.
- Decision owner: the model-driven Group Supervisor / Orchestrator.
- Supporting / enforcement mechanisms: `speak`, `broadcast`, `executeAgentTask`, `executeAgentTasks`, group orchestration runtime, shared group context and supervisor resume after member completion.
- Closure path: supervisor analyzes the request, selects a coordination pattern and dispatches agents; member results return to the supervisor, which synthesizes, follows up or changes the next interaction.
- Why this is / is not agent-owned: deterministic runtime executes the selected pattern, but the supervisor model owns the coordination discretion over mode, agent selection and follow-up.
- Evidence: `packages/builtin-tool-group-management/src/systemRole.ts`, `docs/usage/agent/agent-team.mdx`, group orchestration runtime.
- Basis: explicit + structural
- Confidence: high
- Caveats: generic `callAgent` alone would not establish S2; the positive mapping depends on the explicit dependency/parallelism decision framework and returned supervisor loop.
- Distinct S1 units: two or more specialized agents in an Agent Group, each capable of separate operational work.
- Inter-S1 disturbance: dependent subtasks can be run in the wrong order, overlapping agents can add redundant work, and independent subtasks can be unnecessarily serialized; first-party guidance also calls out weak handoffs and overlapping roles as collaboration failures.
- Attenuating coordination relation: the Group Supervisor chooses sequential, parallel, broadcast or focused modes and assigns work to agents according to dependency and expertise.
- Feedback into subsequent S1 behaviour: member outputs resume the supervisor; it can ask follow-ups, synthesize, invoke another agent or terminate the group turn, thereby changing later contributions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: first-party supervisor policy explicitly diagnoses dependence/parallelizability and selects an attenuation pattern for interactions among distinct operational agents, with returned member results driving further coordination.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-group current-control function over resources, commitments, priorities or constraints is established beyond the S2 orchestration itself.
- Disturbance / variety regulated: group task routing, model choice and current conversation state were inspected, but no distinct S3 current-control loop is established.
- Decisive decision or feedback right: no material first-party owner was found with a whole-system current view and separate authority over group-wide commitments/resources/accountability.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: agent management, group profile editing, async task execution, scheduling and supervisor orchestration.
- Closure path: no qualifying distinct S3 loop was found.
- Why this is / is not agent-owned: the orchestrator's evidenced rights are inter-agent task/mode coordination for the current group operation; naming it supervisor/operator is not enough to promote that same function to S3.
- Evidence: group-management system role, Agent Group docs, agent-management tools.
- Basis: structural
- Confidence: medium-high
- Caveats: LobeHub exposes rich management primitives, but generic ability to edit/create agents is not a demonstrated whole-system current-control owner.

### Absence scope

- Surfaces inspected: Agent Group docs/runtime, group-management tools, agent-management CRUD/call tools, schedules/workspaces and README operator claims.
- Plausible first-party paths checked: orchestrator/supervisor, agent creation/update, scheduling/reporting and group profile changes.
- Why no material first-party path remains: the reviewed first-party autonomous path closes task coordination but does not establish a distinct agent-owned whole-system current-control function over commitments/resources/accountability at the declared recursion.

## S3* — Complementary audit

- State: C
- Function: review another agent's produced work through a distinct reviewer/editor role and return critique into revision/re-review.
- Disturbance / variety regulated: incomplete, unclear, inconsistent or low-quality outputs that require a second perspective before acceptance.
- Decisive decision or feedback right: judge produced work, issue feedback and require/refine another contribution.
- Decision owner: constructor path; LobeHub supplies explicit iterative/reviewer group patterns, but the developer/user must compose the reviewer role, independence and authority in the concrete group.
- Supporting / enforcement mechanisms: iterative Agent Group mode, distinct agent identities, sequential handoffs, shared context and supervisor-mediated repeated turns.
- Closure path: producer emits work; reviewer/editor returns critique; producer revises; reviewer can perform final review in the documented iterative pattern.
- Why this is / is not agent-owned: a separate model-driven reviewer can own the judgment once composed, but the standard distribution does not assign an invariant independent reviewer or audit authority automatically.
- Evidence: `docs/usage/agent/agent-team.mdx`, `packages/builtin-tool-group-management/src/systemRole.ts`.
- Basis: explicit
- Confidence: medium
- Caveats: ordinary debate or synthesis is not counted as S3*; the positive constructor claim is limited to the explicitly documented review/refine pattern with distinct roles.
- Claim being audited: that another agent's draft/output is sufficiently correct, clear or complete for the group's purpose.
- Ordinary reporting path: producer agent returns its draft/result through the normal group turn.
- Complementary access path: a separately configured Editor/reviewer/QA agent receives the produced work and can critique it in an iterative group workflow.
- Independence boundary: first-party group mechanics preserve distinct agent identities, but organizational independence/authority of the reviewer is supplied by the group composition rather than guaranteed by runtime policy.
- Who acts on findings: the producing agent receives reviewer feedback and revises; the group/supervisor can route the revised result back for final review.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate external/prospective organizational intelligence loop is established at the Agent Group boundary.
- Disturbance / variety regulated: user preference/history changes are learned, but no distinct future/environment adaptation function is closed.
- Decisive decision or feedback right: no material first-party owner was found that senses external/future distinctions, generates adaptation options and returns a selected change into group capability/S3.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: Personal Memory, editable structured memory, continual learning and tool/search capability.
- Closure path: memory changes later agent context directly; no separate outside-and-then option-development loop is established.
- Why this is / is not agent-owned: personalization/learning and external tools do not automatically establish S4.
- Evidence: `README.md`, Agent Group/runtime docs.
- Basis: explicit + structural
- Confidence: high
- Caveats: individual agents may perform research as S1 work; that does not become the harness's S4 without a distinct adaptation closure.

### Absence scope

- Surfaces inspected: README Evolve/Personal Memory, Agent Group modes, agent-management tools, schedules and search/plugin capabilities.
- Plausible first-party paths checked: continual learning, memory, research agents, marketplace search and create/refine agent workflows.
- Why no material first-party path remains: these paths personalize or execute user work; no first-party external/future sensing → adaptation option → present capability/S3 loop is established.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy governance function is established for the Agent Group.
- Disturbance / variety regulated: group prompt, member roster and agent configuration can change, but no ultimate identity dispute/authority loop is evidenced.
- Decisive decision or feedback right: no material first-party identity-level authoritative decision with a return-to-operation closure was found.
- Decision owner: none established for qualifying S5.
- Supporting / enforcement mechanisms: group profile, Agent Builder, agent CRUD, prompts, skills and user configuration.
- Closure path: configuration edits alter operation, but they are not an evidenced S5 identity/ultimate-policy process.
- Why this is / is not agent-owned: prompts and editable configuration are implementation/control artifacts, not proof of VSM S5.
- Evidence: `docs/usage/agent/agent-team.mdx`, agent-management manifest/system role.
- Basis: structural
- Confidence: high
- Caveats: the user clearly remains able to configure the group, but generic configurability is insufficient for standalone `P`.

### Absence scope

- Surfaces inspected: group creation/profile, Agent Builder, agent-management tools, self-management, prompts/skills and self-hosted operator surfaces.
- Plausible first-party paths checked: changing group prompt, roster, models/plugins, creating/deleting agents and self-modifying an agent's prompt.
- Why no material first-party path remains: these are configuration/operational changes; no identity/ultimate-policy issue is routed to a legitimate ultimate authority and returned through an explicit S5 closure.

## Recursion

Agent Groups contain multiple agents and can invoke heterogeneous external runtimes, but the reviewed evidence does not establish recursively nested full viable organizations. The assessment therefore maps one Agent Group without treating every child agent as its own full recursion.

## Variety and escalation

The supervisor attenuates collaboration variety by selecting focused, broadcast, sequential or parallel execution and can iterate after member results. Ambiguous requests may be clarified with the user; this is task clarification, not a separate S5 closure.

## Evidence gaps

S3* is the narrowest positive claim: the repository explicitly supplies reviewer/editor iterative patterns, but concrete independence and authority remain composition-dependent, hence `C` rather than `A`.
