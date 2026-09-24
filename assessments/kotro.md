---
harness_id: kotro
project_name: Kotro
repository: https://github.com/kotro-labs/kotro-proxy-engine
review_ref: 3b07c55ba31af68f3b58f78de2492189b07b23fb
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Kotro

## Review boundary

- System in focus: the first-party `kotro-labs/kotro-proxy-engine` repository at pinned revision `3b07c55ba31af68f3b58f78de2492189b07b23fb`, including the shipped LLM reverse proxy, MCP governed relay, shared mode/kill-switch controls, routing/cache/compression/budget/guardrail machinery, flight recorder, approvals, posture surfaces and experimental frozen Permit runtime.
- Purpose and identity: provide a local coding-agent control membrane on the MCP action path and LLM-provider path, constraining and recording actions/traffic produced by external coding-agent clients while reducing cost and enforcing policy.
- Relevant environment: Claude Code, Cursor, Continue, Cline and other IDE/SDK/agent clients; OpenAI/Anthropic-compatible providers; MCP servers; operator approval/control actions; repositories/workspaces; Docker and other containment backends.
- Standard-distribution boundary: repository-owned proxy, MCP wrapper, policy/schema/TaskEnvelope checks, routing, cache/context controls, budgets, circuit breakers, kill switch, evidence and Permit launch membrane are inside. The autonomous reasoning/model-tool loops of governed coding agents and upstream model providers are environmental actors.
- Credited operating / distribution surfaces: `README.md`; `docs/security/THREAT-MODEL.md`; `rust/kotro-proxy/src/main.rs`; `rust/kotro-proxy/src/router/mod.rs`; `rust/kotro-proxy/src/router/classifier.rs`; `rust/kotro-proxy/src/mcp/wrap.rs`; `rust/kotro-proxy/src/permit/run.rs`; shipped local proxy/control APIs and their standard runtime wiring.
- Adjacent first-party surfaces excluded from ownership: Control Lab roadmap/development work, Escape Lab as a repository-development evaluation corpus except where it documents shipped behavior, demos/tests except as corroboration, future managed bridge work, and Permit roadmap expansion explicitly frozen at the reviewed revision.
- First-party operating / deployment modes considered: local/sidecar LLM reverse proxy; MCP stdio/HTTP wrapper; `disabled`/`audit`/`enforce` governance modes; operator approvals and kill switch; adaptive deterministic model routing; experimental `run --permit` sandbox launch of a supplied agent command.
- Recursion level: one Kotro installation/control membrane. A Claude Code/Cursor/Continue/Cline-style agent behind the membrane is a separate operational organization and its internal reasoning/tool loop is not inherited into this repository-relative assessment.
- Reviewed revision: `3b07c55ba31af68f3b58f78de2492189b07b23fb`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Kotro explicitly positions itself as a local coding-agent control plane rather than a replacement agent runtime. The shipped LLM path is a reverse proxy: first-party handlers receive OpenAI/Anthropic-compatible requests from an external client, apply cache/redaction/compression/routing/budget/circuit-breaker/governance logic, and forward traffic to an upstream provider. The threat model states the boundary directly as `Client (IDE / SDK / agent) → Kotro → Upstream` and calls Kotro a data-plane intermediary.

The MCP path has the same organizational shape. `mcp-wrap` is a governed relay between an external client and an MCP server. It can pin schemas, quarantine drift, validate arguments, enforce TaskEnvelope authority and budgets, require exact-action approvals, honor the kill switch and record evidence. Those are substantial constraints on an agent's action channel, but `check_tool_call` evaluates an action already selected by the client; it does not interpret the task objective, choose the next substantive tool call, observe the result and decide what action follows.

The apparently adaptive model-routing path also remains deterministic support rather than an agent actor. `classifier.rs` uses regex, text length, message count and presence of tool-call history to classify a request into `Nano`, `Micro`, `Standard` or `Complex`, then the proxy routes the already-formed request accordingly. It never owns the external agent's task-level goal or continuation decision.

Experimental Permit does not change the boundary. `run_permit` verifies signed authority, stages the repository, establishes sandbox/data-plane conditions and accepts an explicit `agent_cmd`. It then launches that supplied external agent command in the sandbox and records/returns its outcome. The first-party code owns authority, containment, mediation and evidence around the process; the goal-directed agent behavior remains in the launched command. The frozen README/roadmap further says Permit is experimental/code-frozen and that Kotro's primary direction is Control Lab rather than expansion into an agent runtime.

Counterfactual owner test: remove Claude Code, Cursor/Continue/Cline-style clients, supplied Permit `agent_cmd` processes and upstream model actors while leaving Kotro's proxy, MCP governance, routing, budgets, circuit breakers, approvals, flight recorder and sandbox/authority machinery intact. The remainder can inspect, route, admit, deny, transform, record and constrain hypothetical agent traffic, but it cannot take a task objective and autonomously choose/execute a sequence of substantive task actions. First-party S1 therefore does not close.

Under Methodology `0.3.6`, the terminal standalone result is `excluded-no-agentic-vsm`: rich governance/control machinery around external agents is not published as S2-S5 ownership once qualifying first-party operational S1 is absent at the declared repository boundary.

Primary evidence:

- [`README.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/README.md) — product boundary, external supported coding agents, two governed planes, shared controls and explicit Permit/Control Lab status.
- [`docs/security/THREAT-MODEL.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/docs/security/THREAT-MODEL.md) — shipped client → Kotro → upstream architecture and data-plane-intermediary trust boundary.
- [`rust/kotro-proxy/src/main.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/main.rs) — shipped CLI/control entrypoints, MCP wrapper, approval commands, hooks and Permit command integration.
- [`rust/kotro-proxy/src/router/mod.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/router/mod.rs) — reverse-proxy runtime state and HTTP routes for external model traffic and control/telemetry APIs.
- [`rust/kotro-proxy/src/router/classifier.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/router/classifier.rs) — deterministic request-complexity classification/model-routing support rather than task-level agent reasoning.
- [`rust/kotro-proxy/src/mcp/wrap.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/mcp/wrap.rs) — governed client↔MCP-server relay and deterministic policy/schema/approval/TaskEnvelope checks over client-selected calls.
- [`rust/kotro-proxy/src/permit/run.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/permit/run.rs) — authority/sandbox lifecycle around an externally supplied `agent_cmd` rather than a first-party agent loop.

## S1 — Operations

- State: —
- Function: no first-party autonomous goal-directed operational loop is established inside the Kotro repository boundary at the reviewed revision.
- Disturbance / variety regulated: Kotro regulates model traffic, MCP action admission, prompt/tool-loop risk, budgets, cost, schema drift, authority, containment conditions and evidence; the semantic uncertainty of the coding task and the substantive next-action choice remain with external agent/model actors.
- Decisive decision or feedback right: interpret the task objective, select the next substantive model/tool/workspace action, observe its result and decide what action follows.
- Decision owner: external Claude Code/Cursor/Continue/Cline-style agent client or the externally supplied Permit `agent_cmd`, with upstream model inference as its dependency.
- Supporting / enforcement mechanisms: LLM reverse proxy, deterministic model router, MCP policy/schema gate, TaskEnvelope verification, approvals, budget/circuit breaker, kill switch, cache/compression/redaction, sandbox/Permit lifecycle and flight recorder.
- Closure path: external agent formulates a model/tool action → Kotro admits/transforms/routes/denies/records it → upstream provider or MCP server returns a result → that result returns to the external agent → the external agent decides what substantive action follows. The goal-directed continuation loop therefore crosses Kotro but does not close inside it.
- Boundary reachability: the normal HTTP router is explicitly a proxy for external client requests; `mcp-wrap` is explicitly a client↔relay↔server path; Permit requires and launches a caller-supplied `agent_cmd`.
- Why this is / is not agent-owned: first-party code has strong enforcement authority over allowed traffic and side effects, but it never becomes the actor that owns the task-level model/tool feedback decision. Deterministic request classification is routing support, not semantic operational ownership.
- Evidence: [`README.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/README.md); [`docs/security/THREAT-MODEL.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/docs/security/THREAT-MODEL.md); [`rust/kotro-proxy/src/router/mod.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/router/mod.rs); [`rust/kotro-proxy/src/router/classifier.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/router/classifier.rs); [`rust/kotro-proxy/src/mcp/wrap.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/mcp/wrap.rs); [`rust/kotro-proxy/src/permit/run.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/permit/run.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a wider composed system consisting of Kotro plus a particular coding-agent runtime can contain viable S1, but that is a different system-in-focus requiring its own evidence and cannot donate the external harness's autonomy to Kotro.

### Absence scope

- Surfaces inspected: LLM proxy/router, model-complexity classifier, MCP wrapper/policy/schema/approval path, kill switch/budget/circuit-breaker controls, flight recorder/evidence, hooks and experimental Permit launch lifecycle.
- Plausible first-party paths checked: proxy provider call as S1; model router as planner; MCP policy engine as tool-using actor; circuit breaker as agent regulation; Permit sandbox launcher as agent runtime; flight recorder/Control Lab as an operational actor.
- Why no material first-party path remains: each candidate either constrains/routes an action chosen elsewhere, records/evaluates external behavior, or launches a separate externally supplied agent process. None closes task objective → substantive action → observation → next substantive decision in first-party code.

## S2 — Coordination

- State: —
- Function: no first-party S2 state is published because no population of qualifying first-party autonomous S1 units exists at this repository-relative boundary.
- Disturbance / variety regulated: shared kill switches, budgets, session graphs, action admission and proxy routing can regulate traffic from external agents, but they do not establish a concrete first-party S1-to-S1 disturbance/feedback loop.
- Decisive decision or feedback right: not established over first-party operational units.
- Decision owner: external agents remain the operational actors; Kotro supplies membrane-level constraints.
- Supporting / enforcement mechanisms: per-session scopes, graph/correlation state, MCP governance, rate/budget limits and shared control modes.
- Closure path: constraints can affect multiple external clients, but the qualifying S1 units and their behavioral feedback remain outside the assessed boundary.
- Boundary reachability: these mechanisms are shipped in the proxy/control plane but terminate at external client/action interfaces rather than internal S1 units.
- Why this is / is not agent-owned: session plurality or common gating is not S2 by itself, and no internal S1 population survives the admission test.
- Evidence: [`README.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/README.md); [`rust/kotro-proxy/src/router/mod.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/router/mod.rs); [`rust/kotro-proxy/src/mcp/wrap.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/mcp/wrap.rs).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a composed deployment with multiple external agents may expose coordination relations, but those belong to that wider system rather than Kotro standalone.

### Absence scope

- Surfaces inspected: session/scoping state, graph/correlation controls, shared mode/kill switch, budgets/rate limits, MCP wrapper and Permit execution envelope.
- Plausible first-party paths checked: shared kill switch as S2; session graph as S2; common budgets as S2; MCP mediation as inter-S1 coordination.
- Why no material first-party path remains: there are no first-party autonomous S1 units whose mutual disturbance is closed by these mechanisms.

## S3 — Inside-and-now control

- State: —
- Function: no repository-relative S3 state is published after first-party S1 admission fails.
- Disturbance / variety regulated: current traffic volume, budgets, tool-loop repetition, schema/policy violations, kill state, provider-route conditions and approval requirements are strongly regulated by Kotro.
- Decisive decision or feedback right: Kotro can deterministically admit/deny/route/stop external-agent actions, but no whole-current control right is established over an internal qualifying S1 organization.
- Decision owner: deterministic policy/configuration plus operator approvals/kill controls over external agents' action channels.
- Supporting / enforcement mechanisms: `KOTRO_MODE`, kill switch, request/model routing, budget and loop circuit breakers, approvals, TaskEnvelope checks and proxy/MCP enforcement.
- Closure path: current external-agent request/action → Kotro policy/control evaluation → allowed/routed/blocked outcome → external agent receives the result. This is a control membrane around environmental S1, not S3 ownership over first-party operations.
- Boundary reachability: all cited controls are shipped runtime paths; the negative result is about system boundary and ownership, not feature absence.
- Why this is / is not agent-owned: hard gates, budgets, routing and kill switches are enforcement mechanisms and do not become an S3 owner when the operation they govern remains external.
- Evidence: [`README.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/README.md); [`rust/kotro-proxy/src/router/mod.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/router/mod.rs); [`rust/kotro-proxy/src/router/classifier.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/router/classifier.rs); [`rust/kotro-proxy/src/mcp/wrap.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/mcp/wrap.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this does not minimize Kotro's real governance authority; it preserves the distinction between enforcement over external operations and S3 ownership inside the assessed system.

### Absence scope

- Surfaces inspected: unified mode, kill switch, budget/rate/circuit-breaker controls, routing classifier, approvals, TaskEnvelope and MCP policy engine.
- Plausible first-party paths checked: kill switch as S3 owner; budget controller as S3; adaptive model router as S3; approvals as parent S3; Permit authority as management.
- Why no material first-party path remains: every current-control path acts on external client/model/tool traffic and no internal qualifying S1 whole is established.

## S3* — Complementary audit

- State: —
- Function: no repository-relative S3* state is published after first-party S1 admission fails; evidence/validation does not by itself establish an independent audit function over an internal operational organization.
- Disturbance / variety regulated: Kotro records tamper-evident flight events, detects policy/schema/injection/loop conditions and ships Escape Lab/Control Lab evaluation artifacts around agent-control behavior.
- Decisive decision or feedback right: no independent first-party auditor closes a complementary finding into correction of first-party S1 operation, because the audited operational actor remains external.
- Decision owner: deterministic detectors and operator/security-review surfaces over external traffic.
- Supporting / enforcement mechanisms: flight recorder, dashboard/export/verify APIs, schema telemetry, MCP decisions, injection scanner, circuit-breaker evidence and development/evaluation labs.
- Closure path: external behavior → first-party observation/detection/evidence → operator or external agent/control response. No internal S1 audit/corrective loop closes at this recursion.
- Boundary reachability: runtime evidence surfaces are shipped, while Control Lab is explicitly future/development work at the reviewed ref and is not borrowed as runtime S3*.
- Why this is / is not agent-owned: evidence integrity and anomaly detection are valuable but do not substitute for a complementary audit owner over an admitted first-party operation.
- Evidence: [`README.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/README.md); [`docs/security/THREAT-MODEL.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/docs/security/THREAT-MODEL.md); [`rust/kotro-proxy/src/router/mod.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/router/mod.rs).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a composed external-agent deployment could use Kotro's tape as complementary evidence, but the auditor/operation ownership would need reassessment at that wider boundary.

### Absence scope

- Surfaces inspected: flight recorder, telemetry/dashboard/export/verify APIs, injection/loop/schema findings, Escape Lab claims and Control Lab roadmap.
- Plausible first-party paths checked: flight recorder as S3*; Escape Lab as runtime audit; Control Lab as deployed auditor; schema/injection detection as independent corrective audit.
- Why no material first-party path remains: shipped evidence/detectors observe external operations, and development evaluation does not create a first-party runtime audit loop over internal S1.

## S4 — Outside-and-then intelligence

- State: —
- Function: no deployed first-party prospective adaptation loop is published at the assessed Kotro runtime boundary.
- Disturbance / variety regulated: roadmap, Escape/Control Lab work and evolving backend comparisons can inform future repository development, but they belong to the adjacent product-development/evaluation organization.
- Decisive decision or feedback right: no shipped runtime actor is shown sensing external change, generating a prospective organizational/capability adaptation option and returning the selected option into current first-party operation.
- Decision owner: repository maintainers/operators outside the assessed runtime boundary for roadmap and product evolution.
- Supporting / enforcement mechanisms: roadmap documents, adversarial corpus, Control Lab plans, configuration and update/install distribution outside the claimed runtime adaptation loop.
- Closure path: not established inside the first-party runtime organization.
- Boundary reachability: README explicitly frames Control Lab as the next direction and Permit expansion as frozen; those development choices are not standard-runtime adaptation ownership.
- Why this is / is not agent-owned: future-facing development and evaluation are not automatically S4, especially after the runtime's qualifying operational S1 is absent.
- Evidence: [`README.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/README.md); [`docs/security/THREAT-MODEL.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/docs/security/THREAT-MODEL.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: this is not a claim that the Kotro project does no research/adaptation; it is a repository-runtime boundary finding.

### Absence scope

- Surfaces inspected: Control Lab/Permit status exposed by README, shipped proxy/control configuration, runtime routing and experimental Permit path.
- Plausible first-party paths checked: Control Lab as S4; Escape Lab as environmental intelligence; model routing as adaptation; Permit roadmap decisions as S4.
- Why no material first-party path remains: labs/roadmaps belong to development/evaluation, while runtime routing reacts to present requests rather than creating and returning a prospective organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure is established for a qualifying internal operational organization.
- Disturbance / variety regulated: Kotro exposes policies, TaskEnvelope authority, approvals, trust/mode configuration and kill-switch controls, but these are constraints and parent/operator mechanisms around external agent traffic.
- Decisive decision or feedback right: no path is shown from an organizational identity/ultimate-policy issue to legitimate ultimate authority and back into subsequent first-party operation as an authoritative S5 decision.
- Decision owner: not established as S5 inside the assessed runtime boundary.
- Supporting / enforcement mechanisms: policy engine, TaskEnvelope verification, exact-action approvals, control token, `KOTRO_MODE`, kill switch and Permit authority.
- Closure path: operational policy checks can allow/deny external actions; no identity/ultimate-policy issue/authority/return loop is established.
- Boundary reachability: cited policy mechanisms are shipped and reachable, but their function is action admission/current constraint rather than S5 identity governance.
- Why this is / is not agent-owned: policy vocabulary, signatures, approvals and ultimate-looking kill controls do not establish S5 by naming or importance alone.
- Evidence: [`README.md`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/README.md); [`rust/kotro-proxy/src/mcp/wrap.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/mcp/wrap.rs); [`rust/kotro-proxy/src/permit/run.rs`](https://github.com/kotro-labs/kotro-proxy-engine/blob/3b07c55ba31af68f3b58f78de2492189b07b23fb/rust/kotro-proxy/src/permit/run.rs).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: operator ownership of approvals/kill switches or signed task authority is not automatically S5; functions are classified by organizational role, not apparent authority level.

### Absence scope

- Surfaces inspected: MCP policy engine, TaskEnvelope authority, exact-action approvals, control API/token, kill switch, governance mode, Permit authority and repository-development roadmap/governance.
- Plausible first-party paths checked: signed authority as S5; `KOTRO_MODE` as constitutional identity; operator approval as parent S5; kill switch as ultimate authority; repository maintainers as runtime parent S5.
- Why no material first-party path remains: these mechanisms constrain lower-level actions or belong to adjacent project governance; no runtime identity/ultimate-policy closure is established.

## Distributed OSS parent arrangement

Public Kotro maintainers are not treated as the parent of a running installation merely because they publish releases and roadmap decisions. Local operator approvals, mode selection and kill controls govern concrete external-agent actions, but those lower-level rights are not promoted into S5. A composed organization containing Kotro plus an agent runtime may assign different parent relationships and requires a separate assessment.

## Self-hosted and non-human modes

The default local/self-hosted distribution preserves the same boundary across modes: `disabled`, `audit` and `enforce` change how strongly Kotro evaluates or blocks external-agent traffic, not who owns the agent's goal-directed operational reasoning. Permit similarly changes containment/authority around a supplied agent command without internalizing that command's reasoning loop.

## Recursion

Claude Code, Cursor, Continue, Cline or another coding-agent harness behind Kotro may itself form a viable system at its own recursion. Kotro can regulate that external system's model/tool channels and evidence membrane, but this standalone assessment does not inherit the downstream harness's S1-S5 states. A deployment combining both is a separate system-in-focus.

## Variety and escalation

Kotro meaningfully attenuates variety through schema admission, policy checks, TaskEnvelope authority, budgets, circuit breakers, mode/kill controls, prompt scanning/redaction, caching, routing and sandbox constraints. It amplifies observability through a flight recorder, dashboard and replayable evidence. Escalation can reach an operator through exact-action approvals or control surfaces. These are material control mechanisms, but under the declared repository boundary they regulate external agent operations rather than closing a first-party viable agent organization.

## Evidence gaps

- No positive S-function state is published because the first-party admission gate fails at S1; this does not assert that Kotro's governance features are weak or irrelevant in a composed organization.
- The frozen Permit path is executable but explicitly wraps a caller-supplied `agent_cmd`; if a later revision adds a first-party goal-directed model/tool actor rather than only a launch/governance membrane, reassess at that new ref.
- Control Lab is a development/evaluation direction at this revision and must not be treated as deployed runtime S3* or S4 evidence.
