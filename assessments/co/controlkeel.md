---
harness_id: controlkeel
project_name: ControlKeel
repository: https://github.com/aryaminus/controlkeel
review_ref: 1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ControlKeel

## Review boundary

- System in focus: the shipped ControlKeel local/cloud agent control plane, CLI/MCP integration, task execution wrapper, governance, memory, evidence and optional scheduled dispatch, rather than the separate coding agents it governs.
- Purpose and identity: turn organization/user engineering intent into executable checks, review gates, evidence, memory, and governable delegated agent runs.
- Relevant environment: host coding agents (Claude Code, Codex, OpenCode, etc.), project repositories, operators/reviewers, CI/eval subjects and optional hosted workspaces.
- Standard-distribution boundary: Phoenix/Elixir CLI, MCP tools and API, installed host attachments/hooks, `Agent.Execution`, `Platform`, opt-in scheduler/launcher, local observability and skill-evolution tools. External model-host agent binaries and their internal reasoning loops are dependencies outside this first-party boundary.
- Credited operating / distribution surfaces: `README.md`, `docs/getting-started.md`, `docs/control-plane-architecture.md`, `docs/autonomy-scheduler.md`, `lib/controlkeel/agent/{execution,router,autonomy_loop}.ex`, `lib/controlkeel/autonomy/{scheduler,dispatcher}.ex`, `lib/controlkeel/platform.ex`, `lib/controlkeel/mission.ex`, `lib/controlkeel/observability.ex`, MCP review/validation and exported host hooks.
- Adjacent first-party surfaces excluded from ownership: benchmark fixtures and scoring, developer CI/release, hosted marketing UI, package build machinery, tests, examples, contributor policy discussion. These corroborate features but are not an agent decision loop.
- First-party operating / deployment modes considered: local attached host/MCP, CLI direct/handoff/runtime delegation, embedded external executable dispatch, optional timer-driven autonomy wake-up with shell launch explicitly enabled, local and cloud/self-hosted governance, operator-gated review/eval/skill evolution.
- Recursion level: one ControlKeel-governed engineering workspace/session and its first-party control plane; an attached coding agent is an external operational organization, not an internally implemented S1.
- Reviewed revision: `aryaminus/controlkeel@1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d`; frozen intake #2473/controller #2474 row 2, historical #188 row 7.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/README.md) expressly positions ControlKeel *between* coding agents and production. [Architecture](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/control-plane-architecture.md) describes the Phoenix/Ecto state layer, deterministic scanner, host hooks, findings/reviews/proofs, policy snapshots, precedent, budgets, outcomes and observability. MCP tools and exported host integration inject constraints and return findings to an external model-driven host. They do not implement the host's task-semantic reasoning/tool loop.

[Agent.Execution](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/agent/execution.ex) is a genuine shipped delegated-run wrapper, not merely an advertised API: it selects an installed *external* `claude`, `codex`, `opencode`, `aider`, etc. executable; checks review/policy and task claims; builds a run package; launches it via [ExecutionSandbox](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/agent/execution.ex#L433-L553); then validates, records and reports output. A `run_session` processes ready/queued tasks in order. [Agent.Router](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/agent/router.ex) has configured capability/cost/security tables, not a first-party model planning loop. [Agent.AutonomyLoop](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/agent/autonomy_loop.ex) computes deterministic bottleneck/ownership summaries and recommendations from session evidence.

[Scheduler documentation](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/autonomy-scheduler.md) explicitly says the scheduler is off by default and never starts in MCP stdio mode. The [dispatcher](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/autonomy/dispatcher.ex) persists operator-configured objective/session/task/audit rows, then optionally launches a configured external program. Its periodic heartbeat supplies timing and recoverability, not new task-semantic autonomy. [Observability](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/observability-feedback-loop.md) clusters traces, proposes deterministic regression scenarios and can install a derived skill only on explicitly invoked `install=true` after validation; [skill-evolution code](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/mission.ex#L1945-L2050) does not establish an autonomous externally prospective change authority.

Counterfactual owner test: remove Claude/Codex/OpenCode and other external coding agents, leaving CK's database, task graph, CLI/MCP/host exports, scanners, scheduler, routing tables, direct-executable wrapper, reviews, memory and benchmark suite. The remaining control plane can create jobs, gate proposed actions, persist evidence, recommend host selection and launch configured processes, but it cannot interpret an open-ended engineering request, choose its next semantic code/tool act from observations and decide completion. That loop belongs to the **external agent**. This is materially analogous to a governance adapter, not a first-party autonomous S1 harness. The terminal admission outcome is therefore **`excluded-no-agentic-vsm`** despite substantial governance features.

## Operational model

An operator or attached agent establishes tasks and reviews; CK translates policies, evidence and host-attachment state into pre-tool gates and memory. A configured delegate may invoke an external coding-agent CLI, after which CK checks results and persists proof/findings. Reviewers decide plan approval; a configured scheduler can wake up a session; evals can suggest future checks. The externally supplied model agent owns semantic execution. CK's enforcement, observability and optional operator configuration must not be relabeled as autonomous S1–S5 ownership. No local external agent run or cloud integration test was executed.

## S1 — Operations

- State: —
- Function: substantive autonomous engineering task execution would entail deciding code, tests, tool calls and completion from changing repository evidence.
- Disturbance / variety regulated: open-ended bugs, repository state, tool failures and changing requirements; CK itself regulates task metadata, budgets, reviews, security/proof and external-executor lifecycle.
- Decisive decision or feedback right: decide what semantic code/tool action to take after each result and whether the engineering objective is complete.
- Decision owner: an attached or launched *external* coding-agent host; operator/configuration chooses the task and allowed host.
- Supporting / enforcement mechanisms: `Agent.Execution` package/dispatch, configured executable, sandbox, host hook/MCP, task claims, review gates, deterministic scans, session memory and optional scheduler.
- Closure path: task → CK gate/package → external `codex`/`claude`/`opencode` agent → repository/tool observations → **external agent** next act → result → CK validation/finding. CK closes enforcement/reporting, not semantic operating decisions.
- Why this is / is not agent-owned: `run_task` does not contain a first-party model planning or tool-selection loop; source code calls installed other-agent programs and receives their output. The opt-in scheduler only dispatches an operator-authored task.
- Evidence: [execution module](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/agent/execution.ex); [scheduler docs](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/autonomy-scheduler.md); [architecture](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/control-plane-architecture.md).
- Basis: explicit + structural negative.
- Confidence: high.
- Caveats: CK can genuinely **run** a separate agent; operational orchestration is not ownership of that agent's model decisions.

### Absence scope

- Surfaces inspected: product/host docs, `Agent.Execution`, `Agent.Router`, scheduler/dispatcher, mission/task graph, MCP/host export and observability/skill-evolution paths.
- Plausible first-party paths checked: direct embedded/handoff delegation; auto-router; timer-owned jobs; model-provider memory/embedding helpers; skills generated from traces. None selects and revises semantic repository acts within a CK-owned model/tool agent loop.
- Why no material first-party path remains: every supported open-ended work mode invokes or attaches a separate model agent; CK owns invocation, enforcement and reporting rather than the agent's substantive work.

## S2 — Coordination

- State: —
- Function: attenuate actual peer S1 interference/oscillation between autonomous operating units at the assessed recursion.
- Disturbance / variety regulated: task dependencies, sequential delegation, shared policy findings, possible ownership concentration; those are represented but not evidenced as a distinct inter-S1 coordination feedback loop.
- Decisive decision or feedback right: resolve a specific conflicting interaction between two CK-owned autonomous S1s and return a revised coordination rule to both.
- Decision owner: CK has no credited first-party autonomous S1 pair. Task graph constraints and reviewers own ordering/enforcement, external agent hosts perform work.
- Supporting / enforcement mechanisms: `Platform` task edges/readiness, sequential `run_session`, task claims, review/budget gates, deterministic ownership-concentration diagnostics.
- Closure path: session tasks → graph readiness → ordered external calls and task statuses; no source-grounded peer interference → coordination decision → both S1 subsequent behaviour path is established.
- Why this is / is not agent-owned: ordering, dependency edges and bottleneck findings are not conflict-specific S2 rights.
- Evidence: [task execution](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/agent/execution.ex#L145-L224); [task graph](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/platform/task_graph.ex); [autonomy-loop diagnostics](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/agent/autonomy_loop.ex).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: a composed multi-agent organization might use CK for peer coordination, but it is not shipped as CK-owned S2.

### Absence scope

- Surfaces inspected: `Platform` task graph, session execution, router, autonomy diagnostics, delegated-run dispatch and orchestration docs.
- Plausible first-party paths checked: dependency-based ready tasks, shared workspace state, agent routing, concentration findings and serial ordering.
- Why no material first-party path remains: no distinct first-party S1 units or conflict-specific attenuation plus feedback into those units; the inspected paths are lifecycle/routing or advisory signals.

## S3 — Inside-and-now control

- State: —
- Function: regulate current commitments/resources of a whole viable CK-owned agent operation, beyond local task/proof enforcement.
- Disturbance / variety regulated: over-budget tasks, unsafe edits, blocked approvals, unready proofs and workload concentration.
- Decisive decision or feedback right: choose and revise whole-system current priorities, resource trade-offs and interventions in response to an operating portfolio.
- Decision owner: human operators/reviewers define policy, budget and tasks; CK's validators and `Platform` enforce preselected limits. No CK agent exercises whole-system discretionary S3.
- Supporting / enforcement mechanisms: `ck_budget`, `ck_review_submit`/feedback, findings, task claims, scoped workspace dashboard, auto-loop bottleneck scoring and proof-readiness decisions.
- Closure path: external agent attempt → CK deterministic checks → allow/block/finding/approval request → operator or same external agent adjusts task. That is scoped enforcement, not first-party agent-owned whole-system control.
- Why this is / is not agent-owned: `Agent.AutonomyLoop` produces scored recommendations and findings but does not autonomously decide/reallocate cross-task commitments. Parent reviewers can intervene in individual plans, not a reconstructed whole-system S3 parent mode at this boundary.
- Evidence: [architecture enforcement table](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/control-plane-architecture.md); [autonomy loop](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/agent/autonomy_loop.ex); [review/findings](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/autonomy-and-findings.md).
- Basis: structural negative with explicit operator boundary.
- Confidence: medium-high.
- Caveats: powerful enforcement and dashboards are material governance, but do not themselves convey S3 decision ownership.

### Absence scope

- Surfaces inspected: task claims, budget/review gates, security workflow, dashboards, autonomy diagnostics, operator modes and workspace governance docs.
- Plausible first-party paths checked: current whole-workspace task view → operator review, cost/finding bottleneck recommendation → change of commitments; no evidence of an authorized whole-system S3 decisor with return beyond local task/config changes.
- Why no material first-party path remains: the shipped path gates or reports externally chosen work; no CK-owned autonomous S3 or independently evidenced parent whole-system resource/priority closure is established.

## S3* — Complementary audit

- State: —
- Function: independent, complementary reality access to challenge normal operation's account for whole-system current control.
- Disturbance / variety regulated: misleading success/proof claims and unsafe code changes.
- Decisive decision or feedback right: an independent auditor judges raw operating evidence and returns corrective findings into system governance.
- Decision owner: deterministic validation/proof checks under configured rules, benchmark subjects, human reviewers; no separate first-party auditor agent with sufficiently independent audit judgment and returned correction.
- Supporting / enforcement mechanisms: deterministic `ck_validate`, diff/artifact snapshots, findings, trace/proof bundles, regressions, benchmark scoring and human plan feedback.
- Closure path: action/artifact → routine CK scanner/eval/proof → finding or human review → task gate. This is the ordinary mandatory operational assurance chain rather than an independent complementary audit channel.
- Why this is / is not agent-owned: independent *data snapshots* and replayable evidence are useful, but the actual judgment remains deterministic routine policy or human review, not separately controlled S3* authority.
- Evidence: [findings and review architecture](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/autonomy-and-findings.md); [feedback-loop limitations](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/observability-feedback-loop.md); [promotion implementation](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/observability/promotion.ex).
- Basis: structural negative.
- Confidence: medium.
- Caveats: separate human audits or additional external evaluators may be composed by operators; no shipped independent corrective audit ownership was evidenced at CK recursion.

### Absence scope

- Surfaces inspected: scanner/hooks, policy/artifact provenance, proof scoring, observability regression/eval paths and human review disposition.
- Plausible first-party paths checked: artifact-independent hashes, raw findings, reviewed plan and benchmark traces; distinguish ordinary success checking from independent complementary audit authority.
- Why no material first-party path remains: these are in-path checks, replayable reports or external-human judgments, without a distinct first-party independently owned S3* audit-and-return loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: sense external future-relevant shifts, develop alternatives and decisively adapt current operating capability.
- Disturbance / variety regulated: recurring failure modes, regression risk, host/provider choices and future policy drift.
- Decisive decision or feedback right: choose prospective changes to model/tool/skill/policy capability from external and future alternatives, with feedback into subsequent operation.
- Decision owner: humans review eval candidates/promotions and explicitly invoke installation; deterministic counters/draft tests compute recommendations. CK does not own autonomous prospective adaptation.
- Supporting / enforcement mechanisms: `OutcomeTracker`, failure clusters, eval candidates/benchmarks, `Observability.Promotion.evaluate`, `ck_skill_evolution` validation and optional skill installation, configured router weights.
- Closure path: past trace → deterministic cluster/draft/regression/promotion advice → **operator**-selected review/install → changed host skill or deterministic rule for later external-agent runs. This is retrospective evidence and deliberate operator action, not a first-party externally prospective S4 regulatory loop at the assessed boundary.
- Why this is / is not agent-owned: no model-driven prospective option selector and no automatic change to current agent capabilities; the source explicitly keeps policy/skill evolution behind tests and explicit activation.
- Evidence: [observability loop](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/observability-feedback-loop.md); [promotion policy](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/observability/promotion.ex); [skill validation and installation](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/lib/controlkeel/mission.ex#L1945-L2050).
- Basis: explicit + structural negative.
- Confidence: medium-high.
- Caveats: the human-reviewed regression-to-skill route is a material improvement workflow; it should not be erased as nonexistent, nor promoted to autonomous future intelligence.

### Absence scope

- Surfaces inspected: `Agent.AutonomyLoop`, OutcomeTracker/observability, eval candidates and promotions, benchmark generation, skill-evolution validation/installation, router.
- Plausible first-party paths checked: recorded outcomes → new evals → promotion; failure clusters → skill document; adaptive routing weights.
- Why no material first-party path remains: these are deterministic/retrospective or human-invoked changes and do not establish external-and-future autonomous adaptation or a separately legitimized parent strategic S4 closure at the chosen CK agent recursion.

## S5 — Policy and identity

- State: —
- Function: establish and settle identity/ultimate-policy decisions for the viable CK-owned agent organization.
- Disturbance / variety regulated: organizational policy disagreements, acceptable action boundaries and security/regulatory risks.
- Decisive decision or feedback right: legitimate identity-level policy settlement and binding return into the operating agent organization.
- Decision owner: outside human/enterprise administrators and pack authors; CK stores/configures/enforces their policy choices. Ordinary task approval is not an identity decision.
- Supporting / enforcement mechanisms: domain packs, policy snapshots, workspace policy sets, role/permission checks, approval/audit rows and human review.
- Closure path: operator-defined policy pack → deterministic CK validation/hook enforcement → external agent action gate. The external human authority is not a first-party deliberative S5 decision/return loop at the assessed autonomous-agent recursion.
- Why this is / is not agent-owned: policy versioning, admin authorization and checks preserve governance constraints but do not autonomously decide ultimate identity or settle S3–S4 tension.
- Evidence: [control-plane architecture](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/control-plane-architecture.md); [agent/task spec governance](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/agent-specs.md); [review gates](https://github.com/aryaminus/controlkeel/blob/1815d3ca7fd9bfdf944f30150aa8179b6f8eef6d/docs/autonomy-and-findings.md).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: enterprise administrators may maintain real parent policy for a *larger* organization; it is not imported as autonomous CK S5 in this first-party assessment.

### Absence scope

- Surfaces inspected: policy pack/configuration and review tools, workspace org permissions, task specs, finding audit, host exports and operator mode.
- Plausible first-party paths checked: policy set update → enforcement; reviewer disposition → resumed task; admin role → workspace rules.
- Why no material first-party path remains: binding enforcement of externally selected policy is not the decisive identity-level arbitration and return loop; no first-party CK-owned S5 decisor is shipped.

## Distributed OSS parent arrangement

Contributors, package maintainers, workspace administrators and reviewers can change releases, packs, task approvals and agent integration, but repository-visible governance is not evidence of a separately integrated parent S3/S4/S5 system at the assessed CK-operated agent recursion. The source boundary is the product distribution, not the developer organization. No `(P)` mode is claimed by transfer from routine approvals or contributor decisions.

## Recursion

Individual coding-agent CLIs may themselves be viable autonomous S1 organizations, and CK workspaces can govern many sessions. They are **external** independent systems, not nested first-party CK operations simply because launched through CLI/MCP. Task graph nesting and cloud tenancy do not prove recursed viability.

## Variety and escalation

CK attenuates risk variety with policy checks, workspace isolation, proof gates, review status, precedent and budgets. Unresolved findings and high-impact actions reach operators or external agent hosts; audit events preserve history. An exceptional finding/status is a potential escalation signal but is not an independent VSM function or proof of an algedonic channel with a whole-system decision owner.

## Evidence gaps

No live external-host run or cloud deployment was performed. The pinned repository contains multiple exported host adapters; internal model/agent logic of those separately installed products was deliberately not imported. A hypothetical future CK-native agent loop would need fresh source evidence and a different inclusion review. The bounded absence conclusions concern this pinned shipped first-party boundary, not the absence of agentic activity in teams using CK.
