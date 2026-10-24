---
harness_id: purrcode
project_name: PurrCode
repository: https://github.com/Weilin0723/PurrCode
review_ref: 156d83206ed74a89398c0adf8d4fccd3e070ae59
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# PurrCode

## Review boundary

- System in focus: the published PurrCode local-first coding-agent **daemon/CLI with first-party `NativeAgent`**, its detached Git worktree actions, model-gateway and policy/judgment/validation pipeline; assess separately the installed daemon's optional supervisor API without borrowing third-party worker actors.
- Purpose and identity: autonomous repository-coding tasks under durable authorization, sandbox enforcement, evidence-backed validation and model-based separate judgment.
- Relevant environment: changing repository files/tests, user objectives and plans, Git worktrees, model providers, local host sandbox and resource caps, user approvals and external threat material.
- Standard-distribution boundary: shipped `purrcode` terminal/TUI, native desktop IDE, daemon-backed `NativeAgent` loop, tool execution/validation and supported daemon supervisor route. The IDE and TUI share the same daemon session rather than distinct autonomous organizations.
- Credited operating / distribution surfaces: `crates/agent-runtime` autonomous decision/observation loop, daemon production wiring, `crates/claw-sandbox` first-party actions, `crates/pawgate-runtime` deterministic authorization, `crates/contextual-judgment` model judgment, `crates/validation-runtime` and worktree observations, and the reachable `crates/supervisor-runtime` API as its actual one-shot worker implementation.
- Adjacent first-party surfaces excluded from ownership: .codex and contributor agents, build/release CI, tests/golden fixtures and eval-only actors, docs/prd/roadmap proposals, SDK wrappers, external model-provider internal agents, separate GitHub app workflows, deployment operator decisions and third-party extensions/skills not shipped as active owners.
- First-party operating / deployment modes considered: normal `purrcode run` and continuous CLI/daemon `NativeAgent` coding; plan/ask/review read-only modes; optional human approval; contextual action and outcome judgment; separately invoked `supervisor` endpoint with dependency-ordered, independent one-action worktree workers.
- Recursion level: one model-guided coding session is the positively established S1. The optional supervisor mode is considered separately at a potential multi-worker recursion; its API constructs **one model proposal/action per worker**, not a supported self-continuing independent coding-agent loop.
- Reviewed revision: `156d83206ed74a89398c0adf8d4fccd3e070ae59` (frozen intake #848; no repin).
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md) documents direct run/plan/resume, shared durable daemon sessions, worktree isolation, policy authorization and result validation. [crates/agent-runtime/src/agent.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/agent-runtime/src/agent.rs) contains the first-party `NativeAgent`, its `run_until_pause` model/action loop, provider streaming, tool proposals, constraint checks, action results, repair/validation continuation and bounded iteration limits. [crates/runtime-core/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/runtime-core/src/lib.rs) defines typed action, authorization, session and judgment records; [crates/repository-engine/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/repository-engine/src/lib.rs) gives a separate worktree and change-effect evidence boundary.

[crates/purrcode-daemon/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/purrcode-daemon/src/lib.rs) wires live provider routes and `NativeAgent::with_contextual_judge(...)`, including a potentially separate provider model (but same-model fallback is possible). [crates/contextual-judgment/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/contextual-judgment/src/lib.rs) evaluates action proposals separately from the coding worker and evaluates completed outcomes from validation evidence. [crates/agent-runtime/src/context.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/agent-runtime/src/context.rs) constructs outcome evidence using first-party worktree changed paths, patch digest and add/delete counts plus stage-by-stage validation receipts—not the entire raw patch. The judge can allow, replan, deny or require human review; [crates/agent-runtime/src/agent.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/agent-runtime/src/agent.rs) records its outcome and returns replan/denial/review to the active session rather than silently completing.

The optional [crates/supervisor-runtime/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/supervisor-runtime/src/lib.rs) manages independently scoped worker worktrees, dependency waves, budget and path-conflict reports. It is genuinely wired by the daemon `run_supervisor` path, but the installed [crates/purrcode-daemon/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/purrcode-daemon/src/lib.rs) `JudgedSupervisorWorker::execute` takes **one** structured-model turn and at most one policy-approved atomic action per worker; it has no independent model-result-model continuation. The supervisor report explicitly returns `IndependentReviewRequired` without conflicts or `ConflictsRequireResolution` with conflicting changed paths. This is an important non-equivalence between safe parallel work, fully autonomous child S1 units and an autonomous parent conflict-resolution/controller.

Policies and authorization are not decisions of ultimate organizational identity. `crates/runtime-core/src/adaptation.rs` selects Direct/Standard/Ultra workflow budgets/policies from current-task complexity and operator controls, not prospective external/future adaptation of the harness.

## Operational model

A user supplies a coding objective; the daemon initializes or resumes a model-driven session in a managed worktree. The coding model repeatedly chooses bounded actions, receives policy/approval decisions, executes first-party tools, sees returned execution evidence, and can repair or continue. At completion the runtime validates actual outcomes; separate model judgment may veto completion, request approval or force replanning. The autonomous operating decision owner is the coding model in the first-party session loop; policy and validation are constraints and independent observations, not substitute agent discretion.

An opt-in supervisor API can run several separately scoped one-shot model/tool worker actions and discover conflicting paths. However the caller supplies worker objectives and the merge report is returned for external review/resolution; its implementation is not evidence of several **continuing autonomous** S1s or closed autonomous S2/S3. This negative is specific to the shipped supervisor worker semantics, not the broader possibility of composing a full multi-agent harness from its types.

## S1 — Operations

- State: A
- Function: complete a bounded coding operation by adaptively deciding and executing task-specific repository actions from feedback.
- Disturbance / variety regulated: heterogeneous user requests, changed source/test state, tool errors, failed checks, constrained permissions, available model context and accepted plan revisions.
- Decisive decision or feedback right: choose/revise actual read/edit/command actions following observed execution and validation results; decide further repair or completion within outer limits.
- Decision owner: the configured model acting through PurrCode's first-party `NativeAgent` loop; external model API provides inference but not PurrCode's session/tool feedback organization.
- Supporting / enforcement mechanisms: daemon-owned session events, model gateway, deterministic PawGate authorization, worktree effects, tool runtime, execution/validation receipts, cancellation and bounded iteration/rejection budgets.
- Closure path: user task → active `NativeAgent` model turn → proposed action → independent checks/authorization → execution → event and validation evidence → subsequent model prompt/repair or terminal outcome.
- Boundary reachability: the shipped default `purrcode run` and daemon resume paths invoke `NativeAgent`, with the live contextual judge and first-party action/observation loop, not an external coding CLI or CI fixture.
- Why this is / is not agent-owned: the model decides task-specific next actions from changing observations; hard policy can veto but is not the semantic coding decision owner. Removing the model leaves authorization/execution tools but no independently chosen coding course.
- Evidence: [README.md](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md); [crates/agent-runtime/src/agent.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/agent-runtime/src/agent.rs); [crates/purrcode-daemon/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/purrcode-daemon/src/lib.rs); [crates/runtime-core/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/runtime-core/src/lib.rs).
- Basis: direct shipped loop and daemon construction.
- Confidence: high.
- Caveats: ask/plan-only or operator-driven approval modes need not continuously act on the workspace; they do not invalidate supported model-guided coding mode.

## S2 — Coordination

- State: —
- Function: no shipped autonomous inter-**continuing-S1** conflict/oscillation attenuation/returned work adjustment established at the selected multi-worker recursion.
- Disturbance / variety regulated: optional supervisor workers can edit overlapping paths; their worktrees isolate mutation and report path conflicts.
- Decisive decision or feedback right: choose/revise a specific inter-agent coordination action from those conflicts and return it into **subsequent adaptive behaviour of distinct operating S1s**.
- Decision owner: the built-in supervisor deterministically schedules dependencies and reports conflicts; the external API caller decides review or resolution. Each default supervisor worker is restricted to a single model proposal/atomic action and does not receive later conflict feedback for adaptive continuation.
- Supporting / enforcement mechanisms: isolated Git worktrees, dependency-wave ordering, caps on workers/requests/worktrees, changed-path conflict detection and `MergeDecision` report.
- Closure path: worker specifications → deterministic waves → one-action workers → changed-path report → `IndependentReviewRequired` or `ConflictsRequireResolution` to caller, **without** first-party model-owned rescope/retask loop returned to the workers.
- Why this is / is not agent-owned: conflict report and scheduling are valuable coordination **mechanisms**, but no first-party adaptive agent selects subsequent worker-resolution actions. Naming the route supervisor does not make it S2=A.
- Evidence: [crates/supervisor-runtime/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/supervisor-runtime/src/lib.rs); [crates/purrcode-daemon/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/purrcode-daemon/src/lib.rs); [README.md](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md).
- Basis: bounded source-negative for autonomous inter-S1 function (not absence of conflict detection).
- Confidence: medium-high.
- Caveats: an externally implemented multi-turn worker/parent agent using the `IsolatedWorker` interface might form S2; its autonomous decisions do not belong to this standard distribution.

### Absence scope

- Surfaces inspected: standard daemon supervisor route, `JudgedSupervisorWorker`, isolated worker worktree/status/conflict implementation, ordinary single-agent loop and integration reports.
- Plausible first-party paths checked: parallel supervised one-action model workers as independent S1s; isolation and path conflicts as disturbance; `IndependentReviewRequired`/conflict report returned to owner; potential automatic worker retasking or integration.
- Why no material first-party path remains: installed supervisor worker ends after a single proposal/action rather than looping on operation outcomes; its conflict report leaves resolution to the API caller, with no model-owned returned adjustments to subsequent distinct child S1 operations.

## S3 — Inside-and-now control

- State: —
- Function: no closed, discretionary whole-current control of a *multi-S1 operating organization* is established in the shipped modes.
- Disturbance / variety regulated: worker quota, model request budget, worktree capacity, failed dependencies and possible merges in supervisor mode; normal coding runtime has one continuing S1.
- Decisive decision or feedback right: observe the entire current population of S1 units and decide live reallocations/interventions/priorities and return revised commitments to them.
- Decision owner: operator submits worker objectives and limits; supervisor deterministically admits ready workers and reports results. Coding worker decides its own task-specific actions, not metasystem-wide allocations to other S1 units.
- Supporting / enforcement mechanisms: status/roster and consumed model requests, dependency-wave scheduler, governor, `SupervisorReport`, shared daemon state and client UI.
- Closure path: predefined worker spec → bounded dispatch/status → report to external caller; no internally acting whole-current model controller reschedules or negotiates operational commitments from returned worker outcomes.
- Why this is / is not agent-owned: deterministic resource caps and a component named supervisor do not perform discretionary current organizational judgment. A human launching or inspecting a report does not automatically establish first-party parent-governed S3.
- Evidence: [crates/supervisor-runtime/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/supervisor-runtime/src/lib.rs); [crates/purrcode-daemon/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/purrcode-daemon/src/lib.rs); [crates/runtime-core/src/adaptation.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/runtime-core/src/adaptation.rs).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: a separate higher-level model/operator system can own S3 using this engine as support, but that parent isn't packaged as part of the assessed loop.

### Absence scope

- Surfaces inspected: daemon supervisor routing, worker statuses, dependency scheduler, model budget limits, adaptive workflow profile selection and model session control.
- Plausible first-party paths checked: status/roster as whole-current view, one-shot supervisor as current allocator, adaptive workflow budgets as a controller, human approval/report consumption as parent-governed S3.
- Why no material first-party path remains: the implementation schedules externally authored worker specs under fixed limits and returns a report, without first-party authority selecting revised current commitments across an established population of continuing autonomous S1s.

## S3* — Complementary audit

- State: ?
- Function: plausible first-party complementary inspection of coding claims and outcomes using a separate evidence-citing model judge; whether it has sufficiently independent **direct operational reality** access and genuine audit-to-control, beyond mandatory in-band QA, is unresolved.
- Disturbance / variety regulated: coding agent's completion claim may diverge from repo changes, test evidence, safety constraints or accepted objective.
- Decisive decision or feedback right: a sufficiently separate observer judges direct outcomes independently of ordinary agent narration and returns a correction/veto to active regulation.
- Decision owner: an actual `ContextualJudge` model actor is instantiated by the daemon and called during action/outcome checks. Its model route can differ from the coding role but may fall back to the same model/provider; deterministic policy constrains its output.
- Supporting / enforcement mechanisms: `OutcomeJudgmentRequest`, validation receipts from `ValidationRunner`, `RepositoryEngine::effects`, patch digest/changed-path and line-count summary, cited evidence IDs, journaled `OutcomeJudgmentRecorded` and review/replan/deny states.
- Closure path: first-party validation/worktree summary → separate structured-model judgment → `Allow`/human review/`Replan`/`Deny` → session completion veto or further action. This is a real returned judgment path, but its independent evidence exposure is limited to summary/digest/validator details, not an independent raw-patch investigation, and its role remains on the normal completion path.
- Why this is / is not agent-owned: a model actually makes a separate substantive semantic verdict; however an *independent reviewer* label does not prove the VSM complementary audit function rather than in-band routine QA. The strongest plausible shipped route prevents confident `—`, while access and authority evidence does not yet establish full `A` or `C`.
- Evidence: [crates/contextual-judgment/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/contextual-judgment/src/lib.rs); [crates/agent-runtime/src/context.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/agent-runtime/src/context.rs); [crates/agent-runtime/src/agent.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/agent-runtime/src/agent.rs); [crates/purrcode-daemon/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/purrcode-daemon/src/lib.rs); [crates/validation-runtime/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/validation-runtime/src/lib.rs).
- Basis: specific unresolved supported first-party function boundary.
- Confidence: unknown.
- Caveats: a materially independent auditor reading raw artifacts against agent claims could qualify, but cannot be imputed from the current judge receiving summarized/evaluated evidence; no independent assessor of *this Index document* is being requested.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed externally and prospectively oriented strategic adaptation of PurrCode's organizational capabilities into current operation.
- Disturbance / variety regulated: future tool/host/provider trends, changing external threats and long-horizon opportunity.
- Decisive decision or feedback right: sense future external distinctions, generate options, choose/promote organizational capability changes and return to presently executing agent.
- Decision owner: developers/operators manage code, provider routes, skills and configurations; runtime complexity-based Direct/Standard/Ultra selection regulates **current task**, not independent future capability strategy.
- Supporting / enforcement mechanisms: environment inspection, provider discovery, skill store, adaptive workflow profiles, logs/memory, web/research tools and static configuration.
- Closure path: current task complexity selects current execution settings; external future intelligence → option generation → authorized capability promotion → operational feedback is not evidenced as a shipped first-party loop.
- Why this is / is not agent-owned: model choosing tools for the current coding problem and caching skill/provider data are not outside-and-then organizational adaptation.
- Evidence: [crates/runtime-core/src/adaptation.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/runtime-core/src/adaptation.rs); [crates/agent-runtime/src/agent.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/agent-runtime/src/agent.rs); [README.md](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md); [docs/architecture.md](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md).
- Basis: bounded absence.
- Confidence: medium-high.
- Caveats: future independent skill evolution or release-governance mechanisms need new first-party evidence.

### Absence scope

- Surfaces inspected: workflow profiles, environment/provider routing, skills/knowledge context, agent current-task planning, project docs and build/release workflows.
- Plausible first-party paths checked: automatic long-horizon tool/skill evolution, threat intelligence, retrospective provider assessment and runtime capability promotion.
- Why no material first-party path remains: surfaced adaptation is current-task execution-profile selection or maintainer/config work, with no external-future option-to-capability closure.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate organizational identity/policy dispute resolution loop shown at the single coding-session recursion.
- Disturbance / variety regulated: unsafe file/command actions, secrets, authority escalation, user approvals and model-provider conflicts.
- Decisive decision or feedback right: legitimately adjudicate a disputed collective purpose/ultimate policy and return a binding new rule to subsequent operation.
- Decision owner: human/operator-configured task and policy; PawGate deterministic grants and `ContextualJudge` semantic checks enforce decisions within those bounds.
- Supporting / enforcement mechanisms: `AuthorityMode`, action authorization digests, denied/require approval, sandboxing, operator controls, session journal and evidence.
- Closure path: existing policy/permission → allow/deny/approve action or pause task; no actual ultimate-purpose tension → legitimate parent identity decision → returned system-wide policy change.
- Why this is / is not agent-owned: the judgment model cannot relax hard policy; a user approving a risky coding step is not a separately closed S5 parent mode.
- Evidence: [crates/pawgate-runtime/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/pawgate-runtime/src/lib.rs); [crates/contextual-judgment/src/lib.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/contextual-judgment/src/lib.rs); [crates/agent-runtime/src/agent.rs](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/crates/agent-runtime/src/agent.rs); [README.md](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md).
- Basis: bounded absence.
- Confidence: high.
- Caveats: downstream institutions can supply legitimate governance as a separate system, not inherited by the first-party coding agent.

### Absence scope

- Surfaces inspected: hard PawGate policy, contextual independent judgement, human approval, authority/config modes, daemon/IDE controls, project maintainer docs.
- Plausible first-party paths checked: human permission gate as parent policy authority, model judge as S5 identity arbitrator, workflow mode selection as ultimate purpose change, external release governance.
- Why no material first-party path remains: available judgments operate within preselected task/security bounds and do not provide identity-level legitimate dispute-to-authoritative-return closure.

## Distributed OSS parent arrangement

The public development maintainers, host users and connected provider services are separate owners. Contributor PR/release governance and the `.codex` development actor are outside the shipped task-session agent. Initial operator configuration, control panels and human approval do not independently demonstrate parent-governed S3/S4/S5 closure.

## Self-hosted and non-human modes

The daemon operates a model-driven coding loop with local or remote providers and configurable judge routing. This is first-party S1 autonomy even when an external API provides model inference. Human approval limits action authority. The standalone supervisor route is implemented but its one-action-per-worker and external-review design matters for S2/S3; treating model calls as full recursive agents would overstate the standard distribution.

## Recursion

A normal daemon-backed coding session is the assessed autonomous S1 unit. An optional group of one-shot supervised worktree workers forms a bounded fan-out of delegated actions but does not automatically furnish a metasystem of distinct *continuing* S1 organizations. Daemon-wide multiple user sessions and IDE/TUI clients share infrastructure, not necessarily one autonomous collective.

## Variety and escalation

Variety enters through user tasks, source differences, evolving model/context content, allowed tools and validation failures. The agent's model decisions handle task variety while PawGate, worktrees, budgets, policy rejections and judgment bound it. Validation or independent-judge objections can pause/replan/escalate to human, a real exceptional path; that does not alone prove separate S3* or S5.

## Evidence gaps

- The separate `ContextualJudge` is live and can veto completion, but its outcome evidence contains changed paths, digest, counts and validator details—not a raw patch—so the complementarity and reviewer independence requirements of S3* remain a **specific open semantic question**.
- The optional supervisor uses first-party model workers, but each is restricted to **one** proposal/action and ends before its worktree conflict report; no automatic model-managed worker rescope/rework integration is established. Distinguish this from a full S1 team.
- No live provider inference/task benchmark was run. The assessment establishes source-level structure and supported paths rather than a measured quality/safety score.

## Assessment summary

**Proposed disposition: `included`** because shipped `NativeAgent` closes a first-party autonomous coding S1 loop. **Proposed vector:** `S1=A / S2=— / S3=— / S3*=? / S4=— / S5=—`. The independent model judge is acknowledged without mechanically awarding VSM S3*, and optional parallel one-action supervisor workers are not silently promoted into continuing S1 units or higher autonomous metasystems.
