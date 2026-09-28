---
harness_id: autoharness
project_name: AutoHarness
repository: https://github.com/aiming-lab/AutoHarness
review_ref: 3561e468f9ca9f9bf282512e695bd32e4e90fef4
reviewed_at: 2026-09-15
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
last_checked_ref: 3561e468f9ca9f9bf282512e695bd32e4e90fef4
last_checked_at: 2026-09-28
assessment_changed_at: 2026-09-28
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# AutoHarness

## Review boundary

- System in focus: the first-party AutoHarness Python distribution at `3561e468f9ca9f9bf282512e695bd32e4e90fef4`, including `AgentLoop`, the tool-governance pipeline, packaged multi-agent/fork/swarm/coordinator primitives, built-in agent definitions, and explicit verification surfaces available to an embedding application.
- Purpose and identity: execute model-driven agent work under repository-owned tool governance, with optional multi-agent composition and complementary verification primitives.
- Relevant environment: users and embedding applications, external model providers, project workspaces, tools/commands, repository state, and parent-authored constitutions/permissions.
- Standard-distribution boundary: the installable AutoHarness package and documented supported modes at the pinned default-branch revision. Application-specific business logic, custom agents, external model cognition, project-specific CI, and operator decisions remain environment or parent composition unless a first-party path explicitly incorporates them.
- Credited operating / distribution surfaces: `autoharness/agent_loop.py`, `autoharness/core/pipeline.py`, `autoharness/agents/swarm.py`, `autoharness/agents/builtin.py`, packaged multi-agent support, and the documented Verification-agent constructor path in `docs/guides/multi-agent.md`.
- Adjacent first-party surfaces excluded from ownership: repository tests/examples, CI/release activity, documentation-only demonstrations when no matching runtime path exists, and maintainer/contributor governance. Verification tests corroborate the primitive but do not themselves become runtime audit ownership.
- First-party operating / deployment modes considered: ordinary `AgentLoop`; enhanced governance pipeline; optional fork/background/swarm/coordinator composition; optional built-in Verification agent; explicit `ToolGovernancePipeline.verify_session()` verification when invoked by an embedding application.
- Recursion level: one AutoHarness application organization. Forked/background/swarm members may be operational agents, but spawning or role specialization does not establish complete viable recursion by itself.
- Reviewed revision: `3561e468f9ca9f9bf282512e695bd32e4e90fef4`.
- Observation date: 2026-09-28 same-ref correction. The upstream default branch still resolves exactly to the accepted review ref, so there is no upstream delta to repin.
- Generated Profile version: not recorded in the legacy artifact.
- Generated Methodology version: not recorded in the legacy artifact.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

`AgentLoop` is the model-driven execution loop. Tool calls pass through a first-party governance pipeline that can parse/validate, classify risk, run hooks, check permissions, execute tools, sanitize output, track trust/turn limits, and write audit records. These deterministic controls constrain S1 but do not inherit an organizational function merely because they can block or meter execution.

Multi-agent support includes fork/background execution, a file-backed JSONL `TeamMailbox`, swarm members, and coordinator-mode delegation. Swarm messages include ordinary messages/broadcast plus lifecycle protocol messages such as shutdown and plan-approval responses. The mailbox transports those messages; the reviewed distribution does not tie the protocol to a concrete inter-S1 collision/oscillation and a corresponding attenuation loop.

AutoHarness separately ships a built-in `Verification` agent whose prompt is explicitly adversarial. It has direct Read/Grep/Glob/Bash access and must run applicable build, test, lint/type-check and adversarial probes, recording observed output before returning `PASS`, `FAIL`, or `PARTIAL`. The documented post-implementation pattern forks that verifier after production work. A separate deterministic `VerificationEngine` can inspect session audit history and challenge completion claims. These are function-specific complementary-audit primitives, but the caller still has to invoke the audit path and compose FAIL/PARTIAL findings back into corrective execution and re-verification.

## Operational model

The primary S1 is the model-driven `AgentLoop` that interprets a task, selects/uses tools, observes results and continues until an outcome is produced. Governance machinery supplies deterministic constraints and evidence around that operation. Optional worker agents can perform delegated operational tasks.

The current-contract correction removes the former S2 constructor credit. A generic mailbox plus plan/shutdown protocol is not S2 unless evidence establishes a concrete interference/conflict/oscillation among distinct S1s, an attenuation relation specific to it, and feedback changing later S1 behaviour. The pinned repository exposes transport/lifecycle primitives, but not that functional witness.

S3* remains `C` for a different reason: AutoHarness deliberately ships a specialized adversarial verifier that obtains complementary evidence directly from the workspace rather than trusting the producing agent's report. The audit judgment path is first-party and function-specific, while the downstream application must still compose invocation, corrective return and re-verification.

## Primary evidence

- [`autoharness/agent_loop.py`](https://github.com/aiming-lab/AutoHarness/blob/3561e468f9ca9f9bf282512e695bd32e4e90fef4/autoharness/agent_loop.py) — first-party autonomous execution loop.
- [`autoharness/core/pipeline.py`](https://github.com/aiming-lab/AutoHarness/blob/3561e468f9ca9f9bf282512e695bd32e4e90fef4/autoharness/core/pipeline.py) — deterministic tool-governance pipeline plus explicit `verify_session()` entry point over audit history.
- [`autoharness/agents/swarm.py`](https://github.com/aiming-lab/AutoHarness/blob/3561e468f9ca9f9bf282512e695bd32e4e90fef4/autoharness/agents/swarm.py) — `TeamMailbox`, team membership and generic message/broadcast/shutdown/plan-approval transport.
- [`docs/concepts/agents.md`](https://github.com/aiming-lab/AutoHarness/blob/3561e468f9ca9f9bf282512e695bd32e4e90fef4/docs/concepts/agents.md) — supported fork/background/swarm/coordinator modes and built-in agent types.
- [`autoharness/agents/builtin.py`](https://github.com/aiming-lab/AutoHarness/blob/3561e468f9ca9f9bf282512e695bd32e4e90fef4/autoharness/agents/builtin.py) — built-in adversarial `Verification` agent, direct tool access, mandatory checks and `PASS / FAIL / PARTIAL` judgment contract.
- [`docs/guides/multi-agent.md`](https://github.com/aiming-lab/AutoHarness/blob/3561e468f9ca9f9bf282512e695bd32e4e90fef4/docs/guides/multi-agent.md) — supported post-implementation Verification-agent pattern and coordinator composition example.
- [`autoharness/core/verification.py`](https://github.com/aiming-lab/AutoHarness/blob/3561e468f9ca9f9bf282512e695bd32e4e90fef4/autoharness/core/verification.py) — complementary verification of claimed results against actual tool-call/result evidence.
- [Upstream default branch](https://github.com/aiming-lab/AutoHarness/commit/3561e468f9ca9f9bf282512e695bd32e4e90fef4) — still exactly the accepted review ref at re-review time.

## S1 — Operations

- State: A
- Function: autonomously interpret a user task and produce an operational result through iterative model/tool execution.
- Disturbance / variety regulated: heterogeneous task intent, workspace state, tool results/errors, context limits and project-specific implementation uncertainty.
- Decisive decision or feedback right: decide the next model-driven action/tool use and when the requested operational task has been completed.
- Decision owner: the model-driven `AgentLoop` in the standard distribution.
- Supporting / enforcement mechanisms: tool registry/execution, context management, governance pipeline, risk/permission checks, hooks, turn governor, audit logging and optional parent constitution.
- Closure path: task → model decision → governed tool action → observed result → later model decision → returned task outcome.
- Boundary reachability: `AgentLoop` is a directly documented/installable first-party entry point; no repository-development actor is required to expose its operating discretion.
- Why this is / is not agent-owned: deterministic governance can permit/block/enforce actions, but the model-driven loop owns the substantive task/action decisions inside those constraints.
- Evidence: `autoharness/agent_loop.py`; `README.md`; `autoharness/core/pipeline.py`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is external-provider execution and constitutions/tools are parent-configured, but the shipped runtime still exposes autonomous S1 decision/action closure.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes disturbance-specific coordination among distinct S1 units at this recursion.
- Disturbance / variety regulated: no qualifying inter-S1 interference/conflict/oscillation is established by the reviewed standard distribution.
- Decisive decision or feedback right: no S2-specific coordination decision right is established.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: `TeamMailbox`, message/broadcast transport, shutdown request/response, plan-approval response, team config/status, fork/background execution and coordinator delegation.
- Closure path: messages can affect a receiving agent, but no first-party path ties them to a concrete inter-S1 disturbance, a response selected to attenuate that disturbance, and feedback of the coordination result into later S1 behaviour.
- Why this is / is not agent-owned: swarm members may communicate autonomously, but communication/lifecycle protocol alone is below the Profile 0.2.4 S2 functional threshold; ownership classification therefore does not begin.
- Evidence: `autoharness/agents/swarm.py`; `docs/concepts/agents.md`; `docs/guides/multi-agent.md`.
- Basis: current-contract same-ref correction.
- Confidence: high.
- Caveats: downstream applications can use the mailbox to implement genuine conflict regulation; that is a separate composed system unless a first-party S2-specific relation is supplied and reachable here.
- Distinct S1 units: swarm/fork/background workers can be distinct operational agents.
- Inter-S1 disturbance: not established beyond hypothetical disagreement, overlap or lifecycle coordination.
- Attenuating coordination relation: not established; mailbox and handshake primitives are generic transport/lifecycle mechanisms.
- Feedback into subsequent S1 behaviour: generic messages can change later behaviour, but no evidence ties that change to resolution of a qualifying inter-S1 disturbance.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not; the credited evidence is communication, lifecycle and delegation infrastructure.

### Absence scope

- Surfaces inspected: swarm mailbox implementation, team protocol types/status, fork/background modes, coordinator mode, multi-agent guide, role/governance configuration and standard runtime docs.
- Plausible first-party paths checked: plan-approval handshake as conflict resolution; shutdown handshake as oscillation attenuation; coordinator delegation as S2; shared mailbox as mutual adjustment; role-specific governance as collision control.
- Why no material first-party path remains: none establishes the required concrete disturbance → S2-specific attenuation relation → returned change in subsequent S1 behaviour. Profile 0.2.4 explicitly excludes generic mailbox/routing/delegation evidence from S2 by itself.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established over a portfolio of S1 resources, commitments, priorities or constraints.
- Disturbance / variety regulated: not established as S3 at this recursion.
- Decisive decision or feedback right: not established for whole-system current regulation.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: coordinator-mode dispatch, turn governor, budgets/permissions, model routing, team member status and deterministic governance controls.
- Closure path: not applicable as S3.
- Why this is / is not agent-owned: a coordinator can decompose/delegate one task and deterministic controls can enforce preselected limits, but the reviewed evidence does not establish whole-system current visibility plus discretionary authority over shared resources/commitments/priorities on behalf of the organization as a whole.
- Evidence: `docs/concepts/agents.md`; `docs/guides/multi-agent.md`; `autoharness/core/pipeline.py`.
- Basis: structural absence review.
- Confidence: high.
- Caveats: manager/coordinator naming and hard enforcement are not S3 ownership shortcuts.

### Absence scope

- Surfaces inspected: coordinator mode, team status/configuration, turn governor, risk/permissions, pipeline controls, model routing and documented multi-agent workflows.
- Plausible first-party paths checked: coordinator as S3 manager; turn/budget governance as S3 resource control; model router as S3 allocator; team status as whole-system current view.
- Why no material first-party path remains: these mechanisms delegate work or enforce static/local constraints without a reconstructed whole-system current-control decision loop over the operating organization.

## S3* — Complementary audit

- State: C
- Claim being audited: the producing agent's claim that the requested implementation/work is complete and correctly verified.
- Ordinary reporting path: the producing `AgentLoop` returns its own task result and ordinary tool observations to the caller.
- Complementary access path: the separately invoked built-in Verification agent directly runs build/tests/lint/type checks and adversarial workspace probes; `VerificationEngine` can independently compare claimed results with recorded tool-call/result evidence.
- Independence boundary: the verifier is a distinct first-party agent role/evaluation path with its own prompt and direct workspace evidence, rather than merely trusting the producer's completion report; forked history can be shared, so independence is complementary-evidence rather than complete informational isolation.
- Who acts on findings: the embedding application/coordinator receives `PASS`/`FAIL`/`PARTIAL` findings and must compose corrective execution and re-verification, which is why the published ownership remains constructor `C`.
- Function: challenge an operational completion/quality claim using materially different direct evidence from the project/workspace rather than relying on the producing agent's ordinary report.
- Disturbance / variety regulated: false completion, verification avoidance, superficially passing work, missed edge cases, unrun tests/build/lint/type checks and claims inconsistent with actual tool-result evidence.
- Decisive decision or feedback right: produce an audit judgment such as `PASS`, `FAIL`, or `PARTIAL` from direct build/test/lint/type-check/adversarial observations; the deterministic verification surface can likewise flag claim/evidence mismatch from audit history.
- Decision owner: constructor path. AutoHarness supplies a specialized autonomous Verification-agent definition and explicit verification APIs, while the embedding developer/application still decides when that actor is invoked and must compose its findings into corrective authority/closure.
- Supporting / enforcement mechanisms: fork/background execution, direct Read/Grep/Glob/Bash access, audit records, `VerificationEngine`, deterministic verdict/evidence structures and parent permissions.
- Closure path: producing-agent result → separately invoked Verification agent or verification engine obtains complementary evidence → audit verdict/findings return to the caller; FAIL/PARTIAL → corrective execution → re-verification must still be composed downstream.
- Boundary reachability: the `Verification` profile, `get_builtin_agent("verification")`, verification engine and documented post-implementation pattern are shipped in the standard package; the path does not depend on repository CI or maintainer review.
- Why this is / is not agent-owned: the built-in verifier can autonomously gather and judge complementary evidence, but no standard out-of-box loop gives it closed corrective authority over the producer after a failed audit. That missing composition keeps the published state at `C`, not `A`.
- Evidence: `autoharness/agents/builtin.py`; `docs/guides/multi-agent.md`; `autoharness/core/verification.py`; `autoharness/core/pipeline.py` `verify_session()`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: forked verification may inherit parent conversational history, so independence is role/evidence based rather than complete informational isolation. Its fresh direct workspace checks materially differ from ordinary self-report, but the caller still owns the final corrective composition.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective intelligence loop develops organizational adaptation options and returns them into current capability.
- Disturbance / variety regulated: not established as S4.
- Decisive decision or feedback right: not established for future-oriented adaptation.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: model routing, context management, diagnostics, hooks, session trust and configurable agents can alter current execution but do not establish future/environment modeling.
- Closure path: not applicable as S4.
- Why this is / is not agent-owned: current-task planning, runtime diagnostics and configurable extension are not evidence of an outside-and-then adaptation conversation with present S3 capability.
- Evidence: `AgentLoop`, model routing, pipeline and multi-agent configuration surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: an AutoHarness application could build research/self-improvement agents on top of these primitives; that downstream adaptation is not inherited by the generic distribution.

### Absence scope

- Surfaces inspected: model routing, context/session mechanisms, observability/audit, hooks, multi-agent roles, extension/configuration surfaces and current-task planning.
- Plausible first-party paths checked: model routing as adaptation; verification findings as learning; audit/session history as intelligence; dynamic agent choice; custom agent definitions as future-oriented adaptation.
- Why no material first-party path remains: these surfaces regulate current execution or expose extension points but do not model external/future distinctions, develop adaptation options and return them into current organizational capability.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy closure is established at the AutoHarness application recursion.
- Disturbance / variety regulated: not established as an identity/ultimate-policy dispute or adaptation/current-control tension requiring S5 closure.
- Decisive decision or feedback right: constitutions, risk thresholds, permissions, hooks and agent-role definitions are authored/configured by the parent developer/operator rather than decided through a shipped S5 loop.
- Decision owner: application developer/operator outside the autonomous assessed runtime for these policy choices.
- Supporting / enforcement mechanisms: YAML constitution, permission/risk engines, hook profiles, trust state and deterministic enforcement.
- Closure path: parent configuration is loaded into subsequent operation, but no identity/ultimate-policy matter is raised, adjudicated by legitimate S5 authority through a first-party runtime path, and returned as an authoritative policy decision.
- Why this is / is not agent-owned: the agent operates under policy; it does not own ultimate authority to redefine the organization's identity or policy at this recursion.
- Evidence: `autoharness/core/pipeline.py`; constitution/permission configuration docs; built-in agent definitions.
- Basis: structural absence review.
- Confidence: high.
- Caveats: parent authors plainly control configuration, but static policy text or ordinary tool approval does not establish published `P` without a complete identity/policy decision loop.

### Absence scope

- Surfaces inspected: constitution loading, permission/risk policy, hooks, trust/approval handling, built-in role definitions, coordinator/swarm configuration and operator-facing configuration docs.
- Plausible first-party paths checked: YAML constitution as S5; permission approval as S5 escalation; coordinator as executive policy authority; operator configuration as parent S5.
- Why no material first-party path remains: these are pre-authored constraints or operational approvals, not an identity/ultimate-policy issue → legitimate authority → authoritative decision → returned subsequent-operation loop.

## Distributed OSS parent arrangement

Repository contributor/maintainer governance was not credited as part of the shipped AutoHarness runtime. No organization-level distributed parent S3/S4/S5 loop is inferred from open-source contribution activity.

## Self-hosted and non-human modes

Self-hosting exposes strong parent configuration of tools, permissions and constitutions, but no inspected mode closes an additional parent-owned S3/S4/S5 function under the publication rules. Parent-mode notation is therefore absent rather than inferred from configuration power alone.

## Recursion

Forked, background, swarm and coordinator workers provide operational composition. The reviewed repository does not establish that each child carries the complete metasystem required for its own viable recursion, so nesting/spawning is not counted as recursive VSM closure.

## Variety and escalation

Governance attenuates operational variety through risk classification, permissions, hooks, turn limits and output/audit controls. Multi-agent modes amplify operational response variety by adding specialized workers. Verification adds complementary observational variety through direct build/test/lint/type-check/adversarial evidence. Human `ask` decisions are operational permission choices, not automatically S3/S5 escalation.

## Evidence gaps

- No accepted-revision evidence ties mailbox, shutdown or plan-approval messages to a concrete inter-S1 disturbance with a disturbance-specific attenuation-and-feedback loop.
- The Verification-agent constructor is explicit, but the standard distribution does not close failed audit findings back into corrective work and re-verification without downstream composition; this is why S3* remains `C` rather than `A`.
- No whole-system S3 regulator, outside-and-then S4 adaptation loop, or runtime S5 identity/ultimate-policy closure was established at this boundary.
- Upstream default `main` is unchanged from the accepted review ref, so this correction is semantic/current-contract rather than evidence repinning.
