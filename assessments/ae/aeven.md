---
harness_id: aeven
project_name: Aeven
repository: https://github.com/Aeven-AI/Aeven
review_ref: 50e27b33594b7f0400fc666668fc1026c3fe7ca1
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Aeven

## Review boundary

- System in focus: The released Aeven application/session composition, including explicitly named optional account-installed skills from its bundled release catalog.
- Purpose and identity: Model-independent personal/work agent with connected tools, durable sessions and reusable procedures.
- Relevant environment: users, workspaces, model services, tools and the operational disturbances described below.
- Standard-distribution boundary: Official CLI/Web/desktop aeven preset and normal host/session services; supported optional installation of bundled avn-swarm, avn-best-of-n and avn-review-loop is included as a distinct skill-enabled mode.
- Credited operating / distribution surfaces: Native agent-loop, aeven preset, normal continuable subagent controls; catalog packaging/account installation and the three cited runtime skill instructions.
- Adjacent first-party surfaces excluded from ownership: packages/experimental Agent Teams/Inspector and source-checkout-only profiles, repository dogfood/contributor/CI work, disabled developer self-extension, disabled Codex/Claude subagent rows and imported providers internal agency.
- First-party operating / deployment modes considered: Default released aeven sessions plus account-installed catalog swarm/best-of-N/review-loop mode. The latter is optional and not claimed active in a fresh account. Source-only experimental Agent Teams examined to establish exclusion; no operational ownership borrowed from it.
- Recursion level: one deployed harness/composition and its work sessions; repository maintainers and external hosts are outside this operational recursion.
- Reviewed revision: `50e27b33594b7f0400fc666668fc1026c3fe7ca1`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (active Index pair; current Skills main calibration also consulted).

## Repository architecture

Aeven derives from DeepSeek Harness with retained attribution in NOTICE, but this assessment is of its exact own distribution. Cordis composes the first-party turn/step model/tool loop, durable session and subagent services, host integrations and per-session tools. The aeven preset selects native continuable spawn/fork workers, goals/workflows, compaction, memory and procedure learning. Release skill bundles become model-visible only after explicit account installation. Experimental Agent Teams are source-checkout-only and excluded from official payloads; optional Codex/Claude tools and developer mounting are disabled in the reviewed preset. Public maintainers own releases outside this task recursion.

## Operational model

Root and child model/tool actors produce user work. Default controls establish narrow current task-tree intervention; installed catalog skills additionally provide agent-owned write separation and a complementary author/reviewer correction loop. Those optional modes are credited because the release packages both instructions and supported installation/runtime wiring, not because the repository happens to contain development prompts. Automatic learning is traced independently and is not promoted to S4 from persistence alone.

## S1 — Operations

- State: A
- Function: Carry user tasks through first-party model/tool and continuable child work.
- Disturbance / variety regulated: Changing user objectives, tool failures, incomplete artifacts, interruptions and missing context.
- Decisive decision or feedback right: Choose next substantive tool/action, delegation or response from observed results.
- Decision owner: The Aeven session model actor, with first-party spawned/forked child actors.
- Supporting / enforcement mechanisms: Cordis plugin composition, queued turn/step driver, tool execution, durable session logs, filesystem/shell/browser/MCP and host permission gates.
- Closure path: Session log → request assembly → model tool calls → execution results → next step; child messages/reporting return to the parent.
- Why this is / is not agent-owned: The native loop owns iterative execution. Disabled Codex/Claude subagent rows and provider-internal control are not borrowed.
- Evidence: [packages/preset/agent-presets/presets/aeven/agent.cordis.yml](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/preset/agent-presets/presets/aeven/agent.cordis.yml); [packages/core/agent-loop/src/agent.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/core/agent-loop/src/agent.ts); [packages/core/agent-loop/src/tool-calls.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/core/agent-loop/src/tool-calls.ts); [packages/subagent/tool-subagent/src/index.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/subagent/tool-subagent/src/index.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.
- Boundary reachability: The released aeven preset mounts normal tools, native spawn/fork delegation and the first-party session loop; model/provider configuration completes ordinary deployment.

## S2 — Coordination

- State: A
- Function: Prevent writable interference between parallel work actors in the supported installed swarm/best-of-N mode.
- Disturbance / variety regulated: Concurrent workers or competing attempts would otherwise share writable artifacts and contaminate each other before selection.
- Decisive decision or feedback right: Choose nonoverlapping slices/separate output locations, keep attempts independent and decide subsequent retries/integration from returned evidence.
- Decision owner: The parent model following the installed shipped skill; native subagent actors execute the separated briefs.
- Supporting / enforcement mechanisms: avn-swarm and avn-best-of-n packaged instructions, runtime subagents/workflow tools, filesystem/worktree commands and evidence-bearing reports.
- Closure path: Parent allocates nonoverlapping briefs and private write locations → children act in their assigned locations → evidence/commit identity is checked → wrong/no-evidence results are rejected and respawned once or retained as gaps, then parent integrates accepted work.
- Why this is / is not agent-owned: This is explicit conflict attenuation with an agent-owned allocation/return policy, not S2 from generic messaging. No Agent Teams experimental service is needed.
- Evidence: [packages/skill/skill-catalog/authored/avn-swarm/SKILL.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/skill/skill-catalog/authored/avn-swarm/SKILL.md); [packages/skill/skill-catalog/authored/avn-best-of-n/SKILL.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/skill/skill-catalog/authored/avn-best-of-n/SKILL.md); [packages/skill/skill-catalog/README.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/skill/skill-catalog/README.md); [packages/skill/skill-catalog/catalog/index.json](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/skill/skill-catalog/catalog/index.json); [packages/host/account-integrations/src/index.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/host/account-integrations/src/index.ts); [packages/preset/agent-presets/presets/aeven/agent.cordis.yml](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/preset/agent-presets/presets/aeven/agent.cordis.yml).
- Basis: structural.
- Confidence: medium.
- Caveats: Optional account-installed catalog skills, not an always-active default guarantee; constraints are agent instructions, not filesystem sandbox proof..
- Boundary reachability: The official release skill catalog contains both ZIP bundles; Settings installCatalogSkill imports the bundled skill into account skills, which the supported session can load. Local bundle bytes were checked equal to authored instructions.

- Distinct S1 units: parallel native subagents, each with an independent slice or artifact attempt and verification outcome.
- Inter-S1 disturbance: shared writable state and attempt cross-contamination during concurrent work.
- Attenuating coordination relation: nonoverlapping slices, one output location per writing worker, no shared writable state and no pre-scoring access to other attempts.
- Feedback into subsequent S1 behaviour: commit/evidence checks decide one bounded respawn or a recorded gap; parent integration and final checks operate on accepted outputs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the skill explicitly changes ownership of write surfaces and the treatment of interfering/invalid outputs, beyond merely spawning or messaging workers.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current descendant commitments and intervene on behalf of the root task organization.
- Disturbance / variety regulated: Running/idle/ready descendants, corrupt or unavailable records, delayed work and tasks needing redirection or interruption.
- Decisive decision or feedback right: Choose which current descendant work to interrupt and which direct child to steer or continue after inspecting current state.
- Decision owner: The ancestor/root model actor within lineage-bound runtime authority.
- Supporting / enforcement mechanisms: list_agents descendants projection, live/durable status, send_message, interrupt_agent, completion notification and authoritative lineage checks.
- Closure path: Current tree/status/report → parent selects intervention/continuation → subagent service routes steering at a step boundary or requests cancellation → changed child activity and later reports return to the root.
- Why this is / is not agent-owned: The narrow credited function is current commitment regulation over the root task tree. It is not S3 from spawning alone, registry existence or a deterministic cancellation API without the model owner.
- Evidence: [packages/subagent/tool-subagent-control/src/list-agents.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/subagent/tool-subagent-control/src/list-agents.ts); [packages/subagent/tool-subagent-control/src/index.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/subagent/tool-subagent-control/src/index.ts); [packages/subagent/subagent/src/control.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/subagent/subagent/src/control.ts); [packages/subagent/subagent/src/continuation.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/subagent/subagent/src/continuation.ts); [packages/preset/agent-presets/presets/aeven/agent.cordis.yml](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/preset/agent-presets/presets/aeven/agent.cordis.yml).
- Basis: structural.
- Confidence: medium.
- Caveats: Interrupt is asynchronous, stops only the target current turn and does not stop its children or drain queued messages. No human parent modifier is inferred from browser steering..
- Boundary reachability: The default aeven preset mounts list/control alongside continuable spawn/fork children. These tools use the live calling agent and recorded lineage; no custom supervisor or experimental Team layer is needed.

- Whole-system current view: scope descendants traverses the complete root task tree with durable parent/depth, labels, live running/idle/ready states and explicit diagnostics; child reports provide task outcomes.
- Current-control decision scope: retain, redirect or interrupt descendant commitments within the root task. Deep descendants can be interrupted but only direct children can be messaged; this is not fleet/account-wide policy or mutable compute budgeting.

## S3* — Complementary audit

- State: A
- Function: Complement author claims with an independent raw-diff review and a returned correction/re-review loop in the installed review skill mode.
- Disturbance / variety regulated: Self-reported completion can hide bugs, wrong callers or goal failures.
- Decisive decision or feedback right: The fresh reviewer challenges the actual code/diff; the author accepts or rebuts findings with primary evidence, fixes accepted findings and returns the changed artifact for review.
- Decision owner: Separate fresh reviewer model plus author model with explicitly separated review/edit rights; a human resolves only an unresolved terminal dispute.
- Supporting / enforcement mechanisms: avn-review-loop packaged brief, fixed base/diff, raw code/tests, per-finding ledger, four-round bound and no-edit reviewer rule.
- Closure path: Author result → fresh-context read-only reviewer inspects raw changed code → APPROVE/CHANGES with file:line claims → author fixes/rebuts and reruns checks → reviewer rechecks open IDs/changed code; failures/timeouts are not approval.
- Why this is / is not agent-owned: The independently framed critic has materially different access to the artifact rather than repeating author prose; both judgment and returned correction are packaged instructions using supplied model actors. Deterministic CI and routine Ralph reports are not the credited auditor.
- Evidence: [packages/skill/skill-catalog/authored/avn-review-loop/SKILL.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/skill/skill-catalog/authored/avn-review-loop/SKILL.md); [packages/skill/skill-catalog/catalog/index.json](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/skill/skill-catalog/catalog/index.json); [packages/skill/skill-catalog/README.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/skill/skill-catalog/README.md); [packages/host/account-integrations/src/index.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/host/account-integrations/src/index.ts); [packages/preset/agent-presets/presets/aeven/agent.cordis.yml](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/preset/agent-presets/presets/aeven/agent.cordis.yml).
- Basis: structural.
- Confidence: medium.
- Caveats: Optional installed skill mode, not automatic S3* for every session. Actual run compliance or independent approval is not asserted by this source assessment..
- Boundary reachability: The release catalog ships avn-review-loop.zip, verified byte-identical to its authored SKILL.md. Supported Settings/account installation and skill loading make the workflow reachable without custom review code; it can use the default fresh spawn provider.

- Claim being audited: correctness of the current change against its declared goal, including callers and evidence.
- Ordinary reporting path: author statement, result and ordinary checks.
- Complementary access path: fresh reviewer independently reads git diff at the fixed base and surrounding raw source, checking claims against goal/tests.
- Independence boundary: no inherited author history, no reviewer edits/commits/PR writes, one reviewer at a time and no author edits while review runs; same-model fresh context is allowed but model diversity is not guaranteed.
- Who acts on findings: author model records agreement/rebuttal with evidence, fixes and reruns checks; unresolved repeated disagreement stops for the user without claiming approval.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective harness adaptation function is supplied at this boundary.
- Disturbance / variety regulated: The environmental/authority variety potentially addressed by the inspected paths.
- Decisive decision or feedback right: No function-specific decisive right established in the assessed supported distribution.
- Decision owner: No qualifying agent or parent owner established for this function.
- Supporting / enforcement mechanisms: Background procedure distillation, user correction/slowness feedback, memory recall, capability candidates, lessons-to-checks and disabled self-extension tools.
- Closure path: No corresponding function-specific organizational return loop established.
- Why this is / is not agent-owned: The shipped learning path derives reusable procedures from completed tasks and corrections; it does not itself investigate prospective environmental alternatives or arbitrate them with present capability. Tool/web research remains S1 task execution unless a distinct adaptation case/return is established. Source-only developer self-extension and experimental packages do not donate an S4 mode.
- Evidence: [packages/capability/tool-capability/src/learner.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/capability/tool-capability/src/learner.ts); [packages/capability/tool-capability/src/recall.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/capability/tool-capability/src/recall.ts); [packages/capability/tool-capability/src/index.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/capability/tool-capability/src/index.ts); [packages/capability/tool-capability/README.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/capability/tool-capability/README.md); [packages/preset/agent-presets/presets/aeven/agent.cordis.yml](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/preset/agent-presets/presets/aeven/agent.cordis.yml); [packages/skill/skill-catalog/authored/avn-lessons/SKILL.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/skill/skill-catalog/authored/avn-lessons/SKILL.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: packages/capability/tool-capability/src/learner.ts, packages/capability/tool-capability/src/recall.ts, packages/capability/tool-capability/src/index.ts, packages/capability/tool-capability/README.md, packages/preset/agent-presets/presets/aeven/agent.cordis.yml, packages/skill/skill-catalog/authored/avn-lessons/SKILL.md and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Background procedure distillation, user correction/slowness feedback, memory recall, capability candidates, lessons-to-checks and disabled self-extension tools.
- Why no material first-party path remains: The shipped learning path derives reusable procedures from completed tasks and corrections; it does not itself investigate prospective environmental alternatives or arbitrate them with present capability. Tool/web research remains S1 task execution unless a distinct adaptation case/return is established. Source-only developer self-extension and experimental packages do not donate an S4 mode.

## S5 — Policy and identity

- State: —
- Function: No identity or ultimate-policy arbitration loop is supplied.
- Disturbance / variety regulated: The environmental/authority variety potentially addressed by the inspected paths.
- Decisive decision or feedback right: No function-specific decisive right established in the assessed supported distribution.
- Decision owner: No qualifying agent or parent owner established for this function.
- Supporting / enforcement mechanisms: Persona/preferences, permission approvals, plan/goal requests, plugin/preset configuration and optional skill installation.
- Closure path: No corresponding function-specific organizational return loop established.
- Why this is / is not agent-owned: These define or configure the current assistant and authorize ordinary tasks/extensions; no runtime identity/ultimate-policy dispute is routed to a legitimate final authority and returned as a function-specific governing decision. Maintainer governance of Aeven releases is adjacent, not an operational S5 owner.
- Evidence: [packages/preset/agent-presets/presets/aeven/agent.cordis.yml](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/preset/agent-presets/presets/aeven/agent.cordis.yml); [docs/architecture.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/docs/architecture.md); [packages/core/agent-loop/src/agent.ts](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/core/agent-loop/src/agent.ts); [packages/experimental/README.md](https://github.com/Aeven-AI/Aeven/blob/50e27b33594b7f0400fc666668fc1026c3fe7ca1/packages/experimental/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: packages/preset/agent-presets/presets/aeven/agent.cordis.yml, docs/architecture.md, packages/core/agent-loop/src/agent.ts, packages/experimental/README.md and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Persona/preferences, permission approvals, plan/goal requests, plugin/preset configuration and optional skill installation.
- Why no material first-party path remains: These define or configure the current assistant and authorize ordinary tasks/extensions; no runtime identity/ultimate-policy dispute is routed to a legitimate final authority and returned as a function-specific governing decision. Maintainer governance of Aeven releases is adjacent, not an operational S5 owner.

## Distributed OSS parent arrangement

Public maintainers own development and release governance. Their repository process is adjacent to the installed harness; contributor plurality does not establish operational parent S3/S4/S5 at this recursion. No additional closed parent-governed function is established by ordinary configuration or approvals.

## Self-hosted and non-human modes

Default released aeven sessions plus account-installed catalog swarm/best-of-N/review-loop mode. The latter is optional and not claimed active in a fresh account. Source-only experimental Agent Teams examined to establish exclusion; no operational ownership borrowed from it. Model choice, permission settings and deployment administration alone do not establish ultimate-policy governance. Unimplemented extensions do not receive constructor credit.

## Recursion

Subagents are task decomposition; no recursively viable suborganization is established.

## Variety and escalation

Tool/model failures, permission limits and context exhaustion return as observations, refusals, pauses or terminal results. These channels support local recovery; they are not additional VSM functions or automatic algedonic evidence.

## Evidence gaps

No live provider or product E2E run was performed. Conclusions concern reachable source-level ownership at the exact frozen revision, not performance, deployment reliability or benchmark quality. Bounded absence claims cover the stated supported distribution, not arbitrary future extensions.
