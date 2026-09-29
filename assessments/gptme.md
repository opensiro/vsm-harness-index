---
harness_id: gptme
project_name: gptme
repository: https://github.com/gptme/gptme
review_ref: 0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# gptme

## Review boundary

- System in focus: the first-party gptme runtime at frozen revision `0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662`, including the model/tool conversation loop, first-party tools, persistent memory/context machinery, supported autonomous/non-interactive execution, and the explicitly supported `subagent` tool mode with first-party gptme child agents.
- Purpose and identity: a general-purpose local AI-agent harness for open-ended computer work, with optional first-party delegation into multiple isolated/specialized gptme child agents and persistent reuse of learned context across later sessions.
- Relevant environment: users/operators, external model providers, local repositories/files/processes, web/services reached through tools, configured MCP/ACP endpoints, and downstream applications embedding gptme.
- Standard-distribution boundary: first-party chat/executor/tool code, built-in profiles, hooks, subagent API/execution/control/persistence, worktree isolation, memory/lesson/context loading, CLI/server/TUI entry surfaces, and autonomous/non-interactive confirmation mode are inside. External model-provider cognition remains an environmental dependency. External ACP-compatible harness implementations and the separate `gptme-agent-template` repository remain outside ownership claims.
- Credited operating / distribution surfaces: the ordinary gptme model→tool→observation loop; the documented supported mode in which the built-in `subagent` tool is enabled (for example through `--tools ... subagent` / `+subagent`); first-party gptme child execution with profiles, isolation, status/progress/completion, steer/cancel and budget/concurrency controls; built-in persistent memory write/read paths; autonomous/non-interactive auto-confirmation.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI, release and maintainer activity, documentation examples as actors, development-only benchmark/evaluation work, and repository governance. Examples and tests may corroborate shipped behavior but do not themselves own VSM functions.
- First-party operating / deployment modes considered: ordinary interactive CLI/server/TUI/Python use; autonomous/non-interactive gptme runs; and the supported opt-in `subagent` mode using first-party gptme child agents. ACP children implemented by other harnesses are not required for any positive state below.
- Recursion level: in the base mode, one gptme-managed model/tool loop is the operational S1. In the subagent-enabled mode, independently executing first-party gptme child loops are S1 units at the delegated-work recursion, while the parent gptme agent supplies coordination/current-control and may invoke a separate verifier. Positive S2/S3/S3* claims are specific to this supported multi-agent mode rather than inferred from unrelated concurrent sessions.
- Reviewed revision: `0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

gptme's core `chat.py` loop repeatedly asks the configured model for a reply, recognizes model-emitted tool uses, executes them through first-party tool dispatch, appends the returned observations to the conversation log and calls the model again until no runnable tool use remains or a bounded stop condition fires. The external provider supplies model inference, but gptme owns the tool/action boundary and the observation-return loop that makes the trajectory operational.

The built-in `subagent` package is an explicitly supported but disabled-by-default tool surface. Once enabled, the parent model can spawn first-party gptme children in thread or subprocess modes, choose profiles/models/workdirs/context boundaries, run them in parallel or pipelines, observe status/progress/completions, steer or cancel them, continue prior children, and apply shared concurrency/token budgets. Children start with fresh execution contexts. Worktree isolation gives selected children separate Git working trees; changed isolated branches are preserved and returned to the parent for inspection/merge instead of directly mutating the parent's working tree.

Profiles provide specialization and enforced tool boundaries. In particular, `role="verify"` resolves to the built-in `verifier` profile and defaults to subprocess plus isolation. The verifier is instructed to review work produced by other agents, can directly read the repository and execute local checking commands, cannot use the ordinary write-capable tool set exposed to a developer profile, and returns a structured completion to the parent. This creates a first-party complementary audit path distinct from the producer's ordinary report.

Durable adaptation is separate from same-task compaction. The built-in `memory` tool tells the model to save information learned during work when it is worth remembering for future sessions; first-party storage persists those memories, and `prompts/workspace.py` automatically injects layered persistent memory into later sessions. Interactive confirmation can gate a write, but autonomous/non-interactive mode registers a first-party auto-confirm hook, so a supported autonomous mode closes the model-owned selection→persist→future-reuse loop without a human adaptation decision.

Primary evidence:

- [`gptme/chat.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/chat.py) — core model/tool/result continuation loop and bounded step execution.
- [`README.md`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/README.md) — shipped tool surface, including `subagent`, and CLI tool-selection surface.
- [`gptme/tools/subagent/__init__.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/__init__.py) — first-party delegation, parallel/pipeline execution, worktree isolation, fleet budgets, status/wait/steer/cancel and completion hooks.
- [`gptme/tools/subagent/api.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/api.py) — child execution modes, model/profile/context selection, persisted registry and operational control API.
- [`gptme/tools/subagent/execution.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/execution.py) — isolated worktree creation/cleanup, returned branches, profile tool enforcement and child runtime construction.
- [`gptme/tools/subagent/hooks.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/hooks.py) — progress/completion feedback and mid-run steer/cancel closure into child behavior.
- [`gptme/tools/subagent/types.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/types.py) — shared fleet budget and `verify` role defaults to verifier + subprocess + isolation.
- [`gptme/profiles.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/profiles.py) — built-in verifier role and hard tool allowlist behavior for subagents.
- [`gptme/tools/memory.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/memory.py) — model-callable persistent-memory constructor for future sessions.
- [`gptme/prompts/workspace.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/prompts/workspace.py) — automatic loading of persistent memories into later session context.
- [`gptme/hooks/auto_confirm.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/hooks/auto_confirm.py) — autonomous/non-interactive tool confirmation closure.
- [`gptme/attestation.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/attestation.py) — output/workspace provenance support; treated as supporting evidence machinery rather than S3* ownership by itself.

## Operational model

A base gptme run receives a user/task prompt, lets the model choose substantive tool actions, executes those actions in first-party code, returns observations and continues until completion. In a supported `subagent`-enabled run, the parent model can split work into independent gptme child trajectories, isolate mutation-capable children, inspect their current state/results, alter or stop them, and launch an isolated verifier before accepting or integrating work. Persistent memory can carry selected learning from one run into later runs.

The vector below therefore describes first-party capabilities across declared supported modes, not a claim that every default single-agent session instantiates all six functions simultaneously. S2/S3/S3* depend on the shipped `subagent` mode being enabled; S1 and S4 have direct first-party paths in ordinary/autonomous runtime modes. No external agent template, external ACP harness or repository-development organization is imported to complete these paths.

## S1 — Operations

- State: A
- Function: perform open-ended computer work through a model-driven decision/action/observation loop.
- Disturbance / variety regulated: user goals, changing workspace and external state, tool results/errors, provider responses, missing information and runtime/context constraints encountered during a task.
- Decisive decision or feedback right: choose the next substantive response or tool action in light of the current conversation and returned observations.
- Decision owner: the autonomous model-driven gptme agent actor.
- Supporting / enforcement mechanisms: `chat.py`, tool parsing/dispatch, logs, prompt queue, retries/interrupts, tool allowlists, confirmation hooks, context handling and provider adapters.
- Closure path: task/prompt → model reply → model-selected first-party tool invocation → tool result appended to the conversation → next model turn observes the result and revises/continues → completion or bounded stop.
- Boundary reachability: this is the core shipped gptme runtime across ordinary CLI/server/TUI/Python and non-interactive operation; no development-only actor or external harness is required beyond the configured model provider and environment reached by tools.
- Why this is / is not agent-owned: deterministic host code validates and executes actions, but the model owns the substantive next-action choice. Removing the model actor leaves execution machinery without a goal-directed operational decision loop.
- Evidence: [`gptme/chat.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/chat.py); [`README.md`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider-side model internals remain outside the repository boundary; the credited first-party ownership is the harness loop around that model cognition.

## S2 — Coordination

- State: A
- Function: attenuate filesystem/workspace interference among concurrently delegated first-party child S1 units while preserving a controlled reintegration path.
- Disturbance / variety regulated: multiple implementation-capable child agents operating concurrently against one repository could overwrite, expose or otherwise interfere with one another's in-progress workspace changes.
- Distinct S1 units: independently executing first-party gptme child agent loops delegated by the parent in the supported `subagent` mode.
- Inter-S1 disturbance: concurrent mutation-capable children sharing one repository workspace can collide, overwrite, or expose in-progress changes across operational units.
- Attenuating coordination relation: the parent selects first-party worktree isolation, giving each selected child a separate Git working tree/branch so its mutations do not directly alter the parent or sibling workspace.
- Feedback into subsequent S1 behaviour: changed isolated branches and child results return to the parent; the parent can inspect/integrate them before later delegated work, so subsequent S1s operate on the reconciled repository state rather than uncontrolled concurrent mutations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: credit rests on a concrete cross-S1 filesystem-interference disturbance and the worktree separation/reintegration mechanism that specifically attenuates it, not on fan-out, messaging, routing, or delegation by themselves.
- Decisive decision or feedback right: decide which delegated work should execute in isolated worktrees and how/when returned branches should be inspected or integrated relative to other S1 work.
- Decision owner: the autonomous parent gptme agent in the supported `subagent`-enabled mode.
- Supporting / enforcement mechanisms: `isolation="worktree"` / isolated execution, per-child workdirs, separate subprocess/thread contexts, smart worktree cleanup, preserved changed branches, completion results and optional parallel/pipeline scheduling.
- Closure path: parent identifies/delegates concurrent work → parent selects isolated child execution → first-party runtime creates separate worktree(s), preventing direct workspace mutation/collision → child completes → changed branch/result is returned to parent → parent can inspect/integrate the result before subsequent shared-repository work, changing later S1 operating context.
- Boundary reachability: worktree isolation is a documented argument of the shipped built-in `subagent` tool; the README/CLI expose `subagent` as a supported selectable tool. The positive path uses first-party gptme children rather than external ACP implementations.
- Why this is / is not agent-owned: git/worktree machinery deterministically enforces separation, but the parent model has the tool-visible discretion to choose isolated delegation and to act on returned branches. The enforcement layer does not choose the organizational response by itself.
- Evidence: [`gptme/tools/subagent/__init__.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/__init__.py); [`gptme/tools/subagent/api.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/api.py); [`gptme/tools/subagent/execution.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/execution.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: generic parallelism, pipelines, shared budgets and message delivery are not themselves credited as S2. The positive witness is specifically the documented cross-S1 workspace-interference problem and worktree isolation/reintegration relation in the supported multi-agent mode.

## S3 — Inside-and-now control

- State: A
- Function: maintain a current view of delegated S1 work and exercise present-tense authority over fleet execution, resource bounds and intervention.
- Disturbance / variety regulated: child tasks can stall, drift, consume excessive resources, need clarification, complete/fail at different times or require course correction while other work remains active.
- Whole-system current view: the parent can list/inspect all registered children and receives first-party progress/completion notifications, status, logs and persisted child metadata across the active delegated fleet.
- Current-control decision scope: present-tense spawn/continue/wait/steer/cancel choices plus shared concurrency/token-budget allocation across current child commitments.
- Decisive decision or feedback right: decide which children to spawn/continue, inspect, steer, cancel or await and how to allocate current concurrency/token budget across delegated work.
- Decision owner: the autonomous parent gptme agent in `subagent` mode.
- Supporting / enforcement mechanisms: `subagent_list`, status/wait/read-log functions, progress/completion queues, persisted child registry, `SubagentBudget`, max-concurrency semaphore, timeout/cancel machinery and durable steer/control queues.
- Closure path: child status/progress/completion reaches the parent through first-party APIs/hooks → parent model sees the current multi-child state → parent chooses spawn/steer/cancel/wait/continue or budgeted next work → first-party control hooks/semaphores enforce the choice → affected child/fleet operation changes and later state returns to the parent.
- Boundary reachability: the complete control surface is packaged with the supported built-in `subagent` tool and operates with first-party gptme child agents. The tool being opt-in by default is a deployment selection, not a development-only implementation dependency.
- Why this is / is not agent-owned: concurrency semaphores, timeout monitors and budget counters enforce limits but do not own current-control discretion. The parent model owns the choice to create/manage/intervene in child commitments using those first-party functions.
- Evidence: [`gptme/tools/subagent/__init__.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/__init__.py); [`gptme/tools/subagent/api.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/api.py); [`gptme/tools/subagent/hooks.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/hooks.py); [`gptme/tools/subagent/types.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/types.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the state does not credit a fixed token cap or concurrency limit as S3 ownership. Those are support/enforcement for a separately evidenced parent-agent current-control loop.

## S3* — Complementary audit

- State: A
- Function: independently challenge and verify work produced by another operational agent using a separate audit trajectory with direct access to operational artifacts.
- Disturbance / variety regulated: an implementation-producing S1 may report success while code, tests, edge cases, security properties or regression behavior remain wrong or incomplete.
- Claim being audited: the producer child's substantive claim that its implementation/work product is correct, complete and ready for parent acceptance/integration.
- Ordinary reporting path: the producing child returns its own `complete` result/summary and any preserved branch to the parent through the normal subagent completion path.
- Complementary access path: a separate `verify`-role child runs in subprocess + isolated workspace and directly reads the artifacts and can execute local checks/tests through its restricted verifier tool surface.
- Independence boundary: the verifier is a distinct model trajectory/process with fresh child context, an isolated worktree and verifier-specific tool/profile constraints rather than the producing child re-reading its own report.
- Who acts on findings: the autonomous parent gptme agent receives the verifier completion through the first-party completion hook and can reject, retry, steer, re-delegate or integrate subsequent work.
- Decisive decision or feedback right: make the substantive audit judgment about whether the producer's work withstands direct independent inspection/checking and report findings back for correction or acceptance.
- Decision owner: the autonomous verifier gptme child agent; the parent agent owns the subsequent current-control response to the audit result.
- Supporting / enforcement mechanisms: built-in `verifier` profile, `role="verify"` defaults, subprocess execution, isolated worktree, fresh child context, verifier tool restrictions, direct `read`/`shell`/`ipython` access, `complete` result and parent completion hook. Attestation hashes/provenance can support evidence integrity but are not treated as the audit decision owner.
- Closure path: producing child/work creates an artifact or claim → parent invokes a `verify`-role child → first-party role resolution runs verifier in a separate subprocess and isolated workspace → verifier directly reads/runs checks against operational artifacts rather than relying only on producer summary → verifier model returns its judgment via `complete` → first-party completion hook places the result in the parent conversation → parent can steer/retry/reject/integrate subsequent work.
- Boundary reachability: verifier role/profile, subprocess isolation, worktree creation and completion return are all shipped first-party components of the supported `subagent` mode; no external evaluator service or test-only actor is required.
- Why this is / is not agent-owned: isolation and tool allowlists create independence, but the verifier model itself performs the discretionary audit judgment. The parent then receives the judgment through a first-party feedback channel. This is not merely deterministic verdict parsing or self-verification by the producer.
- Evidence: [`gptme/tools/subagent/types.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/types.py); [`gptme/profiles.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/profiles.py); [`gptme/tools/subagent/api.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/api.py); [`gptme/tools/subagent/execution.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/execution.py); [`gptme/tools/subagent/hooks.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/subagent/hooks.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: a generic second model opinion or the standalone attestation utility would not be sufficient. Credit rests on the packaged verifier role's distinct process/workspace/tool access plus returned audit judgment and parent corrective path.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert newly learned future-relevant distinctions from present work into durable context that alters later-session capability/behavior.
- Disturbance / variety regulated: later sessions would otherwise repeat discovery of user preferences, project facts, decisions/rationales and recurring problem-solving context learned from prior interaction with the environment.
- External distinction: a user preference, project/environment fact, decision rationale or recurring problem pattern encountered through present interaction/tool work and judged relevant beyond the current turn.
- Future / prospective distinction: the agent explicitly evaluates whether that newly learned distinction is worth remembering for future sessions rather than only preserving same-task working context.
- Adaptation option generated: the model formulates a named durable memory containing the selected reusable distinction for later-session use.
- Path back into current capability / S3: first-party memory storage/indexing persists the option and later `prompt_workspace` construction automatically injects persistent memory into subsequent sessions, changing the context available to future operational/current-control decisions.
- Decisive decision or feedback right: judge which learned distinction is worth preserving for future work and formulate the durable memory content.
- Decision owner: the autonomous gptme model using the built-in `memory` tool in an autonomous/non-interactive mode.
- Supporting / enforcement mechanisms: `memory` ToolSpec and memory store/index, layered memory roots, future-session `prompt_workspace` loading, confirmation hooks and the autonomous `auto_confirm` hook.
- Closure path: current S1 encounters a future-relevant user/project/environment distinction → model judges it worth remembering and calls `memory` with the selected content → first-party runtime persists/indexes the memory → a later gptme session automatically loads persistent-memory indexes/content into system context → later model decisions operate with the returned distinction, changing subsequent capability/behavior.
- Boundary reachability: `memory` is a built-in first-party tool path, and the repository ships an explicit autonomous/non-interactive auto-confirm hook that confirms tool execution without human interaction. The future read path is in first-party workspace prompt construction.
- Why this is / is not agent-owned: storage/index/prompt injection are deterministic support. The model owns the prospective adaptation judgment — what newly learned distinction merits durable reuse and what content to preserve. Interactive confirmation can constrain a separate operator mode, but the supported autonomous mode closes without a human adaptation owner.
- Evidence: [`gptme/tools/memory.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/memory.py); [`gptme/prompts/workspace.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/prompts/workspace.py); [`gptme/hooks/auto_confirm.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/hooks/auto_confirm.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: context compaction, pre-authored lessons and profile-global memory by themselves are not credited as S4. The positive witness is the model-owned learn→select→persist→future automatic reuse loop.

## S5 — Policy / identity

- State: —
- Function: no first-party runtime identity/ultimate-policy closure is established at the reviewed recursion.
- Disturbance / variety regulated: gptme has prompts, profiles, tool permissions, confirmation/guardrail hooks and operator configuration, but no shipped loop was found in which an identity-level or ultimate-policy matter is autonomously or parent-governedly deliberated, authoritatively decided and returned as governing policy for the organization.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: system/agent instruction files, profiles, tool allowlists, confirmation hooks, behavior rules, environment/project configuration and operator-selected runtime modes.
- Closure path: these constraints can shape subsequent execution, but they enter as configured/static rules or ordinary operational approvals rather than an identity/ultimate-policy matter flowing to an authoritative S5 decision and back into organization-wide policy.
- Why this is / is not agent-owned: the runtime enforces supplied constraints and the model follows prompt/profile policy, but neither enforcement nor compliance establishes the missing ultimate-policy decision function. Ordinary confirmation of a tool or memory write is not S5.
- Evidence: [`gptme/profiles.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/profiles.py); [`gptme/tools/__init__.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/tools/__init__.py); [`gptme/hooks/cli_confirm.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/hooks/cli_confirm.py); [`gptme/prompts/workspace.py`](https://github.com/gptme/gptme/blob/0e4ef82bd6a6090bf9cefd357acc8f1dbebf2662/gptme/prompts/workspace.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: users/organizations embedding gptme may supply constitutional governance externally; that higher-recursion authority is not imported into the repository-relative assessment.

### Absence scope

- Surfaces inspected: core/system/workspace prompt construction, built-in profiles and behavior/tool restrictions, tool allowlist machinery, confirmation/auto-confirm hooks, persistent memory/lessons, autonomous agent service/workspace support, subagent control and repository-level documentation.
- Plausible first-party paths checked: agent/system prompt as durable identity; verifier/parent orchestration as S5; tool permissions and confirmation as ultimate policy; persistent memory as identity governance; autonomous-service configuration as constitutional authority; operator selection of enabled tools as parent S5.
- Why no material first-party path remains: each inspected path is a static/configured constraint, capability selection, learned operating context or lower-level operational/adaptation decision. None establishes a runtime identity/ultimate-policy dispute → authoritative judgment → returned organization-wide policy closure at the assessed recursion.

## Recursion

The frozen distribution supports two materially different first-party organizational modes. Ordinary gptme is one autonomous tool-using S1. With the documented built-in `subagent` tool enabled, independently running first-party gptme children become delegated S1 units and the parent gptme model can operate at the next recursion as coordination/current-control authority. The assessment does not treat mere nesting as recursion; the higher-recursion claim is limited to functions whose cross-child disturbance, whole-fleet view or audit relation is explicitly reconstructed above.

The separate `gptme-agent-template` repository is not treated as a parent or recursive completion layer. Likewise, external ACP-compatible agents may be invoked by the same API but are not required for the credited first-party topology.

## Variety and escalation

Operational variety is absorbed by tool choice, model/tool observation feedback, context management, child specialization, context/worktree isolation and optional model/profile routing. Inter-S1 mutation variety can be separated into worktrees. Current fleet variety returns as progress/completion/status and can trigger parent steer/cancel/continue decisions. Verification findings return through the same parent feedback surface. Future-relevant learned distinctions can be persisted into later-session memory. Clarification and interactive confirmation remain bounded operational/human paths rather than being promoted to S5.

## Evidence gaps

- The positive S2/S3/S3* states describe the explicitly supported `subagent`-enabled mode; the built-in tool is disabled by default and therefore those functions are not asserted for a bare default single-agent session.
- S2 credit is limited to the concrete workspace-interference attenuation path supplied by worktree isolation and parent reintegration; generic parallelism, pipelines or shared queues are not independently credited.
- S3* credit is limited to the first-party verifier role's separate subprocess/worktree plus direct artifact-checking path and returned judgment; attestation, traces, tests and ordinary self-verification are supporting or adjacent evidence only.
- S4 credit uses the explicit persistent-memory constructor and future automatic read path in autonomous/non-interactive mode; pre-authored lessons and same-task compaction are not used as the decisive adaptation witness.
- No runtime identity/constitutional/ultimate-policy closure was found for S5. External organizational governance and the separate `gptme-agent-template` are outside the assessed boundary.