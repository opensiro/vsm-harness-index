---
harness_id: phi
project_name: Phi
repository: https://github.com/pulseaiclub/phi
review_ref: 463c21cccffd4c8b2ee392f7567b094b8fd7b456
reviewed_at: 2026-10-21
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

# Phi

**Proposed, noncanonical inclusion** for batch [#1842](https://github.com/opensiro/vsm-harness-index/issues/1842) row 5, frozen discovery [#860](https://github.com/opensiro/vsm-harness-index/issues/860). Source-scoped VSM vector **A / — / — / — / — / —**, not an evaluation of task success, model quality, customer deployment or maximum extensibility.

## Review boundary

- System in focus: First-party shipped Phi terminal/headless coding-agent program and supported in-process spawned jobs within one installed user's project.
- Purpose and identity: Operator-directed open-ended software editing, investigation and verification through model-chosen tool executions with optional isolated child agents.
- Relevant environment: Repository workspace, shell and files, user policies and permissions, external LLM/provider endpoints, optional MCP servers, extensions and local sessions.
- Standard-distribution boundary: Go command entrypoints and packaged internal agent/model/tool/job/session/permission implementations at this exact source revision. Optional installed extensions and external model reasoning are dependencies, not independently authored organizational decisions.
- Credited operating / distribution surfaces: [cmd/runloop.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/cmd/runloop.go), [internal/agent/engine.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/engine.go), [internal/agent/executor.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/executor.go), [internal/agent/engine_runner.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/engine_runner.go), [internal/job/manager.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/job/manager.go), [internal/session/manager.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/session/manager.go), [internal/permission/gate.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/permission/gate.go) and their shipped wiring.
- Adjacent first-party surfaces excluded from ownership: [internal/optimizer/suggest/suggest.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/optimizer/suggest/suggest.go) is an optional interactive shell-history completion recommender, not a strategic manager; tests, CI/release, README marketing metrics, example extension SDKs, developer roadmap, and human-maintained repository governance are not installed agent organizational functions. Third-party model/provider/extension functions are excluded unless credited only through a concrete shipped call path.
- First-party operating / deployment modes considered: interactive TUI, headless run, optional configured child explore/review/worker jobs, scoped shell/file tool permissions, session resume and explicit model/config changes.
- Recursion level: One self-hosted agent work organization per Phi workspace/session, with optional subordinate model-guided child jobs as task cells, not independently demonstrated viable organizations.
- Reviewed revision: [pulseaiclub/phi@463c21cccffd4c8b2ee392f7567b094b8fd7b456](https://github.com/pulseaiclub/phi/tree/463c21cccffd4c8b2ee392f7567b094b8fd7b456)
- Observation date: 2026-10-21
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The executable [cmd/runloop.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/cmd/runloop.go) builds a first-party [internal/agent/engine.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/engine.go) tool-use loop, model adapter and [internal/agent/executor.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/executor.go) that distinguishes read-only batches from possibly mutating tools. The engine submits observations to a model and preserves user/session outputs. Interactive/headless clients use installed permissions, optional MCP and extension tools, durable [internal/session/manager.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/session/manager.go) state, and configurable operator policy. Optional [internal/agent/jobs.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/jobs.go) creates a process-local [internal/job/manager.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/job/manager.go) whose [internal/agent/engine_runner.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/engine_runner.go) drives distinct child engines in explore, review and worker roles. Its default concurrency budget is four; full capacity returns ErrBusy rather than retaining a queued competing cell. Recovery marks stale jobs failed, while child run outputs are available to the parent. [internal/agent/child_spec.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/child_spec.go) limits reviewer/explorer to read-only tools, worker to bounded editing. The advisory [internal/optimizer/suggest/suggest.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/optimizer/suggest/suggest.go) scores shell history for interactive completion when configured; it is not a deployed forward capability-change controller.

## Operational model

One S1 coding cell receives the user's instruction, chooses from executable tools and observes the results to continue, revise or stop. The optional parent agent can spawn child S1 task units and inspect their outputs, but its delegation/task plan is not automatically a higher-recursion executive. A deterministic process/job manager tracks slots, statuses and cancellation. The user chooses credentials, model, project policy and important approval decisions. Distinct implemented positive S2–S5 organizational ownership and closure must be evidenced separately from these mechanics.

## S1 — Operations

- State: A
- Function: Produce code and analysis by a model-guided sequence of tool uses and result-responsive actions.
- Disturbance / variety regulated: Open-ended project requirements, unknown repository state, failing tools/tests, edit conflicts at the task level and model/tool feedback.
- Decisive decision or feedback right: Choose next task-relevant tool calls and whether/how to revise a response after tool outputs; return a result for the current requested task.
- Decision owner: Model-guided Phi agent loop. Operators authorize task envelope and some effects, deterministic executor implements selected actions.
- Supporting / enforcement mechanisms: Model client, tool registry, session store, typed tools, permission gate, max-round/stop handling, optional MCP/extension and delegated child jobs.
- Closure path: Human prompt → engine/model request → generated tool calls → first-party tool execution → observed outputs in subsequent model context → new action/answer and saved session.
- Boundary reachability: The shipped headless [cmd/runloop.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/cmd/runloop.go) initializes [internal/agent/engine.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/engine.go) and installed tool execution; [internal/agent/executor.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/executor.go) returns ordered observations to the loop. Native tool and model choices are operationally reachable without a custom user-written wrapper.
- Why this is / is not agent-owned: Remove model-selected next steps and the host becomes tools plus a deterministic UI, not an open-ended coding worker. Human approval is a bounded permission owner, not the originator of every intermediate coding choice.
- Evidence: [internal/agent/engine.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/engine.go); [internal/agent/executor.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/executor.go); [cmd/runloop.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/cmd/runloop.go); [internal/tools/tooldef/doc.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/tools/tooldef/doc.go).
- Basis: explicit and structural
- Confidence: high for source-wired coding loop; execution outcome unmeasured
- Caveats: No external live model run or Go source test execution was performed in this inspection environment. Headless Ask is denied if no user prompt interface is present.

## S2 — Coordination

- State: —
- Function: No distinct evidenced inter-S1 conflict-attenuation feedback relationship beyond generic child admission and parent-task routing at the bounded Phi installation.
- Disturbance / variety regulated: Possible competing child workload, shared tool/shell accesses, conflicting edits or approval surfaces.
- Decisive decision or feedback right: A qualifying S2 would arbitrate a specific repeated interference or oscillation among separate S1s and change the losing/waiting unit's subsequent behaviour.
- Decision owner: Not demonstrated. The job manager enforces a static capacity limit and sends ErrBusy when full; model parent decides whether to retry or revise tasks, but this is not an evidenced durable inter-cell return relation.
- Supporting / enforcement mechanisms: Job process slots, MaxConcurrent/MaxDepth, tool-call ordering, serialized individual approval UI, role capabilities and child progress messages.
- Closure path: No function-specific inter-S1 return established: full jobs are rejected, not queued for later capacity release; a parent's request/report is task-level delegation. Parallel read-only tool calls belong to one S1 engine turn.
- Boundary reachability: No positive S2 mode credited. Optional child agent execution is reachable, but a specific interference-attenuation closed loop was not located in supported standard pathways.
- Why this is / is not agent-owned: Limiting worker count, serializing UI events and returning reports do not alone show an S2 organizational conflict and returned attenuation among separate work cells.
- Evidence: [internal/job/manager.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/job/manager.go); [internal/job/manager_test.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/job/manager_test.go); [internal/agent/executor.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/executor.go); [internal/agent/child_spec.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/child_spec.go).
- Basis: structural bounded negative
- Confidence: moderate
- Caveats: A custom higher-level host can build cross-child coordination but is not first-party evidence here.

### Absence scope

- Surfaces inspected: Engine/job manager concurrency and ErrBusy tests, child roles/runner, read-only parallel executor, shared permission and parent results.
- Plausible first-party paths checked: Looked for conflicting sibling claims on common resources with durable hold-and-return, a coordination policy that distinguishes separate S1 units, and influence on their later work.
- Why no material first-party path remains: The first-party limit refuses rather than queues at capacity, and the read-only batching/permission serializations are local execution safety; no supported inter-S1 interference feedback closure established.

## S3 — Inside-and-now control

- State: —
- Function: No materially evidenced whole-installed-system current manager deciding changing shared operational commitments, priorities or resource allocation.
- Disturbance / variety regulated: Resource bottlenecks, pending child work, active sessions, operator interrupts, and project execution errors.
- Decisive decision or feedback right: Whole-current performance/commitment assessment and authoritative cross-cell intervention, returned to affected S1 behaviour.
- Decision owner: Not shown. Deterministic job slots and step limits are enforcement; human chooses tasks/configuration and model parent manages its requested work.
- Supporting / enforcement mechanisms: Job status store, stop/cancel API, maximum concurrent jobs, scoped agent roles, permission modes, user-visible UI.
- Closure path: Job errors or approvals return to one task/parent, without an evidenced portfolio-wide managerial priority/commitment decision and subsequent work rebalancing.
- Boundary reachability: No positive S3 mode credited; shipped TUI/job/session manager and user controls inspected as plausible candidate paths.
- Why this is / is not agent-owned: A per-task model manager and process slot limiter lack demonstrated global management authority over all independently ongoing S1 work.
- Evidence: [internal/job/manager.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/job/manager.go); [internal/agent/jobs.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/jobs.go); [internal/agent/engine.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/engine.go); [cmd/runloop.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/cmd/runloop.go).
- Basis: structural bounded negative
- Confidence: moderate
- Caveats: Human could externally manage a set of Phi installations; that is outside the bundled system.

### Absence scope

- Surfaces inspected: Job monitor/control, statuses/recovery, headless/TUI agent and permission/configuration path.
- Plausible first-party paths checked: Evaluated shared task capacity, reallocation by a whole-system manager, parent-owned priority adjudication and returned correction beyond local tools.
- Why no material first-party path remains: Present features are static resource constraints or per-task control; no dedicated organization-wide current-control decision and return path remains at this scope.

## S3* — Complementary audit

- State: —
- Function: No independent complementary operational audit of the S3 management account with correction fed back to the whole system.
- Disturbance / variety regulated: Misleading completion, inaccurate status, insufficient test evidence and delegated worker mistakes.
- Decisive decision or feedback right: A distinct auditor would inspect independently accessed operational evidence and require corrective current management action.
- Decision owner: No such audit owner found. A model-guided review child is an ordinary task QA role reporting to its parent.
- Supporting / enforcement mechanisms: Reviewer role, read-only diff/tests, job reports, session persistence, deterministic permissions, optional human diff review.
- Closure path: Review worker may report defects for parent to edit, but no autonomous complementary inspection independent from ordinary parent S1 report plus returned S3 corrective decision.
- Boundary reachability: Positive S3* not published; shipped review child mode examined and excluded as task-specific QA rather than a distinct managerial audit relation.
- Why this is / is not agent-owned: Naming an isolated job 'review' does not establish independent reality access, authority or closure to an organization-level S3 control loop.
- Evidence: [internal/agent/child_spec.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/child_spec.go); [internal/job/runner.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/job/runner.go); [internal/job/manager.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/job/manager.go); [internal/agent/engine_runner.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/engine_runner.go).
- Basis: structural bounded negative
- Confidence: moderate-high
- Caveats: A separately governed deployment can compose an independent audit, but no shipped standing S3* loop has been evidenced.

### Absence scope

- Surfaces inspected: Review child role defaults, child engine runner/report, ordinary diff review, job progress and tests.
- Plausible first-party paths checked: Checked for separate independent auditor access, supervisory claim comparison and corrective management owner after finding.
- Why no material first-party path remains: Only per-request code review/job QA can be reconstructed; no distinct independent field-inspection to S3 managerial correction loop is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supported prospectively adapting organization/capability loop over external future conditions.
- Disturbance / variety regulated: Future model/provider/tool conditions and changing kinds of coding work.
- Decisive decision or feedback right: Propose/evaluate future options based on outside environmental intelligence, then authorize/adopt a change in present capability.
- Decision owner: Operator chooses extensions/models and config; the optional 'optimizer' is an advisory current shell-command history completion subsystem, not a future adaptation agent.
- Supporting / enforcement mechanisms: Session history, shell-history suggestion recommender, model switching, project skills/extensions and codebase indexing.
- Closure path: Command completion suggestions update current UI choice; no source-wired outside-and-then option selection/adoption modifying subsequent system capability.
- Boundary reachability: No positive S4 path; optional optimizer and configurable skill/extension path inspected as shipped adjacent mechanisms.
- Why this is / is not agent-owned: A ranking of previously typed bash commands and operator-changed plugins is not a strategic prospective adaptation decision loop.
- Evidence: [internal/optimizer/doc.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/optimizer/doc.go); [internal/optimizer/suggest/suggest.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/optimizer/suggest/suggest.go); [internal/optimizer/features.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/optimizer/features.go); [internal/tui/composer/bash_suggest.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/tui/composer/bash_suggest.go).
- Basis: structural bounded negative
- Confidence: moderate-high
- Caveats: User-authored new features and outside research are excluded from autonomous installed system.

### Absence scope

- Surfaces inspected: Optimizer/backend/suggest and TUI completion, optional skills/extensions, model config and session persistence.
- Plausible first-party paths checked: Tested whether forward environmental signals produce durable adaptation options with an accepted return to deployed policy/capability.
- Why no material first-party path remains: Optimizer is a command suggestion subsystem; extension/config installation is operator action, with no first-party future-intelligence/operational adoption path.

## S5 — Policy and identity

- State: —
- Function: No shipped governing authority establishing or revising the installed agent organization's ultimate identity and purpose.
- Disturbance / variety regulated: Conflict between permissible tool actions, operator rules and enduring organization-level identity/policy.
- Decisive decision or feedback right: Legitimate ultimate policy/identity choice and approved return into organization-wide operation.
- Decision owner: No distinct S5 owner/path evidenced. Operator configures permissions and credentials; static Gate enforces those choices on particular tools.
- Supporting / enforcement mechanisms: Permission Gate/Ask, per-role policies, runtime config, project-specific operating rules, credentials, user confirmation.
- Closure path: Runtime gates affect tool calls and user config affects subsequent launches, but no first-party identity-level deliberation/authority approval and return loop established.
- Boundary reachability: Positive S5 not credited; executable permission gate and config path inspected in supported interactive/headless modes.
- Why this is / is not agent-owned: Runtime policy enforcement and human approval of an individual tool do not establish the organization's ultimate-policy function.
- Evidence: [internal/permission/gate.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/permission/gate.go); [internal/permission/policy.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/permission/policy.go); [internal/agent/executor.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/internal/agent/executor.go); [cmd/runloop.go](https://github.com/pulseaiclub/phi/blob/463c21cccffd4c8b2ee392f7567b094b8fd7b456/cmd/runloop.go).
- Basis: structural bounded negative
- Confidence: moderate
- Caveats: The tool supports operator-owned values, but no separate first-party parent-governed S5 decision-return mode is evidenced.

### Absence scope

- Surfaces inspected: Runtime policy/gate, operator prompts, role capability limits, TUI/headless decisions and configuration/storage.
- Plausible first-party paths checked: Checked potential durable policy issue reaching legitimate parent authority, authorized identity/ultimate-purpose decision and return to all agent work.
- Why no material first-party path remains: Permissions, credential config and per-tool approvals lack a distinct organizational identity/ultimate-policy ownership and feedback cycle.

## Distributed OSS parent arrangement

The public source and shipped end-user self-hosted CLI do not expose an installed distributed principal, quorum or higher-recursion policy/strategy authority. The GitHub development community, upstream models, user skills and plugin SDK authors do not automatically supply a parent VSM function.

## Self-hosted and non-human modes

One user can run the first-party agent/tool loop without approving each read-only step. The operational agent's tool-selection autonomy remains bounded by human-chosen task, credentials, model, gate posture and optional CLI/extension surfaces. No fully non-human S3/S4/S5 mode is evidenced.

## Recursion

The primary coding agent and its optional job children can perform independent assigned operational tasks, but child containment is not a complete recursively viable organization. Job roles and sessions are S1 arrangements at this reviewed installation boundary.

## Variety and escalation

Tool failures, model responses and local repository differences are absorbed at the S1 turn boundary. Permission requests, role restrictions, job limits and exit failures may return task-local signals to the operator or parent model; neither a queued work dashboard nor a red review flag automatically creates an S3 or algedonic organizational channel.

## Evidence gaps

- The delivered Go system was inspected statically at the frozen commit, with first-party tests read as source evidence; Go toolchain and live external model credentials were unavailable on the inspection host, so Phi tests/model tasks were not run here.
- S2 bounded negative applies to the shipped job manager returning ErrBusy, not to hypothetical human-created shared-resource scheduling or plugins that could implement the missing relation.
- Review subagents are task verification; no supported independent managerial audit-to-S3 return was verified. Any future same-ref counterevidence warrants a separate focused re-review.
- The optimizer's name is not interpreted as S4 evidence; the shipped source limits its actual action to interactive shell command suggestions.
