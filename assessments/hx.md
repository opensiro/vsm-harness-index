---
harness_id: hx
project_name: hx
repository: https://github.com/phantomic12/hx-harness
review_ref: 6afe2291a5bc750903eae1e9266ace8cdeb2eaef
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# hx

## Review boundary

- System in focus: one first-party self-hosted hx daemon deployment at pinned revision `6afe2291a5bc750903eae1e9266ace8cdeb2eaef`, including its durable autonomous chat sessions, shared model/provider router and limits, capability/approval machinery, session/event store, remote-host and sandbox execution, embedded web/API control surface, fan-out/research paths and session-integrity audit endpoint.
- Purpose and identity: drive AI agents against real machines through durable model→tool→feedback sessions while the daemon owns shared execution state, provider capacity, policy enforcement, persistence and operator-facing control surfaces.
- Relevant environment: deployment operator, user requests, local and remote workspaces/hosts, model-provider services and credentials, search/web sources, configured sandboxes, external connector/webhook traffic and the files/commands changed by agent actions.
- Standard-distribution boundary: the shipped `hxd` daemon, `hx-agent` loop, `hx-provider` routing/limiting, `hx-store`, first-party HTTP/embedded-web surfaces, approval/capability paths, host/sandbox machinery, research/fan-out facilities and the shipped Laya decision helper as actually wired at the frozen revision. External model/search providers, operator judgment itself and downstream controllers are environment or parent actors rather than internal autonomous owners.
- Credited operating / distribution surfaces: ordinary and resumed `/v1/chat` sessions; concurrent daemon-managed sessions sharing one live `ModelRouter`; role/pool/provider routing and limits; `/v1/status`, `/v1/pools` and `/v1/providers`; embedded web/API provider management; `/v1/sessions/{id}/audit`; normal capability/approval, host and sandbox execution paths.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests and milestone verification documents; `ROADMAP.md` and `PLAN-LAYA.md` future work; post-ref upstream code not present in the frozen tree; one-shot fan-out children where no durable agent loop is instantiated; documentation/examples except where corroborated by frozen runtime wiring.
- First-party operating / deployment modes considered: normal autonomous chat; resume after interruption; multiple concurrent sessions; role-based model routing under shared credential/pool ceilings; operator use of the embedded web/API status and live provider-management surface; session audit verification; fan-out and research; Laya CLI/decision substrate.
- Recursion level: the assessed organization is one hx daemon deployment. A durable autonomous chat session is an S1 operational unit at this recursion. Multiple sessions can coexist and share deployment-level provider capacity. One-shot fan-out children are provider calls and are not promoted to recursive S1 units. The deployment operator is a legitimate parent for the separately evidenced S3 parent mode.
- Reviewed revision: `6afe2291a5bc750903eae1e9266ace8cdeb2eaef`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

hx is daemon-centred. `hxd` owns state and exposes one HTTP surface used by the CLI, embedded web client and other front ends. A normal chat request resolves a role to a routed model, creates or resumes a durable session, constructs a capability/approval context and runs `hx-agent`'s repeated model→tool→observation loop. Messages and events are persisted as the run proceeds, so interrupted sessions can be repaired and resumed.

At the deployment recursion, independently running chat sessions share one live model router. Role bindings select named pools, while provider credentials and named pools carry shared concurrent/rate/token/spend ceilings. `RouterModel` reserves shared capacity before a provider request, selects a permitted route/credential, reconciles actual usage afterwards and marks failed credentials unhealthy. This is more than generic routing: the implementation explicitly prevents multiple pools/sessions from independently spending the full allowance of one shared credential. The path therefore establishes an S2 function, but the coordination discretion remains deterministic/configured rather than agent-owned. The first-party role/pool/limit primitives expose the S2-specific path for composition, so the publication state is Constructor (`C`).

The daemon also exposes a deployment-wide current-control surface. `/v1/status` combines current pool/role, sandbox, host, session-count, provider and webhook-queue state. `/v1/providers` can add, edit or remove providers while the daemon is running; an accepted change rebuilds the live provider registry, `ModelRouter` and model factory, swaps those structures into the running daemon and persists the configuration. The bundled operator path closes this as parent-governed S3. The same first-party status/mutation API specifically exposes the relevant current-resource decision path to a downstream autonomous controller, but hx does not ship such a controller at the frozen revision, yielding `C(P)` rather than `A(P)`.

For complementary audit, every standard API deployment exposes `/v1/sessions/{id}/audit`. The store maintains a hash/HMAC-capable event chain, and the endpoint separately verifies the stored trail and distinguishes `intact`, `broken` and `unchained`, including the broken sequence and stored/expected digest. That gives a first-party audit-specific channel capable of challenging the ordinary session/event record. hx does not ship an autonomous auditor with independent authority and corrective closure around that evidence, so S3* remains `C`.

Research, browser fallback, provider failover and the Laya decision subsystem were inspected for S4. The research pipeline gathers current task evidence; browser/provider fallback reacts operationally to availability/refusal; and the frozen Laya integration is explicitly a decision substrate/CLI helper rather than a regulator wired into organizational adaptation. None closes an external-and-prospective adaptation conversation back into present capability. Approval policy, capability tokens, roles and configuration similarly constrain operation without supplying identity/ultimate-policy closure for S5.

Primary evidence:

- [`crates/hx-agent/src/agent.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-agent/src/agent.rs) — repeated model→tool→result loop, approvals/capabilities, durable transcript sink and run limits.
- [`crates/hx-server/src/chat.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/chat.rs) — standard daemon wiring for one request/session/run, role routing, durable session state, session isolation and restart repair.
- [`crates/hx-agent/src/model.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-agent/src/model.rs) — production `RouterModel` shared router, pre-call reservation, route/credential choice, settlement and unhealthy-credential handling.
- [`crates/hx-provider/src/router.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-provider/src/router.rs) — shared provider credential pools, named-pool ceilings, role mappings and live router status.
- [`hx.example.yaml`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/hx.example.yaml) — first-party credential/pool limits, roles and the supported configuration surface for shared capacity regulation.
- [`crates/hx-server/src/state.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/state.rs) — deployment status snapshot plus live provider add/edit/remove and registry/router/model-factory replacement.
- [`crates/hx-server/src/routes.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/routes.rs) — standard API reachability for status, providers, sessions/audit, approvals, fan-out and research.
- [`crates/hx-store/src/audit.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-store/src/audit.rs) — event-chain construction/verification and its keyed/unkeyed integrity guarantees.
- [`crates/hx-server/src/fanout.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/fanout.rs) and [`crates/hx-server/src/spawn.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/spawn.rs) — bounded parallel one-shot model children inspected and not treated as recursive S1/S2 merely because they execute concurrently.
- [`crates/hx-search/src/research.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-search/src/research.rs) — task-level external research/fetch pipeline inspected for S4.
- [`crates/hx-decision/src/lib.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-decision/src/lib.rs) and [`docs/laya.md`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/docs/laya.md) — typed Laya decision substrate; frozen documentation explicitly limits current integration to the decision helper/CLI rather than a wired adaptive organizational controller.

## Operational model

Each active hx chat session is a durable autonomous operational cell. Its model chooses substantive actions/tools and revises subsequent behavior from returned observations. At the daemon recursion, sessions share provider credentials/pools and other deployment resources. The shared router deterministically coordinates scarce provider capacity. A deployment operator can inspect aggregate current state and mutate live provider resources for the whole daemon; downstream code can use the same first-party API as an S3 constructor surface. Session event chains supply a separately callable integrity-audit channel. No shipped agent owns S2 coordination, daemon-wide S3 control or S3* audit judgment at this revision.

## S1 — Operations

- State: A
- Function: transform user objectives into effects on local/remote files, commands, research targets and other tool-mediated environments through a repeated model→tool→feedback loop inside each durable chat session.
- Disturbance / variety regulated: changing workspace/host state, tool results and failures, ambiguous task requirements, provider responses, permission outcomes, context/transcript state and user follow-up.
- Decisive decision or feedback right: choose the next substantive model/tool action and revise later actions from returned tool/environment evidence.
- Decision owner: the active session's model actor.
- Supporting / enforcement mechanisms: `AgentLoop`, tool registry, capability tokens, approval policy/queue, role-based provider adapter, sandbox/host execution, durable session/event store, turn/deadline/provider-spend limits.
- Closure path: user prompt enters a durable session → model selects content/tool calls → capability/approval machinery permits/refuses and tools act on the environment → tool result/refusal is appended to the transcript → model receives that changed evidence and chooses the next action → persisted operational state and external environment advance.
- Boundary reachability: `POST /v1/chat` is the standard daemon route and directly constructs/runs `AgentLoop`; the same path is used by first-party clients rather than requiring a downstream harness.
- Why this is / is not agent-owned: removing the model leaves routing, policy and execution machinery but removes the discretionary choice of what substantive action to attempt next and how to respond to observations.
- Evidence: [`crates/hx-agent/src/agent.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-agent/src/agent.rs); [`crates/hx-server/src/chat.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/chat.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: provider inference is external, but the first-party hx runtime owns the persistent loop, action execution, observations and return path.

## S2 — Coordination

- State: C
- Function: attenuate contention among concurrent autonomous chat-session S1 units for shared provider credentials/pools so several sessions cannot independently consume the same deployment quota as if they were alone.
- Disturbance / variety regulated: concurrent session model calls competing for the same credential's RPM/TPM/concurrency/spend allowance and for pool-wide capacity, including dead/unhealthy credentials and oversubscribed routes.
- Decisive decision or feedback right: decide whether a competing model call receives a shared-capacity lease/route now, is redirected to another available route, or is refused because the shared limits are exhausted, then reconcile actual usage into the state seen by later calls.
- Decision owner: no autonomous S2 actor is supplied in the standard distribution; deployment-authored limits/routing policy are executed by the deterministic shared `ModelRouter`/limiters. A downstream composition would still need to supply autonomous coordination discretion to move this path from `C` to `A`.
- Supporting / enforcement mechanisms: one credential pool per provider shared across named pools, pool-wide limiters, pre-call leases, provider/model route ordering, credential health, router mutex and actual-usage reconciliation.
- Closure path: concurrent session requests reach the same live router → the router evaluates shared pool/credential state → grants a lease/route or returns a rate/no-route failure → actual successful usage is reconciled into the shared limiter state and failures may bench credentials → later S1 calls are admitted/routed/refused against the changed shared state.
- Boundary reachability: standard `RouterModels` binds every normal daemon chat role to the same `Arc<Mutex<ModelRouter>>`; this S2-specific path is therefore present in ordinary multi-session deployment rather than only in tests/examples.
- Why this is / is not agent-owned: the coordination function is real, but the response follows configured deterministic limiter/routing rules. No agent inspects the inter-session contention and chooses or revises the coordination response. The first-party limits/router expose the relevant S2-specific decision/feedback path for downstream autonomous composition, which supports `C` rather than `A`.
- Evidence: [`crates/hx-agent/src/model.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-agent/src/model.rs); [`crates/hx-provider/src/router.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-provider/src/router.rs); [`hx.example.yaml`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/hx.example.yaml); [`crates/hx-server/src/chat.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/chat.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: one-shot `/v1/fanout` children are not the positive witness. The S2 witness is the deployment's multiple durable autonomous chat sessions sharing one quota-bearing router.
- Distinct S1 units: independently created/resumed durable chat sessions, each running its own model→tool→feedback loop and workspace/session context; only concurrent requests to the same session are serialized, so different sessions can execute concurrently.
- Inter-S1 disturbance: calls from different sessions can contend for the same provider credential and named-pool capacity. The router explicitly shares credential pools across named pools so multiple consumers cannot each spend the full limit of one key.
- Attenuating coordination relation: shared pre-call lease/reservation, pool/credential concurrency/rate/token/spend limits, route selection/failover and post-call reconciliation serialize/account for the scarce capacity.
- Feedback into subsequent S1 behaviour: a call is admitted onto a concrete route or receives a rate/no-route failure; successful usage and credential failures mutate shared limiter/health state, changing admission/routing for later calls from this or other sessions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is tied to a concrete inter-S1 shared-resource collision and is explicitly designed to prevent duplicated consumption of the same provider allowance. Generic fan-out, mailboxes or parent-child delegation are not used as the witness.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the daemon's current shared model-provider resource surface on behalf of the deployment as a whole, using aggregate current state to change which provider/model resources remain available to subsequent S1 operation.
- Disturbance / variety regulated: provider availability/authentication failure, changing model/provider availability, unhealthy credentials, deployment resource pressure visible in shared status, and an operator/controller need to add, replace or remove current provider capacity without restarting/rebuilding each S1.
- Decisive decision or feedback right: choose whether and how the live provider set is changed for the whole deployment—provider identity/kind, endpoint, advertised models, routing strategy/key, or removal—and thereby change the shared registry/router used by subsequent sessions.
- Decision owner: base Constructor mode has no shipped autonomous S3 owner; a downstream controller must own the current-resource judgment while using the first-party status/provider API. In the parent mode, the self-hosted deployment operator owns the decision through the first-party web/API control surface.
- Supporting / enforcement mechanisms: combined status snapshot, provider/pool summaries, authenticated daemon API, provider-config persistence, `ProviderRegistry` rebuild, `ModelRouter` rebuild, model-factory replacement and live state locks/swaps.
- Closure path: current deployment status/provider state is observed → controller/operator decides a provider-resource mutation → `PUT`/`DELETE /v1/providers/{name}` validates the request → hx rebuilds and swaps the live provider registry/router/model factory and persists the config → later S1 model calls resolve through the changed shared resource surface.
- Boundary reachability: `/v1/status`, `/v1/pools` and `/v1/providers` are standard routes on the same authenticated daemon API used by the embedded first-party web client; live replacement is implemented in the shipped runtime, not a development-only helper.
- Why this is / is not agent-owned: hx does not ship an autonomous actor that reads the deployment view and decides when/how to reconfigure current provider resources. The API is nevertheless S3-specific rather than a generic callback: it exposes aggregate current state plus a live whole-deployment resource mutation with immediate operational closure. The bundled operator closes a distinct parent-governed mode.
- Evidence: [`crates/hx-server/src/routes.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/routes.rs); [`crates/hx-server/src/state.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/state.rs); [`crates/hx-provider/src/router.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-provider/src/router.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: the mapping is deliberately limited to current shared provider-resource regulation. Ordinary approval prompts, session-local stop limits, sandbox reaping and fan-out orchestration are supporting/local mechanisms and are not independently counted as S3.
- Whole-system current view: `AppState::status` combines deployment-wide pool/role status, provider count, session count, sandbox availability/capacity/live count, host summaries, search backends and webhook queue depths; provider/pool endpoints expose the current resource configuration used by the same daemon.
- Current-control decision scope: current provider/model resource availability and routing surface for all subsequent sessions in the deployment, including live add/edit/remove and replacement of the shared router/registry/model factory.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Downstream-composed autonomous controller; hx supplies the S3-specific status/provider decision path but not the actor | Developer-defined current deployment condition read through the first-party status/provider API | Controller submits provider mutation → hx rebuilds/swaps live registry/router/model factory → subsequent S1 calls use changed resources | [`crates/hx-server/src/routes.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/routes.rs); [`crates/hx-server/src/state.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/state.rs) |
| Parent (`P`) | Self-hosted deployment operator using the first-party web/API control surface | Operator observes deployment/provider state and decides current provider resources must change | Operator's accepted add/edit/remove is applied to live registry/router/model factory and persisted; later sessions run under the returned decision | [`crates/hx-server/src/routes.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/routes.rs); [`crates/hx-server/src/state.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/state.rs) |

## S3* — Complementary audit

- State: C
- Function: provide a separately callable integrity audit of the persisted operational event trail so routine session/event reporting can be challenged when stored rows have been altered, deleted/reordered or were never covered by the audit chain.
- Disturbance / variety regulated: silent corruption/tampering of persisted operational evidence, missing sequence entries and ambiguity between genuinely verified events and legacy/unchained events.
- Decisive decision or feedback right: produce an audit verdict (`intact`, `broken`, or effectively unverified/`unchained` coverage) from the stored chain, identify the first broken sequence/digest mismatch and expose that finding separately from ordinary event rendering. Organizational independence and corrective action remain to be supplied by the composing application/controller.
- Decision owner: no autonomous first-party auditor owns the organizational response. The deterministic verifier owns computation of the integrity finding; a downstream-composed auditor/controller must supply sufficient independence, judgment over the finding and corrective/escalation closure.
- Supporting / enforcement mechanisms: per-event hash/HMAC-capable chain, sequence/digest verification, keyed/unkeyed guarantee reporting, counts of verified versus unchained events, authenticated audit endpoint.
- Closure path: ordinary operation writes session events → a separate audit request reads/verifies the stored chain → endpoint returns integrity/coverage evidence and exact break location → downstream audit/control composition can use that finding to challenge the ordinary record and change/escalate subsequent control. The last organizational response step is intentionally not shipped, hence `C` rather than `A`.
- Boundary reachability: `GET /v1/sessions/{id}/audit` is registered in the standard daemon router and directly invokes store verification; no test-only harness or post-ref module is required.
- Why this is / is not agent-owned: verification is deterministic and hx supplies no separate autonomous auditor that decides what the finding means or owns corrective authority. The path is nevertheless S3*-specific: it independently recomputes integrity evidence over the persisted trail and can contradict the ordinary event record, rather than merely re-rendering logs.
- Evidence: [`crates/hx-server/src/routes.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/routes.rs); [`crates/hx-store/src/audit.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-store/src/audit.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: the audit claim is deliberately narrow: integrity/ordering of the stored event trail. It does not prove task correctness, environmental truth or authorship. An unkeyed chain is weaker against full rewrites, and the endpoint explicitly reports whether the chain is keyed.
- Claim being audited: that the persisted session event trail covered by the chain still matches the recorded sequence/digests and has not suffered an inconsistent alteration or deletion/reordering.
- Ordinary reporting path: normal session/event APIs and clients read/render the stored event records as operational history.
- Complementary access path: the audit endpoint independently recomputes the event-chain verification and reports checked/unchained coverage plus the first broken sequence and stored/expected digest when a mismatch exists.
- Independence boundary: the verifier is separate from normal event rendering and, when keyed, can use HMAC-backed chain evidence, but it remains inside the same daemon/store trust boundary. Strong deployment separation and an independent autonomous judgment actor are left to composition.
- Who acts on findings: not fixed by the standard distribution; a downstream evaluator/controller or operator must consume the audit finding and establish corrective authority/feedback.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop is established at the assessed daemon recursion.
- Disturbance / variety regulated: task-level web/search variation, provider availability and browser-fetch refusal are handled operationally, but no prospective environmental distinction is converted into a durable adaptation option for the organization.
- Decisive decision or feedback right: not established for S4.
- Decision owner: none established for S4 at this boundary.
- Supporting / enforcement mechanisms: multi-backend research/fetch pipeline, browser fallback ladder, provider failover/health, Laya typed-decision helper, configuration and roadmap material.
- Closure path: not applicable; reviewed external sensing and local decision helpers do not form external/future distinction → adaptation option → conversation with present capability/S3 → changed organizational capability.
- Why this is / is not agent-owned: no qualifying S4 function is established, so ownership classification does not proceed.
- Evidence: [`crates/hx-search/src/research.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-search/src/research.rs); [`crates/hx-decision/src/lib.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-decision/src/lib.rs); [`docs/laya.md`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/docs/laya.md); [`crates/hx-provider/src/router.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-provider/src/router.rs).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a downstream agent could combine research/Laya/current-control APIs into S4, but that would be a new composition and is not a supplied closure at the frozen revision.

### Absence scope

- Surfaces inspected: production research/search and browser-fetch selection, provider routing/failover/health, typed Laya decision substrate and its frozen integration documentation, daemon status/provider control, repository tree for learning/adaptation surfaces, roadmap/plan files as non-current evidence.
- Plausible first-party paths checked: external web research, automatic browser escalation, provider-health reaction, Laya threshold/cascade decisions, future-planning documents and runtime provider reconfiguration.
- Why no material first-party path remains: each implemented path either supports the current task/current availability or exposes a generic decision primitive; none develops prospective organizational adaptation options from environmental distinctions and returns them into present capability as a closed S4 conversation.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the assessed daemon recursion.
- Disturbance / variety regulated: approval levels, capability scopes, host/sandbox restrictions, provider/role configuration and API authentication constrain ordinary operation, but no identity-level dispute/proposal and ultimate-policy resolution path is established.
- Decisive decision or feedback right: not established for S5.
- Decision owner: none established for S5 at this boundary.
- Supporting / enforcement mechanisms: capability tokens, approval policy/floor/allowlist, operator approval queue, roles/pools, provider configuration, API bearer authentication and deployment configuration.
- Closure path: not applicable; ordinary action approvals and live provider-resource changes close operational/current-control questions rather than an identity/ultimate-policy issue.
- Why this is / is not agent-owned: no qualifying S5 function is established. Operator authority over ordinary approvals or current provider resources must not be promoted to S5 merely because the operator has final say on those events.
- Evidence: [`hx.example.yaml`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/hx.example.yaml); [`crates/hx-server/src/chat.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/chat.rs); [`crates/hx-server/src/routes.rs`](https://github.com/phantomic12/hx-harness/blob/6afe2291a5bc750903eae1e9266ace8cdeb2eaef/crates/hx-server/src/routes.rs).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a deployment operator plainly remains an ultimate real-world authority over the software, but Methodology `0.3.x` requires a function-specific identity/ultimate-policy issue → authority → returned-decision closure before publishing S5 parent governance.

### Absence scope

- Surfaces inspected: approval policy and interactive approval responses, capability issuance, role/pool/provider configuration, daemon authentication, runtime provider mutation, prompts/configuration and Laya decision substrate.
- Plausible first-party paths checked: human approval of risky actions, persistent allow/config changes, provider/resource control, configured autonomy levels and operator ownership of the self-hosted daemon.
- Why no material first-party path remains: the reviewed mechanisms decide or enforce operational permissions/resources. None identifies an identity/ultimate-policy matter, routes it to a legitimate ultimate authority as such, and returns that authoritative policy/identity decision to govern subsequent operation.

## Recursion, variety, and escalation

At the chosen daemon recursion, durable chat sessions are the operational units because each has its own persistent transcript/workspace context and autonomous model→tool loop. The shared deployment router sits above them and attenuates provider-capacity contention. Same-session locking prevents transcript corruption inside one S1; it is not the credited inter-S1 S2 relation. One-shot fan-out children are bounded provider calls rather than recursive viable units.

Variety enters from user tasks, changing files/hosts, tool results, model/provider responses, shared quota pressure, credential failures, approvals and external research sources. hx attenuates part of that variety deterministically through capabilities, approvals, sandboxes, pool/credential limits, role routing and bounded concurrency. It amplifies operational reach through remote hosts, tools, search/research and multiple providers.

Escalation is explicit for ordinary protected actions: a policy can ask a parent operator, and absence/timeout becomes refusal rather than implicit permission. That path is operational approval, not S5. Provider resource changes have a separate whole-deployment parent-control closure credited to S3. Audit findings are exposed independently but require downstream/operator composition to turn them into corrective action, which is why S3* remains Constructor rather than Autonomous.

## Evidence gaps

- No frozen first-party autonomous actor was found that consumes deployment status and revises shared provider/resource policy; the Laya subsystem is not wired into that role at the reviewed revision.
- The S3* constructor path verifies stored-event integrity, not task correctness or external ground truth; stronger audit semantics would require a different complementary evidence source and corrective authority.
- Roadmap/plan claims and later upstream files absent from `6afe2291a5bc750903eae1e9266ace8cdeb2eaef` were not used to close any function.
