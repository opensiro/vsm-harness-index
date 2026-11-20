---
harness_id: argentgo
project_name: argentgo
repository: https://github.com/2118505078xyh1/argentgo
review_ref: 0230ad0cff78aee5c97d182b62f753e2fdb85d71
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# argentgo

## Review boundary

- System in focus: The argentgo coding runtime and its first-party operator interfaces.
- Purpose and identity: Perform and resume model-driven software tasks with observable workspace changes.
- Relevant environment: Operator, local development workspace, Git state, provider endpoints and configured tool services.
- Standard-distribution boundary: CLI, TUI, native GUI bridge, RPC/ACP protocol paths, and first-party agent/workflow code. Caller-supplied tools and model services are dependencies.
- Credited operating / distribution surfaces: Agent loop and dispatch, supported persona-enabled delegation and opt-in post-edit verification.
- Adjacent first-party surfaces excluded from ownership: Repository-specific tests/evals, packaging and release CI, and third-party tools/providers.
- First-party operating / deployment modes considered: Direct local coding, persona-enabled orchestration, and configured workspace verification. The CLI is the traced composition path for the opt-in claims.
- Recursion level: One local root run and its active worker team.
- Reviewed revision: 0230ad0cff78aee5c97d182b62f753e2fdb85d71
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The Go application resolves a workspace and tools then starts the agent loop, with layered configuration, session trees and checkpoint records. Workspace personas can turn on the built-in team prompt and task tool. Configured verification runs separately from the editing calls. [README.md](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/README.md), [internal/app/app_execute.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/app_execute.go), [internal/agent/loop.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/loop.go), [internal/session/store.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/session/store.go), [internal/app/verify_wire.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/verify_wire.go).

## Operational model

The root agent performs software work through its tool loop or commissions separate subagent turns. In orchestration mode it decides dependency waves, keeps file-overlapping tasks apart and revises subsequent work after each wave returns.

## S1 — Operations

- State: A
- Function: Perform coding tasks through repeated model and workspace interactions.
- Disturbance / variety regulated: Uncertain files, failures and action effects.
- Decisive decision or feedback right: Choose tools, decide how to use results, and report the outcome.
- Decision owner: Model-backed root or child agent carrying an operational task.
- Supporting / enforcement mechanisms: First-party tool dispatch, checkpoints and transcript persistence.
- Closure path: Tool results enter the conversation and feed subsequent model steps until a terminal output.
- Boundary reachability: The ordinary CLI runs this agent loop with the shipped tools, and opted-in subagents use child runs from the same implementation.
- Why this is / is not agent-owned: Removing model discretion removes the operative coding decisions.
- Evidence: [internal/agent/loop.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/loop.go), [internal/agent/dispatch.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/dispatch.go#L209-L297), [internal/agent/dispatch.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/dispatch.go#L526-L562), [internal/app/app_execute.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/app_execute.go).
- Basis: Explicit
- Confidence: High
- Caveats: External providers supply inference. No live calls were made.

## S2 — Coordination

- State: A
- Function: Prevent interference between operative children sharing one checkout.
- Disturbance / variety regulated: Concurrent children can edit the same files, and later work can depend on earlier output.
- Decisive decision or feedback right: Assign file ownership and decide which children can run in the same wave, then resolve observed conflicts.
- Decision owner: The model-backed orchestrator.
- Supporting / enforcement mechanisms: Packaged orchestrator prompt, task dispatch, and separate child context with explicit file scopes.
- Closure path: Wave returns expose conflicts and dependencies. The lead changes the following assignment and retries or revises bounded work.
- Boundary reachability: A workspace persona activates the first-party orchestrator prompt and task tool in the standard application execute path.
- Why this is / is not agent-owned: The model chooses scopes, wave membership and conflict handling. The dispatcher executes these choices.
- Evidence: [internal/agent/prompts/orchestrator.txt](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/prompts/orchestrator.txt), [internal/app/app_execute.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/app_execute.go#L68-L107), [internal/agent/subagent.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/subagent.go#L219-L269), [internal/agent/dispatch.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/dispatch.go#L209-L297).
- Basis: Explicit
- Confidence: High
- Caveats: This is prompt-directed regulation without hard worktree isolation. It applies in the enabled persona mode.
- Distinct S1 units: Separate subagent runs with concrete operative subtasks and their own run contexts.
- Inter-S1 disturbance: Simultaneous edits by different child workers can collide in the shared workspace.
- Attenuating coordination relation: The packaged lead must put file-overlapping work in successive waves and assign each child concrete file scope.
- Feedback into subsequent S1 behaviour: The lead consumes results and conflicts at the wave boundary and revises or reassigns the following wave.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The first-party wave constraint is targeted to the same-file interference mechanism and requires corrective follow-through.

## S3 — Inside-and-now control

- State: A
- Function: Control the present workload of one orchestrated request across its worker commitments.
- Disturbance / variety regulated: Failed subtasks and emerging dependencies can invalidate the active execution plan.
- Decisive decision or feedback right: Reprioritize or replace current commitments at wave boundaries based on the complete returns.
- Decision owner: The lead model in the configured orchestrator mode.
- Supporting / enforcement mechanisms: Task scope ledger in the lead conversation, child callbacks, shared execution and bounded dispatch.
- Closure path: The lead sees finished workers and failures and changes the next assignment or dispatches a revised retry.
- Boundary reachability: The stock prompt is injected by the standard opted-in persona setup and drives the shipped task return loop.
- Why this is / is not agent-owned: The lead assesses present work and selects a new trajectory. Static child budgets and limits do not make this choice.
- Evidence: [internal/agent/prompts/orchestrator.txt](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/prompts/orchestrator.txt), [internal/agent/subagent.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/subagent.go#L219-L269), [internal/agent/dispatch.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/dispatch.go#L209-L355), [internal/app/app_execute.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/app_execute.go).
- Basis: Structural
- Confidence: High
- Caveats: The claim covers decision points between work waves. It does not imply fleet-wide control or active cancellation of arbitrary external jobs.
- Whole-system current view: Within a bounded request, the leader chooses and observes all synchronous wave commitments, with shared wave results and failure returns in its turn context.
- Current-control decision scope: Defer or advance dependent work and decide what to retry, replace or leave out across the remaining operating plan.

## S3* — Complementary audit

- State: C
- Function: Cross-check mutated workspace work through an independently invoked configured verification command and return corrective feedback.
- Disturbance / variety regulated: The editing agent's tool success or narrative may diverge from build or test evidence.
- Decisive decision or feedback right: Determine which direct check supplies the validity judgment for the particular codebase.
- Decision owner: The operator or project supplies the independent check and criteria through the supported configuration. First-party runtime owns invocation and return.
- Supporting / enforcement mechanisms: Mutating batches trigger the opt-in verification callback. Workspace checks return exit status and bounded diagnostic evidence.
- Closure path: A failure is sent into the editing session as a new correction turn or stops the run after the reflection limit.
- Boundary reachability: The monitor path is an explicit first-party post-mutation configuration of the ordinary agent loop. A tool result alone cannot trigger the same feedback without the independent configured check.
- Why this is / is not agent-owned: A separate process supplies direct test/build evidence. The operator still selects the evidence and criteria. The standard separate task-verdict mode can judge only reported text unless its prompt requests independent evidence and the necessary tools are composed.
- Evidence: [internal/app/app_execute.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/app_execute.go#L380-L390), [internal/app/verify_wire.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/verify_wire.go), [internal/agent/verify_loop.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/verify_loop.go#L123-L176), [internal/agent/subagent.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/subagent.go#L280-L340).
- Basis: Structural
- Confidence: Medium
- Caveats: The verifier can be skipped if it cannot run. No autonomous primary-evidence assessor or hard always-on admission gate is claimed.
- Claim being audited: The actual code changes remain valid against an operator-selected build or test criterion.
- Ordinary reporting path: The editing run's tool outcome and its own generated report.
- Complementary access path: A separately launched configured workspace check reads or tests the edited tree and supplies independent diagnostics.
- Independence boundary: The command runs as its own process after the edited batch and reports the observed result. Domain-specific check selection and strength depend on local configuration.
- Who acts on findings: The producing session receives a failure feedback turn. The runtime ends the run when its bounded corrective attempts run out.

## S4 — Outside-and-then intelligence

- State: —
- Function: Select prospective capability adaptations based on external intelligence.
- Disturbance / variety regulated: Future provider, ecosystem or workload shifts may change suitable capabilities.
- Decisive decision or feedback right: No in-boundary decision channel from external future evidence to capability adoption was established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Provider probes and fallback, product update checks, runtime recovery and reusable skill authoring.
- Closure path: Present provider status can switch the current request. An authorized written skill can be used subsequently.
- Why this is / is not agent-owned: The first-party skill authoring path persists reusable procedures. The inspected path does not establish prospective external intelligence or an environmental adaptation decision over the whole assessed system.
- Evidence: [internal/agent/skill_author.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/skill_author.go), [internal/agent/fallback.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/fallback.go), [internal/provider/health_probe.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/provider/health_probe.go), [docs/USER_GUIDE.md](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/docs/USER_GUIDE.md).
- Basis: Structural
- Confidence: Medium
- Caveats: This leaves room for operator-composed future adaptation or an explicit new evidence witness.

### Absence scope

- Surfaces inspected: Provider health probes and fallback, updater, verification learning, and skill persistence.
- Plausible first-party paths checked: Early external signals, operator or autonomous adaptation prompted by provider status, and reusable procedure adoption.
- Why no material first-party path remains: Health and updates feed immediate operation/maintenance. Skill writing supplies a reusable workflow primitive without a first-party outside-and-then capability loop.

## S5 — Policy and identity

- State: P
- Function: Set which standing operator and project instructions may govern the local coding organization.
- Disturbance / variety regulated: Workspace-provided instructions can alter the standing operational mandate.
- Decisive decision or feedback right: Select the trusted project instruction boundary and supply standing instructions.
- Decision owner: The local operator authorizing project resources for the run.
- Supporting / enforcement mechanisms: Project trust setting, resource filtering and system prompt assembly. Enabled child persona instructions can be inherited inside the team.
- Closure path: The permitted instruction sources enter the model system prompt and inherited instruction snapshot for subsequent operations.
- Boundary reachability: The shipped CLI exposes project trust, and application construction applies it when including instruction resources in the system prompt.
- Why this is / is not agent-owned: The operator controls which boundary can supply governing project instructions. The model carries the applied mandate.
- Evidence: [internal/app/trust_env.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/trust_env.go), [internal/app/app_prompt.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/app/app_prompt.go#L53-L88), [internal/memory/boundary.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/memory/boundary.go), [internal/cli/flags_usage.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/cli/flags_usage.go), [internal/agent/subagent.go](https://github.com/2118505078xyh1/argentgo/blob/0230ad0cff78aee5c97d182b62f753e2fdb85d71/internal/agent/subagent.go#L448-L481).
- Basis: Structural
- Confidence: Medium
- Caveats: Tool permission choices are narrower than this evidence. The S5 claim is confined to owner-governed standing instruction authority in this deployment.
- Identity / ultimate-policy issue: Whose standing instructions can define the local agent's operative mandate at the workspace boundary.
- Ultimate authority in each claimed mode: The operator supplies standing instructions and authorizes the project-local instruction boundary.
- Return-to-operation path: Resource filtering applies the decision when constructing the system prompt and worker instruction snapshot, which govern subsequent model actions.

## Distributed OSS parent arrangement

The operator is parent at the local deployment. Project maintainers and CI remain outside that recursion.

## Self-hosted and non-human modes

Local operation supports owner-governed configuration with model-managed task execution. No additional agent-owned ultimate policy mode was established.

## Recursion

The root request is the boundary for current worker coordination and control. Other sessions and external ACP systems do not extend the assessed team.

## Variety and escalation

Bounded wave assignment contains shared-checkout interference. Optional independent process checks return diagnostics. Trust controls standing project instructions.

## Evidence gaps

Source-only inspection at the exact frozen commit. No live model calls, configured workspace checks or GUI/device operation were exercised.
