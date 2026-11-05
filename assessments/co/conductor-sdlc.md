---
harness_id: conductor-sdlc
project_name: Conductor SDLC
repository: https://github.com/xpressabhi/agentic-sdlc-control-plane
review_ref: 60da52f1806dc5b2fe3297493224fe243d653d7f
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Conductor SDLC

## Review boundary

- System in focus: one self-hosted Conductor orchestration run in its shipped URL-shortener/SDLC scenarios, including typed stage DAGs, agent execution mode, policy/exit gates, approval inbox, stored artifacts, re-planning and audit.
- Purpose and identity: create and validate a governed chain of software-delivery artifacts, preserving stage provenance and allowing controlled retry/rollback/re-plan rather than treating a single generated answer as a release.
- Relevant environment: ambiguous software requirements, real shortener source and tests, parallel design/test/implementation artifacts, unsafe secret-bearing output, stage failures and blocked human release approvals.
- Standard-distribution boundary: first-party Python engine, stage/agent registry, deterministic reference agents, optional `LLMAgent` over an OpenAI-compatible endpoint, scenarios, SQLite state, policy/gates, dashboard and API. The URL shortener is the contained demonstration workspace, not a second S1 governance owner; external model vendor and deployment operator are dependencies.
- Credited operating / distribution surfaces: [README](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/README.md), [engine and runtime dispatch](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py), [optional LLM adapter](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/agents/llm.py), [reference agents](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/agents/reference.py), [gate registry](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/gates.py), [policy](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/policy.py), [audit chain](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/audit.py).
- Adjacent first-party surfaces excluded from ownership: URL redirect serving/analytics as customer application operations, Docker/dev CI, assignment write-ups, unreleased production migration roadmap, tester fixtures and dashboard presentation without action wiring.
- First-party operating modes considered: default deterministic `reference` agents; optional `ASDLC_AGENT_MODE=llm` with configured endpoint/key; greenfield/brownfield/ambiguous YAML scenarios; API or CLI; production prohibition on auto-approval versus explicit demo-only recorded reviewer.
- Recursion level: a single governed SDLC run with stage-level work cells, current DAG and operator; not the whole software organization or an external model-provider company.
- Reviewed revision: `60da52f1806dc5b2fe3297493224fe243d653d7f`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The engine reads a typed workflow, schedules ready stages by dependency level (with parallel independent branches and joins), asks each named agent to produce artifacts/decisions, and checks the result with separate policy and exit-gate modules before committing artifacts. A stage failure can retry, use a fallback agent, compensate or safe-stop. Human approval gates pause the run; approved re-planning resets a downstream impact closure and versions new artifacts. An append-only hash-chained event log and SQLite persistence expose the history to the API/dashboard. The default reference agents are deterministic implementations; only the configured optional LLM adapter asks a model to choose stage content. [Engine](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py); [agent contract](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/docs/AGENT_MODEL.md); [orchestration semantics](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/docs/ORCHESTRATION.md).

## Operational model

An `LLMAgent` wraps a reference stage agent when both `agent_mode == "llm"` and a configured key exist. It sends requirements, upstream artifacts, attempt and replan context to the model, parses returned JSON artifacts/decisions, and sends failures into the engine's retry/fallback route. It does **not** implement a general autonomous shell/tool loop inside that model invocation. In default mode work is scripted; autonomous model ownership is **mode-specific**, and execution engine/gates remain deterministic constructors. This boundary avoids crediting the project's marketing term “agentic” in place of deployed model decisions. [LLM source](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/agents/llm.py); [engine agent selection](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py).

## S1 — Operations

- State: A
- Function: produce bounded software-development stage artifacts and decisions under changing requirements and upstream evidence.
- Disturbance / variety regulated: ambiguous requirements, implementation/test divergence, broken validations, changed upstream design and model-generated content variance.
- Decisive decision or feedback right: in the supported LLM mode, a model selects the semantic content of artifacts and recorded decisions in a named stage; failed output is rejected and the adapter/engine may invoke a fresh attempt or deterministic fallback.
- Decision owner: per-stage `LLMAgent` model call with first-party context/result adapter. Reference agents own **no** model discretion in default mode.
- Supporting / enforcement mechanisms: `AgentContext`, JSON artifact contract, named stage registry, bounded attempts, artifact store, gate/policy results and versioned downstream context.
- Closure path: stage/context and predecessors → model produces artifact/decision JSON → engine evaluates returned artifact → acceptance or failure/retry/replan feedback → stage output conditions subsequent stages.
- Boundary reachability: `_agent_for` in the deployed engine dynamically wraps reference agents with `LLMAgent` when enabled, and scenarios contain stages with specific output gates.
- Why this is / is not agent-owned: configured LLM makes material semantic artifact decisions; deterministic reference/default runs do not. The model has no general unsandboxed tool-execution right from this adapter.
- Evidence: [model adapter](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/agents/llm.py), [agent selection and output return](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py).
- Basis: source-grounded optional-mode execution wiring; no live provider call or evaluation success asserted.
- Confidence: medium-high that decisions reach stage artifacts, lower for real-world model-output quality.
- Caveats: default `reference` mode is deterministic; no general multi-step coding agent or dynamic use of repo tools is inferred for one LLM call.

## S2 — Coordination

- State: C
- Function: coordinate parallel stage dependencies and attenuate interference when an upstream decision invalidates work already produced by dependent cells.
- Disturbance / variety regulated: implementation, test-plan and validation branches can be completed with incompatible predecessor versions; a revised requirement or design can make downstream evidence stale.
- Decisive decision or feedback right: stage dependency graph and reverse-dependency closure deterministically choose which stages may start/join and which must be reset when upstream state changes; the human must approve governed replan if required.
- Decision owner: DAG/topological and replan constructors under typed workflow rules, not a separate free-discretionary coordinating model.
- Supporting / enforcement mechanisms: `topological_levels`, parallel ready-stage batches, join dependencies, artifact lineage, `downstream_closure`, versioned reset and approval gate.
- Closure path: changed upstream stage/approved replan → graph identifies impacted downstream work → engine marks them stale/pending and reexecutes after prerequisites → refreshed evidence reaches validation/join and recorded run state.
- Boundary reachability: shipped ambiguous scenario and engine `_apply_replan` execute this path; parallel joins exist in greenfield flow.
- Why this is / is not agent-owned: there is a concrete inter-stage dependency-conflict correction and returned changed downstream commitments, but its right is rule/graph-defined, not a model S2 choice.
- Evidence: [graph and impact closure](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/graph.py), [engine replan and batches](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py), [scenarios](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/docs/SCENARIOS.md).
- Basis: explicit graph and execution source; no claim that arbitrary competing agents negotiate resources.
- Confidence: medium; dependency-invalidation S2 is narrow, not a generalized mutual-exclusion fleet controller.
- Caveats: initial topological ordering alone would be weak S2 evidence; the material witness is changed-upstream interference plus correction of dependent work.
- Distinct S1 units: separate requirements/design/implementation/test-plan/validation stage agent invocations with their own bounded artifact deliverables and upstream contracts, including independently ready parallel implementation and test-plan branches.
- Inter-S1 disturbance: a revised requirements/design or implementation artifact invalidates downstream tests, validation and release evidence derived from its former version; proceeding without feedback would combine incompatible work-cell results.
- Attenuating coordination relation: approved re-plan computes the reverse-dependency impact closure, marks affected stages stale/pending and runs them only after compatible predecessor outputs are available, retaining lineage for detection.
- Feedback into subsequent S1 behaviour: downstream stage contexts receive refreshed upstream artifact versions and `replan_reason` on their next execution instead of continuing with stale work, and new output goes back through joined validations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the additional invalidation-and-rerun path explicitly responds to cross-stage version interference caused by an upstream change; initial DAG topological order or artifact passing alone would not suffice.

## S3 — Inside-and-now control

- State: C(P)
- Function: govern the present run's stage-portfolio commitments, gate decisions, bounded execution, retries, compensations, stop/resume and human approval.
- Disturbance / variety regulated: failing stages, missing test evidence, a blocked release, excessive attempts, unsafe policy findings and partial rollback.
- Decisive decision or feedback right: the engine uses current stage states, artifact evidence and budgets to select ready stages, retry/fallback or safe-stop; a human approves/rejects release and replans via API/CLI/dashboard.
- Decision owner: deterministic `OrchestrationEngine` current-control constructor (`C`); human operator provides `(P)` approval/stop/override for consequential gates.
- Supporting / enforcement mechanisms: SQLite run/stage state, budgets, gate registry, policy engine, approval records, thread-pool batches, compensation and safe-stop.
- Closure path: current run DAG/artifacts and policy result → engine schedules/pauses/retries/compensates → persisted state and approvals change → subsequent stage allocation observes current outcome.
- Boundary reachability: `execute` runs launched workflows and stage approval pauses; API/CLI expose actual approve, reject, safe-stop, resume and replan endpoints.
- Why this is / is not agent-owned: the engine owns whole-run **current** control but selects from encoded policies; human oversight adds a parent mode, not an autonomous controller. Neither present approval nor DAG replan is prospective S4.
- Whole-system current view: all stage statuses, attempts, current approvals, artifact lineage, blocked dependencies and error/budget states of one run.
- Current-control decision scope: launch/ready-stage admission, failure handling, rollback/safe-stop and resumed work under human gates.
- Evidence: [engine state loop](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py), [API controls](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/api.py), [approval semantics](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/docs/ORCHESTRATION.md).
- Basis: executable deterministic scheduler/approval methods.
- Confidence: high for implemented bounded run control; deployment proof limited to repository code/tests.
- Caveats: demo auto-approval by `demo-reviewer` is barred in production and cannot substitute for a legitimate human release gate.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | First-party deterministic engine | A stage succeeds, fails, exceeds budget or requires replan | current states and rule/gate outcomes → schedule, retry, fallback, rollback or stop → persisted new stage status | [engine](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py) |
| Parent (`P`) | User/release operator | Stage/replan approval pending or task must stop | dashboard/API/CLI approve, reject or safe-stop → engine resumes or terminates with recorded actor/rationale | [approval routes](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/api.py) |

## S3* — Complementary audit

- State: C
- Function: independently challenge a stage agent's claimed acceptable output using policy scans, exit gates, test-evidence requirements and separately verifiable hash-chained event provenance.
- Disturbance / variety regulated: an LLM-generated artifact can contain secrets, miss mandatory evidence or claim tests/release readiness that the run cannot support.
- Decisive decision or feedback right: `PolicyEngine.evaluate` and `check_exit_gate` judge the actual returned artifacts and stored test evidence separately from the agent's summary; policy denial or failed gate rejects output and may trigger bounded retry/fallback. Audit verification checks a separate event chain, but does not prove semantic correctness.
- Decision owner: deterministic policy/gate/audit constructors (`C`), not a distinct adversarial model reviewer.
- Supporting / enforcement mechanisms: rule IDs, artifact/policy input, stored run test evidence, gate registry, denial events, recorded retries and hash-chain verification API.
- Closure path: stage agent emits artifact/claim → policy scanner and gate check actual artifact/record → denial enters stage-attempt failure → engine retries, falls back, stops or requests human approval → new outcome and audit events persist.
- Boundary reachability: `_execute_stage` invokes policy and exit gate on the live agent result before `_persist_success`, so this is not merely an offline report/dashboard.
- Why this is / is not agent-owned: checker accepts independent structured evidence and can veto stage success, but verdict rules are deterministic; no autonomous second critic is evidenced.
- Claim being audited: generated stage artifact is policy-compliant and has sufficient evidence to advance toward release.
- Ordinary reporting path: `AgentResult.summary`, artifact/decision JSON and stage success from reference/LLM agents.
- Complementary access path: first-party policy scans actual artifact content and gate checks stored run test records; the audit verifier independently recomputes event hashes against persisted payload.
- Independence boundary: policy and gate code run outside `LLMAgent` and cannot be rewritten by its JSON response, but some flags (`tests_passed`) are model/result metadata; these checks are not a full independent test execution or formal proof of correctness.
- Who acts on findings: deterministic engine rejects/retries/compensates; human can inspect audit/approval and change further commitments.
- Evidence: [policy and exit gate source](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py), [gate registry](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/gates.py), [policy source](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/policy.py), [audit implementation](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/audit.py).
- Basis: source-implemented independent static checks and corrective return.
- Confidence: high for deterministic policy veto; medium for its ability to catch real-world wrong code.
- Caveats: self-declared test metadata must not be mistaken for separately executed tests; hash chaining detects history tampering but does not establish that reported facts are true.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced external future-sensing, strategic-option comparison and capability-adoption return for the SDLC run.
- Disturbance / variety regulated: new software requirements, future platform changes, changed deployment risk and project evolution may require longer-horizon intelligence.
- Decisive decision or feedback right: `replan` changes current/downstream workflow in response to present changed requirements; releases and roadmaps are manually defined. No S4 owner has an outside-and-then mandate.
- Decision owner: operator and fixed DAG/policy constructors for current work; no distinct future-environment deliberator.
- Supporting / enforcement mechanisms: impact closure, scenario definitions, versioned artifact decisions, release checklist and project documents.
- Closure path: changed requirement resets affected current stages; it does not establish durable selection of a future external operating option affecting the whole system.
- Why this is / is not agent-owned: dynamic re-planning is strong present adaptation but not necessarily VSM S4.
- Evidence: [replan implementation](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/engine.py), [scope and limitations](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/README.md).
- Basis: bounded absence review of future-facing workflows.
- Confidence: medium-high.
- Caveats: project management could later add prospective strategic sensing.

### Absence scope

- Surfaces inspected: scenario YAML and docs, replan and graph, release/approval paths, LLM stage context, architecture and production-roadmap section.
- Plausible first-party paths checked: future requirement analysis, risk register, replan after changed design, release strategy and long-horizon technology choice.
- Why no material first-party path remains: reviewed mechanisms are known-work DAG updates, static policy and manual release planning, without external future sensing and binding capability selection returned to the present controller.

## S5 — Policy and identity

- State: —
- Function: no evidence of charter-level identity/purpose conflict adjudication and legitimate binding return across the entire run.
- Disturbance / variety regulated: security exceptions, licensing conflicts and release risk are concrete current-policy problems, but do not independently establish the ultimate purpose of the agent organization.
- Decisive decision or feedback right: policy rules deny stage outputs, and the human can approve/reject release and re-plan; none of those decisions is shown resolving a fundamental identity dispute or changing the organization's ultimate charter.
- Decision owner: external project owner/developer sets policy; rule engine enforces it. Human release approval does not by itself establish S5(P).
- Supporting / enforcement mechanisms: security/license/change/release rule IDs, approval provenance, demo-only auto-approve ban and safe-stop.
- Closure path: a denial sends a stage back to bounded repair or halts release; no recognized ultimate policy question travels to a legitimate S5 authority and returns as a new whole-system identity commitment.
- Why this is / is not agent-owned: guardrails are regulatory constraints at current work, not autonomous deliberation on organizational identity.
- Evidence: [policy engine](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/src/agentic_sdlc/orchestrator/policy.py), [approval process](https://github.com/xpressabhi/agentic-sdlc-control-plane/blob/60da52f1806dc5b2fe3297493224fe243d653d7f/docs/ORCHESTRATION.md).
- Basis: bounded negative policy/authority inspection.
- Confidence: high for policy enforcement, medium-high for absent identity-level closure.
- Caveats: this does not deny the legitimate human's ultimate ownership of the underlying software project.

### Absence scope

- Surfaces inspected: current-run approval API, policy tags, rule IDs and exceptions, audit actors, auto-approve limitations and release docs.
- Plausible first-party paths checked: licensing denial, secret handling, manual release gates, stage budget stop, operator replan and rollback.
- Why no material first-party path remains: decisions repair or halt current SDLC steps, not resolve identity purpose or assign enduring legitimate constitutional control to a distinct S5.

## Distributed OSS parent arrangement

The GitHub repository and its author's assignment/business governance are outside the one-run operating boundary. Human approver owns current stage gates; no OSS-level identity regulator is imputed solely because the project is a public repository.

## Self-hosted and non-human modes

The app starts without external services in deterministic reference mode, which provides `C` stage constructors but no model-owned S1. The optional configured LLM mode reaches S1 A through artifact generation, while the engine remains deterministic and humans guard consequential release/replan gates. Demo auto-approval is a separate explicitly untrusted demonstration mode and is forbidden when `ASDLC_ENV=production`.

## Recursion

Each stage has a named agent contract and versioned artifact outputs; multiple stage actors form dependent units within one orchestrated run, rather than independently viable organizations. The run-level engine regulates current scheduling and evidence; it is not proof of a multi-company VSM federation.

## Variety and escalation

Model-selected stage artifacts amplify semantic variety. Typed scenarios, DAG join order, policy scans, exit gates, bounded retries, fallback agents, compensation and human approval attenuate output/release risk. Irrecoverable failures safe-stop rather than silently pass. Stage records and hash-chain events expose evidence for human investigation.

## Evidence gaps

- The default mode is fully deterministic; the optional LLM adapter sends a single JSON-stage prompt and relies on model output, with no live key/provider run in this assessment.
- Runtime Python/pytest dependencies are not installed in the local environment, so the upstream test suite could not be executed here; code and documented tests were inspected instead.
- The observed S2 constructor is dependency-invalidation and replan feedback; graph sorting alone would not establish general inter-agent conflict management.
- Policy/gates have a concrete veto path but may trust model metadata for tests; S3* C is therefore a bounded structural checker, not independent semantic code proof.
- Current-run replan and release permission are not external-prospective S4 or an identity-level S5.
