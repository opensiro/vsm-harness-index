---
harness_id: claw-code
project_name: Claw Code
repository: https://github.com/ultraworkers/claw-code
review_ref: 08106b0c3771ef5b4a5aa176acccd460e88b7325
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
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Claw Code

## Review boundary

- System in focus: the first-party Rust `claw` coding-agent runtime at frozen revision `08106b0c3771ef5b4a5aa176acccd460e88b7325`, including the CLI/interactive and one-shot execution surfaces, core conversation/session runtime, provider clients, built-in tool execution, permission/hooks/plugin/config machinery, MCP integration, and the native background `Agent` subagent path where those surfaces are reachable from normal operation.
- Purpose and identity: interpret software-engineering intent against a live repository, autonomously choose model/tool actions, execute bounded coding and inspection work, retain conversation/session state, and return repository-oriented results through the shipped `claw` runtime.
- Relevant environment: the user task, target repository/workspace and git state, model-provider responses, filesystem and shell results, web/MCP resources, tool failures, permission constraints, and concurrently delegated native subagent work.
- Standard-distribution boundary: the canonical Rust workspace under `rust/` and the shipped `claw` CLI/runtime are inside. External model services, external MCP servers, LazyCodex, Gajae-Code, `oh-my-codex` (OmX), `oh-my-openagent` (OmO), `clawhip`, and their independent planning/coordination/notification organizations are outside and do not donate VSM functions to `claw`.
- Credited operating / distribution surfaces: `README.md`; `USAGE.md`; `rust/crates/runtime/src/{lib,conversation,branch_lock,task_registry,team_cron_registry,worker_boot,policy_engine}.rs`; `rust/crates/tools/src/{lib,lane_completion}.rs`; and the native `Agent` execution path in `rust/crates/tools/src/lib.rs` that creates a separate `ConversationRuntime` and session for background subagents.
- Adjacent first-party surfaces excluded from ownership: repository-development/dogfood artifacts under `.omx/` and `docs/g00*`; development worker maps and verification reports; tests/fixtures/roadmap material not wired into the assessed runtime; the companion Python parity/reference layer under `src/` where it does not supply the canonical Rust execution path; and the external OmX/OmO/clawhip coordination stack described by `PHILOSOPHY.md` and `USAGE.md` as sitting around or on top of `claw`.
- First-party operating / deployment modes considered: interactive REPL; one-shot `claw prompt`; standard model/tool turns under read-only, workspace-write and danger-full-access permission modes; native background `Agent` subagents including `Verification`; task/team/worker/cron registry tools; and public runtime coordination/control primitives where they are actually reachable at the frozen revision.
- Recursion level: one `claw` coding-agent session is the focal organization. A native background `Agent` invocation can instantiate another operational coding/inspection unit with its own session and runtime, but tool calls, registry records and external OmX/OmO workers are not promoted to same-recursion S1 units merely from topology.
- Reviewed revision: `08106b0c3771ef5b4a5aa176acccd460e88b7325`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The frozen Rust distribution contains its own model-to-tool operating loop rather than delegating the coding loop to another host agent. `ConversationRuntime` owns the active `Session`, builds provider requests from current conversation state, consumes streamed assistant events, executes requested tools through the first-party `ToolExecutor`, appends tool results back into the session, and repeats until the model returns without further tool calls or the iteration bound is reached. Permission checks, hooks, context compaction and usage state support that loop without replacing the model-backed operational discretion.

The built-in `Agent` tool is a real first-party subagent constructor. `execute_agent` creates persisted output/manifest paths, selects a subagent type and model, derives a restricted tool set and system prompt, then spawns a background job. `run_agent_job` constructs a fresh `ConversationRuntime` with `Session::new()` and runs the delegated prompt. `Verification` is one shipped specialization with repository/test/search-capable tools, so the distribution can instantiate an audit-oriented actor whose evidence access and session are separate from the focal agent turn.

Several apparently multi-agent/control surfaces are materially narrower at the frozen revision than their names suggest. `TaskCreate` creates registry state; `TeamCreate` groups existing task identifiers and assigns a team id; the cron registry stores schedule/prompt metadata; these paths do not by themselves spawn a coordinated team or close a scheduler loop. `branch_lock` exposes a precise same-branch/overlapping-module collision detector and re-exports it from the runtime crate, but repository search at the frozen revision found no production caller that returns its collision result into later S1 behavior. Likewise `PolicyEngine` evaluates one `LaneContext`; the stronger lane-completion glue in `tools/src/lane_completion.rs` is marked dead-code and is not a standard boundary-reachable whole-system controller.

The repository's own `PHILOSOPHY.md` helps preserve the boundary: it attributes parallel workflow execution to OmX, event/notification routing to clawhip, and multi-agent planning/handoffs/disagreement resolution/verification convergence to OmO. Those organizations are useful provenance for how the repository was developed, but they are external to the assessed `claw` runtime and are not credited here.

Primary evidence:

- [`README.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md)
- [`USAGE.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/USAGE.md)
- [`PHILOSOPHY.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/PHILOSOPHY.md)
- [`rust/crates/runtime/src/lib.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/lib.rs)
- [`rust/crates/runtime/src/conversation.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/conversation.rs)
- [`rust/crates/runtime/src/branch_lock.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/branch_lock.rs)
- [`rust/crates/runtime/src/task_registry.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/task_registry.rs)
- [`rust/crates/runtime/src/team_cron_registry.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/team_cron_registry.rs)
- [`rust/crates/runtime/src/policy_engine.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/policy_engine.rs)
- [`rust/crates/tools/src/lib.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/tools/src/lib.rs)
- [`rust/crates/tools/src/lane_completion.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/tools/src/lane_completion.rs)

## Operational model

In normal interactive or one-shot operation, a user prompt enters the first-party conversation runtime. The runtime packages current system/session context for the selected provider, receives model decisions, executes requested built-in tools under its permission/hook machinery, returns tool results into the same session, and continues until the model finishes. This is the primary S1 transformation at the declared boundary.

The focal agent can also invoke the native `Agent` tool. That path creates a fresh background conversation runtime and persists the delegated actor's manifest/output. The standard distribution therefore contains a genuine independent-agent construction path, including an explicitly verification-oriented specialization, rather than only task metadata. However, the surrounding higher-order organization is intentionally conservative in this assessment: task/team registries, collision detection and lane policy helpers receive credit only where a complete function and return path are actually wired into the assessed mode.

## S1 — Operations

- State: A
- Function: autonomously transform software-engineering intent into repository analysis or changes through a first-party model/tool execution loop.
- Disturbance / variety regulated: heterogeneous user goals, repository structure, source state, model responses, tool results and failures, permission outcomes, and intermediate findings that require context-sensitive choices rather than a fixed command script.
- Decisive decision or feedback right: choose the next repository/tool action, interpret returned evidence, revise subsequent action selection, and decide when the turn is complete.
- Decision owner: the model-backed agent actor operating through the first-party `ConversationRuntime`; the external provider supplies inference, while `claw` owns the reachable session/tool/feedback organization in which that discretion is exercised.
- Supporting / enforcement mechanisms: `Session`; provider request/stream plumbing; built-in tool executor; permission policy/enforcer; hooks; iteration bound; usage tracking; automatic context compaction; filesystem/shell/search/MCP tools; CLI and session persistence surfaces.
- Closure path: user prompt → first-party runtime builds a provider request from current session state → model selects an answer or tool call → `claw` permission-checks and executes the tool → tool evidence is appended to the session → the next model turn changes action based on that evidence → iteration ends when the model returns without further tool calls, producing an answer and/or repository effect.
- Boundary reachability: the loop is the shipped core path for interactive REPL and one-shot `claw prompt`; a downstream developer does not need to compose the model/tool feedback cycle.
- Why this is / is not agent-owned: if the model-backed actor is removed while the deterministic runtime, session and tool executors remain, the system retains mechanisms but loses the contextual choice of what to inspect/change next and when the coding turn is complete. The decisive S1 discretion is therefore agent-owned.
- Evidence: [`rust/crates/runtime/src/conversation.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/conversation.rs); [`rust/crates/runtime/src/lib.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/lib.rs); [`USAGE.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/USAGE.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model intelligence is an external dependency. The assessment credits the first-party runtime closure, not unrelated organizational behavior inside Anthropic/OpenAI-compatible providers or other external agent products.

## S2 — Coordination

- State: —
- Function: no complete first-party same-recursion coordination function was established in the reviewed standard-distribution boundary.
- Disturbance / variety regulated: the repository structurally models one relevant disturbance — two lanes targeting the same branch and overlapping/nested module scopes — but the reviewed `claw` operating path does not close an attenuation loop from that detection into subsequent S1 behavior.
- Decisive decision or feedback right: not established. `detect_branch_lock_collisions` deterministically reports collisions; no standard production caller was found that decides and returns an isolation/reservation/reroute response to the affected native agent units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: public `BranchLockIntent` / `BranchLockCollision` types and collision detector; task/team registry metadata; background native `Agent` construction; worker state; external OmX/OmO coordination described in repository documentation but excluded from the `claw` boundary.
- Closure path: not established. The detector returns collision data to a caller, but the frozen first-party runtime does not wire that result into a coordination action that changes the conflicting S1 units' subsequent operation.
- Why this is / is not agent-owned: no S2 function is credited, so ownership is not classified. A disturbance-specific detector is stronger than generic messaging, but an unwired diagnostic surface does not satisfy the required feedback witness.
- Evidence: [`rust/crates/runtime/src/branch_lock.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/branch_lock.rs); [`rust/crates/runtime/src/lib.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/lib.rs); [`rust/crates/runtime/src/task_registry.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/task_registry.rs); [`PHILOSOPHY.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/PHILOSOPHY.md).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: the public collision detector is a plausible future S2 constructor ingredient. It is not published as `C` here because Methodology 0.3.6 requires the S2 function itself — including feedback into subsequent S1 behavior — to be established before ownership classification.

### Absence scope

- Surfaces inspected: native `Agent` subagent construction/execution; `branch_lock`; `TaskRegistry`/lane board; team and cron registries; worker lifecycle; tool dispatch; `PHILOSOPHY.md`/`USAGE.md` descriptions of surrounding multi-agent stacks; and current runtime exports/usages at the frozen revision.
- Plausible first-party paths checked: explicit same-branch/module collision detection; task dependencies/team grouping; worker prompt/state controls; registry heartbeat/lane state; multi-agent command descriptions; and adjacent OmX/OmO coordination claims.
- Why no material first-party path remains: the only disturbance-specific first-party mechanism found is an unwired collision detector; task/team/worker surfaces provide lifecycle/delegation/shared state rather than returned disturbance attenuation; and the documented planning/handoff/disagreement machinery belongs to external OmX/OmO rather than the assessed `claw` runtime.

## S3 — Inside-and-now control

- State: —
- Function: no boundary-reachable whole-system current-control function over the focal organization was established.
- Disturbance / variety regulated: per-lane completion, stale/diverged branch conditions, retries, review status, permission decisions and worker lifecycle are represented by mechanisms, but no standard actor was found that integrates a whole-system current view and exercises discretionary resource/commitment/priority control on behalf of the whole.
- Decisive decision or feedback right: not established at S3 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: task/lane registry state; worker create/observe/restart/terminate surfaces; permission enforcement; workspace-test branch-divergence preflight; `PolicyEngine` rule/action types; and lane-completion helpers.
- Closure path: not established for S3. Static permission/preflight mechanisms can block local actions, and registry APIs can mutate individual records, but no current whole-system decision loop was reconstructed.
- Why this is / is not agent-owned: deterministic enforcement of local constraints and per-lane lifecycle is not sufficient to establish S3, and no autonomous or parent current-control owner closes the missing function in the reviewed mode.
- Evidence: [`rust/crates/runtime/src/task_registry.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/task_registry.rs); [`rust/crates/runtime/src/policy_engine.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/policy_engine.rs); [`rust/crates/tools/src/lane_completion.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/tools/src/lane_completion.rs); [`rust/crates/tools/src/lib.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/tools/src/lib.rs).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: `PolicyEngine` exposes expressive retry/rebase/merge/escalate/block actions, but the inspected context is per-lane and the stronger completion glue at this revision is explicitly dead-code. Component vocabulary and deterministic authority do not substitute for an operational S3 closure.

### Absence scope

- Surfaces inspected: task/lane/team/cron registries; worker lifecycle; permission and branch-preflight behavior in tools; `policy_engine`; `lane_completion`; focal and background conversation runtimes; CLI/usage documentation.
- Plausible first-party paths checked: lane board/heartbeats, terminate/restart controls, policy retry/rebase/merge/escalation actions, completion/cleanup helpers, permission modes, stale-branch blocking, and operator-facing lifecycle APIs.
- Why no material first-party path remains: no inspected standard path combines a whole-system current view with a live decision over resources, commitments, priorities, synergy or intervention and returns that decision across current operations. The strongest policy glue is either per-lane/static enforcement or not wired into production at the frozen revision.

## S3* — Complementary audit

- State: C
- Function: provide a first-party construction path for a materially separate verification actor to challenge claims made by ordinary coding operation using direct repository/test/search evidence.
- Disturbance / variety regulated: a focal coding agent can report a change as correct or complete despite defects, missed constraints, failing tests or evidence it did not inspect in its ordinary session.
- Decisive decision or feedback right: a separately instantiated `Verification` subagent can independently inspect repository artifacts and execute verification-capable tools, producing a persisted finding/result distinct from the focal agent's ordinary report; the standard distribution does not itself close those findings into mandatory corrective action.
- Decision owner: constructor/control state `C`. The first-party runtime supplies the audit-specific autonomous actor and independent evidence path, while a caller/developer or higher-level workflow must still compose the returned finding into a corrective control loop.
- Supporting / enforcement mechanisms: model-visible `Agent` tool; background thread/job; fresh `Session::new()`; separate `ConversationRuntime`; verification-specific system prompt/type; restricted verification tool set; persisted output and manifest; lane events/terminal result state.
- Closure path: focal operation produces a claim/change → caller invokes `Agent` with `Verification` specialization → first-party code creates a separate session/runtime and the verifier directly inspects/tests/searches relevant evidence → verifier output is persisted and exposed via returned output/manifest paths → caller can read the finding and alter later operation. The final finding-to-correction leg is intentionally not treated as prewired standard closure, hence `C` rather than `A`.
- Boundary reachability: `Agent` is a shipped built-in model-visible tool in the canonical Rust runtime; the verification specialization and its fresh runtime/session are created by first-party code without an external workflow framework. No OmX/OmO behavior is needed to instantiate this audit path.
- Why this is / is not agent-owned: the complementary audit judgment itself is model-owned inside the independently instantiated verifier, but the assessed standard distribution leaves authority/closure from finding to subsequent corrective operation to composition. This is the Methodology's constructor case rather than a fully closed autonomous S3* loop.
- Evidence: [`rust/crates/tools/src/lib.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/tools/src/lib.rs); [`rust/crates/runtime/src/conversation.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/conversation.rs); [`USAGE.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/USAGE.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this assessment does not import OmO's documented cross-agent verification loops. It credits only the native verification constructor whose separate runtime/session and persisted evidence path are present in `claw`. No mandatory repair/retry edge driven by the verifier was found in the standard path.
- Claim being audited: correctness/completeness of repository work or claims produced by the focal coding-agent operation.
- Ordinary reporting path: the focal `ConversationRuntime`'s own assistant/tool sequence and final output.
- Complementary access path: a native `Verification` `Agent` job with a fresh session/runtime and direct bash/read/glob/grep/web/search/tool access to repository and external evidence.
- Independence boundary: separate session, runtime instance, background job, prompt specialization and result artifact; model/provider may still be configured from the same family, so this is functional/session independence rather than organizational-provider independence.
- Who acts on findings: the invoking focal agent, developer or higher-level first-party/external workflow after reading the persisted verifier result; corrective return is not automatically enforced by the native constructor.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally and prospectively oriented adaptation loop was established in the reviewed `claw` operating boundary.
- Disturbance / variety regulated: the runtime can fetch current web/MCP information and retain session/context/skills, but these mechanisms serve present tasks rather than a demonstrated future-oriented sensing → option-development → capability-change cycle.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: WebFetch/WebSearch/MCP tools; session persistence and compaction; project/user skill lookup; configuration; recovery/policy helpers; repository-development learning and evolution artifacts outside the product boundary.
- Closure path: not established for S4.
- Why this is / is not agent-owned: present-task research and retained context do not by themselves constitute outside-and-then adaptation, and no standard agent owns a prospective capability-change loop returning into present `claw` capability.
- Evidence: [`rust/crates/tools/src/lib.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/tools/src/lib.rs); [`USAGE.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/USAGE.md); [`PHILOSOPHY.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/PHILOSOPHY.md).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: the repository itself was developed through a broader agent-managed organization and exposes flexible skills/configuration, but development history and generic extensibility are adjacent evidence, not a boundary-reachable S4 function of the shipped runtime.

### Absence scope

- Surfaces inspected: web/MCP tools; native agents; skills lookup; session/context persistence and compaction; policy/recovery helpers; README/USAGE/PHILOSOPHY; adjacent repository-development artifacts.
- Plausible first-party paths checked: external research during tasks, retained skills, session memory, recovery, model/provider configuration, repository self-improvement/dogfood activity, and external OmX/OmO workflow evolution.
- Why no material first-party path remains: inspected mechanisms either support the current task, retain context, or belong to adjacent development/external organizations. None reconstructs environmental/future distinctions into adaptation options with a return path that changes present `claw` capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy decision loop was established at the declared `claw` recursion.
- Disturbance / variety regulated: permission modes, system prompts, provider settings, configuration rules and user approvals constrain ordinary operation, but no identity-level dispute/proposal is routed to an ultimate authority and returned as governing policy for subsequent operation.
- Decisive decision or feedback right: not established at S5 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: system prompt construction; permission policy/enforcer; config/rules imports; approval-token and operator controls; user task intent; repository maintainer/development governance outside the runtime boundary.
- Closure path: not established for identity/ultimate policy.
- Why this is / is not agent-owned: operational safety/configuration choices do not become S5 merely because they can block tools or require human action. No autonomous or parent-governed identity closure was found in the assessed mode.
- Evidence: [`rust/crates/runtime/src/lib.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/lib.rs); [`rust/crates/runtime/src/policy_engine.rs`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/rust/crates/runtime/src/policy_engine.rs); [`USAGE.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/USAGE.md); [`PHILOSOPHY.md`](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/PHILOSOPHY.md).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: the human-directed development philosophy is not imported as a runtime S5 parent arrangement. A user deciding a task or permission escalation is an operational event, not by itself an identity/ultimate-policy decision at this recursion.

### Absence scope

- Surfaces inspected: system prompt/runtime; permission modes and enforcement; config/rules/plugin surfaces; approval-token/policy helpers; CLI/user controls; README/USAGE/PHILOSOPHY; adjacent repository-development governance.
- Plausible first-party paths checked: operator approval, permission escalation, policy rules, provider/model selection, durable prompts/configuration, maintainer direction and external OmX/OmO governance.
- Why no material first-party path remains: no inspected standard-distribution path accepts an identity/ultimate-policy matter, routes it to a legitimate ultimate authority, and returns that authoritative decision to govern subsequent `claw` operation. The available mechanisms are operational constraints or adjacent development governance.

## Distributed OSS parent arrangement

The repository documents an agent-managed public development process with human direction and external OmX/OmO/clawhip coordination. That development organization is adjacent to the `claw` runtime assessed here. No organization-level parent mode for S3/S4/S5 is therefore inferred from contributor activity, public development artifacts, or the existence of a human directing repository work.

## Self-hosted and non-human modes

`claw` is locally runnable and exposes explicit operator permission/configuration controls. These controls do not establish parent notation by themselves. The reviewed runtime contains an autonomous S1 loop and an S3* construction path, but no qualifying first-party parent-governed S3/S4/S5 mode was reconstructed at the declared recursion.

## Recursion

The focal coding session is a viable operational loop. Native `Agent` jobs can create additional first-party autonomous conversations with separate sessions and bounded tools, which is sufficient to establish distinct operational actors where their work is independent. It does not by itself prove recursive viability: no evidence establishes that each spawned subagent carries its own complete metasystem at a lower recursion. Task nesting and background execution are therefore treated as decomposition, not automatic VSM recursion.

## Variety and escalation

The main loop amplifies regulatory capacity by exposing filesystem, shell, search, web/MCP and specialized agent tools; permissions and workspace/path checks attenuate unsafe action variety. Tool failures and returned evidence feed directly back into later model turns. `AskUserQuestion`, permission escalation, worker lifecycle controls and error returns can move exceptional variety to a human/caller, but those channels are classified by the function they actually close rather than treated as additional VSM systems. No separate S3/S4/S5 ownership is inferred from escalation alone.

## Evidence gaps

- This is a source review of the exact frozen revision; no new runtime experiment was required to establish the shipped code paths.
- `branch_lock` is a concrete disturbance-specific detector but no production caller was found that closes it into later S1 behavior, so it is not promoted to `S2=C`.
- `PolicyEngine` and lane-completion types are implementation evidence, but the strongest lane-completion glue is marked dead-code and the available contexts are per-lane rather than a whole-system current-control closure.
- The native `Verification` subagent supplies a strong audit-specific independent-access constructor, but no mandatory native finding → correction/retry path was found; this keeps S3* at `C` rather than `A`.
- OmX, OmO and clawhip may close richer multi-agent coordination/control loops in the broader development stack; they are separate systems and intentionally excluded from this assessment boundary.
