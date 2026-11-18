---
harness_id: gascity
project_name: Gas City
repository: https://github.com/gastownhall/gascity
review_ref: 03f6fe825cf0a54c677c241e4aaa7e76dade28a5
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
assessment_changed_at: 2026-11-18
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Gas City

## Review boundary

- System in focus: a first-party **Gas City** city/deployment initialized from the supported binary, using the bundled core pack, a configured coding-agent provider, one or more rigs, agent sessions, workflow formulas, bead-backed job/state records, orders, and the city controller/reconciler at the pinned revision. This is **not** Gas Town and does not import its historical accepted vector.
- Purpose and identity: provide an installable, role-neutral orchestration platform for coding agents that turns tasks into durable formula/bead graphs, starts configured model-driven workers, coordinates their execution, permits developer-composed independent reviews, and gives a human operator an observable and controllable city.
- Relevant environment: user-supplied source repositories and tasks, Git branch/worktree state, external Claude/Codex/Gemini/other model CLIs, credentials and provider availability, concurrent workflow and agent sessions, repository quality checks, GitHub PR/CI endpoints where explicitly configured, and changes to model/runtime provider APIs.
- Standard-distribution boundary: released first-party `gc` binary and its **bundled core pack**; `gc init` with documented `--template gascity` and a configured real external agent provider; backed first-party beads/formula/controller/session infrastructure and documented optional composition. The role-neutral core requires operator/provider input and does not embed model inference. Optional upstream packs are relevant only when their first-party binding is documented and installed by the supported path; an arbitrary third-party pack, user's custom formula, developer dogfood or foreign PR must not donate a stronger default owner.
- Credited operating / distribution surfaces: [quickstart](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/quickstart.md), [orchestration primitives](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/how-gas-city-works.md), [bundled core pack](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/pack.toml), [single-agent task formula](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-do-work.toml), [scoped workflow formula](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-scoped-work.toml), [formula branch/preflight contract](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-polecat-base.toml), [review-quorum constructor](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-review-quorum.toml), [orders](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/tutorials/07-orders.md), [city status](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_status.go), [agent suspend/resume](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_agent.go), [configuration editor](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/configedit/configedit.go), [reload](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_reload.go), [runtime registry](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/runtime_registry.go), and [API/operator controls](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/reference/api.md).
- Adjacent first-party surfaces excluded from ownership: Gas City source repository's contributor/CI/release review, issue/PR governance, future feature proposals, benchmarking, development-only test actors, test fixtures, external Gas Town product/pack behavior not installed at the declared boundary, and external provider/model vendors. The bundled `control-dispatcher` is explicitly [deterministic with `prompt_mode = "none"`](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/agents/control-dispatcher/agent.toml); do not credit it as a model-owned manager.
- First-party operating / deployment modes considered: default city initialization with a valid model CLI provider and one rig; an ordinary `gc sling` task through `mol-do-work`; independently routed steps in formulas v2; opt-in scoped/branch and review-quorum formulas; operator `gc status`, `gc agent suspend/resume` and `gc reload`; schedule/event/condition-driven orders; pack/provider overrides; self-hosted dashboard/API mode. No new user-defined S4/S5 policy engine or unmerged original PR is counted.
- Recursion level: one Gas City installation and its deployed city as the assessed organization, with rig scopes and worker sessions treated as internal operational units. A rig or an imported pack is not automatically a separately viable recursion.
- Reviewed revision: `03f6fe825cf0a54c677c241e4aaa7e76dade28a5` ([pinned commit](https://github.com/gastownhall/gascity/commit/03f6fe825cf0a54c677c241e4aaa7e76dade28a5)).
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Gas City is a Go orchestration SDK / platform, but the supported binary can operate an actual model-led coding-agent workflow rather than only exposing an empty library. The [README](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/README.md) and [quickstart](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/quickstart.md) show an installed `gc init --template gascity --default-provider claude`, `gc rig add`, and `gc sling <rig>/<provider> ... --on mol-do-work` loop: a launched model-driven session reads a task, performs coding work and writes a result. The source of agent discretion is the configured external model; the core first-party workflow provides a reachable role/task/feedback boundary for that agent in the standard deployment.

The [architecture](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/how-gas-city-works.md) defines six product primitives (Agent, Bead, Formula, Rig, Pack, Event), distinct from VSM S1–S5. Agents are declared configuration, not hard-coded Go job titles; formulas materialize durable beads and independently routable steps; the orchestrator executes dependency and review gates, retry/drain paths, and agent lifecycle; orders dispatch formulas or shell work on event/condition/schedule triggers. The [bundled core pack](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/pack.toml) ships worker-facing instructions, `mol-do-work`, `mol-scoped-work`, review-quorum construction and housekeeping orders. The [control-dispatcher](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/agents/control-dispatcher/agent.toml) is a configured but **non-LLM deterministic command**, so its work cannot by itself confer agent autonomy.

Operator configuration and the current reconciler are distinct: a [config editor](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/configedit/configedit.go) validates and writes provider and agent settings, [status](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_status.go) exposes current city/session conditions, [agent commands](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_agent.go) support explicit suspension/resumption, and [reload](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_reload.go) instructs the controller to apply configuration changes with guarded outcomes. Native runtime and [event history](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/engdocs/architecture/event-bus.md) provide observation/transport, but queueing, a timer, an event or a successful reload alone is not the organizational decision right. The [first-party roadmap](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/ROADMAP.md) and the original GitHub issue tracker are developer/contributor planning, not active S4 governance inside a user's city.

Primary source paths: `internal/bootstrap/packs/core/`, `internal/orders/`, `internal/config/`, `internal/configedit/`, `cmd/gc/`, `internal/runtime/`, `internal/worker/`; this assessment did **not** execute a live model provider, construct a city with real credentials, or complete a downstream migration.

## Operational model

The ordinary S1 actor is a developer-configured AI coding-agent session assigned to work for a rig. A second worker can operate concurrently on a separate task/worktree. The formula graph makes their stage readiness and prerequisites explicit and lets the orchestrator route resolved steps; these deterministic mechanisms constrain interference without autonomously judging all cross-worker priority/conflict cases. Developer-defined coordination formulas can use those first-party dependencies and result-return mechanisms. The optional review-quorum formula supplies a specific two-lane complementary review construction, but the developer still selects reviewer/synthesis targets and an actual lifecycle consumer.

The human operator has a **whole-city** status and explicit current intervention controls; this provides a narrower parent-governed S3 mode than a general model-owned management agent. No first-party standard city future-environment policy chooser or ultimate-identity/policy deliberation loop was established through the examined supported paths. External model choice, human workspace policy and contributor governance are not assumed to be S4/S5 decisions.

## S1 — Operations

- State: A
- Function: carry out an assigned software-development task as an autonomous coding agent and return an executable change or task outcome.
- Disturbance / variety regulated: ambiguous source task instructions, changing files/test failures, local development choices and discoveries while implementing the assigned bounded job.
- Decisive decision or feedback right: choose edits, tool commands, debugging and completion steps inside the assigned coding task, constrained by the formula and available tools.
- Decision owner: the configured model-driven agent executing the `mol-do-work` / supported standard work session; Gas City Go code schedules/records but does not choose the code edit.
- Supporting / enforcement mechanisms: `gc init`, `gc rig add`, `gc sling`, pack agent config, bead assignment, session runtime, model CLI and formula steps.
- Closure path: user task → `gc sling` materializes workflow/bead → agent session claims and executes `do-work` → produces code/result and closes task/step → durable bead/convoy completion returns to the workflow and operator.
- Boundary reachability: documented [quickstart](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/quickstart.md) and [bundled work formula](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-do-work.toml) are shipped through the standard `gc` install/pack, not only a developer's test harness. The model CLI must be installed, authenticated and supplied by the operator; its inference is external, but its role in the first-party operational workflow is explicit.
- Why this is / is not agent-owned: without the model worker, the deterministic graph would not decide what code to write; removing it removes substantive operational discretion. Thus S1 is A in the supported agent-backed runtime, not an inference from deterministic scheduler behavior.
- Evidence: [README](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/README.md); [quickstart](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/quickstart.md); [core work formula](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-do-work.toml); [scoped work](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-scoped-work.toml).
- Basis: explicit + structural
- Confidence: high for supported modeled path, not a provider-backed live execution trace.
- Caveats: work done solely by a no-model deterministic exec order is not evidence of S1 agent autonomy; installed real provider is an explicit environment prerequisite.

## S2 — Coordination

- State: C
- Function: attenuate interference among distinct coding S1 units whose independent work can collide at repository/branch boundaries or when shared prerequisites are unresolved.
- Disturbance / variety regulated: overlapping work against a moving base branch, duplicate defect ownership, conflicting preflight fixes, simultaneous step completion and dependent work becoming ready before its prerequisite has closed.
- Decisive decision or feedback right: choose how to coordinate competing work, constrain readiness and return an intervention (e.g. deduplicate a pre-existing defect, choose rebase/branch handling, or hold a dependent step until the correct result exists).
- Decision owner: a developer-composed workflow/agent policy operating through the first-party S2-specific scoped work/branch/preflight and dependency interfaces, **not** the deterministic dispatcher alone. The preflight formula deliberately requires agent judgment of whether two symptoms represent the same defect.
- Supporting / enforcement mechanisms: isolated worktree/setup steps, named `needs` prerequisites, shared bead evidence, duplicate-issue lookup/comment path and formula graph readiness.
- Closure path: distinct worker tasks and preflight evidence → scoped formula recognizes a potential duplicate/pre-existing branch conflict → configured agent evaluates overlap or selects a safe branch continuation → records existing issue/comment or blocks/rebases the step → task graph and subsequent worker sessions see the changed readiness/evidence.
- Boundary reachability: shipped [`mol-polecat-base` preflight guidance](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-polecat-base.toml) says the matching-failure decision is **manual judgment**, and [`mol-scoped-work` formula](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-scoped-work.toml) exposes the required steps/edges in the first-party core pack. This is a function-specific constructor, not only a generic messaging or pool router.
- Why this is / is not agent-owned: the first-party stock graph handles mechanical ordering and isolation; it does not itself select all discretionary conflict/duplicate resolutions among simultaneously working agents. The developer supplies the coordinating actor/rules to establish the complete S2 owner in a configured deployment. Hence C rather than A.
- Distinct S1 units: separate configured agent worker sessions on different work/beads, potentially operating concurrently against one rig/repository.
- Inter-S1 disturbance: a collision between independently attempted fixes for the same defect or incompatible branches aimed at the same target, plus dependent stages racing unresolved results.
- Attenuating coordination relation: preflight cross-worker evidence check, worktree boundary and graph gates with agent-selected duplicate/branch disposition.
- Feedback into subsequent S1 behaviour: referenced existing bead or updated workflow/branch state changes what later workers implement/merge, preventing duplicate task expansion or premature access.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the cited first-party preflight directs the worker to distinguish same-failure collisions and react by reusing the existing issue, while graph dependencies contain conflicting step access. Merely posting a message or routing to a pool would not satisfy this witness.
- Evidence: [`mol-polecat-base`](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-polecat-base.toml); [`mol-scoped-work`](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-scoped-work.toml); [formula graph explanation](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/guides/understanding-formulas.md).
- Basis: explicit + structural
- Confidence: medium; no live two-worker conflict or completed coordination experiment was run.
- Caveats: only C is asserted, not a default agent-owned S2 across every possible rig, formula or pack; cases without the explicitly configured coordination path do not inherit the state.

## S3 — Inside-and-now control

- State: P
- Function: oversee current city-wide agent/session activity and intervene in present commitments/capacity through operator decisions that the first-party controller applies.
- Disturbance / variety regulated: session oversubscription, stalled or misconfigured workers, active-versus-suspended mismatch, present shared resource allocation and whether the city can continue its current work.
- Decisive decision or feedback right: determine whether a given worker/agent continues, is suspended, resumes or receives a changed current capacity configuration after inspecting the whole-city state.
- Decision owner: the **human city operator** in the first-party supported interactive/Supervisor mode; the reconciler mechanically enforces the returned choice. No model-owned whole-city regulator was established in this assessed boundary.
- Supporting / enforcement mechanisms: [`gc status`](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_status.go) current state and [operator API](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/reference/api.md), `gc agent suspend/resume` [commands](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_agent.go), `max_active_sessions` limits, [config editor](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/configedit/configedit.go), [reload](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_reload.go), and runtime reconciliation.
- Closure path: first-party city/session status → operator determines present capacity or agent intervention → `gc agent suspend`/`resume` or operator config edit → controller/reconciler updates effective desired state → affected current sessions are suspended/resumed/drained or subsequently scheduled accordingly → `gc status` exposes returned state.
- Boundary reachability: the [current city status CLI](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_status.go), [agent command entrypoints](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_agent.go), [API](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/reference/api.md) and [config/reload](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_reload.go) are first-party supported user-facing paths, not contributor-only CI or an external dashboard unattached to the running city.
- Why this is / is not agent-owned: remove the operator while leaving the deterministic status, scheduler and reconciler, and the selected strategic capacity/suspension decision is not made with the same discretion; reactive reconciler retries alone are enforcement. P records the first-party **closed parent supervision** mode, not an AI manager.
- Whole-system current view: status aggregated across installed rigs, configured workers, current sessions and running/held tasks, via city status/API.
- Current-control decision scope: agent current suspension/resumption, desired active capacity and what resources participate in the present city; *not* future model adaptation or ultimate institutional policy.
- Evidence: [status](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_status.go); [agent commands](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_agent.go); [API](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/reference/api.md); [config editor](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/configedit/configedit.go); [reload](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_reload.go); [reconciler architecture](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/engdocs/architecture/reconciler-v2.md).
- Basis: explicit + structural
- Confidence: medium; source-backed operator control and return, no independent live fleet trial.
- Caveats: parent mode is **per installed city**, not source-repository maintainer governance; there is no shown autonomous base S3 path, so notation is P, not A(P)/C(P). A generic agent invoking `gc` is not by itself a qualified constructor.

## S3* — Complementary audit

- State: C
- Function: conduct a suitably separate inspection of coding-work claims and return evidence-backed findings capable of challenging the producing worker's completion report.
- Disturbance / variety regulated: implementation defects, unsupported completion claims, missing tests, inconsistent reviewer judgments and errors that the producer's own self-review does not expose.
- Decisive decision or feedback right: choose whether the work satisfies independently inspected constraints, record pass/fail/blocked verdicts and synthesize divergent reviewer evidence into a durable disposition.
- Decision owner: developer-configured **distinct model reviewer lanes and synthesis agent** in the first-party `mol-review-quorum` formula; the core defines their review role and proof fields, but does not instantiate a universal independent audit actor for every workflow.
- Supporting / enforcement mechanisms: two read-only lane steps with separate declared target/provider/model, isolated read-only mutation baselines, durable `gc.output_json` findings and classification, synthesis step dependent on both lanes, retries and failure-class outputs.
- Closure path: implementation artifact/convoy → two independently routed reviewer lanes inspect diff/outputs → persist structured findings → synthesis agent reads both and emits quorum verdict and failure conditions → the calling formula/lifecycle owner may gate, repair or block downstream work using that durable verdict.
- Boundary reachability: the [bundled core's `mol-review-quorum` formula](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-review-quorum.toml) explicitly exposes lane one, lane two, and synthesis targets as required variables and records their results in first-party bead metadata. It is an intentionally function-specific audit **constructor**, not a hypothetical unshipped design PR.
- Why this is / is not agent-owned: each reviewer may make autonomous judgments when configured; however first-party standard setup supplies the audit protocol, not the complete independent reviewer configuration and consuming lifecycle gate. Thus C rather than a global A.
- Claim being audited: that a coding worker's changed repository artifact is sufficiently correct to progress or merge.
- Ordinary reporting path: worker's own completion/bead closure, self-review and implementation notes.
- Complementary access path: separate read-only diff inspection against a baseline by one/two declared reviewer lanes, with structured finding summaries.
- Independence boundary: distinct read-only reviewer sessions and supplied lane identities; developers must actually choose a non-producer target and ensure the reviewer reads source rather than the worker's self-declared verdict.
- Who acts on findings: separately composed synthesis/calling workflow actor receives the durable verdict and can prevent progression or return repairs; the formula does not claim that an external future `dx-review` integration already consumes it.
- Evidence: [review quorum](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-review-quorum.toml); [workflow outputs](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/guides/understanding-formulas.md); [bead/graph architecture](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/how-gas-city-works.md).
- Basis: explicit + structural
- Confidence: medium. Output contract is first-party and specific; exact downstream gate and independent actor identities must be supplied by adopter.
- Caveats: the formula notes the future `dx-review` consumer is not wired into lifecycle; do not count it as shipped review closure, nor treat ordinary unit CI as independent judgment.

## S4 — Outside-and-then intelligence

- State: —
- Function: anticipate meaningful external future changes and select adaptations that feed back into current capability.
- Disturbance / variety regulated: prospective model/provider availability, compatibility or environmental change affecting the future city.
- Decisive decision or feedback right: no first-party standard-distribution autonomous or parent-governed future adaptation choice with return into current capability established within the evaluated boundary.
- Decision owner: none supplied for this specific function; a human can edit providers manually, but that generic configuration right is not a shipped parent-mediated prospective adaptation decision loop.
- Supporting / enforcement mechanisms: scheduled and event-triggered [orders](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/tutorials/07-orders.md), model/provider [configurability](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/guides/configuring-an-agent.md) and [reload](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/cmd_reload.go) can transport changes; they do not generate prospective environmental alternatives and close a future choice by themselves.
- Closure path: no supported first-party future-signal → option selection → authorized capability revision → later-operation feedback chain established in the examined core distribution.
- Why this is / is not agent-owned: a configured general coding agent or scheduled health probe may react to current failures, but no bounded future-environment decision actor and return is supplied in the standard distribution.
- Evidence: [primitives](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/how-gas-city-works.md); [order triggers](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/tutorials/07-orders.md); [agent configuration](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/guides/configuring-an-agent.md); [runtime registry](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/cmd/gc/runtime_registry.go); [Gas City roadmap](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/ROADMAP.md); open [stale alias issue #8419](https://github.com/gastownhall/gascity/issues/8419), [quota issue #19](https://github.com/gastownhall/gascity/issues/19) and [unmerged reactive standby PR #8693](https://github.com/gastownhall/gascity/pull/8693).
- Basis: structural + bounded negative
- Confidence: medium within pinned core/standard mode.
- Caveats: this is a bounded no-material-path state, not proof S4 is impossible in a custom future pack or that no external operator can plan upgrades.

### Absence scope

- Surfaces inspected: documented standard city and pack architecture, bundled first-party formulas/orders, provider selection and config/reload, model alias/runtime registry, current controller/reconciler, current roadmap, original issue/PR overlap and event/feedback mechanisms.
- Plausible first-party paths checked: conditional/event orders, generic model-driven formulas, provider aliases, manual patches, current rate-limit recovery, standby-provider proposal and source-code change/reload.
- Why no material first-party path remains: none of the reviewed shipped paths owns an externally and prospectively grounded adaptation judgment with explicit lawful options and return of that decision into future capability. Event dispatch plus manual config alone is not future-adaptation ownership, and an unmerged reactive PR cannot fill the gap.

## S5 — Policy and identity

- State: —
- Function: define and maintain ultimate organizational identity and operating policy when conflicting operational/adaptation imperatives arise, and return the authoritative choice to running units.
- Disturbance / variety regulated: conflicts over which work and providers the city may legitimately operate, long-term identity or binding policy when coordination and current control demand competing choices.
- Decisive decision or feedback right: no first-party runtime identity/ultimate-policy deliberative authority with an explicit closed return to operations established in the assessed installed boundary.
- Decision owner: none supplied by the installed city. An operator configures allowed providers/credentials and can inspect/suspend the city, but generic configuration and external login are not sufficient S5 closure.
- Supporting / enforcement mechanisms: declared providers, credential/runtime controls, static agent config, human/manual command authority and workflow gates.
- Closure path: no qualifying first-party identity/policy issue → recognized supreme decision owner → authoritative policy return → ensuing operational change loop traced beyond generic configuration controls.
- Why this is / is not agent-owned: ordinary worker prompts, agent constraints, static provider options and GitHub contributor rules do not independently own and revise the city organization's ultimate identity.
- Evidence: [architecture](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/getting-started/how-gas-city-works.md); [agent settings](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/guides/configuring-an-agent.md); [config editor](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/configedit/configedit.go); [CLI/API controls](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/docs/reference/api.md); [review and workflow gates](https://github.com/gastownhall/gascity/blob/03f6fe825cf0a54c677c241e4aaa7e76dade28a5/internal/bootstrap/packs/core/formulas/mol-review-quorum.toml).
- Basis: structural + bounded negative
- Confidence: medium for the examined installed boundary.
- Caveats: no judgment is made on Gas City, Inc. governance, a user's custom external institutional policy or governance in a separate third-party pack.

### Absence scope

- Surfaces inspected: first-party city/agent/rig/pack schema and supported operator mode, runtime config, user-facing CLI/API, sample workflows/reviews, events, documentation and repository contributor policy.
- Plausible first-party paths checked: operator provider/credential configuration, static permission/run gates, manual city suspend/resume, generic human approval and the original's public maintainer roadmap.
- Why no material first-party path remains: these configure/stop/enforce or develop the product but do not supply a runtime ultimate-policy authority and a separate policy-resolution/identity decision returning into the assessed city. External maintainer governance is outside the deployed organizational boundary.

## Distributed OSS parent arrangement

Gas City source accepts many independently controlled deployments, and users may create independent cities with their own agents, credentials and policies. This review credits the **local city operator** for the S3 parent mode only because first-party status/commands return a concrete current control decision into that city. It does not transfer the external OSS maintainer's GitHub governance, project roadmap or another user's private agents into S3/S4/S5 ownership at this city recursion.

## Self-hosted and non-human modes

The source supports self-hosting and provider-configurable agent sessions. The operator may exercise legitimate city current control, which supports the bounded S3=P path above. The deterministic core with no human intervention does not become A merely because it can reconcile configured state; nor does the ability to construct an arbitrarily capable custom agent constitute shipped S4/S5. Optional fully autonomous non-human city deployments are not evaluated beyond source-reachable documented functions.

## Recursion

A Gas City deployment contains city, rig and worker-scope subdivisions; the first-party platform explicitly supports independent rig namespaces. However organizational subtyping, spawning of agent sessions, and formula nesting do not by themselves demonstrate full S1–S5 closure for each rig. The assessed unit is the city/deployment, not every rig.

## Variety and escalation

Beads and formulas amplify human/developer work intentions into parallel model-driven operations; dependency gates, scoped worktree actions, reviewer formulas, retries, operator suspension, session reconciliation and event streams attenuate conflicts, execution failure and excess capacity. Exceptional status and alert channels may notify an operator, but a status, warning or queue entry is not automatically an algedonic VSM channel; no additional S4/S5 ownership follows from them.

## Evidence gaps

- This is source-pinned structural assessment, **not** an independently executed live city: no model credentials or real provider-backed E2E coding/review trace was run in this evaluation. The first-party quickstart and core formula support S1 structurally; reviewer and S2 construction are documented shipped interfaces.
- The S3=P conclusion is specific to a local operator's whole-current status → intervention → controller return, not to default autonomous S3 or remote organization governance. An independent review might demand a narrower parent-loop proof before strengthening or changing this classification.
- S3* C depends on configured distinct reviewer identities and a real consuming gate; the standalone quorum file does not certify an active independent reviewer in every deployment, and its future `dx-review` integration is explicitly unshipped.
- The conservative S4/S5 negatives are bounded to the standard shipped first-party paths inspected; genuine new supported first-party future-decision or ultimate-policy routes at another frozen source revision would require reassessment.
- Current `gastownhall/gascity` maintainer issues and PRs cited as overlap do not constitute shipped evidence until merged and reachable. Cost reduction of VSM-guided modification has not been measured by this assessment.
