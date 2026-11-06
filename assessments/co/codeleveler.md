---
harness_id: codeleveler
project_name: CodeLeveler
repository: https://github.com/dengmengmian/CodeLeveler
review_ref: b08f9013e1bd62801ef0eca60169f566f7fb6b5d
reviewed_at: 2026-11-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# CodeLeveler

## Review boundary

- System in focus: the shipped local-first CodeLeveler coding-agent product at the frozen revision: the `leveler` CLI/TUI/Web/headless task entry, Coding Harness, model/tool execution loop, first-party delegated agents, exclusive write ownership, `/develop` review loop, host authorization and durable session state.
- Purpose and identity: carry out user-specified coding work inside a local repository, producing inspectable changes and execution evidence while retaining session and permission boundaries.
- Relevant environment: user goals, local source trees and Git worktrees, build/test command results, overlapping child edits, model/provider responses, OS isolation/permissions, session interruptions and external software releases.
- Standard-distribution boundary: installed `leveler`, its first-party runtime, supported optional `--collaboration goal`, `--parallel N` and explicitly invoked `/develop` modes. These are alternative supported product modes, not simultaneous compulsory phases. Provider intelligence and the host OS are dependencies, not first-party VSM decision owners.
- Credited operating / distribution surfaces: `README.md`, `docs/ARCHITECTURE.md`, `crates/leveler-cli/src/{cli,run_cmds}.rs`, `crates/leveler-app/src/parallel.rs`, `crates/leveler-agent/src/{coding,sub_agent,injected_tools,ownership,child_profile}.rs`, `crates/leveler-agent/src/{coding/{develop,run,turn,policy},executor/{drive,handlers},update_plan}.rs`, `crates/leveler-vcs/src/parallel.rs` and first-party TUI/Web/runtime composition.
- Adjacent first-party surfaces excluded from ownership: `crates/leveler-cli/src/eval_cmd.rs`, `crates/leveler-eval/`, repository CI and release checks, development/dogfood agents, tests, proposed separate Review/Research products, experimental mobile preview and deployment/relay research. Tests corroborate code wiring but are not promoted to runtime auditors or managers. Project maintainers, third-party providers, user-authored agents/skills/prompts and external toolchain decisions cannot donate S-functions to the product.
- First-party operating / deployment modes considered: `leveler`, `leveler tui`, `leveler web`, `leveler run`, goal continuation, model-spawned default/explorer/scoped-worker children, `leveler run --parallel N` isolated candidate worktrees, user-initiated `/develop`, optional caller-requested required closure review, and operator-configured permission/isolation modes.
- Recursion level: one user coding goal and its live first-party autonomous work cells. A child can have its own model/tool loop and local workspace scope, but nesting alone does not prove a second complete viable-system recursion.
- Reviewed revision: `b08f9013e1bd62801ef0eca60169f566f7fb6b5d`; observation date 2026-11-07; Profile `0.2.4` / Index-active Methodology `0.3.7`.

## Repository architecture

The shipped CLI/TUI/Web/headless products share an agent runtime. A configured provider supplies model decisions; the Coding Harness builds a request context and tool surface; the executor runs model-selected repository-read/edit/shell/Git actions through host authority, feeds results back, tracks budgets and progress, and persists session, events and child attribution for resume. The host may decline an effect even when the model requests it. An explicit `update_goal` conclusion controls goal termination; deterministic closeout, cancellation and budget rules are not substituted for the model's task judgment.

In multi-agent mode the parent model can spawn self-contained child loops. Children with write capability claim specific paths, and the shared `OwnershipRegistry` refuses overlapping concurrent ownership atomically, including parent mutations in flight. A failed claim returns the collision and owner to the child as a model-readable coordination outcome. A separate `--parallel N` mode instead runs candidates in isolated Git worktrees and merges non-conflicting verified branches; its first-wins conflict handling is deterministic and must not be credited as a distinct autonomous coordination decision without additional evidence.

An expressly invoked `/develop` mode runs read-only Analyze, ordinary model-driven Coding, then a harness-launched read-only Review child. Review receives the original goal, implementer's report, actual diff and changed files, reads code itself, and independently chooses PASS, REWORK or REANALYZE. The resulting verdict controls another Coding/Analyze pass or the terminal outcome. A separate optional closure reviewer is **off by default** and reports warnings; it should not be mistaken for this corrective `/develop` return path. External provider models, user-installed definitions, maintainer CI and benchmark evaluators are not owners of these product loops.

Primary frozen-source paths:

- [Product, supported modes, permissions and updater](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/README.md)
- [Runtime/host-authority architecture and task flow](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/docs/ARCHITECTURE.md)
- [Parent/child prompt and settlement contract](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/sub_agent.rs)
- [Agent-spawn and write-scope model-facing controls](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/injected_tools.rs)
- [Atomic ownership collision/feedback and mutation fence](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/ownership.rs)
- [Develop reviewer brief, verdict and bounded send-back](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/coding/develop.rs)
- [Reachable Develop pipeline and optional closure-review distinction](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/coding/run.rs)
- [Read-only, bounded harness reviewer capability](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/child_profile.rs)
- [Parallel worktree candidates](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-app/src/parallel.rs) and [Git merge conflict disposition](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-vcs/src/parallel.rs)

## Operational model

The user provides a coding objective. The parent agent reasons over repository state, chooses actions and may delegate narrower source/edit work; host authority enforces permissions, while the durable runtime records actual effects. Each child is an operational model/tool loop with a distinct task and limited effect rights. At the shared workspace boundary, write ownership regulates concurrent interference and returns collision information to the affected agent. In `/develop`, a separate read-only reviewer examines the produced artifact and makes a corrective judgment that the harness returns to the implementing loop.

## S1 — Operations

- State: A
- Function: implement user-directed software changes and investigation steps by selecting and revising tools against live repository outcomes.
- Disturbance / variety regulated: unknown code structure, changing requirements, tool errors, failing commands, model uncertainty and partial implementation.
- Decisive decision or feedback right: the model chooses coding actions, tool arguments, follow-up investigation and whether the task goal was met; optional delegated model children own their local task decisions within capability grants.
- Decision owner: configured parent and, where spawned, child agent model loops; runtime owns mechanical lifecycle, not the semantic task decision.
- Supporting / enforcement mechanisms: Coding Harness and `AgentKernel`, repository/shell/Git capabilities, host-side permission sandbox, durable event/request ledger, tool results, budgets, cancellation and session resume.
- Closure path: goal → model investigation/plan → model-selected tool call → host-authorized effect → observed file/process result → next model choice or explicit goal resolution.
- Boundary reachability: CLI/TUI/Web and `leveler run` share the compiled task runner; the documented shipped coding mode and child-spawn tool are exposed to configured model-backed sessions.
- Why this is / is not agent-owned: without the model's discretionary choice, runtime/host authority can enforce or record effects but cannot select goal-specific code edits or decide task-level semantic completion.
- Evidence: [README](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/README.md), [architecture §§4–6, 14](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/docs/ARCHITECTURE.md), [coding task runner](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/coding/run.rs), [executor drive](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/executor/drive.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no provider-backed end-to-end coding run was executed for this review; shipped code establishes the reachable agent loop, not success on a benchmark.

## S2 — Coordination

- State: A
- Function: attenuate destructive inter-S1 file-write collisions among concurrently active child coding agents and the parent in the same workspace.
- Disturbance / variety regulated: two independent operational model/tool loops can attempt to edit the same path while operating concurrently; an in-flight parent mutation can race a child's late claim.
- Distinct S1 units: separate concurrently executing child model/tool work cells (and parent S1 work) with independently selected tool actions and write scopes.
- Inter-S1 disturbance: overlapping exclusive file/directory claims and parent/child simultaneous edits would otherwise produce conflicting mutations or rollback attribution.
- Attenuating coordination relation: child-chosen `claim_write_scope` requests pass through one atomic `OwnershipRegistry`; overlapping claims are denied with the current owner, and host write fences reject edits outside an accepted scope.
- Feedback into subsequent S1 behaviour: the rejected scope and owner are returned to the child model with specific alternatives (narrow scope, another subtask, or wait); the child can select a different coordination response in its next model/tool step. Successful claims permit only its bounded mutations, and settlement releases them.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the tool and collision predicate target the specific disturbance of competing concurrently active writes, not mere task handoff or a generic queue. Atomic exclusion and model-readable rejection form an anti-interference return.
- Decisive decision or feedback right: each agent selects or revises the requested work scope after learning collisions; the runtime decides only whether that proposed scope is currently enforceable.
- Decision owner: autonomous child/parent agent for discretionary work-scope choice and subsequent response; deterministic `OwnershipRegistry` for non-discretionary exclusivity enforcement.
- Supporting / enforcement mechanisms: path normalization, atomic claims, live-parent mutation guard, per-child allowlists, host fence, model-facing owner-aware denial, and release at child settlement.
- Closure path: overlapping proposed edits → atomic conflict result → agent receives path/owner feedback → agent chooses narrower/different/later work → grant/fence changes permissible subsequent edits.
- Boundary reachability: multi-agent cooperation is a documented first-party supported coding mode; `spawn_agent` and `claim_write_scope` are wired model-facing harness controls and the shared registry/fence is passed to child executors.
- Why this is / is not agent-owned: the registry cannot decide *which* legitimate coding scope to work on next; it returns conflict facts, leaving the discretionary coordination adjustment to the agent. The `--parallel` Git merge policy alone would not justify this `A` classification.
- Evidence: [sub-agent coordination contract](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/sub_agent.rs), [scope control definitions](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/injected_tools.rs), [atomic registry and denial feedback](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/ownership.rs), [runtime integration](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/executor/drive.rs).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: structural reachability, not a recorded provider-run example of a model responding to a denied claim; the reported `A` is the supported agent-choice loop and does not credit deterministic Git merge conflict ordering as autonomy.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function that reallocates resources/commitments or corrects an operational portfolio on behalf of the whole is established beyond task-local execution and concurrency enforcement.
- Disturbance / variety regulated: budgets, subprocess failures, overlapping edits and unfinished delegated work are mechanically tracked or regulated as per-task limits and S2 conflict control.
- Decisive decision or feedback right: no separate whole-system S3 current resource/commitment bargain or portfolio intervention right is evidenced.
- Decision owner: not established for S3; the parent agent owns coding/delegation choices, while host/runtime enforce budgets, permissions, lifecycle and safety limits.
- Supporting / enforcement mechanisms: task plan and progress ledger, child-spawn/status notices, residual budgets, concurrency permits, cancellation, settlement and explicit goal closeout.
- Closure path: child results return to the parent coding task, and hard limits stop work; no independently identified whole-current control decision and corrective return across an operating portfolio is shipped.
- Why this is / is not agent-owned: the parent is a coordinator of task implementation, but spawning, decomposing, waiting for children and receiving their reports do not alone establish S3. The deterministic budget/termination mechanisms enforce rather than autonomously choose organizational commitments.
- Evidence: [architecture §§5, 14–15](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/docs/ARCHITECTURE.md), [plan tool](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/update_plan.rs), [child settlement and goal closeout](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/executor/drive.rs), [parallel candidate integration](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-app/src/parallel.rs).
- Basis: structural absence review.
- Confidence: medium.
- Caveats: a future or customized multi-goal deployment could add whole-system allocation/oversight; no such first-party closed S3-specific mode was identified at this frozen revision.

### Absence scope

- Surfaces inspected: model request context, task plan and goal controls, parent/child collaboration, child settlement, residual budget enforcement, parallel candidate integration, runtime/host authority and architecture documentation.
- Plausible first-party paths checked: parent resource arbitration among operating units, current whole-portfolio monitoring, change of shared commitments based on aggregate performance and exception-triggered intervention independent of task decomposition.
- Why no material first-party path remains: shipped parent discretion is about a user coding goal and delegated subtasks; limits and collision guards are runtime/S2 enforcement. None of the reviewed operating paths establishes an additional whole-system current-control function with its own decisive and closed return.

## S3* — Complementary audit

- State: A
- Function: in the supported opt-in `/develop` mode, a distinct read-only reviewer independently checks the implemented code against the original user goal and returns corrective verdicts to the implementing loop.
- Disturbance / variety regulated: an implementer may incorrectly report that a change satisfies its work order, or the original analysis/work order may have misunderstood the real defect.
- Claim being audited: Coding's actual delivered source changes meet the original user goal and the causal work order is sound.
- Ordinary reporting path: the coding agent's own completion report, chosen tests and tool observations.
- Complementary access path: a separately launched read-only Reviewer child receives original goal, work order, coding report, changed-file list and Git diff, then reads the actual workspace code around the change independently of the implementer's report.
- Independence boundary: the Reviewer is a separate harness-launched child conversation with read-only capability, not a model-requestable writer role; it is specifically instructed that the implementer's report is a claim and that it must inspect raw changed code. The default provider model may be shared, so this is contextual/evidence-path independence, not independent vendor or research-audit attestation.
- Who acts on findings: the first-party `/develop` controller parses the reviewer's explicit PASS/REWORK/REANALYZE judgment and routes REWORK back to the Coding agent or REANALYZE back to Analyze, with a bounded send-back count and truthful incomplete terminal.
- Decisive decision or feedback right: the read-only reviewer model owns whether the reviewed change passes or requires a particular corrective return; the harness only parses the explicit verdict and routes it.
- Decision owner: autonomous read-only reviewer agent in the `/develop` operating mode; deterministic parser/loop is enforcement and transmission.
- Supporting / enforcement mechanisms: user-initiated mode selection, separate reviewer role/permissions, direct source-reading tools, diff acquisition, explicit decision marker, bounded send-backs, runtime attribution and durable task lifecycle.
- Closure path: original goal and raw changed code → independent reviewer judgment → PASS terminates or REWORK/REANALYZE returns evidence and directs another implementation/analysis pass → renewed review.
- Boundary reachability: README exposes `/develop`; `run_develop_loop` directly launches Analyze/Review through `develop_stage` with the read-only Reviewer child profile. This is a shipped opt-in first-party path, not a future Review product, user-authored reviewer prompt or CI action.
- Why this is / is not agent-owned: removing the reviewer model leaves only code/diff transport and a parser with no semantic PASS versus REWORK decision; the reviewer does that judgment. Merely enabling the separate optional closure reviewer would supply warnings but not this corrective loop.
- Evidence: [README `/develop`](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/README.md), [Review brief/decisions](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/coding/develop.rs), [closed `run_develop_loop`](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/coding/run.rs), [read-only reviewer profile](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/child_profile.rs), [closure-review opt-in distinction](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/coding/policy.rs).
- Basis: explicit + structural.
- Confidence: high for the opt-in construction and return; medium for independence strength beyond distinct read-only context.
- Caveats: no live provider-run audit trace was executed, the same model/provider may serve both agents, and a conditional `/develop` path is not always-on audit for ordinary `leveler run`.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party closed external-and-prospective environment sensing, adaptation-option selection and return into current organizational capability is established.
- Disturbance / variety regulated: current task requirements, provider choice and web search results may influence immediate coding, but are not an ongoing future-oriented adaptation function.
- Decisive decision or feedback right: no supported agent-owned prospective portfolio/capability adaptation decision.
- Decision owner: not established for S4; user/project decides what to build, and deterministic updater tracks stable binary releases without forming strategic options.
- Supporting / enforcement mechanisms: optional web-search tool, plan/skill/memory features, provider capabilities, automatic release checks and installer verification.
- Closure path: task investigation and stored memory affect the present coding request; stable-release updater can replace a binary on configured schedule, but no future-environment model → adaptation option → organizational return is evidenced.
- Why this is / is not agent-owned: remembering code, searching the web for a task, authoring an agent definition or automatically downloading a stable release does not itself generate externally and prospectively justified adaptation choices for the harness.
- Evidence: [README web/updates/custom agents](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/README.md), [architecture model vs runtime and product evolution](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/docs/ARCHITECTURE.md), [memory extraction](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/memory_extract.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: user extensions could compose an adaptation organization, but that is not a shipped closed first-party S4 path.

### Absence scope

- Surfaces inspected: runtime request/context and memory flows, optional search, updater, skills/agents registry, Develop workflow, CLI modes, architecture and release/docs surfaces.
- Plausible first-party paths checked: sensing future external changes, building competing adaptation options, choosing an option under legitimate capability authority, and feeding that choice into present operation.
- Why no material first-party path remains: these shipped mechanisms serve immediate tasks, persistence, configuration or deterministic software update, not a materially closed outside-and-then adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no first-party organizational identity/ultimate-policy dispute and legitimate authoritative ratification/return loop is established for the coding product.
- Disturbance / variety regulated: risky file/command/network effects, user prompts, authority changes and agent definitions are bounded by host permissions and per-turn configuration, not a constitutional identity decision process.
- Decisive decision or feedback right: none for ultimate-policy/identity closure; user owns task and local permissions, and code controls which effects are admitted.
- Decision owner: not established for S5; human/host is decisive for individual effect grants, without a separate S5-specific parent-governed institutional loop.
- Supporting / enforcement mechanisms: assisted/request-approval profiles, host authority, isolation, capability admission, agent/skill configuration, permission prompts and durable events.
- Closure path: requested effect → host permission/sandbox decision → allowed or denied operation; no identity-level question → legitimate parent policy decision → durable changed policy governing subsequent operation is shipped.
- Why this is / is not agent-owned: safety checks and human permissions concern local effect rights; a user can change instructions/agents but there is no evidence of a distinct ultimate-policy process beyond the ordinary product boundary.
- Evidence: [README permissions and custom agents](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/README.md), [architecture Host Authority](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/docs/ARCHITECTURE.md), [authorization controls](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/authorization.rs), [child profile/capability controls](https://github.com/dengmengmian/CodeLeveler/blob/b08f9013e1bd62801ef0eca60169f566f7fb6b5d/crates/leveler-agent/src/child_profile.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: the human operating the local coding tool retains legitimate external authority, but ordinary approvals are not a positive S5 parent mode under this Methodology.

### Absence scope

- Surfaces inspected: permission/configuration policy, host execution authority, model/task prompts, user-defined agent and skill management, persistent session state and product governance documentation.
- Plausible first-party paths checked: identity/mission dispute, legitimate S5 authority delegation or ratification, binding policy-resolution record, and durable returned control over subsequent coding work.
- Why no material first-party path remains: observed controls regulate single-session effect safety and configurable capabilities, with no shipped identity-level decision and return channel.

## Recursion

The parent and child model/tool loops have local task roles, environment contact and some bounded autonomy; the child nesting mechanism alone does not demonstrate all metasystem functions needed for an independent recursive viable system. This assessment is at one user-goal/workspace operating boundary. The optional `/develop` read-only reviewer is complementary access to that work, not another S1 coding unit merely because it is an agent process.

## Variety and escalation

The model/tool loop amplifies responses to varied source/code failures. Workspace/write-scope grants attenuate inter-agent edit collisions and report exact conflict feedback; host permissions isolate uncontrolled side effects; persisted transcripts, child settlements and budgets preserve task continuity. The `/develop` reviewer can reject both implementation and causal analysis, routing correction to the appropriate stage. These paths are not evidence of a higher organizational policy or prospective strategy function. Exceptional permission requests and failed tasks are not by themselves algedonic organizational channels.

## Evidence gaps

Static frozen-source read and documented supported-mode reconstruction, with no provider-backed E2E, Rust test run or live reviewer trace. Structural code shows agent discretion in scope selection and a closed read-only corrective reviewer, but does not measure empirical coordination or auditor independence under adversarial conditions. This review does not claim that default ordinary coding runs always activate `/develop` or that CLI evaluation tests form an operational S3* audit. Source tree and Git revision were verified locally; external model credentials and OS isolation capabilities were not exercised.

## Assessment summary

CodeLeveler ships an autonomous model/tool coding loop (**S1=A**), a multi-agent write-collision attenuation path with model-selected scope adjustment (**S2=A**) and an explicitly user-invoked, separate read-only reviewer whose code-grounded verdict returns to implementation or analysis (**S3*=A**). Task-local orchestration and enforcement do not independently establish whole-system current control, future-environment capability adaptation or ultimate policy closure (**S3/S4/S5=—**). The vector is boundary- and mode-specific, not a performance or compliance score.

Proposed vector: **`A · A · — · A · — · —`**.
