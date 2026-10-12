---
harness_id: swarms
project_name: Swarms
repository: https://github.com/kyegomez/swarms
review_ref: 3009364a7e44dc3e55fec238b56b3a4fa6949a05
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Swarms

## Review boundary
- System in focus: installed first-party Python `swarms` runtime with individually model-directed Agent operating units, shipped GroupChat coordination and HierarchicalSwarm leader/worker current-control configuration.
- Purpose and identity: deploy reusable agent/tool workers and optional first-party multi-agent orchestration, conversation-floor arbitration and director-based planning/feedback.
- Relevant environment: external model responses, tools and workspace outputs, simultaneous agent conversational claims, user task, differing specialist results and current worker outcomes.
- Standard-distribution boundary: published Swarms Python distribution under `swarms/structs`, not user-written examples, third-party provider internals or external MCP servers ([README.md](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/README.md)).
- Credited operating / distribution surfaces: [swarms/structs/agent.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/agent.py); [swarms/structs/groupchat.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/groupchat.py); [swarms/structs/hiearchical_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/hiearchical_swarm.py); [swarms/structs/majority_voting.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/majority_voting.py); [swarms/structs/conversation.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/conversation.py); [swarms/utils/workspace_manager.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/utils/workspace_manager.py).
- Adjacent first-party surfaces excluded from ownership: experimental prompts not called by runtime, external LLMs, tests/examples, user-managed workers assembled outside the packaged orchestrator, hosted SaaS organization and model vendor governance.
- First-party operating / deployment modes considered: instantiated Agent direct model/tool loop; GroupChat speaker bidding/selection with recency; HierarchicalSwarm model director with dynamic worker orders and optional feedback mode.
- Recursion level: one hosted swarm with independent agents; director/GroupChat facilities govern that bounded set, not every company/team using Swarms.
- Reviewed revision: `3009364a7e44dc3e55fec238b56b3a4fa6949a05`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The package's core `Agent` class implements first-party model-driven action and its own loop, including autonomous continuation and tool invocation. `HierarchicalSwarm` configures a director agent to parse task orders, dispatch to specialized worker agents, collect results and optionally iterate with a distinct feedback director when enabled. These are shipped operational functions, not just the class names or demo topology ([swarms/structs/agent.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/agent.py); [swarms/structs/hiearchical_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/hiearchical_swarm.py); [README.md](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/README.md)).
In the separate `GroupChat` mode each independently executing agent generates a model-based speaking bid with a proposed reply. The first-party coordinator computes a deterministic highest permitted bid after recency adjustments and threshold enforcement, posts **one** response to the shared conversation, and this updated history becomes the next round's input for all agents. Recency specifically attenuates monopolization of the shared conversation floor by one operating unit. This is a distinct, scoped cross-agent contention-control relation implemented by the host rather than an agentic policy decision ([swarms/structs/groupchat.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/groupchat.py); [swarms/structs/conversation.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/conversation.py)).
Swarms includes standalone consensus/judge helpers and hierarchical feedback stages; their distinct prompts/models do not by themselves show a guaranteed independently sourced audit over primary operational artifacts rather than producer reports ([swarms/structs/majority_voting.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/majority_voting.py); [swarms/structs/hiearchical_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/hiearchical_swarm.py); [swarms/structs/heavy_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/heavy_swarm.py)).

## Operational model
The deployed agent can act on task inputs, observe tool/model feedback and continue. In conversational multi-agent mode the GroupChat host lets competing agent speakers bid for shared attention and gates which single contribution is published, which changes peers' next observations. In hierarchical mode the model director creates current work orders for separately operating specialists and can re-evaluate results in later loops. Static configuration and audit-like prompts are not credited as full higher VSM functions without their closure.

## S1 — Operations
- State: A
- Function: Model-directed individual first-party Agent solves a task via model/tool choice, observation and iterative continuation.
- Disturbance / variety regulated: Dynamic goals, changing tool outcomes, external model output, context and task errors.
- Decisive decision or feedback right: Choose steps, call tools/subagents and decide when to continue or finish an operating task.
- Decision owner: Per-agent hosted LLM/Agent runtime, not merely an agent-shaped tuple invoked by a deterministic sequencer.
- Supporting / enforcement mechanisms: Agent `_run`, `_run_autonomous_loop`, tool executor, model wrapper and workspace.
- Closure path: Task → model-generated action/tool use → environment result → next model reasoning and eventual completion.
- Boundary reachability: Python `Agent.run` and optional autonomous-loop configuration are used from the published distribution ([README.md](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/README.md); [swarms/structs/agent.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/agent.py)).
- Why this is / is not agent-owned: Context-sensitive model actions select operating acts; loop counters and provider wrappers do not own that choice.
- Evidence: [swarms/structs/agent.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/agent.py); [README.md](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/README.md).
- Basis: structural
- Confidence: high
- Caveats: Runtime behavior established by source, not live model-backed benchmark execution.

## S2 — Coordination
- State: C
- Function: In bounded GroupChat mode, mediate multiple model-agent bids competing for a single shared conversational speaking slot, preventing speaker domination while retaining useful contributions.
- Distinct S1 units: A configured `GroupChat.agents` set of independently invoked `Agent` objects, each producing a context-contingent `(score, reply)` via model-backed `respond` tool.
- Inter-S1 disturbance: Several operating agents seek the same shared conversation floor simultaneously; unchecked publication produces competing turns, and repeated high-frequency speakers dominate the shared information channel.
- Attenuating coordination relation: `_collect_bids` calls each agent, `_select_speaker` applies a shared threshold and recency penalty, chooses exactly one speaker, and `_post` updates common conversation history seen by all peers on the next turn.
- Feedback into subsequent S1 behaviour: The selected speaker's contribution, not all conflicting bids, enters shared history for every agent's following model turn; recent speakers are penalized in future selections.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The explicit gate is driven by simultaneous claims to a scarce common conversational medium and recurring dominance, with a fairness attenuation policy and returned altered information environment.
- Disturbance / variety regulated: Conflicting simultaneous bids, message crowding and disproportionate conversational control.
- Decisive decision or feedback right: Select exactly one admissible turn among competing agent contributions.
- Decision owner: First-party deterministic GroupChat floor arbiter, therefore `C`, not a separate agentic S2 decision owner.
- Supporting / enforcement mechanisms: `respond(score,message)` tool, threshold, recency window/penalty, chosen-speaker posting and shared Conversation.
- Closure path: Independently formed bids → contention/fairness gate → one allowed published contribution → next turn's changed conversation and adjusted future bids.
- Boundary reachability: `GroupChat.run` uses the packaged bidding, selecting and posting operations; this is an opt-in published architecture, not an inactive helper ([swarms/structs/groupchat.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/groupchat.py); [README.md](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/README.md)).
- Why this is / is not agent-owned: Agents determine proposed content and scores; the decisive inter-agent floor grant is deterministic host policy (`C`).
- Evidence: [swarms/structs/groupchat.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/groupchat.py); [swarms/structs/conversation.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/conversation.py); [README.md](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/README.md).
- Basis: structural
- Confidence: medium
- Caveats: Applies to GroupChat's shared conversation medium, not arbitrary shared file changes or all Swarms topologies. Does not claim broad resource conflict arbitration.

## S3 — Inside-and-now control
- State: A
- Function: Model-led HierarchicalSwarm director assigns present worker orders and adjusts ongoing team work from collected subordinate results.
- Disturbance / variety regulated: Divergent worker progress/results, uncertain task division, errors and changing completion quality.
- Decisive decision or feedback right: Produce a model-derived order batch, choose which specialist performs what, inspect returned outputs and issue fresh orders in further loops.
- Decision owner: First-party configured model `director`; deterministic `parse_orders` and `execute_orders` relay its decisions.
- Supporting / enforcement mechanisms: HierarchicalSwarm director, OrderBatch parser, worker dispatch and optional feedback director, conversation storage.
- Whole-system current view: Director sees the bounded swarm conversation/worker results and prior execution history, not every organization using Swarms.
- Current-control decision scope: Current worker allocation, ordering, revisions and reattempts for the HierarchicalSwarm instance.
- Closure path: Director plans and orders → specialized workers run → results return and enter conversation → director next loop reassigns/replans.
- Boundary reachability: `HierarchicalSwarm.run` calls `step`, `run_director`, `parse_orders`, `execute_orders`, and loops over result feedback when max_loops allows ([swarms/structs/hiearchical_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/hiearchical_swarm.py)).
- Why this is / is not agent-owned: Actual work orders originate in a model-led director within the shipped topology; loop counters and dispatcher enforce, not replace, task choices.
- Evidence: [swarms/structs/hiearchical_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/hiearchical_swarm.py); [README.md](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/README.md).
- Basis: structural
- Confidence: high
- Caveats: Optional hierarchical mode scoped to one instantiated swarm; a sequential workflow or router alone is not credited as S3.

## S3* — Complementary audit
- State: ?
- Function: Some prebuilt modes include judge/verification or consensus phases; materially independent operating evidence inspection and correction path remains unresolved.
- Disturbance / variety regulated: Invalid subordinate claims, low-quality task completion or conflicting agent assertions.
- Decisive decision or feedback right: Judge can evaluate outputs; whether it has independent primary-source evidence and authority over correction is not guaranteed.
- Decision owner: Configured judge/consensus agent, not established as a truly separately observing auditor.
- Supporting / enforcement mechanisms: Hierarchical judge toggle, MajorityVoting consensus and HeavySwarm verification-oriented roles.
- Claim being audited: Specialist worker answer/output claims.
- Ordinary reporting path: Worker results added to director conversation, majority-voting conversation or final report.
- Complementary access path: Shipped judging paths chiefly pass worker outputs/derived conversation text; a separate direct observation of work artifacts has not been established at the first-party boundary.
- Independence boundary: A different model/persona is not a guaranteed independent observations channel.
- Who acts on findings: Directors or consensus can summarize and reconsider, but an independent audit finding → corrective operational reroute is unproven.
- Closure path: Output → judge/consensus verdict → report or next loop, insufficient to classify a distinct S3* audit under the governing method.
- Why this is / is not agent-owned: Another LLM rating peer output is not equivalent to a complementary function sampling reality independently.
- Evidence: [swarms/structs/hiearchical_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/hiearchical_swarm.py); [swarms/structs/majority_voting.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/majority_voting.py); [swarms/structs/heavy_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/heavy_swarm.py).
- Basis: unknown
- Confidence: low
- Caveats: Inspect optional judge access to tools/external ground truth and exact source-backed correction route before any positive or bounded absence.

## S4 — Outside-and-then intelligence
- State: ?
- Function: Planning prompts, persistent workspace and memory may help later tasks but a decision owner adapting future systemic capability from external prospective observations has not been established.
- Disturbance / variety regulated: Future requirements, market or environment shifts and changing task complexity.
- Decisive decision or feedback right: Unresolved among user-supplied swarm config, model director and persisted task memory.
- Decision owner: No uniquely identified first-party outside-and-then intelligence controller at the bounded swarm recursion.
- Supporting / enforcement mechanisms: Conversation/workspace storage, planning role prompts, dynamic agent layouts.
- External distinction: Outside facts can enter model context, but information access alone is not S4.
- Future / prospective distinction: Multi-loop plans address current task commitments, not shown to adapt future organization capability.
- Adaptation option generated: No verified capability-evolution choice produced by a distinct owner.
- Path back into current capability / S3: Persistence and plan prompts can affect later runs, but external foresight → applied organizational redesign remains unresolved.
- Closure path: Retained context → later work, incomplete future-intelligence and capability-change loop.
- Why this is / is not agent-owned: Prompted planning and memory are not enough for S4.
- Evidence: [swarms/structs/hiearchical_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/hiearchical_swarm.py); [swarms/utils/workspace_manager.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/utils/workspace_manager.py); [swarms/structs/agent.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/agent.py).
- Basis: unknown
- Confidence: low
- Caveats: Agent self-building or marketplace features require a separate source-level prospective-adaptation closure analysis.

## S5 — Policy and identity
- State: ?
- Function: Configured swarm identity, roles and execution limits exist but an ultimate organizational purpose/policy closure is not traced.
- Disturbance / variety regulated: User boundaries, acceptable agent/tool behavior and system-level authority.
- Decisive decision or feedback right: Developer/user chooses prompts, members and parameters; no proven ultimate-policy choice by a qualified first-party actor.
- Decision owner: User-supplied configuration for role identity and deterministic safety checks; a complete parent policy mode remains unresolved.
- Supporting / enforcement mechanisms: system prompts, task role configuration and tool/platform restrictions.
- Identity / ultimate-policy issue: Who chooses and revises the organization's overarching identity, purpose and final authority.
- Ultimate authority in each claimed mode: Not established beyond out-of-band user/developer configuration.
- Return-to-operation path: Prompt and parameter selection guides run behavior, but no complete governing policy feedback is proven.
- Closure path: Configured goals/roles → worker execution; no verified policy challenge/ultimate revision returned to operations.
- Why this is / is not agent-owned: A system prompt or fixed role roster is not itself an ultimate decision loop.
- Evidence: [swarms/structs/hiearchical_swarm.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/hiearchical_swarm.py); [swarms/structs/groupchat.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/groupchat.py); [swarms/structs/agent.py](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/agent.py).
- Basis: unknown
- Confidence: low
- Caveats: Optional Swarms management patterns should be assessed under concrete authority and identity closure before credit.

## Recursion
The individual Swarms `Agent` is an operating unit (S1). GroupChat arbitration coordinates competing speaking requests from independent S1 units at its own message-sharing recursion (S2=C), while a separately configured hierarchical director exercises current task allocation and feedback (S3=A). These are distinct first-party modes; the framework is a reusable library and no single unconditional deployment combines every shipped topology.

## Variety and escalation
Independent agents perform dynamic tasks via model/tool outcomes. In GroupChat, deterministic recency-based floor selection attenuates contention and shapes next-turn inputs. In HierarchicalSwarm, model-generated orders allocate tasks and react to worker feedback. Neither multiple worker opinions, independent model calls for scoring nor persistent conversations automatically demonstrate S3*, S4 or S5.

## Evidence gaps
Primary-source static inspection at original frozen commit only. S2 is intentionally scoped to GroupChat, not claimed for all possible configurations. Materially independent auditor source access for S3*, future capability adaptation for S4 and ultimate policy authority/return for S5 are not proved, so these remain `?` rather than unsupported positives or universal negatives.
