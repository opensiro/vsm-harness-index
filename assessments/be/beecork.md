---
harness_id: beecork
project_name: beecork
repository: https://github.com/beecork/beecork
review_ref: fabecb4e8690f2fa347cc750dd0d2dc71ee493dc
reviewed_at: 2026-10-30
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

# beecork

## Review boundary

- System in focus: the repository's from-scratch terminal coding agent, not the separately identified beecork-pipe product.
- Purpose and identity: complete coding tasks through model-directed repository tools, user steering and bounded permissions.
- Relevant environment: local project, user/operator, OpenRouter model service, OS sandbox/shell, optional MCP servers and paired browser extension.
- Standard-distribution boundary: package.json binary/src/index.ts, src/agent.ts, first-party tool/permission/session/journal/task/explorer systems and packaged skills/extension.
- Credited operating / distribution surfaces: ordinary runTurn and restricted exploreLoop plus first-party tool dispatch and returned observations.
- Adjacent first-party surfaces excluded from ownership: .claude development/dogfood prompts, audits/, eval/, test fixtures and release/development scripts; beecork-pipe is explicitly separate.
- First-party operating / deployment modes considered: interactive/piped terminal, normal/auto-approve/read-only/plan permission modes and documented disposable permission-skip mode, optional commands/background processes, explorer, MCP and browser signals.
- Recursion level: one terminal coding session and its focused investigation children.
- Reviewed revision: `fabecb4e8690f2fa347cc750dd0d2dc71ee493dc`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/README.md) separates this coding agent from beecork-pipe. [Package boundary](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/package.json) ships a Node terminal binary, skills, skeleton/extension resources. The entry point calls [runTurn](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L584-L710): append user input, compact context, drain mid-turn steering, request a model response, dispatch tool calls and append their results until a final response or step/abort condition. Independent read calls may run concurrently; mutation calls remain serialized within the parent loop and approvals/sandbox bound their execution.

A dedicated [read-only explorer](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/subagent.ts#L24-L92) uses a fresh context and restricted read/search/web schema, returning a text summary. Background tasks are shell processes with incremental output/check/stop APIs and process-exit cleanup, not autonomous subordinate model cells. Journal events record decisions/outcomes at tool boundaries. Configured post-edit verification feeds command output back into the normal coding loop. Browser tools request approved-site capture and consume console/network symptoms through the paired extension. Memory/settings distinguish trusted user instructions from lower-trust project context; session sealing preserves interrupted tool-call history.

## Operational model

The parent model owns coding choices. The explorer owns a bounded investigation strategy and returns findings; it cannot mutate, run commands or recurse. Tool dispatch, parallel batching, approvals, journal persistence, kernel sandbox and provider APIs are supporting machinery. Background builds/watchers are tools serving the same coding operation. No organization-wide control, independent auditor or identity authority is borrowed from adjacent eval/audit/development files.

## S1 — Operations

- State: A
- Function: produce and repair repository artifacts and answer code investigations.
- Disturbance / variety regulated: user requirements/steering, file contents, execution errors, tool denials and unexpected model/command results.
- Decisive decision or feedback right: model chooses the next code/search/edit/command action, interpretation or final answer after observations.
- Decision owner: parent coding model; explorer model for its narrower read-only task.
- Supporting / enforcement mechanisms: OpenRouter adapter, tool schemas/dispatch, permission decision, OS sandbox, conversation/session state and bounded step loop.
- Closure path: tool outcomes, configured auto-check output and explorer findings become model-visible tool messages; the next iteration acts on them.
- Boundary reachability: shipped binary src/index.ts invokes runTurn; its actual explore tool invokes runExplorer and the supplied fresh-context exploreLoop.
- Why this is / is not agent-owned: the runtime executes/constrains requests but cannot choose a coding strategy without the model.
- Evidence: [Entry invocation](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/index.ts#L370-L385), [Model-action cycle](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L584-L710), [Tool/verification feedback](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L440-L505), [Explorer tool](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/tools.ts#L984-L1004), [Child loop](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/subagent.ts#L48-L92).
- Basis: structural.
- Confidence: high.
- Caveats: availability at the frozen source, not measured coding performance or a verified sandbox guarantee; provider execution was not run.

## S2 — Coordination

- State: —
- Function: no material first-party path established for this function at the assessed session boundary.
- Disturbance / variety regulated: Parallel read-only tool batches belong to one actor; the separate explorer cannot mutate or run commands. Parent serial writes do not establish a relation regulating conflict among distinct coding cells.
- Decisive decision or feedback right: no qualifying function-specific organizational right/feedback owner established.
- Decision owner: local model/operator/developer choices exist, without establishing this higher function.
- Supporting / enforcement mechanisms: tool/runtime/permission/persistence machinery is not promoted from implementation labels.
- Closure path: operational feedback exists; a distinct function-specific closure is not supplied.
- Why this is / is not agent-owned: the organizational relation is tested first, independently of whether a model calls a named tool.
- Evidence: [src/agent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L648-L679), [src/subagent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/subagent.ts#L1-L33), [src/subagent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/subagent.ts#L110-L158).
- Basis: structural.
- Confidence: medium within the reviewed first-party distribution.
- Caveats: bounded absence; custom MCP tools or an external organization are not imported.

### Absence scope

- Surfaces inspected: parent isParallelSafe/read batching, explore allowlist/gate, tool mutation paths and background task APIs.
- Plausible first-party paths checked: read concurrency, serialized writes, explorer context isolation and background shell jobs.
- Why no material first-party path remains: No supplied distinct interacting mutating S1 units plus interference-specific coordination response/returned adjustment is established. Generic batching, delegation and independent context are not S2-specific construction paths.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party path established for this function at the assessed session boundary.
- Disturbance / variety regulated: The model checks/stops background shell jobs and keeps todos; runtime enforces task/step limits and exit cleanup. These are current-task tools, not a demonstrated whole-system regulator over autonomous subordinate operational commitments.
- Decisive decision or feedback right: no qualifying function-specific organizational right/feedback owner established.
- Decision owner: local model/operator/developer choices exist, without establishing this higher function.
- Supporting / enforcement mechanisms: tool/runtime/permission/persistence machinery is not promoted from implementation labels.
- Closure path: operational feedback exists; a distinct function-specific closure is not supplied.
- Why this is / is not agent-owned: the organizational relation is tested first, independently of whether a model calls a named tool.
- Evidence: [src/tasks.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/tasks.ts#L71-L128), [src/tools.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/tools.ts#L930-L954), [src/agent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L607-L630).
- Basis: structural.
- Confidence: medium within the reviewed first-party distribution.
- Caveats: bounded absence; custom MCP tools or an external organization are not imported.

### Absence scope

- Surfaces inspected: runTurn, todos/background tool definitions, task map/status/stop lifecycle, permission modes and steering.
- Plausible first-party paths checked: background capacity cap, check_task/stop_task, user mid-turn instructions, Ctrl-C and task planning.
- Why no material first-party path remains: The owned shell processes are tools/dev servers/builds rather than distinct autonomous coding S1 cells. Their lifecycle APIs and local operator intervention do not establish the whole-system view plus organizational control relation needed for S3 or P.

## S3* — Complementary audit

- State: —
- Function: no material first-party path established for this function at the assessed session boundary.
- Disturbance / variety regulated: Configured post-edit checks return through the producer's ordinary tool result. Journal records the same operational path; browser signals add useful application observations, but the same coding actor requests/interprets them. The independent-context explorer is a generic investigator rather than a supplied audit-specific owner.
- Decisive decision or feedback right: no qualifying function-specific organizational right/feedback owner established.
- Decision owner: local model/operator/developer choices exist, without establishing this higher function.
- Supporting / enforcement mechanisms: tool/runtime/permission/persistence machinery is not promoted from implementation labels.
- Closure path: operational feedback exists; a distinct function-specific closure is not supplied.
- Why this is / is not agent-owned: the organizational relation is tested first, independently of whether a model calls a named tool.
- Evidence: [src/agent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L473-L505), [src/subagent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/subagent.ts#L24-L33), [src/journal.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/journal.ts#L1-L42), [src/tools.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/tools.ts#L1040-L1157).
- Basis: structural.
- Confidence: medium within the reviewed first-party distribution.
- Caveats: bounded absence; custom MCP tools or an external organization are not imported.

### Absence scope

- Surfaces inspected: auto-check/runVerify, journal, explorer prompt/restricted tools, browser signals/watch tools and adjacent audits/eval directories.
- Plausible first-party paths checked: fresh-context exploration, test output, append-only records, browser console/network reality and repository audit files.
- Why no material first-party path remains: No material first-party independent claim-challenging judgment plus corrective-control relation is supplied as audit. Routine verification remains in production; explorer research is generic, browser telemetry is directly consumed by the producer, and development audits/eval are adjacent.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path established for this function at the assessed session boundary.
- Disturbance / variety regulated: Web tools/explorer and browser signals investigate present tasks. remember preserves preferences/conventions; model/effort settings and package update commands change configuration/software but do not by themselves establish prospective adaptation judgment.
- Decisive decision or feedback right: no qualifying function-specific organizational right/feedback owner established.
- Decision owner: local model/operator/developer choices exist, without establishing this higher function.
- Supporting / enforcement mechanisms: tool/runtime/permission/persistence machinery is not promoted from implementation labels.
- Closure path: operational feedback exists; a distinct function-specific closure is not supplied.
- Why this is / is not agent-owned: the organizational relation is tested first, independently of whether a model calls a named tool.
- Evidence: [src/memory.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/memory.ts#L50-L86), [src/agent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L23-L46), [src/update.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/update.ts#L120-L166), [src/tools.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/tools.ts#L1118-L1157).
- Basis: structural.
- Confidence: medium within the reviewed first-party distribution.
- Caveats: bounded absence; custom MCP tools or an external organization are not imported.

### Absence scope

- Surfaces inspected: memory/settings, web/explorer/browser tools, instruction prompt, compaction, version-notice/selfUpdate and skills.
- Plausible first-party paths checked: web research, production-site diagnostics, remembered user feedback, model selection and npm update notification.
- Why no material first-party path remains: These are present-task sensing, context reuse and software-maintenance mechanisms. No external/future distinction to developed adaptation option to returned current-capability loop with a decisive S4 owner is supplied in the coding-session boundary.

## S5 — Policy and identity

- State: —
- Function: no material first-party path established for this function at the assessed session boundary.
- Disturbance / variety regulated: Permission modes, risky-action guards, global/project trust tiers and ask_user steer concrete coding choices. None by itself routes an identity/ultimate-policy issue to a legitimate authority and returns a governance decision.
- Decisive decision or feedback right: no qualifying function-specific organizational right/feedback owner established.
- Decision owner: local model/operator/developer choices exist, without establishing this higher function.
- Supporting / enforcement mechanisms: tool/runtime/permission/persistence machinery is not promoted from implementation labels.
- Closure path: operational feedback exists; a distinct function-specific closure is not supplied.
- Why this is / is not agent-owned: the organizational relation is tested first, independently of whether a model calls a named tool.
- Evidence: [src/agent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L98-L154), [src/memory.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/memory.ts#L50-L86), [src/agent.ts](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/src/agent.ts#L507-L535), [README.md](https://github.com/beecork/beecork/blob/fabecb4e8690f2fa347cc750dd0d2dc71ee493dc/README.md).
- Basis: structural.
- Confidence: medium within the reviewed first-party distribution.
- Caveats: bounded absence; custom MCP tools or an external organization are not imported.

### Absence scope

- Surfaces inspected: approval decision and permission modes, instruction/settings trust separation, user question/steering paths and README boundaries.
- Plausible first-party paths checked: normal/auto/read-only/plan modes, disposable skip flag, trusted cork.md, project rules and ordinary user approvals.
- Why no material first-party path remains: The supplied returns govern actions/preferences/context, not ultimate-policy tension at the session recursion. Static safety text and trusted human configuration do not establish autonomous/constructor S5 or a function-specific parent P loop.

## Distributed OSS parent arrangement

Package maintainers and their development/audit workflows are adjacent to distributed local sessions. Users control their own tasks; no organization-level parent arrangement is inferred from public contribution or author identity.

## Self-hosted and non-human modes

Normal/auto/read-only/plan and documented disposable permission-skip configurations were considered as capabilities, not executed. Optional MCP/paired extension are external inputs/tools. No alternative non-human governance organization or qualifying parent metasystem mode is supplied.

## Recursion

A depth-one fresh-context explorer is a real autonomous investigation cell, but its supplied operations/constraints do not establish a complete recursively viable organization. Background shell processes are not elevated to agents.

## Variety and escalation

Tool denial/error, stderr/verification, browser symptoms and mid-turn user steering return operational variety. Step limits, context recovery, abort sealing and process-group cleanup preserve bounded control/recovery. Journaling makes exceptions visible without itself proving audit, algedonic authority or S5.

## Evidence gaps

Frozen source was obtained through the exact GitHub archive ref; no repin. Node/nodejs/npm/bun/deno are unavailable on the inspection host, so native TypeScript tests/typecheck/build were not run and no native PASS is claimed. No provider-backed agent E2E, browser pairing or command sandbox experiment ran. Structural source evidence is sufficient for the bounded mapping; no guarantee of security, provider behavior, performance or successful response to every observation is inferred.
