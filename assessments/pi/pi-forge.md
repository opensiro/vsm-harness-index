---
harness_id: pi-forge
project_name: pi-Forge
repository: https://github.com/djtoon/pi-forge
review_ref: 3af0d73a0f45701a4b1324d3b3bb272bc312ef2e
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# pi-Forge

## Review boundary

- System in focus: The first-party pi-Forge agent-harness builder and the generated agents that its supported launcher/web UI can run and upgrade locally.
- Purpose and identity: Interview a user, build or update specialized model-driven harnesses with tools, skills, prompts and domain views, then run those harnesses in browser, terminal or headless modes.
- Relevant environment: User requests, local repositories/files, tool APIs, available model providers, independently configured generated harnesses and their subsequent workload.
- Standard-distribution boundary: `npm run forge` (web/TUI), the generated `runHarness` launch path, first-party builder skills/tools, scoped browser “Add to” agent and autoreload, and headless/RPC paths. Provider inference is external.
- Credited operating / distribution surfaces: `forge/bin/forge.ts`, `forge/custom/extensions/forge-tools.ts`, builder/interview/update skills, `packages/harness-core`, `packages/harness-web` builder/main channel and `packages/forge-gen` spec/generation logic.
- Adjacent first-party surfaces excluded from ownership: Bundled chemistry/loan examples, static templates, CLI packaging, tests, docs and CI are examples/deployment mechanisms, not independent managers or auditors.
- First-party operating / deployment modes considered: Forge model-agent through TUI/web; generated model-agents through TUI/web/headless/RPC; browser-scoped builder mode for supported non-Forge harnesses. Read-only/workspace sandbox policies and provider credentials configure allowed actions.
- Recursion level: A locally deployed builder-plus-generated-harness arrangement, with the active task agent as S1 and Forge's prospective customization path acting on its future capabilities. The generated harness itself can alternatively be viewed as a nested local system, not a shared distributed organization.
- Reviewed revision: `3af0d73a0f45701a4b1324d3b3bb272bc312ef2e`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`forge/bin/forge.ts` invokes `runHarness` from the generated core. A `harness.yaml` describes model, tools, guards, prompt, skills, views and UI. The Forge agent uses first-party tools (`forge_ask`, `forge_init`, `forge_validate`, `forge_generate`, `forge_smoke`, etc.) and instructional skills to create or change this specification and custom code. The generator makes a pi-based package and launcher; each launched agent uses model-directed tools and its own session. Web server code wires separate main and builder channels: the scoped builder launches Forge in RPC mode with a target-specific prompt, then reloads the revised main harness/spec/views when generation changes materialize. See [Forge launcher](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/bin/forge.ts), [builder wiring](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/packages/harness-web/src/index.ts), [forge tools](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/custom/extensions/forge-tools.ts), [README](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/README.md).

## Operational model

Within the supported model/provider mode, a pi agent selects built-in and custom tool operations while executing a user task. For Forge, that task can be creating a new harness; for generated agents it can be domain-specific work. The separate customization channel can diagnose a capability request, choose prospective tool/skill/view changes, write them, validate/generate and trigger a subsequent main-agent reload. An interview and human request establish goals, not who chooses the implementation. Deterministic generators, sandboxes, plans, UI display and type-checks remain supporting machinery.

## S1 — Operations

- State: A
- Function: Model-backed Forge and generated pi agents perform their user-delegated building or domain work by selecting tools and adapting responses to results.
- Disturbance / variety regulated: User demands, current workspace state, unavailable credentials, files, tool failures and environment/domain data.
- Decisive decision or feedback right: Decide what to ask, read, write, run, validate or explain on subsequent model turns within available tools and policy.
- Decision owner: The active pi model session in the supported real-provider harness run; user defines goals and guardrails.
- Supporting / enforcement mechanisms: `runHarness`, pi session/tool APIs, `forge-tools`, `custom/skills`, model settings, guard hooks, CLI/web/RPC transport and plan UI.
- Closure path: User/domain request → model chooses tool and arguments → first-party tool executes or denies → result/observation returns to model for next step.
- Boundary reachability: `forge` CLI launches a generated first-party harness in web/TUI and documented generated harness commands expose the same model-tool loop in headless/RPC modes.
- Why this is / is not agent-owned: Without model choice, the tools and generator can be called directly but do not decide how to fulfill an open-ended user request.
- Evidence: [launcher](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/bin/forge.ts), [harness core](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/packages/harness-core/src/index.ts), [Forge tools](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/custom/extensions/forge-tools.ts), [interview skill](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/custom/skills/harness-interview/SKILL.md).
- Basis: structural.
- Confidence: high.
- Caveats: Requires configured model provider; static source analysis does not certify model results, user-approval behavior or build success.

## S2 — Coordination

- State: —
- Function: No first-party S2-specific anti-interference loop across distinct concurrently operating agent units was established.
- Disturbance / variety regulated: Main and builder sessions might contend for files or user interaction; multiple generated harnesses might share host resources.
- Decisive decision or feedback right: No independent actor identifies and resolves particular cross-S1 interference through an adjustment returned to both units.
- Decision owner: The server routes channels and reload events; users may direct sessions, but there is no explicit agent-owned inter-S1 coordinator.
- Supporting / enforcement mechanisms: Per-harness session directories, main/builder channel separation, spec manifest and deterministic reload hooks.
- Closure path: Builder changes trigger refresh of the main harness; this is capability adaptation, not conflict recognition and mutual inter-agent coordination.
- Why this is / is not agent-owned: A separate builder channel and session router do not establish S2 merely because two agents exist.
- Evidence: [web channels](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/packages/harness-web/src/index.ts), [harness update skill](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/custom/skills/harness-update/SKILL.md).
- Basis: structural.
- Confidence: medium.
- Caveats: A custom generated harness could introduce its own S2 in code outside this reviewed standard arrangement.

### Absence scope

- Surfaces inspected: Main/builder RPC channels, builder prompt and reload logic, harness-core sessions and generator contracts.
- Plausible first-party paths checked: Concurrent user sessions, builder/main file interactions, reload lifecycle, shared workspace and plan visibility for specific interference-handling feedback.
- Why no material first-party path remains: These isolate, route or update capability; no shipped S2-specific conflict sensing/attenuation relation between operating S1s is closed.

## S3 — Inside-and-now control

- State: —
- Function: No whole-arrangement discretionary supervisory control over current priorities, resources or commitments of multiple operating S1 units was identified.
- Disturbance / variety regulated: Current agent execution status, multi-step progress, missing keys, safety limits and session lifecycle.
- Decisive decision or feedback right: No manager uses a whole-system operational view to revise allocation or current commitments across agents.
- Decision owner: User selects harness/model/policies; each model owns its own task; web server enforces channel/session management.
- Supporting / enforcement mechanisms: `update_plan`, usage UI, model selector, RPC process lifecycle, static guard settings, session restart and status display.
- Closure path: Plans and status feed back to the same task agent or user; no cross-unit supervisory current-control judgment returns to regulate the whole.
- Why this is / is not agent-owned: Local planning, visibility and process control do not establish a managerial S3 function by themselves.
- Evidence: [core](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/packages/harness-core/src/index.ts), [web](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/packages/harness-web/src/index.ts), [plan](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/forge_modules/plan/plan.ts).
- Basis: structural.
- Confidence: high.
- Caveats: An operator may stop/steer a session, but this alone is not a parent-governed whole-system S3 mode.

### Absence scope

- Surfaces inspected: Launch and session lifecycle, plan tool, web model/status control, browser builder separation and configuration.
- Plausible first-party paths checked: Agent status monitoring, plan progress, concurrent channels, reload commands and operator permissions as current whole-system control.
- Why no material first-party path remains: Controls target individual sessions or static policy; no first-party discretionary whole-system operational management loop appears.

## S3* — Complementary audit

- State: —
- Function: No independent complementary auditor challenges ordinary task-success claims and returns findings to a separate current-control owner.
- Disturbance / variety regulated: Incorrect generated code, invalid specs, broken tools or misleading completion reports.
- Decisive decision or feedback right: Validators and smoke/load checks mechanically test constraints but have no independent agent-owned audit judgment.
- Decision owner: Forge's same task/build agent initiates checks; deterministic validators enforce configured formats, and the user may inspect output.
- Supporting / enforcement mechanisms: `forge_validate`, `forge_smoke`, view checker, type checks and generated-file edit detection.
- Closure path: Validation errors return to the same builder agent for repair; no independent complementary audit/report-to-S3 route is wired.
- Why this is / is not agent-owned: Testing an artifact, even in a separate subprocess, is ordinary build QA unless complementary independent audit ownership is established.
- Evidence: [Forge tools](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/custom/extensions/forge-tools.ts), [update skill](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/custom/skills/harness-update/SKILL.md).
- Basis: structural.
- Confidence: medium.
- Caveats: A developer can add independent review through custom code; not part of the first-party loaded mode.

### Absence scope

- Surfaces inspected: Generator validation, smoke tests, view checks, builder skill and report/feedback surfaces.
- Plausible first-party paths checked: Separate testing commands, generated-file manifests, artifact diffs and human approval for direct evidence access, independent audit judgment and corrective return.
- Why no material first-party path remains: They are invoked by the same builder path or enforce static rules; an independent complementary audit actor/authority is not instantiated.

## S4 — Outside-and-then intelligence

- State: A
- Function: Forge's model-based builder interprets prospective capability needs and develops changes to a target agent's future tools, skills, views, prompts and model settings.
- Disturbance / variety regulated: New domain requirements, tool gaps, user-identified failures and changing future tasks beyond the target agent's present tool repertoire.
- Decisive decision or feedback right: Choose a capability design, ask targeted clarifying questions, implement and iterate on candidate spec/code/skill changes for subsequent operation.
- Decision owner: The Forge model agent, within user-defined scope and file/guard permissions; deterministic generation and smoke checks enforce its design.
- Supporting / enforcement mechanisms: Scoped `builderPrompt`, `harness-update`, tool/view/skill-builder skills, `forge_generate`, `forge_smoke`, reload and target-specific custom directories.
- Closure path: User/future task distinction and existing harness inspection → model chooses a design → spec/code edits and validation → generator writes target package → web auto-reload or `/reload` exposes the new capability to later S1 turns.
- Boundary reachability: The web server creates a dedicated Forge RPC builder for non-Forge harnesses and calls `reloadHarness` on settled modifications; Forge itself exposes build/update tools in normal model sessions.
- External distinction: User-provided new workflow requirements and missing integrations, checked against target spec and tool inventory.
- Future / prospective distinction: A new tool/skill/prompt is intended for subsequent tasks and new harness sessions, not simply to answer the current domain question.
- Adaptation option generated: An agent-chosen modified `harness.yaml`, custom extension, skill and/or view, with validation and smoke-test plan.
- Path back into current capability / S3: Generated assets and the main agent are reloaded; next user request can use new tools or knowledge.
- Why this is / is not agent-owned: Although the human requests a capability, the model chooses the implementation and artifacts; the generator does not determine what should be built.
- Evidence: [builder wiring](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/packages/harness-web/src/index.ts), [update skill](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/custom/skills/harness-update/SKILL.md), [tools](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/custom/extensions/forge-tools.ts), [README](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Capability change is often user-initiated and may need approval/credentials; no autonomous long-horizon self-improvement mandate or guaranteed tested success is asserted.

## S5 — Policy and identity

- State: —
- Function: No binding adjudication of ultimate harness identity/policy disputes by an autonomous or evidenced parent S5 path was found.
- Disturbance / variety regulated: Sandbox scope, protection of files, model/provider restrictions, acceptable tools and target identity.
- Decisive decision or feedback right: Users select guards, models and targets in specs/settings; tool approval denies selected actions but no identity-level issue is escalated and ruled on through a first-party loop.
- Decision owner: User/developer controls policy/configuration and can intervene per action; Forge may edit lower-level settings only within permissions.
- Supporting / enforcement mechanisms: `harness.yaml` guards, sandbox modes, protected paths, confirmation prompts, credentials and spec validation.
- Closure path: Existing rules block or permit local actions; no legitimacy-governed S5 identity conversation and subsequent binding policy return is implemented.
- Why this is / is not agent-owned: A prompt/guard or proposed model change is not automatically ultimate-policy authority, and permission checks do not constitute S5.
- Evidence: [guards](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/forge_modules/guards/guards.ts), [sandbox](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/forge/forge_modules/guards/sandbox.ts), [README](https://github.com/djtoon/pi-forge/blob/3af0d73a0f45701a4b1324d3b3bb272bc312ef2e/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: A human can rewrite the identity of a local generated harness, but this is not an established S5 governance channel.

### Absence scope

- Surfaces inspected: Spec model/guards, safety UI, confirmation, interview/update skills, generator and runtime reload.
- Plausible first-party paths checked: User interviews, model changes, guarded commands, credentials and self-update for ultimate-identity dispute → legitimate authority → binding return.
- Why no material first-party path remains: These are normal capability construction, settings and per-action enforcement rather than a function-specific S5 policy-adjudication closure.

## Distributed OSS parent arrangement

Independent installers can build, share and modify harnesses. Local browser builders and individual generated agents do not constitute a shared organization-level control plane. Public contributor practices and published templates do not establish a central decision-return authority over deployed local agents.

## Self-hosted and non-human modes

Agents run locally, with external model provider selection, web/terminal/headless/RPC delivery and optional packaged binaries. User-chosen sandbox and key settings delimit tool use; they do not replace model-owned S1 choices. The automatic builder/reload path is deliberately absent from packaged binaries, so S4 is attributed to supported source-checkout modes, not every exported distribution.

## Recursion

One generated agent can operate as a standalone task cell. When the Forge builder is installed alongside it, a higher capability-adaptation loop exists, but no evidence of complete viable metasystems for all generated agents or a parent coordinating distributed users follows.

## Variety and escalation

Interviews amplify requirements, spec validation and guards attenuate unsafe or invalid options, and the generator/smoke check returns errors for correction. A failed load prompts builder repair or operator intervention. The path is not an independent S3* audit or identity-policy resolution merely because it can stop deployment.

## Evidence gaps

Source-level static assessment at the frozen ref; no paid-model or web-server live E2E, generated-tool reliability, package portability or sandbox security guarantee was tested. Custom user-generated S2/S3/S3*/S5 behaviors are not attributed to pi-Forge without shipped evidence.
