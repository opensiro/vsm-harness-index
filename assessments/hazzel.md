---
harness_id: hazzel
project_name: Hazzel
repository: https://github.com/mukundzha/hazzel
review_ref: 86f15f052d7a0314fb28dca5592b4aada95a7db9
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Hazzel

## Review boundary

- System in focus: first-party Python terminal coding agent in Hazzel, its model/tool loop, safety and diff approval, sessions, /review mode and safe-read dispatch.
- Purpose and identity: edit and examine local source under user approval with clear tool outputs and undo of agent modifications.
- Relevant environment: local Git repository, filesystem, commands/tests, model API, operator permission settings.
- Standard-distribution boundary: native src/hazzel agent and tools. External MCP providers, hosted inference internals and repository maintainer/CI activity are outside.
- Credited operating / distribution surfaces: src/hazzel/agent/core.py, dispatch.py, tools, safety.py, review.py and session/CLI wiring.
- Adjacent first-party surfaces excluded from ownership: demo playback, test fixtures, CI, independent third-party model behavior and optional MCP plugin effects.
- First-party operating / deployment modes considered: interactive tool use, print/headless mode, safe parallel read calls, read-only plan mode, user-invoked /review and sticky /goal, saved sessions and undo.
- Recursion level: one coding session. Tool-call concurrency is not a multi-agent hierarchy.
- Reviewed revision: 86f15f052d7a0314fb28dca5592b4aada95a7db9.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The native Python coding agent in agent/core.py executes streaming or ordinary model calls, normalizes tool call arguments, dispatches them to native project file/shell handlers and inserts results into next model calls. It uses approved diff edits, read-only plan mode, per-turn safe read batching and selective undo. The program can run multiple file reads in a thread pool, but these are suboperations owned by the same coding agent.

The user-invoked /review independently collects Git diff and asks a distinct reviewer prompt/model to evaluate changes, or uses a deterministic heuristic fallback. Findings are displayed for user consideration; they do not automatically trigger a repair turn in the ordinary coding loop. The named /goal tracks user instructions rather than managing several work cells. Retained sessions/skills are contextual support.

Primary pinned evidence: [src/hazzel/agent/core.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/core.py); [src/hazzel/agent/dispatch.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/dispatch.py); [src/hazzel/review.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/review.py); [src/hazzel/safety.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/safety.py).

## Operational model

One model makes real coding choices and responds to code/test results. Separate user-invoked review has potentially useful critical evidence, but fails to prove full independently returned corrective management. No multiple coding S1s or strategic/policy governance is inferred from tools and approvals.

## S1 — Operations

- State: A
- Function: Autonomous source code operations under one model.
- Disturbance / variety regulated: Unfamiliar files, edit requests, execution errors and test failures.
- Decisive decision or feedback right: Choose file/shell tool and next action using returned tool results.
- Decision owner: Primary Python agent in agent/core.py.
- Supporting / enforcement mechanisms: Provider adapter, native dispatch, safety approval, trace, undo and sessions.
- Closure path: Request → model tool call → first-party file/shell handler → result into model history → next tool choice or completion.
- Boundary reachability: The shipped terminal and print modes invoke the native Python coding loop and tool handlers.
- Why this is / is not agent-owned: The primary model selects next coding actions, and first-party tools execute them.
- Evidence: [src/hazzel/agent/core.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/core.py); [src/hazzel/agent/dispatch.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/dispatch.py); [src/hazzel/tools/edit_file.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/tools/edit_file.py).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: The model inference endpoint is external, while first-party code owns tool dispatch and project state..


## S2 — Coordination

- State: —
- Function: No inter-S1 conflict attenuation between multiple autonomous coding work cells.
- Disturbance / variety regulated: Multiple simultaneous read-only tools are not independent S1 units with an inter-cell disturbance.
- Decisive decision or feedback right: No S2 decision right established.
- Decision owner: No S2 decision owner.
- Supporting / enforcement mechanisms: Safe-read thread pool and execution ordering.
- Closure path: Read results return to the same coding agent; no peer-agent behavior regulation.
- Why this is / is not agent-owned: No complete function-specific ownership established beyond ordinary coder operation.
- Evidence: [src/hazzel/agent/core.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/core.py); [src/hazzel/agent/dispatch.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/dispatch.py); [src/hazzel/agent/toolspec.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/toolspec.py).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Boundary-scoped finding from frozen first-party runtime; user authored extras are excluded..

### Absence scope

- Surfaces inspected: Coding loop, parallel safe read tools and background job execution.
- Plausible first-party paths checked: Threaded read calls, tool caching and command backgrounding.
- Why no material first-party path remains: No separate autonomous project work cells or inter-cell interference and correcting coordination return path exist in the native distribution.


## S3 — Inside-and-now control

- State: —
- Function: No whole-current metasystem control over several operational units.
- Disturbance / variety regulated: Single-agent turn stalls, budget warnings and /goal reminders are local operational issues.
- Decisive decision or feedback right: No separate S3 discretionary regulation of shared multi-unit priorities/resources.
- Decision owner: No S3 owner.
- Supporting / enforcement mechanisms: Turn bounds, goal context, job monitoring and command retries.
- Closure path: Failure prompts the same agent to retry or user to intervene, not a whole current resource allocation.
- Why this is / is not agent-owned: No complete function-specific ownership established beyond ordinary coder operation.
- Evidence: [src/hazzel/agent/core.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/core.py); [src/hazzel/agent/history.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/agent/history.py); [src/hazzel/jobs.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/jobs.py); [src/hazzel/__main__.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/__main__.py).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Boundary-scoped finding from frozen first-party runtime; user authored extras are excluded..

### Absence scope

- Surfaces inspected: Agent loop, goal pin, session state, usage and background jobs.
- Plausible first-party paths checked: Budget view, retries, turn cap and goal reminders.
- Why no material first-party path remains: There is no current whole-system view and returned S1 reallocation decision for several independently active coding units.


## S3* — Complementary audit

- State: ?
- Function: Separate read-only Git diff review provides potential independent evidence, but not proven organizational correction closure.
- Disturbance / variety regulated: An agent may introduce code bugs and prematurely claim completion.
- Decisive decision or feedback right: A user-invoked review model judges first-party Git diff using separate reviewer instructions.
- Decision owner: Independent review model when requested; resulting actions are left to human.
- Supporting / enforcement mechanisms: Native diff capture, REVIEW_SYSTEM, bounded snippets and deterministic fallback heuristic.
- Closure path: User invokes /review → separate model analyses actual diff → recommendations shown in terminal; no automatic steering into coding-agent repair.
- Why this is / is not agent-owned: No complete function-specific ownership established beyond ordinary coder operation.
- Evidence: [src/hazzel/review.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/review.py); [src/hazzel/git.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/git.py); [src/hazzel/__main__.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/__main__.py).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: The diff source is real and reviewer separate, but the user must choose whether to act, so A/C audit-feedback ownership remains unresolved..


## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective environment-facing capability adaptation decision loop.
- Disturbance / variety regulated: Future requirements and environmental changes are not scanned for autonomous capability renewal.
- Decisive decision or feedback right: No S4 adaptation right.
- Decision owner: No S4 owner.
- Supporting / enforcement mechanisms: Project skills, session storage, updates and model choice.
- Closure path: Past context informs later messages, but no future external sensing → adaptation decision → operational change path.
- Why this is / is not agent-owned: No complete function-specific ownership established beyond ordinary coder operation.
- Evidence: [src/hazzel/session.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/session.py); [src/hazzel/skills.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/skills.py); [src/hazzel/update_check.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/update_check.py).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Boundary-scoped finding from frozen first-party runtime; user authored extras are excluded..

### Absence scope

- Surfaces inspected: Session store, project skills, release-check and provider configuration.
- Plausible first-party paths checked: Restored history, user-authored skills, app-update notification and provider switch.
- Why no material first-party path remains: No source-native prospective environment scan and autonomous capability-renewal closure is implemented.


## S5 — Policy and identity

- State: —
- Function: No ultimate-purpose or organizational identity governance.
- Disturbance / variety regulated: Per-command permission and project sandbox are operational authority constraints.
- Decisive decision or feedback right: No organization-wide S5 policy/identity choice.
- Decision owner: User decides approvals; code applies safety restrictions.
- Supporting / enforcement mechanisms: Ask-once approval, diff preview, sandbox, deny lists and plan mode.
- Closure path: User approval affects particular command or file action, not binding governance of ultimate identity.
- Why this is / is not agent-owned: No complete function-specific ownership established beyond ordinary coder operation.
- Evidence: [src/hazzel/safety.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/safety.py); [src/hazzel/tools/approvals.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/tools/approvals.py); [src/hazzel/__main__.py](https://github.com/mukundzha/hazzel/blob/86f15f052d7a0314fb28dca5592b4aada95a7db9/src/hazzel/__main__.py).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Boundary-scoped finding from frozen first-party runtime; user authored extras are excluded..

### Absence scope

- Surfaces inspected: Security gates, plan mode, operation approval and CLI setup.
- Plausible first-party paths checked: Tool consent, model/provider selection, undo and goal configuration.
- Why no material first-party path remains: No legitimate ultimate-policy decision actor and binding organization-governance return path is evidenced.


## Distributed OSS parent arrangement

GitHub maintainers, CI, third-party model providers and user-authored MCP servers are not parents of the installed coding-session organization.

## Self-hosted and non-human modes

Ollama and remote API inference route into the same first-party Python coder. Human consent and headless approval flags limit actions, not VSM identity.

## Recursion

Parallel safe tools and background jobs are task operations of a single S1 agent, not peers with S2 coordination. The separate review call does not by itself establish a whole VSM control hierarchy.

## Variety and escalation

Tool failures and repeated operations can change the next model step. Optional diff review returns findings to the human, but the source does not supply an automatic audit corrective action path to the operating coder.

## Evidence gaps

- No genuine inter-agent coordination; read-tool concurrency is not S2.
- On-demand separate diff review is real, but an integrated independent audit-to-repair return is not shown. S3* remains ?.
- Structural repository evidence is not benchmark evidence.
