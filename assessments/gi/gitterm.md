---
harness_id: gitterm
project_name: GitTerm
repository: https://github.com/OpeOginni/gitterm
review_ref: 1465ca1b3683a24966ce0815129742460b16c13e
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# GitTerm

## Review boundary

- System in focus: MIT first-party GitTerm cloud workspace control plane plus shipped TypeScript SDK, OpenCode runtime adapters and Cloudflare plan-execution loop; hosted OpenCode model internals, cloud infrastructure policies and user-owned repositories are external dependencies.
- Purpose and identity: provision coding-agent workspaces on supported compute/sandbox providers, submit prompts to OpenCode, relay pending permissions/questions, manage run/workspace lifecycle and account resource bounds.
- Relevant environment: arbitrary repository tasks, model errors, runtime readiness, provider outages, lost session subscriptions, missing operator approvals, idle compute waste, quota exhaustion and timed-out/expired sandboxes.
- Standard-distribution boundary: `packages/api` run/agent-loop/workspace services, `packages/agent-runtime` provider-independent adapters, `packages/sdk` client and event relay, `apps/worker` lifecycle reaper, plus CLI/dashboard; not unrelated benchmarks and provider implementation internals.
- Credited operating / distribution surfaces: `runs.create` → runtime `createSession/prompt` → external model-backed coding work; optional plan-file Cloudflare agent loop; first-party workspace-wide quota/idle/retention controller and deterministic run admission/termination.
- Adjacent first-party surfaces excluded from ownership: browser TTYD terminal, share links, credential brokerage, webhook transport, database schemas, provider-specific container setup, benchmarks and API watchers do not by themselves create S2/S3* or strategic S4/S5 rights.
- First-party operating / deployment modes considered: hosted/self-hosted workspace API plus SDK; direct-provider SDK; optional automated plan-file loop on Cloudflare. Managed quota enforcement is conditional on deployment features, whereas caller lifetime/explicit stop paths remain available.
- Recursion level: one cloud coding-agent workspace/service and current managed workspace fleet; Opencode sessions are externally implemented task actors, not the control plane's metasystem ownership.
- Reviewed revision: `1465ca1b3683a24966ce0815129742460b16c13e`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

GitTerm creates and exposes remote OpenCode sandboxes. Its account-scoped API creates an agent run, waits for workspace/runtime readiness, optionally continues a previous native session, creates a runtime session, starts a prompt and watches normalized messages and pending input. The SDK yields lifecycle events and hands a permission or question to the registered human callback; without one, it stops with explicit `INPUT_REQUIRED`. Separately, an optional agent-loop mode asks a cloud sandbox worker to implement the next item in a user-supplied plan and commit/push, bounded by a configured run count and user quota. A periodic idle reaper queries all relevant workspaces and applies pause/termination rules based on activity, quotas, plan retention and caller lifetime. These are different functions: agentic task execution is externally model-decided, while the current workspace resource-control gate is platform-authored.

Pinned primary evidence:

- [Product boundary, lifecycle and hosting/providers](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/README.md)
- [SDK run API, permission/question relay, direct-provider and managed mode](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/sdk/README.md)
- [Run creation and OpenCode session/prompt dispatch](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/api/src/service/agent-run/index.ts)
- [Run routes: create/list/get/respond/cancel and lifecycle stream](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/api/src/routers/run.ts)
- [SDK watch/result and callback/INPUT_REQUIRED paths](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/sdk/src/runs.ts)
- [Provider-independent agent statuses, pending permissions and questions](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/agent-runtime/src/contract.ts)
- [OpenCode runtime normalization and model tool events](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/agent-runtime/src/opencode.ts)
- [Plan-file agent loop: optional automation/max runs, pause/resume and run quota](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/api/src/routers/agent-loop/index.ts)
- [Cloudflare agent run provision and callback setup](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/api/src/service/agent-loop/index.ts)
- [One-plan-feature agent prompt, explicit commit/push and completion marker](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/api/src/providers/cloudflare/index.ts)
- [Multi-workspace idle/quota/retention/lifetime reaper](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/apps/worker/src/idle-reaper.ts)
- [User-plan activity, quota and idle-workspace selection](https://github.com/OpeOginni/gitterm/blob/1465ca1b3683a24966ce0815129742460b16c13e/packages/api/src/utils/metering.ts)

## Operational model

User/integrator provisions a repository workspace and supplies a coding prompt or plan. GitTerm dispatches a native OpenCode model session and continuously reconciles run lifecycle/pending input; the external model selects individual code actions. A question or risky permission is returned to the user/SDK subscriber and only resumes with an answer. The first-party fleet controller observes activity/quota/retention and pauses or terminates workspaces based on configured rules. The platform contains no independent substantive code auditor, long-horizon model-directed future platform adaptation or identity-policy authority of its own.

## S1 — Operations

- State: A
- Function: execute repository coding tasks via a model-driven OpenCode agent inside a supported provisioned remote workspace.
- Disturbance / variety regulated: unknown codebase states, task requirements, implementation errors, model/provider variability and missing context.
- Decisive decision or feedback right: choose coding edits, shell/tool interactions and task responses to a submitted prompt or next plan item.
- Decision owner: configured external OpenCode model agent running in a first-party GitTerm-created and addressed session; its internals are not transferred as GitTerm management rights.
- Supporting / enforcement mechanisms: `createAgentRun`, `runtime.createSession`, `runtime.prompt`, SDK run events, terminal/browser workspace access, provider adapter and input callback relay.
- Closure path: user-specified repository/prompt → live model coding session → tool/messaging events and results → completed/failed/awaiting-input response or next plan iteration.
- Boundary reachability: account-authenticated `run.create` invokes `createAgentRun`, creates a native session and calls `prompt`; the SDK exposes the same route, while optional Cloudflare loop starts an agent run with a plan-file task instruction.
- Why this is / is not agent-owned: actual choice of implementation commands and edits is not specified by the GitTerm queue; first-party orchestration explicitly composes a real external coding agent for the selected task.
- Evidence: pinned `agent-run/index.ts`, OpenCode adapter, SDK README and Cloudflare loop prompt.
- Basis: reachable hosted/sandboxed model-agent execution surface.
- Confidence: high on dispatch and action ownership, not actual correctness.
- Caveats: no live remote workspace, compute provider or model session was executed for this source review.

## S2 — Coordination

- State: —
- Function: no first-party adaptive mediation of ongoing peer S1 work-unit interference is demonstrated.
- Disturbance / variety regulated: multiple users, shared workspace access, concurrent SDK watchers and cloud provider instances can contend, but implementation treats these as authorization, transport or run serialization issues.
- Decisive decision or feedback right: API limits continuation of a native session while previous run is active; Redis watcher leases avoid duplicate lifecycle observers; user-initiated sharing enables teammates to access a workspace.
- Decision owner: constructor-written concurrency checks, scoped tokens and transport lease service, not a peer-unit conflict negotiator.
- Supporting / enforcement mechanisms: active-run status guard, idempotency key, cluster watcher lease, workspace share permission and account routing.
- Closure path: a run is rejected/serialized or a watcher elected; no inter-agent operational conflict → adaptive coordination decision → changed future peer relations is established.
- Why this is / is not agent-owned: multiple client connections or compute instances are not independent VSM S1 units whose contradictions GitTerm resolves; neither is an operator's manual share link.
- Evidence: pinned `agent-run/index.ts`, `agent-run/cluster.ts`, SDK README and product README.
- Basis: scoped negative.
- Confidence: medium-high.
- Caveats: an external collaborative coding team may coordinate its members outside GitTerm.

### Absence scope

- Surfaces inspected: multi-provider workspaces, run/session continuation, cluster watcher leases, dashboard sharing, agent loops and SDK lifecycle events.
- Plausible first-party paths checked: cloud workers as peer units, simultaneous runs as competing departments, shared workspace as a coordination institution and provider routing as S2.
- Why no material first-party path remains: these are resource containment and communication paths, without a shipped agent/work-unit interference feedback and corrective relationship across independent continuing work mandates.

## S3 — Inside-and-now control

- State: C
- Function: preserve current workspace fleet viability and control active compute/run commitments against idle time, quota, retention and caller lifetime.
- Disturbance / variety regulated: zombie or unbounded runtimes, exhausted user plans, stale idle sessions, abandoned paused resources, multiple simultaneous loop runs and failed runtime startup.
- Decisive decision or feedback right: pause idle/quota-exhausted workspaces, terminate beyond retention/lifetime, enforce no active same-loop run and max loop count, cancel/settle abandoned runs.
- Decision owner: first-party deterministic API and worker control logic (`idle-reaper`, metering, workspace service and loop gates), under operator/admin-selected settings.
- Supporting / enforcement mechanisms: account/workspace DB state, Redis activity signal, usage sessions, configured plan thresholds, `getIdleWorkspaces`/`getQuotaExceededWorkspaces`/`getLongTermInactiveWorkspaces`, internal pause/terminate endpoints and run state machine.
- Closure path: current fleet activity/usage/plan state → rule-based classification of excess/idle/expired resources → API pause/terminate and usage bookkeeping → next fleet poll or explicit resume/cleanup.
- Boundary reachability: scheduled `idle-reaper` runs query internal endpoints and issue actual `pauseWorkspaceInternal`/`terminateWorkspaceInternal` mutations; the plan-loop router enforces max-runs/active-run gates and quota before dispatch.
- Why this is / is not agent-owned: resource acceptance, pause, resume and termination are specified by constructor thresholds and user policy; the external coding model has no autonomous control-plane authority over other workspaces.
- Whole-system current view: active/paused/expired managed workspaces and their user quotas and activity across the deployment, plus run-count/current status per plan loop.
- Current-control decision scope: sandbox resource and execution lifecycle commitments, not business-level goal prioritization or final code acceptance.
- Evidence: pinned reaper, metering, agent-loop router and SDK lifecycle.
- Basis: closed first-party cross-workspace current-resource regulation path.
- Confidence: medium-high for managed mode, narrower self-hosted case.
- Caveats: idle and quota features may be off in self-hosted deployments; explicit caller lifetime and run gates are still separate constructor paths, and quota-driven pause is not an evaluation of code quality.

## S3* — Complementary audit

- State: —
- Function: no independent substantive inspection challenges the coding agent's implementation claims or the current resource manager's view of output quality.
- Disturbance / variety regulated: code regressions, missed user requirements and false agent success claims remain outside the platform's own independent audit function.
- Decisive decision or feedback right: SDK returns native model messages and status; no separately governed read-only code reviewer or correction authority is established by these transports.
- Decision owner: OpenCode runtime and its status watcher supply routine reports, while human collaborators may inspect results externally.
- Supporting / enforcement mechanisms: session snapshot, message/tool normalization, run lifecycle events, idempotency and event callbacks.
- Closure path: model result → normalized status/stream → human or caller; no distinct artifact sampling/critical findings → S3 corrective response → re-audit loop.
- Why this is / is not agent-owned: watcher reconciliation is operational bookkeeping, and a prompt like “review PR” still uses the same ordinary run without a first-party independent challenge mandate.
- Evidence: pinned `agent-runtime/opencode.ts`, `agent-run/watcher.ts`, `packages/sdk/src/runs.ts` and README.
- Basis: bounded independence negative.
- Confidence: high.
- Caveats: caller can build an external reviewing integration with the SDK, but it is not shipped as mandatory or a distinct first-party ownership path.

### Absence scope

- Surfaces inspected: run status/snapshot reconciliation, SDK permission/question callbacks, OpenCode tool data, plan loop and workspace lifecycle reaper.
- Plausible first-party paths checked: runtime watcher as audit, provider health as external truth, manual PR review prompt as S3* and result telemetry as quality verification.
- Why no material first-party path remains: all either implement the same run or account/compute administration, without independent evidence access and corrective quality-judgment return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no environmental/future option-building loop to adapt GitTerm's later coding capability or platform strategy is present.
- Disturbance / variety regulated: changing provider capabilities, repositories and model ecosystems are handled through configured integrations and current user actions rather than first-party strategic sensing.
- Decisive decision or feedback right: user chooses providers/models/plan file and may run another feature iteration; no agent is commissioned to generate future capability options from an external horizon and feed adoption to S3.
- Decision owner: external operator and fixed first-party plan/loop rules; coding agent chooses the next current feature, not the platform's future governance/capability portfolio.
- Supporting / enforcement mechanisms: provider registry, model settings, plan/progress file, bounded `maxRuns`, callback completion and git commit path.
- Closure path: current plan file → one implementation run → updated progress/commit → possible next run; no scanned future environment → prospective alternative design → S3 option selection → changed future system capability.
- Why this is / is not agent-owned: iterative implementation of a static user-provided product plan is continuing S1 delivery, not outside-and-then organizational intelligence.
- Evidence: pinned plan-loop router, `agent-loop` service, Cloudflare `generatePrompt`, product README.
- Basis: scoped negative despite real agentic iterations.
- Confidence: medium-high.
- Caveats: caller may program future research via custom SDK prompts, but an arbitrary caller-authored loop is not inherited by this repository.

### Absence scope

- Surfaces inspected: automated agent loop, progress files, provider registry, workspace lifecycle, integrations and model credential management.
- Plausible first-party paths checked: repeated runs as S4 learning, selected model/provider as adaptation, callback completion markers as future planning and provider compatibility testing as environmental monitoring.
- Why no material first-party path remains: no owned prospective option generation based on future-relevant environment analysis with a return to revise platform capability is implemented.

## S5 — Policy and identity

- State: —
- Function: ultimate mission, authorization, risk appetite and repository legitimacy remain with user/admin/provider governance outside GitTerm's agent runtime.
- Disturbance / variety regulated: credential scope, permission approvals, workspace access, private repository rights and acceptable cloud spending.
- Decisive decision or feedback right: user/admin configures providers, quota plans and access; SDK handler/human answers an agent's permission request; first-party code enforces the returned choice rather than deciding constitutional purpose.
- Decision owner: external account owner, admin, credential provider and (for individual questions) the SDK's human callback.
- Supporting / enforcement mechanisms: authenticated account routes, scoped workspace token, requested permission reply, plan settings, quota boundaries and workspace lifecycle.
- Closure path: user-selected purpose/authorization → agent run → per-tool permission or question → handler response → resumed/blocked run; no identity-level dilemma → legitimate parent adjudication → mission-policy decision → binding return to subsequent system operation is furnished as a first-party S5 loop.
- Why this is / is not agent-owned: a user granting a shell command or provisioning a cloud credential exercises operational permission, not a GitTerm-owned right to decide ultimate organizational identity.
- Evidence: pinned SDK README, `runs.ts`, API run route, product README and credential-security docs.
- Basis: bounded negative at declared workspace-service recursion.
- Confidence: high.
- Caveats: parent organization and user may have an external S5; this review does not inherit it.

### Absence scope

- Surfaces inspected: workspace user/admin configuration, provider credential scope, run input callbacks, account quotas and automated plan-loop settings.
- Plausible first-party paths checked: credential policies as S5, operator permission response as parent return, auto-termination as constitution and plan-file instructions as mission identity.
- Why no material first-party path remains: these constrain current execution or resources under a user-defined mandate and do not adjudicate the ultimate purpose of the system.

## Recursion

An OpenCode coding agent may itself be a rich viable system, but GitTerm does not inherit its internal management or policy. The platform governs available sandboxes and their current resource commitments; clients, cloud providers and listener instances are infrastructure units, not S2 peers by default.

## Variety and escalation

Runtime adapters/credential routing amplify provider coverage; OpenCode handles coding variety; statuses, idempotency, workspace waits, permission prompts, idle/usage limits and cleanup rules attenuate operational risks. A blocked permission can be returned to an external human handler, and exhausted quota pauses compute. No internally governed independent quality auditor or future strategy channel is inferred from either route.

## Evidence gaps

- Frozen-source review only; no remote sandbox, external OpenCode session, user credential, cloud billing path or real provider execution was run.
- S3=C applies to constructor-managed resource control of current workspaces, not model-led strategy or source-code quality; managed quota enforcement depends on deployment mode.
- SDK availability for callers to build custom supervisors/auditors is not evidence that such managers are implemented or owned by GitTerm itself.

## Assessment summary

Proposed `included`: first-party composed model-backed coding operations (S1=A) and constructor-defined multi-workspace/run lifecycle and quota control (S3=C). Shared access, lifecycle telemetry, iterative plan execution and user permissions do not establish S2, S3*, S4 or S5. Vector **A · — · C · — · — · —**.
