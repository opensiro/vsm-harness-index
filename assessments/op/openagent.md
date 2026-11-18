---
harness_id: openagent
project_name: OpenAgent
repository: https://github.com/openagt/openagent
review_ref: f1461867acb5161efe5293b28dcb0dfb13c2f1af
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenAgent

## Review boundary
- System in focus: One project registered in the installed OpenAgent dashboard and daemon, with model-driver runs, worktrees and the selected first-party project skill modules.
- Purpose and identity: Turn requested or queued work on a software project into code and reviewable changes under the operator's selected execution and publication conditions.
- Relevant environment: Project files, task queue, ticket/PR state, developer responses, external model CLIs and their quota and availability.
- Standard-distribution boundary: Bundled dashboard, daemon and agent-runner with shipped drivers and optional first-party orchestration, tickets, queue and scheduler. The coding model and inference provider are external.
- Credited operating / distribution surfaces: Default model-backed worktree runs, opt-in model-led plan orchestration, ticket claims and queue worker, operator run overview/intervention, and scheduling controls.
- Adjacent first-party surfaces excluded from ownership: Repository dogfood automations, product development and release CI; third-party model internals, custom hooks and optional user-added workflows are outside credited ownership.
- First-party operating / deployment modes considered: Installed local/dashboard projects with supported configured model CLIs, optional orchestration, optional scheduled queue work and attended interventions.
- Recursion level: The project delivery cell. Concurrent plan workers and autonomous ticket workers contribute to this same project's code and task outcomes.
- Reviewed revision: `f1461867acb5161efe5293b28dcb0dfb13c2f1af`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The dashboard starts coding sessions through the bundled runner and configured driver, lists the project queue and live runs, and surfaces intervention requests. The runner creates worktrees, launches the chosen model CLI, persists session state and ends or resumes runs. Optional modules provide a project task queue, ticket claims, scheduled model work and plan-based subagent start/retry/landing. A child end reaches its originating lead agent via the run inbox or continuation path.

## Operational model

A run performs concrete software work. In selected orchestration mode several child agents act independently on different task outputs and write isolated branches. The lead authors task dependencies and file boundaries, and it decides how to integrate children into its current assignment. The dashboard operator retains portfolio-level current interventions across runs, while human approval of a plan authorizes that plan's child-agent work.

## S1 — Operations

- State: A
- Function: Execute software tasks through a selected model-backed coding run.
- Disturbance / variety regulated: Changing project state, task details, source files, tests and provider/tool results.
- Decisive decision or feedback right: Choose edits, tool and test actions, and substantive task results in the assigned checkout.
- Decision owner: The configured coding model agent participating through OpenAgent's first-party runner/driver.
- Supporting / enforcement mechanisms: Worktree, driver session, tool substrate, adopted project skills and run records.
- Closure path: The session consumes model/tool results, updates code, and persists the outcome, branch or waiting state for continuation.
- Why this is / is not agent-owned: The model controls substantive software actions within the runtime and operator constraints.
- Boundary reachability: Standard dashboard and runner dispatch work via installed Claude Code or Codex adapters, and optional modules launch additional runs.
- Evidence: [normal installed entry](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/README.md#L16-L46), [runner and session creation](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/agent-runner/src/run.ts#L512-L593), [run disposition](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/agent-runner/src/run.ts#L754-L796).
- Basis: structural
- Confidence: medium
- Caveats: Evidence is source-based and requires an installed, authenticated supported driver.

## S2 — Coordination

- State: A
- Function: Attenuate concrete interference between child workers' branch edits and dependent starts.
- Disturbance / variety regulated: Workers changing the same file can collide on landing. A dependent child started before its predecessor's result lands receives a base without that result.
- Decisive decision or feedback right: Choose file owners, merge/split tasks or declare dependencies, then decide which work to start, land or retry in response to actual task state.
- Decision owner: The lead model agent authors and operates the coordination plan once the operator authorizes it.
- Supporting / enforcement mechanisms: Explicit file/dependency plan fields, shared-file warnings, dependency enforcement, separate worktrees and child-end continuation.
- Closure path: The chosen plan shapes future child prompts and branch bases. A later child starts after dependencies land, or the lead reacts to overlap by stopping, revising the plan or relaunching work.
- Why this is / is not agent-owned: The runtime can warn or refuse an invalid launch, but it cannot determine which files to assign to each worker or which competing task to revise.
- Boundary reachability: The selectable orchestration module gives the lead the task-plan, start, status, land and retry commands in the shipped runtime.
- Distinct S1 units: Two model-backed child runs each produce a distinct work result in its own checkout, with separate scope and feedback.
- Inter-S1 disturbance: Both units can be assigned overlapping paths, or a dependent unit can run on a base without the other's landed changes.
- Attenuating coordination relation: The lead model partitions owned paths and chooses dependencies and launch order, with warning/refusal feedback on overlap and missing predecessor state.
- Feedback into subsequent S1 behaviour: The assigned file set is in the new child's prompt and a landed predecessor is in the new child's branch base.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The plan and start feedback explicitly represent conflicting file owners and predecessor changes missing from the child's working base.
- Evidence: [skill plan and one-file-set rule](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/skills/orchestration/SKILL.md#L38-L71), [start, state and concrete conflict feedback](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/skill-orchestration/src/subagents.ts#L162-L244), [parent feedback](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/agent-runner/src/parent.ts#L59-L78), [packaged activation](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/dashboard/src/built-in.ts#L35-L46).
- Basis: structural
- Confidence: medium
- Caveats: File ownership is declared and overlap warnings are advisory. Credit is to the lead's coordinated choices and the enforced dependency/base return, within one authorized orchestration plan.

## S3 — Inside-and-now control

- State: P
- Function: Control current project commitments in flight and resources available to subsequent queued work.
- Disturbance / variety regulated: Multiple running and paused agents compete for current effort and quota, with work carrying pending decisions or live failures.
- Decisive decision or feedback right: Select which live run to stop or answer and which automation to start, pause or slow, using current project state.
- Decision owner: Project dashboard operator who controls the relevant installed project and scheduler.
- Supporting / enforcement mechanisms: Dashboard current-run and queue view, intervention projection, stop action, and persisted scheduler pace/switch state.
- Closure path: Stopping changes the selected run's behavior immediately. A returned answer resumes its execution. Pace and switch choices constrain subsequent starts.
- Why this is / is not agent-owned: The project operator makes the portfolio decision. The model owns task-local orchestration, and quota and scheduling machinery enforce configured limits.
- Boundary reachability: Dashboard actions for live runs, questions and project scheduler commands are first-party supported surfaces.
- Whole-system current view: The installed dashboard projects current running work, queue counts, pending questions and review/dead-end intervention items across the registered project.
- Current-control decision scope: The operator can stop a specific live run, resume a waiting run or change consumption of future execution slots by the current project automation.
- Evidence: [current runs and queue overview](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/dashboard/src/dashboard/overview.ts#L135-L193), [intervention evidence](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/dashboard/src/dashboard/interventions.ts#L18-L46), [operator stop UI](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/dashboard/dashboard/components/AgentActionsMenu.tsx#L271-L286), [operator start, stop and pace](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/skills/scheduler/SKILL.md#L8-L28).
- Basis: structural
- Confidence: medium
- Caveats: The lead's plan-wide stop/retry/continue choices are bounded to its own assignment. There is no demonstrated agentic controller of the whole project portfolio.

## S3* — Complementary audit

- State: —
- Function: The supported paths do not establish an agentic complementary audit loop distinct from regular delivery and integration checks.
- Disturbance / variety regulated: Agent completion claims may miss regression or correctness defects in landed work.
- Decisive decision or feedback right: The lead can run per-task and plan checks while landing; a separate decisive audit right was not established.
- Decision owner: Lead agent and runtime own ordinary task integration; the operator can inspect surfaced changes.
- Supporting / enforcement mechanisms: Isolated branches, plan checks, artifact and PR review surfaces and optional source review task skills.
- Closure path: Landing returns check output to the lead and can trigger a regular retry. Prompt-only review tasks do not have a shipped binding that independently challenges a producer's claim and returns it to project control.
- Why this is / is not agent-owned: The lead reviewing worker branches is also the production integration owner; the external host can run tools unavailable in the assessed first-party boundary.
- Evidence: [ordinary landing checks](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/skills/orchestration/SKILL.md#L86-L104), [project intervention queue](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/dashboard/src/dashboard/interventions.ts#L88-L112), [selectable adjacent review skills](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/README.md#L35-L46).
- Basis: structural
- Confidence: medium
- Caveats: A reviewer can be composed or launched manually as a separate task, but the inspected standard modules supply no function-specific complementary audit-to-control binding.

### Absence scope

- Surfaces inspected: Orchestration check/landing, PR and diff views, optional review task skills and dashboard intervention records.
- Plausible first-party paths checked: Independent raw-diff audit via dashboard or review task, ordinary land checks and host-provided review.
- Why no material first-party path remains: Shipped integration validation is performed inside the delivery path. Standalone review prompts and human artifact inspection lack a dedicated autonomous complementary audit journey whose findings return to project control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No installed loop was found that develops prospective adaptations for OpenAgent's own project delivery capability and returns them to current control.
- Disturbance / variety regulated: Product competitors and feature opportunities can alter the project's requested work. Provider availability or cost can affect how the run is executed.
- Decisive decision or feedback right: No shipped decisive right was found for selecting and folding an outside-and-then capability adaptation into the OpenAgent operating organization.
- Decision owner: The operator selects skills, models and automations. Agents can investigate a product's market and make output tickets.
- Supporting / enforcement mechanisms: Market research and feature suggestion prompts, project ticket flow, configurable scheduler and account availability controls.
- Closure path: The research skill writes product opportunity tickets. Account rotation and scheduler paths operate configured resources. No inspected path converts researched environmental change into an adopted adaptive plan for the delivery cell itself.
- Why this is / is not agent-owned: Market intelligence is a model-selected work product. An agent is not shown owning its adoption as a change to the delivery system's repertoire.
- Evidence: [market research outputs](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/skills/market-research/SKILL.md#L1-L7), [feature suggestions](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/skills/suggest-new-features/SKILL.md#L1-L7), [account availability](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/skills/account-rotation/SKILL.md#L7-L26), [scheduler control](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/skills/scheduler/SKILL.md#L8-L28).
- Basis: structural
- Confidence: medium
- Caveats: A particular project could explicitly compose research into its own system adaptation. Downstream product feature requests alone are task inputs at this boundary.

### Absence scope

- Surfaces inspected: Research and ticket skills, per-project module choices, scheduler controls and account feedback.
- Plausible first-party paths checked: Product market research as S4, quota-triggered account rotation as prospective adaptation, and parent action on project proposals.
- Why no material first-party path remains: Product opportunity tickets change the external work portfolio, while account and scheduler choices concern current delivery under established settings. No installed channel folds prospective evidence into a changed delivery capability.

## S5 — Policy and identity

- State: —
- Function: An installed identity-level adjudication and return path was not established.
- Disturbance / variety regulated: A project operator sets how far runs may publish and authorizes delegation when a plan needs workers.
- Decisive decision or feedback right: No distinct issue-to-decision route for ultimate project-delivery purpose or policy was found.
- Decision owner: The operator chooses mode, publication preferences and answers particular run questions; higher project policy belongs to its own maintainers.
- Supporting / enforcement mechanisms: Publish choices and start requests, per-project saved preferences and hash-bound plan approval.
- Closure path: A publication preference shapes later invocation instructions. Plan approval authorizes the corresponding task plan.
- Why this is / is not agent-owned: The agent does not own the policy decision. Per-run permission and saved default configuration provide no identified policy adjudication/return loop.
- Evidence: [saved publish default and admissible levels](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/dashboard/src/publish-levels.ts#L1-L64), [plan-specific consent](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/skill-orchestration/src/plan.ts#L29-L38), [return of plan decision](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/skill-orchestration/src/plan.ts#L69-L79), [invocation instruction](https://github.com/openagt/openagent/blob/f1461867acb5161efe5293b28dcb0dfb13c2f1af/packages/agent-runner/src/run.ts#L74-L104).
- Basis: structural
- Confidence: medium
- Caveats: A persistent publication default is real operator authority over invocation. The evidence does not show a path that routes and resolves a project-delivery identity or ultimate-policy issue.

### Absence scope

- Surfaces inspected: Default publication level, runner prompts, plan approval, project commands and operator intervention.
- Plausible first-party paths checked: Plan approve/change question, durable publication settings and general user-choice return as potential parent decision rights.
- Why no material first-party path remains: The reachable uses concern specific commitments and settings. No dedicated or demonstrably used path takes up an ultimate policy dispute and feeds back its authoritative resolution.

## Distributed OSS parent arrangement

Maintainers of the OpenAgent distribution and of the client project have separate authority. The assessment credits the deployment operator's current-control decisions within the client project.

## Self-hosted and non-human modes

Local installed runs can use optional orchestration, tickets and scheduling; absence of those modules in a default installation constrains which positive witnesses are reachable.

## Recursion

The lead/child relation nests tasks and contributions. A child with its own branch and local discretion has an operational role, while complete recursive viability was unestablished.

## Variety and escalation

Explicit dependencies, claim ownership and bounded parallelism reduce conflict and scarce-resource pressure. User questions and stop actions return current exceptions to legitimate control.

## Evidence gaps

Source inspected at the frozen revision. No model sessions, hosted connection tests or live agent performance was exercised. Review and adaptation claims stay within the installed delivery boundary.
