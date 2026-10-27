---
harness_id: snow
project_name: Snow
repository: https://github.com/elmissouri16/snow-core
review_ref: 631586d013897a85c0c1f79830204af7822e60b0
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Snow

## Review boundary

- System in focus: one Snow root coding session with optional first-party child agents; separately declared opt-in review-team plugin mode.
- Purpose and identity: perform coding work through a streaming model/tool loop and persistent session branches.
- Relevant environment: local workspace/OS, configured providers, user permissions, plugins and child tasks.
- Standard-distribution boundary: Go binary, core built-in tools, optional root subagent manager and the explicitly documented source-package review-team plugin. No borrowed repository-development auditor.
- Credited operating / distribution surfaces: [internal/agent/lifecycle_run.go](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/agent/lifecycle_run.go), [internal/agent/streaming_tools.go](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/agent/streaming_tools.go), [internal/subagent/tools.go](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/subagent/tools.go), [internal/tools/builtin/root_mutation.go](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/tools/builtin/root_mutation.go), [docs/subagents.md](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/subagents.md), [docs/plugin-extensions.md](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/plugin-extensions.md), [examples/plugins/review-team/main.js](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/examples/plugins/review-team/main.js)
- Adjacent first-party surfaces excluded from ownership: AGENTS.md contributor operations, code-audit/development plans, CI, performance benchmarks, fake-provider tests and browser fixtures are not deployed owners. Plugin examples are not automatically installed; only the specifically documented review-team launch is considered as an optional constructor.
- First-party operating / deployment modes considered: TUI, print/JSON/RPC/Go SDK, local web manager; --subagents and role/mutation options; explicit snow --subagents --js-plugin ./examples/plugins/review-team. Managed web goal mode disables plugins and therefore does not inherit review-team.
- Recursion level: root's current coding task tree; independent host projects and repository-maintainer organization excluded.
- Reviewed revision: 631586d013897a85c0c1f79830204af7822e60b0
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Snow exposes one Go agent loop through terminal, CLI, RPC and SDK surfaces. It persists branched sessions in SQLite, collects streaming provider tool calls, performs permission/admission checks and executes results back into the next turn. A root-scoped manager runs separate child agent contexts, stable identities, bounded result/mailbox delivery and close/resume/interrupt/follow-up operations. Optional mutable children share the process filesystem; a process-wide mutation gate and edit-snapshot validation attenuate write races. Thread Goals continue serial turns under user-defined objectives/budgets. Plan Mode restricts mutation. The optional review-team JavaScript command runs three fresh read-only explorer reviewers, stores findings and prompts root synthesis. Trust, permissions, plugin audit metadata, managed process control, compaction and tool discovery support runtime operation.

## Operational model

Root and child model-backed work cells absorb coding/research variety. Root list/interrupt/close/reopen/follow-up decisions regulate active commitments and release scarce open-child slots; fixed concurrency limits remain operator-selected enforcement. The review-team plugin is a specific packaged optional audit path, distinct from generic child spawning, and is not installed by default.

## S1 — Operations

- State: A
- Function: coding task execution
- Disturbance / variety regulated: uncertain workspace and changing tool outcomes
- Decisive decision or feedback right: choose actions and arguments, inspect results and continue or stop
- Decision owner: root/child provider-backed models
- Supporting / enforcement mechanisms: stream collector, permission service, tool execution, SQLite sessions and bounded retries
- Closure path: provider tool calls → execute/persist results → continuation provider request; final child outcome returns to root mailbox
- Why this is / is not agent-owned: The model chooses the solution; the loop and permission service enforce its available repertoire.
- Evidence: [internal/agent/lifecycle_run.go#L409-L650](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/agent/lifecycle_run.go#L409-L650), [internal/agent/streaming_tools.go#L439-L515](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/agent/streaming_tools.go#L439-L515), [internal/subagent/worker.go#L146-L175](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/subagent/worker.go#L146-L175)
- Basis: structural
- Confidence: medium-high
- Caveats: Pinned source establishes a supported path, not observed effectiveness or universal deployment.
- Boundary reachability: The documented CLI/RPC/SDK surfaces share the core; --subagents constructs child runtimes without custom orchestration.

## S2 — Coordination

- State: C
- Function: attenuate conflicting shared-workspace mutations across operational writers
- Disturbance / variety regulated: enabled root/implementer children can mutate the same files concurrently
- Decisive decision or feedback right: serialize built-in rooted mutations and reject an edit whose read snapshot changed before replacement
- Decision owner: deterministic first-party mutation path; autonomous cross-writer scope negotiation is not supplied by this gate
- Supporting / enforcement mechanisms: process-wide rootedMutationGate, identity/content validation, atomic replacement and returned tool errors
- Closure path: concurrent mutation → gate serialization or snapshot conflict → error asks reread → model revises subsequent action
- Why this is / is not agent-owned: This is a conflict-specific built-in constructor, not autonomous coordination ownership. The gate does not choose disjoint team scopes; broader coordination is left to the agent/operator.
- Evidence: [docs/subagents.md#L6-L8](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/subagents.md#L6-L8), [internal/subagent/tools.go#L285-L294](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/subagent/tools.go#L285-L294), [internal/tools/builtin/edit.go#L105-L181](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/tools/builtin/edit.go#L105-L181), [internal/tools/builtin/root_mutation.go#L9-L55](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/tools/builtin/root_mutation.go#L9-L55)
- Basis: structural
- Confidence: medium-high
- Caveats: External processes may race after the final check; source explicitly disclaims portable CAS. The coordination path is bounded to built-in mutation tools and enabled child modes.
- Boundary reachability: Built-in editing and optional mutation-enabled children use the same process gate. No extra plugin implements the credited collision path.
- Distinct S1 units: root and simultaneously active mutation-enabled implementer children.
- Inter-S1 disturbance: two writers can read/change the same rooted file while another edit is pending.
- Attenuating coordination relation: serialize built-in mutations; validate file identity/content before replacement.
- Feedback into subsequent S1 behaviour: conflicting edit fails with reread-before-retry feedback through the normal tool-result loop.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation directly targets lost edits and shared-file collisions, rather than generic agent messages.

## S3 — Inside-and-now control

- State: A
- Function: regulate current task-tree commitments and child resources
- Disturbance / variety regulated: running/queued/terminal work, failed tasks and finite open-agent slots
- Decisive decision or feedback right: inspect whole root tree, interrupt active work, close idle children to release slots, resume and assign corrective follow-up
- Decision owner: root model in enabled subagent mode
- Supporting / enforcement mechanisms: list_agents counters/limits, lifecycle state machine, mailbox delivery and manager bounds
- Closure path: status/final result → root chooses interruption/closure/reopening/follow-up → manager changes active commitments → later state and results return
- Why this is / is not agent-owned: The model chooses which work to continue and which slot to release; fixed concurrency/deadline enforcement is not credited as owner.
- Evidence: [internal/subagent/tools.go#L147-L213](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/subagent/tools.go#L147-L213), [internal/subagent/tools.go#L285-L294](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/subagent/tools.go#L285-L294), [internal/subagent/operations.go#L15-L96](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/subagent/operations.go#L15-L96), [docs/subagents.md#L97-L127](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/subagents.md#L97-L127)
- Basis: structural
- Confidence: medium-high
- Caveats: Opt-in task-tree scope. TUI next-launch concurrency settings and generic approvals do not establish an additional parent S3 mode.
- Boundary reachability: Enabled root receives the built-in lifecycle tools and independent result feedback. This requires only the documented subagent option.
- Whole-system current view: root's visible task tree with running/queued/open/closed counts, limits and attributed results.
- Current-control decision scope: current child commitments, corrective reassignment and finite open slots; not global host resource administration.

## S3* — Complementary audit

- State: C
- Function: complementary read-only inspection of current workspace change claims
- Disturbance / variety regulated: coding results can contain correctness, architectural or test gaps hidden by ordinary task reports
- Decisive decision or feedback right: launch fresh context reviewers against actual source/tests and return evidence-bearing findings; corrective authority/acceptance coupling remains to be composed
- Decision owner: independent explorer models judge findings; root synthesizes; final corrective current-control mandate is not bound by the plugin
- Supporting / enforcement mechanisms: packaged review-team command, fork_turns:none, role read restrictions, session storage and root prompt
- Closure path: explicit review request → three read-only independent-context source checks → findings stored and injected into root synthesis; further corrective work is not enforced
- Why this is / is not agent-owned: A function-specific audit construction exists with complementary source access. C records the incomplete connection from synthesis to a designated corrective decision, rather than borrowing an audit from repository CI.
- Evidence: [docs/plugin-extensions.md#L25-L60](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/plugin-extensions.md#L25-L60), [examples/plugins/review-team/main.js#L19-L38](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/examples/plugins/review-team/main.js#L19-L38), [examples/plugins/review-team/snow-plugin.json](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/examples/plugins/review-team/snow-plugin.json), [internal/subagent/context.go#L30-L95](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/subagent/context.go#L30-L95)
- Basis: structural
- Confidence: medium-high
- Caveats: Not an installed default auditor or guaranteed fix loop. Review findings are not proof of empirical defect detection or independence from malicious workspace content.
- Boundary reachability: A documented command launches the supplied package using --js-plugin; it needs no custom plugin authoring, but it is opt-in and unavailable when plugins are disabled.
- Claim being audited: the sufficiency/correctness of current workspace changes selected as review focus.
- Ordinary reporting path: coding conversation and child final results.
- Complementary access path: new explorer contexts inspect source/tests directly, returning file/line/severity/evidence.
- Independence boundary: fork_turns:none and read-only roles separate reviewers from producer history and mutation; same provider remains possible.
- Who acts on findings: root receives the review synthesis; user/root must supply the subsequent corrective mandate.

## S4 — Outside-and-then intelligence

- State: —
- Function: external prospective adaptation
- Disturbance / variety regulated: Goals, model inventory, webfetch and plugin authoring do not by themselves adapt harness capability to future environmental distinctions.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: goal controller, provider catalogs, deferred webfetch, skills/plugin management and architecture roadmap
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: The shipped mechanisms execute present objectives or load selected capabilities; no first-party environmental/future adaptation judgment and closed current-capability return was established, including parent mode.
- Evidence: [docs/goals.md](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/goals.md), [internal/goal/controller.go](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/goal/controller.go), [docs/plugins.md](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/plugins.md), [docs/architecture.md](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/architecture.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: goal controller, provider catalogs, deferred webfetch, skills/plugin management and architecture roadmap
- Plausible first-party paths checked: whether goal progression, model selection, research or a plugin update supplies externally/prospectively developed options returning into current capability
- Why no material first-party path remains: The shipped mechanisms execute present objectives or load selected capabilities; no first-party environmental/future adaptation judgment and closed current-capability return was established, including parent mode.

## S5 — Policy and identity

- State: —
- Function: ultimate identity-policy closure
- Disturbance / variety regulated: Plan/Default, project trust and permissions regulate ordinary actions and startup options.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: collaboration policy, permissions, project trust, goal replacement and plugin controls
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: These controls constrain current tasks; no specific unresolved identity-policy issue/legitimate authority/returned policy loop is supplied for the assessed task tree.
- Evidence: [internal/agent/collaboration_policy.go](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/internal/agent/collaboration_policy.go), [docs/security.md](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/security.md), [docs/goals.md](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/goals.md), [docs/plugins.md](https://github.com/elmissouri16/snow-core/blob/631586d013897a85c0c1f79830204af7822e60b0/docs/plugins.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: collaboration policy, permissions, project trust, goal replacement and plugin controls
- Plausible first-party paths checked: whether user goal/permission decisions are identity-level issues with authoritative return
- Why no material first-party path remains: These controls constrain current tasks; no specific unresolved identity-policy issue/legitimate authority/returned policy loop is supplied for the assessed task tree.

## Distributed OSS parent arrangement

Repository maintainers/development audit artifacts are outside the installed coding system. Local user permissions and goals do not establish organization-level parent modes.

## Self-hosted and non-human modes

Provider, CLI, SDK and web surfaces share the loop with different declared restrictions. Review-team is credited only in the documented opt-in plugin mode; managed web goal mode disables plugins. No autonomous/parent S4/S5 mode is inferred.

## Recursion

Stable child paths and optional recursion limits establish delegation structure, not full viable recursive organizations.

## Variety and escalation

Bounded result/mailbox/context projections attenuate reporting. Root can inspect states and change commitments. Conflict rejection returns local failure to the model; goals detect some non-progress but do not prove whole-system adaptation or algedonic governance.

## Evidence gaps

Go toolchain was unavailable, so native tests/build were not executed; no live provider tasks. Source specifies limits and external mutation race. Plugin example support was verified from its launch documentation and code; no installation/execution was performed.

## Index execution provenance

Frozen intake #2176, serial controller #2177, row 3. Source assessment is the executing Index S1 actor's work; GitHub, deterministic checks and CI are supporting machinery. No independent semantic review or autonomy grade is claimed. Proposed publication precedes a separate canonical transaction.
