---
harness_id: slack-agent-runtime
project_name: Slack Agent Runtime
repository: https://github.com/sakomws/slack-agent-runtime
review_ref: 16bb262715b7bacb64c7466cf106063c2fdf6c93
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Slack Agent Runtime

## Review boundary

- System in focus: the shipped Slack-facing Python runtime and bounded GitHub Actions coding/review workers, rather than Slack, You.com or GitHub as independent organizations.
- Purpose and identity: convert user messages/specifications into model-directed answers, MCP tool use, bounded code changes and optional PR reviews under configured credentials and access controls.
- Relevant environment: changing Slack conversation, available MCP records, repository code/tests/diffs, external inference API, GitHub checks and human operators.
- Credited operating / distribution surfaces: `services/agent_runner.py`, `services/completion_runner.py`, `coding/worker.py`, `coding/reviewer.py`, `coding/tools.py`, `plugins/coding.py`, `plugins/reviews.py`, `mcp/approval.py`, `domain/policy.py`, entrypoints and provided coding/review workflows.
- Adjacent first-party surfaces excluded from ownership: architecture proposals/roadmap, tests and fake model clients, CI for this repository, human deployment/security review, downstream GitHub branch protection and external Slack/inference services.
- First-party operating modes: Slack conversational model/tool loop, allowlisted dispatched coding worker, independently invoked PR reviewer, optionally approved MCP calls; no asserted continuous autonomous product portfolio.
- Recursion level: one deployed Slack Agent Runtime installation, with separate bounded coding tasks as operations; the upstream OSS maintainer project is outside the assessed recursion.
- Reviewed revision: `16bb262715b7bacb64c7466cf106063c2fdf6c93`, source-static on 2026-11-11; no live external provider credentials or GitHub Actions executions tested.
- Generated Profile/Methodology: 0.2.4 / 0.3.8; active pair at assessment: 0.2.4 / 0.3.8.

## Repository architecture

Slack Socket Mode events pass through a conversation coordinator and plugin registry. A bounded `AgentRunner` loops inference/tool calls, routes MCP tools and awaits approval for non-autoapproved tools. The separate `CodingWorker` loops model-directed workspace tools inside a GitHub Actions checkout; a later privileged workflow step, not the worker, publishes the PR. A separately dispatched `PullRequestReviewer` examines a diff and emits validated structured findings. These are implemented modes, but no evidence of a first-party autonomous whole-portfolio supervisor, environment-foresight or ultimate-identity agent appears in the reviewed service. See [technical specification](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/docs/slack-agent-runtime-tech-spec.md) and [README](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/README.md).

## Operational model

- User/admin requests choose the task and permitted repository. The model chooses tools, edits, follow-up calls and completion within bounded rounds; deterministic policy, approvals and credential separation enforce, rather than originate, choices.
- A reviewer can make a separate model-based correctness judgment from a submitted PR diff; external GitHub checks, human review and branch protection remain independent controls, not attributed to that model.
- Per-thread history, status and rate/concurrency counters are useful local mechanisms; no default agent is shown deciding resource priorities across all running operations.

## S1 — Operations

- State: A
- Function: carry out bounded conversation/MCP actions and coding tasks based on model-selected next actions.
- Disturbance / variety regulated: unstructured requests, tool replies, changing code/tests and model errors within a bounded assigned job.
- Decisive decision or feedback right: choose subsequent MCP tool or coding workspace operation after observing results, and choose when to finish.
- Decision owner: the first-party agent/tool and coding-worker loops supplied with an external inference model; the user selects the objective and the service bounds permissions.
- Supporting / enforcement mechanisms: step budget, tool schema, `WorkspaceTools`, approval broker, allowlists, isolated checkout and separated publication credentials.
- Closure path: Slack request or dispatched coding task → inference decision → tool execution → result injected into model conversation → next action or final result/PR artifact.
- Boundary reachability: default Slack MCP path and the shipped allowlisted coding-job entrypoint invoke real first-party loops; no custom developer agent implementation is required.
- Why this is / is not agent-owned: tool choice and iterative repair are model-discretionary, while approval and final publish are enforced by non-model layers.
- Evidence: [MCP agent loop](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/services/agent_runner.py), [coding worker](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/coding/worker.py), [tools](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/coding/tools.py).
- Basis: implemented structural flow; no live inference run.
- Confidence: high for agent-loop ownership, not for actual task success.
- Caveats: the GitHub publication step uses separate credentials, and a human is required for merge; neither is credited as agent decision.

## S2 — Coordination

- State: —
- Function: no demonstrated first-party regulation of interference among distinct autonomous S1 coding units at this recursion.
- Disturbance / variety regulated: potential concurrent jobs writing to overlapping branches or projects, but no evidenced S2-specific coordination loop.
- Decisive decision or feedback right: absent for inter-S1 collision resolution; admins choose work requests, while quotas/locks execute fixed limits.
- Decision owner: no autonomous S2-specific coordinator identified in shipped runtime.
- Supporting / enforcement mechanisms: thread state, active task tracking, policy quotas, repository allowlisting, fixed GitHub Actions dispatch.
- Closure path: no first-party conflict signal → discretionary coordination → altered subsequent S1 behavior chain evidenced; isolated task guards are not this chain.
- Why this is / is not agent-owned: scheduling/rate limiting does not demonstrate mediation of an inter-agent conflict.
- Evidence: [policy](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/domain/policy.py), [coding dispatch](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/plugins/coding.py), [spec limitations](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/docs/slack-agent-runtime-tech-spec.md).
- Basis: bounded no-path after checking shipped dispatch, policy and coordination surfaces.
- Confidence: medium-high within deployed runtime boundary.
- Caveats: upstream GitHub may serialize or reject changes, but that is not first-party discretionary inter-S1 coordination.

### Absence scope

- Surfaces inspected: `services/conversation_coordinator.py`, `domain/policy.py`, `plugins/coding.py`, `coding/github.py`, `storage/persistence.py` and the technical specification.
- Plausible first-party paths checked: per-thread locks, global concurrency/rate limits, coding/review job status, GitHub allowlisting, worker dispatch.
- Why no material first-party path remains: those mechanisms route or constrain jobs without identifying competing S1 units, adjudicating their interference and feeding a remedy back to their execution.

## S3 — Inside-and-now control

- State: —
- Function: no whole-installation discretionary present-operational supervision demonstrated.
- Disturbance / variety regulated: current job failures, quota saturation and review/dispatch state are exposed but not used in a first-party whole-system control loop.
- Decisive decision or feedback right: no shipped actor chooses portfolio priorities, reallocates work or changes current operational commitments from a whole-system view.
- Decision owner: human administrators issue independent commands; a programmatic S3 owner is not established by their local job actions.
- Supporting / enforcement mechanisms: durable Actions job-status queries, per-thread state and quotas, policy and stream cancellation.
- Closure path: individual `code status`/`review status` queries return observations to requesters; no demonstrated whole-system current-view → supervisory choice → altered work portfolio path.
- Why this is / is not agent-owned: current status reporting and deterministic quota enforcement are not discretionary whole-system control.
- Evidence: [technical specification](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/docs/slack-agent-runtime-tech-spec.md), [thread coordinator](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/services/conversation_coordinator.py), [coding plugin](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/plugins/coding.py).
- Basis: bounded source-static absence.
- Confidence: medium-high for ordinary shipped modes.
- Caveats: external human operations could build supervision on top; not counted without a first-party return path.

### Absence scope

- Surfaces inspected: core coordinator, policy, coding/review dispatch plugins, persistent state and spec.
- Plausible first-party paths checked: job status commands, quotas, cancellation, active tasks, admin permissions.
- Why no material first-party path remains: no cross-job current control owner or whole-system portfolio intervention is wired; mechanisms remain per-request or fixed constraints.

## S3* — Complementary audit

- State: A
- Function: review the correctness, reliability and security of a proposed code change through a model judgment separate from the coding worker.
- Disturbance / variety regulated: builder omissions and errors that pass self-report or initial local tests.
- Decisive decision or feedback right: report structured findings and select a validated severity-derived `REQUEST_CHANGES` or `APPROVE` recommendation.
- Decision owner: separately dispatched `PullRequestReviewer` model workflow; publication safety checks can downgrade its verdict.
- Supporting / enforcement mechanisms: source diff extraction, exact SHA, JSON validation, check status, GitHub review publication and human merge authority.
- Claim being audited: the submitted PR satisfies correctness, security and reliability requirements; reviewer does not merely summarize coding worker's completion.
- Ordinary reporting path: worker summary, test report and PR diff/CI status.
- Complementary access path: reviewer receives actual PR diff plus title/body with separate inference instructions, producing findings by file/line independently of worker self-report.
- Independence boundary: reviewer is a distinct invocation with its own role and bounded input; same underlying provider/model or stronger institutional independence is **not** established.
- Who acts on findings: review workflow publishes a permitted GitHub review or comment; maintainers and authors correct the change, with required checks/merge authority retained externally.
- Closure path: PR head/diff → independently invoked model reviewer → validated findings/severity → GitHub review/comment → author/maintainer action before merge.
- Boundary reachability: the shipped `review <repo>#<PR>` Slack command dispatches the review workflow; it is an opt-in built-in mode, not automatically run for every coding job.
- Why this is / is not agent-owned: the reviewer generates an evaluative model judgment; deterministic review-event selection and publishing restrictions only constrain it.
- Evidence: [reviewer code](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/coding/reviewer.py), [review plugin](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/plugins/reviews.py), [review workflow architecture](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/docs/slack-agent-runtime-tech-spec.md).
- Basis: implemented separate review mode, source-static.
- Confidence: medium-high in structural complementarity; review efficacy and provider independence untested.
- Caveats: no automatic closed builder-fix/re-review loop proven; closure relies on normal GitHub author/maintainer feedback, so the mode's end-to-end effectiveness remains unverified.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party longer-horizon scanning/adaptation decision path for the runtime's future capabilities.
- Disturbance / variety regulated: prospective changes in user needs, provider/service ecosystem and platform behavior are mentioned in documents but not regulated by an operating adaptation loop.
- Decisive decision or feedback right: no installed agent chooses future runtime strategy/options against external signals and returns them into current capability.
- Decision owner: maintainers can revise roadmap outside the assessed runtime; no shipped S4 actor.
- Supporting / enforcement mechanisms: inference web search for user tasks, roadmap, issue-oriented coding worker and spec review.
- Closure path: normal user-requested coding can change external repositories; it is S1 task delivery, not foresight about this runtime's identity/capability.
- Why this is / is not agent-owned: web search and document review serve immediate requests, not a prospective environment-to-adaptation loop.
- Evidence: [roadmap](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/docs/roadmap.md), [README](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/README.md), [technical spec](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/docs/slack-agent-runtime-tech-spec.md).
- Basis: bounded no-path for shipped first-party modes.
- Confidence: medium.
- Caveats: operator-maintained roadmap is not attributed to a deployed agent or parent-governed runtime S4 without return-to-operation evidence.

### Absence scope

- Surfaces inspected: roadmap, spec, inference/search settings, spec-review and coding job workflows.
- Plausible first-party paths checked: web search, Notion spec review, coding task generation, roadmap prioritization.
- Why no material first-party path remains: no first-party signal → prospective option → strategic selection → updated runtime capability loop; task tools are externally prompted.

## S5 — Policy and identity

- State: —
- Function: no evidenced first-party ultimate mission/identity decision and return loop at the runtime recursion.
- Disturbance / variety regulated: role/credential access boundaries are protected, but the system's purpose/ultimate policy is not decided by the installed runtime.
- Decisive decision or feedback right: no first-party agent or explicit parent policy path authoritatively revises the runtime's ultimate mission and binds later operation.
- Decision owner: humans manage configuration, whitelists, deployment and merge permissions as local operational governance, not a proved S5 identity-mode closure.
- Supporting / enforcement mechanisms: admin IDs, repository allowlists, MCP approval, credentials, model choice and separated privileged publication stages.
- Closure path: local policy configuration gates requests; it does not demonstrate an ultimate-policy decision circuit, nor make approval requests S5 by default.
- Why this is / is not agent-owned: permission checks and human approvals enforce task scope without selecting a durable system identity.
- Evidence: [policy module](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/domain/policy.py), [technical spec](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/docs/slack-agent-runtime-tech-spec.md), [approval broker](https://github.com/sakomws/slack-agent-runtime/blob/16bb262715b7bacb64c7466cf106063c2fdf6c93/src/slack_agent_runtime/mcp/approval.py).
- Basis: bounded absence, not a judgment on the human maintainer organization's actual policy.
- Confidence: medium; no runtime identity decision path identified.
- Caveats: configuration policy can reflect human values; this alone does not prove the required ultimate-policy function.

### Absence scope

- Surfaces inspected: administrator policy, MCP approvals, service configuration, architecture and rollout requirements.
- Plausible first-party paths checked: administrator model selection, repository allowlists, approval choices, human PR merge, deployment rules.
- Why no material first-party path remains: these are operational permissions and external authority checks without an explicit ultimate-identity judgment and return path into deployed operation.

## Distributed OSS parent arrangement

No inference is made about collective authority of this repository's maintainers from contributor activity; the assessment concerns the deployed Slack-facing service only.

## Self-hosted and non-human modes

An administrator controls credentials, allowed users/repos and human PR merge. This is an intentional operational control plane, but no qualifying S3/S4/S5 parent closure is claimed without the corresponding function-first evidence.

## Recursion

A dispatched coding job and independently requested PR review are distinct task roles, not proof of several mutually interfering S1 units or a whole-runtime S3 merely because both run in GitHub Actions.

## Variety and escalation

Step limits, tool allowlists, human MCP approvals, precise repository permissions, security restrictions, model-output validation and separate credentialed publish stages attenuate task variety. These checks do not automatically confer S2, S3 or S5 ownership.

## Evidence gaps

- No live Slack Socket Mode/inference/MCP/GitHub Actions E2E and no independent model audit effectiveness test.
- Source demonstrates separately invoked reviewer but not automatic builder self-correction or provider-institution independence.
- External GitHub, You.com and Slack operational authority and upstream maintainer governance are not attributed to the first-party runtime.
