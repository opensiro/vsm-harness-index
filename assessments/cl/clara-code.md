---
harness_id: clara-code
project_name: Clara Code
repository: https://github.com/ClarkQAQ/clara-code
review_ref: 9a9708dcc8828c934fadd22f32e053681a2718b8
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Clara Code

## Review boundary

- System in focus: The distributed Clara Code terminal coding assistant and its first-party session/task modules.
- Purpose and identity: Investigate, plan and implement code changes in a user workspace.
- Relevant environment: Local project and SQLite-backed sessions with a configured provider, and optional ACP peers.
- Standard-distribution boundary: Native terminal application, local agent loop, tools, goal and delegated task runtime. SDK assembly is a separate extension surface.
- Credited operating / distribution surfaces: CLI/ACP conversation construction, local task scope, built-in reviewer and plan-mode review.
- Adjacent first-party surfaces excluded from ownership: SDK-only custom hosts, development examples, provider internals, external ACP agents and external MCP servers.
- First-party operating / deployment modes considered: Bundled CLI in Agent, Plan and Review mode, local delegation and the first-party ACP entry point.
- Recursion level: One Clara conversation with its descendant workspace task cells.
- Reviewed revision: 9a9708dcc8828c934fadd22f32e053681a2718b8
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The CLI uses Clara's Go agent engine over local tool definitions and session storage. A conversation can persist an objective across turns, expose tools to a root agent, and build child sessions with scoped tool exposure. The foreground review command acquires the Git change set in plan mode. The local reviewer role can run separately with read-only file tools.

## Operational model

The root model uses project operations to satisfy requests. General children close delegated objectives and may write shared files. The root controls their briefs, status and lifetime. A reviewer can gather file evidence independently and return findings to the root.

## S1 — Operations

- State: A
- Function: Deliver coding, investigation or planning results over the local project.
- Disturbance / variety regulated: Changing user requests, tool failures, incomplete context and different workspace states.
- Decisive decision or feedback right: Choose tools, react to their results and decide the response.
- Decision owner: The configured Clara model within the native session.
- Supporting / enforcement mechanisms: Core step loop, local tools, session store and mode policies.
- Closure path: The tool results and subsequent user steering enter the running context. The model returns a final answer and the session records it.
- Boundary reachability: The CLI constructs a Core conversation with its own tool registry and starts the model loop using ordinary provider settings.
- Why this is / is not agent-owned: The model selects concrete operations. Tool dispatch and persistence enforce and report those choices.
- Evidence: [internal/cli/main.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/cli/main.go#L83-L135), [internal/coding/host.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/host.go#L175-L185), [internal/coding/host.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/host.go#L384-L397), [pkg/core/agent.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/core/agent.go#L924-L962)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: The deterministic demo is separate from evidence of agent ownership.

## S2 — Coordination

- State: A
- Function: Coordinate concurrently operating root and delegated units over a shared checkout.
- Disturbance / variety regulated: Child and root edits are immediately visible and can overlap, and wait timeouts can lead to duplicate ownership.
- Decisive decision or feedback right: Partition work and steer, wait for or redirect existing children when scopes collide.
- Decision owner: The root agent receiving task status and intervention tools.
- Supporting / enforcement mechanisms: Unique live task names, explicit instruction against overlapping edits, persistent in-turn child IDs and scoped messaging.
- Closure path: The agent can assign disjoint briefs, detect a busy or duplicate task, steer its existing child and observe its result before releasing it.
- Boundary reachability: Standard execute conversations attach local task tools; the shipped task prompt prescribes ownership and overlap handling.
- Why this is / is not agent-owned: The refusal of duplicate task names enforces part of the relation. The model determines task ownership and how to respond to conflicts.
- Distinct S1 units: The root coding unit and separate general child sessions that own assigned tasks and can edit.
- Inter-S1 disturbance: Overlapping edits and duplicate child work in the shared filesystem.
- Attenuating coordination relation: Disjoint briefs and persisted task IDs constrain interference, with steer and wait on the existing actor.
- Feedback into subsequent S1 behaviour: Steering changes the active child's next inputs. The parent sees the resulting status and output before deciding how work continues.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The supported instruction and controls specifically address conflicting writes and duplicate execution, beyond generic delegation.
- Evidence: [internal/coding/host.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/host.go#L175-L185), [internal/coding/tasks.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/tasks.go#L16-L49), [pkg/core/prompt/tasks.md](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/core/prompt/tasks.md#L3-L17), [pkg/tool/task_messages.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/tool/task_messages.go#L12-L50), [pkg/tool/task.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/tool/task.go#L128-L148)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Delegation must be authorized. The shared checkout is not a worktree isolation guarantee.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the current delegated commitments of a conversation.
- Disturbance / variety regulated: Children can stall, expend slots, or stay active after their work should stop.
- Decisive decision or feedback right: Choose which existing task is interrupted, continued or closed after inspecting the child portfolio.
- Decision owner: The model acting as root for the current conversation.
- Supporting / enforcement mechanisms: Scoped list, close/interrupt, bounded slots and parent-managed child lifetime.
- Closure path: The model's control action changes the child's running turn or ends it, releases session resources and returns the resulting status.
- Boundary reachability: The shipped host attaches the task controls to its operational root conversation.
- Why this is / is not agent-owned: Slot ceilings are fixed enforcement. They do not decide which commitment to stop or whether to retain its session.
- Whole-system current view: The active task list exposes each owned child, status and collected output across the focal conversation.
- Current-control decision scope: Stop, continue, steer or release selected delegated commitments.
- Evidence: [internal/coding/host.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/host.go#L175-L185), [internal/coding/tasks.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/tasks.go#L16-L19), [pkg/tool/task_messages.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/tool/task_messages.go#L32-L58), [pkg/tool/task.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/tool/task.go#L132-L163)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: This is control of the current conversation's children, not fleet-level control across users.

## S3* — Complementary audit

- State: A
- Function: Review a claimed code change by acquiring evidence from the actual workspace.
- Disturbance / variety regulated: A worker can report successful implementation despite defects or missed requirements.
- Decisive decision or feedback right: Determine and report actionable findings after direct file inspection.
- Decision owner: A separately started read-only reviewer model, whose findings the root agent can use.
- Supporting / enforcement mechanisms: Read-only reviewer tool set, empty child history by default, and task result return.
- Closure path: A dedicated reviewer inspects the files independently and returns findings through the task result. The root verifies and can issue follow-up work before closing children.
- Boundary reachability: The installed local task factory recognizes the reviewer role, creates it with real file access and returns its result through the ordinary wait path.
- Why this is / is not agent-owned: The reviewer makes the evidence judgment. Foreground /review is an additional review surface, not the basis for separate actor evidence.
- Claim being audited: The claim that the delegated change meets its brief and is safe to accept.
- Ordinary reporting path: The implementing child or root's own account of its work.
- Complementary access path: A separate reviewer session inspects shared project files with read-only tools.
- Independence boundary: Separate role, tool set and optionally fresh context, with source access beyond a text report.
- Who acts on findings: The root agent consumes findings and can direct additional work or withhold completion.
- Evidence: [internal/coding/tasks.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/tasks.go#L22-L61), [docs/usage.md](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/docs/usage.md#L128-L133), [pkg/core/prompt/tasks.md](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/core/prompt/tasks.md#L3-L17), [pkg/tool/task_messages.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/tool/task_messages.go#L32-L50), [internal/coding/host.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/host.go#L473-L481)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Source proves a supported optional path. It does not make every review independent.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective capability-adoption loop was established.
- Disturbance / variety regulated: Project instructions or tool catalogs can change.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Model selection, skill discovery and enabled/disabled skill state, context compaction, and goal continuation.
- Closure path: Changes to configured skills appear in the next request. Agent goals continue within the existing tool environment.
- Why this is / is not agent-owned: The inspected paths cover current capabilities, task progress and user configuration. No loop transforms evidenced environmental changes into adoption of a new future capability.
- Evidence: [docs/usage.md](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/docs/usage.md#L62-L66), [docs/usage.md](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/docs/usage.md#L84-L102), [docs/core.md](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/docs/core.md#L55-L73), [internal/coding/host.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/host.go#L464-L487)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Bounded to first-party modes at the frozen revision.

### Absence scope

- Surfaces inspected: Skill registry and overlays, persistent goals, role tools, model changes and session compaction.
- Plausible first-party paths checked: A shipped prospective feedback path that derives and adopts a changed capability from outside evidence.
- Why no material first-party path remains: No such adoption path was found. SDK tool injection requires a host choice and the skills menu selects an existing definition.

## S5 — Policy and identity

- State: —
- Function: No ultimate-policy or identity settlement loop was established.
- Disturbance / variety regulated: Different project instructions, mode permissions and user steering can affect a coding turn.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Static prompt policy, scoped file instructions, plan/agent mode selection and terminal changes.
- Closure path: The model applies the current instruction and mode stack on a subsequent turn.
- Why this is / is not agent-owned: The available owner choices govern work within the assistant's established authority. Workspace constraints and plan toggles do not settle its ultimate identity or authority.
- Evidence: [internal/coding/host.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/coding/host.go#L469-L487), [internal/terminal/commands.go](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/internal/terminal/commands.go#L245-L253), [docs/usage.md](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/docs/usage.md#L46-L52), [pkg/core/prompt/base.md](https://github.com/ClarkQAQ/clara-code/blob/9a9708dcc8828c934fadd22f32e053681a2718b8/pkg/core/prompt/base.md#L85-L95)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Host developers can build policy surfaces outside this installed boundary.

### Absence scope

- Surfaces inspected: Terminal modes, host and project instruction layering, task authorization and provider settings.
- Plausible first-party paths checked: A substantive ultimate-policy issue passed to a legitimate authority and returned to govern the organization.
- Why no material first-party path remains: Observed paths implement existing restrictions or user adjustments to operating mode. They do not provide a policy adjudication loop.

## Recursion

The focal unit is a conversation and its child-session portfolio. Separate terminal conversations and external ACP products are outside this portfolio.

## Variety and escalation

Named tasks and explicit completion signals reduce uncertainty about ownership. Models receive runtime tool refusals and task status. The session owner can pause an objective and later resume it.

## Evidence gaps

No provider-backed sessions were executed. Runtime behavior and boundaries are inferred from the pinned first-party implementation.
