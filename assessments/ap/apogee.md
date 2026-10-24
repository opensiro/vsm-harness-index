---
harness_id: apogee
project_name: Apogee
repository: https://github.com/airiclenz/apogee
review_ref: 9fafafb10853dff9eb8d88425d3cf846b7606fb4
reviewed_at: 2026-10-21
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-21
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Apogee

**Canonical general assessment.** Index serial batch [#1842](https://github.com/opensiro/vsm-harness-index/issues/1842) row 2, immutable candidate intake [#860](https://github.com/opensiro/vsm-harness-index/issues/860). Judgments below are limited to the source-shipped supported runtime at the exact frozen commit, not to production adoption or outcomes. The inspection machine did not expose a Go toolchain: present unit tests were read as source evidence but **not run** in this assessment.

## Review boundary

- System in focus: Shipped Apogee Go engine and its TUI, headless and daemon consumer modes, provider-backed coding loop, tool execution, model-driven subagent delegation, context/session/undo state, workflow and reaction integrations.
- Purpose and identity: A self-hosted coding agent for local or remote LLMs performing tool-guided source editing, diagnosis and verification under configurable user authorization boundaries.
- Relevant environment: User requests and intervention, source trees/commands, test outcomes, configured local/cloud model endpoints, OS confinement, optional MCP and schedules; the operator owns model credentials and local policies.
- Standard-distribution boundary: Public `apogee` module, `cmd/apogee` application with interactive/headless/daemon execution, `internal/agent` engine, `internal/workflow` orchestrator, built-in tools/reactions/sessions/security. Optional first-party recipe and model-enabled fan-out are included **only in their documented configured/available modes**, not presumed part of every basic turn.
- Credited operating / distribution surfaces: `apogee.go`; `internal/agent`; `internal/domain`; `internal/provider`; `internal/tools`; `internal/security`; `internal/workflow`; `internal/schedule`; `internal/session`; `internal/reactions`; `cmd/apogee`; shipped configuration/manual.
- Adjacent first-party surfaces excluded from ownership: Source-maintainer CI, benchmarks/bench harness and model-readiness probes, developer design documents, example fixtures, simulated evaluations, documentation-only assertions, contributor/release governance and externally installed agents. Bench data can corroborate a code-path property but is not a live organizational decision owner.
- First-party operating / deployment modes considered: Interactive terminal, headless, foreground daemon schedules, regular model/tool loop, parallel subagents, optional `fan_out` / `workflow` model tools, recipe workflow execution, OS-confined Auto mode and human-gated modes.
- Recursion level: One Apogee installed coding-agent system with model-guided task agents and optional concurrent delegated child agents. Multiple separately installed users or benchmark workers are not one automatically governed enterprise organization.
- Reviewed revision: `airiclenz/apogee@9fafafb10853dff9eb8d88425d3cf846b7606fb4`.
- Observation date: 2026-10-21.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The public `apogee.go` API exposes one embeddable `Agent`, its `New`/`Resume`, `Submit`/`Step`/`Run`, mode changes, snapshots and delegated execution. First-party `internal/agent` owns the model-call/typed-tool/observation loop while `internal/domain` defines its contracts; external model endpoints are inference dependencies. The TUI and headless/daemon frontends drive that same agent rather than wrapping an externally owned coding tool. [apogee.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/apogee.go); [internal/agent/agent.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/agent.go); [internal/agent/loop.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/loop.go); [cmd/apogee/headless.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/cmd/apogee/headless.go); [docs/manual/daemon.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/docs/manual/daemon.md).

Apogee's own dispatch can run nested model-guided child agents concurrently. A first-party shared `queuedApprover` prevents **simultaneous child approvals competing for one human prompt slot**, while `serialEventSink` linearizes child-event writes to a shared host sink. The engine uses a bounded delegation worker pool; test `TestFanOut_ConcurrentChildApprovalsQueueAndNameTheirChild` constructs two concurrent child tasks, ensures the common host Approver receives no overlapping requests, and checks verdict delivery per child. These code/tests support a narrow deterministic S2 interference-damping constructor, not a higher coordination planner. [internal/agent/construct.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/construct.go); [internal/agent/dispatch.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/dispatch.go); [internal/agent/approvalqueue_test.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/approvalqueue_test.go).

Optional workflows/recipes split task items among bounded helper agents, save their receipts, and may add an adversarial per-item verification stage. The workflow checker tests an item output under the task contract; it does not automatically own complementary audit of a whole-current manager. Schedules run predefined human-authored prompts/recipes; OS modes and Reactions enforce safety/repair along coding work, but no manager-level autonomy or parent constitutional authority is inferred merely from those mechanisms. [internal/workflow/runner.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/workflow/runner.go); [internal/agent/workflowcall.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/workflowcall.go); [internal/schedule/schedule.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/schedule/schedule.go); [internal/security/fence.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/security/fence.go); [docs/manual/workflows.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/docs/manual/workflows.md).

## Operational model

The main agent selects code-reading/editing/test/tool actions and adjusts to returned results. Delegated model-driven child agents act as separate S1 operational work cells in the supported parallel mode. Deterministic runtime code bounds and coordinates their access to one shared approval UI (and one event sink), avoiding sibling interference and returning each distinct human decision to the correct waiting child. The user owns autonomy/confinement postures and may intervene during an exchange; these are effective constraints on S1, not proof of a separate full current-control or ultimate-policy function.

## S1 — Operations

- State: A
- Function: Model-guided coding work selects and executes file/shell/git/search/test operations, reads observations, retries or revises actions and returns results.
- Disturbance / variety regulated: Novel source-code changes, test/tool failures, uncertain diagnosis, local workspace edits and shifting user instructions.
- Decisive decision or feedback right: Choose task-semantic tool calls and further corrective coding steps from current observations in the agent's real first-party loop.
- Decision owner: Provider-backed agent cognition operating through Apogee's own engine. Provider server hosts inference but does not provide an external prebuilt agent workflow or inherited organizational control.
- Supporting / enforcement mechanisms: Agent engine, tool registry and dispatch, mode/confinement gate, reactions/floor guards, session persistence, provider adapters and human confirmation of riskier actions.
- Closure path: User instruction → `Agent.Submit`/`Run` or `Step` → provider response → agent-selected tool calls → first-party tool execution → returned result plus model-visible state → next decision or completion, persisted for later session use.
- Boundary reachability: Shipped `cmd/apogee` TUI/headless/daemon frontends call the public `Agent` facade, backed by `internal/agent`; local/remote model drivers are explicitly supported. Model-directed tool feedback is first-party assembled, not a benchmark-only helper.
- Why this is / is not agent-owned: Removing the model-guided agent while keeping deterministic guards, tools and TUI leaves no actor to choose arbitrary coding fixes in response to observed output. No success rate or unattended delivery guarantee is inferred.
- Evidence: [apogee.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/apogee.go); [internal/agent/agent.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/agent.go); [internal/agent/loop.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/loop.go); [internal/agent/dispatch.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/dispatch.go); [README.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/README.md).
- Basis: explicit and structural.
- Confidence: high for first-party reachability, not live task performance.
- Caveats: Auto mode is bounded by the configured platform/sandbox; no assumption that every environment supports unattended file writes. No source Go tests executed here.

## S2 — Coordination

- State: C
- Function: Protect a common human approval/request surface from overlapping requests by **distinct simultaneously running child coding agents**, ensuring one child at a time uses the same prompt slot and each receives its own verdict.
- Disturbance / variety regulated: Two sibling S1 agents concurrently request separate approvals from a single non-concurrent host prompt/Approver; absent first-party mediation, prompts overlap, one reply channel may be orphaned and a child can remain blocked or receive the wrong permission result.
- Decisive decision or feedback right: Enqueue contending children on the shared prompt slot; admit only one approval/question at a time, then release it after an answer/cancellation and return that decision to the correct waiting child.
- Decision owner: Deterministic first-party `queuedApprover`/PromptSlot construction; human operator still decides whether each request is allowed, while the model children own their coding intentions. Thus `C`, not autonomous S2 policy `A`.
- Supporting / enforcement mechanisms: `construct.go::queuedApprovals`, `queuedApprover.Approve`, shared `domain.PromptSlot`, `approvalCache` re-check, parent/child run IDs, `runPool` delegation worker cap and `serialEventSink`.
- Closure path: Concurrent child 1 and child 2 reach human approval simultaneously → first-party prompt slot admits one, delays other → human verdict flows to specific first child → slot releases → second child's approval is presented or satisfied by safe remembered session rule → its verdict flows back into *its* coding action. Shared event sink delivers serial identified outcomes to the parent session.
- Boundary reachability: `internal/agent/construct.go::newAgent` wraps `cfg.Approver` and `cfg.Events` for standard agent construction; depth-0 model-selected fan-out dispatch uses independently running nested `Agent` units against these shared guarded seams. It is a supported in-product parallel subagent mode, not an external workflow.
- Why this is / is not agent-owned: The concurrency collision and queue relation remain deterministically enforced if model deliberation is removed, but the child S1 work itself would disappear. User approval owns permission, not the scheduling of contention, and no distinct model coordinating actor is fabricated.
- Evidence: [internal/agent/construct.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/construct.go); [internal/agent/dispatch.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/dispatch.go); [internal/agent/approvalqueue_test.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/approvalqueue_test.go); [internal/agent/askqueue_test.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/askqueue_test.go); [docs/manual/workflows.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/docs/manual/workflows.md).
- Basis: structural, with explicit first-party adversarial concurrency regression (read, not run).
- Confidence: high for constructor path, bounded to the shared prompt-surface collision.
- Caveats: Host-prompt serialization and event-sink linearization do not mean agents exchange task strategy or coordinate source edits. Generic parallel delegation or workflow width alone is not the S2 witness.

- Distinct S1 units: Different model-guided subagent instances running concurrently as separate child `Agent` engines within one parent Apogee session.
- Inter-S1 disturbance: Simultaneous `Approve`/question requests to a single shared human prompt surface can interleave, race over one reply channel, block or misroute a sibling's approval.
- Attenuating coordination relation: One inherited queued Approver protects the shared `domain.PromptSlot`, and the event sink serializes shared event delivery across child runs.
- Feedback into subsequent S1 behaviour: Human response releases the common prompt, enabling another previously waiting child to receive its own decision and proceed/deny its tool action; correctness of per-child returned outcomes is asserted by `TestFanOut_ConcurrentChildApprovalsQueueAndNameTheirChild`.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: This implementation addresses a concrete inter-S1 **interference failure mode** of simultaneous sibling decisions over one exclusive human prompt, and its release/returned-result path regulates subsequent execution of the *competing* child. Merely having children, tool dispatch, UI or a shared mutex elsewhere would not establish it.

## S3 — Inside-and-now control

- State: —
- Function: No independently established whole-installed-system current-control owner exercising substantive global commitments/priorities/resource-allocation decisions with returned regulation of all S1 units.
- Disturbance / variety regulated: Work backlog, simultaneous tasks, schedule overload, shared model capacity, safety warnings, user interruptions.
- Decisive decision or feedback right: Assess the whole present organization and decide how shared commitments, priorities or resources must be revised and returned to active S1 work.
- Decision owner: Not established in shipped current operations at this recursion. Users set schedules/modes and direct individual sessions; deterministic width/overlap guards constrain subagents.
- Supporting / enforcement mechanisms: TUI and session views, foreground daemon schedules, per-task workflow Runner, model/server profile selection, caps, human approval and interruption.
- Closure path: Per-task steering, queueing, schedules and status reporting affect a particular work item or shared prompt surface; no first-party authority dynamically controlling current cross-S1 resource/commitment tradeoffs from a whole-system view was identified.
- Boundary reachability: No positive S3 state; project-wide dashboard/daemon features are inspected as plausible paths, not credited without management return.
- Why this is / is not agent-owned: An agent deciding its task plan or a scheduler firing human-authored prompts is not the owner of whole-system current control at the declared recursion.
- Evidence: [internal/schedule/schedule.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/schedule/schedule.go); [internal/agent/agent.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/agent.go); [internal/workflow/runner.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/workflow/runner.go); [docs/manual/daemon.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/docs/manual/daemon.md); [docs/manual/sessions.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/docs/manual/sessions.md).
- Basis: bounded source review.
- Confidence: moderate.
- Caveats: A higher-level deployed operations organization could be built using embeddable Apogee; none was imported.

### Absence scope

- Surfaces inspected: First-party supervisor and TUI/headless/daemon controls, workflow runner, session state, model mode/permissions and user steering.
- Plausible first-party paths checked: Single-parent agent with parallel tasks, recurring daemon jobs, run statuses, cross-task priority arbitration and explicit user intervention.
- Why no material first-party path remains: The inspected paths control task dispatch/caps or implement user-specified local operations; they do not establish a whole-current organization manager with substantive decision over collective obligations/resources and feedback into independently continuing S1 cells.

## S3* — Complementary audit

- State: —
- Function: No separately organized complementary independent access that challenges the normal S3 manager's account of operational reality and returns findings for corrective whole-current control.
- Disturbance / variety regulated: Incorrect helper reports, false coding completion, inaccurate CI/tool outputs, mistaken session status.
- Decisive decision or feedback right: Independently inspect operational reality beyond routine agent and manager reporting, issue a corrective finding, and return that into whole-current management.
- Decision owner: Not established. Optional workflow `verify` starts a separate adversarial helper to refute an item's *task report*, but no distinct S3 manager/account, independent field access mandate and corrective whole-current governance loop is documented.
- Supporting / enforcement mechanisms: Workflow verify stage, tool/test outputs, reaction/floor guards, receipt schema checks, session transcript and user review.
- Closure path: A verification helper can label workflow items `confirmed/refuted/unclear`, and a parent can read task-level feedback. This is task QA; it is not a demonstrated independent audit-to-S3 management corrective return at the assessed recursion.
- Boundary reachability: No positive S3* state is claimed. Verify exists in an explicitly enabled/specified workflow, not a standing independent organizational audit.
- Why this is / is not agent-owned: Distinct reviewer model identity is insufficient by itself without complementary access and an attributable corrective relation to current management; deterministic receipt validation also does not create an independent auditor.
- Evidence: [internal/workflow/runner.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/workflow/runner.go); [internal/workflow/stages.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/workflow/stages.go); [docs/manual/workflows.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/docs/manual/workflows.md); [internal/reactions/runner.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/reactions/runner.go).
- Basis: structural bounded negative.
- Confidence: moderate.
- Caveats: Real deployments might design a supervisor whose operational claims an independent Apogee agent audits, but that is not evidenced by the generic distributed engine.

### Absence scope

- Surfaces inspected: First-party workflow verify/retry/merge, receipt/store and task status, reactive verification, regular test/tool output, TUI transcripts.
- Plausible first-party paths checked: Adversarial verifier with a separate view, independent observer/field channel, accepted findings that cause S3 whole-current intervention rather than merely flagging a task result.
- Why no material first-party path remains: Available separate helpers refute *per-item results* inside the same task workflow and do not expose independent organizational inspection with returned management correction. No shipped S3-specific audit relation survives this boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped agent organization loop that takes external/prospective changes, develops strategic capability adaptations and returns accepted options into later operating machinery.
- Disturbance / variety regulated: New model/tool capabilities, environment change, repeated coding failures, changing future workloads.
- Decisive decision or feedback right: Generate and select future capability changes in response to external conditions and incorporate the selection into ongoing operation.
- Decision owner: Not established in the installed product; the user may switch models/skills or edit schedules, and developers may improve guarded behavior through separate benchmarks/releases.
- Supporting / enforcement mechanisms: Live model/profile switching, reaction/floor guard configuration, task- and workflow-level retries, session persistence and producer-maintainer evaluation materials.
- Closure path: Changing configured model or scheduled task can alter later execution, but no complete first-party future-environment sensing → strategic alternative → adopted capability change loop was found within the installed agent recursion.
- Boundary reachability: No positive S4 actor/constructor path attributed to the shipped standard distribution.
- Why this is / is not agent-owned: Fixed reactions correcting malformed tool calls and workflow retries are operational S1 recovery, not future adaptation; separate maintainer benchmark/evolution artifacts remain outside this boundary.
- Evidence: [internal/agent/reactions.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/reactions.go); [internal/agent/floorguards.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/floorguards.go); [internal/agent/setprofile.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/setprofile.go); [docs/manual/reactions.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/docs/manual/reactions.md); [README.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/README.md).
- Basis: bounded source review.
- Confidence: moderate.
- Caveats: Plug-ins, operator choices and future new versions may introduce adaptation without changing this frozen assessment.

### Absence scope

- Surfaces inspected: Live model switching, adaptive per-request floor guards, model/tool provider configuration, workflow retries, daemon schedules, project sessions, maintainer-eval descriptions.
- Plausible first-party paths checked: External trend/incident collection; generation and selection of new operating strategies/rules; adoption of an evaluated option back into current capability without importing an outside operator's custom process.
- Why no material first-party path remains: Observed mechanisms recover present work or enact already chosen user configuration. No active installed capability evolution choice/return at organization recursion is evidenced.

## S5 — Policy and identity

- State: —
- Function: No separately organized legitimate ultimate-purpose/identity policy decision-right and returned constitutional governance path within the installed Apogee agent organization.
- Disturbance / variety regulated: Changing the agent organization's ultimate purpose, defining who can authorize root operating commitments, conflicts between policy identity and lower-level tools.
- Decisive decision or feedback right: Authoritatively adopt/revise an organization's identity/ultimate policy and return that rule into agent operations.
- Decision owner: Not established as Apogee S5 `A`, `C` or completed parent `P` mode. Users choose risk modes/model providers and approve actions; these are local operating and permission decisions without proof of a first-party ultimate-policy governance process.
- Supporting / enforcement mechanisms: OS confinement, read/write guardrails, user approvals, configuration/security policy, signed or verified artifacts and action traces.
- Closure path: An operator's configured constraints can govern individual actions, but no traceable identity-policy issue → legitimate ultimate authority → authoritative return to entire agent organization is shipped as a function.
- Boundary reachability: No positive S5 state credited from configurable permission or tool-selection switches.
- Why this is / is not agent-owned: Model task choices and static security controls have no legitimate authority to redefine the harness's purpose, and the user-owned application configuration is not inherently a parent governance channel.
- Evidence: [internal/security/guard.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/security/guard.go); [internal/security/fence.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/security/fence.go); [internal/agent/gate.go](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/internal/agent/gate.go); [docs/manual/configuration.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/docs/manual/configuration.md); [README.md](https://github.com/airiclenz/apogee/blob/9fafafb10853dff9eb8d88425d3cf846b7606fb4/README.md).
- Basis: bounded source review.
- Confidence: moderate.
- Caveats: A user organization could externally govern Apogee; its undisclosed institutional S5 must not be borrowed.

### Absence scope

- Surfaces inspected: Default runtime operating modes, OS sandbox and approval paths, config, TUI/daemon scheduling, user-controlled agent state.
- Plausible first-party paths checked: Operator root-purpose decisions, policy charter approval and binding return into installed agent organization beyond action-by-action risk approvals.
- Why no material first-party path remains: The supported configuration restricts local tools and controls sessions, but does not supply a distinct attributable S5 policy/identity decision and returned organization-level closure.

## Distributed OSS parent arrangement

Independent Apogee installations and public GitHub contributor/release processes are distinct from the supported local agent system. Human source maintainers and any company's outside approval structure are not automatically a first-party parent authority of the assessed installed agent organization.

## Self-hosted and non-human modes

Apogee supports self-hosted local inference, headless prompts and foreground daemon schedules. A headless scheduled run does not make the installed system autonomously own S3–S5 policy. The model owns coding-task discretion in S1 while deterministic first-party construction attenuates a proven inter-child shared-prompt collision in optional parallel mode.

## Recursion

One user-installed Apogee coding-agent system is the reviewed recursion. Model-directed subagents are independent S1 task units when fan-out is active; a workflow's nested helper and its parent are not automatically distinct recursively viable enterprises.

## Variety and escalation

Code/task variety is handled by S1 model/tool/observation iteration, correction guards and bounded retries. Simultaneous delegated approval requests are serialized and feedback returned as an S2 path; a denied approval prevents that child's requested action. User steering/cancel, model-server faults and workflow retry/stop are local execution/recovery paths; none alone establishes S3 manager control, S3* audit, S4 adaptation or S5 ultimate purpose.

## Evidence gaps

- This is a source-level assessment at a pinned SHA; Apogee's Go regression tests were read but could not be executed on the available inspection machine. No claim of live LLM benchmarks or production operator performance.
- S2's `C` is narrowly evidenced by first-party concurrent child approvals over one exclusive prompt surface, verified by a specific shipped regression. It does not establish cross-file edit conflict resolution or adaptive enterprise resource allocation.
- A workflow `verify` helper is separately model-guided but is limited to task-item QA; a function-specific complementary audit of S3 whole-current management would require different explicit first-party reachability and return evidence.
- Further independent evidence of whole-system priorities/commitments, prospective adaptation or constitutional parent policy may warrant a future same-ref re-review, but is not supplied by configuration, benchmark code or UI controls alone.
