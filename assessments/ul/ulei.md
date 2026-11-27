---
harness_id: ulei
project_name: ulei
repository: https://github.com/pasekahq/ulei
review_ref: 6f0132775c0bd13264c0abfb74ff367aa5e46160
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# ulei

## Review boundary

- System in focus: The first-party ulei personal-assistant distribution, including the configurable Python hive task service documented in the same source tree.
- Purpose and identity: Serve an owner's conversation, inbox and delegated card-based work using durable state.
- Relevant environment: Self-hosted Rust processes and the configured Python dispatcher, connected to the external qb model gateway and configured head executors.
- Standard-distribution boundary: The engine run and serve modes, C6 turn and inbox integration, garden/night services, and the documented hive-py deployment with its own task store and shipped role prompts.
- Credited operating / distribution surfaces: Engine turn construction, journal and tools, Python hive dispatcher, panel, reviewer, and steward apply mode.
- Adjacent first-party surfaces excluded from ownership: Placeholder Rust hive/glue, CI and model evaluation, old secretary implementation, private owner texts and launcher logic, and qb gateway internals.
- First-party operating / deployment modes considered: CLI runs, socket-served assistant, optional garden maintenance and optional Python card operation, judging, panels and steward.
- Recursion level: One owner-operated deployment. Hive cards and role sessions are cells within its task service.
- Reviewed revision: 6f0132775c0bd13264c0abfb74ff367aa5e46160
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The Rust engine constructs the model request from the journal, owner turn and configured tools. C6 supports socket-served turns and the inbox passes events through its distinct service. Garden and archive integrations use separate sockets. The first-party Python hive currently supplies task cards, workspaces, a durable dispatcher, independent reviewer runs, mechanical acceptance and model judging; the Rust hive is a placeholder. Its operators configure the gateway, executors, lanes, and optional daily steward.

## Operational model

The assistant model chooses tools, reacts to results and emits a persistent answer. The hive launches bounded head runs and turns accepted or disputed outcomes into card states and delivery. Its panel heads produce independent reports, its synthesis head closes a shared deliverable, and its steward and reviewer act on different current-work and evidence surfaces.

## S1 — Operations

- State: A
- Function: Resolve an owner's request in the first-party assistant and record the turn.
- Disturbance / variety regulated: New inputs, incomplete context, tool failures and model response variation.
- Decisive decision or feedback right: Select and use available tools, incorporate observations and return a final response.
- Decision owner: The model actor driven by the shipped ulei loop.
- Supporting / enforcement mechanisms: Tool registry, gateway, policies, retry and compaction logic, journal.
- Closure path: The engine feeds tool results into the turn until the model returns an answer or the runtime terminates. The resulting turn is appended to the journal.
- Boundary reachability: The native run and serve entry points construct and invoke the same standard agent loop from configuration.
- Why this is / is not agent-owned: The gateway supplies inference. Removing the model's choices leaves execution and storage machinery without a discretionary response path.
- Evidence: [crates/engine/src/main.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/main.rs#L119-L155), [crates/engine/src/main.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/main.rs#L501-L516), [crates/engine/src/main.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/main.rs#L545-L585), [crates/engine/src/agent.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/agent.rs#L451-L519)
- Basis: Structural, from pinned first-party source and deployment documentation.
- Confidence: high
- Caveats: The revision describes itself as pre-alpha. This is source evidence for reachable behavior.

## S2 — Coordination

- State: A
- Function: Coordinate independent panel heads whose outputs must become one accepted card deliverable.
- Disturbance / variety regulated: Heads can produce conflicting conclusions and competing deliverables for the same brief.
- Decisive decision or feedback right: Independently produce each contribution, then decide how to reconcile discrepancies and merge outputs into the accepted workspace.
- Decision owner: The configured synthesis model owns the reconciliation judgment. The dispatcher enforces member separation and completeness.
- Supporting / enforcement mechanisms: Dedicated member directories and reports, successful-report readiness check, and synthesis completeness check.
- Closure path: Members write only their own reports/workspaces in the supported panel path. The synthesis head reads each and puts a reconciled result in the shared card workspace. A missing member blocks transition to acceptance and generates retry feedback.
- Boundary reachability: The first-party hive wires a panel card to member execution, synthesis and mechanical acceptance.
- Why this is / is not agent-owned: Removing synthesis leaves independent reports and completeness checks, with no choice among materially incompatible work products.
- Distinct S1 units: Distinct panel heads with separately persisted runs, workspaces and reports on the same card.
- Inter-S1 disturbance: Reconciling conflicting answers while preserving independent evidence and one shared deliverable.
- Attenuating coordination relation: Separate contribution spaces, gather all fresh successful results, then commission explicit cross-report reconciliation by one agent.
- Feedback into subsequent S1 behaviour: The reconciled workspace enters the card gate. Omitted or missing member evidence keeps the card in the work loop.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Synthesis explicitly resolves disagreements and has the only shared deliverable handoff. Independent heads and a queue alone would not settle those conflicts.
- Evidence: [hive-py/hive/heads.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/heads.py#L318-L330), [hive-py/hive/heads.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/heads.py#L369-L381), [hive-py/hive/dispatcher.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/dispatcher.py#L588-L626), [hive-py/hive/dispatcher.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/dispatcher.py#L1623-L1643)
- Basis: Structural, from pinned first-party source and deployment documentation.
- Confidence: high
- Caveats: The result applies to panel cards in the optional Python hive.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current hive commitments by choosing which eligible cards to cancel and which related cards to retain.
- Disturbance / variety regulated: Redundant, superseded or competing commitments on the active task board.
- Decisive decision or feedback right: Select specific eligible cards for authoritative cancellation, with an optional retained-card witness.
- Decision owner: The daily steward model in configured apply mode.
- Supporting / enforcement mechanisms: Board snapshot, protected-card rules, validated model response, version checks and operation journal.
- Closure path: Validated cancellation calls update card state through the hive command. Subsequent dispatcher scans exclude cancelled cards.
- Boundary reachability: The Python hive ships the steward script, board snapshot, model call, plan validator and apply path.
- Why this is / is not agent-owned: Safety checks constrain the steward's action. For non-exact duplicate decisions they do not choose the cancellation set.
- Whole-system current view: Open-card board with links, event history, status and cancellation eligibility, subject to input selection limits.
- Current-control decision scope: Cancellation of eligible whole-board commitments in apply mode. Recommendations to the owner do not have the same authority.
- Evidence: [hive-py/hive/steward.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/steward.py#L66-L89), [hive-py/hive/steward.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/steward.py#L209-L263), [hive-py/scripts/hive_steward.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/scripts/hive_steward.py#L103-L146), [hive-py/hive/dispatcher.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/dispatcher.py#L1578-L1618)
- Basis: Structural, from pinned first-party source and deployment documentation.
- Confidence: high
- Caveats: Current protected work and recent owner cards cannot be cancelled by the steward.

## S3* — Complementary audit

- State: A
- Function: Check the outcome reported by a card worker through a separate reviewer who can inspect primary artifacts.
- Disturbance / variety regulated: A report or acceptance command can fail to demonstrate that the requested outcome actually holds.
- Decisive decision or feedback right: Decide a source-based PASS/FAIL finding and identify defects for the closure or rework path.
- Decision owner: The separately launched reviewer model owns the finding. The dispatcher and, on head rounds where applicable, a judge act on it.
- Supporting / enforcement mechanisms: Reviewer prompt, read-oriented verification path, separately logged reviewer run and persisted verdict.
- Closure path: Reviewer findings enter the card check/judge path or directly govern closure on an eligible external-executor review. A failed review can keep the task in the work loop.
- Boundary reachability: A card's configured review path schedules a distinct reviewer and reads its verdict without asking the worker to self-assess.
- Why this is / is not agent-owned: The reviewer is the evidence adjudicator. The judge alone reads a prepared packet and would not supply independent primary access.
- Claim being audited: The stated outcome of the card and the worker's claim to have achieved it.
- Ordinary reporting path: The worker's report and regular acceptance check.
- Complementary access path: The reviewer independently reads files and runs read-only checks against the card goal.
- Independence boundary: Separate run and verdict with separately selected vendor when available. The reviewer may see the worker report but is instructed to verify its claims against the underlying result.
- Who acts on findings: The dispatcher consumes the review and the model judge can order revision on a head round.
- Evidence: [hive-py/hive/heads.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/heads.py#L384-L412), [hive-py/hive/dispatcher.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/dispatcher.py#L567-L579), [hive-py/hive/dispatcher.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/dispatcher.py#L867-L877), [hive-py/hive/dispatcher.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/dispatcher.py#L1761-L1770), [hive-py/hive/judge.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/judge.py#L15-L28)
- Basis: Structural, from pinned first-party source and deployment documentation.
- Confidence: high
- Caveats: This is an optional card path. The reviewer is distinct even where same-vendor fallback is enabled.

## S4 — Outside-and-then intelligence

- State: —
- Function: No distinct prospective capability-adoption path was established.
- Disturbance / variety regulated: Changes in evidence about the owner, archived input and available model routes.
- Decisive decision or feedback right: No evidenced decision about adopting a new way for the organization to operate.
- Decision owner: None at the declared recursion.
- Supporting / enforcement mechanisms: Night garden, archive work, fact reconciliation, owner-directed route selection and maintenance runbooks.
- Closure path: Stored facts can be revised and retrieved by subsequent turns. The steward adjusts current card commitments.
- Why this is / is not agent-owned: Revision of personal facts and routine route changes alter input or execution for current work. The source does not tie external prospective analysis to actual adoption of a different operating capability.
- Evidence: [docs/runbooks/night-gardener.md](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/docs/runbooks/night-gardener.md#L10-L34), [crates/engine/src/night/stages.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/night/stages.rs#L835-L870), [crates/engine/src/tools/garden.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/tools/garden.rs#L24-L38), [crates/engine/src/tools/model.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/tools/model.rs#L22-L34)
- Basis: Structural, from pinned first-party source and deployment documentation.
- Confidence: high
- Caveats: This finding is bounded to the pinned modes and supplied policy paths.

### Absence scope

- Surfaces inspected: Night garden deployment and reconciliation, archive reuse, route tools and the steward's recommendations.
- Plausible first-party paths checked: Adopting a different capability or rule as a consequence of environmental changes or projected requirements.
- Why no material first-party path remains: Fact maintenance updates what the assistant knows. Route changes are owner-selected and the steward's identified decisions concern existing tasks.

## S5 — Policy and identity

- State: —
- Function: No distinct ultimate policy or identity settlement path was established.
- Disturbance / variety regulated: The owner may redirect a disputed card or change the default model within the existing assistant identity.
- Decisive decision or feedback right: No evidenced determination of the deployment's ultimate purpose or authority settlement.
- Decision owner: None at the declared recursion.
- Supporting / enforcement mechanisms: Configured owner, engine request policies, card author disputes, and owner-only model selection.
- Closure path: Returned card clarification changes work on a card. An owner model selection changes model routing.
- Why this is / is not agent-owned: The available choices govern task particulars and provider selection within a fixed purpose and decision hierarchy.
- Evidence: [hive-py/hive/dispatcher.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/dispatcher.py#L889-L928), [hive-py/hive/heads.py](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/hive-py/hive/heads.py#L343-L365), [crates/engine/src/tools/model.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/tools/model.rs#L22-L34), [crates/engine/src/main.rs](https://github.com/pasekahq/ulei/blob/6f0132775c0bd13264c0abfb74ff367aa5e46160/crates/engine/src/main.rs#L653-L686)
- Basis: Structural, from pinned first-party source and deployment documentation.
- Confidence: high
- Caveats: Private operator prompts and governance cannot supply missing first-party closure.

### Absence scope

- Surfaces inspected: Owner-gated model changes, configured workflow constraints, card dispute/steer return and deployment runbooks.
- Plausible first-party paths checked: Escalating an identity/policy conflict to an authorized owner and feeding a binding settlement back into later operation.
- Why no material first-party path remains: The inspected owner loops change individual work or route choices. No separate identity or ultimate-policy decision and return was supplied.

## Recursion

The owner deployment is the unit of analysis. Individual chat turns and card work are operational cells. Provider products, deployment infrastructure and maintainers have their own decision boundaries.

## Variety and escalation

Resource gates constrain overlapping head, script and acceptance work. A dispute over the task itself can return to the card's author. The steward is limited to eligible current commitments and cannot cancel protected cards.

## Evidence gaps

Pinned-source review only. No provider requests, private deployment artifacts or execution traces were used. The README labels this snapshot pre-alpha.
