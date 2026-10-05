---
harness_id: riffer-rig
project_name: riffer-rig
repository: https://github.com/bottrall/riffer-rig
review_ref: e2e914195f7c15c75ee2ae6bb55d772d754a2f37
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# riffer-rig

## Review boundary

- System in focus: the concrete first-party riffer-rig terminal coding application at frozen revision `e2e914195f7c15c75ee2ae6bb55d772d754a2f37`, including its configured coding agent, first-party read/write/edit/bash tools, runtime wrapper, REPL, prompt/instruction composition, hooks/guardrails, model/provider selection and session snapshot surfaces.
- Purpose and identity: provide an interactive terminal coding agent that can inspect, edit and execute a project through a model/tool loop.
- Relevant environment: user coding requests, repository/filesystem state, shell/build/test outputs, configured model provider, AGENTS.md instructions and optional user/project skills.
- Standard-distribution boundary: repository-owned riffer-rig coding composition and first-party tools/runtime wrapper are inside. The generic `riffer` gem runtime and external model providers remain dependencies and cannot donate organizational functions not concretely instantiated by the rig.
- Credited operating / distribution surfaces: installed `riffer` executable, `CodingAgent`, interactive REPL, built-in tools, bundled extensions, runtime/session snapshots, hooks/guardrails, model switching and AGENTS.md/skill loading.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests, release automation, build plans, examples and any future generic-riffer behavior not instantiated by this frozen rig.
- First-party operating / deployment modes considered: ordinary interactive terminal coding and supported embedded/runtime use of the same configured coding composition.
- Recursion level: one riffer-rig coding session is the focal S1 operational unit. Tool calls, extensions, hooks and skills are mechanisms/capabilities rather than separate S1 units.
- Reviewed revision: `e2e914195f7c15c75ee2ae6bb55d772d754a2f37`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

riffer-rig defines a concrete `CodingAgent < Riffer::Agent` with unlimited steps, coding-specific instructions and four bundled tools: read, write, edit and bash. The terminal REPL streams one user prompt into that agent and renders reasoning, tool activity and results. Tool errors are returned to the model as ordinary feedback, allowing subsequent turns to revise the work.

The repository also supplies a first-party Runtime wrapper with cancellation, hooks, guardrails, tool allowlists and snapshot/restore support. Session snapshots preserve conversation/model/skill activation state, but the repository explicitly states that persistent session storage/listing/resume selection is not implemented here yet. AGENTS.md and skills alter prompt context, and model switching changes the provider used within the same operational session.

## Operational model

A user prompt enters the configured coding agent. The model decides whether and how to use read/write/edit/bash, receives concrete filesystem or command results, and continues reasoning/tool use until the turn completes. The REPL then accepts the next user prompt against the same session. Runtime hooks and guardrails can block/transform requests or tool calls, but they do not create a separate organizational decision layer.

## S1 — Operations

- State: A
- Function: autonomously perform coding work through model-selected repository inspection, edits, writes and shell execution.
- Disturbance / variety regulated: unfamiliar codebases, incomplete task information, file state, failing commands/tests, ambiguous edit targets, model/provider outputs and user corrections.
- Decisive decision or feedback right: choose the next coding/tool action, interpret tool errors/results and revise subsequent actions until the requested coding outcome is reached.
- Decision owner: the active model-backed riffer-rig CodingAgent.
- Supporting / enforcement mechanisms: `CodingAgent`, generic-agent execution instantiated by the rig, read/write/edit/bash tools, REPL streaming, runtime cancel flag, hooks/guardrails, AGENTS.md prompt section and provider/model configuration.
- Closure path: user/project context → model selects action/tool → tool executes against the working directory → result/error returns to the agent context → model changes subsequent action until completion or cancellation.
- Boundary reachability: the installed `riffer` executable directly instantiates the repository-owned CodingAgent and bundled coding tools; no adjacent development workflow or unconfigured generic runtime feature is required.
- Why this is / is not agent-owned: removing the model actor leaves tools, UI and runtime wrappers but removes the open-ended decisions that turn repository evidence into coding actions.
- Evidence: README; `lib/riffer/rig/coding_agent.rb`; `lib/riffer/rig/repl.rb`; `lib/riffer/rig/tools/read.rb`; `write.rb`; `edit.rb`; `bash.rb`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the generic `riffer` execution kernel is a dependency; only behavior concretely instantiated by the frozen riffer-rig composition is credited.

## S2 — Coordination

- State: —
- Function: no distinct coordination function among multiple S1 operational units is established.
- Disturbance / variety regulated: the focal runtime may execute tools and load extensions/skills, but the standard coding application exposes one model-backed coding unit rather than peer S1 units with an interference relation.
- Decisive decision or feedback right: no S2-specific choice over inter-S1 conflict, oscillation or mutual adjustment was found.
- Decision owner: not established at S2 level.
- Supporting / enforcement mechanisms: runtime busy state, cancellation, extension ordering and per-runtime working directory.
- Closure path: these mechanisms constrain one operational session and do not feed a coordination result back into distinct peer S1 units.
- Why this is / is not agent-owned: serialization, extension ordering and tool composition do not establish S2 without a concrete inter-S1 disturbance.
- Evidence: README; `lib/riffer/rig/runtime.rb`; `docs/TOOLS.md`; `docs/SESSIONS.md`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: embedders can construct multiple runtimes externally, but the frozen first-party rig does not supply a peer-coordination relation among them.

### Absence scope

- Surfaces inspected: CodingAgent, Runtime, REPL, bundled tools/extensions, snapshots, skills, hooks and provider/model configuration.
- Plausible first-party paths checked: concurrent tools as S1 peers; multiple Runtime instances as S2; extension replacement/order as coordination; skills as collaborating operational units.
- Why no material first-party path remains: the standard distribution contains one focal coding actor and no implemented interference/attenuation/feedback relation among distinct S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established.
- Disturbance / variety regulated: cancellation, runtime busy/closed state, tool allowlists and request/tool guardrails constrain current execution within one session.
- Decisive decision or feedback right: no separate owner has a whole-system current view and substantive authority over shared resources, commitments, priorities or interventions across multiple operations.
- Decision owner: not established at S3 level.
- Supporting / enforcement mechanisms: Runtime busy/closed state, cancel flag, request/tool guardrails, hooks, model switching and host notifications.
- Closure path: these controls alter or stop the focal session's current action path but do not form a whole-current metasystemic loop.
- Why this is / is not agent-owned: local execution controls and guardrails are enforcement around S1, not whole-system management.
- Evidence: `lib/riffer/rig/runtime.rb`; `runtime/request_guardrail.rb`; runtime hooks; REPL model switching.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an embedding application could add fleet management, but such an adjacent composition is outside this concrete coding rig.

### Absence scope

- Surfaces inspected: Runtime state, cancellation, hooks/guardrails, tool allowlists, session snapshots, model switching, REPL and host interfaces.
- Plausible first-party paths checked: Runtime as manager/S3; guardrails as current-control authority; model switching as resource allocation; session snapshots as whole-system state.
- Why no material first-party path remains: all inspected controls are scoped to one session or preconfigured request/tool policy and lack a whole-system current view plus substantive shared-resource/commitment authority.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established.
- Disturbance / variety regulated: tool results, command/test failures, hooks and repository tests can reveal mistakes, but they remain ordinary production feedback or adjacent development checks.
- Decisive decision or feedback right: no separate reviewer/evaluator owns an independent claim-checking judgment that returns findings into a current-control path.
- Decision owner: not established at S3* level.
- Supporting / enforcement mechanisms: shell/test output, after-tool hooks, notifications and repository test suite.
- Closure path: runtime evidence returns to the same coding agent or host; no distinct complementary-access audit loop is supplied.
- Why this is / is not agent-owned: self-checking via bash/tests and hook observation are ordinary operational evidence, not S3*.
- Evidence: `lib/riffer/rig/tools/bash.rb`; runtime hooks/events; repository tests.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an extension could implement review behavior, but no such first-party review path is instantiated in the frozen standard rig.

### Absence scope

- Surfaces inspected: coding tools, hooks/events, guardrails, session snapshots, repository tests, AGENTS.md and skill surfaces.
- Plausible first-party paths checked: command/test output as verifier; after-tool hooks as audit; repository tests as S3*; skills/instructions as reviewer.
- Why no material first-party path remains: these are in-band operational feedback, observation or adjacent development testing rather than a separate sufficiently independent audit channel.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop is established.
- Disturbance / variety regulated: AGENTS.md, user/project skills, provider/model settings and snapshots can change the context used by later turns or restored sessions.
- Decisive decision or feedback right: no first-party process senses environmental/future change, generates adaptation options for the rig and returns a selected adaptation into current capability.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: live AGENTS.md loading, filesystem skill backend, model/provider configuration and runtime snapshot/restore.
- Closure path: operator-authored instructions/configuration or saved session state are loaded into later operation; no autonomous external-and-prospective adaptation conversation exists.
- Why this is / is not agent-owned: context loading and extensibility reuse externally supplied material but do not autonomously develop future-oriented adaptation options.
- Evidence: README; `lib/riffer/rig/prompts/agents_md.rb`; `lib/riffer/rig/coding_agent.rb`; `docs/SESSIONS.md`; `settings.rb`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: skills may encode reusable procedures, but this repository does not supply a learning/evolution loop that creates or revises them from environmental evidence.

### Absence scope

- Surfaces inspected: AGENTS.md loading, skills, snapshots/restores, model/provider settings, extensions/hooks and session documentation.
- Plausible first-party paths checked: snapshots as memory/adaptation; live AGENTS.md as environmental sensing; skills as learning; extension replacement as self-improvement; model switching as adaptation.
- Why no material first-party path remains: every inspected path loads operator-authored/current configuration or historical state and does not generate prospective adaptation options or close them back into capability.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure is established.
- Disturbance / variety regulated: AGENTS.md instructions, tool allowlists, hooks/guardrails, settings and provider credentials constrain ordinary execution.
- Decisive decision or feedback right: no identity/ultimate-policy issue is routed to a legitimate ultimate authority and returned as a durable governing decision for the harness.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: instruction hierarchy, request/tool guardrails, tool allowlists, settings and credentials.
- Closure path: constraints affect current prompts/tool calls/configuration but do not close identity-level policy questions for subsequent operation.
- Why this is / is not agent-owned: static/configurable prompts and guardrails are execution policy mechanisms, not S5.
- Evidence: `prompts/agents_md.rb`; `runtime/request_guardrail.rb`; `runtime.rb`; `settings.rb`; README.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: project maintainers and users can change instructions/configuration outside the run, but that adjacent authority is not a first-party S5 runtime loop.

### Absence scope

- Surfaces inspected: AGENTS.md hierarchy, settings, hooks/guardrails, tool allowlists, credentials, runtime lifecycle and repository governance.
- Plausible first-party paths checked: AGENTS.md as constitution; guardrails as policy; model settings as identity; user configuration as parent authority; maintainer governance as runtime S5.
- Why no material first-party path remains: inspected mechanisms constrain ordinary operation or belong to adjacent development/user configuration and do not form an identity-policy issue/authority/return loop.

## Recursion

The frozen product exposes one focal coding-agent session. Extensions, skills and tools are subordinate capabilities, and externally created multiple runtimes are not a first-party recursive organization by themselves.

## Variety and escalation

The coding actor absorbs variety through iterative read/write/edit/bash use, prompt context and skills. Tool failures return as model-readable errors, while cancellation and guardrails can interrupt or block work. Those are operational controls rather than higher VSM functions.

## Evidence gaps

No `?` state is required. The frozen repository exposes the concrete coding composition, runtime wrapper, tool surfaces, sessions/snapshots, hooks/guardrails and configuration sufficiently to support S1 and the negative S2/S3/S3*/S4/S5 findings.

## Assessment summary

riffer-rig closes autonomous S1 through its concrete coding-agent and first-party tools. It does not establish peer S2, whole-current S3, complementary S3*, prospective S4 or identity-level S5 within the frozen standard distribution.

**Vector:** A · — · — · — · — · —
