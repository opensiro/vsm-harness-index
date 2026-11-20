---
harness_id: codercraft
project_name: CoderCraft
repository: https://github.com/sandraschi/codercraft
review_ref: 37a3b81ab052213c93a974f68e2264c28dc3b134
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: —
---

# CoderCraft

## Review boundary

- System in focus: One CoderCraft installation, including its native desktop and the first-party CLI/MCP goal loop.
- Purpose and identity: Let a user or client inspect and change a local code workspace with a model-backed coding run.
- Relevant environment: Local workspace and IDE operator, configured AI provider, optional MCP integrations, and other applications visible in the depot.
- Standard-distribution boundary: Shipped workspace, model, goal, MCP dispatch, local session records and GUI configuration surfaces.
- Credited operating / distribution surfaces: [Dispatch](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/lib.rs) · [Goal loop](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/autonomy.rs) · [Desktop](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-app/src/main.rs) · [CLI and MCP](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-mcp/src/main.rs)
- Adjacent first-party surfaces excluded from ownership: Storytold and other fleet applications, provider internals, general-purpose external MCP clients and contributor machinery.
- First-party operating / deployment modes considered: CLI/MCP goal execution in plan or build mode and owner-operated desktop model configuration.
- Recursion level: Installation containing individual run sessions.
- Reviewed revision: 37a3b81ab052213c93a974f68e2264c28dc3b134
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The core workspace provides dispatch, coding-loop permissions, patch handling and durable session history. Both CLI and MCP reach AgentRun. The loop calls a configured Craft AI model, logs bounded step results and supplies them back to the model. The desktop also shows an in-memory swarm simulation and a depot of other apps; neither surface dispatches the displayed simulated workers as real peer agents.

## Operational model

The operational agent is a run-scoped configured model that selects workspace actions and interprets the results. The optional deterministic fallback remains a separate non-agent path. The operator or client authorizes the selected invocation and the desktop operator can choose persistent model configuration.

## S1 — Operations

- State: A
- Function: Perform goal-directed workspace exploration or change through a bounded model/tool loop.
- Disturbance / variety regulated: Workspaces differ, actions fail and test results can require a different next step.
- Decisive decision or feedback right: Choose the next permitted workspace action or conclude the goal after receiving step evidence.
- Decision owner: Configured session model in the live brain path.
- Supporting / enforcement mechanisms: Mode-specific tool allowlist, fixed budgets, permission decisions, deterministic fallback, persisted step receipts.
- Closure path: Results and check output enter the loop history, which is assembled into the next model request.
- Why this is / is not agent-owned: The model selects and revises operation. The deterministic mode can explore in its absence but does not exercise the same discretionary choices.
- Boundary reachability: CLI and MCP dispatch AgentRun to autonomy::run_goal with a configured model; both plan and build are first-party run modes.
- Evidence: [Goal loop](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/autonomy.rs) · [Core binding](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/lib.rs) · [CLI/MCP binding](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-mcp/src/main.rs)
- Basis: structural
- Confidence: high
- Caveats: The review did not run a provider or claim that all advertised GUI actions enter the same goal loop.

## S2 — Coordination

- State: —
- Function: Regulate interference among actual peer operational units.
- Disturbance / variety regulated: Concurrent workspace actors could interfere. The advertised node graph suggests candidate peer roles.
- Decisive decision or feedback right: No shipped peer conflict decision or return path was established.
- Decision owner: Goal sessions act per run; the graph's worker entries are simulation records.
- Supporting / enforcement mechanisms: In-memory ledger, scheduled visual state advancement, task-role labels and per-run permission checks.
- Closure path: Simulation updates the rendered node graph; individual run results return to their own loop.
- Why this is / is not agent-owned: The graph advances synthetic records. It does not supply independent S1 actors or mutual adjustment between live sessions.
- Evidence: [Simulation and workers](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-agent/src/lib.rs) · [Graph renderer](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-app/src/main.rs) · [Operational loop](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/autonomy.rs)
- Basis: structural
- Confidence: medium
- Caveats: External IDE workflows or callers might coordinate work outside the assessed installation.

### Absence scope

- Surfaces inspected: Goal-run code, swarm ledger/runtime links, GUI graph and MCP status dispatch.
- Plausible first-party paths checked: Specialist worker execution, workspace ownership conflicts and agent adjustments across sessions.
- Why no material first-party path remains: Graph steps are synthetic, with no live sibling execution or coordination feedback into the goal loop.

## S3 — Inside-and-now control

- State: —
- Function: Regulate the current operations of the installation as a whole.
- Disturbance / variety regulated: Running tasks could compete over resources or require changing a commitment.
- Decisive decision or feedback right: No shipped whole-installation work view coupled to discretionary current intervention was identified.
- Decision owner: User and model make per-run choices. The runtime applies mode and step limits.
- Supporting / enforcement mechanisms: CLI/MCP arguments, per-run permission rules, persistent session histories, depot probes and synthetic swarm graph.
- Closure path: Scoped controls affect the invoked run. Archived evidence is available for recall.
- Why this is / is not agent-owned: Neither one goal loop nor a health projection supplies control over a live portfolio of real owned operations.
- Evidence: [Per-run orchestration](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/autonomy.rs) · [Session records](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/sessions.rs) · [Desktop and fleet surfaces](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-app/src/main.rs)
- Basis: structural
- Confidence: medium
- Caveats: Operators can direct individual work externally but that does not add a supplied whole system closure.

### Absence scope

- Surfaces inspected: First-party run entry points, session storage, desktop swarm and depot, and model settings.
- Plausible first-party paths checked: Whole work inventory, runtime intervention across live goals, and a discretionary supervisor or owner portfolio mode.
- Why no material first-party path remains: The live run exposes task-local controls. Depot reachability and simulated roles do not establish a current work governance surface.

## S3* — Complementary audit

- State: —
- Function: Challenge a substantive operational claim through complementary access and return findings into corrective work.
- Disturbance / variety regulated: A change or model summary can be incorrect.
- Decisive decision or feedback right: No separate audit actor or function-specific independent corrective construction was established.
- Decision owner: The same goal loop owns its own work and uses the output of standard tests.
- Supporting / enforcement mechanisms: Inline patch verification, linter dispatch and persisted session steps.
- Closure path: After-patch output is appended to the same run's ordinary history.
- Why this is / is not agent-owned: The same run initiates ordinary post-patch verification and interprets its output. The rendered specialist roles supply no additional audit access.
- Evidence: [Inline test feedback](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/autonomy.rs) · [Dispatch checks](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/lib.rs) · [Simulated specialist roles](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-agent/src/lib.rs)
- Basis: structural
- Confidence: medium
- Caveats: Recorded tests can provide reliable task feedback without closing an independent audit loop.

### Absence scope

- Surfaces inspected: Goal verification, check dispatch, session recall and the graph's test/lint roles.
- Plausible first-party paths checked: Independent access to work or checks beyond the ordinary action/verification stream, including separate reviewer feedback.
- Why no material first-party path remains: The enabled test path is inline during goal execution and there is no independent audit sampling or reviewer return path in the shipped specialist simulation.

## S4 — Outside-and-then intelligence

- State: P
- Function: Select the model capability used for future runs after observing available provider models.
- Disturbance / variety regulated: A provider can make a different model available or no longer offer the configured choice.
- Decisive decision or feedback right: Select and persist a model based on the provider's observed options.
- Decision owner: Desktop operator in the reviewed human-operated path.
- Supporting / enforcement mechanisms: Live provider listing, editable model selection, persisted config, optional model warming.
- Closure path: Chosen provider/model is written to config and influences following model requests.
- Why this is / is not agent-owned: A caller can select through APIs, with no shipped autonomous model-selection or adoption loop evidenced. The GUI lets the operator choose from observed options.
- Boundary reachability: Desktop model settings invoke provider model listing and let the operator copy a returned model into the saved runtime choice used by the model path.
- External distinction: Models returned by the configured provider's live listing rather than options invented by the UI.
- Future / prospective distinction: A saved choice changes the brain used by later goals.
- Adaptation option generated: The operator evaluates an available model and selects a provider/model combination.
- Path back into current capability / S3: Persisted configuration is consumed by subsequent model-backed operation, with optional immediate resource warming.
- Evidence: [Desktop observation and selection](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-app/src/main.rs) · [List and persist dispatch](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/lib.rs) · [Goal model binding](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/autonomy.rs)
- Basis: structural
- Confidence: medium
- Caveats: Limited to provider capability selection. The reviewed list can include provider-specific curated or unavailable entries; the claim is the supported live observation route.

## S5 — Policy and identity

- State: —
- Function: Decide the installation's ultimate policy and identity.
- Disturbance / variety regulated: Mode choice and tool permissions constrain operational risk.
- Decisive decision or feedback right: No supplied ultimate-policy decision loop was established.
- Decision owner: Repository code defines permission predicates; operators choose run modes or model settings.
- Supporting / enforcement mechanisms: Tool policy checks and plan/build partitions.
- Closure path: Ordinary gate enforcement changes permitted actions for a run.
- Why this is / is not agent-owned: The reviewed paths express established operating rules and tactical configuration.
- Evidence: [Permission rules](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/permissions.rs) · [Mode checks](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/autonomy.rs) · [Configuration commands](https://github.com/sandraschi/codercraft/blob/37a3b81ab052213c93a974f68e2264c28dc3b134/crates/codercraft-core/src/lib.rs)
- Basis: structural
- Confidence: medium
- Caveats: MCP server configuration and mode selection do not by themselves demonstrate an installed authority mechanism for revising ultimate policy.

### Absence scope

- Surfaces inspected: Plan/build modes, permission implementation, desktop and MCP configuration, and extension registration.
- Plausible first-party paths checked: Owner response to a boundary or mission change, autonomous rules revision, and application of such a decision to future policy.
- Why no material first-party path remains: The traced modes change permissions for particular tasks or configure tools/provider. The installation supplies no distinct authority-to-policy revision and return loop.

## Recursion

The model's operational decisions are scoped to a goal session. Fleet depot services and third-party callers are environmental; the projected swarm is a demonstration independent of the operational loop.

## Variety and escalation

Denied actions and verification results return to sessions. Provider availability enters operator configuration; existing permission rules constrain mutation.

## Evidence gaps

Static assessment of the reviewed commit. No native desktop, installed model backend or optional integration run was exercised. No performance claims from the README were relied upon.
