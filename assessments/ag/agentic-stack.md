---
harness_id: agentic-stack
project_name: agentic-stack
repository: https://github.com/codejunkie99/agentic-stack
review_ref: 8fd5726aaebbd421b835ad1c71f2c66064b74caf
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# agentic-stack

## Review boundary

- System in focus: the installed `agentic-stack` portable `.agent/` runtime plus its first-party standalone Python agent path, bounded-loop control plane, memory/skills/protocol layer, local data/mission-control surfaces, adapters, and harness-manager lifecycle code at the frozen revision.
- Purpose and identity: preserve a portable local memory/skills/protocol substrate across coding-agent harnesses while supplying a direct standalone model loop and an optional bounded maker/verifier/checker meta-harness with durable state, worktree isolation, budgets, constraints, review and local observability.
- Relevant environment: a user software project, local Git repository and worktrees, model-provider APIs, compatible external coding-agent CLIs, project files/tests, local episodic/semantic memory, scheduled/cron invocations, and operator approval/configuration.
- Standard-distribution boundary: shipped `.agent/` files, `harness_manager`, bundled adapters, standalone Python adapter, loop templates/contracts, local memory/skills/protocols, Mission Control/data-layer/flywheel tooling, installer/upgrade surfaces and their runtime state are inside. Claude Code, Cursor, Windsurf, OpenCode, OpenClaw, Copilot CLI, Gemini CLI, Hermes, Pi, Codex, Autohand Code, Antigravity and custom-agent internals remain separate systems; optional external `codejunkie99/brain`, host schedulers/cron/systemd/GitHub Actions, model-provider infrastructure and user projects do not donate organizational ownership.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `docs/data-layer.md`; `docs/superpowers/specs/2026-07-18-agentic-loops-meta-harness-design.md`; `.agent/harness/conductor.py`; `.agent/harness/llm.py`; `.agent/loops/harnesses.json`; `.agent/protocols/delegation.md`; `.agent/protocols/permissions.md`; `.agent/memory/auto_dream.py`; `adapters/standalone-python/run.py`; `harness_manager/loops/runner.py`; `harness_manager/loops/commands.py`; `harness_manager/loops/worktrees.py`; and `harness_manager/mission_control_server.py` at the frozen revision.
- Adjacent first-party surfaces excluded from ownership: repository-development plans/tests/examples/demo/release packaging; `.cursor/agents` and bundled third-party Cavecrew/Caveman skills when not installed as the assessed operating mode; future v0.20 design material; project contributor governance; optional external Brain implementation; and the internal organizational functions of every external coding-agent CLI or hosted model provider.
- First-party operating / deployment modes considered: the shipped `standalone-python` adapter using `.agent/harness/conductor.py` and configured Anthropic/OpenAI/MiniMax model access; installed `.agent/` overlays for supported external harnesses; bounded `agentic-stack loop` execution with bundled JSON contracts and user-supplied compatible executor/checker profiles; local Mission Control/data-layer observability; and human/operator approval and permissions modes.
- Recursion level: one installed agentic-stack project environment. Autonomous agent sessions or bounded maker runs are the operational cells; multiple bounded runs may coexist as separate cells. External harness organizations above/below those sessions are not inherited merely because adapters connect them to the same `.agent/` files.
- Reviewed revision: `8fd5726aaebbd421b835ad1c71f2c66064b74caf`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Agentic-stack has two materially different execution paths. The lightweight standalone path is first-party: `adapters/standalone-python/run.py` finds the installed `.agent/` root, imports `conductor.run`, and passes a user prompt into the conductor. The conductor builds context from local memory/skills/protocols, calls the configured model through `.agent/harness/llm.py`, and records execution. The model helper directly supports Anthropic, OpenAI and MiniMax APIs. In this mode the model is the autonomous task actor while agentic-stack provides context, constraints, persistence and logging.

The second path is the bounded-loop meta-harness under `harness_manager/loops`. A loop contract identifies a maker profile, optional checker profile, deterministic verifier, worktree isolation, constraints, approval rules and hard attempt/runtime/output/token limits. The runner checkpoints every transition, creates an owned Git worktree for action-capable loops, invokes the maker, inspects changed paths, runs deterministic verification, then optionally invokes a separately named checker profile in a fresh process. Verifier or checker rejection becomes bounded feedback to a later maker attempt; checker escalation pauses for human judgment. Project-wide and per-run stop paths, resume and refusal-safe cleanup preserve lifecycle state.

The bundled loop profiles are intentionally placeholders (`custom-agent run/review/report`). The control plane therefore ships the maker/checker protocol and closure machinery but does not itself supply a concrete autonomous checker or maker CLI for those default profiles. A user can wire a compatible external command-line harness; those external internals remain outside this assessment.

The shared `.agent/` substrate contains four memory layers, progressively loaded skills, permissions/tool/delegation protocols, local telemetry, and a staging-only dream cycle. `auto_dream.py` explicitly performs mechanical clustering/prefilter/staging only and refuses subjective validation or semantic promotion. Candidate graduation/rejection is performed later by the host agent or user-facing CLI. Skillforge and failure hooks can support retrospective self-modification, but the reviewed surfaces do not establish an outside-and-then prospective intelligence loop.

Local data-layer and Mission Control surfaces aggregate harness events, cron records, active-agent counts, reliability, costs and related summaries. Mission Control serves read-only GET projections plus an operations-event ingestion endpoint. The bounded-loop CLI separately provides `status`, per-run cancel and `stop --all`, but that pause flag governs only agentic-stack bounded loop runners; it does not control all external harness sessions represented in the broader dashboard.

## Operational model

The primary S1 operation is autonomous task work by a model-backed coding-agent cell using the installed `.agent/` context, either through the first-party standalone Python adapter or through an external compatible harness wired to the same portable substrate. In the standalone mode, agentic-stack directly closes model choice/action output back to the user/session and logs the result; removing the model leaves deterministic context/logging machinery but no open-ended task decision maker.

The bounded-loop subsystem can create multiple independent operational runs. Each mutating run receives a dedicated branch/worktree and persistent checkpoint. This is a material coordination primitive: concurrent agents are prevented from editing one shared checkout, and the assigned isolated execution root changes where each S1 acts. The coordination decision itself is deterministic first-party machinery rather than agent-owned discretion, while the bundled role profiles still require the operator/developer to supply the actual maker/checker commands; that combination supports a constructor-level S2 classification rather than S2=A.

The checker protocol is likewise function-specific rather than generic extensibility. It requires a distinct profile name, a fresh process, review instructions after deterministic verification, and a structured approve/reject/escalate verdict whose result changes completion/retry/escalation. However the default distribution only names `custom-agent`; it does not guarantee an independently controlled autonomous auditor. The first-party path therefore establishes S3*=C, not S3*=A.

## S1 — Operations

- State: A
- Function: perform open-ended project/task work using the installed portable context, skills and protocols, observe task/environment results, and return an operational result.
- Disturbance / variety regulated: user task ambiguity, project/repository state, tool/model feedback, remembered conventions, skill selection, failures and other task-local distinctions that require non-preenumerated action choices.
- Decisive decision or feedback right: choose the concrete reasoning/action response to the current task within the supplied context and constraints and revise that response from model/tool/project feedback.
- Decision owner: the autonomous model-backed agent actor reached through the shipped standalone Python/conductor mode; external compatible harness agents can occupy the same operational role but are not needed to establish the first-party standalone path.
- Supporting / enforcement mechanisms: context-budget builder; portable memory/skills/protocol files; configured provider selection; execution logging; permissions/hooks; optional recall/search; and adapter/install machinery.
- Closure path: `standalone-python/run.py` receives a task → `conductor.run` builds the first-party system context → `llm.call_model` invokes the configured model actor → the actor makes the task-level response decision → conductor logs success/failure and returns the result to the operating session.
- Boundary reachability: the repository ships `adapters/standalone-python/run.py`, `.agent/harness/conductor.py`, and `.agent/harness/llm.py` as a supported adapter path. It therefore reaches an autonomous model actor without requiring the organizational internals of Claude Code/Codex/other adjacent harnesses.
- Why this is / is not agent-owned: removing the model actor while leaving conductor, context assembly, local files and logging intact leaves no mechanism that makes the open-ended task decision. The deterministic harness supports and records S1; the agent owns the operative discretion.
- Evidence: [`README.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/README.md); [`adapters/standalone-python/run.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/adapters/standalone-python/run.py); [`.agent/harness/conductor.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/.agent/harness/conductor.py); [`.agent/harness/llm.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/.agent/harness/llm.py); [`docs/architecture.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the provider service and model implementation are external infrastructure. This finding credits the shipped first-party adapter/control path that places the model actor in the operational role; it does not inherit provider-side organizational functions.

## S2 — Coordination

- State: C
- Function: attenuate workspace/branch interference among distinct mutating bounded-loop S1 runs by assigning each run an owned isolated Git worktree and retaining that isolation across retries.
- Disturbance / variety regulated: concurrent or overlapping maker runs against one project could collide in the active checkout, overwrite one another's working changes, or make changed-path verification ambiguous.
- Distinct S1 units: separate bounded loop runs, each with its own maker agent process and task-local operational work.
- Inter-S1 disturbance: shared-workspace mutation would couple otherwise independent runs through the same checkout/files; the design explicitly states that separate runs never share a worktree and action-capable loops require isolation because reliable per-run change attribution matters.
- Attenuating coordination relation: `create_worktree()` allocates a unique run-id-specific branch/worktree from the validated repository base; the runner executes that run's maker and verifier in the owned path; other runs receive different paths.
- Feedback into subsequent S1 behaviour: the coordination result is not merely recorded metadata: the owned worktree becomes `execution_root`, so all later maker retries, verifier checks and changed-path policy for that run occur inside the isolated workspace rather than the shared active checkout.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the path is specifically designed to prevent cross-run mutation interference and preserve independent run identity/forensics. It is not credited from generic delegation, a queue, or the shared memory layer.
- Decisive decision or feedback right: select and bind a run to a unique owned worktree/branch so mutating S1 cells do not operate on the same checkout.
- Decision owner: no autonomous coordination owner is shipped for this right. The first-party loop runtime deterministically applies the isolation contract; the operator/developer supplies the maker profiles and initiates the runs.
- Supporting / enforcement mechanisms: run-id generation; repository/common-dir identity verification; safe worktree root checks; unique branch naming; checkpointed ownership metadata; changed-path collection; refusal-safe cleanup.
- Closure path: a mutating loop is started → runner creates/verifies a unique worktree → that path becomes the maker's execution root → retries/verifier/checker remain bound to the same run worktree → independent runs receive separate worktrees, attenuating shared-checkout interference in subsequent S1 action.
- Boundary reachability: the bounded-loop commands, worktree implementation, default L2/L3 worktree contract and checkpoint machinery are shipped first-party and are installed by `loop init`; a user supplies compatible maker commands but does not have to invent the isolation/feedback path itself.
- Why this is / is not agent-owned: removing any autonomous coordinating agent leaves materially the same unique-worktree decision and enforcement. Conversely, the shipped default loop role profiles are placeholders rather than a first-party autonomous coordination actor. The function-specific S2 path is therefore constructor-level `C`, not `A`.
- Evidence: [`docs/superpowers/specs/2026-07-18-agentic-loops-meta-harness-design.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/docs/superpowers/specs/2026-07-18-agentic-loops-meta-harness-design.md); [`harness_manager/loops/runner.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/harness_manager/loops/runner.py); [`harness_manager/loops/worktrees.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/harness_manager/loops/worktrees.py); [`.agent/loops/harnesses.json`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/.agent/loops/harnesses.json).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this S2 witness is specifically the bounded-loop multi-run mode, not the mere fact that many adapter types can share `.agent/`. The current release does not supply an autonomous agent that decides cross-run coordination policy, so the state is intentionally limited to `C`.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control loop is established across the full assessed agentic-stack operational population.
- Disturbance / variety regulated: individual loop budgets, attempts, policy violations, cancellation and approval are regulated; local dashboards summarize activity across harnesses; neither surface closes whole-system resource/commitment/prioritization control over all current S1 cells.
- Decisive decision or feedback right: no actor inside the credited boundary is shown deciding current priorities, resource allocation, commitments, synergy or intervention for the whole heterogeneous set of agent sessions represented by the installed stack.
- Decision owner: none established for S3 at the declared system boundary.
- Supporting / enforcement mechanisms: per-loop attempt/runtime/token/output breakers; per-run cancellation; project-wide bounded-loop `pause-all`; `loop status`; local data-layer dashboards and Mission Control read projections; operator approvals.
- Closure path: no whole-system S3-specific decision-and-return path spans the complete assessed operational population.
- Why this is / is not agent-owned: `pause-all` is a strong operator intervention but it only governs agentic-stack bounded-loop runners, while Mission Control/data-layer visibility also represents external adapter sessions and cron work that the pause path does not control. Per-loop breakers enforce preselected constraints rather than own whole-system managerial discretion.
- Evidence: [`docs/data-layer.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/docs/data-layer.md); [`harness_manager/loops/commands.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/harness_manager/loops/commands.py); [`harness_manager/loops/runner.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/harness_manager/loops/runner.py); [`harness_manager/mission_control_server.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/harness_manager/mission_control_server.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a narrower recursion containing only bounded loop runs could expose operator stop/status control, but this assessment fixes the shipped installed agentic-stack project boundary rather than silently shrinking the system to make a positive S3 witness.

### Absence scope

- Surfaces inspected: bounded-loop runner/commands/checkpoints/breakers; `loop status` and `stop --all`; data-layer monitoring; Mission Control server/API; delegation protocol; permissions/approval rules; standalone conductor.
- Plausible first-party paths checked: `pause-all` as whole-system intervention; Mission Control as current manager; data-layer KPIs as management view; budgets/circuit breakers as S3 ownership; operator approval as current-control authority; delegation thresholds as resource allocation.
- Why no material first-party path remains: the strongest control path (`pause-all`) is scoped to bounded loops, while the strongest whole-suite view includes external harness activity without matching authority over those sessions. Other reviewed mechanisms are task/run-local enforcement or static policy. The required whole-system current view plus current-control authority plus return across the assessed population is therefore not closed.

## S3* — Complementary audit

- State: C
- Function: independently challenge a maker's claim that a bounded software task is complete after deterministic verification, then return approve/reject/escalate findings into retry or completion control.
- Disturbance / variety regulated: false completion, semantically inadequate changes that nevertheless pass deterministic tests, repeated flawed approaches, and cases requiring human judgment.
- Claim being audited: the maker's current attempt satisfies the original task and constraints after the deterministic verifier has passed.
- Ordinary reporting path: maker process result, changed-file list, deterministic verifier stdout/stderr/exit status and checkpoint/event history.
- Complementary access path: a separately named checker profile is launched in a fresh process after verifier success with review instructions and access to the same isolated project state; its structured verdict is parsed separately from the maker result.
- Independence boundary: the first-party protocol requires checker profile name separation and a fresh process, but permits the same underlying binary and ships only placeholder `custom-agent` profiles. Sufficiently independent autonomous reviewer identity/access must therefore be composed by the user/operator.
- Who acts on findings: `runner.py` deterministically maps `APPROVE` to completion, `REJECT` to feedback and another bounded maker attempt, and `ESCALATE`/malformed output to a paused run requiring human judgment.
- Disturbance / variety regulated: maker self-confirmation and semantic defects not captured by deterministic verification.
- Decisive decision or feedback right: issue the complementary semantic audit verdict that determines whether the attempt completes, retries with feedback, or escalates.
- Decision owner: constructor-level only in the standard distribution. A checker agent can own the judgment once a genuinely independent compatible checker profile is supplied; the bundled placeholder does not itself establish that autonomous owner.
- Supporting / enforcement mechanisms: deterministic verifier gate; distinct checker profile key; fresh process invocation; structured verdict grammar; attempt budget; checkpoint/event log; worktree preservation for inspection.
- Closure path: maker attempt → deterministic verifier pass → checker process reviews task/project outcome → `APPROVE` completes, `REJECT` becomes feedback in the next maker prompt, or `ESCALATE` pauses for human judgment → subsequent operation changes according to the finding.
- Boundary reachability: checker invocation, result parsing, retry/escalation closure and the checker role contract are all shipped in the bounded-loop runtime. The missing piece is the independently controlled checker actor/profile, which is intentionally user-composed through the shipped profile schema.
- Why this is / is not agent-owned: the function-specific audit/feedback path exists, but the default `checker` command is a `custom-agent` placeholder and same-binary checker use is explicitly permitted. Agentic-stack therefore cannot claim that the standard distribution itself owns an independent autonomous audit judgment.
- Evidence: [`docs/superpowers/specs/2026-07-18-agentic-loops-meta-harness-design.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/docs/superpowers/specs/2026-07-18-agentic-loops-meta-harness-design.md); [`harness_manager/loops/runner.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/harness_manager/loops/runner.py); [`.agent/loops/harnesses.json`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/.agent/loops/harnesses.json); [`README.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic verification alone is not credited as S3*. The `C` state specifically reflects the first-party checker/audit decision path while preserving the unresolved independence/actor composition boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party externally/prospectively oriented adaptation loop is established that models future environment distinctions, develops options and returns them into current organizational capability.
- Disturbance / variety regulated: the system does learn from past execution, stage recurring patterns, recall memory, flag repeated failures and permit skill rewrites, but those are retrospective/internal learning paths rather than a demonstrated outside-and-then intelligence loop.
- Decisive decision or feedback right: no first-party actor is shown owning a prospective environment/adaptation judgment satisfying the S4 witness at this boundary.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: episodic/semantic memory; staging-only dream cycle; Skillforge/self-rewrite hooks; failure counters; data flywheel exports; dashboards/KPIs; upgrade and skill-manifest machinery.
- Closure path: no S4-specific external/future distinction → option generation → return-to-current-capability loop is established.
- Why this is / is not agent-owned: autonomous agents may use memories or create/update skills during task work, but the reviewed standard distribution does not show a distinct prospective environmental intelligence function whose options are fed back to alter present organizational capability.
- Evidence: [`docs/architecture.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/docs/architecture.md); [`.agent/memory/auto_dream.py`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/.agent/memory/auto_dream.py); [`.agent/skills/skillforge/SKILL.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/.agent/skills/skillforge/SKILL.md); [`README.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the repository contains future-facing design/spec material and an optional data flywheel, but Methodology 0.3.6 does not treat roadmap/design documents, retrospective learning, or future training possibilities as S4 without the operational prospective loop.

### Absence scope

- Surfaces inspected: architecture feedback loops; episodic/semantic memory; dream cycle; candidate review/promotion; skillforge/self-rewrite; failure hooks; data layer; data flywheel; loop retry feedback; upgrade/spec surfaces.
- Plausible first-party paths checked: automatic memory promotion as adaptation; skill self-rewrite as S4; repeated-failure skill rewrite; dashboards/KPIs as environmental intelligence; flywheel artifacts as future adaptation; v0.20 design/spec as prospective modeling.
- Why no material first-party path remains: each operational path is retrospective, task-local, user-triggered or preparatory. None closes the Profile's required external-and-prospective distinction, adaptation-option generation and return into present S3/capability at the declared boundary.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy decision-and-return loop is established for the installed agentic-stack organization.
- Disturbance / variety regulated: permissions, approval-required actions, deny paths, budgets and user preferences constrain operations, but they are static/operator-authored policies or operational approvals rather than S5 identity deliberation and closure.
- Decisive decision or feedback right: no autonomous or parent path is shown receiving an identity/ultimate-policy issue, deciding it as legitimate ultimate authority, and returning that decision to govern subsequent operation as an S5 loop.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: human-owned `permissions.md`; pre-tool-call enforcement; loop constraints/budgets; approval gates; personal preferences; installer configuration; user-controlled feature toggles.
- Closure path: no qualifying S5 decision-and-return path is established.
- Why this is / is not agent-owned: `permissions.md` explicitly says humans edit it and the agent may not modify/bypass it. That makes ultimate constraints externally configured, but static parent authorship and ordinary action approval do not by themselves establish parent-governed S5 under Methodology 0.3.6.
- Evidence: [`.agent/protocols/permissions.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/.agent/protocols/permissions.md); [`docs/superpowers/specs/2026-07-18-agentic-loops-meta-harness-design.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/docs/superpowers/specs/2026-07-18-agentic-loops-meta-harness-design.md); [`README.md`](https://github.com/codejunkie99/agentic-stack/blob/8fd5726aaebbd421b835ad1c71f2c66064b74caf/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a user clearly remains an ultimate authority outside the autonomous task loop and can edit policies, approve sensitive actions or stop work. Those ordinary operator powers are not published as `S5=P` without evidence of a function-specific identity/ultimate-policy matter and closed return path.

### Absence scope

- Surfaces inspected: `permissions.md` and pre-tool enforcement; loop constraints, budgets and approval flow; personal preferences/features; onboarding/install/upgrade controls; memory review protocol; operator stop/cancel paths; repository governance context.
- Plausible first-party paths checked: human editing of `permissions.md` as parent S5; approval-required merges/deploys as S5; project-wide pause as ultimate policy; user preferences as system identity; lesson graduation/retraction as identity governance; installer configuration as policy closure.
- Why no material first-party path remains: all inspected paths are static configuration, operational safety/intervention, task-memory curation or project setup. No standard runtime path establishes an identity/ultimate-policy issue reaching legitimate ultimate authority and returning an authoritative decision that closes S5.

## Distributed OSS parent arrangement

The public repository and maintainer/release process are adjacent project-governance surfaces rather than part of the installed runtime ownership boundary. Users run local agents, local `.agent/` state and local credentials independently. No organization-level distributed parent S3/S4/S5 mode is inferred from multiple contributors or maintainers.

## Self-hosted and non-human modes

Agentic-stack is local-first and operator-controlled. Operator approvals, `stop --all`, permissions edits and local dashboards were inspected for parent-mode implications. They do not justify `(P)` at the declared whole installed-stack recursion because the required function-specific S3/S4/S5 closure is not complete. The standalone model path nevertheless establishes an autonomous S1 mode.

## Recursion

The principal assessed recursion is one installed agentic-stack project environment. Within it, individual model-backed sessions and bounded maker runs are operational cells. Bounded loops can themselves contain maker/verifier/checker roles; those lifecycle roles are not automatically separate viable systems. External coding harnesses and provider organizations remain adjacent recursions. The S2 worktree witness is intentionally scoped to multiple bounded mutating runs at the project recursion.

## Variety and escalation

Agentic-stack attenuates operational variety through memory/context budgeting, progressive skill disclosure, typed permissions/tool protocols, worktree isolation, path gates, deterministic verification, hard attempt/runtime/output/token budgets, checkpoint/resume and structured checker verdicts. Policy violation, malformed checker output, checker `ESCALATE`, budget exhaustion and explicit cancellation/pause terminate or pause the bounded loop rather than silently widening authority. Human approval remains required for configured sensitive actions.

## Evidence gaps

The default bounded-loop `maker` and `checker` profiles are placeholders rather than concrete bundled autonomous CLI implementations. This prevents promotion of S2 or S3* to `A` based solely on the loop control plane. No frozen first-party evidence establishes a whole-suite current-control actuator paired with Mission Control's heterogeneous visibility, or an operational prospective S4 loop, or runtime S5 identity/ultimate-policy closure. If later releases ship concrete independent checker actors, cross-harness current-control authority, or prospective/policy control loops, those would require a new pinned assessment rather than retroactive credit here.
