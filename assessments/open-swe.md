---
harness_id: open-swe
project_name: Open SWE
repository: https://github.com/langchain-ai/open-swe
review_ref: d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: ?
---

# Open SWE

## Review boundary
- System in focus: Open SWE's shipped first-party coding-agent hosting and its separate GitHub PR reviewer path, at one frozen revision; the external Deep Agents/LangGraph library runtime is a dependency, not an independently attributed Open SWE owner.
- Purpose and identity: conduct source editing/task work through model and sandbox tools; optionally inspect actual PR source changes with a separately dispatched code-review agent and send corrective findings to contributors.
- Relevant environment: user coding goals, GitHub PR/diffs/issues, repo files, sandbox execution, delegated subagents, external model/tool responses, user approvals and review/check results.
- Standard-distribution boundary: first-party `agent/server.py`, `agent/reviewer.py`, `agent/github/webhook.py`, shipped hosted graphs, tool/approval and PR-review registration; library primitives alone, SaaS infrastructure internals, external MCP/model providers and noninstalled user custom plugins excluded ([agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py); [agent/reviewer.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/reviewer.py); [agent/github/webhook.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/github/webhook.py)).
- Credited operating / distribution surfaces: [agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py); [agent/reviewer.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/reviewer.py); [agent/github/webhook.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/github/webhook.py); [agent/tools/fetch_review_diff.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/tools/fetch_review_diff.py); [agent/tools/publish_review.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/tools/publish_review.py); [agent/review/findings.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/review/findings.py); [agent/middleware/settle_review_check.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/middleware/settle_review_check.py); [agent/middleware/workflow_push_guard.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/middleware/workflow_push_guard.py).
- Adjacent first-party surfaces excluded from ownership: benchmarks/evals and example tasks, development CI/contributor dogfood, unrelated paid model provider internals, custom external agents and third-party GitHub reviewer services.
- First-party operating / deployment modes considered: main coding Agent graph, general-purpose subagent task tool, first-party separately triggered PR Reviewer graph, human workflow approval and persisted thread controls.
- Recursion level: coding agent operating on a thread/PR and a separately invoked reviewer control/audit function in the same first-party Open SWE service; not every external repository and human contributor as owned S1.
- Reviewed revision: `d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
Open SWE uses first-party host wiring to construct a Deep Agents model/tool graph with sandbox, code-facing tools, error middleware, general-purpose subagent option and durable threads. The deeper generic control engine is an external dependency; the Open SWE-owned operating boundary is the configured reachable service graph, not a claim about authorship of LangGraph internals ([agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py); [agent/threads/runs.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/threads/runs.py)).
Separately, a GitHub PR review webhook can schedule a dedicated reviewer thread. That graph has its own reviewer model, review sandbox/token acquisition, fetch-review-diff and publish-review tools, and posts concrete findings/check conclusions onto the PR. This gives alternative source-grounded observation beyond the coding agent's ordinary completion report ([agent/github/webhook.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/github/webhook.py); [agent/reviewer.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/reviewer.py); [agent/tools/fetch_review_diff.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/tools/fetch_review_diff.py); [agent/tools/publish_review.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/tools/publish_review.py)).

## Operational model
The coding graph performs user tasks and may delegate a bounded subtask. The independent reviewer mode is activated by GitHub PR events and is capable of examining the actual proposed code diff and posting actionable findings. Static permissions/approval, memory and ordinary delegation are not automatically S2/S3/S4/S5 without stronger source-specific function rights.

## S1 — Operations

- State: A
- Function: Perform first-party model-driven software engineering work via the hosted Deep Agents runtime and first-party tool/sandbox/middleware wiring.
- Disturbance / variety regulated: Changing issue/task objectives, file state, command/tool errors, external information and user steering.
- Decisive decision or feedback right: Choose coding tool actions, inspect files and tool returns, iteratively continue or repair work.
- Decision owner: Configured model-driven Open SWE main agent in a supported service/desktop run.
- Supporting / enforcement mechanisms: First-party graph factory, model/tool bindings, sandbox backend, tool and failure middleware, durable session/threads.
- Closure path: User/issue instruction → hosted model selects tools → sandbox/code effects and observations → further model actions or completion.
- Boundary reachability: The published Agent service path invokes `get_agent` and returns an actual `create_deep_agent` graph with configured tools, sandbox and middleware, rather than a README-only graph ([agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py)).
- Why this is / is not agent-owned: Material agent-model judgment selects actions over operational evidence; deterministic middleware enforces rather than owning that judgment.
- Evidence: [agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py); [agent/threads/runs.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/threads/runs.py)
- Basis: structural
- Confidence: high
- Caveats: Static source-grounded mode analysis at frozen SHA; no real provider-backed production run performed.

## S2 — Coordination

- State: ?
- Function: Potential mitigation of interference among independently running subagents or separate coding threads; no fully reconstructed first-party cross-S1 conflict detector/return.
- Distinct S1 units: Main agent and general-purpose delegated subagent, with additional first-party reviewer process in an independent mode.
- Inter-S1 disturbance: Possible simultaneous workspace edits and shared resource pressure among independently acting coding agents.
- Attenuating coordination relation: No specific shipped contention policy with conflict-conditioned result beyond ordinary task routing/approval has been fully traced.
- Feedback into subsequent S1 behaviour: Returned subagent results or tool denial can affect model work, but actual cross-S1 interference feedback not established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Do not credit S2 from topology or push approvals alone.
- Disturbance / variety regulated: Concurrent agents modifying common workspaces, duplicated work, tool-resource contention or conflicting PR changes.
- Decisive decision or feedback right: Unresolved interference-specific arbitration; available approval/security gates and task delegation are not enough by themselves.
- Decision owner: Unknown between sandbox/workflow policy, developer runtime and model task parent.
- Supporting / enforcement mechanisms: Deep Agents subagent model, sandbox backend, thread-scoped execution and workflow-push approval guard.
- Closure path: Tasks and subagent results can be returned, but source-grounded cross-S1 collision detection and corrected scope/work assignment remain unverified.
- Why this is / is not agent-owned: Neither a generic tool, approval, stage name nor a model-provider capability is credited without the stated organizational owner and closure.
- Evidence: [agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py); [agent/middleware/workflow_push_guard.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/middleware/workflow_push_guard.py); [agent/threads/runs.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/threads/runs.py)
- Basis: unknown
- Confidence: low
- Caveats: Static source-grounded mode analysis at frozen SHA; no real provider-backed production run performed.

## S3 — Inside-and-now control

- State: ?
- Function: Candidate parent current-control through subagent delegation; whole-system current allocation/feedback rights over multiple concurrent independent operating units not established.
- Whole-system current view: Subagent completion feedback is available to the main agent; full team commitment/priority/resource state is not evidenced.
- Current-control decision scope: Task delegation and continuation verified; higher-level current-control regulation remains unproven.
- Disturbance / variety regulated: Live subordinate subtasks, capacity/priority conflicts and incomplete current coding commitments.
- Decisive decision or feedback right: Parent can create general-purpose subagent requests and consume results, but whole-team resource bargaining/intervention beyond task decomposition remains unresolved.
- Decision owner: Potential model-led parent; supported delegation primitive alone cannot qualify whole-system control.
- Supporting / enforcement mechanisms: Configured `subagents` passed to Deep Agents, main thread and tool execution, user steering.
- Closure path: Subagent result → main model continuation; broader current resource/commitment regulation or intervention not established.
- Why this is / is not agent-owned: Neither a generic tool, approval, stage name nor a model-provider capability is credited without the stated organizational owner and closure.
- Evidence: [agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py); [agent/threads/runs.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/threads/runs.py)
- Basis: unknown
- Confidence: low
- Caveats: Static source-grounded mode analysis at frozen SHA; no real provider-backed production run performed.

## S3* — Complementary audit

- State: A
- Function: Separately triggered first-party reviewer agent samples the actual PR diff/repository and challenges coding-output claims via review findings posted into GitHub.
- Claim being audited: Whether a produced PR's new code safely and correctly implements its advertised change.
- Ordinary reporting path: Author or coding agent presents its own completion/PR description and ordinary test outputs.
- Complementary access path: Separate reviewer fetches actual GitHub PR diff and checked-out repository code using independently provisioned repo-scoped credentials.
- Independence boundary: Distinct reviewer thread, tools, sandbox and source-observation route from originating coding-agent execution; external PR author need not be Open SWE itself.
- Who acts on findings: GitHub contributor/repository maintainer or coding agent receives published inline findings/check results and can revise PR.
- Disturbance / variety regulated: Hidden code defects, failure to meet repository rules, bugs missed by ordinary coding-agent self-report and PR authors.
- Decisive decision or feedback right: Independently fetch code changes and repository artifacts, judge material defects, publish actionable review findings/checks.
- Decision owner: First-party reviewer model agent in a separate reviewer thread/graph, not the producing coding-agent self-check.
- Supporting / enforcement mechanisms: PR webhook review trigger, dedicated review token/sandbox, fetch_review_diff, finding registry/publisher and PR/check feedback.
- Closure path: External PR head/base/diff → independent reviewer inspects sources → findings/PR review/check status → author or main agent/human can revise code or gate integration.
- Boundary reachability: The shipped PR-review trigger schedules a separate reviewer thread/graph, with first-party `fetch_review_diff` and `publish_review` tools and status publication, not merely a passive self-check ([agent/github/webhook.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/github/webhook.py); [agent/reviewer.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/reviewer.py); [agent/tools/publish_review.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/tools/publish_review.py)).
- Why this is / is not agent-owned: Material agent-model judgment selects actions over operational evidence; deterministic middleware enforces rather than owning that judgment.
- Evidence: [agent/github/webhook.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/github/webhook.py); [agent/reviewer.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/reviewer.py); [agent/tools/fetch_review_diff.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/tools/fetch_review_diff.py); [agent/tools/publish_review.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/tools/publish_review.py); [agent/middleware/settle_review_check.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/middleware/settle_review_check.py)
- Basis: structural
- Confidence: medium
- Caveats: Static source-grounded mode analysis at frozen SHA; no real provider-backed production run performed.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Skills, thread memory, planning and scheduling may support longer-term improvements; externally prospective capability adaptation decision and closure are unresolved.
- External distinction: Web and GitHub tools observe external change, but this alone is not prospective intelligence.
- Future / prospective distinction: Persisted context and scheduled runs are not automatically forward-looking organizational adaptation.
- Adaptation option generated: Not established as future system-capability redesign.
- Path back into current capability / S3: Later prompts may include knowledge, but a qualifying adaptation-choice/commitment return is unresolved.
- Disturbance / variety regulated: Changed project environment and future tooling/organization needs.
- Decisive decision or feedback right: No demonstrated agent-owned prospective redesign of future operational capability based on external horizon observations.
- Decision owner: Unresolved among user/workspace admin, ordinary agent and optional background automation.
- Supporting / enforcement mechanisms: Skills, configuration, session history, scheduling and model/tool work.
- Closure path: Stored context and tools can feed later tasks; future external opportunity detection → capability-changing option → adoption loop unproved.
- Why this is / is not agent-owned: Neither a generic tool, approval, stage name nor a model-provider capability is credited without the stated organizational owner and closure.
- Evidence: [agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py); [agent/threads/runs.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/threads/runs.py)
- Basis: unknown
- Confidence: low
- Caveats: Static source-grounded mode analysis at frozen SHA; no real provider-backed production run performed.

## S5 — Policy and identity

- State: ?
- Function: Human approval, workflow safety, trust and policy settings constrain agent actions without a demonstrated ultimate identity/policy governance cycle.
- Identity / ultimate-policy issue: Who decides and revises the purpose, final authority and acceptable overall conduct of this Open SWE organization.
- Ultimate authority in each claimed mode: Human workspace/account owners set permissions; an operative full organization-level policy closure is unproven.
- Return-to-operation path: Workflow push guard approval returns to individual operations, not necessarily ultimate identity revision.
- Disturbance / variety regulated: Unsafe repository operations, unauthorized workflow updates and trust/approval boundaries.
- Decisive decision or feedback right: Operator grants/denies actions; identity-level purpose and ultimate policy decision right remains unresolved.
- Decision owner: External operator/permissions and deterministic middleware; no qualifying ultimate agent/parent governor shown.
- Supporting / enforcement mechanisms: WorkflowPushGuard, approval state, run configuration, project/auth controls.
- Closure path: Guarded tool operation → request approval → permitted or denied action, rather than proven ultimate-policy revision and return.
- Why this is / is not agent-owned: Neither a generic tool, approval, stage name nor a model-provider capability is credited without the stated organizational owner and closure.
- Evidence: [agent/middleware/workflow_push_guard.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/middleware/workflow_push_guard.py); [agent/threads/workflow_approval.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/threads/workflow_approval.py); [agent/server.py](https://github.com/langchain-ai/open-swe/blob/d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5/agent/server.py)
- Basis: unknown
- Confidence: low
- Caveats: Static source-grounded mode analysis at frozen SHA; no real provider-backed production run performed.

## Recursion

The main hosted coding agent is an S1 unit. A general-purpose subagent may be delegated but does not automatically imply a metasystem S3 or interference S2. The separately triggered reviewer provides a first-party complementary code-artifact observation route (S3*=A in PR-review mode) that can flag defects for the responsible coding/human actors. External LangGraph implementation internals and unrelated organizations are not borrowed as Open SWE's decisions.

## Variety and escalation

Model-and-tool feedback supports coding operations; independently sampled PR artifacts and actionable published findings provide complementary audit. User approval and tool security policies restrict actions. S2 competing-operational-work regulation, S3 whole-current control, S4 future-capability adaptation and S5 ultimate identity-policy closure remain uncertain under the declared boundary.

## Evidence gaps

Frozen source was inspected, no live provider-run. Need specific inter-S1 interference attenuation/feedback for S2; whole-current multi-operating-unit control/commitment authority for S3; evidence of external prospective organizational capability adaptation for S4; and ultimate purpose-policy decision with returned operations for S5. The S3* positive is limited to the separate supported GitHub PR Reviewer mode with real PR-diff/code inspection and published review findings, not ordinary task self-tests.
