---
harness_id: rex-harness
project_name: rex-harness
repository: https://github.com/rexleimo/rex-harness
review_ref: beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# rex-harness

## Review boundary

- System in focus: the standalone `rex-harness` software-engineering control plane at one work-item recursion, including Request/Observation normalization, Fact derivation, Capability selection, Capability Recipes, Workflow/Capability Activations, the current typed Provider Command, rex-native Provider Skills/Reviewer descriptors, command-token and typed-Evidence validation, `.rex-harness/` persistence/journal, compact CLI/public JS API, and standard client projections.
- Purpose and identity: structure evidence-driven software-engineering work so a supported coding-agent work cell executes exactly the currently selected engineering capability, returns typed evidence, and advances only through the canonical Rex workflow state machine.
- Relevant environment: user software objective, project/repository state, execution/test/diff/artifact observations, a compatible coding-agent runtime, provider-skill execution results, and optional host/runtime capabilities supplied outside standalone Rex.
- Standard-distribution boundary: Rex-owned workflow runtime, standalone persistence, CLI/JS API, `rex-workflow`, packaged `rex-*` Provider Skills, specialist reviewer descriptor catalog, client projection/install machinery, and their documented contracts are inside. Codex, Claude, Gemini, OpenCode, Hermes, Grok Build, AIOS model/process execution, AIOS Team/Harness/ContextDB/safety/audit, CRG/codemap services, external repositories and user/host orchestration remain separate systems and do not donate organizational ownership.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `docs/workflow-ownership.md`; `docs/capability-lifecycle.md`; `docs/provider-contract.md`; `src/workflows/software-workflow-runtime.mjs`; `src/application/evaluate-request.mjs`; `src/composition-root.mjs`; `skill-sources/rex-workflow/SKILL.md`; `skill-sources/rex-code-review/SKILL.md`; `skill-sources/rex-workflow/references/reviewers.json` at the frozen revision.
- Adjacent first-party surfaces excluded from ownership: parent-project AIOS execution/governance surfaces; repository-development CI/tests/release governance; external coding-agent model/tool-loop internals; optional external codemap/CRG tooling; host-specific Team/Harness promotion implementation and AIOS-only reviewer identity/promotion validation.
- First-party operating / deployment modes considered: standalone CLI + native client Skill projection for Codex/Claude/Gemini/OpenCode/Hermes/Grok Build; embedded public JS API use by a host; rex-native skill Providers; risk-domain reviewer descriptors. AIOS-enhanced execution is inspected only to preserve the boundary and is not used to upgrade standalone ownership.
- Recursion level: one Rex software work item / adaptive-software-delivery workflow controlling one current coding-agent operational cell at a time. Capability stages and Provider identities are workflow roles, not automatically distinct S1 units. Any AIOS Team/Harness population is a wider adjacent host recursion.
- Reviewed revision: `beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`rex-harness` is deliberately split between semantic control and external execution. Its composition root derives software-engineering Facts and selects at most one eligible Capability. `software-workflow-runtime.mjs` starts one Capability Activation, emits one current `provider.invoke` Command and accepts only evidence matching the current recipe stage. A completed Activation is added to workflow history; only then does the runtime recompute the next eligible Capability. Missing or invalid evidence keeps the same stage blocked, malformed state is rejected, and one-time command tokens rotate after accepted evidence.

Standalone state is persisted under `.rex-harness/`: Workflow JSON is canonical, work-item indexes support resume, Activation files are projections, and Evidence is appended to a journal. Writes are atomic and corrupted state is not guessed back into validity. `rex-workflow` is the shipped agent-facing orchestration Skill. It instructs a compatible coding agent to start/resume the workflow, load only the current Rex Provider, perform only the current stage objective, submit real typed evidence with the current token, then consume the next compact Command until completion.

Rex itself does not launch the coding-agent/model process. Documentation and source make that ownership split explicit: standalone uses an external compatible coding agent or human to execute the current Command, while AIOS can host execution through the same public API. AIOS may add Team, Harness, ContextDB, safety, recovery and audit, but it may not reselect Rex Capability order. `decidePromotion()` can return a request for `team` or `harness`; it does not instantiate those systems.

The packaged Provider catalog includes implementation, requirements/design/planning/TDD/debug and review procedures. `rex-code-review` directly reads a frozen diff plus standards/spec evidence and emits review evidence, but in the standalone path it is simply the current Provider executed by the same coding-agent work cell. For `providerKind=agent`, `rex-workflow` loads a first-party reviewer descriptor and tells the current agent to adopt exactly one risk-matched reviewer role; Rex does not instantiate a separately controlled reviewer actor. AIOS can add stronger agent identity/promotion checks, but those belong to the adjacent host boundary.

## Operational model

The operating unit is a compatible autonomous coding agent executing a Rex-issued current Command against a project environment. Rex attenuates workflow variety by deciding which engineering capability is currently authorized and by requiring typed evidence before continuation. Within that bounded command, the agent still absorbs local software-engineering variety: it inspects repository/tool state, decides concrete implementation/research/review actions allowed by the Provider procedure, observes results, and returns evidence. Rex then deterministically accepts, blocks, advances the current recipe, or selects the next capability from updated Facts/completion state.

The standalone distribution intentionally avoids a population-level control plane. Exactly one current Capability/Command is active for a work item; Providers cannot trigger the next Provider or mutate the Activation; Team/Harness promotion is a request to an external host rather than an in-boundary organizational mode.

## S1 — Operations

- State: A
- Function: perform the current bounded software-engineering transformation selected by Rex — requirements/design/planning/testing/debugging/implementation/review or another enabled Rex capability — against the actual project environment and return real evidence of the result.
- Disturbance / variety regulated: repository and runtime state, implementation choices, test/debug outcomes, requirements ambiguity, design constraints, diff/spec evidence and other task-local distinctions that determine how the current engineering objective should be accomplished.
- Decisive decision or feedback right: within the Rex-selected current capability/stage and its constraints, choose concrete project-facing actions, revise them from tool/environment feedback, and decide what truthful evidence can be returned for the current objective.
- Decision owner: the autonomous compatible coding-agent actor running the shipped Rex workflow/Provider instructions.
- Supporting / enforcement mechanisms: Fact/Capability selector; Capability Recipe; one current Provider Command; packaged Provider Skill; expected-evidence contract; one-time command token; evidence validator; atomic Workflow/Activation persistence; append-only evidence journal; compact CLI/public JS API.
- Closure path: Rex derives current Facts and emits one Provider Command → the autonomous coding-agent work cell loads the corresponding first-party Provider procedure and acts on project/repository reality → tool/test/diff/artifact feedback informs its subsequent local actions → it submits real typed evidence → Rex validates that evidence and either blocks, advances the recipe, or selects a subsequent capability → the same supported work process continues until the workflow is complete.
- Boundary reachability: `rex-harness init --client ...` installs the first-party `rex-workflow` and Rex Provider projections into the standard discovery surface of supported coding-agent clients. The documented standalone workflow then directly drives the current external agent through Rex-owned Command/Evidence contracts without requiring AIOS or application-authored orchestration. The external agent's internal model/tool implementation remains outside the ownership boundary; only its bounded operational decision role in the Rex-managed process is credited.
- Why this is / is not agent-owned: removing the autonomous coding-agent actor while leaving Rex Facts, deterministic selection, state machine, Provider text, tokens and evidence gates intact leaves a control protocol that can select/validate stages but cannot itself inspect open-ended project reality and make the concrete engineering decisions needed to produce the outcome. The agent therefore owns the S1 discretion; Rex constrains and records it.
- Evidence: [`README.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/README.md); [`docs/workflow-ownership.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/workflow-ownership.md); [`docs/provider-contract.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/provider-contract.md); [`skill-sources/rex-workflow/SKILL.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/skill-sources/rex-workflow/SKILL.md); [`src/workflows/software-workflow-runtime.mjs`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/src/workflows/software-workflow-runtime.mjs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the model/tool loop is supplied by the compatible coding-agent runtime, not implemented by Rex. This finding credits the standard first-party Rex integration that closes those agent decisions into the Rex-managed operation; it does not import the external agent's internal organizational functions.

## S2 — Coordination

- State: —
- Function: no material first-party coordination loop among distinct S1 units is established inside the standalone Rex work-item boundary.
- Disturbance / variety regulated: possible cross-worker collision, oscillation, resource contention or incompatible concurrent commitments were inspected; the standalone runtime instead serializes semantic progress through one current Capability/Command.
- Distinct S1 units: no required concurrent population of distinct operational S1 units is instantiated by standalone Rex. Provider stages/roles are successive roles in one work-item operation, not automatically separate operational cells.
- Inter-S1 disturbance: no concrete in-boundary peer interference relation is established. `INDEPENDENT_WORKSTREAMS` may cause a promotion request to an external Team host, but the peer workstreams and their conflicts are outside standalone Rex.
- Attenuating coordination relation: none established in the standalone control plane. One-at-a-time Capability selection and command sequencing attenuate workflow state variety but do not coordinate interaction among multiple S1s.
- Feedback into subsequent S1 behaviour: no S2-specific peer-conflict result is returned to distinct participating S1 units. The next Command is selected from workflow Facts/evidence for the same work item.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not. The strongest candidate surfaces are deterministic sequencing, current-command gating and a host-promotion request; Methodology 0.3.6 excludes those from S2 absent a specific inter-S1 disturbance/attenuation/feedback witness.
- Decisive decision or feedback right: none established for S2 at the declared boundary.
- Decision owner: none established.
- Supporting / enforcement mechanisms: one-current-Capability selection; current Command token; workflow history; optional `promotion.target=team|harness` request to the host.
- Closure path: no first-party S2 closure exists at the frozen standalone boundary.
- Why this is / is not agent-owned: the operating agent may perform sequential Provider roles, and an external host may later instantiate multiple workers, but Rex itself does not provide the required inter-S1 coordination decision/feedback loop.
- Evidence: [`docs/architecture.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/architecture.md); [`docs/capability-lifecycle.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/capability-lifecycle.md); [`src/composition-root.mjs`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/src/composition-root.mjs); [`docs/workflow-ownership.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/workflow-ownership.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: AIOS Team/Harness may supply coordination at a wider host boundary; it is deliberately excluded rather than inherited.

### Absence scope

- Surfaces inspected: standalone workflow runtime; Fact/Capability selection; Capability lifecycle; current Command/provider contract; workflow persistence; `decidePromotion()`; Rex workflow Skill; documented AIOS boundary.
- Plausible first-party paths checked: multiple Capability stages as S1 plurality; review/implementation Providers as peer cells; `INDEPENDENT_WORKSTREAMS` promotion as coordination; workflow sequencing/current-command locking as anti-collision; shared Evidence/Activation state as coordination.
- Why no material first-party path remains: standalone Rex maintains one current semantic operation and can only request that an external host promote execution to Team/Harness. It does not instantiate distinct peer S1s or close a disturbance-specific mutual-adjustment relation among them.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control function is established above a population of current operational S1 commitments inside standalone Rex.
- Disturbance / variety regulated: current stage eligibility, evidence completeness, failure precedence and continuation state are regulated, but those are workflow/operation controls for one work item rather than whole-system resource/commitment regulation.
- Decisive decision or feedback right: no distinct in-boundary actor holds authority to reprioritize, bargain over, reallocate or intervene across a whole set of current S1 resources/commitments.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: deterministic Fact/Capability priority, one-current-Command state machine, blocked/next/completed transitions, execution-failure precedence, profile enablement and host promotion request.
- Closure path: no S3-specific whole-system current-control loop exists in the standalone boundary.
- Why this is / is not agent-owned: the coding agent owns task-local S1 decisions under the current Command; Rex deterministically chooses the next semantic workflow capability from Facts. Neither role is shown exercising a separate whole-system current-control right over multiple operational units.
- Evidence: [`src/composition-root.mjs`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/src/composition-root.mjs); [`src/workflows/software-workflow-runtime.mjs`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/src/workflows/software-workflow-runtime.mjs); [`docs/capability-lifecycle.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/capability-lifecycle.md); [`docs/workflow-ownership.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/workflow-ownership.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: AIOS may add Team/Harness and host governance at a wider recursion. Rex's authority to select one workflow Capability is not promoted to S3 because it lacks the Profile's whole-system current view and resource/commitment scope.

### Absence scope

- Surfaces inspected: `software-workflow-runtime`, composition root, execution profile, Capability lifecycle, profile/provider bindings, standalone store/CLI, host promotion interface and workflow-ownership contract.
- Plausible first-party paths checked: deterministic Capability selection as manager; priority ordering/failure preemption as current control; current Command as whole-system commitment control; profile enablement as resource governance; Team/Harness promotion request as whole-system S3.
- Why no material first-party path remains: all reviewed Rex-owned controls govern the progression and evidentiary validity of one semantic software workflow. The implementation explicitly leaves multi-agent runtime execution and host governance to AIOS/other hosts, so the required higher-recursion current-control population is absent from standalone Rex.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent first-party complementary audit actor/path is closed in standalone Rex, despite strong review-specific Provider procedures and evidence contracts.
- Disturbance / variety regulated: incorrect implementation/completion claims, standards/spec violations and risk-domain defects are candidate audit targets.
- Decisive decision or feedback right: no independent in-boundary auditor owns a complementary judgment whose findings return into later operation as a separately controlled audit relation.
- Decision owner: none established for S3* at the standalone boundary.
- Supporting / enforcement mechanisms: `rex-code-review`; specialist reviewer descriptors; direct diff/spec/standards evidence; typed `standards-review-recorded`, `spec-review-recorded`, `specialist-scope-recorded` and `specialist-verdict-recorded` evidence; workflow evidence gating.
- Closure path: Rex may select a review Capability and require review evidence before continuation, but the standalone current coding agent executes that Provider/role. The resulting review is therefore an in-path operational stage rather than a sufficiently independent complementary audit channel.
- Why this is / is not agent-owned: the same supported coding-agent work cell that executes the Rex workflow loads `rex-code-review`, or for `providerKind=agent` loads one risk-matched reviewer descriptor and performs that role. Rex does not supply a separately instantiated/controlled reviewer process. AIOS-only identity/promotion validation and any external agent subagent mechanism remain outside the boundary.
- Evidence: [`skill-sources/rex-code-review/SKILL.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/skill-sources/rex-code-review/SKILL.md); [`skill-sources/rex-workflow/SKILL.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/skill-sources/rex-workflow/SKILL.md); [`skill-sources/rex-workflow/references/reviewers.json`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/skill-sources/rex-workflow/references/reviewers.json); [`docs/provider-contract.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/provider-contract.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: `rex-code-review` includes an optional acceptance mode that can instruct a capable external coding-agent runtime to use isolated subagents, and AIOS can validate promoted reviewer identities. Those are not Rex-owned standalone reviewer instantiation/independence paths and are not borrowed into this assessment.

### Absence scope

- Surfaces inspected: standards/spec code-review Skill; specialist reviewer catalog; `providerKind=agent` loading path in `rex-workflow`; Provider contract; review evidence kinds; workflow gating; documented AIOS reviewer handoff/identity validation boundary.
- Plausible first-party paths checked: code-review Provider as independent auditor; specialist reviewer role as separate agent; review evidence gate as S3*; optional acceptance subagents as independent audit; AIOS reviewer handoff as first-party standalone audit.
- Why no material first-party path remains: Rex packages audit procedures and can schedule them, but standalone execution reuses the current external coding-agent cell. The separate identity/runtime needed to make audit access sufficiently independent is supplied only by adjacent external/host capabilities, not by the Rex standalone distribution.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established in standalone Rex.
- Disturbance / variety regulated: current task observations, failures, requirements ambiguity, design/testability state and risk evidence can change which current engineering Capability is selected.
- Decisive decision or feedback right: no first-party path is established that models a future external environment, generates adaptation options for Rex's own future capability/organization and returns one of those options into present capability.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: Fact derivation; re-evaluation after completed Capabilities; failure preemption; requirements/testability decisions; runtime promotion suggestion; execution-profile analysis.
- Closure path: no S4-specific outside-and-then adaptation closure exists. Current observations alter the current work-item workflow, not the harness's future capability model.
- Why this is / is not agent-owned: the coding agent may research or reason about the current software problem inside a Provider, and Rex adapts the next current-task step from Facts, but neither constitutes a separate prospective environmental-intelligence function feeding adaptation of the organization.
- Evidence: [`src/application/evaluate-request.mjs`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/src/application/evaluate-request.mjs); [`src/composition-root.mjs`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/src/composition-root.mjs); [`docs/capability-lifecycle.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/capability-lifecycle.md); [`README.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: "adaptive-software-delivery" describes current workflow selection. Methodology 0.3.6 does not equate current-task adaptation, planning or failure reaction with S4.

### Absence scope

- Surfaces inspected: Fact derivation/evaluation, Capability selection, re-evaluation after completion, testability/requirements decisions, failure priority, execution-profile analysis, promotion logic and Provider procedures.
- Plausible first-party paths checked: adaptive workflow name as S4; re-evaluation from new Facts as adaptation; external repository/research observations as environmental intelligence; post-execution profile analysis as learning; Team/Harness promotion as future organizational adaptation.
- Why no material first-party path remains: these mechanisms distinguish and react to current work-item state. None creates future/environmental adaptation options for the Rex organization and returns a selected option into present capability as required by S4.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established for the standalone Rex organization.
- Disturbance / variety regulated: workflow integrity, Provider authority, evidence authenticity, enabled capabilities, user intent and host promotion authority are strongly constrained, but they remain operational contracts/configuration rather than identity/ultimate-policy decision closure.
- Decisive decision or feedback right: no S5-specific identity or ultimate-policy issue is shown escalating to legitimate ultimate authority and returning as an authoritative policy decision governing subsequent Rex operation.
- Decision owner: none established for S5 at the declared boundary.
- Supporting / enforcement mechanisms: explicit-intent normalization; fixed Rex-native Provider catalog; current-command authorization; one-time evidence tokens; fail-closed malformed state/evidence; profile capability enablement; host-owned acceptance/rejection of Team/Harness promotion; projection digest/update rules.
- Closure path: no first-party S5-specific escalation-and-return path exists in standalone Rex.
- Why this is / is not agent-owned: the operating agent cannot rewrite Capability order, Provider trigger rights or workflow state, but those fixed constraints are constructor policy. User intent and host approval govern ordinary task/runtime choices, not an evidenced identity/ultimate-policy conversation at the selected recursion.
- Evidence: [`docs/provider-contract.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/provider-contract.md); [`skill-sources/rex-workflow/SKILL.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/skill-sources/rex-workflow/SKILL.md); [`src/composition-root.mjs`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/src/composition-root.mjs); [`docs/workflow-ownership.md`](https://github.com/rexleimo/rex-harness/blob/beee2b4e1d25ef03a87b4b0d8b57c815ff6828b5/docs/workflow-ownership.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: AIOS or another embedding organization may supply higher-recursion governance. Static Rex contracts and generic host approval are not upgraded to S5.

### Absence scope

- Surfaces inspected: explicit-intent handling; profile/capability enablement; Provider catalog and trigger ownership; evidence/token integrity; fail-closed workflow state; host promotion authority; client projection update/adoption rules; documented standalone/AIOS ownership split.
- Plausible first-party paths checked: immutable Provider authority as constitution; evidence token as identity; user objective/explicit intent as S5; host acceptance of promotion as ultimate policy; profile enablement as governance; projection trust/digest rules as identity-policy closure.
- Why no material first-party path remains: all inspected paths constrain operational execution, artifact integrity or runtime composition. No identity/ultimate-policy issue reaches a legitimate S5 authority and returns as a function-specific decision governing later operation.

## Distributed OSS parent arrangement

Repository maintainers define Rex's packaged workflow semantics, but repository-development governance is adjacent to the assessed runtime distribution. Independent users can install the standalone package into local coding-agent clients without joining a shared runtime organization. No organization-level parent S3/S4/S5 mode is inferred from maintainer authority or local human use.

## Self-hosted and non-human modes

Standalone Rex is self-hostable and can run through multiple supported coding-agent clients. The positive S1 mode depends on an autonomous compatible coding-agent actor executing Rex's first-party workflow/Provider contract. Human execution of a current Command is possible but is not published as S1 parent ownership. No qualifying standalone operator-governed S3/S4/S5 loop is established.

## Recursion

At the assessed recursion, one adaptive-software-delivery work item is the controlled operating organization and the compatible coding-agent execution cell is S1. Capability stages and Provider personas are semantic roles within that operation, not recursive viable systems merely because they are separately named. If an embedding host accepts Team/Harness promotion, that wider organization is a separate recursion and must be assessed on its own first-party control paths.

## Variety and escalation

Rex strongly attenuates presented workflow variety: one Capability is selected, one current Command is authorized, evidence kinds are typed, real references are required and a token prevents stale replay. The coding agent supplies local requisite variety inside that stage by acting on repository/tool feedback. Missing evidence, malformed state, unknown intent, invalid refs and unavailable Providers fail closed rather than being guessed through. Execution failure can preempt ordinary implementation capabilities. Requests for team/harness promotion transport a need for a wider execution form to the host, but that signal does not itself transfer S2/S3/S5 ownership into Rex.

## Evidence gaps

No material evidence gap prevents publication at the frozen revision. The main boundary-sensitive conclusions are deliberate: the compatible coding-agent work cell is credited as autonomous S1 because Rex's shipped client projection closes that actor into the standard operating protocol while its internals remain external; Team/Harness and AIOS governance are not imported; review procedures are not credited as S3* without Rex-owned independent audit execution.