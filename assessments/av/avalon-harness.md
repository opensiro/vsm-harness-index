---
harness_id: avalon-harness
project_name: Avalon Harness
repository: https://github.com/GeneralReasoning/avalon-harness
review_ref: 817220ed3847ff70bca5f5eba7a8f9a713039775
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Avalon Harness

## Review boundary

- System in focus: One AgentOrg session, including the CEO and live specialists.
- Purpose and identity: Complete a supplied task through model-directed operations and, in team mode, specialist collaboration.
- Relevant environment: A task caller, a configured inference endpoint, selected filesystem tools and an optional environment adapter.
- Standard-distribution boundary: The installable AgentOrg library and the Avalon sampling CLI.
- Credited operating / distribution surfaces: Session supervisor, per-agent loop, scoped tools, live roster, archive, wait broker and reporting surfaces.
- Adjacent first-party surfaces excluded from ownership: Training project, offline benchmark aggregation, repository tests, and implementations of external inference and environment services.
- First-party operating / deployment modes considered: Solo headless, multi-agent headless, and the library's attended session interface.
- Recursion level: One session above its distinct specialist operations.
- Reviewed revision: 817220ed3847ff70bca5f5eba7a8f9a713039775
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The library constructs one CEO and a registry of native tools. The session supervisor starts a separate model loop for each live specialist. Tool definitions and feedback are copied into each inference turn. Per-agent transcripts, channel and archive state, and the roster persist in the workspace. The adapter optionally adds environment actions and terminal scoring.

## Operational model

The CEO can run a task itself in solo mode. In team mode it establishes mandates and coordinates specialists with individual model histories and tools. Specialists execute work and report to the CEO, which selects the final result or submits to the configured environment. Runtime budget and permission checks bound those choices. An attended caller can send information or resolve a permission request.

## S1 — Operations

- State: A
- Function: Complete a task or a delegated mandate through model-selected actions.
- Disturbance / variety regulated: Uncertain task progress, tool failures and incomplete input.
- Decisive decision or feedback right: Choose the next action, incorporate tool results and decide the outcome to send.
- Decision owner: The active CEO in solo mode or the operating specialist within its mandate.
- Supporting / enforcement mechanisms: Native inference and dispatch, transcript, tool scoping and session supervisor.
- Closure path: Tools return results into the active model history. Specialists return a result through ReportToCEO, and the CEO returns its terminal answer to the caller or adapter.
- Why this is / is not agent-owned: Model choice governs operation within the assigned task. The constructor supplies the complete actor and feedback path.
- Boundary reachability: The shipped harness instantiates the CEO and the supervisor starts the same run loop for the live specialists.
- Evidence: [agentorg/harness.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/harness.py#L231-L278), [agentorg/harness.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/harness.py#L338-L411), [agentorg/loop.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/loop.py#L341-L418), [agentorg/loop.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/loop.py#L628-L642), [agentorg/tools/wait_tools.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/tools/wait_tools.py#L261-L295)
- Basis: Static inspection of pinned first-party source.
- Confidence: high
- Caveats: Actual task outcomes depend on the selected model and available tools.

## S2 — Coordination

- State: A
- Function: Avoid concurrent changes to the same environment state by different operational agents.
- Disturbance / variety regulated: Multiple specialists may inherit the same state-advancing tool and race on the environment.
- Decisive decision or feedback right: Choose the one operating holder and revoke or withhold the action from the other contenders.
- Decision owner: The active CEO model performs the coordinating choice for the specialist operations.
- Supporting / enforcement mechanisms: The shipped planning prompt describes the shared-state race. The hire and update tools persist access changes, notify the worker and enforce effective scope on dispatch.
- Closure path: The revised permissions change the next specialist tool view and dispatch, and the targeted agent receives the update in its inbox.
- Why this is / is not agent-owned: Removing the CEO's ownership choice leaves the general permission mechanism, with no chosen single specialist holder.
- Boundary reachability: In multi-agent mode the built-in CEO sees the coordination rule and can use the shipped hire and update tools immediately.
- Distinct S1 units: Two live specialist agents with separate mandates, model loops and relevant environment operations.
- Inter-S1 disturbance: Each specialist may be able to independently advance the same shared environment state, so overlapping calls interfere.
- Attenuating coordination relation: The CEO allocates exclusive ownership of the contested tool using per-specialist tool scope and can revise the allocation in the same run.
- Feedback into subsequent S1 behaviour: The worker receives a scope update and the runtime removes or denies the operation on the next relevant turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The supplied prompt identifies the contention and instructs a single-holder allocation using the native runtime permissions.
- Evidence: [agentorg/prompts.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/prompts.py#L155-L164), [agentorg/prompts.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/prompts.py#L188-L195), [agentorg/org.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/org.py#L331-L357), [agentorg/loop.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/loop.py#L1830-L1856), [agentorg/loop.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/loop.py#L1906-L1937)
- Basis: Static inspection of pinned first-party source.
- Confidence: high
- Caveats: The witness applies where the selected environment provides a shared state-advancing action. The runtime does not serialize all same-tool worker calls by default.

## S3 — Inside-and-now control

- State: A
- Function: Regulate the session's current work and specialist capacity.
- Disturbance / variety regulated: Concurrent specialists consume a shared allotment and may be redundant, blocked, or underperforming.
- Decisive decision or feedback right: Review current commitments and decide whether to hire, fire or reconfigure a specialist.
- Decision owner: The session's CEO model.
- Supporting / enforcement mechanisms: Roster prompt, structured reports, budget check, gated management tools and supervisor.
- Closure path: Hire places a mandate in a new live loop. Fire cancels the specialist's background work, refreshes the roster and wakes its loop to exit. Tool updates change live capability.
- Why this is / is not agent-owned: The configured budget supplies a bound. Within it the CEO decides how to allocate headcount, role and scope and whether to intervene in response to feedback.
- Boundary reachability: The shipped multi-agent registry gives the CEO the necessary management tools and direct access to the live reports and roster.
- Whole-system current view: The CEO holds the global request and sees live roster, specialist mandates, reports, and blocked or failed status.
- Current-control decision scope: Admit, remove or retool current specialists, redistribute active roles and associated finite session capacity.
- Evidence: [agentorg/harness.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/harness.py#L95-L122), [agentorg/org.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/org.py#L44-L95), [agentorg/org.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/org.py#L224-L261), [agentorg/org.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/org.py#L269-L304), [agentorg/tools/wait_tools.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/tools/wait_tools.py#L241-L295), [agentorg/tools/org_mgmt_tools.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/tools/org_mgmt_tools.py#L259-L361), [agentorg/external.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/external.py#L162-L178)
- Basis: Static inspection of pinned first-party source.
- Confidence: high
- Caveats: The attended interface exposes input, individual permission decisions and abort. A distinct parent mode for whole-session allocation was not established.

## S3* — Complementary audit

- State: A
- Function: Challenge a live specialist's account when routine reporting is doubtful.
- Disturbance / variety regulated: A summary may omit a failed operation, hide a mismatch, or drift from the source trace.
- Decisive decision or feedback right: Select a suspect claim, retrieve the independent trace path and decide whether the discrepancy warrants intervention.
- Decision owner: The CEO model in its complementary audit activity.
- Supporting / enforcement mechanisms: Native trace-channel views read the full transcript through a separate read-only route and expose source tool input and output.
- Closure path: The returned trace enters the CEO model context. It can message the specialist for correction or remove and replace it based on the findings.
- Why this is / is not agent-owned: The audited specialist supplies the ordinary report. The controller independently chooses whether to inspect direct runtime records and how to act.
- Boundary reachability: The multilateral CEO prompt explicitly directs sampling of suspect summaries and registers the trace and corrective tools in the ordinary runnable session.
- Claim being audited: A named specialist's claim about what it did and what result it obtained.
- Ordinary reporting path: ReportToCEO sends a worker-authored status, summary and artifact pointers.
- Complementary access path: ViewChannelMessages reads the named specialist's full runtime transcript including raw tool I/O, separately from its report.
- Independence boundary: Inspection and judgment run in the CEO's separate model context. The worker's report does not generate or filter the runtime transcript.
- Who acts on findings: The CEO can send a correction, revise scope, or remove the specialist and reassign the mandate.
- Evidence: [agentorg/prompts.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/prompts.py#L188-L211), [agentorg/tools/comms_tools.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/tools/comms_tools.py#L409-L469), [agentorg/tools/comms_tools.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/tools/comms_tools.py#L718-L741), [agentorg/session.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/session.py#L895-L934), [agentorg/tools/wait_tools.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/tools/wait_tools.py#L276-L295), [agentorg/tools/org_mgmt_tools.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/tools/org_mgmt_tools.py#L311-L361)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: The trail corroborates tool interactions and observed returns. External truth beyond those observations depends on the selected tools. Terminal environment scoring is separately scoped.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospective adaptation of future session capability was sought.
- Disturbance / variety regulated: External changes may require a different future operating capability.
- Decisive decision or feedback right: No first-party decision loop was found that admits a future capability adaptation.
- Decision owner: The caller supplies initial configuration. The CEO changes the current roster and tool allocation.
- Supporting / enforcement mechanisms: Org planning, environment input, archive, context compaction and sampling reward.
- Closure path: The retrieved material guides current execution or is exported as outcome evidence.
- Why this is / is not agent-owned: Roster redesign and environment response close the current assignment. Future adaptation would require an additional consumer and binding decision.
- Evidence: [agentorg/harness.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/harness.py#L193-L238), [agentorg/external.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/external.py#L38-L84), [agentorg/tools/org_mgmt_tools.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/tools/org_mgmt_tools.py#L123-L174), [agentorg/cli/sample.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/cli/sample.py#L145-L170), [agentorg/cli/sample.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/cli/sample.py#L184-L208)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: The broader model training and evaluation process is outside this session.

### Absence scope

- Surfaces inspected: Session configuration, org planning, environment feedback, archival context, reward output and the model-facing external-input interface.
- Plausible first-party paths checked: An external distinction feeding capability options and returning a selected adaptation into a future session or installed tool capability.
- Why no material first-party path remains: The observed input paths change current tasks, and the reward path emits evaluation evidence. The supported runtime supplies no binding capability decision from these paths.

## S5 — Policy and identity

- State: —
- Function: Ultimate identity and policy adjudication was sought for the session.
- Disturbance / variety regulated: A task or tool request may conflict with an operating boundary or authority.
- Decisive decision or feedback right: No supplied owner receives and resolves a session identity dispute with a governing decision.
- Decision owner: The caller supplies goals and limits, while the CEO manages current operations.
- Supporting / enforcement mechanisms: Installation configuration, plan mode, tool rights and attended permission and abort APIs.
- Closure path: Operation proceeds under supplied limits. An individual permission decision returns to the requesting action.
- Why this is / is not agent-owned: Session control and a scoped allow/deny do not establish the governing cycle.
- Evidence: [agentorg/harness.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/harness.py#L231-L278), [agentorg/loop.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/loop.py#L1830-L1898), [agentorg/external.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/external.py#L162-L178), [agentorg/org.py](https://github.com/GeneralReasoning/avalon-harness/blob/817220ed3847ff70bca5f5eba7a8f9a713039775/agentorg/org.py#L331-L357)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Maintainer governance of the distributed code is outside the assessed recursion.

### Absence scope

- Surfaces inspected: Root session configuration, CEO tool portfolio, permission resolution, external input and abort.
- Plausible first-party paths checked: Autonomous or parent resolution of a live identity or ultimate-policy issue with an authoritative decision returned to operation.
- Why no material first-party path remains: The listed paths enforce configured authority or resolve current operational exceptions at the action or session level. No supplied issue-to-governing-policy return path was found.

## Recursion

One AgentOrg session contains agent operations under a CEO. Specialist tools and background subprocesses are supports inside individual operations. Separate sampling rollouts instantiate separate sessions.

## Variety and escalation

Roster and tool scope bound worker variety. The wait path wakes the CEO on group quiescence. The awaited tool permission path allows a specific attended exception. No distinct identity-level escalation was evidenced.

## Evidence gaps

Source inspection only. No provider, live rollout, environment score, or concurrency scenario was executed. The weak point of the audit is any claim whose truth cannot be reconstructed from the runtime transcript.
