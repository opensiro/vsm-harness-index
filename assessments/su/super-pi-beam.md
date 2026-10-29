---
harness_id: super-pi-beam
project_name: Super-Pi-BEAM
repository: https://github.com/oleksandr/super-pi-beam
review_ref: 03c6afd6d8250eaeb4ebca039290f95a9ab73227
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Super-Pi-BEAM

## Review boundary

- System in focus: the first-party configured Gemini-backed conversation runtime, CLI/AGY and multi-conversation gateway within one BEAM application.
- Purpose and identity: execute durable user tasks through a model/tool loop with persisted conversation/task state and optional customization.
- Relevant environment: user workspaces, Gemini service, concurrent conversations, filesystem mutation, crashes and client transports.
- Standard-distribution boundary: lib/super_pi conversation/durable/tools/env, shipped Gemini adapter, CLI/harness presets, gateway/RPC and AGY extensions at the frozen revision.
- Credited operating / distribution surfaces: configured model invocation → tool-call execution → persisted tool result → derived context loop; same-node per-path Local/FileLock coordination constructor.
- Adjacent first-party surfaces excluded from ownership: injected scripted test responders, TestAuditExtension/OneShotVerificationExtension, examples, property tests and development/release material. Source tests corroborate intended behavior but are not a shipped independent audit actor.
- First-party operating / deployment modes considered: configured Gemini AGY/direct/gateway sessions, native read-only planner preset, configurable hooks/permissions, RPC/TUI; unconfigured echo and external-client tool-only MCP modes considered separately.
- Recursion level: one local application with independent user-task conversation actors; durable child task records are not automatically viable cells.
- Reviewed revision: 03c6afd6d8250eaeb4ebca039290f95a9ab73227
- Observation date: 2026-10-29
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Elixir gen_statem persists model turns and tools through Ecto/SQLite or configured PostgreSQL. GeminiClient converts derived messages/tools to HTTP/SSE requests and normalizes model tool calls. Machine executes each call through extensions and SandboxRunner, appends tool observations and starts another request. No-tool completion can be continued by after_run hooks. TaskEngine provides restart/wait/abort state transitions; several Oban jobs broadcast notifications, which alone do not prove worker execution. Local file mutation passes through same-node Registry-backed FileLock. CLI and gateway wire supported presets and real tools. The unconfigured responder returns echo; advertised model labels are not proof all provider modes work. MCP harness_task's startup call passes conv.id rather than Machine's documented option list, so it is not used as S1 reachability evidence.

## Operational model

Each configured conversation's model owns task-specific action/continuation decisions; deterministic state transitions and sandbox enforce mechanics. Gemini is an inference provider wired by first-party code, not an external coding-agent loop. Independent gateway conversations can share Local tools and file-lock Registry. File locking supplies a specific coordination primitive but no autonomous conflict-policy actor; lifecycle scheduling and optional hooks are not assumed to own higher functions.

## S1 — Operations

- State: A
- Function: produce task results through model-selected filesystem/shell actions.
- Disturbance / variety regulated: unknown task state, failing tools, changed evidence and incomplete outputs.
- Decisive decision or feedback right: choose tool calls and revise/finish from returned observations.
- Decision owner: model-backed first-party conversation actor in configured Gemini mode.
- Supporting / enforcement mechanisms: gen_statem, durable Storage/Context, HTTP/SSE adapter, typed tools, sandbox and permissions.
- Closure path: Machine invokes configured default_llm_responder → GeminiClient; returned tool_call blocks execute and are stored as pi.message/tool; preparing_request derives those observations for the next model call.
- Boundary reachability: AGY CLI configures a Gemini model and tools and starts Machine with conversation_id options; gateway Standard preset similarly uses a real configured provider branch. This does not depend on test callbacks or the external OpenCode agent's own loop.
- Why this is / is not agent-owned: the model selects goal-directed tools; state machinery persists/transports/enforces those choices without making them.
- Evidence: [lib/super_pi/conversation/machine.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/conversation/machine.ex); [lib/super_pi/ai/gemini_client.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/ai/gemini_client.ex); [lib/super_pi/agy/cli.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/agy/cli.ex); [lib/super_pi/harness/default.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/harness/default.ex)
- Basis: structural
- Confidence: medium-high
- Caveats: Configured provider/tool mode only. Without a supported configured Gemini branch the default responder echoes; no live-provider success or general provider compatibility is claimed.

## S2 — Coordination

- State: C
- Function: attenuate concurrent same-file mutation interference between independent conversation work units.
- Disturbance / variety regulated: read-modify-write races when two same-node conversation actors edit the same expanded path.
- Decisive decision or feedback right: serialize each mutation at the relevant environment/path and return its actual result to the requesting actor; autonomous conflict-policy composition remains external.
- Decision owner: developer-composed coordinating actors/policy over first-party FileLock/Local path.
- Supporting / enforcement mechanisms: Registry-keyed lock GenServer, DynamicSupervisor, Path.expand and Local.write_file/edit_file.
- Closure path: Tools invokes Local mutation; FileLock executes edit's read/replace/write inside exclusive callback; success or target_not_found returns as persisted tool evidence to the actor's next request.
- Boundary reachability: gateway supports separate configured conversation machines in one application; their built-in tools share Local's default env_id and FileLock Registry, initialized by Application. This is a reachable same-node collision-control path.
- Why this is / is not agent-owned: the lock enforces a fixed developer response; no model chooses or revises the coordination policy. C credits an S2-specific interference/feedback primitive, not agent ownership of the lock.
- Evidence: [lib/super_pi/env/file_lock.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/env/file_lock.ex); [lib/super_pi/env/local.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/env/local.ex); [lib/super_pi/tools.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/tools.ex); [lib/super_pi/application.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/application.ex); [lib/super_pi/gateway/router.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/gateway/router.ex); [test/super_pi/env_test.exs](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/test/super_pi/env_test.exs)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-backed same-node primitive, not executed property-test proof. Full-file stale overwrites, symlink aliases, arbitrary bash writes and cross-node races are not solved; autonomous semantic settlement is not supplied.
- Distinct S1 units: independent configured gateway conversation actors carrying separate user-task objectives within one BEAM application.
- Inter-S1 disturbance: parallel mutations can interleave read/replace/write on the same file; source and property-test fixture explicitly target that race.
- Attenuating coordination relation: Local.write/edit use a shared exclusive Registry/GenServer path lock; edit reads current contents after acquisition.
- Feedback into subsequent S1 behaviour: serialized edit result, including changed-target failure, is returned through Tools/Machine history and changes available next actions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the primitive is specifically wired to same-path mutation interference across actors; it is not merely a task queue or tool-call ordering.

## S3 — Inside-and-now control

- State: —
- Function: No supplied whole-system current control loop at this boundary.
- Disturbance / variety regulated: resource/commitment tension across current conversation operations.
- Decisive decision or feedback right: No qualifying function-specific decisive right supplied.
- Decision owner: none established; developer/runtime/user task authority remains separate.
- Supporting / enforcement mechanisms: TaskEngine ownership/wait/abort/restart, Oban queues, live state, RPC configuration/cancel and presets.
- Closure path: No qualifying function closure; inspected foreground-child settlement, restart caps, manual session steering/configuration and permission gates remain support/local task paths.
- Why this is / is not agent-owned: Function-specific positive and parent alternatives checked; names and extension points do not automatically supply organizational ownership.
- Evidence: [lib/super_pi/durable/task_engine.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/durable/task_engine.ex); [lib/super_pi/rpc/server.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/rpc/server.ex)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: TaskEngine ownership/wait/abort/restart, Oban queues, live state, RPC configuration/cancel and presets.
- Plausible first-party paths checked: foreground-child settlement, restart caps, manual session steering/configuration and permission gates.
- Why no material first-party path remains: These are deterministic task lifecycle/local session mechanisms; no supplied whole-current view plus discretionary cross-operation resource/priority/accountability actor or legitimate parent return loop is established. RPC cancel emits a status event and is not credited as actual whole-system intervention.

## S3* — Complementary audit

- State: —
- Function: No supplied complementary independent audit loop at this boundary.
- Disturbance / variety regulated: unreliable operation reports/completion claims.
- Decisive decision or feedback right: No qualifying function-specific decisive right supplied.
- Decision owner: none established; developer/runtime/user task authority remains separate.
- Supporting / enforcement mechanisms: Machine after_run, AGY Stop hook, VerificationWorker notification, transcript export and test extensions.
- Closure path: No qualifying function closure; inspected hook-requested continuation, read-only planner preset, verification job broadcasts and scripted test audit roles remain support/local task paths.
- Why this is / is not agent-owned: Function-specific positive and parent alternatives checked; names and extension points do not automatically supply organizational ownership.
- Evidence: [lib/super_pi/agy/extensions/hooks_json.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/agy/extensions/hooks_json.ex); [lib/super_pi/workers/oban_workers.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/workers/oban_workers.ex)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: Machine after_run, AGY Stop hook, VerificationWorker notification, transcript export and test extensions.
- Plausible first-party paths checked: hook-requested continuation, read-only planner preset, verification job broadcasts and scripted test audit roles.
- Why no material first-party path remains: The shipped path is a generic completion extension/notification, with neither independent raw-operational audit judgment nor controlled corrective authority supplied. TestAuditExtension is test-only; a planner persona and transcript do not close complementary audit.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied outside-and-then intelligence loop at this boundary.
- Disturbance / variety regulated: external future changes requiring capability adaptation.
- Decisive decision or feedback right: No qualifying function-specific decisive right supplied.
- Decision owner: none established; developer/runtime/user task authority remains separate.
- Supporting / enforcement mechanisms: planner/default/AGY presets, skill/plugin discovery, Brain configuration, compaction and dynamic add_tools/handoff.
- Closure path: No qualifying function closure; inspected internal plans, manually enabled plugins/skills, model configuration and tool discovery/control directives remain support/local task paths.
- Why this is / is not agent-owned: Function-specific positive and parent alternatives checked; names and extension points do not automatically supply organizational ownership.
- Evidence: [lib/super_pi/harness/planner.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/harness/planner.ex); [lib/super_pi/agy/brain.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/agy/brain.ex)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: planner/default/AGY presets, skill/plugin discovery, Brain configuration, compaction and dynamic add_tools/handoff.
- Plausible first-party paths checked: internal plans, manually enabled plugins/skills, model configuration and tool discovery/control directives.
- Why no material first-party path remains: These alter present task context or install an already-selected configuration. No external prospective model/options development and adoption dialogue back into current capability is shipped, including a parent-governed mode.

## S5 — Policy and identity

- State: —
- Function: No supplied runtime policy/identity closure loop at this boundary.
- Disturbance / variety regulated: ultimate identity-policy tensions.
- Decisive decision or feedback right: No qualifying function-specific decisive right supplied.
- Decision owner: none established; developer/runtime/user task authority remains separate.
- Supporting / enforcement mechanisms: pi.agent/systemSections, AGY permissions/rules, CLI flags, session.configure and RPC ui.respond.
- Closure path: No qualifying function closure; inspected workspace/tool permission changes, instruction injection, generic human response storage and static identities remain support/local task paths.
- Why this is / is not agent-owned: Function-specific positive and parent alternatives checked; names and extension points do not automatically supply organizational ownership.
- Evidence: [lib/super_pi/agy/extensions/permissions.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/agy/extensions/permissions.ex); [lib/super_pi/rpc/server.ex](https://github.com/oleksandr/super-pi-beam/blob/03c6afd6d8250eaeb4ebca039290f95a9ab73227/lib/super_pi/rpc/server.ex)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: pi.agent/systemSections, AGY permissions/rules, CLI flags, session.configure and RPC ui.respond.
- Plausible first-party paths checked: workspace/tool permission changes, instruction injection, generic human response storage and static identities.
- Why no material first-party path remains: These express/enforce configuration and ordinary permissions. No identity/ultimate-policy issue is adjudicated by a legitimate ultimate authority and returned to govern operations; a ui.respond pending-value map is not that function.

## Distributed OSS parent arrangement

No parent-governed organizational S3/S4/S5 loop is established. Local user configuration and permissions do not establish identity authority; OSS maintainer governance is not borrowed into the runtime.

## Self-hosted and non-human modes

Local SQLite/gateway and configured PostgreSQL are supported source modes. Positive S1 is limited to the actual Gemini configured branch and proper conversation/tool configuration, not echo, generic injected test responders or every listed model alias. Positive S2 is same-node Local file access, not a distributed filesystem guarantee.

## Recursion

Conversation forks, task ownership and subagent job names are technical nesting. They do not establish autonomous viable children with their own complete regulatory environment/metasystem.

## Variety and escalation

Durable history/context preserves observations; tool errors, retry-after/backoff and extension continuation return into the conversation. Per-path serialization attenuates read-modify-write races, while sandbox/heap/timeout isolate local failures. Fixed restart limits, PubSub status and queue names are enforcement/observability, not whole-system organizational decision ownership.

## Evidence gaps

No live model or native Elixir suite was run; compatible Elixir was not available in the inspected CLI environment. Source tests were read, not reported as passing execution. Echo fallback, partially notification-only worker paths and the MCP startup mismatch limit which README claims are credited. File locks use Path.expand and a local Registry, not realpath or cross-node locking; stale full writes and semantic conflicts can remain. No concrete unresolved higher-function mode remains after reviewing hooks/presets/transport paths; generic future extensions are outside this assessment.
