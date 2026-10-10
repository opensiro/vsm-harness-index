---
harness_id: smolcode
project_name: Smolcode
repository: https://github.com/seanpoyner/smolcode
review_ref: e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Smolcode

## Review boundary

- System in focus: Smolcode's first-party executable coding-agent and task-delegation organization, including parent Rust event-driven model/tool loop, separately running bounded child loops, task_batch, optional LLM judge control decisions and project tools.
- Purpose and identity: execute user coding tasks against local repository files and shell/test output using economical configurable models, with optional tool-using specialist delegations and recovery from stalled work.
- Relevant environment: project workspace, model/inference APIs, tool failures, user instructions/permissions, child agent findings and changing code.
- Standard-distribution boundary: executable Smolcode Rust binary and first-party agent/engine/tools/delegation/judge code; LiteForge SDK is a provider/client dependency, not a source of inferred organizational authority. No importing unrelated Python integration host behavior, maintainer CI or test fixtures.
- Credited operating / distribution surfaces: src/agent.rs and src/engine.rs as runnable parent loop, src/delegate.rs for bounded self-contained subagents, src/judge.rs if actually called by the loop, native Tools in src/tools.rs, config and prompts.
- Adjacent first-party surfaces excluded from ownership: example fanout smoke, local research/demo scripts, model provider internals, Python host embeddings without evidence of their wiring, source repo's developer governance and tests.
- First-party operating / deployment modes considered: Rust coding TUI/headless default, plan/build model selection, model tier escalation, task/task_batch child delegates, optional read-only reviewer, LLM preflight and supervised budget/failed-step recovery, user approval/yolo, session persistence.
- Recursion level: one coding-project organization with a model-directed parent S1 coder and independently tool-using children where invoked; separate judge decision may provide bounded metasystem control within a run, but whole-current S3 extent is unresolved.
- Reviewed revision: `e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Smolcode ships a concrete Rust coding agent atop LiteForge's API client. The first-party run_agent loop repeatedly obtains a model response, extracts tool calls, executes native source and shell tools, and reinserts results. The user-selected model can escalate when the same calls repeat, tool errors accumulate or the worker fails to produce a real edit. Configurable plan/read-only and normal build modes restrict tool exposure, and native session state permits continuity.

The `task` and `task_batch` tools dispatch additional real tool-using agents in src/delegate.rs. Each child gets its own bounded model/tool history, agent prompt and specialized permission tool set; batches run up to four concurrent children. They currently share a project root and can include a build (write-capable) child, while some builtins (explore, review) are read-only. There is no evidenced source claim/reservation, conflict-detection feedback or guaranteed isolation across concurrently editing child S1 units. A concurrency cap and reordering collected child answers do not resolve a specific inter-S1 collision; S2 remains uncertain rather than falsely promoted.

Separate from ordinary model-tool execution, src/judge.rs implements a distinct model request against the whole task and a recent-transcript excerpt. When the primary coder appears stuck, reaches its step budget, or would finish after an observed error, it produces `stop`, `continue`, or `redirect` with optional next-step guidance. src/agent.rs applies the verdict: terminate, grant another bounded leg, prompt an altered next operating approach and sometimes escalate the model tier. This is a material decision and feedback path with an independent judgment owner. However, the judge sees one task and a bounded tail, and the contract does not conclusively show a whole-current view or authority over multiple independent operating commitments/resources at the declared multi-agent project recursion; S3 is therefore left unresolved rather than inferred from the word supervisor.

The project also has a read-only `review` child role which can inspect actual source files, an independent model context and a typed return to parent. That is a plausible complementary evidence-acquisition surface, but the standard coding loop does not appear to require a separate review agent's findings before completion, to use review results to govern downstream coding tasks, or to invoke review as an independently owned audit function. The general LLM judge sees the ordinary recent transcript rather than complementary raw code inspection. S3* thus remains unresolved, not a positive from a reviewer label or secondary model call.

Primary source: [src/agent.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/agent.rs); [src/delegate.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/delegate.rs); [src/judge.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/judge.rs); [src/prompts.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/prompts.rs); [src/tools.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/tools.rs); [src/engine.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/engine.rs).

## Operational model

A native coding S1 repeatedly uses real source-edit/shell tools. The selected deployment may spawn tool-using children, collect their findings and use a model supervisor for stalled-step budget decisions. This makes prospective higher-function paths concrete, but positive S2/S3/S3* ownership requires the specific additional interference/whole-current/complementary audit relationships, not simply child counts or component names.

## S1 — Operations

- State: A
- Function: Model-selected repository edit, inspection and test execution in real user project context.
- Disturbance / variety regulated: Unfamiliar code, build errors, tool failures, user requirements and corrective programming observations.
- Decisive decision or feedback right: Select actual file/shell/python tools and decide what to do next after seeing execution results.
- Decision owner: First-party Smolcode model/tool coding loop, with separately model-directed S1 children on delegated tasks where invoked.
- Supporting / enforcement mechanisms: Native Tools dispatcher, LiteForge API client, model tier router, read-only/build tool profiles, permissions and session state.
- Closure path: User task → model tool call → native source/shell tool result → new model context → further coding action or completion.
- Boundary reachability: Shipped headless/TUI invoke the concrete src/agent.rs loop; src/engine.rs and src/delegate.rs implement the owned project and child execution, rather than relying on a different external coding harness.
- Why this is / is not agent-owned: The model makes contingent operational choices; tools, permissions and provider SDK enact bounded decisions.
- Evidence: [src/agent.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/agent.rs); [src/tools.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/tools.rs); [src/delegate.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/delegate.rs); [src/engine.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/engine.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Source verifies machinery, not benchmark task quality or model performance.

## S2 — Coordination

- State: ?
- Function: Potential attenuation of conflicts among genuinely distinct child coding S1 loops, with the material inter-S1 disturbance/closure not established.
- Disturbance / variety regulated: Multiple write-capable children sharing project workspace might race or overwrite changes; model endpoint contention can also affect simultaneous child runs.
- Decisive decision or feedback right: Parent chooses child tasks; native delegate_batch caps concurrency at four and sorts returned answers, without evidence of active source-write interference judgment.
- Decision owner: Model-authored child decomposition and runtime concurrency limiter; no established separately chosen inter-S1 regulatory decision.
- Supporting / enforcement mechanisms: task/task_batch subagents, shared root, read-only specialization, MAX_CONCURRENCY cap and stable result labeling.
- Closure path: Child findings return to parent. Per-file conflict sensing/ownership reservations or separate worktrees that would change subsequent child write behavior are not evidenced.
- Why this is / is not agent-owned: Fanout, worker-role prompts and concurrency caps alone do not satisfy the four Profile S2 witnesses; no inter-S1 conflict-control path is credited.
- Evidence: [src/delegate.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/delegate.rs); [src/agent.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/agent.rs); [src/prompts.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/prompts.rs); [src/permission.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/permission.rs).
- Basis: structural + explicit.
- Confidence: medium for actual child S1 and uncertain for coordination.
- Caveats: Read-only children reduce particular edit hazards, but protection by specialization does not establish a general inter-S1 mutual-adjustment organization without distinct evidenced work-cell interference.

## S3 — Inside-and-now control

- State: ?
- Function: A first-party supervisory model actually regulates the current coding task's continued effort and approach, but whole-current system management across S1 commitments is unresolved.
- Disturbance / variety regulated: Stalled tool loops, repeatedly failed actions, exhausted step budgets and premature claims of completion after errors.
- Decisive decision or feedback right: A separately queried LLM judge chooses stop, continue (extra work budget), or redirect (change approach); this is a real decision, not solely a static enforcement gate.
- Decision owner: Model answering src/judge.rs supervisor prompts, invoked by the first-party coder's exceptional paths.
- Supporting / enforcement mechanisms: Parent MAX_STEPS/MAX_LEGS, transcript-tail construction, verdict parsing, model-tier escalation and status events.
- Closure path: Parent reports task and recent tool transcript to judge → judge selects and explains action → parent actually stops, restarts bounded step budget or appends corrective new instruction → next S1 coding model turn follows changed commitment/approach.
- Why this is / is not agent-owned: A discretionary decision actor is real; whether a task-tail view and per-leg guidance constitute a **whole-current** view and authority over organizational resources at the declared project boundary still needs a separate completeness witness.
- Evidence: [src/agent.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/agent.rs); [src/judge.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/judge.rs); [src/router.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/router.rs); [src/engine.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/engine.rs).
- Basis: structural + explicit.
- Confidence: high for actual decision/return, medium-low for whole-current S3 mapping.
- Caveats: The supervisor label alone does not establish S3; this uncertainty should not be confused with absence of real LLM control.

## S3* — Complementary audit

- State: ?
- Function: Optional independent read-only reviewer subagent could inspect source with a distinct model context, but no default organizational complementary audit/closed corrective return has been reconstructed.
- Disturbance / variety regulated: The coding S1 may omit defects, misreport tests or leave code vulnerable despite claiming completion.
- Decisive decision or feedback right: A `review` subagent can read files and form defect findings as model-generated text; the primary coding actor chooses whether/when to delegate and what to do with the response.
- Decision owner: Potential independent reviewer model invoked through task/task_batch; established standard audit ownership of that actor is not demonstrated.
- Supporting / enforcement mechanisms: Read-only reviewer prompt, own bounded model/tool history and parent aggregation; separate judge fallback only sees normal transcript tail.
- Closure path: If parent delegates a review, child may inspect raw source and send findings back as one tool result; a required independent audit-trigger/verdict leading to enforceable remediation is not shown.
- Why this is / is not agent-owned: The separate reviewer can gain different raw-source access from routine parent reports, but generic delegation is not by itself a protected audit function and automatic return.
- Evidence: [src/prompts.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/prompts.rs); [src/delegate.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/delegate.rs); [src/agent.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/agent.rs); [src/judge.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/judge.rs).
- Basis: structural + explicit.
- Confidence: medium for reviewer capabilities, unresolved for complementary audit function.
- Caveats: The judge is a supervisor on ordinary transcript rather than a raw-artifact complementary auditor, and no specialized audit-to-repair mandate is claimed.

## S4 — Outside-and-then intelligence

- State: —
- Function: No independently owned prospective external environment study and strategic capability adaptation.
- Disturbance / variety regulated: Future code environment, model limitations, vendor changes and user demands might warrant future-oriented options beyond immediate coding task corrections.
- Decisive decision or feedback right: Model routing/classification chooses among a configured model ladder for current task, while session memory and hooks preserve local context; no future-capability investment decision.
- Decision owner: No S4 decision owner evidenced; configuration belongs to operator/developer.
- Supporting / enforcement mechanisms: Tier router, session state, self-repair hints, skill and file context.
- Closure path: Repeated tool errors can escalate the model tier within current task, but there is no future-environment sensing/options and binding capability-renewal choice returned into present organizational operating capability.
- Why this is / is not agent-owned: Retry/escalation is reactive execution regulation, not prospective organizational intelligence.
- Evidence: [src/router.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/router.rs); [src/agent.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/agent.rs); [src/session.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/session.rs); [src/rules.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/rules.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Users can externally retune their model mix or skills, but these choices are outside first-party independent strategic agency.

### Absence scope

- Surfaces inspected: Model ladder, judge preflight/stalled-task logic, sessions, model routing, skills/configuration and native project tooling.
- Plausible first-party paths checked: Future environment scan, prospective alternatives, durable capability investment choice and return to current S3/operations.
- Why no material first-party path remains: All model escalations and corrective planning are reactive to this task, not a closed external-and-then organization.

## S5 — Policy and identity

- State: —
- Function: No constitutive ultimate-purpose policy adjudication actor and binding return for coding organization identity.
- Disturbance / variety regulated: Tool permission, confined workspace and model controls are task-action restrictions rather than identity/policy disagreement.
- Decisive decision or feedback right: User chooses plan/build/yolo and configured permission posture; runtime enforces action guards and workspace boundary.
- Decision owner: External human/operator and deterministic tool policy, not a first-party organizational S5.
- Supporting / enforcement mechanisms: PermissionSet, read-only/ask/allow tool profiles, confined filesystem tools and hooks.
- Closure path: Tool call allowed or denied, config chosen; no autonomous legitimate identity-policy decision returned to guide all subsequent operating units.
- Why this is / is not agent-owned: A restrictive prompt or approval dialog does not confer highest-level governance decision rights.
- Evidence: [src/permission.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/permission.rs); [src/tools.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/tools.rs); [src/config.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/config.rs); [src/engine.rs](https://github.com/seanpoyner/smolcode/blob/e28e550ca985ff3bbbc99ca2f39e7a85955e5bd3/src/engine.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Maintainer release governance and external company policies are different organizational systems.

### Absence scope

- Surfaces inspected: Permissions, tool/workspace confinement, build/plan configuration, prompt/system rules and code-level hooks.
- Plausible first-party paths checked: Legitimate ultimate authority, identity-policy deliberation, ratification and binding return.
- Why no material first-party path remains: All demonstrated policy decisions govern current tool access and user task behavior rather than the coding organization's ultimate purpose.

## Distributed OSS parent arrangement

Public GitHub release workflows and contributors govern Smolcode development, not each user's coding execution. LiteForge SDK is consumed for model APIs and does not transfer its internal organizational decision ownership into Smolcode.

## Self-hosted and non-human modes

Smolcode can run completely within local model tooling or use hosted OpenAI-compatible providers. It can dispatch independent child agents, delegate inspections and consult a separate model judge for exceptional task budget/approach decisions. This mode has genuine non-human decisions but not automatically all VSM organizational functions.

## Recursion

An independently bounded delegated coding child may perform S1 work. Task prompt labels and bounded worker slots do not make the child fully recursive; the selected parent coding-project organization must still demonstrate distinct inter-S1 coordination and metasystem closure for higher mappings.

## Variety and escalation

Tool errors, missing edits or excessive repeats trigger repair hints and model-tier escalation. A separate model judge can revise immediate operating commitment by stop/continue/redirect and return that to the coder, with finite MAX_LEGS. Review child evidence may reach the parent when specifically asked but a native mandatory independent audit protocol remains unresolved.

## Evidence gaps

- Whether the judge's limited transcript/task snapshot is enough of a whole-current view for positive S3 requires controlled source-native witness; this assessment does not claim it.
- Cross-writer S2 conflict damping, rather than generic parallel task cap, was not substantiated.
- Read-only review child gives plausible complementary access but not a demonstrated independent audit mandate and binding remediation.
- No inference about benchmark efficacy or autonomous software engineering quality is drawn from source code alone.
