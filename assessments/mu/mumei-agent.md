---
harness_id: mumei-agent
project_name: Mumei Agent
repository: https://github.com/mumei-lang/mumei-agent
review_ref: c9fc09cd22302ab5590ca2b2d664b8423bf7949d
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Mumei Agent

## Review boundary

- System in focus: The installed Mumei Agent CLI/MCP verification-guided code generation, repair, audit and optional proliferation runtime.
- Purpose and identity: Generate, repair and assess code against explicit contracts using model proposals and formal/native evidence.
- Relevant environment: Source repositories, specifications, compiler/Z3 reports, native execution results, model providers and operator budgets.
- Standard-distribution boundary: Packaged heal/generate/forge/audit/proliferate commands and MCP-facing equivalents; compiler/Lean/native toolchains supply evidence, not automatically harness-owned agent judgment.
- Credited operating / distribution surfaces: CLI dispatch, classic and structured self-correction, code generation, parallel forge dependency staging/publication, controls gate, audit/native replay, charter guards and benchmark-feedback consumers.
- Adjacent first-party surfaces excluded from ownership: Compiler implementation in the separate mumei repository, maintainer scheduled workflows, benchmarks, evaluation reports and repository-development governance. They may supply inputs but cannot donate runtime decision ownership.
- First-party operating / deployment modes considered: Local CLI heal/generate, opt-in structured self-correction, audit with optional native replay/auto-migrate/auto-heal, proliferate basic/self_evolution/full with configured parallel forge workers, and MCP integration.
- Recursion level: One deployed harness instance; nested execution is not presumed recursively viable.
- Reviewed revision: c9fc09cd22302ab5590ca2b2d664b8423bf7949d
- Observation date: 2026-11-19
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Heal snapshots source and optional charter, invokes the configured verifier, sends failures to a model for repairs, writes candidates and re-verifies under attempt/budget/erosion limits. Generate and forge construct code from specifications. Proliferate identifies target-library gaps, generates candidate specs and code, stages verified dependency code/lemmas, schedules ready workers, then publishes dependency groups with blast-radius checks and rollback. Audit extracts contracts from external source and can add native replay, migration hints and healing. Pattern/benchmark feedback guides later generation. This is not evidence that a compiler, benchmark or maintainer workflow is an autonomous metasystem of the agent harness.

## Operational model

Model-led code generation and repair workers are S1 units. Parallel workers can produce mutually dependent library artifacts, so verified-dependency staging and failure propagation are assessed as a concrete S2 constructor. Audit is also a product operation; its name does not by itself make it an independent audit of the harness own operational claims.

## S1 — Operations

- State: A
- Function: Generate and repair code against contract/verification feedback.
- Disturbance / variety regulated: Unknown code defects, failed proof obligations and malformed generated candidates.
- Decisive decision or feedback right: Choose revised code/repair proposals from source, specification and returned failures.
- Decision owner: Configured LLM generator/repair actor in the packaged CLI/MCP loop.
- Supporting / enforcement mechanisms: Verifier subprocess/MCP transport, backups, charter/erosion checks, retry history, toolchain and budget limits.
- Closure path: Source is verified, failures are sent to the model, candidate code is written and checked again; bounded termination preserves success/failure.
- Why this is / is not agent-owned: The model owns discretionary code changes; deterministic acceptance cannot invent a repair after that actor is removed.
- Evidence: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/self_healing.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/self_healing.py); [agent/generate.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/generate.py); [agent/forge.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/forge.py); [agent/self_correction.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/self_correction.py)
- Basis: structural
- Confidence: high
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Boundary reachability: CLI dispatch invokes the first-party heal/generate/forge implementations, which construct configured model clients and consume verifier feedback.

## S2 — Coordination

- State: C
- Function: Regulate interference among parallel forge units producing dependent code artifacts.
- Disturbance / variety regulated: A dependent worker using unverified or failed in-batch dependency code, and partial publication breaking sibling/dependent artifacts.
- Decisive decision or feedback right: Compose dependency/worker policy and response over verified completion, failure propagation and dependency-group publication.
- Decision owner: Developer/operator composes specifications, worker settings and coordination policy; packaged scheduling/rollback enforces it. No autonomous coordination actor is credited.
- Supporting / enforcement mechanisms: Dependency graph/cycle detection, shared verified staging directory and lemma board, board lock, pending/completed maps and group rollback.
- Closure path: Only workers whose dependencies completed verified are dispatched with staged code/lemmas; failed dependencies suppress dependents; a failed publication group restores originals.
- Why this is / is not agent-owned: The S2-specific dependency and publication path is supplied, but model-owned revision of coordination policy is not installed.
- Evidence: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/proliferate.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/proliferate.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Distinct S1 units: Separate model-led forge workers for different target modules.
- Inter-S1 disturbance: In-batch code dependencies can make one worker verification/publication invalidate or outrun another worker artifact.
- Attenuating coordination relation: Wait for verified dependency completion, propagate exact code/lemmas, reject failed/cyclic dependencies and publish connected dependency groups with rollback.
- Feedback into subsequent S1 behaviour: Worker eligibility and generation inputs change with predecessor results; group failure prevents acceptance of the affected artifacts.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The mechanism binds identified code dependencies and cross-artifact blast-radius failures to worker suppression, revised inputs and atomic restoration, beyond an arbitrary task sequence.
- Boundary reachability: Supported proliferate accepts parallel-forge-workers and routes specs through _parallel_forge and _publish_dependency_group; this is production code rather than a CI-only scheduler.

## S3 — Inside-and-now control

- State: —
- Function: No established whole-harness current-control loop.
- Disturbance / variety regulated: Whole-current resource/commitment tensions.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Attempt schedules, budget policies, proposal limits, health metrics and deterministic rollback.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Local repair strategy and configured worker/attempt limits do not establish an agent-owned whole-system allocation/commitment decision.
- Evidence: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/budget_policy.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/budget_policy.py); [agent/attempt_schedule.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/attempt_schedule.py); [agent/proliferate.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/proliferate.py); [agent/meta_architect.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/meta_architect.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/budget_policy.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/budget_policy.py); [agent/attempt_schedule.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/attempt_schedule.py); [agent/proliferate.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/proliferate.py); [agent/meta_architect.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/meta_architect.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Budget/attempt policy, proliferation health and grouped rollback, MetaArchitect refactoring.
- Why no material first-party path remains: Inspected decisions regulate target-code repair/generation or enforce supplied limits; no whole-harness current-control owner/return is supplied.

## S3* — Complementary audit

- State: ?
- Function: Potential complementary check of generated verification/semantic claims remains unresolved.
- Disturbance / variety regulated: A formally accepted contract may be too weak or diverge from actual native behavior.
- Decisive decision or feedback right: Unresolved independent discretionary audit scope/ownership for harness-generated success claims.
- Decision owner: Model extraction/repair actors and deterministic compiler/replay mechanisms are visible; qualifying separate audit-decision ownership is not established.
- Supporting / enforcement mechanisms: ControlsGate mutation results, native replay, body-port reconciliation and auto-heal/migration feedback.
- Closure path: Controls can request retries or reject candidates; audit can produce migration/healing actions. Whether these close a complementary organizational audit at this recursion remains unresolved.
- Why this is / is not agent-owned: Complementary evidence exists, but a routine verifier pipeline and an audit product do not alone establish sufficiently independent harness audit judgment.
- Evidence: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/controls_gate.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/controls_gate.py); [agent/native_replay.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/native_replay.py); [agent/audit.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/audit.py)
- Basis: structural
- Confidence: low
- Caveats: No positive S3* state and no bounded absence claim; concrete controls/native-replay ownership gap is retained.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then adaptation closure for the agent harness established.
- Disturbance / variety regulated: Changing future external operating requirements.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Pattern library, gap proposals, benchmark-driven domain priorities and self_evolution search profile.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: These improve target-library generation or reuse local repair experience; a profile name does not establish future-environment adaptation of the harness.
- Evidence: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/proliferate.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/proliferate.py); [agent/benchmark_feedback.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/benchmark_feedback.py); [agent/pattern_library.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/pattern_library.py); [agent/harness_ablation.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/harness_ablation.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/proliferate.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/proliferate.py); [agent/benchmark_feedback.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/benchmark_feedback.py); [agent/pattern_library.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/pattern_library.py); [agent/harness_ablation.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/harness_ablation.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Gap analysis, benchmark-generated proposals, repair patterns and optional self_evolution/full search.
- Why no material first-party path remains: The visible feedback develops operational target-code work from local gaps/benchmarks, without an externally prospective harness-capability decision and return.

## S5 — Policy and identity

- State: —
- Function: No returned ultimate-policy authority loop established.
- Disturbance / variety regulated: Disputes about harness identity/ultimate policy.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Pinned charter, tamper detection, erosion protection, configured guards and command flags.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Charter enforcement stops or restores code; it does not decide identity/policy issues or return an authoritative policy revision.
- Evidence: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/charter_guard.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/charter_guard.py); [agent/self_healing.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/self_healing.py); [docs/CONFIGURATION.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CONFIGURATION.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/README.md); [docs/CLI_GUIDE.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CLI_GUIDE.md); [agent/__main__.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/__main__.py); [agent/charter_guard.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/charter_guard.py); [agent/self_healing.py](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/agent/self_healing.py); [docs/CONFIGURATION.md](https://github.com/mumei-lang/mumei-agent/blob/c9fc09cd22302ab5590ca2b2d664b8423bf7949d/docs/CONFIGURATION.md); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Charter discovery/check/tamper handling and operator allow-contract-erosion mode.
- Why no material first-party path remains: Static charter/configuration enforcement and ordinary acceptance choices supply no identity-issue escalation → legitimate authority decision → returned operational policy.

## Distributed OSS parent arrangement

Repository maintenance and contributor approvals are outside the deployed product recursion. Multiple contributors do not establish organization-level parent governance in the assessed harness.

## Self-hosted and non-human modes

Self-hosting and provider choice are supported. Operator configuration or ordinary tool approval alone does not establish a parent-governed S3/S4/S5 mode.

## Recursion

No claim of recursively complete VSM units is made. Execution phases, provider instances and nested calls do not establish recursive viability.

## Variety and escalation

Verifier counterexamples and contract/controls failures feed repair attempts; bounds can stop or restore source. Dependency failures prevent downstream generation/publication. PR creation and health summaries expose outcomes, without proving a parent authority loop.

## Evidence gaps

No live compiler/model/native-replay run was performed. S3* remains specifically unresolved: native replay and mutation controls offer materially alternative evidence, but source tracing did not establish their independent discretionary audit ownership and corrective-control relation for harness-generated success claims across the supported modes. Product audit of arbitrary input code is not automatically S3*. This is the concrete reason for ? rather than an unsupported absence or positive grade.
