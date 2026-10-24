---
harness_id: laudacode
project_name: Laudacode
repository: https://github.com/Anon4You/Laudacode
review_ref: f8906ce9da3b11c83fca4b296e0a90f5c7d39110
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: A(P)
---

# Laudacode

## Review boundary

- System in focus: one first-party Laudacode terminal coding organization at frozen revision `f8906ce9da3b11c83fca4b296e0a90f5c7d39110`, including the main model/tool loop, built-in coding tools, specialist delegation, permissions/approval policy, managed processes, MCP/LSP adapters, post-edit hooks, session persistence/checkpoints, and durable project `AGENTS.md` instructions where they participate in ordinary supported operation.
- Purpose and identity: perform software-engineering work in a selected workspace through iterative model/tool decisions, optionally delegate independent chunks to fresh specialist agents, inspect and verify changes, and persist project-level instructions for later coding sessions.
- Relevant environment: user task; selected repository/filesystem and git state; shell/process/LSP/test results; web/MCP responses; model-provider output; configured approvals/permissions; specialist results; durable session and `AGENTS.md` state.
- Standard-distribution boundary: the shipped Rust `laudacode` binary, main `Agent`, first-party tools, specialist runtime, permission/process/session machinery, slash-command paths, and project-instruction loading are inside. Model-provider internals, external MCP/LSP servers, network services, host OS and target-project behavior are dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `src/agent.rs`; `src/agents.rs`; `src/tools.rs`; `src/permissions.rs`; `src/processes.rs`; `src/repl.rs`; `src/session.rs`; `src/config.rs`.
- Adjacent first-party surfaces excluded from ownership: repository development tests/CI, release packaging, project-maintainer governance, UI presentation that does not own a control decision, and external server internals reached through MCP/LSP.
- First-party operating / deployment modes considered: interactive TUI/REPL; one-shot `exec`; PLAN/BUILD/FULL AUTO approval modes; single-agent coding; `delegate` fan-out to built-in/custom specialists; `/review`; managed processes; sessions/checkpoints; `/init` and later `AGENTS.md` loading.
- Recursion level: one Laudacode-managed coding task/session is the organization in focus. The main coding agent is an S1 when doing direct repository work; delegated specialists become additional S1 units when they independently perform assigned repository-facing work. The assessment does not infer a higher-recursion metasystem merely from concurrent fan-out.
- Reviewed revision: `f8906ce9da3b11c83fca4b296e0a90f5c7d39110`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Laudacode's main `Agent` builds a project-aware system prompt, submits messages and exposed tool definitions to the configured model, executes returned tool calls under permissions/approval policy, appends tool results, and repeats until the model finishes. Safe independent read calls may run concurrently; writes remain ordered behind their own execution/approval path.

The first-party `delegate` tool lets the main model choose one to four specialist tasks. Each specialist receives a fresh conversation, role-specific system prompt and restricted tool set, then runs its own model/tool loop. The main runtime executes all requested specialists with `join_all` and returns their final reports together as the `delegate` tool result.

That fan-out is intentionally for independent chunks. All specialists receive the same working directory; Laudacode does not expose a first-party worker registry, inter-worker mailbox, worktree isolation, lock/ownership partitioning, or live reassignment surface around a delegate batch. Consequently, concurrency itself does not establish S2, and the blocking fan-out/fan-in call does not provide the main model a live whole-fleet current-control view for S3.

The specialist roster includes a read-only `reviewer` and a `tester`. Laudacode's own main system prompt explicitly recommends “reviewer + tester after coding”. When the main model uses `delegate` this way, the fresh specialist reports return as a tool result into the same main model loop, allowing corrective coding decisions. This is distinct from the user-facing `/review` command, whose report is primarily surfaced to the UI; the S3* classification relies on the model-invoked `delegate` return path.

Laudacode also has a durable project-rule surface. `/init` invokes the main coding agent with an explicit instruction to inspect the repository and synthesize `AGENTS.md` with project overview, build/test commands, code layout and inferred conventions. Later agent construction loads `AGENTS.md` into the system prompt. A project owner can directly edit the same file or append persistent project instructions through `#note`.

## Operational model

For direct coding, the main model receives user/project context, chooses an allowed tool, observes the result, and decides the next action. For delegation, it decides which specialists and self-contained tasks to launch; the runtime runs those specialists concurrently and returns their reports only after the batch completes. The main actor can then use those reports for a later coding/review decision.

Permissions, approvals, budgets, retries, post-edit hooks, managed process lifecycle, undo, checkpoints and session persistence constrain or support this operation. They are not promoted to VSM functions merely because they supervise execution.

## S1 — Operations

- State: A
- Function: perform repository-facing software-engineering work by interpreting the task, inspecting code/environment state, selecting coding tools, applying changes or running commands, observing outcomes and revising subsequent actions.
- Disturbance / variety regulated: heterogeneous repositories, ambiguous requirements, file/git state, command/test/LSP failures, provider/network errors, tool denials, changing workspace state and implementation choices.
- Decisive decision or feedback right: choose what evidence to inspect, which allowed coding/tool action to execute, what edits/commands to attempt, whether to delegate independent chunks, how to respond to returned evidence, and when to finish.
- Decision owner: the model-backed Laudacode main agent; delegated specialists instantiate the same operational decision pattern for their assigned work.
- Supporting / enforcement mechanisms: first-party tool registry; approvals/permissions; retry/backoff; token/cost budgets; post-edit hooks; managed processes; MCP/LSP adapters; undo/checkpoints; session persistence.
- Closure path: task + project context → model chooses a tool/action → Laudacode authorizes and executes it → environment/tool result returns into model context → the model chooses the next coding action or final response.
- Boundary reachability: ordinary `laudacode` and `laudacode exec` paths instantiate the shipped loop directly; no downstream application-authored orchestration is required.
- Why this is / is not agent-owned: without the model-backed actor, Laudacode retains tools and enforcement but no open-ended task-specific coding decision owner.
- Evidence: [`README.md`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/README.md); [`src/agent.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agent.rs); [`src/tools.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/tools.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider inference is a dependency; the assessment credits Laudacode's first-party role/tool/feedback composition, not provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination loop was established.
- Disturbance / variety regulated: concurrent delegated specialists can share one workspace, including mutating specialists, but no concrete first-party interference relation is paired with an attenuation mechanism in the delegate runtime.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: the main model is told to delegate independent chunks; a delegate call caps fan-out at four; role toolsets constrain capabilities; main-agent writes are sequential within its own tool loop.
- Closure path: not applicable; no standard path was found from an identified interaction/oscillation among distinct delegated S1 units through an attenuation relation and back into their subsequent behavior.
- Why this is / is not agent-owned: selecting ostensibly independent tasks and gathering reports is delegation/fan-out, not a demonstrated S2-specific regulation of mutual interference.
- Evidence: [`src/agents.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agents.rs); [`src/agent.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agent.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the model may avoid collisions by task design, but Methodology 0.3.6 requires the concrete inter-S1 disturbance and attenuation/feedback relation rather than generic decomposition.

### Absence scope

- Surfaces inspected: `delegate` schema/parser/executor; specialist role/tool restrictions; concurrent `join_all` execution; main tool batching; managed processes; approvals/permissions; session state.
- Plausible first-party paths checked: “independent chunks” prompt guidance as S2; fan-out cap as coordination; role tool restrictions; serialization of main-agent writes; implicit shared-workspace coordination among delegated coders.
- Why no material first-party path remains: delegate specialists receive the same cwd and run independently; no worker ownership map, shared conflict detector, cross-worker message loop, worktree isolation, integration/merge arbitration or returned attenuation feedback was found.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control loop was established above the delegated S1 population.
- Disturbance / variety regulated: the main agent can choose a delegate batch and later receive reports, but it does not receive live worker status/commitment/resource state or intervene in an in-flight batch.
- Decisive decision or feedback right: none established at S3 level.
- Decision owner: none established.
- Supporting / enforcement mechanisms: model-selected specialist/tasks; maximum four delegates; blocking `join_all`; aggregate token/cost accounting; global cancellation/approval; managed process controls.
- Closure path: not applicable; the main agent launches a batch and regains control after fan-in, rather than receiving a live whole-system current view and exercising current resource/priority/commitment decisions over active S1s.
- Why this is / is not agent-owned: pre-dispatch delegation and post-completion replanning remain S1/orchestration behavior without the required current-control function.
- Evidence: [`src/agents.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agents.rs); [`src/agent.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agent.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the main model can start a later wave after reports arrive, but no live current-management surface over the in-flight worker population was found.

### Absence scope

- Surfaces inspected: delegate executor and result aggregation; specialist runtime; budget accounting; cancellation; process manager; plan/todo state; session persistence.
- Plausible first-party paths checked: main agent as coordinator merely because it invokes `delegate`; batch fan-in as whole-system view; token/cost accounting as resource management; global cancel as S3; `update_plan` as organization-wide current control.
- Why no material first-party path remains: no worker registry, live worker status view, reassignment/prioritization/message path, per-worker cancellation or adaptive in-flight resource allocation exists in the reviewed delegate composition. Plan/todo and budgets govern the main task/session rather than a live S1 organization.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation quality/correctness and return audit findings to the main coding actor for corrective action.
- Disturbance / variety regulated: bugs, unsafe assumptions, style/edge-case defects, missing verification and test/build failures that an implementing S1 may overlook.
- Decisive decision or feedback right: a separately instantiated reviewer/tester specialist makes the audit judgment over workspace evidence; the main agent decides subsequent corrective work using that returned judgment.
- Decision owner: the fresh model-backed `reviewer` and/or `tester` specialist invoked through the main model's `delegate` tool.
- Claim being audited: that the implementation/current code is correct and sufficiently verified after coding.
- Ordinary reporting path: the implementing main/coder S1 reports its own tool outcomes and completion through its coding conversation.
- Complementary access path: `delegate` can launch a fresh read-only `reviewer` over current files and a separate `tester` with build/test command access; each runs its own conversation and restricted tool loop.
- Independence boundary: reviewer/tester agents have fresh message histories, role-specific system prompts and restricted tool sets, separate from the implementing S1's conversation; the reviewer is structurally read-only.
- Who acts on findings: `execute_delegate` returns specialist reports as the main agent's tool result; the main model then receives those findings in its ordinary loop and can edit, test, or delegate corrective work.
- Boundary reachability: `delegate`, built-in reviewer/tester roles and the independent sub-agent loop are exposed by the standard first-party agent tool surface; the main system prompt explicitly recommends “reviewer + tester after coding”.
- Supporting / enforcement mechanisms: specialist tool allowlists; read-only reviewer flag; separate `MAX_SUB_ROUNDS`; shared permission boundary; concurrent delegate execution; post-edit hooks as additional deterministic evidence.
- Closure path: implementation exists → main model delegates review/test → fresh reviewer/tester directly inspect/run evidence → reports return as the `delegate` tool result → main model receives findings and chooses corrective work or accepts clean results.
- Why this is / is not agent-owned: deterministic hooks can add evidence, but the credited complementary judgment is made by a distinct model-backed specialist. Removing that specialist leaves only self-checks/hooks and removes the independent semantic audit judgment.
- Evidence: [`src/agents.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agents.rs); [`src/agent.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agent.rs); [`src/repl.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/repl.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the user-facing `/review` path by itself surfaces a report to the UI rather than automatically feeding it into the main agent; the positive closure relies on the model-invoked `delegate` reviewer/tester path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop was established.
- Disturbance / variety regulated: web/MCP research, session history, conversation compaction, skills, provider/model selection and persisted project notes can inform present work but do not operationalize future environmental intelligence into persistent organizational adaptation.
- Decisive decision or feedback right: none established for prospective capability/strategy adaptation.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `web_search`/`fetch_url`; skills; sessions/checkpoints; compaction; custom commands; provider/model configuration; `AGENTS.md` project instructions.
- Closure path: no external/future distinction → adaptation option → persistent capability/strategy change → later operational return loop was found.
- Why this is / is not agent-owned: current-task research and durable context can improve present execution without constituting S4.
- Evidence: [`README.md`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/README.md); [`src/agent.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agent.rs); [`src/session.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/session.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: `AGENTS.md` is credited under S5 for durable project policy, not S4; persistence alone is not prospective adaptation.

### Absence scope

- Surfaces inspected: web/MCP tools; skills/custom commands; session persistence/checkpoints; compaction; provider/model switching; AGENTS/project memory; retry/network adaptation.
- Plausible first-party paths checked: web research as environmental scan; provider/model changes as adaptation; session memory/compaction as learning; `#note` as self-learning; skills as evolving capability; retry/backoff as adaptation.
- Why no material first-party path remains: inspected mechanisms either serve the current task, preserve context, apply externally authored capabilities/configuration, or handle transient execution failure. None closes a prospective intelligence-to-organizational-adaptation loop.

## S5 — Policy and identity

- State: A(P)
- Function: establish and preserve the durable project-level standing instructions that define how later Laudacode coding work understands the project, its build/test expectations, code layout and conventions.
- Disturbance / variety regulated: missing/stale project guidance, inconsistent future-agent assumptions, loss of durable project conventions and divergence in standing build/test/working expectations across sessions.
- Decisive decision or feedback right: decide the semantic content of the project `AGENTS.md` layer that later Laudacode agent construction loads into the system prompt.
- Decision owner: Base (`A`) mode — the model-backed main agent invoked by `/init` inspects repository evidence and chooses the synthesized project overview, commands, layout and conventions. Parent (`P`) mode — the legitimate project owner can directly review/edit the same authoritative file or append standing project instructions through `#note`.
- Identity / ultimate-policy issue: what durable project-level rules, conventions and working expectations should govern later Laudacode coding behavior at this project recursion.
- Ultimate authority in each claimed mode: Base (`A`) — the model-backed `/init` run owns semantic synthesis of the initial `AGENTS.md` within existing higher-level Laudacode/user constraints; Parent (`P`) — the legitimate project owner/editor owns direct changes to that same project-instruction layer.
- Return-to-operation path: `AGENTS.md` persists in the project; subsequent `Agent::build_system_prompt` calls load it and inject its content into the main system prompt before later coding turns, changing the standing instructions under which the agent operates.
- Supporting / enforcement mechanisms: repository exploration through ordinary read/search tools; model-authored file write during `/init`; direct owner edits/`#note`; persistent filesystem; `load_agents_md` in system-prompt construction.
- Closure path: project instruction gap/change → model-driven `/init` synthesis or legitimate owner edit → `AGENTS.md` persists → later Laudacode construction loads the file into system prompt → subsequent coding work is governed by the returned standing layer.
- Boundary reachability: `/init` and `#note` are shipped first-party user surfaces; `/init` directly invokes the standard main agent loop, and the same shipped `Agent::build_system_prompt` path loads `AGENTS.md` for later ordinary sessions.
- Why this is / is not agent-owned: invoking `/init` is a trigger, but the model decides the exact project-rule content from repository evidence; removing the model leaves only the offline stub and external editing. In parent mode the project owner directly chooses the authoritative edit.
- Evidence: [`src/repl.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/repl.rs); [`src/agent.rs`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/src/agent.rs); [`README.md`](https://github.com/Anon4You/Laudacode/blob/f8906ce9da3b11c83fca4b296e0a90f5c7d39110/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is project-recursion S5. It does not claim Laudacode's model can rewrite higher-level application safety rules, permission semantics or user authority.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | model-backed main agent | user invokes shipped `/init` when `AGENTS.md` is absent | inspect project → synthesize durable project instructions → write `AGENTS.md` → later agent construction loads it into system prompt | `src/repl.rs`, `src/agent.rs` |
| Parent (`P`) | legitimate project owner/editor | direct edit/review or `#note` | owner changes durable project instructions → file persists → later agent construction reloads it → subsequent work follows changed standing instructions | `src/repl.rs`, `src/agent.rs` |

## Distributed OSS parent arrangement

The open-source project maintainers govern Laudacode itself outside the assessed running session. The parent mode credited here is narrower: the legitimate target-project owner governs the durable project `AGENTS.md` instruction layer that the running harness loads.

## Self-hosted and non-human modes

Direct coding, delegated review/test and `/init` project-rule synthesis can execute through model decisions after the user supplies the task/trigger and configured authority. Approvals can restrict individual effects but are not themselves promoted to S3/S5. The explicit parent mode is limited to direct ownership of the project `AGENTS.md` layer.

## Recursion

At the chosen recursion, the main coding actor and independently executing delegated specialists are S1 units when they perform repository-facing work. The delegate fan-out does not add S2/S3 without the corresponding interference/current-control loops. Reviewer/tester specialists are complementary S3* actors when invoked to challenge completed implementation. The project `AGENTS.md` instruction layer supplies S5 at the same project recursion.

## Variety and escalation

Open-ended coding variety is absorbed by S1 model/tool loops. Tool permissions, approvals, budgets, network retries, hooks and process limits attenuate execution variety. Delegate batches return specialist reports to the main actor after completion; no live fleet-control escalation path is inferred. Audit findings from delegated reviewers/testers return to the main agent for corrective coding. Project-level standing-rule changes persist through `AGENTS.md` and are returned to later sessions.

## Evidence gaps

No evidence gap requires `?` for the published vector. The main semantic boundary is deliberate: concurrent delegation is not credited as S2/S3 merely because several agents run, and the S5 claim is limited to durable project-recursion `AGENTS.md` policy rather than higher-level Laudacode product identity.

## Assessment summary

Laudacode closes autonomous coding S1, autonomous complementary S3* through fresh reviewer/tester specialists whose reports return to the main model loop, and autonomous-plus-parent S5 through model-synthesized or owner-edited durable `AGENTS.md` instructions loaded into later system prompts. Its concurrent delegation lacks concrete S2 interference attenuation and live S3 fleet control, while current-task research/persistence does not establish S4.

Proposed vector: **`A · — · — · A · — · A(P)`**.
