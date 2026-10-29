---
harness_id: kheish
project_name: Kheish
repository: https://github.com/graniet/kheish
review_ref: df50433f8d577f832c6812b9e67be8ddb766059d
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Kheish

## Review boundary

- System in focus: A self-hosted Kheish daemon running one project or agent-backed session group, including its managed root and sidechain agents, project-task control, runtime permissions and durable run scheduler.
- Purpose and identity: Keep tool-using agent execution durable and accountable beyond the caller's lifetime, with recoverable scoped work and optional coordinated multi-agent tasks.
- Relevant environment: changing requests and tool observations, provider availability, process crashes, concurrent task starts, project dependencies, operator approvals and changing credentials.
- Standard-distribution boundary: shipped Rust daemon, agent runtime, project/task service, control tools, policy and journal; a configured external model provider is a runtime execution dependency.
- Credited operating / distribution surfaces: `crates/kheish-runtime`, `crates/kheish-agent`, daemon run/project services, project workflow, session task tools and the built-in coordination profile, with their documented local daemon APIs.
- Adjacent first-party surfaces excluded from ownership: documentation website, API SDK examples, tests, development agents/AGENTS.md, integration smoke fixtures and external provider internals; these corroborate behavior but are not additional deployed organizational actors.
- First-party operating / deployment modes considered: ordinary daemon-backed session agent; sidechain-enabled session; project tasks with session-member assignment and dependency/start controls; built-in coordination agent profile; optional learning automation and Playbook/Flow review; operator-managed permissions and runtime configuration.
- Recursion level: a daemon-hosted multi-session project with model/tool S1 work cells. A sidechain is task decomposition, not automatically a viable lower-recursion organization.
- Reviewed revision: `df50433f8d577f832c6812b9e67be8ddb766059d`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Kheish separates a submitting caller from a persistent daemon. The agent engine drives model calls and tool result feedback inside journaled sessions, while the daemon restores run/approval state, brokered scoped credentials and agent snapshots after interruptions. A supervisor spawns root/sidechain runtimes, tracks mailboxes and results, and enforces inherited non-widening tool/credential permissions. The project service adds durable multi-session membership, one assigned session per project task, dependency checks, a run start reservation and discussion links. Session-scoped model tools can list and change tasks, send work to children and inspect returned status; a packaged coordination specialist prompt tells the model to manage current work. Learning capture/policy/judge and Playbook/Flow projections provide separate optional memory and workflow safety mechanisms, but no automatic future-environment strategy or independent organization-level audit is established by their names.

Primary frozen sources:

- [README and daemon architecture](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/README.md)
- [Agent runtime/model/tool dependency and restoration](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/crates/kheish-runtime/src/runtime.rs)
- [Managed agent orchestration, spawning and run feedback](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/crates/kheish-agent/src/orchestrator.rs)
- [Supervisor records, mailbox and audit state](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/crates/kheish-agent/src/supervisor.rs)
- [Daemon session run scheduling/serial queue](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/crates/kheish-daemon/src/services/run.rs)
- [Project task assignment, reservation and dependency checks](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/crates/kheish-daemon/src/services/project.rs)
- [Agent-visible task listing, assignment and updates](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/crates/kheish-daemon/src/control_tools/tasks.rs)
- [Packaged coordinator profile](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/crates/kheish-daemon/src/control_tools/helpers.rs)
- [Documented project execution contract](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/docs/concepts/projects-and-project-tasks.mdx)
- [Learning publication modes and prompt visibility](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/docs/concepts/semantic-learning-and-procedural-skills.mdx)
- [Playbook/Flow review and evidence gates](https://github.com/graniet/kheish/blob/df50433f8d577f832c6812b9e67be8ddb766059d/docs/concepts/playbooks-and-flows.mdx)

## Operational model

An operator or connector submits work and may disappear; the daemon retains the run, and a configured model-based agent chooses operations, invokes tools, reads results and resumes after supported interrupts. Optional separate sidechains are agent-backed S1 work cells with their own sessions and mailboxes. Project tasks assign those cells bounded commitments; deterministic reservation/dependency rules prevent the same project task being started twice or before prerequisites settle. In the shipped coordination-profile mode a model supervisor can read tasks and subordinate status, choose assignments and follow-ups, and use tool APIs to revise current commitments. This is a supported configured mode, not proof of successful live provider runs.

## S1 — Operations

- State: A
- Function: perform user/project tasks by model-selected tool actions, revisions and outputs through durable agent sessions.
- Disturbance / variety regulated: heterogeneous goals, environmental/tool feedback, interrupted processes, provider failures and variable execution steps.
- Decisive decision or feedback right: choose next task/tool action after model output and previous observation, or request further help within the session scope.
- Decision owner: configured model-backed root and sidechain agents; the daemon enforces execution, persistence and credentials rather than selecting task-specific solutions.
- Supporting / enforcement mechanisms: `AgentRuntime`, `AgentOrchestrator`, scoped ToolRuntime, permission engine, run journals and resume queues.
- Closure path: submitted session input → model-selected call → tool result or gate/interrupt → persisted observation/resumed turn → model revises or finishes.
- Boundary reachability: daemon `serve` plus configured provider and normal session/run API create the shipped execution path; sidechains and their narrowed context are spawned by first-party supervisor APIs.
- Why this is / is not agent-owned: open-ended tool and next-step selection rests with the model loop; fixed queues and policy merely limit that discretion.
- Evidence: README quickstart; runtime.rs, orchestrator.rs, supervisor.rs; docs/concepts/agents-and-sidechains.mdx.
- Basis: structural model/tool/observation lifecycle and explicit supported daemon entry.
- Confidence: high for architecture, not for live task performance.
- Caveats: provider credentials are required for a real model run; no paid-provider task was executed here.

## S2 — Coordination

- State: C
- Function: attenuate duplicate execution of one shared project commitment and invalid concurrent starts while separate session agents pursue project work.
- Disturbance / variety regulated: more than one actor attempting to start the same assigned project task, stale assignment during preparation, or a dependent work cell starting before its predecessor's completion.
- Decisive decision or feedback right: admit only a task start whose assignee/dependencies are still valid, and reject a second nonterminal start for that shared commitment.
- Decision owner: constructor-authored project service reservation/dependency rules, not the model that submits a start request.
- Supporting / enforcement mechanisms: durable project/member/task store, `blocked_by`, expected-assignee compare, latest-run correlation, and session run queue.
- Closure path: shared task state → reservation/revalidation → one eligible assignee run starts or competing/unready request is rejected → later project task state and dependency completion determine subsequent starts.
- Boundary reachability: project service and start API are shipped daemon features and use the same persisted normal session-run path; no external scheduler or ad hoc user lock is needed.
- Why this is / is not agent-owned: rule-based start arbitration is constructor-owned; the project coordinator can still choose work, but these collision gates do not delegate the arbitration rule to a model.
- Distinct S1 units: separately configured project session members, each with a managed model/tool runtime; a project task has one assignee session.
- Inter-S1 disturbance: simultaneous attempts to act on the same project task and downstream work using unfinished or reassigned output risk duplicate/conflicting execution.
- Attenuating coordination relation: atomic start reservation, nonterminal duplicate-start rejection, assignment revalidation and completed-dependency requirement.
- Feedback into subsequent S1 behaviour: rejected starts do not generate a second run; successful run state updates the project task so dependent session work can become eligible.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the gates handle a concrete shared-work collision and prerequisite disturbance across separately executing sessions, changing actual run eligibility, not merely moving messages.
- Evidence: services/project.rs reservation and dependency tests; state/project_workflow.rs; docs/concepts/projects-and-project-tasks.mdx.
- Basis: structural concurrency control in first-party daemon code.
- Confidence: medium; bounded to project-task start contention and declared dependencies.
- Caveats: this does not prove general conflict avoidance for agents editing the same external file or that every project elects this mode.

## S3 — Inside-and-now control

- State: A
- Function: monitor and revise current project/session work commitments across delegated task agents.
- Disturbance / variety regulated: missed subtasks, changing current priorities, failed children, assignment bottlenecks and incomplete work dependencies.
- Decisive decision or feedback right: the configured coordinating model chooses subtasks/owners, reads current status/results, and updates or reassigns active commitments through control tools.
- Decision owner: model executing the first-party coordination specialist profile at the declared group level; a human/project operator can separately direct or override it, but ordinary model-controlled current work is the credited mode.
- Supporting / enforcement mechanisms: `list_tasks`, `update_task`, child spawn/messaging, stored project/session task state, permission and dependency gates; the daemon enforces what the agent chooses.
- Closure path: coordinator sees active task/child state → directs or revises assignment and follow-up → service validates/persists change → affected session agent receives task/mailbox work or subsequently eligible project start.
- Boundary reachability: coordinator profile is shipped in helpers.rs and is executable as a managed agent with exposed task and sidechain control tools; its decisions affect the same daemon sessions/project execution boundary.
- Why this is / is not agent-owned: the model, not the deterministic task store, decides which commitment needs revision; the store implements authorized state change.
- Whole-system current view: the selected project or session group's task list, assignees, dependency/status records and returned child snapshots/messages, not a claim to control unrelated daemon tenants.
- Current-control decision scope: active group task decomposition, ownership/status revisions, follow-up and interruption/stop within configured capability scope; no ultimate organizational policy authority.
- Evidence: control_tools/helpers.rs coordinator instructions; control_tools/tasks.rs list/update, orchestration and mailboxes; services/project.rs task state; docs/concepts/agents-and-sidechains.mdx.
- Basis: explicit packaged model role plus the corresponding executable state/feedback tools.
- Confidence: medium; reachable configurable coordinator mode, not a demonstrated unattended deployment.
- Caveats: external model/provider and appropriate rights are required; a simple single-session deployment may not exercise group-level S3.

## S3* — Complementary audit

- State: —
- Function: complementary independent challenge to ordinary operating/current-control reports, beyond routine task checking.
- Disturbance / variety regulated: inaccurate agent self-reporting, concealed execution defects and misleading task completion claims.
- Decisive decision or feedback right: an independently sourced audit judgment that can challenge current organizational control.
- Decision owner: no sufficiently independent shipped audit decision owner established for the declared group; ordinary run and Flow reviewers remain part of configured task execution.
- Supporting / enforcement mechanisms: append-only event journals, signed external-action records, debug captures, evidence-required Flow projections and optional verification sidechains.
- Closure path: review/evidence may fail a Flow or send a child finding to its parent task, but no distinct complementary audit channel with separate access and S3 correction is mandated.
- Why this is / is not agent-owned: logs, routine review and separation of a tool profile are not by themselves independent organizational audit judgment.
- Evidence: supervisor.rs audit entries; docs/concepts/playbooks-and-flows.mdx; docs/concepts/agents-and-sidechains.mdx.
- Basis: boundary and independence comparison.
- Confidence: medium-high within sampled shipped paths.
- Caveats: an application may compose its own truly independent auditor, but that is not attributed to the default first-party group.

### Absence scope

- Surfaces inspected: supervisor audit/journal, Playbook review/Flow evidence gates, verification agent profile, runtime logs and project task controls.
- Plausible first-party paths checked: verification sidechain as S3*, run audit trail as complementary access, Flow evidence rule as S3* current-control challenge.
- Why no material first-party path remains: these paths check task outputs, record the same execution or enforce author-specified evidence requirements without establishing independent audit access/judgment feeding a separate S3 review.

## S4 — Outside-and-then intelligence

- State: —
- Function: prospective intelligence that models the changing external environment, forms adaptation options and returns them to current capability.
- Disturbance / variety regulated: future provider/ecosystem changes, changing requirements and long-horizon operational risks.
- Decisive decision or feedback right: evaluate future environmental possibilities and authorize candidate capability adaptations.
- Decision owner: no shipped first-party prospectively oriented S4 owner established; optional model learning judges and operators review past run knowledge.
- Supporting / enforcement mechanisms: semantic fact/preference/decision extraction, scoped retrieval, optional judge, verified publication tiers and reviewed procedure skill rollout.
- Closure path: terminal run → learning candidate/review → future prompt memory or separate operator skill promotion; this is retrospective knowledge reuse, not an external-prospective S3–S4 conversation.
- Why this is / is not agent-owned: adaptive memory and procedure activation can change later prompts, but no distinct future-environment model and option-return loop was found.
- Evidence: docs/concepts/semantic-learning-and-procedural-skills.mdx; services/learning.rs, services/learning_policy.rs and services/learning_judge.rs.
- Basis: documented feature modes contrasted against Profile prospective requirement.
- Confidence: medium-high for reviewed first-party learning modes.
- Caveats: users may supply a future-scanning agent as an application, not a credited bundled organizational S4.

### Absence scope

- Surfaces inspected: semantic learning/extraction/judge/promotion policy, schedules, Playbooks and agent profiles.
- Plausible first-party paths checked: memory review as adaptation, scheduled work as external scanning, procedural skill promotion as prospective S4, operator configuration changes as parent-governed S4.
- Why no material first-party path remains: all documented shipped paths are past-run extraction, present task execution or operator-authored changes; none establishes externally prospective options with a returned current-capability decision.

## S5 — Policy and identity

- State: —
- Function: legitimate ultimate identity/mission/policy adjudication at the project/daemon recursion.
- Disturbance / variety regulated: contested operating purpose, credential risk, permission exceptions and conflicts between operational need and identity boundaries.
- Decisive decision or feedback right: settle a genuinely identity-level issue and return an authoritative policy decision to govern subsequent organization.
- Decision owner: external operator/installer defines purpose, permissions, provider credentials and runtime configuration; no internally reachable identity-policy decision and return cycle is established.
- Supporting / enforcement mechanisms: brokered auth leases, inherited non-widening child scopes, approval/user-question APIs, static runtime policy, Playbook release states and audit trail.
- Closure path: an operator can configure/approve a task and execution resumes, but the reviewed standard product does not distinguish and route an ultimate identity issue through first-party S5 closure.
- Why this is / is not agent-owned: permission and human-input gates restrict individual actions; they are not authority to redefine the system's identity or settle S3–S4 tensions.
- Evidence: README security; docs/concepts/approvals-and-questions.mdx, docs/runtime/permissions.mdx, docs/concepts/playbooks-and-flows.mdx and runtime auth/permission code.
- Basis: explicit operator-rights boundary and absence of a policy-level escalation contract.
- Confidence: medium-high.
- Caveats: a wider organization deploying Kheish can supply its own legitimate parent S5, but no separate first-party `P` loop is evidenced at this chosen boundary.

### Absence scope

- Surfaces inspected: control-plane API, permissions and leases, approvals/questions, runtime config, Playbook release governance, project/member lifecycles.
- Plausible first-party paths checked: operator approval as parent S5, inherited scopes as constitutional policy, learning publication rules as identity adaptation, Playbook verification and runtime config as S5.
- Why no material first-party path remains: these are static or task/release-level controls; an identity-level disturbance/ultimate judgment/returned organizational decision loop is not materially wired.

## Recursion

Root and sidechain agents have separate sessions, environments and scoped tool authority, but their parent-child relation alone does not prove each child has a complete independent metasystem. The claimed group-level S3 is restricted to a configured coordinating agent and its current managed tasks; broader project or institutional governance belongs outside the assessed runtime.

## Variety and escalation

The agent loop absorbs open-ended task variety. Durable journal/restart and scoped permission machinery preserve execution across environmental failures. Project reservations attenuate bounded duplicate-start/dependency conflicts; a configured coordination model can reassign current work based on returned state. Exceptions requiring permissions or human answers suspend runs and resume after external response, without automatically becoming S5 or an algedonic channel.

## Evidence gaps

- Static, exact-ref source-first inspection; no live provider invocation, deployed multi-actor race benchmark, production external credential test or independently executing auditor was performed.
- S2 is bounded to explicit project-task reservation/dependency interference; generic mailbox delivery or session run sequencing was not promoted to S2.
- S3 is the shipped *configured coordination mode*, not a claim that an arbitrary Kheish daemon automatically has a whole-project coordinating model or authority beyond its session scopes.
- No model performance or unattended long-term reliability claim is inferred from docs, tests, stored metadata or component names.
