---
harness_id: mini-swe-agent
project_name: mini-swe-agent
repository: https://github.com/SWE-agent/mini-swe-agent
review_ref: 04d809ceab9df28f9adaed044884180159172930
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# mini-swe-agent

## Review boundary
- System in focus: pinned first-party mini-swe-agent Python `DefaultAgent` and shipped `InteractiveAgent` front end, model and command execution backends.
- Purpose and identity: autonomously run an iterative coding/repair session where a model proposes commands and the environment returns results; optional user command confirmation.
- Relevant environment: repository files, shell observations, model responses, execution errors, task prompt and local/container runtime.
- Standard-distribution boundary: published `minisweagent` Python package, built-in simple/interactive runners and local/Docker/Singularity execution backends; external LLM internals, user-composed multi-agent wrappers and unrelated SWE-bench evaluation organization excluded ([README.md](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/README.md); [src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py)).
- Credited operating / distribution surfaces: [src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py); [src/minisweagent/agents/interactive.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/interactive.py); [src/minisweagent/run/mini.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/run/mini.py); [src/minisweagent/environments/local.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/local.py); [src/minisweagent/environments/docker.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/docker.py); [src/minisweagent/models/litellm_model.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/models/litellm_model.py); [src/minisweagent/config/default.yaml](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/config/default.yaml).
- Adjacent first-party surfaces excluded from ownership: SWE-bench bulk evaluation queues, tests/CI, docs-only proposed configurations, external model services or alternative SWE-agent runtimes, parent multi-agent systems written by users.
- First-party operating / deployment modes considered: baseline `DefaultAgent` run, interactive `human`/`confirm`/`yolo` confirmation modes, local/Docker/Singularity environment execution, standard model provider adapters and configured task boundaries.
- Recursion level: one coding-agent session with one model and environment; no first-party portfolio/worker team is credited simply because multiple CLI processes can be launched.
- Reviewed revision: `04d809ceab9df28f9adaed044884180159172930`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
DefaultAgent exposes a compact `run` loop that alternates `query` model calls and `execute_actions` over an Environment with returned observation messages; it stops on submitted exit or step/cost/time limits. The supported mini runner constructs the agent and an execution backend. InteractiveAgent adds optional human approval to individual command execution but uses the same underlying operating loop ([src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py); [src/minisweagent/agents/interactive.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/interactive.py); [src/minisweagent/run/mini.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/run/mini.py)).
There is no bundled delegate-agent team scheduler, independent PR auditor, prospective capability adaptation service or identity-governance controller in this pinned installed package. Model adapters and environment objects support S1 rather than serving independent S1 workers. [src/minisweagent/models/litellm_model.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/models/litellm_model.py); [src/minisweagent/environments/local.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/local.py); [src/minisweagent/environments/docker.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/docker.py).

## Operational model
A user task is represented in a prompt template. The model returns executable commands; the agent runs them against the chosen environment and records observations for future turns. Independent human confirmations do not change task-local action rights into VSM S5. The standard distribution remains one operating agent, without a proven higher recursion.

## S1 — Operations

- State: A
- Function: Direct first-party model/tool turn loop performs a coding task against a local or container execution environment.
- Disturbance / variety regulated: Uncertain task request, shell/tool errors, changing workspace files and model responses.
- Decisive decision or feedback right: Select environment commands/actions from current model context and revise after observed results.
- Decision owner: Model-driven DefaultAgent (or InteractiveAgent inheriting it) makes task-specific execution choices.
- Supporting / enforcement mechanisms: Model.query, Environment.execute, Jinja templates, observation messages, exit/step/time/cost bounds.
- Closure path: Task and prompt history → model proposes actions → environment executes → returned observations → next model query or stop.
- Boundary reachability: First-party CLI entrypoint constructs DefaultAgent/InteractiveAgent and invokes `run`; actual shell/environment execution occurs through `execute_actions`, not a toy graph.
- Why this is / is not agent-owned: Task-specific model choice drives actual environment operations; deterministic limits and environment runners are supporting mechanisms.
- Evidence: [src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py); [src/minisweagent/environments/local.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/local.py); [src/minisweagent/models/litellm_model.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/models/litellm_model.py); [src/minisweagent/run/mini.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/run/mini.py)
- Basis: structural
- Confidence: high
- Caveats: This is a bounded first-party standard-distribution assessment at the frozen SHA, not a universal claim about possible user-built wrappers.

## S2 — Coordination

- State: —
- Function: No first-party inter-S1 interference attenuation at the declared single-agent distribution boundary.
- Distinct S1 units: Only the one current DefaultAgent/InteractiveAgent is evidenced; external separate invocations are not owned subagents.
- Inter-S1 disturbance: No shipped interacting worker fleet whose conflicts/oscillations require coordination.
- Attenuating coordination relation: No joint-work arbitration, conflict feedback or external worker resource rights found.
- Feedback into subsequent S1 behaviour: Own action observations feed only the same S1 agent.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A single model turn/action loop is not an S2 coordination relation.
- Disturbance / variety regulated: Potential multi-agent content/file collisions are absent as a coordinated first-party operating mode; a user can separately launch processes outside this one-agent recursion.
- Decisive decision or feedback right: No inter-worker arbitration right among distinct operating agents is implemented.
- Decision owner: No S2 owner at the declared one-agent boundary.
- Supporting / enforcement mechanisms: One model/agent and one Environment; step loop serially dispatches selected commands.
- Closure path: Only a single agent's actions and observations return to itself; no cross-agent conflict or corrected coordination path.
- Why this is / is not agent-owned: No first-party function-specific higher-level owner or full closure exists in the inspected supported single-agent modes.
- Evidence: [src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py); [src/minisweagent/agents/interactive.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/interactive.py); [src/minisweagent/run/mini.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/run/mini.py); [src/minisweagent/environments/local.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/local.py)
- Basis: structural
- Confidence: medium
- Caveats: This is a bounded first-party standard-distribution assessment at the frozen SHA, not a universal claim about possible user-built wrappers.

### Absence scope
- Surfaces inspected: S1 runner, core loop, interactive command confirmation, local/Docker environment and CLI construction.
- Plausible first-party paths checked: Searched for shipped team/worker spawn, coordination of independent changing workspaces, actor messaging, merge or contention arbitration.
- Why no material first-party path remains: Packaged runtime only instantiates one acting model-agent and executes its commands; no materially independent S1 units or inter-S1 coordination loop exists.

## S3 — Inside-and-now control

- State: —
- Function: No separate whole-current operational director controlling a plurality of independently acting agents or resource commitments.
- Whole-system current view: Only one agent's messages, execution count, cost, wall time and command observations.
- Current-control decision scope: Individual command/turn limits, not team resources and commitments.
- Disturbance / variety regulated: Task step/time/cost state and human command confirmations apply to one running task rather than team portfolio.
- Decisive decision or feedback right: Model selects the next operating step, while static limits terminate; no above-S1 resource bargaining/priority intervention.
- Decision owner: None established at a higher team recursion; the single operating agent owns task-local decisions.
- Supporting / enforcement mechanisms: step_limit, cost_limit, wall_time_limit_seconds, InteractiveAgent prompt and parent process.
- Closure path: Step cost/errors → terminate or next action of same S1; no independent worker reports → whole-system control → modified shared commitments.
- Why this is / is not agent-owned: No first-party function-specific higher-level owner or full closure exists in the inspected supported single-agent modes.
- Evidence: [src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py); [src/minisweagent/agents/interactive.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/interactive.py); [src/minisweagent/run/mini.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/run/mini.py); [src/minisweagent/config/default.yaml](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/config/default.yaml)
- Basis: structural
- Confidence: medium
- Caveats: This is a bounded first-party standard-distribution assessment at the frozen SHA, not a universal claim about possible user-built wrappers.

### Absence scope
- Surfaces inspected: DefaultAgent `run`/`step`/`query`, InteractiveAgent confirmation modes, CLI runner and environment modules.
- Plausible first-party paths checked: Examined potential parent supervision, active worker rosters, commitment reassignment, resource prioritization and human parent-governed current-control mode.
- Why no material first-party path remains: All inspected modes manage one operating loop; a budget cap or confirmation of an individual shell command is neither portfolio control nor S3 parent-loop authority.

## S3* — Complementary audit

- State: —
- Function: No separate, sufficiently independent complementary inspection of operational reality challenging produced task claims in the bundled agent.
- Claim being audited: Model's code/task completion claim.
- Ordinary reporting path: Model messages and its own environment command output.
- Complementary access path: No independent source/artifact observation owner, only ordinary tool observations.
- Independence boundary: Separate reviewer or audit process unavailable in standard distribution.
- Who acts on findings: None; ordinary tool errors alter the same agent's next actions.
- Disturbance / variety regulated: Incorrect task completion/code is not separately audited by a first-party observer; ordinary command feedback remains in S1.
- Decisive decision or feedback right: No distinct audit sampling/judgment right beyond ordinary model/tool observations and optional human confirmation of commands.
- Decision owner: None; model observes its own executed commands and optional user approves individual actions.
- Supporting / enforcement mechanisms: Command stdout/stderr and exit observations, serialized trajectory and ordinary task feedback.
- Closure path: Tool execution output goes to its own producing model, not independently sampled and judged with corrective control.
- Why this is / is not agent-owned: No first-party function-specific higher-level owner or full closure exists in the inspected supported single-agent modes.
- Evidence: [src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py); [src/minisweagent/agents/interactive.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/interactive.py); [src/minisweagent/environments/local.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/local.py); [src/minisweagent/run/mini.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/run/mini.py)
- Basis: structural
- Confidence: medium
- Caveats: This is a bounded first-party standard-distribution assessment at the frozen SHA, not a universal claim about possible user-built wrappers.

### Absence scope
- Surfaces inspected: Default/Interactive model loop, observation formatter, execution environment, trajectory and run entrypoint.
- Plausible first-party paths checked: Checked for independently executing reviewer/auditor, direct artifact sampling against producer's claim, independent judgment and returned findings to a governing controller.
- Why no material first-party path remains: Only task-internal stdout/stderr and user action approvals exist; no distinct complementary code-audit path or owner is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party outside-and-prospective organizational capability adaptation loop beyond immediate coding task work.
- External distinction: User task and model-supplied context are not ongoing external environmental horizon sensing.
- Future / prospective distinction: Serialized trajectories and static templates alone are not future capability redesign.
- Adaptation option generated: No qualifying organizational future-adaptation option.
- Path back into current capability / S3: No separate capability-changing return beyond ordinary new prompt.
- Disturbance / variety regulated: Future environment opportunity/threat and system redesign are outside this task-bounded loop.
- Decisive decision or feedback right: Agent can adapt the next command, but cannot select and apply a future organizational capability adaptation in a shipped separate function.
- Decision owner: No prospective S4 authority; user chooses static model, environment and configuration.
- Supporting / enforcement mechanisms: Config YAML, model provider wrapper, task conversation and saved trajectory.
- Closure path: Messages inform the current task only; no external future observation → adaptation option → changed operational capability loop.
- Why this is / is not agent-owned: No first-party function-specific higher-level owner or full closure exists in the inspected supported single-agent modes.
- Evidence: [src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py); [src/minisweagent/models/litellm_model.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/models/litellm_model.py); [src/minisweagent/config/default.yaml](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/config/default.yaml); [src/minisweagent/run/mini.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/run/mini.py)
- Basis: structural
- Confidence: medium
- Caveats: This is a bounded first-party standard-distribution assessment at the frozen SHA, not a universal claim about possible user-built wrappers.

### Absence scope
- Surfaces inspected: Core query/execute loop, config, model providers, local/Docker environments and serialization.
- Plausible first-party paths checked: Inspected externally sourced future scanning, prospective option generation, persistent skill/organization changes and return into current agent capability.
- Why no material first-party path remains: The fixed session tasks and static config expose neither ongoing system adaptation ownership nor adoption/feedback; logs and repeat runs are not foresight.

## S5 — Policy and identity

- State: —
- Function: No ultimate organizational identity/policy governance loop in the single-agent standard distribution.
- Identity / ultimate-policy issue: Who chooses and revises overarching organization purpose and authority.
- Ultimate authority in each claimed mode: Outside user, not an operational first-party parent governance loop.
- Return-to-operation path: Action confirmation governs one command, not ultimate organizational policy.
- Disturbance / variety regulated: Command approvals, tool limits and user-chosen settings bound local execution, not the systemic identity/purpose of an agent organization.
- Decisive decision or feedback right: User may approve/deny an individual action and set static modes, not govern ultimate purpose via an operational returned decision loop.
- Decision owner: User/developer external to the assessed single-agent organization; no first-party parent S5 closure.
- Supporting / enforcement mechanisms: InteractiveAgent human/confirm/yolo mode and regular-expression allowlist, task template, execution cost and step limits.
- Closure path: Command action → user allow/deny → one action executes or cancels; no ultimate purpose/identity review and return that governs an organization.
- Why this is / is not agent-owned: No first-party function-specific higher-level owner or full closure exists in the inspected supported single-agent modes.
- Evidence: [src/minisweagent/agents/interactive.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/interactive.py); [src/minisweagent/config/default.yaml](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/config/default.yaml); [src/minisweagent/agents/default.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py); [src/minisweagent/run/mini.py](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/run/mini.py)
- Basis: structural
- Confidence: medium
- Caveats: This is a bounded first-party standard-distribution assessment at the frozen SHA, not a universal claim about possible user-built wrappers.

### Absence scope
- Surfaces inspected: InteractiveAgent confirmation modes and allowlist, YAML config, CLI model selection and DefaultAgent bounds.
- Plausible first-party paths checked: Checked explicit policy/identity adaptation authority, organization-level human parent governance and feedback that changes ongoing purpose/policy.
- Why no material first-party path remains: Available control only approves task commands or sets static parameters; no independent system-identity decision or continuing ultimate-policy loop is implemented.

## Recursion

One `DefaultAgent` or `InteractiveAgent` session is the S1 operating unit; command-execution environment and model service are supporting subsystems, not separately performing first-party independent agent work. Higher S2/S3/S3*/S4/S5 organization and its ownership are not present in this inspected single-agent boundary.

## Variety and escalation

Dynamic task conditions enter via model prompts and command observations. A failed command returns data to the same model for correction. Budget/step/time termination and user approval are execution-level guards. No cross-agent escalation, independently sampled audit or long-horizon organization/policy adaptation paths were found.

## Evidence gaps

No live provider-backed coding task was run; source reachability is structural. All five negative assessments are bounded to the exact installed first-party single-agent CLI distribution and include explicit absence scopes over the plausible shipped alternatives. User-created multi-agent wrappers, hosted provider systems and future plugin behavior are excluded from this evaluation.
