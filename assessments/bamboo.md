---
harness_id: bamboo
project_name: Bamboo
repository: https://github.com/bigduu/Bamboo-agent
review_ref: eb1151378d513e820f80513c387056fb14f5c664
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: C
autonomy_s5: —
---

# Bamboo

## Review boundary

- System in focus: one first-party Bamboo local agent-runtime deployment at pinned revision `eb1151378d513e820f80513c387056fb14f5c664`, including the main model/tool loop, durable sessions, first-party `SubAgent` child-session organization, skill/memory runtime, Gold/Guardian runtime machinery, permissions and ordinary server execution surfaces.
- Purpose and identity: a local-first Rust AI agent runtime that executes user work through model/tool feedback, persistent state, tools, skills, MCP integrations, memory and optional multi-agent delegation.
- Relevant environment: user objectives and approvals, local/project workspaces, files/processes, configured model providers, web/MCP resources, child-agent outcomes, repeated successful workflows and persisted memory/skill state.
- Standard-distribution boundary: the shipped Bamboo server/runtime, built-in tools/skills and first-party engine/infra crates at the frozen revision. Repository CI/tests, design experiments and source paths that are not activatable from a supported runtime mode may corroborate constructor capability but do not donate out-of-box ownership.
- Credited operating / distribution surfaces: the ordinary root Agent runtime; `SubAgent` model-facing tool and child-session adapter/runtime; root/child session persistence and completion coordinator; built-in child assignment contract; `SkillManager` and repeated-trace reuse-draft collector; standard memory/gardener machinery; ordinary permission/configuration surfaces; and engine Guardian constructor machinery where explicitly classified as constructor rather than autonomous runtime ownership.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI and development-only fixtures; Guardian execution that requires a `guardian_config` activation not exposed by the standard server request path at this ref; arbitrary downstream plugins/MCP servers; user-created artifacts that are not promoted into Bamboo's live skill discovery roots; and future/default-branch changes after the frozen ref.
- First-party operating / deployment modes considered: ordinary root model/tool sessions; background and synchronous child delegation; parallel one-shot or resident child sessions; parent wait policies (`all`, `any`, `first_error`); child update/run/message/cancel control; skill discovery/live reload; repeated-trace reuse-draft generation; Gold goal sessions; memory auto-dream/gardener maintenance; permissions/approval; and the implemented but not server-enabled Guardian constructor path.
- Recursion level: one Bamboo root session/deployment. Root and concurrently executing child sessions are distinct operational units for S2/S3 analysis. Nested child spawning is bounded but is not promoted to a separate viable recursion solely because another model/tool loop exists.
- Reviewed revision: `eb1151378d513e820f80513c387056fb14f5c664`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Bamboo's core operating path is a persistent model/tool runtime. The root model receives task/session context, selects substantive tools, observes their results and continues or concludes. The runtime adds persistence, permissions, context management, memory, skills, MCP/tool surfaces, workflow/schedule integration and execution/recovery machinery without replacing the model's task-specific action choice.

The first-party `SubAgent` tool turns the root model into a live controller over separate child model/tool sessions. A `create` call requires an explicit responsibility and prompt, may select workspace/model/reasoning/lifecycle, and normally starts the child in the background so multiple children can run concurrently. The same root model can list/get children, update assignments, run or rerun them, send steering messages, cancel/delete them, and suspend itself under `wait_for=all|any|first_error`. Child completion is durably folded back into the parent and automatically resumes the parent with the child result.

Bamboo explicitly treats child responsibility as a coordination boundary. The model-facing schema says each responsibility should be narrow and non-overlapping with other children. A child receives that responsibility inside an authoritative assignment frame and is instructed to mutate only the workspace/files/external state allowed by its scope or task brief. This matters because children may run in parallel and, unless a separate workspace is chosen, default to the parent workspace. Status guidance feeds running/stalled/error/completed state back to the root, which can steer, cancel, retry in place or change an assignment. The runtime does not provide a hard per-file write lease, so this is a semantic/model-owned coordination contract rather than deterministic disjoint-write enforcement.

The engine also implements a Guardian adversarial completion-review path. A read-only Guardian child is designed to inspect changed files and recorded diff/test evidence independently, issue an approve/reject JSON verdict, and on rejection resume the parent with concrete findings so it must repair and can be reviewed again. This is a materially complementary audit constructor. At the frozen server execution boundary, however, ordinary execution explicitly passes `guardian_config: None` with a TODO to surface Guardian configuration on the request. The spawner is wired, but the standard server path cannot activate the gate; therefore the path is constructor-owned (`C`), not out-of-box autonomous S3*.

For future capability adaptation, Bamboo's `SkillManager` observes successfully checkpointed root-session tool traces. `ReuseDraftCollector` normalizes successful multi-step tool sequences, counts recurrence across distinct sessions and, once a threshold is reached, emits a proposed `SKILL.md` plus validation artifact. The code deliberately stores these under `reuse-drafts/` beside the configured skill directory and never inside a discovery root. Meanwhile the live skill store scans actual skill roots and starts live reload. Bamboo therefore constructs a prospective adaptation candidate from recurring operational demand but intentionally stops before admitting it into current capability: an S4 constructor path, not autonomous closure.

Memory gardeners split/deduplicate/age/archive durable memories, Gold checks current goal completion, and `update_goal` records current-task complete/blocked status. These support memory quality/current-task regulation rather than establishing a separate additional S4 closure. Permissions, approvals, disabled-tool/skill configuration, user goals and system instructions constrain operation but do not close identity or ultimate-policy authority for S5.

Primary evidence:

- [`README.md`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/README.md) — shipped runtime boundary, model/tool engine, memory, skills, MCP, subagents, workflows/schedules and product architecture.
- [`crates/app/bamboo-server-tools/src/sub_agent.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/app/bamboo-server-tools/src/sub_agent.rs) — model-facing child creation, responsibility/workspace/model choices, parallel background operation, wait policy and live child control.
- [`crates/engine/bamboo-engine/src/session_app/child_session/helpers.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/engine/bamboo-engine/src/session_app/child_session/helpers.rs) — authoritative child responsibility/mutation contract and model-facing status/steering guidance.
- [`crates/engine/bamboo-engine/src/session_app/child_completion_coordinator.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/engine/bamboo-engine/src/session_app/child_completion_coordinator.rs) — wait-policy closure, full child-result return, Guardian verdict parsing and reject/approve resume into the parent.
- [`crates/engine/bamboo-engine/src/runtime/guardian_state.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/engine/bamboo-engine/src/runtime/guardian_state.rs) — independent read-only adversarial reviewer contract, audit evidence boundary, verdict state and bounded review loop.
- [`crates/engine/bamboo-engine/src/runtime/config.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/engine/bamboo-engine/src/runtime/config.rs) — Guardian constructor configuration and late-bound reviewer spawner.
- [`crates/app/bamboo-server/src/handlers/agent/execute/runtime/execution.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/app/bamboo-server/src/handlers/agent/execute/runtime/execution.rs) — ordinary server runtime wiring; Guardian spawner present but `guardian_config: None` with request-surface TODO.
- [`crates/infra/bamboo-skills/src/reuse_draft.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/infra/bamboo-skills/src/reuse_draft.rs) — repeated successful trace observation and review-only future Skill-draft generation outside discovery roots.
- [`crates/infra/bamboo-skills/src/lib.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/infra/bamboo-skills/src/lib.rs) — runtime wiring of reuse-draft observation plus initialized/live-reloaded Skill store.
- [`builtin_skills/skill-creator/SKILL.md`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/builtin_skills/skill-creator/SKILL.md) — user-directed skill creation/evaluation/iteration support, inspected as a plausible S4 path but not used to infer automatic capability closure.
- [`crates/engine/bamboo-engine/src/gardener.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/engine/bamboo-engine/src/gardener.rs) — background memory quality maintenance.
- [`crates/engine/bamboo-tools/src/tools/goal.rs`](https://github.com/bigduu/Bamboo-agent/blob/eb1151378d513e820f80513c387056fb14f5c664/crates/engine/bamboo-tools/src/tools/goal.rs) — current-session goal completion/block status, not identity/ultimate policy.

## Operational model

The root model is the primary S1 owner. When it uses the first-party `SubAgent` tool, separately running child model/tool sessions become additional S1 units. The root model owns the task-specific coordination and current-control decisions over those children: responsibilities, workspace/model allocation, lifecycle, wait policy, steering, retry and cancellation. Runtime code enforces lifecycle/persistence and returns child state but does not replace those decisions.

Bamboo also includes two incomplete metasystemic constructor paths relevant here. Guardian implements the S3* audit relation but lacks a standard server activation surface at this revision. Reuse-draft observation implements S4 opportunity detection and candidate generation but intentionally stops before publishing the candidate into the live skill catalog.

## S1 — Operations

- State: A
- Function: perform user-directed work through a persistent model/tool feedback loop and alter the local/external task environment through first-party tools.
- Disturbance / variety regulated: heterogeneous user tasks, workspace/process state, tool results and failures, model/provider responses, context limits, permissions, memory/skill context and follow-up observations.
- Decisive decision or feedback right: choose the next substantive tool/action and arguments, interpret returned evidence, and decide whether to continue, delegate or conclude.
- Decision owner: the active root Bamboo model actor; a child model separately owns operational choices inside its delegated assignment.
- Supporting / enforcement mechanisms: runtime loop, tool registry/executor, durable session state, permissions/approvals, context compression, memory, skill/MCP surfaces, execution/recovery machinery and child runtime.
- Closure path: user/task/session context → model chooses substantive tool/action → runtime executes/refuses and records result → later model round observes the result → model revises action or returns a final result.
- Boundary reachability: the ordinary Bamboo server/runtime ships this model/tool execution path directly; no downstream component is required to obtain the operational loop.
- Why this is / is not agent-owned: deterministic runtime components execute, persist and constrain actions, but removing the model removes task-specific action selection and interpretation of operational feedback.
- Evidence: `README.md`; `crates/app/bamboo-server-tools/src/sub_agent.rs`; ordinary runtime/engine architecture at the pinned ref.
- Basis: explicit + structural
- Confidence: high
- Caveats: schedules, permissions and memory maintenance support operation but do not own the substantive S1 decision right.

## S2 — Coordination

- State: A
- Function: attenuate interference and redundant/overlapping work among concurrently executing child S1 units by assigning explicit non-overlapping responsibilities and mutation scopes, then steering or correcting children as live outcomes reveal conflicts or stalls.
- Disturbance / variety regulated: parallel children may default to the same parent workspace and can otherwise duplicate work, pursue overlapping responsibilities, modify overlapping state, or continue on a stale/wrong assignment.
- Decisive decision or feedback right: decide each child's responsibility, detailed task, workspace and relevant mutation boundary, and revise/steer/cancel that assignment when child status or outcomes show a coordination problem.
- Decision owner: the root Bamboo model invoking the model-facing `SubAgent` tool.
- Supporting / enforcement mechanisms: required `responsibility` field; schema guidance requiring narrow non-overlapping responsibility; child assignment frame making scope authoritative and restricting mutation to assigned scope; optional separate child workspace; background parallel execution; status guidance; `send_message`, `update`, `cancel`, `wait` and completion feedback.
- Closure path: root model partitions work into explicit child responsibilities/workspaces → child assignment makes that scope authoritative during operation → concurrent children execute → current status/completion/error returns to root → root can redirect/retry/cancel/change scope → later child/root operation follows the revised coordination decision.
- Boundary reachability: `SubAgent` is a standard first-party model-facing root tool and its child assignment/status machinery is wired through the shipped server/engine runtime.
- Why this is / is not agent-owned: Bamboo supplies deterministic lifecycle and persistence, but the task-specific responsibility/workspace split and live redirection decisions are chosen by the root model. Removing the model leaves no equivalent semantic partition of the current job.
- Evidence: `crates/app/bamboo-server-tools/src/sub_agent.rs`; `crates/engine/bamboo-engine/src/session_app/child_session/helpers.rs`; `crates/engine/bamboo-engine/src/session_app/child_completion_coordinator.rs`.
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: Bamboo does not establish a hard per-file disjoint-write lease at this ref; the credited attenuation is the model-owned non-overlapping responsibility/mutation-scope contract plus live steering, so badly chosen scopes can still collide.
- Distinct S1 units: separately persisted root/child model-tool sessions; multiple children may be created in one turn and run concurrently in background.
- Inter-S1 disturbance: concurrent children may share the parent workspace and could duplicate or overlap work/state mutation without explicit task boundaries.
- Attenuating coordination relation: required narrow, non-overlapping model-selected responsibilities plus authoritative per-child scope/mutation instructions and optional workspace separation.
- Feedback into subsequent S1 behaviour: child status/results/errors return to the root; status guidance and `send_message`/`update`/`cancel`/rerun paths let the root alter the affected child's subsequent execution rather than blindly spawning redundant work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is not child spawning or mailbox availability alone; it is explicitly aimed at separating concurrent responsibilities/mutations that can interfere in a shared workspace and closing observed problems through changed child behavior.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current root/child organization as a whole, allocate active child commitments/resources and intervene in live child work.
- Disturbance / variety regulated: changing child portfolio, running/pending/error/completed state, stalls, wrong assignments, model/cost tradeoffs, need for early error response and changing current task commitments.
- Decisive decision or feedback right: create or withhold child commitments; select responsibility, workspace, model, reasoning effort and lifecycle; inspect current children; update/rerun/steer/cancel/delete them; and choose whole-set wait policy before integrating results.
- Decision owner: the root Bamboo model actor.
- Supporting / enforcement mechanisms: `SubAgent.list/get/create/update/run/send_message/cancel/delete/wait`; child index/session persistence; runtime status guidance; wait policy; completion coordinator and automatic parent resume.
- Closure path: root creates current child portfolio → children execute and expose current state/results → root lists/gets or waits on the portfolio → root changes assignments/resources/steering or terminates work as needed → runtime applies the chosen intervention and subsequent operation proceeds under the new commitments.
- Boundary reachability: these controls are available directly to the root model through the ordinary shipped `SubAgent` tool; they do not depend on test/dev orchestration.
- Why this is / is not agent-owned: wait scheduling, persistence and cancellation mechanics enforce decisions, but the root model owns the discretionary allocation and intervention choices over the current child organization.
- Evidence: `crates/app/bamboo-server-tools/src/sub_agent.rs`; `crates/engine/bamboo-engine/src/session_app/child_session/helpers.rs`; `crates/engine/bamboo-engine/src/session_app/child_completion_coordinator.rs`.
- Basis: explicit + structural
- Confidence: high
- Caveats: a simple single-agent run does not exercise S3; the state is established in the shipped multi-child mode. No distinct parent-governed S3 mode was established from the inspected operator/UI surfaces.
- Whole-system current view: `list` exposes the active child roster and `get`/completion/status machinery exposes each child's current or terminal state; `wait` can reason over every active child or an explicit subset under a root-selected policy.
- Current-control decision scope: current child commitments, responsibilities, workspaces, model/reasoning allocation, lifecycle, steering, retries, cancellation/deletion and wait/integration timing.

## S3* — Complementary audit

- State: C
- Function: independently challenge the root agent's terminal completion claim using a separate read-only adversarial reviewer that inspects workspace evidence and returns an approve/reject verdict with findings.
- Disturbance / variety regulated: the executing agent can claim completion despite missed requirements, incorrect changed files, inadequate diff/test evidence, regressions or unverified criteria.
- Decisive decision or feedback right: independently inspect changed files and recorded verification evidence, decide whether stopping is justified, and reject with concrete findings that must be addressed before completion.
- Decision owner: a separate Guardian reviewer model in the implemented constructor path; the ordinary server exposes no activation owner because it passes `guardian_config: None` at this ref.
- Supporting / enforcement mechanisms: read-only Guardian child tool denylist, dedicated adversarial rubric, durable Guardian state, bounded review budget, verdict parser, synthetic reject on malformed/error output, completion coordinator and hidden parent-resume message.
- Closure path: when the constructor is enabled, terminal point → runtime spawns read-only Guardian → Guardian independently reads/searches changed-file and recorded diff/test evidence → verdict is recorded → rejection resumes parent with findings and directs repair → a later terminal point can be reviewed again. The standard server stops before the trigger because Guardian configuration is not surfaced.
- Boundary reachability: the complete S3*-specific machinery and server-provided spawner are first-party and shipped, but `crates/app/bamboo-server/src/handlers/agent/execute/runtime/execution.rs` explicitly supplies `guardian_config: None` with a TODO to expose configuration. A downstream/first-party composition step is therefore still required to activate the audit loop, so the publication state is Constructor rather than Autonomous.
- Why this is / is not agent-owned: the independent reviewer would own the audit judgment once activated; deterministic parsing/resume only enforces its verdict. No standard server run can currently instantiate that ownership mode from the supported request surface.
- Evidence: `crates/engine/bamboo-engine/src/runtime/guardian_state.rs`; `crates/engine/bamboo-engine/src/session_app/child_completion_coordinator.rs`; `crates/engine/bamboo-engine/src/runtime/config.rs`; `crates/app/bamboo-server/src/handlers/agent/execute/runtime/execution.rs`.
- Basis: explicit + structural
- Confidence: high
- Caveats: this is intentionally `C`, not `A`: engine completeness is not enough to borrow an activation path absent from the assessed server mode.
- Claim being audited: the main/root agent's claim that the current task is complete and the run may terminate.
- Ordinary reporting path: main agent reaches terminal completion using its own execution context and recorded work/test evidence.
- Complementary access path: a separate read-only Guardian child with dedicated Read/Glob/Grep/GetFileInfo-style inspection access evaluates the actual changed files plus recorded diff/test evidence rather than trusting the main claim.
- Independence boundary: distinct child session/model context, read-only tool surface, explicit adversarial rubric and separate verdict state; mutation/spawn/shell/web tools are removed.
- Who acts on findings: runtime records the verdict and resumes the root model with concrete findings; the root then repairs/reverifies before another terminal attempt.

## S4 — Outside-and-then intelligence

- State: C
- Function: detect recurring operational demand across distinct successful sessions and construct a candidate reusable Skill for future work.
- Disturbance / variety regulated: repeated successful multi-step workflows remain ad hoc and repeatedly consume reasoning/tool orchestration instead of becoming a reusable future capability.
- Decisive decision or feedback right: recognize that a normalized successful tool sequence has repeated across enough distinct sessions and emit a proposed reusable Skill representation with validation evidence.
- Decision owner: deterministic first-party `ReuseDraftCollector` owns detection/candidate generation; no autonomous or parent actor is wired to admit the candidate into the live skill catalog at this ref.
- Supporting / enforcement mechanisms: successful-root-trace extraction, canonical tool/value-shape normalization, stable signature, distinct-session threshold, review artifact generation, persisted `SKILL.md` candidate and validation examples; separate SkillStore discovery/live reload for actual admitted skill roots.
- Closure path: successful root sessions → repeated normalized trace crosses threshold → Bamboo emits review-only `reuse-drafts/<candidate>/SKILL.md` and validation artifact → **constructor boundary stops here**. The draft is intentionally outside every discovery root, so an additional promotion decision/path is required before later runs can use it as a live Skill.
- Boundary reachability: repeated-trace observation is wired directly into first-party `SkillManager` and produces the candidate without downstream code. Because admission into current capability is deliberately omitted, the shipped path establishes S4 construction but not autonomous or parent-governed closure.
- Why this is / is not agent-owned: candidate detection/generation is deterministic rather than an autonomous S4 actor, and neither the root model nor a first-party parent approval surface is shown owning promotion into live capability. This is therefore `C`, not `A`/`P`.
- Evidence: `crates/infra/bamboo-skills/src/reuse_draft.rs`; `crates/infra/bamboo-skills/src/lib.rs`; `crates/infra/bamboo-skills/src/store/mod.rs`; `builtin_skills/skill-creator/SKILL.md`; `crates/engine/bamboo-engine/src/gardener.rs`.
- Basis: explicit + structural
- Confidence: high
- Caveats: user-directed `skill-creator` can produce and iterate Skill artifacts, and SkillStore live-reloads actual discovery roots, but no first-party reviewed path was found that promotes automatic reuse drafts into those roots. Memory gardeners maintain memory quality rather than providing this missing adaptation authority.
- External distinction: repeated successful root sessions encode recurring user/environment demand across distinct operating episodes rather than one current task; the reuse collector deliberately aggregates across distinct sessions.
- Future / prospective distinction: the generated artifact is explicitly a proposed reusable Skill intended to change how future matching work can be performed.
- Adaptation option generated: a proposed Skill definition/`SKILL.md` plus validation artifact derived from the recurring tool sequence.
- Path back into current capability / S3: not closed at this ref; drafts are intentionally written beside, not inside, the configured Skill discovery root. Promotion into a live-reloaded Skill root requires an additional composition/authority path.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the declared Bamboo deployment boundary.
- Disturbance / variety regulated: Bamboo exposes many task goals, system instructions, permission policies, tool/skill disablement settings and human approvals, but these regulate current actions/capabilities rather than resolving the identity or ultimate-policy questions of the organization itself.
- Decisive decision or feedback right: no qualifying identity/ultimate-policy right and closed return path were established.
- Decision owner: none established for S5 at this boundary.
- Supporting / enforcement mechanisms: system prompts, permission checker/approvals, tool/skill configuration, Gold goal configuration, `update_goal`, runtime budgets and Guardian/skill constructor policies.
- Closure path: no qualifying S5 issue → legitimate ultimate authority → authoritative identity/policy decision → returned operational-governance loop was found.
- Why this is / is not agent-owned: the root model can make task decisions and report goal completion, but it does not own the system's identity or ultimate policy. Operator configuration/approval likewise constrains actions without evidencing S5 closure.
- Evidence: `crates/engine/bamboo-tools/src/tools/goal.rs`; `crates/engine/bamboo-engine/src/runtime/config.rs`; `README.md`; inspected server permission/configuration and skill/memory surfaces.
- Basis: explicit + structural absence review
- Confidence: medium-high
- Caveats: this is a boundary-relative negative finding, not a claim that a larger human/project organization around Bamboo lacks S5.

### Absence scope

- Surfaces inspected: root/child runtime and model-facing tools; child control/completion machinery; Guardian/Gold goal machinery; memory auto-dream/gardeners; SkillStore, skill-creator and reuse-draft adaptation surfaces; permission/approval and runtime configuration; workflow/schedule/product architecture documentation.
- Plausible first-party paths checked: identity/system prompts; `update_goal` and Gold goal authority; human approval/permission gates; live tool/skill policy; Guardian review; user-created Skill iteration; memory maintenance; workflow/schedule configuration and child-controller ownership.
- Why no material first-party path remains: each inspected path governs a task, current action, capability, audit or adaptation artifact. None establishes an identity/ultimate-policy issue that reaches an ultimate authority and returns an authoritative decision governing subsequent operation at the declared Bamboo recursion.

## Recursion

Bamboo permits nested sub-agent execution up to a bounded spawn depth and supports resident children, but spawning depth alone is not VSM recursion. This assessment stays at one root Bamboo session/deployment. Child sessions are operational S1 units inside that system-in-focus for S2/S3 analysis.

## Variety and escalation

Operational variety is handled by model-selected tools, specialized child models, optional separate workspaces, reasoning-level/model selection, skills/MCP, memory and runtime recovery/permission controls. Multi-child variety is absorbed by explicit task partition, parallel execution, root current-control tools and child-result feedback. Human approvals address action permission; they are not reclassified as S5. Guardian and reuse-draft mechanisms demonstrate additional audit/adaptation constructor capacity without borrowing missing activation/promotion authority.

## Evidence gaps

- No hard per-file S2 lease was established; S2 relies on model-selected non-overlapping responsibility/mutation scope plus live steering. A future ref with explicit write-conflict arbitration could strengthen the enforcement evidence without changing who currently owns the coordination decision.
- Guardian has a complete engine-side review/fix/re-review loop, but ordinary server execution pins `guardian_config: None`; a later ref that exposes and enables that first-party mode should be reassessed for `S3*=A`.
- Reuse drafts are intentionally review-only and outside skill discovery roots. A later first-party promotion/approval path into live-reloaded skills could change S4 ownership/closure and should trigger reassessment.
- No qualifying S5 path was found within the reviewed standard distribution; if a future Bamboo governance/identity control surface is added, it requires function-first reassessment rather than inference from generic policy settings.
