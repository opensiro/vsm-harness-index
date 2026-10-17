---
harness_id: centian
project_name: Centian
repository: https://github.com/T4cceptor/centian
review_ref: 97ae63779dec8117c7bfe1eb007539e46651358b
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Centian

## Review boundary

- System in focus: the first-party `centian start` MCP proxy, configured downstream tool mediation, optionally enabled `taskVerification` step lifecycle, processor/policy checks, event persistence and read-only UI at pinned source revision `97ae63779dec8117c7bfe1eb007539e46651358b`.
- Purpose and identity: transparent runtime interception, action policy, per-task pre/postconditions and frozen task contract verification around **externally configured agents** using Centian as an MCP endpoint; not a first-party general coding-agent runtime.
- Relevant environment: a separately executing external Claude/Gemini/Codex/other MCP client, configured downstream MCP servers and shell tools, templates, project workspace, human users/process designers, local event database, optional reviewers of stored logs.
- Standard-distribution boundary: shipped default `centian init -q` then `centian start` with a configured external MCP client, plus documented opt-in `taskVerification` and `eventStorage`/UI configuration. The configured agent remains outside the first-party Centian runtime even when it elects to call `centian.task_*` tools.
- Credited operating / distribution surfaces: Go CLI `main.go`/`internal/cli/server.go`, proxy handler and injected task tools, `internal/taskverification/service.go`/`runtime.go`, workflow YAML compiler/templates, event store and read-only task-run UI; first-party tool call enforcement and event capture.
- Adjacent first-party surfaces excluded from ownership: `centian benchmark run` agent-launch/evaluation matrix and `internal/benchmarks/` execution runner; deprecated `centian demo --agent` and `internal/agentrunner` sample model invocations; bundled synthetic completed-run replay; project development/CI tests; externally supplied agent intelligence, models and downstream MCP servers. These are not operating S1 of the documented proxy/verification deployment.
- First-party operating / deployment modes considered: standard HTTP MCP proxy; opted-in `taskVerification.enabled` using `verificationRequirement: optional|required`, with frozen planning and preconditions/invariants; eventStorage and read-only UI; benchmark CLI examined as adjacent testing surface, not as production agent harness.
- Recursion level: one local Centian proxy/verification service mediating one or more external agent clients. Those clients are the environment, not first-party Centian operational S1 workers.
- Reviewed revision: `97ae63779dec8117c7bfe1eb007539e46651358b`.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The shipping `centian start` command starts an HTTP MCP proxy with configured downstream MCP servers, client-facing endpoints and opt-in processing layers. Agents install or configure Centian **as an MCP server** rather than entering a Centian-created model/task loop. Its middleware intercepts model clients' tool actions, applies input/output processor and task workflow constraints, forwards permitted tool calls to configured servers and writes audit/run events. The normal CLI entry declares `centian start`, `init`, `server`, `demo`, `benchmark` and configuration commands, with no standard agent worker/session runtime exposed by `start` ([README.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/README.md); [main.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/main.go); [internal/cli/server.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/cli/server.go); [internal/proxy/proxy_setup.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/proxy/proxy_setup.go); [docs/TASKVERIFICATION.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/TASKVERIFICATION.md)).

When `taskVerification` is configured, Centian injects `centian.task_list_templates/register/complete_onboarding/complete_planning/start_step/complete_step/resume/restart/fail` tools into the same external client's MCP endpoint. It stores task state, freezes planning to a compiled workflow, checks preconditions, captures invariant baselines, checks postconditions and returns typed `recoveryActions`. This is substantive **deterministic governance of an external agent's actions**, not a Centian-owned model deciding or executing the next original operational task after external feedback ([internal/taskverification/service.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/service.go); [internal/taskverification/runtime.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/runtime.go); [internal/proxy/proxy_taskverification_tools.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/proxy/proxy_taskverification_tools.go); [docs/TASKVERIFICATION.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/TASKVERIFICATION.md); [task-templates/integrated/guided_tdd_workflow.yaml](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/task-templates/integrated/guided_tdd_workflow.yaml)).

A distinct `centian benchmark run` subcommand calls `internal/benchmarks/runner.go` whose `LaunchAgent` is `agentrunner.Run` and which executes external Claude, Codex or Gemini CLI against a prepared benchmark case. This **does** launch an agent, but it is an adjacent evaluation/benchmark runner for comparing external agents and Centian task templates, not the standard distributed proxy/verification mission. Likewise `centian demo --agent` is explicitly documented as deprecated while default `centian demo` loads a synthetic, already completed incident. Neither may supply S1 to the assessed production deployment ([internal/cli/benchmark.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/cli/benchmark.go); [internal/benchmarks/runner.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/benchmarks/runner.go); [internal/agentrunner/run.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/agentrunner/run.go); [demo/README.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/demo/README.md); [docs/BENCHMARKING.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/BENCHMARKING.md)).

## Operational model

The operator configures MCP servers and starts Centian. A separately installed agent client chooses tasks and MCP calls, and may explicitly ask the proxy for a task-verification contract. Centian validates phase/step state, pre-/post-conditions and permitted tools, forwards or rejects calls, emits structured recovery information and logs events. The external model then decides whether and how to recover. The Centian service itself does not instantiate an internal model-owned task worker and adapt its next substantive operations from those tool results on the normal supported `start` path. This is a guarded proxy/control layer and has meaningful non-VSM value; it does not by itself establish a first-party agentic VSM harness at the selected recursion.

## S1 — Operations

- State: —
- Function: no first-party standard-distribution model-backed autonomous operational unit choosing tasks, taking tool actions and adapting those operations on environmental feedback is reachable; it supplies tools and restrictions to outside agents.
- Disturbance / variety regulated: external agent requests and tool results are inspected and gated but Centian does not choose the original engineering/research actions or perform them as a first-party agent.
- Decisive decision or feedback right: the substantive tool/task action-selection and adaptation judgment belongs to the external MCP client, not Centian.
- Decision owner: none within the assessed standard MCP proxy; external coding agent owns substantive work. The local task runtime deterministically validates transitions.
- Supporting / enforcement mechanisms: Go proxy, template state, tool allowlists, pre/postcondition commands, event logs, optional UI.
- Closure path: external agent selects next action → Centian permits/rejects/gives diagnostics → external agent, not Centian, chooses next substantive step.
- Boundary reachability: the official `centian start` implementation serves MCP tools to external clients. The only local agent-launch code is in separate benchmark and deprecated agent demo paths.
- Why this is / is not agent-owned: removing the external agent leaves a governed tool/service endpoint but no contextual model-agent task selection.
- Evidence: [main.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/main.go); [internal/cli/server.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/cli/server.go); [internal/proxy/proxy_taskverification_tools.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/proxy/proxy_taskverification_tools.go); [internal/taskverification/runtime.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/runtime.go); [internal/cli/benchmark.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/cli/benchmark.go); [docs/BENCHMARKING.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/BENCHMARKING.md)
- Basis: explicit shipped command dispatch, code owner and boundary distinction
- Confidence: high for supported runtime paths
- Caveats: a Centian-mediated external client may be autonomous, but this does not make that client first-party Centian S1.

### Absence scope

- Surfaces inspected: CLI `centian start` and `benchmark` wiring, proxy setup, task-verification tools/service and agentrunner, demo documentation.
- Plausible first-party paths checked: direct proxy and opt-in verification, built-in task templates, opt-in external model CLI benchmark, deprecated model-running demo.
- Why no material first-party path remains: normal `start` never instantiates a first-party model-driven operational task actor. Benchmarks are adjacent evaluator machinery, deprecated demo is not the declared standard operating mode.

## S2 — Coordination

- State: —
- Function: no first-party supported inter-S1 disturbance attenuation is shown because the assessed local service does not own distinct active S1 workers.
- Disturbance / variety regulated: one-open-run per principal, per-phase tool allowlists and workflow sequencing constrain external tool clients, but no pair of first-party operational S1 units and their interference appears.
- Decisive decision or feedback right: coordinate actual competing first-party S1 units, return attenuation to their subsequent actions; not closed within this boundary.
- Decision owner: taskverification service's deterministic single-open-run invariant is a concurrency/safety rule for external principals rather than S2 among Centian-owned S1.
- Supporting / enforcement mechanisms: OpenTaskExistsError, task phases, proxy tools, permission policy, storage.
- Closure path: external session registers a run → repeated registration may fail → external model decides next; no first-party sibling operational actor is being regulated.
- Boundary reachability: active `RegisterTaskWithDescription` enforces one open run per owner, but it is a task admission rule and is not integrated with first-party sibling agents.
- Why this is / is not agent-owned: an overlapping task ban among external clients is not evidence of first-party S1 actors under the declared recursion.
- Evidence: [internal/taskverification/service.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/service.go); [internal/proxy/proxy_taskverification_tools.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/proxy/proxy_taskverification_tools.go); [docs/TASKVERIFICATION.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/TASKVERIFICATION.md); [internal/cli/server.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/cli/server.go)
- Basis: structural negative for bounded first-party S1 relation
- Confidence: high within declared recursion
- Caveats: the service can mitigate operational risk among externally deployed clients without counting as first-party VSM S2.
- Distinct S1 units: none demonstrated as Centian-owned operational agents in default or opt-in proxy+verification mode.
- Inter-S1 disturbance: hypothetical external agents may collide on tools/tasks; they are outside the assessed system-of-focus.
- Attenuating coordination relation: one-open-task admission for a principal is real, but not shown regulating two internal S1 units.
- Feedback into subsequent S1 behaviour: API rejection returns to external client; no first-party internal S1 actor adjusts its own operations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: no internal conflicting S1 pair; ordinary step ordering and safety restrictions cannot substitute for the required relation.

### Absence scope

- Surfaces inspected: run registration and identity, one-open-run validation, task tool gating and proxy registration.
- Plausible first-party paths checked: multiple MCP clients, principal-specific task admission, shared template steps and event history.
- Why no material first-party path remains: no internally operating S1 units whose conflict the constructor attenuates; proxy can regulate external actors without entering this local VSM recursion.

## S3 — Inside-and-now control

- State: —
- Function: no first-party model or parent current-control authority makes discretionary whole-operational-agent priority/resource/replan decisions over in-boundary S1.
- Disturbance / variety regulated: task states and deviations are detected and deterministic phase constraints imposed, but the external agent or human must choose work and responsive task priorities.
- Decisive decision or feedback right: change current whole-system assignments, rescope or intervene based on aggregate task feedback; none of these choices is made by first-party Centian.
- Decision owner: external agent chooses tool/task actions, human authors templates/permissions; Centian deterministic runtime enforces predeclared transitions.
- Supporting / enforcement mechanisms: frozen task workflow, current phase, violation results, recoveryAction descriptors, UI state and event persistence.
- Closure path: external agent plans → Centian validates/blocks step and returns suggested retry → external model chooses whether to try new actions; not an internal model controller of ongoing work.
- Boundary reachability: first-party service/validator is wired but there is no first-party whole agent mission planner or tool-using agent runtime in `centian start`.
- Why this is / is not agent-owned: if the external client is removed, deterministic proxy still enforces frozen rules but cannot decide which task, next strategy or cross-task priority to select.
- Evidence: [internal/taskverification/service.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/service.go); [internal/taskverification/runtime.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/runtime.go); [internal/proxy/proxy_taskverification_tools.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/proxy/proxy_taskverification_tools.go); [docs/TASKVERIFICATION.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/TASKVERIFICATION.md)
- Basis: source-level negative on actual current-control decision owner
- Confidence: high
- Caveats: deterministic safety gates can be sophisticated without becoming S3 current-control judgments.

### Absence scope

- Surfaces inspected: proxy initiation, step transitions, frozen task templates, operator config, read-only UI and benchmark runner.
- Plausible first-party paths checked: task planning/onboarding, progression, failure/retry, event history and manual approvals.
- Why no material first-party path remains: the available decision owner is the external client or fixed template/operator; no first-party mission-wide discretionary regulation/return exists.

## S3* — Complementary audit

- State: —
- Function: no independent first-party complementary audit actor judging producer representations against distinct actual-world evidence and returning corrective instruction to an in-boundary S3.
- Disturbance / variety regulated: step invariants and pre/postcondition checks detect violations, but these are predeclared deterministic validation of an external task rather than an independent auditing agent.
- Decisive decision or feedback right: a separate auditor could inspect source/execution evidence and judge producer claims, return findings to the whole-agent controller; not shipped here.
- Decision owner: deterministic validator for tests/commands and optional human viewer, no independent model auditor with corrective-return authority.
- Supporting / enforcement mechanisms: step preconditions/postconditions, invariant baselines, append-only event evidence, task-view UI.
- Closure path: external tool call/result → policy/verification command → blocked/allowed or retry diagnostic to external agent; no distinct first-party auditor judgment and return via S3.
- Boundary reachability: actual shipped runtime uses executable checks and event store; these are real safeguards but not independent S3* audit ownership.
- Why this is / is not agent-owned: replacing deterministic checks with no checks would reduce enforcement; it would not remove an autonomous auditor, because none runs.
- Evidence: [internal/taskverification/runtime.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/runtime.go); [internal/taskverification/service.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/service.go); [docs/TASKVERIFICATION.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/TASKVERIFICATION.md); [internal/cli/server.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/cli/server.go)
- Basis: bounded absence after inspection of all plausible verifier/audit surfaces
- Confidence: medium-high
- Caveats: not a claim that execution verification is ineffective; it has a different organizational role.

### Absence scope

- Surfaces inspected: taskverification checks, event processing/history, task-run UI, processed action outcomes and default demo.
- Plausible first-party paths checked: human UI audit trail, pre/postcondition oracle, external benchmark scoring and persisted evidence.
- Why no material first-party path remains: checks are deterministic policy gates for external clients, not complementary independently owned audit decisions returned into a Centian-operated S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future/environment intelligence loop chooses and applies prospective improvements to Centian operating policy or agent capability.
- Disturbance / variety regulated: benchmark outcomes and logged deviations can inform a person changing templates later, but current service has no model-led or separately parent-governed adaptive policy revision/return.
- Decisive decision or feedback right: judge changes in external conditions, select new capability/policy and return accepted changes to future operations; absent in deployed service.
- Decision owner: human operator manually maintains templates/config; benchmark results are external research/evaluation data, not an active adaptation owner.
- Supporting / enforcement mechanisms: benchmarks and scorecards, immutable frozen task contracts, config and template reload/selection, logs.
- Closure path: external agent deviates → runtime records violation → user may inspect and edit future template manually, but no first-party S4 decision/returned policy change is built into service.
- Boundary reachability: the first-party default service performs no prospective model analysis or policy adaptation; the benchmark CLI is an adjacent evaluation tool.
- Why this is / is not agent-owned: removing any external experimenter leaves only fixed policy and task checks, not a prospective intelligence controller.
- Evidence: [docs/BENCHMARKING.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/BENCHMARKING.md); [internal/cli/benchmark.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/cli/benchmark.go); [internal/benchmarks/runner.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/benchmarks/runner.go); [internal/taskverification/service.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/service.go); [docs/TASKVERIFICATION.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/TASKVERIFICATION.md)
- Basis: negative across first-party runtime/adjoining benchmark path
- Confidence: medium-high
- Caveats: human learning from logs may exist outside Centian; mere future manual configuration edits do not establish an internal parent S4.

### Absence scope

- Surfaces inspected: runtime policy/templates, event/benchmark scorecards, benchmark task runner and configuration.
- Plausible first-party paths checked: workflow-template updates from benchmark feedback, user edits and automatic policy evolution.
- Why no material first-party path remains: no supported first-party adaptive future-change proposal/selection/return route; static templates, scorecards and human maintenance are not a closed in-boundary S4.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct ultimate identity/ethos/policy authority loop at the local guarded proxy boundary.
- Disturbance / variety regulated: configuration and approvals set tool access and tenant/project policy but do not determine the ultimate legitimate mission of the whole viable organization.
- Decisive decision or feedback right: authoritative identity-level policy settlement and return to change future S1–S4 conduct; not exercised here.
- Decision owner: operator selects config, template and downstream clients, without a first-party distinct S5 policy channel.
- Supporting / enforcement mechanisms: application config, principal auth, project gateways, template approvals and audit logs.
- Closure path: operator changes configuration → proxy enforces new permissions; no whole-system ethos dispute → legitimate S5 decision → normative return.
- Boundary reachability: inspected first-party config, auth and workflow owner surfaces; these are service controls not organizational identity judgment.
- Why this is / is not agent-owned: manual action authorization and safe tool policy cannot be relabeled as S5.
- Evidence: [internal/config/config.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/config/config.go); [internal/auth/authorizer.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/auth/authorizer.go); [internal/taskverification/service.go](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/internal/taskverification/service.go); [docs/configuration_reference.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/docs/configuration_reference.md); [README.md](https://github.com/T4cceptor/centian/blob/97ae63779dec8117c7bfe1eb007539e46651358b/README.md)
- Basis: bounded negative for local proxy/service recursion
- Confidence: high
- Caveats: an institution operating Centian can have S5 outside this assessed software.

### Absence scope

- Surfaces inspected: auth principals, project config, task approval nodes, UI, runtime authorization and operator docs.
- Plausible first-party paths checked: identity/config decisions, task approval-waits, protected tools and human redirection.
- Why no material first-party path remains: operator-owned setup/permissions affect tool safety but there is no separate whole-system ethos/identity settlement with authoritative return at this first-party runtime boundary.

## Evidence gaps

- Negative states are **bounded** to the standard `centian start` MCP proxy plus opt-in task verification, not to every external agent a customer might connect or a future version.
- The first-party `agentrunner.Run` launch is real and called in the shipped `centian benchmark run` subcommand. Its isolated benchmark/evaluation purpose does not make it a first-party **operational** S1 of the service. `centian demo --agent` is deprecated; default demo uses synthetic completed-run events.
- Tool guard and invariant verification are implemented and valuable, but they validate external agents' actions; no autonomous current-control or complementary independently owned S3* actor was found.
- There was no live external-model inference or production MCP server deployment in this review; source reachability is assessed from the pinned CLI and official configuration docs.
- If a different system boundary encompassing an external model-backed client were explicitly chosen, the VSM mapping could differ; that would be a separate assessment, not a retrofit of external intelligence onto the Centian repository.

## Conclusion

**Proposed canonical disposition: `excluded-no-agentic-vsm`** at frozen source `97ae63779dec8117c7bfe1eb007539e46651358b`; six-state vector `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`. Centian is a functioning MCP policy/verification proxy, with real audit trails and quality gates, but in its supported operating deployment it does not own the agentic S1 task/action/feedback loop: clients provide it from outside. Auxiliary benchmarking/deprecated demo model launches and test-only infrastructure do not donate first-party agentic VSM ownership.
