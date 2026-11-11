---
harness_id: lumak
project_name: LumaK
repository: https://github.com/kuLm1Fs/lumak-ts
review_ref: ef1d2ddb16630e537c205fadb11031ba7bae6131
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# LumaK

## Review boundary

- System in focus: LumaK's TypeScript agent, shipped role prompts, workspace tools and CLI, embedded TUI and WebSocket gateway entrypoints.
- Purpose and identity: Understand and edit a local codebase with bounded tool access and delegated support.
- Relevant environment: Local workspace, configured model endpoint, optional MCP code intelligence, role permission policy and operator approval mode.
- Standard-distribution boundary: CLI, TUI and gateway all bind the same Agent core and provider adapter. The installed core packs its own role prompts. Configured external MCP servers and inference services provide capabilities outside the first-party execution boundary.
- Credited operating / distribution surfaces: [`apps/cli/src/commands/chat.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/apps/cli/src/commands/chat.ts), [`apps/tui/src/embedded-runtime.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/apps/tui/src/embedded-runtime.ts), [`packages/gateway/src/chat.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/gateway/src/chat.ts), [`packages/core/src/agent.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/agent.ts), [`packages/core/src/runtime/loop.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/loop.ts), [`packages/core/src/runtime/delegate.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/delegate.ts), [`packages/core/package.json`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/package.json), [`prompts/subagent-reviewer.md`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/prompts/subagent-reviewer.md)
- Adjacent first-party surfaces excluded from ownership: Live eval scripts, optional external MCP language servers, legacy Python runtime and user-created skills. Development tests and telemetry alone do not add operating actors.
- First-party operating / deployment modes considered: One-shot and interactive CLI, embedded TUI, Web UI via gateway. Auto and approve modes may run delegated work; plan mode denies the delegate tool and keeps its review path outside that mode.
- Recursion level: A top-level coding session contains the primary operation and optional bounded child loops. A separate delegated reviewer can inspect its work product at the coding-session level.
- Reviewed revision: `ef1d2ddb16630e537c205fadb11031ba7bae6131`, [intake #3059](https://github.com/opensiro/vsm-harness-index/issues/3059) and [controller #3060](https://github.com/opensiro/vsm-harness-index/issues/3060).
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Agent selects the configured model, workspace guard and registry with delegate mounted. The loop asks the model, executes ordinary tools in order, then may execute delegated child calls in parallel and return results to the parent request context.
The reviewer role starts a fresh child run with a dedicated review prompt and read-only tools in the same workspace. Its structured answer returns to the parent as a tool result. The parent may use it to fix or report issues, subject to its current permission mode.

## Operational model

S1 performs model-guided local coding and investigation. The optional S3* path challenges code changes with a separately prompted reader of workspace evidence. Child review is selected by the parent model and can require operator approval in approve mode.

## S1 — Operations

- State: A
- Function: Use workspace tools to answer a coding task and, when authorized, change code.
- Disturbance / variety regulated: Ambiguous user goals, workspace state, tool errors, context pressure and permission decisions.
- Decisive decision or feedback right: Select navigation, file/tool actions, delegation and revisions in response to observed results.
- Decision owner: The active model-backed Agent owns the semantic tool and revision choices. Operator permission constrains certain actions.
- Supporting / enforcement mechanisms: WorkspaceGuard, provider adapters, tool registry, dedup cache, role modes, session store and traces.
- Closure path: Task → model request → selected workspace tool → result or denial enters messages → subsequent action or terminal answer.
- Boundary reachability: CLI, embedded TUI and gateway instantiate Agent. Supported auto mode permits the loop to choose and apply local edits within the workspace.
- Why this is / is not agent-owned: Choosing the next investigation or edit is model-owned. The runtime constrains and executes those choices.
- Evidence: [`apps/cli/src/commands/chat.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/apps/cli/src/commands/chat.ts), [`packages/core/src/agent.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/agent.ts), [`packages/core/src/runtime/loop.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/loop.ts), [`packages/core/src/runtime/tool-call.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/tool-call.ts), [`packages/core/src/providers/factory.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/providers/factory.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

## S2 — Coordination

- State: —
- Function: No distinct response to lateral interference between independent coding units is established.
- Disturbance / variety regulated: Concurrent children can share a workspace and issue overlapping operations.
- Decisive decision or feedback right: Observe an actual cross-child conflict and coordinate a subsequent change in both affected operations.
- Decision owner: Main model delegates tasks; the runtime executes child calls concurrently and joins results.
- Supporting / enforcement mechanisms: Promise.all, parent permission ceiling, read-only roles and per-call tool execution.
- Closure path: Children return outcomes to the parent. The shipped scheduling relation does not bind sibling conflict detection and adaptive redistribution.
- Boundary reachability: Agent registry supplies the delegate tool. Child loops have no recursive delegate path.
- Why this is / is not agent-owned: Delegation, capability limits and a final join support the parent task without defining a lateral conflict-resolution loop.
- Evidence: [`packages/core/src/runtime/loop.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/loop.ts#L425-L465), [`packages/core/src/runtime/delegate.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/delegate.ts), [`packages/core/src/runtime/permissions.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/permissions.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Parent dispatch, child run configuration, parallel wait and shared workspace tool paths.
- Plausible first-party paths checked: Read-only role narrowing, independent tasks in the system prompt and parallel editor calls.
- Why no material first-party path remains: Children do not receive sibling interference signals or coordination decisions. The parent sees results and may choose follow-up work within its task.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control mode is established across coding sessions.
- Disturbance / variety regulated: Active session errors, tool requests, workspace selection and availability.
- Decisive decision or feedback right: Intervene in whole-system resource commitments using a current operating view and returned decision.
- Decision owner: Operator governs a local session and tools. The primary agent delegates its own work.
- Supporting / enforcement mechanisms: Gateway conversation and trace views, approval prompts, loop limits and cancellation.
- Closure path: Approvals or changed modes affect specific calls or sessions.
- Boundary reachability: Gateway supports session and project state operations, while Agent handles each turn.
- Why this is / is not agent-owned: Current workspace and per-call permissions do not form a portfolio-control decision or feedback relation.
- Evidence: [`packages/gateway/src/server.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/gateway/src/server.ts), [`packages/gateway/src/state.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/gateway/src/state.ts), [`packages/gateway/src/chat.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/gateway/src/chat.ts), [`packages/core/src/runtime/permissions.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/permissions.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Gateway state, traces, session switching, CLI mode changes, delegation and approvals.
- Plausible first-party paths checked: Human trace inspection, pending approval handling and session-specific interventions.
- Why no material first-party path remains: No shipped owner combines a whole-current view and discretionary resource or priority intervention across operations.

## S3* — Complementary audit

- State: A
- Function: Complement the producing agent's own work report with a separate read-only inspection of code changes.
- Disturbance / variety regulated: Latent implementation defects or gaps that remain after the producing agent's own tool feedback.
- Decisive decision or feedback right: Inspect the target files and judge whether the implementation contains issues worth correction.
- Decision owner: The separately instantiated reviewer model makes the review judgment. The parent model decides whether and how to revise.
- Supporting / enforcement mechanisms: Built-in delegate tool, reviewer-specific prompt, role-bound read-only tools, shared workspace and returned DelegateReport.
- Closure path: Primary model delegates review → fresh reviewer reads source files and reports → answer is appended as a tool result → parent model may edit or report in its next step.
- Boundary reachability: Default Agent registry mounts delegate; auto permits invocation and approve can permit it. The reviewer prompt is shipped by the core prepack configuration.
- Why this is / is not agent-owned: The child chooses its own read actions and findings in a fresh review context. The parent cannot substitute its own work report for that separate tool-backed review within this path.
- Claim being audited: Whether selected existing code or recent edits fulfill the implementation intent without defects relevant to the delegated review.
- Ordinary reporting path: The primary session observes its edit results, tool outcomes and its own response.
- Complementary access path: The role-specific child can read and search the shared workspace directly, with a fresh prompt and without edit permissions.
- Independence boundary: Separate child loop and prompt with read-only access. It uses the same configured provider and filesystem, and the parent chooses scope and contextual framing.
- Who acts on findings: The primary model reads the returned reviewer answer and can adjust implementation or report findings. The harness does not mandate review or enforce a verdict.
- Evidence: [`packages/core/src/agent.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/agent.ts), [`packages/core/src/runtime/delegate.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/delegate.ts), [`packages/core/src/runtime/prompts.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/prompts.ts), [`packages/core/src/runtime/permissions.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/permissions.ts), [`packages/core/src/runtime/loop.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/loop.ts#L438-L466), [`packages/core/package.json`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/package.json), [`prompts/subagent-reviewer.md`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/prompts/subagent-reviewer.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for reachability and separate artifact access; medium for practical independence under shared provider and parent-selected scope.
- Caveats: Conditional on a reviewer call with suitable tools and a code artifact to inspect. Static source demonstrates the corrective return path, not measured effectiveness or mandatory remediation.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective capability adaptation is established.
- Disturbance / variety regulated: Workspace changes, context overflow and availability of existing skills or provider tools.
- Decisive decision or feedback right: Observe future environmental change and select a durable adaptation returned to current capability.
- Decision owner: The operator supplies skill files and provider configuration; the runtime selects available inputs for the current task.
- Supporting / enforcement mechanisms: Skills selector, context truncation, optional MCP and persisted session memory.
- Closure path: A matching skill or retrieved context alters the current prompt.
- Boundary reachability: Built-in skill matching, session resume and provider selection are reachable.
- Why this is / is not agent-owned: Selecting stored guidance and reacting to current input are local operational behaviors.
- Evidence: [`packages/core/src/runtime/loop.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/loop.ts), [`packages/core/src/skills/selector.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/skills/selector.ts), [`packages/core/src/skills/store.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/skills/store.ts), [`packages/core/src/runtime/session.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/session.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Skill loader, prompt assembly, runtime memory, provider fallback and task delegation.
- Plausible first-party paths checked: Prewritten skill triggers, session restoration and locally generated content.
- Why no material first-party path remains: No first-party external-future sensing and capability adaptation decision is fed back into the harness.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity or policy arbitration is established.
- Disturbance / variety regulated: Current tool permissions and configured role boundaries.
- Decisive decision or feedback right: Arbitrate system mandate or ultimate policy and return a binding decision.
- Decision owner: The operator sets the tool mode and workspace; developer-defined role rules enforce limits.
- Supporting / enforcement mechanisms: CLI modes, approval gates and child permission ceiling.
- Closure path: Per-action approval and policy selection change what may run in the current session.
- Boundary reachability: Explicit CLI/Gateway approval and plan modes are shipped.
- Why this is / is not agent-owned: User consent to an action and a constructor policy do not establish a first-party ultimate identity decision process.
- Evidence: [`apps/cli/src/commands/chat.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/apps/cli/src/commands/chat.ts), [`packages/gateway/src/chat.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/gateway/src/chat.ts), [`packages/core/src/runtime/permissions.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/permissions.ts), [`packages/core/src/runtime/delegate.ts`](https://github.com/kuLm1Fs/lumak-ts/blob/ef1d2ddb16630e537c205fadb11031ba7bae6131/packages/core/src/runtime/delegate.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Permission mode choices, role ceiling, tool approval and shipped role prompts.
- Plausible first-party paths checked: Human approval or denial of writes/delegation and changes to local configuration.
- Why no material first-party path remains: The actual decisions regulate operational tool access and leave the system mandate outside the runtime.

## Recursion

A top-level coding session contains the primary operation and optional bounded child loops. A separate delegated reviewer can inspect its work product at the coding-session level.

## Variety and escalation

The runtime absorbs tool errors, repeated actions and context overflow. Optional review provides a separate feedback channel for latent code defects. Permission modes, loop caps and workspace boundaries constrain execution.

## Evidence gaps

No live provider or packaged install was run. The source supports optional review and corrective follow-up; review frequency and quality depend on the task and model.
