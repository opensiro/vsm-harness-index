---
harness_id: openshell
project_name: OpenShell
repository: https://github.com/NVIDIA/OpenShell
review_ref: 1358941b818d4126a7374aaf5216d87fc960e122
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenShell

## Review boundary

- System in focus: the first-party `NVIDIA/OpenShell` standard distribution at pinned revision `1358941b818d4126a7374aaf5216d87fc960e122`, including the CLI/SDK/TUI management surfaces, gateway, supervisor, sandbox lifecycle, policy proxy and prover, policy persistence/delivery, identity and credential boundaries, and agent-driven policy proposal/review machinery.
- Purpose and identity: provide a safe/private runtime and control boundary for autonomous AI agents by isolating agent processes, constraining filesystem/process/network access, binding credentials to approved endpoints, managing sandboxes, and validating/reviewing policy changes.
- Relevant environment: externally supplied autonomous agent programs, model providers, tools/APIs, users/developers/operators, Docker/Podman/Kubernetes/VM runtimes, secret stores, identity systems, and external infrastructure drivers.
- Standard-distribution boundary: OpenShell-owned gateway/supervisor/policy/runtime code and shipped management interfaces are inside. The goal-directed autonomous agent program launched as the restricted child process, including OpenCode in the documented first-agent walkthrough, remains outside unless OpenShell itself supplies the relevant objective→reasoning→action loop.
- Credited operating / distribution surfaces: `README.md`; `architecture/README.md`; `architecture/security-policy.md`; accepted RFC `rfc/0002-agent-driven-policy-management/README.md`; standard gateway/supervisor/sandbox/policy/prover distribution described by those documents.
- Adjacent first-party surfaces excluded from ownership: contributor/dogfood agent workflows, `AGENTS.md`, development automation, tests/examples and benchmark/CI surfaces. They may corroborate architecture but do not donate operational ownership to the distributed OpenShell runtime.
- First-party operating / deployment modes considered: local gateway plus sandbox; Kubernetes/other supported compute-driver deployments; gateway-supervisor control sessions; dynamic network-policy updates; policy-advisor / agent-authored proposal mode when enabled; manual review and future trusted-external-approver path described by the accepted RFC.
- Recursion level: OpenShell itself as the reusable runtime/control system around autonomous agent payloads. A composed organization consisting of OpenShell plus a specific autonomous agent implementation is a wider system and would require its own assessment boundary.
- Reviewed revision: `1358941b818d4126a7374aaf5216d87fc960e122`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

OpenShell explicitly positions itself as a runtime for autonomous agents rather than as the agent reasoning loop itself. The README says each agent runs in an isolated sandbox, but the default sandbox image contains no agent; the documented first-agent path installs/runs an external agent. The architecture reference makes the split sharper: the gateway is the authenticated control plane and owns durable sandbox/policy/settings/provider/session/authorization state, while the supervisor runs inside the sandbox, prepares isolation, starts the proxy, and launches the **agent as a restricted child process**.

The security-policy architecture supplies substantial deterministic control. Filesystem and process restrictions are applied through sandbox/kernel mechanisms; network traffic is forced through the policy proxy; provider credentials are injected only on approved endpoints; explicit denies and hardening checks dominate; invalid policy generations fail closed or retain the last valid generation depending on configured mode. The gateway stores and distributes policy, while the local enforcement boundary performs per-request decisions.

OpenShell also exposes a sophisticated policy adaptation workflow. The accepted agent-driven-policy RFC lets an in-sandbox agent inspect effective policy and denials, draft a narrow policy change and submit it to the gateway. The same RFC explicitly makes unilateral self-approval a non-goal. Gateway-side validation, the prover, and a developer/external-approver boundary decide whether the proposal is approved; the approved policy is then hot-reloaded into the sandbox. This is important organizational machinery, but the agent authoring the proposal is still the externally supplied sandbox agent rather than a first-party OpenShell reasoning actor.

Counterfactual owner test: remove the externally supplied autonomous agent program while leaving the OpenShell gateway, supervisor, sandbox lifecycle, policy engine/proxy, prover, credential handling, proposal persistence/review and management interfaces intact. OpenShell can still create/manage sandboxes, evaluate policy, enforce permissions, record denials, validate proposed changes and apply externally authorized configuration. It cannot receive a substantive user objective, reason over that objective, choose task-directed model/tool actions and iteratively use their results to accomplish the task. The operational S1 loop therefore closes in the payload agent, not in OpenShell.

The proposed terminal result is `excluded-no-agentic-vsm`. OpenShell is a strong governance/enforcement substrate for an agent organization, but Methodology 0.3.6 does not allow adjacent-agent autonomy to be inherited by the control substrate. The body preserves the useful control findings rather than promoting enforcement mechanisms into positive S3/S3*/S5 states without first-party S1.

Primary evidence:

- [`README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/README.md) — product boundary, sandbox model, kernel/policy enforcement, formal verification and the fact that the default sandbox contains no agent and the walkthrough runs an external agent.
- [`architecture/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/README.md) — gateway/control-plane ownership, supervisor boundary, external infrastructure drivers, sandbox semantics and restricted child-agent process.
- [`architecture/security-policy.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/security-policy.md) — deterministic enforcement, policy loading/updates, credential and network boundaries, fail-closed behavior, and gateway-versus-local enforcement split.
- [`rfc/0002-agent-driven-policy-management/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/rfc/0002-agent-driven-policy-management/README.md) — accepted agent-authored proposal workflow, gateway validation/review, human/external approval boundary and explicit non-goal of agent self-approval.

## Operational model

The substantive operational unit in an OpenShell deployment is the sandboxed autonomous agent payload. OpenShell creates and supervises the sandbox and constrains what that payload may access, but the payload owns task interpretation and task-directed action selection. Gateway/supervisor/prover/proxy components are first-party control and enforcement mechanisms around that operation.

The accepted policy-management RFC adds a feedback loop from denied agent activity to policy proposals and approved policy changes. The proposal author can be the sandboxed agent or a deterministic mapper; approval/activation remains outside that proposing agent. This creates a useful constructor for a wider agent organization, but it does not create a first-party OpenShell S1 or transfer the payload agent's higher VSM functions into the runtime.

## S1 — Operations

- State: —
- Function: no first-party autonomous goal-directed operational loop is established inside the OpenShell standard distribution.
- Disturbance / variety regulated: OpenShell regulates execution risk, access, credentials, sandbox lifecycle and policy state; substantive task uncertainty and choice of task-directed actions are handled by the externally supplied agent payload.
- Decisive decision or feedback right: interpret a user/task objective, choose the next substantive model/tool/action step, observe its result and decide what task-directed step follows.
- Decision owner: the external agent program running as the restricted child process.
- Supporting / enforcement mechanisms: gateway, supervisor, sandbox lifecycle, policy proxy/OPA, Landlock/process restrictions, credential injection, provider bindings, policy prover, relay/session infrastructure and management surfaces.
- Closure path: external agent receives objective → chooses/attempts action → OpenShell allows/denies/constrains execution → result/denial returns to the external agent → external agent chooses the next task-directed action.
- Boundary reachability: removing the external agent leaves OpenShell management/enforcement functional but leaves no first-party component that owns the substantive objective→reasoning→action loop.
- Why this is / is not agent-owned: OpenShell governs an agent process but does not itself supply the autonomous actor whose task-directed choices constitute the operation.
- Evidence: [`README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/README.md); [`architecture/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a separately assessed composed system that fixes a particular autonomous agent plus OpenShell inside one organization may establish S1; this repository-relative OpenShell boundary does not inherit it.

### Absence scope

- Surfaces inspected: product README, canonical architecture, gateway/supervisor/sandbox split, policy architecture and accepted agent-driven policy-management design.
- Plausible first-party paths checked: supervisor as agent runtime; gateway as autonomous controller; policy advisor as task agent; mechanistic mapper as operational agent; contributor/dogfood agents as shipped runtime ownership.
- Why no material first-party path remains: the supervisor launches a separate agent child; the README's default sandbox has no agent; policy machinery reacts to/controls agent activity but does not own general task reasoning and action selection.

## S2 — Coordination

- State: —
- Function: no first-party S2 coordination function over an internal population of autonomous S1 units is established at the declared OpenShell boundary.
- Disturbance / variety regulated: OpenShell can manage fleets/sandboxes and mediate policy/identity/network boundaries, but the reviewed evidence does not establish a first-party semantic coordination loop that attenuates concrete interference among first-party operational agents.
- Decisive decision or feedback right: decide how distinct S1 units alter behaviour in response to inter-S1 conflict/oscillation/interference.
- Decision owner: not established inside OpenShell; payload agents and/or an external orchestrator own substantive multi-agent coordination.
- Supporting / enforcement mechanisms: sandbox identities, gateway sessions, policy distribution, sandbox-to-sandbox authorization, relays and fleet management surfaces.
- Closure path: OpenShell can authorize/deny communication and distribute state, but no first-party S2-specific decision path closes from observed inter-agent disturbance back into subsequent autonomous S1 behaviour.
- Boundary reachability: no internal first-party S1 population exists after applying the declared payload-agent boundary.
- Why this is / is not agent-owned: fleet terminology, shared control-plane state and communication/security mechanisms do not satisfy the Methodology's S2 interference-and-feedback witness by themselves.
- Evidence: [`architecture/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/README.md).
- Basis: structural negative search.
- Confidence: high.
- Caveats: OpenShell can be infrastructure inside a wider multi-agent organization whose orchestrator closes S2; that wider organization is outside this assessment.

### Absence scope

- Surfaces inspected: gateway/sandbox relation, relay coordination, sandbox identity/authorization, fleet/sandbox lifecycle and policy distribution.
- Plausible first-party paths checked: relay coordination as S2; sandbox identity as S2; shared gateway state as S2; fleet lifecycle as S2.
- Why no material first-party path remains: these mechanisms regulate transport/security/lifecycle and do not establish a first-party feedback relation that resolves evidenced behavioural interference among internal autonomous operations.

## S3 — Inside-and-now control

- State: —
- Function: OpenShell supplies strong current enforcement and policy administration, but no first-party autonomous whole-system S3 owner exists for an internal operational organization at this boundary.
- Disturbance / variety regulated: unsafe access, invalid policy generations, credential exposure, process/network violations, sandbox lifecycle state and denied capabilities.
- Decisive decision or feedback right: choose current operational priorities/resources/commitments/interventions for the whole viable organization, rather than merely enforce a configured permission boundary.
- Decision owner: policy authors/operators/approvers and any external agent/orchestrator; OpenShell runtime components enforce and persist those choices.
- Supporting / enforcement mechanisms: gateway authorization/state, policy engine/proxy, sandbox supervisor, policy validation, fail-closed/quarantine behavior, compute drivers and provider/credential controls.
- Closure path: operator/configuration or external governance determines policy/current constraints → OpenShell validates/distributes/enforces them → external payload agent operation changes accordingly.
- Boundary reachability: all cited enforcement is reachable in the supported distribution, but the discretionary whole-system current-control owner remains external to OpenShell's first-party agent boundary.
- Why this is / is not agent-owned: hard policy and lifecycle enforcement is not S3 ownership under Methodology 0.3.6; the mechanism can enforce a decision without owning the organizational decision right.
- Evidence: [`architecture/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/README.md); [`architecture/security-policy.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/security-policy.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a wider deployment may use OpenShell as the enforcement substrate for S3 decisions made elsewhere; that does not transfer S3 ownership into OpenShell.

### Absence scope

- Surfaces inspected: gateway control-plane semantics, sandbox lifecycle/reconciliation, policy validation/enforcement, runtime failure modes, provider/credential configuration and authorization.
- Plausible first-party paths checked: gateway as S3 manager; supervisor as S3 controller; policy proxy as S3; fail-closed runtime as S3; compute reconciliation as S3.
- Why no material first-party path remains: inspected paths implement configured/deterministic safety and lifecycle controls around externally owned operations and do not supply the required autonomous whole-system current-control discretion.

## S3* — Complementary audit

- State: —
- Function: the policy prover and validation machinery independently analyze policy risk relative to enforcement rules, but no complementary audit of a first-party S1 operation closes at the assessed OpenShell boundary.
- Disturbance / variety regulated: proposed policy may accidentally broaden access, create credentialed reach, enable unsafe methods or bypass intended L7 restrictions.
- Decisive decision or feedback right: independently challenge an operational claim/state and return findings that alter subsequent first-party operation.
- Decision owner: deterministic prover/validator generates findings; approval authority is human/external; the substantive operation being constrained belongs to the external payload agent.
- Supporting / enforcement mechanisms: formal policy prover, gateway validation, proposal findings, audit/history state and fail-closed activation gates.
- Closure path: proposal → prover/validation findings → external reviewer/approval decision → policy activation/rejection → external agent's allowed action set changes. This is policy assurance around adjacent operation, not an internal S3* loop over first-party S1 reality.
- Boundary reachability: prover/validation is shipped and reachable, but the audited operational unit and corrective authority required for an OpenShell-owned S3* organization are outside the first-party S1 boundary.
- Why this is / is not agent-owned: independent technical verification of policy is not sufficient to publish S3* when the system lacks internal S1 and the final organizational corrective loop belongs to external governance.
- Evidence: [`README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/README.md); [`architecture/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/README.md); [`rfc/0002-agent-driven-policy-management/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/rfc/0002-agent-driven-policy-management/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: in a composed agent organization, the prover can be strong evidence for a complementary assurance mechanism; this assessment does not inherit the composed organization's S3* state.

### Absence scope

- Surfaces inspected: policy prover, policy validation, proposal review/approval flow, audit/history and activation gates.
- Plausible first-party paths checked: prover as S3*; gateway validator as S3*; developer inbox/review as S3*; policy audit trail as S3*.
- Why no material first-party path remains: the mechanisms inspect policy/configuration for an external agent and return findings to external authority; they do not independently audit a first-party operational S1 organization owned by OpenShell.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party autonomous outside/future sensing → option generation → persistent capability adaptation loop is established for OpenShell as the system-in-focus.
- Disturbance / variety regulated: changing task/access needs can trigger policy proposals, and future architecture may support broader trusted automation, but those changes are authored by external agents, humans or external control planes.
- Decisive decision or feedback right: interpret external/prospective change, choose an adaptation option and return that choice into present system capability.
- Decision owner: external payload agent for agent-authored proposal content, or human/external trusted approver for policy adaptation authority.
- Supporting / enforcement mechanisms: denial aggregation, mechanistic proposal generation, `policy.local`, proposal persistence, prover/validation, approval inbox and hot reload.
- Closure path: external agent encounters/plans capability need → agent or deterministic mapper proposes policy change → external reviewer/approver decides → OpenShell hot-reloads accepted policy → external agent gains/retains capability.
- Boundary reachability: the proposal and hot-reload machinery is first-party, but the prospective adaptation judgment does not close in a first-party OpenShell autonomous actor.
- Why this is / is not agent-owned: an externally supplied sandbox agent may generate an adaptation proposal, but its autonomy cannot be credited to OpenShell; deterministic deny-to-rule mapping is support rather than general prospective intelligence.
- Evidence: [`rfc/0002-agent-driven-policy-management/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/rfc/0002-agent-driven-policy-management/README.md); [`architecture/security-policy.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/security-policy.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a composed system with a qualifying autonomous planning/adaptation agent and OpenShell policy feedback could establish S4 at that wider recursion.

### Absence scope

- Surfaces inspected: denial-driven policy advisor, agent-authored proposal path, prover/validation, developer inbox/external approver design, hot-reload policy update path.
- Plausible first-party paths checked: mechanistic mapper as S4; policy advisor as S4; agent-authored proposal system as OpenShell-owned S4; roadmap/RFC process as S4.
- Why no material first-party path remains: the only genuinely agentic prospective judgment is performed by the external sandbox agent; first-party OpenShell machinery validates, transports, approves or deterministically derives bounded policy changes.

## S5 — Policy and identity

- State: —
- Function: OpenShell enforces explicit security policy and identity boundaries, but no first-party autonomous identity/ultimate-policy owner closes S5 for an internal viable agent organization.
- Disturbance / variety regulated: what sandboxes/agents are allowed to access, which credentials/providers are attached, which policies are valid, and who may authorize changes.
- Decisive decision or feedback right: define or revise the organization's ultimate identity/policy commitments rather than apply an already authored security policy.
- Decision owner: human/operator/organization or external trusted control plane. The in-sandbox proposing agent is explicitly not allowed to self-approve its own authority expansion.
- Supporting / enforcement mechanisms: authored policy schema, gateway authorization, identity drivers, policy prover, proposal approval workflow, sandbox policy delivery and runtime enforcement.
- Closure path: external legitimate authority defines/approves policy → gateway persists/distributes it → supervisor/proxy enforces it → external agent operation is constrained by the returned policy.
- Boundary reachability: enforcement and proposal review are first-party, but ultimate policy authority is intentionally kept outside the proposing sandbox agent and outside any autonomous OpenShell actor.
- Why this is / is not agent-owned: a security policy artifact is not S5 ownership by itself. The accepted RFC preserves external approval precisely so the governed agent cannot unilaterally redefine its own authority.
- Evidence: [`architecture/security-policy.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/architecture/security-policy.md); [`rfc/0002-agent-driven-policy-management/README.md`](https://github.com/NVIDIA/OpenShell/blob/1358941b818d4126a7374aaf5216d87fc960e122/rfc/0002-agent-driven-policy-management/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external organizational governance can use OpenShell to enforce S5 decisions in a wider system; this does not create an OpenShell-owned autonomous S5 state.

### Absence scope

- Surfaces inspected: authored/effective policy model, gateway authorization and identities, policy proposal validation/review, agent-driven-policy RFC and runtime policy enforcement.
- Plausible first-party paths checked: policy schema as S5; gateway authorization as S5; prover as S5; sandbox agent proposal as S5; auto-apply direction as autonomous S5.
- Why no material first-party path remains: ultimate authority remains with external legitimate reviewers/organizational control, and the accepted design explicitly prevents the governed proposing agent from unilaterally expanding its own authority.

## Recursion

OpenShell can sit inside a larger viable agent organization as its security/runtime substrate. At that wider recursion, a specific autonomous agent or orchestrator may supply S1 and potentially S2-S5 while OpenShell implements part of the enforcement/feedback plumbing. This assessment intentionally stops at the reusable first-party OpenShell distribution and does not inherit the adjacent agent's functions.

## Variety and escalation

OpenShell attenuates substantial execution variety through sandbox isolation, deny-by-default policy, credential binding, policy validation and fail-closed behavior. Denials can escalate into policy proposals; proposals can carry prover findings to an external reviewer; approved changes return to the sandbox as hot-reloaded policy. This is a strong escalation/enforcement chain, but the decisive task and governance ownership remains outside OpenShell's autonomous boundary.

## Evidence gaps

- The reviewed ref contains rapidly evolving agent-policy automation. Future releases may add a first-party trusted autonomous control actor rather than only external-agent proposal authorship/external approval. Such a material boundary change should trigger reassessment.
- A future standard image could ship an OpenShell-owned autonomous agent loop. The current README explicitly says the default sandbox has no agent, so that mode is not credited here.
- The accepted RFC discusses future trusted external auto-apply under organization-defined ceilings. External trusted approvers remain outside the current OpenShell first-party ownership boundary unless they become a shipped integrated actor whose decision rights and closure are materially owned by the standard distribution.
