---
harness_id: peristyle-harness
project_name: Peristyle Harness
repository: https://github.com/peristyle-ai/harness
review_ref: cfa54f2c808058d2372521c53019f6f3e4b5a52c
reviewed_at: 2026-11-01
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
autonomy_s5: P
---

# Peristyle Harness

## Review boundary

- System in focus: the shipped self-hosted Flask/PostgreSQL multi-agent harness with its installed agent roster, per-agent model/tool loop, per-schema memory, browser/REST chat, group conversations, and optional nightly reverie.
- Purpose and identity: help an operator run named, persistent tool-using language-model agents on one machine, with an agent identity and conversations surviving turns.
- Relevant environment: operator and chat users, hosted/local LLM and embedding APIs, shell/filesystem, PostgreSQL, group transcripts, scheduled timer, and machine services.
- Standard-distribution boundary: the normal config.yaml installation and Flask app, agent loop, tool registry, group-chat dispatcher, protected identity files and optional configured reverie; not merely examples, tests, future integrations or a third-party model provider.
- Credited operating / distribution surfaces: [app/agent/loop.py#L667-L755](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L667-L755), [app/agent/group_chat.py#L141-L273](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/group_chat.py#L141-L273), [app/agent/reverie.py#L135-L305](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/reverie.py#L135-L305), [app/routes/api.py#L376-L539](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/routes/api.py#L376-L539), [app/agent/bootstrap.py#L101-L155](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/bootstrap.py#L101-L155), [app/agent/tools/exec_bash.py#L229-L256](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/tools/exec_bash.py#L229-L256).
- Adjacent first-party surfaces excluded from ownership: contributor workflows, PR-agent automation, test scripts, diagnostic admin views, packaging, operator's external GitHub/operating organization, and decisions of the model/embedding vendors. These can support claims but are not an autonomous upper-level actor in the running install.
- First-party operating / deployment modes considered: ordinary named-agent chat, mentioned-agent group chat, scheduled/forced reverie when enabled, with or without optional operator-mode sudo; per-agent model overrides and operator-held policy files.
- Recursion level: one deployed harness with multiple named agent S1s and a legitimate human operator for ultimate identity/policy rights; each individual LLM/tool cycle is a lower operational unit. Do not count public OSS contributors as a running metasystem.
- Reviewed revision: cfa54f2c808058d2372521c53019f6f3e4b5a52c; exact source checkout.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Flask/API entry points dispatch a named agent to AgentLoop; its per-agent registry supplies bootstrap identity, LLM adapter and Postgres-backed memory. The streaming loop persists a user turn, composes identity/history/memory, calls an LLM, executes tool calls, appends tool results, and persists assistant output and trajectories. Tools cover shell execution, SQL, memory CRUD and file attachment; safety classification, protected-file checks, turn caps, context trimming and concurrent-call limits condition execution ([app/agent/loop.py#L758-L829](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L758-L829), [app/agent/loop.py#L910-L1020](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L910-L1020), [app/agent/tools/exec_bash.py#L1-L33](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/tools/exec_bash.py#L1-L33), [app/agent/memory.py#L392-L452](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/memory.py#L392-L452)).

Each named agent has a schema and identity; group chat parses @mentions, records a canonical transcript, runs each mentioned agent serially and feeds earlier agents' replies into the later agent's next prompt. This is a real multi-agent interaction and order control, but its specific contract is routing/transcript consistency rather than a demonstrated interference/oscillation attenuator ([app/agent/group_chat.py#L1-L29](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/group_chat.py#L1-L29), [app/agent/group_chat.py#L141-L273](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/group_chat.py#L141-L273)).

An optional nightly systemd-triggered reverie is an ordinary persisted agent turn. It measures memory/identity pressure, can unpin/shorten agent-held context, and emits reflection/proposals in the human user's chat. SOUL.md is treated differently: the scheduled maintenance brief explicitly reserves changes to user permission, the shell tool rejects writes to configured protected paths in that mode, and an operator can edit identity on disk for next-turn reload ([app/agent/reverie.py#L135-L305](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/reverie.py#L135-L305), [app/routes/api.py#L491-L534](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/routes/api.py#L491-L534), [app/agent/bootstrap.py#L101-L155](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/bootstrap.py#L101-L155)).

## Operational model

Operational value is produced by the named agents' model-selected tool use, with observed tool/DB results closing into later steps. The harness also coordinates group transcript order, but no S2-specific interference witness was established; operational limits are mostly deterministic and do not constitute autonomous S3. The protected ultimate-policy path is deliberately parent-governed: an agent can raise a SOUL.md change proposal, the human operator has the decisive right, and a permitted file change returns through the next-turn identity prompt. This is a bounded, optional first-party parent mode and is not a claim that an LLM autonomously sets ultimate policy.

## S1 — Operations

- State: A
- Function: perform requested chat, research, memory and machine tasks through an adaptive sequence of model-chosen tool calls.
- Disturbance / variety regulated: variable user requests and unexpected shell, SQL, memory and API results.
- Decisive decision or feedback right: each named LLM agent chooses its next tool, arguments, continuation or answer using prior observations.
- Decision owner: the instantiated model-driven agent in AgentLoop; not the Flask router, deterministic safety classifier or model provider as an organizational unit.
- Supporting / enforcement mechanisms: per-agent bootstrap/DB isolation, tool schemas, context window, iteration/wall-time limits, semaphore, persisted trajectory and safety confirmations.
- Closure path: tool output is returned into the model's subsequent context; the next action or final text is persisted and delivered to the caller.
- Boundary reachability: the standard Flask chat endpoint and group dispatcher call the shipping AgentLoop directly; this does not depend on development CI or an external agent framework.
- Why this is / is not agent-owned: an autonomous agent has substantive discretion within the user task; deterministic guards and operator confirmation constrain rather than choose those operational actions.
- Evidence: [app/agent/loop.py#L667-L755](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L667-L755); [app/agent/loop.py#L758-L829](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L758-L829); [app/agent/loop.py#L910-L1020](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L910-L1020); [app/agent/tools/registry.py#L1-L120](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/tools/registry.py#L1-L120).
- Basis: explicit / structural.
- Confidence: high for source-reachable execution; no provider-backed E2E.
- Caveats: effectful shell commands can require user confirmation and model availability; those do not imply general agent sovereignty.

## S2 — Coordination

- State: —
- Function: no established S2-specific regulatory loop for interference/oscillation among independently acting named S1s.
- Disturbance / variety regulated: potentially inconsistent multi-agent replies or shared task interference; the repo documents transcript order, not an actual systemic conflict and its corrective regulation.
- Decisive decision or feedback right: none shown for regulating that inter-S1 disturbance; @mention order selects who speaks and whose reply enters later context.
- Decision owner: deterministic group dispatcher, not an autonomous coordination agent.
- Supporting / enforcement mechanisms: roster filter, sequential dispatch, shared transcript, per-agent schemas and history overrides.
- Closure path: previous replies appear in later prompts, but no first-party conflict detection, damping decision, revised joint commitments or stabilization feedback is evidenced.
- Why this is / is not agent-owned: communication and serialization are not S2 solely because distinct agents participate.
- Evidence: [app/agent/group_chat.py#L1-L29](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/group_chat.py#L1-L29); [app/agent/group_chat.py#L46-L76](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/group_chat.py#L46-L76); [app/agent/group_chat.py#L141-L273](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/group_chat.py#L141-L273); [app/agent/loop.py#L713-L755](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L713-L755).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: independently configured agents may cooperate via text, but the standard path lacks a function-specific inter-S1 disturbance witness.
### Absence scope

- Surfaces inspected: group mention parsing, message store, transcript ordering, named-agent memory isolation, streaming dispatch.
- Plausible first-party paths checked: @all group turns, agent-to-agent transcript forwarding, serial execution and per-schema state.
- Why no material first-party path remains: each supplies transport/routing/order rather than a decision relation that detects and attenuates demonstrated inter-S1 oscillation and returns a corrective policy to the units.

## S3 — Inside-and-now control

- State: —
- Function: no discretionary whole-harness current-control loop over its multiple named agents established.
- Disturbance / variety regulated: local model latency, turn duration, memory budget and concurrent LLM demand; regulated by preconfigured enforcement.
- Decisive decision or feedback right: no agent- or parent-owned whole-system tradeoff among running units, priorities, shared budgets and commitments.
- Decision owner: operator preselects config; counters/semaphore, per-turn protection, and guards enforce it without ongoing S3 judgment.
- Supporting / enforcement mechanisms: LLM semaphore, per-turn rate/iteration caps, context trimming, group serial dispatcher, UI agent picker, config per-agent model selection.
- Closure path: a turn is delayed/stopped/trimmed; no observed aggregate present-state feedback reassigns resources or priorities across the agent collective.
- Why this is / is not agent-owned: operator configuration and deterministic scheduling alone do not constitute whole-system S3 ownership.
- Evidence: [app/agent/loop.py#L803-L835](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L803-L835); [app/agent/loop.py#L910-L940](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L910-L940); [app/agent/group_chat.py#L208-L240](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/group_chat.py#L208-L240); [app/config.py#L111-L161](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/config.py#L111-L161).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: an administrator can intervene manually but no first-party ongoing parent-controlled S3 closure was reconstructed.
### Absence scope

- Surfaces inspected: app config, model registry, concurrency/turn guards, group routing, admin diagnostics and operator mode.
- Plausible first-party paths checked: semaphore and max-iteration policy, reverie gating, admin settings and per-agent model overrides.
- Why no material first-party path remains: the shipped paths set or enforce local controls, rather than aggregate multi-S1 state and close discretionary current governance over the system as a whole.

## S3* — Complementary audit

- State: —
- Function: no operationally separate, sufficiently independent audit judgment that feeds corrective control to the operational collective.
- Disturbance / variety regulated: hallucinated tool claims, command safety, faulty turns and other local execution errors.
- Decisive decision or feedback right: no independent audit channel with own access and judgment; most guards inspect the same generated text/tool inputs.
- Decision owner: deterministic runtime rules and human-facing diagnostics, rather than a distinct audit actor.
- Supporting / enforcement mechanisms: intent-without-execution nudges, protected path detection, shell audit log, last-prompt/last-emission admin routes and interruption recording.
- Closure path: error nudges can return to the same operational agent; diagnostics can inform an operator, but neither is independent operational-reality audit/feedback into parent control.
- Why this is / is not agent-owned: observing or blocking an agent's own proposed command is not complementary independent audit.
- Evidence: [app/agent/loop.py#L49-L164](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/loop.py#L49-L164); [app/agent/tools/exec_bash.py#L1-L33](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/tools/exec_bash.py#L1-L33); [app/routes/api.py#L945-L1006](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/routes/api.py#L945-L1006); [app/agent/turn_guard.py#L159-L282](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/turn_guard.py#L159-L282).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: operator log review is possible outside the automatic harness path.
### Absence scope

- Surfaces inspected: LLM output nudges, shell safety/audit logs, admin inspection routes, tool and turn guards, group transcript.
- Plausible first-party paths checked: cross-checking actual effects, independent auditor turn or private reality feed, aggregate anomaly report returned to controller.
- Why no material first-party path remains: these are local validation and visibility surfaces; no complementary independent assessor with corrective feedback is wired into the deployed standard flow.

## S4 — Outside-and-then intelligence

- State: —
- Function: no established externally sensing, future-oriented adaptation loop changing the harness's capabilities.
- Disturbance / variety regulated: recurring memory pressure and recent-turn friction, which are internal context-maintenance phenomena.
- Decisive decision or feedback right: reverie makes local memory cleanup choices and suggests future proposals; no first-party external opportunity/threat judgment is adopted into capability strategy.
- Decision owner: agent controls cleanup; any wider changes remain future user requests and manual work outside a demonstrated S4 closure.
- Supporting / enforcement mechanisms: nightly timer, activity gate, last-50-turn reflection, file/memory targets, report to user.
- Closure path: local context is tidied and next-turn bootstrap refreshed; this improves operational continuity, not outside-and-then adaptation of the system's repertoire. Proposed future work has no provided adoption/implementation loop.
- Why this is / is not agent-owned: reflecting, optimizing internal memory and generating proposals does not alone establish S4.
- Evidence: [app/agent/reverie.py#L1-L45](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/reverie.py#L1-L45); [app/agent/reverie.py#L135-L305](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/reverie.py#L135-L305); [app/agent/reverie.py#L396-L428](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/reverie.py#L396-L428); [app/routes/api.py#L376-L539](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/routes/api.py#L376-L539).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: operator-directed future upgrades might create an S4 organization, but are not evidenced as standard-distribution closure.
### Absence scope

- Surfaces inspected: reverie planning/brief/route, optional identity prompts, memory lifecycle, timer, config and group communication.
- Plausible first-party paths checked: reflective proposals, operator task lists, self-edit of non-protected identity, external model selection.
- Why no material first-party path remains: reviewed loops regulate internal attention/context or expose operator choices; they do not independently sense external futures, select adaptation options, and return adopted change to present capability.

## S5 — Policy and identity

- State: P
- Identity / ultimate-policy issue: whether the installed agent's core SOUL.md behavioral constitution may be changed during unattended maintenance.
- Ultimate authority in each claimed mode: the legitimate human operator alone in the configured reverie parent-governed mode; no autonomous S5 mode is claimed.
- Return-to-operation path: operator-approved protected identity edit is reread by BootstrapRegistry before the next agent turn and injected into the model's bootstrap policy.
- Function: reserve ultimate agent identity and protected policy changes to the human operator while allowing the running agent to surface a proposal.
- Disturbance / variety regulated: pressure to let a self-maintaining agent rewrite its own core behavioral boundaries during an unattended nightly turn.
- Decisive decision or feedback right: approve/reject or make the authoritative change to the protected SOUL.md core rules; the agent must propose rather than execute that change in reverie.
- Decision owner: human user/operator as legitimate parent; the agent can identify and report a proposed change but does not own that ultimate right in this mode.
- Supporting / enforcement mechanisms: protected_files config, reverie brief/system-scope, exec_bash write block, persisted chat report and BootstrapRegistry refresh.
- Closure path: reverie raises identity proposals in the operator's main conversation; operator may grant permission and edit the protected file; the standard bootstrap loader rereads it at the next turn and injects the changed rules into subsequent agent decisions. A rejected/no-change proposal leaves existing policy in force.
- Boundary reachability: this parent-governed mode is shipped in the normal optional reverie route, standard shell tool and next-turn bootstrap reload; the core SOUL.md is an installed identity file. No external plugin, contributor workflow or imagined parent process is required.
- Why this is / is not agent-owned: the protected path explicitly removes unilateral agent authority on identity, while the operator controls whether policy changes and the live runtime consumes the resulting identity.
- Evidence: [agent_template/SOUL.md.template#L1-L51](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/agent_template/SOUL.md.template#L1-L51); [app/agent/reverie.py#L279-L295](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/reverie.py#L279-L295); [app/routes/api.py#L491-L518](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/routes/api.py#L491-L518); [app/agent/tools/exec_bash.py#L229-L256](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/tools/exec_bash.py#L229-L256); [app/agent/bootstrap.py#L101-L155](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/bootstrap.py#L101-L155); [app/agent/bootstrap.py#L275-L301](https://github.com/peristyle-ai/harness/blob/cfa54f2c808058d2372521c53019f6f3e4b5a52c/app/agent/bootstrap.py#L275-L301).
- Basis: explicit / structural parent-governed closure.
- Confidence: medium for the supported path; no observed real operator acceptance or production E2E claimed.
- Caveats: this P claim is restricted to the protected identity-policy path in configured reverie mode, not all arbitrary user prompts, ordinary confirmation requests, static safety rules or OSS governance. The manual operator approval/edit step is the parent decision; mere editing ability without the shipped escalation/return chain would not suffice.

## Distributed OSS parent arrangement

Public contributors, PR-agent automation, CI and install scripts do not establish a distributed parent S3/S4/S5 for operators' deployed private runtimes. The S5 parent owner counted here is the legitimate operator/user of a specific installed harness, not the GitHub contributor community.

## Self-hosted and non-human modes

The supported standard deployment is self-hosted and can enable named-agent group chat and nightly reverie. Operator mode changes Unix command permission bounds but does not transfer ultimate identity-policy authority to the model. A fully non-human metasystem is not shown; optional parent-governed S5 is a distinct deployment/turn mode, not co-ownership with an autonomous S5.

## Recursion

Named agents and their per-schema memories are lower-level S1 units within the installed harness; serial group transcript exposure is a communication path. Re-running a model loop, nesting tool calls or adding schemas is not itself proof of higher VSM recursion. The assessed collective does not inherit its operator's other organizations.

## Variety and escalation

User/machine variety is handled by model tool decisions, memory lookup, bounded context and output feedback. Turn interruption, wall-time limits and shell confirmation are local operational safety. The reverie protected-policy exception is reported to the legitimate user instead of auto-edited. None of these error/queue surfaces is separately asserted to be an algedonic channel without evidence of exceptional whole-system escalation.

## Evidence gaps

No live paid model, Postgres deployment or model-provider E2E was run. The path for a user's real-world acceptance/edit of a particular SOUL.md proposal is structurally evidenced but not observed; hence S5 confidence is bounded. The absence conclusions cover this checked first-party revision and supported modes, not any custom external agent composition.
