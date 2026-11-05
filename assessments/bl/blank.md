---
harness_id: blank
project_name: Blank
repository: https://github.com/purplemacaron/blank
review_ref: e7a48c0445599217f8fa2b7320dee6b446735345
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# Blank

## Review boundary

- System in focus: the local Blank desktop/CLI agent composition, including configured specialist and operator-reviewed reflection modes.
- Purpose and identity: perform local workspace, research, code and document/media tasks through a provider-backed agent and approval-gated tools.
- Relevant environment: user requests/corrections, workspace files and diffs, web sources, model providers, MCP/SSH/computer/media services.
- Standard-distribution boundary: first-party Node agent loop, tools, prompt/config/store, Electron IPC and supported CLI; external model and tool services are dependencies.
- Credited operating / distribution surfaces: src/core/agent.js and tool/prompt/config/store composition, configured read-only Critic path and the wired learn reflection/Apply path.
- Adjacent first-party surfaces excluded from ownership: Pages/release workflows, QA screenshots, test fixtures and development instructions. No external provider or plugin internal functions are borrowed.
- First-party operating / deployment modes considered: normal Agent/Coding/Design, read-only Ask/Plan, optional team mode, manual/opt-in automatic reflection and operator Apply. Timed sessions and remote approvals were checked as support.
- Recursion level: one local workspace agent organization; child tasks and sessions do not establish complete recursive systems.
- Reviewed revision: `e7a48c0445599217f8fa2b7320dee6b446735345`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Blank has its own streaming model→tool→result loop in src/core/agent.js, not an external CLI coding loop. runAgent prepares prompts and tool definitions, records assistant/tool messages, executes tools and returns outputs into the next turn. runSubagent creates a separate prompt/history with bounded read-only or write tools. The main model can delegate individual jobs, up to four parallel jobs or a configured team; subagents return reports to its tool result. Configuration supplies Scout/Architect/Critic roles, with team opt-in. Approvals constrain actual tools; step limits, context compaction and fallback selection are support.

The Electron IPC layer calls runAgent, maintains cancellation/approval routing and invokes optional post-run reflection. src/core/learn.js reads recent user/agent/tool sessions and proposes memory, standing instructions or recurring workflow skills. Operator learn:apply applies a selected insight to the actual memory/config/skill store; later prompts and available skills consume it. src/core/schedules.js supplies fixed timer metadata; worktree.js is a manual lifecycle utility. These are distinguished from autonomous current control. Text source was obtained at the exact frozen commit after a clone transport timeout; no head substitution occurred.

## Operational model

The main agent and optional workers own bounded task execution, including tool and implementation choices. A shipped Critic role offers an audit-specific construction path with separate read-only source access, but the caller must compose the concrete audited claim and corrective contract. Reflection differs from mere retained chat: it proposes future reusable capabilities from repeated user needs/corrections and has an explicit owner-selected adoption path.

## S1 — Operations

- State: A
- Function: perform concrete workspace/research/code/document tasks.
- Disturbance / variety regulated: unknown files, requested changes, tool errors and provider failure.
- Decisive decision or feedback right: select tools/edits and revise work from returned results until a response or bounded stop.
- Decision owner: main model actor and configured subagents within first-party tool loops.
- Supporting / enforcement mechanisms: provider streaming, allowlists/approval policy, tool dispatch, session persistence, maximum steps, compaction and fallback.
- Closure path: assistant tool calls → executeTool → saved tool messages → subsequent model turn; reports/results return to user and main agent.
- Boundary reachability: desktop IPC and bin/blank.js instantiate the shipped runAgent; child execution is implemented in runSubagent with its own history and tools.
- Why this is / is not agent-owned: without the model actor the dispatcher and store cannot choose task-specific operations; provider transports do not own those choices.
- Evidence: [src/core/agent.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/agent.js); [src/core/tools.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/tools.js); [src/core/prompt.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/prompt.js); [electron/ipc.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/electron/ipc.js).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Local/provider permissions bound action; no paid-model or desktop E2E run claimed.

## S2 — Coordination

- State: —
- Function: inter-S1 conflict attenuation
- Disturbance / variety regulated: the candidate organizational variety is considered in the checked alternatives below.
- Decisive decision or feedback right: no qualifying function-specific decisive path established.
- Decision owner: ordinary agent/user/developer rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/core/agent.js`, `src/core/worktree.js`, `src/core/tools.js`
- Closure path: delegate_many/team_delegate fan out tasks in the same workspace and aggregate reports; their limits are fan-out bounds. Exact file edits and manually created worktrees are not tied here to a shipped worker collision-settlement loop. No explicit inter-worker interference feedback protocol is supplied.
- Why this is / is not agent-owned: no positive functional witness remains after the supported alternatives are distinguished.
- Evidence: [src/core/agent.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/agent.js); [src/core/worktree.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/worktree.js); [src/core/tools.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/tools.js).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded absence in the reviewed distribution, not impossibility of a custom extension.

### Absence scope

- Surfaces inspected: src/core/agent.js, src/core/worktree.js, src/core/tools.js and README, configured execution/desktop wiring.
- Plausible first-party paths checked: delegate_many/team_delegate fan out tasks in the same workspace and aggregate reports; their limits are fan-out bounds. Exact file edits and manually created worktrees are not tied here to a shipped worker collision-settlement loop. No explicit inter-worker interference feedback protocol is supplied.
- Why no material first-party path remains: The inspected paths support work or runtime implementation but do not close inter-S1 conflict attenuation in this distribution.

## S3 — Inside-and-now control

- State: —
- Function: whole-system current resource/commitment control
- Disturbance / variety regulated: the candidate organizational variety is considered in the checked alternatives below.
- Decisive decision or feedback right: no qualifying function-specific decisive path established.
- Decision owner: ordinary agent/user/developer rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/core/agent.js`, `src/core/schedules.js`, `electron/ipc.js`, `src/core/approvals.js`
- Closure path: Main-agent planning/delegation is local task execution. Static per-run step limits, at most two scheduled runs, cancellation and session UI do not provide a separate whole-system resource bargaining/intervention decision. Generic local/remote approvals do not close a function-specific parent S3 mode.
- Why this is / is not agent-owned: no positive functional witness remains after the supported alternatives are distinguished.
- Evidence: [src/core/agent.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/agent.js); [src/core/schedules.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/schedules.js); [electron/ipc.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/electron/ipc.js); [src/core/approvals.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/approvals.js).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded absence in the reviewed distribution, not impossibility of a custom extension.

### Absence scope

- Surfaces inspected: src/core/agent.js, src/core/schedules.js, electron/ipc.js, src/core/approvals.js and README, configured execution/desktop wiring.
- Plausible first-party paths checked: Main-agent planning/delegation is local task execution. Static per-run step limits, at most two scheduled runs, cancellation and session UI do not provide a separate whole-system resource bargaining/intervention decision. Generic local/remote approvals do not close a function-specific parent S3 mode.
- Why no material first-party path remains: The inspected paths support work or runtime implementation but do not close whole-system current resource/commitment control in this distribution.

## S3* — Complementary audit

- State: C
- Function: a specifically configured complementary source-risk review of operational work.
- Claim being audited: an implementation or proposed result is correct, secure and adequately tested.
- Ordinary reporting path: the main/worker's answer and its own reported checks.
- Complementary access path: separate read-only Critic run can inspect workspace source and git_diff rather than merely repeat the producer transcript; bundled Code review procedure names diff/call-site/evidence checks.
- Independence boundary: new child prompt/history, default Critic write=false and direct read/grep/glob/project_map/git_diff tools. The generic main-agent self-review is not credited.
- Who acts on findings: the caller/main actor receives reports and remains responsible for verification; a claim-specific corrective and recheck contract must still be composed.
- Disturbance / variety regulated: producer blind spots and unverified correctness/security/test claims.
- Decisive decision or feedback right: judge concrete source risks and return evidence-backed findings.
- Decision owner: configured Critic agent for judgment; the caller/developer still supplies claim selection and corrective closure authority.
- Supporting / enforcement mechanisms: team configuration, read-only child tools, report aggregation and optional role model.
- Closure path: review-specific brief → isolated direct-evidence Critic → report tool result to main; no shipped mandatory fix/recheck or automatic audit acceptance transaction is established.
- Boundary reachability: team config ships an audit-specific Critic role and team_delegate instantiates it in the ordinary product; the bundled Code review skill supplies source-oriented review procedure.
- Why this is / is not agent-owned: a function-specific audit construction path is present, but fully autonomous audit/control closure is not established merely by calling a generic specialist.
- Evidence: [src/core/config.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/config.js); [src/core/agent.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/agent.js); [src/core/prompt.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/prompt.js); [assets/skills/code-review/SKILL.md](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/assets/skills/code-review/SKILL.md).
- Basis: structural.
- Confidence: medium; constructor only, no claimed ready-made audit loop.
- Caveats: Team is off by default. A role named Critic alone would be insufficient; the C claim is limited to the explicit separate-context source-risk inspection path and leaves corrective composition unresolved.

## S4 — Outside-and-then intelligence

- State: P
- Function: adapt future assistance capability to evidenced recurring user needs and corrections.
- External distinction: user preferences, repeated corrections and recurring workflows appear in recent sessions, contrasted with current durable memory and skills.
- Future / prospective distinction: reflection explicitly requires durable facts useful weeks later and skills for workflows actually performed that will recur; transient task details are excluded.
- Adaptation option generated: model proposes memory, a standing instruction or a reusable SKILL.md, with reason/confidence, rather than silently changing the system.
- Path back into current capability / S3: operator Apply calls learn:apply → applyInsight updates memory/customInstructions or creates an actual skill; subsequent runAgent reloads skills/memory and buildSystemPrompt consumes instructions.
- Disturbance / variety regulated: repeated user-specific demand and correction that the existing capability repertoire fails to retain.
- Decisive decision or feedback right: choose which proposed durable capability/instruction changes are adopted.
- Decision owner: local operator using the learning proposal Apply action; model owns proposal content, not final adoption.
- Supporting / enforcement mechanisms: reflection model, validated insight store, IPC/UI action, memory/config/skill writers and next-turn prompt construction.
- Closure path: external user evidence → future-oriented reusable proposal → owner applies selected insight → present repertoire/instructions change → later sessions use it.
- Boundary reachability: manual learn:reflect and optional maybeReflect are wired in Electron IPC; learn:apply is the shipped adoption handler, not a development-only example.
- Why this is / is not agent-owned: automatic reflection generates proposals only. The final adaptation judgment remains operator-owned; passive history or arbitrary memory addition is not the credited witness.
- Evidence: [src/core/learn.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/learn.js); [electron/ipc.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/electron/ipc.js); [src/core/agent.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/agent.js); [src/core/prompt.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/prompt.js).
- Basis: structural.
- Confidence: medium-high for the explicit future-reuse/adoption path.
- Caveats: Not every insight is S4; the witness is externally evidenced recurring demand developed into future capability. No autonomous A base or empirical improvement claim.

## S5 — Policy and identity

- State: —
- Function: identity or ultimate-policy closure
- Disturbance / variety regulated: the candidate organizational variety is considered in the checked alternatives below.
- Decisive decision or feedback right: no qualifying function-specific decisive path established.
- Decision owner: ordinary agent/user/developer rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/core/prompt.js`, `src/core/approvals.js`, `src/core/config.js`, `src/core/learn.js`
- Closure path: System identity, project instruction files, learned preferences, modes and permission approval matrices bound execution. The user can accept an insight or grant a tool action, but no first-party path identifies and resolves a constitutional/ultimate-policy issue with a returned authoritative settlement. Adaptation of a workflow or preference is not automatically S5.
- Why this is / is not agent-owned: no positive functional witness remains after the supported alternatives are distinguished.
- Evidence: [src/core/prompt.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/prompt.js); [src/core/approvals.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/approvals.js); [src/core/config.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/config.js); [src/core/learn.js](https://github.com/purplemacaron/blank/blob/e7a48c0445599217f8fa2b7320dee6b446735345/src/core/learn.js).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded absence in the reviewed distribution, not impossibility of a custom extension.

### Absence scope

- Surfaces inspected: src/core/prompt.js, src/core/approvals.js, src/core/config.js, src/core/learn.js and README, configured execution/desktop wiring.
- Plausible first-party paths checked: System identity, project instruction files, learned preferences, modes and permission approval matrices bound execution. The user can accept an insight or grant a tool action, but no first-party path identifies and resolves a constitutional/ultimate-policy issue with a returned authoritative settlement. Adaptation of a workflow or preference is not automatically S5.
- Why no material first-party path remains: The inspected paths support work or runtime implementation but do not close identity or ultimate-policy closure in this distribution.

## Distributed OSS parent arrangement

The parent adaptation owner is the local operator. Maintainer releases and unrelated users' installations do not form an evidenced common OSS parent organization.

## Self-hosted and non-human modes

Hosted/local provider choice changes transport. Optional team and reflection are supported first-party configurations; parent S4 is a real Apply path, not a P state inferred from arbitrary UI settings.

## Recursion

Subagents have bounded tasks and contexts, but no demonstrated full recursive metasystem.

## Variety and escalation

Tool approvals, errors, session checkpoints, fallback, compaction and fixed timers manage implementation variety. These mechanisms are not automatically S2/S3 or algedonic channels.

## Evidence gaps

Static source review; Node runtime is unavailable on the remote review host, so no native JS suite, packaged desktop or provider-backed E2E was run. The C audit finding deliberately does not assert autonomous corrective closure; parent S4 does not assert measured benefit.

