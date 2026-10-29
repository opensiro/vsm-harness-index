---
harness_id: kube-agents
project_name: kube-agents
repository: https://github.com/gke-labs/kube-agents
review_ref: c20297fccc667bec06b5d78f89ee4e368fd29f3d
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# kube-agents

## Review boundary

- System in focus: the installed kube-agents Helm/operator agent deployment at the pinned revision, including its configured Hermes runtime, Planning/Platform/Cluster persona profiles, kanban worker dispatch, first-party patches, fleet-audit skills and GitOps handoff; not Kubernetes/GCP as a whole or the software-maintainer organization.
- Purpose and identity: handle user/chat requests and proactive Kubernetes fleet signals by assigning agent work, diagnosing cluster state, returning bounded plans and reviewable GitOps changes.
- Relevant environment: GKE cluster/network changes, workload incidents, operator and chat requests, multi-tenant credentials and multiple agents competing for shared worker slots.
- Standard-distribution boundary: Helm-deployed agent pod and configured Hermes model/tool runtime, its gateway/kanban profiles, sandbox, GKE MCP and GitOps suggestion path; upstream Hermes supplies inference/loop engine but the shipped composition and decision-bearing profiles are part of this deployment.
- Credited operating / distribution surfaces: `agents/platform/SOUL.md`/`config.yaml`, `agents/cluster/SOUL.md`, deployed default Planning profile, `deploy/shared/defaults/config.yaml`, `deploy/docker/patches/kanban_priority.py`, `kanban_ownership.py`, AutoOps session/incident pipeline and provided fleet-audit tools.
- Adjacent first-party surfaces excluded from ownership: repository CI, contributors, documentation website, Helm/Terraform installation scripts and unit-test fixtures are evidence/support, not live organizational actors; the external human/forge owns approval/merge of proposed infrastructure changes.
- First-party modes considered: Slack/Google Chat conversational turns, scheduled fleet audits, event-triggered AutoOps diagnosis and human-returned fix turn, Platform-to-Cluster agent card fan-out and GitOps PR proposal.
- Recursion level: a deployed fleet-management harness with operational Cluster Agent profiles under a Platform Agent and a Planning Agent ingress; do not conflate K8s controllers or the external company with its VSM recursion.
- Reviewed revision: `c20297fccc667bec06b5d78f89ee4e368fd29f3d`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The distribution installs a Hermes model/tool gateway with multiple configured agent personas. The default Planning Agent receives chat or injected events and creates kanban cards. The Platform Agent runs a model-guided worker session, uses GKE/platform tools, resolves fleet scope, delegates scoped cluster diagnosis and synthesizes returned findings before completing its card. Per-cluster Hermes profiles have a pinned `KUBECONFIG` and read-only tools; they return an RCA or proposed manifest in card result/metadata. A deterministic dispatcher owns actual execution slots and card lifecycle, with task priority and reserved slots separating user work from incident triage. The Platform Agent has the GitOps suggestion/fleet-audit route; an engineer still reviews/approves remediation PRs. Scripts implement fixed namespace, tool and credential gates rather than autonomous identity-level constitutional decisions.

Pinned primary sources:

- [README deployment/architecture](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/README.md)
- [Platform Agent persona / worker and delegation protocol](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/agents/platform/SOUL.md)
- [Per-cluster agent persona](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/agents/cluster/SOUL.md)
- [Configured Hermes agent turns and kanban](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/agents/platform/config.yaml)
- [Default gateway configuration](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/deploy/shared/defaults/config.yaml)
- [Concrete queue interference and reserved-slot attenuation](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/deploy/docker/patches/kanban_priority.py)
- [Card ownership and competing worker contexts](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/deploy/docker/patches/kanban_ownership.py)
- [AutoOps two-turn incident/approval path](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/agents/platform/docs/autoops-architecture.md)
- [Scheduled stockout-risk audit](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/agents/platform/governance/stockout_prevention_sop.md)
- [Readiness judgment and human queue](https://github.com/gke-labs/kube-agents/blob/c20297fccc667bec06b5d78f89ee4e368fd29f3d/agents/platform/governance/upgrade_readiness_brief_sop.md)

## Operational model

Chat/user or an event/cron trigger enters a configured Hermes gateway. A model-driven persona chooses tool calls and, if appropriate, delegates a card; the dispatcher runs a separate worker and persists its result; the Platform Agent interprets per-cluster findings and selects a response or a GitOps change proposal. Source code explicitly distinguishes a diagnosis turn from a later fix turn returned by an engineer's approval. Constructor-owned worker budgets, reserved slots, credentials and read-only controls support/enforce these choices. A PR proposal is not proof that the external engineer approved or merged it.

## S1 — Operations

- State: A
- Function: task-specific Kubernetes operational diagnosis, plan production and bounded GitOps-remediation proposal through model-guided agent/tool iterations.
- Disturbance / variety regulated: variable cluster failures, work requests, GKE configurations, telemetry and command/tool observations.
- Decisive decision or feedback right: interpret a new task, choose the next diagnostic/tool intervention from observations, decide when an RCA, response or proposed change is ready.
- Decision owner: configured Hermes Planning, Platform and per-cluster model-driven agent actors within the shipped deployed harness, each under a defined persona and tool scope.
- Supporting / enforcement mechanisms: Hermes inference/tool engine, skill SOPs, `kanban_show`/`kanban_complete`, MCP adapters, read-only Cluster profile, sandbox and GitOps proposal mechanism.
- Closure path: user/event/cron input → model/tool turn → actual observations → agent revises its action or delegates → result/plan/proposal returned to requesting card/chat; another turn may follow upon returned approval.
- Why this is / is not agent-owned: model-driven tool/diagnostic choice occurs in the shipped agent profiles, not in the deterministic dispatcher alone; the third-party Hermes library is a packaged runtime dependency, not an external task owner at this deployment boundary.
- Evidence: README, `agents/platform/SOUL.md`, `agents/cluster/SOUL.md`, configured gateway and AutoOps design (links above).
- Basis: explicit deployment and source-structural execution flow; no live provider exercise.
- Confidence: medium-high.
- Caveats: externally hosted model inference and human GitOps approval are dependencies; no claim of autonomous infrastructure mutation or universal support for all GKE operations.
- Boundary reachability: model/tool turns are invoked by the installed gateway under first-party persona/profile configuration and deliver card results to the same deployed harness.

## S2 — Coordination

- State: C
- Function: attenuate concrete contention between autonomous user-request and background incident/audit workers for the one host-wide Hermes kanban execution cap.
- Disturbance / variety regulated: bursts of event-triage cards previously consumed every worker slot, starving interactive requests; conversely, user fan-out could silence triage.
- Decisive decision or feedback right: classify a card by trusted originating session, reserve at least one slot for each demand class and delay the competing class while the cap is saturated.
- Decision owner: constructor-authored deterministic `stamp_priority`, `ReservedSlot` and dispatcher integration, not a policy-writing LLM or the underlying queued worker itself.
- Supporting / enforcement mechanisms: trusted session context, inherited card priority, dispatcher priority sort, capacity ledger, saturation warnings and queued notification.
- Closure path: competing ready S1 cards → classifier/slot gate → selected next workers run and skipped cards remain ready → the next dispatch tick retries under available capacity, protecting later service from both demand classes.
- Why this is / is not agent-owned: this is a specific inter-S1 resource contention and returned scheduling correction, not generic kanban routing, shared state or delegation; its actual arbitration is constructor-owned.
- Distinct S1 units: interactive chat/Platform/Cluster task workers versus autonomous background event-triage/audit workers, contending for `kanban.max_in_progress` slots.
- Inter-S1 disturbance: background burst displaced interactive work for minutes; reservation prevents either workload class saturating the other's last slot.
- Attenuating coordination relation: priority classification with bilateral slot reservation and worker-claim gates at dispatch.
- Feedback into subsequent S1 behaviour: waiting cards are made runnable when a slot opens and complete with card results; the next tick applies the reservation to later work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the source identifies measurable interference between concurrently autonomous operations and enforces a dedicated attenuation relation across them, with a return into which S1 runs next.
- Evidence: `deploy/docker/patches/kanban_priority.py`, `kanban_ownership.py`, `apply_kanban_scheduling.py` and related tests.
- Basis: explicit code comments, dispatcher wiring and deterministic test surfaces.
- Confidence: high for constructor mode.
- Caveats: not an agent-owned S2, and a reserved slot does not confer independent cross-agent semantic judgment.
- Boundary reachability: the patch is installed inside the distributed Hermes agent image and affects the same deployed worker queue that runs user and background tasks.

## S3 — Inside-and-now control

- State: A
- Function: the Platform Agent integrates current fleet-operational findings and decides how to intervene across scoped Cluster Agent work, including delegating, synthesizing or proposing reviewed GitOps remediation.
- Disturbance / variety regulated: concurrent cluster failures, incomplete diagnostics, fleet-wide observations, cost/patch posture and available operational response paths.
- Decisive decision or feedback right: decide whether and where to dispatch per-cluster diagnosis, reconcile returned RCAs, select an actionable whole-fleet response and return that to a current request or governed change path.
- Decision owner: Platform Agent's model-driven custodial turn for present-time operational control; an engineer separately owns approval/merge of infrastructure change PRs.
- Supporting / enforcement mechanisms: fleet-scope tool, kanban cards, pinned Cluster Agents, fleet collectors, deterministic pending-card guard and submit-suggestion path.
- Closure path: Platform receives fleet task → delegates scoped S1 workers → reads every settled result/metadata → integrates priority and actionable corrections → returns the whole-fleet answer or proposed GitOps PR; actual change awaits authorized review.
- Why this is / is not agent-owned: the Platform Agent chooses synthesis and current operational response across subordinate Cluster Agent work; the orchestrator/queue merely dispatches and enforces worker protocol.
- Whole-system current view: fleet_scope and multi-cluster returned card results, with explicitly acknowledged excluded/unread clusters rather than assuming total visibility.
- Current-control decision scope: agent selects which diagnostics remain its own, which need per-cluster workers, how to combine findings and which reviewable present-time remediation to propose.
- Evidence: Platform `SOUL.md` section 6, Cluster `SOUL.md` handoff contract, AutoOps current incident workflow.
- Basis: explicit role/control contract with structural reachability.
- Confidence: medium; actual end-to-end production decision quality was not exercised.
- Caveats: no claim that the agent can bypass human GitOps approval or that its operating visibility is complete when scopes are unread.
- Boundary reachability: per-cluster cards and results are in the deployed shared board and must settle before the parent Platform card can close; the parent returns its synthesis into the same chat/proposal route.

## S3* — Complementary audit

- State: —
- Function: security/compliance reports, replay/logs and fleet audit observations are ordinary operating evidence, not a separately independent complementary audit authority examining S3's claims.
- Disturbance / variety regulated: unnoticed drift, RBAC issues, incomplete status claims, failed upgrades and technical audit gaps.
- Decisive decision or feedback right: independently verify ordinary management reporting against a complementary access path and return a corrective challenge to whole-system control.
- Decision owner: no distinct first-party independent audit judge established; the Platform Agent itself runs the scheduled audit and reports results.
- Supporting / enforcement mechanisms: Cron fleet-audit collectors, logs, ledger GitHub issues, cluster metadata, security SOPs and report validation.
- Closure path: operating audit job → collector/finding and Platform report → operator or normal Platform remediation; no independent complementary S3* judge that returns a challenge into S3.
- Why this is / is not agent-owned: first-party audit tasks can be valuable S1/S3 instrumentation without constituting organizational independent audit.
- Evidence: `agents/platform/governance/compliance_audit_sop.md`, `stockout_prevention_sop.md`, README, AutoOps design.
- Basis: structural independence/owner test.
- Confidence: medium-high.
- Caveats: external security or independent reviewers may inspect the outputs, outside the assessed deployment.

### Absence scope

- Surfaces inspected: fleet audit jobs, risk collector/ledger, runbooks, diagnostics and customer report flow.
- Plausible first-party paths checked: audit stream as S3* actor; compliance tool as independent access; approval/review PRs as S3*.
- Why no material first-party path remains: the same operational Platform chain collects, judges and proposes; neither complementary organizational independence nor a corrective challenge returned to distinct S3 is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: scheduled risk and upgrade-readiness checks project failures of current fleet resources, but source does not establish a distinct future-environment intelligence function adapting the harness's capabilities.
- Disturbance / variety regulated: capacity stockout risk, planned GKE upgrades, potential quota bottlenecks and current fleet compatibility.
- Decisive decision or feedback right: develop strategic options for prospective external environmental change and return an authorized adaptation to current capability, not merely report likely current infrastructure faults.
- Decision owner: operator/planner chooses future upgrade strategy; Platform Agent executes bounded audit/recommendation SOPs and may propose current-state fixes.
- Supporting / enforcement mechanisms: scheduled stockout-prevention collector, upgrade-readiness brief, risk ranking, GitOps PR proposals and human decisions queue.
- Closure path: forecast-like audit finding → report/issue/fix proposal → external user decision; no general prospective capability redesign and return path shown inside the harness.
- Why this is / is not agent-owned: proactive incident prevention is not by itself a distinct S4 strategic adaptation relation; forecasts here address operations and safe future changes to clusters, not harness identity or future operational capability design.
- Evidence: `stockout_prevention_sop.md`, `upgrade_readiness_brief_sop.md`, Platform `SOUL.md` remediation rules.
- Basis: bounded negative distinction between present-risk management and future-environment strategy.
- Confidence: medium.
- Caveats: a larger provider organization may use these reports to govern future adaptation; the subsystem could grow genuine S4, but hypothetical extensions do not count.

### Absence scope

- Surfaces inspected: schedule, upgrade readiness, stockout prevention, future risk reports and GitOps response gates.
- Plausible first-party paths checked: prediction before capacity shortage, rollout planning and weekly readiness recommendations as prospective intelligence.
- Why no material first-party path remains: these are fixed-scope infrastructure-maintenance checks and externally decided upgrades, not an owned external-and-then strategic capability loop with returned adaptation.

## S5 — Policy and identity

- State: —
- Function: persona identity, least-privilege credentials and GitOps rules constrain agents but do not establish legitimate ultimate organizational identity/policy adjudication owned by the deployed runtime.
- Disturbance / variety regulated: unauthorised cluster mutation, secrets exposure, repo write permissions, user approvals and policy mismatches.
- Decisive decision or feedback right: resolve a contested ultimate organizational purpose/identity or constitutional policy and return the binding decision into current operations.
- Decision owner: human operator/maintainer sets the identity and security policy; runtime enforces chosen RBAC/GitOps boundaries and model follows static instructions.
- Supporting / enforcement mechanisms: SOUL.md personas, Kubernetes RBAC, gVisor sandbox, credential broker, GitOps-only PR path, approval buttons and tool refusals.
- Closure path: externally authored policy/approval → runtime constrained request or PR proposal; no autonomous legitimate S5 matter → adjudication → returned identity-level policy revision.
- Why this is / is not agent-owned: a 'Platform Custodian' persona and PR safety gates are not, by their names, sovereign identity-level decision authority.
- Evidence: README governance/isolation, Platform/Cluster SOUL, `kanban_ownership.py`, AutoOps human approval design.
- Basis: explicit owner/enforcement separation.
- Confidence: high for the negative runtime boundary.
- Caveats: human higher-level S5 may govern the deployment, but parent mode is not asserted without a specific in-boundary ultimate-policy return.

### Absence scope

- Surfaces inspected: personas, tool grants, RBAC, policy broker, human PR approval route and agent scope rules.
- Plausible first-party paths checked: Platform Custodian identity, infrastructure policy and human approval as parent S5 mode.
- Why no material first-party path remains: these are supplied and enforced constraints; a distinct legitimate identity/ultimate-policy adjudicator and returned constitutional change were not evidenced.

## Recursion

Per-cluster Hermes profiles are operational units with isolated work scopes. The Platform Agent integrates their current reports at the fleet recursion level; the Planning Agent is the front-door orchestrator. The Kubernetes reconciliation controllers beneath the deployment are deterministic infrastructure, not extra model-owned S1 units simply because they reconcile resources.

## Variety and escalation

Agent tool use absorbs some environment and task variety; model-backed diagnosis traverses errors and evidence. Constructors dampen competing worker traffic with reserved slots and configure credential/tool bounds. The Platform Agent synthesizes per-cluster feedback into actionable current operational proposals. Changes to live GitOps-managed infrastructure remain protected by the outside engineer's review decision; a blocked card returns the missing permission rather than circumventing it.

## Evidence gaps

- Static inspection at the frozen commit only. No live GKE cluster, paid provider call, cloud credential use, model E2E, deployed throughput measurement or external security audit was performed.
- Runtime behavior relies on packaged Hermes dependency and specific deployment/configuration; positive S1/S3 denote the supported installed mode, not source ownership of Hermes internals or a performance certificate.
- S2 is bounded to demonstrated worker-slot interference. Other multi-agent routes, telemetry, read-only configuration and shared memory do not automatically inherit S2 or S3* status.

## Assessment summary

**Proposed disposition: `included`.** The shipped composed Hermes-based deployment has model-guided operational workers (S1=A), concrete constructor-owned protection for competing user/background S1 worker capacity (S2=C), and an agent-owned fleet-level current-control synthesis/response path through the Platform Agent (S3=A). Independent S3* audit, strategic S4 adaptation and ultimate S5 identity-policy closure are not established at this boundary. Vector: **A · C · A · — · — · —**.
