---
harness_id: operant
project_name: Operant
repository: https://github.com/ishan-parihar/operant
review_ref: fb1777e9b5510448e5680011f8992281af422ff2
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Operant

## Review boundary

- System in focus: The first-party Rust `operant` CLI/TUI/core agent runtime, including its opt-in persistent kernel, self-directed development runner and native subagents.
- Purpose and identity: Terminal-based AI coding/work assistant with tool loops, durable memory, skills, channels, local execution and optional automation.
- Relevant environment: User goals, source tree/TODO.md, tool and provider outputs, browser/MCP responses, test failures, evolving skill usage and operator permissions.
- Standard-distribution boundary: Open-source Operant binary/core, CLI, bundled skill installation and first-party optional modules at the frozen revision. A separately installed Holon organization kernel and any private boundary overlay are explicitly outside the assessed native operating whole.
- Credited operating / distribution surfaces: `crates/operant-core/src/agent`, tools and verification, `crates/operant-cli/src/autonomous.rs`, `curator`, `crates/operant-os` adapter surface and documented opt-in kernel path.
- Adjacent first-party surfaces excluded from ownership: Third-party model providers, imported skills (including ponytail), Holon kernel policy/work databases/decision workflows, private overlay, developer audits, fixtures and repo maintainers.
- First-party operating / deployment modes considered: Interactive chat, one-shot CLI, delegated subagent tasks, scheduled/autonomous TODO-mode, post-turn skill/memory review, opt-in kernel_refine, and Holon client adapter (as an external-system interface only).
- Recursion level: One running Operant task agent and optional delegated children; an external Holon organization, if installed, is not assumed part of the same evaluated system.
- Reviewed revision: `fb1777e9b5510448e5680011f8992281af422ff2`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`OperantAgent` owns a ReAct loop over model requests and JSON-schema tools, with context/memory retrieval, retries and permission/error handling. A subagent tool can dispatch a bounded child task and return its output. The separate `operant autonomous` CLI runner wakes on a timer, feeds pending TODO items and prior failure status into the same main agent, runs project verification and publishes changed artifacts only when the configured checks pass. A post-turn background review model may update local skills and memory; optional kernel auto-learning extends that pathway to prompt/subagent notes. The `operant-os` crate exposes a read-only versioned API, run supervisor and Chair-channel proxy for a separately installed Holon kernel. It invokes Holon's own CLI/authorization, does not implement that organization's decision processes and must not donate their VSM ownership to the standalone Operant distribution.

## Operational model

The acting model chooses tools and sequential tasks, with optional child delegation. Deterministic checks and a human permission envelope bound current execution. Skill lifecycle/lesson distillation adapts remembered procedures and prompts after completed sessions, but the reviewed source does not establish a separate externally oriented prospective strategy owner. Mixture-of-Agents reference calls see a flattened advisory transcript rather than complementary independent execution evidence. Holon's organizational stage agents, policy decisions and Chair constitutional channel are out of boundary without an evidenced same-system composition.

## S1 — Operations

- State: A
- Function: Convert user/TODO requests into iterative tool, code and subtask actions and revise after observations.
- Disturbance / variety regulated: Changing workspace, API/tool failures, deadlines/budgets, failed tests, memory/context gaps and interruption.
- Decisive decision or feedback right: Select subsequent tools/code work, invoke a subagent, retry or finish based on observed results.
- Decision owner: Operant's main model actor; optional native child model handles its own bounded delegated work.
- Supporting / enforcement mechanisms: Tool registry, ReAct runtime, memory prefetch, tool/result healing, user approvals, event and verification ledger, TODO autonomous driver.
- Closure path: User or TODO goal → model chooses action → guarded tool or child execution → feedback and updated task/context state → subsequent model decision.
- Boundary reachability: `operant chat`, `operant run --query` and `operant autonomous` are documented first-party CLI modes built on the same core `OperantAgent`; optional subagents are shipped tool implementations.
- Why this is / is not agent-owned: Substantive next-step selection belongs to the model, while CLI, tests, deadlines and permissions constrain or schedule its choices.
- Evidence: [README operating modes](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/README.md), [model loop](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/agent/run.rs), [agent/subagent contracts](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/agent/mod.rs), [autonomous TODO driver](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-cli/src/autonomous.rs).
- Basis: structural.
- Confidence: high.
- Caveats: No real hosted model call, external channel session or autonomous publishing run was reproduced in this review.

## S2 — Coordination

- State: —
- Function: No separately owned inter-S1 interference attenuation loop demonstrated at the native Operant task boundary.
- Disturbance / variety regulated: Potential conflicts or duplications between delegated subagent tasks.
- Decisive decision or feedback right: No S2-specific cross-agent conflict decision right established.
- Decision owner: No qualifying coordination owner distinct from ordinary parent S1 task decomposition.
- Supporting / enforcement mechanisms: Bounded child delegation, model-call parallelization, batch tool safety checks and persistent kanban/TODO task views.
- Closure path: A child returns work to the ordinary parent model; no separate cross-S1 conflict witness and corrective work-allocation path is established.
- Why this is / is not agent-owned: A task list, a subagent spawn or parallel model advice does not itself regulate resource interference between independently viable units.
- Evidence: [agent and delegation](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/agent/mod.rs), [parallel execution gate](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/agent/run.rs), [single-agent autonomous driver](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-cli/src/autonomous.rs).
- Basis: structural.
- Confidence: medium.
- Caveats: External Holon role/task scheduling is not owned by the standalone Operant implementation; custom skills might implement coordination but are not credited.

### Absence scope

- Surfaces inspected: Core native delegation, Mixture-of-Agents, autonomous runner, kanban and Holon supervisor bridge.
- Plausible first-party paths checked: Child tool calls, parallel batches, TODO state, read-only org view and external stage scheduler.
- Why no material first-party path remains: Native paths decompose/sequence one current task; the external organization owns any cross-employee policy and interference logic.

## S3 — Inside-and-now control

- State: —
- Function: No separately operated whole-system current control function evidenced within the chosen task-agent boundary.
- Disturbance / variety regulated: Aggregate workload, acceptance failures, capacity and policy breaches of multiple S1 units.
- Decisive decision or feedback right: The autonomous CLI can pause and test one agent's work; no distinct manager commands a portfolio of S1 units.
- Decision owner: No qualifying S3 model/parent owner inside Operant; external Holon is outside the reviewed same-system boundary.
- Supporting / enforcement mechanisms: Test-command gate, failure fingerprint, paused status, permission mode, Holon run-lease supervisor adapter and read-only organization views.
- Closure path: Failing test changes the next single-agent autonomous tick; Holon supervisor `prepare`/`heartbeat`/`finish` relays an outside kernel's stage decisions, not an Operant management judgment.
- Why this is / is not agent-owned: A self-directed development loop that retries one task is S1 regulation; process/lease management is mechanical execution, with organizational current control delegated to a separate kernel.
- Evidence: [autonomous control](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-cli/src/autonomous.rs), [external supervisor protocol](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-os/src/supervisor.rs), [external read API](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-os/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: The external kernel may have S3, but the available public Operant-only evidence cannot be turned into an asserted integrated whole.

### Absence scope

- Surfaces inspected: Autonomous status/validation/commit mode, verification ledger, Holon `api_*` reader, stage dispatch and run heartbeat.
- Plausible first-party paths checked: Paused failure loop, per-seat policy gate, org state views, concurrency cap and lease expiration.
- Why no material first-party path remains: Local controls target one S1's quality and safety; Holon's decisions remain in a different independently administered component.

## S3* — Complementary audit

- State: —
- Function: No first-party independent task-finding → author correction → re-review closure shown.
- Disturbance / variety regulated: False claims that code changes are correct or safely integrated.
- Decisive decision or feedback right: No separately owned independent audit verdict over the current author output.
- Decision owner: No qualifying S3* runtime reviewer; a background review model curates skills and memory rather than validating the submitted artifact.
- Supporting / enforcement mechanisms: Build/test/start verification recipe, output guardrails, unit tests, Mixture-of-Agents advisory opinions and post-turn background skill/memory reviewer.
- Closure path: Verification supplies pass/fail to the acting S1 or its autonomous driver; advice and lessons influence a subsequent session without an independent auditor's findings-to-correction contract.
- Why this is / is not agent-owned: Test recipes are deterministic and MoA advisers receive the acting transcript, not independent raw execution reality; the background reviewer edits lessons, not the reviewed patch.
- Evidence: [verification recipe/runner](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/verification.rs), [MoA reference limits](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/moa.rs), [background reviewer](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/agent/background_review.rs), [turn-finalizer](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/agent/turn_finalizer.rs).
- Basis: structural.
- Confidence: medium.
- Caveats: External Holon verify-stage results are not evidence of an independent first-party Operant reviewer in the selected boundary.

### Absence scope

- Surfaces inspected: Deterministic verification, background review cadence and tool allowlist, MoA advisor prompts, branch tests and external Holon verify schema.
- Plausible first-party paths checked: `verify_task`, skill/memory review, multi-model analyst synthesis, run checks and kernel-stage verifier.
- Why no material first-party path remains: No first-party complementary reviewer has separate access to the candidate artifact and a prescribed returned correction/re-audit loop; external verification orchestration is not imported.

## S4 — Outside-and-then intelligence

- State: —
- Function: No distinct external-and-prospective organizational intelligence function established.
- Disturbance / variety regulated: Future capability mismatch with changing outside environment.
- Decisive decision or feedback right: No model-owned prospective option selection and return into system capability at the assessed organizational level.
- Decision owner: Background curator/review model updates operational lessons; no S4 strategy decision owner established.
- Supporting / enforcement mechanisms: Skill usage/staleness-based curator, LLM skill consolidation, post-turn skill revision, opt-in kernel prompt/subagent lesson refinement and external integration updates.
- Closure path: Completed turns can trigger skill/memory or prompt-lesson edits; these retrospective procedural updates lack a separately observed future-environment intelligence/option evaluation loop.
- Why this is / is not agent-owned: The background model has local adaptive agency, but learning from completed tool errors or consolidating stale skills is not automatically the VSM outside-and-then intelligence function.
- Evidence: [background learning](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/agent/background_review.rs), [curator](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-core/src/curator/mod.rs), [opt-in kernel description](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: This is an explicit boundary distinction, not a denial that the product can learn new skills or change future prompt behavior.

### Absence scope

- Surfaces inspected: After-turn self-evolution, `kernel_refine` prompt/subagent lesson lane, curator reviews, skill marketplace refreshes and MoA analysis.
- Plausible first-party paths checked: User-correction-driven skill edit, skill consolidation, local instruction adaptation and model advice.
- Why no material first-party path remains: These respond retrospectively to S1 history or user configuration, without a separate externally informed future-strategy decision-and-return path.

## S5 — Policy and identity

- State: —
- Function: No self-contained ultimate-policy/identity arbitration loop at the standalone Operant boundary.
- Disturbance / variety regulated: Disputes about legitimate ultimate purpose and who may revise the governing charter.
- Decisive decision or feedback right: No native final charter authority; human configuration sets permissions and external Holon Chair decisions belong to Holon's kernel.
- Decision owner: Ordinary operator for settings; the actual external Holon Chair/kernel, if installed, is not an Operant-owned S5.
- Supporting / enforcement mechanisms: Seat policy scopes, native tool approval and refusal, Chair sender verification/command relay, read-only Holon API client.
- Closure path: Operator config restricts tools; Chair identity message can be forwarded to external `holon plan approve/reject`, but the legitimate ultimate-policy decision itself is not made by Operant.
- Why this is / is not agent-owned: Protected chair channels and per-employee budgets are concrete authorization interfaces, not proof of an Operant identity constitution or model-owned S5 decision process.
- Evidence: [Chair channel adapter](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-os/src/chair.rs), [Holon client boundary](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-os/src/lib.rs), [org mode boundary README](https://github.com/ishan-parihar/operant/blob/fb1777e9b5510448e5680011f8992281af422ff2/crates/operant-os/README.md).
- Basis: structural.
- Confidence: high for exclusion of borrowed ownership, medium for native absence.
- Caveats: A separate assessment of an independently sourced, explicitly integrated Holon+Operant deployment could establish a parent-assisted S5 arrangement; that is not this source boundary.

### Absence scope

- Surfaces inspected: Native user permission modes, seat policy wiring, external Holon Chair identity dispatcher and published `operant-os` boundary docs.
- Plausible first-party paths checked: Operator approvals, Chair-channel `approve/reject` relay, token isolation and policy/seat enforcement.
- Why no material first-party path remains: The ultimate authority is external or configuration-only; no native identity dispute → legitimate decider → governing policy return is supplied by Operant alone.

## Distributed OSS parent arrangement

`operant-os` is a client/runtime adapter to Holon, which owns stage dispatch, policy records, grant ledger and Chair authority. The public source identifies an external kernel API and explicitly refers to a private boundary overlay not present in this repository. No private artifact or assumed kernel behavior is used to claim S3/S4/S5 for Operant. This is not a statement that a full Holon deployment lacks these functions.

## Self-hosted and non-human modes

Local/remote models, TUI, gateway channels and timers enter the same model/tool S1. Autonomous TODO ticks add persistent scheduling and test gates; optional kernel auto-learning changes procedural resources, not the app's governing identity.

## Recursion

Delegated child tasks are subordinate operational units, but the native code inspected does not evidence an S2–S5 metasystem over them. The external Holon organization is a different boundary, not an implicit inner recursive organ.

## Variety and escalation

The autonomous driver pauses repeated failed state fingerprints until the TODO/git state changes and reports test failures to the next run. Permission denial and human prompts constrain S1; external Holon escalation/Chair channels are not credited as native organizational control.

## Evidence gaps

No provider/model or real Holon deployment was executed. The qualification is first-party source and public distribution interfaces at the frozen SHA. Full organizational composition, private boundary documents and imported custom skills were intentionally excluded; no empirical agent quality, publication safety or independent audit success is asserted.
