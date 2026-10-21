---
harness_id: gopi
project_name: Gopi
repository: https://github.com/cgund98/gopi
review_ref: c5aaae8acc169c9c0a0d6c7a1a872074515cb485
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Gopi

**Proposed, noncanonical general assessment** for [Index batch #1842](https://github.com/opensiro/vsm-harness-index/issues/1842), row 8, original frozen intake [#860](https://github.com/opensiro/vsm-harness-index/issues/860). Vector `A / — / — / — / — / —` is bounded first-party source review, not live benchmark performance.

## Review boundary

- System in focus: Standard Go terminal coding agent `gopi` shipped CLI/application in a user's local workspace.
- Purpose and identity: Model-guided coding/editing and workspace investigation under explicit local permissions, with bounded read-only delegated subtasks.
- Relevant environment: Project workspace, shell sandbox, local secrets/trust, external model provider, optional user-provided compiled custom tools, terminal UI.
- Standard-distribution boundary: First-party Go CLI, public gopi.Run, app.New session/wiring, model/tool registration and shipped workspace tools at frozen commit; transitive gogent runtime is invoked, not promoted into a separate organization.
- Credited operating / distribution surfaces: [gopi.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/gopi.go), [cmd/gopi/main.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/cmd/gopi/main.go), [internal/app/app.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/app.go), [internal/app/factory.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/factory.go), [internal/tools/delegate.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/delegate.go), [internal/tools/edit.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/edit.go), [internal/tools/tasks.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/tasks.go), [internal/tools/tasklist.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/tasklist.go), [internal/tools/shell.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/shell.go), [internal/policy/policy.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/policy/policy.go).
- Adjacent first-party surfaces excluded from ownership: [.github/workflows/ci.yml](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/.github/workflows/ci.yml), [AGENTS.md](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/AGENTS.md), [docs/src/index.md](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/docs/src/index.md) as contributor/CI/reference documentation when describing developer governance. Uninstalled gopi-tools module and arbitrary user code/Go embedding are not first-party decision owners at the assessed installed boundary.
- First-party operating / deployment modes considered: default interactive agent, ask/plan modes, embedded Run with optional user tools, read-only child delegation, per-call approval, resume/session storage and diff review.
- Recursion level: One coding agent/workspace installation, optional read-only child work cells with fixed local budget and returned parent result; no automatic higher viable recursion.
- Reviewed revision: [cgund98/gopi@c5aaae8acc169c9c0a0d6c7a1a872074515cb485](https://github.com/cgund98/gopi/tree/c5aaae8acc169c9c0a0d6c7a1a872074515cb485)
- Observation date: 2026-10-22
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The distributed [cmd/gopi/main.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/cmd/gopi/main.go) CLI calls the first-party [gopi.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/gopi.go) application path. [internal/app/app.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/app.go) constructs a usable workspace coding agent by composing an external gogent loop with first-party model factory, tool registry, prompt, file tools and sandbox/trust policy. Model-generated operations can read files, edit, run sandboxed commands, update task/plan state and receive observations. [internal/tools/delegate.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/delegate.go) creates an in-memory limited child model loop with only read/grep/find/sandboxed shell, returning a synchronous text answer; `allowCall()` enforces a finite count and rejects additional calls rather than queuing sibling work. [internal/tools/tasklist.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/tasklist.go) tracks local project steps; [internal/review/diff.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/review/diff.go) and terminal review support user acceptance or revert of edited hunks. Permissions/redaction are first-party security support; optional downstream tools and CI release automation are not organizational S3–S5 owners.

## Operational model

A user authorizes a coding request, installed model-host loop chooses tools and subsequent actions from results. A child delegated research task can be launched through the main tool registry; returned text informs the parent's next coding step. The read-only child is not independently doing concurrent shared-file edits and does not gain permission escalation. First-party security and user code review govern effects, but organizational functions must be established separately before assigning S2–S5.

## S1 — Operations

- State: A
- Function: Execute operator-requested coding and workspace investigation through model-guided, feedback-responsive tool use.
- Disturbance / variety regulated: Open-ended coding requests, unknown repository code, shell errors, file edits and test feedback.
- Decisive decision or feedback right: Choose tool calls and subsequent actions based on observations, concluding or revising the task.
- Decision owner: Installed model-guided gopi session via the gogent agent constructor; the model chooses coding operations; first-party gopi tool wrappers and operator permission govern effects.
- Supporting / enforcement mechanisms: Go CLI/TUI, first-party app mode registries and model factory, tool adapters, workspace/sandbox permissions, session persistence, tool result and prompt composition.
- Closure path: User instruction enters gopi's installed session → model-generated tool request executes through first-party registry/tool wrappers → resulting observations are returned to the running agent → later tool/response is selected.
- Boundary reachability: The shipped cmd/gopi binary uses public gopi.Run and internal/app.New to wire a gogent model loop with concrete workspace tools. Although gogent is a dependency, the first-party distributed gopi CLI makes the coding behavior reachable without writing another host.
- Why this is / is not agent-owned: Without the model's tool choice and observation-responsive actions, tools/terminal UI cannot autonomously do open-ended coding; permission controls constrain effect rights without choosing task actions.
- Evidence: [README.md](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/README.md); [gopi.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/gopi.go); [cmd/gopi/main.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/cmd/gopi/main.go); [internal/app/app.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/app.go); [internal/app/factory.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/factory.go); [internal/tools/edit.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/edit.go); [internal/tools/shell.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/shell.go)
- Basis: explicit and structural
- Confidence: high for source-wired operations, without live model execution
- Caveats: Source-only evidence; Go native unit tests and provider-backed runs not executed in this inspection environment.

## S2 — Coordination

- State: —
- Function: No material first-party inter-S1 interference regulator with a returned coordination decision is established at this local session boundary.
- Disturbance / variety regulated: Possible competition among delegated child investigations for bounded session allowance, shared resources or workspace state.
- Decisive decision or feedback right: Would need distinguish multiple actual S1 units, prevent conflict/oscillation and return an attenuation decision to later behavior of affected S1s.
- Decision owner: Not established; the main session can delegate a bounded read-only investigation and the tool's mutex merely increments an overall call budget.
- Supporting / enforcement mechanisms: Delegate MaxCalls, iterations, timeout, in-memory child loop, read-only registry, failClosed wrapper, progress status and tasklist.
- Closure path: Single synchronous delegate tool call runs a read-only child, waits for the resulting answer and returns it to the parent as an observation; when MaxCalls is exceeded the next call is rejected, with no queued conflicting S1 awaiting a later release.
- Boundary reachability: Subagent delegation is shipped but a function-specific positive inter-S1 homeostatic mode was not found.
- Why this is / is not agent-owned: Calling separate child investigative agents, sharing task records, limiting subagent count, enforcing security or returning an answer are not evidence of interference attenuation and a coordination feedback relation.
- Evidence: [internal/tools/delegate.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/delegate.go); [internal/tools/delegate_progress.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/delegate_progress.go); [internal/tools/delegate_test.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/delegate_test.go); [internal/tools/tasks.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/tasks.go); [internal/app/app.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/app.go)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: Source-only evidence; Go native unit tests and provider-backed runs not executed in this inspection environment.

### Absence scope

- Surfaces inspected: Concrete app.New registration and Delegate tool Execute, allowance mutex/call counter, child read-only sandbox/grants, progress and task/plan store.
- Plausible first-party paths checked: Concurrent distinct S1 contention, conflict-specific arbitration/wait/release, sibling feedback affecting subsequent operational behavior.
- Why no material first-party path remains: Delegate uses a task-local synchronous read-only child and denies additional calls at a fixed limit, without a first-party inter-S1 collision mitigation path or a returned decision to competing child units.

## S3 — Inside-and-now control

- State: —
- Function: No evidenced whole-current management of organizational commitments, competing S1 resources or priorities at the installed session boundary.
- Disturbance / variety regulated: Multiple active coding operations, resource limits, task priority, model/provider choices and permission requests.
- Decisive decision or feedback right: Would require a whole-system current view and decisive manager choice to change shared resources, commitments, accountability or priorities with feedback into ongoing S1 work.
- Decision owner: Not demonstrated; operator selects modes/model/trust and the main model works on one task. TaskList contains ordinary task status, and delegate budget is enforcement.
- Supporting / enforcement mechanisms: TaskList and Tasks, editable plan, app session modes, config/trust, budgeted child execution, progress display and terminal UI.
- Closure path: Task status and plans may change the local work sequence; no separate whole-system resource/commitment current-control action is returned across independent operations.
- Boundary reachability: No positive S3 loop in shipped app/session/task/delegation modes inspected.
- Why this is / is not agent-owned: A single-agent task plan, progress display, and deterministic budget gate are not an S3 manager independent of a local task.
- Evidence: [internal/app/app.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/app.go); [internal/tools/tasklist.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/tasklist.go); [internal/tools/tasks.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/tasks.go); [internal/tools/plan.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/plan.go); [internal/tools/delegate.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/delegate.go)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: Source-only evidence; Go native unit tests and provider-backed runs not executed in this inspection environment.

### Absence scope

- Surfaces inspected: Task-list update/persist, app mode switching, delegation caps, session state and TUI work status.
- Plausible first-party paths checked: Portfolio-wide manager view, choices over cross-S1 commitments and return of interventions into multiple cells.
- Why no material first-party path remains: Inspected paths are local task bookkeeping, mode selection and deterministic tool bounds; no separate S3 organizational decision and return path found.

## S3* — Complementary audit

- State: —
- Function: No independent complementary inspection of a whole-current S3 management account and corrective managerial return is shipped.
- Disturbance / variety regulated: Edits that do not match a requested change, incomplete task results, false reporting and unreviewed code modifications.
- Decisive decision or feedback right: A qualifying independent auditor would inspect reality separately from ordinary S3 reporting, make audit judgments about S3 control and feed findings into an accountable current-management correction.
- Decision owner: Operator is entitled to review/reject individual code hunks, not shown as first-party manager-account auditor.
- Supporting / enforcement mechanisms: User-facing /review diff/hunk UI, saved edit state, tests and optional delegated investigator.
- Closure path: A rejected patch hunk reverts a code edit; this closes editing quality/permission, not the independent audit → S3 managerial correction loop.
- Boundary reachability: The review UI is shipped and reachable, but does not meet S3* function/independence threshold at the assessed recursion.
- Why this is / is not agent-owned: Human QA or a separate child read of code is not a complementary audit of current organizational management.
- Evidence: [README.md](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/README.md); [internal/review/diff.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/review/diff.go); [internal/session/store.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/session/store.go); [internal/tools/edit.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/edit.go); [internal/tools/delegate.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/delegate.go)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: Source-only evidence; Go native unit tests and provider-backed runs not executed in this inspection environment.

### Absence scope

- Surfaces inspected: Runtime /review and diff acceptance, session saved changes, separate delegate reports and UI review docs.
- Plausible first-party paths checked: Auditor's separately acquired information about S3 management claims, independence from routine manager reporting, corrective management decision loop.
- Why no material first-party path remains: Reviewed code-quality/hunk approval is task implementation oversight and no qualified independent S3 managerial inspection owner or feedback path is wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environment intelligence loop selects and installs changes to future operational capability.
- Disturbance / variety regulated: Future user/project changes, external models, tool ecosystem evolution and shifting requirements.
- Decisive decision or feedback right: Choose and adopt an adaptation option based on outside-and-future conditions, with an accepted return into later capability.
- Decision owner: Not established; developer publishes versions and operator configures model, extensions and user instructions.
- Supporting / enforcement mechanisms: Prompt assembler, mode/tool customization, external gopi-tools module and model config, session history and planning.
- Closure path: Configuration and optional added tools can change a user's installation, but source does not independently select a future capability/adaptation from prospective external intelligence and return it into subsequent operation.
- Boundary reachability: No accepted first-party S4 path in standard shipped runtime; custom compiled tools and maintainers' roadmap outside assessed ownership.
- Why this is / is not agent-owned: Having a plugin host, task plan or saved transcript is enabling machinery, not S4 unless prospective intelligence and adoption are operationally closed.
- Evidence: [gopi.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/gopi.go); [internal/prompt/assemble.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/prompt/assemble.go); [internal/app/app.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/app.go); [internal/app/factory.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/app/factory.go); [internal/config/config.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/config/config.go)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: Source-only evidence; Go native unit tests and provider-backed runs not executed in this inspection environment.

### Absence scope

- Surfaces inspected: First-party tool extension registration, prompt assembly, config/mode handling, task planning, session memory and public docs.
- Plausible first-party paths checked: Outside prospective assessment, selected strategic adaptation options and their return into current/future installed capability.
- Why no material first-party path remains: No shipped path evaluating a future operating environment and adopting a different durable organizational arrangement; extensibility is user/developer controlled.

## S5 — Policy and identity

- State: —
- Function: No complete first-party runtime identity/ultimate-policy decision owner and returned organizational governance choice established.
- Disturbance / variety regulated: Sensitive workspace data, secret use, sandbox widening, network permissions and untrusted project instructions.
- Decisive decision or feedback right: A qualifying S5 owner would settle an ultimate identity/policy issue as legitimate authority and return an authoritative decision governing later system operation.
- Decision owner: Operator controls credentials/trust/approvals and compiled policy supplies enforcement; they are not evidenced as closing a distinct installed S5 governing loop.
- Supporting / enforcement mechanisms: Protected read grants, trust workspace boundaries, sandbox fail-closed execution, per-call elevation approvals, network allow/deny, secret redaction.
- Closure path: Individual protected operation → operator approval or denial → one tool is allowed/blocked; this is task effect authorization, not organizational identity/policy question → ultimate legitimacy judgment → binding organizational return.
- Boundary reachability: No positive S5 ownership mode; permission and sandbox paths are present but support lower-level constraint enforcement.
- Why this is / is not agent-owned: Strong sandboxing and human approval of an individual sensitive operation are not, by themselves, ultimate identity governance. No generic human P inference.
- Evidence: [internal/policy/policy.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/policy/policy.go); [internal/trust/trust.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/trust/trust.go); [internal/tools/grants.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/grants.go); [internal/tools/elevate.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/tools/elevate.go); [internal/sandbox/run.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/sandbox/run.go); [internal/secrets/secrets.go](https://github.com/cgund98/gopi/blob/c5aaae8acc169c9c0a0d6c7a1a872074515cb485/internal/secrets/secrets.go)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: Source-only evidence; Go native unit tests and provider-backed runs not executed in this inspection environment.

### Absence scope

- Surfaces inspected: Protected path rules, trust grants, shell sandbox, per-call approval, tool elevation, user CLI settings and credential handling.
- Plausible first-party paths checked: Identity/ultimate policy dilemma, legitimate decisive parent/system authority, and subsequent organizational governance return.
- Why no material first-party path remains: Observed decisions concern access for individual effectful tools or user configuration; there is no distinct first-party ultimate-policy decision cycle with organization-level closure.

## Recursion

The installed coding agent is the system in focus. Read-only spawned agents are model-guided task subunits, not evidence of organizational recursion or separately legitimate S5.

## Variety and escalation

Workspace/tool errors and ambiguous coding tasks are regulated by S1 tool feedback. Limits, secret protection and approval requests are tool-local control and escalation to the user, not a new VSM function absent specific closed organizational authority.

## Evidence gaps

1. Go runtime absent in this inspection environment; cited tests were inspected as code, not executed. No real external provider task success or deploy trace claimed.
2. The gogent dependency is an executable tool-loop dependency wired by first-party code; no unspecified gogent advanced organizational functions are borrowed.
3. Optional downstream gopi-tools/custom agents and unknown private deployments could extend functions, but are outside first-party standard distribution and cannot upgrade this assessment.
