---
harness_id: earshot
project_name: earshot
repository: https://github.com/rishabhguptajs/earshot
review_ref: 5c7f2569631a21961e637e1d57165a9e02db9f4d
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# earshot

## Review boundary

- System in focus: the released local-first earshot coding-agent CLI, its first-party model/tool loop, permissions, declared-scope enforcement, agent-to-agent task tool, session and operator controls, memory, verification and model/provider routing.
- Purpose and identity: assist repository coding in interactive TUI, headless and editor-facing modes while preserving declared task scope, user instructions, cost ceilings, tool receipts and honest completion.
- Relevant environment: source files and tests, user instructions, tool outputs and failures, third-party model/provider variability, changed permission/scope state, model budgets and configured external MCP tools.
- Standard-distribution boundary: first-party TypeScript code under packages/core, providers, cli, tui, acp and mcp as wired to the published earshot CLI. The optional task subagent and verification mechanisms are included; user-installed extensions are mechanisms, not credited as prebuilt independently deciding owners.
- Credited operating / distribution surfaces: interactive TUI and headless Agent.runTurn, provider bridge, file/shell tools, scoped permission approvals, task nested agent, interruption/steering, session tree, post-edit verification, tool hooks, provider pool and ACP wiring.
- Adjacent first-party surfaces excluded from ownership: documentation roadmap and unshipped trust-at-scale designs, CI/test fixture actors, benchmarks, release acceptance, upstream provider internals, user-supplied MCP servers/skills and the project developer organization.
- First-party modes checked: model/tool turns, read-only parallel tool calls versus serial mutating calls, permission/plan mode, opt-in task child with default read-only tools and possible explicit tool subset, self-check after a mutation, background bash jobs, session cost guard, memory proposals and provider pool.
- Recursion level: one installed coding-agent operating organization. The main agent and separately model-backed task child are bounded operating actors; the child's tools and authority are inherited from the parent run, and no recursively viable child metasystem is credited.
- Reviewed revision: 5c7f2569631a21961e637e1d57165a9e02db9f4d (batch #1013 row 3). Observation date: 2026-10-24. MIT license.

## Repository architecture

The first-party Agent.runTurn model/tool loop in packages/core/src/agent.ts assembles the current request, streams model output, invokes model-selected tools with permission/scope checks, appends tool results and uses those results for subsequent model decisions. Executable entry points under packages/cli and packages/tui create sessions; the provider bridge in packages/providers handles transport rather than owning the task plan. Mutating tool calls in a model batch are serialized; read-only tools may run concurrently, but both belong to the same main operational agent rather than independent organizational units.

The shipped task tool starts a separately contextualized nested Agent for one delegated objective. It defaults to read/search tools, intersects any requested tools with the parent's allowed set, inherits the parent's permission and scope contract, sends child cost into the parent's total and returns only the child answer. The task tool itself is marked mutating and executed in the main loop's serial tool path; nested task spawning is disabled. Neither a sibling-workload allocation policy nor a whole-current portfolio manager is wired to this mechanism.

The built-in post-edit selfCheck executes a configured or detected project test command and returns its verbatim output to the *same* coding model alongside a completion prompt. It is operational verification, not an independent review actor: ordinary tests lack a complementary audit judgment owner and the same agent decides on repairs. The opt-in generic task tool could be instructed to perform review by a user or model, but no first-party specialist review mode with an evidence-grounded, sufficiently independent decision and corrective return is established here.

Frozen source anchors: [Agent loop](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/agent.ts), [task tool](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/tools/task.ts), [scope contract](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/scope/contract.ts), [post-edit tests](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/verify/run.ts), [settings](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/permissions/settings.ts).

## Operational model

The user submits a coding request to a single main model-backed actor. Its proposed tool actions are gated by rule precedence, declared scope and approvals, and their observed output reenters its model transcript. When chosen, a task subagent executes a separate bounded investigative loop, returning only conclusions and consumed cost. Session history, memory and portable provider state support that work. No live model/provider execution was used for this source assessment.

## S1 — Operations

- State: A
- Function: adapt source-repository inspections, edits and commands to an open-ended coding objective using model-selected tool actions and returned evidence.
- Disturbance / variety regulated: unforeseen source structures, task ambiguity, failed shell commands, permission refusals, test failures, provider errors and changing user requests.
- Decisive decision or feedback right: choose, revise and stop concrete coding actions and delegated investigation steps in response to tool results and user steering.
- Decision owner: the main earshot coding model; an optional task child separately selects bounded tool calls for its assigned subtask.
- Supporting / enforcement mechanisms: CLI/ACP/TUI adapters, provider translation, tool registry, deny-first permission engine, scope guard, undo, bounded steps/cost, session replay, tests and memory.
- Closure path: user objective + repository state → model chooses tool actions → first-party gate/dispatcher executes or refuses → result and failure return to transcript → model corrects actions or answers.
- Boundary reachability: Agent.runTurn is used by supported CLI/TUI/headless sessions, with first-party file/shell/search tools and a real model stream bridge; the loop is not a prompt-only architecture proposal.
- Why this is / is not agent-owned: static tool executors cannot independently decide code changes and revise them from arbitrary context; model-generated choices own that operational discretion while host policy constrains it.
- Evidence: [packages/core/src/agent.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/agent.ts), [packages/core/src/tools/index.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/tools/index.ts), [packages/core/src/session/create.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/session/create.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider response quality and live coding success were not exercised; scripted tests establish wiring, not real-model effectiveness.

## S2 — Coordination

- State: —
- Function: no distinct first-party interference attenuation and feedback relation between independently operating S1 units is established.
- Disturbance / variety regulated: potential child/parent workspace conflicts, concurrent tool actions and shared spend; these are bounded by local execution sequencing and task/session permissions rather than a distinct closed inter-S1 coordination relation.
- Distinct S1 units: the main model and an optional nested separately contextualized task model; multiple tool calls from the same parent are not separate S1 organizations.
- Inter-S1 disturbance: a delegated child might contend with parent edits or share its cost ceiling; this possible conflict does not by itself demonstrate a qualifying S2 response.
- Attenuating coordination relation: the task tool is treated as mutating and serialized in the parent model batch; the child shares a permission/scope object and cost counter. Those protections are local task sequencing and inherited guards, not a cross-unit adaptive coordination bargain.
- Feedback into subsequent S1 behaviour: a child answer and cost return to the parent model, but no S2-specific conflict observations drive an independently decided quota, priority or interference-resolution policy.
- Decisive decision or feedback right: no S2-specific decision right established.
- Decision owner: parent S1 selects task delegation; developers provide static scheduling/permission enforcement; neither owns an evidenced standalone S2 feedback cycle.
- Supporting / enforcement mechanisms: runCalls read-only concurrency and serialized mutations, non-nesting task restriction, shared ScopeContract, budget counter and child result return.
- Closure path: task request → sequential nested child → bounded answer/cost → parent turn exists, but distinct-S1 interference → S2 attenuation decision → corrected sibling operating conditions is not established.
- Boundary reachability: the task tool and guards are shipped and reachable; no additional coordinator or shared-resource conflict arbitration mode was found.
- Why this is / is not agent-owned: choosing to delegate an investigation and applying static guards does not give a separate actor coordination decision ownership.
- Evidence: [agent runCalls and subagent](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/agent.ts), [task.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/tools/task.ts).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: explicit child tools may permit writes, subject to shared scope/permissions, but serialized spawning and return do not create an evidenced shipped multi-S1 S2 function.

### Absence scope

- Surfaces inspected: main batch scheduler, task tool, child construction, parent/child scope sharing, budget/usage feedback, tool execution and background job registry.
- Plausible first-party paths checked: mutation serialization as S2, multiple read calls as distinct S1s, parent-child shared cost as contention regulation, and user/operator mediation of child-file conflicts.
- Why no material first-party path remains: those paths control one task actor or sequentially delegated child work; no live independent-unit conflict regulator with actionable inter-S1 return was found.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current control of commitments and resources across a population of separately accountable operating units is established.
- Disturbance / variety regulated: cost ceilings, status, interruptions, current todo and background-job changes are limited to an individual session/task.
- Whole-system current view: session transcript, todo list, background process map and operator UI show local activity rather than a system-wide portfolio of independently accountable S1 units.
- Current-control decision scope: the main Agent can revise its task and the user can steer, halt, resume, fork and rewind sessions; these are operational controls without a separate current-allocation authority.
- Decisive decision or feedback right: no S3-specific resource/commitment arbitration decision identified.
- Decision owner: user/session and main S1 task loop; neither constitutes an established separate organizational S3 owner.
- Supporting / enforcement mechanisms: event stream, background jobs, scope approvals, session tree and cost prompt.
- Closure path: operational session receipts → operator/model task changes exists, but a whole-current multiactor control decision and return path are not wired.
- Why this is / is not agent-owned: the main Agent's current tool choices are S1; a user's permission or process-control choice is not whole-system governance merely because it is manual.
- Evidence: [agent.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/agent.ts), [jobs.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/tools/jobs.ts), [session/store.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/session/store.ts).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: task-facing human supervision exists, but the assessment does not identify a distinct whole-current S3 resource-control mode.

### Absence scope

- Surfaces inspected: TUI/CLI control modes, main agent, task children, background job registry, sessions, budget prompts, tool permissions and todo state.
- Plausible first-party paths checked: user as parent S3, task model as manager, job status as whole-system dashboard and multi-session operating commitments.
- Why no material first-party path remains: current controls act within a selected task/session and do not close a separate portfolio-level resource or commitment management function across independent S1 units.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent first-party complementary operational audit judgment with corrective return is established.
- Disturbance / variety regulated: possible unverified coding claims, skipped tasks and defects are addressed by ordinary model self-check plus detected project test commands, not a distinct audit owner.
- Claim being audited: the coding agent's assertion that requested edits are complete and tests pass.
- Ordinary reporting path: same Agent collects tool outputs, test runner stdout/stderr and a completion self-check prompt.
- Complementary access path: tests execute actual workspace state, but they are routine project checks and have no separate first-party risk/claim assessor; generic subagent research is not a specialized reviewer.
- Independence boundary: the model receiving verification output is the model whose coding decisions are being checked; user/project-controlled test commands do not instantiate a distinct complementary audit authority.
- Audit judgment / decisive feedback right: no distinct first-party independent judgment right found; the main Agent still judges meaning and repair.
- Decisive decision or feedback right: no S3*-specific corrective audit verdict right established.
- Decision owner: main task model for interpretation; deterministic test processes report outcomes, while the operator controls any optional third-party reviewer.
- Supporting / enforcement mechanisms: detectTestCommand, runVerification, selfCheck, test output receipts and generic task child.
- How findings enter subsequent control: test stdout/stderr return to the model, which may attempt repairs; this is ordinary task feedback, not a separately owned complementary audit.
- Who acts on findings: the main coding Agent, constrained by normal permission/scope policy.
- Closure path: edited files → test command and same-agent selfCheck → subsequent main-agent response exists; complementary independent risk judgment → corrective control is not established.
- Boundary reachability: automatic post-edit verification is shipped and executable; no built-in independent reviewer specialization or evidence-grounded audit workflow is evidenced.
- Why this is / is not agent-owned: the model can assess its own output, but is not thereby an independent reviewer of its own report; deterministic test execution is not an autonomous complementary judgment owner.
- Evidence: [selfCheck in agent.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/agent.ts), [verify/run.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/verify/run.ts), [task.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/tools/task.ts).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: custom external skills, hooks or task prompts can create review arrangements, but they are not a shipped first-party independently grounded S3* claim at this frozen boundary.

### Absence scope

- Surfaces inspected: post-edit selfCheck, verification command detection and execution, child task prompt and tools, hook executor, ordinary tool results, scope contract and TUI session feedback.
- Plausible first-party paths checked: automatic tests as S3*, child research as a first-party reviewer, external test/skill/hook reviewer injection and transcript honesty prompts as audit.
- Why no material first-party path remains: no separate audit decision owner with complementary access and returned risk judgment was identified beyond generic user-composed extension possibilities.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed environment-scanning and prospective organizational capability-selection cycle is established.
- Disturbance / variety regulated: provider/model availability, context pressure and persistent user preferences are handled for present and repeated tasks, without a demonstrated future-option adoption program.
- Decisive decision or feedback right: no separate forward-looking adaptation selection and authorized capability change return.
- Decision owner: operator/project configuration for model choices and remembered preferences, with deterministic provider pool and in-turn model decisions.
- Supporting / enforcement mechanisms: memory candidate regex, user-approved memory files, models.dev catalog refresh, portable free-model routing, context compaction and roadmap milestones.
- Closure path: feedback/preferences → stored operating context or current provider fallback exists; environmental horizon sensing → future capability option → organizational implementation feedback is absent.
- Why this is / is not agent-owned: preference detection and provider routing do not constitute agent-owned strategic design, experimentation and adoption of new capabilities.
- Evidence: [memory/detect.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/memory/detect.ts), [pool/router.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/pool/router.ts), [context/compaction.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/context/compaction.ts).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: the provider catalog can refresh from an external registry; that data update alone is not an autonomous organizational future-capability adoption decision.

### Absence scope

- Surfaces inspected: provider catalog and pool routing, persistent preference memory, session/context compaction, agent loop, release roadmap and extension/skills integration.
- Plausible first-party paths checked: learned preferences as S4, future model adaptation through catalog refresh, provider failure recovery, automatic installed skill/tool evolution and roadmap implementation.
- Why no material first-party path remains: these are task/context reactions, external configuration or adjacent development plans; no product S4 option-evaluation/implementation cycle was found.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate organizational identity/policy adjudication and return path at the assessed recursion.
- Disturbance / variety regulated: tool risks, permissions, external paths, budget ceilings and scope changes are operational constraints rather than ultimate-identity controversies.
- Decisive decision or feedback right: no qualifying constitutional purpose/identity decision right identified.
- Decision owner: user/developer choose standing rules and task approvals; deterministic engine enforces those external choices.
- Supporting / enforcement mechanisms: deny-first permission rules, plan/ask/auto modes, ScopeContract, operator prompts, persistent allow choices, settings and session budgets.
- Closure path: operator config/ask → deterministic tool allow/deny or scope confirmation → operational tool action exists; identity-level policy conflict → legitimate ultimate S5 decision → authoritative organizational return is absent.
- Why this is / is not agent-owned: an allow-always choice or project scope rule is not automatically an ultimate-purpose decision merely because it persists beyond one tool call.
- Evidence: [permissions/engine.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/permissions/engine.ts), [permissions/settings.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/permissions/settings.ts), [scope/contract.ts](https://github.com/rishabhguptajs/earshot/blob/5c7f2569631a21961e637e1d57165a9e02db9f4d/packages/core/src/scope/contract.ts).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: legitimate humans supervise routine tool safety and permissions; this narrow fact does not warrant S5=P without a whole-organization ultimate-policy controversy and closure.

### Absence scope

- Surfaces inspected: all permission modes and precedence, persisted project/global/local rules, scope confirmations, human ask path, model/provider policies, cost ceilings and first-party governance/release documents.
- Plausible first-party paths checked: human as S5 through allow-always approval, deny-first engine as constitutional authority, automatic identity-policy revision and organizational mission adjudication.
- Why no material first-party path remains: observed controls authorize tools, task boundaries and spending; no installed identity-level legitimate decision institution with authoritative organizational return exists.

## Recursion

The main and nested task models can be distinguished as operational actors, but the child has no independent full organizational metasystem. It is launched under the parent scope, tool/permission restrictions and cost accounting; nested task spawning is disabled. Provider systems, external MCP services, user teams and repository maintainers remain outside the selected product recursion.

## Variety and escalation

earshot amplifies task variety through model-selected repository tools, conditional child investigation, provider adapters and MCP extensions. It attenuates action variety through scoped tool rights, serialized mutations, explicit scope declarations, denied commands, runtime cost/step caps and literal test receipts. Permission and scope disputes can escalate to the human operator, but this is task-level gating rather than proof of S3/S5 organizational control. Verification reports are visible to the same agent and should not be miscast as complementary independent S3* evidence.

## Evidence gaps

- No provider-backed coding or reviewer-quality run was performed; first-party sources and deterministic checks support only shipped reachability and structural function mapping.
- Generic prompted task subagents can be directed to inspect code, but the frozen build does not establish independent S3* reviewer ownership as a bundled specialist mode; external configurations may change this for a particular installation.
- Cost sharing, serialized task calls and session steering do not establish separate inter-S1 conflict regulation or whole-current management at the declared boundary.
- Preference memory and provider catalog refresh do not demonstrate future-facing S4 adoption; permissions and human tool approvals do not establish ultimate S5 policy.
