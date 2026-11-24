---
harness_id: h
project_name: H
repository: https://github.com/parlant/harness
review_ref: a45a50835d9fc51712a3afe0a2f97e8970781a0e
reviewed_at: 2026-11-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# H

## Review boundary

- System in focus: one installed H local daemon and its model-backed coding sessions, workspace resource and operator controls.
- Purpose and identity: run durable interactive or detached coding sessions with shared workspace coordination and review.
- Relevant environment: local workspace/git, provider accounts, user inputs, competing root and child sessions.
- Standard-distribution boundary: root Mix daemon H.*, stock coding harness, native terminal/web clients and first-party supported configuration; external model/provider internals not credited.
- Credited operating / distribution surfaces: coding sessions, daemon-backed child modes, workspace leases, owner live inbox and review, provider selection; separately built MultiCodex considered as optional configured mode.
- Adjacent first-party surfaces excluded from ownership: tests/fakes, release/build/dev organization, hypothetical roadmap, remote simulation not actual external fleet.
- First-party operating / deployment modes considered: daemon with attached or detached client, root and spawned subsessions, read-only/worktree child, owner workspace intervention and raw review, stock and optional pooled accounts.
- Recursion level: one daemon across its root and child coding sessions; root-only subtree management is not daemon-wide control.
- Reviewed revision: a45a50835d9fc51712a3afe0a2f97e8970781a0e.
- Observation date: 2026-11-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

OTP session coordinators persist intent/results, dispatch real provider streams and tools, recover interrupted tasks and expose a shared live catalog. Subagents are separate sessions with immutable spawn lineage and wait/start/await/steer/abort. Mutating calls use canonical-workspace writer leases; owner can intervene on contested workspace. Separate raw file/Git review submits revision-bound findings to coding conversation. Model catalog and optional account pool supply current provider selection. See [docs/architecture.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/architecture.md), [docs/architecture/subagents.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/architecture/subagents.md).

## Operational model

Root and child coding sessions are autonomous operational cells with independent context, task and workspace outcome. Root chooses child modes; runtime coordinates writer access. Authenticated owner sees daemon-wide commitments and can intervene in current shared workspace allocation. Complementary review is exposed but not agent-owned by default.

## S1 — Operations

- State: A
- Function: Execute coding sessions against workspace, using model-selected shell/filesystem tools and subsequent feedback.
- Disturbance / variety regulated: Unknown repository state and task/tool failures.
- Decisive decision or feedback right: Choose and revise tool actions and completion.
- Decision owner: Real model-backed coding session.
- Supporting / enforcement mechanisms: OTP coordinator, provider stream, tool workers, persistence and retry.
- Closure path: Generation emits tool calls, committed results return to next model turn, model returns terminal response.
- Boundary reachability: Default coding harness tools and ReqLLM generation are packaged with daemon; no client attachment required.
- Why this is / is not agent-owned: Removing model leaves transport and state but no task-level discretionary choice.
- Evidence: [lib/h/harness/coding.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/harness/coding.ex#L15-L87), [lib/h/session/server/generation.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/session/server/generation.ex#L810-L976), [lib/h/session/server/tools.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/session/server/tools.ex#L217-L421), [lib/h/provider/req_llm.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/provider/req_llm.ex#L39-L135)
- Basis: explicit
- Confidence: high
- Caveats: Provider credentials and local execution environment required.

## S2 — Coordination

- State: A
- Function: Attenuate conflicting writes among coding sessions by selectable isolated workspaces or read-only child roles, backed by writer leases.
- Disturbance / variety regulated: Parallel parent/child or sibling sessions competing for writes to the same canonical cwd.
- Decisive decision or feedback right: Root model chooses child read-only role or distinct prepared worktree, then responds to returned child receipts/outcomes.
- Decision owner: Root model owns isolation/role choice; deterministic lease manager enforces same-workspace exclusion.
- Supporting / enforcement mechanisms: Subagent schema, child cwd and read-only restrictions, WorkspaceLease waiter/handoff, durable settlements.
- Closure path: Children operate under selected workspace/tool constraints; mutating calls wait for lease, resume on grant; child results return to caller.
- Boundary reachability: Default depth-gated subagent exposes cwd/read_only and bash to prepare worktrees; daemon dispatch and writer lease are shipped.
- Why this is / is not agent-owned: Model chooses separation in response to actual work; deterministic manager serializes same-workspace writes, without owning discretionary choices.
- Evidence: [lib/h/tools/subagent.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/tools/subagent.ex#L17-L76), [lib/h/session/subagents.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/session/subagents.ex#L797-L839), [lib/h/workspace_lease.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/workspace_lease.ex#L107-L161), [lib/h/workspace_lease.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/workspace_lease.ex#L230-L247), [lib/h/session/server/workspace_wait.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/session/server/workspace_wait.ex#L7-L61), [docs/architecture/subagents.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/architecture/subagents.md)
- Basis: structural
- Confidence: high
- Caveats: Worktree preparation is model-selected bash, not automatic; lease keyed by effective cwd, not a sandbox; no claim all overlap cases prevented.

- Distinct S1 units: independently executing coding sessions, including direct children with separate contexts and delegated output.
- Inter-S1 disturbance: competing mutating tools on same workspace trigger workspace_busy; independent writers may interfere.
- Attenuating coordination relation: model chooses separate worktree or read-only child, while shared cwd mutations are serialized by explicit lease.
- Feedback into subsequent S1 behaviour: wait checkpoint, lease-granted signal and subsequent tool dispatch; child outcome returned to root model.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: role/cwd selection and writer lease directly address shared-workspace conflict.

## S3 — Inside-and-now control

- State: P
- Function: Owner regulates current commitments across daemon sessions using catalog state and targeted stop/lease handoff.
- Disturbance / variety regulated: Concurrent operating sessions, contested workspace and conflicting current priorities.
- Decisive decision or feedback right: Choose which current commitment to stop or prioritize for workspace allocation.
- Decision owner: Authenticated daemon owner at the daemon-wide recursion.
- Supporting / enforcement mechanisms: Live catalog, stop-session commands, holder identification and lease-fenced cancellation/handoff.
- Closure path: Owner selects stop holder; waiting session prioritised, holder cancellation commits, lease released and waiter resumes.
- Boundary reachability: Owner web inbox plus session workspace-wait controls invoke first-party command path; no custom composition.
- Why this is / is not agent-owned: Autonomous root can steer/abort its own children but no shipped model with daemon-wide operating authority/view; owner has all-session view and decides exception. Fixed queue/account policy is support, not agent ownership.
- Evidence: [clients/web/lib/h_web/live/inbox_live.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/clients/web/lib/h_web/live/inbox_live.ex#L12-L114), [clients/web/lib/h_web/live/session_live.html.heex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/clients/web/lib/h_web/live/session_live.html.heex#L320-L361), [lib/h/session/server/workspace_wait.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/session/server/workspace_wait.ex#L64-L112), [lib/h/workspace_lease.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/workspace_lease.ex#L127-L161), [lib/h/session/server/commands.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/session/server/commands.ex#L786-L811), [lib/h/session/subagents.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/session/subagents.ex#L466-L730)
- Basis: explicit/structural
- Confidence: medium
- Caveats: Only daemon-owner current control; a root subtree has narrower agent steering rights. No A or C mode for autonomous daemon-wide controller inferred from generic owner API.

- Whole-system current view: owner-authenticated live daemon catalog/inbox across sessions and detailed holder/waiter identity for contested workspace.
- Current-control decision scope: stop chosen live work, prioritize a competing waiter and transfer shared workspace lease, or leave current allocation unchanged.

## S3* — Complementary audit

- State: C
- Function: Expose separate artifact review channel to challenge coding session output against raw worktree or pinned Git blobs, with source-bound findings returned to session.
- Disturbance / variety regulated: Unreliable self-reported coding outcome or incorrect changes.
- Decisive decision or feedback right: Choose independently which evidence to inspect and what corrective findings to return.
- Decision owner: Owner reviewer or composed autonomous reviewer; shipped model audit decision actor not established.
- Supporting / enforcement mechanisms: Review file and commit API, raw Git reads, revision-bound selection and comment submission.
- Closure path: Owner reviewer reads actual changed files/commit and sends anchored ask/note to the target conversation; composed independent model reviewer can use review APIs and return findings.
- Boundary reachability: First-party web review and daemon review APIs are available alongside ordinary session runtime.
- Why this is / is not agent-owned: Producing coding model does not determine what raw bytes the separate reviewer inspects or what findings are submitted; autonomy needs reviewer composition.
- Evidence: [lib/h/daemon/review.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/daemon/review.ex#L87-L160), [clients/web/lib/h_web/live/review_live.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/clients/web/lib/h_web/live/review_live.ex#L367-L410), [lib/h/daemon.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/daemon.ex#L168-L184), [docs/architecture.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/architecture.md)
- Basis: structural
- Confidence: medium
- Caveats: No mandatory independent reviewer, no proof of reviewer competence; review may be performed by owner or composed agent. Ordinary subagent delegation alone not credited.

- Claim being audited: coding session's changed-file and commit output relative to reported work.
- Ordinary reporting path: session transcript and tool outputs in durable session.
- Complementary access path: separately queried working file bytes or Git object/commit snapshots, revision-checked review comments.
- Independence boundary: owner/reviewer chooses file and revision outside producer conversation, direct execution-env/Git read rather than producer summary.
- Who acts on findings: owner selects corrective review ask; target session receives it through normal submission; autonomous review actor requires composition.

## S4 — Outside-and-then intelligence

- State: —
- Function: No demonstrated prospective external adaptation loop at daemon boundary.
- Disturbance / variety regulated: Future shifts in model/provider/environment capabilities.
- Decisive decision or feedback right: No returned adaptation judgment from prospective external sensing.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Curated model catalog, user provider config, external usage polls in optional MultiCodex, context compaction.
- Closure path: Account observations select present eligible route; provider edits affect configuration but no first-party prospective option-generation loop.
- Why this is / is not agent-owned: Quota polling is present resource regulation; user-entered catalog and model picker are configuration, not external-and-future intelligence.
- Evidence: [lib/h/provider/req_llm/catalog.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/provider/req_llm/catalog.ex#L189-L247), [docs/providers.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/providers.md), [extensions/multicodex/README.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/extensions/multicodex/README.md), [docs/architecture.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/architecture.md)
- Basis: structural
- Confidence: medium
- Caveats: No inference from development roadmap or optional arbitrary extensions.

### Absence scope

- Surfaces inspected: Provider catalog and configuration, optional MultiCodex extension, session compaction and architecture docs.
- Plausible first-party paths checked: Current quota observations, model choices, provider catalog edits, startup/restart.
- Why no material first-party path remains: No prospective external modeling and returned capability-option decision, including parent mode.

## S5 — Policy and identity

- State: —
- Function: No runtime ultimate-policy closure at daemon-wide boundary.
- Disturbance / variety regulated: Potential disputes over daemon purpose/ultimate policy.
- Decisive decision or feedback right: No first-party identity-level resolution right evidenced.
- Decision owner: Owner configures accounts, instructions and provider settings, not established S5 path.
- Supporting / enforcement mechanisms: Owner authentication, config, instructions and tool selection, extension settings.
- Closure path: Config changes govern subsequent requests but no identity/policy matter routed to ultimate authority and returned as such.
- Why this is / is not agent-owned: Owner controls local tool/config boundaries, but ordinary configuration and task steering are not ultimate policy arbitration.
- Evidence: [lib/h/harness/coding.ex](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/lib/h/harness/coding.ex#L34-L105), [docs/providers.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/providers.md), [docs/extensions.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/extensions.md), [docs/architecture.md](https://github.com/parlant/harness/blob/a45a50835d9fc51712a3afe0a2f97e8970781a0e/docs/architecture.md)
- Basis: structural
- Confidence: medium
- Caveats: Maintainer governance is outside the installed daemon.

### Absence scope

- Surfaces inspected: Coding harness instruction/config sources, owner UI/command architecture, provider and extension configuration.
- Plausible first-party paths checked: AGENTS.md, owner authentication, account/extension changes, session model changes and stop commands.
- Why no material first-party path remains: These are task/operating settings, with no supplied identity or ultimate-policy decision path including parent mode.

## Recursion

Child sessions are independently executing operational units, not proof of complete recursive viability.

## Variety and escalation

Durable tool results, retry, workspace wait and cancellation feedback regulate local disturbances; owner intervenes in contested shared resource. No separate algedonic channel inferred.

## Evidence gaps

Source-bounded review only. No live provider/session execution, independent semantic review, or proof of universal workspace isolation. Autonomous daemon-wide S3 and autonomous S3* remain unestablished.
