---
harness_id: impulse
project_name: Impulse
repository: https://github.com/spenceriam/impulse
review_ref: 87f7019be3d73768baae8a1e330be436e1f167d4
reviewed_at: 2026-10-11
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

# Impulse

## Review boundary

- System in focus: the first-party Impulse terminal coding-agent application: its primary model/tool loop, executable coding tools, user-selected modes, first-party explore/general subagents, optional model advisor, persisted sessions, and goal continuation.
- Purpose and identity: perform user-directed investigation and software changes in a local working tree through iterative model-selected commands and file operations.
- Relevant environment: local project files and shell, user instruction and approval, provider inference endpoints, external web/MCP services, and installed project checks.
- Standard-distribution boundary: shipped CLI/TUI coding product, its agent/permission/session/tool runtime and packaged optional modes. Only behavior reachable from the product's own execution paths is credited.
- Credited operating / distribution surfaces: [src/cli.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/cli.ts), [src/cli/renderer.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/cli/renderer.ts), [src/agent/loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/loop.ts), [src/tools/registry.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/registry.ts), [src/tools/task.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/task.ts), [src/agent/task-pool.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/task-pool.ts), [src/agent/task-runner.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/task-runner.ts), [src/agent/advisor.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/advisor.ts), [src/agent/goal-loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/goal-loop.ts), [src/permission/index.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/permission/index.ts), and [src/session/manager.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/session/manager.ts).
- Adjacent first-party surfaces excluded from ownership: Impulse maintainer/release GitHub Actions, scripts/evaluation runs, developer tests, prompts used for product development, planned features in docs, and external model/provider/MCP/CI systems. Their behavior cannot be borrowed as a native decision owner.
- First-party operating / deployment modes considered: terminal interactive AGENT/EXPLORE/PLAN/DEBUG, provider-configured normal and advisor-gated turns, general and explore child tasks, persisted/restarted sessions, goal judging/continuation, human steering and approval, and CLI-supported coding tools.
- Recursion level: individual Impulse installation/session and its directly invoked child agent tasks; the user's software organization and project maintainer governance are not co-located as a higher Impulse recursion.
- Reviewed revision: 87f7019be3d73768baae8a1e330be436e1f167d4.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Impulse ships an executable TypeScript terminal coding agent. Its AgentLoop constructs provider/model messages and tool definitions, persists user/assistant/tool messages, invokes a model in a repeated streamed completion loop, parses emitted tool calls, enforces selected mode and permissions, executes first-party file/shell/search/web and task tools, returns results, and continues until the turn ends. The model can select the next action based on actual tool feedback; the runtime does not itself choose the coding solution. Provider APIs supply inference and not an external agent runtime. See [src/agent/loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/loop.ts), [src/tools/registry.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/registry.ts), and [src/agent/prompts.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/prompts.ts).

The task tool invokes first-party separately prompted explore or general subagents through a bounded model/tool loop; the batch runner limits concurrency and returns each result to the parent. Those mechanisms implement delegation and bounded concurrency, but no source-observed inter-S1 conflict arbitration over contending operational workspaces or distinct S1 commitments is demonstrated. The child action summaries are incorporated into parent feedback. See [src/tools/task.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/task.ts), [src/agent/task-pool.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/task-pool.ts), and [src/agent/task-runner.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/task-runner.ts).

Optional advisor mode calls a second configured model to produce plans/advice; an advisor tool gate can block writes and child tasks until consultation, followed by optional user plan approval. The advisory model receives a transcript and task context but is not shown independently inspecting operational reality or owning an organization-wide resource/control mandate. Separately, a configured goal judge evaluates the latest main-agent response, or a plan checklist if provided, and advises DONE/CONTINUE; it is explicitly an auxiliary fail-open continuation mechanism for an individual goal. The CLI mediates these paths and stores session state. See [src/agent/advisor.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/advisor.ts), [src/agent/advisor-gate.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/advisor-gate.ts), [src/agent/goal-loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/goal-loop.ts), and [src/cli/renderer.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/cli/renderer.ts).

Permissions (one action, session, or persisted project approval), mode gates, bash safeguards, goal/loop ceilings, project-validation command discovery and history/compaction are supporting or human-enforced local execution controls. The repository's own release/evaluation workflows are outside the installed coding organization's ownership boundary. See [src/permission/index.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/permission/index.ts), [src/agent/loop-guard.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/loop-guard.ts), [src/tools/project-validate.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/project-validate.ts), [src/session/manager.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/session/manager.ts), and [docs/advisor-executor-architecture.md](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/docs/advisor-executor-architecture.md) (design intent cross-checked against executable code).

## Operational model

The principal operational S1 is the model-guided coder working in the user's project; an explore/general child may carry out a delegated operational subtask, after which its tool/result messages return to the parent. Operational decisions and follow-up tool choices are model-guided, while fixed concurrency ceilings, permissions, tool validation and session recording are runtime enforcement. User approvals or cancellation are human decisions over local tool operations, not automatic evidence of separate S3 or S5 governance. Neither the agent count nor names such as advisor, supervisor, goal, plan, validation, or debug are sufficient VSM evidence without their function-specific decision and closure paths.

## S1 — Operations

- State: A
- Function: autonomously executes user coding/investigation work against a live local project through iterative model-selected tool actions.
- Disturbance / variety regulated: uncertain coding tasks, changing file state, command outcomes, tool failures, and user steering.
- Decisive decision or feedback right: select the next tool/action or final response after observing execution results.
- Decision owner: the configured model acting through Impulse's first-party AgentLoop; project user owns original intent and may enforce approval boundaries.
- Supporting / enforcement mechanisms: provider transport, mode-restricted tool registry, filesystem and bash tools, permissions, session messages, context compaction and loop limits.
- Closure path: user task → model call → chosen first-party code/file/shell tool execution → recorded tool result → next model decision or completion.
- Boundary reachability: the shipped CLI/TUI calls the Impulse AgentLoop and directly exposes first-party coding tools, without an external coding-agent process supplying the core loop.
- Why this is / is not agent-owned: absent model inference the runtime can only execute fixed mechanics and permissions, not select context-dependent coding steps; inference retains material action discretion.
- Evidence: [src/agent/loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/loop.ts); [src/tools/registry.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/registry.ts); [src/tools/file-edit.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/file-edit.ts); [src/tools/file-write.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/file-write.ts); [src/tools/bash.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/bash.ts); [src/cli/renderer.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/cli/renderer.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ownership is of operational coding decisions, not of permissions or user goals; source review is repository-relative, not a live performance benchmark.

## S2 — Coordination

- State: —
- Function: no supported, concrete relation is established that dampens interference or oscillation among distinct active S1 operational units.
- Disturbance / variety regulated: concurrent/delegated children could in principle contend for a file or task, but no implemented inter-S1 conflict witness and attenuation feedback is established in the reviewed distribution.
- Decisive decision or feedback right: the main agent delegates prompts; the batch runner caps/staggers concurrency, while approval covers launching certain children; these are scheduling/admission, not a conflict-specific coordination judgment.
- Decision owner: no established first-party S2-specific owner.
- Supporting / enforcement mechanisms: MAX_CONCURRENT_SUBAGENTS, task queue, batch permission, individual child loops, return of results to the parent.
- Closure path: parent requests subtask → runtime starts child → child result reaches parent; this is a delegation/result path, without evidence of a detected inter-S1 disturbance being attenuated.
- Why this is / is not agent-owned: model-selected delegation and a deterministic worker pool do not by themselves show S2 governance over conflicting S1 units.
- Evidence: [src/tools/task.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/task.ts); [src/agent/task-pool.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/task-pool.ts); [src/agent/task-runner.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/task-runner.ts); [src/agent/loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/loop.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: only the shipped task/permission/working-tree mechanisms were judged; custom extensions are outside the supported evidence boundary.

### Absence scope

- Surfaces inspected: parent tool loop, task launch schema, general/explore subagent tool loop, batch queue/stagger/concurrency/permissions, shared session and work-file access.
- Plausible first-party paths checked: cross-subagent write collision handling, conflict resolution or negotiated shared reservations, oscillation detection, and feedback modifying later behavior of separate S1 units.
- Why no material first-party path remains: the first-party task pool bounds simultaneous execution and aggregates results but does not supply a concrete conflict-responsive attenuation channel between independent operating S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no separately evidenced whole-current operational regulation of resources, commitments, priorities or accountability beyond the local coder and static execution limits.
- Disturbance / variety regulated: local tool failures, unfinished steps, repeated loops, incomplete task checklists, and optional advisor consultation.
- Decisive decision or feedback right: a local model chooses its next coding step; optional goal judge returns DONE/CONTINUE for one user goal, while user may approve a plan or tool action. None establishes whole-system current resource/commitment regulation.
- Decision owner: no identifiable current-organization S3 owner at the assessed recursion.
- Supporting / enforcement mechanisms: goal turn caps, task pool limit, loop guard, user permission/mode gates, persisted goal state and advisor input.
- Closure path: local monitoring/check-ins may guide the next coding turn, not decisions balancing multiple ongoing S1 commitments for the whole.
- Why this is / is not agent-owned: a model judging task completion or a runtime enforcing limits is not, without broader scope, whole-current management.
- Evidence: [src/agent/goal-loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/goal-loop.ts); [src/session/goal-state.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/session/goal-state.ts); [src/agent/loop-guard.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/loop-guard.ts); [src/agent/task-pool.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/task-pool.ts); [src/cli/renderer.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/cli/renderer.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: user-visible controls and advisor mode are included in the reviewed standard distribution; their task-local closure does not establish positive parent S3.

### Absence scope

- Surfaces inspected: AgentLoop, goal-state/judge/continuation, advisor and plan handoff, batch pool, CLI control/approval events, permission gates and persisted session.
- Plausible first-party paths checked: a whole-current view and discretionary cross-operation resource/priority/constraint choice with returned intervention; a legitimate parent mode with the same scope.
- Why no material first-party path remains: paths only constrain or continue an individual coding task, schedule child calls, or request human approval; no materially scoped whole-current management decision is implemented.

## S3* — Complementary audit

- State: —
- Function: no established complementary independently sourced audit of operational truth returning findings to current control.
- Disturbance / variety regulated: code changes and model claims may be mistaken; an independent check could contradict them, but an independent audit loop is not supplied as such.
- Decisive decision or feedback right: model can call project tools/tests and receive feedback; the auxiliary goal judge reads the last assistant answer and optional checklist, and the advisor reads supplied conversation rather than directly auditing the resultant workspace.
- Decision owner: no identified S3*-specific auditor with independent complementary access and corrective closure.
- Supporting / enforcement mechanisms: tool-result summaries, project_validate command detection, self-check nudges, optional judge/advisor and ordinary user-run tests.
- Closure path: ordinary tool/testing results can inform the same coding actor; no independently acquired complementary audit finding is demonstrated returning into current control.
- Why this is / is not agent-owned: a second model or deterministic validation hint does not automatically give complementary access to operational reality.
- Evidence: [src/tools/project-validate.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/tools/project-validate.ts); [src/agent/self-check.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/self-check.ts); [src/agent/goal-loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/goal-loop.ts); [src/agent/advisor.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/advisor.ts); [src/agent/loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/loop.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: optional manually configured independent external project CI might exist, but is not supplied as a first-party complementary audit closure by Impulse.

### Absence scope

- Surfaces inspected: project-validation tool, debug instrumentation scan, goal judge, advisor consultation, tool-result persistence, session and main loop.
- Plausible first-party paths checked: independent raw artifact probing or external-ground-truth checks controlled separately from the coder, finding-to-current-control feedback, and an audit owner with complementary access.
- Why no material first-party path remains: the shipped checks are ordinary current coder tools, prompts based on its transcript, or deterministic self-nudges; no separately realized audit-access/closure organization is shown.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented system-capability adaptation authority.
- Disturbance / variety regulated: future tools, models, environments, and user requirements could require changes to Impulse's enduring capabilities.
- Decisive decision or feedback right: advisor recommends a plan for the present task, web/search tools retrieve task evidence and session memory persists it; none chooses a prospective change to the harness's capacity.
- Decision owner: no first-party S4 agent or legitimate parent adaptation loop at the assessed system boundary.
- Supporting / enforcement mechanisms: strategic-named advisor, plan files, web tools, compacted context, project instructions and human model configuration.
- Closure path: advice and search results can influence the coder's present task; there is no evidenced external/future option → current-capability decision → subsequent operational adaptation cycle.
- Why this is / is not agent-owned: planning a coding action and remembering prior turns are not system-level outside-and-then adaptation.
- Evidence: [src/agent/advisor.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/advisor.ts); [src/agent/goal-loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/goal-loop.ts); [src/agent/prompts.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/prompts.ts); [src/session/manager.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/session/manager.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: experimental advisor configuration is reviewable but remains task-local.

### Absence scope

- Surfaces inspected: advisor architecture and implementation, planning/goal continuity, memory/compaction, web and model-selection tools, release-adjacent material excluded from runtime.
- Plausible first-party paths checked: prospective environment monitoring, development of adaptation alternatives and legitimate binding feedback changing the installed organization's future capabilities.
- Why no material first-party path remains: the supported runtime produces task guidance/continuation rather than an externally grounded prospective organizational adaptation closure.

## S5 — Policy and identity

- State: —
- Function: no shipped legitimate identity/ultimate-policy deliberation and authoritative return.
- Disturbance / variety regulated: permissions, user model/mode choices, scope boundaries and safety constraints concern ordinary actions.
- Decisive decision or feedback right: a human may approve or reject requested tools/plans, set permitted modes and configure permissions; this is local action authorization, not resolution of competing ultimate purposes.
- Decision owner: no function-specific S5 authority/return channel established inside the assessed Impulse organization.
- Supporting / enforcement mechanisms: once/session/always permission replies, advisor tool gate, PLAN→AGENT user handoff, prompts and CLI settings.
- Closure path: operator approval or setting changes affect the next tool/turn, not a higher-level identity-policy decision returned to settle S3/S4 tension.
- Why this is / is not agent-owned: enforcement or a human approval overlay is not by itself governing purpose/identity.
- Evidence: [src/permission/index.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/permission/index.ts); [src/agent/advisor-gate.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/advisor-gate.ts); [src/agent/plan-completion.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/plan-completion.ts); [src/agent/loop.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/agent/loop.ts); [src/cli/renderer.ts](https://github.com/spenceriam/impulse/blob/87f7019be3d73768baae8a1e330be436e1f167d4/src/cli/renderer.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a human operator may exercise external policy authority for their project, but no complete first-party S5 parent mode is evidenced for this coding runtime.

### Absence scope

- Surfaces inspected: installed permission policies, mode switching, advisor approvals, user session commands, prompts and config, release/development boundary.
- Plausible first-party paths checked: raising an actual purpose or enduring identity conflict to legitimate authority and returning a binding policy ruling to subsequent operation.
- Why no material first-party path remains: the implemented controls gate a tool, task or session choice without an identity/purpose-level governance issue and closure.

## Distributed OSS parent arrangement

Impulse is public OSS, but independent user installations are not a first-party organization-wide execution recursion. Maintainer workflows, contributions and release automation are development/distribution processes, not packaged supervisory, adaptation or identity actors for an individual coding session. The user may steer a local coding agent; this is not automatically S3=P, S4=P or S5=P.

## Self-hosted and non-human modes

The local CLI/TUI and its normal first-party tool/subagent loops are credited. Optional advisor-model, goal-judge, headless/noninteractive and human-approved tool modes do not create a separate eligible function-specific parent governance loop in source. Inference models and external MCP tools remain support/dependency surfaces.

## Recursion

The principal coding loop is an operational S1. General/explore subagents can become bounded operational children carrying out delegated work, but the pinned source does not demonstrate a coherent higher recursion with separate inter-S1 conflict regulation, whole-current management or full VSM metasystemic closure.

## Variety and escalation

Model-guided tool choice absorbs local task variety; tool failures, abort/steer injection, permission prompts and turn/concurrency caps regulate execution reliability. Permission denials and advisor-plan approval reach the interactive user at the local action boundary. Those signals alone do not create a higher organizational authority, S3* independent audit, S4 strategic adaptation or S5 governance.

## Evidence gaps

- Source-based classification of shipped paths, not empirical execution of the agent with live provider credentials.
- No independent runtime witness was located for inter-S1 collision attenuation or whole-current allocation despite implemented parallel subagent machinery; do not infer those functions from the concurrency cap.
- Optional third-party CI, custom tools and the user's own company governance are outside the pinned standard-distribution closure boundary, not evidence that such organizational functions are impossible in a composed system.
- The experimental advisor and separate goal judge were inspected as reachable conditional machinery, not treated as independent audits or prospective governance solely because of their names.
