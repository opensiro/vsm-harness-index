---
harness_id: oar
project_name: OAR
repository: https://github.com/botiverse/oar
review_ref: a58672d52acb25f286c67831e114c1738588064c
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OAR

## Review boundary

- System in focus: Published Open Agent Runtime Node library and CLI, including the standard embedded Pi coding session and optional downstream runtime and subagent adapters.
- Purpose and identity: Open and control coding-agent sessions across provider runtimes while preserving native observations and recoverable session identity.
- Relevant environment: User workspace, agent model provider, host application, external agent binaries and SDKs, and optional application-supplied tools.
- Standard-distribution boundary: OAR packages, bundled Pi coding SDK path and its native model/tool session binding, OAR session lifecycle, event projection, runtime registry and published subagent tools.
- Credited operating / distribution surfaces: Default Pi runtime registration, SDK session creation and prompt loop, OAR CLI `run` and `mcp`, and native runtime observation and control.
- Adjacent first-party surfaces excluded from ownership: OAR repository development and release automation, scripted providers and vendor-test infrastructure, Arena and Pi Durable demo applications. Host-owned durable storage, configuration and child scheduling are not ownership belonging to OAR.
- First-party operating / deployment modes considered: Standard Node and CLI Pi SDK, external process adapters, optional Pi Durable constructor with a host-supplied Harness, and host-invoked cross-runtime subagents.
- Recursion level: OAR installation and its reachable coding-agent sessions. A downstream team or host application is a separate organizational boundary.
- Reviewed revision: `a58672d52acb25f286c67831e114c1738588064c`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

OAR provides a common runtime registry plus session open, prompt, steer, queue, withdrawal and abort calls and an attributed native record stream. The default Pi route creates an in-process coding SDK `AgentSession` behind the standard API with native model selection, coding tools and session history. Other adapters may spawn or attach to separately installed processes. The optional Pi Durable route observes a supplied Harness and that Harness retains its scheduler, storage and tool environment. The built-in subagents library can start and manage delegated native sessions, but documented policy and scheduling remain the host's choices.

## Operational model

One S1 unit is a model-backed coding session with actual tool and worktree access in the standard Pi SDK mode. Invoked child sessions can be other operational units. OAR translates their controls and reports. A runtime registry, filter, record observer or session controller has no independent project-level decision authority by itself.

## S1 — Operations

- State: A
- Function: Run a coding agent over an actual workspace task and return its tool and task results.
- Disturbance / variety regulated: Task prompts, inspected workspace state, tool results, diagnosis and coding iteration.
- Decisive decision or feedback right: Choose subsequent tool calls or a terminal answer from workspace and prior tool evidence.
- Decision owner: The live model directing the native agent loop.
- Supporting / enforcement mechanisms: OAR runtime selection, session construction and projection, Pi SDK coding tools, model registry and native session manager.
- Closure path: Model tool calls operate on the workspace and return observations to the same running session. OAR reports the native turn outcome and persists the native session identity for continuation.
- Boundary reachability: The standard registry exposes the bundled in-process Pi route. OAR directly creates the native session with available coding tools and calls its prompt with normal model credentials.
- Why this is / is not agent-owned: The client supplies task and model settings, while the instantiated agent chooses and executes subsequent actions. OAR does not prescribe an action sequence.
- Evidence: [registry](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/packages/oar/src/index.ts#L43-L73), [embedded session creation](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/packages/oar/src/runtimes/pi/open.ts#L144-L217), [session prompt](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/packages/oar/src/runtimes/pi/session.ts), [native contract and default placement](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/runtimes/pi.md).
- Basis: structural
- Confidence: High
- Caveats: A standard first-party binding is credited, not native internals of arbitrary vendor agents or the developer's archived scripted checks.

## S2 — Coordination

- State: —
- Function: Attenuate interference between independently working sessions.
- Disturbance / variety regulated: Child sessions can contend for workspace state, process capacity or execution order.
- Decisive decision or feedback right: No installed cross-session conflict-specific decision and return path was identified.
- Decision owner: Downstream host or calling agent supplies scheduling and workspace policy.
- Supporting / enforcement mechanisms: Attested session identity, per-session busy handling, max-running and depth limits, wait and report delivery.
- Closure path: A caller can act on a refusal or report. The package applies existing limits and operation requests without resolving which distinct unit changes its work in a material conflict.
- Why this is / is not agent-owned: A concurrency cap and mailbox do not assign discretionary mutual adjustment.
- Evidence: [crew controls](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/packages/oar/src/agents/crew.ts), [host limit policy](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/spec/subagents.md#L135-L171), [ownership](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/design/system.md#L125-L132).
- Basis: structural
- Confidence: High
- Caveats: An application using OAR can supply a conflict-specific control relation of its own.

### Absence scope

- Surfaces inspected: Crew, per-session queue and native busy controls, MCP task controls, host/system contract.
- Plausible first-party paths checked: Concurrent child launch refusal, report-triggered steering, shared native process and queued work.
- Why no material first-party path remains: These paths enforce limits, route commands or report readiness. Host integration supplies conflict judgment and return.

## S3 — Inside-and-now control

- State: —
- Function: Allocate or intervene across OAR operational commitments using a whole-system current view.
- Disturbance / variety regulated: A family of active sessions may compete for resources, need reprioritization or fail.
- Decisive decision or feedback right: The library does not own a discretionary allocation or intervention decision across sessions.
- Decision owner: Host/caller owns resource policy and determines which controls to issue. No separate first-party parent-governed whole-system path was established inside the OAR boundary.
- Supporting / enforcement mechanisms: Orientation, account usage, child task map and configurable local caps, typed steer and interrupt responses.
- Closure path: Supplied commands can change native runs. The package provides no aggregate current-control actor that turns the view into a distribution-level commitment decision.
- Why this is / is not agent-owned: A current-state observation and effective runtime stop are supporting mechanisms owned by their caller.
- Evidence: [host/control contract](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/design/system.md#L53-L78), [ownership](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/design/system.md#L125-L132), [MCP tools](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/packages/cli/src/mcp-tools.ts).
- Basis: structural
- Confidence: High
- Caveats: Application effects from a caller choosing to intervene do not evidence a supported supervisory mode for one governed OAR organization.

### Absence scope

- Surfaces inspected: Runtime orientation and usage, subagent list, interrupt, close and command routes, typed outcome semantics and host ownership.
- Plausible first-party paths checked: Host-directed child capacity rules, operator intervention on a session, cross-runtime model and capacity selection.
- Why no material first-party path remains: The host supplies operational priorities and arbitration. Session commands enforce local choices without a bundled whole-system feedback owner.

## S3* — Complementary audit

- State: —
- Function: Audit operational claims through sufficiently independent access and return corrective findings.
- Disturbance / variety regulated: A projected result or child report could hide a fault in actual workspace behavior.
- Decisive decision or feedback right: No packaged reviewer or audit-specific construction yielding an independent operational verdict was identified.
- Decision owner: Record consumer or downstream host can implement a reviewer. OAR owns the observation format.
- Supporting / enforcement mechanisms: Native event retention, attributed session streams, projected task results, optional log files and replay.
- Closure path: Records can be consumed by others, but they yield no complementary audit result or automatic corrective response in the package.
- Why this is / is not agent-owned: Direct evidence visibility preserves evidence but does not make an independent audit judgment.
- Evidence: [record stream](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/spec/record-stream.md), [subagent reports](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/spec/subagents.md#L37-L93), [child report construction](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/packages/oar/src/agents/subagent.ts).
- Basis: structural
- Confidence: High
- Caveats: Primary operational records enable a downstream audit without supplying that function by themselves.

### Absence scope

- Surfaces inspected: Raw and projected records, subagent reports and log transport, verification and replay contracts.
- Plausible first-party paths checked: Second-runtime review via generic delegation, direct native observations, task and completion verification.
- Why no material first-party path remains: Generic tools expose sources and lifecycle evidence. They provide no audit-specific independent judgment and corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: Translate external and prospective changes into new sustained operational capability.
- Disturbance / variety regulated: Vendor model support, installations, quotas and runtime environments change.
- Decisive decision or feedback right: No shipped actor selects and adopts a prospective capability adaptation based on external evidence.
- Decision owner: Host and operators choose provider, model, update and deployment policy. Vendor and OAR developers change packages outside the assessed loop.
- Supporting / enforcement mechanisms: Installation, orientation, model inventory, version checks, explicit update controls and adapter compatibility validation.
- Closure path: An explicit requested update may change an installation. A reading or update primitive does not produce and select a future adaptation option.
- Why this is / is not agent-owned: Runtime records and current availability inform a consumer whose adaptation logic OAR does not provide.
- Evidence: [orientation](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/spec/orientation.md), [updates](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/spec/update.md), [system roadmap context](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/design/system.md#L102-L132).
- Basis: structural
- Confidence: High
- Caveats: Adapter maintenance, upstream roadmap and developer CI are outside deployed OAR operation.

### Absence scope

- Surfaces inspected: Model and runtime inventories, orientation, session resume, update mechanism, native subagent control.
- Plausible first-party paths checked: Detecting vendor availability changes, choosing a new runtime, updating an installation, and returning new operational assumptions.
- Why no material first-party path remains: Explicit commands and read surfaces do not develop or choose a prospective change or lifecycle feedback. The host owns such choices.

## S5 — Policy and identity

- State: —
- Function: Resolve an identity or ultimate-policy matter and bind the authoritative result into operation.
- Disturbance / variety regulated: Host/runtime choices may impose different provider, tool, configuration and deployment constraints.
- Decisive decision or feedback right: No shipped identity/policy question-to-authority-to-governing-operation path was established.
- Decision owner: Host and vendor own configuration and policy at their respective boundaries. OAR validates passed options.
- Supporting / enforcement mechanisms: Capability declarations, refused options, native permission requests and per-session configured instructions.
- Closure path: Chosen settings are passed into a session or refused. No returned ultimate-policy decision is produced in a first-party operating mode.
- Why this is / is not agent-owned: Policy enforcement and provider options embody choices supplied by another actor.
- Evidence: [host ownership](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/design/system.md#L125-L132), [capabilities](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/docs/design/capabilities.md), [embedded configuration](https://github.com/botiverse/oar/blob/a58672d52acb25f286c67831e114c1738588064c/packages/oar/src/runtimes/pi/open.ts#L144-L207).
- Basis: structural
- Confidence: High
- Caveats: Task-specific approvals and persisted instructions do not establish organization-wide policy adjudication.

### Absence scope

- Surfaces inspected: Session instruction, tool and permission options, native host policy boundary, capability declarations and CLI configuration.
- Plausible first-party paths checked: Cross-runtime permission handling, authoritative changes to durable instructions and runtime governance.
- Why no material first-party path remains: These surfaces transport specified inputs and enforce adapter contracts. They do not supply an ultimate-policy escalation and binding return.

## Recursion

Child sessions may exercise scoped operational autonomy. Their launch, supervision and coordination are delegated to the host or caller. Native child-session attribution is neither proof of a metasystem nor proof that every vendor agent has the same governance.

## Variety and escalation

Runtime-specific differences are surfaced as declared capabilities, typed refusal, native observations, and session-identifiable errors. The calling host decides how to respond to these signals.

## Evidence gaps

Source-only review at the frozen revision. No live provider execution, separate semantic review or independent Index audit was claimed. Arbitrary vendor agent, host and optional extension behavior is outside this finding.
