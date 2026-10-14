---
harness_id: errander
project_name: errander
repository: https://github.com/EVAE-AL/errander
review_ref: 699f597971f13de9cf1f22b94a4c8177ad9c3863
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

# errander

## Review boundary

- System in focus: the installed, first-party errander Python terminal coding agent at frozen revision `699f597971f13de9cf1f22b94a4c8177ad9c3863`, including `Agent.run`, its own OpenAI-compatible chat transport, five tool handlers, CLI confirmation and workspace safeguards.
- Purpose and identity: take one natural-language software task and make task-specific model-selected filesystem, search and shell operations within a given workspace, then return an answer or step-limit result.
- Relevant environment: unknown codebase, mutable project files, command/test output and failures, model-generated tool requests, provider endpoint and per-call human confirmations.
- Standard-distribution boundary: Python `errander` package/console entrypoint and the `src/errander/` first-party agent/client/tool/CLI modules. Configured external model services, task repository, generic tools' shell subprocesses, CI, tests, upstream project governance and hypothetical external orchestrators are not credited as separate first-party VSM owners.
- Credited operating / distribution surfaces: `src/errander/agent.py`, `src/errander/llm.py`, `src/errander/tools.py`, `src/errander/cli.py`, `src/errander/__main__.py`, `pyproject.toml`.
- Adjacent first-party surfaces excluded from ownership: README experiments/examples, tests, developer/release CI, user-built wrappers, outside verification systems and projects worked on by errander.
- First-party operating / deployment modes considered: CLI one-shot input/piped task, configured remote/local OpenAI-compatible inference endpoint, interactive command/overwrite confirmation, and explicit `--yes` automation. A new process per task is not a shipped collaborating agent fleet.
- Recursion level: one local coding agent S1 with deterministic tool guardrails and outside human approval. No additional nested viable organization is declared merely from tools/processes.
- Reviewed revision: `699f597971f13de9cf1f22b94a4c8177ad9c3863` (frozen intake #898, not a current-head reassessment).
- Observation date: 2026-10-14.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The shipped `errander` console script invokes an `Agent` composed with a first-party `LLMClient` and `ToolBox`. `Agent.run` sends its conversation and schemas to an OpenAI-compatible model endpoint. Whenever the model supplies tool calls, the harness dispatches each through the first-party toolbox and appends returned strings to the conversation as `tool` observations; the model then chooses another action or ends with a tool-free assistant response, bounded by `max_steps`. The first-party `LLMClient` parses streaming/non-streaming responses, including argument parsing. Malformed/failed tool attempts become model observations.

The toolbox exposes `list_dir`, `read_file`, `write_file`, `search_files` and `run_command`; workspace path containment and sensitive-file filtering restrict local file operations. Shell command denylisting and UI confirmation constrain execution; overwrites also require confirmation unless deliberately waived. `--yes` changes the operator-selected per-action policy but not the agent's identity/ultimate purpose. There are no bundled task planner/fleet managers, child model runners, independent reviewer or adaptation/strategic modules in the frozen source tree. A successful test command invoked by the **same** agent belongs to its S1 coding feedback, not a complementary external audit.

Primary evidence: [`README.md`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/README.md); [`src/errander/agent.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/agent.py); [`src/errander/llm.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/llm.py); [`src/errander/tools.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/tools.py); [`src/errander/cli.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/cli.py); [`pyproject.toml`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/pyproject.toml).

## Operational model

One model decides subsequent coding operations based on observed workspace output. The deterministic toolbox and operator approvals may deny an action, but do not decide what software modification would best satisfy the task. No material first-party function-specific higher metasystem (inter-S1 S2, whole-current S3, complementary S3*, external-prospective S4 or identity/ultimate-policy S5) is reached in this installed single-process standard distribution.

## S1 — Operations

- State: A
- Function: perform environment-contingent coding/inspection by selecting project tool actions against an open-ended user instruction.
- Disturbance / variety regulated: unfamiliar files and APIs, model uncertainty, shell/test errors, refused commands and changing task state.
- Decisive decision or feedback right: choose next tool and parameters, revise after error/output, or declare task complete.
- Decision owner: model-directed first-party `Agent.run`; externally hosted model inference is a dependency, while the looping tool/action-result organization is shipped and first-party.
- Supporting / enforcement mechanisms: `LLMClient`, `ToolBox`, step budget, tool schemas, path/sensitive-file guards and shell/user confirmations.
- Closure path: user task and workspace observations → model tool request → first-party guarded tool execution → observed tool result appended to chat → next model tool choice or final response.
- Boundary reachability: shipped `errander` CLI constructs `Agent` and `ToolBox`; it does not delegate the coding loop to another CLI.
- Why this is / is not agent-owned: without the model's interpretation and next-action choice the deterministic registry could only execute already-specified operations, not choose how to solve an unfamiliar coding task.
- Evidence: [`src/errander/agent.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/agent.py); [`src/errander/llm.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/llm.py); [`src/errander/tools.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/tools.py); [`src/errander/cli.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/cli.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: the agent's unverified final statement is not independent proof of outcome correctness.

## S2 — Coordination

- State: —
- Function: no first-party regulation of disturbance/conflict between distinct operational S1 units.
- Disturbance / variety regulated: hypothetical simultaneous worker edits, divergent tasks or shared resource collisions, absent from the one-agent distribution.
- Decisive decision or feedback right: none relating competing S1 tasks to a corrective coordination action.
- Decision owner: no identifiable S2 owner; tool execution/confirmation belongs within one S1.
- Supporting / enforcement mechanisms: serial agent loop, per-file workspace sandbox, step limit and tool command sequence.
- Closure path: all tool outputs return to one model; no cross-worker interference signal or corrective effect reaches another independent S1.
- Why this is / is not agent-owned: even if an external operator starts two separate errander processes, first-party source does not provide a shared S2 relation between them.
- Evidence: [`src/errander/agent.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/agent.py); [`src/errander/tools.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/tools.py); [`src/errander/cli.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/cli.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: this is not a claim that external scripts cannot coordinate multiple installed copies.

### Absence scope

- Surfaces inspected: all shipped runtime modules (agent, model client, toolbox, CLI), metadata/packaging and documented invocation paths.
- Plausible first-party paths checked: spawned child agents, sibling coordination bus, multiple task owners, collision detection, shared task state and return from conflict adjudication.
- Why no material first-party path remains: no first-party multi-S1 ownership or inter-S1 feedback machinery is instantiated; subprocesses in `run_command` act as task tools, not autonomous worker cells.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-current organizational management over multiple operational commitments or work cells.
- Disturbance / variety regulated: prioritization, capacity and resource conflicts among a worker fleet would require a supervising function; none is present.
- Decisive decision or feedback right: the model's next tool and an operator's shell approval regulate only the current coding run.
- Decision owner: no S3-wide decision owner; current task owner is S1 and per-action permissions owner is user/operator.
- Supporting / enforcement mechanisms: step budget, CLI workdir/options, read/search context and confirmation prompts.
- Closure path: a refused/accepted tool affects that call and model's subsequent S1 choices, not current-control decisions across organizational units.
- Why this is / is not agent-owned: a task-local completion decision and deterministic safety rule lack whole-system current scope.
- Evidence: [`src/errander/agent.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/agent.py); [`src/errander/cli.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/cli.py); [`src/errander/tools.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/tools.py).
- Basis: structural
- Confidence: high
- Caveats: no separate parent-governed S3 mode claimed from human confirmation.

### Absence scope

- Surfaces inspected: agent model loop, CLI run lifecycle, tool registry and operator confirmations.
- Plausible first-party paths checked: whole-fleet current board/roster, multiple S1 outcome aggregation, discretionary reallocations, human parent supervisor and returned current-work interventions.
- Why no material first-party path remains: first-party implementation handles one code task and one agent run, without organizational cross-operation state, view or S3 decision authority.

## S3* — Complementary audit

- State: —
- Function: no independently sourced complementary auditor that evaluates an S1 claim and returns corrective control.
- Disturbance / variety regulated: false claims of fixed bugs or passing tests, incorrect patch and undiscovered defects.
- Decisive decision or feedback right: the same model can request shell tests, read files and decide whether its result is satisfactory; no separate first-party reviewer judges that result.
- Decision owner: no independent S3* actor or constructor; human approval is a guard on a tool action, not a separate audit of produced outcomes.
- Supporting / enforcement mechanisms: same-agent read/search/command tools, shell output returned to model, CLI preview/confirmation and self-check instruction.
- Closure path: self-testing returns directly to the executing S1 model; no independent critique/evidence → challenged claim → corrective management return path.
- Why this is / is not agent-owned: the coding model's instruction to check results does not create an independent examiner; test command outputs are ordinary S1 observations here.
- Evidence: [`src/errander/agent.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/agent.py); [`src/errander/tools.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/tools.py); [`src/errander/cli.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/cli.py); [`README.md`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: independent external CI/human reviewers can inspect artifacts but are not built into the frozen first-party general harness.

### Absence scope

- Surfaces inspected: full shipped Python module set, test-oriented tool calls, CLI output, documented feature list and package entrypoint.
- Plausible first-party paths checked: separately launched reviewer, source-first artifact audit, independent gate/verification report, corrective work return.
- Why no material first-party path remains: no first-party reviewer actor, distinct evidence judge or independent acceptance/repair loop ships.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party outside/future intelligence evaluating strategic changes to the agent organization and returning selected new capabilities.
- Disturbance / variety regulated: future changes in tool availability, project constraints or model competence might merit adaptation, but the current task is the only model-scoped operating horizon.
- Decisive decision or feedback right: model chooses coding tools for this task and operator chooses endpoint/model from environment variables; neither comprises a separate prospective organizational choice.
- Decision owner: no S4 actor identified; upstream repository maintenance and operator upgrades are outside the installed runtime.
- Supporting / enforcement mechanisms: static `SYSTEM_PROMPT`, fixed five-tool toolbox, endpoint settings, prompt history and output truncation.
- Closure path: tool observations influence next task step, not a selected future capability update integrated into continuing organizational operation.
- Why this is / is not agent-owned: model-directed modifications to the user's codebase are S1 task outcomes, not a harness-level ability to sense the outside and plan/adopt future capability.
- Evidence: [`src/errander/agent.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/agent.py); [`src/errander/llm.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/llm.py); [`src/errander/tools.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/tools.py); [`src/errander/cli.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/cli.py).
- Basis: structural
- Confidence: high
- Caveats: maintainer edits to errander itself or external refactoring workflows require a distinct system boundary.

### Absence scope

- Surfaces inspected: endpoint/provider config, agent history, tool implementations, runtime control and README descriptions.
- Plausible first-party paths checked: external horizon scanning, candidate capability proposals, prospective decision over organizational operating modes, returned deployed adaptation.
- Why no material first-party path remains: no long-term environment intelligence, future-option selection or first-party adoption feedback path appears in the compact runtime.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate identity/policy decision and returned constitutional governance for the installed agent organization.
- Disturbance / variety regulated: dangerous shell requests and secrets are constrained but do not constitute ultimate-purpose conflicts.
- Decisive decision or feedback right: human confirms execution of particular commands or overwrites, and chooses optional `--yes`/allow-secrets; no identity/ultimate-policy matter is adjudicated.
- Decision owner: operator sets permitted actions; deterministic toolbox enforces restrictions. No first-party S5 authority over organizational mission is demonstrated.
- Supporting / enforcement mechanisms: CLI confirmation callbacks, path sandbox, secret masks, hard command denylist, max-step setting.
- Closure path: permission result changes current tool execution; no constitutional issue → legitimate parent decision → durable returned identity-level policy governing future operation.
- Why this is / is not agent-owned: the model has no authority to redefine the tool/purpose constitution; safety enforcement has a user-configured action scope.
- Evidence: [`src/errander/cli.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/cli.py); [`src/errander/tools.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/tools.py); [`src/errander/agent.py`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/src/errander/agent.py); [`README.md`](https://github.com/EVAE-AL/errander/blob/699f597971f13de9cf1f22b94a4c8177ad9c3863/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: user organization policy or upstream project developer governance must not be silently borrowed.

### Absence scope

- Surfaces inspected: first-party command/overwrite approval, sandbox, secret protection, task prompt and CLI options.
- Plausible first-party paths checked: identity/policy dispute, legitimate higher authority, durable governing rule choice and return to subsequent operation.
- Why no material first-party path remains: the first-party mechanisms only govern bounded operational tool rights/limits, not the legitimate ultimate identity/constitutional policy decision cycle.

## Distributed OSS parent arrangement

The errander GitHub maintainer and separate users installing the package do not form a first-party distributed S5 parent supervising one installed task run. Contributor workflows, CI and separate externally supervised agents are outside this assessment boundary.

## Self-hosted and non-human modes

An operator can point errander to a local/remote OpenAI-compatible endpoint and enable `--yes`, but the same S1 model/tool loop remains. Model deployment locality and fewer human prompts do not independently supply S2-S5 or `(P)` parent governance.

## Recursion

The source defines one reusable coding operational cell, not an internally recurring fleet of viable subsystems; external composition must declare and prove its own recursion if assessed later.

## Variety and escalation

Unknown source and command feedback are absorbed by model choices. Sandbox, step limit and permission/denylist attenuate risky or excessive tool variety. An execution approval or failed tool remains local task governance and does not prove a separate algedonic/S5 policy channel.

## Evidence gaps

- Static frozen-source assessment only: no model-run empirical success benchmark or correctness claim.
- Future extensions/external operating hosts could introduce additional VSM functions in a different declared assembly. This bounded standard distribution does not credit hypothetical externally wired mechanisms.
