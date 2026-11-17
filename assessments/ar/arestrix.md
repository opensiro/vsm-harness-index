---
harness_id: arestrix
project_name: Arestrix
repository: https://github.com/frankalcantara/Arestrix
review_ref: a8e1075f7303b977426565d0ae88707acdab6416
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: —
---

# Arestrix

## Review boundary

- System in focus: First-party Arestrix desktop Studio, native graph compiler and launched project/batch agent runtime.
- Purpose and identity: Build, execute, supervise and iteratively improve business/task-specific model-backed graph pipelines as a local project.
- Relevant environment: User-supplied model providers, data and MCP services, platform toolchains, files and run output artifacts.
- Standard-distribution boundary: Built-in TypeScript Studio and native C++20 Taskflow generated runners, including optional project memory and batch modes.
- Credited operating / distribution surfaces: Shipped graph authoring/validation, agent tool loop, CLI, standalone runner, native memory, preview/trace, and optional Project Memory review.
- Adjacent first-party surfaces excluded from ownership: CI/release/build checks, example app graph reviewers not wired into ordinary distribution, enterprise branding and external service administrators.
- First-party operating / deployment modes considered: Studio F5, arestrix-cli and standalone executable, multi-path graph, batch checkpoint/resume and per-vertex learn/consult memory.
- Recursion level: One user-owned local project/pipeline; model-backed vertices are S1 units and the project operator is the parent recursion. Not the Arestrix maintainer organization.
- Reviewed revision: a8e1075f7303b977426565d0ae88707acdab6416.
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

A graph built in the Studio is validated, compiled into C++20 Taskflow nodes and executed through the configured native model/tool runtime. Agent vertices maintain local LLM/tool loops; Fork/Join and graph topology are authored and checked separately from model decision ownership. Live trace and batch checkpoints allow operator current-run control. Per-project SQLite memory captures episodes, holds proposals pending approval, and can inject validated knowledge into future runs. Config inheritance and signed delivery artifacts protect execution but are not themselves agent policy makers. [architecture](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/architecture.md); [runtime](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/agents-and-execution.md); [memory](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/how-memory-works.md).

## Operational model

A graph executes task outputs with autonomous local model/tool decisions constrained by a developer-authored topology. Overlapping output writes across parallel paths create a concrete coordination problem: the Studio warns and supplies an optional junction action, but it cannot guarantee automatic conflict recovery. The human project operator supervises current batches and decides which learned future procedures to activate; these parent-mode functions are not credited as agent-owned. No live provider-backed run was performed; classification is pinned source evidence rather than measured task quality.

## S1 — Operations

- State: A
- Function: Build and execute model-driven tool-using steps inside compiled agent vertices of an authorized project graph.
- Disturbance / variety regulated: Open-ended prompt requirements, changing tool results and iterative failure/success of a task.
- Decisive decision or feedback right: The model in an agent vertex chooses tool calls and whether to continue its local tool loop.
- Decision owner: Configured model-backed agent vertex in a shipped compiled Taskflow runner; the graph author supplies the goal and permitted tools.
- Supporting / enforcement mechanisms: C++ generator and runtime, provider/MCP clients, per-node sandbox and user-authored graph edges.
- Closure path: Agent prompt and observed tool output → further model-directed tools → final artifact/return at the graph node; downstream graph nodes consume that result.
- Boundary reachability: Documented Studio F5, headless arestrix-cli and exported Standalone Runner share the compiled execution model.
- Why this is / is not agent-owned: The model, rather than Taskflow scheduling or visual graph, chooses the local investigative/tool action within the fixed graph.
- Evidence: [LLM agent/tool loop](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/agents-and-execution.md); [compiled runtime](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/CppCore/src/compiler/TaskflowGenerator.cpp); [live entry](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/src/core/PipelineRunner.ts).
- Basis: structural.
- Confidence: high for source-supported model loop; no provider-backed live run.
- Caveats: Requires configured model/provider; static nodes themselves are not S1 autonomous agents.


## S2 — Coordination

- State: C
- Function: Reduce conflicts between independently running graph agent paths which may write the same destination.
- Disturbance / variety regulated: Two parallel S1 paths can overwrite a declared output, with last-writer-wins undetected at runtime.
- Decisive decision or feedback right: Choose whether independent paths should converge and add a join so the subsequent graph no longer exposes the same uncontrolled concurrency.
- Decision owner: First-party graph conflict validator and optional assistant/local junction tool expose a specific mitigation; the human/developer must connect the conflict warning and revised graph to the running workflow.
- Supporting / enforcement mechanisms: Graph topology analyzer, `resource_conflict` warning, assistant-mediated or local junction creation, graph validation and Taskflow compile.
- Closure path: Declared concurrent paths → warning and path evidence → user/assistant-constructed join → recompiled execution topology. Not an automatically closed dynamic coordination loop.
- Boundary reachability: Shipped Validate DAG and Merge Paths with Assistant / Suggest Junction Studio actions, not design-only documentation.
- Why this is / is not agent-owned: The validation warning alone does not own coordination; the installed first-party specialized repair constructor exists, but a standing autonomous response to collision is not demonstrated.
- Distinct S1 units: Parallel model-backed agent vertices on distinct graph paths.
- Inter-S1 disturbance: Both paths may write the same output destination and produce overwritten/incoherent deliverables.
- Attenuating coordination relation: First-party declaration-level conflict warning and path-joining operation that changes subsequent Taskflow dependency edges.
- Feedback into subsequent S1 behaviour: New graph join makes later parallel agents synchronize at a shared node when compiled and re-run.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The warning names a concrete inter-path write collision and the junction editor provides a first-party remediation path; graph edges without that witness would not qualify.
- Evidence: [resource conflict check](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/src/core/Validator.ts); [junction decisions](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/src/core/JunctionPlanner.ts); [user-visible restrictions](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/paths-and-junction.md).
- Basis: structural.
- Confidence: medium; this is a constructed path, not automatic live conflict resolution.
- Caveats: Check covers declared output/MCP paths, not opaque C++ writes; warning does not stop execution.


## S3 — Inside-and-now control

- State: P
- Function: Operator oversees the current whole graph or batch of agent steps and regulates execution/recovery of the running workload.
- Disturbance / variety regulated: Current stage failures, pending work, serialized bottlenecks, token and latency limits and blocked batch items.
- Decisive decision or feedback right: Inspect live whole-run statuses, adjust a batch's operational constraints/checkpoints, stop or restart the run and choose which work is resumed.
- Decision owner: Local project operator in the documented Studio and batch operating mode; native runner applies configuration and resumes checkpoints.
- Supporting / enforcement mechanisms: RunnerManager and PipelineRunner telemetry, batch modal, PipelineResumeEngine, serialized-stage settings and trace UI.
- Closure path: Node/stage trace and per-item checkpoint matrix → operator current-run intervention or batch concurrency/restart choice → next resumed run accepts/changes current work.
- Boundary reachability: Supported F5/Stop/Restart and Run tab batch orchestrator; a parent/operator-specific interface, not a speculative plugin.
- Why this is / is not agent-owned: No supervisor LLM with campaign-wide discretionary authority is documented. Parent monitoring and current workload control are operationally supported; deterministic checkpoints alone do not establish autonomous S3.
- Whole-system current view: Studio runner's node timeline, tokens/latency telemetry, live errors and per-item batch checkpoints across the active pipeline.
- Current-control decision scope: Run/stop/restart, current work resume and serialized stage/concurrency choices for the entire local batch.
- Evidence: [batch and runner operations](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/agents-and-execution.md); [live run status](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/src/core/runner/RunnerManager.ts); [resume substrate](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/CppCore/src/sandbox/PipelineResumeEngine.cpp).
- Basis: structural.
- Confidence: medium; operator's ability to change next current run is supported, not all settings are hot-reloadable.
- Caveats: Editing a graph at design time alone does not count. The parent mode here is current batch/run management, not mere Stop button.


## S3* — Complementary audit

- State: —
- Function: No installed, campaign-relative independent examination of the agent's real delivered work is established.
- Disturbance / variety regulated: Faulty model answers or artifacts might need complementary operational evidence, but packaged validators chiefly inspect static graph, asset safety or the agent's own artifacts.
- Decisive decision or feedback right: None established as a separate audit judgement returned to the operating agent or current controller.
- Decision owner: Not established at the selected first-party runner boundary.
- Supporting / enforcement mechanisms: Skill Guard and MCP audits, static graph validator, artifact validation and telemetry logs are reviewed but concern dependencies, declaration validity or checks within the producing path.
- Closure path: No distinct complementary observation → independent judgement → changes to next S1/S3 work closure found.
- Boundary reachability: The checks are packaged and callable, but their evidence identity does not match an independent operational-audit claim.
- Why this is / is not agent-owned: Independent-looking auditing classes are not automatically S3*: no verified separate reviewer with complementary read access to actual run results returning interventions.
- Evidence: [skill audit](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/src/core/workspace/WorkspaceSkillAuditorAgent.ts); [graph check](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/src/core/Validator.ts); [artifact validation](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/agents-and-execution.md).
- Basis: structural.
- Confidence: medium bounded negative.
- Caveats: A custom graph can implement a reviewer, but such user-built graph is not first-party completed audit.

### Absence scope

- Surfaces inspected: First-party skill/MCP audit, validation, telemetry and example node libraries.
- Plausible first-party paths checked: Skill Guard scans input skill packages; graph validator checks edges; artifact checks inspect output shape; user-composed reviewer graph possibilities.
- Why no material first-party path remains: No documented first-party complementary independent examination of actual S1 outcome, decision and feedback into control at supported shipped boundary.


## S4 — Outside-and-then intelligence

- State: P
- Function: Turn observed cross-run performance and environment-specific task lessons into reusable future operating guidance.
- Disturbance / variety regulated: Newly encountered task failures, changed information and recurring procedures may make the current agent instruction ineffective on later work.
- Decisive decision or feedback right: Decide which agent-proposed lessons or procedure candidates become trusted active project memory/playbooks for future runs.
- Decision owner: Project owner in the first-party approval/Project Memory UI; deterministic independent artifact and repeated-case validation is supporting enforcement.
- Supporting / enforcement mechanisms: `learn` mode, lesson proposal tools, episodes, validator outcomes, content-addressed evidence snapshots, prompt brief injection and promoted playbook store.
- Closure path: Environment/task outcome and model lesson proposal → pending approval / validated candidate → owner promotion → new active brief/playbook supplied to subsequent agent runs.
- Boundary reachability: Opt-in per-vertex learn mode and installed Project Memory panel and CLI, with approved knowledge persisted across runs.
- Why this is / is not agent-owned: Model may propose changes, but parent owner or validation gate has the final supported future-capability admission; autonomous strategic adaptation judgement is not demonstrated.
- External distinction: Newly supplied external documents and production task outcomes can contradict the last stored operating procedures.
- Future / prospective distinction: Observed changes in tasks, failed/successful delivered artifacts and newly encountered source passages outside the stored operating playbook.
- Adaptation option generated: Model-proposed reusable lesson and candidate playbook derived from new outcomes; owner selects evidence-backed adoption after validated evidence.
- Path back into current capability / S3: Promoted active memory and playbooks are injected into subsequent model briefs and change usable procedures under project oversight.
- Evidence: [memory promotion cycle](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/how-memory-works.md); [procedure candidate](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/CppCore/src/memory/MemoryPlaybookCompiler.cpp); [owner-visible memory modes](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/workspaces-memory-skills-mcp.md).
- Basis: structural.
- Confidence: medium; classification is confined to concrete task-learning/capability reuse, not external market scanning.
- Caveats: Optional mode; general history retrieval alone is not S4. The UI approval is distinct from ordinary content editing.


## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/policy conflict loop is established at the running-project recursion.
- Disturbance / variety regulated: Whether the agent organization's lasting purpose and non-negotiable constraints need revision is outside ordinary runtime settings.
- Decisive decision or feedback right: No decision right evidenced for system-level ultimate-policy adjudication and return.
- Decision owner: Project owner configures prompts/keys, but not through a demonstrated S5 escalation and closure process.
- Supporting / enforcement mechanisms: Inherited model/tool/sandbox defaults, project-level skill prompts, packaging signatures and user approval of individual runtime interactions.
- Closure path: Configuration/permission is enforced by local runner; no policy-dispute → legitimate authority resolution → changed organizational identity loop observed.
- Boundary reachability: Configuration editing and authorization exist, but do not by themselves qualify S5.
- Why this is / is not agent-owned: A project author sets instructions, yet this is not evidence of revising foundational policy following identity conflict.
- Evidence: [settings hierarchy](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/workspaces-memory-skills-mcp.md); [interaction/packaging](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/docs/en/agents-and-execution.md); [policy gating](https://github.com/frankalcantara/Arestrix/blob/a8e1075f7303b977426565d0ae88707acdab6416/src/core/Validator.ts).
- Basis: structural.
- Confidence: medium bounded negative.
- Caveats: The owner may define a constitution manually; this is not the same as supported first-party S5 organization.

### Absence scope

- Surfaces inspected: Studio/Workspace/Project controls, agent skills and model binding, interaction approvals and package policy.
- Plausible first-party paths checked: Parent can edit mission/task prompts and permissions, guard static files, approve interactions; no observed protocol for identity-level disputes.
- Why no material first-party path remains: Only configuration/enforcement/individual approvals were evidenced; no first-party escalation to identity authority and returned ultimate-policy decision was found.

## Distributed OSS parent arrangement

No private cross-maintainer operating context is assumed. Repository-wide release governance and vendor provider configurations are outside the selected project runtime recursion; S3 and S4 parent modes here are specific to the documented local project operator.

## Self-hosted and non-human modes

Runtime execution requires user-provided model endpoints, compiler and sandbox support. Any fully unattended user-authored graph does not inherit system-wide S3/S4/S5 autonomy without source-evidenced authority at its own declared boundary. Parent-mode P does not imply model supervision.

## Recursion

A whole compiled project graph is the system in focus. Agent vertices perform local work; a graph join is coordination substrate; the Studio operator regulates the active graph and future approved knowledge. External providers, maintainer reviews and CI do not supply missing internal functions.

## Variety and escalation

The model handles uncertain tool outcomes; graph validation reveals possible concurrent output collision and offers a bounded repair constructor; batch checkpoints expose current work to a local owner. Failed/validated episodes can produce future lessons after an explicit evidence and approval gate. Runtime permission questions do not constitute ultimate-identity arbitration.

## Evidence gaps

- Exact compiled code paths are statically inspected, not executed with external credentials; no provider-backed trace is asserted.
- S2=C depends on the user composing a documented warning/junction path rather than asserting an automatic coordination agent.
- Parent S3 is limited to actual batch/project operational management, not mere possession of a dashboard or stop button.
- S4=P concerns opt-in cross-run future procedural learning; generic recall and ordinary prompt editing alone would not suffice.
