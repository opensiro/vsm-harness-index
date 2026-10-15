---
harness_id: openzot
project_name: OpenZot
repository: https://github.com/openzot/openzot
review_ref: d33ccbe444f25b45c708120d22f42eab961f6b9e
reviewed_at: 2026-10-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenZot

## Review boundary

- System in focus: the first-party Go OpenZot/zot coding-agent engine and shipped local execution product at frozen revision `d33ccbe444f25b45c708120d22f42eab961f6b9e`, with model/tool loop, default read/write/list/shell/plan/progress tools, durable work orders, session recorder/recovery, context/window guards and terminal viewer.
- Purpose and identity: carry one or more operator-authored durable coding work orders through autonomous model-directed local code inspection/editing/execution and record the declared result.
- Relevant environment: work order objectives, acceptance criteria and constraints, repository/worktree, shell/tool results, configured provider responses, resource limits, external skills, context-window pressure and saved prior session state.
- Standard-distribution boundary: shipped `agent` and `internal/loop` execution, work-order parser/runner, tool set, session recorder, config/skills and CLI/TUI entry point. Model service, operator-defined order contents, user-created skills, shell-launched independent processes, other products using the importable agent package and arbitrary external tooling are not first-party VSM decision owners.
- Credited operating / distribution surfaces: `agent/agent.go`, `agent/tools.go`, `internal/loop/loop.go`, `internal/order/order.go`, `internal/order/record.go`, `internal/session/recorder.go`, `agent/skills.go`, CLI and terminal viewer, plus released-mode configs.
- Adjacent first-party surfaces excluded from ownership: tests/CI/releases, developer governance, standalone Rook project and user-authored orchestration/quality-control skills. Product roadmap and descriptions cannot donate an implemented runtime function.
- First-party operating / deployment modes considered: ordinary autonomous work-order run, multiple queued YAML orders dispatched by CLI, resumed saved session, embedded/imported `agent` API, optional dynamic skills/model, Docker confinement and shell-mediated child invocation. The last is a generic tool capability, not a bundled supervisor or collaboration policy.
- Recursion level: a single zot model/tool run and its ordinary work-order dispatch context. A shell-launched child may be another zot S1 instance when actually invoked, but no full child metasystem or first-party coordination is inferred from self-invocation alone.
- Reviewed revision: `d33ccbe444f25b45c708120d22f42eab961f6b9e` (unchanged frozen intake #898).
- Observation date: 2026-10-14.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

OpenZot's first-party `agent.ExecuteWithTools` composes `internal/loop.Engine` with a provider client, task instructions, the default tool set, bounded budgets and optional session recording. The engine requests model continuations with tool schemas, dispatches selected tool handlers, appends observations and continues until the model invokes a terminal outcome tool or resource/safety guards stop the run. Its built-in tools include file `read`, `write`, `list`, command `shell`, `plan` and `progress` (with optional image `view`). They implement the actual repository-facing work, rather than delegating coding to an imported coding-agent CLI.

Work orders are YAML with durable `objective`, `acceptance` and `constraints`. Their values enter the system prompt; they are **advisory task inputs**, not themselves authority for independent quality judgments. `internal/order/order.go` explicitly excludes quality gates from its schema and assigns adjudication to operator configuration. The work-order CLI can dispatch multiple records, but file order, progress reporting and terminal outcome storage are not evidence that a whole-system agent governs interacting autonomous divisions. Session logs/resume and context compaction preserve task history under long execution and provider failures, not organizational future adaptation.

The shipped engine explicitly has **no native sub-agent primitive**. The `shell` tool may invoke another `zot` process with a fresh work order; inter-agent communication is left to whatever user workspace/skill conventions exist. This capability is not a first-party collision-arbitration or subordinate current-control organization. In settle mode, the engine confirms that a model **declared** success/failure; `docs/how-it-works.md` explicitly says zot does **not** independently verify that the work was done or independently gate results. Container hardening and external tooling do not change that boundary.

Primary evidence: [README.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/README.md), [docs/how-it-works.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/how-it-works.md), [docs/orders.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/orders.md), [docs/safety.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/safety.md), [agent/agent.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/agent.go), [agent/tools.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/tools.go), [internal/loop/loop.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/loop/loop.go), [internal/order/order.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/order/order.go), [internal/session/recorder.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/session/recorder.go), [agent/skills.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/skills.go).

## Operational model

One model-backed work-cell drives the open-ended work-order plan→action→observation→revision loop. Its goals and acceptance conditions come from an operator-supplied order; the model controls which tools to use and how to react to environmental evidence until it declares an outcome. The persistent records and TUI expose activity without granting additional supervisory discretion. The independent quality gate described in future-looking documentation is not shipped and cannot be credited as S3*.

## S1 — Operations

- State: A
- Function: decide and perform task-specific coding actions against a repository until a work-order outcome is declared or runtime limits stop execution.
- Disturbance / variety regulated: varied repository/task state, shell/tool failures, changing partial work, provider responses, failed actions, context pressure and detected loops.
- Decisive decision or feedback right: choose read/write/shell/plan/progress actions, their parameters and subsequent revisions from observed results; choose when to declare task success/failure through the terminal tool.
- Decision owner: the model-backed zot agent running inside the first-party `agent.ExecuteWithTools` and `loop.Engine`; the external provider does inference but does not own the operating harness/tool feedback organization.
- Supporting / enforcement mechanisms: default `agent.Tools`, work-order prompt, session history and recorder, thread packing, compaction, guard counters and configurable budgets.
- Closure path: work order + current context → model chooses task-specific tool action → first-party tool executes → returned result enters conversation → model revises next action or declares outcome.
- Boundary reachability: the public CLI and `agent` package both instantiate the shipped first-party model/tool loop with real file/shell tools; no adjacent coding agent is needed.
- Why this is / is not agent-owned: absent the model's discretionary tool choice, deterministic YAML/order parsing, guard checks and event logging cannot decide how to carry out the coding objective.
- Evidence: [agent/agent.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/agent.go), [agent/tools.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/tools.go), [internal/loop/loop.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/loop/loop.go), [docs/how-it-works.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/how-it-works.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: outcome declaration is not independent acceptance verification; autonomous file/shell access is powerful and not sandboxed by `--dir` alone.

## S2 — Coordination

- State: —
- Function: no standard first-party inter-S1 interference attenuation and feedback relation established.
- Disturbance / variety regulated: hypothetical write contention, shared-resource conflicts or oscillations between nested/parallel agents.
- Decisive decision or feedback right: no shipped S2-specific intervention right over competing subordinate S1 actions was found.
- Decision owner: none established for a distinct coordination function.
- Supporting / enforcement mechanisms: work-order listing/dispatch, model-selected shell invocation, workspace files and optional user-authored skills; these do not themselves arbitrate agent conflicts.
- Closure path: ordinary child shell output can return to the calling agent; no first-party inter-S1 disturbance → arbitration/attenuation → changed subsequent operations path is installed.
- Why this is / is not agent-owned: generic shell/subprocess delegation does not make a coordinated system; supplying a file protocol or communication convention is delegated to users.
- Evidence: [docs/how-it-works.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/how-it-works.md), [agent/tools.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/tools.go), [internal/order/order.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/order/order.go), [agent/agent.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/agent.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: novel user-authored skills may coordinate separate instances, but they are not a standard-distribution first-party S2 witness.

### Absence scope

- Surfaces inspected: public agent loop, default tools, work-order dispatch, CLI boundaries, first-party skills mechanism and explicit architecture documentation.
- Plausible first-party paths checked: shell-spawned zot, multiple order files, shared filesystem, per-run budgets, user-authored queue/messaging patterns and code-level subagent/supervisor entry points.
- Why no material first-party path remains: shipped runtime expressly supplies no native subagent, supervisor, message bus or organizational conflict-control contract. Potential user-defined protocols cannot be imported as its own concrete corrective S2 closure.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current operations view with distinct resource/priority/commitment intervention and feedback for an organized set of S1s.
- Disturbance / variety regulated: competing work-order priorities, progress bottlenecks, current multi-run performance and resource contention if a supervisory level existed.
- Decisive decision or feedback right: the coding model can plan and record progress for its assigned work order; the CLI runs configured orders, but neither owns an evidenced cross-run current-control decision path.
- Decision owner: the task model for one S1 and operator/CLI input for order selection, not an autonomous current-operations S3.
- Supporting / enforcement mechanisms: `plan`/`progress` tools, work-order YAML/records, session recorder, guard counters and read-only terminal viewer.
- Closure path: S1 plan and progress affect one agent's next steps; no combined current population observation → substantive cross-unit reprioritization/intervention → confirmed operational return is shipped.
- Why this is / is not agent-owned: progress tools are recording/reporting mechanisms; the viewer supplies no decision rights, and sequential order dispatch is not independent management.
- Evidence: [docs/orders.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/orders.md), [docs/how-it-works.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/how-it-works.md), [agent/tools.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/tools.go), [internal/order/order.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/order/order.go), [internal/session/recorder.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/session/recorder.go).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: a separate automation platform around zot could construct S3, outside the assessed product.

### Absence scope

- Surfaces inspected: main command/order-list runner, current model loop, plan/progress handlers, records/session UI and documented subagent design.
- Plausible first-party paths checked: order batches, durable activity ledger, concurrent jobs, shell children, operator viewer, resources/budgets and priority/commitment update.
- Why no material first-party path remains: current-progress data are per run, and no shipped actor uses a whole-multi-S1 view to decide material current obligations, allocate resources or send corrective instructions to independent worker units.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary independent evidentiary check of a worker's outcome, followed by corrective return to operations, is instantiated.
- Disturbance / variety regulated: unobserved code errors and falsely declared completion would be the audit target.
- Claim being audited: that a completed work order meets its acceptance criteria and constraints.
- Ordinary reporting path: the same model may run shell tests and then declare a terminal `success` or `failure`.
- Complementary access path: not established in the shipped product; settle mode checks the declared terminal tool, not independent truth of the outcome.
- Independence boundary: no distinct deployed audit owner is connected to the standard execution loop; independently rerunning a second zot via user-authored skill would require supplied operational organization outside the baseline.
- Who acts on findings: no shipped separate checker produces findings for the S1 model or an organizational controller to act upon.
- Decisive decision or feedback right: model owns its own terminal claim, and any future or user-supplied external gate owns its own judgment; neither proves first-party complementary audit ownership.
- Decision owner: none identified for shipped S3*.
- Supporting / enforcement mechanisms: outcome-settle tool, acceptance text in work order, possible self-run tests, records and external optional skills.
- Closure path: absent; there is no independent direct-evidence challenge → differentiated judgment → feedback altering current corrective control.
- Why this is / is not agent-owned: checking that the agent *said* it was finished does not adjudicate whether the result is correct.
- Evidence: [docs/how-it-works.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/how-it-works.md), [internal/order/order.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/order/order.go), [agent/agent.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/agent.go), [internal/loop/loop.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/loop/loop.go).
- Basis: explicit negative + structural.
- Confidence: high.
- Caveats: the documentation describes possible user-authored reviewer workflows, excluded without a shipped bounded witness.

### Absence scope

- Surfaces inspected: terminal outcome loop/settle mode, work-order acceptance model, tools, session records, possible shell self-delegation and docs on no native subagents.
- Plausible first-party paths checked: acceptance checks, model-self testing, automatic test repair, resume, independent review invocation, separate evidence reader and return of findings.
- Why no material first-party path remains: the implementer and outcome declarer are the same ordinary S1; documentation explicitly disclaims an independent gate, and any further review requires constructing a user-specific pipeline rather than invoking a bundled complementary auditor.

## S4 — Outside-and-then intelligence

- State: —
- Function: no current shipped prospective environment-learning and capability-adaptation decision loop for the zot organization.
- Disturbance / variety regulated: external tools, future software needs, shifting model/provider capabilities and reusable skill discovery.
- Decisive decision or feedback right: dynamic skill descriptions can enter a running prompt, but no first-party capability investment/selection and cross-operation adoption decision is supplied.
- Decision owner: model for the current coding task and operator for installed skills/configuration; none proven for S4.
- Supporting / enforcement mechanisms: `SkillLoader.Skills` rescans local skill folders each iteration, optional model-authored file content, provider configuration, compaction and session resume.
- Closure path: new local instructions can become available for current work; no bounded future external distinction → evaluated option → accepted organizational capability update returned to current control is evidenced.
- Why this is / is not agent-owned: making a skill readable mid-run is a context-loading mechanism; it does not establish prospective S4 governance or durable adoption authority.
- Evidence: [agent/skills.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/skills.go), [internal/loop/loop.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/loop/loop.go), [docs/how-it-works.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/how-it-works.md), [docs/configuration.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/configuration.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: first-party dynamic skill discovery is a real extensibility mechanism but must not be conflated with a closed S4 adaptation organization.

### Absence scope

- Surfaces inspected: skill discovery/loaders, provider/tool abstractions, model loop, work orders, memory/resume/compaction, public orchestration guidance.
- Plausible first-party paths checked: agent-created new skill files, newly found instructions at the next turn, changing models/providers, plan adjustments and work-order reruns.
- Why no material first-party path remains: possible instructions arrive as ordinary prompt inputs; no separately owned future environment analysis or explicit adoption/withdrawal feedback process over the organization's capabilities exists in the pinned first-party runtime.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate-purpose/identity dispute-resolution path with authoritative policy return is evidenced.
- Disturbance / variety regulated: competing task safety/quality goals and user-defined task constraints.
- Decisive decision or feedback right: operators specify work orders, acceptance constraints and process permissions; the model acts within these inputs but does not decide organizational identity or ultimate policy.
- Decision owner: operator/configuration, external to a shipped S5 closure.
- Supporting / enforcement mechanisms: order schema and constraints, shell privileges, config policies, provider credentials, optional container isolation and instructions.
- Closure path: ordinary objective/constraint text guides a task and records the result; no ultimate-identity issue → legitimate authority judgment → returned durable policy change is provided.
- Why this is / is not agent-owned: current operational autonomy does not grant the model the right to rewrite who zot is or whose authority governs the work.
- Evidence: [internal/order/order.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/internal/order/order.go), [docs/orders.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/orders.md), [docs/safety.md](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/docs/safety.md), [agent/agent.go](https://github.com/openzot/openzot/blob/d33ccbe444f25b45c708120d22f42eab961f6b9e/agent/agent.go).
- Basis: structural.
- Confidence: high.
- Caveats: human-designed quality/safety boundaries are real, but are not evidence for first-party VSM S5.

### Absence scope

- Surfaces inspected: order contract and acceptance constraints, current loop safety/termination rules, public safety doc, CLI configuration, model instructions and developer/governance adjacency.
- Plausible first-party paths checked: operator reconfigures run, agent edits order/skill, changes acceptance condition, project-level configuration and container policy.
- Why no material first-party path remains: all demonstrated paths author or enforce routine tasks and execution constraints; none supplies durable legitimate identity policy jurisdiction and corrective return at the selected recursion.

## Distributed OSS parent arrangement

Not evidenced at this runtime boundary. The public upstream maintainers and separate Rook product are independent organizations, not automatically a parent VSM inside a local zot work-order run.

## Self-hosted and non-human modes

The product runs unattended and locally; the terminal viewer is read-only, while provider inference is external. Docker confines a process but provides external OS/security mechanism, not a new agent-owned VSM function. No parent-governed `P` or `A(P)` state is asserted.

## Recursion

A zot agent may execute another zot via its ordinary shell tool. That is an optional first-party code path to another S1 loop with its own task/environment, but no built-in nested S2–S5 organization or recursive viable-system closure is established from the invocation alone.

## Variety and escalation

The model and tools absorb repository variety; context guards, loop detection, token/iteration limits, work-order constraints and external sandboxing attenuate execution variety. A model-declared result or runtime stop is recorded, but the standard product does not contain an independent acceptance audit or an organizational policy-algedonic escalation chain.

## Evidence gaps

- The existence of shell-mediated self-invocation is not evidence of a shipped cross-S1 coordination/management arrangement; a separately pinned bundled skill could change that conclusion in another explicit assessment boundary.
- Dynamic skill exposure is real but lacks a prospective adoption/right-to-update control loop; later code could establish an S4 path.
- Settle-mode success/failure declares rather than independently verifies acceptance; a user-authored reviewer or external CI cannot be credited to zot's first-party standard distribution.
- No executable runtime benchmark was run in this assessment; conclusions are source-first structural claims restricted to the pinned review ref.
