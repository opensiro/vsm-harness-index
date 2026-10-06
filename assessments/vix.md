---
harness_id: vix
project_name: Vix
repository: https://github.com/get-vix/vix
review_ref: e68a25c7df685335f5a202844988d492fe3c1b16
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# Vix

## Review boundary

- System in focus: the first-party Vix coding runtime at frozen revision e68a25c7df685335f5a202844988d492fe3c1b16, including daemon-backed agent execution, first-party tools, workflow/stem-agent execution, subagents, scheduled jobs/watchers, sandbox/session state and bundled prompts/skills.
- Purpose and identity: perform software-engineering work interactively or through reusable workflows and unattended scheduled agent runs.
- Relevant environment: user objectives and approvals, project files/tests, model/provider responses, external web/CLI data, scheduled time/external poll results, workflow state and job runtime state.
- Standard-distribution boundary: the shipped Vix binary/daemon plus bundled defaults under internal/config/defaults. External model providers, MCP servers, shell programs, GitHub itself and user-authored workflow/job content are environment/dependencies and cannot donate ownership.
- Credited operating / distribution surfaces: internal/daemon agent/subagent/job/runtime paths; internal workflow execution; bundled Goal/Plan/heartbeat workflows; general/implementer/reviewer agents; jobs/workflow skills; standard coding, headless/job and supported daemon modes.
- Adjacent first-party surfaces excluded from ownership: repository CI/e2e/benchmarks and project-development activity except as evidence of reachable runtime behaviour.
- First-party operating / deployment modes considered: ordinary interactive coding; Goal workflow; Plan workflow; spawn_agent foreground/background subagents; daemon scheduled jobs including polling workflows; supported sandbox/provider/session modes.
- Recursion level: one Vix coding organization/run. Agent/workflow steps that own bounded engineering outcomes are operational units where materially distinct; scheduled job runs are separate operational instances at the deployment recursion.
- Reviewed revision: e68a25c7df685335f5a202844988d492fe3c1b16.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Vix runs a model-backed coding agent with first-party read/write/edit/bash/code-intelligence tools. Its subagent runtime can start independent conversations with their own LLM and tool sets, including background execution collected later through task_output. Workflow definitions can run agent, tool, bash and conditional steps, fork history, branch and impose budgets.

The shipped Goal workflow repeatedly runs a general operational agent, then invokes a separate verify agent when the worker signals completion. The verifier is explicitly described as independently auditing the completion claim. Its structured verdict is routed by deterministic workflow logic: pass wraps up; failure sends the verifier's feedback back to the pursue step for corrective operation.

Vix also ships a jobs skill and daemon scheduler. The agent can persist job specs directly, including cron/one-shot triggers, prompts and named or inline workflows. The documented polling pattern can sense external changes with a cheap bash step, conditionally invoke a model agent only when something changed, and scheduled runs can operate unattended in a project cwd with auto-write permissions. This is an intentionally exposed constructor for future/external adaptation loops, but the concrete environmental distinction, option-development objective and return policy are supplied in the composed job/workflow rather than being closed by one built-in adaptation owner.

## Operational model

The ordinary coding loop is agent-owned. Workflow routing, budgets, scheduler timers and job persistence are deterministic support. Spawned agents can be independent operational workers, but the standard runtime does not itself supply an S2-specific collision/oscillation regulator for arbitrary parallel writers.

Goal verification is complementary rather than ordinary self-report: the completion claim is made by pursue, then a distinct verifier receives the goal/current state and may reject it; rejection feeds evidence back into another pursue iteration. Scheduled jobs expose a prospective/external constructor, but a concrete S4 loop is authored/composed for the chosen environment.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify software to satisfy a coding objective.
- Disturbance / variety regulated: unfamiliar repository state, implementation choices, tool/test failures, context variation, provider responses and bounded delegated investigations/implementation work.
- Decisive decision or feedback right: choose substantive code/tool actions, interpret evidence and decide how to satisfy the engineering objective.
- Decision owner: the active model-backed Vix agent or a model-backed workflow/subagent step owning its bounded operational outcome.
- Supporting / enforcement mechanisms: daemon tool dispatch, sandbox/permission checks, workflow engine, session state, provider adapters, timeouts and budgets.
- Closure path: objective → agent selects coding/tool action → runtime executes and returns evidence → agent revises work until completion/blocking.
- Boundary reachability: the standard interactive agent, workflow agent steps and scheduled headless runs all invoke the shipped first-party model/tool runtime.
- Why this is / is not agent-owned: deterministic machinery carries/enforces actions; the model chooses the substantive engineering response.
- Evidence: [README.md](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/README.md); [internal/config/defaults/agents/general.md](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/agents/general.md); [internal/daemon/subagent.go](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/daemon/subagent.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: tools and workflows constrain the action surface without owning the coding judgment.

## S2 — Coordination

- State: —
- Function: no material standard-distribution path is established that specifically attenuates an evidenced interference/oscillation between distinct operational S1 units.
- Disturbance / variety regulated: no qualifying inter-S1 disturbance is placed under a first-party coordination loop.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: spawn_agent, background task IDs, task_output, workflow edges/forks, per-step budgets and separate threads transport/decompose work but do not themselves regulate a concrete peer-operational collision.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: models can delegate or run parallel children, but delegation/parallelism alone does not establish coordination; no standard collision/oscillation response with feedback into both/affected S1 units was found.
- Distinct S1 units: independent spawned agents or workflow/job agent steps can own bounded outcomes.
- Inter-S1 disturbance: simultaneous write-capable units could conflict in shared project state, but the reviewed standard path does not document a corresponding S2-specific attenuation relation.
- Attenuating coordination relation: none established beyond generic sequencing/routing/thread isolation.
- Feedback into subsequent S1 behaviour: no S2-specific collision result/negotiation path established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not; the inspected primitives remain generic delegation/workflow transport for this purpose.
- Evidence: [internal/daemon/subagent.go](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/daemon/subagent.go); [internal/daemon/tool_schemas.go](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/daemon/tool_schemas.go); [internal/config/defaults/config/workflow.json](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/config/workflow.json).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a custom workflow can serialize work, but static workflow ordering is not sufficient S2 evidence under the active Profile.

### Absence scope

- Surfaces inspected: subagent runtime/tool schema, background task collection, workflow defaults/engine-facing configuration, daemon thread/job/runtime paths and README-described parallelism.
- Plausible first-party paths checked: write-collision isolation, peer negotiation, conflict detection, reservation/locking, worktree-per-agent regulation and adaptive coordination feedback.
- Why no material first-party path remains: inspected standard primitives spawn, route, sequence and observe agents but do not tie a concrete inter-S1 disturbance to an attenuating coordination decision/feedback loop.

## S3 — Inside-and-now control

- State: —
- Function: no material autonomous or constructor S3 current-control loop is established at the declared standard boundary.
- Disturbance / variety regulated: no whole-system current operational disturbance is placed under a first-party supervisory decision right.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: workflow budgets/conditions, job scheduler state, timeout/auto-disable, task lists and user plan approval enforce or expose selected constraints but do not supply the required whole-system current-control discretion.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: ordinary agents own local task execution; deterministic workflow/scheduler machinery owns no discretionary whole-system S3 judgment, and the Plan approval gate occurs before execution rather than regulating a live operational whole.
- Whole-system current view: job/thread/workflow status surfaces exist, but no standard autonomous owner is wired to use them as a whole-system current-control view.
- Current-control decision scope: no qualifying standard owner/path established over current resource/commitment/priorities on behalf of the whole.
- Evidence: [internal/config/defaults/config/workflow.json](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/config/workflow.json); [internal/daemon/jobs/scheduler.go](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/daemon/jobs/scheduler.go); [internal/config/defaults/skills/jobs/SKILL.md](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/skills/jobs/SKILL.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: users can approve plans and manage jobs; those local/configuration interventions are not promoted to S3 without the Profile's whole-system current-control closure.

### Absence scope

- Surfaces inspected: Goal/Plan/heartbeat workflows, workflow budgets/routes, job scheduler/runtime state, subagents, user plan gate and daemon status surfaces.
- Plausible first-party paths checked: autonomous supervisor over active agents/jobs, adaptive resource/priority allocation, current commitment intervention and parent whole-system operational control.
- Why no material first-party path remains: identified controls are local, pre-execution, static/deterministic enforcement or generic state exposure rather than a closed whole-system S3 decision loop.

## S3* — Complementary audit

- State: A
- Function: independently audit an operational agent's completion claim against current project state and return gaps into corrective execution.
- Disturbance / variety regulated: false completion, missing requirements, unverifiable implementation or defects that ordinary worker self-report can miss.
- Decisive decision or feedback right: make an independent pass/fail audit judgment from direct project evidence.
- Decision owner: the model-backed verify/reviewer agent running in a distinct workflow step/context.
- Supporting / enforcement mechanisms: Goal workflow routing, structured JSON verdict, read/bash/code-intelligence tool access and deterministic pass/fail branch.
- Closure path: pursue agent signals complete → separate verify agent independently inspects current state → verifier returns pass/fail plus feedback → fail routes feedback into a new pursue iteration; pass allows wrap-up.
- Boundary reachability: Goal is a bundled standard workflow and its verifier/pursue routing is shipped in the default workflow configuration; reviewer agent/prompt is bundled first-party.
- Why this is / is not agent-owned: workflow code routes the result, but the separate model-backed auditor makes the evidence-based judgment.
- Claim being audited: the operational worker's claim that the requested goal is complete.
- Ordinary reporting path: pursue's completion signal and ordinary implementation/tool results.
- Complementary access path: a separate verifier/reviewer can read current repository state, run checks and form its own evidence-based verdict rather than trusting the worker transcript.
- Independence boundary: distinct workflow agent step/reviewer role with its own run context and evidence-gathering tools; the Goal verify prompt is explicitly an independent audit.
- Who acts on findings: deterministic workflow routing returns rejected-audit feedback to the operational pursue agent, which must address the gaps before signalling completion again.
- Evidence: [internal/config/defaults/config/workflow.json](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/config/workflow.json); [internal/config/defaults/prompts/goal/verify.md](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/prompts/goal/verify.md); [internal/config/defaults/agents/reviewer.md](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/agents/reviewer.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: S3* is credited to the independent evidence path and corrective return, not merely to the name "reviewer" or to ordinary self-tests.

## S4 — Outside-and-then intelligence

- State: C
- Function: construct recurring external/future sensing workflows whose model-backed reaction can develop and apply adaptation to the current project.
- Disturbance / variety regulated: future time-based needs and changing external conditions such as new pull requests, dependency/security changes, remote state or other polled events.
- Decisive decision or feedback right: the composed scheduled agent step can interpret newly sensed external evidence and choose an adaptive project response; the standard distribution exposes the sensing, gating, model-run and unattended-write path, while the concrete adaptation objective/authority is supplied by the composed job/workflow.
- Decision owner: constructor state — Vix supplies the function-specific first-party primitives and an autonomous general-agent runtime, but the developer/operator/creating agent must compose the concrete external distinction, prospective objective and return policy.
- Supporting / enforcement mechanisms: daemon cron/at scheduler, prompt resolution, bash polling, execute_if gating, workflow agent steps, auto-write permissions, timeout/budget controls and persisted job state.
- Closure path: composed external/time trigger → first-party polling/sensing step → conditional model-backed agent interprets the changed environment and develops a response → unattended workflow may write/act in project cwd → subsequent project capability/operation changes.
- Boundary reachability: the jobs skill and scheduler are shipped first-party; jobs run through the daemon as isolated headless Vix threads and can invoke named/inline workflows using the standard general agent.
- Why this is / is not agent-owned: the eventual reacting agent can be autonomous, but the standard distribution does not pre-close one concrete external-and-prospective adaptation conversation; composition supplies the environmental model/objective/authority, so the published base state is C.
- Evidence: [internal/config/defaults/skills/jobs/SKILL.md](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/skills/jobs/SKILL.md); [internal/daemon/jobs/scheduler.go](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/daemon/jobs/scheduler.go); [internal/daemon/job_runner.go](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/daemon/job_runner.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a reminder or event reaction alone is not S4; C rests on the first-party watcher/workflow construction path being specifically capable of sensing external/future distinctions, invoking an autonomous option-developing agent and returning action into project capability.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level conflict/proposal is routed through authoritative S5 closure.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: sandbox, deny lists, workflow deny_tools, permission/confirmation surfaces, prompts and configuration constrain local operation without becoming identity authority.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: agents operate within developer/operator-authored policy and cannot authoritatively redefine Vix's identity or ultimate governing principles.
- Evidence: [README.md](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/README.md); [internal/config/defaults/skills/jobs/SKILL.md](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/config/defaults/skills/jobs/SKILL.md); [internal/daemon/sandbox.go](https://github.com/get-vix/vix/blob/e68a25c7df685335f5a202844988d492fe3c1b16/internal/daemon/sandbox.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: human confirmation and permissions are operational safety decisions, not S5 by themselves.

### Absence scope

- Surfaces inspected: system/agent prompts, permission/sandbox/deny controls, workflows, jobs, hooks, configuration and user approval paths.
- Plausible first-party paths checked: autonomous constitutional revision, identity-policy escalation, parent identity governance and durable ultimate-policy return.
- Why no material first-party path remains: all observed governance-like surfaces regulate local execution or configuration; no identity/ultimate-policy issue-decision-return loop is wired.

## Distributed OSS parent arrangement

The assessed system is the Vix runtime/deployment, not the GitHub maintainer organization. Repository maintainers and project-development CI are not imported as runtime parent S3/S4/S5 owners.

## Self-hosted and non-human modes

Vix supports self-hosted daemon operation and local/remote providers. The positive S1, S3* and S4-constructor paths are available without a human runtime parent. User plan approval remains a supported interaction but is not used to manufacture a parent-mode S3 claim.

## Recursion

At one coding-run recursion, the active coding/workflow agent is S1 and Goal verification supplies S3*. At a daemon deployment recursion, separately scheduled agent runs can be operational instances; the jobs/workflow surface supplies an S4 constructor for externally triggered adaptation. No positive S2/S3 is inferred from plurality alone.

## Variety and escalation

S1 absorbs coding variety. Independent Goal verification can reject a completion claim and force corrective work. Future/external sensing can be composed through jobs/workflows, but the concrete adaptation loop remains constructor-owned. Workflow budgets, auto-disable, timeouts and permission brakes are enforcement/support, not higher-function owners.

## Evidence gaps

No ? state is required. The frozen source exposes the relevant runtime, independent verification and jobs/workflow construction paths directly; the inspected concurrency/current-control/policy surfaces are broad enough for the documented negative S2/S3/S5 conclusions.
