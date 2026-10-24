---
harness_id: live-swe-agent
project_name: Live-SWE-agent
repository: https://github.com/OpenAutoCoder/live-swe-agent
review_ref: 8d7dd8634580d1e09320b4c27d70380bc9ae74a8
reviewed_at: 2026-10-25
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

# Live-SWE-agent

## Review boundary

- System in focus: The **frozen public GitHub repository's first-party deliverable**: three `config/*.yaml` files specifying prompts and execution settings for external `mini-swe-agent`, associated config notes, README, images and license. The separate installed upstream `mini-swe-agent` Python runtime is not an implementation in this repository.
- Purpose and identity: Distribute model prompts and task rules so an independently installed `mini-swe-agent` can perform software-engineering issue work and, according to the maintainers, create ad hoc helper tools while executing tasks.
- Relevant environment: Consumer codebases, issue descriptions, model providers, external `mini` runner/shell environments, benchmark infrastructures and users; benchmark datasets and historical trajectories are not packaged as active autonomous control code here.
- Standard-distribution boundary: `README.md` instructs the user to **install mini-swe-agent first** and invoke `mini --config config/livesweagent.yaml`. All three YAMLs provide `agent.system_template`, `instance_template`, action/format templates, model/env options and budgets consumed by that external runtime. The current repository ships **no** model-call loop, tool runner, controller, agent process, plugin hook or executable source that implements a distinct local feedback engine.
- Credited operating / distribution surfaces: [README setup and attribution](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md), [normal config](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent.yaml), [SWE-bench config](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent_swebench.yaml), [SWE-bench Pro config](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent_swebench_pro.yaml), [config notes](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/README.md).
- Adjacent first-party surfaces excluded from ownership: README paper/leaderboard/benchmark claims, screenshots, release-associated historical trajectories/patches not in this frozen tree, contributor/research organization, and any separately acquired `mini-swe-agent` Python executor, model provider, shell tool runtime, testbed or user-created helper program. The YAML is first-party config, but the adjacent framework's working agent loop is not first-party implementation.
- First-party operating / deployment modes considered: Normal `livesweagent.yaml` for interactive issue work; two specific SWE-bench benchmark prompt/environment variants; shell-command format enforcement, step/cost limits and prompt-driven helper-tool creation. No live model, benchmark, shell agent or provider invocation was performed.
- Recursion level: One configured issue-solving session of a separately installed upstream host. The assessed repository alone is a configuration overlay without autonomous operational units; no repo-owned parent organizational layer is created by naming it an agent.
- Reviewed revision: `8d7dd8634580d1e09320b4c27d70380bc9ae74a8`, frozen in [intake #2024](https://github.com/opensiro/vsm-harness-index/issues/2024) and [batch control #2025](https://github.com/opensiro/vsm-harness-index/issues/2025).
- Observation date: 2026-10-25.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The repository contains **eight tracked files**: README, config notes, three YAML configs, two images and the license; there is no `src/` implementation, executable entrypoint, package manifest or independent runtime test suite. The normal YAML defines assistant and instance prompt templates, instructs the model to issue one fenced shell command, explains observation formatting and suggests writing issue-scoped helper scripts. The benchmark variants change prompts, environment and budgets. The README explicitly says the project was built **on top of `mini-swe-agent` with minimal modifications** and starts a third-party `mini` executable with a config path. Its reported self-evolution and benchmark results are not proof of a first-party VSM control path in this pinned source. [README setup](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L68-L95), [normal prompts and limits](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent.yaml), [benchmark config](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent_swebench_pro.yaml).

## Operational model

The user supplies an independent `mini-swe-agent` install, shell execution environment, credentials and issue task. The repo's YAML is passed to that external runner and provides prompting/output instructions. The external agent/model generates actions and receives shell observations through **the mini-swe-agent runner**, not through an agentic engine authored in this source. Prompt suggestions to create a reusable script operate inside one issue/task; they neither establish a first-party self-modifying runtime nor an organizational outside-and-then adaptation loop. Because the assessed first-party distribution supplies only instructions/configuration and no owned operational agent decision/execution loop, the canonical outcome is **`excluded-no-agentic-vsm`**, regardless of the quality of external model performance.

## S1 — Operations

- State: —
- Function: Issue-solving agent operation is described but not implemented as a first-party autonomous operational unit in this source tree.
- Disturbance / variety regulated: A real code issue requires interpreting observations and choosing file edits, tests and next shell actions; those decisions are made by the external `mini` runtime/model when installed.
- Decisive decision or feedback right: Choosing the next shell command after an observation is not owned by any shipped executable in this repository.
- Decision owner: Separately installed `mini-swe-agent` with external model, not this repo's YAML authoring/configuration layer.
- Supporting / enforcement mechanisms: Prompt templates, one-command format rule, action/observation and format-error templates, step/cost limits passed to external runner.
- Closure path: User passes YAML to `mini` → external runner presents prompt and executes model-selected actions → external runner returns observations. Only configuration is first-party; no local first-party agent loop closes the path.
- Why this is / is not agent-owned: A model may act autonomously in the composed *external* host, but removing that host leaves static YAML without operational decisions. A prompt advising tool creation does not itself run or own those tools.
- Evidence: [explicit third-party install and command](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L68-L95); [first-party config-only action template](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent.yaml).
- Basis: Explicit maintainer installation boundary plus structural frozen-tree review.
- Confidence: High for this exact first-party source boundary.
- Caveats: The broader externally composed Live-SWE-agent *experiment* can run model-backed work, but assigning that independent mini-swe-agent S1 to this config-only repository would exceed the declared evidence/ownership boundary.

### Absence scope

- Surfaces inspected: README setup, all three runtime/benchmark YAML configs, config notes, full tracked file tree and Git revision.
- Plausible first-party paths checked: `agent.system_template`, `instance_template`, `action_observation_template`, `format_error_template`, runtime option fields and prompt-specified helper tool creation.
- Why no material first-party path remains: Every agent decision/execution path depends on the separate `mini` executable/model and no runnable first-party agent/controller/adapter feedback engine is packaged.

## S2 — Coordination

- State: —
- Function: No first-party attenuation of interference among distinct concurrently operating S1 units is shipped.
- Disturbance / variety regulated: Potential file edit collisions between coding agents could exist externally; the configs define a *single* issue-solving shell actor, not collaborating S1 work cells.
- Decisive decision or feedback right: No coordination authority over an inter-agent conflict, reservation or arbitration feedback is described or implemented.
- Decision owner: None within this first-party boundary; any external mini-swe-agent parallelism is uninspected.
- Supporting / enforcement mechanisms: A single-action-per-model-response formatting rule and shell output truncation template.
- Closure path: Formatting/observation rules regulate one external actor's commands, not a conflict signal returned into another first-party S1.
- Why this is / is not agent-owned: Commands in sequence are one actor's workflow, not multiple S1 units resolving interference.
- Evidence: [single action config](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent.yaml); [repo setup](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L68-L95).
- Basis: Bounded absence of S2-specific shipped path.
- Confidence: High.
- Caveats: The README's software-agent label cannot substitute for distinct S1-conflict/feedback evidence.

### Absence scope

- Surfaces inspected: All YAMLs and `config/README.md` including benchmark execution variants.
- Plausible first-party paths checked: Shell-command serialization, prompt step ordering, feedback templates, benchmark environment settings.
- Why no material first-party path remains: These are sequential instructions for a single external agent; there is no set of owned sibling S1 units, concrete inter-S1 disturbance, or attenuation/return channel.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current coordination of a population of S1 work cells is shipped.
- Disturbance / variety regulated: Cross-agent commitments, resources and priorities are not represented; the config only constrains one issue-solving run.
- Decisive decision or feedback right: No first-party manager sees multiple active operations and can revise commitments/allocations.
- Decision owner: Operator selects model/task/budgets externally; `mini` runs its own loop.
- Supporting / enforcement mechanisms: `step_limit`, `cost_limit`, mode, environment timeouts, step formatting.
- Closure path: Budget/format enforcement is consumed by the external runner; no first-party current-control judgment returns to a portfolio of agents.
- Why this is / is not agent-owned: Hard-coded limits enforce a developer/user choice; they do not transfer a discretionary S3 right to the YAML.
- Evidence: [normal config limits](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent.yaml); [benchmark mode limits](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent_swebench_pro.yaml).
- Basis: Bounded absence.
- Confidence: High.
- Caveats: The host's undisclosed internal accounting may manage *its* work; not credited here.

### Absence scope

- Surfaces inspected: Prompt and action templates, limits, model/environment settings, README install instructions.
- Plausible first-party paths checked: Single-actor budget control, external runner error reporting, instructions for helper-tool creation and benchmark configuration.
- Why no material first-party path remains: None supplies a whole-current operational view plus owned decisions over shared team resources, commitments or accountability.

## S3* — Complementary audit

- State: —
- Function: No first-party complementary and sufficiently independent audit channel checks ordinary operation claims.
- Disturbance / variety regulated: Agents may claim a code change fixes an issue, but instructions to test their own patch are routine production verification.
- Decisive decision or feedback right: No separate independent audit judgment or route back to whole-current control is present.
- Decision owner: Same externally hosted solving actor would invoke tests and interpret them under prompt guidance.
- Supporting / enforcement mechanisms: Prompt-recommended reproduce/fix/test steps, benchmark screenshots and historical result links.
- Closure path: Ordinary tool-test feedback enters the external agent's next task step; no independent first-party audit correction loop.
- Why this is / is not agent-owned: Advice to run tests or verify edge cases is important but cannot substitute for independent evidence access and separate audit ownership.
- Evidence: [recommended workflow](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent.yaml); [benchmark artifacts context](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L96-L117).
- Basis: Bounded absence.
- Confidence: High.
- Caveats: Third-party benchmark evaluators are adjacent research infrastructure, not installed first-party complementary S3*.

### Absence scope

- Surfaces inspected: Issue-fix/testing prompt steps, all benchmark config prompts, README leaderboard/artifact documentation, repository file tree.
- Plausible first-party paths checked: Model-run self-verification instructions, SWE-bench ground truth results, format-error retry and dataset scoring.
- Why no material first-party path remains: The only runtime feedback is ordinary task checking by an external actor; benchmark evaluation lies outside the assessed standard distribution, with no independent corrective path to current multi-agent S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party closed external/prospective capability-adaptation loop is supplied in the frozen repository.
- Disturbance / variety regulated: Future model and codebase changes may require new strategies, but current config asks the external agent to solve the *current* issue.
- Decisive decision or feedback right: No first-party owner chooses a future-oriented adaptation option and returns it into the current harness capability.
- Decision owner: A separately hosted LLM may choose to write a helper script while working on an issue; user/developer can modify YAML later. Neither is a shipped prospective S4 owner/return path here.
- Supporting / enforcement mechanisms: Prompt phrases encouraging tool creation and reflection on previous trajectory, shell-command examples, external benchmark research claims.
- Closure path: Optional issue-specific helper code might be used later in *that task* via external shell operations; no environmental intelligence → strategic option → adopted capability path within this repository.
- Why this is / is not agent-owned: The paper's `self-evolving` label and prompt-guided tool creation are not evidence of an outside-and-then regulator with a future horizon and returned operational adoption.
- Evidence: [prompt helper-tool instructions](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent.yaml); [README self-evolution claim](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L20-L32).
- Basis: Bounded negative despite positive-sounding maintainer claim.
- Confidence: High at frozen code boundary; no empirical negative claim about the separately installed system.
- Caveats: The external mini-swe-agent organization could be assessed as a separate system with its own pinned source, but that is not this repository.

### Absence scope

- Surfaces inspected: All prompt templates, helper creation instructions, normal/benchmark runtime settings, README descriptions and artifact references.
- Plausible first-party paths checked: Creating scripts during current issue, reflecting on prior commands, user editing YAML, changing model settings, learning from historical benchmark releases.
- Why no material first-party path remains: These are task-level work or manual research/configuration; no first-party future-environment model, adaptation-options decision right and subsequent capability return is wired.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/policy decision with legitimate authoritative return is present.
- Disturbance / variety regulated: Unsafe shell commands, limited testbed scope and output formatting are constrained by prompts and limits, not by an identity-level governance system.
- Decisive decision or feedback right: Config rules select task formatting and file-edit boundaries. No ultimate-policy question is escalated, resolved and bound into continued organization operation.
- Decision owner: External `mini` host and its operator govern their own environment/permissions; this repository declares prompt constraints but no authoritative policy decision loop.
- Supporting / enforcement mechanisms: System/instance prompts, format error templates, run mode, step/cost/time budgets, benchmark restriction text.
- Closure path: A model action passes through external formatting/error checks or reaches external shell; no first-party identity dispute → legitimate authority → returned binding policy loop exists.
- Why this is / is not agent-owned: Stating boundaries in a system prompt does not make that prompt an ultimate-policy deliberator; running a benchmark within prescribed folders is ordinary permission scoping.
- Evidence: [normal YAML instructions](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent.yaml); [testbed rules](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/config/livesweagent_swebench.yaml).
- Basis: Bounded negative first-party review.
- Confidence: High.
- Caveats: Maintainer governance and host provider policy are separate recursive authorities, not first-party Live-SWE configuration-level S5(P).

### Absence scope

- Surfaces inspected: System/instance prompts, action/format controls, budget/mode/model/env config and README governance attribution.
- Plausible first-party paths checked: Prompt-derived policy, approval by human operator, shell permissions, benchmark file-edit restrictions and maintainer decisions.
- Why no material first-party path remains: These paths constrain operation or sit outside the installed first-party boundary; none implements legitimate identity-level decision and return-to-operation authority.

## Distributed OSS parent arrangement

The repo's research authors and external mini-swe-agent maintainers are not one installed operational parent. Contributor paper, benchmark and release governance cannot be used to manufacture S3/S4/S5 parent ownership for a consumer's independent mini session.

## Self-hosted and non-human modes

Users may self-install `mini-swe-agent` and configure a local or remote provider. Those self-hosted modes do not introduce executable first-party agency into this YAML source. The behavior of the separately installed mini framework should be assessed under its *own* frozen repository, not assumed here.

## Recursion

One configured shell agent session is not a hierarchy of independently viable S1 work cells within this repository. Benchmark variants are alternative setups, not recursively organized operations.

## Variety and escalation

The external model/runner receives changing shell observations; YAML templates limit message shape, output length and declared task constraints. A failed command or format error is normal task feedback, not evidence of an exceptional algedonic signal reaching a first-party independent authority. The source has no metasystem intervention/return channel.

## Evidence gaps

- The actual `mini-swe-agent` runtime is an independently installed third-party prerequisite and is intentionally excluded from first-party S1 ownership. No inference is drawn about the full composed system's empirical SWE-bench results, provider efficacy or runtime self-modification.
- The only checked revision contains text/config/assets rather than a custom executable. Source coverage for the first-party **frozen distribution** is complete enough for bounded `—` findings; it does not prove impossibility of a different deployed architecture.
- No live model, shell-acting agent or benchmark was executed; no independent effectiveness claim is made.
