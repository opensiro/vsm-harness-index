---
harness_id: deimos
project_name: Deimos
repository: https://github.com/dxiv/dxa-deimos
review_ref: 933a20c064294cb84dafaae2fe0dae617eb44c48
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Deimos

## Review boundary

- System in focus: the shipped `@dxa-deimos/cli` terminal coding-agent runtime, including the first-party opt-in local agent-team mode available from its own source/build, but not developer CI, external AI providers, external cloud-review services, or an independently maintained organization running Deimos.
- Purpose and identity: execute user-directed coding, research, file modifications and tool operations using local/cloud inference, with optional team-level allocation of concurrent coding tasks.
- Relevant environment: user's repository/workspace and Git history, local programs/tests, provider/model APIs, configurable permissions and provider profiles, external MCP tools, humans approving operations, and optional local agent-team members.
- Standard-distribution boundary: the frozen open CLI source, explicit `bun run build` packaging logic, `bin/deimos.mjs` runtime wrapper, packaged `src` tool/query loop and optional first-party team mode. Deimos explicitly gates/degrades internal features in the open build. Experimental Python provider-routing sidecars, maintainer CI/release/policy documents, hosted review services and VS Code editor host are distinguished from deployed native decision owners.
- Credited operating / distribution surfaces: [bin/deimos.mjs](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/bin/deimos.mjs); [package.json](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/package.json); [scripts/build.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/build.ts); [src/entrypoints/cli.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/entrypoints/cli.tsx); [src/main.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/main.tsx); [src/query.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/query.ts); [src/QueryEngine.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/QueryEngine.ts); [src/tools/AgentTool/AgentTool.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/AgentTool.tsx); [src/tools/AgentTool/runAgent.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/runAgent.ts); [src/tools/TeamCreateTool/TeamCreateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TeamCreateTool/TeamCreateTool.ts); [src/tools/TaskCreateTool/TaskCreateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskCreateTool/TaskCreateTool.ts); [src/tools/TaskUpdateTool/TaskUpdateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskUpdateTool/TaskUpdateTool.ts); [src/tools/TaskListTool/TaskListTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskListTool/TaskListTool.ts); [src/tools/SendMessageTool/SendMessageTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/SendMessageTool/SendMessageTool.ts); [src/utils/tasks.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/tasks.ts); [src/hooks/useTaskListWatcher.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/hooks/useTaskListWatcher.ts); [src/utils/swarm/inProcessRunner.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/swarm/inProcessRunner.ts); [src/utils/agentSwarmsEnabled.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/agentSwarmsEnabled.ts).
- Adjacent first-party surfaces excluded from ownership: [.github/workflows/pr-checks.yml](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/.github/workflows/pr-checks.yml), [.github/workflows/codeql.yml](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/.github/workflows/codeql.yml), [scripts/verify-no-phone-home.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/verify-no-phone-home.ts), [scripts/pr-intent-scan.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/pr-intent-scan.ts) and [CONTRIBUTING.md](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/CONTRIBUTING.md) are maintainer/development quality-control and governance rather than the installed coding agent's S3* or S5. [python/smart_router.py](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/python/smart_router.py) is an explicitly optional experimental provider sidecar; model selection, health scoring and retry are current-operation transport, not independently credited adaptive organization. The third-party/hosted `ultrareview` backend is not first-party local reviewer authority.
- First-party operating / deployment modes considered: basic CLI/model/tool loop; local/cloud model backends, tool-permission system, background/synchronous subagent; explicit `DEIMOS_EXPERIMENTAL_AGENT_TEAMS` / `--agent-teams` opt-in (plus configured killswitch), local in-process/team task ownership, messages, shutdown, and company-internal feature-gated verifier excluded from ordinary public build. The VS Code extension is a UI integration, not a separately autonomous organization.
- Recursion level: the local Deimos coding installation, with one default coding S1 or several independent operative teammates under a native team lead in opt-in team mode; the user's entire company and the hosted provider's organization are outside the selected recursion.
- Reviewed revision: 933a20c064294cb84dafaae2fe0dae617eb44c48.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The distributable package [package.json](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/package.json) exposes a `deimos` CLI through [bin/deimos.mjs](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/bin/deimos.mjs), which loads a prebuilt `dist/cli.mjs` when present. The frozen tree includes a Bun build contract at [scripts/build.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/build.ts) and first-party query/tool control surfaces [src/entrypoints/cli.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/entrypoints/cli.tsx), [src/main.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/main.tsx), [src/query.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/query.ts) and [src/QueryEngine.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/QueryEngine.ts). Model providers and local inference are interchangeable backends for a first-party decision-making coder, not independent external agent runtimes that can be borrowed for organizational ownership. Agent calls are implemented by [src/tools/AgentTool/AgentTool.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/AgentTool.tsx) and [src/tools/AgentTool/runAgent.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/runAgent.ts), with actual tool/results feedback to subsequent model decisions.

The first-party team mode is optional, not the default external build experience. [src/utils/agentSwarmsEnabled.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/agentSwarmsEnabled.ts) requires `DEIMOS_EXPERIMENTAL_AGENT_TEAMS` or `--agent-teams`, plus a configured positive `tengu_amber_flint` killswitch. [src/tools/TeamCreateTool/TeamCreateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TeamCreateTool/TeamCreateTool.ts) creates a native team-lead, shared team file and task list; [src/tools/TeamCreateTool/prompt.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TeamCreateTool/prompt.ts) specifies individual operational teammates, assignments and returned messages. [src/tools/AgentTool/AgentTool.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/AgentTool.tsx) supplies named teammate spawning; [src/tools/shared/spawnMultiAgent.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/shared/spawnMultiAgent.ts) provides first-party spawn handling. Team/peer messages are sent through [src/tools/SendMessageTool/SendMessageTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/SendMessageTool/SendMessageTool.ts) and their operational status through [src/utils/swarm/teamHelpers.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/swarm/teamHelpers.ts).

The shared task protocol [src/utils/tasks.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/tasks.ts) performs file-lock-backed atomic claims, returns `already_claimed`, `blocked`, `agent_busy`, and prevents a teammate from claiming unresolved/doubly-owned work. [src/hooks/useTaskListWatcher.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/hooks/useTaskListWatcher.ts) and [src/utils/swarm/inProcessRunner.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/swarm/inProcessRunner.ts) invoke that protocol to choose an eligible next task and return failure or admitted work into the next worker action. [src/tools/TaskUpdateTool/TaskUpdateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskUpdateTool/TaskUpdateTool.ts) updates ownership, blockers and completion and notifies designated agents. This realizes a bounded inter-S1 conflict-attenuation constructor. Separately, the team lead can evaluate the whole current roster/task/blocked view and exercise discretionary choice over current assignments, priorities and interventions.

Feature exclusion is first-party evidence: [scripts/build.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/build.ts) sets explicitly enumerated open-build feature flags and returns `false` for unspecified `feature()` names. `VERIFICATION_AGENT` is not enabled in its feature map; [src/tools/AgentTool/builtInAgents.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/builtInAgents.ts) additionally requires `tengu_hive_evidence` (false default) to load the named verifier. [src/tools/VerifyPlanExecutionTool/VerifyPlanExecutionTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/VerifyPlanExecutionTool/VerifyPlanExecutionTool.ts) is a null stub and [src/tools/ReviewArtifactTool/ReviewArtifactTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/ReviewArtifactTool/ReviewArtifactTool.ts) is an empty stub. Ordinary review/security prompts inside the coder do not by themselves supply a genuinely independent complementary audit; maintainer CI must not be imported. [src/commands/review.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/commands/review.ts) is a prompt-only local review while `/ultrareview` delegates to an external remote service. [python/smart_router.py](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/python/smart_router.py) observes providers' latency/cost/errors for current request routing, rather than making external prospective changes to the agent organization's capabilities.

## Operational model

The default autonomous S1 is a single model-guided coding session. In an explicitly opted-in team, named separately working teammates are distinct S1 units; inter-unit task ownership and dependency collisions are absorbed by a deterministic shared protocol and subsequent task selection. The team-lead model sees whole-current team state and controls current assignment and intervention. Permissions, static security checks, provider selection and CI support or constrain those functions without inheriting their decisive organizational authority.

## S1 — Operations

- State: A
- Function: pursue uncertain coding outcomes through iterative model-selected file, shell, search and other first-party tool actions, including individual teammate tasks.
- Disturbance / variety regulated: incomplete coding instructions, new source state, command/tool outcomes, model/provider errors, changing team work and feedback from other agents.
- Decisive decision or feedback right: choose next tool/operation or completion after observing the previous tool/agent result.
- Decision owner: a configured local/cloud inference model operating in a first-party Deimos query/agent-tool loop; external API only supplies inference and transport.
- Supporting / enforcement mechanisms: SDK adapter and provider profiles, tool dispatcher, terminal session state, permission gates, context handling, subprocess/file tools and model selection.
- Closure path: user or team assignment → model request → selected first-party action/tool → tool output → next model turn/operation or completion returned to user/team lead.
- Boundary reachability: the public CLI launcher loads the built native Deimos entrypoint; the own-source query engine and `AgentTool` produce action/feedback cycles. Team spawning is reachable from the documented first-party optional mode and not from an adjacent hosted agent alone.
- Why this is / is not agent-owned: removing the model while leaving API adapters and tools in place removes the context-sensitive decision about coding actions; static runtime mechanisms cannot replace the operational choice.
- Evidence: [bin/deimos.mjs](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/bin/deimos.mjs); [src/entrypoints/cli.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/entrypoints/cli.tsx); [src/query.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/query.ts); [src/QueryEngine.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/QueryEngine.ts); [src/tools/AgentTool/AgentTool.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/AgentTool.tsx); [src/tools/AgentTool/runAgent.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/runAgent.ts); [README.md](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/README.md).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: this is evidence for native decision-right mapping, not live benchmark accuracy or successful packaging of every optional tool.

## S2 — Coordination

- State: C
- Function: attenuate actual contention and premature succession between distinct active operational teammates through shared task-ownership conflict checks and dependency admission.
- Disturbance / variety regulated: concurrent attempts by two teammates to claim one task, overcommitment of a busy agent, and a successor task begun before its dependencies finish.
- Decisive decision or feedback right: file-lock-serialized, owner/dependency/busy-state checked admission or rejection of a claim; result controls whether a given S1 may start the task.
- Decision owner: native deterministic first-party coordination constructor; teammate models may select subsequent eligible work but no separately evidenced autonomous agent owns the conflict-specific arbitration policy. Hence `C`, not automatic `A`.
- Supporting / enforcement mechanisms: `proper-lockfile`, disk task list, owner/blockedBy graph, watcher, in-process runner, TaskUpdate and mailbox status.
- Closure path: teammate sees an unclaimed task → tries `claimTask` → exclusive lock plus owner/blocked/busy checks → refusal or approved claim returned to watcher/runner → only accepted worker begins its operational prompt; blocked or contending agents wait or inspect newly available work.
- Distinct S1 units: two named first-party team workers handling separate repository modifications under a single team.
- Inter-S1 disturbance: simultaneous ownership claims and incompatible active dependencies.
- Attenuating coordination relation: first-party atomic locking and task dependency checks, not merely a shared mailbox or generic queue.
- Feedback into subsequent S1 behaviour: task-list watcher/in-process runner uses returned success/failure to select or defer its next prompt; failure to submit releases the claim.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the implemented relation directly identifies and rejects a concrete conflict between independent operating agents before work proceeds, and delivers that arbitration into the operational selection loop.
- Boundary reachability: native `DEIMOS_EXPERIMENTAL_AGENT_TEAMS`/flag opt-in enables TeamCreate and teammate spawn; the shipped `useTaskListWatcher` and `inProcessRunner` actually call the same `src/utils/tasks.ts` `claimTask` method. No external runtime is needed for the collision rule.
- Why this is / is not agent-owned: deterministic lock arbitration remains even if agentic reasoning is removed; it establishes constructed S2 conflict regulation, not model-owned S2 policy.
- Evidence: [src/utils/tasks.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/tasks.ts); [src/hooks/useTaskListWatcher.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/hooks/useTaskListWatcher.ts); [src/utils/swarm/inProcessRunner.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/swarm/inProcessRunner.ts); [src/tools/TaskListTool/TaskListTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskListTool/TaskListTool.ts); [src/utils/agentSwarmsEnabled.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/agentSwarmsEnabled.ts); [src/tools/TaskUpdateTool/TaskUpdateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskUpdateTool/TaskUpdateTool.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: direct manual `TaskUpdate` ownership editing is distinct from the protected `claimTask` code; the positive relation is the runtime automatic-claim path, not a universal no-conflicts guarantee.

## S3 — Inside-and-now control

- State: A
- Function: maintain cohesion over an opted-in current team by assigning, revising and supervising several ongoing operational obligations and available teammates.
- Disturbance / variety regulated: blocked dependent work, idle or overburdened teammates, unexpected subtask failures, stale commitments and competing priorities in the active team.
- Decisive decision or feedback right: the model-directed team lead may choose team formation, current owner/priority allocation, updated dependencies, interventions to unblock work, instructions to teammates and shutdown/reallocation of the current team.
- Decision owner: first-party team-lead model at the local team recursion in supported opt-in mode; task persistence and mailbox delivery merely enforce/communicate its decisions.
- Supporting / enforcement mechanisms: TeamCreate/team file/roster, TaskList/TaskUpdate, SendMessage, worker status and shared task metadata.
- Whole-system current view: the team-lead can inspect the complete team task list with owner/status/blocker information and receive teammate completion/blocked or idle messages, rather than merely the contents of one operative tool call.
- Current-control decision scope: priority/ownership among several currently operative teammates, resource allocation and intervention through task ownership and communication.
- Closure path: teammate blocks/completes or signals difficulty → lead reads whole-team state/messages → model chooses reassignment/dependency adjustment/worker instruction → TaskUpdate/SendMessage records/delivers decision → subsequent teammate activity changes.
- Boundary reachability: [src/tools/TeamCreateTool/TeamCreateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TeamCreateTool/TeamCreateTool.ts) initializes native team lead and shared task list in the enabled first-party mode; [src/tools/TaskListTool/TaskListTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskListTool/TaskListTool.ts) and [src/tools/TaskUpdateTool/TaskUpdateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskUpdateTool/TaskUpdateTool.ts) expose ongoing obligations and discretionary owner/dependency changes; [src/tools/SendMessageTool/SendMessageTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/SendMessageTool/SendMessageTool.ts) returns consequential directions to native teammates.
- Why this is / is not agent-owned: the deterministic task store cannot decide what current team obligations should be changed in response to evolving progress; the model controls this whole-current choice rather than only forwarding messages.
- Evidence: [src/tools/TeamCreateTool/TeamCreateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TeamCreateTool/TeamCreateTool.ts); [src/tools/TeamCreateTool/prompt.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TeamCreateTool/prompt.ts); [src/tools/AgentTool/AgentTool.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/AgentTool.tsx); [src/tools/TaskListTool/TaskListTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskListTool/TaskListTool.ts); [src/tools/TaskUpdateTool/TaskUpdateTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/TaskUpdateTool/TaskUpdateTool.ts); [src/tools/SendMessageTool/SendMessageTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/SendMessageTool/SendMessageTool.ts); [src/utils/swarm/teamHelpers.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/swarm/teamHelpers.ts); [src/utils/agentSwarmsEnabled.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/agentSwarmsEnabled.ts).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: only the explicitly opt-in team mode supplies whole-current control; default single coder and user approvals are not re-labelled as S3.

## S3* — Complementary audit

- State: —
- Function: no enabled independent complementary operational-evidence review with a consequential findings-return loop is established in the open Deimos distribution.
- Disturbance / variety regulated: source changes and task-completion claims may be wrong, but routine local reviews/tests and maintainer CI do not establish this additional organizational audit.
- Decisive decision or feedback right: an independent auditor would inspect distinct primary artifacts, judge contradictory evidence and inform current control; the frozen *open build* instead disables the named specialized verifier and has no completed native alternative audit path.
- Decision owner: no positive native S3* owner established. Internal verifier code exists as an adjacent disabled feature; the main coding agent controls ordinary local review.
- Supporting / enforcement mechanisms: local `/review` prompt and `/security-review`, test/code tools, optional external `/ultrareview`, and maintainer CodeQL/CI—all outside a first-party independent complementary audit close.
- Closure path: ordinary coder may read source or tests and continue S1; no alternative first-party auditor with separate judgment and a returned metasystemic control correction is operationally established.
- Why this is / is not agent-owned: `verificationAgent` presence is not sufficient when build-time `feature('VERIFICATION_AGENT')` is false and runtime GrowthBook gate defaults false, and a local model requested to review its own work is not an independent complementary audit by name.
- Evidence: [scripts/build.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/build.ts); [src/tools/AgentTool/builtInAgents.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/builtInAgents.ts); [src/tools/AgentTool/built-in/verificationAgent.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/built-in/verificationAgent.ts); [src/tools/VerifyPlanExecutionTool/VerifyPlanExecutionTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/VerifyPlanExecutionTool/VerifyPlanExecutionTool.ts); [src/tools/ReviewArtifactTool/ReviewArtifactTool.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/ReviewArtifactTool/ReviewArtifactTool.ts); [src/commands/review.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/commands/review.ts); [src/commands/security-review.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/commands/security-review.ts); [.github/workflows/codeql.yml](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/.github/workflows/codeql.yml).
- Basis: structural + explicit.
- Confidence: medium-high for the frozen open-build boundary.
- Caveats: this does not assert that developer CI, an internal build, or a separately hosted external service lacks review/audit. Their decision rights are not credited to this assessed publicly shipped CLI.

### Absence scope

- Surfaces inspected: open-build feature flags and stubs, built-in verifier registry, local code/security review prompts, remote hosted reviewer gate, SDK/tool verification affordances and maintainer CI/test workflows.
- Plausible first-party paths checked: a native independent reviewer with different artifact access; isolated replay or adversarial raw-evidence judgment; actionable audit findings returned into current-team S3 supervision, available in the publicly shipped mode.
- Why no material first-party path remains: verification agent is explicitly omitted by open-build flag default, alternative ReviewArtifact/VerifyPlanExecution modules are stubs, and local prompts/hosted services/CI lack a first-party independent audit judgment and closed S3*→current-control loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed externally prospective adaptation mechanism that generates future capability options and returns them into current S3 oversight was established.
- Disturbance / variety regulated: latency/cost changes among inference providers, new task and repository context and externally hosted service capabilities are addressed by operational routing/configuration rather than a prospective organizational intelligence cycle.
- Decisive decision or feedback right: configured Python provider sidecar may select a current backend by observed health/latency; user/provider profiles govern model selection. This is not a future-directed adaptation judgment over the team's capabilities.
- Decision owner: no evidenced first-party S4 at the local installed coding/agent-team recursion.
- Supporting / enforcement mechanisms: [python/smart_router.py](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/python/smart_router.py) experimental sidecar, provider bootstrap/discovery, model choice and task planning; `PROACTIVE=false` and `AGENT_TRIGGERS=false` in [scripts/build.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/build.ts).
- Closure path: current model/backend switch informs the next inference request, not a future-state/options decision returned into S3 control to transform longer-run capability.
- Why this is / is not agent-owned: provider health scoring and context-dependent code plan are operational, not environmental foresight; future-looking labels on disabled features cannot supply an implemented S4 loop.
- Evidence: [python/smart_router.py](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/python/smart_router.py); [scripts/provider-recommend.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/provider-recommend.ts); [scripts/build.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/build.ts); [src/commands/ultraplan.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/commands/ultraplan.tsx); [README.md](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a separately managed user organization may assess future models and alter its installation, but that external governance is not native S4 ownership.

### Absence scope

- Surfaces inspected: open build feature gates, optional routing sidecar, provider profiles, planning/remote task workflows, project roadmap and user instructions.
- Plausible first-party paths checked: external and prospective sensing; creation/evaluation of adaptation options; return to whole-current S3 for resource/capability adjustment; operational follow-through on the strategic choice.
- Why no material first-party path remains: no source-supported native adaptation loop closes these stages; available mechanisms adapt the current request's routing or implement user-provided tasks, not future organizational capability.

## S5 — Policy and identity

- State: —
- Function: no first-party highest-level identity/ultimate policy decision path is established for this assessed local agent organization.
- Disturbance / variety regulated: credentials, model/provider choice, tool permissions, usage limits and opt-in team access are operational constraints rather than conflicts about organizational identity or ultimate policy.
- Decisive decision or feedback right: users/developers choose settings and approve particular tools, while the runtime enforces fixed rules; no identity/policy choice closing S3–S4 tension is observed.
- Decision owner: no native ultimate-policy owner; external human or maintainer may govern their broader project independently.
- Supporting / enforcement mechanisms: config/profile editor, local permission gates, policy-limit helpers, source build flags and team mode enablement.
- Closure path: a local tool action is approved/rejected or a mode toggled and coding continues; no higher-order identity issue → legitimate policy authority → binding returned system-operation constraint is wired as a first-party S5 loop.
- Why this is / is not agent-owned: static source-build policy and local operator approvals are not an autonomous S5 decision or a legitimate parent-mode ultimate-policy return.
- Evidence: [src/services/policyLimits/index.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/services/policyLimits/index.ts); [src/utils/agentSwarmsEnabled.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/utils/agentSwarmsEnabled.ts); [scripts/build.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/build.ts); [src/tools/AgentTool/AgentTool.tsx](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/src/tools/AgentTool/AgentTool.tsx); [README.md](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/README.md); [LEGAL.md](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/LEGAL.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: organizational/legal governance recorded in public docs is adjacent, not automatically an operating parent mode of the Deimos CLI.

### Absence scope

- Surfaces inspected: permissions and feature flags, local team/agent management, global provider selection, policy limits, contributor/legal documentation and operator tools.
- Plausible first-party paths checked: detection of an identity/mission conflict, legitimate ultimate authority's discretionary decision, and binding return governing later S3/S4 choices.
- Why no material first-party path remains: investigated first-party pathways concern current task consent, developer feature support or hosted/external governance, and do not implement a returned ultimate identity-policy decision.

## Recursion

Single-coder Deimos owns local S1 task execution. In explicitly opted-in agent-team mode, multiple separately operating teammates become S1 units; first-party locked task claims construct an S2 relation and the team-lead model owns whole-current S3 choices over the active team. The user/developer team, external model providers, maintainer CI and remote cloud services are separate organizational layers with no automatically inherited parent-mode grading. A nested agent/tool invocation is not presumed a recursively viable organization by name.

## Variety and escalation

Current source/task complexity is absorbed by model/tool action feedback. Fixed permission/build gates attenuate permitted operation but do not become independent organizational choice. In team mode, task-claim collisions/blocked dependencies are attenuated by atomic locks; teammate status and task list let the lead respond to current team-level resource and commitment disturbances. Ordinary approvals return to the coding tool; neither hosted review nor maintainer CI automatically supplies S3* audit. No native prospective S4 or identity S5 closure was found in the frozen open build.

## Evidence gaps

This is a frozen-source assessment of the documented open-build contract. The local review environment could fetch the immutable source commit and inspect paths but does not have Bun/Node needed to build or run the CLI, so no live end-to-end mode demonstration is claimed. [scripts/build.ts](https://github.com/dxiv/dxa-deimos/blob/933a20c064294cb84dafaae2fe0dae617eb44c48/scripts/build.ts) may provide missing-module stubs and explicitly disables internal features in the open build; positive S2/S3 claims are restricted to the separately documented opt-in local team path with actual first-party task arbitration and lead control, not to unavailable private daemon/bridge/verification modes. Bounded negative states describe the inspected open distribution rather than universal impossibility for hypothetical extensions or external services.
