---
harness_id: loopsmith
project_name: LoopSmith
repository: https://github.com/Mohamed-jarboui/agent-runtime-harness
review_ref: 0c6c7b170bc553be38909800ceb5132e52299e52
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# LoopSmith

## Review boundary

- System in focus: The first-party TypeScript LoopSmith agent runtime and its shipped `workspace-analyst` agent workflow, as instantiated through the CLI and provider configuration.
- Purpose and identity: Execute bounded model-directed tools and workflow tasks with persistent checkpoints, permissions, human approvals, multiple specialist handoffs and optional evidence-checking review.
- Relevant environment: A workspace, variable user goals, file/tool output, live Anthropic/OpenAI-compatible providers or deterministic mock, local persistence, operator permission policy and requested approval.
- Standard-distribution boundary: `@loopsmith/runtime`, workflow engine, orchestrator, provider adapters and first-party CLI/bootstrap/workspace-analyst example installed in the repository; the normal `demo` defaults to deterministic mock, while explicitly supported `--provider anthropic|openai` modes use externally configured live model APIs.
- Credited operating / distribution surfaces: [runtime agent loop](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/packages/runtime/src/agent-runtime.ts), [workflow engine](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/packages/workflow-engine/src/engine.ts), [CLI bootstrap](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/apps/cli/src/bootstrap.ts), [shipped analyst roles](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/agents.ts), [shipped review workflow](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/workflows.ts).
- Adjacent first-party surfaces excluded from ownership: Benchmarks and test-only mock scripts as evidence of live agent decisions, README metrics claims, developer CI, unconfigured third-party MCP servers, external LLM provider reasoning and any hypothetical workflow not included in the reviewed distribution.
- First-party operating / deployment modes considered: Single model agent with selectable tools; allow-listed handoff/delegation; declarative agent/tool/code/approval workflow; flagship workspace-analyst planner → researcher → draft → code verification → distinct reviewer → revision/publish; live-provider and offline-demo modes separately distinguished.
- Recursion level: One configured LoopSmith workflow/goal; specialist roles are task operators rather than independently viable organizations; a separate reviewer supplies complementary evidence against draft production claims.
- Reviewed revision: `Mohamed-jarboui/agent-runtime-harness@0c6c7b170bc553be38909800ceb5132e52299e52` (Apache-2.0).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The first-party `AgentRuntime` builds context from persisted goal/history/memory, requests model output from a configured provider, interprets tool calls/final output/handoff/delegation, applies argument/policy/approval checks, executes tools and returns observations to the model until completion or a bound. `WorkflowEngine` advances a declarative graph with persisted checkpoints, fixed transitions and visits/step caps; its graph routing is not itself another model authority. CLI `boot()` registers the shipped analyst roles and workflows, defaulting to mock for offline runs but allowing configured live providers.

The flagship `workspace-analyst` workflow first has model planner/researcher inspect the workspace, then executor draft a report. A first-party deterministic verification code node checks headings, finding coverage, size and credential-like strings. A **separate reviewer model** with `workspace.read` and `write: deny` is instructed to independently spot-check at least one cited file/line and return `approved` or `needs_changes` plus checked-evidence status. The workflow sends failed review back to the executor, bounded by visit caps, and routes exhausted review to explicit human approval; publication uses a separately gated file write. This is a shipped first-party path, not an injected hypothetical reviewer. See [agent definitions](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/agents.ts) and [workflow definition](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/workflows.ts).

## Operational model

Live model agents choose task-local tool actions and report content; workflow engine/policy constrain possible transitions and effects. In the reviewed analyst mode a different reviewer can directly examine workspace files and veto publication pending draft revision. Static execution limits, policy and human approval are kept separate from organizational S3/S5 claims. The zero-credential mock demo exercises the same orchestration plumbing but does not establish real model discretion or performance.

## S1 — Operations

- State: A
- Function: Context-sensitive, model-directed workspace analysis and report construction through tools, handoffs and feedback.
- Disturbance / variety regulated: Different project files, user objectives, tool responses, untrusted search results, coding/report findings, and reviewer feedback.
- Decisive decision or feedback right: Choose file-inspection/search operations, tool arguments, model-generated findings/draft, and subsequent work from prior observations in configured live provider mode.
- Decision owner: Model actor selected by `AgentRuntime` for the installed analyst role; first-party runtime owns constraints and tool execution, not the substantive task choice.
- Supporting / enforcement mechanisms: Typed tool registry, provider resolution, JSON/tool validation, session/SQLite state, bounded loop, memory, permissions, approval and safe workspace tools.
- Closure path: Goal → model agent receives system/context/tools → chosen tool/delegation or answer → stored tool result/error → updated model context → further choice or terminal workflow result.
- Boundary reachability: CLI registers analyst roles and workflows; documented `--provider` option chooses configured live Anthropic/OpenAI-compatible provider. Default mock mode is explicitly labelled deterministic and not counted as autonomous S1 by itself.
- Why this is / is not agent-owned: Live LLM selects meaningful investigation and writing actions; disabling the model leaves only scripted mock output and deterministic graph/tool enforcement.
- Evidence: [agent runtime loop](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/packages/runtime/src/agent-runtime.ts#L250-L490), [analyst role tools](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/agents.ts), [CLI provider option](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/apps/cli/src/index.ts).
- Basis: explicit + structural first-party live-provider mode.
- Confidence: High for model/tool decision wiring; actual model behavior/quality not exercised.
- Caveats: Live credentials/model endpoint required; offline demo and evaluation suite cannot be substituted for live S1 evidence.

## S2 — Coordination

- State: —
- Function: No specific operational-unit interference attenuation relation with its own feedback is established in the shipped workflows.
- Disturbance / variety regulated: Specialist steps may depend on previous outputs; concurrent/conflicting independent S1 behavior and a correction loop for their interaction are not demonstrated.
- Decisive decision or feedback right: Coordinator role can delegate research and hand off drafting, while graph engine follows author-defined routes; neither detects interaction-generated peer oscillation.
- Decision owner: Model coordinator for task delegation; developer-authored graph/deterministic runtime for ordered transitions.
- Supporting / enforcement mechanisms: Allow-listed `agent.delegate` and `agent.handoff`, bounded depth/count, workflow contexts and conditional transitions.
- Closure path: Coordinator → specialist result → next step, or workflow state → fixed branch; no peer disturbance observation → S2-specific attenuation decision → revised peer commitments loop.
- Why this is / is not agent-owned: Role routing, delegation and deterministic sequence are organizational plumbing, not proof of a distinct S2 regulatory function.
- Evidence: [meta-tools/handoffs](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/packages/runtime/src/agent-runtime.ts#L954-L1077), [coordinator role](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/agents.ts), [workflow](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/workflows.ts).
- Basis: bounded structural absence.
- Confidence: Medium-high.
- Caveats: A developer may compose multiple competing S1 teams with custom coordination, outside this reviewed installed mode.

### Absence scope

- Surfaces inspected: Runtime handoff/delegate, workflow DSL/engine, shipped agent roles, flagship analyst and generic plan-execute-review workflows.
- Plausible first-party paths checked: Coordinator as S2, workflow conditional branches as conflict regulation, parallel specialist interactions, review loop as peer coordination.
- Why no material first-party path remains: Reviewed roles operate in a prescribed task dependency chain; their feedback corrects report quality, not interaction-induced interference between independent S1 units.

## S3 — Inside-and-now control

- State: —
- Function: No distinct discretionary whole-system present-control authority over a portfolio of operational commitments is shown.
- Disturbance / variety regulated: Excessive tool calls, unsafe writes, retries, failed rubric checks and pending approvals; these are bounded by limits/gates within one task workflow.
- Decisive decision or feedback right: Developer authors workflow transitions and caps; reviewer judges the report as a specific QA result; human approves individual writes, but no owner revises multiple S1 resource/priority commitments from a current whole-system view.
- Decision owner: Operator/developer for envelope, runtime for deterministic steps and human for write permission; no separate cross-operational S3 manager in standard mode.
- Supporting / enforcement mechanisms: Persistent workflow checkpoints, `maxSteps`/`maxVisits`, permission engine, approval state and structured reviewer verdict route.
- Closure path: Draft → verification/review → revise/publish or human gate; this is local artifact acceptance, not whole-operating-system resource/commitment balancing.
- Why this is / is not agent-owned: LoopSmith may be a reusable control-plane foundation, but it does not package a whole-portfolio S3 actor in the reviewed workflows; generic graph transitions alone do not count.
- Evidence: [workflow graph](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/workflows.ts), [workflow engine](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/packages/workflow-engine/src/engine.ts), [permission defaults](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/README.md).
- Basis: bounded structural absence.
- Confidence: Medium-high.
- Caveats: Higher-level orchestration/portfolio policy may be built by a customer from provided interfaces; no shipped specific owner/closure is established here.

### Absence scope

- Surfaces inspected: Runtime bounds, workflow engine, CLI bootstrap, analyst roles and reviewer, tool permissions and approval process.
- Plausible first-party paths checked: Workflow graph as S3 control, reviewer quality gate as S3, coordinator task delegation as S3, approval and event metrics as whole-system control.
- Why no material first-party path remains: These regulate one workflow artifact or enforce configured limits without cross-S1 current view and legitimate consequential resource/commitment reallocation.

## S3* — Complementary audit

- State: A
- Function: Evidence-facing independent report review, distinct from the report writer and fixed structural validators, with corrective return.
- Disturbance / variety regulated: Generated reports can omit findings, cite nonexistent file lines or inaccurately describe workspace evidence while passing basic formatting checks.
- Decisive decision or feedback right: Dedicated reviewer agent returns `approved`/`needs_changes`, identified issues and explicit `checkedEvidence` judgments after spot-checking cited source with read-only tool.
- Decision owner: Separate `reviewer` model role in shipped analyst workflow; the graph engine routes its verdict and the executor addresses findings.
- Supporting / enforcement mechanisms: Reviewer `tools:['workspace.read']`, `permissions:{write:'deny'}`, model instruction to inspect cited file/line, typed ReviewSchema and deterministic pre-review `verifyReport` structure checks.
- Closure path: Researcher findings → executor draft → deterministic structure/coverage check → distinct reviewer reads cited source and renders verdict → failed verdict routes to draft revision with reviewer feedback → re-review or human escalation on visit cap.
- Claim being audited: Draft technical improvement report accurately and completely presents workspace findings with valid citations and safe content.
- Ordinary reporting path: Researcher model findings and executor model draft placed in workflow state; writer's own output is the completion claim.
- Complementary access path: Reviewer has separate `workspace.read` access to actual workspace files and a required cited-line spot check, with structured `checkedEvidence` results; deterministic verifier supplies additional independently computed format checks.
- Independence boundary: Named reviewer model role distinct from executor and researcher, its permissions deny file writes and it can directly inspect original code. It shares configured provider infrastructure and is not an external independent auditor; structural independence is at role/readonly-tool boundary.
- Who acts on findings: Conditional workflow routes non-approval back to executor `draft`, inserting prior reviewer feedback; after visit limit, it asks a human whether to publish despite unresolved issues.
- Boundary reachability: `apps/cli/src/bootstrap.ts` registers `analystAgents`/`analystWorkflows`; `workspace-analyst` is advertised in the README and has the review/return path first-party installed.
- Why this is / is not agent-owned: The reviewer makes a discretionary evidence-verification judgment separate from writer's normal self-report; the code rule alone is not credited as S3*.
- Evidence: [reviewer role/permissions](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/agents.ts), [review and revision closure](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/workflows.ts), [installed bootstrap](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/apps/cli/src/bootstrap.ts#L127-L133).
- Basis: structural explicit first-party review closure.
- Confidence: High for shipped definitions; moderate for live-model behavior because standard `demo` is deterministic.
- Caveats: A single spot check is bounded evidence, not exhaustive verification. Structural checks and external provider performance cannot replace actual independent model review.

## S4 — Outside-and-then intelligence

- State: —
- Function: No closed future-environment sensing and strategic adaptation loop changing the harness's future organizational capabilities.
- Disturbance / variety regulated: Historical memory and observations are used to answer the current task; provider fallback handles present availability rather than long-term adaptation.
- Decisive decision or feedback right: Developer/operator changes prompts, agents, workflows and provider config; model planner selects current investigation steps only.
- Decision owner: Developer/operator for prospective capability changes, task agents for current workflow.
- Supporting / enforcement mechanisms: Persistent memory, context compaction, configurable workflow templates, model/provider registry, evaluation CLI.
- Closure path: Stored observations → current task context or test report; no external-future model → adaptation choice → capability-configuration feedback.
- Why this is / is not agent-owned: Persistence, task planning and model fallback are not sufficient for future-facing organizational intelligence.
- Evidence: [context management](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/README.md), [planner instructions](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/examples/workspace-analyst/src/agents.ts), [CLI evaluation](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/apps/cli/src/index.ts).
- Basis: bounded structural absence.
- Confidence: High.
- Caveats: External builders could use benchmarks and workflow reports to guide future strategy, but that is not a first-party installed feedback path.

### Absence scope

- Surfaces inspected: Memory/context, planner/reviewer roles, provider fallback, workflow templates, evaluations and example implementation.
- Plausible first-party paths checked: Persistent FTS memory as adaptation, retry/fallback as environmental intelligence, benchmark as future-facing S4, plan/review as strategic learning.
- Why no material first-party path remains: Each supports current operations, error recovery or offline developer assessment; no prospective decision actor revises future organizational capabilities through a closed return.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate-purpose or identity dispute arbitration beyond per-operation permission rules and human action consent.
- Disturbance / variety regulated: Unsafe tool arguments, writes, external MCP calls, destructive execution and untrusted input.
- Decisive decision or feedback right: Operator configures policies and human approves particular side effects; no packaged S5 actor decides durable system purpose or constitutional boundaries.
- Decision owner: External operator/human for static permission config/individual approval, deterministic policy engine for enforcement.
- Supporting / enforcement mechanisms: Allow/deny/require-approval categories, persistent approvals, workspace sandbox and secret redaction.
- Closure path: Tool request → permission check or human approval → execute/deny/resume, not identity-level dispute → legitimate ultimate authority decision → enduring organizational mandate.
- Why this is / is not agent-owned: Model cannot override tool policy, and approvals are narrow operational gates, not ultimate policy identity choices.
- Evidence: [permission engine](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/packages/policies/src/policy-engine.ts), [human approvals](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/packages/policies/src/approvals.ts), [README boundaries](https://github.com/Mohamed-jarboui/agent-runtime-harness/blob/0c6c7b170bc553be38909800ceb5132e52299e52/README.md).
- Basis: bounded structural absence.
- Confidence: High.
- Caveats: User's external organization may have its own S5 beyond this library.

### Absence scope

- Surfaces inspected: Permissions, approvals, tool executor and sandbox, workflow engine, CLI config and flagship agent roles.
- Plausible first-party paths checked: Permission policy as constitution, approval as S5, workflow goal as identity, reviewer final verdict as legitimate policy authority.
- Why no material first-party path remains: These set execution rules or judge task artifact readiness; no identity/purpose-level conflict-resolution loop with an enduring authoritative return is installed.

## Recursion

The runtime can delegate tasks or transfer execution ownership and build agent pipelines, but a configured workflow is one operational organization. A nested agent role or model call is not shown to possess its own viable metasystem; no independent recursively viable team is inferred.

## Variety and escalation

Typed tools and model planning amplify S1 response variety. Allow-list permissions, limits, schema validation and sandbox attenuate risky tool choices. The independent reviewer supplies complementary evidence access and revision pressure; human approvals govern side effects or exhausted review loops. None implies autonomous S5 or automatic prospective S4.

## Evidence gaps

- Source-traced first-party implementation at the frozen ref; no paid-provider E2E was run, and deterministic demo/tests do not establish real model quality.
- The optional live provider mode requires operator-supplied endpoint/keys. Unconfigured customer workflows and MCP integrations are not silently credited.
- Reviewer is structurally independent of report writer and has read-only workspace tool, but is not a separate institutional auditor and is instructed to spot-check only some evidence.
- Negative functions apply to the installed standard workflow, not arbitrary compositions built using these libraries.
