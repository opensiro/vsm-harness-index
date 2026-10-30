---
harness_id: coding-orchestrator
project_name: Coding Orchestrator
repository: https://github.com/davesheffer/coding-orchestrator
review_ref: dca682d7a1bc99c6b83508ad03186b2015085e8a
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Coding Orchestrator

## Review boundary

- System in focus: one installed Coding Orchestrator role-and-rules bundle controlling a bounded coding project session in Claude Code or Codex, with model-operated main agent and scoped scout/runner/builder/critic children.
- Purpose and identity: supply economical role-routed agentic coding, explicit evidence/verification, conflict-safe assignment, independent adversarial audit and continuation under client context limits.
- Relevant environment: user software tasks, changing repository contents, tests and runtime tools, parallel child work, errors and incomplete reports, context exhaustion, client permission inheritance and risky outputs.
- Standard-distribution boundary: the actively installed global Claude `CLAUDE.md`/`agents/*.md` or Codex `AGENTS.md`/`agents/*.toml`, optional executable restricted Windows `agent-run.py`, first-party relay/role guard/PR and report utilities. Underlying Claude Code/Codex inference and built-in task machinery are external but are explicitly composed and directed through shipped role/operating contracts.
- Credited operating / distribution surfaces: `claude/install.py`, `codex/install.py`, `CLAUDE.md` managed orchestrator block, `codex/AGENTS.md` managed block, `agents/{scout,runner,builder,critic}.md`, `codex/agents/*.toml`, `bin/agent-run.py`, `bin/role-guard.py`, `bin/ro.py`, `bin/agent-report.py`, `relay/relay.py`, and optional `mods/mission-control` UI only in separately installed mode.
- Adjacent first-party surfaces excluded from ownership: root `AGENTS.md` developer instructions, root `CLAUDE.md` auto-generated Hunch block outside the installed managed block, tests and previous-release fixtures, benchmark/trial comparisons, `docs/optimization-research.md`, contributor governance/CI/release packaging, VS Code handoff-bridge examples and external Jev model/API internals. Actual host CLI's unrelated policy/delegation mechanisms are not automatically credited.
- First-party operating / deployment modes considered: Claude installed native named roles; Codex installed native named roles and manual restricted process fallback; Windows-only separately audited `agent-run.py` with exactly scoped optional network exception; optional paid Jev routing hooks; explicitly installed Mission Control; context rollover in Claude or Codex. Native model/sandbox availability varies by host.
- Recursion level: one host-model-controlled coding request/project portfolio with independently acting scout, runner, builder and critic subprocesses/child sessions as bounded subunits, not the global population of installations or the external vendors.
- Reviewed revision: `dca682d7a1bc99c6b83508ad03186b2015085e8a`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Coding Orchestrator is an installable instruction-and-role pack, not a provider-hosted general agent platform. The Claude and Codex installers install a marked main-session operating charter and four executable native role definitions; preserving user-owned instructions is part of installation, not an independent model runtime. `scout` locates and summarizes, `runner` executes exact checks, `builder` implements a bounded design, and `critic` examines risky code/claims from fresh context. All return an evidence/confidence/unverified report. The model main session retains design, root-cause investigation, task allocation, whole-current verification, priority and final acceptance. Native client subagent processes supply the actual model/tool loop; an optional Windows-only `agent-run.py` launches separate scoped Codex CLI agents after explicit effective permission probes and model identity checks.

The first-party Claude scout `role-guard.py` narrows Bash to `ro.py` read verbs, while Codex profile files and the launcher declare/no-op external tool surfaces and try enforced sandboxing. These controls are not substitutes for checking actual inherited client permissions. Parent-owned role and permission policy, no-overlap assignment and fresh-critic review are instructions that a capable host model must follow; the bundle is candid that Claude critic/builder shell restrictions can be weaker than prompt intent. `relay.py` carries context-budget observation and bounded handoff to another session, with optional Jev classifier hooks, while Mission Control is a separately installed observation UI. Root's Hunch block is deliberately not copied by the Claude installer and does not give this bundle its own organizational strategy/identity function.

Primary source: [project README](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/README.md), [Claude installed charter](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/CLAUDE.md), [Codex installed charter](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/AGENTS.md), [Codex installer](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/install.py), [Claude installer](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/claude/install.py), [native-client validation limits](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/docs/client-validation.md).

## Operational model

The host model receives a user coding problem, decides scope and design, delegates small independent units to shipped native roles, observes evidence and code changes, uses runner results and critic findings to correct or accept, and returns a completed answer. Agent roles have separate model-owned tasks but not organizational permission to publish, deploy or change scope; release/destructive actions remain in the main session under actual user authority. Reading and test execution can overlap, but work modifying shared source must have disjoint ownership or be made sequential to prevent interference. The installed charter explicitly instructs the host to wait for each result, inspect builder diffs, verify real exit codes, and consult a fresh-context adversarial critic on risky/irreversible work. The relay makes future session continuity possible but does not decide the project's long-horizon strategic capabilities. Optional Jev assists routing/risk hints but is not a bundled autonomous governance actor.

## S1 — Operations

- State: A
- Function: autonomous coding/research/test work by the host-model agent and installed native scout/runner/builder agents with bounded task/tool loops.
- Disturbance / variety regulated: uncertain repository structure, source changes, failing checks, implementation alternatives and task-local tool feedback.
- Decisive decision or feedback right: the main session model designs/solves ambiguous work, the scout selects what to investigate within its brief, the builder chooses concrete edits/validation for a specified change, and the runner interprets exact check outcome without changing the task's scope.
- Decision owner: Claude Code/Codex main-session and named-child models reachable through installed first-party role contracts, not the Python installer or preconfigured model strings.
- Supporting / enforcement mechanisms: installed role files, native subagent invocation, explicit model/effort/brief, read-only helper/guard, sandbox checks where supported, typed outcome report and optional Windows launcher.
- Closure path: user objective → main model investigation/design and bounded role assignment → child-model tools/read/check/edit feedback → RESULT/EVIDENCE/CONFIDENCE/UNVERIFIED → main model checks, corrects or completes task.
- Boundary reachability: default installers put the role definitions and main charter into the selected assistant home; starting a supported Claude/Codex session exposes the named roles. The Windows launcher separately supplies a real restricted CLI fallback, while native host execution is conditional on role discovery and effective permissions.
- Why this is / is not agent-owned: removing the model leaves static roles, installers, command/report helpers and sandbox policy but no task-specific decisions or coding output. The external client executes inference, while the installed first-party definitions directly shape real normal-operation model roles.
- Evidence: [role dispatch rules](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/AGENTS.md), [Claude role routing](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/CLAUDE.md), [builder role](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/agents/builder.md), [scout role](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/agents/scout.md), [launch restrictions](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/bin/agent-run.py).
- Basis: explicit and structural.
- Confidence: medium-high for distributed role construction; provider-authenticated live role selection and effective sandbox enforcement were not run here.
- Caveats: an optional Windows launcher cannot be silently assumed to work on Linux/macOS, and mere role model metadata is weaker than observing a live session. The role pack's own validation record describes these native gaps.

## S2 — Coordination

- State: A
- Function: direct attenuation of overlapping file edits and order-dependent interference among several independent coding S1 subunits.
- Disturbance / variety regulated: concurrent builders/writers touching one file or repository without disjoint ownership, overlapping edits and approvals during unresolved prior work, and invalid test results produced before a dependency completes.
- Decisive decision or feedback right: the main model assigns disjoint paths and bounded briefs to independent subagents, keeps conflicting edits/dependencies sequential, and changes assignment/wait order after builder diffs, check exits and verification indicate overlap or dependency failure.
- Decision owner: installed main-session orchestration model, constrained by real user scope and native permission boundaries; deterministic role safety guards are not the coordination decision maker.
- Supporting / enforcement mechanisms: role separation (scout/critic read-only, runner check-only, builder scoped writing), explicit file-ownership clauses, dependency/wait rules, actual diffs and result reports, host's task completion notices, and conditional checked sandbox boundaries.
- Closure path: proposed independent work may touch the same mutable code or require an earlier fix → main model gives non-overlapping ownership or delays the dependent worker → observed diff/check/report returns → main model corrects assignment or waits/replans → later model-owned S1 edits use the revised scope/order.
- Boundary reachability: both installed main-session charters explicitly instruct disjoint file ownership, parallelism only for independent units, sequential edits/dependencies and checking actual child results; native named agents are reachable after installation. No unrelated external work manager is required.
- Why this is / is not agent-owned: the main model decides which changes are independent and how to respond to observed overlap; static role restrictions and a guard may reduce the chance of unsafe writes but cannot select a domain-specific collision resolution.
- Distinct S1 units: at least two concurrently or sequentially handed-off native child models (for example separate scout/runner and builder branches, or two scoped builders) working on one coding project under the same main model.
- Inter-S1 disturbance: two builders can produce conflicting edits to shared files, while a runner checking an incomplete dependency can report stale results that mislead the later builder/parent.
- Attenuating coordination relation: first-party parent role contract with disjoint file ownership, specified briefs and ordered dependency/editor actions, plus returned diffs/reports and correction by the main model.
- Feedback into subsequent S1 behaviour: the main model inspects observed builder diffs and real runner exits, then narrows or revises a worker's file scope, reassigns the fix or delays the next writer until conflicting work is reconciled.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: disjoint ownership and dependent-write/check ordering are aimed at a concrete interference among independently acting code-changing S1 roles, not merely routing routine low-cost tasks.
- Evidence: [Codex no-overlap/task/dependency contract](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/AGENTS.md), [Claude task partition](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/CLAUDE.md), [builder scoped writing](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/agents/builder.md), [Codex named role definition](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/agents/builder.toml).
- Basis: explicit skill-driven inter-writer operating policy.
- Confidence: medium for model-owned S2 in correctly followed multi-role operation; no runtime global file-claim database or automatic source-collision detector exists.
- Caveats: generic task delegation or read-only scout/critic isolation alone is not S2; this claim rests on distinct changing/observing S1 units and source-overlap prevention/correction through the parent model. A single writer mode does not exercise inter-S1 coordination.

## S3 — Inside-and-now control

- State: A
- Function: whole-current project control by the main model over delegated task commitments, uncertainty, verification obligations and risk/acceptance interventions.
- Disturbance / variety regulated: competing current tasks, unverified work, weak reports, elapsed context, child sandbox failures, failed tests, risk/irreversible actions and incomplete handoffs.
- Decisive decision or feedback right: main model chooses whether to delegate or handle directly, allocates roles/briefs, analyzes child reports/diffs and risk, requires another check/critic, changes task plan/assignment and accepts or returns work for correction.
- Decision owner: installed main-session orchestration model. A real user retains authorization over pushes and irreversible actions, but no distinct parent-governed whole-current S3 mode is inferred from occasional permission approval.
- Supporting / enforcement mechanisms: `RESULT/EVIDENCE/CONFIDENCE/UNVERIFIED` reports, role constraints, verification commands, client child-task state, optional Mission Control in-flight UI, `agent-report.py`, relay context gauge/handoff, Jev route/guard hints and actual client permission enforcement.
- Closure path: current parallel child outcomes/changed files, low-confidence reports and check exits → model main-session portfolio judgment → correction/delegation/escalation/critic/pass decision → revised child work, accepted code or bounded new session continuation.
- Boundary reachability: the main-session charter is installed and loaded as the normal operating instruction; native role responses return to that session, optional UI/launcher provide further observations. Its job is explicitly design, judgment, verification and final response rather than merely waiting for a model child to finish.
- Why this is / is not agent-owned: static rules and context thresholds advise or constrain; the host model owns what to do with the whole current request and whether evidence is sufficient. A dashboard, hook or permission check does not exercise that judgment alone.
- Whole-system current view: main conversation receives each launched child result and task status, and can inspect diffs/checks; optional Mission Control displays the active model/agent timeline and report cards. The optional Windows launcher aggregates its own bounded run reports, not arbitrary independent client sessions.
- Current-control decision scope: split/reassign project work, sequence disjoint edits, require direct validation or critic review, stop an unsafe course, and choose release readiness within user-granted authority.
- Evidence: [Codex parent-owned supervision](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/AGENTS.md), [Claude parent-owned supervision](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/CLAUDE.md), [Mission Control current observation](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/mods/mission-control/README.md), [agent report helper](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/bin/agent-report.py), [role handoff contracts](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/agents/runner.md).
- Basis: explicit operating ownership, supported by native role/report interfaces.
- Confidence: medium-high for supported agent-caller mode.
- Caveats: Claude shell restrictions may be merely advisory under inherited permissions; actual client permissions and model availability must be verified on deployment. The Mission Control mod is optional and observability, not an independent controller.

## S3* — Complementary audit

- State: A
- Function: model-owned independent challenge of risky code changes and correctness/security claims using direct source and verification evidence.
- Disturbance / variety regulated: an implementer's unsupported confidence, a passing-but-irrelevant test, concurrency/security bugs missed by builder and main agent, and accidental self-review of an asserted fix.
- Decisive decision or feedback right: a separately instantiated `critic` model with a fresh brief independently judges the exact diff/source and produces `SHIP | FIX FIRST | RETHINK` findings; the main model then resolves/acts on the evidence before claiming the risky work done.
- Decision owner: shipped critic role running as a distinct Claude/Codex model agent for independent audit judgment; main model owns remediation and final acceptance, rather than the builder or an automatic CI lint gate.
- Supporting / enforcement mechanisms: fresh-context adversarial role prompts, read-only policy (with effective-enforcement caveats), exact diff/base and claim, expanding through callers/error paths/tests, failure scenarios, line-anchored findings, typed verdict and main-session correction loop.
- Closure path: builder/main proposes risky change or completion claim → separately briefed critic reads direct changed code and adjacent paths → independent finding/SHIP/FIX FIRST/RETHINK returns → main model verifies, requests changes or documents conscious remaining risk before acceptance.
- Boundary reachability: Claude installer places `agents/critic.md`, Codex installer places the native `critic.toml`; both installed main charters explicitly require critic review for risky or irreversible work. It does not rely on a repo maintainer PR process or a hypothetical external assessor.
- Why this is / is not agent-owned: the critic model owns a substantive adversarial audit verdict from complementary direct evidence; the static role manifest/guards and main model's acceptance are separate functions. The builder's own test/report is not substituted for an independent critic.
- Claim being audited: that a proposed coding change or high-risk operation is correct, safe and supported by the stated check evidence.
- Ordinary reporting path: builder or runner returns RESULT/EVIDENCE/CONFIDENCE/UNVERIFIED and main reads the actual work/checks.
- Complementary access path: distinct fresh-context critic receives the exact diff/base and claim, reads actual code/callers/error cases/tests without accepting author reasoning, and reports concrete adverse scenarios with file/line evidence.
- Independence boundary: critic has separate role, model/prompt/brief and read-only posture, no shared author conclusions as settled truth; practical sandbox isolation depends on actual client/host and may be unverified even when role files state read-only.
- Who acts on findings: the main orchestration model investigates blocker/major/minor evidence, orders corrective work, reruns checks or explicitly withholds final acceptance; an automatic critic response does not publish changes.
- Evidence: [Claude critic charter](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/agents/critic.md), [Codex critic definition](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/agents/critic.toml), [fresh critic routing/feedback](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/AGENTS.md), [Claude critic acceptance](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/CLAUDE.md), [native validation boundaries](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/docs/client-validation.md).
- Basis: explicit and structural.
- Confidence: medium-high for distinct installed critical review path, subject to client runtime configuration.
- Caveats: runtime enforcement for Claude `critic` may remain instruction-level under permissive inherited modes, and no paid critic ran in this assessment. Optional user refusal or unsupported native role availability may prevent a specific deployment from exercising S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed organizational future-environment sensing → adaptation-option generation → decision → returned operating capability loop is supplied for the assessed host coding project.
- Disturbance / variety regulated: model tiers, provider availability, token use and future tooling change appear as configuration/routing concerns, not a functionally closed S4 strategy system.
- Decisive decision or feedback right: no first-party S4 owner is bound to a proactive future adaptation cycle; agent choices over current work and context rollover are S3/continuity decisions.
- Decision owner: neither autonomous system-model intelligence authority nor a qualifying distinct parent-governed S4 mode is established within the installed bundle.
- Supporting / enforcement mechanisms: model-routing table and fallback rules, context gauge/rollover, optional Jev classification, `agent-report.py`, benchmarks/optimization research and human configuration updates.
- Closure path: no evidenced future/external distinction → novel adaptation option → authoritative selection → returned change to current system capability. A context threshold may trigger a fresh session but preserves current objectives instead of adapting future organizational capabilities.
- Why this is / is not agent-owned: the host model can choose a different helper or consult benchmarks, but the released bundle does not supply a strategic outside-and-then intelligence role and completed adaptation return loop.
- Evidence: [role/routing and continuity rules](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/AGENTS.md), [Claude relay instructions](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/CLAUDE.md), [relay code](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/relay/relay.py), [Jev routing](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/bin/jev-route.py), [benchmarks](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/benchmarks/README.md).
- Basis: bounded first-party absence.
- Confidence: medium-high for examined installation and runtime paths.
- Caveats: separate external corporate/user strategy may change the role bundle; the repo's benchmark and optimization materials are not an installed, agent-owned prospective capability governance loop.

### Absence scope

- Surfaces inspected: installed Claude/Codex parent charters, four role definitions, model fallback/permission launcher, relay/context gauge, opt-in Jev router, optional Mission Control, local reports, benchmarks and research notes.
- Plausible first-party paths checked: periodic task/model selection, provider-unavailable fallback, learned model effectiveness from reports, the Jev task-shift classifier, context-zone rollover and contributor-led future optimization.
- Why no material first-party path remains: these operate on current-task routing, safety/continuity, retrospective trials or developer research; none embeds an environmental future intelligence actor with capability-level alternatives, decisive selection and returned implemented change into current S3.

## S5 — Policy and identity

- State: —
- Function: no first-party autonomous or parent-governed ultimate identity/policy decision and subsequent charter-return loop is installed for the coding system.
- Disturbance / variety regulated: task scope, authorization, tool/network boundaries, project requirements and model availability are externally configured and handled as task/permission governance, not identity disputes.
- Decisive decision or feedback right: user grants or withholds outward/destructive actions and any optional permission fallback; main agent respects the configured role policy, but cannot adjudicate its own ultimate identity or bind the user/project through an S5 resolution institution.
- Decision owner: no legitimate S5 mode owner within the installed runtime is demonstrated. User-owned config/approval remains at an external parent but is not a full S5 function-specific return path merely because permission checks exist.
- Supporting / enforcement mechanisms: installed `AGENTS`/`CLAUDE` instructions, role sandbox settings, user-owned `agent-routing.json` exception list, external client permissions, Jev risk gate and optional Hunch outside the actual installed managed block.
- Closure path: blocked tool or permission fallback request → user/current-model task decision → resumed/denied particular operation; no defined ultimate-policy issue → legitimate authoritative verdict → binding identity charter update → subsequent operation loop.
- Why this is / is not agent-owned: an agent following constraints has S1/S3 operating rights but no supreme authority to change the system's charter. A user can reinstall/change settings, but installing code and occasional approval are not S5 parent governance.
- Evidence: [Codex role permission and consent boundaries](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/codex/AGENTS.md), [user-local policy handling](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/bin/agent-run.py), [Claude parent authority limits](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/CLAUDE.md), [installed managed-block boundary](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/claude/install.py), [opt-in Jev guard](https://github.com/davesheffer/coding-orchestrator/blob/dca682d7a1bc99c6b83508ad03186b2015085e8a/bin/jev-guard.py).
- Basis: bounded first-party absence.
- Confidence: high for no shipped identity-level return forum at declared boundary.
- Caveats: independent OSS users may each govern their assistant installations; do not aggregate their private settings into an organization-wide S5 or borrow the separate Hunch system as this bundle's own installed authority.

### Absence scope

- Surfaces inspected: installer-managed instruction blocks, role manifests, user-local launcher authorization, native client permission guidance, optional Jev gate, relay handoff, root developer/optional Hunch materials and contributor docs.
- Plausible first-party paths checked: user permission/approval gates for outward actions, saved network exceptions, role policy updates, task-shift prompts, Hunch-styled constraints and contributor policy decisions.
- Why no material first-party path remains: all paths either constrain a current operation, depend on optional external systems or describe maintainer/configuration work; none supplies an operationally closed ultimate-identity decision by an autonomous or legitimate parent owner whose resolution returns into the running harness charter.

## Recursion

The primary recursion is one current main-model coding project with native child role agents as subordinate operational units. The main model is not every role's hidden provider internals. The `critic` has a complementary audit relation to project work; its safety posture cannot be treated as S5 policy authority. Separately installed users/OSS contributors do not share one runtime or legitimate parent-governed system merely because they use the same public bundle. Optional Jev, Hunch, Mission Control and VS Code bridge capabilities remain support/external boundaries rather than an inferred hierarchy of additional VSM decision owners.

## Variety and escalation

Different model roles and occasional separate restricted runs add operational variety without transferring outward-facing authority from the main model. Weak or incomplete child evidence returns to the main model; an implementation uncertainty escalates back from builder to the main designer, and a risky result goes to a fresh critic. If native permission isolation cannot be verified the bundle directs the host to keep work in the main session or seek tightly scoped, explicit user authorization, not to bypass a denial. Context pressure may trigger a handoff with current task state. These are immediate control, audit and continuity closures, not a first-party S4 adaptation or S5 identity program.

## Evidence gaps

- No live paid/connected Claude or Codex model-agent dispatch was made. The repo's own `docs/client-validation.md` documents experimental availability and effective inherited permission gaps; offline tests validate code/config, not comprehensive real role discovery or sandboxing.
- S2 is conditional on the model caller actually enforcing disjoint file ownership and feedback while coordinating multiple S1s; no first-party global source-file lock or conflict resolver is claimed. A reader-only delegation does not alone witness S2.
- S3* is a genuine installed fresh-context critic path, but any specific client under `bypassPermissions`/overridden sandbox needs effective read-only verification; the role file alone is not OS enforcement.
- Optional Jev, Mission Control and separate Hunch integration may add evidence/guardrails, but this review did not attribute external provider reasoning, paid third-party policy models or uninstalled adjacent developer-only tools as first-party authority.
