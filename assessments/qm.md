---
harness_id: qm
project_name: QM
repository: https://github.com/yc-software/qm
review_ref: 9745e3425ec87df199dd82cbf5e72033f1012165
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.4
profile_version: 0.2.2
assessment_procedure_version: 0.3.4
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# QM

## Review boundary

- System in focus: QM's first-party multiplayer agent harness core at pinned revision `9745e3425ec87df199dd82cbf5e72033f1012165`, including per-scope agent loops, durable sessions/sandboxes, permissions/keychains, crons/watches/webhooks and the documented swarm session APIs.
- Purpose and identity: provide persistent scoped workspaces in which autonomous agents can execute work for people/rooms/organizations across selectable model/harness backends.
- Relevant environment: user/room work, scoped files and memory, external services reached through tools/webhooks, supported model/harness backends, organization administrators and peer worker sessions.
- Standard-distribution boundary: QM API/core, session/scope/sandbox/scheduler/policy machinery and swarm APIs. Pi/OpenCode/Codex/Claude Code/model providers are execution backends and are not credited with organizational functions QM does not itself establish.
- First-party modes considered: ordinary scoped agent turns, background crons/watches/webhooks and recursive swarm worker sessions.
- Recursion level: one QM scope/room organization with optional worker sessions. Worker recursion in the API is technical nesting unless a complete local metasystem is evidenced.
- Reviewed revision: `9745e3425ec87df199dd82cbf5e72033f1012165`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.4`.

## Repository architecture

QM gives each person or room a scoped persistent environment with memory, files, permissions, keychain, schedules and a durable sandbox. Every agent turn passes through a central core while the underlying model/harness can be selected from supported providers. Swarms add durable root/worker sessions, private worker computers, optional shared forums, messages/wakeups and bounded execution leases. The swarm protocol deliberately leaves concurrent shared-disk coordination to the agents rather than supplying a distinct first-party conflict-resolution function.

## Primary evidence

- [`README.md`](https://github.com/yc-software/qm/blob/9745e3425ec87df199dd82cbf5e72033f1012165/README.md) — multiplayer harness boundary, central agent loop, scoped memory/files/permissions/sandbox, background work and organization policy surfaces.
- [`docs/swarms.md`](https://github.com/yc-software/qm/blob/9745e3425ec87df199dd82cbf5e72033f1012165/docs/swarms.md) — durable root/worker sessions, recursive spawn, private computers, shared forum, explicit message/wakeup semantics, execution leases and bounded swarm budgets.

## S1 — Operations

- State: A
- Function: autonomous scoped agents perform user/room work through QM's central agent loop and tools inside durable scoped environments.
- Disturbance / variety regulated: user requests, local files/memory, command/tool results, external service responses and task-specific uncertainty inside the active QM scope.
- Decisive decision or feedback right: choose the next model/tool action needed to progress the current scoped task and continue or terminate the agent turn based on returned observations.
- Decision owner: the active autonomous model-driven QM agent/worker.
- Supporting / enforcement mechanisms: central core, selected model/harness backend, scoped sandbox, memory/files, keychain, permissions, fixed tool surface and execution lease.
- Closure path: the agent acts in the scoped environment, receives tool/command observations, updates work/memory/session state and returns a result that persists for later turns/background work.
- Why this is / is not agent-owned: QM's policy/sandbox constrains execution, but the operational action choice is made by the model-driven agent rather than by the scheduler or permission engine.
- Evidence: `README.md` documents the central agent loop and scoped autonomous work; `docs/swarms.md` documents durable worker sessions that act under their own context/identity and execution lease.
- Basis: explicit + structural
- Confidence: high
- Caveats: underlying model/harness engines are external implementations, but QM supplies the standard loop/scope/tool contract through which the autonomous operational actor works.

## S2 — Coordination

- State: —
- Function: no material first-party S2 function is established for regulating a specific interference among distinct QM worker S1s.
- Disturbance / variety regulated: potential shared-disk write races, worker disagreement and concurrent activity were examined, but QM does not itself close a coordination response for them at the reviewed boundary.
- Decisive decision or feedback right: no first-party S2-specific decisive right was found beyond generic spawn/message/forum/isolation/lease primitives.
- Decision owner: none established for a qualifying S2 function.
- Supporting / enforcement mechanisms: private worker computers, optional shared forum, explicit messages/wakeups, worker budgets and execution leases reduce or expose interaction but do not choose a conflict-resolution response between S1s.
- Closure path: no first-party path was found that detects/decides a concrete inter-S1 conflict and feeds the coordination result back into subsequent worker behavior as an organizational S2 loop.
- Why this is / is not agent-owned: worker autonomy and communication do not establish S2; the swarm documentation explicitly places concurrent shared-disk coordination responsibility on the workers themselves rather than on a supplied QM coordination function.
- Evidence: `docs/swarms.md` documents multiple durable workers and notes that workers sharing disk must coordinate concurrent writes themselves; messaging requires explicit agent decisions and does not auto-create a coordination controller.
- Basis: explicit + structural
- Confidence: high
- Caveats: downstream prompts/agents can use the communication primitives to implement coordination, but generic expressiveness is insufficient for `C` without a first-party S2-specific path.

### Absence scope

- Surfaces inspected: pinned README, swarm root/worker lifecycle, spawn/message/forum/wakeup paths, private/shared computer semantics, execution leases and concurrency/budget controls.
- Plausible first-party paths checked: recursive spawning, shared forum, direct/broadcast messaging, wakeups, shared-disk operation, per-worker isolation and lease/budget enforcement.
- Why no material first-party path remains: the reviewed primitives move messages, isolate environments or bound execution, but no supplied mechanism owns/constructs a response to a concrete inter-S1 disturbance and closes it back into worker behavior.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous or constructor-owned whole-system current-control function is established at the reviewed QM organization boundary.
- Disturbance / variety regulated: organization/scope permissions, model availability, worker counts, depth/message budgets and schedules constrain operation, but no first-party S3 decision loop over current whole-system commitments/resources is established.
- Decisive decision or feedback right: no material first-party agent-owned or S3-specific constructor path was found that sees current operations as a whole and discretionarily reallocates/intervenes on behalf of that whole.
- Decision owner: none established for a qualifying S3 function.
- Supporting / enforcement mechanisms: central scheduler, organization configuration, strict/auto/dangerous posture, command policy, fixed worker/depth/message budgets, sandbox/lease enforcement and administrative controls.
- Closure path: configured limits are enforced on subsequent actions, but this is enforcement of preselected policy rather than a reconstructed S3 current-control judgment/return loop.
- Why this is / is not agent-owned: neither root-agent delegation nor central deterministic administration is sufficient; the evidence does not identify an agent that owns whole-system resource/commitment regulation.
- Evidence: `README.md` separates API identity/policy/scheduler from the agent loop and gives administrators organization-level configuration; `docs/swarms.md` defines fixed swarm bounds and leases rather than an autonomous whole-system regulator.
- Basis: structural
- Confidence: high
- Caveats: a downstream root agent may choose what workers to spawn for its own task, but delegation/task decomposition alone is not S3.

### Absence scope

- Surfaces inspected: central core architecture, organization/scope configuration, scheduler/background triggers, posture/permissions, swarm budgets, root/worker lifecycle and leases.
- Plausible first-party paths checked: root-agent spawning, scheduler decisions, worker-budget enforcement, org admin controls, permission inheritance and swarm lifecycle termination.
- Why no material first-party path remains: these surfaces provide task decomposition, administration and hard bounds without an evidenced whole-system current view plus discretionary resource/commitment/intervention authority owned by an autonomous actor or S3-specific constructor path.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit channel is established beyond ordinary logs, permissions, approvals and execution/session state.
- Disturbance / variety regulated: false completion or misleading worker claims are plausible, but no first-party independent auditor path is shown challenging ordinary operational reporting with materially different evidence access.
- Decisive decision or feedback right: no qualifying independent audit judgment right is established.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: session/run history, policy/approval checks, sandbox state and other observability can support later review but do not themselves constitute S3*.
- Closure path: no complementary audit finding → control/correction return path is evidenced as a distinct first-party function.
- Why this is / is not agent-owned: the missing condition is functional independence/complementary access, not merely an autonomous evaluator actor.
- Evidence: pinned README and swarm documentation expose operational/session state and governance controls but no separate independent reviewer/auditor arrangement comparable to the Profile's S3* threshold.
- Basis: structural
- Confidence: high
- Caveats: users can inspect transcripts/results manually; generic human inspection is not published as a first-party S3* ownership mode.

### Absence scope

- Surfaces inspected: README observability/governance descriptions, worker transcripts/session state, execution leases, approval/permission paths and swarm result/message surfaces.
- Plausible first-party paths checked: transcript/audit visibility, approvals, root inspection of workers, run status and sandbox boundaries.
- Why no material first-party path remains: all observed paths are ordinary execution/governance/reporting surfaces and do not add a structurally separate complementary evidence channel with independent judgment and corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective adaptation loop is established at the reviewed QM boundary.
- Disturbance / variety regulated: external events can trigger work through crons/watches/webhooks, and memory persists experience, but those mechanisms do not by themselves model future environmental change or develop adaptation options.
- Decisive decision or feedback right: no first-party S4 decision right is shown converting external/future distinctions into adaptation options and returning them into present organizational capability.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: memory, watches, webhooks, crons and background sessions support sensing/continuity but not a qualifying outside-and-then function.
- Closure path: no external/future model → adaptation option → current capability/S3 path is established.
- Why this is / is not agent-owned: reacting autonomously to an external event or remembering past work is not S4 without the prospective adaptation relation.
- Evidence: `README.md` documents background triggers and memory; `docs/swarms.md` documents ongoing worker sessions, neither of which supplies the required prospective organizational loop.
- Basis: structural
- Confidence: high
- Caveats: domain agents running inside QM can themselves research future conditions, but that is task content unless QM supplies the organizational S4 path at the assessed boundary.

### Absence scope

- Surfaces inspected: memory, crons, watches, webhooks, background work, swarm persistence/messages and organization configuration.
- Plausible first-party paths checked: event-driven background agents, persistent memory, scheduled jobs and recursive worker research.
- Why no material first-party path remains: the reviewed features trigger or retain ordinary work; no standard path develops future-facing adaptation options and returns them into QM's own present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established beyond static/configured organization policy and user/admin control.
- Disturbance / variety regulated: permissions, model/harness availability, sharing and execution posture are important constraints, but the evidence does not show a first-party S5 conversation over organizational identity/ultimate policy.
- Decisive decision or feedback right: no qualifying S5 identity/policy decision path is established inside the harness boundary.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: organization configuration, permissions, security posture, command policy and administrative settings constrain operations.
- Closure path: configuration changes are enforced, but no identity/ultimate-policy issue → legitimate S5 decision → return-to-operation loop is established as an organizational function.
- Why this is / is not agent-owned: static policy/admin settings do not become S5 merely because they are authoritative constraints; no autonomous S5 owner or explicit parent S5 closure is evidenced.
- Evidence: `README.md` documents org/security/sharing/model/harness configuration and policy enforcement but does not reconstruct identity/ultimate-policy closure at the assessed recursion.
- Basis: structural
- Confidence: high
- Caveats: a human organization using QM can of course make policy decisions outside the harness; this assessment does not infer a first-party parent S5 mode from generic administrator control.

### Absence scope

- Surfaces inspected: organization/admin configuration, permissions, sharing, harness/model availability, security posture, command policy, scope inheritance and central core architecture.
- Plausible first-party paths checked: admin policy edits, approval/permission enforcement, organization defaults and human ownership of deployment settings.
- Why no material first-party path remains: these are configuration/enforcement surfaces; no first-party protocol establishes a genuine identity/ultimate-policy issue reaching legitimate authority and returning as an organizational S5 closure.

## Recursion

QM can recursively spawn worker sessions, but workers do not automatically expose their own complete S1–S5 metasystem. Recursive spawn depth is therefore treated as technical/task recursion rather than VSM recursion.

## Variety and escalation

QM provides strong attenuation through scope isolation, permissions, fixed budgets and execution leases while allowing agent workers to absorb local task variety. The reviewed boundary intentionally leaves many organizational choices to users/root agents or downstream composition rather than supplying higher VSM functions itself.

## Evidence gaps

No positive S2–S5 state is inferred from generic messaging, centralized administration, observability, event triggers or static policy. The reviewed source is sufficient for `—` rather than `?` because the primary architecture and swarm-control surfaces explicitly expose where those responsibilities do and do not reside.

## Admission conclusion

Canonical vector: `A — — — — —`.
