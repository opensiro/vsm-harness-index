---
harness_id: the-harness
project_name: the-harness
repository: https://github.com/EvolvingLMMs-Lab/the-harness
review_ref: 2aa4105ce8c8ab143be95969fb1cc5944248e8fd
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# The Harness

## Review boundary

- System in focus: the installable first-party Python task/control runtime and its supported native sub-agent, computer/workspace and learning modes.
- Purpose and identity: turn natural-language goals into ongoing environment work, retaining tested experience where explicitly enabled.
- Relevant environment: user tasks and changes, model providers, computer/browser/workspace state, shared input/windows, optional remote tools and bound knowledge library.
- Standard-distribution boundary: src/harness runtime/core/builtin roles/skills, first-party CLI/session host, computer/workspace packages and optional persistent agent package.
- Credited operating / distribution surfaces: TaskRun/kernel program feedback; native agents/review skill and delegation; computer input/window coordination; session tree/control routes; runtime learning proposal, staged verification and activation.
- Adjacent first-party surfaces excluded from ownership: benchmark scores, eval/self-improve development-seed experiments, developer/CI/test organization, and internal reasoning/governance of externally hosted Claude Code/Codex agents. Ordinary camera verify and own-test checks are not borrowed as S3*.
- First-party operating / deployment modes considered: CLI/API/session host; native sub-agents when session.agents is enabled; computer package with shared resources; optional operator session oversight; explicit bound learning library including nonphysical own_test admission. Core-only/frozen modes do not imply every positive path is active.
- Recursion level: one task/session organization with native work cells and local operator parent; no project-wide governance or universal recursive viability inferred.
- Reviewed revision: `2aa4105ce8c8ab143be95969fb1cc5944248e8fd`.
- Observation date: 2026-11-19.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The main model writes Python programs, waits or answers. Programs run as units; an event/notice queue returns results, interruptions and current active-unit information while longer work may continue. Worker adapters execute environment commands under safety/approval constraints. Reactive rules can act between model calls; scheduling and deterministic checks are support rather than automatic regulatory owners. TaskRun retains context and traces across turns.

The shipped agents skill starts separate native TaskRuns with bounded workspaces/budgets, returns turn reports, forwards additional messages and cancels work. Computer workers coordinate actual shared input/window ownership. Session APIs expose the tree and usage and let the operator end selected work. The dedicated review helper supplies a separate critical code-reading role. Library learning is optional: the model proposes notes/skills/rules for future work; the host checks exact revisions and activates eligible entries at program boundaries. The optional agent package adds persistent dialogue identity/private facts, not an evidenced ultimate-policy resolver.

Primary references: [TaskRun](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/run.py), [installed main role](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/core/core.md), [Agents and REVIEW](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/skills/agents/__init__.py), [installed delegation/review guide](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/shared/agents.md), [native delegation/usage/transfer](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/delegation.py), [input queue/window ownership](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/computer/harness_computer/coordination.py), [owner-aware refusal](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/computer/harness_computer/shield.py), [session control routes](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/host/http.py), [session tree/aggregate usage](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/host/sessions.py), [learning guide](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/shared/learning.md), [prospective practice goal](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/shared/learning-goal.md), [Learner admission/demotion](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/learning/learner.py), [library proposal API](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/skills/learning/__init__.py), [active learning setup](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/learning/active.py), [CLI learn/library mode](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/cli.py), [optional persistent identity](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/agent/harness_agent/state.py), [identity dialogue role](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/agent/harness_agent/session.py).

## Operational model

Native main/child task models are S1 units. The same parent model can also regulate collective commitments/resources and respond to shared-window conflicts; this does not require six named processes. Model-owned adaptation and audit are distinct from admission tests and worker guards. Operator session control is a separate parent S3 mode, not S5. Default-disabled subagents or frozen learning do not negate reachable supported optional modes, nor establish them in an arbitrary run.

## S1 — Operations

- State: A
- Function: turn natural-language tasks into programs that act in a connected environment and revise work after outcomes.
- Disturbance / variety regulated: changing environment state, program/tool failures and task-specific unknowns.
- Decisive decision or feedback right: select the next program, wait, recovery or task answer after observing results.
- Decision owner: installed main model, and native child models for their bounded outcomes.
- Supporting / enforcement mechanisms: Python kernel, worker adapters, execution units, notice queue, safety checks, traces and provider transport.
- Closure path: TaskRun delivers program/child/event results to the model; new programs act on the observed difference.
- Boundary reachability: harness CLI/API creates the first-party TaskRun and core role; optional computer/browser/workspace packages provide environments. Native child reasoning is supplied by this runtime, not borrowed from external-agent adapters.
- Why this is / is not agent-owned: model-authored programs and continuation decisions are discretionary; worker execution and guardrails enforce those decisions without choosing the task solution.
- Evidence: [TaskRun](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/run.py), [installed main role](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/core/core.md), [CLI learn/library mode](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/cli.py), [native delegation/usage/transfer](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/delegation.py)
- Basis: structural.
- Confidence: high.
- Caveats: live model/environment execution was not performed; supported opt-in modes are capability claims, not statements about every default installation.

## S2 — Coordination

- State: A
- Function: mutually adjust use of shared computer input and windows among native operational agents.
- Disturbance / variety regulated: two sessions/children can issue physical input into one desktop or act in a window another agent currently owns.
- Decisive decision or feedback right: choose another window, wait for its owner, or deliberately transfer owned windows to a child and resume after return.
- Decision owner: the native model(s) receiving owner-specific refusal and choosing the follow-on response; the parent model chooses the explicit share handover.
- Supporting / enforcement mechanisms: machine-wide fair InputLock, WindowOwners, command shield, workspace separation and transfer/return enforcement.
- Closure path: a conflicting command has no effect and returns the owner/reason to the model; subsequent programs choose an alternate/wait. share transfers the window away from the parent and back after the child's turn.
- Boundary reachability: the computer package installs these guards; agents-enabled native delegation offers workspace=new/share and binds transfer to actual child turns. No custom coordination actor is required.
- Why this is / is not agent-owned: the lock alone is deterministic support. A specifically reported ownership conflict reaches an already installed model with different supported lawful responses; that discretionary response is absent if the actor is removed. This is stronger than inferring ownership from serialization alone.
- Evidence: [input queue/window ownership](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/computer/harness_computer/coordination.py), [owner-aware refusal](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/computer/harness_computer/shield.py), [native delegation/usage/transfer](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/delegation.py), [computer delegation instructions](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/computer/prompts/computer/agents.md), [TaskRun](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/run.py)
- Basis: structural.
- Confidence: high.
- Caveats: A is bounded to native agent operation in the supported computer/agents mode, not arbitrary external-agent internals. No live collision experiment was run.

- Distinct S1 units: native main/child task agents or independently running native sessions using the same computer.
- Inter-S1 disturbance: shared real mouse/keyboard and an already owned window can be targeted by another S1.
- Attenuating coordination relation: fair input turns, exclusive window ownership with model-visible refusal, explicit parent→child handover and return.
- Feedback into subsequent S1 behaviour: rejected input reports whose window it is and asks the agent to work elsewhere or wait; transferred resources become unavailable to the parent until returned.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the implementation names the conflicting resource/owner and couples exclusion, alternative action and handover to later agent behavior; merely starting a child is not the witness.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the current session's collective work and spending, with a distinct operator current-control mode.
- Disturbance / variety regulated: concurrent work consumes one parent allowance, becomes slow/stuck or needs commitments redirected/stopped.
- Decisive decision or feedback right: base: choose child resource envelopes and continue, redirect or cancel current children/units from their reports; parent: inspect the live session tree/usage and stop a selected agent or the session.
- Decision owner: base: native parent model. Parent mode: the authenticated local operator controlling its session through the first-party host.
- Supporting / enforcement mechanisms: hierarchical usage charging, bounded budgets, per-unit status/elapsed/output feedback, session registry and cancellation/stop enforcement.
- Closure path: child status/usage and active-unit feedback return to the parent model, which can send further work or cancel and choose another allocation; operator stop closes selected live conversations and returns stopped agent IDs.
- Boundary reachability: the installed agents guide exposes budgets/wait/send/cancel, native delegation binds them to real TaskRuns, and the session host exposes aggregated current usage plus targeted stop. Ordinary action approvals are not the parent witness.
- Why this is / is not agent-owned: the model/operator selects the intervention; budget clipping, charging and process termination only enforce it. This is current collective resource/commitment regulation, not the name of a manager or initial task decomposition.
- Evidence: [installed delegation/review guide](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/shared/agents.md), [native delegation/usage/transfer](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/delegation.py), [TaskRun](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/run.py), [installed main role](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/core/core.md), [session tree/aggregate usage](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/host/sessions.py), [session control routes](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/host/http.py)
- Basis: structural.
- Confidence: high.
- Caveats: model-controlled child regulation is an agents-enabled mode. The operator parent path is source-reconstructed local session control, not governance over all independent installations.

- Whole-system current view: base sees active units and child reports/status/spend charged to the shared parent allowance; parent sees the complete session agent tree, per-agent state/usage and aggregate calls/cost.
- Current-control decision scope: bounded child budgets, current commitments and cancellation/redirection; parent can end one selected current agent or the whole session.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Native parent model | Current child/unit reports, elapsed work, errors and shared remaining allowance | Budgeted delegation, send_agent or cancel_agent changes subsequent collective work/spend | [installed delegation/review guide](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/shared/agents.md), [native delegation/usage/transfer](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/delegation.py), [TaskRun](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/run.py) |
| Parent (`P`) | Local session operator | Inspection of session tree, live states and aggregate usage | POST /api/sessions/stop closes selected conversations, sub-agents first, and reports stopped IDs | [session tree/aggregate usage](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/host/sessions.py), [session control routes](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/host/http.py) |

## S3* — Complementary audit

- State: A
- Function: challenge whether retained operational code will work as claimed through a separately prompted source-inspecting reviewer.
- Disturbance / variety regulated: the code author's ordinary successful execution/report can omit a failure, wrong effect or expensive behavior.
- Decisive decision or feedback right: independently identify defects in supplied code against its purpose and primary called source/documentation, returning findings to the producing model.
- Decision owner: native review sub-agent owns the audit judgment; the parent operational model decides corrective follow-up.
- Supporting / enforcement mechanisms: review(code,purpose), fresh child conversation/workspace, native model dispatch and wait_agents result delivery.
- Closure path: the reviewer reports defects and evidence, its turn/report reaches the parent as a unit-end notice; wait_agents retrieves it and send_agent/new programs can implement correction.
- Boundary reachability: the agents skill registers a dedicated review helper and REVIEW role text, with the installed guide directing its use for code kept and relied on. Native delegation and report return are wired when agents are enabled.
- Why this is / is not agent-owned: the witness is a specific review path, not generic child creation. It sees code/purpose and can inspect the called source/docs without the author's conversation or conclusions; deterministic return machinery does not own its judgment.
- Evidence: [Agents and REVIEW](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/skills/agents/__init__.py), [installed delegation/review guide](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/shared/agents.md), [native delegation/usage/transfer](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/delegation.py), [TaskRun](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/run.py)
- Basis: structural.
- Confidence: high.
- Caveats: claim-relative independence is contextual, not a different provider guarantee. The caller chooses which code to submit; coverage is not universal. Routine expect/check, the camera verifier and own-test admission are not credited as independent audit.

- Claim being audited: correctness/fitness and resource behavior of code proposed to be kept and relied on.
- Ordinary reporting path: the author model's programs, local checks and task-result reports.
- Complementary access path: the dedicated reviewer reads the actual code, purpose and primary called source/documentation, rather than only a production success report.
- Independence boundary: a fresh native child has not seen the author's conversation; REVIEW asks for critical judgment rather than reproducing the author's conclusion.
- Who acts on findings: parent model receives the returned report through native notices/wait_agents and may revise its operational code; no automatic successful audit is asserted.

## S4 — Outside-and-then intelligence

- State: A
- Function: learn the external environment for future work and turn prospective failure distinctions into reusable present capability.
- Disturbance / variety regulated: unfamiliar external controls/workflows and harder future cases that the current library cannot handle.
- Decisive decision or feedback right: identify missing capabilities and likely failure situations, design/test an adaptive skill/rule/note and retain or revise the option for later programs/runs.
- Decision owner: the installed learning-enabled model owns adaptive option selection; host fixtures/own-test admission enforce the configured trust boundary.
- Supporting / enforcement mechanisms: explicit bound library, practice goal/learning guide, proposal API, staged exact revisions, proof receipts, activation between programs, reuse and failure-driven demotion.
- Closure path: observed environment differences inform model proposals/tests; admitted exact revisions activate in the live kernel and later prompts, remain in the library for later runs, and recorded failures can demote own-tested entries.
- Boundary reachability: CLI --learn/--library and learning-while-working supply this first-party mode; TaskRun assembles the learning goal and host-side staged verification/activation. A nonphysical supported own_test mode closes executable admission without an external custom verifier.
- Why this is / is not agent-owned: this is not credited from memory or learning labels: the supplied role explicitly models hardest expected future cases and failures in an external environment, develops alternatives and changes reusable capability. Model selection is distinct from deterministic admission and rollout enforcement.
- Evidence: [CLI learn/library mode](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/cli.py), [prospective practice goal](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/shared/learning-goal.md), [learning guide](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/prompts/shared/learning.md), [active learning setup](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/learning/active.py), [library proposal API](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/builtin/skills/learning/__init__.py), [Learner admission/demotion](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/learning/learner.py), [TaskRun](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/task/run.py)
- Basis: structural.
- Confidence: high.
- Caveats: learning is off/frozen unless enabled. Default fixture admission can leave executable proposals pending when no compatible fixture exists; A is supported by the separately shipped nonphysical own_test mode and admitted non-code knowledge, not fabricated success under missing fixtures. Environment practice is domain-specific adaptation, not evidence of universal strategic competence.

- External distinction: observed controls, workflow behavior and failure conditions of the connected environment, not merely token history.
- Future / prospective distinction: hardest forms expected in later work, what may happen faster than deliberation, and later programs/runs starting with the retained library.
- Adaptation option generated: model-authored tested skill, reactive response or environment note addressing the newly identified capability gap.
- Path back into current capability / S3: TaskRun stages, verifies and commits an eligible exact library revision at a safe boundary, updates the active namespace/prompt and exposes it to current programs/parent task control; later runs reuse the same bound library.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy issue-resolution loop established.
- Disturbance / variety regulated: fixed safety, identity metadata and trust settings constrain work; unresolved identity/policy tensions are not routed as such.
- Decisive decision or feedback right: no supplied identity/ultimate-policy adjudication and returned authoritative resolution.
- Decision owner: operator/developer sets instructions and safety/admission settings; no established S5 function owner.
- Supporting / enforcement mechanisms: worker safety/approval policies, static core role, optional Identity instructions and persistent memory, host learning-admission setting.
- Closure path: permissions and exact-revision admission govern actions/capabilities; generic changes to instructions or remembered preferences do not evidence an identity-policy escalation/return.
- Why this is / is not agent-owned: a class named Identity, permission approval or host-controlled trust level alone is not S5.
- Evidence: [optional persistent identity](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/agent/harness_agent/state.py), [identity dialogue role](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/packages/agent/harness_agent/session.py), [safety permissions](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/safety/permissions.py), [approval path](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/safety/approval.py), [Learner admission/demotion](https://github.com/EvolvingLMMs-Lab/the-harness/blob/2aa4105ce8c8ab143be95969fb1cc5944248e8fd/src/harness/runtime/learning/learner.py)
- Basis: structural.
- Confidence: medium-high.
- Caveats: users can build a broader governance organization; this assessment does not import that organization or call every operator decision S5.

### Absence scope

- Surfaces inspected: core roles, safety/approval and host input, learning trust settings, optional agent Identity/Session state and CLI/host adapters.
- Plausible first-party paths checked: durable identity instructions, remembered corrections, user approvals, admission policy and operator session intervention as possible parent-policy channels.
- Why no material first-party path remains: the paths set configuration, facts or ordinary operational rights without exposing an identity/ultimate-policy matter, legitimate adjudication and authoritative governing return; source-repository governance and evaluation policy are outside this runtime.

## Distributed OSS parent arrangement

The evidenced parent is the local operator of one session/host. No project-recursion parent governance is imported from maintainers, contributors or separate installations.

## Self-hosted and non-human modes

A self-hosted session may expose operator oversight and native model-owned task control. Explicit configuration enables native subagents and learning; no hidden developer actor is credited. Default fixture admission remains pending without compatible evidence and is not silently treated as successful autonomous activation.

## Recursion

Native children have local task discretion and may be bounded by max_depth; nested agents and hierarchical charging alone do not prove recursively viable metasystems.

## Variety and escalation

Programs/reactive rules absorb known environment changes; unresolved failures and owner conflicts return to model decisions. Shared usage and cancellation bound collective work. Worker safety cannot be rewritten by learned rules. This is evidence for specific control paths, not a claim of organizational viability or an automatic algedonic/S5 mapping.

## Evidence gaps

Complete pinned tree (664 blobs, untruncated) and relevant roles, runtime, host, coordination, learning, identity and tests/docs were inspected. A transient Git clone transport failure was recovered without repinning. No live model, desktop collision, learning activation or independent secondary semantic review was executed; all positive mappings are source-structural and mode-specific.
