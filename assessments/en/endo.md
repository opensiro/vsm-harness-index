---
harness_id: endo
project_name: Endo
repository: https://github.com/longsurf-ai/endo
review_ref: bd7ec037f63d52766af5c80c82b8e185dd8b5380
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Endo

## Review boundary

- System in focus: the shipped Endo desktop/backend's persistent agent sessions and first-party Prompt/Processor/LLM execution, plus its packaged editable workflow/schedule route; not a union of the external native coding agents whose CLIs it can operate.
- Purpose and identity: provide one persistent conversation and reusable workflows that can direct models and native tools, invoke multiple agent sessions, and return their work to the user.
- Relevant environment: user questions, local workspaces/resources, concurrent runs and child sessions, provider availability, model output, schedule triggers, permission prompts, interrupted processing and persistent history.
- Standard-distribution boundary: installed Endo desktop or source-run backend with `server/agent` Run/Session/Prompt/Processor/LLM, profile and tool registry, SQLite transcripts, workflow authoring/runtime, adapters and scheduled Run admission.
- Credited operating / distribution surfaces: first-party Prompt outer loop and tool binding for regular model SDK paths; durable Run/Session execution; registered resource/task/workflow/transcript/schedule tools; packaged workflow templates and model-selected calls to them; invocation-specific child session control.
- Adjacent first-party surfaces excluded from ownership: development/demo agent, repository CI, workflow/test fixtures, optional live model tests, external Codex/Claude Code/Grok/Antigravity/OpenCode native agent internals, third-party model APIs, unrelated OpenChart project and user-authored workflow extensions not shipped by default.
- First-party operating / deployment modes considered: desktop application and server; regular SDK single-step provider model calls under Endo's `Prompt.loop`; provider-owned native CLI loops through adapters; one-session chat, packaged `/best-of-n` and other named workflows, scheduled prompts, prompt/permission approval and user-editable workflow files.
- Recursion level: one Endo installation with persistent sessions and, for a workflow invocation, a root Run with child operational sessions. Child Session IDs do not automatically prove independent VSM recursion.
- Reviewed revision: `bd7ec037f63d52766af5c80c82b8e185dd8b5380`.
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The backend stores a Run before execution. A per-session runner claims it, and `Prompt.executeInvocation` resolves a profile, model, history, tool registry and workspace, then iterates `Prompt.loop`: committed transcript state determines whether to finish, take a deterministic action or call `processStep`. `Processor` consumes each model/SDK event, persists messages and tool outcomes, and returns control to `Prompt` for another step. For native provider-owned CLI modes, Codex/Claude Code etc. also have their own internal model/tool loops; those internals are not Endo's autonomy evidence. Endo's `WorkflowTool` can execute an installed TypeScript workflow using `agent()` child sessions and bounded `parallel()`, with a root Run and cancellation. Templates include independent parallel research and synthesis; user-defined programs may change the topology but are not credited merely by being possible. `Permission.Service` enforces profile rules and human approval, while schedules enqueue ordinary Runs. [agent architecture](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/agent.md), [Prompt loop](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/prompt/execute.ts), [tool registry](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/tool/registry.ts), [workflow architecture](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/workflow.md).

## Operational model

An Endo session can take a model-selected tool action, observe its persisted result and let its first-party Prompt loop select the next step. A workflow may start several distinct model-backed child sessions through Endo's own invocation machinery, but the shipped templates largely specify their sequence/parallelism as trusted author-written programs. The parent model may select or parameterize a tool, while fixed runtime constraints handle concurrency, session ownership and permission. These are substantial operational capabilities; they are not automatically independent cross-S1 coordination, whole-system control, complementary audit, prospective adaptation or ultimate policy.

## S1 — Operations

- State: A
- Function: produce answers and execute authorized model-selected local tool/workflow operations in response to user or scheduled prompts.
- Disturbance / variety regulated: changing questions and workspace resources, tool observations, provider errors, user clarifications, prior transcript state, stopped runs and resumed conversations.
- Decisive decision or feedback right: in the regular model route, the model selects available tools and arguments; the first-party Prompt outer loop observes committed responses and requests further steps until the conversation is complete.
- Decision owner: model reached by Endo's regular SDK path through the first-party Prompt/Processor/LLM service; external native CLI agent internal decisions remain separately owned by the provider product.
- Supporting / enforcement mechanisms: typed tool registry, `Run` queue, session locks, SQLite transcript and event publisher, permission service, model adapters, persisted tool-result parts, interruption and compaction.
- Closure path: persisted user/scheduled Run → claimed `Prompt.execute` → model response or tool call → first-party tool executes and commits outcome → refreshed transcript/another `Prompt.loop` step → final answer and completed Run.
- Boundary reachability: shipped backend and desktop wire `Prompt.loop`, `processStep`, tool binding and Session runner. The regular SDK path loops at Endo's layer even where a native CLI provider owns its own internal implementation.
- Why this is / is not agent-owned: the model chooses the next action against observed context; deterministic queue, schema, admission and permission checks do not substitute their choices for the model's task discretion.
- Evidence: [Prompt execution](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/prompt/execute.ts), [step and tool binding](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/prompt/step.ts), [tool catalog](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/tool/registry.ts), [runtime call distinction](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/agent.md).
- Basis: structural and explicit.
- Confidence: medium-high.
- Caveats: no paid-provider live run here; regular SDK path and native CLI provider paths must not be conflated, and not every registered business tool is wired in every deployment.

## S2 — Coordination

- State: —
- Function: no first-party relation is established that specifically attenuates an evidenced conflict or oscillation between distinct S1 units.
- Disturbance / variety regulated: child session calls could overlap; the runtime serializes concurrent calls to one Session and caps parallel children, but the examined code does not identify a particular inter-agent workspace/resource conflict and feedback correction.
- Decisive decision or feedback right: workflow author chooses concurrency and sequence by program; runtime semaphores enforce per-session isolation; summarizer model collects research answers.
- Decision owner: trusted workflow program and deterministic runtime, not a demonstrated agent-owned or S2-specific constructor coordination decision.
- Supporting / enforcement mechanisms: `parallel()` ordered result collection, concurrency limit, per-session semaphores and child-ID ownership checks.
- Closure path: an attempted concurrent call to the same child Session waits for the permit and resumes without interleaving; independent child outcomes flow to a summary. No conflict feedback revises subsequent interactions among *distinct* operational units.
- Why this is / is not agent-owned: serial access to one Session protects its own integrity; bounded generic fan-out and synthesis do not establish a function-specific inter-S1 disturbance/attenuation witness.
- Evidence: [workflow `parallel`](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/workflow/authoring/parallel.ts), [workflow session ownership and locking](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/workflow.md), [shipped best-of-n](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/workflow/templates/best-of-n.workflow.ts).
- Basis: bounded negative.
- Confidence: medium; the workflow surface is extensible.
- Caveats: authored custom coordination programs may establish S2 in an individual installation but are not supplied as a first-party supported default witness here.

### Absence scope

- Surfaces inspected: session execution, workflow host, `parallel()`, packaged research/debate templates, child ownership constraints and first-party resource tools.
- Plausible first-party paths checked: same-session concurrent invocations, multiple researcher sessions, shared workspace/resource contention, fan-out limits and synthesis feedback.
- Why no material first-party path remains: examined shipped mechanisms manage execution integrity and authored task composition; none ties a concrete *distinct-S1* interference to an attenuating coordination decision and subsequent S1 feedback.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current-control decision across the installation's live operational cells is demonstrated.
- Disturbance / variety regulated: queued/failed Runs, concurrency pressure, permission requests and workflow child failures affect current execution.
- Decisive decision or feedback right: model can choose local task tools; fixed Run queue claims/finishes tasks, while user selects profiles and approves specific actions; there is no established whole-current view plus discretionary portfolio intervention.
- Decision owner: individual session model for its own task, workflow author for composition and runtime/user for fixed limits and consent.
- Supporting / enforcement mechanisms: Run store, session execution coordinator, child semaphores, workflow concurrency budget, agent status and permission notices.
- Closure path: an individual Run finishes, fails or is interrupted and the transcript is updated; no whole-system current-status evidence returns a changed allocation/commitment decision to several S1 units.
- Why this is / is not agent-owned: a model's choice to invoke a predefined workflow, or a summarizer choosing the best research answer, remains task execution; a queue or name `Coordinator` does not itself own S3.
- Evidence: [agent Run architecture](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/agent.md), [workflow templates](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/workflow/templates/best-of-n.workflow.ts), [workflow runtime](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/workflow.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: a particular authored organizational workflow could add current-control scope but is not the first-party packaged mode assessed.

### Absence scope

- Surfaces inspected: Run queue/claim terminal states, root/child workflow execution, session status, schedule tools, permissions and packaged workflow templates.
- Plausible first-party paths checked: cross-session active Run overview, root workflow summary, child failure intervention, human approvals and concurrency budgets.
- Why no material first-party path remains: no shipped authority receives a whole-current operational view and returns a discretionary resource/priority/commitment change on behalf of a bounded multi-unit whole.

## S3* — Complementary audit

- State: —
- Function: no independent operational auditor with complementary access to S1 reality and a corrective return to current control is established.
- Disturbance / variety regulated: inaccurate model answers and invalid structured outputs can be detected by summarization, schema decoding or ordinary user and developer validation.
- Decisive decision or feedback right: workflow author can insert another agent call or typed reviewer; schema and permission systems reject invalid events; no separately empowered audit actor is shown.
- Decision owner: task workflow or its model and deterministic validators, with human user oversight of normal actions.
- Supporting / enforcement mechanisms: `best-of-n` synthesizer, `thesis-killer` templates, structured output decoder, raw transcript reads, tests and traces.
- Closure path: a workflow's reviewer/model may revise or synthesize its task answer, but there is no independent direct-evidence audit channel that challenges ordinary reporting and returns findings to S3 regulation.
- Why this is / is not agent-owned: separate subagent calls alone do not prove organizational audit independence; review based on peers' model summaries remains in the task's reporting path.
- Evidence: [best-of-n template](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/workflow/templates/best-of-n.workflow.ts), [structured output and transcript tool description](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/workflow.md), [tool registry](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/tool/registry.ts).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: users can author a true audit workflow, but its independent access and authority would need separate evidence in that assembled system.

### Absence scope

- Surfaces inspected: packaged best-of-n/debate/hypothesis workflows, typed-output validation, transcript tools, tracing, approval and test mechanisms.
- Plausible first-party paths checked: model answer comparisons, source transcript replay, child reviewer calls, schema failures, development integration tests and user approvals.
- Why no material first-party path remains: task-level review and validation lack a shown independent direct-evidence access/mandate plus corrective return into whole-current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective external-environment intelligence loop that changes the installation's future operating capability is shown.
- Disturbance / variety regulated: new questions, schedules, available provider accounts and workspace changes are served as current tasks or user settings.
- Decisive decision or feedback right: user authors workflows, schedules and profiles; task model may research an arbitrary subject, but no dedicated adaptation-option authority is evidenced.
- Decision owner: user/developer for installed capability and task agent for on-demand work; no S4 prospective operator.
- Supporting / enforcement mechanisms: scheduling resource, workflow definitions, model references and provider adapters, memory/history.
- Closure path: schedule fires a prompt or user saves a workflow, producing more tasks; no environmental future signal → option comparison → changed current organizational capacity decision return.
- Why this is / is not agent-owned: scheduling a future run or researching a hypothesis inside the user's task does not establish future-facing adaptation of Endo's organization.
- Evidence: [schedule tool](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/tool/tools/create-schedule.ts), [workflow architecture](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/workflow.md), [README](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/README.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: specialized S4 can be composed by operators, but generic workflow expressiveness is not itself an S4 constructor.

### Absence scope

- Surfaces inspected: model registry, schedule resources, shipped workflows, workflow editor, provider adapters and prompt loop.
- Plausible first-party paths checked: scheduled external research, hypothesis-race tasks, provider switching, workflow edits and session memory.
- Why no material first-party path remains: these are present-task or user-configured mechanisms, not a continuous externally and prospectively oriented adaptation path returned to current capability.

## S5 — Policy and identity

- State: —
- Function: no shown identity/ultimate-policy decision channel and authoritative return into operating rules.
- Disturbance / variety regulated: tool risk, profile restrictions, required approvals and choice of provider influence ordinary use of one assistant.
- Decisive decision or feedback right: user can approve once/always/reject and developer supplies profile rules; no identity-level conflict is routed to an identifiable ultimate-policy decision holder through the product.
- Decision owner: user for task authorization and developer for static configuration, not an evidenced system-identity authority.
- Supporting / enforcement mechanisms: profile rule matching, pending `Permission.Service` approvals, persisted grants, tool initialization and default model/agent selection.
- Closure path: configured permission or live user reply allows/blocks the pending tool; it is not an ultimate identity/policy issue returning a governing mandate.
- Why this is / is not agent-owned: a rule library and human permission UI are constraints, not the substantive S5 decision under the Profile.
- Evidence: [permission architecture](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/docs/architecture/permission.md), [agent/profile assembly](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/server/agent/prompt/execute.ts), [README](https://github.com/longsurf-ai/endo/blob/bd7ec037f63d52766af5c80c82b8e185dd8b5380/README.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: any organization deploying Endo can create governance outside the application's assessed boundary.

### Absence scope

- Surfaces inspected: profiles, permission lifecycle and saved grants, tool schema enforcement, approval UI, scheduler, workflow definitions and agent/session identity.
- Plausible first-party paths checked: ruleset edits, profile selection, permission escalation and approval, new workflow admission and parent/child session control.
- Why no material first-party path remains: no source-backed identity-level matter is decided by a legitimate S5 holder and returned as a policy governing subsequent organizational operation.

## Distributed OSS parent arrangement

Source contributors, release maintainers and deployment users have external governance rights over the software. They do not become a runtime parent S3–S5 mode merely because Endo is MIT-licensed and distributable. No function-specific project-parent return into current deployed operations was traced.

## Self-hosted and non-human modes

Endo runs as a locally hosted desktop/backend with user-set model accounts, permissions, schedules and workflow files. These expose substantial task supervision, not by themselves a first-party parent governance arrangement under S3/S4/S5.

## Recursion

The root Run and model-backed child Sessions are operational subdivisions of a workflow. Persisted child identities, isolated transcripts and turn autonomy are real, but the packaged system does not establish those children as independently viable organizations with their own complete metasystems; nested SDK calls are not sufficient evidence of VSM recursion.

## Variety and escalation

Durable transcript and Run admission, per-session lock, queued/concurrent execution, permission replies and interruption cleanup regulate immediate operational variety. A failed child, rejected tool or expired run returns a failure/result at the bounded task; it is not automatically an S3/S4/S5 decision or algedonic channel.

## Evidence gaps

No opt-in paid-provider run, production Mac installation or custom workflow end-to-end was executed in this assessment. Source and architecture docs support the shipped first-party loop and code paths. The exact generality of provider-native tool execution varies across adapters, and user-authored workflows can instantiate organizational relationships beyond the first-party packaged template boundary; those potential deployments are not silently credited.
