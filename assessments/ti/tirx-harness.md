---
harness_id: tirx-harness
project_name: TIRx Harness
repository: https://github.com/mlc-ai/TIRx-harness
review_ref: 370b7461a4424edbd22238f6e6882b2a71e0ad5d
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TIRx Harness

**Proposed disposition:** `excluded-no-agentic-vsm`. TIRx is a substantive open-source GPU programming/compilation and benchmark *tool harness* useful to agents, not a first-party autonomous agent-runner distribution at this revision. The distinction concerns the Index's autonomous agent-harness inclusion boundary, not its engineering merit.

## Review boundary

- System in focus: installed TIRx compiler analysis and GPU benchmark services, packaged skills and the `evolve init` workspace-preparation CLI.
- Purpose and identity: give independently installed coding agents a stable compiler/kernel authoring language, diagnostic tools, GPU feedback and workload constraints.
- Relevant environment: GPU architectures, kernel implementations, correctness/performance requirements, CUDA/TIRx IR, isolated worktrees and externally operated Codex, Claude Code or Humanize agents.
- Standard-distribution boundary: published `tirx-harness` Python tooling and `evolution` run-preparation workflow, with first-party rules, worktrees, benchmark adapter, optional kcoral backend; launching/running an agent is expressly a separate user step.
- Credited operating / distribution surfaces: `tools/src/tirx_harness/`, `evolution/cli.py`, `evolution/preparation/`, generated prompt/worktree/hook modules, benchmark adapter and optional kcoral diagnostics.
- Adjacent first-party surfaces excluded from ownership: imported benchmark workloads, library development tests, docs/book examples, native TIRx engine and kernel packages as independent operations; externally installed model-driven Codex, Claude Code and Humanize executable agent loops.
- First-party operating / deployment modes considered: direct package with installed skills, `evolve init` with local GPU, remote-kcoral run preparation, Codex/Claude worktree hooks, optional separate Humanize multi-agent launch.
- Recursion level: one prepared workload and its independently launched agent run; first-party TIRx does not itself own the agent's operational decision loop.
- Reviewed revision: `370b7461a4424edbd22238f6e6882b2a71e0ad5d`.
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

TIRx exposes compiler tools, synchronization and numeric checkers, kernel-inspection/benchmark APIs and transferable agent skills. `tirx-harness skills install` copies skills into a separate agent's discovery directory. `evolution/cli.py` explicitly describes `evolve init` as **setup-only**: it writes task prompts and manifests, creates a worktree and environment, installs configuration/guards/skills for Codex or Claude, but delegates actual decision-making and session ownership to that external agent. The documented next step is `cd` into the generated worktree and manually invoke `codex`, `claude`, or an independently installed `hmz exec` multi-agent orchestrator. Benchmark commands return measurements and pass/fail results, not model-selected subsequent actions. [README architecture](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/README.md), [setup-only code](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/cli.py), [run preparation/launch instructions](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/docs/optimization-runs.md).

## Operational model

In a completed GPU optimization run, an **external** autonomous coding agent can use TIRx diagnostics to choose and revise kernel implementations. Removing that external agent while retaining all shipped TIRx tooling leaves a well-defined compiler-analysis service, workload scaffold and scoring infrastructure, but not a first-party autonomous goal→decision→action→feedback agent unit. TIRx's correctness gates and process hooks enforce rules on external agents, and optional Humanize may coordinate multiple independently provisioned agents; neither makes TIRx itself the owner of an agentic operational organization.

## S1 — Operations

- State: —
- Function: the first-party distribution has no autonomous operational decision-making agent unit; it provides compiler/diagnostic operations to externally supplied agents.
- Disturbance / variety regulated: varying kernel workloads, device behavior and correctness/performance are addressed by deterministic compiler, inspection and benchmark functions.
- Decisive decision or feedback right: selection of the next candidate kernel/code edit or tool invocation stays with externally launched Codex/Claude/Humanize, not a shipped TIRx agent runtime.
- Decision owner: external user-selected coding agent; TIRx owns deterministic preparation, tool execution and scoring, not model-backed operational choices.
- Supporting / enforcement mechanisms: skills, generated prompts, worktree isolation, process/forbidden-path hooks, TIRx-lite, NumSim/synccheck, benchmark adapter and kcoral GPU server.
- Closure path: user executes setup and launches third-party agent → agent consults TIRx tool results → agent selects next iteration; without that separate executable the first-party package cannot close this autonomous work cycle.
- Why this is / is not agent-owned: the supported execution model explicitly identifies the agent as a separately installed component with its own runtime and durable progress; no first-party model/tool loop is packaged or started.
- Evidence: [direct quickstart starts existing agent](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/docs/quick-start.md), [separate Codex/Claude/Humanize launch](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/docs/optimization-runs.md), [setup-only ownership comment](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/cli.py), [first-party toolset responsibilities](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/README.md).
- Basis: explicit documentation and structural boundary analysis.
- Confidence: high.
- Caveats: TIRx is genuinely agent-oriented and a capable substrate for third-party agents; `S1=—` applies to its assessed first-party autonomous-harness boundary, not the broader composed ecosystem.

### Absence scope

- Surfaces inspected: package/skills entrypoint, `evolution` CLI, worktree/preparation modules, Codex and Claude hook installers, benchmark adapter, README, quickstart and run instructions.
- Plausible first-party paths checked: direct skills-install workflow, `evolve init`, local and remote GPU benchmark invocation, generated prompt/hook instructions and separate Humanize orchestration.
- Why no material first-party path remains: all supported paths expressly prepare or serve *other* agent runtimes; TIRx does not instantiate and govern an internally model-driven operational loop or autonomous S1 work cell.

## S2 — Coordination

- State: —
- Function: no owned inter-S1 conflict damping in a first-party autonomous organization can be attributed at this recursion.
- Disturbance / variety regulated: multiple GPU optimizers can interfere via shared resources or competing candidate writes, but the option for two agents is provided by separately installed Humanize.
- Decisive decision or feedback right: external Humanize flow selects concurrent agent coordination; TIRx setup only prepares a common worktree and enforces predefined constraints.
- Decision owner: external agent/orchestrator and user, not a first-party TIRx S2 decision owner.
- Supporting / enforcement mechanisms: prepared run worktrees, `flowverse.yaml`, allowed source paths, per-candidate frontier and benchmark APIs.
- Closure path: separate Humanize orchestration may feed choices to two agents, but TIRx does not itself observe, adjudicate and return inter-agent conflict decisions.
- Why this is / is not agent-owned: worktree preparation and static resource rules are not a TIRx-owned first-party interference/attenuation loop.
- Evidence: [Humanize explicitly external](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/README.md), [separate orchestrator command](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/docs/optimization-runs.md).
- Basis: bounded negative.
- Confidence: high.
- Caveats: concrete external multi-agent coordination can be useful; it is excluded from first-party ownership.

### Absence scope

- Surfaces inspected: `evolution/README.md`, launcher instructions, `flowverse.yaml`, worktree/guard installers and candidate frontier management.
- Plausible first-party paths checked: shared worktree, independent candidates/frontier, two-agent Humanize configuration, GPU server and hooks.
- Why no material first-party path remains: none owns the specific cross-S1 disturbance judgment and returned adjustment; the only two-agent coordinator is externally installed.

## S3 — Inside-and-now control

- State: —
- Function: no owned whole-system current supervisor regulates the resource and commitment portfolio of first-party S1 units.
- Disturbance / variety regulated: GPU budgets, run timeout and correctness fail are handled by predefined workload contracts or tools.
- Decisive decision or feedback right: user selects task/GPU and policy; benchmarks report fixed results, without discretionary current-system intervention into agent commitments.
- Decision owner: external user/agent for run choices, deterministic benchmark and guard code for rule enforcement; no first-party S3 owner.
- Supporting / enforcement mechanisms: task declaration, benchmark timeout, isolated worktrees and banned-path process guard.
- Closure path: benchmark output becomes a tool result for external agent; no first-party whole-current view and supervisory decision changes an agent fleet.
- Why this is / is not agent-owned: enforcement of a fixed scoring policy is not ownership of a current operations-management decision.
- Evidence: [task/workload and guard responsibilities](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/README.md), [run contracts and result interpretation](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/docs/optimization-runs.md).
- Basis: bounded negative.
- Confidence: high.
- Caveats: human lab operators can supervise GPU workloads outside this distribution.

### Absence scope

- Surfaces inspected: setup CLI, scoring adapter, run manifests, remote kcoral integration, hook constraints and run docs.
- Plausible first-party paths checked: GPU selection, benchmark pass/fail, timeout controls, worktree isolation, multi-agent external mode and operator tasks.
- Why no material first-party path remains: static constraints and result reports lack discretionary whole-system current-control authority and a returned management decision.

## S3* — Complementary audit

- State: —
- Function: correctness checks are real and may contradict candidate claims, but no complementary agent-organization audit with independent correction closure belongs to a TIRx-owned operational S1.
- Disturbance / variety regulated: invalid GPU kernels and misleading performance claims are tested against fixed workload conditions.
- Decisive decision or feedback right: deterministic benchmark judges kernel correctness and speed; external agent/human interprets results and chooses rework.
- Decision owner: benchmark/test program for validation, external agent/operator for operational response; no first-party complementary audit authority over a TIRx agent workforce.
- Supporting / enforcement mechanisms: NumSim, synccheck/racecheck, baseline tests, kcoral timing reports and frontier index.
- Closure path: test evidence is returned to externally launched optimizer as an ordinary evaluation result, not to an independent in-boundary S3* owner with corrective supervision.
- Why this is / is not agent-owned: a separate benchmark implementation is distinguishable from model narration, but in the declared agent optimization procedure it is routine S1 feedback and no first-party S3* corrective loop is shipped.
- Evidence: [benchmark result/verification guidance](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/docs/optimization-runs.md), [benchmark adapter](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/benchmark/adapter.py), [tool checker sources](https://github.com/mlc-ai/TIRx-harness/tree/370b7461a4424edbd22238f6e6882b2a71e0ad5d/tools/src/tirx_harness).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: external auditors can reuse powerful deterministic checks; that is not an S3* owned by the present first-party system.

### Absence scope

- Surfaces inspected: correctness/performance adapters, remote GPU checks, direct compiler analysis, run docs and source agent launch boundary.
- Plausible first-party paths checked: independent correctness verdicts, separate GPU host, frontier ranking and generated agent benchmark instructions.
- Why no material first-party path remains: checks are ordinary task-validation services for separate agents without a first-party independent operational audit judgment and corrective return path at the declared system level.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/prospective adaptation authority with return into current agent-harness capability is established.
- Disturbance / variety regulated: hardware ISA, compiler implementation and future GPU performance developments change the domain, but tools only inspect specified current artifacts.
- Decisive decision or feedback right: externally selected agent can research new kernels; TIRx packages reference manuals/skills and fixed workload contracts, not a strategic adaptation loop.
- Decision owner: external agent or developer for prospective research, not TIRx operational S4.
- Supporting / enforcement mechanisms: reference wiki fetcher, task rule templates, compiler inspection and benchmark results.
- Closure path: references and measurements guide a running external agent's current optimization; no first-party future-environment hypothesis → option → capability adjustment via S3 is wired.
- Why this is / is not agent-owned: a knowledge base and iterative performance feedback are not, alone, organizational S4.
- Evidence: [wiki/tool preparation](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/preparation/live_references.py), [setup-only run contract](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/README.md).
- Basis: bounded negative.
- Confidence: high.
- Caveats: researchers may derive future compiler changes from outputs in a different organization.

### Absence scope

- Surfaces inspected: skills, wiki fetcher, agent prompts, workload declarations, TIRx analysis/docs and run launcher.
- Plausible first-party paths checked: long-running optimization, reference updates, benchmark-driven candidate choice and imported evolution traces.
- Why no material first-party path remains: these supply present-task domain knowledge and metrics; the external agent/developer, not TIRx, owns any prospective option or subsequent system capability choice.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate policy/identity decision path at an autonomous operational organization is present.
- Disturbance / variety regulated: forbidden read paths, process restrictions and correctness standards are explicit fixed task policies, not identity adjudication.
- Decisive decision or feedback right: user/developer selects task and fixed guard constraints; hook scripts enforce without resolving ultimate purpose conflicts.
- Decision owner: external task owner/developer for standing policies, not an in-boundary S5 authority.
- Supporting / enforcement mechanisms: generated Codex/Claude pre-tool hooks, process guards, banned-path lists and benchmark task declarations.
- Closure path: a policy violation blocks an external tool action; no identity-level issue is referred to a legitimate authority and returned as changed governing purpose.
- Why this is / is not agent-owned: executable guardrails and prompt constraints have no S5 discretion or specific ultimate-policy return path.
- Evidence: [Codex hooks configuration](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/preparation/codex.py), [Claude hook setup](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/preparation/claude.py), [task declarations](https://github.com/mlc-ai/TIRx-harness/blob/370b7461a4424edbd22238f6e6882b2a71e0ad5d/evolution/preparation/declare.py).
- Basis: bounded negative.
- Confidence: high.
- Caveats: higher-recursion maintainers and lab operators have genuine governance externally; no parent S5 is inferred from those facts.

### Absence scope

- Surfaces inspected: generated prompt, guard hook installers, task policies, CLI setup and operating documentation.
- Plausible first-party paths checked: task constraints, user-selected benchmark, Codex/Claude hook enforcement, manual run setup and maintainer configuration.
- Why no material first-party path remains: static guard constraints do not constitute an ultimate identity/policy judgment with legitimate return into a first-party agent organization.

## Distributed OSS parent arrangement

The OSS project maintains tooling and contributor workflows, while operators independently launch third-party coding agents in local worktrees. These are separate recursions; maintainer collaboration and manual GPU optimization policy do not instantiate a shared S3/S5 parent loop around first-party autonomous TIRx work cells.

## Self-hosted and non-human modes

Local or remote kcoral servers execute checks and compilers but do not decide model-selected work. The optional Humanize two-agent run is separately installed and launched; it is not a packaged non-human TIRx organization, so the Index neither imports its ownership nor invents an operator-governed `(P)` mode.

## Recursion

A user may compose TIRx with a richer agent system in which GPU optimization is an S1 unit and checks inform an audit; this is an external composed system, not the first-party TIRx distribution.

## Variety and escalation

Compiler diagnostics, correctness errors, remote GPU failures, tool timeouts and guard refusals return to the invoking external agent or user. The agent chooses recovery externally; the tooling itself supplies no agentic escalation hierarchy.

## Evidence gaps

No live GPU benchmark or external model process was executed; classification is based on source and explicit launch contracts. The lack of first-party agent decision ownership is direct and bounded, not a claim that externally composed GPU optimization agents are nonautonomous.
