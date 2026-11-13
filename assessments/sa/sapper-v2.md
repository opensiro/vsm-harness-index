---
harness_id: sapper-v2
project_name: sapper-v2
repository: https://github.com/N1nEmAn/sapper-v2
review_ref: 7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb
reviewed_at: 2026-11-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# sapper-v2

## Review boundary

- System in focus: bundled sapper graph CLI, skill templates and shipped Docker/tmux model-commander plus agent-worker competition deployment, not the whole separate nvwabase project or any externally hosted model.
- Purpose and identity: coordinate multiple autonomous workers toward authorized bounded scenario goals while preserving facts and extracting transferable knowledge.
- Relevant environment: competition's authorized challenge containers and scoring interface, configured model services, tmux, Docker/Python, goal facts and deployment operator.
- Standard-distribution boundary: lib/sapper.py, source-shipped templates, Docker commander SKILL/SPEC, worker and watchdog scripts, graph state and supported CLI role wiring.
- Credited operating / distribution surfaces: reasoning/explore/verify model dispatch, first-party Commander current-control loop, shared fact-intent graph and messaging, cross-case adaptation instruction.
- Adjacent first-party surfaces excluded from ownership: benchmark event recounts, images, third-party nvwabase future ambitions, unsupported generic scenarios and competitive scoring as an external verdict.
- First-party operating / deployment modes considered: CLI graph/dispatch and auto --verify; Docker deployed model Commander with agents/workers; bounded authorized multi-challenge mode and operator setup.
- Recursion level: bounded competition-campaign organization with multiple challenge/worker S1 cells, a current-control Commander and external human authorizer.
- Reviewed revision: 7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb.
- Observation date: 2026-11-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

A Python standard-library fact-intent graph records validated observations, dependent intents, claimed work and human confirmations. Model-driven reason/explore/verify roles can be dispatched separately or through a bounded auto-loop. Docker/tmux commander distribution starts a standing model session that reads a whole-campaign board each cycle, assigns specialized workers, selects resource tiers and transfers confirmed cross-case findings by hints/messages. The watchdog handles runtime recovery only. The external model/arena are dependencies, not first-party audited performance. Evidence: [README.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/README.md), [lib/sapper.py](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/lib/sapper.py), [docker/commander/SKILL.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SKILL.md), [docker/commander/SPEC.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SPEC.md).

## Operational model

The commander performs discretionary S2/S3 control of separate worker operations and prospective tactical transfer; workers solve scoped assigned intents. Independent verify mode uses fresh model inspection of recorded claims. Deterministic graph locks, time limits and tmux state are machinery, not autonomous decisive owners. Parent operator defines ultimate scope externally.

## S1 — Operations

- State: A
- Function: Agent-owned authorized challenge/task execution by mission-scoped workers.
- Disturbance / variety regulated: Unknown environment responses, incomplete task results, missing proofs and changing local facts.
- Decisive decision or feedback right: Worker agent chooses investigation actions and declares produced evidence/facts for its assigned intent.
- Decision owner: External model-backed agent invoked through shipped first-party work interface/role instructions, within authorized arena scope.
- Supporting / enforcement mechanisms: Fact-intent graph, tmux worker script, claim/conclude, typed facts and host tool runtime.
- Closure path: Commander assigns challenge/intent → worker executes and records evidence → fact graph and board update → next agent work is informed.
- Boundary reachability: Shipped Docker commander entrypoint and worker.sh start provider-backed panes; CLI dispatch and auto-loop call run_claude on explore intents.
- Why this is / is not agent-owned: Shell scripts and graph locks cannot determine how to solve a new task absent the reasoning worker.
- Evidence: [docker/commander/entrypoint.sh](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/entrypoint.sh), [docker/commander/worker.sh](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/worker.sh), [lib/sapper.py](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/lib/sapper.py), [SKILL.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/SKILL.md)
- Basis: structural
- Confidence: medium-high
- Caveats: No live competition/model run; historical performance numbers and future designs are not re-proven.

## S2 — Coordination

- State: A
- Function: Coordinate multiple separate worker agent cells sharing work and environment capacity.
- Disturbance / variety regulated: Overlapping challenge activity, redundant exploration, reused instance capacity and inconsistent findings.
- Distinct S1 units: Commander-governed general/scout/soldier panes or separately claimed fact-graph intents.
- Inter-S1 disturbance: Two workers can duplicate one intent and consume scarce arena/agent slots or disagree on shared findings.
- Attenuating coordination relation: Commander reads live board, assigns different missions and roles, creates per-challenge shared graph, sends cross-worker messages and orders pane retirement/retargeting.
- Feedback into subsequent S1 behaviour: Worker reports, new facts and board state trigger commander reassignment or terminate/restart worker paths.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The commander makes contextual decisions to avoid redundant workers and conflicting shared resource claims, not merely relays chat; claimed-intent idempotence is supporting enforcement.
- Decisive decision or feedback right: Contextual task partition, role assignment and correction of overlap.
- Decision owner: Model-backed field Commander under supplied first-party doctrine.
- Supporting / enforcement mechanisms: worker.sh, board, graph claims, pane lifecycle, shared per-challenge graph and watchdog.
- Closure path: Board evidence → Commander message/spawn/kill → specific worker mission changes → next facts/output feed new coordination decisions.
- Boundary reachability: Shipped Docker commander runtime loads its role SKILL and uses worker.sh; lib/sapper.py offers operational claims/dispatch.
- Why this is / is not agent-owned: Deterministic locks can prevent two writes, but no longer decide which challenge/task gets another specialist or alternate tactic.
- Evidence: [docker/commander/SKILL.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SKILL.md), [docker/commander/SPEC.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SPEC.md), [docker/commander/worker.sh](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/worker.sh), [lib/sapper.py](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/lib/sapper.py)
- Basis: structural
- Confidence: medium
- Caveats: Only supported constrained competition deployment; external nvwabase's full architecture is not silently credited.

## S3 — Inside-and-now control

- State: A
- Function: Whole-campaign control of current worker capacity, problem priority and active commitments.
- Disturbance / variety regulated: Underproductive workers, stalled challenges, few available slots, time remaining and allocation between easier/harder cases.
- Whole-system current view: The commander's every-cycle worker.sh board, challenge/pane state and persistent commander-state.md.
- Current-control decision scope: Allocate scarce active instances and model tiers, stop or replace unproductive panes, park/reopen work, and choose cross-challenge priorities.
- Decisive decision or feedback right: Select whole-campaign real-time resource and commitment intervention.
- Decision owner: First-party model-backed Commander, distinct from deterministic watchdog.
- Supporting / enforcement mechanisms: Board views, time budget and pane limit, worker.sh verbs, watchdog restart and model tier configuration.
- Closure path: Current board → Commander intervention → spawned/killed/redirected workers and changed budgets → board reports resulting work.
- Boundary reachability: Commander container entrypoint loads standing role loop and board/worker tools; watchdog only preserves process and credentials.
- Why this is / is not agent-owned: Remove Commander and the watchdog still restarts processes but no meaningful campaign-wide prioritization or reallocation occurs.
- Evidence: [docker/commander/SKILL.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SKILL.md), [docker/commander/SPEC.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SPEC.md), [docker/commander/watchdog.sh](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/watchdog.sh)
- Basis: structural
- Confidence: high for shipped constructor/owner
- Caveats: This is source-first role reachability, not a newly observed autonomous live intervention.

## S3* — Complementary audit

- State: A
- Function: Separately verify recorded operational evidence before treating executor claims as reliable.
- Disturbance / variety regulated: Worker could claim a fact without independently validated underlying proof.
- Claim being audited: Executor's completed intent and resulting fact/evidence.
- Ordinary reporting path: Worker writes a fact and concludes the original intent.
- Complementary access path: A separately invoked verifier model reads original intent/result and is instructed to recheck proof rather than trust worker summary.
- Independence boundary: Verifier call is distinct from the explore executor model invocation and uses separate verify.md evidence-focused instructions; prior graph claim is untrusted context.
- Who acts on findings: CLI/auto-loop marks FAILED with nonzero result or adds a verification-failure fact to graph for subsequent reasoning and work.
- Decisive decision or feedback right: Verifier independently judges true/false with documented evidence and returns an actionable result.
- Decision owner: Dedicated model-backed verifier path available in shipped CLI/optional auto --verify mode.
- Supporting / enforcement mechanisms: Fact graph, intent IDs, verify.md, parser, exit status and auto-loop update.
- Closure path: Executor fact → independent verify command/model → verified/failed judgment → error fact or nonzero exit → subsequent reasoning/current work adjusts.
- Boundary reachability: The shipped lib/sapper.py implements dispatch verify and auto --verify, wiring dedicated model invocation to feedback; standard SKILL advertises both.
- Why this is / is not agent-owned: Model judge resolves evidence truth; syntactic graph validators merely check structure.
- Evidence: [lib/sapper.py](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/lib/sapper.py), [templates/verify.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/templates/verify.md), [SKILL.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/SKILL.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Requires enabling verify path; no independent provider-backed confirmation of any particular frozen historical finding.

## S4 — Outside-and-then intelligence

- State: A
- Function: Generate and circulate prospective cross-task adaptations from confirmed findings to improve capability on related future cases.
- Disturbance / variety regulated: New discovered environment patterns make earlier techniques obsolete or reusable across task families.
- External distinction: Worker findings from other challenge instances, family patterns and confirmed transferable constraints.
- Future / prospective distinction: Commander decides which technique transfers to other, not-yet-solved challenges and changes their subsequent work instructions.
- Adaptation option generated: Agent selects a confirmed pattern, identifies target sibling problems and formulates guidance/changed worker mission.
- Path back into current capability / S3: First-party hint/msg tools insert new shared graph context and directive into other worker panes; their next analysis can use it.
- Decisive decision or feedback right: Choose future-relevant transfer and adapt work approach for a different task family.
- Decision owner: Model-backed Commander following embedded intel-transfer and family-transfer doctrine.
- Supporting / enforcement mechanisms: Layered fact graph, commander persistent state, worker messaging and skill instructions.
- Closure path: Externally discovered confirmed method → Commander recognition of cross-case relevance → hint/msg to another S1 team → changed later exploratory operation.
- Boundary reachability: Commander default role SKILL mandates transferable-intel check each loop; worker.sh provides operational hints and messages to shipped worker panes.
- Why this is / is not agent-owned: Generic history persistence alone is not S4; the model Commander identifies transfer opportunities and constructs targeted prospective change.
- Evidence: [docker/commander/SKILL.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SKILL.md), [docker/commander/worker.sh](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/worker.sh), [README.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/README.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded to campaign-level prospective tactic transfer, not permanent self-modification or general market forecasting; historical campaign claims not independently reproduced.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/policy reconsideration and legitimate deciding return at this recursion established.
- Disturbance / variety regulated: Competition scope rules, time budget and mission ethics are fixed externally, not renegotiated by a governed first-party S5.
- Identity / ultimate-policy issue: Potential changes to ultimate organization purpose, authorized operating scope or legitimate rule owner.
- Ultimate authority in each claimed mode: External human/competition operator supplies scope and doctrine; configured constants/guardrails are not themselves an S5 decision process.
- Return-to-operation path: Existing rules constrain execution, but no first-party identity-level matter → legitimate owner judgment → changed charter return is demonstrated.
- Decisive decision or feedback right: Not present as a shipped S5 path.
- Decision owner: No positive first-party S5 owner established.
- Supporting / enforcement mechanisms: Scope restrictions, static commander doctrine, human setup and service credentials.
- Closure path: Static constraints are enforced; no independent S5 charter decision loop.
- Why this is / is not agent-owned: The commander can revise tactics within fixed ultimate mission but has no authority to redefine ethical or legal operating purpose.
- Evidence: [docker/commander/SKILL.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SKILL.md), [README.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/README.md), [docker/commander/SPEC.md](https://github.com/N1nEmAn/sapper-v2/blob/7b75e6f1f5d5b4ae0c55878b0dd0994d9b08f1fb/docker/commander/SPEC.md)
- Basis: structural negative
- Confidence: medium
- Caveats: Human owners may supervise the surrounding operation, but ordinary rules/mission setup alone cannot supply parent S5.

### Absence scope

- Surfaces inspected: shipped commander role, container entrypoint, source setup, graph CLI, worker permissions, operator config and scope docs.
- Plausible first-party paths checked: doctrine updates, operator scope changes, historical commander's saved state and tactical mission rewrites.
- Why no material first-party path remains: source describes bounded delegated campaign control, not an identity-level charter matter reaching an authorized ultimate authority and returning into operations.

## Distributed OSS parent arrangement

An authorized campaign's human operator provides external ethical/mission boundary. Contributors and model vendors do not constitute shared first-party ultimate authority. No organization-level S5 claim follows from public source.

## Recursion

Each challenge/worker is an operational S1 cell under one model Commander. Commander controls scarce shared capacity and cross-case coordination, and transfers information to future challenge teams. CLI graph has a lower-level intent recursion.

## Variety and escalation

Shared graph facts and claims attenuate duplicated intents; board state and worker reports feed model decisions on priorities/resource use. Failed verification is surfaced for repair and later reason cycles. Watchdog handles crashes and key rotation but owns no strategy. Operator authority over scope remains external.

## Evidence gaps

- No live competition, model session or arena side effects were executed by this assessment.
- Historical score, autonomous invention and benchmark claims in README/BATTLE-REPORT were not independently reproduced or treated as standalone grade proof.
- S3* reflects a separately reachable optional verification mode, not a guarantee every worker result was audited.
- S4 is limited to prospective cross-case learning/mission transfer in the specified campaign, not autonomous source-code rewriting or unrestricted general adaptation.
