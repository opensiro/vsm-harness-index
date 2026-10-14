---
harness_id: scoot
project_name: scoot
repository: https://github.com/sergenes/scootcli
review_ref: b6712481f1ba8b1b5694713ee60fb33d1afd5771
reviewed_at: 2026-10-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# scoot

## Review boundary

- System in focus: one installed first-party scoot (scootcli) Python terminal coding agent, including the `Agent.run_turn` model/tool feedback loop, provider pool, shell/file tools, approval and hook policies, session/context, headless JSONL mode, plan tool and opt-in single-run worktree.
- Purpose and identity: execute operator-specified coding instructions by interpreting project state, selecting and applying coding tools and returning a completion/incomplete/error result, optionally in a headless operator-controlled process.
- Relevant environment: changing software repository, model endpoints and model availability, shell/file commands, errors, human tool approvals, project preferences and user-supplied extensions.
- Standard-distribution boundary: first-party installable Python wheel/zipapp with `scoot` CLI/REPL or headless protocol, `src/scootcli/` code and built-in tool/permission/workspace configuration. External providers, arbitrary projects and user-defined hooks, shell scripts and external controlling agent systems are dependencies or separately configured extensions, not first-party agent owners.
- Credited operating / distribution surfaces: `src/scootcli/agent.py`, `cli.py`, `repl.py`, `headless.py`, `tools/`, `providers/`, `approvals.py`, `worktree.py`, `hooks.py`, `sessions.py`, `context.py`, `config.py` and model/router choices.
- Adjacent first-party surfaces excluded from ownership: tests, CI/release automation, documentation plans, upstream contributor rules, user-installed global/project hooks, custom external machines or CI controllers and other installed agent products invoked by shell.
- First-party operating / deployment modes considered: interactive REPL, bounded one-shot coding request, JSONL headless mode, read-approval/yolo permission variants, restart/resume, optional worktree for one agent run, model routing and command plan tool. Multiple independent installed processes are not organized into a bundled fleet.
- Recursion level: one scoot coding-agent session as one S1. A human can supervise the deployment, but no first-party higher viable-system recursion is claimed for that relation.
- Reviewed revision: `b6712481f1ba8b1b5694713ee60fb33d1afd5771` (frozen from #898; no live upstream repin).
- Observation date: 2026-10-14.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`Agent.run_turn` repeatedly calls a configured provider with conversation/tool schemas. The model decides whether to call `read_file`, `search`, `edit_file`, `write_file`, `run_shell`, `update_plan` and related built-in tools; the first-party execution layer consults hooks, workspace restrictions and approval policy, executes tools and returns concrete outputs/errors to the next model iteration. A final text response without tool calls completes the bounded loop; interruptions, tool denials, context compaction, model fallbacks, incomplete tool arguments and max-step limits are explicit error/stop paths. The provider is an inference dependency, not a borrowed upstream coding-agent executable.

The CLI and REPL supply interactive approval and project/session UX; the headless protocol exposes structured events and waits for operator approval responses over JSONL. Approval policy provides several modes from ask-always to yolo and special catastrophic-command confirmations. User-configured hooks can intercept events or veto tools, but their external scripts and arbitrary decisions are not first-party VSM-function closure. The opt-in worktree creates an isolated branch for a *single* autonomous run and then asks a human to merge, retain or discard. It protects the operator's working tree but does not itself observe distinct competing S1s or resolve their interference. Plan updates publish a model-written task-local checklist; session store and compaction preserve current context. Auto model routing uses prompt/complexity heuristics or user rules for the current turn, not independent prospective system adaptation.

Primary source: [`README.md`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/README.md); [`DESIGN.md`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/DESIGN.md); [`src/scootcli/agent.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/agent.py); [`src/scootcli/headless.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/headless.py); [`src/scootcli/repl.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/repl.py); [`src/scootcli/worktree.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/worktree.py); [`src/scootcli/approvals.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/approvals.py); [`src/scootcli/hooks.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/hooks.py); [`src/scootcli/tools/update_plan.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/tools/update_plan.py); [`src/scootcli/providers/router.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/providers/router.py).

## Operational model

One model-backed coding S1 holds task-level discretion. Local restrictions, tool approvals, external operator responses and worktree merge choices constrain or accept its actions, but do not establish a separate whole-session portfolio S3 or ultimate identity S5. Its step-by-step plan, headless JSONL events and session checkpoints are tools/results for the same operational unit. No shipped independent reviewer or external-future organizational capability loop is evidenced in this frozen standard distribution.

## S1 — Operations

- State: A
- Function: transform uncertain local coding request into adaptive file/shell/repository work through model-selected actions.
- Disturbance / variety regulated: unknown project content, tool failure, changing code, provider responses, context capacity and observed command/test feedback.
- Decisive decision or feedback right: decide which project-tool action to take next or to stop/answer after each tool observation.
- Decision owner: first-party `Agent` with its externally supplied model inference, not the deterministic tool registry or a separate borrowed coding-agent host.
- Supporting / enforcement mechanisms: provider transports, `run_turn` turn/max-step limits, `_run_tools`, approved tool registry, worktree isolation, hooks, context/session utilities.
- Closure path: operator coding objective + current evidence → model selects tool and parameters → first-party approval, tool execution → observed result/error appended to history → model chooses subsequent step or completion.
- Boundary reachability: packaged CLI and headless entrypoints instantiate the first-party `Agent.run_turn` / tool handlers. This path is runtime source, not a test-only or README future mode.
- Why this is / is not agent-owned: the support machinery cannot select task-specific coding actions when the model's discretionary tool choices are removed.
- Evidence: [`src/scootcli/agent.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/agent.py); [`src/scootcli/tools/__init__.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/tools/__init__.py); [`src/scootcli/tools/run_shell.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/tools/run_shell.py); [`src/scootcli/cli.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/cli.py); [`src/scootcli/headless.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/headless.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: model-reported done or shell test output is not a separately verified claim about correctness.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 interference/conflict attenuation loop in the shipped single-agent deployment.
- Disturbance / variety regulated: overlapping concurrent changes by independently working agents would require coordination if multiple S1s existed; scoot does not instantiate/observe a fleet.
- Decisive decision or feedback right: no shipped decision right over distinct S1s' collisions or oscillation. Isolating one worktree for an operator's later merge does not identify multiple independent task-owning S1s.
- Decision owner: no S2 owner identified; git or human merge choices concern the local user's one agent run.
- Supporting / enforcement mechanisms: single-run optional git worktree, human merge/retain/discard, tool sequence, session storage and shell.
- Closure path: a one-run isolated diff returns for human acceptance; no observed S1-versus-S1 disturbance → first-party attenuation choice → corrective feedback into independent S1 workers.
- Why this is / is not agent-owned: an agent inside an isolated worktree is still a single S1, not a pair of coordinated S1 units.
- Evidence: [`src/scootcli/worktree.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/worktree.py); [`src/scootcli/agent.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/agent.py); [`src/scootcli/repl.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/repl.py); [`README.md`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: if an external orchestrator launches several scoot processes, that must be assessed at a new integrated boundary; none is donated to standard scoot.

### Absence scope

- Surfaces inspected: agent run loop, built-in tools, headless protocol, worktree creation/finish, CLI/REPL and documented operating variants.
- Plausible first-party paths checked: native child agent spawn, task/fleet registry, shared agent messaging, concurrent write collision detection between distinct workers and returned conflict arbitration.
- Why no material first-party path remains: each supported instance runs one model-directed worker; worktree protection ends in operator review, and no native multi-agent interaction/regulation return is wired.

## S3 — Inside-and-now control

- State: —
- Function: no current whole-organization operational regulator separate from managing one coding task.
- Disturbance / variety regulated: competing obligations and capacity of multiple live S1 work cells are absent from the supported product's system boundary.
- Decisive decision or feedback right: the model can update its own current task plan and select tools, and the human may approve shell actions; neither makes whole-current commitments/resources regulation across independent operations.
- Decision owner: one coding model and per-action operator, neither credited whole-organization S3.
- Supporting / enforcement mechanisms: `update_plan`, session status/usage, auto model routing, approval policy, headless event stream and worktree decisions.
- Closure path: plan/approval choices affect a current S1 step, not a whole-current supervisory decision returned across operations.
- Why this is / is not agent-owned: the model's plan is a task-specific strategy, not a fleet/portfolio current-control right.
- Evidence: [`src/scootcli/tools/update_plan.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/tools/update_plan.py); [`src/scootcli/agent.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/agent.py); [`src/scootcli/headless.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/headless.py); [`src/scootcli/providers/router.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/providers/router.py); [`README.md`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/README.md).
- Basis: structural
- Confidence: high
- Caveats: an external parent using headless events could own S3, but such a controller is not a first-party operating mode.

### Absence scope

- Surfaces inspected: coding loop, task-plan tool, REPL, headless events, session status, worktree lifecycle and approvals.
- Plausible first-party paths checked: whole-fleet status visibility, cross-task priority adjudication, control over several current S1 commitments, parent decision/return.
- Why no material first-party path remains: source provides single-session task and approval management, not a first-party management organization with whole-current scope.

## S3* — Complementary audit

- State: —
- Function: no separate complementary evidence reviewer/auditor correcting operational reports or code outputs.
- Disturbance / variety regulated: false completion, defective patches and missed test failures.
- Decisive decision or feedback right: the current worker decides whether to run tests or inspect diffs; a human may judge a worktree diff, but no built-in independent raw-work auditor and corrective return is wired at the declared first-party boundary.
- Decision owner: no first-party S3* owner.
- Supporting / enforcement mechanisms: git worktree diff, ordinary shell test commands, user approvals and hook events.
- Closure path: operator-facing diff and same-agent tool results lack a shipped complementary audit finding → management response → revised S1 regulation cycle.
- Why this is / is not agent-owned: user review of one run's changes is ordinary external approval at this product boundary; arbitrary custom review hooks are user-supplied extensions.
- Evidence: [`src/scootcli/worktree.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/worktree.py); [`src/scootcli/agent.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/agent.py); [`src/scootcli/hooks.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/hooks.py); [`README.md`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/README.md).
- Basis: structural
- Confidence: high
- Caveats: not a statement that a human or external CI cannot review a scoot-produced patch; they are outside this declared supported first-party audit arrangement.

### Absence scope

- Surfaces inspected: code/tool loop, session results, headless output, worktree finish/review, hooks, tools list and supported docs.
- Plausible first-party paths checked: separately instantiated evidence-reading reviewer, independently judged acceptance report, distinct raw-file verification with rejection/repair dispatch.
- Why no material first-party path remains: no shipped reviewer agent or standalone first-party audit return code path appears in the pinned distribution.

## S4 — Outside-and-then intelligence

- State: —
- Function: no built-in environmental future scouting and selected organizational capability adaptation returned to current operation.
- Disturbance / variety regulated: future model/tool availability and project changes are possible environment concerns; built-in model router responds to immediate prompt/provider availability.
- Decisive decision or feedback right: current-turn provider choice and user-authored routing/config/hook changes; no first-party prospective capability investment/options authority.
- Decision owner: configured router/user for immediate model selection, not a prospective organizational intelligence function.
- Supporting / enforcement mechanisms: live provider list, per-turn model heuristic, session compaction, local preferences, optional hooks and project workspace.
- Closure path: provider availability and task words affect this turn's model, while no future opportunity analysis → selected capability change → adoption by continuing agents is implemented.
- Why this is / is not agent-owned: model switch and context management solve current execution limitations rather than building future organizational response capacity.
- Evidence: [`src/scootcli/providers/router.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/providers/router.py); [`src/scootcli/models.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/models.py); [`src/scootcli/context.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/context.py); [`src/scootcli/config.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/config.py); [`README.md`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: operator might script ongoing model/skill upgrades externally; that does not change the bundled result.

### Absence scope

- Surfaces inspected: provider/model routing and fallbacks, context compaction, preferences, hooks, project config, CLI session lifecycle and design reference.
- Plausible first-party paths checked: external/future opportunity sensing, alternate capability option building, accepted adaptation roadmap/selection, returned long-lived organizational change.
- Why no material first-party path remains: the frozen shipped paths respond to immediate prompts or operator choices; neither first-party prospective strategic adaptation nor its S3 return is wired.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate organizational identity/policy decision with legitimate return to subsequent operation.
- Disturbance / variety regulated: dangerous shell commands, path scope, user permissions and machine-wide hook trust are operational risk constraints rather than ultimate policy/identity disputes.
- Decisive decision or feedback right: operator approves or denies a tool, opts into yolo, and authorizes local/global hooks; no constitutional authority channel to resolve system-purpose dispute.
- Decision owner: human/operator for permission preferences; deterministic policy code for enforcement, not an S5 identity-governance owner.
- Supporting / enforcement mechanisms: `approvals.py`, `hooks.py`, workspace restrictions, headless `approve` message and configured default policy.
- Closure path: approval/denial changes a tool action or trust decision; no ultimate-policy proposal → legitimate parent decision → durable returned identity rule regulating subsequent system mission.
- Why this is / is not agent-owned: the model does not choose the legitimate ultimate purpose via a tool approval; approval policy is a bounded security rule selected outside that model.
- Evidence: [`src/scootcli/approvals.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/approvals.py); [`src/scootcli/hooks.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/hooks.py); [`src/scootcli/headless.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/headless.py); [`src/scootcli/config.py`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/src/scootcli/config.py); [`README.md`](https://github.com/sergenes/scootcli/blob/b6712481f1ba8b1b5694713ee60fb33d1afd5771/README.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: operator authority to choose provider, scope and tool rights does not automatically establish parent S5.

### Absence scope

- Surfaces inspected: permissions, hook trust, headless approval protocol, project configuration, CLI directives and provider routing.
- Plausible first-party paths checked: system identity issue/proposal, S3-S4 policy disagreement escalation, legitimate parent adjudication and durable returned constitutional governance.
- Why no material first-party path remains: mechanisms authorize individual tool calls or local preferences but do not enact an ultimate identity-level VSM S5 loop.

## Distributed OSS parent arrangement

Repository maintainers and downstream users are not wired together as the installed scoot coding-session's S5 parent or whole-system control organization. The source distribution may be used by different human/deployment parents, but no qualifying first-party parent governed mode is evidenced.

## Self-hosted and non-human modes

Scoot can run locally with Ollama or remote model APIs; headless mode requires an external controller to answer approval messages. Its fixed approval modes and YOLO operation preserve model ownership of S1 but do not create first-party function-specific parent modes S3/S4/S5. No `(P)` state claimed.

## Recursion

A worktree, a restored session or a headless controller process does not by itself establish a nested viable system. Single-model coding S1 is the operational unit in the bounded installed harness.

## Variety and escalation

The model handles task novelty through model/tool selection and observation; approval policies, denylist, context compaction, fallback providers and worktree isolation attenuate tool/security/availability risks. Aborted/dangerous calls can reach the human as operational authorization, not necessarily as algedonic or S5 identity-level escalation.

## Evidence gaps

- This is pinned source-first structural evidence, not a live model-backed execution or benchmark result.
- First-party hooks, shell programs and headless API enable externally composed supervisors, but neither an arbitrary third-party controller nor potential extensions can be borrowed into the assessed standard distribution.
