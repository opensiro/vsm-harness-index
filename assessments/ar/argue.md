---
harness_id: argue
project_name: argue
repository: https://github.com/onevcat/argue
review_ref: 7939e67c8479aa3b9f5d070f5e7feff8b90f876d
reviewed_at: 2026-10-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# argue

## Review boundary

- System in focus: The shipped `@onevcat/argue` deliberation engine as actually wired by the `@onevcat/argue-cli` standard headless operating mode. One user topic becomes a multi-participant model-backed debate, claim/vote resolution, representative speech and optional delegated action. This is **not** the separate Anthropic/OpenAI model provider, independent third-party coding CLIs, or the repository's contributor organization.
- Purpose and identity: Produce an inspectable, multi-perspective argument/consensus report on a specified question through configured independent model participants.
- Environment: User topic and context, supplied participants and round settings, participant answers, disagreements, timeouts/failures, provider output, optional action request and local result consumers.
- Standard-distribution boundary: First-party `packages/argue` engine/contracts and packaged `packages/argue-cli` headless runner, with supported `api`, `sdk`, `cli` providers. External provider reasoning is borrowed; the harness assembles and invokes distinct participant actors with persistent per-participant sessions, prompt schema, iterative critique, final vote and result. `mock` is a test adapter, not positive autonomy evidence.
- Credited operating / distribution surfaces: [headless assembly](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/headless-run.ts#L1-L65), [real provider dispatch](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/runtime/delegate.ts#L27-L142), [model-backed API adapter](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/runtime/api.ts#L1-L49), [engine start/rounds](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L42-L345), [round dispatch and feedback](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L390-L584), [scoring](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/scoring.ts#L1-L108).
- Adjacent first-party surfaces excluded from ownership: UI report viewer, local examples, tests, CI/maintenance, repository governance, runtime vendors' own agentic capabilities, and operator-created downstream workflows not composed into the shipped engine.
- Standard modes considered: Multi-participant headless run using API/SDK/external CLI providers, round-voting/claim merge, optional model-drafted report and post-report delegated action; library mode requires host-supplied delegate and is not independently counted as closed until instantiated by the shipped CLI.
- Recursion: One deliberative service handling a user request; configured participants are S1 contributors to the argument product, not each an independently verified viable metasystem.
- Frozen reviewed revision: `7939e67c8479aa3b9f5d070f5e7feff8b90f876d` from immutable [discovery #2036](https://github.com/opensiro/vsm-harness-index/issues/2036), row 2 in [serial batch #2037](https://github.com/opensiro/vsm-harness-index/issues/2037). Reviewed 2026-10-25 against Profile 0.2.4 / Methodology 0.3.7.

## Repository architecture

`executeHeadlessRun` composes the first-party `ArgueEngine`, a configured `AgentTaskDelegate`, session state and an event observer. `createTaskDelegate` dispatches participant tasks to selected provider runners and normalizes their outputs. The real API runner invokes `generateText` against the configured model, while CLI runners spawn installed provider executables. Thus the model's internal reasoning and external CLI agent loop are not credited to argue, but its participant-task construction, provider invocation, interactive feedback and returned debate report form the shipped system's operating loop. [headless wiring](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/headless-run.ts#L14-L68); [provider selection](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/runtime/delegate.ts#L126-L154); [real generation](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/runtime/api.ts#L12-L50).

The engine dispatches initial contributions, subsequent debate and final votes to active model participants. Before subsequent rounds each participant receives bounded peer output and active shared claims; model participants may propose revisions or duplicate-claim merges. The engine implements those revisions and merges, computes threshold-based resolutions, chooses a representative by deterministic peer-derived scores, optionally asks that participant to compose a report, and optionally delegates an action after debate. This supports a **narrow S2-specific reconciliation constructor** for conflicting contributions; scoring, representative selection and optional execution remain product/session mechanisms, not automatically organization-wide S3 or later metasystem control. [round phases](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L98-L285); [claim merging](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L1137-L1278); [voting](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L1296-L1351).

## Operational model

The primary S1 units are model-backed participants assigned roles and a common question. Each has an environment of previous debate output and shared claims and makes discretionary language/content judgments: arguments, critiques, revisions and final votes. First-party code sequences, validates, records and forwards the product and ultimately returns a structured result. The host chooses task, models, scoring policy, timeouts, maximum rounds and optional action; provider vendors handle inference. Waiting/cancel, active participant filtering, event logs and score aggregation enforce the prescribed debate protocol.

## S1 — Operations

- State: A
- Function: Generate independent argument, critique, claim refinement and votes for a user-directed deliberative outcome.
- Disturbance / variety regulated: Open-ended user questions, competing interpretations, prior participant arguments, claim disagreements and unpredictable model responses.
- Decisive decision or feedback right: Each configured model participant decides its proposed arguments, whether a claim is accepted/rejected/revised/merged and its final vote; subsequent prompts incorporate its output and peers' outputs.
- Decision owner: Shipped, configured first-party participant task loop invoking actual API/SDK/CLI model actors. The model provider executes inference, but argue assembles and operationally invokes the distributed deliberation actors and routes their judgments to subsequent phases.
- Supporting / enforcement mechanisms: Zod input/output contracts, per-participant sticky sessions, model adapters, structured prompts, claim IDs, round budgets, waiting policies and result storage.
- Closure path: User task and configured model participants → `executeHeadlessRun` → `ArgueEngine.start` → real `taskDelegate.dispatch`/provider inference → round outputs and peer feedback → next-round judgment/final vote → consensus/report/result delivered to caller.
- Boundary reachability: The standard CLI connects the concrete `ArgueEngine` to `createTaskDelegate`; real provider runners, not only abstract host interfaces, execute model prompts. The library's uninstantiated delegate alone is insufficient, but the installed CLI mode closes it.
- Why this is / is not agent-owned: Remove the invoked model participants and there is no discretionary argument, critique or vote, only a deterministic schema/wait/score pipeline. Agent content choices are the decisive operational judgments, even if the model weights and vendor implementation are external.
- Evidence: [wired headless runtime](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/headless-run.ts#L14-L66); [dispatch](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L390-L490); [API model call](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/runtime/api.ts#L12-L48); [debate prompt](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L913-L973).
- Basis: Structural first-party standard-mode loop; no runtime/model-quality experiment.
- Confidence: High for source-supported loop assembly, no claim about live response quality.
- Caveats: Provider SDKs/external coding CLI agents are dependencies; their internal task rights and governance are not argue-owned. CLI `mock` does not establish autonomy.

## S2 — Coordination

- State: C
- Function: A narrowly exposed deliberation-coordination constructor reconciles incompatible contributions from separately configured S1 participant work cells into a usable collective claim set.
- Disturbance / variety regulated: Independent participant answers can contradict one another, duplicate factual claims or repeatedly reintroduce already-merged propositions, destabilizing the coherence of the group's shared response. This is a concrete cross-participant consistency conflict, not mere process concurrency.
- Distinct S1 units: At least two separately configured and invoked model participants, each with a distinct `participantId`, role, sticky session, output and per-round model call; their generated answers supply the competing contributions.
- Inter-S1 disturbance: An output's `judgements` may disagree with another participant's active claim or propose `mergesWith` for a duplicate; redundant claim IDs and inconsistent statements would otherwise persist into future rounds.
- Attenuating coordination relation: The first-party `updateClaims` merges duplicates, remaps references to the surviving claim, accepts revision suggestions, limits visible claims to active items, and republishes bounded peer responses plus the shared revised catalog to every subsequent participant round. Final individual claim votes are reduced by a configured consensus threshold.
- Feedback into subsequent S1 behaviour: `runRound` builds each later participant prompt with updated `claimCatalog` and opposing `peerRoundInputs`; previously merged claims are excluded from active catalog and debate prompts explicitly forbid reopening already merged claims. A model's next judgment therefore receives the resolved shared distinctions.
- Decisive decision or feedback right: The first-party debate engine supplies the reconciliation and vote feedback path; model participants choose substantive critiques/merge proposals, while the host selects roles, number of rounds, policies and consensus threshold. It does not install an autonomous general-purpose inter-agent conflict manager.
- Decision owner: A **function-specific first-party constructor**, closed for the bounded discussion mode but with coordination policy/authority still composed by the host. Content autonomy belongs to participant S1s; deterministic merge and threshold application do not transfer general S2 policy ownership to a model.
- Supporting / enforcement mechanisms: Shared claim ID catalog, round feedback payload, `DefaultWaitCoordinator`, active participant set, timeout/cancel, bounded peer context, merged claim graph and fixed early-stop threshold.
- Closure path: Two or more agents emit conflicting claims → S2-specific claim/judgment reducer normalizes revisions and merges → catalog plus peer objections return in next-round prompts → agents can revise and final-vote → bounded consensus/disagreements returned in the result.
- Boundary reachability: Shipped `argue-cli` wires real provider delegates to `ArgueEngine.start`; its `runRound` repeatedly invokes `updateClaims` and repackages the new catalog/peer objections before final voting. This is active in the normal multi-participant deliberation path, not just a developer example or generic queue.
- Why this is S2-specific rather than generic routing: The code specifically recognizes disagreement and semantic overlap as a conflict, transmits opposing arguments for revision and prevents merged claims from oscillating back into the active dispute. Mere parallel dispatch, timeout or participant identity would not establish this witness.
- Why this is / is not agent-owned: Model actors choose substantive merge/critique proposals, but removing a hypothetical independent S2 agent leaves the same developer-defined reconciliation protocol, prompt cadence and threshold. The shipped construct is `C`, not fully autonomous S2 `A`.
- Evidence: [distinct round task dispatch and peer input](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L390-L490); [claim merge and canonicalization](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L1137-L1293); [debate anti-reopening prompts](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L930-L958); [final resolution votes](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L1296-L1351).
- Basis: Structural first-party cross-participant disagreement/reconciliation witness; narrow exposed S2 constructor with real CLI wiring.
- Confidence: Medium-high for the feedback path; no evidence that models reach factual correctness or agreement empirically.
- Caveats: This S2 claim concerns contradictions *between discussion contributors*, not runtime tool/resource contention across unrelated agent work. The first-party method resolves claim identity/revisions mechanically; autonomous organizational conflict-policy ownership is not established.

## S3 — Inside-and-now control

- State: —
- Function: No first-party global present resource/commitment management of independently operating units at the service level beyond fixed single-request debate rules.
- Disturbance / variety regulated: Failed participants, elapsed deadlines, differing scores and incomplete votes; these are session-level outcome constraints, not proven whole-service commitments requiring S3 discretion.
- Decisive decision or feedback right: The engine deterministically eliminates failed/timed-out participants, computes scores and chooses the representative final speaker. It does not review/reallocate overall ongoing organizational priorities or resource commitments based on a whole-current operational view.
- Decision owner: Fixed runtime policy from the host's start request; no installed S3 agent or composed S3-specific delegated judgment. Selecting a final report voice is a product output decision.
- Supporting / enforcement mechanisms: Session store, metrics, state machine, minParticipants, per-task timeout, scoring tie-break, explicit representative configuration.
- Closure path: Round failure removes one debate participant, and scores choose final speech/report composer. No observed whole-service current-control decision changes multiple operations or allocates scarce resources under a global manager.
- Why this is / is not agent-owned: Deterministic score and failover rules regulate one debate run. They do not establish autonomous S3 ownership or an independently composed S3 parent-control mode.
- Evidence: [participant lifecycle / score / representative](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L111-L345); [scoring](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/scoring.ts#L14-L106); [timeout](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/wait-coordinator.ts#L54-L155).
- Basis: Bounded negative, excluding mere fixed workflow/selection from S3.
- Confidence: Medium-high for this one-request recursion.
- Caveats: A calling institution may exercise its own S3 over repeated deliberation runs, but that actor is not automatically a built-in argue metasystem.

### Absence scope

- Surfaces inspected: Start input policies, engine state machine, participant health/timeouts, scores, final representative, request state and CLI run artifacts.
- Plausible first-party paths checked: Auto-elimination and retries, run-wide deadlines, score-driven speaker selection, user-designated speaker and optional action actor.
- Why no material first-party path remains: Decisions close fixed session protocol or content publication; none shows whole-current authority over actual cross-unit organizational resource/commitment regulation and its feedback into continuing operations.

## S3* — Complementary audit

- State: —
- Function: No independently sourced inspection of operational facts complementing routine participant claims and returning corrective evidence to an S3 current-control owner.
- Disturbance / variety regulated: Incorrect participant arguments or votes may degrade the result, but ordinary debate challenge and score calculations reuse participants' own text/judgments.
- Decisive decision or feedback right: Participants critique each other and the engine scores them using peer agreement and text-derived metrics; no separate audit authority samples external task truth or replays actual independently observed operational results.
- Decision owner: Regular debate participants and deterministic scoring/report code; no first-party complementary auditor with independent access to the operational environment.
- Supporting / enforcement mechanisms: Full round record, structured claims, disagreements, final votes, JSONL events and stored report.
- Closure path: Peer critiques become ordinary next-round input and vote totals become report content; no independent audit finding is routed to a distinct current-control correction function.
- Why this is / is not agent-owned: Peer disagreement is intentionally the S1 product; a consensus score or review prompt is not by itself complementary direct access to reality.
- Evidence: [peer-review correctness from participants' votes](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/scoring.ts#L109-L168); [round reports/votes](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L1296-L1351); [headless observer](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/headless-run.ts#L14-L42).
- Basis: Bounded negative despite nontrivial first-party critique and traceability.
- Confidence: Medium-high for shipped operating mode.
- Caveats: A host can supply evidence to a topic or build an external validator, but no distinct shipped audit-to-control path is established by doing so.

### Absence scope

- Surfaces inspected: Peer criticism and final votes, weighted correctness score, stored full responses, logs, structured report and optional action.
- Plausible first-party paths checked: Multi-model independent opinions, explicit objections, truth/correctness scoring, participant elimination and report fallback.
- Why no material first-party path remains: All judgments come from the debate's ordinary data and participant outputs; no independent direct-ground-truth source, separate audit owner or return to an S3 corrective decision is wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: No installed external/future sensing, capability-adaptation option selection and return to present organizational operations.
- Disturbance / variety regulated: Changing user needs or model reliability might motivate future adaptation, but the engine instead performs the one requested deliberation with preconfigured modes.
- Decisive decision or feedback right: User chooses models/policy and debate topic; participants reason about that topic. They do not choose and install future capability changes for argue.
- Decision owner: Host/operator outside the assessed loop for configuration and upgrades; current model participants for task content.
- Supporting / enforcement mechanisms: API/provider configuration, round policies, participant roles, debate history, result artifacts.
- Closure path: Participant thoughts can discuss future topics but terminate as an answer/report/action; no outside prospective observation → adaptation option → S3/present capability update loop.
- Why this is / is not agent-owned: Topic exploration or model-driven answer revision within one debate is ordinary S1, not organizational future-intelligence governance.
- Evidence: [start/run protocol](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L52-L110); [config-selected provider models](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue-cli/src/runtime/delegate.ts#L26-L54); [optional action as task](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L703-L770).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: The software may be embedded in a prospective intelligence service; that downstream application is not shown by this shipped debate CLI.

### Absence scope

- Surfaces inspected: Topic/round policy, participant roles, optional action, report composition, CLI provider configuration and result persistence.
- Plausible first-party paths checked: Debate over future decisions, cross-round learning/claim revision, provider selection and post-consensus action.
- Why no material first-party path remains: These address a bounded user topic or user-chosen configuration; there is no standing capability adaptation function with environmental foresight and return to ongoing organizational control.

## S5 — Policy and identity

- State: —
- Function: No shipped ultimate-identity dispute/decision and binding return route at the deliberation service recursion.
- Disturbance / variety regulated: Role and scoring policy may change the character of an answer, but the service's identity, legitimate purpose and final authority remain determined by the caller/developer.
- Decisive decision or feedback right: Host chooses topic, roles, model/round policies and optional post-debate action. Participants' threshold votes accept **claims**, not alter the service's ultimate purpose or authorization constitution.
- Decision owner: User/operator for inputs and runtime settings outside any in-product identity deliberation. No autonomous or parent-owned closed S5 issue escalation/return path is installed.
- Supporting / enforcement mechanisms: Input schema, constraints field, selected representative, consensus threshold, permission-sensitive external CLI execution options.
- Closure path: Votes are returned as a bounded result and may inform a caller; the shipped engine does not turn an identity/policy dispute into an authoritative new rule governing future runs.
- Why this is / is not agent-owned: Consensus on a debate claim is not organizational S5. A system-prompt role, fixed constraints or user task approval likewise does not establish ultimate policy authority.
- Evidence: [input/engine contract](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/contracts/request.ts); [claim consensus criteria](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L1296-L1351); [action delegates](https://github.com/onevcat/argue/blob/7939e67c8479aa3b9f5d070f5e7feff8b90f876d/packages/argue/src/core/engine.ts#L703-L814).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: External applications could deliberately deploy argue as a democratic policy procedure, but no normal-mode identity-level return path is demonstrated in this repository.

### Absence scope

- Surfaces inspected: Configuration, participant prompts and roles, threshold vote, report representative/optional action, engine state and public CLI entry.
- Plausible first-party paths checked: Consensus-vote-to-authority, human-chosen representative, prompt constraints, final action actor and developer-defined organization governance.
- Why no material first-party path remains: The validated decisions concern answers and session execution; no evidence of an escalated ultimate identity question, legitimate final authority and binding policy change to subsequent service operations.

## Distributed OSS parent arrangement

`onevcat/argue` is shipped as a library/CLI executable used by individually configured local hosts. A public contributor project does not provide a shared organization-wide runtime or proven S3/S4/S5 decision return to each installation. Maintainer issues/CI and provider vendor policies remain outside this assessed product boundary.

## Self-hosted and non-human modes

The standard headless run may be unattended and involve multiple independently configured LLM participants. This establishes S1 product autonomy, not automatically complete organizational metasystems. Users choose topic, models and policy. No parent-governed S3/S4/S5 alternate closure is evidenced merely by host configuration and human control of executable startup.

## Recursion

Each model participant has a durable role and in-run session history, but participates in one host-designed discussion. The source does not show each participant independently controlling resources or maintaining its own S2–S5 loop. A host embedding the debate result into a larger operational organization is a separate unassessed recursion.

## Variety and escalation

Open-ended questions enter through model participants, peer output amplifies contrasting claims, round/context/time limits attenuate volume and timeouts eliminate failing participants. The consensus threshold returns unresolved or partial results when there is no sufficient agreement; these are bounded product statuses, not a demonstrated system-level algedonic signal or ultimate policy arbitration.

## Evidence gaps

- No live model, provider, browser or external-agent quality tests were executed; the source proves an available first-party loop, not that a particular model reaches useful consensus.
- `S2=C` is confined to the supported multi-participant discussion: the first-party catalog/peer-feedback protocol regulates a specific inter-participant contradiction/duplicate-claim disturbance. It does not establish autonomous S2 policy discretion or coordination of external tool/resource conflicts.
- S3-like metrics, participant elimination and representative selection exist, but are session rules and product publication decisions rather than a whole-current S3 authority loop. No autonomous S3 right is inferred from deterministic scoring.
- Source-supplied `AgentTaskDelegate` in library mode depends on a host; the shipped CLI demonstrates actual reachable API/SDK/CLI model connectors. Third-party tools' internal agent machinery is not attributed to argue.
- Operator behavior and external institutional uses of the result are not observed, and no parent mode is inferred from static CLI options.
