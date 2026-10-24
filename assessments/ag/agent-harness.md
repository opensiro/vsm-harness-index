---
harness_id: agent-harness
project_name: Agent Harness
repository: https://github.com/0xenzyme/agent-harness
review_ref: 0c30ff12476898543246912a3d49d653ae86b874
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Agent Harness

## Review boundary
- System in focus: frozen first-party `0xenzyme/agent-harness` adapter/protocol plugin as installed in a supported coding host and downstream project, including `harness:execute`, CLI goal/run/checkpoint/evidence validation and source-of-truth project artifacts.
- Purpose and identity: keep multi-step coding work within accepted human Goal/Spec constraints while preserving evidence, recovery provenance, accepted completion, and project-state synchronization across tasks.
- Relevant environment: user goal, downstream repository files, host-executed model coding actions, DAG node results, test/verification artifacts, run manifest and checkpoint state, authorized user decisions.
- Standard-distribution boundary: the published host plugin, execute skill, CLI, templates and project adapter mode at the pinned SHA ([README.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/README.md); [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md)). It can **invoke the host's own model reasoning and tools** through skill instructions; it does not own Codex/other host runtime scheduler, provider internals, worker creation, model selection or concurrency.
- Credited operating / distribution surfaces: [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md); [plugins/agent-harness/scripts/agent-harness.mjs](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/scripts/agent-harness.mjs); [plugins/agent-harness/references/worker-runner-contract.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/worker-runner-contract.md); [plugins/agent-harness/references/runtime-capabilities.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/runtime-capabilities.md); [docs/project-contract.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/docs/project-contract.md); [plugins/agent-harness/references/gate-results.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/gate-results.md); [docs/cybernetic-stability.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/docs/cybernetic-stability.md).
- Adjacent first-party surfaces excluded from ownership: any Codex/other host internal model scheduler and tool runner, external providers, user-created independent agents, repository development CI/tests, docs-only future contracts, downstream business operating decisions.
- First-party modes considered: `host-direct`, `host-direct-postflight`, `durable-harness` with single model controller or host delegation when available; governed Run/DAG completion, explicitly enforced revision-safe checkpoint, validation and state sync.
- Recursion level: bounded accepted-goal project execution supervised by the host controller; DAG nodes are work units, not automatically independent first-party autonomous S1 workers.
- Reviewed revision: `0c30ff12476898543246912a3d49d653ae86b874`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The distributed `harness:execute` skill gives the active coding host a structured mode switch: direct edits when appropriate; bounded postflight sync for previously tracked simple work; durable Goal/Run/DAG control for recovery, audit or multi-worker cases. The host executes actions and, when available, delegates tasks. The Harness CLI validates Goal/Run identity, accepted task dependencies, checkpoint revision and evidence, rather than launching workers or choosing models itself ([plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md); [plugins/agent-harness/references/worker-runner-contract.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/worker-runner-contract.md); [plugins/agent-harness/references/runtime-capabilities.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/runtime-capabilities.md)).
Enforced managed Runs have a separate checkpoint and fail-closed drift/reconciliation path. Result packets remain candidate evidence until the host controller validates the accepted Goal/Task scope and records authoritative completion. No independent repository-wide future-strategy agent or organizational purpose-policy authority was found in these standard installed modes ([plugins/agent-harness/scripts/agent-harness.mjs](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/scripts/agent-harness.mjs); [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md); [docs/cybernetic-stability.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/docs/cybernetic-stability.md)).

## Operational model
Inside supported host operation, the controller agent can interpret accepted Goal/Spec, choose implementation or delegation and adapt to evidence; first-party Harness protocol and CLI provide the required durable boundary. There is no first-party runtime scheduler. Worker DAG ownership is a durable record and a guidance/gate contract, not by itself an observed independent S1 coordination feedback loop.

## S1 — Operations

- State: A
- Function: Host model controller performs real project coding/verification work under the installed Harness execute contract, with first-party Goal/Run feedback and authoritative state synchronization.
- Disturbance / variety regulated: Changing code/task requirements, tool/error outcomes, candidate worker evidence and state drift.
- Decisive decision or feedback right: Choose implementation tools, task work and revisions in the user-authorized coding host and report actual evidence.
- Decision owner: Model-driven host controller with first-party Harness-provided Goal/Run constraints; host/provider implementation internals excluded.
- Supporting / enforcement mechanisms: Execute skill, configured project Goal/Run, host tools, deterministic CLI guards and checkpoint recovery.
- Closure path: Goal/Spec → host model executes task/code actions → file/test evidence → controller checks against accepted goal → updates project authoritative state or blocks.
- Boundary reachability: The shipped `harness:execute` entry explicitly drives active host execution in durable or direct mode and invokes first-party CLI validation; the optional host's model/tool executor performs the actual operations.
- Why this is / is not agent-owned: The installed harness imposes normative control and returns evidence into the model-owned operating loop; does not claim authorship of the host's implementation.
- Evidence: [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md); [README.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/README.md); [plugins/agent-harness/scripts/agent-harness.mjs](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/scripts/agent-harness.mjs); [plugins/agent-harness/references/runtime-capabilities.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/runtime-capabilities.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded static frozen-source assessment; installed host model behavior is not verified with a live provider run. External runtime capabilities are not attributed to the first-party plugin.

## S2 — Coordination

- State: ?
- Function: Potential dependency ordering and parallel-writer isolation conditions exist but cross-S1 interference-specific first-party decision/return is not fully demonstrable.
- Distinct S1 units: Optional host-delegated worker agents, not unconditionally operating in the package.
- Inter-S1 disturbance: Overlapping repository writes and dependent tasks executed too early.
- Attenuating coordination relation: Ready-DAG/ownership gates and an unresolved-worktree `ask` boundary are first-party; actual worker-isolation enforcement and schedule are host-owned.
- Feedback into subsequent S1 behaviour: Dependency/status signals may pause host work, but no source-traced peer-interference detector or adjustment to active workers is established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A dependency DAG alone does not demonstrate concrete mutual-adjustment control for independently acting S1s.
- Disturbance / variety regulated: Independently dispatched host workers may contend for the same project files, or a dependent DAG node may run before its prerequisite finishes.
- Decisive decision or feedback right: Host decides isolation and concurrency; Harness validates DAG readiness, ownership and work mode, and must pause on unresolved collision-sensitive worktree selection.
- Decision owner: Host execution engine is responsible for real worker creation and concurrent mutation; first-party controller's S2 attenuation boundary remains unclear.
- Supporting / enforcement mechanisms: DAG dependencies, per-node ownership records, worktree recommendation and prompt guidance around separate isolated workers.
- Closure path: Recorded dependency and worktree constraints can inform host execution, but a first-party competing-worker conflict sensor and corrective act cannot be established solely from protocol artifacts.
- Boundary reachability: Multiple DAG nodes may be distinct tasks, but no independent model-worker fleet is launched by the plugin.
- Why this is / is not agent-owned: Interference controls are advisories and deterministic boundary checks tied to host runtime, so S2 is not credited just for multi-worker wording.
- Evidence: [plugins/agent-harness/references/worker-runner-contract.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/worker-runner-contract.md); [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md); [plugins/agent-harness/scripts/agent-harness.mjs](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/scripts/agent-harness.mjs); [plugins/agent-harness/references/runtime-capabilities.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/runtime-capabilities.md)
- Basis: unknown
- Confidence: low
- Caveats: Bounded static frozen-source assessment; installed host model behavior is not verified with a live provider run. External runtime capabilities are not attributed to the first-party plugin.

## S3 — Inside-and-now control

- State: A
- Function: Host agent with the installed Harness controller contract regulates currently accepted Goal/Run commitments, dependency-ready work, evidence acceptance and recovery decisions.
- Whole-system current view: bounded accepted Goal/Task/Run/DAG and gate/evidence state; not a full multi-project portfolio.
- Current-control decision scope: current goal-level commitments and recovery, evidence acceptance and pause/resume.
- Disturbance / variety regulated: Unfinished Goal tasks, stale evidence, blocked runs, checkpoint drift, unclear worker acceptance and overlapping activities.
- Decisive decision or feedback right: Decide next permissible work/action, accept or reject candidate evidence, enforce parent Goal completion, replan or pause on new authority.
- Decision owner: Model-driven host controller assigned accepted-state authority through first-party Harness protocol; CLI provides deterministic guards rather than a separate autonomous scheduler.
- Supporting / enforcement mechanisms: Goal/Spec/Run/DAG, source task state, checkpoint, dependency validation, gate results, candidate-vs-accepted evidence and State Sync Notes.
- Closure path: Project Goal/Run state → controller checks current observations and ready tasks → host chooses next work and validates artifacts → authoritative Goal/Task state and checkpoint updates inform subsequent work.
- Boundary reachability: The packaged execute skill explicitly grants controller authority for accepted Goal/Task state and delegates only ready DAG nodes while CLI checks ownership, staleness, and completion.
- Why this is / is not agent-owned: Controller agent owns consequential current work and acceptance choices within one Goal, but does not imply organization-wide S3 independent of the installed host.
- Evidence: [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md); [plugins/agent-harness/scripts/agent-harness.mjs](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/scripts/agent-harness.mjs); [docs/cybernetic-stability.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/docs/cybernetic-stability.md); [plugins/agent-harness/references/worker-runner-contract.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/worker-runner-contract.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded static frozen-source assessment; installed host model behavior is not verified with a live provider run. External runtime capabilities are not attributed to the first-party plugin.

## S3* — Complementary audit

- State: ?
- Function: Read-only optional reviewer and deterministic verification gates might challenge implementation, but sufficiently independent source-observing audit ownership is not guaranteed in the standard path.
- Claim being audited: Codex/worker completion of accepted Goal requirements.
- Ordinary reporting path: Worker result packet and its own tests/gate evidence.
- Complementary access path: Explicit optional reviewer may inspect source read-only; not a continuously committed independent audit by default.
- Independence boundary: Host/parent selects same-model reviewer; no proven independent reviewer process/method against code production in standard distribution.
- Who acts on findings: Model-led controller or human accepting Goal state, if a review was actually commissioned.
- Disturbance / variety regulated: Incorrect code, overstated completion and missing acceptance evidence.
- Decisive decision or feedback right: Optional reviewer can inspect repository artifacts when explicitly selected by the host; otherwise controller validates ordinary test/evidence records.
- Decision owner: Audit independence remains unresolved: optional reviewer inherits parent model/effort and is not obligatorily commissioned or independently scheduled by Harness.
- Supporting / enforcement mechanisms: Review template, evidence/gate validator, first-party contract for candidate acceptance and host runtime reviewer mode.
- Closure path: Code/worker result → gate check or optional reviewer → findings/failed checks may return for repair; complementary source access and governance independence not universal.
- Boundary reachability: Optional advanced reviewer is documented as explicitly selected read-only; no automatic first-party independent review process is shipped.
- Why this is / is not agent-owned: Checks, verification records and user approvals do not themselves qualify as independent S3* without demonstrable complementarity and audit decision right.
- Evidence: [plugins/agent-harness/templates/codex-agents/harness_reviewer.toml](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/templates/codex-agents/harness_reviewer.toml); [plugins/agent-harness/references/worker-runner-contract.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/worker-runner-contract.md); [plugins/agent-harness/references/gate-results.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/references/gate-results.md); [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md)
- Basis: unknown
- Confidence: low
- Caveats: Bounded static frozen-source assessment; installed host model behavior is not verified with a live provider run. External runtime capabilities are not attributed to the first-party plugin.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party external prospective scanning and adopted capability-redesign loop in the installed execution/controller distribution.
- External distinction: Project context is accepted human direction, not a first-party external-environment foresight scanner.
- Future / prospective distinction: Milestone and roadmap hierarchy are static or operator-updated commitments; they do not generate future capability adaptations.
- Adaptation option generated: None source-grounded for first-party future system capability redesign.
- Path back into current capability / S3: Only externally authored roadmap/adapter changes reach active goal execution.
- Surfaces inspected: Execute skill, CLI command handlers, Goal/Run artifacts, project adapter, roadmap/milestone hierarchy, checkpoint/recovery protocol and host capability contracts.
- Plausible first-party paths checked: horizon scanning, prospective option generation, adaptation authority, adopted changes to installed execution capabilities.
- Why no material first-party path remains: All shipped decisions are current accepted-goal execution and user-authored future instructions, not a separate first-party outside/then loop.
- Disturbance / variety regulated: Longer-term future threat/opportunity and organizational capability development outside current approved Goals.
- Decisive decision or feedback right: None evidenced beyond applying human-supplied roadmap/spec and improving execution documentation.
- Decision owner: No first-party S4 decision owner; external human or unrelated host intelligence controls strategy.
- Supporting / enforcement mechanisms: Roadmap/Milestone references, Goal/Spec records, project adapter and static skill policies.
- Closure path: Accepted roadmap/Goal bounds present work; no external future observation → strategic option/adoption → changed operational capability feedback.
- Boundary reachability: Repository artifact paths and project roadmap support current tasks, not active external horizon intelligence.
- Why this is / is not agent-owned: A roadmap heading and recovery/checkpoint protocol cannot substitute for a future-directed organizational choice/return.
- Evidence: [README.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/README.md); [docs/project-contract.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/docs/project-contract.md); [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md); [docs/cybernetic-stability.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/docs/cybernetic-stability.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded static frozen-source assessment; installed host model behavior is not verified with a live provider run. External runtime capabilities are not attributed to the first-party plugin.

### Absence scope
- Surfaces inspected: Execute skill, CLI command handlers, Goal/Run artifacts, project adapter, roadmap/milestone hierarchy, checkpoint/recovery protocol and host capability contracts.
- Plausible first-party paths checked: horizon scanning, prospective option generation, adaptation authority, adopted changes to installed execution capabilities.
- Why no material first-party path remains: All shipped decisions are current accepted-goal execution and user-authored future instructions, not a separate first-party outside/then loop.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate organization-purpose/policy deciding and returning system beyond user-set acceptance, approval and static adapter constraints.
- Identity / ultimate-policy issue: Who defines the overarching system's purpose and changes it in response to feedback?
- Ultimate authority in each claimed mode: Human/product owner and external host configuration; no first-party higher identity-governing unit.
- Return-to-operation path: Human instructions constrain a local execution, but no adaptive ultimate-policy governance loop exists.
- Surfaces inspected: Host-execute rules, project adapter and permission policy, required human gates, goal/roadmap templates and CLI validation.
- Plausible first-party paths checked: ultimate purpose review and change authority, systemic policy conflict resolution and ongoing governance return.
- Why no material first-party path remains: First-party contracts enforce boundaries created by human/host; no continuous first-party ultimate identity decision loop is supplied.
- Disturbance / variety regulated: Fundamental identity, mission, permission and scope questions are left to the user and host policy.
- Decisive decision or feedback right: Human authorizes direction and risky actions; no operational higher-recursion ultimate purpose authority generated by the plugin.
- Decision owner: External human operator/host developer, not an autonomous/persistently parent-governed first-party S5 system.
- Supporting / enforcement mechanisms: Accepted Goal and Spec, hard stop/approval rules, adapter external action policy and user authorization.
- Closure path: Human-chosen policy limits actions; no overall identity/purpose challenge → final policy decision → returned organizational adaptation loop.
- Boundary reachability: Project contracts define user authority but do not create a governing agent policy actor.
- Why this is / is not agent-owned: Approval of a destructive command and acceptance of a Goal are not whole-organization ultimate policy revision rights.
- Evidence: [docs/project-contract.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/docs/project-contract.md); [plugins/agent-harness/skills/execute/SKILL.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/plugins/agent-harness/skills/execute/SKILL.md); [docs/cybernetic-stability.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/docs/cybernetic-stability.md); [README.md](https://github.com/0xenzyme/agent-harness/blob/0c30ff12476898543246912a3d49d653ae86b874/README.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded static frozen-source assessment; installed host model behavior is not verified with a live provider run. External runtime capabilities are not attributed to the first-party plugin.

### Absence scope
- Surfaces inspected: Host-execute rules, project adapter and permission policy, required human gates, goal/roadmap templates and CLI validation.
- Plausible first-party paths checked: ultimate purpose review and change authority, systemic policy conflict resolution and ongoing governance return.
- Why no material first-party path remains: First-party contracts enforce boundaries created by human/host; no continuous first-party ultimate identity decision loop is supplied.

## Recursion

Single installed coding host with Harness control supplies the agent-led project operation (S1=A) and accepted Goal current-state control (S3=A) at one bounded project recursion. Separate host workers are optional, and Harness does not own actual worker runtime concurrency; no independent first-party S2 feedback loop or S3* reviewer is unambiguously established. Static Roadmap/approval cannot be credited as S4/S5.

## Variety and escalation

Accepted scope and evidence shape the model controller's current decisions; documented DAG readiness and protected checkpoint state enforce task-level feedback. Missing or stale results fail closed and require owner reconciliation; this is distinct from a separate organizational conflict coordinator or independent audit.

## Evidence gaps

S2 requires an actually reached first-party competing worker interference sensor and adjustment, not only host-dependent scheduling guidance. S3* requires a demonstrably independent complementary source-observation authority and corrective return beyond ordinary evidence gates/optional same-model reviewer. S4/S5 negative scopes apply only to packaged installed distribution, not any human-enterprise organization using it.
