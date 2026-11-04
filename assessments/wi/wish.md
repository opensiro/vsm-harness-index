---
harness_id: wish
project_name: Wish
repository: https://github.com/WindustH/wish-core
review_ref: 28e6a07b2ac36684a3280c6ecf9b963c28bca831
reviewed_at: 2026-11-04
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

# Wish

## Review boundary

- System in focus: The wish-core Rust agent server, durable session engine and first-party tools/peer bridge.
- Purpose and identity: Execute self-hosted user tasks through persistent model/tool sessions exposed over HTTP and a CLI bridge.
- Relevant environment: User workspaces and questions, model providers, shell/background tasks, session peers, MCP/services, SQLite state and interruptions.
- Standard-distribution boundary: The wish binary with application/session/executor/storage/protocol/tool machinery, direct or command-delivered capabilities and optional group/peer sessions. wish-web and the separate wish-test suite are adjacent repositories; provider services and external MCP processes are dependencies.
- Credited operating / distribution surfaces: [README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/README.md); [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [src/session/machine.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/session/machine.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [docs/internals/skills.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/skills.md); [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md).
- Adjacent first-party surfaces excluded from ownership: Web client, wish-test black-box suite, GitHub CI/release and architecture/input-preemption development-audit documents. Their reviewers and test harnesses are not runtime audit actors of a deployed Wish server.
- First-party operating / deployment modes considered: Self-hosted HTTP server, ordinary single-session execution, serial/parallel tool batches, interrupted/resumed sessions, background shell results, session create/manage/send and group chat, skills/MCP discovery, ask_user and operator config/model switching.
- Recursion level: One task-executing harness; multiple calls, processes or sessions do not establish recursive viability.
- Reviewed revision: `28e6a07b2ac36684a3280c6ecf9b963c28bca831`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Application services instantiate persistent sessions and schedule one executor per session. The state machine consumes queued inputs, builds model requests, records model responses and selects pending tool batches. executor/run.rs calls models, accepts responses, executes tools and records outcomes before another turn. The model chooses task actions; the deterministic session machine preserves effect ordering, stable cutovers and suspension/recovery. SQLite records history and queues; observers receive committed events and live stream fragments. Shell/background tasks and user questions return results into session input. Peers can create/configure their own child sessions and send messages through groups. Groups store chat transcripts and wake every other member; they do not run a controller or constrain mutual replies. Skills/MCP are discoverable capabilities, not additional organizational actors.

Primary implementation: [README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/README.md); [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [src/session/machine.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/session/machine.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [docs/internals/skills.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/skills.md); [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md).

## Operational model

Each running task session is a potential S1 unit coupled to a workspace and user task. Its model selects actions, observes tool outcomes and finishes or continues. Multiple sessions, ownership-based management permissions and group messages make plurality possible, but do not themselves prove a coordination or current-management organization. The server enforces selected capabilities and lifecycle constraints without becoming the owner of higher organizational discretion.

## S1 — Operations

- State: A
- Function: Produce task outcomes through durable model-selected tool execution.
- Disturbance / variety regulated: Workspace state, model output, tool/process results, user answers and interruptions.
- Decisive decision or feedback right: Choose tools and subsequent actions or finish after receiving observations.
- Decision owner: The active model-backed actor of each session.
- Supporting / enforcement mechanisms: Session state machine, executor, model protocol adapters, tool dispatch, SQLite history/queue, process supervision and stable configuration cutovers.
- Closure path: Model response tool calls become pending effects; completed tool outcomes enter session history/request context and the executor calls the model again until completion or suspension.
- Boundary reachability: The installed wish server schedules SessionSlot.execute and executor.run_with_boundary for HTTP input; direct and CLI-bridge capabilities return through the same first-party application/session path.
- Why this is / is not agent-owned: Without the model actor the deterministic state machine can persist and dispatch specified effects but does not decide task-specific work.
- Evidence: [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [src/session/machine.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/session/machine.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

## S2 — Coordination

- State: —
- Function: No S2-specific stabilization relation established.
- Disturbance / variety regulated: Potential interference among peer sessions, shared workspaces and group reply cascades.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Group transcript/queues, session mutex, schedule epoch and peer bridge.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Groups explicitly wake all other members without counting or limiting exchanges. Messaging and ownership checks lack a concrete conflict/oscillation attenuation decision with returned mutual S1 adjustment. Per-session locking prevents duplicate executors of one unit, not interference among distinct S1s.
- Evidence: [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [src/application/groups.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/groups.rs); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/README.md); [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [src/session/machine.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/session/machine.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [docs/internals/skills.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/skills.md); [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md).
- Plausible first-party paths checked: Group post/wakeup semantics, peer create/send/manage permissions, per-session mutex/epoch and serial/parallel tool batch mode.
- Why no material first-party path remains: Groups explicitly wake all other members without counting or limiting exchanges. Messaging and ownership checks lack a concrete conflict/oscillation attenuation decision with returned mutual S1 adjustment. Per-session locking prevents duplicate executors of one unit, not interference among distinct S1s.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system inside-and-now control organization established.
- Disturbance / variety regulated: Current session commitments, provider limits and server resources.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Session status, ownership permissions, runtime permits, interrupts and selection boundary.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: A generic session status/control API and creator permissions do not instantiate a whole-system controller owning shared priorities/resources/accountability. Fixed permits and lifecycle transitions enforce constraints; no S3-specific autonomous constructor or returned parent judgment is supplied.
- Evidence: [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [docs/internals/executor.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/executor.md); [docs/internals/README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/README.md); [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [src/session/machine.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/session/machine.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [docs/internals/skills.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/skills.md); [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md).
- Plausible first-party paths checked: Peer list/show current status, management of created sessions, operator interrupt/resume, provider switching, blocking-work permits and shutdown.
- Why no material first-party path remains: A generic session status/control API and creator permissions do not instantiate a whole-system controller owning shared priorities/resources/accountability. Fixed permits and lifecycle transitions enforce constraints; no S3-specific autonomous constructor or returned parent judgment is supplied.

## S3* — Complementary audit

- State: —
- Function: No runtime complementary independent audit established.
- Disturbance / variety regulated: False task claims, uncertain side effects or incorrect persisted reports.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Committed events, transcripts, application traces and adjacent build/integration checks.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: History and process observations support ordinary operations. Named audit documents and wish-test are development validation, not a deployed independent operational actor with complementary access and corrective authority. No audit-specific constructor is wired into session execution.
- Evidence: [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [docs/internals/history.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/history.md); [docs/internals/architecture-audit-followup.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/architecture-audit-followup.md); [docs/internals/input-preemption-audit.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/input-preemption-audit.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/README.md); [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [src/session/machine.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/session/machine.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [docs/internals/skills.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/skills.md); [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md).
- Plausible first-party paths checked: Model/tool history, observer delivery, history search, unknown-outcome recovery, and architecture/input-preemption audit documentation.
- Why no material first-party path remains: History and process observations support ordinary operations. Named audit documents and wish-test are development validation, not a deployed independent operational actor with complementary access and corrective authority. No audit-specific constructor is wired into session execution.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective capability adaptation organization.
- Disturbance / variety regulated: Changing information needs, tool/provider capabilities and future tasks.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Search services, skill/MCP bridges, settings and standby summaries.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Operational web lookup, selecting skills or switching providers does not supply external/future modeling, adaptation-option judgment and adoption into present capability. No S4-specific actor/constructor or parent adaptation return is present.
- Evidence: [docs/internals/skills.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/skills.md); [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md); [docs/internals/compaction.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/compaction.md); [src/application/session/selection.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/selection.rs).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/README.md); [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [src/session/machine.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/session/machine.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [docs/internals/skills.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/skills.md); [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md).
- Plausible first-party paths checked: Web search/fetch, disk-read skill discovery, model/provider switching, compaction/handoff and peer creation.
- Why no material first-party path remains: Operational web lookup, selecting skills or switching providers does not supply external/future modeling, adaptation-option judgment and adoption into present capability. No S4-specific actor/constructor or parent adaptation return is present.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy referral and return.
- Disturbance / variety regulated: Changes to purpose, tools, permissions and session instructions.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Session tokens, capability switches, questions, metadata/instruction edits and operator configuration.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: These paths gather task answers or enforce ordinary configuration rights. They do not route an identity/ultimate-policy tension to legitimate authority and return a binding identity decision governing the harness. Upstream maintenance governance remains adjacent.
- Evidence: [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md); [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [docs/configuration.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/configuration.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/README.md); [src/executor/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/executor/run.rs); [src/session/machine.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/session/machine.rs); [src/application/session/run.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/session/run.rs); [src/application/peer_commands.rs](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/src/application/peer_commands.rs); [docs/internals/groups.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/groups.md); [docs/internals/skills.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/skills.md); [docs/internals/tools.md](https://github.com/WindustH/wish-core/blob/28e6a07b2ac36684a3280c6ecf9b963c28bca831/docs/internals/tools.md).
- Plausible first-party paths checked: ask_user and late-answer input, tool capability switches, creator-only child configuration, server access control and idle-only instruction updates.
- Why no material first-party path remains: These paths gather task answers or enforce ordinary configuration rights. They do not route an identity/ultimate-policy tension to legitimate authority and return a binding identity decision governing the harness. Upstream maintenance governance remains adjacent.

## Distributed OSS parent arrangement

The upstream maintainer and contributors govern repository development. That adjacent organization is not a runtime parent mode of the assessed task harness. No function-specific returned organization-level S3/S4/S5 decision is credited merely from contributor activity.

## Self-hosted and non-human modes

The operator can change configuration/model, interrupt/resume sessions and answer questions. Session actors may manage sessions they created. These generic controls have no supplied whole-system supervisory mandate or identity/future-adaptation procedure. ask_user is documented as an ordinary tool call; late answers become session input, not automatic parent S3/S4/S5 evidence.

## Recursion

No complete recursive viable unit is established. Local tool execution, process spawning and durable session state alone do not demonstrate a child identity, environment and metasystem.

## Variety and escalation

Rejected/malformed model batches, unknown tool outcomes, interruption and storage/provider failures suspend or end execution and preserve evidence. Explicit resume, output feedback and context recovery may continue the task. Ownership of reconciling unknown external effects remains with the resumer; no higher VSM function is inferred from the scheduler/queue/error state.

## Evidence gaps

Pinned code and internal docs establish the runtime wiring. Cargo is unavailable in this worker; the upstream Rust build and separate wish-test suite were not executed. No live model, MCP/service or production run is claimed. External clients/tests and arbitrary user-created team roles do not supply credited owners. Bounded negatives concern this distribution rather than possible future peer programs.
