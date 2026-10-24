---
harness_id: coder
project_name: CodeR
repository: https://github.com/NL2Code/CodeR
review_ref: d63468344bc215bbabb8f0c1ba4af24897a946df
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# CodeR

## Review boundary

- System in focus: the published CodeR issue-resolution system evidenced by first-party role configurations and serialized SWE-bench execution traces at the frozen revision, **not** a locally inspectable implementation of its manager/runtime.
- Purpose and identity: resolve repository issues through specialized roles and a manager-selected predefined task graph, with an editor acting on the target codebase.
- Relevant environment: issue descriptions; SWE-bench repository snapshots; model-generated shell/edit/tool actions and returned terminal/file observations; test and role-result summaries.
- Standard-distribution boundary: published `config/roles/{manager,reproducer,fault_localizer,editor,verifier}.yml`, `trajs/*.traj`, readme and evaluation outputs. No first-party `.py` implementation, executable agent runner, implementation of `plan`/`submit`, or source of referenced shell commands is included in the frozen published tree.
- Credited operating / distribution surfaces: documented task graphs and role prompts, plus recorded executions where a manager chooses a plan, an editor inspects/edits files and the manager receives a result. Trace records are supporting observations, not proof that every stated path is enabled or general.
- Adjacent first-party surfaces excluded from ownership: research paper claims, SWE-bench evaluation scripts and scores, leaderboard, third-party provider/runtime internals and human academic project governance.
- First-party operating / deployment modes considered: recorded SWE-bench runs, declared manager/editor/reproducer/localizer/verifier role templates; other runtime modes cannot be verified from the published repository.
- Recursion level: one CodeR issue-solving episode with specified specialist cells and a manager, not the CodeR research group or tested repository organization.
- Reviewed revision: [`NL2Code/CodeR@d63468344bc215bbabb8f0c1ba4af24897a946df`](https://github.com/NL2Code/CodeR/tree/d63468344bc215bbabb8f0c1ba4af24897a946df), frozen in [intake #237](https://github.com/opensiro/vsm-harness-index/issues/237) and [batch #1884](https://github.com/opensiro/vsm-harness-index/issues/1884).
- Observation date: 2026-10-22; repository artifacts and saved trajectories only; no live provider/agent tests.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

CodeR's README describes a multi-agent issue-repair approach with predefined task graphs. The published configuration contains a manager prompt with alternative plans and specialist role prompts for reproduction, fault localization, editing and verification. The manager must choose among the supplied plans and can issue a `plan` or ordinary command; individual roles are instructed to issue one tool/shell/edit action, observe the result, and continue or return `succeed`/`fail`. Manager plan data includes explicit downstream role destinations and forwarded information on success/failure. At least one saved trajectory records a model-selected plan, code open/edit observations, local corrective edit, success and final submission, providing observation-level S1 evidence beyond a hypothetical prompt.

This revision is **not an executable source release**: it contains configuration, traces, result JSON and images, but no manager scheduler, command implementation, provider interface or actual code for maintaining responsibility boundaries. The documented graph, logs and role labels are therefore insufficient to establish who owns unobserved S2–S5 decision/feedback rights or prove their negative across runtime variants.

Evidence: [README](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/README.md), [manager plans](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/manager.yml), [editor model/tool loop](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/editor.yml), [saved Django trace](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/trajs/django__django-15790.traj).

## Operational model

The manager owns task-graph selection as declared by its prompt, and the specialist roles own issue-local proposed shell/search/edit choices. A serialized example documents that returned environment observations affect an editor's next action: the editor notices an accidental duplicate return and removes it before `succeed`. The plan runner's implementation and the provenance of its role activation are not provided. The issue-solving actions are observable; true cross-unit interference settlement, present-wide resource governance, audit independence, outside-future adaptation and ultimate-policy ownership are not sufficiently observable for a definitive positive or bounded negative classification.

## S1 — Operations

- State: A
- Function: operate on a supplied issue and target code through model-selected investigation, editing and corrective next actions.
- Disturbance / variety regulated: unknown fault location, changing source state, incorrect edits, tool observations and incomplete task outcomes.
- Decisive decision or feedback right: choose the issue plan and next shell/open/edit action, then revise a specific local code modification after seeing execution feedback.
- Decision owner: model-driven manager and/or specialist as recorded in saved trajectories and explicitly instructed by role templates; underlying command execution is external runtime support.
- Supporting / enforcement mechanisms: manager plan prompt, editor/reproducer/localizer/verifier templates, line-oriented editor and shell interface, task outcome markers and observations.
- Closure path: issue → manager-chosen plan → delegated role goal → model-selected code action → environment response → revised action/`succeed` → manager receipt and `submit`.
- Boundary reachability: frozen repository includes actual serialized run artifacts with `plan`, `open`, `edit`, subsequent corrective edit, `succeed` and `submit`, so the loop is observed beyond a promise in documentation.
- Why this is / is not agent-owned: actions and revision decisions appear as model responses in the recorded conversation; file operations themselves are supplied by an unshared execution interface.
- Evidence: [manager plan and submission protocol](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/manager.yml#L1-L87), [editor's one-command observation loop](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/editor.yml#L1-L91), [recorded multi-action repair trace](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/trajs/django__django-15790.traj).
- Basis: observed trace and configuration, not direct inspection of runtime implementation.
- Confidence: medium-high that an agent-owned operational editing loop ran in the recorded mode; lower confidence about unseen deployment modes and success claims.
- Caveats: the trace is a saved artifact whose generation cannot be independently replayed from published source. It supports existence of the loop, not benchmark quality, safety or every described role path.

## S2 — Coordination

- State: ?
- Function: attenuate disturbance among distinct specialist S1 cells while preserving their local decision-making.
- Disturbance / variety regulated: incompatible edits, inconsistent reproduction/verification outcomes and poorly aligned inter-role commitments.
- Decisive decision or feedback right: manager-directed routing after `succeed`/`fail` and role-summary handoffs are declared, but conflict-specific inter-S1 correction ownership is not established.
- Decision owner: manager-model plan selection is declared; who senses/settles a concrete inter-S1 collision in running code is unknown.
- Supporting / enforcement mechanisms: task-graph `downstream` destinations, role result summaries and manager handoff template.
- Closure path: producer outcome → configured next role or manager; the additional loop required to detect **specific inter-S1 interference**, choose an attenuating response and return it to affected roles is not evidenced.
- Why this is / is not agent-owned: a chosen task graph and serial task handoff are not automatically conflict-regulating coordination, but without actual orchestration source a bounded absence claim is premature.
- Evidence: [manager's predefined success/failure graphs](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/manager.yml#L1-L140), [role transfer template](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/verifier.yml#L80-L94), [serialized example](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/trajs/django__django-15790.traj).
- Basis: partial structural declarations and output trace.
- Confidence: high that task routing alone is insufficient; unresolved whether unpublished runtime supports genuine S2.
- Caveats: no reproducible first-party scheduler or evidence of actual incompatible sibling commitments and model-directed damping.

## S3 — Inside-and-now control

- State: ?
- Function: govern the whole current issue-solving organization's resources, priorities, accountability and commitments.
- Disturbance / variety regulated: plan failure, role handoffs, competing tasks and limited execution resources.
- Decisive decision or feedback right: manager plans and `PlanFailed` returns are specified, but whether they represent whole-current discretionary resource/commitment control rather than issue-level task planning cannot be established.
- Decision owner: declared manager model for plan selection; actual current-wide authority and information path unknown.
- Supporting / enforcement mechanisms: alternate predefined plans and manager-directed retry/submit instructions.
- Closure path: issue → model chooses a plan → role outcomes return; no verified current-wide resource/prioritization negotiation or binding corrective intervention path.
- Why this is / is not agent-owned: a prompt naming a manager and choosing a workflow does not prove S3 ownership, while hidden implementation prevents a confident negative for all modes.
- Evidence: [manager role and task graph contract](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/manager.yml), [recorded manager plan](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/trajs/django__django-15790.traj).
- Basis: bounded publication evidence.
- Confidence: low for final state because manager implementation is unpublished.
- Caveats: default S3 cannot be inferred from the role name.

## S3* — Complementary audit

- State: ?
- Function: independently test S3's operating claims through a complementary evidence route and return findings for management correction.
- Disturbance / variety regulated: inaccurate manager/producer success claims and hidden operating errors.
- Decisive decision or feedback right: verifier prompt asks a tester to check reproducer/test correctness; S3 management claims, independence and corrective return are not shown.
- Decision owner: role tester for local QA; managerial audit owner undetermined.
- Supporting / enforcement mechanisms: terminal test commands, `succeed`/`fail`, and downstream role results.
- Closure path: code/test → verifier report → another task phase; an independent audit of present S3 decisions and returned management correction remains unverified.
- Why this is / is not agent-owned: an autonomous tester is not automatically a complementary S3* auditor; missing runtime blocks a confident global absence claim.
- Evidence: [verifier role template](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/verifier.yml#L1-L89), [manager's role graph](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/manager.yml#L1-L140).
- Basis: source documents without implementation.
- Confidence: high that shipped prompts do not themselves establish S3*; low about unpublished modes.
- Caveats: task-level test validation must not be upgraded to management audit.

## S4 — Outside-and-then intelligence

- State: ?
- Function: sense external/future disturbances and return strategic capability adaptations to present operation.
- Disturbance / variety regulated: changing repositories, future bug patterns and external technology/method changes.
- Decisive decision or feedback right: no prospective adaptation decision evidenced in the published role prompts and traces; hidden runtime boundary prevents a complete negative survey.
- Decision owner: research maintainers select public releases; future-facing autonomous decision owner unknown.
- Supporting / enforcement mechanisms: role prompts, optional related-issue retrieval, published benchmark results and a paper.
- Closure path: similar-issue retrieval and bug context → present patch; not a documented future-environment sensing/options/adoption return loop.
- Why this is / is not agent-owned: present-issue retrieval and academic reporting are not sufficient S4 evidence.
- Evidence: [editor's related-issue retrieval instruction](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/editor.yml#L52-L90), [README research context](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/README.md).
- Basis: partial public boundary.
- Confidence: unresolved beyond the published operation.
- Caveats: do not count development of the paper or published model results as an autonomous S4 runtime.

## S5 — Policy and identity

- State: ?
- Function: legitimately adjudicate ultimate organizational purpose, ethos and policy disputes and bind subsequent operation.
- Disturbance / variety regulated: mismatched operator goals, hazardous code actions and conflicting role instructions.
- Decisive decision or feedback right: the user-supplied issue and maintainer-authored prompts constrain tasks; no identity-policy adjudication appears in recorded operation.
- Decision owner: human authors supply goals and role rules, but parent-loop legitimacy and an explicit post-decision return path within unpublished runtime are not verifiable.
- Supporting / enforcement mechanisms: manager's pre-specified plans, role-specific prohibitions and `submit` protocol.
- Closure path: supplied policy → tasks and submitted patch; no demonstrated ultimate-policy dispute → legitimate owner decision → binding revised operation.
- Why this is / is not agent-owned: an instruction to choose among predefined plans is not the right to set ultimate identity; the absence of implementation prevents a comprehensive S5-negative proof.
- Evidence: [manager constraints](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/manager.yml), [editor's no-test-code instruction](https://github.com/NL2Code/CodeR/blob/d63468344bc215bbabb8f0c1ba4af24897a946df/config/roles/editor.yml#L1-L47).
- Basis: published configuration only.
- Confidence: low for final state, high that no positive owner can be assigned from role prompts alone.
- Caveats: human-maintainer repository governance is outside the evaluated issue-solving recursion.

## Distributed OSS parent arrangement

The repository exposes a paper and run outputs, but does not contain a standing multisession organization where open-source contributors jointly govern executing CodeR copies. No cross-repository governance is borrowed into runtime S3/S4/S5, and no parent-modifier notation is justified by mere existence of maintainers.

## Self-hosted and non-human modes

Role templates describe command-line agents, while first-party deployment scripts and command implementations are not published at this frozen ref. Recorded traces show a non-human operational loop using generated commands and tool feedback. They do not establish supported local supervised S3/S4/S5 or fully agent-owned non-human metasystem modes.

## Recursion

Manager and specialist roles share a single issue repair episode. Predefined graph cells handle subprocess-like work, but the public evidence does not establish recursively viable suborganizations with their own management/strategic/policy loops.

## Variety and escalation

Issue context enters the chosen plan, model/tool feedback enters next code edits, and role success/failure paths return outcomes to manager-selected workflow edges. There is no concrete published trace of conflict-specific inter-S1 oscillation damping, an algedonic current-management escalation, S3 complementary audit, or organization-level policy ratification. Unlike an inspected complete implementation, these unproven paths stay `?`, not universal `—`.

## Evidence gaps

- Frozen Git tree contains **no implementation source or runnable first-party agent/manager scripts**; the referenced shell-command files and scheduler cannot be inspected or independently executed. This materially limits both positive and negative ownership claims.
- Trace output supports real model-selected S1 commands and feedback but does not prove generality, correctness or whole-system rights. The published SWE-bench results are not independent evidence for S2–S5 autonomy.
- All five metasystem states are `?` pending an accessible pinned implementation or sufficiently specific first-party operational receipts; the visible task graph alone cannot justify S2, S3 or S3*.
- No LLM-agent, model-provider or Browser quality tests were run; only repository inspection and deterministic Index scripts are authorized for this assessment stream.
