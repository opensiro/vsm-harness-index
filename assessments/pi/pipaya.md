---
harness_id: pipaya
project_name: pipaya
repository: https://github.com/dohwi/pipaya
review_ref: dd5cdfd560c1499301a1f2fe4c07f9173a12d53a
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# pipaya

## Review boundary

- System in focus: One trusted self-hosted pipaya server, its connected operator clients and first-party persistent session/peer composition.
- Purpose and identity: Provide durable workspace agents usable across devices, with peer teamwork and extensible tools.
- Relevant environment: Server workspaces and OS commands, user-configured inference endpoints, clients, trusted installed extensions and optional MCP services.
- Standard-distribution boundary: Server runtime plus supported desktop/headless composition; Pi-core is an instantiated dependency. First-party built-in peer, helper, question, context and operator control surfaces are included; separately installed marketplace extensions are not.
- Credited operating / distribution surfaces: SessionManager, peer service/tools, app endpoints, SQLite persistence, built-in coding tools, subagent execution and normal client/API operator paths.
- Adjacent first-party surfaces excluded from ownership: Development/CI/tests, client UI workbench examples, server todo example and externally installed marketplace extensions do not supply autonomous organizational owners.
- First-party operating / deployment modes considered: Headless or desktop-bundled server; ordinary model-backed sessions; automatically offered peer tools unless disabled; configurable ephemeral helpers; authenticated human client/API supervision.
- Recursion level: One server's operational session organization; a helper or newly created session does not itself prove viable recursion.
- Reviewed revision: `dd5cdfd560c1499301a1f2fe4c07f9173a12d53a`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Bun/Fastify serves authenticated REST, SSE/WebSocket and persisted SQLite sessions. SessionManager constructs Pi Agent with first-party workspace tools, live instructions/skills, stored history and context transformations. Each session has prompt/steer/follow-up queues and bounded run guards. Built-in peer tools list/read/message, create, stop, close/reconfigure and answer other independently running sessions; watchers deliver one-shot finish/question reports. Disposable role-file helpers have isolated context and no peer/delegate/user-question powers. The operator client uses the same server session state through explicit control APIs. Extension hooks may alter tools/results but the repository says no server extensions ship; marketplace code is separate. The release updater compares a rolling tag, refuses dirty/busy cases and installs/restarts on request. [Server][R3], [sessions][R1], [peers][R5], [subagents][R8], [updates][R10].

## Operational model

Model-backed sessions own local task choices; peers may also exercise supplied cross-session current-control tools. The narrow peer reply/notification protocol attenuates documented reciprocal-message oscillation. Runtime counters and lifecycle enforcement remain support. Human operator control is a distinct S3 mode over the same server, not an inferred policy/identity function. Higher functions are not imported from Pi or external extensions.

## S1 — Operations

- State: A
- Function: Persistent model-backed workspace sessions perform coding/investigation tasks and can use disposable helpers.
- Disturbance / variety regulated: User requests, file/command results, provider faults, context pressure and delegated observations.
- Decisive decision or feedback right: Choose workspace tools, follow-up actions and final answers; choose whether to delegate or create a persistent peer.
- Decision owner: The configured session agent, composed by the first-party SessionManager around Pi Agent.
- Supporting / enforcement mechanisms: Pi inference/loop dependency, first-party tools, SQLite transcript/context state, queues, compaction, retry and limits.
- Closure path: Prompt → constructed Agent with owned tool definitions → selected calls → observations/persistence → further turns and final response.
- Boundary reachability: ensureLive creates Agent with the session's actual model, history, prompt and first-party tools. The packaged server and desktop-bundled server wire this composition directly.
- Why this is / is not agent-owned: The first-party product owns the concrete executable composition; Pi SDK is a dependency and does not donate uninstantiated higher functions. Without the session actor, server APIs and gates do not choose project work.
- Evidence: [Session construction and helper execution][R1], [tools][R2], [server distribution][R3], [manifest][R4].
- Basis: structural.
- Confidence: high.
- Caveats: No provider-backed E2E run or Pi-wide capability claim is made.


## S2 — Coordination

- State: A
- Function: The supplied peer protocol attenuates reciprocal reply/notification oscillation between independently running sessions.
- Disturbance / variety regulated: Two peer sessions can repeatedly reply to one another or cause completion notifications to trigger further replies.
- Decisive decision or feedback right: The receiving agent decides whether a peer response is needed and whether to end that exchange; the sender chooses explicit reply/notification requests.
- Decision owner: The participating session agents own semantic response necessity; runtime-authored notification and send bounds constrain the exchange.
- Supporting / enforcement mechanisms: peerMessage marks other-session origin and says to reply only if needed; completion watches are consumed once, reports say no reply needed, and per-run send overflow returns stop/report feedback.
- Closure path: Peer message or one-shot completion report → recipient agent sees explicit reply/termination semantics → chooses further peer_send only when needed, or stops; cap refusal feeds back to the sender's next action.
- Boundary reachability: Peer tools are automatically included in normal session tool plans unless the operator disables them. PeerService wraps actual delivered messages and sends report feedback into prompt/follow_up paths of ordinary agents.
- Why this is / is not agent-owned: The narrow credited discretion is agent choice over necessary replies under a first-party anti-oscillation protocol. The generic mailbox, layout groups and delegation are not themselves the S2 witness, and the counter is not an autonomous owner.
- Evidence: [Peer templates, send counter and one-shot watchers][R5], [tool descriptions][R2], [always-reachable peer tool wiring][R1], [tool plan][R6].
- Basis: structural.
- Confidence: medium.
- Caveats: This is bounded structural attenuation, not proof that arbitrary agent conversations terminate. The counter resets each run and cannot alone rule out cross-run ping-pong or shared-file collisions.

- Distinct S1 units: Independent persistent session agents addressed by distinct peer names.
- Inter-S1 disturbance: Reciprocal peer replies or notification-triggered replies can keep otherwise completed work alive.
- Attenuating coordination relation: Explicit reply-only-when-needed agent protocol plus consumed-once completion watchers and bounded send/refusal feedback.
- Feedback into subsequent S1 behaviour: The recipient receives origin/response instructions and no-reply completion notices; the sender receives overflow stop/report errors and busy/queued delivery state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The credited path specifically targets reply/notification oscillation; ordinary transport or group membership is not credited.


## S3 — Inside-and-now control

- State: A(P)
- Function: A session agent can regulate current commitments across peer sessions, and the local human operator has a distinct supplied supervisory mode.
- Disturbance / variety regulated: Peers are stuck, working on the wrong course, waiting on questions, or consuming the wrong model/active-session capacity.
- Decisive decision or feedback right: Inspect all peer state, steer/abort work, create/close/resume sessions, withdraw queued work, change model/effort and answer blocked questions; in parent mode the operator makes those current-control choices through the server/client API.
- Decision owner: Base mode: a model-backed session acting as peer supervisor. Parent mode: the local server operator using the administrator-authority client/API.
- Supporting / enforcement mechanisms: peer_list/read/current watcher notifications, peer_send steer/follow_up, peer_abort/manage/create/answer, persisted session state and authenticated REST/WebSocket interfaces.
- Closure path: Current peer view/report → agent or operator selects intervention → SessionManager applies queue/run/model/lifecycle/question changes → subsequent peer execution follows the changed current commitment.
- Boundary reachability: Every normal session receives the first-party peer tools, wired to SessionManager host methods, unless disabled. The client/API exposes server-wide activity/session/status/usage and actual abort/message/patch/question endpoints for its operator.
- Why this is / is not agent-owned: Removing the supervisory actor leaves APIs, messages and limits but no discretionary selection of whom to stop, steer, resume or reconfigure. Parent control is evidenced separately from generic ask_user approval.
- Evidence: [Peer state/intervention methods][R5], [specific tool semantics][R2], [SessionManager host wiring][R1], [authenticated operator routes][R7], [server API contract][R3].
- Basis: structural.
- Confidence: high.
- Caveats: Authority is broad among sessions of one trusted server; this is neither a global organizational claim nor evidence that every run uses a supervisor.

- Whole-system current view: peer_list exposes all other open sessions with working/idle/archive state, title, branch and directory; peer_read adds current questions and recent operations; watches return completion/question changes. The operator has activity, session, status and usage views across the same server.
- Current-control decision scope: Current peer commitments, interruption/steering, queued-message withdrawal, capacity/session lifecycle, model/effort and blocked-question resolution.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Session agent using the built-in peer supervisor tools | Peer report/list/read reveals stuck, misdirected or blocked current work | Agent selects steer/abort/manage/create/answer; SessionManager changes subsequent peer operation | [PeerService][R5], [tools][R2], [host wiring][R1] |
| Parent (`P`) | Local server administrator/operator | Activity/status/usage and user-observed current commitments require intervention | Operator API/client message/abort/patch/answer changes the same live sessions | [Application routes][R7], [server API][R3] |


## S3* — Complementary audit

- State: —
- Function: No shipped audit-specific independent challenge-and-corrective-control loop is established.
- Disturbance / variety regulated: A peer or helper may make an incorrect completion claim.
- Decisive decision or feedback right: No supplied audit role/verdict/return protocol decides that claim independently.
- Decision owner: Ordinary producing sessions report their work. Helper role files and extension logic are user supplied.
- Supporting / enforcement mechanisms: peer_read can inspect ordinary transcript/tool snippets; workspace read/grep and generic helpers are available; event/context/read tracing preserve evidence.
- Closure path: Peer/helper output returns as ordinary tool text or messages, without an audit-specific independently controlled adjudication and corrective path.
- Why this is / is not agent-owned: A fresh helper context and raw file tools can be used to build a reviewer, but the shipped delegate interface itself is generic operational delegation. No bundled reviewer is credited from an external marketplace.
- Evidence: [Helper definition/execution][R8], [session delegate][R1], [peer read][R5], [extension boundary][R9].
- Basis: structural.
- Confidence: high.
- Caveats: Users can create a material complementary audit application; it needs its own independent owner, evidence-access and corrective-return proof.

### Absence scope

- Surfaces inspected: server/src sessions/peers/tools/tool-plan/subagents/questions/run-guard/context/skills/compaction/self-update, app/configuration routes and extension host/types; root and server README, built-in usage/extension skills, bundled example/test surfaces
- Plausible first-party paths checked: Checked default/read-only subagents, role loading, peer transcript access, completion watcher messages, tool-result hooks, read-file tracing and bundled skills/extensions for a first-party audit-specific judgment and corrective protocol.
- Why no material first-party path remains: These are general operational, observational and extension surfaces. The distribution ships no reviewer/evaluator actor or audit-specific constructor loop; marketplace and user-authored extensions are external.


## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation loop is supplied.
- Disturbance / variety regulated: Provider configuration, new skills/extensions, changing instructions and available upstream releases.
- Decisive decision or feedback right: No first-party intelligence path develops future-relevant options and negotiates a return into current capability.
- Decision owner: Users configure endpoints/extensions/skills and request updates; sessions perform requested present tasks.
- Supporting / enforcement mechanisms: AGENTS.md/skill refresh, compaction, provider settings, extension APIs and release-tag updater.
- Closure path: Settings apply next run; updater installs the latest release after operator request and running-session checks. No prospective environment model/adaptation-option decision loop is wired.
- Why this is / is not agent-owned: A latest-tag inequality check and package restart are maintenance, not external/future adaptation judgment. General capability extension and compaction are not S4; no parent adaptation mode is inferred from update consent.
- Evidence: [Source update policy][R10], [live context/skills][R11], [SessionManager][R1], [extension skill boundary][R9].
- Basis: structural.
- Confidence: high.
- Caveats: The assessment does not claim that users cannot organize an adaptive workflow on this product.

### Absence scope

- Surfaces inspected: server/src sessions/peers/tools/tool-plan/subagents/questions/run-guard/context/skills/compaction/self-update, app/configuration routes and extension host/types; root and server README, built-in usage/extension skills, bundled example/test surfaces
- Plausible first-party paths checked: Inspected built-in configuration/extension-authoring skills, self-update status/apply/rollback, endpoint/model settings, session purpose/title generation, skills/instruction reload and context summarization.
- Why no material first-party path remains: The shipped paths are current configuration, user-directed construction, memory/context management or release maintenance; no external-and-prospective option-to-current-capability loop remains.


## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy adjudication-and-return loop is supplied.
- Disturbance / variety regulated: Session instructions, permissions, enabled skills/tools and broad server administrator control.
- Decisive decision or feedback right: No identity-level issue is routed to ultimate authority and returned as an authoritative system policy decision.
- Decision owner: Users author prompts/settings; trusted extensions run with server privileges; agents can change bounded peer metadata/current work.
- Supporting / enforcement mechanisms: Authentication token, frozen initial tool/base-prompt snapshot, live AGENTS/skill settings, extension approval and per-tool enforcement.
- Closure path: Settings constrain subsequent calls, and ask_user/peer_answer returns ordinary question answers. Those are not a supplied identity-policy adjudication protocol.
- Why this is / is not agent-owned: A field named purpose, a user answer and administrator control are not S5 without a function-specific ultimate-policy issue and governing return.
- Evidence: [Context and instruction boundary][R11], [session controls][R1], [question lifecycle][R12], [operator API][R7], [peer metadata][R5].
- Basis: structural.
- Confidence: high.
- Caveats: The S3 parent mode is not reused as S5 evidence; external extension policy does not enter the first-party default boundary.

### Absence scope

- Surfaces inspected: server/src sessions/peers/tools/tool-plan/subagents/questions/run-guard/context/skills/compaction/self-update, app/configuration routes and extension host/types; root and server README, built-in usage/extension skills, bundled example/test surfaces
- Plausible first-party paths checked: Inspected AGENTS.md/skill refresh, fixed session base prompt/tools, peer purpose changes, user questions, admin-token authority and extension policy hooks for identity-level issue/decision/return closure.
- Why no material first-party path remains: Only generic configuration/communications and operational authority remain; no supplied identity/ultimate-policy loop or S3–S4 tension resolver is established.


## Distributed OSS parent arrangement

MIT licensing and public contributors do not create a project-level parent VSM organization. The parent S3 mode is local to the trusted server operator; no contributor-governance loop is transferred to the installed product.

## Self-hosted and non-human modes

The server token is administrator authority; peer tools are automatically added but globally disableable. The client/API supplies reconstructable current supervision over all local sessions. Arbitrary external extensions and their independent policies are not part of the credited default mode.

## Recursion

Peer sessions and one-shot helpers are technical agent compositions. No complete local metasystem is established for each child, and groups are UI/addressing structures.

## Variety and escalation

Summaries, hint/transcript caps, tool schemas, send/helper limits and context compaction attenuate variety. File/shell/MCP and extension surfaces amplify operational repertoire. One-shot watcher feedback and explicit reply necessity reduce peer chatter. Notifications/questions carry ordinary exception information; they are not automatically algedonic channels.

## Evidence gaps

Pinned-source assessment; no real provider, desktop, security, or multi-agent E2E execution. S2 is a narrow structural reply/notification attenuation claim, not guaranteed termination or file-lock protection. S3 covers one trusted server with broad peer authority. Marketplace extensions, Pi-wide features and user-created reviewer/adaptation applications are excluded.

[R1]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/sessions.ts
[R2]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/tools.ts
[R3]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/README.md
[R4]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/package.json
[R5]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/peers.ts
[R6]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/tool-plan.ts
[R7]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/app.ts
[R8]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/subagents.ts
[R9]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/builtin-skills/pipaya-server-extensions/SKILL.md
[R10]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/self-update.ts
[R11]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/context.ts
[R12]: https://github.com/dohwi/pipaya/blob/dd5cdfd560c1499301a1f2fe4c07f9173a12d53a/server/src/questions.ts
