---
harness_id: nodecode
project_name: Nodecode
repository: https://github.com/nodecode-ai/nodecode
review_ref: 314476ddee650954f32695500be308276243f28b
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Nodecode

## Review boundary

- System in focus: One installed Nodecode personal-agent runtime, including its supported optional standing-team and experience-reflector modes.
- Purpose and identity: Perform user work through live Common Lisp evaluation, retain useful code/knowledge, and support durable multi-session operation.
- Relevant environment: Operator workspaces, files/processes, model providers, shared Lisp image, optional channels and installed cells.
- Standard-distribution boundary: Main repository at the frozen ref plus the exact first-party cell bundle selected by `cells/bundle.json`: nodecode-ai/cells@`39dcac03bf81b26498257586962eaa3cb15ef67d`. Cell source is immutable distribution evidence, not a newer repository head.
- Credited operating / distribution surfaces: Kernel/session/store, engine agent-loop/eval, fork fencing, cells loader and pinned team/board/goal/experience cell paths when enabled.
- Adjacent first-party surfaces excluded from ownership: Development tests/proofs/performance benchmarks, the maintainers' own release/PR organization, external community cells and the team's advisory-feed authoring organism. PR triage over external work is an application workload, not automatically internal S3*.
- First-party operating / deployment modes considered: Local CLI/gateway and attached shells, model-driven eval turns, fork helpers, optional scored/unscored standing teams and experience post-turn reflection. No central cloud service owns these local decisions.
- Recursion level: One installed operator-owned agent application; optional team mode contains distinct task-working sessions under one operator's current supervision.
- Reviewed revision: `314476ddee650954f32695500be308276243f28b`, plus exact pinned cell-bundle commit above.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[src/engine/turn.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/engine/turn.lisp) owns the model/eval feedback loop. Durable session facts are hydrated into a compiled request, provider output and usage are recorded, selected calls execute and tool outcomes enter subsequent rounds. Background evaluations retain independent registry/lifecycle state and wake the task with actual results. Mutations become code/knowledge cell files; kernel floor locks, provisional first-use verification and generations provide rollback and persistence mechanisms.

[cells/bundle.json](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/cells/bundle.json) pins the supported cells separately; [docs/CELLS.md](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/docs/CELLS.md) explains loading and activation. The pinned team cell runs distinct full-tool sessions against a shared directory with per-node work areas and a common artifact. Its agent protocol makes nodes inspect peers' approaches, revise collisions, reproduce results and serialize artifact promotion. The board adds bounded message delivery, but is not alone the S2 witness. The operator can inspect the standing team, redirect all its current work and replace spent seats at a subsequent input.

The pinned experience cell observes completed operator turns and launches a separate reflection session. Its verification instruction reconstructs the intended user-visible invariant, reads actual result/durable evidence, records pass/fail/blocked status, permits bounded safe repair and returns a recap or operator attention request. This is separate from ordinary goal-completion checking and self-selected mutation tests.

## Operational model

A model-driven session chooses Lisp/actions for user work, receives actual effects/errors and may persist useful definitions. Fork/team sessions can be distinct S1 units. Deterministic storage, fences, budgets, token accounting and locks constrain them; their implementation does not itself own the agent's production or peer-adjustment discretion. Standing-team current supervision is explicitly parent-operated; audit judgment in optional experience mode belongs to a separate reflector.

## S1 — Operations

- State: A
- Function: Model-directed task transformation through Lisp, shell and installed capabilities.
- Disturbance / variety regulated: Task/environment changes, tool failure, context limits and background work completing later.
- Decisive decision or feedback right: Choose next eval/action or answer based on accumulated observations.
- Decision owner: The configured task agent.
- Supporting / enforcement mechanisms: agent-loop, provider adapters, durable session facts, eval dispatch, background registry, context/recall and mutation persistence.
- Closure path: execute-tool-calls appends actual results; agent-loop recurs with updated context, reading background exits before final answers when necessary.
- Boundary reachability: Public installed runtime supplies the agent-loop and eval tool directly; model APIs provide inference rather than an imported agent harness.
- Why this is / is not agent-owned: Without the model actor there is persistence/enforcement but no equivalent task-dependent action selection.
- Evidence: [src/engine/turn.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/engine/turn.lisp); [src/engine/exec.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/engine/exec.lisp); [README.md](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/README.md).
- Basis: structural
- Confidence: high for shipped ownership.
- Caveats: No live provider, task-quality or sandbox test was run. The repository explicitly states that eval is not a security sandbox.

## S2 — Coordination

- State: A
- Function: Attenuate interference and destructive convergence among parallel task agents sharing one directory/image/artifact.
- Disturbance / variety regulated: Duplicate approaches, concurrent artifact replacement, peer function redefinition and oscillating adoption of unverified results.
- Decisive decision or feedback right: Select/revise a distinct approach, decide evidence-based adoption while preserving variation, and decide whether a candidate warrants promotion after rereading the shared best.
- Decision owner: Team nodes mutually adjusting their work through the first-party agent protocol.
- Supporting / enforcement mechanisms: Atomic slot claims, private work-K directories, LOG/DISCONFIRMED/ADOPTED, verified scores, best.lock and kernel fork-name fencing.
- Closure path: Nodes reread peers' approaches/results, change a conflicting or dominated strategy, reproduce candidate evidence and conditionally replace best under the lock; later nodes observe the new state.
- Boundary reachability: Installed pinned team cell constructs and submits these prompts to each minted full-tool session via start-nodes/node-prompt. No developer-supplied coordination agent is required.
- Why this is / is not agent-owned: Locks enforce ordering, while model nodes choose the substantive approach and adoption response. Removing their judgment leaves serialization without mutual strategy adjustment.
- Distinct S1 units: Separately minted team-node sessions with task execution and local work areas.
- Inter-S1 disturbance: Shared approach/artifact/image collisions and repeatedly replacing a peer's stronger result without reproduction.
- Attenuating coordination relation: Explicit approach differentiation, periodic peer-evidence rereads, validated adoption with retained variation, and conditional locked promotion.
- Feedback into subsequent S1 behaviour: Changed strategies and shared best/evidence influence subsequent node actions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shipped protocol explicitly names cross-node collisions/convergence and prescribes agent-chosen corrective adjustment, not merely message transport.
- Evidence: [team/cell.lisp](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-team/cell.lisp) prompt/start-nodes; [team/README.md](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-team/README.md); [src/organism/fork.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/fork.lisp) fork-fence.
- Basis: structural
- Confidence: high for the optional team mode.
- Caveats: Board messaging or fork plurality alone would not establish S2. Coordination is behavioral rather than a security isolation guarantee.

## S3 — Inside-and-now control

- State: P
- Function: Current regulation of the standing team's commitments and continuing resource use.
- Disturbance / variety regulated: Several active/idle/spent workers continuing an obsolete commitment or consuming budget under stale instructions.
- Decisive decision or feedback right: Redirect the standing team's work, stop the team or submit a new current commitment using its current collective state.
- Decision owner: Legitimate operator of the local session/standing team.
- Supporting / enforcement mechanisms: Per-node usage folding, team roster/status, budget-hook, /team control, put-input steering and replacement of spent seats.
- Closure path: /team reads current team state; /team TEXT reaches current nodes as a steer or follow-up and seats fresh nodes where spent nodes cannot continue; /team stop cancels the team.
- Boundary reachability: These are installed native slash commands on the operator's session, with node sessions explicitly refused the right to seat another standing team. This is collective current control, not a generic single-action approval.
- Why this is / is not agent-owned: Node agents own local work; the operator supplies standing-team current commitments and intervention. Automatic budget enforcement/reseating does not select the operator's decision.
- Whole-system current view: The standing-team roster, node activity/remaining spend and shared findings/artifact at the assessed team mode, exposed by result/result-text and /team.
- Current-control decision scope: Team-wide work redirection, continuation/reseating and collective stop.
- Evidence: [team/cell.lisp](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-team/cell.lisp) node-spend/node-left, seat, put-input, run-slash, result/result-text; [team/README.md](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-team/README.md).
- Basis: structural
- Confidence: medium-high, explicitly limited to the standing-team mode.
- Caveats: No autonomous S3 manager is claimed. An uninstantiated generic eval capable of management is not credited. Operator intervention over one ordinary tool call would be insufficient.

## S3* — Complementary audit

- State: A
- Function: Post-turn challenge to operational claims and user-visible changes through separate verification.
- Disturbance / variety regulated: A successful-looking task answer or write receipt despite an incorrect/unverified resulting state.
- Decisive decision or feedback right: Reconstruct the intended invariant, choose narrow direct checks and adjudicate pass/fail/blocked, then repair within bounds or return actionable findings.
- Decision owner: A separately instantiated experience reflection agent.
- Supporting / enforcement mechanisms: Frame observer, frozen parent-turn anchor, dedicated child session, verification sightings, safe-tool fence, bounded repair budget and durable recap/attention delivery.
- Closure path: Reflector reads actual results/durable facts, records evidence and verdict; a narrow supported repair is reverified, otherwise a next action/blocked finding returns to the originating session or operator.
- Boundary reachability: The pinned experience cell's installed observer and worker invoke reflect-turn/fork-reflection after eligible task turns, using the bundled verification prompt and available safe verbs.
- Why this is / is not agent-owned: The worker schedules reflection and stores its findings, but the separate agent chooses evidence and judges the invariant. Ordinary producer completion and deterministic receipt checks do not make that judgment.
- Claim being audited: That user-visible code/config/data/live-surface changes and operational claims actually satisfy their intended invariant.
- Ordinary reporting path: Original task agent answer, transcript and tool/write receipts.
- Complementary access path: Separate reflector verification using existing safe verbs to read back actual result state and durable facts; its prompt explicitly rejects a write receipt as sufficient proof.
- Independence boundary: Separate post-turn session/role and verification mandate, capable of outcome readback and challenge rather than repeating the original answer. It inherits context and may use the same model; independence is functional and limited, not a security separation.
- Who acts on findings: Reflector for one bounded allowed repair; otherwise originating task/current operator via recap and attention request.
- Evidence: [experience/reflect.lisp](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-experience/reflect.lisp) reflection-prompt/fork-reflection; [experience/cell.lisp](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-experience/cell.lisp) installed observer/worker and repair setting.
- Basis: structural
- Confidence: medium-high for this optional mode.
- Caveats: Cached inherited history can bias the reflector. Goal judges, ordinary runtime tests, candidate races and external PR triage are not separately counted as audit witnesses.

## S4 — Outside-and-then intelligence

- State: —
- Function: Outside-and-then intelligence at the declared installed-agent recursion.
- Disturbance / variety regulated: Plausible shipped regulatory paths were checked below.
- Decisive decision or feedback right: No material function-specific closure established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Mutable definitions, configuration and operator controls support operation without establishing this function.
- Closure path: No qualifying shipped closure for this function.
- Why this is / is not agent-owned: Agent access to eval does not by itself establish the separate organizational decision.
- Evidence: [src/organism/evolve.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/evolve.lisp); [src/organism/knowledge.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/knowledge.lisp); [src/organism/update.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/update.lisp); [experience/reflect.lisp](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-experience/reflect.lisp); [cyber-security/README.md](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-cyber-security/README.md)
- Basis: structural
- Confidence: medium-high, bounded to the inspected distribution.
- Caveats: Downstream deployments can add organizational behavior.

### Absence scope

- Surfaces inspected: [src/organism/evolve.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/evolve.lisp); [src/organism/knowledge.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/knowledge.lisp); [src/organism/update.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/update.lisp); [experience/reflect.lisp](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-experience/reflect.lisp); [cyber-security/README.md](https://github.com/nodecode-ai/cells/blob/39dcac03bf81b26498257586962eaa3cb15ef67d/tools/nodecode-cyber-security/README.md)
- Plausible first-party paths checked: Self-mutation/retention, candidate races/generations, experience keeps, release/hub updates and external vulnerability advisory reporting; possible operator adaptation modes.
- Why no material first-party path remains: Experience derives lessons from completed internal task operation; code racing and update application are improvement/deployment mechanisms. Cyber-security reporting executes a user-environment workload, while the external advisory-authoring organism is adjacent. None of the inspected installed paths establishes a prospective external environment model generating organizational adaptation options that return into the application's current capability regulation.


## S5 — Policy and identity

- State: —
- Function: Policy and identity at the declared installed-agent recursion.
- Disturbance / variety regulated: Plausible shipped regulatory paths were checked below.
- Decisive decision or feedback right: No material function-specific closure established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Mutable definitions, configuration and operator controls support operation without establishing this function.
- Closure path: No qualifying shipped closure for this function.
- Why this is / is not agent-owned: Agent access to eval does not by itself establish the separate organizational decision.
- Evidence: [src/organism/evolve.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/evolve.lisp); [src/organism/profile.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/profile.lisp); [src/gateway/control.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/gateway/control.lisp); [src/engine/turn.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/engine/turn.lisp); [docs/CELLS.md](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/docs/CELLS.md)
- Basis: structural
- Confidence: medium-high, bounded to the inspected distribution.
- Caveats: Downstream deployments can add organizational behavior.

### Absence scope

- Surfaces inspected: [src/organism/evolve.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/evolve.lisp); [src/organism/profile.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/organism/profile.lisp); [src/gateway/control.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/gateway/control.lisp); [src/engine/turn.lisp](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/src/engine/turn.lisp); [docs/CELLS.md](https://github.com/nodecode-ai/nodecode/blob/314476ddee650954f32695500be308276243f28b/docs/CELLS.md)
- Plausible first-party paths checked: System prompt, profile identity, kernel floor/recorded lowering, cell installation/configuration, operator trust and model access; possible parent ultimate-policy closure.
- Why no material first-party path remains: A named reason for lowering a mutation lock records a technical permission act; it does not establish an identity/ultimate-policy matter, legitimate arbitration and returned governing decision. Profiles and prompts identify/configure a process. No function-specific S5 path is supplied at the assessed recursion.


## Recursion

Anchored forks and detached team nodes are real work sessions; neither is automatically a viable recursive organization. This assessment establishes only the functions and optional modes above, not complete viability for each node.

## Variety and escalation

Durable facts, original results/recall and distinct background exits preserve task variety. Context projection and recap compress it. Team nodes retain measured contradictions and adoption lineage; blocked reflection repairs identify missing authority for the operator. Notices and attention delivery are not automatically algedonic/S5 claims.

## Evidence gaps

Source-first assessment only; no model/provider, public scanning, external PR write or operator filesystem execution was performed. Both frozen repositories were inspected at the pinned commits. Optional modes depend on enabling their first-party cells; no unknown third-party cell or maintainer-only service is credited. Behavioral coordination/audit effectiveness and security isolation were not empirically measured.
