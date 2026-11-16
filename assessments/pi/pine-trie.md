---
harness_id: pine-trie
project_name: pine·trie
repository: https://github.com/halecraft/pinetrie
review_ref: 0f4483f4aa86058347448f616848b475cb8c0fa5
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# pine·trie

## Review boundary

- System in focus: One pine·trie host serving a project with concurrent lane-backed threads.
- Purpose and identity: Collaborative, branching agent work whose proposed changes can be inspected and integrated into a common project baseline.
- Relevant environment: Project files, peer threads and human users, Git/jj or folder history, optional lane shares and configured model endpoints.
- Standard-distribution boundary: The installed CLI/host, web client, Pi-backed lane agent, Docker/VM lane management, jj and folder acceptance adapters.
- Credited operating / distribution surfaces: Supported tool-enabled project host, threaded agents, peer relay/round decision flow, accepted project config and review/accept paths.
- Adjacent first-party surfaces excluded from ownership: Repository dogfooding, development process and out-of-boundary examples; Docker, Kyneta and Pi supply dependencies rather than the assessed ownership decisions.
- First-party operating / deployment modes considered: Git/jj-backed and folder projects, local or shared team host, supported multi-agent rounds and operator-controlled acceptance.
- Recursion level: One project host. Separate lane-backed threads provide operational units at the assessed recursion.
- Reviewed revision: `0f4483f4aa86058347448f616848b475cb8c0fa5`
- Observation date: 2026-11-16
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

A project host connects browser clients to a tree-shaped session and to isolated first-party lanes. The embedded Pi core is configured and invoked by the host, with tool calls bound to a lane. The host separates observations, proposed revisions and accepted work. Peer replies can trigger a bundled round-resolution model call.

## Operational model

Lane models perform requested work inside a separate checkout or folder. The host records turn changes and exposes proposals. Users decide which revisions advance the project baseline and govern its setup. Multi-agent follow-up choices can be delegated to the bundled round model.

## S1 — Operations

- State: A
- Function: Carry out coding or inquiry tasks on a conversational thread.
- Disturbance / variety regulated: Different jobs, tool outcomes and changes in the lane's working copy.
- Decisive decision or feedback right: Choose tool actions from thread context and use their returned results to continue or answer.
- Decision owner: The installed lane's model-backed agent.
- Supporting / enforcement mechanisms: A Pi-backed harness instance, thread-specific tool context, containerized operations, Kyneta session and turn recording.
- Closure path: The tool's response reaches the lane's agent continuation. At turn boundaries, file effects and primary messages are recorded and visible as proposed work.
- Why this is / is not agent-owned: The model decides which permitted tools to use and how to respond. The host supplies lane storage, tool registration and dispatch.
- Evidence: [packages/pi/agent.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/packages/pi/agent.ts#L201-L276), [packages/pi/tools.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/packages/pi/tools.ts#L68-L120), [ARCHITECTURE.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/ARCHITECTURE.md#L8-L30), [README.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/README.md#L14-L26).
- Basis: First-party model/tool binding, continuation and turn records.
- Confidence: High.
- Caveats: Pi and the model provider are dependencies. The cited lane, tools, history and feedback are wired by the product.
- Boundary reachability: The shipped host builds the Pi-backed agent with its own tool registration, thread-specific context and turn-recording hooks, and starts it in the thread lane.

## S2 — Coordination

- State: A
- Function: Resolve dependencies or disagreements among active operational threads.
- Disturbance / variety regulated: Separate thread agents can reach incompatible answers or require one another's results.
- Decisive decision or feedback right: Decide if a peer is to answer a discrepancy, select that peer, and formulate the returned task.
- Decision owner: The model the host invokes with its bundled agents-round skill.
- Supporting / enforcement mechanisms: Completed peer answer gathering, member-constrained reply parser, allowance accounting and actual relay.
- Closure path: The host observes a completed multi-agent round, asks the model whether to intervene, parses its choice and delivers a new ask to the selected thread agent. The answer can resolve the identified dependency or disagreement.
- Why this is / is not agent-owned: The model picks the live follow-up target and question. The host validates membership and enforces budget and relay.
- Evidence: [apps/pinetrie/host/answers.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/answers.ts#L175-L258), [packages/pi/skills/agents-round/SKILL.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/packages/pi/skills/agents-round/SKILL.md#L7-L15), [packages/rules/told.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/packages/rules/told.ts#L358-L385), [apps/pinetrie/host/work/update.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/work/update.ts#L414-L445).
- Basis: Shipped follow-up wiring plus a separate lane conflict mechanism.
- Confidence: High.
- Caveats: The decisive example is an eligible person-triggered multi-agent round. Lane isolation and catch-up also attenuate file conflicts.
- Boundary reachability: The run-end handler dispatches the bundled round skill after eligible replies; its structured output drives a real follow-up relay.
- Distinct S1 units: Peer thread agents with distinct contexts and lane work.
- Inter-S1 disturbance: Disagreeing answers or dependencies between peer-agent results on a shared request.
- Attenuating coordination relation: A model reviews the replies together and can task one identified peer with a specific reply to resolve an open disagreement or dependency.
- Feedback into subsequent S1 behaviour: The validated ask is delivered to the selected thread and becomes a new request for that agent.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The follow-up decision is conditional on a completed multi-agent round and explicit disagreement or dependence. Its output changes a peer's subsequent activity.

## S3 — Inside-and-now control

- State: P
- Function: Choose the currently accepted project basis among alternative lane contributions.
- Disturbance / variety regulated: Concurrent agent and human proposals can conflict or be based on stale accepted work.
- Decisive decision or feedback right: Choose which prepared revision or stack advances the shared accepted baseline, or leave it pending.
- Decision owner: The project operator through the acceptance workflow.
- Supporting / enforcement mechanisms: Cross-thread work summaries, diff inspection, accepted bookmark, destination and conflict checks, serialized writes.
- Closure path: The admitted revision advances accepted work. Other threads receive a base-change signal and can update their actual work to the changed basis.
- Why this is / is not agent-owned: Agents propose and can repair their lane work. The user owns advancement of accepted shared work and its destinations.
- Evidence: [docs/pinetrie.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/docs/pinetrie.md#L616-L646), [apps/pinetrie/host/jj/proposed/act.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/jj/proposed/act.ts#L74-L109), [apps/pinetrie/host/folder/writes.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/folder/writes.ts#L321-L354), [apps/pinetrie/host/work/update.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/work/update.ts#L414-L445).
- Basis: First-party operator surface, proposal acceptance rules and shared base propagation.
- Confidence: Medium-high.
- Caveats: The evidence covers project baseline control. A newer base reaches existing lanes when they update; it does not silently merge into running work.
- Boundary reachability: The installed host exposes proposal and accept commands for both jj and folder projects, and its lane machinery reads the accepted baseline.
- Whole-system current view: A project-wide tree of active lanes, their proposed changes and their conflicts against current accepted work, with material diffs available for the user's choice.
- Current-control decision scope: Current admission and destination of proposed project changes into the authoritative baseline used by peer lanes.

## S3* — Complementary audit

- State: —
- Function: Audit material operational claims independently of normal proposal reporting.
- Disturbance / variety regulated: A free-form report can disagree with the work's actual contents or outcomes.
- Decisive decision or feedback right: Inspect operational reality with an audit mandate independent of ordinary production/acceptance and return a correction to current control.
- Decision owner: No function-specific first-party audit owner identified.
- Supporting / enforcement mechanisms: Proposal summaries, separate file diff reads for the acceptance decision, conflict detection and peer asks.
- Closure path: The data feeds ordinary acceptance and source synchronization. Peer answers inform coordination.
- Why this is / is not agent-owned: Diff reading supplies primary evidence to the person who accepts a proposal. No distinct auditor is tasked to verify agents' operational claims and return an audit verdict.
- Evidence: [apps/pinetrie/host/folder/review.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/folder/review.ts#L42-L75), [docs/pinetrie.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/docs/pinetrie.md#L616-L644), [apps/pinetrie/host/answers.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/answers.ts#L175-L258), [packages/pi/skills/agents-round/SKILL.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/packages/pi/skills/agents-round/SKILL.md#L7-L15).
- Basis: Review reads, proposal acceptance and built-in peer skills.
- Confidence: Medium.
- Caveats: A project can request independent ad hoc review through a separate thread. That judgment is not an installed audit loop in the reviewed mode.

### Absence scope

- Surfaces inspected: Actual file/revision review, accepted-work decisions, summarization and peer-agent follow-up.
- Plausible first-party paths checked: Complementary diff checks, conflict reporting and a separate agent checking another's outcome.
- Why no material first-party path remains: The diffs and conflicts are part of the direct approval and merge workflow. The review and round surfaces do not bind a separate audit responsibility to a returned corrective verdict.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adopt reusable model, command, skill or prompt changes for future project work.
- Disturbance / variety regulated: Future workflows can require model capabilities or tools beyond the current host setup.
- Decisive decision or feedback right: Select which proposed project setup change becomes a durable future operating capability.
- Decision owner: The project operator accepting the configuration change.
- Supporting / enforcement mechanisms: Supported project configuration layers, lane proposals, config-change feedback and host Pi startup setup.
- Closure path: The operator accepts a revision with updated setup, accepted configuration is read in the next host startup, and its models or reusable skills become part of later thread operation.
- Why this is / is not agent-owned: Agents can propose the change. Authority to make a lane's setup proposal the project's future setup remains with the operator.
- Evidence: [apps/pinetrie/host/work/config.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/work/config.ts#L44-L140), [apps/pinetrie/host/TECHNICAL.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/TECHNICAL.md#L724-L737), [docs/pinetrie.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/docs/pinetrie.md#L590-L627), [apps/pinetrie/host/jj/proposed/act.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/jj/proposed/act.ts#L74-L109).
- Basis: Source-wired accepted configuration and documented host startup semantics.
- Confidence: Medium-high.
- Caveats: This covers setup adoption. Some changes require an operator restart and the assessment makes no claim of an autonomous environmental scan.
- Boundary reachability: The shipped startup reads accepted work's configuration and passes resolved models, skills and prompts to the Pi setup. The shipped accept operation advances the input revision.
- External distinction: A project operator can choose models, supported external skill packages or new runbooks to address upcoming work outside the current thread.
- Future / prospective distinction: Project setup changes deliberately persist beyond the producing turn and can govern future host launches.
- Adaptation option generated: A proposed revision of project configuration choosing a new reusable skill, prompt or model capability.
- Path back into current capability / S3: Acceptance advances the source for startup setup. The next host reads that accepted state and runs future lanes with the adopted capability.

## S5 — Policy and identity

- State: P
- Function: Set the standing authority of lanes to reach project-shared resources.
- Disturbance / variety regulated: A proposed scope change can introduce new directories or access grants that would change the project's operating boundary.
- Decisive decision or feedback right: Authorize the project-level grants by deciding which configuration revision becomes accepted.
- Decision owner: The project operator who can advance the accepted project basis.
- Supporting / enforcement mechanisms: Layered authority decoding, accepted config preflight, share/grant application and lane start specification.
- Closure path: The accepted base changes, the host rereads accepted authority, applies the sharing/grant plan then takes the new config into force. Lanes use the accepted authority in subsequent starts.
- Why this is / is not agent-owned: Agents can make proposals inside their lane scope. The host enforces accepted project authority and the person chooses the binding project grant as part of acceptance.
- Evidence: [apps/pinetrie/host/work/config.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/work/config.ts#L44-L140), [apps/pinetrie/host/work/setup.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/work/setup.ts#L286-L312), [apps/pinetrie/host/work/setup.ts](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/apps/pinetrie/host/work/setup.ts#L393-L435), [docs/pinetrie.md](https://github.com/halecraft/pinetrie/blob/0f4483f4aa86058347448f616848b475cb8c0fa5/docs/pinetrie.md#L606-L615).
- Basis: First-party config and share-and-grant application.
- Confidence: High.
- Caveats: Scope is project-level lane rights. User and host settings may further constrain the effective permissions.
- Boundary reachability: The installed host's lane setup guards access through the accepted-config and share-and-grant path, which is re-read when accepted work changes.
- Identity / ultimate-policy issue: Which external directories/resources are within the continuing lane operating and trust boundary.
- Ultimate authority in each claimed mode: The project operator choosing accepted configuration within host/user-level limits.
- Return-to-operation path: An accepted change is decoded, host share-and-grant is applied, accepted configuration is replaced and subsequent lane specs reflect the choice.

## Distributed OSS parent arrangement

The project operator is the parent authority for baseline, adaptation and lane grants within this installation. Maintainer policies governing the pine·trie repository are outside the assessment.

## Recursion

Threads can branch with independent histories and filesystem lanes. A host retains project-level accepted work and authority shared across the lanes. The project's external tool/model providers remain environmental dependencies.

## Variety and escalation

Lane isolation prevents routine output collisions. Catch-up returns merge conflicts to the agent and can surface them to the user. Model coordination can return a new ask or a matter for people to decide.

## Evidence gaps

Source-only reconstruction at the frozen revision. No runtime model outcome, controlled contention measurement or external deployment was observed. The S4 adoption path is scoped to the supported persistent configuration changes.
