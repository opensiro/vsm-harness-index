---
harness_id: sandcastle
project_name: Sandcastle
repository: https://github.com/mattpocock/sandcastle
review_ref: e99f832f26dc9d245c019a9ddd19fa5dee792427
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Sandcastle

## Review boundary

- System in focus: the first-party Sandcastle TypeScript library/CLI at frozen revision `e99f832f26dc9d245c019a9ddd19fa5dee792427`, including sandbox/worktree lifecycle, `run()`/`createSandbox()`/`interactive()`, `Orchestrator`, agent-provider adapters, session transfer, completion/timeout logic, commit collection/merge, direct sandbox execution and bundled workflow templates.
- Purpose and identity: orchestrate externally implemented AI coding-agent CLIs inside isolated sandboxes/worktrees, capture their sessions/output/commits and provide reusable first-party templates for parallel planning, implementation, review and merge workflows.
- Relevant environment: workflow author/operator, target git repository, Docker/Podman/Vercel/custom sandbox providers, externally installed Claude Code/Codex/Pi/Cursor/OpenCode/Copilot agent CLIs, their model/provider services, filesystem/session stores and issue trackers used by templates.
- Standard-distribution boundary: first-party Sandcastle process, sandbox/worktree factories, lifecycle/merge/commit logic, provider command/parsing adapters, session transport, prompt/output plumbing and shipped templates. The autonomous decision/action/tool loops inside Claude Code, Codex, Pi, Cursor, OpenCode, Copilot and other supported agent CLIs remain adjacent systems and do not donate first-party VSM ownership merely because Sandcastle launches or resumes them.
- Credited operating / distribution surfaces: `src/Orchestrator.ts`; `src/run.ts`; `src/createSandbox.ts`; `src/AgentProvider.ts`; sandbox/worktree lifecycle and providers; session capture/resume; direct `sandbox.exec()`; output/completion/timeout handling; shipped `blank`, `simple-loop`, `sequential-reviewer`, `parallel-planner` and `parallel-planner-with-review` templates.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests/release infrastructure, contributor docs and research notes not wired into the shipped runtime. External agent CLI internals, their subagents/reviewers/approval logic, model reasoning/tool policies and provider-side services are not credited as Sandcastle-owned autonomy.
- First-party operating / deployment modes considered: one-shot `run`; multi-iteration run; reusable `createSandbox`; worktree runs; interactive external-agent launch; host/no-sandbox mode; session capture/resume/fork; parallel planner template; sequential/parallel review templates; direct deterministic `sandbox.exec` verification.
- Recursion level: one first-party Sandcastle harness/workflow execution. Externally launched coding-agent processes may be autonomous systems at a lower recursion, but their task-level cognition is not inherited by the repository-relative Sandcastle boundary.
- Reviewed revision: `e99f832f26dc9d245c019a9ddd19fa5dee792427`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Sandcastle supplies substantial first-party execution and isolation infrastructure but delegates autonomous agent cognition to separately implemented CLIs. Its `AgentProvider` interface requires providers to build a non-interactive CLI command, parse the CLI's structured stream, expose session identifiers and optionally transfer provider-owned session files. Built-in factories construct commands such as `claude --print ...`, `codex exec ...`, `pi -p ...`, Cursor/OpenCode/Copilot equivalents. `Orchestrator.invokeAgent()` asks the provider for that command, executes it inside the sandbox and parses emitted text, tool-call, result, usage and session events. Sandcastle does not implement the external agent's model/tool decision loop.

The repository's own provider-extension guide makes this mechanism/intelligence boundary explicit: a new “agent provider” is support for an agent CLI that already has unattended run mode, auto-approval, model selection, structured streaming, session IDs and resume semantics. Sandcastle consumes those capabilities; it does not supply them.

First-party workflow templates are materially richer than the base runner. `parallel-planner` launches a planner CLI agent, validates its structured plan, fans out implementer CLI agents on separate branches, then launches a merger CLI agent. `parallel-planner-with-review` and `sequential-reviewer` additionally launch a separate reviewer CLI agent after implementation. Those templates establish real first-party topology, sandbox/worktree isolation and lifecycle composition, but their substantive planning, implementation, review and merge judgments are made by external `claudeCode(...)` processes. The TypeScript template decides when to invoke them and how to route their outputs; it does not become the owner of those agents' task-level decision loops.

The counterfactual owner test therefore fails S1. Remove Claude Code/Codex/Pi/etc. while preserving Sandcastle's sandbox lifecycle, prompt preprocessing, iteration counter, branch strategy, worktrees, commit collection, completion signals, direct shell execution, templates and stream/session plumbing: Sandcastle can still create/merge branches, run deterministic hooks/commands and manage processes, but no first-party actor remains that interprets an arbitrary coding objective and repeatedly chooses substantive actions from environment observations. Remove Sandcastle while preserving one of those external CLIs: that CLI retains its own autonomous coding-agent loop. Sandcastle is an orchestration/isolation harness around external agents rather than a first-party agentic organization under the repository-relative Index boundary.

Primary evidence:

- [`README.md`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/README.md) — product boundary as a library for orchestrating AI coding agents in isolated sandboxes and examples using `claudeCode(...)`.
- [`src/AgentProvider.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/AgentProvider.ts) — provider interface plus built-in factories that build external agent CLI commands and parse their stream/session formats.
- [`src/Orchestrator.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/Orchestrator.ts) — invokes provider-built external commands inside first-party sandboxes, handles output/completion/timeouts and records commits/sessions.
- [`docs/agents/adding-an-agent-provider.md`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/docs/agents/adding-an-agent-provider.md) — supported agent is explicitly an external CLI expected to own unattended execution, structured tool/result streaming and session/resume behavior.
- [`src/templates/parallel-planner/main.mts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/templates/parallel-planner/main.mts) — first-party planner/fan-out/merge topology whose substantive actors are external Claude Code agents.
- [`src/templates/parallel-planner-with-review/main.mts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/templates/parallel-planner-with-review/main.mts) and [`src/templates/sequential-reviewer/main.mts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/templates/sequential-reviewer/main.mts) — shipped review compositions using separate external implementer/reviewer CLI processes.
- [`package.json`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/package.json) — runtime distribution has orchestration/sandbox dependencies rather than an embedded model/agent SDK implementing task cognition.

## Operational model

A caller supplies an `AgentProvider`, prompt and sandbox provider. Sandcastle prepares a git worktree/sandbox, asks the `AgentProvider` to construct the external agent command, runs that process, parses its emitted stream and collects resulting commits/session state. Optional outer iterations rerun the external agent; completion signals/timeouts decide when the process loop stops. Shipped templates compose multiple such external agent invocations into planner/implementer/reviewer/merger pipelines and use first-party branch/sandbox isolation and deterministic TypeScript control flow around them.

The autonomous action recurrence nevertheless remains inside each external CLI. Streamed tool calls are observations of what that CLI decided, not first-party Sandcastle tool decisions. Session capture/resume transports the CLI's own conversation state; it does not relocate ownership of the session's policy into Sandcastle.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit owns the arbitrary coding-task decision/action/feedback loop inside the frozen Sandcastle repository boundary.
- Disturbance / variety regulated: Sandcastle handles sandbox/process/git lifecycle variety, while coding objectives, repository observations, tool results and substantive next-action choices are interpreted by external agent CLIs.
- Decisive decision or feedback right: interpret the current task/environment evidence, choose a substantive tool/code action, observe its result and choose the next action.
- Decision owner: external Claude Code/Codex/Pi/Cursor/OpenCode/Copilot or another supplied agent provider runtime, not the first-party Sandcastle orchestrator.
- Supporting / enforcement mechanisms: sandbox/worktree lifecycle, `AgentProvider` command/parsing adapters, prompt preprocessing, completion signals, iteration limits, timeouts, session capture/resume, commit collection/merge and direct sandbox execution.
- Closure path: caller/template selects provider → Sandcastle builds sandbox and launches provider CLI → external CLI performs its autonomous model/tool loop → Sandcastle parses output/tool events and collects commits → authored Sandcastle logic may launch another external CLI. The substantive decision/action/observation recurrence closes in the adjacent agent runtime.
- Why this is / is not agent-owned: provider factories literally construct external CLI commands; provider documentation requires the external CLI itself to support autonomous unattended run and structured tool/result streaming. Sandcastle observes and contains that autonomy rather than implementing it.
- Evidence: [`src/AgentProvider.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/AgentProvider.ts); [`src/Orchestrator.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/Orchestrator.ts); [`docs/agents/adding-an-agent-provider.md`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/docs/agents/adding-an-agent-provider.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary Sandcastle deployments clearly run autonomous coding agents. This finding concerns repository-relative first-party ownership, not whether the assembled external-agent system behaves agentically.

### Absence scope

- Surfaces inspected: `AgentProvider`, all built-in CLI factories, `Orchestrator`, run/createSandbox/interactive paths, session capture/resume, sandbox/worktree lifecycle, direct sandbox execution, shipped templates and package runtime dependencies.
- Plausible first-party paths checked: Orchestrator as S1; completion iteration as an agent loop; external tool-call stream as first-party tools; captured/resumed sessions as transferred cognition; planner/reviewer templates as first-party autonomous actors.
- Why no material first-party path remains: every general task-level autonomous choice is made by a separately implemented external agent CLI. First-party Sandcastle supplies isolation, invocation, deterministic lifecycle and transport but no surviving autonomous task actor when those external runtimes are removed.

## S2 — Coordination

- State: —
- Function: Sandcastle contains strong isolation/coordination mechanisms, but the coordinated autonomous units in standard workflows are external agent runtimes rather than first-party Sandcastle S1s.
- Disturbance / variety regulated: parallel coding agents can interfere through shared repository/filesystem state and branches; worktree/sandbox isolation and separate branches attenuate that disturbance in assembled deployments.
- Decisive decision or feedback right: workflow/template/caller selects branch and sandbox topology; first-party lifecycle enforces the isolation. No qualifying first-party S1 plurality exists at the declared recursion.
- Decision owner: TypeScript template/caller configuration for topology; external planner agent may choose branch/task assignments in some bundled templates, but that planner is an adjacent Claude Code runtime.
- Supporting / enforcement mechanisms: per-run worktrees, branch strategies, per-issue sandboxes, independent provider processes, `Promise.allSettled`, worktree locking, lifecycle cleanup and later merge phase.
- Closure path: bundled template/caller creates separate branches/sandboxes → external agents operate independently → first-party code gathers branches/results → external merger or deterministic git lifecycle reconciles later. The attenuation mechanism is real, but the S1 units are external under this boundary.
- Why this is / is not agent-owned: the Profile requires distinct S1 units at the assessed recursion before publishing S2. Sandcastle's worktree/sandbox isolation would be material S2 evidence for a wider composed system, but it cannot bootstrap missing first-party S1 ownership.
- Evidence: [`README.md`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/README.md); [`src/templates/parallel-planner/main.mts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/templates/parallel-planner/main.mts); [`src/WorktreeManager.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/WorktreeManager.ts).
- Basis: explicit + structural absence at declared ownership boundary
- Confidence: high
- Caveats: this `—` does not mean Sandcastle lacks coordination engineering; it means the repository-relative Index does not inherit the external agents as first-party S1s.

### Absence scope

- Surfaces inspected: branch strategies, worktrees/locking, sandbox providers, parallel planner templates, per-issue sandboxes, Promise concurrency, merge lifecycle and completion/error handling.
- Plausible first-party paths checked: worktree isolation as S2; sandbox isolation as S2; planner-assigned branches as agent-owned S2; parallel templates as S1 plurality.
- Why no material first-party path remains: the concrete interference attenuation operates around adjacent autonomous CLIs, while first-party Sandcastle itself contains no autonomous operational S1 units to coordinate.

## S3 — Inside-and-now control

- State: —
- Function: no first-party discretionary whole-system current-control owner over autonomous S1 commitments/resources/priorities is established.
- Disturbance / variety regulated: process hangs, idle timeouts, completion signals, aborts, iteration caps, commit/no-commit outcomes and merge lifecycle are regulated mechanically; bundled planner/merger judgments are delegated to external agents.
- Decisive decision or feedback right: no first-party actor inspects a whole autonomous operation and chooses current commitments/priorities/interventions from organizational evidence.
- Decision owner: caller/template code for fixed lifecycle policy; external planner/merger agents for substantive plan/merge judgments.
- Supporting / enforcement mechanisms: iteration loop, completion/idle timeouts, AbortSignal, lifecycle hooks, commit collection, merge strategies, structured-output parsing, direct sandbox exec and failure handling.
- Closure path: authored policy or external agent determines current action → Sandcastle enforces process/sandbox/git lifecycle. No first-party whole-system discretionary decision → changed autonomous S1 commitments loop is established.
- Why this is / is not agent-owned: `Orchestrator` is a process/lifecycle orchestrator, not evidence of VSM S3 decision ownership. It does not interpret current mission-wide evidence to revise priorities; external planner agents in shipped templates remain adjacent CLI runtimes.
- Evidence: [`src/Orchestrator.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/Orchestrator.ts); [`src/templates/parallel-planner/main.mts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/templates/parallel-planner/main.mts); [`src/run.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/run.ts).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a parent application may implement current-control policy using Sandcastle APIs, but generic programmability is not a shipped first-party S3 owner.

### Absence scope

- Surfaces inspected: orchestrator loop, timeouts/completion/abort, lifecycle hooks, structured output retries, branch/merge logic and planner/merger templates.
- Plausible first-party paths checked: `Orchestrator` naming; completion-signal decisions; structured-output retry; planner template; merger agent; caller AbortSignal/current intervention.
- Why no material first-party path remains: first-party logic enforces fixed lifecycle conditions, while substantive whole-run planning/control decisions are either authored externally or made by external agent CLIs.

## S3* — Complementary audit

- State: —
- Function: shipped templates can launch a separate reviewer agent and deterministic shell verification, but no first-party complementary-audit organization is established over a first-party S1 reporting path.
- Disturbance / variety regulated: reviewer templates can challenge implementation branches and `sandbox.exec()` can run tests/lints, but the audited implementer and substantive reviewer are external autonomous CLIs.
- Decisive decision or feedback right: external reviewer agent decides review findings/corrections; deterministic verification commands return process results to caller/template code.
- Decision owner: external reviewer CLI or caller-authored TypeScript logic, not a first-party Sandcastle audit actor.
- Supporting / enforcement mechanisms: `sequential-reviewer`, `parallel-planner-with-review`, shared branch/sandbox handoff, `sandbox.exec()`, structured output extraction and commit collection.
- Closure path: external implementer creates branch → first-party template invokes external reviewer on same branch → reviewer may correct it → first-party runtime gathers commits. This is a useful assembled review loop, but both claim and review cognition are outside first-party Sandcastle S1 ownership.
- Why this is / is not agent-owned: bundled review topology does not transfer the external reviewer agent's judgment into repository ownership. With no first-party S1 reporting path, S3* cannot be published at this recursion.
- Evidence: [`src/templates/sequential-reviewer/main.mts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/templates/sequential-reviewer/main.mts); [`src/templates/parallel-planner-with-review/main.mts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/templates/parallel-planner-with-review/main.mts); [`README.md`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/README.md).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: at a wider application boundary that treats the external implementer/reviewer CLIs as constituent S1/audit units, these shipped templates become material S3* evidence; that is a different system-in-focus.

### Absence scope

- Surfaces inspected: reviewer templates/prompts, implementer→reviewer same-branch handoff, direct `sandbox.exec`, structured-output checks, commit/no-commit gates and provider approval-reviewer options.
- Plausible first-party paths checked: separate reviewer template as S3*; direct tests as complementary audit; Codex `auto_review` as Sandcastle audit; structured output parser/retry as S3*.
- Why no material first-party path remains: substantive review/approval cognition belongs to adjacent provider CLIs, deterministic checks lack a first-party S1 claim/audit organization at this boundary, and provider-native auto-review remains internal to Codex rather than Sandcastle.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party environment-facing prospective adaptation loop changes Sandcastle's later organizational capability/strategy from observed external/future variety.
- Disturbance / variety regulated: sessions can be captured/resumed and templates can repeat over a changing issue backlog, but this preserves external-agent state or reruns authored topology rather than adopting first-party future-facing capability changes.
- Decisive decision or feedback right: no first-party actor selects and persists an adaptation to future operating capability.
- Decision owner: not established.
- Supporting / enforcement mechanisms: session capture/resume/fork, outer template loops, issue replanning by external planner agents, reusable sandboxes, hooks and configuration.
- Closure path: no first-party external/future sensing → generated adaptation option → adoption decision → persistent capability change → later operation loop is established.
- Why this is / is not agent-owned: a planner can replan from new issues, but that planner is an external CLI performing current task operation. Session persistence and iterative templates do not by themselves constitute S4.
- Evidence: [`src/SessionStore.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/SessionStore.ts); [`src/templates/parallel-planner/main.mts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/templates/parallel-planner/main.mts); [`src/Orchestrator.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/Orchestrator.ts).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: downstream applications can use Sandcastle to build evolutionary/self-modifying loops; generic composition capability is not a dedicated first-party S4 constructor.

### Absence scope

- Surfaces inspected: session capture/resume/fork, outer iteration loops, planner templates, hooks, prompts, configuration and sandbox reuse.
- Plausible first-party paths checked: persistent sessions as learning; planner replanning as S4; repeated backlog passes; forked sessions; external agents modifying prompts/templates.
- Why no material first-party path remains: these mechanisms preserve/reinvoke external agent state or execute current authored workflows; they do not autonomously produce and adopt a persistent first-party capability/strategy change for future conditions.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy governance function is established.
- Disturbance / variety regulated: model/provider selection, permission flags, sandbox policy, prompts and hooks constrain execution but are ordinary construction/enforcement rather than governance of an autonomous Sandcastle organization's identity or ultimate policy.
- Decisive decision or feedback right: no first-party ultimate authority is established that resolves an identity/purpose/policy issue and returns that decision into first-party autonomous operation.
- Decision owner: caller/developer configures the harness; external agent CLIs own any provider-native identity/approval policy.
- Supporting / enforcement mechanisms: agent-provider options, Codex approvals flags, Claude permission modes, sandbox/network/mount policy, prompts, branch strategy and hooks.
- Closure path: no identity/ultimate-policy issue → legitimate authority → authoritative decision → return into qualifying first-party autonomous operation loop is established.
- Why this is / is not agent-owned: sandbox/permission/provider configuration can be strong policy enforcement, but Profile 0.2.4 does not equate configuration with S5, and the reviewed first-party boundary lacks autonomous S1 identity to govern.
- Evidence: [`src/AgentProvider.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/AgentProvider.ts); [`README.md`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/README.md); [`src/SandboxProvider.ts`](https://github.com/mattpocock/sandcastle/blob/e99f832f26dc9d245c019a9ddd19fa5dee792427/src/SandboxProvider.ts).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a parent organization can impose meaningful governance through Sandcastle's configuration boundary; that policy belongs to the parent/composed system unless a dedicated S5 closure is implemented inside Sandcastle.

### Absence scope

- Surfaces inspected: provider/model/permission options, sandbox/network/mount configuration, prompts/templates, hooks, branch strategies, session controls and provider-native review flags.
- Plausible first-party paths checked: sandbox policy as S5; Claude permission mode; Codex auto-review approval policy; prompt files as identity; developer configuration as ultimate authority.
- Why no material first-party path remains: inspected surfaces configure or enforce external-agent execution but do not implement a live first-party identity/ultimate-policy decision and return path.

## Recursion

The assessment fixes recursion at the first-party Sandcastle harness/runtime. External coding-agent CLIs can be autonomous S1 systems at their own recursion, and shipped templates deliberately compose several of them. That wider assembled topology can exhibit coordination, current control and complementary review; repository-relative Index ownership does not silently absorb those separately implemented agent runtimes.

## Variety and escalation

Sandcastle strongly attenuates infrastructure variety through isolated sandboxes/worktrees, lifecycle hooks, branch strategies, session portability, completion/timeout controls and provider adapters. Shipped templates add repeatable planner/parallel/review/merge compositions. These are substantive harness mechanisms, but the autonomous judgments remain external. Under the first-party counterfactual, removing adjacent agent CLIs removes the autonomous operating actors while leaving the Sandcastle mechanism intact.

## Evidence gaps

- Sandcastle can support custom `AgentProvider`s; arbitrary downstream implementations are not imported into the standard-distribution boundary.
- The shipped templates are first-party and operationally meaningful, but every planner/implementer/reviewer/merger in the frozen templates is instantiated via an external agent provider.
- Provider-native subagents, approval reviewers and tool loops remain properties of the external CLI runtime even when their events/sessions are captured by Sandcastle.
- No first-party model SDK or task-level agent policy remains after removing the supported CLI/provider runtimes.

## Assessment summary

Sandcastle is a strong orchestration, sandboxing and multi-agent workflow substrate, but its frozen first-party distribution does not own the autonomous operational decision/action/observation loop required to establish S1. It launches external agent CLIs, isolates them, transports their sessions/events, and packages useful planner/reviewer/merge topologies around them. Under Profile 0.2.4 / Methodology 0.3.6, the proposed canonical outcome is `excluded-no-agentic-vsm` with `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.
