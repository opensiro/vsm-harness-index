---
harness_id: aivo-code
project_name: Aivo Code
repository: https://github.com/yuanchuan/aivo
review_ref: b26438571e80ae28fa489f07c2c22fd595e10269
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Aivo Code

## Review boundary

- System in focus: the first-party Aivo Code coding-agent runtime in `yuanchuan/aivo` at frozen revision `b26438571e80ae28fa489f07c2c22fd595e10269`, including `AgentEngine`, its model/tool turn loop, tool batching, named subagents, built-in review subagents, session communication, durable code sessions, TUI and headless `aivo code -e` paths, and directly wired first-party runtime controls.
- Purpose and identity: execute software-engineering tasks through a first-party model/tool loop, optionally fan work out to bounded Aivo subagents, coordinate parallel delegates through explicit isolation, communicate across open Aivo Code sessions, and return delegated/review evidence to the producing agent.
- Relevant environment: user tasks and steering, repository/workspace state, Git worktrees, filesystem/process/test output, provider/model responses, Aivo session state, peer Aivo Code sessions, MCP tools, named agent profiles and runtime permissions.
- Standard-distribution boundary: the built-in Aivo Code engine and its shipped subagent/review profiles are inside. Aivo's ability to launch Claude Code, Codex, Gemini, OpenCode, Pi, Grok or other external developer agents is outside this assessment except as launcher functionality; those external agents cannot donate their internal organizational functions to Aivo Code.
- Credited operating / distribution surfaces: `README.md`; `src/agent/engine.rs`; `src/agent/engine/turn.rs`; `src/agent/engine/tool_batch.rs`; `src/agent/engine/subagent.rs`; `src/agent/engine/session_comms.rs`; `src/agent/subagents.rs`; `src/agent/builtin_agents/verification.md`; `src/agent/builtin_agents/evaluate.md`; `src/commands/engine_assembly.rs`; `src/commands/code_agent_oneshot.rs`; and the Aivo Code TUI runtime where it directly wires the same engine.
- Adjacent first-party surfaces excluded from ownership: generic provider/router compatibility code, imported foreign-agent transcripts, desktop/launcher glue for external coding agents, repository-development CI, and maintainer governance except where a source directly corroborates the shipped Aivo Code runtime.
- First-party operating / deployment modes considered: interactive Aivo Code TUI; headless `aivo code -e`; named and generic subagents; parallel subagent batches; optional worktree isolation; built-in `verification`, `evaluate`, and `advisor` profiles; open-session `list_sessions` / `send_session`; project/user agent profiles; skills/MCP; post-edit self-verification.
- Recursion level: one Aivo Code coding organization centered on a top-level `AgentEngine`. The main model-backed agent is the focal production S1. Delegated Aivo sub-engines are bounded production/support S1s when they execute coding tasks; the built-in verification/evaluate subagents are complementary audit actors when used in review mode.
- Reviewed revision: `b26438571e80ae28fa489f07c2c22fd595e10269`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Aivo Code ships a first-party `AgentEngine` used by both the terminal UI and the headless `aivo code -e` path. A user turn enters a multi-step model/tool loop: Aivo sends the current conversation and tool schemas to the selected model, executes returned tools subject to permissions and guards, appends results, and repeats until the model converges or a typed stop condition ends the turn.

The same engine can delegate to fresh Aivo sub-engines. Named specialist profiles are discovered from project/user paths, with compiled-in first-party profiles at lowest precedence. A delegated engine inherits the parent workspace context, provider/runtime, relevant tools and budgets, cannot recurse further, and returns its answer/report as the parent `subagent` tool result.

Parallel delegation has an explicit interference-control path. If the model emits several leading `subagent` calls in one batch, Aivo can run them concurrently. The `subagent` tool exposes `isolation: "worktree"` to the model with guidance to use it for file-editing delegates, especially several in parallel. A requested worktree gives that delegate a disposable Git worktree; when a parallel isolated delegate cannot obtain it, Aivo refuses to fall back into the shared workspace because concurrent writers would collide.

Aivo also compiles first-party review specialists into the binary. The `verification` profile is explicitly adversarial and returns a PASS/FAIL verdict backed by commands and observed results; `evaluate` performs read-only code review and returns APPROVE/REQUEST CHANGES. These profiles omit edit/write tools, run in a separate sub-engine/model context, inspect the live workspace/diff, and return their report into the parent agent's tool-result stream. For edit-less reviewers, Aivo deliberately avoids worktree isolation so the reviewer sees the producing agent's uncommitted changes.

Primary evidence:

- [`README.md`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/README.md)
- [`src/agent/engine/turn.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/turn.rs)
- [`src/agent/engine/tool_batch.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/tool_batch.rs)
- [`src/agent/engine/subagent.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/subagent.rs)
- [`src/agent/engine/session_comms.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/session_comms.rs)
- [`src/agent/subagents.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/subagents.rs)
- [`src/agent/builtin_agents/verification.md`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/builtin_agents/verification.md)
- [`src/agent/builtin_agents/evaluate.md`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/builtin_agents/evaluate.md)
- [`src/commands/engine_assembly.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/commands/engine_assembly.rs)
- [`src/commands/code_agent_oneshot.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/commands/code_agent_oneshot.rs)

## Operational model

The main Aivo Code agent receives the user's task and the current coding-session/workspace state. It chooses tools, observes outputs and iterates. It may issue one or more `subagent` calls. Several leading delegate calls in the same model batch are executed concurrently by Aivo's worker pool.

For work that can interfere through shared file writes, the model-visible subagent contract explicitly offers disposable Git worktree isolation and tells the agent to use it for editing delegates, especially parallel ones. The model therefore owns a real coordination choice: isolate delegates whose concurrent writes would collide. Aivo's runtime then enforces that choice and fails closed rather than silently running a requested isolated parallel delegate in the shared workspace.

For complementary review, the main agent can delegate to Aivo's compiled-in `verification` or `evaluate` profiles. The reviewer is a separate model-backed sub-engine with a no-edit tool scope. It reads the current change, runs real commands/tests where applicable, produces an evidence-backed verdict, and returns the report to the parent agent. The producing agent can then change its subsequent implementation or completion decision.

Peer Aivo Code sessions can also exchange messages via `list_sessions` / `send_session`, including bounded blocking waits and explicit mutual-wait handling. This is useful supporting communication, but the positive S2 finding does not depend on treating every open user session as one organization: the parallel-subagent worktree path already supplies a concrete same-recursion interference/attenuation closure.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work by interpreting a task, selecting coding/tools, executing them, observing results and iterating to a completed or typed terminal outcome.
- Disturbance / variety regulated: heterogeneous codebases and requests, changing files/Git/process state, compiler/test/tool failures, permissions, provider responses, context pressure, interruptions, background work and implementation choices.
- Decisive decision or feedback right: choose what to inspect, which tool or subagent to invoke, what edit/command to perform next, how to react to returned evidence and when to finish or continue.
- Decision owner: the main model-backed Aivo Code agent instantiated by `AgentEngine`.
- Supporting / enforcement mechanisms: first-party turn loop; file/process/search tools; plan/finish tools; MCP; skills; permissions; retries/guards; session persistence; context compaction; TUI/headless hosts.
- Closure path: user task + current workspace/session → model selects action/tool → Aivo executes or gates it → result enters conversation → next model request sees the updated state → next action or terminal outcome.
- Boundary reachability: `aivo code` and `aivo code -e` instantiate the same first-party engine directly.
- Why this is / is not agent-owned: removing the model-backed actor removes the open-ended coding judgment; deterministic runtime code remains transport/enforcement only.
- Evidence: [`src/agent/engine/turn.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/turn.rs); [`src/commands/engine_assembly.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/commands/engine_assembly.rs); [`src/commands/code_agent_oneshot.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/commands/code_agent_oneshot.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference comes from an external provider; Aivo is credited for the first-party decision/tool/feedback organization around it.

## S2 — Coordination

- State: A
- Function: attenuate concrete interference among concurrently executing delegated coding S1s by separating their mutable repository state when the main agent judges isolation necessary.
- Disturbance / variety regulated: parallel file-mutating delegates can write the same shared workspace and collide, overwrite, or observe each other's partial changes.
- Decisive decision or feedback right: decide, in the model-authored `subagent` call, to request `isolation: "worktree"` for an editing delegate, especially when several delegates are fanned out in parallel.
- Decision owner: the main model-backed Aivo Code agent. A profile may also predeclare isolation, but the standard tool contract independently exposes the same coordination decision to the agent at runtime.
- Supporting / enforcement mechanisms: concurrent subagent worker pool; model-visible `isolation` argument; disposable Git worktrees; per-delegate cwd; worktree guards/finalization; fail-closed refusal when requested isolation cannot be created for a parallel delegate.
- Closure path: main agent identifies/fans out parallel delegated work → chooses worktree isolation for writers → Aivo creates separate worktrees before concurrent execution → delegates operate without shared-write collision → each result/worktree disposition returns to the parent → parent integrates or continues.
- Boundary reachability: normal Aivo Code engine assembly advertises the `subagent` tool and its model-callable `isolation: "worktree"` argument; several leading subagent calls in one ordinary model tool batch enter the built-in parallel worker pool, so this is a shipped runtime path rather than test-only plumbing.
- Distinct S1 units: two or more fresh delegated Aivo `AgentEngine` sub-engines running concurrently from one parent tool-call batch, each executing a bounded model/tool coding task.
- Inter-S1 disturbance: parallel file-mutating delegates in the same checkout can collide through shared writes, overwrite or observe one another's partial changes, and make the combined workspace result unreliable.
- Attenuating coordination relation: the parent model selects worktree isolation for the affected delegates; Aivo binds each isolated child to a disposable Git worktree and, for a parallel delegate that requested isolation, refuses to fall back to the shared workspace if isolation cannot be created.
- Feedback into subsequent S1 behaviour: isolation changes each child S1's actual workspace before it acts; after the parallel batch, each delegated result and worktree disposition returns as parent tool results so the main S1 can decide subsequent integration, review, or follow-up.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping rests on an explicit inter-S1 concurrent-write collision and a first-party worktree relation chosen to attenuate that disturbance. Parallel delegation, session mail, worker-pool scheduling and result fan-in are not credited by themselves.
- Why this is / is not agent-owned: the runtime deterministically enforces the requested boundary, but the substantive choice that a delegate should be isolated is available to and selected by the main agent from the tool schema. Without that model decision, the generic path can run shared-workspace delegates.
- Evidence: [`src/agent/engine/tool_batch.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/tool_batch.rs); [`src/agent/engine/subagent.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/subagent.rs); [`src/agent/builtin_skills/create-agent.md`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/builtin_skills/create-agent.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Aivo does not force every parallel delegate into a worktree. The credited autonomous S2 mode is the supported runtime path where the agent explicitly chooses isolation to attenuate the documented writer-collision disturbance.

## S3 — Inside-and-now control

- State: —
- Function: no distinct first-party whole-organization current-control function was established beyond the focal main coding agent's own task execution and bounded delegation.
- Disturbance / variety regulated: plans, budgets, permission state, context/step ceilings, subagent progress, background jobs and session messages are controlled operationally, but no separate whole-system current portfolio/resource/accountability control role is established.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `update_plan`; `finish_turn`; typed stops; subagent status; background jobs; permissions; TUI `/goal`; session mail; runtime guards.
- Closure path: not applicable; no distinct whole-current state aggregation → metasystem intervention → changed multi-S1 operational allocation/accountability loop was reconstructed.
- Why this is / is not agent-owned: the main agent can delegate and observe bounded work while performing its own S1 task, but that does not by itself create a separate S3 function.
- Evidence: [`src/agent/engine/turn.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/turn.rs); [`src/agent/engine/tool_batch.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/tool_batch.rs); [`src/agent/engine/session_comms.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/session_comms.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: this negative state does not deny substantial lifecycle control inside a coding turn.

### Absence scope

- Surfaces inspected: plan/finish tracking; autonomous goal loop; subagent worker pool; delegate status/tokens/budgets; jobs; permissions; open-session communication; TUI/headless runtime.
- Plausible first-party paths checked: main agent as supervisor; `/goal` as metasystem objective control; subagent status feed; session-to-session communication; runtime budget/guard interventions.
- Why no material first-party path remains: located controls either belong to the focal S1's current task, enforce configured bounds, or support peer/delegate communication. None establishes a distinct whole-system S3 authority over a portfolio of operational S1 commitments/resources.

## S3* — Complementary audit

- State: A
- Function: independently challenge a producing coding agent's change/completion using a separate model-backed reviewer with complementary read-only access and evidence-backed verdicts.
- Disturbance / variety regulated: the producing agent may believe its implementation is correct or complete while the actual diff, tests, commands or edge cases reveal failure.
- Decisive decision or feedback right: inspect the live workspace/change through a separate review context, decide PASS/FAIL or APPROVE/REQUEST CHANGES from observed evidence, and return that verdict/report to the parent agent.
- Decision owner: the separate model-backed Aivo subagent instantiated from the compiled-in `verification` or `evaluate` profile.
- Supporting / enforcement mechanisms: built-in review profiles compiled into the binary; fresh delegated `AgentEngine`; no edit/write tools; read/grep/glob/list/run tools; real command/test execution; bounded subagent run; parent `subagent` result path; optional deterministic post-edit self-verification as corroborating evidence.
- Closure path: producing main agent has a change/completion claim → invokes built-in verification/evaluate subagent → separate reviewer reads current workspace/diff and runs independent checks → reviewer emits an evidence-backed verdict → Aivo returns it as the parent tool result → main agent sees the verdict and can revise or reconfirm subsequent work.
- Boundary reachability: the review profiles are compiled-in defaults discovered by normal Aivo Code engine assembly; no downstream custom reviewer implementation is required.
- Why this is / is not agent-owned: deterministic Aivo code constructs the sub-engine and tool boundary, but the substantive audit findings/verdict are generated by a separate model-backed reviewer. Removing that reviewer removes the semantic audit judgment.
- Evidence: [`src/agent/subagents.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/subagents.rs); [`src/agent/builtin_agents/verification.md`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/builtin_agents/verification.md); [`src/agent/builtin_agents/evaluate.md`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/builtin_agents/evaluate.md); [`src/agent/engine/subagent.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/engine/subagent.rs); [`src/commands/engine_assembly.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/commands/engine_assembly.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: review invocation is optional and model-selected; the state records a supported first-party audit mode, not a claim that every Aivo Code turn is independently reviewed.
- Claim being audited: the producing main agent's implementation/change and its implied correctness/completion claim.
- Ordinary reporting path: the producing agent's normal tool loop, text answer and `finish_turn` completion path.
- Complementary access path: a distinct sub-engine with no editing tools reads the live change/workspace and can run real tests/commands; edit-less review intentionally stays on the shared workspace so uncommitted producer changes remain visible.
- Independence boundary: separate model invocation/session state, separate specialist system instructions and tool scope, no nested delegation, and no write/edit capability for the built-in verification/evaluate profiles.
- Who acts on findings: the main Aivo Code agent receives the subagent's report as a tool result and controls subsequent coding/completion behavior.

## S4 — Intelligence / adaptation

- State: —
- Function: no material autonomous outside-and-future intelligence loop that selects and persists an organizational adaptation was established.
- Disturbance / variety regulated: skills, agent profiles, session history, model/provider choice and project guides can change available capability/context, but the standard runtime does not autonomously scan future environmental change and adopt a persistent organizational redesign on that basis.
- Decisive decision or feedback right: not established.
- Decision owner: user/project configuration or ordinary task-level model action, depending on the surface.
- Supporting / enforcement mechanisms: persistent agent profiles; create-agent skill; skills; project guides; session state; MCP; model/provider configuration.
- Closure path: not applicable; no environmental/future distinction → adaptation-option generation → autonomous selection → persistent capability/strategy change → later operation closure was found.
- Why this is / is not agent-owned: the model can author a profile when asked and Aivo can rediscover it mid-run, but generic authoring capability is not by itself a prospective S4 loop.
- Evidence: [`src/agent/subagents.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/subagents.rs); [`src/agent/builtin_skills/create-agent.md`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/builtin_skills/create-agent.md); [`src/commands/engine_assembly.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/commands/engine_assembly.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a downstream workflow may use Aivo tools to implement adaptation; that organization is outside this standalone assessment.

### Absence scope

- Surfaces inspected: persistent skills/agent profiles; create-agent workflow; session history/compaction; project guides; MCP; model/provider configuration; self-correction; review reports.
- Plausible first-party paths checked: self-improving agent profile creation; review-driven persistent change; model/provider switching; durable memory as organizational learning.
- Why no material first-party path remains: these mechanisms can modify capability or context under task/user control, but no shipped loop autonomously owns prospective environmental intelligence and persistent adaptation selection.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop was established.
- Disturbance / variety regulated: permissions, auto-approval, sandbox boundaries, project guides, model/provider settings, agent profiles and hooks constrain behavior, but they are operating policy/configuration rather than a reconstructed identity-level governance function.
- Decisive decision or feedback right: not established for an identity/ultimate-policy issue.
- Decision owner: user/operator/project configuration for the relevant policies; Aivo runtime enforces them and agents operate within them.
- Supporting / enforcement mechanisms: permission ladder; grants; sandbox escalation; hooks; project guides; model/provider configuration; agent profiles; approval UI/headless fail-closed behavior.
- Closure path: not applicable at S5 level; no genuine identity/policy conflict → legitimate ultimate authority → authoritative identity decision → returned operation loop was established.
- Why this is / is not agent-owned: neither the main coding model nor review subagents own Aivo Code's ultimate identity/policy boundary.
- Evidence: [`src/agent/permission.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/agent/permission.rs); [`src/commands/engine_assembly.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/commands/engine_assembly.rs); [`src/commands/code_agent_oneshot.rs`](https://github.com/yuanchuan/aivo/blob/b26438571e80ae28fa489f07c2c22fd595e10269/src/commands/code_agent_oneshot.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: human/operator policy can govern a broader organization that uses Aivo; that parent is not imported without a function-specific parent-mode closure.

### Absence scope

- Surfaces inspected: permission/grant system; sandbox policy; hooks; prompts/guides; model/provider settings; profile configuration; TUI/headless approval boundaries.
- Plausible first-party paths checked: user approval as ultimate authority; persistent grants; project instructions; model selection; agent-profile governance.
- Why no material first-party path remains: these are configured constraints and enforcement mechanisms, not evidence of an S5 identity/ultimate-policy adjudication loop at the assessed recursion.

## Distributed OSS parent arrangement

Aivo's public maintainer process is outside the deployed Aivo Code organization. User/project configuration may serve as external governance, but no S3/S4/S5 parent state is published here without a corresponding function-specific closure.

## Self-hosted and non-human modes

Aivo Code supports interactive and headless first-party execution. S1 remains agent-owned in both. S2 can be agent-owned when the model chooses worktree isolation for parallel delegates. S3* is agent-owned in the supported built-in reviewer mode. Permissions can remain human-configured or fail closed in headless use without changing those function ownership findings.

## Recursion

The focal recursion is one top-level Aivo Code coding organization. The main `AgentEngine` is the primary production S1. Parallel delegated sub-engines become bounded subordinate S1s for concrete tasks; their potential write interference creates the S2 disturbance. Verification/evaluate sub-engines are complementary S3* actors rather than production peers for the reviewed task.

Open-session mail can connect separate top-level Aivo Code sessions, but this assessment does not require folding every user session into the same recursion. It is supporting evidence that Aivo exposes model-owned peer communication, not the basis of the positive S2 classification.

## Variety and escalation

Aivo attenuates operational variety with permissions, retry/guard logic, context compaction, plan/finish contracts, background-job tracking, typed stops and self-verification. At the multi-actor boundary, model-selected worktree isolation attenuates concurrent writer interference. At the audit boundary, the main agent can escalate a correctness/completion claim to a separately instructed no-edit reviewer and consume its returned verdict.

## Evidence gaps

No `?` state is required at the frozen revision. Exact-ref implementation and first-party embedded review profiles establish S1, S2 and S3* closures. The review also inspected the strongest plausible S3/S4/S5 candidates—goal/plan supervision, persistent profile authoring and permission/policy controls—without finding the stronger required closures.

## Assessment summary

Aivo Code closes autonomous S1 through its first-party `AgentEngine` model/tool loop, autonomous S2 through model-selected Git-worktree isolation for explicitly parallel editing delegates, and autonomous S3* through compiled-in separate model-backed verification/evaluate reviewers whose evidence-backed verdicts return to the parent agent. Its planning/goal/runtime controls do not establish a distinct whole-system S3, profile/skill persistence does not close prospective S4, and permissions/configuration do not establish identity-level S5.

**Vector:** A · A · — · A · — · —
