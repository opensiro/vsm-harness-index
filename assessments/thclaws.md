---
harness_id: thclaws
project_name: thClaws
repository: https://github.com/thClaws/thClaws
review_ref: cd700937a71a391f052438d139b7b1c5a6456755
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# thClaws

## Review boundary

- System in focus: the first-party thClaws harness at pinned revision `cd700937a71a391f052438d139b7b1c5a6456755`, including the core agent/tool loop, local session/workspace runtime, opt-in Agent Teams machinery, team lead and teammate prompts, mailbox/task queue, worktree isolation and role guards, team status/merge controls, owned KMS/auto-learn paths, and signed organization-policy loader/enforcement surfaces.
- Purpose and identity: provide a native agent harness that executes environment-facing tool loops and can organize multiple teammate agents under a lead while enforcing workspace, coordination, runtime and enterprise constraints.
- Relevant environment: user tasks; local repositories/files/processes; git branches/worktrees; teammate status/task/message state; model-provider responses; external tool/MCP surfaces; organization security/identity infrastructure; and signed enterprise policy distributed by an organizational administrator.
- Standard-distribution boundary: the open-source thClaws binary and first-party CLI/GUI/headless/team/enterprise mechanisms shipped at the pinned revision. External LLM providers, third-party MCP servers, external IdPs/gateways/SIEMs, operating-system confinement facilities and the human/organization administrator are environment or Parent rather than thClaws-owned autonomous actors.
- Credited operating / distribution surfaces: `crates/core/src/agent.rs`; `crates/core/src/team.rs`; `crates/core/src/default_prompts/lead.md`; `crates/core/src/default_prompts/agent_team.md`; `user-manual/ch17-agent-teams.md`; `crates/core/src/config.rs`; `crates/core/src/policy/`; and the shipped runtime call sites that consult the active policy.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI/development logs and manuals are corroborating evidence rather than autonomous actors; external model inference, MCP implementations, IdP/gateway/SIEM decisions, git itself and OS sandbox implementations are substrate unless a first-party thClaws actor owns the relevant organizational decision.
- First-party operating / deployment modes considered: ordinary single-agent execution; opt-in Agent Teams with first-party teammate processes and lead coordination; worktree/non-worktree team modes; and organization-managed enterprise deployments using a verified signed policy. Optional KMS auto-learn and `/dream`-style knowledge maintenance are considered for S4 but not assumed to satisfy it by name.
- Recursion level: one thClaws installation/team as the system-in-focus. Lead and teammate processes are internal organizational actors. The organization administrator/security authority is an external legitimate Parent for S5 when enterprise policy mode is active.
- Reviewed revision: `cd700937a71a391f052438d139b7b1c5a6456755`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

The core agent loop persists assistant tool-use blocks, dispatches selected tools through the registry, feeds tool results back into history, and repeats until the model stops requesting tools or the iteration cap is reached. This supplies the ordinary environment-facing S1 path.

Agent Teams add a first-party organizational layer. `TeamCreate` establishes named teammates and turns the initiating agent into a coordinator; `SpawnTeammate` starts independent teammate processes; filesystem mailboxes and task records carry messages, ownership, dependencies, status and completion; `TeamStatus` gives the lead a current team/task view; and `TeamMerge` aggregates isolated worktree branches. The lead prompt gives the lead explicit authority to assign owners, set task/dependency structure, inspect status and workspace state, verify completed work, return failed work to the responsible teammate and merge accepted results. Runtime guards separately enforce role constraints and protect shared work from destructive lead actions.

The enterprise policy subsystem is a distinct Parent-owned control path. A security/IT administrator holds the signing key, signs organization policy, and deploys it. thClaws resolves an embedded/runtime verification key, verifies Ed25519 signatures, checks policy binding/expiry, stores the resulting `ActivePolicy`, and exposes enforcement accessors used at runtime. Organization policy can override user choices and constrain permission mode, available tools, remote access, serving, gateway/provider capability and related enterprise surfaces. That is credited as S5=`P`: the ultimate policy decision is owned by the legitimate external organization Parent, while first-party thClaws code makes the signed decision effective in later operation.

## Operational model

In ordinary operation, a thClaws agent observes conversation/tool results, selects an environment-facing action, the first-party registry executes it, and the result is returned to the same loop. In Team mode, a lead creates and supervises multiple operational teammate loops. Distinct workers can otherwise contend for tasks, overwrite shared work or perform destructive changes. thClaws attenuates that variety through owner reservations, blocked-by dependencies, worktree separation, role guards and explicit lead coordination; completion and failure signals return to the lead, which changes subsequent assignments or sends corrective work.

The same lead has a whole-team current view and discretionary authority over assignments, dependencies, intervention, plan approval when requested, acceptance/rework and branch integration. Its ordinary information path is teammate mailbox/status reporting, while direct workspace inspection via `Read`/`Glob`/`Grep` supplies a complementary path to challenge completion claims before the lead acts on them.

## S1 — Operations

- State: A
- Function: perform environment-facing task work through autonomous iterative tool use, including file/code/process operations and teammate-specific assigned work.
- Disturbance / variety regulated: changing user tasks, repository/file state, command/tool outcomes, provider responses and execution errors that require context-sensitive next actions.
- Decisive decision or feedback right: choose the next tool/action from current conversation and tool-result state, and decide when the operational task is sufficiently complete to stop or report completion.
- Decision owner: the active first-party thClaws agent or teammate agent in its model-driven execution loop.
- Supporting / enforcement mechanisms: core `Agent` loop, tool registry/dispatch, persistent session history, iteration cap, permission/sandbox layer and teammate process runtime.
- Closure path: task/history observation → agent selects tool call → first-party runtime dispatches it → environment/tool result returns into history → agent selects the next action or terminates/reports completion.
- Boundary reachability: the loop is the documented core runtime used by ordinary CLI/GUI/headless execution and by each first-party teammate process; it is not repository-development-only machinery.
- Why this is / is not agent-owned: deterministic dispatch executes selected calls, but the context-sensitive operational choice of what to do next is made by the agent loop; removing that decision owner leaves only execution plumbing.
- Evidence: [`crates/core/src/agent.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/agent.rs), [`thclaws-technical-manual/agentic-loop.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/thclaws-technical-manual/agentic-loop.md), [`user-manual/ch17-agent-teams.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/user-manual/ch17-agent-teams.md).
- Basis: structural
- Confidence: high
- Caveats: model inference is external compute, but thClaws owns the execution loop, action registry, observation/result return and operational actor boundary; external provider internals are not imported.

## S2 — Coordination

- State: A
- Function: attenuate interference among distinct simultaneously operating teammate agents so their work can proceed without task-ownership collisions, destructive cross-effects or dependency-order violations.
- Disturbance / variety regulated: multiple S1 teammates can contend for the same pending task, grab work outside their role, write conflicting implementation state, or damage another teammate's/shared work; documented role guards were added after an observed destructive `rm -rf tests/` incident by a lead.
- Decisive decision or feedback right: choose task owner/dependency structure and work isolation appropriate to the team situation, then redirect/reassign work when completion/failure/status feedback shows coordination needs changed.
- Decision owner: the autonomous team lead agent, which assigns owners/dependencies and coordinates teammates; individual teammates autonomously claim only eligible work within runtime-enforced reservations.
- Supporting / enforcement mechanisms: per-agent inboxes/status, task queue with owner reservation and `blocked_by`, atomic task IDs/locking, idle auto-claim, worktree isolation, teammate sandboxing, role guards, `SendMessage`, `TeamTaskCreate`, `TeamTaskClaim`, `TeamTaskComplete`, `TeamStatus` and `TeamMerge`.
- Closure path: cross-S1 contention/dependency/destructive-risk state → lead chooses owner/dependency/isolation/coordination response → runtime enforces claim eligibility/isolation/role guards → teammates operate under changed constraints → completion/failure/idle status returns to lead → subsequent coordination is revised.
- Distinct S1 units: separately running named teammate processes, each with its own agent loop, inbox/status and potentially its own git worktree/branch.
- Inter-S1 disturbance: competing claims on pending work, role-mismatched FIFO task grabs, conflicting shared/worktree edits and destructive operations that can erase or block another teammate's work.
- Attenuating coordination relation: explicit ownership/dependencies plus lead-directed assignment and runtime worktree/role-guard enforcement reduce the admissible interactions among teammates rather than merely forwarding messages.
- Feedback into subsequent S1 behaviour: task completion/failure/blocked/idle notifications and `TeamStatus` change what the lead assigns next; dependencies unblock later work and corrective messages send failed work back to the responsible teammate.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the evidence names concrete cross-worker disturbances and mechanisms whose purpose/effect is to attenuate those disturbances; messaging is only the transport for that coordination decision.
- Boundary reachability: Agent Teams are a shipped opt-in product mode registered through `teamEnabled`, with first-party tools, teammate processes and runtime guards; the S2 path is reachable without custom user-authored coordination code.
- Why this is / is not agent-owned: static guards enforce limits, but the lead autonomously decides owners, dependencies, isolation/parallel work structure and corrective coordination from live team state, so the decisive S2 response is agent-owned.
- Evidence: [`crates/core/src/default_prompts/lead.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/default_prompts/lead.md), [`user-manual/ch17-agent-teams.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/user-manual/ch17-agent-teams.md), [`crates/core/src/team.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/team.rs).
- Basis: structural
- Confidence: high
- Caveats: mailbox/task/worktree mechanisms alone would not earn S2; credit depends on the documented interference witness plus lead-owned coordination response and feedback closure.

## S3 — Inside-and-now control

- State: A
- Function: maintain current whole-team control over commitments, task ownership, dependency state, worker status, acceptance/rework and integration of the team's operational work.
- Disturbance / variety regulated: changing task backlog, blocked/failed/interrupted workers, mismatched ownership, incomplete work, branch divergence and merge conflicts that affect the current organization as a whole.
- Decisive decision or feedback right: assign and reprioritize team work, choose owners/dependencies, inspect team status, approve/revise teammate plans when that mode is requested, return failed work, decide next steps and decide when/how isolated branch work is integrated.
- Decision owner: the autonomous team lead agent acting in its shipped coordinator role.
- Supporting / enforcement mechanisms: `TeamStatus`, task queue/status files, inbox protocol, plan-approval convention, `TeamMerge`, role-specific prompts and role guards that keep the lead in a control rather than implementation role.
- Closure path: whole-team status/task/commitment state → lead evaluates current condition → lead assigns, redirects, approves/revises, waits, requests fixes or integrates work → teammates/runtime execute changed commitments → updated statuses/messages/workspace state return to the lead.
- Whole-system current view: `TeamStatus` and the filesystem task/status model expose the roster, current tasks and task queue; inbox completion/failure signals and branch/worktree state supplement that current view across the team.
- Current-control decision scope: the lead controls operational assignments, dependencies, corrective intervention, acceptance/rework and integration across all teammates rather than only selecting a worker for one subtask.
- Boundary reachability: `TeamCreate` explicitly changes the initiating agent into the shipped lead/coordinator role, and the lead prompt/runtime tools are injected in the supported Agent Teams path.
- Why this is / is not agent-owned: deterministic task/status storage does not choose the organizational response; the lead agent exercises discretionary current-control authority from the whole-team view.
- Evidence: [`crates/core/src/default_prompts/lead.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/default_prompts/lead.md), [`user-manual/ch17-agent-teams.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/user-manual/ch17-agent-teams.md), [`crates/core/src/team.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/team.rs).
- Basis: structural
- Confidence: high
- Caveats: credit is not based on the word “lead” or generic delegation; it is based on the shipped whole-team current view plus broad discretionary control over commitments and corrective/integration decisions.

## S3* — Complementary audit

- State: A
- Function: independently challenge teammate completion/quality claims through direct access to workspace reality and return discrepancies into current team control.
- Disturbance / variety regulated: a teammate may report completion while the actual code/workspace state remains incomplete, inconsistent or test-failing; relying only on its own report would leave a control blind spot.
- Decisive decision or feedback right: decide whether a reported completion is acceptable after complementary inspection, and return failed/inadequate work to the responsible teammate instead of accepting or integrating it.
- Decision owner: the autonomous team lead agent acting on the complementary inspection path.
- Supporting / enforcement mechanisms: lead-only review access through `Read`, `Glob` and `Grep`, teammate completion/inbox reporting, workspace/worktree visibility, status information and corrective `SendMessage`/merge controls.
- Closure path: teammate completion claim arrives through mailbox/status → lead separately inspects relevant workspace/code state → lead accepts/integrates or identifies discrepancy → discrepancy is messaged back to the responsible teammate → corrected work returns for renewed control/verification.
- Claim being audited: a teammate's claim that assigned implementation/task work is complete and ready for the lead's next step/integration.
- Ordinary reporting path: teammate `SendMessage`, `TeamTaskComplete`, idle notification and status/task records.
- Complementary access path: direct lead inspection of repository/workspace state with `Read`/`Glob`/`Grep`, explicitly permitted for review/coordination independently of the teammate's self-report.
- Independence boundary: the evidence source for the audit is the first-party workspace state rather than the producing teammate's message; the lead is prohibited from ordinary implementation, preserving a distinct review/control role even though it commissions and acts on the audit itself.
- Who acts on findings: the lead; the shipped prompt directs it to message the responsible teammate to fix failures rather than silently repair the implementation itself.
- Boundary reachability: the complementary inspection and corrective return are explicit in the shipped lead prompt reached by Agent Teams, not merely repository CI or an external reviewer.
- Why this is / is not agent-owned: the lead autonomously decides when the completion claim is sufficient and what corrective return is required; `Read`/`Glob`/`Grep` are only access mechanisms.
- Evidence: [`crates/core/src/default_prompts/lead.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/default_prompts/lead.md), [`user-manual/ch17-agent-teams.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/user-manual/ch17-agent-teams.md).
- Basis: structural
- Confidence: medium-high
- Caveats: ordinary tests/logs alone are not credited as S3*. Credit is limited to the explicit complementary direct-inspection path that is separate from teammate self-report and has a corrective return into S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party S4 path is established at the reviewed boundary.
- Disturbance / variety regulated: not established; thClaws has persistence, KMS reconciliation and session-derived auto-learning, but no reviewed shipped loop closes external horizon sensing → prospective adaptation option → selection/decision → reintegration into future organizational capability.
- Decisive decision or feedback right: no S4-specific actor is shown choosing a prospective organizational adaptation from externally sensed future-relevant variety.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: optional KMS, session-end `auto_learn`, KMS ingest/reconcile, persistent memory/knowledge surfaces and `/dream`-style reflective/knowledge-maintenance features.
- Closure path: these mechanisms preserve or reconcile internal historical/session knowledge, but the reviewed evidence does not close the Profile's outside-and-then adaptation conversation back into changed future capability or S3.
- Why this is / is not agent-owned: autonomous memory ingestion/reconciliation can be agentic maintenance without being S4; no distinct future-facing external intelligence/adaptation decision is evidenced.
- Evidence: [`crates/core/src/config.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/config.rs), [`README.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/README.md).
- Basis: structural
- Confidence: high
- Caveats: a future or custom workflow could use web/research tools to propose redesigns, but framework expressiveness or memory branding is not credited without a first-party S4-specific closure.

### Absence scope

- Surfaces inspected: core config and session/KMS controls; auto-learn documentation/code references; persistent memory/knowledge features; team runtime; lead/team prompts; and ordinary external tool access.
- Plausible first-party paths checked: session-end auto-learn, KMS ingest/reconcile, `/dream`/reflection-style persistence, model/tool discovery through ordinary operations, and team-level learning/review mechanisms.
- Why no material first-party path remains: the strongest mechanisms consolidate internal past experience or expose general-purpose tools; none establishes an owned external/prospective scan that generates an adaptation option and closes a decision back into the organization's future capability/current-control system.

## S5 — Identity and ultimate policy

- State: P
- Function: set and enforce organization-level identity and ultimate operating constraints for an enterprise thClaws deployment through a legitimate external Parent authority.
- Disturbance / variety regulated: end-user settings or runtime flags can otherwise diverge from organizational safety/security identity and global constraints, including permission mode, tool availability, external connectivity, serving surface, gateway/SSO/provider/plugin restrictions and policy provenance.
- Decisive decision or feedback right: choose the organization policy and signing key authority that determines which global constraints/identity rules the deployment must obey; thClaws may verify/enforce but does not autonomously redefine that ultimate policy.
- Decision owner: `P` — the organization administrator/security authority holding the private signing key and issuing the signed policy; first-party thClaws is the enforcement substrate.
- Supporting / enforcement mechanisms: Ed25519 policy verification, compile-time embedded public-key trust root, system/user policy discovery with precedence, binding/expiry checks, fail-closed startup, `ActivePolicy`, forced permission mode, denied-tool accessors, Remote/serve gates and enterprise gateway/plugin/SSO policy consumers.
- Closure path: Parent security authority defines/signs policy → policy is distributed to the deployment → thClaws verifies signature/binding/expiry against the configured trust root → verified policy becomes `ActivePolicy` → runtime decision points override/restrict user-level choices → subsequent agent operation occurs within Parent-defined identity/global constraints.
- Identity / ultimate-policy issue: who may define the organizational deployment's trusted issuer/identity and non-overridable global safety/security constraints when user preferences conflict with enterprise requirements.
- Ultimate authority in each claimed mode: in enterprise-policy mode, the external organization Parent controls the signing key and signed policy; the embedded verification key and fail-closed loader prevent an ordinary end user from substituting an unsigned/conflicting policy. Open-core mode without a policy has no claimed S5 owner and is not the positive mode used for this `P` classification.
- Return-to-operation path: a verified policy is stored as `ActivePolicy`; runtime accessors and feature enforcement consume it at decision points, so Parent choices alter permission/tool/connectivity and related behavior of subsequent operational loops.
- Boundary reachability: the policy loader/verifier and enforcement accessors are shipped in the same open-source binary, and the authoritative Enterprise guide documents the supported organization-managed deployment path; no repository-development actor is required.
- Why this is / is not agent-owned: the ultimate decision belongs to the legitimate external Parent, not to a model-driven agent. thClaws autonomously enforces the decision but may not promote enforcement into `A`; therefore the correct state is `P`.
- Evidence: [`ENTERPRISE.md`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/ENTERPRISE.md), [`crates/core/src/policy/mod.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/policy/mod.rs), [`crates/core/src/policy/verify.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/policy/verify.rs), [`crates/core/src/config.rs`](https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/config.rs).
- Basis: structural
- Confidence: high
- Caveats: policy/config naming alone would not earn S5. Credit depends on the externally legitimate Parent's signing authority, non-overridable trust/enforcement path and concrete return to later operation. The `P` state applies to the supported enterprise-policy mode, not to an unrestricted open-core launch with no policy.

## Summary

At the pinned revision thClaws is classified as **`A A A A — P`**. The strongest organizational evidence is its Agent Teams path: autonomous operational teammates are coordinated against concrete interference, a lead owns whole-team current control, and the lead has a complementary direct-inspection path for completion claims. KMS/auto-learn mechanisms do not establish a prospective S4 loop. Enterprise signed-policy mode establishes S5 through a legitimate organization Parent whose policy is cryptographically verified and enforced in subsequent runtime decisions.