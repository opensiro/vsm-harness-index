---
harness_id: ferrum
project_name: Ferrum
repository: https://github.com/ominiverdi/ferrum
review_ref: f31151d34fade3ef88104a33ba2a4042e689be35
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ferrum

## Review boundary

- System in focus: the first-party `ominiverdi/ferrum` Rust-native coding-agent distribution at frozen revision `f31151d34fade3ef88104a33ba2a4042e689be35`, including its model/tool agent loop, native coding tools, session/history/compaction machinery, safety/tool policy, MCP bridge, interactive/print execution and one active ACP agent session where they bear on organizational function.
- Purpose and identity: perform software-engineering work in a selected project workspace by letting one model-backed coding actor inspect repository/environment evidence, execute bounded file/shell/tool actions, observe results and continue until it can return an answer or the runtime terminates the turn.
- Relevant environment: the selected project workspace and project instructions, user task, file and shell state, provider/model responses, configured MCP services, user/global/project policy, durable session history and optional ACP client interaction.
- Standard-distribution boundary: the shipped `ferrum` CLI/interactive/print runtime, core agent loop, first-party native tools, session JSONL/history/compaction surfaces, safety/config enforcement, MCP stdio integration and the official `ferrum acp` per-session runtime are inside. External provider inference, MCP servers, ACP clients/editors, host Linux, target-project governance and external repositories/web resources are dependencies/environment rather than Ferrum organizational decision owners.
- Credited operating / distribution surfaces: `README.md`; `docs/spec.md`; `docs/tools.md`; `docs/acp.md`; `docs/sessions.md`; `docs/security.md`; `src/agent/*`; first-party tool/config/session/ACP surfaces directly reached by supported user runs.
- Adjacent first-party surfaces excluded from ownership: `bench/` benchmark tasks/validators; repository tests/CI/release machinery; contributor/development governance; roadmap/research notes; and `docs/background-tasks.md`, which explicitly declares itself a deferred exploratory design note rather than implemented runtime behavior.
- First-party operating / deployment modes considered: interactive coding, print/headless prompts, named/resumed sessions, ACP v1 sessions, context compaction/history recovery, native/MCP tool use, foreground `wait` monitoring and supported project/user policy modes.
- Recursion level: one Ferrum coding organization is one active agent session around one task/workspace. Safe read-only tool calls executed concurrently are actions of that S1, not distinct S1 units. An ACP process may host multiple independent Ferrum sessions concurrently, but each session owns an independent agent session/canonical cwd and is treated as another instance at this recursion rather than as a subordinate S1 inside one selected organization.
- Reviewed revision: `f31151d34fade3ef88104a33ba2a4042e689be35`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Ferrum is a compact Rust coding agent whose documented core loop constructs context from runtime/system/project instructions, session history, user input and active tool definitions; calls the selected provider; executes requested tools in the core loop; appends tool results; and repeats until the model returns no tool calls or loop policy ends the turn. Provider adapters translate provider protocol only and do not own tool execution.

The standard native tools cover reads/search, bounded file write/edit, guarded bash/wait execution and current-session history lookup. Safe batches containing only `read`, `ls`, `grep` and `find` may execute concurrently, but their results are returned in model-requested order. Mutating, shell, wait and MCP calls stay sequential. This parallelism therefore increases one S1 actor's tool throughput; the reviewed standard session does not create distinct model-backed operational units that must coordinate with one another.

Ferrum's adaptive loop guard observes repeated identical tool calls, consecutive tool errors and a hard safety ceiling. It can inject transient guidance into the next request and, if the behavior continues, perform one final no-tools request for findings/next steps. This is deterministic execution-loop protection around the same S1 rather than a separate whole-organization S3 decision owner.

Sessions are durable JSONL and support resume, history search/read and model-assisted context compaction. Compaction summarizes older conversation so the same operational actor can continue under a context budget; it does not alter Ferrum's organizational capabilities or strategy. Project `.ferrum/config.toml` may only narrow safety, tools, roots, skills, MCP and tool-round limits; provider/model/auth and broader authority remain user/global or CLI owned.

The official ACP adapter can host multiple active sessions and bounds concurrent turns. Its documentation states that every active ACP session owns an independent Ferrum agent session and canonical absolute working directory. The assessment therefore does not collapse co-resident ACP sessions into one multi-S1 organization. Optional ACP permission UX can only further restrict operations Ferrum has already authorized; client approval cannot add authority.

`bench/` and related validation artifacts are project-development/evaluation surfaces rather than a standard runtime audit role. The background-task design note is also explicitly non-implemented and says current Ferrum uses foreground `wait` rather than a durable model-owned background task abstraction.

Primary evidence:

- [`README.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/README.md)
- [`docs/spec.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/spec.md)
- [`docs/tools.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/tools.md)
- [`docs/acp.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/acp.md)
- [`docs/background-tasks.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/background-tasks.md)
- [`src/agent/`](https://github.com/ominiverdi/ferrum/tree/f31151d34fade3ef88104a33ba2a4042e689be35/src/agent)

## Operational model

A supported Ferrum turn receives a user task plus current project/session context. The model-backed actor chooses a native or configured MCP tool, Ferrum executes or rejects that request under first-party policy, and the tool result returns into the conversation for the next provider request. The actor can iteratively read/search/edit/run commands and reason over results until it produces a final response.

Session/history, context compaction, loop guard, cancellation, safety tiers, writable roots and tool allow/deny policy support this S1 closure. They do not create additional autonomous organizational decision owners by themselves.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work on the selected workspace by interpreting the task, inspecting project evidence, selecting coding/tool actions, applying or running them and reacting to returned results.
- Disturbance / variety regulated: heterogeneous source trees and project instructions, incomplete task information, file contents, search/command output, tool failures, changing workspace state and implementation choices encountered while completing coding work.
- Decisive decision or feedback right: decide what project evidence to inspect, which exposed coding action/tool to invoke next, what modifications or commands to attempt, and when enough work/evidence exists to produce the final response within externally selected policy limits.
- Decision owner: the model-backed coding actor instantiated by Ferrum's standard agent loop.
- Supporting / enforcement mechanisms: runtime/system/project context construction; native/MCP tool registry; provider adapters; safety/tool/root policy; durable session/history; compaction; loop guard; cancellation; interactive/print/ACP transport.
- Closure path: user task/workspace context → provider request → model selects tool/action → Ferrum executes or rejects the action → tool/environment result is appended to the session context → the same model-backed actor receives the result and selects the next action or terminates.
- Boundary reachability: `ferrum`, `ferrum -p` and each supported ACP session directly instantiate the first-party agent/tool loop; no application-authored orchestration layer is needed to reach the coding actor.
- Why this is / is not agent-owned: removing the model-backed actor while retaining tools, policies and session machinery removes the open-ended coding judgment that selects and sequences repository-facing work.
- Evidence: [`docs/spec.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/spec.md); [`docs/tools.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/tools.md); [`README.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model inference remains an external dependency; Ferrum is credited for the shipped role/tool/feedback composition, not provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established at S2 level because one active Ferrum agent session exposes one primary model-backed S1 rather than multiple distinct S1 operational units with a concrete mutual interference/oscillation relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: safe read-only tool batches may execute concurrently; mutating/mixed/MCP batches stay sequential; ACP can host multiple independent sessions; session persistence uses file locking. These are execution/session mechanisms rather than a demonstrated coordination relation among S1 units inside one organization.
- Closure path: not applicable; no distinct-S1 disturbance → attenuation → changed subsequent S1 behavior loop exists in the reviewed standard session.
- Why this is / is not agent-owned: parallel `read`/`ls`/`grep`/`find` calls are tools chosen by the same coding actor. Concurrent ACP sessions are documented as independent agent sessions, so their co-residence in one server process does not create subordinate S1s at the selected session recursion.
- Evidence: [`docs/tools.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/tools.md); [`docs/acp.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/acp.md); [`docs/spec.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/spec.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: this classification is recursion-sensitive; a separately defined external organization composed from several Ferrum ACP sessions could require a different assessment, but Ferrum does not supply that organization at the reviewed boundary.

### Absence scope

- Surfaces inspected: documented core agent loop; native tool execution/parallel-batch policy; source `src/agent/` surface; interactive/print modes; ACP session/concurrency semantics; session persistence/history; MCP integration; background-task design note.
- Plausible first-party paths checked: subagent/delegation/team APIs; concurrent model-backed workers inside one session; parallel tool calls; ACP concurrent sessions; shared session/history state; background workers/tasks; MCP peers.
- Why no material first-party path remains: no standard subagent/team/delegation actor was found; parallelism inside one session is limited to safe tool execution for one S1, while ACP explicitly owns independent sessions. Generic MCP/tool/session mechanisms do not supply an S2-specific interference attenuation relation.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-control function distinct from the coding S1 and deterministic loop/runtime safeguards was established.
- Disturbance / variety regulated: not established at S3 ownership level.
- Decisive decision or feedback right: not established. The adaptive loop guard can detect repeated calls/errors and alter the next request, while cancellation, tool-round limits and policy can stop/limit work; these mechanisms regulate one S1's execution according to encoded/operator policy rather than manage current commitments/resources across an organization of S1 units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: adaptive loop guard; optional `max_tool_rounds`; cancellation; safety tiers; tool/root policy; session/ACP active-turn limits; foreground `wait` bounds.
- Closure path: not applicable; no whole-organization current view plus substantive resource/priority/commitment/accountability intervention path was found.
- Why this is / is not agent-owned: the loop guard's response is deterministic runtime policy and survives conceptually without an autonomous management actor; model action after guard guidance remains the same S1's operational continuation rather than S3 management.
- Evidence: [`docs/tools.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/tools.md); [`docs/spec.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/spec.md); [`docs/acp.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/acp.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: strong lifecycle/safety enforcement is not denied; it does not meet the Profile's stronger S3 organizational-control threshold at this recursion.

### Absence scope

- Surfaces inspected: loop guard and tool-round behavior; cancellation; safety/config policy; active-turn/session controls in ACP; foreground wait/command lifecycle; session context/goal metadata; standard agent loop.
- Plausible first-party paths checked: runtime supervision; current progress/error feedback; adaptive loop guard; user cancellation; resource ceilings; ACP active-turn concurrency; session-scoped goal; current policy changes.
- Why no material first-party path remains: all located current-control mechanisms govern one operational loop or enforce predetermined/operator constraints. No first-party actor receives a whole-system view of multiple relevant current operations and owns substantive organization-wide reallocation/commitment decisions.

## S3* — Complementary audit

- State: —
- Function: no material complementary audit role with sufficiently independent access, audit judgment and corrective return into the supported runtime was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. Ferrum can run tests/commands as normal S1 tools and its repository includes benchmark validators, but the standard coding distribution does not wire a separate reviewer/judge actor to challenge S1 conclusions and return an audit verdict into current control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ordinary `bash`/tool verification, deterministic safety validation and repository `bench/` task validators are operation/development evidence rather than an independent runtime audit owner.
- Closure path: not applicable; no supported independent challenge → audit judgment → corrective-control return path was found.
- Why this is / is not agent-owned: a coding model may choose to run tests or inspect its own work, but that remains S1 self-checking. Repository benchmark scripts are adjacent project-development evaluation and are not boundary-reachable decision owners in ordinary Ferrum sessions.
- Evidence: [`README.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/README.md); [`docs/tools.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/tools.md); [`bench/`](https://github.com/ominiverdi/ferrum/tree/f31151d34fade3ef88104a33ba2a4042e689be35/bench).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: deterministic validation and self-verification can materially improve quality without satisfying S3* independence.

### Absence scope

- Surfaces inspected: native coding/test/shell tools; core loop; benchmark tasks/validators; source/test tree; ACP client permission path; session history/performance/usage surfaces; roadmap/docs searches for verifier/reviewer/judge roles.
- Plausible first-party paths checked: separate reviewer agent; benchmark/evaluator feedback; test/command verification; client permission review; independent ACP session acting as reviewer; post-turn diagnostics/metrics.
- Why no material first-party path remains: no audit-specific runtime actor/path is packaged into one assessed Ferrum organization, and development benchmark validators do not feed a separate judgment back into ordinary runtime control.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party prospective environment-intelligence and organizational adaptation loop was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Ferrum can load current project instructions/skills, consult session history, use MCP/tools and summarize old context, but these mechanisms support the present coding operation rather than model future environmental change and persistently alter Ferrum's organizational capability/strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: AGENTS/context files; skills; MCP; history search/read; durable sessions; context compaction; user/provider/model configuration; foreground `wait` monitoring.
- Closure path: not applicable; no prospective scan → adaptation-option formation → persistent capability/strategy change → later operation loop was found.
- Why this is / is not agent-owned: compaction changes the representation of current conversation history, and history/skills expose information to S1. The separate background-task document explicitly states that durable/model-owned background tasks are deferred exploration rather than implemented behavior.
- Evidence: [`docs/spec.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/spec.md); [`docs/tools.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/tools.md); [`docs/background-tasks.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/background-tasks.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: present-task learning/replanning and persistent conversational state are not sufficient S4 evidence under Profile 0.2.4.

### Absence scope

- Surfaces inspected: context/project instruction loading; skills; MCP; session history and compaction; provider/model selection; foreground wait/monitoring; background-task design note; roadmap/spec; benchmark/development surfaces.
- Plausible first-party paths checked: external/prospective research; durable monitoring; autonomous background tasks; session learning; self-update/evolution; model/provider adaptation; skill/capability changes driven by observed future conditions.
- Why no material first-party path remains: current features either expose operator-selected capabilities/information or preserve current-session continuity. The only explicit durable autonomous/background direction is documented as deferred and not implemented, so no standard prospective adaptation closure exists.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy closure was established.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. User/global/project configuration chooses provider/model, system prompt, safety, tool/root/MCP/skill limits and the task itself; project policy may narrow authority but cannot autonomously redefine Ferrum's identity/purpose.
- Decision owner: not established inside the assessed organization; ultimate purpose/policy remains developer/operator/project-config owned.
- Supporting / enforcement mechanisms: safety tiers; `[tools]` allow/deny and writable roots; project restrictive policy; system prompt override; ACP optional permission UX; credential/protected-target guards; cancellation and tool limits.
- Closure path: not applicable; no identity/ultimate-policy proposal/dispute reaches an autonomous or qualifying parent S5 decision path and returns as an authoritative policy change to later operation.
- Why this is / is not agent-owned: the runtime strongly enforces selected limits, but enforcement is distinct from ownership. ACP client permission can only restrict an operation Ferrum already authorizes and is ordinary operational approval, not an identity-level parent governance loop.
- Evidence: [`README.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/README.md); [`docs/spec.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/spec.md); [`docs/acp.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/acp.md); [`docs/tools.md`](https://github.com/ominiverdi/ferrum/blob/f31151d34fade3ef88104a33ba2a4042e689be35/docs/tools.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: restrictive project policy and client permissions are important governance/safety boundaries, but generic configuration/approval does not satisfy S5 identity closure.

### Absence scope

- Surfaces inspected: user/global/project config; system prompt override; safety/tool/root policy; ACP permission UX; credential/protected-target controls; session goal metadata; model/provider selection; roadmap/spec and standard runtime modes.
- Plausible first-party paths checked: agent-authored policy revision; parent approval/escalation; identity/purpose change; project-policy return; ACP client governance; autonomous policy selection; persistent governance decisions.
- Why no material first-party path remains: authoritative values are supplied externally and the agent operates beneath them. No first-party ultimate-policy decision loop exists; ordinary permissions/configuration cannot be promoted to S5.

## Assessment summary

Ferrum closes a clear autonomous coding S1 through its shipped provider/tool feedback loop. Its execution safeguards, durable sessions, adaptive loop guard, compaction, restrictive policy and ACP transport improve one operational actor's reliability but do not create additional VSM functions at the selected session recursion. Safe tool parallelism is intra-S1, ACP sessions are independent organization instances, benchmark validation is adjacent development infrastructure, background autonomy is explicitly deferred, and ultimate policy remains externally configured.

Proposed vector: **`A · — · — · — · — · —`**.
