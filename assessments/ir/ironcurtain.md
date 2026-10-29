---
harness_id: ironcurtain
project_name: IronCurtain
repository: https://github.com/provos/ironcurtain
review_ref: d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# IronCurtain

## Review boundary

- System in focus: IronCurtain's shipped first-party local agent/session runtime, deterministic trusted-process policy coordination and bundled workflow controller; not every external AI coding agent that can be run in its Docker containers.
- Purpose and identity: enable constrained autonomous model/tool work through human-authored constitutions, compiled policy, tool interception and bounded multi-role workflows.
- Relevant environment: user prompts, untrusted files/tools, MCP and network effects, role transitions, current workflow artifacts, failed validation, policy changes and human escalations.
- Standard-distribution boundary: `src/session/agent-session.ts`, trusted-process tool-call coordinator, policy compilation/enforcement, `src/workflow/orchestrator.ts`, bundled `vuln-discovery`, `design-and-code` and `evolve` workflows, their stock Docker-agent adapters and human gates.
- Credited operating / distribution surfaces: builtin model-driven TypeScript action/tool loop; bundled vulnerability-investigation workflow where a distinct model-driven router reviews the shared journal and selects subsequent agents; role-bound policy handover with in-flight tool-call quiescence.
- Adjacent first-party surfaces excluded from ownership: external Claude Code, Goose and Codex internal decision loops; arbitrary user-defined workflows; off-repository governance; developer tests; a customer's evaluator or own constitution.
- First-party modes considered: builtin agent code mode and Docker-backed multi-agent workflow modes, including shared-container policy cycling and distinct workflow roles. Docker mode's agent-model behavior is externally supplied, while its first-party prompts, roles, arbitration and return paths are shipped and wired.
- Recursion level: one deployed IronCurtain instance and its supported workflow operating cells; external human owner/administrator is parent authority.
- Reviewed revision: `d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The builtin `AgentSession` calls a configured model using the AI SDK, exposes tools, limits steps/budget, receives responses and tool effects and returns their observations for further model decisions. All relevant effects pass through the sandbox and trusted process. In Docker mode IronCurtain instead intercepts and policy-checks an external agent's effects: the provider's internal deliberation is **not** an IronCurtain S1 by mere containment.

The shipped `vuln-discovery` workflow defines separate model-backed `analyze`, `orchestrator`, harness design/build/validate, discovery and triage roles. Unlike a passive linear pipeline, its `orchestrator` role sees the investigation journal and new agent artifacts, is prohibited from acting as the analyst, examines progress/evidence, chooses to reanalyze, pursue particular hypotheses, revise harnesses, dispatch triage or escalate, and writes a concrete directive that the next agent receives. The first-party orchestrator runner parses an `agent_status` verdict, applies the workflow transition and makes the directive/notes accessible on the next entry. The source thus exhibits a model-owned inside-and-now decision over the investigation's current commitments, not simply a state-machine sequence.

Shared-container workflow roles have potentially incompatible permissions despite accessing the same process/workspace. `cyclePolicy` requests the new persona's compiled policy before starting its state and fails closed if policy loading fails or a newly required MCP server was not provisioned. The trusted-process coordinator suspends new calls, drains in-flight effects (including human-escalation waits), obtains call/policy locks, validates the policy directory, constructs the new engine and atomically swaps policy plus persona. This attenuates a **specific inter-role interference**: an effect initiated under agent A must not execute under agent B's policy or contaminate B's audit attribution. It is a deterministic `C` coordination mechanism; the LLM orchestrator's dispatch is separately classified at S3.

The constitutional pipeline turns administrator-authored English permissions into rules and tests them against generated and handwritten scenarios. Runtime policy decisions permit, deny or request human consent for particular effects. These are important governance constraints, but the reviewed supported workflow does not connect an identity-level constitutional dilemma from operating cells to legitimate final authority and back as an actual S5 adjudication path. Similarly, routine verifier/reviewer stages in task work are not automatically an independent S3* audit. The `evolve` workflow optimizes the user's experiment under an external evaluator; it does not by itself adapt IronCurtain's organization in conversation with its operating S3.

Pinned source: [README](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/README.md), [builtin agent session](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/session/agent-session.ts), [workflow orchestrator](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/orchestrator.ts), [vulnerability workflow](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/vuln-discovery/workflow.yaml), [tool-call coordinator](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/trusted-process/tool-call-coordinator.ts), [evolve workflow](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/evolve/README.md).

## Operational model

The builtin agent owns model-directed S1 action and receives tool feedback. In a bundled Docker workflow, role agents are S1 operating units at the workflow recursion, while the first-party investigation orchestrator has a cross-role current-operational mandate and supplies S3 decisions. The trusted process provides deterministic S2 separation between operating roles' security context at shared-resource handoff. None of this promotes the external provider's general reasoning, one-off approvals or user-defined experimental optimizer into additional first-party metasytem authority.

## S1 — Operations

- State: A
- Function: first-party model-directed autonomous task/tool cycles; in bundled workflows, role-scoped agent actions changing investigation and workspace artifacts.
- Disturbance / variety regulated: evolving task demands, tool outputs, code observations, environment errors, model continuations and operational investigation evidence.
- Decisive decision or feedback right: choose model-generated tools/actions, interpret their results and continue or settle; in role workflows, produce artifacts and agent status from task-directed reasoning.
- Decision owner: IronCurtain's builtin `AgentSession` model loop or a workflow's configured model-driven operating role, not the sandbox, MCP proxy or external agent vendor as a first-party component.
- Supporting / enforcement mechanisms: AI SDK model invocation, registered tools, sandbox, compiled policy, Docker adapters, role prompts and workflow artifact storage.
- Closure path: `AgentSession` model invocation → generated tool call → trusted policy-mediated execution/result → next SDK model step or final answer. Workflow roles write new files/status which are read on next orchestrator/role entry.
- Boundary reachability: builtin mode is shipped, and bundled workflow YAML/runner make multi-role execution a first-party supported path with external LLM credentials supplied by the installer.
- Why this is / is not agent-owned: model inputs and observed outcomes determine substantive next tool/work decision; deterministic policy permits or blocks effects but does not decide the task.
- Evidence: [agent-session.ts](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/session/agent-session.ts), [vuln-discovery/workflow.yaml](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/vuln-discovery/workflow.yaml), [orchestrator.ts](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/orchestrator.ts).
- Basis: structural.
- Confidence: high.
- Caveats: No model or Docker session was live-run; external coding agents' private internal loops are excluded from first-party ownership.

## S2 — Coordination

- State: C
- Distinct S1 units: model-backed `analyze`, `harness_design`, `harness_build`, `discover` and `triage` roles in the bundled vulnerability workflow run separate task phases against one shared-container tool coordinator; the collision witness is the outgoing role and incoming successor role.
- Inter-S1 disturbance: an outgoing operating role's delayed tool call (possibly paused on approval) could be evaluated using the successor operating role's different permission policy, creating privilege bleed and corrupted per-role audit attribution.
- Attenuating coordination relation: the trusted coordinator quiesces new admission, drains old in-flight effects, validates the new policy and atomically changes the engine/persona before allowing successor calls.
- Feedback into subsequent S1 behaviour: an unsuccessful policy cycle fails the workflow rather than starting the successor; a successful cycle changes which tools the successor is allowed to execute and how its calls are attributed, without applying those privileges retroactively to outgoing calls.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the handoff implements a targeted collision-inhibition invariant across distinct role agents with incompatible authority, beyond delivery of messages or sequencing of their tasks.
- Function: deterministic inter-role security-context coordination at shared-container workflow transitions.
- Disturbance / variety regulated: conflicting permissions for distinct model-backed S1 workflow roles sharing the same coordinator, outstanding tool effects and audit stream; a previous role's in-flight effect could otherwise cross into the next role's policy/persona.
- Decisive decision or feedback right: gate admission and complete existing effects under the old role, atomically load a validated new role policy and release the successor role only when separation is restored; abort unsafe transitions.
- Decision owner: trusted-process deterministic coordinator, invoked by first-party workflow runner as it switches from one role to another; not an independent agent choosing the policy.
- Supporting / enforcement mechanisms: quiescence counter, `callMutex`, `policyMutex`, validated persona directory, `PolicyEngine` replacement, current persona audit stamp and workflow-scoped control socket.
- Closure path: outgoing role completion/next state selected → `cyclePolicy` RPC → in-flight old calls drain and new policy/persona become active together → subsequent successor calls are checked under its own rights; failed load halts the workflow instead of silently retaining old privileges.
- Boundary reachability: the bundled vulnerability workflow declares `sharedContainer: true`, and `WorkflowOrchestrator.cyclePolicy` is called for role state entry; the policy swap RPC is implemented by the trusted-process coordinator.
- Why this is / is not agent-owned: it attenuates a concrete first-party inter-S1 interference with a corrective handoff, but the decision mechanism is deterministic (`C`), not a model-negotiated `A` coordination agent.
- Evidence: [vuln-discovery YAML](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/vuln-discovery/workflow.yaml), [workflow cyclePolicy](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/orchestrator.ts), [trusted-process loadPolicy](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/trusted-process/tool-call-coordinator.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: This is a narrow persona/tool-policy collision regulator, not evidence of general scheduling, resource bargaining or collaboration quality between agents; only supported shared-container paths are credited.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: the orchestrator reads the shared investigation journal plus fresh artifacts from all preceding operating roles, including validation coverage and unresolved hypotheses; this is the task-system view, not the entire installation's fleet.
- Current-control decision scope: the model-backed orchestrator allocates the next investigation phase, target region, test tier and agent directive, can recycle/reprioritize work after feedback or halt to request a human when task evidence is inadequate.
- Function: model-backed current investigation management and dynamic commitment/priority control over multiple operating roles in the bundled vulnerability-discovery workflow.
- Disturbance / variety regulated: divergent hypotheses, missing evidence, failed harness validation, inadequate coverage, exhausted lines of inquiry and unproductive or blocked agent phases.
- Decisive decision or feedback right: inspect the whole investigation journal/current outputs and choose which role to call next, what hypothesis/coverage region to prioritize, when to revise work or send the case to human escalation.
- Decision owner: the dedicated model-backed `orchestrator` agent role (not the similarly named TypeScript execution/transition engine).
- Supporting / enforcement mechanisms: full investigation journal, artifacts and evidence rules, required directive/status output, verdict parsing, state transitions, visit caps and human gate.
- Closure path: an S1 role writes artifact plus result → dedicated orchestrator reads journal and new evidence, decides verdict and concrete next directive → first-party workflow runner parses the verdict, routes to a selected S1 role and supplies that directive → changed work returns with new evidence for the next control round.
- Boundary reachability: `src/workflow/workflows/vuln-discovery/workflow.yaml` ships this dedicated role and its reachable transitions, and the first-party workflow runner executes them. It is a supported mode, not an adopter-created downstream supervisor.
- Why this is / is not agent-owned: routing and investigation resource commitments follow the router agent's evidence-sensitive model decision; deterministic parser/transition/visit limits implement but do not substitute for its choice.
- Evidence: [vulnerability orchestrator role and directives](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/vuln-discovery/workflow.yaml), [workflow controller](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/orchestrator.ts), [workflow status parser](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/status-parser.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: S3 is specific to the supported multi-role investigation at its recursion; no claim of organizational S3 over every concurrently deployed IronCurtain session or source-confirmed runtime effectiveness.

## S3* — Complementary audit

- State: —
- Function: no separate alternative-source audit of the operational management account with a return into S3 is established.
- Disturbance / variety regulated: inaccurate analyst claims, defective harnesses, missing fuzz feedback and incorrect findings are checked during primary task execution.
- Decisive decision or feedback right: `harness_validate`, evaluation stages and critic/review roles accept/reject task artifacts in their normal work path, not an independently scoped complementary audit over S3's managerial account.
- Decision owner: role agents and workflow gates as part of operational investigation, human reviewing deliverables; no distinct S3* mandate proven.
- Supporting / enforcement mechanisms: validation role, sanitizer/fuzzer coverage instrumentation, journal/evidence checks, design critic and human report review.
- Closure path: validation failures return to task states or to the same operational router; this is task QA rather than independent reality sampling and separate findings-to-manager feedback.
- Why this is / is not agent-owned: a routine checker or a second role does not become S3* merely because it checks a prior role's product.
- Evidence: [vulnerability workflow](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/vuln-discovery/workflow.yaml), [design-and-code workflow](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/design-and-code/workflow.yaml).
- Basis: structural.
- Confidence: medium.
- Caveats: A downstream deployment could add an independent audit role; it is not imputed to this stock workflow.

### Absence scope

- Surfaces inspected: vulnerability validation/discovery/triage roles, independent-looking coding reviewer, workflow journal and coverage reports.
- Plausible first-party paths checked: fuzz instrumentation independent of agent narrative, mandatory validation, agent critic and final human review.
- Why no material first-party path remains: these check the substantive target's task artifacts inside the production sequence, not a separately authorized complementary audit of current S3 managerial claims with its own sampled operational access.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced future/environment intelligence that informs IronCurtain organizational adaptation through a reciprocal S3 negotiation loop.
- Disturbance / variety regulated: novel task hypotheses, changing experiments, objective/fitness metrics and accumulated learning inside user tasks.
- Decisive decision or feedback right: user-provided evaluator scores `evolve` candidate programs; researcher/analyzer propose and record better task solutions, while no shipped actor proposes changes to the operating IronCurtain system for its S3 to adopt.
- Decision owner: task agents, evaluator supplied by user and external administrator for actual framework/constitution changes.
- Supporting / enforcement mechanisms: `evolve` sampling/research/evaluation/cognition stages and round budget, general web/tools, human preflight review.
- Closure path: candidate → external evaluator score → lesson → next experiment candidate; this closes the user's optimization S1 task, not outside/future system intelligence to present organizational control.
- Why this is / is not agent-owned: `evolve` is a real model-led search, but its target is the user's experiment and its result stays within the commissioned work; it is not automatically VSM S4.
- Evidence: [evolve README](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/evolve/README.md), [evolve YAML](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/workflows/evolve/workflow.yaml), [workflow orchestrator](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/workflow/orchestrator.ts).
- Basis: structural.
- Confidence: high.
- Caveats: No custom deployment that explicitly feeds a learning track into runtime strategy/architecture is part of this assessment.

### Absence scope

- Surfaces inspected: bundled `evolve`, vulnerability hypothesis research, role routing, model/task memory and operational workflow configuration.
- Plausible first-party paths checked: multi-round candidate evolution, cognition store and current-investigation hypothesis revision.
- Why no material first-party path remains: the shipped objectives and feedback are bounded user-task optimization, with no outside-future organizational option owner and S3/current-capability adoption-feedback relation.

## S5 — Policy and identity

- State: —
- Function: no established identity-level dilemma/adjudication and return to all relevant operations at the declared system recursion.
- Disturbance / variety regulated: unsafe tool actions, human-defined constitution intent, persona access rights and human-required individual approvals.
- Decisive decision or feedback right: administrator writes or modifies constitutional permissions, explicitly recompiles and inspects resulting rules; individual risky tool calls can request human approval. No first-party mechanism escalates a conflict over ultimate system identity/mandate to a final authority and returns an authoritative organizational decision to ongoing work.
- Decision owner: external installer/human policy author and per-effect approver; deterministic compiler/verifier/policy engine. They constrain execution but are not a demonstrated operating S5 circuit.
- Supporting / enforcement mechanisms: `constitution-user.md`, `compile-policy`, LLM compilation and scenario checks, `compiled-policy.json`, human escalation channel, policy protection against agent self-modification.
- Closure path: human-authored rule → explicit compilation → deterministic runtime enforcement; human per-effect approval resumes a blocked tool. Neither alone demonstrates an identity conflict → ultimate decision → durable authority-return loop.
- Why this is / is not agent-owned: constitutional vocabulary is substantial, but manual rule authorship and tool-level veto do not satisfy S5 functional closure without a documented identity/ultimate-policy adjudication event.
- Evidence: [constitution and compile process](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/README.md), [policy pipeline](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/pipeline/pipeline-runner.ts), [tool coordinator](https://github.com/provos/ironcurtain/blob/d51a3467cbda6a2e94cf04e885e8ae1abdd0f6be/src/trusted-process/tool-call-coordinator.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: An organization adopting IronCurtain can govern its constitutional identity externally; this assessment cannot import that unobserved parent arrangement as IronCurtain's own S5.

### Absence scope

- Surfaces inspected: constitution authoring and compilation/verification, policy reload, per-tool human escalation, workflow human gates and protected policy files.
- Plausible first-party paths checked: user changes rule and recompiles; an agent requests sensitive action; workflow blocks for human review; persona changes at role transition.
- Why no material first-party path remains: these are authored constraints and bounded action/work-product permissions without a wired identity/ultimate-policy conflict raised from operational/strategic units, legitimate authoritative adjudication, and returned new continuing mandate.

## Distributed OSS parent arrangement

Upstream maintainers define the program; installer/operators own local policy text, credentials and approval choices; external agent and model vendors supply parts of Docker-mode cognition. The distinct parent roles are not collapsed into a single IronCurtain-owned VSM S5. The provided constitution is a local tool-permission policy, not evidence of an organization-wide identity decision by an autonomous parent.

## Self-hosted and non-human modes

The builtin agent and the Docker workflow can operate under provided credentials without human participation in every read/action, subject to deterministic policy checks and optional explicit approval gates. The bundled investigation router is model-backed; the policy swap is deterministic. This distinction supports `S3=A` and `S2=C` without assigning external model vendor governance to the runtime.

## Recursion

Operating roles in `vuln-discovery` are distinguishable S1 task units governed by a dedicated model-backed router at the encompassing investigation recursion. Their shared-container policy handover constitutes narrow deterministic S2 coordination. Individual agent internals and the maintainer organization are different recursion levels not silently folded into this result.

## Variety and escalation

Compiled allow/deny/escalate decisions, test scenarios, policy-directory checks, quiescent persona changes, agent visit caps, resource budgets and explicit investigation directives constrain variety. Operational uncertainty can reach the investigation S3 router, which may send an ambiguous case to `human_escalation`; this is a bounded task escalation, not automatic proof of a distinct S5 identity-level judgment or VSM algedonic channel.

## Evidence gaps

- Source-first structural assessment on pinned revision only; no model calls, Docker execution, security tests against third-party targets or measured agent outcomes were run.
- The `S2=C` assessment is restricted to the explicit old/new persona collision at the shared coordinator, not all forms of multi-agent collaboration.
- The `S3=A` assessment is restricted to the shipped `vuln-discovery` multi-role task, with actual status-driven agent routing, not an unobserved manager over all installations.
- Human authorship of a constitution, routine validation, and a candidate-optimization workflow do not automatically establish S5, S3* and S4 respectively.

## Assessment summary

IronCurtain supplies a real builtin model-to-tool feedback loop (`S1=A`), a shipped deterministic role-policy handoff that prevents inter-S1 privilege/audit interference (`S2=C`), and a distinct model-backed investigation router with cross-role journal view and evidence-conditioned dispatch (`S3=A`). Routine task validators, user-experiment evolution and constitutional tool permissions do not furnish the specific complementary audit, prospective organizational adaptation or identity-level adjudication closures required for S3*, S4 or S5. The proposed vector is **`A / C / A / — / — / —`**.
