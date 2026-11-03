---
harness_id: nonaut
project_name: Nonaut
repository: https://github.com/nolabs-ai/nonaut
review_ref: 72811854a6e33e3b316ec0013d1534f85e3fd858
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Nonaut

## Review boundary

- System in focus: First-party Rust interactive coding-agent runtime, model provider adapters, history/turn orchestration, tool registry, pinned Nono sandbox policy, filesystem/command operations, TUI and optional independently packaged control-plane audit delivery.
- Purpose and identity: Carry out user coding tasks with model-driven source/command tools while confining tool access to a policy-pinned workspace and preserving human-visible changes and undo.
- Relevant environment: Software repository, files/commands/tests, external model API, compiler/runtime installations, user policy/consent and sandbox denials; external optional audit collection server.
- Standard-distribution boundary: Shipped `nonaut` CLI/TUI, first-party Claude and OpenAI-compatible model loops, Claude Code/Codex provider adapters, common `tools::execute`/tool guards, pinned runtime workspace policy, Nono worker/Seatbelt/Landlock enforcement. Control-plane enrollment/audit shipping is **opt-in** build, not standard runtime independent S3* auditor.
- Credited operating / distribution surfaces: [provider Claude loop](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/providers/claude.rs), [OpenAI-compatible loop](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/providers/openai_compatible.rs), [provider dispatch](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/providers/mod.rs), [tool execution](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/tools/mod.rs), [policy](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/policy.rs), [security model](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/docs/security.md), [opt-in audit](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/crates/nonaut-control-plane/src/audit.rs).
- Adjacent first-party surfaces excluded from ownership: Nono library's intrinsic OS security rights, model vendor/inference server, Codex/Claude Code own runtime cognition when they are used as external adapters, optional unverified remote audit service, nonaut repository development CI, human editor/reviewer decisions.
- First-party operating / deployment modes considered: Local CLI/TUI interactive coding session, first-party provider model-tool loops (Claude API/OpenAI-compatible), optional external provider adapters, file/command sandbox, project security policy consent, undo/detach and opt-in audit delivery.
- Recursion level: One user coding task/session with one model-driven operational agent; model tool calls and OS worker processes are not distinct autonomously managed S1 agents.
- Reviewed revision: `72811854a6e33e3b316ec0013d1534f85e3fd858`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The TUI accepts a user request, supplies history and a first-party tool schema to the configured provider, and relays streamed responses. Claude and OpenAI-compatible adapters each implement repeated model turn→structured tool request→first-party sandbox tool execution→tool result fed back into history until the model ends the turn. Tool calls are constrained by repeat guards, per-command timeouts and a session-pinned Nono worker: the provider connection and secrets remain in trusted Nonaut, while file/search/edit/command tools execute inside a separate OS-constrained worker. Configuration and runtime packs determine limits before the session; failures or sandbox denials are tool feedback, not an autonomous supervisor. The default build has no control-plane enrollment or audit shipping. An opt-in build computes hashed session/event records and queues them for an external service, without an independent auditor deciding correctness. [README](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/README.md), [security](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/docs/security.md), [control_plane.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/control_plane.rs).

## Operational model

One coding model chooses substantive file inspection, edits and commands, observes tool outputs and adjusts choices within current user task. The pinned access boundary can refuse operations and require user reconfiguration on restart; it does not decide which code change is appropriate. TUI diff/undo and detached sessions support a human's control, not a separate first-party governance S3/S5. Optional audit events capture and transport activity but do not supply independent challenge and corrective audit return.

## S1 — Operations

- State: A
- Function: Autonomous task-specific coding and debugging through source/command tool feedback.
- Disturbance / variety regulated: Unknown repository structure, failing commands/tests, missing source evidence, sandbox denials and unanticipated implementation details.
- Decisive decision or feedback right: Select which tool to call, interpret observations, amend files or commands, and determine when a requested coding turn is complete.
- Decision owner: The configured model within first-party Claude/OpenAI-compatible conversation-and-tool loops; external provider supplies model inference but Nonaut owns loop and tool dispatch/return.
- Supporting / enforcement mechanisms: Model tool schema, `ToolLoopGuard`, persistent provider history, streamed response decoding, first-party `tools::execute` and pinned Nono worker.
- Closure path: User task→Nonaut first-party model request→model-chosen structured tool calls→policy-constrained first-party tool result→history/tool response→next model decision or completed turn.
- Boundary reachability: Standard Nonaut TUI connects a provider and runs these adapters; no optional external control-plane build is needed to reach the agent loop.
- Why this is / is not agent-owned: The model chooses substantive code/evidence actions after each result; static sandbox policy and the human editor do not replace the model's local work discretion.
- Evidence: [claude.rs#L183-L355](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/providers/claude.rs#L183-L355), [openai_compatible.rs#L148-L193](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/providers/openai_compatible.rs#L148-L193), [tools/mod.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/tools/mod.rs).
- Basis: explicit + structural
- Confidence: high for first-party model-tool control closure, not for model success or sandbox efficacy on every platform.
- Caveats: Needs a configured model/API and supported OS sandbox; no actual paid model session was run. With Claude Code/Codex adapters the external CLI may own its own model internals, but the first-party Claude/OpenAI-compatible paths independently suffice.

## S2 — Coordination

- State: —
- Function: No distinct coordination among independently operating S1 agents in a standard single-agent coding session.
- Disturbance / variety regulated: Concurrent tool requests, repeated calls and filesystem command timing are intra-agent operations; not an inter-S1 interference phenomenon.
- Decisive decision or feedback right: No distributed peer-unit conflict is routed to a separate S2 coordinator with corrective return into different S1 units.
- Decision owner: Single current agent handles tool decisions; deterministic tool guards/sandbox manage execution hazards.
- Supporting / enforcement mechanisms: Tool-loop repeat guards, Nono worker serialization, abort-on-interrupt, command timeout, TUI session/detach controls.
- Closure path: Tool errors return to the same agent's task loop, without coordinating distinct agents.
- Why this is / is not agent-owned: A batch of tool calls, several provider choices, or multiple separately detached sessions does not establish an actively coordinated S1 peer set at this recursion.
- Evidence: [providers/mod.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/providers/mod.rs), [sessions.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/sessions.rs), [tools/mod.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/tools/mod.rs).
- Basis: structural
- Confidence: high at one active task session.
- Caveats: An outside system may coordinate many Nonaut processes, but that outside controller does not belong to this runtime.

### Absence scope

- Surfaces inspected: Provider loops, tools and repeat guards, CLI/TUI, detached-session process control, worker sandbox and optional control-plane feature.
- Plausible first-party paths checked: Concurrent tool calls, provider switching, multiple detached sessions, runtime packs and event/audit delivery.
- Why no material first-party path remains: No first-party inter-agent collision detection, coordination decision or correction path closes across two distinct S1 units.

## S3 — Inside-and-now control

- State: —
- Function: No separately agent-owned whole-current management of several operational task units or cross-unit resource commitments.
- Disturbance / variety regulated: Model tools may hit policy denials, runtime dependencies or timeouts; these are current single-agent operating constraints.
- Decisive decision or feedback right: Choose cross-task priority, reassign working units and revise current organizational commitments.
- Decision owner: Human user sets workspace permissions/providers and may inspect/undo; deterministic configuration/OS boundary enforces fixed constraints.
- Supporting / enforcement mechanisms: Project policy capture, runtime pack detection, TUI `/permissions`/`/undo`, private capability manifest and immutable session grants.
- Closure path: A denied command → model gets an error or user must restart/reconfigure permissions; no distinct S3 receives whole-system state and returns task-level reallocation.
- Why this is / is not agent-owned: Enforced sandbox rules are security controls, not discretionary whole-current management by an independent agent/parent.
- Evidence: [policy.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/policy.rs), [runtime](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/runtime/mod.rs), [security](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/docs/security.md).
- Basis: structural
- Confidence: high for normal single-session first-party boundary.
- Caveats: Persistent OS users can supervise several sessions externally; they are not a shipped S3 decision actor.

### Absence scope

- Surfaces inspected: Policy/consent/setup, TUI, session lifecycle, tool loop, runtime detection, host sandbox and optional control-plane.
- Plausible first-party paths checked: Session control, runtime environment selection, token/tool budgets, human undo and remote fleet audit reports.
- Why no material first-party path remains: These regulate one agent's safety or record activity but do not choose corrective actions for a multi-S1 whole.

## S3* — Complementary audit

- State: —
- Claim being audited: The coding agent's actions are correct, safe and complete for the user task.
- Ordinary reporting path: Model response, tool output, TUI diff and per-call activity/error events.
- Complementary access path: Optional feature creates a cryptographic event/response ledger with per-session Merkle/hash-chain digests and can ship it to an external control plane; it does not independently inspect actual diffs/task truth and issue actionable audit findings.
- Independence boundary: Audit recorder observes the same first-party tool/event stream; optional external receiver is not established as an independent auditor with source/host cross-check access or a returned decision.
- Who acts on findings: User may inspect tool results, diffs and logs; no shipped independent reviewer return gate requires corrective agent action.
- Function: No independent complementary validation beyond ordinary execution status and recorded telemetry.
- Disturbance / variety regulated: Event tampering/omission risks are mitigated by hashing and snapshots, not independently judged task reality or agent self-report bias.
- Decisive decision or feedback right: Independently challenge model claims against actual evidence, decide false positive/negative and return a correction or halt.
- Decision owner: None established; event hashing/storage is deterministic and optional server interpretation is outside the repository.
- Supporting / enforcement mechanisms: `AuditSession`, event chain/Merkle root, `Client::sync`, TUI change viewer, undo, OS sandbox policy.
- Closure path: Model/tool event → optional hash record and queued upload → outside collector; no verified independent finding/decision feeds back to agent/merge gate.
- Boundary reachability: Default binary omits control-plane audit shipping; opt-in feature records/syncs evidence only, not a first-party audit decision actor.
- Why this is / is not agent-owned: Audit-labeled telemetry and an external upload channel are not automatically complementary S3* audit, regardless of record integrity.
- Evidence: [crates/nonaut-control-plane/src/audit.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/crates/nonaut-control-plane/src/audit.rs), [control_plane.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/control_plane.rs), [README](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/README.md).
- Basis: explicit + structural negative review
- Confidence: high for no first-party audit verdict in inspected paths; outside receiver not evaluated.
- Caveats: Event integrity may help a separate auditor later, but is not proof of an independent audit decision.

### Absence scope

- Surfaces inspected: Default feature gates, optional audit crate session/event chain, optional control-plane sync, TUI diff/undo and policy checking.
- Plausible first-party paths checked: Hash-chained event logs, enrolled audit shipping, sandbox denials, TUI change-review and CI provider test hooks.
- Why no material first-party path remains: None produces an independent reality check with its own verdict/feedback closure into model correction; recording and sending evidence alone is insufficient.

## S4 — Outside-and-then intelligence

- State: —
- Function: No distinct prospective environment intelligence→capability adaptation pathway supplied by agent control architecture.
- Disturbance / variety regulated: Missing tools or runtime packs are detected when preparing the current workspace, not as strategic future-environment signals.
- Decisive decision or feedback right: Anticipate external changes, choose future options and commit new operating capabilities back into current policy/execution.
- Decision owner: Developer/user configures project policies and upgrades software; current agent chooses task-specific coding steps.
- Supporting / enforcement mechanisms: Automatic project runtime detection, language packs, dependency inspection, provider model listing/cache, session startup policy.
- Closure path: Local environment inspection → pinned current sandbox/runtime configuration; no prospective option selection alters organization strategy or future capabilities.
- Why this is / is not agent-owned: Auto-detection and prompt/context compaction are current task support rather than an outside-and-then planning function.
- Evidence: [runtime/mod.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/runtime/mod.rs), [runtime/inspection.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/runtime/inspection.rs), [providers/mod.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/providers/mod.rs).
- Basis: structural
- Confidence: medium-high.
- Caveats: Project coding may improve future software, but current S1's code changes are not separate strategic S4 ownership.

### Absence scope

- Surfaces inspected: Project discovery, runtime packs, provider catalog/cache, session config, model history compaction and optional audit.
- Plausible first-party paths checked: Runtime toolchain detection, project policies, external provider model selection and coding agent improvements.
- Why no material first-party path remains: No bounded environmental foresight→option choice→current-capability revision decision loop at selected recursion.

## S5 — Policy and identity

- State: —
- Function: No legitimate ultimate-policy/identity decision owner and feedback process is implemented within the coding agent.
- Disturbance / variety regulated: Exposure of home credentials, network/fileroot access, malicious tool inputs and risky workspace changes; they are controlled by fixed user-approved capabilities.
- Decisive decision or feedback right: Define/resolve the system's binding mission and update cross-function identity/policy when trade-offs arise.
- Decision owner: Human user chooses workspace permissions and model provider; fixed Nono OS sandbox enforces decisions, and outside optional control plane may revoke device authorization.
- Supporting / enforcement mechanisms: Session-pinned policy, OS kernel Seatbelt/Landlock, provider/tool split, user approval, read-only manifest and access protections.
- Closure path: Human config → immutable worker grants → tool allowed/denied; runtime cannot autonomously revise mission, and adding permissions requires restart.
- Why this is / is not agent-owned: Static access/security policy and an external operator's authority are real controls but not a first-party S5 governance decision loop.
- Evidence: [security.md](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/docs/security.md), [policy.rs](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/policy.rs), [control-plane opt-in](https://github.com/nolabs-ai/nonaut/blob/72811854a6e33e3b316ec0013d1534f85e3fd858/src/control_plane.rs).
- Basis: explicit + structural
- Confidence: high for static policy control, medium-high for absence of parent-policy process.
- Caveats: First-party security enforcement is important independently of any VSM S5 autonomy grade.

### Absence scope

- Surfaces inspected: Policy consent/setup, kernel worker grants, TUI approval/undo, feature-gated control-plane enrollment and docs/security.
- Plausible first-party paths checked: Workspace access policy, sandbox refusal, external audit enrollment, user undo and provider selection.
- Why no material first-party path remains: No identity-level appeal/decision/return path exists beyond static user approval and external service configuration.

## Distributed OSS parent arrangement

The open-source developers, optional control-plane server and local policy-configuring user remain outside this coding session's first-party S3/S4/S5 ownership. An opt-in enrolled device is not itself a distributed OSS policy mandate.

## Self-hosted and non-human modes

The OpenAI-compatible adapter can connect to a locally hosted model while keeping the same first-party model-tool S1 loop and Nono sandbox boundary. Operator permissions stay explicit. No first-party autonomous non-human governance mode is established by model locality.

## Recursion

The operational cell is a single model-driven coding session. Nono worker processes/tool calls and attached/detached terminal instances do not automatically become separately governed viable suborganizations.

## Variety and escalation

Tool schemas, history compaction and read/search/command access amplify coding variety; repeat guards, typed tools, command timeouts and OS sandbox attenuate unsafe variety. Sandbox denials/errors return to the same model or user; an optional event chain improves evidence custody but supplies no independent audit verdict.

## Evidence gaps

Source-pinned review without live model/paid provider/sandbox run. Rust/Cargo unavailable in review environment, so source tests not executed. Kernel boundary effectiveness and optional remote audit service internals are not independently verified; S3* absence is limited to first-party shipped standard/opt-in feature at selected recursion.

## Verdict

**Propose inclusion.** Nonaut implements first-party Claude/OpenAI-compatible model/tool feedback and an OS-constrained coding S1. No separate multi-agent coordination, whole-current management, independent complementary audit, prospective capability intelligence or ultimate-policy decision return is established by its sandbox, telemetry, human TUI and opt-in control-plane feature.
