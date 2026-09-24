---
harness_id: rottay-agent-control-plane
project_name: Rottay Agent Control Plane
repository: https://github.com/rottay/agent-control-plane
review_ref: 07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Rottay Agent Control Plane

## Review boundary

- System in focus: the first-party `rottay/agent-control-plane` repository at pinned revision `07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8`, including runtime/durability/account/observation domains, provider execution ports, CLI/API/local transport adapters, routing/quota/lease/conflict/commit controls, ledger-backed lifecycle and the shipped daemon/entrypoint surfaces that exist at the reviewed ref.
- Purpose and identity: provide a local-first control plane around AI coding-agent executions across providers/accounts, with durable orchestration, routing, quotas, lifecycle ownership, conflict/write controls, evidence and recovery.
- Relevant environment: Claude/Codex/Kimi and other provider-agent CLIs, injected API/local streaming clients and their model/tool loops, users/operators, repositories/worktrees, external tool servers, provider accounts and application integrations.
- Standard-distribution boundary: repository-owned control-plane packages and provider adapters are inside. The autonomous reasoning/tool loops of external provider harnesses or injected streaming clients are environmental actors unless the repository itself closes their model/tool feedback loop.
- Credited operating / distribution surfaces: `README.md`; `docs/ROADMAP.md`; `packages/domains/runtime/README.md`; `packages/edges/providers/src/session/index.ts`; `packages/edges/providers/src/execution-port/index.ts`; `packages/edges/providers/src/api-key/index.ts`; `packages/edges/providers/src/claude/index.ts`; `packages/domains/runtime/src/tool-call/index.ts`; shipped daemon/runtime/account/observation code where it documents current behavior.
- Adjacent first-party surfaces excluded from ownership: target-state README claims not yet backed by the frozen implementation; roadmap packets not landed at the reviewed ref; tests/drills except as corroboration; future SDK/product cutover work. Existing P0-P8 implementation is credited where it actually ships and is not dismissed merely because P9 cutover remains incomplete.
- First-party operating / deployment modes considered: CLI-subscription execution over provider child processes; API-key execution over injected streaming clients; local/self-hosted injected clients; durable task lifecycle, routing, account quota, pressure/switch handling, tool-call recording/claims, conflict/write enforcement, observation/evidence and recovery paths.
- Recursion level: this repository's reusable control plane itself, as admitted to organizational/control batch #407. A deployment that embeds an external coding-agent harness behind these transports is a wider composed system and requires separate evidence.
- Reviewed revision: `07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Rottay Agent Control Plane contains unusually deep first-party control machinery, but the reviewed implementation still places the autonomous coding-agent actor on the transport side of the boundary.

For CLI subscriptions, the provider layer starts admitted external coding-agent processes such as Claude/Codex/Kimi and normalizes their emitted events. `startSession` owns process/session lifecycle, sends the task instruction to the child and parses the child stream; it does not implement the provider harness's internal model/tool reasoning loop. The execution port explicitly describes itself as converting a resolved route into an execution and its output into normalized events while adding no decision authority of its own.

The API/local legs preserve the same ownership boundary in a different form. `ApiStreamingClient` is an injected client interface whose `stream(request)` produces model/provider chunks such as text and tool-use events. The first-party adapter validates and normalizes those chunks, but no provider SDK or autonomous model/tool loop is implemented in that adapter. The code itself states that the SDK binding is an optional implementation behind the injected interface.

The runtime domain is substantial: ledger-first durable lifecycle, account/routing/quota policy, provider pressure, failure/cancellation, execution effects, conflict graphs, leases, commit authorization, evidence roots, tool-call receipts and recovery. Yet its own README calls the package a durability/supervisor plane and says the enforcement plane is "decision machinery only" with no production observer. It also states that this package is not product adoption and is not connected to real operation at that boundary.

The direct tool-call path is especially decisive. `runtime/src/tool-call` says it supplies the explicit tool-call *operation only*: there is no door, route, CLI verb, process start or tools-package import, and until an entrypoint composes those pieces nothing in that runtime module calls a tool. Thus the reviewed control plane cannot be credited with an internal model → tool invocation → observation → next-model-decision loop merely because the contracts and durable recording machinery for such a loop already exist.

`docs/ROADMAP.md` is used only to distinguish landed machinery from target/product cutover, not as the sole reason for exclusion. P9 remains the SDK cutover that removes direct harness orchestration from consumers and binds the control plane as the normal product path. More importantly for VSM classification, the actual frozen implementation still delegates goal-directed agent behavior either to a spawned provider harness or an injected streaming client.

Counterfactual owner test: remove the external provider harnesses and injected model clients while leaving routing, quotas, ledger lifecycle, execution ports, account switching, pressure handling, conflict/write enforcement, observation and recovery intact. The remaining repository can admit, route, constrain, persist, supervise, normalize and recover hypothetical executions, but it has no first-party autonomous actor that can interpret the task objective, choose substantive model/tool actions, observe tool results and decide what action follows. First-party S1 therefore does not close.

Under Methodology `0.3.6`, the terminal result is `excluded-no-agentic-vsm`. Rich organizational/control primitives are not published as S2-S5 states once the qualifying operational S1 organization lies outside the repository boundary.

Primary evidence:

- [`docs/ROADMAP.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/docs/ROADMAP.md) — canonical implementation/cutover status and remaining SDK/product adoption boundary.
- [`packages/domains/runtime/README.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/domains/runtime/README.md) — durability/supervisor scope, decision-machinery-only boundary, no production observer/product adoption and tool-call operation status.
- [`packages/edges/providers/src/session/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/session/index.ts) — provider child-process session ownership and instruction/event transport.
- [`packages/edges/providers/src/execution-port/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/execution-port/index.ts) — unified CLI/API/local execution boundary, normalized event ownership and transport semantics.
- [`packages/edges/providers/src/api-key/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/api-key/index.ts) — injected streaming-client boundary rather than a first-party provider model loop.
- [`packages/edges/providers/src/claude/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/claude/index.ts) — adapter around the external Claude CLI protocol.
- [`packages/domains/runtime/src/tool-call/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/domains/runtime/src/tool-call/index.ts) — explicit tool-call operation without an entrypoint/door that performs the call from this domain.

## S1 — Operations

- State: —
- Function: no first-party autonomous goal-directed model/tool operational loop is established inside the repository boundary at the reviewed ref.
- Disturbance / variety regulated: the control plane regulates routing, account/provider availability, quotas, leases, process/session lifecycle, conflicts, writes, failures, evidence and recovery; the semantic task uncertainty and next-action selection remain with the provider harness/client.
- Decisive decision or feedback right: interpret the task objective, choose the next substantive coding/model/tool action, observe returned tool/environment state and decide what operational action follows.
- Decision owner: external Claude/Codex/Kimi-style provider harnesses on the CLI leg or externally supplied streaming clients/model runtimes on API/local legs.
- Supporting / enforcement mechanisms: execution port, provider adapters/session controller, routing/accounts, quota/pressure/switching, runtime lifecycle, ledger, effects, tool receipts, conflict/lease/write enforcement and recovery.
- Closure path: durable task/route → first-party control plane admits and starts/contacts a provider execution → external harness/client performs autonomous model/tool work → first-party adapters normalize events/evidence → control plane supervises lifecycle. The semantic next-action loop remains inside the external provider actor rather than closing in first-party control-plane code.
- Boundary reachability: CLI execution explicitly spawns provider binaries; API/local execution explicitly depends on injected streaming clients; the runtime tool-call module explicitly lacks its own operational door at the frozen revision.
- Why this is / is not agent-owned: the control plane owns execution governance and lifecycle, not the autonomous task-level decision process that makes an execution an S1 operation.
- Evidence: [`packages/edges/providers/src/session/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/session/index.ts); [`packages/edges/providers/src/execution-port/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/execution-port/index.ts); [`packages/edges/providers/src/api-key/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/api-key/index.ts); [`packages/domains/runtime/src/tool-call/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/domains/runtime/src/tool-call/index.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the repository already owns much of the membrane around an operational actor, and a later cutover/wiring change could materially change this result. That would require a new-ref reassessment rather than retroactively crediting the frozen revision.

### Absence scope

- Surfaces inspected: provider CLI adapters/session controller, execution-port factory, API/local transport interfaces, runtime lifecycle/step executor/tool-call/effects, account routing/quota/switching, observation/evidence, roadmap and daemon/product-cutover documentation.
- Plausible first-party paths checked: spawned CLI session as S1; execution port as model runtime; injected API client as first-party actor; tool-call operation as an internal agent loop; step executor as planner/agent; daemon lifecycle as autonomous operation.
- Why no material first-party path remains: each candidate either supervises/transports an external autonomous actor or is durable decision/effect infrastructure whose direct operational door/model-tool continuation is absent at this revision.

## S2 — Coordination

- State: —
- Function: no first-party S2 state is published because the qualifying autonomous operational units are not inside this repository-relative boundary.
- Disturbance / variety regulated: conflict graphs, account switching, routing, leases and provider-pressure logic can regulate interactions among external executions, but the S1 actors whose interference would define S2 remain environmental.
- Decisive decision or feedback right: no internal coordination owner over first-party S1-to-S1 disturbance is established.
- Decision owner: not established inside the qualifying repository boundary.
- Supporting / enforcement mechanisms: conflict graph, leases, routing, account switching, provider pressure and execution-session identity.
- Closure path: control machinery can coordinate externally hosted executions, but the resulting relation does not close among first-party S1 units because those operational actors are outside the boundary.
- Why this is / is not agent-owned: function-specific coordination primitives may become S2 in a composed deployment, but primitives around external agents are not sufficient for positive repository-relative publication after S1 admission fails.
- Evidence: [`packages/domains/runtime/README.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/domains/runtime/README.md); [`packages/edges/providers/src/execution-port/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/execution-port/index.ts).
- Basis: structural negative search.
- Confidence: high.
- Caveats: this does not claim the conflict/routing machinery is organizationally uninteresting; it says its positive VSM classification belongs to a wider system that includes the autonomous provider actors.

### Absence scope

- Surfaces inspected: conflict graph, leases, routing, quotas, account switching, provider pressure and execution registry/session ownership.
- Plausible first-party paths checked: conflict graph as S2; routing/account switching as S2; session/harness registry as coordination; pressure handling as inter-S1 attenuation.
- Why no material first-party path remains: the interacting autonomous units are externally hosted and no internal S1 population is established at this recursion.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current-control state is published after repository-relative S1 admission fails.
- Disturbance / variety regulated: quotas, route selection, leases, process lifecycle, provider pressure, task state, failure/cancellation, conflict and commit authorization all regulate current execution conditions.
- Decisive decision or feedback right: the repository contains substantial deterministic/current-control authority, but the governed operational units are external provider actors and no qualifying internal S1 whole exists at this boundary.
- Decision owner: control-plane rules/operators over external executions rather than an internal autonomous S3 owner of a first-party operational organization.
- Supporting / enforcement mechanisms: accounts/quota/routing, runtime lifecycle, pressure/switching, cancellation/failure, leases, commit authorization and daemon supervision.
- Closure path: current telemetry/state → deterministic control-plane decision/enforcement → external provider execution is admitted, switched, interrupted or constrained. This can serve S3 in a composed organization but does not establish repository-alone S3 publication without internal S1.
- Why this is / is not agent-owned: strong current-control enforcement is not discarded; it is simply not promoted into a positive VSM state across a boundary that excludes the operation it governs.
- Evidence: [`packages/domains/runtime/README.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/domains/runtime/README.md); [`packages/edges/providers/src/execution-port/index.ts`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/edges/providers/src/execution-port/index.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a composed deployment that includes provider workers could plausibly expose constructor or stronger S3 paths; this assessment intentionally does not import them.

### Absence scope

- Surfaces inspected: accounts, quota, routing, switching, runtime lifecycle, pressure, cancellation/failure, conflict/lease/write enforcement and daemon supervision.
- Plausible first-party paths checked: quota as S3; route/account selector as manager; provider switching as current control; daemon as manager; commit authorization as S3.
- Why no material first-party path remains: all positive control acts target externally owned operational actors or durability/enforcement state rather than an internal qualifying S1 whole.

## S3* — Complementary audit

- State: —
- Function: no positive repository-relative complementary-audit state is published without an internal first-party S1 operational organization and a function-specific independent corrective loop over it.
- Disturbance / variety regulated: evidence roots, shadow ledgers, observation rollups, verification/commit authorization and separate identities can independently constrain or inspect execution facts.
- Decisive decision or feedback right: no credited runtime path establishes an independent first-party auditor challenging an internal S1's operational reality and returning corrective action into its controller.
- Decision owner: not established at this recursion.
- Supporting / enforcement mechanisms: observation package, evidence roots, ledger records, commit authorization and verifier/writer separation constraints.
- Closure path: evidence can be independently checked around external executions, but no qualifying internal S1 → independent audit → corrective return closure is established.
- Why this is / is not agent-owned: verifier/evidence terminology and even independent-verifier constraints are not enough by themselves; S3* requires the complementary organizational relation at the declared system boundary.
- Evidence: [`packages/domains/runtime/README.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/domains/runtime/README.md); repository `packages/domains/observation` and commit-authorization surfaces at the pinned revision.
- Basis: structural negative search.
- Confidence: high.
- Caveats: the repository has strong ingredients for independent audit in a wider composed agent organization; exclusion prevents treating those ingredients as a standalone S3* publication here.

### Absence scope

- Surfaces inspected: observation/read models/rollups/shadow ledger, evidence root, commit authorization, verification separation and recovery evidence.
- Plausible first-party paths checked: observation plane as S3*; independent verifier as S3*; shadow ledger/evidence root as audit; commit authorization as corrective audit.
- Why no material first-party path remains: these paths establish evidence/verification constraints around externally owned operation, not an internal complementary-audit loop over first-party S1.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/prospective intelligence and adaptation closure is established at the assessed repository boundary.
- Disturbance / variety regulated: routing policy, provider/account choices and product evolution can change as capabilities/conditions evolve, but the frozen runtime does not show an internal actor building prospective environmental models/options and feeding adaptation into a qualifying internal S3/S1 organization.
- Decisive decision or feedback right: select future organizational capability changes from external/prospective evidence.
- Decision owner: roadmap/developers/operators or external provider actors, not a first-party runtime S4 actor.
- Supporting / enforcement mechanisms: observation metrics, routing/account policy, provider capability data, roadmap/qualification drills and configuration.
- Closure path: external development/operator decisions change later code/configuration; no runtime S4 feedback closure is established.
- Why this is / is not agent-owned: provider switching and capability-aware routing are current execution selection, while roadmap-driven product evolution is development activity; neither establishes S4 by itself.
- Evidence: [`docs/ROADMAP.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/docs/ROADMAP.md); [`packages/domains/runtime/README.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/domains/runtime/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: extensive roadmap/qualification work is evidence of engineering adaptation, not automatically a deployed organizational S4 function.

### Absence scope

- Surfaces inspected: observation, account routing/switching, provider capability/pressure, roadmap qualification, runtime recovery and policy surfaces.
- Plausible first-party paths checked: provider switching as adaptation; observation trends as sensing; roadmap/qualification as learning; account policy evolution as S4.
- Why no material first-party path remains: no deployed first-party external/prospective option-generation loop is coupled back into a qualifying current-control/operational organization.

## S5 — Policy / identity

- State: —
- Function: no first-party identity/ultimate-policy deliberation and closure path is established at this repository-relative recursion.
- Disturbance / variety regulated: capability policies, account/provider admission, identities, quotas, commit/write rules and operator configuration strongly constrain operation.
- Decisive decision or feedback right: determine the organization's durable mission/identity and resolve ultimate policy tradeoffs.
- Decision owner: external developers/operators/policy configuration rather than a first-party runtime S5 actor or evidenced parent-governed return path.
- Supporting / enforcement mechanisms: policy/configuration contracts, worker identities, account registry, route/admission policy, commit/write authorization and operator controls.
- Closure path: externally authored policy/configuration → first-party enforcement → external provider executions are constrained. No identity-level matter → legitimate ultimate authority → authoritative decision → returned first-party operation loop is established.
- Why this is / is not agent-owned: strict policy enforcement and authoritative ledger contracts are mechanisms, not evidence that this repository owns organizational identity or ultimate policy.
- Evidence: [`docs/ROADMAP.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/docs/ROADMAP.md); [`packages/domains/runtime/README.md`](https://github.com/rottay/agent-control-plane/blob/07f4f9c4f8914bb8bec6e179b747f7a8cb7085c8/packages/domains/runtime/README.md).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a wider organization may deliberately use this control plane as an enforcement membrane beneath parent-owned S5, but generic operator/configuration ownership is insufficient to publish `P` here.

### Absence scope

- Surfaces inspected: worker identity, account/policy/routing, quotas, runtime authorization/enforcement, ledger authority, operator configuration and roadmap governance.
- Plausible first-party paths checked: ledger authority as S5; capability policy as S5; operator state as parent S5; commit authorization as ultimate policy; README mission as identity closure.
- Why no material first-party path remains: these surfaces encode/enforce externally authored rules and system invariants without an operational identity-level deliberation/return loop.

## Proposed terminal outcome

`excluded-no-agentic-vsm`.

Rottay Agent Control Plane is a substantial, unusually rigorous control-plane implementation. The exclusion is specifically about the pinned repository-relative operational boundary: the autonomous coding-agent model/tool loop remains in external provider harnesses or injected clients, while the first-party runtime's direct tool path is not yet product-wired into such a loop. Therefore the repository does not establish first-party S1 required for Index inclusion at this revision.

## Evidence boundaries / caveats

- Incomplete P9 cutover is contextual evidence, not the sole exclusion criterion; landed P0-P8 machinery is credited as real where primary code establishes it.
- The external provider child/client is not imported merely because the control plane owns its process/session lifecycle.
- `toolUse`, execution events and tool-call receipts are not treated as proof of a first-party agent loop unless the repository also closes the invocation/observation/next-decision path.
- Conflict, routing, quota, verification, observation and policy mechanisms may map positively in a wider composed system; they remain `—` in this standalone exclusion because first-party S1 admission fails.