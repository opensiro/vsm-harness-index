---
harness_id: dscode
project_name: DSCode
repository: https://github.com/thinkany-ai/dscode
review_ref: 1ce0328cfa856700f6c955f5429ca00b08d99ea5
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# DSCode

## Review boundary

- System in focus: the first-party DSCode coding-agent runtime at frozen revision `1ce0328cfa856700f6c955f5429ca00b08d99ea5`, including the shipped Core extension, CLI/headless/RPC/Desktop-backed session surfaces, coding tools, permissions/sandboxing, durable sessions/checkpoints, and built-in parallel `delegate` roles.
- Purpose and identity: execute software-engineering work locally through a model/tool coding session, optionally decompose independent work into bounded parallel explorer/implementer/reviewer/tester children, isolate implementation candidates, and return child evidence/diffs to the primary agent for integration.
- Relevant environment: user objectives, project files and Git state, command/test/diagnostic output, model-provider responses, session history/checkpoints, permission/sandbox state, child worktrees and MCP/hooks/project instructions.
- Standard-distribution boundary: DSCode's own Core extension and runtime assembly plus the concretely instantiated coding-session substrate shipped as a normal dependency are inside insofar as DSCode directly wires them into its supported CLI/Desktop/RPC product. External model providers, MCP servers, host OS/container sandbox implementations and unrelated upstream features not instantiated by DSCode remain dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `packages/core/src/dscode-extension.ts`; `packages/core/src/tools.ts`; `packages/core/src/subagents.ts`; `packages/core/src/plan.ts`; `packages/core/src/access.ts`; `packages/core/src/checkpoint.ts`; `packages/core/src/session.ts`; CLI/headless/RPC assembly and Desktop surfaces that instantiate the same Core.
- Adjacent first-party surfaces excluded from ownership: release/CI machinery; maintainer governance; role labels without runtime closure; comparison prose except where corroborated by implementation; and external developer-agent or provider internals.
- First-party operating / deployment modes considered: interactive terminal; one-shot/JSONL; RPC; Desktop; VS Code thin integration; minimal/safe harnesses; plan/ask/auto/full permission modes; parallel delegation; isolated implementers; read-only reviewers; durable/resumable local sessions.
- Recursion level: one DSCode coding organization. The primary model-backed coding session is the main production S1. Delegated implementers are bounded subordinate production S1s. Reviewer children are complementary audit actors. Explorer/tester children are supporting actors unless used in a function-specific closure.
- Reviewed revision: `1ce0328cfa856700f6c955f5429ca00b08d99ea5`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

DSCode ships a local coding-agent product around a shared Core extension used by terminal, headless/RPC and Desktop surfaces. The standard distribution exposes model-facing repository tools, command execution, patching, diagnostics, planning, permissions, sandboxing, sessions, MCP/hooks and durable checkpoints.

The Core registers a model-callable `delegate` tool whose schema accepts up to eight role/task pairs and executes up to four children concurrently. The primary agent is explicitly instructed to delegate only independent work and remains responsible for final integration and verification. Each `implementer` child is launched as a fresh DSCode process inside a detached Git worktree; explorer/reviewer children are read-only, while tester children run focused checks. Child recursion is depth-limited and every result is returned to the primary agent, including a candidate diff for isolated implementers.

This supplies two distinct organizational closures. Parallel implementation has a concrete interference problem: multiple editing workers sharing one checkout could overwrite/observe one another's partial changes. The primary model chooses which independent tasks receive the `implementer` role; DSCode then guarantees separate worktrees for those production children. Complementary review is supplied by a separately invoked `reviewer` child with read-only permission/sandbox and explicit independent-review instructions; its findings are returned to the primary agent as the delegate tool result.

Primary evidence:

- [`README.md`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/README.md)
- [`packages/core/src/dscode-extension.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/dscode-extension.ts)
- [`packages/core/src/tools.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/tools.ts)
- [`packages/core/src/subagents.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/subagents.ts)

## Operational model

The primary DSCode coding actor operates through the standard session/model/tool substrate and the tools DSCode registers. It inspects files, runs commands/diagnostics, applies patches, observes tool results and continues until the current task ends or is interrupted.

When useful, the primary actor calls `delegate` with a list of independent tasks and roles. DSCode runs the children concurrently with a cap of four. Implementers receive isolated Git worktrees and return both textual output and candidate diffs; reviewers run read-only and return independent findings. The parent sees all child results and retains integration/final-verification responsibility.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work through a model-driven coding session that selects tools, observes results and iterates.
- Disturbance / variety regulated: heterogeneous user requests, repository/file/Git state, command/test/diagnostic output, tool failures, model observations, context pressure, permissions and implementation choices.
- Decisive decision or feedback right: choose what evidence to inspect, what coding/command/patch/delegation action to perform next, how to revise work from results and when to finish the task.
- Decision owner: the primary model-backed DSCode coding agent in the supported session runtime.
- Supporting / enforcement mechanisms: DSCode Core tool registration; minimal/safe toolsets; patch/checkpoint path; command sandbox; permissions; sessions; plan state; diagnostics; MCP/hooks; CLI/Desktop/RPC hosts.
- Closure path: user objective + current session/workspace → model selects tool/action → DSCode executes/gates it → result returns into the coding session → model chooses subsequent action or completes.
- Boundary reachability: normal terminal, headless/RPC and Desktop surfaces instantiate the same DSCode Core and coding session without requiring downstream orchestration.
- Why this is / is not agent-owned: removing the model-backed primary actor leaves tools, permission/sandbox and session machinery but removes the open-ended coding judgment that selects and sequences actions.
- Evidence: [`README.md`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/README.md); [`packages/core/src/dscode-extension.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/dscode-extension.ts); [`packages/core/src/tools.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/tools.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference and generic coding-session substrate are dependencies; DSCode is credited for the concrete first-party product composition and organizational roles it exposes.

## S2 — Coordination

- State: A
- Function: attenuate destructive write interference among concurrently executing delegated implementation S1s by assigning them independent Git worktrees.
- Disturbance / variety regulated: two or more implementation children editing the same checkout in parallel could overwrite, race with or observe one another's incomplete changes, making candidate ownership/integration unreliable.
- Decisive decision or feedback right: choose which independent delegated tasks receive the `implementer` role, whose standard semantics include isolated candidate changes rather than shared-workspace mutation.
- Decision owner: the primary model-backed DSCode agent calling the standard `delegate` tool.
- Supporting / enforcement mechanisms: role-bearing delegate schema; explicit model prompt guidelines; four-worker bounded fan-out; per-implementer detached Git worktree creation; per-child cwd; returned candidate diffs; depth-one child boundary.
- Closure path: primary agent identifies independent parallel work → assigns implementation tasks to `implementer` children → DSCode creates a separate worktree for each before execution → children modify isolated repository states → each returns its result/diff → primary agent uses the coordinated outputs for subsequent integration/verification.
- Boundary reachability: `registerSubagentTools` registers `delegate` in the normal DSCode Core and the README documents it as standard parallel work; no external team orchestrator is required.
- Distinct S1 units: two or more concurrently launched `implementer` child DSCode coding sessions, each capable of bounded model/tool software-engineering work.
- Inter-S1 disturbance: parallel implementation children would otherwise share mutable repository state and can overwrite or contaminate one another's in-progress file changes.
- Attenuating coordination relation: DSCode maps the model-selected implementer role to a separate detached Git worktree for each child, removing the shared-write surface while preserving an explicit candidate diff for integration.
- Feedback into subsequent S1 behaviour: isolation changes each child S1's actual working environment before it acts; after completion the primary S1 receives every child result/diff and can choose which candidate to integrate or rework.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping rests on a concrete cross-S1 write-collision disturbance and a first-party isolation relation that specifically attenuates that disturbance. Role names, concurrency and delegation alone are not credited.
- Why this is / is not agent-owned: DSCode deterministically enforces implementer isolation, but the primary model owns the task-specific decision to classify/delegate independent work as implementation tasks under that coordination mode.
- Evidence: [`packages/core/src/subagents.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/subagents.ts); [`README.md`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: explorer/reviewer/tester children do not need the same write isolation. S2=A credits the supported agent-owned role/decomposition decision that invokes the interference-specific implementer path.

## S3 — Inside-and-now control

- State: —
- Function: no distinct first-party whole-organization current-control loop was established.
- Disturbance / variety regulated: the primary agent decomposes work and later receives child outcomes, but reviewed evidence does not expose live descendant-state observation plus substantive mid-run steering/reallocation/commitment control across the child organization.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: delegate task decomposition; concurrency cap; child success/failure/result fan-in; primary integration responsibility; plan/status; permissions and background processes.
- Closure path: not applicable; no whole-system current view → current-control intervention → changed active child commitments/resources loop was reconstructed.
- Why this is / is not agent-owned: initial delegation and final integration remain part of the primary S1's execution/decomposition. The parent waits for bounded child results rather than acting as a live current-control center over them.
- Evidence: [`packages/core/src/subagents.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/subagents.ts); [`packages/core/src/dscode-extension.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/dscode-extension.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: “the primary agent owns integration and final validation” is meaningful responsibility but does not by itself establish the Profile's whole-current S3 closure.

### Absence scope

- Surfaces inspected: delegate fan-out; child process lifecycle; concurrency cap; result aggregation; plan/status; background process controls; checkpoints/sessions; Desktop/RPC status surfaces.
- Plausible first-party paths checked: primary agent as manager; child task assignment; child failure/success visibility; plan state; integration responsibility; abort/process controls.
- Why no material first-party path remains: children are launched as bounded calls and results fan in at completion; no standard model-owned live view plus steering/reallocation path over active child S1 commitments was found.

## S3* — Complementary audit

- State: A
- Function: independently review a producing coding S1's change using a separate read-only model-backed reviewer and return findings to the primary agent.
- Disturbance / variety regulated: the primary/implementer coding path may produce a change that contains correctness defects, regressions or unsupported assumptions.
- Decisive decision or feedback right: independently inspect repository/change evidence in a read-only child context and return a reviewer judgment prioritizing correctness/regressions.
- Decision owner: the separate model-backed DSCode child selected with role `reviewer`.
- Supporting / enforcement mechanisms: model-callable `delegate`; reviewer role instructions; child DSCode process; `--permission plan`; `--sandbox read-only`; independent child context; result aggregation into the parent tool response.
- Closure path: producing S1 has a candidate/change → primary delegates a reviewer task → separate read-only reviewer inspects current repository evidence → reviewer returns findings → DSCode delivers those findings in the `delegate` result → primary agent can revise/integrate/reject subsequent work.
- Boundary reachability: reviewer is a built-in standard role in the normal `delegate` tool and is documented in the shipped product; no custom downstream reviewer code is required.
- Why this is / is not agent-owned: deterministic runtime launches and confines the reviewer, while the semantic review judgment comes from a distinct model-backed child; removing that child removes the complementary audit judgment.
- Evidence: [`packages/core/src/subagents.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/subagents.ts); [`README.md`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: review invocation is model-selected rather than mandatory for every task.
- Claim being audited: the correctness/fitness of a code change or candidate implementation produced by the primary/implementation path.
- Ordinary reporting path: normal primary/implementer coding output and candidate diff/result.
- Complementary access path: a separate reviewer process with read-only permission/sandbox independently inspects repository evidence under explicit correctness/regression review instructions.
- Independence boundary: separate child process/model context, role-specific instructions, read-only execution boundary, no nested delegation and no file-editing role.
- Who acts on findings: the primary DSCode agent receives the reviewer output in the delegate result and owns subsequent integration/fix/verification decisions.

## S4 — Intelligence / adaptation

- State: —
- Function: no material outside-and-future intelligence/adaptation loop was established.
- Disturbance / variety regulated: project instructions, skills, model/provider configuration, sessions and diagnostics enrich future operation, but no autonomous prospective environmental-modeling and persistent adaptation-selection loop was reconstructed.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: AGENTS/CLAUDE instructions; Agent Skills; MCP/hooks; model/provider selection; durable sessions; context compaction; diagnostics.
- Closure path: not applicable; no external/future distinction → adaptation-option generation → autonomous selection → persistent capability/strategy change → later operation closure was found.
- Why this is / is not agent-owned: generic ability to edit project instructions/configuration or use skills is not by itself S4.
- Evidence: [`README.md`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/README.md); [`packages/core/src/dscode-extension.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/dscode-extension.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: downstream workflows can use DSCode to modify durable project configuration; that generic capability is not credited as a closed first-party S4 loop.

### Absence scope

- Surfaces inspected: sessions/compaction; project instructions; skills; MCP/hooks; provider/model settings; diagnostics; subagent roles; checkpoints.
- Plausible first-party paths checked: persistent skill/instruction changes; model switching; reviewer-driven process improvement; session learning; autonomous configuration.
- Why no material first-party path remains: the reviewed mechanisms preserve context or expose configurable capability, but no supported autonomous process owns prospective adaptation selection and persistent organizational change.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy decision loop was established.
- Disturbance / variety regulated: permission modes, sandbox/network boundaries, project trust, hooks and project instructions constrain operation, but they are configured operating policy rather than identity-level governance.
- Decisive decision or feedback right: not established for a genuine identity/ultimate-policy issue.
- Decision owner: user/operator/project configuration for the relevant constraints.
- Supporting / enforcement mechanisms: plan/ask/auto/full permissions; OS/Docker sandbox; network gating; project trust; approvals; AGENTS/CLAUDE instructions; hooks.
- Closure path: not applicable at S5 level; no identity/policy conflict → legitimate ultimate authority → authoritative decision → returned organizational operation loop was established.
- Why this is / is not agent-owned: models operate within selected policy; deterministic enforcement does not become S5 by being strong.
- Evidence: [`README.md`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/README.md); [`packages/core/src/dscode-extension.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/dscode-extension.ts); [`packages/core/src/access.ts`](https://github.com/thinkany-ai/dscode/blob/1ce0328cfa856700f6c955f5429ca00b08d99ea5/packages/core/src/access.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a broader organization can govern DSCode through these controls, but that external parent is not imported without function-specific closure.

### Absence scope

- Surfaces inspected: permission modes; approval/access controller; sandbox/network; project trust; hooks; project instructions; model/provider settings.
- Plausible first-party paths checked: human approvals as parent policy; project trust; AGENTS identity; sandbox/network settings; provider selection.
- Why no material first-party path remains: these surfaces configure/enforce runtime behavior and do not reconstruct a first-party identity/ultimate-policy adjudication function.

## Distributed OSS parent arrangement

Public maintainer/release governance is outside the deployed DSCode coding organization. Human permission/project-trust choices can govern a run, but they are not promoted to S3/S4/S5 without the corresponding function-specific parent closure.

## Self-hosted and non-human modes

DSCode runs locally and supports interactive, headless/CI, RPC and Desktop modes. Autonomous S1, model-owned S2 delegation/isolation, and autonomous S3* reviewer mode remain available without requiring a human in each tool step under suitable permissions.

## Recursion

The focal recursion is one primary DSCode coding session plus its depth-one delegates. Implementer children count as bounded production S1s for the specific delegated tasks, creating the S2 interference problem. Reviewer children are complementary audit actors. This does not imply a persistent multi-agent organization with S3 current-control.

## Variety and escalation

DSCode attenuates variety through permission/sandbox controls, checkpoints, sessions, diagnostics, plans, bounded parallel delegation and specialized child roles. Worktree isolation addresses inter-S1 write interference; read-only reviewer delegation supplies complementary challenge evidence. The remaining lifecycle/configuration mechanisms strengthen operation without independently establishing S3/S4/S5.

## Evidence gaps

No `?` state is required at the frozen revision. Exact-ref implementation establishes the S1, S2 and S3* closures and provides sufficient coverage to bound S3/S4/S5 conservatively.

## Assessment summary

DSCode closes autonomous S1 through its supported coding session, autonomous S2 through model-selected parallel implementation roles mapped to isolated Git worktrees, and autonomous S3* through a separate read-only reviewer child whose findings return to the primary agent. It does not establish live whole-system S3 control, prospective S4 adaptation or identity-level S5.

**Vector:** A · A · — · A · — · —
