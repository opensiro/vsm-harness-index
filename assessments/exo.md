---
harness_id: exo
project_name: Exo
repository: https://github.com/exoharness/exo
review_ref: 6164288895a5851b2118492c880fb37b543e2ac6
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: A(P)
---

# Exo

## Review boundary

- System in focus: one first-party Exo long-running self-hosted agent installation at the frozen candidate revision, including its model/tool turn loop, durable exoharness state, canonical event history, sandbox, scheduler/adapters, standard self-code mount, capability-extension tools, self-update guardian path, and supported operator service controls.
- Purpose and identity: operate a local machine over time as a long-running research/operations agent, while retaining durable state and first-party means to inspect, extend, validate, rebuild, restart and revise its own harness behavior.
- Relevant environment: users and external adapter messages, local-machine and sandbox state, repositories/files, web/services and installed tools, scheduled events, model-provider responses, host service health, and changing capability demands encountered over time.
- Standard-distribution boundary: the canonical Exo setup at the pinned revision: first-party `exo` harness plus shipped exoharness runtime, default agent sandbox/repository mount, durable `.exo` state, scheduler/adapter runners, guardian self-update path, CLI/ExoChat/adapters and documented operator service controls. External model providers, messaging services, downstream extensions, examples and future roadmap components are outside credited ownership.
- Credited operating / distribution surfaces: `exo/harness.ts`, `exoharness/typescript/model-runtime/turn-loop.ts`, built-in/installed tool machinery, `exo/prompts/me.md`, `exo/SELF.md`, `exo/tools/guardian-tools.ts`, `exo/tools/introspection-tools.ts`, scheduler/adapter tools and runners, canonical event/state APIs, sandbox snapshot/rewind paths, and `exo/scripts/exo-service-guardian` / standard `./exo.sh` operating controls.
- Adjacent first-party surfaces excluded from ownership: CI/release workflows, repository contributor governance, tests, website presentation, tutorial/example harnesses including Gameboy Agent/ExoWorker, and roadmap-only cloning/high-level multi-agent work. Documentation is used to interpret shipped paths but does not itself supply an organizational owner.
- First-party operating / deployment modes considered: canonical single-Agent local setup; scheduled and adapter-triggered long-running operation; model-driven installation of reusable tools/skills and self-code edits activated through the fixed guardian path; sandbox snapshot/rewind recovery; and the documented self-hosted operator mode for host-service status/restart plus direct prompt/code changes.
- Recursion level: the whole local Exo installation is the system-in-focus. Conversations, scheduled tasks, adapters, sandboxes and future clone/lineage ideas are not promoted to recursively viable lower systems without separate evidence.
- Reviewed revision: `6164288895a5851b2118492c880fb37b543e2ac6`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

The frozen batch #89 review ref is authoritative for this assessment. Exo's later `main` state is not borrowed to upgrade the pinned system.

## Repository architecture

Exo owns its primary agent loop. `exo/harness.ts` supplies the Exo prompt and first-party tool registry to `runResponsesHarnessTurn`; the model-runtime loop repeatedly materializes context, calls the configured model, appends returned events, executes requested tools and appends their results, then calls the model again until no further tool call remains or the configured round bound is reached. The canonical setup therefore has an autonomous model→tool→observation→next-decision operational loop rather than delegating agency to an external coding assistant.

Durable exoharness state sits outside the resettable sandbox. Conversation history, tool activity, artifacts and lifecycle events survive ordinary service restarts and sandbox rewinds. `list_conversation_events` and adapter telemetry expose that history to the Agent. The canonical source tree is simultaneously mounted into the Agent's sandbox at `/workspace/exo`; `exo/SELF.md` maps the important self-maintenance surfaces. Registry-backed tools can be created/installed and become callable on a later model round; deeper source edits can be made against the mounted repository and activated through the narrow first-party `rebuild_and_restart_exo` tool, which validates/builds the system, durably records the requested update, and hands restart of scheduler/adapters to the host guardian after the active turn finishes.

This self-change path is deliberately broader than ordinary memory or skills. Maintainer material identifies `exo/prompts/me.md` as the durable identity and operating-rules prompt, `exo/harness.ts` as harness-policy assembly, and source/tool definitions as changeable behavior. The shipped model is instructed to inspect `SELF.md`, edit its own mounted source when appropriate, and invoke the guardian activation path afterward. The same distribution supports a parent/operator mode: a human can directly edit prompts/code and uses `exo-service-guardian` / `./exo.sh` to inspect and regulate host services, build/restart the installation, and preserve or reset state.

No complete high-level multi-agent organization is credited. The frozen README explicitly puts policies for when to clone, divide work, collect child results, resolve conflicting conclusions and stop a lineage under ongoing work. The more implementation-specific `docs/SELF-CONTROL.md` says whole-agent cloning/migration is not yet built. Conversation forks and sandbox snapshots therefore remain technical primitives, not evidence of sibling S1 units plus S2 regulation or VSM recursion.

Primary evidence:

- [`README.md`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/README.md)
- [`docs/RSI.md`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/docs/RSI.md)
- [`docs/SELF-CONTROL.md`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/docs/SELF-CONTROL.md)
- [`exo/harness.ts`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/exo/harness.ts)
- [`exoharness/typescript/model-runtime/turn-loop.ts`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/exoharness/typescript/model-runtime/turn-loop.ts)
- [`exo/prompts/me.md`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/exo/prompts/me.md)
- [`exo/SELF.md`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/exo/SELF.md)
- [`exo/tools/guardian-tools.ts`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/exo/tools/guardian-tools.ts)
- [`exo/tools/introspection-tools.ts`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/exo/tools/introspection-tools.ts)
- [`exo/tools/scheduler-tools.ts`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/exo/tools/scheduler-tools.ts)
- [`exo/scripts/exo-service-guardian`](https://github.com/exoharness/exo/blob/6164288895a5851b2118492c880fb37b543e2ac6/exo/scripts/exo-service-guardian)

## Operational model

The primary S1 is the long-running Exo Agent. User messages, external-adapter wakeups and scheduler wakeups enter its first-party turn loop. The model selects tool actions, receives their returned observations, can alter environment state, schedule durable future work, create capabilities, communicate externally, or complete the turn. The canonical state/event layer persists what happened across restarts and sandbox recovery.

For metasystem ownership, Exo exposes two materially different control topologies. Current host-service control remains parent-owned: the standard Agent can diagnose some adapters/tasks and request the fixed self-update restart, but service-wide status/logs and direct scheduler/adapter service controls are explicitly reserved to the operator guardian CLI. By contrast, the standard Agent itself owns substantial prospective adaptation and identity-policy self-change discretion because source code, tool creation, identity prompt and the build/restart closure are intentionally placed inside its normal first-party reach. The operator retains separate supported parent modes for adaptation and identity through direct edits plus the same activation infrastructure.

## S1 — Operations

- State: A
- Function: autonomously perform open-ended research/operations work on the local-machine/external environment through repeated model decisions and first-party tools.
- Disturbance / variety regulated: heterogeneous user or adapter objectives, changing sandbox/filesystem state, web/service responses, command/tool outcomes and failures, scheduled wakeups, and newly observed information during a turn.
- Decisive decision or feedback right: choose each next tool/action or final response from the current prompt and returned observations.
- Decision owner: the running Exo model actor inside the first-party responses turn loop.
- Supporting / enforcement mechanisms: exoharness durable context/events, prompt assembly, tool registry/execution, sandbox, scheduler/adapters, provider runtime and configured round limits.
- Closure path: model decision → first-party tool execution or external action → result/event appended to canonical context → next model round incorporates the observation and revises action until completion.
- Boundary reachability: `exo/harness.ts` directly invokes the shipped `runResponsesHarnessTurn` in the canonical harness; no adjacent development agent or downstream orchestration is required.
- Why this is / is not agent-owned: deterministic runtime code supplies context, transport and execution, but the model actor selects discretionary next actions in response to changing observations.
- Evidence: pinned `exo/harness.ts` and `exoharness/typescript/model-runtime/turn-loop.ts`; README corroborates the canonical long-running Agent operating boundary.
- Basis: `structural` and `explicit`.
- Confidence: high.
- Caveats: available tools, configured limits and provider behavior constrain operational variety without replacing the Agent's next-action discretion.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation among distinct sibling S1 units is established in the frozen standard distribution.
- Disturbance / variety regulated: no qualifying inter-S1 interference/conflict/oscillation with an implemented attenuation loop was found.
- Decisive decision or feedback right: no S2-specific coordination discretion is supplied at the declared recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: conversation/event ordering, scheduler timing, adapter supervision, sandbox scoping, conversation forks and lineage-related state primitives.
- Closure path: no qualifying coordination-result→subsequent-sibling-S1 feedback loop is implemented at the assessed boundary.
- Why this is / is not agent-owned: the frozen implementation establishes one primary long-running Agent plus tasks/adapters/conversations, not an implemented sibling multi-Agent organization with a concrete interference-control relation.
- Evidence: pinned `README.md`, especially its ongoing-work statement for high-level multi-agent orchestration, and `docs/SELF-CONTROL.md`, which marks whole-agent cloning/migration as not yet built.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: README language about recursive improvement/lineage describes architectural direction and primitives; it is not sufficient to manufacture an S2 function that implementation-specific material says is unfinished.

### Absence scope

- Surfaces inspected: core turn loop, agents/conversations, scheduler and adapters, sandbox snapshot/rewind, event/state layer, README architecture/ongoing-work material, RSI material, and the implementation-status Self-Control document.
- Plausible first-party paths checked: scheduled tasks as possible sibling operations, adapter workers, conversation forks, sandbox snapshots, cloning/lineage claims and future high-level multi-agent orchestration.
- Why no material first-party path remains: tasks/adapters/forks are execution or transport/state primitives rather than independently evidenced sibling S1 units with a specific regulated mutual disturbance; the repository explicitly states the missing orchestration policies and that complete cloning/migration is not yet implemented.

## S3 — Inside-and-now control

- State: P
- Function: regulate the currently running Exo installation's host-side service capacity and lifecycle on behalf of the whole.
- Disturbance / variety regulated: scheduler/adapter process failure or stale state, need to stop/restart current host services, fresh-build activation, and mismatch between current process state and desired installation-wide service state.
- Decisive decision or feedback right: inspect current guardian-managed service status/logs and choose start/stop/restart/rebuild actions for scheduler and adapter runners, including the control REPL refresh path.
- Decision owner: the self-hosted human operator in the supported guardian/`./exo.sh` parent mode.
- Supporting / enforcement mechanisms: PID/state files, graceful drain markers, process supervision, build scripts, reboot notices and preserved `.exo` state.
- Closure path: operator observes the whole guardian-managed current service state → invokes the chosen guardian control → deterministic supervisor drains/stops/starts/rebuilds affected services → later current operation continues under the selected service state.
- Boundary reachability: `exo/scripts/exo-service-guardian` and `./exo.sh` are documented standard day-to-day operating surfaces in the canonical self-hosted distribution; they are not contributor-only development utilities.
- Why this is / is not agent-owned: the Agent receives read-only/introspection and a narrow self-update handoff, but maintainer instructions explicitly keep service status, host logs and targeted service controls as operator CLI responsibilities. Thus the whole-installation current-control decision is parent-owned.
- Evidence: pinned `exo/scripts/exo-service-guardian`, `exo/SELF.md`, `exo/harness.ts`, `docs/SELF-CONTROL.md` and README operating instructions.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: conversation-local task/adapter management and the fixed `rebuild_and_restart_exo` activation tool are not separately credited as autonomous S3 because they do not establish an autonomous whole-installation current-control view/right.
- Whole-system current view: guardian `status` reports scheduler and adapter runner status plus pending REPL restart state; standard operating material identifies it as the host-service control surface for the installation.
- Current-control decision scope: build and start/stop/restart of the scheduler and adapter service capacity, including current service recovery while preserving durable state.

## S3* — Complementary audit

- State: —
- Function: no complete first-party complementary-audit function with sufficiently independent operational access and audit judgment is established.
- Disturbance / variety regulated: no S3*-specific claim/risk is closed by an independent audit relation at the declared boundary.
- Decisive decision or feedback right: no independent audit judgment/feedback right is supplied.
- Decision owner: not established.
- Supporting / enforcement mechanisms: append-only canonical event history, `list_conversation_events`, adapter telemetry, git history, guardian outcome records and host logs.
- Closure path: these records can support diagnosis and reconstruction, but no distinct auditor observes operational reality through a sufficiently independent path, forms findings and returns those findings through a credited current-control loop.
- Why this is / is not agent-owned: Exo gives the same Agent unusually durable visibility into what happened to it, including evidence surviving sandbox rewind, but protected observability/history is not by itself complementary audit under the Profile.
- Evidence: pinned `docs/RSI.md`, `docs/SELF-CONTROL.md`, `exo/SELF.md` and `exo/tools/introspection-tools.ts`.
- Basis: `structural`.
- Confidence: high.
- Caveats: the immutable event log is stronger evidence than ordinary ephemeral tracing and is useful audit substrate; the negative mapping is about the missing independent audit function/judgment/closure, not a claim that Exo lacks traceability.

### Absence scope

- Surfaces inspected: immutable canonical event log, conversation and adapter introspection, git history, sandbox snapshot/rewind records, self-update outcomes, service logs, self-verification/rollback guidance and normal tool execution events.
- Plausible first-party paths checked: using immutable history as an auditor, adapter telemetry as alternate truth, git/change history, post-rebuild outcome records and self-verification checks.
- Why no material first-party path remains: all discovered paths are observability, provenance, ordinary verification or operational history available to the same production/self-maintenance organization; no separate sufficiently independent access-and-judgment relation is implemented to challenge routine operational claims and feed findings into S3.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: turn changing external capability demands and observed operational limitations into reusable future capability changes to the running Exo harness.
- Disturbance / variety regulated: new user/environment requirements, missing tools/integrations, recurring work that deserves durable capability, failures or limitations exposed by real operation, and future-fit concerns in prompts/tooling/harness behavior.
- Decisive decision or feedback right: base mode — the Exo Agent decides what reusable tool, skill, prompt or source-level harness adaptation to implement and whether/how to validate and activate it; parent mode — the operator decides the adaptation and directly edits/configures the corresponding first-party capability before rebuilding/restarting it.
- Decision owner: base (`A`) — the long-running Exo model actor using its intentionally exposed self-maintenance/capability-extension surfaces; parent (`P`) — the self-hosted human operator through direct source/prompt/configuration edits and standard activation controls.
- Supporting / enforcement mechanisms: source mount and self-map, `shell`, `manage_tool`, skills, sandbox snapshots/rewind, git history, tests/build commands, `rebuild_and_restart_exo`, durable update events and guardian service activation.
- Closure path: base — externally observed need/limitation → Agent develops a reusable adaptation → writes/installs it → validates and, for source changes, invokes the guardian build/restart → later turns operate with the changed capability. Parent — operator forms the adaptation judgment → edits the same capability surface → rebuild/restart or normal reload → subsequent Agent operation uses the changed capability.
- Boundary reachability: self-source visibility, managed-tool creation and the fixed guardian self-update path are deliberately wired into the canonical standard Agent prompt/toolset; the parent edit/guardian path is also a supported day-to-day self-hosted mode.
- Why this is / is not agent-owned: code mounting, git and guardian are supporting machinery; in base mode the model actor can itself interpret an externally revealed capability gap, choose the future reusable change and activate it without requiring a developer to compose an additional adaptation actor or closure loop.
- Evidence: pinned README, `docs/RSI.md`, `docs/SELF-CONTROL.md`, `exo/harness.ts`, `exo/SELF.md`, `exo/tools/guardian-tools.ts` and managed-tool paths documented at the frozen ref.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: generic source-code mutability alone would not be S4. The credited witness is the standard long-running Agent's externally coupled path from encountered capability demand/limitation to a reusable tool/prompt/harness adaptation that is returned into later capability. Roadmap-only autonomous periodic cleanup is not used as evidence.
- External distinction: a user/environment exposes a capability need, failed/insufficient current behavior, integration requirement or recurring operational pattern that the existing harness does not adequately absorb.
- Future / prospective distinction: the Agent distinguishes a one-off task from a reusable capability change intended to alter later turns—installed tools are explicitly re-registered on following model rounds, skills persist across conversations, and source/prompt updates are activated for future operation.
- Adaptation option generated: create/replace a managed tool; install a durable reusable skill; change prompts/tool schemas/harness source; add an adapter/integration; or modify broader Exo code and validate/restart it.
- Path back into current capability / S3: managed-tool changes become callable on a later model round; skills/prompt changes enter later context; source edits become running code after the first-party validation/build/restart guardian path. Parent guardian control supplies the current-service activation edge without owning the base Agent's adaptation judgment.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Exo model actor | externally observed future-relevant capability need/limitation | Agent creates/edits reusable capability → installs or validates/builds/restarts it → later turns use changed capability | `exo/harness.ts`, `exo/SELF.md`, `docs/SELF-CONTROL.md`, `guardian-tools.ts`, managed-tool path |
| Parent (`P`) | self-hosted operator | operator judges that future capability should change | direct prompt/code/config edit → standard reload/build/restart → later Agent operation uses the change | README prompt-edit guidance, `SELF-CONTROL.md`, `exo-service-guardian` |

## S5 — Policy and identity

- State: A(P)
- Function: govern the durable identity, purpose and highest-level operating policy of the Exo Agent through the first-party prompt/harness surfaces that define subsequent behavior.
- Disturbance / variety regulated: tension between the Agent's current durable identity/operating principles and a proposed new purpose, ethos or ultimate behavior policy, whether the proposal arises from the Agent's own self-evolution judgment or from its parent operator.
- Decisive decision or feedback right: base mode — decide to revise durable identity/operating-rule surfaces such as `exo/prompts/me.md` or equivalent harness-policy assembly and activate that revision; parent mode — authoritatively choose and edit those same identity/policy surfaces for the local installation.
- Decision owner: base (`A`) — the Exo model actor, which is intentionally granted the standard-distribution self-source write/activation path over its identity/harness policy; parent (`P`) — the self-hosted user/operator, who can directly define/edit the durable identity/prompt policy and activate or override it.
- Supporting / enforcement mechanisms: mounted source repository, `shell`, `exo/SELF.md`, git history/revert, prompt assembly in `exo/harness.ts`, the fixed guardian build/restart operation and operator service controls.
- Closure path: base — identity/ultimate-policy issue is judged by the Agent → Agent edits the durable identity/policy source → validates/commits as appropriate and invokes the first-party rebuild/restart path → subsequent turns receive the changed authoritative prompt/policy. Parent — operator makes the identity/policy decision → direct first-party-supported prompt/source edit and activation → subsequent Agent turns are governed by it.
- Boundary reachability: the canonical prompt tells Exo that its own source tree is mounted and that it should inspect/modify itself through `SELF.md` plus `rebuild_and_restart_exo`; `docs/SELF-CONTROL.md` identifies prompt evolution as an existing self-control capability, and README separately documents direct human prompt editing.
- Why this is / is not agent-owned: the positive base claim is not inferred from the existence of a static system prompt. The standard Agent is the actor that can inspect and alter the durable identity/operating-policy artifact and close the change into its own later runtime; no additional developer-composed S5 actor is required. The supported human path remains a distinct parent-authority mode and can override the autonomous configuration.
- Evidence: pinned `exo/prompts/me.md`, `exo/harness.ts`, `exo/SELF.md`, `docs/RSI.md`, `docs/SELF-CONTROL.md`, README and `exo/tools/guardian-tools.ts`.
- Basis: `explicit` and `structural`.
- Confidence: medium-high.
- Caveats: normal task instructions, adapter side-effect rules and tool permissions are not individually promoted to S5. `A(P)` is limited to the documented durable identity/basic-harness-policy self-modification path plus the distinct operator-owned path; it does not imply that every runtime constraint is autonomously mutable.
- Identity / ultimate-policy issue: `exo/prompts/me.md` explicitly states what the Agent is, its purpose and broad operating rules; maintainer material calls it the durable identity prompt and states that prompt/basic-harness policy can evolve through the self-modification path.
- Ultimate authority in each claimed mode: base (`A`) — the standard Exo Agent can itself select and activate a change to its durable identity/basic harness policy without a separate approval mechanism in that mode; parent (`P`) — the local operator can authoritatively set/override those surfaces and activate the resulting build/configuration.
- Return-to-operation path: identity/policy source enters `exoInstructions` on later turns; source-level changes are activated through `rebuild_and_restart_exo` or the operator guardian path, after which subsequent operation loads the changed policy.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Exo model actor | an identity/ultimate-policy issue that the Agent decides warrants durable self-change | self-source identity/policy edit → validation/build/restart → changed policy governs later turns | `me.md`, `harness.ts`, `SELF.md`, `SELF-CONTROL.md`, `guardian-tools.ts` |
| Parent (`P`) | self-hosted operator | operator decides the Agent's durable identity/purpose/ultimate operating policy should change | direct prompt/source edit → standard activation → later turns load the parent decision | README prompt-edit path, `SELF-CONTROL.md`, guardian controls |

## Recursion

Exo uses the word "recursive" for recursive self-improvement, but that is not automatically VSM recursion. At the frozen revision, the implementation-status documentation says full cloning/migration is not yet built and the README describes high-level multi-agent orchestration policy as ongoing work. Conversation forks, scheduled tasks and sandbox snapshots do not independently establish lower units with their own relevant environments and complete metasystems. No positive VSM-recursion claim is therefore made.

## Variety and escalation

The primary Agent amplifies regulatory variety with shell/web access, installable tools and skills, adapters, scheduled work, persistent memory/state and the ability to alter its own harness. Sandbox snapshots, git history and durable events make risky experimentation recoverable. External side effects remain explicit tool decisions. Self-code activation is handed to a narrow host guardian so the active turn can finish and services can drain/restart safely. When self-visible telemetry is insufficient for a host-service problem, standard instructions escalate to the human operator, who has the guardian-wide status/log/current-control surface.

## Evidence gaps

- S3 autonomous ownership is not claimed: the Agent can manage some conversation-scoped tasks/adapters and request its self-update restart, but the frozen documentation explicitly reserves whole-host status/logs and targeted service controls for the operator.
- The immutable event stream is a strong provenance/recovery substrate but does not supply a complete independent S3* auditor at this boundary.
- S4 `A` depends on function, not the project's "recursive self improvement" label: the assessment credits only standard, executable paths that turn external capability demands into durable later capability.
- S5 `A` is the most ownership-sensitive positive mapping. It relies on the standard Agent being intentionally granted writable, activatable access to its durable identity/basic-harness-policy surfaces. If a later revision adds mandatory parent approval for those identity-level changes, ownership must be reassessed rather than carried forward.
- Roadmap-only cloning, migration, canary comparison and high-level lineage coordination are explicitly excluded from current-state positive mappings.
