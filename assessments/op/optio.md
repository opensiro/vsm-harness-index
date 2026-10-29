---
harness_id: optio
project_name: Optio
repository: https://github.com/jonwiggins/optio
review_ref: 3163761c3a0974bbb290afea8d09ddc1a8e8ac7c
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

# Optio

## Review boundary

- System in focus: the first-party Optio self-hosted orchestration, persistent-agent turn services, pod isolation and reconciliation as shipped at the reviewed commit; not the internal implementation or governance of all external agent CLI vendors.
- Purpose and identity: create, schedule, safely place, observe, resume and connect coding-agent work in repositories, jobs, interactive sessions and persistent inbox-driven agents across hosted clusters and Optio Local.
- Relevant environment: prompts, webhooks, tickets, schedules, incoming agent messages, repo/PR/CI status, pod or network outages, Kubernetes capacity, credential boundaries and human control intents.
- Standard-distribution boundary: web/API services, workers, shared state-machine functions, pod pools, persistent-agent HTTP/MCP messaging, shipped configurable multi-provider agent adapters and bundled runnable agent-team examples. Agent provider/model selection is an operator option.
- Credited operating / distribution surfaces: executable model-led external harness turns hosted by Optio through first-party prompt assembly, run protocol, agent pods and result/inbox return; distinct running agent tasks/roles and first-party credential-compatible pod placement constraints.
- Adjacent first-party surfaces excluded from ownership: external Claude Code/Codex/Copilot/Gemini/OpenCode/other vendors' internal cognitive machinery; a customer's custom task instructions, manual application operation, non-shipped planned features, testing and maintainers' security-review reports.
- First-party modes considered: repo tasks and PR-review stages, standalone sessions and jobs, message-triggered persistent agents, built-in Ask Optio controller-chat mode and first-party example teams as supported configurations. Pure shell jobs have no model-owned S1.
- Recursion level: one Optio workspace deployment and multiple separately running agentic work units, with the human workspace/administrator as external parent.
- Reviewed revision: `3163761c3a0974bbb290afea8d09ddc1a8e8ac7c`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Optio launches operator-selected coding-agent runtimes in agent pods or paired local machines. The repo-task flow can hand a prompt to an agent, accept resulting code/PR, read CI/review feedback and resume when configured. The persistent-agent worker is a particularly explicit first-party operational path: it claims a named agent, drains its pending inbox, renders the turn prompt, starts a configured model-backed agent command in a pod with scoped tools/secrets, streams results and finishes a durable turn. Completion returns the agent to idle for the next message, schedule or event; another agent can address its mailbox using a signed per-turn API token. The model's task-sensitive actions occur in an external provider CLI, but Optio's standard distribution instantiates and feeds that agent as a supported operating mode, rather than relying on a downstream adopter to invent the entire loop.

One concrete inter-S1 disturbance is incompatible trust domains being packed into shared repo execution pods: processes, home directories, credentials and worktree files in one pod are mutually readable. The first-party security review identifies the prior repository-URL-only pooling defect, and source implements isolation keys from workspace, owner, purpose and credential profile. Pod selection must match the isolation key, with different derived workload/resource identities and separate review purpose; an incompatible agent is not admitted to the other agent's pool. This is a narrow deterministic `S2=C` collision-prevention relation among separate agentic work units. It does not assert hostile multi-tenant isolation within a compatible pool: the code and documentation explicitly call co-resident work mutually trusted.

Optio's reconciler has per-run snapshots of dependencies, pod state, capacity, PR checks, attachment leases, control intents and liveness. It issues typed transitions under compare-and-swap; a stale observer re-enqueues a fresh pass. This is operationally significant current-work supervision and reliable lifecycle enforcement. However, the pure `reconcileRepo`/`reconcilePersistentAgent` decisions are *per run*, and `Ask Optio` is an agent for a user's requested work, with user confirmation for writes; the stock system does not establish a whole-system regulator that negotiates competing priorities/commitments across operating units or makes exceptions on behalf of the system as a whole. It is not automatically S3 because a module calls itself a control plane.

Source anchors: [README](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/README.md), [persistent-agent worker](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/workers/persistent-agent-worker.ts), [persistent-agent operating model](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/persistent-agents.md), [pod isolation](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/services/pod-isolation.ts), [pod pool](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/services/agent-pod-pool.ts), [security review](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/security-review-2026-10.md), [reconciliation](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/reconciliation.md).

## Operational model

The unit of operation is an agentic task or persistent-agent turn: a model-backed provider performs task-sensitive work with tools and observed feedback, while Optio provides material continuity, placement, external trigger routing, record persistence and optional resumption. Distinct S1 tasks may be assigned to shared physical pods only when their first-party trust/isolation partition matches; this enforces a cross-unit safety coordination constraint. A separate organizational S3 audit, future strategy loop or ultimate-policy hierarchy is not inferred from run-oriented recovery and permissions.

## S1 — Operations

- State: A
- Function: run autonomous model-directed work in a supported CLI agent with tool effects and returned results, including persistent message-driven turns and coding task feedback.
- Disturbance / variety regulated: variable requests, repo changes, tool and CI results, messages from other agents/users, errors, scheduled/wake events and agent continuation.
- Decisive decision or feedback right: the configured model-backed runtime chooses task-specific tools and work product, receives resulting tool/output observations and may continue or report completion.
- Decision owner: instantiated CLI agent runtime during an Optio work/turn, not deterministic BullMQ scheduling or an Optio database row. External vendor implementation is not claimed as Optio-owned code; invocation/wiring is a shipped first-party mode.
- Supporting / enforcement mechanisms: provider adapters and `buildAgentCommand`, turn prompt built from durable inbox, run supervisor/attachment protocol, workspace tools/secrets, job and pod workers, workflow/review feedback.
- Closure path: a message/event triggers a persisted turn → prompt and agent executable are assembled and started → CLI model/tools process work and emit results/logs → Optio retains status/output and notifies/returns the persistent agent to idle → subsequent messages or resumed code-review work re-enter with relevant evidence.
- Boundary reachability: persistent-agent worker and built-in work UI/API supply this actual path, with installer-provided provider account. Bundled Forge/Mars examples instantiate persistent specialist roles without requiring a custom orchestration engine.
- Why this is / is not agent-owned: the CLI model selects task action based on observations, while Optio's first-party scheduling, security and state persistence are supporting mechanisms; shell-only work is not counted.
- Evidence: [persistent-agent-worker.ts](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/workers/persistent-agent-worker.ts), [docs/persistent-agents.md](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/persistent-agents.md), [repo task work](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/tasks.md), [bundled Forge agents](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/examples/persistent-agents/forge/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: No provider/model live run, Kubernetes cluster or end-to-end workflow was executed; external agent vendor internals are outside repository ownership.

## S2 — Coordination

- State: C
- Distinct S1 units: separate repo-task agents, persistent specialists, automated PR review agents and interactive sessions with different owners/workspaces/credential capabilities may execute concurrently on the Optio pod fleet.
- Inter-S1 disturbance: pooling by repository URL alone could co-locate different agentic S1 units whose credentials, home directories, process environment and files should not be mutually accessible. A review agent also has a distinct trust purpose from the primary implementation agent.
- Attenuating coordination relation: `podIsolationKey` derives a stable partition from workspace, owner, purpose and credential profile, and pod selection validates that key plus pool/resource matching. Isolated workload names/homes prevent unlike scopes from reusing a pod even if repository URLs match.
- Feedback into subsequent S1 behaviour: on new work/turn admission the scheduler reuses an eligible compatible pod or provisions/selects a separate one; subsequent agent processes inherit only that selected execution environment and its scoped secrets. A preferred pod with mismatched identity is rejected for reuse.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: this is not just an inbox or common queue; it is an explicit first-party response to a documented inter-agent interference hazard (cross-owner credential/filesystem exposure), with each later S1's physical admission/placement constrained by the result.
- Function: deterministic isolation of incompatible operating cells while permitting trusted compatible work to share a local resource pool.
- Disturbance / variety regulated: concurrent agent workload placement with incompatible workspaces, owners, review purposes, credential profiles and retained process state.
- Decisive decision or feedback right: reject incompatible pod reuse and ensure distinct execution identities/pools for agents crossing trust domains.
- Decision owner: deterministic Optio pool selector/isolation-key code, supplied work metadata and human-configured access policy; no model-owned coordinator decision.
- Supporting / enforcement mechanisms: SHA-derived isolation keys, `pickPod` guard, owner-aware secret selection, purpose-specific review workers, separate interactive session pods.
- Closure path: incoming S1 work metadata → derived isolation key → guarded pod selection or provisioning → agent receives scoped environment on its own partition → next work re-evaluates compatibility rather than inheriting an unsafe preferred pod.
- Boundary reachability: first-party repo/standalone pod services calculate and pass `isolationKey` to the shared pool manager; security review identifies the concrete cross-unit collision this implementation corrected.
- Why this is / is not agent-owned: a definite interference-damping placement relation is present, but its decisions are deterministic (`C`), not autonomously chosen by an S2 model.
- Evidence: [pod-isolation.ts](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/services/pod-isolation.ts), [agent-pod-pool.ts](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/services/agent-pod-pool.ts), [repo-pool-service.ts](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/services/repo-pool-service.ts), [security-review-2026-10.md](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/security-review-2026-10.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Compatible agents inside one pool are mutually trusted; this does not prove robust hostile-tenant containment, agent-to-agent plan negotiation or overall workforce coordination.

## S3 — Inside-and-now control

- State: —
- Function: no demonstrated whole-system current operations arbitration of competing agent commitments beyond per-run lifecycle decisions and configured capacity constraints.
- Disturbance / variety regulated: PR state, capacity saturation, failed pods, stale attachments, dependency failures, individual queue state and manual retry/cancel intents.
- Decisive decision or feedback right: the reconciler evaluates each run's snapshot and emits one typed state transition, delay, resume, review or auto-merge action; administrator configures resource caps and per-task options. No dedicated cross-work manager has a whole-system view and chooses changing operational priorities/commitments.
- Decision owner: deterministic per-run `reconcileRepo` and siblings, user/admin for manual intents, agent responding to a commissioned task via optional controller MCP. No qualifying metasystem S3 decision owner evidenced.
- Supporting / enforcement mechanisms: `WorldSnapshot`, global/repo capacity counters, BullMQ queue, CAS updates, PR/CI watcher, reconcile backoff, agent attachment lease and control intents.
- Closure path: particular run observation → per-run action and version-guarded execution → that run is enqueued/resumed/terminated/reviewed. Aggregate capacity merely gates admission; no whole-system priority bargaining or exception regulation across operating unit commitments is shown.
- Why this is / is not agent-owned: calling a module the control plane and providing a management MCP does not turn per-task state machines, schedules or tools into a separate system-wide S3 authority.
- Evidence: [docs/reconciliation.md](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/reconciliation.md), [reconcile-repo.ts](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/packages/shared/src/reconcile/reconcile-repo.ts), [reconcile-worker.ts](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/workers/reconcile-worker.ts), [controller MCP](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/controller-mcp.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Rich operational telemetry and controls could support a downstream S3 agent; optional control tools are not proof that such an organization-wide controller is shipped as default.

### Absence scope

- Surfaces inspected: all four per-run reconciler state machines, world snapshot and executor, shared capacity counters, Ask Optio and controller MCP, parent/child messaging.
- Plausible first-party paths checked: automatic PR resume/merge, central capacity gating, dashboard queue and LLM-assisted work creation/manipulation.
- Why no material first-party path remains: these govern execution per run or per requested action without a first-party cross-S1 manager acquiring whole-system current evidence and dynamically allocating/revising shared priorities, commitments or resources for the collective.

## S3* — Complementary audit

- State: —
- Function: no ongoing independent second access to operational reality that challenges S3 reporting and returns findings to a current-system regulator.
- Disturbance / variety regulated: PR reviewer disagreements, job failures, log gaps and security/workload configuration errors.
- Decisive decision or feedback right: optional PR review agents check a code artifact in the ordinary delivery lifecycle; recovery logs and security-review documents inform developers/operators, without a separately scoped runtime S3* authority.
- Decision owner: primary task worker, review worker, administrative user and adjacent security-review authors, not an independent complementary audit of whole-system current control.
- Supporting / enforcement mechanisms: PR review worker, checks and approvals, audit/activity logs, telemetry, security-review markdown and test suites.
- Closure path: reviewer feedback can cause an ordinary task's resumption; security reports guide maintainer fixes outside the running operating metasystem. No independent audit signal is specifically returned to a whole-system S3 manager.
- Why this is / is not agent-owned: an automated PR critic or developer security review is not a second source of operational evidence with independent S3* mandate and return path merely because it is called review.
- Evidence: [reconciliation](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/reconciliation.md), [PR-review worker](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/apps/api/src/workers/pr-review-worker.ts), [security review](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/security-review-2026-10.md).
- Basis: structural.
- Confidence: high.
- Caveats: No live independent auditing of an Optio deployment has been established by this review.

### Absence scope

- Surfaces inspected: PR reviewer path, CI status ingestion, telemetry, shared run logs and security review docs.
- Plausible first-party paths checked: reviews after code change, stale-lease recovery, independent report cards and offline security audits.
- Why no material first-party path remains: these are within ordinary delivery/recovery or adjacent developer assurance, not a distinct, sufficiently independent runtime auditing owner examining management claims and returning an actionable finding to S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped prospective environmental intelligence-and-adaptation function that negotiates new organizational options with current system control.
- Disturbance / variety regulated: external events, incident alerts, code issues, integration changes and agent tasks selected by a user.
- Decisive decision or feedback right: trigger adapters start prescribed work; agents can research outside topics as user tasks, but no designated S4 owner develops long-horizon operating capability options from environmental evidence and returns them to a current S3 function.
- Decision owner: workspace operator defines schedules/triggers/prompts, individual agent runtime performs commissioned investigations, maintainers implement product roadmap.
- Supporting / enforcement mechanisms: external trigger integrations, job reports, memory of persistent agents, roadmap plans and event-to-prompt bindings.
- Closure path: event → task/agent run → output/PR/inbox; this is task operations, not external future adaptation into the organization’s present capability.
- Why this is / is not agent-owned: access to PagerDuty/Sentry/GitHub or an optional research prompt is not by itself an autonomous organizational S4 relation.
- Evidence: [README](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/README.md), [tasks.md](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/tasks.md), [persistent-agents.md](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/persistent-agents.md).
- Basis: structural.
- Confidence: high.
- Caveats: A downstream persistent team can be configured with strategic foresight, but that would require a pinned deployment-specific operating relation.

### Absence scope

- Surfaces inspected: incident/event triggers, recurring jobs, example agent teams, prompt inputs, roadmaps and persistent memory.
- Plausible first-party paths checked: scheduled research tasks, post-incident reports and external connector feeds.
- Why no material first-party path remains: stock triggers and tasks do not return externally grounded capability-change options through a two-way S3/current capacity adoption process.

## S5 — Policy and identity

- State: —
- Function: no evidenced ultimate organizational identity/mandate dispute adjudication with legitimate authority and returned policy closure.
- Disturbance / variety regulated: workspace membership, user/work ownership, controller grants, password/credential scope and individual approval for tool writes.
- Decisive decision or feedback right: human administrators configure access and keys, choose runtimes, create work and approve actions; no first-party path elevates a conflict over the collective system’s identity/strategy to final authority and returns the outcome to S3/S4 and future operations.
- Decision owner: deployment owner/workspace administrator for ordinary permissions, credentials, operational composition and membership; no live ultimate-policy adjudicator established.
- Supporting / enforcement mechanisms: OAuth/OIDC roles, scoped per-turn controller credentials, member/admin checks, session approval and credential isolation.
- Closure path: configured policy and scoped token restrict the next tool/run; one action can be approved or denied, but no identity-level constitutional issue reaches an authoritative decision and is returned as a new continuing mandate.
- Why this is / is not agent-owned: standard access control and human approval are real but not VSM S5 in the absence of identity/ultimate-policy closure.
- Evidence: [controller MCP](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/controller-mcp.md), [sign-in](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/sign-in.md), [security review](https://github.com/jonwiggins/optio/blob/3163761c3a0974bbb290afea8d09ddc1a8e8ac7c/docs/security-review-2026-10.md).
- Basis: structural.
- Confidence: high.
- Caveats: A real human parent governance body could supply S5 outside the product boundary, but its organizational evidence is not in this repository.

### Absence scope

- Surfaces inspected: workspace/owner permission checks, human controller approval, task-scoped identity, security review and configuration-as-code.
- Plausible first-party paths checked: administrator reconfigures permissions, a task requests control rights, personal/organization ownership changes, manual work approval.
- Why no material first-party path remains: these are ordinary access/operational authorization processes without a demonstrated cross-time identity conflict, legitimate final policy choice and returned organizational instruction path.

## Distributed OSS parent arrangement

Optio maintainers ship orchestration; workspace administrators configure work and rights; separate vendors own the internal model agent implementations; external GitHub/CI/incident providers own their integration responses. The repo does not establish a joint S5 that governs every live workspace or agent vendor. Local user policy is not presumed to be a canonical organizational identity mandate.

## Self-hosted and non-human modes

Self-hosted Kubernetes/Optio Local execute provider-backed agent work with external model/service credentials. Persistent agents can receive non-human agent messages, run unattended scheduled turns and produce work, subject to quotas and permissions. The platform recovers and resumes runs while keeping each turn bounded. Neither the existence of an inter-agent mailbox nor an optional managing controller token proves an independent S3 agent.

## Recursion

Persistent agents have stable identity and multiple model-driven turns; repo tasks and reviewer tasks can act as other S1 units. Optio's deployment supplies shared placement/isolation and message infrastructure. Higher-level agent teams designed by users and provider-company governance are different recursions and not automatically inherited.

## Variety and escalation

Owner-and-purpose isolation keys, bounded concurrent agent slots, explicit control intents, lease-based reattachment, PR-review feedback, role-scoped controller grants and resync reduce operational variety. Needs-attention/failed/retry events can reach a human, but a dashboard badge or task alert is not by itself a VSM algedonic channel or S3/S5 decision.

## Evidence gaps

- Source-first structural analysis on pinned commit only; no deployed cluster, vendor LLM calls, API integration, security attack or operational success benchmark executed.
- `S2=C` narrowly credits explicit incompatible-agent pod/co-residency regulation. Reuse inside a compatible, mutually trusted pool is outside the containment claim; static per-run scheduling does not establish whole-system S3 autonomy.
- The optional controller MCP permits an authorized agent to manage work, but optional capability is not evidence that a stock deployment contains a whole-system current manager or policy-making identity authority.
- Reviewer agents, CI and developer security tests are not credited as independent S3* audits; external trigger response and scheduled research are not S4 without prospective system-capability feedback.

## Assessment summary

Optio ships model-backed tool-work execution through configured agent runtimes and durable persistent-agent turns (`S1=A`). Its first-party pod partitioning explicitly prevents incompatible S1 work units from sharing credentials and processes (`S2=C`). Per-run reconciliation, PR review, external triggers, controller tools and access policies do not demonstrate the stronger whole-system S3, independent S3*, future-oriented S4 or ultimate-policy S5 closure at this recursion. Proposed vector **`A / C / — / — / — / —`**.
