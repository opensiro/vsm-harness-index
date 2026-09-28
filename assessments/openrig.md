---
harness_id: openrig
project_name: OpenRig
repository: https://github.com/mvschwarz/openrig
review_ref: c8fca9d5c436e5357807e05254bf6735613eea3f
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# OpenRig

## Review boundary

- System in focus: one first-party OpenRig deployment at pinned revision `c8fca9d5c436e5357807e05254bf6735613eea3f`, including the shipped daemon/CLI/TUI/MCP control plane, durable queue/workflow state, RigSpec topology, managed Claude Code/Codex/Pi seats, bundled agent roles/skills, and shipped launchable rig/workflow compositions.
- Purpose and identity: organize multiple persistent coding-agent sessions as one durable team with named seats, work custody, orchestration, independent review, topology control, workflow routing and supported self-improvement modes.
- Relevant environment: configured Claude Code/Codex/Pi runtimes and their model providers, repositories/workspaces acted on by managed seats, local or registered remote hosts, tmux/session infrastructure, authenticated human operator, and external product/user reality observed by the factory dogfood mode.
- Standard-distribution boundary: OpenRig-owned daemon, CLI/TUI/MCP server, SQLite-backed queue/workflow/topology state, built-in RigSpecs, bundled agent definitions/skills and shipped workflow specs. Model-provider internals and generic Claude Code/Codex/Pi reasoning engines remain external dependencies; their unrelated internal organizational functions are not imported.
- Credited operating / distribution surfaces: `rig up` launchable starters including `first-project` and `factory-rsi`; managed seat/runtime adapters; queue/handoff/workflow runtime; bundled `orchestration-team`, development/QA/review roles; live topology/session surfaces; and the factory-rsi dogfood→next-plan path where those surfaces are packaged together in a supported mode.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests, maintainer/contributor governance, release notes as historical evidence, preview-only compositions where no shipped mode is needed for a positive claim, benchmark/demo fixtures, and dogfood/review artifacts that are not wired into a credited supported mode.
- First-party operating / deployment modes considered: `first-project`; ordinary managed multi-seat rigs using queue/workflow/orchestration primitives; the shipped `factory-rsi` starter and built-in workflow; supported live topology mutation; operator inspection/control. Preview product-team material was inspected as corroboration only and is not required for the positive vector.
- Recursion level: one OpenRig rig/deployment. Managed coding-agent seats are S1 operational units. Orchestrator, QA/reviewer and factory-dogfood seats are mapped only when they exercise a distinct metasystem function over those operations in the shipped composition.
- Reviewed revision: `c8fca9d5c436e5357807e05254bf6735613eea3f`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

OpenRig deliberately wraps agent harnesses rather than replacing their model/tool loops. Its daemon maintains stable rig/pod/member identities, durable work records, queue transitions, workflow instances and runtime bindings around Claude Code, Codex and Pi sessions. RigSpecs declare seats, roles, runtimes and topology; the runtime launches or adopts sessions and injects bundled role/skill context. The queue provides durable custody and handoff, while workflow specs route bounded work among named roles.

The smallest shipped multi-agent starter, `first-project`, launches an outcome-owner Codex seat and a separate checker Codex seat. The owner claims durable work, implements a bounded outcome and hands the exact candidate/evidence to `dev-check`; the checker is explicitly independent of the author, reads the diff and actual behavior, records findings, and returns them to the owner for repair/recheck. This forms a directly reachable complementary-audit loop rather than a merely available test utility.

OpenRig also ships an explicit orchestration function. The bundled orchestrator reads current queue custody plus live seat state, dispatches current outcomes with territory/context/return boundaries, detects blocked or dropped work, redirects/unblocks it, reassigns or defers current commitments and can add capacity within authorized scope. The function is carried by an autonomous managed orchestrator seat in shipped compositions such as `factory-rsi`; deterministic queue/workflow/topology services enforce the selected commitments but do not own the orchestration judgment.

A distinct shipped `factory-rsi` mode closes prospective adaptation. `rig up factory-rsi` launches a seven-seat rig and the built-in workflow runs plan → implement → QA → review → release preparation. A decoupled dogfood seat continuously uses the already-shipped product out-of-band, records real-use findings as durable evidence, and feeds those findings into the next planner cycle. The planner turns that external operational evidence into a new buildable slice; later implementation/review/release changes future shipped capability. Publication itself remains human-gated, but the adaptation judgment/loop does not require a human.

Primary evidence:

- [`README.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/README.md) — declared harness-of-harnesses boundary, managed team model, RigSpec/topology/runtime surfaces and shipped starter overview.
- [`docs/reference/getting-started.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/docs/reference/getting-started.md) — first-project owner/checker operation, durable task custody and exact-candidate independent check.
- [`packages/daemon/specs/rigs/launch/first-project/rig.yaml`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/rigs/launch/first-project/rig.yaml) and [`CULTURE.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/rigs/launch/first-project/CULTURE.md) — shipped owner + independent checker topology and corrective return contract.
- [`packages/daemon/specs/agents/development/implementer/guidance/role.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/agents/development/implementer/guidance/role.md) and [`development/qa/guidance/role.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/agents/development/qa/guidance/role.md) — operational owner and independent-QA decision boundaries.
- [`packages/daemon/specs/agents/orchestration/orchestrator/guidance/role.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/agents/orchestration/orchestrator/guidance/role.md) and [`shared/skills/pods/orchestration-team/SKILL.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/agents/shared/skills/pods/orchestration-team/SKILL.md) — whole-rig current view, dispatch, blocker handling and current-work intervention.
- [`packages/daemon/specs/agents/review/independent-reviewer/guidance/role.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/agents/review/independent-reviewer/guidance/role.md) and [`shared/skills/pods/review-team/SKILL.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/agents/shared/skills/pods/review-team/SKILL.md) — independent evidence-based review semantics.
- [`docs/as-built/architecture/coordination-primitive.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/docs/as-built/architecture/coordination-primitive.md) — durable queue ownership, transitions and hot-potato handoff enforcement inspected for S2/S3 support.
- [`packages/daemon/specs/rigs/launch/factory-rsi/rig.yaml`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/rigs/launch/factory-rsi/rig.yaml), [`packages/daemon/src/builtins/workflow-specs/factory-rsi.yaml`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/src/builtins/workflow-specs/factory-rsi.yaml), and [`factory-rsi/dogfood/guidance/role.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/packages/daemon/specs/agents/factory-rsi/dogfood/guidance/role.md) — shipped autonomous outside-and-then feedback into future product slices.
- [`docs/releases/v0.4.6.md`](https://github.com/mvschwarz/openrig/blob/c8fca9d5c436e5357807e05254bf6735613eea3f/docs/releases/v0.4.6.md) — release-level confirmation that `factory-rsi` and its dogfood→next-plan edge are shipped product surfaces.

## Operational model

OpenRig's operational units are managed coding-agent seats that receive durable owned work and autonomously transform repository/product state using their underlying model/tool runtime. OpenRig itself supplies the durable organization around those actors: identity, task custody, role context, routing, observation, workflow and topology enforcement.

Higher functions are credited only where the standard distribution supplies a separate relationship. The orchestrator's whole-rig current regulation is S3; owner-independent QA/review with direct artifact access and corrective return is S3*; and factory-rsi's real-world shipped-product dogfood feeding later product changes is S4. Queueing, messaging, topology and deterministic workflow sequencing support these functions but are not promoted to S2 without a specific sibling-interference attenuation loop.

## S1 — Operations

- State: A
- Function: perform bounded substantive software/product work assigned to a managed OpenRig seat and return a durable candidate/result with evidence.
- Disturbance / variety regulated: repository state, task ambiguity, implementation defects, tool/runtime feedback, tests, model uncertainty and local execution failures encountered while producing the assigned outcome.
- Decisive decision or feedback right: choose the task-specific code/research/tool actions and iterative corrections needed to satisfy the currently owned outcome.
- Decision owner: the model-driven managed Claude Code/Codex/Pi seat instantiated and role-bound by the shipped OpenRig runtime.
- Supporting / enforcement mechanisms: RigSpec seat identity, runtime adapters, injected role/skill context, queue custody, workspaces, tmux/session lifecycle, workflow routing, context packs and durable evidence records.
- Closure path: durable assignment/context → managed agent interprets current repository/product state → model selects substantive actions/tool use → environment/test feedback returns to the same seat → seat produces candidate/evidence and closes or hands off the work.
- Boundary reachability: shipped starters such as `first-project` create real managed Codex seats from bundled agent definitions; the runtime directly launches/binds those seats and durable work is addressed to their stable OpenRig identities.
- Why this is / is not agent-owned: removing the managed model-driven seat while leaving queue/workflow/topology machinery intact removes the substantive software-work decision right; deterministic OpenRig services can route and enforce custody but do not implement the assigned outcome themselves.
- Evidence: `README.md`; `docs/reference/getting-started.md`; `first-project/rig.yaml`; `development/implementer/guidance/role.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Claude Code/Codex/Pi model-provider internals remain external dependencies. The assessment credits only the first-party supported operating mode that instantiates and governs those agents as OpenRig seats, not unrelated metasystem functions inside the external runtimes.

## S2 — Coordination

- State: —
- Function: no material first-party S2 function is established at the reviewed rig recursion.
- Disturbance / variety regulated: no sufficiently evidenced interaction-generated conflict, oscillation or interference among distinct sibling S1 seats is paired with a first-party attenuation relation that changes their later operational behaviour.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: durable queue custody, hot-potato handoff, messaging, chatrooms, workflow sequencing, role routing, topology edges, host-aware idempotent forwarding and stable seat identity were inspected as possible coordination mechanisms.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the reviewed mechanisms reliably route work, preserve custody and prevent dropped/duplicated transport effects, but generic queueing, messaging, sequencing and handoff are not S2 without a concrete sibling-S1 disturbance/attenuation/feedback witness.
- Evidence: `docs/as-built/architecture/coordination-primitive.md`; `README.md`; `orchestration-team/SKILL.md`; shipped RigSpecs/workflow specs.
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an adopter can use OpenRig to partition work or avoid conflicts, and some preview/topology material discusses territory and capacity. That does not establish a standard-distribution S2 mapping under the current threshold without a specific disturbance relation and feedback into subsequent sibling behaviour.

### Absence scope

- Surfaces inspected: SQLite queue/transition/handoff architecture, cross-host forwarding/dedup, built-in workflows, first-project and factory-rsi topologies, orchestration/development skills, messaging/chatroom/transport, live topology mutation and seat identity/routing.
- Plausible first-party paths checked: exclusive queue ownership, handoff closure, duplicate-forward suppression, task/territory dispatch, multi-host work routing, topology edges and concurrent seat management.
- Why no material first-party path remains: these paths provide reliable custody, routing, sequencing, transport or whole-rig current regulation, but the pinned standard distribution does not establish the required specific inter-S1 interference plus S2-specific attenuation and returned peer-behaviour feedback.

## S3 — Inside-and-now control

- State: A
- Function: regulate the rig's current work portfolio so authorized outcomes remain owned, unblocked, correctly assigned and progressing through the live team.
- Disturbance / variety regulated: current queue custody, blocked or idle owners, missing handoffs, live seat availability, capability/capacity constraints, workflow exceptions, stalled work, assignment gaps and current review boundaries.
- Decisive decision or feedback right: choose current assignments/territories, redirect or unblock stuck work, reassign/defer commitments, select needed capacity, and route exceptions while observing the current rig frontier.
- Decision owner: the model-driven managed orchestrator seat in supported orchestrated compositions.
- Supporting / enforcement mechanisms: durable queue and transitions, `rig ps --nodes`, workflow state, watchdog wake/event signals, `rig send`, context packs, handoff primitives, topology/seat management and deterministic workflow routing.
- Closure path: live queue + seat/workflow evidence → orchestrator interprets whole-rig current condition → orchestrator dispatches/redirects/unblocks/reassigns the current commitment → OpenRig queue/workflow/runtime services enforce the selected transition → later queue/seat state reports the changed current organization.
- Boundary reachability: `factory-rsi` is a shipped `rig up` starter containing an `orch.lead` seat bound to the bundled orchestrator agent, and its built-in workflow routes exceptions to that orchestrator. The same first-party orchestration skill operates on live queue and seat state.
- Why this is / is not agent-owned: deterministic queue/workflow/topology services implement and record transitions but do not choose which current outcome should be dispatched, redirected, deferred or unblocked. Removing the orchestrator actor leaves enforcement machinery but removes the function-specific current-regulation judgment.
- Evidence: `orchestration/orchestrator/guidance/role.md`; `orchestration-team/SKILL.md`; `factory-rsi/rig.yaml`; `factory-rsi.yaml`; `coordination-primitive.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: fixed workflow edges, max-hop guards, queue validation and operator controls are enforcement/support, not the S3 owner. The positive mapping depends on the separately packaged autonomous orchestrator role and its whole-rig current view/decision scope.
- Whole-system current view: current queue frontier/custody and transitions, live rig seats/capabilities/activity, blocked/idle work, workflow attention/exceptions and the current assignment/review boundary state.
- Current-control decision scope: present assignments and territories, unblock/redirect/reassign/defer decisions, capacity choice within authorization, exception routing and current handoff/review sequencing.

## S3* — Complementary audit

- State: A
- Function: independently inspect an operational candidate/outcome against direct artifact and behavior evidence and return defects into corrective operational work before acceptance/continuation.
- Disturbance / variety regulated: an implementation owner may report completion while the exact diff, public journey, tests or failure cases reveal defects, broken promises or unsupported claims not visible through the owner's ordinary report.
- Decisive decision or feedback right: determine whether the exact candidate satisfies the assigned contract and identify evidence-backed defects that require correction/recheck.
- Decision owner: a distinct managed QA/checker or independent-reviewer agent whose role explicitly excludes the author when independence is selected.
- Supporting / enforcement mechanisms: separate checker/reviewer seat, direct diff/source/public-journey access, durable handoff/evidence packet, queue routing, review artifacts, cross-runtime diversity in factory-rsi and deterministic failure routing back to implementation.
- Closure path: owner produces exact candidate/evidence → separate checker/reviewer directly inspects diff/source/behavior/tests → independent findings/verdict are recorded and returned → owner/implementer repairs findings → affected outcome is rechecked before final continuation.
- Boundary reachability: the shipped `first-project` starter contains separate owner and checker seats and its culture explicitly requires the first meaningful code change to be handed to `dev-check` for an independent exact-candidate check. `factory-rsi` separately ships QA/reviewer roles with failed checks/reviews routed back to implementation.
- Why this is / is not agent-owned: deterministic routing can enforce a failed-review return, but the audit judgment itself is made by the independent model-driven checker/reviewer reading complementary evidence. Removing that actor leaves routing and records without an equivalent defect judgment.
- Evidence: `first-project/rig.yaml`; `first-project/CULTURE.md`; `development/qa/guidance/role.md`; `review/independent-reviewer/guidance/role.md`; `review-team/SKILL.md`; `factory-rsi.yaml`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary builder-held verification/TDD is not the S3* witness. Credit comes only from the selected independent path where evaluator authorship is excluded and findings return to corrective work.
- Claim being audited: that the operational owner's exact candidate delivers the assigned user outcome and its stated behavior/evidence is trustworthy.
- Ordinary reporting path: implementer/owner reports the candidate, changed behavior, commands/results and remaining uncertainty through the durable work handoff.
- Complementary access path: independent checker/reviewer reads the exact diff/source and directly exercises or verifies the relevant public behavior/tests rather than relying only on the author's report.
- Independence boundary: the selected independent evaluator must not be the author; if a tester becomes an author, that attribution invalidates the independent role for the repaired candidate until a distinct check is restored.
- Who acts on findings: the owner/implementer receives actionable findings, repairs the candidate and rechecks the affected outcome; shipped factory workflow failure routes the work back to implementation.

## S4 — Outside-and-then intelligence

- State: A
- Function: sense real external use of the already-shipped OpenRig product and convert those observations into prioritized prospective changes that alter later product capability.
- Disturbance / variety regulated: real-user/operator friction, wrong defaults, missing affordances, broken assumptions and other distinctions that appear only when the shipped product is exercised outside the current build/check/review loop.
- Decisive decision or feedback right: identify and prioritize meaningful shipped-product findings, then turn the recorded external-use evidence into the next buildable product slice for future operation.
- Decision owner: the autonomous factory-rsi dogfood agent owns the real-use finding judgment; the subsequent autonomous planner owns selection/formulation of the next buildable slice from those recorded findings.
- Supporting / enforcement mechanisms: shipped `factory-rsi` RigSpec and built-in workflow, durable evidence/packet trail, dogfood role/startup context, planner role, bounded build/QA/review/release workflow and versioned product/release process.
- Closure path: shipped OpenRig is exercised out-of-band by the dogfood seat → real-use distinctions are recorded as durable findings → next planner cycle consumes those findings → planner creates a prospective slice → implement/check/review/release-prep changes the product candidate → after the separate human publish act, later shipped operation contains the adapted capability.
- Boundary reachability: release v0.4.6 explicitly ships `rig up factory-rsi`; the starter launches a dedicated dogfood seat and the built-in workflow names recorded dogfood findings as the next planner input. This is a supported product mode, not repository-development dogfood borrowed from outside the assessed deployment.
- Why this is / is not agent-owned: the product supplies an autonomous dogfood actor and planner with the adaptation judgment; deterministic workflow routing and the human publication gate support/enforce lifecycle boundaries but do not choose which external distinctions matter or what next slice should address them. Human publication is not the adaptation decision itself.
- Evidence: `factory-rsi/rig.yaml`; `factory-rsi.yaml`; `factory-rsi/dogfood/agent.yaml`; `factory-rsi/dogfood/guidance/role.md`; `docs/releases/v0.4.6.md`.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: v0.4.6 states that the exact continuous out-of-band runtime mechanism is refined in a later release. The positive mapping therefore relies on the shipped launchable dogfood seat plus its explicit autonomous role and planner-return contract, not on a claim that every cadence/trigger detail is already fully mechanized. Publication remains a separate human act and is not counted as S4 ownership.
- External distinction: observable behavior of the already-shipped OpenRig product under real user/operator-style use, outside the in-band build artifact and its QA/review loop.
- Future / prospective distinction: which product friction/default/affordance/assumption should become a later development slice rather than merely correcting the current in-band candidate.
- Adaptation option generated: prioritized durable dogfood findings and a planner-authored next buildable slice/spec derived from them.
- Path back into current capability / S3: the new slice enters the same first-party implementation/check/review/release pipeline; after publication, the changed shipped product becomes the capability exercised by later dogfood and operational cycles.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity / ultimate-policy closure is established at the declared OpenRig deployment recursion.
- Disturbance / variety regulated: rig culture, role guidance, workflow rules, permissions, release authorization, roadmap choices and topology policy exist, but none supplies a first-party S5 decision loop over the organization's enduring identity or ultimate policy with returned operational closure.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `CULTURE.md`, RigSpec/agent definitions, workflow gates, human release signoff, permissions, topology rules and maintainer-authored bundled skills were inspected as possible policy/identity surfaces.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: culture/configuration and workflow policy are pre-authored operating constraints; the factory human release gate authorizes publication of a prepared candidate but does not decide the rig's ultimate identity/policy. Repository-maintainer changes are contributor governance outside the assessed runtime organization unless a first-party return loop is separately established.
- Evidence: `first-project/CULTURE.md`; `factory-rsi.yaml`; bundled role/skill and topology policy surfaces; repository release/governance material inspected at the pinned revision.
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a human can steer factory work through the roadmap and approve release, but generic steering/approval is not S5 under the Profile.

### Absence scope

- Surfaces inspected: RigSpec/culture files, bundled agent identity/role definitions, permissions and human-in-loop guidance, release-signoff gate, topology mutation policy, workflow invariants and repository-level release/maintainer governance.
- Plausible first-party paths checked: culture amendment, agent/role identity change, human release approval, roadmap steering, topology authority and maintainer publication of bundled policy.
- Why no material first-party path remains: the runtime surfaces constrain or authorize operations/adaptation, while repository-maintainer governance lies outside the assessed running rig; no supported mode closes an identity/ultimate-policy issue through a legitimate S5 authority and returns that decision as the governing identity/policy of subsequent rig operation.

## Recursion

The assessed recursion is one OpenRig rig/deployment. Managed coding-agent seats are operational S1 units. An orchestration seat can regulate the rig's current portfolio as S3; separate QA/review seats can audit operational claims as S3*; and in the shipped factory-rsi mode a dogfood/planner relation adapts future product capability as S4. OpenRig can itself be embedded inside a larger human or organizational recursion, but this assessment does not import functions from that parent unless a first-party parent loop is operationally closed.

## Variety and escalation

OpenRig absorbs operational variety through persistent agent sessions, explicit role/context injection, durable work custody, queue transitions, workflow routing, multi-host transport and live topology changes. S3 adds whole-rig current regulation over blocked/idle/misassigned work; S3* introduces an independent evidence path before continuation; factory-rsi S4 adds an outside-and-then channel from shipped-product use to future capability change. Exceptional workflow failures and blockers route to the orchestrator or, where configured, a human gate. Those escalation channels are mechanisms and do not create an additional VSM function by themselves.

## Evidence gaps

- The pinned v0.4.6 release explicitly marks the exact continuous out-of-band dogfood runtime mechanism as a follow-on refinement. The shipped seat/role/next-plan semantics establish the reviewed S4 mode, but a future reassessment should verify whether later runtime automation strengthens or materially changes that closure.
- No sufficiently specific pinned witness was found for S2 under the current disturbance-specific threshold. A future positive S2 claim should identify the sibling S1 units, concrete interaction-generated interference, attenuation relation and returned change in later sibling behavior rather than rely on queue/messaging/topology names.
- Preview product-team compositions contain richer organizational structure but are not required for the present vector and were not used to upgrade any state.