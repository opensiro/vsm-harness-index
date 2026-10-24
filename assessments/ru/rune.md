---
harness_id: rune
project_name: Rune
repository: https://github.com/khang859/rune
review_ref: afefbad9f8f4a7818a6defc4165f4a0c6aeacdad
reviewed_at: 2026-10-21
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-21
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Rune

**Proposed, noncanonical assessment:** candidate inclusion based on source-evidenced first-party coding agent operation. Frozen intake [#860](https://github.com/opensiro/vsm-harness-index/issues/860), serial batch [#1842](https://github.com/opensiro/vsm-harness-index/issues/1842), row 3. This assesses the pinned Go source distribution, not externally observed task success. Proposed vector **S1=A / S2=C / S3=— / S3*=— / S4=— / S5=—**; the S2 construction is limited to shared subagent execution capacity, not inter-agent strategic negotiation.

## Review boundary

- System in focus: Rune's standalone terminal/headless Go coding-agent program, installed model-to-tool feedback loop, optional model-directed subagent execution and first-party session state.
- Purpose and identity: Answer software-development requests, inspect and modify a chosen codebase, test or research it with an agent-controlled sequence of file/shell/search and optional MCP actions.
- Relevant environment: User prompts and interventions, local repository/files, code/test results, configured model providers, external MCP and search endpoints, host resource capacity, custom skills and agent definitions.
- Standard-distribution boundary: Runnable cmd/rune client and internal/agent, internal/tools, internal/ai, internal/session, internal/config, internal/agentdef and TUI provided by the pinned Go repository; interactive, one-shot/script, plan/act and configured subagent modes, excluding uninstalled future extensions.
- Credited operating / distribution surfaces: cmd/rune run wiring, first-party agent loop, registered read/write/edit/bash/search tools, bounded subagent supervisor with task lifecycle and dependency/slot return, session persistence, explicit Plan Mode tool registry.
- Adjacent first-party surfaces excluded from ownership: Documentation-only future designs and feature plans, evaluation/benchmark scripts, repository contributor governance and CI, tests as operators, uninvoked external provider logic, external agent runtimes and arbitrary user-installed skills, MCP servers or custom agents not shipped as the standard decision owner.
- First-party operating / deployment modes considered: interactive TUI, one-shot/scripted headless coding, Plan/Act mode with registry enforcement, optional single-parent parallel subagents and restored local sessions.
- Recursion level: one local Rune-assisted coding workflow with executable S1 cells, including independently model-driven child tasks in a selected parent session. Nested processes do not create separately demonstrated viable enterprises.
- Reviewed revision: [khang859/rune@afefbad9f8f4a7818a6defc4165f4a0c6aeacdad](https://github.com/khang859/rune/tree/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad)
- Observation date: 2026-10-21
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The shipped [architecture](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/docs/architecture.md) traces cmd/rune to a Bubble Tea UI and an internal/agent loop. [Agent.Run ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/loop.go) appends a user message, streams an external model provider with first-party registered tool specifications, executes model-selected calls and returns tool observations into later steps. The tool [Registry ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/tools/tool.go) filters Plan Mode tools at specification and execution time; write/edit/bash and untrusted MCP effects are denied by default in that mode. Session trees and compacted history are first-party persisted; separate provider API and OAuth transport are dependencies, not management.

A [SubagentSupervisor ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/subagents.go) creates distinct model-driven child task sessions, enforces a configurable concurrency semaphore, records statuses/results, gates explicitly dependent follow-on child tasks, propagates cancellation/failure and injects completed child summaries to the parent loop. Read-only child registries are standard; explicitly configured full-tool children may be allowed to edit. User-selected task dependencies and typed agent definitions remain settings, not evidence of an autonomous inter-agent executive. [Subagent tests ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/subagents_test.go) include blocked/dependency completion, failed dependency propagation, status transitions and capacity settings. These tests were inspected but not executed.

A standalone [README](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/README.md) documents interactive, one-shot and script modes, provider selection, skill loading and Plan Mode. The installed [session tree ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/session/session.go) supports branch/fork, message persistence and summary memory. No first-party self-modification/adopted future agent policy has been established from session compaction or skill authoring alone. No actual model task run or Go test execution is claimed: the inspection environment lacks a Go toolchain.

## Operational model

The operator configures provider and top-level task; the shipped agent selects a sequence of tool operations in response to observations. A parent may request multiple child tasks; each child owns its individual open-ended work loop, while the first-party supervisor owns deterministic admission to a finite number of child execution slots and returns completed/dependency results. The operator may authorize a plan or configured side effects. No source evidence attributes whole-portfolio current management, a complementary independent auditor, prospective adopted adaptation or ultimate organizational policy decisions to those mechanisms.

## S1 — Operations

- State: A
- Function: Execute a model-guided coding task with real tool and codebase feedback.
- Disturbance / variety regulated: Open-ended requirements, unknown project files, failed commands/tests, context limits, variable model/tool responses and discovered code defects.
- Decisive decision or feedback right: Choose next file/search/edit/shell/MCP tool call and follow-up based on prior observation; produce or revise coding output.
- Decision owner: Model-directed Rune agent session via installed first-party loop, within mode/tool policy selected by an operator; an external provider supplies inference rather than a separate first-party S3 owner.
- Supporting / enforcement mechanisms: ai.Provider stream, Registry tool selection and execution, retry/compaction, typed session history, Plan Mode permissions, TUI/headless entrypoints.
- Closure path: User request → Rune agent provider request → model-selected tool → first-party executed result → observed result in session history → subsequent model step or final answer.
- Boundary reachability: Shipped [loop ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/loop.go) and [agent constructor ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/agent.go) implement an actual reachable model-to-tool feedback path, with [tool registry ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/tools/tool.go), not a role-only prompt pack.
- Why this is / is not agent-owned: Removing the agent's model-directed next-action choice leaves tools and fixed policies but no open-ended coding solution. Human top-level task authorization does not decide intermediate tool semantics.
- Evidence: [agent loop ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/loop.go); [agent ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/agent.go); [tool registry ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/tools/tool.go); [README](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/README.md).
- Basis: explicit and structural
- Confidence: high for first-party reachable operating loop; no live performance validation
- Caveats: Requires an available model provider. Plan Mode deliberately limits tools until changed by the user.

## S2 — Coordination

- State: C
- Function: Attenuate interference between concurrently requested child S1 work cells competing for a common finite executable-agent capacity, and return waiting/dependent work after capacity or prerequisite results become available.
- Disturbance / variety regulated: Unbounded parallel children would overcommit one parent's local child-execution budget, while dependent children that start before prerequisite outputs would operate with missing task context.
- Decisive decision or feedback right: Admit at most MaxConcurrent children to active execution, make another wait for a slot, unblock dependent work only when its declared prerequisites complete, propagate failed dependencies, and pass completion summaries to subsequent tasks.
- Decision owner: Deterministic first-party SubagentSupervisor semaphore/dependency state, not a separate model making coordinating choices; therefore C rather than A.
- Supporting / enforcement mechanisms: buffered concurrency semaphore, task state map, explicit dependency set, lifecycle events, completion signals, persisted child records, user/model authored task dependencies and child execution cancellation.
- Closure path: Two or more model-guided children contend for configured slots → one obtains the final semaphore slot, another waits → completion releases capacity → waiting model/tool child starts; a dependent child remains blocked until prerequisites complete and then receives their summaries as input. Failed prerequisites explicitly prevent that child from executing.
- Boundary reachability: [SubagentSupervisor ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/subagents.go) is instantiated by [NewWithSubagentConfig ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/agent.go) and wired to runtime [subagent tool registration ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/tools/subagents.go). It executes child Run loops and returns outcomes; not a hypothetical extension.
- Why this is / is not agent-owned: S2-specific construction regulates competing execution attempts for the same shared resource and closes back to the waiting child; model agents do not own the fixed slot-allocation policy. Dependency scheduling alone would not establish S2 absent this actual resource-contention return.
- Evidence: [subagent supervisor ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/subagents.go); [subagent tests ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/subagents_test.go); [agent constructor ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/agent.go); [tools ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/tools/subagents.go).
- Basis: structural, with source-level tests documenting lifecycle and dependency return
- Confidence: moderate; contention logic is executable but a runtime concurrency experiment was not performed
- Caveats: Scoped to finite child execution capacity in one parent, not inter-agent file-collision resolution, organizational priority arbitration, negotiated cooperation or standalone distributed S2 authority.
- Distinct S1 units: Independent subordinate Rune Agent instances with their own session/model/tool loops inside one parent coding task.
- Inter-S1 disturbance: Concurrent child starts contend for a shared configured process/model-call concurrency budget; overcommit would interfere with other live children and their parent.
- Attenuating coordination relation: Shared MaxConcurrent semaphore plus blocked/pending/running state machine for prerequisites; no queued task is activated before a slot/prerequisite becomes eligible.
- Feedback into subsequent S1 behaviour: Slot release runs the deferred child task; terminal dependency resolution starts eligible children with prerequisite completion summaries or fails them closed when prerequisites fail.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A concrete capacity-conflict attenuation with a released-slot execution return is implemented for independently operating S1 cells; simple spawn/status metadata or a shared task list would not provide that closure.

## S3 — Inside-and-now control

- State: —
- Function: No demonstrated owner of whole-current coding-organization resource and commitment management at the declared recursion.
- Disturbance / variety regulated: Aggregate task backlog, changing code priorities, human approvals, cumulative context/token costs, child failures.
- Decisive decision or feedback right: View the entire running organization, revise shared operational priorities/resources/accountability and return interventions across current S1 units.
- Decision owner: Not established. Operator selects work and policies, model plans its own task, supervisor enforces a fixed child limit; none is evidenced as a global current executive.
- Supporting / enforcement mechanisms: Per-task subagent tracking, concurrency semaphore, TUI session view, provider/model preferences, Plan Mode restrictions, token accounting.
- Closure path: Task-level status/permission and deterministic child gating return into individual work; an independent whole-current decision over competing commitments that changes later S1 priorities was not identified.
- Boundary reachability: No positive S3 claimed; supported main/child/session controls were reviewed rather than promoted from manager-like names.
- Why this is / is not agent-owned: Capacity semaphore and user plan approval implement local execution constraints, not a decisive whole-system current managerial loop.
- Evidence: [subagents ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/subagents.go); [agent ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/agent.go); [session ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/session/session.go); [architecture](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/docs/architecture.md).
- Basis: bounded source review
- Confidence: moderate
- Caveats: No enterprise-wide deployed system is inferred from the embeddable CLI.

### Absence scope

- Surfaces inspected: Main loop, session state, subagent supervision/dependencies, read-only/full tool modes, Plan/Act modes and shipped operator UI architecture.
- Plausible first-party paths checked: Parent agent managing child work, global backlog/priority choices, concurrency/resource reallocation, budget and failure escalation, parent operator steering and continuation.
- Why no material first-party path remains: Observed decisions are one-task planning, deterministic child admission/dependency processing and human-selected settings. No installed organizational controller with a whole-current view, distinct decisive resource/commitment tradeoff and return to multiple S1 units is evidenced.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent complementary access and corrective audit loop challenging a standing S3 manager's operational account.
- Disturbance / variety regulated: Agent misunderstandings, incorrect code, unverified completion or misleading execution summaries.
- Decisive decision or feedback right: Independently inspect operating reality beyond routine reporting and return findings to an S3 corrective decision.
- Decision owner: Not established in the shipped agent runtime.
- Supporting / enforcement mechanisms: Code-reviewer/validator child templates, tool output, git status/diff, session messages, read-only child registry and tests.
- Closure path: A child reviewer can report findings to its parent task; this is delegated task-level quality assurance, not an evidenced independent audit-to-whole-current-management intervention.
- Boundary reachability: No positive audit channel credited; builtin review subagents are reachable but functionally ordinary S1 task support.
- Why this is / is not agent-owned: A different named reviewer or read-only execution surface does not by itself establish independent organizational audit authority.
- Evidence: [subagents ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/subagents.go); [agent definitions ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agentdef/agentdef.go); [subagent documentation](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/docs/subagents.md); [session ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/session/session.go).
- Basis: structural
- Confidence: moderate
- Caveats: A human can design a complementary audit with custom roles; this is not a shipped standing VSM S3* path.

### Absence scope

- Surfaces inspected: Shipped builtin review subagents, parent-child reports, repo read-only tools, test and verification design, session state.
- Plausible first-party paths checked: Independent evidence acquisition, challenged ordinary agent reporting, distinct auditor judgment and feedback to a whole-current controller.
- Why no material first-party path remains: Review helpers inspect individual task outputs, with no independent S3 audit mandate/owner and no managerial corrective return in the standard distribution.

## S4 — Outside-and-then intelligence

- State: —
- Function: No closed prospective external-environment intelligence/adaptation selection into future Rune organizational capability in the shipped product.
- Disturbance / variety regulated: New coding environments/providers, recurring failures, future task demands, model/tool capability changes.
- Decisive decision or feedback right: Compare forward conditions and select/implement a durable future operating adaptation returned to current organizational capability.
- Decision owner: Not established. User controls provider, skill/agent definitions and run mode; model plans current work.
- Supporting / enforcement mechanisms: Session branching/compaction, repo map and memory loading, editable markdown skills/agents, model switch and optional web search.
- Closure path: Prior messages and memory influence later context, but no first-party closed outside-and-then option judgment followed by authorized durable capability change is evidenced.
- Boundary reachability: No positive S4 claim; user-created future adaptation skill is an adjacent configurable possibility.
- Why this is / is not agent-owned: Retaining session history or synthesizing a plan is not selecting and adopting a change to the harness's future capabilities.
- Evidence: [session ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/session/session.go); [memory ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/memory/memory.go); [skills ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/skill/skill.go); [loop ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/loop.go).
- Basis: bounded source review
- Confidence: moderate-high
- Caveats: Source assessment does not exclude downstream adopters building such functionality.

### Absence scope

- Surfaces inspected: Compaction/session state, repo-map, built-in planning/skills, custom agents, provider configuration and agent loop.
- Plausible first-party paths checked: External trend/input to future options, prospective adaptation decision, durable revision to installed tool/agent capability, subsequent reuse.
- Why no material first-party path remains: No wired first-party future-intelligence selector/adoption/return exists in examined shipped modes; editable skill files and provider settings are operator inputs rather than adaptive feedback closure.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate-identity/purpose authority returning organizational policy revisions into an ongoing agent organization.
- Disturbance / variety regulated: Disagreement between agent requests and governing purpose/authority over permissible organizational acts.
- Decisive decision or feedback right: Define or revise ultimate purpose/identity/authority for Rune and return the chosen policy to later operation.
- Decision owner: Not established; operator provides credentials, tasks and permitted tool mode. Deterministic Registry enforces tool permissions.
- Supporting / enforcement mechanisms: Deny-by-default Plan Mode, tool allowlists, local user configuration, custom role files, plan approval and provider authentication.
- Closure path: Human selection of Act/Plan mode changes tool availability, but no separately evidenced first-party identity/policy deliberation, adjudication and canonical return loop appears.
- Boundary reachability: No positive S5 credited; generic operator preferences are not promoted to parent S5 authority.
- Why this is / is not agent-owned: Safety gating and human sign-off on a task plan are operational constraints, not whole-organizational identity/ultimate-policy governance.
- Evidence: [tool permissions ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/tools/tool.go); [architecture](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/docs/architecture.md); [agent ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/agent/agent.go); [settings ](https://github.com/khang859/rune/blob/afefbad9f8f4a7818a6defc4165f4a0c6aeacdad/internal/config/settings.go).
- Basis: bounded source review
- Confidence: moderate
- Caveats: A particular adopter may impose a parent organizational identity externally; that owner is outside this shipped first-party distribution.

### Absence scope

- Surfaces inspected: Tool authorization/Plan Mode, provider auth, operator-configured settings, agent definitions, runtime tasks and contributor governance as adjacent evidence.
- Plausible first-party paths checked: Legitimating a higher-level purpose/identity choice and returning accepted organizational policy to operating units; first-party parent mode with an explicit authorization/return relation.
- Why no material first-party path remains: Rune exposes tool/mode restrictions and user-defined roles but no separate shipped S5-specific decision and feedback channel at this recursion.

## Distributed OSS parent arrangement

This is a local self-hosted coding-agent installation with an operator-selected task boundary, not a collective OSS governance organization. The repository's contributors, CI and users are outside the credited installed runtime organization. Custom skills, externally supplied models and ad hoc manual review cannot be silently counted as first-party higher-level VSM owners.

## Self-hosted and non-human modes

Rune has autonomous intermediate coding choices conditional on a configured inference provider and user-gated tool permissions. Concurrent child cells share one parent and deterministic budget/dependency control; no separate autonomous executive, independent corrective auditor, foresight adopter or organization-level policy owner is evidenced. A human owns task and authorization choices, but task approvals alone do not create first-party S3/S4/S5 parent modes.

## Recursion

A Rune parent session may spawn independent child coding loops, but their process hierarchy does not establish recursively viable policy/strategy organizations. The one assessed operating boundary remains the installed coding workflow.

## Variety and escalation

Agent/tool errors and context limits are fed back to the local model loop; dependency failure cancels downstream child work; concurrency saturation defers another child until resources free. Human plan approvals and custom tool configuration constrain the action space. No algedonic channel, independent audit or institution-level authority is inferred from status labels.

## Evidence gaps

- S2 is source-level and limited to shared finite child capacity, not proof of enterprise coordination or runtime performance.
- No model-provider live experiment or Go test run was performed; the inspection machine lacked Go.
- No default independent semantic reviewer was invoked; acceptance remains governed by the Index proposal/CI and separate canonical-admission process.
- A new repository revision or custom workflow could provide different VSM functions but would require a separately pinned reassessment.
