---
harness_id: zigent
project_name: Zigent
repository: https://github.com/chhuax/Zigent
review_ref: f6252e65dc28b202b71f54a9a5d70424cc7010b5
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Zigent

## Review boundary

- System in focus: the first-party public `chhuax/Zigent` repository at frozen revision `f6252e65dc28b202b71f54a9a5d70424cc7010b5`, exactly as pinned by candidate intake #878. The boundary includes the committed build graph, `src/` tree, utilities, public README/AGENTS/ROADMAP and shipped repository content at that revision; later commits and untracked/private design material are excluded.
- Purpose and identity: the repository describes a from-scratch Zig coding-agent kernel intended to provide a model/tool loop, tools, permissions, memory, compaction, recovery, transcript and local service.
- Relevant environment: future model providers, coding workspaces, shell/filesystem/process state, future clients and future kernel modules described by repository documentation.
- Standard-distribution boundary: only files actually committed at the frozen revision count. Public documentation explicitly says private `design/` material is not published; planned or later implementation cannot be imported into the frozen assessment.
- Credited operating / distribution surfaces: `README.md`; `AGENTS.md`; `build.zig`; `src/util/root.zig`; `src/util/io.zig`; `src/util/fsio.zig`; `src/util/proc.zig`; `src/util/log.zig`; `src/util/watch.zig`.
- Adjacent first-party surfaces excluded from ownership: later repository revisions; private/untracked `design/`; roadmap intent; stale README claims not backed by the frozen executable tree; future provider/client integrations; any spike/design behavior absent from the pinned tree.
- First-party operating / deployment modes considered: the actual frozen build/test graph and committed `src/` implementation. No executable coding-agent entrypoint, engine/model loop, tool registry, permission engine, memory runtime, transcript runtime or server/client runtime is present in the pinned tree.
- Recursion level: one Zigent repository/kernel candidate. Because first-party operational S1 admission fails at the frozen boundary, higher VSM functions are not published as autonomous harness ownership states.
- Reviewed revision: `f6252e65dc28b202b71f54a9a5d70424cc7010b5`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The frozen revision is materially earlier than the implementation described by its README. The immutable Git tree contains `src/util/` only. `build.zig` constructs one `util` module, tests only that module, and explicitly notes that `src/common/` has not yet been created. It defines no executable coding-agent target and no engine, LLM, tools, permissions, memory, server, client-protocol or CLI module.

`AGENTS.md` independently corroborates the frozen implementation state: it says design is complete, a spike skeleton exists, and the next steps are to install Zig, run/fix the spike, freeze contracts and then begin parallel kernel implementation. This conflicts with README status prose claiming a complete 12-module kernel and 537 tests. Under the repository's own instruction that contracts must be read from code rather than documentation, the executable frozen tree governs.

The committed `src/util/root.zig` is an OS-boundary utility module exposing I/O, filesystem, process, logging and watch helpers. These are substrate capabilities. They do not interpret a coding objective, invoke a model, select task-specific tools, observe results and decide what substantive action follows.

Counterfactual owner test: remove all future/later model, engine, tool, permission, memory and client components claimed by documentation but absent from the frozen tree. The committed remainder still performs utility operations/tests, but no goal-directed coding decision loop remains because none exists at this revision. First-party S1 therefore does not close.

Under Methodology `0.3.6`, an autonomous harness assessment is not retained by forcing higher-function classifications after S1 admission fails. The review therefore proposes canonical `excluded-no-agentic-vsm` disposition for this exact frozen revision. This is a frozen-ref finding, not a claim about later Zigent revisions.

Primary evidence:

- [`build.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/build.zig) — actual build graph: only the `util` module is created/tested; the comment explicitly says `src/common/` is not yet created.
- [`src/util/root.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/src/util/root.zig) — frozen source root exposes only OS-boundary utility helpers.
- [`AGENTS.md`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/AGENTS.md) — frozen project state says implementation work is the next phase after spike/contract preparation.
- [`README.md`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/README.md) — contains the conflicting later-looking implementation claims; treated as product intent/status prose rather than executable evidence where it disagrees with the pinned code tree.

## S1 — Operations

- State: —
- Function: no first-party autonomous coding operation is implemented at the frozen revision.
- Disturbance / variety regulated: committed utility code regulates low-level I/O, filesystem/process, logging and watch concerns, but not semantic coding-task uncertainty or selection among substantive repository actions.
- Decisive decision or feedback right: interpret a coding objective, select a substantive model/tool action, observe its result and decide what action follows.
- Decision owner: not established inside the frozen first-party repository boundary.
- Supporting / enforcement mechanisms: OS-boundary utility functions and tests.
- Closure path: no objective → model/decision → tool/action → observation → next-decision loop exists in committed first-party code at the frozen revision.
- Boundary reachability: `build.zig` constructs only `src/util/root.zig`; no shipped executable or agent-loop module is reachable from the frozen build graph.
- Why this is / is not agent-owned: deterministic utilities can execute caller-selected operations but do not choose open-ended coding actions. Removing future/later agent components leaves the same utility substrate and no autonomous task owner.
- Evidence: [`build.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/build.zig); [`src/util/root.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/src/util/root.zig); [`AGENTS.md`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/AGENTS.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: README claims a later-looking completed kernel, but those modules are absent from the exact frozen tree. This assessment intentionally does not repin to a later revision.

### Absence scope

- Surfaces inspected: immutable root/src trees; `build.zig`; `README.md`; `AGENTS.md`; committed `src/util` implementation and its tests.
- Plausible first-party paths checked: utility process execution as agent action; filesystem helpers as coding tools; watch loop as autonomous feedback; undocumented executable target; README-described engine/model/tool loop.
- Why no material first-party path remains: every committed executable code path is utility substrate selected by a caller; the modules required to close a semantic coding loop are absent from the frozen tree/build graph.

## S2 — Coordination

- State: —
- Function: no first-party S2 function is published because no population of qualifying autonomous S1 units exists at the frozen repository boundary.
- Disturbance / variety regulated: file/process/watch utilities may later support concurrency, but no inter-S1 conflict/oscillation is instantiated among autonomous operational units.
- Distinct S1 units: not established.
- Inter-S1 disturbance: not established.
- Attenuating coordination relation: not established.
- Feedback into subsequent S1 behaviour: not established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: no such S2-specific path is present; utility primitives are generic substrate only.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: generic filesystem/process/watch utilities only.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no multi-agent/subagent runtime is reachable from the frozen build graph.
- Why this is / is not agent-owned: without S1 units there is no coordination judgment to own.
- Evidence: [`build.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/build.zig); [`src/util/root.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/src/util/root.zig).
- Basis: structural negative search.
- Confidence: high.
- Caveats: later revisions may implement extensions or subagents; they are outside this frozen review.

### Absence scope

- Surfaces inspected: frozen source/build graph, process/watch/filesystem utilities, README/AGENTS claims.
- Plausible first-party paths checked: process helpers as separate S1s; watcher as coordination; future subagent extension claims.
- Why no material first-party path remains: no first-party autonomous operational units or disturbance-specific attenuation/feedback relation is committed at the pinned revision.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control function over a first-party operational organization is established.
- Disturbance / variety regulated: utility code can observe filesystem/process events, but there is no live population of autonomous commitments to regulate.
- Decisive decision or feedback right: not established for current resource/priority/commitment intervention.
- Decision owner: not established.
- Supporting / enforcement mechanisms: low-level process/watch/filesystem substrate.
- Closure path: not applicable for the negative finding.
- Whole-system current view: no first-party operational S1 population exists; utility state is not a whole-system organizational view.
- Current-control decision scope: no first-party actor allocates priorities/resources/commitments or intervenes across autonomous operations.
- Boundary reachability: no supervisor, task manager, scheduler or operational control loop is reachable from the frozen build graph.
- Why this is / is not agent-owned: there is no S3 decision function to assign to an agent or parent.
- Evidence: [`build.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/build.zig); [`AGENTS.md`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/AGENTS.md).
- Basis: structural negative search.
- Confidence: high.
- Caveats: architectural plans are not runtime closure.

### Absence scope

- Surfaces inspected: source/build tree, process/watch helpers, project-state documentation.
- Plausible first-party paths checked: watcher state as whole-system view; process control as S3; roadmap/planned task orchestration.
- Why no material first-party path remains: the frozen implementation has no operational organization whose current commitments can be observed and regulated.

## S3* — Complementary audit

- State: —
- Function: no complementary operational-audit loop exists because there is no first-party operating S1 organization at the frozen revision.
- Disturbance / variety regulated: build tests and architecture guard verify utility/build properties, not independent claims about live agent operations.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: module tests and architecture guard.
- Closure path: not applicable for the negative finding.
- Claim being audited: no live operational claim from a first-party S1 is assigned to a complementary auditor.
- Ordinary reporting path: no first-party agent-operation reporting path exists.
- Complementary access path: tests inspect committed utility/build behavior in development; they are not a runtime route to operational reality.
- Independence boundary: no runtime auditor distinct from an ordinary production path exists.
- Who acts on findings: developers act on build/test failures outside the assessed runtime.
- Boundary reachability: tests/guard are development checks, not a deployed audit actor reachable in an agent runtime.
- Why this is / is not agent-owned: deterministic development tests do not supply autonomous audit judgment or corrective return into live operations.
- Evidence: [`build.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/build.zig); [`src/util/root.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/src/util/root.zig).
- Basis: structural negative search.
- Confidence: high.
- Caveats: CI/test evidence can corroborate source behavior but does not become S3* runtime ownership.

### Absence scope

- Surfaces inspected: build tests, architecture guard, utility implementations, project documentation.
- Plausible first-party paths checked: unit tests as independent verifier; architecture guard as complementary audit; watcher/logging as runtime inspection.
- Why no material first-party path remains: inspected mechanisms are development validation or utility observation and do not close an independent audit judgment back into a first-party operational organization.

## S4 — Outside-and-then adaptation

- State: —
- Function: no prospective adaptation loop is implemented at the frozen revision.
- Disturbance / variety regulated: future documentation describes memory/compaction/recovery aspirations, but committed code does not sense external/future distinctions and generate durable capability adaptations.
- Decisive decision or feedback right: not established for adaptation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: generic utility substrate only.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no memory, learning, reflection, provider-selection or adaptation module is reachable from the frozen build graph.
- Why this is / is not agent-owned: there is no adaptation judgment to own; documentation intent cannot substitute for an executed path.
- Evidence: [`build.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/build.zig); [`AGENTS.md`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/AGENTS.md); [`README.md`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: later implementations may contain memory/compaction/recovery; this frozen revision does not.

### Absence scope

- Surfaces inspected: frozen build/source tree; README/AGENTS references to memory, compaction and recovery; utility state.
- Plausible first-party paths checked: persistence as adaptation; watcher feedback as environmental sensing; roadmap/design claims as future-option generation.
- Why no material first-party path remains: no committed first-party mechanism develops an adaptation from future/external distinctions and returns it into later operational capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy tension-and-resolution loop is implemented at the frozen revision.
- Disturbance / variety regulated: AGENTS/README contain project-development decisions and scope, but these are repository documentation for contributors rather than runtime policy authority inside an operational harness.
- Decisive decision or feedback right: not established for identity/ultimate policy at runtime.
- Decision owner: project maintainers authored documentation; no runtime S5 actor exists.
- Supporting / enforcement mechanisms: build dependency guard and static project documentation.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no operational runtime exists to receive an identity/ultimate-policy resolution.
- Why this is / is not agent-owned: static contributor rules and architecture constraints do not create an autonomous or parent-governed runtime identity loop without a live organization and return path.
- Evidence: [`AGENTS.md`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/AGENTS.md); [`build.zig`](https://github.com/chhuax/Zigent/blob/f6252e65dc28b202b71f54a9a5d70424cc7010b5/build.zig).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: repository governance exists at the development level; it is not runtime S5 for this absent harness operation.

### Absence scope

- Surfaces inspected: AGENTS/README project identity/scope decisions, build guard, frozen source tree.
- Plausible first-party paths checked: maintainer design decisions as parent S5; build guard as policy enforcement; roadmap as identity change.
- Why no material first-party path remains: no identity/ultimate-policy issue reaches a runtime authority and returns into subsequent first-party operational behavior because the operational harness is not implemented at the frozen revision.

## Assessment summary

At the exact frozen revision, Zigent does not satisfy first-party autonomous S1 admission. The repository's executable tree contains only the utility foundation while its own project-state document says kernel implementation is the next phase. The apparent complete-kernel status in README is not backed by the pinned code/build graph. Canonical disposition should therefore be `excluded-no-agentic-vsm` for this frozen ref, without repinning to later work.

**Vector:** `— · — · — · — · — · —`
