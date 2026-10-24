---
harness_id: ambient-cli
project_name: Ambient CLI
repository: https://github.com/AmbientCrypto/ambient-cli
review_ref: 46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: P
---

# Ambient CLI

## Review boundary

- System in focus: installed Ambient CLI TypeScript coding harness using the Ambient inference fleet, including its normal model/tool agent loop, bundled parallel `subagent` tool, verification, capability/fleet selection and session-level human-approved north-star goal control.
- Purpose and identity: autonomously investigate and modify one coding workspace against user-defined goals, optionally splitting bounded investigation, review and edit work across model-backed children while requiring user authority for consequential permissions and changes to durable purpose.
- Relevant environment: code and test failures, concurrent builder approvals, live model-fleet readiness/capabilities and experienced reliability, workspace protections, changing user constraints, tool failures and human oversight.
- Standard-distribution boundary: pinned first-party packages/runtime, cli, tools-core, reliability, capabilities, context, sessions and permissions and their CLI/TUI/headless modes. Only installed first-party code wiring is credited; remote Ambient model service behavior and local project-authored hooks/agents/MCP servers are dependencies or optional user composition.
- Credited operating / distribution surfaces: one main coding Agent, first-party `subagent` waves with separate `scout`/`oracle`/`builder` model loops, serialized child approvals, read-only optional reviewer, native file/tool/diagnostics feedback, persistent per-model capability evidence and live-fleet role selection, TUI goal approval and durable next-turn instruction return.
- Adjacent first-party surfaces excluded from ownership: evals/ benchmarks and release ship-gates, unit tests, developer doc/brand organization, CI/npm packaging, upstream Ambient inference platform internal governance, user-provided custom reviewer presets, untrusted project hooks and MCP services until explicitly trusted and instantiated.
- First-party operating / deployment modes considered: interactive TUI vs one-shot/headless; default native tool-calling vs controller-assisted lane; optional foreground/background multi-child `subagent` waves with oracle role; configured trusted project verification; model `auto` with live catalogue and learned outcomes; optional `--goal`/`/goal` and agent `propose_goal_update` with interactive human confirmation.
- Recursion level: one Ambient CLI coding session organization, with a main model-backed Agent and bounded concurrent child S1 work cells; the legitimate human owner of the session north-star is a parent-governed identity authority, not the upstream OSS organization.
- Reviewed revision: `46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9` (batch #1013 row 9), observed 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The project is a pnpm TypeScript monorepo. `runtime/src/agent.ts` implements a model-driven turn/tool loop with native or controller-assisted tool calls and actual file/shell/diagnostics feedback. CLI/TUI binds project context, permissions, model-catalog access, durable session logs and interactive approvals. A built-in `subagent` tool can dispatch a wave of up to sixteen requested `scout`, `oracle`, or `builder` children; up to four run concurrently by default, with separate Agent contexts, model calls, role-specific tools, caps and event logs. Scouts and oracles run under forced read-only mode. Builder actions use the same permission ladder as the parent, and changes return for ordinary parent verification. The tool is not available to children, bounding recursion depth.

When multiple builders simultaneously request human approval or ask questions, `runSubagents` queues these prompts in a per-wave promise chain. This directly addresses a documented resolver-slot collision in the shared parent user prompt interface and returns each decision to the correct child. The policy is fixed developer code, not a model-selected conflict arbiter. A model-selected `oracle` role runs a separately instantiated read-only model agent, routed toward reviewer-strength live models, with direct file/search inspection capabilities and its own context. Its report returns to the main Agent as independent critique *when the parent actually asks for review*; ordinary post-edit diagnostics are not the S3* evidence.

The `auto` model path fetches the live inference fleet, compares candidate capabilities, readiness and role suitability, and scores accumulated per-model request outcomes (success frequency/latency) learned from previous runs before selecting the model for later runs. This is an externally oriented model-capability option-and-adoption mechanism, but the choice is a deterministic developer-written heuristic rather than autonomous S4 judgment. Separately, the optional north-star goal is user-authored, pinned in high-priority prompt context across turns/compaction and inherited by children. The model may call `propose_goal_update` when constraints change, but the user must approve or edit the proposed new purpose. Only that confirmation emits `goal.set` and causes subsequent turns to follow the new identity-level goal.

Pinned source: [README](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/README.md), [runtime Agent](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/agent.ts), [subagent wave](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/subagent.ts), [CLI tool wiring](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/agent/subagent-tool.ts), [model selection](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/reliability/src/pick-best.ts), [goal revision](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/tools-core/src/tools/propose-goal-update.ts).

## Operational model

A user supplies coding instructions and optionally a durable purpose. A model-backed main Agent selects tools and, for suitable work, may delegate read-only investigation, separate optional code review or bounded writing to child model loops. Child results and real workspace effects return to the main model. Multiple child prompts share one operator prompt resolver, so fixed serialization prevents approval promise overwrites. Successful/failed provider outcomes can change next-run model selection automatically from the live fleet; purpose changes remain authoritatively human-approved. No real LLM/provider/Browser performance test was run; this is frozen source and script-based contract verification.

## S1 — Operations

- State: A
- Function: make coding and repository investigation decisions from user goals, real workspace state and returned tools/results.
- Disturbance / variety regulated: source unknowns, code errors, tool failures, user changes, model uncertainty, tests/diagnostics and delegated work outcomes.
- Decisive decision or feedback right: select file/tool actions, revise edits, launch bounded children and respond to actual observations.
- Decision owner: the main Ambient model-backed Agent, plus separately model-driven child agents within assigned read-only or writable mandates.
- Supporting / enforcement mechanisms: compiled tool registry, permission/risk classifier, memory and context, model-controller lane, executor, session persistence, abort/budget limits and human confirmation.
- Closure path: task/prompt + repository context → model-selected tool or delegation → first-party file/shell/tool execution → observed result/report → model revisions or completion.
- Boundary reachability: normal `ambient` CLI wires first-party Agent with project tools and the advertised subagent tool; the child tool invokes actual `new Agent(...).run(...)` with scoped context and returns observed effects to the same parent.
- Why this is / is not agent-owned: choosing code edits and investigative responses needs model discretion; deterministic permissions and runtime cannot perform these decisions alone.
- Evidence: [Agent runtime](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/agent.ts), [built-in child tool](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/agent/subagent-tool.ts), [tool registry](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/agent/registry.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no live model-effectiveness claim; read-only/oracle and builder tools have distinct capabilities and approval paths.

## S2 — Coordination

- State: C
- Function: stabilize simultaneous independently acting worker S1 units competing for the operator's single question/approval resolution channel.
- Disturbance / variety regulated: two builder children asking approval concurrently would each overwrite the same parent prompt resolver or strand a promise; independent child questions similarly collide at the user interaction endpoint.
- Distinct S1 units: child `Agent.run` instances within the same `runSubagents` wave, each with separate task, model context, child ID, tool decisions and permission questions.
- Inter-S1 disturbance: simultaneous calls to the shared user-facing approval/question resolver can clobber another worker's outstanding request and prevent a correct answer reaching its author.
- Attenuating coordination relation: a first-party per-wave `approveChain` queues approvals and `askChain` queues questions, while non-asking children continue operating in parallel.
- Feedback into subsequent S1 behaviour: each queued approval/question resolves against its original child tool action, allowing that child to execute or adapt/retry; the result is then included in its normal model/tool loop.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: source directly names and prevents a concrete mutual-interference failure among concurrent children over one scarce interactive decision slot, returning each decision to the correct continuing worker.
- Decisive decision or feedback right: choose how concurrent child approvals are serialized and resumed; shipped order is deterministic, authored by the developer, not renegotiated by another autonomous agent.
- Decision owner: developer-provided first-party approval queue/coordination policy. The main model can choose which tasks to launch but does not autonomously decide the shared-resolver contention policy.
- Supporting / enforcement mechanisms: separate child contexts and task IDs, promise chains, bounded parallel wave workers and role-limited permissions.
- Closure path: concurrent child tool effects request approval → serialized resolver queue → original human decision delivered to each child → child executes/denies and continues with the observed result.
- Boundary reachability: `makeSubagentTool` injects `runSubagents` into normal CLI tools, and its child `Approver`/`AskPort` are replaced with the shipped gated queues; this is not a test-only lock.
- Why this is / is not agent-owned: model agents own their coding actions, but changing the S2 exclusion/ordering rule would require runtime modification or developer composition rather than the model's organizational discretion.
- Evidence: [runSubagents approval/question chains](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/subagent.ts), [CLI subagent instantiation](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/agent/subagent-tool.ts), [question/approval surface](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/tui/prompt-queue.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: attenuates question/approval-slot contention; does not claim general workspace conflict resolution or model negotiation among builders.

## S3 — Inside-and-now control

- State: —
- Function: no independently established whole-current resource/commitment manager with authority to revise a portfolio of S1 commitments beyond composing a current delegated coding wave.
- Disturbance / variety regulated: background child progress, shared user approvals and per-role deadlines are managed for one requested task, not a durable independently accountable multi-mission portfolio.
- Whole-system current view: the TUI sees child started/finished progress, and the main model receives child summaries; it does not receive a separate standing whole-current performance/commitment ledger spanning independent operations.
- Current-control decision scope: the main model selects wave jobs/roles and integrates reports; the user can interrupt or request early wrap-up. Four-way concurrency and per-child time/turn caps are fixed runtime limits, not model-owned global resource bargaining.
- Decisive decision or feedback right: no separate cross-unit current-control decision evidenced beyond initial delegation, ordinary task integration and human interruption.
- Decision owner: model for operational decomposition; human and fixed runtime for approval/limits; no independently demonstrated S3 owner.
- Supporting / enforcement mechanisms: `runSubagents` wave statuses, task records, completion summaries, fixed concurrency caps, soft/hard deadlines and parent cancellation.
- Closure path: child task start → aggregate result into main coding task exists; independent current S1 commitment state → whole-system intervention → revised continuing child commitments is not wired as a separate control path.
- Why this is / is not agent-owned: choosing tasks at one delegation point does not establish whole-current S3; task overview is not a discretionary organizational control loop without returned reallocations.
- Evidence: [child wave and caps](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/subagent.ts), [CLI subagent tool](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/agent/subagent-tool.ts), [runtime Agent](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/agent.ts).
- Basis: structural bounded absence review.
- Confidence: medium.
- Caveats: a team-shaped task can be sizeable; a different broader organization integrating ongoing workspace management might support S3, but no such first-party control return is credited here.

### Absence scope

- Surfaces inspected: main Agent/child wave, background tasks, TUI child status, report aggregation, role budgets, deadline/hurry, session memory and human approvals.
- Plausible first-party paths checked: main Agent as independent S3 manager, wave activity as whole-current status, model role/job selection as resource bargain and operator progress UI as parent S3.
- Why no material first-party path remains: the reviewed shipped mechanisms allocate and summarize one coding task's children or deterministically gate their limits; no distinct ongoing whole-current commitment adjustment loop is wired to their feedback.

## S3* — Complementary audit

- State: A
- Function: provide an optional independent second-opinion read of actual repository artifacts, distinct from the main coding Agent's own narrative and ordinary post-edit checks.
- Disturbance / variety regulated: unobserved design/correctness mistakes or optimistic self-reporting after code changes may escape the author's tool/test account.
- Claim being audited: that proposed or completed project code changes are sound for the requested design/task.
- Ordinary reporting path: main model tools, builder output and current diagnostics/verify scripts return into its usual coding context.
- Complementary access path: the built-in `subagent` tool exposes explicit `oracle` role for review; a separate model-backed child session with read-only file/search tools inspects source directly and reports independent findings. Auto routing selects reviewer-oriented fleet models (without guaranteeing distinct model identity).
- Independence boundary: separate Agent instance/session, own prompt and context and enforced read-only tool set, rather than a rephrased main-agent summary; user-authored extra reviewer scripts or external platform evaluators are not credited.
- Who acts on findings: the parent coding Agent, which receives and may act on the oracle's review summary; oracle cannot mutate files.
- Decisive decision or feedback right: decide what shortcomings the directly observed code has, using model judgment in the separate review mandate.
- Decision owner: the first-party instantiated oracle child model for semantic review, opt-in when the main Agent selects a review delegation.
- Supporting / enforcement mechanisms: role-based tool registry, separate child session/history, `RoutedRole=reviewer`, summary cap, event/progress stream and parent result injection.
- Closure path: existing code → separate read-only oracle's direct file inspection → reviewer-model assessment → returned child report → parent model can revise coding actions.
- Boundary reachability: `oracle` is one of three advertised shipped `subagent` roles, is dispatched through actual `new Agent(...).run`, and read-only permissions are enforced in the child registry; no custom reviewer plugin is required.
- Why this is / is not agent-owned: a separate model chooses semantic review findings; the deterministic read-only rule and output cap enforce isolation but do not make the audit judgment.
- Evidence: [role schema/registry](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/agent/subagent-tool.ts), [actual child reviewer model runner](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/subagent.ts), [reviewer role fleet route](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/reliability/src/pick-best.ts), [system delegation instruction](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/system-prompt.ts).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: optional, not mandatory; no live demonstration or empirical reviewer effectiveness. The oracle may resolve to the same underlying model family as its parent; independence here is context and direct read-only evidence, not guaranteed model-provider diversity.

## S4 — Outside-and-then intelligence

- State: C
- Function: re-evaluate alternative external model capabilities from a changing live inference fleet and accumulated real-request performance before adopting a more suitable model for subsequent coding runs.
- Disturbance / variety regulated: models become cold/unavailable, new candidates appear with differing tool/reasoning/context capability, and experience reveals persistent differences in request success and latency.
- External distinction: the current Ambient live catalogue exposes per-model readiness and advertised capabilities, while local capability records persist observed provider outcomes across earlier requests.
- Future / prospective distinction: a next run/phase may benefit from a different available model; a score ranks alternative candidates from current fleet plus historical success/latency instead of hard-coding one model identity.
- Adaptation option generated: select the highest-scored ready, tool-capable candidate; role-specific planner/executor/reviewer/compactor selectors further specialize the next model choice.
- Path back into current capability / S3: when `requestedModel=auto` or a role is routed, `Agent.resolveModel` applies the selected model and lane to the next model call, and subsequent outcomes update stored performance evidence for future decisions.
- Decisive decision or feedback right: determine which external model-capability option replaces/serves the next coding model run based on reported and learned evidence.
- Decision owner: developer-specified deterministic scoring and role-selection heuristics; no separately agent-owned S4 strategy actor is present.
- Supporting / enforcement mechanisms: Ambient live catalogue, `CapabilityStore`, per-model sampled success/latency and tool-call evidence, model-resolution events, fallbacks and context budgeting.
- Closure path: external fleet states + past request experience → bounded candidate scoring → selected role/default model applied for the next Agent request → outcomes recorded for later re-selection.
- Boundary reachability: CLI injects `makeCapabilityPort`; `runtime Agent` calls `resolveRequestedModel` with its persisted stats and `pickForRole` on `auto` routed work, not merely a developer roadmap or bare library helper.
- Why this is / is not agent-owned: prospective option and adaptation return are implemented, but the decisive scoring policy is fixed TypeScript; an independent autonomous strategy selector/replanner would require additional composition.
- Evidence: [live-catalog scoring](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/reliability/src/pick-best.ts), [future-model resolution and application](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/agent.ts), [persisted learning port](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/agent/capability-port.ts), [run outcome capture](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/failover.ts).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: S4=C is restricted to adaptive **model capability** selection for later operations, not autonomous changes to the product's mission, tools, source or long-range business strategy. Role choice is heuristic, not validated as optimal, and historical outcomes need sufficient samples.

## S5 — Policy and identity

- State: P
- Function: preserve and legitimately revise a session-long ultimate coding objective when new evidence makes its north-star purpose obsolete or inconsistent with subordinate plans.
- Disturbance / variety regulated: tool-level plans or newly revealed constraints might conflict with the durable user-chosen mission; the agent must not silently move its own identity-level objective.
- Identity / ultimate-policy issue: whether to keep or replace the user-defined `--goal`/`/goal` north star that explicitly outranks intermediate plans and governs every subsequent run in this session.
- Ultimate authority in each claimed mode: legitimate human session owner in supported interactive mode. The model can propose a revision but cannot commit an identity-level change; no autonomous S5 mode claimed.
- Return-to-operation path: model `propose_goal_update` → interactive question including reason and proposed purpose → user confirms/edits or declines → only approval emits durable `goal.set` → pinned system-prompt goal and future turns follow the accepted identity. The explicit user `/goal` command also changes the purpose directly.
- Decisive decision or feedback right: accept, reject or rewrite the *session mission itself*, rather than approve one routine shell/edit action.
- Decision owner: human operator/session owner; a model-generated proposal is subordinate and non-binding.
- Supporting / enforcement mechanisms: `ctx.ask` confirmation UI, reducer `goal.set`, session JSONL persistence, compaction goal anchor, next-turn system prompt and child goal inheritance.
- Closure path: conflict with ultimate session purpose → agent proposal → legitimate human edit/confirmation → `goal.set` event → persistent next-turn prompt/children constrained by new user-chosen goal.
- Boundary reachability: `propose_goal_update` is registered as a first-party built-in tool and interactive TUI binds the approval to the live session with durable event return. In headless/no-user mode the proposal explicitly changes nothing, so S5=P is claimed only for supported interactive mode.
- Why this is / is not agent-owned: removing the human owner leaves the proposal without binding effect; the model cannot silently change the goal, so final identity decision belongs to parent.
- Evidence: [first-party goal proposal/approval](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/tools-core/src/tools/propose-goal-update.ts), [goal outranks plans](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/runtime/src/system-prompt.ts), [goal events in interactive session](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/tui/App.tsx), [goal restore](https://github.com/AmbientCrypto/ambient-cli/blob/46dfd8aada3eb73f4446b6b2e3c34c6b3c7a68b9/packages/cli/src/agent/resume-context.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is S5 at the coding **session's purpose** recursion only, not Ambient corporate/OSS identity governance; no session goal means the option remains dormant, and headless operation has no interactive parent return.

## Distributed OSS parent arrangement

The assessed session owner may directly set its purpose, but project maintainers, Ambient's inference-network governance, upstream GitHub commits, commercial branding and independent contributors are adjacent systems. S5=P applies only to the interactive user's first-party session-goal approval-and-return path, not organization-wide governance.

## Self-hosted and non-human modes

User-confirmed S5 goal updates are an interactive mode; headless mode declines goal changes without a real user. The subagent's `oracle` review and model-selection adaptation are optional/role-dependent. No other parent S3/S4 governance mode is inferred from generic approvals or model setting commands.

## Recursion

Main and children are distinct operational cells with genuine model/tool choices. Children use separate contexts and histories but cannot spawn grandchildren and lack separately demonstrated complete metasystems, so tool nesting is not counted as recursion into another full VSM.

## Variety and escalation

Live fleet routing, controller-assisted tool calling, delegated parallel scout/oracle/builder work and tool/code feedback amplify task variety. A shared approval queue, permission policy, child limits and user verification attenuate harmful interference. Optional oracle review supplies complementary direct-file judgment, live-fleet evidence can revise future model capability, and durable purpose disputes must reach the human owner for S5 closure.

## Evidence gaps

- S2=C is limited to actual serialized operator-prompt contention within parallel child waves; it does not establish autonomous inter-worker file conflict arbitration.
- S3 absence is bounded to the lack of an independent standing whole-current commitment-control loop; selecting child roles and collecting summaries are insufficient alone.
- S3*=A is an optional `oracle` model with direct read-only source access and independent context. Reviewer quality, model dissimilarity and real defect detection were not tested.
- S4=C describes only cross-run capability options for auto-model selection from the changing external fleet and learned outcomes, under deterministic policy; it does not imply autonomous strategic product planning.
- S5=P is restricted to the human-owned north-star goal for an interactive session. Ordinary permission approval is not used as S5 evidence.
- This source assessment uses immutable first-party code and deterministic Index scripts, not live LLM/agent/provider/Browser execution or benchmark claims.
