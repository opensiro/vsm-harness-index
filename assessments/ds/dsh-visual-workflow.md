---
harness_id: dsh-visual-workflow
project_name: dsh Visual Workflow
repository: https://github.com/GZX2211/dsh-Visual-Workflow
review_ref: 4cd99b20713ef2a488522ccf5a95807274a1a6ab
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# dsh Visual Workflow

## Review boundary
- System in focus: One locally installed Visual Workflow host plugin running a workflow or headless API service instance, a root orchestration agent, dynamically instantiated child role agents and persisted organizational assets/experience.
- Purpose and identity: Execute a configurable multi-agent graph or adaptive meta-orchestrated task with model-selected work and model-managed current graph/dispatch decisions, while operator edits may affect running work.
- Relevant environment: User task/request, graph topology and node states, child results, tooling and model-provider feedback, dynamic user graph edits, prior successful/failed task experiences and runtime status.
- Standard-distribution boundary: Node plugin as shipped in package `lib`, original `src/host` runtime, graph patch, org catalog, child runner, scheduler and experience services. Host model inference and official Agent Team implementations are dependencies and cannot independently donate VSM ownership.
- Credited operating / distribution surfaces: First-party parent/child model prompts and tool rights, workflow start/child launch/current run callbacks, root-only graph mutation, visible updated run graph, parent-result feedback and optional operator current intervention.
- Adjacent first-party surfaces excluded from ownership: Dev-only tests/CI, aspirational roadmap text, screenshots without runtime wiring, external provider model training, officially supplied Agent Team task board unless the plugin itself closes the claimed coordination.
- First-party operating / deployment modes considered: Installed plugin in mode1 flow orchestration with root model and local child agents; optional mode2 API service with single parent answering; UI edits of active instance; installed Experience recall/feedback tools when configured.
- Recursion level: One executing workflow with multiple child task operations under one parent current controller, not the plugin vendor's own company organization.
- Reviewed revision: 4cd99b20713ef2a488522ccf5a95807274a1a6ab.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture
The package's entry point targets committed `lib/index.js` while `src/host` holds typed source for tools and runtime. User selects roles, model/tools, edges and flow mode. The main model agent is configured as the parent; `wf_org_catalog` returns the active flow definition, `wf_run_node` launches configured child agents from an active run and `wf_finish` closes it. Child state changes arrive through a first-party subagent-end observer and are persisted for future parent decisions. Only the root can patch running instance topology with `wf_graph_patch`, which validates changes, saves new revision and refreshes the active run. UI workbench edits also appear in later dispatch checks. Experience recall/feedback stores and scores task histories so next runs can reuse them; retrospective memory does not independently establish outside-and-future strategy.

## Operational model
The root model is instructed to direct child work without performing the children’s tasks, to wait for settlement and acceptance, to choose actual conditional branches and retry/pause after failures. Each model child makes substantive choices against its user-assigned task and returns outputs. The same root also owns a distinct project-current control capability by choosing dispatch, applying valid graph topology changes and responding to child settlement; this is agent-owned S3 within this workflow recursion. Deterministic graph validation/locks and operator pause or edits constrain the root. No independently sourced current-work audit actor, outside-future sensing/strategic adaptation or ultimate identity-policy dispute closure was established.

## S1 — Operations
- State: A
- Function: Execute assigned task nodes using model-selected reasoning and tool actions.
- Disturbance / variety regulated: Open-ended task inputs, code/text/API returns, changed upstream node outputs and task-specific failures.
- Decisive decision or feedback right: Child role model selects which tools and actions fulfill the delegated node request and returns evidence/output; root may also operate in the API service mode answering user questions.
- Decision owner: First-party spawned child-role model agents constrained by configured role, model, tools and ReAct/retry limits.
- Supporting / enforcement mechanisms: Agent runner, task node context builder, tool-filter scopes, model selection and node completion observer.
- Closure path: Root issues `wf_run_node`; first-party runtime starts child node; child model executes substantive work and returns its answer; observer records result and wakes waiting parent, which may launch later work.
- Boundary reachability: Standard installed host plugin registers these tool/runner surfaces and a first-party root/child flow. The external model provider supplies inference only; no external whole-agent conductor is required.
- Why this is / is not agent-owned: Child model decides nontrivial operational work, rather than a fixed DAG only replaying predetermined command outputs.
- Evidence: [node start/dispatch](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/orchestrator/runtime-execute.ts#L44-L130), [first-party child role runner and tool scope](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/agent/runner.ts#L443-L510), [child completion return](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/orchestrator/runtime-observe.ts#L13-L90), [shipped node tools](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/shared/protocol.ts#L201-L260).
- Basis: structural
- Confidence: high
- Caveats: Source-pinned assessment only. Requires a functional host model/session; no live paid provider inference run was made.

## S2 — Coordination
- State: —
- Function: No independently demonstrated relation detecting and attenuating concrete interference among two distinct operating child agents rather than ordinary workflow order and communication.
- Disturbance / variety regulated: Two child agents may collide on a shared file, task board role or scarce tool resource.
- Decisive decision or feedback right: A coordinator would need a specific cross-agent conflict witness, resolution decision and returned constraints on both affected operations.
- Decision owner: Root parent and host enforce flow schedules; official Team runtime may handle its own collaboration, but the plugin-owned S2 interference loop is not evidenced.
- Supporting / enforcement mechanisms: DAG flow edges, node limits, worktree/run locks, `wf_send_message`, optional official Team task-board and CAS.
- Closure path: Messages and dependency order can change what child runs next, but no first-party documented or coded conflicting pair is resolved through a dedicated attenuation decision.
- Why this is / is not agent-owned: Scheduling a graph, a task board, ordinary peer messages, CAS safety and node retry logic do not prove independently owned S2 conflict attenuation.
- Evidence: [default Team/degraded messaging modes](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/README.en.md#L101-L110), [root role instructions](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/prompts/texts/en/parent-orchestrator.ts#L7-L30), [fallback message tool](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/tools/wf-send-message/tool.ts#L1-L106)
- Basis: structural
- Confidence: medium
- Caveats: Possible user-composed flow conflict resolution is not a first-party general S2 closure.

### Absence scope
- Surfaces inspected: Root/child prompts, work-state mutation, messaging, team mode fallback, graph patch and official Team adapter.
- Plausible first-party paths checked: Sought a concrete inter-S1 conflict discriminator (contention/contradictory commitments) and selected mitigation applied to affected children, not just graph order or provider-owned task board.
- Why no material first-party path remains: Scheduling a graph, a task board, ordinary peer messages, CAS safety and node retry logic do not prove independently owned S2 conflict attenuation.

## S3 — Inside-and-now control
- State: A
- Function: Control currently executing workflow commitments by observing child results, choosing conditional branches and revising the current graph/dispatch plan.
- Disturbance / variety regulated: Failed or incomplete child outputs, dynamically changed graph topology and currently running nodes that require retrial, delay or alternative resource allocation.
- Decisive decision or feedback right: Root model selects which child tasks to start/continue, whether acceptance criteria are met, whether to retry/pause or modify the organization graph, and when to close the current workflow.
- Decision owner: Separate root orchestration model role inside the installed workflow, distinguished from child node operating agents; operator can override by live UI edits.
- Supporting / enforcement mechanisms: `wf_org_catalog` complete active graph/node view, `wf_run_node`/wait results, root-only graph-patch tool, completed child observation, live graph revision refresh and bounded global call limits.
- Closure path: Root retrieves current workflow topology, receives actual child finish/error events and outputs, chooses dispatch/graph change; validated `wf_graph_patch` persists revision and refreshes current running baseline; later `wf_run_node` re-reads it, launching/withholding a different child. Root may finish the run only after returned outcomes.
- Boundary reachability: Mode1 installed parent orchestrator has the prescribed prompt, active-run graph catalog and root-only patch/dispatch tools, while child agents are expressly denied root orchestration rights.
- Whole-system current view: First-party catalog of current instance with node/flow/role structure plus subagent-end snapshots, node status and accepted output.
- Current-control decision scope: Reorganize present flow graph, choose next child launch, change/retry delivery, pause for human after exhausted retry and close the present run.
- Why this is / is not agent-owned: Root model decides substantive scheduling/organizational adjustments from current results; host validates and applies them, so this is not merely an autonomous child S1 mislabelled as whole-project S3.
- Evidence: [root current-control role and acceptance check](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/prompts/texts/en/parent-orchestrator.ts#L7-L30), [root-only dispatch and current graph reload](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/orchestrator/runtime-execute.ts#L24-L130), [subagent outcome/feedback](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/orchestrator/runtime-observe.ts#L13-L90), [graph patch ownership and live rebind](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/tools/wf-graph-patch/tool.ts#L488-L527), [root-only graph patch tool](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/tools/wf-graph-patch/tool.ts#L598-L675).
- Basis: structural
- Confidence: medium
- Caveats: Mode-specific to an installed multi-node workflow using a live root model and graph/dispatch tools. A human can change the canvas but is not the credited autonomous S3 actor; deterministic graph validation is not autonomous management.

## S3* — Complementary audit
- State: —
- Function: No separate independent complementary reality/audit actor with a returned corrective S3 finding is demonstrated for current whole-workflow state.
- Disturbance / variety regulated: Parent may accept an erroneous child result and self-reported completion without external reality correspondence.
- Decisive decision or feedback right: A complementary reviewer would sample actual task outcomes through an independent channel, challenge model claims and return findings for root/operator correction.
- Decision owner: Existing root model checks child acceptance and user may view logs; no separate audit actor with independent evidence-based authority is wired into this project workflow.
- Supporting / enforcement mechanisms: Node status, finish output, result transcript, Experience feedback and UI event logs.
- Closure path: Feedback travels to the same root controller or future experience store, but not from an independent audit mechanism into a distinct current-control correction.
- Why this is / is not agent-owned: Root checking its children's outputs and remembering their quality is part of primary S3/operational feedback, not proof of an independently sourced complementary audit.
- Evidence: [root acceptance instructions](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/prompts/texts/en/parent-orchestrator.ts#L7-L17), [child result events](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/orchestrator/runtime-observe.ts#L13-L90), [Experience feedback](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/experience/feedback.ts#L137-L215)
- Basis: structural
- Confidence: medium
- Caveats: An explicitly configured user review-node might implement audit within a particular flow but is not a default proved independent reviewer.

### Absence scope
- Surfaces inspected: Root/child roles and prompts, workflow event logs, Experience tools, graph validation and manual canvas.
- Plausible first-party paths checked: Searched for separately commissioned audit, independent evidence, findings routed to current root and actual corrective operation; found primary orchestration checks and retrospective scoring.
- Why no material first-party path remains: Root checking its children's outputs and remembering their quality is part of primary S3/operational feedback, not proof of an independently sourced complementary audit.

## S4 — Outside-and-then intelligence
- State: —
- Function: Experience recall and feedback provide past-work learning but not distinct prospective external intelligence with an authoritative future strategic adaptation loop.
- Disturbance / variety regulated: New requirements and external ecosystem changes could require different future organization designs beyond current task improvement.
- Decisive decision or feedback right: A distinct S4 function would observe future environmental developments, choose a prospective organizational change and return it to modify the organization's available capabilities.
- Decision owner: Root can modify present task graph and recall old experiences; no separate outside-future decision owner and returned new capability were demonstrated.
- Supporting / enforcement mechanisms: Experience submission, recall, usage tracking, embedding/ranking, scoring and scheduled workflows.
- Closure path: Ratings and retrieval affect later prompt choices, but are retrospective evaluation of current/past executions, not independently justified external prospective strategy.
- Why this is / is not agent-owned: Reinforcement-like experience storage is not S4 solely because its effects persist into subsequent tasks.
- Evidence: [Experience feedback storage](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/experience/feedback.ts#L78-L215), [experience service](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/experience/service.ts#L1-L90), [recall tool contract](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/tools/wf-experience-recall/tool.ts#L50-L96)
- Basis: structural
- Confidence: medium
- Caveats: Custom user goals may include future sensing; not credited without a first-party decision and returned adaptation witness.

### Absence scope
- Surfaces inspected: Experience learn/recall/feedback, rank/retirement, scheduled tasks, org catalog and dynamic graph patch.
- Plausible first-party paths checked: Looked for future external signal, prospective distinction, strategic option selection and durable change to organizational capabilities distinct from short-horizon graph control.
- Why no material first-party path remains: Reinforcement-like experience storage is not S4 solely because its effects persist into subsequent tasks.

## S5 — Policy and identity
- State: —
- Function: Root/child permissions, org budgets and user-created templates constrain an instance but do not establish an ultimate identity-policy dispute resolution and return.
- Disturbance / variety regulated: Agent could propose unauthorized graph edits or violate budgets or user preferences.
- Decisive decision or feedback right: S5 would require a legitimate authority to decide an ultimate identity/mission/policy issue and return a durable rule governing operating work.
- Decision owner: User may define a workflow goal and organizational metadata; host enforces root/child tool boundaries; no separate policy decision authority is proven.
- Supporting / enforcement mechanisms: Root-only graph patch, tool restrictions, graph schema validation, role presets, org metadata and human UI configuration.
- Closure path: A policy-like budget or node permission blocks invalid operations but does not demonstrate a mission/identity-level decision and returned system mandate.
- Why this is / is not agent-owned: Structural graph invariants, template ownership, prompt duties and runtime limits are governance support, not themselves an ultimate identity-policy closure.
- Evidence: [root tool role restriction](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/tools/wf-graph-patch/tool.ts#L598-L675), [child hidden tools](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/agent/runner.ts#L443-L510), [org metadata limits](https://github.com/GZX2211/dsh-Visual-Workflow/blob/4cd99b20713ef2a488522ccf5a95807274a1a6ab/src/host/graph/org-meta.ts#L1-L100)
- Basis: structural
- Confidence: medium
- Caveats: A broader human organization could use this tool as a work system, but that external policy actor is outside the assessed workflow recursion.

### Absence scope
- Surfaces inspected: Org metadata, tool permission boundaries, graph validation, human canvas configuration and parent duties.
- Plausible first-party paths checked: Sought a concrete identity/ultimate policy issue, legitimate deciding authority, competing permissible responses and a returned binding mandate beyond local graph changes.
- Why no material first-party path remains: Structural graph invariants, template ownership, prompt duties and runtime limits are governance support, not themselves an ultimate identity-policy closure.

## Distributed OSS parent arrangement
The plugin publisher/developer is not credited as runtime S5. At the selected execution recursion, the model root has current workflow control, children own task operations and the user can override current flow. External provider models and official Agent Team mechanisms are dependencies, not evidence of independent first-party organizational control.

## Self-hosted and non-human modes
The package ships a Node host plugin and compiled `lib` with optional mode1 workflow and mode2 API service. First-party tools register into the host runtime. Model inference and official team features are optional host dependencies; if the host is not available, positive model-owned functions are not established in a live deployment.

## Recursion
Distinct child node agents are operational S1 units in the current workflow; the model parent is a current whole-workflow controller that can change the graph and respond to results. There is no separately verified interference-attenuating S2 actor or complementary audit S3* actor. Later reuse of stored Experience is not evidence of future external adaptation.

## Variety and escalation
Dynamic graph re-read propagates user or model topology changes; child outcome events return statuses to the root; graph patch validates and returns errors/revisions; exhausted retries may place a pause gate for a human decision. Experience scoring influences later retrieval and selection. No ultimate identity policy closure is claimed.

## Evidence gaps
Pinned public source and shipped compiled entry inspection; no live paid model call or independent audit. This assessment credits a mode-specific root current-control S3 A, not the host provider's external team management. S2/S3*/S4/S5 negatives are bounded to inspected shipped runtime; agentic node tests or user-composed review flows may exist but are not presumed.
