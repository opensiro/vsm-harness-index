---
harness_id: openharness
project_name: OpenHarness
repository: https://github.com/autonomous-ai/openharness
review_ref: ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: —
---

# OpenHarness

## Review boundary

- System in focus: one OpenHarness installation at pinned revision `ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85`, including the first-party desktop app, daemon/CLI, durable session registry, local/remote control protocol, multi-machine transport, DSH package/install/update protocol, live Store/catalog integration and built-in first-party DSH packages as supported operating modes.
- Purpose and identity: keep coding-agent sessions durable and reachable across the user's machines, let a person direct and supervise many concurrent agent sessions, and extend those sessions with domain-specific instructions, toolchains, checks and live viewers without replacing the underlying agent engines.
- Relevant environment: installation owner/operator, local and remote machines, repositories and workspaces, external Claude/Codex/Cursor/OpenCode/Pi/Hermes/etc. agent engines, domain toolchains, external/community package repositories, the published Store catalog, relay/network conditions and the application domains in which agent sessions produce artifacts.
- Standard-distribution boundary: OpenHarness-owned desktop/daemon/CLI/backend code, session registry and control frames, tmux lifecycle, remote transport, Store/DSH protocol, bundled Store packages and package-management paths. External agent CLI/model internals remain separate agent actors and do not donate their internal organizational functions. The hosted web client is documented but not sourced in this repository, so its undocumented internals are not credited.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `docs/app.md`; `docs/cli.md`; `docs/extending.md`; `store/README.md`; `store/spec/README.md`; bundled DSH manifests/instructions such as `store/agents/marp/AGENTS.md`; daemon/local-WebSocket control surfaces reached by those documented modes.
- Adjacent first-party surfaces excluded from ownership: repository-development handoffs under `HANDOFF.md` and `work/`; CI/release/catalog-publishing jobs; maintainer acceptance/release evidence; provider conformance fixtures and tests; repository governance/contributor activity. Built-in DSH internal sub-agent structures such as Roundtable seats are treated as lower-recursion organization inside one session rather than as installation-level S1 peers unless the top-level OpenHarness control relation itself reaches them.
- First-party operating / deployment modes considered: desktop-managed local sessions, headless daemon sessions, linked remote machines, optional Harness-device control, installed built-in/community DSH sessions, Store-driven install/update, and the documented local automation WebSocket.
- Recursion level: the OpenHarness installation is the system-in-focus. Individual durable agent/DSH sessions are installation-level S1 units. A DSH may itself contain a lower-recursion organization (for example Roundtable's moderator and vendor seats), but lower-recursion S2/S3/S3* relations are not promoted into the installation-level vector.
- Reviewed revision: `ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

OpenHarness is a control and workspace layer around vendor-native coding agents rather than a replacement reasoning runtime. The documented architecture is desktop app → daemon → tmux → Claude/Codex/etc. The daemon owns only panes it created, persists a registry containing engine, working directory, pane, transcript and process identity, reconciles those sessions every five seconds, restores panes after tmux/reboot loss, normalizes vendor transcript/hooks into session events, and carries the same control frames across linked machines.

The desktop/app layer can hold any number of panes from any mix of machines. It creates sessions, lists/searches harnesses, projects and machines, surfaces agents waiting for a human answer, and can stop or restart sessions. The optional device exposes an installation-wide agent list with current state/recap, focus selection, prompt dispatch, stop and question-answer operations. The local WebSocket intentionally exposes the same family of agent lifecycle/control operations to other programs on the machine.

Domain-specific harnesses are separately installable first-party packages. A DSH selects a base engine and may materialize workspace templates, agent instructions/skills, a pinned toolchain, a checker/verdict feed and a live viewer. The repository explicitly states that the agent does the reasoning while the harness supplies the tools and view. Store/catalog state can change independently of an app/CLI release; the CLI can discover, install and update packages, and installed instructions/toolchains/viewers become part of subsequent session capability.

Some built-in DSHs contain richer organization. Roundtable, for example, instructs a moderator agent to seat multiple vendor agents, seal their opening rounds to prevent convergence, cross-examine claims and preserve dissent. That is evidence of a real nested organizational form, but its vendor seats live inside one DSH session's purpose. This assessment therefore records it under recursion rather than using that child-level structure to manufacture installation-level S2 or S3*.

## Operational model

The operator chooses a machine, working directory and engine or DSH, then OpenHarness creates a durable tmux-backed session. The launched vendor agent owns substantive reasoning and tool/action choices for that session. OpenHarness keeps the process/session reachable, reattaches or restores it when possible, normalizes current state, transports input/output and equips DSH sessions with first-party package instructions and domain tooling.

At installation level, the human is the only first-party decisive owner demonstrated for closed current supervision: the app/device presents current sessions and attention state, while stop/restart/focus/message/question operations return that decision into the chosen running session. Separately, OpenHarness exposes a deliberate current-control constructor surface: a local automation client can list agents and invoke create/restart/retarget/delete/update/message/cancel operations, but the distribution does not package an autonomous installation-level supervisor that decides those interventions. That split supports `S3=C(P)` rather than `A`.

Future capability adaptation has the same ownership pattern. The live Store/catalog and DSH package manager expose concrete capability options and install/update/remove paths, but no first-party installation-level agent autonomously decides which external/community capability to adopt. A human can close the loop by choosing a package/update and returning it into present capability; the dedicated DSH management primitives also form a constructor path for a downstream autonomous adopter. That supports `S4=C(P)`.

## S1 — Operations

- State: A
- Function: execute user-directed coding/domain work inside durable agent sessions and produce artifacts, analyses, designs, data, code or other domain outcomes in the selected workspace.
- Disturbance / variety regulated: heterogeneous user objectives, repository/workspace state, domain-tool behavior, remote-machine conditions, tool results and iterative artifact feedback.
- Decisive decision or feedback right: choose the substantive sequence of reasoning, tool use, file edits, commands and task-specific responses needed to satisfy the admitted objective inside a running session.
- Decision owner: the launched vendor model/agent actor (Claude Code, Codex, OpenCode, Pi, Hermes or another supported engine) operating through the OpenHarness-created session.
- Supporting / enforcement mechanisms: daemon-owned tmux pane/session lifecycle, durable registry, transcript/hook normalization, remote transport, DSH instructions/skills, pinned toolchains, workspace materialization, viewers and verdict feeds.
- Closure path: operator supplies objective → OpenHarness starts/reaches the selected agent session with workspace/DSH context → agent chooses and executes work → artifacts/terminal events/verdict/viewer state are returned through OpenHarness → user or subsequent session work consumes the result.
- Boundary reachability: the standard desktop/daemon flow directly launches the supported vendor engine, binds it to an OpenHarness-owned session and workspace, and returns its output through first-party session/control surfaces. The reasoning engine is external, but the autonomous actor is reached by the shipped OpenHarness operating mode rather than borrowed from an adjacent development system.
- Why this is / is not agent-owned: the daemon decides lifecycle transitions and transports input/output, but the material operational choices within an admitted task are made by the model actor. README and DSH documentation explicitly separate these roles: the agent reasons; the harness supplies tools and view.
- Evidence: [`README.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/README.md); [`docs/architecture.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/architecture.md); [`store/spec/README.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/store/spec/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: OpenHarness does not own the vendor model's internal reasoning loop; `A` credits autonomous operational ownership made reachable by OpenHarness's standard distribution, not vendor internals as first-party OpenHarness code.

## S2 — Coordination

- State: —
- Function: no installation-level S2 function is established from the reviewed evidence.
- Disturbance / variety regulated: the installation can host many concurrent sessions, but the reviewed top-level surfaces do not identify a specific inter-session interference/conflict/oscillation together with a first-party coordination relation that attenuates it.
- Decisive decision or feedback right: not established at installation recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: tmux/session isolation, pane layouts, remote transport, receipts/idempotency, focus targeting, registries and shared viewers support coexistence/transport but are not credited as S2 without a concrete inter-S1 disturbance relation.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no installation-level S2 organizational path is established, so no ownership state is assigned.
- Evidence: [`docs/app.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/app.md); [`docs/architecture.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/architecture.md); [`docs/cli.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/cli.md); [`store/agents/roundtable/AGENTS.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/store/agents/roundtable/AGENTS.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: Roundtable does contain a concrete lower-recursion coordination relation: sealed openings prevent vendor-seat convergence before cross-examination. Those seats are internal to one DSH work cell, not installation-level S1 peers, so that child-recursion witness is not promoted into this vector.

### Absence scope

- Surfaces inspected: installation architecture/session registry; app multi-pane/multi-machine controls; local automation protocol; remote/device targeting and receipts; DSH package/viewer/verdict protocol; representative built-in DSH organization including Roundtable.
- Plausible first-party paths checked: session layouts and tmux isolation, machine/session routing, focus and message targeting, shared viewers, duplicate-request receipts, DSH-level multi-agent protocols.
- Why no material first-party path remains: top-level primitives move, isolate, display or address sessions but the evidence does not tie them to regulation of a specific interaction-generated disturbance among installation-level S1 sessions. The one clear anti-convergence relation found is at Roundtable's lower recursion.

## S3 — Inside-and-now control

- State: C(P)
- Function: provide an installation-wide current-control surface over active agent sessions so current session commitments/processes can be inspected and intervened in across machines.
- Disturbance / variety regulated: agents can be running, idle, waiting for questions, attached to the wrong target, stale after process/tmux loss, or in need of restart/retarget/cancel/stop while other sessions continue operating.
- Decisive decision or feedback right: choose which current session to create, stop, restart, retarget, update, cancel, message or answer, and thereby change the installation's current operational allocation/attention state.
- Decision owner: constructor mode — not supplied; a downstream autonomous controller must be composed over the first-party automation/control protocol. Parent mode — the installation owner/operator using app/device controls.
- Supporting / enforcement mechanisms: daemon registry and reconciliation, `agents_list`, `agent_create`, `agent_restart`, `agent_retarget`, `agent_delete`, `agent_update`, `message`, `cancel`, question/attention state, focus revisions, tmux process lifecycle and remote encrypted transport.
- Closure path: installation-wide session state is exposed → controller/operator chooses an intervention → first-party control frame reaches the owning daemon/session → session process/target/message/turn state changes → subsequent current operation reflects the intervention.
- Boundary reachability: the parent path is standard app/device operation, and the constructor path is the documented loopback WebSocket/daemon control surface shipped with OpenHarness. No repository-development bot or CI actor is required.
- Why this is / is not agent-owned: OpenHarness supplies whole-installation current state and specific intervention primitives but no standard-distribution autonomous installation-level actor that decides among them. Deterministic daemon reconciliation can restore missing panes, but that lifecycle enforcement does not own the broader current-control judgment.
- Evidence: [`docs/app.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/app.md); [`docs/cli.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/cli.md); [`docs/autonomous-device-integration.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/autonomous-device-integration.md); [`docs/architecture.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: session liveness/recovery, model/usage display and process enforcement are supporting mechanisms, not themselves autonomous S3 owners.
- Whole-system current view: the app can search harnesses/tabs/projects/machines and list every agent waiting on the user; the device/application interface exposes `agents.list` with agent state/recap and explicit focus; the daemon registry is the source of truth for the sessions it owns.
- Current-control decision scope: create, stop/restart, retarget, delete/update, message/cancel a session or turn, answer an open question and redirect current operator attention among running S1 units.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous controller must be composed | current multi-session state exposed over `agents_list` / local control protocol | controller can invoke first-party restart/retarget/update/delete/message/cancel operations that alter subsequent session operation | `docs/cli.md`; `docs/autonomous-device-integration.md` |
| Parent (`P`) | installation owner/operator | app/device shows current sessions, waiting questions, state/recaps or a session needing intervention | owner chooses stop/restart/focus/message/question action; daemon applies it and the selected session subsequently runs under that decision | `docs/app.md`; `docs/autonomous-device-integration.md` |

## S3* — Complementary audit

- State: —
- Function: no installation-level complementary audit path is established from the reviewed standard distribution.
- Disturbance / variety regulated: OpenHarness exposes transcripts, verdict findings, checks and development acceptance evidence, but the installation-level runtime does not provide a materially independent auditor that challenges ordinary S1 completion/reality claims and closes findings back into top-level control.
- Decisive decision or feedback right: not established at installation recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: transcript normalization, DSH checker/verdict feeds, pane viewers, daemon health/reconciliation and development/release acceptance checks.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: ordinary package checks can observe artifacts independently of a producing model process, but they are routine domain checks/verdict feeds in the same work path and do not establish the required installation-level independent audit relation. Development acceptance/CI is outside the assessed operating boundary.
- Evidence: [`store/spec/README.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/store/spec/README.md); [`store/README.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/store/README.md); [`store/agents/marp/AGENTS.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/store/agents/marp/AGENTS.md); [`HANDOFF.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/HANDOFF.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: individual DSHs may implement lower-recursion checking or adversarial deliberation; that does not establish a top-level OpenHarness S3* owner without an installation-level audit relationship.

### Absence scope

- Surfaces inspected: daemon transcript/event normalization; DSH verdict contract and viewer-triggered checks; representative Marp checker workflow; Roundtable nested panel workflow; repository development handoff/acceptance material.
- Plausible first-party paths checked: verdict/findings, toolchain checks, transcript/recap, viewer inspection, Roundtable cross-examination, CI/release/acceptance evidence.
- Why no material first-party path remains: verdict/check paths are routine within one DSH's production loop, Roundtable cross-examination belongs to a lower recursion, and repository acceptance/CI is adjacent development governance rather than a shipped installation-level auditor.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: adapt the installation's future operational repertoire to changes/opportunities in the available domain-harness ecosystem by discovering and adopting new or updated DSH capabilities.
- Disturbance / variety regulated: future work may require a domain/toolchain the installation does not currently have, while community/built-in packages and package versions can change independently of the installed app/CLI release.
- Decisive decision or feedback right: choose whether a newly available or updated domain capability should be installed/updated/removed so it becomes part of the installation's future S1 repertoire.
- Decision owner: constructor mode — not supplied; a downstream autonomous adopter must be composed around the dedicated DSH catalog/install/update commands. Parent mode — the installation owner selecting a package/update through Store/CLI.
- Supporting / enforcement mechanisms: public live catalog reader/cache, Store metadata and examples, `harness dsh list/install/update/remove`, package manifests, setup/doctor, viewer dependency resolution and workspace materialization.
- Closure path: live catalog/current package state exposes new or updated capability option → autonomous controller (if composed) or parent user selects adaptation → DSH manager installs/updates package and dependencies → instructions/skills/toolchain/viewer become available in New Harness/subsequent sessions → later operations can use the changed capability.
- Boundary reachability: Store/DSH management is a documented shipped OpenHarness mode. Built-in and community packages are resolved by the standard CLI and materialized into ordinary sessions; no development-only publisher actor is used as the adaptation owner.
- Why this is / is not agent-owned: the distribution has function-specific sensing/options and a concrete capability-mutation path, but it does not package an autonomous installation-level decision-maker that chooses which capability to adopt. The operator can close that judgment directly, while downstream specialization can compose an autonomous actor over the dedicated DSH management path.
- Evidence: [`store/README.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/store/README.md); [`store/spec/README.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/store/spec/README.md); [`README.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the adjacent catalog-publishing workflow decides what the OpenHarness project publishes and is excluded from installation ownership. The credited S4 path is the installed system consuming catalog/package change and mutating its own available capability; it is not a claim that package publication itself is installation S4.
- External distinction: the live catalog can expose packages from repositories outside the installation and changes independently of client releases; Store metadata carries source/upstream/examples and installed/update state.
- Future / prospective distinction: a package/update represents a capability that can be added before subsequent domain work, rather than merely a response inside the current agent turn.
- Adaptation option generated: install a new DSH/viewer, update an installed package while preserving its workspaces, or remove/replace an available capability.
- Path back into current capability / S3: accepted package state is materialized under `~/.harness/dsh`, its instructions/skills/toolchain/viewer are wired into subsequent session creation, and the capability appears as an available Harness tile/engine mode.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous adopter must be composed | catalog/package state exposes a new or updated domain capability | dedicated `dsh` list/install/update/remove path can mutate installed capability; subsequent sessions consume the package | `store/README.md`; `store/spec/README.md` |
| Parent (`P`) | installation owner/operator | user identifies a future domain need or sees an available/update Store capability | user chooses install/update; CLI materializes the package and later sessions run with the new capability | `README.md`; `store/README.md` |

## S5 — Policy and identity

- State: —
- Function: no installation-level identity/ultimate-policy closure path is established from the reviewed standard distribution.
- Disturbance / variety regulated: OpenHarness contains account/device trust, engine selection, permission-bypass flags, package manifests/instructions and security constraints, but these are access/configuration/operational policy surfaces rather than a demonstrated identity-level decision loop.
- Decisive decision or feedback right: no first-party path was found in which an OpenHarness identity or ultimate-policy issue reaches legitimate ultimate authority and the returned decision governs subsequent installation operation as S5.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: SSO/pairing, E2EE trust/revocation, engine permission flags, DSH manifests and instructions, Store metadata, daemon configuration and security limits.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: none of the inspected policy/configuration surfaces establishes an identity-level deciding actor or parent closure; ordinary user authority over engines, packages, trust and session actions is not promoted to S5.
- Evidence: [`docs/app.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/app.md); [`docs/cli.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/cli.md); [`docs/architecture.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/docs/architecture.md); [`store/spec/README.md`](https://github.com/autonomous-ai/openharness/blob/ffbc4b0d7de0dfb8ccf43213e17e2495dce7fd85/store/spec/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a parent user plainly has broad product authority, but Methodology 0.3.6 requires the underlying matter itself to be identity/ultimate-policy level and operationally returned; generic configuration or approval is insufficient.

### Absence scope

- Surfaces inspected: account/login and machine pairing, device trust/revocation, app engine/session configuration, DSH manifests/instructions, Store/package selection, daemon environment/configuration and security boundaries.
- Plausible first-party paths checked: SSO/account ownership, permission-bypass flags, engine/DSH selection, device pairing/revocation, DSH `AGENTS.md`, manifest policy and Store package governance.
- Why no material first-party path remains: the inspected surfaces authorize, constrain or configure ordinary operation but do not expose a runtime identity/ultimate-policy dispute/proposal → legitimate ultimate authority → returned policy decision → subsequent-operation closure at the installation recursion.

## Distributed OSS parent arrangement

Repository maintainers and contributors decide what enters the upstream OpenHarness project and Store catalog, but that public development organization is adjacent to the assessed installed product. It is therefore not credited as installation-level parent S3/S4/S5 ownership. The positive parent modes above belong to the installation owner operating the shipped product; repository CI, release and catalog publication are evidence/context only.

## Self-hosted and non-human modes

OpenHarness can run its daemon headlessly and exposes automation controls, but the reviewed standard distribution does not package a non-human installation-level S3 or S4 decider. The `C` base states record the specific first-party construction paths without upgrading them to `A`. Human app/device/CLI operation closes the corresponding parent modes.

## Recursion

The installation contains multiple durable S1 sessions. Some DSH sessions can themselves be organizational systems. Roundtable is the clearest frozen example: one moderator session launches multiple vendor seats, deliberately seals opening rounds to prevent cross-agent convergence, then exposes cross-examination, claim mapping, a human-chair pause and a final recommendation with named dissent. Those relations are meaningful lower-recursion S2/S3/S3*-adjacent evidence, but the seats are subprocesses inside the Roundtable work cell, not peers of every installation-level Harness session. The installation vector therefore does not inherit those child functions.

## Variety and escalation

OpenHarness attenuates session/process variety through one registry, normalized event frames, durable tmux panes, receipts/idempotency and encrypted multi-machine transport. It amplifies operator variety through an installation-wide search/attention surface and through DSH packages that add domain-specific tools, checks and viewers.

Questions are an explicit escalation path: the agent's own question reaches the app/device, the operator answers it, and the answer returns into the engine's dialog. This is a useful algedonic/current-control channel but is not automatically S5; the receiving decision remains whatever operational/current-control function the question actually concerns.

Store packages change the installation's future response repertoire. The live catalog preserves a last-valid snapshot when the network is unavailable, while installed packages remain usable. That persistence reduces adaptation-channel fragility without changing who owns the adoption decision.

## Evidence gaps

- The hosted web client is not in the reviewed repository; only its documented wire behavior was considered, and no undocumented web-client owner or function is credited.
- The repository ships many DSHs. Representative first-party packages were inspected where they could plausibly change the top-level mapping, especially Marp (routine checker/verdict) and Roundtable (nested multi-agent organization). A future reassessment may find a newly shipped package that explicitly closes an installation-level relation, but lower-recursion capability is not inferred upward here.
- `S3=C(P)` depends on treating the documented automation WebSocket as a function-specific current-control construction path rather than generic extensibility; its operations are explicitly session-control operations over installation state, but an autonomous controller is not shipped.
- `S4=C(P)` depends on the live Store/DSH manager being an installation capability-adaptation path. The autonomous adoption judgment is not shipped, and adjacent Store publication/governance is deliberately excluded from ownership.
