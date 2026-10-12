---
harness_id: kai-linux-agent-os
project_name: Agent-OS (kai-linux)
repository: https://github.com/kai-linux/agent-os
review_ref: d7330ebc5e117f06df1fdf23118af8da2c327507
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: ?
---

# Agent-OS (kai-linux)

## Review boundary
- System in focus: one first-party Agent-OS persistent delivery/controller installation, GitHub-backed accepted goal/project/program work, autonomous coding workers under first-party queue and isolated worktrees, independent PR verification, goal monitoring and human-approved strategic planning.
- Purpose and identity: preserve and execute explicitly accepted human software-delivery intent through bounded task ownership, retries, PR evidence/merge gates and future priority/capability planning.
- Relevant environment: live GitHub issues/PRs/CI, real code worktrees and external-model-powered worker results, business/outcome scorecards, operator-authorized goals and human handoffs.
- Standard-distribution boundary: packaged Python `orchestrator` scheduler/queue/PR monitor/goal records/independent verifier and planner under documented supported supervised and autonomy modes ([README.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/README.md); [docs/delivery.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/docs/delivery.md); [docs/architecture.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/docs/architecture.md)). Coding backends (Codex, OMP, Claude, Gemini), their model internals, Telegram, GitHub and cloud services are external; operational decisions made by their model workers are counted only when first-party Agent-OS actually launches/observes them and closes work.
- Credited operating / distribution surfaces: [orchestrator/queue.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/queue.py); [orchestrator/supervisor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/supervisor.py); [orchestrator/worker_isolation.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/worker_isolation.py); [orchestrator/pr_monitor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/pr_monitor.py); [orchestrator/work_verifier.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/work_verifier.py); [orchestrator/strategic_planner.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/strategic_planner.py); [orchestrator/delivery_program.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/delivery_program.py); [orchestrator/delivery_contract.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/delivery_contract.py); [orchestrator/qualified_worker.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/qualified_worker.py); [docs/delivery.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/docs/delivery.md).
- Adjacent first-party surfaces excluded from ownership: developer CI for the Agent-OS repository, promotion/docs-only claims, historical KPI marketing examples, external proof dashboard and external worker/provider model internals, user-created custom integrations not supported in shipped configuration.
- First-party modes considered: accepted-goal tracked execution, dispatcher/queue and per-repo worker isolation, PR/CI/current-goal controller, separately run independent work verifier, prospective model-generated sprint planning with explicit human approval, supervised/deterministic capability promotion.
- Recursion level: one Agent-OS managed goal/project delivery organization with multiple external worker tasks as lower-recursion operating S1 units; no attribution to the external model-provider company.
- Reviewed revision: `d7330ebc5e117f06df1fdf23118af8da2c327507`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The frozen first-party queue selects admitted work, configures agent backends and runs external coding-agent CLIs in task-specific isolated Git worktrees, parses their results, retries within limits and escalates unresolvable faults. A supervisor and durable delivery-state/goal machinery retain ownership beyond individual tasks. External models choose concrete coding work but the Agent-OS host owns task admission, git-isolated execution, result/status monitoring, recovery and accepted-goal closure ([orchestrator/queue.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/queue.py); [orchestrator/supervisor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/supervisor.py); [orchestrator/worker_isolation.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/worker_isolation.py); [orchestrator/delivery_program.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/delivery_program.py); [docs/architecture.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/docs/architecture.md)).
A separate PR monitor checks source/CI status before automated merge. The first-party WorkVerifier fetches actual issue acceptance criteria and GitHub PR diff, applies deterministic anti-pattern checks and calls an independently chosen **different model family** from the coding worker to judge the artifact against the issue. Its verdict is stored and blocks auto-merge or returns findings/override prompts to the operator, not merely to the producing worker ([orchestrator/work_verifier.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/work_verifier.py); [orchestrator/pr_monitor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/pr_monitor.py)).
The strategic planner samples outside business-goal scorecards, GitHub/product constraints and research, invokes a model to propose future sprint choices, sends the plan for required human approval, then promotes accepted backlog issues into the operative queue. Current execution and future adaptation are separate: the latter is parent-owned because the model proposal is not enacted without a human approval action ([orchestrator/strategic_planner.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/strategic_planner.py); [orchestrator/objectives.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/objectives.py); [docs/delivery.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/docs/delivery.md)).

## Operational model
Accepted user goals persist through child task decomposition, queue assignment, bounded model-worker editing in isolated workspaces, separate PR acceptance review and CI merge evidence. Deterministic queue/PR controls handle present commitments; prospective model-selected sprint plans are accepted or rejected by the human before updating priorities. Explicit safeguards prevent success claims from being inferred merely from plan/activity count.

## S1 — Operations

- State: A
- Function: Task-conditioned software engineering by independently operating model-driven coding workers launched, bounded and observed through first-party Agent-OS execution paths.
- Disturbance / variety regulated: Variable task requirements, live source repository and environment state, tool errors, code-test failures and external model outputs.
- Decisive decision or feedback right: Worker model chooses specific coding actions/edits/tests in an isolated checkout and reports result; host runs it as a concrete accepted task.
- Decision owner: Configured model-driven coding worker (Codex/OMP/Claude etc.) acting in the first-party launched Agent-OS execution envelope; model provider internals remain external.
- Supporting / enforcement mechanisms: QueueEngine task selection, worker CLI adapter, isolated checkout, prompt/task contract, result parser, attempt budget and run log.
- Closure path: Accepted GitHub task → model-guided coding in managed worktree → changed files and result artifact → PR/CI observation and correction/retry/merge feedback.
- Boundary reachability: The shipped `queue.py` dispatches real external agent executables against its own per-task worktrees and parses their artifacts, rather than displaying a static plan ([orchestrator/queue.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/queue.py); [orchestrator/qualified_worker.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/qualified_worker.py); [README.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/README.md)).
- Why this is / is not agent-owned: The worker performs open-ended task-specific decisions; deterministic Agent-OS delivery guards provide an operating envelope, not external provider authorship.
- Evidence: [orchestrator/queue.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/queue.py); [orchestrator/qualified_worker.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/qualified_worker.py); [README.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/README.md)
- Basis: explicit + structural
- Confidence: high
- Caveats: This is a bounded source-first inspection of one frozen supported first-party mode, not a production reliability claim or credit for unshipped external providers.

## S2 — Coordination

- State: C
- Function: Prevent concurrent independent S1 coding workers from corrupting shared project/repository state and manage collisions during integration/PR activity.
- Distinct S1 units: Independently launched coding agents operating on distinct task worktrees for the same managed repository.
- Inter-S1 disturbance: Concurrent modifications or git/PR operations can contend over common repository integration state.
- Attenuating coordination relation: Worktree separation, per-repository locks and explicit CI/conflict-aware PR integration rules.
- Feedback into subsequent S1 behaviour: Queued/blocked work, conflict/rebase failure and bounded retry/escalation alter the next worker attempt/commitment.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The relation directly protects shared editing/integration resources under actual competing S1 work rather than being only a generic backlog or message queue.
- Disturbance / variety regulated: Two or more workers can edit branches/files for one repository, race over git state, or return incompatible work into the same integration target.
- Decisive decision or feedback right: Enforce per-repository locking, isolate task checkout state and reject/route conflicting integration/PR states rather than allowing concurrent overwrites.
- Decision owner: First-party deterministic supervisor/worktree and PR merge/rebase gate, with external Git providing transactional conflict detection.
- Supporting / enforcement mechanisms: Task-specific git worktrees, worker isolation, per-repo locks, exclusive task processing and PR Monitor conflict/rebase policies.
- Closure path: Competing work admissions → repo/worktree protection and merge conflict signals → serialize/rebase/retry/escalate → changed worker eligibility and next operating assignment.
- Boundary reachability: The supported queue and supervisor actually create isolated task worktrees and enforce repo-specific locks; PR monitor processes live conflicts and retries/rebases under explicit rules ([orchestrator/queue.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/queue.py); [orchestrator/supervisor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/supervisor.py); [orchestrator/pr_monitor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/pr_monitor.py)).
- Why this is / is not agent-owned: Conflicts are between independently acting code workers, and the attenuation/feedback path is a real running coordination mechanism but deterministically owned (C).
- Evidence: [orchestrator/queue.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/queue.py); [orchestrator/worker_isolation.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/worker_isolation.py); [orchestrator/supervisor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/supervisor.py); [orchestrator/pr_monitor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/pr_monitor.py)
- Basis: structural
- Confidence: medium
- Caveats: This is a bounded source-first inspection of one frozen supported first-party mode, not a production reliability claim or credit for unshipped external providers.

## S3 — Inside-and-now control

- State: C
- Function: Regulate current delivery obligations, worker assignment, attempt budgets, PR waiting/merge status and run-level interventions across a managed project/program.
- Whole-system current view: Accepted goal/project/program and worker/PR lifecycle state with retries, active leases, constraints and waiting steps.
- Current-control decision scope: Live worker allocation, current priority, attempt ceilings, PR acceptance, stall recovery and escalations within a managed repository/program.
- Disturbance / variety regulated: Open goals, unassigned backlog, agent failures/quota limits, stalled PRs, CI status, changing execution resources and disputed completion.
- Decisive decision or feedback right: Choose admitted/pending work by queue priority and availability, select a worker fallback chain, retry within bounded policy, escalate irrecoverable failures and merge only after required current gates.
- Decision owner: First-party deterministic Queue Engine / PR Monitor / delivery controller using accepted human goals and policy; LLM prompt formatting does not itself own whole-current control.
- Supporting / enforcement mechanisms: Persistent goal/queue state, task-priority labels, attempts and worker fallbacks, stage/status files, CI gate, PR monitor, webhook/GitHub feedback and human handoff.
- Closure path: Current issue/goal and queue state → prioritized worker task/PR gate action → status/CI/result observations → retry, merge, blocker or escalation → next current delivery commitments.
- Boundary reachability: The deployed service loop regularly runs queue dispatch and PR monitor and routes real GitHub and worker results back into retained goal/issue state ([orchestrator/queue.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/queue.py); [orchestrator/pr_monitor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/pr_monitor.py); [orchestrator/delivery_program.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/delivery_program.py); [docs/delivery.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/docs/delivery.md)).
- Why this is / is not agent-owned: The decisive ongoing admission/priority/merge policy is implemented by deterministic service components; tools and model-generated issue descriptions support but do not own those decisions.
- Evidence: [orchestrator/queue.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/queue.py); [orchestrator/pr_monitor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/pr_monitor.py); [orchestrator/delivery_program.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/delivery_program.py); [orchestrator/delivery_contract.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/delivery_contract.py)
- Basis: structural
- Confidence: medium
- Caveats: This is a bounded source-first inspection of one frozen supported first-party mode, not a production reliability claim or credit for unshipped external providers.

## S3* — Complementary audit

- State: A
- Function: Separately assess substantive PR code against the linked issue's acceptance criteria using primary diff evidence and an LLM reviewer from a model family independent of the coding worker.
- Claim being audited: A worker's PR actually implements the linked accepted goal.
- Ordinary reporting path: Worker `.agent_result.md`, PR body and own tests.
- Complementary access path: WorkVerifier reads GitHub issue acceptance criteria and actual proposed source diff independently from worker report.
- Independence boundary: Reviewer picks a different model family from the worker and is not the same coding model continuation.
- Who acts on findings: PR Monitor blocks auto-merge and posts a block finding; worker retries or human override/repair returns to subsequent operation.
- Disturbance / variety regulated: Incorrect/stubbed/incomplete code from an otherwise green or plausible worker result, acceptance mismatch or missing tests.
- Decisive decision or feedback right: Inspect first-party fetched PR diff and issue source, judge individual acceptance criteria/scope, block auto-merge and issue review findings or escalations.
- Decision owner: Distinct first-party WorkVerifier model judgment, with independent model-family selection; deterministic PR Monitor enforces its verdict.
- Supporting / enforcement mechanisms: Raw GitHub issue and diff acquisition, code anti-pattern heuristics, fixed review rubric, distinct Claude/Gemini model family, report/override audit, PR Monitor merge block.
- Closure path: Produced PR diff + independent issue criteria → independent model review → stored block/pass with specific findings → PR monitor blocks or permits merge and returns issue comment/Telegram signal for repair/override.
- Boundary reachability: The PR monitor's live merge gate invokes `verify_pull_request` for each qualifying autonomous PR; WorkVerifier enforces a model-family difference from the producing agent and uses actual diff/issue source ([orchestrator/work_verifier.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/work_verifier.py); [orchestrator/pr_monitor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/pr_monitor.py)).
- Why this is / is not agent-owned: A separate model makes the complementary artifact-judgment decision on independently sourced PR data; CI status itself, pass/fail parser and human approval are only enforcement.
- Evidence: [orchestrator/work_verifier.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/work_verifier.py); [orchestrator/pr_monitor.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/pr_monitor.py); [docs/delivery.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/docs/delivery.md)
- Basis: explicit
- Confidence: high
- Caveats: This is a bounded source-first inspection of one frozen supported first-party mode, not a production reliability claim or credit for unshipped external providers.

## S4 — Outside-and-then intelligence

- State: P
- Function: Future delivery adaptation through objective/outcome measurement, external research and model-proposed sprint planning, with legitimate human approval before changing operational commitments.
- External distinction: Observes business/outcome criteria, external research and repository activity rather than just the current executing worker's tool output.
- Future / prospective distinction: Forms next-sprint options and improvements after retrospectives, as opposed to merely selecting the next in-flight task.
- Adaptation option generated: Model-created ranked future backlog/sprint plan constrained by approved goals and measured outcomes.
- Path back into current capability / S3: Human approves selected plan; accepted tickets are promoted into ready work and executed by existing current-control machinery.
- Disturbance / variety regulated: Future product/business objective gaps, external repository changes, recurring reliability risks and emerging capabilities/opportunities beyond a current task.
- Decisive decision or feedback right: Choose whether to accept/reject model-proposed future sprint priorities or capability work and thereby change ready backlog/current team commitments.
- Decision owner: Human parent/operator for plan promotion; first-party strategic planner/model and research system propose but do not independently enact approved priority changes.
- Supporting / enforcement mechanisms: Objective/outcome scorecards, research context, log analysis, strategic model prompt, approval/expiry action, accepted plan promotion and queued tickets.
- Closure path: Observed outcomes/external context → future sprint options proposed by model → explicit human approval/skip → accepted tasks promoted to Ready queue → current S3 dispatcher operates those commitments.
- Boundary reachability: The shipped `strategic_planner` gathers objective/production/research inputs, model-produces a plan and refuses to apply it absent Telegram approval; approval triggers `apply_plan_promotions` and subsequent queue execution ([orchestrator/strategic_planner.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/strategic_planner.py); [orchestrator/objectives.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/objectives.py)).
- Why this is / is not agent-owned: The decisive adaptation commitment is parent-owned; model research/proposals do not constitute autonomous promotion. This is P, not simply scheduled recurrence or S3 task ordering.
- Evidence: [orchestrator/strategic_planner.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/strategic_planner.py); [orchestrator/objectives.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/objectives.py); [orchestrator/agent_scorer.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/agent_scorer.py); [orchestrator/backlog_groomer.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/backlog_groomer.py)
- Basis: explicit + structural
- Confidence: medium
- Caveats: This is a bounded source-first inspection of one frozen supported first-party mode, not a production reliability claim or credit for unshipped external providers.

## S5 — Policy and identity

- State: ?
- Function: Human-chartered goals and autonomy tiers express purpose and authorization, but an operational ultimate-purpose policy revision cycle and complete returned governance feedback remain unestablished.
- Identity / ultimate-policy issue: Whether ultimate organization purpose/charter can be revised as a governed feedback response.
- Ultimate authority in each claimed mode: Human owner of accepted goal scope and rollout tiers, without demonstrated full systemic S5 loop.
- Return-to-operation path: Specific human handoffs may update one accepted goal, but feedback into overarching governing policy is unresolved.
- Disturbance / variety regulated: Legitimate changes of purpose/scope, policy risks, trust in automatic merge, unacceptable commitments.
- Decisive decision or feedback right: Operator sets original accepted-goal scope and tiers and handles escalations; no verified full ultimate-policy adaptation decision loop beyond accepted-delivery governance.
- Decision owner: Human parent/operator and deterministic contract guards, but S5 functional closure remains unresolved at the declared recursion.
- Supporting / enforcement mechanisms: Goal charters, targeted operating model, config scopes, autonomous-rollout stages, human approvals and override log.
- Closure path: Policy/goal settings constrain work; escalation returns human decisions, but ultimate organizational identity/purpose review and returned generalized policy update are not established.
- Why this is / is not agent-owned: Final approval and bounded user goals do not automatically establish complete S5 governance.
- Evidence: [orchestrator/delivery_contract.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/delivery_contract.py); [orchestrator/delivery_program.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/delivery_program.py); [target_operating_model.yaml](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/target_operating_model.yaml); [orchestrator/repo_modes.py](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/orchestrator/repo_modes.py); [docs/delivery.md](https://github.com/kai-linux/agent-os/blob/d7330ebc5e117f06df1fdf23118af8da2c327507/docs/delivery.md)
- Basis: unknown
- Confidence: low
- Caveats: This is a bounded source-first inspection of one frozen supported first-party mode, not a production reliability claim or credit for unshipped external providers.

## Recursion

External model-driven coding workers are the first-party-hosted operating S1 units. First-party isolation/locking and conflict-aware shared repository work bound inter-S1 interference (S2=C). Deterministic persistent goal/task/PR management supplies S3=C at a managed program/project recursion. A separate WorkVerifier model, with independent model family and primary code/criteria data, provides PR-gated S3*=A. Human authorization of model-generated forward-looking sprint/priority proposals gives an externally grounded parent-governed future adaptation mode S4=P, without claiming an autonomous model plan can promote itself. S5 stays unknown.

## Variety and escalation

Worker failures, inconsistent changes and capacity issues enter bounded retries, repo locks, PR health gates and escalation paths. First-party verifier findings block integration while retaining human override records. Longer-horizon goal scores and planning research return through explicitly approved Ready work. Worktree existence, CI status and static charter templates are each less than a higher VSM function absent their traced feedback.

## Evidence gaps

S5 purpose/identity-level governing loop is not fully established from human accepted-goal policy and rollout choices. Need stronger cross-run policy revision evidence to credit it. S4 is limited to the documented human-approved prospective sprint plan mode; no autonomous S4 adoption is claimed. Other external coding/model libraries do not transfer additional organizational functions to this first-party boundary.
