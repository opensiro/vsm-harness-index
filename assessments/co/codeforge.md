---
harness_id: codeforge
project_name: CodeForge
repository: https://github.com/Asem-Saber/CodeForge
review_ref: 30027de1de2831ffceac830129df5ccb9d664881
reviewed_at: 2026-10-30
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

# CodeForge

## Review boundary

- System in focus: CodeForge's installed terminal/headless coding-session harness.
- Purpose and identity: generate, inspect, validate and execute Python code in a per-session sandbox with human approval of edits/runs.
- Relevant environment: user requests, session workspace, Docker daemon/image, OpenAI-compatible provider and optional LangSmith telemetry.
- Standard-distribution boundary: main.py, src/agent, service, tools, sandbox and UI; supported local and Docker Compose deployment of the same session implementation.
- Credited operating / distribution surfaces: model/tool graph, Session send/resume API and per-session sandbox/filesystem tools.
- Adjacent first-party surfaces excluded from ownership: tests, CI/image-build workflows and contributor development are corroborating infrastructure, not an installed metasystem or independent auditor.
- First-party operating / deployment modes considered: local REPL, containerized REPL, headless Session API, resumable SQLite conversations and approval interrupts.
- Recursion level: one coding session; multiple separately listed sessions are not assumed to form a regulated organization.
- Reviewed revision: `30027de1de2831ffceac830129df5ccb9d664881`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[Architecture and gates](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/README.md#L11-L106) describes a LangGraph cycle: model → validation → approval → tools → execution processing → retry → model. [Graph wiring](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/graph.py#L22-L58) directly implements those transitions and SQLite checkpoints. The provider is bound to first-party tools; action results accumulate in AgentState. Validation checks saved Python syntax/import availability before execution, while the human gate interrupts edits and runs, returning denial messages into the model's history. [Session API](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/service/session.py#L38-L79) exposes send/resume and typed events; stats and previews support the operator. [Sandbox lifecycle](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/sandbox/manager.py#L28-L74) supplies per-session bind mounts and Docker limits. There is one model decision loop, not separate validation/audit agents. Persistence and retries recover the current coding task.

## Operational model

The coding agent chooses files, tools and corrective actions; the operator may approve or decline an edit/run. The graph and Docker execute/enforce those choices. Human action veto does not replace all model-owned operational discretion, so this is an included bounded semi-autonomous S1 harness. Multiple graph nodes are phases/support for that S1, rather than multiple operational units. No whole-system metasystem or identity-policy parent loop is inferred from the UI.

## S1 — Operations

- State: A
- Function: produce and repair Python coding results in the session workspace.
- Disturbance / variety regulated: user requirements, file contents, syntax/import errors, execution stdout/stderr and declined actions.
- Decisive decision or feedback right: choose the next read/edit/validation/run request or final answer after feedback.
- Decision owner: model-backed coding agent, bounded by the user's operational veto.
- Supporting / enforcement mechanisms: LangGraph routing, first-party tools, validation/approval gates, Docker restrictions and SQLite persistence.
- Closure path: model tool requests run or yield refusal/error ToolMessages; subsequent graph cycles call the model with accumulated history.
- Boundary reachability: main/Session uses the compiled first-party graph, which binds the actual registered tools and exposes resume decisions.
- Why this is / is not agent-owned: the human approves selected side effects but does not specify every next tool or code revision; removing the model leaves no coding strategy in the graph.
- Evidence: [Model and tool binding](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/nodes.py#L19-L56), [Approval feedback](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/nodes.py#L141-L183), [Closed cycle](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/graph.py#L22-L58).
- Basis: structural.
- Confidence: high.
- Caveats: no provider-backed task executed; approval frequency and deterministic safeguards are not capability or security guarantees.

## S2 — Coordination

- State: —
- Function: no material first-party path established for concurrent operational interference.
- Disturbance / variety regulated: There is one coding agent per assessed session. Validation, approval and execution are phases of that loop; independent sessions have isolated workspaces but no supplied mutual-adjustment relation.
- Decisive decision or feedback right: no qualifying function-specific right evidenced at the declared boundary.
- Decision owner: none established for this VSM function; operational actor/operator/configuration ownership remains as described.
- Supporting / enforcement mechanisms: graph, state, tools, gates and persistence do not inherit a higher function from implementation names.
- Closure path: current-task feedback exists; the distinct closure required for this function is not supplied.
- Why this is / is not agent-owned: absence is function-first, not a deduction from deterministic implementation.
- Evidence: [src/agent/graph.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/graph.py#L22-L54), [src/sandbox/manager.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/sandbox/manager.py#L28-L74).
- Basis: structural.
- Confidence: high within the small inspected distribution.
- Caveats: this is a bounded absence claim; custom external orchestration or future development is outside the assessed mode.

### Absence scope

- Surfaces inspected: graph phases, per-session sandbox/container mapping and session listing.
- Plausible first-party paths checked: parallel tool requests, session isolation and graph routing.
- Why no material first-party path remains: No distinct interacting S1 cells plus interference-specific coordination/feedback path is shipped at the session boundary. Per-session containment does not establish cross-session coordination.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party path established for whole-system current commitments/resources.
- Disturbance / variety regulated: Session stats expose turn/token/retry counters, and the operator answers individual edit/run requests. Fixed MAX_TURNS, MAX_RETRIES, TOKEN_BUDGET and sandbox limits enforce preselected bounds.
- Decisive decision or feedback right: no qualifying function-specific right evidenced at the declared boundary.
- Decision owner: none established for this VSM function; operational actor/operator/configuration ownership remains as described.
- Supporting / enforcement mechanisms: graph, state, tools, gates and persistence do not inherit a higher function from implementation names.
- Closure path: current-task feedback exists; the distinct closure required for this function is not supplied.
- Why this is / is not agent-owned: absence is function-first, not a deduction from deterministic implementation.
- Evidence: [src/service/session.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/service/session.py#L108-L147), [src/config.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/config.py#L19-L24), [src/agent/nodes.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/nodes.py#L266-L319).
- Basis: structural.
- Confidence: high within the small inspected distribution.
- Caveats: this is a bounded absence claim; custom external orchestration or future development is outside the assessed mode.

### Absence scope

- Surfaces inspected: Session stats/resume, model counters, routers, config and Docker lifecycle.
- Plausible first-party paths checked: budget exhaustion, retry ceiling, per-call human approval and sandbox resource caps.
- Why no material first-party path remains: The shipped paths regulate local coding actions with fixed limits; they do not expose a whole-system discretionary resource/commitment controller or a legitimate parent current-control loop. Generic action approval is not sufficient.

## S3* — Complementary audit

- State: —
- Function: no material first-party path established for producer claims that require independent challenge.
- Disturbance / variety regulated: Syntax/import gates and execution-result parsing occur in the ordinary production graph. They provide useful operational checks without a separate sufficiently independent audit judgment/access path.
- Decisive decision or feedback right: no qualifying function-specific right evidenced at the declared boundary.
- Decision owner: none established for this VSM function; operational actor/operator/configuration ownership remains as described.
- Supporting / enforcement mechanisms: graph, state, tools, gates and persistence do not inherit a higher function from implementation names.
- Closure path: current-task feedback exists; the distinct closure required for this function is not supplied.
- Why this is / is not agent-owned: absence is function-first, not a deduction from deterministic implementation.
- Evidence: [src/tools/validation.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/tools/validation.py#L11-L123), [src/agent/nodes.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/nodes.py#L59-L107), [src/agent/nodes.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/nodes.py#L186-L263).
- Basis: structural.
- Confidence: high within the small inspected distribution.
- Caveats: this is a bounded absence claim; custom external orchestration or future development is outside the assessed mode.

### Absence scope

- Surfaces inspected: validation tools/gate, result processing, graph, unit/integration/E2E and CI boundaries.
- Plausible first-party paths checked: AST checking, sandbox imports, execution feedback, optional tracing and developer tests.
- Why no material first-party path remains: All installed checks are routine production feedback; tests/CI belong to development, and tracing stores reports. No complementary auditor can challenge the normal claims and return findings through a distinct installed audit path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path established for external/prospective capability adaptation.
- Disturbance / variety regulated: Package installation repairs current task dependencies. Conversation checkpoints, retries and a fixed prompt preserve or correct current work rather than model environmental futures.
- Decisive decision or feedback right: no qualifying function-specific right evidenced at the declared boundary.
- Decision owner: none established for this VSM function; operational actor/operator/configuration ownership remains as described.
- Supporting / enforcement mechanisms: graph, state, tools, gates and persistence do not inherit a higher function from implementation names.
- Closure path: current-task feedback exists; the distinct closure required for this function is not supplied.
- Why this is / is not agent-owned: absence is function-first, not a deduction from deterministic implementation.
- Evidence: [README.md](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/README.md#L45-L64), [src/prompts.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/prompts.py#L6-L36), [src/agent/graph.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/graph.py#L56-L75).
- Basis: structural.
- Confidence: high within the small inspected distribution.
- Caveats: this is a bounded absence claim; custom external orchestration or future development is outside the assessed mode.

### Absence scope

- Surfaces inspected: package/validation tool architecture, prompts, configuration, session persistence and README.
- Plausible first-party paths checked: dependency installation, retry/error learning, provider selection and developer updates.
- Why no material first-party path remains: No shipped external/future sensing → adaptation-option judgment → returned current-capability loop is supplied, whether agent-owned, a function-specific constructor or parent-governed. General extension/development possibilities are adjacent.

## S5 — Policy and identity

- State: —
- Function: no material first-party path established for identity/ultimate-policy decisions.
- Disturbance / variety regulated: The static safety prompt, environment configuration and user approval gate constrain actions. The interrupted matter is a proposed edit/run, not an identity-level or ultimate-policy dispute.
- Decisive decision or feedback right: no qualifying function-specific right evidenced at the declared boundary.
- Decision owner: none established for this VSM function; operational actor/operator/configuration ownership remains as described.
- Supporting / enforcement mechanisms: graph, state, tools, gates and persistence do not inherit a higher function from implementation names.
- Closure path: current-task feedback exists; the distinct closure required for this function is not supplied.
- Why this is / is not agent-owned: absence is function-first, not a deduction from deterministic implementation.
- Evidence: [src/prompts.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/prompts.py#L3-L37), [src/agent/nodes.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/agent/nodes.py#L125-L183), [src/service/session.py](https://github.com/Asem-Saber/CodeForge/blob/30027de1de2831ffceac830129df5ccb9d664881/src/service/session.py#L47-L59).
- Basis: structural.
- Confidence: high within the small inspected distribution.
- Caveats: this is a bounded absence claim; custom external orchestration or future development is outside the assessed mode.

### Absence scope

- Surfaces inspected: prompt, config, approval normalization/gate, Session resume and deployment instructions.
- Plausible first-party paths checked: human approval, task clarification, secret/provider configuration and static safety rules.
- Why no material first-party path remains: No identity/ultimate-policy matter reaches a legitimate parent authority and returns as binding governance at this recursion. User veto of a concrete code action does not establish P, and static rules do not create A/C.

## Distributed OSS parent arrangement

The public development project and its maintainers are adjacent to installed sessions. No organization-level parent modes are imported from OSS status or CI. The local human action gate is explicitly considered without treating every human decision as S5.

## Self-hosted and non-human modes

Both local and Compose operation use the same graph/Session interface. Docker is external execution support; headless use does not add an autonomous supervisor. No alternative non-human identity/governance mode is supplied.

## Recursion

Graph nodes are not recursively viable units. Session UUIDs, separate containers and checkpoint threads partition operations without demonstrating complete child metasystems.

## Variety and escalation

Errors/denials return in ToolMessages; retry exhaustion and hard budgets terminate locally for user attention. Resume retains pending approval and conversation. These are operational recovery/escalation surfaces without an inferred algedonic channel or higher-function owner.

## Evidence gaps

Frozen source compileall passed. The selected native path test could not collect because the host lacks the Docker Python package; no native-test PASS, live Docker, provider-backed agent E2E or performance claim is made. Static review supports the explicit small-distribution boundary. The README's broad approval/security wording is not treated as an independently verified guarantee; implementation approval covers the named edit/run actions.
