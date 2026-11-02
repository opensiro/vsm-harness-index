---
harness_id: cc10x
project_name: cc10x
repository: https://github.com/romiluz13/cc10x
review_ref: 36c7b06a7c846d18cfbf33969ee0a7a2483985af
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# cc10x

## Review boundary

- System in focus: cc10x 12.10.0 Claude Code plugin with a main-session model router, specialized Claude subagents, workflow-specific skills, persisted workflow artifacts and event/hook guards.
- Purpose and identity: route coding, debugging, planning, QA, reviews, triage and maintenance requests into bounded role workflows with independent evidence gates, remediation and durable resume.
- Relevant environment: user request and approved decisions, mutable code workspace, Claude Code agent/tool sessions, scope changes, source findings, plan artifacts, tests, errors and compaction/resume state.
- Standard-distribution boundary: installed plugins/cc10x plugin under Claude Code; main model reads and executes cc10x-router skill, dispatches first-party prompt-defined specialized model agents with Claude's Agent primitive and persists machine-readable state. Claude provider/runtime and target repository are external execution infrastructure.
- Credited operating / distribution surfaces: cc10x-router and workflow references, 14 bundled agent prompts, verification skills, hooks.json, state persistence and artifact-guard Python scripts.
- Adjacent first-party surfaces excluded from ownership: maintainer issue/PR decisions, historical research/benchmark experiments, docs plans and test fixtures. They are sources/context, not runtime governing actors.
- Modes considered: standard Agent-subagent dispatch with task tools or artifact-only graph fallback; reduced/full BUILD, DEBUG, PLAN, REVIEW and QA modes; sanctioned inline fallback when Agent primitive unavailable (does not establish separate audit actor).
- Recursion: one user workflow, main-session router model supervises model-led S1 work/investigation; fresh reviewers and independent verifier are complementary S3* audit lanes.
- Reviewed frozen revision 36c7b06a7c846d18cfbf33969ee0a7a2483985af on 2026-11-02; Profile 0.2.4; Methodology 0.3.7.

## Repository architecture

The router is a first-party skill activated by task intent and instructed to remain the sole workflow dispatcher. It loads or creates a durable UUID-scoped workflow artifact and event log, constructs a dependent graph of Claude subagents, validates each handoff against a structured contract, and advances phases only after results and evidence are persisted. A standard BUILD dispatches component-builder, then parallel read-only code-reviewer and failure-hunter, then read-only integration-verifier, followed by documentation/memory steps. A trivial BUILD still has an independent verifier; scope increase promotes it to the full graph. PLAN invokes a context-clean plan-gap-reviewer, and QA has a separate research, plan-review, harness/execution topology. A failed verifier or blocking finding creates a remediation task followed by re-review and re-verification; authority remains with the router. Hooks persist workflow state through compaction and check subagent output/artifact changes. When Claude Agent dispatch is missing, the documented inline fallback loses agent isolation and is excluded from positive independent-audit inference.

Primary sources: [README](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/README.md), [router](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/SKILL.md), [BUILD workflow](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/references/build-workflow.md), [integration verifier](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/agents/integration-verifier.md), [fresh plan reviewer](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/agents/plan-gap-reviewer.md).

## Operational model

Claude models own coding, investigation, review and orchestration judgments in their respective assigned roles. Python hooks and persisted state enforce record/contract invariants, while the main-session router agent owns the overall task graph and final current workflow decisions. Read-only verifier and fresh review lanes have distinct evidence instructions and deliver their findings back to router remediation, not directly to builder self-certification.

## S1 — Operations

- State: A
- Function: implement, debug, plan, review or execute a targeted coding/QA task through a specialized Claude model agent with tool-feedback iteration.
- Disturbance / variety regulated: unknown code behavior, test failures, integration surprises and findings discovered during the assigned phase.
- Decisive decision or feedback right: worker model selects investigative/implementation steps, reads tool outputs, edits code where authorized and returns contract-structured results.
- Decision owner: dispatched Claude model agent such as component-builder, bug-investigator or QA-executor, according to task type.
- Supporting / enforcement mechanisms: role prompts, agent-common and domain skills, Claude Agent tool, workflow phase artifact, handoff contract checks.
- Closure path: router's phase scope → model agent tools/result interpretation → implementation/evidence → structured report → router records outcome or returns remediation.
- Boundary reachability: official plugin install documents main router + built-in agents, and default task graph calls Claude Agent primitive; separate Task tools are optional with supported artifact-only mode.
- Why this is / is not agent-owned: absent the specialized model, prompts and Python guards cannot choose substantive source edits or judge task evidence.
- Evidence: [router](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/SKILL.md), [builder workflow](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/references/build-workflow.md), [README](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/README.md).
- Basis: explicit + structural.
- Confidence: high for documented/installed role loop; live Claude coding run not reproduced.
- Caveats: external Claude Code provider/Agent primitive required for isolated cells; inline fallback does not prove independent role execution.

## S2 — Coordination

- State: —
- Function: no material first-party regulation of interaction-driven interference between distinct active S1 cells identified.
- Disturbance / variety regulated: reviewer and failure-hunter may independently find issues, but they are read-only and their result aggregation is not an observed inter-agent resource collision.
- Decisive decision or feedback right: none specific to countering S1 peer interference.
- Decision owner: no S2 owner established; task phase graph and conflicts in evidence are resolved by router current-control S3.
- Supporting / enforcement mechanisms: blockedBy task dependencies, serial phase dispatch, parallel read-only review/hunt, artifact scope by workflow UUID and router result aggregation.
- Closure path: no demonstrated peer interference → local coordination correction → changed affected S1 behavior.
- Boundary reachability: no positive S2 mode claimed.
- Why this is / is not agent-owned: parallel agents, role delegation, task dependency edges and validation sequencing are not enough without a concrete S2 variety witness.
- Evidence: [router](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/SKILL.md), [BUILD graph](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/references/build-workflow.md).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: router can handle conflicting audit opinions as current workflow control, but no distinct operational peer-contention loop has been proven.

### Absence scope

- Surfaces inspected: BUILD/QA task graphs, review fanout, workflow state/UUID scoping, workspace isolation offer and router correction logic.
- Plausible first-party paths checked: shared-write collisions, worktree merge conflicts, peer resource contention, independent S1 feedback mediation and revised simultaneous agent allocations.
- Why no material first-party path remains: write work is normally serial and auditors read-only; graph ordering and source-claim adjudication do not evidence interaction-caused S2 disturbances.

## S3 — Inside-and-now control

- State: A
- Function: control the entire current coding workflow across specialized worker, audit, verification, remediation and memory steps.
- Disturbance / variety regulated: contradictory evidence, incomplete phases, failed tests, growing scope, stale state, blocked permissions and budgeted remediation.
- Decisive decision or feedback right: router model interprets user intent, selects workflow/complexity, authors dependent role graph, validates reports, decides remediation escalation versus pause, and re-enters phases until verified.
- Decision owner: first-party instructed main-session Claude router agent, not state-persistence Python hooks.
- Supporting / enforcement mechanisms: cc10x-router skill, UUID-scoped artifact/events, contract envelope validation, phase_exit_gate, task tool or artifact-only graph, remediation history and stop rules.
- Closure path: whole workflow state/agent findings → model router decides next phase or remediation → dispatch and persisted results → updated state and verifier feedback → next model decision.
- Boundary reachability: plugin entry router is installed/activated for ordinary code requests and maintains authority in supported Agent dispatch mode.
- Why this is / is not agent-owned: deterministic guards cannot choose the substantive phase topology, scope negotiation or remedy; those rights belong to router model.
- Whole-system current view: router reconstructs all active phase state, task blockers, results and artifact history within the current workflow UUID and validates graph completion.
- Current-control decision scope: role assignments, phase gates, escalation from trivial/full graph, remediation/re-review chain, accepted user clarifications and stop/continue.
- Evidence: [router](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/SKILL.md), [BUILD reference](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/references/build-workflow.md), [state persistence](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/scripts/cc10x_state_persist.py).
- Basis: explicit + structural.
- Confidence: high for model ownership and standard instructions.
- Caveats: enforced prompt process depends on compliance by external Claude model, and human approval/permission input is not a separate S3 parent mode.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation and planning success claims with fresh or read-only model evidence.
- Disturbance / variety regulated: review anchoring, hallucinated findings, green tests that prove little, unverified user flows and premature phase completion.
- Decisive decision or feedback right: independent read-only integration-verifier executes tests, independently checks code/line evidence and returns PASS/FAIL to router; PLAN uses a fresh anti-anchored plan-gap-reviewer.
- Decision owner: separately dispatched Claude model agents under verifier/reviewer prompts; router receives verdict and controls remediation, rather than self-auditing builder claims.
- Supporting / enforcement mechanisms: isolated Agent dispatch, verifier read-only tools, per-scenario evidence contract, test honesty sweeps, fresh reviewer forbidden to load planner memory, phase exit gate and remedial re-review.
- Closure path: builder/plan output → independently grounded reviewer/verifier evidence → blocking verdict → router creates REM-FIX/re-review and re-verification; only checked PASS advances.
- Boundary reachability: full BUILD, trivial BUILD verifier, DEBUG and PLAN/QA graphs ship mandatory review/verification roles in supported subagent mode.
- Why this is / is not agent-owned: another model agent explicitly reopens code, re-runs tests and adjudicates findings; deterministic gate and router relay rather than make the independent audit judgment.
- Claim being audited: builder task goal/implementation correctness, source findings and phase exit readiness; PLAN mode challenges execution-plan completeness.
- Ordinary reporting path: builder/reviewer structured handoffs and workflow artifact state into the router.
- Complementary access path: separate read-only verifier's own direct code/test/tool observations and fresh plan reviewer's original request/plan/source investigation.
- Independence boundary: verifier has distinct Agent session/tool access and must treat prior claims as UNVERIFIED; fresh plan reviewer excludes prior planner rationale and memory.
- Who acts on findings: router blocks phase advance and schedules bounded remediation or pauses for user, then invokes new verifier.
- Evidence: [verifier](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/agents/integration-verifier.md), [fresh plan reviewer](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/agents/plan-gap-reviewer.md), [router](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/SKILL.md).
- Basis: explicit + structural.
- Confidence: high for standard independent model review-and-return path; live provider audit accuracy not claimed.
- Caveats: supported inline fallback loses independent subagent session; no S3* A inference from inline mode alone.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate outward-facing prospective organizational adaptation cycle established beyond current workflow memory/replay.
- Disturbance / variety regulated: task failure and compaction are managed in present workflow; future external capability shifts not monitored in an evidenced closed path.
- Decisive decision or feedback right: no first-party strategic future-option decision returned into present operating capability.
- Decision owner: none for S4.
- Supporting / enforcement mechanisms: reusable memory patterns, failure history, research agent, skills and session persistence.
- Closure path: no established external horizon → future option → adopted change to current system method.
- Boundary reachability: no positive S4 mode claimed.
- Why this is / is not agent-owned: saving lessons and researching inside a task improves context but does not constitute a distinct outside-and-then intelligence loop.
- Evidence: [router](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/SKILL.md), [README](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/README.md).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: a user can request roadmap research as ordinary workflow work without creating S4 organization.

### Absence scope

- Surfaces inspected: router memory rules, research/plan and QA workflows, workflow persistence, stop hooks and knowledge promotion.
- Plausible first-party paths checked: external change signals, future-scenario distinction, adaptation option selection, authorized capability change and subsequent operational return.
- Why no material first-party path remains: recorded artifacts primarily hold present workflow experience and user requests, not a closed future-external adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no ultimate identity/policy decision loop established.
- Disturbance / variety regulated: user permission gates, scope choices, review confidence and workflow opt-out are per-task operating constraints.
- Decisive decision or feedback right: no first-party identity-level authority or subsequent governance return.
- Decision owner: none for S5; Claude user permissions and project standards govern individual tasks.
- Supporting / enforcement mechanisms: AskUserQuestion, user plan approval, permission settings, safety instructions and no-destructive-action rules.
- Closure path: no identity-level proposal → legitimate authority → ultimate-policy return to agent operating mode.
- Boundary reachability: no positive S5 mode claimed.
- Why this is / is not agent-owned: approvals for edits, branch finishing, risk and plans do not govern organizational identity/ultimate policy.
- Evidence: [router](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/SKILL.md), [BUILD workflow](https://github.com/romiluz13/cc10x/blob/36c7b06a7c846d18cfbf33969ee0a7a2483985af/plugins/cc10x/skills/cc10x-router/references/build-workflow.md).
- Basis: bounded structural absence.
- Confidence: high.
- Caveats: human managers of actual projects may supply independent policy, outside this packaged plugin's recursion.

### Absence scope

- Surfaces inspected: router user gates, project standards, scope approvals, permission and versioned artifact policies, maintainer identity.
- Plausible first-party paths checked: ultimate-policy dispute, legitimate decision forum, identity resolution and return-to-operation binding.
- Why no material first-party path remains: all cited decisions constrain immediate task planning/security; none establishes a separate identity governance loop.

## Distributed OSS parent arrangement

Public contributors maintain plugin code and releases, but no first-party deployed organization-level S3/S4/S5 parent closure follows from a repository workflow.

## Self-hosted and non-human modes

The installed plugin relies on Claude Code hosted locally or remotely. Main-session model routing and isolated subagent validation constitute standard autonomous modes. Optional user plans and permission approvals are not distinct parent governance modes.

## Recursion

Within one user workflow, the router holds S3 authority, specialized model agents own S1 tasks, and independent read-only auditor agents return S3* evidence. Subagent calls are role units rather than automatically nested viable organizations.

## Variety and escalation

Missing contracts, incomplete persistence, blocked phases and failed tests stop advancement; the router uses remediation history and reruns verification. Compaction is bridged by event/artifact state. The independent audit path is diminished in sanctioned inline fallback.

## Evidence gaps

Source/prompt/hook review at frozen SHA, with no live Claude Code or plugin end-to-end test executed. Agent compliance and quality are not claimed. Source-backed positive states use the installed, supported isolated-subagent mode only.
