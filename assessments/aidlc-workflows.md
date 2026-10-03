---
harness_id: aidlc-workflows
project_name: AI-DLC Workflows
repository: https://github.com/awslabs/aidlc-workflows
review_ref: 59105b319c344ff51183667727ddca942748d135
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AI-DLC Workflows

## Review boundary

- System in focus: the first-party AI-DLC `core/`, native `aidlc` command, stage/workflow state machine, role/profile composition, hooks, review/approval gates, audit/persistent-state/knowledge machinery and thin harness projections at frozen revision `59105b319c344ff51183667727ddca942748d135`.
- Purpose and identity: turn supported external AI coding harnesses into a structured, auditable software-delivery lifecycle across five phases and 33 stages.
- Relevant environment: user/project requirements, repository artifacts, supported host coding harnesses, host model/provider configuration, tools/MCP services, approval decisions and delivery environments.
- Standard-distribution boundary: AI-DLC-authored core, tools, hooks, stage graph, role prompts, memory/knowledge and harness adapters are inside. Claude Code, Kiro, Codex, Cursor, opencode and GitHub Copilot runtime/model loops remain external host systems and do not donate their autonomous ownership.
- Credited operating / distribution surfaces: README.md; AGENTS.md; `core/`; `core/agents/`; `core/hooks/`; `core/tools/`; `docs/reference/05-agent-system.md`; `harness/<name>/` projections.
- Adjacent first-party surfaces excluded from ownership: CI/release/evaluation tooling, repository-development governance, tests, and any host-harness or model-provider reasoning loop not implemented by AI-DLC.
- First-party operating / deployment modes considered: native `aidlc` configuration/doctor/orchestration tools plus installed Claude/Kiro/Codex/Cursor/opencode/Copilot workflow projections, including role delegation, stage reviews and approval gates.
- Recursion level: one AI-DLC-managed software-delivery workflow embedded into an external coding-agent harness.
- Reviewed revision: `59105b319c344ff51183667727ddca942748d135`.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

AI-DLC owns a substantial deterministic and declarative control layer: stage graph, state, hooks, exact rule delivery, audit events, approval gates, role/persona definitions, model-tier projection, persistent method/knowledge layers and harness-specific adapters. The repository explicitly says one harness-neutral core “runs natively in Claude Code, Kiro CLI, Kiro IDE, Codex CLI, Cursor, opencode, and GitHub Copilot”; model-provider setup belongs to the selected harness.

The agent-system reference states that authored AI-DLC personas are projected into each host harness's native agent surface, inherit host session models/tools, and are delegated through host-native agent/subagent mechanisms. Thus AI-DLC defines role instructions and control constraints, but the open-ended model/tool action loop is executed by the external host harness.

Counterfactual owner test: remove the selected host coding-agent runtime while retaining `aidlc`, stage definitions, hooks, audit state, role Markdown, rules and adapters. AI-DLC can validate/configure state and enforce workflow invariants but cannot autonomously interpret an open-ended software task, choose semantic engineering actions and iterate on their results. First-party S1 does not close.

Primary evidence:

- [README.md](https://github.com/awslabs/aidlc-workflows/blob/59105b319c344ff51183667727ddca942748d135/README.md)
- [AGENTS.md](https://github.com/awslabs/aidlc-workflows/blob/59105b319c344ff51183667727ddca942748d135/AGENTS.md)
- [Agent System](https://github.com/awslabs/aidlc-workflows/blob/59105b319c344ff51183667727ddca942748d135/docs/reference/05-agent-system.md)
- [stage-rule hook](https://github.com/awslabs/aidlc-workflows/blob/59105b319c344ff51183667727ddca942748d135/core/hooks/aidlc-deliver-stage-rules.ts)

## Operational model

A user invokes AI-DLC inside a supported coding harness. AI-DLC supplies workflow/stage/role instructions, state and deterministic hooks; the host harness's model-backed session or native subagent executes those instructions and tools. AI-DLC records/validates state, gates transitions and supplies later stage context. Human approval gates can pause advancement. The semantic software-engineering judgments remain in host agent actors.

## S1 — Operations

- State: —
- Function: no first-party AI-DLC-owned autonomous operational agent loop is established.
- Disturbance / variety regulated: workflow structure, stage completeness, traceability, rule delivery and audit state are first-party regulated; open-ended engineering variety is absorbed by host coding agents.
- Decisive decision or feedback right: interpret the task/artifacts, choose semantic engineering/tool actions, evaluate results and choose the next action or completion within a stage.
- Decision owner: external host-harness model-backed session/subagent.
- Supporting / enforcement mechanisms: stage graph, role prompts, hooks, state machine, skills, knowledge, native `aidlc` tools and review/approval gates.
- Closure path: AI-DLC stage/role/rules → host agent reasoning/tool loop → project effects/evidence → host agent next decision → AI-DLC state/report/gate.
- Why this is / is not agent-owned: AI-DLC supplies strong instructions and deterministic lifecycle control, but the autonomous task-semantic actor is furnished by the selected host harness.
- Evidence: README.md; AGENTS.md; docs/reference/05-agent-system.md.
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: role/persona prompts are first-party artifacts, but prompt authorship alone does not transfer ownership of the host runtime's autonomous loop.

### Absence scope

- Surfaces inspected: core stages/agents/tools/hooks/memory/knowledge, native command, harness projections, role/model-tier projection and workflow documentation.
- Plausible first-party paths checked: conductor skill as S1; domain-agent personas as S1; native `aidlc` command as S1; composer/reviewer agents.
- Why no material first-party path remains: all open-ended agent execution is instantiated by the external harness/model runtime; first-party native tools remain deterministic workflow/control machinery.

## S2 — Coordination

- State: —
- Function: stage dependencies, dispatch structure and shared workflow state organize multiple role executions, but no first-party autonomous S2 owner over first-party S1 units is established.
- Disturbance / variety regulated: ordering, dependency consistency and rule handoff among role/stage work can reduce conflicts.
- Decisive decision or feedback right: choose/revise an interference-specific coordination response among distinct S1 units.
- Decision owner: external conductor/host agent or deterministic stage graph; no first-party autonomous AI-DLC actor established.
- Supporting / enforcement mechanisms: stage graph, dependency edges, dispatch-rule injection, shared memory/state, in-flight tracking and host-native subagent dispatch.
- Closure path: stage/dependency state constrains host dispatch; host agents execute/adjust work.
- Why this is / is not agent-owned: sequencing/dependency enforcement and host-native delegation do not by themselves establish first-party autonomous S2 ownership.
- Evidence: AGENTS.md; core hooks/stage graph.
- Basis: structural absence review.
- Confidence: high.
- Caveats: host agents may coordinate delegated workers, but those autonomous actors remain outside AI-DLC's first-party runtime boundary.

### Absence scope

- Surfaces inspected: stage graph, role collaboration, dispatch hooks, subagent tracking, shared state/memory and workflow profiles.
- Plausible first-party paths checked: dependency sequencing; conductor dispatch; pipeline/mob/subagent stages; shared-memory rules.
- Why no material first-party path remains: AI-DLC supplies orchestration constraints but not a first-party autonomous coordination decision owner over first-party S1 units.

## S3 — Inside-and-now control

- State: —
- Function: deterministic lifecycle/current-state enforcement and human gates exist without first-party autonomous whole-system current-control judgment.
- Disturbance / variety regulated: stage position, completion receipts, review status, transition validity, token/usage evidence and workflow progress.
- Decisive decision or feedback right: discretionary whole-workflow allocation/prioritization/intervention across active operations.
- Decision owner: host agent/human for discretionary choices; AI-DLC tooling deterministically enforces stage/gate rules.
- Supporting / enforcement mechanisms: state machine, hooks, status surfaces, approval gates, stage graph, audit receipts.
- Closure path: current workflow facts → deterministic rule or host/human judgment → stage/dispatch transition.
- Why this is / is not agent-owned: strong state enforcement is not autonomous current-control ownership.
- Evidence: README.md; AGENTS.md; core hooks/tools.
- Basis: structural absence review.
- Confidence: high.
- Caveats: a host conductor may exercise whole-workflow judgment, but that actor belongs to the external harness.

### Absence scope

- Surfaces inspected: workflow state, transitions, hooks, stage graph, approval gates, status and dispatch controls.
- Plausible first-party paths checked: orchestrator/conductor; state validator; approval handoff; stage scheduler; token/usage controls.
- Why no material first-party path remains: discretionary current-control judgment is external; first-party paths enforce/record selected constraints.

## S3* — Complementary audit

- State: —
- Function: AI-DLC defines reviewer personas, review stages, sensors and evidence receipts, but their semantic audit judgment is executed by external host agents.
- Disturbance / variety regulated: design/product/code quality claims and stage completion evidence can be independently challenged.
- Decisive decision or feedback right: independently judge the operational artifact and return findings that alter later work.
- Decision owner: model-backed reviewer instantiated by the external host harness; deterministic AI-DLC sensors can validate structural claims only.
- Supporting / enforcement mechanisms: reviewer prompts, read-scope/write-freeze hooks, sensors, review receipts, stage gates and audit trail.
- Closure path: artifact → host-instantiated reviewer/sensor → findings/receipt → workflow gate or follow-up stage.
- Why this is / is not agent-owned: AI-DLC specifies and constrains the audit path but does not supply the autonomous reviewer runtime.
- Evidence: docs/reference/05-agent-system.md; AGENTS.md; core hooks.
- Basis: explicit + structural negative publication review.
- Confidence: high.
- Caveats: deterministic sensors may close narrow checks, but Methodology S3* publication requires the independent audit judgment/ownership path, not merely validation machinery.

### Absence scope

- Surfaces inspected: reviewer personas, review stages, sensors, review receipt enforcement, audit trail and host projections.
- Plausible first-party paths checked: architecture/product reviewers; sensors; review gates; write-freeze/read-scope hooks.
- Why no material first-party path remains: semantic reviewer discretion is supplied by external host agents, while first-party validators are deterministic support.

## S4 — Outside-and-then intelligence

- State: —
- Function: persistent team/project knowledge, learned rules, adaptive composer and workflow profiles provide adaptation mechanisms but do not establish first-party autonomous prospective adaptation ownership at this boundary.
- Disturbance / variety regulated: future workflow shape, team practices, model policies and project-specific rules may be revised.
- Decisive decision or feedback right: interpret external/prospective evidence and choose a persistent capability/organizational adaptation.
- Decision owner: host model actor and/or human/operator; AI-DLC persists/enforces the resulting configuration.
- Supporting / enforcement mechanisms: memory layers, knowledge, composer prompts, profile composition, model policy and plugin/configuration machinery.
- Closure path: external/host/human judgment → persisted AI-DLC configuration/knowledge → later workflow behaviour.
- Why this is / is not agent-owned: persistent adaptation surfaces exist, but autonomous judgment is not supplied by a first-party AI-DLC actor.
- Evidence: README.md; AGENTS.md; agent-system reference.
- Basis: structural absence review.
- Confidence: high.
- Caveats: “learned rules” and composer naming do not transfer host-model ownership into AI-DLC.

### Absence scope

- Surfaces inspected: org/team/project memory, knowledge, composer agent, workflow profiles, plugins, model/tier policy and refresh/configuration.
- Plausible first-party paths checked: adaptive composer; learned rules; feedback-optimization stages; model-policy adaptation.
- Why no material first-party path remains: the persistent machinery stores/projects adaptations selected by external host agents or humans.

## S5 — Policy and identity

- State: —
- Function: methodology rules, approvals, guard policies and role/tool restrictions constrain operation without first-party autonomous identity/ultimate-policy resolution.
- Disturbance / variety regulated: workflow policy, stage/role authority, review class, guard policy and approval requirements.
- Decisive decision or feedback right: resolve identity/ultimate-policy tensions for the organization and authoritatively return that resolution.
- Decision owner: framework authors/project humans or external host agent under supplied policy.
- Supporting / enforcement mechanisms: core rules, hooks, approval gates, guard-policy configuration, role tool restrictions and state-transition enforcement.
- Closure path: authored/operator policy → AI-DLC enforcement/projection → host-agent operation.
- Why this is / is not agent-owned: static/configured policy and approval enforcement do not constitute autonomous S5 ownership.
- Evidence: README.md; AGENTS.md; core hooks/rules.
- Basis: structural absence review.
- Confidence: high.
- Caveats: human approval gates are operational gates, not automatically parent S5.

### Absence scope

- Surfaces inspected: core methodology rules, role authority, guard policy, approvals, configuration/model policy and transition hooks.
- Plausible first-party paths checked: approval gates; guard policy; role definitions; methodology identity; plugin policy.
- Why no material first-party path remains: ultimate policy choices are authored or operator-selected rather than autonomously resolved by a first-party actor.

## Recursion

AI-DLC is assessed as a workflow/control organization embedded into an external host coding harness. Its role personas and conductor instructions shape external agent actors but do not make the host agent runtime first-party AI-DLC ownership.

## Variety and escalation

AI-DLC attenuates variety through stage decomposition, role specialization, deterministic hooks, state/audit records, review gates, sensors, memory/knowledge and harness-neutral projections. Ambiguous semantic work and discretionary review/adaptation remain with host agents or humans.

## Evidence gaps

- Frozen revision only.
- Host-harness internal organizational functions are not imported.
- CI/live-model test infrastructure is adjacent development/evaluation evidence, not standard-distribution ownership.

## Assessment summary

At the frozen revision, AI-DLC Workflows provides a sophisticated first-party organizational control methodology around multiple host coding-agent harnesses. Its deterministic engine, prompts, roles, reviews and adaptation surfaces strongly shape execution, but the autonomous open-ended reasoning/tool loops are instantiated by external host systems. First-party S1 therefore does not close. Proposed terminal disposition: excluded-no-agentic-vsm.

**Vector:** — · — · — · — · — · —
