---
harness_id: universal-agentic-os
project_name: Universal Agentic Engineering OS
repository: https://github.com/3mar-baha/universal-agentic-os
review_ref: 04ee2b7cea82c87679b404771961f3cddafb4ef0
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Universal Agentic Engineering OS

## Review boundary

- System in focus: the **standard first-party Bash/PowerShell scripts, hook settings, prompts and lifecycle orchestration** in Universal Agentic Engineering OS v1.4.6.1 at frozen source revision, rather than a composed installation of upstream cognitive coding agents.
- Purpose and identity: guide external AI coding agents and a user through discovery, spec acceptance, implementation worktrees, tests, second-pass quality guards, merge and release; provide a reusable engineering governance and orchestration toolkit across domains.
- Environment: task goals and repo workspaces, local shell/git/runtime tools, upstream toolkit repositories, installed Claude Code/OpenCode/Codex/Cursor/Windsurf coding assistants, hosted inference providers configured for those external programs, user-led review and release management.
- Standard-distribution boundary: pinned repo `scripts/*.sh`, `vantrilex.ps1`, `.claude/` settings/hooks, `.githooks`, `CLAUDE.md`, `AGENTS.md`, `skills/`, `docs/` and tests. **Do not assign proprietary or independently implemented Claude Code/OpenCode/Codex reasoning or their native tool loops to this repository** merely because a PowerShell wrapper launches them. Prompts are first-party authored but require an external consuming agent runtime to close discretionary decisions.
- Credited operating / distribution surfaces: [vantrilex.ps1](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/vantrilex.ps1); [scripts/uos.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/uos.sh); [scripts/dispatch-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/dispatch-worktrees.sh); [scripts/merge-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/merge-worktrees.sh); [scripts/orchestrate-stage.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/orchestrate-stage.sh); [scripts/teardown-stage.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/teardown-stage.sh); [scripts/setup-toolkit.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/setup-toolkit.sh); [scripts/init.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/init.sh); [scripts/new-project.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/new-project.sh); [scripts/release.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/release.sh); [.claude/settings.json](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/.claude/settings.json); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md); [AGENTS.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/AGENTS.md); [CLAUDE.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/CLAUDE.md); [docs/05-INITIAL-PROMPT.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/docs/05-INITIAL-PROMPT.md); [tests/workflow-tests.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/tests/workflow-tests.sh).
- Adjacent first-party surfaces excluded from ownership: externally installed coding agents, their native LLM/action loop, independent model endpoints, six upstream toolkit repositories and their agent implementations, GitHub/CI task runner, user/developer approval and planning decisions. The configured MCP server/runtime outside the repo does not become a first-party autonomous actor simply via configuration.
- First-party operating / deployment modes considered: Windows Vantrilex interactive launch for Claude Code, OpenCode and Codex with DeepSeek/OpenRouter/Orca/custom provider settings; user invokes `uos init/new/plan/dispatch/merge/doctor/ship/release` on Bash; native Claude Code hook lifecycle and stage kit injection; any coding assistant reads AGENTS.md / CLAUDE.md and follows the manually supplied initial prompt; Git worktree parallelism, three-strike circuit breaker and second-pass test/quality/release gates.
- Recursion level: one externally driven development project with parallel issue worktrees and Leader/Guide/Implementer **roles defined by written contracts**; no first-party internal agent worker with substantive open-ended model/tool choices. The composed external human/Claude/OpenCode/Codex organization may have multiple functions, but its decisional autonomy cannot be imported as this repository's own.
- Reviewed revision: `3mar-baha/universal-agentic-os@04ee2b7cea82c87679b404771961f3cddafb4ef0`, exact Git tree `f853faebf695b0b6a917e9271899f6c889f6533e`, GitHub repo ID 1343801790; created 2026-08-23T13:31:09Z, public nonfork nonarchived, MIT, default main.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

This is a substantial, real, first-party **workflow-construction and governance toolkit**. `scripts/new-project.sh` scaffolds 16 canonical project files, installs shell/Claude hooks and makes the project ready for engineering. `scripts/uos.sh` provides plan, doctor, status, dispatch, merge and release frontends; for example `cmd_plan()` scans the checkpoint milestone lines, derives the first open milestone slug and prints an actionable dispatch command **without a model call**. `scripts/orchestrate-stage.sh` removes stale phase context and injects fixed toolkit skills and agent prompt files from external upstream toolkits; `scripts/dispatch-worktrees.sh` creates isolated Git worktrees with a briefing; `scripts/merge-worktrees.sh` runs diff-scoped `bash -n`, shellcheck and Markdown lint gates and merges/refuses branches. Circuit-breaker policy, Git hooks, quality gates and release scripts can block unsafe work or failed tests. The machinery is concrete, useful and its state transitions execute without requiring a model. [scripts/new-project.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/new-project.sh); [scripts/uos.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/uos.sh); [scripts/orchestrate-stage.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/orchestrate-stage.sh); [scripts/dispatch-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/dispatch-worktrees.sh); [scripts/merge-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/merge-worktrees.sh); [scripts/release.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/release.sh); [tests/workflow-tests.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/tests/workflow-tests.sh).

The decisive autonomous *thinking, coding, tool interpretation and correction*, however, belongs to third-party agent programs. The standard user-facing [Vantrilex launcher](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/vantrilex.ps1#L622-L632) builds endpoint environment variables and arguments, then directly executes one of `& npx '@anthropic-ai/claude-code@latest' @AllArgs`, `& npx 'opencode-ai@latest' @AllArgs`, or `& npx '@openai/codex@latest' @AllArgs` (lines 630–632). `AGENTS.md` explicitly addresses any *other* existing agent and tells it to read `CLAUDE.md`, role/skill instructions and checkpoint; without installing an external coding-agent runtime there is **no first-party provider request / tool invocation / observation / new-model-decision loop**. Setting `ANTHROPIC_MODEL`, `ANTHROPIC_AUTH_TOKEN`, `OPENAI_API_BASE` or Codex model-provider overrides does not turn this PowerShell source into its own agent; those are arguments to upstream third-party runtimes. [vantrilex.ps1](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/vantrilex.ps1); [AGENTS.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/AGENTS.md); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md); [CLAUDE.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/CLAUDE.md); [README.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/README.md).

The README states Leader decomposition, Guide approval and Implementer TDD rights; those are **contracts for whoever inhabits externally executed agent roles** and/or a human Guide, not distinct first-party agent services. First-party shell guards do retain authority to refuse certain unsafe dispatches, unapproved checkpoint transitions and merging changed files failing deterministic tests. The distinction is not between useful and useless, or real and fake automation; it is between enforcement/construction on the one hand and the decisive *agent-owned organizational* functions required by the normative Profile on the other. [README.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/README.md); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md); [docs/04-QUALITY-GATES-AND-SAFETY.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/docs/04-QUALITY-GATES-AND-SAFETY.md); [scripts/dispatch-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/dispatch-worktrees.sh); [scripts/merge-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/merge-worktrees.sh).

## Admission judgment

**Status: excluded-no-agentic-vsm at this frozen standard-distribution boundary.** The system intentionally helps a *composed* external AI-agent organization execute real coding missions. But no native first-party S1 model/tool feedback actor closes operations: that role is explicitly delegated to separate Claude Code/OpenCode/Codex or a user-provided agent. Accordingly it does not meet this Methodology's general autonomous-harness Index admission condition, even though substantial first-party workflow, control, safety, coordination and quality infrastructure is present. The six negatives are **bounded source-ownership findings**, not a verdict about the usefulness of this system, or the viability of a deployment combining third-party agents.

## Operational model

External actor selects and reasons over project mission → first-party launcher/config and context scripts provision the environment → upstream coding-agent's own agent loop operates on repo via tool calls → first-party hooks/guards/checkpoints enforce safety → external Guide/Leader reviews and invokes merge/release helpers. The first-party scripts do not decide what implementation is semantically required next, whom to delegate novel work to or how to interpret arbitrary tool observations. Even when scripts run without an agent, they can scaffold/check/lint/merge governed work but cannot invent/choose task-specific code.

## S1 — Operations

- State: —
- Function: Repository-supplied native worktree/code-development tools do not themselves execute a first-party autonomous agent deciding substantive coding, research or business tasks.
- Disturbance / variety regulated: Novel user specifications, test failures, architecture choices, tool observations and open-ended implementation tasks.
- Decisive decision or feedback right: Interpret an open user goal, select next code/tool acts, inspect resulting tests and decide task-specific corrections until delivery.
- Decision owner: The configured **external** Claude Code, OpenCode or Codex agent launched by vantrilex, or any already-open external assistant instructed via AGENTS.md/CLAUDE.md; the local shell scripts deterministically scaffold and gate files.
- Supporting / enforcement mechanisms: Model/provider CLI environment maps and launch arguments; phase/context kit injection, worktrees, TDD/merge/release shell gates, checkpoint and human Guide signoff instructions.
- Closure path: User picks launcher prompt + provider + agent → vantrilex provisions/sets environment and runs npx external coding-agent package → upstream runtime owns model/tool reasoning and task-action loop → first-party scripts supply context and enforce deterministic boundary/merge tests. The first-party code does not make independent task-specific model decisions or consume observations in its own model-controlled action loop.
- Why this is / is not agent-owned: Under the owner counterfactual, remove the externally installed agent packages and user-driven agent decisions but keep all first-party scripts, prompts and phase machinery: new projects can be scaffolded, dependencies injected and tests gated, but no autonomous engineering worker decides code/repair actions. Direct provider URLs in the PowerShell launcher configure upstream clients; they do not themselves implement an internal provider inference/tool-act loop.
- Evidence: [vantrilex.ps1](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/vantrilex.ps1); [AGENTS.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/AGENTS.md); [CLAUDE.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/CLAUDE.md); [scripts/uos.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/uos.sh); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md); [scripts/dispatch-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/dispatch-worktrees.sh); [scripts/orchestrate-stage.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/orchestrate-stage.sh); [scripts/new-project.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/new-project.sh)
- Basis: explicit source and launch-call ownership
- Confidence: High.
- Caveats: This is a repository-relative first-party autonomy conclusion, not a claim that a composition with Claude Code/OpenCode/Codex cannot build software.

### Absence scope

- Surfaces inspected: PowerShell vantrilex agent/provider execution switch, all Bash scripts, AGENTS.md/CLAUDE.md operating prompts, bundled skills, native hooks, tests and README.
- Plausible first-party paths checked: Examined Claude/OpenCode/Codex direct startup, custom model endpoints and their actual CLI invocation, Bash orchestration and worktree pipeline for any separate internal model SDK/API actor or first-party thought/tool/observation loop.
- Why no material first-party path remains: Every nontrivial open-ended agent action is delegated to npx-installed third-party agent CLIs or the human user; the shipped repository has no independent first-party model/tool-feedback task actor.

## S2 — Coordination

- State: —
- Function: No first-party regulatory attenuation of mutual operational disturbances among independently continuing first-party S1 units.
- Disturbance / variety regulated: Concurrent developers/agents in parallel Git worktrees, conflicting edits and integration ordering.
- Decisive decision or feedback right: Detect real interference between viable S1 units, choose balancing action and feed corrections back into both continuing units' behaviour.
- Decision owner: The external agents or human Leader/Guide decide how to handle conflicting work; scripts create isolated worktrees and gate merges with deterministic status checks.
- Supporting / enforcement mechanisms: Worktree isolation by branch, stream briefing, merge gates, checkpoint status, branch discipline, tests and phase kits.
- Closure path: dispatch-worktrees.sh creates per-stream Git worktree + fixed prompt briefing → external agent works there → merge-worktrees.sh checks changed files/tests and merges or refuses. This is configuration/transport and gating. No continuing autonomous S1-to-S1 disturbance measurement and returned adaptive coordination owner is in this repository.
- Why this is / is not agent-owned: Git worktree isolation is valuable preventive structure, not an agent-owned S2 decision. A multi-agent diagram and named Leader role are instructions addressed to external assistants, not first-party S1-to-S1 anti-oscillation.
- Evidence: [docs/03-ORCA-WORKTREES-AND-PARALLEL-AGENTS.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/docs/03-ORCA-WORKTREES-AND-PARALLEL-AGENTS.md); [scripts/dispatch-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/dispatch-worktrees.sh); [scripts/merge-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/merge-worktrees.sh); [AGENTS.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/AGENTS.md); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md); [scripts/orchestrate-stage.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/orchestrate-stage.sh)
- Basis: bounded negative; source wires deterministic isolation only
- Confidence: High.
- Caveats: The installed upstream agents may negotiate conflicts when externally composed, but their coordination intelligence is not contained here.

### Absence scope

- Surfaces inspected: Dispatch and merge shell scripts, worktree status files/branch and checkpoint gates, role manual, stage context provisioner, launcher.
- Plausible first-party paths checked: Checked actual multi-worktree isolation, supposed Leader routing, merge conflict and failed regression escalation as S2 candidates with independent continuing actor return.
- Why no material first-party path remains: There are no first-party autonomous operating S1 units to regulate, nor a first-party conflict-balancing decision owner that changes their future actions; static Git gates and instructions do not suffice.

## S3 — Inside-and-now management

- State: —
- Function: No self-owned or parent-closed inside-and-now whole-system management of distinct, continuing viable operating units.
- Disturbance / variety regulated: Implementation backlogs, in-flight workstreams, failed tests, deployment risk, release priority and resource contention.
- Decisive decision or feedback right: Decide binding resource/priority/control changes across the entire present organization and return them to its S1 units.
- Decision owner: Human/externally implemented Leader and Guide roles defined in policy documents; scripts read checkpoint values, print plan, control dispatch/merge and enforce quality gates deterministically.
- Supporting / enforcement mechanisms: uos plan/status/doctor/ship, docs/10-CHECKPOINT.md, dispatch/merge and phase transitions, human-defined role rights, circuit breaker status.
- Closure path: External Leader/Guide or operator updates checkpoint/plans → uos derives milestone list/commands → dispatch runs Git worktree operations → test gates block or permit merge. There is no internally instantiated management actor deciding cross-business needs; no first-party authoritative parent feedback contract for continuing autonomous S1 operations.
- Why this is / is not agent-owned: The words Leader and Guide assign rights in documentation, not code implementing first-party reasoning. Parent involvement in README does not establish a separately closed parent-governed S3 mode: human actions occur outside a first-party management report/decision/return loop.
- Evidence: [scripts/uos.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/uos.sh); [docs/10-CHECKPOINT.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/docs/10-CHECKPOINT.md); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md); [docs/00-ARCHITECTURE-GUIDE.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/docs/00-ARCHITECTURE-GUIDE.md); [scripts/dispatch-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/dispatch-worktrees.sh); [scripts/merge-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/merge-worktrees.sh); [CLAUDE.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/CLAUDE.md)
- Basis: bounded negative after parent-mode and runtime investigation
- Confidence: High.
- Caveats: This workflow is designed to help external organizations exercise management; the absence concerns only first-party agent-owned VSM classification.

### Absence scope

- Surfaces inspected: uos plan/status/doctor and release paths, checkpoint schema, Guide approval documents, native hook policy, worktree/merge logic.
- Plausible first-party paths checked: Checked whether the human Guide/Leader parent route constitutes an operationally closed S3 manager, whether uos owns resource/priority discretion, and whether scripts return binding cross-unit management interventions.
- Why no material first-party path remains: The first-party scripts read and enforce external decisions, but are not decision owners; continuing own S1 businesses and closed S3 management/parent returns are absent.

## S3* — Complementary audit

- State: —
- Function: No independent first-party organizational audit that tests an S3 manager's picture against actual operating-unit evidence and returns corrective management intervention.
- Disturbance / variety regulated: Quality regressions, failed tests, misleading claims of task completion, insecure changes and inaccurate release readiness.
- Decisive decision or feedback right: Independently inspect real S1 activity outside management reports, challenge the S3 view and return correction to a legitimate S3 decision owner.
- Decision owner: Deterministic bash -n, shellcheck/markdownlint, change-scope and release guards; semantic reviews/sign-offs expected from external Guide, installed agents or human.
- Supporting / enforcement mechanisms: merge-worktrees.sh diff-scoped guards, scripts/release.sh checks, Git hooks, circuit-breaker three-strike, preflight/quality skills and repo tests.
- Closure path: Changed code → shellcheck/bash -n or configured test commands → gate permits/refuses integration and external Guide reviews it; no separate S3 organization account is audited or corrected by a first-party independent auditor.
- Why this is / is not agent-owned: Code test/quality verification is task/product QA; it does not automatically become S3* management audit. External semantic Guide independence is a document contract rather than a first-party executable organizational audit owner.
- Evidence: [scripts/merge-worktrees.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/merge-worktrees.sh); [scripts/release.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/release.sh); [docs/04-QUALITY-GATES-AND-SAFETY.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/docs/04-QUALITY-GATES-AND-SAFETY.md); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md); [tests/workflow-tests.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/tests/workflow-tests.sh); [.claude/settings.json](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/.claude/settings.json)
- Basis: bounded negative; direct inspection of strongest QA witnesses
- Confidence: High.
- Caveats: Human reviews and external multi-agent critique can form broader composite oversight but are not credited here.

### Absence scope

- Surfaces inspected: Native hooks, quality/test/docs guard skills, merge/release scripts, circuit-breaker/checkpoint, Guide review documents and test harness.
- Plausible first-party paths checked: Checked independent Guide second-pass and three code-quality guards as potential direct-evidence S3* audit of management reports, including error feedback channels.
- Why no material first-party path remains: The gates operate on code/test files and return task-level pass/fail; no first-party S3 managerial view, independent S3* organizational fact audit, or returned manager correction exists.

## S4 — Outside-and-then intelligence

- State: —
- Function: No owned prospective system/environment intelligence and adopted strategic capability-change loop.
- Disturbance / variety regulated: New external coding models/toolkits, future library changes, user domain shifts and security trends.
- Decisive decision or feedback right: Compare environmental futures and adopt strategy or capability changes to preserve the continuing organization's viability.
- Decision owner: Human/third-party agents choose new model/skills and run setup-toolkit.sh or sync-toolkit.sh; deterministic utilities copy/refresh context sources for the next phase.
- Supporting / enforcement mechanisms: Centralized toolkit installation/synchronization, language/domain model archetypes, dynamic stage kit injection, model provider selection at launch, docs on multi-domain strategy.
- Closure path: Operator or agent selects toolkit/provider/phase → first-party setup/sync/orchestrate-stage scripts download/copy predefined third-party skills and prompts → external agent uses updated context. Missing independently owned future-environment judgement, adopted whole-system strategic decision and return to ongoing first-party operation.
- Why this is / is not agent-owned: Dynamic context injection and periodic manual toolkit synchronization can improve future assistance, but the sources are externally chosen and no first-party prospective reasoning/adoption actor is supplied. Model selection in launcher is per-session configuration rather than VSM S4.
- Evidence: [scripts/setup-toolkit.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/setup-toolkit.sh); [scripts/orchestrate-stage.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/orchestrate-stage.sh); [scripts/teardown-stage.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/teardown-stage.sh); [vantrilex.ps1](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/vantrilex.ps1); [README.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/README.md); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md)
- Basis: bounded negative after checking adaptation candidate
- Confidence: High.
- Caveats: A living human-led product may innovate through this tool, but that is not a first-party supported S4 parent mode.

### Absence scope

- Surfaces inspected: Toolkit setup/sync scripts, stage injection policy, package launcher model/endpoint selection, checkpoint and project-phase documents.
- Plausible first-party paths checked: Checked whether dynamic toolkit rotation and future environment/resource management form an autonomous or legitimate parent-governed accepted strategic adaptation loop rather than configured one-time updates.
- Why no material first-party path remains: The scripts fetch/copy predetermined toolkits for externally chosen phases; no internal foresight or authorized strategy decision actor and feedback to a continuing owned S1 system is closed.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate purpose/identity policy arbitration, nor an operational constitutional parent decision-return path.
- Disturbance / variety regulated: Security constraints, contradictory requirements, forbidden secrets, architecture vs performance tradeoffs and role/approval disputes.
- Decisive decision or feedback right: Determine governing purpose and constitutional priorities when current execution and future adaptation requirements conflict and return an authoritative policy update.
- Decision owner: The human organization or external coding agent acts under CLAUDE.md/AGENTS.md, policy documents and prewritten shell guards; the repository itself statically encodes constraints.
- Supporting / enforcement mechanisms: Nine engineering invariants, rule files, three-strike breaker, no-secret hooks, Guide signoff text, Git safety and release gates.
- Closure path: External operator/Guide sets task policy → code hook checks pattern/checkpoint and refuses unsafe command/merge → user or external agent changes plan. No internal S5 forum considers policy identity conflicts and returns accepted revised constitutional instructions governing the organization.
- Why this is / is not agent-owned: Documents called constitution and the ability to edit config do not establish a first-party S5 decisive authority. Static rules and human instructions enforce constraints, not autonomous or parent-mode organization-level policy adjudication.
- Evidence: [CLAUDE.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/CLAUDE.md); [AGENTS.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/AGENTS.md); [docs/04-QUALITY-GATES-AND-SAFETY.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/docs/04-QUALITY-GATES-AND-SAFETY.md); [scripts/uos.sh](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/scripts/uos.sh); [.claude/settings.json](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/.claude/settings.json); [docs/05-INITIAL-PROMPT.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/docs/05-INITIAL-PROMPT.md); [skills/universal-agentic-workflow.md](https://github.com/3mar-baha/universal-agentic-os/blob/04ee2b7cea82c87679b404771961f3cddafb4ef0/skills/universal-agentic-workflow.md)
- Basis: bounded negative with parent-ownership counterfactual
- Confidence: High.
- Caveats: This repository intentionally functions as reusable policy for external coding organizations, outside the assessed first-party actor boundary.

### Absence scope

- Surfaces inspected: CLAUDE.md, AGENTS.md, lifecycle skills, role-rights guide, quality/circuit-breaker hooks, provider launch settings and uos control surface.
- Plausible first-party paths checked: Checked constitutional text and externally owned Guide/Leader authority, counterfactual no-agent operation, and whether violations escalate to a legitimate parent S5 judgement with returned amended policy.
- Why no material first-party path remains: All governing statements are static contracts for external people/agents, enforced by deterministic code; no first-party identity-level decision and accepted parent constitutional return is shipped.

## Distributed OSS parent arrangement

The README's Leader/Guide/Implementer tripartite model, external tools and human approval represent a parent/user governance arrangement in a composed organization, not an internally implemented parent-mode VSM manager for this repository. `uos` handles concrete plan/checkpoint/test/merge transitions. While this is genuine enforcement and may be valuable to an organization, no shipped autonomous/constructor S3, S4 or S5 path combines a legitimate parent deliberation with returned policy that materially affects *continuing first-party autonomous S1 operations*. Repo maintainer releases and updates to externally installed Claude agent prompts are outside the bounded assessed runtime.

## Self-hosted, operator and non-human modes

Windows launcher can map several external hosted inference endpoints to Claude/OpenCode/Codex; Bash utilities run on the host with Git, shell, optional shellcheck/Node lint and previously installed toolkits. Users of Cursor/Windsurf/other agents can read AGENTS.md manually. A human may use only the first-party Bash setup/guard features, but then all open-ended decisions are human-owned. In an externally installed coding-agent session, those cognitive decisions remain in the external agent process. None of these standard modes implements a self-contained first-party agent loop.

## Recursion

Each stream is a Git worktree for a user-selected concern, and Leader/Guide/Implementer are documented role partitions. Streams are not proven continuing viable S1 business units; their code-writing agents are independently owned external systems. Worktree scheduling, role prompts and test gates are important preconditions for a **wider composed** organization but cannot by themselves prove higher autonomous recursion within the evaluated repository.

## Variety and escalation

The native tools can detect a BLOCKED checkpoint and refuse dispatch/merge, run syntax/lint checks, refuse unsafe branch merges, and store strike/decision report information that alerts a user/external Guide. These outputs are deterministic guardrails, not independent agent insight or a standalone VSM algedonic loop. External humans/agents can respond and update checkpoints, but the corresponding higher-recursion authority and accepted decision loop are not implemented in first-party runtime.

## Evidence gaps

Source was inspected at fixed exact revision. An independent checkout successfully passed dependency-free Bash syntax checking (`bash -n`) of shipped scripts/hooks/tests without executing destructive scaffolding, toolchain installation, external model CLI or full workflow end-to-end operations. Neither actual external Claude Code/OpenCode/Codex model calls nor PowerShell launched sessions were run; their explicit `npx` invocation source is enough to ground ownership. The repository's own full end-to-end test script creates/restructures throwaway projects and depends on optional external tooling; it was not run for this semantic assessment. Future addition of a native model/tool actor or a first-party governance return loop would require an independent pinned reassessment. The exclusion is not a security rating or engineering-quality score.
