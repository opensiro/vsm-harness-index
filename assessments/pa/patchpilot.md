---
harness_id: patchpilot
project_name: PatchPilot
repository: https://github.com/jx-grxf/PatchPilot
review_ref: 79eed49aa6c8daf7dd939047031c942424782abc
reviewed_at: 2026-11-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# PatchPilot

## Review boundary

- System in focus: the shipped PatchPilot 2.0 local coding-agent application at the frozen `jx-grxf/PatchPilot` revision, including its main model/tool loop, bounded child agents, workspace execution, approvals, terminal interface, local session/context stores and runtime/model selection.
- Purpose and identity: carry out user-directed repository inspection, code modification, command execution and verification using a model running on user-controlled inference infrastructure.
- Relevant environment: an operator and their chosen Git workspace, arbitrary task and code variation, tool results and errors, filesystem permissions, model/runtime capabilities and context pressure.
- First-party operating boundary: the Node.js CLI/Ink TUI invokes `AgentRunner` and `WorkspaceTools`, optionally delegating bounded requests to first-party child loops. Ollama/OpenAI-compatible inference servers provide model inference; the target repository, its test commands and the human operator are external. Model inference is not a separate third-party coding-agent framework.
- Credited operating / distribution surfaces: `src/cli.tsx`, `src/core/agent.ts`, `subagentRunner.ts`, `workspace.ts`, `toolSchema.ts`, `capability.ts`, `session.ts`, `contextStore.ts`, `memory.ts`, `localRuntimes.ts`, and `src/tui/`.
- Adjacent first-party surfaces excluded from ownership: GitHub CI/release workflows, repository-maintainer quality checks and product design documents are evidence, but are not a deployed complementary auditor or metasystem for the user's coding session. Ollama and the target repository do not become first-party VSM controllers.
- Operating modes: `plan` read-only, `build` with per-action approval and `bypass` with trusted-workspace write/shell permissions; optional `explore` and `general` child agents; local/remote inference routes, session resume and operator-configured context/memory.
- Recursion level: one operator-directed coding task and its optional subordinate exploration/editing loops, not the maintainer's organization or a federation of unrelated CLI sessions.
- Reviewed revision: `79eed49aa6c8daf7dd939047031c942424782abc`.
- Observation date: 2026-11-06.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`src/cli.tsx` configures the operator-selected workspace, inference provider, model and permission mode, then starts the first-party `AgentRunner`. The runner probes native tool-calling capability, advertises a mode-specific tool surface or validated JSON fallback, streams model decisions and dispatches them through the bounded workspace layer. Executed tool results and failures become the model's next observations. The runtime checks repeated/invalid calls and step limits, and persists events in local session/context stores.

With delegation enabled, a `task` call instantiates another `AgentRunner` in a fresh context. An `explore` child has `read/glob/grep`; a `general` child additionally has `write/edit`. Children have no shell or grandchildren, run at most eight steps, and return a compact summary with a saved local trace. The parent executes pending children serially to conserve one local model server's prefix cache, then processes normal workspace tool results. This is demonstrable operational delegation, but it does not by itself establish an inter-S1 interference controller, organizational resource bargaining, or independent audit.

`WorkspaceTools` resolves paths inside the designated workspace, rejects sensitive targets, classifies shell risk, and asks the human or applies explicit bypass rules for side effects. The terminal reports activity, todos and diffs. Context compaction, optional searchable memory, model discovery and `/update` help operate the current product, but their configured/user-confirmed behavior does not constitute an agent-owned future adaptation program.

Primary source:

- [Architecture and deployment boundary](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/docs/architecture.md)
- [Main model/tool loop](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/agent.ts)
- [Child-agent execution and bounds](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/subagentRunner.ts)
- [Workspace execution and approval boundary](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/workspace.ts)
- [Product operating modes](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/README.md)

## Operational model

The primary model-backed agent selects task-specific reads, searches, edits, commands, optional child requests and final answers. The first-party harness validates, executes or blocks each requested action, returns the actual observation, and lets the agent revise its next choice. When requested, child agents independently execute narrower operational work and give their results to the parent. The operator retains permissions, configuration, cancellation and final acceptance. Step caps, validation, serial scheduling and persisted traces are deterministic constraints or transport; they do not automatically own VSM metasystem decisions.

## S1 — Operations

- State: A
- Function: produce code/repository-work outcomes through one or more environment-facing model-directed observe–act–observe coding loops.
- Disturbance / variety regulated: unknown code structure, heterogeneous user tasks, unexpected tool output, tool/model errors, context limits and discovered test results.
- Decisive decision or feedback right: choose the next concrete tool invocation, child task or correction after observations; decide whether a coding answer is complete.
- Decision owner: the primary model-backed `AgentRunner`, and bounded model-backed child loops for delegated local operations.
- Supporting / enforcement mechanisms: model capability probing, tool schemas and repair, `WorkspaceTools`, approval mode, command/path policy, child allowlists, cancellation, context compaction and session events.
- Closure path: user task and code observations → model-selected tool/task → validated/approved first-party execution → returned result or error → revised model action or answer.
- Boundary reachability: shipped CLI/TUI starts the main loop; the optional shipped `task` path constructs real child runners without importing an external agent framework.
- Why this is / is not agent-owned: without the model actors, deterministic tools and permissions would not choose task-specific edits, exploration or iterative correction. Those choices remain agent-discretionary within bounded operator rights.
- Evidence: [`agent.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/agent.ts); [`subagentRunner.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/subagentRunner.ts); [`workspace.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/workspace.ts); [`toolSchema.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/toolSchema.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the selected model inference endpoint must be available; writes or shell steps may be blocked pending a human decision. Child loops exist only in configured or explicitly requested delegation mode.

## S2 — Coordination

- State: —
- Function: no specific inter-S1 disturbance plus a closed coordinating response is established at this task recursion.
- Disturbance / variety regulated: the main loop and optional children can touch one workspace, but no demonstrated cross-child write collision, negotiation or oscillation with a dedicated mitigation/feedback relation is shown.
- Decisive decision or feedback right: no first-party agent-owned cross-S1 coordination decision evidenced.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: parent task requests, child-specific tool permissions, serial child execution, bounded steps and compact parent-facing results.
- Closure path: child results inform the parent task loop; serial execution is explicitly designed for prefix-cache preservation, not evidenced regulation of interference among autonomous S1 cells.
- Why this is / is not agent-owned: parent delegation and serial scheduling organize work but do not identify a concrete inter-S1 disturbance and adaptive coordination closure required by the Profile.
- Evidence: [`agent.ts` child scheduling](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/agent.ts); [`subagentRunner.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/subagentRunner.ts); [`architecture.md`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/docs/architecture.md).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: optional child editing is genuine S1 delegation; a later implementation of conflict detection, shared state reservations or cross-child feedback could change this assessment.

### Absence scope

- Surfaces inspected: parent/child runner, tool scheduling, workspace write/edit paths, child tool allowlists and architecture description.
- Plausible first-party paths checked: shared workspace write-conflict handling, child reservations, mutual adjustment, scheduler intervention and parent-mediated conflict resolution.
- Why no material first-party path remains: code documents serial execution for inference-cache reasons; there is no evidenced specific child–child collision recognized and regulated through a distinct S2 closure.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current performance/resource bargaining across distinct operational units is established beyond one task's orchestration.
- Disturbance / variety regulated: tool failures, step count, permission risk and task progress are controlled locally, not demonstrated as competing commitments or portfolio-level performance requiring S3 intervention.
- Decisive decision or feedback right: the parent model can select subtask assignments, but no evidenced whole-system resource/priority intervention authority distinct from task decomposition.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: child step cap, serial invocation, todo list, result envelopes, permission mode, cancellation and loop breaker.
- Closure path: child output flows to the parent model and can change the next coding step; no separate current-operation-wide allocation or exception-regulation cycle is shown.
- Why this is / is not agent-owned: task delegation and bounded execution are real, but parent summarization and static limits are insufficient for an S3 organizational claim.
- Evidence: [`agent.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/agent.ts); [`subagentRunner.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/subagentRunner.ts); [`toolSchema.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/toolSchema.ts).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: the parent can react to a failing child; a task-local retry or delegation decision should not be mislabeled current-system accountability across organizational units.

### Absence scope

- Surfaces inspected: parent loop, child execution, budgets/step caps, operational telemetry, todos and approval policy.
- Plausible first-party paths checked: whole-system performance view, resource bargaining, cross-unit priority changes, accountability and intervention on current commitments.
- Why no material first-party path remains: no production-wired whole-organization control decision is distinguished from agent task sequencing and deterministic safety caps.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary inspection channel that challenges routine agent claims and returns audit findings to a distinct supervisory decision path is established.
- Disturbance / variety regulated: output errors may be caught by tests or viewed in `/diff`, but these are ordinary task verification and operator inspection rather than an independent audit of S1/S3 reporting.
- Decisive decision or feedback right: no separate auditor with independent access and corrective supervisory return evidenced.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ordinary run-tests/shell results, Git diff, terminal telemetry, JSONL logs, child transcripts and optional same-agent post-write verification nudge.
- Closure path: operational tool results feed the same model loop and user view; no distinct independent auditor's finding is routed to supervisory correction.
- Why this is / is not agent-owned: a child `explore` agent may independently read files, but it is delegated operational research—not a deployed complementary audit path for the producer's claims.
- Evidence: [`agent.ts` verification and child results](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/agent.ts); [`session.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/session.ts); [`subagentRunner.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/subagentRunner.ts); [`README.md`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: this does not deny the utility of normal tests, file inspection or the human's own independent review.

### Absence scope

- Surfaces inspected: `/diff`, task testing, agent verification pushback, telemetry, saved transcripts and child tools.
- Plausible first-party paths checked: separate reviewer-agent sampling, direct-artifact reconciliation independent of producer reports and audit-return intervention.
- Why no material first-party path remains: ordinary checks remain on the producer task path; no independent complementary audit owner, claim comparison and closed corrective return is instantiated.

## S4 — Outside-and-then intelligence

- State: —
- Function: no agent-owned prospective environmental intelligence to future capability adaptation and S3 dialogue is established.
- Disturbance / variety regulated: changing local runtimes, model availability, long-session context and version releases are monitored or configured for current use, not turned into a prospective organizational capability strategy.
- Decisive decision or feedback right: no autonomous future-option formation and approved capability-change return demonstrated.
- Decision owner: not established.
- Supporting / enforcement mechanisms: runtime/model discovery, `/connect`, `/update` with user confirmation, context compaction and optional memory persistence.
- Closure path: operator selects models or installs a release and context history influences task continuation; no first-party environment-sensing → future-option → capability-change → present-control conversation is shown.
- Why this is / is not agent-owned: endpoint enumeration and upgrade prompts are operational configuration, while generated task plans target present coding work, not future system adaptation.
- Evidence: [`localRuntimes.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/localRuntimes.ts); [`contextStore.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/contextStore.ts); [`memory.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/memory.ts); [`tui/commands.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/tui/commands.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a future agent-directed adaptation layer would require fresh review at its actual deployment boundary.

### Absence scope

- Surfaces inspected: model inventory and runtime selection, update command, context stores, memory feature and task prompting.
- Plausible first-party paths checked: prospective opportunity/threat analysis, persistent self-improvement proposals, S3-governed capability adaptation and future-market/environment sensing.
- Why no material first-party path remains: the observed controls are operator-driven upgrades/configuration or task context maintenance, without a closed prospective system-change loop.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/mission or parent-governed policy adjudication with durable return is established.
- Disturbance / variety regulated: local workspace risks, shell commands, hidden files, permissions and prompt behavior are limited by static code and human action-level approval.
- Decisive decision or feedback right: no S5 identity-level policy choice, legitimacy escalation or return governing later operations.
- Decision owner: not established; human operator chooses modes and accepts/denies individual side effects.
- Supporting / enforcement mechanisms: `plan/build/bypass`, tool allowlists, workspace confinement, sensitive path denial, shell risk classification and approval handler.
- Closure path: a requested write/shell action is allowed or denied for the current task. This local permission does not enact a new organizational identity/policy decision.
- Why this is / is not agent-owned: removing the model leaves the authored safety rules and human authorization intact; the model is not delegated ultimate-policy authority.
- Evidence: [`workspace.ts`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/workspace.ts); [`agent.ts` prompt/mode](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/src/core/agent.ts); [`product-context.md`](https://github.com/jx-grxf/PatchPilot/blob/79eed49aa6c8daf7dd939047031c942424782abc/docs/product-context.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: user approval is legitimate local action authorization; this is not evidence of a distinct S5 organizational policy function.

### Absence scope

- Surfaces inspected: mode and tool policy, workspace sandboxing, shell approval, external network boundaries and human control of configuration.
- Plausible first-party paths checked: constitutional/identity decisions, parent-recognized policy-change proposals, identity escalation and durable parent decision returning to runtime governance.
- Why no material first-party path remains: shipped paths enforce preset constraints or ask for action-specific human permission; they do not close an ultimate identity/mission dispute.

## Recursion

One primary coding session can spawn model-backed child operational loops with separate context and narrower rights. This makes multiple local S1 activities possible, but nesting and delegated subtasks alone do not demonstrate that the child group plus parent has the S2–S5 relations of a separate viable organization. Other PatchPilot sessions and the project's own CI are outside this chosen runtime recursion.

## Variety and escalation

Native/fallback tool calling and local-model selection amplify operational variety. Mode-based tool exposure, path confinement, tool/shell validation, human approvals, step/recursion limits, context pressure controls, task todos and cancellation attenuate variety. Child summaries return to the parent; tool errors return to the task model; side-effect permission disputes reach the user. Those paths enforce local operating bounds without automatically converting their handlers into S2, S3, S3* or S5.

## Evidence gaps

This is source-first static review of shipped code at the immutable revision, not a live model-provider end-to-end task. We did not run a local Ollama/LM Studio model or instantiate actual child agents. A dedicated inter-child collision-control path, whole-system current-governance loop, independent complementary auditor, prospective adaptation function or parent-ratified identity-policy loop was not evidenced in the inspected standard operating boundary. Any later feature or changed ref needs re-review.

## Assessment summary

PatchPilot implements a genuine first-party coding agent and bounded model-backed subordinate operational loops (**S1=A**). The parent delegates, collects results and applies safety limits, but those facts alone do not establish the distinct interference-regulation, whole-current control, independent audit, prospective adaptation or policy-identity closure required for S2–S5.

Proposed vector: **`A · — · — · — · — · —`**.
