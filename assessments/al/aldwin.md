---
harness_id: aldwin
project_name: Aldwin
repository: https://github.com/hvess/aldwin-agent
review_ref: f6a17306688e75f5d206df8bcdb421b075d859c9
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Aldwin

## Review boundary

- System in focus: Aldwin's first-party released coding-agent product at frozen revision `f6a17306688e75f5d206df8bcdb421b075d859c9`: `aldwin-core` agent loop and event/log state, first-party LLM adapters, `aldwin-tools` built-ins/staging/sandbox/MCP bridge, configuration/session persistence and the CLI/TUI composition that executes them.
- Purpose and identity: help a developer understand and deliberately shape code while an autonomous coding actor performs repository inspection, command execution, planning and edit proposal. Staged edits are deliberately held for developer review before Aldwin writes them.
- Relevant environment: developer requests and review comments, current workspace/source state, shell/build/test results, model-provider responses, language-server responses, configured MCP tools, session history and developer approval/discard choices.
- Standard-distribution boundary: the released Aldwin binary/product composition is inside. Model providers, language servers and MCP servers are dependencies. Repository-development dogfood machinery (`crates/review`, `.agents/skills/*`, `.githooks/` and CI/release workflows) is adjacent development infrastructure and cannot donate organizational functions to the released runtime.
- Credited operating / distribution surfaces: `README.md`; `docs/spec/aldwin.md`; accepted runtime ADRs including `docs/adr/0009-the-review-is-the-only-gate.md`; `crates/core/src/agent.rs`; released core/tool/config/TUI/CLI composition and session/resume surfaces.
- Adjacent first-party surfaces excluded from ownership: the dev-only `aldwin-review` crate, its ten-stage repository submission loop, blind subagent judges, agent-development review skill, git hooks, CI/release processes, contributor governance and screenshots/baselines used to develop Aldwin. `docs/spec/aldwin.md` explicitly says `aldwin-review` is dev-only and never in a release build.
- First-party operating / deployment modes considered: ordinary terminal session/TUI, persisted session resume, built-in provider and OpenAI-compatible provider modes, built-in tools plus configured MCP extension, staging/review approval-comment-discard paths, sandboxed `run`/language-server/MCP process execution.
- Recursion level: one Aldwin user session and its model/tool coding loop is the assessed organization. Built-in tool calls, concurrently dispatched calls, staged edits, plan entries and external MCP tools are capabilities/actions of that S1 rather than distinct first-party S1 operational units. Separate sessions are not composed into one multi-S1 organization.
- Reviewed revision: `f6a17306688e75f5d206df8bcdb421b075d859c9`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Aldwin's core owns one conversation loop per session. A submitted user message starts a turn; each step streams a model response, records text/thinking/tool calls, dispatches requested tools, appends tool results to the live message context and repeats until the model ends the turn, cancellation/error occurs, or the dispatcher's turn-ending hook finishes. Session records are append-oriented and can be restored with `/resume`.

The shipped tool layer includes read, run, edit, explain, plan and ask, plus configured MCP extensions. Tool calls from one model step can be dispatched concurrently, but they remain actions selected by the same model-backed S1. Aldwin's own `edit` does not mutate the filesystem directly: it writes to an in-memory staged overlay. Before a later run/MCP call would observe staged code, or when the turn would end, the dispatcher opens the review. Developer approval writes the staged changes; comments prevent the pending step/turn from proceeding and are returned to the model as corrective input; discard drops the changes.

That review is a deliberate human-in-the-loop operational gate. It is routine, mandatory for the staged-edit path and integrated into the normal S1 execution cycle. It is therefore not credited as S3*: it does not provide sporadic complementary access outside routine production reporting. The separate repository-development `aldwin-review` machinery does contain deterministic checks and blind subagent judges, but it is explicitly dev-only and never part of a release build, so Methodology 0.3.6 boundary reachability excludes it from product ownership.

Reads and `run` calls do not require human grants under the accepted runtime policy. `run` executes in the workspace sandbox and may write within the permitted workspace; the product documentation explicitly warns that a command such as `rm` can still mutate the project. Deny locks, sandboxing and the edit-review mechanism constrain execution but do not choose the model actor's open-ended coding plan.

Primary evidence:

- [`README.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/README.md)
- [`docs/spec/aldwin.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/spec/aldwin.md)
- [`docs/adr/0009-the-review-is-the-only-gate.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/adr/0009-the-review-is-the-only-gate.md)
- [`crates/core/src/agent.rs`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/crates/core/src/agent.rs)
- [`docs/spec/aldwin-review.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/spec/aldwin-review.md) — boundary evidence for the excluded dev-only review system.

## Operational model

The developer supplies intent; the model-backed actor decides what to inspect, what tools/commands to call, what changes to stage and how to respond to tool results. Core dispatch returns operational evidence to the same actor and the loop continues autonomously. The developer can interrupt the turn and is the final authorizer for staged `edit` changes; review comments create an automatic follow-up turn so the model can revise the proposal.

This gives Aldwin a hybrid human-constrained S1 rather than a human-operated shell. The model owns the open-ended coding judgment and autonomous tool/action sequence, while deterministic sandbox/deny mechanisms and the mandatory staged-edit review constrain specific effects. The standard distribution does not add independent operational workers or a runtime metasystem beyond that loop.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work by interpreting developer intent, inspecting the project, planning, running commands, proposing/staging code changes, reacting to results/review feedback and iterating until the turn's coding objective is resolved or stopped.
- Disturbance / variety regulated: heterogeneous source state, build/test results, language-server evidence, shell output, implementation choices, stale/changed files, tool failures, developer questions and review feedback encountered during coding.
- Decisive decision or feedback right: choose the task-specific sequence of reads, commands, explanations, plans, questions and proposed code changes and revise those choices from returned tool/review evidence.
- Decision owner: the model-backed Aldwin coding actor.
- Supporting / enforcement mechanisms: core event/log loop; concurrent tool dispatcher; staged changeset; sandbox/workspace boundary; deny locks; developer edit-review gate; cancellation; session persistence; provider/MCP adapters.
- Closure path: developer request/current history → model reasoning/tool choices → first-party dispatch → repository/process/tool results and, when relevant, review decision/comments → results/follow-up enter the same model actor's next step/turn → revised action or turn completion.
- Boundary reachability: ordinary released Aldwin sessions directly instantiate this loop. The S1 claim does not depend on the dev-only repository review harness.
- Why this is / is not agent-owned: removing the model actor while retaining review UI, sandbox, staging and tools leaves no open-ended coding judgment to construct or sequence task-specific work. The developer's mandatory review constrains staged edits but does not supply the model's autonomous planning/tool-use loop; `run` is also an autonomous first-party action path within the sandbox.
- Evidence: [`crates/core/src/agent.rs`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/crates/core/src/agent.rs); [`README.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/README.md); [`docs/adr/0009-the-review-is-the-only-gate.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/adr/0009-the-review-is-the-only-gate.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Aldwin intentionally gives the developer decisive approval over the staged-edit write path and is not intended for unattended ticket throughput. This constrains S1 authority but does not eliminate the autonomous operational model/tool loop present in the standard distribution.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established at S2 level because the released product contains one model-backed coding S1, not several distinct operational units whose interaction creates a specific interference/oscillation problem.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: multiple tool calls may be dispatched concurrently through `join_all`, but those are actions of one S1. Staging serializes one turn's edits, and review ordering keeps staged state coherent, but neither is coordination among independent S1 units.
- Closure path: not applicable; no distinct-S1 disturbance → attenuation → changed S1 behavior witness exists in the supported distribution.
- Why this is / is not agent-owned: the product documentation explicitly states there are no background or parallel agents. MCP servers are external tools and do not become S1 units merely because Aldwin can call them.
- Evidence: [`README.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/README.md); [`crates/core/src/agent.rs`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/crates/core/src/agent.rs); [`docs/spec/aldwin.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/spec/aldwin.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: concurrent tool futures and external MCP processes provide implementation concurrency without establishing multiple first-party operational units.

### Absence scope

- Surfaces inspected: core session/turn/step loop; concurrent tool dispatch; tool/staging/review architecture; MCP extension boundary; product capability statement; session persistence.
- Plausible first-party paths checked: parallel/background agents; subagent/delegation API; concurrent tool calls as possible units; MCP servers as possible units; multiple sessions; review/comment role separation.
- Why no material first-party path remains: all standard task actions originate from one coding actor, while external tools and multiple sessions are not composed into a first-party multi-S1 organization. No S2-specific interference/attenuation/feedback relation is supplied.

## S3 — Inside-and-now control

- State: —
- Function: no material separate whole-current organizational control function was established in the released product.
- Disturbance / variety regulated: not established at S3 ownership level.
- Decisive decision or feedback right: not established. The plan tool, cancellation, sandbox/deny constraints, staged review timing and developer edit comments regulate one current coding operation rather than resources, commitments or priorities across several S1 units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: plan tool; command channel/cancellation; workspace sandbox; deny locks; review gate; session state; dispatcher lifecycle.
- Closure path: not applicable; no whole-system current view → substantive organization-wide resource/priority/commitment decision → return-to-operations loop was found.
- Why this is / is not agent-owned: the model's plan is task decomposition/self-management within S1. Human review of a concrete staged changeset is a local operational correction, not management on behalf of the whole at a higher recursion.
- Evidence: [`docs/spec/aldwin.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/spec/aldwin.md); [`docs/adr/0009-the-review-is-the-only-gate.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/adr/0009-the-review-is-the-only-gate.md); [`crates/core/src/agent.rs`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/crates/core/src/agent.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: Aldwin deliberately centers developer engagement, but human involvement in current task edits does not by itself establish a higher-recursion S3 function.

### Absence scope

- Surfaces inspected: plan/ask tools; turn/step lifecycle; dispatcher hooks; review/comment path; permissions/sandbox; session state; product/development boundary.
- Plausible first-party paths checked: planner as current manager; developer reviewer as S3; permission/sandbox controller; review timing; session supervisor; concurrent dispatcher.
- Why no material first-party path remains: each located mechanism governs one coding operation or enforces a static/operator boundary. No separate first-party owner regulates whole-current organizational commitments/resources across operational units.

## S3* — Complementary audit

- State: —
- Function: no material boundary-reachable complementary audit function was established in the released Aldwin product.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. The product's full-window edit review is the routine mandatory gate for staged edits, not alternative/sporadic access beyond ordinary operational reporting. It reviews the proposed changeset before it becomes the operating state.
- Decision owner: not established for an autonomous complementary-audit role. The developer owns routine staged-edit acceptance/comment/discard judgment.
- Supporting / enforcement mechanisms: staged overlay; full-window diff review; line comments; automatic corrective follow-up turn; ordinary command/test evidence.
- Closure path: routine edit proposal → developer approve/comment/discard → write, rework turn or discard is closed, but this is the primary operational edit gate rather than a complementary S3* channel.
- Why this is / is not agent-owned: the released product does not ship a separate reviewer/judge actor. The repository's separate `aldwin-review` loop has blind subagent judges and mechanical gates, but `docs/spec/aldwin.md` explicitly declares that crate dev-only and never in a release build, so its judgments are not boundary-reachable in the assessed product mode.
- Evidence: [`docs/adr/0009-the-review-is-the-only-gate.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/adr/0009-the-review-is-the-only-gate.md); [`docs/spec/aldwin-review.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/spec/aldwin-review.md); [`docs/spec/aldwin.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/spec/aldwin.md).
- Basis: explicit + boundary-provenance absence review.
- Confidence: high.
- Caveats: the product has unusually strong human review and the repository-development system has unusually strong independent judges. Neither should be collapsed into product S3*: the former is routine S1 gating and the latter is adjacent development infrastructure.

### Absence scope

- Surfaces inspected: product staged review path; automatic review-comment follow-up; command/test workflow; dev-only `aldwin-review` specification; `.agents`/git-hook relationship as documented; release-boundary description.
- Plausible first-party paths checked: human staged review as complementary audit; dev blind subagent judges; deterministic quality stages; commit gate; second reviewer in released runtime; independent artifact inspection.
- Why no material first-party path remains: the only product-reachable review is the ordinary edit-acceptance path, while the genuinely independent judge system is explicitly excluded from release builds and belongs to repository development.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective outside-and-then intelligence/adaptation loop was established in the released runtime.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Aldwin can inspect the current repository, execute commands and query configured language/MCP tools, but the pinned product explicitly has no web search, no background agents and no self-carried cross-session memory.
- Decision owner: not established.
- Supporting / enforcement mechanisms: current-session conversation history/resume; project instructions; provider/model selection; MCP extension; language-server explain tool.
- Closure path: not applicable; no external/future distinction → adaptation option → change to Aldwin organizational strategy/capability → return to current operation loop was found.
- Why this is / is not agent-owned: current-task code understanding and developer-authored memory are operational context. New capabilities/providers/MCP servers are operator configuration rather than autonomous prospective adaptation by the runtime.
- Evidence: [`README.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/README.md); [`docs/spec/aldwin.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/spec/aldwin.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external model/MCP/language-server information can improve the present coding task without constituting future-oriented organizational adaptation.

### Absence scope

- Surfaces inspected: product capability statement; project/session memory semantics; provider/model configuration; MCP and language-server extension; plan/review loop; repository development review boundary.
- Plausible first-party paths checked: web/environment scanning; autonomous capability acquisition; future planning; cross-session learned memory; evaluator-driven self-improvement; model/provider adaptation; background research agents.
- Why no material first-party path remains: the pinned release explicitly omits several candidate mechanisms, and the remaining external integrations serve current operations under developer configuration rather than an autonomous outside-and-then adaptation loop.

## S5 — Identity and ultimate policy

- State: —
- Function: no material runtime identity/ultimate-policy decision path was established at the selected session recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Aldwin has a strong authored product ethos and durable safety/review boundaries, and the developer has final say over each staged edit, but those are static identity constraints plus operational authorship rather than a runtime path for deciding identity/ultimate-policy matters.
- Decision owner: not established.
- Supporting / enforcement mechanisms: mandatory edit review; workspace sandbox; deny locks; project/global configuration; provider/model selection; developer-authored instructions and memory.
- Closure path: not applicable; no identity/ultimate-policy issue is surfaced to a legitimate S5 authority and returned as a new governing policy for subsequent runtime operation.
- Why this is / is not agent-owned: the model cannot remove the structural edit-review gate or redefine the system's purpose. The developer's approve/comment/discard choice concerns a concrete code change, which Methodology 0.3.6 explicitly distinguishes from S5-level policy/identity governance.
- Evidence: [`README.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/README.md); [`docs/spec/aldwin.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/spec/aldwin.md); [`docs/adr/0009-the-review-is-the-only-gate.md`](https://github.com/hvess/aldwin-agent/blob/f6a17306688e75f5d206df8bcdb421b075d859c9/docs/adr/0009-the-review-is-the-only-gate.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: Aldwin's ethos is unusually explicit, but a written ethos and mandatory task-level human approval are not by themselves runtime S5 closure.

### Absence scope

- Surfaces inspected: product ethos/identity specification; review gate; permission/sandbox boundaries; developer-authored memory/instructions; provider/model/MCP configuration; session command/control paths.
- Plausible first-party paths checked: developer review as S5; autonomous policy revision; parent-governed identity escalation; purpose/ethos update; provider/model decision as strategy; config/deny policy as ultimate authority.
- Why no material first-party path remains: the reviewed runtime enforces durable externally authored constraints and operational developer decisions but does not supply an identity/ultimate-policy deliberation-and-return loop at this recursion.

## Recursion, variety, escalation and unresolved evidence

- Recursion: one Aldwin coding session. The model actor plus tools/review/session machinery form one S1; MCP servers remain dependencies, and repository-development judges belong to a different adjacent organization.
- Variety: source/build state, shell/LSP/tool results, implementation choices, staged code, developer review comments and execution failures are primarily absorbed by S1 plus deterministic/human constraints.
- Escalation: staged edits always reach developer review before Aldwin writes them. Comments/discard feed directly back into the same S1 operation. This is an operational authorship/approval path, not evidence of S3/S5 by itself.
- Unresolved evidence: no material evidence gap remained that required `?` at the frozen revision. The boundary distinction between released review and dev-only `aldwin-review` was explicit enough to support negative higher-function conclusions.

## Assessment vector

**`A · — · — · — · — · —`**
