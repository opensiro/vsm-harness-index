---
harness_id: opencode-jarvis
project_name: OpenCode Jarvis
repository: https://github.com/yizhi0107-bot/opencode-jarvis
review_ref: fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OpenCode Jarvis

## Review boundary

- System in focus: The published OpenCode cost-tiered orchestration plugin and the first-party Jarvis parent plus eight installed worker roles, ticket-governance hooks and bundled command workflows.
- Purpose and identity: Assign coding tasks to appropriate local or strong-model roles, prevent unregulated concurrent edits, review implementation and consolidate verified outcomes within one Jarvis-led task composition.
- Relevant environment: OpenCode host and model providers, workspace files, human programming requests, child results, concurrent ticket scopes, permission events and configurable model/tier caps.
- Standard-distribution boundary: Installed plugin 0.4.2 with agentScope global/project, first-party role and command templates, dispatch/permission/tool hooks and telemetry. OpenCode is a declared host dependency; its generic agents are not counted beyond the first-party Jarvis-specific composition.
- Credited operating / distribution surfaces: [plugin entry](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/index.ts), [tickets](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/tickets.ts), [Jarvis role](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/agents/jarvis.md), [reviewer](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/agents/reviewer.md), [deep command](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/commands/deep.md), [OPTIONS](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/OPTIONS.md).
- Adjacent first-party surfaces excluded from ownership: Development verification script, npm release metadata, external OpenCode host internals, Ollama/strong provider internals, human software project governance, off-mode user-maintained replacement agent definitions and README claims unimplemented outside the pinned wiring.
- First-party operating / deployment modes considered: Agent installation in user or project scope, interactive Jarvis agent, explicit /deep and /council workflows, /quick and /digest, jarvis_dispatch tool, local telemetry and user-configured model/tier limits; agentScope=off disables role installation and is not an independent deployed Jarvis composition.
- Recursion level: One Jarvis-controlled programming work package with dedicated subagents. Plugin-wide metrics may aggregate use across sessions but are not a whole organization policy system.
- Reviewed revision: fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The plugin installs one restricted primary Jarvis agent, eight named workers and four command templates through OpenCode, and registers a first-party ticket tool plus permission and post-tool hooks. The parent cannot edit files or invoke shell directly; it routes through cheaper local triage/scribe/scout/digest or strong architect/executor/debugger/reviewer, issuing a ticket with worker, goal, scope, acceptance and output limit before any Jarvis-prefixed subagent. The ticket map enforces tier concurrency limits and mutual exclusion for overlapping executor/debugger scopes; unauthorized dispatch is refused and returned to the parent agent. Subagent completion closes the ticket, records metric events and compresses overlong output. The Jarvis role prescribes route confidence fallback, dependency-aware parallel work and escalation from executor to debugger. The installed /deep workflow mandates architect → executor → read-only reviewer, then repairs and one re-review for significant findings. /council asks separate configured judges for independent inputs and summarizes disagreement. Model availability warnings are nonblocking; /jarvis-stats aggregates past dispatch, rejection and compression records rather than presenting an automatic governance policy. [README](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/README.md), [tickets](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/tickets.ts), [template installer](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/install-agents.ts).

## Operational model

Writer workers own substantive workspace changes and verification; local read-only workers research, triage or produce summaries (S1). The model-bearing Jarvis controller receives worker outcomes and ticket refusals, revises assignment/scopes and enforces same-file discipline (S2), while allocating current task work among local and strong workers and escalating failed efforts (S3). A separate restricted read-only reviewer can inspect actual code and test evidence after implementation and return issues for corrective executor work in the installed /deep workflow (S3*); it is distinct from ordinary executor reporting. The system has no installed prospective external strategy or enduring policy/identity adjudication (S4/S5).

## S1 — Operations

- State: A
- Function: Execute code, research, debugging and documentation subtasks through model-bearing specialist workers and tool result feedback.
- Disturbance / variety regulated: Unknown files, failing tests, coding defects, unclear task scope and errors returned by tools or delegated roles.
- Decisive decision or feedback right: Select file modifications, investigations, debug hypotheses, test commands and worker responses within an assigned scoped ticket.
- Decision owner: Each specialist LLM role, notably executor/debugger for code writes and architect/scout/scribe for analysis; OpenCode transports actual tool calls.
- Supporting / enforcement mechanisms: Role-specific tools and permissions, bounded steps, task instructions, acceptance criteria, ticketed subagent launch and test reporting.
- Closure path: Parent issues ticket/task → specialist runs model-selected work and observes file/test results → child reports result → parent consumes output and may assign correction.
- Boundary reachability: Plugin setup installs the bundled roles via installResources and agent.reload; Jarvis commands and first-party agent prompt delegate to them through the OpenCode host. The claim requires running the declared host, not external maintainer dogfood.
- Why this is / is not agent-owned: Worker model chooses substantive edits/investigations. The ticket gate restricts scope/parallelism but does not implement the code.
- Evidence: [executor](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/agents/executor.md), [debugger](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/agents/debugger.md), [installer](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/install-agents.ts), [tickets](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/tickets.ts).
- Basis: explicit + structural
- Confidence: high for shipped decision path, medium for actual provider outcome.
- Caveats: Models and OpenCode host runtime were not live exercised here; this is a source-level review.

## S2 — Coordination

- State: A
- Function: Agent-governed adjustment of contemporaneous specialist work to avoid collisions over shared file scopes and tier capacity.
- Disturbance / variety regulated: Two executor/debugger workers target overlapping files, or local/strong concurrency cap is exhausted while the parent seeks another dispatch.
- Decisive decision or feedback right: After refusal, choose to wait, narrow scope, group independent work, change worker or dispatch order, then issue a revised ticket; repeated collision is no longer blindly launched.
- Decision owner: Strong-model Jarvis parent chooses changed task boundaries/timing; plugin ticket guard detects and enforces collisions.
- Supporting / enforcement mechanisms: Ticket map with scopeConflict, writesFiles classifier, per-tier caps, dispatch refusal messages, permission hook denying subagents with no issued ticket, completion/TTL cleanup.
- Closure path: Active writer ticket creates occupied scope → new overlapping dispatch rejected with actual ticket ID/reason → Jarvis receives refusal and is instructed to revise scope/wait → revised dispatch, or changed sequence, allows nonconflicting work → completion frees scope.
- Boundary reachability: src/index.ts registers the governance plugin hooks, and the installed Jarvis role explicitly requires ticketed dispatch and instructs the model to respond to rejection rather than simply repeat it; this is a first-party standard-distribution path.
- Distinct S1 units: Named executor and debugger (and other local/strong workers) dispatched as separate model-bearing subagents.
- Inter-S1 disturbance: Overlapping writer file scopes and excessive simultaneously active workers.
- Attenuating coordination relation: Substantive model selection of a revised scope or time coupled to a first-party ticket collision guard.
- Feedback into subsequent S1 behaviour: Returned rejected ticket or completed-ticket audit changes the next dispatch, so subsequent workers run with non-overlapping scopes or deferred timing.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It identifies competing file ownership of two actual worker types and supplies explicit conflict refusal plus returned agent-directed correction; ordinary subagent routing alone would not be credited.
- Why this is / is not agent-owned: Collision detection is deterministic, but the living Jarvis model owns the correction and subsequent assignment, making this A in the documented operating mode.
- Evidence: [tickets collision and issue](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/tickets.ts#L90-L192), [tickets hooks](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/tickets.ts#L245-L340), [Jarvis discipline](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/agents/jarvis.md), [workers](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/workers.ts).
- Basis: explicit + structural
- Confidence: medium-high for installed per-process tickets.
- Caveats: Scope matching is string/path-prefix-based and can miss semantically shared state; it does not prove cross-process or cross-organization conflict isolation.

## S3 — Inside-and-now control

- State: A
- Function: Jarvis allocates and revises current work across the specialized agent portfolio in one managed task.
- Disturbance / variety regulated: Task difficulty variation, local-model failure, worker resource saturation, poor implementation quality and mismatched work commitments.
- Decisive decision or feedback right: Decompose task, choose route/tier and worker, set goal/scope/acceptance, decide parallel vs sequential dispatch and escalate executor failures to debugger or reviewer.
- Decision owner: Primary strong-model Jarvis in the installed role; human sets initial task and broad resource limits.
- Supporting / enforcement mechanisms: Explicit primary agent with no edit/shell permission, eight worker roster, local/strong tier caps, dispatch ticket lifecycle, route-confidence fallback and scoped result summaries.
- Closure path: Current user goal and worker feedback/refusals → Jarvis assesses whole local task and active commitments → changes worker, scope, order or escalation → ticketed child action → returned results for further current decisions.
- Boundary reachability: Plugin installs a primary Jarvis agent and dispatch tool, and documented --agent jarvis or TUI selection reaches the agent instructions; /deep assigns a concrete sequence. No independent external PM is required.
- Whole-system current view: The supervising Jarvis conversation owns its task decomposition, issued ticket IDs, child returns, failure/rejection feedback and, when requested, aggregated /jarvis-stats telemetry. This is a local one-task composition view, not a cross-session global operations center.
- Current-control decision scope: Allocation of current subtask work by model tier, worker, acceptance criteria, file scope, concurrency/ordering and escalation after failure.
- Why this is / is not agent-owned: Jarvis decides substantive current priorities and reassignments; deterministic ticket limits enforce rather than decide the portfolio plan.
- Evidence: [Jarvis primary role](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/agents/jarvis.md), [deep workflow](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/commands/deep.md), [tickets](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/tickets.ts).
- Basis: explicit + structural
- Confidence: medium at declared task recursion; no global whole-project oversight claim.
- Caveats: Ticket active map remains internal to one plugin process; operational view is parent conversation and its task, not all users or projects.

## S3* — Complementary audit

- State: A
- Function: Separate read-only reviewer role independently checks implemented code and tests, returning repair findings to the task controller.
- Disturbance / variety regulated: An executor may claim a successful change despite defects, regression risks, boundary gaps or insufficient tests.
- Decisive decision or feedback right: Inspect real files/test outcomes distinct from executor narrative, judge severity and return issues for correcting the actual implementation.
- Decision owner: Jarvis/reviewer model, separate from writer executor and constrained to read/grep/glob plus user-confirmed shell tests; Jarvis orders returned corrections.
- Supporting / enforcement mechanisms: Reviewer role permission boundary denying edits, dedicated reviewerModel option, /deep mandated review and severity-triggered executor fix + one re-review, /council independent judge inputs.
- Closure path: Executor reports implemented diff → separate reviewer reads working source and may run checks → reviewer returns high/medium findings with file:line/severity → Jarvis sends executor correction → reviewer rechecks, then final report.
- Boundary reachability: Bundled reviewer and /deep templates are installed in global/project scope by the first-party installer; the exact installed command explicitly mandates reviewer and returned fix/review. No external CI auditor is borrowed.
- Claim being audited: Correctness, regressions, boundaries, maintainability and test evidence for this task's implementation.
- Ordinary reporting path: Executor's changed-file and verification report to Jarvis after its assigned work.
- Complementary access path: Reviewer uses independent tool calls to read/search changed files and, with permission, run tests/static checks.
- Independence boundary: Separate model role and tool restrictions (read-only; cannot edit); reviewer does not merely repeat executor's output, but its subprocess still shares the workspace and is not an organizationally independent external auditor.
- Who acts on findings: Jarvis directs executor to repair high/medium issues and orders one subsequent reviewer pass in /deep mode.
- Why this is / is not agent-owned: The reviewing model makes its own issue/severity judgment from code; controller/host pass its findings to an explicit correction path.
- Evidence: [reviewer role](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/agents/reviewer.md), [deep workflow](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/commands/deep.md), [council workflow](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/commands/council.md).
- Basis: explicit + structural
- Confidence: medium for documented correction ownership; direct provider-level independence and efficacy not runtime tested.
- Caveats: A bundled command instructing review is not itself evidence of actual effective audit in every provider run. CLI must explicitly select --agent jarvis for the /deep pathway, as README warns.

## S4 — Outside-and-then intelligence

- State: —
- Function: No installed prospective external environment sensing and future system capability adaptation loop.
- Disturbance / variety regulated: Cost/quality routing, output limits and failed tools are handled for the present request.
- Decisive decision or feedback right: Form and select a strategic future adaptation option and return it to current capability governance; not supplied.
- Decision owner: Jarvis selects current task route; operator/maintainer changes models/options and versions outside a first-party prospective policy cycle.
- Supporting / enforcement mechanisms: Triage confidence fallback, model availability warning, metrics audit and /jarvis-stats historical aggregation, setup/reload command.
- Closure path: Metrics are visible to a user and routing decisions affect present task; no automatic or mandatory future adaptation selection and capability-return channel is closed.
- Why this is / is not agent-owned: Cheap-vs-strong model choice is an immediate current allocation (S3), not automatically outside-and-then strategic intelligence.
- Evidence: [Jarvis prompt](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/templates/agents/jarvis.md), [commands/stats](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/commands.ts), [options](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/options.ts).
- Basis: explicit + structural
- Confidence: medium-high.
- Caveats: Human may analyze historical routing metrics and change configuration manually; this is not a separately closed S4 mode.

### Absence scope

- Surfaces inspected: Route templates, triage, model lists, /jarvis-stats data, setup/reload, options and roadmap.
- Plausible first-party paths checked: Dynamic route, historical metrics, configurable route thresholds/models and error-driven debugger escalation.
- Why no material first-party path remains: All shipped feedback regulates present dispatch or passive statistics; no first-party future-oriented adaptation authority returns selected capability changes into operation.

## S5 — Policy and identity

- State: —
- Function: No separate ultimate identity or policy adjudication with authoritative returned governance.
- Disturbance / variety regulated: Unauthorized dispatch and unsafe commands are bounded by fixed plugin ticket and role permission rules.
- Decisive decision or feedback right: Resolve a continuing identity/ultimate-policy conflict and issue binding policy for later organizational operations; absent.
- Decision owner: Maintainer-designed Jarvis purpose and role templates, human-selected installation scope/models; tickets enforce operational rules rather than a changing S5 mandate.
- Supporting / enforcement mechanisms: User configuration, agentScope global/project/off, role permissions, no-ticket dispatch refusal, selected local/strong models.
- Closure path: User selects options or model and reloads; call gates execute configured rules. No S5 identity question → legitimate ultimate authority judgment → binding policy-return feedback loop is shipped.
- Why this is / is not agent-owned: Fixed local-first identity and per-call permission policies do not create self-governing S5; config changes alone do not establish P.
- Evidence: [options](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/options.ts), [installer](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/install-agents.ts), [tickets](https://github.com/yizhi0107-bot/opencode-jarvis/blob/fb8e47dc6525ec4ff4b4ef333ae7a8d8420c49d7/src/tickets.ts).
- Basis: explicit + structural
- Confidence: medium-high.
- Caveats: OpenCode's broader host or a user's project governance may supply policy elsewhere but is not this plugin's credited S5.

### Absence scope

- Surfaces inspected: Jarvis primary role, configured options and scope, model setup, worker permissions, ticket gates and plugin registration.
- Plausible first-party paths checked: Operator changing models/tier caps, project/global install choice, fixed local-first mission and denied unauthorized dispatch.
- Why no material first-party path remains: They select and enforce runtime behavior but never establish an ultimate-policy issue, authorized identity-level adjudicator and returned policy decision.

## Distributed OSS parent arrangement

The OpenCode plugin ships per-installation agents and ticket hooks; contributor governance and npm/GitHub release practices are adjacent. No organization-wide parent control is credited across independently configured OpenCode installations.

## Self-hosted and non-human modes

The plugin can use local Ollama models and strong remote providers. Default model availability warnings do not block setup; runtime outcomes depend on the selected host. The autonomous S2/S3/S3* findings concern the first-party installed Jarvis model/task workflow, not generic unconfigured OpenCode or agentScope=off.

## Recursion

The Jarvis primary agent and eight worker roles form one bounded task recursion with specialist operational cells; concurrent work is ticketed, but scope locks and metrics are local process state. Nothing establishes higher-recursion organizational S5 or global cross-session current control.

## Variety and escalation

Cost-tier routing and distinct roles amplify response variety; ticket schema, overlap checks, per-tier caps and output compression attenuate overload. Refusal messages feed back to Jarvis for changed dispatch, and review findings may return to executor for a second check. Statistics preserve history but do not independently select future adaptation.

## Evidence gaps

- Verified pinned source, templates and development verifier. The OpenCode host and configured model providers were not installed for end-to-end dispatch or reviewer runs; success/quality are not claimed.
- The reviewer is role-separated and can inspect source/test results, but separate-provider independence, external institutional audit and objective efficacy remain unproven. Existing user-owned role files may be retained rather than overwritten by installation.
