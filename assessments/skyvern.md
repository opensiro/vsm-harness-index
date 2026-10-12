---
harness_id: skyvern
project_name: Skyvern
repository: https://github.com/Skyvern-AI/skyvern
review_ref: f5f3f28a9ce0021a1db24286928a7bff6582a1eb
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Skyvern

## Review boundary

- System in focus: the first-party self-hosted Skyvern browser-agent, task/workflow runners, browser interaction loop and workflow-run-group mode at the frozen source revision.
- Purpose and identity: execute user- or API-specified browser tasks and reusable workflows by model-guided observation and action under a self-hosted runtime.
- Relevant environment: target websites and their changes, browser sessions, model APIs, database state, user workflow parameters, credentials, external sites and external model providers.
- Standard-distribution boundary: documented pip-installable local API/SDK/CLI and first-party execution services at f5f3f28a9ce0021a1db24286928a7bff6582a1eb; Cloud-specific managed provider internals are outside the source boundary.
- Credited operating / distribution surfaces: [README.md](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/README.md); [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L2181-L2250); [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L4708-L4810); [skyvern/forge/sdk/executor/background_task_executor.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/sdk/executor/background_task_executor.py#L697-L812); [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L291-L355); [skyvern/services/workflow_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_service.py#L229-L357).
- Adjacent first-party surfaces excluded from ownership: repository development and CI, benchmark demonstrations, unexecuted template prompts, Cloud-only integrations not shown to run in the local distribution, third-party browser sites and model-provider internals, arbitrary user-authored orchestration outside the installed Skyvern services.
- First-party operating / deployment modes considered: ordinary task execution, Task V3 model/tool loop, defined workflow execution, workflow-run-group serial dispatch/recovery, supported local/API operator intervention.
- Recursion level: a self-hosted Skyvern deployment operating an individual task or an optional run group of separately executed child workflows; not the Skyvern company or external customer organization.
- Reviewed revision: `f5f3f28a9ce0021a1db24286928a7bff6582a1eb`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The installable Skyvern system exposes local/browser automation, task and workflow API/SDK interfaces and a first-party agent runtime ([README.md](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/README.md)). The ForgeAgent task implementations create tasks and steps and use model responses plus fresh browser observations to select actions, execute them and return results; a separate completion-checking pass can re-scrape the page ([skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L2127-L2181), [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L4708-L4810), [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L6550-L6721)). The background executor owns dispatch/retry bookkeeping; workflow services construct run context and schedule block execution. Workflow-run-group services track child state, prevent stale dispatch claims and resume after terminal child events ([skyvern/forge/sdk/executor/background_task_executor.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/sdk/executor/background_task_executor.py#L123-L205), [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L322-L355), [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L580-L608)).

## Operational model

An ordinary task is one agentic operating unit: external prompt/goals and page observations are inputs; browser actions, extraction and completion are outputs. Group mode can create multiple independently executing workflow-run S1 units under a deterministic first-party dispatcher; model/provider outputs select page-level actions, while dispatch fencing, status transitions and cancellation are deterministic controls. The decision owner for each organizational function is assessed separately; agent model involvement does not automatically grant ownership of platform-wide governance.

## S1 — Operations
- State: A
- Function: Model-driven execution of browser tasks against changing web pages, with repeated perception, action selection, tool/browser effects and feedback.
- Disturbance / variety regulated: Unfamiliar websites, forms, page navigation, site errors, interaction state and model/tool failures.
- Decisive decision or feedback right: Choose context-specific browser actions and whether to continue an individual assigned goal in the running model/tool loop.
- Decision owner: The model-driven first-party agent at task recursion; host runtime bounds what can execute.
- Supporting / enforcement mechanisms: Browser/Playwright layer, ForgeAgent task and step state, retries, tools, configured step/timeout controls, persistence and result capture.
- Closure path: Task goal and page evidence → model action proposal → browser tool execution → fresh page/action results → next step or completion decision.
- Boundary reachability: The supported local SDK/API invokes the shipped ForgeAgent and executor, not only an example script ([README.md](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/README.md); [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L4708-L4810)).
- Why this is / is not agent-owned: Model-selected actions change the operational trajectory; deterministic execution limits and browser services are enforcement rather than the task-level actor.
- Evidence: [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L2181-L2250); [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L4708-L4810); [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L5561-L5610); [README.md](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/README.md).
- Basis: structural
- Confidence: high
- Caveats: Static source inspection only; no live site execution, provider inference or quality/robustness benchmark was performed.

## S2 — Coordination
- State: C
- Function: In workflow-run-group mode, protect independently running child workflows from concurrent/stale-dispatch overlap and provide a return path once in-flight work settles.
- Distinct S1 units: Separate child workflow runs prepared and executed for group items ([skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L372-L403)).
- Inter-S1 disturbance: A stale claimed item can still have an executing worker; releasing or launching a later child before the previous in-flight execution stops produces an overlapping/concurrent group run contrary to its serial boundary.
- Attenuating coordination relation: Claimed-item fencing, in-flight reconciliation, dispatch tokens, cancellation/settlement checks and ordered claim_next_item gating ([skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L322-L355); [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L504-L590)).
- Feedback into subsequent S1 behaviour: Terminal child notification leads to advance_workflow_run_group and a next-item claim only after reconciliation ([skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L580-L608)).
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The claimed positive mode specifically guards a demonstrated overlap/interference hazard for independently executing child work, not ordinary ordered workflow blocks or a generic task queue.
- Disturbance / variety regulated: Concurrent in-flight child execution, stale claim owners and race between cancellation/failure and downstream dispatch.
- Decisive decision or feedback right: Whether a group item may be dispatched while earlier child execution may still be active.
- Decision owner: Deterministic, first-party run-group controller (constructor mode), not the child agent deciding its own browser actions.
- Supporting / enforcement mechanisms: Database claims, status tracking, dispatch tokens and workflow-run executor.
- Closure path: Child state/termination → reconciliation and fenced decision → release/claim next unit → changed subsequent workflow-run execution.
- Boundary reachability: Run-group service submits, dispatches and advances executable child workflow runs in shipped first-party service mode ([skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L113-L239); [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L580-L608)).
- Why this is / is not agent-owned: Real inter-run attenuation exists in the packaged mode, but its decisive dispatch right is deterministic first-party code, not an autonomous metacoordinator model.
- Evidence: [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L322-L355); [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L504-L608); [skyvern/forge/sdk/executor/background_task_executor.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/sdk/executor/background_task_executor.py#L762-L912).
- Basis: structural
- Confidence: medium
- Caveats: Scope is the optional serial group mode only. The credited S2 interference is limited to active overlapping child runs within the shipped serial run-group mode, not generic task queueing or idempotency outside it.

## S3 — Inside-and-now control
- State: ?
- Function: Potential operator intervention and run-group current-state supervision, not yet established as whole-system current-control authority at the declared recursion.
- Disturbance / variety regulated: In-flight workload, stalled or canceled workflow runs and resource/commitment conflicts.
- Decisive decision or feedback right: Unresolved: group cancellation and retry dispatch exist, but a system-wide discretionary commitment/resource choice by a legitimate owner has not been reconstructed.
- Decision owner: Unresolved; deterministic service owns group lifecycle enforcement, while operators own requested cancellations.
- Supporting / enforcement mechanisms: Group status API, child status enumeration, cancel group, claim/retry executor.
- Closure path: Group cancellation and terminal-event rescheduling are real; a whole-system S3 feedback loop remains unproven.
- Why this is / is not agent-owned: Service monitoring and deterministic cancellation do not themselves imply S3.
- Evidence: [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L240-L307); [skyvern/services/workflow_run_group_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_run_group_service.py#L580-L608); [skyvern/forge/sdk/executor/background_task_executor.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/sdk/executor/background_task_executor.py#L123-L205).
- Basis: unknown
- Confidence: low
- Caveats: Need supported operator surfaces establishing a whole-current view, discretionary priorities/commitments and returned effects. Do not silently upgrade group scheduling to S3.

## S3* — Complementary audit
- State: ?
- Function: Completion verification is documented in code, but the material independence of the complementary observational and judgment path is not yet settled.
- Disturbance / variety regulated: False task completion claims and goal/criterion errors.
- Decisive decision or feedback right: The completion verifier may return complete/terminate/continue based on rescraped page state, but the separately independent audit right is unresolved.
- Decision owner: Completion-checking LLM handler and first-party result controller; independence from production agent's ordinary reporting remains to be demonstrated.
- Supporting / enforcement mechanisms: Fresh scrape, optional action history and alternative completion LLM handler feature flag.
- Closure path: A verifier outcome feeds task continuation/termination, but this alone is not sufficient for S3*.
- Why this is / is not agent-owned: A second model call or routine validator is not automatically an independent complementary audit.
- Evidence: [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L6550-L6721); [skyvern/forge/agent.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/agent.py#L6723-L6780); [skyvern/forge/validation_evidence_router.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/validation_evidence_router.py).
- Basis: unknown
- Confidence: low
- Caveats: Need source-grounded separation of audit observation, decision authority and corrective closure beyond a routine same-pipeline goal check; additional script-review paths require inspection.

## S4 — Outside-and-then intelligence
- State: ?
- Function: The repository includes workflow/script generation and external page adaptation, but no established external-and-prospective adaptation ownership closure at the system boundary yet.
- Disturbance / variety regulated: Future site changes, repeat-task automation demands and possible workflow evolution.
- Decisive decision or feedback right: Not established for prospective portfolio/capability adaptation.
- Decision owner: Unresolved; a user designing workflows or generating scripts does not automatically constitute first-party S4 closure.
- Supporting / enforcement mechanisms: Workflow service, script-generation subsystem, planner levers and reusable workflow definitions.
- Closure path: Generated scripts can potentially become future capability; triggering prospective evaluation and return into deployed capability require more evidence.
- Why this is / is not agent-owned: Short-horizon browser reaction and current-step planning are S1; storing a workflow alone is not S4.
- Evidence: [skyvern/core/script_generations/generate_script.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/core/script_generations/generate_script.py); [skyvern/services/workflow_service.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/workflow_service.py#L89-L145); [skyvern/services/planner_levers.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/services/planner_levers.py).
- Basis: unknown
- Confidence: low
- Caveats: Evaluate shipped script generation, workflow-builder and operator modes for an actual outside-and-then decision/feedback loop before resolving positive or bounded absence.

## S5 — Policy and identity
- State: ?
- Function: Organizational credentials, task-level constraints and permissions are present, but ultimate policy/identity decision and closed parent-governed return path are not yet established.
- Disturbance / variety regulated: Security boundaries, acceptable browsing behavior and organizational identity/policy changes.
- Decisive decision or feedback right: Unresolved at the declared deployment recursion; user-supplied constraints and permissions enforce delegated policy but do not establish an ultimate-policy owner in this review.
- Decision owner: Unresolved between parent operator and host configuration/developer authority.
- Supporting / enforcement mechanisms: Organization-scoped permissions, API keys, credential checks, policy/configuration flags.
- Closure path: Per-request permission filtering exists; a legitimate ultimate-policy decision changing subsequent operation has not yet been traced.
- Why this is / is not agent-owned: Enforcement of static permissions is not S5 ownership.
- Evidence: [skyvern/cli/mcp_tools/org.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/cli/mcp_tools/org.py); [skyvern/forge/sdk/executor/background_task_executor.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/forge/sdk/executor/background_task_executor.py#L379-L395); [skyvern/cli/config_command.py](https://github.com/Skyvern-AI/skyvern/blob/f5f3f28a9ce0021a1db24286928a7bff6582a1eb/skyvern/cli/config_command.py).
- Basis: unknown
- Confidence: low
- Caveats: Resolve actual deployed identity/policy authority and parent return path before canonical admission; do not infer S5=P from a generic administrative UI.

## Recursion

Each browser task is an S1 operating unit; workflow-run-group mode can regulate multiple child workflow runs at its group recursion. The self-hosted deployment operator and Skyvern project maintainers are not automatically a higher-recursion S3/S5 owner without a specific first-party return path.

## Variety and escalation

Model-guided browser actions absorb site-level variety. Task statuses, retries and terminal events regulate execution, while group dispatch fencing manages overlap risk. User intervention, external model providers and website failures remain external dependencies; no independent organizational algedonic channel has been credited from an alert or status alone.

## Evidence gaps

Source-first but static review at the exact frozen SHA. Full first-party operator/dashboard current-control paths, script-generation prospective use, independent review/script-verifier modes and identity/policy return paths remain unresolved. Four `?` states are explicit limits rather than negative findings. Before canonical resolution, either prove a positive path or perform Methodology 0.3.7 bounded-absence adjudication with the required three-part scope; re-evaluate the S2 interference witness against the Methodology threshold.
