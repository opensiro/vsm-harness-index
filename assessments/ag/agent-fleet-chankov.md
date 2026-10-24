---
harness_id: agent-fleet-chankov
project_name: Agent Fleet
repository: https://github.com/chankov/agent-fleet
review_ref: d260099e67911d38f7cfbe90bd30b2639c2fd4b6
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Agent Fleet

## Review boundary

- System in focus: the shipped, Pi-centered Agent Fleet extension/harness and first-party installed personas, workflow engine, Verification Contract, peer communication, and operator controls at the exact frozen revision. One task-oriented local fleet is the assessed recursion.
- Purpose and identity: carry out coding/research/verification tasks through model-backed specialist executions while a thin model dispatcher governs current work and code-owned workflows enforce narrowly scoped operational controls.
- Relevant environment: human requestor, project Git repository and worktrees, tests and artifacts, configured external Pi provider/model registry, optional peer Pi/Claude/Hermes processes, remote workspaces and local operator.
- Standard-distribution boundary: package-distributed .pi/harnesses/agent-hub, included .pi/agents/personas, skills, .pi/agent-fleet/scripts flow commands, and their documented opt-in operating modes. Agent cognition uses Pi as a supported model executor, not as imported first-party implementation.
- Credited operating / distribution surfaces: shipped agent-hub native dispatcher; installed model-backed personas and scoped specialists; assertion/evidence ledger; documented executable just flow commands, quality runner and writer lease; code-reviewer persona; explicitly invoked af-compound/documenter loop.
- Adjacent first-party surfaces excluded from ownership: vendored upstream skills, archived .versions histories, CI/release tests, documentation-only future flows, external Pi agent internals, standalone Herdr server and remote Hermes service, model-provider judgments not elicited by a shipped Agent Fleet path.
- First-party operating / deployment modes considered: bare operator mode (empty roster); configured orchestrator with selected native team; conditional code-reviewer dispatch; explicit headless quality/build-test/poll flows; separately explicitly invoked parent-approved compound-learning skill. These are not assumed simultaneously active.
- Recursion level: a single local Agent Fleet hub with several model-backed specialist S1 operations or opt-in workflow agent phases; outside provider work, company governance and remote servers are environmental.
- Reviewed revision: d260099e67911d38f7cfbe90bd30b2639c2fd4b6
- Observation date: 2026-10-17
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7
## Repository architecture

The package's documented launcher loads Fleet Core and agent-hub into Pi; the hub registers dispatch and research tools, maintains tasks/sessions, and starts specialists under first-party personas. A configurable roster, work mode and optional peer topology are independent axes, and a bare launch defaults to operator mode with no native team. Agent Fleet owns prompts, tool bindings, coordination, diagnostics, verification/evidence records and much of local persistence, not the underlying Pi model inference or remote coding-agent internals ([docs/ARCHITECTURE.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/docs/ARCHITECTURE.md); [.pi/harnesses/agent-hub/README.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/README.md); [package.json](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/package.json)).

The Verification Contract persists checkable assertions and evidence; its normal use remains **advisory**—an unproven assertion does not globally block all hub work. Native dispatcher scopes can report overlapping writes but are advisory too. By contrast an explicitly started headless flow has a real configured quality-command acceptance gate, file-write policy, phase checks and per-process writer lease for poll merge; it does **not** automatically run inside the hub. Code-reviewer is a separate shipped read-only persona with direct Git/diff access, available when explicitly selected by the dispatcher. af-compound is a distinct invoked human-governed lessons-to-rules loop ([.pi/harnesses/agent-hub/README.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/README.md); [.pi/harnesses/agent-hub/assertion-ledger.js](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/assertion-ledger.js); [.pi/agent-fleet/scripts/flow.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/agent-fleet/scripts/flow.ts); [.pi/agent-fleet/scripts/workflows/lib/gates.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/agent-fleet/scripts/workflows/lib/gates.ts); [agents/code-reviewer.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/agents/code-reviewer.md); [skills/compound-learning/SKILL.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/skills/compound-learning/SKILL.md)).

## Operational model

User requests enter the Pi-backed hub. In configured orchestrator mode the model sees task/evidence context, dispatches builder/research/reviewer specialist sessions, receives structured returns and chooses follow-up actions; the helper model owns local coding/review judgments. Explicit just flow commands instead own ordered agent/code phases, configured quality checks and trace/branch results. An optional human-authorized compound-learning pass can turn observed failures, user corrections or environmental feedback into durable future rules. No end-to-end live provider run is claimed here; source reachability is distinguished from guaranteed model compliance.

## S1 — Operations

- State: A
- Function: actual coding, testing, research and artifact delivery by selected model-backed specialists or the hub operator agent.
- Disturbance / variety regulated: task requirements, source errors, tool failures and repository test feedback.
- Decisive decision or feedback right: specialist model chooses read/edit/test/research steps and integrates feedback to complete assigned work.
- Decision owner: model-backed Pi specialist (or directly operating hub model), instantiated with first-party persona and tool scope.
- Supporting / enforcement mechanisms: first-party persona definitions, spawnPiAgent composition, dispatch returns, bounded subprocess/runs, repository tools.
- Closure path: hub dispatch → spawned coding/research persona → source/test interaction → structured result and artifact path → hub follow-up or user outcome.
- Boundary reachability: agent-hub is wired into just fleet and selected team personas are installed; real model/registry and Git workspace are external prerequisites.
- Why this is / is not agent-owned: removing the model executor leaves a typed dispatcher and state, not substantive problem solving.
- Evidence: [.pi/harnesses/agent-hub/README.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/README.md); [docs/ARCHITECTURE.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/docs/ARCHITECTURE.md); [.pi/harnesses/agent-hub/dispatch-native-complete.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/dispatch-native-complete.ts); [agents/builder.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/agents/builder.md); [package.json](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/package.json)
- Basis: explicit first-party orchestrated mode and code paths
- Confidence: medium-high for supported source mode; no live provider result
- Caveats: bare operator with empty roster does not instantiate multiple native specialists; configured specialist mode is required.

## S2 — Coordination

- State: C
- Function: narrow interference attenuation when multiple independently started agent-driven flow integrations would write the same repository.
- Disturbance / variety regulated: simultaneous conflicting modifications of the same worktree and failure to preserve one writer at a time.
- Decisive decision or feedback right: allow or refuse acquisition of one live writer lease for the effectful poll merge, returning holder identity to the competing flow.
- Decision owner: deterministic first-party writer-lease constructor; the independent model voices/integrator own their own work, not the lease logic.
- Supporting / enforcement mechanisms: atomic exclusive lock creation, PID liveness/reaping and finally-release; poll apply gating.
- Closure path: two effectful polling/merge flows target one cwd → first lease holder proceeds → live contender receives WriterLeaseHeldError → later flow can retry after the prior release.
- Boundary reachability: withWriterLease is invoked by the shipped effectful poll merge and is a concrete narrow first-party coordination path, not hypothetical general mailbox semantics.
- Why this is / is not agent-owned: the S2-specific conflict resolution is deterministic; no model autonomously assigns global worktree exclusion across the whole hub.
- Evidence: [.pi/agent-fleet/scripts/workflows/lib/writer-lease.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/agent-fleet/scripts/workflows/lib/writer-lease.ts); [.pi/agent-fleet/scripts/workflows/lib/merge.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/agent-fleet/scripts/workflows/lib/merge.ts); [.pi/agent-fleet/scripts/workflows/wf-poll.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/agent-fleet/scripts/workflows/wf-poll.ts); [docs/workflows.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/docs/workflows.md)
- Basis: implementation + documented opt-in flow mode
- Confidence: medium; scoped to effectful flow merges
- Caveats: hub's concurrent writable specialist scope violations are only advisory; the lease is not a universal lock.
- Distinct S1 units: separate model-backed poll integrator runs/independently initiated effectful flow cells in a shared repository.
- Inter-S1 disturbance: two competing model-led integration attempts can overwrite or interleave changes in one worktree.
- Attenuating coordination relation: atomic exclusive writer lease based on repository path with PID-aware contention refusal.
- Feedback into subsequent S1 behaviour: the refused run does not apply its write, while a holder completes/releases before another may proceed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: exclusion explicitly regulates actual conflicting effectful sibling S1 write rights, not just their messages or scheduled order.

## S3 — Inside-and-now control

- State: A
- Function: current control of the configured multi-specialist task as one local fleet, including priority, delegation, verification follow-ups and resource allocation.
- Disturbance / variety regulated: unbounded specialist spawning, incomplete assertions, failed outputs, context pressure and mismatched task progress.
- Decisive decision or feedback right: hub model selects assignments, next intervention, corrective dispatch, pause or request for human assistance from aggregated work status.
- Decision owner: Pi-backed hub model guided by first-party orchestration prompt/commands; hard tool budgets and watchdog only enforce constraints.
- Supporting / enforcement mechanisms: tier limits, roster, model routing, assertion ledger, dispatcher results, zoom/status dashboards, ask_user and budget guard.
- Closure path: request/task ledger and specialist result → hub current view and model judgment → dispatch/plan/retry/clarification → new specialist action and evidence/status.
- Boundary reachability: explicit configured orchestrator with roster gives the hub active dispatch tools, result/history/ledger and decisional prompt; not claimed for bare empty-roster default.
- Why this is / is not agent-owned: without model hub judgment a gate can refuse spawns but cannot choose the current fleet goal, re-plan work or reassign specialist attention.
- Evidence: [.pi/harnesses/agent-hub/README.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/README.md); [docs/ARCHITECTURE.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/docs/ARCHITECTURE.md); [.pi/harnesses/agent-hub/dispatch-native-complete.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/dispatch-native-complete.ts); [.pi/harnesses/agent-hub/assertion-ledger.js](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/assertion-ledger.js)
- Basis: explicit and structural model-control mode
- Confidence: medium-high for conditional standard mode
- Caveats: generic ask_user approval is not separately credited as a closed parent S3 mode; no claim of hard guarantees for model prompt compliance.
- Whole-system current view: current task/role roster, outstanding verification assertions, active child states, structured returns, time/dispatch budgets and human blockers.
- Current-control decision scope: choose which specialist executes which present commitment; retry, stop, re-scope, verify or escalate work based on returns.

## S3* — Complementary audit

- State: A
- Function: conditional separate code-review judgment on implemented work, feeding concrete findings back to the task-owning hub.
- Disturbance / variety regulated: implementation claims or assertions that look complete but diverge from changed source, tests, architecture or security constraints.
- Decisive decision or feedback right: read-only code-reviewer model independently inspects repository changes and issues findings/risks rather than copying builder status.
- Decision owner: distinct reviewer persona's model; hub dispatcher handles corrective assignment and receipt of findings.
- Supporting / enforcement mechanisms: code-reviewer read/bash/grep/find/ls tools; preflight/quality/perf/doc reviewer subroles; direct diff and project rules; structured artifacts, reviews path.
- Closure path: builder artifact/diff → separately dispatched reviewer with direct source/rules → quality findings → hub receives evidence and can issue builder correction/re-review.
- Boundary reachability: first-party installed code-reviewer is callable through native dispatch when roster contains it; a separate full review is conditional, not default on every task.
- Why this is / is not agent-owned: independent reviewer makes a separate model judgment, while the dispatcher and deterministic evidence/scope mechanisms do not themselves acquire audit autonomy.
- Evidence: [agents/code-reviewer.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/agents/code-reviewer.md); [.pi/harnesses/agent-hub/README.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/README.md); [.pi/harnesses/agent-hub/dispatch-native-complete.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/dispatch-native-complete.ts); [docs/ARCHITECTURE.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/docs/ARCHITECTURE.md)
- Basis: shipped persona and dispatched operating mode
- Confidence: medium: independent access is structural, not an observed review outcome
- Caveats: this is not a universal mandatory merge gate; review not invoked in bare default mode and no institutional outsider independence is claimed.
- Claim being audited: producer's completed implementation and evidence meet requirements, project rules and quality/security expectations.
- Ordinary reporting path: builder status, structured success output and self-reported assertions.
- Complementary access path: reviewer reads actual Git change set, files, project rules, tests and optional independent subreviewer findings.
- Independence boundary: separate read-only code-reviewer specialist and independent review role versus producing builder; both remain within the same configured hub.
- Who acts on findings: hub model delegates rework or asks the human; no hard automatic block of every task is asserted.

## S4 — Outside-and-then intelligence

- State: P
- Function: conditionally turn observed user/environment corrections or repeated task failures into durable rules affecting future agent behavior.
- Disturbance / variety regulated: future tasks differ from stale practices; repeated user correction, failed test assumptions and drift in project conventions.
- Decisive decision or feedback right: legitimate operator/human accepts or rejects a specific proposed lesson diff before rule/document changes that later sessions load.
- Decision owner: human parent in the explicitly invoked compound-learning mode, not the session's documenter model or deterministic diff writer.
- Supporting / enforcement mechanisms: first-party af-compound command, compound-learning skill, documenter persona, evidence collection, target rules/docs index and diff verification.
- Closure path: past user corrections/test failures → model finds candidate future rule → human approves relevant diff → write/dedupe checked → next task loads updated rules/docs and changes work choices.
- Boundary reachability: af-compound is a shipped command invoking the model documenter; compound-learning specifies approval or explicit standing authorization and a verified write to declared rules/docs targets. Requires an opted-in user and project rules surface.
- Why this is / is not agent-owned: the option is generated by a model, but the effectful long-term adaptation choice belongs to the human; without human authorization (or preauthorization) no learning diff is applied.
- Evidence: [.pi/harnesses/agent-hub/commands/compound.ts](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/commands/compound.ts); [skills/compound-learning/SKILL.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/skills/compound-learning/SKILL.md); [agents/documenter.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/agents/documenter.md); [.pi/harnesses/agent-hub/README.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/README.md)
- Basis: first-party skill and model/human operational contract
- Confidence: medium; prospective path source-documented, no executed multi-session learning trial
- Caveats: only the explicit compound-learning mode is credited, not generic memory, simple rechecking tests or all future changes; published P remains a source-based hypothesis for Index S1 adjudication.
- External distinction: feedback from human requestor/corrections and actual tests/repository conventions rather than mere current task status.
- Future / prospective distinction: curated durable prompts/rules guide later independent tasks and sessions, not only repairing the present broken test.
- Adaptation option generated: a precise new/modified repeatable operational rule with evidence, source and deduped target.
- Path back into current capability / S3: operator-approved rule is written to indexed rules/docs and read by future role/hub work, altering next operational decisions.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct ultimate identity/ethos policy settlement for the whole fleet is evidenced.
- Disturbance / variety regulated: basic mission and normative tensions between current work and future adjustment.
- Decisive decision or feedback right: distinct legitimate ultimate-policy judgment plus return into operating fleet would be required; no such first-party closed loop established.
- Decision owner: humans select policy and approve operations/compound diffs; these are task/quality/future-rule choices, not independently established whole-system S5.
- Supporting / enforcement mechanisms: work modes, persona config, skill policies, damage controls, approval prompts, role labels.
- Closure path: configuration changes constraints and local work, but no distinct whole-fleet identity conflict → ultimate authority → policy settlement → binding return was identified.
- Boundary reachability: inspected shipped team-policy, approval, user and adaptation paths; the bounded absence is about first-party local fleet, not an operator organization's possible S5.
- Why this is / is not agent-owned: the presence of human yes/no and safety defaults does not itself identify an S5 owner or organizational policy closure.
- Evidence: [docs/ARCHITECTURE.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/docs/ARCHITECTURE.md); [.pi/harnesses/agent-hub/README.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/harnesses/agent-hub/README.md); [.pi/damage-control-rules.yaml](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/.pi/damage-control-rules.yaml); [skills/compound-learning/SKILL.md](https://github.com/chankov/agent-fleet/blob/d260099e67911d38f7cfbe90bd30b2639c2fd4b6/skills/compound-learning/SKILL.md)
- Basis: bounded negative scope, no assumption of universal impossibility
- Confidence: medium-high within defined first-party surface
- Caveats: users may operate legitimate S5 governance outside Agent Fleet; it is not part of this assessed shipped loop.

### Absence scope

- Surfaces inspected: native persona/team/work-mode and approval/guard prompts, shipped task and workflow policy, conditional compound-learning change path.
- Plausible first-party paths checked: top-level team identity selection, human tool approval, security guardrails, approved future rule changes, remote Herdr/Hermes authority.
- Why no material first-party path remains: these are configuration, present safety/current control or bounded adaptation; no separate first-party legitimate whole-fleet ultimate policy settlement with governing return was found in supported modes.

## Evidence gaps

- Positive states are **source-structural supported modes**, not an observed production/provider run. No autonomous quality or performance guarantee follows.
- Bare operator mode does not inherit optional native-roster review, flow writer-lease or compound-learning parent adaptation; the six-state vector aggregates independently configured first-party supported modes.
- S2=C is narrowly scoped to effectful poll merge/flow writer contention. Advisory hub scope warnings do not count as hard S2 enforcement.
- S3* independent code-reviewer is opt-in and shares parent hub, so organizational/external independent reviewer credentials are not claimed.
- S4=P depends on a human-approved proposal and next-session application; the available source proves the shipped instruction-level pathway but not an actually exercised environmental adaptation. If the present Skills threshold demands runtime-confirmed prospective change rather than supported mode wiring, this requires Index S1 semantic narrowing.
- S5 is bounded absence for this local fleet recursion, not a claim about the deploying organization.
- No upstream provider execution, Hermes/Herdr deployment or user approval trace was generated during this review.

## Conclusion

**Proposed, not canonical:** S1=A / S2=C / S3=A / S3*=A / S4=P / S5=— for supported (not necessarily simultaneous) Agent Fleet modes. S1 model-backed specialists perform work; first-party writer exclusivity mitigates one narrow inter-S1 conflict; the hub model steers current task commitments; a separate read-only model reviewer can audit actual artifacts; a human authorizes durable future-rule adaptation. S5 ultimate identity/policy remains absent at the assessed local fleet boundary. This draft requires source-backed Index S1 semantic adjudication and exact-head validation before any canonical decision.
