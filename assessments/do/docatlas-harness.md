---
harness_id: docatlas-harness
project_name: DocAtlas Harness
repository: https://github.com/microsoft/DocAtlas-Harness
review_ref: 183be5498432b0e911e6e74daa177f8b6fd2532f
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# DocAtlas Harness

## Review boundary

- System in focus: The installed DocAtlas document investigation runtime and its shipped terminal and chat entry points.
- Purpose and identity: Produce evidence-grounded answers about one or more documents within a user-selected workspace.
- Relevant environment: Local or downloaded documents, a configured model provider, and an interactive user or CLI caller.
- Standard-distribution boundary: The packaged AgentLoop, runtime assembly, four portable Skills and session/workspace support.
- Credited operating / distribution surfaces: Interactive workbench and chat, local preprocessing, Skills called within the runtime, and session-local tools and inspection.
- Adjacent first-party surfaces excluded from ownership: Benchmark runners, offline scoring scripts, repository development and release workflows, and test fixtures. Standalone Skill consumers outside DocAtlas supply their own agent.
- First-party operating / deployment modes considered: Interactive multi-turn workbench and CLI chat, with supported session preprocessing and optional post-note hooks.
- Recursion level: One document investigation session; document readers and model calls made by tools are subordinate to that operational session.
- Reviewed revision: `183be5498432b0e911e6e74daa177f8b6fd2532f`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The runtime composes provider and tool schemas, dispatches structured tool calls to Search, Read, Note and Review subprocesses, and owns the session and tool-result loop. Persisted session state carries a document tree and notes. In a configurable path a note also enriches the session tree and archives earlier tool results. Interactive chat and benchmark execution share infrastructure but their policies and output consumers differ. [`ARCHITECTURE.md`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/ARCHITECTURE.md#L8-L79), [`docatlas/runtime.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/runtime.py#L28-L94), [`docatlas/agent/loop.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/agent/loop.py#L190-L430), [`docatlas/agent/post_note.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/agent/post_note.py#L145-L223).

## Operational model

The workbench selects a user-authorized document workspace. The model chooses what to search, read or record as evidence and when to answer. The runtime enforces document/session limits, dispatches tools, and returns resource content to the model. Operators configure the environment and can inspect or clear their own session.

## S1 — Operations

- State: A
- Function: Answer a document question through iterative evidence collection.
- Disturbance / variety regulated: Questions, document structure, tool results and chart/table evidence vary between tasks.
- Decisive decision or feedback right: Choose model-visible skill, arguments, follow-on investigation and answer after observing results.
- Decision owner: The model-backed investigation agent.
- Supporting / enforcement mechanisms: Workspace and session store, tool schemas, subprocess dispatch and response history.
- Closure path: Returned text or images and archived notes become context for the next model action; a tool-free response completes the question.
- Why this is / is not agent-owned: Without the model, search/read/note primitives and session state cannot select an investigation sequence or decide what answer to give.
- Evidence: [`docatlas/runtime.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/runtime.py#L28-L94), [`docatlas/agent/loop.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/agent/loop.py#L190-L430), [`ARCHITECTURE.md`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/ARCHITECTURE.md#L37-L75).
- Basis: structural
- Confidence: High
- Caveats: Task correctness varies with provider and documents. Source and test code reviewed without a live model run.
- Boundary reachability: The CLI chat and workbench assemble the same packaged AgentLoop with shipped Skills and configured provider access.

## S2 — Coordination

- State: —
- Function: Dampen interference between independent operational units.
- Disturbance / variety regulated: Parallel readers or different document workspaces could contend if treated as distinct S1 units.
- Decisive decision or feedback right: No shipped resolution of interference among independently committed investigation agents.
- Decision owner: One investigation agent owns search choices; subprocesses and writes are runtime-controlled.
- Supporting / enforcement mechanisms: Private workspace/session state and atomic state writes.
- Closure path: Tool output returns within the same investigation; session separation partitions callers.
- Why this is / is not agent-owned: Operations by Search and Read remain delegated primitives under one investigation owner.
- Evidence: [`ARCHITECTURE.md`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/ARCHITECTURE.md#L37-L79), [`ARCHITECTURE.md`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/ARCHITECTURE.md#L81-L125), [`docatlas/agent/dispatch.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/agent/dispatch.py#L279-L360).
- Basis: structural
- Confidence: High
- Caveats: Batch parallelism and consumers of portable Skills outside this runtime are outside scope.

### Absence scope

- Surfaces inspected: Session state and workbench lifecycle, runtime assembly, dispatch and Skills.
- Plausible first-party paths checked: Checked multiple PDF selection, multimodal subprocess calls and workspace replacement as candidate peer paths.
- Why no material first-party path remains: Multiple inputs and tool subprocesses feed one question, while private independent workspaces expose no cross-unit feedback or arbitration.

## S3 — Inside-and-now control

- State: —
- Function: Control present operational commitments and shared resources at the investigation-system boundary.
- Disturbance / variety regulated: Long questions and response context can hit turn, image or tool resource limits.
- Decisive decision or feedback right: No separate current-control decision over shared commitments from a whole-system view.
- Decision owner: The user chooses or resets their session; the agent decides evidence collection inside it.
- Supporting / enforcement mechanisms: Turn caps, image trimming, post-note archival, workbench status and read-only overview.
- Closure path: Trimming and resetting constrain or replace the active task state; they do not reprioritize a portfolio of commitments.
- Why this is / is not agent-owned: Ordinary model choices about what evidence to read next belong to S1. Configuration and the read-only status view give no separate control loop.
- Evidence: [`docatlas/agent/loop.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/agent/loop.py#L66-L155), [`docatlas/agent/loop.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/agent/loop.py#L190-L430), [`docatlas/agent/post_note.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/agent/post_note.py#L145-L223), [`ARCHITECTURE.md`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/ARCHITECTURE.md#L97-L125).
- Basis: structural
- Confidence: High
- Caveats: A user can inspect or abandon a question.

### Absence scope

- Surfaces inspected: AgentLoop cap and context maintenance, workbench commands and overview, workspace replacement, CLI profiles.
- Plausible first-party paths checked: Checked post-note archival, read-only overview, tool dispatch and user reset as current-control paths.
- Why no material first-party path remains: The operative paths constrain one investigation or expose its state. No first-party decision revises wider live commitments or capability use from that view.

## S3* — Complementary audit

- State: —
- Function: Independently challenge operational evidence or answer claims and feed back a finding.
- Disturbance / variety regulated: A final answer could omit contrary evidence or cite the wrong passage.
- Decisive decision or feedback right: No shipped complementary in-use judgment with independent authority over the investigation result.
- Decision owner: The investigation agent reopens its own notes. The separate benchmark scorer operates on exported predictions and ground truth.
- Supporting / enforcement mechanisms: Review Skill, oversight view, tool traces and offline scoring scripts.
- Closure path: Review returns saved evidence to the same agent; scoring produces a separate report without a return edge into the live question.
- Why this is / is not agent-owned: Neither the Review label nor the separate benchmark judge supplies an independent in-operation audit decision.
- Evidence: [`docatlas/skills/review/scripts/run.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/skills/review/scripts/run.py#L82-L155), [`docatlas/scoring/finrag_judge.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/scoring/finrag_judge.py#L228-L296), [`ARCHITECTURE.md`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/ARCHITECTURE.md#L103-L113).
- Basis: structural
- Confidence: High
- Caveats: Independent benchmark judgment is real in its own evaluation scope.

### Absence scope

- Surfaces inspected: Review Skill and note state, ordinary model trace and user overview, offline FinRAG and MMLongBench scoring.
- Plausible first-party paths checked: Checked note retrieval, direct operator inspection and the report from comparative LLM judging.
- Why no material first-party path remains: The runtime delegates review to evidence retrieval for the same actor; external scoring has no shipped return path to gate or revise this operational answer.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense prospective environmental shifts and revise future investigation capability.
- Disturbance / variety regulated: Models and document sources might change across deployments.
- Decisive decision or feedback right: No packaged prospective adaptation decision backed by environment sensing and returned to live capability.
- Decision owner: Users choose provider/profile and document input. The model decides task-local note content.
- Supporting / enforcement mechanisms: Provider factory, profiles, workspace keys, session tree and note hooks.
- Closure path: Note enrichment changes later searches in the same investigation. Cache compatibility decides whether initialization artifacts can be reused.
- Why this is / is not agent-owned: An evidence note updates a task model during operations. It selects no future operating capability against prospective alternatives.
- Evidence: [`docatlas/agent/post_note.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/agent/post_note.py#L145-L223), [`docatlas/__main__.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/__main__.py#L97-L129), [`docatlas/runtime.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/runtime.py#L28-L94), [`ARCHITECTURE.md`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/ARCHITECTURE.md#L81-L90).
- Basis: structural
- Confidence: High
- Caveats: Provider benchmarking may inform humans external to the assessed runtime.

### Absence scope

- Surfaces inspected: Post-note hooks, CLI profiles, model provider factory, workspace cache and benchmark entry points.
- Plausible first-party paths checked: Checked note-driven tree evolution, profile switches and evaluation outputs as future-capability mechanisms.
- Why no material first-party path remains: Shipped note hooks consume the current task. Profiles and reports support manual setup without a function-specific adaptation judgment loop in the distribution.

## S5 — Policy and identity

- State: —
- Function: Resolve standing identity or ultimate authority questions for the deployed runtime.
- Disturbance / variety regulated: Answer policy, accessible resources and accepted provider capabilities bound an investigation.
- Decisive decision or feedback right: No shipped ultimate-policy decision path over conflicting standing authorities.
- Decision owner: The implementation defines defaults. Operators select files and local configuration at launch.
- Supporting / enforcement mechanisms: System prompt composition, profiles, document read boundary and runtime enforcement.
- Closure path: Effective configuration constrains each launched session; no operational escalation returns a standing policy ruling.
- Why this is / is not agent-owned: A configurable startup argument or session document selection supplies parameters rather than an ultimate authority process.
- Evidence: [`docatlas/__main__.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/__main__.py#L97-L129), [`docatlas/runtime.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/runtime.py#L28-L94), [`docatlas/prompt_composer.py`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/docatlas/prompt_composer.py), [`ARCHITECTURE.md`](https://github.com/microsoft/DocAtlas-Harness/blob/183be5498432b0e911e6e74daa177f8b6fd2532f/ARCHITECTURE.md#L150-L185).
- Basis: structural
- Confidence: High
- Caveats: Repository maintainers can change the software outside this operating recursion.

### Absence scope

- Surfaces inspected: Prompt composition and profiles, chat startup, workspace boundaries and user commands.
- Plausible first-party paths checked: Checked file authorization, profile precedence and assessment-specific prompts for a durable policy escalation path.
- Why no material first-party path remains: The inspected surfaces enforce configured identity and operate documents; none receives and resolves a standing identity or authority issue for subsequent deployment operation.

## Recursion

The investigation is the operational cell. Documents, subprocesses and model calls under the four Skills are inputs or instruments at that recursion.

## Variety and escalation

The model responds to document and tool-result variety with iterative search and note-taking. Provider/turn/tool limits and local workspace isolation bound this operational discretion.

## Evidence gaps

No live provider traces or benchmark reruns were generated. No broader project governance claim is made.
