---
harness_id: hip-agent
project_name: hip-agent
repository: https://github.com/changjonathanc/hip-agent
review_ref: 0c022719ebcf4894f932c1ab5d2c309e06528c2f
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# hip-agent

## Review boundary

- System in focus: The executable hip-agent Python harness, its Codex transport/rollout adapter and three shipped context/cwd plugins.
- Purpose and identity: Complete coding or shell tasks using a prompt-visible minimal harness that can be inspected and modified.
- Relevant environment: User task, local filesystem and subprocesses, images, provider errors and context limits.
- Standard-distribution boundary: agent and codex.py execute the model/tool loop directly; the existing Codex login supplies transport credentials, not the Codex CLI tool loop. Included example plugins are concrete context/cwd integrations, not independent reviewers.
- Credited operating / distribution surfaces: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Adjacent first-party surfaces excluded from ownership: External Codex backend/login implementation, third-party skills/plugins and user-created children; MIT license/maintainer development activity supplies provenance rather than runtime governance. No test or CI organization is shipped.
- First-party operating / deployment modes considered: Fresh CLI/stdin task; AGENT_RESUME rollout; optional environment, agentsmd and cwd plugins; model-initiated child invocation through sh.
- Recursion level: One task-executing harness; multiple calls, processes or sessions do not establish recursive viability.
- Reviewed revision: `0c022719ebcf4894f932c1ab5d2c309e06528c2f`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

agent constructs tool schemas for sh and view_image, loads instructions and plugin skills, restores a Codex-format rollout, and calls codex.respond repeatedly. Each emitted function call passes PreToolUse, executes the tool, passes PostToolUse, appends function_call_output and enters the next model request. A Stop hook can refuse completion by injecting feedback. codex.py implements HTTP/SSE, retries, rollout persistence and server compaction. Child agents are ordinary shell-launched invocations with a fresh conversation and inherited environment; there is no packaged team scheduler or separate organizational control agent.

Primary implementation: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).

## Operational model

One model-backed task loop is S1. It autonomously chooses shell commands/image inspections, observes their real outputs and finishes or iterates. External inference is a dependency; the repository owns invocation, dispatch and result-return. The operator chooses initial task and configuration; hooks execute preselected extension rules. Neither unrestricted shell capability nor the prompt inviting source edits establishes a higher VSM function.

## S1 — Operations

- State: A
- Function: Produce a task outcome through repeated model-selected shell/image actions.
- Disturbance / variety regulated: Workspace changes, command results, malformed/failed actions and visual evidence.
- Decisive decision or feedback right: Select the next sh/view_image call, revise after the result, or emit the final reply.
- Decision owner: The model-backed task actor in agent.main.
- Supporting / enforcement mechanisms: codex.py HTTP/SSE and rollout persistence, shell process timeout, image validation, pre/post hooks and compaction.
- Closure path: Function outputs are appended by call_id and become the next respond input; Stop-hook feedback may restart the same operational loop.
- Boundary reachability: The documented ./agent entry executes main directly and uses the repository-owned dispatcher rather than invoking a Codex CLI agent loop.
- Why this is / is not agent-owned: Removing the model leaves transport and fixed hooks, but no discretionary task solution or next-action selection.
- Evidence: [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

## S2 — Coordination

- State: —
- Function: No S2-specific inter-unit stabilization path.
- Disturbance / variety regulated: Potential child-agent overlap and shared workspace mutations.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Sequential dispatcher, environment inheritance and per-conversation cwd files.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Shell spawning is generic delegation; the shipped harness has no conflict-aware inter-S1 coordination response or return into competing workers. The cwd plugin scopes command context per conversation rather than negotiating shared work.
- Evidence: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Plausible first-party paths checked: Child invocation through sh, inherited CHILD_ENV, fresh conversations, sequential per-response tool dispatch and cwd plugin.
- Why no material first-party path remains: Shell spawning is generic delegation; the shipped harness has no conflict-aware inter-S1 coordination response or return into competing workers. The cwd plugin scopes command context per conversation rather than negotiating shared work.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system inside-and-now regulation established.
- Disturbance / variety regulated: Current task completion, output limits, timeouts and resource use.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: Operator/developer select fixed constraints; the task model owns local operations.
- Supporting / enforcement mechanisms: Timeouts, compaction, rollout recovery and hook blocking.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: The model regulates one task and runtime enforces fixed limits. No whole-system commitment/resource view plus S3 decision/return, autonomous or parent-owned, is shipped.
- Evidence: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Plausible first-party paths checked: Stop-hook continuation, subprocess timeout, transcript resume, compaction thresholds and plugin configuration.
- Why no material first-party path remains: The model regulates one task and runtime enforces fixed limits. No whole-system commitment/resource view plus S3 decision/return, autonomous or parent-owned, is shipped.

## S3* — Complementary audit

- State: —
- Function: No materially independent complementary audit.
- Disturbance / variety regulated: Incorrect completion claims or tool results.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Hooks, image/shell observations and rollout traces.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Stop feedback is a generic extension point; supplied plugins only add environment/instructions or cwd. No audit-specific independent judgment, complementary access and corrective authority are composed. Task self-checking remains ordinary operations.
- Evidence: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Plausible first-party paths checked: Stop/PostToolUse hook return path, view_image, shell-based checking, and all three supplied plugins.
- Why no material first-party path remains: Stop feedback is a generic extension point; supplied plugins only add environment/instructions or cwd. No audit-specific independent judgment, complementary access and corrective authority are composed. Task self-checking remains ordinary operations.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation closure.
- Disturbance / variety regulated: Changing environment and future task capability.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Source self-inspection instruction, skill paths and summary persistence.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Permission to edit source or load a skill does not supply an outside-and-then adaptation organization. No shipped external/future sensing-to-option-to-current-capability decision loop, including a parent mode, is evidenced.
- Evidence: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Plausible first-party paths checked: Source-visible harness edit prompt, skill discovery, inherited configuration, resume and server compaction.
- Why no material first-party path remains: Permission to edit source or load a skill does not supply an outside-and-then adaptation organization. No shipped external/future sensing-to-option-to-current-capability decision loop, including a parent mode, is evidenced.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy decision-and-return organization.
- Disturbance / variety regulated: Changes to purpose, instruction authority and execution limits.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: Operator/developer provide initial task/configuration; no first-party S5 process is supplied.
- Supporting / enforcement mechanisms: Static prompt, nearest AGENTS.md and hook policy responses.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Operator-authored instructions and ordinary action vetoes bound a task. They neither route an identity/ultimate-policy issue to legitimate authority nor return an authoritative identity decision to govern subsequent operation.
- Evidence: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/README.md); [agent](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/agent); [codex.py](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/codex.py); [plugins/agentsmd/hooks/agentsmd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/agentsmd/hooks/agentsmd); [plugins/cwd/hooks/cwd](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/cwd/hooks/cwd); [plugins/environment/hooks/context](https://github.com/changjonathanc/hip-agent/blob/0c022719ebcf4894f932c1ab5d2c309e06528c2f/plugins/environment/hooks/context).
- Plausible first-party paths checked: AGENT_INSTRUCTIONS_FILE, AGENTS.md context plugin, tool-hook denial, task input and Stop feedback.
- Why no material first-party path remains: Operator-authored instructions and ordinary action vetoes bound a task. They neither route an identity/ultimate-policy issue to legitimate authority nor return an authoritative identity decision to govern subsequent operation.

## Distributed OSS parent arrangement

The upstream maintainer and contributors govern repository development. That adjacent organization is not a runtime parent mode of the assessed task harness. No function-specific returned organization-level S3/S4/S5 decision is credited merely from contributor activity.

## Self-hosted and non-human modes

Self-hosted execution uses operator privileges and existing provider access. Configurable instructions, hook denial and Stop feedback constrain ordinary work. No supported identity referral, prospective capability-adaptation protocol or whole-system parent supervisor is evidenced.

## Recursion

No complete recursive viable unit is established. Local tool execution, process spawning and durable session state alone do not demonstrate a child identity, environment and metasystem.

## Variety and escalation

Process-group timeouts, truncated outputs, interrupted-call repair, provider exceptions and tool failure are returned or terminate the run. A blocking hook can require more work. These local recovery/denial channels are not an independent audit or established algedonic authority channel.

## Evidence gaps

This is pinned-source analysis. No real model, paid provider, external worker or production workload was executed. Operational success, reliability and downstream effectiveness are unmeasured. The bounded negative judgments concern the declared distribution, not hypothetical future extensions.
