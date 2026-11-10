---
harness_id: nonstop-agent
project_name: Nonstop Agent
repository: https://github.com/seolcoding/nonstop-agent
review_ref: bc950dcc36cb3fbe92388bd3616e0da53a3ed265
reviewed_at: 2026-11-10
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

# Nonstop Agent

## Review boundary

- System in focus: the shipped first-party Python `nonstop-agent` CLI/package, its Claude Agent SDK binding, initializer/coding session driver, tool and permission configuration, project progress files, optional existing-project analysis and resumption.
- Purpose and identity: keep a single model-backed coding project progressing across short-lived sessions by providing prompts, tool access, durable checkpoints and automatic re-entry.
- Relevant environment: chosen codebase, evolving tests and feature checklist, filesystem and Git, Claude SDK/provider, CLI operator and OS sandbox.
- Standard-distribution boundary: installed `nonstop-agent` launches SDK `query` with its own coding/initializer/analysis prompts, tool schema, project directory, and security hooks; it classifies the next run and persists session identifiers. The SDK performs low-level model/tool dispatch and provider inference. First-party runner owns the bounded long-running workflow, not the underlying LLM implementation.
- Credited operating / distribution surfaces: [CLI entrypoint](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/main.py), [agent/session loop](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/agent.py), [SDK options](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/client.py), [project progress](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/progress.py), [command hook](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/security.py), [prompt templates](https://github.com/seolcoding/nonstop-agent/tree/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/prompts).
- Adjacent first-party surfaces excluded from ownership: Anthropic Claude Code internals/model provider, README tutorial claims, tests/fixtures and alternate `skills/templates` scaffolds copied into downstream projects, any independently installed external agent or model.
- First-party operational modes: CLI `--project-dir` default new-project initializer, subsequent coding loops, `--analyze-first` existing-project preflight, `--resume` SDK session resume, `--max-iterations` cap and optional system prompt/model override.
- Recursion: one autonomous coding task per chosen project directory across sequential sessions. The initializer, analyzer and coding stage are successive operating roles, not independent concurrently negotiating departments.
- Reviewed source: `bc950dcc36cb3fbe92388bd3616e0da53a3ed265`, immutable Index intake #3047, controller #3048; reviewed 2026-11-10; Profile 0.2.4; Methodology 0.3.8. This is source-static evidence, not a live Claude-provider test.

## Repository architecture

The [CLI](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/main.py) verifies presence of the Claude OAuth environment and invokes `run_autonomous_agent`. The [driver](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/agent.py) selects initial analysis or initializer based on flags and `feature_list.json`, then chooses a coding prompt on subsequent iterations. Each session calls the Claude Agent SDK `query`; the configured [client](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/client.py) grants Read/Write/Edit/Grep/Glob/Bash/Web tools, project workdir, sandbox, file checkpointing, and a first-party `PreToolUse` Bash security hook. The generator agent can inspect a project and autonomously select tool actions through the SDK. Result events and model text are displayed; the session ID is saved for future resume, and a new prompt is launched after a fixed delay.

The [progress state](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/progress.py) counts features marked `passes` and reads/writes `claude_session.json`; it does not independently adjudicate actual implementation quality. Importantly, the outer `while True` in `run_autonomous_agent` ends on a supplied iteration cap, not a sourced autonomous global completion decision; an uncapped run can keep launching sessions even if all features pass. Security validation controls Bash actions but is not semantic quality audit. [Architecture README](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/README.md) explains the intended initializer/coder handoff and progress-file pattern.

## Operational model

- S1: a sequential model-backed coding worker repeatedly receives a scoped prompt, chooses and uses project tools through Claude Agent SDK, observes outputs, and continues with an updated repository/feature file.
- Control plane: Python dispatcher selects phase with fixed state tests, enforces iteration count, configures permissions and records session IDs; progress records inform the next task but do not own an S3/S4 policy decision.
- Outcome: evolving code/tests and feature checklist in the chosen directory; actual functional correctness is not certified by source review.

## S1 — Operations

- State: A
- Function: autonomous execution of project coding/initialization tasks with feedback from repository and tool state.
- Disturbance / variety regulated: missing files, tool errors, evolving project requirements and test failures across a coding session, with cross-session working state reused.
- Decisive decision or feedback right: select edits, commands, searches, implementation and debugging steps from changing evidence.
- Decision owner: the configured Claude model-backed coding/initializer agent invoked through the first-party `run_agent_session`; Python runner determines session role and limits, while SDK handles agent/tool protocol.
- Supporting / enforcement mechanisms: [Claude SDK options](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/client.py), model-visible prompts, sandbox, tool allowlist, Bash hook, durable Git/progress file and saved session ID.
- Closure path: CLI task → first-party session prompt → SDK model decision → permitted file/command/tool call → tool result back to model → model revises approach/output; outer runner saves ID and launches later coding iteration in the same project.
- Boundary reachability: [CLI](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/main.py) calls [actual driver](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/agent.py) and [SDK query](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/client.py) with a real project workdir, rather than only exporting an abstract adapter; token and provider execution are required at runtime.
- Why this is / is not agent-owned: the model makes semantic next-action choices while the Python package explicitly wires it into a runnable, persistent working loop. Removing model decisions would leave only fixed file/phase scheduling and tool security.
- Evidence: [model session invocation and feedback](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/agent.py), [SDK tools and permissions](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/client.py), [entry](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/main.py).
- Basis: first-party implementation and invoked mode traced source-first.
- Confidence: high structural confidence for actual runnable agent loop, without provider execution verification.
- Caveats: agent quality, successful Claude OAuth, tool compatibility and tests passing on live projects were not experimentally established.

## S2 — Coordination

- State: —
- Function: no independent inter-S1 conflict attenuation among simultaneously operating cells at the reviewed single-project recursion.
- Disturbance / variety regulated: handoff between initializer and coding roles is serial; no overlapping S1 decisions shown to compete over shared operations.
- Decisive decision or feedback right: coordinate conflicting choices of multiple autonomous S1 teams; no first-party actor owns such a right.
- Decision owner: Python fixed phase dispatch and one model-worker context at a time, not a coordination metasystem.
- Supporting / enforcement mechanisms: sequential initializer/coder prompts, `feature_list.json`, iteration count and session resumption.
- Closure path: initial feature scaffold → next coding session; no inter-agent oscillation/conflict evidence returns to a coordinating decision mechanism.
- Why this is / is not agent-owned: a '2-Agent Pattern' naming two sequential roles does not establish multiple independent operational cells or S2-specific feedback.
- Evidence: [session phase loop](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/agent.py), [progress](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/progress.py).
- Basis: source-static structural.
- Confidence: high within first-party CLI modes.
- Caveats: downstream user-created multi-agent systems are outside the first-party package boundary.

### Absence scope

- Surfaces inspected: phase selection, initializer/coder prompts, progress storage, SDK configuration and documented resumption.
- Plausible first-party paths checked: two-agent recipe and multiple successive Claude sessions, which are not concurrently conflicting S1 units.
- Why no material first-party path remains: no independent first-party inter-S1 relation with a conflict signal, attenuating response and feedback is implemented.

## S3 — Inside-and-now control

- State: —
- Function: no demonstrated portfolio-wide current operations supervision and discretionary intervention.
- Disturbance / variety regulated: progress count and file state are visible, but fixes and priority choices remain within the working agent's local task.
- Decisive decision or feedback right: revise current portfolio-level resources, commitments and work priority; not exposed by the fixed launcher.
- Decision owner: one model worker for individual feature changes and the operator for the project specification, model and run cap.
- Supporting / enforcement mechanisms: progress summary, iteration count, feature checklist and phase prompts.
- Closure path: observe `feature_list.json` count → report local progress and launch next coding prompt; no discretionary whole-current supervisory intervention.
- Why this is / is not agent-owned: fixed progress printing and continuation do not establish S3 with current-system decision authority, nor a human-centered S3=P intervention return.
- Evidence: [outer loop](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/agent.py), [progress counter](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/progress.py).
- Basis: source-static.
- Confidence: medium-high in documented shipped modes.
- Caveats: a project owner may manually act on progress outside this harness.

### Absence scope

- Surfaces inspected: phase driver, `feature_list` progress, persisted sessions, CLI run settings and prompts.
- Plausible first-party paths checked: outer session selection, auto-restart, progress logging and operator pause/resume.
- Why no material first-party path remains: none has a current whole-system state → autonomous management intervention → returned S1 reallocation closure path.

## S3* — Complementary audit

- State: —
- Function: no separately owned complementary audit checking an S1 output independently of the producing worker.
- Disturbance / variety regulated: model may test code and Bash calls are filtered, but both remain inside the single producer's workflow or static permission policy.
- Decisive decision or feedback right: challenge completed code based on independent evidence and force corrective review; no dedicated first-party verifier holds that right.
- Decision owner: coding model or developer-defined command allowlist, not an independently delegated evaluator.
- Supporting / enforcement mechanisms: test-oriented coding prompt, security hook, feature checklist and SDK file checkpoints.
- Closure path: coding agent tests and marks progress as part of its own task; fixed hook can deny unsafe Bash; neither sends a separate independent audit finding to the worker.
- Why this is / is not agent-owned: self-review and safety restrictions are not a complementary auditor with independent assessment and corrective authority.
- Evidence: [agent driver](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/agent.py), [security hook](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/security.py), [SDK opts](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/client.py).
- Basis: source-static.
- Confidence: medium-high for the first-party run loop.
- Caveats: external CI or human review may audit these generated projects, but are not part of the source-proven active mode.

### Absence scope

- Surfaces inspected: model session outputs, test/progress handling, defense-in-depth security and feature passes flag.
- Plausible first-party paths checked: self-tests, checklists and security hook validation.
- Why no material first-party path remains: all checks are performed by the same coding agent or fixed rule, with no independent evidence/decision path feeding correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: no ongoing first-party future-environment intelligence and adaptation loop.
- Disturbance / variety regulated: `--analyze-first` inspects an existing repository as current problem context, not prospective shifts in an external environment.
- Decisive decision or feedback right: choose strategy based on future threats/opportunities and alter capabilities; not demonstrated by this CLI.
- Decision owner: operator supplies project goal/prompts, and the coding agent works on immediate existing project state.
- Supporting / enforcement mechanisms: analysis/initializer prompts, current files, CLI flags and progress state.
- Closure path: one-time project analysis → initializer/coder work; no future distinction → adaptation option → operating-system policy update.
- Why this is / is not agent-owned: analyzing present code and resuming tasks is current S1 work, not S4 strategic intelligence.
- Evidence: [mode selection](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/agent.py), [CLI arguments](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/main.py).
- Basis: source-static.
- Confidence: medium-high in shipped modes.
- Caveats: a user could provide an S4 research goal, but capability in the supplied task is not endogenous S4 ownership.

### Absence scope

- Surfaces inspected: existing-project analysis mode, prompts, project state, resume and CLI settings.
- Plausible first-party paths checked: project re-analysis and WebSearch tool authorization.
- Why no material first-party path remains: no future-oriented first-party sensing program, adaptation option owner and return-to-current operations path.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate-policy identity mediation over different S3/S4 commitments.
- Disturbance / variety regulated: sandbox, access and command limits regulate tool safety, not organizational mission.
- Decisive decision or feedback right: reconcile mission, acceptable risk and multiple governance claims; not exercised by the static program.
- Decision owner: operator sets spec, token, model and policy; hard-coded command hook enforces limits; coding model pursues local goal.
- Supporting / enforcement mechanisms: `PreToolUse` Bash allowlist, OS sandbox, permission mode, project directory and user-supplied prompts.
- Closure path: configured policy → allow/deny individual tool call; there is no identity-level decision fed back into operational strategy.
- Why this is / is not agent-owned: static safety enforcement is an important constraint but not autonomous S5 deliberation or mandate setting.
- Evidence: [SDK settings](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/client.py), [Bash command hook](https://github.com/seolcoding/nonstop-agent/blob/bc950dcc36cb3fbe92388bd3616e0da53a3ed265/src/nonstop_agent/security.py).
- Basis: source-static.
- Confidence: medium-high in reviewed distribution.
- Caveats: human owner and hosting provider may hold S5 rights at a parent recursion.

### Absence scope

- Surfaces inspected: command policy, sandbox and permissions, CLI options and project spec.
- Plausible first-party paths checked: customizable allowlist, authentication, project instructions and role prompts.
- Why no material first-party path remains: they constrain local actions, without a policy-identity arbitration mechanism or S3/S4 organizational return.

## Recursion

One running coding project is the assessed S1. Initializer, analyzer and continuing coder are successive modes of its long-running operation. Claude SDK is a separately distributed agent engine, but Nonstop Agent's first-party CLI actively binds it to an executable project loop. The project owner/provider may form a parent recursion, not credited here.

## Variety and escalation

Short-lived contexts and Git/progress checkpoints help absorb long-task state and tool variety. Errors trigger a timed restart; source code does not demonstrate automatic recognition of all-features-completed as a terminal stop in uncapped mode. Escalation of global scope, provider billing and risk tolerance remains human-configured.

## Evidence gaps

- Source review only: no Claude OAuth call, tool execution, live project testing or verified long-duration reliability.
- README claims of production readiness and security are not independently benchmarked.
- Future independently staffed auditor, external environment intelligence or policy layer would need first-party operational evidence at its own recursion.
