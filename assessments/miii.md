---
harness_id: miii
project_name: miii
repository: https://github.com/maruakshay/miii-cli
review_ref: f84c629c91cd0ff096ff1f0a1231519cf6ea51b5
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# miii

## Review boundary

- System in focus: shipped native miii TypeScript local coding-agent CLI/TUI/headless distribution, including runAgent model/tool operation, task subagents, optional separate-model completion Decision Box, local permission policies, project context and persisted sessions.
- Purpose and identity: plan, investigate, edit and verify coding tasks with a selectable external/local model while enforcing local safety/approval boundaries.
- Relevant environment: current project files, shell and test results, configured inference endpoint, operator consent, filesystem mutations and persistent user/session context.
- Standard-distribution boundary: first-party executable miii app and bundled tools. Outside: upstream model internals, third-party MCP/plugin effects, user-authored agent definitions and repository development organization.
- Credited operating / distribution surfaces: `src/agent/loop.ts`, `src/agent/decide.ts`, `src/tools`, `src/prompt`, `src/session`, `src/permissions`, and first-party CLI/TUI/headless tool invocation.
- Adjacent first-party surfaces excluded from ownership: `eval/` benchmark infrastructure, documentation/demo media, contributor CI/release machinery, tests, and custom external MCP providers that are not part of the installed runtime.
- First-party operating / deployment modes considered: ordinary CLI/TUI local coding turns; headless scripted invocation; `task` subagent; optional configured Decision Box; plan/permission modes; persistent sessions/rewind; project/user instructions.
- Recursion level: one coding session as the focal organization; the child `task` agent is a subordinate local operational action with isolated context, not a demonstrated separate metasystem.
- Reviewed revision: `f84c629c91cd0ff096ff1f0a1231519cf6ea51b5`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The main `runAgent` is a provider/tool loop: it accepts a coding request, advertises first-party tools, normalizes model-generated tool calls, checks local read-before-write and permission/plan constraints, executes file/shell/search/edit tools, records tool results in history, and iterates until the model finishes or a bounded stop fires. The distribution also has JSONL sessions and file checkpoints for recovery/rewind.

The model may call `task` to run one self-contained child `runAgent` with fresh history, a limited tool set and bounded turns, returning a final report to the parent. Its stated aim is context budget protection, not coordinated parallel worker governance. A separately configured Decision Box can use a second inference model to decide whether a final claim matches the request, but the supplied evidence is a clipped user request, summarized tool-use trail and assistant final text; there is no independent file-reading audit path in this judging mode. The runner may return one additional corrective nudge.

User/project `MIII.md` supplies remembered instructions; persisted permissions or read-only plan approval constrain tool authority. Those mechanisms are supporting safeguards, and neither model multiplicity, task nesting nor static permission policies automatically creates a higher VSM function.

Primary evidence: [agent loop](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/loop.ts), [task delegation](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/tools/task.ts), [Decision Box](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/decide.ts), [permissions](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/permissions/policy.ts), [project context](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/prompt/context.ts), [sessions](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/session/store.ts).

## Operational model

The main model selects task operations and responds to first-party tool feedback. A delegated `task` child can perform bounded local exploration or editing and report a result to the parent. The user may control permissions, plan approval and provider, but those settings are not whole-system or identity-governance decision rights. The separate completion judge is advisory, with normal execution reports as its evidence source.

## S1 — Operations

- State: A
- Function: Primary coding transformation via a model-driven tool loop.
- Disturbance / variety regulated: Unfamiliar code, changing files, user goals, test failures and tool errors.
- Decisive decision or feedback right: Choose next code action and tool call from the evolving conversation and returned tool results.
- Decision owner: Main miii model-based agent.
- Supporting / enforcement mechanisms: First-party model adapter, file/shell/search tools, permission and read-before-write guards, turn budget, JSONL session history and checkpoints.
- Closure path: User request → model selects a coding tool → first-party handler executes → tool result added to history → model selects its next action or completion.
- Boundary reachability: The shipped CLI/TUI/headless implementation wires runAgent to the native tool registry and executes those choices; this is not an illustrative SDK example.
- Why this is / is not agent-owned: The agent/model chooses operations and responds to observations; runtime and permission engine transport/enforce those choices.
- Evidence: [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/loop.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/tools/registry.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/session/store.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: External inference supplies decisions through the first-party loop; local permission configuration may require human action approvals..


## S2 — Coordination

- State: —
- Function: No qualifying first-party inter-S1 oscillation/interference-regulation relation established.
- Disturbance / variety regulated: No specific interference among distinct active S1 units is regulated by the shipped one-shot task delegation interface.
- Decisive decision or feedback right: None identified for S2; task delegation is a one-shot subtask request and final report.
- Decision owner: No established S2 decision owner.
- Supporting / enforcement mechanisms: Context-isolated child runAgent calls, task registry, todo records and shared working directory.
- Closure path: The child report returns to the sole parent agent, without a demonstrated feedback path that attenuates actual inter-child conflict.
- Why this is / is not agent-owned: Multiple child-capable tools do not establish coordination absent a specific inter-S1 disturbance plus an explicit regulator.
- Evidence: [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/tools/task.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/agents.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/loop.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/tools/write_todos.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A downstream custom workflow could establish S2 but is not credited to this standard distribution..

### Absence scope

- Surfaces inspected: First-party agent loop, task subagent implementation, builtin subagent definitions, tool registry and todo paths.
- Plausible first-party paths checked: Task dispatch, nested contexts, synchronous report return, todo status and common project filesystem.
- Why no material first-party path remains: The native task tool returns one bounded child's final report to its parent; no committed inter-S1 conflict detector, attenuating coordination decision or resulting peer behavioral adjustment is evidenced.


## S3 — Inside-and-now control

- State: —
- Function: No first-party metasystem-level whole-current regulation of shared operational commitments/resources established.
- Disturbance / variety regulated: Task completion uncertainty is checked, but a multi-unit whole-system current resource/commitment disturbance is not established.
- Decisive decision or feedback right: No S3 whole-current choice: ordinary action planning, a bounded continuation judgment and user permission gating regulate the same local S1 task.
- Decision owner: No qualifying S3 owner.
- Supporting / enforcement mechanisms: Decision Box, bounded turn counts, todo markers, read-before-write and permission gates, optional child task tool.
- Closure path: Completion uncertainty → optional judge nudge → same primary agent retries; does not close shared organization-level allocation/intervention.
- Why this is / is not agent-owned: The separate model sees a clipped tool history and final answer; it is neither a whole-system operational resource view nor a controller of several S1 commitments.
- Evidence: [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/loop.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/decide.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/tools/task.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/tools/write_todos.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/permissions/policy.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Stop/continue is meaningful for local task correctness, but alone cannot establish S3..

### Absence scope

- Surfaces inspected: Main runAgent turns, Decision Box, task subagents, permission/plan mode, todo state and hook gates.
- Plausible first-party paths checked: Second-model completion gate, delegated task status, maximum turns, runtime permissions, and model-authored planning.
- Why no material first-party path remains: None exposes a whole-system current operations view coupled to organizational authority over shared priorities, commitments or resources; the completion return is to the original coding agent.


## S3* — Complementary audit

- State: —
- Function: No sufficiently independent audit channel with alternative access to operating evidence and corrective return.
- Disturbance / variety regulated: A main agent can claim successful work without actually satisfying all requirements.
- Decisive decision or feedback right: A separately configured judgment model may flag an incomplete request, but cannot independently inspect source reality through the shipped Decision Box interface.
- Decision owner: Optional judgment model owns a narrow advisory yes/no completion opinion; no complementary audit function established.
- Supporting / enforcement mechanisms: askBool/stopGate, JSON confidence parsing, clipped toolTrail from model history and one bounded retry nudge.
- Closure path: Main final message and ordinary tool log → second model says incomplete → primary agent may retry once; the audit access path never acquires independent operational evidence.
- Why this is / is not agent-owned: A different model reading ordinary agent reporting is not independent complementarity; deterministic completion checks or suggestions are part of task execution.
- Evidence: [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/decide.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/loop.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/tools/verifyHint.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/README.md).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Decision Box is optional and explicitly advisory; it provides no tool API for fresh repository inspection..

### Absence scope

- Surfaces inspected: Judge question/state encoding and stopGate, run loop integration, verification hints, tool results, hooks and builtin task agent definitions.
- Plausible first-party paths checked: Second-model completion verdict, Stop hooks, prompted testing, task child results and README review claims.
- Why no material first-party path remains: The second model consumes the request, up to 30 tool-result summaries and final claim, not independently acquired source or outcome facts. No other standard wired complementary evidence-acquisition and organizational review/correction chain was established.


## S4 — Outside-and-then intelligence

- State: —
- Function: No implemented prospective environment-facing adaptation organization at this recursion.
- Disturbance / variety regulated: Project demands may evolve, but there is no first-party future-facing distinction and capability renewal decision.
- Decisive decision or feedback right: No prospective adaptation decision identified.
- Decision owner: No established S4 agent, constructor or parent owner.
- Supporting / enforcement mechanisms: MIII.md human-maintained instructions, session persistence, checkpoint/rewind, provider switching, model prompt repairs and extension hooks.
- Closure path: Past instructions are re-injected when a session loads but not after an autonomous forecast/adaptation decision changing future capability.
- Why this is / is not agent-owned: Retaining knowledge, recovering a session or choosing another model manually does not demonstrate S4 environment/prospective governance.
- Evidence: [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/prompt/context.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/session/store.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/config.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/prompt/system.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/hooks/run.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: Custom scripts/user instructions can extend the application but are not evidenced as a built-in S4 decision loop..

### Absence scope

- Surfaces inspected: Project/user MIII.md read/append, provider/settings code, model prompt, persistent sessions, checkpointing, hooks and subagent definitions.
- Plausible first-party paths checked: Remembered notes, model hot-swap, prompt/context reduction, durable session restart, user-authored agent extensions.
- Why no material first-party path remains: No first-party path identifies externally arising future threats/opportunities, develops capability options, decides among them and returns a change into the current organization.


## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy decision and return loop.
- Disturbance / variety regulated: Tool action safety, approval and prompt instructions constrain tasks, but are not identity or ultimate-policy questions.
- Decisive decision or feedback right: None established for runtime ultimate purpose or governing identity.
- Decision owner: User sets permission mode/instructions and can approve a plan or individual tool invocation; deterministic code applies rules.
- Supporting / enforcement mechanisms: Project/user permissions.json, plan read-only guard, user approval prompts, MIII.md instruction hierarchy and configurable modes.
- Closure path: Human approval returns to a specific tool/plan action, not an organizational identity or ultimate-policy decision governing subsequent operation.
- Why this is / is not agent-owned: Operator configuration and action-level consent are not the same as ultimate-policy closure at the assessed recursion.
- Evidence: [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/permissions/policy.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/prompt/system.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/prompt/context.ts); [first-party source](https://github.com/maruakshay/miii-cli/blob/f84c629c91cd0ff096ff1f0a1231519cf6ea51b5/src/agent/loop.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Human oversight exists but does not justify S5=P absent a function-specific parent governance loop..

### Absence scope

- Surfaces inspected: Permission modes and persisted project/user rules, plan exit and consent, project context and system prompts, hooks, operator settings.
- Plausible first-party paths checked: Shell/file permissions, mode switching, user plan approval, static policy and model changes.
- Why no material first-party path remains: No runtime first-party identity/policy-level issue, legitimate ultimate authority decision and governance-return path is supplied at the coding-session organization boundary.


## Distributed OSS parent arrangement

Public repository contributors, maintainers, CI, evaluations and release governance are separate from an installed miii coding-session organization. No project-wide parent S3/S4/S5 mode is imported from GitHub-based development or users running independent copies of the tool.

## Self-hosted and non-human modes

Model inference can be local or hosted with the same first-party loop. Permission bypass/default/plan changes constrain tool execution, not VSM ownership classification. No human `(P)` is credited solely from a user pressing approve or editing a configuration file.

## Recursion

A task subagent owns local tool choices on an isolated subtask, but synchronous one-shot delegation is not itself recursion or inter-S1 coordination. No first-party cross-unit current metasystem is established at the declared session boundary.

## Variety and escalation

Tool errors, repeated failing calls and file-state conflict can lead the same agent to retry or stop. The optional Decision Box sends a completion nudge, and user steering messages are consumed after tools return. These are S1 operating feedback/safety processes, not automatically S2/S3/S3*/S4/S5.

## Evidence gaps

- The optional Decision Box has an independently configured model but not complementary operational evidence; no claim about empirical defect-detection rate follows from this review.
- Negative states are scoped to the inspected native distribution. User-provided plugins, custom task agents, and external enterprise governance can change a deployed organization but are not part of the evidenced first-party boundary.
- This is a pinned-source qualitative classification only, not an executed model benchmark or an estimate of coding performance.
