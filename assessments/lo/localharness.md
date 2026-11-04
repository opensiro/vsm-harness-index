---
harness_id: localharness
project_name: LocalHarness
repository: https://github.com/ahwurm/localharness
review_ref: d0859f71d1bb4b99cae78e72ddf459d105c47f93
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# LocalHarness

## Review boundary

- System in focus: One self-hosted LocalHarness installation operating a local-model agent, its optional multi-step task-flow children and reply critics; when explicitly invoked, its shipped autoresearch operating mode changes that installation's future configuration.
- Purpose and identity: Deliver tool-using coding/research work for a human operator through local models, bounded tools, review, task orchestration and optional measured adaptation of operating parameters.
- Relevant environment: User work and new instructions, untrusted local and web sources, tool failures, long task dependencies, changing model or runtime quality on sampled work scenarios, security and resource constraints.
- Standard-distribution boundary: Python 3.12+ application with CLI/ACP/optional channels, model-compatible tool loop, permissions, fresh task executor/explorer and critic agents, task documents, bundled default-on autoresearch plugin and its experiment/adoption code. Locally served or external OpenAI-compatible models are dependencies, not first-party organizational owners.
- Credited operating / distribution surfaces: [README](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/README.md), [metaharness and supported controls](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/metaharness.md), [agent loop](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/agent/loop.py), [task runner](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/runner.py), [panel](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/panel.py), [autoresearch plugin](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/plugins/autoresearch.md), [autoresearch loop](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/autoresearch/loop.py), [adoption](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/autoresearch/adoption.py).
- Adjacent first-party surfaces excluded from ownership: Maintainer development and CI, benchmark author's scenario design, package publication, example research-note workflow, external model-serving organizations, hypothetical separately run installations and their OSS governance. Shipped benchmark *observations* can feed the invoked autoresearch mode, but developing or maintaining the benchmark suite is not credited to the runtime.
- First-party operating / deployment modes considered: Default single-agent tool-using turn with reply critic panel, optional multi-stage `/task` flow with fresh executors, user-directed `/task plan` and `/task accept` interventions, installed default-on autoresearch plugin invoked with a configured proposer and benchmark corpus, automatic adoption of validated wins or operator review/adoption of held changes. The autoresearch command is not automatically running during a normal chat.
- Recursion level: One local installation and its whole current work/task and configurable future agent capability; a fresh executor is a bounded S1 work cell, not a proven independently viable child organization.
- Reviewed revision: d0859f71d1bb4b99cae78e72ddf459d105c47f93 (GitHub repository ID 1247964551).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI starts a locally configured model client and a ReAct-style model/tool loop. YAML defines agents and permitted tools; one gate restricts sensitive effects for the root and its fresh child agents. For larger jobs a root model owns the objective and task-flow progression, writes decisions, research and a step/dependency plan, invokes a separate bounded executor for each step and receives its report and critic outcomes. The default reply panel creates fresh fixed-role read-only critics after a tool-using turn; their separate source inspection and findings can block a draft and require root correction. An optional, default-enabled but separately invoked autoresearch plugin reads failed benchmark traces, has a proposer model choose typed config changes, gates them through training and holdout experiments, and automatically applies qualifying wins to the live user configuration overlay. A human can instead review and adopt held changes. [README](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/README.md), [task docs](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/metaharness.md), [autoresearch](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/plugins/autoresearch.md).

## Operational model

One root agent chooses tools and work steps in direct sessions; for task-flow mode, fresh executors carry out allocated operational steps under the root's plan, and independent critics inspect the resulting evidence. The root's explicit plan and feedback decisions make a narrower whole-task S3 path than a general multi-project enterprise controller. Deterministic budget limits, permissions, step ordering and score parsing enforce decisions but do not own discretion. The operator has a separate whole-task intervention path by reviewing the full plan/status and authoritatively accepting revised documents. The externally benchmarked autoresearch experiment is a distinct *supported, invoked* operating mode; its measured adaptation may change later local-harness work but is not an always-on current-turn planner. These independent contexts and modes must not be collapsed into one permanently autonomous S3/S4/S5 hierarchy.

## S1 — Operations

- State: A
- Function: Interpret human work and pursue open-ended actions using a chosen local model and permitted tools.
- Disturbance / variety regulated: Changing files, requests, sources, provider outputs, unexpected tool errors and changing subtasks.
- Decisive decision or feedback right: Select next tool, its arguments, whether to delegate, inspect results and choose whether to continue or answer.
- Decision owner: The configured root LLM agent; a fresh executor LLM owns its bounded assigned operational step.
- Supporting / enforcement mechanisms: ReAct loop, local OpenAI-compatible model client, YAML tool resolver, permission gate, child budgets and completion recovery.
- Closure path: A model chooses a tool; LocalHarness gates and executes it; result and stamped outcome return to model context for further action or a completed answer.
- Boundary reachability: Standard `localharness start` and `/task` routes invoke the first-party agent and child loop; no developer-supplied missing autonomy actor is needed beyond choosing an operational model endpoint.
- Why this is / is not agent-owned: Tool/action discretion belongs to the agent, while the runtime checks permissions, schedules calls and transports their results.
- Evidence: [README agents and tools](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/README.md), [ReAct loop](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/agent/loop.py), [task executor](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/runner.py).
- Basis: structural.
- Confidence: high.
- Caveats: No actual third-party local model execution or GPU end-to-end session was performed in this source review.

## S2 — Coordination

- State: —
- Function: No first-party S2-specific regulator of conflict among separately viable S1 operating units is established at this one-installation recursion.
- Disturbance / variety regulated: Task dependencies and step order are controlled, but no demonstrated distinct S1 interference/oscillation is negotiated.
- Decisive decision or feedback right: The root plans dependencies; runtime runs one step and its review at a time.
- Decision owner: Root agent's overall task management and deterministic stage runner, not a separately evidenced inter-S1 coordinating actor.
- Supporting / enforcement mechanisms: `depends_on` fields, step status, fresh child contexts, task manifest, file digests, time limits.
- Closure path: Step reports enter the task state and later work proceeds, but no S2-specific conflict relation alters two distinct S1 units' subsequent behavior.
- Why this is / is not agent-owned: Task decomposition, ordering, independent reviewers and shared task documents do not themselves witness attenuation of an actual inter-S1 interference.
- Evidence: [task pipeline](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/metaharness.md), [runner and dependencies](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/runner.py), [task records](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/record.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: External deployment orchestration of multiple installations is outside the reviewed boundary.

### Absence scope

- Surfaces inspected: Task-stage runner, dependency manifests, fresh explorers/executors, shared file state and orchestration controls.
- Plausible first-party paths checked: Parallel agents, dependency scheduling, write controls, shared state and critic feedback.
- Why no material first-party path remains: Distinct independent viable operating units, a specific interference and an S2-specific relation/feedback were not evidenced; ordinary task management and auditing belong to different functions.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate a whole multi-step task's current commitments, sequencing and corrective intervention across its distinct operational steps.
- Disturbance / variety regulated: Failed prior steps, incomplete objective coverage, stale plan assumptions, budget and dependency constraints, critic blockers and diverging deliverables.
- Decisive decision or feedback right: Root model writes/revises the whole-task plan and decides what unit executes next or should be corrected; an operator in the separate guided mode can inspect and authoritatively accept revised task documents or changes.
- Decision owner: Task-flow root agent in autonomous mode; legitimate human operator of that installation in the supported `/task plan <change>` / edit-and-`/task accept` mode.
- Supporting / enforcement mechanisms: Persisted `decisions.md`, `plan.md`, `step-N.md`, stage/status manifests, `depends_on`, bounded children, critic result ingestion and human-visible `/task show`.
- Closure path: Root receives current whole-task outcomes and critic findings, changes plan/next unit or retries a step, and the task runner executes the resulting decisions. In parent mode the user's accepted plan change becomes the source of truth for subsequent task runs.
- Boundary reachability: `/task new` or model-opened multi-step task starts the supported root/task runner; `/task show`, `/task plan` and `/task accept` are first-party operator commands changing the same active task, rather than adjacent maintainer tools.
- Why this is / is not agent-owned: The model has discretion over task-level commitments, unlike the deterministic stage runner; the operator has an actual independent plan-acceptance control path, not merely a pause/kill switch.
- Whole-system current view: Task objective, decisions, research, complete ordered plan, step outcomes and critic verdicts in task documents/manifests exposed to the root and `/task show`.
- Current-control decision scope: Select/revise the whole task's steps, dependencies, changes to unsatisfied deliverables, and how corrective work returns to a bounded executor.
- Evidence: [task lifecycle and operator control](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/metaharness.md), [root/task runner](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/runner.py), [stage records](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/record.py), [user commands](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/verbs.py).
- Basis: structural.
- Confidence: medium for the narrow whole-task recursive boundary; high that both control routes are shipped.
- Caveats: This does not establish enterprise-wide or multi-installation resource bargaining. A default single-turn session may have only one S1 and thus no separate S3 supervisory scope.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Root task agent | Whole-task step results, updated requirements and critic blockers | Agent revises `plan.md`/next-step decision; runner executes updated commitment | [task runner](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/runner.py) |
| Parent (`P`) | Human task owner/operator | `/task show` exposes task documents and blocked steps | Operator's changed task plan is accepted into task records, changing what `/task run` next executes | [document acceptance](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/metaharness.md) |

## S3* — Complementary audit

- State: A
- Function: Challenge root work or task reports through fresh purpose-separated, independently sourced read-only reviews that can provoke correction.
- Disturbance / variety regulated: Unsupported claims, missed objectives, stale facts, policy/security issues, mismatch between actual artifacts and agent-reported completion.
- Decisive decision or feedback right: A separate critic agent independently inspects primary sources and outputs its own finding/score; a blocker prevents ordinary acceptance of the draft and returns criticism to the root for a bounded corrective turn.
- Decision owner: Shipped fresh critic LLM agents with fixed package-owned roles, not the draft-producing root; the root decides how to repair or dispute within the feedback loop.
- Supporting / enforcement mechanisms: Eight first-party critic specs, distinct read-only tool grants, source/result handles, scored blocking rules, panel finding parser and reply revision caps.
- Closure path: A tool-using root draft triggers a fresh panel; `factual`, `security`, `spec-compliance` or other selected critic reads raw file/web/tool source evidence, issues independent findings, and the panel sends blockers to a new root corrective round before the answer is delivered.
- Boundary reachability: A reply after tool use gets a panel by default; the packaged `assets/critics` roles cannot be replaced from a project overlay. The multi-step task flow uses the same first-party reviews after its documents and steps. The operator may turn `/review off`, so the claim is for enabled default mode.
- Why this is / is not agent-owned: The auditors perform their own source queries in fresh contexts and judge root claims; the deterministic blocker threshold merely carries that independent judgment. This is stronger than self-critique by the original answer agent, but not an externally accredited third-party audit.
- Claim being audited: Root answer's factual basis, security/spec compliance, and task stage's claimed fulfillment.
- Ordinary reporting path: The root's draft and delegated child's `step-N.md`/reported artifacts.
- Complementary access path: Critics' `read`, `grep`, `glob`, `git_read`, `tool_result_get` and for factual/recency reply critics optional web access to original evidence, including full draft and tool-result handles.
- Independence boundary: Separate fresh agent contexts, immutable package critic jobs, read-only scoped tools and evidence not limited to the root's summary; shared model provider and inline invocation limit assurance and should not be mistaken for independent human certification.
- Who acts on findings: Root must correct or evidence-dispute blockers; operator can inspect audit review and make explicit acceptance decisions in task flow.
- Evidence: [metaharness review semantics](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/metaharness.md), [critic specification and tools](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/orchestrator/task_flow/panel.py), [root correction loop](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/agent/loop.py).
- Basis: structural.
- Confidence: medium-high for complementary access; no empirical adversarial independence claim.
- Caveats: A panel can be disabled, interrupted, or deliver with caveats; routine inline checking alone would not be S3*, so this attribution depends specifically on fresh separate auditors' alternative direct evidence access and returned challenge authority.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: Develop and test prospective runtime-configuration adaptations against future-relevant benchmark work behavior, then return validated choices to operational capability.
- Disturbance / variety regulated: Evidence of model/harness failures on sampled problem classes, changing future quality/cost tradeoffs, overfitting to training examples and unsuitable parameter settings.
- Decisive decision or feedback right: A separate proposer LLM chooses one typed future configuration mutation based on observed failed benchmark traces; two-stage statistical tests decide accept/hold/reject; in supported auto-adopt mode a passing choice updates the live global user overlay without intervening human adoption judgment. Human review/adopt of held candidate is a separate operator mode.
- Decision owner: Proposer model develops the adaptation option; first-party experiment gate restricts it and the loop autonomously adopts clean wins. For held outcomes a human operator can choose the adaptation via CLI review/adopt path.
- Supporting / enforcement mechanisms: Failed training scenario trace corpus, typed component registry, sealed holdout, Welch plus corrected promotion test, anti-reward-hacking guard, archive, atomic user overlay and `ComponentMutated` audit event.
- Closure path: Observed failed scenarios → proposer selects typed config change → train+holdout experiment tests prospective behavior → accepted adaptation updates `overrides.yaml` at the same layer future sessions load → later agent work uses altered parameters. A held result can instead be reviewed/adopted by an operator and reach that same overlay.
- Boundary reachability: `autoresearch` ships enabled by default with the distribution and `localharness autoresearch run` is an exposed supported command once an external/local proposer endpoint is configured; `adopt()` writes the runtime global config and emits a component mutation. This is an invoked experimentation mode, not a background action in each ordinary session.
- Why this is / is not agent-owned: Model selects the actual future parameter option rather than simply observing benchmark scores, and the accepted option reaches subsequent operation; a deterministic statistical gate may reject the option but does not invent it. A human's configured proposer/startup and holdout setup do not themselves make the base mode parent-owned.
- External distinction: Failed runs on heterogeneous benchmark scenarios representing work the model/harness must handle, not the model's internal chain-of-thought or a one-turn task plan.
- Future / prospective distinction: Out-of-training holdout behavior asks whether a mutation should generalize to unseen future workload instances, rather than merely reproduce the current task's outcome.
- Adaptation option generated: A bounded one-component runtime configuration change grounded in sampled failures, e.g. a permitted agent or harness control parameter.
- Path back into current capability / S3: Atomic validated overlay modification affects the next model/agent configuration; a component mutation event and archive record make adaptation observable to operators controlling the installation.
- Evidence: [autoresearch supported operation](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/plugins/autoresearch.md), [failed-trace proposer](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/autoresearch/proposer.py), [auto-adopt decision](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/autoresearch/loop.py), [live overlay adoption](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/autoresearch/adoption.py), [operator CLI](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/cli/autoresearch_cmd.py).
- Basis: structural.
- Confidence: medium; prospective workload proxy and invoked mode are explicit limitations.
- Caveats: The documentation's introductory phrase that the operator chooses what to adopt describes the manual path, but the pinned source loop explicitly auto-adopts a clean `ADOPT` verdict. Benchmark scenarios are imperfect environmental proxies, not evidence of monitoring market, user population or real-world drift. No experiment was run here.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Proposer LLM under calibrated autonomous experiment/adoption loop | Failed training traces and future holdout scenarios | Accepted candidate is auto-adopted into live runtime overlay for future sessions | [experiment loop](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/autoresearch/loop.py) |
| Parent (`P`) | Human installation operator | Held proposal/report and its measured train/holdout evidence | Operator chooses `autoresearch adopt`; same validated overlay governs later work | [CLI and adoption](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/cli/autoresearch_cmd.py) |

## S5 — Policy and identity

- State: —
- Function: No evidenced first-party identity/ultimate-policy deliberation and return path for this installation's organizational purpose.
- Disturbance / variety regulated: Users set work objectives and local security policies, but the source does not establish an identity-level conflict between current operations and prospective adaptations requiring ultimate adjudication.
- Decisive decision or feedback right: Human configures root/permissions and starts tasks; the gate enforces choices, but these are ordinary task and permission rights rather than evidenced S5 ultimate policy.
- Decision owner: Operator for presets and task requests, program for enforcement; no S5-specific identity adjudicator is demonstrated.
- Supporting / enforcement mechanisms: YAML agent role, permission gate, config overlay and plugin toggles, human task steering.
- Closure path: Changed configuration can govern future tools but does not by itself demonstrate an identity issue reaching a legitimate ultimate authority and a policy-level decision returned to reconcile S3/S4 tension.
- Why this is / is not agent-owned: Static constraints, human task acceptance and improvement parameters do not amount to a current organizational ethos/identity arbitration loop.
- Evidence: [security boundary](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/SECURITY.md), [task controls](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/docs/metaharness.md), [config/overlays](https://github.com/ahwurm/localharness/blob/d0859f71d1bb4b99cae78e72ddf459d105c47f93/src/localharness/config/overlay.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A user/organization operating LocalHarness might exercise real S5 outside the product; that higher-recursion governance is not included.

### Absence scope

- Surfaces inspected: Agent YAML role, task objective/acceptance, approval gate, machine-level config, plugin controls, autoresearch adoption rules and runtime CLI.
- Plausible first-party paths checked: Human authority over tasks/permissions, static policies, automatic parameter adoption, config change audit, security escalation and maintainer governance.
- Why no material first-party path remains: The paths address individual permissions, current task direction and performance adaptation, with no evidenced distinct identity/ultimate-policy conflict-resolution decision and return to operation.

## Distributed OSS parent arrangement

GitHub project contributors, releases and CI are adjacent to the reviewed local installation, not a common live parent with access to its private local task and model outcomes. The positive parent modes are the actual *local* human installation/operator controls; no organization-wide parent governance claim is made.

## Self-hosted and non-human modes

The self-hosted root/task and autoresearch operations can be agent-owned under the selected model/explicit invocation, with distinct local operator changes. The external model engine, benchmark suite author and OS guardrails are supporting actors, not automatically owners of VSM functions. `A(P)` denotes available alternative routes, not two simultaneous authorities for one decision.

## Recursion

In a multi-step task the root and task record form the system-level current commitments; fresh executors contribute bounded independent steps. Such children do not have evidenced identity, independent environmental coupling and their own complete metastystem, so no nested viable S1 recursion is inferred. Another entire installation would be a separate assessed unit.

## Variety and escalation

Tool results return to S1, critic blockers return independently to root correction (S3* into task control), and failed/held step reviews can change the whole-task plan (S3). In separately invoked autoresearch, sampled failures and unseen holdout scenarios inform parameter adaptation (S4), which is returned through the validated overlay to future S1 operation. Hard budgets and permissions enforce boundaries, and the user remains legitimate operator; they are not by themselves S2 or S5.

## Evidence gaps

- Source and documentation review only at the immutable Git revision; no live local language model, GPU run, exhaustive benchmark battery, adversarial critic study or measured self-improvement was executed.
- The packaged review critics have complementary source handles and fresh contexts, but share first-party runtime and potentially provider; their independence from compromised evidence or identical-model bias is bounded, not independently certified.
- Autoresearch's train/holdout proxy supplies a prospective test of work performance, not independently observed external market or user-population change. Its `A(P)` conclusion is restricted to the supported plugin invocation/configuration mode, not everyday chat.
- S3 is at a *single multi-step task* boundary; assigning `A(P)` must not be read as cross-project enterprise management. S2 and S5 negative findings remain bounded to inspected first-party runtime surfaces.
