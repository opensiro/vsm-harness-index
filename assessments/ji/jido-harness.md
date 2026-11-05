---
harness_id: jido-harness
project_name: Jido.Harness
repository: https://github.com/agentjido/jido_harness
review_ref: 20fe00f7e954b8634b5ca73fc8cb7ee55230de24
reviewed_at: 2026-11-05
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

# Jido.Harness

## Review boundary

- System in focus: installable Elixir Jido.Harness application supervision tree plus first-party ACP integration of an explicitly selected coding-agent CLI.
- Purpose and identity: host/observe/cancel bounded autonomous coding-agent runs, turns, and persistent process sessions, with a normalized process and event API.
- Relevant environment: caller applications, checked-out coding workspace, installed external Claude/Codex/Pi/other coding-agent CLI, operating-system subprocesses, ACP protocol and user.
- Standard-distribution boundary: the library and its supervised run/session/ACP adapter modes; external model/CLI supplies the task intelligence when invoked, not autonomous governance owned by the library.
- Credited operating / distribution surfaces: lib/jido_harness/run/manager.ex, run/worker.ex, session/manager.ex, session/worker.ex, adapters/*, session/transports/acp/*, guides/overview.md and guides/ownership_timeouts_and_cancellation.md.
- Adjacent first-party surfaces excluded from ownership: guides/livebooks/* examples, test fixtures and provider-specific external CLI internals, host application's policy/retry/credential/job management.
- First-party operating / deployment modes considered: one-shot blocking run, detached run, continuing ACP session, generic managed process. The process-only mode is not itself an AI-agent S1.
- Recursion level: one installed Jido.Harness-managed agent execution installation; an individually launched provider CLI is an operational cell, not an independent complete VSM organization by default.
- Reviewed revision: 20fe00f7e954b8634b5ca73fc8cb7ee55230de24.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Elixir supervisors/registries retain run, session and managed-process owners independently of the requesting caller. RunManager validates the provider/ACP adapter, starts a supervised RunWorker and waits or returns a stable resource identifier. RunWorker asynchronously invokes an ACP session+turn through the provider subprocess, collects ordered normalized events, handles progress, and records terminal result/error/cancellation. SessionManager and SessionWorker keep a provider process across turns, with queueing, steering, interruption and cleanup. Provider-specific adapters launch external agent CLIs; Arbor ACP owns transport/correlation, not task cognition. Configured runtime/idle/approval timeouts and process-group signals enforce selected limits; retention/journal/replay exposes observed activity but no separate autonomous evaluator. Host app chooses provider, workspaces, policy, retries and durable jobs. There is no built-in cross-run scheduler making strategic choices.

Primary evidence: [overview](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/overview.md), [run worker](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/lib/jido_harness/run/worker.ex), [run manager](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/lib/jido_harness/run/manager.ex), [session manager](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/lib/jido_harness/session/manager.ex).

## Operational model

The agentic operational cell is a selected external coding-agent provider executing an objective and choosing successive model/tool actions while the first-party harness constructs and supervises its ACP lifecycle. Concurrent runs/sessions are different process resources; multiplexing them is not by itself evidence of deliberate S2 mediation. Elixir host code owns lifecycle and deterministic safety enforcement, while the host caller owns provider choice and limits. Neither tool execution nor model-provider outputs automatically establish metasystemic decision ownership.

## S1 — Operations

- State: A
- Function: execute the requested coding/assistant task in a workspace through a provider-backed agent run or turn.
- Disturbance / variety regulated: variable user tasks, workspace observations, external tool responses and the need to choose follow-up actions.
- Decisive decision or feedback right: the invoked ACP coding agent chooses task-specific model/tool actions within the offered session and returns a result.
- Decision owner: external autonomous coding-agent CLI incorporated as a managed operational actor; Jido.Harness does not itself select semantic coding actions.
- Supporting / enforcement mechanisms: RunManager's provider selection/validation, RunWorker/SessionWorker supervised OS process, normalized event delivery, timeout and cancellation.
- Closure path: provider chooses and executes tool actions; observations return over ACP to the provider; its terminal completion/error is normalized and returned to host consumers.
- Boundary reachability: first-party RunManager invokes the ACP adapter and RunWorker invokes the provider with the frozen standard run interface; no example-only or test-only actor is being credited.
- Why this is / is not agent-owned: S1 work choices belong to the running provider agent; process supervisors make lifecycle decisions but not autonomous task choices.
- Evidence: [run manager](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/lib/jido_harness/run/manager.ex), [run worker](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/lib/jido_harness/run/worker.ex), [sessions](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/interactive_sessions.md).
- Basis: structural
- Confidence: high for supported provider-backed mode, not for a bare managed process.
- Caveats: the agent's task decisions reside in installed third-party executables; no live paid coding-agent end-to-end run was performed.

## S2 — Coordination

- State: —
- Function: no shipped inter-S1 interference attenuation with a complete feedback loop established.
- Disturbance / variety regulated: potential concurrent runs or provider sessions, rather than a demonstrated inter-unit collision/dispute.
- Decisive decision or feedback right: absent at this recursion; callers operate separate resources.
- Decision owner: not established; caller may impose coordination outside this library.
- Supporting / enforcement mechanisms: registry, per-session turn queue and supervision serialize local process lifecycle, not a specific conflict among distinct S1 operational cells.
- Closure path: no cross-S1 coordination decision is returned to alter competing operational cells.
- Why this is / is not agent-owned: transport/queue and isolation are not a negotiated multi-unit S2 function.
- Evidence: [overview](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/overview.md), [session manager](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/lib/jido_harness/session/manager.ex).
- Basis: structural
- Confidence: medium-high
- Caveats: downstream hosts can build coordination from these primitives; that separate system is out of scope.

### Absence scope

- Surfaces inspected: run/session managers and workers, process management, guides/overview.md, operation/ownership docs, provider adapters and package boundary.
- Plausible first-party paths checked: concurrent run registries, session turn queue, supervisor cancellation, normalized events and scheduling/selection of adapters.
- Why no material first-party path remains: no evidence of a concrete inter-agent conflict plus a first-party coordinating decision fed back to both cells; queueing turns for one session alone is not cross-S1 regulation.

## S3 — Inside-and-now control

- State: —
- Function: no shipped whole-installation resource/priorities bargain or active current-operation regulatory choice.
- Disturbance / variety regulated: per-run execution duration, idle time and cancellation; caller-selected bounds rather than a whole-system commitment tradeoff.
- Decisive decision or feedback right: host caller selects resource/task/policy parameters; the harness enforces them and exposes cancel/interrupt.
- Decision owner: external host/operator for the chosen bounds; no first-party current-control decision owner with a whole-system view.
- Supporting / enforcement mechanisms: timeout timers, supervised task cancellation, OS process-group kill and returned status.
- Closure path: a fixed limit can stop a run, but no S3-specific whole-system discretion is evidenced.
- Why this is / is not agent-owned: deterministic enforcement does not take ownership from the host.
- Evidence: [ownership/timeouts](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/ownership_timeouts_and_cancellation.md), [run worker](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/lib/jido_harness/run/worker.ex).
- Basis: structural
- Confidence: medium-high
- Caveats: supervision can enforce locally selected policies but does not prove a whole-system regulator.

### Absence scope

- Surfaces inspected: run/session/managed-process lifecycle code, timeout/config guides, host boundary in overview.
- Plausible first-party paths checked: global registry listings, runtime/idle/approval budgets, cancel/kill APIs, host retry and configured limits.
- Why no material first-party path remains: these paths manage or enforce individual resource contracts; current priority/resource authority across all S1 units remains with an embedding host not supplied here.

## S3* — Complementary audit

- State: —
- Function: no separate audit judgment challenging routine agent claims.
- Disturbance / variety regulated: unreliable agent reports could be checked against raw recorded events, but such challenge/feedback is not built in.
- Decisive decision or feedback right: none evidenced; log replay is an observation API.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ACP event normalization, bounded journals, replay and telemetry.
- Closure path: recordings return to callers but are not compared and adjudicated by an independent auditor with a returned control action.
- Why this is / is not agent-owned: recorder and operational provider do not form an independent audit owner.
- Evidence: [overview](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/overview.md), [event journal](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/lib/jido_harness/journal.ex).
- Basis: structural
- Confidence: medium-high
- Caveats: applications may attach independent auditing, outside the declared distribution.

### Absence scope

- Surfaces inspected: event/journal, run/session results, ACP path, operations and replay guides.
- Plausible first-party paths checked: independently observed raw activity, provider event vs status reconciliation, external checkers and audit-to-control callback.
- Why no material first-party path remains: the first-party path exposes records but contains neither complementary audit judgment nor closure into subsequent management.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective external-environment modeling and adaptation path to current system capability.
- Disturbance / variety regulated: varying provider capability is detected as request errors/capabilities, not studied as future options.
- Decisive decision or feedback right: absent; host selects provider and upgrades.
- Decision owner: external host/maintainer; no first-party S4 choice owner.
- Supporting / enforcement mechanisms: provider capability profiles, adapter configuration and diagnostics.
- Closure path: present compatibility settings do not produce future-oriented adaptation decisions returned to current operations.
- Why this is / is not agent-owned: provider switching/normalization is a current integration mechanism, not prospective intelligence.
- Evidence: [provider guide](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/providers.md), [overview](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/overview.md).
- Basis: structural
- Confidence: high
- Caveats: host software could add its own adaptive decisions.

### Absence scope

- Surfaces inspected: provider adapters, capability and config guides, release/operation overview, run/session implementations.
- Plausible first-party paths checked: provider updates, capability discovery, future environment investigation and reconfiguration authority.
- Why no material first-party path remains: shipped system normalizes currently available providers; it does not form and return future-facing options for changing its operational repertoire.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision with legitimate authority and return.
- Disturbance / variety regulated: request-level approvals or process limits, not the organization's identity or highest-level policy.
- Decisive decision or feedback right: no first-party ultimate-policy path; host owns policies.
- Decision owner: external application/operator for execution policy, not an S5 loop supplied by Jido.Harness.
- Supporting / enforcement mechanisms: approval request/timeout flow, secure adapter execution, config defaults.
- Closure path: permissions can be denied for an individual action but no identity-policy issue → legitimate authority → returned policy governance loop is shipped.
- Why this is / is not agent-owned: user approval and hard runtime boundaries are not themselves S5.
- Evidence: [security](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/security.md), [ownership/timeouts](https://github.com/agentjido/jido_harness/blob/20fe00f7e954b8634b5ca73fc8cb7ee55230de24/guides/ownership_timeouts_and_cancellation.md).
- Basis: structural
- Confidence: high
- Caveats: no conclusion about organizational governance of an embedding host.

### Absence scope

- Surfaces inspected: security/approval docs, config and lifecycle code, public host/application contract.
- Plausible first-party paths checked: approval callbacks, caller/administrator configuration, policy escalation and returned persistent ultimate-policy revision.
- Why no material first-party path remains: approvals and caller configuration regulate operations; there is no first-party pathway to adjudicate and reapply identity-level authority.

## Recursion

External provider coding agents can be complex autonomous organizations themselves, but Jido.Harness only launches/hosts them under a unified resource lifecycle. It does not establish a complete nested recursion with local S2–S5 for each child.

## Variety and escalation

ACP normalizes diverse provider events, typed requests and turn results; per-resource timeouts attenuate execution duration and memory/disk retention. Failure, timeout, cancel and unsupported capability produce explicit lifecycle/error feedback to the host. This is bounded runtime exception handling, not by itself an algedonic channel or metasystemic governance.

## Evidence gaps

- Source/released-interface inspection only; no paid external coding-agent or BEAM runtime integration executed in this review.
- Provider implementations and host application policy were explicitly excluded from first-party S2–S5 ownership.
- Results apply to the exact frozen revision and standard documented modes, not hypothetical embeddings.
