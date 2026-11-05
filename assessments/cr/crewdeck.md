---
harness_id: crewdeck
project_name: CrewDeck
repository: https://github.com/mnbresearch/crewdeck
review_ref: 7925ffb4c5e922f0081cce9ca59f62190b6e7864
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CrewDeck

## Review boundary

- System in focus: one self-hosted CrewDeck company with registered agent participants, tasks/goals, the Node dispatcher/remote-worker API, persisted operating state and operator board.
- Purpose and identity: coordinate a company-shaped portfolio of delegated AI-agent work, its dependencies, current spending and task acceptance.
- Relevant environment: changing human requests, external CLI/HTTP agents, failed or slow work, constrained budgets, shared tasks and dependent deliverables.
- Standard-distribution boundary: the shipped `node crewdeck.mjs` server, shared state engine, shell/HTTP/remote adapters, and configured participant agents. The `sim` adapter demonstrates control without supplying an autonomous S1 decision.
- Credited operating / distribution surfaces: [self-hosted entry, scheduler and API](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/crewdeck.mjs), [task/agent/governance state engine](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs), [external agent execution adapters](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/runner.mjs) and [documented operating modes](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/README.md).
- Adjacent first-party surfaces excluded from ownership: static in-browser simulation and demo seeded actors, screenshot fixtures, repository development/tests, and unimplemented external agents' internal managers/auditors/strategists.
- First-party operating / deployment modes considered: configured shell agent, HTTP agent, remote polling agent, human/manual task, optional approval, routines and budgets; simulated demo is corroboration of mechanics only.
- Recursion level: the installed company-level work-portfolio harness; individual provider agents and their own private internal organizations are lower or external recursions.
- Reviewed revision: `7925ffb4c5e922f0081cce9ca59f62190b6e7864`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

CrewDeck is a zero-dependency Node HTTP server with a JSON snapshot, a three-second dispatcher tick and a pure state engine shared with the browser demo. An operator creates agents, goals, assignments, dependencies, budgets, routines and approval requirements through API/UI. The dispatcher selects a runnable assigned task, claims a per-task and per-agent lock, builds a mission/goal/task/prerequisite/comment prompt and invokes a configured shell or HTTP agent; a remote worker can instead poll and complete the run. Completion persists output and cost, makes the task done or awaiting human review, or retries/fails it. Operators may change the portfolio, pause agents, approve or request work again. On server restart a running task is failed rather than silently reported complete. [Engine](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs); [server/remote API](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/crewdeck.mjs); [adapters](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/runner.mjs).

## Operational model

Each configured external AI agent supplies its own task-local model discretion and work product. CrewDeck deliberately does not implement those models; it organizes the supported invocation, prompt, output and next-task loop. One agent's result may enter a dependent agent's later task. Human operators decide company mission, goals, assignments, priority, spending allowance and acceptance. The engine deterministically enforces claims, limits and transitions; those safeguards are not agent-owned organizational decisions. [Task/agent construction and execution](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L22-L267); [runner](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/runner.mjs).

## S1 — Operations

- State: A
- Function: configured autonomous participant agents execute assigned coding/research/other tasks and return results into the company portfolio.
- Disturbance / variety regulated: task requirements, tool outputs, errors and changing local work conditions faced by each participating agent.
- Decisive decision or feedback right: each invoked autonomous CLI/HTTP worker chooses how to perform its assigned task and returns an outcome; CrewDeck decides neither the model's work steps nor its answer.
- Decision owner: the configured external agent actor for task-local S1 discretion; human/manual and simulation modes do not supply this autonomous state.
- Supporting / enforcement mechanisms: `nextTaskFor`, `claim`, context prompt assembly, shell/HTTP/remote adapters, run outputs, status transitions and persisted state.
- Closure path: operator creates an assigned task → scheduler/remote claim supplies context to the AI agent → agent works and reports → `completeRun` records the outcome and result/cost → later tasks consume the result or the same work is retried/approved.
- Boundary reachability: shell/HTTP agent adapters are shipped and directly called by the real server tick; remote participants have a shipped claim/complete protocol. The documented CLI examples require user-supplied providers and do not imply internal provider capabilities are CrewDeck's own metasystem.
- Why this is / is not agent-owned: the external agent makes meaningful task-specific execution decisions in the supported assembled operating mode; CrewDeck's deterministic queue/rules do not acquire that discretion.
- Evidence: [README launch and agent adapter modes](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/README.md), [server dispatch and remote claim/complete](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/crewdeck.mjs#L48-L137), [runner implementation](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/runner.mjs#L8-L94).
- Basis: structural, supported configuration and first-party wiring.
- Confidence: medium-high for reachable assembled agent execution; no live proprietary provider run was performed in this review.
- Caveats: neither browser `sim` nor a manual user task demonstrates agent ownership, and no foreign agent's S2–S5 is inherited.

## S2 — Coordination

- State: C
- Function: explicit ownership/lock and dependency guards attenuate competing execution and premature consumption of work across distinct participating agents.
- Disturbance / variety regulated: two agent workers claiming the same task/agent capacity concurrently and downstream work starting before its prerequisite result is available.
- Decisive decision or feedback right: assigned task identity and dependency choice originate in portfolio configuration; deterministic first-party claim eligibility denies incompatible concurrent starts and releases locks on completion/timeout.
- Decision owner: operator/configuration for assignment/dependency intent and deterministic runtime for fixed admission; there is no autonomous agent selecting/revising the inter-agent coordination policy at this boundary.
- Supporting / enforcement mechanisms: per-task run lock with expiry, one-task-per-agent invariant, `blockedBy`, cycle checks and status/attempt state.
- Closure path: candidate agent run is tested against assignment, live locks and completed prerequisites → conflicting claim is rejected or deferred → a completed/expired run releases the lock and changes subsequent eligibility.
- Boundary reachability: the same `claim` and `nextTaskFor` invariants are called in real server dispatch and remote polling and are exercised by first-party engine tests.
- Why this is / is not agent-owned: the anti-contention path is function-specific and operational, but its decisive policy is configured/deterministic. An autonomous coordinating owner would require further composition; generic agent-to-agent conversation is not claimed.
- Distinct S1 units: independently configured shell/HTTP/remote participants performing different assigned tasks at the company recursion.
- Inter-S1 disturbance: competing workers could otherwise double-execute a shared work item, or a consumer agent could act on incomplete producer output.
- Attenuating coordination relation: exclusive task/worker claims plus explicit completed-prerequisite gating and dependency-cycle rejection.
- Feedback into subsequent S1 behaviour: denied claims remain unstarted; completion or timeout changes eligibility; dependent agents receive completed producer summaries only once prerequisite tasks reach `done`.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive witness is the source-enforced concurrent-claim conflict and consumption-of-incomplete-output prevention, not the mere existence of task ordering or a board.
- Evidence: [selection, claim, completion, lock expiry](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L130-L245), [claimed-node tests](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/tests/engine.test.mjs), [real server dispatch](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/crewdeck.mjs#L48-L78).
- Basis: structural first-party code and passing offline tests.
- Confidence: medium; the lock conflict is direct, whereas broader semantic work-product interference is not resolved by this mechanism.
- Caveats: no independent agent negotiates shared files or autonomously revises coordination policy.

## S3 — Inside-and-now control

- State: P
- Function: the company operator reviews whole-portfolio current tasks, staff capacity and spend and sets effective resource, priority and commitment constraints.
- Disturbance / variety regulated: competing work, agent availability, constrained cost and tasks that fail or await review.
- Decisive decision or feedback right: human operator creates/reassigns/prioritizes tasks, changes budgets/pauses and approves or requests rework across the company portfolio.
- Decision owner: legitimate installed company owner/operator; the server merely enforces selected rules and makes current state visible.
- Supporting / enforcement mechanisms: `/api/state` and `/api/summary`, UI and editing API, budget accounting and hard dispatch stop, task review and status ledger.
- Closure path: operator inspects shared current state → changes assigned worker, task priority or monthly budget, pauses an agent or rejects a reviewed task → saved state and next dispatcher tick govern subsequent commitments and execution.
- Boundary reachability: the shipped self-hosted API exposes whole-company state and operator mutations that the same production dispatch path immediately consumes.
- Why this is / is not agent-owned: an AI agent may perform an assigned task, but no shipped agent owns company-wide current prioritization or budget selection; numerical sorting and hard stops enforce human settings.
- Whole-system current view: `summary` spans task statuses, active agents, total current spend and waiting reviews, with full state available to the board.
- Current-control decision scope: organization-wide worker availability, priority, task assignment and cost envelopes, plus returned acceptance/rework control.
- Evidence: [summary and controls](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L22-L151), [budget/review gates](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L175-L267), [operating API](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/crewdeck.mjs#L83-L137).
- Basis: explicit operator mode and structural return-to-dispatch.
- Confidence: high for installed human current-control path.
- Caveats: a human's acceptance of an individual deliverable alone is not S3; the positive mapping relies on the broader current portfolio view and cross-agent authority.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary independent audit loop over operational truth is established.
- Disturbance / variety regulated: false self-reported completion or faulty work would require evidence outside the ordinary participant result and routine operator approval.
- Decisive decision or feedback right: not supplied as a distinct audit judgment; generic human `approve/reject` of the returned output is task acceptance.
- Decision owner: no separate first-party auditor identified.
- Supporting / enforcement mechanisms: ordinary result comments, run log, review state and operator approval.
- Closure path: no complementary independently sourced findings-to-current-control path supplied.
- Why this is / is not agent-owned: recordkeeping and task acceptance do not create independence from the agent's own report.
- Evidence: [completion and approval flow](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L207-L265), [adapter-reported result](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/runner.mjs).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: a separately configured reviewer agent could be given a task, but no shipped independent evidence path is wired as a company-level audit loop.

### Absence scope

- Surfaces inspected: README modes, engine task/approval code, server routes, adapter outputs, tests and demo.
- Plausible first-party paths checked: `requiresApproval`, result logging, routine tasks, agent hierarchy and optional reviewer work assignments.
- Why no material first-party path remains: these consume ordinary output or require a separately composed operator/task arrangement; none supplies a complementary evidence channel and independent audit judgment with returned current-control closure in the standard distribution.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally/prospectively coupled capability-adaptation loop is established.
- Disturbance / variety regulated: market, user, model/tool or other future change is not sensed and turned into a runtime capability change by CrewDeck.
- Decisive decision or feedback right: absent; humans can edit the portfolio and agents can research as task work, but no shipped S4 feedback path selects future adaptations.
- Decision owner: not established at the company boundary.
- Supporting / enforcement mechanisms: goals, routine task generation, company mission field and task comments.
- Closure path: no separate outside/future model → adaptation proposal → current capability revision path.
- Why this is / is not agent-owned: ordinary planning and scheduled repetition do not establish S4.
- Evidence: [goal/task construction and routines](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L89-L119), [routine tick](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L290-L323).
- Basis: structural bounded negative.
- Confidence: high for inspected shipped composition.
- Caveats: future adaptation could be implemented by external bots through generic APIs; such a hypothetical composition is not present evidence.

### Absence scope

- Surfaces inspected: server dispatch and APIs, engine goals/routines/tasks, README feature claims, adapters and tests.
- Plausible first-party paths checked: recurring tasks, changing human goals, prompt context and external HTTP workers.
- Why no material first-party path remains: fixed repetition and task-local research do not close a first-party externally informed prospective adaptation loop back into company-level capability.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy disagreement or exceptional matter is routed to legitimate final authority and returned as a governing resolution.
- Disturbance / variety regulated: tension over company mission, ethos or final operating constraints is not handled by a separate runtime identity-policy loop.
- Decisive decision or feedback right: no S5-level closed path; the human directly edits company name/mission and ordinary runtime settings.
- Decision owner: human configuration authority exists, but no evidenced first-party S5 decision transaction is supplied.
- Supporting / enforcement mechanisms: company mission string in state/prompt, human API settings and approval/budget controls.
- Closure path: static mission is passed into future task prompts; no surfaced identity matter → legitimate ultimate decision → returned resolution loop.
- Why this is / is not agent-owned: a mission string and task approvals are not an authoritative identity/policy decision process.
- Evidence: [company state and prompt](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L9-L12), [mission ingestion](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/lib/engine.mjs#L267-L288), [company API and operator controls](https://github.com/mnbresearch/crewdeck/blob/7925ffb4c5e922f0081cce9ca59f62190b6e7864/crewdeck.mjs#L96-L113).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: the host human can always change values out-of-band, but this does not itself establish first-party S5 closure.

### Absence scope

- Surfaces inspected: README, engine company/task/agent state, server API, approval gates, tests and demo.
- Plausible first-party paths checked: editable mission, budgets, role hierarchy, human approvals, import/export and operator intervention.
- Why no material first-party path remains: those are direct configuration or current-task/current-control operations, not an identity-level matter with legitimate decisive review and return-to-operation transaction.

## Recursion

Participant agents have their own task-local environments and may run complex external harnesses, but CrewDeck exposes them primarily as registered workers. The `reportsTo` hierarchy and nested tasks do not prove a complete recursive VSM for each worker. The assessed recursion is the installed company portfolio.

## Variety and escalation

Assignment and priority reduce task-selection variety; locks and prerequisites prevent some harmful concurrent states; spend counters and review states expose current exceptions. A failing run is retried up to `maxAttempts`, then failed; an approval requirement returns work to a human. These are bounded current-work controls and are not, by themselves, evidence of an exceptional algedonic channel or S4/S5 ownership.

## Evidence gaps

- Review is based on pinned first-party source, README and nine passing offline Node tests; no live Claude/Codex/other external agent subscription was used and actual third-party work quality is not claimed.
- The S2 evidence is specific to execution reservation and prerequisite interference. Agent-authored negotiation over shared workspaces and cross-agent semantic conflict handling are not shown.
- No inferred VSM decision rights are borrowed from external worker providers or the standalone browser demo.
