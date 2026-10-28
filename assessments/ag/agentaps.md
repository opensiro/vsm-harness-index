---
harness_id: agentaps
project_name: Agentaps
repository: https://github.com/cachix/agentaps
review_ref: 1dbaeeea88f446a2fdaf633dc00e7a344351d05a
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agentaps

## Review boundary

- System in focus: Agentaps desktop/local-SSH ACP client and paired browser workspace at the frozen source revision.
- Purpose and identity: present and persist external coding-agent sessions and forward user interaction locally or over SSH.
- Relevant environment: installed ACP agents/adapters, local/remote projects, desktop users and paired browsers.
- Standard-distribution boundary: Rust desktop/session/ACP transport, discovery, session-control CLI, config/persistence, diff/terminal views and browser control protocol.
- Credited operating / distribution surfaces: src/acp.rs, session.rs and session/prompt.rs, discovery.rs, cli.rs, app/session/mobile paths and bundled agentaps skill.
- Adjacent first-party surfaces excluded from ownership: tests, CI/releases and project-maintainer governance; separately installed Claude/Codex/Gemini/OpenCode internals and reasoning/tool loops are outside the reviewed first-party client.
- First-party operating / deployment modes considered: local ACP v1/v2, SSH agent command, npx adapter discovery, resumed/forked sessions and paired browser prompt/cancel/permission controls.
- Recursion level: one desktop session workspace/client, not the external agent or contributor organization.
- Reviewed revision: `1dbaeeea88f446a2fdaf633dc00e7a344351d05a`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The desktop discovers installed ACP commands or offers an adapter download, starts an external agent process locally or over SSH, initializes its protocol/session and forwards user prompt blocks. session.rs records queued/active prompts and renders external updates; persistence saves client snapshots while conversation history is replayed by the external harness. Fork prompts supply conversation context. The bundled skill exposes one local CLI capability: open an empty session with the same project/command. It explicitly does not transfer history, send a prompt or start work there. Paired-browser commands expose snapshot, prompt, cancel, permission and session creation. Diff/terminal views and process control are workspace affordances, not a first-party model/action organization.

## Operational model

Recommended disposition: excluded-no-agentic-vsm. The first-party boundary closes ACP interaction, connection/session state and UI actions; the decisive coding action/result loop belongs to the selected external harness. No positive autonomy state is assigned to the client by borrowing that engine. This is a corpus-boundary exclusion, not a quality or security judgment. The historical alias domenkozar/agentaps was screened as a client in discovery #875; this is the first canonical frozen-source record and preserves that provenance without reopening the old batch.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational task loop at the client boundary
- Disturbance / variety regulated: connection failures, interrupted prompts, session/UI state and external-agent updates
- Decisive decision or feedback right: substantive coding/tool decisions remain inside the external ACP agent
- Decision owner: external model/harness for coding; user for client requests; deterministic client for transport/lifecycle
- Supporting / enforcement mechanisms: ACP subprocess, JSON-RPC, prompt queue, reconnect/replay and snapshots
- Closure path: user prompt → external session/prompt → external events/permission requests → client view
- Why this is / is not agent-owned: first-party code transports the external decision loop rather than supplying a model/tool actor
- Evidence: [src/acp.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/acp.rs), [src/session.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/session.rs), [src/session/prompt.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/session/prompt.rs), [src/discovery.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/discovery.rs).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: all 116 frozen tracked paths inventoried; desktop/session/ACP/discovery, prompt conversion and bundled CLI skill inspected
- Plausible first-party paths checked: local/SSH command, adapter download, resume/retry/fork and agent-invoked new-session
- Why no material first-party path remains: every substantive action is delegated to an installed external harness; new-session creates an empty session and starts no task; no shipped first-party autonomous S1 owner remains

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 conflict-regulation loop established
- Disturbance / variety regulated: multiple visible conversations and panes
- Decisive decision or feedback right: open/focus sessions and forward queued prompts
- Decision owner: user/client lifecycle; external agents own any operational coordination
- Supporting / enforcement mechanisms: panes, session IDs, prompt queues and local new-session endpoint
- Closure path: client selections change displayed/target sessions, not coordinated operational commitments
- Why this is / is not agent-owned: multiple agent windows do not establish S2
- Evidence: [src/panes.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/panes.rs), [src/app/sessions.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/app/sessions.rs), [src/cli.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/cli.rs), [skills/agentaps/SKILL.md](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/skills/agentaps/SKILL.md).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: panes/session selection, independent commands, CLI capability, queue and browser sessions
- Plausible first-party paths checked: parallel conversations, shared project paths, forked context, new-session requests and queued steering
- Why no material first-party path remains: no first-party specific inter-operational conflict/oscillation response with returned S1 adjustment is wired; session plurality/routing alone is insufficient

## S3 — Inside-and-now control

- State: —
- Function: no in-boundary whole-system operational regulation established
- Disturbance / variety regulated: busy sessions, process disconnection and permissions awaiting users
- Decisive decision or feedback right: cancel a turn, switch a model/mode or answer an external permission request
- Decision owner: desktop user and external harness, with client enforcing transport/process actions
- Supporting / enforcement mechanisms: session activity indicators, cancel RPC, process groups and browser control
- Closure path: generic session control returns to the external agent; no task-fleet resource/commitment regulation owned by the client
- Why this is / is not agent-owned: a workspace UI and stop button alone do not establish parent S3
- Evidence: [src/session.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/session.rs), [src/acp.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/acp.rs), [crates/control-protocol/src/lib.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/crates/control-protocol/src/lib.rs), [src/app/mobile.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/app/mobile.rs).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: session controller, settings, local/SSH process management, paired-browser snapshots and controls
- Plausible first-party paths checked: model/mode settings, cancel, interrupted-request resume, permission forwarding and multi-session current view
- Why no material first-party path remains: the view/control contract is conversation lifecycle over external agents, not a first-party task organization with function-specific whole-system current-control closure

## S3* — Complementary audit

- State: —
- Function: no complementary independent audit path established
- Disturbance / variety regulated: external tool status and changed files
- Decisive decision or feedback right: display diff or inspect conversation/tool events
- Decision owner: user or external harness; no independent first-party auditor
- Supporting / enforcement mechanisms: diff watcher/view, transcript presentation and protocol validation
- Closure path: display/validation updates the UI, without independent audit judgment and corrective return
- Why this is / is not agent-owned: viewing raw diffs can support an external review but is not a supplied audit actor
- Evidence: [src/git_diff.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/git_diff.rs), [src/diff_view.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/diff_view.rs), [src/app/tool_activity.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/app/tool_activity.rs), [src/session/protocol.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/session/protocol.rs).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: diff and tool presentation, protocol tests, external update handling and user permission requests
- Plausible first-party paths checked: raw Git diff, tool logs, external permission requests and developer/browser tests
- Why no material first-party path remains: these expose information or validate protocol; none supplies complementary operational-claim challenge, independent audit judgment and returned corrective control

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective capability adaptation loop established
- Disturbance / variety regulated: new agent commands, model choices and retained session context
- Decisive decision or feedback right: user chooses installed command/settings and reopens/forks context
- Decision owner: user/external harness; no first-party adaptation actor
- Supporting / enforcement mechanisms: agent discovery, configuration snapshots and history replay
- Closure path: settings/context affect future prompts without prospective environmental option synthesis
- Why this is / is not agent-owned: discovery of an executable and retained conversation are not S4
- Evidence: [src/discovery.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/discovery.rs), [src/config.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/config.rs), [src/persistence.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/persistence.rs), [src/session/prompt.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/session/prompt.rs).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: discovery/settings, reconnect/replay, forks, docs and local/SSH operating modes
- Plausible first-party paths checked: executable discovery, adapter fallback, model/effort setting, history persistence and contextual fork
- Why no material first-party path remains: no first-party external prospective inquiry → capability adaptation option → returned present-capability change is supplied; hypothetical external skills are not credited

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy resolution loop established
- Disturbance / variety regulated: connection trust, browser pairing and external tool approvals
- Decisive decision or feedback right: pair/revoke a client or answer a task permission
- Decision owner: user plus external harness authorization policy
- Supporting / enforcement mechanisms: paired tokens, protocol permission responses and local control authentication
- Closure path: permission/connection responses govern specific access; no identity-policy issue referral/return
- Why this is / is not agent-owned: authentication or final user say over a tool does not establish S5
- Evidence: [crates/control-protocol/src/lib.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/crates/control-protocol/src/lib.rs), [src/mobile.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/mobile.rs), [src/cli.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/cli.rs), [src/session.rs](https://github.com/cachix/agentaps/blob/1dbaeeea88f446a2fdaf633dc00e7a344351d05a/src/session.rs).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: pairing/control credentials, session modes, external permission UI and bundled instructions
- Plausible first-party paths checked: user approvals, paired-browser revocation, agent/model selection and source-project governance
- Why no material first-party path remains: the client supplies trust and access controls, without identity/ultimate-policy dispute → legitimate authority → authoritative decision returned into an owned agent organization

## Exclusion decision

Canonical disposition is excluded-no-agentic-vsm at this first-party client boundary. The proposed-stage all-absence vector is boundary documentation and does not rate the external coding agents. No synthesis/signature or included ranking entry is justified.

## Distributed OSS parent arrangement

Project maintainers and local workspace users are separate from the external harness. No organization-level parent function is inferred from contributors or permission UI.

## Self-hosted and non-human modes

Local/SSH and paired-browser modes preserve the same external operational owner. The bundled new-session skill supplies an explicit client capability, not a running agent organization.

## Recursion

Sessions/panes are presentation and process boundaries; nesting or parallel views do not establish recursive viable units.

## Variety and escalation

Client errors, reconnect state, queued prompts and permission requests are forwarded/displayed within protocol boundaries. No VSM escalation function is inferred from a dialog or error status.

## Evidence gaps

Rust/Cargo and native GUI dependencies are unavailable on the inspection host, so Rust/desktop/browser integration tests were not run. Model-free JavaScript syntax checks for web/src/browser.js, web/site/site.js and web/tests/browser.mjs, plus shell syntax checks for build scripts, passed. No external ACP agent was run. The source boundary is directly inspectable; no missing source is being relabeled as semantic absence.
