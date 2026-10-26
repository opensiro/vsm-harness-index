---
harness_id: harness-for-codex
project_name: Harness for Codex
repository: https://github.com/revfactory/codex-harness
review_ref: 80f8217b5b6d3f220a31f05f9c0adaf09dac40f4
reviewed_at: 2026-10-26
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

# Harness for Codex

## Review boundary

- System in focus: One project-local Harness for Codex installation after explicit `$harness` invocation, running a bounded software/content work objective with its parent Codex orchestrator and actual project subagent roles. Plugin installation alone and the upstream `revfactory/harness` ecosystem are not counted as an active runtime.
- Purpose and identity: Build project-specific reusable agent/skill infrastructure and then organize current project work among narrow native Codex workers, coordinate conflicting ownership, independently examine delivered source evidence, correct faults and verify completion.
- Relevant environment: Real project source and acceptance criteria, overlapping worker edits, cross-task dependencies, stale inputs, contradictory interface assumptions, child lifecycle/capacity, tool permissions, reviewer/QA findings, malformed records and explicit human constraints.
- Standard-distribution boundary: Released Codex marketplace/plugin manifest, canonical `skills/harness/SKILL.md`, shipped project-specific role TOMLs, `.codex/config.toml`, native parent/child Codex execution contract, `run.py`/`communication.py`/validation utilities, and optional predefined five-role installer. The external Codex host owns model inference, native spawn/send/stop tools and effective sandbox; no arbitrary external model capabilities are imported beyond these role-bound uses.
- Credited operating / distribution surfaces: [Codex plugin manifest](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.codex-plugin/plugin.json), [marketplace](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.agents/plugins/marketplace.json), [canonical installed harness skill](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/SKILL.md), [first-party multi-agent protocol](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/docs/multi-agent.md), [read-only reviewer role](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.codex/agents/harness-reviewer.toml), [bounded worker role](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.codex/agents/harness-worker.toml), [run-record and dependency lifecycle](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/scripts/run.py).
- Adjacent first-party surfaces excluded from ownership: `archive/upstream/` source and benchmarks, unused sample service-migration project, optional live smoke itself, repository maintainer CI and migration audit artifacts. A TOML agent definition without project-local installation and an exposed native Codex role is not credited as already executing. Structural run state, native session status, peer logs and a user approval are not autonomous S2/S3/S3*/S5 judgments by themselves.
- First-party operating / deployment modes: Explicit `$harness` plugin invocation in target project; actual role generation plus compatible native Codex subagents; optional installer that preloads five roles; parent-led independent fan-out, dependency waves, source-bound integration, separate review/QA, bounded rework and resume. If role discovery/native spawning is unavailable, the skill specifies sequential parent fallback **without** falsely claiming multi-agent execution.
- Recursion level: One project-local harness-supported work organization / bounded task run. Worker agent tasks are its S1 cells; source maintainer project, customer company and generic Codex platform are separate recursions.
- Reviewed revision: `revfactory/codex-harness@80f8217b5b6d3f220a31f05f9c0adaf09dac40f4` (`main`), plugin manifest v0.1.0, Codex CLI compatibility evidence version 0.153.4.
- Observation date: 2026-10-26; frozen first-party source, repo-native deterministic tests, no new live Codex/LLM trials.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The plugin's explicit invocation resolves the **target project**, creates/updates `.codex/agents` roles, reusable skills, pointers and config while preserving existing files, and then uses a model-backed parent Codex session to pursue the actual requested work. The first-party five-role team distinguishes explorer/architect (read-only), worker (owned source), reviewer (independent read-only diff inspection), and QA (checks and assigned test/artifact writes). The parent has an explicit current-run ledger with task plans, fingerprints, dependency readiness, actual native child IDs, status, acceptance evidence and peer events. It checks true tool exposure, tests one standby spawn, distributes bounded packets with disjoint ownership, dynamically assigns subsequent ready tasks, reconciles shared interfaces and conflicts, inspects results, routes specific review findings back to the owner and verifies terminal work. `run.py` and `communication.py` persist/enforce and correlate these choices; they neither spawn an agent nor infer that recording a message means it was delivered. Native Codex model/tool host executes the actual parent/child reasoning and tool actions. The source explicitly refuses to treat repository installer tests as proof of live model orchestration.

## Operational model

The first-party harness contracts model-backed roles with distinct task, coordination, present-control and audit rights. The same parent may exercise both conflict-specific S2 settlement and whole-current S3 control, but these are evidenced as **different decisions**: a concrete two-worker shared-file/interface collision is redirected through one owner/contract revision (S2), whereas current allocation, priority, capacity, dependency and integration decisions serve the overall run (S3). The separate reviewer accesses original code/diff, challenges the implementation report and returns findings to the parent for worker repair; QA separately checks observable behavior. This does not give the first-party harness ultimate company purpose or an anticipatory external-environment S4 owner. Positive autonomy claims concern **supported actual installed-and-invoked mode**, not files sitting passively in plugin cache.

## S1 — Operations

- State: A
- Function: Explore source, design bounded implementation, write assigned code/tests or conduct narrowly scoped technical verification as actual project work units.
- Disturbance / variety regulated: Unknown source architecture, technical errors, implementation alternatives, failing project tests, individual task acceptance details and changed inputs.
- Decisive decision or feedback right: The project's model-backed explorer/architect/worker/QA agents choose source inspection, code modifications and test actions within a refreshed task packet and role permissions, returning findings, files and checks.
- Decision owner: Native Codex subagent instantiated with a first-party `harness_*` role and assigned project-local packet; parent coordinates, and generic Codex model/tool runtime supplies inference/execution transport.
- Supporting / enforcement mechanisms: `.codex/agents` TOML, plugin/skill invocation, work scopes, `workspace-write` or `read-only` role sandbox requests, native spawn/follow-up, run/input/result records, actual agent IDs and test commands.
- Closure path: User goal → `$harness` target-project setup and model parent task breakdown → role-specific packet to native child → model-selected project read/write/check work → evidence/actual output to parent → accepted result or returned correction.
- Boundary reachability: Plugin marketplace and skill explicitly enable target-project bootstrap; `docs/multi-agent.md` and `skills/harness/SKILL.md` describe actual native spawn and current-project prerequisites, including first-spawn preflight and operational fallback. Seed roles are valid TOMLs installed into the project, not merely benchmark sample agents.
- Why this is / is not agent-owned: The Python run ledger can check contracts and fingerprints but cannot select code edits or semantic analysis. The first-party agent role plus model execution is the operational owner; an unstarted agent definition alone would not be.
- Evidence: [installed plugin and `$harness` invocation](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/README.md#install-as-a-plugin-recommended); [harness Phase 2/3 and first child preflight](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/SKILL.md); [bounded worker role](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.codex/agents/harness-worker.toml); [read-only explorer and QA roles](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/docs/multi-agent.md).
- Basis: Explicit installed model-backed native worker path and differentiated job rights; dynamic task actions returned to parent.
- Confidence: High for shipped wiring, medium for live behavior across user-specific Codex clients and permission settings.
- Caveats: Actual native role discovery, spawn capability, parent cwd and runtime limits must pass; source includes guarded fallback that must not be reported as a live multi-agent PASS. This assessment itself did not execute any model task.

## S2 — Coordination

- State: A
- Function: Suppress actual/structurally evidenced collisions between two current task workers' shared-file ownership, interface expectations or write succession, and return a revised conflict-free contract to affected S1s.
- Disturbance / variety regulated: Concurrent worker A and B both trying to update a shared config/type/lockfile, incompatible interface assumptions, one worker's dependency output changing while another has begun, or competing edits to a shared workspace.
- Decisive decision or feedback right: The first-party parent is directed to assign one owner to shared files, serialize overlapping work, inspect a combined diff when concurrent contributions conflict, negotiate affected interface contracts and **reassign/return** updates to the appropriate workers. Peers report collisions and propose changes but do not silently overwrite.
- Decision owner: Model-backed parent using explicit collaboration/ownership rules when mediating a concrete inter-worker conflict; deterministic dependency ledger and messaging helper support but do not decide semantic repair.
- Supporting / enforcement mechanisms: Disjoint `ownership` file sets, shared-interface agreements, actual native peer messages, parent-contract confirmation, ready/dependency checks, worktree preservation instruction, change fingerprint invalidation and recorded ownership transfers.
- Closure path: Worker A's discovered shared-interface/file conflict with Worker B → direct peer event/parent report → parent examines source and shared contract, selects owner/serial order or revised interface → new current packets/explicit native follow-ups alter A/B actions → integrated source/test evidence closes the collision.
- Boundary reachability: `docs/multi-agent.md` explicitly mandates single ownership for shared types/manifests/lockfiles and says out-of-scope edits go to the parent for reassignment/serialization. Its failure handling separately instructs the parent to inspect combined diffs after actual concurrent edits collide. `harness_worker` specifically reports a concurrent ownership overlap, and canonical skill Phase 5 makes parent contract confirmation/worker handoff part of supported runtime behavior.
- Why this is / is not agent-owned: The S2 claim is **not** credit for a mailbox, task DAG or parent delegation. The parent makes a discretionary dispute-specific ownership/interface reconciliation based on different workers' potentially incompatible changes; scripts merely record ownership and deliver refreshed packets.
- Distinct S1 units: Two or more native `harness_worker` agents assigned separate project modules/parts of a dependency wave; independently execute and return their artifacts.
- Inter-S1 disturbance: Both need the same shared interface/config/file, or one worker's new contract invalidates another's assumptions; concurrent edits would corrupt or contradict the integrated source.
- Attenuating coordination relation: Single shared-file owner plus negotiated interface and serial handoff, with parent examination/reassignment if conflict is observed, not indiscriminate shared-write access.
- Feedback into subsequent S1 behaviour: Parent-confirmed revised ownership/dependencies and newly refreshed task packets dictate which worker may change the contested file and when dependent agents may proceed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The intervention addresses a **named inter-worker interference** — overlapping writes/shared interface contradiction — and changes both workers' subsequent allowed work; generic ready-queue execution or communication logging would not settle the contested source contract.
- Evidence: [shared types and out-of-ownership return](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/docs/multi-agent.md#task-packet); [collision handling and parent reconciliation](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/docs/multi-agent.md#failure-handling); [worker explicit ownership-overlap return](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.codex/agents/harness-worker.toml); [skill Phase 2 and Phase 5 parent contract confirmation](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/SKILL.md).
- Basis: Differentiated first-party parent-owned inter-S1 collision mitigation with explicit returned file/contract changes.
- Confidence: Medium; behavior is a real installed model-role contract, not independently measured actual conflict-resolution performance.
- Caveats: `run.py` metadata validation alone does not choose a conflict resolution. File scopes constrain behavior by instructions, not OS-enforced per-path ACLs; agent mistakes remain possible and user policies may force manual repair.

## S3 — Inside-and-now control

- State: A
- Function: Govern this project's current run across worker cells: priority/ready choices, commitment/ownership, available subagent capacity, integration, correction rounds and terminal acceptance.
- Disturbance / variety regulated: Global task dependency drift, incomplete or stale outputs, multiple workers contending for current resources, model/tool incompatibilities, uneven progress, review/QA failures and inability to satisfy acceptance criteria.
- Decisive decision or feedback right: The parent Codex session reads the whole current goal, plan, dependencies, input fingerprints, accepted decisions, actual native agent states and returned evidence; it selects tasks to dispatch within capacity, verifies predecessor completion, returns specific defects to workers or performs permitted fallback, and accepts/blocks final integration.
- Decision owner: First-party harness-configured parent model session, distinct from the deterministic `run.py ready/result/resume` checks and from an individual implementation worker.
- Supporting / enforcement mechanisms: Run plan and task packets, actual native spawn IDs, 3-thread requested capacity with real runtime recheck, agents registry, dependencies and fingerprints, explicit message correlation, bounded retry limits and completion validator.
- Closure path: Parent receives current state and worker/reviewer reports → chooses ready assignments, current interface/commitment correction, retry or escalation → native follow-up or agent launch directs S1 work → updated outputs/status, original tests and reviewer findings return → parent re-evaluates integration/closure.
- Boundary reachability: Canonical skill Phase 5 makes the parent the active executor of task dispatch, current capacity control and final work acceptance after explicit invocation; repository `.codex/config.toml` and AGENTS pointer route the parent to the skill. Both plugin and installer modes have a documented path to actual Codex role/tool use.
- Why this is / is not agent-owned: Merely storing a plan, rate-limiting workers or printing a ready queue would not choose semantic task priorities, reconcile present interface changes or decide review-driven worker rework. Those choices are assigned to the executing model parent.
- Whole-system current view: The one project run's objective, input fingerprints, dependency DAG, contracts, all registered live worker states, results, shared-file ownership, review and QA evidence, known blockers and remaining budget.
- Current-control decision scope: Which task/role runs now, reallocation after failure/capacity, accepted interface changes, dependency readiness, updated work packets, bounded verification/rework and final current-run outcome; not product-market strategy or enterprise identity.
- Evidence: [parent role and actual scheduling/handoffs](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/docs/multi-agent.md#scheduling-and-handoff); [Phase 5 integration and decision path](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/SKILL.md); [run registry and input freshness rules](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/scripts/run.py); [configuration and target-project activation](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.codex/config.toml).
- Basis: Active parent model with current-run-wide resource/commitment and rework decisions; deterministic state gives auditability, not autonomy on its own.
- Confidence: Medium-high for the first-party mandate, moderate for live runtime compatibility in arbitrary Codex deployments.
- Caveats: Parent must be in target-project cwd with actual role discovery/spawn tools; the source warns that absent native tooling leads to a limited fallback and no fabricated multi-agent success.

## S3* — Complementary audit

- State: A
- Function: Challenge an implementer's source/correctness/completeness claims through a separate read-only reviewer and return causal findings into parent-controlled correction.
- Disturbance / variety regulated: Incorrect or overstated worker success claims, missed regressions, mismatched interfaces, unsafe permissions assumptions, implementation artifacts that fail acceptance despite an apparently completed task.
- Decisive decision or feedback right: Separately instantiated `harness_reviewer` has a read-only context/role and directly examines assigned diff, surrounding code and acceptance criteria; it issues severity/file/line/trigger/impact/remedy findings to the parent. QA may independently run boundary tests and return actual check evidence.
- Decision owner: The first-party reviewer role executed as its own native Codex subagent; parent uses returned findings to choose corrective assignment, while `validate.py` only checks structural/evidence completeness.
- Supporting / enforcement mechanisms: `harness_reviewer.toml` sandbox request read-only, direct diff/code inspection contract, refreshed review packet, no implementation rights, independent child context where supported, distinct QA role, returned findings and parent recheck loop.
- Closure path: Worker edits project and reports success → parent commissions distinct read-only reviewer after integration → reviewer independently inspects real source/diff and acceptance boundaries → findings returned directly to parent → parent sends defects back to owning worker → changes and re-review/test outcomes update terminal acceptance.
- Boundary reachability: Shipped reviewer TOML and canonical skill Phase 5/6 specify independent review after modules/integration. `docs/multi-agent.md` explicitly invokes reviewer/QA and routes defects to owning workers; plugin installation with actual native role use can instantiate the reviewer without developing a new capability. This is a normal bounded mode, not an external optional code-review vendor.
- Why this is / is not agent-owned: Reviewer makes new semantic judgments from original code evidence, rather than validating the implementer's own response or passing a static schema. The read-only role cannot silently rewrite its target change during review.
- Claim being audited: Worker/parent's assertion that the changed code and current integration satisfy specified behavior and acceptance criteria.
- Ordinary reporting path: Worker result status, summary, changed files, own test report and current-run ledger.
- Complementary access path: Distinct reviewer reads actual source/diff and criteria directly; QA can run observable tests independently, with findings not restricted to the worker's summary.
- Independence boundary: Dedicated `harness_reviewer` native role/context and requested read-only sandbox; shared Codex provider/models are possible, effective runtime policy may differ and the parent chooses reviewer task scope.
- Who acts on findings: Parent owns acceptance and routes confirmed defects back to the implementation owner; worker implements corrections, then parent rechecks relevant boundary tests/audit.
- Evidence: [reviewer original diff and independent findings contract](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.codex/agents/harness-reviewer.toml); [QA role limits](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/.codex/agents/harness-qa.toml); [integrate/review/route corrections](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/docs/multi-agent.md#scheduling-and-handoff); [Phase 6 verification and rework](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/SKILL.md).
- Basis: First-party, separate reviewer with complementary raw artifact access and returned implementation correction loop.
- Confidence: High for specified audit role/feedback, not measured reviewer effectiveness.
- Caveats: A reviewer with read-only role may need a separately configured runtime to achieve effective isolation; no proof of model/vendor independence or live successful audit was generated by this Index assessment.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would autonomously scan the changing future environment, develop strategic capability options and return them to this task organization's current operating capability.
- Disturbance / variety regulated: Future model/tool ecosystem, user markets and external technology shifts beyond the declared project-local current work objective.
- Decisive decision or feedback right: Phase 0/1 inspects the target project's current source, Phase 2 chooses reusable local agent architecture, and Phase 7 handles user-requested drift/maintenance. No distinct future/outside intelligence owner with a standing prospective return loop is established at the current-run recursion.
- Decision owner: Parent project operator instructs harness creation/updating and sets enduring purpose; first-party parent selects current local role/tool design to execute the requested task.
- Supporting / enforcement mechanisms: Domain audit, role/skill creation, six architecture templates, explicit subsequent modification/drift review, retained project-local role instructions and validations.
- Closure path: Current project inspection leads to reusable roles and skills used for the requested project tasks; later user-triggered audit can revise them. This is project-local capability provisioning, not an autonomous externally prospective strategy-to-current S3 return loop.
- Boundary reachability: The explicit factory capability is real and operating, but targets a known current project and user request; generic potential use for future work does not show future external sensing and option selection.
- Why this is / is not agent-owned: Model-backed local harness design can be agent-owned S1 engineering work and may affect later executions, but that alone lacks the future environmental distinction, adaptation-option choice and S3 conversation required for S4.
- Evidence: [Phase 0/1 source audit and domain analysis](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/SKILL.md); [Phase 7 on-demand evolution and drift](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/SKILL.md); [actual bounded invocation contract](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/README.md#install-as-a-plugin-recommended).
- Basis: Negative for external/future strategic intelligence; legitimate agent-authored present task's reusable infrastructure distinguished.
- Confidence: Medium.
- Caveats: At a differently defined long-term harness-maintenance organization, Phase 7 plus an explicit future environment sensing agent would merit a separate S4 review; no such owner was proven here.

### Absence scope

- Surfaces inspected: Domain audit, six agent-team design patterns, role/skill generation, task resume, reference docs, Phase 7 drift and maintenance, project installer and Codex compatibility checks.
- Plausible first-party paths checked: Model vendor/tool future change monitoring, autonomous capability redesign, prospective strategic option comparison, an S4-to-S3 adaptation mandate and reusable role regeneration.
- Why no material first-party path remains: All inspected activities are requested project analysis, compatibility for actual runtime or later human-invoked maintenance; no standing outside-and-then future-model decision loop was established within this one work organization.

## S5 — Policy and identity

- State: —
- Function: Would adjudicate the ultimate identity and legitimate governing purpose of the project organization, with binding return to current work.
- Disturbance / variety regulated: Deep disputes about mission, legitimate parent authority, principal values or constitutional constraints beyond ordinary code/task permissions.
- Decisive decision or feedback right: User request establishes the project/harness purpose, and inherited Codex tool/sandbox permissions determine allowable operations; the parent enforces current task contracts and can escalate, but does not originate ultimate policy.
- Decision owner: Human project owner/operator and applicable higher-level Codex/user policy remain outside the first-party current work-run organization.
- Supporting / enforcement mechanisms: Role sandbox requests, skill boundaries, user approval/consent, Codex parent session, project-local `AGENTS.md`, target-workdir safety, forbidden privilege escalation and tool availability checks.
- Closure path: Parent follows existing user authorization and role permissions and may stop/escalate work; no evidence of an identity dispute deliberated and returned as an enduring policy decision across subsequent projects.
- Boundary reachability: First-party permission and target-project checks are reachable and explicit, but they enforce already accepted instructions rather than empowering a separate legitimate-policy actor.
- Why this is / is not agent-owned: Model role's current acceptance decisions and framework instruction texts are not authority to change organizational purpose; inherited permissions and human approvals are constraints, not a first-party S5 choice.
- Evidence: [user explicit invocation and project scope](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/skills/harness/SKILL.md); [parent responsibilities and platform permissions](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/docs/multi-agent.md#boundaries-and-verification); [AGENTS project guidance](https://github.com/revfactory/codex-harness/blob/80f8217b5b6d3f220a31f05f9c0adaf09dac40f4/AGENTS.md).
- Basis: Negative for ultimate identity-policy authority at one project-local run recursion.
- Confidence: Medium-high.
- Caveats: Parent model's final delivery answer and a user's approval are current task/parent inputs, not automatically published `S5=P`.

### Absence scope

- Surfaces inspected: Plugin invocation, role permissions, inherited model/sandbox config, AGENTS pointer, parent escalation, project validation, user consent and integration/acceptance rights.
- Plausible first-party paths checked: Ultimate mission conflict, stakeholder legitimacy, project identity change, constitutional purpose arbitration and binding future policy return.
- Why no material first-party path remains: Observed first-party rights select tasks, reconcile worker conflicts, verify code or obey user-defined limits; no durable self-owned ultimate-purpose policy deliberator was found.

## Distributed OSS parent arrangement

The human project owner, Codex runtime, installed Harness for Codex role contracts and upstream maintainers are separable. First-party parent model rights exist only when a target-project session discovers/executes the skill and agents. Neither parent helper scripts nor maintainer CI are imported as higher-recursion policy governance. Ordinary operator permission to merge or request a harness is not enough to publish `P`.

## Self-hosted and non-human modes

The system is project-local and can run non-human parent/child Codex roles with a user-approved installation. Dynamic role creation, bounded three-thread native pool, fresh task packets and separate reviewer are supported; actual role exposure/spawn and effective permissions must be verified on the user's Codex runtime. If those are unavailable, the parent can do bounded work sequentially and must leave required native tests unresolved rather than fake child records. Neither installed plugin metadata nor success of Python validation by itself proves a non-human run.

## Recursion

One target project/run is the organization: explorer, implementers, reviewer and QA are differentiated operational/audit cells under the active parent. The same parent may own S2 conflict settlement and S3 overall current-control decisions, but only when it exercises each specific feedback relation. The factory's reusable roles may be used in later runs; company strategy, vendor model policy and upstream product maintenance remain external.

## Variety and escalation

The project goal is decomposed into disjoint source ownership and stable input packets. Inter-worker shared-interface collisions are brought back to the parent, whose revised contract prevents overwrite and changes subsequent worker assignments. The parent handles current capacity, dependency and evidence variety, then invites a separate read-only reviewer and QA to challenge source claims. Failed outcomes are routed to the responsible worker for bounded rework; true missing Codex runtime tools and user authorization limits are escalated without fabricating success.

## Evidence gaps

- Frozen first-party plugin source inspected; no new live Codex/model/Browser session, independent-review quality experiment or real runtime smoke executed for this Index batch.
- Repository-native deterministic verification was run locally: `python3 scripts/validate.py --project .` PASS (five agent definitions/one skill, no errors), `python3 -m unittest discover -s tests -q` **97/97 PASS**. These tests check code/installer/validator behavior, not autonomous agent judgment; upstream README's older live-smoke assertions were not rerun or treated as this assessment's measurements.
- S2=A is narrowly the parent-mediated **specific shared-file/interface conflict** path, not the existence of chat, task ordering or a manager title; co-location with S3 does not imply all communication is S2.
- S3=A is the activated model parent using the full run state to select current assignments, correction and integration, not `run.py ready`'s deterministic queue or static skill installation.
- S3*=A uses a distinct direct-diff read-only reviewer with findings returned to parent and implementer; effective sandbox and provider independence vary with the Codex runtime.
- Native role discovery may require a fresh project-root session; if tools or parent context are unavailable, the explicitly specified fallback cannot substantiate the positive multi-agent execution path on that particular deployment.
