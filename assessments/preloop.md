---
harness_id: preloop
project_name: Preloop
repository: https://github.com/preloop/preloop
review_ref: 06d53f902d9a8712ea3345ae0bee9b0b8292f917
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Preloop

## Review boundary

- System in focus: one self-hosted Preloop control-plane installation at pinned revision `06d53f902d9a8712ea3345ae0bee9b0b8292f917`, including the MCP firewall, model gateway, policy/approval services, managed-agent and runtime-session inventory, flow scheduler/execution state, private-runner protocol, operator-note and kill-switch paths, evidence/publication controls, and shipped flow presets.
- Purpose and identity: govern external AI agents and their model/tool access, make their current operation attributable and controllable, and run durable event-driven agent workflows under policy, budget, approval, verification and recovery constraints.
- Relevant environment: human operators and approvers; governed Claude Code, Codex, Cursor, Gemini, Hermes, OpenCode, OpenClaw, Pi/DeepSeek Harness and other agent runtimes; GitHub/GitLab/Jira and webhooks; model providers; MCP servers/tools; repositories and CI systems; private runners; and external provider pricing information.
- Standard-distribution boundary: the first-party Preloop self-hosted service, CLI/runtime adapters, public APIs, scheduler/workers, built-in tools and shipped presets documented at the frozen revision. External agent/model reasoning loops remain separate operational actors. GitHub/GitLab/Jira, CI providers, model providers and downstream repositories are environmental systems rather than first-party organizational owners.
- Credited operating / distribution surfaces: `README.md`; operator-note and account-kill-switch guides; flow delegation; Pull Request Reviewer and Automated Issue Implementation presets; durable implementation feedback; model-price refresh and weekly review preset; first-party gateway/firewall/policy/session/flow/runner implementation reached by those supported modes.
- Adjacent first-party surfaces excluded from ownership: Preloop repository CI and maintainer review, contributor/release governance, development-only tests, and upstream approval/merge governance for changes to the Preloop repository. Those surfaces may corroborate behavior but do not donate S-functions to an installed control plane unless a shipped runtime path explicitly reaches them.
- First-party operating / deployment modes considered: self-hosted Docker/Helm control plane; governed local or remote agent sessions; event/CI-triggered flows on hosted or private runners; flow delegation; opt-in agent-to-agent notes; human operator notes and emergency halt/recovery; automated issue implementation with durable review/CI feedback; Pull Request Reviewer; weekly model-price review plus reviewed-price feed.
- Recursion level: the installed Preloop account/control plane is the system-in-focus. Governed agent sessions and flow executions are S1 operational units. Delegation trees are lower-recursion operational organizations inside this installation; their internal parent/child relations are not automatically promoted to installation-wide metasystem functions.
- Reviewed revision: `06d53f902d9a8712ea3345ae0bee9b0b8292f917`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Preloop places a first-party governance plane between external agent runtimes and the tools/models they use. The MCP firewall resolves allow/deny/approval policy, the model gateway enforces attribution and budgets, runtime/session records expose current activity, and flows launch bounded agent executions on standard or private runners. The reasoning loop remains in the governed external agent; Preloop supplies admission, transport, policy, lifecycle, evidence and control.

The runtime also exposes explicit current-control surfaces. Operators can inspect managed agents, session timelines, flow executions, spend and policy state; send notes to a live agent; stop executions; or activate an account kill switch that halts gateway, tools and/or flows. Those decisions are enforced by first-party gateway/tool/worker machinery. Public API/CLI surfaces make the same current-control path composable, but the standard distribution does not package an installation-wide autonomous supervisor that decides when to exercise those interventions.

Two shipped workflow paths matter above ordinary governance. First, the Pull Request Reviewer is a separate model-driven flow that independently reads PR evidence and issues findings; durable implementation feedback accepts only configured trusted reviewer identities, keeps reviewer and implementer conversations separate, and creates a fresh bounded repair execution on the implementation branch. Second, the weekly model-price review examines external provider evidence, prepares a tested pricing change and publication artifact, and leaves the decisive merge/publication step to a human; the reviewed-feed service then imports the approved future/current tariff policy into serving processes without an application deployment.

## Operational model

An operator enrolls an external agent or launches a flow. The governed model actor makes task-local reasoning and tool choices while Preloop mediates model/tool calls, policies, approvals and budgets and records the session. Event-driven flows can start child flows and later resume after children, human approvals, review feedback or CI feedback. Durable execution state, branch bindings, checkpoints and recovery mechanics preserve continuity without transferring the external model's internal reasoning to Preloop.

At installation recursion, current regulation is intentionally open to operator or downstream-controller ownership rather than assigned to one resident autonomous manager. Machine-facing APIs expose state and interventions; the operator closes the normal parent-governed mode. Lower-recursion parent agents can inspect and steer their own descendants through `run_flow`, `get_execution` and opt-in `send_note`, but that does not by itself establish installation-wide autonomous S3.

## S1 — Operations

- State: A
- Function: perform bounded coding, review, security, evidence-collection and other agent work against an admitted objective through a governed external runtime.
- Disturbance / variety regulated: heterogeneous tracker events and user objectives, repository/environment state, tool/model feedback, failures, review/CI feedback and task-local uncertainty.
- Decisive decision or feedback right: choose the substantive reasoning path, tool calls and task actions within the objective and Preloop policy/budget envelope.
- Decision owner: the autonomous external model/agent actor launched or governed by Preloop.
- Supporting / enforcement mechanisms: MCP firewall, model gateway, managed credentials, flow execution/runner lifecycle, tool allowlists, budgets, approvals, workspace/checkpoint recovery, runtime plugins and session observability.
- Closure path: objective/event is admitted → Preloop starts or governs an agent runtime → the model chooses actions/tools → Preloop mediates calls and returns environment results → the model continues until a bounded result/commit/review/evidence outcome is produced.
- Boundary reachability: the frozen README documents onboarding existing agents and launching event/CI-triggered flows through the self-hosted service; supported runtime adapters and private runners reach those external actors directly without relying on repository-development CI.
- Why this is / is not agent-owned: Preloop decides admission and enforces constraints, but substantive task-local reasoning and action selection belong to the external model actor.
- Evidence: [`README.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/README.md); [`docs/guide/flows/automated-issue-implementation.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/flows/automated-issue-implementation.md); [`docs/guide/flows/flow-delegation.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/flows/flow-delegation.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no internal VSM function of Claude Code, Codex, Cursor or another governed runtime is inherited merely because Preloop launches or mediates it.

## S2 — Coordination

- State: —
- Function: no installation-level S2 mutual-adjustment function is established from the reviewed standard distribution.
- Disturbance / variety regulated: Preloop can run many sessions/flows and maintains lineage, concurrency, budgets and notes, but the inspected paths do not establish a distinct installation-level oscillation/interference among sibling S1 units together with a first-party relation whose organizational purpose is to attenuate that interaction.
- Decisive decision or feedback right: not established at the installation recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: child-flow lineage, fan-out/depth/tree budgets, runner concurrency, transactional admission locking, `send_note`, waiting/resume and stop propagation structure work and resource use but are not credited as S2 without the required disturbance witness.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no installation-level S2 function was established, so there is no S2 decision right to classify.
- Evidence: [`docs/guide/flows/flow-delegation.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/flows/flow-delegation.md); [`docs/guide/operator-notes.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/operator-notes.md); [`README.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/README.md).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: delegation and communication can be ingredients in a downstream S2 design, but generic routing, shared budgets, sequencing and notes do not manufacture the function on their own.

### Absence scope

- Surfaces inspected: flow delegation, child waiting/resume, tree budgets and admission locking, private-runner concurrency, operator/agent notes, event subscriptions, durable feedback coalescing and session/runtime governance.
- Plausible first-party paths checked: sibling/descendant notes; child-flow fan-out; shared tree-budget admission; concurrent runner executions; webhook deduplication; branch/current-head gates in durable feedback.
- Why no material first-party path remains: the mechanisms prevent duplicate admission, bound resource commitments, transport information or serialize lifecycle events, but no reviewed installation-level path is explicitly tied to attenuation of a concrete interaction-generated disturbance among distinct sibling S1 units. The stronger resource/commitment paths map to current control rather than S2.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate current account-wide agent activity, access and resource commitments using live agent/session/flow/spend/policy state and intervention controls.
- Disturbance / variety regulated: active sessions and executions can consume excessive budget, take a wrong operational direction, continue under unsafe tool/model access, or require an immediate account-wide or targeted stop/steer decision.
- Decisive decision or feedback right: choose current intervention — change policy/budget/access, steer a live agent, stop an execution, or halt/recover gateway/tool/flow scopes — in response to current installation conditions.
- Decision owner: base constructor mode — no resident autonomous installation supervisor is supplied; a downstream controller can be composed over the first-party API/CLI/state/intervention surfaces. Parent mode — the authorized installation/account operator, approver or administrator.
- Supporting / enforcement mechanisms: runtime-session timelines, managed-agent/flow inventory, spend attribution, policy engine, approval service, operator-note delivery, execution stop intents, account kill-switch transactions, gateway/tool enforcement and worker recovery/confirmation.
- Closure path: current account/session/flow/spend/policy state is observed → controller/operator selects a targeted steer/policy/budget/stop or account halt/recovery action → first-party API/CLI writes that decision → gateway/firewall/scheduler/worker paths enforce it → subsequent current operation is steered, admitted, denied, stopped or resumed under the returned decision.
- Boundary reachability: the self-hosted distribution exposes account/session/flow state plus operator-note, policy, approval, budget and kill-switch actions through its console, CLI and HTTP APIs. These are runtime surfaces, not repository-maintainer controls.
- Why this is / is not agent-owned: deterministic policies, budgets and kill-switch propagation enforce current decisions but do not decide when policy should change or an emergency intervention should occur. The standard product deliberately exposes the S3-specific observation/intervention path without assigning that installation-wide discretion to a resident autonomous agent.
- Evidence: [`README.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/README.md); [`docs/guide/operator-notes.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/operator-notes.md); [`docs/guide/account-kill-switch.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/account-kill-switch.md); [`docs/guide/flows/flow-delegation.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/flows/flow-delegation.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: lower-recursion parent agents can autonomously delegate, inspect descendants and send bounded notes, but that does not promote their local management to installation-wide S3 ownership.
- Whole-system current view: the control plane maintains account-scoped managed-agent/session/flow state, live timelines and spend/policy information, while the kill-switch status exposes the current account-wide gateway/tools/flows halt state. The function boundary is the governed account rather than every external system an agent may reach.
- Current-control decision scope: current policy/budget/access changes, live steering notes, execution stop control and account-wide gateway/tools/flows halt/recovery.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous account controller must be composed | current agent/session/flow/spend/policy state indicates an intervention | controller uses first-party API/CLI control surfaces; Preloop enforcement changes subsequent current operation | `README.md`; operator-note and kill-switch guides |
| Parent (`P`) | authorized account operator/admin/approver | observed current risk, spend, wrong direction, approval state or emergency | operator steers/stops/changes policy or activates/deactivates halt scopes; runtime enforcement returns the decision into operation | operator-note and account-kill-switch guides |

## S3* — Complementary audit

- State: A
- Function: independently challenge an implementation/PR claim against fresh code, issue and review evidence and return trusted findings into corrective implementation work.
- Disturbance / variety regulated: an implementer may claim completion while the produced change contains defects, security/quality regressions, unmet requirements or current-head CI/review failures.
- Decisive decision or feedback right: independently judge the produced PR/change, issue review findings or a review action, and thereby supply corrective feedback that can trigger the next bounded repair execution.
- Decision owner: the separate autonomous model actor executing the Pull Request Reviewer flow.
- Supporting / enforcement mechanisms: distinct reviewer flow/conversation, bounded PR diff and referenced-issue reads, stateful findings, trusted reviewer actor IDs, provider/current-head gates, runner-controlled verification evidence, feedback debounce/coalescing, branch binding, checkpoints and fresh repair execution budgets/credentials.
- Closure path: implementer publishes or updates a PR → separate reviewer flow reads PR/diff/issue evidence and posts findings/review action → durable feedback authenticates configured reviewer identity and current PR/head → feedback is reserved into a fresh implementation repair execution → implementer resumes the bound branch/conversation and addresses findings → later current-head review/CI state is reconciled again.
- Boundary reachability: both Pull Request Reviewer and Automated Issue Implementation/durable-feedback modes are shipped first-party presets and runtime services; the reviewer/repair connection is available through normal flow configuration rather than repository-development CI for Preloop itself.
- Why this is / is not agent-owned: the critical review judgment is produced by a separate model-driven reviewer conversation, not by the implementation agent or a deterministic gate. Provider and runner checks constrain trusted evidence but do not replace reviewer judgment.
- Evidence: [`docs/guide/flows/pull-request-review.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/flows/pull-request-review.md); [`backend/presets/002-pull-request-reviewer.yaml`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/backend/presets/002-pull-request-reviewer.yaml); [`docs/guide/flows/durable-implementation-feedback.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/flows/durable-implementation-feedback.md); [`docs/guide/flows/automated-issue-implementation.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/flows/automated-issue-implementation.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: human approval by itself is not credited as S3*. The positive claim depends on the distinct autonomous reviewer plus authenticated corrective return; deterministic trusted verification is supporting complementary evidence rather than the sole owner.
- Claim being audited: the implementation agent's produced PR/change and its implicit or explicit claim that the requested change is correct and ready under the relevant review criteria.
- Ordinary reporting path: the implementer writes its result/commit and Preloop publishes/binds the PR and implementation execution state.
- Complementary access path: the reviewer independently fetches the current PR metadata/diff/comments and referenced issue and may inspect bounded project context; runner/provider gates independently read current-head checks and review state.
- Independence boundary: reviewer and implementer are separate flows/conversations; durable feedback distinguishes `trusted_reviewer_ids` from `implementer_actor_ids`, ignores untrusted/copied review markers, and creates each repair as a new execution with fresh credentials/budgets.
- Who acts on findings: the implementation thread receives trusted review/CI feedback in the next repair execution and the autonomous implementer acts on it; unresolved blockers can instead remain visible for human action.

## S4 — Outside-and-then adaptation

- State: P
- Function: sense external model-provider tariff changes, generate a verified future pricing-policy adaptation and return an approved reviewed feed into serving Preloop processes.
- Disturbance / variety regulated: provider models, regional tariffs, cache policies, effective dates and pricing evidence change outside the installation, making existing cost estimates stale or incomplete.
- Decisive decision or feedback right: decide whether the externally evidenced candidate pricing revision becomes an approved publication consumed by the installation.
- Decision owner: the human/operator who reviews and merges/publishes the pricing change; the scheduled review agent prepares and tests the option but does not own final adoption.
- Supporting / enforcement mechanisms: public weekly model-price-review preset, provider/public evidence reads, reviewed catalog and manifest, isolated verification/publication tooling, revision/provenance/expiry validation, allowlists, periodic reviewed-feed polling and atomic runtime price-map replacement.
- Closure path: scheduled review examines external provider pricing evidence → agent prepares catalog/manifest/feed changes and tested PR → human reviews and merges/publishes the revision → configured serving processes poll the reviewed artifact → validated price policy replaces current estimates without application deployment → future model-cost control uses the adapted prices.
- Boundary reachability: the weekly review preset and reviewed-feed consumer are documented first-party distribution surfaces at the frozen revision. The mode requires normal operator configuration and a human publication decision, not Preloop repository maintainer machinery as an implicit hidden owner.
- Why this is / is not agent-owned: the autonomous review agent performs sensing and option generation, but the documented contract explicitly says human PR merge controls feed publication. The decisive adaptation right therefore remains parent-governed.
- Evidence: [`docs/guide/model-price-refresh.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/model-price-refresh.md); [`README.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic saved-session history, search and replay are not S4. The positive mapping relies specifically on external tariff sensing plus a documented adaptation option and return into runtime pricing.
- External distinction: official/public model-provider pricing evidence and regional/cache tariff information are outside Preloop and can change independently of the installation.
- Future / prospective distinction: the weekly scheduled review prepares new or future-effective pricing revisions before subsequent governed requests are costed, including explicitly future-dated tariff policies where supported.
- Adaptation option generated: the review flow prepares catalog/manifest/generated-feed changes in a tested PR with provenance, effective dates and unresolved-evidence reporting.
- Path back into current capability / S3: after parent approval/publication, the reviewed-feed service polls the artifact and atomically replaces serving-process price maps; subsequent current budget/cost regulation uses the updated estimates.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy closure is established for the installed Preloop organization.
- Disturbance / variety regulated: policy-as-code, roles, approvals, budgets, kill switches, flow configuration and security controls regulate what current/adaptive work may do, but the inspected distribution does not identify an identity/ultimate-policy issue resolved by an ultimate authority and returned as a governing organizational decision.
- Decisive decision or feedback right: not established as S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: account roles, YAML/CEL tool policy, approvals, model/tool allowlists, budget configuration, kill switch, flow configuration and human merge gates are operational governance mechanisms rather than demonstrated S5 closure.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no S5 function was established to classify; the presence of parent authority over operational controls does not by itself create identity/ultimate-policy governance.
- Evidence: [`README.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/README.md); [`docs/guide/account-kill-switch.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/account-kill-switch.md); [`docs/guide/flows/durable-implementation-feedback.md`](https://github.com/preloop/preloop/blob/06d53f902d9a8712ea3345ae0bee9b0b8292f917/docs/guide/flows/durable-implementation-feedback.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: human-controlled policy and emergency authority are materially important governance, but S5 requires a distinct identity/ultimate-policy function rather than generic high-privilege administration.

### Absence scope

- Surfaces inspected: YAML/CEL policy, roles/approvals, account kill switch and staged recovery, model/tool allowlists, flow configuration, delegation limits, operator notes, durable feedback trust settings, reviewed-price publication and account authority surfaces.
- Plausible first-party paths checked: owner/admin emergency authority; policy-as-code; approval/quorum semantics available in the OSS edition; model/harness routing; flow identity/configuration; external pricing adaptation; reviewer trust and publication decisions.
- Why no material first-party path remains: these paths govern operational permission, resource use, safety, review or adaptation, but none establishes an explicit organizational identity question, ultimate authority for that identity/policy issue, and a returned governing decision that reconstitutes operation under S5.
