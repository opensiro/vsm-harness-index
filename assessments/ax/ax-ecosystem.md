---
harness_id: ax-ecosystem
project_name: AX ecosystem
repository: https://github.com/3-lines-studio/ax
review_ref: 166905e4953f011a2c930abb18ca420d6340e4d1
reviewed_at: 2026-10-29
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

# AX ecosystem

## Review boundary

- System in focus: the released AX programs assembled around one bot directory and its conversations.
- Purpose and identity: carry out user tasks using a model-directed tool loop through portable local/MCP capabilities.
- Relevant environment: users, workspaces, external APIs, model providers, tool processes and host failures.
- Standard-distribution boundary: AX engine, shipped providers, Botdir loader and supported CLI/webi/slaxi transports, including optional boti serve and deterministic routines.
- Credited operating / distribution surfaces: cmd/ax runStream and catalog dispatch; local providers; supported bot.toml configuration, sessions and transports.
- Adjacent first-party surfaces excluded from ownership: repository contributor AGENTS.md, packaging/release CI and development tests. Promotion checks corroborate deployment behavior but do not supply an independent organizational actor.
- First-party operating / deployment modes considered: direct ax CLI; persistent webi/slaxi transport; boti-supervised deployment; operator-triggered promotion/rollback; deterministic scheduled routines.
- Recursion level: one deployed bot; conversations are operational work episodes, providers are tools rather than automatically independent S1 units.
- Reviewed revision: 166905e4953f011a2c930abb18ca420d6340e4d1.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

A single Go module ships independent binaries. AX requests a model response, dispatches selected calls through a catalog of local describe/run providers or MCP connections, appends results, and repeats. JSONL sessions and compaction retain conversation state. webi and slaxi expose the engine; fsx/bashx and other providers perform actions. User steering is drained into later model history. boti manages installation and process health, with crash-loop rollback and idle-aware activation of a tested build. Routines are explicitly model-free programs with per-routine exclusion locks and cron dispatch. Personal memory stores facts, not a prospective adaptation controller. See [README.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/README.md), [cmd/ax/loop.go](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/cmd/ax/loop.go), [docs/routines.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/docs/routines.md) and [docs/deploy.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/docs/deploy.md).

## Operational model

The model in each AX conversation chooses tools and subsequent actions toward the user's requested outcome. Runtime catalog, cancellation, retry, truncation checks and parallel execution enforce developer-selected mechanics. The user chooses the initial task and may steer; no separate shipped policy authority is inferred from that input. A model provider supplies inference to the first-party loop; it is not an external coding-agent loop borrowed wholesale. Neither independent binaries nor parallel tool invocations establish separate viable organizational cells.

## S1 — Operations

- State: A
- Function: produce user-requested workspace/information outcomes through iterative model decisions and tool feedback.
- Disturbance / variety regulated: unknown workspace state, tool errors, incomplete results and changing task evidence.
- Decisive decision or feedback right: select tool calls, interpret their returned content and choose the next action or final response.
- Decision owner: model-backed AX conversation actor.
- Supporting / enforcement mechanisms: catalog search/execute, providers, validated arguments, deadlines, retry/cancellation and append-only history.
- Closure path: requestStream returns calls; runToolBatch executes them; pushToolResult adds observations to history consumed by the next request.
- Boundary reachability: supported ax command directly calls this shipped loop with configured connections; webi/slaxi use that engine rather than requiring a developer to implement an agent.
- Why this is / is not agent-owned: removing the model leaves dispatch and limits but no task-specific choice of actions; a human need not choose each tool.
- Evidence: [cmd/ax/loop.go](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/cmd/ax/loop.go); [cmd/ax/README.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/cmd/ax/README.md); [cmd/ax/tools.go](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/cmd/ax/tools.go).
- Basis: structural.
- Confidence: high.
- Caveats: source establishes ownership and reachability, not task success, safety or comparative performance; tools and credentials remain deployment-specific.

## S2 — Coordination

- State: —
- Function: Distinct conversations and routines can coexist, but parallel tools are one actor's calls, and a routine's non-overlap lock prevents duplicate deterministic execution rather than closing a specific mutual-adjustment relation among distinct autonomous S1 units.
- Disturbance / variety regulated: interference between separate operational agents; no qualifying regulatory path established.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: no qualifying first-party owner; ordinary runtime/configuration/operator rights remain separate.
- Supporting / enforcement mechanisms: the named mechanisms below support S1 or deployment, without owning this function.
- Closure path: no qualifying function-specific closure supplied.
- Why this is / is not agent-owned: function not established; deterministic execution or generic agent extensibility cannot substitute for it.
- Evidence: [docs/routines.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/docs/routines.md); [internal/routine/scheduler.go](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/internal/routine/scheduler.go).
- Basis: structural, bounded negative adjudication.
- Confidence: medium-high.
- Caveats: absence is relative to the reviewed standard distribution, not a universal inability to compose another system.

### Absence scope

- Surfaces inspected: loop parallelism, routines, scheduler, per-channel state and Botdir.
- Plausible first-party paths checked: tool batch sequencing and per-routine lock/scheduled skip.
- Why no material first-party path remains: The shipped routine is expressly model-free and per-channel isolated. No S2-specific inter-agent conflict-response and returned adjustment loop is provided at this bot boundary.

## S3 — Inside-and-now control

- State: —
- Function: The host reports build/process health and restarts or rolls back according to fixed rules. AX exposes local task steering and developer limits, without a whole-bot resource/commitment bargaining or current-control decision actor.
- Disturbance / variety regulated: whole-bot resource and commitment pressure; no qualifying regulatory path established.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: no qualifying first-party owner; ordinary runtime/configuration/operator rights remain separate.
- Supporting / enforcement mechanisms: the named mechanisms below support S1 or deployment, without owning this function.
- Closure path: no qualifying function-specific closure supplied.
- Why this is / is not agent-owned: function not established; deterministic execution or generic agent extensibility cannot substitute for it.
- Evidence: [cmd/boti/serve.go](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/cmd/boti/serve.go); [docs/deploy.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/docs/deploy.md).
- Basis: structural, bounded negative adjudication.
- Confidence: medium-high.
- Caveats: absence is relative to the reviewed standard distribution, not a universal inability to compose another system.

### Absence scope

- Surfaces inspected: engine cancellation/limits, boti host state/control, promotion/rollback and deployment docs.
- Plausible first-party paths checked: host status/restart/rollback, human steering, model/tool limits and idle activation.
- Why no material first-party path remains: These are liveness/deployment or local task actions. Neither the deterministic supervisor nor an ordinary operator command supplies an established whole-system discretionary current-control loop. A function-specific parent mode is not evidenced.

## S3* — Complementary audit

- State: —
- Function: Session logs, provider errors, selftest and pre-promotion go vet/go test provide ordinary execution/deployment checks. No complementary independent audit judgment challenges operational claims and returns corrective control.
- Disturbance / variety regulated: unreliable operational success claims; no qualifying regulatory path established.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: no qualifying first-party owner; ordinary runtime/configuration/operator rights remain separate.
- Supporting / enforcement mechanisms: the named mechanisms below support S1 or deployment, without owning this function.
- Closure path: no qualifying function-specific closure supplied.
- Why this is / is not agent-owned: function not established; deterministic execution or generic agent extensibility cannot substitute for it.
- Evidence: [cmd/boti/promote.go](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/cmd/boti/promote.go); [cmd/ax/loop.go](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/cmd/ax/loop.go).
- Basis: structural, bounded negative adjudication.
- Confidence: medium-high.
- Caveats: absence is relative to the reviewed standard distribution, not a universal inability to compose another system.

### Absence scope

- Surfaces inspected: engine sessions/results, routine histories, deployment selftest and promotion validation.
- Plausible first-party paths checked: independent reading of raw tool artifacts, host health, build tests and selftest.
- Why no material first-party path remains: The actual paths remain producer feedback or deterministic release validation. No separately controlled audit actor/access-and-corrective-feedback arrangement is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: Web/tool access, durable memory, skill loading, routine authoring and transactional promotion can support new capabilities, but the distribution does not ship an external-and-prospective sensing/options dialogue with current capability.
- Disturbance / variety regulated: future environmental changes requiring capability adaptation; no qualifying regulatory path established.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: no qualifying first-party owner; ordinary runtime/configuration/operator rights remain separate.
- Supporting / enforcement mechanisms: the named mechanisms below support S1 or deployment, without owning this function.
- Closure path: no qualifying function-specific closure supplied.
- Why this is / is not agent-owned: function not established; deterministic execution or generic agent extensibility cannot substitute for it.
- Evidence: [docs/deploy.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/docs/deploy.md); [cmd/memoryx/README.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/cmd/memoryx/README.md).
- Basis: structural, bounded negative adjudication.
- Confidence: medium-high.
- Caveats: absence is relative to the reviewed standard distribution, not a universal inability to compose another system.

### Absence scope

- Surfaces inspected: catalog/tools and memory, bot definition, routines, deployment update/promote/rollback.
- Plausible first-party paths checked: agent-written routines or code, external web information, model/provider configuration and operator upgrades.
- Why no material first-party path remains: Those paths execute requested work or install an already-selected build. No supplied adaptation judgment develops future-facing options and returns them to a current-capability regulator; generic shell access does not close S4 or its parent mode.

## S5 — Policy and identity

- State: —
- Function: bot.md, bot.toml, connection trust and host/vault controls constrain operation. They do not route an identity or ultimate-policy tension to a legitimate authority and apply its returned resolution.
- Disturbance / variety regulated: identity and ultimate-policy tension; no qualifying regulatory path established.
- Decisive decision or feedback right: no function-specific decisive right supplied.
- Decision owner: no qualifying first-party owner; ordinary runtime/configuration/operator rights remain separate.
- Supporting / enforcement mechanisms: the named mechanisms below support S1 or deployment, without owning this function.
- Closure path: no qualifying function-specific closure supplied.
- Why this is / is not agent-owned: function not established; deterministic execution or generic agent extensibility cannot substitute for it.
- Evidence: [docs/botdir/BOTDIR.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/docs/botdir/BOTDIR.md); [AGENTS.md](https://github.com/3-lines-studio/ax/blob/166905e4953f011a2c930abb18ca420d6340e4d1/AGENTS.md).
- Basis: structural, bounded negative adjudication.
- Confidence: medium-high.
- Caveats: absence is relative to the reviewed standard distribution, not a universal inability to compose another system.

### Absence scope

- Surfaces inspected: Botdir specification, runtime configuration, user steering, host controls and contributor rules.
- Plausible first-party paths checked: system instructions, trust/secret configuration, human steering and repository governance.
- Why no material first-party path remains: Configuration and ordinary input lack a function-specific runtime identity/policy adjudication-return path. Contributor governance belongs to the adjacent development organization, not this deployed bot. No autonomous or parent S5 mode is supplied.

## Distributed OSS parent arrangement

Repository maintainers govern development. No organization-level parent S3/S4/S5 is borrowed into user deployments from contributor rules. A user's ordinary steering does not itself establish those functions.

## Self-hosted and non-human modes

The reviewed self-hosted boti/webi path supplies working process supervision and configuration. No separately closed parent-governed organizational mode was found; model-free routines do not become non-human viable organizations by scheduling alone.

## Recursion

Bot directories, threads, tool processes and routines expose technical nesting/isolation. No recursively viable child with its own evidenced metasystem is established.

## Variety and escalation

Catalog discovery amplifies S1 tool choice; result history preserves operational feedback. Truncation checks, timeouts, retries, cancellation and compaction attenuate runtime variety. Host crash-loop rollback addresses liveness. Errors and notifications remain observations; no exceptional signal-to-organizational-authority closure is inferred from a failed status.

## Evidence gaps

No live provider, user-task or deployment run was performed. External MCP implementations and private deployments are outside the source boundary. The reviewed supplied deployment/update paths do not establish future adaptation or identity authority. No specific unresolved shipped function path requires an unknown state within this declared bot boundary.
