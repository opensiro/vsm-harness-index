---
harness_id: ante
project_name: Ante
repository: https://github.com/AntigmaLabs/ante
review_ref: 74ce24554341fb0c6cc3521baa5da5b94cedf881
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
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# Ante

## Review boundary

- System in focus: one Ante coding-agent organization at frozen revision `74ce24554341fb0c6cc3521baa5da5b94cedf881`, including the root model/tool loop, first-party subagent machinery, goal-driven session control, persistent auto-memory and documented first-party extension surfaces.
- Purpose and identity: perform autonomous tool-backed software-engineering work in a user-selected project while supporting bounded delegation, persistence, evaluation and reusable adaptation across sessions.
- Relevant environment: user requests and corrections, project files and repositories, shell/tool results, external model providers or local inference, first-party subagents, optional terminal agents, MCP/tools and operator policy/configuration.
- Standard-distribution boundary: the shipped Ante binary behavior documented at the pinned revision plus public first-party protocol/configuration/documentation and repository-shipped curated components. External model providers, llama.cpp, MCP servers, Claude Code/Codex terminal processes and Harbor remain dependencies or adjacent systems rather than inherited VSM owners.
- Credited operating / distribution surfaces: root Ante session/turn/tool loop; built-in `Agent` subagents; `max_concurrent_subagents`; `/goal`; auto-memory; documented skill installation/discovery; repository-shipped `curated/skills/simplify` as a function-specific constructor surface.
- Adjacent first-party surfaces excluded from ownership: Terminal-Bench/Harbor evaluation and benchmark development; repository development/release activity; future target architecture in the experimental agent-organization docs; external interactive terminal agents. These may corroborate design but do not own functions in the assessed runtime unless explicitly credited below.
- First-party operating / deployment modes considered: interactive TUI; headless execution; server mode; goal-driven sessions; built-in subagent delegation; persistent auto-memory; installed first-party curated skills; user/project settings and permission modes.
- Recursion level: one root Ante work organization. Built-in subagents count as additional S1 units only when they execute real delegated work inside the root organization; external `/term` programs remain environment unless separately assessed.
- Reviewed revision: `74ce24554341fb0c6cc3521baa5da5b94cedf881`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Ante presents a session-oriented autonomous coding loop through TUI, headless and server clients. The daemon/session runtime repeatedly sends model context, executes first-party tools, returns observations and continues until the running model finishes or the surrounding control mode stops the session. Built-in tools include file operations, shell execution, web access where supported and an `Agent` tool that launches isolated delegated subagents with their own context and optional model override.

Subagents are one level deep and return their result to the parent. Ante also exposes `max_concurrent_subagents`: when concurrent child calls exceed the configured cap, excess calls wait for a slot before opening a model stream. The documentation explicitly recommends a cap of one when a local model can handle only one request at a time, tying this mechanism to a concrete shared-capacity disturbance rather than generic message passing.

A separate goal-driven mode adds a current-control loop around ordinary operation. After each turn a goal evaluator judges the whole conversation against the active success condition. A `continue` judgment returns evaluator feedback into another agent turn; `met` or `unreachable` closes the current commitment. A deterministic iteration cap remains a safety backstop rather than the owner of the substantive continue/stop judgment.

Ante also carries persistent per-project auto-memory. The agent consults existing memory, records useful lessons and corrections, and updates or removes stale memories. `MEMORY.md` and typed topic files are then injected into future sessions, so selected distinctions from prior user/project experience can alter later operating behavior.

The repository ships a `curated/skills/simplify` package that defines a complementary review organization: multiple independent subagents inspect the same change through different lenses, are instructed not to edit, return findings, and the parent validates/deduplicates those findings before applying improvements. This is a real first-party S3* construction path, but it is not resident by default; the user must install/equip the curated skill through Ante's skill mechanism.

## Operational model

The root model owns ordinary substantive action selection: it interprets the task, chooses tools and delegated work, incorporates returned observations and decides when the operational task is complete. Runtime permission checks, tool filtering, transport, context management and persistence constrain or support those choices without becoming the owner of the underlying operational judgment.

When built-in subagents are used, the root can create multiple real work units. Ante supplies a concrete shared-capacity coordination relation through the concurrency cap and waiting queue, but the decisive cap is selected through user/project configuration rather than by an autonomous coordination actor. In contrast, `/goal` supplies a model-owned whole-session performance-regulation loop and is therefore credited as autonomous S3.

## Primary evidence

- [`docs-site/docs/reference/architecture.mdx`](https://github.com/AntigmaLabs/ante/blob/74ce24554341fb0c6cc3521baa5da5b94cedf881/docs-site/docs/reference/architecture.mdx) — client/daemon/session loop, tools and agent-centric direction.
- [`docs-site/docs/extend/subagents.mdx`](https://github.com/AntigmaLabs/ante/blob/74ce24554341fb0c6cc3521baa5da5b94cedf881/docs-site/docs/extend/subagents.mdx) — built-in/custom subagents, delegation ownership and concurrency cap.
- [`docs-site/docs/usage/goal-sessions.mdx`](https://github.com/AntigmaLabs/ante/blob/74ce24554341fb0c6cc3521baa5da5b94cedf881/docs-site/docs/usage/goal-sessions.mdx) — goal evaluator, continuation feedback and termination judgments.
- [`docs-site/docs/extend/memory.mdx`](https://github.com/AntigmaLabs/ante/blob/74ce24554341fb0c6cc3521baa5da5b94cedf881/docs-site/docs/extend/memory.mdx) — persistent auto-memory and future-session loading.
- [`curated/skills/simplify/SKILL.md`](https://github.com/AntigmaLabs/ante/blob/74ce24554341fb0c6cc3521baa5da5b94cedf881/curated/skills/simplify/SKILL.md) — independent complementary reviewers and returned findings.
- [`docs-site/docs/configuration/preference.mdx`](https://github.com/AntigmaLabs/ante/blob/74ce24554341fb0c6cc3521baa5da5b94cedf881/docs-site/docs/configuration/preference.mdx) and [`docs-site/docs/configuration/permission.mdx`](https://github.com/AntigmaLabs/ante/blob/74ce24554341fb0c6cc3521baa5da5b94cedf881/docs-site/docs/configuration/permission.mdx) — operator configuration/policy boundary.

## S1 — Operations

- State: A
- Function: autonomously perform user-directed software-engineering work through a repeated model/tool feedback loop.
- Disturbance / variety regulated: heterogeneous coding requests, repository state, file/shell/tool observations, execution failures, model/context limits and delegated-work results.
- Decisive decision or feedback right: choose substantive next actions/tools/delegation and decide when enough operational evidence exists to return a result.
- Decision owner: the running root model agent.
- Supporting / enforcement mechanisms: daemon/session turn lifecycle, tool implementations, permission engine, provider transport, persistence, compaction and external/local inference hosts.
- Closure path: user task → model decision → first-party tool/delegation execution → returned observation → subsequent model decision → completed task/result.
- Boundary reachability: the shipped Ante TUI/headless/server paths instantiate this model/tool loop directly; no downstream harness composition is required.
- Why this is / is not agent-owned: deterministic runtime mechanisms execute and constrain actions, but the model owns the substantive selection of what to do next and whether the task is operationally complete.
- Evidence: `docs-site/docs/reference/architecture.mdx`, `docs-site/docs/reference/tools-reference.mdx`, README headless/TUI usage.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference may be external or local; ownership is credited to the model actor operating through Ante's first-party loop, not to the provider.

## S2 — Coordination

- State: C
- Function: attenuate contention among concurrently delegated Ante work units for bounded shared inference capacity.
- Disturbance / variety regulated: multiple child agents attempting concurrent model work when the selected local/model-serving environment can only process a smaller number of requests without queueing/timeouts.
- Decisive decision or feedback right: determine how much concurrent subagent work the session may admit before excess work waits.
- Decision owner: constructor/operator configuration; Ante supplies the function-specific concurrency mechanism but no autonomous agent owns or revises the cap in the documented standard mode.
- Supporting / enforcement mechanisms: `max_concurrent_subagents`, waiting-for-slot queueing and parent interruption/cancellation behavior.
- Closure path: parallel child calls → cap check → excess child waits → slot becomes available → queued child starts; later S1 execution therefore changes according to the coordination result.
- Boundary reachability: the cap is a documented built-in session setting applied directly to built-in `Agent` calls in ordinary Ante execution.
- Why this is / is not agent-owned: the root chooses which subagents to delegate to, but the specific collision-attenuation policy is selected through settings and enforced by the runtime; an autonomous S2 decision owner is not supplied.
- Evidence: `docs-site/docs/extend/subagents.mdx`, `docs-site/docs/configuration/preference.mdx`, `docs-site/docs/reference/tools-reference.mdx`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic delegation is not credited as S2; only the documented shared-capacity interference and cap/queue relation are used.
- Distinct S1 units: the root organization can launch multiple built-in/custom subagents that independently execute real delegated tasks with their own model context and tool set.
- Inter-S1 disturbance: child model requests can exceed the usable concurrent capacity of the selected inference environment; the docs specifically call out a local model that handles one request at a time.
- Attenuating coordination relation: `max_concurrent_subagents` limits admitted parallel children and queues excess calls until a slot opens.
- Feedback into subsequent S1 behaviour: queued child work does not begin until capacity becomes available, preventing the competing S1 requests from simultaneously consuming the bounded model-serving channel.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is explicitly tied to regulating a concrete concurrency/capacity interference among multiple operational child units, not to the existence of the `Agent` handoff itself.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current session's continuing commitment against a declared success condition and intervene when progress is insufficient or the goal is no longer reachable.
- Disturbance / variety regulated: incomplete work, premature completion, current-turn outcomes that do not yet satisfy the session goal, and situations where the active commitment has become unreachable.
- Decisive decision or feedback right: after each turn, judge whether the whole-session goal is met, unreachable or requires another regulated continuation with corrective feedback.
- Decision owner: the model-based goal evaluator in the first-party `/goal` mode.
- Supporting / enforcement mechanisms: goal-session protocol state, deterministic continuation plumbing, session persistence and iteration cap.
- Closure path: current conversation + goal → evaluator judgment → `continue` returns evaluator feedback into another operational turn, while `met`/`unreachable` terminates the commitment.
- Boundary reachability: `/goal` is a shipped first-party TUI/protocol capability and can be used directly without a downstream controller.
- Why this is / is not agent-owned: the iteration cap is only a backstop; the substantive assessment of current performance and continue/stop state is made by the evaluator model and its feedback changes subsequent work.
- Evidence: `docs-site/docs/usage/goal-sessions.mdx`, protocol documentation and changelog entries for goal evaluation.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary one-turn execution alone would not establish S3; this state is credited from the supported goal-driven mode.
- Whole-system current view: the goal evaluator receives the active success condition and evaluates the conversation after each completed turn rather than judging one isolated tool call.
- Current-control decision scope: continue the current commitment with corrective feedback, or end it as met/unreachable; this regulates current performance/accountability for the session as a whole.

## S3* — Complementary audit

- State: C
- Function: independently challenge changed-code quality claims through multiple review lenses and return complementary findings for corrective action.
- Disturbance / variety regulated: duplication, unnecessary complexity, avoidable inefficiency and misplaced abstraction that can survive the ordinary implementation/check path.
- Decisive decision or feedback right: each independent reviewer judges the same scoped changes under a distinct audit lens and returns supported findings without editing the work being audited.
- Decision owner: constructor path; first-party curated `simplify` supplies the audit organization and reviewer contracts, but the standard Ante installation does not equip/invoke this lane automatically.
- Supporting / enforcement mechanisms: skill discovery/equipping, parallel subagent calls, shared review scope, prohibition on reviewer edits, parent deduplication/validation and subsequent normal tool execution.
- Closure path: implementation/diff → independent reviewer findings → parent validates/deduplicates → worthwhile corrections are applied and verified.
- Boundary reachability: the skill is shipped in the public Ante repository and is installable through the documented first-party skill mechanism; it is therefore a concrete first-party constructor surface, not a hypothetical downstream design.
- Why this is / is not agent-owned: reviewer judgments are agentic, but obtaining this S3* organization still requires the operator/developer to install/equip the curated skill; Ante does not supply it as a resident standard audit owner.
- Evidence: `curated/skills/simplify/SKILL.md`, `curated/README.md`, `docs-site/docs/extend/skills.mdx`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary tests, `/diff`, logs and root self-review are not credited; only the separate reviewer construction path supports `C`.
- Claim being audited: that the current changed code is sufficiently reusable, simple, efficient and well-abstracted for the requested cleanup scope.
- Ordinary reporting path: the root agent implements/inspects the task and runs its ordinary checks.
- Complementary access path: independent subagents receive the same diff/scope under separate reuse, simplification, efficiency and abstraction lenses and return findings without modifying files.
- Independence boundary: reviewer contexts are separate subagents and are prohibited from editing; the parent receives their findings only after each independent judgment is made.
- Who acts on findings: the parent agent validates and deduplicates findings, applies worthwhile improvements and runs verification.

## S4 — Outside-and-then intelligence

- State: A
- Function: learn reusable distinctions from user/project experience and convert them into persistent guidance that changes later sessions.
- Disturbance / variety regulated: recurring user corrections, confirmations, project constraints, learned working patterns and memories that become stale or wrong over time.
- Decisive decision or feedback right: decide which observed lessons should be recorded, updated or removed as persistent project memory for future work.
- Decision owner: the running Ante agent under the first-party auto-memory behavior.
- Supporting / enforcement mechanisms: per-project memory directory, typed memory format, `MEMORY.md` cap, session-start memory injection and Write/Edit tools.
- Closure path: current user/project interaction → agent identifies reusable lesson → memory is created/updated/removed → future session injects the retained memory into the system prompt → later operational choices change.
- Boundary reachability: auto-memory is a documented built-in Ante capability enabled by default in interactive TUI sessions and optionally in headless mode.
- Why this is / is not agent-owned: the user supplies environmental feedback, but the agent is explicitly taught to consult, record, revise and discard persistent memories; the runtime only stores and reloads the selected adaptation.
- Evidence: `docs-site/docs/extend/memory.mdx`, preference/headless documentation.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: session transcript persistence alone is not credited; the witness is the agent-selected conversion of experience into reusable future-session guidance.
- External distinction: corrections, confirmations and project-specific guidance arrive from the user/project environment rather than from an internal fixed task plan alone.
- Future / prospective distinction: the agent evaluates whether a lesson should guide later conversations and can remove or update it when no longer valid.
- Adaptation option generated: persist or revise a concise typed memory/rule describing how future work should be handled.
- Path back into current capability / S3: retained memories are automatically injected into later session prompts, changing the options and constraints available to subsequent S1 work and goal-regulated sessions.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy adjudication loop is established at the selected Ante boundary.
- Disturbance / variety regulated: operator-defined prompts, permissions, profiles and project settings constrain behavior, but no specific identity/ultimate-policy conflict or proposal is routed through an S5 closure.
- Decisive decision or feedback right: no material first-party identity/ultimate-policy decision path with complete issue → legitimate authority → authoritative decision → returned governance was established.
- Decision owner: none established for qualifying S5.
- Supporting / enforcement mechanisms: user `system_prompt`/`append_system_prompt`, permission modes/rules, profiles, project settings and generic `AskUser` questions.
- Closure path: configuration is loaded into sessions and generic questions can return user input, but no function-specific S5 issue-and-return path is established.
- Why this is / is not agent-owned: parent/operator authority over configuration is real, but Methodology 0.3.5 does not treat editable policy text, permission gates or generic human input as S5 by themselves.
- Evidence: `docs-site/docs/configuration/preference.mdx`, `docs-site/docs/configuration/permission.mdx`, protocol/AskUser documentation.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a wider organization embedding Ante may provide S5, but that authority is outside this standalone harness boundary.

### Absence scope

- Surfaces inspected: system-prompt settings, named/project profiles, permission modes and persistent rules, `AskUser`, session protocol, goal sessions, memory and agent-organization documentation.
- Plausible first-party paths checked: user-owned prompt replacement, project prompt append/narrowing, permission changes, structured questions, goal declaration and persistent memory guidance.
- Why no material first-party path remains: these surfaces configure or constrain operation and can request ordinary task clarification, but the reviewed evidence does not establish an identity/ultimate-policy issue being escalated to legitimate authority and returned as an authoritative S5 decision governing subsequent operation.

## Distributed OSS parent arrangement

The AntigmaLabs repository and contributor/release process are adjacent to the assessed runtime. Maintainers may define shipped defaults and users may configure local installations, but repository governance is not imported as product-runtime S5. No organization-level parent mode is published from contributor or release activity.

## Self-hosted and non-human modes

Ante can run with hosted or local models and can be operator-governed through prompts, permissions and profiles. Those operator controls constrain S1 and surrounding runtime behavior, but no additional S3/S4/S5 parent modifier is claimed unless the function-specific parent loop is separately evidenced.

## Recursion

Built-in subagents have isolated contexts and real delegated operational work, but delegation is one level deep and child agents do not receive the `Agent` tool. External `/term` sessions can be persistent and nested through other CLIs, but they are not automatically part of the assessed first-party Ante organization. The pinned evidence therefore does not establish a recursively viable Ante unit merely from spawning/nesting.

## Variety and escalation

Ante attenuates operational variety through tool filtering, permission modes, context compaction and bounded subagent concurrency while retaining model discretion over substantive work. Root agents can delegate search/research when their own short-path capability is insufficient; unattended child calls deny actions requiring approval rather than blocking on an unavailable human. Goal sessions provide a separate escalation/continuation signal when current work has not yet satisfied the declared success condition.

## Evidence gaps

The main unresolved positive gap is autonomous S2 ownership: Ante supplies a concrete collision-specific coordination mechanism, but the concurrency policy remains configured rather than autonomously revised. S3* is also constructor rather than resident because the strongest complementary review lane is supplied as an installable curated skill. No qualifying S5 closure was found. Experimental future agent-centric architecture is not used to upgrade current states.
