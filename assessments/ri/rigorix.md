---
harness_id: rigorix
project_name: Rigorix
repository: https://github.com/arman-jalili/rigorix-oss
review_ref: 4700f60c6296542a1d36d3cea2318c1300549498
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Rigorix

## Review boundary

- System in focus: Rigorix's **standalone first-party CLI, planning pipeline, template/DAG engine, policy/budget/approval machinery and optional locally configured audit/scored checks** at the exact frozen revision. This is not an umbrella assessment of coding agents that use the Rigorix MCP server.
- Purpose and identity: convert a user's intent to a template-constrained plan and execute/verify that graph under risk, identity, permissions, budgets, approval and audit gates. The upstream expressly describes Rigorix as an execution-governance layer, **not** an open-ended agent loop.
- Relevant environment: source tree, CLI user task, operator-authored template/policy, model provider performing remote inference, repository/tool state, test/quality/approval results, optional external MCP agent.
- Standard-distribution boundary: `rigorix-cli`, `rigorix-engine`, and `rigorix-mcp` only insofar as it exposes the engine as a tool to an already autonomous **external** client. No inferred authority or model decision loop from Claude Code, Cursor, Aider or the host application is credited.
- Credited operating / distribution surfaces: CLI `plan`/`run`, the actually wired `PlanningPipelineImpl` backed by `ClaudeClassifier`/`OpenaiClassifier`, `LlmParameterExtractor` and optional generated-template fallback; the first-party `OrchestratorServiceImpl`, deterministic DAG tool executor/retry and its gates, event/state/audit and configured scoring hooks.
- Adjacent first-party surfaces excluded from ownership: MCP-client agent cognition and continuation; developer `.agents`/`.pi`/`.claude` and repository dogfood; GitHub Actions and external demo; tests, mocks, roadmap and optional separate validation-loop assembly without live standard CLI wiring; externally run scoring backends.
- First-party operating / deployment modes considered: packaged standalone CLI run and plan; opt-in CLI human approval, risk and score backends; `rigorix-mcp` tool facade driven by external models; optional library-level `ValidationLoopService`, which is **not wired by** the ordinary CLI builder at this ref.
- Recursion level: one bounded intent-to-DAG execution, whose parallel DAG nodes are ordered **steps**, not independently deciding S1 agents. Source-level components are not automatically viable subsidiary organizations.
- Reviewed revision: `4700f60c6296542a1d36d3cea2318c1300549498` (candidate intake [#848](https://github.com/opensiro/vsm-harness-index/issues/848), no repin).
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/README.md) describes template-driven deterministic execution and expressly distinguishes Rigorix from open-ended coding agent loops. In its standard CLI, [cli/src/cli_boundary/orchestrator.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/cli/src/cli_boundary/orchestrator.rs) constructs real model-backed classifiers and a parameter extractor plus template-generator fallback; this is a meaningful **LLM-assisted planning** workflow rather than a bare API gateway. [engine/src/planning/application/pipeline_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/planning/application/pipeline_impl.rs) selects/fills templates, constructs and validates a task graph, with [engine/src/template_generation/application/generation_service_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/template_generation/application/generation_service_impl.rs) providing model-generated templates when needed.

[engine/src/orchestrator/application/orchestrator_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/orchestrator/application/orchestrator_impl.rs) sequences task planning → graph execution → result/state/audit. [engine/src/execution_engine/application/service_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/execution_engine/application/service_impl.rs) executes approved graph nodes through a fixed `execute_tool` dispatch (`run_command`, file and git operations, etc.) with predetermined dependency order and retry/recovery policy. The executor's dispatched tools do **not** include a standard dynamically planned `llm_generate` tool that gives the model a continuing action selection loop after step feedback. [engine/src/llm_step/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/llm_step/mod.rs) separately defines LLM generation primitives, but their existence as a module does not establish live DAG executor wiring.

[engine/src/plan_validation/application/loop_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/plan_validation/application/loop_impl.rs) and `OrchestratorServiceImpl::with_validation_loop` expose an opt-in library-level iterative plan→execute→verify path; source tracing of the shipped CLI builder found that it constructs `OrchestratorBuilderImpl` with planning/execution/budget/state/audit/scored-evaluation services but **does not attach the validation-loop service**. Treating a separately composable library loop as the ordinary installed agent would incorrectly cross a standard-distribution boundary. [mcp/README.md](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/mcp/README.md) explicitly states external agents keep their own loop and use Rigorix as gated tools.

[engine/src/audit/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/audit/mod.rs) records HMAC-signed execution envelopes; [engine/src/scored_evaluation/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/scored_evaluation/mod.rs) defines pluggable local/MCP/HTTP artifact-quality scoring. [cli/src/cli_boundary/orchestrator.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/cli/src/cli_boundary/orchestrator.rs) optionally configures these backends; independently operated backend scorers supply their own analysis and must not be borrowed as a shipped Rigorix organizational owner. [engine/src/quality_gates/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/quality_gates/mod.rs) and [engine/src/approval/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/approval/mod.rs) implement validation and human tool-step gates.

## Operational model

The operator provides a task and preconfigured restrictions. CLI-backed LLM inference can classify the intent, fill a template, or propose a new template; the engine executes a **sealed DAG** under fixed policy, verifies/records results and returns a terminal status. Failure-based retries/recovery are rule-controlled. For the default supported CLI path at this pinned ref, a runtime result does not return to the model for a fresh discretionary coding decision and subsequent tool-action selection. A user, an external MCP agent or an explicitly composed nondefault validation loop would have to supply the missing iterative operational actor/closure. The CLI is valuable as **an agent-execution governance substrate**, but that is not by itself an autonomous AI agent harness in the canonical Index's admission sense.

## S1 — Operations

- State: —
- Function: the target VSM S1 would be an autonomous operational coding agent that changes its substantive work decisions from environmental/tool feedback. Rigorix performs bounded model-assisted plan construction and deterministic graph execution but does not establish a complete first-party autonomous S1 under the reviewed standalone distribution.
- Disturbance / variety regulated: differing user intents, file content, repository states and failures are handled by model-based initial classification/templates and rule-driven execution/retry.
- Decisive decision or feedback right: choose future work steps from observed code/tool/quality feedback and iterate until task resolution or bounded stop.
- Decision owner: **not established** in standard standalone CLI. The LLM owns initial template/parameter selection, but the graph execution path owns subsequent scheduling deterministically; full iterative discretion remains with a host/operator or separately wired service.
- Supporting / enforcement mechanisms: model classifier/extractor, generated templates, DAG executor, approval, permission, retry/recovery policy, validation/audit and result reporting.
- Closure path: task → LLM-backed initial plan → validated DAG → fixed tool execution → rule-based retry/recovery → result. No supported **default CLI** result → model re-evaluation → newly model-chosen next coding act closure is evidenced.
- Why this is / is not agent-owned: an LLM call during initial planning is not identical to an autonomously closed operating agent. Without the model, planning loses task-specific choices; with the model but without a returned task-result decision right, ongoing operation remains a template/DAG execution rather than an independently regulating first-party agent.
- Evidence: [README.md](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/README.md); [cli/src/cli_boundary/orchestrator.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/cli/src/cli_boundary/orchestrator.rs); [engine/src/planning/application/pipeline_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/planning/application/pipeline_impl.rs); [engine/src/execution_engine/application/service_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/execution_engine/application/service_impl.rs); [engine/src/orchestrator/application/orchestrator_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/orchestrator/application/orchestrator_impl.rs); [engine/src/plan_validation/application/loop_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/plan_validation/application/loop_impl.rs); [mcp/README.md](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/mcp/README.md).
- Basis: explicit first-party CLI/engine source and bounded absence of standard-distribution model-return wiring.
- Confidence: medium-high.
- Caveats: this **does not** say Rigorix lacks AI or cannot generate/run code; its separate library `ValidationLoopService` is a plausible *construction primitive*. An external autonomous agent integrating Rigorix may have S1=A at the external agent's own system boundary. Index requires included harnesses to show actual S1=A (see `scripts/validate_tldr.py`); no such first-party standard-mode closure is claimed here.

### Absence scope

- Surfaces inspected: CLI builder/wiring, model-backed planning/classification/parameter/template generator, graph execution tool dispatch and retries, optional plan-validation loop, MCP tool server and standard README.
- Plausible first-party paths checked: model planning as a one-shot S1 actor; iterative model call after graph/tool result; separately composable `with_validation_loop` runtime; `llm_step` module and executor dispatch; external MCP agent steering.
- Why no material first-party path remains: shipped default CLI consumes an initial model-assisted plan but deterministically executes its DAG and reports the result without continued first-party model-selected operational steps. Library-only optional composition lacks demonstrated default CLI reachability; external MCP model loops are expressly owned by separate systems.

## S2 — Coordination

- State: —
- Function: no demonstrable interference attenuation between **distinct autonomous operating S1 agents** at this single-run recursion.
- Disturbance / variety regulated: parallel DAG nodes and shared files may create execution contention or ordering problems, but those nodes are not separate adaptive coding S1 organizations.
- Decisive decision or feedback right: resolve inter-S1 conflicts and return revised coordination arrangements to those S1s.
- Decision owner: no autonomous S2; the DAG scheduler, dependency validation, permission/sequence policy and retry service carry out deterministic ordering and gating.
- Supporting / enforcement mechanisms: graph dependency edges, concurrent node execution, budget/permission gates and event/state tracking.
- Closure path: completed/failing nodes update DAG scheduling, not subsequent action strategies of multiple model-driven S1 units.
- Why this is / is not agent-owned: graph concurrency and permission checks remain when any model-directed coordinator is removed; no inter-agent negotiation/control loop is surfaced.
- Evidence: [engine/src/dag_engine/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/dag_engine/mod.rs); [engine/src/execution_engine/application/service_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/execution_engine/application/service_impl.rs); [engine/src/execution_engine/domain/parallel_executor.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/execution_engine/domain/parallel_executor.rs); [README.md](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/README.md).
- Basis: bounded absence.
- Confidence: high.
- Caveats: external agents can coordinate their usage of Rigorix, outside this boundary.

### Absence scope

- Surfaces inspected: graph scheduler, executor concurrency/dependencies/retries, orchestrator and MCP gateway.
- Plausible first-party paths checked: DAG branches treated as independent agents, path-conflict management, external multi-agent MCP client and shared resource policies.
- Why no material first-party path remains: DAG nodes are steps in one template execution, with no first-party population of independent autonomous child S1 agents and no corresponding inter-S1 feedback/coordination owner.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current supervisory judgment over an autonomous S1 organization is closed.
- Disturbance / variety regulated: approvals, budget exhaustion, failed nodes and plan drift are handled with per-run rules rather than discretionary whole-current operating-unit commitments.
- Decisive decision or feedback right: choose resource/commitment intervention across active S1 operations using an actual whole-system current view and return that regulation into operations.
- Decision owner: deterministic budget/sequence/approval and status machinery; human step authorization is not a deployed S3 parent-governance decision over first-party S1 units.
- Supporting / enforcement mechanisms: DAG ready queue, cost caps, plan review TUI, cancellation/resume, identity and risk gating.
- Closure path: ready/blocked DAG node → configured gate/status → execute/retry/stop; no whole-S1 current-control intervention owner and returned revision.
- Why this is / is not agent-owned: eliminating an imagined S3 actor leaves the same predetermined DAG controller and human approval prompts.
- Evidence: [engine/src/orchestrator/application/orchestrator_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/orchestrator/application/orchestrator_impl.rs); [engine/src/execution_engine/application/service_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/execution_engine/application/service_impl.rs); [engine/src/budget_tracking/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/budget_tracking/mod.rs); [cli/src/tui/plan_review.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/cli/src/tui/plan_review.rs).
- Basis: bounded absence.
- Confidence: high.
- Caveats: a surrounding organization may deploy current-control policy for multiple agents and enforce it through Rigorix.

### Absence scope

- Surfaces inspected: live execution state, resource budget, approvals and sequencing, CLI/TUI control, scoring integration.
- Plausible first-party paths checked: single DAG graph as current team view, automatic budget throttling as S3, approval stop/resume as S3 parent mode, external MCP parent controller.
- Why no material first-party path remains: the first-party installed system executes and enforces one graph, without complete current discretionary control over independently operating S1s.

## S3* — Complementary audit

- State: —
- Function: no independently owned complementary inspection **and returned organizational correction** over an existing current S3 function is established; Rigorix does ship important logging and quality-evaluation controls.
- Disturbance / variety regulated: poor artifacts, unsafe steps, misreported completion or audit gaps.
- Decisive decision or feedback right: a complementary auditor separately inspect direct evidence, reach an audit judgment and return binding corrective action to the present operating regulation.
- Decision owner: local HMAC envelopes and policy/test checks are ordinary record/enforcement components; configured local/MCP/HTTP scorers supply optional task QA, often computed by external backend owners.
- Supporting / enforcement mechanisms: signed audit envelope, scored-evaluation protocol/backend, quality gates, per-node evaluation events, read-only audit tools, static merge thresholds.
- Closure path: operation → logged/audited/scored evidence → threshold/record/optional host report, **not** a proven complementary audit judgment → S3 corrective authority → new organizational regulation loop.
- Why this is / is not agent-owned: signing execution metadata proves provenance, not an independent audit judge. A separately operated scoring provider cannot donate its autonomy to first-party Rigorix; a score gate is ordinary task QA unless its independent direct evidence and corrective authority/return are established.
- Evidence: [engine/src/audit/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/audit/mod.rs); [engine/src/scored_evaluation/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/scored_evaluation/mod.rs); [engine/src/quality_gates/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/quality_gates/mod.rs); [cli/src/cli_boundary/orchestrator.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/cli/src/cli_boundary/orchestrator.rs); [engine/src/orchestrator/application/orchestrator_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/orchestrator/application/orchestrator_impl.rs).
- Basis: bounded absence of *organizational S3* ownership*, not absence of audit functionality.
- Confidence: medium-high.
- Caveats: Rigorix could support an independent auditor in a larger configured host organization; no such end-to-end first-party delivered parent-regulatory arrangement is proven at the reviewed boundary.

### Absence scope

- Surfaces inspected: audit envelope generation/read-back, optional scoring adapters and threshold gates, ordinary quality gates, CLI wiring and first-party run status.
- Plausible first-party paths checked: HMAC record as independent audit actor, model-based scoring as an autonomous auditor, third-party scoring service as first-party owner, threshold veto as corrective returned S3 control.
- Why no material first-party path remains: the available checks are ordinary execution/QA or external scoring; the reviewed first-party package has no independently acting complementary auditor whose finding changes an actual S3 organization's current control decisions.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed first-party prospective external environmental intelligence and adaptation cycle for the Rigorix organization's future capabilities.
- Disturbance / variety regulated: evolution of codebases, model providers and future threat/policy expectations.
- Decisive decision or feedback right: consider future environment and implement chosen changed operational capability over subsequent runs.
- Decision owner: human users/maintainers choose templates, packages and policy; local LLM template generation concerns current tasks, not independent future organizational strategy.
- Supporting / enforcement mechanisms: generated template storage, configuration, log history and composable planning/validation modules.
- Closure path: current task template may persist/reuse, but no automatically selected outside future strategy re-enters deployed operations as an organizational capability change.
- Why this is / is not agent-owned: current-task model planning and cache reuse are not long-horizon external adaptation authority.
- Evidence: [engine/src/template_generation/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/template_generation/mod.rs); [engine/src/planning/application/pipeline_impl.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/planning/application/pipeline_impl.rs); [engine/src/plan_validation/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/plan_validation/mod.rs); [README.md](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/README.md).
- Basis: bounded absence.
- Confidence: medium-high.
- Caveats: externally requested source changes, CI or release processes are adjacent operator/maintainer work.

### Absence scope

- Surfaces inspected: planning/generator/cache, event/audit history, config changes, optional validation loop and maintainer documents.
- Plausible first-party paths checked: automatically revised templates as S4, future threat monitoring, model-generated new capabilities, next-run capability feedback.
- Why no material first-party path remains: shipped autonomy targets current task planning, while whole-harness future capability selection/promotion remains outside first-party runtime agency.

## S5 — Policy and identity

- State: —
- Function: no function closing ultimate organizational identity/legitimate policy conflicts over a first-party agent organization.
- Disturbance / variety regulated: risk/permission escalation, identity mismatch, policy violation and protected file edits.
- Decisive decision or feedback right: adjudicate ultimate legitimate identity/policy and return binding changed authority to operation, not merely approve a configured tool.
- Decision owner: operator-authored policies and human step approvals; runtime applies bounded enforcement without authority to redefine legitimate purpose.
- Supporting / enforcement mechanisms: policy.toml, risk gating, identity metadata, approval record, sequence policy, permission enforcer and audit.
- Closure path: preconfigured policy → allow/deny/pause current tool or node → execute or abort; no independent institutional identity-level decision and return.
- Why this is / is not agent-owned: control-plane naming and human approvals are not the full S5 function.
- Evidence: [engine/src/policy_engine/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/policy_engine/mod.rs); [engine/src/permission/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/permission/mod.rs); [engine/src/approval/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/approval/mod.rs); [engine/src/identity/mod.rs](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/engine/src/identity/mod.rs); [README.md](https://github.com/arman-jalili/rigorix-oss/blob/4700f60c6296542a1d36d3cea2318c1300549498/README.md).
- Basis: bounded absence.
- Confidence: high.
- Caveats: a business using Rigorix may govern its identity in a larger human organization; that is not in the evaluated source boundary.

### Absence scope

- Surfaces inspected: permission/identity policy, approvals, risk controls, CLI human modes, audit and MCP consumers.
- Plausible first-party paths checked: operator node approval as parent-governed S5, policy override as ultimate identity decision, user editing config as policy closure.
- Why no material first-party path remains: these only authorize steps inside previously supplied goals and cannot evidence a legitimate ultimate-purpose dispute/decision/return governance loop.

## Distributed OSS parent arrangement

Upstream code maintainers, individual product users and external agents do not form one shared first-party viable coding organization. The governance and PR processes of the OSS project, as well as other-agent MCP clients, are adjacent to this single task executor. No `P` mode is inferred from users configuring policy or approving a risky node.

## Self-hosted and non-human modes

The installed CLI is useful as a self-hosted execution-governance layer, but an operator choosing a plan and an external agent invoking MCP tools remain outside its autonomous S1 boundary. `ValidationLoopService` can be manually composed by a downstream implementer; its module is not sufficient to reclassify the ordinary CLI as an integrated autonomous agent. Read-only audit access and optional independent scoring can be used by an **external** audit organization, whose actual authority and returned correction would require its own assessment.

## Recursion

A single execution graph comprises deterministic steps and model-assisted plan compilation; it is not a nested population of autonomous operational S1 agents. Concurrent DAG branches and separate externally operated MCP clients are not credited as child viable systems of the same Rigorix instance.

## Variety and escalation

Unknown tasks are handled through LLM-backed classification/template selection, followed by bounded execution under budget/policy, retries and approval escalation. Signed evidence and optional scoring can surface exceptional problems externally. Such safety and reporting functions are valuable but do not close the full six-function VSM organization on the first-party boundary.

## Evidence gaps

- This is a **source-first structural review**, not a live end-to-end model-provider benchmark. It records actual CLI construction of LLM classifier/extractor/generator but finds no supported default CLI return of execution results into further model-chosen code actions.
- This negative applies to **`rigorix-cli` at the pinned revision**, not to an external autonomous MCP client or a distinct re-composed custom library app. Evidence of a genuinely shipped first-party standard-mode iterative agent could justify a new same-ref correction without repinning.
- Audit and scoring are real product features. The negative S3* is specifically about absence of a first-party complementary independent corrective-return path into an operating S3 loop, not about cryptographic-log integrity or scorer quality.
- No manual independent review, GitHub approval or semantic gate is claimed.

## Assessment summary

**Proposed disposition: `excluded-no-agentic-vsm`**, because the pinned first-party Rigorix standalone product is a model-assisted deterministic execution/governance engine without a standard-distribution autonomous coding-agent S1 that owns continuing post-execution task decisions. **Vector:** `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`. This is not a criticism of Rigorix's safety, policy, audit or user usefulness; it prevents importing an external MCP agent as the product's own agentic VSM.
