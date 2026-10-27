---
harness_id: ferrule
project_name: Ferrule
repository: https://github.com/maximarhipkin/ferrule
review_ref: 24023deffa325405db3f260a5a03d736976fa1b0
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Ferrule

## Review boundary

- System in focus: the installed Ferrule runtime, one root's operational agent tree, and its first-party self-hosted operator envelope.
- Purpose and identity: perform persistent coding/assistant work through tools, channels and scheduled tasks under explicit resource/security constraints.
- Relevant environment: user workspace, providers, concurrent child agents, external services, scheduled commitments and the deployment owner.
- Standard-distribution boundary: ferrule-core/agents and wired CLI/gateway, trust/dashboard/admin paths; optional configured learning and Linux owner mode are considered with platform limits.
- Credited operating / distribution surfaces: core ReAct agent; agent supervisor/tools/board/worktree/prompts; first-party CLI/gateway child factories, self_service admin and dashboard/config/settings/trust.
- Adjacent first-party surfaces excluded from ownership: benchmarks and ferrule-eval, tests/mock LLM, research comparisons, build/release pipelines and maintainer design approval history. Dated design status is not substituted for pinned code wiring.
- First-party operating / deployment modes considered: run/chat/gateway/scheduler with enabled agent tools; non-forked verifier role; default supervised admin and optional Linux protected owner mode; offline learning pass.
- Recursion level: root operational tree and its local deployment parent; no claim about the viability of the wider OSS organization.
- Reviewed revision: 24023deffa325405db3f260a5a03d736976fa1b0.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Ferrule assembles a Rust ReAct loop with filesystem/shell/web/MCP tools, transcript, memory, model profiles, verification and budget guards. The agents crate supplies worker/planner/verifier/media roles, child lifecycles, shared tasks, messages, cancellation and token accounting. Coding workers normally get isolated git worktrees; verifiers get throwaway snapshots. Root tools expose current child status/tokens, messaging and stop interventions. The deployment owner can inspect health/tasks/caps and approve exact administrative changes; protected owner mode executes permitted changes autonomously while reserving security-envelope settings to the dashboard. Learning reflects on failed/retried episodes and validates playbook deltas by checks or blind transcript comparison between runs. The repository's benchmark claims are not taken as observed performance.

## Operational model

Local root/children own S1 action selection. Agents claim work and select isolation/integration responses to avoid sibling interference (S2). At the root-tree recursion, the root sees current children/token use and can stop or redirect commitments under resource warnings; the deployment operator separately controls shared caps (S3 modes). A fresh verifier inspects a raw snapshot and returns evidence without altering production, providing an optional complementary audit mode. Ultimate delegation/security-envelope changes remain parent-owned. Retrospective playbook learning is not automatically S4.

## S1 — Operations

- State: A
- Function: execute coding/assistant/scheduled outcomes through a model/tool loop.
- Disturbance / variety regulated: task-specific files, commands, service responses, tool failures and verification errors.
- Decisive decision or feedback right: select actions, tool arguments and continuation after observations.
- Decision owner: root and child model-backed agents within their assigned outcomes.
- Supporting / enforcement mechanisms: provider adapters, tool registry, sandbox/credential proxy, verification, transcript, scheduler and budget/stuck guards.
- Closure path: call → tools → observations → repeated model choice; returned results and failed check tails enter subsequent operation.
- Boundary reachability: shipped run/chat/gateway and child factories construct ferrule_core::Agent and equip product tools; no external cognitive harness is borrowed.
- Why this is / is not agent-owned: enforcement alone cannot choose the next task-dependent action if the model is removed.
- Evidence: [shipped runtime](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/README.md#L30-L47); [core loop entry](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-core/src/agent.rs#L1243-L1320); [action/verification loop](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-core/src/agent.rs#L1422-L1630); [child construction](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/supervisor.rs#L697-L782).
- Basis: structural.
- Confidence: high.
- Caveats: Source-relative finding; no empirical model-quality claim.

## S2 — Coordination

- State: A
- Function: prevent duplicate task effort and mutually destructive sibling workspace edits.
- Disturbance / variety regulated: two children attempt the same work or modify the same parent checkout.
- Decisive decision or feedback right: choose/claim a non-conflicting task, select worktree isolation and decide when to integrate a returned branch.
- Decision owner: participating model agents, with the root owning integration into its checkout.
- Supporting / enforcement mechanisms: atomic SQLite claims/dependency refusals, isolated worktrees and returned branch/workspace notes.
- Closure path: claim refusal returns current ownership/dependency information; agents select other work or wait; worker changes remain isolated until root merge/cherry-pick.
- Boundary reachability: the supplied tasks and spawn_agent tools are registered for the actual running tree, not hypothetical external coordination code.
- Distinct S1 units: concurrent root/worker/planner agents producing separate code/work outcomes.
- Inter-S1 disturbance: duplicate task claims and concurrent code edits contaminating one another.
- Attenuating coordination relation: exclusive task claim plus per-worker worktree and root-controlled integration.
- Feedback into subsequent S1 behaviour: claim/result/branch metadata changes what work an agent can take and which changes enter subsequent parent operation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: atomic task ownership and workspace separation directly regulate identified duplicate-effort/edit collisions; the shared board alone is not the witness.
- Why this is / is not agent-owned: agents choose tasks/isolation and root integration; transactions/git merely enforce those choices.
- Evidence: [task choice/feedback contract](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/prompts.rs#L189-L205); [atomic conflict-aware claim](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/board.rs#L236-L280); [tool dispatch](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/tools.rs#L185-L253); [isolation wiring](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/supervisor.rs#L649-L683); [worktree integration boundary](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/docs/agents.md#L170-L190).
- Basis: structural.
- Confidence: high.
- Caveats: Outside git or on worktree failure a child may share the workspace; this is reported, not claimed equally isolated.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current child commitments/capacity and deployment spending on behalf of the root tree.
- Disturbance / variety regulated: too many live commitments, shared token scarcity and children needing intervention.
- Decisive decision or feedback right: root selects wait/message/stop and renewed child effort; parent selects shared caps and approved administrative intervention.
- Decision owner: root agent in the base tree-control mode; legitimate self-hosting operator in the separate parent mode.
- Supporting / enforcement mechanisms: child status/token projection, budget warnings, stop flags/tree accounting, admin approval cards, shared Hub caps and audit/config persistence.
- Closure path: root interventions change running child behaviour or stop descendants; approved parent cap changes are applied to the live Hub and subsequent runs are governed by them.
- Boundary reachability: message_agent/stop_agent are actual root tools; owner chat ferrule_admin and dashboard use the same first-party control APIs. No adjacent benchmark supervisor is credited.
- Whole-system current view: root lists its current children with role/status/token use and reports, and receives tree budget feedback; operator sees gateway health/current turns, tasks and shared caps.
- Current-control decision scope: current operational commitments and scarce tree/deployment resources, beyond merely decomposing the user's task.
- Why this is / is not agent-owned: the root chooses intervention under current operational feedback; fixed max-depth/token checks do not own that choice. In parent mode the operator's exact approval/cap decision owns the intervention.
- Evidence: [current child view and intervention tools](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/prompts.rs#L175-L190); [current consumption view](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/supervisor.rs#L1098-L1126); [tree budget feedback](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/supervisor.rs#L449-L474); [parent health/current control](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-cli/src/self_service/run.rs#L29-L82); [operator status view](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-cli/src/self_service/run.rs#L150-L175); [live cap return](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-cli/src/settings_admin.rs#L302-L345); [approval execution](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-cli/src/self_service/tool.rs#L178-L275).
- Basis: structural.
- Confidence: medium.
- Caveats: A is scoped to root-tree current commitments; it is not an autonomous governor of all gateway roots or OSS governance. The P mode is independently supported, not simultaneous dual ownership.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Root agent over its child tree | Current child status/token scarcity or a problematic report | Message/stop/renewed effort changes current child commitments | Agent prompts and supervisor list/budget paths above |
| Parent (`P`) | Deployment owner | Current health/spend/capacity review | Exact approved cap/admin action enters live Hub/config and subsequent operation | self_service tool/run and Settings::set_caps above |

## S3* — Complementary audit

- State: A
- Function: optionally challenge a worker/parent claim or code change through a separate verifier's raw-artifact access.
- Disturbance / variety regulated: a plausible completion report may hide broken tests, incorrect code or contaminated evidence.
- Decisive decision or feedback right: verifier chooses proof commands/code inspection and judges whether the submitted claim holds.
- Decision owner: a non-forked verifier agent in a separate session; parent acts on returned findings.
- Supporting / enforcement mechanisms: verifier-specific prompt/role, throwaway workspace snapshot, separate transcript, optional distinct provider and parent notice/report return.
- Closure path: verifier result is delivered to the parent, which can reject the claim, redirect/restart work or inspect further through its existing message/stop/tool paths.
- Boundary reachability: spawn_agent role=verifier is a shipped runtime mode with role-specific placement and child construction, not a test/eval-only role.
- Claim being audited: a submitted operational completion claim or code change.
- Ordinary reporting path: worker final report/status to parent.
- Complementary access path: verifier directly reads the copied code including uncommitted/new files and runs proof commands.
- Independence boundary: separate non-forked model context and snapshot; verifier does not implement/repair production changes. Same provider is allowed but is not claimed as model independence.
- Who acts on findings: the root/parent with authority to redirect or stop the relevant child and change its own next operation.
- Why this is / is not agent-owned: the verifier model owns the evidence-selection/verdict, rather than a deterministic parser or self-reported success flag.
- Evidence: [audit role purpose](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/prompts.rs#L18-L38); [snapshot placement](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/supervisor.rs#L649-L683); [fresh child context/role](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/supervisor.rs#L697-L782); [return and parent response modes](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/docs/agents.md#L137-L156); [verifier workspace boundary](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/docs/agents.md#L170-L190).
- Basis: structural.
- Confidence: medium.
- Caveats: Optional claim-relative audit mode, not every verifier invocation. Forking producer context, using it as ordinary same-path QA, or choosing non-isolated shared work can invalidate this independence claim; no live audit or general reliability guarantee is asserted.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supplied outside-and-future adaptation process with the required supervisory coupling established.
- Disturbance / variety regulated: future external provider/tool/user changes could demand capability adaptation.
- Decisive decision or feedback right: no shipped future-relevant option judgment and two-way S3 adoption loop established.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: offline reflection/probing/playbook deltas, model discovery/testing/fallbacks, doctor and install/update/admin operations.
- Closure path: learning applies lessons to later prompts and admin changes current capability; the inspected triggers are retrospective internal failures or present configuration needs, without an explicit external/prospective adaptation distinction.
- Why this is / is not agent-owned: learning between runs and autonomous self-configuration are not sufficient S4 evidence.
- Evidence: [retrospective learning inputs](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/docs/m16-learning-loop.md#L60-L100); [learning implementation](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-learn/src/pass.rs#L1-L105); [contrastive pass scope](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/docs/m53-contrastive-probing.md#L7-L39); [admin change scope](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/prompts.rs#L128-L158).
- Basis: structural.
- Confidence: medium.
- Caveats: Source-relative finding; no empirical model-quality claim.

### Absence scope

- Surfaces inspected: learning reflect/probe/pass/playbook paths and docs, model/provider profile/routing controls, doctor/self-service/admin capability changes and operational planner roles.
- Plausible first-party paths checked: failed-episode reflection with check/blind probe, prompt/skill improvement, model tests/fallbacks, dependency install/self-update and planner delegation.
- Why no material first-party path remains: the shipped paths improve current execution from internal episodes or implement present requested configuration. No materially external-and-prospective option-development loop linked both ways to current S3 is supplied at the declared runtime boundary.

## S5 — Policy and identity

- State: P
- Function: retain legitimate ultimate authority over the deployment's autonomy/security envelope.
- Disturbance / variety regulated: whether Ferrule may act without per-change consent while protected keys and owner-only boundaries remain reserved.
- Decisive decision or feedback right: the operator chooses Ask me first versus Protected autonomous and controls security settings that the bot cannot alter.
- Decision owner: the authenticated deployment owner via the dashboard; the model cannot grant itself this authority.
- Supporting / enforcement mechanisms: page-only sandbox-mode API, confirmation/fresh-config guard, protected configuration keys, audit record, saved policy and gateway restart.
- Closure path: the owner's mode choice is saved and audited; the gateway restarts with the returned sandbox/trust envelope, changing subsequent admin/tool behaviour.
- Boundary reachability: dashboard sandbox_mode is a first-party operating endpoint explicitly omitted from chat operation routing; owner-mode and supervised admin prompts/tools are wired alternatives.
- Identity / ultimate-policy issue: the system's standing autonomy/delegation and protected-secret authority boundary, rather than approval of a single task.
- Ultimate authority in each claimed mode: deployment owner; autonomous admin operation inside the envelope does not authorize changing the envelope itself.
- Return-to-operation path: confirmed owner choice → policy/config save → gateway restart → subsequent operation under chosen consent/autonomy mode.
- Why this is / is not agent-owned: the model may perform permitted admin work, but cannot decide its own ultimate sandbox/delegation policy.
- Evidence: [owner-only envelope and protected limits](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/docs/m54-autonomous.md#L46-L84); [actual authoritative switch and return](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-cli/src/dashboard/config_page.rs#L1203-L1288); [distinct subsequent admin behaviour](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-agents/src/prompts.rs#L102-L158); [chat routes omit sandbox authority](https://github.com/maximarhipkin/ferrule/blob/24023deffa325405db3f260a5a03d736976fa1b0/crates/ferrule-cli/src/self_service/run.rs#L29-L92).
- Basis: structural.
- Confidence: medium.
- Caveats: Linux owner mode has platform-specific constraints. This is deployment-parent policy, not a claim of project-level governance or that ordinary approval cards alone are S5.

## Distributed OSS parent arrangement

The positive P claims are local deployment-owner modes. Public maintainer approvals/design notes and benchmark results are not credited to the installed runtime's ownership. S3 base and parent modes are separately reconstructed; no human-owned S1/S2/S3* publication mode is invented.

## Self-hosted and non-human modes

CLI/chat/gateway roots support different wake behaviour; scheduled roots must explicitly await needed reports. Non-forked verifier mode is the eligible audit configuration. Default owner approvals and protected owner mode retain owner-only envelope decisions; no untested platform mode is claimed equivalent.

## Recursion

Children perform durable local work and may spawn to configured depth, but nesting alone does not establish complete recursive viability. S3 A is limited to the root's actual child-tree scope.

## Variety and escalation

Task claims/worktree metadata attenuate collision variety; status/token/budget feedback supports bounded current intervention. Tool/verification failures return to models. Tagged peer data and exact owner approvals protect authority provenance. Stop flags/caps enforce choices without themselves owning them.

## Evidence gaps

No benchmark or live LLM/provider/agent/audit execution was run. Cargo is unavailable on the inspection host, so native Rust checks are not reported PASS. Claims are pinned source/mode findings and do not demonstrate causal benefit, deployed reliability or full organizational viability. Current Profile and Skills main were refreshed; the Index-selected released Methodology 0.3.7 remains the generation/semantic contract.
