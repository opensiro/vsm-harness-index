---
harness_id: uh-universal-harness
project_name: UH — Universal Harness
repository: https://github.com/Antoine-Thomas/UH-Universal-Harness
review_ref: 5b63113bc6096779500bb1c99e624919bcf48fc0
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# UH — Universal Harness

## Review boundary

- System in focus: one user-operated installation of UH, serving local CLI and cockpit sessions.
- Purpose and identity: provider-agnostic, local-first tool-using assistant under installation-owner control.
- Relevant environment: the operator, the workspace and host, local or configured remote inference, MCP tool servers, and optional UHB-backed knowledge sources.
- Standard-distribution boundary: the installed Python package and its first-party CLI, web cockpit, provider adapters/router, toolsets, session store and optional Dream/repair workflows.
- Credited operating / distribution surfaces: `uh chat`, `uh web`, bundled toolset and provider APIs, persisted installation policy, optional UHB-backed `uh dream` and the shipped `uh fix` entry point.
- Adjacent first-party surfaces excluded from ownership: contributor and release workflows, tests and roadmap commitments. A worktree that exposes repair code is covered only as the supported input of the repair interface. External UHB, model endpoints and MCP servers supply dependencies or data.
- First-party operating / deployment modes considered: local CLI, local cockpit with an optional remote provider, explicitly configured free-provider router, and optional idle/scheduled Dream pass.
- Recursion level: one UH installation; agent task sessions are its operational units.
- Reviewed revision: `5b63113bc6096779500bb1c99e624919bcf48fc0`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The CLI and cockpit use `ChatSession` and `run_turn`. The loop calls the selected provider, executes model-selected tool calls, and returns tool results into the conversation. The cockpit stores sessions and decisions, exposes aggregated telemetry and permits operator changes to deployment defaults. Dream uses a separate scheduler, reads knowledge/tool inventories and emits reports. Repair proposes a patch against a checkout and applies it only through a separate operator action. The model and UHB are external providers; UH supplies the turn, runtime policy, and optional report workflows. [docs/ARCHITECTURE.md](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/docs/ARCHITECTURE.md#L1-L79), [uh/agent.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/agent.py#L261-L344), [README.md](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/README.md#L165-L173).

## Operational model

A session accepts an operator goal, makes model-directed choices over admitted tools and returns the resulting task output. Installation-wide resource and trust decisions sit with the local operator. Tool approval and iteration bounds delimit the delegated task right. Provider fallback, journaling and persistence support the session. Dream analysis and patch proposals have separate entry points and return different artifacts.

## S1 — Operations

- State: A
- Function: Complete user-directed work through a tool-using session.
- Disturbance / variety regulated: Different tasks, tool results, failed tool calls and incomplete intermediate outputs.
- Decisive decision or feedback right: Select the next admitted tool call and its arguments, revise the task response using results, or finish the turn.
- Decision owner: The session's model-backed agent in the first-party turn loop.
- Supporting / enforcement mechanisms: Tool definitions, result/error transport, context preparation, iteration limit and optional remote-tool approval.
- Closure path: The response proposes a tool call, the tool result enters history and the next model iteration acts on it or returns the final answer; the session emits and records the result.
- Boundary reachability: CLI and cockpit invoke `ChatSession`, which directly binds the provider and admitted toolsets to `run_turn`.
- Why this is / is not agent-owned: The runtime executes bounded decisions while the model chooses how to proceed within them. The operator can stop a turn and gate remote tools.
- Evidence: [uh/agent.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/agent.py#L261-L344), [uh/console.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/console.py#L403-L475), [uh/console.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/console.py#L600-L631), [docs/ARCHITECTURE.md](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/docs/ARCHITECTURE.md#L47-L66).
- Basis: Implemented turn loop and supported entry-point wiring.
- Confidence: High.
- Caveats: Scope is task execution within a session.

## S2 — Coordination

- State: —
- Function: Attenuate interference between concurrent operational sessions.
- Disturbance / variety regulated: Potential contention for workspace, processing and provider capacity.
- Decisive decision or feedback right: An inter-session coordination outcome that changes subsequent behaviour of distinct sessions.
- Decision owner: No first-party witness in the reviewed modes.
- Supporting / enforcement mechanisms: Per-session histories, provider ordering/cooldown and host-idle scheduling for Dream.
- Closure path: No inter-session feedback relation reconstructed.
- Why this is / is not agent-owned: Tool sequencing operates inside one turn. Provider fallback handles inference availability for calls. Dream's daemon observes host idle state and runs a bounded background pass.
- Evidence: [uh/agent.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/agent.py#L290-L344), [uh/router/provider.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/router/provider.py#L26-L91), [uh/dream_daemon.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/dream_daemon.py#L132-L195), [docs/ARCHITECTURE.md](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/docs/ARCHITECTURE.md#L47-L74).
- Basis: Source inspection of session execution, fallback and Dream scheduling.
- Confidence: Medium.
- Caveats: Host scheduling and an operator's manual coordination can still affect contention.

### Absence scope

- Surfaces inspected: Session/turn execution, provider pool and fallback, stored sessions, and Dream's host-idle daemon.
- Plausible first-party paths checked: Shared provider allocation, cross-session cooperation through session storage, and foreground/background coordination.
- Why no material first-party path remains: Session output feeds its own model context, fallback chooses available inference endpoints, and the daemon schedules intelligence work from host idle time. The reviewed paths provide no function-specific exchange or rule between peer S1 units.

## S3 — Inside-and-now control

- State: P
- Function: Control the current installation's default inference allocation across operational sessions.
- Disturbance / variety regulated: Changes in installed models, observed resource pressure, session usage and availability of inference backends.
- Decisive decision or feedback right: Choose and persist the installation's default provider/model pair and apply it to subsequent default operation.
- Decision owner: The authenticated local operator, who can consult the cockpit's installation-level resource and usage view.
- Supporting / enforcement mechanisms: Aggregate session decisions and host resource telemetry, model/provider compatibility checks, authenticated model switch, application-state and user-config writes.
- Closure path: The cockpit returns aggregate usage and host availability to the operator; the operator selects the default pair, which the web route validates, applies to app state and stores for subsequent launch. Existing explicit session overrides remain scoped to their session.
- Boundary reachability: The telemetry and no-session model switch routes are shipped together in the web operating mode. The persist-and-use path is available inside the installed package.
- Whole-system current view: Session, cost and Dream records are aggregated with host CPU, RAM and VRAM for the installation.
- Current-control decision scope: Default inference allocation across the installation. Per-call retry, cooldown and max-iteration enforcement are runtime support.
- Why this is / is not agent-owned: The operator reads the overview and selects the installation default. Provider fallback follows a configured strategy within inference requests.
- Evidence: [uh/web/app.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/web/app.py#L1413-L1439), [uh/telemetry.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/telemetry.py#L529-L570), [uh/web/app.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/web/app.py#L2294-L2365), [docs/ARCHITECTURE.md](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/docs/ARCHITECTURE.md#L93-L99).
- Basis: Shipped web telemetry and installation-default model switch.
- Confidence: Medium.
- Caveats: This supports parent current resource control at installation scope. It does not establish broader control over user task commitments.

## S3* — Complementary audit

- State: —
- Function: Independently check material operational claims made through ordinary session reporting.
- Disturbance / variety regulated: Divergence between reported outcomes and what tools or sessions accomplished.
- Decisive decision or feedback right: Inspect primary operational reality through a complementary channel, form an audit judgment and return it to a current-control owner.
- Decision owner: No first-party witness in the reviewed modes.
- Supporting / enforcement mechanisms: Turn journal, session decisions, read-only Dream inventory, connector probes and repair checks.
- Closure path: The reviewed surfaces close reporting, connector setup or routine repair validation. No separate operational outcome audit loop was established.
- Why this is / is not agent-owned: Dream checks notebook and tooling samples for knowledge defects and feasible workflow ideas. It has no observed mandate to verify session claims from independent execution evidence.
- Evidence: [uh/web/app.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/web/app.py#L760-L791), [uh/web/app.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/web/app.py#L1426-L1439), [uh/dream_pass.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/dream_pass.py#L485-L527), [uh/dream_pass.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/dream_pass.py#L609-L676), [uh/fixes.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/fixes.py#L209-L260).
- Basis: Source inspection of both ordinary reporting and candidate complementary paths.
- Confidence: Medium.
- Caveats: Direct MCP inventory checks validate exposed tooling; the reviewed target is independent audit of session operation.

### Absence scope

- Surfaces inspected: Turn journal, decision and telemetry reporting, Dream sampling and probes, and repair branch checks.
- Plausible first-party paths checked: Reconstructing execution through the journal, Dream cross-checks from source inventories, and a verifier separate from patch composition.
- Why no material first-party path remains: Journaling is generated by the turn itself; Dream reviews knowledge and inventory without adjudicating task outcomes; repair checks gate a patch locally. The shipped paths do not pair an operational claim with a complementary observation and a corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospectively adapt installation capability to environmental change.
- Disturbance / variety regulated: New tooling, changing knowledge sources and possible future workflows.
- Decisive decision or feedback right: Decide which prospective option to adopt and return that decision into current capability.
- Decision owner: Dream generates proposals. No owner-to-capability transition from the prospective proposals was evidenced in the reviewed modes.
- Supporting / enforcement mechanisms: Optional knowledge and MCP inventory, provider-generated ideas, persisted reports and operator plan export.
- Closure path: The supported Dream flow reaches a report or plan file; neither its fulfill route nor its plan writer applies the proposal. The separate fix flow addresses operator-described breakage and has no Dream-selection input.
- Why this is / is not agent-owned: The model contributes prospective ideas and the operator can export them. The installed feedback path ends at delivery of the plan.
- Evidence: [uh/dream_pass.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/dream_pass.py#L286-L373), [uh/dream_pass.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/dream_pass.py#L609-L676), [uh/dream_store.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/dream_store.py#L132-L171), [uh/web/app.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/web/app.py#L1108-L1136), [uh/web/app.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/web/app.py#L1618-L1658).
- Basis: Trace from environment inventory to argument validation, output and operator action.
- Confidence: Medium.
- Caveats: An operator can manually implement an idea outside this workflow; the reviewed boundary is the shipped return path.

### Absence scope

- Surfaces inspected: Dream scheduling and source inventory, review synthesis, plan/optional upload routes and self-repair.
- Plausible first-party paths checked: Autonomous workflow execution from Dream, parent adoption through Fulfill, and handoff from Dream to repair.
- Why no material first-party path remains: The Dream report preserves and validates proposals, Fulfill exports a plan, and repair is a separate present-problem intervention. No shipped selection-to-capability return was found.

## S5 — Policy and identity

- State: P
- Function: Determine the installation's trust boundary for the integrated free-provider mode.
- Disturbance / variety regulated: Failure or unavailability of local inference creates a choice between remaining local and admitting remote inference.
- Decisive decision or feedback right: Permit or prohibit the integrated free router's remote use of session data and persist that deployment policy.
- Decision owner: The installation owner through operator configuration, local-only override and first-use consent.
- Supporting / enforcement mechanisms: Merged config, environment and local-only precedence, persisted consent, router refusal before use.
- Closure path: The owner sets the remote policy and supplies any required consent; subsequent integrated-router calls enforce it. Local-only overrides or denial keep that route closed.
- Boundary reachability: The shipped router invokes the policy code, reads the installation configuration and enforces it at runtime.
- Identity / ultimate-policy issue: Which data may cross the local-first deployment boundary in the integrated-router mode.
- Ultimate authority in each claimed mode: The installation owner controls the configuration, startup flags and consent. The router and session agent operate within that choice.
- Return-to-operation path: Stored config/consent or an explicit local-only override is read on later use and enforces the decision.
- Why this is / is not agent-owned: Provider fallback is bounded by the operator's durable trust policy and cannot grant itself remote authority.
- Evidence: [uh/router/policy.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/router/policy.py#L38-L101), [uh/router/provider.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/router/provider.py#L90-L149), [uh/config.py](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/uh/config.py#L42-L92), [README.md](https://github.com/Antoine-Thomas/UH-Universal-Harness/blob/5b63113bc6096779500bb1c99e624919bcf48fc0/README.md#L39-L56).
- Basis: Shipped policy configuration and pre-call enforcement.
- Confidence: High.
- Caveats: The witness concerns the integrated free router. Explicitly configured remote providers and MCP servers have their own paths.

## Distributed OSS parent arrangement

The assessed parent is the operator of the installation. Repository contribution and release governance is outside that recursion.

## Recursion

The installation coordinates its own system boundary. Repeated sessions instantiate the turn loop and host task-specific contexts. Model and MCP providers remain external dependencies. UHB supplies optional information and classification to Dream.

## Variety and escalation

Turn errors feed the model or stop at the iteration budget. The cockpit reports provider and tool failures and exposes an operator change of default resource. Trust-boundary changes depend on operator consent.

## Evidence gaps

The assessment reconstructs source-wired behaviour at the pinned revision. It has no live provider run or usage measurements from a deployed installation. The S3 result covers default inference resource allocation. The prospective Dream path was inspected through operator plan delivery and the separate repair interface.
