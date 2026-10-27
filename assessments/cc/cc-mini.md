---
harness_id: cc-mini
project_name: cc-mini
repository: https://github.com/e10nMa2k/cc-mini
review_ref: 73c5bc563093b650ea8754bf9101a7507d8328a8
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# cc-mini

## Review boundary

- System in focus: The installed cc-mini terminal coding harness, including the opt-in coordinator/worker mode; not the organization developing cc-mini.
- Purpose and identity: Complete user-directed software research and changes with model-selected tool actions.
- Relevant environment: Local source trees, shell/filesystem, model APIs, user permissions and concurrent coding workers.
- Standard-distribution boundary: Packaged Python src modules and their first-party CLI/REPL modes at the frozen ref.
- Credited operating / distribution surfaces: [src/tui/app.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/tui/app.py); [src/core/engine.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/engine.py); [src/features/coordinator.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/coordinator.py); [src/features/agents/worker_manager.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/agents/worker_manager.py)
- Adjacent first-party surfaces excluded from ownership: tests/ corroborate wiring without becoming an audit actor. Buddy/poke-game entertainment is an adjacent purpose; it does not own coding-team regulation. Development/release activity and upstream Claude Code claims are outside this boundary.
- First-party operating / deployment modes considered: Normal interactive/print mode; --auto-approve; --coordinator; plan/explore; optional memory consolidation, skills and sandbox. Parent operator permission prompts checked separately.
- Recursion level: One local coding session/team; coordinator and outcome-producing workers are within this recursion.
- Reviewed revision: `73c5bc563093b650ea8754bf9101a7507d8328a8`
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The CLI builds a tool-enabled Engine and streams model responses. Tool_use blocks execute through a PermissionChecker; results are appended to messages before the next model call. Session persistence, context compaction, cost accounting and optional sandbox constrain/support execution. Coordinator mode adds Agent, SendMessage and TaskStop backed by first-party worker engines, a task registry and completion notifications injected into the coordinator loop. Built-in review/test/simplify skills and a fresh verification-worker instruction exist, but are part of ordinary production QA. Memory consolidation rewrites learned user/project notes. No centralized maintainer governance is packaged into the runtime.

## Operational model

A main agent and, in coordinator mode, workers choose local investigation, edits and tests. Read-only work can overlap; write-heavy work on the same file set must be sequenced by the coordinator. The coordinator receives status/failure results and can continue, replace or stop workers. Permission enforcement and queues do not make these discretionary choices.

## S1 — Operations

- State: A
- Function: Produce software-task outcomes through autonomous observation/action iteration.
- Disturbance / variety regulated: Unknown code, tool failures and changing intermediate results.
- Decisive decision or feedback right: Choose next tool/action, react to returned output and decide to conclude.
- Decision owner: Main model-backed agent and first-party worker agents.
- Supporting / enforcement mechanisms: Engine, concrete tools, permission checks, persistence and model transport.
- Closure path: Model tool_use → tool execution/result messages → next model decision; no-tool result ends the turn.
- Why this is / is not agent-owned: Removing the model leaves tool transport but removes task-specific action selection; --auto-approve is supported, while default operation constrains writes with user consent.
- Evidence: [src/core/engine.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/engine.py); [src/tui/app.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/tui/app.py); [src/features/agents/worker_manager.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/agents/worker_manager.py); [src/core/permissions.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/permissions.py)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.
- Boundary reachability: src/tui/app.py constructs Engine and first-party tools; workers use the same Engine in the shipped coordinator mode.

## S2 — Coordination

- State: A
- Function: Attenuate write interference among concurrently running coding workers.
- Disturbance / variety regulated: Two write-heavy workers can modify the same local file set; research can safely overlap.
- Decisive decision or feedback right: Choose which file areas run in parallel, sequence conflicting writes and revise worker instructions.
- Decision owner: The model-backed coordinator under its shipped concurrency instructions.
- Supporting / enforcement mechanisms: Agent/SendMessage tools, worker task IDs, notifications; no file lock is falsely credited as decision owner.
- Closure path: Worker reports return to the coordinator, which synthesizes and sends the next scoped instruction or launches work in a different file area.
- Why this is / is not agent-owned: The prompt supplies a concrete coordination rule for same-file writes; the agent applies its judgment to task/file overlap, rather than a queue alone deciding.
- Evidence: [src/features/coordinator.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/coordinator.py); [src/tui/app.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/tui/app.py); [src/tools/agent.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/tools/agent.py); [src/features/agents/worker_manager.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/agents/worker_manager.py)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Prompt-level coordination is not a hard filesystem reservation or a guarantee that all collisions are prevented.
- Boundary reachability: --coordinator wires the concurrency prompt and worker tools into Engine; notification draining calls run_query on that same engine.
- Distinct S1 units: Two or more tool-using workers producing research/implementation outcomes.
- Inter-S1 disturbance: Concurrent write-heavy tasks on the same file set risk conflicting edits.
- Attenuating coordination relation: Coordinator-directed one-at-a-time work per file set, with safe independent research/verification overlap.
- Feedback into subsequent S1 behaviour: Completion/failure notifications inform synthesized follow-up prompts and worker continuation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shipped concurrency instructions explicitly distinguish same-file writes from independent/read-only work; messages carry the chosen adjustment.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the coding team's current commitments and corrective intervention against the user goal.
- Disturbance / variety regulated: Workers fail or pursue an approach that no longer serves the current goal; wrong-direction work consumes present capacity.
- Decisive decision or feedback right: Stop misdirected running work, retain or replace failed workers, and issue synthesized corrective specifications.
- Decision owner: The model-backed coordinator.
- Supporting / enforcement mechanisms: Worker status/results/usage, TaskStop abort, SendMessage continuation and worker creation.
- Closure path: Current failure or changed-direction evidence reaches coordinator; its stop/restart/replacement decision changes which worker operates and under which instructions.
- Why this is / is not agent-owned: The agent chooses the corrective commitment intervention from team results; the runtime merely aborts or resumes the chosen worker. This is narrower than budget allocation or organization-wide governance.
- Evidence: [src/features/coordinator.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/coordinator.py); [src/features/agents/worker_manager.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/agents/worker_manager.py); [src/tools/agent.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/tools/agent.py); [src/tui/app.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/tui/app.py)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Only the local session/team recursion is credited. Generic user permission and interruption do not independently establish S3=P.
- Boundary reachability: The supported coordinator prompt explicitly instructs failure recovery and stopping wrong-direction work; shipped worker tools implement those choices.
- Whole-system current view: Coordinator receives worker completion/failure, result and usage across the local team, alongside the user goal.
- Current-control decision scope: Present team commitments: continue an existing worker, substitute a fresh one, or stop ongoing wrong-direction work.

## S3* — Complementary audit

- State: —
- Function: No complementary audit outside routine production verification established.
- Disturbance / variety regulated: Worker claims may be wrong; routine checks can miss defects.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Fresh verifier instructions are ordinary research→implementation→verification workflow; review/simplify runs within normal production. No separately governed sporadic audit path is shipped.
- Evidence: [src/features/coordinator.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/coordinator.py); [src/features/skills_bundled.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/skills_bundled.py); [src/features/agents/definitions.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/agents/definitions.py); [src/features/agents/worker_manager.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/agents/worker_manager.py)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [src/features/coordinator.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/coordinator.py); [src/features/skills_bundled.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/skills_bundled.py); [src/features/agents/definitions.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/agents/definitions.py); [src/features/agents/worker_manager.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/agents/worker_manager.py)
- Plausible first-party paths checked: Fresh verification workers, built-in /review and /simplify, Explore isolation, worker result return and normal test instructions.
- Why no material first-party path remains: These provide normal acceptance/recovery, not materially complementary audit access and independent audit control beyond routine reporting. Generic ability to spawn a reviewer is insufficient.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective capability adaptation loop established.
- Disturbance / variety regulated: User/project information and previous mistakes change across sessions.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: KAIROS consolidates internal transcripts and preferences; coordinator research and plan mode address the current task. Neither supplies future-environment adaptation options coupled to current team capability.
- Evidence: [src/features/memory.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/memory.py); [docs/memory.md](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/docs/memory.md); [src/features/coordinator.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/coordinator.py); [src/features/plan.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/plan.py); [src/core/config.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/config.py)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [src/features/memory.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/memory.py); [docs/memory.md](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/docs/memory.md); [src/features/coordinator.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/coordinator.py); [src/features/plan.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/plan.py); [src/core/config.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/config.py)
- Plausible first-party paths checked: Auto-dream memory consolidation, research workers, planning, provider/model configuration and user corrections.
- Why no material first-party path remains: The shipped paths retain current/previous task context or fixed configuration; no function-specific outside-and-then option selection and returned capability change remains. Parent editing settings is not such a loop.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy decision-and-return path established.
- Disturbance / variety regulated: Permissions, tool risk and plan approval constrain work.
- Decisive decision or feedback right: No qualifying first-party decisive right established for this function.
- Decision owner: No qualifying owner at the declared boundary.
- Supporting / enforcement mechanisms: The cited runtime and documentation are supporting surfaces, not decision owners.
- Closure path: No function-specific returned closure at this boundary.
- Why this is / is not agent-owned: Permission choices, plan acceptance, sandbox configuration and saved preferences govern operational actions; they do not route an identity-policy matter to legitimate ultimate authority.
- Evidence: [src/core/permissions.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/permissions.py); [src/features/plan.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/plan.py); [src/tools/plan_tools.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/tools/plan_tools.py); [src/core/context.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/context.py); [src/core/config.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/config.py)
- Basis: structural
- Confidence: high within the declared source boundary
- Caveats: Static source evidence; no live model/provider run or empirical viability claim.

### Absence scope

- Surfaces inspected: [src/core/permissions.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/permissions.py); [src/features/plan.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/features/plan.py); [src/tools/plan_tools.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/tools/plan_tools.py); [src/core/context.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/context.py); [src/core/config.py](https://github.com/e10nMa2k/cc-mini/blob/73c5bc563093b650ea8754bf9101a7507d8328a8/src/core/config.py)
- Plausible first-party paths checked: User prompts, plan mode return, saved configuration/system context and sandbox permission enforcement; parent-governed alternative considered.
- Why no material first-party path remains: No shipped identity/ultimate-policy issue → authority decision → subsequent identity-level regulation loop is supplied. Static prompts and ordinary approvals do not close S5.

## Distributed OSS parent arrangement

The user owns task/permission choices in this local cell. No project-wide distributed parent arrangement or distinct qualifying S3/S4/S5 parent mode is established from public contribution activity.

## Self-hosted and non-human modes

The local CLI and coordinator are first-party self-hosted modes. Model/provider substitution and auto-approve alter enforcement; they do not create new ultimate-policy or adaptation rights.

## Recursion

Workers are durable enough to execute and continue local tasks but no full worker metasystem/viability evidence is established. Spawning is not credited as VSM recursion.

## Variety and escalation

Tool denial/errors, failure notifications and user interruption preserve local disturbances for another action. Notifications are ordinary reporting, not automatically algedonic or S3*. Sandbox and concurrency instructions attenuate different risks.

## Evidence gaps

Static frozen-source assessment only. No live provider/model/agent-quality run; test dependencies (pytest, anthropic, rich, openai) are absent in this runtime, so native tests were not executed. No root LICENSE was found; no licensing assertion is inferred. Optional prompt paths are credited only where wired by app.py. Confidence is source-relative, not a performance/viability guarantee.
