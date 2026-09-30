---
harness_id: mini-coding-agent
project_name: mini-coding-agent
repository: https://github.com/rasbt/mini-coding-agent
review_ref: 717cae4ff10d01773bd12951f62a575825053414
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# mini-coding-agent

## Review boundary

- System in focus: the first-party `mini-coding-agent` executable coding harness at frozen revision `717cae4ff10d01773bd12951f62a575825053414`, including `MiniAgent`, its Ollama-backed model/tool loop, workspace context, structured tools and permission gates, transcript/working-memory persistence, session resume, context reduction, and the bounded read-only `delegate` child-agent path.
- Purpose and identity: autonomously inspect and modify a local software repository in response to a user objective, using a small model/tool feedback loop that can read, search, execute, write, patch, retain session state, and delegate bounded investigation.
- Relevant environment: the user request, current workspace/repository and Git state, repository documentation, filesystem contents, shell/test results, Ollama model responses, tool failures, approval decisions, and findings returned by bounded child agents.
- Standard-distribution boundary: `mini_coding_agent.py`, its installed `mini-coding-agent` CLI entry point, first-party session format, built-in tools and bounded delegation machinery are inside. Ollama and the selected model are external inference dependencies. The operator remains outside the autonomous actor when manually approving risky tools. Repository-development CI is an adjacent development system rather than part of normal runtime operation.
- Credited operating / distribution surfaces: `README.md`; `mini_coding_agent.py`; `pyproject.toml`; and runtime behavior corroborated by `tests/test_mini_coding_agent.py` and `EXAMPLE.md` at the frozen revision.
- Adjacent first-party surfaces excluded from ownership: `.github/workflows/ci.yml` and its repository-development lint/test jobs; tests as development verification rather than a shipped complementary-audit actor; tutorial/example instructions insofar as they describe operator actions outside the runtime; later default-branch behavior beyond the frozen revision.
- First-party operating / deployment modes considered: interactive REPL; one-shot CLI prompt; approval modes `ask`, `auto`, and `never`; session resume; normal mutable parent-agent operation; bounded read-only delegated child operation at one lower depth.
- Recursion level: one local coding-agent session is the focal organization. A delegated child is a separate bounded `MiniAgent` execution used as a subordinate investigative helper, but the frozen distribution does not establish it as a complete viable recursive organization with its own metasystem.
- Reviewed revision: `717cae4ff10d01773bd12951f62a575825053414`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The frozen repository is deliberately small: the executable harness is implemented in one Python module, `mini_coding_agent.py`, with the CLI exposed through `pyproject.toml`. `WorkspaceContext` collects current repository facts, including branch, status, recent commits and selected project documentation. `SessionStore` persists full session JSON under `.mini-coding-agent/sessions`, while `MiniAgent` retains a smaller working memory of the current task, touched files and recent notes.

`MiniAgent.ask()` owns the operating loop. It records the user request, sends the assembled prompt to the configured Ollama model, parses either a structured tool request or final answer, runs first-party tools, records tool evidence, updates memory and invokes the model again. Malformed outputs are fed back as retry notices; the loop is bounded by tool-step and malformed-response limits. Built-in tools provide repository listing/reading/searching, shell execution, file creation and exact patching. Path containment, argument validation, a repeated-identical-tool guard and approval modes constrain execution without replacing the model actor's task-specific discretion.

Delegation is first-party and operationally reachable. When the parent model calls `delegate`, the runtime creates another `MiniAgent` with the same model client/workspace/session store, increments depth, disables nested delegation at the configured bound, forces `read_only=True` and `approval_policy="never"`, seeds the child with the delegated task plus a clipped parent-history note, runs `child.ask(task)`, and returns the child's final text as `delegate_result` to the parent loop. The test suite explicitly exercises this path and verifies that the parent incorporates the child result.

The repository does not ship a separate scheduler, organization-wide resource controller, independent reviewer/auditor, prospective capability-adaptation loop, or identity-policy authority. The example workflow asks the same focal agent to create code, write tests, run them and fix failures; that is ordinary operational feedback within S1 rather than a complementary audit organization.

Primary evidence:

- [`README.md`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md)
- [`mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/mini_coding_agent.py)
- [`tests/test_mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/tests/test_mini_coding_agent.py)
- [`EXAMPLE.md`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/EXAMPLE.md)
- [`pyproject.toml`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/pyproject.toml)
- [`.github/workflows/ci.yml`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/.github/workflows/ci.yml)

## Operational model

A user starts one `MiniAgent` against a workspace. The runtime gives the model current workspace facts, memory and transcript context. The model chooses whether to inspect, search, execute, mutate, delegate or finish. Tool outputs and validation/approval failures are recorded into the session and therefore alter subsequent model decisions. The operational outcome is repository-facing coding work or a repository-grounded answer.

The bounded child-agent path does not create a persistent peer organization. A child is invoked by the parent as one read-only investigation tool, receives a scoped task, cannot mutate the workspace, cannot delegate beyond the configured depth, and returns one result into the parent operation. The parent remains the focal actor deciding what to do with that information.

## S1 — Operations

- State: A
- Function: perform repository-facing software-engineering work by interpreting a user objective, choosing context-sensitive repository/tool actions, observing their results and iterating until completion or a runtime bound is reached.
- Disturbance / variety regulated: heterogeneous coding requests, unknown repository structure/content, changing workspace/Git state, model uncertainty, tool errors, test/shell evidence, approval outcomes and child-investigation findings.
- Decisive decision or feedback right: choose the next task-specific tool/action or final answer and revise that choice from returned repository evidence.
- Decision owner: the model-backed `MiniAgent` actor. Ollama supplies inference, while the first-party harness owns the prompt/tool/session/feedback loop in which the actor's coding discretion is exercised.
- Supporting / enforcement mechanisms: `WorkspaceContext`; `SessionStore`; prompt assembly; structured tool parser; built-in tools; argument/path validation; approval modes; step/attempt bounds; repeated-call guard; context clipping/deduplication; working-memory persistence; CLI/session-resume machinery.
- Closure path: user request → first-party prompt/session assembly → model chooses tool/final → runtime validates and executes the tool → result/error is recorded into transcript/memory → next model call observes that evidence and changes action or completes.
- Boundary reachability: this loop is the shipped `MiniAgent.ask()` path behind both interactive and one-shot `mini-coding-agent` CLI operation; no downstream composition is required to create the model/tool feedback cycle.
- Why this is / is not agent-owned: removing the model-backed actor while leaving workspace collection, tools, persistence and enforcement in place preserves mechanisms but removes contextual choice of what coding action to take next and when the task is complete.
- Evidence: [`mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/mini_coding_agent.py); [`README.md`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md); [`tests/test_mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/tests/test_mini_coding_agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model intelligence is external through Ollama. In `ask` mode, a human may approve or deny risky tool execution, but the standard distribution also supports `auto`; approval enforcement does not own the ordinary coding decision right.

## S2 — Coordination

- State: —
- Function: no complete same-recursion inter-S1 coordination function was established in the reviewed standard distribution.
- Disturbance / variety regulated: no concrete interference, conflict or oscillation among distinct same-recursion S1 units was evidenced together with a mechanism that attenuates it and feeds the result back into their subsequent behavior.
- Decisive decision or feedback right: not established at S2 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: bounded `delegate` child execution; shared workspace/session-store substrate; read-only restriction on child agents; maximum delegation depth; parent receipt of `delegate_result`.
- Closure path: no S2 closure established. Delegation sends a scoped investigative task downward and returns information upward, but does not regulate a demonstrated conflict among peer operational units.
- Why this is / is not agent-owned: no S2 function is credited, so ownership is not classified. The parent may autonomously choose to delegate, but task decomposition/delegation alone is not S2.
- Evidence: [`mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/mini_coding_agent.py); [`tests/test_mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/tests/test_mini_coding_agent.py); [`README.md`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: the read-only child restriction reduces one possible parent/child collision surface, but the distribution does not expose a same-recursion peer coordination organization satisfying the S2 witness.

### Absence scope

- Surfaces inspected: full `mini_coding_agent.py` runtime; delegation implementation; session/memory and tool enforcement; README architecture/usage; runnable example; tests; package entry point; repository CI.
- Plausible first-party paths checked: parent/child delegation, shared workspace access, read-only child enforcement, repeated-tool suppression, transcript/session sharing patterns, tool sequencing and approval gates.
- Why no material first-party path remains: the only multi-actor path is bounded hierarchical investigation. No two distinct same-recursion S1 units plus a concrete inter-S1 disturbance, attenuation relation and returned coordination feedback are supplied at the frozen boundary.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system inside-and-now current-control function over multiple operational commitments/resources was established.
- Disturbance / variety regulated: local step exhaustion, malformed model output, repeated identical actions, risky tool execution and workspace escape are regulated, but these are per-agent execution/safety disturbances rather than organization-wide current commitments requiring S3 control.
- Decisive decision or feedback right: not established at S3 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `max_steps`/attempt bounds; approval modes; path containment; tool argument validation; repeated-identical-call rejection; read-only child mode; session reset/resume.
- Closure path: local enforcement can allow, deny, retry or stop one focal operational loop, but no whole-system current view selects or revises shared resources, commitments, priorities, accountability or cross-unit interventions.
- Why this is / is not agent-owned: deterministic execution controls do not become S3 merely because they constrain an autonomous S1, and no separate autonomous or parent S3 owner closes a current-control loop in the standard distribution.
- Evidence: [`mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/mini_coding_agent.py); [`README.md`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: an operator can approve or deny individual risky actions in `ask` mode, but that is ordinary execution permission over one S1 action, not an evidenced whole-system S3 parent loop.

### Absence scope

- Surfaces inspected: focal loop, tool/permission system, delegation, session persistence/resume, CLI modes and bounds, tests, README and example workflow.
- Plausible first-party paths checked: approval policy, step/attempt limits, repeated-call guard, child read-only/depth constraints, workspace-state snapshot, session reset/resume and tool failure feedback.
- Why no material first-party path remains: every identified control mechanism regulates one agent's local execution or enforces a static operator-selected constraint. There is no first-party whole-system current view plus discretionary authority over shared commitments/resources/priorities at the reviewed recursion.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary-audit path was established beyond ordinary operational inspection and testing.
- Disturbance / variety regulated: implementation defects or mistaken completion claims can be discovered when the focal agent reads code, runs tests or delegates investigation, but the distribution does not define a separate audit claim/path with independent challenge and corrective return.
- Decisive decision or feedback right: not established as a complementary audit judgment.
- Decision owner: not established.
- Supporting / enforcement mechanisms: read-only delegated child agents; ordinary `read_file`/`search`/`run_shell`; user-directed test execution in `EXAMPLE.md`; repository-development CI/tests.
- Closure path: ordinary tool/test evidence returns to the same focal S1 loop. A generic delegated investigation result also returns to the parent, but the child is not given an audit/reviewer contract distinct from normal task investigation.
- Why this is / is not agent-owned: the standard distribution ships no first-party independent reviewer/verifier role whose evidence access challenges an ordinary production claim and whose findings enter a defined corrective-control path.
- Evidence: [`mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/mini_coding_agent.py); [`tests/test_mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/tests/test_mini_coding_agent.py); [`EXAMPLE.md`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/EXAMPLE.md); [`.github/workflows/ci.yml`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/.github/workflows/ci.yml).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: the generic child-agent constructor could be composed into an audit workflow by a model/user, but no S3*-specific ordinary-report/complementary-access/independence/corrective-closure contract is first-party established at this frozen boundary.

### Absence scope

- Surfaces inspected: complete delegation implementation and delegation tests; operational example including pytest/fix behavior; built-in tool set; repository test suite; CI workflow; README.
- Plausible first-party paths checked: read-only child investigation, parent incorporation of child results, shell/test execution, retry/repeated-action checking, development CI and unit tests.
- Why no material first-party path remains: all runtime verification evidence belongs to the ordinary S1 execution path or generic investigation. CI/tests are adjacent development verification. No materially independent shipped audit actor/path challenges an ordinary operational claim under a distinct audit contract and returns findings into corrective control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective adaptation loop was established.
- Disturbance / variety regulated: workspace/Git facts, repository documentation, transcript history and current tool evidence inform the present coding task, but they do not model an external/future environment to generate capability adaptations.
- Decisive decision or feedback right: not established at S4 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `WorkspaceContext`; project-document snippets; recent Git commits/status; durable transcript and working memory; context clipping/deduplication; session resume.
- Closure path: current repository/context evidence returns directly into current S1 execution. No prospective environmental distinction is turned into an adaptation option that modifies later system capability through an S4↔S3 relation.
- Why this is / is not agent-owned: context gathering and memory reuse support S1 but do not establish the S4 organizational function.
- Evidence: [`mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/mini_coding_agent.py); [`README.md`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: recent commits and project docs are environmental context, but they are consumed as present-task evidence rather than as a prospective capability-adaptation program.

### Absence scope

- Surfaces inspected: workspace snapshot construction; project-doc/commit ingestion; prompt/memory/history logic; session persistence/resume; delegation; README, example, tests and CI.
- Plausible first-party paths checked: current project sensing, recent-commit awareness, durable notes/files memory, resumed sessions, child investigation and context reduction.
- Why no material first-party path remains: no first-party process distinguishes future/external change, develops adaptation options and returns a selected option into present capability. Persistence and current-context reuse alone do not supply S4.

## S5 — Policy and identity

- State: —
- Function: no runtime identity or ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: tool permissions, model choice, sampling limits, workspace root and runtime bounds constrain execution, but they are configuration/enforcement surfaces rather than an identity-level decision process.
- Decisive decision or feedback right: no first-party identity/ultimate-policy decision path is supplied.
- Decision owner: not established at S5 scope.
- Supporting / enforcement mechanisms: fixed system prompt/rules; CLI configuration; approval modes; tool schema and path restrictions; model/host/temperature/top-p settings; step/token bounds.
- Closure path: configuration is loaded/enforced during operation, and an operator may approve a risky action, but no identity/policy issue is routed to legitimate ultimate authority and returned as an authoritative system-level policy decision.
- Why this is / is not agent-owned: neither the model actor nor deterministic runtime is given an ultimate identity/policy right. Generic operator approval of tool actions is below S5 scope.
- Evidence: [`mini_coding_agent.py`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/mini_coding_agent.py); [`README.md`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/README.md); [`pyproject.toml`](https://github.com/rasbt/mini-coding-agent/blob/717cae4ff10d01773bd12951f62a575825053414/pyproject.toml).
- Basis: structural absence conclusion.
- Confidence: high.
- Caveats: users/developers can choose runtime configuration or modify the OSS code, but ordinary configuration/maintainer authority is not a first-party runtime S5 closure path.

### Absence scope

- Surfaces inspected: system prompt/rules; CLI/configuration arguments; approval policy; tool permissions/path restrictions; session controls; README; package metadata; tests and CI.
- Plausible first-party paths checked: operator approval, model/provider selection, execution-policy flags, fixed behavioral rules, session reset and repository-maintainer/development surfaces.
- Why no material first-party path remains: the frozen runtime exposes constraints and operator choices but no identity/ultimate-policy matter → legitimate authority → authoritative decision → returned-governance loop at the assessed organization boundary.

## Recursion

The parent `MiniAgent` can instantiate a child `MiniAgent`, so the implementation has genuine nested agent execution rather than merely a function call returning static data. The child has its own session and model/tool loop but is deliberately bounded: read-only, `approval_policy="never"`, limited steps and one level of delegation. The evidence establishes subordinate operational autonomy for investigation, not a self-contained viable recursive organization with its own S2–S5 metasystem. No stronger recursion claim is made.

## Variety and escalation

The focal S1 absorbs coding-task variety through model discretion, repository inspection, shell/file tools and iterative evidence feedback. Deterministic mechanisms attenuate dangerous or unproductive variety: workspace containment, tool schemas, approval gates, output/history clipping, maximum steps and repeated-call rejection. Malformed model outputs are amplified back into the next model turn as runtime notices so the agent can retry.

Escalation is narrow. In `ask` mode, risky tool execution is presented to the local operator for approval; denial returns an error into the same operational loop. That is an execution permission boundary, not evidence of S3 or S5. The runtime has no separate organization-wide escalation structure.

## Evidence gaps

The assessment is intentionally repository-relative to frozen revision `717cae4ff10d01773bd12951f62a575825053414`. Ollama/model internals are external and were not credited with additional VSM functions. The repository is compact enough that all substantive first-party runtime, documentation, example, tests, package metadata and CI surfaces were reviewed for negative-state scope. No materially ambiguous first-party S2/S3/S3*/S4/S5 path remained at this boundary; therefore `—` rather than `?` is used for those functions.
