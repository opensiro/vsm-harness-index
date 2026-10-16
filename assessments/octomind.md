---
harness_id: octomind
project_name: Octomind
repository: https://github.com/Muvon/octomind
review_ref: fceb8cbe970d2ad097e59d266ae915a3ebb43779
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# Octomind

## Review boundary

- System in focus: first-party installed Rust Octomind CLI agent runtime at frozen `fceb8cbe970d2ad097e59d266ae915a3ebb43779`, with built-in out-of-band supervisor, optional specialist delegation, independent verify-gate and opt-in evolution of generated future-session behaviors.
- Purpose and identity: conduct user-directed coding/operational work via local and MCP tools, control progress externally to the specialist loop, verify claims and (when enabled) adapt reusable future capabilities from grounded cross-session evidence.
- Relevant environment: user objective, selected role/tap, local repository/workdir and tools, external model inference, MCP processes, session transcript and runtime action evidence, scope-separated stored lessons, configured generated skills/guardrails.
- Standard-distribution boundary: compiled first-party `octomind` Rust binary and its native session/chat tool dispatcher, supervisor planner/gate/learning/evolution, optional first-party agent delegation and dynamic-capability paths. External `octohub` inference, third-party tap contents, hosted models, installed optional MCP servers and separately operated Octobench are not themselves Octomind's owned organizational functions.
- Credited operating / distribution surfaces: shipped local interactive, piped, daemon and ACP-compatible session modes, native model→MCP-tool feedback loop; enabled supervisor with plan and gate (enabled in `config-templates/default.toml`); configured learning/evolution mode (explicitly **disabled by default**, can be enabled by operator) and its first-party synthesize→shadow→trial→promote/retire feedback to installed skills/guardrails.
- Adjacent first-party surfaces excluded from ownership: published benchmark scores, external tap/role repositories, README demos, developer-only tests and CI, model-provider capabilities, third-party MCP agent orchestration. An optional capability triggered by user-authored configuration is not evidence the main model invented the external component.
- First-party operating / deployment modes considered: ordinary CLI/daemon coding with default-enabled supervisor, completion gate on a specialist `done` claim and runtime evidence, external planner when objective warrants multiple phases, cross-session learning/recall, and opt-in generated-capability evolution. No actual paid model/provider inference, learner promotion or live audit was performed for this frozen source-first review.
- Recursion level: one Octomind session/work-system with separate specialist S1, supervisor current manager and auditor, and optional prospective generated-capability lifecycle. Multiple delegated children are examined for S2, but generic delegation is not automatic inter-S1 regulation.
- Reviewed revision: `fceb8cbe970d2ad097e59d266ae915a3ebb43779` (frozen batch intake #379).
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The single Rust binary ships native model-guided local/MCP tool execution and session control, exposed through interactive, pipe, daemon, WebSocket and ACP interfaces ([README.md](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/README.md), [src/session/chat/session/api_executor.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/chat/session/api_executor.rs), [src/mcp/core/functions.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/mcp/core/functions.rs)). The upstream specialist/tap choice configures a model and tool access, not an imported coding-agent runtime. First-party supervisor functions, by contrast, are coded under `src/supervisor` and invoked from the session executor. Their default enablement is explicit in `config-templates/default.toml` ([src/supervisor/mod.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/mod.rs), [config-templates/default.toml](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/config-templates/default.toml)).

The **external planner** owns a separate structured supervisor model decision interface. The specialist cannot create/advance/revise plan state by tools; it only signals runtime-selected `request`, `phase_complete` or `reassess`. `reconcile_after_actions` collects the current user request, runtime evidence and active plan, asks the supervisor model for an independent `Create/Advance/Hold/Revise/NoPlan` decision, validates it, executes a first-party state transition `sidecar_start/advance/revise` and injects authoritative phase state/hold findings back to subsequent specialist steps ([src/supervisor/plan.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/plan.rs), [src/mcp/core/functions.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/mcp/core/functions.rs), [src/session/chat/session/api_executor.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/chat/session/api_executor.rs)). This is a mode-specific autonomous whole-current decision/return, not ordinary delegated coding or a counter that just prints status. It is selective: answer-only/simple requests skip the plan, and unavailable planner does not assert invented progress.

The **verify-gate** runs on specialist completion claims using a separately tasked supervisor model with user objective, current outputs, runtime ledger, readback evidence and relevant file state. It can request a bounded readback, refute unsupported gaps and return `Pass/Gaps/Indeterminate`; a grounded negative verdict either injects corrective work back into the current specialist loop or produces an explicit unverified/nonconverged handoff. It does not silently accept an unavailable verifier as evidence of correctness ([src/supervisor/gate.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/gate.rs), [src/session/chat/session/api_executor.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/chat/session/api_executor.rs), [src/supervisor/detect.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/detect.rs)).

The **learning path** is more than transcript compression: enabled first-party extraction stores quote- and scope-grounded lessons, and bounded relevance retrieval supplies future sessions. The distinct opt-in **evolution** subpath uses those lessons and verified outcomes to synthesize reusable skill/pipe/guard/hook/validator candidates, perform native/replay checks and persist registry state `Shadow→Trial→Active/Retired`. Shadow matches collect control verdicts without invoking candidate behavior, a trial applies the candidate in bounded future turns and records treatment verdict/cost, and acceptance/rollback is judged against smoothed counterfactual evidence. A promoted skill is bound into future session activation and a validated generated guardrail participates in the first-party runtime. Effectful candidate trials require explicit parent authorization; advisory candidates can progress autonomously after operator enables the evolution feature ([src/supervisor/learning/evolution/synthesize.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/synthesize.rs), [src/supervisor/learning/evolution/runtime.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/runtime.rs), [src/supervisor/learning/evolution/registry.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/registry.rs), [src/session/context.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/context.rs), [src/session/guardrails.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/guardrails.rs)). This is a prospective capability-feedback path, not simply retrieving memories as text.

## Operational model

A user sets the task and role; the main specialist model selects MCP/native tools and receives their observations for subsequent steps. For a complex objective, the first-party external supervisor can decide which phase to pursue and whether evidence supports advancing or revising the plan, persisting that change and returning it as a runtime-authoritative message to the specialist. A specialist claim of completion can be challenged by a separate verifier reading the first-party action ledger and requested readback; its concrete `Gaps` finding becomes re-entry/corrective instruction, while a pass records a verified outcome for subsequent learning.

Across sessions, when evolution is *explicitly opted in* and normal learning/gate evidence is available, an autonomous supervisor-model synthesis creates candidate behavioral artifacts, a separate first-party registry and counterfactual trial select which should become active, and later sessions load those active behaviors. The parent explicitly controls effectful guardrail trials and can approve/reject/roll back generated behaviors. All of these mechanisms are source-confirmed options, not evidence of real-world performance at the frozen source SHA.

## S1 — Operations

- State: A
- Function: execute user objectives through model-directed local/MCP tool actions in an adaptive session.
- Disturbance / variety regulated: unknown source tree, changing command results, failed tests, tool errors, external API responses and task-specific observations.
- Decisive decision or feedback right: model chooses the next tool, argument and work step after receiving prior action output.
- Decision owner: first-party specialist actor in Octomind's session/chat runtime; the selected external model supplies inference, not a separate vendor harness.
- Supporting / enforcement mechanisms: native Rust chat session, MCP call dispatch, role/tool config, session history, guardrails, compression, supervision and provider client.
- Closure path: task→session model request→model tool instruction→MCP/native executor→recorded tool result→subsequent model turn or terminal result.
- Boundary reachability: ordinary installed CLI and piped/daemon session modes enter same first-party model/tool session path.
- Why this is / is not agent-owned: action choices depend on model reasoning about live observations, rather than being only a prewritten deterministic script; policy and tool mediation constrain choices but do not invent them.
- Evidence: [src/session/chat/session/api_executor.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/chat/session/api_executor.rs), [src/session/chat/response/tool_execution.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/chat/response/tool_execution.rs), [src/mcp/core/functions.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/mcp/core/functions.rs), [README.md](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/README.md).
- Basis: source-backed installed autonomous specialist.
- Confidence: high for runnable first-party code structure, not model task performance.
- Caveats: tap-specific tools, hosted model weights and endpoint success are not part of ownership attribution.

## S2 — Coordination

- State: —
- Function: no separately demonstrated first-party inter-S1 interference-attenuation relation within the selected coding-session and optional specialist group.
- Disturbance / variety regulated: nested/dynamic agents can contend for model capacity or shared files; concrete conflicts are plausible but not shown as a closed native feedback relation.
- Decisive decision or feedback right: inter-agent conflict-specific arbitration that changes affected S1 behavior after detecting interference; not established by inspected paths.
- Decision owner: supervisor handles the *whole* session's plan; child delegation and MCP orchestration communicate tasks/results without proven distinctive inter-S1 collision arbitration.
- Supporting / enforcement mechanisms: delegate, MCP agent invocation, monitored tool processes, role constraints, generic authorizer/cost bounds and session/workdir state.
- Closure path: child task/return and supervisor's whole-current plan changes do not independently form an S2-specific conflicting-worker attenuation loop.
- Why this is / is not agent-owned: a plan owner, tool batch authorization, per-role access bounds or generic delegation do not prove shared-resource contention detection and corrective return between separate operational divisions.
- Evidence: [src/supervisor/delegate.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/delegate.rs), [src/mcp/agent/functions.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/mcp/agent/functions.rs), [src/mcp/orchestration/monitor.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/mcp/orchestration/monitor.rs), [src/supervisor/plan.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/plan.rs).
- Basis: bounded negative source inspection.
- Confidence: moderate at selected recursion level.
- Caveats: additional externally configured multi-agent topology might bring S2 evidence, but that would require a concrete first-party collision-specific path and return.

### Absence scope

- Surfaces inspected: local/MCP tool execution, delegation, MCP process monitoring, external supervisor and plan state, model/cost/tool gates.
- Plausible first-party paths checked: child parallelism, delegated task return, process health monitoring, planner holds/revisions and tool authorizer ordering.
- Why no material first-party path remains: observed controls protect or steer the whole session, or generic agent/task execution, rather than regulating proven interference *between separate active S1 units* with an S2-specific feedback-to-workers loop.

## S3 — Inside-and-now control

- State: A
- Function: separate model-based whole-current supervisor of active specialist plan/phase commitments.
- Disturbance / variety regulated: stalled work, unverified phase completion, broken assumptions or changed trajectory within a multi-phase objective.
- Decisive decision or feedback right: external supervisor decides when to create, advance, hold or revise the operative phase plan according to runtime action evidence and original user outcome constraints.
- Decision owner: first-party out-of-band supervisor model planner; runtime validates and applies its structured decision. The specialist does not possess the plan mutation tool.
- Supporting / enforcement mechanisms: plan signals, per-turn preparation, `call_supervisor_json`, `PlanDecision`, `sidecar_start/advance/revise`, injected authoritative plan notes and bounded error latches.
- Closure path: runtime-observed action/phase evidence→external planner decision→persistent current plan transition or evidence-grounded hold→`runtime-plan` note to model-directed specialist→subsequent task decisions occur under revised current phase.
- Boundary reachability: first-party supervisor plan is enabled in shipped default config for qualifying complex tasks; trivial/answer-only jobs intentionally bypass it.
- Why this is / is not agent-owned: distinct model decides actual whole-task phase regulation and returned current commitments, not a fixed progress counter or human-only approval. `A` concerns this documented current-control mode only.
- Evidence: [src/supervisor/plan.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/plan.rs), [src/session/chat/session/api_executor.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/chat/session/api_executor.rs), [src/mcp/core/functions.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/mcp/core/functions.rs), [config-templates/default.toml](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/config-templates/default.toml).
- Whole-system current view: standing instructions, original task, active plan, phase trajectory, evidence ledger and outcome conditions, beyond a single pending model tool call.
- Current-control decision scope: choose and revise current task phase commitments and prevent unjustified advancement despite specialist claims.
- Basis: source-confirmed distinct autonomous supervisor decision/return.
- Confidence: high for structural ownership and default enablement, without live demonstration.
- Caveats: planner intentionally declines simple requests, failed model calls can leave bookkeeping unchanged, and no autonomy is imported from a third-party agent.

## S3* — Complementary audit

- State: A
- Function: out-of-band supervisor-model verification of producer specialist's claimed done/completion against independent runtime action evidence and artifacts, with returned corrective work.
- Disturbance / variety regulated: false completion, missing tests, unsupported work claims and regressions hidden by optimistic specialist narration.
- Decisive decision or feedback right: separately tasked verifier determines `Pass/Gaps/Indeterminate`, with challenged findings able to prevent verified completion and re-enter correction.
- Decision owner: distinct Octomind supervisor verification model invocation (not the specialist's own status token); first-party runtime owns the binding verdict gate and reentry budget.
- Supporting / enforcement mechanisms: runtime action ledger, readback output, task/claim, ground-truth Git state, structured decision schema, independent refutation, bounded reentry and learning outcome labels.
- Closure path: specialist self-reports done→first-party runtime captures actions/artifacts→separate supervisor verifier judges them→`Gaps` returned to specialist for bounded correction or explicit unverified outcome; `Pass` finalizes verifiable claim/plan and logs verified outcome.
- Boundary reachability: enabled supervisor/gate in packaged default TOML, called at qualifying actual completion claims in the session executor; not off-box CI or benchmark scoring.
- Why this is / is not agent-owned: distinct model performs substantive correctness judgment with access to runtime-owned evidence not controlled by producer, rather than mere transcript logging or same-agent self-review.
- Evidence: [src/supervisor/gate.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/gate.rs), [src/session/chat/session/api_executor.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/chat/session/api_executor.rs), [src/supervisor/detect.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/detect.rs), [config-templates/default.toml](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/config-templates/default.toml).
- Claim being audited: requested coding task is actually completed and outcome conditions hold.
- Ordinary reporting path: specialist `done` token, user-facing summary and tool outputs.
- Complementary access path: separate supervisor builds task/evidence packet from session action ledger, Git state and tool readbacks; can independently request missing output.
- Independence boundary: independent role/model call and runtime-furnished ledger rather than specialist self-report, though same configured model-provider infrastructure may serve both.
- Who acts on findings: runtime applies completion gate, new specialist correction prompt or unverified handoff; successful gate finalizes plan and supplies outcome credit.
- Basis: source-confirmed agent decision and binding first-party corrective return.
- Confidence: high for wired audit constructor, live model quality untested.
- Caveats: abstention/timeout is not evidence of passing; no claim that an independent reviewer actually ran in this assessment.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: when operator enables optional evolution, external and cross-session observations are synthesized into proposed changes of future-session skills/guardrails; first-party counterfactual evaluation determines trial/promotion/retirement of generated behavior.
- Disturbance / variety regulated: recurrent user constraints, observed repeated failure patterns, newly learned project rules and changed usefulness/cost of optional capabilities across future sessions.
- Decisive decision or feedback right: separate supervisor model may autonomously synthesize an advisory skill candidate from grounded lessons; a first-party counterfactual trial judges whether activating it improves future outcomes, promotes an effective candidate or retires weak/regressed behavior. Parent controls enablement, effectful trials and explicit approval/reject/rollback.
- Decision owner: detached learning supervisor plus native promotion/pruning policy own the autonomous S4 path; operator supplies initial opt-in and effectful authorizations, so supplementary parent `(P)` is explicitly recorded. User approval is not confused with autonomous model judgment.
- Supporting / enforcement mechanisms: source-quote and outcome-grounded `Lesson`, per-project store + scope, `synthesize_after_extraction/synthesize_store_if_due`, schema verification/replay checks, candidate registry, `Shadow→Trial→Active/Retired`, held-out counterfactual control/treatment, `init_for_session` and generated skill/guardrail runtime merges.
- Closure path: verified previous-session evidence→deduped reusable lessons→separate supervisor chooses a capability candidate→native schema/replay validation→shadow sample of future tasks without application→gated live treatment with counterfactual results→promoted skill/guard accessible to new sessions (or retired candidate)→actual future behavior changes and continues receiving evidence.
- Boundary reachability: this is installed first-party `[supervisor.learning.evolution] enabled = true` mode, **off by default**, with code from extraction to runtime activation; no unpublished external R&D process or user-installed extension is required. Effectful guards need explicit operator authorization; advisory promotion can be autonomous once opted in.
- Why this is / is not agent-owned: prospective hypothesis/capability selection is produced by a model outside an individual current-task coding loop, then evaluated and fed back into later operational capabilities. It is not mere text-only memory recall or compaction. Both autonomous and parent-governed decisions have distinct documented roles.
- Evidence: [src/supervisor/learning/evolution/synthesize.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/synthesize.rs), [src/supervisor/learning/evolution/runtime.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/runtime.rs), [src/supervisor/learning/evolution/registry.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/registry.rs), [src/supervisor/learning/extract.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/extract.rs), [src/session/context.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/context.rs), [config-templates/default.toml](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/config-templates/default.toml).
- External distinction: observations gathered across past sessions and project/role boundaries rather than an in-flight same task's tool result.
- Future / prospective distinction: choose whether a machine-generated reusable skill/guard should persist as available behavior for later tasks.
- Adaptation option generated: scope-bounded, verified native skill/guardrail candidate with a registry identity and explicit artifact path.
- Path back into current capability / S3: runtime `init_for_session` loads active generated skills and merges validated guardrails; promotion/retirement changes subsequent specialist behavior while gate/plan continue regulating current work. The operator may approve effectful candidates or revert the registry state.
- Basis: first-party optional autonomous skill-generation→trial→activation and bounded parent rights.
- Confidence: medium-high for source-confirmed pipeline; actual learning benefit not measured.
- Caveats: evolution disabled in default config; without activation/grounded lessons or enough verified samples no positive rollout occurs. Distinguish confirmed code path from successful on-device trial. Parent permission for effectful native behaviors is mandatory.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Detached supervisor model plus native shadow/trial evaluation controller | Evolution enabled; grounded stored learning records and verified cross-session outcomes support a candidate | Advisory candidate synthesized, validated, trialled against control and promoted to active skill for later sessions, or retired after negative evidence | [src/supervisor/learning/evolution/synthesize.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/synthesize.rs); [src/supervisor/learning/evolution/runtime.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/runtime.rs) |
| Parent (`P`) | Operator enabling evolution and approving effectful behavior or rollbacks | Candidate entails effectful guard/hook/pipe execution or human decides to reject/change an active artifact | Native registry requires explicit authorization before effectful candidate can leave shadow; operator can approve/reject/retire/rollback the generated behavior | [src/session/chat/session/commands/learning.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/chat/session/commands/learning.rs); [src/supervisor/learning/evolution/runtime.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/runtime.rs) |

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct legitimately constituted ultimate identity and organizational-purpose policymaker beyond scoped user/role constraints within an Octomind session.
- Disturbance / variety regulated: tool misuse, role conflicts and evolved guardrail risks are addressed by operator instructions, bounded security policy and optional supervisor authorizer but do not constitute a separate S5 mandate.
- Decisive decision or feedback right: interpret and resolve top-level organizational identity, constitutional purpose and ultimate contested policy with binding return to S3/S4; not established.
- Decision owner: external operator provides objectives/configuration, first-party security controller enforces those constraints, supervisor authorizer may optionally judge specific tool intent.
- Supporting / enforcement mechanisms: role settings, hard guards, user-intent authorizer, command confirmation, generated-effectful authorization and user approval.
- Closure path: a disallowed tool can be blocked, but no separately chartered ultimate organization policy/identity judgment returns to govern system aims; parent S4 guard approval does not create one.
- Why this is / is not agent-owned: policy-as-code and delegated parent permissions are not sufficient to demonstrate a legitimately differentiated S5 above the task supervisor.
- Evidence: [src/supervisor/authorizer.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/authorizer.rs), [src/session/guardrails.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/session/guardrails.rs), [src/config/mod.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/config/mod.rs), [src/supervisor/learning/evolution/runtime.rs](https://github.com/Muvon/octomind/blob/fceb8cbe970d2ad097e59d266ae915a3ebb43779/src/supervisor/learning/evolution/runtime.rs).
- Basis: bounded negative.
- Confidence: medium.
- Caveats: a user or adopting organization might own external S5, but that is not a first-party installed control loop at this recursion.

### Absence scope

- Surfaces inspected: supervisor authorizer, role and user instruction scopes, native guardrails, config, generated guard approval, external planner/verification and skill lifecycle.
- Plausible first-party paths checked: legitimate role/user permission decisions, tool authorization, human approval of effectful generated changes, configurable specialist identity and external maintainer project rules.
- Why no material first-party path remains: each remains task-level authority or existing policy enforcement; no separate overarching identity-purpose adjudication and authoritative return is established.

## Evidence gaps

- No model-backed live coding, separate verifier case or cross-session candidate trial was executed as part of this source-first assessment; confidence is limited to first-party wired capabilities and explicit frozen code, not observed performance.
- Stronger S3 and S3* claims are based on the actual independent supervisor planner and verification code paths with default enablement, not merely naming files `supervisor` or `gate`. Qualifying complex plan and completion claim still determine invocation.
- Strong S4 is specifically gated by opt-in evolution; plain learning/memory by itself would not prove it. Counterfactual `Shadow/Trial/Active/Retired` and loaded changed behavior are the decisive evidence. Effectful candidates require parent authorization.
- Generic delegation, specialist/model routing and tool monitor do not by themselves prove independent inter-S1 S2 interference regulation.
- Hosted octohub model, dynamic outside tap role content, and published Octobench leaderboards are not credited as first-party functions or outcome evidence.

## Conclusion

Frozen Octomind owns native autonomous model/tool coding operations (S1=A); no qualifying inter-S1 interference S2 is established; a separate model-backed external plan manager has actual whole-current decision/return authority for qualifying tasks (S3=A), and an independent completion verifier returns evidence-grounded findings and correction (S3*=A). A distinct opt-in long-horizon learning-evolution mechanism selects, trials and promotes generated future-session skills/guards (S4=A(P), effectful cases parent-governed); policy enforcement does not establish ultimate identity S5. Source-first proposed vector: **A / — / A / A / A(P) / —**; canonical status requires separate Index admission.
