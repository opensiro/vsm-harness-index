---
harness_id: ironclaw
project_name: IronClaw
repository: https://github.com/nearai/ironclaw
review_ref: b0b999d96781516ee05e6ba961d6f3ead900da96
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-21
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: —
---

# IronClaw

## Review boundary

- System in focus: one first-party IronClaw Agent OS instance at pinned revision `b0b999d96781516ee05e6ba961d6f3ead900da96`, including the canonical agent loop, job/routine execution, scheduler and self-repair, built-in job-control tools, memory, skills/extensions and runtime authorization/approval surfaces.
- Purpose and identity: operate a persistent personal AI agent that can execute tool-using turns and background jobs, manage concurrent work, retain state and extend recurring behavior while enforcing the user's configured security boundary.
- Relevant environment: user requests and learned user context, external services and model/tool results, concurrent job load, provider/system capacity, routine schedules/events and installed capabilities.
- Standard-distribution boundary: the shipped `ironclaw` product and first-party runtime surfaces at the pinned revision. External model providers, MCP servers, user-written extensions, repository-development agents, CI/release governance and maintainer audit documents are outside organizational ownership.
- Credited operating / distribution surfaces: `ironclaw` application/composition path; `ironclaw_agent_loop` canonical executor and planner; standard job/routine tools and scheduler; runtime self-repair; shipped `routine-advisor` skill; first-party authorization/approval and extension runtime mechanisms.
- Adjacent first-party surfaces excluded from ownership: `.claude` contributor commands/skills, CodeRabbit configuration, internal architecture/development audits, benchmark/test-only surfaces, repository governance and maintainer remediation work.
- First-party operating / deployment modes considered: normal interactive agent turns, parallel/background jobs, routines, self-repair and the standard user-confirmed routine-advisor path.
- Recursion level: one IronClaw personal-agent organization. Concurrent jobs are distinct operational S1 units when they independently run model/tool work under isolated contexts; the parent interactive agent can inspect/control the current job portfolio.
- Reviewed revision: `b0b999d96781516ee05e6ba961d6f3ead900da96`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

IronClaw ships a canonical model/tool loop rather than merely proxying an external agent runtime. The Reborn architecture routes durable turns through a canonical runner/driver into `CanonicalAgentLoopExecutor`; planning, capability discovery/authorization, execution results, checkpoints and subsequent model steps remain first-party runtime surfaces. Jobs use the same operational substrate in isolated contexts and may run concurrently.

The job subsystem exposes a bounded shared execution pool. Jobs can be Pending, InProgress, Completed, Failed or Stuck; each active job has isolated conversation/tool context. `MAX_PARALLEL_JOBS` caps simultaneous jobs, and excess jobs remain Pending until a slot opens. The documentation explicitly connects the cap to shared LLM-provider concurrency and available system resources. This is a concrete cross-S1 resource-contention attenuation path, but the scheduling decision is deterministic runtime policy rather than an autonomous coordinating agent.

Inside-and-now control is separately available to the model agent. Standard tools let it create jobs, list all active jobs with state/metadata, inspect an individual job and cancel Pending/InProgress work. Thus the agent can obtain a current portfolio view and alter current commitments; scheduler limits and stuck-job recovery remain supporting enforcement, not the S3 owner.

Self-repair is intentionally not credited as S3*. A background monitor scans all InProgress jobs for inactivity, deterministically marks them Stuck, consults retry history, restarts from a checkpoint or fails the job. Failure history is fed to the retried worker so it can avoid the failed approach, but there is no independent complementary auditor making a distinct claim about operational reality. Repository security/design audits and contributor review agents are adjacent development-system evidence and are excluded from the runtime ownership boundary.

A qualifying future-adaptation path exists through the shipped `routine-advisor` skill, but the decisive right is retained by the user. The skill is instructed to notice recurring behavior, forgetting, periodic requests and learned user patterns, formulate a concrete future routine, and **always wait for user confirmation before creating it**. On confirmation, `builtin__trigger_create` installs the persistent scheduled program whose later fires alter future operation. That establishes parent-governed S4 rather than autonomous S4. Dynamic tool discovery/building and extension installation broaden available capability, but the reviewed evidence does not independently establish a prospective autonomous environment→adaptation loop beyond the explicit parent-governed routine path.

Primary evidence:

- [`README.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md) — shipped Agent OS, autonomous execution, jobs/routines, memory, safety and extension surfaces.
- [`AGENTS.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/AGENTS.md) — current product routing through durable thread/turn services, scheduler/run executor and canonical agent loop.
- [`crates/loop/ironclaw_agent_loop/README.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/crates/loop/ironclaw_agent_loop/README.md) — `CanonicalAgentLoopExecutor`, planner and loop public surface.
- [`docs/capabilities/jobs/jobs.mdx`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/capabilities/jobs/jobs.mdx) — job state machine, isolated parallel jobs, bounded concurrency and `create_job`/`list_jobs`/`job_status`/`cancel_job` tools.
- [`docs/capabilities/jobs/self-repair.mdx`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/capabilities/jobs/self-repair.mdx) — deterministic stuck detection/retry flow and returned failure history.
- [`skills/routine-advisor/SKILL.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/skills/routine-advisor/SKILL.md) — pattern-derived future automation proposal, mandatory user confirmation and persistent routine creation.
- [`crates/loop/ironclaw_loop_host/prompts/tool_disclosure_protocol.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/crates/loop/ironclaw_loop_host/prompts/tool_disclosure_protocol.md) — runtime capability discovery when the current agent needs an unavailable/undisclosed tool.

## Operational model

An inbound request becomes a durable turn and enters the canonical model/tool execution loop. The model plans and chooses capabilities; first-party runtime layers authorize and execute them, return observations and checkpoint state, and the loop continues until a terminal result. Background jobs are additional operational loops with their own contexts.

Concurrent jobs share provider and machine capacity. IronClaw limits simultaneous execution and queues the excess, while keeping job contexts isolated. The parent agent can inspect all active jobs and alter the current work portfolio with job-control tools. A separate timeout monitor handles mechanical recovery of stuck work.

For future recurring work, the routine advisor can recognize a pattern across user interaction/context and propose a durable automation. The user must approve the adaptation before it is installed; after creation, future routine fires become part of normal operation.

## S1 — Operations

- State: A
- Function: execute user-directed or background work through a model-driven plan/tool/observation loop and produce operational outcomes.
- Disturbance / variety regulated: ambiguous requests, tool/service observations, model results, persistent context, capability availability and execution failures.
- Decisive decision or feedback right: choose substantive next actions/tools and revise the plan from returned observations within configured authority.
- Decision owner: the running IronClaw model agent/job.
- Supporting / enforcement mechanisms: canonical executor/planner, durable turn state, capability resolver, authorization/approval gates, tool runtimes, checkpoints and model transport.
- Closure path: request/job state → model decision → authorized capability/tool action → returned observation/checkpoint → subsequent model decision → result.
- Boundary reachability: the shipped `ironclaw` composition invokes the first-party canonical agent-loop executor; no downstream harness must be supplied to create the operational model/tool loop.
- Why this is / is not agent-owned: runtime code transports and constrains actions, while the model loop owns the substantive choice of action and follow-up from current evidence.
- Evidence: [`AGENTS.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/AGENTS.md), [`crates/loop/ironclaw_agent_loop/README.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/crates/loop/ironclaw_agent_loop/README.md), [`README.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external execution substrate, not an imported organizational owner.

## S2 — Coordination

- State: C
- Function: attenuate shared provider/system-capacity contention among distinct concurrently runnable job S1 units.
- Disturbance / variety regulated: too many jobs simultaneously consuming finite LLM-provider concurrency and local runtime resources.
- Decisive decision or feedback right: admit a Pending job to execution only when a concurrency slot is available.
- Decision owner: first-party deterministic scheduler/concurrency policy; no autonomous S2 actor is established.
- Supporting / enforcement mechanisms: isolated job contexts, `MAX_PARALLEL_JOBS`, Pending queue and creation-order dispatch.
- Closure path: concurrent runnable jobs exceed the configured shared-capacity envelope → excess work remains Pending → completion/cancellation frees a slot → scheduler admits queued work → subsequent S1 execution proceeds inside the bounded envelope.
- Boundary reachability: parallel jobs and the bounded scheduler are standard first-party job behavior documented for the shipped instance; no downstream coordinator is required.
- Why this is / is not agent-owned: the S2-specific attenuation relation is first-party and operational, but the coordination decision is deterministic policy rather than a model agent choosing how to reconcile the competing units.
- Evidence: [`docs/capabilities/jobs/jobs.mdx`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/capabilities/jobs/jobs.mdx), [`docs/capabilities/routines/cron.mdx`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/capabilities/routines/cron.mdx), [`.env.example`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/.env.example).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: generic job sequencing is not the basis; the credited witness is bounded shared-capacity contention across concurrently runnable S1 jobs.
- Distinct S1 units: independently executing IronClaw jobs with isolated contexts.
- Inter-S1 disturbance: simultaneous jobs contend for shared LLM-provider concurrency and available instance resources.
- Attenuating coordination relation: a first-party maximum-concurrency envelope and Pending queue prevent all runnable jobs from consuming the shared resource at once.
- Feedback into subsequent S1 behaviour: queued units remain Pending and become InProgress only after another unit releases capacity.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the queue/cap is explicitly tied to the finite shared capacity that concurrent S1 execution would otherwise overrun; it regulates a concrete cross-unit interference rather than merely choosing message order.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current portfolio of active/pending background work for the IronClaw instance.
- Disturbance / variety regulated: new work demand, current job state, stalled or no-longer-needed jobs and changing current priorities.
- Decisive decision or feedback right: create new work, inspect the full active-job portfolio/status and cancel current Pending/InProgress commitments.
- Decision owner: the model-driven IronClaw agent using the standard job-control tools.
- Supporting / enforcement mechanisms: job repository/state machine, scheduler, `create_job`, `list_jobs`, `job_status`, `cancel_job` and self-repair state transitions.
- Closure path: current job portfolio/state → agent `list_jobs`/`job_status` observation → model current-control decision → create/cancel/continue action → scheduler/job state changes → new portfolio state available to the agent.
- Boundary reachability: all four job-control capabilities are documented as built-in tools in the shipped job subsystem and are available to the standard agent path.
- Why this is / is not agent-owned: scheduler and self-repair enforce mechanics, but the discretionary decision to add or cancel current commitments from the current portfolio is made by the model agent.
- Evidence: [`docs/capabilities/jobs/jobs.mdx`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/capabilities/jobs/jobs.mdx), [`docs/capabilities/jobs/self-repair.mdx`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/capabilities/jobs/self-repair.mdx).
- Basis: explicit.
- Confidence: high.
- Caveats: timeout/retry and concurrency enforcement are not treated as autonomous S3 ownership.
- Whole-system current view: `list_jobs` exposes all active jobs with current state/metadata, with `job_status` providing per-job detail.
- Current-control decision scope: create a new commitment or cancel an existing Pending/InProgress job, thereby changing the current work portfolio.

## S3* — Complementary audit

- State: —
- Function: no material first-party runtime path establishes an independent complementary audit owner whose distinct operational-reality findings close back into corrective S1 behavior.
- Disturbance / variety regulated: not established as S3* at the reviewed runtime boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic authorization/safety gates, logs/audit sinks, self-repair monitoring and repository-development audits exist but do not establish runtime S3* ownership.
- Closure path: not applicable.
- Why this is / is not agent-owned: self-repair observes inactivity mechanically and security controls enforce policy; development audits/reviewer agents operate outside the credited product runtime.
- Evidence: [`docs/capabilities/jobs/self-repair.mdx`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/capabilities/jobs/self-repair.mdx), [`docs/internal/reborn/target-architecture/ws12-security-audit.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/internal/reborn/target-architecture/ws12-security-audit.md).
- Basis: negative after targeted runtime/development-surface review.
- Confidence: medium-high.
- Caveats: audit logging and policy checks may be valuable controls without constituting S3*.

### Absence scope

- Surfaces inspected: runtime self-repair, job failure history, authorization/safety/audit mechanisms, internal security-audit material and contributor review-agent instructions.
- Plausible first-party paths checked: stuck-job monitor/retry, tool-failure feedback, runtime security/audit sinks and repository-level independent review/audit workflows.
- Why no material first-party path remains: runtime paths found are deterministic monitoring/policy enforcement or ordinary failure feedback, while independent review/audit actors found are development-system surfaces outside the operational boundary and do not close findings into running S1 units.

## S4 — Outside-and-then intelligence

- State: P
- Function: recognize recurring/future user needs, formulate a persistent automation adaptation and return the parent-approved option into future IronClaw operation.
- Disturbance / variety regulated: repeated user work, recurring omissions/forgetting, periodic monitoring needs and learned patterns likely to recur.
- Decisive decision or feedback right: approve whether the proposed persistent routine becomes part of future operation.
- Decision owner: the user as legitimate parent in the shipped routine-advisor mode.
- Supporting / enforcement mechanisms: user/context memory, `routine-advisor` activation/pattern rules, `builtin__trigger_list`, `builtin__trigger_create`, cron/once schedules and routine execution history.
- Closure path: observed recurring pattern/future need → agent proposes specific future automation → user confirms or rejects → on confirmation agent creates the routine → later scheduled/event-driven runs alter future operation.
- Boundary reachability: `routine-advisor` is a shipped first-party skill and explicitly instructs the standard agent to use built-in trigger capabilities after confirmation; no downstream adaptation workflow is required.
- Why this is / is not agent-owned: the agent owns pattern detection and option generation, but the skill explicitly says to always wait for user confirmation. The decisive adaptation judgment therefore remains parent-owned.
- Evidence: [`skills/routine-advisor/SKILL.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/skills/routine-advisor/SKILL.md), [`docs/capabilities/routines/cron.mdx`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/capabilities/routines/cron.mdx).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: dynamic tool discovery/building and current-task extension use are not independently credited as S4 without the prospective distinction; the positive claim rests on the explicit recurring-pattern→future-routine path.
- External distinction: recurring user behavior, installed-capability context and expressed/learned needs are evidence outside the current internal execution state.
- Future / prospective distinction: the advisor distinguishes tasks likely to recur and proposes a schedule for later executions rather than merely solving the present turn.
- Adaptation option generated: a concrete persistent routine specifying what future runs do, when they run and how results are delivered.
- Path back into current capability / S3: parent confirmation authorizes `builtin__trigger_create`; the installed routine becomes part of the active operational program and later fires as standard jobs.
- Parent ownership of decisive adaptation judgment/feedback right: the shipped skill says to wait for the user to confirm before creating any routine.
- Return of parent decision into present capability: confirmation permits the agent to install the trigger immediately.
- Subsequent operational/capability change under that returned decision: future cron/event fires execute the newly installed recurring program.

## S5 — Policy and identity

- State: —
- Function: no material runtime path establishes an agent or parent closure over IronClaw's identity or ultimate organizational policy at the declared system boundary.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: user requests, settings, authorization/approval policy, agent name/profile, skills and extension permissions constrain operation but do not by themselves constitute S5 closure.
- Closure path: not applicable.
- Why this is / is not agent-owned: the reviewed surfaces expose operational authority/configuration and action approvals, not a reconstructable identity/ultimate-policy issue resolved by a legitimate S5 owner and returned as governing identity/policy.
- Evidence: [`README.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md), [`docs/extensions/building-a-tool.md`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/docs/extensions/building-a-tool.md), [`.env.example`](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/.env.example).
- Basis: negative after targeted policy/configuration review.
- Confidence: medium-high.
- Caveats: human approval of risky tool actions is operational governance; it is not automatically S5=P.

### Absence scope

- Surfaces inspected: user configuration/settings, authorization and approval gates, skills, extension permissions, agent naming/profile surfaces, job/routine governance and runtime prompts.
- Plausible first-party paths checked: user approvals, configurable safety/security policy, agent settings, extension lifecycle permissions and model-visible instructions.
- Why no material first-party path remains: these surfaces constrain actions and capabilities but no reviewed standard path turns an identity/ultimate-policy question into an authoritative S5 decision and returns that decision as the organization's governing identity/policy.

## Distributed OSS parent arrangement

The public repository's contributor/maintainer governance is outside the assessed running IronClaw instance. Multiple contributors and repository audits therefore do not establish organization-level parent modes for the product runtime.

## Self-hosted and non-human modes

IronClaw can run self-hosted. Generic operator settings and action approvals are not promoted to S3/S5 parent modes without function-specific closure. The one credited parent mode is S4, because the shipped routine-advisor procedure explicitly assigns the decisive future-adaptation confirmation to the user and returns that decision into a persistent operational program.

## Recursion

The assessment is at one IronClaw instance. Background jobs can be distinct S1 units because they execute independent operational loops with isolated contexts. This does not imply that every turn, routine fire or extension is a separate viable-system recursion.

## Variety and escalation

The runtime attenuates execution variety through capability authorization, bounded job concurrency, isolation, checkpoints and deterministic recovery. Operational escalation can reach the main agent through job state and tool results; risky actions can pause for user approval. Only the routine-advisor confirmation path is credited as a parent-owned VSM function here, because it closes a future adaptation decision rather than merely authorizing one current action.

## Evidence gaps

No positive S3* path was established at the operational boundary. Dynamic tool building is real first-party extensibility, but this review did not use it to raise S4 because current need→tool creation alone does not establish the Methodology's prospective outside-and-then distinction. No S5 identity/ultimate-policy closure was established.