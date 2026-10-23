---
harness_id: nanocoder
project_name: Nanocoder
repository: https://github.com/Nano-Collective/nanocoder
review_ref: 258a916ee5bff51564635100a71625b63fb99673
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Nanocoder

## Review boundary

- System in focus: the first-party Nanocoder terminal coding harness, its model-backed delegated subagents and its optional per-project event-triggered skill daemon at frozen commit `258a916ee5bff51564635100a71625b63fb99673`.
- Purpose and identity: let user-chosen models inspect and change a local project through bounded tools, optionally delegating specialized work or running subscribed skills when project events occur.
- Relevant environment: user instructions, repository files and conflicts, model/provider outputs, tool errors, filesystem/cron triggers, project skill definitions and operator approvals.
- Standard-distribution boundary: Node CLI/Ink chat or `run`, the main conversation/model tool execution loop, model-backed subagents with isolated contexts, tool filtering and permissions, optional daemon with registered skill subscriptions, cron/file watchers and IPC.
- Credited first-party operating surfaces: `source/hooks/chat-handler/conversation/`, `source/tools/agent-tool.tsx`, `source/subagents/`, `source/skills/{bootstrap,dispatcher,registrar}.ts`, `source/events/`, `source/daemon/`, the checked-in configuration and mode policy.
- Adjacent first-party surfaces excluded: AVA specs and fixtures, benchmarks, VS Code packaging, repository development and maintainer governance, example skill proposals, external MCP providers and any user-supplied reviewer or future-planning skill not actually wired by the default distribution.
- Reviewed modes: attended normal/auto-accept/yolo/plan/architect, non-interactive runs, concurrently delegated first-party subagents, optional daemon file/cron subscriptions and `confirm: true` plan-only runs.
- Recursion level: a local Nanocoder session and its delegated operating units, or a single project's daemon-triggered operating cohort. The daemon mode is explicitly narrower than all processes, independent repositories or the Nano Collective maintainer organization.
- License screen: `LICENSE.md` and `package.json` both declare MIT at the frozen ref. GitHub's API `NOASSERTION` metadata does not negate the checked-in license text.
- Observation date: 2026-10-23; Profile `0.2.4`; Methodology `0.3.7`.

## Repository architecture

The first-party chat loop exposes a tool manager to the current model, executes accepted tool calls, inserts tool results back into conversation history and repeats. The `agent` tool starts a separately model-backed `SubagentExecutor`, with its own prompt, tool set, message history and current task. A parent response may include up to five concurrent subagent calls. The subagent executor limits recursion to depth two and enforces the parent's effective development-mode tool permissions, including an inherited mutable mode resolver. The parent receives settled agent results, rather than a live model-facing global management channel.

An optional daemon boots first-party skill registries and attaches a file watcher and cron scheduler to an `EventRouter`, `BackpressureDispatcher` and `SkillDispatcher`. A matching skill subscription starts a headless model-backed agent, or a plan-only agent if the subscription requests confirmation. The backpressure wrapper imposes one running execution per **subscription ID**, drops additional events during that run and debounces bursts of file-change events for 500 ms. This is a real inter-run collision/overload stabilizer for repeat invocations of the *same* subscription, not global coordination across all concurrently delegated agents or different subscriptions. Event-triggered execution is optional, not the mandatory mode of a normal interactive session.

Tasks, plans, persisted transcripts, checkpoints, semantic memory, approvals and tool-call hooks can aid the work. The named verifier and optional custom reviewer are not evidence of a distinct independently owned audit circuit. Model-selected task plans address present work; subscriptions respond to present file/cron signals and do not themselves map future environmental options into evolved harness capability.

Frozen sources: [`conversation-loop.tsx`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/hooks/chat-handler/conversation/conversation-loop.tsx), [`tool-executor.tsx`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/hooks/chat-handler/conversation/tool-executor.tsx), [`subagent-executor.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/subagents/subagent-executor.ts), [`daemon.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/daemon/daemon.ts), [`backpressure.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/events/backpressure.ts), [`dispatcher.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/skills/dispatcher.ts), [`approval-policy.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/tools/approval-policy.ts).

## Operational model

The agent model owns its choices of tools and arguments in the main session and in genuinely separate delegated/triggered runs (S1). Runtime permission and event gates constrain the effects of those choices. For the daemon subscription cohort, *deterministic runtime code*, not an agent, owns the decision to suppress overlapping runs of the same subscribed skill (S2=C). No holistic present-work management decision, alternative independent audit, externally prospective adaptation or ultimate-policy closure is demonstrated at the declared distributed product boundary.

## S1 — Operations

- State: A
- Function: turn a natural-language or subscribed skill task into repository inspection, model-selected tool actions and a reported outcome.
- Disturbance / variety regulated: changing repository contents, unfamiliar files, tool failures, user objectives, provider responses and triggered skill inputs.
- Decisive decision or feedback right: the main agent or a delegated/triggered subagent selects next actions after model/tool feedback.
- Decision owner: the first-party model-backed main or subagent instance; the daemon's event matcher merely schedules the latter.
- Supporting / enforcement mechanisms: tool registry, context/message store, permission resolver, mode-specific tool filtering, prompt builder, configurable model providers and per-project daemon.
- Closure path: prompt or event → agent model/tool choice → tool execution and result → agent model's next choice or final outcome.
- Boundary reachability: the supported terminal/headless runner and `agent` tool construct the shipped executors; the optional daemon wires subscription dispatch into a real subagent executor.
- Why this is / is not agent-owned: the agent selects operations based on changing feedback, unlike the fixed event router or tool executor.
- Evidence: [`conversation-loop.tsx`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/hooks/chat-handler/conversation/conversation-loop.tsx), [`agent-tool.tsx`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/tools/agent-tool.tsx), [`subagent-executor.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/subagents/subagent-executor.ts).
- Basis: source-verified, with first-party fake-provider/script tests; no live LLM-agent performance run.
- Confidence: high for the shipped execution path, not measured task quality.
- Caveats: no default guarantee that a particular optional skill or subagent is configured, and subscribed runs require the daemon to be running.

## S2 — Coordination

- State: C
- Function: attenuate destructive overlap and event storms among separate model-backed runs of one daemon subscription.
- Disturbance / variety regulated: a burst of file changes or another cron/file event can start multiple concurrent project-mutating agents for the same skill before a previous run completes.
- Distinct S1 units: potential overlapping `SubagentExecutor` run instances from one registered `agent:`/`command:` subscription; each is a separately deciding model agent, not a mere tool call.
- Inter-S1 disturbance: duplicate concurrent executions of one skill could race over the same work surface and overload local resources.
- Attenuating coordination relation: the subscription ID identifies the shared project task cell; a deterministic in-flight exclusion gate prevents two such independently deciding cells from running at the same time, and the file watcher coalesces repeated changes.
- Feedback into subsequent S1 behaviour: permitted event delivery starts the model worker; suppressed concurrent events do not start competing workers, while subsequent eligible events can again launch one after the previous run exits.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the code enforces an exclusion precisely against duplicate concurrently mutating agent runs for the same subscription, not merely moving messages or assigning children; unlike a global mutex it is narrowly scoped to this inter-run disturbance.
- Coordination channel and decisive right: `BackpressureDispatcher` checks a subscription-specific in-flight set and deterministically drops a new event if a run with that ID is active; file changes are trailing-edge debounced.
- Decision owner: first-party deterministic runtime C, **not** the triggered agent or an autonomous S2 manager.
- Supporting / enforcement mechanisms: `EventRouter` registered subscription identity, `BackpressureDispatcher` in-flight set/debouncer and `SkillDispatcher` model-backed execution.
- Closure path: matching event → per-subscription gate → at most one in-flight model run for that subscription; excess events are dropped and later eligible events can execute.
- Boundary reachability: the `startDaemon` production path constructs the router → backpressure wrapper → skill dispatcher → model-backed executor and starts actual filesystem/cron event sources when the operator enables daemon mode.
- Boundary reachability: `startDaemon` wraps the actual skill dispatcher with `BackpressureDispatcher` before subscribing file watcher/cron sources; script test explicitly checks drop-while-in-flight.
- Why this is / is not agent-owned: protective inter-run scheduling is fixed source logic; the agents do not choose or negotiate interference responses.
- Evidence: [`daemon.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/daemon/daemon.ts), [`backpressure.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/events/backpressure.ts), [`backpressure.spec.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/events/backpressure.spec.ts).
- Basis: explicit code wiring and deterministic first-party script test.
- Confidence: medium-high for the bounded daemon overlap case, low for general multi-agent collaboration.
- Caveats: **not** a global project lock; different subscriptions or ordinary parallel `agent` calls may still edit the same files concurrently. Excess triggers are dropped, not durably queued or reconciled.

| Mode | S2 state | Disturbance and closure | Owner |
| --- | --- | --- | --- |
| Interactive delegated agents | — | Parallel children have a concurrency maximum of five, but no evidenced shared-file conflict detection or conflict-resolution feedback across them | None established |
| Optional per-project subscribed daemon | C | Same-subscription event races suppressed by the in-flight gate; file bursts debounced | Deterministic runtime |

## S3 — Inside-and-now control

- State: —
- Function: no demonstrated whole-current operational management with selectable priorities/resources and an intervention return across the assessed agent cohort.
- Disturbance / variety regulated: competing active commitments, slow/stuck workers or cross-subscription project resource conflicts could need higher-level decisions.
- Decisive decision or feedback right: the main model can delegate tasks and consume each worker's **final** result; a human can choose the overall mode or interrupt a turn; the daemon enforces a fixed per-subscription cap. No model/operator current-work portfolio decision with a sufficiently specific management return is demonstrated.
- Decision owner: none established for whole-cohort S3; model and human retain local task/delegation/permission rights.
- Supporting / enforcement mechanisms: parallel subagent progress map and UI, depth/fan-out limits, abort signal, mode resolver, task list, daemon per-subscription gate and event logging.
- Closure path: subagent final result → originating parent's ordinary next task decision, or top-level cancel; no current cohort inspection → selective commitment/resource intervention → workers' ongoing changed operations path was evidenced.
- Why this is / is not agent-owned: delegation, UI progress and bounded concurrency alone do not prove autonomous or parent-governed S3 resource management.
- Evidence: [`tool-executor.tsx`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/hooks/chat-handler/conversation/tool-executor.tsx), [`subagent-events.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/services/subagent-events.ts), [`subagent-executor.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/subagents/subagent-executor.ts).
- Basis: structural source inspection and bounded absence review.
- Confidence: medium.
- Caveats: external organizations could wrap Nanocoder with higher-level governance, which is not first-party S3 in this local product boundary.

### Absence scope

- Surfaces inspected: `agent` concurrency/fan-out, parent result aggregation, subagent progress UI/store, abort handling, skill daemon, task manager and approval settings.
- Plausible paths checked: progress display as a management roster, global cancellation as resource intervention, plan/task tools as manager, event backpressure as S3.
- Why no material first-party path remains: progress has no evidenced model-facing selective intervention operation; task delegation and fixed constraints do not themselves make whole-system operating-resource decisions.

## S3* — Complementary audit

- State: —
- Function: no independently accessed check of S1 operational claims with a finding fed to a responsible S3 controller was established.
- Disturbance / variety regulated: false claims of work completion and uncontrolled code changes may occur, but routine tool outputs or test execution are not separate audit ownership.
- Decisive decision or feedback right: the producer model can run tests or use hooks; a user may review actions, and custom reviewer agents may be authored, but no independent first-party complementary audit is mandated/wired with corrective closure.
- Decision owner: none established for an S3* audit function.
- Supporting / enforcement mechanisms: tool hooks, verification helpers, checkpoints, code diagnostics, subagent isolation, logs and first-party AVA tests.
- Closure path: ordinary tool and hook results → same acting agent or user approval; no complementary audit claim → S3 corrective return is wired.
- Why this is / is not agent-owned: optional user-defined reviewers and adjacent tests cannot be counted as first-party production audit merely because they can inspect code.
- Evidence: [`subagent-executor.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/subagents/subagent-executor.ts), [`approval-policy.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/tools/approval-policy.ts), [`subagents.md`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/docs/features/subagents.md).
- Basis: explicit design and bounded absence review.
- Confidence: medium-high.
- Caveats: a downstream team can construct a genuine independent review skill, but an available construction capability is not a demonstrated shipped audit circuit.

### Absence scope

- Surfaces inspected: built-in `explore` agent, custom agents/skills, pre/post-tool hooks, test and diff mechanisms, source AVA test suite.
- Plausible paths checked: a custom `code-reviewer` agent, verification command, git checkpoint, diagnostics, lifecycle hook audit logs and developer tests.
- Why no material first-party path remains: none is evidenced as a default independent auditor with direct complementary access whose judgment returns to first-party whole-current S3 control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed future-facing external-environment option development and return to harness capability was identified.
- Disturbance / variety regulated: changing model capabilities, users, ecosystem constraints and future task demands would require strategic adaptation, whereas file/cron events are present-state triggers.
- Decisive decision or feedback right: the working model may consult external tools, maintain memory or revise a task plan; a configured skill may react to file changes. None is demonstrated as first-party prospective adaptation governance.
- Decision owner: current S1 task agent for immediate choices and external human/maintainers for later product or skill redesign.
- Supporting / enforcement mechanisms: semantic memory, web/MCP tools, plan/architect modes, skill manifests, cron/file subscriptions and checkpoints.
- Closure path: current observations → local task response, or event → registered task run; no future environmental model → adaptation options → capability-update/control dialogue path is evidenced.
- Why this is / is not agent-owned: reactive subscriptions and a generic skill constructor do not themselves create S4; no default research-to-redesign loop is shipped.
- Evidence: [`skills.md`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/docs/features/skills.md), [`dispatcher.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/skills/dispatcher.ts), [`daemon.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/daemon/daemon.ts).
- Basis: bounded first-party path review.
- Confidence: medium.
- Caveats: external users could implement a prospective watcher, but that is a *configured use case*, not credited as default harness S4.

### Absence scope

- Surfaces inspected: model/tool loop, project memory, plan/architect modes, events/daemon, skill creation and bundled subscriptions.
- Plausible paths checked: memory as learning, cron watcher as external horizon scan, custom skills as organizational evolution, internal architect planning.
- Why no material first-party path remains: none shows a shipped feedback loop that forms future-relevant options from external distinctions and changes subsequent harness capability through a management dialogue.

## S5 — Policy and identity

- State: —
- Function: no in-boundary ultimate-identity/policy decision and authoritative closure is evidenced.
- Disturbance / variety regulated: risky command execution and permitted tools are constrained locally; higher-level conflicts over organizational ethos or future-versus-present policy remain external.
- Decisive decision or feedback right: the user selects modes, preauthorizes tools or answers operational prompts; skill authors configure permissions. This is not an identity-level adjudication with S3–S4 return.
- Decision owner: no first-party legitimate S5 actor or closed parent arrangement established within the operating product.
- Supporting / enforcement mechanisms: `resolveToolApproval`, `alwaysAllow`, mode-sensitive tool availability, blocked subagent tools and headless/plan constraints.
- Closure path: per-tool approval/mode configuration governs individual operations; no policy-identity proposal → legitimate ultimate authority → system-wide decision return path is evidenced.
- Why this is / is not agent-owned: static developer rules and granular user consent are action permission, not VSM S5 decision rights.
- Evidence: [`approval-policy.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/tools/approval-policy.ts), [`development-modes.md`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/docs/features/development-modes.md), [`subagent-executor.ts`](https://github.com/Nano-Collective/nanocoder/blob/258a916ee5bff51564635100a71625b63fb99673/source/subagents/subagent-executor.ts).
- Basis: explicit first-party permission mechanisms and bounded absence review.
- Confidence: medium-high.
- Caveats: a separately governed organization can set an identity for deployments; this assessment does not equate the product's maintainers with a live S5 parent.

### Absence scope

- Surfaces inspected: modes, approvals, per-tool custom policies, scoped tool visibility, skill permissions, headless and daemon safety gates.
- Plausible paths checked: user approval as S5, system prompt as identity mandate, maintainers as governance, `architect` review as an ultimate policy decision.
- Why no material first-party path remains: these decisions affect tactical actions and work products, not a recognized identity/ultimate-policy question returned as a durable operating constraint.

## Distributed OSS parent arrangement

Nano Collective maintainers may govern upstream software evolution, but their GitHub discussions or releases are not connected to any assessed local Nanocoder run as a first-party ultimate-policy or prospective-adaptation loop. Individual user-authored skill bundles can change operational behaviour; they remain downstream configuration until a concrete bounded mode and closure are evidenced.

## Self-hosted and non-human modes

Both interactive and headless Nanocoder can enact S1 through the model/tool loop. `startDaemon` adds the bounded S2=C subscription-overlap guard when enabled. The `confirm: true` branch executes a plan-only inspection instead of modifying files; default triggered work is headless. These alternatives cannot be pooled to fabricate a universal S3, S4 or S5 controller.

## Recursion

Each separately model-backed delegated agent/triggered skill run is an S1 at the selected work-session recursion. S2=C is at the shared daemon subscription-run cohort. The broader repository, its maintainer community, external model providers and independent Nanocoder installations are not part of that one operating-control recursion.

## Variety and escalation

Operating errors return to the producing S1. A subscription collision is damped by skip/debounce rather than solved semantically; the human or a later run must settle competing work intent. Tool mode restrictions follow delegated execution. No autonomous whole-cohort intervention, independent audit, or strategic capability adaptation can be inferred from this operational plumbing.

## Evidence gaps

- No live LLM-agent runs and no measured task-success or collision-effectiveness outcomes, per the deterministic-script-only batch rule.
- The concurrency cap covers one subscription ID, not different skills or concurrent interactive children; dropping an event can lose an intended task.
- A custom skill could implement more sophisticated collaboration, audit or foresight, but no concrete first-party closed path is demonstrated at this frozen ref.
- First-party source tests and typecheck are corroborative, not an LLM effectiveness experiment.
