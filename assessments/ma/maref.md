---
harness_id: maref
project_name: MAREF (Multi-Agent Recursive Evolution Framework)
repository: https://github.com/maref-org/maref
review_ref: 35b1d8108887bf162711c2212b7a67d6e21d9342
reviewed_at: 2026-10-21
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-21
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: C
autonomy_s5: —
---

# MAREF (Multi-Agent Recursive Evolution Framework)

**Canonical disposition:** included first-party configured recursive code-evolution work cell as an agentic harness, **not** all first-party governance claims as VSM ownership. Batch [#1827](https://github.com/opensiro/vsm-harness-index/issues/1827), row 4; original frozen intake [#1281](https://github.com/opensiro/vsm-harness-index/issues/1281), position 7.

## Review boundary

- System in focus: the shipped MAREF OSS distribution's internally runnable code-evolution path and adjacent governance/run-state support, rather than an externally hosted CrewAI/LangGraph/AutoGen system merely wrapped by the governance overlay.
- Purpose and identity: allow safety-constrained execution and iterative improvement of MAREF's own source modules while exposing reusable guardrails for third-party agents.
- Relevant environment: project source/test tree, Git and Python tools, configured OpenAI/Anthropic provider, model-generated code, runtime guardrails, external clients of the overlay and CI.
- Standard-distribution boundary: `src/maref/recursive/recursive_evolution_loop.py`, first-party observer/diagnostician/architect, `llm_code_generator.py`, `self_executor.py`, codegen work cell, source validators, governance FSM and bounded coordinator. No client application agents imported from other frameworks.
- Credited operating / distribution surfaces: recursive REL class usable in Python, MCP `maref_codegen`/`maref_deploy` tools, configured LLM provider adapters and local code/test/deploy effects; governance wrappers only to the extent actually wired.
- Adjacent first-party surfaces excluded from ownership: TLA+ model/state proofs as semantic governance decisions, >11k test count assertions, formal model demos, mock/no-provider generator, marketing scores, independent framework agents and server/GUI without a specified substantive task loop. Model inference is a dependency, not a distributed organization by itself.
- First-party operating / deployment modes considered: the configured OpenAI/Anthropic recursive codegen mode, deterministic generator fallback, stand-alone governance-only overlay, caller-supplied `UnifiedHarness`/`MultiAgentCoordinator` mode, local dry-run desktop path and mock pipeline tests.
- Recursion level: one source-code evolution work cell, with a prospective self-modification constructor; no independently established organization of multiple continuing viable S1 businesses.
- Reviewed revision: `35b1d8108887bf162711c2212b7a67d6e21d9342`.
- Observation date: 2026-10-21.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

MAREF's [README](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/README.md) primarily presents a governance overlay for external agents; its default `GovernedLoop` requires a subclass-provided cycle and `LoopGovernanceBridge` wraps a supplied loop. The `UnifiedHarness` runs caller-supplied step handlers. These surfaces do **not** themselves claim autonomy borrowed from an external agent or user-supplied callable. See [src/maref/execution/harness/unified.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/execution/harness/unified.py); [src/maref/loop/bridge.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/loop/bridge.py).

A distinct first-party supported `RecursiveEvolutionLoop.run_session` implementation actually orchestrates self-observation, diagnosis, architecture proposal, configured model-based code generation, safety, source deployment, test/quality verification and rollback. The `LLMCodeGenerator` selects real OpenAI/Anthropic adapters when credentials and libraries exist, else a mock provider (not credited as an agent). `SelfExecutor`'s direct path can generate code, AST-validate, check constitution/safety, deploy and verify; a separate optional `CodeGenLoop` exposes a model/tool-call loop when a backend is attached but is otherwise deterministic. These pathways cannot be treated as always active or equivalent. See [src/maref/recursive/recursive_evolution_loop.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/recursive_evolution_loop.py); [src/maref/recursive/self_observer.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_observer.py); [src/maref/recursive/self_diagnostician.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_diagnostician.py); [src/maref/recursive/self_architect.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_architect.py); [src/maref/recursive/llm_code_generator.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/llm_code_generator.py); [src/maref/recursive/self_executor.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_executor.py); [src/maref/codegen/loop.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/codegen/loop.py); [src/maref/mcp/evolution_tools.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/mcp/evolution_tools.py).

The generic `MultiAgentCoordinator` is a task fanout utility operating caller-supplied harnesses; even its named parallel mode holds a lock around `_dispatch`, so claimed independent collision resolution/organizational S2 cannot be inferred from naming. The FSM transitions and audit chain record or constrain pre-selected task action, not the independent deliberation of a legitimate VSM management layer.

## Operational model

Source/test state → first-party observer/diagnosis → deterministic architecture option selection → model content generated on a configured provider → constitution/safety gate → code change deployment → source validation/test results → possible rollback or another evolution round. This is meaningful agentic S1 when the provider path is configured, with bounded prospective self-modification. The default governance-only wrapper remains support, not another agentic S1. The assessment is *source-first static*; no real provider, production deployment, safety proof or full test suite was executed.

## S1 — Operations

- State: A
- Function: A configured model-backed first-party recursive code-change work cell produces substantive source changes and evaluates their acceptance for a developer-defined system evolution task.
- Disturbance / variety regulated: Nontrivial architectural refactoring, code quality regressions, test coverage and generated source correctness.
- Decisive decision or feedback right: In the normal configured OpenAI/Anthropic route, the model chooses task-semantic implementation text in response to a locally generated architecture proposal; the harness evaluates, deploys/rolls back and can observe another round.
- Decision owner: `LLMCodeGenerator` with `OpenAIProvider`/`AnthropicProvider` supplies first-party invoked semantic code generation; the REL/SelfExecutor controls step admission and environment effects. External model compute does not own the harness architecture.
- Supporting / enforcement mechanisms: `RecursiveEvolutionLoop` OBSERVE→DIAGNOSE→ARCHITECT→CODEGEN→SAFETY→DEPLOY→VERIFY→EVALUATE; `SelfObserver`, `SelfArchitect`, `LLMCodeGenerator`, `SelfExecutor`, AST, tests, rollback and constitutional red-line guard.
- Closure path: Local code and test observations become bounded architecture proposals; a model call generates change content; source is screened and deployed; verification feeds acceptance / rollback and further attempts. This is an operational loop with tool/file effects, not a static LLM API wrapper.
- Boundary reachability: `RecursiveEvolutionLoop.run_session()` calls first-party observer/diagnostician/architect, then `LLMCodeGenerator.generate`, then `SelfExecutor.deploy`, then test/verification. The provider uses actual async OpenAI/Anthropic APIs when configured; absent keys, the fallback mock does not support a live cognitive claim.
- Why this is / is not agent-owned: Configured model-generated source changes are first-party invoked and assessed within a bounded work-cell execution path; model inference alone does not carry ownership.
- Evidence: [src/maref/recursive/recursive_evolution_loop.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/recursive_evolution_loop.py); [src/maref/recursive/self_observer.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_observer.py); [src/maref/recursive/self_diagnostician.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_diagnostician.py); [src/maref/recursive/self_architect.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_architect.py); [src/maref/recursive/llm_code_generator.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/llm_code_generator.py); [src/maref/recursive/self_executor.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_executor.py); [src/maref/evolution/constitution_harness.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/evolution/constitution_harness.py)
- Basis: structural
- Confidence: moderate-high
- Caveats: No real external model execution in this review; current source path is sufficient to establish a configured autonomous S1, not performance, production adoption or customer reliability.


## S2 — Coordination

- State: —
- Function: Attenuate reciprocal interference between multiple continuing, viable first-party agentic S1 units and return corrections to those units.
- Disturbance / variety regulated: Concurrent worker changes and conflicting ownership over shared work might require coordination.
- Decisive decision or feedback right: A continuing coordinator would decide shared contention and return a changed action/commitment to distinct agent-owned S1 operations.
- Decision owner: `MultiAgentCoordinator` dispatches caller-supplied `BaseHarness` objects and applies deterministic trust gates; no owner of reciprocal independent S1 operations is identified.
- Supporting / enforcement mechanisms: Sequential/parallel task dispatch with trust check, optional circuit breaker, logging/metering and result aggregation; proposed role labels.
- Closure path: `run_all` fans one task out to registered harnesses and gathers results. It does not show collision detection across continuing S1 operations or a resolution that returns to those agents. Parallel implementation holds a lock around the whole `_dispatch`, in fact serializing the supposed parallel work.
- Boundary reachability: Do not credit S2 merely from multi_agent naming, adapter integration or preflight safety gates.
- Why this is / is not agent-owned: No material eligible first-party VSM function closure at the assessed organizational boundary; the cited mechanisms are narrower.
- Evidence: [src/maref/execution/multi_agent/coordinator.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/execution/multi_agent/coordinator.py); [src/maref/execution/harness/unified.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/execution/harness/unified.py); [src/maref/loop/bridge.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/loop/bridge.py)
- Basis: structural
- Confidence: moderate-high
- Caveats: An external caller can supply independent autonomous units and its own coordination, but that would require separate supported evidence.

### Absence scope

- Surfaces inspected: Default `MultiAgentCoordinator`, governed loop bridge, recursive coding work cell, task schedule and adapter surfaces.
- Plausible first-party paths checked: Concrete separate model-backed S1 units with conflicting shared effects and an implemented conflict-attentuating feedback relation.
- Why no material first-party path remains: Current first-party coordinator sequences and checks supplied harness calls, but does not close a demonstrable inter-viable-unit disturbance→resolution→changed-operation path.


## S3 — Inside-and-now control

- State: —
- Function: Regulate current whole-system resources, operational commitments and exceptions across multiple viable operations.
- Disturbance / variety regulated: Cost/safety interruptions, agent failures, task timeouts and backlog would need system-level managerial decisions.
- Decisive decision or feedback right: Choose/revise global priorities or resource commitments, assign authority and return the decision to ongoing S1 units.
- Decision owner: Deterministic FSM and circuit breakers enforce pre-supplied bounds on individual runtime/task loops; no S3 steward/controller with whole-system decision feedback established.
- Supporting / enforcement mechanisms: Gray-code governance FSM, `GovernedLoop`, per-execution circuit breaker, identity, tool permission, safety/quality gates and per-task cost caps.
- Closure path: Stages advance along predefined local paths, or stop when preflight, cost, safety or test conditions fail. This is current-task execution safety, not an evidenced whole-of-organization management relation across ongoing S1 units.
- Boundary reachability: Governance code is real and executable, but an implementation of constraints is not itself an S3 decision owner.
- Why this is / is not agent-owned: No material eligible first-party VSM function closure at the assessed organizational boundary; the cited mechanisms are narrower.
- Evidence: [src/maref/governance/state_machine.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/governance/state_machine.py); [src/maref/loop/bridge.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/loop/bridge.py); [src/maref/execution/harness/unified.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/execution/harness/unified.py); [src/maref/execution/multi_agent/coordinator.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/execution/multi_agent/coordinator.py); [src/maref/codegen/loop.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/codegen/loop.py)
- Basis: structural
- Confidence: moderate
- Caveats: There may be bespoke client deployments with human operational management; not credited at the default source boundary.

### Absence scope

- Surfaces inspected: Default governed loop, unified harness, multi-harness coordinator, governance state and circuit-breaker paths.
- Plausible first-party paths checked: Portfolio/global priority allocation, negotiated resource limits between independently continuing S1 cells, managerial exception decisions and returned work instructions.
- Why no material first-party path remains: Inspected controls have only per-run state/transitions or externally supplied policy; no first-party whole-system commitments and corrective return to continuing S1 operations.


## S3* — Complementary audit

- State: —
- Function: Complement routine managerial reports with an independent audit of operational reality and deliver discrepancies to an S3 management owner.
- Disturbance / variety regulated: A first-party agent's own completion/health claims might be inaccurate or misleading.
- Decisive decision or feedback right: Independently inspect across reporting lines, judge discrepancies, and return findings to current organizational management for corrective intervention.
- Decision owner: First-party AST/test/quality checkers, HMAC audit logs and verification registries primarily attest task/work-product facts; no independent complementary S3* reviewer and S3 feedback owner are evidenced.
- Supporting / enforcement mechanisms: Audit hash chains, snapshot/provenance and verifier consensus, source lint/tests, separate ratchet configuration guard.
- Closure path: A failed code check blocks/rolls back the same code-change pipeline; its result does not challenge an S3 manager's global report through a distinct organizational channel.
- Boundary reachability: No material S3* relation established; source verifies code/safety and records transitions, but this does not prove audit of an S3 account.
- Why this is / is not agent-owned: No material eligible first-party VSM function closure at the assessed organizational boundary; the cited mechanisms are narrower.
- Evidence: [src/maref/recursive/recursive_evolution_loop.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/recursive_evolution_loop.py); [src/maref/recursive/self_executor.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_executor.py); [src/maref/execution/harness/unified.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/execution/harness/unified.py); [src/maref/evolution/constitution_harness.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/evolution/constitution_harness.py); [src/maref/governance/state_machine.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/governance/state_machine.py)
- Basis: structural
- Confidence: moderate-high
- Caveats: The system has substantial audit instrumentation; no claim that auditing is absent in an engineering sense.

### Absence scope

- Surfaces inspected: HMAC-chain audit, Merkle/identity audit, test verification, codegen safety, ratchet guard and ordinary lifecycle reporting.
- Plausible first-party paths checked: Independent challenger of whole-current managerial performance figures and a corrective return into a separate S3 authority.
- Why no material first-party path remains: These paths verify a proposed code change or record run events; no complementary management-report audit and corrective S3 relation is identifiable.


## S4 — Outside-and-then intelligence

- State: C
- Function: Construct prospective changes to the harness's own future coding/verification capability using observed system health, architecture and proposed source evolution.
- Disturbance / variety regulated: Changing module coupling, code coverage, recurring test failures and new technology constraints on future runs.
- Decisive decision or feedback right: Select an adaptation candidate targeting future capabilities and route it through bounded safety/deploy/verify; no separate independent S4 strategy authority is demonstrated.
- Decision owner: The `SelfArchitect` and REL pipeline form first-party prospective options; the model may generate code for a candidate, but constitution/safety and transaction guards bound effect and do not constitute an independent strategic S4 regulator.
- Supporting / enforcement mechanisms: `SelfObserver.observe_codebase`/test coverage, `SelfDiagnostician`, `SelfArchitect.propose_all`, code generation, transactional deploy, tests, divergence detector and rollback.
- Closure path: Observations about the system's own code/test environment generate future codebase improvement options and can lead to deployed capability modifications after checks; a subsequent observer could evaluate the changed codebase. Unlike mere per-task repair, this path targets the framework's future reusable code and tests.
- Boundary reachability: `RecursiveEvolutionLoop.run_session` wires OBSERVE→DIAGNOSE→ARCHITECT→CODEGEN→DEPLOY→VERIFY→EVALUATE on the actual source tree. This supports a *constructor-level* prospective adaptation capability, not established stable autonomous S4 organizational governance.
- Why this is / is not agent-owned: The default runtime implements a concrete reusable prospective adaptation constructor but not independently owned strategic S4 authority.
- Evidence: [src/maref/recursive/recursive_evolution_loop.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/recursive_evolution_loop.py); [src/maref/recursive/self_observer.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_observer.py); [src/maref/recursive/self_diagnostician.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_diagnostician.py); [src/maref/recursive/self_architect.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_architect.py); [src/maref/recursive/llm_code_generator.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/llm_code_generator.py); [src/maref/recursive/self_executor.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/self_executor.py)
- Basis: structural
- Confidence: moderate
- Caveats: A test/coverage driven self-modifier is narrower than environmental market/strategy forecasting. It does not prove independent future-option appraisal or safe live deployment; S4=A would be unsupported.

### Prospective adaptation boundary

- External distinction: The observed repository module graph, test failures, toolchain and code environment are outside the particular coding agent work turn, but are not claims of future market sensing.
- Future / prospective distinction: The adaptation addresses future reusable code/test capability, rather than simply producing the currently assigned user answer; it is narrow internal capability evolution.
- Adaptation option generated: `SelfArchitect` constructs alternative refactor/test/import cleanup proposals; `LLMCodeGenerator` generates one selected candidate as source.
- Path back into current capability / S3: REL can deploy and verify a codebase update, or roll it back. This changes available code for subsequent S1 runs, without establishing a legitimate whole-organization S3 strategy dialogue.


## S5 — Policy and identity

- State: —
- Function: Legitimately arbitrate ultimate identity/purpose and constitutional policy for the agent organization and return it as operative authority.
- Disturbance / variety regulated: Conflicts about permitted autonomous modification, safety red lines, final system identity and legitimate governance changes.
- Decisive decision or feedback right: A legitimate S5 decision owner must adopt/revise ultimate policy and make an operative authority change that governs future S1 behavior.
- Decision owner: A `ConstitutionHarness` compares strings and actor labels against fixed protected paths; there is no authenticated first-party organizational constitutional decision owner or policy-change transaction in the assessed runtime.
- Supporting / enforcement mechanisms: `ConstitutionHarness`, freeze zones, safety state machine, rule/policy defaults and immutable-file restrictions.
- Closure path: `check_change` returns allowed/blocked for source modifications based on hard-coded rule lists, with `actor='human_constitution_maker'` exempting selected red-line tests; neither verified human authority nor ultimate system-level policy adoption and return is shown.
- Boundary reachability: Literal human-role string, governance slogans and static red-lines cannot be reclassified as a legitimate parent S5 function.
- Why this is / is not agent-owned: No material eligible first-party VSM function closure at the assessed organizational boundary; the cited mechanisms are narrower.
- Evidence: [src/maref/evolution/constitution_harness.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/evolution/constitution_harness.py); [src/maref/governance/state_machine.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/governance/state_machine.py); [README.md](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/README.md); [src/maref/recursive/recursive_evolution_loop.py](https://github.com/maref-org/maref/blob/35b1d8108887bf162711c2212b7a67d6e21d9342/src/maref/recursive/recursive_evolution_loop.py)
- Basis: structural
- Confidence: moderate-high
- Caveats: Real organizations maintaining/using MAREF may have independent human constitutional authority; no first-party default supporting return loop was established.

### Absence scope

- Surfaces inspected: Constitution guard, static policy predicates, governance/FSM, identity and security documentation, default codegen evolution entry.
- Plausible first-party paths checked: Human-authenticated approval changing legitimate organizational purpose or red-line policy, followed by a runtime return that enforces the new constitutional decision.
- Why no material first-party path remains: Checks implement static developer constraints and file-label privileges; they neither validate the ultimate legitimate human holder nor close a revision/policy identity decision over an autonomous organization.

## Distributed OSS parent arrangement

The maintainers and OSS governance of the repository are not automatically a human operating S5 for an autonomous MAREF instance. No multi-tenant deployed S1 parent organization is present in the pinned source. External client agents and their parent organization do not transfer VSM ownership to the MAREF library.

## Self-hosted and non-human modes

The configured codegen path can run with OpenAI or Anthropic credentials and mutate source files subject to safety gates. With no provider it falls back to a mock/deterministic path and must not count as model-backed autonomy. A real human may govern protected files, but a code-level actor string or preconfigured policy does not prove authentication/constitutional authority. No full non-human ultimate constitutional decision is claimed.

## Recursion

The recursive evolution pipeline is one source-code work cell. `MultiAgentCoordinator` dispatches supplied harness calls and is not itself a recursively viable organization; one controller plus role labels does not create a multi-level VSM by declaration.

## Variety and escalation

Unstable generated code, syntax errors and safety violations are controlled by AST/safety gates, transaction snapshots, and rollback. Tool/runtime faults can trigger circuit breakers; these are bounded operational protections, not demonstrated algedonic escalation from lower viable units to a separately constituted S3/S5. A model-driven change passing a safety predicate is not the same as a democratically/constitutionally authorized global policy revision.

## Evidence gaps

- Strong S1 reachability is pinned-source structural evidence; no live provider credential, effectful run, long-lived agent workload or production service outcome was observed.
- S4=C is specifically confined to a future code/test capability modifier. No market sensing, enterprise strategy committee, managerial S3–S4 dialogue or demonstrated measurable benefit after the change is claimed.
- External LangGraph/CrewAI model/tool loops are not inherited. Default governance overlay/FSM, separate model-free fallback and test fixtures are credited only as supporting controls.
- Formal and cryptographic safety claims in README are not independently verified by this VSM assessment. Tests or TLA+ artifacts cannot be substituted for functional closure.
