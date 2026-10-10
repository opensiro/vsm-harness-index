---
harness_id: octo
project_name: Octo
repository: https://github.com/open-octo/octo-agent
review_ref: d68cd81aed46c999e1d413ac8c0b4c3f7b324b23
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: —
---

# Octo

## Review boundary

- System in focus: shipped Octo Go coding-agent system including native model/tool loop, coding tools, session/task state, first-party subagent Spawner, builtin reviewer profile, implement/review skills and reachable CLI/server interfaces.
- Purpose and identity: autonomously complete coding tasks and, in the shipped implementation mode, coordinate separately executing coding agents with independent review.
- Relevant environment: user-selected repository, filesystem/shell, upstream model provider, local tasks, project design/acceptance tests, changing source code and operator permission boundaries.
- Standard-distribution boundary: first-party code/tools/skills bundled in the runnable Octo distribution; no ownership credited from third-party model, MCP, OS program, plugin or privately written user workflow.
- Credited operating / distribution surfaces: internal/agent, internal/app/spawner.go, internal/tools, internal/agentprofile/builtins.go, internal/workflow, first-party bundled implement and code-review skills, first-party CLI/server wiring.
- Adjacent first-party surfaces excluded from ownership: dev-docs design-only proposals, project contributor CI/release organization and tests, web/mobile presentation absent runtime closure, external editor extension repos and third-party service behavior.
- First-party operating / deployment modes considered: standard local agent turn, sub_agent tooling, native bundled implementation-slice coordination, built-in code-review audit, operator-configured permissions, persisted sessions/memory and optional workflow engine.
- Recursion level: one coding project under an Octo implementation organization; nested coding agents are separate local operational cells only when they own task work with meaningful discretion.
- Reviewed revision: d68cd81aed46c999e1d413ac8c0b4c3f7b324b23.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The native Go Agent.Run/RunStream loop supplies tools to a model, permission-gates requested execution, records responses and sends tool results into the next model decision. Native tools can read/edit repository files, run commands and perform searches. Sessions are persisted as JSONL for later continuation. The builtin sub_agent tool resolves a typed profile, launches a separate child Agent with isolated history/budget, and returns synchronous results or asynchronous completion notifications depending on its transport. The project also provides a first-party Ruby workflow DSL that invokes the same child-runner but arbitrary user scripts do not automatically donate VSM functions.

The bundled implement skill is a substantive operating composition: create dependency waves, assign each child disjoint files, isolate work in worktrees, track slice status, review/test/merge output, and resolve failures before moving to the next wave. The bundled code-review skill invokes a fresh independent read-only reviewer when implementation was performed in the parent context. Audit findings return to the parent for verification and repairs. These optional first-party modes, not mere topology/feature names, supply the assessed coordination, whole-current-control and complementary-audit paths.

Primary source examples: https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/agent/agent.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/app/spawner.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/tools/agent.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/agentprofile/builtins.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/skills/defaults/implement/SKILL.md ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/skills/defaults/code-review/SKILL.md ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/workflow/runtime.go.

## Operational model

The top-level agent performs S1 coding work through iterative tool decisions. During shipped implement-mode multi-agent operation, the same agent partitions shared work and reconciles independent child outcomes with a whole-project progress view. Worktree branches and task ledgers are supporting mechanisms; the agent owns coordination/current-control judgments. The optional code-review agent conducts separate-source audit and returns prioritized findings to the parent implementer. Model-provider inference, deterministic concurrency gates, and user permissions cannot independently donate autonomy or any higher VSM organizational decision right.

## S1 — Operations

- State: A
- Function: Autonomous repository/coding task execution with tool use.
- Disturbance / variety regulated: Uncertain task and environment, changing files, tool output and failures.
- Decisive decision or feedback right: Select/revise the next operational tool action after receiving prior results.
- Decision owner: Octo primary model-driven agent.
- Supporting / enforcement mechanisms: Go agent loop, tools/permission gate, session storage and provider interface.
- Closure path: Task → model tool call → tool execution → result in model context → new decision / completion.
- Boundary reachability: CLI/server directly invoke the first-party agent Run or RunStream loop with registered tools.
- Why this is / is not agent-owned: The agent selects operational actions; deterministic tools execute them.
- Evidence: https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/agent/agent.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/README.md ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/agent/session.go
- Basis: structural + explicit
- Confidence: high
- Caveats: Inference provider and optional human action approval remain external/configured limits.



## S2 — Coordination

- State: A
- Function: Attenuate interference between separate coding subagents in a project-level implementation wave.
- Disturbance / variety regulated: Two workers modifying overlapping repository files can create merge conflicts, oscillation or incompatible slices.
- Decisive decision or feedback right: Partition wave and non-overlapping file ownership, choose isolation, react to detected merge conflicts.
- Decision owner: Top-level implementing model/agent in the shipped implement-skill mode.
- Supporting / enforcement mechanisms: Isolated worktrees, subagent manager, slice ledger, branch/merge tooling.
- Closure path: Agent forms disjoint wave → children edit independently → branches/results return → parent resolves collision and revises the next wave.
- Boundary reachability: Standard bundled implement skill invokes first-party sub_agent and terminal; first-party Spawner/worktree machinery is reachable.
- Why this is / is not agent-owned: Model decides partition and reconciliation; worktrees and git only enforce/expose chosen separation.
- Evidence: https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/skills/defaults/implement/SKILL.md ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/app/spawner.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/app/worktree.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/tools/agent.go
- Basis: structural + explicit
- Confidence: medium
- Caveats: A is supported in the bundled implementation/review operating mode, not automatically in every ordinary chat.

- Distinct S1 units: two or more autonomous general coding subagents executing independent implementation slices.
- Inter-S1 disturbance: materially overlapping edits and conflicting branches when separate S1 units change a shared checkout.
- Attenuating coordination relation: agent-assigned disjoint file sets plus worktree isolation and reviewed integration.
- Feedback into subsequent S1 behaviour: merge result/conflict or test failure changes the parent's reconciliation, repair and next-wave decisions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the procedure explicitly tackles an actual structurally evidenced collision mode and conditions later work on resolving it.

## S3 — Inside-and-now control

- State: A
- Function: Whole-current regulation of multiple slice commitments and shared delivery/review constraints.
- Disturbance / variety regulated: Partial implementation, failed tests or design violations can jeopardize the entire current coding project.
- Decisive decision or feedback right: Choose sequential/parallel waves, prioritize and repair failing slices, approve progression after reviewing all wave outcomes.
- Decision owner: Top-level coordinating model/agent in bundled implement skill.
- Supporting / enforcement mechanisms: Implementation state file, task store, subagent manager, review status and test tooling.
- Closure path: Global progress ledger + child outcomes → parent assesses current constraints → fixes, reorders, merges or stops → next operational wave.
- Boundary reachability: Bundled implement procedure is offered as a native skill and uses shipped subagent/terminal/session mechanisms rather than an external project manager.
- Why this is / is not agent-owned: The agent exercises current multi-unit commitment decisions; fixed budgets/locks are supporting enforcement.
- Evidence: https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/skills/defaults/implement/SKILL.md ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/tools/tasks.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/tools/subagent_manager.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/app/spawner.go
- Basis: structural + explicit
- Confidence: medium
- Caveats: A is supported in the bundled implementation/review operating mode, not automatically in every ordinary chat.

- Whole-system current view: implementation-state ledger tracks all active slices, their wave, file ownership, review, tests and completion status.
- Current-control decision scope: which work may run, what must be repaired before releasing the next wave, and when verification/merging closes shared commitments.

## S3* — Complementary audit

- State: A
- Function: Independent check of code-change claims with findings returned for correction.
- Disturbance / variety regulated: A coding agent can report an apparently completed change that fails correctness/security/design checks.
- Decisive decision or feedback right: Read-only fresh reviewer decides defects and severity from directly inspected files/diffs; implementing agent chooses and performs correction.
- Decision owner: Fresh-context autonomous built-in code-review child for audit judgment, parent implementing agent for remediation.
- Supporting / enforcement mechanisms: Reviewer profile, Spawner isolated conversation, git diff/read tools, bundled code-review and implement procedures.
- Closure path: Implementation claim/diff → independent fresh reviewer examines actual source → findings → parent verifies and repairs Important/Critical findings before subsequent wave.
- Boundary reachability: A built-in read-only code-review profile is registered in first-party code; shipped skills invoke it via first-party sub_agent in the standard implementation mode.
- Why this is / is not agent-owned: The separate model auditor forms its own source-based judgment, not a deterministic pass/fail gate over the original report.
- Evidence: https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/agentprofile/builtins.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/tools/agent.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/app/spawner.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/skills/defaults/code-review/SKILL.md ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/skills/defaults/implement/SKILL.md
- Basis: structural + explicit
- Confidence: medium-high
- Caveats: A is supported in the bundled implementation/review operating mode, not automatically in every ordinary chat.

- Claim being audited: correctness, safety, test coverage, conventions and design compliance of the implemented code change.
- Ordinary reporting path: completing implementer/subagent response and persisted slice status.
- Complementary access path: fresh read-only code-review agent reads actual changed files and git diff.
- Independence boundary: zero inherited implementation conversation, distinct reviewer persona and tool slice.
- Who acts on findings: implementing parent checks reviewer findings, repairs Critical/Important ones and gates next wave.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Prospective environment-facing adaptation not resolved by the reviewed structural evidence.
- Disturbance / variety regulated: Future requirements may require changed operating repertoire, beyond retrospective session/context storage.
- Decisive decision or feedback right: Not established: whether the first-party harness decides external/future options and returns them into capability.
- Decision owner: Unknown; user/model can write memory and skills but the higher adaptation decision topology remains open.
- Supporting / enforcement mechanisms: Memory files, skills, workflow replay and creation, model configuration.
- Closure path: Stored memory can affect later sessions, but no sufficiently established prospective environment → option → adaptation decision → current-capability closure.
- Why this is / is not agent-owned: Persisting facts and configurable reusable tools is not automatically an S4 adaptation loop.
- Evidence: https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/docs/src/content/docs/guides/memory.md ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/workflow/runtime.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/agent/session.go
- Basis: structural + unknown
- Confidence: low
- Caveats: Detailed source-native investigation of skill/workflow adaptation is still required.



## S5 — Policy and identity

- State: —
- Function: No evidenced first-party identity/ultimate-policy closure at the assessed coding recursion.
- Disturbance / variety regulated: Global purpose/policy contradiction beyond ordinary action permissions not closed in the reviewed runtime.
- Decisive decision or feedback right: No S5-specific decisive policy or identity decision established.
- Decision owner: Human operator configures permissions and model; deterministic runtime enforces selected constraints.
- Supporting / enforcement mechanisms: Static identity/system prompts, permissions engine, tool approval, user-configured model/skills.
- Closure path: Human command approval permits or refuses one tool operation; no evidenced issue → ultimate authority → authoritative return to subsequent organizational identity/policy.
- Why this is / is not agent-owned: Action approval, global permission policy and prompt text do not by themselves establish S5 ownership.
- Evidence: https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/permission/permission.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/README.md ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/agent/session.go ; https://github.com/open-octo/octo-agent/blob/d68cd81aed46c999e1d413ac8c0b4c3f7b324b23/internal/skills/defaults/implement/SKILL.md
- Basis: structural + explicit
- Confidence: medium
- Caveats: This is a boundary-relative conclusion, not a proof that humans cannot define policy.

### Absence scope

- Surfaces inspected: project README and architecture; first-party agent/tool loop, model/session/permission paths; builtin profiles and subagents; bundled implement/code-review skills; workflow and memory interfaces.
- Plausible first-party paths checked: model/system identity prompt, human tool approvals, fixed permission policies, profile switching, developer-defined workflow and contributor governance.
- Why no material first-party path remains: these mechanisms constrain lower-level tasks or configure an operator's runtime, but do not evidence identity/ultimate-policy adjudication with a legitimate return/closure into subsequent operation at this recursion.

## Distributed OSS parent arrangement

Public GitHub contributor development, issue handling and CI are adjacent to the installed user-facing coding harness. Independent contributors running their own Octo instances do not become a common parent-governed S3/S4/S5 system merely by committing code in the same upstream repository.

## Self-hosted and non-human modes

The runtime offers local autonomy plus configurable operator restrictions. Human-permission prompts are action-level gates; no function-specific parent mode is claimed. A multi-agent implementation under Octo can have an autonomous agent making coordination/current-control judgments while external human operator rules constrain individual actions.

## Recursion

Focal boundary is an Octo-run coding project, where a child general-purpose coding agent can have a local S1 environment. A child process or model call is not automatically another viable recursion; the coordinator and audit are identified functionally.

## Variety and escalation

Tool failures and context observations return into the model loop. Implementation merges, reviews and tests expose cross-agent interference and current delivery problems. The implementing agent resolves those feedback signals before advancing, while permissions and limits enforce configured guardrails. Exceptional messages are not automatically a separate VSM system function.

## Evidence gaps

- S2 and S3 are mode-specific, structurally evidenced by shipped implement instructions plus runnable first-party machinery; confirm concrete correction sequences independently before quantitative capability claims.
- S3* is mode-specific and requires actual invocation of the fresh read-only reviewer, not merely the presence of a profile name.
- S4 is undecided: model-authored memory, saved workflows and extensibility are not automatically a prospective external adaptation loop.
- Review is of pinned source, not a benchmark run or success-rate measurement. This proposal must pass independent semantic review and exact-head validation before canonical admission.
