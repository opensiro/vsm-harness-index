---
harness_id: teaql-agent-kit
project_name: TeaQL Agent Kit
repository: https://github.com/teaql/teaql-agent-kit
review_ref: 270baae75b4482ed51c45d44b5777930451cda03
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TeaQL Agent Kit

## Review boundary

- System in focus: the installed TeaQL Agent Kit, especially its supported protected Pi native-CLI / SDK agent execution mode, context-lifecycle and policy extensions, host-controlled tools, and the `build-teaql-app` development workflow.
- Purpose and identity: equip an existing coding agent to develop TeaQL applications from a model-first specification while constraining its context access, file mutation and completion evidence.
- Relevant environment: user software requirements, project model and source, evaluation/generation service, model provider, permitted code and diagnostics, host-approved tools and human application review.
- Standard-distribution boundary: first-party Skill plus `@teaql/agent-context-kit`, its Pi native CLI bootstrap and host-tool integration. Pi SDK/provider, TeaQL service, adopter project and operator's trusted configuration remain explicit dependencies.
- Credited operating / distribution surfaces: [`runPiContextCli` / `createPiContextCliExtension`](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-cli.ts), [`createContextPolicyPiSession`](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-context.ts), controlled file/tool operations, [completion continuation](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-completion.ts), [trusted TeaQL capability tools](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/integrations/pi-teaql/tools.mjs) and the packaged [development Skill](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/skills/build-teaql-app/SKILL.md).
- Adjacent first-party surfaces excluded from ownership: documentation-only agent logos and unsupported adapters, downstream generated TeaQL application governance, the Robot Task Board showcase, release/CI/contributor workflows, test fixtures, and evidence of external hosts outside enabled entry points.
- First-party operating / deployment modes considered: instructions in a user's existing coding agent; installable Context Kit lifecycle adapters; dedicated read-only Pi SDK session; protected native Pi CLI with controlled writes; optional host-registered build/test and TeaQL evaluate/assist/generate tools; opt-in OpenCode V2 strict plugin; unsupported/limited agent integrations.
- Recursion level: one protected model-driven application-development session, not the whole TeaQL company, service or a portfolio of coding agents.
- Reviewed revision: `270baae75b4482ed51c45d44b5777930451cda03`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [top-level README](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/README.md) separates a model→evaluate→generate→implement→verify Skill from deterministic context, permission and verification adapters. The Skill provides agent-directed instructions and repair budgets; by itself a Markdown Skill is not an autonomous actor. The [activation matrix](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/docs/agent-feature-activation.md) distinguishes ordinary plugins from the operationally stronger protected Pi and OpenCode modes and expressly disclaims complete enforcement in Codex/Claude/Cursor guidance-only modes.

The supported [native Pi CLI bootstrap](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-cli.ts) launches the installed Pi model session with first-party extensions, a bounded tool catalog, controlled file edits and host-registered capabilities. It disables generic Bash, MCP, delegation and arbitrary resource loading, but retains Pi's actual user→model→tool→model turn loop. The [SDK mode](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-context.ts) constructs a dedicated Pi session with guarded read/search and optional host commands. The autonomous model is supplied by the installed Pi runtime/provider; the Kit is a first-party **packaging and operational integration** of that model runtime, not a claim to have implemented the model itself.

[`LifecycleSession`](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/session.ts) projects tagged context into a request-local view; [`ContextFiles`](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/context-files.ts), [`FileAccessPolicy`](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/file-policy.ts) and the [Pi file tools](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-cli.ts) enforce paths and marker-derived read exclusion. Optional [TeaQL tools](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/integrations/pi-teaql/tools.mjs) expose fixed evaluate/generate/Assist/build/test operations; the trusted host chooses allowed programs and project roots. The [completion guard](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-completion.ts) launches missing host-approved checks after a premature model stop following edits, then continues the model turn with real results. It does not independently choose a strategic objective.

## Operational model

The human/adopter states a development goal and provisions Pi, a model and permissible tools. The installed protected Pi session lets its model inspect permitted project context, decide file edits and invoke authorized TeaQL/build/test tools, observe returned results and revise work. The Kit supplies an operationally reachable autonomous S1 loop through the host; the model owns task-content and tool-choice discretion, whereas trusted host config and policy code determine what is allowed. Documented real-model verification is corroborative but not a new live run by this assessment. No distinct ongoing sibling S1 units or metasystem parent is established within one such session.

**Proposed disposition: included**, vector `A — — — — —`. The positive S1 depends on the supported integrated Pi mode, not the mere ability to paste a prompt into unrelated hosts; other functions below are tested against their specific organizational thresholds.

## S1 — Operations

- State: A
- Function: turn a user software request into model-selected project modeling, code edits, tool invocations and verified application-development deliverables.
- Disturbance / variety regulated: incomplete domain requirements, model evaluation errors, generated API details, compiler diagnostics, missing files and evolving intermediate implementation state.
- Decisive decision or feedback right: select next development action, allowed file edits, evaluation or generation command and repair based on observations until the current task is addressed.
- Decision owner: autonomous coding model in the first-party supported protected Pi session; the operator supplies goal/credentials and host policy, Pi supplies model/tool runtime and Kit supplies the controlled integration.
- Supporting / enforcement mechanisms: Skill phase rules, lifecycle view, marker-aware read guard, trusted fixed commands, zero-error model-generation gate, mutation restrictions and automatic verification continuation.
- Closure path: user request → Pi model proposes read/edit/evaluate/build/test → Kit-registered guarded tool executes and returns bounded result → Pi model revises action or reports truthful completion.
- Boundary reachability: `runPiContextCli` calls Pi's `main` with `createPiContextCliExtension`; that extension registers actual guarded tools and model-context/turn handlers. `createContextPolicyPiSession` is an alternate first-party SDK entry; no unrelated coding-agent installation is silently credited.
- Why this is / is not agent-owned: without the model there is still a policy/file/test executor, but no adaptive selection of business model, implementation or repair; those operational decisions are model-owned. A host-controlled verification check is not promoted into independent S3 ownership.
- Evidence: [Pi protected session bootstrap](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-cli.ts), [SDK session integration](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-context.ts), [development Skill](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/skills/build-teaql-app/SKILL.md), [recorded supported mode](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/docs/agent-feature-activation.md).
- Basis: structural runtime wiring and documented real-model supported-mode observations.
- Confidence: high for S1 reachability, not a measured model quality claim.
- Caveats: model, credentials and TeaQL remote service are dependencies; host tools are opt-in and not automatically present in every install. The guided prompt-only mode does not by itself show Kit-owned agency.

## S2 — Coordination

- State: —
- Function: no evidenced coordination of a concrete interference or oscillation among distinct ongoing operational S1 units in the scoped session.
- Disturbance / variety regulated: tool failures, competing file restrictions and request-context size, none shown as inter-S1 collision.
- Decisive decision or feedback right: reconcile conflicting sibling S1 actions and feed a revised arrangement back into their subsequent behavior; not supplied by the Kit's shipped protected session.
- Decision owner: human/operator fixes tool rights; deterministic lifecycle and policy adapters enforce bounds. There is no S2-specific AI or constructor actor evidenced.
- Supporting / enforcement mechanisms: host hooks, sequential tool execution, protected reads, context-lifecycle tags, adapter/subagent context inheritance where supported.
- Closure path: policy denial or tool result returns to the same coding agent, not a corrective coordination agreement among distinct S1 units.
- Why this is / is not agent-owned: delegation hooks and tool scheduling are not evidence of a relationship mediating identified S1 interference.
- Evidence: [adapters/compatibility](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/README.md), [Pi tools](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-cli.ts), [lifecycle sessions](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/session.ts).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: adopter organizations can install multiple agents and supply a separate coordinator; that is not automatically part of this Kit.

### Absence scope

- Surfaces inspected: supported Pi/OpenCode modes, packaged agent adapters, lifecycle/session state, child-agent context inheritance and controlled tool dispatch.
- Plausible first-party paths checked: child-agent inheritance as S2, serial host tool scheduling as collision attenuation, shared context blocks as peer coordination.
- Why no material first-party path remains: no specific two-S1 disturbance, coordination discretion and returned multi-unit adjustment are implemented in these paths.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-commitment/resource control over multiple S1 operations at the declared one-session recursion.
- Disturbance / variety regulated: tool access violations, oversized outputs, incomplete verification and repeated non-tool promises.
- Decisive decision or feedback right: assess a whole organization's current priorities/resources and intervene across operating divisions; not evidenced.
- Decision owner: host/operator preconfigures restrictions and checks; model owns local task execution, while deterministic guards enforce configured response limits.
- Supporting / enforcement mechanisms: permission policy, `MAX_ROUNDS` completion recovery, session restore, diagnostic caps and repeated-reply recovery.
- Closure path: check results and denials return to the same agent for local repair; no whole-system discretionary current-control decision returns to distinct S1 units.
- Why this is / is not agent-owned: completion enforcement may override premature task stop but does not allocate resources/commitments across the system; host policy is not itself a supervising S3 parent decision.
- Evidence: [completion guard](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-completion.ts), [progress recovery](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-progress.ts), [controlled tasks](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/controlled-tasks.ts).
- Basis: bounded structural negative, including parent-mode check.
- Confidence: medium-high.
- Caveats: a human can revise operator config, but no supported whole-current supervisory channel and decision-return loop is evidenced by that ability.

### Absence scope

- Surfaces inspected: protected Pi hooks, SDK session, completion state, progress recovery, host tool allow-list, OpenCode strict mode and project registration.
- Plausible first-party paths checked: verification policy as S3, automated recovery as current supervisory intervention, trusted human config as S3(P).
- Why no material first-party path remains: local procedural guards enforce preselected constraints without whole-system views or discretionary portfolio-control rights at this recursion.

## S3* — Complementary audit

- State: —
- Function: no established sufficiently independent systemic audit of operational reality with findings returned to whole-system control.
- Disturbance / variety regulated: incorrect code, false model completion and masked compiler/test failures.
- Decisive decision or feedback right: independently inspect claims through an alternate reality-access path, adjudicate operational drift and initiate system-level corrective control.
- Decision owner: tests/build tools produce real results; host completion hook deterministically runs configured checks. The coding model remains ordinary implementer/reviewer of those results.
- Supporting / enforcement mechanisms: host-executed build and test commands, bounded diagnostics, automatic missing-verification checks after edits, audit-context advice in the Skill.
- Closure path: actual compiler/test outcome → host-generated continuation message → same task model repairs/reports. This is routine task QA rather than separately governed complementary audit of ongoing S1 reality.
- Why this is / is not agent-owned: external test observation is stronger than self-report, but independence of an information source and compulsory local verification alone do not establish the S3* organizational function and owner.
- Evidence: [completion guard](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-completion.ts), [fixed Rust test/build tools](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/integrations/pi-teaql/tools.mjs), [verification record](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/docs/t003-business-repair-verification.md).
- Basis: bounded structural negative.
- Confidence: medium.
- Caveats: a separately constituted independent auditor that consumes raw evidence could change this result at a different application boundary.

### Absence scope

- Surfaces inspected: completion, fixed build/test wrappers, diagnostic and policy filters, test evidence reports and Skill report requirements.
- Plausible first-party paths checked: host compile/test as complementary audit; automatic stop verification as independent reviewer; audit trail from TeaQL application runtime as S3*.
- Why no material first-party path remains: these inspect task output inside the same implementation loop and route routine failures to that implementer, without separate independent operational auditor/whole-system corrective control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no standing future-environment intelligence and capability-option return to current organizational control.
- Disturbance / variety regulated: changes to API versions, toolchain availability, model-generated designs and future project requirements.
- Decisive decision or feedback right: sense external/future shifts, assess alternatives and send an accepted adaptation to operating capability.
- Decision owner: current model may fetch up-to-date Assist and repair the requested application; external future policy/capability decisions stay with adopter/maintainer.
- Supporting / enforcement mechanisms: progressive service Assist, model evaluation, generation tools, skill instructions and adapter compatibility matrix.
- Closure path: provider documentation and compilation diagnostics inform task production, not a future-facing options decision returned to a supervisory S3.
- Why this is / is not agent-owned: learning the current generated API and editing current application code is operational adaptation to a task, not the organizational outside-and-then relation.
- Evidence: [development Skill](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/skills/build-teaql-app/SKILL.md), [generation/Assist tools](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/integrations/pi-teaql/tools.mjs), [feature activation](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/docs/agent-feature-activation.md).
- Basis: bounded negative, parent-mode checked.
- Confidence: medium-high.
- Caveats: a future monitoring/adaptation operator could place these tools within a separate S4 system.

### Absence scope

- Surfaces inspected: Skill phase workflow, model evaluation and Assist, agent context lifecycle, compatibility matrix, adapters and host configuration.
- Plausible first-party paths checked: progressive API discovery as external intelligence; retry/model repair as future adaptation; operator updates to host tools as S4(P).
- Why no material first-party path remains: no recurring prospective option assessment and authoritative return into persistent system capability is evidenced.

## S5 — Policy and identity

- State: —
- Function: no runtime closure of ultimate identity/policy conflicts for the agent organization under assessment.
- Disturbance / variety regulated: prohibited file access, untrusted marker text, unsafe tool/resource loading, incomplete attestations and project-scope changes.
- Decisive decision or feedback right: settle a genuine identity/ultimate-policy matter by legitimate authority and return a binding policy to ongoing operation.
- Decision owner: trusted host config/operator sets allowed resource modules and edit roots before the run; deterministic tools enforce. Human task feedback is an input, not a first-party constitutional parent loop.
- Supporting / enforcement mechanisms: immutable host tool selection, fail-closed marker handling, read/write boundary, command denial, user permission requests, parent-supplied enterprise policy.
- Closure path: blocked tools return non-retryable feedback and the model changes local action, but no identity-level issue → legitimate authority → authoritative policy change → returned runtime constraint is first-party implemented.
- Why this is / is not agent-owned: static hard guardrails are meaningful safety mechanisms yet do not grant the model or parent within the Kit an ultimate-policy decision path.
- Evidence: [Pi policy bootstrap](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-cli.ts), [read guard](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/read-guard.ts), [trusted host tools](https://github.com/teaql/teaql-agent-kit/blob/270baae75b4482ed51c45d44b5777930451cda03/packages/agent-context-kit/src/adapters/pi-host-tools.ts).
- Basis: bounded structural negative, including parent-mode check.
- Confidence: medium-high.
- Caveats: adopter's organization may have an actual S5 policy authority; its decisions cannot be borrowed solely because the Kit reads its static configuration.

### Absence scope

- Surfaces inspected: Pi/OpenCode policy entry points, context/file guards, host tool config, human prompt/review and contributor/security material.
- Plausible first-party paths checked: trusted operator configuration as S5(P), blocked action escalation as policy adjudication, Skill requirements as system identity.
- Why no material first-party path remains: permitted operations are predetermined by host policy; the shipped mode does not route a new ultimate-policy issue to a legitimate authority and install a returned binding decision during continued operation.

## Distributed OSS parent arrangement

Independent adopters may install context adapters inside multiple third-party coding agents. No shared TeaQL Agent Kit operating organization, central resource authority or cross-installation legitimate S5 decision loop is established by that distribution. Repository maintainers and contributor approvals belong to product development, not the assessed protected coding session.

## Self-hosted and non-human modes

The documented local Pi/OpenCode protected modes run with model decisions subject to a trusted operator-configured capability boundary. The protected native Pi mode has an actual autonomous S1 task loop; the dedicated read-only SDK mode does not imply a write-capable development outcome. Configurable hosts or multiple installed adapters do not by themselves establish S3/S4/S5 `(P)` functions.

## Recursion

A model-development run can sit as an S1 cell inside a larger development team or organization. Its lifecycle blocks, projects and host adapters are not recursive viable organizations merely because they nest sessions or inherit context across subagents. An adopter-specific higher recursion would require its own decision-right evidence.

## Variety and escalation

The Skill attenuates open-ended implementation variety into modeling, semantic evaluation, generated API, implementation and verification phases. Model tool choice and generated source amplify operational options; hard file policies, marker pruning, fixed command targets and bounded diagnostics attenuate unsafe tool/context variety. Policy denials, failed builds and premature-stop completion reports go back to the active agent/operator as task exceptions, not a separately established algedonic channel into S3/S4/S5.

## Evidence gaps

This is pinned first-party source/mode review, not a fresh live Pi model trial or TeaQL service benchmark. Local upstream Python suite passed 2/2; JavaScript contract suite could not be fully exercised because the local checkout lacks package dependency `typebox` (one contract passed, two entrypoints failed import), not because application behavior was tested and found wrong. The documented source-based real-model records distinguish their scoped outcomes, including zero-test runs. Operational S1 is credited only to supported installed Pi integration with a model/provider, not to guidance-only plugins or arbitrary external coding agents.
