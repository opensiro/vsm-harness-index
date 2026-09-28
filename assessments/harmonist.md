---
harness_id: harmonist
project_name: Harmonist
repository: https://github.com/GammaLabTechnologies/harmonist
review_ref: 6fd5941cce8c3f6f411fd14cde0daa663ccffa8f
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Harmonist

## Review boundary

- System in focus: the first-party Harmonist portable agent pack at frozen revision `6fd5941cce8c3f6f411fd14cde0daa663ccffa8f`, including its markdown agent catalogue, generated index, `AGENTS.template.md`, integration/upgrade tooling, Cursor hook enforcement runtime, structured memory tooling, repo-map helpers, protocol rules, reviewer definitions, playbooks and supply-chain verification surfaces.
- Purpose and identity: provide a portable organizational/protocol layer for existing AI coding assistants, supplying specialist personas, routing instructions, durable project rules/memory and mechanical process gates around subagent dispatch, review, destructive commands and task completion.
- Relevant environment: Cursor Agent mode and other supported AI coding assistants; the host assistant's model/tool/subagent runtime; user project repositories; external specialist/reviewer model executions; shell/test commands; human confirmation for destructive commands; local `.cursor/` state and memory.
- Standard-distribution boundary: files and executable stdlib Python/bash shipped by Harmonist at the frozen revision. Cursor, Claude Code, Copilot, Windsurf, Aider, Gemini CLI, OpenCode and other host/model runtimes remain adjacent systems. Their model reasoning, Task/subagent execution and tool loops do not become first-party Harmonist ownership merely because Harmonist supplies prompts, personas, markers, hooks or protocol instructions consumed by those hosts.
- Credited operating / distribution surfaces: `AGENTS.template.md`; `agents/index.json`; `agents/orchestration/**`; `agents/review/**`; `hooks/**`; `memory/**`; `agents/scripts/integrate.py`, `upgrade.py`, `project_context.py`, `repomap.py` and validation/telemetry utilities; `integration-prompt.md`; installed `.cursor/rules`/hook configuration produced by the first-party integration flow.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor workflows, pack-development tests and documentation-only scenario examples. The autonomous reasoning/tool loops of the external host assistant and its spawned subagents/reviewers are environment, even when their prompts are copied from first-party Harmonist markdown definitions.
- First-party operating / deployment modes considered: Cursor integration through the documented one-shot integration prompt; CLI integration via `integrate.py`; installed hook runtime with session/subagent/edit/shell/stop phases; orchestrator/specialist/reviewer markdown definitions consumed by supported host assistants; persistent memory and telemetry; upgrades and supply-chain verification.
- Recursion level: one installed Harmonist protocol/control layer around one host coding-assistant session and its host-spawned subagents. The host assistant and its subagents can be autonomous systems at a wider composed boundary, but their internal cognition is not inherited by this repository-relative system-in-focus.
- Reviewed revision: `6fd5941cce8c3f6f411fd14cde0daa663ccffa8f`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Harmonist deliberately positions itself as a portable protocol/enforcement pack rather than an agent runtime. The README says there is “No runtime” and requires an AI coding assistant with subagent dispatch. The recommended integration path is to paste `integration-prompt.md` into Cursor Agent mode; the CLI integration path installs deterministic files, hooks, memory and repo-map helpers, then explicitly tells the team/orchestrator to customize project identity/rules, choose specialists and start a new Cursor chat so the external orchestrator can act.

The first-party hook runtime is substantial but deterministic. It records edits and subagent starts/stops, enforces a concurrency cap, scopes readonly reviewers, asks/denies dangerous shell operations, requires selected reviewer markers and memory updates, optionally requires regression evidence, and returns a `followup_message` when the protocol is incomplete. Its subprocess calls run first-party local utilities such as repo-map and memory validators. It does not itself interpret an open-ended user goal, select a substantive implementation plan, invoke a model, choose domain tools, inspect model observations and decide the next task-level action.

The organizational intelligence described by Harmonist lives in markdown consumed by the host assistant. `agents-orchestrator.md` instructs a model to decompose work, query the agent index, invoke specialists through the host Task/subagent facility, inspect gate results and retry/escalate. Likewise `qa-verifier.md` is a readonly model persona instructed to inspect a diff and return a verdict. These are meaningful first-party role definitions and protocol contracts, but the autonomous actors that execute them are supplied by Cursor/Claude/other adjacent runtimes.

This distinction controls the published VSM states. Removing the external host assistant and its model/subagent runtime while leaving the Harmonist installation intact leaves a deterministic enforcement, memory, routing-data and validation substrate. It can deny, ask, record and emit follow-up instructions in reaction to host events, but it cannot autonomously perform an operational task or instantiate the organizational actors described by its markdown catalogue. Therefore the frozen first-party boundary does not establish S1, and higher-function mechanisms are not promoted into S2-S5 ownership merely because they would be useful inside a wider composed agent organization.

Primary evidence:

- [`README.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/README.md) — explicit “No runtime” positioning, requirement for an AI coding assistant with subagent dispatch, Cursor Agent-mode integration, hook/memory architecture and supported host assistants.
- [`agents/orchestration/agents-orchestrator.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/orchestration/agents-orchestrator.md) — model persona instructing the host agent to plan, choose specialists, invoke Task/subagents, run reviewer gates, retry and escalate.
- [`agents/review/qa-verifier.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/review/qa-verifier.md) — independent-review persona implemented as markdown/model instructions rather than a first-party reviewer runtime.
- [`AGENTS.template.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/AGENTS.template.md) — post-install project precedence, routing/delegation protocol, memory contract and external Task/subagent instructions.
- [`hooks/scripts/hook_runner.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/scripts/hook_runner.py) — deterministic hook event state, subagent concurrency/readonly controls, destructive-command gate, reviewer-marker accounting, stop-gate requirements, bounded follow-up loop and local-helper invocation.
- [`hooks/README.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/README.md) — host-hook contract, marker-based reviewer identity and explicit limitations of the process gates.
- [`agents/scripts/integrate.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/scripts/integrate.py) — deterministic integration tooling and explicit manual/host-orchestrator follow-ups the script cannot perform.
- [`integration-prompt.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/integration-prompt.md) — one-shot instructions executed by the external Cursor Agent-mode host to analyze the project and complete integration.

## Operational model

After installation, Harmonist gives an external coding assistant project-level orchestration instructions, a catalogue of specialist/reviewer prompts and deterministic hook events. The host assistant reads project memory/rules, chooses a plan and invokes host subagents with `AGENT: <slug>` markers. Harmonist hooks observe those host events and enforce configured process invariants: a concurrency cap can deny another subagent launch; reviewer markers and memory updates are recorded; destructive shell commands can be sent to human confirmation; and task completion can be rejected with a follow-up message until required process evidence exists.

The actor/enforcer split is explicit. The host model decides what substantive work to do, which specialist to invoke, what tool action to take and how to respond to reviewer findings. Harmonist constrains and records that activity but does not contain the model/tool loop that makes those decisions. Its strongest runtime behavior is therefore first-party enforcement around adjacent autonomous agents, not a first-party autonomous organization at the declared recursion.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit closes an open-ended task decision/action/feedback loop inside the Harmonist repository boundary.
- Disturbance / variety regulated: user requests, repository state, coding/research uncertainty, tool outcomes and reviewer feedback are substantively interpreted by the external host assistant/subagents.
- Decisive decision or feedback right: interpret the goal and observations, choose the next implementation/research/tool action, evaluate returned evidence and revise the course of work.
- Decision owner: external Cursor/Claude/other host-agent runtime executing Harmonist's copied markdown instructions and personas.
- Supporting / enforcement mechanisms: agent catalogue, project `AGENTS.md`, routing metadata, project-context preamble, hook event recorder, stop/shell gates, memory/repo-map helpers and integration tooling.
- Closure path: user task → external host assistant reads Harmonist rules/personas → host chooses plan/subagent/tool actions → Harmonist hooks observe/constrain events → host assistant interprets the resulting allow/deny/follow-up/reviewer output and chooses the next substantive action. The autonomous task loop closes in the adjacent host runtime.
- Why this is / is not agent-owned: Harmonist explicitly ships no runtime and its executable Python/bash does not invoke a model or implement the host's model/tool loop. The first-party orchestrator and specialists are markdown definitions that require an external agent host to become actors.
- Evidence: [`README.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/README.md); [`agents/orchestration/agents-orchestrator.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/orchestration/agents-orchestrator.md); [`hooks/scripts/hook_runner.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/scripts/hook_runner.py); [`agents/scripts/integrate.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/scripts/integrate.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: an installed Harmonist deployment normally contains autonomous host agents in ordinary use. This assessment is repository-relative ownership, not a claim that the composed Cursor/Harmonist system is non-agentic.

### Absence scope

- Surfaces inspected: README/integration modes, orchestrator and specialist/reviewer definitions, project AGENTS protocol, hook runtime, integration/upgrade scripts, memory/repo-map helpers and model/runtime dependency/search surfaces.
- Plausible first-party paths checked: markdown orchestrator as S1; hook follow-up loop as S1; integration prompt as S1; deterministic helper subprocesses; reviewer/specialist catalogue as bundled actors.
- Why no material first-party path remains: all substantive open-ended decisions require a separately implemented host model/subagent runtime; first-party executables install, observe, constrain, validate or persist state but do not run an autonomous operational actor.

## S2 — Coordination

- State: —
- Function: Harmonist provides real anti-overload and delegation-enforcement mechanisms, but the distinct autonomous S1 units being coordinated are external host subagents rather than first-party Harmonist S1 units at this recursion.
- Disturbance / variety regulated: excessive concurrent host subagents, readonly-agent writes, missing handoff context and potentially conflicting work are constrained or surfaced.
- Decisive decision or feedback right: admit/deny another subagent launch under a fixed concurrency cap and reject selected protocol violations; substantive work partitioning/routing remains with the external orchestrator model.
- Decision owner: deterministic hook policy for caps/scoping; external host assistant for task decomposition and specialist assignment.
- Supporting / enforcement mechanisms: `max_concurrent_subagents`, subagent start/stop state, readonly capability flags, delegation-context gate, routing metadata and project-precedence preamble.
- Closure path: external host requests subagent launch → hook checks configured cap/context/identity → may deny or record launch → external host decides how/when to re-dispatch. This is useful enforcement around external actors, not an S2 function among first-party S1 units.
- Why this is / is not agent-owned: the Profile requires qualifying S1 plurality at the declared recursion. Harmonist's hook can attenuate host-level fan-out but does not supply the autonomous workers whose interaction it constrains, and the richer routing/partitioning judgment is executed by the adjacent host orchestrator.
- Evidence: [`hooks/scripts/hook_runner.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/scripts/hook_runner.py); [`AGENTS.template.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/AGENTS.template.md); [`agents/orchestration/agents-orchestrator.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/orchestration/agents-orchestrator.md).
- Basis: explicit + structural absence at declared ownership boundary
- Confidence: high
- Caveats: in a wider composed system that explicitly includes Cursor/other spawned agents as constituent S1 units, the concurrency/readonly/delegation mechanisms can be material coordination evidence; that is a different system-in-focus.

### Absence scope

- Surfaces inspected: subagent concurrency cap, start/stop bookkeeping, readonly enforcement, delegation-context checks, routing/index protocol and orchestration markdown.
- Plausible first-party paths checked: concurrency cap as S2; readonly scoping; index-driven routing; mandatory handoff context; reviewer ordering.
- Why no material first-party path remains: these mechanisms constrain external host-agent interactions and/or implement fixed process policy, while no first-party autonomous S1 plurality is established at the Harmonist repository boundary.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system autonomous current-control owner is established over first-party operations.
- Disturbance / variety regulated: incomplete protocol steps, missing review/memory evidence, excessive retries, destructive commands and current subagent count are monitored or constrained.
- Decisive decision or feedback right: Harmonist deterministically decides whether configured gate predicates are satisfied; the external orchestrator model decides the current plan, task assignments, retries, substitutions and escalation recommendation.
- Decision owner: deterministic hook state machine for enforcement; external host model/human for substantive current-control judgment.
- Supporting / enforcement mechanisms: session state, reviewer ledger, write/memory records, loop limit, stop follow-up, destructive-command human confirmation, incidents and telemetry.
- Closure path: host performs work → hooks observe current event state → fixed predicates allow/deny/follow up → host model interprets the finding and decides what organizational action to take next. Whole-system discretionary current control therefore closes outside Harmonist.
- Why this is / is not agent-owned: `AgentsOrchestrator` describes plan/retry/escalation judgment, but it is a prompt for an external model. The hook runner supplies enforcement, not an autonomous manager deciding current commitments/resources/priorities among first-party S1 units.
- Evidence: [`hooks/scripts/hook_runner.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/scripts/hook_runner.py); [`agents/orchestration/agents-orchestrator.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/orchestration/agents-orchestrator.md).
- Basis: explicit + structural absence at declared ownership boundary
- Confidence: high
- Caveats: mechanical stop/shell gates are operationally meaningful current controls. `—` means no qualifying first-party organizational S3 ownership after actor/function separation, not absence of enforcement.

### Absence scope

- Surfaces inspected: stop gate, shell gate, retry/exhaustion incidents, sessionStart state injection, telemetry/current subagent state and orchestrator retry/escalation instructions.
- Plausible first-party paths checked: stop gate as manager; loop-limit escalation; destructive-command HITL; session-level context injection; orchestrator persona as current-control owner.
- Why no material first-party path remains: first-party code evaluates fixed predicates and emits constraints/instructions, while the substantive whole-run judgment and organizational correction are made by the external host model or human.

## S3* — Complementary audit

- State: —
- Function: Harmonist mandates and tracks reviewer roles, but the substantive independent audit judgment is executed by external host-model subagents rather than a first-party Harmonist audit actor.
- Disturbance / variety regulated: implementer completion claims can omit defects, tests, migrations, edge cases, idempotency problems or security issues.
- Decisive decision or feedback right: the `qa-verifier` persona is instructed to compare request/plan/diff and return `done | partially_done | blocked`, but that judgment is produced by the adjacent host model; the hook runner only records reviewer identity/completion markers and configured regression/memory evidence.
- Decision owner: external reviewer subagent instantiated by Cursor/other host runtime.
- Supporting / enforcement mechanisms: readonly reviewer definitions, `AGENT: <slug>` marker contract, reviewer ledger, required `qa-verifier`, optional regression/affected-test gates and stop-gate refusal until markers/evidence exist.
- Closure path: external implementer reports/edits → external orchestrator invokes external reviewer using Harmonist markdown → reviewer model produces substantive finding → first-party hook records that the reviewer ran and may block completion if required process evidence is absent → external host decides corrective work. The semantic audit judgment is outside first-party ownership.
- Why this is / is not agent-owned: `qa-verifier.md` contains a strong independent-review specification, but it is not an executable first-party reviewer runtime. Hook identity is marker-based and cannot independently determine whether the reviewer model's substantive audit was correct or replace the missing actor.
- Evidence: [`agents/review/qa-verifier.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/review/qa-verifier.md); [`hooks/README.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/README.md); [`hooks/scripts/hook_runner.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/scripts/hook_runner.py).
- Basis: explicit + structural absence at declared ownership boundary
- Confidence: high
- Caveats: deterministic regression/affected-test checks provide complementary evidence mechanisms and the reviewer prompt is designed for independence; a composed host deployment may therefore support a strong S3* path, but the required autonomous reviewer is not first-party Harmonist at this boundary.

### Absence scope

- Surfaces inspected: all strict reviewer definitions, `qa-verifier`, reviewer marker/readonly paths, stop-gate reviewer requirements, regression/affected-test options and subagent lifecycle accounting.
- Plausible first-party paths checked: qa-verifier as S3* actor; required-review marker as audit; regression gate as S3*; readonly enforcement as independence; retry-after-review loop.
- Why no material first-party path remains: substantive claim evaluation is performed by an external model persona; first-party hooks attest process events or deterministic test predicates but do not supply an autonomous complementary audit judgment over first-party S1 claims.

## S4 — Intelligence / adaptation

- State: —
- Function: no first-party environment-facing prospective intelligence loop generates and returns an organizational adaptation option into current capability.
- Disturbance / variety regulated: telemetry, usage, incidents, persistent memory, agent-definition freshness and upgrade/version drift can be observed or maintained, but they are not closed into a first-party prospective adaptation decision.
- Decisive decision or feedback right: selection of changed strategy, agent roster, project rules, identity/invariants or future operating capability remains with the external host assistant, project team or pack maintainer.
- Decision owner: none established inside the reviewed runtime boundary.
- Supporting / enforcement mechanisms: usage telemetry, protocol incident logs, memory patterns/decisions, freshness/safety scanners, upgrade tooling, project-context/repo-map data and domain/trend specialist prompts.
- Closure path: no first-party external/future sensing → generated adaptation option → organizational selection → changed current capability loop is wired in the installed runtime. Telemetry/memory can inform a later external agent/human, and upgrade tools can apply an already chosen pack version, but those are support paths.
- Why this is / is not agent-owned: learning/adaptation language in personas/playbooks is executed by external host models, while executable first-party scripts deterministically scan, report, migrate or install. They do not autonomously reason about prospective environmental change and select a returned adaptation.
- Evidence: [`AGENTS.template.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/AGENTS.template.md); [`agents/scripts/upgrade.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/scripts/upgrade.py); [`hooks/scripts/hook_runner.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/scripts/hook_runner.py); [`memory/README.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/memory/README.md).
- Basis: structural absence
- Confidence: high
- Caveats: the catalogue includes trend/optimization specialists and memory can preserve lessons for later sessions, but those actors are external model executions and generic persistence is not S4 closure.

### Absence scope

- Surfaces inspected: telemetry, incidents, memory/patterns/decisions, freshness/safety scanners, repo-map/project-context helpers, upgrade/migration tools, trend/optimization personas and operate/evolve playbooks.
- Plausible first-party paths checked: memory as learning; telemetry-driven adaptation; freshness scan; pack upgrade; trend specialist; reusable-pattern memory.
- Why no material first-party path remains: executable paths report or apply externally selected changes, and adaptive personas require the external host model; no first-party prospective environment-to-option-to-capability decision loop is established.

## S5 — Policy / identity

- State: —
- Function: Harmonist carries and mechanically enforces portions of project policy, but no first-party ultimate-policy/identity decision function is established.
- Disturbance / variety regulated: project invariants, platform/module rules, required review, dangerous-command policy and protocol configuration constrain host-agent behavior.
- Decisive decision or feedback right: the project team/user and external integration/orchestrator process choose the domain identity, invariants, specialist set and configurable policy. Harmonist then injects/enforces those supplied values.
- Decision owner: external human/project owner or external host assistant during integration/customization.
- Supporting / enforcement mechanisms: generated project `AGENTS.md`, project-precedence injection, `.cursor/rules`, hook configuration, manifest/version state, dangerous-command gate and protocol-enforcement rules.
- Closure path: external user/host defines identity/invariants/policy → first-party install/injection/enforcement makes those constraints visible/effective → external host agent operates under them. Harmonist supplies the policy carrier/enforcer but not a first-party legitimate ultimate authority deciding what the organization is or what ultimate policy should be.
- Why this is / is not agent-owned: the template explicitly requires customization of domain identity/invariants and `integrate.py` lists that work among things the script cannot do. Static supplied policy and deterministic enforcement do not by themselves establish S5 ownership.
- Evidence: [`AGENTS.template.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/AGENTS.template.md); [`agents/scripts/integrate.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/agents/scripts/integrate.py); [`integration-prompt.md`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/integration-prompt.md); [`hooks/scripts/hook_runner.py`](https://github.com/GammaLabTechnologies/harmonist/blob/6fd5941cce8c3f6f411fd14cde0daa663ccffa8f/hooks/scripts/hook_runner.py).
- Basis: explicit + structural absence at declared ownership boundary
- Confidence: high
- Caveats: a parent project organization can express genuine S5 policy through Harmonist's AGENTS/rules/hooks surfaces. That may establish S5 in the wider parent organization, but the authority belongs to that parent rather than to first-party Harmonist at the reviewed recursion.

### Absence scope

- Surfaces inspected: project identity/invariant template, project-precedence injection, integration customization flow, protocol rules/config, destructive-command HITL and upgrade/manifest state.
- Plausible first-party paths checked: AGENTS identity block as S5; invariants/rules as S5; destructive-command human gate; user customization as parent S5; pack manifest/version as identity.
- Why no material first-party path remains: Harmonist deterministically transports/enforces policy selected outside its boundary; it does not provide a first-party ultimate-policy decision authority or identity-resolution loop whose decision returns into autonomous first-party operation.

## Assessment summary

Harmonist is a substantial first-party protocol, memory and mechanical-enforcement pack for external coding-agent runtimes, but the frozen standard distribution deliberately does not ship the autonomous host that interprets goals, plans work, invokes specialist/reviewer models and chooses task-level actions. Its hook runtime can deny, ask, record and force protocol follow-up, and its markdown catalogue can define sophisticated organizational roles, yet the qualifying S1 actors and the semantic manager/reviewer intelligence live in adjacent Cursor/Claude/other runtimes. Under Profile 0.2.4 / Methodology 0.3.6, those mechanisms cannot be promoted into repository-relative S2-S5 ownership without first-party operational autonomy and function-specific decision closure.

Proposed canonical outcome: `excluded-no-agentic-vsm` with `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.
