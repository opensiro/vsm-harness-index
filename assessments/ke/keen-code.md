---
harness_id: keen-code
project_name: Keen Code
repository: https://github.com/mochow13/keen-code
review_ref: 8a3d495975ba5d90a6a86a9635b4478a346436bc
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Keen Code

## Review boundary

- System in focus: the first-party Keen Code terminal coding harness, its main agent loop and optional user-configured delegated subagents at frozen commit `8a3d495975ba5d90a6a86a9635b4478a346436bc` (release v0.57.1).
- Purpose and identity: help a user inspect and change project files by selecting model-directed tools, using local context, configurable providers/skills/MCP and optionally delegated specialist workers.
- Relevant environment: user instructions, files and git state, streaming model replies, tool results/errors, permissions, concurrent delegated children, local context and session events.
- Standard-distribution boundary: Go CLI and Bubble Tea REPL, first-party provider/model tool loop, filesystem guard, `delegate_task` parallel barrier over separately model-backed user-supplied agent profiles and local session/permission machinery.
- Credited operating / distribution surfaces: `internal/cli/repl/`, `internal/agentcore/`, `internal/llm/`, `internal/tools/`, `internal/subagents/`, `internal/filesystem/`, `internal/session/` and shipped docs/permission settings.
- Adjacent first-party surfaces excluded from ownership: documentation-only example `explorer`, `implementer`, `test-designer`, `reviewer` profiles and model prompts, external MCP/LLM providers, external worktree/CI/QA orchestrators, source Go tests and the upstream maintainer organization.
- Reviewed modes: interactive main model coding, plan/build permission modes, model-chosen parallel `delegate_task` with user-authored role profiles, optional skills/MCP/memory, queued follow-up user input and side question (`/btw`) without tools.
- Recursion level: a current Keen Code coding session and optionally its bounded delegated children, not a project management organization or multiple unrelated sessions.
- License screen: checked-in frozen `LICENSE` is MIT, also reported as MIT by the repository; eligible for public-source assessment.
- Observation date: 2026-10-23; Profile `0.2.4`; Methodology `0.3.7`.

## Repository architecture

The interactive REPL streams a model's tool calls and executes them through Go tool implementations. Main-thread operational choices follow user intent and tool observations. The session store reconstructs context from events. `delegate_task` accepts one to ten assignments referencing **user-defined** named subagent profiles and starts independent model runs concurrently via a `SubagentRunner`. A `sync.WaitGroup` barrier returns ordered results and per-task errors after *all* children finish. Children have their own system prompts/model choices and tools, cannot recursively delegate, and inherit or receive explicit profile permissions. This is real S1 delegation with feedback to the parent, not simply a tool alias.

The multi-agent design explicitly does **not** enforce dependencies, shared write-file ownership, isolated worktrees, inter-agent scheduling, cross-child budgeting or transactional integration. All writable children can operate on a shared working directory. The document's partition, independent review, verification and staged integration recipes require external user-authored profiles or workflow prompts and are not shipped organizational mechanisms.

The TUI shows compact per-child tool activity; one `delegate_task` blocks the main model until all its children settle. Parent cancellation can stop the whole outstanding call, and a follow-up user-message queue serializes later input, but no persistent whole-cohort controller with a selectable current commitment/resource intervention is exposed. The user may grant per-action permission, but this is not a live S5 identity council. The external provider catalog, skills, plans and memory serve present coding tasks, without an evidenced prospective research-to-capability redesign control loop.

Frozen sources: [`docs/architecture.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/architecture.md), [`docs/subagents.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/subagents.md), [`docs/multi-agent-orchestration.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/multi-agent-orchestration.md), [`internal/tools/delegate_tool.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/tools/delegate_tool.go), [`internal/subagents/runner.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/subagents/runner.go).

## Operational model

The current model has genuine operational discretion through the main tool loop; independently instantiated children also make S1 choices (S1=A). The delegate barrier collects child outcomes but **does not** regulate conflicting child operations; that coordination remains a task-design responsibility (S2=—). Neither the parent model's decomposition/integration nor the human's ordinary permissions, queue and whole-turn cancellation demonstrate present whole-cohort S3 control. Review profiles are not bundled, and tests are normal validation rather than independent S3* audit. No first-party S4 or S5 closure was evidenced.

## S1 — Operations

- State: A
- Function: inspect, modify and test local project content through model-selected tool actions, with optional independently acting child coding/research agents.
- Disturbance / variety regulated: changing source files, unfamiliar project structure, compiler or command failures, provider tool results, user requirements and child-agent discoveries.
- Decisive decision or feedback right: each model-based main or delegated child can select which exposed tool to invoke next, adjust approach from returned results and decide the final task reply.
- Decision owner: first-party main model-backed actor, or an independently instantiated model-backed subagent for a delegated assignment.
- Supporting / enforcement mechanisms: provider adapter `StreamChat`, core tool registry, permission requester, file guards, session event store and bounded subagent runner.
- Closure path: REPL user message → model and registry → selected tool executes → outcome re-enters current model's context → next decision/completion; delegated child's terminal result re-enters the parent after the barrier.
- Boundary reachability: the shipped REPL creates the main agent/tool loop and registers the first-party delegate tool when discoverable profiles exist; `RunDelegate` constructs actual independent child model execution.
- Why this is / is not agent-owned: tools and guards enforce physical effects, while each model decides adaptive task actions based on current feedback.
- Evidence: [`docs/architecture.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/architecture.md), [`internal/agentcore/agentcore.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/agentcore/agentcore.go), [`internal/tools/delegate_tool.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/tools/delegate_tool.go), [`internal/subagents/runner.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/subagents/runner.go).
- Basis: first-party frozen source and scripted fake/mock-based tests, **no live LLM-agent evaluation**.
- Confidence: high for the execution and delegation path, not measured code-quality or success rates.
- Caveats: delegating requires the operator to create suitable role files; example profiles in docs are not a bundled default team and do not grant autonomous control ownership.

## S2 — Coordination

- State: —
- Function: no first-party interference-damping relation among distinct concurrent S1 agents was established.
- Disturbance / variety regulated: separate write-capable children can edit the same files, collide in shared state or produce mutually incompatible outputs.
- Decisive decision or feedback right: one model may propose assignment partitions; Go launches up to ten independent children and joins their results, without a demonstrated inter-worker collision detection/negotiation/enforcement right.
- Decision owner: no S2 owner established. Delegation choices belong to S1 parent task decomposition, not a coordinating runtime with interference closure.
- Supporting / enforcement mechanisms: `delegate_task` task-count cap, concurrent `RunDelegate` calls, profile capability permissions, read/write guard and ordered result aggregation.
- Closure path: a parent initiates concurrent children → individual task results/errors return after a barrier → the parent continues its own task; no enforced inter-S1 conflict attenuation before or during shared writes.
- Why this is / is not agent-owned: launching and joining subagents is orchestration plumbing; external instructions may urge disjoint file ownership, but runtime neither checks nor protects it.
- Evidence: [`internal/tools/delegate_tool.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/tools/delegate_tool.go), [`docs/subagents.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/subagents.md), [`docs/multi-agent-orchestration.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/multi-agent-orchestration.md).
- Basis: direct negative first-party design disclosure corroborated by source inspection and scripted delegate/mock tests.
- Confidence: high at the current frozen ref.
- Caveats: a custom external orchestrator may coordinate work; the present assessment excludes unshipped user workflows.

### Absence scope

- Surfaces inspected: `delegate_task`, child runner, profile permissions, live activity/backpressure, task-result barrier, session queue and multi-agent design documentation.
- Plausible first-party paths checked: ordered results as coordination, static ten-task cap as interference control, channel backpressure as inter-agent regulation, shared directory guard as file ownership, user-written instructions as runtime enforcement.
- Why no material first-party path remains: there is no first-party shared-file conflict guard, worktree partition, cross-worker resource negotiation, workload reassignment or other demonstrated operational feedback that attenuates disturbances among separately deciding children.

## S3 — Inside-and-now control

- State: —
- Function: no accessible whole-current view and selective multi-agent resource/priority/commitment controller across the local operational cohort was established.
- Disturbance / variety regulated: a set of children can race, spend resources inefficiently or require reassignment when an individual worker stalls.
- Decisive decision or feedback right: the parent assigns tasks and waits; the human can cancel the parent turn or respond to a tool approval. Neither is evidenced dynamically selecting an intervention from a whole-current per-worker management state.
- Decision owner: none established for S3; main model's ordinary task decomposition and human permissions remain S1-level/outer controls.
- Supporting / enforcement mechanisms: task barrier, timeout per profile, compact per-child tool activity, parent-context cancellation, input queue and project instructions.
- Closure path: `delegate_task` joins all child results and returns them to the originating parent model; no live whole-cohort diagnosis → selective reprioritization/resource revision/cancel of specific active children → operating return is shipped.
- Why this is / is not agent-owned: a parent actor aggregating completed work is not by itself a current operations manager with authority over shared commitments.
- Evidence: [`internal/tools/delegate_tool.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/tools/delegate_tool.go), [`docs/subagents.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/subagents.md), [`docs/queuing.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/queuing.md).
- Basis: bounded negative source review and explicit first-party scope statement.
- Confidence: medium-high.
- Caveats: an external supervisor could implement the missing current-control loop, but such a supervisor is not part of Keen Code's first-party distribution.

### Absence scope

- Surfaces inspected: interactive child activity, main and child cancellation, per-profile timeouts, result barrier, prompt-guided task decomposition and queued user messages.
- Plausible first-party paths checked: parent-as-manager, activity log as current system view, user cancellation as targeted S3 intervention, profile timeouts as budget bargaining, input queue as operations scheduler.
- Why no material first-party path remains: current child activity is not a management roster with per-child decisive intervention; task results arrive after barrier; cancellation propagates to the outstanding call as a whole and limits are fixed execution constraints.

## S3* — Complementary audit

- State: —
- Function: no independently initiated/accessed reviewer of S1 performance with findings returned to accountable S3 management was demonstrated.
- Disturbance / variety regulated: model-generated patches and claimed tests can be wrong, but that failure potential is not an audit function on its own.
- Decisive decision or feedback right: a user can write and invoke a `reviewer` profile, or the parent can choose tests; the built-in distribution supplies neither the reviewer profile nor an autonomous mandatory audit authority.
- Decision owner: none established as complementary auditor within the first-party harness; optional reviewer children would act on parent-supplied S1 tasks.
- Supporting / enforcement mechanisms: profile discovery and child prompts, optional `delegate_task` with permissions, source tests, tool failures and session records.
- Closure path: when configured, a reviewer would return a task result to the same parent model; no independent audit trigger, alternate access independence guarantee and S3 corrective disposition channel is wired by default.
- Why this is / is not agent-owned: example reviewer prompts and ordinary test tool outputs cannot be counted as a live first-party independent audit circuit.
- Evidence: [`docs/multi-agent-orchestration.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/multi-agent-orchestration.md), [`internal/subagents/discover.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/subagents/discover.go), [`internal/tools/delegate_tool.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/tools/delegate_tool.go).
- Basis: negative review against explicitly non-bundled workflow examples.
- Confidence: high for default distribution; custom downstream extensions are unassessed.
- Caveats: independent review could be configured separately, but requires evidence of concrete boundary reachability and corrective return before a positive S3* state.

### Absence scope

- Surfaces inspected: subagent role discovery, prompts, optional reviewer example, Go unit tests, model result aggregation and TUI tool-activity reporting.
- Plausible first-party paths checked: reviewer example as mandatory S3*, model verification as independent audit, approval requester as audit, test results as complementary reporting.
- Why no material first-party path remains: all review is optional user-authored production activity without evidenced sufficiently independent access, adjudication and return to a separately accountable S3 manager.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped prospective outside-environment analysis that develops options and changes present operating capability through S3 dialogue.
- Disturbance / variety regulated: future task demand, external tools/models and emerging constraints could require capability adaptation beyond current coding requests.
- Decisive decision or feedback right: present-task agent can fetch web/MCP materials or use memory/skills and planning, while humans/maintainers choose future harness changes.
- Decision owner: none established for a prospective S4 function at this local-session recursion.
- Supporting / enforcement mechanisms: web fetch/MCP access, provider catalog, user-loaded skills, task memory, compaction and exploratory subagents.
- Closure path: a tool result can guide the current task and a user-authored skill may be loaded later; no built-in external trend sensing → adaptation alternatives → update to current S3 capability is evidenced.
- Why this is / is not agent-owned: optional general-purpose research and configuration are means for present S1 tasks rather than organizational strategic intelligence.
- Evidence: [`docs/skills-system.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/skills-system.md), [`docs/architecture.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/architecture.md), [`docs/memory.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/memory.md).
- Basis: bounded first-party design/source inspection.
- Confidence: medium.
- Caveats: a user could build a future-watching skill, which this first-party evidence does not show running or governing adaptation.

### Absence scope

- Surfaces inspected: web/MCP tools, skills, provider registry, model memory, planning and example multi-agent research workflows.
- Plausible first-party paths checked: external web fetch as horizon scanning, persistent memory as capability redesign, provider catalog refresh as S4, generic plan agents as prospective management.
- Why no material first-party path remains: no first-party closed process generates future-relevant strategic options and negotiates resulting changes with current whole-cohort control.

## S5 — Policy and identity

- State: —
- Function: no demonstrated legitimate ultimate-policy or system-identity authority inside the assessed coding-session organization.
- Disturbance / variety regulated: unsafe tool actions and sensitive filesystem paths are constrained operationally, but do not by themselves address identity/purpose conflicts.
- Decisive decision or feedback right: a human can approve/deny commands and set modes or role permissions; implementation supplies deterministic hard filesystem guards. None exercises a constitutional choice with S3/S4 return.
- Decision owner: no first-party S5 actor established at the local coding-session boundary.
- Supporting / enforcement mechanisms: `PermissionRequester`, interactive modal, filesystem guard, profile permissions and restricted child nested delegation.
- Closure path: tool request → static guard / user permission → individual operation allowed or denied; no S5-level identity proposal → legitimate authority → durable organizational operating-policy return.
- Why this is / is not agent-owned: action approvals and developer configuration are safety enforcement rather than legitimate system identity governance.
- Evidence: [`docs/permission-system.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/permission-system.md), [`internal/filesystem/guard.go`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/internal/filesystem/guard.go), [`docs/subagents.md`](https://github.com/mochow13/keen-code/blob/8a3d495975ba5d90a6a86a9635b4478a346436bc/docs/subagents.md).
- Basis: explicit permission semantics, first-party operating boundary.
- Confidence: medium-high.
- Caveats: external organizational policies can bind an installation but are not proven as a shipped Keen Code S5 return.

### Absence scope

- Surfaces inspected: user approval prompts, child capability profiles, blocked path guard, local project instructions, provider configuration and maintainers' distribution boundary.
- Plausible first-party paths checked: human permission as S5, safety rules as identity code, `AGENTS.md` as legitimate policy council, provider registry as strategic mandate.
- Why no material first-party path remains: these constrain or route specific operations without a legitimate in-boundary ultimate identity decision and balancing return into S3/S4.

## Distributed OSS parent arrangement

The upstream project organization, example multi-agent orchestration documents and user-maintained project instructions are outside the assessed session's first-party S3–S5 control recursion. Unlike a shipped organizational manager, the repository's example workflow needs a user to create each named subagent profile and define ownership/review rules.

## Self-hosted and non-human modes

The usual attended REPL can operate with a single main S1, or invoke user-defined children through `delegate_task`. Children are independently model-backed but approval-free for tools their profiles expose, and share a project working directory; parallel writes therefore require caution. The `/btw` side-channel explicitly cannot call tools, and queued user inputs are delivered serially to the main thread, so neither constitutes an additional self-managing operational unit. An externally automated deployment could wrap the CLI, but no organizational autonomy is credited without its actual first-party closure.

## Recursion

At the local project session recursion, a main agent is S1 and, when configured, each delegated child is its own bounded S1. A parallel task barrier is not a higher level of viable management without interference attenuation or resource-intervention rights. The user's project workflow and the upstream maintainer organization are distinct recursions not silently included.

## Variety and escalation

Each child reports its completion/errors to the parent; sibling failures do not automatically cancel the other workers. Parent-initiated task cancellation interrupts a whole outstanding batch, not an individually chosen intervention based on a live global roster. Concurrent-write conflicts, budget tradeoffs and independent audits remain matters for user instructions and later parent-task decisions, rather than closed first-party S2/S3/S3* functions.

## Evidence gaps

- No live LLM-agent evaluation and no measured task-success or multi-agent coordination outcomes; only deterministic script/Go tests are permissible for this batch.
- The frozen source explicitly disclaims first-party worktree isolation, file ownership and execution-budget control; no implied capabilities from documentation-only example subagents were credited.
- Automatically approved subagent Bash/MCP tools are a permission-risk distinction, not an S2/S5 positive mapping.
- A future revision or downstream configured team could exhibit additional functions, but is not evidence at frozen commit `8a3d495975ba5d90a6a86a9635b4478a346436bc`.
