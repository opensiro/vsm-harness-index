---
harness_id: klaat-code
project_name: Klaat Code
repository: https://github.com/KlaatAI/klaatcode
review_ref: b988be7cf6ffe7878e87ed3e720759e0f7247c33
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Klaat Code

## Review boundary

- System in focus: the public first-party Klaat Code client/runtime at frozen revision \`b988be7cf6ffe7878e87ed3e720759e0f7247c33\`, including its local model/tool loop, built-in coding tools, permission/sandbox state, Plan/Build mode, local sessions/compaction/memory, subagent personas/background task registry, ACP path, hooks/plugins/MCP integration, verification/diagnostics and terminal/headless/server surfaces.
- Purpose and identity: provide a terminal coding agent that can inspect/edit/test a project, delegate scoped work to isolated-context subagents, run dedicated review subagents, and persist local operating state.
- Relevant environment: user goals/approvals, repository files, shell/test/typecheck outputs, background subagent status/results, provider/model responses, local session/memory/configuration, MCP/plugin services and hosted Klaatu API responses.
- Standard-distribution boundary: shipped public Klaat Code client/runtime only. Hosted Klaatu routing/model services, third-party model endpoints, MCP servers, browser/network services and the user's project are dependencies and cannot donate hidden VSM functions.
- Credited operating / distribution surfaces: \`src/screens/repl.ts\`, \`src/tools/\`, \`src/agent/\`, \`src/acp/\`, \`src/permissions/\`, local session/memory/configuration and supported terminal/headless/server/ACP paths.
- Adjacent first-party surfaces excluded from ownership: benchmark fixtures/solutions, CI/release automation, hosted KlaatAI/Klaatu server behavior not present in the public client, and roadmap-only worktree isolation.
- First-party operating / deployment modes considered: ordinary Build mode; read-only Plan mode followed by user approval; synchronous/background \`delegate_task\`; dedicated \`review\` persona; local/custom model endpoint use; headless \`run\`; API server/web; ACP; configured hooks/plugins/MCP.
- Recursion level: one Klaat Code coding session. The main coding agent and write-capable delegated build/general agents can each own bounded S1 outcomes. Dedicated read-only review agents are complementary audit actors, not coding S1s for the audited change.
- Reviewed revision: \`b988be7cf6ffe7878e87ed3e720759e0f7247c33\`.
- Observation date: 2026-10-06.
- Generated Profile version: \`0.2.4\`.
- Generated Methodology version: \`0.3.6\`.
- Current Profile version: \`0.2.4\`.
- Current Methodology version: \`0.3.6\`.

## Repository architecture

The REPL implements a model-owned coding loop over built-in tools, permissions, sandboxing and project evidence. The \`delegate_task\` tool can instantiate fresh isolated-context personas: read-only \`explore\` and \`review\`, plus write-capable \`build\` and \`general\`. Background delegations run concurrently, publish live status through \`task_status\`, and inject completion notices/results back into the parent conversation.

The public client does not expose a first-party inter-agent write-conflict controller for concurrent write-capable children. The README explicitly lists git-worktree isolation for parallel/risky sub-agent work as roadmap rather than current behavior. Likewise, \`task_status\` is observation-only: it lists/renders running tasks and final reports but supplies no per-child kill/steer/reprioritization right to the parent agent.

A dedicated \`review\` persona is shipped as data and reachable through the same model-callable \`delegate_task\` tool. It starts with an isolated context, is restricted to read-only repository/search tools, independently reads the specified code, and returns severity-ranked findings to the caller. This supplies a function-specific complementary audit path distinct from the main author's ordinary coding context.

## Operational model

The main model chooses coding actions, verification, delegation and completion. Deterministic code applies permissions, sandboxing, diagnostics, phase/cost limits, compaction and loop-breaker rules. Delegated agents get their own context and persona-scoped tools; only the final report returns to the parent.

Background task visibility and result delivery support delegation, but without a substantive live intervention/reallocation right they do not establish S3. Concurrent write-capable children make cross-agent interference possible, but without an implemented first-party collision attenuation/feedback loop they do not establish S2.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify a software project through model-selected coding/tool actions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, tool/process/test failures, context pressure, permissions, provider/model variation and bounded delegated subtasks.
- Decisive decision or feedback right: choose substantive coding/tool actions, decide whether to delegate, interpret returned evidence and determine when the task is complete.
- Decision owner: the active model-backed Klaat Code agent; write-capable build/general subagents own their bounded delegated work.
- Supporting / enforcement mechanisms: tool registry, permissions/sandbox, diagnostics/verification, Plan/Build mode, context compaction, phase/cost guards, sessions, provider routing and hooks/plugins/MCP.
- Closure path: user request → model selects direct action or delegated work → first-party runtime executes → results return to the model → model revises/validates or completes.
- Boundary reachability: ordinary REPL/headless/server paths instantiate the first-party model/tool loop; \`delegate_task\` is a built-in model-callable tool.
- Why this is / is not agent-owned: deterministic runtime code constrains and transports execution, but the model owns open-ended engineering choices and interpretation.
- Evidence: [README.md](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/README.md); [src/screens/repl.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/screens/repl.ts); [src/tools/index.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/tools/index.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: hosted Klaatu may perform additional routing, but no hidden hosted function is imported into this public-client assessment.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination loop is established.
- Disturbance / variety regulated: concurrent write-capable delegated agents can potentially overlap in one project workspace, but no implemented public-client mechanism is shown detecting/attenuating that peer interference.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persona tool scoping, permission prompts, atomic multi-file patch application and read-only explore/review personas constrain individual operations but do not coordinate peer write-capable S1s.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: the main agent may choose multiple delegated tasks, but delegation/concurrency is not itself coordination; roadmap worktree isolation cannot be credited as current runtime behavior.
- Evidence: [src/agent/personas.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/agent/personas.ts); [src/screens/repl.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/screens/repl.ts); [README.md](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: read-only personas are intentionally parallel-safe; that prevents one class of interference by capability restriction but does not establish a general S2 loop for the write-capable operational units.

### Absence scope

- Surfaces inspected: subagent personas, synchronous/background delegation, task registry, permissions/sandboxing, patch/write tools, project state management and roadmap.
- Plausible first-party paths checked: file/path leases, worktree isolation, peer scheduler, conflict detector, merge controller and cross-agent mutation feedback.
- Why no material first-party path remains: no current public-client path closes a concrete distinct-S1 interference → attenuation → feedback loop for write-capable children.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established over the live set of delegated operational commitments.
- Disturbance / variety regulated: background child status is observable, but no standard actor has a substantive live control right over individual current child commitments beyond initial delegation and later result use.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: \`task_status\`, live output tails, completion notices, loop limits, phase/cost stops and whole-turn cancellation expose/enforce state without supplying selective live child reallocation.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the parent agent can spawn and observe children but cannot kill, steer, retry or reprioritize a specific running background child through the reviewed tool surface.
- Evidence: [src/screens/repl.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/screens/repl.ts); [src/tools/index.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/tools/index.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: task visibility is necessary but insufficient; generic cost/loop stops and turn cancellation are enforcement/safeguards rather than whole-system current-control judgment.

### Absence scope

- Surfaces inspected: background task registry/status, completion injection, main-turn steering queue, cancellation, phase/cost budget guards and ACP session cancellation.
- Plausible first-party paths checked: selective child kill/retry/steer, dynamic priority/resource reallocation, whole-current dashboard controller and model-owned supervisor.
- Why no material first-party path remains: observed controls stop/bound a turn or report child state; they do not close a substantive whole-current management loop.

## S3* — Complementary audit

- State: A
- Function: independently inspect a coding claim/change through a separate fresh read-only review agent and return findings to the caller.
- Disturbance / variety regulated: bugs, edge cases, security issues, needless complexity and defects missed by the authoring agent's ordinary coding path.
- Decisive decision or feedback right: inspect repository evidence independently and produce severity-ranked findings or a clean judgment.
- Decision owner: the dedicated model-backed \`review\` persona instantiated as a fresh delegated agent.
- Supporting / enforcement mechanisms: isolated subagent context, read-only tool allowlist, dedicated review system prompt, separate routing tier/loop cap and final-report return to the parent.
- Closure path: main agent has a code/change claim → invokes \`delegate_task\` with \`agent: "review"\` and a self-contained target → fresh reviewer reads/searches repository evidence → reviewer returns findings → parent agent receives the final report and decides corrective/acceptance action.
- Boundary reachability: \`review\` is an explicit built-in persona and an enumerated value of the model-callable \`delegate_task\` tool.
- Why this is / is not agent-owned: the audit judgment is produced by a separate model context with direct repository-reading tools, not by deterministic linting or the author merely reviewing its own transcript.
- Claim being audited: a specified implementation/change or coding claim supplied by the main agent to the review subagent.
- Ordinary reporting path: the main/build agent's own tool results and completion statement.
- Complementary access path: the review persona independently uses read/search/code-graph/web-read tools in a fresh context.
- Independence boundary: isolated context, dedicated reviewer prompt, read-only capability boundary, no nested delegation and separate model loop.
- Who acts on findings: the parent coding agent receives the reviewer final report and owns subsequent repair or acceptance.
- Evidence: [src/agent/personas.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/agent/personas.ts); [src/tools/index.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/tools/index.ts); [src/screens/repl.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/screens/repl.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the slash \`/review\` path is not needed for this claim; S3* rests on the dedicated fresh delegated reviewer with direct evidence access.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no qualifying changing external/future condition is put under an owner that develops adaptation options and returns them into current organizational capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: automatic/session memory distillation, session resume, code graph, web tools, model switching, skills/plugins/MCP and update checks retain or extend capability but do not by themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: memory is distilled and injected into later sessions, but persistence/reuse of learned facts is not evidence of an external-and-prospective option-development loop returning into current S3 capability.
- Evidence: [src/agent/memory.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/agent/memory.ts); [src/screens/repl.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/screens/repl.ts); [README.md](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: hosted Klaatu routing cannot donate an unobserved S4 function to the public client.

### Absence scope

- Surfaces inspected: local memory/distillation, code graph, web tools, model/tier choice, skills/plugins/MCP, session resume, update checking and diagnostics.
- Plausible first-party paths checked: autonomous future-environment sensing, adaptation-option generation, durable learned policy/tool/model reconfiguration and feedback into current-control capability.
- Why no material first-party path remains: located mechanisms are context retention, current-task evidence, user configuration or software maintenance rather than S4 closure.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level policy issue is routed to an authoritative owner and returned as governing policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission rules, sandbox restrictions, project rules, system/persona prompts, config, hooks and Plan approval constrain execution without constituting identity governance.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: coding/review agents operate within user/developer-authored rules and have no authority to redefine Klaat Code's ultimate identity or governing principles.
- Evidence: [src/permissions/index.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/permissions/index.ts); [src/agent/personas.ts](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/src/agent/personas.ts); [README.md](https://github.com/KlaatAI/klaatcode/blob/b988be7cf6ffe7878e87ed3e720759e0f7247c33/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user approval in Plan/permission flows is operational authority, not an identity/ultimate-policy decision.

### Absence scope

- Surfaces inspected: system/persona prompts, permissions, project rules, config, hooks/plugins, Plan approval and provider/tier settings.
- Plausible first-party paths checked: autonomous constitution revision, parent identity governance, policy conflict adjudication and authoritative policy return.
- Why no material first-party path remains: all located policy surfaces are configured operating constraints rather than S5 closure.

## Distributed OSS parent arrangement

The assessed organization is the running public Klaat Code client, not KlaatAI's hosted service or GitHub maintainer organization. Hosted/model-service behavior is treated as environment unless the public client itself owns the relevant decision right.

## Self-hosted and non-human modes

Custom third-party model endpoints and headless/ACP modes use the same local tool/runtime boundary. The positive S1/S3* claims therefore do not depend on hidden hosted orchestration.

## Recursion

The session-level viable-unit candidate contains the main coding S1, optional write-capable delegated S1s and dedicated read-only review actors. Observation-only background task state does not create S3; missing write-conflict attenuation prevents S2.

## Variety and escalation

S1 handles ordinary coding variety. Dedicated review agents can independently challenge a coding claim under S3*. Permissions, diagnostics, auto-verification, compaction, budgets and doom-loop guards regulate execution but are not promoted to S2/S3/S4/S5 without their required decision loops.

## Evidence gaps

No \`?\` state is required. Frozen public source directly establishes the main/subagent/reviewer tool paths and exposes enough task-status, permissions, memory and roadmap state to support the bounded negative conclusions for S2/S3/S4/S5.
