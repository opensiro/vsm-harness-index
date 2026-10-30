---
harness_id: agent-from-scratch
project_name: Agent From Scratch
repository: https://github.com/liiiiiiiiil/coding-agent-from-scratch
review_ref: cd7ec0ee2031d1723e1d38593d43385778fd5d30
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-30
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Agent From Scratch

## Review boundary

- System in focus: the first-party `mini_agent` v0.51 Python coding-agent runtime at the frozen commit `cd7ec0ee2031d1723e1d38593d43385778fd5d30`; its main model/tool loop, repository tools, permissions, task/plan state, recovery, context/session/memory, provider adapters, and model-callable read-only Subagent delegation.
- Purpose and identity: a local software-development agent built as a step-by-step educational implementation, with operative code rather than a prompt-only tutorial. The English README explicitly positions v0.51 as a coding benchmark/evaluation milestone without claiming real-model benchmark scores.
- Relevant environment: an authorized local project tree, user instructions/tasks, selected model endpoint, tool results, code/test evidence, plan state, child reviewer findings, and optional MCP or skill material.
- Standard-distribution boundary: `src/mini_agent` and its CLI are credited. Bundled tutorials, offline tests, benchmarking runners and authoring governance corroborate intent but are not imported as independently running organizational regulators in an ordinary coding session.
- Credited operating / distribution surfaces: `agent.py`, `runtime.py`, `tools/file.py`, `tools/shell.py`, `tools/plan.py`, `state.py`, `recovery.py`, `tools/delegation.py`, `delegation.py`, `agent_profiles.py`, `context.py`, `session.py`, `memory.py`, `permission.py` and the built-in CLI wiring.
- Adjacent first-party surfaces excluded from ownership: `evaluation/` and benchmark reports are separately invoked evaluation facilities, not an always-on external S3* or S4 owner; docs/plans/governance and tutorial snapshots are not runtime organizational actors. Providers, models, external MCP servers, the host shell and target repositories are environment/dependencies, not donated control functions.
- First-party operating / deployment modes considered: interactive task execution with tool permission prompts or preauthorized rules; explicit plan/replan, failure recovery, process/session continuation and memory; synchronous read-only `delegate_task` and background `spawn_subagent` plus result retrieval; named built-in `reviewer`/`explorer`/`tester` profiles. Actual model service availability remains external.
- Recursion level: the agent-assisted local coding task/workspace. The main mutating parent is the operational S1. Read-only specialist investigations are complementary observers, not independent mutating S1 cells; parallel tool calls/processes do not by themselves create an S1 population.
- Reviewed revision: `cd7ec0ee2031d1723e1d38593d43385778fd5d30` (the exact ref frozen in intake #966, controller #970 row 5, also listed as an identity alias in #989).
- Observation date: 2026-10-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The standard-library Python `AgentRuntime.run()` is a model→tool→observation loop. The selected model receives context, proposes repository/file/shell/plan/delegation tools, and subsequent turns receive execution results. `ParentRuntimePolicy` governs approval, planning, durable tool boundaries, completion reminders, process waits and recovery. Its many checkpoints are largely deterministic *constraints on* current work, not separate autonomous S3 ownership.

The parent can invoke `delegate_task` (synchronous) or `spawn_subagent` (background), and later retrieve `get_subagent_result` or issue a bounded follow-up. At v0.51, those children are restricted to read/search/calculation under scope gates; the named built-in `reviewer` profile is instructed to identify actual correctness, boundary and regression risks. `SubagentRunner` creates distinct state, context, system prompt, model binding and tool view. Child reports must contain evidence linked to actual first-party read-only observations before their findings return to the parent. This is a complementary evidence route for auditing the parent's implementation, even though the parent retains the right to accept or repair it.

The project also ships plan revisions, execution/recovery trace, checkpoint rollback, session persistence, external workspace memory, skills and a separately launched evaluation harness. These improve operational reliability, but there is no first-party multi-mutating-agent interference attenuation loop, whole-population allocation decision, prospective adaptation/selection loop or ultimate identity-policy adjudicator in the assessed runtime.

Primary frozen evidence:

- [`runtime.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/runtime.py)
- [`agent.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/agent.py)
- [`agent_profiles.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/agent_profiles.py)
- [`tools/delegation.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/tools/delegation.py)
- [`delegation.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/delegation.py)
- [`state.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/state.py)
- [`memory.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/memory.py)
- [English README](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/README_EN.md)

## Operational model

An interactive user requests a code change. The main Agent may inspect/search files, choose a patch/command, observe an execution result, update its plan and retry/repair. It can delegate a read-only code review to the `reviewer` role and inspect the returned source-linked findings before deciding on the next edit. Permissions and plan/recovery guards may refuse actions, and the parent can be held at an awaiting state while background investigations are unclaimed.

The evaluation runner freezes tasks and independent graders, but is an offline/separately invoked benchmark path rather than the ordinary coding agent's independent in-run quality governor. Neither its fixtures nor the author's future lesson roadmap are credited as S4/S5 governance.

## S1 — Operations

- State: A
- Function: perform task-specific software engineering, including investigating code, editing project files, running tests/commands and iterating on observed failures.
- Disturbance / variety regulated: unknown repository structure, incomplete user requirements, file/content changes, command/test failures, tool errors, recovery and context limitations.
- Decisive decision or feedback right: choose the next code/tool/plan action and revise behavior after each observed tool result.
- Decision owner: the model-backed parent Agent executing through `AgentRuntime` and `ParentRuntimePolicy`.
- Supporting / enforcement mechanisms: file/shell/search tools, tool registry/permission gate, plan state, execution generations, recovery/checkpoint machinery, context budget, traces and sessions.
- Closure path: user task and workspace → model-selected tool/action → first-party execution against the codebase → result/failure and state returned to model context → next corrective/continuation action.
- Boundary reachability: standard `python -m mini_agent` task execution binds the parent runtime to enabled file/shell/plan tools; model inference is externally provided but the operative action/feedback loop is first-party.
- Why this is / is not agent-owned: removing the model actor leaves a deterministic tool executor and protection machinery without an agent able to choose problem-specific code modifications or react semantically to tests.
- Evidence: [`runtime.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/runtime.py); [`agent.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/agent.py); [`tools/file.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/tools/file.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: permission prompts can pause an unapproved side effect; a supported preauthorized configuration closes this path without repeated human decision. No live provider E2E was run for this review.

## S2 — Coordination

- State: —
- Function: no material inter-S1 interference attenuation loop established at the coding-task recursion.
- Disturbance / variety regulated: parallel observations, child task overlap, or concurrent shell calls may require scheduling and isolation, but the packaged children are read-only investigators and not competing mutating S1 units.
- Decisive decision or feedback right: not evidenced for a plurality of mutating S1 units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: child concurrency and aggregate budgets, fixed role/tool/scoping restrictions, ordered result delivery, task/process lifecycle controls and plan-step serialization.
- Closure path: no evidence of independent mutating S1 cells whose operational conflicts are identified and attenuated through a feedback relation. Read-only isolation and ordered tool results protect execution but do not prove S2 at this recursion.
- Why this is / is not agent-owned: generic parallel calls, single-parent work, restricted child investigations and sequencing are not a separately regulated inter-S1 coordination function.
- Evidence: [`tools/delegation.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/tools/delegation.py); [`delegation.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/delegation.py); [`runtime.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/runtime.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: source implements deliberate safety isolation for read-only children; that is valuable but not the inter-operational attenuation required here.

### Absence scope

- Surfaces inspected: parent action loop, synchronous/background child delegation, role capabilities, tool authorization/scope gates, process controls, plan and result ordering.
- Plausible first-party paths checked: concurrent mutating child workers, file/worktree ownership claims, shared workspace collision detection/negotiation, child-child interference resolution and cross-S1 reallocation.
- Why no material first-party path remains: bundled child tool allowlists contain no mutating repository action; only the parent executes code-changing work, so the needed inter-S1 disturbance/feedback relation is absent.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system discretionary current-commitment/resource control loop over a population of operational S1 cells.
- Disturbance / variety regulated: plan drift, failed tools, active processes and unfinished background child work are monitored or gated, but within a single parent task rather than organization-wide current S1 priorities.
- Decisive decision or feedback right: no actor controls the current commitments of multiple semi-autonomous operational units based on a whole-system view.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `ParentRuntimePolicy`, plan revisions and reminders, task/state tracker, durable tool boundary, child cancellation/result claiming, process cleanup, recovery rules and budgets.
- Closure path: the parent can change its own plan, cancel a read-only investigation or wait for a process; there is no live multi-S1 overview → discretionary resource/priority judgment → changed commitments across an operational population → feedback loop.
- Why this is / is not agent-owned: the parent is an autonomous coding actor (S1); its self-management and deterministic task guards should not be relabeled whole-system S3.
- Evidence: [`agent.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/agent.py); [`state.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/state.py); [`tools/delegation.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/tools/delegation.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: planning, cancellation and recovery are substantial first-party controls; the missing element is the whole-system recursion/decision scope, not an absence of safeguards.

### Absence scope

- Surfaces inspected: task/plan states and revisions, background process tools, child statuses and cancellations, main runtime decisions, recovery/checkpoint, CLI control surfaces.
- Plausible first-party paths checked: fleet-wide operational status, competing S1 commitments and budgets, model-owned worker reassignment/prioritization, live operational portfolio correction and escalation from lower S1 cells.
- Why no material first-party path remains: the supported delegation population is read-only and subordinate to one mutating parent; no model or parent control plane exercises discretionary whole-S1 resource allocation.

## S3* — Complementary audit

- State: A
- Function: independently challenge a coding result with a separately instantiated read-only reviewer which re-reads source evidence and reports concrete defects/regression risks.
- Disturbance / variety regulated: unnoticed implementation defects, incorrect assumptions, missing boundary checks and regression risks in the parent agent's engineering decisions.
- Decisive decision or feedback right: a model-backed child `reviewer` selects defects/claims and supporting observed evidence independently of the implementer's own self-report; parent retains corrective action rights.
- Decision owner: the separately instantiated reviewer `SubagentRunner`, scoped by the built-in `reviewer` profile.
- Supporting / enforcement mechanisms: model-callable `delegate_task` / `spawn_subagent`, built-in frozen `reviewer` prompt and read-only allowlist, child `AgentRuntime`, independent state/context and model binding, evidence-backed `SubagentResult`, background status/result/follow-up tools.
- Closure path: parent implements a change → model autonomously delegates source review to `agent_profile="reviewer"` → child reads/searches source using its own model/tools → evidence-linked findings return to parent through a tool result → parent can repair/retest or order follow-up before final acceptance.
- Boundary reachability: the parent registry exposes both delegation tools in the normal model-facing runtime; `AgentProfileCatalog` ships `reviewer` by default; `SubagentRunner` constructs a new context/tool executor without relying on an external review service.
- Claim being audited: the correctness and regression safety of the current coding implementation or task result.
- Ordinary reporting path: parent model's own file/command results, plan progression and terminal task response.
- Complementary access path: a separate role-specific model loop performs direct scoped file reads/grep/listing and must link claims to actual observed tool output; it need not accept the parent's implementation narrative.
- Independence boundary: independent child state, context, prompt, role, execution budget and read-only tool enforcement; model provider may be the same family, and the parent supplies goal/scope and selected facts, so this is organizational/evidence-path independence rather than provider diversity or a mandatory external assessor.
- Who acts on findings: the parent Agent receives synchronous results immediately or explicitly claims a background result; it decides subsequent corrections or verification, and may request another reviewer pass.
- Why this is / is not agent-owned: fixed schemas can reject unsupported evidence but cannot identify arbitrary defects or their significance without the child model's substantive review judgment.
- Evidence: [`agent_profiles.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/agent_profiles.py); [`tools/delegation.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/tools/delegation.py); [`delegation.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/delegation.py); [`agent.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: review must be chosen by the parent, not run automatically for every change. Read-only reviewer findings are not automatically promoted to independent verification state; they are complementary audit feedback for possible subsequent S1 correction. The separate benchmark grader is not credited for this positive runtime path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/prospective organizational adaptation loop closed.
- Disturbance / variety regulated: historical tool results, retrieved memories, skill definitions, benchmark outcomes and the author's lesson roadmap are available as context or offline artifacts, but no standard agent-owned response to a future environmental change is enacted as durable organizational capability adaptation.
- Decisive decision or feedback right: no separate prospective intelligence/adaptation actor with authority to select and implement persistent changes to the operating system.
- Decision owner: not established.
- Supporting / enforcement mechanisms: explicit workspace memory editing and retrieval, context compaction, skill discovery, model configuration, plan revision and separately launched `evaluation/` benchmark tools.
- Closure path: memory retrieval feeds ordinary task context; benchmark reports remain external evaluation outputs; neither establishes sensing an outside future → generating alternatives → approving/enacting a persistent capability change → operational feedback.
- Why this is / is not agent-owned: remembering a prior observation and changing the current task plan are S1 context/actions, not the required future-facing organizational adaptation.
- Evidence: [`memory.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/memory.py); [`context.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/context.py); [`evaluation/runner.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/evaluation/runner.py); [English README](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/README_EN.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: benchmarks may later inform human developers; no experimental result or unmerged roadmap feature is attributed to the frozen runtime.

### Absence scope

- Surfaces inspected: memory write/recall, context retrieval, skills, provider/model configuration, plan/replanning, evaluation runner/reports, educational roadmap and CLI lifecycle.
- Plausible first-party paths checked: future-environment sensing, adaptive skill or model adoption, experiment-driven policy/capability update, persistent organizational redesign, automatic benchmark-to-runtime feedback.
- Why no material first-party path remains: relevant updates are task-local, explicit user configuration, or offline developer/evaluator activities, with no owned, enacted prospective adaptation cycle in normal agent operation.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate identity/policy adjudication and authoritative return to the operating organization.
- Disturbance / variety regulated: user/project instructions, permission policy, plan approval and child role restrictions constrain work, but do not form autonomous highest-level purpose or identity governance.
- Decisive decision or feedback right: no actor may legitimately redefine the agent organization's final mission, identity, or policy for subsequent work.
- Decision owner: not established; highest-level purpose and permissions remain human/configuration-authored.
- Supporting / enforcement mechanisms: project `AGENTS.md` injection, system prompts, permission policy/gate, CLI user approvals, fixed child profile contracts, plan approval and task stop rules.
- Closure path: authored instructions/policies → enforcement/approval/denial during task execution; no operational identity conflict → ultimate-authority decision → authoritative organization-wide policy update/return loop.
- Why this is / is not agent-owned: model tool selection operates inside externally defined rules and cannot claim authority to rewrite them merely through planning or skills.
- Evidence: [`permission.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/permission.py); [`instructions.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/instructions.py); [`agent_profiles.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/agent_profiles.py); [`state.py`](https://github.com/liiiiiiiiil/coding-agent-from-scratch/blob/cd7ec0ee2031d1723e1d38593d43385778fd5d30/src/mini_agent/state.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: ordinary user authority is important to the system's safety, but external human approval is not by itself an internally owned S5 loop under this assessment boundary.

### Absence scope

- Surfaces inspected: prompt/instruction generation, config and permission enforcement, agent profile definitions, task/plan approvals, session/recovery/skill paths and author governance documents.
- Plausible first-party paths checked: ultimate-policy appeal, constitutive identity decisions, conflict between mission and operations, policy revision accepted as authoritative by the entire agent runtime.
- Why no material first-party path remains: governance remains user/developer authored and runtime mechanisms apply preexisting constraints without a distinct identity-decision-and-return capability.

## Recursion

Only the parent is a mutating engineering S1 at this level. A read-only review child can be an S3* complementary auditor without being promoted to S1 or implying S2/S3. Nested mutating organizational cells are not evidenced; child delegation is single-level and scoped.

## Variety and escalation

Local file/shell tools amplify the parent agent's operational repertoire. Permission patterns, deterministic planning/recovery guards, scoped child capabilities, budgets, evidence assertions, durable session boundaries and checkpoint tools attenuate operational risk. A reviewer finding is delivered to the parent; a tool failure or uncertain effect can lead to recovery or an explicit user decision. These are concrete paths, but no whole-system S3 or ultimate-policy S5 is inferred from them.

## Evidence gaps

The frozen runtime, source-visible supported modes, built-in reviewer role and absence candidates were inspected. No live provider-backed E2E agent run was undertaken. Thus the states describe source-supported ownership/closure at the pinned revision, not measured success rates or mandatory reviewer invocation. The separate benchmark explicitly has no live model baseline as of this source snapshot.

## Assessment summary

Agent From Scratch closes autonomous **S1** through its model-directed coding/tool loop and autonomous **S3*** through the model-callable, separately instantiated, read-only evidence-grounded reviewer. Read-only delegation does not establish a population of mutating S1 cells for S2/S3, while memory and offline evaluation lack prospective S4 adaptation and configured approvals do not close S5.

Proposed vector: **`A · — · — · A · — · —`**
