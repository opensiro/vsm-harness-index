---
harness_id: jazz
project_name: Jazz
repository: https://github.com/lvndry/jazz
review_ref: 957ad8ef522f9137f690c8acc319553f56e5bdb9
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Jazz

## Review boundary

- System in focus: one first-party Jazz agent-harness deployment at pinned revision `957ad8ef522f9137f690c8acc319553f56e5bdb9`, including the ordinary model/tool agent loop, recursive sub-agent and companion execution, workflow/scheduler, background job queue, memory/context machinery, peer tool, permissions/approvals and supported terminal/headless/chat/daemon surfaces.
- Purpose and identity: execute user-defined agent work through one persistent harness identity across interactive, headless, scheduled and chat surfaces, with model-selected tool actions, optional bounded recursive delegation and durable memory/workflow support.
- Relevant environment: user/operator requests, filesystem/process/git state, configured model providers, MCP/tools, web/search services, chat surfaces, peer Jazz agents and scheduled triggers.
- Standard-distribution boundary: first-party packages and documented runtime paths used by ordinary Jazz operation. Repository-development evals/benchmarks/CI and arbitrary downstream compositions are adjacent unless frozen production code directly wires them into runtime operation.
- Credited operating / distribution surfaces: ordinary `AgentRunner` execution, repeated model/tool feedback, `spawn_subagent`, capability-bound companion dispatch, workflow schedules, daemon unattended resume, background shell-job batches, approvals, peer queries and memory/context compaction/extraction.
- Adjacent first-party surfaces excluded from ownership: repository eval tasks and GitHub development verification as organizational audit of Jazz itself; arbitrary prompting of a sub-agent as reviewer/manager; external peer organizations; generic plugin/MCP extension points without function-specific VSM closure.
- First-party operating / deployment modes considered: interactive and headless agent runs, scheduled/unattended workflow runs, recursive sub-agent execution, media companion dispatch, daemon background-job fan-out/fan-in and configured peer queries.
- Recursion level: one Jazz harness deployment centered on one configured primary agent. A primary or recursive child model/tool run is an S1 operational loop. Ephemeral sub-agents may create temporary S1 plurality, but plurality/delegation alone is not mapped upward into S2 or S3.
- Reviewed revision: `957ad8ef522f9137f690c8acc319553f56e5bdb9`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Jazz's core runtime is a genuine model/tool operational loop. The active model receives conversation and tool state, chooses a response or tool calls, first-party tool execution returns results, those results are appended to the same run state, and the loop samples again until completion or a configured bound. The harness persists conversation/memory state and can run the same agent through terminal, headless, scheduled and chat surfaces. This establishes S1 autonomy.

Jazz also supplies recursive execution. `spawn_subagent` creates an ephemeral child `Agent` with a fresh conversation, bounded depth/iterations and an inherited effective tool/approval surface, then invokes `AgentRunner.runRecursive`; only the child's result returns to the parent. Capability-bound media companions use the same recursive runner. These children are real operational loops rather than plain model calls, but the standard constructor is task delegation: it does not provide a persistent whole-tree current view or a function-specific inter-S1 coordination regulator.

Parallel tool execution is bounded by `MAX_CONCURRENT_TOOLS`, so multiple `spawn_subagent` calls can occupy the generic tool-execution pool. That limit protects runtime resources, but no reviewed path exposes a concrete child-to-child disturbance and S2-specific attenuation/feedback relation that changes subsequent child behavior. Waiting for a generic tool slot is not by itself an organizational coordination loop. Likewise, the background job queue has concurrency caps, leases, retries and fan-in, but its jobs are shell commands rather than autonomous S1 agents; completion simply resumes the originating Jazz agent.

The primary model can decide to delegate work and can use returned child results, but the reviewed `spawn_subagent` path does not expose live enumeration/status/steering/interrupt rights over the temporary child organization. The parent waits for final tool results rather than operating a whole-system current-control surface, so generic delegation is not promoted to S3. Scheduled workflows, wake triggers, approval parking and daemon recovery are execution/control infrastructure around S1 rather than a separate current-regulation actor.

No qualifying S3*, S4 or S5 closure was found. Repository evals, PR-review workflows, run history and telemetry can verify or observe work but are not a materially independent complementary audit loop over the assessed runtime. Web/peer research and memory extraction can add information or retain experience but do not close an external-and-prospective organizational adaptation conversation. Persona, system prompts, permissions, approval policy and user-authored rules configure identity/constraints but do not establish identity/ultimate-policy decision closure.

Primary evidence:

- [`packages/core/src/agent/execution/agent-loop.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/execution/agent-loop.ts) — repeated model completion, tool-call execution, result reinsertion, loop recovery and bounded completion.
- [`packages/core/src/agent/agent-runner.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/agent-runner.ts) — standard and recursive agent-run construction.
- [`packages/core/src/agent/tools/subagent-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/subagent-tools.ts) — bounded recursive child agents, fresh conversations, inherited tool/approval limits and result return to the parent.
- [`packages/core/src/agent/execution/tool-executor.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/execution/tool-executor.ts) — generic parallel tool execution/concurrency guard inspected for S2.
- [`packages/adapters/src/job-queue-service.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/adapters/src/job-queue-service.ts) and [`packages/adapters/src/daemon/job-worker.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/adapters/src/daemon/job-worker.ts) — background shell-job batching, concurrency, leasing/retries and fan-in resume inspected for S2/S3.
- [`packages/core/src/workflows/scheduler-service.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/workflows/scheduler-service.ts) — scheduled workflow trigger binding to the ordinary Jazz agent execution path.
- [`packages/core/src/agent/tools/peer-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/peer-tools.ts) — bounded, attributed questions to somebody else's agent; inspected but treated as environment/peer communication rather than an internal S2/S4 regulator.
- [`README.md`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/README.md) — supported harness boundary, surfaces, scheduling and primary/companion model composition, used only where corroborated by source.

## Operational model

A Jazz agent run is the primary operational cell. The model chooses substantive next actions; tools change or inspect the environment; results return to the transcript and affect later choices. The same operational cell can be started interactively, headlessly, on a schedule or from a chat surface. Recursive children can perform bounded delegated tasks and return results, while generic concurrency, approval and daemon mechanisms constrain execution. No qualifying metasystemic closure above S1 is established at the chosen deployment boundary.

## S1 — Operations

- State: A
- Function: transform a user/workflow objective into tool-mediated environmental outcomes through repeated model reasoning, tool selection, execution and result feedback.
- Disturbance / variety regulated: changing task requirements, tool/environment state, provider responses, command/file/web results, approval outcomes, context pressure, failures and user/queued input.
- Decisive decision or feedback right: choose the next substantive response/tool action and revise subsequent behavior from returned tool/environment evidence.
- Decision owner: the active Jazz model agent in the primary or recursive child run.
- Supporting / enforcement mechanisms: `AgentRunner`, agent loop, tool executor/registry, conversation/context manager, approvals, retry/budget guards, memory, persistence and presentation surfaces.
- Closure path: objective/context → model completion chooses tool/action → tool runtime executes/observes environment → tool result is appended to the run → next model completion observes changed evidence and chooses subsequent action → task/environment state changes.
- Boundary reachability: standard first-party path used by terminal, headless, workflow/chat and recursive sub-agent execution.
- Why this is / is not agent-owned: deterministic runtime machinery bounds and executes choices, but removing the model removes the substantive next-action judgment while leaving only transport/enforcement mechanisms.
- Evidence: [`agent-loop.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/execution/agent-loop.ts); [`agent-runner.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/agent-runner.ts); [`subagent-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/subagent-tools.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: recursive sub-agents are bounded/ephemeral, but each executes the same complete reason/tool/feedback loop and therefore qualifies as an operational loop when spawned.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination relation is established at the assessed deployment recursion.
- Disturbance / variety regulated: no complete qualifying inter-S1 interference/oscillation witness is established among Jazz operational agents.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S2 at this boundary.
- Supporting / enforcement mechanisms: generic tool concurrency cap, recursive child depth/iteration bounds, background shell-job queue, workflow scheduler, peer messaging and approval serialization constrain execution but do not by themselves establish S2.
- Closure path: not applicable; no reviewed standard path reconstructs distinct S1 agents → concrete inter-S1 disturbance → S2-specific attenuation → feedback changing subsequent S1 behavior.
- Distinct S1 units: a parent can spawn one or more recursive child agents with their own fresh conversations and complete model/tool loops.
- Inter-S1 disturbance: not established as a concrete organizational interaction. Generic contention for `MAX_CONCURRENT_TOOLS` is tool-runtime capacity and no child-specific disturbance is surfaced into child behavior; shell jobs are not autonomous S1s.
- Attenuating coordination relation: generic tool scheduling, recursion depth bounds and job-worker concurrency prevent resource exhaustion but are not shown regulating a concrete child-to-child operational disturbance.
- Feedback into subsequent S1 behaviour: child final results return to the parent, but no coordination verdict about an inter-S1 disturbance is returned to affected child S1s or otherwise closes an S2 relation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is deliberately not mapped as S2. `spawn_subagent`, `ask_peer`, schedules and job fan-out are delegation/communication/execution primitives without the required inter-S1 disturbance-and-feedback witness.
- Why this is / is not agent-owned: no material S2 function is established, so ownership classification does not proceed.
- Evidence: [`subagent-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/subagent-tools.ts); [`tool-executor.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/execution/tool-executor.ts); [`job-queue-service.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/adapters/src/job-queue-service.ts).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: downstream composition could add a real multi-agent coordination relation, but that would be a different system-in-focus and requires its own evidence.

### Absence scope

- Surfaces inspected: recursive sub-agents, parallel tool batching, background job queue, daemon worker, workflows/schedules, peer tool and approval queuing.
- Plausible first-party paths checked: simultaneous child delegation, shared tool-execution capacity, job-batch concurrency, scheduled runs and peer communication.
- Why no material first-party path remains: these mechanisms bound or transport work but no standard path establishes a specific disturbance between credited S1s and an S2 attenuation/feedback loop.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system inside-and-now current-control loop is established at the assessed deployment recursion.
- Disturbance / variety regulated: the parent agent decomposes its own task and the daemon/scheduler regulates execution mechanics, but no whole-deployment current operational variety is managed through a distinct S3 current view/decision loop.
- Decisive decision or feedback right: not established over current commitments/resources/priorities of all credited S1 units.
- Decision owner: none established for S3 at this boundary.
- Supporting / enforcement mechanisms: `spawn_subagent`, returned child results, workflow scheduler, job-batch status/cancel, approvals, daemon retries/recovery and normal run state.
- Closure path: not applicable; delegation supplies a task and later a child result, but the standard path does not close whole-system current view → S3 judgment → current intervention across S1 commitments → renewed whole-system feedback.
- Boundary reachability: the controls are first-party and reachable, but reachability/delegation does not establish the S3 function.
- Whole-system current view: not established. `spawn_subagent` is a synchronous tool-style child run with a final result; no standard live child-tree list/status surface was established for the parent.
- Current-control decision scope: the model can decide whether to spawn another bounded child, but no first-party path was found for persistent whole-tree steering, reassignment or interruption based on a current aggregate view.
- Why this is / is not agent-owned: no qualifying S3 function is established. Generic model orchestration of delegated subtasks remains part of current S1 task execution rather than a separately evidenced metasystemic regulator.
- Evidence: [`subagent-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/subagent-tools.ts); [`scheduler-service.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/workflows/scheduler-service.ts); [`job-worker.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/adapters/src/daemon/job-worker.ts).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a wider multi-agent composition can use Jazz agents as operating units, but that external organization is not the assessed Jazz deployment.

### Absence scope

- Surfaces inspected: sub-agent creation/result return, job batch list/cancel/fan-in, scheduler metadata/run triggers, daemon unattended resume, approvals and peer communication.
- Plausible first-party paths checked: parent sub-agent supervision, daemon-wide operations, workflow control and background-job management.
- Why no material first-party path remains: no reviewed path combines a whole-system current view of credited S1 commitments with discretionary cross-operation current-control rights and a feedback return loop.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary-audit closure is established at the assessed deployment recursion.
- Disturbance / variety regulated: Jazz exposes transcripts, run history, telemetry, eval/development checks and can run review tasks, but no materially independent audit loop is established over ordinary runtime claims.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S3* at this boundary.
- Supporting / enforcement mechanisms: logs/run history/telemetry, repository evals, GitHub PR-review workflow capability, generic recursive sub-agents and approval gates.
- Closure path: not applicable; reviewed surfaces can observe or evaluate work but no standard runtime path closes complementary access → independent audit judgment → finding returned into current organizational control.
- Claim being audited: no function-specific first-party claim/loop established for audit of the assessed Jazz organization.
- Ordinary reporting path: normal model/tool transcript, tool results, metrics and workflow/job status.
- Complementary access path: evals/review tasks can inspect outputs or repository state, but they are task/development surfaces rather than a distinct production audit channel over Jazz operations.
- Independence boundary: no audit-specific actor/sensor boundary separate from ordinary runtime reporting was established.
- Who acts on findings: a user or parent agent can act on a review result, but that generic composition is not a shipped S3* closure.
- Why this is / is not agent-owned: no S3* function is established before ownership classification.
- Evidence: [`README.md`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/README.md); [`packages/core/src/agent/tools/subagent-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/subagent-tools.ts).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: generic review/eval capability is intentionally not promoted to `C`; Methodology requires the S3* function itself to be established, not merely an extension point or promptable reviewer.

### Absence scope

- Surfaces inspected: recursive children, repository evals, PR-review use case, run history/metrics/telemetry, approval lifecycle and ordinary transcripts.
- Plausible first-party paths checked: reviewer child prompts, CI/PR review, observability and approval checks.
- Why no material first-party path remains: these either perform user tasks/development verification or expose ordinary evidence without an independent complementary audit judgment and corrective return path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then organizational adaptation loop is established at the assessed deployment recursion.
- Disturbance / variety regulated: web/search/peer information and memory can influence current/future task responses, but no organizationally scoped external/prospective adaptation function is established.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S4 at this boundary.
- Supporting / enforcement mechanisms: web/search tools, `ask_peer`, scheduled workflows, durable memory/context extraction, plugins/MCP and model/provider configuration.
- Closure path: not applicable; no reviewed path reconstructs external/future-relevant sensing → explicit adaptation option development → adaptation judgment → return into present Jazz organizational capability/control.
- Why this is / is not agent-owned: Jazz agents can autonomously research and remember information, but generic research/learning is part of task execution unless it participates in a demonstrated external-and-prospective organizational adaptation conversation.
- Evidence: [`peer-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/peer-tools.ts); [`packages/core/src/agent/context/memory-extractor.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/context/memory-extractor.ts); [`README.md`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/README.md).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a downstream organization may assign Jazz an S4 research/adaptation role; that role is not inherent in the frozen standalone harness.

### Absence scope

- Surfaces inspected: web/search, peer questions, memory extraction, workflows/schedules, model/provider configuration, plugins/MCP and recursive research children.
- Plausible first-party paths checked: external research, durable learned context, scheduled scans and capability configuration.
- Why no material first-party path remains: information acquisition and memory persistence are present, but no standard loop owns prospective organizational adaptation and returns chosen changes into present capability/control.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the assessed deployment recursion.
- Disturbance / variety regulated: persona, system prompt, permissions, approval policy, tool grants and user rules constrain operation but are not shown as identity-level policy issues resolved by an ultimate authority loop.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S5 within the standard Jazz deployment.
- Supporting / enforcement mechanisms: agent JSON configuration, persona/system instructions, permissions/approvals, auto-approval policy, peer grants, tool allowlists and operator configuration.
- Closure path: not applicable; no reviewed first-party path shows an identity/ultimate-policy issue reaching legitimate ultimate authority and returning as authoritative policy governing subsequent Jazz operation.
- Why this is / is not agent-owned: model agents operate within configured identity/permission boundaries; they are not shown exercising ultimate authority over those boundaries. Operator approval/configuration alone is not reclassified as S5.
- Evidence: [`README.md`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/README.md); [`packages/core/src/agent/tools/subagent-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/subagent-tools.ts); [`packages/core/src/agent/tools/peer-tools.ts`](https://github.com/lvndry/jazz/blob/957ad8ef522f9137f690c8acc319553f56e5bdb9/packages/core/src/agent/tools/peer-tools.ts).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: Jazz intentionally makes agent rules and permissions configurable; Methodology `0.3.6` does not treat configuration existence or ordinary approval as S5 without identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: persona/system configuration, tool permissions, approval/auto-approval policy, peer permissions, workflow agent binding and operator-managed model/tool configuration.
- Plausible first-party paths checked: human approval, permission escalation, persona/rule changes and peer authorization.
- Why no material first-party path remains: these define operational constraints and delegated authority, but no standard path elevates an identity/ultimate-policy issue to an ultimate authority and returns its resolution to govern subsequent operation.

## Distributed OSS parent arrangement

Jazz is open source, but repository maintainer/contributor governance was not used to infer runtime parent ownership. The assessed boundary is one operating Jazz deployment; project/release governance is adjacent unless wired into runtime decision closure, and no such parent S3/S4/S5 path is claimed.

## Self-hosted and non-human modes

Jazz can run locally/self-hosted and unattended through headless, workflow and daemon surfaces. Human approval can gate risky actions and configuration controls tool/model/peer access, but these generic controls do not establish parent notation for S3/S4/S5 without the corresponding organizational function.

## Recursion

The primary recursion is one Jazz harness deployment centered on a configured primary agent. Primary and recursively spawned child agents each instantiate an S1 model/tool feedback loop. Children are bounded, ephemeral delegated operations with fresh conversations; no separate first-party S2/S3 metasystem over the temporary child set is established. External peers are other organizations/environment rather than silently absorbed into the focal system.

## Variety and escalation

Jazz attenuates operational variety through tool allowlists, approvals, command risk policy, recursion/iteration limits, context compaction, generic tool concurrency limits, job-batch caps/retries/leases and scheduler bounds. Tool results, child results and peer answers return variety to the active S1. Approval-required actions can park/escalate to a human; failed background jobs retry/back off and fan in to resume the originating agent. These are operational containment/escalation mechanisms and are not double-counted as S2–S5 without function-specific closure.

## Evidence gaps

- No fresh runtime trace was executed inside this assessment environment; positive claims rely on pinned first-party source/docs and production wiring.
- S2 remains absent despite real recursive S1 plurality because no concrete inter-S1 disturbance → attenuation → behavioral-feedback witness was established.
- S3 remains absent because child delegation/result return lacks a standard live whole-system current view plus persistent cross-S1 intervention rights.
- S3* remains absent despite review/eval/observability surfaces because no materially independent production audit judgment plus corrective return path was established.
- S4 remains absent despite web/peer research and durable memory because these do not form an external/prospective organizational adaptation conversation.
- S5 remains absent despite persona/rules/permissions/approvals because configuration and action authorization do not establish identity/ultimate-policy closure.
