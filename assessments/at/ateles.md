---
harness_id: ateles
project_name: Ateles
repository: https://github.com/markmhendrickson/ateles
review_ref: 516edbf0bf6a96654f69b8a797fd2998aa4983cb
reviewed_at: 2026-10-21
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-21
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: —
autonomy_s4: C
autonomy_s5: P
---

# Ateles

**Canonical disposition:** included agentic harness for Index batch [#1827](https://github.com/opensiro/vsm-harness-index/issues/1827) row 2 (original candidate intake #1281 position 5). The function evidence and boundary are accepted for this exact frozen source revision.

## Review boundary

- System in focus: Ateles' shipped single-operator personal/company swarm: Apis and Anthus dispatch, Neotoma-canonical agent/policy identities, role/skill execution, first-party task and action gating and feedback.
- Purpose and identity: Execute multi-domain human/AI work in one principal's environment while keeping authority, provenance and high-risk action decisions explicitly bounded.
- Relevant environment: the operator, GitHub repositories/issues, mail/calendar/payment and content systems, Neotoma state service, model-provider CLIs and host process runner.
- Standard-distribution boundary: released Python agent daemons, shared libraries, first-party runner, configured local Neotoma and documented single-operator P1 flow, including real routed model tasks. Does not assume nonpublic live instance or a working multi-operator implementation.
- Credited operating / distribution surfaces: `execution/daemons/apis/{apis,skill_runner,build_delivery}.py`, `execution/daemons/anthus/anthus.py`, `lib/daemon_runtime/{gating,agent_loader,generalizer}.py`, shipped role/skill definitions, task identity and checkpoint modules.
- Adjacent first-party surfaces excluded from ownership: `docs/foundation/` unbuilt P2–P5 design, mocked tests, GitHub/CI/release validation, foundation `status.md` measurements of a separate local prod Neotoma from September, and unused or prospective workflow-engine slices. External model tooling and Neotoma backend are dependencies, not independently self-governing Ateles roles.
- First-party operating / deployment modes considered: Apis event→role/model skill execution, Anthus workflow dispatch, Neotoma-backed policy and identity, task-level action checkpoints and deferred build recovery; operator rule changes; drift→policy proposal. P2–P5 designed modes excluded.
- Recursion level: one personal/company multi-agent swarm under one operator, with distinct model-enabled task operations; not a multi-operator enterprise organization.
- Reviewed revision: 516edbf0bf6a96654f69b8a797fd2998aa4983cb (2026-10-17 source commit).
- Observation date: 2026-10-21.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/README.md) declares a much broader planned organizational architecture than currently ships. Its own [implementation status](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/foundation/status.md) is explicitly dated and partly measures a live Neotoma checkout outside this source review; we do not promote that measurement into reproducible current runtime truth.

Actual `Apis` can accept Neotoma task events, resolve a configured skill/agent role and launch an autonomous tool-enabled model process through `run_skill`, with role-specific prompts, scoped tools, credential treatment, retry/provider routing and run/session recording. `Anthus` also dispatches skill owner subprocesses and can harvest drift. `build_delivery` creates issue-bound claims and linked worktrees; Apis defers overlapping builds and later recovers held tasks via a release hook or startup sweep. Neotoma-canonical policy and grants constrain permissible actions, and human operator checkpoints preserve nondelegated action rights. `generalizer` produces proposed policy changes from drift but is not authorized to promote them autonomously. Source: [api](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/apis.py); [runner](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/skill_runner.py); [delivery](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/build_delivery.py); [anthus](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/anthus/anthus.py); [policy](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/gating.py); [general](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/generalizer.py).

The foundation describes future task *claim/lease/sign-off* semantics that may not match the actual runtime; [status.md](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/foundation/status.md) reports historic differences between architecture and implementation. This assessment credits executable existing daemon/runner control paths, not ideals in the documents.

## Operational model

Task/change event → select agent/skill identity → scoped model task process chooses domain actions and records outcome → relevant action gate evaluates risk/policy → allowed action executes or human operator checkpoint intervenes → later task/signal is recorded. When competing builds contend for the same GitHub issue, the second task is deferred and recovered after the active claim releases. Repeated drift can become a signed policy change proposal, but the operator holds ultimate adoption authority. External coding models are computation dependencies; the system-owned loop lies in configured first-party dispatch, permission scope, task/result path and feed-forward into operations.

## S1 — Operations

- State: A
- Function: Agent work cells perform model-guided coding, reviews, release handling, mail/calendar/content tasks in the configured personal swarm.
- Disturbance / variety regulated: Open-ended task requirements and changing tool/work results, including code defects, review findings and external requests.
- Decisive decision or feedback right: The loaded agent/skill chooses task-semantic tool actions and adapts during a headless Codex/Claude/Cursor execution; specific risky outward effects are separately gated.
- Decision owner: Each dispatched, role-defined model agent within an Ateles-controlled T4 invocation; external model inference alone is not assigned supervisory authority.
- Supporting / enforcement mechanisms: Neotoma agent_definition mirror/loader, signed grants, provider selector, context/system prompt, controlled subprocess, task/session records, event dispatch.
- Closure path: Event/task arrives → Apis/Anthus selects role and builds scoped prompt → first-party runner launches model tool loop → result/agent-produced outputs are recorded to Neotoma, can enter follow-up workflow and approved external action.
- Boundary reachability: `execution/daemons/apis/apis.py::_spawn_harness_skill()` calls shipped `skill_runner.run_skill()`; runner constructs actual CLI commands and subprocesses for named agents, and `anthus.py::_spawn_agent()` provides another wired route. External inference is a configured dependency for shipped first-party autonomous work cell, not a separately administered employee.
- Why this is / is not agent-owned: The roles' model-driven semantic choices and tool paths are bounded by first-party orchestration, identity and task/result recording. Removing the model leaves deterministic dispatch but no S1 problem-solving; keeping it in this shipped path realizes S1.
- Evidence: [api](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/apis.py); [runner](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/skill_runner.py); [anthus](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/anthus/anthus.py); [prereq](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/neotoma-agent/neotoma_agent.py); [readme](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/README.md)
- Basis: structural and explicit
- Confidence: high
- Caveats: This is source-level reachable agency, not verified live customer outcomes, daily-use statistics or deployed multi-operator scope.




## S2 — Coordination

- State: C
- Function: Prevent damaging overlap between distinct S1 agent builds targeting the same repository issue and return deferred work into task execution when the collision ceases.
- Disturbance / variety regulated: Two independent dispatched work cells can act on the same `repository#issue` before the first completes; uncoordinated duplicate editing/PR delivery would cause interference.
- Decisive decision or feedback right: Select which in-flight build retains the issue key, hold the overlapping task with an exact deferral record, and release/re-dispatch eligible deferred work when the claim ends.
- Decision owner: Deterministic first-party Apis/build_delivery machinery owns atomic in-process claim and recovery; task agents execute after the coordination decision, but there is no demonstrated agent discretion in choosing the coordination policy.
- Supporting / enforcement mechanisms: `active_build`, `claim_build`, `deferral_context`, guarded Neotoma task writes, release hook, startup sweep, deferred task recovery and scoped worktree.
- Closure path: A second task finds an active issue claim and becomes a durable `deferred_behind_build` task; the original holder's release signals a recovery sweep, which checks fresh state and re-dispatches only qualified work. Different task agents then resume in the permitted order.
- Boundary reachability: `apis.py`'s task dispatcher and recovery paths use `build_delivery` and `skill_runner.run_skill`; these are shipped Python modules, not foundation-only future requirements.
- Why this is / is not agent-owned: The code establishes a concrete inter-S1 collision and specific attenuation with feedback; `C` recognizes this first-party function-specific coordination construction without pretending the model agent chooses the rules.
- Evidence: [delivery](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/build_delivery.py); [api](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/apis.py); [runner](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/skill_runner.py)
- Basis: structural
- Confidence: moderate-high
- Caveats: The in-flight claim is explicitly process-local, not a distributed lease among independently deployed operator instances. Broader design claims are not inherited.

- Distinct S1 units: independently spawned role-defined coding/build agents on one repository/issue; the global process can accept a second eligible task while one build remains active.
- Inter-S1 disturbance: overlapping deliveries to the same `repository#issue`, with concurrent modifications and duplicated PR effects.
- Attenuating coordination relation: single active `BuildClaim`, ineligible overlapping work marked with an exact durable deferral context.
- Feedback into subsequent S1 behaviour: original holder exits → release hook → deferred recovery → fresh task check → new dispatch.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the lock specifically attenuates an evidenced collision on one object, and the release-driven recovery alters a competing S1's subsequent execution.


## S3 — Inside-and-now control

- State: ?
- Function: Whole-current swarm regulation over task priorities, resource limits, external-effect commitments and corrective intervention is plausible but not fully evidenced as one organization-level S3 decision.
- Disturbance / variety regulated: Cross-domain execution costs, asynchronous task backlog, delivery collisions and approval risks.
- Decisive decision or feedback right: A whole-system authority should choose/revise operational commitments and priorities using a global view and return changes to S1 agent work.
- Decision owner: The operator controls some execution policy, while deterministic dispatch gates constrain tasks; the evidence does not yet establish a single decisive current-control owner and closed whole-system feedback path.
- Supporting / enforcement mechanisms: Blast/confidence gate, role grants, configurable model tier, task queue, checkpoints, provider capacity windows and reports.
- Closure path: Per-action approval/checkpoint and per-task retry are implemented, but a sourced whole-swarm performance/resource bargaining and accountable reallocation loop was not reconstructed.
- Boundary reachability: No positive S3 published; the first-party task gate and current-task control paths remain plausible and prevent a bounded `—`.
- Why this is / is not agent-owned: A threshold gate and routing/scheduling are not by themselves global resource regulation; the need to inspect live, accepted priorities and operator override return paths is material.
- Evidence: [policy](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/gating.py); [api](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/apis/apis.py); [arch](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/architecture.md); [status](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/foundation/status.md)
- Basis: structural with unresolved semantics
- Confidence: moderate
- Caveats: Conservatively unknown rather than claiming static enforcement grants an agent S3 or operator `P`.




## S3* — Complementary audit

- State: —
- Function: No separate complementary, sufficiently independent audit judgment with findings returned into a current S3 management decision is established for the shipped swarm.
- Disturbance / variety regulated: Untruthful task completion, inaccurate recorded evidence or mistaken routine checks.
- Decisive decision or feedback right: A distinct, independent access path must challenge normal S1/S3 reporting and feed corrective control.
- Decision owner: Routine reviewers, workflow sign-offs, CI checks and Neotoma audit records exist; no function-specific complementary auditor/decisive feedback owner established.
- Supporting / enforcement mechanisms: Signed identities, observation provenance, developer/tests, review gates, operator checkpoints, archive and drift records.
- Closure path: Ordinary review/gate findings can block one task, but a distinct sporadic audit channel + corrective whole-system management return is not shown.
- Boundary reachability: No positive state claimed.
- Why this is / is not agent-owned: A separate reviewer role, signature or audit trail alone cannot establish S3* at the assessed agent-organization recursion.
- Evidence: [status](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/foundation/status.md); [gates](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/foundation/gates_and_workflows.md); [arch](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/architecture.md); [general](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/generalizer.py)
- Basis: structural
- Confidence: moderate
- Caveats: The repo includes substantial review and governance; the negative is narrow to complementary independent audit rather than generic verification.



### Absence scope

- Surfaces inspected: First-party routine review workflows, signed provenance, Neotoma observations, CI/tests, drift collector, operator checkpoints.
- Plausible first-party paths checked: An independent observation channel challenging S1 reports, owner of complementary audit and return of findings to S3 regulation.
- Why no material first-party path remains: Evidence demonstrates routine verification and reporting, not a different independent complementary audit-to-S3 closure in the shipped operating path.


## S4 — Outside-and-then intelligence

- State: C
- Function: Convert externally relevant runtime/organizational drift and contradictions into prospective policy-adjustment options for later authorization and operational adoption.
- Disturbance / variety regulated: New conditions, recurring failures, tool/provider behaviours, misfit of agent operating rules against task environment.
- Decisive decision or feedback right: Distinguish repeated environmental drift, propose changed agent policy, and present an adaptation option to governing authority for incorporation into future operating rules.
- Decision owner: The first-party generalizer clusters drift and creates signed `agent_policy`/revision proposals; ultimate active-policy authorization is left to the operator/approval path, with no self-promotion of live rules.
- Supporting / enforcement mechanisms: Anthus drift harvesting, threshold/risk classification, operator-conflict detection, signed proposal write, Neotoma-backed policy reader.
- Closure path: `anthus` harvests drift → `generalizer.process_signals` classifies clusters and persists policy/revision proposals → separately authorized operator must approve/adopt → live `agent_policy` loader/governing runtime can change subsequent behaviour. Last integration is a configured approval/composition path, not proven autonomous promotion.
- Boundary reachability: `lib/daemon_runtime/generalizer.py::_act_on_cluster` emits first-party rule proposals from harvested signals; `execution/daemons/anthus/anthus.py` invokes harvesting, and loader/gate read current policies. This is a prospective adaptation constructor path within the shipped system.
- Why this is / is not agent-owned: A concrete option generator and policy return surface go beyond internal task planning; `C`, not `A`, because decisions on cross-cutting rule adoption remain operator-gated.
- Evidence: [general](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/generalizer.py); [anthus](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/execution/daemons/anthus/anthus.py); [agentload](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/agent_loader.py); [policy](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/gating.py)
- Basis: structural
- Confidence: moderate
- Caveats: The revision/proposal bridge is not evidence of auto-adoption, measurable improved future outcomes or the full P5 organizational strategy vision.

- External distinction: recurring drift/errors attributable to environment, tools, policies or observed tasks, ingested by Anthus rather than a mere task-local thought.
- Future / prospective distinction: an amended `agent_policy` could change how the swarm treats later recurring situations.
- Adaptation option generated: `create_policy_proposal` / `create_revision_proposal` with signed defining fields, rather than a direct production rule overwrite.
- Path back into current capability / S3: authorized human approval/adoption to Neotoma `agent_policy` read by runtime; only a *constructor* path claimed, not autonomous deployment.


## S5 — Policy and identity

- State: P
- Function: Maintain the single-operator swarm's legitimate organizational policy and identity boundary under a named ultimate human principal.
- Disturbance / variety regulated: Cross-agent role authority, rules for what may be done autonomously, and conflicts between proposed policy drift and operator-owned governing commitments.
- Decisive decision or feedback right: Approve or reject changes to ultimate agent policies, grant scope and identity/action authority, which later runtime decisions must obey.
- Decision owner: One explicitly documented founder/operator principal governs the single-operator reference. Agent-generated rule proposals cannot overwrite operator-authored policies; multi-operator ownership/quorum remains design-only.
- Supporting / enforcement mechanisms: Neotoma-canonical `agent_policy`, signed agent-to-principal identity and grants, operator-only blast class and runtime fail-closed policy reader, change proposals.
- Closure path: Agent observes/presents proposed policy/authority revision → legitimate operator approves/adopts into canonical Neotoma policy → runtime loads resulting approved policy and applies it to subsequent agent dispatch/action gating. Human approval of individual routine PRs alone is NOT the S5 witness.
- Boundary reachability: The repo ships the single-principal regime and reads effective policies in `gating.load_policy`/agent loader; `generalizer` explicitly defers operator-conflicting and high-layer changes to the parent. The authority binding is part of the supported P1 reference, not the hypothetical P2–P5 distributed system.
- Why this is / is not agent-owned: Agent may propose; ultimate identity/policy remains with the human principal and the authorized version returns into action constraints. No autonomous S5 mode is claimed.
- Evidence: [readme](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/README.md); [policy](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/gating.py); [general](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/generalizer.py); [agentload](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/lib/daemon_runtime/agent_loader.py); [status](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/foundation/status.md)
- Basis: explicit and structural
- Confidence: moderate
- Caveats: Operator policy acceptance must be distinguished from design-only multi-operator governance and current-work approvals.

- Identity / ultimate-policy issue: who can originate/revise the swarm's operator-level `agent_policy` and effect rights, including never-automatic action classes.
- Ultimate authority in each claimed mode: single operator/parent principal. No evidenced independent swarm-level agent ultimate authority or fully configured distributed parent mode.
- Return-to-operation path: accepted Neotoma `agent_policy`/grant → loader/gate on the next affected task or action → policy-constrained agent action.


## Distributed OSS parent arrangement

No enterprise-wide distributed parent is credited. The shipped supported regime is one human operator principal using multiple local/task agents. Neotoma state and signed grant boundaries exist, but P2 multi-operator ownership, P3 multi-principal delegation, P4 quorum and P5 strategy governance are explicitly design/unbuilt in [status](https://github.com/markmhendrickson/ateles/blob/516edbf0bf6a96654f69b8a797fd2998aa4983cb/docs/foundation/status.md). Operator review of external pull requests does not create a second S5.

## Self-hosted and non-human modes

A single-operator environment can run model-providing agent skills and deterministic daemons together. The operator is a genuine policy principal but cannot be confused with an autonomous S3/S4/S5 actor. There is no evidenced entirely non-human policy owner. A model invocation that chooses task actions counts as first-party reachable S1 only via its shipped agent harness path, not via any unrestricted external model session.

## Recursion

Task agents are distinct operational roles in this recursion, not individually established recursively viable organizations. GitHub issue/build worktrees and the source-of-truth Neotoma service are means of operating and coordination rather than independent VSM recursions.

## Variety and escalation

Model/provider failure, stale policy, cross-task delivery collisions and high-impact external effects are differentiated into capacity/error signals, held/deferred tasks, strict `operator_only` checkpoints and signed new policy proposals. A collision has bounded recovery as a coordination problem; operator escalation on an individual high-risk action does not by itself prove S5. Unknown execution state and unreadable policy should not be treated as positive authority.

## Evidence gaps

- **S3 remains `?`**: task-local effect gates, role scheduling and operator dashboard are concrete, but the source review has not established a decisive whole-of-swarm resource/commitment intervention loop with current-system visibility and returned S1 regulation.
- **S3*** negative is bounded: first-party regular checks, typed review and observability inspected. A shipped alternative audit judgment path with independent complementary operational access and S3 feedback would require a correction on the exact frozen revision.
- **S4 is constructor, not autonomous**: generalizer emits prospective options, not an adopted adaptation; verification of an actual signed operator approval and reloaded policy on the source's environment was not performed.
- **S5 parent** is limited to one configured operator and operator-level policy rule return; not future multi-operator autonomous self-governance.
- Source-first static examination only; no live operator Neotoma, external Claude/Codex billing or runtime deployment was invoked. The foundation status is perishable and self-describes its measurement limits. If exact source reveals missing wires, correct this proposal before admission.
