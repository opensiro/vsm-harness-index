---
harness_id: turri
project_name: turri
repository: https://github.com/turri-oss/turri
review_ref: 47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# turri

## Review boundary

- System in focus: the installed turri coding harness, with its conversation, `***plain` specification, regeneration work loop, role-constrained model agents and project-local module stores.
- Purpose and identity: preserve reviewable software intent and acceptance conditions while repeatedly producing and checking replaceable executable code from it.
- Relevant environment: developer requirements, local project and toolchains, model providers, changing specification and code, failing tests and conflicting work on modules.
- Standard-distribution boundary: documented npm/clone CLI, pi-based conversation plus turri extension, configured provider models, TypeScript work loop and module-level implementation, review and conformance agents. Provider inference and the underlying pi host are dependencies, not turri-owned governance.
- Credited operating / distribution surfaces: [documented installed operation](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/README.md), [regeneration and feedback protocol](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/docs/regenerating.md), [work loop](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/loop.ts), [module collision lanes](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/lanes.ts), [reviewer](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/unit-review.ts).
- Adjacent first-party surfaces excluded from ownership: repository contribution/release CI, test fixtures and developer-only validation, genome skill authoring, static example stacks, and independent vendor/pi organizations. Included genome skills count only when invoked in the installed runtime, not as a separate persistent management organization.
- First-party operating / deployment modes considered: interactive conversation and headless `turri regenerate`, concurrent module pulses, configuration/steering/halt, implementation reviewer and judge model, optional conformance track and test advisor, self-hosted provider selection.
- Recursion level: one turri-controlled project and its codebase/modules; each implementation/reviewer/conformance agent is a bounded work cell, not automatically a fully viable suborganization.
- Reviewed revision: `47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

turri extends the pi coding-agent host with a conversation that authors `***plain` functional specifications. It pins configuration and model roles (harness/coding/judge/advisor), derives module and change plans, starts isolated work pulses, supplies constrained command/file tools, records per-module code/test histories, checks unit tests, arranges separate code/test reviewers, optionally produces independently written conformance tests, and records outcomes. The TypeScript registry and work loop maintain module dependencies, wait conditions, statuses and ledger entries. The operator can inspect the panel, change project configuration, halt/steer modules and request subsequent regeneration. Code cannot freely rewrite its own specification or black-box tests. [README](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/README.md); [regeneration contract](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/docs/regenerating.md); [command fence](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/command-check.ts); [project mutation audit](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/audit.ts).

## Operational model

A human and harness-model conversation refine the durable specification. A planning model groups changes; coding agents decide implementation steps and tool calls. A separate review agent compares code/diff, tests and claims with the specification, and returns findings to the coding agent; an arbiter model decides which disputed review findings remain actionable. Turri-owned deterministic steps check each job's test result, roll back failed changes and serialize module collision lanes. These guards implement selected constraints but do not become discretionary autonomous owners merely by enforcing them. Provider calls are necessary but are only reached through shipped turri role wiring. [Implementation lifecycle](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/docs/regenerating.md); [arbiter source](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/arbiter.ts).

## S1 — Operations

- State: A
- Function: model-directed coding and specification/conformance-test production deliver functional code from changing project requirements.
- Disturbance / variety regulated: partial or contradictory descriptions, code faults, test failures, tool results and new behavior requested by the operator.
- Decisive decision or feedback right: writing/updating `***plain`, planning a feasible implementation change and choosing edits, tests and repairs within a pulse.
- Decision owner: the configured harness/planner and coding/conformance model agents in the supported turri roles; a human still owns the initiating requested purpose and may edit the source specification.
- Supporting / enforcement mechanisms: pi tool adapter, `createWorkLoop`, module ledgers, role-specific confined tools, test scripts, histories and retry caps.
- Closure path: revised specification → planned pulse → coding-agent edits/tests → review findings and any repairs → passing scripted checks and committed module record → generated code made available to subsequent pulses/release.
- Boundary reachability: `turri regenerate` and installed conversation enter the same first-party regeneration work loop; model-backed role executors are created for that loop, not merely present in developer examples.
- Why this is / is not agent-owned: the model chooses meaningful implementation and repair actions while turri enforces paths/test gates; static sequence rules are not themselves the agent's decisions.
- Evidence: [README operational flow](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/README.md), [work-loop source](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/loop.ts), [review/repair flow](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/unit-review.ts).
- Basis: explicit supported design corroborated by first-party runtime wiring.
- Confidence: high for shipped role construction; no paid-provider execution in this review.
- Caveats: external pi/model providers supply inference; a no-model configured installation cannot perform this S1.

## S2 — Coordination

- State: C
- Function: a first-party dependency/collision lane prevents simultaneous work cells from overwriting the same module or a required upstream module.
- Disturbance / variety regulated: concurrent code/test pulses writing overlapping module directories or shared `requires` ancestors can race and corrupt one another's results.
- Decisive decision or feedback right: map each queued pulse to its entire writable module dependency chain, withhold a conflicting pulse and retry after the occupying pulse settles.
- Decision owner: a first-party deterministic registry and lane relation implements the conflict-specific path; no model is shown to choose or revise this cross-unit settlement autonomously. Developer-constructed policies define lane granularity.
- Supporting / enforcement mechanisms: `moduleLanes`, job registry queue/waiting states, module dependency tracking and run ledger.
- Closure path: observed overlapping lane claims → one pulse waits instead of writing → completion/release of the lane → waiting pulse may start against the updated module state.
- Boundary reachability: both CLI and conversation work paths request the same first-party job lanes on the supported project files, not only a test fixture.
- Why this is / is not agent-owned: the S2-specific collision feedback path is shipped, but the authority and choice of this conservative coordination relation live in constructor code rather than an autonomous coordinating agent; hence `C`, not `A`.
- Distinct S1 units: separately running model-backed code or conformance pulses on two modules that share a dependency or output directory.
- Inter-S1 disturbance: both writing the same module chain would race and lose one worker's changes.
- Attenuating coordination relation: overlapping module-directory lanes become mutually exclusive, with required ancestor chains included.
- Feedback into subsequent S1 behaviour: the later pulse waits and is re-planned/started after the earlier work completes and the code record is refreshed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: `moduleLanes` explicitly identifies a concrete competing-write interference and ties waiting to shared writable paths, beyond simply assigning tasks in sequence.
- Evidence: [lane collision intent and function](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/lanes.ts), [work-loop wait and dependency checks](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/loop.ts), [job registry](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/jobs.ts).
- Basis: structural code path and explicit collision rationale.
- Confidence: medium-high for the conservative S2 constructor; it is not model-governed coordination.
- Caveats: no negotiated or autonomous dynamic arbitration of cross-module conflicts is claimed.

## S3 — Inside-and-now control

- State: P
- Function: the live project operator can survey current multi-module work, choose priorities/constraints, change model/concurrency configuration and halt or steer ongoing work as a whole.
- Disturbance / variety regulated: competing active pulse commitments, accumulated work, cost, stalled modules and currently unwanted regeneration.
- Decisive decision or feedback right: inspect the project queue/pulse status, halt an affected module, steer its pending work or alter capacity/models at the next allowed transition.
- Decision owner: the legitimate human owner of the local turri project, not the panel renderer, deterministic loop or individual coding agents.
- Supporting / enforcement mechanisms: current pulse/job panel, state registry, `halt`, `steer`, and `/turri-config` commands with documented effective-time behavior.
- Closure path: operator reads current module/pulse state → changes or halts a current commitment → work loop stops/rolls back a pulse, holds dependent modules, or uses the updated config on subsequent eligible pulses.
- Boundary reachability: these commands and project-current panels are shipped in the installed conversation and CLI mode; the work loop records held/waiting modules and processes configuration changes during operation.
- Why this is / is not agent-owned: the user decides intervention and priority; deterministic suspension/enforcement carries out the choice. Autonomous agent planning within one coding job is not promoted to whole-project S3.
- Whole-system current view: module-level planned/running/halted/waiting state and pulse costs/stages in the interactive panel.
- Current-control decision scope: which project modules proceed now, which halt, what current compute/model/concurrency envelope applies and which pending work is steered.
- Evidence: [panel, halt and config supported modes](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/README.md), [work-loop hold/wait implementation](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/loop.ts), [live config commands](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/config-command.ts).
- Basis: explicit operator workflow plus implemented return path.
- Confidence: medium-high for bounded single-project human S3.
- Caveats: some settings change only on the next pulse; this is local parent current control, not upstream maintainers' org-wide governance.

## S3* — Complementary audit

- State: A
- Function: a separately instantiated read-only reviewer independently inspects code and unit tests against the frozen specification and source diff, challenging an implementation agent's self-report.
- Disturbance / variety regulated: plausible successful code-agent narratives and green but weak tests can conceal defects or missing requirements.
- Decisive decision or feedback right: reviewer names actual code/test discrepancies from direct file access; an optional judge model independently upholds or dismisses contested findings; coder must address upheld blocking findings before successful landing.
- Decision owner: read-only reviewer/judge model roles supplied by the installed harness, separate from the model agent that produced code; the test runner is a deterministic gate rather than owner of their findings.
- Supporting / enforcement mechanisms: exact worktree diff, specification snapshot, testing script, `can_it_fail` probes, two-stage review/arbiter and returned review notes.
- Closure path: agent edits and declares work → first-party diff/raw files and test script are provided to reviewer → independent problems are returned to coder → revised code and rerun tests/review → evidence-backed landing or rollback.
- Boundary reachability: the shipped implementation path invokes `createUnitReviewer` and `arbitrateReview` as role-confined executors during regeneration, with different write permissions from coding agents.
- Why this is / is not agent-owned: critical judgment is made by independent role models inspecting code, not by a boolean status check or the coding agent's own completion statement; this is a complementary path even though run as a standard quality gate.
- Claim being audited: implementation and tests actually satisfy the declared functional spec, beyond the coding agent's report and green test exit code.
- Ordinary reporting path: coding agent's account, tool transcript and unit-test pass/fail result.
- Complementary access path: frozen changed-file diff, direct files, test script and adversarial ability to run targeted test-failure probes.
- Independence boundary: reviewer cannot write the code under review and receives an independent review task; the arbiter model rules on disputed review findings instead of letting the coder silently waive them.
- Who acts on findings: the coding agent repairs issues upheld by reviewer/arbiter; deterministic harness reruns checks and records the result.
- Evidence: [reviewer function and read-only task](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/unit-review.ts), [arbiter role and ruling](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/arbiter.ts), [conformance check roles](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/conformance-agents.ts).
- Basis: explicit review contract and structural read-only, diff-based model access.
- Confidence: medium-high; code path inspected without invoking paid models.
- Caveats: independence is role/tool/context separation, not a wholly different vendor or external human audit; findings are bounded by the specification and reviewer quality.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped distinct outside-and-then loop converting future environmental distinctions into durable organizational capability adaptation was established at the reviewed project boundary.
- Disturbance / variety regulated: changing external models, frameworks, dependencies and stakeholder needs could motivate later tool/strategy changes.
- Decisive decision or feedback right: no first-party future-environment interpretation/option selection is shown beyond developer/operator configuration and current-spec regeneration.
- Decision owner: not established for an S4 path; model selection, new requirements and project maintenance remain operator/developer choices.
- Supporting / enforcement mechanisms: test advisor, model configuration, skills, `***plain` revision, replayable regeneration and provider adapters.
- Closure path: present requirements or current test failure may trigger another build, but no independently selected prospective environmental option returns to change the standing harness capability.
- Why this is / is not agent-owned: scenario exploration and internal re-planning regulate the requested product; they do not evidence continuous external/future sensing coupled to present management.
- Evidence: [test advisor's current-spec questions](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/test-advisor.ts), [regeneration scope](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/docs/regenerating.md), [config model selection](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/README.md).
- Basis: bounded negative first-party source review.
- Confidence: medium for the supported standard modes.
- Caveats: future plugins or human upgrades are possible but not credited without a shipped closure path.

### Absence scope

- Surfaces inspected: regeneration and advisor roles, model configuration, operator steering, linked skills, release/support and CLI modes.
- Plausible first-party paths checked: test-advisor scenario generation, self-check/diagnose/repair loops, provider switching and code/spec regeneration.
- Why no material first-party path remains: all inspected paths work on present local project specifications or repair current failures; none shows external prospective intelligence selecting and returning a change to enduring project capability.

## S5 — Policy and identity

- State: —
- Function: no shipped organizational identity/ultimate-policy deliberation, legitimate authority and return-to-operation loop was established inside one turri-controlled project.
- Disturbance / variety regulated: conflicting long-term purpose, allowed organizational missions and ultimate authority could arise outside the provided task workflow.
- Decisive decision or feedback right: operator creates/edits the project's purpose and configuration; the product enforces static safety walls but does not adjudicate identity-level matters through a returning governing loop.
- Decision owner: not established for a first-party S5 path; the human project owner remains ultimate authority outside this specific function claim.
- Supporting / enforcement mechanisms: command fence, OS sandbox, file audit, model role definitions, configuration and user permissions.
- Closure path: ordinary task authorization and command refusal affect execution, not a standing process for identity/policy disagreement → legitimate authority → binding new policy → changed subsequent operation.
- Why this is / is not agent-owned: a durable specification records *what software to build*, not who may redefine the harness organization or reconcile S3/S4 at identity level.
- Evidence: [safety and install overview](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/README.md), [command-check scope](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/command-check.ts), [project mutation audit](https://github.com/turri-oss/turri/blob/47b578cafcab669a0ed3c02b9d0f1d5e17fcd8fa/src/regenerate/audit.ts).
- Basis: bounded negative first-party source review.
- Confidence: high for no identity-level closure in shipped modes.
- Caveats: contributor governance and external vendor policies are outside this declared runtime/project recursion.

### Absence scope

- Surfaces inspected: agent tool walls, config/role selection, operator workflow, source specification, package/release and repository governance materials.
- Plausible first-party paths checked: static command/credential policy, user changing config/models, project-spec editing, runtime approvals and code-review verdict escalation.
- Why no material first-party path remains: these are implementation, security enforcement or current project decisions; none carries a policy/identity issue to an authoritative decision and returns a binding changed organizational policy.

## Distributed OSS parent arrangement

Public contributors may revise turri itself through source PRs, but that maintainer organization is outside the installed one-project runtime boundary. Local operator S3 is bounded to the project work queue; no upstream organization-level S3/S4/S5 status is borrowed.

## Self-hosted and non-human modes

The installed CLI and conversational modes run with the user's configured model provider and local toolchain. The model-led coding/review work cells are autonomously active inside fixed constraints; operator `halt`, `steer` and config establish a distinct supervised current-control path, not an autonomous project-governor. No separate autonomous S5 mode is evidenced.

## Recursion

The project is the declared system; separate implementation, reviewer and conformance roles are operational cells. Module dependency graphs and nested model calls do not prove full viable recursion with separate identity and metasystem per module.

## Variety and escalation

Specification and model roles amplify local implementation variety; test scripts, strong read-only review, conformance and collision lanes attenuate failure/interference. The operator can steer or halt present work. Failing runs roll back/hold instead of being silently admitted. Human changes to requirements and provider credentials remain external bounds; statuses do not by themselves establish an algedonic S-function.

## Evidence gaps

- Pinned source/README/doc inspection only; no paid model, active provider account, or completed live turri regeneration was run. The review asserts executable wiring and documented supported operation, not observed provider quality.
- The S2 constructor is conservative deterministic lane serialization, not autonomous model negotiation; no stronger owner is inferred.
- S3* role independence is first-party read-only reviewer/judge separation; it is not proof of external institutional independence or flawless audit recall.
- No cross-project/global VSM organization claim is inferred from the one-project CLI and the OSS development repository.
