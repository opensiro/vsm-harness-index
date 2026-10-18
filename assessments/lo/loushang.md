---
harness_id: loushang
project_name: Loushang
repository: https://github.com/zhnt/loushang
review_ref: 3970a791ba277ecc686df7e5477c86ec71915687
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Loushang

## Review boundary

- System in focus: one first-party Loushang Coding session at pinned revision `3970a791ba277ecc686df7e5477c86ec71915687`, including its standard model/tool agent loop, Harness session/runtime, Coding Product composition, implemented multi-agent control plane, child-agent workspaces, Method/HarnessWork surfaces where selected, and the normal `loushang code` CLI wiring.
- Purpose and identity: operate an AI coding workbench in which a root coding agent can solve software-development tasks directly and organize bounded child agents for investigation, implementation, testing, review and synthesis under first-party policy, approval, workspace and lifecycle controls.
- Relevant environment: the user/operator, the working Git repository, model/provider services, optional network/tool dependencies, external package/plugin sources, and project state changed by concurrent child agents.
- Standard-distribution boundary: first-party Loushang Agent, Harness, Coding Product, implemented Harness multi-agent runtime/tool surface, Coding child-agent factory/workspace paths, current Method runtime, HarnessWork runtime, standard CLI/TUI wiring and first-party resource/tool-policy mechanisms at the pinned ref. External model providers, Git hosting/services, downstream OEM composition and roadmap-only target architecture remain environment.
- Credited operating / distribution surfaces: `loushang code` standard session wiring; model→tool agent loop; Harness session/runtime; Coding multi-agent root/child tree; `spawn_agent` / `send_message` / `wait_agent` / `list_agents` / `interrupt_agent` / `close_agent`; admitted Coding child roles; shared and isolated worker modes; collaboration recipes; completion notices; live agent-tree/progress facts; workspace artifacts and lifecycle controls.
- Adjacent first-party surfaces excluded from ownership: tests/playback and development CI for Loushang itself; roadmap/target architecture not yet implemented; contributor/maintainer design governance; implementation plans used only as development records; Hosting/AppHost surfaces explicitly described as uncomposed/default-dark where they are not part of the assessed standard Coding session; opt-in/incomplete future tool-governance target semantics beyond the implemented boundary.
- First-party operating / deployment modes considered: normal tool-enabled `loushang code`; direct root model/tool operation; root-spawned explorer/reviewer/synthesizer/proposer/critic/judge/implementation/test children; same-worktree shared implementation workers; isolated Git-worktree implementation/test workers; `parallel-review` and `debate` collaboration recipes; explicit Method selection; durable HarnessWork where selected; standard approval/policy enforcement.
- Recursion level: the assessed organization is one Coding session. The root coding agent is the inside-and-now organizing actor at this recursion; independently executing child agents are operational S1 units when delegated bounded work. External provider inference is a dependency rather than a separately credited organization.
- Reviewed revision: `3970a791ba277ecc686df7e5477c86ec71915687`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Loushang separates the model/tool loop from Harness lifecycle and Product composition. The Agent loop repeatedly samples a model, executes returned tool calls, appends tool results and continues from those results. Harness owns session/host/runtime mechanics, tools, policy, approval, sandboxing, resources and continuity; Coding owns Product semantics, prompts, tool selection, CLI and final Product composition. Method supplies explicitly selected work contracts/plans, while HarnessWork supplies durable Work lifecycle/event-log/query/recovery when selected.

The implemented multi-agent layer is a Harness-owned technical control plane consumed by Coding. The normal `loushang code` CLI constructs sessions with multi-agent enabled; in ordinary tool-enabled mode Coding installs and activates six model-callable collaboration tools. A root agent can spawn bounded child agents, send follow-up/steering messages, wait for asynchronous activity, inspect the visible agent tree, interrupt work and close descendants. Child completion notices return through the session input path. Agent records expose current lifecycle status, round, progress, workspace and artifact facts.

Coding supplies role-specific child types. Read-only roles include explorer, reviewer, synthesizer, proposer, critic and judge. Implementation workers can run in isolated Git worktrees, while `shared_implementation_worker` operates in the root session's current worktree and branch. For parallel shared writes, the root agent is explicitly instructed to assign disjoint files or responsibilities, children are instructed to preserve/adapt to concurrent changes and to stop/report overlapping required write scope, and coupled writes are to be serialized. This creates a concrete coordination loop rather than merely a message bus.

The same organization exposes current-control and complementary-audit paths. The root sees and controls its whole descendant tree and chooses which commitments to spawn, reuse, steer, interrupt or close when capacity or task conditions change. Separately, Coding defines an independent read-only reviewer role and a `parallel-review` recipe that fans out multiple independent reviewers before synthesis. These reviewers inspect operational reality directly through read/search tools rather than relying only on an implementation worker's self-report.

Current Method selection is explicit/configured rather than autonomous adaptation. Tool/resource policy and approval mechanisms govern permitted action but do not establish an identity/ultimate-policy deliberation loop. Roadmap and architecture-target material was inspected but is not credited as current S4 or S5 ownership.

Primary evidence:

- [`README.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/README.md) — current Coding workbench, sessions, tools, methods and work-product framing.
- [`docs/internals/architecture/architecture-overview.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/architecture-overview.md) — current Product/Harness/Agent ownership boundaries and implemented multi-agent scope versus target architecture.
- [`src/loushang/agent/agent_loop.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/agent/agent_loop.py) — repeated model/tool execution and feedback continuation.
- [`docs/internals/architecture/harness/multiagent/README.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/harness/multiagent/README.md) — implemented child-agent architecture, collaboration invariants, shared/isolated workspaces and executable Coding slice.
- [`docs/internals/architecture/harness/multiagent/tool-surface-boundary.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/harness/multiagent/tool-surface-boundary.md) — implemented six-tool model-callable collaboration surface and prompt discipline.
- [`src/loushang/harness/tools/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/tools/multiagent.py) — model-callable spawn/message/wait/list/interrupt/close implementations and current agent-tree projections.
- [`src/loushang/harness/multiagent/control.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/multiagent/control.py) — child admission, authority, capacity, progress/fact recording, message routing and completion notices.
- [`src/loushang/harness/session/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/session/multiagent.py) — session-owned live handles, root/child notification return and runtime-tool registration.
- [`src/loushang/coding/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/multiagent.py) — role catalog, root collaboration discipline, shared-write coordination and child workspace/tool authority.
- [`src/loushang/coding/bootstrap.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/bootstrap.py) — production Coding multi-agent installation and tool activation path.
- [`src/loushang/coding/cli/application.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/cli/application.py) — normal Coding CLI enabling the multi-agent runtime.
- [`src/loushang/harness/multiagent/recipes.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/multiagent/recipes.py) — independent parallel-review and debate topologies.
- [`src/loushang/method/runtime.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/method/runtime.py) — explicit/off Method policy and fixed-plan compilation.
- [`src/loushang/harnesswork/runtime.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harnesswork/runtime.py) — durable Work lifecycle and observable execution support.
- [`src/loushang/harness/approval/rules.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/approval/rules.py) — approval-policy persistence and user authorization mechanics.
- [`docs/internals/architecture/harness/tool-governance.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/harness/tool-governance.md) — implemented-versus-target tool-governance boundary and Product-owned policy/configuration responsibilities.

## Operational model

A Coding task is owned operationally by a model-driven root agent running the standard Agent loop against first-party tools and repository state. The root can decompose work into independently executing child agents with role/tool/workspace constraints. Shared implementation children are distinct operational units acting directly in one current worktree; isolated implementation/test children act in managed detached worktrees and return artifact/workspace facts. Runtime code supplies admission, isolation, limits, persistence, notification and policy enforcement, while the root model owns discretionary delegation, coordination and current-control choices inside the live tree.

## S1 — Operations

- State: A
- Function: transform an open-ended software-development objective into repository analysis, code/test changes or other bounded coding outcomes through a repeated model→tool→feedback loop.
- Disturbance / variety regulated: changing repository state, ambiguous implementation requirements, tool outputs, errors, test/command results, user steering and child-agent feedback.
- Decisive decision or feedback right: choose substantive next actions/tool calls, interpret returned evidence and revise subsequent coding behavior.
- Decision owner: the active root or delegated Coding agent model in the standard first-party Agent loop.
- Supporting / enforcement mechanisms: Harness session/runtime, tool registry, policy/approval checks, sandbox/workspace binding, transcript/session persistence, provider adapters and child-agent lifecycle machinery.
- Closure path: task/prompt enters the Coding session → model selects a coding/tool action → Harness executes the tool under policy → result is appended to the model context → the agent selects subsequent action from changed evidence → repository/task state changes and later model turns continue from that feedback.
- Boundary reachability: the normal `loushang code` path constructs the production Agent/Harness/Coding session and runs this model/tool loop; it is the primary distributed operating mode, not a test or example-only path.
- Why this is / is not agent-owned: deterministic runtime machinery constrains and executes already-selected actions, but removing the model eliminates the substantive coding decision loop rather than leaving an equivalent discretionary operation behind.
- Evidence: [`agent_loop.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/agent/agent_loop.py); [`architecture-overview.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/architecture-overview.md); [`README.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: model inference is provided externally, but Loushang supplies and closes the first-party operational loop that repeatedly invokes that dependency and applies its decisions to the coding environment.

## S2 — Coordination

- State: A
- Function: attenuate write/interference risk between distinct concurrently operating Coding child agents sharing one repository worktree.
- Disturbance / variety regulated: parallel implementation workers editing overlapping files/responsibilities, reverting one another's concurrent work, or producing highly coupled simultaneous writes that make the shared operational environment inconsistent.
- Decisive decision or feedback right: partition shared implementation work into non-overlapping file/responsibility scopes, decide when work may proceed concurrently versus serialize, and react to returned overlap/conflict signals.
- Decision owner: the root Coding agent in the standard multi-agent session.
- Supporting / enforcement mechanisms: `shared_implementation_worker` role constraints, root multi-agent system prompt, child prompts, spawn/message/wait/list tools, completion notices, explicit ownership instructions and the shared worktree itself.
- Closure path: root identifies bounded parallel work → root assigns explicit disjoint scopes to separate shared workers → workers operate concurrently while preserving/adapting to others' changes and stop/report if required scope overlaps → conflict/completion feedback returns to the root → root can revise scope, message, wait, interrupt/close or serialize subsequent work.
- Boundary reachability: the normal `loushang code` CLI enables multi-agent operation, installs Coding's child factory and exposes the collaboration tools to the root model; `shared_implementation_worker` is an admitted Coding type in that standard runtime.
- Distinct S1 units: two or more independently executing `shared_implementation_worker` child agents, each running the Coding Agent loop on an assigned bounded implementation outcome in the same current worktree.
- Inter-S1 disturbance: overlapping write scope or rollback of another worker's concurrent changes can cause direct interference between the operational units sharing repository state.
- Attenuating coordination relation: the root agent assigns explicit non-overlapping files/responsibilities; workers are instructed not to revert others, to adapt to concurrent changes and to stop/report scope overlap; highly coupled/same-file work is to be serialized.
- Feedback into subsequent S1 behaviour: the assigned ownership scope changes each child's permitted/expected behavior before work begins, while returned conflict/completion activity gives the root evidence to change later delegation, messaging, interruption, closure or serialization choices.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mapping rests on a named inter-worker write-conflict disturbance and a first-party attenuation contract specifically governing concurrent shared-worktree behavior; spawn/message primitives alone are not credited as S2.
- Why this is / is not agent-owned: Loushang supplies deterministic role/tool boundaries, but the root model owns the discretionary partition of actual work scopes and the concurrent-versus-serial response. Removing that agent leaves prompts and mechanisms but not the task-specific coordinating decision.
- Evidence: [`multiagent/README.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/harness/multiagent/README.md); [`coding/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/multiagent.py); [`harness/tools/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/tools/multiagent.py); [`coding/cli/application.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/cli/application.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: the runtime does not need to infer write conflicts itself for S2 ownership; the positive claim is the standard agent-owned scope-allocation/feedback relation around the explicitly documented disturbance, not generic concurrency limiting.

## S3 — Inside-and-now control

- State: A
- Function: maintain a current view of the live Coding organization and regulate current child-agent commitments/capacity on behalf of the session as a whole.
- Disturbance / variety regulated: changing child lifecycle/progress, bounded open-agent capacity, failed/completed/interrupted children that remain open, changing task priorities and current need to reuse, steer, stop or release child commitments.
- Decisive decision or feedback right: decide which bounded work to delegate, which existing child to reuse or steer, and which current child commitments to interrupt or close/release when present conditions or capacity require intervention.
- Decision owner: the root Coding agent.
- Supporting / enforcement mechanisms: live agent registry/tree, status/progress/workspace facts, `list_agents`, spawn limits, per-type limits, follow-up/steering delivery, completion notices, interrupt/close operations and session-owned handle disposal.
- Closure path: child operations generate current status/progress/completion facts → root can inspect the visible live tree → current state/capacity informs root delegation/reuse/steering/interrupt/close choice → selected control action is enforced by the Harness runtime → the live organization and available capacity change for subsequent work.
- Boundary reachability: standard tool-enabled `loushang code` sessions register the multi-agent tool pack for the root model; the current-control surface is therefore reachable in the ordinary Coding operating mode, not only via development utilities.
- Whole-system current view: `list_agents` exposes the live descendant tree visible to the root, including each agent's path/type/status/round, token/tool progress, recent activity, summary and workspace/artifact references; completion notices asynchronously return terminal state to the parent.
- Current-control decision scope: current operational commitments and resources represented by child creation/reuse, steering, interruption, closure and release of bounded open-agent capacity; deterministic limits constrain the feasible set but do not choose which commitment to retire or redirect.
- Why this is / is not agent-owned: capacity/depth/type checks are enforcement. The root model is explicitly told to inspect the tree and choose reuse/closure or further delegation; materially the same discretionary current-control decision does not remain if the root agent is removed.
- Evidence: [`harness/tools/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/tools/multiagent.py); [`harness/multiagent/control.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/multiagent/control.py); [`harness/session/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/session/multiagent.py); [`coding/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/multiagent.py); [`coding/cli/application.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/cli/application.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: the assessment credits root-agent discretion over current commitments, not scheduler/concurrency enforcement itself.

## S3* — Complementary audit

- State: A
- Function: independently inspect operational coding reality through a read-only reviewer path separate from the implementing worker's ordinary self-report, and return findings for corrective action/synthesis.
- Disturbance / variety regulated: implementation defects, security/lifecycle/test risks or inaccurate/incomplete worker conclusions that ordinary execution/reporting may fail to expose.
- Decisive decision or feedback right: form an independent review judgment from direct repository evidence rather than merely relay the implementing agent's report.
- Decision owner: the independently spawned reviewer agent(s).
- Supporting / enforcement mechanisms: dedicated `reviewer` role with read-only direct-inspection tools, isolated child context/session, multi-agent completion notices, optional multi-review fan-out and synthesizer role.
- Closure path: implementation/current repository state exists → root spawns an independent reviewer or invokes the `parallel-review` topology → reviewer directly inspects files/evidence and produces findings → findings return through child completion/synthesis → the root organization can alter subsequent implementation, delegation or acceptance behavior from those findings.
- Boundary reachability: Coding's reviewer is an admitted first-party child type in the normal multi-agent runtime, and the shipped recipe catalog separately exposes `parallel-review` with multiple reviewer replicas and a synthesizer.
- Claim being audited: that the current implementation/repository state is correct, secure, lifecycle-sound and adequately tested for the requested work.
- Ordinary reporting path: implementation workers return their own final message/summary plus workspace/artifact facts through the standard child completion path.
- Complementary access path: the reviewer role independently reads/searches the repository through read-only tools; `parallel-review` can fan out multiple independent reviewers before synthesis rather than relying on the implementer's report.
- Independence boundary: reviewer agents are separate child sessions/model turns with a reviewer-specific read-only prompt/tool set and no implementation write authority; their evidence path is direct repository inspection rather than reuse of the implementation worker's internal judgment.
- Who acts on findings: the parent/root Coding agent in ordinary spawned-review use, or the first-party synthesizer followed by the calling organization in the `parallel-review` recipe; returned findings can drive subsequent implementation/delegation/control actions.
- Why this is / is not agent-owned: runtime isolation and read-only tooling enforce independence, but the audit judgment itself is produced by the reviewer model from direct evidence. Removing the reviewer agent leaves access mechanics but no equivalent complementary evaluative judgment.
- Evidence: [`coding/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/multiagent.py); [`harness/multiagent/recipes.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/multiagent/recipes.py); [`tool-surface-boundary.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/harness/multiagent/tool-surface-boundary.md); [`harness/session/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/session/multiagent.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: the strongest direct-access witness is review of the current/shared Coding workspace. The assessment does not assume a reviewer can inspect every un-applied isolated worktree without an explicit artifact/workspace handoff.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then adaptation loop is established at the assessed Coding-session recursion.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: none established within the assessed standard-distribution boundary.
- Supporting / enforcement mechanisms: explicit Method plans, explorer/network-capable investigation, debate/review roles, resource/catalog refresh and durable Work state can support current work or developer-driven change, but none establishes the required prospective adaptation function at this recursion.
- Closure path: not applicable; no reviewed first-party path closes external/future sensing → adaptation-option generation → returned capability/current-control change as an organizational function.
- Why this is / is not agent-owned: current agents can research or reason about a task, but task-local investigation is not itself an organizational S4 adaptation loop. Method selection is explicit/configured, and capability/resource refresh applies selected/configured inputs rather than autonomously generating and adopting future-facing adaptations.
- Evidence: [`method/runtime.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/method/runtime.py); [`architecture-overview.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/architecture-overview.md); [`coding/multiagent.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/coding/multiagent.py); [`harnesswork/runtime.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harnesswork/runtime.py).
- Basis: explicit + structural absence review
- Confidence: medium-high
- Caveats: a downstream Product/OEM could compose adaptation behavior from Loushang primitives, but generic composability and roadmap targets do not establish S4 in the frozen standard boundary.

### Absence scope

- Surfaces inspected: current architecture/package ownership map; Agent loop; Coding Product and multi-agent roles/recipes; Method runtime; HarnessWork runtime; resource/tool-policy and approval surfaces; current-versus-target architecture documentation.
- Plausible first-party paths checked: explorer/network investigation, proposer/critic/judge debate, reviewer/synthesizer feedback, Method plan selection/compilation, resource/catalog refresh, durable Work recovery and architecture evolution material.
- Why no material first-party path remains: reviewed current paths either regulate the present task, replay/recover configured work, apply explicit configuration, or belong to development/roadmap governance. None supplies a standard operational loop that senses outside/future distinctions, generates organizational adaptation options and returns an adopted adaptation into present Coding capability/S3.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the assessed Coding-session recursion.
- Disturbance / variety regulated: not established as an identity/ultimate-policy issue.
- Decisive decision or feedback right: not established.
- Decision owner: none established within the assessed standard-distribution boundary.
- Supporting / enforcement mechanisms: Product-owned prompts/composition/defaults, tool policy, approval rules, user intent and Method constraints govern action/configuration, but these mechanisms do not by themselves establish S5.
- Closure path: not applicable; no reviewed path reconstructs identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned decision → subsequent organization governed by it.
- Why this is / is not agent-owned: root/child agents operate within Product policy and user/tool authority; they are not shown owning or deliberating the Coding organization's ultimate identity/policy. Conversely, ordinary user approval, tool enable/disable, Method selection, apply/discard, commit/merge/publish control and developer Product composition are not promoted to S5 without an identity-level closure loop.
- Evidence: [`architecture-overview.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/architecture-overview.md); [`harness/tool-governance.md`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/docs/internals/architecture/harness/tool-governance.md); [`approval/rules.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/harness/approval/rules.py); [`method/runtime.py`](https://github.com/zhnt/loushang/blob/3970a791ba277ecc686df7e5477c86ec71915687/src/loushang/method/runtime.py).
- Basis: explicit + structural absence review
- Confidence: medium-high
- Caveats: Loushang intentionally exposes substantial Product/OEM policy construction, but Methodology `0.3.6` does not treat generic policy/configuration extensibility as `S5=C`; the S5 function itself must first be established.

### Absence scope

- Surfaces inspected: Product/Harness ownership documentation, Coding prompts/composition boundary, approval and tool-policy paths, Method policy, multi-agent authority, tool-governance current/target contract and standard CLI operating modes.
- Plausible first-party paths checked: user approval and persisted allow decisions, Product default/profile composition, tool intent/policy, Method selection/constraints, multi-agent authority/limits, apply/discard/commit/merge/publish ownership and developer/roadmap governance.
- Why no material first-party path remains: these paths govern permissions, configuration, current work or development ownership, but no current standard-distribution path elevates an identity/ultimate-policy matter to a legitimate ultimate authority and returns that authoritative decision as the governing identity/policy of subsequent Coding operation.

## Distributed OSS parent arrangement

Loushang is open source, but repository contributor/maintainer governance was not used to infer runtime parent ownership. The assessed recursion is one operating Coding session. Public development decisions, target architecture and maintainer review are adjacent development/governance surfaces unless an explicit standard runtime return loop is established; no such organization-level parent mode is claimed here.

## Self-hosted and non-human modes

The assessed standard Coding session is self-hostable and user-supervised, but generic operator configuration/approval is not enough for parent-mode notation. No separate first-party parent-governed S3/S4/S5 mode meeting Methodology `0.3.6` closure requirements is claimed. S3 is credited to the autonomous root agent in the ordinary multi-agent mode; S4/S5 remain absent at this boundary.

## Recursion

The primary recursion is one Coding session as the viable organization under assessment. Direct root work and bounded child-agent work are S1 operations within that organization. When multiple child agents run, the root owns coordination/current-control rights over its descendant tree. A child that can itself spawn descendants forms a lower recursive organization, but this assessment does not transfer root-level function claims across recursion merely from tree structure.

## Variety and escalation

Loushang attenuates operational variety through role/tool allowlists, sandbox/workspace boundaries, approval/policy checks, child-count/depth limits, isolated worktrees and explicit shared-write ownership. Residual variety returns through tool results, child completion/conflict notices, live agent status/progress and user steering. The root model can respond by continuing directly, sending follow-up/steering input, changing delegation, serializing work, interrupting or closing children. Human/operator approval remains an external escalation path for protected actions; it is not treated as S5 merely because it can veto an operation.

## Evidence gaps

- No executed trace was available inside this assessment environment; positive claims rely on pinned first-party source/docs and production wiring rather than a newly captured runtime session.
- The S2 claim is intentionally narrow: shared-worktree write-scope interference and its root-agent allocation/feedback contract. Generic multi-agent communication is not credited.
- The S3* claim is intentionally narrow: independent read-only direct inspection of the current/shared Coding workspace and returned review findings. It does not assume direct access to every un-applied isolated child worktree.
- No current standard-distribution evidence established a prospective organizational adaptation closure for S4 or an identity/ultimate-policy closure for S5; roadmap/target architecture was excluded rather than projected into the frozen revision.
