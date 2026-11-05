---
harness_id: gifford
project_name: Gifford
repository: https://github.com/smellak/gifford
review_ref: b618cff69f3f83a4513304c55ef34fd13bfd50f5
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Gifford

## Review boundary

- System in focus: one installed Gifford communication fabric, its participating interactive agent sessions, authenticated MCP messages, human channel control, PTY delivery proxy, optional Glimmer decision path and bounded inter-agent conversation loops.
- Purpose and identity: let independently running CLI agents communicate across harnesses and machines without trampling human input or permitting unbounded conversations.
- Relevant environment: live Codex, Claude Code, Muse Code and OpenCode sessions, other users/nodes, human keyboard activity, changing agent readiness, model uncertainty, stalled deliveries and adversarial/cyclic messages.
- Standard-distribution boundary: `gifford up`, `gifford run`, `gifford mcp`, panel/CLI controls, first-party orchestration, analyst, proxy, control engine and federation; configured outside agent runtimes and Glimmer model are dependencies, not owned autonomous departments.
- Credited operating / distribution surfaces: [README and operating modes](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/README.md), [architecture and implemented limits](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/DESIGN.md), [live results and limitations](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/RESULTS.md), [orchestrator decision implementation](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/orchestrator/decide.go), [loop admission](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/channel/loop_admission.go).
- Adjacent first-party surfaces excluded from ownership: offline model training/evaluation, contribution and release CI, benchmark fixture sessions, standalone vendor agents' own software-editing capabilities, and developer roadmaps that are not active production modes.
- First-party operating / deployment modes considered: locally managed agents, linked multi-node agents, manual delivery with one-shot human approval, configured model-backed automatic delivery, default finite loop limits, pause/off and link-level policies, signed message/ack and locally encrypted artifacts.
- Recursion level: the communication and current-control layer over a set of participating independently operating agent sessions, not each vendor harness as an independently Gifford-owned full organization.
- Reviewed revision: `b618cff69f3f83a4513304c55ef34fd13bfd50f5`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `gifford run` PTY proxy hosts a registered interactive agent session; its MCP child can send, read, acknowledge and reply to signed envelopes through a local hub or federated peer. The channel engine evaluates global-to-loop controls and bounded conversation state before acceptance and delivery. A daemon monitors the receiving session, optionally asks Glimmer to triage and choose `INJECT_PTY_PROMPT` versus `DEFER`, and the single-writer proxy performs final human-draft, session and delivery checks before injecting a brief notice. Operators can inspect queues, pause participants, require link approvals and approve one delivery without turning automation back on. [Architecture](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/DESIGN.md); [README](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/README.md).

## Operational model

Participating external agent sessions decide whether to initiate messages, read/acknowledge received messages and respond within their own tasks; those actions participate in this installed network but do not import the external harness's whole coding organization. Distinctively, the optional configured Glimmer decision model makes a consequential local delivery/defer choice after first-party policy restricts allowed actions. In unconfigured mode, no model is credited: each delivery requires human approval. The model cannot grant permission, write arbitrary terminal text, lift budgets or override a human draft; those are deterministic/human-held control rights. [Model decision](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/orchestrator/decide.go); [live model checks](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/RESULTS.md).

## S1 — Operations

- State: A
- Function: connected agent sessions initiate and conduct cross-agent message exchanges, while the configured Glimmer choice loop makes bounded, context-sensitive delivery decisions that enact Gifford's operational purpose.
- Disturbance / variety regulated: a recipient's changing interactive state, external message content, timing and whether a message is safe/useful to surface now.
- Decisive decision or feedback right: a participating agent chooses to send/read/reply; in the supported automatic mode Glimmer chooses `INJECT_PTY_PROMPT` or `DEFER` when *both* are allowed, which materially changes immediate delivery.
- Decision owner: actual participant model for authored conversation; configured Glimmer for the constrained delivery/defer choice. The proxy, hub and rule engine only enforce or transport.
- Supporting / enforcement mechanisms: MCP send/read/ack tools, signed agent identity, durable queue, triage/classification, chosen action, last-mile PTY writer and recipient acknowledgement.
- Closure path: autonomous sender uses MCP → stored/authorized message → automatic model decides delivery when eligible → proxy notices receiver → receiving agent reads/acknowledges and may answer → conversation continues within control limits.
- Boundary reachability: the documented `state_analysis` configuration wires the model and the pinned live bench measured actual model-backed deliveries/reads; manual mode remains separately supported and does not itself supply A.
- Why this is / is not agent-owned: Glimmer's action selection is a real permitted operational alternative, not merely readiness scoring. However the model does **not** own policy or terminal guard discretion, and no vendor model's unrelated coding powers are attributed to Gifford.
- Evidence: [MCP and run mode](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/README.md), [allowed actions and model choice](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/orchestrator/decide.go), [actual live model deliveries](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/RESULTS.md).
- Basis: pinned installed wiring plus separately bounded reported live acceptance.
- Confidence: high for the real choice and policy boundary; medium for generalizability across harness/agent states.
- Caveats: `gifford init` does not configure Glimmer automatically, the separate trained LoRA was not yet production-cut over, and observed model-mode negatives do not establish all silently-busy cases.

## S2 — Coordination

- State: C
- Function: a finite, versioned inter-agent loop budget interrupts repeated reply cycles that would otherwise amplify message traffic and tie up participating S1 agents.
- Disturbance / variety regulated: A→B→A conversation oscillation, repeated same-pair traffic and unbounded hops, retries, turns or messages.
- Decisive decision or feedback right: the owner defines bounded conversation rules; the channel engine counts activity, refuses or holds over-budget continuation, persists a paused loop and raises a request for an operator's explicit extension.
- Decision owner: first-party deterministic admission/continuation and human budget authority, not an autonomous S2 model with permission to revise the limits.
- Supporting / enforcement mechanisms: loop generation/state, per-loop turn/message/hop/same-pair caps, hard-limit outcomes, compare-and-swap pause and budget extension approvals.
- Closure path: participating agents exchange replies → counters approach a specific cap → continuation is held/denied and loop is paused → agents cannot extend the same cyclic conversation without a new authorized budget; if extended, the new bounded generation governs later replies.
- Boundary reachability: `internal/channel/loop_admission.go` actively pauses loops and creates budget-approval records in installed admission, and the engine is wired into MCP delivery; this is not a metrics-only concept.
- Why this is / is not agent-owned: the actual interference is a reciprocal agent-to-agent response loop. Hard limits attenuate its feedback amplification and force changed next agent behavior, but the choice of response policy belongs to configuration/humans, so `C`.
- Distinct S1 units: separate connected sending and receiving interactive agent sessions, potentially from different harnesses/nodes.
- Inter-S1 disturbance: replies can trigger still more replies indefinitely, starving current tasks and saturating channels.
- Attenuating coordination relation: bounded loop mode and directional messages with hop/message/turn and same-pair caps.
- Feedback into subsequent S1 behaviour: over-budget reply cannot proceed; a pending human approval and a later revised budget explicitly determine whether its successors may continue.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: ordinary signed routing is insufficient; the positive mapping is the concrete closed *anti-oscillation* control over a reciprocating pair of operational agents.
- Evidence: [loop budgets](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/channel/budgets.go), [loop admission and pause](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/channel/loop_admission.go), [operator budget extensions](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/channel/loops.go).
- Basis: first-party source paths and limit/approval tests; not a measured production oscillation incident.
- Confidence: medium-high for enforced anti-loop relation, bounded on provider-behavior generality.
- Caveats: budgets restrict conversation frequency and length; they do not independently reconcile semantic conflicts between agents or optimize task allocation.

## S3 — Inside-and-now control

- State: P
- Function: human operator monitors active agents, pending/uncertain message delivery and node/link state, and regulates current network commitments and safety envelopes.
- Disturbance / variety regulated: competing incoming messages, recipient availability, human typing, unsafe automatic notices, channel overload and stuck approvals.
- Decisive decision or feedback right: owner pauses/resumes a specific agent, switches a channel off, imposes link approval, approves one safe notice, observes incident and controls budget extension.
- Decision owner: human responsible for this installed fabric; model delivery preferences and deterministic guards are lower-level constrained operations, not ultimate portfolio control.
- Supporting / enforcement mechanisms: `gifford panel`, `gifford ctl`, six-scope versioned channel controls, pending approval list, event/status store and resumed queue.
- Closure path: current pending/incident view → human changes a control or grants one-shot approval → channel decision is recalculated → subsequent delivery obeys the revised restriction with all other safety guards still enforced.
- Whole-system current view: panel includes the delivery queue, agents and recorded incidents spanning the node, rather than the sender's single reply.
- Current-control decision scope: channel-wide, per-agent, directional link, thread and loop delivery authority, plus selected one-shot exceptions.
- Why this is / is not agent-owned: current commitments are governed by human choice; encoded guard policies do not make S3 autonomous.
- Evidence: [human controls](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/README.md), [implemented control scope](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/DESIGN.md), [live panel reconciliation](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/RESULTS.md).
- Basis: documented CLI/panel commands and reported live queue/incident validation.
- Confidence: high for explicit parent controls, with no evidence of independent autonomous portfolio planning.
- Caveats: an ordinary UI kill switch by itself would not close S3; this mapping depends on its broader live fabric view and enforceable changes across participants.

## S3* — Complementary audit

- State: C
- Function: raw PTY observation, deterministic idle/busy corroboration and independent human-keystroke guard challenge the model/native-session inference that a recipient is safe to interrupt.
- Disturbance / variety regulated: a plausible but wrong model `IDLE_AT_PROMPT` label or stale native event could cause injection over active work or a human draft.
- Decisive decision or feedback right: independently re-evaluate the live PTY and draft generation at prepare/commit; suppress delivery when contrary concrete evidence appears, even if the model recommends injection.
- Decision owner: first-party independent observational detector/PTY guard, with human operator receiving held incidents; the Glimmer classifier cannot override failed corroboration.
- Supporting / enforcement mechanisms: deterministic tmux/screen detector, human-draft instrumentation, current session/manifest evidence, versioned guard results, and two-phase proxy delivery.
- Closure path: model/classifier reports apparent idle state → detector directly inspects screen and guard directly checks keyboard/draft → contradiction blocks injection or aborts commit → channel waits for a fresh supported safe observation before retrying.
- Boundary reachability: raw-screen corroboration is wired into the actual automatic delivery path, and `docs/RESULTS.md` separately reports real harness and captured-window trials with independent busy-state vetoes.
- Why this is / is not agent-owned: the complementary check is deterministic and independent of the model's assertion, not another model-generated explanation. It earns `C`, not autonomous `A` or an independent institutional audit.
- Claim being audited: the operational agent is idle and safe for interruption now.
- Ordinary reporting path: Glimmer state classification and optional native life-cycle events used by the delivery decision.
- Complementary access path: first-party raw PTY capture and human input guard that inspect the actual receiving process/input outside the classifier's redacted inference.
- Independence boundary: model cannot alter detector/guard checks, and detected human keys veto output; detector shares the Gifford runtime and is therefore **not** an external auditor or comprehensive safety proof.
- Who acts on findings: deterministic executor defers/aborts; human can inspect pending incidents and decide when to resume within remaining controls.
- Evidence: [corroboration and live probes](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/RESULTS.md), [model/detector choice logic](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/orchestrator/decide.go), [producer and independent observed state](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/orchestrator/state_producer.go).
- Basis: implemented separate access and return-to-control path, supported by limited reported live evidence.
- Confidence: medium, because same-runtime and timing gaps bound independence and efficacy.
- Caveats: neither synthetic keyboard fuzzing nor visible-busy probes establish atomic check-to-Enter safety or silently-busy performance for all harnesses; a routine safety guard alone is not a free-standing S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed outside-and-prospective adaptation cycle with an operationally selected future option returning to live Gifford was established at the pinned cutover.
- Disturbance / variety regulated: new harness behavior, model drift, changing state distributions and future compatibility could motivate adaptation.
- Decisive decision or feedback right: no live system owner was shown turning prospective outside-environment distinctions into a selected and activated future capability under the assessed boundary.
- Decision owner: developer/operator chooses releases and may manually activate or roll back a model; offline evaluation is an adjacent product-development surface.
- Supporting / enforcement mechanisms: first-party capture/dataset/label/evaluation and six-criterion adapter gate, LoRA training and staging reported in docs, `gifford ctl model activate` capability.
- Closure path: external harness screens inform offline training → improved LoRA was selected and staged → **production cutover pending** at the pinned revision; there is no evidenced completed feedback path into the live serving selection for that trained option.
- Why this is / is not agent-owned: offline model evaluation can be sophisticated, but neither automatic future-environment sensing nor an activated adaptation loop is shown in the configured Gifford runtime.
- Evidence: [trained vs production state](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/README.md), [deployment boundary](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/DESIGN.md), [bounded evaluation](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/RESULTS.md).
- Basis: pinned explicit production-cutover status and first-party training/eval/runbook sources.
- Confidence: medium-high for this release; future model activation could materially alter the mapping.
- Caveats: the model selection tooling is real and may provide a future S4 return if externally oriented options are actually incorporated and operated; it is not credited prospectively.

### Absence scope

- Surfaces inspected: README model cutover state, runtime analyst selection, offline capture/dataset/eval, adapter gate, activation/rollback controls and live results.
- Plausible first-party paths checked: labelled real-agent screen windows, prospective compatibility testing, LoRA comparison, staged inference endpoint and operator-controlled production activation.
- Why no material first-party path remains: the selected improvement had not closed its real-harness activation and return to current production operation; available model input classifies present readiness rather than planning a future external change.

## S5 — Policy and identity

- State: —
- Function: no identity-level question, legitimate adjudication and binding returned ultimate charter were established inside this installed communication fabric.
- Disturbance / variety regulated: conflicts over whether Gifford should exist as a human-first federation, how autonomy should be bounded, and whose constitutional authority prevails are potential identity questions.
- Decisive decision or feedback right: humans can change channel/agent/link/loop delivery policy and approve incidents; no documented identity-level agenda and deciding authority are wired into a recurring S5 closure.
- Decision owner: ultimate project and installation identity remain with the human owner outside the demonstrated runtime governance loop.
- Supporting / enforcement mechanisms: strictest-scope controls, fail-closed hard guard, explicit human approval, pause/off switches and user-configured model boundaries.
- Closure path: changed current channel rules govern subsequent messages, but that is current S3 governance; no first-party policy-identity deliberation returns a higher charter to rebalance present operations against future adaptation.
- Boundary reachability: controls are installed and binding, yet their scope concerns present delivery authority rather than a recognized ultimate-policy dispute.
- Why this is / is not agent-owned: a human is in the loop and has final veto, but retained parent authority and routine safety policy are not sufficient evidence of VSM S5(P).
- Evidence: [human and policy controls](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/README.md), [policy scope](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/docs/DESIGN.md), [channel controls](https://github.com/smellak/gifford/blob/b618cff69f3f83a4513304c55ef34fd13bfd50f5/internal/channel/loops.go).
- Basis: bounded negative source review of product operation and operator/owner controls.
- Confidence: medium-high at the declared recursion.
- Caveats: this does not deny legitimate human governance outside the first-party operating boundary.

### Absence scope

- Surfaces inspected: channel global/node/agent/link/thread/loop control, operator CLI/panel, approval records, model deployment switches and policy-protection code.
- Plausible first-party paths checked: parent veto, global `off`, human-only deployment, link authorization, owner-defined loop limits and direct edit of runtime controls.
- Why no material first-party path remains: these adjust what work may proceed now, but provide no evidenced issue→legitimate identity-level decision→binding system charter return loop.

## Distributed OSS parent arrangement

The GitHub maintainer organization, upstream releases and model training organization do not become this installed communications system's S5 merely by sharing a codebase. Users are active parent controllers for immediate communications; this supports S3(P), not an inferred S5(P).

## Self-hosted and non-human modes

Gifford is self-hosted and has an optional automatic model-backed delivery mode. With no configured model, approved manual delivery can work without Glimmer, but does not generate agent-owned delivery discretion. With a model, authorization is still human/constructor governed, and the model can only choose within the code-established permissible set.

## Recursion

Each connected agent can retain its own internal task loop, but Gifford does not define or govern all vendor-side models, tools and goals. The communication fabric constitutes the declared shared cross-agent recursion; two-node federation extends its reach, not its identity-level autonomy.

## Variety and escalation

MCP communication amplifies available cross-agent cooperation. Signed identity, link policy, human-draft veto, model-choice guard, finite conversation budgets and manual pause attenuate message/interaction hazards. Unresolved approval, exhausted budget and uncertain delivery stop or defer rather than silently overriding a person; an explicit human action can release the specific permitted path.

## Evidence gaps

- Actual four-harness bench delivery/read observations are reported, but some used an inbox bridge rather than direct native integration; the pinned docs distinguish these carefully.
- Model-backed live acceptance covers free and visibly busy cases; silently busy and complete keyboard-interference variants were not all verified, so S3* `C` is a limited complementary check rather than an assurance guarantee.
- Anti-loop behavior is implemented and tested in source, but this review did not run a live provider-to-provider unbounded oscillation experiment.
- The selected Glimmer LoRA was staging-served rather than activated in the reviewed production release; no prospective S4 credit is borrowed from future rollout.
- No local production installation or paid model inference was performed for this assessment; source and the project's stated measured results form the bounded evidence base.
