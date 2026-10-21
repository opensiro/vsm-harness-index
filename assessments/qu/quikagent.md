---
harness_id: quikagent
project_name: QuikAgent
repository: https://github.com/shaneburrell/quikagent
review_ref: d5851f84de2354f42b555367efaa339feaa46765
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# QuikAgent

**Canonical general VSM assessment** for [batch #1842](https://github.com/opensiro/vsm-harness-index/issues/1842), row 7, frozen intake [#860](https://github.com/opensiro/vsm-harness-index/issues/860). Evidence-bounded vector `A / C / — / — / — / —`, not performance or deployment attestation.

## Review boundary

- System in focus: Installed first-party Go QuikAgent model/tool coding assistant with optional structured plan-step orchestration.
- Purpose and identity: Work on operator-requested source-code changes within one configured repository/workspace, using model/tool calls and optional parallel child task execution.
- Relevant environment: Local filesystem and terminal, OpenAI-compatible provider, optional router/MCP/extensions, local JSONL sessions, TUI/print/loopback web interfaces.
- Standard-distribution boundary: Executable and shipped first-party model/tool loop, plan handoff, wave coordinator, subagents, permissions and session/tool configuration at exact frozen commit.
- Credited operating / distribution surfaces: [cmd/quikagent/main.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/cmd/quikagent/main.go), [internal/agent/agent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/agent.go), [internal/agent/orchestrate.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/orchestrate.go), [internal/agent/subagent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/subagent.go), [internal/tools/plan.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/plan.go), [internal/tools/permissions.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/permissions.go), [internal/session/session.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/session/session.go), [internal/session/plan.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/session/plan.go), [internal/server/server.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/server/server.go).
- Adjacent first-party surfaces excluded from ownership: [docs/design/README.md](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/docs/design/README.md), [deploy/harvester/quikagent-lab.yaml](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/deploy/harvester/quikagent-lab.yaml), [.github/workflows/ci.yml](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/.github/workflows/ci.yml), [docs/REVIEW_DISPOSITIONS.md](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/docs/REVIEW_DISPOSITIONS.md); proposed daemon/jobs/projects, release/CI, lab VM, maintainer security issue dispositions and third-party provider intelligence are not bundled higher-function organizational owners.
- First-party operating / deployment modes considered: TUI, print, loopback web UI, read-only Plan mode with subsequent 'go' handoff, model-route enabled/pinned alternatives, optional parallel scoped child workers, sessions, hooks, tool permissions and plugin/MCP extensions.
- Recursion level: One user-directed QuikAgent coding organization/workspace; within the handoff execution there can be distinct model-guided child S1 work cells sharing an artifact workspace, not independent durable corporations.
- Reviewed revision: [shaneburrell/quikagent@d5851f84de2354f42b555367efaa339feaa46765](https://github.com/shaneburrell/quikagent/tree/d5851f84de2354f42b555367efaa339feaa46765)
- Observation date: 2026-10-22
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The shipped [cmd/quikagent/main.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/cmd/quikagent/main.go) exposes interactive, print, and loopback-web modes, registering first-party model and tools. [internal/agent/agent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/agent.go) consumes streamed model responses, executes tool calls, returns tool observations into subsequent model turns and persists session history. Plan mode produces typed [internal/tools/plan.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/plan.go) steps with file scopes and dependencies. On an installed supported plan handoff, [internal/agent/orchestrate.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/orchestrate.go) dispatches disjoint file-set work in parallel to separate [internal/agent/subagent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/subagent.go) child model/tool loops, deferring overlapping edits. A small-model reviewer checks each wave as ordinary task QA; failures mark step status, not S3 managerial audit. [internal/session/plan.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/session/plan.go) persists plans and [internal/tools/permissions.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/permissions.go) filters effectful tool access. The separate [docs/design/README.md](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/docs/design/README.md) describes prospective services not credited as shipped organizational control.

## Operational model

One configured main coding agent selects operations in response to user requests and returned observations (S1). In supported plan handoff mode, distinct child coding agents can compete for writable files; a deterministic path-overlap selector schedules non-overlapping children concurrently, returns deferred conflicts in later waves and enforces scoped operations (narrow S2=C). Routing current steps, checking wave output, tracking plan state and tool approval do not become S3/S3*/S4/S5 by name or dependency.

## S1 — Operations

- State: A
- Function: Open-ended model-guided editing, investigation and tool-driven coding in a configured QuikAgent workspace.
- Disturbance / variety regulated: User requirements, changing file states, command errors, tool outputs and model-selected next actions.
- Decisive decision or feedback right: Model chooses task-relevant tools and iteratively responds to returned results or emits a final answer.
- Decision owner: QuikAgent main model-guided Agent.Run; the runtime executes choices, and the operator governs privileged effects.
- Supporting / enforcement mechanisms: OpenAI-compatible model client, tools registry, router when enabled, tool approval, JSONL session, context compaction and optional subagents.
- Closure path: User request → streamed model output/tool call → runToolBatch permission-checked tool execution → messages with observed results → next model turn or final response; session retained.
- Boundary reachability: The shipped CLI TUI/print and loopback web paths instantiate the agent in normal operation; Agent.Run and bundled tools are first-party installed, not an external custom harness.
- Why this is / is not agent-owned: Removing the model-selected next-tool policy leaves only a deterministic tool/UI host; configured human approval limits effects but does not own every coding choice.
- Evidence: [cmd/quikagent/main.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/cmd/quikagent/main.go); [internal/agent/agent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/agent.go); [internal/tools/tool.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/tool.go); [internal/llm/client.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/llm/client.go); [internal/session/session.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/session/session.go)
- Basis: explicit and structural
- Confidence: high source-wired path; no provider-backed live inference
- Caveats: Evidence is frozen source and first-party tests inspected as code; full Go suite/live provider execution was not run in this environment.

## S2 — Coordination

- State: C
- Function: Deterministic prevention of shared-file write interference between distinct concurrently eligible model-guided plan-step workers.
- Disturbance / variety regulated: Two independently executing coding child S1 operations can target overlapping file sets in a plan wave; running both simultaneously would contend for the same files.
- Decisive decision or feedback right: Select non-overlapping eligible steps for concurrent dispatch, defer overlapping steps and release them in later waves after earlier work reaches a terminal wave status.
- Decision owner: First-party deterministic plan-wave orchestrator and file-overlap selector; no independent model-owned coordination policy assumed.
- Supporting / enforcement mechanisms: PlanStep.Files and Deps, maxParallelWorkers=3, pathOverlap/filesOverlap, scoped child edit tools, wave waitgroup, reviewer and step status tracking.
- Closure path: Confirmed plan handoff → nextWave selects eligible pending steps → pickNonOverlapping excludes conflicting file regions → concurrently launch non-overlapping subagents → wait and record done/failed states → subsequent nextWave admits formerly blocked steps into later execution. Supported test covers same-file serial execution.
- Boundary reachability: Shipped Agent.Run dispatches runOrchestrated on supported plan 'go' handoff, with model not pinned, and child Agent executes the planned work with first-party tools; this is an installed selectable mode, not docs/design future jobs.
- Why this is / is not agent-owned: The actual conflict-sensitive decision is a compiled deterministic relation in the shipped runtime, not a model autonomously adjudicating competition; S2=C is deliberately limited to this source-defined scheduler mode.
- Evidence: [internal/agent/orchestrate.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/orchestrate.go); [internal/agent/orchestrate_test.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/orchestrate_test.go); [internal/agent/subagent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/subagent.go); [internal/tools/plan.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/plan.go); [internal/agent/agent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/agent.go)
- Basis: explicit, structural and unit-test fixture
- Confidence: moderate-to-high for construction, no Go runtime attested
- Caveats: Evidence is frozen source and first-party tests inspected as code; full Go suite/live provider execution was not run in this environment.

- Distinct S1 units: Separate model/tool-running subagent workers launched for simultaneously eligible plan steps; not separate named organizations.
- Inter-S1 disturbance: Overlapping PlanStep.Files, e.g. two simultaneous workers intending main.go, produce potential write contention; frozen first-party regression test explicitly contrasts disjoint parallel work with overlapping serial work.
- Attenuating coordination relation: pickNonOverlapping plus filesOverlap/pathOverlap admits only disjoint file sets in a wave and holds overlaps for later waves; unknown empty file sets run alone.
- Feedback into subsequent S1 behaviour: Worker completion/reviewer result records step status, the loop invokes nextWave again, and previously withheld independent coding steps are then dispatched under the same model/tool runner.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The file-overlap interference criterion actively determines which distinct concurrent S1s may run and defers contention; mere tool batching and model routing are explicitly not credited.

## S3 — Inside-and-now control

- State: —
- Function: No established whole-QuikAgent current-control function owning shared organization commitments/priorities/resources beyond a user task plan.
- Disturbance / variety regulated: Workspace capacity, changing steps, user approvals, model utilization and task statuses.
- Decisive decision or feedback right: Would require a manager's whole-system current view and authoritative reallocation of operational priorities or commitments across S1 work.
- Decision owner: No qualifying distinct owner; user approves a plan and deterministic orchestrator enforces wave constraints for the current coding task.
- Supporting / enforcement mechanisms: Agent plan/todo state, model router, plan wave dispatch, session state, step limits and web/TUI reporting.
- Closure path: Plan changes and child results flow back into one requested task and its step execution; no standalone whole-current management decision governing a portfolio of independent ongoing operations.
- Boundary reachability: No S3 positive mode evidenced in installed CLI, agent, server and plan infrastructure.
- Why this is / is not agent-owned: A task plan, approval button or runtime concurrency gate cannot itself decide whole-system commitments and restore cross-S1 current control.
- Evidence: [internal/agent/orchestrate.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/orchestrate.go); [internal/tools/plan.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/plan.go); [internal/agent/agent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/agent.go); [internal/session/plan.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/session/plan.go); [internal/server/server.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/server/server.go)
- Basis: bounded first-party negative
- Confidence: moderate
- Caveats: Evidence is frozen source and first-party tests inspected as code; full Go suite/live provider execution was not run in this environment.

### Absence scope

- Surfaces inspected: Plan/todo management, orchestration, session state, server/TUI run entry and router configuration.
- Plausible first-party paths checked: Whole-system resource allocation beyond one task, cross-S1 commitment tradeoffs, current manager view and returned intervention.
- Why no material first-party path remains: Only per-task wave selection, status and operator approvals are installed; no function-specific distinct whole-system S3 right and control return was located.

## S3* — Complementary audit

- State: —
- Function: No independent audit of a whole-system S3 management account with authoritative corrective return.
- Disturbance / variety regulated: Erroneous worker completion reports, code quality defects, misleading test outcomes or audit omissions.
- Decisive decision or feedback right: Would require complementary evidence access, independent judgment over a managerial claim, and feedback to accountable whole-current control.
- Decision owner: The optional child reviewer uses a model to check step outputs, but is task-work QA serving the same orchestrator, not an S3 auditor.
- Supporting / enforcement mechanisms: reviewWave, small_model selection, PASS/FAIL parser, event tracing, feedback to failed/done step statuses and optional user approvals.
- Closure path: A code reviewer may mark a current plan wave as failed, not inspect and correct independent manager claims through a separate complementary regulatory channel.
- Boundary reachability: The reviewWave source is reachable within installed plan orchestration but cannot be promoted to S3* solely from a model label or separate child context.
- Why this is / is not agent-owned: Reviewer isolation and ordinary task-acceptance decisions are not enough to establish independent S3 report challenge and corrective governance.
- Evidence: [internal/agent/orchestrate.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/orchestrate.go); [internal/agent/orchestrate_test.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/orchestrate_test.go); [internal/agent/subagent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/subagent.go); [docs/architecture.md](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/docs/architecture.md)
- Basis: bounded first-party negative
- Confidence: moderate
- Caveats: Evidence is frozen source and first-party tests inspected as code; full Go suite/live provider execution was not run in this environment.

### Absence scope

- Surfaces inspected: First-party reviewWave and FAIL handling, tracing, reviewer model/child wrapper, task plan and web/TUI report path.
- Plausible first-party paths checked: Independent sampling of S3 current-management claims, distinct audit authority and corrective returned manager act.
- Why no material first-party path remains: All review verdicts concern step output acceptance within one coding task; no separate complementary managerial audit function or S3 corrective return is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No observed first-party future viability intelligence that selects and installs durable new agent capability or strategy from prospective external assessment.
- Disturbance / variety regulated: Changing tools/providers, technology environment, project requirements, new model choices and future workflow needs.
- Decisive decision or feedback right: A qualified S4 actor would generate prospective adaptation options and decide/reinstate adopted capability in later operation.
- Decision owner: Not established; user chooses model, config, skills/agents and developers evolve repo; optional router routes current tasks.
- Supporting / enforcement mechanisms: Model router, persisted plans/JSONL sessions, custom agents/skills, configurable hooks and roadmap design documents.
- Closure path: Current routing, session reuse and plan editing affect immediate task execution, not independently evidenced external-and-future analysis → adaptation choice → durable adopted next-generation capability.
- Boundary reachability: No S4 positive in shipped runtime; proposed daemon/jobs/projects design docs are not credited as executed capabilities.
- Why this is / is not agent-owned: Session memory and selecting a current model are task-level support; developer roadmap and external plugin possibilities cannot donate first-party S4.
- Evidence: [internal/router/router.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/router/router.go); [internal/session/session.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/session/session.go); [internal/agent/agent.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/agent/agent.go); [docs/extending.md](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/docs/extending.md); [docs/design/README.md](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/docs/design/README.md)
- Basis: bounded first-party negative
- Confidence: moderate
- Caveats: Evidence is frozen source and first-party tests inspected as code; full Go suite/live provider execution was not run in this environment.

### Absence scope

- Surfaces inspected: Model routing, config, hooks/skills/custom agents, session/plan persistence and proposed designs.
- Plausible first-party paths checked: First-party prospective environmental intelligence, selected adaptation decision and durable feedback into changed future operation.
- Why no material first-party path remains: Installed facilities select/use existing options for current tasks; future subsystem designs are unshipped and no verified adoption loop is present in source.

## S5 — Policy and identity

- State: —
- Function: No shipped legitimate ultimate purpose/identity decision loop returning an authoritative decision to the agent organization.
- Disturbance / variety regulated: Requests beyond configured bounds, unsafe shell/file operations, operator model choices and external service credentials.
- Decisive decision or feedback right: A qualified S5 owner would decide legitimate system purpose and ultimate policy then send an enforceable return to operation.
- Decision owner: Operator supplies instructions, keys and tool approval, but no source-installed organization-level function-specific parent S5 is established.
- Supporting / enforcement mechanisms: RuleMatcher, CheckPermission, TUI/web approval, sandbox tools, setup/YAML and user docs.
- Closure path: Permission checks filter individual tool requests; the returned allow/deny is an execution gate, not a full identity/ultimate-policy issue processed and decided with governance feedback.
- Boundary reachability: No positive S5 mode credited; tool policies are shipped but are distinct from a complete S5 owner.
- Why this is / is not agent-owned: Static allow/deny rules and user task directives enforce boundaries chosen elsewhere rather than constitute first-party ultimate policy authority.
- Evidence: [internal/tools/permissions.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/permissions.go); [internal/tools/tool.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/tools/tool.go); [internal/config/config.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/internal/config/config.go); [cmd/quikagent/main.go](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/cmd/quikagent/main.go); [docs/config.md](https://github.com/shaneburrell/quikagent/blob/d5851f84de2354f42b555367efaa339feaa46765/docs/config.md)
- Basis: bounded first-party negative
- Confidence: moderate
- Caveats: Evidence is frozen source and first-party tests inspected as code; full Go suite/live provider execution was not run in this environment.

### Absence scope

- Surfaces inspected: Bundled security permissions, config, interactive/print/web approval, agent instruction path and operator CLI.
- Plausible first-party paths checked: Legitimate whole-organization identity question, decisive policy authority and returned rule across later operation.
- Why no material first-party path remains: Tool permissions implement externally chosen rules per effect without the required function-specific ultimate-policy decision and organizational return.

## Recursion

The project is a deployable local coding assistant. Optional plan worker loops are S1 task cells sharing a project; 'spawning' alone does not establish higher recursion or transferred S5 authority.

## Variety and escalation

File-path conflicts and task dependencies are concrete inter-S1 variety; the deterministic wave selector limits concurrent competing edits. Provider retries, tool approvals, session plan statuses and failure results are ordinary operational signals; no dedicated higher-recursion algedonic channel was established.

## Evidence gaps

1. Frozen source was inspected with explicit tests including `TestOrchestrateOverlappingFilesSerial` and `TestOrchestrateParallelDisjointFiles`; no Go toolchain was available to execute those tests. Source tests corroborate implementation but are not newly executed runtime traces.
2. S2 positive claim is narrow: first-party plan-wave file collision attenuation in the supported unpinned handoff mode. This does not claim autonomous policy, generalized organizational concurrency control or prevention of all possible file conflicts.
3. Plugin/custom-agent behavior, unshipped designs, human maintainer governance and model-provider internal capabilities are outside the assessed first-party owner boundary.
