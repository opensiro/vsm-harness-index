---
harness_id: autonomous-coding-agent
project_name: Autonomous Coding Agent
repository: https://github.com/Quality-Max/autonomous-coding-agent
review_ref: eda302b5a93c877a4138855ea712000971c3abcf
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Autonomous Coding Agent

## Review boundary

- System in focus: the first-party deployable coding-agent application in `Quality-Max/autonomous-coding-agent` at frozen revision `eda302b5a93c877a4138855ea712000971c3abcf`, including the agent API route, prompt-governed coding loop, first-party planning/approval/tools, session-scoped sandbox lifecycle, provider routing, MCP composition and streamed UI.
- Purpose and identity: take a repository plus coding task, inspect and plan the work, obtain user approval before substantial mutation, then implement and verify changes inside an isolated coding sandbox.
- Relevant environment: user task and approval choices, target Git repository and filesystem, shell/test/build results, configured model provider, E2B sandbox, connected MCP services and preview/test surfaces.
- Standard-distribution boundary: the Next.js application, `/api/agent` route, first-party system prompt and tools, session/UI contract, router, sandbox lifecycle and MCP loading are inside. Vercel AI SDK, external LLM providers, E2B infrastructure, external MCP servers and target Git hosting are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: the ordinary web/BYOK deployment; model-driven coding route; `update_plan`, `request_approval`, command/file/edit/Playwright/preview tools; session-scoped coding sandbox; provider selection/fallback; MCP tool composition; streamed user interaction.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests, maintainer contribution/release decisions, the separate documentation/testing ecosystem linked from README, and demo/test fixtures that do not participate in ordinary deployed operation.
- First-party operating / deployment modes considered: self-hosted or public BYOK web deployment with one active coding session, optional first-party approval interaction, configured provider routing and optional connected MCP servers.
- Recursion level: one coding session/run is the operational unit. Tool calls, provider adapters, MCP tools and the separate desktop preview are mechanisms or subordinate actions rather than additional viable S1 units.
- Reviewed revision: `eda302b5a93c877a4138855ea712000971c3abcf`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The application exposes a streaming Next.js agent endpoint backed by Vercel AI SDK `streamText`. A first-party system prompt requires the model to create and maintain a plan, explore the repository, request user approval before the first mutating or outward action, then carry out the approved work and verify it. The route binds the selected model to first-party coding tools and optional MCP tools, limits a turn to 25 steps, and stops the turn when `request_approval` is called so the user's response can govern the next turn.

The first-party tool set provides plan updates, approval requests, shell execution, file reads/writes, exact and model-assisted edits, Playwright execution and public-port exposure. Coding state lives in an E2B sandbox keyed by session ID; the runtime reconnects where possible, refreshes the sandbox timeout during tool use, and tears sandboxes down on abort/stop/new-session paths. Provider routing selects among configured Anthropic, OpenAI, Google and Cerebras backends. Optional MCP servers extend the available tool set but remain external service dependencies.

## Operational model

The model actor receives the repository/task and conversation history, records a plan, explores through tools, and chooses subsequent actions from returned evidence. Before substantial mutation it must call `request_approval`; the route then terminates the turn. After the user selects an option or otherwise approves an approach, the conversation returns to the same first-party route and the model continues implementing the authorized work. This human gate constrains ordinary S1 action but does not by itself establish a distinct whole-system S3 or identity-level S5 function.

## S1 — Operations

- State: A
- Function: perform repository coding work by autonomously planning, inspecting, editing, executing and verifying inside a session sandbox.
- Disturbance / variety regulated: unfamiliar repository structure, incomplete task information, command/test failures, file contents, edit outcomes, provider outputs, optional MCP results and user approval constraints.
- Decisive decision or feedback right: choose what to inspect next, how to revise the plan, which coding/tool action to take within the approved scope, how to respond to concrete results, and when the requested coding outcome is complete.
- Decision owner: the active model-backed coding actor; the user owns the explicit approval gate for substantial mutation, while deterministic runtime machinery enforces turn/tool boundaries.
- Supporting / enforcement mechanisms: Vercel AI SDK tool loop, first-party system prompt, E2B sandbox, tool schemas, session ID, provider router, MCP loader, 25-step stop condition and streamed UI.
- Closure path: repository/task/context → model plan/action choice → first-party or MCP tool execution → concrete result re-enters conversation → model revises subsequent work until approval pause, completion or bounded stop.
- Boundary reachability: the ordinary deployed `/api/agent` route directly instantiates the model/tool loop and first-party coding tools without requiring adjacent development automation.
- Why this is / is not agent-owned: removing the model leaves the sandbox, tools, router and approval UI but removes the open-ended decisions that turn repository evidence into coding actions; deterministic machinery only executes or constrains those choices.
- Evidence: README; `app/api/agent/route.ts`; `lib/tools.ts`; `lib/sandbox.ts`; `lib/router.ts`; `app/page.tsx`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: mutation authority is deliberately interrupted by a user approval step before substantial work; this bounds S1 autonomy but does not remove the autonomous coding loop after approval.

## S2 — Coordination

- State: —
- Function: no distinct inter-S1 coordination function is established at the assessed recursion.
- Disturbance / variety regulated: the standard deployment presents one coding run/session; tool calls and optional MCP tools are subordinate capabilities rather than distinct operational S1 units whose interference must be damped.
- Decisive decision or feedback right: no S2-specific choice over conflict, oscillation or mutual adjustment among distinct S1 units was found.
- Decision owner: not established at S2 level.
- Supporting / enforcement mechanisms: ordered tool calls, one in-progress plan step, session-scoped sandbox state, MCP tool merging and user approval.
- Closure path: these mechanisms structure one focal coding run but do not close an inter-S1 stabilization loop.
- Why this is / is not agent-owned: sequencing and planning inside one S1 actor are operational control, not coordination among distinct operational units.
- Evidence: README; `app/api/agent/route.ts`; `lib/tools.ts`; `lib/sandbox.ts`; `lib/mcp.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external MCP servers may themselves contain multiple actors, but their internal organization is outside this harness boundary.

### Absence scope

- Surfaces inspected: agent route, plan/approval tools, coding tools, MCP loading, sandbox/session lifecycle, provider router, UI workspace/preview flow and repository architecture documentation.
- Plausible first-party paths checked: plan sequencing as S2; MCP tool aggregation as S2; sandbox/session isolation as S2; separate desktop/Playwright sandboxes as peer S1 coordination.
- Why no material first-party path remains: no inspected standard-distribution path establishes two distinct coding S1 units plus a specific interference relation and a coordination feedback loop that changes their subsequent behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established beyond regulation of the single focal coding run.
- Disturbance / variety regulated: task-local planning, approval, provider selection, sandbox lifetime and turn limits constrain current execution but do not constitute management of a standing set of operations on behalf of the whole.
- Decisive decision or feedback right: the user can approve or reject a proposed mutating approach and the model can manage its current plan, but no separate current-control authority over a portfolio of resources, commitments, priorities, accountability or inter-unit synergy is supplied.
- Decision owner: not established at S3 level.
- Supporting / enforcement mechanisms: `request_approval`, `update_plan`, 25-step cap, abort handling, sandbox teardown, provider selection and preview/session controls.
- Closure path: approval returns to the coding conversation and changes whether the focal S1 run may mutate state; that is an operational gate for one task, not a separate whole-system current-management loop.
- Why this is / is not agent-owned: task planning is part of S1 execution, while the human approval right is local task intervention rather than the Profile's whole-system S3 authority.
- Evidence: `app/api/agent/route.ts`; `lib/tools.ts`; README; `app/page.tsx`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the approval topology could participate in a larger parent-governed S3 composition, but that larger current-control function is not first-party in this frozen application.

### Absence scope

- Surfaces inspected: mandatory approval workflow, plan state, stop/abort path, session lifecycle, model/provider routing, MCP configuration, workspace UI and sandbox cleanup.
- Plausible first-party paths checked: user approval as S3 parent governance; plan tab as whole-system current view; provider routing as resource control; stop/teardown as supervisory intervention.
- Why no material first-party path remains: Methodology requires a whole-system current view plus a substantive current-control decision on behalf of the whole. The inspected mechanisms govern a single coding task/session and expose no separate management loop over multiple current operations.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary audit path sufficiently independent from ordinary production reporting is established.
- Disturbance / variety regulated: tests, shell output, generated Playwright execution and streamed tool results can challenge current coding work, but they remain ordinary evidence used by the same focal coding actor or explicitly requested user workflow.
- Decisive decision or feedback right: no separate auditor owns an independent claim-checking judgment that returns into a distinct control path.
- Decision owner: not established at S3* level.
- Supporting / enforcement mechanisms: test commands, `run_playwright_test`, live preview, streamed command/file/diff output and repository test suite.
- Closure path: verification results return directly to the same coding conversation as normal operational feedback; no complementary audit relation distinct from the production path is supplied.
- Why this is / is not agent-owned: an agent can run tests and inspect output, but self-checking in the ordinary coding loop is not sufficient independence for S3*.
- Evidence: README; `lib/tools.ts`; `lib/playwrightRunner.ts`; `app/api/agent/route.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a connected external MCP service could provide independent review, but external service behavior cannot donate a first-party S3* function.

### Absence scope

- Surfaces inspected: coding/test tools, Playwright runner, live preview, streamed tool outputs, MCP composition, repository tests and system prompt verification guidance.
- Plausible first-party paths checked: ordinary tests as audit; Playwright runner as audit; user visual inspection as audit; external MCP reviewer as audit.
- Why no material first-party path remains: inspected first-party paths are routine production verification or user observation and lack a distinct complementary-access/independence boundary with a separate audit judgment and control feedback path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop is established.
- Disturbance / variety regulated: the agent can inspect a target repository, use external MCP tools and switch configured model providers while solving the current task.
- Decisive decision or feedback right: no first-party process senses future-relevant environmental change, develops adaptation options for the harness and returns a selected option into present capability.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: model router, MCP connections, repository exploration, vision/recognition surface and configurable provider/model selection.
- Closure path: external/repository evidence changes current task execution or operator configuration, not a distinct outside-and-then adaptation cycle.
- Why this is / is not agent-owned: current-task research, provider fallback and model selection are operational mechanisms; they do not create future-oriented organizational adaptation.
- Evidence: README; `lib/router.ts`; `lib/mcp.ts`; `app/api/agent/route.ts`; recognition/vision routes.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: adjacent QualityMax ecosystem development and repository evolution are excluded from product-harness ownership.

### Absence scope

- Surfaces inspected: provider router, MCP integration, recognition/vision flow, repository exploration, configurable models, UI session flow and linked ecosystem documentation.
- Plausible first-party paths checked: model fallback as adaptation; recognition/vision as environmental sensing; MCP as external intelligence; repository exploration as S4.
- Why no material first-party path remains: each path serves the current task or static operator configuration and does not generate prospective adaptation options that return into the harness's present capability/S3 relation.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure is established at the assessed recursion.
- Disturbance / variety regulated: the first-party system prompt, approval requirement, safe MCP URL validation, credentials and operator-selected provider constrain ordinary execution.
- Decisive decision or feedback right: the user decides whether a proposed task mutation may proceed, but no identity/ultimate-policy issue is routed to legitimate authority and returned as a durable policy/identity decision for the harness.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: mandatory `request_approval`, prompt rules, schemas, SSRF guards, BYOK configuration, provider selection and stop/new-session controls.
- Closure path: user approval or rejection changes the next operational action inside the current task; it does not close an identity/ultimate-policy issue for subsequent system operation.
- Why this is / is not agent-owned: static prompt and safety constraints bound the agent, and the human has final say over particular substantial actions, but neither constitutes the Profile's S5 identity/policy function.
- Evidence: `app/api/agent/route.ts`; `lib/tools.ts`; `lib/mcp.ts`; README; `app/page.tsx`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: deployment owners can change configuration/source outside a run; generic configurability is not a first-party runtime S5 closure.

### Absence scope

- Surfaces inspected: system prompt, approval workflow, MCP safety validation, BYOK/provider settings, session controls, deployment documentation and contribution/governance surfaces.
- Plausible first-party paths checked: user approval as S5; system prompt as constitution; provider/model choice as policy; security guards as ultimate policy; maintainer governance as product-harness S5.
- Why no material first-party path remains: all inspected runtime mechanisms constrain ordinary task actions/configuration, while development governance is adjacent; no identity-level issue → legitimate authority → authoritative decision → returned durable operation path is established.

## Recursion

The assessed standard deployment exposes one model-driven coding run as S1. Tool invocations, Fast Apply helper inference, MCP calls, Playwright execution and separate preview sandboxes are subordinate mechanisms or dependencies, not demonstrated viable recursive operational units.

## Variety and escalation

The coding actor absorbs repository/task variety through plan revision, shell/file/edit tools, tests, model-assisted edits and optional MCP access. Before substantial mutation or outward action, variety exceeding the pre-approval operating boundary is escalated to the user through `request_approval`; the returned user choice constrains subsequent S1 work. Abort/stop and sandbox teardown provide deterministic safety enforcement.

## Evidence gaps

No `?` state is required. The frozen source is sufficiently explicit to establish the S1 loop and approval boundary, and the reviewed first-party runtime/docs/tools/UI surfaces are broad enough to support negative S2/S3/S3*/S4/S5 findings.

## Assessment summary

Autonomous Coding Agent closes S1 through a first-party model/tool coding loop inside a session sandbox, with an explicit human approval gate before substantial mutation. The standard application does not establish distinct inter-S1 coordination, whole-system current control, complementary independent audit, prospective adaptation or identity-level policy closure.

**Vector:** A · — · — · — · — · —
