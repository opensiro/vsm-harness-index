---
harness_id: axocoatl
project_name: Axocoatl
repository: https://github.com/axocoatl/axocoatl
review_ref: edfe5031463686dc782cf3539e5aabae4e8eb9ab
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Axocoatl

## Review boundary

- System in focus: one first-party Axocoatl daemon/workbench organization at pinned revision `edfe5031463686dc782cf3539e5aabae4e8eb9ab`, including durable Session/Agent execution, the standard model/tool loop, multi-agent Session execution, Coordinator/Workers, isolated Ways/Attempt execution, Checks/Judge/Keep control, checkpoint/memory support and the canonical Automation runtime where reachable from the shipped daemon.
- Purpose and identity: provide a local-first agent workbench in which autonomous agents perform repository work through sandboxed tools, optionally collaborate or explore isolated competing Ways, preserve durable execution evidence and return selected work to the primary Session for human review.
- Relevant environment: user objectives and operator decisions, repository/workspace state, model-provider responses, sandbox/tool results, external MCP/integration effects where configured, repository checks and events that can trigger Automations.
- Standard-distribution boundary: first-party Rust daemon, actor, coordination, memory, tools, sandbox, Session/Attempt and Automation runtime plus supported HTTP/IPC/browser controls that invoke daemon-owned state. External model endpoints, Podman/E2B implementations, external MCP servers, repository-specific test commands and business services remain dependencies and do not donate VSM ownership.
- Credited operating / distribution surfaces: `DefaultAgentBehavior` and agent actors; Session-owned sandbox and turn lifecycle; multi-agent Session execution; Coordinator/declared Workers; daemon-owned Ways/Attempt lifecycle with isolated clones/containers, Checks, optional Judge and Keep/Discard; Automation execution only as an inspected supported runtime surface.
- Adjacent first-party surfaces excluded from ownership: demo films/fixtures, marketing site, examples, CI/repository-development governance and documentation-only claims. Browser JavaScript is treated only as a client of daemon-owned control state; it does not itself supply an organizational owner.
- First-party operating / deployment modes considered: ordinary autonomous Session turns; configured multi-agent Session mode; Coordinator mode; local-Podman Ways/Attempt comparison; operator-mediated Checks/Judge/Keep; configured Automation execution.
- Recursion level: one Axocoatl runtime organization around a Workspace/Session objective. Individual autonomous agents/attempt lanes are operational units inside that boundary; external providers, repository checks and tool services are environment/dependencies.
- Reviewed revision: `edfe5031463686dc782cf3539e5aabae4e8eb9ab`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Axocoatl ships an executable daemon-owned agent organization. `DefaultAgentBehavior` performs the standard model-facing turn: it builds provider requests from durable Session context, accepts model-selected tool calls, executes them through the first-party tool layer, appends tool results to the conversation and re-enters the model loop until completion, while preserving budget, cancellation, checkpoint and memory state. The daemon therefore owns the harness loop even though model inference and some tools are external dependencies.

The repository exposes two materially different multi-agent forms. A configured `Lattice` Session spawns Session-scoped actors in one sandbox and runs them in declared dependency order, passing upstream outputs to downstream agents. Separately, `CoordinatorBehavior` decomposes a goal, assigns subtasks through a capability/budget auction, executes declared autonomous Workers with their own configured model, memory and tool boundaries, and synthesizes their results. Those mechanisms establish real plural operations, but dependency order, auctions and delegation are not credited as S2 or S3 merely by topology.

The strongest metasystemic path is the shipped Ways/Attempt mechanism. Several autonomous candidate attempts can start from the same repository snapshot and request. Each attempt receives a separate clone, branch, actor scope and rootless Podman container, cannot reach the primary workspace or sibling attempts through repository tools, and retains independent lifecycle/output/Route/usage state. This deterministic isolation directly attenuates the destructive-interference risk that would arise if competing candidates modified one shared repository checkout. The isolation decision itself is runtime-owned rather than model-owned, so the S2 publication state is `C`.

Ways also exposes a separate current-control/audit sequence. The daemon retains the whole unresolved Attempt set, lane lifecycle, outputs, Route, usage/cost, diffs and later Check/Judge state. The legitimate operator decides which surviving current candidate, if any, is returned to the primary Session by `Keep`; `Keep` requires a terminal, passing, non-empty candidate, stops all attempt containers/tasks, applies the selected delta and records the selected transcript. This is a first-party parent current-control loop, but the runtime does not choose the winning current commitment autonomously, so S3 is `P` rather than `A` or `C`.

For complementary audit, ordinary attempt reporting is the candidate agent's output/Route/lifecycle. Checks instead execute a common repository validation surface against each independent candidate clone and protect the exact checked candidate as Git objects. Only passing, non-empty survivors may enter Judge. The optional Judge is a separately selected autonomous Agent operating after Checks over the preserved candidate evidence; its returned ranking/winner is validated and persisted with the unresolved set. The Judge does not edit candidate work and is advisory: the parent operator remains the actor who performs `Keep`. This creates a materially complementary evidence path whose autonomous judgment returns into S3 parent control, so S3* is `A`.

Automations, event triggers, memory and checkpointing were inspected for S4. The canonical Automation store supports manual, interval, event and Skill-triggered DAGs and includes loop damping such as single-flight/cooldown, but these execute configured responses; they do not themselves model an external future, generate adaptation options and revise current organizational capability. Agent core/semantic/daily memory changes context and recall, but memory accumulation alone is not prospective adaptation. No qualifying S4 closure is established.

Likewise, configured agent system prompts, model/tool permissions, workspace/session identity, project instructions and human operational approval/control were inspected for S5. They constrain or describe operation but do not establish an identity/ultimate-policy issue that is escalated to legitimate ultimate authority and returned as a runtime identity/policy decision for this system boundary. S5 remains `—`.

Primary evidence:

- [`crates/axocoatl-actor/src/default_behavior.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-actor/src/default_behavior.rs) — standard model/tool feedback loop, tool dispatch, memory, checkpointing, budget and cancellation.
- [`crates/axocoatl-actor/src/coordinator.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-actor/src/coordinator.rs) — goal decomposition, capability/budget auction, declared Worker execution, worker memory/tool boundaries, resumable orchestration state and synthesis.
- [`crates/axocoatl-daemon/src/attempts.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-daemon/src/attempts.rs) — set/lane isolation identities and protected checked-candidate refs used by Judge/Keep.
- [`docs/ARCHITECTURE.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/docs/ARCHITECTURE.md) — shipped daemon wiring, Session-turn ownership, multi-agent execution, complete Attempt lifecycle, Checks/Judge/Keep closure and Automation runtime; used to reconstruct how the source surfaces are wired, not to substitute for code ownership.
- [`README.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/README.md) — supported product boundary and Ways/Attempt operator flow, used as corroboration.

## S1 — Operations

- State: A
- Function: transform user objectives into repository/workbench outcomes through autonomous model decisions, tool actions and repeated observation-feedback turns; in plural modes, autonomous Worker/Attempt agents perform bounded operational subtasks or competing candidate implementations.
- Disturbance / variety regulated: open-ended user requests, changing repository state, provider responses, tool observations/errors, heterogeneous subtasks and candidate implementation choices.
- Decisive decision or feedback right: choose substantive response/tool actions and subsequent actions after observing tool results; in Coordinator/Attempt modes, each invoked autonomous agent owns its local operational choices inside its assigned boundary.
- Decision owner: the configured model-driven Axocoatl Agent/Worker/Attempt actor.
- Supporting / enforcement mechanisms: `DefaultAgentBehavior`, provider adapters, `ToolExecutor`, hooks, sandbox boundaries, token budgets, cancellation controls, Session memory/checkpoints and daemon lifecycle state.
- Closure path: Session request reaches an autonomous Agent → model selects response/tool calls → first-party runtime executes allowed tools → tool results are appended to the model-facing conversation → the model decides subsequent tool/action or completion → durable Session/Attempt state receives the outcome.
- Boundary reachability: `DefaultAgentBehavior` is the standard actor behavior wired into normal autonomous Sessions and declared Coordinator Workers; the same streamed model/tool loop is used by isolated Attempt actors at the pinned revision.
- Why this is / is not agent-owned: deterministic runtime machinery constrains tools, budgets and persistence, but removing the model decision maker removes the substantive tool/response choices; the runtime does not reproduce materially the same operational decisions by itself.
- Evidence: [`crates/axocoatl-actor/src/default_behavior.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-actor/src/default_behavior.rs); [`crates/axocoatl-actor/src/coordinator.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-actor/src/coordinator.rs); [`docs/ARCHITECTURE.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/docs/ARCHITECTURE.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: external model endpoints supply inference and external tools may own environmental effects; they do not own the first-party execution organization. Coordinator decomposition alone is not counted as a separate VSM function.

## S2 — Coordination

- State: C
- Function: prevent competing autonomous candidate operations from interfering destructively with one another or with the primary repository while several Ways explore the same objective.
- Disturbance / variety regulated: multiple autonomous Attempt S1s start from the same repository snapshot and can perform filesystem/shell mutations; without separation, concurrent alternative implementations would contend for and overwrite one shared working tree, contaminating sibling evidence and the primary Session state.
- Decisive decision or feedback right: impose per-attempt repository/container isolation so each candidate's subsequent mutations and observations remain scoped to its own lane until a later parent selection.
- Decision owner: first-party deterministic Axocoatl Attempt runtime; isolation topology is built into the supported Ways mechanism rather than selected autonomously by an agent during the run.
- Supporting / enforcement mechanisms: set/session digest namespaces, independent `--no-hardlinks` clones, set-scoped branches and actor scopes, fresh rootless Podman containers, removal of each clone's `origin`, withheld non-rollback-safe external effects and protected refs for checked candidates.
- Closure path: parent starts several Ways from one snapshot → daemon creates distinct clone/container/actor scopes → each autonomous candidate performs later repository actions only against its own lane → sibling/primary mutations cannot enter that lane through repository tools → candidate-specific state is preserved until Checks/Keep/Discard resolves the set.
- Boundary reachability: isolated Ways are a supported first-party daemon/workbench mode for autonomous single-Agent local-Podman Sessions at the pinned ref; the clone/container identities are daemon-owned runtime paths, not demo-only scaffolding.
- Distinct S1 units: each independently executing Attempt actor/Agent is an autonomous operational candidate with its own provider/model route, tool loop, output, usage and lane state.
- Inter-S1 disturbance: competing candidates would otherwise mutate the same repository checkout and invalidate one another's work/evidence; they are intentionally exploring alternative implementations from one common snapshot.
- Attenuating coordination relation: deterministic per-lane Git clone + sandbox + actor identity isolation prevents cross-candidate and primary-workspace mutation during exploration.
- Feedback into subsequent S1 behaviour: every later repository file/shell/tool action is resolved inside that candidate's isolated lane, so each S1 observes and acts on its own evolving repository state rather than a sibling's mutations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is not Coordinator routing or dependency order; it directly regulates a concrete destructive-interference mode between simultaneously viable alternative S1 operations over one repository objective.
- Why this is / is not agent-owned: the autonomous candidates own their local implementation choices, but the coordination choice that separates their mutation domains is predetermined and enforced by the first-party runtime, so the function is constructor/runtime-owned rather than `A`.
- Evidence: [`crates/axocoatl-daemon/src/attempts.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-daemon/src/attempts.rs); [`docs/ARCHITECTURE.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/docs/ARCHITECTURE.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary multi-agent dependency order and Coordinator auction/delegation are not independently credited as S2. The positive witness is specifically the disturbance-oriented isolation of competing Ways.

## S3 — Inside-and-now control

- State: P
- Function: provide whole-set current control over an unresolved group of competing candidate operations by exposing their current evidence and allowing legitimate parent authority to select the candidate commitment that returns to the primary Session, or discard the set.
- Disturbance / variety regulated: several autonomous current candidate commitments can complete, fail, block or consume different routes/costs; only one passing non-empty candidate may be returned to the primary working tree, while unresolved/unsafe candidates must remain isolated.
- Decisive decision or feedback right: decide which eligible current Attempt, if any, becomes the kept Session result after comparing whole-set lifecycle/output/Route/diff/Check/Judge evidence.
- Decision owner: the user/operator acting as legitimate parent authority through the first-party Ways/Attempts control surface.
- Supporting / enforcement mechanisms: persisted Attempt-set manifest and lane lifecycle, whole-set current views, common Checks, optional Judge advice, Keep eligibility gates, container/task stop/join, resumable apply transaction, transcript recording and Discard cleanup.
- Closure path: several Attempts execute → daemon retains whole-set current evidence → parent inspects current candidates and their Checks/Judge evidence → parent invokes Keep on one eligible candidate (or Discard) → daemon stops all lanes, applies the selected delta and records the selected answer into canonical Session history → subsequent Session operation proceeds from that returned current-control decision.
- Boundary reachability: Ways/Checks/Judge/Keep are supported first-party daemon/workbench operations at the pinned ref; browser/CLI surfaces are clients into the same daemon-owned Attempt state, so the parent loop is reachable without borrowing demo infrastructure.
- Whole-system current view: the unresolved Attempt set retains every lane's lifecycle, output, Route, usage/cost, changed paths/diff availability, Check verdicts and optional Judgment, and blocks a new set or normal Session turn until the decision is resolved.
- Current-control decision scope: choose the current candidate commitment that may modify the primary Session checkout, or reject/discard the unresolved set; Keep then halts the sibling candidate operations and returns exactly the selected result.
- Why this is / is not agent-owned: the daemon enforces eligibility and transaction safety and Judge may advise, but the decisive selection of the current commitment is explicitly left to the operator. No standard first-party autonomous or constructor-owned base mode makes the same winner/keep decision without that parent authority.
- Evidence: [`crates/axocoatl-daemon/src/attempts.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-daemon/src/attempts.rs); [`docs/ARCHITECTURE.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/docs/ARCHITECTURE.md); [`docs/PRODUCT.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/docs/PRODUCT.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: Coordinator decomposition/auction and deterministic dependency scheduling are not counted as S3. Judge does not own Keep and is therefore treated as complementary audit input to the parent S3 loop, not as the S3 owner.

## S3* — Complementary audit

- State: A
- Function: independently challenge ordinary candidate self-report using protected repository evidence and a separate autonomous judgment path before current control chooses a candidate to keep.
- Disturbance / variety regulated: a candidate Agent can report plausible success while its actual repository delta fails common checks, is empty, differs materially in route, or is weaker than another passing candidate.
- Decisive decision or feedback right: after common Checks establish eligible non-empty survivors, independently rank those surviving candidates and produce a reasoned winner recommendation from their preserved evidence.
- Decision owner: the separately selected model-driven Judge Agent; deterministic Checks and rank validation constrain its evidence/admissible output but do not choose the substantive ranking when multiple survivors remain.
- Supporting / enforcement mechanisms: per-lane isolation, common repository Checks, protected checked-candidate Git refs, persisted Check verdicts, bounded candidate evidence, schema/rank validation and durable Judgment storage.
- Closure path: candidate Agents finish and report ordinary outputs/Routes → daemon runs the same Checks against each independent clone and protects the exact candidate identity → passing non-empty candidate evidence is presented to the selected Judge Agent → Judge returns ranked survivors/reasoning → runtime validates and persists the Judgment → parent S3 control can use that finding when deciding Keep.
- Boundary reachability: Checks and optional Judge are wired into the supported unresolved Attempt-set lifecycle at the pinned ref; Judge runs through a configured autonomous Agent/provider path, while protected candidate refs keep the audited reality independent of mutable lane storage.
- Claim being audited: that a candidate implementation is a valid, non-empty and comparatively suitable resolution of the requested repository task.
- Ordinary reporting path: each producer Attempt's model output, lifecycle state, Route/tool evidence and live changed paths/diff.
- Complementary access path: common repository Checks execute against each independent candidate clone; completed Checks protect the exact candidate tree as Git objects, and Judge consumes evidence derived from the passing protected survivors rather than merely trusting producer prose.
- Independence boundary: producer Attempts run in separate actor/clone/container identities and cannot mutate sibling candidates or the primary checkout; Judge is a separately selected Agent invoked only after Checks and does not perform candidate implementation work. Protected refs make later audit/Keep independent of mutable lane storage.
- Who acts on findings: the parent operator uses Check/Judge findings in the S3 Keep/Discard decision; `Keep` accepts only a completed, passing, non-empty candidate.
- Why this is / is not agent-owned: deterministic Checks supply direct evidence and enforce eligibility, but when multiple survivors require comparison the separate model-driven Judge owns the substantive ranking discretion. Removing the Judge leaves the same evidence but not the same comparative autonomous judgment.
- Evidence: [`crates/axocoatl-daemon/src/attempts.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-daemon/src/attempts.rs); [`docs/ARCHITECTURE.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/docs/ARCHITECTURE.md); [`README.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: Judge is advisory and optional; one surviving candidate can be resolved from Checks without Judge. The `A` state records the reachable first-party complementary autonomous audit mode, not a claim that every Attempt set always invokes it.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then adaptation loop is established at the assessed boundary.
- Disturbance / variety regulated: no supported path was found that distinguishes relevant external/future change, develops a prospective adaptation option and returns that option into current organizational capability/S3.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Automation triggers/DAGs, event lattice, Skills, Agent memory tiers, project instructions, checkpointing, Ways alternative exploration and ordinary planning were inspected.
- Closure path: no external/future distinction → adaptation-option generation → return into changed current capability path is established.
- Why this is / is not agent-owned: event-triggered Automations execute previously configured responses; agent memory/recall changes context; Ways compares current candidate solutions. None of those facts alone supplies the prospective adaptation function required by the Profile.
- Evidence: [`docs/ARCHITECTURE.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/docs/ARCHITECTURE.md); [`crates/axocoatl-daemon/src/automation_executor.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-daemon/src/automation_executor.rs); [`crates/axocoatl-actor/src/default_behavior.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-actor/src/default_behavior.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: downstream Automations can be authored for environment-monitoring/adaptation purposes, but a generic DAG/event mechanism does not itself establish a first-party S4 organizational function.

### Absence scope

- Surfaces inspected: daemon Automation store/executor and trigger runtime, event lattice/Skills paths, Agent core/daily/semantic memory and recall, project instructions/checkpointing, Coordinator planning and Ways candidate exploration.
- Plausible first-party paths checked: interval/event/Skill-triggered Automations, proactive example language, memory editing/retrieval, current-task planning, multiple candidate implementations and provider/model configuration.
- Why no material first-party path remains: all inspected shipped paths either execute configured current workflows, retain/retrieve context, or explore the present task. None establishes an externally and prospectively oriented adaptation decision that returns a generated option into Axocoatl's current organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established for the Axocoatl organization at the assessed recursion.
- Disturbance / variety regulated: no identity- or ultimate-policy-level issue is shown reaching a legitimate authority and returning as a governing runtime decision.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: agent system prompts, configured models/tools/budgets, project `AXOCOATL.md` instructions, Workspace/Session identities, sandbox/security boundaries, human approvals and ordinary operational Settings were inspected.
- Closure path: no qualifying identity/ultimate-policy issue → ultimate authority → returned policy/identity decision path is established.
- Why this is / is not agent-owned: configuration and prompts constrain behavior, and the operator owns ordinary work/control decisions, but those facts do not by themselves instantiate S5. No autonomous or parent-governed runtime path is evidenced for deciding Axocoatl's organizational identity or ultimate policy.
- Evidence: [`crates/axocoatl-actor/src/default_behavior.rs`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/crates/axocoatl-actor/src/default_behavior.rs); [`docs/ARCHITECTURE.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/docs/ARCHITECTURE.md); [`README.md`](https://github.com/axocoatl/axocoatl/blob/edfe5031463686dc782cf3539e5aabae4e8eb9ab/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: repository/project governance and operator ownership exist, but repository-maintainer governance is adjacent to the assessed runtime unless an identity-level decision is operationally wired back into the running organization.

### Absence scope

- Surfaces inspected: runtime Agent configuration/system prompts, project instructions, Workspace/Session identity, tool/security policy, approval/operator surfaces, Automation configuration and repository governance/docs.
- Plausible first-party paths checked: prompt/persona configuration, project `AXOCOATL.md`, model/tool/budget Settings, approvals, Keep/Discard, Session/Workspace naming, security constraints and maintainer governance.
- Why no material first-party path remains: these surfaces configure or constrain operational behavior and current control; the frozen standard distribution does not show an identity/ultimate-policy issue reaching legitimate S5 authority and returning to govern subsequent operation as an S5 decision.

## Recursion

Axocoatl visibly nests autonomous actors, Coordinator Workers and Attempt lanes, but nesting alone is not VSM recursion. This assessment treats those actors as operational units inside one daemon/workbench system-in-focus. Their local persistent memory, tools and autonomy may support separate lower-recursion analyses, but no additional recursive viability claim is needed for this standalone vector.

## Variety, escalation and algedonic signalling

Axocoatl attenuates operational variety through tool/sandbox permissions, token budgets, bounded call counts, one-active-turn/one-unresolved-Attempt-set constraints and isolated candidate lanes. It amplifies regulatory variety through model-selected tools, multiple heterogeneous candidate Ways, common repository Checks and optional separate Judge evidence. Parent intervention enters explicitly through Stop, Checks/Judge invocation and Keep/Discard rather than being relabelled as S5.

Failures, cancellations, interrupted turns, blocked Attempts and runtime status are durably visible, but status visibility alone is not an algedonic channel. This assessment therefore does not publish a separate function for those signals; where parent action is credited, it is classified by the S3 current-control function actually closed.

## Standalone vector

`S1=A / S2=C / S3=P / S3*=A / S4=— / S5=—`
