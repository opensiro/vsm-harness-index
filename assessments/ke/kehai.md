---
harness_id: kehai
project_name: Kehai
repository: https://github.com/sh1ny/kehai
review_ref: 170d97ae4f89ccda16e513abc4d9a531f8558c38
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-04
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Kehai

## Review boundary

- System in focus: Shipped Dart headless coding-agent engine, RPC client, model tools, job supervisor and role-based child agents.
- Purpose and identity: Execute user programming tasks with verifiable tool effects, persisted session state, optional child work and human tool permissions.
- Relevant environment: Project files, provider responses, shell/job outcomes, role configurations, session journals and user answers.
- Standard-distribution boundary: First-party Dart engine/CLI/RPC, tool roster, session writer, permission/hooks stages, job supervisor, child-agent RPC launch and live M1 sensorium; deferred roadmap designs excluded.
- Credited operating / distribution surfaces: [README](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/README.md), [driver](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/loop/driver.dart), [runtime](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/tools/runtime.dart), [agent](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/tools/agent.dart), [supervisor](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/jobs/supervisor.dart), [job](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/tools/job_tool.dart).
- Adjacent first-party surfaces excluded from ownership: Future sensorium/Nocterm/LSP/jj designs, Dart test fixtures, repository ADR governance and CI, provider internals and optional consumer-authored role/hook policies.
- First-party operating / deployment modes considered: Line client and NDJSON RPC, one coding session, foreground/background child role processes, configured hooks, user permissions, resume/fork/rewind.
- Recursion level: One Kehai task session with children launched by its agent tool; child roles do not automatically define a separate autonomous organization.
- Reviewed revision: 170d97ae4f89ccda16e513abc4d9a531f8558c38.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

An RPC server owns a journal-backed session tree. ExchangeDriver issues model requests with coding instructions, a live turn/budget sensorium and a bounded roster; model tool calls run via a validated runtime and feed results into later steps. Tools cover anchored read/edit/write, search, bash, skills, ask, agent and job; long results remain in a handle store. Permissions check credential targets, built-in allow rules, user configuration and operator prompts; optional hooks veto individual calls. AgentTool starts a same-binary child RPC process with a configured role, inherited effort, restricted child roster and typed result. JobSupervisor enforces 16 live jobs and four live agents, returning an actionable refusal on excess. Session writer records request/step provenance, outcomes, usage, effort and recovery events. The ambitious [sensorium specification](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/docs/sensorium-spec.md) explicitly distinguishes planned M2 features from the narrow shipped M1 [sensorium](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/loop/sensorium.dart).

## Operational model

A model-bearing parent chooses workspace actions and which role-based child tasks to start; each child runs its own S1 loop. The supervisor refuses shared slot overbooking and provides a specific wait/cancel feedback path for a prospective coordinator (S2 C), without selecting which commitment wins. It does not supply a distinct whole-current S3 decision owner. Configurable child reviewers are not required independent audit; role, provider and permission settings do not constitute S4 or S5 governance.

## S1 — Operations

- State: A
- Function: Model-selected coding and workspace work across repeated tool observations.
- Disturbance / variety regulated: Unknown repository state, failed tools, provider errors, stale edit anchors, user questions and child results.
- Decisive decision or feedback right: Choose investigations, code edits, shell operations, delegation, retries and final reply after results.
- Decision owner: The model-bearing parent or child exchange; deterministic host mediates and enforces its limits.
- Supporting / enforcement mechanisms: ExchangeDriver, tool roster, anchored edits, result handles, session journal, permissions and optional hooks.
- Closure path: User task → model tool request → validated execution/refusal → observed result → next model step or terminal response.
- Boundary reachability: Shipped line client invokes the RPC driver; child agent tool launches the same first-party engine with a role and constrained roster.
- Why this is / is not agent-owned: The model chooses substantive code/task actions, whereas permissions and step ceilings enforce external limits.
- Evidence: [driver](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/loop/driver.dart), [instructions](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/loop/instructions.dart), [runtime](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/tools/runtime.dart), [agent](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/tools/agent.dart).
- Basis: explicit + structural
- Confidence: high for source-level loop closure.
- Caveats: No paid model execution or real task quality benchmark was run.

## S2 — Coordination

- State: C
- Function: Construction path for regulation of contention between running child-agent units for shared process slots.
- Disturbance / variety regulated: A fifth child agent requests capacity when four child workers already hold the shared limit; other jobs can exhaust the 16-job cap.
- Decisive decision or feedback right: Prioritize which worker to wait for or cancel, then retry a refused child request; the decisive coordinator is not installed.
- Decision owner: Uncomposed parent model/user; the deterministic supervisor refuses overload without picking winners.
- Supporting / enforcement mechanisms: maxLiveAgents/maxLiveJobs admission, TooManyLiveAgents refusal, JobTool status/wait/cancel.
- Closure path: Concurrent children exceed slots → supervisor refuses with explicit recovery advice → prospective actor waits/cancels a named job → capacity becomes available for a later child request. No obligatory actor/decision loop is shipped, hence C.
- Boundary reachability: AgentTool catches the shipped job supervisor exception and returns refusal to the calling model; JobTool exposes corrective wait/cancel in the same released tool roster; [capacity test](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/test/jobs/agent_job_test.dart#L400-L434) exercises the live refusal.
- Distinct S1 units: Up to four independently running child model/tool RPC engines with separate role tasks.
- Inter-S1 disturbance: Competition for bounded simultaneous agent-worker slots.
- Attenuating coordination relation: Atomic slot admission and a returned instruction to wait for or cancel an existing worker.
- Feedback into subsequent S1 behaviour: The parent sees refusal and can query/cancel the identified live job before replanning its agent calls.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A concrete cross-agent resource conflict has a dedicated first-party detection/refusal path and subsequent capacity-release interface. Simple child spawning alone is not credited; file-edit conflicts are not solved.
- Why this is / is not agent-owned: Cap enforcement is deterministic, while priority arbitration remains to be composed; no automatically operating S2 governor is demonstrated.
- Evidence: [supervisor limits](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/jobs/supervisor.dart#L20-L38), [admission](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/jobs/supervisor.dart#L645-L679), [agent tool](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/tools/agent.dart), [job tool](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/tools/job_tool.dart).
- Basis: explicit + structural
- Confidence: medium; only shared worker-slot coordination is credited.
- Caveats: The supervisor is not a general conflict arbiter or independent model S2. The construction requires an actor to close priority feedback.

## S3 — Inside-and-now control

- State: —
- Function: No distinct whole-system current-control owner making cross-task resource/commitment decisions from a system-wide live view.
- Disturbance / variety regulated: Step limits, job capacity and interrupts are fixed or per-session execution constraints.
- Decisive decision or feedback right: Review all current commitments and return a binding allocation or supervisory intervention; not supplied.
- Decision owner: Parent agent delegates local tasks, user submits and approves individual calls, supervisor enforces caps.
- Supporting / enforcement mechanisms: One-exchange busy gate, child results, per-job inspection, RPC events and permission prompts.
- Closure path: Child returns to parent S1 and capacity refusal returns to a single tool caller; no dedicated whole-current S3 view and discretion closes.
- Why this is / is not agent-owned: Local delegation and deterministic scheduling do not become organizational S3 by virtue of multiple workers.
- Evidence: [driver](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/loop/driver.dart), [RPC](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/rpc/server.dart), [job](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/tools/job_tool.dart).
- Basis: structural
- Confidence: medium-high.
- Caveats: A supervising consumer could be built on RPC, outside this standard mode.

### Absence scope

- Surfaces inspected: RPC, driver, child process orchestration, job controls, role inventory, CLI and permissions.
- Plausible first-party paths checked: Parent delegations, child status/cancel, 4-agent cap, user interruptions, session writer.
- Why no material first-party path remains: These are per-task operations/capacity controls without a separate whole-current portfolio judgment and returned supervisory intervention.

## S3* — Complementary audit

- State: —
- Function: No shipped independent direct-evidence auditor with a binding corrective return path.
- Disturbance / variety regulated: Incorrect code or completion reports may be checked in an optional user-defined review role.
- Decisive decision or feedback right: Challenge an ordinary S1 report via complementary evidence and issue a corrective finding; not installed.
- Decision owner: User-authored roles/hooks can inspect or deny calls, but no separated auditor is constituted.
- Supporting / enforcement mechanisms: Child roles, independent child context, tests, hooks, session records and result store.
- Closure path: Child result feeds its parent; hook denial gates a tool. Neither is an independent audit verdict returned to S3 control.
- Why this is / is not agent-owned: A generic review-capable child or pre-tool hook does not establish complementary independent auditing.
- Evidence: [role discovery](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/workspace/roles.dart), [child result](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/jobs/agent_run.dart), [hooks](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/hooks/hook_stage.dart).
- Basis: explicit + structural
- Confidence: medium-high.
- Caveats: Consumer composition can implement an audit role, but its independence/authority are not shipped.

### Absence scope

- Surfaces inspected: Child roles/returns, hook stage, permission stage, result/journal evidence and tests.
- Plausible first-party paths checked: Reviewer child role, stored tool outputs, hook veto and independent child process.
- Why no material first-party path remains: No first-party independent evidence-access mandate, audit judgment owner or required correction feedback to a supervisor is provided.

## S4 — Outside-and-then intelligence

- State: —
- Function: No operational future-environment assessment and prospective capability-adaptation loop.
- Disturbance / variety regulated: New coding requirements, context budget and provider failures are met during current task work.
- Decisive decision or feedback right: Select forward-looking adaptation and return it into current organizational capabilities; not found.
- Decision owner: Model changes local coding tactics; operator changes provider and roles; developers own product roadmap.
- Supporting / enforcement mechanisms: Turn/budget sensorium, skills, provider effort, session fork/resume and future ADR plans.
- Closure path: Current observations return to current model step; future sensorium specifications have no shipped selected adaptation decision and return.
- Why this is / is not agent-owned: User task planning and prospective documentation are not first-party S4 governance.
- Evidence: [implemented sensorium](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/loop/sensorium.dart), [M1/M2 ADR](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/docs/adr/0007-tree-derived-perception-and-rendering.md).
- Basis: explicit + structural
- Confidence: medium-high.
- Caveats: Planned test-watch/diagnostic collectors cannot be credited as active.

### Absence scope

- Surfaces inspected: Driver, sensorium, model settings, skill/role loading, session resume and ADR roadmap.
- Plausible first-party paths checked: Context budget, role switching, future diagnostics, fork and provider effort.
- Why no material first-party path remains: Shipped paths manage present coding observations and persistence; future-oriented mechanisms remain proposals without a strategic return loop.

## S5 — Policy and identity

- State: —
- Function: No established enduring organizational identity or ultimate-policy adjudication and return.
- Disturbance / variety regulated: Credential exposure and unsafe file/shell actions are bounded by fixed rules, user allow lists and approvals.
- Decisive decision or feedback right: Decide a legitimate identity/policy conflict and return binding governance for later operation; not evidenced.
- Decision owner: Operator configures permissions/hooks/models; built-in credential veto and prompts control individual tool calls.
- Supporting / enforcement mechanisms: PermissionGate, credential protections, hook stage, child role digests and trust prompt.
- Closure path: Proposed tool → allow/deny/prompt → execution/refusal; there is no identity issue → ultimate authority judgment → governing return.
- Why this is / is not agent-owned: Per-tool consent and security enforcement do not constitute S5 policy.
- Evidence: [gate](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/permissions/gate.dart), [hooks](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/hooks/hook_stage.dart), [instructions](https://github.com/sh1ny/kehai/blob/170d97ae4f89ccda16e513abc4d9a531f8558c38/lib/src/loop/instructions.dart).
- Basis: explicit + structural
- Confidence: medium-high.
- Caveats: External OSS governance and consumer-defined policy are different recursions.

### Absence scope

- Surfaces inspected: Instructions, AGENTS/role loaders, provider settings, permissions, hook and RPC lifecycle.
- Plausible first-party paths checked: User consent, allow rules, credential veto, role digests, model settings and stop.
- Why no material first-party path remains: These authorize local calls without a distinct identity issue and authoritative policy decision returned into continuing governance.

## Distributed OSS parent arrangement

Contributor ADRs and tests are not a runtime governing parent in a user's session. Multiple consumer configurations do not establish an organization-level policy return path.

## Self-hosted and non-human modes

The local engine runs user-chosen provider backends, with child agents using inherited effort and restricted tools. S2 C is bounded to shared process-slot collision feedback; no operator-configured role or hook is silently credited as S3, S3* or S5.

## Recursion

Up to four role-scoped child model processes form subordinate S1 cells; nested child-agent launch is disabled. This does not by itself show recursive viability or a meta-controller.

## Variety and escalation

Anchored edits, result handles, journals and permission decisions give each coder actionable error feedback; fixed caps prevent overload. On a fifth agent the refusal gives a corrective wait/cancel option, but no agent is installed with binding inter-cell priority rights. Provider errors and recovery are ordinary task feedback.

## Evidence gaps

- Dart SDK was unavailable in the assessment environment. Source and shipped tests were inspected, but Dart tests and provider requests were not executed here.
- An externally supplied independent reviewer or supervising organization could alter a deployed boundary; neither is credited at this pinned standard distribution.
