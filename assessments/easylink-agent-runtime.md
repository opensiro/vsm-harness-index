---
harness_id: easylink-agent-runtime
project_name: Easylink Agent Runtime
repository: https://github.com/easylink-ai-open/agent-runtime
review_ref: a9447bb5d9f3ab3b258fd399e9a1619c97e621fd
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Easylink Agent Runtime

## Review boundary

- System in focus: the standalone first-party `easylink-ai-open/agent-runtime` kernel at frozen revision `a9447bb5d9f3ab3b258fd399e9a1619c97e621fd`, including `Agent`/`AgentLoop`, built-in provider clients and neutral message types, tools, collaboration-mode enforcement, hooks, budgets, interruption/HITL, context compaction, and the exported `subagents` control/dispatcher primitives.
- Purpose and identity: a product-neutral agent runtime that owns request→tool calls→repeat→finalize and exposes reusable subagent control primitives while leaving product persistence, memory, sandboxes, channels, concrete collaboration policy, and durable product state outside.
- Relevant environment: external model providers, caller/product applications, injected tools/policies/factories, users/HITL, sandboxes and persistence supplied by consumers.
- Standard-distribution boundary: the model/tool loop, first-party HTTP clients, neutral runtime types, collaboration enforcement, hooks/budgets, context helpers, `AgentControl`, in-memory subagent state/mailbox/runners, and `SubagentToolDispatcher` are inside. Product-owned persistence, concrete policy, sandboxing, channels, memory/skills and other consumer behavior remain outside.
- Credited operating / distribution surfaces: ordinary `Agent.ask`/`continue_turn`; optionally composed public subagent primitives in which `SubagentToolDispatcher` exposes spawn/run/send/wait/list/read/close to a model-driven root agent. Because this higher-level mode requires caller construction of the child `SubagentFactory` and explicit assembly into the root `Agent`, it is treated as constructor reachability rather than a preassembled autonomous manager deployment.
- Adjacent first-party surfaces excluded from ownership: tests/CI, repository governance, caller hooks as decision owners, arbitrary role labels such as `reviewer`, and product behavior explicitly declared outside the runtime.
- Recursion level: ordinary `AgentLoop` is operational S1. In the optional subagent constructor, child `AgentLike` instances are S1 units and `AgentControl` plus the root-facing dispatcher form a potential parent current-control layer.
- Reviewed revision: `a9447bb5d9f3ab3b258fd399e9a1619c97e621fd`.
- Observation date: 2026-09-29.

## Repository architecture

The runtime's primary `AgentLoop` repeatedly requests a provider-neutral model response, executes requested tools, turns tool failures into observations when configured, and feeds results back until the model finalizes or an iteration/interruption/HITL boundary stops the turn. Collaboration modes constrain tool/effect availability but intentionally contain mechanism rather than product policy.

The frozen ref also exports a complete low-level subagent constructor surface. `AgentControl` stores a root/child tree, can spawn and run children, track current status/results, exchange mailbox messages and close children. `SubagentToolDispatcher` exposes those controls directly as model-callable tools, including `spawn_subagent`, `run_subagent`, `send_to_subagent`, `wait_subagent`, `list_subagents`, `read_subagent`, and `close_subagent`. The repository, however, does not provide a preassembled high-level mode that wires a root `Agent`, a concrete first-party child factory and that dispatcher together; `SubagentFactory` is supplied by the consumer.

Primary evidence:

- [`README.md`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/README.md)
- [`src/agent_runtime/core.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/core.py)
- [`src/agent_runtime/loop.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/loop.py)
- [`src/agent_runtime/__init__.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/__init__.py)
- [`src/agent_runtime/subagents/control.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/subagents/control.py)
- [`src/agent_runtime/subagents/dispatcher.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/subagents/dispatcher.py)
- [`tests/test_subagents.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/tests/test_subagents.py) — corroborates reachability of the exported constructor surface; tests are not ownership actors.

## Operational model

In the base mode, a first-party `Agent` owns the model/tool feedback loop while substantive action choice comes from the configured model. A caller can additionally construct `AgentControl` and wrap the root's tool dispatcher with `SubagentToolDispatcher`; then the root model can inspect child status/results and decide to spawn, run, message, wait for, read or close children. Because the runtime intentionally leaves the child factory and product assembly to the consumer, that higher current-control function receives constructor credit rather than autonomous runtime ownership.

## S1 — Operations

- State: A
- Function: execute open-ended task work through repeated model decisions and tool/environment feedback.
- Disturbance / variety regulated: task changes, provider responses, tool results/errors, context pressure, interruption, HITL pauses and iteration limits encountered during a turn.
- Decisive decision or feedback right: choose substantive next response or tool calls after observing accumulated conversation/tool results.
- Decision owner: the model-driven `Agent` actor running through the first-party `AgentLoop`.
- Supporting / enforcement mechanisms: provider-neutral requests/responses, built-in HTTP clients, tool dispatcher, collaboration-mode filtering, hooks, retries, iteration budget, context compaction, interruption and tool-error containment.
- Closure path: user/task input → model response → model-requested tool → first-party dispatch/result → result appended to messages → later model request revises/continues → final response or bounded stop.
- Boundary reachability: this is the ordinary public `Agent.ask` / `continue_turn` path and requires no product-level orchestration beyond supplied model credentials/tools.
- Why this is / is not agent-owned: deterministic kernel code executes and constrains actions, while model cognition owns the substantive next-action choice in the closed first-party loop.
- Evidence: [`README.md`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/README.md); [`src/agent_runtime/core.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/core.py); [`src/agent_runtime/loop.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/loop.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: persistence, product memory and sandbox behavior are explicitly outside the standalone runtime and are not imported into S1 credit.

## S2 — Coordination

- State: —
- Function: no qualifying first-party S2 coordination function is established.
- Disturbance / variety regulated: no concrete inter-S1 disturbance with a first-party attenuation-and-feedback loop is established.
- Decisive decision or feedback right: no qualifying S2 coordination right is identified.
- Decision owner: none identified for S2 inside the standalone runtime.
- Supporting / enforcement mechanisms: subagent mailboxes, parent/child messaging, child-count/depth limits, thread-pool execution, collaboration modes and generic delegation exist, but these do not establish S2 by topology or communication alone.
- Closure path: no complete function-specific path was found from interference among distinct S1 units through an attenuating relation back into subsequent S1 behaviour.
- Why this is / is not agent-owned: because the function itself is not established, autonomy is not graded.
- Evidence: [`src/agent_runtime/subagents/control.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/subagents/control.py); [`src/agent_runtime/subagents/dispatcher.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/subagents/dispatcher.py); [`README.md`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/README.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: model-callable messaging/delegation is not credited as S2 without a demonstrated inter-S1 disturbance and attenuation relation.

### Absence scope

- Surfaces inspected: subagent tree/store/mailbox/runners, model-callable subagent dispatcher, collaboration modes, budgets and tool execution.
- Plausible first-party paths checked: mailbox communication, parent/child delegation, parallel runner capacity, depth/child limits, blocked effects/tools and shared model/tool loop constraints.
- Why no material first-party path remains: these mechanisms communicate, limit or route work but do not establish a function-specific cross-S1 disturbance attenuation loop.

## S3 — Inside-and-now control

- State: C
- Function: provide a reusable current-control constructor over a root agent's active subagent tree.
- Disturbance / variety regulated: child agents can be idle, running, waiting, completed, errored or closed; the parent may need to inspect current results/status and change active commitments.
- Whole-system current view: `AgentControl` stores the root/child tree and current node status/result/last-run state; model-callable `list_subagents`, `read_subagent` and `wait_subagent` expose that current state to the root when assembled through `SubagentToolDispatcher`.
- Current-control decision scope: spawn or run children, message/wake them, wait/read current status/results, and close child commitments.
- Decisive decision or feedback right: the composed root model can choose those current-control actions through the first-party dispatcher; the base runtime does not itself assemble the root agent, child factory and dispatcher into a supported one-call manager mode.
- Decision owner: supplied/composed root model actor; first-party runtime provides the function-specific constructor rather than standalone ownership.
- Supporting / enforcement mechanisms: `AgentControl`, `AgentStore`, mailbox, runners, node statuses, lifecycle events, depth/child caps and `SubagentToolDispatcher` tool schemas/dispatch.
- Closure path: child tree/status/result → model-visible list/read/wait result → root model chooses spawn/run/send/wait/read/close → `AgentControl` applies lifecycle change → updated tree/status becomes visible to subsequent root decisions.
- Boundary reachability: all control types/tools are exported from the public package and mechanically tested, but callers must supply `SubagentFactory` and explicitly wire `SubagentToolDispatcher` into an `Agent`.
- Why this is / is not agent-owned: the function-specific loop and model-callable decision surface are first-party, yet the organization is not preassembled and the decisive manager actor enters through caller composition; constructor credit therefore fits better than A.
- Evidence: [`src/agent_runtime/__init__.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/__init__.py); [`src/agent_runtime/subagents/control.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/subagents/control.py); [`src/agent_runtime/subagents/dispatcher.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/subagents/dispatcher.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: ordinary `Agent` construction does not automatically mount subagent control; the C state is specific to the exported constructor surface rather than the default single-agent path.

## S3* — Audit / monitoring

- State: —
- Function: no qualifying independent corrective audit function is established.
- Disturbance / variety regulated: no distinct audit disturbance is closed by an independent first-party evidence path and corrective return.
- Decisive decision or feedback right: no qualifying auditor decision right is established.
- Decision owner: none identified for S3*.
- Supporting / enforcement mechanisms: hooks, tool callbacks, subagent role labels, lifecycle events, retries and caller-supplied auditing hooks are available but do not create an independent audit organ.
- Closure path: no first-party path was found from complementary evidence access through independent challenge/judgment into corrective current-control action.
- Why this is / is not agent-owned: observer hooks and an arbitrary child role such as `reviewer` do not establish S3* without materially independent challenge and corrective return.
- Evidence: [`README.md`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/README.md); [`src/agent_runtime/subagents/dispatcher.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/subagents/dispatcher.py).
- Basis: explicit absence after audit review.
- Confidence: high.
- Caveats: caller hooks may implement auditing in a consumer, but caller-supplied behavior is not imported into the standalone runtime assessment.

### Absence scope

- Surfaces inspected: lifecycle hooks, stream/tool callbacks, subagent roles/events/status, HITL pause and collaboration-mode constraints.
- Plausible first-party paths checked: reviewer-labelled child agents, after-tool/after-turn hooks, interruption/HITL, tool-error feedback and subagent result inspection.
- Why no material first-party path remains: none defines an independent evidence source/judgment role plus a corrective return path as shipped runtime behavior.

## S4 — Intelligence / adaptation

- State: —
- Function: no qualifying prospective adaptation/intelligence function is established.
- Disturbance / variety regulated: no environment-facing future-capability disturbance is shown to trigger a first-party adaptation decision.
- Decisive decision or feedback right: no runtime actor selects durable capability changes from evidence for later work.
- Decision owner: none identified for S4.
- Supporting / enforcement mechanisms: context compaction, hooks, messages, collaboration configuration and caller-created subagents can change current execution, but the README explicitly leaves memory/skills/product persistence outside.
- Closure path: no path from external/future evidence through candidate capability generation/evaluation into durable adoption for later runs was found.
- Why this is / is not agent-owned: current-turn compaction and caller configuration are not prospective organizational adaptation.
- Evidence: [`README.md`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/README.md); [`src/agent_runtime/loop.py`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/src/agent_runtime/loop.py).
- Basis: explicit absence after adaptation review.
- Confidence: high.
- Caveats: `SummarizingCompactor` changes current context representation, not future organizational capability.

### Absence scope

- Surfaces inspected: compaction, hooks, messages, subagent construction/configuration, collaboration modes and exported runtime state.
- Plausible first-party paths checked: model-generated summaries, subagent creation, configuration changes and consumer-provided hooks.
- Why no material first-party path remains: these are current-execution or externally authored mechanisms; no first-party durable evidence→adaptation→later-operation closure exists.

## S5 — Identity / ultimate policy

- State: —
- Function: no qualifying identity / ultimate-policy function is established.
- Disturbance / variety regulated: no identity-level constitutional disturbance is established.
- Decisive decision or feedback right: collaboration modes and hooks enforce supplied constraints but do not decide ultimate organizational identity/policy.
- Decision owner: none identified for S5.
- Supporting / enforcement mechanisms: collaboration-mode developer instructions, blocked tool/effect sets, hooks, budgets and runtime configuration.
- Closure path: no path from identity/constitutional issue through legitimate ultimate authority back into subsequent operation was found.
- Why this is / is not agent-owned: the runtime intentionally ships mechanism rather than concrete product policy, so generic constraints cannot be promoted to S5.
- Evidence: [`README.md`](https://github.com/easylink-ai-open/agent-runtime/blob/a9447bb5d9f3ab3b258fd399e9a1619c97e621fd/README.md).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: consumer-defined collaboration policy belongs to the product layer and is not inherited as runtime S5.

### Absence scope

- Surfaces inspected: collaboration modes, hooks, configuration, tool-effect restrictions and product/runtime boundary documentation.
- Plausible first-party paths checked: blocked tools/effects, developer instructions, runtime budgets and caller policies.
- Why no material first-party path remains: all are execution constraints/mechanisms; no identity-level issue, ultimate authority or return-to-operation closure is defined.

## Recursion

The subagent primitives permit hierarchical root/child trees and even optional child spawning, but hierarchy alone is not a VSM function. The assessment gives S3 constructor credit only to the explicit current-view/current-control path exposed to a root model and does not infer S2/S3*/S4/S5 from plurality or role labels.

## Variety and escalation

Iteration budgets, tool/effect blocking, model retries, HITL pause, interruption, child/depth caps and current child status constrain execution variety. These mechanisms support S1 and the S3 constructor but are not independently promoted to organizational functions.

## Evidence gaps / terminal outcome

Proposed vector: `S1=A / S2=— / S3=C / S3*=— / S4=— / S5=—`.

The notable result at this frozen revision is the exported `subagents` surface: it is stronger than generic delegation because a root model can be given a current view and model-callable lifecycle authority over children. The runtime nevertheless leaves the concrete child factory and assembly into the root agent to the consumer, so current-control is classified conservatively as constructor credit rather than autonomous S3. No function-specific S2 disturbance attenuation, independent corrective S3*, prospective S4 adaptation or S5 identity closure was found.
