---
harness_id: bough
project_name: Bough
repository: https://github.com/andreylukin/bough
review_ref: 18d07fe115e6ca872273d40d7cedc0881af4561e
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

# Bough

**Canonical general assessment** for Index batch [#1842](https://github.com/opensiro/vsm-harness-index/issues/1842), row 1, sourced from immutable intake [#860](https://github.com/opensiro/vsm-harness-index/issues/860). The function evidence and boundary are accepted for this exact frozen source revision. No live provider session, developer-performance benchmark, or Bough Go tests were run as part of this inspection; the inspected host did not have a Go executable.

## Review boundary

- System in focus: Bough's shipped, self-hosted terminal/headless/web coding-agent runtime and first-party model/tool feedback, child-agent execution, history, hooks, project isolation, and background-agent supervisor.
- Purpose and identity: Let a model inspect and modify code through owned tools and return results in local or optionally isolated project workspaces.
- Relevant environment: Human prompts and permission/configuration choices; repository source, shell/tool responses, model API providers; optional MCP services and container runtimes.
- Standard-distribution boundary: Source-shipped Go binary and embedded `go/bough.yml`; default `engine-unreal` native tool-call engine, selectable first-party `loop` code-mode implementation; local, headless, web and project modes. Background children require `bough serve`. Features behind explicit installed/operator configuration are evaluated only for their evidenced reachable modes, never presumed always on.
- Credited operating / distribution surfaces: `go/cmd/bough`, `go/bough.yml`, `go/plugins/engine`, `go/plugins/loop`, `go/plugins/workers`, `go/plugins/llm`, `go/plugins/codemode`, `go/plugins/tools`, `go/plugins/history`, `go/plugins/hooks`, `go/plugins/orb`, `go/internal/serve`, `go/plugins/wiki` to the extent they are wired to shipped runtime.
- Adjacent first-party surfaces excluded from ownership: Repository CI/workflows, maintainer dogfooding/usage statistics, source tests and fuzz/model benchmarks, demo recordings, install/release jobs, README performance anecdotes and generated wiki prose considered as independent strategic governance. External model reasoning is credited only through Bough's first-party dispatch/feedback loop, not as Bough-owned organizational policy.
- First-party operating / deployment modes considered: Native-tool default; selectable first-party code-mode; terminal and headless; `bough serve` background child agents; project/orb isolation; optional scheduled wiki ingestion. No unstated active always-on instance presumed.
- Recursion level: One installed Bough agent-and-child-work system for a user's coding tasks. Child agent processes are S1 task units in the coordinated background mode; separate operator installations are not assumed one global enterprise VSM recursion.
- Reviewed revision: `andreylukin/bough@18d07fe115e6ca872273d40d7cedc0881af4561e` (the exact pinned source checkout).
- Observation date: 2026-10-21.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Bough is a first-party Go coding agent, not merely a prompt pack or wrapper around an outside agent process. The distributed plugin graph selects an LLM provider, tool registry, history, workers, safety hooks and an engine. Importantly, `go/bough.yml` currently selects `engine-unreal` (native calls) by default, while the separately shipped `loop` implements code-mode `LLM → JavaScript block → tool execution → returned output`; these are alternative execution modes, not evidence that code-mode is always active. Model providers are external decision substrates; Bough owns the executable integration, turn dispatch, tool-result feedback and stopping/cancellation paths. [go/bough.yml](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/bough.yml); [go/plugins/engine/engine.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/engine/engine.go); [go/plugins/loop/loop.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/loop/loop.go); [go/plugins/codemode/codemode.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/codemode/codemode.go).

The standard workers plugin exposes bounded, model-driven synchronous children (`spawn`/`spawnAll`) and independently launched background children through the first-party `serve` supervisor. The background path has a running limit, FIFO queue, persistent pending tasks, restart recovery, parent-bound result notification and stopping. Project-orb mode optionally uses isolated Git worktrees/containers, but a local shell is explicitly not a generic enforced sandbox. Session state is append-only history; `wiki` optionally summarizes old sessions into evidence-linked notes, not automatically injected governing policy. [go/plugins/workers/workers.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/workers/workers.go); [go/plugins/workers/background.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/workers/background.go); [go/internal/serve/children.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/internal/serve/children.go); [go/internal/serve/supervisor.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/internal/serve/supervisor.go); [go/plugins/wiki/run.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/wiki/run.go); [README.md](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/README.md).

## Operational model

The model-guided agent owns coding-turn semantic discretion: inspect/patch/test, select subsequent tool actions based on observations and terminate/report. The native or code-mode runner, tool registry, limits, sandbox options, and human prompts configure/enforce rather than independently decide what fix to attempt. In the `bough serve` mode, simultaneously dispatched background coding agents are distinct S1 task processes competing for a *shared finite* background execution capacity. The shipped supervisor deterministically damps that concrete competition, and on slot release starts a queued child and returns child results to the parent. No first-party whole-organization management or policy constitution is inferred from this lower-level coordination.

## S1 — Operations

- State: A
- Function: Perform model-guided coding and repository operations by selecting tool actions, observing results, correcting a plan/edit and returning task results.
- Disturbance / variety regulated: Open-ended code/problem requirements; failures and outputs of file, shell, test and external-tool actions; changed context during execution.
- Decisive decision or feedback right: The agent's model selects which first-party tool actions or code programs to execute next in response to observations, rather than a developer-encoded fixed workflow supplying every semantic step.
- Decision owner: Model-guided agent in the installed Bough runtime; Bough runner executes and reports its decisions. Providers supply inference but are not an independently credited organizational owner.
- Supporting / enforcement mechanisms: Shipped `engine-unreal` runner, native tool registry, optional code-mode VM, history projection, filesystem/search/bash tools, permissions/hooks and human-configured runtime boundaries.
- Closure path: Human task → Bough native engine or selected first-party code loop → model tool/code decision → tool execution → returned result/observation → next model decision or final reply, with history and cancellation recorded.
- Boundary reachability: Default `go/bough.yml` mounts `engine-unreal` and agent-tools, `engine.go` constructs and runs the session through `Submit`, tool responses wake the model; the alternate `loop.go::Run` is also packaged and selectable, not imported from an external product.
- Why this is / is not agent-owned: With the model removed the runtime can register tools and enforce bounds but cannot choose task-semantic coding/edit actions in response to novel evidence. This is a supported autonomous S1 path, not a claim of successful unsupervised software delivery.
- Evidence: [go/bough.yml](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/bough.yml); [go/plugins/engine/engine.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/engine/engine.go); [go/plugins/loop/loop.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/loop/loop.go); [go/plugins/tools/tools.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/tools/tools.go); [README.md](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/README.md).
- Basis: explicit and structural.
- Confidence: high for code-path reachability; no live source-toolchain execution claimed.
- Caveats: The example/reported usage counts come from maintainer sessions and are not controlled benchmark results. Default local shell access is not sandboxed; no implicit elevated S1 authority is credited.

## S2 — Coordination

- State: C
- Function: Attenuate interference among independently running/queued background S1 child agents contending for the same Bough supervisor's finite runnable child slots, returning waiting task agents to execution once a slot frees.
- Disturbance / variety regulated: Multiple model-driven child processes can otherwise start while all available background execution slots are occupied, oversubscribing the shared host capacity and letting later requests overtake already queued agents.
- Decisive decision or feedback right: Determine which child starts now versus waits under a configured global `maxRunning` and which queued child receives the next freed slot; release/feed back completion and launch failure to the parent workflow.
- Decision owner: First-party deterministic supervisor/queue construction, with the limit selected by runtime configuration; no claim that an autonomous coordinating model chooses the cap or priority policy. This is `C`, not `A`.
- Supporting / enforcement mechanisms: `CreateChild` slot counting, `s.running`, persistent `s.queue`, FIFO `drainQueue`, queued-child restart reconstruction, parent notification, background-agent API and `workers` registration.
- Closure path: Parent launches child agents → supervisor allows up to cap, queues competitors and persists pending task → capacity is freed on child exit/stop → `drainQueue` starts next waiting agent; `report` sends completed/stopped/failed child result to the parent for subsequent model action. Later queued S1 behavior is materially changed from launch-now to launch-after-capacity.
- Boundary reachability: `go/bough.yml` mounts the workers plugin; `workers/background.go::startAgent` calls the first-party serve API; `children.go::CreateChild` and `drainQueue` close the queue/slot feedback path. This S2 witness is conditional on the documented `bough serve` background-child mode, not an always-on global fleet manager.
- Why this is / is not agent-owned: Removing the model would leave the deterministic conflict attenuation intact but not the model-guided child S1 tasks. The first-party coordinator owns admission/deferral mechanics, while human configuration owns the cap. No independent S2 policy deliberator is inferred.
- Evidence: [go/plugins/workers/background.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/workers/background.go); [go/internal/serve/children.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/internal/serve/children.go); [go/internal/serve/children_test.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/internal/serve/children_test.go); [go/internal/serve/children_restart_test.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/internal/serve/children_restart_test.go); [go/bough.yml](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/bough.yml).
- Basis: structural; concurrency and restart scenarios appear in shipped first-party tests.
- Confidence: moderate. The claimed function is narrow shared-slot interference, not semantic cooperation or outcome arbitration between children.
- Caveats: Queue capacity limits by themselves would not be enough if only one S1 existed; this witness depends specifically on multiple distinct first-party child agents in the supported serve mode, concrete shared capacity and release-triggered return.

- Distinct S1 units: Concurrent background model-guided child agent processes with separate session IDs and work tasks under one Bough `serve` supervisor.
- Inter-S1 disturbance: They compete for bounded running capacity, and a newer child can otherwise consume capacity reserved for a waiting earlier child; a running agent prevents other agent work from starting safely under the cap.
- Attenuating coordination relation: Supervisor atomically counts starting/running children, persists FIFO queue for excess requests and ensures queued children start before later requests.
- Feedback into subsequent S1 behaviour: Termination/stop or failed child launch frees a slot → drain starts next queued agent; child's durable turn closure is reported to its parent, enabling further tool/agent decisions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The first-party queue is used specifically to prevent demonstrated inter-agent competition over a finite shared execution resource; its output changes *which competing S1 can execute when*, and the release/recovery feedback closes the interference. Mere child spawning or availability of `spawnAll` is not used as the S2 witness.

## S3 — Inside-and-now control

- State: —
- Function: No separately demonstrated whole-organization inside-and-now resource/commitment management decision with returned change to all Bough S1 operations.
- Disturbance / variety regulated: Current task failures, resource saturation, budget/session limits and project-state drift would be candidates for whole-system control.
- Decisive decision or feedback right: A current whole-of-installed-agent-workload authority would assess cross-S1 commitments/priorities and choose corrective reallocations or interventions.
- Decision owner: Not established at the declared recursion. Operators configure or manually stop individual sessions; deterministic supervisor enforces queue/concurrency mechanics.
- Supporting / enforcement mechanisms: `bough serve` project/session UI, child status APIs, launch caps, cost/session tracking, project containers, tool/hook checks.
- Closure path: S1 session results and queue state are visible and individually actionable, but no shipped whole-system current assessment → discretionary shared-priority/commitment decision → returned multi-S1 regulation loop was established.
- Boundary reachability: No positive S3 claim. UI visibility and direct stop/configuration do not by themselves close this function.
- Why this is / is not agent-owned: A queue scheduler and monitoring UI do not own whole-system current-control discretion. Neither the model's per-task plan nor a configured slot cap changes that.
- Evidence: [go/internal/serve/supervisor.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/internal/serve/supervisor.go); [go/internal/serve/children.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/internal/serve/children.go); [go/plugins/cost/cost.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/cost/cost.go); [go/cmd/bough/serve.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/cmd/bough/serve.go); [go/bough.yml](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/bough.yml).
- Basis: structural negative scoped to shipped paths.
- Confidence: moderate.
- Caveats: Distinct operator organizations could build S3 above the Bough API; that would be a different, externally composed system boundary.

### Absence scope

- Surfaces inspected: Shipped engine/worker/serve supervisor, project and session control documentation/config, cost monitoring, basic stop/cancel and queue controls.
- Plausible first-party paths checked: Web whole-session lists, running child counters, configurable limits, parent messages and current user intervention in sessions.
- Why no material first-party path remains: Inspected paths return local status, impose predefined capacity rules or accept per-session user commands; none implements a first-party whole-current management choice over shared obligations with a returned decision affecting collective S1 regulation. No specific alternative shipped S3 actor/loop surfaced.

## S3* — Complementary audit

- State: —
- Function: No separately independent complementary audit of operational claims with corrective findings returned to whole-current management.
- Disturbance / variety regulated: Misstated code fixes, unreliable child reports or inaccurate history/wiki summaries.
- Decisive decision or feedback right: Independent evidence gathering/judgment challenging ordinary operating reports and feeding a current-control correction.
- Decision owner: Not established as a shipped complementary auditor; routine tool/test output, editable checks and citation validation are not an independent audit channel.
- Supporting / enforcement mechanisms: Test-run tools, hooks, history and replay, `wiki check` citation references, optional human review.
- Closure path: A coding agent can run tests and use findings inside its S1 iteration; wiki citations can be checked for provenance, but no independent S3*-to-S3 corrective return was found.
- Boundary reachability: No positive S3* publication state.
- Why this is / is not agent-owned: The operating agent may verify its own work and a deterministic validator may check references; neither has the distinct independent operational access and corrective path required for S3*.
- Evidence: [go/plugins/wiki/wiki.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/wiki/wiki.go); [go/plugins/wiki/run.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/wiki/run.go); [go/plugins/hooks/hooks.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/hooks/hooks.go); [go/plugins/history/history.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/history/history.go); [README.md](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/README.md).
- Basis: structural bounded negative.
- Confidence: moderate.
- Caveats: Bough may host third-party reviewers via plugins; their mere availability would not make an integrated first-party complementary audit.

### Absence scope

- Surfaces inspected: Shipped hooks, verification/tool-result feedback, recorded sessions, replay, wiki claim/citation handling, worker return.
- Plausible first-party paths checked: Separate review plugin, live independent monitoring access, falsification or correction routed to a distinct supervisory current-control owner.
- Why no material first-party path remains: Inspected first-party checks are same-loop validation, deterministic formatting/provenance checking or ordinary external-human intervention, not an independent corrective audit channel connected to S3 current control at this recursion.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party installed loop evidenced that observes an external/future change, formulates a prospective organizational adaptation and returns an adopted change to Bough's later operating capability.
- Disturbance / variety regulated: New provider/tool ecosystems, recurrent coding failures, changing project requirements and learned experience.
- Decisive decision or feedback right: Evaluate external future conditions and choose/propose a change to the agent organization's future capability, policy or distribution, then return the change into S1/S3.
- Decision owner: No function-specific first-party S4 actor or parent-closed adaptation loop established. Humans can edit plugins; coding models can learn within a task.
- Supporting / enforcement mechanisms: Hot-reloadable plugin configuration, skills, MCP, project history, optional `wiki` ingestion from old logs.
- Closure path: Plugin edits can change subsequent Bough sessions and the wiki generates evidence-linked memory on an optional schedule, but neither supplies a complete shipped external/prospective option-evaluation-and-adoption feedback path. Wiki notes are explicitly not automatically injected into prompts.
- Boundary reachability: No positive S4 mode claimed. Wiki/skill availability alone is not the function-specific return path.
- Why this is / is not agent-owned: Summarizing prior sessions and permitting a human to update config are memory and extension mechanisms, not evidence the installed organization owns future-oriented adaptation decisions.
- Evidence: [go/plugins/wiki/run.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/wiki/run.go); [go/plugins/wiki/wiki.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/wiki/wiki.go); [go/bough.yml](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/bough.yml); [go/plugins/skills/skills.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/skills/skills.go); [README.md](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/README.md).
- Basis: structural bounded negative.
- Confidence: moderate.
- Caveats: A separately installed adaptation plugin or operator-managed roadmap would require an explicit changed system boundary/new-ref review.

### Absence scope

- Surfaces inspected: Bough default plugin rows, plugin remounts, session history, wiki scheduled ingestion/briefs, skills and agent loop.
- Plausible first-party paths checked: Autonomous plugin replacement after environmental feedback, model-mediated redesign/evaluation of future capabilities, reusing wiki summaries as automatically selected operating rules.
- Why no material first-party path remains: The shipped mechanisms either manage present-task context or require a separate developer/operator/agent instruction to choose and apply capability changes; an installed external/future adaptive decision-and-return loop was not found.

## S5 — Policy and identity

- State: —
- Function: No first-party organization-level ultimate-purpose/identity authority with a complete operative decision-return loop identified in the Bough agent installation.
- Disturbance / variety regulated: Conflicting high-level operating purpose, authorization to revise root policy, rules governing which agent organization exists and its ultimate commitments.
- Decisive decision or feedback right: Make and return binding identity or ultimate-policy choices for the installed agent organization rather than merely approve a risky shell command or edit plugin configuration.
- Decision owner: No model-owned S5, constructor S5 or explicit separate first-party parent S5 loop evidenced. Operators control their local setup and API keys, but configuration power does not by itself establish Methodology S5 parent mode.
- Supporting / enforcement mechanisms: Human-written `bough.yml`, session permissions, workspace scoping, host/container boundaries, hooks and explicit prompts.
- Closure path: Human configuration or tool approval can affect subsequent execution, but the evidence inspected does not show an identified ultimate-policy matter reaching a legitimate parent governance process and a returned authoritative decision governing the installation at this recursion.
- Boundary reachability: No positive S5 state published.
- Why this is / is not agent-owned: Agent autonomy over coding work and runtime permission enforcement do not confer legitimate authority to redefine organizational identity or governing purpose.
- Evidence: [go/bough.yml](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/bough.yml); [go/plugins/hooks/hooks.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/hooks/hooks.go); [go/plugins/orb/orb.go](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/go/plugins/orb/orb.go); [README.md](https://github.com/andreylukin/bough/blob/18d07fe115e6ca872273d40d7cedc0881af4561e/README.md).
- Basis: structural bounded negative.
- Confidence: moderate.
- Caveats: A real customer's institutional parent governance might use this harness; no such undisclosed parent system is imported here.

### Absence scope

- Surfaces inspected: Default runtime/configuration, permission and project hooks, operator UI, plugin reconfiguration, agent work/session APIs.
- Plausible first-party paths checked: Human-approved root policy revision, delegated identity decisions, organization-level constitutional authority and their return into running task decisions.
- Why no material first-party path remains: Shipped support lets an operator configure a tool runtime, grant/deny actions or start sessions, without implementing a dedicated first-party identity/ultimate-policy decision process or attributable parent-mode return. No qualifying S5 function ownership evidenced at the declared scope.

## Distributed OSS parent arrangement

This is an independently installable user-local coding harness. GitHub maintainers' repository governance, open-source release acceptance and an operator's personal tool preferences are adjacent to the installed agent organization. None is borrowed as a shared S5 parent mode; an institutional user might compose its own governance externally.

## Self-hosted and non-human modes

Local and project-isolated execution can run model-owned S1 inside human-selected constraints. The optional serve mode adds deterministic S2 child-capacity coordination. Headless use does not prove a permanently unattended multi-agent business, and external model inference does not donate S3/S4/S5 rights to Bough.

## Recursion

The selected recursion is one Bough installed coding-agent system with multiple task cells in background mode. Child agents have independent sessions and tools, but no claim that each is itself a complete viable S1–S5 organization. The Bough repository's human contributor community and other isolated local installations are different boundaries.

## Variety and escalation

Coding errors, test failures, model latency and tool denial feed back as model-visible outcomes in S1. Background worker limits attenuate host-capacity competition in S2 and queue waiting tasks until slot release. Provider failures, failed child launches and stop events generate explicit returned results. Hooks, permission modes and containers enforce bounded action rights but do not themselves constitute S3 current management, S3* complementary audit, S4 adaptation or S5 identity authority.

## Evidence gaps

- The assessment is source-first: Bough source unit tests are present but **not executed by this reviewer** because Go 1.27+ toolchain was unavailable in the inspection host. Thus S2 is grounded in the shipped supervisor implementation and its first-party test fixtures, not a claimed live multi-agent experiment.
- S2's `C` is narrowly a cross-child running-cap interference/queuing mechanism. No assertion of content-level coordination, shared-code conflict resolution, autonomous cap adjustment or independent productivity improvement is implied. If later primary evidence shows the served children do not actually share one bounded contention domain, reassess the S2 witness.
- Operator supervision and `bough serve` status/control may support externally composed S3, but a *shipped substantive whole-current decision and return path* has not been established at this installed-product recursion.
- `wiki` ingestion is prospective contextual knowledge, not proven external-intelligence/organizational-adaptation closure. A genuinely integrated future-oriented adaptation actor or policy-governance workflow at the same frozen SHA would warrant a same-ref review.
